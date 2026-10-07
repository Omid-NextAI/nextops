# NextOps project status brief

[فارسی](../fa/PROJECT_STATUS_BRIEF.md) · [Documentation index](INDEX.md) · [Project state](../PROJECT_STATE.md) · [Next task](../NEXT_TASK.md)

Updated: 2026-10-07

## Current executive summary: retained audit-repair release

As recorded on 2026-10-07, exact `52e5179` is selected for app, AI API and canonical MCP/source
runner, with the matching existing collector on all four guests. The
[release manifest](../status/current-release.yaml) and
[all-role qualification](../requirements/AUDIT_REPAIR_LIVE_QUALIFICATION_2026-10-07.md) are
authoritative. This is live controlled user testing, not full production acceptance.

| Area | Current design and measured status |
|---|---|
| User workspace | Static local EN/FA HTML/CSS/JavaScript, original OCS images, static logo login, compact chat and evidence on demand |
| Identity and memory | Existing local authentication, current-user policy, owner-scoped PostgreSQL conversations, bounded follow-ups/resume and sensitive-view cleanup |
| Inference | Unchanged Qwen3.8-27B Q8 CPU runtime; 32 workers, one slot, 16K configured context, six saved turns, thinking off, one active/two queued |
| Monitoring | Real MCP gateway and isolated credential-owning runner on the existing connector VM; protected two-source/seven-target catalog, with three secondary targets qualified for bounded reads |
| Evidence/security | Source/time/scope, deterministic counts/coverage, secret-text redaction, physical-call admission ownership and late authorization/mandatory audit fixes |
| Deployment | Four existing role guests on one ESXi/G10; separate NextOps/Zabbix PostgreSQL; native systemd, private TLS, restricted tunnels and immutable artifacts |
| Latest verified checks | Five exact-source CI jobs: 1509 unit/API, 119 browser, 60 PostgreSQL 16 and 60 PostgreSQL 17 tests, plus secret scan; actual EN/FA primary/secondary, saved resume, durable audit/hash and exact all-role rollback/reapply |
| Remaining limits | Raw model 13/16 remains failed; thinking/privacy/full-window, current-source server-WAN, VM cold-start and sustained load remain unqualified; GOV-01 needs repository administration |

Existing queue/provider/app/proxy budgets remain 5/300/330/360 seconds. Configured context is not
full-window quality acceptance. Earlier raw-model exceptions do not waive authentication, audit,
privacy, resource bounds or offline safeguards. Recognized-secret redaction is defense in depth,
not a guarantee for arbitrary secret formats.

The old HTTP connector is disabled, not a fallback. Approved-source listing is not automatic
discovery or proof of monitoring-engine health; fresh reads and their exact scope matter.
Local user-management source remains implemented but unaccepted, not a newly qualified
administration feature. No broad retrieval, topology, general worker or remediation system is
claimed. Independent recovery remains owner-deferred; snapshots do not establish independent
PostgreSQL/WAL/PITR or host-loss recovery.

Current design is documented in [Architecture](ARCHITECTURE.md), [Diagrams](DIAGRAMS.md),
[Technology stack](TECH_STACK.md), [MCP](MCP.md) and [UI](UI.md).
[Next task](../NEXT_TASK.md) retains the unfinished held-out factual/reliability strategy.
This documentation update does not operate or redeploy any server.

## Historical status snapshots: preserved, not current acceptance

Everything below retains earlier presentation/qualification records. Versions, counts, readiness
statements and “current” wording inside these dated snapshots apply only to their original
checkpoint; they do not override the current summary or manifest above. Earlier WAN, reboot,
load, restore and model results must not be transferred to `52e5179`.

