"""Presentation regressions against isolated fixtures, never operational services."""

from __future__ import annotations

import json
from typing import Any

import pytest
from playwright.sync_api import Page, expect, sync_playwright

from .test_phase2_panel import (
    _incident_response,
    _launch_browser,
    _login,
    _options,
    _profile_action,
)
from .test_phase2_panel import browser_server as browser_server

pytestmark = pytest.mark.browser


def _prepare_freshness_case(page: Page, base: str, locale: str, partial: bool = False) -> None:
    page.clock.install(time="2026-09-23T10:00:02Z")
    _login(page, base)
    page.set_viewport_size({"width": 1672, "height": 941})
    if locale == "fa":
        page.locator("#languageButton").click()
    _options(page)
    page.locator('[data-mode="incident"]').click()
    page.locator("#incidentTarget").select_option("app")
    page.locator("#composerOptions summary").click()
    # Test-only instrumentation, outside the shipped application. Track only the
    # presentation callback, not auth/request timers or private application state.
    page.evaluate(
        """() => {
          const schedule=window.setTimeout, cancel=window.clearTimeout, active=new Set();
          let ticks=0, maximum=0;
          window.setTimeout=(callback, delay, ...args)=>{
            if(callback.name!=='refreshFreshness')return schedule(callback,delay,...args);
            const id=schedule(()=>{active.delete(id);ticks++;callback(...args)},delay);
            active.add(id);maximum=Math.max(maximum,active.size);return id;
          };
          window.clearTimeout=id=>{active.delete(id);cancel(id)};
          window.fixtureFreshnessTimers=()=>({pending:active.size,ticks,maximum});
        }"""
    )
    body = _incident_response(locale, "app")
    body["evidence"]["zabbix"]["is_partial"] = partial
    body["evidence"]["zabbix"]["summary"]["is_partial"] = partial
    page.route("**/api/v1/incidents/investigate", lambda route: route.fulfill(json=body))
    page.locator("#question").fill("Inspect recorded observations only")
    page.locator("#askButton").click()
    expect(page.locator("#resultCard")).to_be_visible()
    page.wait_for_load_state("networkidle")
    page.locator("#resultCard .response-evidence > summary").click()
    page.locator('#resultCard [data-followup="evidence"]').click()


@pytest.mark.parametrize("locale", ["en", "fa"])
@pytest.mark.parametrize("partial", [False, True])
def test_visible_evidence_ages_without_requery_or_losing_selected_context(
    browser_server: tuple[str, Any], locale: str, partial: bool
) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page()
        _prepare_freshness_case(page, base, locale, partial)
        page.locator('#resultCard [data-evidence-index="1"]').click()
        expect(page.locator("#evidencePosition")).to_have_text("2 / 10")
        partial_label = "ناقص" if locale == "fa" else "Partial"
        fresh_label = "قدیمی علامت‌گذاری نشده" if locale == "fa" else "Not marked stale"
        expect(page.locator("#inspectorContent .freshness")).to_have_text(
            partial_label if partial else fresh_label
        )
        expect(page.locator("#inspectorContent dd").nth(8)).to_have_text(
            partial_label if partial else fresh_label
        )
        page.locator("#tab-context").click()
        page.locator("#tab-context").focus()
        context = page.locator("#panel-context").inner_text()
        raw = page.locator("#panel-raw code").text_content()
        collected = page.locator("#inspectorContent dd").nth(2).inner_text()
        requests: list[str] = []
        page.on("request", lambda request: requests.append(request.url))
        page.clock.fast_forward(301_000)
        stale_label = "قدیمی" if locale == "fa" else "Stale"
        expect(page.locator("#inspectorContent .freshness")).to_have_text(stale_label)
        expect(page.locator("#inspectorContent dd").nth(8)).to_have_text(
            stale_label + (f" · {partial_label}" if partial else "")
        )
        expect(page.locator("#evidencePosition")).to_have_text("2 / 10")
        expect(page.locator('#resultCard [data-evidence-index="1"]')).to_have_attribute(
            "aria-current", "true"
        )
        expect(page.locator("#tab-context")).to_have_attribute("aria-selected", "true")
        expect(page.locator("#tab-context")).to_be_focused()
        assert page.locator("#panel-context").inner_text() == context
        assert page.locator("#panel-raw code").text_content() == raw
        assert page.locator("#inspectorContent dd").nth(2).inner_text() == collected
        assert requests == []
        assert page.evaluate("window.fixtureFreshnessTimers().pending") == 0
        assert page.evaluate("window.fixtureFreshnessTimers().maximum") == 1
        browser.close()


