"""Real-browser acceptance for the bilingual Phase 2 incident panel."""

from __future__ import annotations

import asyncio
import socket
import threading
import time
from collections.abc import Iterator
from pathlib import Path
from typing import Any
from urllib.request import urlopen
from uuid import uuid4

import pytest
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import Page, expect, sync_playwright

from nextops.api.incident_focus import incident_focus

pytestmark = pytest.mark.browser
STATIC = Path(__file__).resolve().parents[2] / "packages" / "nextops" / "api" / "static"
NOW = "2026-09-23T10:00:00Z"


def _assistant(locale: str) -> dict[str, Any]:
    return {
        "request_id": str(uuid4()),
        "correlation_id": str(uuid4()),
        "locale": locale,
        "answer": (
            "شواهد زنده در دسترس است و علت قطعی هنوز اثبات نشده است."
            if locale == "fa"
            else "Live evidence is available; a definitive root cause is not established."
        ),
        "model_id": "nextops-qwen3-8b-q4-k-m",
        "prompt_tokens": 120,
        "completion_tokens": 16,
        "finish_reason": "stop",
        "started_at": NOW,
        "completed_at": "2026-09-23T10:00:01Z",
        "queue_ms": 0,
        "cpu_only_required": True,
        "evidence_mode": "model_only",
        "live_monitoring_data": False,
    }


def _summary() -> dict[str, Any]:
    return {
        "source": "zabbix",
        "source_version": "7.0.30",
        "host": "NextOps App",
        "collected_at": NOW,
        "metrics": [
            {
                "name": "CPU idle time",
                "key": "system.cpu.util[,idle]",
                "value": "91.2",
                "units": "%",
                "measured_at": "2026-09-23T09:59:45Z",
                "stale": False,
            }
        ],
        "active_problems": [],
        "is_partial": False,
        "partial_reasons": [],
    }


def _incident_response(locale: str, target_id: str, question: str = "") -> dict[str, Any]:
    summary = _summary()
    evidence = {
        "target_id": target_id,
        "zabbix": {
            "source": "zabbix",
            "source_version": "7.0.30",
            "host": "NextOps App",
            "collected_at": NOW,
            "window_started_at": "2026-09-23T09:00:00Z",
            "window_ended_at": NOW,
            "summary": summary,
            "history": [],
            "events": [
                {
                    "event_id": "30001",
                    "name": "CPU pressure observed",
                    "severity": 3,
                    "occurred_at": "2026-09-23T09:58:00Z",
                    "state": "problem",
                    "acknowledged": False,
                    "suppressed": False,
                }
            ],
            "is_partial": False,
            "partial_reasons": [],
        },
        "linux": {
            "source": "linux",
            "collector_version": "1.0.0",
            "target_id": target_id,
            "hostname": "nextops-app",
            "operating_system": "Ubuntu 24.04.3 LTS",
            "collected_at": NOW,
            "uptime_seconds": 7200,
            "logical_cpu_count": 8,
            "load_1m": 0.1,
            "load_5m": 0.2,
            "load_15m": 0.3,
            "memory_total_bytes": 34_359_738_368,
            "memory_available_bytes": 30_064_771_072,
            "swap_total_bytes": 0,
            "swap_free_bytes": 0,
            "filesystems": [
                {
                    "path": "/",
                    "total_bytes": 100_000,
                    "available_bytes": 75_000,
                    "used_percent": 25.0,
                }
            ],
            "processes": [{"pid": 101, "name": "uvicorn", "rss_bytes": 120_000_000}],
            "services": [
                {
                    "unit": "nextops-app.service",
                    "load_state": "loaded",
                    "active_state": "active",
                    "sub_state": "running",
                }
            ],
            "journal": [],
            "local_user_count": 1,
            "logged_in_user_count": 0,
            "installed_package_count": 850,
            "listening_sockets": [{"family": "ipv4", "address": "127.0.0.1", "port": 8090}],
            "routes": [{"interface": "ens192", "destination": "0.0.0.0/0", "gateway": "10.0.0.1"}],
            "nameservers": ["10.0.0.1"],
            "is_partial": False,
            "partial_reasons": [],
        },
        "is_partial": False,
        "partial_reasons": [],
    }
    run_id = str(uuid4())
    focus = incident_focus(question)
    assistant = _assistant(locale)
    if focus == "file_listing":
        assistant["answer"] = "The read-only collector cannot list system file names or contents."
        assistant["integrity_status"] = "deterministic_focus"
        assistant["limitations"] = ["read_only_no_action_performed", "file_listing_unavailable"]
    elif focus == "filesystems":
        assistant["answer"] = "Approved filesystem capacity only; no system file names or contents."
        assistant["integrity_status"] = "deterministic_focus"
        assistant["limitations"] = ["read_only_no_action_performed"]
    elif focus in {"network", "service", "network_service"}:
        assistant["answer"] = (
            "مشاهدات ثبت‌شدهٔ Linux به‌تنهایی سلامت یا دسترسی راه دور را ثابت نمی‌کنند."
            if locale == "fa"
            else "The recorded Linux observations alone do not prove health or remote access."
        )
        assistant["integrity_status"] = "deterministic_focus"
        assistant["limitations"] = ["read_only_no_action_performed"]
    return {
        "assistant": assistant,
        "evidence": evidence,
        "run_id": run_id,
        "evidence_reference": f"run-evidence:{run_id}",
        "evidence_sha256": "a" * 64,
        "audit_event_id": str(uuid4()),
        "evidence_mode": "live_zabbix_linux",
        "live_monitoring_data": True,
        "answer_focus": focus,
    }


