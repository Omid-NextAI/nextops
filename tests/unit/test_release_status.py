"""Release/status manifest invariants."""

from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from types import ModuleType
from typing import Any
from unittest.mock import patch

import yaml
from jsonschema import Draft202012Validator

from nextops.inference.llama_cpp import THINKING_BUDGET_TOKENS

ROOT = Path(__file__).resolve().parents[2]


def _status_module() -> ModuleType:
    path = ROOT / "scripts" / "check_release_status.py"
    spec = importlib.util.spec_from_file_location("check_release_status", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _manifest() -> dict[str, Any]:
    result = yaml.safe_load((ROOT / "docs/status/current-release.yaml").read_text(encoding="utf-8"))
    assert isinstance(result, dict)
    return result


def test_release_status_manifest_is_valid_and_matches_ai_artifacts() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts/check_release_status.py")],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert "PASS:" in result.stdout


def test_retained_expanded_profile_is_not_misattributed_to_a_new_serving_model() -> None:
    status = _manifest()
    profile = json.loads((ROOT / "deploy/inference/expanded-chat-profile.json").read_text("utf-8"))
    assert profile["record_scope"] == "retained_35b_historical_qualification"
    assert profile["source_commit"] == "7ce9d2969d6bea8186783c5ce04a1c93be811a97"
    if status["components"]["model"]["identifier"] == profile["model_id"]:
        assert profile["source_commit"] == status["components"]["inference_api"]["source_commit"]
    else:
        assert status["components"]["model"]["identifier"] == "nextops-qwen3-8-27b-q8-0"
        candidate = json.loads(
            (ROOT / "deploy/inference/qwen3-8-27b-q8.candidate.json").read_text("utf-8")
        )
        assert candidate["status"] == "controlled_selected_with_quality_exception"
        assert (
            _status_module().model_identity_errors(status["components"]["model"], {}, candidate)
            == []
        )
        assert status["components"]["inference_api"]["source_commit"] == (
            "60605d8b98f13d01152fa95881919f01021df902"
        )
    assert profile["request_reasoning_budget_tokens"] == THINKING_BUDGET_TOKENS


def test_selected_model_identity_checks_all_fields_and_rejects_unqualified_selection() -> None:
    module = _status_module()
    baseline = yaml.safe_load((ROOT / "deploy/inference/qwen3-8b-q4-k-m.yaml").read_text("utf-8"))[
        "model"
    ]
    larger = json.loads(
        (ROOT / "deploy/inference/qwen3-14b-q4-k-m.candidate.json").read_text("utf-8")
    )
    larger_32b = json.loads(
        (ROOT / "deploy/inference/qwen3-32b-q4-k-m.candidate.json").read_text("utf-8")
    )
    larger_moe = json.loads(
        (ROOT / "deploy/inference/qwen3-30b-a3b-q4-k-m.candidate.json").read_text("utf-8")
    )
    larger_qwen35 = json.loads(
        (ROOT / "deploy/inference/qwen3-5-35b-a3b-q4-k-m.candidate.json").read_text("utf-8")
    )
    references = {
        item["model_id"]: item for item in (larger, larger_32b, larger_moe, larger_qwen35)
    }
    for artifact in (
        baseline,
        {**larger, "quantization": "Q4_K_M"},
        {**larger_32b, "quantization": "Q4_K_M"},
        {**larger_moe, "quantization": "Q4_K_M"},
        {**larger_qwen35, "quantization": "Q4_K_M"},
    ):
        reference = references.get(artifact["model_id"], larger)
        model = {
            "identifier": artifact["model_id"],
            **{
                key: artifact[key]
                for key in ("source_revision", "quantization", "size_bytes", "sha256")
            },
        }
        reviewed = {**reference, "status": "controlled_selected_not_production_accepted"}
        assert module.model_identity_errors(model, baseline, reviewed) == []
        for field, wrong in (
            ("source_revision", "0" * 40),
            ("quantization", "Q8_0"),
            ("size_bytes", 1),
            ("sha256", "0" * 64),
            ("identifier", "unreviewed-model"),
        ):
            assert module.model_identity_errors({**model, field: wrong}, baseline, reviewed)
        if artifact["model_id"] != baseline["model_id"]:
            assert module.model_identity_errors(
                model, baseline, {**reference, "status": "pinned_candidate_not_live_qualified"}
            )


def test_current_app_qualification_is_bound_to_serving_release() -> None:
    module = _status_module()
    status = _manifest()
    assert module.current_application_errors(status) == []

    mismatched_release = copy.deepcopy(status)
    mismatched_release["current_application_qualification"]["release"] = "nextops-0.1.0-deadbee"
    assert any(
        "release differs" in error
        for error in module.current_application_errors(mismatched_release)
    )

    mismatched_commit = copy.deepcopy(status)
    mismatched_commit["current_application_qualification"]["source_commit"] = "deadbee"
    assert any(
        "source_commit differs" in error
        for error in module.current_application_errors(mismatched_commit)
    )


def test_incomplete_semantic_review_is_not_recorded_as_production_acceptance() -> None:
    status = _manifest()
    current_gates = {
        gate["id"]: gate["status"] for gate in status["current_application_qualification"]["gates"]
    }
    release_gates = {gate["id"]: gate["status"] for gate in status["acceptance_gates"]}

    assert current_gates["current_app_held_out_answer_semantics"] in {"failed", "partial"}
    assert release_gates["answer_integrity_live"] in {"failed", "partial"}
    assert release_gates["production_acceptance"] == "not_run"


def test_current_app_qualification_requires_all_revision_sensitive_gates() -> None:
    module = _status_module()
    status = _manifest()
    status["current_application_qualification"]["gates"].pop()

    assert any(
        "missing or unexpected" in error for error in module.current_application_errors(status)
    )

    duplicate = _manifest()
    gates = duplicate["current_application_qualification"]["gates"]
    gates[-1] = copy.deepcopy(gates[0])
    assert any("must be unique" in error for error in module.current_application_errors(duplicate))


def test_schema_rejects_missing_or_invalid_candidate_qualification() -> None:
    schema = json.loads(
        (ROOT / "docs/status/release-status.schema.json").read_text(encoding="utf-8")
    )
    validator = Draft202012Validator(schema)
    status = _manifest()
    assert not list(validator.iter_errors(status))

    missing_candidate = copy.deepcopy(status)
    missing_candidate.pop("current_application_qualification")
    assert list(validator.iter_errors(missing_candidate))

    invalid_status = copy.deepcopy(status)
    invalid_status["current_application_qualification"]["gates"][0]["status"] = "assumed"
    assert list(validator.iter_errors(invalid_status))


def test_production_claim_rejects_blocked_recovery_and_current_release_gates() -> None:
    module = _status_module()
    status = _manifest()
    assert module.recovery_profile_qualified() is False
    assert module.production_claim_errors(status, False) == []

    for gate in status["acceptance_gates"]:
        if gate["id"] == "production_acceptance":
            gate["status"] = "passed"
    errors = module.production_claim_errors(status, False)
    assert any("deployment status" in error for error in errors)
    assert any("current-app gate" in error for error in errors)
    assert any("release gate" in error for error in errors)
    assert any("qualified recovery" in error for error in errors)


def test_unavailable_recovery_validator_fails_closed() -> None:
    module = _status_module()
    with patch.object(module.subprocess, "run", side_effect=OSError("unavailable")):
        assert module.recovery_profile_qualified() is False
    with patch.object(
        module.subprocess,
        "run",
        side_effect=subprocess.TimeoutExpired("check_recovery_profile.py", 30),
    ):
        assert module.recovery_profile_qualified() is False


def test_production_claim_requires_all_gates_even_with_asserted_recovery() -> None:
    module = _status_module()
    status = _manifest()
    status["deployment_status"] = "production_accepted"
    for gate in status["acceptance_gates"]:
        gate["status"] = "passed"

    errors = module.production_claim_errors(status, False)
    assert any("current-app gate" in error for error in errors)
    assert any("qualified recovery" in error for error in errors)

    assert any(
        "current-app gate" in error for error in module.production_claim_errors(status, True)
    )
    assert not any(
        "qualified recovery" in error for error in module.production_claim_errors(status, True)
    )

    for gate in status["current_application_qualification"]["gates"]:
        gate["status"] = "passed"
    # This in-memory predicate fixture does not call or bypass the real recovery validator.
    if status["components"]["model"]["identifier"] == "nextops-qwen3-8-27b-q8-0":
        assert any("owner-excepted" in e for e in module.production_claim_errors(status, True))
        # Exercise the generic gate policy with a hypothetical ordinary model, not acceptance
        # of today's owner-excepted Q8. Exact artifact selection is tested independently.
        status["components"]["model"]["identifier"] = "nextops-qwen3-5-35b-a3b-q4-k-m"
    assert module.production_claim_errors(status, True) == []


def test_production_acceptance_gate_cannot_be_omitted() -> None:
    module = _status_module()
    status = _manifest()
    status["acceptance_gates"] = [
        gate for gate in status["acceptance_gates"] if gate["id"] != "production_acceptance"
    ]

    assert module.production_claim_errors(status, False) == [
        "production_acceptance gate is missing"
    ]


def test_owner_recovery_deferral_is_explicit_and_cannot_be_reported_as_passed() -> None:
    module = _status_module()
    status = _manifest()
    assert module.deferred_recovery_errors(status) == []

    for gate in status["acceptance_gates"]:
        if gate["id"] == "independent_backup":
            gate["status"] = "passed"
        if gate["id"] == "production_acceptance":
            gate["status"] = "passed"
    errors = module.deferred_recovery_errors(status)
    assert any("independent_backup" in error for error in errors)
    assert any("full production acceptance" in error for error in errors)


def test_schema_requires_explicit_owner_recovery_scope() -> None:
    schema = json.loads(
        (ROOT / "docs/status/release-status.schema.json").read_text(encoding="utf-8")
    )
    validator = Draft202012Validator(schema)
    status = _manifest()
    assert not list(validator.iter_errors(status))

    status.pop("delivery_scope")
    assert list(validator.iter_errors(status))


def test_owner_snapshot_restore_attestation_is_not_qualified_recovery_evidence() -> None:
    schema = json.loads(
        (ROOT / "docs/status/release-status.schema.json").read_text(encoding="utf-8")
    )
    validator = Draft202012Validator(schema)
    status = _manifest()
    assert status["snapshot_restore_owner_attestation"]["evidence_review"] == "pending"
    assert not list(validator.iter_errors(status))

    missing = copy.deepcopy(status)
    missing.pop("snapshot_restore_owner_attestation")
    assert list(validator.iter_errors(missing))

    gate_status = {gate["id"]: gate["status"] for gate in status["acceptance_gates"]}
    assert gate_status["independent_backup"] == "partial"
    assert gate_status["isolated_restore"] == "partial"
    assert gate_status["production_acceptance"] == "not_run"
    assert _status_module().recovery_profile_qualified() is False
