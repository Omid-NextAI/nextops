# Reference workspace and OCS login — source and controlled live handoff

## Latest owner redesign: source only, 2026-10-07

The company-logo/static-login and compact chat candidate supersedes the old Signal Gate and
violet composition described below. Both supplied JPEGs are unchanged, selected for light/dark
themes. The login takes the supplied video's split glass card and angular background, without
unsupported sign-up/reset controls. No model, prompt, API policy, schema or live service changed.
See [bounded requirements](../requirements/OCS_UI_SIMPLIFICATION_2026-10-07.md).

From the reviewed worktree, using already-provisioned Python/browser dependencies:

```powershell
.venv/Scripts/python.exe -B -X utf8 -m uvicorn tests.browser.ui_preview:create_preview --factory --host 127.0.0.1 --port 8879 --log-level error
```

Open `http://127.0.0.1:8879/`; isolated fixture credentials are `owner` / `test-password`, never
production credentials. The visible “Demo data — not live” label cannot be enabled in production.
Use a different free loopback port if needed; do not stop unrelated previews.

```powershell
.venv/Scripts/python.exe -B -X utf8 -m pytest -m "not integration and not browser" -q --tb=short
.venv/Scripts/python.exe -B -X utf8 -m pytest tests/browser -q --tb=short
.venv/Scripts/python.exe -B -X utf8 scripts/check_docs.py
.venv/Scripts/python.exe -B -X utf8 scripts/check_release_status.py
.venv/Scripts/python.exe -B -X utf8 -m tests.browser.capture_reference_ui --base-url http://127.0.0.1:8879 --output artifacts/ocs-redesign/pass-2 --theme dark
.venv/Scripts/python.exe -B -X utf8 -m tests.browser.capture_reference_ui --base-url http://127.0.0.1:8879 --output artifacts/ocs-redesign/light --theme light
```

Observed final results: **1446 unit/API tests passed, two existing POSIX-only skips** (30.15s);
**101 browser tests passed** (326.13s), including seven new redesign cases. Ruff check/format,
Linux-target typing (152 files), JavaScript syntax, diff whitespace and documentation/status/
inference/dossier validators passed. Documentation inventory:143 Markdown files/39 EN/FA pairs.
The existing AnyIO deprecation warning remains; no dependency was changed to hide it.
PostgreSQL integration, live infrastructure, human assistive-technology review and new CI were not
run in this source-only change. The zoom test uses a 200%-equivalent CSS viewport, not browser chrome.

An offline local wheel was built with the already-installed backend:

```powershell
.venv/Scripts/python.exe -B -X utf8 -c "from setuptools.build_meta import build_wheel; print(build_wheel('artifacts/ocs-redesign/wheel'))"
.venv/Scripts/python.exe -B -X utf8 -m ruff check packages migrations tests scripts deploy/installers
.venv/Scripts/python.exe -B -X utf8 -m ruff format --check packages migrations tests scripts deploy/installers
.venv/Scripts/python.exe -B -X utf8 -m mypy --platform linux packages tests scripts deploy/installers
.venv/Scripts/python.exe -B -X utf8 scripts/check_inference_artifacts.py
.venv/Scripts/python.exe -B -X utf8 scripts/check_deployment_dossiers.py
Get-ChildItem packages/nextops/api/static/*.js | ForEach-Object { node --check $_.FullName }
git diff --check
```

The wheel contains all12 static assets, both logo hashes match, and test preview files are absent.
Wheel SHA-256:`bc11414ec968eddea0048baba774b58ee1446f75fd5feb8a887761a178df5554`.
`pip wheel` was unavailable because this venv has no pip; no installer/network download was added.
Gitleaks scans of static assets, the new specification and new browser tests passed. A wider
requirements-directory scan retained one finding in the untouched v2 archive (line463), not
the new files; no archive edit or broad suppression was introduced.

Screenshots include `login-en-1672.png`,
`workspace-empty-en-1672.png`, `dashboard-en-1672.png`, `evidence-en-1672.png`, corresponding
Persian/mobile views and `login-reduced-motion.png`. Capture checks block non-loopback destinations
while preserving the fixture API, use fresh contexts/fixed times, and report errors/overflow.
Before/first-pass/refined screenshots were actually inspected. This is local fixture coverage,
not live integration, server-WAN, VM restart, model accuracy or complete WCAG certification.

