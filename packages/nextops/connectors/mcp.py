"""Optional official-SDK adapter; no anonymous runtime entrypoint or target credentials."""

from __future__ import annotations

import json
from datetime import timedelta
from typing import Any

from mcp import ClientSession
from mcp.server.lowlevel import Server
from mcp.server.stdio import stdio_server
from mcp.types import CallToolResult, TextContent, Tool, ToolAnnotations
from pydantic import ValidationError

from nextops.application.errors import ApplicationError
from nextops.application.source_reads import MAX_SOURCE_EVIDENCE_BYTES, SourceReader
from nextops.contracts.errors import ErrorCode
from nextops.contracts.models import ActorContext
from nextops.contracts.sources import SourceEvidence, SourceReadOperation, SourceReadRequest

TOOLS: dict[str, SourceReadOperation] = {
    "nextops_zabbix_summary": "summary",
    "nextops_zabbix_incident_context": "incident_context",
}


def create_source_mcp_server(reader: SourceReader, actor: ActorContext) -> Server[Any, Any]:
    """The trusted host supplies the actor and real application ports, never the LLM."""
    server: Server[Any, Any] = Server("nextops-zabbix-ro", version="1.0.0")

    # The pinned SDK decorators are untyped; adapter inputs/outputs remain typed.
    @server.list_tools()  # type: ignore[no-untyped-call, untyped-decorator]
    async def list_tools() -> list[Tool]:
        return [
            Tool(
                name=name,
                description=f"Bounded, authorized Zabbix {operation}.",
                inputSchema=SourceReadRequest.model_json_schema(),
                outputSchema=SourceEvidence.model_json_schema(),
                annotations=ToolAnnotations(
                    readOnlyHint=True, destructiveHint=False, openWorldHint=False
                ),
            )
            for name, operation in TOOLS.items()
        ]

    @server.call_tool(validate_input=False)  # type: ignore[untyped-decorator]
    async def call_tool(name: str, arguments: dict[str, Any]) -> CallToolResult:
        try:
            operation = TOOLS.get(name)
            if operation is None:
                await reader.deny_protocol(actor, ErrorCode.POLICY_DENIED)
                raise ApplicationError(ErrorCode.POLICY_DENIED, "connector.mcp_tool_denied")
            try:
                request = SourceReadRequest.model_validate(arguments)
            except ValidationError:
                await reader.deny_protocol(actor, ErrorCode.INVALID_REQUEST)
                raise ApplicationError(
                    ErrorCode.INVALID_REQUEST, "connector.mcp_input_invalid"
                ) from None
            evidence = await reader.read(actor, request, operation)
            payload = evidence.model_dump(mode="json")
            return CallToolResult(
                content=[
                    TextContent(
                        type="text",
                        text=json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
                    )
                ],
                structuredContent=payload,
            )
        except ApplicationError as error:
            return _safe_error(error.code)
        except Exception:
            # SDK defaults may serialize arbitrary exception strings; do not leak them.
            return _safe_error(ErrorCode.DEPENDENCY_UNAVAILABLE)

    return server


def _safe_error(code: ErrorCode) -> CallToolResult:
    return CallToolResult(
        isError=True,
        content=[
            TextContent(
                type="text",
                text=json.dumps(
                    {"error": {"code": code.value, "message_key": f"connector.mcp_{code.value}"}}
                ),
            )
        ],
    )


async def serve_source_stdio(reader: SourceReader, actor: ActorContext) -> None:
    """Run only after a trusted composition authenticates its parent/caller and binds ports."""
    server = create_source_mcp_server(reader, actor)
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


class McpSourceGateway:
    """Typed client for an already initialized, privately connected official SDK session."""

    def __init__(self, session: ClientSession, *, deadline_seconds: float = 30.0) -> None:
        if not 0 < deadline_seconds <= 60:
            raise ValueError("MCP client deadline exceeds the reviewed profile")
        self._session = session
        self._deadline = timedelta(seconds=deadline_seconds)

    async def read(
        self, request: SourceReadRequest, operation: SourceReadOperation
    ) -> SourceEvidence:
        tool = next((name for name, value in TOOLS.items() if value == operation), None)
        if tool is None:
            raise ApplicationError(ErrorCode.POLICY_DENIED, "connector.mcp_tool_denied")
        try:
            response = await self._session.call_tool(
                tool, request.model_dump(mode="json"), read_timeout_seconds=self._deadline
            )
            if response.isError:
                code = ErrorCode.DEPENDENCY_UNAVAILABLE
                if (
                    len(response.content) == 1
                    and isinstance(response.content[0], TextContent)
                    and len(response.content[0].text.encode("utf-8")) <= 1024
                ):
                    try:
                        error = json.loads(response.content[0].text)
                        code = ErrorCode(error["error"]["code"])
                    except (ValueError, KeyError, TypeError):
                        pass
                raise ApplicationError(code, f"connector.mcp_{code.value}")
            if response.structuredContent is None:
                raise ApplicationError(
                    ErrorCode.DEPENDENCY_UNAVAILABLE, "connector.mcp_read_failed"
                )
            if (
                len(
                    json.dumps(
                        response.structuredContent, ensure_ascii=False, separators=(",", ":")
                    ).encode("utf-8")
                )
                > MAX_SOURCE_EVIDENCE_BYTES
            ):
                raise ApplicationError(
                    ErrorCode.DEPENDENCY_UNAVAILABLE, "connector.mcp_output_invalid"
                )
            result = SourceEvidence.model_validate(response.structuredContent)
            if (
                result.source_id != request.source_id
                or result.target_id != request.target_id
                or result.correlation_id != request.correlation_id
                or result.operation != operation
            ):
                raise ApplicationError(
                    ErrorCode.DEPENDENCY_UNAVAILABLE, "connector.mcp_source_mismatch"
                )
            return result
        except ApplicationError:
            raise
        except Exception:
            raise ApplicationError(
                ErrorCode.DEPENDENCY_UNAVAILABLE, "connector.mcp_unavailable"
            ) from None