@pytest.mark.parametrize("locale", ["en", "fa"])
def test_freshness_changes_only_after_existing_five_minute_collection_boundary(
    browser_server: tuple[str, Any], locale: str
) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page()
        _prepare_freshness_case(page, base, locale, partial=True)
        page.clock.pause_at("2026-09-23T10:04:59Z")
        page.clock.run_for(1_000)
        expect(page.locator("#inspectorContent .freshness")).to_have_text(
            "ناقص" if locale == "fa" else "Partial"
        )
        assert page.evaluate("Date.now()") == 1_790_157_900_000
        assert page.evaluate("window.fixtureFreshnessTimers().pending") == 1
        page.clock.run_for(1)
        expect(page.locator("#inspectorContent dd").nth(8)).to_have_text(
            "قدیمی · ناقص" if locale == "fa" else "Stale · Partial"
        )
        assert page.evaluate("window.fixtureFreshnessTimers().pending") == 0
        browser.close()


@pytest.mark.parametrize("locale", ["en", "fa"])
@pytest.mark.parametrize("age_while_hidden", [False, True])
def test_visible_aging_announces_once_with_context_without_focus_or_hidden_updates(
    browser_server: tuple[str, Any], locale: str, age_while_hidden: bool
) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page()
        _prepare_freshness_case(page, base, locale, partial=True)
        announcement = page.locator("#evidenceFreshnessStatus")
        expect(announcement).to_have_count(1)
        expect(announcement).to_have_attribute("role", "status")
        expect(announcement).to_have_attribute("aria-live", "polite")
        expect(announcement).to_have_attribute("aria-atomic", "true")
        expect(announcement).to_be_empty()
        page.evaluate(
            """() => {
              const status=document.getElementById('evidenceFreshnessStatus');
              window.fixtureFreshnessAnnouncements=[];
              new MutationObserver(()=>{
                if(status.textContent)window.fixtureFreshnessAnnouncements.push(status.textContent);
              }).observe(status,{childList:true,characterData:true,subtree:true});
            }"""
        )
        page.locator("#tab-context").click()
        page.locator("#tab-context").focus()
        if age_while_hidden:
            page.evaluate(
                "Object.defineProperty(document,'hidden',{get:()=>true,configurable:true});"
                "document.dispatchEvent(new Event('visibilitychange'))"
            )
        page.clock.fast_forward(301_000)
        if age_while_hidden:
            expect(announcement).to_be_empty()
            assert page.evaluate("window.fixtureFreshnessAnnouncements") == []
            page.evaluate(
                "Object.defineProperty(document,'hidden',{get:()=>false,configurable:true});"
                "document.dispatchEvent(new Event('visibilitychange'))"
            )
        message = (
            "تازگی: قدیمی · ناقص. بیش از پنج دقیقه از گردآوری گذشته است."
            if locale == "fa"
            else "Freshness: Stale · Partial. Collection is older than five minutes."
        )
        expect(announcement).to_have_text(message)
        assert page.evaluate("window.fixtureFreshnessAnnouncements") == [message]
        expect(page.locator("#tab-context")).to_be_focused()
        page.evaluate("document.dispatchEvent(new Event('visibilitychange'))")
        page.clock.fast_forward(301_000)
        assert page.evaluate("window.fixtureFreshnessAnnouncements") == [message]
        # Selection and translation create an empty status, not a new age warning.
        page.locator("#evidenceNext").click()
        expect(announcement).to_be_empty()
        page.locator("#languageButton").click()
        expect(announcement).to_be_empty()
        _profile_action(page, "#logoutButton")
        expect(announcement).to_have_count(0)
        page.clock.fast_forward(301_000)
        assert page.evaluate("window.fixtureFreshnessAnnouncements") == [message]
        browser.close()


