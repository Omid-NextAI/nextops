"""Company redesign regressions using isolated, sanitized browser fixtures only."""

from __future__ import annotations

import hashlib
from typing import Any

import pytest
from playwright.sync_api import expect, sync_playwright

from .test_phase2_panel import STATIC, _launch_browser, _login, _profile_action
from .test_phase2_panel import browser_server as browser_server

pytestmark = pytest.mark.browser


@pytest.mark.parametrize("locale", ["en", "fa"])
def test_busy_controls_and_summary_stay_synchronized(
    browser_server: tuple[str, Any], locale: str
) -> None:
    base, app = browser_server
    app.state.source_delay = 2.0
    app.state.ready_model = "nextops-qwen3-8-27b-q8-0"
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page(viewport={"width": 1672, "height": 941})
        _login(page, base)
        page.set_viewport_size({"width": 1672, "height": 941})
        if locale == "fa":
            page.locator("#languageButton").click()
        expect(page.locator("#inspectorSlot")).to_be_hidden()
        expect(page.locator("#overviewDetails")).to_be_hidden()
        expect(page.locator("#executionDetails")).to_be_hidden()
        page.locator("#composerOptions summary").click()
        # Open options must not cover the modes, including the RTL layout.
        page.locator('[data-mode="monitoring"]').click()
        page.locator("#monitoringSource").select_option("secondary")
        page.locator("#monitoringSourceTarget").select_option("sla")
        page.locator("#question").fill("Inspect the selected source without changes")
        page.locator("#askButton").click()
        expect(page.locator("body")).to_have_attribute("data-request-busy", "true")
        expect(page.locator("#investigationValue")).to_have_text(
            page.locator("#investigationState").inner_text()
        )
        expect(page.locator("#conversationFeed")).to_have_attribute("aria-busy", "true")
        expect(page.locator("#askButton")).to_be_hidden()
        expect(page.locator("#cancelRequest")).to_be_visible()
        for selector in (
            '[data-mode="general"]',
            "#monitoringSource",
            "#monitoringSourceTarget",
            '[data-monitoring-shortcut="problems"]',
        ):
            expect(page.locator(selector)).to_be_disabled()
        expect(page.locator("#resultCard")).to_be_visible()
        expect(page.locator("body")).to_have_attribute("data-request-busy", "false")
        expect(page.locator("#askButton")).to_be_visible()
        expect(page.locator("#cancelRequest")).to_be_hidden()
        expect(page.locator("#modelStatusLabel")).to_contain_text("Qwen3.8-27B")
        expect(page.locator("#investigationValue")).to_have_text(
            page.locator("#investigationState").inner_text()
        )
        assert len(app.state.monitoring_requests) == 1
        assert app.state.monitoring_requests[0]["source_id"] == "secondary"
        browser.close()


@pytest.mark.parametrize("locale", ["en", "fa"])
def test_real_model_label_survives_saved_resume_and_new_chat(
    browser_server: tuple[str, Any], locale: str
) -> None:
    base, app = browser_server
    app.state.saved_chats_enabled = True
    app.state.ready_model = "nextops-qwen3-8-27b-q8-0"
    app.state.ready_context = 16384
    app.state.thinking_allowed = False
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page(viewport={"width": 1672, "height": 941})
        _login(page, base)
        page.set_viewport_size({"width": 1672, "height": 941})
        if locale == "fa":
            page.locator("#languageButton").click()
        page.locator("#question").fill("Remember a fixture-only technical question")
        page.locator("#askButton").click()
        expect(page.locator("#answer")).to_be_visible()
        page.reload(wait_until="networkidle")
        page.locator(".saved-chat-button").click()
        expect(page.locator("#askedQuestion")).to_have_text(
            "Remember a fixture-only technical question"
        )
        expect(page.locator("#modelStatusLabel")).to_contain_text("Qwen3.8-27B")
        page.locator("#newChatButton").click()
        expect(page.locator("#modelStatusLabel")).to_contain_text("Qwen3.8-27B")
        page.locator("#modelStatusLabel").click()
        expect(page.locator("#capabilitiesContent")).to_contain_text(
            "۱۶٬۳۸۴" if locale == "fa" else "16,384"
        )
        page.locator("#closeCapabilities").click()
        _profile_action(page, "#logoutButton")
        expect(page.locator("#capabilitiesContent")).to_be_empty()
        expect(page.locator("#modelStatusLabel")).to_be_hidden()
        expect(page.locator("#savedChatsList")).to_be_empty()
        browser.close()