Intended deviations: company palette instead of violet; static original logo instead of gate;
compact chat instead of always-open empty KPIs/inspector/findings; unsupported attachment removed;
truthful model/source/status metadata preserved. System fonts remain locally available; no remote
font, new frontend framework or dependency was added. Live promotion requires its own change window.

### Changed files in this source task

Presentation: `packages/nextops/api/static/index.html`, `app.css`, `workspace.css`, `login.css`,
`app.js`, `investigation-view.js`, `capabilities.js`, `theme.js`, `login-motion.js`,
`ocs-logo-dark.jpg`, `ocs-logo-light.jpg`. The legacy motion module now only handles password
visibility; no motion remains. Evidence CSS, inference, policy, schema, lockfiles and deployed pins
are unchanged.

Verification: `tests/api/test_app.py`, `tests/browser/test_phase2_panel.py`,
`test_reference_ui.py`, `test_panel_quality_regression.py`, `test_login_motion_regression.py`,
`test_ocs_redesign.py`, `capture_reference_ui.py`, `ui_preview.py`.

Documentation: paired `docs/en/UI.md`/`docs/fa/UI.md` and `REFERENCE_UI.md`,
`docs/requirements/OCS_UI_SIMPLIFICATION_2026-10-07.md`, `docs/PROJECT_STATE.md`,
`docs/NEXT_TASK.md`, `docs/MARKDOWN_CONTEXT_INDEX.md`, `CHANGELOG.md`; `.gitignore` excludes
generated redesign artifacts. Final dark/light captures are additionally in
`artifacts/ocs-redesign/final-dark/` and `final-light/`, with `capture-checks.json`.

[فارسی](../fa/REFERENCE_UI.md) · [Specification](../requirements/REFERENCE_UI_SPEC.md) · [UI history](UI.md)

## Scope and implementation

The 7 October follow-up adds enabled-model metadata, visible approved source/host selection and
problem/metric filters without changing OCS branding, login motion or the underlying reference
layout. Its [qualification record](../requirements/UI_QWEN38_SOURCE_QUALIFICATION_2026-10-07.md)
and the current release manifest supersede historical component identities below.

Branch: `codex/reference-dashboard`, inspected main baseline `625ca80`, 2026-10-04.
The owner subsequently authorized deployment: repaired app `3d92b71` was serving on5 October,
while connector `2a7c8dc` and AI/model were unchanged within that UI change.
The [5 October repair record](../requirements/UI_REPAIR_LIVE_QUALIFICATION_2026-10-05.md)
records the 88-browser/738-non-browser follow-up, exact-source CI, real aging/browser/audit
and `f169875` rollback/reapply, preserving the earlier 70-test repair and `836b1ea` rollback. The [earlier UI record](../requirements/REFERENCE_UI_LIVE_QUALIFICATION_2026-10-05.md)
retains the original 47-test deployment and repaired failures. Model quality, server-WAN/cold-start,
reboot, recovery and production gates are not closed by this visual release.

The native HTML/CSS/JS frontend remains. `app.css` owns shared/OCS tokens; `workspace.css` owns
authenticated violet/blue chrome; `login.css` and `login-motion.js` own the original signal gate.
`investigation-view.js` is a presentation adapter for existing DTOs, not a permission system or
new API. `evidence.css` retains detailed evidence, now theme-aware. The embedded OCS JPEG and base
teal/gold/green values are unchanged. Outline SVGs and the decorative gate are original local code.
Font fallback is Segoe UI/Tahoma/Arial; no remote font, icon CDN or animation framework is used.

The reference is [the supplied image](../design/reference/nextops-investigation.png).
Intentional semantic corrections are listed in the specification. In particular, the UI does not
invent calibrated confidence, estate-wide totals, thresholds, trend deltas, structured causes or
execution timings. Charts require compatible numeric history from the selected observation.
“API reachable” does not establish monitoring-engine health. Model knowledge, absent document
retrieval and fresh infrastructure evidence remain distinct.

## Use and preview

### Evidence aging follow-up — historical controlled `3d92b71`

The selected observation now ages from its original collection time without another request.
One visibility-aware deadline timer stops on close, unmount, hidden page, account view and logout;
reopening recalculates age. Explicit stale status takes precedence, partial labels are not duplicated,
and a single polite contextual announcement reports a visible aging transition. Selection, tab,
focus, raw data and provenance remain unchanged. This is presentation freshness, not a new collection.