Current controlled workspace: app `48e3a8a` is retained with the original OCS images, static login
and simpler chat. AI API `ec1ed32`, Qwen3.8-27B Q8/CPU and MCP are unchanged. Exact-source CI,
offline installation, real saved-chat/secondary-Zabbix browser, durable audit and app rollback
passed. A model timeout remains recorded; thinking/full-context/raw quality/current WAN/VM/load
are not accepted. [The live record](../requirements/OCS_UI_LIVE_QUALIFICATION_2026-10-07.md) and
current manifest are authoritative; this is not full production acceptance.

Earlier 2026-10-04 controlled workspace: matched app/AI `7ce9d29` adds narrow diagnostic safeguards while
retaining 35B/CPU, saved standard chat, themes and OCS branding. Five-job CI, 524 local checks,
three fresh offline installs, 45 functional cases, 36 text-free audits/nine live hashes, bounded
queue recovery, exact69 rollback and final re-promotion passed. All four guests denied external
WAN/proxy traffic during fresh login, EN/FA generation and LAN evidence retrieval; native model,
AI API and application restart also passed. Final UI/reload checks preserve the visible fallback
notice. Four rejected candidates and broader PR51 failures remain recorded. Scoped app-owned
answers do not certify raw-model accuracy. Thinking stays disabled; full-context quality/latency
remain failed, broad semantics partial and this source's VM cold-start/sustained-load gates unrun.
Earlier b5e74f9 reboot evidence is separately dated. Independent recovery remains owner-deferred,
not passed. [Testing](TESTING.md) and the [release manifest](../status/current-release.yaml) are
authoritative; live controlled use is not full production acceptance.

Earlier 2026-09-30 checkpoint: app/API 810102f retains 35B/CPU, the exact OCS palette/logo and
canonical evidence boundaries. Five CI jobs, fresh offline install, six live EN/FA browser cases,
six audit/hash matches and exact 862d311 rollback with fresh restored answers passed. Named-service
answers and the focused panel now exclude unrelated units. The 49.5–93.0s first-run samples are
not load percentiles. General technical semantics, server-WAN/VM cold-start and independent
recovery remain open; no new connector, training or full production acceptance. The release
manifest is authoritative; the following 95c6e50 qualification is historical evidence.

Previous controlled selection: app/API `95c6e50` served Qwen3.5-35B-A3B Q4_K_M on the existing
CPU-only guest/runtime. Twelve API and twelve browser cases, eight durable audit/hash pairs,
exact 8B/app/API rollback and six final re-promotion confirmations passed. Sample latency was
12.7–94.3s; hardware/queues/deadlines did not change. Full held-out quality is partial, not
production accepted. Preserve the first 35B semantic failure and rejected 14B/32B/30B findings.
The retired owner form remains retired. Earlier clarity regressions and checks are recorded in
the testing guide; larger weights do not guarantee universally correct answers.

Owner clarification: an ESXi VM snapshot restore was tested by the owner; its dated result was
not reviewed here. This does not qualify independent PostgreSQL backup, WAL/PITR or isolated
restore. Non-recovery work remains the active delivery sequence.

Current scope note: the owner reports daily ESXi snapshots and has deferred independent recovery
from this local delivery. The owner's snapshot-restore result has not been independently reviewed;
protection against loss of the serving host or storage is unproven. Recovery work is no longer the first active checkpoint, but its acceptance
gates remain unpassed and full production acceptance is not claimed. The next work is the serving
app's held-out bilingual answer review and other non-recovery release/security gates.

### Executive position

NextOps has reached a controlled user-testing checkpoint. The first complete read-only path is live
across the four Ubuntu 24.04 servers: a user signs in through the private TLS application panel,
selects one of four approved targets, receives bounded Zabbix history/events plus a direct
read-only Linux snapshot through the restricted connector, and obtains an explanation generated by
the local CPU-only model in English or Persian.