def _fixture_app() -> FastAPI:
    app = FastAPI()
    app.mount("/assets", StaticFiles(directory=STATIC), name="assets")
    app.state.incident_requests = []
    app.state.logout_requests = 0
    app.state.general_answers = {}
    app.state.general_requests = []
    app.state.general_integrity = "deterministic_fallback"
    app.state.general_delay = 0.0
    app.state.monitoring_requests = []

    @app.get("/")
    def panel() -> FileResponse:
        return FileResponse(STATIC / "index.html")

    @app.post("/api/v1/login")
    async def login() -> dict[str, Any]:
        return {
            "actor": {
                "subject_id": str(uuid4()),
                "organization_id": str(uuid4()),
                "environment_id": str(uuid4()),
                "roles": ["admin"],
                "scopes": ["zabbix.read", "linux.read", "runs.read"],
            },
            "session": {"access_token": "browser-test-token", "expires_at": NOW},
        }

    @app.get("/api/v1/me")
    async def me() -> dict[str, str]:
        return {"status": "authenticated"}

    @app.post("/api/v1/logout", status_code=204)
    async def logout() -> None:
        app.state.logout_requests += 1

    @app.get("/api/v1/assistant/ready")
    async def ready() -> dict[str, Any]:
        return {
            "state": "ready",
            "model_id": "nextops-qwen3-8b-q4-k-m",
            "runtime_version": "v0.4.1",
            "cpu_only_required": True,
            "max_active_requests": 1,
            "max_queued_requests": 2,
            "active_requests": 0,
            "queued_requests": 0,
        }

    @app.post("/api/v1/assistant/generate")
    async def general(request: Request) -> dict[str, Any]:
        payload = await request.json()
        app.state.general_requests.append(payload)
        await asyncio.sleep(app.state.general_delay)
        assistant = _assistant(str(payload["locale"]))
        assistant["answer"] = (
            "سلام! چطور می‌توانم کمک کنم؟" if payload["locale"] == "fa" else "Hello! How can I help?"
        )
        assistant["answer"] = app.state.general_answers.get(payload["locale"], assistant["answer"])
        assistant["integrity_status"] = app.state.general_integrity
        assistant["limitations"] = ["no_live_evidence", "model_output_may_be_incorrect"]
        return assistant

    @app.get("/api/v1/monitoring/summary")
    async def summary() -> dict[str, Any]:
        return _summary()

    @app.post("/api/v1/investigate")
    async def investigate(request: Request) -> dict[str, Any]:
        payload = await request.json()
        app.state.monitoring_requests.append(payload)
        assistant = _assistant(str(payload["locale"]))
        assistant["answer"] = (
            "این نمای زبیکس وضعیت دسترسیِ همهٔ میزبانان را ندارد."
            if payload["locale"] == "fa"
            else "This Zabbix view cannot identify unavailable hosts."
        )
        assistant["evidence_mode"] = "live_zabbix"
        assistant["live_monitoring_data"] = True
        assistant["integrity_status"] = "deterministic_focus"
        assistant["limitations"] = [
            "read_only_no_action_performed",
            "host_inventory_unavailable",
        ]
        run_id = str(uuid4())
        return {
            "assistant": assistant,
            "evidence": _summary(),
            "run_id": run_id,
            "evidence_reference": f"run-evidence:{run_id}",
            "evidence_sha256": "a" * 64,
            "audit_event_id": str(uuid4()),
            "evidence_mode": "live_zabbix",
            "live_monitoring_data": True,
        }

    @app.get("/api/v1/incidents/targets")
    async def targets() -> dict[str, list[str]]:
        return {"targets": ["app", "ai", "connector", "zabbix"]}

    @app.post("/api/v1/incidents/investigate")
    async def incident(request: Request) -> dict[str, Any]:
        payload = await request.json()
        app.state.incident_requests.append(payload)
        return _incident_response(
            str(payload["locale"]), str(payload["target_id"]), str(payload["question"])
        )

    return app


