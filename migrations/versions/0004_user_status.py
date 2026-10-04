"""Add only account activation UPDATE privilege; authorization columns remain immutable."""

from alembic import op

revision: str = "0004_user_status"
down_revision: str | None = "0003_conversations"
branch_labels: str | None = None
depends_on: str | None = None


def upgrade() -> None:
    op.execute("GRANT UPDATE (is_active) ON identities TO nextops_app")


def downgrade() -> None:
    op.execute("REVOKE UPDATE (is_active) ON identities FROM nextops_app")
