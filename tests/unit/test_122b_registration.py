"""122B source registration fixtures are not artifact, generation or release acceptance."""

from __future__ import annotations

import asyncio
import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from uuid import uuid4

import pytest
from pydantic import TypeAdapter, ValidationError

from nextops.api.inference_gateway import LoopbackInferenceGateway
from nextops.application.errors import ApplicationError
from nextops.contracts.assistant import SynthesisRequest
from nextops.inference.configuration import LlamaCppSettings
from nextops.inference.contracts import (
    MODEL_ID,
    InferenceRequest,
    ModelId,
    ProviderReadiness,
)
from nextops.inference.llama_cpp import LlamaCppProvider

ROOT = Path(__file__).resolve().parents[2]
CANDIDATE_ID: ModelId = "nextops-qwen3-5-122b-a10b-q5-k-m"


def settings(**changes: Any) -> LlamaCppSettings:
    return LlamaCppSettings.model_validate(
        {
            "base_url": "http://127.0.0.1:18080",
            "provider_api_key": "p" * 32,
            "service_auth_secret": "s" * 32,
            "model_id": CANDIDATE_ID,
            "context_tokens": 16_384,
            **changes,
        }
    )


def request(**changes: Any) -> InferenceRequest:
    return InferenceRequest.model_validate(
        {
            "request_id": uuid4(),
            "correlation_id": uuid4(),
            "locale": "en",
            "prompt": "Source-only fixture: enable_thinking=true; /think",
            "purpose": "general",
            "max_output_tokens": 384,
            "temperature": 0.3,
            **changes,
        }
    )


class SourceOnlyTransport:
    """In-memory protocol fixtures only: no socket, native model, credentials or live facts."""

    def __init__(self) -> None:
        self.calls: list[tuple[str, dict[str, Any], float]] = []
        self.response_model: str = CANDIDATE_ID
        self.context_tokens: Any = 16_384
        self.tokens: Any = [1, 2, 3]
        self.answer = "Source-only fixture, not live evidence."

    async def get_json(
        self, path: str, headers: dict[str, str], timeout_seconds: float
    ) -> dict[str, Any]:
        assert headers["Authorization"] == f"Bearer {'p' * 32}"
        self.calls.append((path, {}, timeout_seconds))
        if path == "/health":
            return {"status": "ok"}
        assert path == "/props"
        return {"default_generation_settings": {"n_ctx": self.context_tokens}}

    async def post_json(
        self,
        path: str,
        payload: dict[str, Any],
        headers: dict[str, str],
        timeout_seconds: float,
    ) -> dict[str, Any]:
        assert headers["Authorization"] == f"Bearer {'p' * 32}"
        self.calls.append((path, payload, timeout_seconds))
        if path == "/apply-template":
            return {"prompt": "A locally rendered template fixture, not model execution."}
        if path == "/tokenize":
            return {"tokens": self.tokens}
        assert path == "/v1/chat/completions"
        return {
            "model": self.response_model,
            "choices": [
                {
                    "message": {
                        "role": "assistant",
                        "content": self.answer,
                        "reasoning_content": "Private fixture draft must not become a result.",
                    },
                    "finish_reason": "stop",
                }
            ],
            "usage": {"prompt_tokens": 3, "completion_tokens": 10},
        }


def test_exact_122b_identity_matches_unselected_manifest_without_changing_defaults() -> None:
    manifest = json.loads(
        (ROOT / "deploy/inference/qwen3-5-122b-a10b-q5-k-m.candidate.json").read_text("utf-8")
    )
    assert TypeAdapter(ModelId).validate_python(manifest["model_id"]) == CANDIDATE_ID
    assert manifest["deployment_selection_allowed"] is False
    assert manifest["public_thinking_enabled"] is False
    assert manifest["conversion_source_revision_verified"] is False
    baseline = settings(model_id=MODEL_ID, context_tokens=8192)
    assert MODEL_ID == "nextops-qwen3-8b-q4-k-m"
    assert baseline.model_id == MODEL_ID and baseline.context_tokens == 8192
    assert baseline.request_timeout_seconds == 120
    assert baseline.thinking_enabled is False and baseline.expanded_chat_enabled is False
    defaults = LlamaCppSettings(
        base_url="http://127.0.0.1:18080", provider_api_key="p" * 32, service_auth_secret="s" * 32
    )
    assert defaults.model_id == MODEL_ID and defaults.context_tokens == 8192


