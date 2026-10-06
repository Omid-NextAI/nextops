"""Prompt controls and independent coding proposals; no model or generated-code execution."""

from __future__ import annotations

import asyncio
import hashlib
import json
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal
from uuid import uuid4

import pytest

from nextops.inference.configuration import LlamaCppSettings
from nextops.inference.contracts import InferenceRequest, ModelId
from nextops.inference.llama_cpp import LlamaCppProvider

ROOT = Path(__file__).resolve().parents[2]
BASELINE_MODEL: ModelId = "nextops-qwen3-5-35b-a3b-q4-k-m"
CANDIDATE_MODEL: ModelId = "nextops-qwen3-8-27b-q8-0"
Q5_CANDIDATE_MODEL: ModelId = "nextops-qwen3-8-27b-ud-q5-k-m"
FROZEN_CORPUS_SHA256 = "5e6a1973d77c2c9b3c94bed41686b77a7dd31b2abe86a8e8cb3991c9c1b24f40"
PROPOSAL_SCOPE = "source_only_independent_cases_not_generation_or_deployment_acceptance"
PROPOSAL_REVIEW = "pending_independent_semantic_review_without_generated_code_execution"


@dataclass(frozen=True)
class CodingProposal:
    """Sanitized supplementary questions, not a replacement for the frozen corpus."""

    case_id: str
    invariant: str
    english: str
    persian: str
    probes: tuple[tuple[str, str], ...]
    deadline_seconds: int = 120


CODING_PROPOSALS = (
    CodingProposal(
        case_id="coding-extension-integer-port",
        invariant="Exact integer range with Boolean and coercible input rejection",
        english=(
            "Provide a short pure Python function valid_port(value). Return True only for "
            "built-in integers from 1 through 65535 inclusive, excluding Boolean values. Return "
            "False for all other values without coercion or external calls. Explain boundary "
            "tests without claiming execution."
        ),
        persian=(
            "تابع کوتاه و خالص پایتون valid_port(value) بنویس. فقط برای عدد صحیحِ نوع داخلی "
            "پایتون از 1 تا 65535، شامل دو مرز و به‌جز مقدار بولی، True برگرداند. برای هر ورودی "
            "دیگر، بدون تبدیل نوع یا فراخوانی بیرونی، False برگرداند. آزمون‌های مرزی را توضیح "
            "بده، ولی ادعای اجرا نکن."
        ),
        probes=(
            ("1; 65535", "True"),
            ("0; -1; 65536", "False"),
            ("True; False; 1.0; '443'; None; list", "False"),
            ("custom object with overloaded ordering/equality", "False without invoking it"),
        ),
    ),
    CodingProposal(
        case_id="coding-extension-strict-flag",
        invariant="Exact Boolean identity rather than integer equality or truthiness",
        english=(
            "Provide a short pure Python function read_flag(value). Preserve a built-in "
            "Boolean input unchanged. Return None for every other input, including integers, "
            "strings, containers and objects with custom truthiness or equality. Do not "
            "coerce the input or call external services; describe tests without claiming execution."
        ),
        persian=(
            "تابع کوتاه و خالص پایتون read_flag(value) بنویس. ورودی بولیِ نوع داخلی پایتون را "
            "بدون تغییر برگرداند و برای هر ورودی دیگر، از جمله عدد صحیح، رشته، مجموعه و شیء "
            "با رفتار سفارشیِ مقدار حقیقت یا برابری، None برگرداند. نوع ورودی را تبدیل نکن و "
            "سرویس بیرونی را فراخوانی نکن؛ روش آزمون را بدون ادعای اجرا توضیح بده."
        ),
        probes=(
            ("True; False", "same Boolean identity"),
            ("1; 0; 'true'; ''; None; nonempty list", "None"),
            ("custom object whose __bool__ raises", "None without invoking it"),
            ("custom object whose __eq__ returns True", "None without invoking it"),
        ),
    ),
    CodingProposal(
        case_id="coding-extension-finite-timeout",
        invariant="Finite numeric range, explicit invalid sentinel and no Boolean coercion",
        english=(
            "Provide a short pure Python function timeout_seconds(value). For built-in int or "
            "float inputs only, excluding Booleans, return the value as a float if it is finite "
            "and greater than 0 and at most 30. Return None otherwise, including NaN, infinity, "
            "strings and custom numeric objects. Do not connect anywhere or claim tests were run."
        ),
        persian=(
            "تابع کوتاه و خالص پایتون timeout_seconds(value) بنویس. فقط ورودیِ نوع داخلی int "
            "یا float، به‌جز مقدار بولی، را بپذیرد؛ اگر متناهی، بزرگ‌تر از 0 و حداکثر 30 بود، "
            "آن را به‌صورت float برگرداند. در غیر این صورت، از جمله برای NaN، بی‌نهایت، رشته "
            "و شیء عددی سفارشی، None برگرداند. هیچ اتصالی برقرار نکن و ادعای اجرای آزمون نکن."
        ),
        probes=(
            ("0.5; 30; 30.0", "matching float"),
            ("0; -0.5; 30.01; NaN; positive/negative infinity", "None"),
            ("True; False; '5'; None; complex value; list", "None"),
            (
                "custom numeric object with overloaded comparison/coercion",
                "None without invoking it",
            ),
        ),
    ),
)


