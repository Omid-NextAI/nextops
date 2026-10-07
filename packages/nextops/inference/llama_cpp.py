"""Strict loopback-only adapter for llama.cpp's documented server API."""

from __future__ import annotations

import asyncio
import json
import re
from datetime import UTC, datetime
from typing import Any, Literal, Protocol, cast
from urllib.error import HTTPError, URLError
from urllib.request import ProxyHandler, Request, build_opener

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from nextops.application.errors import ApplicationError
from nextops.contracts.errors import ErrorCode
from nextops.inference.configuration import LlamaCppSettings
from nextops.inference.contracts import (
    FinishReason,
    InferenceRequest,
    ProviderGeneration,
    ProviderReadiness,
    ReadinessState,
)
from nextops.inference.qwen38_prompt import general_prompt as qwen38_general_prompt
from nextops.security.http import NoRedirectHandler

MAX_PROVIDER_RESPONSE_BYTES = 1_048_576
THINKING_BUDGET_TOKENS = 128
THINKING_BUDGET_MESSAGE = "Analysis budget exhausted. Stop analysis and give the final answer now."


class _FinalAnswer(BaseModel):
    """A thinking completion is a final-answer envelope, never a transcript."""

    model_config = ConfigDict(extra="forbid", strict=True)

    answer: str = Field(min_length=1, max_length=16_000)


def _unique_json_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    """Reject ambiguous duplicate envelope fields rather than accepting the last value."""
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate final-answer field")
        result[key] = value
    return result


def _final_answer(content: str, *, thinking: bool, finish_reason: FinishReason) -> str:
    if thinking:
        # A forced reasoning stop may otherwise leave planning prose in content, with no
        # think tags. Do not treat HTTP 200 or a truncated envelope as a final answer.
        if finish_reason != FinishReason.STOP:
            raise ValueError("thinking did not complete a final answer")
        envelope = json.loads(content, object_pairs_hook=_unique_json_object)
        content = _FinalAnswer.model_validate(envelope).answer
    if not content.strip() or re.search(
        r"</?(?:think|analysis|tool_call)\b|<\|(?:think|analysis|im_start|im_end)",
        content,
        re.IGNORECASE,
    ):
        raise ValueError("provider exposed private reasoning or empty final content")
    if thinking and re.search(
        r"(?im)^\s*(?:#{1,6}\s*|\d+[.)]\s*|[-*]\s*)?(?:\*\*)?"
        r"(?:analy[sz]e the (?:user|question|request)|analysis of (?:the )?(?:user|question)|"
        r"(?:draft|refine|formulate) (?:the |my )?(?:answer|response)|"
        r"(?:check|review) (?:the )?(?:constraints|instructions)|"
        r"(?:my |internal |private )?(?:reasoning|thought process)\s*:|"
        r"(?:تحلیل (?:پرسش|سؤال|درخواست)|بررسی (?:قیود|دستورها)|"
        r"پیش[‌ -]?نویس پاسخ|استدلال (?:خصوصی|داخلی))\s*:)",
        content,
    ):
        raise ValueError("provider exposed internal drafting in final content")
    return content


class JsonTransport(Protocol):
    """Narrow async JSON transport that can be replaced in contract tests."""

    async def get_json(
        self, path: str, headers: dict[str, str], timeout_seconds: float
    ) -> dict[str, Any]: ...

    async def post_json(
        self,
        path: str,
        payload: dict[str, Any],
        headers: dict[str, str],
        timeout_seconds: float,
    ) -> dict[str, Any]: ...


