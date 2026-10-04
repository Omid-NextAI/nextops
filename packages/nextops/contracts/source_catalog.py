"""Credential-free approved catalogue, never a claim of live discovery or health."""

from typing import Literal, Self
from uuid import UUID

from pydantic import Field, model_validator

from nextops.contracts.assistant import AssistantRequest
from nextops.contracts.models import FrozenContract
from nextops.contracts.sources import BindingDigest, LogicalSourceId, SourceReadBinding


class CatalogTarget(FrozenContract):
    target_id: LogicalSourceId
    label: str = Field(min_length=1, max_length=128)
    binding_sha256: BindingDigest | None = None


class CatalogSource(FrozenContract):
    source_id: LogicalSourceId
    label: str = Field(min_length=1, max_length=128)
    organization_id: UUID
    environment_id: UUID
    targets: tuple[CatalogTarget, ...] = Field(min_length=1, max_length=16)


class SourceCatalog(FrozenContract):
    schema_version: Literal["1.0.0"] = "1.0.0"
    discovery_mode: Literal["approved_registry"] = "approved_registry"
    sources: tuple[CatalogSource, ...] = Field(default=(), max_length=8)

    @model_validator(mode="after")
    def unique_bindings(self) -> Self:
        if len({s.source_id for s in self.sources}) != len(self.sources) or any(
            len({t.target_id for t in s.targets}) != len(s.targets) for s in self.sources
        ):
            raise ValueError("duplicate catalogue identity")
        return self

    def resolve_binding(self, source_id: str, target_id: str) -> SourceReadBinding:
        for source in self.sources:
            target = next((t for t in source.targets if t.target_id == target_id), None)
            if source.source_id == source_id and target is not None:
                return SourceReadBinding(
                    source_id=source_id,
                    target_id=target_id,
                    organization_id=source.organization_id,
                    environment_id=source.environment_id,
                    binding_sha256=target.binding_sha256,
                )
        raise KeyError("unapproved source/target")


class SourceAssistantRequest(AssistantRequest):
    source_id: LogicalSourceId
    target_id: LogicalSourceId


class GatewayReadRequest(FrozenContract):
    """Closed runner message; source arguments cannot replace a named operation."""

    operation: Literal[
        "source_summary",
        "source_incident_context",
        "primary_summary",
        "primary_incident_context",
        "incident_evidence",
    ]
    correlation_id: UUID
    source_id: LogicalSourceId | None = None
    target_id: LogicalSourceId | None = None
    binding_sha256: BindingDigest | None = None

    @model_validator(mode="after")
    def bind_operation(self) -> Self:
        if self.operation.startswith("source_"):
            if self.source_id is None or self.target_id is None:
                raise ValueError("source and target required")
        elif (
            self.source_id is not None
            or (self.operation == "incident_evidence" and self.target_id is None)
            or (self.operation != "incident_evidence" and self.target_id is not None)
        ):
            raise ValueError("invalid operation binding")
        return self


class GatewayToolRequest(FrozenContract):
    correlation_id: UUID
    target_id: LogicalSourceId | None = None
    binding_sha256: BindingDigest | None = None
