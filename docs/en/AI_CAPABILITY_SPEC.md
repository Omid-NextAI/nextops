# AI capability improvement — bounded increment 1

[فارسی](../fa/AI_CAPABILITY_SPEC.md) · [Model comparison](MODEL_UPGRADE_SPEC.md)

Status: implemented in source, 2026-10-03; standard native completion passed, semantic/coding
qualification failed. Source `c145500` remains unpromoted. This is not production readiness.

Measured outcome: 18 new final answers completed in 3.428–79.780s (median 13.602s); all four
exact checks passed. Technical scope and coding conformance still failed, notably a Persian
function that invented port-range input and retained an invalid unhandled test. Both code blocks
compile, but were not executed. Offline guard replay changed four synthetic/stale-data replies
into scope redirects; that is not matched serving-API/browser acceptance. Preserve this frozen
corpus and scores. The next repair needs new cases, not a retuned pass on this set. See
[testing](TESTING.md). Thinking, near-budget context, live promotion and WAN/cold-start/rollback
for this revision were not run after the prerequisite failure.

## Problem and baseline

## Increment 2 plan — 2026-10-04

The owner requests gap repair and an iterative qualification-to-deployment loop. Preserve v1
results; do not retry unchanged failures or relabel tuned cases as independent. First repair
diagnostic intent classification (a supplied hypothetical is not a request to inspect our live
hosts), with mixed live requests still redirected. Strengthen coding requirement conformance:
no invented input grammar, exact requested test count and correctly handled expected errors.
Checks must describe their actual scope, including absence of a log entry not proving a cause.
Freeze a new EN/FA corpus before local generation; this is engineering evaluation, not an external
benchmark. Tests cover malicious mixed questions, unsupported execution and existing live guards.
No schema, dependency, model, thinking, resource or branding change is planned.

Run the locked tests/CI, then an authorized protected standard35 probe with fresh guest preflight.
Inspect final answers and code statically, never execute model code on a credential-bearing host.
Each failed iteration records its cause and stop/recovery observations; only a justified new
revision/corpus may follow. A passing semantic prerequisite permits matched application/browser,
history/audit/admission, recovery, offline start and exact rollback checks before guarded release
promotion. This authorizes the bounded existing-guest release workflow, not bypassing gates or
automatic indefinite retries. Deployment uses the existing offline installer and retained exact
69c9260 rollback. A real unavailable prerequisite stops that operation, not independent code work.

### Original v1 baseline

The owner asks for stronger answers, coding, technical solutions and conversational context.
The completed 56-request comparison found technical overclaims in both 35B models, with and
without thinking. More RAM, a larger model or a longer context is not evidence of correctness.
Keep the live `69c9260`/Qwen3.5 standard profile and both thinking flags off during qualification.
Preserve the original scores and prior near-16K timeout; do not retune that corpus into a pass.
Legacy instructions also impose a word limit and prohibit procedures even for an explicit coding
request. An oversized recent exchange currently prevents any earlier usable history from selection.

## Requirements and acceptance criteria

- CAP-01: one versioned, trusted general-answer policy serves legacy and saved chat. Answer the
  actual question, honor exact requested formats, use natural EN/FA, stay brief for simple questions
  and provide useful code/technical explanation when requested, within unchanged output budgets.
- CAP-02: distinguish user reports, hypotheses and observations. Permission/configuration is not
  proof of connectivity; transport, TLS and application checks have different scopes. A completed
  request does not prove a loss-free network. Do not infer present status from stale facts or propose
  unrequested public exposure. No invented execution, citations, current advisories or secrets.
- CAP-03: coding guidance states necessary assumptions and provides a minimal complete example,
  error handling and meaningful tests when requested. Never claim code was run or tested. No model
  execution, arbitrary shell interface or infrastructure authority is introduced.
- CAP-04: select up to six complete eligible pairs, newest fitting first, from at most 100 stored
  exchanges within 12,000 serialized characters. Skip oversized pairs without clipping and retain
  chronological order. An internal omission marker tells the model not to invent missing referents;
  the existing user-visible omission metadata remains. The browser cannot set history or that marker.
- CAP-05: a fresh versioned EN/FA corpus exercises transport/TLS/DNS uncertainty, stale claims,
  safety, coding and recall. Freeze questions and review criteria before generation. Completion and
  exact formatting are structural gates, not factual certification. Keep semantic review separate.
- CAP-06: preserve evidence-only synthesis, provenance labels, deterministic authorization,
  owner/session isolation, atomic text-free audit, local assets, CPU-only/offline inference, 16K
  admission, one-active/two-queued, five-second queue and 120-second provider deadline.

## Non-goals and threats

No model import/switch, thinking enablement, resource enlargement, fine-tuning, cloud fallback,
external memory, new agent framework, retrieval, runtime downloads or UI rebranding. Prompts are
development guidance, not security controls or guarantees against hallucination. History, diagnostic
output and code are untrusted; missing history must not become fabricated context. General advice
remains `model_unverified`, never live evidence. Generated code is not automatically executed.

## Plan and tasks

1. Run the locked baseline and inspect current CI/locks/contracts. Preserve the clean primary checkout.
2. Implement the shared policy and bounded whole-pair history selection with source regression tests.
3. Freeze a new capability corpus and explicit semantic criteria; preserve older corpora unchanged.
4. Run lint/types, unit/API, browser fixtures, docs/artifact checks and PostgreSQL16/17 CI.
5. Stage exact source privately against the existing 35B profile, only within authorized qualification.
   Record final answers, latency and resource observations; reconcile native work after a timeout.
6. Review EN/FA semantics independently. A failure prevents promotion; retain the useful source repair
   without claiming deployment acceptance. Only passing prerequisites permit matched app/browser,
   history/audit/admission, WAN/cold-start and exact rollback qualification.

## Rollback and documentation

No schema migration or dependency change. Source rollback restores the previous policy/selector;
stored transcripts stay intact. Deployment, if later qualified, retains the previous immutable app
and AI releases with thinking off. Update paired guides, state, next task, traceability and the context
index with measured results. Historical failures remain visible.

## Later capability work — separately gated

Benchmark model alternatives only after a semantic prerequisite passes. Longer context requires
measured prefill/deadline recovery; local retrieval needs provenance and authorization benchmarks;
coding execution needs a separately reviewed credential-free sandbox. UI polish/accessibility must
preserve OCS branding and EN/FA parity. None of these is implied to be implemented by this increment.

Technical calibration references: [TCP specification](https://www.rfc-editor.org/rfc/rfc9293.html)
and [TLS 1.3 specification](https://www.rfc-editor.org/rfc/rfc8446.html). These support distinctions,
not the accuracy of any particular generated answer.
