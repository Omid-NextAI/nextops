# Architecture diagram atlas

[فارسی](../fa/DIAGRAMS.md) · [Index](INDEX.md) · [Technology stack](TECH_STACK.md) · [Architecture](ARCHITECTURE.md)

## Current controlled system, 2026-10-07

These three views describe retained source `52e5179` and the existing four-role deployment.
They contain sanitized role names, not private inventory. The
[manifest](../status/current-release.yaml) and
[live qualification](../requirements/AUDIT_REPAIR_LIVE_QUALIFICATION_2026-10-07.md) own identities
and measured gates. Diagrams are descriptive, not authorization or new production acceptance.

### C1. Deployment and credential ownership

```mermaid
flowchart LR
    Browser["Authenticated EN/FA browser"] -->|"HTTPS"| Web
    subgraph Host["Existing ESXi / G10: one failure domain"]
        subgraph AppVM["App guest"]
            Web["Nginx / local static UI"] --> API["FastAPI / deterministic application policy"]
            API --> DB[("Restricted NextOps PostgreSQL")]
        end
        subgraph AIVM["AI guest: CPU only"]
            AI["Protected inference API"] --> Native["Pinned llama.cpp / Qwen Q8"]
            Files["Verified local model / template"] --> Native
        end
        subgraph ConnectorVM["Existing connector guest"]
            Gate["Authenticated MCP gateway: no target secrets"] -->|"Unix socket: peer UID checks both ways"| Runner["Isolated read-only Zabbix / Linux runner"]
            Secrets["Protected target tokens / SSH keys"] --> Runner
        end
        subgraph ZabbixVM["Dedicated primary Zabbix guest"]
            Primary["Zabbix API / monitoring"] --> ZDB[("Separate Zabbix PostgreSQL")]
        end
        API -->|"Restricted verified SSH tunnel"| AI
        API -->|"MCP Streamable HTTP / TLS through verified SSH tunnel"| Gate
        Runner -->|"Approved HTTPS JSON-RPC reads"| Primary
        Runner -->|"Forced-command SSH reads"| Linux["Existing collectors on four approved guests"]
    end
    Runner -->|"Approved HTTPS API only"| Secondary["Existing secondary Zabbix: no server administration"]
```

The gateway has loopback-only networking; only its separate runner reaches approved targets.
Application service credentials, target tokens and user sessions are different identities.
The disabled old HTTP service is not a fallback. GitHub/package registries have no runtime arrow.
No additional database, connector or GPU VM is implied.

### C2. Source-scoped investigation, evidence and audit

```mermaid
sequenceDiagram
    autonumber
    actor User as Authenticated user
    participant API as App API / policy
    participant DB as NextOps PostgreSQL
    participant Gate as MCP gateway
    participant Runner as Isolated runner
    participant Target as Approved Zabbix / Linux
    participant AI as Local CPU inference
    User->>API: Question + approved source/target
    API->>DB: Current session/scope checks + durable start
    API->>Gate: Named read + service identity + binding/correlation
    Gate->>Runner: Bounded operation over peer-verified Unix socket
    Runner->>Runner: Check registry, source binding, scope and limits
    Runner->>Target: Allowlisted read with runner-held target credential
    Target-->>Runner: Bounded observations or explicit dependency failure
    Runner-->>Gate: Typed source/time/scope envelope
    Gate-->>API: Validated envelope or typed denial/failure
    alt Valid evidence and generation available
        API->>API: Validate, redact, compute scoped counts/coverage
        API->>AI: Question + sanitized evidence + bounded budget
        AI-->>API: Successful final answer
        API->>API: Deterministic answer-integrity checks
        API->>DB: Recheck current access; atomically commit result/hash/audit
        alt Current access and mandatory audit commit succeed
            DB-->>API: Committed authorized result
            API-->>User: Answer + source/time/scope and limitations
        else Access revoked or required audit fails
            DB-->>API: Denial or dependency failure
            API-->>User: Explicit error; no result disclosure
        end
    else Missing/denied/failed dependency
        API->>DB: Mandatory bounded failure audit
        API-->>User: Explicit limitation/error; no invented healthy evidence
    end
```

Timeout/generation errors follow the failure/audit path, not successful result disclosure.
The request is bounded API orchestration, not a deployed general worker. The gateway's fsynced
service journal is supplemental; it does not bypass mandatory PostgreSQL user audit. General chat
uses its existing owner-scoped conversation endpoints without requiring a Zabbix read. Saved
history is not fresh infrastructure evidence or model training. Out-of-band privileged target
changes still require controlled quiescence.

