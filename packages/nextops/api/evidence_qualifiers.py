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
_SEVERITIES = (
    ("Not classified", "طبقه‌بندی‌نشده"),
    ("Information", "اطلاعات"),
    ("Warning", "هشدار"),
    ("Average", "متوسط"),
    ("High", "زیاد"),
    ("Disaster", "فاجعه"),
)


def monitoring_counts(locale: str, evidence: MonitoringSummary) -> str:
    """Counts/labels come from typed rows, never sampled or generated prose."""
    count = len(evidence.active_problems)
    counts = [
        sum(p.severity == severity for p in evidence.active_problems) for severity in range(6)
    ]
    labels = "; ".join(
        f"{severity}={_SEVERITIES[severity][locale == 'fa']}: {number}"
        for severity, number in enumerate(counts)
        if number
    )
    truncated = "problems_truncated" in evidence.partial_reasons
    if locale == "fa":
        total = (
            " تعداد کل نامعلوم است؛ این تعداد فقط حد پایینِ نمای دریافتی است." if truncated else ""
        )
        return (
            f"شمارش برنامه در دامنهٔ همین میزبان مجاز: {count} ردیف مشکل فعال دریافت شد؛ "
            f"{len(evidence.metrics)} سنجه دریافت شد.{total}"
            + (f" شدت ردیف‌های دریافتی: {labels}." if labels else "")
            + " دسترسی‌پذیری شبکه و سلامت موتور پایش از این داده نامعلوم است."
        )
    total = (
        " The total is unknown; this is only a lower bound of the returned snapshot."
        if truncated
        else ""
    )
    return (
        f"Application counts within this authorized host scope: {count} active problem row(s) "
        f"returned; {len(evidence.metrics)} metric(s) returned.{total}"
        + (f" Returned-row severity: {labels}." if labels else "")
        + " Network reachability and monitoring-engine health are unknown from this data."
    )


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
            "نبود علامت قدیمی، اثبات سلامت فعلی نیست؛ جزئیات در بخش شواهد است.\n"
            + monitoring_counts(locale, evidence)
        )
    observations = observed or "metric observation time unavailable"
    coverage = "partial" if evidence.is_partial else "marked complete by the received contract"
    return (
        "Evidence qualifiers — supplied by the application:\n"
        f"Source: {source}; scope: only authorized host {_quoted(evidence.host)}; "
        f"collected: {_timestamp(evidence.collected_at)}; "
        f"metric observation times: {observations}.\n"
        f"Coverage: {coverage}; metrics marked stale: {stale}. "
        "Absence of a stale marker is not proof of current health; see the evidence panel.\n"
        + monitoring_counts(locale, evidence)
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
