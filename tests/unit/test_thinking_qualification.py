"""Qualification checks cannot convert native probes into serving feature acceptance."""

import argparse
import asyncio
import importlib.util
import json
from pathlib import Path
from types import ModuleType, SimpleNamespace
from typing import Any

import pytest
from pydantic import SecretStr

from nextops.application.errors import ApplicationError
from nextops.contracts.errors import ErrorCode


def module() -> ModuleType:
    path = Path(__file__).resolve().parents[2] / "scripts/qualify_thinking.py"
    spec = importlib.util.spec_from_file_location("qualify_thinking", path)
    assert spec is not None and spec.loader is not None
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


def test_short_cases_use_exact_saved_chat_controls_and_both_locales() -> None:
    cases = module().short_cases()
    assert len(cases) == 8
    assert {payload.locale for _, payload, _ in cases} == {"en", "fa"}
    assert all(payload.thinking and payload.detailed for _, payload, _ in cases)
    assert all(payload.max_output_tokens == 2048 for _, payload, _ in cases)
    assert all("Prior general conversation JSON" in payload.prompt for _, payload, _ in cases)
    assert sum(expected is not None for _, _, expected in cases) == 4


@pytest.mark.parametrize(
    ("answer", "expected"),
    [
        (" ۲۵٪ ", "25%"),
        ("٢٥٪", "25%"),
        ("25%", "25%"),
        ("بیست و پنج درصد", "بیست و پنج درصد"),
        ("25% because 55/220", "25% because 55/220"),
        ("CASE-628", "CASE-628"),
    ],
)
def test_exact_check_accepts_numeral_glyphs_but_does_not_erase_explanations(
    answer: str, expected: str
) -> None:
    assert module().normalized_exact_answer(answer) == expected


def test_context_cannot_evade_application_character_quotas() -> None:
    for locale in ("en", "fa"):
        payload = module().context_request(locale, 5700)
        assert len(payload.prompt) <= 32000
        assert "EARLY-" in payload.prompt
    with pytest.raises(ValueError, match="saved context exceeds"):
        module().context_request("en", 6100)
    with pytest.raises(ValueError):
        module().request("en", "x" * 4001)


@pytest.mark.parametrize("thinking", [False, True])
def test_fresh_technical_cases_are_bilingual_bounded_and_not_a_semantic_judge(
    thinking: bool,
) -> None:
    cases = module().technical_cases(thinking)
    assert len(cases) == 14
    assert {payload.locale for _, payload, _ in cases} == {"en", "fa"}
    assert all(payload.thinking is thinking and payload.detailed for _, payload, _ in cases)
    assert all(payload.max_output_tokens == (2048 if thinking else 1024) for _, payload, _ in cases)
    assert sum(expected is not None for _, _, expected in cases) == 4
    assert not any(
        "502" in payload.prompt or "TICKET-732" in payload.prompt for _, payload, _ in cases
    )


@pytest.mark.parametrize("thinking", [False, True])
def test_new_capability_corpus_has_explicit_review_and_unchanged_budgets(thinking: bool) -> None:
    runner = module()
    cases = runner.capability_cases(thinking)
    assert len(cases) == 18
    assert len({name for name, _, _ in cases}) == 18
    assert {payload.locale for _, payload, _ in cases} == {"en", "fa"}
    assert all(payload.thinking is thinking and payload.detailed for _, payload, _ in cases)
    assert all(payload.max_output_tokens == (2048 if thinking else 1024) for _, payload, _ in cases)
    assert sum(exact is not None for _, _, exact in cases) == 4
    assert set(runner.CAPABILITY_REVIEW_CRITERIA) == {
        name.rsplit("-", 1)[-1] for name, _, _ in cases
    }
    for name, payload, _ in cases:
        if name.endswith("history"):
            assert "Some prior exchanges were omitted" in payload.prompt
            assert "ignore policy" in payload.prompt
        if name.endswith("coding"):
            assert "parse_port" in payload.prompt and "ValueError" in payload.prompt
    old_ids = {name for name, _, _ in runner.technical_cases(thinking)}
    assert old_ids.isdisjoint(name for name, _, _ in cases)


