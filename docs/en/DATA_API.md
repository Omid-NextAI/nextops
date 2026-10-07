# Data, durable workflows, evidence and API

[فارسی](../fa/DATA_API.md) · [Index](INDEX.md)

**Status: the Stage 1 durable foundation and the complete controlled Phase 2 read-only investigation
API are deployed.**
Source: master specification sections 11, 16–17 and 20. The implemented subset is deliberately
local, single-organization and read-only. General model-only answers remain separate; live Zabbix
investigations now use the existing durable run and append-only audit model.

## Implemented durable subset

Authenticated readiness adds nullable `configured_context_tokens` in source `ec1ed32`. It reports
the configured input-admission ceiling, not a measured full-window quality result. Older providers
may omit it. Deploy the accepting app before the API; roll back API before app because the old app
contract rejects extra fields. This metadata does not authorize thinking or alter inference limits.
See [the bounded UI/source record](../requirements/UI_QWEN38_SOURCE_QUALIFICATION_2026-10-07.md).

Local user administration has a controlled installation recorded in the
[MCP qualification](../requirements/MCP_LIVE_QUALIFICATION_2026-10-04.md); live account mutations
remain unaccepted. `GET /api/v1/users?offset=0`
returns at most 50 same-organization/environment accounts and `next_offset`. `POST /api/v1/users`
accepts `{username,password,role}` with role viewer/operator/engineer. `PATCH
/api/v1/users/{identity_id}` accepts `{is_active,expected_version}`; `POST
/api/v1/users/{identity_id}/password` accepts `{new_password,expected_version}`. Each revalidates
the bearer/current administrator inside its transaction, protects every administrator account and
audits decisions, including schema/JSON/path/query rejections. Malformed input from a valid admin
returns 422 only after denial audit; invalid sessions/non-admins return 401/403 and required audit
failure returns 503. No submitted body or malformed identifier is audited. Status/password changes
revoke all target sessions atomically. No role/scope
editing or deletion exists. Migration 0004 grants only `identities.is_active` UPDATE. Responses
are non-cacheable and secret-free. See [contract](../requirements/USER_MANAGEMENT_SPEC.md).

Controlled saved standard chat is deployed, including migration 0003's owner-scoped tables and
authenticated conversation APIs; thinking remains disabled. Support-read roles have no transcript
grant. See [reference](CONVERSATIONS.md) and ADR 0009; preserve additive tables and audit/version
history for ordinary source rollback. This does not imply acceptance of full-budget context or
current-source VM cold start.

Available in controlled 862d311 (introduced in b346c3e): `POST /api/v1/assistant/generate` accepts optional `history`, a
closed array of at most two `{question, answer}` pairs. Each field is 1–2,000 characters; total
serialized JSON is at most 6,000 characters, including escaping. The current question retains its
4,000-character limit. Context is untrusted/model-only and cannot supply roles, evidence, provider
identity or instructions. Old clients omit it. Monitoring/incident endpoints reject it. This is
nonpersistent request context, not an authenticated durable conversation record or authorization.
No schema migration is needed. See [the bounded packet](../requirements/NOC_SOC_WORKSPACE_SPEC.md)
and the release manifest for deployment status.
The RTL display and single-check health-claim repairs do not change this contract.

Alembic revision `0001_durable_app` creates PostgreSQL tables for organizations,
environments, targets, identities, opaque sessions, runs, worker leases, and audit events.
Database constraints enforce the single-organization starting boundary, scoped foreign
keys, run idempotency, bounded run/locale states, and lease validity. The migration creates
`nextops_migrator`, `nextops_app`, and `nextops_support_ro` group roles; the application
role can append but cannot update/delete audit records, and a trigger also rejects audit
mutation by a table owner. Deployment login roles and secret delivery remain external
deployment work.

Alembic revision `0002_phase2_linux_read` adds only the explicit `linux.read` scope to existing
administrators and removes only that scope on downgrade. It creates no target addresses or
credentials in the application database.

The implemented HTTP surface is:

| Method and path | Authentication | Behavior |
|---|---|---|
| `GET /healthz` | none | Process liveness only; it does not claim dependency readiness |
| `POST /api/v1/bootstrap` | one-time deployment header | Atomically creates the organization, environment, admin, fixture target, audit event, and first session |
| `POST /api/v1/login` | local username/password | Returns an opaque expiring bearer token; only its SHA-256 digest is stored |
| `POST /api/v1/recovery` | protected recovery header | Rotates the admin password/version and revokes every prior session |
| `GET /api/v1/me` | bearer | Returns actor roles/scopes derived from the database session |
| `GET /api/v1/assistant/ready` | bearer | Returns bounded local inference readiness without exposing its service credential |
| `POST /api/v1/assistant/generate` | bearer | Returns a model-only general answer with no monitoring evidence |
| `GET /api/v1/monitoring/summary` | bearer plus server-derived `zabbix.read` scope | Retrieves the current bounded read-only Zabbix summary |
| `GET /api/v1/monitoring/incident-context` | bearer plus server-derived `zabbix.read` scope | Retrieves the configured host's bounded current summary, recent numeric history and trigger events |
| `GET /api/v1/incidents/targets` | bearer plus server-derived `zabbix.read` and `linux.read` scopes | Returns only deployment-owned logical target IDs; never addresses or credentials |
| `POST /api/v1/incidents/investigate` | bearer plus server-derived `zabbix.read` and `linux.read` scopes | Creates a durable target-scoped run, retrieves bounded composite Zabbix/Linux evidence, generates locally, then atomically stores the result, canonical evidence hash and completion audit |
| `POST /api/v1/investigate` | bearer | Creates a durable scoped run, retrieves bounded evidence, generates locally, then atomically stores the result/evidence hash and completion audit |
| `POST /api/v1/runs` | bearer plus `Idempotency-Key` | Authorizes and persists one read-only fixture run, leases it, and returns its explicit fixture result |
| `GET /api/v1/runs/{run_id}` | bearer | Reads only within the actor's server-derived organization/environment scope |

Passwords use Argon2id. Session and lease tokens are opaque, returned once, and stored as
hashes. A reused idempotency key returns the same run only for identical canonical intent;
changed intent returns a conflict. Expired worker leases can be reclaimed after restart.
Required state and audit writes share transactions, so audit/database failure cannot
produce reported success. Errors have stable codes, message keys, retryability, details,
and a correlation ID.

The original fixture result remains explicit, stale and non-live. A live investigation creates its
run before contacting the connector or model. Successful completion stores the bounded
`MonitoringSummary`, its canonical SHA-256 and `run-evidence:<run_id>` reference, the typed local
model result, scope identifiers and the matching completion-audit ID in the run result. The state
change and append-only audit insert share one transaction. Safe failure code, message key and
retryability are stored and audited without raw dependency responses. The API and panel expose the
run/evidence/audit identifiers, and scoped run retrieval returns the same durable result.

`MonitoringSummary` now carries `is_partial` plus bounded, machine-readable `partial_reasons`.
Current reasons distinguish a truncated metric selection, a problem page that reached its result
limit, and absence of usable measurements. The marker and reasons are included in the canonical
evidence hash, durable result and completion audit. Every source-controlled string remains
untrusted content: authentication establishes where the observation came from, not permission for
instructions embedded in a host, metric, value, unit or problem name. Staleness remains a separate
per-measurement flag because a freshly fetched summary can contain old source values.

`MonitoringIncidentContext` is the bounded Zabbix transport contract. It fixes the target to the
connector's configured host, bounds the lookback and list sizes, preserves source timestamps, and
uses explicit partial reasons. `LinuxDiagnosticSnapshot` represents bounded, redacted output from
one immutable forced-command target. `IncidentEvidence` combines the two while preserving target,
collector, collection-time, freshness, partial and failure provenance. The connector exposes only
authenticated internal `/api/v1/linux/{target_id}/snapshot` and
`/api/v1/incidents/{target_id}/evidence` routes; the target ID is resolved through its immutable
registry and cannot supply an address, command, path or SSH option.