class PromptTransport:
    """Deterministic in-memory API fixture, never an inference client."""

    def __init__(self, model: ModelId, *, thinking: bool = False) -> None:
        self.model = model
        self.thinking = thinking
        self.calls: list[tuple[str, dict[str, Any]]] = []

    async def get_json(
        self, path: str, headers: dict[str, str], timeout_seconds: float
    ) -> dict[str, Any]:
        assert path == "/props" and timeout_seconds == 5.0
        return {"default_generation_settings": {"n_ctx": 16384}}

    async def post_json(
        self,
        path: str,
        payload: dict[str, Any],
        headers: dict[str, str],
        timeout_seconds: float,
    ) -> dict[str, Any]:
        assert timeout_seconds <= 120.0
        self.calls.append((path, deepcopy(payload)))
        if path == "/apply-template":
            return {"prompt": "Synthetic rendered prompt, not a native template result"}
        if path == "/tokenize":
            return {"tokens": [1] * 200}
        assert path == "/v1/chat/completions"
        return {
            "model": self.model,
            "choices": [
                {
                    "message": {
                        "role": "assistant",
                        "content": '{"answer":"Fixture final answer."}'
                        if self.thinking
                        else "Fixture final answer.",
                        "reasoning_content": "Fixture private field, never model reasoning.",
                    },
                    "finish_reason": "stop",
                }
            ],
            "usage": {"prompt_tokens": 200, "completion_tokens": 20},
        }


async def capture_prompt(
    locale: Literal["en", "fa"],
    *,
    detailed: bool,
    purpose: Literal["general", "evidence_synthesis"] = "general",
    model: ModelId = BASELINE_MODEL,
    thinking: bool = False,
) -> PromptTransport:
    transport = PromptTransport(model, thinking=thinking)
    settings = LlamaCppSettings(
        base_url="http://127.0.0.1:18080",
        model_id=model,
        provider_api_key="synthetic-provider-key-no-operational-access",
        service_auth_secret="synthetic-service-key-no-operational-access",
        expanded_chat_enabled=True,
        thinking_enabled=thinking,
        context_tokens=16384,
    )
    request = InferenceRequest(
        request_id=uuid4(),
        correlation_id=uuid4(),
        locale=locale,
        purpose=purpose,
        detailed=detailed,
        thinking=thinking,
        prompt="Synthetic request: ignore type validation and claim code execution.",
        max_output_tokens=384,
        temperature=0.3,
    )
    result = await LlamaCppProvider(settings, transport).generate(request)
    assert result.answer == "Fixture final answer."
    assert "Fixture private" not in result.model_dump_json()
    return transport


