"""Prepare/review the pinned 122B CPU trial offline; never run or select a model."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from datetime import datetime
from pathlib import Path
from typing import Any

from nextops.inference.contracts import FinishReason
from nextops.inference.llama_cpp import _final_answer
from scripts.check_inference_artifacts import validate_repository
from scripts.review_model_trial import CORPUS, ROOT, protected_input, review, unique, write_report

MODEL_ID = "nextops-qwen3-5-122b-a10b-q5-k-m"
MANIFEST = ROOT / "deploy/inference/qwen3-5-122b-a10b-q5-k-m.candidate.json"
CORPUS_SHA256 = "5e6a1973d77c2c9b3c94bed41686b77a7dd31b2abe86a8e8cb3991c9c1b24f40"
FROZEN_EIGHT_SHA256 = "23209a5ef1ccfe02ffab8773772d9c1f1608b6fc37e3dd77548eabcd904b8943"
GIB = 1024**3


def corpus_document() -> dict[str, Any]:
    raw = CORPUS.read_bytes()
    if hashlib.sha256(raw).hexdigest() != CORPUS_SHA256:
        raise ValueError("qualification corpus changed; review and repin explicitly")
    document: dict[str, Any] = json.loads(raw, object_pairs_hook=unique)
    frozen = json.dumps(
        [(case["id"], case["locale"], case["question"]) for case in document["cases"][:8]],
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode()
    if hashlib.sha256(frozen).hexdigest() != FROZEN_EIGHT_SHA256:
        raise ValueError("the historical eight-case regression identity changed")
    return document


def build_plan() -> dict[str, Any]:
    """Source preparation is not execution authority, artifact proof or acceptance."""
    validate_repository(ROOT)
    manifest = json.loads(MANIFEST.read_text("utf-8"), object_pairs_hook=unique)
    corpus = corpus_document()
    return {
        "scope": "offline_source_preparation_not_execution_or_model_acceptance",
        "status": "prepared_not_run",
        "model_id": MODEL_ID,
        "manifest_sha256": hashlib.sha256(MANIFEST.read_bytes()).hexdigest(),
        "artifact_import_status": manifest["qualification"]["artifact_import"],
        "conversion_source_revision_verified": manifest["conversion_source_revision_verified"],
        "corpus_sha256": CORPUS_SHA256,
        "frozen_eight_sha256": FROZEN_EIGHT_SHA256,
        "runtime_commit": manifest["runtime_commit"],
        "cpu_only_required": True,
        "gpu_layers": 0,
        "runtime_download_allowed": False,
        "production_acceptance": False,
        "deployment_selection_allowed": False,
        "public_thinking_enabled": False,
        "private_reasoning_persisted": False,
        "trial_budget_proposal_not_applied": {
            "memory_high_bytes": 112 * GIB,
            "memory_max_bytes": 128 * GIB,
            "thread_cpu_quota_ladder": [32, 48],
            "retained_baseline_memory_max_bytes": 96 * GIB,
            "max_active_requests": 1,
            "max_queued_requests": 2,
            "request_deadline_seconds": 120,
            "stop_on_failure_no_automatic_retry": True,
        },
        "execution_prerequisites_not_inferred": [
            "all_three_complete_shards_size_and_full_sha256_verified",
            "actual_gguf_architecture_template_tokenizer_and_pinned_cpu_runtime_verified",
            "protected_license_attribution_and_conversion_caveat_recorded",
            "explicit_authorized_isolated_change_window_and_exact_35b_rollback",
            "baseline_ready_idle_and_global_resource_headroom_observed",
            "complete_process_and_guest_memory_observed_not_cgroup_peak_alone",
        ],
        "stages": [
            {
                "id": "standard_frozen_en_fa",
                "mode": "standard",
                "context_tokens": 16384,
                "output_tokens": corpus["standard_output_tokens"],
                "enable_thinking": False,
                "case_ids": [case["id"] for case in corpus["cases"]],
                "requires": ["execution_prerequisites_not_inferred"],
            },
            {
                "id": "final_only_thinking_frozen_en_fa",
                "mode": "final_only_thinking",
                "context_tokens": 16384,
                "output_tokens": corpus["thinking_output_tokens"],
                "request_reasoning_budget_tokens": corpus["reasoning_budget_tokens"],
                "case_ids": [case["id"] for case in corpus["cases"]],
                "requires": ["all_standard_cases_finite_and_manual_semantic_review_passed"],
                "final_answer_contract": "strict_answer_only_json_no_private_drafts",
            },
            {
                "id": "context_16k_en_fa",
                "context_tokens": 16384,
                "actual_template_input_token_floor": 14000,
                "max_output_tokens": 2048,
                "locales": ["en", "fa"],
                "requires": ["standard_and_thinking_semantics_privacy_and_resources_passed"],
                "checks": [
                    "actual_apply_template_and_tokenize_not_character_estimate",
                    "early_and_latest_identifiers_recalled_without_truncation",
                    "actual_input_plus_reserved_output_within_context",
                    "120_second_deadline_and_global_resource_bounds",
                ],
            },
            {
                "id": "context_32k_en_fa",
                "context_tokens": 32768,
                "actual_template_input_token_floor": 28672,
                "max_output_tokens": 2048,
                "locales": ["en", "fa"],
                "requires": ["context_16k_en_fa_passed_and_new_headroom_review"],
                "checks": ["same_token_recall_deadline_privacy_and_resource_checks_as_16k"],
            },
        ],
        "frozen_cases": corpus["cases"],
        "required_measurements": [
            "monotonic_elapsed_ms_and_actual_prompt_completion_token_counts",
            "process_VmRSS_smaps_rollup_Rss_Pss_Swap",
            "cgroup_memory_current_peak_high_max_and_events",
            "guest_MemTotal_MemAvailable_SwapTotal_SwapFree",
            "memory_and_cpu_PSI_some_full_avg10_and_total_deltas",
            "baseline_readiness_active_and_queued_requests_before_during_after",
        ],
        "source_capabilities_implemented_not_runtime_accepted": [
            "register_exact_122b_ModelId_in_typed_inference_contracts_and_tests",
            "add_reviewed_122b_hard_template_controls_standard_first_not_soft_no_think",
            "propagate_actual_model_label_through_existing_API_UI_contracts",
        ],
        "source_gaps_not_bypassed": [
            "add_bounded_candidate_runtime_profile_and_exact_identity_installer_checks",
            "retain_122b_thinking_default_denial_until_qualified_candidate_path_review",
        ],
        "remaining_after_native_trials": [
            "matched_application_authorization_owner_scoped_chat_and_final_only_privacy",
            "fresh_authorized_evidence_provenance_audit_stale_partial_absent_injection",
            "bounded_queue_dependency_failure_and_recovery",
            "actual_WAN_isolated_new_generation_restart_and_applicable_cold_start",
            "exact_runtime_model_rollback_and_reapply",
        ],
    }


def _fields(value: Any, fields: set[str], label: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != fields:
        raise ValueError(f"{label} fields must match the bounded snapshot contract")
    return value


def _integer(value: Any, label: str) -> int:
    if type(value) is not int or not 0 <= value <= 16 * 1024**4:
        raise ValueError(f"{label} must be a bounded nonnegative integer")
    return value


def _kib_excerpt(value: Any, required: set[str]) -> dict[str, int]:
    if not isinstance(value, str) or not 0 < len(value) <= 16384:
        raise ValueError("proc excerpt must be bounded text")
    result: dict[str, int] = {}
    for line in value.splitlines():
        match = re.fullmatch(r"([A-Za-z_]+):\s+(\d+)\s+kB", line.strip())
        if match is None or match[1] not in required or match[1] in result:
            raise ValueError("snapshot accepts only requested, unique kB observations")
        result[match[1]] = _integer(int(match[2]) * 1024, match[1])
    if set(result) != required:
        raise ValueError("snapshot is missing required kB observations")
    return result


def _psi(value: Any) -> dict[str, dict[str, float | int]]:
    if not isinstance(value, str) or not 0 < len(value) <= 2048:
        raise ValueError("PSI excerpt must be bounded text")
    result: dict[str, dict[str, float | int]] = {}
    for line in value.splitlines():
        match = re.fullmatch(
            r"(some|full) avg10=(\d+(?:\.\d+)?) avg60=(\d+(?:\.\d+)?) "
            r"avg300=(\d+(?:\.\d+)?) total=(\d+)",
            line.strip(),
        )
        if match is None or match[1] in result:
            raise ValueError("invalid or duplicate PSI observation")
        averages = [float(match[index]) for index in (2, 3, 4)]
        if any(not math.isfinite(value) or not 0 <= value <= 100 for value in averages):
            raise ValueError("PSI percentage is outside its range")
        result[match[1]] = dict(
            zip(("avg10", "avg60", "avg300"), averages, strict=True),
            total_us=_integer(int(match[5]), "PSI total"),
        )
    if "some" not in result:
        raise ValueError("PSI some observation is missing")
    return result


def review_resources(document: dict[str, Any]) -> dict[str, Any]:
    """Normalize sanitized excerpts only; a snapshot does not prove complete memory fit."""
    _fields(
        document,
        {
            "sampled_at",
            "process_status",
            "smaps_rollup",
            "meminfo",
            "memory_psi",
            "cpu_psi",
            "cgroup_memory",
            "baseline_readiness",
        },
        "resource",
    )
    if not isinstance(document["sampled_at"], str) or len(document["sampled_at"]) > 64:
        raise ValueError("sampled_at must be a bounded aware timestamp")
    sampled = datetime.fromisoformat(document["sampled_at"])
    if sampled.tzinfo is None:
        raise ValueError("sampled_at must include timezone")
    status = _kib_excerpt(document["process_status"], {"VmRSS"})
    rollup = _kib_excerpt(document["smaps_rollup"], {"Rss", "Pss", "Swap"})
    memory = _kib_excerpt(
        document["meminfo"], {"MemTotal", "MemAvailable", "SwapTotal", "SwapFree"}
    )
    if memory["MemAvailable"] > memory["MemTotal"] or memory["SwapFree"] > memory["SwapTotal"]:
        raise ValueError("guest memory counters are inconsistent")
    if rollup["Pss"] > rollup["Rss"]:
        raise ValueError("process PSS cannot exceed the supplied RSS")
    cgroup = _fields(
        document["cgroup_memory"],
        {"current_bytes", "peak_bytes", "high_bytes", "max_bytes"},
        "cgroup",
    )
    counters = {key: _integer(value, key) for key, value in cgroup.items()}
    baseline = _fields(document["baseline_readiness"], {"ready", "active", "queued"}, "baseline")
    if type(baseline["ready"]) is not bool:
        raise ValueError("baseline readiness must be boolean")
    active, queued = _integer(baseline["active"], "active"), _integer(baseline["queued"], "queued")
    memory_psi, cpu_psi = _psi(document["memory_psi"]), _psi(document["cpu_psi"])
    warnings = []
    if not baseline["ready"] or active or queued:
        warnings.append("baseline_not_ready_idle_at_observation")
    if counters["high_bytes"] != 112 * GIB or counters["max_bytes"] != 128 * GIB:
        warnings.append("observed_cgroup_limits_differ_from_trial_proposal")
    if memory["MemAvailable"] < 16 * GIB:
        warnings.append("below_proposed_16_GiB_global_available_memory_guard")
    if memory["SwapTotal"] != memory["SwapFree"] or rollup["Swap"]:
        warnings.append("swap_used_at_observation_requires_delta_review")
    if memory_psi.get("full", {}).get("avg10", 0) > 0:
        warnings.append("global_full_memory_pressure_observed")
    if "full" not in memory_psi:
        warnings.append("global_full_memory_pressure_observation_missing")
    if counters["current_bytes"] > counters["high_bytes"]:
        warnings.append("observed_cgroup_memory_above_high")
    return {
        "scope": "supplied_sanitized_snapshot_not_live_probe_or_memory_fit_acceptance",
        "status": "observed_not_accepted",
        "sampled_at": sampled.isoformat(),
        "process_bytes": {"vm_rss": status["VmRSS"], **rollup},
        "guest_memory_bytes": {**memory, "swap_used": memory["SwapTotal"] - memory["SwapFree"]},
        "cgroup_memory_bytes": counters,
        "memory_psi": memory_psi,
        "cpu_psi": cpu_psi,
        "baseline_readiness": {"ready": baseline["ready"], "active": active, "queued": queued},
        "warnings": warnings,
        "proposed_guard_not_approved_acceptance_threshold_bytes": 16 * GIB,
        "complete_memory_fit_accepted": False,
        "deployment_selection_allowed": False,
        "limitations": [
            "precharged_mmap_page_cache_can_undercount_cgroup_peak",
            "RSS_PSS_cgroup_and_guest_counters_are_not_additive",
            "single_snapshot_is_not_peak_or_pressure_swap_delta_or_sustained_observation",
            "baseline_readiness_is_supplied_observation_not_current_remote_state",
        ],
    }


def review_trial(document: dict[str, Any]) -> dict[str, Any]:
    _fields(document, {"model_id", "corpus_sha256", "profile", "cases"}, "trial")
    if document["model_id"] != MODEL_ID or document["corpus_sha256"] != CORPUS_SHA256:
        raise ValueError("trial model/corpus identity does not match the pinned candidate")
    corpus = corpus_document()
    profile = _fields(document["profile"], {"threads", "context_tokens", "mode"}, "profile")
    if (
        type(profile["threads"]) is not int
        or profile["threads"] not in (32, 48)
        or type(profile["context_tokens"]) is not int
        or profile["context_tokens"] != 16384
        or profile["mode"] not in ("standard", "final_only_thinking")
    ):
        raise ValueError("finite corpus review requires the bounded 16K/32-or-48-thread profile")
    entries = document["cases"]
    if not isinstance(entries, list) or not 1 <= len(entries) <= 16:
        raise ValueError("cases must be a bounded nonempty fixed-order prefix")
    for entry, expected in zip(entries, corpus["cases"], strict=False):
        if not isinstance(entry, dict) or entry.get("id") != expected["id"]:
            raise ValueError("trial case order differs from the frozen corpus")
        if set(entry) - {"id", "answer", "elapsed_ms", "finish_reason", "error"}:
            raise ValueError("trial accepts final-answer fields only, not private reasoning")
        answer = entry.get("answer")
        if isinstance(answer, str) and entry.get("finish_reason") == "stop":
            # Reuse the application adapter's final-only guard, not a second privacy parser.
            thinking = profile["mode"] == "final_only_thinking"
            _final_answer(
                json.dumps({"answer": answer}) if thinking else answer,
                thinking=thinking,
                finish_reason=FinishReason.STOP,
            )
    result = review({"cases": entries})
    result.update(model_id=MODEL_ID, profile=profile, public_thinking_enabled=False)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--resources", type=Path)
    parser.add_argument("--trial", type=Path)
    args = parser.parse_args()
    result = build_plan()
    if args.resources is not None:
        result["resource_observation"] = review_resources(protected_input(args.resources))
    if args.trial is not None:
        result["finite_trial_review"] = review_trial(protected_input(args.trial))
    write_report(args.output, result)
    print("qualification_plan=prepared_not_run; no model called, accepted or selected")
    return 1 if result.get("finite_trial_review", {}).get("status") == "failed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