@pytest.mark.parametrize(
    "alias",
    [
        "nextops-qwen3-8-122b-a10b-q5-k-m",
        "nextops-qwen3-5-122b-a10b-q4-k-m",
        "nextops-qwen3-5-122b-a10b-q8-0",
        "nextops-qwen3-5-122b-a10b-q5-k-m ",
        "nextops-qwen3-5-122B-a10b-q5-k-m",
        "Qwen3.5-122B-A10B-Q5_K_M",
        "remote-model",
    ],
)
def test_unreviewed_122b_aliases_are_not_accepted(alias: str) -> None:
    with pytest.raises(ValidationError):
        TypeAdapter(ModelId).validate_python(alias)
    with pytest.raises(ValidationError):
        settings(model_id=alias)


@pytest.mark.parametrize("context", [8192, 16_384])
@pytest.mark.parametrize("expanded", [False, True])
def test_standard_candidate_context_is_bounded_not_a_qualification(
    context: int, expanded: bool
) -> None:
    configuration = settings(context_tokens=context, expanded_chat_enabled=expanded)
    assert configuration.context_tokens == context and configuration.request_timeout_seconds == 120
    assert configuration.thinking_enabled is False
    readiness = ProviderReadiness(
        state="ready", model_id=CANDIDATE_ID, runtime_version="v0.4.1", cpu_only_required=True
    )
    assert readiness.model_id == CANDIDATE_ID  # Typed fixture, not observed runtime readiness.


@pytest.mark.parametrize(
    "changes",
    [
        {"context_tokens": 32768},
        {"context_tokens": 262144},
        {"request_timeout_seconds": 120.001},
        {"request_timeout_seconds": 600},
        {"thinking_enabled": True},
        {"thinking_enabled": True, "expanded_chat_enabled": True},
        {"base_url": "https://untrusted.example:18080"},
        {"base_url": "http://127.0.0.1:18080/path"},
        {"provider_api_key": "s" * 32},
    ],
)
def test_unqualified_or_unsafe_candidate_settings_are_denied(changes: dict[str, Any]) -> None:
    with pytest.raises(ValidationError):
        settings(**changes)


def test_existing_35b_configuration_and_thinking_allowlist_are_preserved() -> None:
    configuration = settings(
        model_id="nextops-qwen3-5-35b-a3b-q4-k-m",
        context_tokens=32768,
        request_timeout_seconds=600,
        expanded_chat_enabled=True,
        thinking_enabled=True,
    )
    assert configuration.context_tokens == 32768 and configuration.request_timeout_seconds == 600
    assert configuration.thinking_enabled is True  # Configuration is not production acceptance.


