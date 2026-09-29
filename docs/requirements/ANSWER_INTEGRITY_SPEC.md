# Answer integrity specification

Status: the focused app increment is deployed for controlled user testing on release
`nextops-0.1.0-01755d1`; earlier bounded live API/browser checks passed, but a fresh synthetic
semantic probe failed and the full held-out review remains unfinished. A source-only correction
is not yet deployed. Qualification remains revision-specific and is not a guarantee that model-only
text is always true.

## Problem

A small local language model can produce fluent text that is irrelevant, unsupported, stale or
wrong. Prompt instructions alone are not a security or truth boundary. NextOps must never present
model memory as live infrastructure evidence, must never imply that a read-only assistant performed
an operation, and must preserve stale/partial qualifiers even when generated prose fails.

## Requirements

- Application-owned generation purpose separates ordinary Q&A from evidence synthesis. Browser
  requests cannot choose provider identity, system instructions or synthesis purpose.
- Preserve the complete accepted question (up to 4,000 characters) in a separate bounded internal
  prompt contract (up to 12,000 characters); never silently discard the question's last instruction.
- The UI and application permit at most 384 output tokens per answer, respecting a lower requested
  limit. Incident input accepts up to 512 but the application clamps it to 384. Existing truncation
  rejection and one-active/two-queued scheduling remain mandatory.

- General mode remains useful for ordinary questions but is explicitly labelled as model-only and
  potentially incorrect.
- A general-mode question asking for current infrastructure state is redirected to a live evidence
  mode instead of being answered from model memory.
- Monitoring and incident responses label the nested assistant result with the same evidence mode
  as the enclosing response.
- Deterministic application code rejects generated operational-execution claims, unsupported
  root-cause assertions, missing source labels and omitted stale/partial qualifiers.
- A rejected monitoring or incident answer is replaced by a bilingual deterministic summary built
  only from typed evidence. Untrusted names are not copied into this fallback.
- A long general-mode prompt echo is replaced with a deterministic retry notice; short natural
  greetings such as `Hi` and `سلام` remain valid answers.
- For a greeting-only general question, reject a model reply that does not begin with a short
  greeting in the selected language or introduces unrequested operational subjects or telemetry.
  Show a localized greeting as a deterministic fallback, without implying live status was checked.
- A model completion stopped by the output-token limit is incomplete, even if it contains the
  expected source words. It must not receive `evidence_bounded`; a live route uses a clearly
  limited evidence-only fallback, and general mode asks for a narrower question.
- Live-mode fallback text must not pose as a complete answer to the user's specific question or
  duplicate the entire metric list already available in the evidence panel.
- Every result exposes a machine-readable integrity outcome and limitations. The browser explains
  the outcome without implying that automated checks prove factual correctness.
- The stored completion audit records the integrity outcome and limitations.
- Qualification remains local, CPU-only and offline-capable. No evaluator may silently call a
  remote model or telemetry service.
- Returning the user's prompt or instructions as the answer is a failed relevance case, even when
  the echoed text happens to contain required safety words.
- A question limited to filesystems must not receive unrelated CPU, service or event narration.
  Allowlisted mount capacity is not a list of system file names or contents. Until semantic model
  qualification, focused file/filesystem answers use typed deterministic text, keep partial markers
  and retain the complete authorized evidence and audit separately.
- Explicit English/Persian exclusions such as “do not include CPU” or “دادهٔ CPU را اضافه نکن”
  must not turn a file-only request into an overview. Mixed affirmative requests remain overview.
- A single-host Zabbix summary does not contain authorized host-inventory reachability states.
  Questions asking which hosts are available or unavailable must state this scope limitation,
  not infer host reachability from enabled status, active problems or generic metric counts.
- The browser initially shows only the requested filesystem evidence or an explicit notice that
  file names/content were not collected. Complete authorized evidence remains accessible through
  an explicit secondary reveal and in the audited response.

## Non-goals

- Claiming that any generative model is free of hallucinations.
- Fact-checking arbitrary general knowledge without an approved local source.
- Treating lexical gates, model confidence or fluent wording as proof.
- Granting execution authority, credentials or mutation capability to the model.
- Replacing exact evidence, provenance, audit or operator judgment with generated prose.

## Threat considerations

The controls address prompt injection in source-controlled text, fabricated current state,
fabricated execution, unsupported root cause, hidden evidence truncation, stale-data laundering and
contradictory response metadata. They fail closed to deterministic evidence summaries. They do not
establish the truth of arbitrary model-only answers, so the UI must preserve the verification
warning.

## Implementation and tasks

### Clarity repair and larger-model comparison — 2026-09-29

Problem: the prior shared system prompt treated ordinary chat as an evidence recap, public and
internal prompt bounds were conflated, and the UI/application reduced every answer to 128 tokens.
The repair does not rebuild the platform, train a foundation model, increase concurrency, add
retrieval, or grant execution. General explanations remain model-only; live answers retain the
stricter evidence-only prompt, assurance, provenance and audit.