@pytest.fixture()
def browser_server() -> Iterator[tuple[str, FastAPI]]:
    app = _fixture_app()
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        port = int(probe.getsockname()[1])
    server = uvicorn.Server(
        uvicorn.Config(app, host="127.0.0.1", port=port, log_level="error", access_log=False)
    )
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()
    base_url = f"http://127.0.0.1:{port}"
    deadline = time.monotonic() + 10
    while time.monotonic() < deadline:
        try:
            with urlopen(f"{base_url}/", timeout=0.25) as response:
                if response.status == 200:
                    break
        except OSError:
            time.sleep(0.05)
    else:
        server.should_exit = True
        thread.join(timeout=5)
        raise RuntimeError("browser fixture server did not start")
    try:
        yield base_url, app
    finally:
        server.should_exit = True
        thread.join(timeout=5)


def _login(page: Page, base_url: str) -> None:
    page.goto(base_url, wait_until="networkidle")
    expect(page.locator(".ocs-logo-header")).to_be_visible()
    expect(page.get_by_text("Omid System Computer Services")).to_be_visible()
    logo_background = str(
        page.locator(".ocs-logo-header").evaluate(
            "element => getComputedStyle(element).backgroundImage"
        )
    )
    assert logo_background.startswith('url("data:image/jpeg;base64,')
    icon_href = page.locator("#appIcon").get_attribute("href")
    assert icon_href is not None
    assert icon_href.startswith("data:image/jpeg;base64,")
    page.locator("#languageButton").click()
    page.set_viewport_size({"width": 375, "height": 812})
    assert page.locator("html").get_attribute("dir") == "rtl"
    assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth") is True
    page.locator("#languageButton").click()
    page.set_viewport_size({"width": 1280, "height": 900})
    page.get_by_label("Username").fill("owner")
    page.get_by_label("Password").fill("test-password")
    page.get_by_role("button", name="Sign in securely").click()
    expect(page.get_by_role("heading", name="Ask the local assistant")).to_be_visible()


def _launch_browser(playwright: Any) -> Any:
    try:
        return playwright.chromium.launch()
    except PlaywrightError:
        return playwright.chromium.launch(channel="chrome")


