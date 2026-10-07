# Qwen 3.8 Flash-Next preparation / آماده‌سازی Qwen 3.8 Flash-Next

Status: **partial provisioning, private development only, unselected**. This dated increment follows
the [failed 27B trial](QWEN38_QUALIFICATION_2026-10-05.md), not a replacement of its results.
[English CPU guide](../en/CPU_AI.md) / [راهنمای فارسی](../fa/CPU_AI.md).

## English

### Bounded problem and sequence

The owner requests larger-model development after manually expanding the existing AI guest.
Improve measured EN/FA instruction following, technical/coding answers and final-only thinking;
do not infer accuracy from parameter count. Inspect pinned source/license and actual first-shard
metadata, prepare only the identified blank added disk, verify bounded transfer behavior, improve
the frozen evaluation corpus, then perform full-artifact and isolated CPU qualification. Customer
publication remains separate from private development and requires license applicability review.

No ESXi/VM resize, original-disk change, GPU/runtime migration, target permission, prompt change,
application/AI deployment, new database schema or public thinking enablement occurred. Preserve
the serving 35B, exact runtime, existing application policy, source/time/scope and audit controls.

### Observed resources and storage

Direct checks after the owner-managed boot show 80 online vCPUs, 80 virtual sockets, three guest
NUMA nodes and 257905 MiB usable RAM (about 251.86 GiB). Swap use is zero. Only VMware virtual
graphics is visible; the legacy NVIDIA/audio passthrough assignments are absent. Guest NUMA
observations do not prove physical placement or an optimal inference thread count.

The added 400-GiB disk was resolved through its stable private device path and repeatedly checked
for exact size, absence of partitions, filesystem signatures, mounts, holders and configuration.
Only this blank disk was formatted as ext4 with 1% reserved space. It is mounted separately at
`/srv/nextops/models/large`: approximately 393 GiB filesystem / 389 GiB available after formatting,
with `nodev,nosuid,noexec`. The UUID-based boot entry uses `nofail` and a 10-second device timeout;
the previous fstab and exact identity are retained privately. Original model paths are not covered
by this mount. Existing disk/model links, baseline PID and zero service-restart count remained
unchanged, with `/readyz` HTTP 200 after preparation. Boot persistence has **not** been tested.

Current native serving limits remain 96 GiB / 18 CPU equivalents. These cannot simply be reused
for a 151.46-GiB Q8 artifact. A future separate loopback trial requires an explicit complete-memory
budget (resident weights, page cache, state and buffers), monitored baseline/OS headroom and stop
conditions. Do not sum guessed NUMA averages, start an oversized concurrent trial or claim full
memory fit from a metadata shard. The owner's fresh supplied DS-C observation remains capacity
evidence, not unlimited storage authorization; preserve the project ceiling and free-space guard.

### Pinned candidate and actual metadata

The [candidate manifest](../../deploy/inference/qwen3-8-flash-next-q8.candidate.json) pins
`ggml-org/Qwen3.8-Flash-Next-GGUF` at `052beeaca7bec4a303e59cc7bc630c4f3a1b845d`, Q8_0,
two shards totalling **162624826784 bytes (about 151.46 GiB)**. This is a ggml-org conversion,
not an official Qwen-published GGUF. The pinned `.src_sha` resolves the declared conversion source
to the official upstream revision `de4b8e4d43b917e7706784d8bb445c9af86a3540`; this is source
provenance, not reproduction of the conversion or weight-level equivalence verification.

The complete 10945440-byte metadata shard passed SHA-256 verification. Actual GGUF v3 metadata:
`qwen4exp`, 48 layers, 2560 embedding width, two splits, 1224 total tensors and template SHA-256
`c3cf9e34abf4f9e36c2d72165aa9c132d3e2a725b6c2586aaa3a8af9d7a81041`. The first shard contains
zero tensors; it is **not** a complete model. The pinned runtime source contains `QWEN4EXP`, but
actual CPU loading and tokenizer/template application are not run. Native 262144 context metadata
is not accepted NextOps context; the trial remains bounded to 16384 and a 120-second deadline.

