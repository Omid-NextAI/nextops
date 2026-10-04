"""Canonical authenticated MCP gateway and separate Linux peer-verified read runner."""

from __future__ import annotations

import asyncio
import json
import os
import secrets
import socket
import stat
import struct
from collections.abc import AsyncIterator, Callable
from contextlib import asynccontextmanager, suppress
from datetime import UTC, datetime
from hashlib import sha256
from pathlib import Path
from typing import Any
from uuid import UUID

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from mcp.server.streamable_http_manager import StreamableHTTPSessionManager
from mcp.server.transport_security import TransportSecuritySettings

from nextops.application.errors import ApplicationError
from nextops.application.source_reads import SourceAuditEvent, SourceReader
from nextops.connectors.configuration import ConnectorSettings
from nextops.connectors.linux import (
    IncidentEvidenceClient,
    LinuxReadClient,
    LinuxTargetRegistry,
    SshLinuxTransport,
)
from nextops.connectors.mcp import create_source_mcp_server
from nextops.connectors.sources import (
    ScopedZabbixTransport,
    ZabbixSourceCollector,
    ZabbixSourceRegistry,
)
from nextops.connectors.zabbix import HttpsZabbixTransport, ZabbixTransport
from nextops.contracts.errors import ErrorCode
from nextops.contracts.incidents import IncidentEvidence
from nextops.contracts.models import ActorContext, Role
from nextops.contracts.monitoring import MonitoringIncidentContext, MonitoringSummary
from nextops.contracts.source_catalog import GatewayReadRequest
from nextops.contracts.sources import (
    SourceEvidence,
    SourceReadBinding,
    SourceReadOperation,
    SourceReadRequest,
)
from nextops.security.deployment_credentials import deployment_secret
from nextops.security.source_catalog import CatalogBindings, load_catalog

FRAME_LIMIT = 131_072


class DrainingZabbixTransport:
    """Cancellation never releases a native HTTPS read's runner slot before actual drain."""

    def __init__(self, inner: ZabbixTransport) -> None:
        self.inner = inner

    async def call(self, method: str, params: dict[str, Any]) -> Any:
        task = asyncio.create_task(self.inner.call(method, params))
        try:
            return await asyncio.shield(task)
        except asyncio.CancelledError:
            with suppress(Exception):
                await asyncio.shield(task)
            raise


class DurableGatewayAudit:
    """Append-only-by-interface, bounded local service audit; app user audit stays in PostgreSQL."""

    def __init__(self, path: Path) -> None:
        self.path = path

    def _append(self, payload: dict[str, Any]) -> None:
        import fcntl  # Linux runtime only

        raw = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode() + b"\n"
        fd = os.open(self.path, os.O_WRONLY | os.O_APPEND | os.O_CREAT | os.O_NOFOLLOW, 0o600)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX)
            meta = os.fstat(fd)
            if (
                not stat.S_ISREG(meta.st_mode)
                or meta.st_uid != os.geteuid()
                or meta.st_mode & 0o077
                or meta.st_size + len(raw) > 268_435_456
            ):
                raise OSError("audit protection or retention limit")
            view = memoryview(raw)
            while view:
                written = os.write(fd, view)
                if written <= 0:
                    raise OSError("audit write failed")
                view = view[written:]
            os.fsync(fd)
        finally:
            os.close(fd)

    async def record(self, event: SourceAuditEvent) -> None:
        try:
            await asyncio.to_thread(self._append, event.model_dump(mode="json"))
        except OSError:
            raise ApplicationError(
                ErrorCode.DEPENDENCY_UNAVAILABLE, "connector.audit_unavailable"
            ) from None

    async def compat(
        self, request: GatewayReadRequest, outcome: str, digest: str | None = None
    ) -> None:
        try:
            await asyncio.to_thread(
                self._append,
                {
                    "operation": request.operation,
                    "target_id": request.target_id,
                    "correlation_id": str(request.correlation_id),
                    "outcome": outcome,
                    "occurred_at": datetime.now(UTC).isoformat(),
                    "evidence_sha256": digest,
                },
            )
        except OSError:
            raise ApplicationError(
                ErrorCode.DEPENDENCY_UNAVAILABLE, "connector.audit_unavailable"
            ) from None


