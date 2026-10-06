# Qwen 3.8 qualification / پذیرش فنی Qwen 3.8

Status: bounded existing-guest trial, authorized by the owner's upgrade/resource instructions
on 2026-10-05. Not a serving-model selection, new production acceptance or permission to erase
other workloads. [CPU guide](../en/CPU_AI.md) / [راهنمای CPU](../fa/CPU_AI.md).

## English

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

### نمایهٔ پاسخ طولانی با مجوز مالک — ۶ اکتبر ۲۰۲۶

[اصلاح زمان](PROMPT_CHANGELOG.md) سقف مهلت را برای آزمون جدید تغییر می‌دهد، نه نتیجهٔ گذشته
یا معیار معنایی را. مهلت پیش‌فرضِ مدل/برنامه/پراکسی ۱۲۰/۱۵۰/۱۸۰ ثانیه می‌ماند. فقط نامزدهای
دقیق Q8 و Q5 با گفت‌وگوی گسترش‌یافته و پرچم صریح بالا می‌توانند تا ۳۰۰ ثانیه پاسخ دهند؛
زمینهٔ 16K و منع استدلال ثابت است. نمایه‌های اختیاری، مهلت‌های ۳۰۰/۳۳۰/۳۶۰ ثانیه را در سه
مرز هماهنگ می‌کنند. انتظار نامحدود، صف بزرگ‌تر، دستور تازه، مدل تازه یا منابع بیشتر در scope نیست.
کنترل پیش‌فرض، فعال‌سازی صریح، سقف، مدل ناسازگار، زمینه، منع استدلال، کوتاهی بررسی آمادگی
و ثبات مسیر عادی آزموده شوند. دستورهای ثابتِ کد ثبت‌شده برای دو پرسش فرضیهٔ EN/FA روی Q5
و runtime محافظت‌شدهٔ موجود اجرا شوند؛ زمان واقعی، کیفیت، شکست، توقف فرایند اختصاصی و
بازخوانی جداگانهٔ خط مبنای آماده و بی‌درخواست ثبت شوند. چهارده پرسش دیگر در این نمایه اجرا
نشده‌اند. خودبازبینی تأیید مستقل نیست و شکست توپولوژی/کد/منشأ همچنان مانع انتخاب مدل است.
بازگشت با حذف نمایه‌ها و بازگرداندن دو دستور ۱۸۰ ثانیه‌ای پراکسی، کنترل پیکربندی پیش از
بارگذاری و تعیین وضعیت درخواست جاری در تغییر مجازِ جدا انجام می‌شود. این تغییر کد به دست‌کاری
فایل یا راه‌اندازی مجدد زنده نیاز ندارد؛ معیارهای WAN، زمینه، استدلال، برنامه و بازگشت بازند.

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
