"""Local identity administration through real restricted PostgreSQL/API boundaries."""

from concurrent.futures import ThreadPoolExecutor
from datetime import UTC, datetime, timedelta
from threading import Event
from typing import Any
from uuid import uuid4

import pytest
from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient
from pydantic import SecretStr
from sqlalchemy import Engine, event, func, select, text, update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker

from nextops.api.app import create_app
from nextops.application.errors import ApplicationError
from nextops.application.service import DurableAppService
from nextops.application.users import DurableUserService
from nextops.configuration import AppSettings
from nextops.contracts.durable import BootstrapRequest, LoginRequest
from nextops.contracts.errors import ErrorCode
from nextops.contracts.users import UserStatusRequest
from nextops.persistence.models import AuditEvent, Environment, Identity

pytestmark = pytest.mark.integration
PASSWORD = "local fixture password only"


@pytest.fixture()
def user_app(
    app_session_factory: sessionmaker[Session],
) -> tuple[TestClient, str, DurableAppService]:
    settings = AppSettings(
        database_url=SecretStr("postgresql+psycopg://unused"),
        bootstrap_secret=SecretStr("user-management-bootstrap-fixture-only"),
        recovery_secret=SecretStr("user-management-recovery-fixture-only"),
    )
    service = DurableAppService(app_session_factory, settings)
    bootstrap = service.bootstrap(
        BootstrapRequest(
            organization_slug="user-lab",
            organization_name="User lab",
            environment_slug="local",
            environment_name="Local",
            admin_username="owner",
            admin_password=PASSWORD,
        ),
        settings.bootstrap_secret.get_secret_value(),
        uuid4(),
    )
    token = bootstrap.authenticated_session.session.access_token
    return (
        TestClient(create_app(service, user_service=DurableUserService(app_session_factory))),
        token,
        service,
    )


