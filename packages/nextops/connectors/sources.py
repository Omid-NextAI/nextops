"""Private source registry and scoped reuse of the existing Zabbix reader."""

from __future__ import annotations

import json
import os
import stat
import sys
from collections.abc import Callable
from hashlib import sha256
from pathlib import Path
from typing import Any, Literal, Self
from urllib.parse import urlsplit
from uuid import UUID

from pydantic import Field, model_validator

from nextops.application.errors import ApplicationError
from nextops.connectors.zabbix import ZabbixReadClient, ZabbixTransport
from nextops.contracts.errors import ErrorCode
from nextops.contracts.models import FrozenContract
from nextops.contracts.sources import (
    LogicalSourceId,
    SourceEvidence,
    SourceReadBinding,
    SourceReadOperation,
    SourceReadRequest,
    ZabbixObjectId,
)

MAX_REGISTRY_BYTES = 65_536
READ_METHODS = frozenset(
    {"apiinfo.version", "host.get", "item.get", "problem.get", "history.get", "event.get"}
)


class ZabbixSourceTarget(FrozenContract):
    """Deployment-owned exact target binding, independent of host ID collisions."""

    target_id: LogicalSourceId
    host_id: ZabbixObjectId
    host: str = Field(min_length=1, max_length=128, repr=False)
    host_group_ids: tuple[ZabbixObjectId, ...] = Field(min_length=1, max_length=32)


class ZabbixSource(FrozenContract):
    """Private manifest: credential reference only, never a token value."""

    source_id: LogicalSourceId
    organization_id: UUID
    environment_id: UUID
    api_url: str = Field(max_length=512, repr=False)
    ca_file: Path = Field(repr=False)
    credential_name: str = Field(pattern=r"^[a-z][a-z0-9-]{2,63}$", repr=False)
    approved_group_ids: tuple[ZabbixObjectId, ...] = Field(min_length=1, max_length=32)
    targets: tuple[ZabbixSourceTarget, ...] = Field(min_length=1, max_length=16)

    @model_validator(mode="after")
    def validate_bindings(self) -> Self:
        url = urlsplit(self.api_url)
        if (
            url.scheme != "https"
            or not url.hostname
            or url.path != "/api_jsonrpc.php"
            or url.username
            or url.password
            or url.query
            or url.fragment
            or (url.port is not None and not 1 <= url.port <= 65_535)
        ):
            raise ValueError("source requires a plain verified HTTPS API origin")
        if not self.ca_file.is_absolute():
            raise ValueError("source CA must be an absolute deployment path")
        groups = set(self.approved_group_ids)
        if len(groups) != len(self.approved_group_ids):
            raise ValueError("approved groups must be unique")
        if len({target.target_id for target in self.targets}) != len(self.targets):
            raise ValueError("target identifiers must be unique within a source")
        if len({target.host_id for target in self.targets}) != len(self.targets):
            raise ValueError("a source host must have exactly one target binding")
        for target in self.targets:
            if len(set(target.host_group_ids)) != len(target.host_group_ids):
                raise ValueError("target group identifiers must be unique")
            if not set(target.host_group_ids).issubset(groups):
                raise ValueError("target groups must be explicitly approved")
        return self


