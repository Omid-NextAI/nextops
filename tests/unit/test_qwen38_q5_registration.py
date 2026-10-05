"""Source-only candidate registration is not generation or release acceptance."""

from __future__ import annotations

import asyncio
import copy
import importlib.util
import json
from datetime import UTC, datetime
from pathlib import Path
from types import ModuleType
from typing import Any
from uuid import uuid4

import pytest
import yaml
from pydantic import TypeAdapter, ValidationError

from nextops.api.inference_gateway import LoopbackInferenceGateway
from nextops.contracts.assistant import SynthesisRequest
from nextops.inference.configuration import LlamaCppSettings
from nextops.inference.contracts import MODEL_ID, GenerationPurpose, ModelId, ProviderReadiness

ROOT = Path(__file__).resolve().parents[2]
CANDIDATE_ID: ModelId = "nextops-qwen3-8-27b-ud-q5-k-m"
PROFILE = "qwen3-8-27b-ud-q5-k-m"


def _candidate() -> dict[str, Any]:
    result = json.loads(
        (ROOT / "deploy/inference" / f"{PROFILE}.candidate.json").read_text("utf-8")
    )
    assert isinstance(result, dict)
    return result


def _release_validator() -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        "qwen38_q5_release_review", ROOT / "scripts/check_release_status.py"
    )
    assert spec is not None and spec.loader is not None
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def _settings(**changes: Any) -> LlamaCppSettings:
    return LlamaCppSettings.model_validate(
        {
            "base_url": "http://127.0.0.1:8080",
            "provider_api_key": "p" * 32,
            "service_auth_secret": "s" * 32,
            "model_id": CANDIDATE_ID,
            **changes,
        }
    )


def test_candidate_identity_is_distinct_and_defaults_remain_unchanged() -> None:
    candidate = _candidate()
    assert TypeAdapter(ModelId).validate_python(candidate["model_id"]) == CANDIDATE_ID
    assert CANDIDATE_ID not in {
        MODEL_ID,
        "nextops-qwen3-8-27b-q8-0",
        "nextops-qwen3-5-35b-a3b-q4-k-m",
    }
    defaults = LlamaCppSettings(
        base_url="http://127.0.0.1:8080",
        provider_api_key="p" * 32,
        service_auth_secret="s" * 32,
    )
    assert defaults.model_id == MODEL_ID == "nextops-qwen3-8b-q4-k-m"
    assert defaults.context_tokens == 8192
    assert defaults.request_timeout_seconds == 120
    assert defaults.thinking_enabled is False and defaults.expanded_chat_enabled is False
    assert candidate["deployment_selection_allowed"] is False
    assert candidate["conversion_source_revision_verified"] is False
    assert candidate["public_thinking_enabled"] is False
    selected = yaml.safe_load((ROOT / "docs/status/current-release.yaml").read_text("utf-8"))
    assert selected["components"]["model"]["identifier"] == "nextops-qwen3-5-35b-a3b-q4-k-m"


@pytest.mark.parametrize(
    "unreviewed",
    [
        "nextops-qwen3-8-27b-q5-k-m",
        "nextops-qwen3-8-27b-UD-Q5_K_M",
        "nextops-qwen3-8-27b-ud-q5-k-m ",
        "Qwen3.8-27B-UD-Q5_K_M",
        "nextops-qwen3-8-27b-ud-q4-k-m",
    ],
)
def test_candidate_registration_does_not_accept_aliases(unreviewed: str) -> None:
    with pytest.raises(ValidationError):
        TypeAdapter(ModelId).validate_python(unreviewed)
    with pytest.raises(ValidationError):
        _settings(model_id=unreviewed)


@pytest.mark.parametrize("context", [8192, 16384])
def test_candidate_settings_allow_only_bounded_standard_context(context: int) -> None:
    settings = _settings(context_tokens=context, expanded_chat_enabled=True)
    assert settings.context_tokens == context
    assert settings.request_timeout_seconds == 120
    assert settings.thinking_enabled is False
    readiness = ProviderReadiness(
        state="ready", model_id=CANDIDATE_ID, runtime_version="v0.4.1", cpu_only_required=True
    )
    assert readiness.model_id == CANDIDATE_ID  # A typed fixture is not runtime readiness.


