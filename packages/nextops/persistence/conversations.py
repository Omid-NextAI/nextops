"""Additive PostgreSQL mappings for private model-only conversation history."""

from datetime import datetime
from typing import Any
from uuid import UUID

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    DateTime,
    ForeignKey,
    ForeignKeyConstraint,
    Index,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from nextops.persistence.models import Base


class Conversation(Base):
    __tablename__ = "conversations"
    __table_args__ = (
        ForeignKeyConstraint(
            ["owner_id", "organization_id", "environment_id"],
            ["identities.id", "identities.organization_id", "identities.environment_id"],
            ondelete="RESTRICT",
            name="fk_conversations_owner_scope",
        ),
        CheckConstraint("turn_count BETWEEN 0 AND 100", name="ck_conversations_turns"),
        CheckConstraint("content_bytes BETWEEN 0 AND 1048576", name="ck_conversations_bytes"),
        CheckConstraint("locale IN ('en', 'fa')", name="ck_conversations_locale"),
        CheckConstraint("expires_at > created_at", name="ck_conversations_expiry"),
        CheckConstraint(
            "(pending_nonce IS NULL AND pending_until IS NULL) OR "
            "(pending_nonce IS NOT NULL AND pending_until IS NOT NULL)",
            name="ck_conversations_pending",
        ),
        Index("ix_conversations_owner", "owner_id", "updated_at"),
    )

    id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True)
    owner_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), nullable=False)
    organization_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), nullable=False)
    environment_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), nullable=False)
    title: Mapped[str] = mapped_column(String(80), nullable=False)
    locale: Mapped[str] = mapped_column(String(2), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    turn_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    content_bytes: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    pending_nonce: Mapped[UUID | None] = mapped_column(PGUUID(as_uuid=True))
    pending_until: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))


class ConversationMessage(Base):
    __tablename__ = "conversation_messages"
    __table_args__ = (
        UniqueConstraint("conversation_id", "sequence", name="uq_conversation_message_sequence"),
        CheckConstraint("sequence BETWEEN 1 AND 100", name="ck_conversation_message_sequence"),
        CheckConstraint(
            "char_length(question) BETWEEN 1 AND 4000", name="ck_conversation_question"
        ),
        CheckConstraint("context_turns BETWEEN 0 AND 6", name="ck_conversation_context_turns"),
    )

    conversation_id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("conversations.id", ondelete="CASCADE"),
        primary_key=True,
    )
    request_id: Mapped[UUID] = mapped_column(PGUUID(as_uuid=True), primary_key=True)
    request_sha256: Mapped[str] = mapped_column(String(64), nullable=False)
    sequence: Mapped[int] = mapped_column(Integer, nullable=False)
    question: Mapped[str] = mapped_column(Text, nullable=False)
    assistant: Mapped[dict[str, Any]] = mapped_column(JSONB, nullable=False)
    thinking_requested: Mapped[bool] = mapped_column(Boolean, nullable=False)
    context_turns: Mapped[int] = mapped_column(Integer, nullable=False)
    context_omitted: Mapped[bool] = mapped_column(Boolean, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
