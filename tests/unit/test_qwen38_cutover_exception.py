"""The recorded quality exception never fabricates qualification or permissions."""

import copy
import json
from pathlib import Path
from typing import Any

import pytest
import yaml
from jsonschema import Draft202012Validator

from scripts.check_inference_artifacts import (
    QWEN38_OWNER_EXCEPTION,
    ArtifactValidationError,
    validate_qwen38_candidate,
)
from scripts.check_release_status import model_identity_errors, production_claim_errors

ROOT = Path(__file__).resolve().parents[2]


def test_exact_installed_source_suffix_does_not_allow_other_releases_or_source_mismatch() -> None:
    schema = json.loads((ROOT / "docs/status/release-status.schema.json").read_text())
    validator = Draft202012Validator(schema)
    status = yaml.safe_load((ROOT / "docs/status/current-release.yaml").read_text())
    assert not list(validator.iter_errors(status))
    for release, commit in (
        ("nextops-0.1.0-60605d8-arbitrary", "60605d8b98f13d01152fa95881919f01021df902"),
        ("nextops-0.1.0-60605d8-q38", "7ce9d2969d6bea8186783c5ce04a1c93be811a97"),
    ):
        changed = copy.deepcopy(status)
        changed["components"]["inference_api"] = {"release": release, "source_commit": commit}
        assert list(validator.iter_errors(changed))
    changed = copy.deepcopy(status)
    # Test the historical API-only suffix explicitly. A later ordinary matched app/API
    # release must not make this negative test depend on the current serving pair.
    changed["components"]["application"] = {
        "release": "nextops-0.1.0-60605d8-q38",
        "source_commit": "60605d8b98f13d01152fa95881919f01021df902",
    }
    assert list(validator.iter_errors(changed))


def candidate() -> dict[str, Any]:
    data = json.loads((ROOT / "deploy/inference/qwen3-8-27b-q8.candidate.json").read_text())
    assert isinstance(data, dict)
    data.update(
        status="controlled_selected_with_quality_exception",
        deployment_selection_allowed=True,
        owner_quality_exception=copy.deepcopy(QWEN38_OWNER_EXCEPTION),
    )
    return data


def selected(data: dict[str, Any]) -> dict[str, Any]:
    return {
        "identifier": data["model_id"],
        **{k: data[k] for k in ("source_revision", "quantization", "size_bytes", "sha256")},
    }


def test_exact_exception_records_selection_not_passing_semantics(tmp_path: Path) -> None:
    data = candidate()
    (tmp_path / "qwen3-8-27b-q8.candidate.json").write_text(json.dumps(data))
    validate_qwen38_candidate(tmp_path)
    assert data["qualification"]["standard_semantics"] == "failed"
    assert model_identity_errors(selected(data), {}, data) == []


@pytest.mark.parametrize(
    "field,value",
    [
        ("owner_quality_exception", None),
        ("deployment_selection_allowed", False),
        ("public_thinking_enabled", True),
        ("private_reasoning_persisted", True),
        ("max_active_requests", 2),
        ("max_queued_requests", 10),
        ("runtime_download_allowed", True),
        ("cpu_only_required", False),
        ("sha256", "0" * 64),
    ],
)
def test_exception_does_not_widen_safety_or_artifact_identity(
    tmp_path: Path, field: str, value: Any
) -> None:
    data = candidate()
    data[field] = value
    (tmp_path / "qwen3-8-27b-q8.candidate.json").write_text(json.dumps(data))
    with pytest.raises(ArtifactValidationError):
        validate_qwen38_candidate(tmp_path)


@pytest.mark.parametrize("field", tuple(QWEN38_OWNER_EXCEPTION))
def test_exception_is_not_a_generic_waiver(tmp_path: Path, field: str) -> None:
    data = candidate()
    del data["owner_quality_exception"][field]
    (tmp_path / "qwen3-8-27b-q8.candidate.json").write_text(json.dumps(data))
    with pytest.raises(ArtifactValidationError):
        validate_qwen38_candidate(tmp_path)
    assert model_identity_errors(selected(data), {}, data)


def test_failed_raw_results_cannot_be_laundered_to_passed(tmp_path: Path) -> None:
    data = candidate()
    data["qualification"]["standard_semantics"] = "passed"
    (tmp_path / "qwen3-8-27b-q8.candidate.json").write_text(json.dumps(data))
    with pytest.raises(ArtifactValidationError):
        validate_qwen38_candidate(tmp_path)
    assert model_identity_errors(selected(data), {}, data)


def test_exception_cannot_justify_production_even_if_other_gates_are_forged() -> None:
    status = {
        "components": {"model": selected(candidate())},
        "deployment_status": "production_accepted",
        "acceptance_gates": [{"id": "production_acceptance", "status": "passed"}],
        "current_application_qualification": {"gates": [{"status": "passed"}]},
    }
    assert any("owner-excepted" in e for e in production_claim_errors(status, True))


def test_native_profile_matches_bounded_standard_trial_and_preserves_base_sandbox() -> None:
    profiles = ROOT / "deploy/systemd/model-profiles"
    runtime = (profiles / "qwen3-8-27b-q8-runtime.conf").read_text()
    for expected in (
        "--threads 32",
        "--threads-batch 32",
        "--ubatch-size 512",
        "--ctx-size 16384",
        "--parallel 1",
        "--gpu-layers 0",
        "--host 127.0.0.1",
        "--api-key-file %d/llama-api-key",
        '"enable_thinking":false',
        '"preserve_thinking":false',
        "--no-reasoning-preserve",
        "--no-webui",
        "--no-slots",
        "--log-disable",
        "CPUQuota=3200%",
    ):
        assert expected in runtime
    for forbidden in (
        "IPAddressDeny=",
        "NoNewPrivileges=",
        "LoadCredential=",
        "User=",
        "MemoryMax=",
    ):
        assert forbidden not in runtime
    env = (profiles / "qwen3-8-27b-q8.env").read_text()
    assert "NEXTOPS_THINKING_ENABLED=0" in env
    assert "NEXTOPS_QWEN38_GREEDY_DECODING_ENABLED=1" in env
    assert "NEXTOPS_QWEN38_INSTRUCT_SAMPLING_ENABLED=0" in env
