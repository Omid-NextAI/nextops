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
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import Page, expect, sync_playwright

from nextops.api.incident_focus import incident_focus

pytestmark = pytest.mark.browser


@pytest.mark.parametrize("locale", ["en", "fa"])
def test_qwen38_capabilities_and_secondary_problem_inspection(
    browser_server: tuple[str, FastAPI], locale: str
) -> None:
    """Sanitized fixtures: no live model, connector or quality qualification."""
    base_url, app = browser_server
    app.state.ready_model = "nextops-qwen3-8-27b-q8-0"
    app.state.ready_context = 16384
    app.state.saved_chats_enabled = True
    app.state.thinking_allowed = False
    app.state.source_problems = [
        {"name": "Demo agent unavailable", "severity": 4, "started_at": NOW}
    ]
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        _login(page, base_url)
        if locale == "fa":
            page.locator("#languageButton").click()
        expect(page.locator("#modelStatusLabel")).to_contain_text("Qwen3.8-27B")
        page.locator("#modelStatusLabel").click()
        expect(page.locator("#modelCapabilitiesDialog")).to_be_visible()
        expect(page.locator("#capabilitiesContent")).to_contain_text(
            "۱۶٬۳۸۴" if locale == "fa" else "16,384"
        )
        expect(page.locator("#capabilitiesContent")).to_contain_text(
            "غیرفعال" if locale == "fa" else "Disabled"
        )
        page.keyboard.press("Escape")
        expect(page.locator("#modelStatusLabel")).to_be_focused()
        page.locator('[data-nav="connectors"]').click()
        page.locator('[data-inspect-source="secondary"]').first.click()
        expect(page.locator("#composerOptions")).not_to_have_attribute("open", "")
        expect(page.locator("#monitoringSource")).to_be_visible()
        expect(page.locator("#monitoringSource")).to_have_value("secondary")
        expect(page.locator("#question")).not_to_be_empty()
        page.locator('[data-monitoring-shortcut="metrics"]').click()
        assert ("۶۰" if locale == "fa" else "60") in page.locator("#question").input_value()
        assert not app.state.monitoring_requests  # Shortcut prepares; does not execute.
        page.locator("#askButton").click()
        expect(page.locator("#evidenceSource")).to_contain_text("secondary / sla")
        page.locator("#resultCard .response-evidence > summary").click()
        page.locator('#resultCard [data-evidence-filter="problems"]').click()
        expect(page.locator("#resultCard .evidence-row")).to_have_count(1)
        page.locator("#resultCard [data-evidence-index]").first.click()
        expect(page.locator("#panel-raw")).to_contain_text("Demo agent unavailable")
        expect(page.locator("#panel-raw")).to_contain_text('"severity": 4')
        page.locator("#evidenceClose").click()
        page.locator('#resultCard [data-evidence-filter="metrics"]').click()
        expect(page.locator("#resultCard .evidence-row")).to_have_count(1)
        page.set_viewport_size({"width": 390, "height": 844})
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
        expect(page.locator("#monitoringSource")).to_be_visible()
        screenshot_root = Path("artifacts/q38-ui-sync")
        screenshot_root.mkdir(parents=True, exist_ok=True)
        page.evaluate("""() => {
            const note=document.createElement('p');
            note.textContent='Demo data — not live'; note.id='fixtureNotice';
            document.querySelector('.topbar').append(note);
        }""")
        page.screenshot(path=str(screenshot_root / f"secondary-{locale}-mobile.png"))
        page.locator("#workspaceInputControls").scroll_into_view_if_needed()
        page.screenshot(path=str(screenshot_root / f"controls-{locale}-mobile.png"))
        page.set_viewport_size({"width": 1672, "height": 941})
        page.screenshot(path=str(screenshot_root / f"secondary-{locale}-desktop.png"))
        page.locator("#modelStatusLabel").click()
        page.screenshot(path=str(screenshot_root / f"capabilities-{locale}-desktop.png"))
        page.keyboard.press("Escape")
        _profile_action(page, "#logoutButton")
        expect(page.locator("#loginView")).to_be_visible()
        expect(page.locator("#capabilitiesContent")).to_be_empty()
        assert page.locator("#modelStatusLabel").get_attribute("aria-label") is None
        browser.close()


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
                },
                {
                    "unit": "nginx.service",
                    "load_state": "loaded",
                    "active_state": "active",
                    "sub_state": "running",
                },
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
    app.state.incident_targets = ["app", "ai", "connector", "zabbix"]
    app.state.logout_requests = 0
    app.state.general_answers = {}
    app.state.general_requests = []
    app.state.general_integrity = "deterministic_fallback"
    app.state.general_delay = 0.0
    app.state.monitoring_requests = []
    app.state.ready_model = "nextops-qwen3-8b-q4-k-m"
    app.state.ready_context = 8192
    app.state.thinking_allowed = True
    app.state.source_problems = []
    app.state.source_failed = False
    app.state.source_delay = 0.0
    app.state.saved_chats_enabled = False
    app.state.saved_chats = {}
    app.state.user_role = "admin"
    app.state.user_requests = []
    app.state.users_expired = False
    app.state.users = [
        {
            "identity_id": str(uuid4()),
            "username": "owner",
            "roles": ["admin"],
            "is_active": True,
            "credential_version": 1,
            "created_at": NOW,
            "manageable": False,
        }
    ]

    @app.get("/api/v1/users")
    async def users_list() -> Any:
        if app.state.users_expired:
            return JSONResponse(status_code=401, content={"error": {"code": "unauthenticated"}})
        return {"users": app.state.users, "next_offset": None}

    @app.post("/api/v1/users", status_code=201)
    async def users_create(request: Request) -> dict[str, Any]:
        payload = await request.json()
        app.state.user_requests.append(payload)
        user = {
            "identity_id": str(uuid4()),
            "username": payload["username"],
            "roles": [payload["role"]],
            "is_active": True,
            "credential_version": 1,
            "created_at": NOW,
            "manageable": True,
        }
        app.state.users.append(user)
        return user

    @app.patch("/api/v1/users/{identity_id}")
    async def users_status(identity_id: str, request: Request) -> Any:
        payload = await request.json()
        app.state.user_requests.append(payload)
        user = next(u for u in app.state.users if u["identity_id"] == identity_id)
        if payload["expected_version"] != user["credential_version"]:
            return JSONResponse(status_code=409, content={"error": {"code": "conflict"}})
        user["is_active"] = payload["is_active"]
        user["credential_version"] += 1
        return user

    @app.post("/api/v1/users/{identity_id}/password")
    async def users_password(identity_id: str, request: Request) -> dict[str, Any]:
        payload = await request.json()
        app.state.user_requests.append(payload)
        user = next(u for u in app.state.users if u["identity_id"] == identity_id)
        user["credential_version"] += 1
        return dict(user)

    @app.get("/api/v1/conversations/config")
    async def chat_config() -> dict[str, Any]:
        return {
            "enabled": app.state.saved_chats_enabled,
            "thinking_enabled": app.state.saved_chats_enabled and app.state.thinking_allowed,
            "context_turns": 6,
            "context_characters": 12000,
            "retention_days": 30,
        }

    @app.get("/api/v1/conversations")
    async def chats() -> list[dict[str, Any]]:
        return [c["conversation"] for c in app.state.saved_chats.values()]

    @app.post("/api/v1/conversations", status_code=201)
    async def create_chat(request: Request) -> dict[str, Any]:
        payload = await request.json()
        chat = {
            "conversation_id": str(uuid4()),
            "title": "New chat",
            "locale": payload["locale"],
            "turn_count": 0,
        }
        app.state.saved_chats[chat["conversation_id"]] = {
            "conversation": chat,
            "messages": [],
            "before_sequence": None,
        }
        return chat

    @app.get("/api/v1/conversations/{chat_id}")
    async def get_chat(chat_id: str) -> dict[str, Any]:
        return dict(app.state.saved_chats[chat_id])

    @app.delete("/api/v1/conversations/{chat_id}", status_code=204)
    async def delete_chat(chat_id: str) -> None:
        del app.state.saved_chats[chat_id]

    @app.post("/api/v1/conversations/{chat_id}/messages")
    async def chat_message(chat_id: str, request: Request) -> dict[str, Any]:
        payload = await request.json()
        app.state.general_requests.append(payload)
        chat = app.state.saved_chats[chat_id]
        answer = _assistant(payload["locale"])
        answer["answer"] = (
            "پاسخ محلیِ پیگیری" if payload["locale"] == "fa" else "Local follow-up answer."
        )
        answer["integrity_status"] = "model_unverified"
        saved = {
            "request_id": payload["request_id"],
            "question": payload["question"],
            "assistant": answer,
            "context_turns": min(6, len(chat["messages"])),
            "context_omitted": False,
            "thinking_requested": payload["thinking"],
        }
        chat["messages"].append(saved)
        chat["conversation"]["title"] = chat["messages"][0]["question"][:80]
        return {"conversation_id": chat_id, "message": saved}

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
    async def me() -> dict[str, Any]:
        return {"status": "authenticated", "roles": [app.state.user_role]}

    @app.post("/api/v1/logout", status_code=204)
    async def logout() -> None:
        app.state.logout_requests += 1

    @app.get("/api/v1/assistant/ready")
    async def ready() -> dict[str, Any]:
        return {
            "state": "ready",
            "model_id": app.state.ready_model,
            "configured_context_tokens": app.state.ready_context,
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

    @app.get("/api/v1/monitoring/sources")
    async def source_catalog() -> dict[str, Any]:
        return {
            "schema_version": "1.0.0",
            "discovery_mode": "approved_registry",
            "sources": [
                {
                    "source_id": "secondary",
                    "label": "Second Zabbix",
                    "organization_id": str(uuid4()),
                    "environment_id": str(uuid4()),
                    "targets": [{"target_id": "sla", "label": "SLA <img src=x>"}],
                }
            ],
        }

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

    @app.post("/api/v1/monitoring/investigate")
    async def selected_source(request: Request) -> Any:
        await asyncio.sleep(app.state.source_delay)
        if app.state.source_failed:
            return JSONResponse(
                {
                    "error": {
                        "code": "dependency_unavailable",
                        "message_key": "monitoring.source_failed",
                    }
                },
                status_code=503,
            )
        result = await investigate(request)
        payload = app.state.monitoring_requests[-1]
        result["evidence"].update(
            source_id=payload["source_id"], target_id=payload["target_id"], host_group_ids=["23"]
        )
        result["evidence"]["active_problems"] = app.state.source_problems
        return result

    @app.get("/api/v1/incidents/targets")
    async def targets() -> dict[str, list[str]]:
        return {"targets": app.state.incident_targets}

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
    page.set_default_timeout(10000)
    page.goto(base_url, wait_until="networkidle")
    expect(page.locator(".ocs-logo-hero")).to_be_visible()
    expect(page.locator(".ocs-logo-hero")).to_have_attribute(
        "aria-label", "Omid Computer Services company logo"
    )
    logo_background = str(
        page.locator(".ocs-logo-header").evaluate(
            "element => getComputedStyle(element).backgroundImage"
        )
    )
    assert "/assets/ocs-logo-" in logo_background
    icon_href = page.locator("#appIcon").get_attribute("href")
    assert icon_href is not None
    assert icon_href == "/assets/ocs-logo-light.jpg"
    page.locator("#languageButton").click()
    page.set_viewport_size({"width": 375, "height": 812})
    assert page.locator("html").get_attribute("dir") == "rtl"
    assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth") is True
    page.locator("#languageButton").click()
    page.set_viewport_size({"width": 1280, "height": 900})
    page.locator("#loginForm").get_by_label("Username").fill("owner")
    page.locator("#loginForm").get_by_label("Password", exact=True).fill("test-password")
    page.locator("#loginForm button[type=submit]").click()
    expect(page.get_by_role("heading", name="Ask NextOps", exact=True)).to_be_visible()
    page.locator("#composerOptions summary").click()


def _options(page: Page) -> None:
    if not page.locator("#composerOptions").evaluate("e => e.open"):
        page.locator("#composerOptions summary").click()


def _mode(page: Page, mode: str) -> None:
    _options(page)
    page.locator(f'[data-mode="{mode}"]').click()


def _profile_action(page: Page, selector: str) -> None:
    if not page.locator(selector).is_visible():
        page.locator("#profileMenu summary").click()
    page.locator(selector).click()


def _launch_browser(playwright: Any) -> Any:
    try:
        return playwright.chromium.launch()
    except PlaywrightError:
        return playwright.chromium.launch(channel="chrome")


@pytest.mark.parametrize("locale", ["en", "fa"])
def test_admin_users_create_status_password_and_localized_mobile_panel(
    browser_server: tuple[str, FastAPI],
    tmp_path: Path,
    locale: str,
) -> None:
    base_url, app = browser_server
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        requests: list[str] = []
        page.on("request", lambda request: requests.append(request.url))
        _login(page, base_url)
        if locale == "fa":
            page.locator("#languageButton").click()
        page.locator("#profileMenu summary").click()
        page.locator("#usersButton").focus()
        page.keyboard.press("Enter")
        expect(page.locator("#usersHeading")).to_be_focused()
        expect(page.locator("#usersList .user-row")).to_have_count(1)
        assert page.locator("#usersList button").count() == 0  # Protected administrator.
        page.locator("#userCreateName").fill("reader")
        page.locator("#userCreateRole").select_option("operator")
        page.locator("#userCreatePassword").fill("browser fixture password")
        page.locator("#userCreateForm button").click()
        expect(page.locator("#usersList .user-row")).to_have_count(2)
        expect(page.locator("#userCreatePassword")).to_have_value("")
        assert app.state.user_requests[0]["role"] == "operator"
        row = page.locator("#usersList .user-row").filter(has_text="reader")
        page.once("dialog", lambda dialog: dialog.accept())
        row.locator("button").first.click()
        expect(row).to_contain_text("غیرفعال" if locale == "fa" else "Disabled")
        page.once("dialog", lambda dialog: dialog.accept())
        row.locator("button").first.click()
        expect(row).to_contain_text("فعال" if locale == "fa" else "Active")
        row.locator("button").nth(1).click()
        expect(page.locator("#userResetPassword")).to_be_focused()
        expect(page.locator("#userPasswordName")).to_have_text("reader")
        page.locator("#userResetPassword").fill("new browser fixture password")
        page.locator("#userResetConfirm").check()
        page.locator("#userPasswordForm button[type=submit]").click()
        expect(page.locator("#userPasswordForm")).to_be_hidden()
        expect(page.locator("#userResetPassword")).to_have_value("")
        assert len(app.state.user_requests) == 4
        page.locator("#themeButton").click()
        page.screenshot(
            path=str(tmp_path / f"users-{locale}-desktop.png"),
            full_page=True,
            animations="disabled",
        )
        page.set_viewport_size({"width": 375, "height": 812})
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth") is True
        assert page.locator("html").get_attribute("dir") == ("rtl" if locale == "fa" else "ltr")
        page.screenshot(
            path=str(tmp_path / f"users-{locale}-mobile.png"), full_page=True, animations="disabled"
        )
        assert all(url.startswith(base_url) or url.startswith("data:") for url in requests)
        page.locator("#usersBack").click()
        expect(page.locator("#usersButton")).to_be_focused()
        expect(page.locator("#workspaceView")).to_be_visible()
        browser.close()


def test_non_admin_has_no_user_controls_and_expired_admin_purges_panel(
    browser_server: tuple[str, FastAPI],
) -> None:
    base_url, app = browser_server
    app.state.user_role = "viewer"
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page()
        _login(page, base_url)
        page.locator("#profileMenu summary").click()
        expect(page.locator("#usersButton")).to_be_hidden()
        _profile_action(page, "#logoutButton")
        app.state.user_role = "admin"
        _login(page, base_url)
        _profile_action(page, "#usersButton")
        expect(page.locator("#usersList .user-row")).to_have_count(1)
        page.locator("#userCreatePassword").fill("private form data only")
        app.state.users_expired = True
        page.locator("#usersRefresh").click()
        expect(page.locator("#loginView")).to_be_visible()
        expect(page.locator("#usersView")).to_be_hidden()
        expect(page.locator("#usersList")).to_be_empty()
        expect(page.locator("#userCreatePassword")).to_have_value("")
        assert page.evaluate("sessionStorage.getItem('nextops-session')") is None
        browser.close()


def test_user_conflict_is_not_retried_and_logout_rejects_late_account_response(
    browser_server: tuple[str, FastAPI],
) -> None:
    base_url, app = browser_server
    app.state.users.append(
        {
            "identity_id": str(uuid4()),
            "username": "reader",
            "roles": ["viewer"],
            "is_active": True,
            "credential_version": 1,
            "created_at": NOW,
            "manageable": True,
        }
    )
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page()
        _login(page, base_url)
        _profile_action(page, "#usersButton")
        expect(page.locator("#usersList .user-row")).to_have_count(2)
        app.state.users[-1]["credential_version"] = 2
        page.once("dialog", lambda dialog: dialog.accept())
        page.locator("#usersList .user-row").filter(has_text="reader").locator(
            "button"
        ).first.click()
        expect(page.locator("#usersError")).to_contain_text("Refresh")
        expect(page.locator("#usersError")).to_be_focused()
        assert len(app.state.user_requests) == 1
        captured: list[Any] = []
        page.route("**/api/v1/users?offset=*", lambda route: captured.append(route))
        page.locator("#usersRefresh").click()
        expect(page.locator("#usersRefresh")).to_be_disabled()
        _profile_action(page, "#logoutButton")
        expect(page.locator("#usersList")).to_be_empty()
        assert len(captured) == 1
        captured[0].fulfill(json={"users": app.state.users, "next_offset": None})
        expect(page.locator("#usersList")).to_be_empty()
        expect(page.locator("#usersView")).to_be_hidden()
        browser.close()


@pytest.mark.parametrize("locale", ["en", "fa"])
@pytest.mark.parametrize("width", [375, 1280])
def test_theme_toggle_persists_is_keyboard_accessible_and_keeps_brand(
    browser_server: tuple[str, FastAPI], locale: str, width: int
) -> None:
    base_url, _ = browser_server
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(viewport={"width": width, "height": 900}, color_scheme="light")
        page.goto(base_url, wait_until="networkidle")
        if locale == "fa":
            page.locator("#languageButton").click()
        logo = page.locator(".ocs-logo-hero").evaluate("el => getComputedStyle(el).backgroundImage")
        assert logo.endswith('/ocs-logo-light.jpg")')
        switch = page.locator("#themeButton")
        expect(switch).to_have_attribute("aria-pressed", "false")
        switch.focus()
        page.keyboard.press("Space")
        expect(switch).to_have_attribute("aria-pressed", "true")
        expect(page.locator("html")).to_have_attribute("data-theme", "dark")
        assert page.evaluate("localStorage.getItem('nextops-theme')") == "dark"
        assert (
            page.locator(".ocs-logo-hero")
            .evaluate("el => getComputedStyle(el).backgroundImage")
            .endswith('/ocs-logo-dark.jpg")')
        )
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
        tokens = page.evaluate(
            """() => {
              const css = getComputedStyle(document.documentElement);
              return Object.fromEntries(['--ink', '--muted', '--surface', '--button-bg',
                '--brand-gold-dark', '--brand-gold', '--brand-teal']
                .map(k => [k, css.getPropertyValue(k).trim()]));
            }"""
        )
        assert tokens["--brand-gold"] == "#d0a840"
        assert tokens["--brand-teal"] == "#0090a0"
        assert _contrast(tokens["--ink"], tokens["--surface"]) >= 4.5
        assert _contrast(tokens["--muted"], tokens["--surface"]) >= 4.5
        expect(switch).to_have_css("color", "rgb(242, 245, 250)")
        assert _contrast(tokens["--brand-gold-dark"], tokens["--surface"]) >= 4.5
        assert _contrast("#ffffff", tokens["--button-bg"]) >= 4.5
        page.reload(wait_until="networkidle")
        expect(page.locator("html")).to_have_attribute("data-theme", "dark")
        expect(switch).to_have_attribute(
            "aria-label", "پوستهٔ تیره" if locale == "fa" else "Dark theme"
        )
        switch.click()
        expect(page.locator("html")).to_have_attribute("data-theme", "light")
        expect(switch).to_have_attribute("aria-pressed", "false")
        browser.close()


def _contrast(first: str, second: str) -> float:
    def luminance(color: str) -> float:
        values = [int(color[index : index + 2], 16) / 255 for index in (1, 3, 5)]
        linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in values]
        return sum(v * weight for v, weight in zip(linear, (0.2126, 0.7152, 0.0722), strict=True))

    values = sorted((luminance(first), luminance(second)))
    return (values[1] + 0.05) / (values[0] + 0.05)


