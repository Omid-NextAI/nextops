"""Offline, fail-closed tests for runtime SBOM license evidence."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import zipfile
from pathlib import Path
from typing import Any

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from scripts.enrich_runtime_sbom import SbomEvidenceError, enrich_sbom  # noqa: E402


def _fixture(
    tmp_path: Path,
    *,
    declaration: str | None = "MIT",
    bundled_license: bool = True,
    legacy_field: bool = False,
) -> tuple[Path, Path, Path, Path]:
    wheelhouse = tmp_path / "wheels"
    wheelhouse.mkdir()
    wheel = wheelhouse / "sample_pkg-1.2.3-py3-none-any.whl"
    license_field = "License" if legacy_field else "License-Expression"
    header = (
        "Metadata-Version: 2.4\n"
        "Name: sample-pkg\n"
        "Version: 1.2.3\n" + (f"{license_field}: {declaration}\n" if declaration else "") + "\n"
    )
    with zipfile.ZipFile(wheel, "w") as archive:
        archive.writestr("sample_pkg-1.2.3.dist-info/METADATA", header)
        if bundled_license:
            archive.writestr("sample_pkg-1.2.3.dist-info/licenses/LICENSE", "sample license")
    digest = hashlib.sha256(wheel.read_bytes()).hexdigest()
    lock = tmp_path / "uv.lock"
    lock.write_text(
        "[[package]]\n"
        'name = "sample-pkg"\n'
        'version = "1.2.3"\n'
        "wheels = [\n"
        f'  {{ url = "https://example.invalid/{wheel.name}", hash = "sha256:{digest}" }},\n'
        "]\n",
        encoding="utf-8",
    )
    sbom = tmp_path / "runtime.cdx.json"
    sbom.write_text(
        json.dumps(
            {
                "bomFormat": "CycloneDX",
                "specVersion": "1.5",
                "version": 1,
                "components": [
                    {
                        "type": "library",
                        "name": "sample-pkg",
                        "version": "1.2.3",
                        "purl": "pkg:pypi/sample-pkg@1.2.3",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    return sbom, wheelhouse, lock, wheel


def test_enriches_verified_wheel_without_claiming_approval(tmp_path: Path) -> None:
    sbom, wheelhouse, lock, wheel = _fixture(tmp_path)

    result = enrich_sbom(sbom, wheelhouse, lock)

    component = result["components"][0]
    assert result["version"] == 2
    assert component["licenses"] == [{"expression": "MIT"}]
    assert component["hashes"] == [
        {"alg": "SHA-256", "content": hashlib.sha256(wheel.read_bytes()).hexdigest()}
    ]
    assert component["properties"] == [
        {"name": "nextops:license-declaration-source", "value": "unreviewed wheel METADATA"},
        {"name": "nextops:license-declaration-field", "value": "License-Expression"},
        {
            "name": "nextops:bundled-license-file",
            "value": "sample_pkg-1.2.3.dist-info/licenses/LICENSE",
        },
        {"name": "nextops:component-hash-object", "value": "staged wheel archive"},
    ]


def test_rejects_wheel_changed_after_lock(tmp_path: Path) -> None:
    sbom, wheelhouse, lock, wheel = _fixture(tmp_path)
    with wheel.open("ab") as stream:
        stream.write(b"changed")

    with pytest.raises(SbomEvidenceError, match="SHA-256 differs"):
        enrich_sbom(sbom, wheelhouse, lock)


def test_legacy_spdx_declaration_is_labeled(tmp_path: Path) -> None:
    sbom, wheelhouse, lock, _ = _fixture(tmp_path, legacy_field=True)

    result = enrich_sbom(sbom, wheelhouse, lock)

    assert {
        "name": "nextops:license-declaration-field",
        "value": "License",
    } in result["components"][0]["properties"]


@pytest.mark.parametrize(
    ("declaration", "bundled_license", "message"),
    [
        (None, True, "license declaration"),
        ("MIT", False, "bundled license text"),
        ("not a reviewable expression!", True, "expression shape"),
    ],
)
def test_rejects_missing_or_unreviewable_license(
    tmp_path: Path, declaration: str | None, bundled_license: bool, message: str
) -> None:
    sbom, wheelhouse, lock, _ = _fixture(
        tmp_path, declaration=declaration, bundled_license=bundled_license
    )

    with pytest.raises(SbomEvidenceError, match=message):
        enrich_sbom(sbom, wheelhouse, lock)


def test_rejects_sbom_wheel_set_mismatch(tmp_path: Path) -> None:
    sbom, wheelhouse, lock, _ = _fixture(tmp_path)
    document: dict[str, Any] = json.loads(sbom.read_text(encoding="utf-8"))
    document["components"][0]["version"] = "9.9.9"
    sbom.write_text(json.dumps(document), encoding="utf-8")

    with pytest.raises(SbomEvidenceError, match="no unique verified wheel"):
        enrich_sbom(sbom, wheelhouse, lock)


def test_rejects_overwriting_existing_license(tmp_path: Path) -> None:
    sbom, wheelhouse, lock, _ = _fixture(tmp_path)
    document: dict[str, Any] = json.loads(sbom.read_text(encoding="utf-8"))
    document["components"][0]["licenses"] = [{"expression": "Apache-2.0"}]
    sbom.write_text(json.dumps(document), encoding="utf-8")

    with pytest.raises(SbomEvidenceError, match="already has license"):
        enrich_sbom(sbom, wheelhouse, lock)


def test_cli_requires_private_new_output(tmp_path: Path) -> None:
    sbom, wheelhouse, lock, _ = _fixture(tmp_path)
    output = tmp_path / "enriched.cdx.json"
    command = [
        sys.executable,
        "scripts/enrich_runtime_sbom.py",
        "--sbom",
        str(sbom),
        "--wheelhouse",
        str(wheelhouse),
        "--lock",
        str(lock),
        "--output",
        str(output),
    ]
    first = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
    second = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)

    assert first.returncode == 0, first.stderr
    assert output.is_file()
    assert second.returncode != 0
    assert "File exists" in second.stderr