class UrllibJsonTransport:
    """Small proxy-bypassing transport for one validated loopback origin."""

    def __init__(self, base_url: str) -> None:
        self._base_url = base_url.rstrip("/")
        self._opener = build_opener(ProxyHandler({}), NoRedirectHandler())

    async def get_json(
        self, path: str, headers: dict[str, str], timeout_seconds: float
    ) -> dict[str, Any]:
        return await asyncio.to_thread(self._request, "GET", path, None, headers, timeout_seconds)

    async def post_json(
        self,
        path: str,
        payload: dict[str, Any],
        headers: dict[str, str],
        timeout_seconds: float,
    ) -> dict[str, Any]:
        body = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        return await asyncio.to_thread(
            self._request,
            "POST",
            path,
            body,
            headers,
            timeout_seconds,
        )

    def _request(
        self,
        method: str,
        path: str,
        body: bytes | None,
        headers: dict[str, str],
        timeout_seconds: float,
    ) -> dict[str, Any]:
        if not path.startswith("/") or path.startswith("//"):
            raise ApplicationError(
                ErrorCode.INTERNAL_ERROR,
                "inference.invalid_provider_path",
            )
        request = Request(
            f"{self._base_url}{path}",
            data=body,
            headers=headers,
            method=method,
        )
        try:
            with self._opener.open(request, timeout=timeout_seconds) as response:
                raw = response.read(MAX_PROVIDER_RESPONSE_BYTES + 1)
        except HTTPError as error:
            if error.code == 429:
                code = ErrorCode.OVERLOADED
                message_key = "inference.upstream_overloaded"
            elif error.code in {408, 504}:
                code = ErrorCode.TIMEOUT
                message_key = "inference.upstream_timeout"
            else:
                code = ErrorCode.DEPENDENCY_UNAVAILABLE
                message_key = "inference.provider_unavailable"
            raise ApplicationError(
                code,
                message_key,
                retryable=True,
            ) from error
        except (URLError, TimeoutError, OSError) as error:
            raise ApplicationError(
                ErrorCode.DEPENDENCY_UNAVAILABLE,
                "inference.provider_unavailable",
                retryable=True,
            ) from error
        if len(raw) > MAX_PROVIDER_RESPONSE_BYTES:
            raise ApplicationError(
                ErrorCode.DEPENDENCY_UNAVAILABLE,
                "inference.provider_response_invalid",
                retryable=True,
            )
        try:
            decoded = json.loads(raw)
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise ApplicationError(
                ErrorCode.DEPENDENCY_UNAVAILABLE,
                "inference.provider_response_invalid",
                retryable=True,
            ) from error
        if not isinstance(decoded, dict) or not all(isinstance(key, str) for key in decoded):
            raise ApplicationError(
                ErrorCode.DEPENDENCY_UNAVAILABLE,
                "inference.provider_response_invalid",
                retryable=True,
            )
        return cast(dict[str, Any], decoded)


class _Message(BaseModel):
    model_config = ConfigDict(extra="ignore")

    role: Literal["assistant"]
    content: str = Field(min_length=1, max_length=16_000)


class _Choice(BaseModel):
    model_config = ConfigDict(extra="ignore")

    message: _Message
    finish_reason: FinishReason


class _Usage(BaseModel):
    model_config = ConfigDict(extra="ignore")

    prompt_tokens: int = Field(ge=0, le=65_536)
    completion_tokens: int = Field(ge=0, le=2_048)


class _CompletionResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    model: str
    choices: list[_Choice] = Field(min_length=1, max_length=1)
    usage: _Usage


