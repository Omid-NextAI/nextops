"""Long responses are explicit candidate-only budgets, never wider operational permission."""

from pathlib import Path
from typing import Any

import pytest

from nextops.configuration import AppSettings
from nextops.inference.configuration import LlamaCppSettings
from nextops.inference.contracts import ModelId

ROOT = Path(__file__).resolve().parents[2]
CANDIDATES: tuple[ModelId, ...] = (
    "nextops-qwen3-8-27b-q8-0",
    "nextops-qwen3-8-27b-ud-q5-k-m",
)


def settings(model_id: ModelId, **changes: Any) -> LlamaCppSettings:
    return LlamaCppSettings.model_validate(
        {
            "base_url": "http://127.0.0.1:18080",
            "provider_api_key": "synthetic-provider-secret-00000000",
            "service_auth_secret": "synthetic-service-secret-000000000",
            "model_id": model_id,
            "context_tokens": 16384,
            "expanded_chat_enabled": True,
            **changes,
        }
    )


@pytest.mark.parametrize("model_id", CANDIDATES)
def test_qwen38_long_response_requires_explicit_opt_in(model_id: ModelId) -> None:
    assert settings(model_id).request_timeout_seconds == 120
    with pytest.raises(ValueError, match="120 seconds"):
        settings(model_id, request_timeout_seconds=300)
    extended = settings(model_id, request_timeout_seconds=300, qwen38_extended_timeout_enabled=True)
    assert extended.queue_timeout_seconds == 5
    assert extended.context_tokens == 16384
    assert extended.thinking_enabled is False


@pytest.mark.parametrize("model_id", CANDIDATES)
@pytest.mark.parametrize("deadline", [300.001, 600])
def test_extended_deadline_is_still_finite(model_id: ModelId, deadline: float) -> None:
    with pytest.raises(ValueError, match="300 seconds"):
        settings(model_id, request_timeout_seconds=deadline, qwen38_extended_timeout_enabled=True)


@pytest.mark.parametrize("model_id", CANDIDATES)
@pytest.mark.parametrize("changes", [{"context_tokens": 32768}, {"thinking_enabled": True}])
def test_long_response_does_not_enable_context_or_private_thinking(
    model_id: ModelId, changes: dict[str, Any]
) -> None:
    with pytest.raises(ValueError):
        settings(
            model_id,
            request_timeout_seconds=300,
            qwen38_extended_timeout_enabled=True,
            **changes,
        )


def test_extended_flag_rejects_unrelated_models_and_unexpanded_profile() -> None:
    for model_id in ("nextops-qwen3-5-35b-a3b-q4-k-m", "nextops-qwen3-5-122b-a10b-q5-k-m"):
        with pytest.raises(ValueError, match=r"expanded Qwen3\.8 candidate"):
            settings(model_id, qwen38_extended_timeout_enabled=True)
    with pytest.raises(ValueError, match=r"expanded Qwen3\.8 candidate"):
        settings(CANDIDATES[0], qwen38_extended_timeout_enabled=True, expanded_chat_enabled=False)
    assert settings("nextops-qwen3-5-35b-a3b-q4-k-m").request_timeout_seconds == 120
    with pytest.raises(ValueError, match="122B candidate"):
        settings("nextops-qwen3-5-122b-a10b-q5-k-m", request_timeout_seconds=300)


def test_long_response_environment_is_explicit(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in (
        "CREDENTIALS_DIRECTORY",
        "NEXTOPS_LLAMA_API_KEY_FILE",
        "NEXTOPS_INFERENCE_SERVICE_SECRET_FILE",
        "NEXTOPS_QWEN38_EXTENDED_TIMEOUT_ENABLED",
        "NEXTOPS_THINKING_ENABLED",
    ):
        monkeypatch.delenv(name, raising=False)
    for name, value in {
        "NEXTOPS_LLAMA_BASE_URL": "http://127.0.0.1:18080",
        "NEXTOPS_LLAMA_API_KEY": "synthetic-provider-secret-00000000",
        "NEXTOPS_INFERENCE_SERVICE_SECRET": "synthetic-service-secret-000000000",
        "NEXTOPS_MODEL_ID": CANDIDATES[1],
        "NEXTOPS_CONTEXT_TOKENS": "16384",
        "NEXTOPS_EXPANDED_CHAT_ENABLED": "1",
        "NEXTOPS_INFERENCE_TIMEOUT_SECONDS": "300",
    }.items():
        monkeypatch.setenv(name, value)
    with pytest.raises(ValueError, match="120 seconds"):
        LlamaCppSettings.from_environment()
    monkeypatch.setenv("NEXTOPS_QWEN38_EXTENDED_TIMEOUT_ENABLED", "1")
    assert LlamaCppSettings.from_environment().request_timeout_seconds == 300
    monkeypatch.setenv("NEXTOPS_QWEN38_EXTENDED_TIMEOUT_ENABLED", "true")
    with pytest.raises(ValueError, match="120 seconds"):
        LlamaCppSettings.from_environment()


def test_profiles_leave_defaults_and_ordinary_proxy_routes_unchanged() -> None:
    provider = (ROOT / "deploy/systemd/model-profiles/qwen38-long-response.env").read_text()
    app = (ROOT / "deploy/systemd/model-profiles/qwen38-long-response-app.env").read_text()
    proxy = (ROOT / "deploy/nginx/profiles/qwen38-long-response.conf").read_text()
    baseline = (ROOT / "deploy/nginx/nextops-app.conf").read_text()
    assert "NEXTOPS_QWEN38_EXTENDED_TIMEOUT_ENABLED=1" in provider
    assert "NEXTOPS_INFERENCE_TIMEOUT_SECONDS=300" in provider
    assert "NEXTOPS_THINKING_ENABLED=0" in provider
    assert "NEXTOPS_QUEUE_TIMEOUT_SECONDS=5" in provider
    assert "NEXTOPS_INFERENCE_TIMEOUT_SECONDS=330" in app
    assert "proxy_read_timeout 360s;" in proxy
    assert "proxy_send_timeout 360s;" in proxy
    assert "proxy_pass" not in proxy and "limit_req" not in proxy
    assert "proxy_read_timeout 180s;" in baseline
    assert "proxy_read_timeout 30s;" in baseline
    assert "limit_req zone=nextops_assistant burst=3 nodelay;" in baseline
    assert AppSettings.model_fields["inference_timeout_seconds"].default == 150
