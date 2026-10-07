"""Static company login and responsive checks; sanitized loopback fixtures only."""

from __future__ import annotations

import socket
import threading
import time
from collections.abc import Iterator
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
from urllib.request import urlopen

import pytest
import uvicorn
from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import expect, sync_playwright

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
def test_logo_led_static_login_under_strict_csp(
    motion_server: str, locale: str, width: int, height: int
) -> None:
    with sync_playwright() as p:
        browser = _browser(p)
        context = browser.new_context(viewport={"width": width, "height": height})
        context.add_init_script(
            f"localStorage.setItem('nextops-language','{locale}');"
            "localStorage.setItem('nextops-theme','dark')"
        )
        external: list[str] = []
        errors: list[str] = []

        def local_only(route: Any) -> None:
            if urlparse(route.request.url).hostname == "127.0.0.1":
                route.continue_()
            else:
                external.append(route.request.url)
                route.abort()

        context.route("**/*", local_only)
        page = context.new_page()
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        response = page.goto(motion_server, wait_until="networkidle")
        assert (
            response is not None
            and "style-src 'self'" in response.headers["content-security-policy"]
        )
        expect(page.locator(".ocs-logo-hero")).to_be_visible()
        expect(page.locator(".signal,.gate-scene,#motionButton")).to_have_count(0)
        assert page.locator("#loginView").evaluate("e=>e.getAnimations({subtree:true}).length") == 0
        assert page.evaluate("document.documentElement.scrollWidth<=innerWidth")
        assert page.locator("html").get_attribute("dir") == ("rtl" if locale == "fa" else "ltr")
        SCREENSHOTS.mkdir(parents=True, exist_ok=True)
        page.screenshot(path=str(SCREENSHOTS / f"logo-login-{locale}-{width}.png"), full_page=True)
        page.locator("#username").fill("owner")
        page.locator("#password").fill("test-password")
        page.locator("#loginForm button[type=submit]").click()
        expect(page.locator("#workspaceView")).to_be_visible()
        _profile_action(page, "#logoutButton")
        expect(page.locator("#loginView")).to_be_visible()
        expect(page.locator("#password")).to_have_value("")
        assert not errors and not external
        context.close()
        browser.close()


def test_old_motion_preference_cannot_hide_logo_or_form(motion_server: str) -> None:
    with sync_playwright() as p:
        browser = _browser(p)
        context = browser.new_context(reduced_motion="reduce")
        context.add_init_script("localStorage.setItem('nextops-motion','paused')")
        page = context.new_page()
        page.goto(motion_server)
        expect(page.locator(".ocs-logo-hero")).to_be_visible()
        expect(page.locator("#loginTitle")).to_be_visible()
        assert page.locator("#loginView").evaluate("e=>e.getAnimations({subtree:true}).length") == 0
        page.emulate_media(reduced_motion="no-preference")
        page.reload()
        expect(page.locator("#username")).to_be_visible()
        assert page.locator("#loginView").evaluate("e=>e.getAnimations({subtree:true}).length") == 0
        context.close()
        browser.close()


@pytest.mark.parametrize("theme", ["light", "dark"])
def test_static_mobile_login_without_preference_storage(motion_server: str, theme: str) -> None:
    with sync_playwright() as p:
        browser = _browser(p)
        context = browser.new_context(
            viewport={"width": 390, "height": 844}, reduced_motion="reduce"
        )
        context.add_init_script(
            "Object.defineProperty(window,'localStorage',{get(){"
            "throw new DOMException('blocked','SecurityError')}})"
        )
        page = context.new_page()
        errors: list[str] = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(motion_server)
        page.evaluate("theme=>document.documentElement.dataset.theme=theme", theme)
        expect(page.locator(".ocs-logo-hero")).to_be_visible()
        page.locator("#password").fill("pasted fixture password")
        page.locator("#passwordVisibility").click()
        expect(page.locator("#password")).to_have_attribute("type", "text")
        page.locator("#passwordVisibility").click()
        expect(page.locator("#password")).to_have_attribute("type", "password")
        page.locator("#loginForm button[type=submit]").scroll_into_view_if_needed()
        assert page.locator("#loginForm button[type=submit]").evaluate(
            "e=>{const r=e.getBoundingClientRect();"
            "return e.contains(document.elementFromPoint(r.x+r.width/2,r.y+r.height/2))}"
        )
        assert page.evaluate("document.documentElement.scrollWidth<=innerWidth")
        assert not errors
        context.close()
        browser.close()
