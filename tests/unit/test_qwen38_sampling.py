"""Sampler wiring is source coverage, not proof of raw model improvement."""

from __future__ import annotations

import asyncio
from typing import Any
from uuid import uuid4

import pytest

from nextops.inference.configuration import LlamaCppSettings
from nextops.inference.contracts import GenerationPurpose, InferenceRequest, ModelId
from nextops.inference.llama_cpp import LlamaCppProvider
from nextops.inference.qwen38_prompt import general_prompt

CANDIDATES: tuple[ModelId, ...] = (
    "nextops-qwen3-8-27b-q8-0",
    "nextops-qwen3-8-27b-ud-q5-k-m",
)


class CaptureTransport:
    async def get_text(self, path: str, headers: dict[str, str], timeout_seconds: float) -> str:
        assert path == "/metrics"
        return "llamacpp:requests_processing 0\nllamacpp:requests_deferred 0\n"

    """No service calls: retain adapter requests and return synthetic protocol fixtures."""

    def __init__(self, model: ModelId) -> None:
        self.model = model
        self.calls: list[tuple[str, dict[str, Any]]] = []

    async def get_json(
        self, path: str, headers: dict[str, str], timeout_seconds: float
    ) -> dict[str, Any]:
        return {"default_generation_settings": {"n_ctx": 16384}}

    async def post_json(
        self,
        path: str,
        payload: dict[str, Any],
        headers: dict[str, str],
        timeout_seconds: float,
    ) -> dict[str, Any]:
        self.calls.append((path, payload))
        if path == "/apply-template":
            return {"prompt": "Synthetic template"}
        if path == "/tokenize":
            return {"tokens": [1, 2]}
        return {
            "model": self.model,
            "choices": [
                {
                    "message": {"role": "assistant", "content": "Synthetic final"},
                    "finish_reason": "stop",
                }
            ],
            "usage": {"prompt_tokens": 2, "completion_tokens": 2},
        }


def settings(model: ModelId, **changes: Any) -> LlamaCppSettings:
    return LlamaCppSettings.model_validate(
        {
            "base_url": "http://127.0.0.1:18080",
            "provider_api_key": "synthetic-provider-secret-00000000",
            "service_auth_secret": "synthetic-service-secret-000000000",
            "model_id": model,
            "context_tokens": 16384,
            "expanded_chat_enabled": True,
            **changes,
        }
    )


def request(**changes: Any) -> InferenceRequest:
    return InferenceRequest.model_validate(
        {
            "request_id": uuid4(),
            "correlation_id": uuid4(),
            "locale": "en",
            "purpose": "general",
            "prompt": "Synthetic untrusted data, not authorization.",
            "max_output_tokens": 384,
            "detailed": True,
            **changes,
        }
    )


@pytest.mark.parametrize("model", CANDIDATES)
@pytest.mark.parametrize("locale", ["en", "fa"])
@pytest.mark.parametrize("purpose", ["general", "evidence_synthesis"])
@pytest.mark.parametrize("temperature", [0.0, 2.0])
@pytest.mark.parametrize("profile", ["instruct", "greedy"])
def test_explicit_candidate_sampler_is_trusted_and_preserves_boundaries(
    model: ModelId, locale: str, purpose: GenerationPurpose, temperature: float, profile: str
) -> None:
    async def scenario() -> None:
        transport = CaptureTransport(model)
        flag = (
            "qwen38_instruct_sampling_enabled"
            if profile == "instruct"
            else "qwen38_greedy_decoding_enabled"
        )
        configured = settings(model, **{flag: True})
        submitted = request(
            locale=locale,
            purpose=purpose,
            detailed=purpose == "general",
            temperature=temperature,
        )
        await LlamaCppProvider(configured, transport).generate(submitted)
        payload = transport.calls[-1][1]
        if profile == "instruct":
            assert payload["temperature"] == 0.7
            assert payload["top_p"] == 0.8 and payload["top_k"] == 20
            assert payload["presence_penalty"] == 1.5
        else:
            assert payload["temperature"] == 0.0
            assert payload["top_p"] == 1.0 and payload["top_k"] == 1
            assert payload["presence_penalty"] == 0.0
        assert payload["min_p"] == 0.0
        assert payload["repeat_penalty"] == 1.0 and payload["seed"] == 0
        assert payload["max_tokens"] == 384 and payload["stream"] is False
        assert payload["messages"][-1] == {"role": "user", "content": submitted.prompt}
        assert payload["chat_template_kwargs"] == {
            "enable_thinking": False,
            "preserve_thinking": False,
        }
        assert "tools" not in payload and "reasoning_budget_tokens" not in payload
        if purpose == "general":
            assert payload["messages"][0]["content"] == general_prompt(submitted)
        else:
            assert "isolated NextOps language synthesizer" in payload["messages"][0]["content"]
        assert configured.request_timeout_seconds == 120
        assert configured.context_tokens == 16384 and not configured.thinking_enabled

    asyncio.run(scenario())


