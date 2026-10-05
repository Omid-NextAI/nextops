from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

import pytest
from jsonschema import Draft202012Validator

DIRECTORY = Path(__file__).resolve().parents[2] / "deploy/inference"


def manifest() -> dict[str, Any]:
    value = json.loads((DIRECTORY / "qwen3-8-flash-next-q8.candidate.json").read_text("utf-8"))
    assert isinstance(value, dict)
    return value


def validator() -> Draft202012Validator:
    return Draft202012Validator(
        json.loads((DIRECTORY / "model-flash-next-candidate.schema.json").read_text("utf-8"))
    )


def test_partial_sharded_candidate_is_not_selectable_or_customer_licensed() -> None:
    candidate = manifest()
    assert not list(validator().iter_errors(candidate))
    assert sum(s["size_bytes"] for s in candidate["shards"]) == candidate["total_size_bytes"]
    assert candidate["license"]["internal_use_exception_for_customer_deployment"] is False
    assert candidate["deployment_selection_allowed"] is False
    assert candidate["qualification"]["artifact_import"] != "passed"


@pytest.mark.parametrize(
    "field,value",
    [
        ("source_revision", "main"),
        ("upstream_reference_revision", "main"),
        ("total_size_bytes", 1),
        ("deployment_selection_allowed", True),
        ("public_thinking_enabled", True),
        ("runtime_download_allowed", True),
        ("gpu_layers", 1),
        ("max_active_requests", True),
        ("configured_context_tokens", 262144),
        ("deadline_seconds", 600),
    ],
)
def test_identity_and_boundaries_cannot_be_relaxed(field: str, value: object) -> None:
    candidate = manifest()
    candidate[field] = value
    assert list(validator().iter_errors(candidate))


def test_both_exact_shards_and_license_are_required() -> None:
    for field in ("shards", "license", "metadata"):
        candidate = copy.deepcopy(manifest())
        if field == "shards":
            candidate[field][1]["sha256"] = "0" * 64
        elif field == "license":
            candidate[field]["customer_deployment_review"] = "approved"
        else:
            candidate[field]["scope"] = "complete_model"
        assert list(validator().iter_errors(candidate))


def test_import_status_requires_complete_hash_not_a_metadata_shard() -> None:
    candidate = manifest()
    candidate["status"] = "verified_candidate_unselected"
    assert list(validator().iter_errors(candidate))
    candidate["qualification"]["artifact_import"] = "passed"
    assert not list(validator().iter_errors(candidate))