class ZabbixSourceRegistry(FrozenContract):
    """Bounded reviewed registry; no implicit default or source fallback."""

    schema_version: Literal["1.0.0"] = "1.0.0"
    sources: tuple[ZabbixSource, ...] = Field(min_length=1, max_length=8)

    @model_validator(mode="after")
    def unique_sources(self) -> Self:
        if len({source.source_id for source in self.sources}) != len(self.sources):
            raise ValueError("source identifiers must be unique")
        if len({source.credential_name for source in self.sources}) != len(self.sources):
            raise ValueError("source credentials must have distinct references")
        endpoints = {
            (urlsplit(source.api_url).hostname, urlsplit(source.api_url).port or 443)
            for source in self.sources
        }
        if len(endpoints) != len(self.sources):
            raise ValueError("source endpoints must be distinct")
        return self

    @classmethod
    def from_file(cls, path: Path) -> ZabbixSourceRegistry:
        """Read bounded regular metadata; redact parser input from failures."""
        try:
            metadata = path.lstat()
            if sys.platform == "win32":
                # The future trusted Windows composition must qualify its private ACL.
                owner_safe = True
            else:
                owner_safe = not metadata.st_mode & 0o022 and metadata.st_uid in (0, os.geteuid())
            if (
                not path.is_absolute()
                or not stat.S_ISREG(metadata.st_mode)
                or metadata.st_size > MAX_REGISTRY_BYTES
                or not owner_safe
            ):
                raise ValueError("invalid source registry file")
            with path.open("rb") as stream:
                opened = os.fstat(stream.fileno())
                if (metadata.st_dev, metadata.st_ino) != (opened.st_dev, opened.st_ino):
                    raise ValueError("source registry changed during open")
                raw = stream.read(MAX_REGISTRY_BYTES + 1)
            if len(raw) > MAX_REGISTRY_BYTES:
                raise ValueError("source registry exceeds byte budget")
            return cls.model_validate(json.loads(raw, object_pairs_hook=_unique_object))
        except (OSError, ValueError):
            raise ValueError("source registry invalid or unavailable") from None

    def resolve(self, source_id: str, target_id: str) -> tuple[ZabbixSource, ZabbixSourceTarget]:
        for source in self.sources:
            if source.source_id == source_id:
                for target in source.targets:
                    if target.target_id == target_id:
                        return source, target
        raise ApplicationError(ErrorCode.POLICY_DENIED, "connector.source_target_denied")

    def resolve_binding(self, source_id: str, target_id: str) -> SourceReadBinding:
        source, target = self.resolve(source_id, target_id)
        return SourceReadBinding(
            source_id=source.source_id,
            target_id=target.target_id,
            organization_id=source.organization_id,
            environment_id=source.environment_id,
            binding_sha256=self.binding_digest(source_id, target_id),
        )

    def binding_digest(self, source_id: str, target_id: str) -> str:
        """Opaque identity commits endpoint, tenant, trust/credential references and exact scope."""
        source, target = self.resolve(source_id, target_id)
        return sha256(
            json.dumps(
                {
                    "source": source.model_dump(mode="json", exclude={"targets"}),
                    "target": target.model_dump(mode="json"),
                },
                sort_keys=True,
                separators=(",", ":"),
                ensure_ascii=False,
            ).encode("utf-8")
        ).hexdigest()


class ZabbixSourceCollector:
    """Outer adapter owns private endpoints and reader construction, not application policy."""

    def __init__(
        self,
        registry: ZabbixSourceRegistry,
        transport_factory: Callable[[ZabbixSource], ZabbixTransport],
    ) -> None:
        self._registry = registry
        self._transport_factory = transport_factory

    async def collect(
        self,
        request: SourceReadRequest,
        operation: SourceReadOperation,
        *,
        stopped: Callable[[], bool],
    ) -> SourceEvidence:
        source, target = self._registry.resolve(request.source_id, request.target_id)
        digest = self._registry.binding_digest(request.source_id, request.target_id)
        if request.binding_sha256 is not None and request.binding_sha256 != digest:
            raise ApplicationError(ErrorCode.POLICY_DENIED, "connector.source_binding_mismatch")
        transport = ScopedZabbixTransport(
            source, target, self._transport_factory(source), stopped=stopped
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
            binding_sha256=digest if request.binding_sha256 is not None else None,
            evidence=evidence,
        )


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for name, value in pairs:
        if name in result:
            raise ValueError("duplicate registry property")
        result[name] = value
    return result


