"""Audit repair regressions against bounded, sanitized loopback fixtures only."""

from __future__ import annotations

import re
from typing import Any
from urllib.parse import urlparse

import pytest
from playwright.sync_api import Page, Route, expect, sync_playwright

from .test_phase2_panel import _launch_browser, _login, _profile_action
from .test_phase2_panel import browser_server as browser_server

pytestmark = pytest.mark.browser


def _sign_in_current_page(page: Page) -> None:
    """Sign in without a document reload that would hide replaced-element regressions."""
    page.locator("#username").fill("owner")
    page.locator("#password").fill("test-password")
    page.locator("#loginForm button[type=submit]").click()
    expect(page.locator("#workspaceView")).to_be_visible()


@pytest.mark.parametrize("script_failure", ["disabled", "app_unavailable"])
def test_login_cannot_serialize_credentials_into_url_when_scripts_fail(
    browser_server: tuple[str, Any], script_failure: str
) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = _launch_browser(p)
        context = browser.new_context(java_script_enabled=script_failure != "disabled")
        page = context.new_page()
        if script_failure == "app_unavailable":
            page.route("**/assets/app.js?*", lambda route: route.abort())
        page.goto(base, wait_until="networkidle")
        expect(page.locator("#loginForm button[type=submit]")).to_be_disabled()
        expect(page.locator("#loginForm")).to_have_attribute("method", "post")
        page.locator("#username").fill("owner")
        page.locator("#password").fill("fixture-only-password")
        page.locator("#password").press("Enter")
        assert urlparse(page.url).query == ""
        # Even native submission bypassing the disabled-button gate has no query credentials.
        with page.expect_request(base + "/") as request:
            page.locator("#loginForm").evaluate("form => form.submit()")
        assert request.value.method == "POST"
        assert urlparse(request.value.url).query == ""
        browser.close()


@pytest.mark.parametrize("storage_failure", ["getter", "methods"])
def test_unavailable_tab_storage_keeps_login_and_logout_usable(
    browser_server: tuple[str, Any], storage_failure: str
) -> None:
    base, app = browser_server
    app.state.saved_chats_enabled = True
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page()
        errors: list[str] = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        if storage_failure == "getter":
            page.add_init_script("""Object.defineProperty(window, 'sessionStorage', {
                get() { throw new DOMException('Storage unavailable', 'SecurityError'); }
            });""")
        else:
            page.add_init_script("""Object.defineProperty(window, 'sessionStorage', {
                value: {
                    getItem() { return null; },
                    setItem() { throw new DOMException('Storage full', 'QuotaExceededError'); },
                    removeItem() { throw new DOMException('Storage unavailable', 'SecurityError'); }
                }
            });""")
        _login(page, base)
        page.locator("#question").fill("A fixture-only question with unavailable tab storage")
        page.locator("#askButton").click()
        expect(page.locator("#resultCard")).to_be_visible()
        _profile_action(page, "#logoutButton")
        expect(page.locator("#loginView")).to_be_visible()
        expect(page.locator("#answer")).to_be_empty()
        expect(page.locator("#savedChatsList")).to_be_empty()
        _sign_in_current_page(page)
        assert not errors
        assert urlparse(page.url).query == ""
        browser.close()


def test_new_chat_during_initialization_keeps_current_session_capabilities(
    browser_server: tuple[str, Any],
) -> None:
    base, app = browser_server
    app.state.saved_chats_enabled = True
    app.state.ready_model = "nextops-qwen3-8-27b-q8-0"
    held: dict[str, Route] = {}

    def hold(route: Route) -> None:
        held[urlparse(route.request.url).path] = route

    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page(viewport={"width": 1672, "height": 941})
        for path in (
            "/api/v1/assistant/ready",
            "/api/v1/monitoring/sources",
            "/api/v1/incidents/targets",
            "/api/v1/conversations/config",
        ):
            page.route("**" + path, hold)
        _login(page, base)
        page.locator("#newChatButton").click()
        assert len(held) == 4
        for route in held.values():
            route.fulfill(response=route.fetch())
        expect(page.locator("#modelStatusLabel")).to_contain_text("Qwen3.8-27B")
        expect(page.locator("#aiStatus")).to_contain_text("ready")
        expect(page.locator("#incidentTarget option")).to_have_count(4)
        expect(page.locator("#monitoringSource option")).to_have_count(2)
        expect(page.locator("#savedChatsPanel")).to_be_visible()
        assert not app.state.general_requests
        assert not app.state.monitoring_requests
        browser.close()


