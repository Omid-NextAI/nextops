"""Boundaries for the private exact-release semantic-review capture tool."""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
from pathlib import Path
from types import ModuleType
from typing import Any

import pytest

ROOT = Path(__file__).resolve().parents[2]


def _module() -> ModuleType:
    path = ROOT / "scripts/evaluate_live_app_semantics.py"
    spec = importlib.util.spec_from_file_location("evaluate_live_app_semantics", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _case(**updates: str) -> dict[str, str]:
    case = {
        "id": "EN-FILES-01",
        "mode": "incident",
        "locale": "en",
        "question": "Only show system files.",
        "target_id": "app",
    }
    case.update(updates)
    return case


def test_semantic_review_corpus_is_bounded_and_requires_explicit_routes() -> None:
    module = _module()
    assert module.validate_cases({"cases": [_case()]})[0]["target_id"] == "app"
    assert (
        module.validate_cases(
            {
                "cases": [
                    _case(
                        expected_answer_focus="filesystems",
                        required_limitation="read_only_no_action_performed",
                    )
                ]
            }
        )[0]["expected_answer_focus"]
        == "filesystems"
    )
    assert (
        module.validate_cases({"cases": [_case(mode="general", target_id="")]})[0]["mode"]
        == "general"
    )

    invalid_cases: tuple[dict[str, Any], ...] = (
        {"cases": []},
        {"cases": [_case(), _case()]},
        {"cases": [_case(mode="shell")]},
        {"cases": [_case(target_id="../app")]},
        {"cases": [{**_case(), "target_id": None}]},
        {"cases": [_case(question=" ")]},
        {"cases": [_case(expected_answer_focus="unknown")]},
        {"cases": [_case(mode="general", target_id="", expected_answer_focus="filesystems")]},
        {"cases": [_case(expected_integrity_status="unknown")]},
        {"cases": [_case(required_limitation="bad value")]},
        {"cases": [_case(required_answer_fragment="x" * 161)]},
        {"cases": [{**_case(), "unexpected": "ignored"}]},
        {"cases": [_case()] * 13},
    )
    for invalid in invalid_cases:
        with pytest.raises(ValueError):
            module.validate_cases(invalid)


def test_semantic_review_restricts_credentials_to_private_https_origin() -> None:
    module = _module()
    assert module.validate_private_https_origin("https://192.168.1.10/") == "https://192.168.1.10"
    assert module.validate_private_https_origin("https://nextops.local") == "https://nextops.local"
    for invalid in (
        "http://192.168.1.10",
        "https://example.com",
        "https://user:secret@192.168.1.10",
        "https://192.168.1.10/path",
        "https://192.168.1.10/?key=secret",
    ):
        with pytest.raises(ValueError):
            module.validate_private_https_origin(invalid)


def test_semantic_review_private_report_is_not_overwritten(tmp_path: Path) -> None:
    module = _module()
    report = tmp_path / "semantic-review.json"
    module.write_private_report(report, {"manual_semantic_review_required": True})
    assert json.loads(report.read_text(encoding="utf-8"))["manual_semantic_review_required"]
    if os.name == "posix":
        assert report.stat().st_mode & 0o777 == 0o600
    with pytest.raises(FileExistsError):
        module.write_private_report(report, {})
    with pytest.raises(ValueError, match="absolute"):
        module.write_private_report(Path("relative.json"), {})
    with pytest.raises(ValueError, match="outside the repository"):
        module.write_private_report(ROOT / "uncommitted-review.json", {})


def test_semantic_review_redirects_are_rejected() -> None:
    module = _module()
    assert module.NoRedirect().redirect_request(None, None, None, None, None) is None


def test_semantic_review_rejects_invalid_expected_code_digest_before_network(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    module = _module()
    monkeypatch.setattr(
        module,
        "parse_args",
        lambda: argparse.Namespace(expected_app_code_sha256="not-a-digest"),
    )
    with pytest.raises(ValueError, match="SHA-256"):
        module.main()


def test_semantic_review_flags_bounded_response_mismatches_without_claiming_truth() -> None:
    module = _module()
    case = _case(
        expected_answer_focus="filesystems",
        expected_integrity_status="deterministic_focus",
        required_limitation="file_listing_unavailable",
        required_answer_fragment="filesystem",
        forbidden_answer_fragment="CPU idle time",
    )
    result = {
        "status": 200,
        "body": {
            "answer_focus": "overview",
            "assistant": {
                "answer": "Generic CPU idle time",
                "integrity_status": "deterministic_fallback",
                "limitations": [],
            },
        },
    }
    checks = module.check_case_expectations(case, result)
    assert checks == {
        "status": "failed",
        "failures": [
            "answer_focus",
            "integrity_status",
            "required_limitation",
            "required_answer_fragment",
            "forbidden_answer_fragment",
        ],
    }
    assert module.check_case_expectations(_case(), result)["status"] == "not_configured"
    assert module.check_case_expectations(case, {"status": 503})["failures"] == ["http_status"]
    echo = _case(required_answer_fragment="Only show system files")
    assert module.check_case_expectations(
        echo, {"status": 200, "body": {"assistant": {"answer": echo["question"]}}}
    ) == {"status": "failed", "failures": ["prompt_echo"]}
    assert (
        module.check_case_expectations(
            _case(), {"status": 200, "body": {"assistant": {"answer": "Only show system files."}}}
        )["status"]
        == "failed"
    )
    greeting = _case(
        mode="general",
        target_id="",
        forbidden_answer_fragment="Zabbix",
    )
    assert (
        module.check_case_expectations(greeting, {"status": 200, "body": {"answer": "Hello!"}})[
            "status"
        ]
        == "passed"
    )
    persian = _case(
        mode="general",
        target_id="",
        locale="fa",
        forbidden_answer_fragment="زبیکس",
    )
    assert (
        module.check_case_expectations(persian, {"status": 200, "body": {"answer": "سلام!"}})[
            "status"
        ]
        == "passed"
    )
    assert module.summarize_expectations(["passed", "passed"]) == "passed"
    assert module.summarize_expectations(["passed", "not_configured"]) == "partial"
    assert module.summarize_expectations(["not_configured"]) == "not_configured"
    assert module.summarize_expectations(["passed", "failed"]) == "failed"


@pytest.mark.parametrize(
    ("expected_focus", "observed_digest", "expected_exit"),
    [
        ("file_listing", "a" * 64, 0),
        ("filesystems", "a" * 64, 1),
        (None, "a" * 64, 1),
        ("file_listing", "b" * 64, 1),
        ("file_listing", "", 1),
    ],
)
def test_semantic_review_captures_an_authenticated_case_and_logs_out(
    expected_focus: str | None,
    observed_digest: str,
    expected_exit: int,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    module = _module()
    endpoint = tmp_path / "endpoint.txt"
    login = tmp_path / "login.txt"
    corpus = tmp_path / "corpus.json"
    output = tmp_path / "report.json"
    endpoint.write_text("url: https://nextops.local\n", encoding="utf-8")
    login.write_text("username: reviewer\npassword: " + "x" * 32 + "\n", encoding="utf-8")
    expectation: dict[str, str] = (
        {"expected_answer_focus": expected_focus} if expected_focus is not None else {}
    )
    corpus.write_text(json.dumps({"cases": [_case(**expectation)]}), encoding="utf-8")
    if os.name == "posix":
        for path in (endpoint, login, corpus):
            path.chmod(0o600)

    requests: list[tuple[str, dict[str, str], str | None]] = []

    class FakeResponse:
        def __init__(
            self, status: int, body: dict[str, Any] | None, headers: dict[str, str] | None = None
        ) -> None:
            self.status = status
            self.body = json.dumps(body).encode() if body is not None else b""
            self.headers = headers or {}

        def __enter__(self) -> FakeResponse:
            return self

        def __exit__(self, *_args: Any) -> None:
            return None

        def read(self, _size: int) -> bytes:
            return self.body

    class FakeOpener:
        def open(self, request: Any, *, timeout: int) -> FakeResponse:
            assert timeout == 120
            payload = json.loads(request.data)
            auth = request.get_header("Authorization")
            requests.append((request.full_url, payload, auth))
            if request.full_url.endswith("/login"):
                return FakeResponse(200, {"session": {"access_token": "t" * 40}})
            if request.full_url.endswith("/logout"):
                return FakeResponse(204, None)
            return FakeResponse(
                200,
                {
                    "assistant": {"answer": "Only system files."},
                    "answer_focus": "file_listing",
                    "evidence": [],
                },
                {module.CODE_DIGEST_HEADER: observed_digest} if observed_digest else {},
            )

    monkeypatch.setattr(
        module,
        "parse_args",
        lambda: argparse.Namespace(
            endpoint_file=endpoint,
            login_file=login,
            ca_file=tmp_path / "ca.pem",
            corpus=corpus,
            output=output,
            expected_release="nextops-0.1.0-01755d1",
            expected_app_code_sha256="a" * 64,
        ),
    )
    monkeypatch.setattr(module.ssl, "create_default_context", lambda **_kwargs: object())
    monkeypatch.setattr(module, "build_opener", lambda *_args: FakeOpener())

    assert module.main() == expected_exit
    assert [entry[0].rsplit("/", 1)[-1] for entry in requests] == [
        "login",
        "investigate",
        "logout",
    ]
    assert requests[1][2] == "Bearer " + "t" * 40
    assert requests[1][1]["question"] == "Only show system files."
    report = json.loads(output.read_text(encoding="utf-8"))
    assert report["manual_semantic_review_required"] is True
    assert report["acceptance_claimed"] is False
    if expected_focus is None:
        expected_checks = {"status": "not_configured", "failures": []}
    elif expected_focus == "file_listing":
        expected_checks = {"status": "passed", "failures": []}
    else:
        expected_checks = {"status": "failed", "failures": ["answer_focus"]}
    assert report["automatic_expectations"] == expected_checks["status"]
    assert report["cases"][0]["automatic_checks"] == expected_checks
    assert report["application_code_digest_matched"] is (observed_digest == "a" * 64)
    assert report["cases"][0]["code_digest_match"] is (observed_digest == "a" * 64)
    assert report["expected_app_code_sha256"] == "a" * 64
    assert report["release_identity_verified_by_this_script"] is False
    assert report["cases"][0]["result"]["body"]["assistant"]["answer"] == "Only system files."
    assert "t" * 40 not in output.read_text(encoding="utf-8")
    assert "Only system files." not in capsys.readouterr().out
