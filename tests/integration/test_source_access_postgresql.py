"""Real restricted PostgreSQL source policy/audit and fresh selected-source investigations."""

from datetime import UTC, datetime
from typing import Any
from unittest.mock import AsyncMock
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from pydantic import SecretStr
from sqlalchemy import event, select, update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker

from nextops.api.app import APP_CODE_SHA256, create_app
from nextops.application.service import DurableAppService
from nextops.application.source_access import DurableSourceAccess
from nextops.configuration import AppSettings
from nextops.contracts.assistant import AssistantResponse
from nextops.contracts.durable import BootstrapRequest
from nextops.contracts.monitoring import MonitoringSummary
from nextops.contracts.source_catalog import SourceCatalog
from nextops.contracts.sources import SourceEvidence
from nextops.persistence.models import AuditEvent, Identity, Run, Target

pytestmark = pytest.mark.integration


@pytest.fixture()
def source_app(
    app_session_factory: sessionmaker[Session],
) -> tuple[TestClient, str, AsyncMock, AsyncMock]:
    settings = AppSettings(
        database_url=SecretStr("postgresql+psycopg://unused"),
        bootstrap_secret=SecretStr("source-bootstrap-fixture-only-0000000"),
        recovery_secret=SecretStr("source-recovery-fixture-only-0000000"),
    )
    service = DurableAppService(app_session_factory, settings)
    bootstrap = service.bootstrap(
        BootstrapRequest(
            organization_slug="source-lab",
            organization_name="Source lab",
            environment_slug="local",
            environment_name="Local",
            admin_username="owner",
            admin_password="source fixture password only",
        ),
        settings.bootstrap_secret.get_secret_value(),
        uuid4(),
    )
    catalog = SourceCatalog(
        sources=(
            {
                "source_id": "secondary",
                "label": "Secondary Zabbix",
                "organization_id": bootstrap.organization_id,
                "environment_id": bootstrap.environment_id,
                "targets": [
                    {"target_id": "sla", "label": "Fixture SLA", "binding_sha256": "a" * 64}
                ],
            },
        )
    )
    gateway, ai = AsyncMock(), AsyncMock()

    async def read(request: Any) -> SourceEvidence:
        return SourceEvidence(
            source_id=request.source_id,
            target_id=request.target_id,
            correlation_id=request.correlation_id,
            operation="summary",
            host_group_ids=("23",),
            binding_sha256=request.binding_sha256,
            evidence=MonitoringSummary(
                source_version="7.0.29",
                host="Fixture SLA",
                collected_at=datetime.now(UTC),
                metrics=(),
                active_problems=(),
                is_partial=True,
                partial_reasons=("no_usable_metrics",),
            ),
        )

    gateway.read.side_effect = read

    async def generate(request: Any, correlation_id: Any) -> AssistantResponse:
        now = datetime.now(UTC)
        return AssistantResponse(
            request_id=uuid4(),
            correlation_id=correlation_id,
            locale=request.locale,
            answer="No definitive root cause is established from the supplied evidence.",
            model_id="nextops-qwen3-8b-q4-k-m",
            prompt_tokens=16,
            completion_tokens=16,
            finish_reason="stop",
            started_at=now,
            completed_at=now,
            queue_ms=0,
            cpu_only_required=True,
        )

    ai.generate.side_effect = generate
    return (
        TestClient(
            create_app(
                service,
                inference_gateway=ai,
                source_gateway=gateway,
                source_catalog=catalog,
                source_access=DurableSourceAccess(app_session_factory),
            )
        ),
        bootstrap.authenticated_session.session.access_token,
        gateway,
        ai,
    )


def test_fresh_source_question_has_namespaced_durable_evidence(
    source_app: tuple[TestClient, str, AsyncMock, AsyncMock],
    app_session_factory: sessionmaker[Session],
) -> None:
    client, token, gateway, ai = source_app
    headers = {"Authorization": f"Bearer {token}"}
    catalog = client.get("/api/v1/monitoring/sources", headers=headers)
    assert catalog.status_code == 200 and len(catalog.json()["sources"]) == 1
    response = client.post(
        "/api/v1/monitoring/investigate",
        headers=headers,
        json={
            "locale": "en",
            "question": "What is this host's current status?",
            "source_id": "secondary",
            "target_id": "sla",
        },
    )
    assert response.status_code == 200, response.text
    assert response.headers["X-NextOps-App-Code-SHA256"] == APP_CODE_SHA256
    result = response.json()
    assert (
        result["evidence"]["source_id"] == "secondary" and result["evidence"]["target_id"] == "sla"
    )
    assert "secondary" in ai.generate.call_args.args[0].question
    with app_session_factory() as session:
        run = session.scalar(select(Run))
        assert run is not None
        assert (
            session.scalar(select(Target.name).where(Target.id == run.target_id))
            == "zabbix:secondary/sla"
        )
        assert run.parameters["source_id"] == "secondary"
        assert run.result is not None and run.result["evidence"]["source_id"] == "secondary"
        completed = session.scalar(
            select(AuditEvent).where(AuditEvent.event_type == "monitoring.source.completed")
        )
        assert completed is not None
        assert completed.details["evidence_sha256"] == result["evidence_sha256"]
        assert completed.details["evidence_sha256"] == run.result["evidence_sha256"]
    assert gateway.read.await_count == 1


