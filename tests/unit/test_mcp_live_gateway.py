"""Real Streamable HTTP protocol and closed discovery contracts; no live credentials."""

import asyncio
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from unittest.mock import AsyncMock
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from nextops.connectors.source_runtime import DrainingZabbixTransport, create_gateway_app
from nextops.contracts.models import ActorContext, Role
from nextops.contracts.monitoring import MonitoringSummary
from nextops.contracts.source_catalog import GatewayReadRequest, SourceCatalog
from nextops.contracts.sources import SourceEvidence, SourceReadRequest
from nextops.security.source_catalog import load_catalog


def test_authenticated_streamable_http_and_source_provenance() -> None:
    actor = ActorContext(
        subject_id=uuid4(),
        organization_id=uuid4(),
        environment_id=uuid4(),
        roles=frozenset({Role.VIEWER}),
        scopes=frozenset({"zabbix.read"}),
    )
    reader = AsyncMock()
    correlation = uuid4()
    reader.read.return_value = SourceEvidence(
        source_id="secondary",
        target_id="sla",
        operation="summary",
        correlation_id=correlation,
        host_group_ids=("23",),
        evidence=MonitoringSummary(
            source_version="7.0.29",
            host="Fixture SLA",
            collected_at=datetime.now(UTC),
            metrics=(),
            active_problems=(),
        ),
    )
    secret = "gateway-fixture-secret-only-000000000"
    with TestClient(
        create_gateway_app(reader, actor, secret), base_url="http://localhost"
    ) as client:
        assert client.get("/healthz").status_code == 200
        assert client.post("/mcp/", json={}).status_code == 401
        reader.deny_protocol.assert_awaited_once()
        headers = {
            "Authorization": f"Bearer {secret}",
            "Accept": "application/json, text/event-stream",
        }
        initialized = client.post(
            "/mcp/",
            headers=headers,
            json={
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2025-11-25",
                    "capabilities": {},
                    "clientInfo": {"name": "nextops-test", "version": "1.0.0"},
                },
            },
        )
        assert initialized.status_code == 200, initialized.text
        listed = client.post(
            "/mcp/", headers=headers, json={"jsonrpc": "2.0", "id": 2, "method": "tools/list"}
        )
        names = {tool["name"] for tool in listed.json()["result"]["tools"]}
        assert names == {"nextops_zabbix_summary", "nextops_zabbix_incident_context"}
        result = client.post(
            "/mcp/",
            headers=headers,
            json={
                "jsonrpc": "2.0",
                "id": 3,
                "method": "tools/call",
                "params": {
                    "name": "nextops_zabbix_summary",
                    "arguments": {
                        "source_id": "secondary",
                        "target_id": "sla",
                        "correlation_id": str(correlation),
                    },
                },
            },
        )
        assert result.status_code == 200, result.text
        assert result.json()["result"]["structuredContent"]["source_id"] == "secondary"
        assert result.json()["result"]["structuredContent"]["target_id"] == "sla"
        assert secret not in result.text
        reader.read.assert_awaited_once()
        invalid = client.post(
            "/mcp/",
            headers=headers,
            json={
                "jsonrpc": "2.0",
                "id": 4,
                "method": "tools/call",
                "params": {
                    "name": "nextops_zabbix_summary",
                    "arguments": {"url": "https://example.invalid"},
                },
            },
        )
        assert invalid.json()["result"]["isError"] is True
        assert reader.read.await_count == 1
        assert client.post("/mcp/", headers=headers, content="x" * 8193).status_code == 413


@pytest.mark.parametrize(
    "changes",
    [
        {"source_id": "secondary"},
        {"target_id": "server"},
        {"operation": "shell"},
        {"url": "https://example.invalid"},
        {"roles": ["admin"]},
    ],
)
def test_named_primary_read_cannot_inject_scope(changes: dict[str, Any]) -> None:
    with pytest.raises(ValidationError):
        GatewayReadRequest.model_validate(
            {"operation": "primary_summary", "correlation_id": str(uuid4()), **changes}
        )


