# Qwen 3.8 qualification / پذیرش فنی Qwen 3.8

Status: bounded existing-guest trial, authorized by the owner's upgrade/resource instructions
on 2026-10-05. Not a serving-model selection, new production acceptance or permission to erase
other workloads. [CPU guide](../en/CPU_AI.md) / [راهنمای CPU](../fa/CPU_AI.md).

## English

### Full greedy result — 2026-10-07, 06:35:53 UTC

Exact `60605d8`/greedy Q8 completes all sixteen finals under explicit300; main semantic review is
13 passed/3 failed: English unverified upstream assertion, Persian omission of one-authorized-host
scope, and Persian causal answer lacking an explanatory hypothesis. Both raw code samples pass
twelve finite AST boundaries. English stale evidence65373ms resolves the earlier diagnostic
timeout, not a blanket latency/quality acceptance; Persian hypothesis126362ms still exceeds
historical120. Native SHA `b69e4cf3a9725a344b2eadc92a72bb9ec0090ce971934de5ca051d09ac17926e`.
Owned stop/separate PID0/inactive/free-port/unchanged ready-idle baseline and five exact-source
CI jobs pass, not raw quality. Offline finite review is partial/exit2: six finite passes, ten manual
reviews, no missing cases; direct main review resolves the semantic findings, not independence.

Decision: keep both profiles default-off/unselected and preserve all five prompt/sampler reports,
failures and wheels. Prompt/sampler-only changes have not cured persistent factual/instruction
failures. Do not repeat identical tests, cherry-pick seeds, soften scoring, train on frozen cases
or award app-fallback credit. Further work needs a materially evidenced artifact/method strategy,
applicable license/integrity/resource/tool review and unchanged full raw acceptance. Independent,
matched app/thinking/privacy/context/evidence/WAN/model rollback remain open; live35B and public
thinking are unchanged. This is not a live release or production acceptance.

### Instruct result and greedy-decoding plan — 2026-10-07, 06:10 UTC

The exact `da8d61c` instruct-sampler trial completed ten finals, then TimeoutError on English
stale/partial evidence under300. Main-only accounting: nine passed/two failed/five not run;
English networking asserts an unverified upstream condition. Both completed coding samples pass
twelve finite AST boundaries. Native SHA
`79178feeb7f7d4e910bd868d031c20c5383dd64c6a965e8b7d3176e13d35b9de`; owned stop and separate
baseline reconciliation passed. Five exact-source CI jobs passed, not native quality.

Problem: stochastic instruct sampling did not cure factual instruction following and introduced
a retained timeout. A distinct greedy comparison removes stochastic choice; it is not upstream
guidance, training or guaranteed correctness. Explicit `NEXTOPS_QWEN38_GREEDY_DECODING_ENABLED=1`
requires an expanded exact Q8/Q5 candidate; temperature0/top-k1/top-p1/min-p0/presence0/repeat1/
preselected seed0. Both sampler flags default off; enabling both fails closed. Do not widen
thinking, context, deadlines, queues, output or any authorization boundary.

Plan/tasks: source default/mutual-exclusion/security tests, exact committed full16 capture,
bounded controller review, fresh artifact/resource/idle preflight, full raw trial and unchanged
semantic/code scoring. Same retained Q8/no-BLAS/32 workers/48GiB/16K/384/300/global watchdog;
all previous failures retained. No question matching, prompt change, downloads, lucky-seed
selection, fallback credit or private-reasoning retention. Repetition/truncation from greedy
decoding is a failure, not a waiver. Independent and matched app/privacy/context/evidence/WAN/
model-rollback gates follow only after full standard correctness. Source rollback is reverting
the greedy field/wiring/tests to the parent and stopping only the owned unit; live35B is untouched.
Update paired guides, project state, next task and traceability with actual outcomes.

### Candidate sampler comparison — 2026-10-07

