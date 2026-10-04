"""Actual official-SDK protocol exchanges; downstream data/audit are explicit fixtures."""

from __future__ import annotations

import asyncio
import hashlib
import json
import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any
from unittest.mock import AsyncMock
from uuid import uuid4

import pytest
from mcp import ClientSession, McpError, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.shared.memory import create_connected_server_and_client_session
from mcp.types import (
    CallToolResult,
    CancelledNotification,
    CancelledNotificationParams,
    ClientNotification,
)
from pydantic import ValidationError

from nextops.application.errors import ApplicationError
from nextops.application.source_reads import SourceAuditEvent, SourceReader
from nextops.connectors.mcp import McpSourceGateway, create_source_mcp_server
from nextops.connectors.sources import ScopedZabbixTransport, ZabbixSource, ZabbixSourceRegistry
from nextops.contracts.models import ActorContext, Role
from nextops.contracts.sources import SourceReadRequest

ORG, ENV, SUBJECT = uuid4(), uuid4(), uuid4()
ACTOR = ActorContext(
    subject_id=SUBJECT,
    organization_id=ORG,
    environment_id=ENV,
    roles=frozenset({Role.VIEWER}),
    scopes=frozenset({"zabbix.read"}),
)


def source(source_id: str = "primary", *, host: str = "Fixture host") -> ZabbixSource:
    return ZabbixSource(
        source_id=source_id,
        organization_id=ORG,
        environment_id=ENV,
        api_url=f"https://{source_id}.example.invalid/api_jsonrpc.php",
        ca_file=Path("C:/fixture/ca.crt")
        if __import__("os").name == "nt"
        else Path("/fixture/ca.crt"),
        credential_name=f"token-{source_id}",
        approved_group_ids=("2",),
        targets=(
            {"target_id": "server", "host_id": "10084", "host": host, "host_group_ids": ("2",)},
        ),
    )


class Authorization:
    def __init__(self) -> None:
        self.calls = 0
        self.revoke_after: int | None = None

    async def authorize(self, actor: ActorContext, item: ZabbixSource, target: Any) -> None:
        from nextops.contracts.errors import ErrorCode

        self.calls += 1
        if self.revoke_after is not None and self.calls > self.revoke_after:
            raise ApplicationError(ErrorCode.POLICY_DENIED, "fixture.scope_revoked")


class Audit:
    """Non-durable recording fixture; not PostgreSQL acceptance."""

    def __init__(self, fail_at: str | None = None) -> None:
        self.events: list[SourceAuditEvent] = []
        self.fail_at = fail_at

    async def record(self, event: SourceAuditEvent) -> None:
        await asyncio.sleep(0)  # make protocol cancellation reach a real await point
        if event.outcome == self.fail_at:
            raise RuntimeError("fixture secret must not escape")
        self.events.append(event)


class Transport:
    def __init__(
        self, host: str = "Fixture host", *, group_id: str = "2", audit: Audit | None = None
    ) -> None:
        self.calls: list[tuple[str, dict[str, Any]]] = []
        self.host, self.group_id, self.audit = host, group_id, audit

    async def call(self, method: str, params: dict[str, Any]) -> Any:
        if self.audit is not None:
            assert self.audit.events[0].outcome == "started"
        self.calls.append((method, params))
        now = str(int(datetime.now(UTC).timestamp()) - 1)
        if method == "apiinfo.version":
            return "7.0.29"
        if method == "host.get":
            return [
                {
                    "hostid": "10084",
                    "host": self.host,
                    "name": self.host,
                    "status": "0",
                    "hostgroups": [{"groupid": self.group_id}],
                }
            ]
        if method == "item.get":
            return [
                {
                    "hostid": "10084",
                    "itemid": "20001",
                    "name": "پردازنده / CPU",
                    "key_": "system.cpu.util[,idle]",
                    "value_type": "0",
                    "lastvalue": "88",
                    "units": "%",
                    "lastclock": now,
                    "status": "0",
                    "state": "0",
                }
            ]
        if method == "problem.get":
            return []
        if method == "history.get":
            return [{"itemid": "20001", "clock": now, "value": "88"}]
        if method == "event.get":
            return []
        raise AssertionError("unexpected read")


def setup_reader(
    *,
    transports: dict[str, Transport] | None = None,
    fail_at: str | None = None,
    deadline: float = 30,
) -> tuple[SourceReader, Audit, Authorization]:
    audit, auth = Audit(fail_at), Authorization()
    registry = ZabbixSourceRegistry(sources=(source(), source("secondary", host="میزبان دوم")))
    entries = transports or {
        "primary": Transport(audit=audit),
        "secondary": Transport("میزبان دوم", audit=audit),
    }
    return (
        SourceReader(
            registry, auth, audit, lambda item: entries[item.source_id], deadline_seconds=deadline
        ),
        audit,
        auth,
    )