def test_system_theme_and_unavailable_preference_storage_do_not_block_login(
    browser_server: tuple[str, FastAPI],
) -> None:
    base_url, _ = browser_server
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(color_scheme="dark")
        page.add_init_script(
            """Object.defineProperty(window, 'localStorage', {
              get() { throw new DOMException('blocked', 'SecurityError'); }
            });"""
        )
        _login(page, base_url)
        expect(page.locator("html")).to_have_attribute("data-theme", "dark")
        page.locator("#themeButton").click()
        expect(page.locator("html")).to_have_attribute("data-theme", "light")
        expect(page.locator("#workspaceView")).to_be_visible()
        browser.close()


def test_saved_chat_reload_followup_thinking_delete_and_logout(
    browser_server: tuple[str, FastAPI],
) -> None:
    """Browser fixture verifies UX; PostgreSQL tests verify the real ownership boundary."""
    base_url, app = browser_server
    app.state.saved_chats_enabled = True
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        _login(page, base_url)
        expect(page.locator("#savedChatsPanel")).to_be_visible()
        page.get_by_label("Question", exact=True).fill("What is DNS?")
        page.locator("#askButton").click()
        expect(page.locator("#answer")).to_have_text("Local follow-up answer.")
        assert len(app.state.saved_chats) == 1
        first = app.state.general_requests[-1]
        assert "request_id" in first and "history" not in first and "max_output_tokens" not in first
        _options(page)
        page.get_by_label("Response mode").select_option("thinking")
        page.get_by_label("Question", exact=True).fill("Give an example.")
        page.locator("#askButton").click()
        expect(page.locator("#askedQuestion")).to_have_text("Give an example.")
        expect(page.locator("#askButton")).to_be_enabled()
        assert app.state.general_requests[-1]["thinking"] is True
        page.reload(wait_until="networkidle")
        page.get_by_role("button", name="What is DNS?", exact=True).click()
        expect(page.locator("#askedQuestion")).to_have_text("Give an example.")
        expect(page.locator("#conversationHistory")).to_contain_text("What is DNS?")
        page.get_by_role("button", name="New conversation", exact=True).click()
        expect(page.locator("#resultCard")).to_be_hidden()
        assert len(app.state.saved_chats) == 1  # New does not delete saved history.
        page.get_by_role("button", name="What is DNS?", exact=True).click()
        page.on("dialog", lambda dialog: dialog.accept())
        page.get_by_role("button", name="Delete this conversation").click()
        expect(page.locator("#savedChatsList")).to_be_empty()
        assert not app.state.saved_chats
        _profile_action(page, "#logoutButton")
        expect(page.locator("#savedChatsPanel")).to_be_hidden()
        assert page.locator("#savedChatsList").text_content() == ""
        browser.close()


