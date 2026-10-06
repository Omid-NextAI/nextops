from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from scripts.review_model_trial import (
    CORPUS,
    protected_input,
    review,
    unique,
    write_report,
)


def entry(case_id: str, answer: str) -> dict[str, object]:
    return {"id": case_id, "answer": answer, "elapsed_ms": 1000, "finish_reason": "stop"}


def test_corpus_preserves_eight_regressions_and_paired_new_cases() -> None:
    corpus = json.loads(CORPUS.read_text("utf-8"))
    cases = corpus["cases"]
    assert len(cases) == 16 and len({case["id"] for case in cases}) == 16
    assert all(case["frozen_from"] == "2026-10-05-27b-trial" for case in cases[:8])
    frozen = json.dumps(
        [(case["id"], case["locale"], case["question"]) for case in cases[:8]],
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode()
    assert hashlib.sha256(frozen).hexdigest() == (
        "23209a5ef1ccfe02ffab8773772d9c1f1608b6fc37e3dd77548eabcd904b8943"
    )
    assert sum(case["locale"] == "en" for case in cases) == 8
    assert sum(case["locale"] == "fa" for case in cases) == 8
    assert corpus["deadline_seconds"] == 120 and corpus["standard_output_tokens"] == 384
    assert corpus["private_reasoning_persisted"] is False


def test_machine_pass_does_not_claim_acceptance_or_hide_missing_cases() -> None:
    result = review({"cases": [entry("fa-format", "\u06f0")]})
    assert result["cases"][0]["status"] == "passed"
    assert len(result["missing_cases"]) == 15
    assert result["status"] == "partial" and result["production_acceptance"] is False
    assert "answer" not in result["cases"][0]


def test_human_semantics_cannot_be_promoted_from_http_success() -> None:
    result = review({"cases": [entry("en-network", "An unsupported cause is invented here.")]})
    assert result["cases"][0]["status"] == "manual_review_required"
    assert result["status"] == "partial"


def test_frozen_coding_failure_and_context_deadline_remain_failed() -> None:
    coding = entry(
        "en-coding", 'def is_allowed(method):\n    return method in ("host.get", "item.get")'
    )
    late = {**entry("en-recall", "LAB-284"), "elapsed_ms": 120163}
    result = review({"cases": [coding, late]})
    assert result["status"] == "failed"
    assert all(case["status"] == "failed" for case in result["cases"])


@pytest.mark.parametrize(
    "field,value", [("error", "timeout"), ("finish_reason", "length"), ("finish_reason", None)]
)
def test_incomplete_result_cannot_be_an_exact_answer_pass(field: str, value: object) -> None:
    result = review({"cases": [{**entry("en-format", "0"), field: value}]})
    assert result["cases"][0]["status"] == "failed"


def test_unknown_duplicate_and_private_reasoning_entries_are_rejected() -> None:
    for entries in (
        [entry("unknown", "0")],
        [entry("en-format", "0")] * 2,
        [{**entry("en-format", "0"), "reasoning_content": "private text"}],
    ):
        with pytest.raises(ValueError):
            review({"cases": entries})
    with pytest.raises(ValueError, match="duplicate"):
        unique([("answer", "a"), ("answer", "b")])


def test_report_is_exclusive_and_does_not_overwrite_evidence(tmp_path: Path) -> None:
    tmp_path.chmod(0o700)
    output = tmp_path / "review.json"
    result = review({"cases": [entry("en-format", "0")]})
    write_report(output, result)
    assert protected_input(output) == result
    with pytest.raises(FileExistsError):
        write_report(output, result)


def test_report_input_is_bounded_and_cannot_be_inside_git(tmp_path: Path) -> None:
    path = tmp_path / "oversize.json"
    path.write_bytes(b"x" * 1_048_577)
    with pytest.raises(ValueError, match="private bounded"):
        protected_input(path)
    with pytest.raises(ValueError, match="private bounded"):
        protected_input(CORPUS)


def test_extended_report_does_not_silently_rewrite_frozen_deadline() -> None:
    late = {**entry("fa-hypothesis", "A hypothetical explanation."), "elapsed_ms": 150000}
    document = {
        "model_id": "nextops-qwen3-8-27b-ud-q5-k-m",
        "profile": {"deadline_seconds": 300},
        "cases": [late],
    }
    assert review(document)["cases"][0]["status"] == "failed"
    extended = review(document, deadline_seconds=300)
    assert extended["cases"][0]["status"] == "manual_review_required"
    assert extended["corpus_deadline_seconds"] == 120
    assert extended["review_deadline_seconds"] == 300
    assert extended["status"] == "partial" and len(extended["missing_cases"]) == 15
    assert extended["deployment_selection_allowed"] is False
    late["elapsed_ms"] = 300001
    assert review(document, deadline_seconds=300)["cases"][0]["status"] == "failed"


@pytest.mark.parametrize("model_id", [None, "remote-model", "nextops-qwen3-5-35b-a3b-q4-k-m"])
def test_extended_review_cannot_be_applied_to_unrelated_reports(model_id: str | None) -> None:
    with pytest.raises(ValueError, match=r"recorded Qwen3\.8"):
        review(
            {"model_id": model_id, "profile": {"deadline_seconds": 300}, "cases": []},
            deadline_seconds=300,
        )


@pytest.mark.parametrize("profile", [None, {}, {"deadline_seconds": 120}, "300"])
def test_extended_review_requires_matching_recorded_profile(profile: object) -> None:
    with pytest.raises(ValueError, match=r"recorded Qwen3\.8"):
        review(
            {"model_id": "nextops-qwen3-8-27b-q8-0", "profile": profile, "cases": []},
            deadline_seconds=300,
        )


@pytest.mark.parametrize("deadline", [0, 121, 600])
def test_arbitrary_deadline_cannot_hide_a_failed_result(deadline: int) -> None:
    with pytest.raises(ValueError, match="explicit 120- or 300-second"):
        review({"cases": []}, deadline_seconds=deadline)