def request(source_id: str = "primary", target_id: str = "server") -> SourceReadRequest:
    return SourceReadRequest(source_id=source_id, target_id=target_id, correlation_id=uuid4())


@pytest.mark.parametrize("operation", ["summary", "incident_context"])
def test_real_sdk_initialize_discover_and_call_two_sources(operation: str) -> None:
    async def check() -> None:
        reader, audit, auth = setup_reader()
        async with create_connected_server_and_client_session(
            create_source_mcp_server(reader, ACTOR), read_timeout_seconds=timedelta(seconds=5)
        ) as session:
            tools = await session.list_tools()
            assert {tool.name for tool in tools.tools} == {
                "nextops_zabbix_summary",
                "nextops_zabbix_incident_context",
            }
            assert all(tool.inputSchema["additionalProperties"] is False for tool in tools.tools)
            gateway = McpSourceGateway(session)
            first = await gateway.read(request(), operation)  # type: ignore[arg-type]
            second = await gateway.read(request("secondary"), operation)  # type: ignore[arg-type]
            assert (first.source_id, second.source_id) == ("primary", "secondary")
            assert first.evidence.host == "Fixture host"
            assert second.evidence.host == "میزبان دوم"
            assert first.host_group_ids == second.host_group_ids == ("2",)
            assert [event.outcome for event in audit.events] == ["started", "completed"] * 2
            assert all(
                event.evidence_sha256 for event in audit.events if event.outcome == "completed"
            )
            completed = [event for event in audit.events if event.outcome == "completed"]
            for result, event in zip((first, second), completed, strict=True):
                canonical = json.dumps(
                    result.model_dump(mode="json"),
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                ).encode("utf-8")
                assert event.evidence_sha256 == hashlib.sha256(canonical).hexdigest()
            assert auth.calls == 4

    asyncio.run(check())


@pytest.mark.parametrize(
    "arguments",
    [
        {"source_id": "missing", "target_id": "server"},
        {"source_id": "primary", "target_id": "unknown"},
        {"source_id": "primary", "target_id": "server", "api_url": "https://secret.invalid"},
        {"source_id": "primary", "target_id": "server", "roles": ["admin"]},
        {"source_id": "../secondary", "target_id": "server"},
    ],
)
def test_invalid_or_unauthorized_calls_do_not_touch_targets(arguments: dict[str, Any]) -> None:
    async def check() -> None:
        calls: dict[str, Transport] = {"primary": Transport(), "secondary": Transport("میزبان دوم")}
        reader, audit, _ = setup_reader(transports=calls)
        async with create_connected_server_and_client_session(
            create_source_mcp_server(reader, ACTOR)
        ) as session:
            result = await session.call_tool(
                "nextops_zabbix_summary", arguments | {"correlation_id": str(uuid4())}
            )
            assert result.isError
            assert "secret.invalid" not in result.model_dump_json()
            assert not any(transport.calls for transport in calls.values())
            assert len(audit.events) == 1
            assert audit.events[0].outcome == "denied"
            assert "secret.invalid" not in audit.events[0].model_dump_json()

    asyncio.run(check())


@pytest.mark.parametrize(
    "field,value",
    [("scopes", frozenset()), ("organization_id", uuid4()), ("environment_id", uuid4())],
)
def test_forged_actor_scope_denied_and_audited(field: str, value: Any) -> None:
    async def check() -> None:
        transport = Transport()
        reader, audit, _ = setup_reader(transports={"primary": transport})
        with pytest.raises(ApplicationError):
            await reader.read(ACTOR.model_copy(update={field: value}), request(), "summary")
        assert not transport.calls
        assert audit.events[0].outcome == "denied"

    asyncio.run(check())


@pytest.mark.parametrize("fail_at", ["started", "completed"])
def test_audit_failure_has_no_success_or_raw_exception(fail_at: str) -> None:
    async def check() -> None:
        reader, audit, _ = setup_reader(fail_at=fail_at)
        async with create_connected_server_and_client_session(
            create_source_mcp_server(reader, ACTOR)
        ) as session:
            result = await session.call_tool(
                "nextops_zabbix_summary", request().model_dump(mode="json")
            )
            assert result.isError
            assert "fixture secret" not in result.model_dump_json()
            assert not any(event.outcome == "completed" for event in audit.events)

    asyncio.run(check())


def test_revocation_during_read_blocks_completion() -> None:
    async def check() -> None:
        reader, audit, auth = setup_reader()
        auth.revoke_after = 1
        with pytest.raises(ApplicationError):
            await reader.read(ACTOR, request(), "summary")
        assert [event.outcome for event in audit.events] == ["started", "failed"]

    asyncio.run(check())


