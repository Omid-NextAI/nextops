"""Loopback-only, visibly labelled design fixture. Never imported by the application."""

from __future__ import annotations

from typing import Any

from fastapi import FastAPI, Request
from fastapi.responses import Response

from .test_phase2_panel import STATIC, _fixture_app


def create_preview() -> FastAPI:
    app = _fixture_app()
    app.state.saved_chats_enabled = True

    @app.middleware("http")
    async def design_fixture(request: Request, call_next: Any) -> Response:
        if request.url.path == "/":
            source = (STATIC / "index.html").read_text(encoding="utf-8")
            source = source.replace(
                '<body data-authenticated="false">',
                '<body data-authenticated="false">'
                '<div class="demo-notice" role="note">Demo data — not live</div>',
            )
            response = Response(source, media_type="text/html")
        else:
            response = await call_next(request)
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; base-uri 'none'; frame-ancestors 'none'; "
            "form-action 'self'; object-src 'none'; script-src 'self'; style-src 'self'; "
            "img-src 'self' data:"
        )
        return response

    return app