@pytest.mark.parametrize(
    "changes",
    [
        {"context_tokens": 32768},
        {"context_tokens": 262144},
        {"request_timeout_seconds": 120.001},
        {"request_timeout_seconds": 600},
        {"thinking_enabled": True},
        {"thinking_enabled": True, "expanded_chat_enabled": True},
        {"base_url": "http://untrusted.example:8080"},
        {"provider_api_key": "s" * 32},
    ],
)
def test_candidate_settings_reject_wider_or_unsafe_profiles(changes: dict[str, Any]) -> None:
    with pytest.raises(ValidationError):
        _settings(**changes)


def test_other_existing_profile_contracts_are_not_silently_narrowed() -> None:
    settings = _settings(
        model_id="nextops-qwen3-5-35b-a3b-q4-k-m",
        context_tokens=32768,
        request_timeout_seconds=600,
        expanded_chat_enabled=True,
    )
    assert settings.context_tokens == 32768 and settings.request_timeout_seconds == 600
    # Existing configuration validation is not acceptance of these optional profile values.


def test_candidate_source_profile_keeps_base_hardening_and_explicit_template_controls() -> None:
    directory = ROOT / "deploy/systemd"
    base = (directory / "nextops-llama.service").read_text("utf-8")
    runtime = (directory / "model-profiles" / f"{PROFILE}-runtime.conf").read_text("utf-8")
    base_command = base.split("ExecStart=", 1)[1].split("\nRestart=", 1)[0].strip()
    expected = (
        base_command.replace("Qwen3-8B-Q4_K_M.gguf", _candidate()["filename"])
        .replace(MODEL_ID, CANDIDATE_ID)
        .replace("--ctx-size 8192", "--ctx-size 16384")
    )
    expected += " \\\n    --no-reasoning-preserve \\\n"
    expected += '    --chat-template-kwargs \'{"enable_thinking":false,"preserve_thinking":false}\''
    assert runtime.split("ExecStart=\nExecStart=", 1)[1].strip() == expected
    assert f"ConditionPathExists=/srv/nextops/models/current/{_candidate()['filename']}" in runtime
    directives = [line for line in runtime.splitlines() if "=" in line and not line.startswith("#")]
    assert len(directives) == 4
    for forbidden in (
        "CPUQuota=",
        "MemoryHigh=",
        "MemoryMax=",
        "IPAddressDeny=",
        "LoadCredential=",
        "--hf-repo",
        "--model-url",
        "--mmproj",
        "--spec-type",
    ):
        assert forbidden not in runtime
    api = (directory / "model-profiles" / f"{PROFILE}-api.conf").read_text("utf-8")
    assert "EnvironmentFile=/etc/nextops/model-selection.env" in api
    assert "EnvironmentFile=-" not in api and "Environment=" not in api
    assert "Unselected" in runtime and "Unselected" in api