def test_phase2_panel_supports_incident_evidence_and_persian_rtl(
    browser_server: tuple[str, FastAPI],
) -> None:
    base_url, app = browser_server
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        _login(page, base_url)

        assert page.locator(".mode-choice.active").evaluate(
            "element => element.getBoundingClientRect().height >= 44"
        )
        expect(page.get_by_text("How evidence works")).to_be_visible()

        page.get_by_role("button", name="Incident investigation").click()
        target = page.get_by_label("Investigation target")
        expect(target).to_be_visible()
        target.select_option("app")
        page.get_by_label("Question").fill("Explain the current application condition.")
        page.get_by_role("button", name="Ask assistant").click()

        expect(page.get_by_text("Live Zabbix + Linux evidence")).to_be_visible()
        expect(page.locator("#askedQuestion")).to_have_text(
            "Explain the current application condition."
        )
        page.locator("#evidenceDetails > summary").click()
        expect(page.get_by_text("nextops-app.service")).to_be_visible()
        expect(page.get_by_text("CPU pressure observed")).to_be_visible()
        assert app.state.incident_requests[-1]["target_id"] == "app"

        page.locator("#languageButton").click()
        expect(page.get_by_role("button", name="بررسی رخداد")).to_be_visible()
        expect(page.locator("#evidenceBrief")).to_contain_text("زمان گردآوری Linux")
        expect(page.get_by_text("شرکت رایانه خدمات امید سیستم")).to_be_hidden()
        expect(page.locator(".brand").get_by_text("هوشمندی داخلی برای عملیات")).to_be_visible()
        assert page.locator("html").get_attribute("dir") == "rtl"

        page.set_viewport_size({"width": 375, "height": 812})
        assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth") is True
        assert page.get_by_role("button", name="بررسی رخداد").evaluate(
            "element => element.getBoundingClientRect().height >= 44"
        )

        page.emulate_media(reduced_motion="reduce")
        page.set_viewport_size({"width": 844, "height": 390})
        assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth") is True

        page.get_by_role("button", name="خروج").click()
        expect(page.get_by_role("button", name="ورود امن")).to_be_visible()
        assert page.evaluate("sessionStorage.getItem('nextops-session')") is None
        assert app.state.logout_requests == 1
        browser.close()


def test_general_fallback_notice_does_not_imply_live_evidence(
    browser_server: tuple[str, FastAPI],
) -> None:
    base_url, _ = browser_server
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        _login(page, base_url)
        page.get_by_label("Question").fill("Hi")
        page.get_by_role("button", name="Ask assistant").click()

        expect(page.locator("#answer")).to_have_text("Hello! How can I help?")
        expect(page.locator("#integrityNotice")).to_contain_text(
            "does not report live infrastructure status"
        )
        expect(page.locator("#evidencePanel")).to_be_hidden()
        page.locator("#languageButton").click()
        expect(page.locator("#integrityNotice")).to_contain_text(
            "گزارشی از وضعیت زندهٔ زیرساخت نیست"
        )
        browser.close()


def test_file_request_is_honest_and_does_not_open_a_data_dump(
    browser_server: tuple[str, FastAPI],
) -> None:
    base_url, _ = browser_server
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        _login(page, base_url)
        page.get_by_role("button", name="Incident investigation").click()
        page.get_by_label("Investigation target").select_option("app")
        page.get_by_label("Question").fill("Only show the system files on app.")
        page.get_by_label("Question").press("Enter")

        expect(page.locator("#answer")).to_contain_text("cannot list system file names")
        expect(page.locator("#integrityNotice")).to_contain_text(
            "outside the current read-only collector scope"
        )
        expect(page.locator("#evidenceBrief")).to_contain_text(
            "File names and contents unavailable"
        )
        expect(page.locator("#askedQuestion")).to_have_text("Only show the system files on app.")
        assert page.locator("#askedQuestion").get_attribute("dir") == "auto"
        assert page.locator("#evidenceDetails").evaluate("element => element.open") is False
        expect(page.get_by_text("nextops-app.service")).to_be_hidden()
        page.locator("#evidenceDetails > summary").click()
        expect(page.get_by_text("No system file names or contents were collected")).to_be_visible()
        expect(page.get_by_role("heading", name="Filesystems")).to_be_hidden()
        expect(page.get_by_text("nextops-app.service")).to_be_hidden()
        page.get_by_text("Show complete authorized evidence").click()
        expect(page.get_by_text("nextops-app.service")).to_be_visible()
        page.set_viewport_size({"width": 375, "height": 812})
        assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth") is True
        browser.close()


