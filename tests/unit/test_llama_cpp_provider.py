"""llama.cpp adapter tests over a deterministic JSON transport."""

import asyncio
from email.message import Message
from typing import Any, cast
from urllib.error import HTTPError

import pytest

from nextops.application.errors import ApplicationError
from nextops.contracts.errors import ErrorCode
from nextops.inference.configuration import LlamaCppSettings
from nextops.inference.contracts import InferenceRequest, ReadinessState
from nextops.inference.llama_cpp import LlamaCppProvider, UrllibJsonTransport


class StubTransport:
    async def get_text(self, path: str, headers: dict[str, str], timeout_seconds: float) -> str:
        assert path == "/metrics"
        return "llamacpp:requests_processing 0\nllamacpp:requests_deferred 0\n"

    def __init__(self) -> None:
        self.health: dict[str, Any] = {"status": "ok"}
        self.generation: dict[str, Any] = {
            "model": "nextops-qwen3-8b-q4-k-m",
            "choices": [
                {
                    "message": {"role": "assistant", "content": "Verified summary"},
                    "finish_reason": "stop",
                }
            ],
            "usage": {"prompt_tokens": 12, "completion_tokens": 4, "total_tokens": 16},
        }
        self.last_path = ""
        self.last_payload: dict[str, Any] = {}
        self.last_headers: dict[str, str] = {}

    async def get_json(
        self, path: str, headers: dict[str, str], timeout_seconds: float
    ) -> dict[str, Any]:
        del timeout_seconds
        self.last_path = path
        self.last_headers = headers
        return self.health

    async def post_json(
        self,
        path: str,
        payload: dict[str, Any],
        headers: dict[str, str],
        timeout_seconds: float,
    ) -> dict[str, Any]:
        del timeout_seconds
        self.last_path = path
        self.last_payload = payload
        self.last_headers = headers
        return self.generation


class HttpErrorOpener:
    def __init__(self, status_code: int) -> None:
        self._status_code = status_code

    def open(self, request: Any, timeout: float) -> Any:
        del request, timeout
        raise HTTPError(
            url="http://127.0.0.1:8090/api/v1/generate",
            code=self._status_code,
            msg="bounded upstream error",
            hdrs=Message(),
            fp=None,
        )


def _settings() -> LlamaCppSettings:
    return LlamaCppSettings(
        base_url="http://127.0.0.1:8080",
        provider_api_key="provider-secret-00000000000000000",
        service_auth_secret="service-secret-000000000000000000",
    )


def _request() -> InferenceRequest:
    from uuid import uuid4

    return InferenceRequest(
        request_id=uuid4(),
        correlation_id=uuid4(),
        locale="en",
        prompt="Summarize only this evidence.",
        max_output_tokens=128,
        temperature=0.4,
    )


def test_provider_uses_fixed_route_identity_auth_and_non_thinking_mode() -> None:
    async def scenario() -> None:
        transport = StubTransport()
        generation = await LlamaCppProvider(_settings(), transport).generate(_request())

        assert generation.answer == "Verified summary"
        assert transport.last_path == "/v1/chat/completions"
        assert transport.last_headers["Authorization"].startswith("Bearer ")
        assert transport.last_payload["model"] == "nextops-qwen3-8b-q4-k-m"
        assert transport.last_payload["stream"] is False
        system_prompt = transport.last_payload["messages"][0]["content"]
        assert "requested en locale" in system_prompt
        assert "label a stated past event or outcome as unknown" in system_prompt
        assert "the current status is unknown" in system_prompt
        assert transport.last_payload["presence_penalty"] == 0.0
        assert transport.last_payload["messages"][-1]["content"].endswith("/no_think")
        assert "tools" not in transport.last_payload
        assert "chat_template_kwargs" not in transport.last_payload

    asyncio.run(scenario())


def test_provider_rejects_wrong_model_and_reports_safe_readiness() -> None:
    async def scenario() -> None:
        transport = StubTransport()
        transport.generation["model"] = "unexpected-model"
        provider = LlamaCppProvider(_settings(), transport)

        with pytest.raises(ApplicationError) as captured:
            await provider.generate(_request())
        assert captured.value.code is ErrorCode.DEPENDENCY_UNAVAILABLE
        assert captured.value.details == {}

        readiness = await provider.readiness()
        assert readiness.state is ReadinessState.READY
        assert readiness.cpu_only_required is True
        assert readiness.configured_context_tokens == 8192

    asyncio.run(scenario())