@pytest.mark.parametrize("late_result", ["unauthorized", "unavailable", "old_actor"])
def test_cached_session_initialization_cannot_replace_a_fresh_login(
    browser_server: tuple[str, Any], late_result: str
) -> None:
    base, _ = browser_server
    held: list[Route] = []
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page()
        page.add_init_script("sessionStorage.setItem('nextops-session', 'expired-cached-token')")
        page.route("**/api/v1/me", lambda route: held.append(route), times=1)
        page.goto(base, wait_until="domcontentloaded")
        expect(page.locator("#loginForm button[type=submit]")).to_be_enabled()
        _sign_in_current_page(page)
        expect(page.locator("#usersButton")).not_to_have_class(re.compile(r"\bhidden\b"))
        assert len(held) == 1
        if late_result == "old_actor":
            held[0].fulfill(json={"status": "authenticated", "roles": ["viewer"]})
        else:
            held[0].fulfill(
                status=401 if late_result == "unauthorized" else 503,
                json={"error": {"code": "fixture_old_session"}},
            )
        # A following request settles after the held response, without reloading the page.
        page.locator("#question").fill("Explain a fixture-only technical concept")
        page.locator("#askButton").click()
        expect(page.locator("#resultCard")).to_be_visible()
        expect(page.locator("#workspaceView")).to_be_visible()
        expect(page.locator("#usersButton")).not_to_have_class(re.compile(r"\bhidden\b"))
        expect(page.locator("#loginError")).to_be_empty()
        browser.close()


def test_new_chat_does_not_strand_an_account_list_in_progress(
    browser_server: tuple[str, Any],
) -> None:
    base, _ = browser_server
    held: list[Route] = []
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page(viewport={"width": 1672, "height": 941})
        _login(page, base)
        page.route("**/api/v1/users?offset=*", lambda route: held.append(route))
        _profile_action(page, "#usersButton")
        expect(page.locator("#usersView")).to_have_attribute("aria-busy", "true")
        page.locator("#newChatButton").click()
        held[0].fulfill(response=held[0].fetch())
        expect(page.locator("#usersView")).to_have_attribute("aria-busy", "false")
        expect(page.locator("#usersRefresh")).to_be_enabled()
        expect(page.locator("#workspaceView")).to_be_visible()
        expect(page.locator('[data-nav="ask"]')).to_have_attribute("aria-current", "page")
        page.unroute("**/api/v1/users?offset=*")
        _profile_action(page, "#usersButton")
        expect(page.locator("#usersList .user-row")).to_have_count(1)
        expect(page.locator("#usersRefresh")).to_be_enabled()
        browser.close()


def test_older_initial_saved_chat_list_cannot_replace_the_post_save_list(
    browser_server: tuple[str, Any],
) -> None:
    base, app = browser_server
    app.state.saved_chats_enabled = True
    held: list[Route] = []
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page()
        page.route("**/api/v1/conversations", lambda route: held.append(route), times=1)
        _login(page, base)
        assert len(held) == 1
        initial_list = held[0].fetch()
        assert initial_list.json() == []
        page.locator("#question").fill("A newly saved fixture conversation")
        page.locator("#askButton").click()
        expect(page.locator("#savedChatsList .saved-chat-button")).to_have_count(1)
        held[0].fulfill(response=initial_list)
        page.evaluate("async () => { await fetch('/api/v1/me'); }")
        # The settled composer and current list must retain the newer server snapshot.
        expect(page.locator("#askButton")).to_be_enabled()
        expect(page.locator("#savedChatsList .saved-chat-button")).to_have_count(1)
        expect(page.locator("#savedChatsList")).to_contain_text(
            "A newly saved fixture conversation"
        )
        browser.close()


