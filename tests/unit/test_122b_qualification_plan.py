from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts import prepare_122b_qualification as preparation
from scripts.review_model_trial import CORPUS, protected_input, write_report


def resources() -> dict[str, Any]:
    return {
        "sampled_at": "2026-10-05T12:00:00Z",
        "process_status": "VmRSS: 90000000 kB\n",
        "smaps_rollup": "Rss: 90000000 kB\nPss: 89000000 kB\nSwap: 0 kB\n",
        "meminfo": "MemTotal: 264094720 kB\nMemAvailable: 50000000 kB\n"
        "SwapTotal: 8388608 kB\nSwapFree: 8388608 kB\n",
        "memory_psi": "some avg10=0.00 avg60=0.00 avg300=0.00 total=100\n"
        "full avg10=0.00 avg60=0.00 avg300=0.00 total=50\n",
        "cpu_psi": "some avg10=0.50 avg60=0.25 avg300=0.10 total=1000\n",
        "cgroup_memory": {
            "current_bytes": 10 * preparation.GIB,
            "peak_bytes": 12 * preparation.GIB,
            "high_bytes": 112 * preparation.GIB,
            "max_bytes": 128 * preparation.GIB,
        },
        "baseline_readiness": {"ready": True, "active": 0, "queued": 0},
    }


def trial() -> dict[str, Any]:
    return {
        "model_id": preparation.MODEL_ID,
        "corpus_sha256": preparation.CORPUS_SHA256,
        "profile": {"threads": 32, "context_tokens": 16384, "mode": "standard"},
        "cases": [{"id": "en-format", "answer": "0", "elapsed_ms": 1000, "finish_reason": "stop"}],
    }


def test_plan_exact_corpus_identity_and_bounded_standard_first_ladder() -> None:
    plan = preparation.build_plan()
    assert plan["model_id"] == preparation.MODEL_ID
    assert plan["corpus_sha256"] == hashlib.sha256(CORPUS.read_bytes()).hexdigest()
    assert plan["frozen_eight_sha256"] == preparation.FROZEN_EIGHT_SHA256
    assert len(plan["frozen_cases"]) == 16
    assert [case["locale"] for case in plan["frozen_cases"]].count("fa") == 8
    assert plan["artifact_import_status"] in {"partial", "not_run", "failed", "passed"}
    assert plan["conversion_source_revision_verified"] is False
    assert plan["trial_budget_proposal_not_applied"]["memory_max_bytes"] == 128 * preparation.GIB
    assert plan["trial_budget_proposal_not_applied"]["request_deadline_seconds"] == 120
    assert plan["stages"][0]["mode"] == "standard"
    assert plan["stages"][0]["enable_thinking"] is False
    assert plan["stages"][1]["request_reasoning_budget_tokens"] == 128
    assert plan["stages"][2]["actual_template_input_token_floor"] == 14000
    assert "context_16k_en_fa_passed_and_new_headroom_review" in plan["stages"][3]["requires"]
    assert plan["status"] == "prepared_not_run"
    assert all(
        plan[field] is False
        for field in (
            "production_acceptance",
            "deployment_selection_allowed",
            "public_thinking_enabled",
            "private_reasoning_persisted",
            "runtime_download_allowed",
        )
    )
    assert len(plan["source_gaps_not_bypassed"]) == 5


def test_frozen_corpus_changes_require_explicit_repin(tmp_path: Path, monkeypatch: Any) -> None:
    changed = tmp_path / "changed.json"
    changed.write_bytes(CORPUS.read_bytes() + b"\n")
    monkeypatch.setattr(preparation, "CORPUS", changed)
    with pytest.raises(ValueError, match="repin"):
        preparation.corpus_document()


def test_resource_snapshot_preserves_real_units_and_cache_undercount_caveat() -> None:
    observed = preparation.review_resources(resources())
    assert observed["process_bytes"]["Pss"] == 89000000 * 1024
    assert observed["guest_memory_bytes"]["MemAvailable"] == 50000000 * 1024
    assert observed["cgroup_memory_bytes"]["peak_bytes"] == 12 * preparation.GIB
    assert observed["guest_memory_bytes"]["swap_used"] == 0
    assert observed["warnings"] == []
    assert observed["complete_memory_fit_accepted"] is False
    assert "undercount" in observed["limitations"][0]
    assert "not_additive" in observed["limitations"][1]
    assert "process_status" not in observed


def test_resource_pressure_and_baseline_degradation_are_visible_not_silenced() -> None:
    snapshot = resources()
    snapshot["baseline_readiness"]["ready"] = False
    snapshot["meminfo"] = (
        snapshot["meminfo"]
        .replace("50000000", "1000000")
        .replace("SwapFree: 8388608", "SwapFree: 7388608")
    )
    snapshot["memory_psi"] = snapshot["memory_psi"].replace("full avg10=0.00", "full avg10=1.00")
    result = preparation.review_resources(snapshot)
    assert len(result["warnings"]) == 4
    assert result["status"] == "observed_not_accepted"
    assert result["deployment_selection_allowed"] is False


