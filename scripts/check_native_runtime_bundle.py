"""Read-only verification of a pinned, protected POSIX native runtime inventory.

This checks installed tree identity, not ELF closure, effective units, loaded mappings,
build provenance, CPU execution, model quality, offline operation or deployment acceptance.
It never executes an artifact, installs anything, changes a link or writes a report.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import sys
from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import Any

SOURCE_COMMIT = "b29c606e28a01b1bc8c1351026a0fa6e616bf6c4"
BINARY_SHA256 = "dbe5a5cdd4842fe2d498270c1e1df58344e9052e97214e2ba9c9845443a1b0dc"
MAX_INVENTORY_BYTES = 262_144
MAX_FILE_BYTES = 536_870_912
MAX_TOTAL_BYTES = 2_147_483_648
MAX_FILES = 256
MAX_DIRECTORIES = 64
MAX_ALIASES = 128
MAX_TREE_ENTRIES = MAX_FILES + MAX_DIRECTORIES + MAX_ALIASES
MAX_DEPTH = 8
MAX_ALIAS_HOPS = 16
_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_COMPONENT = re.compile(r"[A-Za-z0-9._+-]{1,96}\Z")
_ROOT = re.compile(
    r"/srv/nextops/releases/llama\.cpp-"
    r"(?:b29c606e|b29c606e28a01b1bc8c1351026a0fa6e616bf6c4)"
    r"(?:-[a-z0-9][a-z0-9._-]{0,63})?\Z"
)
NOT_VERIFIED = (
    "effective unit; loaded mappings; ELF closure; system dependencies; build provenance; "
    "CPU execution; model quality; WAN/offline operation; deployment acceptance"
)


class NativeBundleError(ValueError):
    """A bounded, sanitized failure; no private paths or inventory values in messages."""


@dataclass(frozen=True)
class Fingerprint:
    device: int
    inode: int
    mode: int
    uid: int
    gid: int
    links: int
    size: int
    modified_ns: int
    changed_ns: int


@dataclass(frozen=True)
class FileRecord:
    path: str
    size_bytes: int
    sha256: str
    mode: int
    gid: int


@dataclass(frozen=True)
class DirectoryRecord:
    path: str
    mode: int
    gid: int


@dataclass(frozen=True)
class AliasRecord:
    path: str
    target: str
    gid: int


@dataclass(frozen=True)
class Inventory:
    root: str
    root_mode: int
    root_gid: int
    files: dict[str, FileRecord]
    directories: dict[str, DirectoryRecord]
    aliases: dict[str, AliasRecord]


@dataclass(frozen=True)
class VerificationSummary:
    file_count: int
    directory_count: int
    alias_count: int
    total_bytes: int
    inventory_sha256: str


def _require_posix_root() -> None:
    if os.name != "posix" or not hasattr(os, "geteuid") or os.geteuid() != 0:
        raise NativeBundleError("verification requires POSIX root; no platform bypass")
    required = ("O_NOFOLLOW", "O_DIRECTORY", "O_CLOEXEC", "O_NONBLOCK")
    if any(not hasattr(os, name) for name in required):
        raise NativeBundleError("required no-follow filesystem controls are unavailable")


def _fingerprint(metadata: os.stat_result) -> Fingerprint:
    return Fingerprint(
        metadata.st_dev,
        metadata.st_ino,
        metadata.st_mode,
        metadata.st_uid,
        metadata.st_gid,
        metadata.st_nlink,
        metadata.st_size,
        metadata.st_mtime_ns,
        metadata.st_ctime_ns,
    )


def _safe_components(value: object, *, absolute: bool = False) -> tuple[str, ...]:
    if type(value) is not str or not value or len(value) > 240:
        raise NativeBundleError("invalid bounded path")
    if absolute:
        if not value.startswith("/"):
            raise NativeBundleError("an absolute protected path is required")
        value = value[1:]
    elif value.startswith("/"):
        raise NativeBundleError("inventory entries must be relative")
    parts = value.split("/")
    if not parts or len(parts) > MAX_DEPTH:
        raise NativeBundleError("path depth exceeds the bound")
    if any(part in {".", ".."} or not _COMPONENT.fullmatch(part) for part in parts):
        raise NativeBundleError("noncanonical or unsafe path")
    return tuple(parts)


def _protected(metadata: os.stat_result, *, kind: str) -> Fingerprint:
    value = _fingerprint(metadata)
    expected_type = {"directory": stat.S_ISDIR, "file": stat.S_ISREG, "alias": stat.S_ISLNK}
    if not expected_type[kind](value.mode):
        raise NativeBundleError("unexpected filesystem object type")
    if value.uid != 0:
        raise NativeBundleError("a runtime or inventory path is not root owned")
    # A symlink's 0777 bits do not authorize target writes; protect its parent and target instead.
    if kind != "alias" and value.mode & (stat.S_IWGRP | stat.S_IWOTH | 0o7000):
        raise NativeBundleError("a protected path has unsafe write or special permissions")
    if kind != "directory" and value.links != 1:
        raise NativeBundleError("hard-linked runtime or inventory objects are not permitted")
    return value


def _directory_flags() -> int:
    return os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC


def _file_flags() -> int:
    return os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC | os.O_NONBLOCK


def _open_absolute_directory(path: str) -> tuple[int, dict[str, Fingerprint]]:
    parts = _safe_components(path, absolute=True)
    descriptor = os.open("/", _directory_flags())
    ancestors: dict[str, Fingerprint] = {}
    try:
        ancestors["/"] = _protected(os.fstat(descriptor), kind="directory")
        current = ""
        for part in parts:
            observed = os.stat(part, dir_fd=descriptor, follow_symlinks=False)
            before = _protected(observed, kind="directory")
            following = os.open(part, _directory_flags(), dir_fd=descriptor)
            try:
                if _fingerprint(os.fstat(following)) != before:
                    raise NativeBundleError("directory metadata changed during traversal")
            except BaseException:
                os.close(following)
                raise
            os.close(descriptor)
            descriptor = following
            current += "/" + part
            ancestors[current] = before
        return descriptor, ancestors
    except BaseException:
        os.close(descriptor)
        raise


def _read_inventory(path: str, expected_sha256: str) -> tuple[bytes, dict[str, Fingerprint]]:
    _safe_components(path, absolute=True)
    location = PurePosixPath(path)
    descriptor, observed = _open_absolute_directory(str(location.parent))
    try:
        before = _protected(
            os.stat(location.name, dir_fd=descriptor, follow_symlinks=False), kind="file"
        )
        if before.size < 1 or before.size > MAX_INVENTORY_BYTES:
            raise NativeBundleError("inventory size exceeds the bound")
        source = os.open(location.name, _file_flags(), dir_fd=descriptor)
        try:
            if _fingerprint(os.fstat(source)) != before:
                raise NativeBundleError("inventory metadata changed before reading")
            chunks: list[bytes] = []
            remaining = MAX_INVENTORY_BYTES + 1
            while remaining:
                block = os.read(source, min(65_536, remaining))
                if not block:
                    break
                chunks.append(block)
                remaining -= len(block)
            contents = b"".join(chunks)
            if len(contents) != before.size or _fingerprint(os.fstat(source)) != before:
                raise NativeBundleError("inventory metadata or length changed during reading")
        finally:
            os.close(source)
        if hashlib.sha256(contents).hexdigest() != expected_sha256:
            raise NativeBundleError("inventory digest differs from the external trust anchor")
        observed[path] = before
        return contents, observed
    finally:
        os.close(descriptor)


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise NativeBundleError("duplicate inventory JSON field")
        result[key] = value
    return result


def _object(value: object, fields: set[str]) -> dict[str, Any]:
    if type(value) is not dict or set(value) != fields:
        raise NativeBundleError("inventory fields do not match the strict contract")
    return value


def _integer(value: object, maximum: int, *, minimum: int = 0) -> int:
    if type(value) is not int or not minimum <= value <= maximum:
        raise NativeBundleError("inventory integer violates its bounded contract")
    return value


def _mode(value: object) -> int:
    if type(value) is not str or re.fullmatch(r"0[0-7]{3}", value) is None:
        raise NativeBundleError("invalid inventory permission mode")
    mode = int(value, 8)
    if mode & 0o022:
        raise NativeBundleError("inventory permits non-root writes")
    return mode


def _records(value: object, maximum: int) -> list[Any]:
    if type(value) is not list or len(value) > maximum:
        raise NativeBundleError("inventory entry count exceeds the bound")
    return value


def _alias_destination(path: str, target: object) -> str:
    if type(target) is not str or not target or len(target) > 240 or target.startswith("/"):
        raise NativeBundleError("invalid relative alias target")
    destination = list(PurePosixPath(path).parent.parts)
    for part in target.split("/"):
        if part == "..":
            if not destination:
                raise NativeBundleError("alias escapes the runtime root")
            destination.pop()
        elif part == "." or not _COMPONENT.fullmatch(part):
            raise NativeBundleError("unsafe or noncanonical alias target")
        else:
            destination.append(part)
    result = "/".join(destination)
    _safe_components(result)
    return result


def _expected_binary_digest(candidate_binary_sha256: str | None) -> str:
    if candidate_binary_sha256 is None:
        return BINARY_SHA256
    if (
        type(candidate_binary_sha256) is not str
        or _SHA256.fullmatch(candidate_binary_sha256) is None
    ):
        raise NativeBundleError("external candidate binary SHA-256 is invalid")
    return candidate_binary_sha256


def _parse_inventory(contents: bytes, *, candidate_binary_sha256: str | None = None) -> Inventory:
    expected_binary = _expected_binary_digest(candidate_binary_sha256)
    expected_version = "1.0.0" if candidate_binary_sha256 is None else "1.1.0"
    try:
        document = json.loads(contents, object_pairs_hook=_unique_object)
    except (ValueError, UnicodeError, RecursionError) as error:
        raise NativeBundleError("inventory JSON is invalid or ambiguous") from error
    document = _object(
        document,
        {
            "schema_version",
            "source_commit",
            "runtime_root",
            "root_mode",
            "root_gid",
            "binary_sha256",
            "files",
            "directories",
            "aliases",
        },
    )
    if (
        document["schema_version"] != expected_version
        or document["source_commit"] != SOURCE_COMMIT
        or document["binary_sha256"] != expected_binary
    ):
        if candidate_binary_sha256 is not None:
            raise NativeBundleError(
                "inventory does not describe the externally pinned candidate runtime"
            )
        raise NativeBundleError("inventory does not describe the pinned original runtime")
    root = document["runtime_root"]
    if type(root) is not str or _ROOT.fullmatch(root) is None:
        raise NativeBundleError(
            "runtime root is outside the commit-bearing protected release scope"
        )
    _safe_components(root, absolute=True)
    files: dict[str, FileRecord] = {}
    directories: dict[str, DirectoryRecord] = {}
    aliases: dict[str, AliasRecord] = {}
    used: set[str] = set()
    for kind, fields, maximum in (
        ("files", {"path", "size_bytes", "sha256", "mode", "gid"}, MAX_FILES),
        ("directories", {"path", "mode", "gid"}, MAX_DIRECTORIES),
        ("aliases", {"path", "target", "gid"}, MAX_ALIASES),
    ):
        for item in _records(document[kind], maximum):
            record = _object(item, fields)
            path = "/".join(_safe_components(record["path"]))
            if path in used:
                raise NativeBundleError("duplicate or overlapping inventory path")
            used.add(path)
            gid = _integer(record["gid"], 2_147_483_647)
            if kind == "files":
                digest = record["sha256"]
                if type(digest) is not str or _SHA256.fullmatch(digest) is None:
                    raise NativeBundleError("invalid file SHA-256")
                files[path] = FileRecord(
                    path,
                    _integer(record["size_bytes"], MAX_FILE_BYTES, minimum=1),
                    digest,
                    _mode(record["mode"]),
                    gid,
                )
            elif kind == "directories":
                directories[path] = DirectoryRecord(path, _mode(record["mode"]), gid)
            else:
                _alias_destination(path, record["target"])
                aliases[path] = AliasRecord(path, record["target"], gid)
    executable = files.get("bin/llama-server")
    if executable is None or executable.sha256 != expected_binary or not executable.mode & 0o100:
        raise NativeBundleError("inventory omits the pinned executable or its execute permission")
    if sum(record.size_bytes for record in files.values()) > MAX_TOTAL_BYTES:
        raise NativeBundleError("runtime inventory total size exceeds the bound")
    for path in used:
        for parent in PurePosixPath(path).parents:
            if str(parent) != "." and str(parent) not in directories:
                raise NativeBundleError("an inventory parent is absent or is a symlink")
    for alias in aliases.values():
        seen = {alias.path}
        destination = _alias_destination(alias.path, alias.target)
        for _ in range(MAX_ALIAS_HOPS):
            if destination in files:
                break
            if destination in seen or destination not in aliases:
                raise NativeBundleError("alias is cyclic, dangling or not a regular-file reference")
            seen.add(destination)
            next_alias = aliases[destination]
            destination = _alias_destination(next_alias.path, next_alias.target)
        else:
            raise NativeBundleError("alias chain exceeds the bound")
    return Inventory(
        root,
        _mode(document["root_mode"]),
        _integer(document["root_gid"], 2_147_483_647),
        files,
        directories,
        aliases,
    )


def _hash_descriptor(descriptor: int, expected_size: int) -> str:
    digest = hashlib.sha256()
    read_bytes = 0
    while True:
        block = os.read(descriptor, min(1_048_576, expected_size - read_bytes + 1))
        if not block:
            break
        read_bytes += len(block)
        if read_bytes > expected_size:
            raise NativeBundleError("runtime file grew during verification")
        digest.update(block)
    if read_bytes != expected_size:
        raise NativeBundleError("runtime file length changed during verification")
    return digest.hexdigest()


def _scan_tree(inventory: Inventory, *, verify_hashes: bool) -> dict[str, Fingerprint | str]:
    root_descriptor, ancestors = _open_absolute_directory(inventory.root)
    snapshot: dict[str, Fingerprint | str] = dict(ancestors)
    root_metadata = ancestors[inventory.root]
    if (
        stat.S_IMODE(root_metadata.mode) != inventory.root_mode
        or root_metadata.gid != inventory.root_gid
    ):
        os.close(root_descriptor)
        raise NativeBundleError("runtime root permissions differ from the inventory")
    actual: set[str] = set()

    def visit(descriptor: int, prefix: str) -> None:
        names = os.listdir(descriptor)
        if len(names) > MAX_TREE_ENTRIES:
            raise NativeBundleError("runtime tree entry count exceeds the bound")
        for name in sorted(names):
            path = prefix + name
            _safe_components(path)
            if len(actual) >= MAX_TREE_ENTRIES:
                raise NativeBundleError("runtime tree entry count exceeds the bound")
            actual.add(path)
            metadata = os.stat(name, dir_fd=descriptor, follow_symlinks=False)
            if path in inventory.directories:
                directory = inventory.directories[path]
                fingerprint = _protected(metadata, kind="directory")
                if (
                    stat.S_IMODE(fingerprint.mode) != directory.mode
                    or fingerprint.gid != directory.gid
                ):
                    raise NativeBundleError("directory permissions differ from the inventory")
                following = os.open(name, _directory_flags(), dir_fd=descriptor)
                try:
                    if _fingerprint(os.fstat(following)) != fingerprint:
                        raise NativeBundleError("runtime directory changed during traversal")
                    snapshot[inventory.root + "/" + path] = fingerprint
                    visit(following, path + "/")
                    if _fingerprint(os.fstat(following)) != fingerprint:
                        raise NativeBundleError(
                            "runtime directory metadata changed during verification"
                        )
                finally:
                    os.close(following)
            elif path in inventory.files:
                file = inventory.files[path]
                fingerprint = _protected(metadata, kind="file")
                if (
                    fingerprint.size != file.size_bytes
                    or stat.S_IMODE(fingerprint.mode) != file.mode
                    or fingerprint.gid != file.gid
                ):
                    raise NativeBundleError("file metadata differs from the inventory")
                source = os.open(name, _file_flags(), dir_fd=descriptor)
                try:
                    if _fingerprint(os.fstat(source)) != fingerprint:
                        raise NativeBundleError("runtime file changed before verification")
                    if verify_hashes and _hash_descriptor(source, file.size_bytes) != file.sha256:
                        raise NativeBundleError("runtime file digest mismatch")
                    if _fingerprint(os.fstat(source)) != fingerprint:
                        raise NativeBundleError("runtime file metadata changed during verification")
                    snapshot[inventory.root + "/" + path] = fingerprint
                finally:
                    os.close(source)
            elif path in inventory.aliases:
                alias = inventory.aliases[path]
                fingerprint = _protected(metadata, kind="alias")
                target = os.readlink(name, dir_fd=descriptor)
                if target != alias.target or fingerprint.gid != alias.gid:
                    raise NativeBundleError("alias identity differs from the inventory")
                if (
                    _fingerprint(os.stat(name, dir_fd=descriptor, follow_symlinks=False))
                    != fingerprint
                ):
                    raise NativeBundleError("alias metadata changed during verification")
                snapshot[inventory.root + "/" + path] = fingerprint
                snapshot["alias:" + path] = target
            else:
                raise NativeBundleError("runtime tree contains an unlisted object")

    try:
        visit(root_descriptor, "")
        if (
            actual
            != inventory.files.keys() | inventory.directories.keys() | inventory.aliases.keys()
        ):
            raise NativeBundleError("runtime tree is missing inventory objects")
        if _fingerprint(os.fstat(root_descriptor)) != root_metadata:
            raise NativeBundleError("runtime root metadata changed during verification")
        return snapshot
    finally:
        os.close(root_descriptor)


def verify_bundle(
    inventory_path: str,
    expected_inventory_sha256: str,
    *,
    candidate_binary_sha256: str | None = None,
) -> VerificationSummary:
    """Read-only identity check; candidate mode requires a separate external binary anchor.

    Omission preserves the original v1.0 contract. An explicit candidate anchor requires
    v1.1 and grants no permission to execute, select, install or accept the runtime.
    """
    _expected_binary_digest(candidate_binary_sha256)
    _require_posix_root()
    if _SHA256.fullmatch(expected_inventory_sha256) is None:
        raise NativeBundleError("external inventory SHA-256 is invalid")
    try:
        contents, inventory_before = _read_inventory(inventory_path, expected_inventory_sha256)
        inventory = _parse_inventory(contents, candidate_binary_sha256=candidate_binary_sha256)
        before = _scan_tree(inventory, verify_hashes=True)
        after = _scan_tree(inventory, verify_hashes=False)
        _, inventory_after = _read_inventory(inventory_path, expected_inventory_sha256)
        if before != after or inventory_before != inventory_after:
            raise NativeBundleError("tree or inventory metadata changed during verification")
    except (OSError, OverflowError) as error:
        raise NativeBundleError("protected filesystem verification failed") from error
    return VerificationSummary(
        len(inventory.files),
        len(inventory.directories),
        len(inventory.aliases),
        sum(record.size_bytes for record in inventory.files.values()),
        expected_inventory_sha256,
    )


def main(arguments: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", required=True, help="protected private JSON inventory path")
    parser.add_argument(
        "--inventory-sha256", required=True, help="separately trusted inventory SHA-256"
    )
    parser.add_argument(
        "--candidate-binary-sha256",
        help=(
            "independently trusted candidate binary SHA-256; "
            "requires a v1.1 inventory, not approval"
        ),
    )
    options = parser.parse_args(arguments)
    try:
        result = verify_bundle(
            options.inventory,
            options.inventory_sha256,
            candidate_binary_sha256=options.candidate_binary_sha256,
        )
    except NativeBundleError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        "PASS: protected runtime tree inventory verified; "
        f"files={result.file_count}; directories={result.directory_count}; "
        f"aliases={result.alias_count}; bytes={result.total_bytes}. No changes made."
    )
    print(f"NOT VERIFIED: {NOT_VERIFIED}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