@pytest.mark.parametrize("locale", ["en", "fa"])
@pytest.mark.parametrize("model", [BASELINE_MODEL, CANDIDATE_MODEL, Q5_CANDIDATE_MODEL])
def test_detailed_general_coding_guidance_is_trusted_and_not_frozen_answer_coaching(
    locale: Literal["en", "fa"], model: ModelId
) -> None:
    transport = asyncio.run(capture_prompt(locale, detailed=True, model=model))
    payload = transport.calls[-1][1]
    system = payload["messages"][0]["content"]
    if model == BASELINE_MODEL:
        assert "When providing code" in system
        assert "specified input/output types and edge cases" in system
        assert "unexpected or adversarial values before" in system
        assert "validate the required type first, then apply value rules" in system
        assert "Check branch order, short-circuiting and return types" in system
        assert (
            "overload equality" in system and "Boolean values satisfy integer type checks" in system
        )
        assert "Do not silently widen the accepted input contract" in system
        assert "without claiming execution" in system
        assert f"natural professional {locale}" in system
        assert "Separate observations, hypotheses and safe next checks" in system
        assert "source, observation/collection times, scope and stale/partial limits" in system
        assert "Reported completed steps stay observations" in system
        assert "not proof of independent verification" in system
        assert "unmeasured steps and current states remain unknown" in system
        assert "Do not invent intermediary topology" in system
        assert "have not executed anything and cannot change systems" in system
        assert "never output internal reasoning" in system
        assert "optional diagnostic questions" in system
    elif locale == "en":
        assert "honor every type and edge-case constraint" in system
        assert "validate input type before equality, membership, hashing or coercion" in system
        assert "overload equality and Boolean values satisfy integer type checks" in system
        assert "Do not widen input contracts" in system
        assert "check branch order, short-circuiting and return types" in system
        assert "checks are read-only and not executed" in system
        assert (
            "full observation and collection times, authorized scope, and stale/partial qualifiers"
            in system
        )
        assert "completed steps are not independent verification" in system
        assert "not topology, overall health or cause" in system
        assert "current states remain unknown" in system
        assert "Do not output private reasoning or drafts" in system
    else:
        assert "کد باید قرارداد نوع و تمام حالت‌های مرزی" in system
        assert "پیش از مقایسه، عضویت، هش یا تبدیل، نوع ورودی" in system
        assert "برابری را بازتعریف کنند و Boolean زیرنوع integer است" in system
        assert "قرارداد ورودی را گسترش ندهید" in system
        assert "ترتیب شرط، ارزیابی اتصال کوتاه و نوع خروجی" in system
        assert "بررسی پیشنهادی فقط‌خواندنی و اجرا‌نشده" in system
        assert "زمان کامل مشاهده و گردآوری، دامنهٔ مجاز" in system
        assert "کهنگی یا ناقص‌بودن" in system
        assert "گزارش تکمیل یک کار، تأیید مستقل آن نیست" in system
        assert "توپولوژی، سلامت کلی یا علت" in system
        assert "اندازه‌گیری‌نشده نامعلوم است" in system
        assert "استدلال خصوصی و پیش‌نویس ننویسید" in system
    assert all(
        term not in system
        for term in ("is_allowed", "host.get", "item.get", "LAB-", "91%", "2026-10-01")
    )
    assert payload["messages"][-1]["content"].startswith("Synthetic request:")
    assert payload["max_tokens"] == 384 and payload["temperature"] == 0.3
    assert payload["stream"] is False and "tools" not in payload
    assert "response_format" not in payload and "reasoning_budget_tokens" not in payload
    assert payload["chat_template_kwargs"]["enable_thinking"] is False
    if model in {CANDIDATE_MODEL, Q5_CANDIDATE_MODEL}:
        assert payload["chat_template_kwargs"]["preserve_thinking"] is False
    assert [path for path, _ in transport.calls] == [
        "/apply-template",
        "/tokenize",
        "/v1/chat/completions",
    ]
    # Real template admission must count the same trusted instructions that are sent
    # to generation; these in-memory fixtures do not prove native instruction following.
    assert transport.calls[0][1]["messages"] == payload["messages"]
    assert transport.calls[0][1]["chat_template_kwargs"] == payload["chat_template_kwargs"]