The exact final command `.venv/Scripts/python.exe -m pytest tests/browser -q
--junitxml=artifacts/ui-panel-quality/shell-followup/browser-results.xml` passed **88 tests in
280.26s**, including 18 added regressions. Retain the preceding **87/88** fixture-login availability
failure: its transport cause was not reproduced by the bounded four-case diagnostic rerun or the
complete rerun. No retry, longer timeout or authentication bypass was added. The current combined
source passed 738 non-browser/non-integration tests, two POSIX skips, Ruff and Linux-target types
(137 files). Existing PG 16/17 CI evidence belongs to its recorded commit, not this follow-up.

Twenty revised sanitized viewport captures and `shell-report.json` are in
`artifacts/ui-panel-quality/shell-followup/`. EN/FA dark/light at 1672×941 and scroll 0/900 preserve
238px navigation, 64px topbar and a 392px inspector track; zero page overflow, JavaScript errors,
external requests or aging-triggered queries were recorded. Main review inspected EN dark and FA
light captures. Automated status/keyboard checks do not replace human screen-reader review.
Asset versions are `20261005-freshness`. Exact-source CI, offline install, guarded real browser/audit
and `f169875` rollback/reapply passed; both trials verified actual five-minute aging without changing
the browser clock. The app verified in that record was `3d92b71`; its final rollback guard was stopped. See the live
record above for identity/latencies and preserved unrun server-WAN/model gates.

### Motion and panel repair checkpoint — 2026-10-05

The desktop packets already moved in a fresh browser; the reported failure exposed two real
responsive defects: the tablet scene was behind the page, and the phone scene was hidden while
its pause control remained. The scene now occupies a compact normal-flow region on tablet/phone.
Pause/resume no longer replays the entrance or temporarily hides readable content. Visibility,
reduced-motion and authenticated states stop motion; a stored pause preference still takes priority.
The official OCS mark, base colors, CSP, local assets and authentication contract are unchanged.

The phone composer now reserves a full-width 72px typing row with 16px text and a separate 44px
control row. Keyboard navigation restores focus to the actual destination; locale switching retains
the selected observation and retranslates supported destinations without stealing focus. Empty
request details are disabled. Archived observations are labelled as previous-response evidence,
not a fresh collection. Displayed raw JSON remains complete after allowlisted field redaction and
matches Copy. These are presentation repairs, not new monitoring or model capabilities.

