"""Meaningful context, provenance, privacy, and reasoning-budget invariants."""

from datetime import UTC, datetime
from uuid import uuid4

import pytest
from pydantic import ValidationError

from nextops.api.answer_integrity import assure_general_answer
from nextops.api.app import _general_prompt
from nextops.application.conversations import select_context
from nextops.contracts.assistant import AssistantResponse, GeneralAssistantRequest
from nextops.contracts.conversations import (
    ConversationAssistantRequest,
    ConversationMessageRequest,
    SavedMessage,
)
from nextops.inference.contracts import FinishReason, InferenceRequest


def assistant(answer: str = "General guidance only.") -> AssistantResponse:
    now = datetime.now(UTC)
    return AssistantResponse(
        request_id=uuid4(),
        correlation_id=uuid4(),
        locale="en",
        answer=answer,
        model_id="nextops-qwen3-5-35b-a3b-q4-k-m",
        prompt_tokens=12,
        completion_tokens=16,
        finish_reason=FinishReason.STOP,
        started_at=now,
        completed_at=now,
        queue_ms=0,
        cpu_only_required=True,
    )


def message(
    sequence: int, question: str = "What is DNS?", answer: str = "DNS maps names."
) -> SavedMessage:
    return SavedMessage(
        request_id=uuid4(),
        sequence=sequence,
        question=question,
        assistant=assistant(answer),
        thinking_requested=False,
        context_turns=0,
        context_omitted=False,
        created_at=datetime.now(UTC),
    )


def test_context_selects_six_whole_recent_pairs_and_reports_omission() -> None:
    messages = [message(n, question=f"Question {n}") for n in range(1, 9)]
    context, omitted = select_context(messages)
    assert len(context) == 6
    assert context[0].question == "Question 3"
    assert context[-1].question == "Question 8"
    assert omitted


def test_oversized_pair_is_not_silently_clipped() -> None:
    context, omitted = select_context([message(1, answer="پ" * 16_000)])
    assert not context
    assert omitted


def test_rejected_answers_are_not_followup_facts() -> None:
    rejected = message(1).model_copy(
        update={
            "assistant": assistant().model_copy(
                update={"integrity_status": "deterministic_fallback"}
            ),
        }
    )
    assert select_context([rejected]) == ((), True)


def test_saved_operational_followup_still_requires_live_evidence() -> None:
    context, _ = select_context([message(1, question="Explain my Linux server.")])
    request = ConversationAssistantRequest(
        locale="en", question="Is it healthy now?", history=context
    )
    result = assure_general_answer(request, assistant("It is healthy now."))
    assert result.integrity_status == "scope_redirect"
    assert not result.live_monitoring_data


def test_durable_prompt_keeps_literal_unicode_and_untrusted_boundaries() -> None:
    context, _ = select_context([message(1, question="DNS چیست؟", answer="سامانهٔ نام دامنه")])
    request = ConversationAssistantRequest(
        locale="fa",
        question="حالا مثال بزن",
        history=context,
        thinking=True,
        max_output_tokens=2048,
    )
    prompt = _general_prompt(request)
    assert "سامانهٔ نام دامنه" in prompt.question
    assert "untrusted model-only context" in prompt.question
    assert prompt.thinking and prompt.detailed and prompt.max_output_tokens == 2048
    assert (
        _general_prompt(GeneralAssistantRequest(locale="en", question="hi")).max_output_tokens
        == 384
    )


@pytest.mark.parametrize(
    "extra", [{"history": []}, {"roles": ["admin"]}, {"max_output_tokens": 99999}]
)
def test_browser_cannot_supply_memory_policy_or_budget(extra: dict[str, object]) -> None:
    with pytest.raises(ValidationError):
        ConversationMessageRequest.model_validate(
            {
                "request_id": str(uuid4()),
                "locale": "en",
                "question": "hello",
                **extra,
            }
        )


def test_expanded_inference_does_not_expand_live_synthesis() -> None:
    with pytest.raises(ValidationError):
        InferenceRequest(
            request_id=uuid4(),
            correlation_id=uuid4(),
            locale="en",
            prompt="evidence",
            purpose="evidence_synthesis",
            detailed=True,
            max_output_tokens=2048,
        )