@pytest.mark.parametrize(
    "field,value",
    [
        ("sampled_at", "2026-10-05T12:00:00"),
        ("process_status", "VmRSS: 1 kB\nVmRSS: 2 kB"),
        ("process_status", "Name: private-process\nVmRSS: 1 kB"),
        ("process_status", "VmRSS: 17179869185 kB"),
        ("smaps_rollup", "Rss: 1 kB\nPss: 2 kB\nSwap: 0 kB"),
        ("memory_psi", "some avg10=101.00 avg60=0.00 avg300=0.00 total=1"),
        ("memory_psi", "full avg10=0.00 avg60=0.00 avg300=0.00 total=1"),
        ("cpu_psi", "some avg10=NaN avg60=0.00 avg300=0.00 total=1"),
    ],
)
def test_malformed_or_unsanitized_resource_snapshots_rejected(field: str, value: Any) -> None:
    snapshot = resources()
    snapshot[field] = value
    with pytest.raises(ValueError):
        preparation.review_resources(snapshot)


def test_snapshot_extra_fields_wrong_types_and_memory_inconsistency_rejected() -> None:
    for mutation in ("secret", "bool_counter", "readiness_string", "invalid_free"):
        snapshot = resources()
        if mutation == "secret":
            snapshot["credential"] = "must not persist"
        elif mutation == "bool_counter":
            snapshot["cgroup_memory"]["max_bytes"] = True
        elif mutation == "readiness_string":
            snapshot["baseline_readiness"]["ready"] = "true"
        else:
            snapshot["meminfo"] = snapshot["meminfo"].replace(
                "SwapFree: 8388608", "SwapFree: 9388608"
            )
        with pytest.raises(ValueError):
            preparation.review_resources(snapshot)


def test_trial_finite_pass_not_application_or_semantic_acceptance() -> None:
    result = preparation.review_trial(trial())
    assert result["cases"][0]["status"] == "passed"
    assert result["status"] == "partial" and len(result["missing_cases"]) == 15
    assert result["production_acceptance"] is False
    assert result["public_thinking_enabled"] is False
    assert "answer" not in result["cases"][0]


def test_trial_preserves_timeout_failure_and_no_raw_answers() -> None:
    document = trial()
    document["cases"][0]["elapsed_ms"] = 120102
    result = preparation.review_trial(document)
    assert result["cases"][0]["status"] == "failed"
    assert result["status"] == "failed"
    assert "0" not in json.dumps(result["cases"])


def test_coding_reuses_ast_invariant_without_running_generated_code() -> None:
    document = trial()
    cases = preparation.corpus_document()["cases"][:7]
    document["cases"] = [
        {
            "id": case["id"],
            "answer": case.get("expected", "Manual review required."),
            "elapsed_ms": 1000,
            "finish_reason": "stop",
        }
        for case in cases
    ]
    document["cases"][-1]["answer"] = (
        'def is_allowed(method):\n    return method in ("host.get", "item.get")'
    )
    result = preparation.review_trial(document)
    assert result["cases"][-1]["status"] == "failed"
    assert "equality_spoof" in result["cases"][-1]["failed_cases"]


def test_trial_wrong_identity_order_profile_and_private_reasoning_rejected() -> None:
    for mutation in ("model", "corpus", "order", "thinking", "context", "bool", "secret"):
        document = copy.deepcopy(trial())
        if mutation == "model":
            document["model_id"] = "nextops-qwen3-5-35b-a3b-q4-k-m"
        elif mutation == "corpus":
            document["corpus_sha256"] = "0" * 64
        elif mutation == "order":
            document["cases"][0]["id"] = "fa-format"
        elif mutation == "thinking":
            document["cases"][0]["reasoning_content"] = "private"
        elif mutation == "context":
            document["profile"]["context_tokens"] = 32768
        elif mutation == "bool":
            document["profile"]["threads"] = True
        else:
            document["key"] = "must not persist"
        with pytest.raises(ValueError):
            preparation.review_trial(document)


@pytest.mark.parametrize("mode", ["standard", "final_only_thinking"])
def test_final_answer_reuses_adapter_guard_against_private_drafts(mode: str) -> None:
    document = trial()
    document["profile"]["mode"] = mode
    document["cases"][0]["answer"] = "<think>private draft</think>0"
    with pytest.raises(ValueError):
        preparation.review_trial(document)


def test_thinking_finite_review_still_cannot_approve_thinking() -> None:
    document = trial()
    document["profile"]["mode"] = "final_only_thinking"
    result = preparation.review_trial(document)
    assert result["cases"][0]["status"] == "passed"
    assert result["status"] == "partial"
    assert result["public_thinking_enabled"] is False


def test_cli_failed_trial_returns_failure_without_overwriting_protected_evidence(
    tmp_path: Path, monkeypatch: Any
) -> None:
    tmp_path.chmod(0o700)
    input_path, output = tmp_path / "trial.json", tmp_path / "failed-review.json"
    document = trial()
    document["cases"][0]["elapsed_ms"] = 120102
    write_report(input_path, document)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "prepare_122b_qualification",
            "--output",
            str(output),
            "--trial",
            str(input_path),
        ],
    )
    assert preparation.main() == 1
    result = protected_input(output)
    assert result["finite_trial_review"]["status"] == "failed"
    assert result["deployment_selection_allowed"] is False


def test_cli_only_private_exclusive_report_and_no_selection(
    tmp_path: Path, monkeypatch: Any
) -> None:
    tmp_path.chmod(0o700)
    output = tmp_path / "plan.json"
    monkeypatch.setattr(sys, "argv", ["prepare_122b_qualification", "--output", str(output)])
    assert preparation.main() == 2
    plan = protected_input(output)
    assert plan["deployment_selection_allowed"] is False
    with pytest.raises(FileExistsError):
        preparation.main()
