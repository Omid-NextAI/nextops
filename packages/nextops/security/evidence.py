"""Bounded explicit-label redaction before evidence is prompted, hashed or served.

This is not a detector of arbitrary unlabeled secrets. The collector counterpart
is deliberately standalone for approved offline Linux targets; parity is tested.
"""

import re

from pydantic import BaseModel

SECRET_PATTERN = re.compile(
    r"""(?i)(["']?(?:password|passwd|secret|(?:client[_-]?)secret|(?:access[_-]?|refresh[_-]?|session[_-]?|auth[_-]?)?token|api[_-]?key)["']?\s*[:=]\s*)(\[REDACTED\]|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|[^\s,;}\]]+)"""
)
AUTHORIZATION_PATTERN = re.compile(
    r"""(?i)(["']?authorization["']?\s*[:=]\s*)(\[REDACTED\]|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|(?:basic|bearer)\s+[^\s,;}\]]+|[^\s,;}\]]+)"""
)


def redact_text(value: str, limit: int) -> str:
    """Redact whole quoted values/auth schemes before any bounded clipping."""
    normalized = value.replace("\x00", " ")
    redacted = AUTHORIZATION_PATTERN.sub(lambda m: f"{m.group(1)}[REDACTED]", normalized)
    redacted = SECRET_PATTERN.sub(lambda m: f"{m.group(1)}[REDACTED]", redacted)
    # Never cut a redaction marker into an ambiguous fragment at a field boundary.
    if redacted != normalized and len(redacted) > limit:
        return "[REDACTED]"[:limit]
    return redacted[:limit]


def sanitize_contract[Contract: BaseModel](value: Contract) -> Contract:
    """Revalidate a copy, preserving typed identity/time and all original bounds."""
    updates: dict[str, object] = {}
    for name, field in type(value).model_fields.items():
        member = getattr(value, name)
        if isinstance(member, str):
            limit = next(
                (m.max_length for m in field.metadata if hasattr(m, "max_length")), len(member) + 64
            )
            updates[name] = redact_text(member, limit)
        elif isinstance(member, BaseModel):
            updates[name] = sanitize_contract(member)
        elif isinstance(member, tuple):
            updates[name] = tuple(
                sanitize_contract(m)
                if isinstance(m, BaseModel)
                else redact_text(m, len(m) + 64)
                if isinstance(m, str)
                else m
                for m in member
            )
        else:
            updates[name] = member
    return type(value).model_validate(updates)
