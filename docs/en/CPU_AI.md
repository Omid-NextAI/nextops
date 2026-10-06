# Local CPU-only AI and capacity planning

## Retained Qwen 3.8 diagnostic and bounded repair — 2026-10-06

The first locale-native standard trial ended at 09:53 UTC with **12 main-reviewed passes/four
failures**: an unverified Persian networking topology, missing authorized scope in both stale
answers, and the final Persian hypothesis timeout. Fifteen finals were retained; both coding
answers passed twelve finite AST checks, never executed. The protected report's SHA-256 is
`3b9574281efb81fe07ac0937ef1dde9f7a3682275adb73d0bd80c037f30de1ab`.
Cleanup and a separate ready-idle baseline reread passed. Exact `5500a24` passed five CI jobs,
not model acceptance. A distinct compact-policy diagnostic is watched; it explicitly preserves
authorized scope/full timestamps and asks for short complete parts. Frozen questions, sampling,
32-thread CPU profile, 16K/output/deadline/security controls remain. Its result is pending;
independent/application/thinking/context/WAN/rollback gates and serving 35B remain unchanged.

## Current priority: Qwen 3.8, even at lower parameter count — 2026-10-06

The owner's clarified goal prioritizes actual **3.8**, not a larger relabelled 3.5. Resume the
complete pinned 27B Q5. Candidate-only general instructions now use native EN/FA wording and
budget-aware concision while preserving type-first coding, full provenance and uncertainty.
They do not inspect question keywords or insert expected fixture answers. Serving 3.5 and
evidence synthesis remain unchanged. This is source work, not training or a model-quality pass.
Local checks passed **1315 tests**, two POSIX skips/126 deselected; lint/format and Linux types
passed. Frozen questions, sampling, context, output/deadline and thinking denial are unchanged.
The separate main-only native diagnostic requires actual final/semantic/deadline/cleanup review;
independent, matched application, thinking/context, WAN and rollback gates are not inferred.
See the [updated plan](../requirements/QWEN38_QUALIFICATION_SPEC.md).

## Previous transfer checkpoint — historical

