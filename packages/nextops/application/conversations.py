"""Bounded private chat storage. Model context is never policy or live evidence."""

import json
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from hashlib import sha256
from typing import Literal
from uuid import UUID, uuid4

from pydantic import ValidationError
from sqlalchemy import delete, func, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker

from nextops.application.errors import ApplicationError
from nextops.contracts.assistant import AssistantResponse
from nextops.contracts.conversations import (
    ConversationAssistantRequest,
    ConversationMessageRequest,
    ConversationPage,
    ConversationSummary,
    SavedContextTurn,
    SavedMessage,
)
from nextops.contracts.errors import ErrorCode
from nextops.persistence.conversations import Conversation, ConversationMessage
from nextops.persistence.models import AuditEvent, Identity
from nextops.persistence.models import Session as SessionModel
from nextops.security.secrets import hash_opaque_token

MAX_CONVERSATIONS = 50
MAX_TURNS = 100
MAX_BYTES = 1_048_576
CONTEXT_CHARACTERS = 12_000
RETENTION = timedelta(days=30)
PENDING_TTL = timedelta(seconds=540)


def select_context(messages: list[SavedMessage]) -> tuple[tuple[SavedContextTurn, ...], bool]:
    """Select whole recent pairs, never clipped text or rejected/generated evidence."""
    eligible = [
        SavedContextTurn(question=m.question, answer=m.assistant.answer)
        for m in messages
        if m.assistant.evidence_mode == "model_only"
        and m.assistant.integrity_status == "model_unverified"
    ]
    selected: list[SavedContextTurn] = []
    for turn in reversed(eligible[-6:]):
        candidate = [turn, *selected]
        if (
            len(json.dumps([t.model_dump() for t in candidate], ensure_ascii=False))
            > CONTEXT_CHARACTERS
        ):
            break
        selected = candidate
    return tuple(selected), len(selected) < len(messages)


