from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any

import pytest


def module() -> Any:
    spec = importlib.util.spec_from_file_location(
        "coding_review",
        Path(__file__).resolve().parents[2] / "scripts/check_model_coding_invariant.py",
    )
    assert spec and spec.loader
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


@pytest.mark.parametrize("collection", ['("host.get", "item.get")', '{"host.get", "item.get"}'])
def test_typed_guard_satisfies_finite_invariant(collection: str) -> None:
    code = (
        f"def is_allowed(method):\n    return isinstance(method, str) and method in {collection}\n"
    )
    assert module().check(code)["status"] == "passed"


def test_frozen_failed_model_output_is_not_a_coding_pass() -> None:
    code = 'def is_allowed(method):\n    return method in ("host.get", "item.get")\n'
    result = module().check(code)
    assert result["status"] == "failed"
    assert "equality_spoof" in result["failed_cases"]


def test_guarded_early_return_and_code_fence_are_supported() -> None:
    code = (
        "```python\ndef is_allowed(method):\n    if not isinstance(method, str):\n"
        '        return False\n    return method in ("host.get", "item.get")\n```'
    )
    assert module().check(code)["status"] == "passed"


@pytest.mark.parametrize(
    "code",
    [
        "import os\ndef is_allowed(method):\n    return True",
        'def is_allowed(method):\n    return __import__("os").system("echo unsafe")',
        "@unexpected()\ndef is_allowed(method):\n    return True",
        "def is_allowed(method):\n    while True:\n        pass",
        (
            "def is_allowed(method):\n    if False:\n"
            '        __import__("os").system("unsafe")\n    return False'
        ),
    ],
)
def test_arbitrary_generated_code_is_never_executed(code: str) -> None:
    result = module().check(code)
    assert result["status"] != "passed"
    assert result["scope"].endswith("no_generated_execution")
