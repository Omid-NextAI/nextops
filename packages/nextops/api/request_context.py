"""Request correlation without an optional protocol dependency."""

from contextvars import ContextVar
from uuid import UUID

CALL_CORRELATION: ContextVar[UUID | None] = ContextVar("mcp_correlation", default=None)