class ServiceAuthorization:
    """TLS/service authentication binds this principal; the app rechecks the real user in PG."""

    def __init__(self, trusted: ActorContext) -> None:
        self._trusted = trusted

    async def authorize(self, actor: ActorContext, binding: SourceReadBinding) -> None:
        if (
            actor != self._trusted
            or actor.organization_id != binding.organization_id
            or actor.environment_id != binding.environment_id
            or "zabbix.read" not in actor.scopes
        ):
            raise ApplicationError(ErrorCode.POLICY_DENIED, "connector.source_scope_denied")


class UnixRunnerClient:
    def __init__(self, path: Path, runner_uid: int, audit: DurableGatewayAudit) -> None:
        self.path, self.runner_uid, self.audit = path, runner_uid, audit
        self._active = asyncio.Semaphore(2)

    async def call(self, request: GatewayReadRequest) -> dict[str, Any]:
        if self._active.locked():
            raise ApplicationError(ErrorCode.OVERLOADED, "connector.source_overloaded")
        async with self._active:
            writer: asyncio.StreamWriter | None = None
            try:
                async with asyncio.timeout(60):
                    reader, writer = await asyncio.open_unix_connection(
                        str(self.path), limit=FRAME_LIMIT + 1
                    )
                    peer = writer.get_extra_info("socket")
                    uid = struct.unpack(
                        "3i", peer.getsockopt(socket.SOL_SOCKET, socket.SO_PEERCRED, 12)
                    )[1]
                    if uid != self.runner_uid:
                        raise ApplicationError(
                            ErrorCode.POLICY_DENIED, "connector.runner_identity_denied"
                        )
                    writer.write(request.model_dump_json().encode() + b"\n")
                    await writer.drain()
                    raw = await reader.readline()
                    if not raw.endswith(b"\n") or len(raw) > FRAME_LIMIT:
                        raise ValueError()
                    reply = json.loads(raw)
                    if (
                        not isinstance(reply, dict)
                        or set(reply) != {"request", "payload", "error"}
                        or GatewayReadRequest.model_validate(reply["request"]) != request
                    ):
                        raise ValueError()
                    if reply["error"] is not None:
                        raise ApplicationError(
                            ErrorCode(reply["error"]), "connector.runner_read_failed"
                        )
                    if not isinstance(reply["payload"], dict):
                        raise ValueError()
                    return reply["payload"]
            except ApplicationError:
                raise
            except (OSError, TimeoutError, ValueError):
                raise ApplicationError(
                    ErrorCode.DEPENDENCY_UNAVAILABLE, "connector.runner_unavailable"
                ) from None
            finally:
                if writer is not None:
                    writer.close()
                    await writer.wait_closed()

    async def collect(
        self,
        request: SourceReadRequest,
        operation: SourceReadOperation,
        *,
        stopped: Callable[[], bool],
    ) -> SourceEvidence:
        payload = await self.call(
            GatewayReadRequest.model_validate(
                {**request.model_dump(), "operation": f"source_{operation}"}
            )
        )
        return SourceEvidence.model_validate(payload)

    async def compat_read(self, request: GatewayReadRequest) -> dict[str, Any]:
        await self.audit.compat(request, "started")
        try:
            payload = await self.call(request)
            digest = sha256(
                json.dumps(
                    payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
                ).encode()
            ).hexdigest()
            await self.audit.compat(request, "completed", digest)
            return {"request": request.model_dump(mode="json"), "evidence": payload}
        except BaseException:
            from anyio import CancelScope

            with CancelScope(shield=True):
                await asyncio.wait_for(self.audit.compat(request, "failed"), 5)
            raise


def create_gateway_app(
    reader: SourceReader, actor: ActorContext, secret: str, compat: UnixRunnerClient | None = None
) -> FastAPI:
    if not 32 <= len(secret) <= 512:
        raise ValueError("protected MCP service credential required")
    server = create_source_mcp_server(reader, actor, compat.compat_read if compat else None)
    manager = StreamableHTTPSessionManager(
        server,
        json_response=True,
        stateless=True,
        max_request_body_size=8192,
        security_settings=TransportSecuritySettings(
            enable_dns_rebinding_protection=True,
            allowed_hosts=["localhost", "127.0.0.1", "localhost:*", "127.0.0.1:*"],
            allowed_origins=[],
        ),
    )

    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncIterator[None]:
        async with manager.run():
            yield

    app = FastAPI(lifespan=lifespan, docs_url=None, redoc_url=None, openapi_url=None)

    @app.middleware("http")
    async def authenticate(request: Request, call_next: Callable[..., Any]) -> Any:
        if request.url.path == "/healthz":
            return await call_next(request)
        value = request.headers.get("authorization", "")
        if len(value) > 520 or not secrets.compare_digest(value, f"Bearer {secret}"):
            try:
                await reader.deny_protocol(actor, ErrorCode.UNAUTHENTICATED)
            except Exception:
                return JSONResponse({"error": {"code": "dependency_unavailable"}}, status_code=503)
            return JSONResponse({"error": {"code": "unauthenticated"}}, status_code=401)
        return await call_next(request)

    @app.get("/healthz")
    def health() -> dict[str, str]:
        return {"status": "ok", "service": "nextops-mcp-gateway"}

    app.mount("/mcp", manager.asgi_app)
    return app