def headers(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def add_user(
    client: TestClient, token: str, name: str = "reader", role: str = "viewer"
) -> dict[str, Any]:
    response = client.post(
        "/api/v1/users",
        headers=headers(token),
        json={
            "username": name,
            "password": PASSWORD,
            "role": role,
        },
    )
    assert response.status_code == 201, response.text
    assert PASSWORD not in response.text and "password" not in response.text
    return dict(response.json())


def test_local_user_create_disable_reenable_reset_and_audit(
    user_app: tuple[TestClient, str, DurableAppService],
    app_session_factory: sessionmaker[Session],
) -> None:
    client, token, service = user_app
    user = add_user(client, token)
    identity_id = user["identity_id"]
    login = service.login(LoginRequest(username="reader", password=PASSWORD), uuid4())
    old_token = login.session.access_token
    assert login.actor.roles == {"viewer"} and "linux.read" not in login.actor.scopes
    response = client.patch(
        f"/api/v1/users/{identity_id}",
        headers=headers(token),
        json={
            "is_active": False,
            "expected_version": 1,
        },
    )
    assert response.status_code == 200 and response.json()["credential_version"] == 2
    with pytest.raises(ApplicationError, match=r"auth\.session_invalid"):
        service.authenticate(old_token)
    assert (
        client.post("/api/v1/login", json={"username": "reader", "password": PASSWORD}).status_code
        == 401
    )
    response = client.patch(
        f"/api/v1/users/{identity_id}",
        headers=headers(token),
        json={
            "is_active": True,
            "expected_version": 2,
        },
    )
    assert response.status_code == 200
    with pytest.raises(ApplicationError):
        service.authenticate(old_token)  # Re-enabling does not resurrect a revoked bearer.
    current = service.login(
        LoginRequest(username="reader", password=PASSWORD), uuid4()
    ).session.access_token
    new_password = "different fixture password only"
    response = client.post(
        f"/api/v1/users/{identity_id}/password",
        headers=headers(token),
        json={
            "new_password": new_password,
            "expected_version": 3,
        },
    )
    assert response.status_code == 200 and response.json()["credential_version"] == 4
    with pytest.raises(ApplicationError):
        service.authenticate(current)
    assert (
        client.post("/api/v1/login", json={"username": "reader", "password": PASSWORD}).status_code
        == 401
    )
    assert (
        client.post(
            "/api/v1/login", json={"username": "reader", "password": new_password}
        ).status_code
        == 200
    )
    listed = client.get("/api/v1/users", headers=headers(token))
    assert listed.status_code == 200 and listed.headers["Cache-Control"] == "no-store"
    with app_session_factory() as session:
        audits = list(
            session.scalars(
                select(AuditEvent).where(AuditEvent.event_type.like("identity.users.%"))
            )
        )
        assert len(audits) == 5 and all(a.outcome == "accepted" for a in audits)
        assert str(identity_id) in str(audits[0].details)
        details = str([a.details for a in audits])
        assert all(secret not in details for secret in (PASSWORD, new_password, token, old_token))


def test_every_user_route_denies_missing_and_non_admin_sessions(
    user_app: tuple[TestClient, str, DurableAppService],
    app_session_factory: sessionmaker[Session],
) -> None:
    client, token, service = user_app
    user = add_user(client, token)
    viewer = service.login(
        LoginRequest(username="reader", password=PASSWORD), uuid4()
    ).session.access_token
    calls = [
        ("GET", "/api/v1/users", None),
        ("POST", "/api/v1/users", {"username": "other", "password": PASSWORD}),
        (
            "PATCH",
            f"/api/v1/users/{user['identity_id']}",
            {"is_active": False, "expected_version": 1},
        ),
        (
            "POST",
            f"/api/v1/users/{user['identity_id']}/password",
            {"new_password": PASSWORD, "expected_version": 1},
        ),
    ]
    for method, path, payload in calls:
        assert client.request(method, path, json=payload).status_code == 401
        assert (
            client.request(method, path, headers=headers(viewer), json=payload).status_code == 403
        )
    with app_session_factory() as session:
        denied = list(
            session.scalars(
                select(AuditEvent).where(
                    AuditEvent.event_type.like("identity.users.%"), AuditEvent.outcome == "denied"
                )
            )
        )
        assert len(denied) == 4


def test_protected_admin_duplicates_extra_fields_and_stale_edit(
    user_app: tuple[TestClient, str, DurableAppService],
) -> None:
    client, token, _ = user_app
    owner = client.get("/api/v1/users", headers=headers(token)).json()["users"][0]
    assert owner["manageable"] is False
    for path, payload in [
        (f"/api/v1/users/{owner['identity_id']}", {"is_active": False, "expected_version": 1}),
        (
            f"/api/v1/users/{owner['identity_id']}/password",
            {"new_password": PASSWORD, "expected_version": 1},
        ),
    ]:
        method = "POST" if path.endswith("password") else "PATCH"
        assert client.request(method, path, headers=headers(token), json=payload).status_code == 403
    user = add_user(client, token)
    assert (
        client.post(
            "/api/v1/users",
            headers=headers(token),
            json={"username": "reader", "password": PASSWORD},
        ).status_code
        == 409
    )
    for extra in (
        {"role": "admin"},
        {"scopes": ["users.manage"]},
        {"organization_id": str(uuid4())},
    ):
        response = client.post(
            "/api/v1/users",
            headers=headers(token),
            json={"username": "invalid", "password": PASSWORD, **extra},
        )
        assert response.status_code == 422 and PASSWORD not in response.text
    path = f"/api/v1/users/{user['identity_id']}"
    assert (
        client.patch(
            path, headers=headers(token), json={"is_active": False, "expected_version": 1}
        ).status_code
        == 200
    )
    assert (
        client.patch(
            path, headers=headers(token), json={"is_active": True, "expected_version": 1}
        ).status_code
        == 409
    )
    assert (
        client.patch(
            path, headers=headers(token), json={"is_active": "false", "expected_version": 2}
        ).status_code
        == 422
    )


def test_cross_environment_is_not_listed_or_mutable(
    user_app: tuple[TestClient, str, DurableAppService],
    app_session_factory: sessionmaker[Session],
) -> None:
    client, token, service = user_app
    actor = service.authenticate(token)
    foreign_id, env_id = uuid4(), uuid4()
    with app_session_factory() as session, session.begin():
        session.add(
            Environment(
                id=env_id, organization_id=actor.organization_id, slug="other", display_name="Other"
            )
        )
        session.flush()
        session.add(
            Identity(
                id=foreign_id,
                organization_id=actor.organization_id,
                environment_id=env_id,
                username="foreign",
                password_hash="not-a-login-hash",
                roles=["viewer"],
                scopes=[],
                is_active=True,
                credential_version=1,
            )
        )
    assert [
        u["username"] for u in client.get("/api/v1/users", headers=headers(token)).json()["users"]
    ] == ["owner"]
    assert (
        client.patch(
            f"/api/v1/users/{foreign_id}",
            headers=headers(token),
            json={"is_active": False, "expected_version": 1},
        ).status_code
        == 404
    )
    assert (
        client.post(
            f"/api/v1/users/{foreign_id}/password",
            headers=headers(token),
            json={"new_password": PASSWORD, "expected_version": 1},
        ).status_code
        == 404
    )


def test_audit_failure_rolls_back_create_and_disable(
    user_app: tuple[TestClient, str, DurableAppService],
    app_session_factory: sessionmaker[Session],
) -> None:
    client, token, service = user_app
    user = add_user(client, token)
    old_token = service.login(
        LoginRequest(username="reader", password=PASSWORD), uuid4()
    ).session.access_token

    def reject_audit(session: Session, *args: Any) -> None:
        if any(
            isinstance(row, AuditEvent) and row.event_type.startswith("identity.users.")
            for row in session.new
        ):
            raise SQLAlchemyError("fixture audit unavailable")

    event.listen(app_session_factory, "before_flush", reject_audit)
    try:
        response = client.post(
            "/api/v1/users",
            headers=headers(token),
            json={"username": "rollback", "password": PASSWORD},
        )
        assert response.status_code == 503
        response = client.patch(
            f"/api/v1/users/{user['identity_id']}",
            headers=headers(token),
            json={"is_active": False, "expected_version": 1},
        )
        assert response.status_code == 503
    finally:
        event.remove(app_session_factory, "before_flush", reject_audit)
    assert service.authenticate(old_token)
    with app_session_factory() as session:
        assert session.scalar(select(Identity).where(Identity.username == "rollback")) is None
        row = session.scalar(select(Identity).where(Identity.username == "reader"))
        assert row is not None and row.is_active and row.credential_version == 1


def test_quota_and_pagination_are_bounded(
    user_app: tuple[TestClient, str, DurableAppService],
    app_session_factory: sessionmaker[Session],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    client, token, service = user_app
    monkeypatch.setattr("nextops.application.users.MAX_USERS", 2)
    user = add_user(client, token)
    assert (
        client.post(
            "/api/v1/users",
            headers=headers(token),
            json={"username": "excess", "password": PASSWORD},
        ).status_code
        == 429
    )
    monkeypatch.setattr("nextops.application.users.MAX_USERS", 500)
    actor = service.authenticate(token)
    with app_session_factory() as session, session.begin():
        for i in range(52):
            session.add(
                Identity(
                    id=uuid4(),
                    organization_id=actor.organization_id,
                    environment_id=actor.environment_id,
                    username=f"fixture{i:03}",
                    password_hash="not-a-login-hash",
                    roles=["viewer"],
                    scopes=[],
                    is_active=True,
                    credential_version=1,
                )
            )
    page = client.get("/api/v1/users", headers=headers(token)).json()
    assert len(page["users"]) == 50 and page["next_offset"] == 50
    assert len(client.get("/api/v1/users?offset=50", headers=headers(token)).json()["users"]) == 4
    assert user["identity_id"]


def test_concurrent_status_edit_has_one_winner(
    user_app: tuple[TestClient, str, DurableAppService],
    app_session_factory: sessionmaker[Session],
) -> None:
    client, token, _ = user_app
    user = add_user(client, token)
    service = DurableUserService(app_session_factory)

    def change() -> str:
        try:
            service.change_status(
                token,
                uuid4(),
                user["identity_id"],
                UserStatusRequest(is_active=False, expected_version=1),
            )
            return "accepted"
        except ApplicationError as error:
            return error.code.value

    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(lambda _: change(), range(2)))
    assert sorted(results) == sorted(["accepted", ErrorCode.CONFLICT.value])


def test_narrow_grant_and_expired_session(
    user_app: tuple[TestClient, str, DurableAppService],
    migrated_postgres: tuple[str, Engine],
) -> None:
    client, token, _ = user_app
    _, engine = migrated_postgres
    with engine.begin() as connection:
        assert connection.scalar(
            text("SELECT has_column_privilege('nextops_app', 'identities', 'is_active', 'UPDATE')")
        )
        for column in ("roles", "scopes", "organization_id", "environment_id"):
            assert not connection.scalar(
                text(
                    "SELECT has_column_privilege('nextops_app', 'identities', "
                    f"'{column}', 'UPDATE')"
                )
            )
        from nextops.persistence.models import Session as SessionModel

        connection.execute(
            update(SessionModel).values(expires_at=datetime.now(UTC) - timedelta(seconds=1))
        )
    assert client.get("/api/v1/users", headers=headers(token)).status_code == 401


@pytest.mark.parametrize("role", ["operator", "engineer"])
def test_read_only_role_profiles_do_not_grant_administration(
    user_app: tuple[TestClient, str, DurableAppService],
    role: str,
) -> None:
    client, token, service = user_app
    add_user(client, token, role=role)
    logged_in = service.login(LoginRequest(username="reader", password=PASSWORD), uuid4())
    assert logged_in.actor.scopes == {"linux.read", "runs.read", "zabbix.read"}
    assert (
        client.get("/api/v1/users", headers=headers(logged_in.session.access_token)).status_code
        == 403
    )


def test_administration_role_is_rechecked_after_waiting_for_lock(
    user_app: tuple[TestClient, str, DurableAppService],
    app_session_factory: sessionmaker[Session],
    migrated_postgres: tuple[str, Engine],
) -> None:
    client, token, service = user_app
    actor = service.authenticate(token)
    _, engine = migrated_postgres
    waiting = Event()

    def before_execute(connection: Any, cursor: Any, statement: str, *args: Any) -> None:
        if "pg_advisory_xact_lock" in statement:
            waiting.set()

    bind = app_session_factory.kw["bind"]
    event.listen(bind, "before_cursor_execute", before_execute)
    try:
        with engine.connect() as lock:
            lock.execute(select(func.pg_advisory_xact_lock(actor.environment_id.int % (2**63 - 1))))
            with ThreadPoolExecutor(max_workers=1) as pool:
                future = pool.submit(client.get, "/api/v1/users", headers=headers(token))
                assert waiting.wait(1)
                with engine.begin() as update_connection:
                    update_connection.execute(
                        update(Identity)
                        .where(Identity.id == actor.subject_id)
                        .values(roles=["viewer"])
                    )
                lock.commit()
                assert future.result(timeout=5).status_code == 403
    finally:
        event.remove(bind, "before_cursor_execute", before_execute)


def test_user_activation_grant_can_be_rolled_back_without_resetting_accounts(
    migrated_postgres: tuple[str, Engine],
    alembic_config: Config,
) -> None:
    _, engine = migrated_postgres
    command.downgrade(alembic_config, "0003_conversations")
    try:
        with engine.connect() as connection:
            assert not connection.scalar(
                text(
                    "SELECT has_column_privilege('nextops_app', 'identities', "
                    "'is_active', 'UPDATE')"
                )
            )
            assert connection.scalar(
                text(
                    "SELECT has_column_privilege('nextops_app', 'identities', "
                    "'password_hash', 'UPDATE')"
                )
            )
    finally:
        command.upgrade(alembic_config, "head")