def test_saved_chat_persian_rtl_literal_title_and_live_memory_separation(
    browser_server: tuple[str, FastAPI],
) -> None:
    base_url, app = browser_server
    app.state.saved_chats_enabled = True
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        _login(page, base_url)
        page.locator("#languageButton").click()
        question = "DNS چیست؟ <img src=x onerror=alert(1)>"
        page.locator("#question").fill(question)
        page.locator("#askButton").click()
        expect(page.locator("#answer")).to_have_text("پاسخ محلیِ پیگیری")
        expect(page.locator("#askButton")).to_be_enabled()
        expect(page.locator(".saved-chat-button")).to_have_text(question)
        assert page.locator("#savedChatsList img").count() == 0
        page.set_viewport_size({"width": 375, "height": 812})
        assert page.locator("html").get_attribute("dir") == "rtl"
        page.locator("#navOpen").click()
        expect(page.locator("#savedChatsHeading")).to_be_visible()
        assert page.locator("#savedChatsPanel").evaluate(
            "el => el.getBoundingClientRect().width >= 250"
        )
        assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth")
        assert page.locator(".saved-chat-button").evaluate(
            "el => el.getBoundingClientRect().height >= 44"
        )
        page.locator(".saved-chat-button").focus()
        assert page.locator(".saved-chat-button").evaluate("el => el === document.activeElement")
        page.screenshot(path="build/chat-ui-fa.png", full_page=True)
        page.keyboard.press("Escape")
        page.emulate_media(reduced_motion="reduce")
        _mode(page, "monitoring")
        expect(page.locator("#thinkingField")).to_be_hidden()
        page.locator("#question").fill("وضعیت فعلی چیست؟")
        page.locator("#askButton").click()
        expect(page.locator("#evidenceBadge")).to_contain_text("Zabbix")
        assert "history" not in app.state.monitoring_requests[-1]
        assert "thinking" not in app.state.monitoring_requests[-1]
        assert sum(len(c["messages"]) for c in app.state.saved_chats.values()) == 1
        browser.close()


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
        expect(page.locator("#workspaceHeading")).to_be_visible()

        _mode(page, "incident")
        target = page.get_by_label("Investigation target")
        expect(target).to_be_visible()
        target.select_option("app")
        page.get_by_label("Question", exact=True).fill("Explain the current application condition.")
        page.locator("#askButton").click()

        expect(page.get_by_text("Live Zabbix + Linux evidence")).to_be_visible()
        expect(page.locator("#askedQuestion")).to_have_text(
            "Explain the current application condition."
        )
        page.locator("#requestDetailsButton").click()
        expect(
            page.locator("#incidentDetail").get_by_text("nextops-app.service", exact=True)
        ).to_be_visible()
        expect(
            page.locator("#incidentDetail").get_by_text("CPU pressure observed", exact=True)
        ).to_be_visible()
        assert app.state.incident_requests[-1]["target_id"] == "app"

        page.locator("#languageButton").click()
        _options(page)
        expect(page.get_by_role("button", name="بررسی رخداد", exact=True)).to_be_visible()
        expect(page.locator("#evidenceBrief")).to_contain_text("زمان گردآوری Linux")
        expect(page.get_by_text("شرکت رایانه خدمات امید سیستم")).to_be_hidden()
        expect(page.locator(".topbar .product-lockup")).to_be_hidden()
        assert page.locator("html").get_attribute("dir") == "rtl"

        page.set_viewport_size({"width": 375, "height": 812})
        assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth") is True
        assert page.get_by_role("button", name="بررسی رخداد").evaluate(
            "element => element.getBoundingClientRect().height >= 44"
        )

        page.emulate_media(reduced_motion="reduce")
        page.set_viewport_size({"width": 844, "height": 390})
        assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth") is True

        _profile_action(page, "#logoutButton")
        expect(page.locator('#loginForm button[type="submit"]')).to_be_visible()
        assert page.evaluate("sessionStorage.getItem('nextops-session')") is None
        assert app.state.logout_requests == 1
        browser.close()


