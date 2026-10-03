"""Question targeting is presentation intent, never infrastructure authorization."""

from __future__ import annotations

import re

_ROLE_ALIASES = {
    "ai": r"ai|هوش\s*مصنوعی",
    "app": r"app|application|برنامه",
    "connector": r"connectors?|کانکتور|اتصال",
    "zabbix": r"zabbix|زبیکس",
}
_STATUS = re.compile(
    r"\b(?:status|state|health|current|latest|now)\b|وضعیت|سلامت|فعلی|آخرین|الان", re.I
)
_EXPLANATION = re.compile(
    r"\b(?:why|explain|mean(?:ing|s)?|compare|difference|how)\b|"
    r"چرا|توضیح|معنی|معنا|مقایسه|تفاوت|چطور|چگونه",
    re.I,
)
_OTHER_TOPIC = re.compile(
    r"\b(?:cpu|ram|memory|disk|file(?:s|systems?)?|network|dns|ports?|logs?|journal|services?)\b|"
    r"پردازنده|حافظه|دیسک|فایل|شبکه|پورت|لاگ|ژورنال|سرویس",
    re.I,
)


def requested_named_target(question: str) -> str | None:
    """Only one explicitly named known role; never guess from a generic AI topic."""
    matches = {
        role
        for role, aliases in _ROLE_ALIASES.items()
        if re.search(
            rf"(?<![\w@.-])(?:nextops-{role}(?![\w@.-])|"
            rf"(?:server|host|vm|سرور|میزبان)\s+(?:{aliases})|"
            rf"(?:{aliases})\s+(?:server|host|vm|سرور|میزبان))(?![\w-])",
            question,
            re.I,
        )
    }
    return next(iter(matches)) if len(matches) == 1 else None


def named_host_status(question: str) -> str | None:
    """A narrow observed-status request, not guidance or another requested topic."""
    if (
        _EXPLANATION.search(question)
        or _OTHER_TOPIC.search(question)
        or not _STATUS.search(question)
    ):
        return None
    return requested_named_target(question)


def evidence_host_role(host: str) -> str | None:
    """Display mismatch detection only; a host label cannot grant credentials/scope."""
    normalized = host.strip().casefold()
    for role, aliases in _ROLE_ALIASES.items():
        if re.fullmatch(rf"(?:nextops[ -])?(?:{aliases})(?:[ -](?:server|host|vm))?", normalized):
            return role
    return None
