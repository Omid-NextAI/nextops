"""Offline review of sanitized private trial reports; never calls or selects a model."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
from pathlib import Path
from typing import Any

from scripts.check_model_coding_invariant import check

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "deploy/inference/model-qualification-corpus.json"
MAX_REPORT_BYTES = 1_048_576


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate review field")
        result[key] = value
    return result


def review(document: dict[str, Any]) -> dict[str, Any]:
    corpus_bytes = CORPUS.read_bytes()
    corpus = json.loads(corpus_bytes, object_pairs_hook=unique)
    cases = {case["id"]: case for case in corpus["cases"]}
    entries = document.get("cases")
    if not isinstance(entries, list) or not 1 <= len(entries) <= len(cases):
        raise ValueError("trial cases must be a bounded non-empty list")
    seen: set[str] = set()
    findings = []
    for entry in entries:
        if not isinstance(entry, dict) or "reasoning_content" in entry or "analysis" in entry:
            raise ValueError("raw private reasoning is not an accepted review input")
        case_id = entry.get("id")
        if not isinstance(case_id, str) or case_id not in cases or case_id in seen:
            raise ValueError("unknown or duplicated trial case")
        seen.add(case_id)
        expected = cases[case_id]
        finding: dict[str, Any] = {"id": case_id, "status": "not_run"}
        answer = entry.get("answer")
        elapsed = entry.get("elapsed_ms")
        if type(elapsed) is not int or elapsed < 0:
            raise ValueError("trial requires measured nonnegative integer elapsed_ms")
        if elapsed > 120_000 or entry.get("error") or entry.get("finish_reason") == "length":
            finding.update(status="failed", reason="deadline_transport_or_truncation")
        elif entry.get("finish_reason") != "stop":
            finding.update(status="failed", reason="missing_completed_final_answer")
        elif not isinstance(answer, str) or not 0 < len(answer) <= 16_000:
            raise ValueError("trial requires a bounded final answer")
        elif expected["review"] == "exact":
            normalized = answer.strip().translate(str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789"))
            finding["status"] = "passed" if normalized == expected["expected"] else "failed"
        elif expected["review"] == "bounded_coding_ast":
            finding.update(check(answer))
        else:
            finding.update(status="manual_review_required", criteria=expected["criteria"])
        findings.append(finding)
    return {
        "scope": "offline_finite_checks_not_model_or_application_acceptance",
        "corpus_sha256": hashlib.sha256(corpus_bytes).hexdigest(),
        "canonical_input_sha256": hashlib.sha256(
            json.dumps(document, sort_keys=True, ensure_ascii=False).encode()
        ).hexdigest(),
        "status": "failed" if any(f["status"] == "failed" for f in findings) else "partial",
        "production_acceptance": False,
        "deployment_selection_allowed": False,
        "private_reasoning_persisted": False,
        "cases": findings,
        "missing_cases": sorted(set(cases) - seen),
        "unrun_gates": ["matched_application", "expanded_context", "wan_offline", "rollback"],
    }


def protected_input(path: Path) -> dict[str, Any]:
    metadata = path.lstat()
    if (
        not path.is_absolute()
        or path.resolve().is_relative_to(ROOT)
        or not stat.S_ISREG(metadata.st_mode)
        or metadata.st_size > MAX_REPORT_BYTES
        or (os.name == "posix" and metadata.st_mode & 0o077)
    ):
        raise ValueError("input must be a private bounded regular file outside Git")
    value = json.loads(path.read_text("utf-8"), object_pairs_hook=unique)
    if not isinstance(value, dict):
        raise ValueError("trial report must be an object")
    return value


def write_report(path: Path, document: dict[str, Any]) -> None:
    if (
        not path.is_absolute()
        or path.resolve().is_relative_to(ROOT)
        or path.parent.is_symlink()
        or not path.parent.is_dir()
        or (os.name == "posix" and path.parent.stat().st_mode & 0o077)
    ):
        raise ValueError("output must be private and outside Git")
    descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
        json.dump(document, stream, ensure_ascii=False, indent=2)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = review(protected_input(args.input))
    write_report(args.output, result)
    print(f"review_status={result['status']}; no model called or selected")
    return 1 if result["status"] == "failed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
