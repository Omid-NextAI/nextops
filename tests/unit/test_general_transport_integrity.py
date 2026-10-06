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


@pytest.mark.parametrize(
    ("locale", "question"),
    [
        ("en", "Suppose TLS succeeds; does that establish application health?"),
        ("fa", "فرض کن TLS موفق است؛ آیا سلامت برنامه ثابت می‌شود؟"),
        (
            "en",
            "Suppose certificate and hostname validation succeed but an example API returns "
            "HTTP 404. What can and cannot be concluded about whole-network "
            "and application health?",
        ),
        (
            "fa",
            "در یک آزمون فرضی، اعتبارسنجی گواهی و نام میزبان موفق است ولی API خطا می‌دهد. "
            "دربارهٔ سلامت کل شبکه و برنامه چه چیزی معلوم است؟",
        ),
    ],
)
@pytest.mark.parametrize("finish", [FinishReason.STOP, FinishReason.LENGTH])
def test_bounded_tls_scope_is_application_owned_without_relabelling_raw_completion(
    locale: Literal["en", "fa"], question: str, finish: FinishReason
) -> None:
    request = GeneralAssistantRequest(locale=locale, question=question)
    raw = response("DNS resolution works.").model_copy(
        update={"locale": locale, "finish_reason": finish}
    )
    result = assure_general_answer(request, raw)
    assert result.integrity_status == "deterministic_fallback"
    assert result.finish_reason == finish and result.model_id == raw.model_id
    assert result.answer != raw.answer and "DNS" in result.answer
    assert result.evidence_mode == "model_only" and not result.live_monitoring_data


def test_hypothetical_tls_guidance_stays_model_only_but_actual_state_and_actions_are_denied() -> (
    None
):
    request = GeneralAssistantRequest(
        locale="en", question="Suppose TLS is configured. Explain TLS."
    )
    answer = "TLS protects the transport exchange."
    assert assure_general_answer(request, response(answer)).answer == answer
    request = GeneralAssistantRequest(
        locale="en", question="Suppose TLS succeeds. Show my current server health."
    )
    assert assure_general_answer(request, response(answer)).integrity_status == "scope_redirect"
    request = GeneralAssistantRequest(
        locale="en", question="Suppose TLS succeeds; does that establish application health?"
    )
    assert (
        assure_general_answer(request, response("I restarted the server.")).integrity_status
        == "scope_redirect"
    )


@pytest.mark.parametrize(
    ("locale", "question", "answer"),
    [
        (
            "en",
            "A TCP connection to port 443 succeeds but HTTPS returns 502. Explain what this "
            "proves and what remains unknown; no commands.",
            # Retained synthetic Q8 final, not a claim about any real target.
            "This proves the network path, TCP handshake, and TLS termination are functional, "
            "but the upstream origin server failed to return a valid response to the load "
            "balancer or reverse proxy. It remains unknown whether the origin is down, "
            "misconfigured, timing out, or rejecting the request due to application-level errors.",
        ),
        (
            "fa",
            "اتصال TCP برقرار می‌شود ولی HTTPS خطا می‌دهد. چه چیزی ثابت شده و چه چیزی نامعلوم است؟",
            "ثابت شده که دروازه معیوب است و سرویس بالادستی پاسخ معتبر ارائه نکرده است.",
        ),
        (
            "en",
            "Suppose TCP fails and HTTP has no response. What can be concluded?",
            "The backend is offline.",
        ),
        (
            "fa",
            "فرض کن TCP ناموفق است و HTTP پاسخی ندارد؛ چه نتیجه‌ای می‌توان گرفت؟",
            "فایروال درخواست را رد کرده است.",
        ),
    ],
)
@pytest.mark.parametrize("finish", [FinishReason.STOP, FinishReason.LENGTH])
def test_protocol_results_do_not_authorize_topology_or_tls_inferences(
    locale: Literal["en", "fa"], question: str, answer: str, finish: FinishReason
) -> None:
    raw = response(answer).model_copy(update={"locale": locale, "finish_reason": finish})
    result = assure_general_answer(GeneralAssistantRequest(locale=locale, question=question), raw)
    assert result.integrity_status == "deterministic_fallback"
    assert result.evidence_mode == "model_only" and not result.live_monitoring_data
    assert result.answer != raw.answer
    assert "TCP" in result.answer and "HTTP" in result.answer and "TLS" in result.answer
    assert result.finish_reason == finish and result.model_id == raw.model_id


@pytest.mark.parametrize(
    "question",
    [
        "TCP succeeds and HTTPS returns 418. Show our current network health.",
        "TCP و HTTP موفق هستند؛ وضعیت فعلی شبکهٔ شرکت چیست؟",
        "Suppose TCP succeeds and HTTP fails. What is my server status now?",
    ],
)
def test_protocol_wording_cannot_bypass_live_state_denial(question: str) -> None:
    request = GeneralAssistantRequest(locale="en", question=question)
    assert (
        assure_general_answer(request, response("The gateway is broken.")).integrity_status
        == "scope_redirect"
    )


def test_protocol_scope_does_not_replace_tutorials_or_allow_execution_claims() -> None:
    request = GeneralAssistantRequest(
        locale="en", question="Explain the difference between TCP and HTTP."
    )
    raw = response("TCP transports bytes; HTTP is an application protocol.")
    assert assure_general_answer(request, raw).answer == raw.answer
    request = GeneralAssistantRequest(
        locale="en", question="Suppose TCP and HTTP fail. What is unknown?"
    )
    assert (
        assure_general_answer(request, response("I restarted the server.")).integrity_status
        == "scope_redirect"
    )


@pytest.mark.parametrize(
    "answer",
    [
        "The TCP result does not prove TLS validation; the gateway's state remains unknown.",
        "The backend might be offline; that is only a hypothesis, not an observed cause.",
        "از این نتیجه، دروازهٔ معیوب اثبات نشده است؛ وضعیت بالادستی نامعلوم است.",
        "اگر سرویس بالادستی خاموش باشد، خطا ممکن است رخ دهد؛ این فقط یک فرضیه است.",
    ],
)
def test_correctly_qualified_protocol_answers_are_not_replaced(answer: str) -> None:
    request = GeneralAssistantRequest(
        locale="en",
        question="TCP connects but HTTP fails. What is proven and what remains unknown?",
    )
    result = assure_general_answer(request, response(answer))
    assert result.answer == answer and result.integrity_status == "model_unverified"


def test_later_uncertainty_does_not_hide_an_earlier_affirmative_protocol_claim() -> None:
    request = GeneralAssistantRequest(
        locale="en",
        question="TCP connects but HTTP fails. What is proven and what remains unknown?",
    )
    result = assure_general_answer(
        request, response("This proves TLS termination works, but the cause is unknown.")
    )
    assert result.integrity_status == "deterministic_fallback"
