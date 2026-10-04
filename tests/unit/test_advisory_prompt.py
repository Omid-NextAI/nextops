"""Policy regression checks do not certify generated answers or authorize operations."""

from typing import Literal

import pytest

from nextops.inference.advisory_prompt import ADVISORY_POLICY_REVISION, general_system_prompt


@pytest.mark.parametrize("locale", ["en", "fa"])
@pytest.mark.parametrize("detailed", [False, True])
def test_shared_policy_has_task_adaptive_and_calibrated_guidance(
    locale: Literal["en", "fa"], detailed: bool
) -> None:
    prompt = general_system_prompt(locale, detailed=detailed)
    assert ADVISORY_POLICY_REVISION in prompt
    assert len(prompt) < 4_000
    assert "use digits, not number words" in prompt
    assert "smallest complete example" in prompt
    assert "Never solicit passwords" in prompt
    assert "does not establish a completed TCP connection" in prompt
    assert "TCP can recover packet loss" in prompt
    assert "Do not advise unrequested public exposure" in prompt
    assert "An old observation is not current status" in prompt
    assert "Missing log entries do not prove" in prompt
    assert "only the specified input grammar" in prompt
    assert "exact requested test count" in prompt
    assert "not abandoned drafts" in prompt
    assert "Never expand an answer into a full procedure" not in prompt
    assert ("smaller legacy response budget" in prompt) is not detailed
    assert ("Use saved conversation only" in prompt) is detailed