def create_runtime_gateway_app() -> FastAPI:
    catalog = load_catalog(Path(os.environ["NEXTOPS_SOURCE_CATALOG_FILE"]))
    if not catalog.sources:
        raise ValueError("reviewed source catalogue required")
    first = catalog.sources[0]
    actor = ActorContext(
        subject_id=UUID(os.environ["NEXTOPS_MCP_SERVICE_ID"]),
        organization_id=first.organization_id,
        environment_id=first.environment_id,
        roles=frozenset({Role.OPERATOR}),
        scopes=frozenset({"zabbix.read", "linux.read"}),
    )
    audit = DurableGatewayAudit(Path(os.environ["NEXTOPS_MCP_AUDIT_FILE"]))
    client = UnixRunnerClient(
        Path(os.environ["NEXTOPS_RUNNER_SOCKET"]), int(os.environ["NEXTOPS_RUNNER_UID"]), audit
    )
    reader = SourceReader(
        CatalogBindings(catalog), ServiceAuthorization(actor), audit, client, deadline_seconds=60
    )
    secret = deployment_secret(
        value_variable="NEXTOPS_MCP_SERVICE_SECRET",
        file_variable="NEXTOPS_MCP_SERVICE_SECRET_FILE",
        credential_name="mcp-service-secret",
    )
    return create_gateway_app(reader, actor, secret, client)


