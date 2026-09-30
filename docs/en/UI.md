# Bilingual operations console and design system

## Live local theme switch — 2026-09-30

The header has a keyboard-accessible light/dark switch on login and workspace screens. Before
first paint it uses the saved local preference or system theme. Only the theme/language preference
is stored locally, never transcripts or credentials; restricted preference storage falls back to
the current tab. Persian labels/RTL, 375-pixel layout and dark text/button contrast are tested.
OCS base gold/teal values and the embedded logo are unchanged. This is live in controlled b5e74f9;
five theme fixtures and the live 375-pixel Persian view passed. Use the header button to switch.

## Live standard saved chat — 2026-09-30

Owner-only local history and resume/new/delete controls are enabled in b5e74f9. Thinking is hidden
and rejected at both APIs after failed final-answer trials. The UI/UX workflow guided keyboard navigation and existing OCS tokens;
brand assets are unchanged. See [conversation operation](CONVERSATIONS.md) for limits and privacy.

## Serving focused incident panel — 2026-09-30

The focused behavior first qualified in 810102f remains in serving b5e74f9/35B. A question naming `nextops-app.service` shows
only that authorized unit's recorded state in the answer and default focused panel. Other
already-authorized observations remain in “Show complete authorized evidence,” opened only by
the user. English/Persian live browser checks, mobile width, exact app rollback and audit/hash
matching passed; see [testing](TESTING.md). The OCS logo/palette are unchanged. This is not
a claim that the model can answer every NOC/SOC question or that full production gates passed.

## Network/service incident focus candidate — 2026-09-30

For an unambiguous network or service investigation, the candidate shows the requested bounded
observations first and keeps unrelated, already-authorized evidence behind “Show complete
authorized evidence.” It does not broaden collection or infer firewall/VPN state. English and
Persian 375-pixel browser fixtures passed. At this earlier checkpoint the serving UI was 862d311;
the current release is recorded above. Logo and palette bytes are unchanged.

[فارسی](../fa/UI.md) · [Index](INDEX.md)

**Status: specification plus a delivered controlled user-testing subset.** Source: master specification sections 3, 7 and 17 plus original sections 3 and 30.

## Earlier page-memory-only NOC/SOC workspace — 2026-09-29

At that earlier controlled 862d311/35B checkpoint: five first/four final fresh browser/API cases,
three audit/hash matches and exact b346c3e source rollback passed. Text-only `bdi` isolates plain UTC
timestamps, IP/CIDR and percentages, preserving original answer/copy bytes; fresh offline package,
RTL/mobile/copy and live provenance checks passed. Original OCS logo/palette bytes and all model,
evidence and resource boundaries remain unchanged. Technical model quality is still partial,
not ChatGPT-equivalence or production acceptance. See [testing](TESTING.md) for exact identities.

The [bounded specification](../requirements/NOC_SOC_WORKSPACE_SPEC.md) adds a conversation thread,
operator starters for servers/services, DNS/network latency, firewalls/VPN and defensive security,
safe text/code presentation, answer/code copying and a compact composer. The locally embedded OCS
logo and the original gold/teal/semantic palette are unchanged. No framework, CDN, font or package
dependency is added. Twelve local real-browser fixtures passed, including native RTL/LTR, hostile
HTML remaining inert text, code direction, responsive layouts, copying, expiry and late logout
responses. These are fixture results, not actual model accuracy or deployed-release acceptance.

The following paragraph describes that older release, superseded for enabled general saved chat
by [the current local history contract](CONVERSATIONS.md).

At most twelve completed turns remain in page memory. New conversation, logout or session expiry
clears the transcript; refresh starts afresh. No conversation is saved in localStorage/sessionStorage.
General mode carries at most two recent accepted model-only question/answer pairs, bounded at 2,000
characters per field and 6,000 serialized characters. Oversized turns are omitted with a notice,
not silently clipped. Mode changes clear model context. Live modes do not submit previous turns and
continue fresh, authorized collection; archived evidence keeps its original source/time/audit.

