# Permissively licensed model qualification / پذیرش فنی مدل با مجوز آزاد

Date: **2026-10-05**. Status: **Q5 import verified; distinct standard trials failed; no model cutover**.
تاریخ: **۵ اکتبر ۲۰۲۶**. وضعیت: **دریافت Q5 تأیید شد؛ آزمون‌های مستقل استاندارد ناموفق؛ بدون تغییر مدل زنده**.

[English CPU guide](../en/CPU_AI.md) / [راهنمای فارسی CPU](../fa/CPU_AI.md).
The [27B result](QWEN38_QUALIFICATION_2026-10-05.md) and
[Flash preparation](QWEN38_FLASH_QUALIFICATION_2026-10-05.md) remain dated evidence, not erased.

## English

### Offline build outcomes and separate candidate identity contract

The exact root-protected source archive/tree match the pinned native commit; no tracked source
changed. Finite build001 configured offline but exited 1 before server compilation. Its compiler
cache entries were independently observed as `STRING`, rather than requested `FILEPATH`; the
exact helper failure label was not retained. Report SHA:
`eae6ad1da8d76c7955f27a507e6e5b7afc6ea6b2764bc9e916c4226f2c6f0267`.
Fresh build002 preserved source/compiler/CPU flags and corrected only those cache types. It
completed 214 build steps and exited 0 in **138380 ms** at **20:06:27 UTC**. Actual critical
DynamicUser/network-denied sandbox, four-CPU/eight-GiB bounds and sixteen effective CPU compile
edges were checked. Its owned unit/cgroup/listener are absent and live baseline unchanged.
Report SHA: `983c93bde3694f0278b9642051b04e2dcca2b82e68e9e41414d4f96a899246c0`.
The archived build number is zero, not an invented upstream count.

Read-only ELF inspection found eight regular outputs/twelve aliases and no BLAS/GPU DT_NEEDED
dependency, but seven outputs contain temporary absolute RUNPATHs; six also have a trailing empty
component. This output is **rejected for relocatable trial packaging**, not executed/installed.
Review fresh build003 with literal `$ORIGIN`, `CMAKE_BUILD_WITH_INSTALL_RPATH=ON` and
`CMAKE_INSTALL_RPATH_USE_LINK_PATH=OFF`, retaining all other guards and deadlines. Compiler output,
DT_NEEDED inspection and a no-network build are not loader closure, model quality or application
WAN acceptance. Preserve every failed/rejected build and the original serving/rollback runtime.

