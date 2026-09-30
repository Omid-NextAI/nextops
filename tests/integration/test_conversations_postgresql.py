"""Real restricted-role PostgreSQL acceptance, not in-memory chat simulation."""

from datetime import UTC, datetime, timedelta
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from pydantic import SecretStr
from sqlalchemy import Engine, func, select, text, update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker

from nextops.api.app import create_app
from nextops.application.conversations import DurableConversationService, GenerationTicket
from nextops.application.errors import ApplicationError
from nextops.application.service import DurableAppService
from nextops.configuration import AppSettings
from nextops.contracts.assistant import AssistantResponse, SynthesisRequest
from nextops.contracts.conversations import ConversationMessageRequest, SavedMessage
from nextops.contracts.durable import BootstrapRequest, LoginRequest
from nextops.contracts.errors import ErrorCode
from nextops.inference.contracts import InferenceReadiness
from nextops.persistence.conversations import Conversation, ConversationMessage
from nextops.persistence.models import AuditEvent, Identity

pytestmark = pytest.mark.integration


def assistant(answer: str = "General guidance only.") -> AssistantResponse:
    now = datetime.now(UTC)
    return AssistantResponse(
        request_id=uuid4(),
        correlation_id=uuid4(),
        locale="en",
        answer=answer,
        model_id="nextops-qwen3-5-35b-a3b-q4-k-m",
        prompt_tokens=12,
        completion_tokens=16,
        finish_reason="stop",
        started_at=now,
        completed_at=now,
        queue_ms=0,
        cpu_only_required=True,
    )


@pytest.fixture()
def chats(
    app_session_factory: sessionmaker[Session],
) -> tuple[
    DurableAppService,
    DurableConversationService,
    str,
]:
    settings = AppSettings(
        database_url=SecretStr("postgresql+psycopg://unused-in-service"),
        bootstrap_secret=SecretStr("bootstrap-secret-only-for-conversation-tests"),
        recovery_secret=SecretStr("recovery-secret-only-for-conversation-tests"),
    )
    service = DurableAppService(app_session_factory, settings)
    service.bootstrap(
        BootstrapRequest(
            organization_slug="chat-lab",
            organization_name="Chat lab",
            environment_slug="local",
            environment_name="Local",
            admin_username="owner",
            admin_password="conversation test password only",
        ),
        settings.bootstrap_secret.get_secret_value(),
        uuid4(),
    )
    result = service.login(
        LoginRequest(
            username="owner",
            password="conversation test password only",
        ),
        uuid4(),
    )
    return service, DurableConversationService(app_session_factory), result.session.access_token


def payload(question: str = "What is DNS?") -> ConversationMessageRequest:
    return ConversationMessageRequest(request_id=uuid4(), locale="en", question=question)


def completed(store: DurableConversationService, token: str) -> tuple[object, SavedMessage]:
    chat = store.create(token, "en", uuid4())
    ticket = store.begin(token, chat.conversation_id, payload(), uuid4())
    assert isinstance(ticket, GenerationTicket)
    return chat, store.complete(token, ticket, assistant("DNS maps names."), uuid4())


def test_persistence_restart_replay_conflict_and_audit(
    chats: tuple[DurableAppService, DurableConversationService, str],
    app_session_factory: sessionmaker[Session],
) -> None:
    _, store, token = chats
    chat = store.create(token, "fa", uuid4())
    question = payload("DNS چیست؟")
    ticket = store.begin(token, chat.conversation_id, question, uuid4())
    assert isinstance(ticket, GenerationTicket)
    with pytest.raises(ApplicationError) as concurrent:
        store.begin(token, chat.conversation_id, payload("follow-up"), uuid4())
    assert concurrent.value.code == ErrorCode.CONFLICT
    saved = store.complete(token, ticket, assistant("سامانهٔ نام دامنه"), uuid4())
    restarted = DurableConversationService(app_session_factory)
    page = restarted.get(token, chat.conversation_id, uuid4())
    assert page.messages == (saved,)
    assert page.conversation.title == "DNS چیست؟"
    assert restarted.begin(token, chat.conversation_id, question, uuid4()) == saved
    with pytest.raises(ApplicationError):
        restarted.begin(
            token, chat.conversation_id, question.model_copy(update={"question": "other"}), uuid4()
        )
    with app_session_factory() as session:
        audit = list(
            session.scalars(
                select(AuditEvent).where(
                    AuditEvent.event_type.like("conversation.%"),
                )
            )
        )
    assert {a.event_type for a in audit} >= {
        "conversation.created",
        "conversation.completed",
        "conversation.replayed",
    }
    assert "سامانه" not in str([a.details for a in audit])