@pytest.mark.parametrize(
    ("locale", "answer", "direction"),
    [
        ("fa", "SSD داده را پس از قطع برق نگه می‌دارد.", "rtl"),
        ("en", "سلام means hello in Persian.", "ltr"),
    ],
)
def test_answer_direction_uses_response_locale_not_first_strong_character(
    browser_server: tuple[str, FastAPI], locale: str, answer: str, direction: str
) -> None:
    base_url, app = browser_server
    app.state.general_answers[locale] = answer
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        _login(page, base_url)
        # The answer language is independent of the interface language.
        if locale == "en":
            page.locator("#languageButton").click()
        page.locator(f'.locale-choice[data-locale="{locale}"]').click()
        page.locator("#question").fill("Explain briefly.")
        page.locator("#askButton").click()
        expect(page.locator("#answer")).to_have_text(answer)
        assert page.locator("#answer").get_attribute("dir") == direction
        assert (
            page.locator("#answer").evaluate("element => getComputedStyle(element).direction")
            == direction
        )
        page.set_viewport_size({"width": 375, "height": 812})
        assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth")
        page.emulate_media(reduced_motion="reduce")
        page.set_viewport_size({"width": 844, "height": 390})
        assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth")
        browser.close()


def test_file_only_question_hides_unrelated_evidence_until_explicit_expand(
    browser_server: tuple[str, FastAPI],
) -> None:
    base_url, _ = browser_server
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        _login(page, base_url)
        page.get_by_role("button", name="Incident investigation").click()
        page.get_by_label("Investigation target").select_option("app")
        page.get_by_label("Question").fill(
            "Show only system file and filesystem evidence for this host. "
            "Do not include CPU, memory, or unrelated Zabbix data."
        )
        page.get_by_role("button", name="Ask assistant").click()

        expect(page.locator("#answer")).to_contain_text("Approved filesystem capacity only")
        expect(page.locator("#evidenceBrief")).to_contain_text("Approved filesystem mounts only")
        page.locator("#evidenceDetails > summary").click()
        expect(page.get_by_role("heading", name="Filesystems")).to_be_visible()
        expect(page.get_by_text("nextops-app.service")).to_be_hidden()
        expect(page.locator("#metricList").get_by_text("CPU idle time")).to_be_hidden()
        expect(page.locator(".complete-evidence").get_by_text("CPU idle time")).to_be_hidden()
        page.get_by_text("Show complete authorized evidence").click()
        expect(page.get_by_text("nextops-app.service")).to_be_visible()
        expect(page.locator(".complete-evidence").get_by_text("CPU idle time")).to_be_visible()
        browser.close()


