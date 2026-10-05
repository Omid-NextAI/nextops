from __future__ import annotations

import ast
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
    "body",
    [
        'return method in ("host.get", "item.get") and isinstance(method, str)',
        'return method in ["host.get", "item.get"] and isinstance(method, str)',
        'return method in {"host.get", "item.get"} and isinstance(method, str)',
        'return True and method in ("host.get", "item.get") and isinstance(method, str)',
        'return (method == "host.get" or method == "item.get") and isinstance(method, str)',
        'return ("host.get" == method or "item.get" == method) and type(method) is str',
        'return not (method not in ("host.get", "item.get") or not isinstance(method, str))',
        (
            'return ((method,) == ("host.get",) or (method,) == ("item.get",)) '
            "and isinstance(method, str)"
        ),
        (
            'if method in ("host.get", "item.get"):\n'
            "        return isinstance(method, str)\n    return False"
        ),
        (
            "return not not method and isinstance(method, str) "
            'and method in ("host.get", "item.get")'
        ),
        (
            "return (method or False) and isinstance(method, str) "
            'and method in ("host.get", "item.get")'
        ),
        (
            "if method:\n"
            '        return isinstance(method, str) and method in ("host.get", "item.get")\n'
            "    return False"
        ),
    ],
)
def test_late_type_guard_is_failed_even_when_finite_return_values_match(body: str) -> None:
    result = module().check(f"def is_allowed(method):\n    {body}\n")
    assert result["status"] == "failed"
    assert {"none", "boolean", "integer", "list", "mapping", "bytes", "equality_spoof"} <= set(
        result["failed_cases"]
    )
    assert result["case_count"] == 12
    assert result["scope"] == "finite_pure_function_ast_review_no_generated_execution"


@pytest.mark.parametrize(
    "body",
    [
        'return type(method) is str and method in ("host.get", "item.get")',
        'return type(method) == str and method in ("host.get", "item.get")',
        'return isinstance(method, str) and (method == "host.get" or method == "item.get")',
        'return (isinstance(method, str) and method) in ("host.get", "item.get")',
        'return not (not isinstance(method, str) or method not in ("host.get", "item.get"))',
        'return ((isinstance(method, str) and method),) in (("host.get",), ("item.get",))',
        (
            "if isinstance(method, str):\n"
            '        return method in ("host.get", "item.get")\n    return False'
        ),
        (
            "if type(method) is not str:\n        return False\n"
            '    return method in ("host.get", "item.get")'
        ),
        (
            "return isinstance(method, str) and not not method "
            'and method in ("host.get", "item.get")'
        ),
        (
            "if not isinstance(method, str):\n        return False\n"
            '    if method:\n        return method in ("host.get", "item.get")\n'
            "    return False"
        ),
    ],
)
def test_guard_first_keeps_supported_short_circuit_and_early_return_forms(body: str) -> None:
    result = module().check(f"def is_allowed(method):\n    {body}\n")
    assert result["status"] == "passed"
    assert result["failed_cases"] == []
    assert result["case_count"] == 12


@pytest.mark.parametrize(
    "operation",
    [
        'method in ("host.get", "item.get")',
        'method not in {"host.get", "item.get"}',
        'method == "host.get"',
        '"host.get" != method',
        '(method,) == ("host.get",)',
        '"host.get" in (method, "item.get")',
        "{method}",
        "not method",
        "not not method",
        "method and True",
        "method or False",
    ],
)
def test_interpreter_rejects_unguarded_input_before_equality_or_hash_side_effects(
    operation: str,
) -> None:
    class SideEffectInput:
        def __eq__(self, other: object) -> bool:
            raise AssertionError("review must not invoke unguarded input equality")

        def __hash__(self) -> int:
            raise AssertionError("review must not invoke unguarded input hashing")

        def __bool__(self) -> bool:
            raise AssertionError("review must not invoke unguarded input truthiness")

    checker = module()
    with pytest.raises(checker.UnsafeInputOperationError):
        checker.expression(ast.parse(operation, mode="eval").body, SideEffectInput())


def test_if_condition_rejects_unguarded_input_before_truthiness() -> None:
    class SideEffectInput:
        def __bool__(self) -> bool:
            raise AssertionError("review must not coerce unguarded if-condition input")

    checker = module()
    function = ast.parse("def is_allowed(method):\n    if method:\n        return False").body[0]
    assert isinstance(function, ast.FunctionDef)
    with pytest.raises(checker.UnsafeInputOperationError):
        checker.statements(function.body, SideEffectInput())


def test_guard_does_not_expand_the_supported_membership_language() -> None:
    code = 'def is_allowed(method):\n    return isinstance(method, str) and method in "host.get"\n'
    assert module().check(code)["status"] == "manual_review_required"


@pytest.mark.parametrize("case_id", ["en-coding", "fa-coding"])
def test_offline_trial_review_cannot_promote_a_late_type_guard(
    case_id: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.syspath_prepend(str(Path(__file__).resolve().parents[2]))
    from scripts.review_model_trial import review

    result = review(
        {
            "cases": [
                {
                    "id": case_id,
                    "answer": (
                        'def is_allowed(method):\n    return method in ("host.get", "item.get") '
                        "and isinstance(method, str)\n"
                    ),
                    "elapsed_ms": 1000,
                    "finish_reason": "stop",
                }
            ]
        }
    )
    assert result["status"] == result["cases"][0]["status"] == "failed"
    assert "equality_spoof" in result["cases"][0]["failed_cases"]
    assert result["production_acceptance"] is result["deployment_selection_allowed"] is False
    assert len(result["missing_cases"]) == 15


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