def test_other_identity_including_admin_cannot_access_delete_or_generate(
    chats: tuple[DurableAppService, DurableConversationService, str],
    app_session_factory: sessionmaker[Session],
) -> None:
    service, store, token = chats
    chat = store.create(token, "en", uuid4())
    owner = service.authenticate(token)
    with app_session_factory() as session, session.begin():
        owner_identity = session.get(Identity, owner.subject_id)
        assert owner_identity is not None
        session.add(
            Identity(
                id=uuid4(),
                organization_id=owner.organization_id,
                environment_id=owner.environment_id,
                username="second",
                password_hash=owner_identity.password_hash,
                credential_version=1,
                roles=["admin"],
                scopes=["zabbix.read"],
                is_active=True,
            )
        )
    other = service.login(
        LoginRequest(username="second", password="conversation test password only"), uuid4()
    ).session.access_token
    assert store.list(other, uuid4()) == ()
    for operation in (
        lambda: store.get(other, chat.conversation_id, uuid4()),
        lambda: store.delete(other, chat.conversation_id, uuid4()),
        lambda: store.begin(other, chat.conversation_id, payload(), uuid4()),
    ):
        with pytest.raises(ApplicationError) as denied:
            operation()
        assert denied.value.code == ErrorCode.NOT_FOUND


def test_logout_during_generation_cannot_store_or_return_answer(
    chats: tuple[DurableAppService, DurableConversationService, str],
    app_session_factory: sessionmaker[Session],
) -> None:
    service, store, token = chats
    chat = store.create(token, "en", uuid4())
    ticket = store.begin(token, chat.conversation_id, payload(), uuid4())
    assert isinstance(ticket, GenerationTicket)
    service.logout(token, uuid4())
    with pytest.raises(ApplicationError) as expired:
        store.complete(token, ticket, assistant(), uuid4())
    assert expired.value.code == ErrorCode.UNAUTHENTICATED
    with app_session_factory() as session:
        assert session.scalar(select(func.count()).select_from(ConversationMessage)) == 0


def test_delete_pending_chat_invalidates_late_generation(
    chats: tuple[DurableAppService, DurableConversationService, str],
) -> None:
    _, store, token = chats
    chat = store.create(token, "en", uuid4())
    ticket = store.begin(token, chat.conversation_id, payload(), uuid4())
    assert isinstance(ticket, GenerationTicket)
    store.delete(token, chat.conversation_id, uuid4())
    with pytest.raises(ApplicationError) as deleted:
        store.complete(token, ticket, assistant(), uuid4())
    assert deleted.value.code == ErrorCode.NOT_FOUND


def test_expired_chat_and_generation_nonce_are_not_reused(
    chats: tuple[DurableAppService, DurableConversationService, str],
    app_session_factory: sessionmaker[Session],
) -> None:
    _, store, token = chats
    chat = store.create(token, "en", uuid4())
    ticket = store.begin(token, chat.conversation_id, payload(), uuid4())
    assert isinstance(ticket, GenerationTicket)
    with app_session_factory() as session, session.begin():
        session.execute(
            update(Conversation)
            .where(Conversation.id == chat.conversation_id)
            .values(
                pending_until=datetime.now(UTC) - timedelta(seconds=1),
            )
        )
    fresh = store.begin(token, chat.conversation_id, ticket.payload, uuid4())
    assert isinstance(fresh, GenerationTicket) and fresh.nonce != ticket.nonce
    with pytest.raises(ApplicationError):
        store.complete(token, ticket, assistant(), uuid4())
    store.fail(token, fresh, uuid4())
    # An expiry shorter than the creation time would violate the DB constraint.
    future = DurableConversationService(
        app_session_factory, lambda: datetime.now(UTC) + timedelta(days=31)
    )
    with pytest.raises(ApplicationError) as expired:
        future.get(token, chat.conversation_id, uuid4())
    assert expired.value.code == ErrorCode.UNAUTHENTICATED


def test_role_separation_and_migration_grants(migrated_postgres: tuple[str, Engine]) -> None:
    _, engine = migrated_postgres
    with engine.connect() as connection:
        assert connection.scalar(
            text("SELECT has_table_privilege('nextops_app', 'conversations', 'DELETE')")
        )
        assert not connection.scalar(
            text(
                "SELECT has_table_privilege('nextops_support_ro', "
                "'conversation_messages', 'SELECT')"
            )
        )
        assert not connection.scalar(
            text("SELECT has_table_privilege('nextops_app', 'audit_events', 'DELETE')")
        )


