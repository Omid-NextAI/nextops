"""Review one bounded pure-function invariant without executing generated Python."""

from __future__ import annotations

import ast
import re
from typing import Any


class UnsupportedCodeError(ValueError):
    """The submitted snippet exceeds the deliberately small review language."""


class UnsafeInputOperationError(ValueError):
    """A supported expression touches non-string input before its type guard."""


class EvaluatedValue:
    """Track input provenance through the bounded interpreter, never generated code."""

    def __init__(self, value: Any, nonstring_input: bool = False) -> None:
        self.value = value
        self.nonstring_input = nonstring_input


class EqualToEverything:
    """Synthetic non-string counterexample to unsafe string membership alone."""

    def __eq__(self, other: object) -> bool:
        return True

    __hash__ = None  # type: ignore[assignment]


def truth_value(evaluated: EvaluatedValue) -> bool:
    if evaluated.nonstring_input:
        raise UnsafeInputOperationError("non-string input coerced before type guard")
    return bool(evaluated.value)


def evaluated_expression(node: ast.expr, value: object) -> EvaluatedValue:
    if isinstance(node, ast.Name) and node.id in {"method", "str"}:
        return (
            EvaluatedValue(value, nonstring_input=not isinstance(value, str))
            if node.id == "method"
            else EvaluatedValue(str)
        )
    if isinstance(node, ast.Constant) and (
        node.value is None
        or type(node.value) is bool
        or (type(node.value) is str and len(node.value) <= 64)
    ):
        return EvaluatedValue(node.value)
    if isinstance(node, (ast.Tuple, ast.List, ast.Set)) and len(node.elts) <= 8:
        elements = [evaluated_expression(child, value) for child in node.elts]
        nonstring_input = any(element.nonstring_input for element in elements)
        if isinstance(node, ast.Set) and nonstring_input:
            raise UnsafeInputOperationError("non-string input hashed before type guard")
        contents = [element.value for element in elements]
        return EvaluatedValue(
            set(contents) if isinstance(node, ast.Set) else tuple(contents), nonstring_input
        )
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and not node.keywords:
        if node.func.id == "isinstance" and len(node.args) == 2:
            target = evaluated_expression(node.args[1], value).value
            if target is str:
                return EvaluatedValue(
                    isinstance(evaluated_expression(node.args[0], value).value, str)
                )
        if node.func.id == "type" and len(node.args) == 1:
            return EvaluatedValue(type(evaluated_expression(node.args[0], value).value))
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
        return EvaluatedValue(not truth_value(evaluated_expression(node.operand, value)))
    if isinstance(node, ast.BoolOp) and 2 <= len(node.values) <= 4:
        current = evaluated_expression(node.values[0], value)
        for child in node.values[1:]:
            truth = truth_value(current)
            if isinstance(node.op, ast.And) and not truth:
                return current
            if isinstance(node.op, ast.Or) and truth:
                return current
            current = evaluated_expression(child, value)
        return current
    if isinstance(node, ast.Compare) and len(node.ops) == len(node.comparators) == 1:
        left = evaluated_expression(node.left, value)
        right = evaluated_expression(node.comparators[0], value)
        operation = node.ops[0]
        if isinstance(operation, (ast.In, ast.NotIn)) and not isinstance(right.value, (tuple, set)):
            raise UnsupportedCodeError("unsupported membership container; manual review required")
        if isinstance(operation, (ast.In, ast.NotIn, ast.Eq, ast.NotEq)) and (
            left.nonstring_input or right.nonstring_input
        ):
            raise UnsafeInputOperationError("non-string input compared before type guard")
        if isinstance(operation, (ast.In, ast.NotIn)) and isinstance(right.value, (tuple, set)):
            member = left.value in right.value
            return EvaluatedValue(member if isinstance(operation, ast.In) else not member)
        if isinstance(operation, ast.Eq):
            return EvaluatedValue(left.value == right.value)
        if isinstance(operation, ast.NotEq):
            return EvaluatedValue(left.value != right.value)
        if isinstance(operation, ast.Is):
            return EvaluatedValue(left.value is right.value)
        if isinstance(operation, ast.IsNot):
            return EvaluatedValue(left.value is not right.value)
    raise UnsupportedCodeError("unsupported expression; manual review required")