@pytest.mark.parametrize("locale", ["en", "fa"])
def test_named_ai_host_status_selects_the_approved_target_not_the_zabbix_snapshot(
    browser_server: tuple[str, FastAPI],
    locale: str,
) -> None:
    base_url, app = browser_server
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        _login(page, base_url)
        _mode(page, "monitoring")
        if locale == "fa":
            page.locator("#languageButton").click()
            _options(page)
            page.locator('[data-locale="fa"]').click()
        question = (
            "آخرین وضعیت سرور Ai رو بهم بگو"
            if locale == "fa"
            else "Show the current status of the AI server."
        )
        page.locator("#question").fill(question)
        page.locator("#askButton").click()
        expect(page.locator("#resultCard")).to_be_visible()
        expect(page.locator('[data-mode="incident"]')).to_have_attribute("aria-pressed", "true")
        expect(page.locator("#incidentTarget")).to_have_value("ai")
        assert app.state.incident_requests[-1]["target_id"] == "ai"
        assert app.state.incident_requests[-1]["question"] == question
        assert "history" not in app.state.incident_requests[-1]
        assert app.state.monitoring_requests == []
        assert app.state.general_requests == []
        page.locator("#requestDetailsButton").click()
        expect(page.locator("#incidentDetail > div").first).to_contain_text("nextops-app.service")
        expect(page.locator("#incidentDetail > details")).not_to_have_attribute("open", "")
        expect(page.get_by_text("CPU pressure observed")).to_be_hidden()
        page.set_viewport_size({"width": 375, "height": 812})
        assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth") is True
        browser.close()


