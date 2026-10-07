"""Native ownership and reconciliation regressions; no real model or credentials."""

import asyncio
import threading
from typing import Any

import pytest
from test_inference_scheduler import ControlledProvider, _request
from test_llama_cpp_provider import StubTransport, _settings

from nextops.application.errors import ApplicationError
from nextops.contracts.errors import ErrorCode
from nextops.inference.llama_cpp import LlamaCppProvider, UrllibJsonTransport
from nextops.inference.native_idle import NativeIdleGuard, native_counts
from nextops.inference.scheduler import BoundedInferenceService, SchedulerLimits

IDLE = "llamacpp:requests_processing 0\nllamacpp:requests_deferred 0\n"


@pytest.mark.parametrize(
    "metrics",
    [
        "",
        "llamacpp:requests_processing 0\n",
        IDLE + "llamacpp:requests_processing 0\n",
        IDLE.replace("processing 0", 'processing{slot="0"} 0'),
        IDLE.replace("processing 0", "processing NaN"),
        IDLE.replace("processing 0", "processing Inf"),
        IDLE.replace("processing 0", "processing -1"),
        IDLE.replace("processing 0", "processing 0.5"),
        IDLE.replace("processing 0", "processing 0 1234"),
        pytest.param(IDLE + "x" * 65_536, id="oversized"),
    ],
)
def test_ambiguous_metrics_cannot_prove_idle(metrics: str) -> None:
    with pytest.raises(ValueError):
        native_counts(metrics)


def test_metrics_counts_are_exact_not_health_or_similar_names() -> None:
    metrics = "# HELP example\n" + IDLE + "llamacpp:requests_processing_total 9"
    assert native_counts(metrics) == (0, 0)
    assert native_counts(IDLE.replace("processing 0", "processing 1")) == (1, 0)


class MetricsFixture:
    def __init__(self, values: list[str]) -> None:
        self.values = values
        self.calls = 0

    async def get_text(self, path: str, headers: dict[str, str], timeout_seconds: float) -> str:
        assert path == "/metrics" and headers["Accept"] == "text/plain"
        assert timeout_seconds == 5.0
        value = self.values[min(self.calls, len(self.values) - 1)]
        self.calls += 1
        return value


@pytest.mark.parametrize("bad", ["", IDLE.replace("deferred 0", "deferred 1")])
def test_startup_requires_two_fresh_idle_observations(
    monkeypatch: pytest.MonkeyPatch, bad: str
) -> None:
    monkeypatch.setattr("nextops.inference.native_idle.IDLE_POLL_SECONDS", 0.001)

    async def scenario() -> None:
        transport = MetricsFixture([IDLE, bad])
        guard = NativeIdleGuard(transport, {"Authorization": "Bearer test-only"})
        with pytest.raises(ApplicationError, match=r"inference\.native_not_idle"):
            await guard.reconcile()
        assert guard.required and transport.calls == 2
        transport.values = [IDLE]
        await guard.reconcile()
        assert not guard.required and transport.calls == 4

    asyncio.run(scenario())


def test_post_failure_requires_reconciliation_before_any_future_generation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("nextops.inference.native_idle.IDLE_POLL_SECONDS", 0.001)

    class AmbiguousTransport(StubTransport):
        busy = False
        posts = 0

        async def get_text(self, path: str, headers: dict[str, str], timeout_seconds: float) -> str:
            return IDLE.replace("processing 0", "processing 1") if self.busy else IDLE

        async def post_json(
            self,
            path: str,
            payload: dict[str, Any],
            headers: dict[str, str],
            timeout_seconds: float,
        ) -> dict[str, Any]:
            self.posts += 1
            self.busy = True
            raise ApplicationError(
                ErrorCode.DEPENDENCY_UNAVAILABLE, "inference.provider_unavailable"
            )

    async def scenario() -> None:
        transport = AmbiguousTransport()
        provider = LlamaCppProvider(_settings(), transport)
        with pytest.raises(ApplicationError):
            await provider.generate(_request())
        with pytest.raises(ApplicationError, match=r"inference\.native_not_idle"):
            await provider.generate(_request())
        assert transport.posts == 1
        assert (await provider.readiness()).state.value == "unavailable"

    asyncio.run(scenario())