@pytest.mark.parametrize("locale", ["en", "fa"])
def test_hidden_page_clears_freshness_timer_and_resumes_aged_partial_without_requery(
    browser_server: tuple[str, Any], locale: str
) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page()
        _prepare_freshness_case(page, base, locale, partial=True)
        assert page.evaluate("window.fixtureFreshnessTimers().pending") == 1
        requests: list[str] = []
        page.on("request", lambda request: requests.append(request.url))
        page.evaluate(
            "Object.defineProperty(document,'hidden',{get:()=>true,configurable:true});"
            "document.dispatchEvent(new Event('visibilitychange'))"
        )
        assert page.evaluate("window.fixtureFreshnessTimers().pending") == 0
        ticks = page.evaluate("window.fixtureFreshnessTimers().ticks")
        page.clock.fast_forward(301_000)
        assert page.evaluate("window.fixtureFreshnessTimers().ticks") == ticks
        page.evaluate(
            "Object.defineProperty(document,'hidden',{get:()=>false,configurable:true});"
            "document.dispatchEvent(new Event('visibilitychange'))"
        )
        expect(page.locator("#inspectorContent .freshness")).to_have_text(
            "قدیمی" if locale == "fa" else "Stale"
        )
        expect(page.locator("#inspectorContent dd").nth(8)).to_have_text(
            "قدیمی · ناقص" if locale == "fa" else "Stale · Partial"
        )
        expect(page.locator("#evidencePosition")).to_have_text("1 / 10")
        assert page.evaluate("window.fixtureFreshnessTimers().pending") == 0
        assert requests == []
        browser.close()


@pytest.mark.parametrize("locale", ["en", "fa"])
def test_freshness_timer_is_bounded_and_cleared_when_view_unmounts_closes_or_logs_out(
    browser_server: tuple[str, Any], locale: str
) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page()
        _prepare_freshness_case(page, base, locale)
        expect(page.locator("#evidencePosition")).to_have_text("1 / 10")
        assert page.evaluate("window.fixtureFreshnessTimers().pending") == 1
        page.evaluate("window.dispatchEvent(new Event('pagehide'))")
        assert page.evaluate("window.fixtureFreshnessTimers().pending") == 0
        page.clock.fast_forward(1_000)
        page.evaluate("window.dispatchEvent(new Event('pageshow'))")
        assert page.evaluate("window.fixtureFreshnessTimers().pending") == 1
        page.evaluate(
            "window.fixtureDetachedInspector=document.getElementById('evidenceInspector');"
            "window.fixtureDetachedInspector.remove()"
        )
        assert page.evaluate("window.fixtureFreshnessTimers().pending") == 0
        page.clock.fast_forward(1_000)
        page.evaluate(
            "document.getElementById('inspectorSlot').append(window.fixtureDetachedInspector)"
        )
        assert page.evaluate("window.fixtureFreshnessTimers().pending") == 1
        requests: list[str] = []
        page.on("request", lambda request: requests.append(request.url))
        page.locator('[data-nav="knowledge"]').click()
        assert page.evaluate("window.fixtureFreshnessTimers().pending") == 0
        page.clock.fast_forward(1_000)
        page.locator('[data-nav="investigations"]').click()
        assert page.evaluate("window.fixtureFreshnessTimers().pending") == 1
        page.locator("#evidenceClose").click()
        assert page.evaluate("window.fixtureFreshnessTimers().pending") == 0
        page.clock.fast_forward(1_000)
        page.locator('#resultCard [data-evidence-index="0"]').click()
        assert page.evaluate("window.fixtureFreshnessTimers().pending") == 1
        page.set_viewport_size({"width": 1280, "height": 800})
        expect(page.locator("#evidenceInspector")).to_be_hidden()
        page.wait_for_function("window.fixtureFreshnessTimers().pending===0")
        assert page.evaluate("window.fixtureFreshnessTimers().pending") == 0
        page.locator('#resultCard [data-evidence-index="0"]').click()
        expect(page.locator("#evidenceDialog")).to_be_visible()
        assert page.evaluate("window.fixtureFreshnessTimers().pending") == 1
        page.keyboard.press("Escape")
        expect(page.locator("#evidenceDialog")).to_be_hidden()
        assert page.evaluate("window.fixtureFreshnessTimers().pending") == 0
        page.set_viewport_size({"width": 1672, "height": 941})
        expect(page.locator("#evidenceInspector")).to_be_visible()
        page.wait_for_function("window.fixtureFreshnessTimers().pending===1")
        assert page.evaluate("window.fixtureFreshnessTimers().pending") == 1
        assert requests == []
        _profile_action(page, "#logoutButton")
        expect(page.locator("#loginView")).to_be_visible()
        assert page.evaluate("window.fixtureFreshnessTimers().pending") == 0
        ticks = page.evaluate("window.fixtureFreshnessTimers().ticks")
        page.wait_for_load_state("networkidle")
        requests.clear()
        page.clock.fast_forward(301_000)
        assert page.evaluate("window.fixtureFreshnessTimers().ticks") == ticks
        assert page.evaluate("window.fixtureFreshnessTimers().maximum") == 1
        expect(page.locator("#inspectorContent")).not_to_contain_text("CPU idle time")
        assert requests == []
        browser.close()