Problem: repeated instruction-following failures persist across three prompt policies. The
retained candidate sends temperature0.3/presence0 and inherits native top-k/min-p defaults;
this differs from [Qwen's non-thinking guidance](https://huggingface.co/Qwen/Qwen3.8-27B#best-practices).
Test a materially distinct, opt-in sampling profile without changing the restored prompt or tests.
`NEXTOPS_QWEN38_INSTRUCT_SAMPLING_ENABLED=1` requires an expanded exact Q8/Q5 candidate. It sets
temperature0.7/top-p0.8/top-k20/min-p0/presence1.5/repeat-penalty1. Seed0 is fixed before the trial
for input reproducibility, not an upstream recommendation or cross-hardware determinism claim.
The flag defaults off; serving35B/other models cannot enable it. Thinking remains denied.

Risks: higher presence penalty can worsen language consistency; vendor settings do not prove
NextOps quality. Preserve all sixteen frozen questions/semantic/AST criteria, including format,
authorized scope, full times, unsupported claims, code guards and deadline failures. Run one finite
retained-Q8/no-BLAS/32-worker/48-GiB/16K/384-output comparison with explicit300-second deadlines
and unchanged watchdog/security/owned cleanup. No new weights, downloads, VM/storage/route changes,
target credentials, application fallback credit or private-reasoning retention. Record the full
sampler/source/capture identity, all finals and failures; do not retry the same sample blindly.

Tasks: configuration/adapter tests and default isolation; exact-source capture/tool review; fresh
idle/artifact/resource preflight; full raw trial/review; then independent and matched application,
privacy/context/evidence/WAN/rollback qualification only after standard correctness passes. Source
and live acceptance remain separate. Roll back the source flag/wiring to this change's parent and
stop only the owned trial unit; baseline stays untouched. Preserve earlier failed reports and update
paired CPU guides, state/next task and traceability. Native and live gates are not run at this plan.

### Third policy rejected; exact source rollback — 14:31 UTC

The `4654b43` full Q8/300 run met all sixteen deadlines but regressed to **11 main-reviewed
passes/five failures**: both networking topology claims, missing Persian string guard and scope,
and an unsupported categorical English denial of causation. Persian explanatory hypothesis now
passes, but that cannot offset the regressions. Native SHA:
`0984bfea6235c3b24b2cf464ff7e557fc642e506020f58b436c9c6568b2285ce`.
The unchanged AST checker again rejects seven Persian guard boundaries; no generated code runs.
Owned cleanup/separate baseline reconciliation and five exact-source CI jobs passed, not quality.

This policy was rejected and `qwen38_prompt.py` plus its two policy tests restored to exact `6c3a380`
contents. All reports and the rejected wheel are retained. The restored policy's measured 13/16 remains
failed, not a selected model or a new unchanged trial. Prompt-only changes have not reliably
repaired raw instruction following; do not cherry-pick samples, train on frozen questions or
credit deterministic application text as raw success. Further model work needs a materially
justified artifact/profile/method strategy with applicable license/integrity/resource/tool review,
then unchanged full semantic/code acceptance. Serving35B/defaults/public thinking remain unchanged;
independent/app/privacy/thinking/context/evidence/WAN/model rollback are still open.

### Labelled-policy result and closed-observation experiment — 14:07 UTC

The `6c3a380` full Q8 run completed all sixteen finals within explicit300 seconds, but main
semantic review is **13 passed/three failed**: English networking assumes an upstream dependency,
Persian stale evidence omits explicit authorized scope, and Persian causality gives uncertainty/
two checks without a specific explanatory hypothesis. Its124395ms final fits300, not historical120.
Both coding samples pass all twelve finite AST boundaries; English stale scope is preserved.
Native SHA `edfe704360afb2a17b9413c775f7b7730e9f75050340717571d869fac7f18d8c`;
owned stop/separate baseline reread and all five exact-source CI jobs pass, not model acceptance.

The next bounded policy changes the framing rather than repeating an identical run: supplied
observations define actual infrastructure facts; diagnostic explanations must not turn textbook
error definitions into observed components. Observation reports start with supplied authorization/
scope before host/value. A requested hypothesis needs a possible causal explanation, explicitly
unverified, not uncertainty alone. General model knowledge stays distinct from live evidence.
No frozen answers/values/question matching, relaxed criteria or application fallback credit.
Run the full unchanged sixteen-case Q8/300-second CPU corpus with the same artifact/runtime/
sampling/384 output/16K/resources/security/global watchdog. Preserve all failures and main-only
review; serving35B/public thinking and later independent/app/context/privacy/WAN/rollback gates
are unchanged. Prompt edits are not training or a promise of improvement.

### Priority-rule result and distinct labelled-provenance follow-up — 13:43 UTC

The `d401583` Q8 run returned fifteen finals; the last Persian hypothesis timed out. Main review
records **12 passes/four failures**: English networking still asserts upstream failure, both
stale answers omit explicit authorized scope, and Persian hypothesis has no completed final.
Both raw code answers now pass all twelve finite AST boundaries and Persian networking passes.
These narrow repairs are not whole-model acceptance. Native SHA:
`8a6682fd3d5235fdd7fdf8edfa05ef5ad99b8cba2826424ac19c2e5046ddd6ad`.
Owned cleanup and separate inactive/PID0/listener-absent/unchanged ready-idle serving checks passed.
All five exact-source CI jobs passed; neither CI nor application fallback changes the raw score.

Next distinct experiment: retain type-first rules; forbid asserting intermediary/upstream failure
from an error code and require labelled source/scope/observed/collected/limits in observation
sentences. A host name alone is not authorization scope; absent fields stay unknown. No frozen
values/answers or question matching are added. Capture the committed opt-in300-second adapter
profile and test the full unchanged sixteen-case corpus, same Q8/runtime/32 workers/16K/384
tokens/sampling/one slot/48 GiB. Keep the finite2100-second native watchdog and2200-second
controller bound; aggregate timeout is a failure, not a waiver. Record the explicit300 deadline
separately from historical120 outcomes. Do not promote while any semantic gate remains failed;
independent/app/thinking/privacy/context/evidence/WAN/rollback gates remain separate.

### Raw-quality repair experiment — 2026-10-06

The owner requests repair of raw coding/reasoning failures, not application fallback credit.
The candidate-only locale-native policy now prioritizes runtime type guards before value tests,
limits TCP/HTTP conclusions to observed protocol facts, and requires explicit source/full times/
authorized scope/stale-partial qualifiers with unchanged technical identifiers. These generic
rules depend only on trusted locale/output metadata; they contain no frozen answers or question
matching. They are instructions, not training, authorization or measured model improvement.

Acceptance plan: capture the exact committed adapter's full unchanged sixteen EN/FA requests,
then run the retained Q8/no-BLAS/32-worker CPU profile with 16K context, 384 output tokens,
unchanged sampling, 120-second case deadlines, one slot and 48 GiB hard memory. Review finals
directly against the frozen semantic criteria and finite coding checker, without application
fallbacks. Record main-only review separately from independent approval. No downloads, model/
runtime replacement, serving prompt/configuration, public thinking, queue or resource changes.
On failure retain the report and stop/reconcile only the owned transient unit; keep the serving
35B ready-idle baseline unchanged. Historical Q8 12/16 and Q5 failures remain failed. Further
app/proxy, thinking/privacy/context, evidence/WAN and rollback gates remain open.

### Timing result — 11:53:44 UTC

The retained-Q5 two-case300-second probe returned EN/FA finals in88441/145010 ms; both pass
the narrow main-reviewed hypothesis criteria. Fourteen cases are not run under300. Native SHA:
`96813c347b8035d592c941ffc6ead9d1a0250dfa4f9347b730a57ab49e0275c5`.
Owned cleanup/separate baseline reconciliation passed; source `5e15b5c` passed five CI jobs.
The explicit offline review deadline records300 separately from the frozen corpus120; default
review still fails the late Persian sample. Full model semantics, independent, app/proxy,
thinking/privacy/context/evidence/WAN/rollback remain open; live35B/defaults remain unchanged.

### Owner-authorized long-response profile — 2026-10-06

The later [timing amendment](PROMPT_CHANGELOG.md) replaces the old timing ceiling prospectively,
not historical outcomes or semantic criteria. Default provider/app/proxy budgets remain
120/150/180 seconds. An explicit `NEXTOPS_QWEN38_EXTENDED_TIMEOUT_ENABLED=1` permits only the
expanded exact Q8/Q5 candidates up to 300 seconds; 16K and thinking denial remain enforced.
Candidate-only overlays supply 300/330/360 seconds at provider/app/generation proxy boundaries.
No arbitrary unlimited wait, wider queue, different prompts, new model or resources are included.

Acceptance: test default denial, explicit opt-in, upper bounds, incompatible models, context and
thinking denial, short readiness checks and unchanged ordinary routes. Capture the committed
adapter's unchanged synthetic payloads; run only the two frozen hypothesis questions under the
new deadline on the existing protected Q5/native CPU profile. Record actual final latency,
semantic review, failure, owned-unit stop and a separate unchanged ready-idle baseline reread.
Fourteen other cases are not run under this profile, not implicitly passed. Main self-review is
not independent approval. Existing topology/coding/provenance failures still block selection.

Rollback: remove the optional overlays and restore the base proxy's two 180-second directives
in a separately authorized change, validate configuration before reload and reconcile inflight
requests. No live files/restarts are required by this source change. WAN, full context, thinking,
app/browser integration and model rollback gates are still open.

### Distinct Q8 comparison failed quality — 11:19:59 UTC

The planned Q8/restored-policy/no-BLAS full comparison actually completed sixteen final deadlines,
but main-only semantic review is **12 passed/four failed**: both networking topology claims,
Persian coding guard and Persian authorized scope. Both hypothesis samples now pass the narrow
frozen criteria, not independent/model-wide acceptance. Retain native SHA
`b13ddbcb8e71555c81ff951126a4900eed0b7bf46f200ba7444a847c434a34f8`, finite failures and separate
stopped/listener-absent/unchanged-ready-idle rereads. Exact `4ac2cf4` source CI passed five jobs.
No unchanged retry, precision downgrade, relaxed gate, relabelled model or serving cutover.
Further trials need a justified materially distinct strategy and applicable review; thinking/
app/context/evidence/WAN/rollback remain unaccepted. Actual3.8 is still the goal, not live yet.

### Rejected third diagnostic — 10:47 UTC

The third full run met all sixteen final deadlines, but semantic review is **11 passed/five
failed**, main-only. Reject the generic 50-word experiment: Persian coding regressed across
seven finite AST boundaries; unverified networking topology, missing Persian provenance and
missing causal hypothesis remain. Restore prompt/tests to exact `7157c3b` bytes and retain
the report SHA `c8591c1ffa8cda6bbd4df6c165ff56b847e881c9ab419f3e72a7e488a18049dc`.
Successful cleanup and unchanged baseline are not semantic acceptance. A smaller Q4 metadata
lookup is not an imported/qualified candidate and reduces precision, not parameter count.
Any distinct follow-up requires source/license/hash/capacity/tool review and a measured reason
to expect benefit; preserve corpus, deadlines and security. Do not select a failed model,
relabel 3.5, repeat unchanged diagnostics or claim main self-review as independent approval.
Standard/app/thinking/privacy/context/evidence/WAN/rollback gates stay open; live35B unchanged.

Next bounded comparison: use the retained Q8 artifact with the restored locale-native policy
and already reviewed no-BLAS runtime, the same full corpus/32-worker profile/16K/384 output/
120-second deadlines and independent-review labels. The initial Q8 experiment used different
instructions/runtime and only eight standard questions; this is a distinct full diagnostic, not
an unchanged retry or promised improvement. No download, promotion or precision downgrade.

### Failed compact trial and bounded follow-up — 10:30 UTC

The second full diagnostic and separate two-case 16/64-worker probes also failed the Persian
deadline. Preserve all report identities, semantic findings, actual cleanup and unchanged baseline
checks; the probes do not cover fourteen other questions. Do not infer a thread optimum from
different answer lengths/cache histories. The next generic source experiment adds a 50-word target
only under small trusted output budgets, never overriding required facts/code/format/provenance;
explicitly preserves Latin technical timestamps in Persian; and checks final sentence count and
provenance. Error-code definitions cannot establish unobserved topology. Keep corpus/sampling/
deadlines/context/artifact/security fixed. This is another main-only diagnostic, not acceptance.

### Observed failure and distinct compact-policy experiment — 2026-10-06

The first locale-native diagnostic actually failed at the last Persian deadline. Main-only
review records 12 passes/four failures against the unchanged criteria: unverified Persian
networking topology, omitted authorized scope in both stale answers, and the timeout. Preserve
the protected report and separate stopped/listener-absent/unchanged-ready-idle checks. The next
bounded source experiment makes scope/full-time omission explicitly forbidden, reduces generic
wording and requests the shortest complete parts. This is not training, a new answer router,
an identical retry or independent approval. Keep the same native profile and all fixed limits.
Do not begin thinking/cutover gates while applicable standard failures remain.

### Owner priority and candidate-only repair — 2026-10-06

The owner now prioritizes Qwen **3.8**, accepting a lower parameter count, and asks the main
agent to perform the work. A 3.5 alternative cannot satisfy that goal. Resume from the complete
pinned 27B Q5 artifact rather than repeating the stalled 122B transfer. Preserve those transport
records and the unaccepted V3 review bundle; this instruction does not turn self-review into
independent review or license a failed model for public use.

The bounded source repair is a locale-native, compact general-answer policy shared by the two
exact 3.8 candidates. It preserves reported source/full observation and collection times/scope,
stale/partial qualifiers, unknown current states, conditional hypotheses and type-first coding.
It uses trusted locale/output metadata only, never question keywords or fixture-specific answers.
Keep serving 3.5 and evidence-synthesis instructions unchanged. Do not change frozen questions,
review criteria, sampling, 120-second deadline, 16K context or thinking denial.

Acceptance sequence: local policy/adapter/security regressions; an isolated standard-first native
diagnostic; semantic review of every final and deadline failure; then matched application,
final-only thinking, measured context, authorized evidence/audit/offline and exact rollback gates.
Main-only native results are not independent approval. Preserve failed attempts. Revert the
candidate-only module/wiring to roll back source; the diagnostic has no serving cutover to undo.
No training, GPU, cloud, download, infrastructure permission or architectural migration is added.

### Bounded follow-up after the failed Q8 trial

The [dated permissive packet](PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md) adds a distinct pinned
27B UD-Q5_K_M trial after the failed Q8 coding/context results. It reduces weight size, not parameter
count, and must independently pass full hash, actual template, CPU load, frozen/independent coding,
standard-first EN/FA, final-only thinking and actual context/latency acceptance. Historical Q8 gates
and the 122B alternative remain recorded. Generic defensive-coding prompt guidance is source-only,
not training, a keyword router or proof of improvement. All security, offline, deadline, resource,
rollback and documentation requirements below also apply to this follow-up. Serving identity and
public thinking remain unchanged until matched application qualification.

### Problem and requirements

Improve actual EN/FA instruction following, technical/coding answers, follow-ups and useful
bounded thinking. Compare the serving 35B baseline with a pinned Qwen3.8-27B Q8 precision trial,
not an assertion that 27B is the largest model or that vendor scores prove NextOps accuracy.
The owner supplies a fresh DS-C Storage screenshot (rounded 3.49 TB capacity, 1.79 TB provisioned,
1.71 TB free) and reports no reserved space. Host screenshot: 1.31 TB RAM total, 213.64 GB used,
1.1 TB free; 112 CPUs labelled Xeon Platinum 8280. These are supplied observations/attestation,
not formal all-VM growth accounting, sustained capacity or verified physical NUMA placement.

Direct guest preflight: 80 online vCPUs, 128769 MiB usable RAM, 107664 MiB available, no swap use,
one guest NUMA node/80 virtual sockets, AVX-512/VNNI visible, 169557 MiB available model volume.
The working native runtime remains capped at 96 GiB/18 CPU equivalents. Unused host RAM is not
guest RAM. One 29047086048-byte candidate and its bounded range/assembly workspace fit the
existing model volume; no VM, disk, reservation or serving resource-limit change is required.
The 900-GiB DS-C free-space target is a safety target, not a configured reservation. Keep the
3-TB project ceiling and preserve ESXi, app, connector, databases and Zabbix capacity.

### Non-goals, threats and dependencies

No cloud/GPU, replacement framework, new target tools, operational permissions, schema change,
unbounded output/context/queue, private reasoning display/storage, runtime downloads or live
telemetry inference from host screenshots. Pinned llama.cpp and baseline artifacts remain intact.
Untrusted model bytes, templates, monitoring text and generated code do not grant authorization.
Third-party GGUF declares Qwen3.8-27B lineage; exact conversion-source revision is still unverified.
Keep this uncertainty in the manifest. Do not call a quantizer artifact an official Qwen GGUF.
Record Apache-2.0 licensing; Flash-Next's custom license requires separate applicability review.

### Plan and tasks

1. Record private change scope, fresh supplied capacity and direct guest/mount/runtime checks.
2. Provision **one** immutable Q8 artifact at the pinned source revision through the existing
   proxy chain. Bound transfers and verify exact complete size/SHA-256. Preserve partial attempts;
   never select a partial file. Eight-range continuation is provisioning, not runtime downloading.
3. Inspect actual GGUF architecture, tokenizer/template, lineage and embedded metadata after hash
   verification. Use a separate protected loopback-only CPU trial, one slot, explicit memory/CPU/
   time limits and idle-baseline checks; no target credentials. Stop/clean up the trial at handoff.
4. Reuse the existing adapter with the exact candidate identity. Trusted standard template flags
   disable default thinking and preserved thinking; serving model selection stays unchanged.
   Thinking remains denied for this candidate until a separate matched profile is qualified.
5. Freeze EN/FA format/arithmetic, saved follow-up, DNS/TCP/HTTP/firewall/service, coding and
   provenance/stale/partial/missing/injection cases. Record final answers and resource/timing data;
   discard private reasoning immediately. Review semantics, not merely HTTP 200 or token count.
6. Benchmark thread counts within a bounded isolated profile before changing serving limits.
   Review Flash-Next separately for actual CPU compatibility, complete memory fit and license.
   A proposed 256–512-GiB guest trial is not an applied resize or a promised optimum.
7. Only after usefulness/privacy/deadline gates pass, qualify matched app/API behavior, fresh
   authorized EN/FA evidence/audit, WAN-offline start/restart, failure/queue and rollback/reapply.
   Record any applicable VM reboot/cold-start gap as not run, not passed.

### Acceptance, rollback and documentation

Full-file hash, CPU load and template tests are separate gates. Each answer has the existing
120-second deadline; a timeout is a failure, not a reason to silently widen it. Preserve one active/
two queued requests, context admission, session/owner isolation, source/time/scope and integrity
guards. Model knowledge is not fresh infrastructure evidence; no source substitution on failure.
No unattended trial unit, download or rollback timer remains after handoff. Import rollback needs
no live service restart: baseline links/config are untouched. A later selected-profile change needs
exact retained artifacts/config, timed rollback and fresh authenticated generation/evidence/audit
checks. No destructive schema downgrade or automatic model/snapshot deletion.

Maintain paired CPU guides, project state/next task, the pinned candidate manifest, local tests and
this index entry. Preserve the prior failed-thinking and UI deployment records. Update the serving
release manifest only for an actually accepted identity change, not source registration.

## فارسی

### نتیجهٔ کامل حریصانه — ۷ اکتبر ۲۰۲۶، ۰۶:۳۵:۵۳ UTC

Q8 با کد دقیق `60605d8` و انتخاب حریصانهٔ توکن، همهٔ شانزده پاسخ را در مهلت صریح۳۰۰ثانیه
تکمیل کرد؛ بازبینی عامل اصلی۱۳ مورد موفق و۳ ناموفق دارد: ادعای بی‌شاهد بالادست انگلیسی،
حذف دامنهٔ «تنها میزبان مجاز» در فارسی و نبودِ فرضیهٔ توضیحی فارسی. هر نمونهٔ کد، دوازده
مرز محدود AST را گذراند. شاهد انگلیسی با۶۵۳۷۳میلی‌ثانیه پایان مهلت پیشین را رفع کرد، نه
اینکه پذیرش عمومی سرعت یا کیفیت باشد؛ فرضیهٔ فارسی۱۲۶۳۶۲میلی‌ثانیه طول کشید و هنوز از۱۲۰
تاریخی بیشتر است. هش بومی بالا، توقف اختصاصی و بررسی جداگانهٔ نبود PID/شنونده و آمادگی
بی‌درخواستِ خط مبنا حفظ‌اند. پنج CI همان کد، صحت خام نیست. بررسی محدود آفلاین partial با
کد خروج۲ دارد: شش کنترل محدود موفق، ده مورد نیازمند بررسی دستی و هیچ مورد غایب؛ بازبینی
مستقیم عامل اصلی معنا را بررسی می‌کند، نه استقلال بررسی را.

تصمیم: هر دو نمایه پیش‌فرض خاموش و انتخاب‌نشده بمانند؛ پنج گزارش دستور/نمونه‌گیری، شکست‌ها
و فایل‌های بسته حفظ شوند. این تغییرها خطای پایدار واقع‌گویی و پیروی از دستور را رفع نکردند.
اجرای یکسان تکرار، seed موفق جدا انتخاب، معیار آسان‌تر یا پرسش ثابت وارد آموزش نشود؛ پاسخ
جایگزین برنامه به مدل امتیاز ندهد. برای کار بعدی، راهبرد متفاوتِ فایل یا روش با شاهد و
بررسی مجوز، صحت، منابع و ابزار و سپس پذیرش کامل خام با معیار ثابت لازم است. معیارهای مستقل،
برنامه، استدلال، حریم خصوصی، زمینه، شاهد، WAN و بازگشت مدل بازند؛ مدل زندهٔ35B و استدلال
عمومی ثابت‌اند. نسخهٔ زندهٔ تازه یا پذیرش عملیاتی اعلام نمی‌شود.

### نتیجهٔ نمونه‌گیری سازنده و برنامهٔ رمزگشایی حریصانه — ۷ اکتبر ۲۰۲۶، ۰۶:۱۰ UTC

آزمون نمایهٔ سازنده از کد دقیق `da8d61c` ده پاسخ نهایی داد و شاهد کهنه/ناقص انگلیسی در
مهلت۳۰۰ثانیه با TimeoutError پایان یافت. بازبینی عامل اصلی نه موفق، دو ناموفق و پنج
اجرا‌نشده را ثبت می‌کند؛ پاسخ شبکهٔ انگلیسی وضعیت بالادست را بدون شاهد قطعی می‌داند.
هر نمونهٔ کامل کد، دوازده حالت محدود AST را گذراند. هش بومی بالا، توقف اختصاصی و بررسی
جداگانهٔ خط مبنا حفظ‌اند. پنج کار CI همان کد صحت خام را ثابت نمی‌کند.

مسئله: نمونه‌گیری تصادفیِ سازنده پیروی از دستور واقع‌محور را اصلاح نکرد و مهلت یک پاسخ
پایان یافت. مقایسهٔ متفاوتِ حریصانه انتخاب تصادفی را حذف می‌کند؛ توصیهٔ سازنده، آموزش یا
تضمین صحت نیست. فعال‌سازی صریح `NEXTOPS_QWEN38_GREEDY_DECODING_ENABLED=1` فقط برای نامزد
دقیق Q8/Q5 با نمایهٔ expanded است و مقادیر ثابت بالا را دارد. دو نمایه پیش‌فرض خاموش و
هم‌زمانی آن‌ها مردود است. استدلال، زمینه، مهلت، صف، خروجی یا مجوز گسترده‌تر نشود.

گام‌ها: آزمون جدایی و منع هم‌زمانی و امنیت کد؛ ثبت شانزده درخواست از کد دقیق؛ بازبینی
کنترل‌کنندهٔ محدود؛ بررسی تازهٔ فایل، منابع و آمادگی بی‌درخواست؛ آزمون کامل خام با معیار
معنا و کدِ ثابت. فایل Q8، runtime بدون BLAS، منابع و سقف‌های بالا حفظ شوند. همهٔ شکست‌های
پیشین نگه‌داری شوند. تطبیق پرسش، تغییر دستور، دانلود، seed موفق، امتیاز پاسخ جایگزین یا
نگه‌داری استدلال خصوصی مجاز نیست. تکرار یا بریدگی پاسخ حریصانه شکست است، نه استثنا.
پذیرش مستقل و برنامه/حریم خصوصی/زمینه/شاهد/WAN/بازگشت مدل پس از موفقیت کامل استاندارد است.
بازگشت کد، حذف تغییر حریصانه به محتوای parent و توقف فقط واحد اختصاصی است؛ مدل زندهٔ35B
ثابت می‌ماند. راهنمای دو زبان، وضعیت، کار بعد و ردیابی با نتیجهٔ واقعی به‌روز شوند.

### مقایسهٔ نمونه‌گیری نامزد — ۷ اکتبر ۲۰۲۶

مسئله: سه دستور متفاوت، خطاهای پیروی از دستور را به‌طور پایدار رفع نکردند. نامزد موجود
temperature0.3 و presence0 می‌فرستد و top-k و min-p را به پیش‌فرض runtime واگذار می‌کند؛
این تنظیم با راهنمای بدون استدلال Qwen تفاوت دارد. نمایهٔ اختیاری و متفاوتی با همان دستور
بازگردانده‌شده و معیارهای ثابت آزموده شود. پرچم
`NEXTOPS_QWEN38_INSTRUCT_SAMPLING_ENABLED=1` فقط برای نامزد دقیق Q8 یا Q5 با گفت‌وگوی
گسترش‌یافته پذیرفته می‌شود. مقادیر temperature0.7، top-p0.8، top-k20، min-p0، presence1.5
و repeat-penalty1 صریح‌اند. Seed0 پیش از آزمون برای ثبت ورودی تکرارپذیر انتخاب شده؛ پیشنهاد
سازنده یا تضمین نتیجهٔ یکسان روی هر سخت‌افزار نیست. پرچم به‌صورت پیش‌فرض خاموش است، برای
35B زنده و مدل‌های دیگر پذیرفته نمی‌شود و استدلال را فعال نمی‌کند.

خطر: جریمهٔ حضور بالاتر ممکن است یکنواختی زبان را کاهش دهد؛ توصیهٔ سازنده پذیرش NextOps
نیست. هر شانزده پرسش و معیار معنایی و AST، از جمله قالب، دامنهٔ مجاز، زمان کامل، ادعای
بی‌شاهد، شرط نوع و مهلت، ثابت بمانند. یک مقایسهٔ محدود روی Q8 موجود با runtime بدون BLAS،
۳۲ رشته، سقف ۴۸ GiB، زمینهٔ16K، خروجی۳۸۴ و مهلت صریح۳۰۰ ثانیه اجرا شود؛ سقف کلی، امنیت
و توقف اختصاصی تغییر نکنند. فایل مدل، دریافت اینترنتی، منابع یا مسیر شبکهٔ VM، اطلاعات ورود
مقصد، امتیاز پاسخ جایگزین و نگه‌داری استدلال خصوصی در دامنه نیستند. هویت کامل نمایه و کد،
همهٔ پاسخ‌ها و شکست‌ها ثبت شوند؛ همان اجرای بدون تغییر کورکورانه تکرار نشود.

گام‌ها: آزمون تنظیم و نگاشت و جدایی پیش‌فرض؛ ثبت درخواست از کد دقیق و بازبینی ابزار؛ بررسی
تازهٔ آمادگی، فایل و منابع؛ آزمون و بازبینی کامل پاسخ خام؛ سپس فقط پس از موفقیت استاندارد،
بازبینی مستقل و پذیرش مسیر برنامه، حریم خصوصی، زمینه، شواهد، قطع WAN و بازگشت مدل. پذیرش
کد و محیط عملیاتی جدا هستند. بازگشت کد با حذف پرچم و نگاشت این تغییر به نسخهٔ والد و توقف
فقط واحد آزمون انجام می‌شود؛ خط مبنا دست‌نخورده می‌ماند. سوابق شکست حفظ و راهنمای CPU،
وضعیت، کار بعدی و ردیابی در هر دو زبان به‌روز شوند. آزمون بومی و زنده در زمان این طرح هنوز
اجرا نشده‌اند.

### رد دستور سوم و بازگشت دقیق کد — ساعت۱۴:۳۱ UTC

اجرای کامل Q8/۳۰۰ با کد `4654b43` همهٔ شانزده مهلت را گذراند، اما به **۱۱ موفقیت/پنج شکست
در بازبینی عامل اصلی** برگشت: ادعای توپولوژی در هر دو زبان، نبود شرط رشته و دامنه در فارسی
و رد قطعی و بی‌شاهدِ علت در انگلیسی. فرضیهٔ توضیحیِ فارسی اکنون موفق است، اما شکست‌های دیگر
را جبران نمی‌کند. هش بومی در بخش انگلیسی همین رکورد آمده است. کنترل ثابت AST دوباره هفت
مرز شرط نوعِ فارسی را رد می‌کند؛ کد تولیدشده اجرا نمی‌شود. توقف/بازخوانی جداگانهٔ خط مبنا
و پنج CI همان کد موفق‌اند، نه کیفیت مدل.

این دستور رد شد و فایل دستور و دو آزمون آن به محتوای دقیق `6c3a380` بازگشتند. گزارش‌ها و
wheel ردشده حفظ شده‌اند. نتیجهٔ ۱۳ از ۱۶ دستور بازگردانده‌شده هنوز ناموفق است؛ این بازگشت
نه انتخاب مدل است و نه آزمون تازهٔ اجرای بدون تغییر. تغییر دستور به‌تنهایی پیروی از دستور
را در پاسخ خام به‌طور پایدار اصلاح نکرده است. نمونهٔ موفق به‌تنهایی ملاک نباشد، پرسش‌های
ثابت وارد آموزش نشوند و متن قطعی برنامه به مدل امتیاز ندهد. کار بعدی به راهبرد متفاوت و
مستدلی برای فایل مدل، نمایه یا روش آزمون نیاز دارد؛ بررسی مجوز، صحت فایل‌ها، منابع و ابزارها
و سپس پذیرش با مجموعهٔ کامل و ثابت معیارهای معنا و کد لازم است. مدل زندهٔ 35B، تنظیمات
پیش‌فرض و وضعیت استدلال عمومی ثابت‌اند. بازبینی مستقل و پذیرش برنامه، حریم خصوصی، استدلال،
پنجرهٔ زمینه، شواهد، قطع WAN و بازگشت مدل همچنان تکمیل نشده‌اند.

### نتیجهٔ دستور عنوان‌دار و آزمایشِ مشاهدهٔ محدود — ساعت۱۴:۰۷ UTC

اجرای کامل Q8 با کد `6c3a380` هر شانزده پاسخ نهایی را در مهلت صریح۳۰۰ثانیه ثبت کرد، اما
بازبینی معناییِ عامل اصلی **۱۳ موفقیت/سه شکست** دارد: شبکهٔ انگلیسی وجودِ بالادست را فرض
می‌کند، شاهد کهنهٔ فارسی دامنهٔ صریحِ مجاز را حذف می‌کند و پاسخ علّی فارسی، با وجود عدم قطعیت/
دو بررسی، توضیح احتمالیِ مشخصی نمی‌دهد. پاسخ۱۲۴۳۹۵میلی‌ثانیه‌ای در۳۰۰ جا دارد، نه سابقهٔ۱۲۰.
هر دو کد، دوازده حالت محدود AST را می‌گذرانند؛ دامنهٔ شاهد کهنهٔ انگلیسی حفظ است. هش بومی
در بخش انگلیسی آمده؛ توقف/بازخوانی جداگانهٔ خط مبنا و پنج CI همان کد موفق‌اند، نه پذیرش مدل.

دستور محدودِ بعدی، چارچوب بیان را عوض می‌کند، نه اینکه آزمون یکسان تکرار شود: واقعیت وضعیت
زیرساخت از مشاهدهٔ داده‌شده می‌آید؛ تعریف کتابیِ خطا نباید به جزء مشاهده‌شده تبدیل شود.
گزارش مشاهده با مجوز/دامنهٔ داده‌شده، پیش از میزبان/مقدار آغاز شود. فرضیهٔ خواسته‌شده باید
توضیح احتمالیِ مشخص و صریحاً تأییدنشده باشد، نه فقط بیان عدم قطعیت. دانش عمومی مدل از شاهد
زنده جداست. پاسخ/مقدار ثابت، تطبیق سؤال، معیار آسان‌تر یا امتیاز پاسخ جایگزین اضافه نمی‌شود.
مجموعهٔ کامل و ثابتِ Q8/۳۰۰ثانیه با همان فایل/runtime/نمونه‌گیری/۳۸۴توکن/16K/منابع/امنیت/
watchdog اجرا شود. همهٔ شکست‌ها و برچسب بازبینی عامل اصلی حفظ‌اند؛ مدل زندهٔ35B/استدلال
عمومی و معیار مستقل/برنامه/زمینه/حریم خصوصی/WAN/بازگشت ثابت‌اند. تغییر دستور، آموزش یا وعدهٔ
بهبود نیست.

### نتیجهٔ دستور اولویت‌دار و بررسی متفاوتِ منشأِ عنوان‌دار — ساعت۱۳:۴۳ UTC

اجرای Q8 با کد `d401583` پانزده پاسخ نهایی ثبت کرد؛ آخرین فرضیهٔ فارسی از مهلت گذشت.
بازبینی عامل اصلی **۱۲ موفقیت/چهار شکست** دارد: شبکهٔ انگلیسی هنوز خرابی بالادست را قطعی
می‌داند، هر دو پاسخِ شاهد کهنه دامنهٔ صریحِ مجاز را حذف می‌کنند و فرضیهٔ فارسی پاسخ کامل
ندارد. اکنون هر دو کد خام، هر دوازده حالتِ محدود AST را می‌گذرانند و شبکهٔ فارسی موفق است.
این اصلاح‌های محدود، پذیرش کل مدل نیستند. هش بومی در بخش انگلیسی همین رکورد آمده است.
توقف اختصاصی و بازخوانی جداگانهٔ واحد غیرفعال/PID0/نبود listener/خط مبنای آماده و بی‌درخواست
موفق‌اند. هر پنج کنترل CI کد دقیق موفق است؛ CI یا پاسخ جایگزین، امتیاز خام را تغییر نمی‌دهد.

آزمایش متفاوتِ بعدی: قواعد شرط نوع حفظ، استنتاج قطعیِ واسط/خرابی بالادست از کد خطا ممنوع و
منبع/دامنه/مشاهده/گردآوری/محدودیت در جملهٔ مشاهده عنوان‌دار شوند. نام میزبان به‌تنهایی دامنهٔ
مجاز نیست؛ مقدار غایب نامعلوم می‌ماند. مقدار یا پاسخ ثابت و تطبیق سؤال اضافه نمی‌شود.
درخواستِ نمایهٔ اختیاری۳۰۰ثانیه از کد دقیق ثبت و هر شانزده پرسش ثابت با همان Q8/runtime/۳۲
رشته/16K/۳۸۴توکن/نمونه‌گیری/یک جایگاه/۴۸ GiB آزموده شود. watchdog محدود۲۱۰۰ثانیه و سقف
کنترل۲۲۰۰ثانیه حفظ شوند؛ عبور از مهلت کلی شکست است، نه حذف معیار. مهلت صریح۳۰۰ از سابقهٔ
۱۲۰ جدا ثبت شود. تا رفع شکست معنایی، انتخاب زنده مجاز نیست؛ معیار مستقل/برنامه/استدلال/
حریم خصوصی/زمینه/شاهد/WAN/بازگشت جدا باقی است.

### آزمایش اصلاح کیفیت پاسخ خام — ۶ اکتبر ۲۰۲۶

مالک، اصلاح خطای خامِ کدنویسی و نتیجه‌گیری را خواسته است، نه امتیاز دادن به پاسخ جایگزین
برنامه. دستور بومیِ مخصوص نامزد اکنون شرط نوعِ زمان اجرا را پیش از سنجش مقدار قرار می‌دهد،
نتیجهٔ TCP/HTTP را به واقعیت مشاهده‌شده محدود می‌کند و منبع، زمان کامل، دامنهٔ مجاز و قید
کهنگی/نقص را با شناسهٔ فنیِ دست‌نخورده لازم می‌داند. این قواعد عمومی فقط از زبان و سقف خروجیِ
معتبر استفاده می‌کنند؛ پاسخ ثابت یا تطبیق متن سؤال ندارند. این تغییر، دستور است؛ نه آموزش،
مجوز یا شاهدِ بهبود اندازه‌گیری‌شدهٔ مدل.

برنامهٔ پذیرش: درخواست هر شانزده پرسش ثابت EN/FA از نگاشتِ کد دقیق ثبت شود؛ سپس Q8 موجود با
runtime بدون BLAS، ۳۲ رشته، زمینهٔ 16K، سقف خروجی ۳۸۴، نمونه‌گیری ثابت، مهلت۱۲۰ ثانیه، یک
جایگاه و سقف حافظهٔ۴۸ GiB اجرا شود. پاسخ نهایی مستقیماً با معیار معنایی و کنترل محدودِ کد
سنجیده شود؛ پاسخ جایگزین برنامه دخیل نیست. بازبینی عامل اصلی از تأیید مستقل جدا ثبت شود.
دریافت تازه، تغییر مدل/runtime/پرامپت و تنظیم زنده/استدلال عمومی/صف/منابع در دامنه نیست.
در شکست، گزارش حفظ و فقط واحد موقتِ اختصاصی متوقف و بازخوانی شود؛ مدل زندهٔ35B آماده و
بی‌درخواست ثابت بماند. نتیجهٔ تاریخی Q8 با۱۲ موفقیت از۱۶ و شکست Q5 محفوظ‌اند. معیارهای
برنامه‌ـ‌پراکسی، استدلال/حریم خصوصی/زمینه، شاهد/WAN و بازگشت همچنان بازند.

### نتیجهٔ زمان — ساعت ۱۱:۵۳:۴۴ UTC

آزمون دوپرسشی Q5 موجود با مهلت۳۰۰ ثانیه، پاسخ EN/FA را در۸۸۴۴۱/۱۴۵۰۱۰ میلی‌ثانیه ثبت
کرد؛ هر دو معیار محدودِ فرضیه را در بازبینی عامل اصلی گذراندند. چهارده مورد با این مهلت
اجرا نشده‌اند. هش: `96813c347b8035d592c941ffc6ead9d1a0250dfa4f9347b730a57ab49e0275c5`.
توقف/بازخوانی جداگانهٔ خط مبنا و پنج کنترل CI کد `5e15b5c` موفق‌اند. مهلت صریحِ ابزار آفلاین،
۳۰۰ را جدا از۱۲۰ِ مجموعهٔ ثابت ثبت می‌کند؛ پیش‌فرض هنوز پاسخ دیرهنگام فارسی را ناموفق می‌داند.
معناشناسی کامل مدل/مستقل/برنامه‌ـ‌پراکسی/استدلال/حریم خصوصی/زمینه/شاهد/WAN/بازگشت بازند؛
مدل زندهٔ35B و پیش‌فرض‌ها ثابت‌اند.

### نمایهٔ پاسخ طولانی با مجوز مالک — ۶ اکتبر ۲۰۲۶

[اصلاح زمان](PROMPT_CHANGELOG.md) سقف مهلت را برای آزمون جدید تغییر می‌دهد، نه نتیجهٔ گذشته
یا معیار معنایی را. مهلت پیش‌فرضِ مدل/برنامه/پراکسی ۱۲۰/۱۵۰/۱۸۰ ثانیه می‌ماند. فقط نامزدهای
دقیق Q8 و Q5 با گفت‌وگوی گسترش‌یافته و پرچم صریح
`NEXTOPS_QWEN38_EXTENDED_TIMEOUT_ENABLED=1` می‌توانند تا ۳۰۰ ثانیه پاسخ دهند؛
زمینهٔ 16K و منع استدلال ثابت است. نمایه‌های اختیاری، مهلت‌های ۳۰۰/۳۳۰/۳۶۰ ثانیه را در سه
مرز هماهنگ می‌کنند. انتظار نامحدود، صف بزرگ‌تر، دستور تازه، مدل تازه یا منابع بیشتر در دامنه نیست.
کنترل پیش‌فرض، فعال‌سازی صریح، سقف، مدل ناسازگار، زمینه، منع استدلال، کوتاهی بررسی آمادگی
و ثبات مسیر عادی آزموده شوند. دستورهای ثابتِ کد ثبت‌شده برای دو پرسش فرضیهٔ EN/FA روی Q5
و runtime محافظت‌شدهٔ موجود اجرا شوند؛ زمان واقعی، کیفیت، شکست، توقف فرایند اختصاصی و
بازخوانی جداگانهٔ خط مبنای آماده و بی‌درخواست ثبت شوند. چهارده پرسش دیگر در این نمایه اجرا
نشده‌اند. خودبازبینی تأیید مستقل نیست و شکست توپولوژی/کد/منشأ همچنان مانع انتخاب مدل است.
بازگشت با حذف نمایه‌ها و بازگرداندن دو دستور ۱۸۰ ثانیه‌ای پراکسی، کنترل پیکربندی پیش از
بارگذاری و تعیین وضعیت درخواست جاری در تغییر مجازِ جدا انجام می‌شود. این تغییر کد به دست‌کاری
فایل یا راه‌اندازی مجدد زنده نیاز ندارد؛ معیارهای WAN، زمینه، استدلال، برنامه و بازگشت بازند.

### شکست کیفیت در مقایسهٔ متفاوت Q8 — ساعت ۱۱:۱۹:۵۹ UTC

مقایسهٔ کاملِ برنامه‌ریزی‌شدهٔ Q8/دستور بازگردانده‌شده/runtime بدون BLAS واقعاً شانزده مهلت
پاسخ را گذراند، اما بازبینی معنایی صرفاً عامل اصلی **دوازده موفق/چهار ناموفق** است: ادعای
توپولوژی در هر دو زبان، شرط نوع کد فارسی و دامنهٔ مجاز فارسی. هر دو نمونهٔ فرضیه معیار
ثابتِ محدود را گذراندند، نه پذیرش مستقل یا کلی مدل. هش گزارش بومی
`b13ddbcb8e71555c81ff951126a4900eed0b7bf46f200ba7444a847c434a34f8`، شکست‌های محدود و
بازخوانی جداگانهٔ توقف/نبود شنونده/ثبات خط مبنای آماده و بی‌درخواست حفظ شوند. پنج کنترل CI
کد دقیق `4ac2cf4` موفق‌اند. آزمون یکسان تکرار، دقت کم، معیار آسان، مدل تغییر نام یا خدمت زنده
عوض نشود. آزمون بعدی به راهبرد متفاوتِ واقعاً توجیه‌شده و بازبینی لازم نیاز دارد؛ معیارهای
استدلال/برنامه/زمینه/شاهد/WAN/بازگشت پذیرفته نیستند. هدف همچنان 3.8 واقعی است؛ هنوز زنده نیست.

### رد تشخیص سوم — ساعت ۱۰:۴۷ UTC

اجرای کامل سوم هر شانزده مهلت پاسخ نهایی را گذراند، اما بازبینی معنایی **یازده موفق/پنج
ناموفق** و صرفاً متعلق به عامل اصلی است. آزمایش عمومیِ هدف پنجاه‌واژه‌ای رد شود: کد فارسی
در هفت مرز آزمون محدود AST پسرفت کرد؛ توپولوژی شبکهٔ تأییدنشده، منشأ ناقص فارسی و نبود
فرضیهٔ علّی باقی‌اند. دستور/آزمون‌ها دقیقاً به کد `7157c3b` بازگردند و هش گزارش
`c8591c1ffa8cda6bbd4df6c165ff56b847e881c9ab419f3e72a7e488a18049dc` حفظ شود.
توقف موفق و ثبات خط مبنا پذیرش معنایی نیست. فرادادهٔ Q4 کوچک‌تر به معنی نامزد دریافت‌شده/
پذیرفته‌شده نیست و دقت را کم می‌کند، نه تعداد پارامتر. پیگیری متفاوت به بازبینی منبع/مجوز/
هش/ظرفیت/ابزار و دلیل سنجیده برای انتظار بهبود نیاز دارد؛ پرسش، مهلت و امنیت ثابت بمانند.
مدل ناموفق انتخاب، 3.5 تغییر نام، تشخیص یکسان تکرار یا خودبازبینی عامل، تأیید مستقل معرفی
نشود. معیارهای استاندارد/برنامه/استدلال/حریم خصوصی/زمینه/شاهد/WAN/بازگشت بازند؛ 35B زنده ثابت.

مقایسهٔ محدود بعدی: فایل موجود Q8 با دستور بومیِ بازگردانده‌شده و runtime بدون BLAS دارای
بازبینی پیشین، همان پرسش کامل/روش۳۲رشته‌ای/زمینه16K/خروجی۳۸۴/مهلت۱۲۰ثانیه و برچسب بازبینی
مستقل آزموده شود. آزمایش اولیهٔ Q8، دستور/runtime متفاوت و فقط هشت پرسش استاندارد داشت؛ این
تشخیص کامل متفاوت است، نه تکرار یکسان یا وعدهٔ بهبود. دریافت، انتخاب یا کاهش دقتی رخ نمی‌دهد.

### آزمون فشردهٔ ناموفق و پیگیری محدود — ساعت ۱۰:۳۰ UTC

تشخیص کاملِ دوم و دو بررسی جدا و دوپرسشیِ ۱۶/۶۴رشته‌ای نیز مهلت فارسی را نگذراندند. هویت
گزارش، یافتهٔ معنایی، توقف واقعی و ثبات خط مبنا حفظ شوند؛ بررسی محدود، چهارده سؤال دیگر را
پوشش نمی‌دهد. طول پاسخ/سابقهٔ cache متفاوت، تعداد رشتهٔ بهینه را ثابت نمی‌کند. آزمایش عمومیِ
بعدی، فقط برای بودجهٔ خروجی کوچک هدف پنجاه‌واژه‌ای دارد، نه به قیمت حذف واقعیت/کد/قالب/منشأ
ضروری؛ زمان فنیِ لاتین در فارسی را صریحاً حفظ و تعداد جمله/منشأ پاسخ را کنترل می‌کند. معنای
کد خطا، اثبات توپولوژیِ مشاهده‌نشده نیست. پرسش/نمونه‌گیری/مهلت/زمینه/فایل/امنیت ثابت‌اند؛
این نیز تشخیص عامل اصلی است، نه پذیرش.

### شکست مشاهده‌شده و آزمون جدا با دستور فشرده — ۶ اکتبر ۲۰۲۶

نخستین تشخیص با دستور بومی واقعاً در آخرین پرسش فارسی به پایان مهلت رسید. بازبینی عامل اصلی،
با همان معیار، دوازده موفقیت/چهار شکست ثبت کرد: توپولوژی تأییدنشدهٔ شبکه در فارسی، حذف دامنهٔ
مجاز در دو پاسخ کهنه و پایان مهلت. گزارش محافظت‌شده و کنترل جداگانهٔ توقف/نبود شنونده/ثبات
خط مبنای آماده و بی‌درخواست حفظ شود. آزمایش بعدی، حذف دامنه/زمان کامل را صریحاً منع می‌کند،
عبارت‌های عمومی را فشرده و کوتاه‌ترین پاسخ کامل را می‌خواهد. این آموزش، مسیریابی تازهٔ پاسخ،
تکرار همان تلاش یا پذیرش مستقل نیست. روش بومی و همهٔ سقف‌های ثابت حفظ شوند؛ تا باقی‌بودن
شکست استاندارد، معیار استدلال یا تغییر مدل زنده آغاز نشود.

### اولویت تازهٔ مالک و اصلاح محدودِ نامزد — ۶ اکتبر ۲۰۲۶

مالک، Qwen **3.8** را حتی با پارامتر کمتر در اولویت گذاشته و انجام کار را به عامل اصلی سپرده
است. جایگزین 3.5 هدف را برآورده نمی‌کند. ادامه از فایل کامل و ثابتِ 27B Q5 باشد، نه تکرار انتقال
متوقف‌شدهٔ 122B. سوابق انتقال و بستهٔ بازبینیِ پذیرفته‌نشدهٔ نسخهٔ سوم حفظ شوند؛ این دستور،
بازبینی عامل اصلی را مستقل نمی‌کند و مجوز انتشار مدل ناموفق نیست.

اصلاح کد، دستور پاسخ عمومیِ فشرده و بومیِ هر زبان برای دو نامزد دقیقِ 3.8 است: منبع، زمان کامل
مشاهده و گردآوری، دامنه، قید کهنگی/نقص، وضعیت فعلیِ نامعلوم، فرضیهٔ مشروط و بررسی نوع پیش از
مقایسه در کد حفظ می‌شوند. فقط زبان و بودجهٔ خروجیِ معتبر مبنا هستند، نه کلیدواژهٔ سؤال یا پاسخ
ساختگیِ آزمون. دستور مدل زندهٔ 3.5 و خلاصه‌سازی شاهد ثابت بماند. پرسش و معیار ثابت، نمونه‌گیری،
مهلت ۱۲۰ ثانیه، زمینهٔ 16K و ممنوعیت استدلال نامزد تغییر نکنند.

ترتیب پذیرش: آزمون محلیِ دستور/رابط/امنیت؛ تشخیص بومیِ استاندارد در محیط جدا؛ بازبینی معنای
تمام پاسخ‌ها و شکست زمانی؛ سپس برنامهٔ هماهنگ، استدلال با نمایش صرفاً پاسخ نهایی، زمینهٔ سنجیده،
شاهد/ممیزی/آفلاین و بازگشت دقیق. نتیجهٔ عامل اصلی پذیرش مستقل نیست. تلاش ناموفق حفظ شود.
بازگشت کد با برگرداندن ماژول و اتصال صرفاً نامزد انجام می‌شود؛ آزمون تشخیصی، مدل زنده را تغییر
نمی‌دهد. آموزش مدل، GPU، ابر، دانلود، مجوز زیرساخت یا تغییر معماری افزوده نمی‌شود.

### پیگیری محدود پس از آزمون ناموفق Q8

[گزارش تاریخ‌دارِ مجوز آزاد](PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md)، پس از شکست کدنویسی/
زمینهٔ Q8، آزمون مستقل و ثابتِ 27B UD-Q5_K_M را می‌افزاید. اندازهٔ وزن کمتر می‌شود، نه شمار
پارامتر. هش کامل، قالب واقعی، بارگذاری CPU، کدنویسی با پرسش ثابت/مستقل، پاسخ استانداردِ
دوزبانه، استدلال با نمایش صرفاً پاسخ نهایی و زمینه/تأخیر واقعی باید جدا پذیرفته شوند. معیارهای
تاریخی Q8 و نامزد جایگزینِ 122B حفظ‌اند. راهنمای عمومیِ کدنویسی دفاعی، تغییر کد است، نه آموزش،
مسیریابی کلیدواژه یا اثبات بهبود. تمام الزام‌های امنیت، آفلاین، مهلت، منابع، بازگشت و مستندات
زیر در این پیگیری نیز برقرارند. هویت زنده و استدلال عمومی تا پذیرش هماهنگِ برنامه ثابت می‌مانند.

### مسئله و الزامات

هدف، بهبود واقعیِ پیروی از دستور، پاسخ فنی و کدنویسی، ادامهٔ گفتگو و استدلالِ محدود در هر دو
زبان است. مدل زندهٔ 35B با نامزد دقیق‌ترِ Qwen3.8-27B Q8 مقایسه می‌شود؛ 27B بزرگ‌ترین مدل
نیست و امتیاز سازنده، درستی پاسخ NextOps را اثبات نمی‌کند. تصویر تازهٔ مالک برای DS-C، ظرفیت
گردشدهٔ ۳٫۴۹ TB، تخصیص ۱٫۷۹ TB و فضای آزاد ۱٫۷۱ TB را نشان می‌دهد؛ مالک نبود فضای رزروشده
را اعلام کرده است. تصویر میزبان، حافظهٔ کل ۱٫۳۱ TB، مصرف ۲۱۳٫۶۴ GB، آزاد ۱٫۱ TB و ۱۱۲ CPU
با نام Platinum 8280 را نشان می‌دهد. این‌ها شاهد ارسالی و اظهار مالک‌اند، نه حسابرسی کامل رشد
ماشین‌ها، ظرفیت پایدار یا تأیید جای‌گیری فیزیکی NUMA.

پیش‌بررسی مستقیم مهمان: ۸۰ vCPU آنلاین، حافظهٔ قابل‌استفادهٔ ۱۲۸۷۶۹ MiB، مقدار در دسترس
۱۰۷۶۶۴ MiB، مصرف صفر swap، یک گرهٔ NUMA/۸۰ سوکت مجازی، قابلیت AVX-512/VNNI و فضای آزاد
۱۶۹۵۵۷ MiB در حجم مدل. سقف خدمت زنده همچنان ۹۶ GiB و سهم CPU معادل ۱۸ است. حافظهٔ آزاد
میزبان، حافظهٔ تخصیص‌یافته به مهمان نیست. یک نامزدِ ۲۹۰۴۷۰۸۶۰۴۸ بایتی و فضای محدودِ بخش‌ها/
مونتاژ آن در حجم موجود جا می‌گیرند؛ افزایش ماشین، دیسک، رزرو یا سقف خدمت لازم نیست. حاشیهٔ
۹۰۰ GiB برای DS-C هدف ایمنی است، نه رزرو تنظیم‌شده. سقف سه‌ترابایتی و منابع ESXi، برنامه،
اتصال‌دهنده، پایگاه‌ها و زبیکس حفظ شوند.

### موارد خارج از دامنه، تهدیدها و وابستگی‌ها

ابر/GPU، چارچوب جایگزین، ابزار یا مجوز عملیاتی تازه، تغییر schema، خروجی/زمینه/صف نامحدود،
نمایش یا ذخیرهٔ استدلال خصوصی و دانلود زمان اجرا مجاز نیستند. از تصاویر میزبان، وضعیت زندهٔ
زیرساخت برای پاسخ ساخته نشود. runtime ثابت و مدل سالم حفظ شوند. فایل مدل، قالب، متن پایش و
کد تولیدشده غیرقابل‌اعتمادند و مجوز نمی‌دهند. GGUF شخص ثالث، تبار Qwen3.8-27B را اعلام می‌کند؛
نسخهٔ دقیقِ منبع تبدیل هنوز تأیید نشده و این محدودیت باید ثبت بماند. این artifact انتشار رسمیِ
GGUF از Qwen نامیده نشود. Apache-2.0 ثبت شود؛ شرایط مجوز اختصاصی Flash جدا بررسی شوند.

### برنامه و گام‌ها

۱. دامنهٔ تغییر خصوصی، ظرفیت تازهٔ ارسالی و کنترل مستقیم مهمان، mount و runtime ثبت شوند.
۲. فقط یک artifactِ Q8 از نسخهٔ ثابت، با زنجیرهٔ پراکسی موجود آماده شود. انتقال محدود و اندازه/
هش کامل بررسی شوند. تلاش ناقص حفظ شود و هرگز انتخاب نشود؛ ادامهٔ هشت‌بخشی، آماده‌سازی است،
نه دانلود زمان اجرا.
۳. پس از تأیید هش، معماری و قالب/tokenizer و metadata واقعی بررسی شوند. آزمون مستقلِ CPU فقط
روی loopback، با یک جایگاه، سقف صریح حافظه/CPU/زمان، کنترل بیکار بودن مدل زنده و بدون اطلاعات
ورود مقصد اجرا شود؛ هنگام تحویل، فرایند آزمایشی متوقف باشد.
۴. رابط موجود با هویت دقیق نامزد استفاده شود. گزینه‌های قابل‌اعتمادِ استاندارد، استدلال و حفظ
آن را خاموش کنند؛ انتخاب مدل زنده ثابت بماند. استدلال نامزد تا پذیرش نمایهٔ هماهنگ ممنوع است.
۵. پرسش‌های ثابتِ دوزبانه برای قالب/محاسبه، پیگیری گفتگو، DNS/TCP/HTTP/فایروال/خدمت، کدنویسی
و منشأ/شاهد کهنه، ناقص، غایب و تزریق ثبت شوند. پاسخ نهایی و مصرف/زمان اندازه‌گیری و استدلال
خصوصی فوراً دور ریخته شود. صحت معنا بررسی شود، نه فقط HTTP 200 یا شمار توکن.
۶. پیش از تغییر خدمت، تعداد رشته در آزمون مستقل و محدود سنجیده شود. Flash-Next از نظر سازگاری
واقعی CPU، مصرف کامل و مجوز جدا بررسی شود. پیشنهاد ۲۵۶ تا ۵۱۲ GiB، تغییر اجراشده یا مقدار
بهینهٔ تضمین‌شده نیست.
۷. تنها پس از موفقیتِ کاربردپذیری، حریم خصوصی و مهلت، مسیر هماهنگ برنامه/API، شاهد تازهٔ مجاز
فارسی/انگلیسی و ممیزی، شروع/راه‌اندازی دوباره بدون WAN، خرابی/صف و بازگشت/استقرار دوباره
پذیرفته شوند. شکاف reboot/شروع سردِ قابل‌اعمال، اجرا‌نشده ثبت شود، نه موفق.

### پذیرش، بازگشت و مستندات

هش کامل، بارگذاری CPU و قالب، معیارهای جدا هستند. مهلت موجودِ هر پاسخ ۱۲۰ ثانیه است؛ timeout
شکست است و به افزایش پنهانی مهلت منجر نمی‌شود. یک درخواست فعال/دو منتظر، کنترل زمینه، جداسازی
نشست/مالک، منشأ/زمان/دامنه و کنترل صحت حفظ شوند. دانش مدل شاهد زنده نیست و منبع خراب با منبع
دیگر جایگزین نشود. هنگام تحویل، فرایند دانلود، خدمت آزمایشی یا تایمر بدون نظارت باقی نماند.
بازگشتِ ورود فایل به restart خدمت نیاز ندارد؛ لینک و تنظیم مدل سالم تغییر نکرده‌اند. انتخاب
بعدیِ نمایه، artifact/تنظیم دقیق، بازگشت زمان‌دار و آزمون تازهٔ ورود، پاسخ، شاهد و ممیزی لازم
دارد. downgrade مخرب یا حذف خودکار مدل/snapshot ممنوع است.

راهنمای CPU دو زبان، وضعیت/کار بعدی، manifest نامزد، آزمون‌های محلی و فهرست context به‌روز
شوند. سابقهٔ شکست استدلال و استقرار رابط حفظ شود. ثبت هویت در کد، تغییر مدل زنده نیست؛ manifest
انتشار زنده فقط با تغییر پذیرفته‌شدهٔ واقعی به‌روز شود.
