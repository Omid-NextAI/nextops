"""Real gateway serialization keeps application-owned purpose off the browser contract."""

import asyncio
from datetime import UTC, datetime
from typing import Any
from uuid import uuid4

import pytest

from nextops.api.inference_gateway import LoopbackInferenceGateway
from nextops.contracts.assistant import SynthesisRequest
from nextops.inference.contracts import GenerationPurpose, ModelId


class CapturingTransport:
    def __init__(self, model_id: ModelId = "nextops-qwen3-14b-q4-k-m") -> None:
        self.payload: dict[str, Any] = {}
        self.model_id = model_id
        self.deadlines: dict[str, float] = {}

    async def get_json(
        self, path: str, headers: dict[str, str], timeout_seconds: float
    ) -> dict[str, Any]:
        assert path == "/readyz"
        assert "Authorization" not in headers
        self.deadlines[path] = timeout_seconds
        return {
            "state": "ready",
            "model_id": self.model_id,
            "runtime_version": "v0.4.1",
            "cpu_only_required": True,
            "max_active_requests": 1,
            "max_queued_requests": 2,
            "active_requests": 0,
            "queued_requests": 0,
        }

    async def post_json(
        self,
        path: str,
        payload: dict[str, Any],
        headers: dict[str, str],
        timeout_seconds: float,
    ) -> dict[str, Any]:
        assert path == "/api/v1/generate"
        self.deadlines[path] = timeout_seconds
        self.payload = payload
        now = datetime.now(UTC).isoformat()
        return {
            "request_id": payload["request_id"],
            "correlation_id": headers["X-Correlation-ID"],
            "locale": payload["locale"],
            "answer": "A bounded local answer.",
            "model_id": self.model_id,
            "prompt_tokens": 10,
            "completion_tokens": 8,
            "finish_reason": "stop",
            "started_at": now,
            "completed_at": now,
            "queue_ms": 0,
            "cpu_only_required": True,
        }


@pytest.mark.parametrize("purpose", ["general", "evidence_synthesis"])
@pytest.mark.parametrize(
    "model_id",
    [
        "nextops-qwen3-14b-q4-k-m",
        "nextops-qwen3-32b-q4-k-m",
        "nextops-qwen3-30b-a3b-q4-k-m",
        "nextops-qwen3-5-35b-a3b-q4-k-m",
    ],
)
def test_gateway_serializes_trusted_purpose_and_preserves_exact_model(
    purpose: GenerationPurpose,
    model_id: ModelId,
) -> None:
    async def scenario() -> None:
        transport = CapturingTransport(model_id)
        gateway = LoopbackInferenceGateway("http://127.0.0.1:8090", "s" * 32, 120, transport)
        request = SynthesisRequest(locale="en", question="q" * 5000, purpose=purpose)
        response = await gateway.generate(request, uuid4())
        assert transport.payload["purpose"] == purpose
        assert transport.payload["prompt"] == request.question
        assert response.model_id == model_id
        assert "purpose" not in response.model_dump()
        assert response.evidence_mode == "model_only"
        assert response.live_monitoring_data is False

    asyncio.run(scenario())


def test_long_response_gateway_keeps_health_short_and_identity_checked() -> None:
    async def scenario() -> None:
        transport = CapturingTransport("nextops-qwen3-8-27b-ud-q5-k-m")
        gateway = LoopbackInferenceGateway("http://127.0.0.1:8090", "s" * 32, 330, transport)
        assert (await gateway.readiness()).max_active_requests == 1
        response = await gateway.generate(SynthesisRequest(locale="fa", question="سلام"), uuid4())
        assert response.model_id == transport.model_id
        assert transport.deadlines == {"/readyz": 5.0, "/api/v1/generate": 330}
        assert "Authorization" not in transport.payload

    asyncio.run(scenario())