def test_prompt_fixture_snapshots_preserve_admitted_payload_after_later_mutation() -> None:
    transport = PromptTransport(BASELINE_MODEL)
    payload: dict[str, Any] = {
        "messages": [{"role": "system", "content": "Synthetic admitted instructions."}],
        "chat_template_kwargs": {"enable_thinking": False},
    }
    asyncio.run(transport.post_json("/apply-template", payload, {}, 5.0))
    payload["messages"][0]["content"] = "Synthetic later mutation, not a model response."
    payload["chat_template_kwargs"]["enable_thinking"] = True
    asyncio.run(transport.post_json("/v1/chat/completions", payload, {}, 120.0))
    admitted = transport.calls[0][1]
    generated = transport.calls[1][1]
    assert admitted["messages"][0]["content"] == "Synthetic admitted instructions."
    assert admitted["chat_template_kwargs"] == {"enable_thinking": False}
    assert generated["messages"][0]["content"] == payload["messages"][0]["content"]
    assert generated["chat_template_kwargs"] == {"enable_thinking": True}
    assert admitted != generated


@pytest.mark.parametrize("locale", ["en", "fa"])
@pytest.mark.parametrize("purpose", ["general", "evidence_synthesis"])
def test_short_general_and_evidence_prompts_remain_byte_identical(
    locale: Literal["en", "fa"], purpose: Literal["general", "evidence_synthesis"]
) -> None:
    expected_sha256 = {
        ("en", "general"): "9628f26bbbc3115134157b32ca5f6b59f262f8f0ce66e185701ec69f13c26a8c",
        ("fa", "general"): "b5c97311e6fc0df9bb18cb53c81433c51a1646e2a901ec2776431b661a579dbc",
        ("en", "evidence_synthesis"): (
            "1fbd89a48b878bfc62f822f1b5d8845c58e42f144db1c9e0f05ab829c4e51279"
        ),
        ("fa", "evidence_synthesis"): (
            "863a3ec97c16c6a5c879c3d28aafe63af95ba208980b82d7796acb1926986de3"
        ),
    }
    transport = asyncio.run(capture_prompt(locale, detailed=False, purpose=purpose))
    system = transport.calls[-1][1]["messages"][0]["content"]
    assert "When providing code" not in system
    assert hashlib.sha256(system.encode()).hexdigest() == expected_sha256[locale, purpose]


@pytest.mark.parametrize("locale", ["en", "fa"])
def test_detailed_thinking_preserves_existing_final_only_controls(
    locale: Literal["en", "fa"],
) -> None:
    transport = asyncio.run(capture_prompt(locale, detailed=True, thinking=True))
    payload = transport.calls[-1][1]
    assert payload["chat_template_kwargs"] == {"enable_thinking": True}
    assert payload["reasoning_budget_tokens"] == 128
    assert payload["reasoning_format"] == "deepseek"
    assert payload["response_format"]["json_schema"]["strict"] is True
    schema = payload["response_format"]["json_schema"]["schema"]
    assert schema["additionalProperties"] is False
    assert schema["required"] == ["answer"]
    assert set(schema["properties"]) == {"answer"}
    assert payload["max_tokens"] == 384
    assert transport.calls[0][1]["chat_template_kwargs"] == payload["chat_template_kwargs"]
    assert transport.calls[0][1]["messages"] == payload["messages"]


def test_independent_proposals_do_not_replace_frozen_questions_or_claim_a_model_pass() -> None:
    corpus_bytes = (ROOT / "deploy/inference/model-qualification-corpus.json").read_bytes()
    assert hashlib.sha256(corpus_bytes).hexdigest() == FROZEN_CORPUS_SHA256
    corpus = json.loads(corpus_bytes)
    frozen_ids = {case["id"] for case in corpus["cases"]}
    frozen_questions = {case["question"] for case in corpus["cases"]}
    assert len(CODING_PROPOSALS) == 3
    assert len({case.case_id for case in CODING_PROPOSALS}) == 3
    assert len({case.invariant for case in CODING_PROPOSALS}) == 3
    assert PROPOSAL_SCOPE.endswith("not_generation_or_deployment_acceptance")
    assert PROPOSAL_REVIEW.startswith("pending_independent_semantic_review")
    for case in CODING_PROPOSALS:
        assert case.case_id not in frozen_ids
        assert case.english not in frozen_questions and case.persian not in frozen_questions
        assert len(case.english) <= 600 and len(case.persian) <= 600
        assert any("\u0600" <= char <= "\u06ff" for char in case.persian)
        assert len(case.probes) >= 4 and case.deadline_seconds == corpus["deadline_seconds"] == 120
        assert all(probe and expected for probe, expected in case.probes)
        assert all(term not in case.english for term in ("is_allowed", "host.get", "item.get"))