def test_evidence_is_on_demand_and_resizes_without_losing_selection(
    browser_server: tuple[str, Any],
) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page(viewport={"width": 1672, "height": 941})
        _login(page, base)
        page.set_viewport_size({"width": 1672, "height": 941})
        page.locator('[data-mode="incident"]').click()
        page.locator("#incidentTarget").select_option("app")
        page.locator("#question").fill("Inspect the approved host")
        page.locator("#askButton").click()
        expect(page.locator("#resultCard")).to_be_visible()
        expect(page.locator("#inspectorSlot")).to_be_hidden()
        expect(page.locator("#resultCard [data-evidence-index]").first).to_be_hidden()
        page.locator("#resultCard .response-evidence > summary").click()
        row = page.locator('#resultCard [data-evidence-index="1"]')
        row.focus()
        page.keyboard.press("Enter")
        expect(row).to_have_attribute("aria-current", "true")
        expect(page.locator("#evidenceClose")).to_be_focused()
        box = page.locator("#inspectorSlot").bounding_box()
        assert box and box["width"] == 392
        page.locator("#evidenceClose").click()
        expect(row).to_be_focused()
        page.set_viewport_size({"width": 390, "height": 844})
        row.click()
        expect(page.locator("#evidenceDialog")).to_be_visible()
        position = page.locator("#evidencePosition").inner_text()
        page.set_viewport_size({"width": 1672, "height": 941})
        expect(page.locator("#evidenceDialog")).to_be_hidden()
        expect(page.locator("#inspectorSlot")).to_be_visible()
        expect(page.locator("#evidencePosition")).to_have_text(position)
        page.locator("#evidenceClose").click()
        expect(row).to_be_focused()
        browser.close()


def test_supplied_brand_assets_are_served_unchanged(browser_server: tuple[str, Any]) -> None:
    base, _ = browser_server
    digests = {
        "ocs-logo-dark.jpg": "46ddba23a4b55f5f35d90bd4f41f1fe8f6e35bcc3c396931e58be219ffff072d",
        "ocs-logo-light.jpg": "e9f6390b99b971d996dbb3e3d777d4efb53ac5d4823124fa12a142bbc6716c48",
    }
    with sync_playwright() as p:
        browser = _launch_browser(p)
        context = browser.new_context()
        for filename, digest in digests.items():
            response = context.request.get(f"{base}/assets/{filename}")
            assert response.ok and response.headers["content-type"] == "image/jpeg"
            assert hashlib.sha256(response.body()).hexdigest() == digest
            assert response.body() == (STATIC / filename).read_bytes()
        browser.close()


def test_password_locale_and_settings_theme_controls_follow_actual_state(
    browser_server: tuple[str, Any],
) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page(color_scheme="light")
        page.goto(base)
        page.locator("#passwordVisibility").click()
        page.locator("#languageButton").click()
        expect(page.locator("#passwordVisibility")).to_have_attribute(
            "aria-label", "پنهان‌کردن گذرواژه"
        )
        page.locator("#languageButton").click()
        _login(page, base)
        page.locator('[data-nav="settings"]').click()
        control = page.locator("[data-theme-preference]")
        expect(control).to_have_text("Use dark theme")
        control.click()
        expect(control).to_have_text("Use light theme")
        page.locator("#themeButton").click()
        expect(control).to_have_text("Use dark theme")
        page.locator("#languageButton").click()
        expect(control).to_have_text("استفاده از پوستهٔ تیره")
        browser.close()
