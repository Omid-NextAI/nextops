"""Framework-free source-read orchestration with mandatory authorization/audit ports."""

from __future__ import annotations

import asyncio
import hashlib
import json
from collections.abc import Callable
from datetime import UTC, datetime
from typing import Literal, Protocol
from uuid import UUID, uuid4

from anyio import CancelScope
from pydantic import AwareDatetime, Field, model_validator

from nextops.application.errors import ApplicationError
from nextops.connectors.sources import (
    ScopedZabbixTransport,
    ZabbixSource,
    ZabbixSourceRegistry,
    ZabbixSourceTarget,
)
from nextops.connectors.zabbix import ZabbixReadClient, ZabbixTransport
from nextops.contracts.errors import ErrorCode
from nextops.contracts.models import ActorContext, FrozenContract
from nextops.contracts.sources import SourceEvidence, SourceReadOperation, SourceReadRequest

MAX_SOURCE_EVIDENCE_BYTES = 131_072


class SourceAuditEvent(FrozenContract):
    """Text-free source event; the deployment audit port must persist it durably."""

    actor: ActorContext
    correlation_id: UUID
    request: SourceReadRequest | None = None
    operation: SourceReadOperation | None = None
    outcome: Literal["started", "completed", "failed", "denied", "cancelled"]
    occurred_at: AwareDatetime
    evidence_sha256: str | None = Field(default=None, pattern=r"^[0-9a-f]{64}$")
    error_code: ErrorCode | None = None

    @model_validator(mode="after")
    def validate_context(self) -> SourceAuditEvent:
        if self.request is None:
            if self.outcome != "denied" or self.operation is not None:
                raise ValueError("only protocol denials may omit validated request context")
        elif self.operation is None or self.correlation_id != self.request.correlation_id:
            raise ValueError("source audit correlation must match its validated request")
        return self


class SourceAuthorization(Protocol):
    """Revalidate live caller permission; never supplied through tool arguments."""

    async def authorize(
        self, actor: ActorContext, source: ZabbixSource, target: ZabbixSourceTarget
    ) -> None: ...


class SourceAudit(Protocol):
    """Required port: implementations must fail closed on unavailable durable storage."""

    async def record(self, event: SourceAuditEvent) -> None: ...