def test_group_change_and_host_substitution_fail_before_dependent_reads() -> None:
    async def check() -> None:
        for transport in (Transport(group_id="999"), Transport(host="Different host")):
            reader, audit, _ = setup_reader(transports={"primary": transport})
            with pytest.raises(ApplicationError):
                await reader.read(ACTOR, request(), "summary")
            assert [name for name, _ in transport.calls] == ["apiinfo.version", "host.get"]
            assert audit.events[-1].outcome == "failed"

    asyncio.run(check())


def test_no_write_or_unscoped_or_cross_item_read() -> None:
    async def check() -> None:
        item = source()
        transport = Transport()
        scoped = ScopedZabbixTransport(item, item.targets[0], transport)
        for method, params in (("host.update", {}), ("item.get", {"hostids": ["10084"]})):
            with pytest.raises(ApplicationError):
                await scoped.call(method, params)
        assert not transport.calls
        await scoped.call("host.get", {"filter": {"host": ["Fixture host"]}})
        for params in (
            {"hostids": ["999"], "itemids": ["20001"]},
            {"hostids": ["10084"], "itemids": ["999"]},
        ):
            with pytest.raises(ApplicationError):
                await scoped.call("history.get", params)
        assert transport.calls[0][1]["hostids"] == ["10084"]
        assert transport.calls[0][1]["groupids"] == ["2"]

    asyncio.run(check())


def test_timeout_holds_admission_until_actual_drain_and_recovers() -> None:
    async def check() -> None:
        release = asyncio.Event()

        class SlowTransport(Transport):
            async def call(self, method: str, params: dict[str, Any]) -> Any:
                if method == "apiinfo.version":
                    await release.wait()
                return await super().call(method, params)

        transport = SlowTransport()
        # A quarter-second fixture deadline avoids relying on sub-tick Windows timers.
        reader, audit, _ = setup_reader(transports={"primary": transport}, deadline=0.25)
        expired = await asyncio.gather(
            *(reader.read(ACTOR, request(), "summary") for _ in range(2)), return_exceptions=True
        )
        assert all(
            isinstance(error, ApplicationError) and error.code.value == "timeout"
            for error in expired
        )
        with pytest.raises(ApplicationError, match="source_overloaded"):
            await reader.read(ACTOR, request(), "summary")
        release.set()
        await asyncio.sleep(0.01)
        assert [name for name, _ in transport.calls] == ["apiinfo.version"] * 2
        result = await reader.read(ACTOR, request(), "summary")
        assert result.source_id == "primary"
        assert sum(event.outcome == "completed" for event in audit.events) == 1

    asyncio.run(check())


def test_cancelled_call_keeps_slot_and_records_cancelled() -> None:
    async def check() -> None:
        release, entered = asyncio.Event(), asyncio.Event()

        class SlowTransport(Transport):
            async def call(self, method: str, params: dict[str, Any]) -> Any:
                entered.set()
                await release.wait()
                return await super().call(method, params)

        transport = SlowTransport()
        reader, audit, _ = setup_reader(transports={"primary": transport})
        task = asyncio.create_task(reader.read(ACTOR, request(), "summary"))
        await entered.wait()
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task
        assert audit.events[-1].outcome == "cancelled"
        release.set()
        await asyncio.sleep(0.01)
        assert len(transport.calls) == 1
        assert not any(event.outcome == "completed" for event in audit.events)

    asyncio.run(check())


def test_real_sdk_cancellation_stops_dependent_reads_and_recovers() -> None:
    async def check() -> None:
        release, entered = asyncio.Event(), asyncio.Event()

        class SlowTransport(Transport):
            async def call(self, method: str, params: dict[str, Any]) -> Any:
                if method == "apiinfo.version":
                    request_ids.append(server.request_context.request_id)
                    entered.set()
                    await release.wait()
                return await super().call(method, params)

        transport = SlowTransport()
        reader, audit, _ = setup_reader(transports={"primary": transport})
        request_ids: list[str | int] = []
        server = create_source_mcp_server(reader, ACTOR)
        async with create_connected_server_and_client_session(server) as session:
            call = asyncio.create_task(
                session.call_tool("nextops_zabbix_summary", request().model_dump(mode="json"))
            )
            await entered.wait()
            await session.send_notification(
                ClientNotification(
                    CancelledNotification(
                        params=CancelledNotificationParams(requestId=request_ids[0])
                    )
                )
            )
            with pytest.raises(McpError):
                await call
            # Explicit protocol cancellation is distinct from cancelling a local wait.
            for _ in range(50):
                if any(event.outcome == "cancelled" for event in audit.events):
                    break
                await asyncio.sleep(0.01)
            assert audit.events[-1].outcome == "cancelled"
            release.set()
            await asyncio.sleep(0.01)
            assert [name for name, _ in transport.calls] == ["apiinfo.version"]
            assert not any(event.outcome == "completed" for event in audit.events)
            result = await McpSourceGateway(session).read(request(), "summary")
            assert result.source_id == "primary"

    asyncio.run(check())