class ScopedZabbixTransport:
    """Recheck exact host/group binding before any dependent read."""

    def __init__(
        self,
        source: ZabbixSource,
        target: ZabbixSourceTarget,
        transport: ZabbixTransport,
        *,
        stopped: Callable[[], bool] = lambda: False,
    ) -> None:
        self._source = source
        self._target = target
        self._transport = transport
        self._stopped = stopped
        self._host_verified = False
        self._item_ids: set[str] = set()
        self.verified_group_ids: tuple[str, ...] = ()

    async def call(self, method: str, params: dict[str, Any]) -> Any:
        if self._stopped():
            raise ApplicationError(ErrorCode.TIMEOUT, "connector.source_timeout")
        if method not in READ_METHODS:
            raise ApplicationError(ErrorCode.POLICY_DENIED, "connector.zabbix_method_denied")
        bound = dict(params)
        if method == "apiinfo.version":
            if params:
                raise ApplicationError(ErrorCode.POLICY_DENIED, "connector.zabbix_scope_denied")
        elif method == "host.get":
            self._host_verified = False
            self._item_ids.clear()
            self.verified_group_ids = ()
            if params.get("filter") != {"host": [self._target.host]}:
                raise ApplicationError(ErrorCode.POLICY_DENIED, "connector.zabbix_scope_denied")
            bound.update(
                hostids=[self._target.host_id],
                groupids=list(self._target.host_group_ids),
                selectHostGroups=["groupid"],
                limit=2,
            )
        else:
            if not self._host_verified or params.get("hostids") != [self._target.host_id]:
                raise ApplicationError(ErrorCode.POLICY_DENIED, "connector.zabbix_scope_denied")
            if method == "history.get" and (
                not isinstance(params.get("itemids"), list)
                or not params["itemids"]
                or not set(params["itemids"]).issubset(self._item_ids)
            ):
                raise ApplicationError(ErrorCode.POLICY_DENIED, "connector.zabbix_scope_denied")
            if method == "item.get":
                bound["output"] = [*params["output"], "hostid"]
            if method in {"problem.get", "event.get"}:
                bound.update(source=0, object=0)
                bound["output"] = list(
                    dict.fromkeys([*params["output"], "eventid", "objectid", "source", "object"])
                )
                if method == "event.get":
                    bound["selectHosts"] = ["hostid"]
        result = await self._transport.call(method, bound)
        if self._stopped():
            # A timed-out native request may finish; never start its dependent reads.
            raise ApplicationError(ErrorCode.TIMEOUT, "connector.source_timeout")
        if method == "host.get":
            if not isinstance(result, list) or len(result) != 1 or not isinstance(result[0], dict):
                raise ApplicationError(ErrorCode.POLICY_DENIED, "connector.zabbix_scope_denied")
            host = result[0]
            groups = host.get("hostgroups")
            if (
                host.get("hostid") != self._target.host_id
                or host.get("host") != self._target.host
                or not isinstance(groups, list)
                or len(groups) > 32
                or any(not isinstance(group, dict) for group in groups)
            ):
                raise ApplicationError(ErrorCode.POLICY_DENIED, "connector.zabbix_scope_denied")
            observed = {group.get("groupid") for group in groups}
            if not observed.intersection(self._target.host_group_ids):
                raise ApplicationError(ErrorCode.POLICY_DENIED, "connector.zabbix_scope_denied")
            self._host_verified = True
            self.verified_group_ids = tuple(
                sorted(observed.intersection(self._target.host_group_ids))
            )
        elif method == "item.get":
            if (
                not isinstance(result, list)
                or len(result) > 1000
                or any(
                    not isinstance(item, dict)
                    or item.get("hostid") != self._target.host_id
                    or not isinstance(item.get("itemid"), str)
                    for item in result
                )
            ):
                raise ApplicationError(ErrorCode.DEPENDENCY_UNAVAILABLE, "connector.source_invalid")
            self._item_ids = {item["itemid"] for item in result}
        elif method == "history.get":
            if not isinstance(result, list) or any(
                not isinstance(point, dict) or point.get("itemid") not in params["itemids"]
                for point in result
            ):
                raise ApplicationError(ErrorCode.DEPENDENCY_UNAVAILABLE, "connector.source_invalid")
        elif method in {"problem.get", "event.get"}:
            limit = params.get("limit")
            if (
                not isinstance(limit, int)
                or not 1 <= limit <= 101
                or not isinstance(result, list)
                or len(result) > limit
                or any(not isinstance(row, dict) for row in result)
            ):
                raise ApplicationError(ErrorCode.DEPENDENCY_UNAVAILABLE, "connector.source_invalid")
            if method == "problem.get" and result:
                # problem.get cannot return selectHosts. Resolve the exact bounded event
                # identities through the already allowlisted event.get ownership relation.
                if any(not _valid_object_id(row.get("eventid")) for row in result):
                    raise ApplicationError(
                        ErrorCode.DEPENDENCY_UNAVAILABLE, "connector.source_invalid"
                    )
                events = await self.call(
                    "event.get",
                    {
                        "hostids": [self._target.host_id],
                        "eventids": [row["eventid"] for row in result],
                        "source": 0,
                        "object": 0,
                        "output": ["eventid", "objectid", "source", "object"],
                        "limit": len(result),
                    },
                )
                identities = {row["eventid"]: row["objectid"] for row in events}
                if len(identities) != len(result) or any(
                    not _valid_object_id(row.get("objectid"))
                    or row.get("source") != "0"
                    or row.get("object") != "0"
                    or identities.get(row["eventid"]) != row["objectid"]
                    for row in result
                ):
                    raise ApplicationError(ErrorCode.POLICY_DENIED, "connector.zabbix_scope_denied")
            elif method == "event.get":
                if len({row.get("eventid") for row in result}) != len(result) or any(
                    not _valid_object_id(row.get("eventid"))
                    or not _valid_object_id(row.get("objectid"))
                    or row.get("source") != "0"
                    or row.get("object") != "0"
                    or not isinstance(row.get("hosts"), list)
                    or not 1 <= len(row["hosts"]) <= 32
                    or any(
                        not isinstance(host, dict) or host.get("hostid") != self._target.host_id
                        for host in row["hosts"]
                    )
                    for row in result
                ):
                    raise ApplicationError(ErrorCode.POLICY_DENIED, "connector.zabbix_scope_denied")
        return result


def _valid_object_id(value: Any) -> bool:
    return (
        isinstance(value, str)
        and value.isascii()
        and value.isdecimal()
        and (1 <= len(value) <= 20 and not value.startswith("0"))
    )
