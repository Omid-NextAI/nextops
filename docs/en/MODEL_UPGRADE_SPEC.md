# Bounded Qwen3.6 CPU model evaluation

[فارسی](../fa/MODEL_UPGRADE_SPEC.md) · [CPU guide](CPU_AI.md) · [Current release](../status/current-release.yaml)

## Problem and authorization

On 2026-10-03 the owner accepted the recommendation to evaluate Qwen3.6-35B-A3B before a larger
122B model. Current standard app/AI `69c9260` and the selected Qwen3.5-35B-A3B remain the rollback
baseline. Prior thinking semantics and real near-16K deadline failures remain failed; a new model
does not erase them. This is a bounded comparison, not training or production acceptance.

## Requirements and non-goals

- MU-01: preserve the CPU-only llama.cpp build, one active/two queued API boundary, 120-second
  provider deadline, credential isolation, deterministic policy, evidence and text-free audit.
- MU-02: import only an explicitly provisioned artifact with exact immutable source, size, SHA-256,
  license and template record. No runtime download, GPU, projector, MTP or cloud fallback.
- MU-03: verify fresh guest and backing-datastore capacity before server import. Unknown ESXi
  placement/snapshot/thin commitments are not available capacity. Do not resize or delete artifacts.
- MU-04: initially use an authenticated, loopback-only temporary candidate on port 8081 with
  read-only artifacts, bounded CPU/RAM/lifetime and explicit cleanup. Never change the serving
  release/model links, public flags or native port 8080 merely to run a probe.
- MU-05: use the existing saved-chat prompt builder, actual native template/tokenizer and final-only
  adapter. Qwen3.6 receives trusted `enable_thinking` and `preserve_thinking=false`; neither switch
  is controlled by user text. Never retain historical private reasoning.
- MU-06: compare fresh synthetic EN/FA questions without tuning against their observed answers.
  Review factual scope, uncertainty, injection, requested format, arithmetic and follow-up recall.
  HTTP/JSON success is not semantic acceptance; upstream scores do not qualify Persian NOC/SOC.
- MU-07: record actual input/output tokens, completion state, latency, CPU and memory. Compare
  equivalent thread/quota/context/output profiles and identify serving-load interference. Samples
  are not sustained throughput, host NUMA placement or a production p95 guarantee.
- MU-08: timeout stops the run. Reconcile actual native completion/slot release before any further
  call. No automatic generation retry or larger deadline to hide a failure.
- MU-09: only passing prerequisites permit matched app/API/browser/history/audit/admission tests,
  exact model/profile/source rollback and fresh offline startup/generation. The previous model's
  WAN/reboot results cannot be transferred to this artifact.

No UI redesign, branding change, new connector, arbitrary shell/tool execution, memory architecture,
database migration, ESXi topology change, 122B import, independent-recovery redesign or training.
Existing accepted ADRs remain applicable; no architectural replacement is proposed.

## Artifact and threat considerations

The [candidate manifest](../../deploy/inference/qwen3-6-35b-a3b-q4-k-m.candidate.json) pins
Bartowski `5c2410d71524f4f72b023ce8daf7a80528226d5f`, Q4_K_M, 22,285,080,192 bytes and SHA-256
`b46fedd33e0bfb0cae308aa3c158d0a4b2c4a1d2185a1ed6f093cdaf39064772`.
Its template hash is `e84f32a23fdda27689f868aa4a1a5621f41133e51a48d7f3efcbea2839574259`.
The inspected prefix declares `qwen35moe`, Apache-2.0 and the new reasoning-preservation option;
prefix inspection is not full-artifact integrity or runtime compatibility. The separately pinned
[official post-trained reference](https://huggingface.co/Qwen/Qwen3.6-35B-A3B/tree/995ad96eacd98c81ed38be0c5b274b04031597b0)
does not prove the quantizer's exact conversion source revision. Keep that lineage limitation.

Model text, saved history and monitoring descriptions remain untrusted. The model cannot authorize
an operation or manufacture a live observation. Only authorized connectors supply current facts.
Reports are protected outside Git and keep final synthetic answers plus reasoning length, not raw
reasoning, secrets or real monitoring text. Signed download URLs are not copied into reports.

## Implementation and acceptance tasks

1. Record owner authority, exact current identities, protected fallback and fresh read-only preflight.
2. Provision and independently verify the complete pinned file; inspect its metadata/template.
3. Run source fixtures for the new fixed alias, trusted switches, final-envelope validation,
   denied thinking and the candidate runner's serving-port exclusion.
4. After capacity verification, import without promotion and test CPU load/authentication/egress
   in the temporary unit. Stop on unsupported runtime/template, resource pressure or identity drift.
5. Run the versioned fourteen-case `technical` corpus in standard and thinking modes for both
   models under equivalent measured limits. Review the final answers separately; do not tune
   prompts and relabel repeated development questions as an independent pass.
6. If semantic/short-latency prerequisites pass, qualify genuine near-budget context/recall and
   timeout recovery. Keep not-run cases explicit when a prerequisite fails.
7. Only then package the exact source offline, qualify matched user-facing boundaries and guarded
   rollback/offline startup. Promotion requires evidence, not a manifest boolean or coding-agent verdict.

Rollback compatibility is a prerequisite, not cleanup: `69c9260` uses a literal model-ID contract
inside saved `AssistantResponse` and the database reader revalidates that JSON. A Qwen3.6 answer
cannot be read by that old parser. Before a user-facing switch, qualify an exact compatibility
release with the old serving model and both thinking flags off, then test preserved old/new-ID
transcripts across rollback to that release. Retain 69c9260 as historical recovery material but
do not claim it is a transcript-compatible rollback target after new-ID messages exist. Never
delete user chats or substitute the old model ID to conceal this incompatibility.

The opt-in [runner](../../scripts/qualify_thinking.py) supports `--scope technical`,
`--mode standard|thinking`, the two reviewed aliases and fixed loopback ports. Qwen3.6 is rejected
on serving port 8080 before report creation or credential reads. The temporary unit name used for
candidate resource samples is `nextops-model-candidate-qualification.service`. Reports are exclusive,
absolute, private and outside the checkout; source digest mismatch rejects the run. Exit 1 is failed
and exit 2 is partial, never acceptance. This private scheduler is not the serving API admission gate.

## Rollback and documentation

Before promotion, rollback is cleanup of only the owned temporary unit/listener: the serving model
is never replaced. If a later guarded trial is qualified, preserve and test the exact old source,
model, template, profile and credentials before touching links. Verify new EN/FA baseline answers
after rollback; do not blindly replay uncertain calls. Independent recovery stays owner-deferred,
not passed. Update the candidate manifest, paired CPU/testing guides, state, next task, traceability
and release status with actual outcomes; preserve all earlier failure records.