def test_cancelled_urllib_coroutine_owns_physical_thread_even_after_second_cancel() -> None:
    started, release = threading.Event(), threading.Event()

    class BlockingTransport(UrllibJsonTransport):
        def _request(
            self,
            method: str,
            path: str,
            body: bytes | None,
            headers: dict[str, str],
            timeout_seconds: float,
        ) -> dict[str, Any]:
            started.set()
            assert release.wait(5), "test must release physical request"
            return {"finished": True}

    async def scenario() -> None:
        transport = BlockingTransport("http://127.0.0.1:8090")
        task = asyncio.create_task(transport.post_json("/v1/chat/completions", {}, {}, 1))
        try:
            assert await asyncio.to_thread(started.wait, 2)
            task.cancel()
            await asyncio.sleep(0)
            task.cancel()
            await asyncio.sleep(0)
            assert not task.done()
        finally:
            release.set()
        with pytest.raises(asyncio.CancelledError):
            await task

    asyncio.run(scenario())


def test_abandoned_owner_keeps_one_active_two_queued_bound_until_finish() -> None:
    async def scenario() -> None:
        provider = ControlledProvider()
        service = BoundedInferenceService(
            provider, SchedulerLimits(queue_timeout_seconds=1, provider_timeout_seconds=1)
        )
        caller = asyncio.create_task(service.generate(_request()))
        await provider.started.wait()
        caller.cancel()
        with pytest.raises(asyncio.CancelledError):
            await caller
        waiters = [asyncio.create_task(service.generate(_request())) for _ in range(2)]
        await asyncio.sleep(0)
        with pytest.raises(ApplicationError, match=r"inference\.capacity_exhausted"):
            await service.generate(_request())
        waiters[0].cancel()
        with pytest.raises(asyncio.CancelledError):
            await waiters[0]
        state = await service.readiness()
        assert state.active_requests == 1 and state.queued_requests == 1
        assert state.state.value == "degraded"
        provider.release.set()
        await waiters[1]
        await asyncio.sleep(0)
        state = await service.readiness()
        assert state.active_requests == state.queued_requests == 0
        assert state.state.value == "ready"

    asyncio.run(scenario())


def test_provider_exception_releases_owned_admission_and_is_observed() -> None:
    class FailingProvider(ControlledProvider):
        async def generate(self, request: Any) -> Any:
            raise ValueError("synthetic provider failure")

    async def scenario() -> None:
        service = BoundedInferenceService(FailingProvider())
        for _ in range(2):
            with pytest.raises(ValueError, match="synthetic provider failure"):
                await service.generate(_request())
            state = await service.readiness()
            assert state.active_requests == state.queued_requests == 0

    asyncio.run(scenario())


@pytest.mark.parametrize("mode", ["timeout", "cancel"])
def test_complete_provider_transport_chain_never_overlaps_physical_workers(
    monkeypatch: pytest.MonkeyPatch, mode: str
) -> None:
    monkeypatch.setattr("nextops.inference.native_idle.IDLE_POLL_SECONDS", 0.001)

    class PhysicalTransport(UrllibJsonTransport):
        def __init__(self) -> None:
            super().__init__("http://127.0.0.1:8090")
            self.started, self.release = threading.Event(), threading.Event()
            self.lock = threading.Lock()
            self.posts = self.active = self.peak = 0

        def _request(
            self,
            method: str,
            path: str,
            body: bytes | None,
            headers: dict[str, str],
            timeout_seconds: float,
        ) -> dict[str, Any]:
            if path == "/metrics":
                return {"_metrics_text": IDLE}
            if path == "/health":
                return {"status": "ok"}
            assert method == "POST" and path == "/v1/chat/completions"
            with self.lock:
                self.posts += 1
                self.active += 1
                self.peak = max(self.peak, self.active)
                first = self.posts == 1
            try:
                if first:
                    self.started.set()
                    assert self.release.wait(5)
                return StubTransport().generation
            finally:
                with self.lock:
                    self.active -= 1

    async def scenario() -> None:
        transport = PhysicalTransport()
        service = BoundedInferenceService(
            LlamaCppProvider(_settings(), transport),
            SchedulerLimits(queue_timeout_seconds=1, provider_timeout_seconds=0.05),
        )
        caller = asyncio.create_task(service.generate(_request()))
        try:
            assert await asyncio.to_thread(transport.started.wait, 2)
            if mode == "cancel":
                caller.cancel()
                with pytest.raises(asyncio.CancelledError):
                    await caller
            else:
                with pytest.raises(ApplicationError, match=r"inference\.provider_timeout"):
                    await caller
            state = await service.readiness()
            assert state.active_requests == 1 and state.state.value == "degraded"
            waiter = asyncio.create_task(service.generate(_request()))
            await asyncio.sleep(0.01)
            assert transport.active == transport.posts == transport.peak == 1
            transport.release.set()
            await waiter
            await asyncio.sleep(0)
            state = await service.readiness()
            assert state.active_requests == state.queued_requests == 0
            assert transport.peak == 1 and state.state.value == "ready"
        finally:
            transport.release.set()
            await asyncio.gather(*service._generations, return_exceptions=True)

    asyncio.run(scenario())