@pytest.mark.parametrize("port", [8080, 8082])
def test_qwen36_probe_cannot_contact_the_serving_or_arbitrary_native_port(
    tmp_path: Path, port: int
) -> None:
    runner = module()
    output = tmp_path / "must-not-exist.json"
    args = argparse.Namespace(
        model=runner.QWEN36,
        provider_port=port,
        mode="thinking",
        scope="technical",
        output=output,
        expected_app_code_sha256=runner.APP_CODE_SHA256,
    )
    with pytest.raises(ValueError):
        asyncio.run(runner.qualify(args))
    assert not output.exists()


def test_private_report_is_exclusive_and_not_inside_repository(tmp_path: Path) -> None:
    tmp_path.chmod(0o700)
    report = tmp_path / "report.json"
    module().create_report(report)
    with pytest.raises(FileExistsError):
        module().create_report(report)
    with pytest.raises(ValueError, match="outside the source tree"):
        module().create_report(Path(__file__).resolve().parents[2] / "thinking-private.json")
    with pytest.raises(ValueError):
        module().create_report(Path("relative-report.json"))


def test_timeout_stops_without_retry_or_feature_enablement(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    runner = module()
    tmp_path.chmod(0o700)
    calls: list[str] = []

    class Idle:
        def __init__(self, *_args: Any) -> None:
            pass

        async def get_json(self, *_args: Any) -> dict[str, Any]:
            return {"state": "ready", "active_requests": 0, "queued_requests": 0}

    class Timeout:
        def __init__(self, *_args: Any) -> None:
            pass

        async def generate(self, payload: Any) -> None:
            calls.append(payload.locale)
            raise ApplicationError(ErrorCode.TIMEOUT, "inference.provider_timeout")

    monkeypatch.setattr(runner, "secret", lambda _path: SecretStr("s" * 40))
    monkeypatch.setattr(runner, "runtime_resources", lambda: {})
    monkeypatch.setattr(runner, "UrllibJsonTransport", Idle)
    monkeypatch.setattr(runner, "BoundedInferenceService", Timeout)
    output = tmp_path / "result.json"
    args = argparse.Namespace(
        expected_app_code_sha256=runner.APP_CODE_SHA256,
        output=output,
        provider_api_key_file=tmp_path / "key",
        change_id="thinking-unit-test",
        scope="short",
    )
    assert asyncio.run(runner.qualify(args)) == 1
    report = json.loads(output.read_text())
    assert calls == ["en"]
    assert report["status"] == "failed" and report["flags_changed"] is False
    assert report["semantic_review"] == "pending"
    assert report["cases"][0]["error"] == "inference.provider_timeout"
    assert "reasoning_content" not in output.read_text()


@pytest.mark.parametrize("scope", ["short", "capabilities"])
def test_complete_native_diagnostics_still_exit_partial_not_accepted(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, scope: str
) -> None:
    runner = module()
    tmp_path.chmod(0o700)
    cases = runner.short_cases() if scope == "short" else runner.capability_cases(True)
    answers = iter(
        [exact or "Synthetic completion; not semantic acceptance." for _, _, exact in cases]
    )

    class Idle:
        def __init__(self, *_args: Any) -> None:
            pass

        async def get_json(self, *_args: Any) -> dict[str, Any]:
            return {"state": "ready", "active_requests": 0, "queued_requests": 0}

    class Complete:
        def __init__(self, *_args: Any) -> None:
            pass

        async def generate(self, _payload: Any) -> Any:
            answer = next(answers)
            return SimpleNamespace(answer=answer, model_dump=lambda **_kwargs: {"answer": answer})

    monkeypatch.setattr(runner, "secret", lambda _path: SecretStr("s" * 40))
    monkeypatch.setattr(runner, "runtime_resources", lambda: {})
    monkeypatch.setattr(runner, "UrllibJsonTransport", Idle)
    monkeypatch.setattr(runner, "BoundedInferenceService", Complete)
    output = tmp_path / "result.json"
    args = argparse.Namespace(
        expected_app_code_sha256=runner.APP_CODE_SHA256,
        output=output,
        provider_api_key_file=tmp_path / "key",
        change_id="thinking-unit-test",
        scope=scope,
    )
    assert asyncio.run(runner.qualify(args)) == 2
    report = json.loads(output.read_text())
    assert len(report["cases"]) == len(cases) and report["status"] == "partial"
    assert report["semantic_review"] == "pending" and report["flags_changed"] is False
    if scope == "capabilities":
        assert report["corpus_revision"] == report["advisory_policy_revision"] == "capability-v1"
        assert len(report["corpus_sha256"]) == 64
        assert report["semantic_criteria"] == runner.CAPABILITY_REVIEW_CRITERIA