The initial assembled checkpoint passed 69 browser tests. After hidden-DOM logout cleanup and
native request-details synchronization, the final suite passed **70 tests in 224.05s**. Ruff,
formatting and strict Linux-target types passed (135 source files). Both dark/light capture passes
cover the five specified viewport sizes and EN/FA, with no page overflow, JavaScript errors, failed
assets or third-party requests. Additional GPU-disabled motion checks measured all nine moving
packets in desktop English/Persian and the light theme. Screenshots are local ignored artifacts in
`artifacts/ui-panel-quality/pass-2-dark/`, `pass-2-light/` and
`artifacts/ui-reference/login-motion-repair/`. Fixture coverage is not full server-WAN acceptance.
The separate guarded `f169875` cutover/real checks are recorded above. The editable [Figma repair board](https://www.figma.com/design/WyrJzqOl3llpnZEondHPCK?node-id=3-2)
documents product tokens and component/motion states; its font substitutes do not change app assets.

After login, open investigation options beside the composer for mode, approved source/target,
answer language and the existing response-mode flag. Enter sends; Shift+Enter adds a line; IME
composition does not submit. Stop waiting preserves the draft and explains that remote work may
continue. Saved conversations remain in navigation; on small screens open its drawer. Administrators
find existing user management in the profile menu. No public signup/reset/social login was added.

Numbered observations select the inspector; its tabs and previous/next controls work by keyboard.
Raw data is an explicit sanitized field projection, selectable LTR text, with copy feedback.
Request details opens the full existing authorized disclosure. It does not fetch new privileges.
Ctrl/Cmd+K searches this page's permitted evidence and saved titles, not devices or a knowledge index.
Unsupported destinations explain their status. Attachments are disabled; no fake success action exists.

Run from the repository root after its existing locked development environment is provisioned:

```powershell
uv sync --locked --extra dev
.venv/Scripts/python.exe -m uvicorn tests.browser.ui_preview:create_preview --factory --host 127.0.0.1 --port 8878
```

Open `http://127.0.0.1:8878`. This separate loopback test server is labelled **Demo data — not live**.
Its disposable fixture login is `owner` / `test-password`; these are not company credentials.
Do not expose this server beyond loopback or use it for live/model qualification. No production
module imports the fixture. A failed live request never selects it.

## Verification record

Commands below used the already provisioned `.venv/Scripts/python.exe` rather than reprovisioning.
See the final check totals below; test fixtures, PostgreSQL lab and live acceptance are separate.

```powershell
$env:PYTHONUTF8='1'
.venv/Scripts/python.exe -m pytest -m "not integration and not browser" -q
.venv/Scripts/python.exe -m pytest -m browser -q
.venv/Scripts/python.exe -m ruff format --check packages migrations tests scripts deploy/installers
.venv/Scripts/python.exe -m ruff check packages migrations tests scripts deploy/installers
.venv/Scripts/python.exe -m mypy --platform linux packages tests scripts deploy/installers
.venv/Scripts/python.exe scripts/check_docs.py
.venv/Scripts/python.exe scripts/check_release_status.py
.venv/Scripts/python.exe scripts/check_deployment_dossiers.py
.venv/Scripts/python.exe scripts/check_inference_artifacts.py
.venv/Scripts/python.exe scripts/check_recovery_profile.py
.venv/Scripts/python.exe scripts/check_server_installers.py
node --check packages/nextops/api/static/app.js
node --check packages/nextops/api/static/investigation-view.js
node --check packages/nextops/api/static/login-motion.js
.venv/Scripts/python.exe -m tests.browser.capture_reference_ui --output artifacts/ui-reference/final
.venv/Scripts/python.exe -m tests.browser.capture_reference_ui --theme light --output artifacts/ui-reference/light
uv build --offline --no-build-isolation --wheel --out-dir artifacts/ui-reference/package
git diff --check
gitleaks git --pre-commit --staged --redact --no-banner
```

Final verification completed 2026-10-05 (Tehran); source inspection/design began 2026-10-04.
Full local regression: **687 passed, two POSIX-specific skips in 167.53s**: 608 unit/API, 38 PostgreSQL
integration and 41 browser tests. The final browser-only rerun passed **41 tests**; collection also
reported the POSIX Linux-collector skip, with 647 non-browser tests deselected. The other full-suite
skip is the POSIX symlink qualification check. One pre-existing Starlette deprecation warning remains.

The integration tests used the existing isolated loopback PostgreSQL **18.6** lab, including actual
saved-chat ownership, session revocation and restricted user administration. They recreate/downgrade
the test schema: **never point them at a company or deployed database**. Existing CI 16/17 strategy is
unchanged; this run is not deployed PostgreSQL 16 acceptance. The full-suite command was:

```powershell
# Only the already provisioned, disposable loopback lab:
$env:NEXTOPS_TEST_DATABASE_URL='postgresql+psycopg://nextops_lab@127.0.0.1:55432/nextops_user_management_test'
.venv/Scripts/python.exe -m pytest -q --tb=short
```

Ruff formatting/lint and Linux-target strict types passed. All three JavaScript syntax checks passed.
The documentation validator passed 134 Markdown files/39 language pairs, including catalog coverage,
local links and RTL wrappers. Release status, deployment dossiers, inference artifacts, recovery-profile
structure and server installers passed their structural validators. The recovery validator still
reports its historical qualification blockers; a valid profile is not a passed restore gate.

Browser checks cover valid login, 401/503/429 distinctions, the show/hide control, session expiry,
sign-out and late
response cleanup; saved-chat reload/resume, request integrity, scoped evidence, owner isolation in the
database tests; EN/FA, themes, motion, drafts/IME, duplicates, failure/cancellation, stale/partial
fields, archived-turn provenance, inspector tabs/copy, keyboard drawers/search and unavailable views.

At 1672px the sidebar/topbar/inspector measure **238/64/392px**. Seven language/viewport combinations
in each of dark and light themes at 1672×941, 1440×900, 1280×800, 768×1024 and 390×844 reported no page overflow,
JavaScript errors or third-party requests. A fresh context blocks non-loopback destinations while
retaining the fixture API. This is browser asset isolation, not real WAN/model/VM acceptance.
Multiple inspection/refinement passes corrected a duplicated initial shell, hidden paused reveal,
overlay interception, focus restoration and archived-evidence association. Screens were visually
reviewed against the reference; no pixel-perfect or complete WCAG certification is claimed.
Keyboard/reflow checks include a 200% zoom-equivalent CSS viewport. Actual browser-chrome zoom and
human assistive-technology sign-off are not recorded by that automated check.

## Screenshots and remaining limits

Generated screenshots and capture checks: `artifacts/ui-reference/final/` (ignored local artifacts).
Selected sanitized copies are in `docs/design/previews/`: desktop workspace/login, Persian RTL
workspace/login, mobile workspace/login and reduced-motion login. All numbers/times are fixtures.

- [English desktop workspace](../design/previews/dashboard-en-1672.png) and [OCS login](../design/previews/login-en-1672.png).
- [Persian desktop workspace](../design/previews/dashboard-fa-1672.png) and [OCS login](../design/previews/login-fa-1672.png).
- [Persian mobile workspace](../design/previews/dashboard-fa-390.png), [login](../design/previews/login-fa-390.png) and [evidence sheet](../design/previews/evidence-fa-390.png).
- [Static reduced-motion login](../design/previews/login-reduced-motion.png).
- [Light desktop workspace](../design/previews/dashboard-light-1440.png) and [light OCS login](../design/previews/login-light-1440.png).

The offline wheel build succeeded without downloads. Its inventory contains all **nine** frontend
assets (HTML, three JS modules plus theme JS, four CSS files) and no test preview/fixture code.
Gitleaks **8.30.1 passed with no leaks** in the staged source change, using redacted output.
No scanner or rule was disabled. An initial generic-key false positive in English coverage prose was
resolved by rewording that sentence, not adding an allowlist.

Current API lacks structured baseline/change, affected-host inventory, cause/next-check fields,
calibrated confidence/thresholds, attachments, share-link, document retrieval and stage-by-stage tool
timings. These remain explicitly unavailable. No backend functionality was added to fill the image.
Existing live checkpoints remain in [NEXT_TASK](../NEXT_TASK.md). Asset packaging uses the existing
`static/*` wheel rule and existing offline installer, with no runtime download or security-policy change.
At the original source-only handoff, rollback meant a reviewed revert/rebuild and no live promotion
had occurred. The later authorized app-only deployment/immutable rollback is recorded above;
wheel/asset verification alone is still not deployment acceptance.

## Deployment preflight repair — 2026-10-05

The owner subsequently authorized deployment followed by a separate Qwen upgrade. PR 56's first
Linux CI run passed quality/security and both PostgreSQL 16/17 jobs, but browser acceptance failed:
the sidebar footer covered saved-conversation deletion. The source repair prevents flex children
from shrinking over their contents and adds short-viewport EN/FA pointer-reachability regression
tests. This initial CI failure is retained, not relabelled as a pass. Fresh exact-head CI and live
qualification were subsequently completed as recorded above; no model change is part of this repair.

The first guarded live trial of `9740868` passed login and the two-source/seven-target catalogue,
but failed Users-to-assistant navigation: the open profile popup obscured Back. Exact rollback
restored `2a7c8dc` with no failed services or schema/config changes. Close the menu on entering
Users, retain focus restoration on return, and test both desktop widths in EN/FA before a new trial.
The failed trial remains recorded separately from subsequent acceptance.

## Changed-file inventory

- Frontend: `packages/nextops/api/static/index.html`, `app.css`, `app.js`, `evidence.css`, new
  `workspace.css`, `login.css`, `investigation-view.js`, `login-motion.js`. Existing `theme.js` is unchanged.
- Regression/preview: `tests/api/test_app.py`, `tests/browser/test_phase2_panel.py`, new
  `tests/browser/__init__.py`, `ui_preview.py`, `test_reference_ui.py`, `capture_reference_ui.py`.
- Documentation: `docs/en/REFERENCE_UI.md`, `docs/fa/REFERENCE_UI.md`, paired `UI.md`,
  `docs/requirements/REFERENCE_UI_SPEC.md`, `TRACEABILITY.md`, `PROJECT_STATE.md`, `NEXT_TASK.md`,
  `MARKDOWN_CONTEXT_INDEX.md`, `CHANGELOG.md`.
- Assets: `docs/design/reference/nextops-investigation.png` and the ten preview images linked above.
- Housekeeping: `.gitignore` excludes generated `artifacts/ui-reference/` output.

The project workflows kept source evidence separate from deployment acceptance and preserved the
unfinished checkpoints. Design/motion guidance favored native semantic controls, a bounded SVG scene,
static reduced-motion composition and no new frontend framework or runtime dependency.

A final accessibility pass strengthened only functional input/dialog boundaries, not the base OCS
palette or panel borders. Browser-computed input contrast is checked in both themes (text at least
4.5:1, boundary at least 3:1). Persian navigation/conversation/tab labels are localized for screen readers.
