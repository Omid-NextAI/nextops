# AI answer integrity

**Status: controlled user testing; named regressions repaired, full semantic acceptance partial.** NextOps cannot
guarantee that a generative model will never be wrong. It instead prevents the most dangerous
category error: presenting unsupported model text as live operational fact.

## Larger-model comparison — 2026-09-29

Fourteen matched bilingual cases completed at 384 tokens on both 8B and 14B. Semantic review
rejected 14B for incorrect Persian RAM and arithmetic answers and missing/weakened evidence
qualifiers. 8B also failed some source/stale cases. These are development observations, not
independent held-out acceptance. No model gained a tool or credential. The serving 8B remains
unchanged; pinned 32B provisioning and source-only identity support are the next step. See
[CPU_AI](CPU_AI.md); larger weights do not waive deterministic safeguards.

## Clarity repair — 2026-09-29

The corrected `c4351fd` application/inference API is now live. Twelve fresh bilingual API cases
passed the named greeting, knowledge, unknown-current-state, file-focus and host-scope expectations
with matching code digests. Browser review covered five general cases and two filesystem cases
in separate fresh contexts. App/API rollback and re-promotion worked. This fixes the observed
regressions, not arbitrary correctness. Full held-out quality, current-release WAN/VM cold start
and larger-model qualification remain open; the selected model is still 8B.

The dated records below preserve what was observed before this correction.

The first guarded promotion of source `089e3ad` exposed an HTTP contract gap: the gateway sent
`purpose`, but the inference endpoint rejected it. Six requests failed with dependency errors,
so the operator restored the previous application and then the previous inference API. Fresh
login, generation and logout worked after rollback. The corrected endpoint explicitly accepts
only the two trusted synthesis purposes and defaults legacy calls to evidence synthesis. New
tests traverse gateway serialization, authenticated HTTP validation, scheduler and provider
prompt selection in both languages; only the model completion is synthetic. This incident is
retained as a failed promotion, not a live acceptance.

The 14B artifact was size/hash-verified and imported into a protected candidate directory without
changing the serving model. Eight serial 192-token comparisons found a truncated Persian RAM
answer and source/wording weaknesses. A four-case follow-up with the actual general prompt and
384-token budget completed in about 13–41 seconds. These are bounded comparisons, not a complete
bilingual or offline qualification; the 8B model remains selected.

The development candidate separates ordinary Q&A from the evidence-only synthesizer prompt,
preserves all 4,000 accepted question characters instead of clipping at 800/1,200, and raises the
UI/application answer ceiling from 128 to 384 tokens without expanding concurrency. A typed
12,000-character internal prompt is distinct from the public question. Clients cannot select a
provider or override synthesis purpose. Truncated answers still fail closed, and the exact serving
release's failed semantic gate is not repaired by source tests alone.

The official 14B Q4_K_M candidate has a separate pinned artifact record. Its model identity is
allowlisted explicitly rather than reported as 8B. Downloads are provisioning-only; no runtime
resolver, remote model fallback or new target credential is introduced. Compare measured bilingual
answers and CPU latency before choosing the larger model. Deployment must update inference before
the application, and rollback must reverse that order. See the [bounded specification](../requirements/ANSWER_INTEGRITY_SPEC.md).

On 2026-09-26, six private-path synthetic questions found that the serving app misclassified two
English/Persian file-only requests as `overview` and gave two multi-host availability questions
generic Zabbix counts despite having no host-inventory reachability data. A source-only candidate
now treats explicit exclusions as exclusions, states the missing host-inventory scope, and makes
focused evidence the default browser detail. Full authorized evidence remains available on
explicit expansion and in the audited API response. API/browser fixtures pass; this candidate is
not deployed or live-qualified. The serving release's expanded semantic gate is `failed`.

A further source-only guard now checks greeting-only general questions. If the model replies with
unrelated text or introduces operational status or telemetry, the application shows a short local
greeting instead and labels it `deterministic_fallback`; a relevant short model greeting remains
`model_unverified`. The browser uses a general-mode notice that does not imply evidence was
retrieved. API and local browser fixture tests pass, but this change is not deployed or live-qualified and does not
repair the serving release's failed semantic gate. It is a narrow intent check, not a general
factual or relevance verifier.

## Answer-completion correction and controlled promotion — 2026-09-26

