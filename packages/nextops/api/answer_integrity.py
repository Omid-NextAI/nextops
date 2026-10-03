"""Deterministic truthfulness controls around locally generated assistant text."""

# Ruff's confusable-character rule is not suitable for intentional Persian user-facing text.
# ruff: noqa: RUF001

from __future__ import annotations

import ipaddress
import re
from datetime import datetime
from decimal import Decimal

from nextops.api.incident_focus import (
    incident_focus,
    monitoring_cpu_focus,
    requested_service_units,
)
from nextops.api.target_focus import evidence_host_role, requested_named_target
from nextops.contracts.assistant import AssistantRequest, AssistantResponse, GeneralAssistantRequest
from nextops.contracts.conversations import ConversationAssistantRequest
from nextops.contracts.incidents import IncidentEvidence, IncidentInvestigationRequest
from nextops.contracts.monitoring import MonitoringSummary
from nextops.inference.contracts import FinishReason

_LIVE_QUESTION_MARKERS = re.compile(
    r"(?:\b(?:current|currently|now|today|live|status|state|health|running|available|"
    r"restarted|rebooted|deployed|installed|changed)\b|"
    r"(?:وضعیت|همین\s*الان|(?<!\w)الان(?!\w)|اکنون|فعلی|زنده|سلامت|در\s*حال\s*اجرا|"
    r"راه[‌ ]اندازی\s*مجدد|"
    r"ری[‌ ]استارت|نصب|اعمال))",
    re.IGNORECASE,
)
_OPERATIONAL_SUBJECT_MARKERS = re.compile(
    r"(?:\b(?:server|service|system|database|zabbix|linux|host|vm|deployment|application|"
    r"connector|infrastructure|network|firewall|router|switch|vpn|dns|interface)\b|"
    r"(?:سرور|سرویس|سامانه|سیستم|پایگاه\s*داده|زبیکس|لینوکس|میزبان|ماشین\s*مجازی|"
    r"استقرار|برنامه|کانکتور|زیرساخت|شبکه|فایروال|دیوار\s*آتش|روتر|سوییچ|سوئیچ))",
    re.IGNORECASE,
)
_DIAGNOSTIC_GUIDANCE_QUESTION = re.compile(
    r"^\s*(?:how\s+(?:can|do|should)\s+(?:i|we)\s+"
    r"(?:safely\s+)?(?:check|diagnose|troubleshoot|inspect|investigate|verify)\b|"
    r"(?:چطور|چگونه).{0,60}(?:بررسی|عیب[‌ ]یابی|ارزیابی).{0,20}"
    r"(?:کنم|کنیم|انجام\s*دهم|انجام\s*دهیم))",
    re.IGNORECASE,
)
_EXPLICIT_CURRENT_FACT_QUESTION = re.compile(
    r"(?:(?:^|[?;.]\s*|\band\s+)(?:what|which|is|are|show|tell|report)\b.{0,80}"
    r"\b(?:current|currently|now|today|my|our)\b|"
    r"(?:وضعیت.{0,60}(?:چیست|چگونه\s*است)|آیا.{0,60}(?:اکنون|فعلی|الان)))",
    re.IGNORECASE,
)
_SINGLE_CHECK_HEALTH = re.compile(
    r"(?:\b(?:successful|succeeds|success)\b.{0,80}\b(?:means|proves|confirms)\b"
    r".{0,45}\b(?:network|system|service|server)\b.{0,25}\b(?:healthy|secure|safe)\b|"
    r"(?:موفقیت|موفق\s*بودن|موفق\s*باشد|موفق\s*شود).{0,40}"
    r"(?:یعنی|اثبات\s*می[‌ ]کند|نشان\s*می[‌ ]دهد).{0,35}"
    r"(?:شبکه|سامانه|سیستم|سرویس|سرور).{0,25}(?:سالم|امن))",
    re.IGNORECASE,
)
_HEALTH_NEGATION = re.compile(r"(?:\b(?:not|never|cannot)\b|نیست|نمی[‌ ]|نه\s)", re.IGNORECASE)
_HEALTH_TRAILING_NEGATION = re.compile(r"^\s*(?:نیست|نمی[‌ ]|نخواهد)")
_UNSAFE_EXECUTION_CLAIMS = (
    re.compile(
        r"\b(?:i|we)\s+(?:have\s+)?(?:successfully\s+)?(?:restarted|rebooted|deployed|"
        r"installed|changed|deleted|fixed|executed|ran|rotated)\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"(?:من|ما).{0,32}(?:راه[‌ ]اندازی\s*مجدد|ری[‌ ]استارت|استقرار|نصب|تغییر|حذف|"
        r"اصلاح|اجرا|تعویض).{0,24}(?:کردم|کردیم|انجام\s*دادم|انجام\s*دادیم|شد|شده\s*است)",
        re.IGNORECASE,
    ),
)
_UNSUPPORTED_CAUSE_CLAIMS = (
    re.compile(r"\b(?:the\s+)?(?:root\s+)?cause\s+(?:is|was)\b", re.IGNORECASE),
    re.compile(r"\b(?:was|is)\s+caused\s+by\b", re.IGNORECASE),
    re.compile(r"علت\s+(?:اصلی|ریشه[‌ ]ای).{0,20}(?:است|بود)", re.IGNORECASE),
)
_PARTIAL_DISCLOSURE = re.compile(
    r"(?:\b(?:partial|incomplete|limited|truncated)\b|(?:ناقص|جزئی|محدود|کامل\s+نیست))",
    re.IGNORECASE,
)
_STALE_DISCLOSURE = re.compile(
    r"(?:\b(?:stale|outdated|not\s+current|current\s+(?:state|status)\s+is\s+unknown)\b|"
    r"(?:قدیمی|کهنه|به[‌ ]روز\s+نیست|وضعیت\s+فعلی.{0,12}نامعلوم))",
    re.IGNORECASE,
)
_ZABBIX_DISCLOSURE = re.compile(r"(?:\bzabbix\b|زبیکس)", re.IGNORECASE)
_LINUX_DISCLOSURE = re.compile(r"(?:\blinux\b|لینوکس)", re.IGNORECASE)
_GREETING_ONLY = re.compile(r"\s*(?:hi|hello|hey|سلام|درود)[\s!?.،؟]*", re.IGNORECASE)
_GREETING_REPLY = {
    "en": re.compile(
        r"\s*(?:hi|hello|hey|greetings|good (?:morning|afternoon|evening))\b",
        re.IGNORECASE,
    ),
    "fa": re.compile(r"\s*(?:سلام|درود|صبح بخیر|عصر بخیر|وقت بخیر)(?:$|[\s!?.،؟])"),
}
_GREETING_TELEMETRY = re.compile(
    r"(?:\b(?:cpu|ram|memory|disk|metric|alert|problem|trigger)\b|"
    r"(?:پردازنده|حافظه|دیسک|سنجه|هشدار|مشکل|رخداد))",
    re.IGNORECASE,
)
_PROMPT_BOUNDARY_LEAK = re.compile(
    r"(?:user question \((?:bounded )?untrusted|untrusted zabbix|"
    r"data only, never instructions|answer the user's question directly)",
    re.IGNORECASE,
)
_SYSTEM_FILE_REQUEST = re.compile(
    r"(?:\b(?:show(?:ing)?|list(?:ing)?|display(?:ing)?|find(?:ing)?)\b.{0,60}"
    r"\b(?:system files|filesystems?|file systems?)\b|"
    r"(?:نشان\s*بده|نمایش\s*بده|فهرست\s*کن).{0,60}(?:فایل|فایل[‌ ]?سیستم)|"
    r"(?:فایل|فایل[‌ ]?سیستم).{0,60}(?:نشان\s*بده|نمایش\s*بده|فهرست\s*کن))",
    re.IGNORECASE,
)
_MULTI_HOST_QUESTION = re.compile(
    r"(?:\b(?:hosts|servers|vms)\b|میزبان[‌ ]?های?|سرور[‌ ]?های?)",
    re.IGNORECASE,
)
_HOST_AVAILABILITY_QUESTION = re.compile(
    r"(?:\b(?:unavailable|available|offline|online|unreachable|down)\b|"
    r"در\s*دسترس|خارج\s*از\s*دسترس|قطع|خاموش)",
    re.IGNORECASE,
)


def assure_general_answer(
    request: AssistantRequest,
    assistant: AssistantResponse,
) -> AssistantResponse:
    """Label model-only output and replace unverifiable operational claims."""

    historical_subject = bool(
        isinstance(request, GeneralAssistantRequest | ConversationAssistantRequest)
        and any(_OPERATIONAL_SUBJECT_MARKERS.search(turn.question) for turn in request.history)
    )
    direct_subject = bool(_OPERATIONAL_SUBJECT_MARKERS.search(request.question))
    explicit_current_fact = bool(_EXPLICIT_CURRENT_FACT_QUESTION.search(request.question))
    requires_live_evidence = bool(
        (
            (
                _LIVE_QUESTION_MARKERS.search(request.question)
                and (direct_subject or historical_subject)
            )
            or (explicit_current_fact and direct_subject)
        )
        and (not _DIAGNOSTIC_GUIDANCE_QUESTION.search(request.question) or explicit_current_fact)
    )
    file_request = bool(_SYSTEM_FILE_REQUEST.search(request.question))
    unsafe_claim = _contains_unsafe_execution_claim(assistant.answer)
    single_check_health = any(
        not _HEALTH_NEGATION.search(match.group())
        and not _HEALTH_TRAILING_NEGATION.search(assistant.answer[match.end() : match.end() + 16])
        for match in _SINGLE_CHECK_HEALTH.finditer(assistant.answer)
    )
    prompt_echo = _is_long_prompt_echo(request.question, assistant.answer)
    incomplete = assistant.finish_reason != FinishReason.STOP
    greeting_mismatch = bool(
        _GREETING_ONLY.fullmatch(request.question)
        and (
            len(assistant.answer) > 200
            or not _GREETING_REPLY[request.locale].match(assistant.answer)
            or _OPERATIONAL_SUBJECT_MARKERS.search(assistant.answer)
            or _GREETING_TELEMETRY.search(assistant.answer)
        )
    )
    if (
        not requires_live_evidence
        and not file_request
        and not unsafe_claim
        and not single_check_health
        and not prompt_echo
        and not incomplete
        and not greeting_mismatch
    ):
        return assistant.model_copy(
            update={
                "evidence_mode": "model_only",
                "live_monitoring_data": False,
                "integrity_status": "model_unverified",
                "limitations": ("no_live_evidence", "model_output_may_be_incorrect"),
            }
        )

    limitations: tuple[str, ...]
    if file_request:
        answer = (
            "دستیار عمومی به فایل‌های سیستم دسترسی ندارد. «بررسی رخداد» تنها می‌تواند ظرفیت "
            "نقاط اتصالِ مجاز را نشان دهد، نه نام یا محتوای فایل‌ها."
            if request.locale == "fa"
            else "General assistant cannot inspect system files. Incident investigation can show "
            "only approved filesystem mount capacity, not file names or contents."
        )
        integrity_status = "scope_redirect"
        limitations = (
            "no_live_evidence",
            "read_only_no_action_performed",
            "file_listing_unavailable",
        )
    elif prompt_echo or incomplete:
        answer = (
            "مدل محلی پاسخ قابل اتکایی تولید نکرد. پرسش را با عبارت‌بندی دقیق‌تر دوباره مطرح کنید؛ "
            "برای وضعیت زیرساخت نیز یکی از حالت‌های دارای شاهد زنده را به کار ببرید."
            if request.locale == "fa"
            else "The local model did not produce a reliable answer. Rephrase the question more "
            "precisely, or use a live evidence mode for infrastructure state."
        )
        integrity_status = "deterministic_fallback"
        limitations = ("no_live_evidence", "model_output_may_be_incorrect")
    elif greeting_mismatch:
        answer = (
            "سلام! چطور می‌توانم کمک کنم؟" if request.locale == "fa" else "Hello! How can I help?"
        )
        integrity_status = "deterministic_fallback"
        limitations = ("no_live_evidence", "model_output_may_be_incorrect")
    elif single_check_health and not requires_live_evidence and not unsafe_claim:
        answer = (
            "نتیجه‌گیری مدل بیش‌ازحد کلی بود. موفقیت یک بررسی شبکه فقط همان مسیر، مقصد و "
            "پروتکلِ بررسی‌شده را تأیید می‌کند؛ سلامت کل شبکه، امنیت یا کارکرد سرویس‌های دیگر "
            "را ثابت نمی‌کند. مقصد و پورت موردنظر و خروجی پالایش‌شده را مشخص کنید تا بررسی "
            "فقط‌خواندنیِ دقیق‌تری پیشنهاد شود. هیچ وضعیت زنده یا اجرای عملیاتی تأیید نشده است."
            if request.locale == "fa"
            else "The model's conclusion was too broad. A successful network check confirms only "
            "the tested path, destination and protocol, not overall network health, security or "
            "other services. Specify the target and port and provide redacted output for more "
            "focused read-only guidance. No live status or executed action has been verified."
        )
        integrity_status = "deterministic_fallback"
        limitations = ("no_live_evidence", "model_output_may_be_incorrect")
    else:
        answer = (
            "حالت «دستیار عمومی» به شواهد زنده دسترسی ندارد؛ بنابراین نمی‌توانم وضعیت فعلی "
            "زیرساخت یا انجام‌شدن یک عملیات را تأیید کنم. برای دریافت دادهٔ تازه و قابل انتساب، "
            "حالت «پایش زنده» یا «بررسی رخداد» را انتخاب کنید."
            if request.locale == "fa"
            else "General assistant mode has no live evidence, so I cannot verify the current "
            "infrastructure state or claim that an operation occurred. Select Live monitoring or "
            "Incident investigation for fresh, attributable evidence."
        )
        integrity_status = "scope_redirect"
        limitations = ("no_live_evidence", "read_only_no_action_performed")
    return assistant.model_copy(
        update={
            "answer": answer,
            "evidence_mode": "model_only",
            "live_monitoring_data": False,
            "integrity_status": integrity_status,
            "limitations": limitations,
        }
    )


def assure_monitoring_answer(
    request: AssistantRequest,
    assistant: AssistantResponse,
    evidence: MonitoringSummary,
) -> AssistantResponse:
    """Accept bounded synthesis only when mandatory monitoring qualifiers survive."""

    is_stale = any(metric.stale for metric in evidence.metrics)
    limitations = _evidence_limitations(is_partial=evidence.is_partial, is_stale=is_stale)
    named_target = requested_named_target(request.question)
    if named_target and named_target != evidence_host_role(evidence.host):
        answer = (
            f"وضعیت هدف {named_target} از این شاهد معلوم نیست. این نمای Zabbix در "
            f"{_timestamp(evidence.collected_at)} فقط میزبان {evidence.host} را پوشش می‌دهد، "
            "نه سرور خواسته‌شده. برای شاهد همان سرور، هدف مجاز را در «بررسی رخداد» انتخاب کنید. "
            "نبودِ مشکل در میزبان دیگر، سلامت سرور شما را ثابت نمی‌کند. هیچ تغییری انجام نشد."
            if request.locale == "fa"
            else f"The status of target {named_target} is unknown from this evidence. This Zabbix "
            f"snapshot at {_timestamp(evidence.collected_at)} covers only {evidence.host}, not "
            "the requested server. Select that approved target in Incident investigation. "
            "No problems on a different host do not prove your server healthy. "
            "No change was performed."
        )
        qualifiers = (
            (" شاهد ناقص است." if request.locale == "fa" else " Evidence is partial.")
            if evidence.is_partial
            else ""
        ) + (
            (" برخی سنجه‌ها قدیمی‌اند." if request.locale == "fa" else " Some metrics are stale.")
            if is_stale
            else ""
        )
        return assistant.model_copy(
            update={
                "answer": answer + qualifiers,
                "evidence_mode": "live_zabbix",
                "live_monitoring_data": True,
                "integrity_status": "deterministic_focus",
                "limitations": (*limitations, "requested_target_not_in_evidence"),
            }
        )
    if _MULTI_HOST_QUESTION.search(request.question) and _HOST_AVAILABILITY_QUESTION.search(
        request.question
    ):
        qualifier = (
            (" شاهد ناقص است." if request.locale == "fa" else " Evidence is partial.")
            if evidence.is_partial
            else ""
        )
        if is_stale:
            qualifier += (
                " برخی سنجه‌ها قدیمی‌اند و وضعیت کنونی آن‌ها نامعلوم است."
                if request.locale == "fa"
                else " Some metrics are stale and their current state is unknown."
            )
        answer = (
            f"نمای زبیکس در {_timestamp(evidence.collected_at)} فقط میزبان پیکربندی‌شدهٔ "
            f"{evidence.host} را "
            "پوشش می‌دهد و وضعیت دسترسیِ فهرست میزبان‌های مجاز را ندارد. بنابراین نمی‌توانم "
            f"بگویم کدام میزبان‌ها در دسترس‌اند یا نیستند.{qualifier} هیچ تغییری انجام نشد."
            if request.locale == "fa"
            else f"The Zabbix snapshot at {_timestamp(evidence.collected_at)} covers only "
            f"configured host {evidence.host} and has no reachability states for the authorized "
            "host inventory. I cannot "
            f"identify which hosts are available or unavailable.{qualifier} "
            "No change was performed."
        )
        return assistant.model_copy(
            update={
                "answer": answer,
                "evidence_mode": "live_zabbix",
                "live_monitoring_data": True,
                "integrity_status": "deterministic_focus",
                "limitations": (*limitations, "host_inventory_unavailable"),
            }
        )
    if _SYSTEM_FILE_REQUEST.search(request.question):
        if request.locale == "fa":
            qualification = (
                f" شاهد Zabbix ناقص است ({', '.join(evidence.partial_reasons)})."
                if evidence.is_partial
                else ""
            ) + (" برخی سنجه‌های Zabbix قدیمی‌اند." if is_stale else "")
        else:
            qualification = (
                f" Zabbix evidence is partial ({', '.join(evidence.partial_reasons)})."
                if evidence.is_partial
                else ""
            ) + (" Some Zabbix metrics are stale." if is_stale else "")
        answer = (
            "پایش Zabbix نام یا محتوای فایل‌های سیستم را نمی‌بیند. برای ظرفیت نقاط اتصالِ "
            "مجاز، حالت «بررسی رخداد» را انتخاب کنید؛ آن حالت نیز فایل‌ها را فهرست "
            f"نمی‌کند.{qualification}"
            if request.locale == "fa"
            else "Zabbix monitoring cannot see system file names or contents. Choose Incident "
            "investigation for approved filesystem mount capacity; it cannot list files "
            f"either.{qualification}"
        )
        return assistant.model_copy(
            update={
                "answer": answer,
                "evidence_mode": "live_zabbix",
                "live_monitoring_data": True,
                "integrity_status": "deterministic_focus",
                "limitations": (*limitations, "file_listing_unavailable"),
            }
        )
    if monitoring_cpu_focus(request.question):
        answer, available = _cpu_idle_summary(request.locale, evidence)
        return assistant.model_copy(
            update={
                "answer": answer,
                "evidence_mode": "live_zabbix",
                "live_monitoring_data": True,
                "integrity_status": "deterministic_focus",
                "limitations": (
                    limitations if available else (*limitations, "cpu_idle_percentage_unavailable")
                ),
            }
        )
    safe = (
        _is_safe_evidence_answer(
            assistant.answer,
            require_linux=False,
            is_partial=evidence.is_partial,
            is_stale="stale_evidence" in limitations,
        )
        and assistant.finish_reason == FinishReason.STOP
        and not _is_long_prompt_echo(request.question, assistant.answer)
    )
    return assistant.model_copy(
        update={
            "answer": assistant.answer if safe else _monitoring_fallback(request.locale, evidence),
            "evidence_mode": "live_zabbix",
            "live_monitoring_data": True,
            "integrity_status": "evidence_bounded" if safe else "deterministic_fallback",
            "limitations": limitations,
        }
    )


def assure_incident_answer(
    request: IncidentInvestigationRequest,
    assistant: AssistantResponse,
    evidence: IncidentEvidence,
) -> AssistantResponse:
    """Accept bounded synthesis only when both evidence sources remain explicit."""

    is_stale = any(metric.stale for metric in evidence.zabbix.summary.metrics)
    limitations = _evidence_limitations(is_partial=evidence.is_partial, is_stale=is_stale)
    focus = incident_focus(request.question)
    if focus == "host_status":
        return assistant.model_copy(
            update={
                "answer": _host_status_summary(request.locale, evidence),
                "evidence_mode": "live_zabbix_linux",
                "live_monitoring_data": True,
                "integrity_status": "deterministic_focus",
                "limitations": limitations,
            }
        )
    if focus != "overview":
        # A lexical source check cannot verify whether a generated file name or capacity is real.
        # Render the bounded collector data directly until semantic validation is qualified.
        return assistant.model_copy(
            update={
                "answer": _focused_incident_summary(
                    request.locale, evidence, focus, request.question
                ),
                "evidence_mode": "live_zabbix_linux",
                "live_monitoring_data": True,
                "integrity_status": "deterministic_focus",
                "limitations": (
                    (*limitations, "file_listing_unavailable")
                    if focus == "file_listing"
                    else limitations
                ),
            }
        )
    safe = (
        assistant.finish_reason == FinishReason.STOP
        and not _is_long_prompt_echo(request.question, assistant.answer)
        and _is_safe_evidence_answer(
            assistant.answer,
            require_linux=True,
            is_partial=evidence.is_partial,
            is_stale=is_stale,
        )
        and evidence.target_id.casefold() in assistant.answer.casefold()
    )
    return assistant.model_copy(
        update={
            "answer": assistant.answer if safe else _incident_fallback(request.locale, evidence),
            "evidence_mode": "live_zabbix_linux",
            "live_monitoring_data": True,
            "integrity_status": "evidence_bounded" if safe else "deterministic_fallback",
            "limitations": limitations,
        }
    )


def _host_status_summary(locale: str, evidence: IncidentEvidence) -> str:
    """Observed target facts only: running services are not an application health test."""
    linux = evidence.linux
    states = "; ".join(
        f"{service.unit}={service.active_state}/{service.sub_state}"
        for service in linux.services
        if _safe_service_state(service.active_state) and _safe_service_state(service.sub_state)
    ) or ("وضعیت سرویس دریافت نشد" if locale == "fa" else "no service states collected")
    memory = (
        f"{linux.memory_available_bytes / 1073741824:.1f}/"
        f"{linux.memory_total_bytes / 1073741824:.1f} GiB"
    )
    partial = (
        f" شاهد ناقص است ({', '.join(evidence.partial_reasons)})."
        if locale == "fa" and evidence.is_partial
        else f" Evidence is partial ({', '.join(evidence.partial_reasons)})."
        if evidence.is_partial
        else ""
    )
    stale = (
        " برخی سنجه‌های Zabbix قدیمی‌اند."
        if locale == "fa" and any(m.stale for m in evidence.zabbix.summary.metrics)
        else " Some Zabbix metrics are stale."
        if any(m.stale for m in evidence.zabbix.summary.metrics)
        else ""
    )
    if locale == "fa":
        return (
            f"برای سرورِ هدف {evidence.target_id}، شاهد Linux در {_timestamp(linux.collected_at)} "
            f"این وضعیت را ثبت کرده است: {states}. حافظهٔ در دسترس/کل: {memory}؛ "
            f"بار یک‌دقیقه‌ای: {linux.load_1m:.2f}؛ مدت روشن‌بودن: {linux.uptime_seconds} ثانیه. "
            "فعال‌بودن سرویس، موفقیت تولید پاسخ یا سلامت کامل برنامه را ثابت نمی‌کند. "
            f"دامنهٔ جداگانهٔ Zabbix، میزبان {evidence.zabbix.host} در "
            f"{_timestamp(evidence.zabbix.collected_at)} است؛ دادهٔ میزبان دیگر به این سرور نسبت "
            f"داده نمی‌شود.{partial}{stale} هیچ تغییری انجام نشد."
        )
    return (
        f"For server target {evidence.target_id}, "
        f"Linux at {_timestamp(linux.collected_at)} records "
        f"{states}. Available/total memory: {memory}; one-minute load: {linux.load_1m:.2f}; "
        f"uptime: {linux.uptime_seconds} seconds. Running services alone do not prove successful "
        "generation or full application health. "
        f"The separate Zabbix scope is {evidence.zabbix.host} "
        f"at {_timestamp(evidence.zabbix.collected_at)}; another host's data is not attributed to "
        f"this server.{partial}{stale} No change was performed."
    )


def _cpu_idle_summary(locale: str, evidence: MonitoringSummary) -> tuple[str, bool]:
    """Own the meaning of a reviewed item key; never trust a generated metric label."""

    metrics = tuple(
        metric
        for metric in evidence.metrics
        if metric.key in {"system.cpu.util[,idle]", "system.cpu.util[,idle,avg1]"}
    )
    # Multiple matching items are ambiguous; do not silently choose one observation.
    metric = metrics[0] if len(metrics) == 1 else None
    if metric and not (
        metric.units == "%"
        and re.fullmatch(r"[0-9]{1,3}(?:\.[0-9]{1,16})?", metric.value)
        and Decimal(metric.value) <= 100
    ):
        metric = None
    collected = _timestamp(evidence.collected_at)
    if locale == "fa":
        observation = (
            f"در میزبان {evidence.host}، درصد بیکاری پردازنده (CPU idle) برابر {metric.value}٪ "
            f"در {_timestamp(metric.measured_at)} ثبت شده است؛ این مقدار درصد مصرف CPU نیست. "
            if metric
            else f"برای میزبان {evidence.host}، درصد بیکاری پردازندهٔ معتبر و بدون ابهام "
            "در این شاهد موجود نیست. "
        )
        qualifier = (
            f"شواهد ناقص است ({', '.join(evidence.partial_reasons)}). "
            if evidence.is_partial
            else ""
        )
        freshness = (
            "برخی سنجه‌ها قدیمی‌اند و وضعیت کنونی آن‌ها نامعلوم است. "
            if any(item.stale for item in evidence.metrics)
            else "این مشاهدهٔ ثبت‌شده به‌تنهایی سلامت یا وضعیت همین لحظه را ثابت نمی‌کند. "
        )
        return (
            f"{observation}منبع Zabbix؛ زمان گردآوری {collected}. "
            f"{qualifier}{freshness}هیچ تغییری انجام نشد.",
            metric is not None,
        )
    observation = (
        f"For {evidence.host}, CPU idle was {metric.value}% measured at "
        f"{_timestamp(metric.measured_at)}; this is not CPU utilization. "
        if metric
        else f"For {evidence.host}, no usable, unambiguous CPU-idle percentage is available "
        "in this evidence. "
    )
    qualifier = (
        f"Evidence is partial ({', '.join(evidence.partial_reasons)}). "
        if evidence.is_partial
        else ""
    )
    freshness = (
        "Some metrics are stale and their current state is unknown. "
        if any(item.stale for item in evidence.metrics)
        else "This recorded observation alone does not prove health or the state right now. "
    )
    return (
        f"{observation}Source Zabbix; collected at {collected}. "
        f"{qualifier}{freshness}No change was performed.",
        metric is not None,
    )


def _focused_incident_summary(
    locale: str, evidence: IncidentEvidence, focus: str, question: str
) -> str:
    linux = evidence.linux
    when = _timestamp(linux.collected_at)
    partial_fa = (
        f" شواهد ناقص است ({', '.join(evidence.partial_reasons)})." if evidence.is_partial else ""
    )
    partial_en = (
        f" Evidence is partial ({', '.join(evidence.partial_reasons)})."
        if evidence.is_partial
        else ""
    )
    if focus in {"network", "service", "network_service"}:
        return _observed_incident_summary(locale, evidence, focus, question)
    if focus == "file_listing":
        if locale == "fa":
            return (
                f"گردآورندهٔ فقط‌خواندنی Linux برای میزبان {evidence.target_id} در {when} "
                "فهرست نام یا محتوای فایل‌های سیستم را دریافت نکرده است؛ بنابراین نمی‌توانم "
                "آن فایل‌ها را نشان دهم. فقط ظرفیت نقاط اتصالِ مجاز قابل مشاهده است. "
                f"زمان Zabbix منبعی برای تأیید محتوای فایل نیست.{partial_fa}"
            )
        return (
            f"The read-only Linux collector for {evidence.target_id} at {when} did not retrieve "
            "system file names or contents, so I cannot list them. Only approved filesystem "
            f"mount capacity is available. Zabbix does not verify file contents.{partial_en}"
        )
    mounts = linux.filesystems
    if locale == "fa":
        details = (
            "؛ ".join(
                f"{item.path}: {item.used_percent:g}٪ مصرف، {item.available_bytes} بایت آزاد"
                for item in mounts[:3]
            )
            or "هیچ نقطهٔ اتصال مجازی ثبت نشد"
        )
        remainder = f"؛ {len(mounts) - 3} مورد دیگر در جزئیات شواهد" if len(mounts) > 3 else ""
        return (
            f"برای میزبان {evidence.target_id}، نمای فقط‌خواندنی Linux در {when} "
            f"این ظرفیت فایل‌سیستم‌های مجاز را ثبت کرد: {details}{remainder}.{partial_fa} "
            "این داده‌ها فهرست نام یا محتوای فایل‌های سیستم نیستند."
        )
    details = (
        "; ".join(
            f"{item.path}: {item.used_percent:g}% used, {item.available_bytes} bytes available"
            for item in mounts[:3]
        )
        or "no approved mounts were recorded"
    )
    remainder = f"; {len(mounts) - 3} more in evidence details" if len(mounts) > 3 else ""
    return (
        f"For {evidence.target_id}, the read-only Linux snapshot at {when} recorded only "
        f"approved filesystem capacity: {details}{remainder}.{partial_en} "
        "This does not list system file names or contents."
    )


def _observed_incident_summary(
    locale: str, evidence: IncidentEvidence, focus: str, question: str
) -> str:
    """Render typed observations, not model conjecture, for named service/network questions."""

    linux = evidence.linux
    zabbix = evidence.zabbix
    network = focus in {"network", "network_service"}
    service = focus in {"service", "network_service"}
    details: list[str] = []
    if network:
        wanted = _requested_network_fields(question)
        valid_resolvers = [
            address
            for raw in linux.nameservers[:3]
            if (address := _safe_ip_address(raw)) is not None
        ]
        resolvers = ", ".join(valid_resolvers) or _missing_network_value(
            locale, bool(linux.nameservers)
        )
        valid_routes = [
            _route_description(locale, destination, gateway, item.interface)
            for item in linux.routes[:2]
            if (destination := _safe_ip_destination(item.destination)) is not None
            and (gateway := _safe_ip_address(item.gateway)) is not None
        ]
        routes = "; ".join(valid_routes) or _missing_network_value(locale, bool(linux.routes))
        ordered_sockets = sorted(
            linux.listening_sockets,
            key=lambda item: 0 if re.search(rf"(?<!\d){item.port}(?!\d)", question) else 1,
        )
        valid_sockets = [
            f"{f'[{address}]' if ':' in address else address}:{item.port}/{item.family}"
            for item in ordered_sockets[:3]
            if (address := _safe_ip_address(item.address)) is not None
        ]
        sockets = "; ".join(valid_sockets) or _missing_network_value(
            locale, bool(linux.listening_sockets)
        )
        network_details: list[str] = []
        if "resolvers" in wanted:
            network_details.append(
                f"نام‌سرورهای پیکربندی‌شده: {resolvers}"
                if locale == "fa"
                else f"configured resolvers: {resolvers}"
            )
            if any(ipaddress.ip_address(address).is_loopback for address in valid_resolvers):
                network_details.append(
                    "نشانی محلیِ ثبت‌شده، نام‌سرور بالادستی را مشخص نمی‌کند"
                    if locale == "fa"
                    else "a recorded loopback resolver does not identify its upstream server"
                )
        if "routes" in wanted:
            network_details.append(
                f"مسیرهای ثبت‌شده: {routes}" if locale == "fa" else f"recorded routes: {routes}"
            )
        if "sockets" in wanted:
            network_details.append(
                f"سوکت‌های در حال شنودِ ثبت‌شده: {sockets}"
                if locale == "fa"
                else f"recorded listening sockets: {sockets}"
            )
        details.append(("؛ " if locale == "fa" else "; ").join(network_details))
    if service:
        named_units = requested_service_units(question, (item.unit for item in linux.services))
        selected_services = (
            [item for item in linux.services if item.unit in named_units]
            if named_units is not None
            else list(linux.services[:3])
        )
        states = "; ".join(
            f"{item.unit}={item.active_state}/{item.sub_state}"
            for item in selected_services[:3]
            if _safe_service_state(item.active_state) and _safe_service_state(item.sub_state)
        )
        if named_units is not None and not states:
            service_detail = (
                "وضعیت واحدِ نام‌برده در نمای مجاز ثبت نشده است؛ وضعیت واقعی آن نامعلوم است"
                if locale == "fa"
                else "the named unit has no usable state in the authorized snapshot; "
                "its actual state is unknown"
            )
        else:
            states = states or _missing_network_value(locale, bool(linux.services))
            service_detail = (
                f"وضعیت سرویس‌های ثبت‌شده: {states}"
                if locale == "fa"
                else f"recorded service states: {states}"
            )
        if re.search(r"\b(?:journal|logs?)\b|ژورنال|لاگ|گزارش", question, re.IGNORECASE):
            service_detail += (
                f"؛ {len(linux.journal)} رکورد ژورنالِ مجاز"
                if locale == "fa"
                else f"; {len(linux.journal)} bounded journal record(s)"
            )
        details.append(service_detail)
    partial = (
        f" شاهد ناقص است ({', '.join(evidence.partial_reasons)})."
        if locale == "fa" and evidence.is_partial
        else f" Evidence is partial ({', '.join(evidence.partial_reasons)})."
        if evidence.is_partial
        else ""
    )
    stale_count = sum(metric.stale for metric in zabbix.summary.metrics)
    stale = (
        f" {stale_count} سنجهٔ Zabbix قدیمی است."
        if locale == "fa" and stale_count
        else f" {stale_count} Zabbix metric(s) are stale."
        if stale_count
        else ""
    )
    if locale == "fa":
        qualification = (
            "این مشاهده‌ها به‌تنهایی موفقیت DNS یا دسترسی راه دور را ثابت نمی‌کنند. "
            if network and not service
            else "این وضعیتِ ثبت‌شده به‌تنهایی سلامت سرویس یا رفع خطای پیشین را ثابت نمی‌کند. "
            if service and not network
            else "این مشاهده‌ها به‌تنهایی موفقیت DNS، دسترسی راه دور، سلامت سرویس "
            "یا رفع خطای پیشین را ثابت نمی‌کنند. "
        )
        return (
            f"برای هدف Linux به نام {evidence.target_id}، گردآوریِ {_timestamp(linux.collected_at)} "
            f"این موارد را نشان می‌دهد: {'؛ '.join(details)}. نمای جداگانهٔ Zabbix برای "
            f"{zabbix.host} در {_timestamp(zabbix.collected_at)} گردآوری شده است؛ "
            "یکسان‌بودن این دو میزبان ثابت نشده است. "
            f"{qualification.strip()}{partial}{stale} هیچ تغییری انجام نشد."
        )
    qualification = (
        "These observations alone do not prove DNS success or remote reachability. "
        if network and not service
        else "The recorded state alone does not prove service readiness or recovery. "
        if service and not network
        else "These observations alone do not prove DNS success, remote reachability, "
        "service readiness or recovery. "
    )
    return (
        f"For Linux target {evidence.target_id}, the {_timestamp(linux.collected_at)} snapshot "
        f"shows {'; '.join(details)}. The separate Zabbix scope is {zabbix.host}, collected "
        f"at {_timestamp(zabbix.collected_at)}; these are not proven to be the same host. "
        f"{qualification.strip()}{partial}{stale} No change was performed."
    )


def _requested_network_fields(question: str) -> frozenset[str]:
    resolvers = re.search(
        r"\b(?:dns|resolvers?|nameservers?)\b|نام[‌-]?سرور|دی[‌-]?ان[‌-]?اس", question, re.IGNORECASE
    )
    routes = re.search(r"\b(?:routes?|routing|gateway)\b|مسیر|دروازه", question, re.IGNORECASE)
    sockets = re.search(
        r"\b(?:ports?|sockets?|listen(?:ing)?)\b|پورت|سوکت|شنود", question, re.IGNORECASE
    )
    selected = {
        field
        for field, matched in (("resolvers", resolvers), ("routes", routes), ("sockets", sockets))
        if matched
    }
    return frozenset(selected or {"resolvers", "routes", "sockets"})


def _route_description(locale: str, destination: str, gateway: str, interface: str) -> str:
    if gateway == "0.0.0.0":
        note = "بدون گیت‌وی ثبت‌شده" if locale == "fa" else "no gateway recorded"
        return f"{destination} ({note}; {interface})"
    if locale == "fa":
        return f"{destination} از طریق {gateway} ({interface})"
    return f"{destination} via {gateway} ({interface})"


def _safe_ip_address(raw: str) -> str | None:
    try:
        return str(ipaddress.ip_address(raw))
    except ValueError:
        return None


def _safe_ip_destination(raw: str) -> str | None:
    address = _safe_ip_address(raw)
    if address is not None:
        return address
    try:
        return str(ipaddress.ip_network(raw, strict=False))
    except ValueError:
        return None


def _safe_service_state(raw: str) -> bool:
    return re.fullmatch(r"[a-z][a-z-]{0,31}", raw) is not None


def _missing_network_value(locale: str, had_values: bool) -> str:
    if locale == "fa":
        return "دادهٔ قابل‌استفاده ثبت نشد" if had_values else "ثبت نشده"
    return "no usable recorded value" if had_values else "none recorded"


def _contains_unsafe_execution_claim(answer: str) -> bool:
    return any(pattern.search(answer) for pattern in _UNSAFE_EXECUTION_CLAIMS)


def _is_long_prompt_echo(question: str, answer: str) -> bool:
    normalized_question = " ".join(question.casefold().split())
    normalized_answer = " ".join(answer.casefold().split())
    return len(normalized_question) >= 40 and normalized_answer == normalized_question


def _is_safe_evidence_answer(
    answer: str,
    *,
    require_linux: bool,
    is_partial: bool,
    is_stale: bool,
) -> bool:
    if _contains_unsafe_execution_claim(answer):
        return False
    if _PROMPT_BOUNDARY_LEAK.search(answer):
        return False
    if any(pattern.search(answer) for pattern in _UNSUPPORTED_CAUSE_CLAIMS):
        return False
    if not _ZABBIX_DISCLOSURE.search(answer):
        return False
    if require_linux and not _LINUX_DISCLOSURE.search(answer):
        return False
    if is_partial and not _PARTIAL_DISCLOSURE.search(answer):
        return False
    return not (is_stale and not _STALE_DISCLOSURE.search(answer))


def _evidence_limitations(*, is_partial: bool, is_stale: bool) -> tuple[str, ...]:
    values = ["read_only_no_action_performed"]
    if is_stale:
        values.append("stale_evidence")
    if is_partial:
        values.append("partial_evidence")
    return tuple(values)


def _monitoring_fallback(locale: str, evidence: MonitoringSummary) -> str:
    partial = ", ".join(evidence.partial_reasons)
    stale_count = sum(metric.stale for metric in evidence.metrics)
    if locale == "fa":
        qualification = (
            f"شاهد ناقص است ({partial}). "
            if evidence.is_partial
            else "شاهد با برچسب کامل دریافت شد. "
        )
        freshness = (
            f"{stale_count} سنجه قدیمی است و وضعیت فعلی آن نامعلوم است. "
            if stale_count
            else "سنجهٔ قدیمی علامت‌گذاری نشده است. "
        )
        return (
            "پاسخ کامل و قابل‌اتکایی به پرسش شما تولید نشد. "
            f"دادهٔ ثبت‌شدهٔ Zabbix در {_timestamp(evidence.collected_at)} "
            f"شامل {len(evidence.active_problems)} مشکل فعال و {len(evidence.metrics)} سنجه است. "
            f"{qualification}{freshness}از این نمای ثبت‌شده نمی‌توان علت ریشه‌ای، بازیابی یا انجام‌شدن "
            "هیچ تغییری را نتیجه گرفت. برای پاسخ به پرسش اصلی، جزئیات بخش شواهد را بررسی کنید."
        )
    qualification = (
        f"Evidence is partial ({partial}). "
        if evidence.is_partial
        else "Evidence is marked complete. "
    )
    freshness = (
        f"{stale_count} metric(s) are stale and their current state is unknown. "
        if stale_count
        else "No metric is marked stale. "
    )
    return (
        "A complete, reliable answer to your question was not produced. "
        f"The observed Zabbix snapshot collected at {_timestamp(evidence.collected_at)} contains "
        f"{len(evidence.active_problems)} active problem(s) and {len(evidence.metrics)} metric(s). "
        f"{qualification}{freshness}This snapshot does not establish a root cause, recovery, or "
        "any performed change. Review the attributable details in the evidence panel."
    )


def _incident_fallback(locale: str, evidence: IncidentEvidence) -> str:
    zabbix = evidence.zabbix
    linux = evidence.linux
    stale_count = sum(metric.stale for metric in zabbix.summary.metrics)
    partial = ", ".join(evidence.partial_reasons)
    service_states = "; ".join(
        f"{service.unit}={service.active_state}/{service.sub_state}" for service in linux.services
    ) or (
        "no bounded service records"
        if locale == "en"
        else "رکورد محدودشده‌ای برای سرویس‌ها دریافت نشد"
    )
    if locale == "fa":
        qualifier = (
            f"شاهد ناقص است ({partial}). "
            if evidence.is_partial
            else "شاهد با برچسب کامل دریافت شد. "
        )
        stale = (
            f"{stale_count} سنجهٔ Zabbix قدیمی است و وضعیت فعلی آن نامعلوم است. "
            if stale_count
            else "سنجهٔ قدیمی Zabbix علامت‌گذاری نشده است. "
        )
        return (
            "پاسخ کامل و قابل‌اتکایی به پرسش شما تولید نشد. "
            f"دادهٔ ثبت‌شده برای هدف {evidence.target_id}: نمای زبیکس در "
            f"{_timestamp(zabbix.collected_at)} شامل {len(zabbix.events)} رخداد و "
            f"{len(zabbix.summary.active_problems)} مشکل فعال است. نمای لینوکس در "
            f"{_timestamp(linux.collected_at)} بارهای {linux.load_1m:.2f}/{linux.load_5m:.2f}/"
            f"{linux.load_15m:.2f} و وضعیت سرویس‌های «{service_states}» را ثبت کرده است. "
            f"{qualifier}{stale}این داده‌ها علت ریشه‌ای، بازیابی یا اجرای تغییر را اثبات نمی‌کنند."
        )
    qualifier = (
        f"Evidence is partial ({partial}). "
        if evidence.is_partial
        else "Evidence is marked complete. "
    )
    stale = (
        f"{stale_count} Zabbix metric(s) are stale and their current state is unknown. "
        if stale_count
        else "No Zabbix metric is marked stale. "
    )
    return (
        "A complete, reliable answer to your question was not produced. "
        f"The observed snapshot for target {evidence.target_id}: Zabbix at "
        f"{_timestamp(zabbix.collected_at)} contains {len(zabbix.events)} event(s) and "
        f"{len(zabbix.summary.active_problems)} active problem(s). The Linux snapshot at "
        f"{_timestamp(linux.collected_at)} records load {linux.load_1m:.2f}/{linux.load_5m:.2f}/"
        f"{linux.load_15m:.2f} and service states {service_states}. "
        f"{qualifier}{stale}These observations do not prove a root cause, recovery, or "
        "executed change."
    )


def _timestamp(value: datetime) -> str:
    return value.isoformat().replace("+00:00", "Z")
