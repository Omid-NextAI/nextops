"""UI-only acceptance: sanitized fixtures, never operational credentials or model qualification."""

from __future__ import annotations

import json
from typing import Any

import pytest
from playwright.sync_api import Page, Route, expect, sync_playwright

from .test_phase2_panel import (
    _incident_response,
    _launch_browser,
    _login,
    _profile_action,
)
from .test_phase2_panel import (
    browser_server as browser_server,
)

pytestmark = pytest.mark.browser


def _options(page: Page) -> None:
    if not page.locator("#composerOptions").evaluate("e=>e.open"):
        page.locator("#composerOptions summary").click()


@pytest.mark.parametrize(
    "width,height", [(1672, 941), (1440, 900), (1280, 800), (768, 1024), (390, 844)]
)
def test_reference_geometry_native_drawer_and_no_external_assets(
    browser_server: tuple[str, Any], width: int, height: int
) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page(viewport={"width": width, "height": height})
        errors: list[str] = []
        requests: list[str] = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.on("request", lambda r: requests.append(r.url))
        _login(page, base)
        page.set_viewport_size({"width": width, "height": height})
        expect(page.locator("#profileMenu")).not_to_have_attribute("open", "")
        if width < 1101:
            page.locator("#navOpen").focus()
            page.keyboard.press("Enter")
            expect(page.locator("#navDialog")).to_be_visible()
            expect(page.locator("#navClose")).to_be_focused()
            page.keyboard.press("Escape")
            expect(page.locator("#navOpen")).to_be_focused()
        if width == 1672:
            page.set_viewport_size({"width": width, "height": height})
            for selector, dimension, size in [
                ("#appNav", "width", 238),
                ("#inspectorSlot", "width", 392),
                (".topbar", "height", 64),
            ]:
                box = page.locator(selector).bounding_box()
                assert box is not None and box[dimension] == size
        assert page.evaluate("document.documentElement.scrollWidth<=innerWidth")
        assert not errors
        assert all(url.startswith(base + "/") for url in requests)
        browser.close()


def test_motion_static_visibility_password_and_login_error_states(
    browser_server: tuple[str, Any],
) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page(reduced_motion="reduce")
        page.goto(base)
        for theme in ("dark", "light"):
            page.evaluate("theme=>document.documentElement.dataset.theme=theme", theme)
            contrast = page.locator("#username").evaluate(
                r"""element => {
                  const style = getComputedStyle(element);
                  const luminance = color => color.match(/[\d.]+/g).slice(0,3)
                    .map(v=>Number(v)/255)
                    .map(v=>v<=.04045?v/12.92:((v+.055)/1.055)**2.4)
                    .reduce((sum,v,i)=>sum+v*[.2126,.7152,.0722][i],0);
                  const ratio = (a,b) => (Math.max(a,b)+.05)/(Math.min(a,b)+.05);
                  const background = luminance(style.backgroundColor);
                  return {text:ratio(luminance(style.color),background),
                          boundary:ratio(luminance(style.borderTopColor),background)};
                }"""
            )
            assert contrast["text"] >= 4.5
            assert contrast["boundary"] >= 3
        expect(page.locator("#motionButton")).to_be_disabled()
        expect(page.locator("#loginTitle")).to_be_visible()
        assert (
            page.locator(".gate-architecture").evaluate("e=>getComputedStyle(e).animationName")
            == "none"
        )
        assert page.locator("#password").get_attribute("autocomplete") == "current-password"
        page.locator("#password").fill("test-password")
        page.locator("#passwordVisibility").click()
        expect(page.locator("#password")).to_have_attribute("type", "text")
        page.locator("#passwordVisibility").click()
        expect(page.locator("#password")).to_have_attribute("type", "password")
        page.locator("#username").fill("owner")
        for code, text in [(401, "incorrect"), (503, "unavailable"), (429, "attempts")]:
            page.route(
                "**/api/v1/login",
                lambda route, request, status_code=code: route.fulfill(
                    status=status_code, json={"error": {"code": "unauthenticated"}}
                ),
            )
            page.locator('#loginForm button[type="submit"]').click()
            expect(page.locator("#loginError")).to_contain_text(text)
            expect(page.locator("#workspaceView")).to_be_hidden()
            page.unroute("**/api/v1/login")
        page.emulate_media(reduced_motion="no-preference")
        page.locator("#motionButton").click()
        assert page.evaluate("localStorage.getItem('nextops-motion')") == "paused"
        page.reload()
        assert page.locator("body").get_attribute("data-motion") == "paused"
        expect(page.locator("#loginTitle")).to_be_visible()
        browser.close()


def test_login_without_gpu_and_hidden_page_pauses_motion(browser_server: tuple[str, Any]) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", args=["--disable-gpu"])
        page = browser.new_page(viewport={"width": 390, "height": 844})
        page.goto(base)
        expect(page.locator("#username")).to_be_visible()
        expect(page.locator("#loginForm button[type=submit]")).to_be_visible()
        assert page.evaluate("document.documentElement.scrollWidth<=innerWidth")
        page.evaluate(
            "Object.defineProperty(document,'hidden',{get:()=>true,configurable:true});"
            "document.dispatchEvent(new Event('visibilitychange'))"
        )
        expect(page.locator("body")).to_have_attribute("data-motion", "paused")
        page.evaluate(
            "Object.defineProperty(document,'hidden',{get:()=>false,configurable:true});"
            "document.dispatchEvent(new Event('visibilitychange'))"
        )
        expect(page.locator("body")).to_have_attribute("data-motion", "playing")
        browser.close()