def test_host_status_intent_does_not_grant_an_unlisted_target_or_route_advice(
    browser_server: tuple[str, FastAPI],
) -> None:
    base_url, app = browser_server
    app.state.incident_targets = ["app"]
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page()
        _login(page, base_url)
        _mode(page, "monitoring")
        page.locator("#question").fill("Show the current status of the AI server.")
        page.locator("#askButton").click()
        expect(page.locator("#resultCard")).to_be_visible()
        assert app.state.incident_requests == []
        assert len(app.state.monitoring_requests) == 1
        _mode(page, "general")
        page.locator("#question").fill("How can I check the AI server status?")
        page.locator("#askButton").click()
        expect(page.locator("#askedQuestion")).to_have_text("How can I check the AI server status?")
        assert len(app.state.general_requests) == 1
        assert app.state.incident_requests == []
        browser.close()


def test_general_fallback_notice_does_not_imply_live_evidence(
    browser_server: tuple[str, FastAPI],
) -> None:
    base_url, _ = browser_server
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        _login(page, base_url)
        page.get_by_label("Question", exact=True).fill("Hi")
        page.locator("#askButton").click()

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
        _mode(page, "incident")
        page.get_by_label("Investigation target").select_option("app")
        page.get_by_label("Question", exact=True).fill("Only show the system files on app.")
        page.get_by_label("Question", exact=True).press("Enter")

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
        page.locator("#requestDetailsButton").click()
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
        _options(page)
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
        _mode(page, "incident")
        page.get_by_label("Investigation target").select_option("app")
        page.get_by_label("Question", exact=True).fill(
            "Show only system file and filesystem evidence for this host. "
            "Do not include CPU, memory, or unrelated Zabbix data."
        )
        page.locator("#askButton").click()

        expect(page.locator("#answer")).to_contain_text("Approved filesystem capacity only")
        expect(page.locator("#evidenceBrief")).to_contain_text("Approved filesystem mounts only")
        page.locator("#requestDetailsButton").click()
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
        _mode(page, "incident")
        page.get_by_label("Investigation target").select_option("app")
        _options(page)
        page.locator(f'.locale-choice[data-locale="{locale}"]').click()
        page.get_by_label("Question", exact=True).fill(question)
        page.locator("#askButton").click()

        expect(page.locator("#evidenceBrief")).to_contain_text(scope)
        expect(page.locator("#integrityNotice")).to_contain_text("deterministic")
        page.locator("#requestDetailsButton").click()
        expect(page.get_by_role("heading", name=focused_heading)).to_be_visible()
        expect(page.get_by_role("heading", name=excluded_heading)).to_be_hidden()
        if scope == "Recorded network observations only":
            expect(page.get_by_role("heading", name="Listening sockets")).to_be_hidden()
        if scope == "Recorded service observations only":
            expect(page.get_by_role("heading", name="High-priority journal")).to_be_hidden()
            expect(page.get_by_text("nginx.service")).to_be_hidden()
        page.get_by_text("Show complete authorized evidence").click()
        expect(page.get_by_role("heading", name=excluded_heading)).to_be_visible()
        if scope == "Recorded service observations only":
            expect(page.get_by_text("nginx.service")).to_be_visible()
        page.set_viewport_size({"width": 375, "height": 812})
        assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth") is True
        browser.close()


