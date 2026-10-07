"""Fail-closed reconciliation for the pinned single-slot CPU server.

/health is liveness, not idleness. The protected native profile exposes authenticated
/metrics and disables /slots. No generation is retried by this guard.
"""

import asyncio
import re
from typing import Protocol

from nextops.application.errors import ApplicationError
from nextops.contracts.errors import ErrorCode

IDLE_POLL_SECONDS = 1.1  # Longer than the pinned server's one-second disconnect poll.
_GAUGES = ("llamacpp:requests_processing", "llamacpp:requests_deferred")
MAX_METRICS_BYTES = 65_536


class MetricsTransport(Protocol):
    async def get_text(self, path: str, headers: dict[str, str], timeout_seconds: float) -> str: ...


def native_counts(text: str) -> tuple[int, int]:
    """Require exactly one unlabeled finite integer sample for both gauges."""
    if len(text.encode("utf-8")) > MAX_METRICS_BYTES:
        raise ValueError("oversized metrics")
    values: dict[str, int] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        for name in _GAUGES:
            if line.startswith(name) and (len(line) == len(name) or line[len(name)] in "{ \t"):
                matched = re.fullmatch(re.escape(name) + r"[ \t]+([0-9]+)", line)
                if matched is None or name in values:
                    raise ValueError("ambiguous native gauge")
                values[name] = int(matched[1])
    if set(values) != set(_GAUGES):
        raise ValueError("missing native gauge")
    return values[_GAUGES[0]], values[_GAUGES[1]]


class NativeIdleGuard:
    """Reconcile startup/abnormal exits before any subsequent native dispatch."""

    def __init__(self, transport: MetricsTransport, headers: dict[str, str]) -> None:
        self._transport = transport
        self._headers = {**headers, "Accept": "text/plain"}
        self._lock = asyncio.Lock()
        self.required = True

    async def reconcile(self) -> None:
        async with self._lock:
            if not self.required:
                return
            try:
                for observation in range(2):
                    raw = await self._transport.get_text("/metrics", self._headers, 5.0)
                    if native_counts(raw) != (0, 0):
                        raise ValueError("native work remains")
                    if observation == 0:
                        await asyncio.sleep(IDLE_POLL_SECONDS)
            except (ApplicationError, ValueError, UnicodeError) as error:
                raise ApplicationError(
                    ErrorCode.DEPENDENCY_UNAVAILABLE,
                    "inference.native_not_idle",
                    retryable=True,
                ) from error
            self.required = False
