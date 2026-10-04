"""Static security checks for the user-panel reverse proxy profile."""

import re
from pathlib import Path

ROOT = Path(__file__).parents[2]
PROFILE = ROOT / "deploy" / "nginx" / "nextops-app.conf"


def test_app_proxy_requires_tls_and_only_targets_loopback() -> None:
    profile = PROFILE.read_text(encoding="utf-8")

    assert "listen 443 ssl" in profile
    assert "ssl_protocols TLSv1.2 TLSv1.3" in profile
    assert "proxy_pass http://127.0.0.1:8000" in profile
    assert "client_max_body_size 16k" in profile
    assert "Strict-Transport-Security" in profile
    assert "limit_req zone=nextops_login" in profile
    assert "limit_req zone=nextops_assistant" in profile
    assert "assistant/generate|investigate|monitoring/investigate|incidents/investigate" in profile
    assert "api/v1/(bootstrap|recovery)" in profile
    assert "docs|redoc|openapi" in profile
    assert "192.168." not in profile


def test_saved_generation_inherits_existing_bounded_inference_proxy_policy() -> None:
    profile = PROFILE.read_text(encoding="utf-8")
    matched = re.search(
        r'location ~ "(\^/api/v1/[^\n]+)" \{(.+?)\n    \}',
        profile[profile.index('    location ~ "^/api/v1/(assistant/') :],
        re.DOTALL,
    )
    assert matched is not None
    pattern, body = matched.groups()
    assert re.fullmatch(
        pattern, "/api/v1/conversations/12345678-1234-1234-1234-123456789abc/messages"
    )
    assert re.fullmatch(pattern, "/api/v1/monitoring/investigate")
    for path in (
        "/api/v1/conversations",
        "/api/v1/conversations/config",
        "/api/v1/monitoring/sources",
        "/api/v1/monitoring/investigate/other",
        "/api/v1/conversations/not-a-uuid/messages",
        "/api/v1/conversations/12345678-1234-1234-1234-123456789abc/messages/other",
    ):
        assert not re.fullmatch(pattern, path)
    assert "limit_req zone=nextops_assistant burst=3 nodelay" in body
    assert "proxy_read_timeout 180s" in body
    assert "proxy_send_timeout 180s" in body
    assert "proxy_pass http://127.0.0.1:8000" in body
    assert "proxy_read_timeout 30s" in profile.split("    location / {", 1)[1]
