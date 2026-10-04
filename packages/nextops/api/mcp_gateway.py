"""Private verified-TLS MCP client; original user/target credentials never cross here."""

from __future__ import annotations

import asyncio
import json
import ssl
from datetime import timedelta
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit
from uuid import uuid4

import httpx
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

from nextops.api.request_context import CALL_CORRELATION
from nextops.application.errors import ApplicationError
from nextops.connectors.mcp import COMPAT_TOOLS, McpSourceGateway
from nextops.contracts.errors import ErrorCode
from nextops.contracts.incidents import IncidentEvidence
from nextops.contracts.monitoring import MonitoringIncidentContext, MonitoringSummary
from nextops.contracts.source_catalog import GatewayReadRequest
from nextops.contracts.sources import SourceEvidence, SourceReadOperation, SourceReadRequest

MAX_HTTP_REPLY_BYTES = 524_288  # MCP contains both structured and text copies of bounded evidence.


class BoundedTlsTransport(httpx.AsyncBaseTransport):
    def __init__(self, context: ssl.SSLContext) -> None:
        self._inner = httpx.AsyncHTTPTransport(verify=context, retries=0)

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        response = await self._inner.handle_async_request(request)
        raw = bytearray()
        try:
            if response.headers.get("content-encoding", "identity") != "identity":
                raise ApplicationError(
                    ErrorCode.DEPENDENCY_UNAVAILABLE, "connector.mcp_encoding_denied"
                )
            if 300 <= response.status_code < 400:
                raise ApplicationError(
                    ErrorCode.DEPENDENCY_UNAVAILABLE, "connector.mcp_redirect_denied"
                )
            async for chunk in response.aiter_raw():
                raw.extend(chunk)
                if len(raw) > MAX_HTTP_REPLY_BYTES:
                    raise ApplicationError(
                        ErrorCode.DEPENDENCY_UNAVAILABLE, "connector.mcp_output_invalid"
                    )
            return httpx.Response(
                response.status_code, headers=response.headers, content=bytes(raw), request=request
            )
        finally:
            await response.aclose()

    async def aclose(self) -> None:
        await self._inner.aclose()


class TlsMcpGateway:
    def __init__(self, url: str, ca: Path, secret: str) -> None:
        origin = urlsplit(url)
        if (
            origin.scheme != "https"
            or origin.path != "/mcp/"
            or not origin.hostname
            or origin.username
            or origin.password
            or origin.query
            or origin.fragment
            or not 32 <= len(secret) <= 512
        ):
            raise ValueError("fixed verified HTTPS MCP endpoint required")
        self._url, self._ca, self._secret = url, ca, secret
        self._active = asyncio.Semaphore(2)

    async def _invoke(
        self,
        tool: str | None,
        args: dict[str, Any],
        source_request: SourceReadRequest | None = None,
        operation: SourceReadOperation = "summary",
    ) -> Any:
        if self._active.locked():
            raise ApplicationError(ErrorCode.OVERLOADED, "connector.source_overloaded")
        async with self._active:
            try:
                async with asyncio.timeout(65):
                    context = ssl.create_default_context(cafile=str(self._ca))
                    async with (
                        httpx.AsyncClient(
                            transport=BoundedTlsTransport(context),
                            trust_env=False,
                            follow_redirects=False,
                            headers={
                                "Authorization": f"Bearer {self._secret}",
                                "Accept-Encoding": "identity",
                            },
                            timeout=httpx.Timeout(60, connect=5),
                        ) as client,
                        streamable_http_client(
                            self._url, http_client=client, terminate_on_close=False
                        ) as (read, write, _),
                        ClientSession(
                            read, write, read_timeout_seconds=timedelta(seconds=60)
                        ) as session,
                    ):
                        await session.initialize()
                        if source_request is not None:
                            return await McpSourceGateway(session, deadline_seconds=60).read(
                                source_request, operation
                            )
                        if tool is None:
                            raise ValueError("named read required")
                        result = await session.call_tool(
                            tool, args, read_timeout_seconds=timedelta(seconds=60)
                        )
                        if result.isError or result.structuredContent is None:
                            raise ApplicationError(
                                ErrorCode.DEPENDENCY_UNAVAILABLE,
                                "connector.mcp_read_failed",
                            )
                        if len(json.dumps(result.structuredContent).encode()) > 131_072:
                            raise ValueError()
                        return result.structuredContent
            except ApplicationError:
                raise
            except Exception:
                raise ApplicationError(
                    ErrorCode.DEPENDENCY_UNAVAILABLE, "connector.mcp_unavailable"
                ) from None

    async def read(
        self, request: SourceReadRequest, operation: SourceReadOperation = "summary"
    ) -> SourceEvidence:
        result = await self._invoke(None, {}, request, operation)
        return SourceEvidence.model_validate(result)

    async def _compat(self, operation: str, target_id: str | None = None) -> dict[str, Any]:
        request = GatewayReadRequest.model_validate(
            {
                "operation": operation,
                "target_id": target_id,
                "correlation_id": CALL_CORRELATION.get() or uuid4(),
            }
        )
        tool = next(name for name, value in COMPAT_TOOLS.items() if value == operation)
        result = await self._invoke(
            tool, {"target_id": target_id, "correlation_id": str(request.correlation_id)}
        )
        try:
            if (
                set(result) != {"request", "evidence"}
                or GatewayReadRequest.model_validate(result["request"]) != request
                or not isinstance(result["evidence"], dict)
            ):
                raise ValueError()
            return result["evidence"]
        except (TypeError, ValueError):
            raise ApplicationError(
                ErrorCode.DEPENDENCY_UNAVAILABLE, "connector.mcp_source_mismatch"
            ) from None

    async def summary(self) -> MonitoringSummary:
        return MonitoringSummary.model_validate(await self._compat("primary_summary"))

    async def incident_context(self) -> MonitoringIncidentContext:
        return MonitoringIncidentContext.model_validate(
            await self._compat("primary_incident_context")
        )

    async def incident_evidence(self, target_id: str) -> IncidentEvidence:
        return IncidentEvidence.model_validate(await self._compat("incident_evidence", target_id))