Checkpoint — **2026-10-06, 08:25 UTC**: three additional finite transfers failed with
zero imports and actual stopped/closed/unchanged-baseline reconciliation passed. Totals remain
282 ranges/75685225248 bytes, 14744229504 bytes outstanding, one whole shard verified.
Small discarded HTTPS probes passed but the next full-range transfer failed; require stronger
route/profile evidence or a reviewed alternative, not identical retries or deadline widening.
Exact `e95618e` passed five [CI jobs](https://github.com/Omid-NextAI/nextops/actions/runs/37432024392).
The owner selected themselves for independent V3 review. A private bilingual guide, eight
isolated checks and a blank report template are ready; actual owner review remains not_run.
No V3 host use, new selection or thinking enablement; live35B stays. Full-set/native/model/
privacy/context/app/operational/rollback gates remain separate. See the [paired record](../requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md).

## Earlier transfer checkpoint — historical

Checkpoint — **2026-10-06, 07:45 UTC**: 282 ranges/75685225248 bytes verified as transported;
14744229504 remain and only one whole upstream shard is verified. Two more reviewed windows
passed actual receipts/exit0/pre-import verification. Two distinct failed windows imported
zero ranges, retaining all bodies; the later one had two complete and two partial HTTP206
responses. Actual terminal failures, closed handles, reaped curl and unchanged ready-idle
reconciliation were recorded, without partial promotion or timeout widening. Exact `5bf461c`
passed five [CI jobs](https://github.com/Omid-NextAI/nextops/actions/runs/37426920560).
Official licence-page rereading is not legal approval or a new artifact pin. Independent
V3/full-set/native/model/thinking/privacy/context/app/operational/rollback gates stay open;
no unattended trial or new selection. The alternative is correctly Apache Qwen3.5-122B-A10B;
live35B/public thinking-off remain unchanged. See the [paired record](../requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md).

## Earlier transport checkpoint — historical

Transport checkpoint — **2026-10-06, 06:56 UTC**: 274 ranges/73537741600 bytes verified as
transported; 16891713152 remain and only one whole upstream shard is verified. Four more
reviewed V7 windows passed actual receipt/exit0/pre-import numeric/identity/hash/retention/
cleanup/baseline checks; the slow last window stayed within fixed limits. Exact `940b84d`
passed five [CI jobs](https://github.com/Omid-NextAI/nextops/actions/runs/37423271410).
Independent review/full-set/native/model/thinking/privacy/context/app/operational/rollback
gates remain open. No new model selection or unattended trial; the Apache 122B alternative
is correctly 3.5, while the live 35B model and public thinking-off remain unchanged.

## Earlier transport/CI checkpoint — historical

Follow-up — **2026-10-06, 06:18 UTC**: 258 ranges/69242774304 bytes verified as transported;
21186680448 remain and only one whole upstream shard is verified. Another actual bounded V7
window passed receipt/exit0/numeric/identity/hash/retention/cleanup/baseline checks. Exact
`906a081` passed five [CI jobs](https://github.com/Omid-NextAI/nextops/actions/runs/37422445456).
Independent review/full-set/model/thinking/privacy/context/operational gates below remain open;
no V3 host use, model selection or unattended trial. Live35B/public thinking-off are unchanged.

## Earlier provisioning/handoff checkpoint — historical

Provisioning/review handoff — **2026-10-06, 06:10 UTC**: 254 ranges/68169032480 bytes transferred
with numeric HTTP206/exit0 and pre-import identity/hash/retention/stop/baseline checks;
22260422272 bytes remain and one whole shard is verified. A private handoff binds fourteen
freshly rehashed V3 source/checker files, isolated review commands and failure criteria; JSON/pin
validation passed, not independent review. Exact `8b94d88` passed five
[CI jobs](https://github.com/Omid-NextAI/nextops/actions/runs/37419756842). Quota-blocked independent
review, full-set/native/standard/thinking/privacy/context/app/operational/rollback gates remain.
No V3 host execution or model selection; live35B stays and the 122B alternative is correctly 3.5.

## Earlier transport/regression checkpoint — historical

Transport follow-up — **2026-10-06, 05:33 UTC**: 242 ranges/64947807008 bytes verified,
25481647744 remain, one whole shard verified. Three more bounded windows passed actual desktop
receipt/exit0/pre-import numeric/hash/retention/stop/baseline checks. Exact `4e78144` passed five
[CI jobs](https://github.com/Omid-NextAI/nextops/actions/runs/37417547944) and 61 targeted local
regression tests (5.12s); neither is native model acceptance. Independent reviews and model/
thinking/privacy/context/app/operational/rollback gates below remain open; live35B stays.

## Earlier directory-durability checkpoint — historical

Latest checkpoint — **2026-10-06, 05:10 UTC; provisioning/local repair only**: 230 verified
transport ranges/61726581536 bytes; 28702873216 remain and one whole shard is verified. Three
further windows passed actual desktop receipt/exit/retention/closed-handle/ready-idle checks.
Frozen native V2 lacks directory-entry fsync; distinct V3 adds it under retained identity-checked
locks and passed 1869 main assertions/Bash syntax. Matching trio installer/controller passed
227/1022; external read-only reconciliation/controller passed 18403/842 main assertions. Expanded
mocks caught/repaired a bytearray process-token bug before host use; the large count includes
per-block scan checks, not independent tests. Independent review remains not run after subagent
usage-limit errors; no V3 host installation/execution. Exact `4bb295d` passed five
[CI jobs](https://github.com/Omid-NextAI/nextops/actions/runs/37414641936).
Apache Qwen3.5-122B-A10B Q5 is still unselected, not 3.8 or accepted maximum context/thinking.
Preserve completed earlier work/failures and live35B/public thinking-off. See the
[paired record](../requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md).

## Earlier installer-controller checkpoint — historical

Latest checkpoint — **2026-10-06, 04:36 UTC; provisioning/local checks only**: 218 transport
ranges/58505356064 bytes verified, 31924098688 bytes remain; one whole shard verified. Four
additional windows passed actual desktop receipt/exit and retained-body/closed-handle/unchanged
ready-idle checks. Native-trio installer/controller passed 227/1022 main-only Python/PowerShell
checks; independent review and external execution/reconciliation remain open. Publication
installer V3 also awaits independent review. Exact `2838b2a` passed five
[CI jobs](https://github.com/Omid-NextAI/nextops/actions/runs/37413048626).
This is the Apache Qwen3.5-122B-A10B Q5 alternative, not accepted 3.8 or an accepted maximum
context/thinking profile. Full-shard/standard/privacy/context/app/operational/rollback gates
remain; live35B/public thinking-off and earlier completed work/failures are preserved.
See the [paired record](../requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md).

## Earlier execution-tool checkpoint — historical

Latest checkpoint — **2026-10-06, 04:12 UTC; provisioning/local repair only**: 202 verified
transport ranges/54210388768 bytes; 36219065984 remain and one whole upstream shard is verified.
Native V2's 1478 main/independent checks and publication execution V2's 1646 each-side checks
passed, not host execution. Pinned actual template/license bytes match reviewed hashes; native
privacy/token-array/context acceptance is open. Publication installer V2 was subsequently rejected
for close/receipt failure gaps. Distinct V3 passed 256/989 main-only Python/PowerShell checks;
the repaired native installer draft passed 227 main-only checks. Required unfinished controller/
independent reviews are not credited; authorized subagents stopped on usage limits. Exact
`2847651` passed five [CI jobs](https://github.com/Omid-NextAI/nextops/actions/runs/37403305543).
Finish reviewed transport and all-file verification before standard/thinking/privacy/context/
matched operational gates. Successful metadata installation/history, staged ca1, live35B/public
thinking-off and unaccepted advertised context remain unchanged. See the [paired record](../requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md).

## Earlier preparation checkpoint — historical

Latest checkpoint — **2026-10-06, 02:11 UTC; provisioning only**: transport reached
194 ranges/52062905120 bytes; 38366549632 remain and only the first whole shard is verified.
The latest four-request window passed in 461282 ms; the earlier fast/slow windows are not a
proven general speedup. Review rejected two preparation-tool failure boundaries; the distinct
complete-inspector V2 passed 6278 main/independent pure checks and its fixed installer passed
1020 each-side checks plus actual 238-ms installation/owned-stop/hash/receipt checks. Full-set
inspection has not run. Publication V2 passed 3035 each-side pure checks, not publication;
native lock-identity/cleanup repair is unfinished. Exact `9375d49` passed five
[CI jobs](https://github.com/Omid-NextAI/nextops/actions/runs/37400813523).
Preserve rejected tools, original root-only files, staged-not-installed ca1 and live 35B/public
thinking-off. Complete transport/full-set/template/standard semantics before separate thinking,
privacy, measured context and matched operational gates. Advertised 262144 is not accepted.

## Earlier expanded metadata checkpoint — historical

Latest checkpoint — **2026-10-06, 01:36 UTC; provisioning only**: 178 verified transport ranges/
47767937824 bytes, with 42661516928 remaining; only one whole upstream shard is verified.
The distinct four-request parallel window passed in 463594 ms of curl time, not a proven
general speedup. Separately installed expanded metadata tools passed actual first-file inspection
in 87843 ms and independent protected-result reread/owned cleanup/live-baseline checks.
Actual `qwen35moe` fields include 256 experts/8 used, 32 attention heads/2 KV heads and
EOS/padding IDs 248046/248044. Missing scalars remain absent; token arrays and template-control
semantics are unreviewed. Advertised 262144 context is not accepted. Exact `495b704` passed five
[CI jobs](https://github.com/Omid-NextAI/nextops/actions/runs/37397504800); ca1 remains staged,
not installed. Finish transport, all-shard verification and immutable service-readable copies
before native standard tests, then separate thinking/privacy/context and operational acceptance.
Original two-link root-only files, live 35B/public thinking-off and failed trials are preserved.

## Earlier staging checkpoint — historical

Latest checkpoint — **2026-10-06, following the 00:57 UTC window**: 166 verified ranges/
44546712352 canonical bytes; 45882742400 still require transport. The distinct wheel-only repair
passed 1303 main/independent checks and protected ca1 source/wheel staging, with unchanged ACLs,
owned stop and ready-idle baseline. Staging is not installation or model acceptance. Exact
`f7d0b35` passed all five [CI jobs](https://github.com/Omid-NextAI/nextops/actions/runs/37396025687).
Only one complete upstream shard is verified; live 35B/public thinking-off remain unchanged.
Expanded actual metadata and complete-set/native/semantic/thinking/context gates remain open.

## Earlier metadata checkpoint — historical

Checkpoint — **2026-10-06, 00:27 UTC; first-file metadata, not model acceptance**:
protected full-hash/metadata inspection passed in 89798 ms, with independent read-only stopped/
baseline reconciliation. Actual `qwen35moe`, 49 blocks, 3072 embedding dimensions, split count 3,
first-file tensor count 392 and template hash were recorded. Aggregate 899 tensors and 262144
context tokens are advertised only. Expert/special-token fields and template branches are not
verified by this reader. Protected serial S-drive transfer reached 158 ranges/42399228704 bytes,
leaving 48030226048 transport bytes. Only one full shard is upstream-hash verified. Finish
transport before remaining assembly to preserve the importer free-space guard. `861bf7d` CI
passed all five jobs. The source planner separates implemented registration/hard-standard/
model-label capabilities from uncompleted runtime/qualified-thinking work; 63 focused tests
passed. None of this enables thinking, selects a model or accepts advertised context. Full-set,
native semantics, privacy and matched operational gates remain unfinished; live 35B is unchanged.
See the [paired record](../requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md).

Subsequently, 00:44 UTC transport reached 162 ranges/43472970528 bytes, with 46956484224
missing. Source-only bounded MoE/special-token inspection passed 1098 unit tests/two POSIX
skips; independent focused reader tests passed 211. The installed reader stays unchanged.
The ca1 stager failed local preflight on the fixed packaged wheel's OWNER RIGHTS ACL, before
host access. Preserve that failure/original ACL and review a distinct exact-wheel boundary;
never relax the generic path validator or mistake source checks for model acceptance.

## Earlier first-shard checkpoint — historical

Historical checkpoint — **2026-10-06; not model acceptance**: the first of three Apache
Qwen3.5-122B-A10B Q5 shards is complete, **39714874144 bytes**, and matches upstream SHA
`d7d5aa3ef843ba3fe5ee27cdaebe17abd8a6a8a03a5c236db9bfe2fc6b88be2e`.
The protected assembler verified all 148 ranges, completed in 480111 ms and reconciled owned
stop/unchanged live readiness. Two shards/**50714580608 bytes** remain. A three-range download
after first-shard transport completed but before assembly timed out; zero ranges were accepted
and short bodies remain preserved.
The distinct prefix/suffix continuation then completed at 23:56:08 UTC, adding one verified
268435456-byte transport range with protected receipts/cleanup and unchanged readiness:
149 ranges/39983309600 bytes, with 50446145152 transport bytes still missing. All local bodies
are retained; there is still only one complete upstream-shard result.
The ca1 source archive/wheel passed offline packaging/parity in 23046 ms, with all five exact
`ca1da27` CI jobs successful, including the distinct 88-test browser rerun. Packaging is not
upload, deployment, signature or WAN acceptance. Actual GGUF/load, standard semantics,
final-only thinking/privacy, measured context and matched app/operational gates are still
unrun for 122B. Do not claim its advertised context or larger parameter count is accepted.
Live 35B/public thinking-off and failed Qwen3.8 evidence remain unchanged. See the
[paired record](../requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md).

## Earlier provisioning checkpoints — historical

Current provisioning checkpoint — **2026-10-06**: exact `293164e` passed all five CI jobs in
[run 37378458739](https://github.com/Omid-NextAI/nextops/actions/runs/37378458739). The reviewed
122B importer is installed root-owned/mode `0400` with exact source parity; 825 main/independent
definition checks passed. Initial window `resume-20261006-639268346254710321` failed at
`remote_begin`, before any download/root start/result record. Read-only reconciliation confirmed
stopped transport/absent open handles and unchanged 35B PIDs/restarts/ready-idle state. Isolated
SSH runner tests identified missing `ProgramData`; the distinct v2 desktop helper passed 406
preparation checks and read-only reconciliation. Window `resume-20261006-639268352065353249`
completed one 268435456-byte range, index 133; protected receipts, verified-duplicate cleanup and
unchanged baseline passed. The subsequent v2 window `resume-20261006-639268355159703524`
completed indexes 134–137, each 268435456 bytes, with root finish/stopped/baseline checks passed.
Current canonical data total 138 ranges/37044092928 bytes, not a full-shard result; the 134-range
snapshot is history. V3 passed 430 local preparation checks but first window
`resume-20261006-639268362479556681` failed at `finite_download`, exit 1/zero accepted ranges;
root stopped/baseline reconciliation was reported true. Canonical data stayed unchanged,
failed bodies remain retained, and no transfer-speed gain or blind retry is accepted.
Distinct serial window `resume-20261006-639268366509946555` completed indexes 138–140, each
268435456 bytes, at 22:40:16 UTC with root finish/stopped/baseline checks passed. Latest
canonical data total **141 ranges/37849399296 bytes**; seven first-shard ranges remain, not a
complete-shard result. No later range or transfer-performance cause is claimed.
The one-shard assembler remains local-only/unuploaded/unrun despite
671 pure/mock checks and 414 independent checks. Its prepared desktop wrapper passed 387 peer
mocks; exact final execution review and actual assembly remain separate and unrun.
Typed 122B registration is implemented/tested, not deployed or accepted. Main's source suite
passed 1094 tests/two POSIX skips/126 deselected in 25.99 seconds; lint/format/Linux-target types
passed, with one existing AnyIO warning retained. A broad directory secret scan included ignored
trees and reported 18 findings, not a pass. Main's separate new staged-change Gitleaks check
passed exit 0; keep its limited scope, the protected broad-scan report and earlier CI distinct.
This is an Apache
Qwen3.5-122B-A10B alternative, not a Qwen3.8 rename. Preserve failed records, live 35B and public
thinking-off; artifact, model, context and matched app/offline/rollback gates remain separate.
See the [paired record](../requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md).

## Prior completed native comparison — historical

Latest completed comparison: the exact-`b94a84c` Q5 no-BLAS NUMA trial ended failed at
**21:36:41.463473 UTC on 2026-10-05**. Fourteen stopped finals returned; English hypothesis
timed out at **120001 ms**, Persian hypothesis was not run. Main/independent review agree on
**nine passes/six failures/one not run**. Unsupported network topology, FA coding type guards
and missing stale-evidence date/collection/scope remain failures. Load/controller: 6002/776965 ms.
598 samples observed maximum RSS/PSS **21116248/21112229 KiB**, minimum sampled available memory
**240639852 KiB** (controller minimum **240231444 KiB**), no swap or nonzero memory events,
zero recorded memory-PSI averages and ready/idle baseline. Seven project-library/no-BLAS checks passed in their recorded
scope; fourteen available NUMA postchecks recorded 37 tasks and three guest-node/broad masks,
not physical placement, cache relocation, warning absence, cause or optimum. Observed generation
around 1.18–1.20 tokens/second is not an accepted improvement or TTFT; a changed FA stale-answer
length is not a quality gain. Owned cleanup passed; live 35B/public thinking-off remain unchanged.
Exact `7f14ba1` CI passed all five jobs in
[run 37376324673](https://github.com/Omid-NextAI/nextops/actions/runs/37376324673).
The separate Apache Qwen3.5-122B-A10B resumption helpers are local/in review, not uploaded/run at
this checkpoint; freshly rehash retained ranges and verify storage budgets before any authorized
import window. Thinking/context and matched app/WAN/rollback remain separate. See the
[paired record](../requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md).

## Prior no-BLAS checkpoints — historical

The distinct `b94a84c` no-BLAS standard retest ended failed at 21:14:22 UTC on 2026-10-05:
eleven stopped finals, Persian stale/partial deadline failure at 120234 ms, four cases not run.
Main/independent review agree on seven passes/five failures/four not run. Source/date/collection
time are now preserved in EN evidence, but explicit authorized scope is still omitted. Both network
answers and FA coding fail. Load/controller took 6621/567205 ms; owned cleanup and unchanged live
35B readiness passed. Exact `f9a4a83` CI passed all five jobs. A distinct reviewed NUMA comparison
started at 21:23:44 UTC, loaded in 6002 ms and is in progress, not an optimum or acceptance;
no live model, context or thinking setting changed.

The earlier `f6cff8f` no-BLAS standard trial ended failed at 20:55:02 UTC: fourteen finals,
English hypothesis timeout at 120003 ms, Persian hypothesis not run. Protected packaging/static
closure/tree checks and actual seven-library/no-BLAS maps passed within their stated scope; owned
cleanup and unchanged live baseline passed. First EN/FA native prefill took 22428.166/19713.992 ms
for 359/369 uncached tokens; later observed generation was about 1.18–1.20 tokens/second. Warm-cache,
build and instrumentation differences limit attribution; these are not TTFT, optimum, thinking or
near-context acceptance. Main/independent review agree on nine passes/six failures/one not run; no
live model/profile changed. Preserve that dated failure separately from the retest above.

Fresh build003 completed offline in 130332 ms at 20:20:41 UTC on 2026-10-05, with unchanged
serving baseline and reconciled cleanup. All eight read-only-inspected ELF outputs have literal
`$ORIGIN` RUNPATHs; build002's temporary absolute/empty paths remain rejected. Build output is not
model acceptance: protected packaging, system-library closure and actual execution are separate.

## Candidate runtime identity — explicit, read-only and not acceptance

The default `scripts/check_native_runtime_bundle.py` contract still requires the original pinned
binary and v1.0 inventory. A separately reviewed runtime uses a distinct v1.1 inventory under
`deploy/inference/native-runtime-candidate-bundle.schema.json` and an independently supplied
`--candidate-binary-sha256`, in addition to the independently trusted inventory digest. Neither
anchor may be inferred from untrusted inventory contents. Both declarations bind to the external
binary digest; the same protected commit-bearing root, no-follow traversal, exact tree, metadata
stability and size/count bounds apply. No execution, installation, selection or approval option
exists. The original schema is unchanged. 176 focused tests and 1053 source tests passed (two
POSIX skips); synthetic filesystem coverage is not actual candidate linkage or runtime acceptance.
Build provenance, ELF/system closure, effective loaded mappings, CPU performance, answer quality,
thinking/privacy, context, application/offline/rollback gates remain separate. No serving model changed.

## Passive-wait result and next runtime experiment — 2026-10-05

The distinct exact-`f6cff8f` Q5 trial used passive OpenMP waiting with verified process settings.
EN/FA format finals took 73373/77074 ms; English networking timed out at 120002 ms without a
final, leaving thirteen cases unrun. No improvement or standard approval follows. Cleanup and
unchanged live baseline passed. 227 completed samples observed RSS/PSS maxima 22126412/22116125
KiB and no swap/OOM; cgroup peak is not full mapped-memory accounting. Numeric CPU deltas are
non-atomic, not cause or downtime. Added instrumentation/warm-cache conditions limit comparisons.
Exact `b94a84c` CI passed five jobs and offline package/staging code digests matched; generated
answers were unrun at that prior checkpoint. The separate CPU no-BLAS build hypothesis keeps the same pinned source,
protects serving/rollback artifacts and disables build downloads. It is not accepted or selected.
See the [paired record](../requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md).

## Detailed-answer source follow-up — not deployed

The generic detailed prompt explicitly retains source/observation/collection/scope and stale/partial
limits, distinguishes reported from independently verified observations, and requires type checks
before value operations. It does not contain fixture answers or change the frozen corpus, short/
evidence prompts, template flags, context/output/deadlines or policy. Captured-payload tests now
snapshot nested values and detect later mutation, rather than comparing shared mutable references.
118 focused and 967 source tests passed (two POSIX skips); actual generated-answer improvement
is not yet accepted. The historical passive-wait comparison keeps exact `f6cff8f`; this later source needs its own
pinned semantic/privacy/context/app/offline/rollback qualification before deployment or selection.

## Distinct Q5 physical-batch512 result — 2026-10-05

The separate exact-`f6cff8f` standard trial loaded in 7856 ms at 32 threads/16K/384 output/
120 seconds with thinking off. Eleven final answers returned; Persian stale/partial evidence
timed out at 120002 ms, leaving four cases unrun. Main and independent review recorded six passes,
six failures and four not run. Both coding answers lacked a string guard before membership;
network scope/format and stale-evidence source/scope also failed. Cleanup passed without changing
the live 35B or enabling thinking. Its 619 completed samples observed maximum RSS/PSS
22134148/22123893 KiB and no process swap/OOM kill; cgroup peak is not complete model accounting.
Native timings are not TTFT or proven cause. The reviewed build record and live baseline maps show
GNU OpenMP and pthread OpenBLAS; environment thread counts alone do not prove effective BLAS
parallelism. A separate passive waiting-policy test is preparation, not an accepted optimization.
All five exact-`ead5e30` CI jobs passed; source checks are not model qualification. See the
[paired evidence record](../requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md).

## Complete Q5 candidate import — 2026-10-05

All 74 canonical ranges of the separate **Qwen3.8-27B UD-Q5_K_M** candidate were assembled.
The complete 19771509664-byte file matches its pinned upstream SHA-256; a protected independent
reader rehashed it and extracted actual GGUF3/qwen35 metadata and the 9993-byte template. Candidate
storage is protected and service-readable; no stable model link or serving service changed.
The template's 262144-token metadata is not accepted context. A distinct private standard trial
ran at 32 threads/16K/120 seconds per case after a 7179-ms load and exact protected project
mapping checks. Its first `en-format` case timed out at 120010 ms without an answer; fifteen cases
were not run, and cleanup confirmed unit/process/listener absence and unchanged baseline readiness.
The failed standard report creates no thinking gate. Numeric-only native timing fields
are diagnostic, not time-to-first-token or model reasoning; none were returned for this timeout.
Keep all failed Q8/Q5 records and unrun
thinking/context/matched-app/WAN/rollback gates. The live 35B model and public thinking-off remain.
All five exact-`e6af416` source CI jobs passed; neither CI nor artifact identity qualifies answers.
See the [paired qualification record](../requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md).

## Protected native runtime-tree verification

`scripts/check_native_runtime_bundle.py` checks a private inventory and its independently reviewed
SHA-256 under POSIX root. The strict schema is `deploy/inference/native-runtime-bundle.schema.json`.
Exact files/aliases, hashes, root ownership, modes, no-follow traversal, hardlinks, work bounds and
stable metadata are checked; it executes/installs nothing and writes no report or selection state.
Main checks passed 962 source tests/two POSIX skips and 156 related tests, with lint/types/docs.
The 90 new filesystem tests are explicit simulations; actual Windows verification is denied.
Controlled Linux-root verification passed nine regular files, one directory, fourteen aliases and
18761200 bytes without runtime changes; the live 35B PID/restart count and idle readiness stayed
unchanged. Tree identity is not signature/build provenance, complete ELF/system dependencies,
effective unit/maps, performance, model quality, WAN/cold start or deployment acceptance.
Keep private inventories and operational paths outside Git; see the paired record below.

## Latest bounded diagnostic — 2026-10-05

The exact-`f6cff8f` Q8 retest failed coding, source/scope preservation and an English hypothesis
deadline at 120001 ms; the corresponding Persian case was not run. Cleanup passed without changing
the serving model. The [paired qualification record](../requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md)
records final-answer review, resource-accounting limitations and protected-path corrections.
The finite AST checker now rejects unguarded non-string equality, membership, hashing and truthiness;
872 source tests/two POSIX skips are not model-quality acceptance. Q5 has 48 protected ranges/12 GiB,
not a full hash/load. Keep standard-first, actual context, final-only privacy, matched application,
WAN and rollback gates. Effective service mappings use protected libraries; shell RUNPATH output
alone is not proof of live mutable loading. Preserve runtime/35B rollback and public thinking-off.

## Distinct 3.8 Q5 source preparation — 2026-10-05

After the current finite 122B import window, prioritize the pinned **Qwen3.8-27B UD-Q5_K_M**
experiment in the [permissive packet](../requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md).
Its 18.41-GiB weights retain 27B parameters; lower precision is a bandwidth hypothesis, not an
accepted speed/coding improvement. Strict metadata/regression validation and generic detailed-answer
coding guidance are source work. Frozen regressions, deadline and normal/evidence prompt controls
are unchanged; independent bilingual coding proposals are ungraded. Full hash/template/CPU load,
standard semantics, final-only thinking, real context, matched app/WAN/rollback remain required.
Preserve Q8 failures, 122B partial ranges and the live 35B rollback. No serving/public thinking change.

## Permissively licensed alternative — 2026-10-05

The owner confirms Bank/customer access and now explicitly requests a permissive alternative.
The [dated qualification packet](../requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md)
records why the reviewed Apache-2.0 Qwen3.8 family stops at 27B, while Flash/Max weight licenses
remain custom. A further native-only 27B Q8 coding sample at 48 threads/16K/256 reasoning-budget
tokens/768 output exceeded 120 seconds at 120102 ms; it did not produce an accepted final answer.
The trial was stopped and the baseline remained ready. Historical failures are not replaced.

The pinned Apache-2.0 alternative **Qwen3.5-122B-A10B Q5_K_M** has three shards totalling about
84.22 GiB; its upstream license copy is verified, exact conversion revision remains unverified.
Range provisioning is partial, not a complete import/load or semantic pass. Observed guest
251.86 GiB/80 vCPUs/three NUMA nodes is distinct from a proposed 128-GiB/32–48-CPU/16K isolated
trial. Protect complete memory/cache accounting and the 120-second deadline. Serving 35B/runtime/
limits and public thinking-off are unchanged; no Q5 selection or full production acceptance.

## Flash-Next preparation — 2026-10-05

The [current record](../requirements/QWEN38_FLASH_QUALIFICATION_2026-10-05.md) supersedes earlier
guest-capacity observations, not their historical results: 80 vCPUs, three guest NUMA nodes and
about 251.86 GiB usable RAM after the owner-managed resize. A blank added 400-GiB disk is now a
separate protected model volume; original disks and serving limits/selection remain unchanged.
The pinned ggml-org Q8 two-shard set is **151.46 GiB**, distinct from earlier larger quantizer-set
estimates. Only its complete metadata shard and a bounded 512-MiB weight-range batch are staged.
Full memory fit, CPU load, actual template and answer/thinking/context qualification are not run.
Customer-facing custom-license applicability is pending; internal-only use cannot be assumed.
New offline metadata/coding/trial-review tools preserve failed samples and frozen questions; they
cannot approve or select a model. No model/AI release, public thinking or GPU path was enabled.

## Actual Qwen 3.8 trial outcome — 2026-10-05

[Dated measurements](../requirements/QWEN38_QUALIFICATION_2026-10-05.md): the single pinned
27B Q8 artifact is imported, size/hash verified and protected but **unselected**. Actual GGUF/template
and CPU loading at 16K passed. Four strict digit/short-recall cases passed per profile; native-only
thinking arithmetic passed in both languages. That is not complete coding, technical-thinking,
saved-chat or live-evidence acceptance. Both baseline/candidate missed an explicit non-string coding
invariant; candidate near-context recall (15360 input tokens) exceeded the 120-second deadline.

Candidate network answers took 69–74 seconds at 16 threads, 48–66 seconds at 32 threads, versus
12–20 seconds on the serving model in these single samples. Final trial RSS was about 30.15 GiB,
with zero swap; small cgroup accounting excluded precharged model page cache and is not full memory
fit. No comprehensive throughput, latency percentile or physical NUMA optimum is established.
The trial is stopped/removed; verified candidate/logs remain and ~27.05 GiB of exact temporary
duplicate parts was reclaimed. Serving 35B/runtime/limits, VM configuration and public thinking-off
are unchanged. Do not promote this slower failed-context profile just because host resources exist.

## Fresh capacity and Qwen 3.8 trial — 2026-10-05

The owner now supplies fresh DS-C/host screenshots and states no space is reserved and resources
are available for larger AI development. DS-C shows rounded **3.49 TB total / 1.79 TB provisioned /
1.71 TB free**. Host RAM shows **1.31 TB total / 213.64 GB used / 1.1 TB free** and a Platinum 8280
CPU label. These are point-in-time supplied observations, not measured future all-VM growth or
an instruction to consume ESXi/other services' capacity. The 900-GiB free-space guard is a planning
target, not a configured reservation; retain the existing 3-TB ceiling and other datastore exclusions.
Do not request the already supplied aggregate totals or this Storage screenshot again as missing.

Direct preflight at `2026-10-05T07:28:57Z`: 80 online vCPUs, 128769 MiB usable/107664 MiB available
RAM, no swap use, AVX-512/VNNI visible, one guest NUMA node and **80 virtual sockets**. Model-volume
space remains 169557 MiB available. Native serving MemoryMax is 96 GiB with 18 CPU equivalents.
The screenshot's spare host RAM has **not** been assigned to this guest. Physical NUMA placement,
saved virtual-hardware settings and storage latency are not proved by these observations.

The bounded [qualification packet](../requirements/QWEN38_QUALIFICATION_SPEC.md) resolves the
earlier capacity stop for **one** 27B Q8 trial and its range/assembly workspace. Provisioning uses
the configured proxy chain and pinned SHA-256; partial transfers cannot be selected. The working
35B model, runtime, app, secrets, public thinking-off flags and serving limits remain unchanged.
The source adapter adds the exact Q8 identity and disables Qwen3.8's default thinking/preserved
thinking; registration is not live selection. No runtime download or model-owned target credential.

For a later higher-precision Flash-Next trial, **256 GiB guest RAM** is a starting proposal;
consider 512 GiB only for measured larger-context/buffer needs. Its Q8 file metadata totals about
175.3 GiB before runtime state, whereas Q4 is already 103.69 GiB before state. Neither fits the
current 96-GiB service limit. Do not automatically allocate all host RAM or assume 80 inference
threads are optimal; review actual topology and benchmark bounded thread counts. This proposal is
not a resize, complete-memory-fit result, license approval or performance promise. Flash-Next is
the larger experimental option; the 27B precision trial is not the maximum parameter count.

## Earlier pre-import checkpoint — 2026-10-05

The owner authorized an upgrade after the UI deployment, not unlimited resource allocation or
automatic promotion. UI app `836b1ea` is live; the serving 35B model, runtime and disabled-thinking
flag remained unchanged. At that earlier checkpoint, no Qwen 3.8 weights had been downloaded,
imported or started; the fresh evidence/trial section above supersedes its capacity stop.

Fresh read-only guest preflight: 80 online vCPUs, 128769 MiB usable RAM (about 125.75 GiB), 108015
MiB available at observation, no swap use, one visible guest NUMA node, 169557 MiB available on the
model volume, and native-service MemoryMax **96 GiB**/CPU quota **18 equivalents**. Guest free space
does not establish backing-datastore capacity or outstanding snapshot/thin commitments. The old
owner screenshot and 500-GiB growth permission are not current observations. `nextops-server-operations`
stops large import here until a fresh DS-C Storage view and co-resident growth budget are supplied.
Do not delete snapshots, resize guests, assume spare host RAM, or change memory reservations to fit.

Official models are real current releases, not renamed Qwen3.5 artifacts:

| Option | Source facts and metadata | Current disposition |
|---|---|---|
| [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | Dense 27B; Apache-2.0; thinking controls | First lower-architecture-risk qualification candidate, not a proved improvement |
| [Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) | 125B/6B active language part, plus 51B n-gram embedding and 4B MTP; `qwen4_exp`; Qwen Community License 1.0 | Larger experimental candidate; license and actual CPU loading must qualify |
| [Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) | 2.4T total/95B active | Ideal four-bit weights alone are about 1.2 TB; outside this guest/budget |

The last row is arithmetic, not a measured complete footprint. Active parameters do not eliminate
stored weights. Larger parameter counts or vendor benchmarks do not establish more correct NextOps
answers. The current pinned llama.cpp source declares `LLM_ARCH_QWEN4EXP`; that is **not a successful
Flash-Next load/template/CPU test**. Do not claim either guaranteed compatibility or incompatibility
from an enum. No runtime replacement is approved by this observation.

### Pinned discovery metadata, not verified downloaded bytes

Upstream 27B revision: `1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`.
[Unsloth GGUF conversion](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/tree/4ca720788d1e01f1bff70c033e0d0028fd02e502)
revision: `4ca720788d1e01f1bff70c033e0d0028fd02e502` (third-party quantizer, not official Qwen GGUF).
`Qwen3.8-27B-Q8_0.gguf`: 29047086048 bytes, advertised SHA-256
`a680f44a06920e5d689774823782006aa3acc8db95750323373b24139b67e348`.
`Qwen3.8-27B-UD-Q4_K_M.gguf`: 16464440224 bytes, advertised SHA-256
`322e194ff79741c7baa497c240f677f54b201b0efab44ca8e50f122b39123482`.

Flash-Next upstream revision: `de4b8e4d43b917e7706784d8bb445c9af86a3540`.
[Unsloth GGUF conversion](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF/tree/38bb39ee97821de2c9009abb7e93950eec396e66)
revision: `38bb39ee97821de2c9009abb7e93950eec396e66`. Metadata sums: UD-Q3_K_XL three shards total
89986353824 bytes (about 83.81 GiB); UD-Q4_K_XL four shards total 111334654784 bytes (about
103.69 GiB). Q4 already exceeds the 96-GiB service limit before KV/state/buffers. Q3's arithmetic
headroom is not an accepted memory/quality/latency budget. Check every shard hash and conversion
lineage before provisioning. Legal applicability/organizational approval of Flash's custom license
is not established by this engineering review.

### Bounded implementation and acceptance sequence

Problem: improve EN/FA instruction following, technical/coding answers and useful bounded thinking
without destabilizing the working local service. Non-goals: cloud/GPU inference, model-owned
credentials, new tools/permissions, private reasoning storage, unlimited context/output or host resize.

1. Resolve fresh backing capacity and growth/rollback staging; record the exact license, conversion
   lineage, file hashes, template/tokenizer and immutable candidate manifest. No runtime download.
2. Qualify 27B Q8 as an initial precision/compatibility trial. Consider larger Flash Q3 only after
   custom-license review and measured complete memory fit. Do not import both speculatively.
3. Use an isolated CPU-only qualification profile behind existing interfaces, explicit lifecycle,
   protected rollback and unchanged production limits. Do not co-load an oversized candidate and
   serving model beyond available guest memory. Benchmark before any runtime change.
4. Compare frozen held-out EN/FA, arithmetic/formatting, DNS/network/firewall/service diagnostics,
   coding tests, source/time/scope, stale/partial/missing evidence and injection/denial cases against
   the baseline. Inspect raw final answers as well as guarded publication; no cloud evaluator.
5. Test bounded thinking separately. Set trusted template behavior explicitly; discard private
   reasoning and retain final-answer-only history. Default upstream thinking/history preservation
   must not silently enable the public flag. Test all supported effort levels within resource and
   deadline budgets; `xhigh` is not automatically the best usable profile.
6. Record load/queue, latency, CPU/RAM/NUMA, restart, actual server-WAN and fresh EN/FA live evidence,
   rollback/reapply and applicable VM cold-start gates. Keep one active/two queued requests. Promote
   only after required semantic/privacy/deadline gates pass; failed cases remain recorded.

Rollback: preserve the exact 35B artifact/runtime/app/profile and secrets; restore verified links
and configuration, restart only affected services, then check new generation, auth, evidence and
audit. No schema change is planned. Documentation must update this guide and its Persian pair,
current state/next task, artifact manifest, tests and release-status evidence only for actual outcomes.
See [conversation qualification](CONVERSATIONS.md) and [current next task](../NEXT_TASK.md).

## Model option review and fresh guest observation — 2026-10-04

Read-only inspection now observes 80 online guest vCPUs and 135024599040 usable RAM bytes
(about 125.75 GiB), with the recorded Qwen3.5-35B-A3B runtime/model links active. This is a guest
observation, not proof of saved ESXi allocation or spare host capacity; it supersedes the older
point-in-time sizing below. No resources, runtime, model or thinking flags were changed.

The official [MiMo-V2.6-Pro-RL card](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL)
reports 1.02T total/42B active parameters, 1M context and MIT licensing. The official
[Kimi K3 card](https://huggingface.co/moonshotai/Kimi-K3) reports 2.8T total/104B active,
1048576 context, native MXFP4 and its own license. K3 also expects preserved thinking history;
NextOps currently saves only final answers, so this is an interface/privacy design consideration,
not permission to start storing private reasoning.

Arithmetic inference, **not measured requirements**: ideal four-bit weights alone are about
510 GB/475 GiB for MiMo and 1400 GB/1304 GiB for K3, before metadata, KV/state, activations,
runtime and other guests. Active parameters reduce computation, not total stored weights. K3's
lower bound already leaves inadequate headroom on the documented host; MiMo might fit a larger
reviewed lab allocation, but usable CPU latency, artifact size and compatibility are unproven.
Neither is a qualified drop-in for the pinned CPU-only runtime. Advertised context is not an
accepted application budget, and vendor benchmarks do not establish Persian/NOC correctness.

Recommendation: preserve the serving model; first qualify an auditable CPU-compatible artifact
with frozen EN/FA/coding/live-evidence cases, measured latency/NUMA/memory, cold start, offline
behavior and exact rollback. Review license, source/revision/hash and conversion code before any
provisioning. Keep host/app/database/Zabbix capacity and storage-growth headroom; “all G10 resources”
does not imply that current co-resident services can safely lose their resources. No download,
API fallback, architecture migration or new resource allocation is authorized by this comparison.

The following sizing and qualification records are dated history, not the current guest allocation
or a claim that VM cold start passed for the latest source.

## Historical guest sizing and standard-chat profile — 2026-09-30

After the owner's resource extension, authorized read-only guest preflight observes 64 vCPUs,
193185 MiB usable RAM, zero swap use and one guest NUMA node/64 virtual sockets. This supersedes
the older AI guest allocation for current sizing, not the measured inference limits: the serving
profile has 16 threads, 16384 context, one slot, 18 CPU-quota equivalents and 96 GiB MemoryMax.
No further resize or ESXi topology change was made. Host placement/reservations remain unknown.
The [standard-chat profile](CONVERSATION_MEMORY_SPEC.md) is serving in controlled b5e74f9;
thinking failed and is disabled. Four-guest WAN/reboot and fresh short-context answers passed,
not full-budget context quality/latency. 122B is pinned research, not downloaded or selected.

[فارسی](../fa/CPU_AI.md) · [Index](INDEX.md)

**Status: bounded CPU evidence and tested native profiles; full benchmark and production acceptance remain open.** Source: master specification sections 2, 9–10 and 21. Exact bounded restart/rollback observations are recorded below. Earlier dated profiles passed WAN/VM cold-start tests; latest `7ce9d29` has process/WAN evidence but no current-source VM reboot/cold-start acceptance. Sustained expanded-profile throughput, production behavior and independent restore remain unqualified.

## Current larger-model qualification — 2026-09-29

Selected controlled profile: pinned Bartowski 35B-A3B Q4_K_M, protected immutable bytes, source
95c6e50 and unchanged llama.cpp b29c606e. Twelve API cases completed in 12.7–93.6s; twelve browser
cases and exact model/source rollback passed. Six final re-promotion confirmations and four
additional audit/hash pairs passed; their latency was 21.3–94.3s. Original 8B/source rollback is protected. GGUF architecture qwen35moe and template
SHA are recorded with trusted `enable_thinking=false` and configured context 8192. Its base-model
metadata names Qwen3.5-35B-A3B-Base; the upstream instruct reference is not verified conversion
lineage. Do not infer lineage or enlarge context to the native limit. VM/resources/one slot/queue/
384 tokens/120 seconds remain unchanged; no projector/MTP/GPU is enabled. Raw/full quality and
sustained load/NUMA/WAN/VM/production acceptance remain partial or not run. Older checkpoints:


Earlier continuation: protected 35B import passed; fourteen CPU samples stopped in 13.5–64.5s.
The first bb81109 guarded trial completed twelve API cases, but Persian CPU-idle labeling failed.
Exact rollback restored 8d1f1d2/8B; 35B is protected, not selected. Point process RSS was about
35.4 GiB; cgroup peak is not total resident RAM. VM/runtime/threads/context/queues/tokens/deadlines
remain unchanged. The source-only semantic repair requires fresh qualification. Raw provenance,
sustained/NUMA/server-WAN/VM/production gates are partial or not run. Earlier observations follow.


Fourteen matched development cases used the corrected app prompts, 384 output tokens, 16 threads
and one slot. Every sample completed: 8B took about 1.5–21 seconds; 14B about 4–54 seconds.
Semantic review rejected 14B: its Persian RAM answer called RAM flash memory and its Persian
calculation gave 50/200 as 50%, not 25%. Source/time/stale qualifiers also failed some cases.
The 8B baseline likewise had unsupported stale-health wording and source omissions. Completion,
fluency and enough RAM are not accuracy. The serving 8B and deterministic safeguards remain intact.

Official Qwen3-32B Q4_K_M is pinned in
[32B metadata](../../deploy/inference/qwen3-32b-q4-k-m.candidate.json) at revision
`938a7432affaec9157f883a87164e2646ae17555`, 19,762,149,024 bytes, SHA-256
`efd971561896866f0e910cce52761ca77b1b138090c7f15fe284676d57d1f689`, Apache-2.0.
Desktop and protected server import passed size/hash verification. Eleven answers completed in
9.9–97.6 seconds, with correct RAM/arithmetic and explicit English stale/source/time qualifiers.
The Persian stale request exceeded 120 seconds; testing stopped before injection cases. Its
latency gate failed, quality remains partial, and it was not selected. The transient cgroup peak
was 18,324,066,304 bytes, not a sustained memory/capacity benchmark.

Pinned [Qwen3-30B-A3B-GGUF](https://huggingface.co/Qwen/Qwen3-30B-A3B-GGUF), with 30.5B total and
3.3B active parameters, passed desktop/server size/hash import. All fourteen matched questions
completed in 1.3–23.7 seconds with the same prompts, 384-token ceiling, 16 threads and one slot.
This is a bounded observation, not sustained throughput. Raw source/collection/partial qualifiers
and Persian terminology remain partial. Unchanged assurance replay retained typed evidence and
replaced incomplete evidence prose; it does not prove arbitrary correctness.

The earlier timed 3deba0d/30B-A3B app trial returned twelve authenticated responses, but browser review
exposed Latin-prefix Persian LTR rendering. Exact model and source rollback restored c4351fd/8B
with fresh bilingual generation. The response-locale direction repair passed seven browser fixtures.
The corrected 8d1f1d2/30B-A3B trial passed eleven strict browser cases, then failed raw Persian
filesystem completion. Persian technical errors also rejected selection: SSD was called main
memory and non-native terms recurred. Twelve API responses and four stored evidence/audit hash
checks are not a semantic pass. [The artifact record](../../deploy/inference/qwen3-30b-a3b-q4-k-m.candidate.json)
now records failed bilingual quality and unrun offline cold start. Runtime, deadline, queue, network restrictions
and the existing 24-vCPU/128-GiB guest are unchanged; no cloud, runtime download or VM increase is
introduced. Full held-out and production acceptance remain separate.

Only the exact RTL source repair is live as 8d1f1d2 with original 8B. Twelve fresh API requests
passed literal/code checks; the strict browser likewise failed final raw Persian filesystem
completion after eleven cases. A separate focused-answer display check passed, without claiming
raw completion. The shared 384-token finding needs bounded prompt-scope review, not a larger queue
or deadline. Do not claim baseline 8B is universally accurate either.

The next bounded candidate is [Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B), with
35B total/3B active parameters. The [pinned artifact record](../../deploy/inference/qwen3-5-35b-a3b-q4-k-m.candidate.json)
uses [Bartowski's Q4_K_M quantization](https://huggingface.co/bartowski/Qwen_Qwen3.5-35B-A3B-GGUF),
not an official Qwen GGUF publication. Both cards declare Apache-2.0. Upstream reference revision
is not verified conversion lineage. Provisioning and source fixtures are not a load/quality pass.
Qwen3.5 needs trusted `chat_template_kwargs.enable_thinking=false`; Qwen3's soft suffix is not
supported. The native context is not the configured context: retain 8192, CPU-only, one slot,
the existing ceilings, no vision projector and no speculative MTP. Preserve older provider payloads.

## Non-negotiable execution boundary

Generation, planning, embeddings, reranking, AI anomaly processing and optional automated model judging run on local CPUs. No external AI endpoint or silent cloud fallback is permitted. An OpenAI-compatible request format is only a protocol shape, not authorization to call an external provider. GitHub is not a runtime AI dependency.

Use deterministic parsers, inventory resolution, policy checks, scheduling, basic correlation and known runbooks wherever possible. Logical planner/collector/analyst/verifier roles do not require multiple simultaneous models.

## Runtime and model candidates

The baseline is one dedicated service built from a pinned llama.cpp CPU revision. Verify the selected build's GPU-disable options, zero offload configuration and startup device report. Do not install CUDA/ROCm, GPU containers, accelerator-only dependencies or remote-code model loaders.

| Workload | Starting evaluation, not a final selection |
|---|---|
| General diagnostics | Approximately 7–9B multilingual quantized model; Qwen3-8B is one candidate |
| Triage | Smaller model versus deterministic classification |
| More difficult synthesis | Roughly 14B candidate after the baseline |
| Larger generation | 24–32B only when measured quality improvement justifies latency |
| Embeddings | Small multilingual encoder versus a candidate such as Qwen3-Embedding-0.6B |
| Reranking | Optional; enable only with measured retrieval gains within budget |

Compare supported Q4_K_M/Q5_K_M quantizations where available. Verify chat templates, structured-output behavior, tool arguments and Persian quality on the exact model/runtime combination. Do not choose 70B+ solely because weights fit in RAM. Ollama, OpenVINO CPU and vLLM CPU are alternatives to evaluate, not three additional mandatory services.

### Stage 1B repository candidate

The source-level evaluation pair is now recorded in the schema-validated
[`qwen3-8b-q4-k-m.yaml`](../../deploy/inference/qwen3-8b-q4-k-m.yaml): llama.cpp
`v0.4.1` at commit `b29c606e28a01b1bc8c1351026a0fa6e616bf6c4`, plus the official
`Qwen3-8B-Q4_K_M.gguf` at repository revision
`7c41481f57cb95916b40956ab2f0b139b296d974`. The model source records size
5,027,783,488 bytes and SHA-256
`d98cdcbd03e17ce47681435b5150e34c1417f50b5c0019dd560e4882c5745785`.

The pinned runtime was built with the recorded compiler/flags and OpenBLAS/OpenMP, promoted with its
binary SHA-256, and the model matched its expected filename, size, and SHA-256 before and after
promotion. A bounded authenticated CPU-only loopback smoke test succeeded. The repository now also
contains the paired hardened native units documented in [AI_SYSTEMD](AI_SYSTEMD.md), two file-backed
credential boundaries, fixed loopback origins, one llama.cpp slot, and the one-active/two-queued API
scheduler. These are source and smoke-test results, not full bilingual quality, latency, memory,
failure, offline cold-start, backup, restore, rollback, or production acceptance.

### Larger clarity candidate — 2026-09-29

The owner requested a larger local model. The official [Qwen3-14B-GGUF](https://huggingface.co/Qwen/Qwen3-14B-GGUF)
Q4_K_M artifact is pinned in [candidate metadata](../../deploy/inference/qwen3-14b-q4-k-m.candidate.json):
revision `530227a7d994db8eca5ab5ced2fb692b614357fd`, 9,001,752,960 bytes, SHA-256
`500a8806e85ee9c83f3ae08420295592451379b4f8cf2d0f41c15dffeb6b81f0`, upstream Apache-2.0.
It ran with the existing pinned CPU runtime in a temporary loopback-only comparison. Desktop and
guest size/hash checks and protected artifact import passed. Eight serial 192-token cases found
a truncated Persian RAM answer and wording/source omissions; a four-case 384-token follow-up
using the actual general prompt completed in about 13–41 seconds. The comparison used 16 threads,
one slot and a 32 GiB memory ceiling; it was not a sustained capacity or NUMA benchmark. Quality
remains failed and resource comparison partial. The serving 8B artifact and rollback are preserved.
Explicit `NEXTOPS_MODEL_ID` accepts only the reviewed 8B/14B/32B/30B-A3B/Qwen3.5-35B-A3B source aliases; arbitrary
names/URLs fail. Source compatibility is not serving selection or quality acceptance.
Runtime alias, local file and configuration must match, and missing files must not trigger a download.

Compare the same English/Persian questions, completion state, relevance, evidence preservation,
latency and resources. A larger model is a candidate, not a guarantee of accuracy or production
acceptance. Provisioning downloads occur outside the model service, not through runtime Internet.

## Hardware discovery before tuning

Confirm CPU model, physical/logical cores, sockets, NUMA nodes, effective affinity/cgroup allocation, instruction sets, available RAM, storage and existing workload contention. “G10” and “90 CPU” establish none of these details. Discovery must not install packages or stress the host; see [installation](INSTALL.md).

## Staged benchmark

Begin with one small candidate, one active request and a bounded prompt/output. Compare generation and prompt-processing thread counts, physical-core versus SMT placement and NUMA-local versus controlled multi-node execution. Then compare model sizes and quantizations using the same versioned corpus. Increase active requests from one to two and then four only when latency and resource pressure remain acceptable. Initially evaluate representative 2K/4K/8K input contexts and verify total-versus-per-slot context semantics. Finally test bounded mixed traffic: chat, incident synthesis, embeddings, ingestion, database work and builds.

Record exact model/build/revision, flags, CPU mask, memory placement, input/output token counts, sample count, cold/warm state, queue delay, time to first token, prompt and generation throughput, total latency, p50/p95, peak memory, CPU pressure, swap/page faults, cancellations and errors. Evaluate complete answers and correct tool arguments, not tokens/second alone.

## Resource policy

Maintain one budget across all services. Reserving roughly 20% of effective CPU capacity for the OS/control plane is only an unvalidated starting experiment from the specification. Replace it with measured allocations. Do not allocate 90 threads per request or start 90 API workers. Cap runtime/BLAS/OpenMP thread pools, worker counts, queue lengths, context, output, tool fan-out and investigation concurrency.

Enforce limits through validated container controls or systemd/cgroups. Give interactive work priority over re-indexing; use backpressure and cancellation. API access, audit and manual incident views must remain usable when inference is saturated or absent.

## Artifact and acceptance record

Every model record includes source, immutable revision, license, quantization, tokenizer/template, dimensions where relevant, file size and checksum. Provision or import artifacts explicitly; missing files must fail preflight rather than trigger downloads. Keep weights outside Git.

Select the production candidate only after held-out bilingual quality and latency tests, explicit CPU execution verification, no-Internet acceptance tests and a documented operating envelope. Capacity targets must be labeled targets until measured.
