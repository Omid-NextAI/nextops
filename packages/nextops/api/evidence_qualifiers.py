"""Application-owned provenance text, independent of generated answer wording.

This is not a semantic verifier. Only validated, already authorized contracts are
accepted; it neither retrieves evidence nor expands its scope.
"""

# Intentional native Persian product text.
# ruff: noqa: RUF001

import json
from datetime import datetime
from typing import Literal

from nextops.contracts.assistant import AssistantResponse
from nextops.contracts.incidents import IncidentEvidence
from nextops.contracts.monitoring import MonitoringSummary

Locale = Literal["en", "fa"]
ANSWER_LIMIT = 16_000
_BIDI_CONTROLS = "\u061c\u200e\u200f\u202a\u202b\u202c\u202d\u202e\u2066\u2067\u2068\u2069"


def _timestamp(value: datetime) -> str:
    return value.isoformat().replace("+00:00", "Z")


def _quoted(value: str) -> str:
    # Names are data, not prose instructions. Escape newlines/control characters;
    # the existing browser text renderer, never HTML insertion, displays them.
    return json.dumps(value, ensure_ascii=False).translate(
        {ord(char): f"\\u{ord(char):04x}" for char in _BIDI_CONTROLS}
    )


def monitoring_qualifiers(locale: Locale, evidence: MonitoringSummary) -> str:
    """Identify this one-host snapshot without inferring present health."""
    source = "Zabbix"
    if evidence.source_id is not None:
        source += f" ({evidence.source_id})"
    observed = ", ".join(sorted({_timestamp(metric.measured_at) for metric in evidence.metrics}))
    stale = sum(metric.stale for metric in evidence.metrics)
    if locale == "fa":
        observations = observed or "زمان مشاهدهٔ سنجه در دسترس نیست"
        coverage = "ناقص" if evidence.is_partial else "طبق قرارداد دریافتی کامل"
        return (
            "مشخصات شاهد — درج‌شده توسط برنامه:\n"
            f"منبع: {source}؛ دامنه: فقط میزبان مجاز {_quoted(evidence.host)}؛ "
            f"گردآوری: {_timestamp(evidence.collected_at)}؛ "
            f"زمان‌های مشاهدهٔ سنجه‌ها: {observations}.\n"
            f"پوشش: {coverage}؛ سنجه‌های علامت‌گذاری‌شده به‌عنوان قدیمی: {stale}. "
            "نبود علامت قدیمی، اثبات سلامت فعلی نیست؛ جزئیات در بخش شواهد است."
        )
    observations = observed or "metric observation time unavailable"
    coverage = "partial" if evidence.is_partial else "marked complete by the received contract"
    return (
        "Evidence qualifiers — supplied by the application:\n"
        f"Source: {source}; scope: only authorized host {_quoted(evidence.host)}; "
        f"collected: {_timestamp(evidence.collected_at)}; "
        f"metric observation times: {observations}.\n"
        f"Coverage: {coverage}; metrics marked stale: {stale}. "
        "Absence of a stale marker is not proof of current health; see the evidence panel."
    )


def incident_qualifiers(locale: Locale, evidence: IncidentEvidence) -> str:
    """Keep direct Linux and Zabbix scopes distinct, including collection times."""
    zabbix = monitoring_qualifiers(locale, evidence.zabbix.summary)
    target = _quoted(evidence.target_id)
    collected = _timestamp(evidence.linux.collected_at)
    if locale == "fa":
        coverage = "ناقص" if evidence.is_partial else "طبق قرارداد دریافتی کامل"
        return (
            f"{zabbix}\nLinux: فقط هدف مجاز {target}؛ گردآوری: {collected}؛ "
            f"پوشش ترکیبی: {coverage}. این دو منبع لزوماً به یک میزبان اشاره ندارند؛ "
            "سابقه یا رخدادِ موجود، همراه زمان مستقل آن، در بخش شواهد قابل بررسی است."
        )
    coverage = "partial" if evidence.is_partial else "marked complete by the received contract"
    return (
        f"{zabbix}\nLinux: only authorized target {target}; collected: {collected}; "
        f"combined coverage: {coverage}. These sources are not necessarily the same host; "
        "see the evidence panel for any history/event records and their own times."
    )


def with_evidence_qualifiers(assistant: AssistantResponse, qualifiers: str) -> AssistantResponse:
    """Preserve raw completion metadata; do not silently clip to fit the contract."""
    if assistant.evidence_mode == "model_only" or not assistant.live_monitoring_data:
        raise ValueError("evidence qualifiers require an already guarded live-evidence result")
    answer = f"{assistant.answer}\n\n{qualifiers}"
    status = assistant.integrity_status
    if len(answer) > ANSWER_LIMIT:
        answer = (
            "پاسخ تولیدشده برای حفظ مشخصات الزامی شاهد بیش‌ازحد طولانی بود؛ "
            "جزئیات معتبر را در بخش شواهد بررسی کنید."
            if assistant.locale == "fa"
            else "The generated answer was too long to preserve required evidence qualifiers; "
            "review the attributable details in the evidence panel."
        ) + f"\n\n{qualifiers}"
        status = "deterministic_fallback"
    # Revalidate the public bound and label invariants instead of relying on
    # model_copy(), which does not validate updated values.
    return AssistantResponse.model_validate(
        {**assistant.model_dump(), "answer": answer, "integrity_status": status}
    )
