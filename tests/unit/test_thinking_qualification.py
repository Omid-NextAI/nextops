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


def test_context_cannot_evade_application_character_quotas() -> None:
    for locale in ("en", "fa"):
        payload = module().context_request(locale, 5700)
        assert len(payload.prompt) <= 32000
        assert "EARLY-" in payload.prompt
    with pytest.raises(ValueError, match="saved context exceeds"):
        module().context_request("en", 6100)
    with pytest.raises(ValueError):
        module().request("en", "x" * 4001)


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


def test_complete_native_diagnostics_still_exit_partial_not_accepted(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    runner = module()
    tmp_path.chmod(0o700)
    answers = iter(["final", "final", "0", "TICKET-732"] * 2)

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
        scope="short",
    )
    assert asyncio.run(runner.qualify(args)) == 2
    report = json.loads(output.read_text())
    assert len(report["cases"]) == 8 and report["status"] == "partial"
    assert report["semantic_review"] == "pending" and report["flags_changed"] is False
