# Current technology stack and future options

[فارسی](../fa/TECH_STACK.md) · [Index](INDEX.md) · [Architecture](ARCHITECTURE.md) · [Diagrams](DIAGRAMS.md) · [CPU evaluation](CPU_AI.md)

## Deployed controlled slice, 2026-10-07

This guide describes the current repository and retained deployment, not a technology replacement
plan. [Release status](../status/current-release.yaml) owns exact serving identities/artifact pins;
[pyproject.toml](../../pyproject.toml) and [uv.lock](../../uv.lock) own package definitions and
resolved versions. App/API/MCP source is `52e5179`. Live controlled use is not production acceptance.

| Layer | Current implementation | Important boundary |
|---|---|---|
| Physical host and guests | Existing ESXi/G10; four existing Ubuntu 24.04 role guests | One failure domain; Ubuntu is not a replacement ESXi host |
| Python and packaging | Python 3.12, uv, setuptools; application version 0.1.0 | Frozen reviewed lock and preprovisioned offline wheel bundles |
| API/contracts | FastAPI, Pydantic, Uvicorn | Typed validation plus independent deterministic authorization |
| State/migrations | PostgreSQL 16.15, Psycopg, SQLAlchemy, Alembic | Separate restricted NextOps and Zabbix databases; no shared administrator account |
| Execution | Bounded API use cases, persisted investigations/results/audit and conversation records | Not a deployed generic background-worker/outbox platform |
| CPU inference | Pinned llama.cpp `v0.4.1` / `b29c606e`, selected Qwen3.8-27B Q8 | Local CPU only; no cloud, GPU dependency or runtime download |
| MCP | Official Python SDK `mcp==1.30.0`; authenticated Streamable HTTP/TLS | Canonical gateway on the existing connector VM; MCP is not authorization |
| Runner boundary | Separate gateway/runner identities; bidirectional peer-UID-verified Unix socket | Target credentials and approved LAN routes belong only to the runner |
| Evidence drivers | Scoped Zabbix JSON-RPC; existing forced-command Linux SSH collectors | Protected source/target catalog, TLS/SSH trust, allowlists, deadlines and response caps |
| Frontend | Local semantic HTML, CSS and JavaScript in `packages/nextops/api/static/` | No React/Vite/Tailwind/Node production server or new frontend package manager |
| Brand and localization | Unchanged local OCS dark/light JPEGs, company tokens, EN/FA dictionaries, RTL/LTR and themes | Static company-logo login; no remote fonts, icon CDN or hosted translation |
| Deployment | Native systemd units, Nginx/TLS, immutable releases and protected stable links | Verified offline import and exact rollback; not automatic deployment on GitHub push |
| Quality | Ruff, mypy, pytest, HTTPX, Playwright, real PostgreSQL 16/17 integration, Gitleaks and validators | Fixture/source tests and real infrastructure acceptance remain separate |

The official MCP SDK is already deployed, not an unevaluated future dependency. The old HTTP
connector service is disabled and retained only for exact rollback. The secondary Zabbix server
is an approved API integration; its separate existing Docker stack is not NextOps's deployment
technology or a newly managed database.

## Selected inference profile and its limits

The retained profile uses 32 workers, one native slot, configured 16K context, six whole saved
turns, one active/two queued requests and thinking off. Queue/provider/app/proxy budgets remain
5/300/330/360 seconds. The native memory limit remains 96 GiB. Guest allocations and apparent
free host RAM are not measurements of model quality, usable concurrency or NUMA locality.

Raw model quality remains failed at 13/16 under the recorded owner exception. Thinking/privacy,
full-window quality and current-source WAN/VM/load qualification remain open. The chosen
configuration is not a claim that this model is the latest vendor model, universally accurate or
the fastest CPU option. Compare candidates only with pinned artifacts and measured acceptance;
see [CPU AI](CPU_AI.md) and [Testing](TESTING.md).

## Frontend and data conventions

Keep the current modular static implementation. `app.js`, `theme.js`, `capabilities.js` and
`investigation-view.js` use existing API contracts; CSS responsibilities and local assets remain
separate. `pyproject.toml` includes `static/*` in the wheel. No frontend lockfile is required for
a package graph that does not exist; adding React merely to satisfy an old proposal would rebuild
working architecture.

UI state cannot authorize operations or substitute cached evidence for fresh reads. Saved-chat
data is backend-owned and owner-scoped; visual theme preferences are separate. Keep technical
identifiers/code LTR within Persian RTL, UTC in storage, readable local font fallbacks, explicit
failure states, keyboard access and logout-sensitive-state cleanup.

## Retained future options, not installed capabilities

These preserve the earlier design choices without presenting them as today's implementation.
Each adoption needs a bounded specification, relevant ADR, offline provisioning, bilingual
acceptance and measured benefit.

| Option | Appropriate trigger | Must preserve |
|---|---|---|
| General PostgreSQL-backed worker, leases/checkpoints/outbox | A feature needs durable asynchronous execution beyond current bounded use cases | Audit, permission rechecks, idempotency and uncertain-outcome reconciliation |
| React/TypeScript/Vite; reviewed shadcn/ui/Tailwind/i18next/TanStack Query | A justified frontend migration, not reference reconstruction alone | Local static output, session contracts, owner isolation, EN/FA and accessibility |
| Local retrieval/pgvector and optional CPU encoder/reranker | Bilingual relevance and authorization filtering prove useful | Document provenance separate from live evidence; no remote embeddings |
| React Flow/topology | A permitted, bounded topology API exists | Provenance/freshness, keyboard alternatives and read-only starting scope |
| Local OpenTelemetry/Prometheus/Grafana | A specific operational visibility need | Redaction/local telemetry; security audit remains independent |
| Redis or another workflow framework | Measurement demonstrates missing functionality | PostgreSQL authority and compatible recovery/approval semantics |
| Other CPU inference runtimes or replicas | Benchmarks justify migration or added complexity | No cloud fallback/GPU requirement; pinned templates, resources and rollback |
| Compose inside guests | A separately reviewed deployment need | No-pull offline artifacts, no container socket, equivalent enforced boundaries |

Broader connectors and controlled remediation remain in the roadmap, not invented active
integrations. Kubernetes, Kafka, service mesh, remote AI and foundational model training are not
required to improve the current evidence path.

## Packaging and release discipline

Provision runtime/native libraries, Python wheels, UI/translations/API-documentation assets,
model/template files and browser test dependencies deliberately. Missing artifacts must fail
preflight/readiness, not silently download. Keep component/model licenses and hashes, exact source
and build flags in their existing manifests. Development tools are not automatically runtime
dependencies.

GitHub CI runs without infrastructure credentials. It covers PostgreSQL 16 (deployed major) and
17; a green check does not configure branch protection or deploy a release. Follow
[Development](DEVELOPMENT.md), [Offline runtime](OFFLINE_RUNTIME.md) and
[the current bounded qualification](../requirements/AUDIT_REPAIR_LIVE_QUALIFICATION_2026-10-07.md).
Independent recovery remains owner-deferred, not passed.
