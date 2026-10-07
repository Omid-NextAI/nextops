# Architecture and repository structure

[فارسی](../fa/ARCHITECTURE.md) · [Index](INDEX.md) · [Current diagrams](DIAGRAMS.md) · [Technology stack](TECH_STACK.md)

## Current system: controlled deployment, 2026-10-07

The retained app, AI API and canonical MCP/source runner use exact source `52e5179`, with the
matching Linux collector on all four existing guests. This is controlled user testing, not full
production acceptance. The [release manifest](../status/current-release.yaml) owns component
identities and gate results; the [dated live record](../requirements/AUDIT_REPAIR_LIVE_QUALIFICATION_2026-10-07.md)
owns the observed qualification. Updating this guide neither deploys code nor extends acceptance.

Keep the modular control plane and separate processes where credential, network or resource
isolation requires them. The current application executes bounded investigations through its API
use cases and persists results/audit in PostgreSQL. There is no deployed general-purpose durable
worker, retrieval service, topology service or infrastructure-change executor. Those remain target
architecture, not missing prerequisites to rebuild the functioning read-only path.

```text
Authenticated browser -> HTTPS / Nginx -> app API + deterministic policy
                                          |-> NextOps PostgreSQL: sessions, runs, saved chat, audit
                                          |-> protected AI API -> local CPU llama.cpp
                                          |-> authenticated MCP gateway on connector VM
                                                -> peer-verified Unix socket
                                                -> isolated Zabbix/Linux runner
                                                -> approved LAN targets only
```

## Placement and trust boundaries

Four existing Ubuntu guests share one ESXi/G10 failure domain. They are not host-loss high
availability. Initial resource tables in the startup/storage guides are historical provisioning
profiles, not a claim about today's available capacity or the resized AI guest.

| Role | Current responsibility | Boundary |
|---|---|---|
| App VM | Nginx/TLS, static EN/FA panel, FastAPI application, local identity and restricted NextOps PostgreSQL | Application policy authorizes current users; no target credentials or direct managed-device route |
| AI VM | Protected inference API and one pinned local CPU llama.cpp/model service | Sanitized questions/history/evidence only; no target credentials, cloud fallback or device access |
| Existing connector VM | `nextops-mcp.service` gateway and `nextops-source-runner.service` runner | Distinct service identities; only the runner holds target tokens/SSH keys and approved LAN reachability |
| Dedicated Zabbix VM | Primary Zabbix service/API, its separate PostgreSQL and existing Linux collector | Not the NextOps database; monitored through approved read-only bindings |
| Existing secondary Zabbix | Additional approved API source, outside the four-role deployment | API-only integration; no server administration or new VM implied |

The application reaches AI and MCP through separate restricted, host-key-verified SSH tunnels.
MCP uses authenticated Streamable HTTP with TLS and the pinned official Python SDK. Gateway and
runner communicate over a Unix socket with peer-UID checks in both directions. The gateway is
loopback-only and has no target credential or target-LAN route. Its deployment service principal
does not replace the application's current end-user authorization.

The former HTTP connector service is disabled. Its original artifacts remain for exact rollback,
not an alternate live connector, automatic fallback or authorization bypass. See
[MCP contracts](MCP.md), [ADR 0010](../adr/0010-source-scoped-zabbix-mcp.md) and `deploy/mcp/`.

## Current investigation and disclosure path

1. Authenticate locally, resolve an approved source/target binding, check current user scope and
   record the bounded investigation.
2. Call a named MCP read. Gateway/runner validate identity, binding digest, correlation, operation,
   scope, deadlines and response bounds. The runner uses the existing restricted Zabbix or
   forced-command Linux driver; arbitrary URLs, JSON-RPC methods and shell commands are not tools.
3. Validate returned evidence and redact recognized secrets before prompting, hashing, storage or
   response. Compute counts and clipping/coverage in code under the returned authorized scope.
4. Generate locally, then apply deterministic answer-integrity checks. General model knowledge,
   saved conversation and fresh infrastructure evidence remain distinct.
5. Recheck current session/user/scope/source access and atomically persist the result, evidence
   hash and mandatory completion audit before successful disclosure. Authorized reads also require
   audit; failure must not become successful unlogged access.

Redaction is defense in depth, not a guarantee for every possible secret format. Application
target-update grants remain absent; out-of-band privileged target edits require controlled
quiescence. Do not describe the implemented late checks as universal serializability.

The protected catalog contains two sources and seven approved targets; three secondary targets
have bounded read-only qualification. Catalog visibility is authorized metadata, not network
discovery, all-group enrollment or proof of health. API success, host enabled state, reachability
and monitoring-engine health are different facts. Missing/stale/partial evidence stays explicit.

## Model, memory and interface

The configured label is Qwen3.8-27B Q8, running on CPU with 32 workers, one native slot, configured
16K context, six whole saved turns, thinking off and one active/two queued requests. Existing
queue/provider/app/proxy budgets are 5/300/330/360 seconds. Artifact pins belong in the manifest
and model profiles, not a second inventory in this guide. Configured capacity is not qualified
full-window quality or a throughput guarantee.

Native admission retains physical-call ownership through cancellation/timeout until verified
drain; uncertain idle fails closed. A healthy API is not proof the model is idle, and browser
cancellation does not prove remote generation stopped.

Owner-scoped saved conversations use existing PostgreSQL endpoints and bounded history, not model
training or unlimited memory. Logout clears sensitive view state. The current panel is locally
served HTML/CSS/JavaScript with EN/FA, RTL/LTR, persistent theme preference and evidence on demand.
The login uses unchanged local OCS dark/light images and a static company-logo composition; the
earlier animated gate is not the selected login.

## Actual source and deployment layout

```text
packages/nextops/
  api/                 # FastAPI composition and static/* presentation assets
  application/         # identity, investigations, source access, conversations, users
  contracts/           # typed request/result/evidence contracts
  domain/              # entities and invariants
  policy/              # deterministic authorization and answer integrity
  inference/           # local providers, capabilities and bounded admission
  connectors/          # real MCP gateway/runner, scoped Zabbix/Linux drivers
  persistence/         # PostgreSQL repositories and transactions
  security/            # trust, authentication, catalogs and secret handling
migrations/            # Alembic migrations
deploy/                # native systemd, MCP, inference, TLS and installer profiles
scripts/               # validators, isolated qualification and lifecycle tooling
tests/                 # unit/API, real PostgreSQL, protocol and browser coverage
docs/                  # maintained EN/FA guides, requirements, ADRs and evidence
pyproject.toml         # Python/package definitions and static asset inclusion
uv.lock                # reviewed resolved dependency lock
```

Keep domain/application boundaries independent of framework I/O. Do not create the older proposed
`apps/web`, `apps/worker`, `knowledge` or `observability` trees just to match an aspirational diagram.

## Future architecture and remaining acceptance

A general durable worker, document retrieval/embeddings, topology, expanded connectors and approved
remediation remain bounded future features. React/Vite and other optional libraries are proposals,
not the deployed frontend. Any migration needs evidence of benefit, compatible offline packaging,
an appropriate ADR and tests; MCP itself is not the authorization system.

The raw-model result remains failed at 13/16 under the recorded owner exception. Thinking/privacy,
full-context quality, current-source server-WAN isolation, VM cold start and sustained load are
unqualified. Earlier release tests are dated history, not acceptance of this source. Independent
recovery is owner-deferred, not passed; repository protection also needs administration access.
See [Next task](../NEXT_TASK.md) and [Testing](TESTING.md). GitHub is a development/publication
source only, never a runtime dependency; missing artifacts fail explicitly rather than downloading.