### C3. Bounded inference and physical-call ownership

```mermaid
flowchart TB
    Q["Authenticated local request"] --> Admission["Bounded admission: one active / two queued"]
    Admission -->|"Capacity and budget available"| API["Protected AI API"]
    Admission -->|"Queue full / five-second wait expires"| Busy["Explicit busy / timeout"]
    API --> Native["One CPU llama.cpp slot: 32 workers"]
    Native --> Result["Final answer / typed failure"]
    Cancel["Cancellation / provider timeout"] --> Drain["Retain physical-call ownership"]
    Native --> Drain
    Drain -->|"Verified completion / idle"| Release["Release admission"]
    Drain -->|"Idle uncertain"| Closed["Fail closed: do not overlap another generation"]
    Result --> Integrity["Application integrity, late authorization and audit"]
```

Configured context is 16K with six whole saved turns; thinking is off. Queue/provider/app/proxy
budgets remain 5/300/330/360 seconds. A successful health probe is not native-idle proof. Cancellation
is not proof of remote stop. Raw quality, thinking/privacy, full-window, current-source server-WAN,
VM cold start and sustained load remain unqualified; browser WAN blocking alone is not server
offline acceptance.

## Future target atlas: preserved design, not current deployment

The seven original views below retain target concepts from the master specification. Their
general worker, retrieval, topology, embeddings, off-host backup and remediation paths are not
deployed by this documentation update. Direct database arrows in these conceptual views do not
grant the current gateway database access. See C1–C3 for the actual path.

Each view answers a separate design question. Arrows describe labeled data/request/state flows,
not unrestricted network permission. Dashed provisioning links are not cloud runtime dependencies.
The active v3 master prompt and its immutable v2 archive remain unchanged by this update.

### 1. System context and trust boundaries

Who interacts with NextOps, and where may infrastructure credentials exist?

```mermaid
flowchart TB
    U["Operator | Persian / English"] --> P["TLS reverse proxy"]
    E["Authenticated monitoring events"] --> P
    P --> A["FastAPI control plane"]
    A --> D[("PostgreSQL | runs and durable jobs")]
    W["Bounded workflow worker"] <-->|"Lease and checkpoint"| D
    W <-->|"Sanitized evidence and synthesis"| L["Local CPU inference | no target credentials"]
    W <-->|"Authorized retrieval"| K["Evidence and topology"]
    W <-->|"Typed requests and results"| G["MCP gateway | policy, audit, limits"]
    G <-->|"Authorized operation"| C["Isolated connector runners"]
    S["Target-scoped secret references"] --> C
    C <-->|"Allowlisted destinations"| T["Authorized infrastructure"]
```

The worker requests evidence through the gateway; it does not connect directly to devices. The model receives only permitted, sanitized context. Policy is enforced again at the execution boundary. All eleven integration families fit behind the connector contract; not all run by default.

### 2. Single-host deployment and network zones

Where do the processes run, and what happens when the G10 fails?

```mermaid
flowchart TB
    B["User browser"] -->|"HTTPS"| R
    GH["GitHub | approved release artifacts"] -.->|"Controlled provisioning"| I
    subgraph HOST["One G10 host | one failure domain | CPU only"]
        I["Owner-controlled release importer"]
        subgraph EDGE["User-facing zone"]
            R["Reverse proxy and static UI"]
        end
        subgraph CONTROL["Private control-plane zone"]
            A["API"]
            W["Durable worker"]
            DB[("PostgreSQL | separate service roles")]
            EV["Restricted evidence storage"]
        end
        subgraph AI["Inference zone | no Internet or device access"]
            L["CPU generation service"]
            M["Verified local model files"]
        end
        subgraph EXEC["Execution zone | scoped egress"]
            G["Authenticated MCP gateway"]
            C["Enabled connector runners"]
        end
        R --> A
        A --> DB
        W <--> DB
        W <--> EV
        W <--> L
        M --> L
        W <--> G
        G <--> C
        BK["Consistent encrypted backup job"]
        DB --> BK
        EV --> BK
    end
    C <-->|"Approved management LAN targets"| T["Devices and monitoring systems"]
    BK -->|"Protected transfer"| O["Independent off-host backup destination"]
```

