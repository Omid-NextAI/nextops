"""Deterministic question focus for bounded, read-only incident explanations."""

# Intentional Persian patterns contain characters flagged as confusable by Ruff.
# ruff: noqa: RUF001

from __future__ import annotations

import re
from typing import Literal

IncidentFocus = Literal["overview", "filesystems", "file_listing"]

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
    filesystem_requested = bool(_FILESYSTEM.search(requested))
    file_requested = bool(_FILES.search(requested))
    if file_requested and not filesystem_requested and _FILE_ACTION.search(requested):
        return "file_listing"
    if _OTHER.search(_EXCLUDED_OTHER.sub("", requested)):
        return "overview"
    if filesystem_requested:
        return "filesystems"
    if file_requested:
        return "file_listing"
    return "overview"