def test_catalogue_is_credential_free_and_not_live_health(tmp_path: Path) -> None:
    catalog = SourceCatalog(
        sources=(
            {
                "source_id": "secondary",
                "label": "Second Zabbix",
                "organization_id": uuid4(),
                "environment_id": uuid4(),
                "targets": [{"target_id": "sla", "label": "SLA", "binding_sha256": "a" * 64}],
            },
        )
    )
    assert catalog.discovery_mode == "approved_registry"
    assert set(catalog.sources[0].model_dump()) == {
        "source_id",
        "label",
        "organization_id",
        "environment_id",
        "targets",
    }
    with pytest.raises(KeyError):
        catalog.resolve_binding("secondary", "unknown")
    path = tmp_path / "catalog.json"
    path.write_text(catalog.model_dump_json(), encoding="utf-8")
    assert load_catalog(path) == catalog
    path.write_text('{"sources":[],"sources":[]}', encoding="utf-8")
    with pytest.raises(ValueError, match="invalid or unavailable"):
        load_catalog(path)


def test_selected_source_summary_requires_complete_provenance() -> None:
    with pytest.raises(ValidationError):
        MonitoringSummary(
            source_id="secondary",
            source_version="7.0.29",
            host="Fixture",
            collected_at=datetime.now(UTC),
            metrics=(),
            active_problems=(),
        )


@pytest.mark.parametrize(
    "changed",
    [
        "organization_id",
        "environment_id",
        "api_url",
        "credential_name",
        "approved_group_ids",
        "targets",
    ],
)
def test_runner_binding_drift_is_denied_before_transport(changed: str) -> None:
    from test_source_mcp import source

    from nextops.application.errors import ApplicationError
    from nextops.connectors.sources import ZabbixSourceCollector, ZabbixSourceRegistry

    original = source()
    first = ZabbixSourceRegistry(sources=(original,))
    values: dict[str, Any] = {
        "organization_id": uuid4(),
        "environment_id": uuid4(),
        "api_url": "https://different.example.invalid/api_jsonrpc.php",
        "credential_name": "different-token",
        "approved_group_ids": ("2", "3"),
        "targets": ({**original.targets[0].model_dump(), "host_id": "10085"},),
    }
    drifted = ZabbixSourceRegistry.model_validate(
        {"sources": [{**original.model_dump(), changed: values[changed]}]}
    )
    transport = AsyncMock()
    collector = ZabbixSourceCollector(drifted, lambda _: transport)
    intent = SourceReadRequest(
        source_id="primary",
        target_id="server",
        correlation_id=uuid4(),
        binding_sha256=first.binding_digest("primary", "server"),
    )
    with pytest.raises(ApplicationError, match="source_binding_mismatch"):
        asyncio.run(collector.collect(intent, "summary", stopped=lambda: False))
    assert not transport.call.called


@pytest.mark.parametrize("operation", ["summary", "incident_context", "incident_evidence"])
def test_invalid_compat_evidence_has_safe_typed_error(operation: str, tmp_path: Path) -> None:
    from nextops.api.mcp_gateway import TlsMcpGateway
    from nextops.application.errors import ApplicationError

    gateway = TlsMcpGateway("https://localhost:18100/mcp/", tmp_path / "ca.crt", "a" * 64)
    gateway._compat = AsyncMock(return_value={"invalid": "fixture"})  # type: ignore[method-assign]
    args = ("app",) if operation == "incident_evidence" else ()
    with pytest.raises(ApplicationError, match="mcp_output_invalid"):
        asyncio.run(getattr(gateway, operation)(*args))


def test_native_read_cancellation_waits_for_actual_drain() -> None:
    async def scenario() -> None:
        entered, finish = asyncio.Event(), asyncio.Event()

        class Transport:
            async def call(self, method: str, params: dict[str, Any]) -> Any:
                entered.set()
                await finish.wait()
                return []

        call = asyncio.create_task(DrainingZabbixTransport(Transport()).call("host.get", {}))
        await entered.wait()
        call.cancel()
        await asyncio.sleep(0)
        assert not call.done()
        finish.set()
        with pytest.raises(asyncio.CancelledError):
            await call

    asyncio.run(scenario())