Zones are intended restrictions, not implemented firewall rules. Compose networks alone are not a complete egress policy. Only the reverse proxy is user-facing; host administration has a separate approved path. Importing a release is not permission to run arbitrary GitHub workflows on the management host. Recovery keys need their own protected recovery process. The off-host backup destination is still unresolved; a second directory on the G10 is not disaster recovery.

### 3. First read-only investigation

How does the first useful workflow produce an evidence-linked answer?

```mermaid
sequenceDiagram
    autonumber
    actor User as Operator
    participant API as API
    participant DB as PostgreSQL
    participant Worker as Durable worker
    participant Gate as Policy and MCP gateway
    participant Target as Linux / Zabbix connector
    participant Model as Local CPU model
    User->>API: Submit scoped investigation
    API->>API: Authenticate, authorize, validate
    API->>DB: Persist run and job atomically
    API-->>User: Run ID and authenticated progress stream
    Worker->>DB: Lease job and checkpoint
    Worker->>Gate: Named read-only operation with limits
    Gate->>Gate: Recheck identity, scope, target and policy
    alt Request denied
        Gate->>DB: Record denial audit
        Gate-->>Worker: Structured denial, no target call
        Worker->>DB: Persist denied outcome
    else Authorized diagnostic
        Gate->>DB: Record authorized request
        Gate->>Target: Execute bounded diagnostic
        Target-->>Gate: Result or explicit partial/error status
        Gate->>DB: Record sanitized result metadata and audit
        Gate-->>Worker: Permission-scoped evidence references
        Worker->>Model: Sanitized evidence, question and output budget
        Model-->>Worker: Hypotheses and evidence-linked draft
        Worker->>Worker: Check schema, references and unsupported claims
        Worker->>DB: Persist answer or degraded outcome
    end
    User->>API: Read current run state
    API->>DB: Fetch run with authorization
    API-->>User: Answer, evidence or explicit failure state
```

Change approval is not needed for an authorized read, but access checks and audit still apply. Connector failures must remain visible; missing evidence is not replaced with invented measurements. Model unavailability leaves a readable run and its collected evidence, not a silently rerouted cloud request. Sequence arrows to PostgreSQL represent distinct scoped service roles, not a shared superuser.

### 4. Future remediation lifecycle

How is an exact action approved, and how are ambiguous remote outcomes handled?

```mermaid
stateDiagram-v2
    [*] --> Proposed
    Proposed --> Denied: Mutation disabled or policy denies
    Proposed --> AwaitingApproval: Reviewed runbook and scope permitted
    AwaitingApproval --> Denied: Rejected
    AwaitingApproval --> Expired: Approval TTL reached
    AwaitingApproval --> Recheck: Exact-action approval recorded
    Recheck --> Invalidated: Target, arguments, policy or pre-state changed
    Recheck --> Denied: Permission revoked or audit unavailable
    Recheck --> Executing: Atomic single-use authorization
    Executing --> Verifying: Remote result received
    Executing --> OutcomeUnknown: Transport timeout after possible effect
    OutcomeUnknown --> Reconciling: Fresh authorized state read
    Reconciling --> Verifying: Outcome established
    Reconciling --> ManualReview: Cannot establish outcome
    Verifying --> Completed: Postconditions confirmed
    Verifying --> ManualReview: Postconditions fail
    Denied --> [*]
    Expired --> [*]
    Invalidated --> [*]
    Completed --> [*]
    ManualReview --> [*]
```

**All mutation paths remain disabled in the MVP.** Approval binds the exact action, arguments, target, requester, environment, expected pre-state, policy version, expiry and single-use nonce. An uncertain outcome must never trigger a blind retry. Cancellation of local work does not prove remote cancellation. Rollback is a separately authorized operation, not an automatic transition in this diagram. This is the remediation sub-workflow, not the entire investigation state machine.

### 5. Core data relationships

What must be stored durably? This is a conceptual subset—not an implemented schema.