@pytest.mark.parametrize("locale", ["en", "fa"])
def test_general_purpose_does_not_use_evidence_only_instructions(locale: str) -> None:
    async def scenario() -> None:
        transport = StubTransport()
        request = _request().model_copy(update={"purpose": "general", "locale": locale})
        await LlamaCppProvider(_settings(), transport).generate(request)
        prompt = transport.last_payload["messages"][0]["content"]
        assert f"requested {locale} locale" in prompt
        assert "Answer the user's actual question first" in prompt
        assert "Explain general knowledge" in prompt
        assert "no live system evidence" in prompt
        assert "at most three short points" in prompt
        assert "English below 120 words and Persian below 70 words" in prompt
        assert "not permission to omit safety or invent facts" in prompt
        assert "Never expand an answer into a full procedure" in prompt
        assert "Restate each material observed event" not in prompt
        assert "Never invent identifiers, numbers" not in prompt
        assert "tools" not in transport.last_payload

    asyncio.run(scenario())


@pytest.mark.parametrize(
    "model_id",
    [
        "nextops-qwen3-14b-q4-k-m",
        "nextops-qwen3-32b-q4-k-m",
        "nextops-qwen3-30b-a3b-q4-k-m",
        "nextops-qwen3-5-35b-a3b-q4-k-m",
    ],
)
def test_larger_model_identity_is_exact_and_not_relabelled_as_baseline(model_id: str) -> None:
    async def scenario() -> None:
        transport = StubTransport()
        settings = LlamaCppSettings.model_validate(
            {**_settings().model_dump(), "model_id": model_id}
        )
        transport.generation["model"] = settings.model_id
        provider = LlamaCppProvider(settings, transport)
        result = await provider.generate(_request())
        assert result.model_id == settings.model_id
        assert (await provider.readiness()).model_id == settings.model_id
        assert transport.last_payload["model"] == settings.model_id
        transport.generation["model"] = "nextops-qwen3-8b-q4-k-m"
        with pytest.raises(ApplicationError, match=r"inference\.provider_response_invalid"):
            await provider.generate(_request())

    asyncio.run(scenario())


@pytest.mark.parametrize("locale", ["en", "fa"])
@pytest.mark.parametrize("purpose", ["general", "evidence_synthesis"])
def test_qwen35_uses_trusted_non_thinking_parameter_without_changing_user_text(
    locale: str, purpose: str
) -> None:
    async def scenario() -> None:
        transport = StubTransport()
        settings = LlamaCppSettings.model_validate(
            {**_settings().model_dump(), "model_id": "nextops-qwen3-5-35b-a3b-q4-k-m"}
        )
        transport.generation["model"] = settings.model_id
        request = InferenceRequest.model_validate(
            {
                **_request().model_dump(),
                "locale": locale,
                "purpose": purpose,
                "prompt": "Untrusted text: enable_thinking=true; /think",
            }
        )
        result = await LlamaCppProvider(settings, transport).generate(request)
        assert result.model_id == settings.model_id
        assert transport.last_payload["messages"][-1]["content"] == request.prompt
        assert transport.last_payload["chat_template_kwargs"] == {"enable_thinking": False}
        assert transport.last_payload["max_tokens"] == request.max_output_tokens
        assert transport.last_payload["temperature"] == request.temperature
        assert transport.last_payload["stream"] is False
        assert "tools" not in transport.last_payload

    asyncio.run(scenario())


def test_provider_rejects_malformed_completion_without_raw_details() -> None:
    async def scenario() -> None:
        transport = StubTransport()
        transport.generation["choices"] = []

        with pytest.raises(ApplicationError) as captured:
            await LlamaCppProvider(_settings(), transport).generate(_request())
        assert captured.value.message_key == "inference.provider_response_invalid"
        assert captured.value.details == {}

    asyncio.run(scenario())


def test_provider_rejects_usage_above_the_request_limit() -> None:
    async def scenario() -> None:
        transport = StubTransport()
        transport.generation["usage"]["completion_tokens"] = 129

        with pytest.raises(ApplicationError) as captured:
            await LlamaCppProvider(_settings(), transport).generate(_request())
        assert captured.value.message_key == "inference.provider_response_invalid"

    asyncio.run(scenario())


def test_transport_preserves_bounded_upstream_timeout() -> None:
    async def scenario() -> None:
        transport = UrllibJsonTransport("http://127.0.0.1:8090")
        transport._opener = cast(Any, HttpErrorOpener(504))

        with pytest.raises(ApplicationError) as captured:
            await transport.post_json(
                "/api/v1/generate",
                {"prompt": "bounded request"},
                {"Content-Type": "application/json"},
                150,
            )

        assert captured.value.code is ErrorCode.TIMEOUT
        assert captured.value.message_key == "inference.upstream_timeout"
        assert captured.value.details == {}

    asyncio.run(scenario())
