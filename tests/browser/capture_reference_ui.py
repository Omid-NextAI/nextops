"""Deterministic, sanitized screenshots against the isolated design preview only."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright

from .test_phase2_panel import _launch_browser


def capture(base_url: str, output: Path, theme: str = "dark") -> None:
    if urlparse(base_url).hostname not in {"localhost", "127.0.0.1"}:
        raise ValueError(
            "Screenshots require the isolated loopback fixture, never live credentials"
        )
    output.mkdir(parents=True, exist_ok=True)
    findings: list[dict[str, object]] = []
    with sync_playwright() as playwright:
        browser = _launch_browser(playwright)
        for locale, width, height in [
            ("en", 1672, 941),
            ("en", 1440, 900),
            ("en", 1280, 800),
            ("en", 768, 1024),
            ("en", 390, 844),
            ("fa", 1672, 941),
            ("fa", 390, 844),
        ]:
            context = browser.new_context(viewport={"width": width, "height": height})
            context.add_init_script(
                f"localStorage.setItem('nextops-language','{locale}');"
                f"localStorage.setItem('nextops-theme','{theme}');"
                "localStorage.setItem('nextops-motion','paused');"
            )
            requests: list[str] = []
            errors: list[str] = []
            context.route(
                "**/*",
                lambda route, request, requests=requests: (
                    route.continue_()
                    if urlparse(route.request.url).hostname in {"127.0.0.1", "localhost"}
                    else (requests.append(route.request.url), route.abort())[-1]
                ),
            )
            page = context.new_page()
            page.on("pageerror", lambda error, errors=errors: errors.append(str(error)))
            page.on(
                "console",
                lambda message, errors=errors: (
                    errors.append(message.text) if message.type == "error" else None
                ),
            )
            page.on(
                "requestfailed",
                lambda request, errors=errors: errors.append(f"Failed request: {request.url}"),
            )
            page.on(
                "response",
                lambda response, errors=errors: (
                    errors.append(f"HTTP {response.status}: {response.url}")
                    if response.status >= 400
                    else None
                ),
            )
            page.clock.set_fixed_time("2026-09-23T10:00:02Z")
            page.goto(base_url, wait_until="networkidle")
            page.get_by_role("note").filter(has_text="Demo data").wait_for()
            page.screenshot(path=str(output / f"login-{locale}-{width}.png"), full_page=True)
            page.locator("#username").fill("owner")
            page.locator("#password").fill("test-password")
            page.locator('#loginForm button[type="submit"]').click()
            page.locator("#workspaceView:not(.hidden)").wait_for()
            page.wait_for_load_state("networkidle")
            page.screenshot(
                path=str(output / f"workspace-empty-{locale}-{width}.png"), full_page=True
            )
            page.locator("#composerOptions summary").click()
            page.locator('[data-mode="incident"]').click()
            page.locator("#incidentTarget").select_option("app")
            page.locator("#composerOptions summary").click()
            page.locator("#question").fill(
                "شواهد فشار پردازنده در میزبان مجاز را بررسی کن؛ علت را قطعی ندان."
                if locale == "fa"
                else "Investigate CPU pressure on the approved host; do not assume a root cause."
            )
            page.locator("#askButton").click()
            page.locator("#resultCard:not(.hidden)").wait_for()
            page.evaluate("window.scrollTo(0,0)")
            page.screenshot(path=str(output / f"dashboard-{locale}-{width}.png"), full_page=True)
            page.locator("#resultCard .response-evidence > summary").click()
            page.locator('#resultCard [data-evidence-index="0"]').click()
            if width >= 1450:
                page.screenshot(path=str(output / f"evidence-{locale}-{width}.png"), full_page=True)
            if width < 1450:
                # A fixed evidence sheet is a viewport, not the full underlying document.
                page.screenshot(path=str(output / f"evidence-{locale}-{width}.png"))
                page.keyboard.press("Escape")
            findings.append(
                {
                    "locale": locale,
                    "width": width,
                    "viewport_height": height,
                    "document_height": page.evaluate("document.documentElement.scrollHeight"),
                    "overflow": page.evaluate("document.documentElement.scrollWidth > innerWidth"),
                    "errors": errors,
                    "external_requests": requests,
                }
            )
            context.close()
        context = browser.new_context(
            viewport={"width": 1672, "height": 941}, reduced_motion="reduce"
        )
        context.add_init_script(f"localStorage.setItem('nextops-theme','{theme}');")
        context.route(
            "**/*",
            lambda route: (
                route.continue_()
                if urlparse(route.request.url).hostname in {"127.0.0.1", "localhost"}
                else route.abort()
            ),
        )
        page = context.new_page()
        page.clock.set_fixed_time("2026-09-23T10:00:02Z")
        page.goto(base_url, wait_until="networkidle")
        page.screenshot(path=str(output / "login-reduced-motion.png"), full_page=True)
        context.close()
        browser.close()
    (output / "capture-checks.json").write_text(json.dumps(findings, indent=2), encoding="utf-8")
    print(json.dumps(findings, indent=2))
    if any(item["overflow"] or item["errors"] or item["external_requests"] for item in findings):
        raise AssertionError("Visual fixture has overflow, browser errors or external requests")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://127.0.0.1:8878")
    parser.add_argument("--output", type=Path, default=Path("artifacts/ui-reference/pass-1"))
    parser.add_argument("--theme", choices=["dark", "light"], default="dark")
    args = parser.parse_args()
    capture(args.base_url, args.output, args.theme)