def test_audit_failure_rolls_back_answer_and_deletion_cascades(
    chats: tuple[DurableAppService, DurableConversationService, str],
    app_session_factory: sessionmaker[Session],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _, store, token = chats
    chat = store.create(token, "en", uuid4())
    ticket = store.begin(token, chat.conversation_id, payload(), uuid4())
    assert isinstance(ticket, GenerationTicket)

    def broken_audit(*args: object, **kwargs: object) -> None:
        raise SQLAlchemyError("private diagnostic must not escape")

    with monkeypatch.context() as patch:
        patch.setattr(store, "_audit", broken_audit)
        with pytest.raises(ApplicationError) as failure:
            store.complete(token, ticket, assistant(), uuid4())
        assert failure.value.message_key == "conversation.transaction_failed"
        assert failure.value.details == {}
    assert store.get(token, chat.conversation_id, uuid4()).messages == ()
    store.complete(token, ticket, assistant(), uuid4())
    store.delete(token, chat.conversation_id, uuid4())
    with app_session_factory() as session:
        assert session.scalar(select(func.count()).select_from(ConversationMessage)) == 0
        assert (
            session.scalar(
                select(func.count())
                .select_from(AuditEvent)
                .where(
                    AuditEvent.event_type == "conversation.deleted",
                )
            )
            == 1
        )


def test_conversation_and_turn_quotas_are_enforced(
    chats: tuple[DurableAppService, DurableConversationService, str],
    app_session_factory: sessionmaker[Session],
) -> None:
    _, store, token = chats
    chat = store.create(token, "en", uuid4())
    for _ in range(49):
        store.create(token, "en", uuid4())
    with pytest.raises(ApplicationError) as limit:
        store.create(token, "en", uuid4())
    assert limit.value.code == ErrorCode.OVERLOADED
    with app_session_factory() as session, session.begin():
        session.execute(
            update(Conversation)
            .where(Conversation.id == chat.conversation_id)
            .values(
                turn_count=100,
            )
        )
    with pytest.raises(ApplicationError) as full:
        store.begin(token, chat.conversation_id, payload(), uuid4())
    assert full.value.message_key == "conversation.quota_exceeded"


def test_expired_owner_chat_is_purged_after_fresh_login(
    chats: tuple[DurableAppService, DurableConversationService, str],
    app_session_factory: sessionmaker[Session],
) -> None:
    _, store, token = chats
    chat = store.create(token, "en", uuid4())
    future_time = datetime.now(UTC) + timedelta(days=31)
    future = DurableConversationService(app_session_factory, lambda: future_time)
    settings = AppSettings(
        database_url=SecretStr("postgresql+psycopg://unused-in-service"),
        bootstrap_secret=SecretStr("bootstrap-secret-only-for-conversation-tests"),
        recovery_secret=SecretStr("recovery-secret-only-for-conversation-tests"),
    )
    future_service = DurableAppService(app_session_factory, settings, clock=lambda: future_time)
    fresh = future_service.login(
        LoginRequest(
            username="owner",
            password="conversation test password only",
        ),
        uuid4(),
    ).session.access_token
    with pytest.raises(ApplicationError) as expired:
        future.get(fresh, chat.conversation_id, uuid4())
    assert expired.value.code == ErrorCode.NOT_FOUND
    assert future.list(fresh, uuid4()) == ()
    with app_session_factory() as session:
        assert session.get(Conversation, chat.conversation_id) is None


class ChatGateway:
    def __init__(self) -> None:
        self.requests: list[SynthesisRequest] = []
        self.reply = assistant("DNS maps names to addresses.")

    async def generate(
        self, request: SynthesisRequest, correlation_id: object
    ) -> AssistantResponse:
        self.requests.append(request)
        return self.reply

    async def readiness(self) -> InferenceReadiness:
        return InferenceReadiness(
            state="ready",
            model_id=self.reply.model_id,
            runtime_version="v0.4.1",
            cpu_only_required=True,
            max_active_requests=1,
            max_queued_requests=2,
            active_requests=0,
            queued_requests=0,
        )


def test_real_api_authentication_memory_and_no_provider_or_live_controls(
    chats: tuple[DurableAppService, DurableConversationService, str],
) -> None:
    service, store, token = chats
    gateway = ChatGateway()
    client = TestClient(create_app(service, gateway, conversation_service=store))
    assert client.get("/api/v1/conversations").status_code == 401
    headers = {"Authorization": f"Bearer {token}"}
    created = client.post("/api/v1/conversations", headers=headers, json={"locale": "en"})
    assert created.status_code == 201
    chat_id = created.json()["conversation_id"]
    route = f"/api/v1/conversations/{chat_id}/messages"
    first = client.post(route, headers=headers, json=payload().model_dump(mode="json"))
    assert first.status_code == 200
    second = client.post(
        route, headers=headers, json=payload("Give an example.").model_dump(mode="json")
    )
    assert second.status_code == 200
    assert second.json()["message"]["context_turns"] == 1
    assert "DNS maps names" in gateway.requests[-1].question
    assert gateway.requests[-1].detailed and gateway.requests[-1].max_output_tokens == 1024
    assert (
        client.post(
            route, headers=headers, json=payload().model_dump(mode="json") | {"thinking": True}
        ).status_code
        == 403
    )
    assert (
        client.post(
            route, headers=headers, json=payload().model_dump(mode="json") | {"history": []}
        ).status_code
        == 422
    )
    assert len(gateway.requests) == 2
