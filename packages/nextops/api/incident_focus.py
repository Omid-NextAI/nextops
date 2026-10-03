"""Deterministic question focus for bounded, read-only incident explanations."""

# Intentional Persian patterns contain characters flagged as confusable by Ruff.
# ruff: noqa: RUF001

from __future__ import annotations

import re
from collections.abc import Iterable
from typing import Literal

from nextops.api.target_focus import named_host_status

IncidentFocus = Literal[
    "overview",
    "filesystems",
    "file_listing",
    "network",
    "service",
    "network_service",
    "host_status",
]

_NAMED_UNIT = re.compile(
    r"(?<![\w@.-])([A-Za-z0-9_@.-]+\.(?:service|socket|timer))(?![\w@.-])",
    re.IGNORECASE,
)


def requested_service_units(
    question: str, available_units: Iterable[str]
) -> tuple[str, ...] | None:
    """Return explicitly named authorized units, or None for a broad service question.

    An unknown named unit yields an empty tuple; it must not cause unrelated
    service observations to be presented as the answer.
    """

    named = {match.casefold() for match in _NAMED_UNIT.findall(question)}
    if not named:
        return None
    return tuple(unit for unit in available_units if unit.casefold() in named)


_NON_NETWORK_SERVICE_TOPIC = re.compile(
    r"(?:\b(?:cpu|memory|ram|files?|filesystems?|disks?|storage|zabbix|metrics?|"
    r"problems?|events?|everything|all\s+data)\b|"
    r"پردازنده|حافظه|فایل|دیسک|زبیکس|سنجه|مشکل|رویداد|همه[ٔ‌ ]?\s*داده)",
    re.IGNORECASE,
)

_FILESYSTEM = re.compile(
    r"(?:\b(?:filesystems?|file\s+systems?|disk\s+(?:space|usage)|mounts?|"
    r"storage\s+(?:space|usage))\b|فایل[‌ ]?سیستم|سامانه[‌ ]?فایل|فضای\s*دیسک|"
    r"پارتیشن|نقطه[‌ ]?اتصال)",
    re.IGNORECASE,
)
_FILES = re.compile(
    r"(?:\b(?:files?|directories|directory|folders?)\b|/(?:etc|var|usr)(?:/|\b)|"
    r"فایل[‌ ]?ها|پرونده[‌ ]?ها|پوشه[‌ ]?ها|فایل[‌ ]?های\s*سیستم)",
    re.IGNORECASE,
)
_OTHER = re.compile(
    r"(?:\b(?:services?|cpu|memory|ram|events?|journal|processes?|network|"
    r"problems?|everything|all\s+data|zabbix)\b|سرویس|پردازنده|حافظه|رویداد|فرایند|"
    r"شبکه|زبیکس|همه[ٔ‌ ]?\s*داده)",
    re.IGNORECASE,
)
_FILE_ACTION = re.compile(
    r"(?:\b(?:show(?:ing)?|list(?:ing)?|display(?:ing)?|find(?:ing)?|"
    r"read(?:ing)?|open(?:ing)?)\b|نشان|نمایش|فهرست|بخوان|باز\s*کن)",
    re.IGNORECASE,
)
_EXCLUDED_OTHER = re.compile(
    r"(?:\b(?:no|not|without|exclude|excluding)\s+(?:any\s+|the\s+)?"
    r"(?:services?|cpu|memory|ram|events?|journal|processes?|network|problems?)\b|"
    r"بدون\s*(?:سرویس|پردازنده|حافظه|رویداد|فرایند|شبکه))",
    re.IGNORECASE,
)
_EN_NEGATED_ACTION = re.compile(
    r"\b(?:do\s+not|don't|dont)\s+(?:include|show|list|display|report|summarize|add)\b",
    re.IGNORECASE,
)
_FA_NEGATED_ACTION = re.compile(r"(?:اضافه\s*نکن|نشان\s*نده|گزارش\s*نکن)")
_FA_POSITIVE_ACTION = re.compile(r"(?:نشان\s*بده|نمایش\s*بده|فهرست\s*کن|گزارش\s*کن)")
_CPU_TOPIC = re.compile(r"(?:\bcpu\b|\bprocessor\b|پردازنده)", re.IGNORECASE)
_CPU_OBSERVATION = re.compile(
    r"(?:\b(?:measurements?|readings?|idle)\b|اندازه[‌ ]گیری|مشاهده|بیکاری)",
    re.IGNORECASE,
)
_OTHER_CPU_TOPIC = re.compile(
    r"(?:\b(?:memory|ram|disk|storage|files?|filesystems?|services?|events?|problems?|"
    r"network|everything|history|trend|peak|average|cause|why|restart|reboot|explain|"
    r"meaning|means)\b|"
    r"حافظه|دیسک|فایل|سرویس|رویداد|مشکل|شبکه|همه|تاریخچه|روند|بیشینه|میانگین|"
    r"علت|چرا|توضیح|معنی|معنا|راه[‌ ]اندازی\s*مجدد)",
    re.IGNORECASE,
)