@pytest.mark.parametrize("model", (*CANDIDATES, "nextops-qwen3-5-35b-a3b-q4-k-m"))
def test_opt_out_keeps_existing_sampler_payload(model: ModelId) -> None:
    async def scenario() -> None:
        transport = CaptureTransport(model)
        configured = settings(model)
        assert not configured.qwen38_instruct_sampling_enabled
        assert not configured.qwen38_greedy_decoding_enabled
        await LlamaCppProvider(configured, transport).generate(request(temperature=0.3))
        payload = transport.calls[-1][1]
        assert payload["temperature"] == 0.3 and payload["top_p"] == 0.8
        assert payload["presence_penalty"] == 0.0
        assert {"top_k", "min_p", "repeat_penalty", "seed"}.isdisjoint(payload)

    asyncio.run(scenario())


@pytest.mark.parametrize(
    "model", ["nextops-qwen3-5-35b-a3b-q4-k-m", "nextops-qwen3-5-122b-a10b-q5-k-m"]
)
def test_sampling_flag_cannot_reconfigure_unrelated_models(model: ModelId) -> None:
    with pytest.raises(ValueError, match=r"instruct sampling requires an expanded Qwen3\.8"):
        settings(model, qwen38_instruct_sampling_enabled=True)


def test_sampling_opt_in_requires_expanded_profile_without_relaxing_limits() -> None:
    with pytest.raises(ValueError, match="instruct sampling"):
        settings(CANDIDATES[0], qwen38_instruct_sampling_enabled=True, expanded_chat_enabled=False)
    for change in ({"thinking_enabled": True}, {"context_tokens": 32768}):
        with pytest.raises(ValueError):
            settings(CANDIDATES[0], qwen38_instruct_sampling_enabled=True, **change)


@pytest.mark.parametrize(
    "model", ["nextops-qwen3-5-35b-a3b-q4-k-m", "nextops-qwen3-5-122b-a10b-q5-k-m"]
)
def test_greedy_opt_in_denies_unrelated_models(model: ModelId) -> None:
    with pytest.raises(ValueError, match="greedy decoding"):
        settings(model, qwen38_greedy_decoding_enabled=True)


def test_greedy_opt_in_keeps_limits_and_denies_ambiguous_profiles() -> None:
    for change in (
        {"expanded_chat_enabled": False},
        {"thinking_enabled": True},
        {"context_tokens": 32768},
        {"request_timeout_seconds": 121},
    ):
        with pytest.raises(ValueError):
            settings(CANDIDATES[0], qwen38_greedy_decoding_enabled=True, **change)
    with pytest.raises(ValueError, match="mutually exclusive"):
        settings(
            CANDIDATES[0],
            qwen38_greedy_decoding_enabled=True,
            qwen38_instruct_sampling_enabled=True,
        )


@pytest.mark.parametrize(
    "flag,attribute",
    [
        ("NEXTOPS_QWEN38_INSTRUCT_SAMPLING_ENABLED", "qwen38_instruct_sampling_enabled"),
        ("NEXTOPS_QWEN38_GREEDY_DECODING_ENABLED", "qwen38_greedy_decoding_enabled"),
    ],
)
def test_sampling_environment_opt_in_is_explicit(
    monkeypatch: pytest.MonkeyPatch, flag: str, attribute: str
) -> None:
    for name in (
        "CREDENTIALS_DIRECTORY",
        "NEXTOPS_LLAMA_API_KEY_FILE",
        "NEXTOPS_INFERENCE_SERVICE_SECRET_FILE",
        "NEXTOPS_QWEN38_INSTRUCT_SAMPLING_ENABLED",
        "NEXTOPS_QWEN38_GREEDY_DECODING_ENABLED",
        "NEXTOPS_QWEN38_EXTENDED_TIMEOUT_ENABLED",
        "NEXTOPS_THINKING_ENABLED",
    ):
        monkeypatch.delenv(name, raising=False)
    for name, value in {
        "NEXTOPS_LLAMA_BASE_URL": "http://127.0.0.1:18080",
        "NEXTOPS_LLAMA_API_KEY": "synthetic-provider-secret-00000000",
        "NEXTOPS_INFERENCE_SERVICE_SECRET": "synthetic-service-secret-000000000",
        "NEXTOPS_MODEL_ID": CANDIDATES[0],
        "NEXTOPS_CONTEXT_TOKENS": "16384",
        "NEXTOPS_EXPANDED_CHAT_ENABLED": "1",
        "NEXTOPS_INFERENCE_TIMEOUT_SECONDS": "120",
    }.items():
        monkeypatch.setenv(name, value)
    assert not getattr(LlamaCppSettings.from_environment(), attribute)
    monkeypatch.setenv(flag, "1")
    assert getattr(LlamaCppSettings.from_environment(), attribute)
    monkeypatch.setenv(flag, "true")
    assert not getattr(LlamaCppSettings.from_environment(), attribute)
    monkeypatch.setenv(flag, "1")
    monkeypatch.setenv("NEXTOPS_MODEL_ID", "nextops-qwen3-5-35b-a3b-q4-k-m")
    with pytest.raises(ValueError, match=r"instruct sampling|greedy decoding"):
        LlamaCppSettings.from_environment()