def test_candidate_source_environment_loads_without_changing_defaults(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    environment = (ROOT / "deploy/systemd/model-profiles" / f"{PROFILE}.env").read_text("utf-8")
    values = dict(
        line.split("=", 1) for line in environment.splitlines() if line and line[0] != "#"
    )
    assert values == {
        "NEXTOPS_MODEL_ID": CANDIDATE_ID,
        "NEXTOPS_CONTEXT_TOKENS": "16384",
        "NEXTOPS_INFERENCE_TIMEOUT_SECONDS": "120",
        "NEXTOPS_EXPANDED_CHAT_ENABLED": "1",
        "NEXTOPS_THINKING_ENABLED": "0",
    }
    for name in (
        "NEXTOPS_LLAMA_API_KEY_FILE",
        "NEXTOPS_INFERENCE_SERVICE_SECRET_FILE",
        "CREDENTIALS_DIRECTORY",
        "NEXTOPS_QUEUE_TIMEOUT_SECONDS",
    ):
        monkeypatch.delenv(name, raising=False)
    for name, value in values.items():
        monkeypatch.setenv(name, value)
    monkeypatch.setenv("NEXTOPS_LLAMA_BASE_URL", "http://127.0.0.1:8080")
    monkeypatch.setenv("NEXTOPS_LLAMA_API_KEY", "p" * 32)
    monkeypatch.setenv("NEXTOPS_INFERENCE_SERVICE_SECRET", "s" * 32)
    settings = LlamaCppSettings.from_environment()
    assert settings.model_id == CANDIDATE_ID and settings.context_tokens == 16384
    assert settings.thinking_enabled is False and settings.queue_timeout_seconds == 5


class CandidateTransport:
    """Only in-memory contract fixtures; no socket, generation or infrastructure evidence."""

    async def get_json(
        self, path: str, headers: dict[str, str], timeout_seconds: float
    ) -> dict[str, Any]:
        raise AssertionError("This serialization test does not probe runtime readiness")

    async def post_json(
        self,
        path: str,
        payload: dict[str, Any],
        headers: dict[str, str],
        timeout_seconds: float,
    ) -> dict[str, Any]:
        assert path == "/api/v1/generate" and timeout_seconds == 120
        timestamp = datetime(2026, 10, 5, tzinfo=UTC).isoformat()
        return {
            "request_id": payload["request_id"],
            "correlation_id": headers["X-Correlation-ID"],
            "locale": payload["locale"],
            "answer": "A source-only contract fixture, not live evidence.",
            "model_id": CANDIDATE_ID,
            "prompt_tokens": 12,
            "completion_tokens": 10,
            "finish_reason": "stop",
            "started_at": timestamp,
            "completed_at": timestamp,
            "queue_ms": 0,
            "cpu_only_required": True,
        }


@pytest.mark.parametrize("purpose", ["general", "evidence_synthesis"])
@pytest.mark.parametrize("locale", ["en", "fa"])
def test_existing_gateway_keeps_exact_q5_identity_without_inventing_evidence(
    purpose: GenerationPurpose, locale: str
) -> None:
    async def scenario() -> None:
        gateway = LoopbackInferenceGateway(
            "http://127.0.0.1:8090", "s" * 32, 120, CandidateTransport()
        )
        request = SynthesisRequest.model_validate(
            {"locale": locale, "question": "Source-only contract check", "purpose": purpose}
        )
        result = await gateway.generate(request, uuid4())
        assert result.model_id == CANDIDATE_ID
        assert result.evidence_mode == "model_only" and result.live_monitoring_data is False
        assert "purpose" not in result.model_dump()

    asyncio.run(scenario())


def _release_model(candidate: dict[str, Any]) -> dict[str, Any]:
    return {
        "identifier": candidate["model_id"],
        **{
            field: candidate[field]
            for field in ("source_revision", "quantization", "size_bytes", "sha256")
        },
    }


def test_release_verification_recognizes_distinct_candidate_but_cannot_promote_it() -> None:
    module = _release_validator()
    candidate = _candidate()
    baseline = yaml.safe_load((ROOT / "deploy/inference/qwen3-8b-q4-k-m.yaml").read_text("utf-8"))[
        "model"
    ]
    assert module.QWEN38_Q5_MODEL_ID == CANDIDATE_ID
    assert module.QWEN38_Q5_MODEL_MANIFEST.name == f"{PROFILE}.candidate.json"
    errors = module.model_identity_errors(_release_model(candidate), baseline, candidate)
    assert errors == ["Qwen3.8 Q5 candidate is unselected and has no release-selection acceptance"]
    for field, incorrect in (
        ("source_revision", "0" * 40),
        ("quantization", "Q5_K_M"),
        ("quantization", "Q8_0"),
        ("size_bytes", 29_047_086_048),
        ("size_bytes", True),
        ("sha256", "0" * 64),
    ):
        errors = module.model_identity_errors(
            {**_release_model(candidate), field: incorrect}, baseline, candidate
        )
        assert any(f"selected model {field} differs" in error for error in errors)
    forged = copy.deepcopy(candidate)
    forged.update(
        status="controlled_selected_not_production_accepted",
        deployment_selection_allowed=True,
        conversion_source_revision_verified=True,
    )
    forged["qualification"] = dict.fromkeys(forged["qualification"], "passed")
    assert module.model_identity_errors(_release_model(forged), baseline, forged)
    assert module.model_identity_errors(_release_model(forged), forged, forged)
    swapped = {**candidate, "model_id": "nextops-qwen3-8-27b-q8-0"}
    assert any(
        "distinct candidate manifest" in error
        for error in module.model_identity_errors(_release_model(candidate), baseline, swapped)
    )


def test_release_main_rejects_candidate_selection_without_modifying_any_manifest(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    module = _release_validator()
    status = yaml.safe_load((ROOT / "docs/status/current-release.yaml").read_text("utf-8"))
    status["components"]["model"] = _release_model(_candidate())
    path = tmp_path / "source-only-unselected.yaml"
    path.write_text(yaml.safe_dump(status), encoding="utf-8")
    monkeypatch.setattr(module, "MANIFEST", path)
    monkeypatch.setattr(module, "recovery_profile_qualified", lambda: False)
    assert module.main() == 1
    assert "unselected and has no release-selection acceptance" in capsys.readouterr().out
