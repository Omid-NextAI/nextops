"""Add owner-scoped model-only chats; no grants to support or connector roles."""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import JSONB, UUID

revision: str = "0003_conversations"
down_revision: str | None = "0002_phase2_linux_read"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "conversations",
        sa.Column("id", UUID(as_uuid=True), primary_key=True),
        sa.Column("owner_id", UUID(as_uuid=True), nullable=False),
        sa.Column("organization_id", UUID(as_uuid=True), nullable=False),
        sa.Column("environment_id", UUID(as_uuid=True), nullable=False),
        sa.Column("title", sa.String(80), nullable=False),
        sa.Column("locale", sa.String(2), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("turn_count", sa.Integer(), nullable=False),
        sa.Column("content_bytes", sa.Integer(), nullable=False),
        sa.Column("pending_nonce", UUID(as_uuid=True)),
        sa.Column("pending_until", sa.DateTime(timezone=True)),
        sa.ForeignKeyConstraint(
            ["owner_id", "organization_id", "environment_id"],
            ["identities.id", "identities.organization_id", "identities.environment_id"],
            ondelete="RESTRICT",
            name="fk_conversations_owner_scope",
        ),
        sa.CheckConstraint("turn_count BETWEEN 0 AND 100", name="ck_conversations_turns"),
        sa.CheckConstraint("content_bytes BETWEEN 0 AND 1048576", name="ck_conversations_bytes"),
        sa.CheckConstraint("locale IN ('en', 'fa')", name="ck_conversations_locale"),
        sa.CheckConstraint("expires_at > created_at", name="ck_conversations_expiry"),
        sa.CheckConstraint(
            "(pending_nonce IS NULL AND pending_until IS NULL) OR "
            "(pending_nonce IS NOT NULL AND pending_until IS NOT NULL)",
            name="ck_conversations_pending",
        ),
    )
    op.create_index("ix_conversations_owner", "conversations", ["owner_id", "updated_at"])
    op.create_table(
        "conversation_messages",
        sa.Column(
            "conversation_id",
            UUID(as_uuid=True),
            sa.ForeignKey("conversations.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column("request_id", UUID(as_uuid=True), primary_key=True),
        sa.Column("request_sha256", sa.String(64), nullable=False),
        sa.Column("sequence", sa.Integer(), nullable=False),
        sa.Column("question", sa.Text(), nullable=False),
        sa.Column("assistant", JSONB(), nullable=False),
        sa.Column("thinking_requested", sa.Boolean(), nullable=False),
        sa.Column("context_turns", sa.Integer(), nullable=False),
        sa.Column("context_omitted", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.UniqueConstraint("conversation_id", "sequence", name="uq_conversation_message_sequence"),
        sa.CheckConstraint("sequence BETWEEN 1 AND 100", name="ck_conversation_message_sequence"),
        sa.CheckConstraint(
            "char_length(question) BETWEEN 1 AND 4000", name="ck_conversation_question"
        ),
        sa.CheckConstraint("context_turns BETWEEN 0 AND 6", name="ck_conversation_context_turns"),
    )
    op.execute("REVOKE ALL ON conversations, conversation_messages FROM PUBLIC, nextops_support_ro")
    op.execute(
        "GRANT SELECT, INSERT, UPDATE, DELETE ON conversations, conversation_messages "
        "TO nextops_app"
    )


def downgrade() -> None:
    """Destructive: export private transcripts before an explicitly approved downgrade."""
    op.drop_table("conversation_messages")
    op.drop_table("conversations")
