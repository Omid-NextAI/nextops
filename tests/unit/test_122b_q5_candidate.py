from __future__ import annotations

import copy
import importlib.util
import json
import shutil
from pathlib import Path
from typing import Any

import pytest
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "deploy/inference"
FILENAME = "qwen3-5-122b-a10b-q5-k-m.candidate.json"


def manifest() -> dict[str, Any]:
    value = json.loads((DIRECTORY / FILENAME).read_text("utf-8"))
    assert isinstance(value, dict)
    return value


def validator() -> Draft202012Validator:
    schema = json.loads((DIRECTORY / "model-122b-a10b-q5-candidate.schema.json").read_text("utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def artifact_module() -> Any:
    spec = importlib.util.spec_from_file_location(
        "candidate_artifact_check", ROOT / "scripts/check_inference_artifacts.py"
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_q5_is_a_pinned_unselected_alternative_not_a_live_upgrade() -> None:
    candidate = manifest()
    assert not list(validator().iter_errors(candidate))
    assert sum(shard["size_bytes"] for shard in candidate["shards"]) == 90429454752
    assert candidate["status"] == "provisioning_unselected"
    assert candidate["conversion_source_revision_verified"] is False
    assert candidate["deployment_selection_allowed"] is False
    assert candidate["public_thinking_enabled"] is False
    assert candidate["qualification"]["permissive_license_metadata_review"] == "passed"
    assert candidate["qualification"]["artifact_import"] == "partial"
    assert all(
        value == "not_run"
        for gate, value in candidate["qualification"].items()
        if gate not in {"permissive_license_metadata_review", "artifact_import"}
    )


@pytest.mark.parametrize(
    "field,value",
    [
        ("model_id", "nextops-qwen3-8-122b"),
        ("status", "accepted"),
        ("source_revision", "main"),
        ("upstream_reference_revision", "main"),
        ("conversion_source_revision_verified", True),
        ("total_size_bytes", 1),
        ("deployment_selection_allowed", True),
        ("public_thinking_enabled", True),
        ("private_reasoning_persisted", True),
        ("runtime_download_allowed", True),
        ("cpu_only_required", False),
        ("gpu_layers", 1),
        ("gpu_layers", False),
        ("max_active_requests", True),
        ("max_queued_requests", 3),
        ("configured_context_tokens", 262144),
        ("max_output_tokens", 32768),
        ("request_reasoning_budget_tokens", 4096),
        ("deadline_seconds", 600),
    ],
)
def test_q5_identity_and_safety_bounds_are_immutable(field: str, value: object) -> None:
    candidate = manifest()
    candidate[field] = value
    assert list(validator().iter_errors(candidate))


@pytest.mark.parametrize("field", ["shards", "license", "qualification"])
def test_q5_rejects_changed_nested_identity_and_ambiguous_gates(field: str) -> None:
    candidate = copy.deepcopy(manifest())
    if field == "shards":
        candidate[field][2]["sha256"] = "0" * 64
    elif field == "license":
        candidate[field]["sha256"] = "0" * 64
    else:
        candidate[field]["cpu_load"] = "assumed_passed"
    assert list(validator().iter_errors(candidate))


@pytest.mark.parametrize("field", list(manifest()))
def test_q5_requires_every_field(field: str) -> None:
    candidate = manifest()
    del candidate[field]
    assert list(validator().iter_errors(candidate))


def test_q5_rejects_extra_fields_and_shard_substitution() -> None:
    candidate = manifest()
    candidate["cloud_fallback"] = True
    assert list(validator().iter_errors(candidate))
    candidate = manifest()
    candidate["shards"] = candidate["shards"][:2]
    assert list(validator().iter_errors(candidate))
    candidate = manifest()
    candidate["qualification"]["unreviewed_gate"] = "passed"
    assert list(validator().iter_errors(candidate))


def test_q5_import_status_needs_complete_artifact_and_never_enables_selection() -> None:
    candidate = manifest()
    candidate["status"] = "verified_candidate_unselected"
    assert list(validator().iter_errors(candidate))
    candidate["qualification"]["artifact_import"] = "passed"
    assert not list(validator().iter_errors(candidate))
    candidate["deployment_selection_allowed"] = True
    assert list(validator().iter_errors(candidate))
    candidate["deployment_selection_allowed"] = False
    candidate["status"] = "provisioning_unselected"
    assert list(validator().iter_errors(candidate))


def test_repository_validator_checks_q5_and_duplicate_keys(tmp_path: Path) -> None:
    copied = tmp_path / "deploy/inference"
    shutil.copytree(DIRECTORY, copied)
    module = artifact_module()
    module.validate_repository(tmp_path)
    path = copied / FILENAME
    original = path.read_text("utf-8")
    path.write_text(original.replace('"status":', '"status": "accepted", "status":', 1), "utf-8")
    with pytest.raises(module.ArtifactValidationError, match="duplicate"):
        module.validate_repository(tmp_path)
    candidate = manifest()
    candidate["deployment_selection_allowed"] = True
    path.write_text(json.dumps(candidate), "utf-8")
    with pytest.raises(module.ArtifactValidationError, match="schema validation"):
        module.validate_repository(tmp_path)


def test_original_q4_research_and_failed_27b_are_preserved() -> None:
    research = json.loads((DIRECTORY / "qwen3-5-122b-a10b-research.json").read_text("utf-8"))
    assert research["quantization"] == "Q4_K_M"
    assert research["total_size_bytes"] == 77616511296
    assert research["download_verified"] is False
    assert research["deployment_selection_allowed"] is False
    failed = json.loads((DIRECTORY / "qwen3-8-27b-q8.candidate.json").read_text("utf-8"))
    assert failed["qualification"]["standard_semantics"] == "failed"
    assert failed["qualification"]["latency_resource_comparison"] == "failed"
    assert failed["public_thinking_enabled"] is False
