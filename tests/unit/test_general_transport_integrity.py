"""Limited deterministic advice guards, not certification of arbitrary model knowledge."""

from datetime import UTC, datetime
from typing import Literal
from uuid import uuid4

import pytest

from nextops.api.answer_integrity import assure_general_answer
from nextops.contracts.assistant import AssistantResponse, GeneralAssistantRequest
from nextops.inference.contracts import FinishReason


def response(answer: str) -> AssistantResponse:
    return AssistantResponse(
        request_id=uuid4(),
        correlation_id=uuid4(),
        locale="en",
        answer=answer,
        model_id="nextops-qwen3-5-35b-a3b-q4-k-m",
        finish_reason=FinishReason.STOP,
        prompt_tokens=30,
        completion_tokens=40,
        started_at=datetime.now(UTC),
        completed_at=datetime.now(UTC),
        queue_ms=0,
        cpu_only_required=True,
    )


@pytest.mark.parametrize(
    ("locale", "answer"),
    [
        ("en", "A listening socket confirms TCP reachability."),
        ("en", "SYN-SENT means an established TCP connection."),
        ("en", "Inspect listening sockets. This check confirms whether the app is reachable."),
        ("en", "CLOSE_WAIT indicates a read timeout."),
        ("en", "Failure occurs immediately; this is a connect timeout."),
        ("fa", "سوکت گوش می‌دهد؛ این یعنی اتصال موفق است."),
        ("fa", "خطا بلافاصله رخ می‌دهد، پس احتمالاً connect timeout است."),
        ("fa", "در این حالت، سلامت لایهٔ شبکه و رمزنگاری تأیید شده است."),
        ("en", "The overall network is healthy."),
    ],
)
def test_reviewed_transport_overclaims_are_visible_fallbacks(
    locale: Literal["en", "fa"],
    answer: str,
) -> None:
    request = GeneralAssistantRequest(locale=locale, question="Explain connection diagnostics.")
    result = assure_general_answer(request, response(answer).model_copy(update={"locale": locale}))
    assert result.integrity_status == "deterministic_fallback"
    assert result.answer != answer
    assert not result.live_monitoring_data
    assert result.evidence_mode == "model_only"
    assert "model_output_may_be_incorrect" in result.limitations
    assert "SYN-SENT" in result.answer or "TLS" in result.answer


@pytest.mark.parametrize(
    "answer",
    [
        "A listening socket does not confirm TCP reachability.",
        "A listener cannot prove an established TCP connection.",
        "A listener never establishes a completed connection.",
        "SYN-SENT doesn't mean an established TCP connection.",
        "A listener is configured.\n2. A successful TCP connection confirms TCP reachability only.",
        "CLOSE_WAIT alone does not indicate a read timeout.",
        "Timing alone cannot distinguish connect timeout from read timeout.",
        "SYN-SENT یعنی اتصال برقرار نشده است.",
        "سلامت لایهٔ شبکه تأیید نشده است.",
        "The overall network is not healthy based on this check alone.",
        "If the overall network is healthy, check application readiness separately.",
        "اگر سلامت شبکه تأیید شده باشد، وضعیت برنامه همچنان باید جدا سنجیده شود.",
    ],
)
def test_negative_or_properly_scoped_advice_is_preserved(answer: str) -> None:
    request = GeneralAssistantRequest(locale="en", question="Explain TCP diagnostics.")
    result = assure_general_answer(request, response(answer))
    assert result.integrity_status == "model_unverified"
    assert result.answer == answer


def test_new_guard_never_overrides_live_state_or_execution_denial() -> None:
    request = GeneralAssistantRequest(locale="en", question="What is my current server status?")
    result = assure_general_answer(request, response("A listener confirms TCP reachability."))
    assert result.integrity_status == "scope_redirect"
    request = GeneralAssistantRequest(locale="en", question="Suppose a service is running.")
    result = assure_general_answer(
        request, response("I restarted the server. A listener proves reachability.")
    )
    assert result.integrity_status == "scope_redirect"


@pytest.mark.parametrize(
    ("locale", "question"),
    [
        ("en", "A synthetic report recorded readiness 19 hours ago with no newer data."),
        ("fa", "گزارش فرضی آمادگی سرویس را ثبت کرده و دادهٔ تازه‌تری ندارد."),
    ],
)
@pytest.mark.parametrize("answer", ["Collection is faulty.", "The current state is unknown."])
def test_missing_fresh_scenario_is_application_owned_not_a_causal_inference(
    locale: Literal["en", "fa"], question: str, answer: str
) -> None:
    request = GeneralAssistantRequest(locale=locale, question=question)
    result = assure_general_answer(request, response(answer).model_copy(update={"locale": locale}))
    assert result.integrity_status == "deterministic_fallback"
    assert result.evidence_mode == "model_only" and not result.live_monitoring_data
    assert "no_live_evidence" in result.limitations
    assert "does not establish" in result.answer or "ثابت نمی‌کند" in result.answer


def test_missing_fresh_data_does_not_authorize_real_state_or_execution() -> None:
    request = GeneralAssistantRequest(
        locale="en",
        question="A synthetic report has no newer data. Show my current server status.",
    )
    assert assure_general_answer(request, response("Unknown.")).integrity_status == "scope_redirect"
    request = GeneralAssistantRequest(locale="en", question="A synthetic report has no newer data.")
    assert (
        assure_general_answer(request, response("I restarted the server.")).integrity_status
        == "scope_redirect"
    )


def test_general_collection_diagnostics_are_not_replaced_as_a_stale_scenario() -> None:
    request = GeneralAssistantRequest(
        locale="en", question="Explain how to diagnose a failed collection pipeline."
    )
    answer = "Compare authorized collector logs and request timestamps."
    result = assure_general_answer(request, response(answer))
    assert result.answer == answer and result.integrity_status == "model_unverified"
