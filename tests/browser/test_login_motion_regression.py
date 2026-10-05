"""Real SVG motion and responsive login checks; sanitized loopback fixtures only."""

from __future__ import annotations

import socket
import threading
import time
from collections.abc import Iterator
from pathlib import Path
from typing import Any, cast
from urllib.parse import urlparse
from urllib.request import urlopen

import pytest
import uvicorn
from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import Page, expect, sync_playwright

from .test_phase2_panel import _profile_action
from .ui_preview import create_preview

pytestmark = pytest.mark.browser
SCREENSHOTS = Path("artifacts/ui-reference/login-motion-repair")


@pytest.fixture()
def motion_server() -> Iterator[str]:
    """Use the production-equivalent restrictive CSP, unlike the plain UI fixture."""
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        port = int(probe.getsockname()[1])
    server = uvicorn.Server(
        uvicorn.Config(
            create_preview(), host="127.0.0.1", port=port, log_level="error", access_log=False
        )
    )
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{port}"
    try:
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            try:
                with urlopen(base, timeout=0.25) as response:
                    if response.status == 200:
                        break
            except OSError:
                time.sleep(0.05)
        else:
            raise RuntimeError("isolated motion fixture did not start")
        yield base
    finally:
        server.should_exit = True
        thread.join(timeout=5)


def _browser(playwright: Any) -> Any:
    # The decorative scene and real form must not require hardware acceleration.
    try:
        return playwright.chromium.launch(args=["--disable-gpu"])
    except PlaywrightError:
        return playwright.chromium.launch(channel="chrome", args=["--disable-gpu"])


def _scene_state(page: Page) -> list[dict[str, str]]:
    return cast(
        list[dict[str, str]],
        page.locator(".signal,.gate-architecture").evaluate_all(
            "elements=>elements.map(e=>({transform:getComputedStyle(e).transform,"
            "opacity:getComputedStyle(e).opacity,playState:getComputedStyle(e).animationPlayState}))"
        ),
    )


def _settle(page: Page) -> None:
    page.evaluate("()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))")


@pytest.mark.parametrize(
    "locale,width,height",
    [
        ("en", 1672, 941),
        ("en", 1440, 900),
        ("en", 1280, 800),
        ("en", 768, 1024),
        ("en", 390, 844),
        ("fa", 1672, 941),
        ("fa", 768, 1024),
        ("fa", 390, 844),
    ],
)
def test_actual_motion_and_visible_compact_scene_under_strict_csp(
    motion_server: str, locale: str, width: int, height: int
) -> None:
    with sync_playwright() as playwright:
        browser = _browser(playwright)
        context = browser.new_context(
            viewport={"width": width, "height": height}, reduced_motion="no-preference"
        )
        context.add_init_script(
            f"localStorage.setItem('nextops-language','{locale}');"
            "localStorage.setItem('nextops-theme','dark');"
        )
        external: list[str] = []

        def local_only(route: Any) -> None:
            if urlparse(route.request.url).hostname == "127.0.0.1":
                route.continue_()
            else:
                external.append(route.request.url)
                route.abort()

        context.route("**/*", local_only)
        page = context.new_page()
        errors: list[str] = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.on(
            "console",
            lambda message: errors.append(message.text) if message.type == "error" else None,
        )
        response = page.goto(motion_server, wait_until="networkidle")
        assert response is not None
        assert "style-src 'self'" in response.headers["content-security-policy"]
        expect(page.locator("body")).to_have_attribute("data-motion", "playing")
        expect(page.locator(".gate-scene")).to_be_visible()
        assert page.locator(".gate-scene").evaluate("e=>getComputedStyle(e).zIndex") != "-1"
        before = _scene_state(page)
        # Measure an actual animation interval, not an absent UI condition.
        page.wait_for_timeout(650)
        after = _scene_state(page)
        assert any(
            first["transform"] != second["transform"]
            for first, second in zip(before, after, strict=True)
        )
        assert all(value["playState"] == "running" for value in after)
        assert page.evaluate("document.documentElement.scrollWidth<=innerWidth")
        SCREENSHOTS.mkdir(parents=True, exist_ok=True)
        page.screenshot(
            path=str(SCREENSHOTS / f"login-{locale}-{width}-playing.png"), full_page=True
        )
        page.locator("#motionButton").focus()
        page.keyboard.press("Space")
        expect(page.locator("body")).to_have_attribute("data-motion", "paused")
        _settle(page)
        paused = _scene_state(page)
        page.wait_for_timeout(300)
        assert _scene_state(page) == paused
        expect(page.locator("#motionButton")).to_contain_text(
            "ادامه" if locale == "fa" else "Resume"
        )
        page.keyboard.press("Space")
        expect(page.locator("body")).to_have_attribute("data-motion", "playing")
        assert (
            page.locator("#loginTitle").evaluate("e=>getComputedStyle(e).animationName") == "none"
        )
        # The normal-flow graphic cannot intercept credentials or prevent reaching submit.
        page.locator("#username").fill("owner")
        page.locator("#password").fill("test-password")
        page.locator('#loginForm button[type="submit"]').click()
        expect(page.locator("#workspaceView")).to_be_visible()
        expect(page.locator("body")).to_have_attribute("data-motion-reason", "authenticated")
        assert page.locator("#loginView").evaluate("e=>e.getAnimations({subtree:true}).length") == 0
        assert not errors
        assert not external
        context.close()
        browser.close()


