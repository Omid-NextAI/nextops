"""Source-qualified requests and evidence; no credential or endpoint fields."""

from typing import Annotated, Literal, Self
from uuid import UUID

from pydantic import Field, model_validator

from nextops.contracts.models import FrozenContract
from nextops.contracts.monitoring import MonitoringIncidentContext, MonitoringSummary
from nextops.contracts.sources_ids import LogicalSourceId as LogicalSourceId
from nextops.contracts.sources_ids import ZabbixObjectId as ZabbixObjectId

SourceReadOperation = Literal["summary", "incident_context"]
BindingDigest = Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")]


class SourceReadBinding(FrozenContract):
    """Credential-free policy binding supplied by a trusted registry adapter."""

    source_id: LogicalSourceId
    target_id: LogicalSourceId
    organization_id: UUID
    environment_id: UUID
    binding_sha256: BindingDigest | None = None


class SourceReadRequest(FrozenContract):
    """Only logical identifiers and correlation, never URLs/methods/roles."""

    source_id: LogicalSourceId
    target_id: LogicalSourceId
    correlation_id: UUID
    binding_sha256: BindingDigest | None = None


class SourceEvidence(FrozenContract):
    """Namespaced evidence, including the verified collection scope."""

    source_id: LogicalSourceId
    target_id: LogicalSourceId
    operation: SourceReadOperation
    correlation_id: UUID
    host_group_ids: tuple[ZabbixObjectId, ...] = Field(min_length=1, max_length=32)
    binding_sha256: BindingDigest | None = None
    evidence: MonitoringSummary | MonitoringIncidentContext

    @model_validator(mode="after")
    def consistent_operation(self) -> Self:
        if (self.operation == "summary") != isinstance(self.evidence, MonitoringSummary):
            raise ValueError("source operation must match evidence type")
        if len(set(self.host_group_ids)) != len(self.host_group_ids):
            raise ValueError("source group identifiers must be unique")
        return self
