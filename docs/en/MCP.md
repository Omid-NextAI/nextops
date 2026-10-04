# MCP gateway and connector contracts

[فارسی](../fa/MCP.md) · [Index](INDEX.md)

**Status: MCP-01 additive source implementation, not deployed.** The existing HTTP connector remains
the live path. The broader gateway contract below is still planned. Source: master specification
sections 11–15 and 21, [bounded specification](../requirements/MULTI_SOURCE_MCP_SPEC.md) and
[ADR 0010](../adr/0010-source-scoped-zabbix-mcp.md).

## Placement and migration contract

The existing `nextops-connectors-ro` VM is the intended MCP gateway/runner host, as required by
master sections 5 and 12 and reaffirmed by the owner on 2026-10-04. Native MCP becomes its canonical
application-facing contract. Zabbix and Linux remain scoped integration drivers behind the gateway,
not an unrelated non-MCP connector beside a second platform. No extra VM is required.

Plan authenticated internal Streamable HTTP over verified TLS between app and gateway. Local
stdio is suitable only inside an appropriately isolated local process boundary; the MCP-01 stdio
tests do not prove an app-to-connector-VM transport. MCP-02 must qualify caller identity/audience,
origin handling where applicable, per-call scope, durable audit, frame limits and runner isolation
before opening a listener. Gateway and runners use separate identities; target tokens stay with
their runner, not the gateway, app or model.

Keep the current serving HTTP release during staged migration and for exact rollback. A temporary
compatibility adapter must enter the same deterministic authorization/audit boundary, never bypass
it or silently substitute another source after a denial/failure. Retire or disable the old interface
at the qualified cutover; retaining rollback artifacts does not require leaving a bypass reachable.
Only implemented, separately qualified tools may be advertised; Linux MCP mapping and the remaining
integration families are not completed by this two-tool Zabbix foundation.

## Implemented Zabbix subset

The optional extra pins the official MIT-licensed [Python SDK v1.30.0](https://github.com/modelcontextprotocol/python-sdk/tree/v1.30.0)
on its maintained 1.x line; it is not an automatic adoption of the latest major. AnyIO, already
locked transitively, is now an explicit dependency for cancellation-safe bounded audit attempts.
Provision dependencies before offline operation; neither the factory nor client installs anything.

`create_source_mcp_server(reader, actor)` and `serve_source_stdio(reader, actor)` require a trusted
actor and application authorization/audit ports. There is no standalone operational launcher or
anonymous listener. Actual SDK initialization, discovery, structured calls, error handling,
explicit cancellation notifications and subprocess stdio exchanges have fixture-backed tests.
`McpSourceGateway` validates source, target, operation and correlation on every response.

Two tools exist: `nextops_zabbix_summary` and `nextops_zabbix_incident_context`. Their closed input
schema accepts only logical `source_id`, `target_id` and UUID `correlation_id`. Endpoint, token,
actor roles and arbitrary method/parameters cannot be supplied through tool arguments. A private
registry binds each source to organization/environment, verified HTTPS/CA, a separate credential
reference, exact hosts and numeric approved groups. Limits: eight sources, sixteen targets per
source, 32 group IDs, 64-KiB registry and 128-KiB canonical result. Windows ACL qualification is a
trusted-launch requirement, not something the registry parser proves.

The reused reader permits only `host.get`, `item.get`, `problem.get`, `history.get`, `event.get`
and unauthenticated `apiinfo.version`. A fresh exact host/group check precedes dependent reads;
history IDs must belong to items from that collection. Results retain source/target/correlation
and the observed approved group intersection alongside the existing timestamps and evidence.
This bounded exact-target subset is not complete host discovery or proof of access to every group.

Authorization is rechecked before collection and before publication. Required audit intent
precedes credential/transport creation; completion includes the canonical SHA-256. Malformed
input/tool denials are audited without their raw text. At most two reads are admitted, without
a waiting queue or retry. Collection and individual authorization/audit waits each default to
30 seconds (maximum 60); the client has its own explicit 30-second wait. Cancellation/timeout
prevents subsequent reads but cannot stop an in-flight native HTTPS request. Its admission slot
is held until actual drain. A client wait cancellation is not a protocol cancellation notice.

MCP-02 must supply **real durable PostgreSQL ports**, trusted caller/source selection, protected
credential loading and runner launch, bounded protocol frames, safe SDK logging, and qualified
process egress. MCP-03 must qualify offline provisioning, live bilingual browser answers, audit
correlation, source failure and rollback. Fixture audits, desktop API probes and passed contracts
do not satisfy those gates. No second source is available in the live UI yet.

## Protocol versus application abstraction

A Python method named `execute()` is not an MCP implementation. Use the official maintained SDK with a pinned, tested protocol version: initialization, capability negotiation, tool discovery, typed schemas, results/errors, cancellation and transport behavior. Resolve exact versions at implementation time.

Prefer local stdio for suitably isolated local connectors. Use authenticated Streamable HTTP for independently deployed long-running services when justified. Never expose unauthenticated endpoints; validate origins where applicable. Client identity, MCP sessions, downstream credentials and token audiences are different concerns. Do not blindly pass client tokens to downstream devices.

## Registry and boundaries

Begin with an administrator-controlled registry of reviewed connector manifests. Do not automatically install arbitrary remote MCP servers. Enable only required connectors. Each connector has a version, supported target/version matrix, health information, credential-reference requirements and bounded tool catalog.

The gateway authenticates callers, checks authorization and policy, validates approvals, enforces deadlines and quotas, records audit, routes calls and reports typed failures. Connector runners recheck relevant constraints and reject direct unauthenticated calls. Validate destinations, redirects and resolved addresses against authorized inventory; avoid unrestricted discovery and SSRF-style proxy behavior.

## Planned tool definition

| Field group | Required meaning |
|---|---|
| Identity | Name, version, connector and supported target types |
| Contract | Typed input/output schemas and structured error classes |
| Authorization | Required scope, environment and deterministic risk class |
| Execution | Timeout, byte/row/output limits, concurrency and cancellation behavior |
| Safety | Approval requirement, preconditions, idempotency semantics and verification |

Remote tool descriptions or read-only annotations are untrusted metadata. Policy authority remains in versioned application rules.

## Planned execution request and result

Request: operation ID, authenticated actor/scope, immutable target ID, validated arguments, policy version, optional approval reference, deadline, idempotency key and correlation ID.

Result: status, collection/execution timestamps, sanitized evidence references, partial-result marker, verification outcome and structured authentication/permission/connectivity/vendor errors. A connector without a capability returns an explicit unsupported result, never invented success.

## Bounded execution sequence

```text
Authorize actor and target
  -> validate named operation and arguments
  -> check policy / approval / preconditions / audit availability
  -> record durable intent
  -> execute through scoped connector
  -> persist result or unknown outcome
  -> verify fresh target state when applicable
  -> finish audit and user-visible summary
```

Eligible reads may use bounded retries and backoff. A mutation that timed out may already have executed; mark `OUTCOME_UNKNOWN` and reconcile before another attempt. Cancellation of a local request does not prove a remote command stopped. Connector failure must not crash the whole platform.

## Acceptance

Protocol conformance, invalid input, auth failures, target substitution, cancellation, bounded outputs, partial data, connector crash, replayed approval, duplicate delivery and unknown remote outcomes require tests. Simulators are the default; actual devices require explicit authorization and a documented lab/version record.
