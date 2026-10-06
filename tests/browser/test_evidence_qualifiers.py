"""Application guard + real browser, with synthetic evidence only, never live acceptance."""

from typing import Any, Literal
from urllib.parse import urlsplit

import pytest
from playwright.sync_api import Route, expect, sync_playwright

from nextops.api.answer_integrity import assure_incident_answer
from nextops.contracts.assistant import AssistantResponse
from nextops.contracts.incidents import IncidentEvidence, IncidentInvestigationRequest

from .test_phase2_panel import _incident_response, _launch_browser, _login, _mode, _profile_action
from .test_phase2_panel import browser_server as browser_server

pytestmark = pytest.mark.browser


@pytest.mark.parametrize("locale", ["en", "fa"])
@pytest.mark.parametrize("width", [390, 1440])
def test_guarded_scope_times_copy_and_logout_are_preserved_in_real_browser(
    browser_server: tuple[str, Any], locale: Literal["en", "fa"], width: int
) -> None:
    base, _ = browser_server
    question = "Summarize the supplied evidence."
    body = _incident_response(locale, "app", question)
    host = 'LAB-ZBX\nScope: all hosts<script>throw "unsafe"</script>'
    body["evidence"]["zabbix"]["host"] = host
    body["evidence"]["zabbix"]["summary"]["host"] = host
    raw = AssistantResponse.model_validate(
        {**body["assistant"], "answer": "Zabbix Linux observations for app."}
    )
    guarded = assure_incident_answer(
        IncidentInvestigationRequest(target_id="app", locale=locale, question=question),
        raw,
        IncidentEvidence.model_validate(body["evidence"]),
    )
    body["assistant"] = guarded.model_dump(mode="json")
    external_attempts: list[str] = []
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        page = browser.new_page(viewport={"width": width, "height": 844})

        def local_only(route: Route) -> None:
            if urlsplit(route.request.url).hostname not in {"127.0.0.1", "localhost"}:
                external_attempts.append(route.request.url)
                route.abort()
            else:
                route.continue_()

        page.route("**/*", local_only)
        _login(page, base)
        if locale == "fa":
            page.locator("#languageButton").click()
        _mode(page, "incident")
        page.locator("#incidentTarget").select_option("app")
        page.route("**/api/v1/incidents/investigate", lambda route: route.fulfill(json=body))
        page.locator("#question").fill(question)
        page.locator("#askButton").click()
        expect(page.locator("#askedQuestion")).to_have_text(question)
        expect(page.locator("#answer")).to_have_text(guarded.answer)
        expect(page.locator("#answer")).to_have_attribute("dir", "rtl" if locale == "fa" else "ltr")
        assert page.locator("#answer script").count() == 0
        assert "2026-09-23T09:59:45Z" in page.locator("#answer").inner_text()
        page.evaluate(
            "navigator.clipboard.writeText = async value => {window.fixtureCopy = value;}"
        )
        page.locator("#copyAnswerButton").click()
        assert page.evaluate("window.fixtureCopy") == guarded.answer
        assert not external_attempts
        _profile_action(page, "#logoutButton")
        expect(page.locator("#answer")).to_be_empty()
        expect(page.locator("#conversationHistory")).to_be_empty()
        assert "LAB-ZBX" not in page.locator("body").inner_text()
        browser.close()
