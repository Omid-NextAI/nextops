"""Pure finite redaction tests, without collectors, credentials or network access."""

import ast
import re
from collections.abc import Callable
from pathlib import Path
from typing import cast

import pytest

from nextops.security.evidence import redact_text


@pytest.mark.parametrize(
    "text",
    [
        "password=AUDIT_ONLY_CANARY",
        "password: AUDIT_ONLY_CANARY",
        '{"password": "AUDIT_ONLY_CANARY"}',
        "{'api_key': 'AUDIT_ONLY_CANARY'}",
        "Authorization: Basic AUDIT_ONLY_CANARY",
        "Authorization: Bearer AUDIT_ONLY_CANARY",
        '{"Authorization": "Basic AUDIT_ONLY_CANARY"}',
        "refresh_token = AUDIT_ONLY_CANARY",
        "client-secret: AUDIT_ONLY_CANARY",
    ],
)
def test_explicit_secret_labels_are_redacted_in_both_collectors(text: str) -> None:
    source = Path("scripts/linux_readonly_collector.py").read_text(encoding="utf-8")
    parsed = ast.parse(source)
    allowed = {"SECRET_PATTERN", "AUTHORIZATION_PATTERN"}
    nodes: list[ast.stmt] = [
        n
        for n in parsed.body
        if (
            isinstance(n, ast.Assign)
            and any(isinstance(t, ast.Name) and t.id in allowed for t in n.targets)
        )
        or (isinstance(n, ast.FunctionDef) and n.name == "_safe_text")
    ]
    namespace: dict[str, object] = {"re": re}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), "<pure-redaction>", "exec"), namespace)
    safe_text = cast(Callable[[str, int], str], namespace["_safe_text"])
    for result in (redact_text(text, 512), safe_text(text, 512)):
        assert "AUDIT_ONLY_CANARY" not in result
        assert "[REDACTED]" in result
        assert redact_text(result, 512) == result


def test_redaction_precedes_clipping_and_preserves_ordinary_observations() -> None:
    assert (
        redact_text("CPU idle 91.25%; service zabbix-server active", 256)
        == "CPU idle 91.25%; service zabbix-server active"
    )
    assert "AUDIT" not in redact_text('password="AUDIT_ONLY_CANARY"', 14)
