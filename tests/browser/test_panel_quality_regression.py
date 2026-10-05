"""Presentation regressions against isolated fixtures, never operational services."""

from __future__ import annotations

import json
from typing import Any

import pytest
from playwright.sync_api import expect, sync_playwright

from .test_phase2_panel import (
    _incident_response,
    _launch_browser,
    _login,
    _options,
    _profile_action,
)
from .test_phase2_panel import browser_server as browser_server

pytestmark = pytest.mark.browser


@pytest.mark.parametrize("locale", ["en", "fa"])
def test_mobile_composer_has_readable_unobscured_typing_area(
    browser_server: tuple[str, Any], locale: str
) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page(viewport={"width": 390, "height": 844})
        _login(page, base)
        page.set_viewport_size({"width": 390, "height": 844})
        if locale == "fa":
            page.locator("#languageButton").click()
        page.locator("#question").fill("Explain a safe, read-only diagnostic for network latency.")
        page.locator("#question").scroll_into_view_if_needed()
        dimensions = page.locator("#question").evaluate(
            "e=>{const s=getComputedStyle(e),r=e.getBoundingClientRect();"
            "return {usable:r.width-parseFloat(s.paddingLeft)-parseFloat(s.paddingRight),"
            "bottom:r.bottom,top:r.top}}"
        )
        assert dimensions["usable"] >= 290
        controls = page.locator("#askButton").bounding_box()
        assert controls is not None and controls["y"] >= dimensions["bottom"]
        assert page.locator("#askButton").evaluate(
            "e=>{const r=e.getBoundingClientRect();return e.contains("
            "document.elementFromPoint(r.x+r.width/2,r.y+r.height/2))}"
        )
        assert page.evaluate("document.documentElement.scrollWidth<=innerWidth")
        browser.close()


@pytest.mark.parametrize("locale", ["en", "fa"])
@pytest.mark.parametrize("width", [390, 1672])
def test_navigation_moves_keyboard_focus_to_destination_without_hidden_drawer_focus(
    browser_server: tuple[str, Any], locale: str, width: int
) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page(viewport={"width": width, "height": 941})
        _login(page, base)
        page.set_viewport_size({"width": width, "height": 941})
        if locale == "fa":
            page.locator("#languageButton").click()
        if width < 1101:
            page.locator("#navOpen").click()
        page.locator('[data-nav="infrastructure"]').focus()
        page.keyboard.press("Enter")
        expect(page.locator("#destinationTitle")).to_be_focused()
        expect(page.locator("#navDialog")).not_to_be_visible()
        page.locator("#languageButton").click()
        expect(page.locator("#destinationTitle")).to_have_text(
            "Infrastructure" if locale == "fa" else "زیرساخت"
        )
        expect(page.locator("#languageButton")).to_be_focused()
        page.locator("#destinationBack").click()
        expect(page.locator("#workspaceHeading")).to_be_focused()
        browser.close()


def test_locale_preserves_selected_evidence_and_empty_details_are_disabled(
    browser_server: tuple[str, Any],
) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page(viewport={"width": 1672, "height": 941})
        _login(page, base)
        page.set_viewport_size({"width": 1672, "height": 941})
        expect(page.locator("#requestDetailsButton")).to_be_disabled()
        _options(page)
        page.locator('[data-mode="incident"]').click()
        page.locator("#incidentTarget").select_option("app")
        page.locator("#composerOptions summary").click()
        page.route(
            "**/api/v1/incidents/investigate",
            lambda route: route.fulfill(json=_incident_response("en", "app")),
        )
        page.locator("#question").fill("Inspect recorded observations only")
        page.locator("#askButton").click()
        expect(page.locator("#requestDetailsButton")).to_be_enabled()
        page.locator('#resultCard [data-evidence-index="1"]').click()
        expect(page.locator("#evidencePosition")).to_have_text("2 / 10")
        page.locator("#languageButton").click()
        expect(page.locator("#evidencePosition")).to_have_text("2 / 10")
        expect(page.locator('#resultCard [data-evidence-index="1"]')).to_have_attribute(
            "aria-current", "true"
        )
        page.locator("#requestDetailsButton").click()
        expect(page.locator("#requestDetailsButton")).to_have_attribute("aria-expanded", "true")
        # The workspace intentionally hides the legacy summary; app.js may still close
        # the native details element. Its toggle event must synchronize the new control.
        page.locator("#evidenceDetails").evaluate("e=>{e.open=false}")
        expect(page.locator("#requestDetailsButton")).to_have_attribute("aria-expanded", "false")
        browser.close()