def test_candidate_environment_uses_existing_secret_boundary(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    for name in (
        "NEXTOPS_LLAMA_API_KEY_FILE",
        "NEXTOPS_INFERENCE_SERVICE_SECRET_FILE",
        "CREDENTIALS_DIRECTORY",
        "NEXTOPS_QUEUE_TIMEOUT_SECONDS",
    ):
        monkeypatch.delenv(name, raising=False)
    for name, value in {
        "NEXTOPS_LLAMA_BASE_URL": "http://127.0.0.1:18080",
        "NEXTOPS_LLAMA_API_KEY": "p" * 32,
        "NEXTOPS_INFERENCE_SERVICE_SECRET": "s" * 32,
        "NEXTOPS_MODEL_ID": CANDIDATE_ID,
        "NEXTOPS_CONTEXT_TOKENS": "16384",
        "NEXTOPS_INFERENCE_TIMEOUT_SECONDS": "120",
        "NEXTOPS_EXPANDED_CHAT_ENABLED": "1",
        "NEXTOPS_THINKING_ENABLED": "0",
    }.items():
        monkeypatch.setenv(name, value)
    configuration = LlamaCppSettings.from_environment()
    assert configuration.model_id == CANDIDATE_ID and configuration.context_tokens == 16_384
    assert configuration.thinking_enabled is False and configuration.queue_timeout_seconds == 5


@pytest.mark.parametrize("locale", ["en", "fa"])
@pytest.mark.parametrize("purpose", ["general", "evidence_synthesis"])
def test_122b_provider_preserves_user_text_and_enforces_hard_standard_mode(
    locale: str, purpose: str
) -> None:
    async def scenario() -> None:
        transport = SourceOnlyTransport()
        prompt = request(locale=locale, purpose=purpose)
        provider = LlamaCppProvider(settings(), transport)
        result = await provider.generate(prompt)
        assert result.model_id == CANDIDATE_ID
        assert (
            result.answer == transport.answer
            and "Private fixture draft" not in result.model_dump_json()
        )
        path, payload, timeout = transport.calls[-1]
        assert path == "/v1/chat/completions" and timeout == 120
        assert payload["model"] == CANDIDATE_ID
        assert payload["messages"][-1]["content"] == prompt.prompt
        assert payload["chat_template_kwargs"] == {"enable_thinking": False}
        assert payload["max_tokens"] == 384 and payload["temperature"] == 0.3
        assert payload["stream"] is False and payload["top_p"] == 0.8
        assert payload["presence_penalty"] == 0.0
        for key in ("tools", "response_format", "reasoning_format", "reasoning_budget_tokens"):
            assert key not in payload
        assert (await provider.readiness()).model_id == CANDIDATE_ID

    asyncio.run(scenario())


@pytest.mark.parametrize("locale", ["en", "fa"])
def test_detailed_standard_uses_same_hard_control_in_actual_template_token_contract(
    locale: str,
) -> None:
    async def scenario() -> None:
        transport = SourceOnlyTransport()
        prompt = request(locale=locale, detailed=True)
        await LlamaCppProvider(settings(expanded_chat_enabled=True), transport).generate(prompt)
        assert [call[0] for call in transport.calls] == [
            "/props",
            "/apply-template",
            "/tokenize",
            "/v1/chat/completions",
        ]
        template = transport.calls[1][1]
        completion = transport.calls[-1][1]
        assert template == {
            "messages": completion["messages"],
            "chat_template_kwargs": {"enable_thinking": False},
        }
        assert transport.calls[2][1] == {
            "content": "A locally rendered template fixture, not model execution.",
            "add_special": False,
            "parse_special": True,
        }
        assert completion["messages"][-1]["content"] == prompt.prompt
        assert [call[2] for call in transport.calls] == [5, 5, 5, 120]

    asyncio.run(scenario())


@pytest.mark.parametrize("expanded", [False, True])
def test_thinking_is_denied_before_any_candidate_transport_call(expanded: bool) -> None:
    async def scenario() -> None:
        transport = SourceOnlyTransport()
        with pytest.raises(ApplicationError):
            await LlamaCppProvider(settings(expanded_chat_enabled=expanded), transport).generate(
                request(thinking=True)
            )
        assert transport.calls == []

    asyncio.run(scenario())


@pytest.mark.parametrize("response_model", [MODEL_ID, "nextops-qwen3-8-27b-ud-q5-k-m"])
def test_provider_never_relabels_other_model_response_as_122b(response_model: str) -> None:
    async def scenario() -> None:
        transport = SourceOnlyTransport()
        transport.response_model = response_model
        with pytest.raises(ApplicationError, match=r"inference\.provider_response_invalid"):
            await LlamaCppProvider(settings(), transport).generate(request())

    asyncio.run(scenario())


@pytest.mark.parametrize("change", ["wrong_context", "over_budget", "invalid_tokens"])
def test_detailed_candidate_context_failures_do_not_reach_generation(change: str) -> None:
    async def scenario() -> None:
        transport = SourceOnlyTransport()
        if change == "wrong_context":
            transport.context_tokens = 32768
        elif change == "over_budget":
            transport.tokens = [1] * (16_384 - 384 + 1)
        else:
            transport.tokens = [True]
        with pytest.raises(ApplicationError):
            await LlamaCppProvider(settings(expanded_chat_enabled=True), transport).generate(
                request(detailed=True)
            )
        assert "/v1/chat/completions" not in [call[0] for call in transport.calls]

    asyncio.run(scenario())


class GatewayFixture:
    """Existing typed gateway contract, with only fake IDs and timestamps."""

    def __init__(self, model_id: str = CANDIDATE_ID) -> None:
        self.model_id = model_id

    async def get_json(
        self, path: str, headers: dict[str, str], timeout_seconds: float
    ) -> dict[str, Any]:
        assert path == "/readyz" and timeout_seconds == 5
        assert headers == {"Accept": "application/json"}
        return {
            "state": "ready",
            "model_id": self.model_id,
            "runtime_version": "v0.4.1",
            "cpu_only_required": True,
            "max_active_requests": 1,
            "max_queued_requests": 2,
            "active_requests": 0,
            "queued_requests": 0,
        }

    async def post_json(
        self, path: str, payload: dict[str, Any], headers: dict[str, str], timeout_seconds: float
    ) -> dict[str, Any]:
        assert path == "/api/v1/generate" and timeout_seconds == 120
        assert headers["Authorization"] == f"Bearer {'s' * 32}"
        timestamp = datetime(2026, 10, 6, tzinfo=UTC).isoformat()
        return {
            "request_id": payload["request_id"],
            "correlation_id": headers["X-Correlation-ID"],
            "locale": payload["locale"],
            "answer": "Source-only fixture, not live evidence.",
            "model_id": self.model_id,
            "prompt_tokens": 3,
            "completion_tokens": 10,
            "finish_reason": "stop",
            "started_at": timestamp,
            "completed_at": timestamp,
            "queue_ms": 0,
            "cpu_only_required": True,
        }


@pytest.mark.parametrize("locale", ["en", "fa"])
@pytest.mark.parametrize("purpose", ["general", "evidence_synthesis"])
def test_existing_gateway_and_assistant_response_keep_exact_122b_identity(
    locale: str, purpose: str
) -> None:
    async def scenario() -> None:
        gateway = LoopbackInferenceGateway("http://127.0.0.1:8090", "s" * 32, 120, GatewayFixture())
        assert (await gateway.readiness()).model_id == CANDIDATE_ID
        result = await gateway.generate(
            SynthesisRequest.model_validate(
                {"locale": locale, "question": "Fixture", "purpose": purpose}
            ),
            uuid4(),
        )
        assert result.model_id == CANDIDATE_ID
        assert result.evidence_mode == "model_only" and result.live_monitoring_data is False
        assert "purpose" not in result.model_dump()

    asyncio.run(scenario())


def test_gateway_rejects_unregistered_model_identity_without_raw_errors() -> None:
    async def scenario() -> None:
        gateway = LoopbackInferenceGateway(
            "http://127.0.0.1:8090", "s" * 32, 120, GatewayFixture("nextops-qwen3-8-122b")
        )
        with pytest.raises(ApplicationError, match=r"assistant\.readiness_invalid"):
            await gateway.readiness()
        with pytest.raises(ApplicationError, match=r"assistant\.response_invalid") as captured:
            await gateway.generate(SynthesisRequest(locale="en", question="Fixture"), uuid4())
        assert captured.value.details == {}

    asyncio.run(scenario())