def test_old_session_target_failure_does_not_clear_new_session_targets(
    browser_server: tuple[str, Any],
) -> None:
    base, app = browser_server
    held: list[Route] = []
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page()
        page.route("**/api/v1/incidents/targets", lambda route: held.append(route), times=1)
        _login(page, base)
        _profile_action(page, "#logoutButton")
        expect(page.locator("#incidentTarget option")).to_have_count(0)
        _sign_in_current_page(page)
        expect(page.locator("#incidentTarget option")).to_have_count(4)
        held[0].fulfill(status=503, json={"error": {"code": "dependency_unavailable"}})
        page.locator("#question").fill("Tell me the current status of the AI server")
        page.locator("#askButton").click()
        expect(page.locator("#resultCard")).to_be_visible()
        expect(page.locator('[data-mode="incident"]')).to_have_attribute("aria-pressed", "true")
        assert app.state.incident_requests[-1]["target_id"] == "ai"
        expect(page.locator("#incidentTarget")).to_be_enabled()
        browser.close()


def test_delayed_target_catalog_cannot_enable_controls_during_generation(
    browser_server: tuple[str, Any],
) -> None:
    base, _ = browser_server
    targets: list[Route] = []
    answers: list[Route] = []
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page()
        page.route("**/api/v1/incidents/targets", lambda route: targets.append(route))
        page.route("**/api/v1/assistant/generate", lambda route: answers.append(route))
        _login(page, base)
        page.locator("#question").fill("Explain a fixture-only technical concept")
        page.locator("#askButton").click()
        expect(page.locator("#cancelRequest")).to_be_visible()
        targets[0].fulfill(response=targets[0].fetch())
        expect(page.locator("#incidentTarget option")).to_have_count(4)
        expect(page.locator("#incidentTarget")).to_be_disabled()
        answers[0].fulfill(response=answers[0].fetch())
        expect(page.locator("#resultCard")).to_be_visible()
        expect(page.locator("#incidentTarget")).to_be_enabled()
        browser.close()


@pytest.mark.parametrize("locale", ["en", "fa"])
def test_filter_preserves_evidence_cursor_and_close_focus(
    browser_server: tuple[str, Any], locale: str
) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page(viewport={"width": 1672, "height": 941})
        _login(page, base)
        page.set_viewport_size({"width": 1672, "height": 941})
        if locale == "fa":
            page.locator("#languageButton").click()
        page.locator('[data-mode="incident"]').click()
        page.locator("#question").fill("Inspect the approved fixture host")
        page.locator("#askButton").click()
        expect(page.locator("#resultCard")).to_be_visible()
        page.locator("#resultCard .response-evidence > summary").click()
        page.locator('#resultCard [data-evidence-index="4"]').click()
        expect(page.locator("#evidencePosition")).to_have_text("5 / 10")
        page.locator('#resultCard [data-evidence-filter="all"]').click()
        expect(page.locator("#evidencePosition")).to_have_text("5 / 10")
        expect(page.locator('#resultCard [data-evidence-index="4"]')).to_have_attribute(
            "aria-current", "true"
        )
        page.locator("#languageButton").click()
        page.locator("#languageButton").click()
        expect(page.locator("#evidencePosition")).to_have_text("5 / 10")
        page.locator("#evidenceNext").click()
        expect(page.locator("#evidencePosition")).to_have_text("6 / 10")
        expect(page.locator("#inspectorContent h3")).to_have_text("nginx.service")
        page.locator("#evidenceClose").click()
        expect(page.locator('#resultCard [data-evidence-filter="all"]')).to_be_focused()
        browser.close()


