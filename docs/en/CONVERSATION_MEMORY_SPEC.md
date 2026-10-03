# Bounded conversation memory and local thinking

[فارسی](../fa/CONVERSATION_MEMORY_SPEC.md) · [Operator guide](CONVERSATIONS.md)

Status, 2026-09-30: b5e74f9/35B serves controlled standard saved chat with 16,384 configured
context tokens. Bilingual short follow-ups, exact rollback and four-guest WAN/reboot acceptance
passed. Thinking failed live qualification and is disabled at both boundaries. Full-context
quality/latency and broad technical accuracy remain unqualified; this is not full production.

## Problem and precedence

The owner requested persistent chat, consecutive follow-up questions, more context and thinking,
then extended the AI guest and asked to start implementation. This bounded increment supersedes
the earlier nonpersistent general-chat non-goal in NOC_SOC_WORKSPACE_SPEC, not the live-evidence
policy or failed historical qualification results. Bigger models and thinking do not guarantee
accuracy. The exact 35B conversion lineage remains unverified.

## Requirements and acceptance

- CM-01: local PostgreSQL stores model-only questions and final answers for their authenticated
  owner, organization and environment. Even another administrator receives the same 404 as an
  absent ID. Recheck the current session inside each transaction, including after generation.
- CM-02: at most 50 conversations per identity, 100 completed exchanges and 1 MiB of question/final
  result content per conversation. Availability expires 30 days after creation. Physically purge
  expired owner rows on the next list/create operation; inactive-account rows are not a promise of
  scheduled secure erasure. Explicit deletion cascades transcript rows but retains text-free audit
  metadata. Existing independent backup/snapshot copies have their own retention.
- CM-03: select at most six recent accepted model-only exchanges within 12,000 serialized
  characters. Never clip a pair, persist private reasoning, or reuse live evidence as model memory.
  Expose context omissions. Keep fallback/redirect turns visible but out of subsequent context.
- CM-04: the browser supplies only a UUID request ID, question, locale and a thinking boolean.
  The application owns history, roles, purpose and budgets. Replayed completed IDs return the
  original saved result; a changed payload conflicts. One pending request per conversation uses
  a generation nonce and a 540-second lease. No successful late completion after delete/logout.
- CM-05: saved standard answers have a 1024-token total limit; requested thinking has 2048 total.
  Thinking is general-only and independently enabled by operator configuration. The candidate
  runtime limits reasoning to 384 tokens and extracts it into a discarded provider field.
  This supersedes the failed 1024-token live profile without widening the 120-second deadline.
  Final content containing reasoning tags is rejected. Only a final answer passes to UI/storage.
- CM-06: candidate context is 16,384 tokens, not the advertised native maximum. Read actual
  runtime context from authenticated local properties, render the exact local template, tokenize
  it locally, and reject prompt-plus-output overflow or configuration mismatch before generation.
  One active/two queued requests, CPU-only, credential isolation, no runtime downloads and
  deterministic answer integrity remain mandatory.
- CM-07: English/Persian history selection, follow-ups, response-mode control, RTL/LTR, keyboard
  access, safe literal titles, deletion and logout must pass browser tests. Keep OCS palette/logo.
- CM-08: mutation and transcript access produce text-free audit events; completed transcript and
  its audit commit atomically. Storage/audit failure must not return a successful unsaved answer.

## Non-goals and threats

No fine-tuning, remote memory/AI, vector retrieval, new connector, model tool execution,
cross-user memory, indefinite retention, raw reasoning display or assertion of ChatGPT-equivalence.
Conversation text is untrusted and may inject instructions or repeat false claims. Ownership checks,
scope, budgets and live-fact redirection are code, never model decisions. Local transcripts are
sensitive application data; do not paste secrets. Existing database/TLS/backup controls still apply.

## Implementation plan and tasks

1. Preserve the current qualified release and run the locked baseline.
2. Add typed contracts, additive migration 0003 and an owner-scoped service with quotas, session
   recheck, nonce/idempotency, deletion, expiry and atomic audit.
3. Add authenticated APIs and local history controls; leave the old endpoint compatible.
4. Add gated provider controls, final-only extraction and actual token admission.
5. Run unit/contract, restricted-role PostgreSQL, EN/FA browser and five-job CI checks.
6. Qualify a guarded exact-source candidate on the existing 35B artifact first: standard/thinking,
   repeated follow-ups, longer context, held-out technical correctness, injection, latency, memory,
   recovery after failed generation and exact rollback. Failed or incomplete replies fail quality.
7. Separately provision/verify/benchmark the pinned 122B research shards only after capacity and
   rollback checks. They are not selectable by runtime source and are not a deployed upgrade.
8. Run fresh server-WAN/VM cold-start gates on the selected exact release; fixtures do not count.

## Tests and deployment rollback

### Bounded requalification — 2026-10-03

The owner requests qualification testing and implementation of thinking. Preserve b5e74f9
standard service while diagnosing the exact pinned runtime; do not simply flip the failed flag.
First run explicit native reasoning budgets with synthetic, secret-free questions. A candidate
must deliver a nonempty, complete EN/FA final answer within 120 seconds, discard private reasoning,
and obey an application-owned reasoning budget no greater than 384 tokens and total output at
most 2048. A HTTP 200, truncated reply or template-only success is insufficient.

The new adapter owns a 128-token reasoning request, an explicit analysis-to-final transition
message and a strict `answer` JSON envelope. Only its decoded, complete final answer is returned;
empty/truncated/malformed envelopes, reasoning delimiters and recognizable internal drafting
headings fail closed. These checks are not a proof that arbitrary reasoning prose cannot leak.
Native diagnostic results: the 64-token English trial leaked drafting and failed; four revised
128-token EN/FA final-envelope probes completed in 25.570–61.446 seconds. These short synthetic
passes do not qualify the matched APIs, browser, persisted history, longer context or general
technical correctness. Both live thinking flags remain disabled pending the complete gate.

Then independently review held-out technical correctness and requested format; measure actual
local token counts near the 16K admission boundary, rejection beyond it, latency and memory.
Exercise at most four concurrent synthetic requests against the one-active/two-queued boundary:
the excess request must be denied, waiters must expire within the existing five-second queue
deadline, counters must return to zero and a new request must complete. Do not widen queues,
deadlines, context or resources to obtain a pass. Native diagnostic outcomes, API outcomes and
browser/storage/audit outcomes are separate evidence. Full-budget context generation can fail
even when admission is correct. Preserve raw failed findings outside Git.

Tasks: diagnose template/budget handling; implement trusted bounded controls and regression tests;
run the bounded corpus and contention/recovery; review EN/FA outcomes; qualify exact package and
matched rollback before enabling both flags. No runtime/model replacement, downloads, VM resize,
schema downgrade or new target integration is part of this increment. If any required thinking
gate fails, retain standard live service and the disabled thinking flag. Update both guides,
project state and next task with actual results, not intended acceptance.

Unit tests cover Unicode, whole-pair selection, omission, no client policy/history controls,
live-fact follow-ups, thinking denial, wrong context, token overflow and reasoning leakage.
PostgreSQL tests cover restart, cross-owner denial, concurrent requests, replay/conflict,
logout/delete during generation and restricted grants. Browser fixtures cover local UX, not
production model quality or real WAN isolation.

Enable feature flags only after migration and matched AI-profile qualification. Restore the prior
app/profile and disable feature flags to roll back; leave additive tables intact. Database downgrade
deletes transcripts and is not routine rollback. Documentation, traceability, state, next task and
artifact records must distinguish source, lab, CI and live acceptance.
