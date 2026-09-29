"""Selected local-inference artifact metadata validation tests."""

import json
import subprocess
import sys
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator

REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
MANIFEST = REPOSITORY_ROOT / "deploy" / "inference" / "qwen3-8b-q4-k-m.yaml"


@pytest.mark.parametrize("size,filename", [("14b", "14B"), ("30b-a3b", "30B-A3B")])
def test_larger_runtime_profile_changes_identity_without_weakening_the_base_unit(
    size: str, filename: str
) -> None:
    directory = REPOSITORY_ROOT / "deploy" / "systemd"
    original = (directory / "nextops-llama.service").read_text("utf-8")
    profile = (directory / "model-profiles" / f"qwen3-{size}-runtime.conf").read_text("utf-8")
    base_command = original.split("ExecStart=", 1)[1].split("\nRestart=", 1)[0].strip()
    expected = base_command.replace(
        "Qwen3-8B-Q4_K_M.gguf", f"Qwen3-{filename}-Q4_K_M.gguf"
    ).replace("nextops-qwen3-8b-q4-k-m", f"nextops-qwen3-{size}-q4-k-m")
    assert profile.split("ExecStart=\nExecStart=", 1)[1].strip() == expected
    assert "ConditionPathExists=\nConditionPathExists=" in profile
    assert (
        f"ConditionPathExists=/srv/nextops/models/current/Qwen3-{filename}-Q4_K_M.gguf" in profile
    )
    directives = [line for line in profile.splitlines() if "=" in line and not line.startswith("#")]
    assert len(directives) == 4


@pytest.mark.parametrize("size", ["14b", "30b-a3b"])
def test_larger_api_profile_requires_a_separate_exact_identity_file(size: str) -> None:
    directory = REPOSITORY_ROOT / "deploy" / "systemd" / "model-profiles"
    profile = (directory / f"qwen3-{size}-api.conf").read_text("utf-8")
    assert "EnvironmentFile=/etc/nextops/model-selection.env" in profile
    assert "EnvironmentFile=-" not in profile
    assert (directory / f"qwen3-{size}.env").read_text("utf-8").strip() == (
        f"NEXTOPS_MODEL_ID=nextops-qwen3-{size}-q4-k-m"
    )
    assert "Environment=" not in profile


@pytest.mark.parametrize("size", ["14b", "32b", "30b-a3b"])
def test_larger_candidate_is_pinned_without_runtime_download_or_acceptance_claim(size: str) -> None:
    directory = MANIFEST.parent
    candidate = json.loads((directory / f"qwen3-{size}-q4-k-m.candidate.json").read_text("utf-8"))
    schema_name = {
        "14b": "model-candidate.schema.json",
        "32b": "model-32b-candidate.schema.json",
        "30b-a3b": "model-30b-a3b-candidate.schema.json",
    }[size]
    schema = json.loads((directory / schema_name).read_text("utf-8"))
    validator = Draft202012Validator(schema)
    assert not list(validator.iter_errors(candidate))
    assert candidate["runtime_download_allowed"] is False
    assert candidate["cpu_only_required"] is True
    assert candidate["status"] in {
        "pinned_candidate_not_live_qualified",
        "controlled_selected_not_production_accepted",
    }
    for field, value in (
        ("sha256", "0" * 64),
        ("source_revision", "main"),
        ("runtime_download_allowed", True),
        ("max_active_requests", 2),
        ("source_repository", "https://unapproved.invalid/model"),
    ):
        assert list(validator.iter_errors({**candidate, field: value}))


def test_selected_artifact_manifest_is_human_readable_and_schema_valid() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/check_inference_artifacts.py"],
        cwd=REPOSITORY_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    assert "controlled_service_qualified_not_production_accepted" in result.stdout
    document = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    assert document["model"]["size_bytes"] == 5_027_783_488
    assert document["model"]["sha256"] == (
        "d98cdcbd03e17ce47681435b5150e34c1417f50b5c0019dd560e4882c5745785"
    )
    assert document["runtime"]["binary_sha256"] == (
        "dbe5a5cdd4842fe2d498270c1e1df58344e9052e97214e2ba9c9845443a1b0dc"
    )
    assert document["evidence"]["runtime_binary_built"] is True
    assert document["evidence"]["model_imported"] is True
    assert document["evidence"]["cpu_only_execution_verified"] is True
    assert document["evidence"]["controlled_service_installed"] is True
    assert document["evidence"]["application_source_commit"] == (
        "62de8d61fb4a841f016732815f75d95ca6c403a9"
    )
    assert document["evidence"]["authentication_readiness_verified"] is True
    assert document["evidence"]["bilingual_quality_review_passed"] is True
    assert document["evidence"]["bounded_load_run"] is True
    assert document["evidence"]["cold_process_restart_verified"] is True
    assert document["evidence"]["application_rollback_verified"] is True
    assert document["evidence"]["benchmark_run"] is False
    assert document["evidence"]["offline_cold_start_verified"] is True