@pytest.mark.parametrize("field", ["source_id", "target_id", "correlation_id", "operation", "size"])
def test_gateway_rejects_mismatched_or_oversized_structured_output(field: str) -> None:
    async def check() -> None:
        reader, _, _ = setup_reader()
        query = request()
        evidence = await reader.read(ACTOR, query, "summary")
        payload = evidence.model_dump(mode="json")
        payload[field] = "x" * 131_073 if field == "size" else "secondary"
        session = AsyncMock(spec=ClientSession)
        session.call_tool.return_value = CallToolResult(content=[], structuredContent=payload)
        with pytest.raises(ApplicationError):
            await McpSourceGateway(session).read(query, "summary")
        assert session.call_tool.call_args.kwargs["read_timeout_seconds"] == timedelta(seconds=30)

    asyncio.run(check())


def test_gateway_preserves_denial_and_secondary_failure_never_falls_back() -> None:
    async def check() -> None:
        from nextops.contracts.errors import ErrorCode

        class BrokenTransport(Transport):
            async def call(self, method: str, params: dict[str, Any]) -> Any:
                raise RuntimeError("fixture private error")

        primary = Transport()
        reader, _, _ = setup_reader(transports={"primary": primary, "secondary": BrokenTransport()})
        async with create_connected_server_and_client_session(
            create_source_mcp_server(reader, ACTOR)
        ) as session:
            gateway = McpSourceGateway(session)
            for query, code in (
                (request("missing"), ErrorCode.POLICY_DENIED),
                (request("secondary"), ErrorCode.DEPENDENCY_UNAVAILABLE),
            ):
                with pytest.raises(ApplicationError) as caught:
                    await gateway.read(query, "summary")
                assert caught.value.code == code
                assert not primary.calls
            assert (await gateway.read(request(), "summary")).source_id == "primary"

    asyncio.run(check())


def test_official_sdk_stdio_child_uses_only_fixture_ports() -> None:
    async def check() -> None:
        # Test-only subprocess: no operational launcher, registry or credentials.
        code = (
            "import asyncio, sys; "
            f"sys.path.insert(0, {str(Path(__file__).parent)!r}); "
            "from test_source_mcp import setup_reader, ACTOR; "
            "from nextops.connectors.mcp import serve_source_stdio; "
            "reader, _, _ = setup_reader(); "
            "asyncio.run(serve_source_stdio(reader, ACTOR))"
        )
        parameters = StdioServerParameters(
            command=sys.executable,
            args=["-c", code],
            env={"PYTHONUTF8": "1"},
        )
        async with (
            stdio_client(parameters) as (read_stream, write_stream),
            ClientSession(
                read_stream, write_stream, read_timeout_seconds=timedelta(seconds=10)
            ) as session,
        ):
            await session.initialize()
            assert len((await session.list_tools()).tools) == 2
            result = await McpSourceGateway(session).read(request("secondary"), "summary")
            assert result.source_id == "secondary"
            assert result.evidence.host == "میزبان دوم"

    asyncio.run(check())


def test_registry_rejects_duplicate_scope_and_extra_secrets(tmp_path: Path) -> None:
    item = source()
    with pytest.raises(ValidationError):
        ZabbixSourceRegistry(sources=(item, item))
    for changes in (
        {"api_url": "http://source.example.invalid/api_jsonrpc.php"},
        {"api_url": "https://name:password@example.invalid/api_jsonrpc.php"},
        {"token": "fixture secret"},
        {"approved_group_ids": ["999"]},
    ):
        with pytest.raises(ValueError):
            ZabbixSource.model_validate(item.model_dump() | changes)
    path = tmp_path / "registry.json"
    path.write_text(
        '{"schema_version":"1.0.0","schema_version":"bad","secret":"fixture secret"}',
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="source registry invalid or unavailable") as caught:
        ZabbixSourceRegistry.from_file(path)
    assert "fixture secret" not in str(caught.value)


def test_unknown_tool_and_raw_vendor_failure_are_sanitized() -> None:
    async def check() -> None:
        class BrokenTransport(Transport):
            async def call(self, method: str, params: dict[str, Any]) -> Any:
                raise RuntimeError("fixture token and private endpoint")

        reader, _, _ = setup_reader(transports={"primary": BrokenTransport()})
        async with create_connected_server_and_client_session(
            create_source_mcp_server(reader, ACTOR)
        ) as session:
            for tool in ("nextops_zabbix_summary", "host.update"):
                result = await session.call_tool(tool, request().model_dump(mode="json"))
                assert result.isError
                assert "fixture token" not in json.dumps(result.model_dump(mode="json"))

    asyncio.run(check())