The assistant provides technical advice, not unrestricted NOC/SOC device access. Only the existing
authorized Zabbix/Linux evidence routes are connected. Other vendors/devices receive general
guidance, not invented live status. No command executes from this interface. Broader product
screens, additional connectors and full accuracy/accessibility/production acceptance remain open.
The release manifest identifies the currently serving package. Fixture passes are not model
factuality certificates; additional device connectors still need separate acceptance.

## Existing controlled subset

The controlled subset provides authenticated English/Persian login, genuine RTL/LTR switching,
AI and monitoring readiness and a bounded question form with three explicit answer modes. General
assistant is the default: it answers through the local model without retrieving or displaying live
monitoring evidence. Live monitoring is opt-in: it returns an evidence-grounded answer and a source
panel showing Zabbix version, host, collection time, measurement time, freshness and active-problem
count. Incident investigation adds one deployment-approved target and combines bounded Zabbix
history/events with the direct read-only Linux snapshot. The result badge always identifies whether
live evidence was used. A completed evidence-backed answer also shows its durable run, evidence
reference and audit-event identifiers; the full evidence SHA-256 is available as the
evidence-reference tooltip. Assets are served locally without a CDN.
The broader operations console described below—inventory, incident timelines, topology, approvals,
audit search and settings—remains specification work.

Live investigations are capped server-side at the bounded 384-token CPU budget; the browser uses
the same bound. Completion and quality still require measured qualification. Timeout, overload
and local-dependency failures retain safe machine-readable status
and are presented as distinct actionable messages in both languages. This prevents a stale or
modified browser from raising the output limit beyond the qualified user-testing profile.

A deployed correction dated 2026-09-26 clarifies the result notice: automated source checks do
not prove that an answer is true or relevant. A token-limit completion is treated as incomplete
and displayed through an explicitly limited evidence-only fallback. The app-only release passed
bounded live API and browser checks; the full held-out semantic corpus remains unrun.

The earlier controlled application redesign replaced the dense two-column evaluation workspace with a
single-column question/answer flow. Mode, approved target and language remain explicit; the
submitted question and answer appear together, with source, collection times and scope visible.
The full authorized evidence and audit identifiers are available in a collapsed disclosure rather
than an unsolicited all-data table. Each request is independent; the panel does not send earlier
screen content as conversation history in that earlier release. The new general-only context above
does not change the independence of live requests. A filesystem-capacity question shows only allowlisted mount
observations in the answer. A request for system file names or contents is answered as unavailable:
the read-only collector does not retrieve them. The application labels these focused responses as
deterministic evidence summaries, not verified AI prose. Fresh English/Persian API checks and a
fresh Edge browser pass for this exact app release; they do not establish production readiness.

## Information architecture

For unambiguous CPU-measurement-only monitoring requests, transparent deterministic focus labels
the reviewed CPU-idle percentage, not utilization or health. Source, both timestamps, partial/stale
warnings and the full authorized evidence/audit remain available. Missing or ambiguous readings
are unavailable, not guessed; interpretation/mixed-topic questions retain model synthesis.

Build an operations console, not just a chat page or decorative landing page. Primary areas are overview, asset inventory/details, incidents and evidence timeline, topology, approval requests, connector health, audit search, model/resource health, and settings. Chat is one way to start or inspect a durable investigation.

An investigation view shows affected assets, time window, permission scope, task progress, source-linked evidence, missing/partial data, alternative causes and a concise decision summary. Show tool activity and sanitized outputs, not unrestricted internal reasoning traces. Recommendations and actual execution outcomes must be visually distinct.

## Shared design system

Define semantic tokens for spacing, typography, colors, borders and component states before building many pages. Use reusable navigation, tables, filters, timelines, evidence cards, status badges, dialogs and approval panels. Status meaning must not rely on color alone. Keep labels, keyboard interaction, focus behavior and contrast accessible.