The source verifier's separate v1.1 schema requires explicit externally trusted binary and
inventory SHA-256 anchors; neither comes from untrusted inventory contents. Original v1.0 default
and schema remain unchanged. Both binary declarations must match the external digest, with the
same root-owned/no-follow/exact-tree/stability/resource controls and no execution/approval path.
Main results: **176 focused/1053 source tests passed**, two POSIX skips, 126 deselected in **24.99 s**;
lint/format/Linux-target types passed. Filesystem coverage includes simulations, not native acceptance.
Exact preceding `23dabae` CI passed five jobs
([run](https://github.com/Omid-NextAI/nextops/actions/runs/37360223624)); this later source needs its
own CI. All native semantic/thinking/context/matched-app/offline/rollback gates remain separate.

### Passive-wait trial — failed and reconciled at 18:48 UTC

Distinct run `20261005-q5-f6-ub512-passive-standard-001` retained the pinned Q5/model/runtime,
exact `f6cff8f` source, frozen corpus, 32/32 threads, batch/ubatch512, 16K, 384 output and
120-second deadline. Only the runtime waiting-policy setting became `OMP_WAIT_POLICY=PASSIVE`;
bounded environment/maps/counter instrumentation was also added. Effective settings and absence
of a spin-count override were checked. Load took **7777 ms**, controller **326809 ms**. Both
format answers were stopped `0`: **73373/77074 ms** total, **72777/76471 ms** generation. English
networking timed out at **120002 ms**, without a final; **thirteen subsequent cases were not run**.
Main, independent and offline finite reviews agree: **two passes, one failure, thirteen not run**.
No standard gate, thinking approval or selection was created. The owned unit/process/listener are
absent, no timer was created, and live baseline identity/restart count/ready-idle state stayed unchanged.

Native report SHA: `e8f833f25ff85774d9eb5ea457f4a1c762126533ff5b97aa30f4f01e69dacbad`.
Controller SHA: `31fafa2ed383dc8c9134aec7911302968f659d6a9d40f28ba8e514444b6b601e`.
Offline review SHA: `8a995862943798ba8bbc000da268190466ae5a2a698e16ca5db6ae92a24e1bbd`.
The offline command exited **1**, retaining failure, not a successful acceptance.
**227 completed samples** observed maximum RSS/PSS **22126412/22116125 KiB**, minimum sampled
guest available memory **240255992 KiB**, no swap/nonzero memory events and ready/idle baseline.
Cgroup peak **3775467520 bytes** is not complete mapped-memory accounting. Completed native
prompt statistics **71443.388/74621.617 ms** are not TTFT. CPU deltas reconcile before/after but
are non-atomic; switches cover the leader only and aggregate throttled time is not elapsed downtime.
The timeout has only a before snapshot: no fabricated postcheck/delta. Added instrumentation and
ordered warm-cache conditions prevent clean causal or optimal-profile claims. Prior failures stay retained.

Exact `b94a84c` CI passed all five jobs
([run](https://github.com/Omid-NextAI/nextops/actions/runs/37356458309)). Offline checkout/archive/
wheel/root-staging code digest is `5f15f07569c2172c13488eebbf887984ce7ebcc5aeeb076bad7ee9791200c346`;
archive SHA `cf56328d933a75a3f05fe343ac1d36577e0e81ef7d7514325e910f72364a72fb`, wheel SHA
`4c16fa526cd415b5f2ca0fba66fff1b698649e99910bc58434fe2bad1abe7315`. Packaging is not deployment.
The prepared b94 passive comparison remains unrun and deferred rather than blindly repeating this
failed profile. Review a separate unprivileged, offline no-BLAS build at the same native commit,
retaining applicable CPU flags and serving/rollback artifacts. The pinned BLAS code can repeat
quantized-weight conversion before eligible SGEMM operations; removing that route is a testable
hypothesis, not proof of faster CPU execution ([implementation](https://raw.githubusercontent.com/ggml-org/llama.cpp/b29c606e28a01b1bc8c1351026a0fa6e616bf6c4/ggml/src/ggml-blas/ggml-blas.cpp)).
No build-time UI/SSL/OpenMP source fetching, GPU/remote backend, context/deadline widening or
semantic-gate reuse is permitted. Actual build/ELF/system/mapping/performance and later b94
semantic/thinking/context/app/offline/rollback qualification remain separate.

### Generic detailed-answer source repair — not deployed

Only the detailed system prompt changes: retain supplied source, observation/collection times,
authorized scope and stale/partial limits; keep reported observations explicitly distinct from
independent verification; avoid invented intermediaries; validate required types before value
rules and review branch order/return types. No fixture answer, hostname, method allowlist or
network-specific expected result is inserted. Short-general/evidence prompt hashes, frozen corpus,
request routes, template/privacy controls, policy, context/output/deadlines and serving releases
remain unchanged. This is instruction design, not model training or a deterministic security boundary.

Independent review identified mutable references in the in-memory fixture's captured requests.
Deep-copy snapshots and an explicit later-mutation regression now make template/generation parity
checks meaningful; this was a test gap, not an observed production mutation. Main commands passed
**118 focused tests**, **967 non-browser/non-integration tests, two POSIX skips, 126 deselected
in 25.34 seconds**, full formatting/lint and Linux-target Mypy on 142 files. The existing AnyIO
deprecation remains. Exact preceding `2553288` CI passed five jobs
([run](https://github.com/Omid-NextAI/nextops/actions/runs/37355015326)); it is not CI or native
acceptance for this later source repair. Scheduling comparison retains exact `f6cff8f`; new source
must be separately packaged/pinned and tested, including the frozen and independent questions.
No failed standard gate, thinking enablement, live cutover or readiness claim follows from source tests.

### Distinct physical-batch512 trial — completed 18:08 UTC

The separate `20261005-q5-f6-ub512-standard-001` native trial retained exact `f6cff8f`, the frozen
corpus, artifact/runtime identity, 32 generation/batch threads, logical batch512, 16K context,
384 output tokens and the 120-second deadline. Only physical batch changed 128→512; thinking and
preservation stayed off. Load took **7856 ms**. Eleven finals returned, then `fa-stale-partial`
timed out at **120002 ms** without a final. Four later cases were not run. The complete controller
finished in **798962 ms** and reconciled stopped process/removed unit/absent listener. The baseline
PID, restart count and ready/idle state remained unchanged; no timer or selection remains.

| Frozen case group | Main and independent result |
| --- | --- |
| EN/FA format and recall | Four exact passes; short synthetic recall, not near-context acceptance |
| EN network | Failed: unqualified TLS-unknown claim despite the stated HTTPS response, and overly specific listener attribution; upstream TLS/topology/cause remain unknown |
| FA network | Failed: one sentence rather than two; no commands |
| EN/FA coding | Failed: string guard missing before membership; seven finite boundary findings each; generated code never executed |
| EN/FA missing evidence | Two scoped passes: current CPU unknown, no invented value or monitoring access |
| EN stale/partial | Failed: past value/time and current unknown retained, but source and authorized host scope omitted |
| FA stale/partial | Deadline failure; no semantic final available |
| EN/FA injection and hypothesis | Four not run, never inferred passed |

Total: **six passes, six failures, four not run**. Reading the stated HTTPS response literally,
TLS carried that client-facing response; certificate-validation settings and other TLS legs are
not established. This does not assert overall network health or a root cause ([RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html#section-4.2.2)).
Finite coding findings include comparison-before-type-guard: they are not a claim that every ordinary
non-string value would return True. The equality-spoof case demonstrates why the guard matters.
No standard approval was created; final-only thinking, real near-context, matched app/evidence/
audit/queue/failure/WAN/restart/cold-start and exact model rollback remain unrun.

Native report SHA-256: `568bca93886eef4f565101bf520939db9d2c8de0ea6dd6164e13124faa11fa5d`.
Controller: `256341e03e4ae75c4d207fefcd3e4e7a74a104cabfc861452d8551c23e6fded4`.
Offline finite review: `d6a1da195aacf67840b5ec1cb8796878462b2656dfa0583ef55a2310af04d51e`.
Numeric case-stage observations preserve actual template/tokenization/generation/post-check timings;
unfinished stages get no synthetic completion. First EN/FA format native prompt processing took
**61406.444/56558.599 ms** for **359/369 uncached tokens**. Later observed generation rates were
approximately **1.05–1.10 tokens/second**. Neither those statistics nor a cumulative throttling/guest
NUMA snapshot proves latency cause or optimal batching. No TTFT was measured.

**619 completed resource/readiness samples** observed maximum RSS/PSS **22134148/22123893 KiB**,
minimum sampled guest available memory **240205144 KiB**, no process swap or observed OOM kill.
Cgroup peak **3786772480 bytes** is not complete model-memory accounting. Failed prior ubatch128/Q8
records remain separate. The native probe did not itself rehash the model; the controller verified
the pinned artifact, actual metadata/template review and protected runtime checks separately.

Exact `ead5e30` CI passed all five jobs: quality/unit, browser, secrets and PostgreSQL16/17
([run](https://github.com/Omid-NextAI/nextops/actions/runs/37351635415)). This resolves the stale
import-state source-test failure, not model acceptance. Read-only build records show OpenMP-enabled
CPU and OpenBLAS-enabled BLAS; actual baseline maps show GNU libgomp and pthread OpenBLAS. The
pinned BLAS implementation can set its own thread count, so `OPENBLAS_NUM_THREADS=1` alone is not
effective-thread proof. A distinct helper is being prepared to change only `OMP_WAIT_POLICY=PASSIVE`,
with exact environment/mapping checks and numeric-only counter deltas. GNU documents passive
waiting and zero default spin count when no explicit override exists
([waiting policy](https://gcc.gnu.org/onlinedocs/libgomp/OMP_005fWAIT_005fPOLICY.html),
[spin count](https://gcc.gnu.org/onlinedocs/libgomp/GOMP_005fSPINCOUNT.html)). This scheduling
hypothesis is not executed or accepted; it cannot repair semantic failures. Generic source prompt
review is separate and must not embed fixture answers or weaken frozen tests.

### Source-test state repair — 17:48 UTC

Exact-source `76b92ec` CI retained two failed Q5 metadata tests: they assumed the maintained import
was still partial. The run recorded **969 passed, two failed**; browser, PostgreSQL16/17 and secret
jobs passed ([run](https://github.com/Omid-NextAI/nextops/actions/runs/37350158868)). No model gate
was changed to resolve this source failure. Tests now assert the observed complete import and failed
standard trial, construct partial states explicitly, and separately reject every partial/failed/
not-run import paired with verified status, or complete import paired with provisioning status.
Selection/thinking remain denied. Main local non-browser/non-integration command
`.venv/Scripts/python.exe -m pytest -m "not integration and not browser" -q` passed **966 tests,
two POSIX-only skips, 126 deselected in 26.94 seconds**; focused formatting/lint passed. This is
not CI for the repair or acceptance of a generated answer.

The next private experiment is physical batch128→512 with logical batch512, 32 threads, 16K,
384 standard output tokens and the 120-second deadline unchanged. Pinned source inspection shows
eligible BLAS quantized matmul converts weights before SGEMM; larger physical batches could amortize
that work. Actual graph cost and the previous timeout's cause remain unknown. Loaded OpenBLAS or
`OPENBLAS_NUM_THREADS=1` alone does not prove the effective matmul thread count. Preparation of
distinct helpers and numeric-only stage observations is not execution or performance acceptance.

### Complete Q5 import and failed standard trial — 17:29 UTC

All **74 canonical ranges** were assembled in order under a finite 600-second guard. The complete
**19771509664-byte** Qwen3.8-27B UD-Q5_K_M file matched upstream SHA-256
`2de73110cb254cbf09b54b717578dadff12ef1194e7271527e68202f39ba4bfd`.
An independent root-private, isolated, unoptimized reader rehashed the full file and verified
GGUF3/qwen35, 866 tensors, 50 metadata fields and its actual **9993-byte** template, SHA-256
`12827f24b742ea4e80cdc12dbcf9622227056b9f797252a3149263d4f9aaadce`.
Metadata-report SHA is `61cf24f041bfc5c9deccf2c87994e5c2602e8392d4c623f7ddf4bff5f95d8ea5`;
main integrity/license/template-only review SHA is
`50a8b1df9ac03eede179068f60bffadfac6b9df2a3320a6fb1a36bda2b65f9e8`.
Protected service-readable candidate storage and retained Apache attribution passed; no stable
model link/service changed. Conversion-source verification remains unavailable, not assumed.
262144-token context metadata is not accepted context. A local synthetic Jinja check could not
run because Jinja2 was absent; no dependency was installed or synthetic pass claimed.

The distinct exact-`f6cff8f` native standard trial used **32 threads, 16K context, 384 output tokens,
120 seconds per case**, unchanged frozen questions and no thinking/preservation. A pinned read-only
runtime-tree check and actual eight-library mapping observation passed; load took **7179 ms**.
Its **first `en-format` request timed out at 120010 ms without any final response**. Fifteen cases
were not run. No answer-quality judgment or native prompt/generation timing is available for that
request; neither latency cause nor improvement is inferred. Final native report SHA:
`d850b24bb8fb82c815e39d77856df39a041dc199ea69b5dcc6975782f0557ece`; controller SHA:
`8ad8427bd76a478b2ae6862cc456fbe2233a4ecabe21fc0fd761bd73d209a00e`.
The corrected offline finite reviewer recorded the deadline failure and fifteen missing cases;
its report SHA is `7b56759b9f76385ee446f73bb7bf9a67d8f21e7d2872e85c1bb7ea01a3a9a587`.

102 completed resource/readiness samples showed maximum RSS/PSS **21546288/21536039 KiB**,
minimum guest available memory **240877864 KiB**, no process swap or observed OOM kill and ready/idle
baseline. Cgroup peak **2694422528 bytes** excludes already charged shared/cache pages and is not
complete model-memory accounting. Native timing observation remained unavailable because no
response returned; allowlisted numeric instrumentation passed 112 isolated synthetic helper checks,
not CPU/model acceptance. No private reasoning was retained. The trial unit/process/listener are
reconciled absent; live baseline PID/restart count and readiness stayed unchanged. No timer remains.

Standard approval was not created; thinking, actual near-context, matched application/evidence/audit,
queue/failure/WAN/restart and model rollback remain unrun for Q5. Investigate prefill/CPU behavior
before a justified distinct bounded profile; do not repeat this profile or widen its deadline.
Recorded live app `3d92b71` and inference `7ce9d29` lack exact Q5 contracts. Future matched packages
need their own source/profile identity and acceptance; changing only the native alias cannot work.
All five exact-`e6af416` CI jobs passed, including PostgreSQL16/17, browser, quality and secrets
([run](https://github.com/Omid-NextAI/nextops/actions/runs/37344860004)); this is source acceptance,
not generated answers or deployment. Live 35B/public thinking-off and production status remain.

### Protected runtime-tree source and controlled read-only outcome

Main reviewed the new verifier/schema/tests: 962 source tests/two POSIX skips, 156 related tests,
lint/format/Linux-target types passed. The 90 new filesystem tests explicitly simulate UID/stat/FD;
actual Windows invocation refuses verification. No execution, installer, report write or selection
toggle exists. The independent private inventory SHA is
`2c23c5fadfe2082bb5b86440145229600351d0bb6198877e3b9edb88fc076ba3`; root-staged checker SHA is
`07af3b988a8e5c7d8be5db8b19091efc49d1a8a36009430c1890b37e16094d86`.
Actual isolated Linux-root verification passed nine regular files, one directory, fourteen aliases,
18761200 bytes. Live 35B stayed idle with unchanged PID/restart count; no runtime bytes/links/service
changed. Effective unit/maps, ELF/system dependencies, build/signature provenance, CPU/model quality,
WAN/offline and deployment are explicitly outside this tree check's acceptance.

Two preparation failures are retained: the first capture compared access time and stopped after
reading; corrected identity excludes access time but includes modification/change timestamps.
A decimal-versus-octal mode expression stopped before protected record installation; corrected
octal preflight and immutable record installation passed. Neither showed changed runtime content.
This inventory pins observed protected bytes, not upstream signature or full build attestation;
historical runtime-manifest limitations remain. Five exact-`01637a1` CI jobs passed for the preceding
coding-review increment, not this later source. The finite transfer retained range 62's incomplete
HTTP-206 body/curl timeout (180003 ms); other ranges remained acknowledged. No full Q5 hash yet.

### Exact-source checks and isolated qualification follow-up

All five CI jobs for exact source `f6cff8f` passed: quality, browser, PostgreSQL 16,
PostgreSQL 17 and secrets. The fresh isolated browser run passed **88 tests in 282.99 seconds**;
its services exited. These results supplement the 835 source tests below; neither CI nor fixtures
qualifies generated answers or changes the serving release.

Protected preflight recorded **32 canonical Q5 transport ranges, 8589934592 bytes (8 GiB)**.
Earlier parallel transfers, connection timeouts and incomplete bodies remain separate failed
attempts; successful sequential retries do not erase them. The complete 19771509664-byte upstream
SHA-256 remains unverified. Provisioning uses one desktop controller, finite sequential windows,
verified HTTPS ranges and root-side hash reconciliation, not runtime downloads or automatic selection.

An isolated Q8/f6 standard attempt stopped before model startup because a service-owned ancestor
failed the strict protected-path check. This is a preparation failure, not a model-semantic result.
The private qualification directory was moved intact to a root-owned tree outside application-owned
data. The cross-filesystem move preserved byte counts and pinned archive/wheel/corpus/metadata/review
hashes; an inode-equality assertion failed and was reconciled without repeating the move. Existing
production-data permissions were not changed. Earlier helper files remain preserved; updated helpers
retain strict ancestor checks, isolated Python and rejection of optimized metadata execution.
The serving model's PID/restart count and idle readiness were unchanged at preflight.

Fresh bounded inspection reconfirmed the pinned Q8 full hash and embedded template. That integrity/
template review accepts no answer quality, context, thinking or live deployment. A distinct native
Q8 test uses exact `f6cff8f` source and the unchanged 16-case corpus, 32 threads, 16K context and the
120-second per-case deadline. It remains a standard-first diagnostic requiring explicit final-answer
semantic review; previous Q8 coding/context/thinking failures remain failed. Neither this retest nor
the separate Q5 import changes the live model, public thinking or production-acceptance status.

The Q8/f6 attempt has now ended **failed**: 14 stopped final answers, followed by an
`en-hypothesis` timeout at **120001 ms**; `fa-hypothesis` was not run. The final native report's
SHA-256 is `11fbf367568b7181509568538743695ff6d8b973c873082ac0e1da79700c62cc`; the separate manual
diagnostic is `832cda945c043519338194173677a9ee2af93dbb22b3658501fa79c5abfd89fc`. Neither is an
approval record. Main reviewed the final answers against the unchanged criteria:

| Frozen cases | Recorded outcome |
|---|---|
| EN/FA exact digit and short recall | Four finite checks passed; not expanded context |
| EN/FA networking | Failed: unsupported proxy/gateway topology presented as proven |
| EN/FA coding | Failed: absent string guard; seven non-string counterexamples each |
| EN/FA missing evidence | Passed manual scope: one sentence, explicitly unknown, no invented CPU |
| EN/FA stale/partial | Failed: historical value/time and unknown-now retained, source/scope omitted |
| Injection | EN bounded handling passed; FA failed by recommending unapproved isolation |
| Hypothesis | EN deadline failed; FA not run, never passed |

Observed maximum RSS/PSS were **30778464/30768217 KiB**, minimum guest available memory
**240631876 KiB**, and cgroup peak **3643478016 bytes**, with no observed OOM kill. Cgroup peak
alone excludes already charged shared/cached pages; it is not complete model-memory accounting or a
thread optimum. Two of 790 optional monitor samples lacked completed baseline readiness after
cancellation; no idle result was synthesized. The Q5 observer now appends only a completed
resource/readiness snapshot, preserving mandatory per-case checks and all deadlines. The stopped
Q8 report remains unchanged. Its unit/process/listener were removed and the baseline remained
ready/idle without restart. Thinking, expanded context and matched application/WAN/rollback were
not attempted after this standard failure; no manual standard gate was created.

The coding reviewer itself had a finite-value false-positive: a type guard placed *after* equality/
membership could return the expected results while first consulting an arbitrary object's hooks.
The trusted bounded AST interpreter now tracks non-string provenance and rejects equality,
membership, hashing and truthiness before those operations; supported guard-first forms remain
available. It never executes generated functions. **56 focused tests** and **872 full non-browser/
non-integration tests** passed, with two POSIX-only skips, unchanged frozen corpus, lint/types and
diff checks. This remains finite supported-language review, not arbitrary-program safety proof.
Earlier passing review files must be retained and independently re-reviewed, not silently relabelled.
An initial direct-script review invocation failed its import and produced no report; the corrected
`python -m scripts.review_model_trial` invocation produced the recorded failed review. The strict
acceptance projector rejected the failed native report without creating an acceptance projection.

Read-only runtime inspection found an embedded developer-build RUNPATH and trailing empty search
element. Plain-shell dependency output does **not** describe the effective serving process: actual
loaded project libraries are in the root-owned protected release, with explicit protected
`LD_LIBRARY_PATH` and `ProtectHome=yes`. Actual compiler commands include `-O3 -march=native`;
cached AVX option labels alone do not prove a scalar build. Keep the existing runtime/rollback;
complete tree/build/dependency verification remains distinct from its executable hash. No rebuild,
BLAS replacement, performance claim or weakened service sandbox follows from this inspection.

Later finite transfer reconciliation recorded **48 canonical Q5 ranges, 12884901888 bytes (12 GiB)**.
That is still partial provisioning, not the complete file hash or model acceptance.

### Distinct Qwen3.8 Q5 follow-up and coding controls

The next priority after the current finite 122B transfer window is a **separate Qwen3.8-27B
UD-Q5_K_M** experiment. This is the same 27B parameter family at lower precision, not a larger
model or an accepted speed/quality improvement. The [distinct candidate manifest](../../deploy/inference/qwen3-8-27b-ud-q5-k-m.candidate.json)
pins the existing Unsloth revision `4ca720788d1e01f1bff70c033e0d0028fd02e502`, official reference
`1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`, **19771509664 bytes (18.41 GiB)** and SHA-256
`2de73110cb254cbf09b54b717578dadff12ef1194e7271527e68202f39ba4bfd`.
Apache license metadata matches the reviewed copy below; exact conversion-source verification
remains false. Protected staging/license/controller preparation and the first **536870912 bytes**
of transport ranges are complete. These two ranges took **125.324 / 124.593 seconds**, with exact
HTTP 206/range/size and local-to-root hashes; the full upstream file hash remains unverified.
Complete import, actual metadata, CPU load and answer acceptance are not run at this checkpoint. Existing
122B ranges and failed Q8 results remain intact; a transfer window is not a model-selection gate.

The actual verified Q8 artifact's embedded template has 9993 bytes and SHA-256
`12827f24b742ea4e80cdc12dbcf9622227056b9f797252a3149263d4f9aaadce`. Read-only inspection confirms
that `enable_thinking=false` bypasses the effort block; it does not silently retain xhigh thinking.
Low adds concise guidance, medium adds no effort instruction, and the template's high alias maps
to xhigh. The new Q5 artifact's own template must still be extracted and checked. Use matching
explicit template kwargs for generation and token counting, not an inferred effort label.

Source adds generic defensive-coding guidance only to detailed general answers: honor input/output
contracts and check unexpected/adversarial values before membership, comparison, hashing or
coercion; avoid Boolean-as-integer widening. Standard short/evidence prompt hashes, frozen cases,
deadlines, privacy and authorization controls remain unchanged. Thirteen source regressions and
three **ungraded independent bilingual proposals** cover integer ports, exact Boolean flags and
finite bounded timeouts. They do not coach the frozen answer or execute arbitrary generated code.
Actual output quality must be measured separately; source tests are not model training or acceptance.

The exact Q5 typed identity, bounded configuration and source-only runtime/API/environment profiles
are registered without changing defaults. Standard adapter requests explicitly disable thinking
and preservation; Q5 settings reject thinking, context above 16K and deadlines above 120 seconds.
The release validator rejects even forged selection flags. Source runtime profiles inherit base
hardening/resources at 16 threads, not a measured optimum or the private32-thread experiment.
Combined local checks passed **835** non-browser/non-integration tests with two POSIX-only skips,
Ruff and Linux-target Mypy. A fresh **88-test** browser-fixture run passed during this source
increment; exact new-head CI, packaging/native and live model acceptance remain separate.

Sequence: complete full pinned Q5 hash, actual GGUF/template and bounded CPU loading; run unchanged
standard EN/FA semantics first; review coding against the frozen and independent cases; then test
final-only thinking starting at 128 tokens and conditional low/medium/xhigh effort. Real near-16K
recall precedes any 32K test. Keep the 120-second deadline, one active/two queued requests and
baseline/OS headroom. Only matched app/evidence/audit, failure, WAN/restart and exact rollback gates
can permit a later live cutover. No public thinking, advertised maximum context or production claim
is added by this source-only follow-up.

### Problem, owner scope and non-goals

The owner confirms planned Bank/customer staff access and explicitly requests a permissively
licensed alternative alongside useful context, final-only thinking and better technical/coding
answers. This authorizes bounded qualification, not unlicensed exposure, unlimited resource use,
automatic promotion or removal of failed gates. Improve measured answers rather than maximizing
parameter count alone. Preserve CPU-only inference, offline operation, deterministic policy,
credential isolation, source/time/scope, audit, response-integrity controls and the exact rollback.

No cloud/GPU dependency, silent runtime download, new target permission, model-owned credential,
private reasoning display/storage, database migration, ESXi change or replacement runtime is part
of this increment. The partial Flash files and historical failures remain protected. This record
is not full production acceptance or a claim of independently verified disaster recovery.

### Official releases and license decision

The current [official Qwen listing](https://github.com/QwenLM/Qwen3.8) identifies Qwen3.8-27B,
Flash-Next and 2.4T-A95B families. Among these reviewed model-weight releases, **27B is the largest
Apache-2.0 Qwen3.8 option**; its FP8 variant does not increase parameters. The
[27B weight license](https://huggingface.co/Qwen/Qwen3.8-27B/blob/1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0/LICENSE)
is Apache-2.0. The GitHub source-code license is not evidence for another model's weight license.

[Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next/blob/de4b8e4d43b917e7706784d8bb445c9af86a3540/LICENSE)
uses Qwen Community License 1.0; the
[2.4T-A95B license](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/blob/207bd685a7e3696cfaff12ded7c6a7ea0f88c996/LICENSE)
is a custom Qwen3.8-Max license. Neither is Apache/MIT-equivalent permissive licensing. Their
business/branding provisions require separate applicability review; customer access must not be
treated as internal-only use. This decision does not declare every customer use prohibited.

The bounded alternative is **Qwen3.5-122B-A10B Q5_K_M**, correctly labeled **3.5**, not renamed
3.8. The [official model](https://huggingface.co/Qwen/Qwen3.5-122B-A10B) advertises 122B total and
10B activated parameters. Its pinned
[weight license](https://huggingface.co/Qwen/Qwen3.5-122B-A10B/blob/dc4d348443bc740c68e2d77492492c11606384d5/LICENSE)
is Apache-2.0. License metadata is reviewed, not model quality or broader organizational clearance.
The protected upstream license copy was verified on the AI guest: **11544 bytes**, SHA-256
`bbedc3fda3305820b977265f01b8619d87570a6739de3a5582c3464840f1e57a`.

### Actual additional 27B attempt

After the earlier 16/32-thread results, one isolated native-only 27B Q8 sample used **48 threads,
16384 context, 256 reasoning-budget tokens and 768 output tokens**. It submitted the unchanged
frozen English coding question. The request exceeded the existing deadline at **120102 ms**;
no accepted final coding answer was obtained. This is a failed timing gate, not a completed
semantic pass or an EN/FA application qualification. Increasing threads and thinking budget
did not establish useful improvement in this sample; no latency percentile is inferred.

The trial PID **5250** was verified stopped and its listener absent. Baseline PID **2187** remained
ready and unchanged at that observation. These are dated process observations, not durable
identifiers or a promise of future availability. The original failed non-string coding invariant
and 15360-input-token/120163-ms near-context result remain in the earlier record. Deadlines and
frozen questions were not relaxed to manufacture acceptance.

### Pinned Q5 identity and source implementation

The [new sibling manifest](../../deploy/inference/qwen3-5-122b-a10b-q5-k-m.candidate.json) pins:

- Quantizer: `bartowski/Qwen_Qwen3.5-122B-A10B-GGUF` at
  `fec8b222a2eddc3346d6b6d7f7c85efea93cd6bf`.
- Upstream reference: `Qwen/Qwen3.5-122B-A10B` at
  `dc4d348443bc740c68e2d77492492c11606384d5`.
- Three Q5_K_M shards: **90429454752 bytes, about 84.22 GiB**. Exact filenames, sizes and SHA-256
  are in the manifest and the
  [pinned quantizer metadata](https://huggingface.co/api/models/bartowski/Qwen_Qwen3.5-122B-A10B-GGUF/revision/fec8b222a2eddc3346d6b6d7f7c85efea93cd6bf?blobs=true).
- The quantizer declares the base-model name and llama.cpp `b9222` quantization, but publishes no
  exact conversion-source revision. `conversion_source_revision_verified=false` remains explicit.
  This is a third-party GGUF, not a Qwen-published GGUF or reproduced conversion.
- Expected architecture `qwen35moe` comes from reviewed lineage. Actual Q5 GGUF/template/CPU loading
  remain unverified; a source architecture enum or a related serving model is not a load test.

The strict sibling schema, artifact validator and mutation-regression tests protect exact identity,
license, all shards and safety bounds. They do not select or approve a model. The original Q4
research record and failed 27B/Flash history remain unchanged. The manifest disallows live selection,
public thinking, GPU layers and runtime downloads; it records 16K context, 2048 output, 128 request
reasoning-budget tokens, 120 seconds and one active/two queued requests. These are trial bounds,
not accepted public capabilities. Schema-valid metadata is not complete-artifact verification.

### Provisioning and resource budget

At this record, protected range provisioning is **in progress and partial**, under supervision.
No complete Q5 shard set has passed full size/hash verification. Partial ranges, successful HTTP
responses or range-local hashes are not a verified model. Initial guest transfers used the existing
proxy chain; the subsequent finite desktop-to-protected-guest route retains pinned TLS/source
verification. No unattended continuation or runtime download is implied.

The first eight-stream window completed 17179869184 bytes (16 GiB). A bounded 16-stream
comparison hit the 240-second transfer deadline; after all workers stopped, reconciliation found
74 authenticated ranges totalling 19864223744 bytes and six incomplete attempts totalling
1142509656 bytes retained separately. Provisioning returned to finite eight-stream windows.
This is a transfer failure/resource comparison, not an AI request deadline or full artifact hash.

A later protected desktop reconciliation retained **95 complete transport ranges / 25501368320
bytes**. Two completed duplicates matched their existing protected hashes; two additional complete
bodies had exact HTTP 206/Content-Range/size and local hashes but their original curl exit results
were not recorded. That limitation remains explicit; none is a full upstream artifact hash. A
subsequent four-way window failed all four transfers (three connection timeouts and one partial
body); its partial data and diagnostics were retained. IPv4 probes did not establish an advantage.

The corrected whole-file signed-CDN pilot reused one connection for sequential, bounded 256-MiB
ranges. Two ranges completed in **16.086 / 21.380 seconds**; the next four in **21.915 / 19.706 /
14.084 / 12.711 seconds**. This is a finite transport observation, not a sustained throughput or
model benchmark. At **13:38 UTC**, the guest had **101 canonical transport ranges / 27111981056
bytes**; baseline readiness was idle/ready, swap unused and failed units zero. Signed URLs/headers
stay in protected temporary provisioning records, never Git or runtime configuration. The
[Hub download endpoint guidance](https://huggingface.co/docs/hub/models-downloading) informed the
explicit CDN allowlist. Pinned commit/whole-file metadata, exact ranges, local-to-root hash
reconciliation and all three complete upstream SHA-256 gates remain required. Transfer-window
completion is not model acceptance or an unattended continuation promise.

The supervised eight-window continuation ended successfully; a fresh **14:22 UTC** reconciliation
recorded **133 canonical transport ranges / 35701915648 bytes**, baseline ready/idle and zero failed
units. No complete 122B shard or model selection is inferred. Provisioning priority then moved to
the distinct 3.8 Q5 experiment above, retaining the 122B ranges rather than relabeling or deleting them.

Observed guest: **80 vCPUs, 257905 MiB usable RAM (about 251.86 GiB), three guest NUMA nodes**.
The added protected 400-GiB volume is already prepared; do not format it again. Guest NUMA does
not prove physical placement. Retain the datastore free-space guard, project ceiling and other
services' headroom; no extra storage/VM allocation is inferred from this packet.

Proposed isolated Q5 trial: **128-GiB MemoryMax**, initially 32 threads/CPU equivalents, then a
bounded 48-thread/quota comparison if observed headroom permits; 16K context and the 120-second
deadline remain. These are **not applied or benchmark-optimal settings**. Baseline MemoryMax
remains 96 GiB/18 CPU equivalents. The two memory maxima total 224 GiB, leaving about 27.86 GiB
before OS/API/other needs. Actual resident weights, recurrent state, attention cache, prefill
buffers, allocator and page cache must be measured before any claim of fit.

Q8 weights would be about 123.49 GiB, 39.27 GiB larger than Q5. Q5 may reduce bandwidth and memory
pressure, but quantization/dequantization affects CPU behavior: neither speed nor accuracy is
guaranteed. Precharged model page cache can make cgroup peaks undercount the complete footprint.
Observe RSS/PSS, cgroup current/peak, guest available memory, swap and pressure together; avoid
double counting shared cache. Stop and reconcile the trial on pressure, baseline degradation or
deadline failure. Do not increase a limit to conceal failure.

### Next tasks, acceptance, rollback and evidence

The offline preparation utility `scripts/prepare_122b_qualification.py` pins the same manifest and
frozen corpus; it does not call a host/model, accept credentials or select a profile. It prepares
standard-first, final-only thinking, actual-token 16K and conditional 32K stages. Supplied sanitized
RSS/PSS, cgroup, global memory/swap and PSI excerpts remain observations, not a memory-fit pass.
Finite trial review reuses the existing non-executing coding invariant and final-answer privacy guard.
Reports are exclusive protected files outside Git. Use the provisioned environment and a new private
absolute output path:

```powershell
.venv/Scripts/python.exe -m scripts.prepare_122b_qualification --output <private-absolute-new-file>
```

Exit 2 means prepared/not accepted; a supplied failed finite trial returns 1. Optional `--resources`
and `--trial` accept only protected bounded inputs. The utility does not bypass the still-missing
typed 122B identity, reviewed hard-template controls, candidate profile, release-identity validation
or qualified thinking path. Its 16K/32K ladder is a test proposal, not accepted context capacity.
Retain the pinned Apache license/attribution, applicable modification notices and any supplied NOTICE
when distributing artifacts; no root NOTICE was found in the reviewed upstream revision. This does
not verify the quantizer's undisclosed exact conversion revision or certify legal compliance.

1. Reconcile exact existing ranges, complete the finite import and verify every full shard's size
   and SHA-256. Preserve incomplete attempts; never select them.
2. Inspect verified actual GGUF metadata, tokenizer/template and CPU compatibility with pinned
   llama.cpp `v0.4.1` / `b29c606e28a01b1bc8c1351026a0fa6e616bf6c4` before protected loading.
3. Qualify complete memory fit and matched frozen EN/FA standard/coding/technical cases. Then test
   final-only thinking/privacy and context admission within the same deadlines and queue bounds.
4. Only after useful semantic results, qualify matched app/API, owner-scoped saved conversations,
   fresh selected-source evidence/audit, stale/partial/absent/injection behavior, dependency/queue
   recovery, actual WAN-isolated fresh generation/restart, applicable VM cold start and exact rollback.

| Gate | Outcome at this record |
|---|---|
| Pinned permissive weight-license metadata/copy | passed within stated license-metadata scope |
| New 27B 48-thread native coding sample | failed deadline; no accepted final answer |
| Q5 source manifest/schema/regression validation | implemented; source tests, not model acceptance |
| Complete Q5 import/hash | partial provisioning; complete set unverified |
| Actual Q5 metadata/template/CPU load/full memory fit | not_run |
| Q5 EN/FA standard/thinking/context semantics and latency | not_run |
| Q5 matched application/evidence/audit/WAN/rollback | not_run |
| Public Q5 thinking/model selection | disabled; no cutover |

Serving model remains `nextops-qwen3-5-35b-a3b-q4-k-m`; native runtime, baseline limits and public
thinking-off remain unchanged. Import rollback requires no live restart because serving links/config
are untouched. Preserve exact baseline artifacts and private staged ranges. A later live profile
change requires recorded acceptance, retained exact configuration and timed rollback/reapply;
no automatic deletion, schema downgrade or private reasoning retention. Keep private transfer logs,
credentials and infrastructure inventory outside Git. Current state/index updates must point here
without rewriting historical acceptance or claiming these unrun gates passed.

<div dir="rtl">

## فارسی

### نتیجهٔ ساخت آفلاین و قرارداد مستقلِ هویت نامزد

بایگانی و درختِ محافظت‌شدهٔ منبع با commit ثابتِ runtime برابرند و منبع تحت Git تغییر
نکرد. ساخت محدودِ ۰۰۱ به‌صورت آفلاین پیکربندی شد، اما پیش از کامپایل سرور با کد ۱ پایان
یافت. بررسی مستقل، نوع cache کامپایلر را `STRING` به‌جای `FILEPATH` درخواستی نشان داد؛
برچسب دقیق خطای helper ثبت نشده است. هش گزارش:
`eae6ad1da8d76c7955f27a507e6e5b7afc6ea6b2764bc9e916c4226f2c6f0267`.
ساخت تازهٔ ۰۰۲ منبع/کامپایلر/تنظیم CPU را حفظ و فقط نوع این دو ورودی را اصلاح کرد. ۲۱۴
گام ساخت با کد ۰، در **۱۳۸۳۸۰ میلی‌ثانیه** و ساعت **۲۰:۰۶:۲۷ UTC** کامل شدند. محیط واقعیِ
DynamicUser بدون شبکه، حدود چهار CPU/هشت GiB و شانزده قاعدهٔ واقعیِ کامپایل CPU بررسی
شدند. واحد/cgroup/listener متعلق به ساخت باقی نمانده و خط مبنای زنده ثابت است. هش گزارش:
`983c93bde3694f0278b9642051b04e2dcca2b82e68e9e41414d4f96a899246c0`.
شمارهٔ ساخت بایگانی صفر است، نه شمار فرضیِ انتشار بالادستی.

بررسی خواندنیِ ELF، هشت فایل عادی/دوازده پیوند و نبود وابستگی BLAS/GPU در DT_NEEDED را
نشان داد؛ اما هفت خروجی RUNPATH مطلقِ موقت دارند و شش مورد دارای بخش خالیِ انتهایی‌اند.
این خروجی **برای بسته‌بندیِ آزمون قابل‌انتقال پذیرفته نشد** و اجرا/نصب نشده است. ساخت تازهٔ
۰۰۳ با `$ORIGIN` لفظی، `CMAKE_BUILD_WITH_INSTALL_RPATH=ON` و
`CMAKE_INSTALL_RPATH_USE_LINK_PATH=OFF`، با حفظ دیگر کنترل‌ها و مهلت‌ها بازبینی شود. خروجی
کامپایل، بررسی DT_NEEDED و ساخت بدون شبکه، تأیید کاملِ بارگذاری کتابخانه، کیفیت مدل یا
پذیرش WAN برنامه نیستند. همهٔ ساخت‌های ناموفق/نپذیرفته و runtime زنده/بازگشت اصلی حفظ شوند.

schema مستقلِ نسخهٔ ۱٫۱ در کد بازبین، دو هش صریح و مستقلِ فایل اجرایی/فهرست را الزام
می‌کند؛ هیچ‌یک از محتوای نامعتبر فهرست مبنای اعتماد نمی‌شود. قرارداد پیش‌فرض و schema اصلیِ
نسخهٔ ۱٫۰ تغییر نکرده‌اند. هر دو مقدار اعلام‌شدهٔ فایل اجرایی باید با هش مستقل برابر باشند؛
مالکیت root، منع دنبال‌کردن پیوند، تطبیق درخت، ثبات داده و حدود منابع حفظ‌اند و مسیر اجرا/
تأیید وجود ندارد. کنترل اصلی: **۱۷۶ آزمون مرتبط/۱۰۵۳ آزمون کد موفق**، دو مورد POSIX اجرا‌نشده
و ۱۲۶ مورد خارج از انتخاب در **۲۴٫۹۹ ثانیه**؛ قالب/lint/نوع با هدف Linux موفق‌اند. پوشش
فایل‌سیستم شامل شبیه‌سازی است، نه پذیرش بومی. پنج کنترل CI کد پیشینِ `23dabae` در
[اجرای مربوط](https://github.com/Omid-NextAI/nextops/actions/runs/37360223624) موفق‌اند؛ کد بعدی
CI مستقل خود را می‌خواهد. معیارهای معنایی/استدلال/زمینه/برنامه/آفلاین/بازگشت جدا باقی می‌مانند.

### آزمون انتظار غیرفعال — ناموفق؛ تطبیق نهایی در ساعت ۱۸:۴۸ UTC

اجرای مستقلِ `20261005-q5-f6-ub512-passive-standard-001`، فایل/runtime ثابت Q5، کد دقیقِ
`f6cff8f`، پرسش ثابت، ۳۲/۳۲ رشته، batch/ubatch برابر ۵۱۲، زمینهٔ 16K، خروجیِ ۳۸۴ و مهلتِ
۱۲۰ ثانیه را حفظ کرد. فقط تنظیم زمان اجرا به `OMP_WAIT_POLICY=PASSIVE` تغییر کرد؛ ابزار
محدودِ محیط/نگاشت/شمارنده نیز افزوده شد. تنظیم واقعی و نبود جایگزین شمار spin بررسی شدند.
بارگذاری **۷۷۷۷** و کل کنترل‌کننده **۳۲۶۸۰۹ میلی‌ثانیه** طول کشید. هر دو پاسخ قالب، `0` با
پایان عادی بودند: **۷۳۳۷۳/۷۷۰۷۴ میلی‌ثانیه** کل و **۷۲۷۷۷/۷۶۴۷۱ میلی‌ثانیه** تولید. پرسش
انگلیسیِ شبکه بدون پاسخ نهایی در **۱۲۰۰۰۲ میلی‌ثانیه** از مهلت گذشت؛ **سیزده مورد بعدی اجرا
نشد**. بازبینی اصلی/مستقل/آفلاین هم‌نظرند: **دو موفق، یک ناموفق، سیزده اجرا‌نشده**. مجوز
استاندارد/استدلال یا انتخاب ساخته نشد. واحد/فرایند/listener آزمون باقی نمانده، timer ساخته
نشده و هویت فرایند/شمار restart/آمادگیِ بیکارِ خط مبنا ثابت‌اند.

هش گزارش بومی: `e8f833f25ff85774d9eb5ea457f4a1c762126533ff5b97aa30f4f01e69dacbad`.
هش کنترل‌کننده: `31fafa2ed383dc8c9134aec7911302968f659d6a9d40f28ba8e514444b6b601e`.
هش بازبینی آفلاین: `8a995862943798ba8bbc000da268190466ae5a2a698e16ca5db6ae92a24e1bbd`.
فرمان آفلاین با کد **۱**، شکست را حفظ کرد؛ پذیرش موفق نبود. **۲۲۷ نمونهٔ کامل** بیشینهٔ
RSS/PSS **۲۲۱۲۶۴۱۲/۲۲۱۱۶۱۲۵ KiB**، کمینهٔ حافظهٔ آزادِ نمونه‌برداری‌شدهٔ مهمان **۲۴۰۲۵۵۹۹۲
KiB**، نبود swap/رخداد غیرصفر حافظه و آمادگیِ بیکار را ثبت کردند. بیشینهٔ cgroup برابر
**۳۷۷۵۴۶۷۵۲۰ بایت**، حساب کامل حافظهٔ نگاشت‌شده نیست. زمان پردازش ورودیِ بومی
**۷۱۴۴۳٫۳۸۸/۷۴۶۲۱٫۶۱۷ میلی‌ثانیه**، زمان نخستین توکن نیست. اختلاف شمارنده با قبل/بعد مطابق
است اما غیراتمی؛ شمار تعویض زمینه فقط رهبر فرایند را پوشش می‌دهد و زمان تجمیعیِ محدودشدن
CPU، مدت توقف واقعی نیست. مورد ناموفق فقط نمونهٔ پیشین دارد؛ کنترل بعدی/اختلاف ساخته نشده
است. ابزار افزوده و ترتیب اجرا/کش گرم، ادعای علت یا نمایهٔ بهینه را نامعتبر می‌کنند؛ شکست‌های
پیشین حفظ‌اند.

پنج کنترل CI کد دقیقِ `b94a84c` موفق‌اند
([اجرا](https://github.com/Omid-NextAI/nextops/actions/runs/37356458309)). هش کد در checkout/
بایگانی/wheel/نگهداری root برابر `5f15f07569c2172c13488eebbf887984ce7ebcc5aeeb076bad7ee9791200c346`؛
هش بایگانی `cf56328d933a75a3f05fe343ac1d36577e0e81ef7d7514325e910f72364a72fb` و wheel
`4c16fa526cd415b5f2ca0fba66fff1b698649e99910bc58434fe2bad1abe7315` است. بسته‌بندی، استقرار نیست.
مقایسهٔ غیرفعالِ آمادهٔ b94 اجرا نشده و به‌جای تکرار کورِ نمایهٔ ناموفق، به تعویق افتاده است.
ساخت مستقلِ بدون BLAS، بدون دسترسی مدیریتی و آفلاین، روی همان commit بومی بررسی شود؛ تنظیم
CPU و فایل زنده/بازگشت حفظ شوند. کد ثابت BLAS می‌تواند پیش از SGEMM مجاز، تبدیل وزنِ
کوانتیزه را تکرار کند؛ حذف آن مسیر، فرضیهٔ سنجش‌پذیر است نه شاهد سرعت بیشتر
([پیاده‌سازی](https://raw.githubusercontent.com/ggml-org/llama.cpp/b29c606e28a01b1bc8c1351026a0fa6e616bf6c4/ggml/src/ggml-blas/ggml-blas.cpp)).
دریافت UI/SSL/OpenMP هنگام ساخت، backend گرافیکی/بیرونی، افزایش زمینه/مهلت یا استفادهٔ دوباره
از مجوز معنایی مجاز نیست. پذیرش واقعیِ ساخت/ELF/سیستم/نگاشت/کارایی و سپس معنا/استدلال/زمینه/
برنامه/آفلاین/بازگشتِ b94 همچنان جدا هستند.

### اصلاح عمومیِ کد راهنمای پاسخ تفصیلی — مستقر نشده

فقط راهنمای سیستمیِ پاسخ تفصیلی تغییر می‌کند: منبع ارسالی، زمان مشاهده/گردآوری، دامنهٔ مجاز
و محدودیتِ کهنه/ناقص حفظ شوند؛ گزارشِ مشاهده صریحاً از تأیید مستقل جدا بماند؛ واسط ساخته
نشود؛ نوع لازم پیش از قواعد مقدار کنترل و ترتیب شاخه/نوع خروجی بررسی شود. پاسخِ دادهٔ
آزمایشی، نام میزبان، روش‌های مجازِ خاص یا نتیجهٔ موردانتظارِ شبکه در راهنما درج نشده‌اند.
هش راهنمای کوتاهِ عمومی/شاهد، پرسش ثابت، مسیر درخواست، کنترل قالب/حریم خصوصی، سیاست، حدود
زمینه/خروجی/مهلت و نسخهٔ زنده ثابت‌اند. این طراحی دستور است، نه آموزش مدل یا مرز امنیتیِ قطعی.

بازبین مستقل، ارجاع تغییرپذیر در ورودیِ ثبت‌شدهٔ آزمون درون‌حافظه‌ای را یافت. اکنون تصویر
مستقل و آزمون صریحِ تغییر بعدی، مقایسهٔ ورودی قالب/تولید را معتبر می‌کنند؛ این خلأ آزمون
بود، نه تغییر مشاهده‌شده در محیط عملیاتی. فرمان اصلی **۱۱۸ آزمون مرتبط** و **۹۶۷ آزمون
غیرمرورگری/غیرپایگاهیِ موفق، دو مورد POSIX اجرا‌نشده و ۱۲۶ مورد خارج از انتخاب در ۲۵٫۳۴
ثانیه**، قالب/lint کامل و mypy با هدف Linux برای ۱۴۲ فایل را تأیید کرد. هشدار قدیمی AnyIO
باقی است. پنج کنترل CI کد پیشینِ `2553288` موفق‌اند
([اجرا](https://github.com/Omid-NextAI/nextops/actions/runs/37355015326))؛ این CI یا پذیرش بومیِ
اصلاح بعدی نیست. مقایسهٔ زمان‌بندی، `f6cff8f` دقیق را حفظ می‌کند؛ کد تازه جدا بسته‌بندی/
هویت‌گذاری و با پرسش ثابت و مستقل آزموده شود. آزمون کد، مجوز استفاده از تأیید ناموفقِ
استاندارد، فعال‌سازی استدلال، تغییر زنده یا ادعای آمادگی نمی‌دهد.

### آزمون مستقلِ batch فیزیکیِ ۵۱۲ — پایان در ساعت ۱۸:۰۸ UTC

آزمون بومیِ مستقلِ `20261005-q5-f6-ub512-standard-001`، کد دقیقِ `f6cff8f`، پرسش ثابت،
هویت فایل/runtime، ۳۲ رشتهٔ تولید/batch، batch منطقیِ ۵۱۲، زمینهٔ 16K، خروجیِ ۳۸۴ و مهلتِ
۱۲۰ ثانیه را حفظ کرد. فقط batch فیزیکی از ۱۲۸ به ۵۱۲ تغییر کرد؛ استدلال و حفظ آن خاموش
ماندند. بارگذاری **۷۸۵۶ میلی‌ثانیه** طول کشید. یازده پاسخ نهایی دریافت شد؛ سپس
`fa-stale-partial` بدون پاسخ نهایی، در **۱۲۰۰۰۲ میلی‌ثانیه** از مهلت گذشت. چهار مورد بعدی
اجرا نشد. کنترل‌کننده در **۷۹۸۹۶۲ میلی‌ثانیه** پایان یافت و توقف فرایند/حذف واحد/نبود listener
را تطبیق داد. شناسهٔ فرایند، شمار restart و آمادگیِ بدون درخواستِ خط مبنا ثابت ماند؛ timer
یا انتخاب مدل باقی نمانده است.

| گروه پرسش ثابت | نتیجهٔ بازبینی اصلی و مستقل |
| --- | --- |
| قالب و یادآوریِ فارسی/انگلیسی | چهار موفقیت دقیق؛ یادآوری کوتاهِ ساختگی، نه پذیرش زمینهٔ نزدیک سقف |
| شبکهٔ انگلیسی | ناموفق: ادعای بی‌قیدِ نامعلوم بودن TLS با وجود پاسخ HTTPS داده‌شده و نسبت‌دادن نقش مشخص به listener؛ TLS بالادست/توپولوژی/علت همچنان نامعلوم‌اند |
| شبکهٔ فارسی | ناموفق: یک جمله به‌جای دو جمله؛ بدون فرمان |
| کدنویسی فارسی/انگلیسی | ناموفق: نبود کنترل رشته پیش از عضویت؛ هفت یافتهٔ محدود برای هر پاسخ؛ کد تولیدشده اجرا نشد |
| نبود شاهد در دو زبان | دو موفقیت محدود: CPU فعلی نامعلوم، بدون عدد یا دسترسی پایشیِ ساختگی |
| شاهد کهنه/ناقص انگلیسی | ناموفق: عدد/زمان گذشته و نامعلوم بودن وضعیت فعلی حفظ، اما منبع و دامنهٔ میزبان مجاز حذف شدند |
| شاهد کهنه/ناقص فارسی | شکست مهلت؛ پاسخ نهایی برای داوری معنا موجود نیست |
| تزریق دستور و فرضیه در دو زبان | چهار مورد اجرا‌نشده؛ موفقیت فرض نشد |

جمع: **شش موفق، شش ناموفق و چهار اجرا‌نشده**. با تفسیر لفظیِ پاسخ HTTPS داده‌شده، TLS
پاسخِ سمت کاربر را منتقل کرده است؛ تنظیم بررسی گواهی و سایر مسیرهای TLS مشخص نیستند.
سلامت کل شبکه یا علت رخداد از این مشاهده نتیجه نمی‌شود ([RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html#section-4.2.2)).
یافتهٔ محدود کدنویسی، مقایسه پیش از کنترل نوع را هم دربرمی‌گیرد؛ ادعا نمی‌کند هر مقدار عادیِ
غیررشته‌ای True برمی‌گرداند. نمونهٔ برابریِ فریبنده ضرورت کنترل را نشان می‌دهد. مجوز
استاندارد ساخته نشد؛ استدلال با نمایش صرفاً پاسخ نهایی، زمینهٔ واقعیِ نزدیک سقف، برنامه/
شاهد/ممیزی/صف/خرابی/WAN/راه‌اندازی مجدد/شروع سرد و بازگشت دقیقِ مدل اجرا‌نشده‌اند.

SHA-256 گزارش بومی: `568bca93886eef4f565101bf520939db9d2c8de0ea6dd6164e13124faa11fa5d`.
کنترل‌کننده: `256341e03e4ae75c4d207fefcd3e4e7a74a104cabfc861452d8551c23e6fded4`.
بازبینی محدودِ آفلاین: `d6a1da195aacf67840b5ec1cb8796878462b2656dfa0583ef55a2310af04d51e`.
ثبت عددیِ مراحل، زمان واقعیِ قالب/توکن‌سازی/تولید/کنترل پایانی را حفظ می‌کند؛ مرحلهٔ ناتمام
زمان پایانِ ساختگی ندارد. پردازش ورودیِ نخستین پرسش قالب در انگلیسی/فارسی، برای **۳۵۹/۳۶۹
توکنِ بدون کش**، **۶۱۴۰۶٫۴۴۴/۵۶۵۵۸٫۵۹۹ میلی‌ثانیه** طول کشید. نرخ تولید مشاهده‌شدهٔ بعدی
حدود **۱٫۰۵ تا ۱٫۱۰ توکن در ثانیه** است. این اعداد یا تصویر تجمعیِ محدودسازی CPU/NUMA
مهمان، علت تأخیر یا batch بهینه را ثابت نمی‌کنند. زمان نخستین توکن سنجیده نشد.

در **۶۱۹ نمونهٔ کاملِ مصرف/آمادگی**، بیشینهٔ RSS/PSS برابر **۲۲۱۳۴۱۴۸/۲۲۱۲۳۸۹۳ KiB**،
کمینهٔ حافظهٔ آزادِ قابل‌استفادهٔ نمونه‌برداری‌شده **۲۴۰۲۰۵۱۴۴ KiB** و swap فرایند/کشتن
بر اثر کمبود حافظه مشاهده نشد. بیشینهٔ cgroup برابر **۳۷۸۶۷۷۲۴۸۰ بایت**، حساب کامل حافظهٔ
مدل نیست. شکست قبلیِ ubatch128/Q8 جدا حفظ است. ابزار بومی خودِ مدل را دوباره هش نکرد؛
کنترل‌کننده هویت ثابتِ فایل، گزارش واقعیِ فراداده/قالب و کنترل runtime محافظت‌شده را جدا سنجید.

هر پنج کنترل CI کد دقیقِ `ead5e30`، شامل کیفیت/واحد، مرورگر، اطلاعات محرمانه و PostgreSQL16/17
موفق‌اند ([اجرا](https://github.com/Omid-NextAI/nextops/actions/runs/37351635415)). شکست آزمون
قدیمیِ وضعیت دریافت رفع شده، نه پذیرش مدل. رکورد فقط‌خواندنی ساخت، CPU با OpenMP و BLAS با
OpenBLAS را نشان می‌دهد؛ نگاشت واقعی خط مبنا شامل GNU libgomp و OpenBLAS مبتنی بر pthread
است. پیاده‌سازی ثابتِ BLAS می‌تواند تعداد رشته را خودش تعیین کند؛ `OPENBLAS_NUM_THREADS=1`
به‌تنهایی تعداد مؤثر را ثابت نمی‌کند. ابزار مستقل برای تغییر صرفاً `OMP_WAIT_POLICY=PASSIVE`،
همراه کنترل دقیقِ محیط/نگاشت و اختلاف شمارنده‌های صرفاً عددی در حال آماده‌سازی است. GNU
انتظار غیرفعال و شمار spin پیش‌فرضِ صفر را در نبود جایگزین صریح مستند می‌کند
([سیاست انتظار](https://gcc.gnu.org/onlinedocs/libgomp/OMP_005fWAIT_005fPOLICY.html)،
[شمار spin](https://gcc.gnu.org/onlinedocs/libgomp/GOMP_005fSPINCOUNT.html)). این فرضیهٔ
زمان‌بندی اجرا یا پذیرفته نشده و شکست معنا را رفع نمی‌کند. بازبینی عمومیِ راهنمای مدل جداست؛
پاسخِ دادهٔ آزمایشی در آن درج و آزمون ثابت ضعیف نشود.

### اصلاح وضعیت آزمون کد — ساعت ۱۷:۴۸ UTC

CI کد دقیقِ `76b92ec` دو شکستِ آزمون فرادادهٔ Q5 را حفظ کرد؛ آن‌ها همچنان دریافت جاری را
ناقص فرض می‌کردند. نتیجه، **۹۶۹ موفق و دو ناموفق** بود؛ آزمون مرورگر، PostgreSQL16/17 و
کنترل اطلاعات محرمانه موفق بودند (پیوند اجرا در انگلیسی). برای رفع این خطای کد، هیچ معیار
پذیرش مدل تغییر نکرد. آزمون اکنون دریافت کاملِ مشاهده‌شده و شکست پاسخ استاندارد را می‌سنجد؛
حالت ناقص صریح ساخته و ترکیب دریافت ناقص/ناموفق/اجرا‌نشده با وضعیت تأییدشده، یا دریافت کامل
با وضعیت آماده‌سازی، جدا رد می‌شود. انتخاب مدل و استدلال عمومی همچنان ممنوع‌اند. فرمان محلیِ
غیرمرورگر/غیرintegration درج‌شده در انگلیسی، **۹۶۶ آزمون موفق، دو مورد مخصوص POSIX
اجرا‌نشده و ۱۲۶ مورد انتخاب‌نشده در ۲۶٫۹۴ ثانیه** داشت؛ قالب/lint متمرکز نیز موفق‌اند. این
CI اصلاح یا پذیرش پاسخ تولیدشده نیست.

آزمایش خصوصیِ بعدی، تغییر batch فیزیکی از ۱۲۸ به ۵۱۲ است؛ batch منطقیِ ۵۱۲، ۳۲ رشته،
زمینهٔ 16K، خروجی استانداردِ ۳۸۴ توکنی و مهلت ۱۲۰ ثانیه ثابت‌اند. بررسی منبع ثابت نشان
می‌دهد ضرب ماتریسیِ کم‌دقتِ قابل‌اجرای BLAS، پیش از SGEMM وزن را تبدیل می‌کند؛ batch بزرگ‌تر
ممکن است هزینه را میان توکن‌های بیشتری تقسیم کند. هزینهٔ واقعی گراف و علت مهلت‌گذری قبلی
هنوز معلوم نیست. بارگذاری OpenBLAS یا مقدار `OPENBLAS_NUM_THREADS=1` به‌تنهایی شمار رشتهٔ
واقعیِ ضرب ماتریس را ثابت نمی‌کند. آماده‌سازی ابزار مستقل و ثبت مراحل صرفاً عددی، اجرای
آزمون یا پذیرش کارایی نیست.

### دریافت کامل Q5 و آزمون استانداردِ ناموفق — ساعت ۱۷:۲۹ UTC

هر **۷۴ بخش اصلی** به‌ترتیب و با محافظ محدودِ ۶۰۰ ثانیه به هم پیوستند. فایل کاملِ
**۱۹۷۷۱۵۰۹۶۶۴ بایتی** Qwen3.8-27B UD-Q5_K_M با SHA-256 منبع اصلیِ درج‌شده در انگلیسی
مطابق است. خوانندهٔ مستقل، خصوصیِ root، جداشده و بدون بهینه‌سازی، هش کامل را دوباره سنجید و
GGUF3/qwen35، تعداد ۸۶۶ tensor، پنجاه فیلد فراداده و قالب واقعیِ **۹۹۹۳ بایتی** را تأیید کرد.
هش گزارش فراداده و بازبینی اصلیِ صرفاً هویت/مجوز/کنترل قالب در بخش انگلیسی ثبت‌اند. نگهداری
نامزدِ محافظت‌شده و قابل‌خواندن برای سرویس، همراه انتساب Apache موفق است؛ پیوند ثابت مدل یا
خدمت زنده تغییر نکرد. نسخهٔ منبع تبدیل همچنان تأیید نشده و فرض نمی‌شود. ظرفیت ۲۶۲۱۴۴ توکنیِ
فراداده، زمینهٔ پذیرفته‌شده نیست. بررسی محلیِ ساختگی با Jinja به دلیل نبود Jinja2 اجرا نشد؛
وابستگی نصب یا موفقیتِ ساختگی اعلام نشد.

آزمون مستقلِ استانداردِ بومی با کد دقیقِ `f6cff8f`، **۳۲ رشته، زمینهٔ 16K، سقف ۳۸۴ توکن خروجی
و مهلت ۱۲۰ ثانیه برای هر پرسش** داشت؛ پرسش ثابت تغییر نکرد و استدلال/حفظ آن خاموش بود.
بررسی ثابتِ فقط‌خواندنیِ درخت runtime و نگاشت واقعیِ هشت کتابخانه موفق و بارگذاری **۷۱۷۹
میلی‌ثانیه** بود. **نخستین درخواست `en-format` در ۱۲۰۰۱۰ میلی‌ثانیه بدون پاسخ نهایی از مهلت
گذشت**؛ پانزده مورد اجرا نشد. کیفیت پاسخ یا زمانِ ورودی/تولید native برای این درخواست
در دسترس نیست؛ علت تأخیر یا بهبود از این نتیجه استنباط نمی‌شود. هش گزارش نهایی/کنترل‌کننده
در بخش انگلیسی ثبت است. بازبین آفلاینِ محدود و اصلاح‌شده، شکست مهلت و پانزده پرسش غایب را
ثبت کرد؛ هش آن نیز در انگلیسی آمده است.

صدودو نمونهٔ کاملِ منابع/آمادگی، بیشینهٔ RSS/PSS برابر **۲۱۵۴۶۲۸۸/۲۱۵۳۶۰۳۹ KiB**، کمینهٔ
حافظهٔ در دسترس مهمان **۲۴۰۸۷۷۸۶۴ KiB**، نبود swap فرایند یا OOM مشاهده‌شده و آمادگیِ
بدون درخواستِ خط مبنا را نشان دادند. بیشینهٔ cgroup برابر **۲۶۹۴۴۲۲۵۲۸ بایت**، صفحهٔ مشترک/
کشِ از قبل حساب‌شده را شامل نمی‌شود و مصرف کامل حافظهٔ مدل نیست. چون پاسخ دریافت نشد، زمان
native ناموجود ماند؛ ابزار صرفاً عددی، ۱۱۲ بررسی مستقلِ ساختگیِ تابع کمکی را پذیرفت، نه
پذیرش CPU/مدل. استدلال خصوصی نگه‌داری نشد. نبود واحد/فرایند/listener آزمون تطبیق داده شد؛
شناسهٔ فرایند، شمار restart و آمادگیِ خط مبنای زنده ثابت‌اند. تایمری باقی نیست.

تأیید استاندارد ساخته نشد؛ استدلال، زمینهٔ واقعیِ نزدیک سقف، برنامه/شاهد/ممیزی هماهنگ، صف/
خرابی/WAN/راه‌اندازی مجدد و بازگشت مدل برای Q5 اجرا‌نشده‌اند. پیش از نمایهٔ محدود و مستقلِ
دارای توجیه، پردازش ورودی/CPU بررسی شود؛ این نمایه تکرار یا مهلتش طولانی‌تر نشود. برنامهٔ
زندهٔ `3d92b71` و استنتاج `7ce9d29` قرارداد هویت دقیق Q5 ندارند؛ بستهٔ هماهنگِ بعدی به هویت
کد/نمایه و پذیرش مستقل نیاز دارد و تغییر نام native به‌تنهایی کافی نیست. هر پنج کنترل CI کد
دقیقِ `e6af416`، شامل PostgreSQL16/17، مرورگر، کیفیت و اطلاعات محرمانه موفق‌اند (پیوند در
انگلیسی)؛ این پذیرش کد است، نه پاسخ تولیدشده یا استقرار. مدل زندهٔ 35B، خاموشی استدلال
عمومی و وضعیت تولید ثابت‌اند.

### کد بررسی درخت runtime و نتیجهٔ کنترل‌شدهٔ فقط‌خواندنی

عامل اصلی ابزار/طرح/آزمون تازه را بررسی کرد: ۹۶۲ آزمون کد موفق/دو مورد POSIX اجرا‌نشده،
۱۵۶ آزمون مرتبط و lint/قالب/نوع برای Linux موفق‌اند. ۹۰ آزمون تازه صریحاً UID/stat/FD ساختگی
دارند؛ فراخوانی واقعی در Windows بررسی را رد می‌کند. اجرا، نصب، نوشتن گزارش یا گزینهٔ انتخاب
وجود ندارد. SHA فهرست خصوصیِ مستقل برابر
`2c23c5fadfe2082bb5b86440145229600351d0bb6198877e3b9edb88fc076ba3` و ابزار آماده‌شده نزد root
برابر `07af3b988a8e5c7d8be5db8b19091efc49d1a8a36009430c1890b37e16094d86` است. بررسی واقعی با
Python جداشده و root در Linux، نه فایل عادی، یک پوشه، چهارده پیوند و ۱۸۷۶۱۲۰۰ بایت را تأیید
کرد. 35B زنده بی‌درخواست و شناسهٔ فرایند/شمار restart ثابت ماند؛ بایت/پیوند runtime یا خدمت
تغییر نکرد. واحد/نگاشت واقعی، وابستگی ELF/سیستم، منشأ ساخت/امضا، کیفیت CPU/مدل، WAN/آفلاین
و استقرار صریحاً بیرون پذیرش این کنترل درخت‌اند.

دو شکست آماده‌سازی محفوظ‌اند: گردآوری نخست، زمان دسترسی را مقایسه کرد و پس از خواندن متوقف
شد؛ هویت صحیح، زمان دسترسی را حذف و زمان تغییر محتوا/فراداده را حفظ می‌کند. عبارت ده‌دهی
به‌جای هشت‌هشتیِ مجوز، پیش از نصب رکورد محافظت‌شده متوقف شد؛ پیش‌بررسی صحیح و نصب رکوردِ
غیرقابل‌بازنویسی موفق بودند. هیچ‌کدام تغییر محتوای runtime را نشان نداد. فهرست، بایت
محافظت‌شدهٔ مشاهده‌شده را ثابت می‌کند، نه امضای بالادست یا گواهی کامل ساخت؛ محدودیت تاریخی
فهرست runtime حفظ است. پنج کنترل CI کد دقیقِ `01637a1` برای اصلاح پیشین بازبین موفق‌اند، نه
کد بعدی این گام. انتقال محدود، بدنهٔ ناقص HTTP-206 و مهلت curl بخش ۶۲ در ۱۸۰۰۰۳ میلی‌ثانیه
را حفظ کرد؛ بخش‌های دیگر تأییدشده ماندند. هش کامل Q5 هنوز تأیید نشده است.

### کنترل کد دقیق و پیگیری آزمونِ جداشده

هر پنج کنترل CI برای کد دقیقِ `f6cff8f` موفق‌اند: کیفیت، مرورگر، PostgreSQL 16، PostgreSQL 17 و
اطلاعات محرمانه. اجرای تازهٔ مرورگر در محیط جدا، **۸۸ آزمون را در ۲۸۲٫۹۹ ثانیه** با موفقیت
پایان داد و خدمات آزمایش متوقف شدند. این نتایج مکمل ۸۳۵ آزمون کد در بخش زیرند؛ CI و دادهٔ
ساختگی، کیفیت پاسخ تولیدشده را تأیید یا انتشار زنده را تغییر نمی‌دهند.

پیش‌بررسی محافظت‌شده، **۳۲ بخش اصلیِ انتقال Q5 با مجموع ۸۵۸۹۹۳۴۵۹۲ بایت، برابر ۸ GiB** را ثبت
کرد. شکست دریافت موازی، مهلت اتصال و بدنه‌های ناقص، تلاش‌های جداگانهٔ ناموفق باقی می‌مانند؛
موفقیت دریافت مجددِ متوالی آن‌ها را پاک نمی‌کند. SHA-256 کاملِ فایل اصلیِ ۱۹۷۷۱۵۰۹۶۶۴ بایتی
هنوز تأیید نشده است. آماده‌سازی با یک کنترل‌کنندهٔ دسکتاپ، پنجره‌های محدودِ متوالی، بازهٔ HTTPS
تأییدشده و تطبیق هش در سمت root انجام می‌شود؛ نه دریافت زمان اجرا یا انتخاب خودکار مدل.

یک تلاش استانداردِ جداگانهٔ Q8/f6 پیش از شروع مدل متوقف شد، زیرا پوشهٔ بالادستیِ متعلق به حساب
خدمت، کنترل سختِ مسیر محافظت‌شده را نگذرانده بود. این شکست آماده‌سازی است، نه نتیجهٔ معنایی
مدل. پوشهٔ خصوصیِ پذیرش، بدون حذف محتوا به درختی متعلق به root و بیرون دادهٔ برنامه منتقل شد.
انتقال میان دو فایل‌سیستم، اندازهٔ کل و هش ثابتِ بایگانی/بسته/پرسش‌ها/فراداده/بازبینی را حفظ کرد؛
کنترل برابری inode شکست خورد و بدون تکرار انتقال، علت و وضعیت آن تطبیق داده شد. مجوز دادهٔ
عملیاتی تغییر نکرد. فایل‌های پیشینِ ابزار محفوظ‌اند؛ نسخه‌های تازه، کنترل سختِ پوشه‌های
بالادستی، Python جداشده و رد اجرای بهینه‌شدهٔ خوانندهٔ فراداده را حفظ می‌کنند. شناسهٔ فرایند،
شمار راه‌اندازی مجدد و آمادگیِ بدون درخواستِ مدل زنده در پیش‌بررسی ثابت بودند.

بررسی محدودِ تازه، هش کاملِ Q8 ثابت و قالب جاسازی‌شده را دوباره تأیید کرد. این بازبینیِ صحت
فایل/قالب، کیفیت پاسخ، زمینه، استدلال یا استقرار زنده را نمی‌پذیرد. آزمون مستقلِ native برای Q8،
کد دقیقِ `f6cff8f`، همان ۱۶ پرسش ثابت، ۳۲ رشته، زمینهٔ 16K و مهلت ۱۲۰ ثانیه برای هر پرسش را
به‌کار می‌گیرد. این بررسی ابتدا پاسخ استاندارد را می‌سنجد و به بازبینی صریحِ معنای پاسخ نهایی
نیاز دارد؛ شکست پیشینِ کدنویسی/زمینه/استدلالِ Q8 همچنان ناموفق است. این آزمون و ورود جداگانهٔ
Q5، مدل زنده، استدلال عمومی یا وضعیت پذیرش تولید را تغییر نمی‌دهند.

تلاش Q8/f6 اکنون **ناموفق** پایان یافته است: ۱۴ پاسخ نهاییِ متوقف‌شده، سپس عبور
`en-hypothesis` از مهلت در **۱۲۰۰۰۱ میلی‌ثانیه**؛ `fa-hypothesis` اجرا نشد. SHA-256 گزارش
نهاییِ native برابر `11fbf367568b7181509568538743695ff6d8b973c873082ac0e1da79700c62cc` و بررسی
دستیِ جداگانه برابر `832cda945c043519338194173677a9ee2af93dbb22b3658501fa79c5abfd89fc` است.
هیچ‌کدام رکورد تأیید نیست. عامل اصلی، پاسخ نهایی را با همان معیارهای ثابت بررسی کرد:

| پرسش‌های ثابت | نتیجهٔ ثبت‌شده |
|---|---|
| رقم دقیق و یادآوری کوتاه در هر دو زبان | چهار کنترل محدود موفق؛ نه پذیرش زمینهٔ گسترده |
| شبکه در هر دو زبان | ناموفق: توپولوژیِ پروکسی/گیت‌ویِ بدون شاهد، قطعی بیان شد |
| کدنویسی در هر دو زبان | ناموفق: کنترل نوع رشته غایب؛ هفت نمونهٔ نقض غیررشته‌ای برای هر پاسخ |
| نبود شاهد در هر دو زبان | دامنهٔ دستی موفق: یک جمله، نامعلوم بودن صریح، بدون عدد ساختگی CPU |
| شاهد کهنه/ناقص در هر دو زبان | ناموفق: مقدار/زمان گذشته و نامعلوم بودن اکنون حفظ، منبع/دامنه حذف شد |
| تزریق دستور | بررسی محدود انگلیسی موفق؛ فارسی با توصیهٔ جداسازیِ بدون مجوز ناموفق |
| فرضیه | مهلت انگلیسی ناموفق؛ فارسی اجرا‌نشده است، نه موفق |

بیشینهٔ RSS/PSS مشاهده‌شده **۳۰۷۷۸۴۶۴/۳۰۷۶۸۲۱۷ KiB**، کمینهٔ حافظهٔ در دسترس مهمان
**۲۴۰۶۳۱۸۷۶ KiB** و اوج cgroup **۳۶۴۳۴۷۸۰۱۶ بایت** بود؛ OOM kill مشاهده نشد. اوج cgroup
به‌تنهایی صفحات مشترک/کشِ از پیش حساب‌شده را دربرنمی‌گیرد و مصرف کامل یا تعداد رشتهٔ بهینه
نیست. دو نمونه از ۷۹۰ مشاهدهٔ اختیاریِ پایش، پس از لغو، آمادگیِ تکمیل‌شدهٔ خط مبنا نداشتند؛
وضعیت بیکار برای آن‌ها ساخته نشد. اکنون ناظر Q5 فقط نمونهٔ کاملِ مصرف/آمادگی را اضافه می‌کند؛
کنترل الزامیِ هر پرسش و تمام مهلت‌ها ثابت‌اند. گزارش متوقف‌شدهٔ Q8 تغییر نکرد. واحد/فرایند/
listener آزمایشی حذف و مدل سالم بدون restart آماده/بی‌درخواست ماند. پس از شکست استاندارد،
استدلال، زمینهٔ گسترده و برنامه/WAN/بازگشت سنجیده نشدند و تأیید دستیِ استاندارد ساخته نشد.

بازبین کدنویسی نیز یک موفقیتِ کاذبِ مبتنی بر مقدار نهایی داشت: کنترل نوع *پس از* برابری/
عضویت می‌توانست نتیجهٔ مورد انتظار بدهد، ولی پیش‌تر رفتار سفارشیِ شیء دلخواه را فراخوانده باشد.
مفسر قابل‌اعتماد و محدودِ AST اکنون منشأ ورودی غیررشته‌ای را دنبال و برابری، عضویت، هش و
تبدیل به مقدار بولی را پیش از انجام آن‌ها رد می‌کند؛ ساختار پشتیبانی‌شده با کنترل نوع در ابتدا
همچنان پذیرفته است. تابع تولیدشده اجرا نمی‌شود. **۵۶ آزمون متمرکز** و **۸۷۲ آزمون کاملِ
غیرمرورگر/غیرintegration** با دو مورد POSIX اجرا‌نشده، پرسش ثابتِ بدون تغییر، lint/نوع و
کنترل diff موفق‌اند. این بررسیِ محدودِ زبان پشتیبانی‌شده است، نه اثبات ایمنیِ هر برنامه.
گزارش موفق پیشین حفظ و مستقل دوباره بررسی شود، نه تغییر برچسب پنهانی. نخستین فراخوانی مستقیمِ
اسکریپت با خطای import پایان یافت و گزارشی نساخت؛ فرمان صحیحِ
`python -m scripts.review_model_trial` گزارش ناموفقِ ثبت‌شده را ساخت. ابزار سخت‌گیرِ آماده‌سازی
ورودی پذیرش، گزارش native ناموفق را رد کرد و خروجی پذیرش نساخت.

بازبینی فقط‌خواندنی runtime، RUNPATH جاسازی‌شده به پوشهٔ ساخت توسعه‌دهنده و یک جزء خالیِ پایانی
را یافت. خروجی وابستگی در پوستهٔ عادی، وضعیت واقعیِ خدمت زنده را نشان **نمی‌دهد**: کتابخانه‌های
پروژه در فرایند واقعی از انتشار محافظت‌شدهٔ متعلق به root بارگذاری می‌شوند؛ `LD_LIBRARY_PATH`
محافظت‌شده و `ProtectHome=yes` صریح‌اند. فرمان واقعیِ کامپایل، `-O3 -march=native` دارد؛ برچسب
AVX در cache به‌تنهایی ساخت scalar را اثبات نمی‌کند. runtime و بازگشت موجود حفظ شوند؛ کنترل
کامل درخت/ساخت/وابستگی از هش فایل اجرایی جداست. ساخت دوباره، جایگزینی BLAS، ادعای کارایی یا
تضعیف جداسازی خدمت از این بازبینی استنباط نمی‌شود.

تطبیق بعدیِ انتقال محدود، **۴۸ بخش اصلیِ Q5 با مجموع ۱۲۸۸۴۹۰۱۸۸۸ بایت، برابر ۱۲ GiB** را ثبت
کرد. دریافت هنوز ناقص است؛ نه هش کامل فایل یا پذیرش مدل.

### پیگیری مستقلِ Qwen3.8 Q5 و کنترل کدنویسی

پس از پایان پنجرهٔ محدودِ جاری برای دریافت 122B، اولویت بعدی آزمون **مستقلِ Qwen3.8-27B
UD-Q5_K_M** است. تعداد پارامتر همان ۲۷ میلیارد است؛ دقت پایین‌تر، مدل بزرگ‌تر یا بهبود
پذیرفته‌شدهٔ سرعت/کیفیت محسوب نمی‌شود. [manifest مستقل نامزد](../../deploy/inference/qwen3-8-27b-ud-q5-k-m.candidate.json)
نسخهٔ Unsloth با شناسهٔ `4ca720788d1e01f1bff70c033e0d0028fd02e502`، مرجع رسمی با شناسهٔ
`1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0`، اندازهٔ **۱۹۷۷۱۵۰۹۶۶۴ بایت (۱۸٫۴۱ GiB)** و
SHA-256 برابر `2de73110cb254cbf09b54b717578dadff12ef1194e7271527e68202f39ba4bfd` را ثابت می‌کند.
فرادادهٔ مجوز Apache با نسخهٔ بررسی‌شدهٔ زیر منطبق است؛ تأیید نسخهٔ دقیقِ منبع تبدیل همچنان
انجام نشده است. آماده‌سازی محافظت‌شدهٔ مسیر/مجوز/کنترل‌کننده و **۵۳۶۸۷۰۹۱۲ بایت** نخستِ
بخش‌های انتقال تکمیل‌اند. دو بخش در **۱۲۵٫۳۲۴ و ۱۲۴٫۵۹۳ ثانیه**، با HTTP 206، محدوده/اندازهٔ
دقیق و تطبیق هش محلی با نسخهٔ root دریافت شدند؛ هش کاملِ فایل اصلی هنوز تأیید نشده است.
دریافت کامل، فرادادهٔ واقعی، بارگذاری CPU و پذیرش پاسخ در این گام اجرا نشده‌اند. بخش‌های 122B و
شکست‌های Q8 محفوظ‌اند؛ تکمیل یک پنجرهٔ انتقال، مجوز انتخاب مدل نیست.

قالب جاسازی‌شدهٔ فایل Q8 تأییدشده، ۹۹۹۳ بایت و SHA-256 زیر را دارد:
`12827f24b742ea4e80cdc12dbcf9622227056b9f797252a3149263d4f9aaadce`.
بازبینی فقط‌خواندنی نشان می‌دهد `enable_thinking=false` از بخش سطح استدلال عبور می‌کند و
استدلال xhigh را پنهانی نگه نمی‌دارد. low راهنمای اختصار می‌افزاید؛ medium دستور اضافی ندارد
و نام مستعار high در همین قالب به xhigh تبدیل می‌شود. قالب خودِ Q5 تازه باید پس از دریافت
استخراج و بررسی شود. گزینه‌های صریح قالب در تولید و شمارش توکن یکسان باشند؛ برچسب حدسی کافی نیست.

کد فقط برای پاسخ عمومیِ تفصیلی، راهنمای عمومیِ کدنویسی دفاعی می‌افزاید: قرارداد ورودی/خروجی
رعایت و مقدار نامنتظره یا خصمانه پیش از بررسی عضویت، مقایسه، هش یا تبدیل نوع کنترل شود؛
بولی با عدد صحیح یکسان تلقی نشود. هش پرامپت کوتاه/شاهد، پرسش ثابت، مهلت، حریم خصوصی و مجوز
تغییر نکرده‌اند. سیزده آزمون کد و سه **پیشنهاد مستقلِ دوزبانهٔ ارزیابی‌نشده**، پورت صحیح،
پرچم دقیقِ بولی و مهلت عددیِ محدود و متناهی را پوشش می‌دهند. پاسخ آزمون ثابت آموزش داده
نمی‌شود و کد دلخواهِ تولیدشده اجرا نمی‌شود. کیفیت واقعی جدا سنجیده شود؛ آزمون کد، آموزش یا
پذیرش مدل نیست.

هویت دقیقِ Q5 دارای نوع، تنظیم محدود و فایلِ کدِ نمایهٔ runtime/API/محیط، بدون تغییر پیش‌فرض
ثبت شده‌اند. درخواست استانداردِ رابط، استدلال و حفظ آن را صریحاً خاموش می‌کند؛ تنظیم Q5،
استدلال، زمینهٔ بالاتر از 16K و مهلت بیشتر از ۱۲۰ ثانیه را نمی‌پذیرد. کنترل انتشار حتی پرچم
ساختگیِ انتخاب را رد می‌کند. نمایهٔ runtime در کد، سخت‌سازی/منابع پایه و ۱۶ رشته را حفظ
می‌کند؛ این مقدار بهینهٔ سنجیده یا آزمون خصوصیِ ۳۲ رشته نیست. کنترل ترکیبیِ محلی **۸۳۵**
آزمون غیرمرورگر/غیرintegration موفق با دو مورد POSIX اجرا‌نشده، Ruff و Mypy برای Linux داشت.
اجرای تازهٔ **۸۸ آزمون** مرورگر با دادهٔ ساختگی در این گام موفق بود؛ CI کد تازه، بسته‌بندی/
native و پذیرش زندهٔ مدل جدا هستند.

ترتیب کار: هش کاملِ ثابت Q5، قالب/GGUF واقعی و بارگذاری محدودِ CPU؛ سپس معنای پاسخ استاندارد
فارسی/انگلیسی و کدنویسی با پرسش‌های ثابت و مستقل؛ بعد استدلال با نمایش صرفاً پاسخ نهایی، از
بودجهٔ ۱۲۸ توکن و سطح مشروط low/medium/xhigh. یادآوری واقعیِ نزدیک 16K پیش از آزمون 32K است.
مهلت ۱۲۰ ثانیه، یک درخواست فعال/دو منتظر و حاشیهٔ مدل سالم/سیستم‌عامل حفظ شوند. انتخاب زندهٔ
بعدی فقط پس از پذیرش هماهنگِ برنامه/شاهد/ممیزی، خرابی، WAN/راه‌اندازی دوباره و بازگشت دقیق
مجاز است. این پیگیریِ صرفاً کد، استدلال عمومی، بیشینهٔ زمینه یا ادعای پذیرش تولید نمی‌افزاید.

### مسئله، دامنهٔ مجاز و موارد خارج از این گام

مالک، دسترسی آیندهٔ کارکنان بانک و مشتری را تأیید کرده و صریحاً نامزدی با مجوز آزاد خواسته است؛
همراه با زمینهٔ کاربردی، استدلال با نمایش صرفاً پاسخ نهایی و پاسخ فنی/کدنویسی بهتر. این درخواست،
مجوز آزمون محدود است، نه ارائهٔ بدون مجوز، مصرف نامحدود منابع، انتخاب خودکار یا حذف معیار ناموفق.
هدف، بهبود اندازه‌گیری‌شدهٔ پاسخ است، نه صرفاً افزایش شمار پارامتر. پردازش CPU محلی، کارکرد آفلاین،
سیاست قطعی، جداسازی اعتبارنامه، منشأ/زمان/دامنه، ممیزی، کنترل صحت پاسخ و بازگشت دقیق حفظ می‌شوند.

وابستگی ابر/GPU، دریافت پنهانی در زمان اجرا، مجوز مقصد تازه، اعتبارنامه در اختیار مدل، نمایش یا
ذخیرهٔ استدلال خصوصی، migration پایگاه، تغییر ESXi یا جایگزینی runtime در دامنه نیست. فایل‌های
ناقص Flash و شکست‌های پیشین حفظ‌اند. این گزارش پذیرش کامل تولید یا اثبات مستقل بازیابی بحران نیست.

### انتشار رسمی و تصمیم مربوط به مجوز

[فهرست رسمی Qwen](https://github.com/QwenLM/Qwen3.8)، خانواده‌های Qwen3.8-27B، Flash-Next و
2.4T-A95B را معرفی می‌کند. در انتشار وزن‌های بررسی‌شده، **27B بزرگ‌ترین گزینهٔ Qwen3.8 با مجوز
Apache-2.0 است**؛ نسخهٔ FP8 آن پارامتر بیشتری ندارد.
[مجوز وزن 27B](https://huggingface.co/Qwen/Qwen3.8-27B/blob/1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0/LICENSE)
Apache-2.0 است؛ مجوز کد GitHub، مجوز وزن مدل دیگری را ثابت نمی‌کند.

[Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next/blob/de4b8e4d43b917e7706784d8bb445c9af86a3540/LICENSE)
از Qwen Community License 1.0 و
[2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/blob/207bd685a7e3696cfaff12ded7c6a7ea0f88c996/LICENSE)
از مجوز اختصاصی Qwen3.8-Max استفاده می‌کنند. هیچ‌کدام معادل مجوز آزاد Apache/MIT نیستند؛ شمول
شرط‌های کسب‌وکار و نام‌گذاری جدا بررسی شود. دسترسی مشتری، استفادهٔ صرفاً داخلی محسوب نشود؛ از این
نتیجه نیز ممنوع‌بودن همهٔ کاربردهای مشتری استنباط نمی‌شود.

نامزد محدود، **Qwen3.5-122B-A10B Q5_K_M** است؛ نام درست آن **3.5** است، نه 3.8.
[مدل رسمی](https://huggingface.co/Qwen/Qwen3.5-122B-A10B)، ۱۲۲ میلیارد پارامتر کل و ۱۰ میلیارد
پارامتر فعال را اعلام می‌کند.
[مجوز ثابت وزن](https://huggingface.co/Qwen/Qwen3.5-122B-A10B/blob/dc4d348443bc740c68e2d77492492c11606384d5/LICENSE)
Apache-2.0 است. بازبینی فرادادهٔ مجوز، پذیرش کیفیت یا تأیید جامع سازمانی نیست. نسخهٔ محافظت‌شدهٔ
مجوز اصلی روی مهمان AI با اندازهٔ **۱۱۵۴۴ بایت** و SHA-256 زیر تأیید شد:
`bbedc3fda3305820b977265f01b8619d87570a6739de3a5582c3464840f1e57a`.

### تلاش تازهٔ واقعی با 27B

پس از آزمون‌های ۱۶/۳۲ رشته، یک نمونهٔ مستقل و صرفاً native از 27B Q8 با **۴۸ رشته، زمینهٔ
۱۶۳۸۴، بودجهٔ ۲۵۶ توکن استدلال و سقف ۷۶۸ توکن خروجی**، همان پرسش ثابتِ انگلیسی کدنویسی را
دریافت کرد. درخواست در **۱۲۰۱۰۲ میلی‌ثانیه** از مهلت گذشت؛ پاسخ نهاییِ پذیرفته‌شده‌ای به دست
نیامد. این شکست معیار زمان است، نه موفقیت معنایی یا پذیرش دوزبانهٔ برنامه. افزایش رشته و بودجهٔ
استدلال، بهبود کاربردی این نمونه را ثابت نکرد؛ صدک تأخیر نیز از آن استنباط نمی‌شود.

توقف PID آزمایشی **5250** و نبود listener تأیید شد؛ PID خط مبنا **2187** در همان مشاهده آماده
و بدون تغییر بود. این شناسه‌ها مشاهدهٔ تاریخ‌دارند، نه شناسهٔ ماندگار یا تضمین دسترس‌پذیری آینده.
شکست پیشینِ شرط ورودی غیررشته‌ای و آزمون زمینهٔ ۱۵۳۶۰ توکنی با ۱۲۰۱۶۳ میلی‌ثانیه در گزارش قبلی
باقی‌اند. برای ساختن نتیجهٔ موفق، مهلت یا پرسش ثابت تغییر نکرد.

### هویت ثابت Q5 و پیاده‌سازی در کد

[manifest مستقل تازه](../../deploy/inference/qwen3-5-122b-a10b-q5-k-m.candidate.json) موارد زیر را
ثبت می‌کند:

- تبدیل‌کننده: `bartowski/Qwen_Qwen3.5-122B-A10B-GGUF` با نسخهٔ
  `fec8b222a2eddc3346d6b6d7f7c85efea93cd6bf`.
- مرجع مدل اصلی: `Qwen/Qwen3.5-122B-A10B` با نسخهٔ
  `dc4d348443bc740c68e2d77492492c11606384d5`.
- سه فایل Q5_K_M: **۹۰۴۲۹۴۵۴۷۵۲ بایت، حدود ۸۴٫۲۲ GiB**. نام، اندازه و SHA-256 دقیق در
  manifest و [فرادادهٔ نسخهٔ ثابت](https://huggingface.co/api/models/bartowski/Qwen_Qwen3.5-122B-A10B-GGUF/revision/fec8b222a2eddc3346d6b6d7f7c85efea93cd6bf?blobs=true) آمده‌اند.
- تبدیل‌کننده، نام مدل پایه و کوانتیزه‌سازی با llama.cpp `b9222` را اعلام می‌کند، اما نسخهٔ دقیق
  منبع تبدیل را منتشر نکرده است؛ `conversion_source_revision_verified=false` صریح باقی می‌ماند.
  این GGUF شخص ثالث است، نه انتشار GGUF توسط Qwen یا تبدیلِ بازتولیدشده.
- معماری موردانتظار `qwen35moe` از تبار اعلامی می‌آید. GGUF، قالب و بارگذاری CPU این Q5 هنوز
  تأیید نشده‌اند؛ enum کد یا اجرای مدل هم‌خانواده، آزمون بارگذاری این فایل نیست.

schema سخت‌گیرانهٔ مستقل، اعتبارسنج فایل و آزمون‌های تغییر نامعتبر، هویت، مجوز، همهٔ فایل‌ها و
حدود ایمنی را حفظ می‌کنند؛ انتخاب یا پذیرش مدل انجام نمی‌دهند. رکورد پژوهشی Q4 و شکست‌های
27B/Flash بدون تغییرند. انتخاب زنده، استدلال عمومی، لایهٔ GPU و دانلود زمان اجرا ممنوع‌اند؛ حدود
آزمون شامل زمینهٔ 16K، خروجی ۲۰۴۸، بودجهٔ درخواست استدلال ۱۲۸، مهلت ۱۲۰ ثانیه، یک درخواست فعال
و دو درخواست منتظر است. این حدود، قابلیت عمومی پذیرفته‌شده نیستند؛ صحت schema، هش کامل وزن نیست.

### آماده‌سازی فایل و بودجهٔ منابع

در زمان این گزارش، دریافت محافظت‌شدهٔ بخش‌ها **در حال اجرا و ناقص** است و نظارت می‌شود. مجموعهٔ
کامل Q5 هنوز اندازه/هش کاملِ موفق ندارد. بخش ناقص، پاسخ HTTP موفق یا هشِ بخش، مدل تأییدشده نیست.
دریافت نخست روی مهمان از زنجیرهٔ پراکسی موجود انجام شد؛ مسیر بعدیِ محدود از دسکتاپ به مهمانِ
محافظت‌شده نیز نسخهٔ ثابت و TLS معتبر را کنترل می‌کند. ادامهٔ بدون نظارت یا دریافت زمان اجرا از
این مشاهده استنباط نشود.

نخستین پنجرهٔ هشت‌انتقالی، ۱۷۱۷۹۸۶۹۱۸۴ بایت، یعنی ۱۶ GiB را کامل کرد. مقایسهٔ محدود با
۱۶ انتقال از مهلت ۲۴۰ ثانیهٔ دریافت گذشت. پس از توقف همهٔ فرایندهای انتقال، تطبیق، ۷۴ بخش
با هش محلی و مجموع ۱۹۸۶۴۲۲۳۷۴۴ بایت و شش تلاش ناقص با مجموع ۱۱۴۲۵۰۹۶۵۶ بایت را نشان داد؛
تلاش‌های ناقص جدا حفظ شدند. آماده‌سازی به پنجره‌های محدودِ هشت‌انتقالی برگشت. این شکست دریافت
و مقایسهٔ منابع است، نه مهلت درخواست AI یا هش کامل مدل.

در تطبیق بعدیِ محافظت‌شدهٔ دسکتاپ، **۹۵ بخش کامل انتقال با مجموع ۲۵۵۰۱۳۶۸۳۲۰ بایت** حفظ شد.
دو نسخهٔ تکراری با هشِ بخشِ موجود تطبیق داشتند؛ دو بدنهٔ کامل دیگر پاسخ 206، Content-Range،
اندازه و هش محلیِ دقیق داشتند، اما کد خروج اصلی curl ثبت نشده بود. این محدودیت صریح است و هیچ‌کدام
هش کامل فایل اصلی نیستند. پنجرهٔ چهارانتقالیِ بعدی در هر چهار تلاش شکست خورد: سه مهلت اتصال و یک
بدنهٔ ناقص؛ دادهٔ ناقص و تشخیص‌ها حفظ شدند. آزمون IPv4 نیز برتری آن را ثابت نکرد.

آزمون اصلاح‌شدهٔ نشانی امضاشدهٔ CDN برای فایل کامل، یک اتصال را میان دریافت‌های متوالی و محدودِ
۲۵۶ MiB بازاستفاده کرد. دو بخش در **۱۶٫۰۸۶ و ۲۱٫۳۸۰ ثانیه** و چهار بخش بعدی در **۲۱٫۹۱۵،
۱۹٫۷۰۶، ۱۴٫۰۸۴ و ۱۲٫۷۱۱ ثانیه** کامل شدند. این مشاهدهٔ محدود انتقال است، نه توان پایدار یا
معیار کارایی مدل. در **۱۳:۳۸ UTC**، مهمان **۱۰۱ بخش اصلیِ انتقال با مجموع ۲۷۱۱۱۹۸۱۰۵۶ بایت**
داشت؛ خط مبنا آماده و بی‌درخواست، swap بدون مصرف و تعداد واحدهای ناموفق صفر بود. نشانی/سرآیند
امضاشده فقط در رکورد موقت و محافظت‌شدهٔ آماده‌سازی می‌ماند، نه در Git یا تنظیم زمان اجرا.
[راهنمای رسمی دریافت Hub](https://huggingface.co/docs/hub/models-downloading) مبنای فهرست صریح
CDN بود. کنترل commit/فرادادهٔ فایل کامل، بازهٔ دقیق، تطبیق هش محلی با نسخهٔ root و SHA-256 کاملِ
هر سه فایل همچنان الزامی‌اند. پایان پنجرهٔ انتقال، پذیرش مدل یا وعدهٔ ادامهٔ بدون نظارت نیست.

ادامهٔ تحت نظارت در هشت پنجره موفق پایان یافت. تطبیق تازه در **۱۴:۲۲ UTC**، **۱۳۳ بخش اصلیِ
انتقال با مجموع ۳۵۷۰۱۹۱۵۶۴۸ بایت**، خط مبنای آماده/بی‌درخواست و صفر واحد ناموفق را ثبت کرد.
از این نتیجه، کامل‌بودن فایل 122B یا انتخاب مدل استنباط نمی‌شود. سپس اولویت آماده‌سازی به
آزمون مستقلِ 3.8 Q5 در بالا منتقل شد؛ بخش‌های 122B حفظ شدند، نه تغییر نام یا حذف.

مشاهدهٔ مهمان: **۸۰ vCPU، حافظهٔ قابل‌استفادهٔ ۲۵۷۹۰۵ MiB، حدود ۲۵۱٫۸۶ GiB و سه گرهٔ NUMA
مهمان**. حجم محافظت‌شدهٔ ۴۰۰ GiB قبلاً آماده شده و دوباره قالب‌بندی نشود. NUMA مهمان، جای‌گیری
فیزیکی را ثابت نمی‌کند. حاشیهٔ آزاد datastore، سقف پروژه و منابع دیگر خدمات حفظ شوند؛ تخصیص تازهٔ
دیسک/ماشین از این بسته مجاز یا اجراشده تلقی نشود.

آزمون مستقل پیشنهادی Q5: **MemoryMax برابر ۱۲۸ GiB**، ابتدا ۳۲ رشته/سهم معادل CPU و سپس، تنها
با حاشیهٔ مشاهده‌شده، مقایسهٔ محدود ۴۸ رشته/سهم CPU؛ زمینهٔ 16K و مهلت ۱۲۰ ثانیه حفظ می‌شوند.
این‌ها **تنظیم اجراشده یا بهینهٔ اثبات‌شده نیستند**. سقف خط مبنا ۹۶ GiB و معادل ۱۸ CPU است؛
جمع دو سقف حافظه ۲۲۴ GiB و حاشیهٔ اولیه حدود ۲۷٫۸۶ GiB پیش از نیاز سیستم‌عامل/API/دیگر مصرف‌هاست.
وزن مقیم، حالت بازگشتی، کش attention، بافر prefill، تخصیص‌دهنده و کش فایل باید واقعاً اندازه‌گیری
شوند تا جا شدن مدل قابل ادعا باشد.

وزن Q8 حدود ۱۲۳٫۴۹ GiB، یعنی ۳۹٫۲۷ GiB بیشتر از Q5 است. Q5 ممکن است فشار حافظه/پهنای‌باند را
کم کند، اما رفتار کوانتیزه‌سازی و بازگشایی آن روی CPU سنجیده شود؛ سرعت یا درستی تضمین نیست.
کش فایل که پیش‌تر حساب شده، ممکن است اوج cgroup را کمتر از مصرف کامل نشان دهد. RSS/PSS، مصرف
جاری/اوج cgroup، حافظهٔ در دسترس مهمان، swap و فشار با هم دیده و کش مشترک دوباره‌شماری نشود.
با فشار منابع، افت خط مبنا یا شکست مهلت، آزمون متوقف و وضعیت تطبیق داده شود؛ سقف برای پنهان‌کردن
شکست بزرگ نشود.

### گام بعد، پذیرش، بازگشت و شواهد

ابزار آفلاین `scripts/prepare_122b_qualification.py` همان manifest و مجموعهٔ پرسش ثابت را کنترل
می‌کند؛ میزبان/مدل را فراخوانی، اعتبارنامه را دریافت یا نمایه را انتخاب نمی‌کند. ترتیب پیشنهادی،
پاسخ استاندارد، استدلال با خروجی صرفاً نهایی، زمینهٔ واقعیِ 16K و سپس 32K مشروط است. دادهٔ
پالایش‌شدهٔ RSS/PSS، cgroup، حافظه/swap مهمان و PSI فقط مشاهده‌اند، نه پذیرش مصرف کامل. بازبینی
محدود، معیار کدنویسیِ بدون اجرای کد تولیدشده و کنترل حریم خصوصی پاسخ نهاییِ موجود را به‌کار می‌گیرد.
گزارش، فایل تازهٔ محافظت‌شده و بیرون Git است. فرمان بخش انگلیسی با محیط آمادهٔ مخزن و مسیر
مطلقِ خصوصیِ تازه اجرا شود؛ کد خروج ۲ یعنی آماده‌سازی، نه پذیرش. آزمون محدودِ ناموفقِ ورودی، کد
خروج ۱ دارد. گزینه‌های `--resources` و `--trial` فقط فایل ورودیِ محدود و محافظت‌شده می‌پذیرند.

هویت typedِ 122B، کنترل سختِ قالب، نمایهٔ نامزد، اعتبارسنج هویت انتشار و مسیر استدلالِ واجد
پذیرش همچنان گام‌های کدیِ باقی‌اند؛ ابزار آن‌ها را دور نمی‌زند. پلکان 16K/32K پیشنهاد آزمون است،
نه ظرفیت زمینهٔ پذیرفته‌شده. هنگام توزیع، متن مجوز ثابتِ Apache، انتساب، اعلام تغییرهای لازم و
NOTICE احتمالیِ همراه حفظ شوند؛ در ریشهٔ نسخهٔ بررسی‌شدهٔ upstream، NOTICE یافت نشد. این
بررسی، commit دقیقِ تبدیلِ اعلام‌نشدهٔ کوانتیزه‌کننده یا انطباق جامع حقوقی را تأیید نمی‌کند.

۱. بخش‌های موجود دقیق تطبیق، ورود محدود تکمیل و اندازه/SHA-256 کاملِ هر فایل تأیید شود؛ تلاش
ناقص حفظ و هرگز انتخاب نشود.
۲. GGUF واقعیِ تأییدشده، tokenizer/قالب و سازگاری CPU با llama.cpp ثابتِ `v0.4.1` و commit
`b29c606e28a01b1bc8c1351026a0fa6e616bf6c4` پیش از بارگذاری محافظت‌شده بررسی شوند.
۳. مصرف کامل و پرسش‌های ثابتِ همسان دوزبانه برای پاسخ استاندارد، فنی و کدنویسی پذیرفته شوند؛ سپس
استدلال با خروجی صرفاً نهایی، حریم خصوصی و پذیرش زمینه در همان مهلت/صف سنجیده شوند.
۴. فقط پس از نتیجهٔ معنایی کاربردی، مسیر برنامه/API، مالکیت گفتگو، شاهد تازهٔ منبع انتخاب‌شده و
ممیزی، شاهد کهنه/ناقص/غایب/تزریق، خرابی/بازیابی وابستگی و صف، پاسخ تازه و restart با WAN مسدود،
شروع سرد VMِ قابل‌اعمال و بازگشت دقیق جدا پذیرفته شوند.

| معیار | نتیجه در زمان گزارش |
|---|---|
| فراداده/نسخهٔ ثابتِ مجوز آزاد وزن | موفق در همان دامنهٔ مجوز/فراداده |
| نمونهٔ native کدنویسی 27B با ۴۸ رشته | شکست مهلت؛ بدون پاسخ نهایی پذیرفته‌شده |
| manifest/schema/آزمون پسرفت Q5 | پیاده‌سازی در کد؛ آزمون کد، نه پذیرش مدل |
| ورود/هش کامل Q5 | آماده‌سازی ناقص؛ مجموعهٔ کامل تأیید نشده |
| metadata/قالب/بارگذاری CPU/مصرف کامل Q5 | اجرا‌نشده |
| معنا و زمان پاسخ استاندارد/استدلال/زمینهٔ دوزبانه Q5 | اجرا‌نشده |
| برنامه/شاهد/ممیزی/WAN/بازگشت Q5 | اجرا‌نشده |
| استدلال عمومی و انتخاب Q5 | غیرفعال؛ بدون گذار زنده |

مدل زنده `nextops-qwen3-5-35b-a3b-q4-k-m` است؛ runtime، حدود خط مبنا و خاموشی استدلال عمومی
ثابت‌اند. بازگشتِ آماده‌سازی فایل به restart نیاز ندارد؛ لینک/تنظیم زنده دست‌نخورده‌اند. فایل دقیق
خط مبنا و بخش‌های خصوصی حفظ شوند. تغییر زندهٔ بعدی به پذیرش ثبت‌شده، تنظیم دقیقِ محفوظ و بازگشت/
استقرار دوبارهٔ زمان‌دار نیاز دارد؛ حذف خودکار، downgrade پایگاه یا حفظ استدلال خصوصی مجاز نیست.
log انتقال، اعتبارنامه و موجودی خصوصی بیرون Git بمانند. وضعیت/فهرست جاری به این گزارش ارجاع دهند،
بدون بازنویسی پذیرش تاریخی یا موفق نامیدن معیار اجرا‌نشده.

</div>