def test_fresh_session_navigation_matches_visible_workspace(
    browser_server: tuple[str, Any],
) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page()
        _login(page, base)
        page.locator('[data-nav="knowledge"]').click()
        expect(page.locator("#destinationView")).to_be_visible()
        _profile_action(page, "#logoutButton")
        expect(page.locator("#appNav")).to_be_hidden()
        page.locator("#username").fill("owner")
        page.locator("#password").fill("test-password")
        page.locator('#loginForm button[type="submit"]').click()
        expect(page.locator("#workspaceView")).to_be_visible()
        expect(page.locator('[data-nav="investigations"]')).to_have_attribute(
            "aria-current", "page"
        )
        expect(page.locator("#destinationView")).to_be_hidden()
        browser.close()


def test_logout_clears_authorized_destination_and_model_from_hidden_dom(
    browser_server: tuple[str, Any],
) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page()
        _login(page, base)
        page.locator('[data-nav="infrastructure"]').click()
        expect(page.locator("#destinationContent")).not_to_be_empty()
        expect(page.locator("#modelStatusLabel")).to_have_attribute(
            "title", "nextops-qwen3-8b-q4-k-m"
        )
        _profile_action(page, "#logoutButton")
        expect(page.locator("#loginView")).to_be_visible()
        expect(page.locator("#destinationContent")).to_be_empty()
        expect(page.locator("#destinationTitle")).to_be_empty()
        expect(page.locator("#destinationHelp")).to_be_empty()
        assert page.locator("#modelStatusLabel").get_attribute("title") is None
        browser.close()


def test_raw_json_remains_complete_and_copy_matches_after_bounded_redaction(
    browser_server: tuple[str, Any],
) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page()
        _login(page, base)
        page.set_viewport_size({"width": 1672, "height": 941})
        _options(page)
        page.locator('[data-mode="incident"]').click()
        page.locator("#incidentTarget").select_option("app")
        page.locator("#composerOptions summary").click()
        body = _incident_response("en", "app")
        body["evidence"]["linux"]["journal"] = [
            {
                "unit": "nextops-app.service",
                "message": "x" * 5700 + " password=fixture-sensitive " + "y" * 800,
                "observed_at": "2026-09-23T09:59:00Z",
            }
        ]
        page.route("**/api/v1/incidents/investigate", lambda route: route.fulfill(json=body))
        page.locator("#question").fill("Inspect all recorded observations")
        page.locator("#askButton").click()
        expect(page.locator("#resultCard")).to_be_visible()
        for _ in range(7):
            page.locator("#evidenceNext").click()
        rendered = page.locator("#panel-raw code").inner_text()
        data = json.loads(rendered)
        assert data["unit"] == "nextops-app.service"
        assert "fixture-sensitive" not in data["message"]
        assert "[redacted]" in data["message"]
        page.locator("#panel-raw pre").focus()
        expect(page.locator("#panel-raw pre")).to_be_focused()
        expect(page.locator("#panel-raw pre")).to_have_attribute("dir", "ltr")
        page.evaluate("navigator.clipboard.writeText=async value=>{window.fixtureCopy=value}")
        page.locator("#copyRaw").click()
        assert page.evaluate("window.fixtureCopy") == rendered
        browser.close()


@pytest.mark.parametrize("locale", ["en", "fa"])
def test_archived_evidence_context_does_not_claim_fresh_current_collection(
    browser_server: tuple[str, Any], locale: str
) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page()
        _login(page, base)
        if locale == "fa":
            page.locator("#languageButton").click()
        _options(page)
        page.locator('[data-mode="incident"]').click()
        page.locator("#incidentTarget").select_option("app")
        page.locator("#composerOptions summary").click()
        for question in ("First recorded investigation", "Second recorded investigation"):
            page.locator("#question").fill(question)
            page.locator("#askButton").click()
            expect(page.locator("#askedQuestion")).to_have_text(question)
        page.locator('#conversationHistory [data-evidence-index="0"]').click()
        page.locator("#tab-context").click()
        expect(page.locator("#panel-context")).to_contain_text(
            "بدون گردآوری تازه" if locale == "fa" else "no new collection"
        )
        page.keyboard.press("Escape")
        expect(page.locator('#conversationHistory [data-evidence-index="0"]')).to_be_focused()
        browser.close()