def test_unknown_source_and_malformed_request_do_not_call_runner(
    source_app: tuple[TestClient, str, AsyncMock, AsyncMock],
    app_session_factory: sessionmaker[Session],
) -> None:
    client, token, gateway, _ = source_app
    for payload, expected in [
        ({"locale": "en", "question": "status", "source_id": "other", "target_id": "sla"}, 403),
        ({"locale": "en", "question": "status", "url": "https://example.invalid"}, 422),
    ]:
        response = client.post(
            "/api/v1/monitoring/investigate",
            headers={"Authorization": f"Bearer {token}"},
            json=payload,
        )
        assert response.status_code == expected, response.text
    assert gateway.read.await_count == 0
    assert client.get("/api/v1/monitoring/sources").status_code == 401
    with app_session_factory() as session:
        failed = session.scalars(
            select(AuditEvent).where(AuditEvent.event_type == "monitoring.source.failed")
        ).all()
        assert len(failed) == 2 and all(event.outcome == "failed" for event in failed)


def test_revocation_during_generation_blocks_publication(
    source_app: tuple[TestClient, str, AsyncMock, AsyncMock],
    app_session_factory: sessionmaker[Session],
) -> None:
    client, token, gateway, ai = source_app
    original = ai.generate.side_effect

    async def revoke(request: Any, correlation: Any) -> AssistantResponse:
        result: AssistantResponse = await original(request, correlation)
        with app_session_factory() as session, session.begin():
            session.execute(update(Identity).values(is_active=False))
        return result

    ai.generate.side_effect = revoke
    response = client.post(
        "/api/v1/monitoring/investigate",
        headers={"Authorization": f"Bearer {token}"},
        json={"locale": "en", "question": "status", "source_id": "secondary", "target_id": "sla"},
    )
    assert response.status_code == 401
    assert gateway.read.await_count == 1


def test_runner_binding_mismatch_never_reaches_model(
    source_app: tuple[TestClient, str, AsyncMock, AsyncMock],
) -> None:
    client, token, gateway, ai = source_app
    original = gateway.read.side_effect

    async def drift(request: Any) -> SourceEvidence:
        evidence: SourceEvidence = await original(request)
        return evidence.model_copy(update={"binding_sha256": "b" * 64})

    gateway.read.side_effect = drift
    response = client.post(
        "/api/v1/monitoring/investigate",
        headers={"Authorization": f"Bearer {token}"},
        json={"locale": "en", "question": "status", "source_id": "secondary", "target_id": "sla"},
    )
    assert response.status_code == 503
    assert ai.generate.await_count == 0


def test_required_access_audit_failure_blocks_collection(
    source_app: tuple[TestClient, str, AsyncMock, AsyncMock],
    app_session_factory: sessionmaker[Session],
) -> None:
    client, token, gateway, _ = source_app

    def fail(session: Session, context: Any, instances: Any) -> None:
        if any(
            isinstance(obj, AuditEvent) and obj.event_type == "monitoring.source.started"
            for obj in session.new
        ):
            raise SQLAlchemyError("fixture audit failure")

    event.listen(app_session_factory, "before_flush", fail)
    try:
        response = client.post(
            "/api/v1/monitoring/investigate",
            headers={"Authorization": f"Bearer {token}"},
            json={
                "locale": "en",
                "question": "status",
                "source_id": "secondary",
                "target_id": "sla",
            },
        )
        assert response.status_code == 503
        assert gateway.read.await_count == 0
    finally:
        event.remove(app_session_factory, "before_flush", fail)


def test_source_completion_audit_and_result_commit_are_atomic(
    source_app: tuple[TestClient, str, AsyncMock, AsyncMock],
    app_session_factory: sessionmaker[Session],
) -> None:
    client, token, gateway, _ = source_app

    def fail(session: Session, context: Any, instances: Any) -> None:
        if any(
            isinstance(obj, AuditEvent) and obj.event_type == "monitoring.source.completed"
            for obj in session.new
        ):
            raise SQLAlchemyError("finite source completion audit outage")

    event.listen(app_session_factory, "before_flush", fail)
    try:
        response = client.post(
            "/api/v1/monitoring/investigate",
            headers={"Authorization": f"Bearer {token}"},
            json={
                "locale": "en",
                "question": "status",
                "source_id": "secondary",
                "target_id": "sla",
            },
        )
        assert response.status_code == 503
        assert gateway.read.await_count == 1
        with app_session_factory() as session:
            run = session.scalar(select(Run))
            assert run is not None and run.status == "failed" and run.result is None
            assert not session.scalars(
                select(AuditEvent).where(
                    AuditEvent.event_type.in_(
                        ("monitoring.source.completed", "investigation.completed")
                    )
                )
            ).all()
    finally:
        event.remove(app_session_factory, "before_flush", fail)