@pytest.mark.parametrize(
    ("question", "locale", "scope", "focused_heading", "excluded_heading"),
    [
        (
            "Which DNS resolver and route were recorded for app?",
            "en",
            "Recorded network observations only",
            "Configured resolvers",
            "Filesystems",
        ),
        (
            "وضعیت سرویس nextops-app.service چه بود؟",
            "fa",
            "Recorded service observations only",
            "Allowlisted services",
            "Filesystems",
        ),
    ],
)
def test_network_and_service_focus_hide_unrelated_evidence_until_explicit_expand(
    browser_server: tuple[str, FastAPI],
    question: str,
    locale: str,
    scope: str,
    focused_heading: str,
    excluded_heading: str,
) -> None:
    base_url, _ = browser_server
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        _login(page, base_url)
        page.get_by_role("button", name="Incident investigation").click()
        page.get_by_label("Investigation target").select_option("app")
        page.locator(f'.locale-choice[data-locale="{locale}"]').click()
        page.get_by_label("Question").fill(question)
        page.get_by_role("button", name="Ask assistant").click()

        expect(page.locator("#evidenceBrief")).to_contain_text(scope)
        expect(page.locator("#integrityNotice")).to_contain_text("deterministic")
        page.locator("#evidenceDetails > summary").click()
        expect(page.get_by_role("heading", name=focused_heading)).to_be_visible()
        expect(page.get_by_role("heading", name=excluded_heading)).to_be_hidden()
        page.get_by_text("Show complete authorized evidence").click()
        expect(page.get_by_role("heading", name=excluded_heading)).to_be_visible()
        page.set_viewport_size({"width": 375, "height": 812})
        assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth") is True
        browser.close()


def test_monitoring_host_inventory_limit_is_explained_in_browser(
    browser_server: tuple[str, FastAPI],
) -> None:
    base_url, _ = browser_server
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        _login(page, base_url)
        page.get_by_role("button", name="Live monitoring").click()
        page.get_by_label("Question").fill(
            "Which authorized Zabbix hosts are currently unavailable?"
        )
        page.get_by_role("button", name="Ask assistant").click()

        expect(page.locator("#answer")).to_contain_text("cannot identify unavailable hosts")
        expect(page.locator("#integrityNotice")).to_contain_text(
            "does not contain reachability states"
        )
        expect(page.locator("#evidenceBrief")).to_contain_text("Zabbix monitoring")
        page.locator("#languageButton").click()
        expect(page.locator("#integrityNotice")).to_contain_text(
            "وضعیت دسترسیِ فهرست میزبان‌های مجاز"
        )
        browser.close()


def test_general_conversation_context_is_bounded_and_live_evidence_is_independent(
    browser_server: tuple[str, FastAPI],
) -> None:
    base_url, app = browser_server
    app.state.general_integrity = "model_unverified"
    app.state.general_answers["en"] = "DNS maps names to addresses."
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        _login(page, base_url)
        page.locator("#question").fill("Explain DNS.")
        page.locator("#question").press("Shift+Enter")
        assert app.state.general_requests == []
        page.locator("#question").fill("Explain DNS.")
        page.locator("#question").press("Enter")
        expect(page.locator("#answer")).to_have_text("DNS maps names to addresses.")
        assert page.evaluate("document.activeElement.id") == "resultCard"
        page.locator("#question").fill("What about caching?")
        page.locator("#askButton").click()
        expect(page.locator("#conversationHistory .conversation-turn")).to_have_count(1)
        assert "history" not in app.state.general_requests[0]
        assert app.state.general_requests[1]["history"] == [
            {"question": "Explain DNS.", "answer": "DNS maps names to addresses."}
        ]
        page.locator('[data-mode="monitoring"]').click()
        page.locator("#question").fill("Which hosts are currently unavailable?")
        page.locator("#askButton").click()
        expect(page.locator("#evidenceBrief")).to_be_visible()
        assert "history" not in app.state.monitoring_requests[0]
        page.locator('[data-mode="general"]').click()
        page.locator("#question").fill("Explain DNS TTL.")
        page.locator("#askButton").click()
        expect(page.locator("#conversationHistory .conversation-turn")).to_have_count(3)
        assert "history" not in app.state.general_requests[-1]
        assert page.evaluate(
            "new Set([...document.querySelectorAll('[id]')].map(n => n.id)).size === "
            "document.querySelectorAll('[id]').length"
        )
        assert page.evaluate("Object.keys(sessionStorage)") == ["nextops-session"]
        assert page.evaluate("Object.keys(localStorage)") == ["nextops-language"]
        page.locator("#newChatButton").click()
        expect(page.locator("#conversationHistory")).to_be_empty()
        expect(page.locator("#resultCard")).to_be_hidden()
        expect(page.locator("#conversationWelcome")).to_be_visible()
        expect(page.locator("#answer")).to_be_empty()
        browser.close()