def monitoring_cpu_focus(question: str) -> bool:
    """Narrow an unambiguous CPU observation request; never authorize collection."""

    requested = _EXCLUDED_OTHER.sub("", _requested_text(question))
    return bool(
        _CPU_TOPIC.search(requested)
        and _CPU_OBSERVATION.search(requested)
        and not _OTHER_CPU_TOPIC.search(requested)
    )


def _requested_text(question: str) -> str:
    """Remove explicit exclusion clauses, never interpreting them as requested topics."""

    requested: list[str] = []
    for sentence in re.split(r"[.!?؟؛]+", question):
        english_exclusion = _EN_NEGATED_ACTION.search(sentence)
        if english_exclusion:
            sentence = sentence[: english_exclusion.start()]
        persian_exclusion = _FA_NEGATED_ACTION.search(sentence)
        if persian_exclusion:
            positive_actions = tuple(
                _FA_POSITIVE_ACTION.finditer(sentence[: persian_exclusion.start()])
            )
            sentence = sentence[: positive_actions[-1].end()] if positive_actions else ""
        requested.append(sentence)
    return " ".join(requested)


def incident_focus(question: str) -> IncidentFocus:
    """Narrow only an unambiguous single-topic request; never grant new access."""

    requested = _requested_text(question)
    if named_host_status(requested):
        return "host_status"
    filesystem_requested = bool(_FILESYSTEM.search(requested))
    file_requested = bool(_FILES.search(requested))
    if file_requested and not filesystem_requested and _FILE_ACTION.search(requested):
        return "file_listing"
    if (filesystem_requested or file_requested) and _OTHER.search(
        _EXCLUDED_OTHER.sub("", requested)
    ):
        return "overview"
    if filesystem_requested:
        return "filesystems"
    if file_requested:
        return "file_listing"
    if not _NON_NETWORK_SERVICE_TOPIC.search(requested):
        return incident_evidence_topic(requested)
    return "overview"


def incident_evidence_topic(question: str) -> IncidentFocus:
    """Select a bounded prompt/answer topic, never authorize evidence collection."""

    requested = _requested_text(question)
    network = bool(
        re.search(
            r"\b(?:network|dns|resolver|nameserver|routing|routes?|sockets?|listen(?:ing)?|"
            r"ports?|firewall|vpn)\b",
            requested,
            re.IGNORECASE,
        )
    ) or any(
        word in requested
        for word in (
            "شبکه",
            "مسیر",
            "فایروال",
            "پورت",
            "شنود",
            "سوکت",
            "اتصال",
            "وی‌پی‌ان",
            "نام‌سرور",
        )
    )
    services = bool(
        re.search(
            r"\b(?:services?|systemd|units?|journals?|logs?|daemons?)\b",
            requested,
            re.IGNORECASE,
        )
    ) or any(word in requested for word in ("سرویس", "خدمت", "واحد", "ژورنال", "گزارش", "لاگ"))
    if network and services:
        return "network_service"
    if network:
        return "network"
    if services:
        return "service"
    return "overview"