@pytest.mark.parametrize("reset", ["new_chat", "saved_resume", "logout_login"])
def test_replaced_request_details_keeps_expansion_state_correct(
    browser_server: tuple[str, Any], reset: str
) -> None:
    base, app = browser_server
    app.state.saved_chats_enabled = True
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page()
        _login(page, base)
        page.locator("#question").fill("Initial fixture conversation")
        page.locator("#askButton").click()
        expect(page.locator("#resultCard")).to_be_visible()
        if reset == "new_chat":
            page.locator("#newChatButton").click()
        elif reset == "saved_resume":
            page.locator(".saved-chat-button").click()
            expect(page.locator("#askedQuestion")).to_have_text("Initial fixture conversation")
        else:
            _profile_action(page, "#logoutButton")
            _sign_in_current_page(page)
        page.locator("#question").fill("First turn after fixture reset")
        page.locator("#askButton").click()
        expect(page.locator("#askedQuestion")).to_have_text("First turn after fixture reset")
        page.locator("#requestDetailsButton").click()
        expect(page.locator("#requestDetailsButton")).to_have_attribute("aria-expanded", "true")
        page.locator("#question").fill("Next turn after fixture reset")
        page.locator("#askButton").click()
        expect(page.locator("#askedQuestion")).to_have_text("Next turn after fixture reset")
        expect(page.locator("#evidenceDetails")).not_to_have_attribute("open", "")
        expect(page.locator("#requestDetailsButton")).to_have_attribute("aria-expanded", "false")
        browser.close()


def test_generated_persian_labels_preserve_raw_evidence_and_archived_rows(
    browser_server: tuple[str, Any],
) -> None:
    base, _ = browser_server

    def include_journal(route: Route) -> None:
        response = route.fetch()
        body = response.json()
        linux = body["evidence"]["linux"]
        linux["journal"] = [
            {
                "unit": "nginx.service",
                "message": "Fixture journal observation",
                "observed_at": linux["collected_at"],
            }
        ]
        route.fulfill(response=response, json=body)

    labels = {
        2: "بار سامانه",
        3: "حافظهٔ در دسترس",
        6: "ظرفیت فایل‌سیستم",
        7: "رکورد ژورنال",
        8: "حل‌کنندهٔ نام پیکربندی‌شده",
        9: "مسیر ثبت‌شده",
        10: "سوکت در حال شنود",
    }
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page(viewport={"width": 1672, "height": 941})
        _login(page, base)
        page.set_viewport_size({"width": 1672, "height": 941})
        page.route("**/api/v1/incidents/investigate", include_journal)
        page.locator('[data-mode="incident"]').click()
        page.locator("#question").fill("Inspect the approved fixture host")
        page.locator("#askButton").click()
        expect(page.locator("#resultCard")).to_be_visible()
        page.locator("#resultCard .response-evidence > summary").click()
        raw: dict[int, str] = {}
        for index in labels:
            page.locator(f'#resultCard [data-evidence-index="{index}"]').click()
            raw[index] = page.locator("#panel-raw pre").inner_text()
        page.locator("#languageButton").click()
        for index, label in labels.items():
            page.locator(f'#resultCard [data-evidence-index="{index}"]').click()
            expect(page.locator("#inspectorContent")).to_contain_text(label)
            expect(page.locator("#panel-raw pre")).to_have_text(raw[index])
        page.locator('#resultCard [data-evidence-index="3"]').click()
        expect(page.locator("#inspectorContent h3")).to_have_text("حافظهٔ در دسترس")
        expect(page.locator("#inspectorContent")).to_contain_text("memory_available_bytes")
        page.locator('#resultCard [data-evidence-index="8"]').click()
        expect(page.locator("#inspectorContent")).to_contain_text("حل‌کنندهٔ نام پیکربندی‌شده")
        expect(page.locator("#panel-raw pre")).to_contain_text('"resolver": "10.0.0.1"')
        page.locator("#question").fill("یک پرسش دیگر دربارهٔ میزبان مجاز")
        page.locator("#askButton").click()
        expect(page.locator("#conversationHistory .conversation-turn")).to_have_count(1)
        page.locator("#languageButton").click()
        expect(page.locator('#conversationHistory [data-evidence-index="3"]')).to_contain_text(
            "Memory available"
        )
        page.locator("#languageButton").click()
        expect(page.locator('#conversationHistory [data-evidence-index="3"]')).to_contain_text(
            "حافظهٔ در دسترس"
        )
        page.locator('#conversationHistory [data-evidence-filter="all"]').click()
        expect(page.locator("#evidencePosition")).to_have_text("1 / 11")
        expect(page.locator("#inspectorContent h3")).to_have_text("CPU idle time")
        browser.close()
