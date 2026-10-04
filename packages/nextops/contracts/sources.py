"""Source-qualified requests and evidence; no credential or endpoint fields."""

from typing import Annotated, Literal, Self
from uuid import UUID

from pydantic import Field, model_validator

from nextops.contracts.models import FrozenContract
from nextops.contracts.monitoring import MonitoringIncidentContext, MonitoringSummary

LogicalSourceId = Annotated[str, Field(pattern=r"^[a-z][a-z0-9-]{1,31}$")]
ZabbixObjectId = Annotated[str, Field(pattern=r"^[1-9][0-9]{0,19}$")]
SourceReadOperation = Literal["summary", "incident_context"]


class SourceReadRequest(FrozenContract):
    """Only logical identifiers and correlation, never URLs/methods/roles."""

    source_id: LogicalSourceId
    target_id: LogicalSourceId
    correlation_id: UUID


class SourceEvidence(FrozenContract):
    """Namespaced evidence, including the verified collection scope."""

    source_id: LogicalSourceId
    target_id: LogicalSourceId
    operation: SourceReadOperation
    correlation_id: UUID
    host_group_ids: tuple[ZabbixObjectId, ...] = Field(min_length=1, max_length=32)
    evidence: MonitoringSummary | MonitoringIncidentContext

    @model_validator(mode="after")
    def consistent_operation(self) -> Self:
        if (self.operation == "summary") != isinstance(self.evidence, MonitoringSummary):
            raise ValueError("source operation must match evidence type")
        if len(set(self.host_group_ids)) != len(self.host_group_ids):
            raise ValueError("source group identifiers must be unique")
        return self