Use responsive layouts with long device names, mixed-language text, overflowing commands and dense operational data in mind. Prefer locally hosted licensed assets; runtime must not depend on font, icon or JavaScript CDNs.

### Current OCS visual identity

The current source redesign uses the company mark supplied through the owner's public OCS profile
reference and the observed OCS gold (`#D0A840`) and teal (`#0090A0`) as brand accents. The exact
logo is embedded locally and also supplies the browser icon; system fonts, CSS artwork and interface
icons are local, so the page issues no runtime request to LinkedIn, a font host or a CDN. The light
enterprise layout keeps semantic success, warning and failure colors separate from the brand.

A development-only [Figma design source](https://www.figma.com/design/fXtpP4xBQg3qovTDcchuHx)
now records the OCS cover, 48 primitive/semantic/dimension variables, 11 bilingual text styles and
two elevation styles. The deployed workspace mirrors its spacing, radii and brand tokens, with
numbered answer-mode cards, a high-contrast evidence boundary, compact service-status pills and a
branded result accent. The current controlled release retains the OCS tokens but replaces the
cards and permanent side panel with compact mode choices and optional evidence guidance. Figma is
not a runtime dependency or an authority for application behavior;
the reviewed source, tests and documentation remain authoritative. Full product-screen composition
inside Figma was not completed because the Starter-plan MCP call quota was reached, so the file
must not be represented as a complete screen library.

The real-browser fixture covers the branded login, authenticated workspace, composite incident
evidence, English LTR, Persian RTL, reduced motion and 375-pixel mobile width without horizontal
overflow or external requests. The visual foundation was first promoted as immutable application
release `nextops-0.1.0-54c8bb4`; release `nextops-0.1.0-cdde129` preserved it and server-side
session termination and explicit localized integrity notices for unverified model-only answers,
evidence-bounded answers, deterministic fallbacks and monitoring-scope redirects. A fresh
authenticated Phase 2 browser workflow passed English/Persian incident evidence, normal TLS, WAN
denial, mobile RTL, audited logout and new-tab isolation without an external page request. The
2026-09-26 live API qualification also passed all four answer-integrity modes. The current app
release `nextops-0.1.0-01755d1` adds the focused, collapsed-detail workspace and passed fresh
greeting, file-boundary, evidence/audit, RTL/mobile and browser-WAN checks. This did not rerun
the full semantic corpus or the earlier VM-reboot campaign.

## Persian and English behavior

Persian uses a genuine RTL layout with natural wording; English uses LTR. Isolate code, IP addresses, interface names, timestamps and identifiers so bidirectional rendering cannot alter perceived technical meaning. Keep command bytes and raw diagnostic strings unchanged except explicit secret redaction. Do not localize protocol field values or store translated labels as business keys.

Use [the glossary](GLOSSARY.md) for consistency. Review Persian with realistic incident narratives, not merely automated detection of Persian characters. Language switches must preserve the same record, permissions, evidence and workflow state. The application stores UTC and lets the deployment choose display timezone.

## Required states

Explicitly represent loading, empty, stale, partial, offline, overloaded, access denied, awaiting approval and unknown outcome. Model unavailability must not block manual incident/evidence access. Read-only mode versus mutation-enabled mode must be obvious. Display connector capability status accurately: planned, simulated, lab-verified or production-validated.

## Approval interface

Present the exact target, named action, arguments or change diff, requester, policy/risk, expected pre-state, impact, freshness, approver requirement and expiry. A generic Approve button is insufficient. Changed details invalidate the old approval. Never display credential contents; the screen refers to the approval record, not an executable secret.

For a timed-out mutation, show that the outcome is unknown and requires reconciliation. Do not present a green success indicator or offer blind retry. Distinguish requested cancellation from verified remote cancellation.

## Acceptance

Browser tests cover both directions, keyboard navigation, mixed text, long commands, permission boundaries, approval expiry/changes, reconnecting progress, partial evidence and offline assets. Domain and language reviewers verify that wording does not overstate certainty or imply an unexecuted action succeeded.