The Phase 2 application route persists a target-scoped run before dependency calls, sends only the
bounded composite evidence to the local model, and stores a canonical evidence hash plus the typed
answer and append-only audit linkage in one completion transaction. Safe dependency failures are
also stored and audited. The panel exposes logical targets and evidence identifiers, not connector
credentials. The original Phase 2 browser gate and the current focused-app browser checks have
passed on their named releases; neither proves production acceptance.

Controlled application release `nextops-0.1.0-01755d1` adds `answer_focus` (`overview`,
`filesystems`, or `file_listing`)
to the incident response. It is derived from question terms: mixed filesystem/service requests
stay in `overview`, while an explicit file-listing request fails safely even if it also mentions
another metric. The exact bounded evidence, hash and audit do not change. Focused prompts receive
only relevant metadata and approved mount observations; displayed focused answers carry
`deterministic_focus` and are built from typed evidence, or state that file listing is unsupported.
The existing read scopes and connector capabilities are unchanged. Release-specific browser/API
checks passed; full held-out semantic review and exact-release rollback remain open.

The controlled application recorded in the [current release manifest](../status/current-release.yaml)
already supplies `X-NextOps-App-Code-SHA256` on successful authenticated answer responses: general,
primary monitoring, selected-source monitoring, incident investigation and saved-message creation.
It hashes the installed NextOps package source and
local UI assets at process startup; unauthenticated responses do not receive the header. The
private reviewer compares it with the same bounded digest computed from a reviewed wheel. It does
not identify dependencies, migrations, model files or host state, and it is not an artifact
signature or production acceptance result.

### 2026-10-07 audit-repair source increment

These repairs describe source behavior, not an additional live acceptance claim. Exact-source
PostgreSQL 16/17 restricted-role CI and the separately authorized, release-identified rollout must
pass before deployment is reported. No database migration, role grant or model profile changes.

Investigation creation/replay and completion recheck the bearer session, expiry, active identity,
credential version and current actor scope inside their persistence transaction. Completion keeps
session/identity read locks through result/audit commit and rechecks the enabled scoped target and
selected logical source/target. Revocation completed before this checkpoint blocks publication.
Selected-source completion access audit and the stored result now share the same transaction.

Direct summary/incident-context reads require user-attributable start and terminal access audits;
the terminal transaction rechecks permission before evidence is returned. Stored run/evidence reads
require a current scoped session and an access audit, including scoped denials/not-found decisions.
Required audit failure blocks return, rather than reporting successful unlogged access. Audit
details contain bounded identifiers, reasons and hashes, not collected text or bearer credentials.

Explicitly labeled secrets, including quoted password/token fields and Basic/Bearer Authorization
values, are replaced by `[REDACTED]` before model input, canonical hashing, persistence and public
evidence responses. The standalone Linux collector and application boundary have matching coverage.
This is not detection of arbitrary unlabeled secrets. Historical results containing these sensitive
representations are denied with `run.evidence_redaction_required`; collect new authorized evidence.
Old stored content, hashes and append-only audit history are not silently rewritten.

Caller cancellation runs bounded, shielded terminal cleanup for saved messages and investigations.
Saved cleanup clears only the matching server-issued generation nonce and records a text-free failed
audit; it can perform this cleanup after logout without granting read or generation permission.
A replacement nonce is never cleared. Audit/database failure remains visible; a process crash still
requires expiry/recovery reconciliation. Local cancellation is not proof remote inference stopped.

Monitoring prompt projections retain application-computed returned problem counts, whether the
total is known, and sample counts. Every row omission/meaningful field clipping marks the prompt
view partial separately from source partiality; the canonical evidence/hash is not changed by
sampling. Bilingual count answers and provenance report returned rows, an unknown total/lower bound
when problems are truncated, exact severity labels (`3=Average`, `4=High`), and unknown reachability
and monitoring-engine health. `deterministic_focus`/`deterministic_fallback` remain distinct from
model synthesis. Narrow lexical rejection of known false count/status/label claims is not general
semantic validation of generated prose.

## Persistence model

