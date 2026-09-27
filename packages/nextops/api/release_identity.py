"""Bounded, offline digest of the installed NextOps package or a candidate wheel.

This identifies package bytes served by an application process. It is not an artifact
signature, host attestation, dependency inventory, or proof of answer correctness.
"""

from __future__ import annotations

import hashlib
import stat
from pathlib import Path, PurePosixPath
from zipfile import BadZipFile, ZipFile

MAX_FILES = 256
MAX_FILE_BYTES = 5_000_000
MAX_TOTAL_BYTES = 20_000_000
MAX_WHEEL_BYTES = 30_000_000
HEADER_NAME = "X-NextOps-App-Code-SHA256"
_DOMAIN = b"nextops-app-code-tree-v1\0"
_REQUIRED = frozenset({"api/app.py", "api/static/index.html"})


class CodeDigestError(ValueError):
    """The package tree is ambiguous, incomplete, or outside its read budget."""


def _valid_name(name: str) -> bool:
    normalized = PurePosixPath(name)
    parts = normalized.parts
    return (
        bool(parts)
        and name == normalized.as_posix()
        and not normalized.is_absolute()
        and "\\" not in name
        and all(part not in ("", ".", "..", "__pycache__") for part in parts)
    )


def _include(name: str) -> bool:
    return not name.endswith(".pyc") and "__pycache__" not in PurePosixPath(name).parts


def _digest(entries: list[tuple[str, bytes]]) -> str:
    if not 1 <= len(entries) <= MAX_FILES:
        raise CodeDigestError("package file count is outside the bounded range")
    names = [name for name, _ in entries]
    if len(names) != len(set(names)) or not _REQUIRED.issubset(names):
        raise CodeDigestError("package files are duplicate or required files are missing")
    total = 0
    digest = hashlib.sha256()
    digest.update(_DOMAIN)
    for name, content in sorted(entries):
        if not _valid_name(name) or len(content) > MAX_FILE_BYTES:
            raise CodeDigestError("package file name or size is invalid")
        total += len(content)
        if total > MAX_TOTAL_BYTES:
            raise CodeDigestError("package contents exceed the read budget")
        encoded_name = name.encode("utf-8")
        digest.update(len(encoded_name).to_bytes(4, "big"))
        digest.update(encoded_name)
        digest.update(len(content).to_bytes(8, "big"))
        digest.update(hashlib.sha256(content).digest())
    return digest.hexdigest()


def installed_code_digest(package_root: Path) -> str:
    """Hash actual package source/assets at process start, excluding bytecode caches."""

    if not package_root.is_dir() or package_root.is_symlink():
        raise CodeDigestError("installed package root is unavailable or linked")
    entries: list[tuple[str, bytes]] = []
    for path in package_root.rglob("*"):
        name = path.relative_to(package_root).as_posix()
        if not _include(name):
            continue
        mode = path.lstat().st_mode
        if stat.S_ISLNK(mode):
            raise CodeDigestError("installed package contains a linked path")
        if stat.S_ISDIR(mode):
            continue
        if not stat.S_ISREG(mode):
            raise CodeDigestError("installed package contains a nonregular file")
        if path.stat().st_size > MAX_FILE_BYTES:
            raise CodeDigestError("installed package file exceeds the read budget")
        with path.open("rb") as stream:
            content = stream.read(MAX_FILE_BYTES + 1)
        entries.append((name, content))
        if len(entries) > MAX_FILES:
            raise CodeDigestError("installed package contains too many files")
    return _digest(entries)


def wheel_code_digest(wheel_path: Path) -> str:
    """Hash matching package members in a wheel without extracting it or using a network."""

    if not wheel_path.is_file() or wheel_path.is_symlink():
        raise CodeDigestError("wheel is unavailable or linked")
    if wheel_path.stat().st_size > MAX_WHEEL_BYTES:
        raise CodeDigestError("wheel exceeds the read budget")
    entries: list[tuple[str, bytes]] = []
    try:
        with ZipFile(wheel_path) as wheel:
            for member in wheel.infolist():
                if not member.filename.startswith("nextops/") or member.is_dir():
                    continue
                name = member.filename.removeprefix("nextops/")
                if not _include(name):
                    continue
                if member.file_size > MAX_FILE_BYTES:
                    raise CodeDigestError("wheel member exceeds the read budget")
                member_type = (member.external_attr >> 16) & 0o170000
                if member_type not in (0, stat.S_IFREG):
                    raise CodeDigestError("wheel package member is not a regular file")
                with wheel.open(member) as stream:
                    content = stream.read(MAX_FILE_BYTES + 1)
                entries.append((name, content))
                if len(entries) > MAX_FILES:
                    raise CodeDigestError("wheel contains too many package files")
    except (BadZipFile, OSError) as error:
        raise CodeDigestError("wheel cannot be read") from error
    return _digest(entries)