def expression(node: ast.expr, value: object) -> Any:
    return evaluated_expression(node, value).value


def statements(body: list[ast.stmt], value: object) -> tuple[bool, Any]:
    for node in body:
        if isinstance(node, ast.Return) and node.value is not None:
            return True, expression(node.value, value)
        if isinstance(node, ast.If):
            branch = (
                node.body if truth_value(evaluated_expression(node.test, value)) else node.orelse
            )
            returned, result = statements(branch, value)
            if returned:
                return True, result
        else:
            raise UnsupportedCodeError("only bounded if/return bodies are supported")
    return False, None


def check(answer: str) -> dict[str, Any]:
    """A pass is this finite invariant only, never authorization or whole-code approval."""
    result: dict[str, Any] = {"scope": "finite_pure_function_ast_review_no_generated_execution"}
    try:
        if len(answer) > 16_000:
            raise UnsupportedCodeError("answer bound exceeded")
        fenced = re.findall(r"```(?:python|py)?\s*\n(.*?)```", answer, re.DOTALL)
        code = fenced[0] if len(fenced) == 1 else answer
        tree = ast.parse(code)
        if len(list(ast.walk(tree))) > 128 or len(tree.body) != 1:
            raise UnsupportedCodeError("AST bound or function count exceeded")
        function = tree.body[0]
        if not isinstance(function, ast.FunctionDef) or function.name != "is_allowed":
            raise UnsupportedCodeError("expected is_allowed function")
        args = function.args
        if (
            function.decorator_list
            or len(args.args) != 1
            or args.args[0].arg != "method"
            or args.posonlyargs
            or args.kwonlyargs
            or args.vararg
            or args.kwarg
            or args.defaults
        ):
            raise UnsupportedCodeError("unsupported function signature")
        allowed_nodes = (
            ast.Module,
            ast.FunctionDef,
            ast.arguments,
            ast.arg,
            ast.Return,
            ast.If,
            ast.Name,
            ast.Constant,
            ast.Tuple,
            ast.List,
            ast.Set,
            ast.Call,
            ast.UnaryOp,
            ast.Not,
            ast.BoolOp,
            ast.And,
            ast.Or,
            ast.Compare,
            ast.In,
            ast.NotIn,
            ast.Eq,
            ast.NotEq,
            ast.Is,
            ast.IsNot,
            ast.Load,
        )
        if any(not isinstance(node, allowed_nodes) for node in ast.walk(tree)):
            raise UnsupportedCodeError("unsupported AST node, including unreachable branches")
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and (
                not isinstance(node.func, ast.Name)
                or node.func.id not in {"isinstance", "type"}
                or node.keywords
            ):
                raise UnsupportedCodeError("unapproved call, including unreachable branches")
        # Validation never imports, compiles or evaluates the submitted function/annotations.
        cases: list[tuple[str, object, bool]] = [
            ("host_get", "host.get", True),
            ("item_get", "item.get", True),
            ("wrong_method", "host.delete", False),
            ("case_sensitive", "HOST.GET", False),
            ("whitespace", "host.get ", False),
            ("none", None, False),
            ("boolean", True, False),
            ("integer", 1, False),
            ("list", ["host.get"], False),
            ("mapping", {}, False),
            ("bytes", b"host.get", False),
            ("equality_spoof", EqualToEverything(), False),
        ]
        failures = []
        for name, value, expected in cases:
            try:
                returned, observed = statements(function.body, value)
                if not returned or type(observed) is not bool or observed is not expected:
                    failures.append(name)
            except UnsupportedCodeError:
                raise
            except (TypeError, ValueError, RecursionError):
                failures.append(name)
        result.update(
            status="failed" if failures else "passed", failed_cases=failures, case_count=len(cases)
        )
    except (UnsupportedCodeError, SyntaxError, RecursionError):
        result.update(status="manual_review_required", reason="unsupported_bounded_ast")
    return result