def test_safe_code_formatting_copy_brand_and_responsive_rtl(
    browser_server: tuple[str, FastAPI], tmp_path: Path
) -> None:
    base_url, app = browser_server
    print(f"Fixture-only UI previews: {tmp_path}")
    app.state.general_integrity = "model_unverified"
    hostile = '<img src="https://invalid.example/steal" onerror="window.injected=true">'
    answer = (
        "Inspect `example.service`:\n```bash\nsystemctl status example.service\n```\n" + hostile
    )
    app.state.general_answers["en"] = answer
    app.state.general_answers["fa"] = (
        "بررسی فقط‌خواندنی:\n```bash\nsystemctl status example.service\n```\n"
        "زمان: 2026-09-29T10:01:02.123Z؛ نشانی: 192.0.2.15/24؛ مقدار: 13.79%"
    )
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(viewport={"width": 1440, "height": 1000})
        requests: list[str] = []
        page.on("request", lambda request: requests.append(request.url))
        _login(page, base_url)
        page.screenshot(path=str(tmp_path / "noc-workspace-welcome.png"), full_page=True)
        page.locator("#question").fill("Suggest a read-only service check.")
        page.locator("#askButton").click()
        expect(page.locator("#answer .code-block code")).to_have_text(
            "systemctl status example.service\n"
        )
        expect(page.locator("#answer")).to_contain_text(hostile)
        expect(page.locator("#answer img, #answer script, #answer a")).to_have_count(0)
        assert page.evaluate("window.injected") is None
        assert all(url.startswith(base_url + "/") for url in requests)
        assert (
            page.evaluate(
                "getComputedStyle(document.documentElement).getPropertyValue('--brand-gold').trim()"
            )
            == "#d0a840"
        )
        assert (
            page.evaluate(
                "getComputedStyle(document.documentElement).getPropertyValue('--brand-teal').trim()"
            )
            == "#0090a0"
        )
        page.evaluate("navigator.clipboard.writeText = async text => { window.copiedText = text; }")
        page.get_by_role("button", name="Copy code", exact=True).click()
        assert page.evaluate("window.copiedText") == "systemctl status example.service\n"
        page.locator("#copyAnswerButton").click()
        assert page.evaluate("window.copiedText") == answer
        page.locator("#languageButton").click()
        page.locator("#question").fill("یک بررسی ایمن پیشنهاد کن.")
        page.locator("#askButton").click()
        expect(page.locator("#askedQuestion")).to_have_text("یک بررسی ایمن پیشنهاد کن.")
        expect(page.locator("#answer .code-block")).to_be_visible()
        assert page.locator("#answer").get_attribute("dir") == "rtl"
        assert page.locator("#answer pre").get_attribute("dir") == "ltr"
        expect(page.locator("#answer p bdi[dir=ltr]")).to_have_text(
            ["2026-09-29T10:01:02.123Z", "192.0.2.15/24", "13.79%"]
        )
        assert (
            page.locator("#answer p bdi").first.evaluate(
                "element => getComputedStyle(element).direction"
            )
            == "ltr"
        )
        assert (
            page.locator("#answer").get_attribute("data-raw-text")
            == app.state.general_answers["fa"]
        )
        page.locator("#copyAnswerButton").click()
        assert page.evaluate("window.copiedText") == app.state.general_answers["fa"]
        page.screenshot(path=str(tmp_path / "noc-workspace-persian.png"), full_page=True)
        for width, height in [(375, 812), (844, 390), (768, 1024)]:
            page.set_viewport_size({"width": width, "height": height})
            page.emulate_media(reduced_motion="reduce")
            assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth")
        page.set_viewport_size({"width": 375, "height": 812})
        page.screenshot(path=str(tmp_path / "noc-workspace-mobile.png"), full_page=True)
        browser.close()