```mermaid
erDiagram
    SCOPE ||--o{ ASSET : contains
    SCOPE ||--o{ RUN : limits
    RUN ||--o{ JOB : schedules
    RUN ||--o{ EVIDENCE : collects
    ASSET ||--o{ EVIDENCE : concerns
    RUN ||--o{ PROPOSAL : produces
    PROPOSAL ||--o{ APPROVAL : requests
    PROPOSAL ||--o{ EXECUTION : attempts
    APPROVAL o|--o| EXECUTION : authorizes
    RUN ||--o{ AUDIT_EVENT : records
    ASSET ||--o{ TOPOLOGY_EDGE : source
    ASSET ||--o{ TOPOLOGY_EDGE : destination
    SCOPE {
        uuid id PK
        string environment
    }
    ASSET {
        uuid id PK
        uuid scope_id FK
        string credential_ref
    }
    RUN {
        uuid id PK
        uuid scope_id FK
        string status
    }
    EVIDENCE {
        uuid id PK
        uuid run_id FK
        datetime collected_at
        string content_hash
    }
    APPROVAL {
        uuid id PK
        uuid proposal_id FK
        string action_digest
        datetime expires_at
    }
    EXECUTION {
        uuid id PK
        uuid proposal_id FK
        uuid approval_id FK
        string outcome
    }
```

Execution approval is nullable for permitted reads; policy requires it for enabled mutations. A consumed approval cannot authorize another execution: enforce uniqueness and atomic transitions. Scope-safe foreign keys, role assignments, retention, audit-only administrative events, document chunks and many-to-many evidence links need the full design in [Data and API](DATA_API.md). `credential_ref` is a reference, never a plaintext credential. An asset relation is observed or inferred with provenance and freshness; it is not proof of a live network link.

### 6. CPU work admission and resource control

How can the API stay responsive while the model is busy?

```mermaid
flowchart LR
    U["Interactive investigation"] --> Q["Bounded admission queue"]
    B["Batch ingestion or re-indexing"] --> Q
    Q --> S["Scheduler | priority and global CPU budget"]
    S -->|"Measured generation slots"| L["One local generation service"]
    S -.->|"Lower-priority bounded work"| E["CPU embedding worker | when enabled"]
    S -->|"Queue full or deadline exceeded"| D["Explicit busy / deferred result"]
    M["Verified local model registry"] --> L
    M --> E
    C["cgroups, thread caps and NUMA-aware allocation"] --> L
    C --> E
    R["Reserved control-plane capacity"] --> A["API, audit, PostgreSQL and manual views"]
    L --> O["Measure queue delay, TTFT, latency and memory"]
    E --> O
    O -.->|"Reviewed tuning"| S
```

The initial benchmark starts with one active generation request and increases concurrency only after measurement. The diagram is not a claim of a specific thread count, core count or tokens/second. Count prompt work, generation, embeddings, ingestion, compilation and database activity in one resource budget. Async APIs do not make CPU-heavy inference free. The old 90-CPU/1-TB estimate is historical; the hardware record supersedes it without establishing available serving capacity.

### 7. GitHub-to-server release path

How do reviewed artifacts reach the server without granting untrusted code infrastructure access?

```mermaid
flowchart LR
    C["Small source change"] --> PR["Reviewable branch / pull request"]
    PR --> CI["Isolated checks | no device credentials"]
    CI --> REV["Review and approved commit"]
    REV --> ART["Pinned build, checksums and dependency manifests"]
    ART --> LAB["Authorized staging and CPU validation"]
    LAB --> GATE["Owner release approval"]
    GATE --> PRE["Backup, migration and compatibility preflight"]
    PRE --> DEP["Controlled G10 deployment"]
    DEP --> HEALTH["Readiness and verification"]
    HEALTH -->|"Healthy"| ACCEPT["Accept release"]
    HEALTH -->|"Unhealthy"| REC["Tested rollback or recovery procedure"]
```

This is a future end-to-end promotion policy, not a claim of automated deployment. Isolated Actions CI is configured; it does not authorize server access. Generic pull requests never run on a privileged persistent G10 runner. Hardware/lab checks are explicitly authorized and isolated. Rollback must account for schema and model compatibility; restarting an older container does not undo a database migration. Offline releases follow the same verification gates through an imported bundle.

### Editing and rendering

Keep English and Persian views equivalent. Diagram identifiers and database fields stay in English; explanations and operator-facing labels are localized. Use ordinary Mermaid `flowchart`, `sequenceDiagram`, `stateDiagram-v2` and `erDiagram` blocks. GitHub supports Mermaid in Markdown; syntax support depends on its renderer version. See [GitHub's diagram guide](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams), reviewed 2026-09-20.

No external image host, embedded credential, production address or diagram-generation service is required. GitHub rendering is a documentation feature, not part of NextOps's offline runtime. Text/link checks are not a Mermaid rendering test. The [earlier review record](../VISUAL_REVIEW.md) is historical, not proof that the new C1–C3 views were rendered.
