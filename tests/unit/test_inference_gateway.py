"""Real gateway serialization keeps application-owned purpose off the browser contract."""

import asyncio
from datetime import UTC, datetime
from typing import Any
from uuid import uuid4

import pytest

from nextops.api.inference_gateway import LoopbackInferenceGateway
from nextops.contracts.assistant import SynthesisRequest
from nextops.inference.contracts import GenerationPurpose


class CapturingTransport:
    def __init__(self) -> None:
        self.payload: dict[str, Any] = {}

    async def get_json(
        self, path: str, headers: dict[str, str], timeout_seconds: float
    ) -> dict[str, Any]:
        raise AssertionError("Readiness is not part of this serialization test")

    async def post_json(
        self,
        path: str,
        payload: dict[str, Any],
        headers: dict[str, str],
        timeout_seconds: float,
    ) -> dict[str, Any]:
        assert path == "/api/v1/generate"
        self.payload = payload
        now = datetime.now(UTC).isoformat()
        return {
            "request_id": payload["request_id"],
            "correlation_id": headers["X-Correlation-ID"],
            "locale": payload["locale"],
            "answer": "A bounded local answer.",
            "model_id": "nextops-qwen3-14b-q4-k-m",
            "prompt_tokens": 10,
            "completion_tokens": 8,
            "finish_reason": "stop",
            "started_at": now,
            "completed_at": now,
            "queue_ms": 0,
            "cpu_only_required": True,
        }


@pytest.mark.parametrize("purpose", ["general", "evidence_synthesis"])
def test_gateway_serializes_trusted_purpose_and_preserves_exact_model(
    purpose: GenerationPurpose,
) -> None:
    async def scenario() -> None:
        transport = CapturingTransport()
        gateway = LoopbackInferenceGateway("http://127.0.0.1:8090", "s" * 32, 120, transport)
        request = SynthesisRequest(locale="en", question="q" * 5000, purpose=purpose)
        response = await gateway.generate(request, uuid4())
        assert transport.payload["purpose"] == purpose
        assert transport.payload["prompt"] == request.question
        assert response.model_id == "nextops-qwen3-14b-q4-k-m"
        assert "purpose" not in response.model_dump()
        assert response.evidence_mode == "model_only"
        assert response.live_monitoring_data is False

    asyncio.run(scenario())