The deployed slice is suitable for supervised user testing, not production acceptance. It covers
four approved hosts, a five-method Zabbix reader and four forced-command Linux identities with
distinct keys. Phase 2 source CI, live bilingual API investigations, durable evidence/audit linkage,
service restart, rollback, guarded WAN denial, authenticated live browser, serial VM reboot and
dependency loss/recovery pass. Certificate-expiry detection and the local Zabbix problem/recovery
path also pass on both TLS frontends. Independent off-datastore backup, WAL/PITR, certificate
rotation/operator notification and disaster-recovery sign-off remain open. The owner subsequently
deferred independent recovery; no independent destination or isolated restore lab exists and no
recovery acceptance is implied. No SMTP or alternate named-recipient delivery route is configured.

The earlier application and AI API were `nextops-0.1.0-95c6e50`; connector remains on
`nextops-0.1.0-cdde129`. The clarity update preserves full questions, separates general and evidence
instructions, and bounds answers at 384 tokens. Selected CPU model is Qwen3.5-35B-A3B Q4_K_M.
Twelve API/browser cases each, eight audit/hash pairs, exact 8B/source rollback and six final
re-promotion confirmations passed; full held-out quality was partial and that historical release's
server WAN isolation and VM cold start had not run. The current release retains the rejection of credential-bearing HTTP redirects;
all four guests require key-only, non-root SSH and the
AI host firewall is active. Zabbix Agent 2 is aligned at `7.0.31` on all four guests. The owner confirmed that recovery/restore resources, an approved
project license, a named-recipient notification channel, replacement CA certificates and named
approvers are unavailable. The tested offline capability does not imply permanent host egress
denial: current administrator shells can reach public IPv4, although app/AI/model units deny
non-loopback IP traffic. The connector process is limited to its reviewed LAN; persistent
host-wide egress and an approved SSH management allowlist remain partial.

Earlier application release `nextops-0.1.0-2397581` and AI application release
`nextops-0.1.0-fd3c353` added deterministic answer-integrity enforcement. Model-only answers are
explicitly unverified; current infrastructure state requires live evidence; evidence answers retain
provenance, freshness and limitations; unsupported live claims fail closed to a bounded fallback.

### Status at a glance

Recovery entries in the table retain the full-production evidence contract; they are deferred
from the present local-delivery work queue, not passed or deleted.

| Workstream | Current status | Verified result | Remaining acceptance |
|---|---|---|---|
| Architecture and governance | Accepted baseline | Four-server, CPU-only, local-inference and read-only-first boundaries remain enforced | Complete operation-specific audit and the remaining recovery gates |
| Application and database | Live for controlled testing | Immutable application release, PostgreSQL 16, local identity, private TLS, bilingual panel, rollback and socket-only logical restore passed | Establish independent backup, WAL/PITR and production observability |
| Local CPU inference | Live and integrated | Pinned llama.cpp/Qwen, authenticated generation, eight-case bilingual integrity evaluation, cold restart, artifact rollback, cancellation/dependency recovery and five-minute bounded load passed in earlier controlled qualification | Approve production SLOs and complete independent recovery |
| Zabbix | Live with restricted scope | Zabbix 7.0.31 and Agent 2 7.0.31 on all four guests, separate PostgreSQL, restricted reader, socket-only logical restore and certificate lifecycle triggers passed | Complete retention, independent backup, WAL/PITR and operator notification delivery |
| Read-only connector | Live and least-privilege | Rootless loopback service, protected Zabbix credential, strict TLS, four distinct forced-command Linux keys and bounded composite evidence; denial, restart, rollback, guarded WAN and dependency-recovery cases passed | Complete production monitoring and independent recovery sign-off |
| End-to-end user path | Controlled user testing | Current-source fresh EN/FA answers, saved UI reloads, evidence/audit hashes, exact rollback and server WAN/process restart passed | Complete broad held-out semantics, current-source VM/full cold start, context/thinking qualification and operational sign-off; independent recovery remains deferred |

### Delivered user-testing capability

- A private HTTPS panel with English left-to-right and Persian right-to-left interfaces.
- Protected local sign-in; no infrastructure credential is exposed to the browser or model.
- A fixed, read-only investigation workflow rather than arbitrary JSON-RPC, URL, command or write
  access.
