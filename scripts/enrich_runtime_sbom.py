#!/usr/bin/env python3
"""Add unreviewed wheel license declarations to a private CycloneDX runtime SBOM.

This is a supply-chain evidence tool, not a license-policy decision or release signer.
It never downloads packages and never extracts wheel members to the filesystem.
"""

from __future__ import annotations

import argparse
import email
import hashlib
import io
import json
import re
import sys
import tomllib
import zipfile
import zlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MAX_WHEELS = 128
MAX_WHEEL_BYTES = 100_000_000
MAX_UNCOMPRESSED_BYTES = 250_000_000
MAX_METADATA_BYTES = 1_000_000
SPDX_SHAPE = re.compile(r"[A-Za-z0-9.+-]+(?: (?:AND|OR|WITH) [A-Za-z0-9.+-]+)*")
LEGACY_SPDX_VALUES = frozenset({"MIT", "Apache-2.0"})


class SbomEvidenceError(ValueError):
    """Raised when archive, lock, or SBOM evidence is missing or contradictory."""


@dataclass(frozen=True)
class WheelEvidence:
    name: str
    version: str
    sha256: str
    license_expression: str
    license_field: str
    license_file: str


def _normalized_name(value: str) -> str:
    return re.sub(r"[-_.]+", "-", value).lower()


def _read_bounded(path: Path, maximum: int) -> bytes:
    if not path.is_file() or path.stat().st_size > maximum:
        raise SbomEvidenceError(f"missing or oversized input: {path.name}")
    content = path.read_bytes()
    if len(content) > maximum:
        raise SbomEvidenceError(f"input grew past size limit: {path.name}")
    return content


def _locked_wheels(lock_path: Path) -> dict[str, tuple[str, str, str]]:
    try:
        lock = tomllib.loads(_read_bounded(lock_path, 10_000_000).decode("utf-8"))
    except (UnicodeError, tomllib.TOMLDecodeError) as error:
        raise SbomEvidenceError("cannot parse dependency lock") from error
    packages = lock.get("package")
    if not isinstance(packages, list):
        raise SbomEvidenceError("dependency lock has no package list")
    result: dict[str, tuple[str, str, str]] = {}
    for package in packages:
        if not isinstance(package, dict):
            raise SbomEvidenceError("invalid locked package")
        name, version = package.get("name"), package.get("version")
        if not isinstance(name, str) or not isinstance(version, str):
            raise SbomEvidenceError("locked package lacks name or version")
        for wheel in package.get("wheels", []):
            if not isinstance(wheel, dict):
                raise SbomEvidenceError("invalid locked wheel")
            url, digest = wheel.get("url"), wheel.get("hash")
            if not isinstance(url, str) or not isinstance(digest, str):
                raise SbomEvidenceError("locked wheel lacks URL or hash")
            filename = Path(urlsplit(url).path).name
            if not filename.endswith(".whl") or not re.fullmatch(r"sha256:[0-9a-f]{64}", digest):
                raise SbomEvidenceError("invalid locked wheel filename or SHA-256")
            record = (_normalized_name(name), version, digest.removeprefix("sha256:"))
            if filename in result and result[filename] != record:
                raise SbomEvidenceError(f"ambiguous locked wheel: {filename}")
            result[filename] = record
    return result


def _inspect_wheel(path: Path, expected: tuple[str, str, str]) -> WheelEvidence:
    wheel_bytes = _read_bounded(path, MAX_WHEEL_BYTES)
    actual_digest = hashlib.sha256(wheel_bytes).hexdigest()
    expected_name, expected_version, expected_digest = expected
    if actual_digest != expected_digest:
        raise SbomEvidenceError(f"wheel SHA-256 differs from lock: {path.name}")
    try:
        with zipfile.ZipFile(io.BytesIO(wheel_bytes)) as archive:
            members = archive.infolist()
            if (
                len(members) > 10_000
                or sum(item.file_size for item in members) > MAX_UNCOMPRESSED_BYTES
            ):
                raise SbomEvidenceError(f"oversized wheel contents: {path.name}")
            metadata = [
                item
                for item in members
                if item.filename.endswith(".dist-info/METADATA") and item.filename.count("/") == 1
            ]
            if len(metadata) != 1 or metadata[0].file_size > MAX_METADATA_BYTES:
                raise SbomEvidenceError(f"missing or ambiguous wheel metadata: {path.name}")
            prefix = metadata[0].filename.removesuffix("/METADATA")
            message = email.message_from_bytes(archive.read(metadata[0]))
            name, version = message.get("Name"), message.get("Version")
            if (
                not isinstance(name, str)
                or not isinstance(version, str)
                or _normalized_name(name) != expected_name
                or version != expected_version
            ):
                raise SbomEvidenceError(f"wheel metadata differs from lock: {path.name}")
            expression = message.get("License-Expression")
            license_field = "License-Expression"
            if not expression:
                legacy = message.get("License")
                if legacy not in LEGACY_SPDX_VALUES:
                    raise SbomEvidenceError(
                        f"wheel lacks a reviewable license declaration: {path.name}"
                    )
                expression = legacy
                license_field = "License"
            if len(expression) > 128 or SPDX_SHAPE.fullmatch(expression) is None:
                raise SbomEvidenceError(f"unsupported license expression shape: {path.name}")
            license_files = sorted(
                item.filename
                for item in members
                if item.filename.startswith(f"{prefix}/licenses/")
                and item.file_size > 0
                and Path(item.filename).name.lower().startswith(("license", "copying"))
            )
            if not license_files:
                raise SbomEvidenceError(f"wheel lacks bundled license text: {path.name}")
            if archive.testzip() is not None:
                raise SbomEvidenceError(f"wheel archive CRC failed: {path.name}")
    except (EOFError, OSError, RuntimeError, zipfile.BadZipFile, zlib.error) as error:
        raise SbomEvidenceError(f"cannot inspect wheel: {path.name}") from error
    return WheelEvidence(
        expected_name,
        expected_version,
        actual_digest,
        expression,
        license_field,
        license_files[0],
    )