Plan: retire the unrelated owner form; add typed internal purpose and prompt bounds; remove silent
question-tail clipping; raise the bounded answer budget; test forged controls, all three route
question tails, model-identity mismatches and bilingual behavior. Pin the official 14B Q4_K_M
artifact separately from the serving 8B record, verify its downloaded bytes, and compare both using
the same synthetic and held-out questions before any model selection. Larger weights alone do not
establish clarity, truth or acceptable CPU latency.

Deployment dependency: upgrade the inference API before the application because older inference
APIs reject the new `purpose` field. Old application calls omit it and retain evidence-synthesis
semantics. Roll back the application before the inference API; preserve compatible previous
immutable releases and the verified 8B model. No database migration, host firewall change, VM
reboot or destructive operation belongs to this repair. Model switching needs its own verified
runtime/path/identity tuple and measured comparison; it must not download at startup.

Acceptance: all accepted question tails reach synthesis; forged browser purpose/model fields fail;
both locales use the intended prompt; no false live/execution claims pass; results name the actual
configured model. Local fixtures, bounded loopback generation and serving-path qualification are
recorded separately in paired guides and current state. Exact-release offline/rollback tests and
full semantic review remain required, not inferred from lexical checks or a downloaded artifact.

1. Extend the assistant contract with consistent evidence mode, live-data marker, integrity status
   and bounded limitation codes.
2. Apply deterministic general, monitoring and incident answer assurance before persistence.
3. Add localized browser notices for unverified, evidence-bounded, fallback and redirect outcomes.
4. Expand the bilingual local evaluation corpus with relevance and no-live-evidence cases and add
   deterministic lexical safety gates while retaining manual semantic review.
5. Run source checks, PostgreSQL integration CI, live loopback model qualification and live browser/API
   acceptance for the exact deployed revision.
6. Allow bounded, literal per-case response expectations in the private live semantic corpus.
   Fail the capture command when a configured focus, integrity label, limitation or answer-fragment
   check fails, while retaining the complete private report and server-side logout attempt.
   These checks do not replace human semantic review or independently prove release identity.
7. Fail the capture command when any case lacks a configured expectation, even if all HTTP requests
   succeed. Flag an answer that only repeats a longer question, including when the repetition
   satisfies a configured answer fragment. Preserve the report and logout attempt in both cases.
   A zero exit means only that the configured automatic checks passed; release identity, factual
   relevance and human acceptance remain separate.
8. Bind successful authenticated answer responses to a bounded SHA-256 digest of the application
   package code and locally served assets. Derive the expected digest offline from the separately
   hash-verified candidate wheel and fail the private live capture when a response omits or differs
   from it. This is source-byte correlation, not a signature, host attestation, dependency/model
   identity, proof of semantic correctness, or permission to mark an exact-release gate passed.

## Acceptance criteria

- `Hi` and `سلام` remain short greetings and do not introduce Zabbix state.
- Unrelated model replies to greeting-only questions are replaced in English and Persian; a short
  relevant model greeting remains model-labelled and a genuine status question is not mistaken for
  a greeting-only request.
- General mode does not answer a current infrastructure-status question as fact.
- A generated claim that NextOps restarted, fixed, deployed or changed infrastructure is never
  returned to the user.
- Live responses carry `live_zabbix` or `live_zabbix_linux` in both enclosing and nested metadata.
- Stale or partial evidence cannot be presented without its qualifier; failure produces the
  deterministic fallback.
- Injected metric/problem names cannot cause instructions or secret disclosure and are absent from
  the deterministic fallback.
- Audit, evidence hash/reference and read-only authorization remain intact.
- The eight-case English/Persian loopback corpus passes deterministic checks; a human reviewer still
  inspects meaning and language quality.
- Prompt echo fails automatically and semantic review must reject an answer that merely restates the
  question.
- Truncated English and Persian completions fail closed before persistence, while the exact typed
  evidence, provenance and audit linkage remain available.

## Tests and evidence

Unit/API tests cover contract consistency, scope redirect, false execution claims, greeting-only
relevance, evidence-bounded acceptance, stale/partial fallback and prompt-injection containment.
The existing private live
evaluation report remains outside Git because deployment evidence may contain operational metadata.
Passing tests qualify only the named cases and revision.

## Rollback

Retain the prior immutable application and inference releases. Roll back each `current` link
independently, restart the affected unit, and verify authentication, readiness and the exact `Hi`
relevance case. A rollback also removes the new integrity metadata and must therefore be recorded as
a security-significant downgrade.

## Documentation

The paired [English](../en/AI_INTEGRITY.md) and [Persian](../fa/AI_INTEGRITY.md) guides describe the
operator-visible behavior. Project state and the release manifest record only observed deployment
and acceptance results.