@pytest.mark.parametrize("locale", ["en", "fa"])
def test_approved_source_selection_provenance_and_no_fallback(
    browser_server: tuple[str, FastAPI],
    locale: str,
) -> None:
    base_url, app = browser_server
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        _login(page, base_url)
        if locale == "fa":
            page.locator("#languageButton").click()
        _options(page)
        page.locator('[data-mode="monitoring"]').focus()
        page.keyboard.press("Enter")
        expect(page.locator("#sourceSelectionField")).to_be_visible()
        expect(page.locator("#monitoringSource option")).to_have_count(2)
        page.locator("#monitoringSource").select_option("secondary")
        expect(page.locator("#monitoringSourceTarget")).to_have_value("sla")
        assert page.locator("#monitoringSourceTarget img").count() == 0
        page.locator("#question").fill(
            "وضعیت میزبان انتخاب‌شده چیست؟"
            if locale == "fa"
            else "What is the selected host's status?"
        )
        page.locator("#askButton").click()
        expect(page.locator("#evidenceSource")).to_contain_text("secondary / sla")
        expect(page.locator("#evidenceBrief")).to_contain_text("secondary / sla")
        assert app.state.monitoring_requests[-1]["source_id"] == "secondary"
        assert page.locator("html").get_attribute("dir") == ("rtl" if locale == "fa" else "ltr")
        page.set_viewport_size({"width": 375, "height": 812})
        assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth") is True
        app.state.source_failed = True
        count = len(app.state.monitoring_requests)
        page.locator("#question").fill("Another fresh status question")
        page.locator("#askButton").click()
        expect(page.locator("#assistantError")).not_to_be_empty()
        expect(page.locator("#askButton")).to_be_enabled()
        assert len(app.state.monitoring_requests) == count
        expect(page.locator("#monitoringSource")).to_have_value("secondary")
        _profile_action(page, "#logoutButton")
        expect(page.locator("#monitoringSource option")).to_have_count(0)
        expect(page.locator("#monitoringSourceTarget option")).to_have_count(0)
        browser.close()


def test_monitoring_host_inventory_limit_is_explained_in_browser(
    browser_server: tuple[str, FastAPI],
) -> None:
    base_url, _ = browser_server
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        _login(page, base_url)
        _mode(page, "monitoring")
        page.get_by_label("Question", exact=True).fill(
            "Which authorized Zabbix hosts are currently unavailable?"
        )
        page.locator("#askButton").click()

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
        _mode(page, "monitoring")
        page.locator("#question").fill("Which hosts are currently unavailable?")
        page.locator("#askButton").click()
        page.locator("#requestDetailsButton").click()
        expect(page.locator("#evidenceBrief")).to_be_visible()
        assert "history" not in app.state.monitoring_requests[0]
        _mode(page, "general")
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
        _profile_action(page, "#logoutButton")
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