def test_pause_preference_reduced_motion_and_hidden_lifecycle(motion_server: str) -> None:
    with sync_playwright() as playwright:
        browser = _browser(playwright)
        context = browser.new_context(viewport={"width": 1672, "height": 941})
        context.add_init_script("localStorage.setItem('nextops-theme','dark')")
        page = context.new_page()
        page.goto(motion_server, wait_until="networkidle")
        page.locator("#motionButton").click()
        page.reload(wait_until="networkidle")
        expect(page.locator("body")).to_have_attribute("data-motion-reason", "preference")
        expect(page.locator("#loginTitle")).to_be_visible()
        assert page.locator("#motionButton use").get_attribute("href") == "#i-chevron"
        page.locator("#motionButton").click()
        page.emulate_media(reduced_motion="reduce")
        expect(page.locator("body")).to_have_attribute("data-motion-reason", "reduced")
        expect(page.locator("#motionButton")).to_be_disabled()
        assert page.locator("#loginView").evaluate("e=>e.getAnimations({subtree:true}).length") == 0
        SCREENSHOTS.mkdir(parents=True, exist_ok=True)
        page.screenshot(path=str(SCREENSHOTS / "login-reduced-motion.png"), full_page=True)
        page.emulate_media(reduced_motion="no-preference")
        expect(page.locator("body")).to_have_attribute("data-motion", "playing")
        # Simulated document lifecycle, not a WAN/infrastructure acceptance claim.
        page.evaluate(
            "Object.defineProperty(document,'hidden',{get:()=>true,configurable:true});"
            "document.dispatchEvent(new Event('visibilitychange'))"
        )
        expect(page.locator("body")).to_have_attribute("data-motion-reason", "hidden")
        _settle(page)
        hidden = _scene_state(page)
        page.wait_for_timeout(250)
        assert _scene_state(page) == hidden
        assert page.evaluate("localStorage.getItem('nextops-motion')") == "playing"
        page.evaluate(
            "Object.defineProperty(document,'hidden',{get:()=>false,configurable:true});"
            "document.dispatchEvent(new Event('visibilitychange'))"
        )
        expect(page.locator("body")).to_have_attribute("data-motion", "playing")
        page.locator("#username").fill("owner")
        page.locator("#password").fill("test-password")
        page.locator('#loginForm button[type="submit"]').click()
        expect(page.locator("#workspaceView")).to_be_visible()
        _profile_action(page, "#logoutButton")
        expect(page.locator("#loginView")).to_be_visible()
        expect(page.locator("body")).to_have_attribute("data-motion", "playing")
        assert page.locator("#password").input_value() == ""
        context.close()
        browser.close()


@pytest.mark.parametrize("theme", ["light", "dark"])
def test_static_mobile_login_without_preference_storage(motion_server: str, theme: str) -> None:
    with sync_playwright() as playwright:
        browser = _browser(playwright)
        context = browser.new_context(
            viewport={"width": 390, "height": 844}, reduced_motion="reduce"
        )
        context.add_init_script(
            "Object.defineProperty(window,'localStorage',{get(){"
            "throw new DOMException('blocked','SecurityError')}});"
        )
        page = context.new_page()
        errors: list[str] = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto(motion_server, wait_until="networkidle")
        page.evaluate("theme=>document.documentElement.dataset.theme=theme", theme)
        expect(page.locator(".gate-scene")).to_be_visible()
        expect(page.locator("#loginTitle")).to_be_visible()
        expect(page.locator("#motionButton")).to_be_disabled()
        page.locator("#password").fill("pasted fixture password")
        page.locator("#passwordVisibility").click()
        expect(page.locator("#password")).to_have_attribute("type", "text")
        page.locator("#passwordVisibility").click()
        expect(page.locator("#password")).to_have_attribute("type", "password")
        page.locator("#username").fill("owner")
        page.locator('#loginForm button[type="submit"]').scroll_into_view_if_needed()
        assert page.locator('#loginForm button[type="submit"]').evaluate(
            "e=>{const r=e.getBoundingClientRect();return e.contains("
            "document.elementFromPoint(r.x+r.width/2,r.y+r.height/2))}"
        )
        assert page.evaluate("document.documentElement.scrollWidth<=innerWidth")
        assert not errors
        context.close()
        browser.close()