def enrich_sbom(sbom_path: Path, wheelhouse: Path, lock_path: Path) -> dict[str, Any]:
    """Verify a one-to-one wheel/SBOM set and add source-labeled license evidence."""

    try:
        sbom = json.loads(_read_bounded(sbom_path, 10_000_000))
    except (UnicodeError, json.JSONDecodeError) as error:
        raise SbomEvidenceError("cannot parse CycloneDX SBOM") from error
    if not isinstance(sbom, dict) or sbom.get("bomFormat") != "CycloneDX":
        raise SbomEvidenceError("input is not a CycloneDX SBOM")
    if sbom.get("specVersion") != "1.5" or not isinstance(sbom.get("components"), list):
        raise SbomEvidenceError("expected a CycloneDX 1.5 component list")
    sbom_version = sbom.get("version", 1)
    if isinstance(sbom_version, bool) or not isinstance(sbom_version, int) or sbom_version < 1:
        raise SbomEvidenceError("invalid CycloneDX BOM version")
    if not wheelhouse.is_dir():
        raise SbomEvidenceError("wheelhouse directory is missing")
    paths = sorted(wheelhouse.iterdir())
    if not paths or len(paths) > MAX_WHEELS or any(path.suffix != ".whl" for path in paths):
        raise SbomEvidenceError("wheelhouse must contain only a bounded set of wheels")
    locked = _locked_wheels(lock_path)
    wheels: dict[tuple[str, str], WheelEvidence] = {}
    for path in paths:
        if path.name not in locked:
            raise SbomEvidenceError(f"wheel is absent from dependency lock: {path.name}")
        evidence = _inspect_wheel(path, locked[path.name])
        key = (evidence.name, evidence.version)
        if key in wheels:
            raise SbomEvidenceError(f"duplicate wheel identity: {evidence.name}")
        wheels[key] = evidence
    components = sbom["components"]
    if len(components) != len(wheels):
        raise SbomEvidenceError("SBOM and wheelhouse component counts differ")
    seen: set[tuple[str, str]] = set()
    for component in components:
        if not isinstance(component, dict):
            raise SbomEvidenceError("invalid SBOM component")
        name, version = component.get("name"), component.get("version")
        if not isinstance(name, str) or not isinstance(version, str):
            raise SbomEvidenceError("SBOM component lacks name or version")
        key = (_normalized_name(name), version)
        component_evidence = wheels.get(key)
        if component_evidence is None or key in seen:
            raise SbomEvidenceError(f"SBOM component has no unique verified wheel: {name}")
        seen.add(key)
        if component.get("purl") != f"pkg:pypi/{key[0]}@{version}":
            raise SbomEvidenceError(f"SBOM purl differs from wheel identity: {name}")
        if "licenses" in component or "hashes" in component:
            raise SbomEvidenceError(f"SBOM already has license or hash data: {name}")
        properties = component.setdefault("properties", [])
        if not isinstance(properties, list):
            raise SbomEvidenceError(f"invalid SBOM properties: {name}")
        component["licenses"] = [{"expression": component_evidence.license_expression}]
        component["hashes"] = [{"alg": "SHA-256", "content": component_evidence.sha256}]
        properties.extend(
            [
                {
                    "name": "nextops:license-declaration-source",
                    "value": "unreviewed wheel METADATA",
                },
                {
                    "name": "nextops:license-declaration-field",
                    "value": component_evidence.license_field,
                },
                {"name": "nextops:bundled-license-file", "value": component_evidence.license_file},
                {"name": "nextops:component-hash-object", "value": "staged wheel archive"},
            ]
        )
    sbom["version"] = sbom_version + 1
    return sbom


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sbom", type=Path, required=True)
    parser.add_argument("--wheelhouse", type=Path, required=True)
    parser.add_argument("--lock", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.is_relative_to(REPOSITORY_ROOT):
        print("FAIL: private SBOM output must be outside the repository", file=sys.stderr)
        return 1
    try:
        document = enrich_sbom(args.sbom, args.wheelhouse, args.lock)
        with output.open("x", encoding="utf-8") as stream:
            json.dump(document, stream, ensure_ascii=False, indent=2, sort_keys=True)
            stream.write("\n")
    except (OSError, SbomEvidenceError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(
        f"PASS: {len(document['components'])} wheel hashes and upstream license declarations "
        "added to a private SBOM; legal approval and release authenticity remain unverified."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
