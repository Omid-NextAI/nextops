from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

import pytest

from scripts.check_inference_artifacts import (
    ArtifactValidationError,
    validate_qwen38_q5_candidate,
    validate_repository,
)

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "deploy/inference"
FILENAME = "qwen3-8-27b-ud-q5-k-m.candidate.json"


def candidate() -> dict[str, Any]:
    value: dict[str, Any] = json.loads((DIRECTORY / FILENAME).read_text("utf-8"))
    return value


def write(directory: Path, document: dict[str, Any]) -> None:
    (directory / FILENAME).write_text(json.dumps(document), "utf-8")


def test_q5_is_a_distinct_unselected_pinned_precision_experiment() -> None:
    validate_qwen38_q5_candidate(DIRECTORY)
    value = candidate()
    assert value["size_bytes"] == 19771509664
    assert value["status"] == "verified_candidate_unselected"
    assert value["qualification"]["artifact_import"] == "passed"
    assert value["qualification"]["actual_gguf_metadata"] == "passed"
    assert value["qualification"]["cpu_load"] == "passed"
    assert value["qualification"]["standard_semantics"] == "failed"
    assert value["qualification"]["thinking_semantics_privacy"] == "not_run"
    assert value["qualification"]["matched_application"] == "not_run"
    assert value["conversion_source_revision_verified"] is False
    assert value["deployment_selection_allowed"] is value["public_thinking_enabled"] is False
    previous = json.loads((DIRECTORY / "qwen3-8-27b-q8.candidate.json").read_text("utf-8"))
    assert previous["qualification"]["standard_semantics"] == "failed"
    assert previous["qualification"]["latency_resource_comparison"] == "failed"


@pytest.mark.parametrize(
    "field,value",
    [
        ("model_id", "nextops-qwen3-8-27b-q8-0"),
        ("source_revision", "main"),
        ("upstream_reference_revision", "main"),
        ("size_bytes", True),
        ("sha256", "0" * 64),
        ("license", "Qwen-Community"),
        ("license_sha256", "0" * 64),
        ("conversion_source_revision_verified", True),
        ("cpu_only_required", False),
        ("gpu_layers", False),
        ("gpu_layers", 1),
        ("runtime_download_allowed", True),
        ("deployment_selection_allowed", True),
        ("public_thinking_enabled", True),
        ("private_reasoning_persisted", True),
        ("configured_context_tokens", 262144),
        ("request_reasoning_budget_tokens", 4096),
        ("deadline_seconds", 600),
        ("max_active_requests", True),
        ("max_queued_requests", 99),
        ("status", []),
        ("status", "live"),
    ],
)
def test_q5_rejects_identity_and_safety_mutations(
    tmp_path: Path, field: str, value: object
) -> None:
    document = candidate()
    document[field] = value
    write(tmp_path, document)
    with pytest.raises(ArtifactValidationError):
        validate_qwen38_q5_candidate(tmp_path)


@pytest.mark.parametrize("field", list(candidate()))
def test_q5_requires_all_fields(tmp_path: Path, field: str) -> None:
    document = candidate()
    del document[field]
    write(tmp_path, document)
    with pytest.raises(ArtifactValidationError):
        validate_qwen38_q5_candidate(tmp_path)


def test_complete_import_needs_exact_verified_status_but_never_enables_selection(
    tmp_path: Path,
) -> None:
    document = candidate()
    document["status"] = "verified_candidate_unselected"
    # Construct the partial state explicitly: the maintained candidate can advance.
    document["qualification"]["artifact_import"] = "partial"
    write(tmp_path, document)
    with pytest.raises(ArtifactValidationError, match="state is ambiguous"):
        validate_qwen38_q5_candidate(tmp_path)
    document["qualification"]["artifact_import"] = "passed"
    write(tmp_path, document)
    validate_qwen38_q5_candidate(tmp_path)
    document["deployment_selection_allowed"] = True
    write(tmp_path, document)
    with pytest.raises(ArtifactValidationError):
        validate_qwen38_q5_candidate(tmp_path)


@pytest.mark.parametrize("import_gate", ["partial", "failed", "not_run"])
def test_partial_import_requires_provisioning_status_without_inheriting_acceptance(
    tmp_path: Path, import_gate: str
) -> None:
    document = candidate()
    document["status"] = "provisioning_unselected"
    document["qualification"]["artifact_import"] = import_gate
    write(tmp_path, document)
    validate_qwen38_q5_candidate(tmp_path)
    document["status"] = "verified_candidate_unselected"
    write(tmp_path, document)
    with pytest.raises(ArtifactValidationError, match="state is ambiguous"):
        validate_qwen38_q5_candidate(tmp_path)


def test_complete_import_cannot_retain_provisioning_status(tmp_path: Path) -> None:
    document = candidate()
    document["status"] = "provisioning_unselected"
    document["qualification"]["artifact_import"] = "passed"
    write(tmp_path, document)
    with pytest.raises(ArtifactValidationError, match="state is ambiguous"):
        validate_qwen38_q5_candidate(tmp_path)


@pytest.mark.parametrize("mutation", ["extra", "unknown_gate", "invalid_gate", "license_gate"])
def test_q5_rejects_unreviewed_fields_and_ambiguous_gates(tmp_path: Path, mutation: str) -> None:
    document = candidate()
    if mutation == "extra":
        document["cloud_fallback"] = True
    elif mutation == "unknown_gate":
        document["qualification"]["marketing_score"] = "passed"
    elif mutation == "invalid_gate":
        document["qualification"]["standard_semantics"] = True
    else:
        document["qualification"]["permissive_license_metadata_review"] = "not_run"
    write(tmp_path, document)
    with pytest.raises(ArtifactValidationError):
        validate_qwen38_q5_candidate(tmp_path)


def test_repository_checks_q5_and_rejects_duplicate_json_fields(tmp_path: Path) -> None:
    directory = tmp_path / "deploy/inference"
    shutil.copytree(DIRECTORY, directory)
    validate_repository(tmp_path)
    original = (directory / FILENAME).read_text("utf-8")
    (directory / FILENAME).write_text(
        original.replace('"status":', '"status": "live", "status":', 1), "utf-8"
    )
    with pytest.raises(ArtifactValidationError, match=r"cannot parse Qwen3\.8 Q5"):
        validate_repository(tmp_path)