One 32-MiB range sample completed in 8.232 seconds at 4075933 bytes/second. Four parallel 128-MiB
ranges completed in 30.09–30.54 seconds each: 536870912 bytes staged. Exact range headers/sizes
were checked; local chunk hashes were recorded for resumption. These do not replace the expected
complete-shard SHA-256. Full weights are **not imported or selected**. Partial/sample data remains
protected; no download or trial process remains running at handoff. The licensed full-import
decision and finite resume/assembly/full-hash qualification are the next provisioning tasks.

### Customer-facing license consideration

The [pinned official license](https://huggingface.co/Qwen/Qwen3.8-Flash-Next/blob/de4b8e4d43b917e7706784d8bb445c9af86a3540/LICENSE)
is **Qwen Community License 1.0**, not Apache-2.0. A protected copy was provisioned; SHA-256:
`a0dc422560841fd68e06d974907f8b4c709bca44a67daad2b528437bdf676c08`.
The owner confirms intended Bank/customer staff access, so an internal-only deployment exception
cannot be assumed. Commercial Model-as-a-Service or AI Work Assistant businesses may require a
separate Qwen license; the domain-specific assistant exclusion is not a blanket exemption from
the separate Model-as-a-Service definition. Applicability to NextOps/OCS and any affiliate must be
reviewed before customer exposure. No organizational approval or separate license was supplied.
Private isolated development is not customer publication or an assertion of legal clearance.

### Source implementation and regression review

- `scripts/inspect_gguf_metadata.py`: bounded offline full-file identity check and metadata reader;
  does not load tensors or emit raw templates/vocabulary. Actual small-shard inspection ran.
- `deploy/inference/model-qualification-corpus.json`: 16 paired synthetic cases; the original
  eight questions are unchanged and their canonical fingerprint is regression-tested. Additional
  cases cover missing/stale/partial evidence, untrusted instructions and unproven causal claims.
- `scripts/check_model_coding_invariant.py`: interprets only a small, bounded pure-function AST;
  never imports, compiles or executes generated Python. Finite cases include spoofed equality,
  unhashable values, bytes, case sensitivity and whitespace. This is not a proof for arbitrary code
  or an authorization boundary; unsupported code requires manual review.
- `scripts/review_model_trial.py`: offline, bounded private-report review; no network/model calls,
  no overwrites, no copied answers/private reasoning and no automatic acceptance. Exact checks
  cannot conceal missing cases, truncation, the 120-second deadline or required semantic review.
- Actual retained baseline/32-thread 27B standard samples were reviewed privately. Both coding
  answers fail EN and FA; four digit/recall checks pass per profile, network semantics remain
  manually reviewed. This is review of old samples, **not** a new generation or Flash evaluation.

Before changes: 622 passed, 2 POSIX/Windows skips, 85 deselected (22.07 seconds). With new code:
**660 passed, 2 skips, 85 deselected**, one existing AnyIO deprecation warning (21.16 seconds).
Commands:

```powershell
uv run --extra dev --extra mcp --frozen pytest -m "not integration and not browser" -q
uv run --extra dev --extra mcp --frozen ruff check packages tests scripts deploy/installers
uv run --extra dev --extra mcp --frozen ruff format --check packages tests scripts deploy/installers
uv run --extra dev --extra mcp --frozen mypy --platform linux packages tests scripts deploy/installers
uv run --frozen python -X utf8 scripts/check_docs.py
uv run --frozen python scripts/check_inference_artifacts.py
uv run --frozen python scripts/check_release_status.py
uv build --no-sources --offline
```

Ruff check/format passed 133 files; Linux-target mypy passed 132 source files. Documentation and
artifact/status validators are source/structure checks, not deployment or model acceptance.
The dossier validator checks the original role-budget proposals, not the resized live inventory.
The offline wheel/sdist build passed; these new development tools are run from the source checkout,
not installed as runtime endpoints. Docs passed 138 Markdown / 39 language pairs; inference/status/
dossier validators passed. A broad directory secret scan reported 17 matches: 15 in ignored virtual-
environment dependencies and two in unchanged idempotency-test/archive prose. They are not new
credential findings. The source-commit range Gitleaks scan passed; no scanner control was removed.
Initial lint/type/test-import problems were repaired and rerun; one private transfer used the wrong
local checkout and stopped before copying/reviewing code, then succeeded with the correct workdir.
No dependency, lockfile or security-boundary relaxation was needed. New browser/PostgreSQL/live
integration/WAN/reboot testing is not implied by the non-browser source command.

Private offline review, after transferring these tools beside the corpus (never raw reports into
Git):

```bash
python3 -m scripts.review_model_trial --input /protected/recorded-standard.json --output /protected/new-review.json
```

The command needs the repository root as its working directory, private paths outside the checkout
and exclusive output. Exit 1 means a failed finite check; exit 2 means partial/manual/unrun review.
It intentionally has no full-acceptance exit and cannot select a model.

### Remaining gates, threats and rollback

| Gate | Observed status |
|---|---|
| New volume, exact small-shard identity/metadata | passed within stated preparation scope |
| Complete two-shard import | partial |
| Customer-facing license review | partial; applicability/organizational decision missing |
| Actual CPU load, tokenizer/template, complete memory fit | not_run |
| Flash standard/thinking EN/FA, coding/technical semantics | not_run |
| Expanded context, queue/resource/latency comparison | not_run |
| Matched app/evidence/audit, WAN/restart/reboot/cold start | not_run |
| Selected-model rollback/reapply | not_run; serving selection never changed |

Keep the old failed-context/coding tests frozen. Never solve them by widening deadlines, changing
the test question, hiding failed samples, displaying private reasoning or inventing live evidence.
Artifacts, templates, monitoring notes and generated code are untrusted and grant no permissions.
Do not place target credentials in the trial, enable a cloud fallback or fetch weights at runtime.

No serving rollback is needed for this preparation: no live model/configuration was changed. For
new-volume withdrawal, reconcile all readers/downloads, verify exact mount identity, remove only
the added boot entry under a reviewed change and unmount it; preserve verified/partial data and
the private configuration backup. Do not reformat, delete VMDKs/snapshots or replace a later fstab
wholesale. A future serving cutover still requires exact retained artifacts/configuration and a
timed rollback/reapply test with fresh authenticated answers, evidence and audit. Update the paired
CPU/testing guides, state/next checkpoint and manifest for actual results only.

<div dir="rtl">

## فارسی

### دامنه و ترتیب اجرا

مالک پس از افزایش دستی منابع ماشین AI، توسعه و ارتقای مدل بزرگ‌تر را خواسته است. هدف، بهبود
سنجیدهٔ پیروی از دستور، پاسخ فنی و کدنویسی و استدلالِ محدود در دو زبان است؛ تعداد پارامتر،
درستی پاسخ را ثابت نمی‌کند. ترتیب کار: بررسی منبع و مجوز ثابت، خواندن metadata واقعی، آماده‌سازی
فقط دیسک تازه و خالیِ شناسایی‌شده، سنجش انتقال محدود، تکمیل آزمون‌های ثابت و سپس پذیرش فایل
کامل و اجرای مستقل روی CPU. ارائه به مشتری، از توسعهٔ خصوصی جدا و نیازمند بررسی مجوز است.

ESXi، اندازهٔ ماشین، دیسک اصلی، GPU، runtime، مجوز مقصد، دستور مدل، schema، استقرار برنامه/AI
و فعال‌سازی استدلال عمومی تغییر نکرده‌اند. مدل زندهٔ 35B، سیاست برنامه، منبع/زمان/دامنه و ممیزی
حفظ‌اند؛ سابقهٔ شکست آزمون 27B بازنویسی نشده است.

### منابع و ذخیره‌سازیِ مشاهده‌شده

بررسی مستقیم پس از روشن شدن ماشین، ۸۰ vCPU، ۸۰ سوکت مجازی، سه گرهٔ NUMA مهمان و حافظهٔ
قابل‌استفادهٔ ۲۵۷۹۰۵ MiB، حدود ۲۵۱٫۸۶ GiB، را نشان داد؛ swap مصرف نشده است. فقط گرافیک مجازی
VMware دیده می‌شود و واگذاری PCI کارت‌های قدیمی NVIDIA/صدا وجود ندارد. این مشاهده، جای‌گیری
فیزیکی NUMA یا تعداد بهینهٔ رشتهٔ مدل را تأیید نمی‌کند.

دیسک افزودهٔ ۴۰۰ GiB با مسیر ثابتِ خصوصی و اندازهٔ دقیق شناسایی و نبود پارتیشن، امضای فایل‌سیستم،
mount، استفاده‌کننده و تنظیم قبلی دوباره بررسی شد. فقط همین دیسک خالی با ext4 و یک درصد فضای
رزرو قالب‌بندی و جداگانه در `/srv/nextops/models/large` متصل شد: حدود ۳۹۳ GiB فایل‌سیستم و
۳۸۹ GiB فضای در دسترس. گزینه‌های `nodev,nosuid,noexec` اعمال شده‌اند. ورودی راه‌اندازی بر پایهٔ
UUID، با `nofail` و مهلت ده‌ثانیه‌ای است؛ نسخهٔ پیشین fstab و هویت دقیق، خصوصی نگه‌داری می‌شوند.
این mount مسیر مدل زنده را نمی‌پوشاند. دیسک اصلی، لینک مدل، PID و شمار صفرِ restart ثابت ماندند
و پاسخ `/readyz` پس از آماده‌سازی HTTP 200 بود. پایداری mount پس از reboot هنوز آزموده نشده است.

سقف خدمت زنده همچنان ۹۶ GiB و سهم CPU معادل ۱۸ است؛ این نمایه برای فایل Q8 با اندازهٔ
۱۵۱٫۴۶ GiB قابل استفادهٔ مستقیم نیست. آزمون آینده باید بودجهٔ کاملِ حافظهٔ مقیم، کش، وضعیت و
بافرها، حاشیهٔ خدمت سالم/سیستم‌عامل و شرط توقف داشته باشد. جمع میانگین‌های حدسی NUMA، اجرای
هم‌زمانِ بیش‌ازظرفیت یا استنباط مصرف کامل از یک فایل metadata مجاز نیست. شاهد تازهٔ DS-C،
مجوز مصرف نامحدود نیست؛ سقف پروژه و حاشیهٔ فضای آزاد حفظ شوند.

### هویت نامزد و انتقال

manifest، نسخهٔ `052beeaca7bec4a303e59cc7bc630c4f3a1b845d` از GGUFِ ggml-org را با Q8_0،
دو فایل و مجموع ۱۶۲۶۲۴۸۲۶۷۸۴ بایت، حدود ۱۵۱٫۴۶ GiB، ثابت می‌کند. این تبدیل ggml-org است،
نه انتشار رسمیِ GGUF از Qwen. فایل ثابتِ `.src_sha` به نسخهٔ رسمی بالادست
`de4b8e4d43b917e7706784d8bb445c9af86a3540` ارجاع دارد و وجود همان نسخه بررسی شد؛ این شاهدِ
منشأ است، نه بازتولید تبدیل یا اثبات برابری وزن‌ها.

فایل کامل metadata با اندازهٔ ۱۰۹۴۵۴۴۰ بایت و SHA-256 تأیید شد. GGUF نسخهٔ سه، معماری
`qwen4exp`، تعداد ۴۸ لایه، عرض ۲۵۶۰، دو بخش و ۱۲۲۴ tensor در مجموع را نشان می‌دهد؛ هش قالب
در بخش انگلیسی و manifest ثبت است. بخش اول هیچ tensor ندارد و مدل کامل نیست. کد runtime ثابت،
معماری `QWEN4EXP` را دارد؛ بارگذاری واقعی CPU و کاربرد قالب/tokenizer هنوز اجرا نشده‌اند.
زمینهٔ ۲۶۲۱۴۴ توکنیِ metadata، زمینهٔ پذیرفته‌شدهٔ NextOps نیست؛ آزمون به 16K و مهلت
۱۲۰ ثانیه محدود می‌ماند.

نمونهٔ انتقال ۳۲ MiB در ۸٫۲۳۲ ثانیه و با نرخ ۴۰۷۵۹۳۳ بایت در ثانیه تکمیل شد. چهار بخش هم‌زمانِ
۱۲۸ MiB، هرکدام در حدود ۳۰٫۰۹ تا ۳۰٫۵۴ ثانیه، مجموعاً ۵۳۶۸۷۰۹۱۲ بایت را آماده کردند.
اندازه و محدودهٔ HTTP بررسی و هش محلیِ بخش‌ها برای ادامه ثبت شد؛ این‌ها جایگزین هش کاملِ فایل
دوم نیستند. وزن کامل وارد یا انتخاب نشده است. نمونه و بخش‌های ناقص محافظت شده‌اند؛ هنگام تحویل،
فرایند دریافت یا مدل آزمایشی فعال نیست. تصمیم مجوز و ادامهٔ محدود، مونتاژ و هش کامل، گام بعد است.

### مجوز و ارائه به مشتری

مجوز رسمی، **Qwen Community License 1.0** است، نه Apache-2.0. نسخهٔ ثابت و هش آن خصوصی
نگه‌داری شده و در بخش انگلیسی آمده است. مالک استفادهٔ کارکنان بانک/مشتری را تأیید کرده؛ بنابراین
نمی‌توان استثنای استفادهٔ صرفاً داخلی را مبنای ارائه قرار داد. فعالیت تجاریِ Model-as-a-Service
یا AI Work Assistant ممکن است مجوز جداگانهٔ Qwen بخواهد؛ استثنای دستیار تخصصی، معافیت کلی از
تعریف مستقلِ Model-as-a-Service نیست. شمول شرایط برای NextOps/OCS و شرکت وابسته باید پیش از
دسترسی مشتری بررسی شود. تأیید سازمانی یا مجوز جداگانه ارائه نشده است. توسعهٔ مستقل و خصوصی،
ارائه به مشتری یا اعلام تأیید حقوقی نیست.

### پیاده‌سازی، آزمون و شواهد

خوانندهٔ محدودِ metadata، هویت کاملِ فایل ورودی را بدون بارگذاری tensor و انتشار متن قالب یا
واژگان بررسی می‌کند؛ روی بخش اول واقعی اجرا شد. مجموعهٔ ارزیابی ۱۶ پرسش دوزبانه دارد: هشت
پرسش قبلی با fingerprint ثابت حفظ شده‌اند و شاهد غایب/کهنه/ناقص، تزریق دستور و علتِ اثبات‌نشده
افزوده شده‌اند. ارزیاب کدنویسی فقط زیرمجموعهٔ کوچک و محدود AST را تفسیر می‌کند؛ کد تولیدشده
import، compile یا اجرا نمی‌شود. برابری فریبنده، ورودی هش‌ناپذیر، bytes، بزرگی حروف و فاصله
آزموده می‌شوند؛ نتیجه، اثبات همهٔ کدها یا مرز مجوز نیست. ساختار پشتیبانی‌نشده بازبینی دستی می‌خواهد.

بازبین گزارش فقط آفلاین کار می‌کند: تماس مدل/شبکه، بازنویسی شاهد، کپی پاسخ/استدلال خصوصی و
پذیرش خودکار ندارد. پاسخ دقیق، معیار غایب، ناقص بودن خروجی، مهلت و بازبینی معنا را پنهان نمی‌کند.
نمونه‌های استانداردِ نگه‌داری‌شدهٔ مدل زنده و 27B با ۳۲ رشته، خصوصی بازبینی شدند؛ کد هر دو مدل
در فارسی و انگلیسی مردود است، چهار معیار رقم/یادآوری هر نمایه موفق‌اند و معنای شبکه بازبینی دستی
می‌خواهد. این بازبینیِ نمونه‌های گذشته است، نه پاسخ تازه یا آزمون Flash.

پیش از تغییر: ۶۲۲ موفق، دو ردشدهٔ POSIX/Windows و ۸۵ خارج از انتخاب، در ۲۲٫۰۷ ثانیه. پس از
افزودن کد: **۶۶۰ موفق، دو اجرا‌نشده و ۸۵ خارج از انتخاب**، در ۲۱٫۱۶ ثانیه؛ یک هشدار قدیمی
AnyIO باقی است. Ruff روی ۱۳۳ فایل و mypy با هدف Linux روی ۱۳۲ فایل موفق‌اند. فرمان‌های دقیق
در بخش انگلیسی آمده‌اند. کنترل سند/manifest فقط کنترل ساختار کد است، نه پذیرش مدل یا استقرار.
خطاهای اولیهٔ lint/type/import آزمون اصلاح و دوباره اجرا شدند؛ یک انتقال خصوصی با checkout
نادرست پیش از کپی/بازبینی متوقف و با مسیر درست موفق شد. قفل، وابستگی یا مرز امنیتی تضعیف نشد.
آزمون تازهٔ مرورگر، PostgreSQL، زیرساخت زنده، WAN و reboot از این فرمان استنباط نمی‌شود.
کنترل پروندهٔ سرورها، پیشنهاد اولیهٔ بودجهٔ نقش‌ها را می‌سنجد، نه موجودی زندهٔ ماشینِ افزایش‌یافته.
ساخت آفلاین wheel/sdist موفق بود؛ ابزار تازه از کد مخزن اجرا می‌شود، نه به‌صورت endpoint زمان
اجرا. کنترل سند برای ۱۳۸ Markdown و ۳۹ جفت زبانی و کنترل manifest/وضعیت/پرونده موفق‌اند.
اسکن گستردهٔ پوشه ۱۷ تطبیق داشت: ۱۵ مورد در وابستگی‌های محیط توسعهٔ خارج Git و دو مورد در
آزمون idempotency و متن بایگانیِ تغییرنکرده. این‌ها یافتهٔ تازهٔ اطلاعات ورود نیستند. اسکن
Gitleaks محدودهٔ commit کد موفق بود و هیچ کنترل اسکن حذف نشد.

فرمان بازبینی خصوصیِ بخش انگلیسی، از ریشهٔ مخزن و با مسیر خارج Git اجرا می‌شود؛ خروجی موجود
را نمی‌پوشاند. exit برابر یک، شکست معیار محدود و برابر دو، بررسی ناقص/دستی/اجرا‌نشده است؛
فرمان هیچ حالت «پذیرش کامل» و هیچ امکان انتخاب مدل ندارد.

### معیارهای باقی‌مانده و بازگشت

آماده‌سازی حجم و هویت/metadata بخش اول در دامنهٔ گفته‌شده موفق‌اند؛ ورود دو فایل و بررسی مجوز
جزئی‌اند. بارگذاری CPU، قالب/tokenizer، مصرف کامل، پاسخ و استدلال Flash، معنا، زمینه/صف/منابع/
تأخیر، مسیر برنامه/شاهد/ممیزی، WAN/شروع دوباره/reboot/شروع سرد و بازگشت مدل انتخاب‌شده اجرا
نشده‌اند. پرسش و شکست قبلی، مهلت، حریم خصوصی و صحت شاهد تغییر نکنند. فایل، قالب، متن پایش و
کد تولیدشده مجوز نمی‌دهند؛ اطلاعات ورود مقصد، ابر یا دانلود زمان اجرا وارد آزمون نشوند.

بازگشت خدمت زنده لازم نیست، زیرا انتخاب و تنظیم آن تغییر نکرده است. برای کنارگذاری حجم جدید،
همهٔ استفاده‌کننده‌ها/دریافت‌ها و هویت mount بررسی، فقط ورودی افزودهٔ boot در تغییر بازبینی‌شده
حذف و حجم جدا شود؛ داده‌ها و نسخهٔ خصوصی حفظ شوند. قالب‌بندی دوباره، حذف VMDK/snapshot یا
جایگزینی کاملِ fstab با نسخهٔ قدیمی مجاز نیست. انتخاب آینده به artifact/تنظیم دقیق، بازگشت زمان‌دار
و آزمون تازهٔ ورود، پاسخ، شاهد و ممیزی نیاز دارد. راهنمای دو زبان، وضعیت/کار بعدی و manifest فقط
بر پایهٔ نتیجهٔ واقعی به‌روز شوند.

</div>