class SourceReader:
    """Bounded two-source-or-more reads without changing the legacy connector."""

    def __init__(
        self,
        registry: ZabbixSourceRegistry,
        authorize: SourceAuthorization,
        audit: SourceAudit,
        transport_factory: Callable[[ZabbixSource], ZabbixTransport],
        *,
        deadline_seconds: float = 30.0,
        max_active: int = 2,
    ) -> None:
        if not 0 < deadline_seconds <= 60 or not 1 <= max_active <= 2:
            raise ValueError("source read limits exceed the reviewed profile")
        self._registry = registry
        self._authorize = authorize
        self._audit = audit
        self._transport_factory = transport_factory
        self._deadline = deadline_seconds
        self._admission = asyncio.Semaphore(max_active)

    async def deny_protocol(self, actor: ActorContext, code: ErrorCode) -> None:
        """Persist a denial without copying malformed arguments/tool names into audit."""
        await self._record(
            SourceAuditEvent(
                actor=actor,
                correlation_id=uuid4(),
                outcome="denied",
                occurred_at=datetime.now(UTC),
                error_code=code,
            )
        )

    async def _record(self, event: SourceAuditEvent) -> None:
        # MCP cancellation uses AnyIO level cancellation. Preserve a bounded durable
        # terminal audit attempt instead of cancelling its transaction immediately.
        with CancelScope(shield=True):
            await asyncio.wait_for(self._audit.record(event), self._deadline)

    async def _check_permission(
        self, actor: ActorContext, source: ZabbixSource, target: ZabbixSourceTarget
    ) -> None:
        try:
            await asyncio.wait_for(self._authorize.authorize(actor, source, target), self._deadline)
        except TimeoutError:
            raise ApplicationError(
                ErrorCode.TIMEOUT, "connector.source_authorization_timeout"
            ) from None

    async def read(
        self, actor: ActorContext, request: SourceReadRequest, operation: SourceReadOperation
    ) -> SourceEvidence:
        if operation not in {"summary", "incident_context"}:
            raise ApplicationError(ErrorCode.POLICY_DENIED, "connector.source_operation_denied")

        def event(
            outcome: Literal["started", "completed", "failed", "denied", "cancelled"],
            error: ErrorCode | None = None,
            digest: str | None = None,
        ) -> SourceAuditEvent:
            return SourceAuditEvent(
                actor=actor,
                correlation_id=request.correlation_id,
                request=request,
                operation=operation,
                outcome=outcome,
                occurred_at=datetime.now(UTC),
                error_code=error,
                evidence_sha256=digest,
            )

        try:
            source, target = self._registry.resolve(request.source_id, request.target_id)
            if (
                "zabbix.read" not in actor.scopes
                or actor.organization_id != source.organization_id
                or actor.environment_id != source.environment_id
            ):
                raise ApplicationError(ErrorCode.POLICY_DENIED, "connector.source_scope_denied")
            await self._check_permission(actor, source, target)
        except ApplicationError as error:
            await self._record(event("denied", error.code))
            raise
        if self._admission.locked():
            await self._record(event("denied", ErrorCode.OVERLOADED))
            raise ApplicationError(
                ErrorCode.OVERLOADED, "connector.source_overloaded", retryable=True
            )
        await self._admission.acquire()
        task: asyncio.Task[SourceEvidence] | None = None
        stop_collection = asyncio.Event()
        try:
            await self._record(event("started"))
            task = asyncio.create_task(
                self._collect(source, target, request, operation, stop_collection)
            )
            try:
                evidence = await asyncio.wait_for(asyncio.shield(task), self._deadline)
                # Role/scope revocation during collection cannot publish an old grant.
                await self._check_permission(actor, source, target)
                payload = json.dumps(
                    evidence.model_dump(mode="json"),
                    sort_keys=True,
                    separators=(",", ":"),
                    ensure_ascii=False,
                ).encode("utf-8")
                if len(payload) > MAX_SOURCE_EVIDENCE_BYTES:
                    raise ApplicationError(
                        ErrorCode.DEPENDENCY_UNAVAILABLE, "connector.source_response_too_large"
                    )
            except TimeoutError:
                stop_collection.set()
                raise ApplicationError(
                    ErrorCode.TIMEOUT, "connector.source_timeout", retryable=True
                ) from None
            except asyncio.CancelledError:
                stop_collection.set()
                await self._record(event("cancelled", ErrorCode.TIMEOUT))
                raise
            except ApplicationError:
                raise
            except Exception:
                raise ApplicationError(
                    ErrorCode.DEPENDENCY_UNAVAILABLE, "connector.source_unavailable", retryable=True
                ) from None
            await self._record(event("completed", digest=hashlib.sha256(payload).hexdigest()))
            return evidence
        except ApplicationError as error:
            await self._record(event("failed", error.code))
            raise
        finally:
            stop_collection.set()
            if task is not None and not task.done():
                # Cancellation of a coroutine does not stop urllib's native thread. Keep the
                # slot until actual collection exits; no detached unbounded retry/queue.
                task.add_done_callback(self._drained)
            else:
                self._admission.release()

    def _drained(self, task: asyncio.Task[SourceEvidence]) -> None:
        if not task.cancelled():
            task.exception()  # retrieve, never log raw exception text
        self._admission.release()

    async def _collect(
        self,
        source: ZabbixSource,
        target: ZabbixSourceTarget,
        request: SourceReadRequest,
        operation: SourceReadOperation,
        stop_collection: asyncio.Event,
    ) -> SourceEvidence:
        transport = ScopedZabbixTransport(
            source, target, self._transport_factory(source), stopped=stop_collection.is_set
        )
        client = ZabbixReadClient(target.host, transport)
        evidence = (
            await client.summary() if operation == "summary" else await client.incident_context()
        )
        return SourceEvidence(
            source_id=source.source_id,
            target_id=target.target_id,
            correlation_id=request.correlation_id,
            operation=operation,
            host_group_ids=transport.verified_group_ids,
            evidence=evidence,
        )