async def serve_runner() -> None:
    """No TCP listener, shell interface or service bearer; only the gateway UID can connect."""
    registry = ZabbixSourceRegistry.from_file(Path(os.environ["NEXTOPS_SOURCE_REGISTRY_FILE"]))
    credentials = Path(os.environ["CREDENTIALS_DIRECTORY"])

    def transport(source: Any) -> ZabbixTransport:
        token = deployment_secret(
            value_variable="NEXTOPS_UNUSED_SOURCE_TOKEN",
            file_variable="NEXTOPS_UNUSED_SOURCE_TOKEN_FILE",
            credential_name=source.credential_name,
        )
        if not 32 <= len(token) <= 512:
            raise ValueError("protected source token required")
        return DrainingZabbixTransport(
            HttpsZabbixTransport(source.api_url, source.ca_file, token, 12)
        )

    collector = ZabbixSourceCollector(registry, transport)
    # The old HTTP service bearer is deliberately not delivered to this runner.
    settings = ConnectorSettings(
        zabbix_api_url=os.environ["NEXTOPS_ZABBIX_API_URL"],
        zabbix_ca_file=Path(os.environ["NEXTOPS_ZABBIX_CA_FILE"]),
        zabbix_api_token=deployment_secret(
            value_variable="NEXTOPS_ZABBIX_API_TOKEN",
            file_variable="NEXTOPS_ZABBIX_API_TOKEN_FILE",
            credential_name="zabbix-api-token",
        ),
        service_auth_secret="unused-runner-config-placeholder-00000000",
        zabbix_host=os.environ.get("NEXTOPS_ZABBIX_HOST", "Zabbix server"),
        linux_targets_file=Path(os.environ["NEXTOPS_LINUX_TARGETS_FILE"])
        if os.environ.get("NEXTOPS_LINUX_TARGETS_FILE")
        else None,
    )
    primary_transport = DrainingZabbixTransport(
        HttpsZabbixTransport(
            settings.zabbix_api_url,
            settings.zabbix_ca_file,
            settings.zabbix_api_token.get_secret_value(),
            12,
        )
    )
    primary_source = next(s for s in registry.sources if s.source_id == "primary")
    primary_target = next(t for t in primary_source.targets if t.host == settings.zabbix_host)
    linux_client = None
    linux_registry = None
    if settings.linux_targets_file:
        linux_registry = LinuxTargetRegistry.from_file(settings.linux_targets_file)
        linux_client = LinuxReadClient(
            linux_registry,
            SshLinuxTransport(linux_registry.known_hosts_file, timeout_seconds=15),
        )
    expected_uid = int(os.environ["NEXTOPS_GATEWAY_UID"])
    path = Path(os.environ["NEXTOPS_RUNNER_SOCKET"])
    if not path.is_absolute() or path.exists() or not credentials.is_dir():
        raise ValueError("fresh protected runtime socket required")
    active = asyncio.Semaphore(2)

    async def handle(stream: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        try:
            peer = writer.get_extra_info("socket")
            uid = struct.unpack("3i", peer.getsockopt(socket.SOL_SOCKET, socket.SO_PEERCRED, 12))[1]
            if uid != expected_uid or active.locked():
                return
            async with active:
                async with asyncio.timeout(90):
                    raw = await asyncio.wait_for(stream.readline(), 5)
                    if not raw.endswith(b"\n") or len(raw) > 8192:
                        return
                    request = GatewayReadRequest.model_validate_json(raw)
                    payload, error = None, None
                    evidence: (
                        SourceEvidence
                        | MonitoringSummary
                        | MonitoringIncidentContext
                        | IncidentEvidence
                    )
                    try:
                        if request.operation.startswith("source_"):
                            evidence = await collector.collect(
                                SourceReadRequest(
                                    source_id=request.source_id,
                                    target_id=request.target_id,
                                    correlation_id=request.correlation_id,
                                ),
                                "summary"
                                if request.operation == "source_summary"
                                else "incident_context",
                                stopped=stream.at_eof,
                            )
                        elif request.operation in {"primary_summary", "primary_incident_context"}:
                            scoped = await collector.collect(
                                SourceReadRequest(
                                    source_id="primary",
                                    target_id=primary_target.target_id,
                                    correlation_id=request.correlation_id,
                                ),
                                "summary"
                                if request.operation == "primary_summary"
                                else "incident_context",
                                stopped=stream.at_eof,
                            )
                            evidence = scoped.evidence
                            provenance = {
                                "source_id": "primary",
                                "target_id": primary_target.target_id,
                                "host_group_ids": scoped.host_group_ids,
                            }
                            if isinstance(evidence, MonitoringSummary):
                                evidence = MonitoringSummary.model_validate(
                                    {**evidence.model_dump(), **provenance}
                                )
                            else:
                                summary = MonitoringSummary.model_validate(
                                    {**evidence.summary.model_dump(), **provenance}
                                )
                                evidence = MonitoringIncidentContext.model_validate(
                                    {**evidence.model_dump(), "summary": summary}
                                )
                        elif (
                            linux_client is not None
                            and linux_registry is not None
                            and request.target_id is not None
                        ):
                            linux_target = linux_registry.resolve(request.target_id)
                            source_target = next(
                                t
                                for t in primary_source.targets
                                if t.host == linux_target.zabbix_host
                            )
                            scoped_transport = ScopedZabbixTransport(
                                primary_source,
                                source_target,
                                primary_transport,
                                stopped=stream.at_eof,
                            )
                            evidence = await IncidentEvidenceClient(
                                linux_registry,
                                scoped_transport,
                                linux_client,
                                incident_lookback_minutes=settings.incident_lookback_minutes,
                            ).evidence(request.target_id)
                        else:
                            raise ApplicationError(
                                ErrorCode.DEPENDENCY_UNAVAILABLE, "connector.linux_not_configured"
                            )
                        payload = evidence.model_dump(mode="json")
                    except ApplicationError as exc:
                        error = exc.code.value
                    except Exception:
                        error = ErrorCode.DEPENDENCY_UNAVAILABLE.value
                    reply = (
                        json.dumps(
                            {
                                "request": request.model_dump(mode="json"),
                                "payload": payload,
                                "error": error,
                            },
                            ensure_ascii=False,
                            separators=(",", ":"),
                        ).encode()
                        + b"\n"
                    )
                    if len(reply) <= FRAME_LIMIT:
                        writer.write(reply)
                        await writer.drain()
        except (OSError, TimeoutError, ValueError):
            pass
        finally:
            writer.close()
            await writer.wait_closed()

    server = await asyncio.start_unix_server(handle, path=str(path), limit=8193)
    os.chmod(path, 0o660)
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(serve_runner())