PostgreSQL is authoritative. Separate business data from the databases NextOps manages. Define stable IDs, foreign keys, unique constraints, indexes, retention and permission rules for each record group.

| Group | Records and relationships |
|---|---|
| Identity/scope | Organizations, environments, users, roles and scoped grants |
| Inventory | Assets, approved endpoints, capability/version facts and credential references |
| Integration | Connector registrations, versions and tool capabilities |
| Workflow | Incidents/events, runs, steps, durable jobs, leases and checkpoints |
| Evidence | Source references, asset/scope, observed/collected times, sanitized content reference and freshness |
| Actions | Proposals, approvals, execution attempts and verification outcomes |
| Knowledge | Documents/chunks/embeddings, conversations, incident memory, topology nodes/edges |
| Governance | Audit and model/prompt/policy/release versions |

Conceptual relationships: an organization contains environments and scoped users; an environment contains assets; an incident relates to affected assets and workflow runs; runs contain steps and evidence; a proposal relates to an exact target/action and possibly an approval; each execution attempt points to its proposal and verification evidence. Audit records reference the relevant actor, target and operation. This is not an executable ER schema.

Use UTC internally, preserving source timezone, collection time and clock-skew uncertainty. Permission-sensitive data must carry scope. Restrict database roles so API/planning code cannot forge execution approvals through unrestricted database writes.

## Durable workflow

```text
RECEIVED -> AUTHORIZED -> SCOPED -> PLANNED
  -> COLLECTING -> ANALYZING -> PROPOSAL_READY
  -> AWAITING_APPROVAL -> READY_TO_EXECUTE -> EXECUTING
  -> VERIFYING -> COMPLETED

Other outcomes: DENIED, EXPIRED, CANCEL_REQUESTED, CANCELLED,
FAILED, OUTCOME_UNKNOWN, MANUAL_RECONCILIATION_REQUIRED
```

Read-only investigations skip change approval, not authorization or audit. Persist progress around external effects. Use transactional job creation/outbox where necessary, leases/heartbeats and duplicate detection. Do not claim exactly-once execution across a device and PostgreSQL. Reconcile a possibly executed mutation before retry. Local cancellation does not guarantee remote cancellation.

Bound elapsed time, LLM calls/tokens, tool calls/bytes, fan-out and retries. The specification's six LLM calls and twenty tool calls are starting experiments, not measured optimal limits.

## Evidence, retrieval and topology

Store provenance, source version, source and collection timestamps, content hash, authorization scope and redaction/partial-result markers. Filter by permission before retrieval and when serving evidence. A historical incident is not proof of current state. Keep raw monitoring history in its source system where practical.

Start topology with relational edges carrying relationship type, origin, freshness and observed/inferred status. Re-index changed documents only. Track chunk and embedding model versions/dimensions; an embedding switch requires index compatibility work. Cached retrieval remains scope- and freshness-aware.

RCA output separates symptoms, collected evidence, possible causes, supporting and contradictory evidence, confidence with justification, unknowns, next safe diagnostic step and proposed action/risk/approval/verification. Only call a cause verified when supported. Do not generate unsupported numeric probabilities.

## Implemented and planned API behavior

The implemented routes above use `/api/v1`. Fixed-role local user administration and its bounded
account pagination are implemented and controlled-installed as described above; live account
mutations remain unaccepted. Agents, connector/device administration, incident lifecycle management,
separate evidence/audit browsing, approvals, role/scope editing and user deletion, settings,
streaming, general pagination, an explicit client cancellation API and alert ingress remain planned.
Preserve old paths through an explicit compatibility decision if existing code is later
imported. Liveness/readiness endpoints disclose no sensitive public diagnostics.

A long request creates a durable run and returns its ID. Authenticated progress streaming supports reconnection; cancellation is a request, not proof of halted remote work. Define pagination, bounded payloads, idempotent command submission and structured errors. Browser timeouts never erase jobs.

Alert ingress validates payloads, authenticates scoped senders, applies replay/deduplication and rate limits, and routes malformed input for manual review. Anonymous input must not trigger arbitrary operations. No direct browser route to inference or connectors is permitted.