def request_hash(request: ConversationMessageRequest) -> str:
    return sha256(request.model_dump_json().encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class GenerationTicket:
    conversation_id: UUID
    nonce: UUID
    payload: ConversationMessageRequest
    context: ConversationAssistantRequest
    context_omitted: bool


class DurableConversationService:
    """Every operation rechecks the same local session inside its DB transaction."""

    def __init__(
        self,
        session_factory: sessionmaker[Session],
        clock: Callable[[], datetime] | None = None,
    ) -> None:
        self._factory = session_factory
        self._clock = clock or (lambda: datetime.now(UTC))

    @contextmanager
    def _transaction(self, token: str) -> Iterator[tuple[Session, Identity, datetime]]:
        try:
            with self._factory() as session, session.begin():
                now = self._clock()
                # Lock session/identity briefly so logout/recovery and quota checks serialize.
                identity = session.scalar(
                    select(Identity)
                    .join(SessionModel, SessionModel.identity_id == Identity.id)
                    .where(
                        SessionModel.token_sha256 == hash_opaque_token(token),
                        SessionModel.revoked_at.is_(None),
                        SessionModel.expires_at > now,
                        SessionModel.credential_version == Identity.credential_version,
                        Identity.is_active.is_(True),
                    )
                    .with_for_update(of=(Identity, SessionModel))
                )
                if identity is None:
                    raise ApplicationError(ErrorCode.UNAUTHENTICATED, "auth.session_required")
                yield session, identity, now
        except (SQLAlchemyError, ValidationError) as error:
            raise ApplicationError(
                ErrorCode.DEPENDENCY_UNAVAILABLE,
                "conversation.transaction_failed",
                retryable=True,
            ) from error

    @staticmethod
    def _owned(
        session: Session,
        identity: Identity,
        conversation_id: UUID,
        now: datetime,
    ) -> Conversation:
        conversation = session.scalar(
            select(Conversation)
            .where(
                Conversation.id == conversation_id,
                Conversation.owner_id == identity.id,
                Conversation.organization_id == identity.organization_id,
                Conversation.environment_id == identity.environment_id,
                Conversation.expires_at > now,
            )
            .with_for_update()
        )
        if conversation is None:
            # Identical response for absent, expired, and someone else's conversation.
            raise ApplicationError(ErrorCode.NOT_FOUND, "conversation.not_found")
        return conversation

    @staticmethod
    def _summary(conversation: Conversation) -> ConversationSummary:
        return ConversationSummary(
            conversation_id=conversation.id,
            title=conversation.title,
            locale=conversation.locale,
            created_at=conversation.created_at,
            updated_at=conversation.updated_at,
            expires_at=conversation.expires_at,
            turn_count=conversation.turn_count,
        )

    @staticmethod
    def _message(message: ConversationMessage) -> SavedMessage:
        return SavedMessage(
            request_id=message.request_id,
            sequence=message.sequence,
            question=message.question,
            assistant=AssistantResponse.model_validate(message.assistant),
            thinking_requested=message.thinking_requested,
            context_turns=message.context_turns,
            context_omitted=message.context_omitted,
            created_at=message.created_at,
        )

    @staticmethod
    def _audit(
        session: Session,
        identity: Identity,
        correlation_id: UUID,
        now: datetime,
        event: str,
        conversation_id: UUID | None = None,
        request_id: UUID | None = None,
    ) -> None:
        # Deliberately omit titles, question/answer text, tokens, and private reasoning.
        session.add(
            AuditEvent(
                id=uuid4(),
                organization_id=identity.organization_id,
                environment_id=identity.environment_id,
                actor_id=identity.id,
                correlation_id=correlation_id,
                event_type=f"conversation.{event}",
                outcome="accepted",
                occurred_at=now,
                details={
                    "conversation_id": str(conversation_id) if conversation_id else None,
                    "request_id": str(request_id) if request_id else None,
                },
            )
        )

    def _purge_expired(
        self,
        session: Session,
        identity: Identity,
        correlation_id: UUID,
        now: datetime,
    ) -> None:
        expired = list(
            session.scalars(
                select(Conversation.id)
                .where(
                    Conversation.owner_id == identity.id,
                    Conversation.expires_at <= now,
                )
                .limit(MAX_CONVERSATIONS)
            )
        )
        for conversation_id in expired:
            session.execute(delete(Conversation).where(Conversation.id == conversation_id))
            self._audit(session, identity, correlation_id, now, "expired", conversation_id)

    def create(
        self,
        token: str,
        locale: Literal["en", "fa"],
        correlation_id: UUID,
    ) -> ConversationSummary:
        with self._transaction(token) as (session, identity, now):
            self._purge_expired(session, identity, correlation_id, now)
            count = session.scalar(
                select(func.count())
                .select_from(Conversation)
                .where(
                    Conversation.owner_id == identity.id,
                )
            )
            if count is not None and count >= MAX_CONVERSATIONS:
                raise ApplicationError(ErrorCode.OVERLOADED, "conversation.quota_exceeded")
            conversation = Conversation(
                id=uuid4(),
                owner_id=identity.id,
                organization_id=identity.organization_id,
                environment_id=identity.environment_id,
                locale=locale,
                title="گفت‌وگوی تازه" if locale == "fa" else "New chat",
                created_at=now,
                updated_at=now,
                expires_at=now + RETENTION,
                turn_count=0,
                content_bytes=0,
            )
            session.add(conversation)
            self._audit(session, identity, correlation_id, now, "created", conversation.id)
            session.flush()
            return self._summary(conversation)

    def list(self, token: str, correlation_id: UUID) -> tuple[ConversationSummary, ...]:
        with self._transaction(token) as (session, identity, now):
            self._purge_expired(session, identity, correlation_id, now)
            conversations = session.scalars(
                select(Conversation)
                .where(
                    Conversation.owner_id == identity.id,
                    Conversation.organization_id == identity.organization_id,
                    Conversation.environment_id == identity.environment_id,
                    Conversation.expires_at > now,
                )
                .order_by(Conversation.updated_at.desc(), Conversation.id)
                .limit(MAX_CONVERSATIONS)
            )
            self._audit(session, identity, correlation_id, now, "listed")
            return tuple(self._summary(c) for c in conversations)

    def get(
        self,
        token: str,
        conversation_id: UUID,
        correlation_id: UUID,
        before_sequence: int = 101,
    ) -> ConversationPage:
        with self._transaction(token) as (session, identity, now):
            conversation = self._owned(session, identity, conversation_id, now)
            messages = list(
                session.scalars(
                    select(ConversationMessage)
                    .where(
                        ConversationMessage.conversation_id == conversation_id,
                        ConversationMessage.sequence < before_sequence,
                    )
                    .order_by(ConversationMessage.sequence.desc())
                    .limit(20)
                )
            )
            messages.reverse()
            self._audit(session, identity, correlation_id, now, "read", conversation_id)
            return ConversationPage(
                conversation=self._summary(conversation),
                messages=tuple(self._message(m) for m in messages),
                before_sequence=messages[0].sequence
                if messages and messages[0].sequence > 1
                else None,
            )

    def delete(self, token: str, conversation_id: UUID, correlation_id: UUID) -> None:
        with self._transaction(token) as (session, identity, now):
            conversation = self._owned(session, identity, conversation_id, now)
            session.delete(conversation)
            self._audit(session, identity, correlation_id, now, "deleted", conversation_id)

    def begin(
        self,
        token: str,
        conversation_id: UUID,
        payload: ConversationMessageRequest,
        correlation_id: UUID,
    ) -> GenerationTicket | SavedMessage:
        with self._transaction(token) as (session, identity, now):
            conversation = self._owned(session, identity, conversation_id, now)
            existing = session.get(ConversationMessage, (conversation_id, payload.request_id))
            if existing is not None:
                if existing.request_sha256 != request_hash(payload):
                    raise ApplicationError(ErrorCode.CONFLICT, "conversation.request_conflict")
                self._audit(
                    session,
                    identity,
                    correlation_id,
                    now,
                    "replayed",
                    conversation_id,
                    payload.request_id,
                )
                return self._message(existing)
            if conversation.pending_until is not None and conversation.pending_until > now:
                raise ApplicationError(
                    ErrorCode.CONFLICT, "conversation.generation_pending", retryable=True
                )
            if conversation.turn_count >= MAX_TURNS or conversation.content_bytes >= MAX_BYTES:
                raise ApplicationError(ErrorCode.OVERLOADED, "conversation.quota_exceeded")
            messages = [
                self._message(m)
                for m in session.scalars(
                    select(ConversationMessage)
                    .where(
                        ConversationMessage.conversation_id == conversation_id,
                    )
                    .order_by(ConversationMessage.sequence)
                    .limit(MAX_TURNS)
                )
            ]
            context, omitted = select_context(messages)
            nonce = uuid4()
            conversation.pending_nonce = nonce
            conversation.pending_until = now + PENDING_TTL
            self._audit(
                session,
                identity,
                correlation_id,
                now,
                "started",
                conversation_id,
                payload.request_id,
            )
            return GenerationTicket(
                conversation_id=conversation_id,
                nonce=nonce,
                payload=payload,
                context=ConversationAssistantRequest(
                    locale=payload.locale,
                    question=payload.question,
                    history=context,
                    thinking=payload.thinking,
                    max_output_tokens=2_048 if payload.thinking else 1_024,
                ),
                context_omitted=omitted,
            )

    def complete(
        self,
        token: str,
        ticket: GenerationTicket,
        assistant: AssistantResponse,
        correlation_id: UUID,
    ) -> SavedMessage:
        with self._transaction(token) as (session, identity, now):
            conversation = self._owned(session, identity, ticket.conversation_id, now)
            if (
                conversation.pending_nonce != ticket.nonce
                or conversation.pending_until is None
                or conversation.pending_until <= now
            ):
                raise ApplicationError(ErrorCode.CONFLICT, "conversation.generation_expired")
            if assistant.evidence_mode != "model_only" or assistant.live_monitoring_data:
                raise ApplicationError(ErrorCode.INTERNAL_ERROR, "conversation.evidence_rejected")
            payload = assistant.model_dump(mode="json")
            size = len(ticket.payload.question.encode("utf-8")) + len(
                json.dumps(payload, ensure_ascii=False).encode("utf-8")
            )
            if conversation.content_bytes + size > MAX_BYTES:
                raise ApplicationError(ErrorCode.OVERLOADED, "conversation.quota_exceeded")
            message = ConversationMessage(
                conversation_id=ticket.conversation_id,
                request_id=ticket.payload.request_id,
                request_sha256=request_hash(ticket.payload),
                sequence=conversation.turn_count + 1,
                question=ticket.payload.question,
                assistant=payload,
                thinking_requested=ticket.payload.thinking,
                context_turns=len(ticket.context.history),
                context_omitted=ticket.context_omitted,
                created_at=now,
            )
            session.add(message)
            conversation.turn_count += 1
            conversation.content_bytes += size
            conversation.pending_nonce = None
            conversation.pending_until = None
            conversation.updated_at = now
            if conversation.turn_count == 1:
                conversation.title = ticket.payload.question[:80]
            self._audit(
                session,
                identity,
                correlation_id,
                now,
                "completed",
                conversation.id,
                message.request_id,
            )
            session.flush()
            return self._message(message)

    def fail(self, token: str, ticket: GenerationTicket, correlation_id: UUID) -> None:
        with self._transaction(token) as (session, identity, now):
            conversation = self._owned(session, identity, ticket.conversation_id, now)
            if conversation.pending_nonce == ticket.nonce:
                conversation.pending_nonce = None
                conversation.pending_until = None
                self._audit(
                    session,
                    identity,
                    correlation_id,
                    now,
                    "failed",
                    conversation.id,
                    ticket.payload.request_id,
                )
