"""Private source registry and scoped reuse of the existing Zabbix reader."""

from __future__ import annotations

import json
import os
import stat
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any, Literal, Self
from urllib.parse import urlsplit
from uuid import UUID

from pydantic import Field, model_validator

from nextops.application.errors import ApplicationError
from nextops.connectors.zabbix import ZabbixTransport
from nextops.contracts.errors import ErrorCode
from nextops.contracts.models import FrozenContract
from nextops.contracts.sources import LogicalSourceId, ZabbixObjectId

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
        return result