- Current Zabbix evidence with source version, host, collection time, metric observation time,
  stale-data state and active-problem count.
- A local CPU-generated explanation grounded in the returned evidence, with no cloud inference
  fallback.
- Native systemd deployment with immutable release directories, stable links, root-owned protected
  configuration and credentials, loopback backends, private TLS and host firewalls.
- Separate restricted SSH tunnels from the application server to the AI and connector services.

### Acceptance evidence

- Repository checks passed: Ruff formatting and lint, strict mypy, documentation, deployment,
  inference and release-status validators, 160 unit/API tests, PostgreSQL 16 and 17 CI,
  real-browser fixture acceptance and secret scanning.
- Connector verification returned bounded Zabbix and direct Linux evidence for each of four fixed
  targets; generic shell, unauthenticated and unknown-target requests were denied.
- Authenticated Phase 2 application API checks passed composite evidence and grounded local
  generation in both languages, with durable run/evidence/audit identifiers.
- A fresh Phase 2 Edge context behind a WAN-deny proxy passed the authenticated HTTPS workflow,
  English LTR, Persian RTL, composite incident evidence, provenance, audited sign-out and new-tab
  isolation with no external page requests.
- The local certificate checker passed on both frontends with hardened timers and key denial. A
  guarded timer outage produced the expected Zabbix problem and recovery returned all triggers to
  healthy; operator notification delivery and live-pair rotation were not run.
- Application/runtime/model rollback, cancellation, dependency/artifact recovery, isolated
  low-space behavior and a five-minute two-client load passed; detailed measurements are in the
  [Stage 1 report](STAGE_1_COMPLETION_REPORT.md).
- Both database dumps restored into temporary socket-only PostgreSQL 16.15 clusters and were
  verified and cleaned up. This is logical restore evidence, not independent disaster recovery.
- A prior serial reboot returned all four servers on kernel `6.8.0-142` with healthy systemd state.
  The later rollback-protected maintenance applied the pending packages and Zabbix `7.0.31`;
  current checks show zero failed units, pending packages or reboot markers on all four guests.

### Security posture

The current slice deliberately limits authority. Zabbix credentials exist only on the connector;
the connector API is loopback-only; its API role permits exactly `host.get`, `item.get`,
`problem.get`, `history.get` and `event.get` for one approved host group; and non-allowlisted reads
and writes were verified as denied. Each Linux target uses a distinct connector-held key, a pinned
host identity and one forced command. The model receives normalized evidence, not infrastructure
credentials, and has no change or approval capability. Only SSH and the intended private HTTPS
endpoint are allowed by the relevant host firewalls.

### Remaining non-recovery work and deferred risk

The owner confirmed that the following inputs do not yet exist. Item 1 is deferred from this local
delivery; items 2–4 and the current-release qualification gates remain active:

1. An independent recovery destination and isolated restore lab for PostgreSQL-aware backup,
   WAL/PITR, file recovery, key recovery and measured RPO/RTO acceptance.
2. A company-approved NextOps license, offline signing trust root and named legal/security/
   production approvers for supply-chain and release acceptance.
3. A LAN-local notification channel with primary and backup recipients, plus replacement CA-issued
   application/Zabbix certificate pairs and protected handoff for a live rotation/rollback drill.
4. An approved DNS/time/maintenance-proxy and management-network allowlist for persistent
   host-wide outbound and SSH-ingress policy. The connector process already has a qualified LAN
   allowlist; historical whole-guest WAN denial was a temporary test.

Further production hosts and connector methods require separate scope review; they are not needed
to resolve these four present blockers.

### Presentation conclusion

NextOps now has a functioning, security-bounded product slice rather than only prepared
infrastructure. It is ready for supervised user testing of the bilingual, read-only investigation
experience with explicit integrity labeling and fail-closed evidence behavior. It is not production
accepted: independent restore, certificate, notification, license/security and final approval
gates above remain open.