@pytest.mark.parametrize("locale", ["en", "fa"])
def test_explicit_stale_evidence_takes_precedence_over_partial_without_timer(
    browser_server: tuple[str, Any], locale: str
) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page()
        _prepare_freshness_case(page, base, locale, partial=True)
        body = _incident_response(locale, "app")
        body["evidence"]["zabbix"]["summary"]["metrics"][0]["stale"] = True
        body["evidence"]["zabbix"]["summary"]["is_partial"] = True
        page.route("**/api/v1/incidents/investigate", lambda route: route.fulfill(json=body))
        page.locator("#question").fill("Inspect the explicitly stale metric")
        page.locator("#askButton").click()
        expect(page.locator("#askedQuestion")).to_have_text("Inspect the explicitly stale metric")
        expect(page.locator("#inspectorContent .freshness")).to_have_text(
            "قدیمی" if locale == "fa" else "Stale"
        )
        expect(page.locator("#inspectorContent dd").nth(8)).to_have_text(
            "قدیمی · ناقص" if locale == "fa" else "Stale · Partial"
        )
        assert page.evaluate("window.fixtureFreshnessTimers().pending") == 0
        browser.close()


@pytest.mark.parametrize("locale", ["en", "fa"])
def test_archived_selected_observation_ages_without_becoming_a_new_collection(
    browser_server: tuple[str, Any], locale: str
) -> None:
    base, _ = browser_server
    with sync_playwright() as p:
        browser = _launch_browser(p)
        page = browser.new_page()
        _prepare_freshness_case(page, base, locale, partial=True)
        page.locator("#question").fill("Second recorded investigation")
        page.locator("#askButton").click()
        expect(page.locator("#askedQuestion")).to_have_text("Second recorded investigation")
        row = page.locator('#conversationHistory [data-evidence-index="1"]')
        row.click()
        expect(page.locator("#evidencePosition")).to_have_text("2 / 10")
        page.locator("#tab-context").click()
        expect(page.locator("#panel-context")).to_contain_text(
            "بدون گردآوری تازه" if locale == "fa" else "no new collection"
        )
        context = page.locator("#panel-context").inner_text()
        page.wait_for_load_state("networkidle")
        requests: list[str] = []
        page.on("request", lambda request: requests.append(request.url))
        page.clock.fast_forward(301_000)
        expect(page.locator("#inspectorContent dd").nth(8)).to_have_text(
            "قدیمی · ناقص" if locale == "fa" else "Stale · Partial"
        )
        expect(row).to_have_attribute("aria-current", "true")
        expect(page.locator('#resultCard [data-evidence-index="1"]')).to_have_attribute(
            "aria-current", "false"
        )
        expect(page.locator("#evidencePosition")).to_have_text("2 / 10")
        assert page.locator("#panel-context").inner_text() == context
        assert requests == []
        browser.close()


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
        transport_errors: list[str] = []
        page.on(
            "requestfailed",
            lambda request: transport_errors.append(
                f"{request.method} {request.url}: {request.failure}"
            ),
        )
        try:
            _login(page, base)
        except Exception as error:
            error.add_note(f"Isolated fixture transport diagnostics: {transport_errors}")
            raise
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
        page.locator("#resultCard .response-evidence > summary").click()
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
        expect(page.locator('[data-nav="ask"]')).to_have_attribute("aria-current", "page")
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
        page.locator('#resultCard [data-followup="evidence"]').click()
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
        page.locator("#conversationHistory .response-evidence > summary").first.click()
        page.locator('#conversationHistory [data-evidence-index="0"]').click()
        page.locator("#tab-context").click()
        expect(page.locator("#panel-context")).to_contain_text(
            "بدون گردآوری تازه" if locale == "fa" else "no new collection"
        )
        page.keyboard.press("Escape")
        expect(page.locator('#conversationHistory [data-evidence-index="0"]')).to_be_focused()
        browser.close()