A fresh live browser review exposed a 128-token incident answer that appeared unfinished while the
interface displayed the `evidence_bounded` notice. A controlled repetition of the same question
returned `finish_reason=length` and `deterministic_fallback`; this confirms output truncation can
occur while the previous label varied with the model's wording. The existing source checker
required source and partial-evidence words but did not inspect the model's `finish_reason`.
Application release `nextops-0.1.0-01755d1` now rejects `length`-terminated completions and long
question echoes on live routes,
replaces them with an evidence-only fallback that states it may not answer the full question, and
asks the model to answer the actual question first in short plain text. The browser notice now
states that lexical/source checks do not certify factual correctness or relevance. Focused
API/browser-fixture tests and bounded live release checks pass: fresh English/Persian greetings,
current Zabbix evidence, file questions, provenance, audit and a fresh browser. The owner's exact
prompt/response pair and full held-out bilingual semantic corpus remain **not run**; automated
checks do not prove every answer relevant or true.

Fine-tuning is not a substitute for current Zabbix evidence or a release gate based on a single
example. A versioned set of real, redacted question/answer failures and held-out Persian/English
cases is needed before comparing prompt, output-budget, model or fine-tuning changes.

## What users see

General assistant mode has no live evidence. Its output is labelled `model_unverified`, and the UI
asks users to verify important facts. Questions about current infrastructure state are not answered
from model memory; the response directs the user to Live monitoring or Incident investigation.

Live modes return the exact typed evidence, provenance, durable run, SHA-256 evidence reference and
audit identifier beside the answer. The nested assistant metadata matches the outer evidence mode.
The UI distinguishes these outcomes:

| Outcome | Meaning |
|---|---|
| `model_unverified` | Model-only text; no current evidence and no factual guarantee |
| `scope_redirect` | The question requires live evidence and was not answered from memory |
| `evidence_bounded` | Mandatory source/freshness/partial/read-only checks passed; exact evidence still governs |
| `deterministic_fallback` | Generated wording failed a mandatory check and was replaced with a safe deterministic response |
| `deterministic_focus` | A file/filesystem question receives a source-built answer instead of unverified generated detail |

The deployed focused-answer increment distinguishes allowlisted filesystem capacity from actual
system-file names and contents. Its prompt excludes unrelated incident fields, and application code
builds the displayed answer from typed Linux observations or states that file listing is unavailable.
It preserves partial-evidence disclosure, authorization, complete evidence, provenance and audit.
The machine-readable `file_listing_unavailable` limitation prevents a generic live-evidence prompt
from implying that another mode can show file contents. This does not train the model or qualify
arbitrary generated answers. Live acceptance of this release is bounded to the named checks; full
semantic review remains outstanding.

## Deterministic boundary

Before a generated answer is stored or shown, application code checks for false execution claims,
unsupported root-cause assertions, missing evidence-source labels and omitted stale/partial
qualifiers. A failure never retries with a less restrictive prompt. It returns a localized template
derived from the validated evidence contract. Source-controlled names are excluded from that
fallback so a hostile metric or problem name cannot become an instruction.

A long answer that merely repeats the general question is also replaced with a localized retry
notice. This does not reject short natural greeting replies.

These checks are deliberately narrow. They do not certify every sentence as true, judge arbitrary
general knowledge or replace review of exact evidence. NextOps still performs no infrastructure
mutation and the model receives no target credential.

## Qualification

The local evaluation corpus covers English and Persian evidence preservation, refusal to claim
execution, greeting relevance and refusal to invent current health without live evidence. The
harness checks authentication, readiness, required/forbidden language and script presence while
rejecting prompt echo and keeping semantic review explicit. It uses only the protected loopback
inference API and writes its report to a private file.

The normative requirements, acceptance cases and rollback are in the
[answer integrity specification](../requirements/ANSWER_INTEGRITY_SPEC.md).

## Controlled acceptance — 2026-09-26

At that checkpoint, application release `nextops-0.1.0-2397581` and inference API release
`nextops-0.1.0-fd3c353` were active. Their hosted workflow passed quality/unit, PostgreSQL 16,
PostgreSQL 17, browser fixture and secret-scan jobs. The final private loopback report passed all
eight automated cases; engineering semantic review accepted every English and Persian answer,
including direct greetings, explicit unknown current state, preserved timeout evidence and no
claim of execution. The report still sets `acceptance_claimed=false` because this is a bounded
quality gate, not production acceptance.

A short-lived server-created test session then exercised the deployed application. `Hi` returned no
Zabbix content, the current-status question returned `scope_redirect`, live monitoring returned
`evidence_bounded`, and the composite incident route returned `deterministic_fallback` with exact
evidence metadata. The session was revoked immediately. A subsequent serial reboot of Zabbix,
connector, AI and application loaded kernel `6.8.0-142`; every guest returned `running`, zero failed
units and no reboot marker. No recovery or SMTP-delivery claim is included.