def test_visible_turn_limit_and_oversized_context_are_not_silent_truncation(
    browser_server: tuple[str, FastAPI],
) -> None:
    base_url, app = browser_server
    app.state.general_integrity = "model_unverified"
    app.state.general_answers["en"] = "A bounded general explanation."
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        _login(page, base_url)
        for index in range(14):
            page.locator("#question").fill(f"Explain concept {index}.")
            page.locator("#askButton").click()
            expect(page.locator("#question")).to_be_editable()
        expect(page.locator(".conversation-turn:not(.hidden)")).to_have_count(12)
        assert len(app.state.general_requests[-1]["history"]) == 2
        question = "q" * 3_980 + " QUESTION_TAIL"
        page.locator("#question").fill(question)
        page.locator("#askButton").click()
        expect(page.locator("#askedQuestion")).to_have_text(question)
        expect(page.locator("#contextNotice")).to_contain_text("too long")
        assert app.state.general_requests[-1]["question"] == question
        page.locator("#question").fill("Explain another concept.")
        page.locator("#askButton").click()
        expect(page.locator("#question")).to_be_editable()
        assert "history" not in app.state.general_requests[-1]
        browser.close()


def test_pending_logout_clears_private_turns_and_rejects_late_result(
    browser_server: tuple[str, FastAPI],
) -> None:
    base_url, app = browser_server
    app.state.general_delay = 0.7
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        _login(page, base_url)
        page.locator("#question").fill("Explain safe service diagnostics.")
        page.locator("#askButton").click()
        expect(page.locator("#newChatButton")).to_be_disabled()
        expect(page.locator('[data-mode="monitoring"]')).to_be_disabled()
        page.evaluate(
            "document.getElementById('assistantForm').dispatchEvent("
            "new Event('submit', {cancelable: true}))"
        )
        page.locator("#logoutButton").click()
        expect(page.locator("#loginView")).to_be_visible()
        page.wait_for_timeout(850)  # Controlled fixture's delayed response, not a serving model.
        assert len(app.state.general_requests) == 1
        assert app.state.logout_requests == 1
        expect(page.locator("#resultCard")).to_be_hidden()
        expect(page.locator("#answer")).to_be_empty()
        expect(page.locator("#conversationHistory")).to_be_empty()
        assert page.evaluate("sessionStorage.getItem('nextops-session')") is None
        browser.close()


def test_expired_session_purges_transcript_and_failed_request_keeps_question(
    browser_server: tuple[str, FastAPI],
) -> None:
    base_url, _ = browser_server
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        _login(page, base_url)
        page.locator("#question").fill("Hi")
        page.locator("#askButton").click()
        expect(page.locator("#answer")).to_contain_text("Hello")
        page.route(
            "**/api/v1/assistant/generate",
            lambda route: route.fulfill(
                status=503, json={"error": {"code": "dependency_unavailable"}}
            ),
        )
        page.locator("#question").fill("Explain DNS.")
        page.locator("#askButton").click()
        expect(page.locator("#assistantError")).to_contain_text("temporarily unavailable")
        expect(page.locator("#question")).to_have_value("Explain DNS.")
        expect(page.locator("#answer")).to_contain_text("Hello")
        page.unroute("**/api/v1/assistant/generate")
        page.route(
            "**/api/v1/assistant/generate",
            lambda route: route.fulfill(status=403, json={"error": {"code": "forbidden"}}),
        )
        page.locator("#askButton").click()
        expect(page.locator("#assistantError")).to_contain_text("denied by application policy")
        expect(page.locator("#question")).to_have_value("Explain DNS.")
        page.unroute("**/api/v1/assistant/generate")
        page.route(
            "**/api/v1/assistant/generate",
            lambda route: route.fulfill(status=401, json={"error": {"code": "unauthenticated"}}),
        )
        page.locator("#askButton").click()
        expect(page.locator("#loginView")).to_be_visible()
        expect(page.locator("#answer")).to_be_empty()
        assert page.evaluate("sessionStorage.getItem('nextops-session')") is None
        browser.close()