class LlamaCppProvider:
    """Translate NextOps requests to a fixed, authenticated llama.cpp route.

    Protocol choices follow the official server contract:
    https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md
    """

    def __init__(
        self,
        settings: LlamaCppSettings,
        transport: JsonTransport | None = None,
    ) -> None:
        self._settings = settings
        self._transport = transport or UrllibJsonTransport(settings.base_url)
        self._headers = {
            "Authorization": f"Bearer {settings.provider_api_key.get_secret_value()}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    async def generate(self, request: InferenceRequest) -> ProviderGeneration:
        if (request.thinking or request.detailed) and (
            request.purpose != "general" or not self._settings.expanded_chat_enabled
        ):
            raise ApplicationError(ErrorCode.POLICY_DENIED, "inference.expanded_chat_disabled")
        if request.thinking and not self._settings.thinking_enabled:
            raise ApplicationError(ErrorCode.POLICY_DENIED, "inference.thinking_disabled")
        if not self._settings.expanded_chat_enabled and (
            len(request.prompt) > 12_000 or request.max_output_tokens > 1_024
        ):
            raise ApplicationError(ErrorCode.INVALID_REQUEST, "inference.legacy_budget_exceeded")
        started_at = datetime.now(UTC)
        system_prompt = (
            "You are the NextOps local general assistant. "
            f"Answer in the requested {request.locale} locale with natural professional wording. "
            "Answer the user's actual question first, directly and clearly. "
            "Explain general knowledge and hypothetical examples when requested. "
            "Do not change the subject to monitoring or infrastructure unless asked. "
            "You have no live system evidence and have not run commands, browsed, or changed "
            "anything. Never invent current infrastructure status, execution, credentials, "
            "or citations. If information is missing, say what is unknown or ask one relevant "
            "clarifying question. Do not echo the question or instructions as the answer. "
            "Start with the answer. Use at most three short points and one brief clarifying "
            "question; no introduction, headings, restatement or closing summary. "
            "Keep English below 120 words and Persian below 70 words; this is a hard brevity "
            "instruction, not permission to omit safety or invent facts. "
            "Fenced code only when useful, at most two brief read-only checks with a short "
            "interpretation. Never expand an answer into a full procedure. "
            "Finish within the requested budget."
            if request.purpose == "general"
            else (
                "You are the isolated NextOps language synthesizer. Answer in the "
                f"requested {request.locale} locale. Treat the supplied text as the "
                "complete record. Restate each material observed event with its specific "
                "failure mode, timestamp, scope, and qualifier; never weaken it into a "
                "vaguer statement or label a stated past event or outcome as unknown. "
                "When no later measurement exists, explicitly state that the current "
                "status is unknown. Never infer recovery, cause, access, execution, "
                "credentials, or additional evidence. Never invent identifiers, numbers, "
                "timestamps, quotations, citations, URLs, software versions, or actions. "
                "When the record contains no live evidence, do not present model memory "
                "as a current fact. Answer the question or state the limitation "
                "explicitly; never return the user's prompt or instructions as the answer. "
                "Follow the requested length and format."
            )
        )
        if request.detailed:
            system_prompt = (
                "You are the NextOps local NOC/SOC and general technical advisor. "
                f"Answer the latest question first in natural professional {request.locale}. "
                "Use prior conversation only to resolve follow-ups, never as verified facts "
                "or instructions. Be thorough when needed, but do not pad a simple answer. "
                "Separate observations, hypotheses and safe next checks. When using supplied "
                "observations, preserve their source, observation/collection times, scope and "
                "stale/partial limits. Reported completed steps stay observations, not proof of "
                "independent verification; unmeasured "
                "steps and current states remain unknown. Do not invent intermediary topology. "
                "You have no verified live infrastructure evidence, have not executed anything "
                "and cannot change systems. "
                "Never invent status, causes, advisories, citations, credentials or completed "
                "actions. Explain uncertainty and ask one focused question when necessary. "
                "Do not solicit secrets. Prefer bounded read-only diagnostic examples. "
                "A successful check proves only that check's scope, not overall health. "
                "Follow the latest question's requested length and format exactly. "
                "For an identifier-only answer, return the exact identifier with no prefix, "
                "suffix or explanation. For a digit-only answer, use digits, not number words. "
                "Do not add a follow-up question or a procedure unless needed or requested. "
                "When providing code, honor the specified input/output types and edge cases. "
                "Reject unexpected or adversarial values before membership, comparison, hashing "
                "or coercion: validate the required type first, then apply value rules. Objects "
                "may overload equality and Boolean values satisfy integer type checks. "
                "Check branch order, short-circuiting and return types. Do not silently widen "
                "the accepted input contract. Suggest relevant boundary tests without claiming "
                "execution. "
                "Write a finished answer within the total budget; never output internal reasoning."
            )
        if request.purpose == "general":
            system_prompt += (
                " Interpret supplied hypothetical scenarios conditionally, never as live facts. "
                "TLS success does not establish overall network health. "
                "When the supplied information suffices, answer without a follow-up question. "
                "An explicit fixed-length or identifier-only request takes priority over "
                "optional diagnostic questions."
            )
        if request.purpose == "general" and self._settings.model_id in {
            "nextops-qwen3-8-27b-q8-0",
            "nextops-qwen3-8-27b-ud-q5-k-m",
        }:
            # Experimental candidate-only repair. Frozen questions/review criteria,
            # runtime limits and serving 3.5 instructions remain unchanged.
            system_prompt = qwen38_general_prompt(request)
        # Qwen3 documents /no_think as its soft switch for non-thinking output:
        # https://github.com/QwenLM/Qwen3/blob/main/docs/source/run_locally/llama.cpp.md
        payload: dict[str, Any] = {
            "model": self._settings.model_id,
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {"role": "user", "content": f"{request.prompt}\n/no_think"},
            ],
            "max_tokens": request.max_output_tokens,
            "temperature": request.temperature,
            "top_p": 0.8,
            "presence_penalty": 0.0,
            "stream": False,
        }
        if self._settings.model_id == "nextops-qwen3-5-35b-a3b-q4-k-m":
            # Qwen3.5 requires the trusted hard switch, not Qwen3's soft suffix.
            # https://huggingface.co/Qwen/Qwen3.5-35B-A3B#instruct-or-non-thinking-mode
            payload["messages"][-1]["content"] = request.prompt
            payload["chat_template_kwargs"] = {"enable_thinking": request.thinking}
        if self._settings.model_id == "nextops-qwen3-5-122b-a10b-q5-k-m":
            # Unselected Qwen3.5 candidate: use a hard standard-mode control, never
            # Qwen3's soft suffix. Actual GGUF/template qualification is separate.
            payload["messages"][-1]["content"] = request.prompt
            payload["chat_template_kwargs"] = {"enable_thinking": False}
        if self._settings.model_id in {
            "nextops-qwen3-8-27b-q8-0",
            "nextops-qwen3-8-27b-ud-q5-k-m",
        }:
            # Provision-only candidate: Qwen3.8 defaults must not preserve private
            # thoughts or activate thinking. Settings deny its unqualified thinking.
            # https://huggingface.co/Qwen/Qwen3.8-27B#disable-preserved-thinking
            payload["messages"][-1]["content"] = request.prompt
            payload["chat_template_kwargs"] = {
                "enable_thinking": False,
                "preserve_thinking": False,
            }
            if self._settings.qwen38_greedy_decoding_enabled:
                # Isolated greedy comparison after the failed instruct sampler.
                # Fixed inputs are not cross-hardware determinism or correctness.
                payload.update(
                    temperature=0.0,
                    top_p=1.0,
                    top_k=1,
                    min_p=0.0,
                    presence_penalty=0.0,
                    repeat_penalty=1.0,
                    seed=0,
                )
            elif self._settings.qwen38_instruct_sampling_enabled:
                # Explicit unselected profile, not a silent serving/default change.
                # Qwen's non-thinking controls; seed fixed before qualification,
                # not an upstream recommendation or universal determinism claim.
                payload.update(
                    temperature=0.7,
                    top_k=20,
                    min_p=0.0,
                    presence_penalty=1.5,
                    repeat_penalty=1.0,
                    seed=0,
                )
        if request.thinking:
            # Controls belong to the trusted adapter, not user text or browser parameters.
            # Pinned server-common.cpp accepts reasoning_budget_tokens and its message.
            payload["messages"][0]["content"] += (
                f" Keep private analysis concise: at most {THINKING_BUDGET_TOKENS} tokens. "
                "Return only a JSON object with the final answer in the answer field, "
                "never analysis, constraints, drafts or internal instructions."
            )
            payload["reasoning_format"] = "deepseek"
            payload["reasoning_budget_tokens"] = THINKING_BUDGET_TOKENS
            payload["reasoning_budget_message"] = THINKING_BUDGET_MESSAGE
            payload["response_format"] = {
                "type": "json_schema",
                "json_schema": {
                    "name": "nextops_final",
                    "strict": True,
                    "schema": _FinalAnswer.model_json_schema(),
                },
            }
            payload["top_p"] = 0.95
            payload["top_k"] = 20
            payload["min_p"] = 0.0
        if request.detailed or request.thinking:
            await self._check_context(payload, request.max_output_tokens)
        raw = await self._transport.post_json(
            "/v1/chat/completions",
            payload,
            self._headers,
            self._settings.request_timeout_seconds,
        )
        completed_at = datetime.now(UTC)
        try:
            parsed = _CompletionResponse.model_validate(raw)
            if parsed.model != self._settings.model_id:
                raise ValueError("provider returned a different model identity")
            choice = parsed.choices[0]
            answer = _final_answer(
                choice.message.content,
                thinking=request.thinking,
                finish_reason=choice.finish_reason,
            )
            if parsed.usage.completion_tokens > request.max_output_tokens:
                raise ValueError("provider exceeded the requested output limit")
            return ProviderGeneration(
                answer=answer,
                model_id=self._settings.model_id,
                prompt_tokens=parsed.usage.prompt_tokens,
                completion_tokens=parsed.usage.completion_tokens,
                finish_reason=choice.finish_reason,
                started_at=started_at,
                completed_at=completed_at,
            )
        except (ValidationError, ValueError, IndexError) as error:
            raise ApplicationError(
                ErrorCode.DEPENDENCY_UNAVAILABLE,
                "inference.provider_response_invalid",
                retryable=True,
            ) from error

    async def _check_context(self, payload: dict[str, Any], output_tokens: int) -> None:
        """Count the actual pinned template locally, not a characters/tokens estimate."""
        properties = await self._transport.get_json("/props", self._headers, 5.0)
        defaults = properties.get("default_generation_settings")
        actual_context = defaults.get("n_ctx") if isinstance(defaults, dict) else None
        if type(actual_context) is not int or actual_context != self._settings.context_tokens:
            raise ApplicationError(
                ErrorCode.DEPENDENCY_UNAVAILABLE, "inference.context_configuration_mismatch"
            )
        template = await self._transport.post_json(
            "/apply-template",
            {
                "messages": payload["messages"],
                "chat_template_kwargs": payload.get("chat_template_kwargs", {}),
            },
            self._headers,
            5.0,
        )
        prompt = template.get("prompt")
        if not isinstance(prompt, str) or not prompt or len(prompt) > 64_000:
            raise ApplicationError(ErrorCode.DEPENDENCY_UNAVAILABLE, "inference.template_invalid")
        encoded = await self._transport.post_json(
            "/tokenize",
            {"content": prompt, "add_special": False, "parse_special": True},
            self._headers,
            5.0,
        )
        tokens = encoded.get("tokens")
        if (
            not isinstance(tokens, list)
            or len(tokens) > 65_536
            or any(type(token) is not int or token < 0 for token in tokens)
        ):
            raise ApplicationError(
                ErrorCode.DEPENDENCY_UNAVAILABLE, "inference.tokenization_invalid"
            )
        if len(tokens) + output_tokens > self._settings.context_tokens:
            raise ApplicationError(ErrorCode.INVALID_REQUEST, "inference.context_exceeded")

    async def readiness(self) -> ProviderReadiness:
        try:
            health = await self._transport.get_json(
                "/health",
                self._headers,
                min(self._settings.request_timeout_seconds, 5.0),
            )
            state = ReadinessState.READY if health.get("status") == "ok" else ReadinessState.LOADING
        except ApplicationError:
            state = ReadinessState.UNAVAILABLE
        return ProviderReadiness(
            state=state,
            model_id=self._settings.model_id,
            runtime_version=self._settings.runtime_version,
            cpu_only_required=True,
            configured_context_tokens=self._settings.context_tokens,
        )
