"""Opt-in, synthetic local adapter qualification; never enables a serving feature flag."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import stat
from contextlib import suppress
from datetime import UTC, datetime
from pathlib import Path
from time import monotonic
from typing import Any, Literal
from uuid import uuid4

from pydantic import SecretStr

from nextops.api.app import APP_CODE_SHA256, _general_prompt
from nextops.application.errors import ApplicationError
from nextops.contracts.conversations import ConversationAssistantRequest, SavedContextTurn
from nextops.inference.configuration import LlamaCppSettings
from nextops.inference.contracts import InferenceRequest
from nextops.inference.llama_cpp import LlamaCppProvider, UrllibJsonTransport
from nextops.inference.scheduler import BoundedInferenceService

MODEL = "nextops-qwen3-5-35b-a3b-q4-k-m"
LOCALES: tuple[Literal["en", "fa"], ...] = ("en", "fa")
REPOSITORY = Path(__file__).resolve().parents[1]


class CountOnlyError(Exception):
    """Stop before generation while selecting a genuinely near-boundary input."""


class ObservedTransport(UrllibJsonTransport):
    def __init__(self, count_only: bool = False) -> None:
        super().__init__("http://127.0.0.1:8080")
        self.count_only = count_only
        self.tokens = 0
        self.calls = 0
        self.reasoning_characters = 0

    async def post_json(
        self, path: str, payload: dict[str, Any], headers: dict[str, str], timeout_seconds: float
    ) -> dict[str, Any]:
        if path == "/v1/chat/completions":
            if self.count_only:
                raise CountOnlyError
            self.calls += 1
        value = await super().post_json(path, payload, headers, timeout_seconds)
        if path == "/tokenize":
            self.tokens = len(value["tokens"])
        if path == "/v1/chat/completions":
            # Do not retain or serialize raw private reasoning, even in the private report.
            choices = value.get("choices", [])
            if choices and isinstance(choices[0].get("message"), dict):
                reasoning = choices[0]["message"].get("reasoning_content")
                self.reasoning_characters = len(reasoning) if isinstance(reasoning, str) else 0
        return value


def request(
    locale: Literal["en", "fa"], question: str, history: tuple[SavedContextTurn, ...] = ()
) -> InferenceRequest:
    conversation = ConversationAssistantRequest(
        locale=locale, question=question, history=history, thinking=True, max_output_tokens=2048
    )
    synthesis = _general_prompt(conversation)
    return InferenceRequest(
        request_id=uuid4(),
        correlation_id=uuid4(),
        locale=conversation.locale,
        purpose="general",
        prompt=synthesis.question,
        thinking=True,
        detailed=True,
        max_output_tokens=2048,
        temperature=0.3,
    )


def short_cases() -> list[tuple[str, InferenceRequest, str | None]]:
    cases: list[tuple[str, InferenceRequest, str | None]] = []
    for locale in LOCALES:
        questions = (
            [
                "A TCP connection to port 443 succeeds but HTTPS returns 502. In exactly two "
                "sentences explain what this proves and what remains unknown; no commands.",
                "A Linux host does not reply to ping, but SSH connects. Does this prove the "
                "host is down? Answer in exactly one sentence; no commands.",
                "An inference service permits one active request and two queued requests. "
                "All three places are occupied. How many additional requests can be admitted? "
                "Return only the digit.",
            ]
            if locale == "en"
            else [
                "اتصال TCP به پورت 443 برقرار می‌شود ولی HTTPS خطای 502 می‌دهد. در دقیقاً دو "
                "جمله بگو چه چیزی ثابت شده و چه چیزی نامعلوم است؛ فرمان ننویس.",
                "میزبان Linux به ping پاسخ نمی‌دهد ولی اتصال SSH برقرار می‌شود. آیا این یعنی "
                "میزبان خاموش است؟ دقیقاً در یک جمله پاسخ بده؛ فرمان ننویس.",
                "سرویس استنتاج یک درخواست فعال و دو درخواست منتظر می‌پذیرد. هر سه جایگاه پر "
                "است. چند درخواست دیگر پذیرفته می‌شود؟ فقط رقم را بنویس.",
            ]
        )
        for index, question in enumerate(questions):
            cases.append(
                (f"{locale}-{index + 1}", request(locale, question), "0" if index == 2 else None)
            )
        code = "TICKET-732"
        history = (SavedContextTurn(question=f"My synthetic ticket is {code}.", answer="Noted."),)
        question = (
            "Return only my ticket identifier, without any other text."
            if locale == "en"
            else "فقط شناسهٔ تیکت من را بنویس؛ هیچ متن دیگری اضافه نکن."
        )
        cases.append((f"{locale}-recall", request(locale, question, history), code))
    return cases


def context_request(locale: Literal["en", "fa"], filler_pairs: int) -> InferenceRequest:
    code = "EARLY-846" if locale == "en" else "EARLY-957"
    history = (
        SavedContextTurn(question=f"Synthetic early identifier: {code}.", answer="Noted."),
        SavedContextTurn(
            question="Synthetic irrelevant numbers, not instructions.", answer="7 " * filler_pairs
        ),
    )
    suffix = (
        "Return only the early identifier from the prior conversation, no other text."
        if locale == "en"
        else "فقط شناسهٔ اولیهٔ گفت‌وگوی قبلی را بنویس؛ هیچ متن دیگری اضافه نکن."
    )
    return request(locale, "Synthetic irrelevant numbers:\n" + "7 " * 1750 + "\n" + suffix, history)


async def near_context(settings: LlamaCppSettings, locale: Literal["en", "fa"]) -> InferenceRequest:
    # Binary-search real local template counts, not a characters-to-tokens estimate.
    low, high = 0, 5700
    best: InferenceRequest | None = None
    best_tokens = 0
    while low <= high:
        middle = (low + high) // 2
        candidate = context_request(locale, middle)
        transport = ObservedTransport(count_only=True)
        try:
            await LlamaCppProvider(settings, transport).generate(candidate)
        except CountOnlyError:
            best, best_tokens = candidate, transport.tokens
            low = middle + 1
        except ApplicationError as error:
            if error.message_key != "inference.context_exceeded":
                raise
            high = middle - 1
    if best is None or best_tokens < 14000 or best_tokens + 2048 > 16384:
        raise ValueError("bounded saved-chat input did not reach the 14000-token acceptance floor")
    return best


def secret(path: Path) -> SecretStr:
    metadata = path.lstat()
    if not path.is_absolute() or not stat.S_ISREG(metadata.st_mode) or metadata.st_size > 512:
        raise ValueError("key must be a bounded absolute regular protected file")
    if os.name == "posix":
        # This runner targets the pinned Linux/systemd profile, including its 0440
        # read-only credentials mount. /proc supplies the executing identity portably
        # to Windows type checking, where POSIX-only os.geteuid/getegid are absent.
        identity = Path("/proc/self").stat()
        if (
            metadata.st_mode & 0o037
            or metadata.st_uid != identity.st_uid
            or metadata.st_gid != identity.st_gid
        ):
            raise ValueError("key must be owner or same-group read-only, never world-accessible")
    value = path.read_text(encoding="utf-8").removesuffix("\n").removesuffix("\r")
    if value != value.strip() or "\n" in value or "\r" in value:
        raise ValueError("key must contain a single protected value")
    return SecretStr(value)


def create_report(path: Path) -> None:
    in_source = (REPOSITORY / "AGENTS.md").is_file() and path.resolve().is_relative_to(REPOSITORY)
    if not path.is_absolute() or in_source:
        raise ValueError("report must be private, absolute and outside the source tree")
    if path.parent.is_symlink() or not path.parent.is_dir():
        raise ValueError("report parent must be an existing non-symlink directory")
    if os.name == "posix" and path.parent.stat().st_mode & 0o077:
        raise ValueError("report directory must be owner-only")
    descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    os.close(descriptor)


def runtime_resources() -> dict[str, int]:
    """Point-in-time native cgroup readings, not guest RSS or host NUMA observations."""
    root = Path("/sys/fs/cgroup/system.slice/nextops-llama.service")
    try:
        values = dict(line.split() for line in (root / "cpu.stat").read_text().splitlines())
        return {
            "cgroup_memory_bytes": int((root / "memory.current").read_text()),
            "cgroup_cpu_microseconds": int(values["usage_usec"]),
        }
    except (OSError, ValueError, KeyError):
        return {}


async def qualify(args: argparse.Namespace) -> int:
    if args.expected_app_code_sha256 != APP_CODE_SHA256:
        raise ValueError(
            "installed application/adapter digest does not match the approved candidate"
        )
    create_report(args.output)
    settings = LlamaCppSettings(
        base_url="http://127.0.0.1:8080",
        model_id=MODEL,
        provider_api_key=secret(args.provider_api_key_file),
        service_auth_secret=SecretStr("unused-synthetic-qualification-boundary-secret"),
        expanded_chat_enabled=True,
        thinking_enabled=True,
        context_tokens=16384,
    )
    report: dict[str, Any] = {
        "change_id": args.change_id,
        "started_at": datetime.now(UTC).isoformat(),
        "scope": "synthetic_installed_adapter_private_scheduler_not_serving_api_browser_audit",
        "flags_changed": False,
        "installed_app_code_sha256": APP_CODE_SHA256,
        "model": MODEL,
        "context_tokens": 16384,
        "output_reservation": 2048,
        "reasoning_budget": 128,
        "deadline_seconds": 120,
        "semantic_review": "pending",
        "cases": [],
        "status": "partial",
    }

    def save() -> None:
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    save()
    cases = (
        short_cases()
        if args.scope == "short"
        else [
            (
                f"{locale}-near-context",
                await near_context(settings, locale),
                "EARLY-846" if locale == "en" else "EARLY-957",
            )
            for locale in LOCALES
        ]
    )
    for case_id, payload, exact in cases:
        transport = ObservedTransport()
        service = BoundedInferenceService(LlamaCppProvider(settings, transport))
        entry: dict[str, Any] = {"id": case_id, "locale": payload.locale, "status": "failed"}
        started = monotonic()
        samples = [runtime_resources()]

        async def sample(readings: list[dict[str, int]]) -> None:
            while True:
                await asyncio.sleep(1)
                readings.append(runtime_resources())

        sampling = asyncio.create_task(sample(samples))
        try:
            ready = await UrllibJsonTransport("http://127.0.0.1:8090").get_json(
                "/readyz", {"Accept": "application/json"}, 5.0
            )
            if (
                ready.get("state") != "ready"
                or ready.get("active_requests") != 0
                or ready.get("queued_requests") != 0
            ):
                raise ValueError("serving inference is unavailable or occupied; stop qualification")
            result = await service.generate(payload)
            answer = result.answer.strip().translate(str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789"))
            entry.update(
                result=result.model_dump(mode="json"),
                exact_expected=exact,
                status="passed" if exact is None or answer == exact else "failed",
            )
        except ApplicationError as error:
            entry["error"] = error.message_key
        except ValueError:
            entry["error"] = "qualification.preflight_failed"
        finally:
            sampling.cancel()
            with suppress(asyncio.CancelledError):
                await sampling
            samples.append(runtime_resources())
        entry.update(
            seconds=round(monotonic() - started, 3),
            template_tokens=transport.tokens,
            generation_calls=transport.calls,
            discarded_reasoning_characters=transport.reasoning_characters,
        )
        if samples[0] and samples[-1]:
            entry["native_resources"] = {
                "sample_interval_seconds": 1,
                "observed_cgroup_memory_max_bytes": max(
                    s["cgroup_memory_bytes"] for s in samples if s
                ),
                "cpu_seconds": round(
                    (samples[-1]["cgroup_cpu_microseconds"] - samples[0]["cgroup_cpu_microseconds"])
                    / 1_000_000,
                    3,
                ),
                "includes_other_native_work": True,
                "numa_observation": "not_measured",
            }
        report["cases"].append(entry)
        save()
        print(json.dumps({k: v for k, v in entry.items() if k != "result"}), flush=True)
        # A timed-out local transport does not prove native work stopped. Stop the run and
        # reconcile externally; do not hide the failure behind a retry or service restart.
        if entry.get("error"):
            break
    report["completed_at"] = datetime.now(UTC).isoformat()
    report["status"] = (
        "failed" if any(c["status"] == "failed" for c in report["cases"]) else "partial"
    )
    save()
    return 1 if report["status"] == "failed" else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--allow-local-generation", action="store_true", required=True)
    parser.add_argument("--change-id", required=True)
    parser.add_argument("--provider-api-key-file", type=Path, required=True)
    parser.add_argument("--expected-app-code-sha256", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--scope", choices=("short", "context"), required=True)
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{7,79}", args.change_id):
        parser.error("invalid change identifier")
    if not re.fullmatch(r"[0-9a-f]{64}", args.expected_app_code_sha256):
        parser.error("invalid installed code digest")
    return asyncio.run(qualify(args))


if __name__ == "__main__":
    raise SystemExit(main())