@pytest.mark.parametrize("locale", ["en", "fa"])
def test_evidence_rows_tabs_copy_archived_provenance_and_safe_fields(
    browser_server: tuple[str, Any], locale: str
) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page(viewport={"width": 1280, "height": 900})
        _login(page, base)
        if locale == "fa":
            page.locator("#languageButton").click()
        expect(page.locator("#appNav")).to_have_attribute(
            "aria-label", "پیمایش اصلی" if locale == "fa" else "Main navigation"
        )
        expect(page.locator("#conversationFeed")).to_have_attribute(
            "aria-label", "گفت‌وگو" if locale == "fa" else "Conversation"
        )
        _options(page)
        page.locator('[data-mode="incident"]').click()
        page.locator("#incidentTarget").select_option("app")
        count = 0

        def result(route: Route) -> None:
            nonlocal count
            count += 1
            body = _incident_response(locale, "app")
            summary = body["evidence"]["zabbix"]["summary"]
            summary["metrics"][0]["value"] = str(count * 10)
            summary["metrics"][0]["stale"] = True
            summary["is_partial"] = True
            summary["partial_reasons"] = ["metrics_truncated"]
            body["private_draft"] = "must-not-be-rendered"
            body["evidence"]["zabbix"]["history"] = [
                {**summary["metrics"][0], "value": "8", "measured_at": "2026-09-23T09:57:00Z"},
                {**summary["metrics"][0], "value": "10", "measured_at": "2026-09-23T09:58:00Z"},
            ]
            route.fulfill(json=body)

        page.route("**/api/v1/incidents/investigate", result)
        for question in ["First bounded investigation", "Second bounded investigation"]:
            page.locator("#question").fill(question)
            page.locator("#askButton").click()
            expect(page.locator("#askedQuestion")).to_have_text(question)
        page.locator('#conversationHistory [data-evidence-index="0"]').focus()
        page.keyboard.press("Enter")
        expect(page.locator("#evidenceDialog")).to_be_visible()
        expect(page.locator("#panel-raw")).to_contain_text('"value": "10"')
        assert "must-not-be-rendered" not in page.locator("body").inner_text()
        expect(page.locator("#inspectorContent")).to_contain_text(
            "قدیمی" if locale == "fa" else "Stale"
        )
        expect(page.locator("#inspectorContent")).to_contain_text(
            "ناقص" if locale == "fa" else "Partial"
        )
        page.evaluate("navigator.clipboard.writeText=async value=>{window.fixtureCopy=value}")
        page.locator("#copyRaw").click()
        assert json.loads(page.evaluate("window.fixtureCopy"))["value"] == "10"
        page.locator("#tab-raw").focus()
        page.keyboard.press("End")
        expect(page.locator("#tab-visualize")).to_be_focused()
        expect(page.locator("#panel-visualize table")).to_be_visible()
        page.locator("#tab-context").click()
        expect(page.locator("#panel-context")).to_contain_text("primary")
        page.keyboard.press("Escape")
        expect(page.locator('#conversationHistory [data-evidence-index="0"]')).to_be_focused()
        _profile_action(page, "#logoutButton")
        assert "10" not in page.locator("#panel-raw").inner_text()
        expect(page.locator("#conversationHistory")).to_be_empty()
        browser.close()


def test_ime_duplicate_requests_cancellation_and_draft_retention(
    browser_server: tuple[str, Any],
) -> None:
    base, app = browser_server
    app.state.general_delay = 1.0
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page()
        _login(page, base)
        page.locator("#question").fill("A retained draft")
        page.locator("#question").dispatch_event(
            "keydown", {"key": "Enter", "isComposing": True, "keyCode": 229}
        )
        assert len(app.state.general_requests) == 0
        page.locator("#question").focus()
        page.keyboard.press("Shift+Enter")
        assert "\n" in page.locator("#question").input_value()
        page.locator("#askButton").click()
        expect(page.locator("#cancelRequest")).to_be_visible()
        page.locator("#assistantForm").evaluate(
            "f=>f.dispatchEvent(new Event('submit',{cancelable:true}))"
        )
        page.locator("#cancelRequest").click()
        expect(page.locator("#assistantError")).to_contain_text(
            "does not prove remote cancellation"
        )
        assert page.locator("#question").input_value().startswith("A retained draft")
        assert len(app.state.general_requests) <= 1
        expect(page.locator("#investigationState")).to_have_text("Request failed")
        browser.close()


def test_command_search_truthful_destinations_zoom_and_logout_clear(
    browser_server: tuple[str, Any],
) -> None:
    base, app = browser_server
    app.state.saved_chats_enabled = True
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page(viewport={"width": 1672, "height": 941})
        _login(page, base)
        page.locator("#question").fill("DNS saved fixture")
        page.locator("#askButton").click()
        expect(page.locator("#askedQuestion")).to_have_text("DNS saved fixture")
        page.keyboard.press("Control+k")
        expect(page.locator("#searchInput")).to_be_focused()
        page.locator("#searchInput").fill("DNS")
        expect(page.locator("#searchResults")).to_contain_text("DNS saved fixture")
        page.keyboard.press("Escape")
        expect(page.locator("#globalSearch")).to_be_focused()
        page.locator('[data-nav="knowledge"]').click()
        expect(page.locator("#destinationHelp")).to_contain_text("not connected")
        page.locator("#destinationBack").click()
        # 200% zoom-equivalent CSS viewport, with real reflow and keyboard drawers.
        page.set_viewport_size({"width": 836, "height": 470})
        assert page.evaluate("document.documentElement.scrollWidth<=innerWidth")
        _profile_action(page, "#logoutButton")
        expect(page.locator("#searchResults")).to_be_empty()
        assert page.evaluate("sessionStorage.getItem('nextops-session')") is None
        expect(page.locator("#appNav")).to_be_hidden()
        browser.close()
