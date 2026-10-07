# Audit repair live qualification / پذیرش زندهٔ اصلاح ممیزی

Date: 2026-10-07. Status: exact code retained live; final all-four verification passed at17:12:47 UTC.

## English

### Authority, scope and artifacts

The owner requested repairs followed by live shipping. The bounded
[repair specification](AUDIT_REPAIR_2026-10-07.md) governs this code-only window. Exact source
`52e51792e4d06845544bc7ae1be6042890b2ad22` supplies the app, AI API, canonical MCP gateway/source
runner and existing standalone Linux collector. No schema, dependency, credential, account,
permission, native runtime, model, resource or infrastructure configuration change is included.
OCS JPEGs, colors and static logo login are unchanged. This is controlled user testing, not full
production acceptance or certification of model answers.

| Artifact | SHA-256 |
|---|---|
| Exact-source wheel | `9c90ddfebf1d547075332b3f5e64c041134c595315ec5ac3c187ca42ce69f808` |
| Installed package code | `1b4864df13864f2acffb117d35f2d2bdc745d147ee7ab8762285c368b3f1f8ab` |
| Standalone collector | `1e9890b93d9867195eba226ba00b99fbedf182c43ae2b50e58bdd93b9f05ec0d` |

Every wheel package member matches the committed source bytes; no development fixtures, test
modules or executable package hooks were introduced. Fresh offline preparation on all four guests
used existing hash-locked dependencies in a separate network namespace. Immutable original releases,
collector backups and failed-candidate records remain protected and recoverable.

### Source acceptance and preserved failure

Exact-source CI run `37650022276` passed all five jobs: **1,509 unit/API tests, 119 browser tests,
60 PostgreSQL16 tests and 60 PostgreSQL17 tests**, plus lint, formatting, types, documentation,
build, dependency audit and full-history secret scan. Merge commit
`7a419ee6c553b2dab931f12280461ff274f5ee0e` and source have the same tree
`20b3f2bd7ab5f8cb98dd2df9bfea4aa90e9b7fc7`. Passing fixture tests are not live proof.

Post-retention Windows handoff checks passed:1,500 unit/API tests, two POSIX-only skips,
179 deselected and one existing AnyIO deprecation warning in153.08s;14 release-status tests
separately passed in3.34s. Ruff checked158 formatted files; mypy checked157 source files.
Documentation checked146 Markdown files/39 EN/FA guide pairs. Release/inference/installers/
deployment validators and staged Gitleaks passed. Recovery-profile syntax is valid but its
qualification is BLOCKED with four existing blockers; validation is not restore acceptance.
The handoff changes documentation/status tests, not the selected package bytes.

The earlier `3cdd3c0` candidate failed a real primary Persian request with403
`connector.source_scope_changed`. All four roles were restored exactly, including a fresh primary
read on the old code. The new default route binds the configured trusted `primary/zabbix` catalog
entry through the existing strict named-source workflow; mismatched provenance remains denied.
Five API and seven PostgreSQL regressions cover the repaired real boundary. The earlier test-only
login-header assertion and all failed reports are retained, not renamed or relabelled as passes.

### Actual v3 checks

Fresh read-only preflight confirmed the original app `48e3a8a`, AI API `ec1ed32`, MCP/source runner
`2a7c8dc` and original collector. Independent development agents reviewed the source slices and
protected publication tools; this is agent review, not an invented human sign-off.

Initial guarded promotion, actual first browser, exact all-role rollback, fresh original primary
read, reapply and final browser passed. App admission was stopped before reconciling two real zero
processing/deferred native samples at least1.1s apart. AI rollback immediately followed; connector,
Zabbix collector and app followed in order. No native model restart occurred. The original releases
and collector remain the manual rollback targets even after retention.

The actual TLS-validated Edge checks use fresh contexts, no fixtures and no third-party requests.
They cover POST login without URL credentials; EN/FA light/dark/mobile static login and logo-byte
identity; current model metadata and denied thinking; source catalog and denied unapproved source;
saved initial/follow-up, reload and final same-owner resume; model/settings/New chat/theme state;
evidence filters/cursor, tabs, locale labels, keyboard/focus, copy and mobile sheet; logout, sensitive
view purge and revoked session/catalog/conversation replay rejection. Five workspace sizes had no
page-wide overflow. Actual Persian desktop/mobile evidence screenshots were opened and inspected.

| Fresh completion | Language | Total request time |
|---|---|---|
| Saved initial identifier | English |21.438s |
| Saved follow-up identifier | English |20.937s |
| Primary scoped count | Persian |118.281s |
| Secondary scoped count | English |80.766s |
| Final secondary scoped count | Persian |129.297s |

Primary evidence returned zero active problems/eight metrics; secondary returned one active
problem/eight metrics, with received severity3 correctly labelled Average. These are bounded
returned-row counts, not total infrastructure counts, reachability or monitoring-engine health.
Coverage, source, collection time and authorized scope remain visible. The selected count path is
deterministic application projection over real evidence, not proof of unrestricted model reasoning.

Separate bounded read-only PostgreSQL transactions matched both saved completions, three live
investigation results, canonical evidence hashes, completion/source audits and owner-scoped saved
read audits to canonical parsed browser-response JSON; receipts also bind the exact report-file
bytes. No DB writes, grant changes or schema migration
were used by the verifier. The final proof binds the first/rollback/final reports, both audit
receipts and twenty ordered, distinct command logs. Failed/empty/stale/substituted evidence cannot
authorize retention. Private reports, screenshots, identifiers and trusted target details stay out
of Git. A fail-closed consumer passed against the exact reports, audit receipts and command
ledger before root-sealed retention authority. Interrupted-marker fault review required an
append-only v4 recovery helper: ten isolated test groups passed independently. All four new
guards were armed and verified before the older standby guards were retired; the canonical
guards remained armed throughout that transition. Atomic authorization, all-four retain and
postverify, atomic common completion sealing, standby disarm and final read-only reconciliation
passed. The completion proof SHA-256 is
`a818dbd21b6bbecc2c832828159e1b79f1ac18323b91f2c15dd70b3862a696fc`.
At17:12:44–47 UTC all roles matched that proof and all window guard timers/services were idle
with no pending jobs. Exact source/collector, service health and unchanged native/configuration
were separately reverified after disarm. A valid completion proof supersedes automatic rollback;
future recovery requires a fresh authorized window, not reuse of an expired timer.

### Disposition and remaining work

Twelve source findings are repaired: UI-01–UI-05, AI-01–AI-03, SEC-01–SEC-03 and DOC-01.
GOV-01 remains open because the available GitHub integration has no repository-administration
permission. PR60 contains inherited unfinished work and is not blindly merged into main. Code
selection is bound to the exact qualified commit, not the later documentation handoff commit.

Transport drain, hostile credential-text redaction, late authorization/audit and cancellation
failure branches have deterministic source/CI coverage. No intentional live credential injection,
account mutation, dependency outage, overload or new operational permission was exercised.
Privileged out-of-band target edits require operational quiescence; the app has no target UPDATE
grant. Redaction is defense in depth, not a promise that arbitrary secret formats are detectable.

The same Qwen3.8-27B Q8 CPU runtime,32 workers/one native slot,16K configured context, six saved
turns, thinking off, one active/two queued and existing5/300/330/360s deadlines remain. Raw model
quality remains failed at13/16 with the recorded owner exception. Thinking/privacy, full-context quality,
same-release server-WAN, VM reboot/cold start and broader load remain unqualified. Origin blocking
in a browser is not server-WAN disconnection. Recovery is owner-deferred, not passed. Repetition
in the deterministic answer/qualifier presentation remains a polish opportunity; no new UI rebuild
is hidden in this release. Existing historical acceptance records are preserved.

### Reproducible checks and protected operation sequence

```powershell
.venv/Scripts/python.exe -B -X utf8 -m pytest -m 'not integration and not browser' -q --tb=short
.venv/Scripts/python.exe -B -X utf8 -m ruff check packages tests scripts deploy/installers
.venv/Scripts/python.exe -B -X utf8 -m ruff format --check packages tests scripts deploy/installers
.venv/Scripts/python.exe -B -X utf8 -m mypy --platform linux packages tests scripts deploy/installers
.venv/Scripts/python.exe -B -X utf8 scripts/check_docs.py
.venv/Scripts/python.exe -B -X utf8 scripts/check_release_status.py
.venv/Scripts/python.exe -B -X utf8 scripts/check_inference_artifacts.py
.venv/Scripts/python.exe -B -X utf8 scripts/check_deployment_dossiers.py
git diff --check
```

CI uses the existing workflow and locked browser/PG16/PG17 setup. The protected v3 sequence was
`desktop.py prepare`, `step-v3.py initial quiesce/promote`, `browser-live.py first -001`,
`audit-run-v3.py browser-first-001.json`, `step-v3.py rollback candidate-stop/native-idle/rollback`,
`browser-live.py rollback -001`, `step-v3.py reapply quiesce/promote`,
`browser-live.py final -001 --first-report <protected-first-report>`,
`audit-run-v3.py browser-final-001.json`, `step-v3.py final verify`, `build-ledger-v3.py` and
`retention-evidence-v3.py` with explicit report/receipt/ledger basenames and pinned producer hash.
Finalization used `partial-run-v4.py seal/arm/verify-armed/retire-v3` on all four roles,
`seal-qualified-retention-v3.py`, `step-v3.py final retain` in AI/connector/Zabbix/app order,
all-four v4 `postverify`, `complete-retention-v3.py`, all-four v4 `disarm`, all-four final
`verify`, and `final-guards-readonly-v4.py`. The frozen lifecycle/config and sealed v3 helper
were not overwritten. Publication files use exclusive staging, fsync and atomic markers;
timeouts are unknown outcomes requiring exact-file reconciliation, not blind retries.
These are window-specific reviewed private helpers, not reusable provisioning authorization.

## فارسی

### مجوز، دامنه و فایل‌ها

مالک رفع ممیزی و سپس انتشار زنده را خواسته است. مشخصات محدود بالا، پنجرهٔ فقط کد را تعیین
می‌کند. commit کامل `52e5179` بالا برای برنامه، API مدل، MCP اصلی/runner منبع و collector
موجود است. schema، وابستگی، اطلاعات ورود، حساب/مجوز، runtime بومی، مدل، منابع و تنظیم زیرساخت
تغییر نمی‌کنند؛ JPEGهای OCS، رنگ و ورود ثابت با نشان حفظ‌اند. این انتشار آزمون کنترل‌شدهٔ کاربر
است، نه پذیرش کامل production یا گواهی درست‌بودن همهٔ پاسخ‌ها. هش‌های دقیق در جدول آمده‌اند.
همهٔ عضوهای wheel با بایت commit تطبیق، fixture و test بسته‌بندی نشده و نصب تازهٔ آفلاین هر
چهار مهمان با وابستگی قفل‌شده و فضای شبکهٔ جدا انجام شد. اصل نسخه‌ها و collector محفوظ‌اند.

### پذیرش کد و شکست حفظ‌شده

هر پنج کار CI دقیق بالا موفق‌اند: **۱٬۵۰۹ واحد/API،۱۱۹ مرورگر،۶۰ PostgreSQL16 و۶۰ PostgreSQL17**،
lint/قالب/types/اسناد/build/ممیزی وابستگی و اسکن کل تاریخ. tree کد و merge دقیقاً برابر است؛
fixture جای آزمون زنده نیست. نامزد `3cdd3c0` با درخواست واقعی فارسیِ اصلی403 داد؛ هر چهار نقش
دقیق بازگردانده و خواندن تازهٔ اصلی روی اصل موفق شد. مسیر پیش‌فرض با ورودی معتبر catalog و
گردش‌کار سخت‌گیرانهٔ منبع مشخص اصلاح شده؛ provenance ناهمخوان همچنان رد می‌شود. پنج regression
API و هفت پایگاه مرز واقعی را پوشش می‌دهند. خطای assertion ابزار دربارهٔ header ورود و همهٔ
گزارش‌های ناموفق حفظ‌اند و موفق نامیده نمی‌شوند.

بررسی تحویل پس از تثبیت روی Windows موفق است:۱۵۰۰ آزمون واحد/API،دو skip مختص POSIX،۱۷۹
انتخاب‌نشده و هشدار موجود AnyIO در۱۵۳٫۰۸ ثانیه؛۱۴ آزمون وضعیت جدا در۳٫۳۴ ثانیه. Ruff تعداد۱۵۸
فایل قالب‌شده و mypy تعداد۱۵۷ فایل را بررسی کردند.۱۴۶ Markdown و۳۹ جفت راهنما، validator
انتشار/مدل/installer/deployment و Gitleaks فایل stage موفق‌اند. ساختار نمایهٔ بازیابی معتبر
ولی پذیرش آن با چهار مانع قبلی BLOCKED است؛ اعتبار ساختار، پذیرش restore نیست. تحویل فقط
اسناد/آزمون وضعیت را تغییر می‌دهد، نه بایت بستهٔ خدمت.

### آزمون واقعی v3

preflight تازهٔ فقط‌خواندنی، برنامهٔ `48e3a8a`، API مدل `ec1ed32`، MCP/runner با `2a7c8dc`
و collector اصل را تأیید کرد. عامل‌های توسعهٔ مستقل کد و ابزار خصوصی را بازبینی کردند؛ این
review عامل است، نه تأیید انسانیِ ساخته‌شده. انتشار محافظت‌شده، مرورگر اول، بازگشت دقیق همهٔ
نقش‌ها، خواندن تازهٔ اصل، اعمال دوباره و مرورگر نهایی موفق‌اند. پذیرش برنامه پیش از دو نمونهٔ
واقعی صفرِ processing/deferred با فاصلهٔ دست‌کم۱٫۱ ثانیه متوقف و بلافاصله API مدل بازگردانده
شد؛ سپس اتصال، collector پایش و برنامه به‌ترتیب بازگشتند. مدل بومی شروع مجدد نشد. اصل‌ها حتی
پس از تثبیت، مقصد بازگشت دستی‌اند.

Edge تازه با TLS معتبر، بدون fixture و درخواست ثالث بررسی شد: ورود POST بی‌رمز در URL؛ نشان
و ورود ثابت EN/FA روشن/تیره/موبایل؛ مدل واقعی و منع thinking؛ catalog و رد منبع غیرمجاز؛ ذخیره،
دو نوبت و reload/بازگشایی همان مالک؛ تنظیم/New chat/تم؛ فیلتر/cursor/زبانه/زبان/صفحه‌کلید/تمرکز/
کپی/پنجرهٔ موبایلِ شاهد؛ خروج، پاک‌شدن نمای حساس و رد نشست/catalog/سابقهٔ قدیمی. پنج اندازه بدون
سرریز کلی‌اند؛ تصاویر واقعی فارسی دسکتاپ/موبایل باز و مشاهده شدند. زمان پنج پاسخ واقعی در جدول
انگلیسی به‌ترتیب۲۱٫۴۳۸،۲۰٫۹۳۷،۱۱۸٫۲۸۱،۸۰٫۷۶۶ و۱۲۹٫۲۹۷ ثانیه است.

شاهد اصلی صفر مشکل فعال/هشت سنجه و دوم یک مشکل/هشت سنجه داد؛ شدت دریافتی۳ درست با «متوسط»
نمایش داده شد. این شمارش سطر مجازِ دریافتی است، نه کل زیرساخت، reachability یا سلامت موتور.
منبع/زمان/دامنه و محدودیت پوشش آشکارند. پاسخ شمارش، projection قطعی برنامه بر شاهد واقعی است،
نه پذیرش استدلال آزاد مدل. transaction جدا و محدودِ فقط‌خواندنی PostgreSQL، دو پاسخ سابقه، سه
نتیجهٔ زنده، هش شاهد و ممیزی تکمیل/منبع/خواندن مالک را با JSON تجزیه‌شدهٔ canonical پاسخ تطبیق
داد؛ receipt به بایت دقیق فایل گزارش هم متصل است. write، تغییر grant
و مهاجرت انجام نشد. اثبات نهایی گزارش‌های اول/بازگشت/نهایی، دو receipt ممیزی و۲۰ log مجزای
مرتب را متصل می‌کند؛ شاهد شکست‌خورده/خالی/قدیمی/تعویض‌شده تثبیت را مجاز نمی‌کند. داده و تصویر و
شناسه و جزئیات مقصد خصوصی وارد Git نمی‌شوند. consumer بسته با گزارش/receipt/log دقیق موفق شد.
بازبینی شکستِ نوشتن ناتمام marker به helper افزودهٔ v4 نیاز داشت؛ ده گروه آزمون مستقل موفق‌اند.
محافظ تازهٔ هر چهار نقش پیش از توقف محافظ standby قبلی فعال و کنترل شد؛ محافظ اصلی در این
گذار باقی ماند. مجوز اتمی، تثبیت/کنترل هر چهار نقش، ثبت اتمی اثبات مشترک، توقف standby و
تطبیق نهایی فقط‌خواندنی موفق‌اند. ساعت۱۷:۱۲:۴۴ تا۴۷ UTC هر چهار نقش هش اثبات بالا را داشتند؛
همهٔ timer/serviceهای پنجره غیرفعال و بدون job بودند. کد/collector/سلامت و ثبات مدل/تنظیم پس
از توقف محافظ جدا بررسی شدند. اثبات معتبر، بازگشت خودکار را پایان می‌دهد؛ بازیابی آینده
پنجرهٔ مجاز تازه می‌خواهد، نه استفادهٔ دوباره از timer منقضی. ترتیب تثبیت و ابزارهای افزوده
در بخش انگلیسی ثبت است؛ lifecycle/config و helper مهرشدهٔ قبلی بازنویسی نشدند. staging انحصاری،
fsync و marker اتمی استفاده شدند؛ timeout نتیجهٔ مبهم و نیازمند تطبیق فایل است، نه تکرار کور.

### وضعیت و کار باقی‌مانده

دوازده یافتهٔ کد اصلاح‌اند: UI-01 تاUI-05، AI-01 تاAI-03، SEC-01 تاSEC-03 و DOC-01.
GOV-01 باز است چون integration موجود مجوز مدیریت مخزن ندارد. PR60 کار ناتمامِ قبلی هم دارد
و کورکورانه به main ادغام نمی‌شود. کد خدمت همان commit پذیرفته است، نه commit بعدیِ اسناد.
شاخه‌های failure تخلیه/redaction/مجوز دیرهنگام/audit/لغو آزمون قطعی کد و CI دارند؛ تزریق عمدی
اطلاعات ورود زنده، تغییر حساب، outage، overload و مجوز جدید اجرا نشد. ویرایش privileged هدف
بیرون برنامه توقف پذیرش می‌خواهد؛ برنامه grant UPDATE هدف ندارد. redaction دفاع تکمیلی است،
نه تضمین تشخیص همهٔ قالب‌های محرمانه.

Qwen3.8-27B Q8 روی CPU،۳۲ worker/یک slot،زمینهٔ تنظیم‌شدهٔ16K،شش نوبت،thinking خاموش،یک فعال/
دو منتظر و زمان‌های۵/۳۰۰/۳۳۰/۳۶۰ ثانیه ثابت‌اند. معیار کیفیت خام با۱۳/۱۶ همچنان ناموفق است و
استثنای قبلی مالک باقی است.
thinking/حریم خصوصی، کیفیت کل زمینه، WAN سرور همین نسخه، reboot/cold-start و بار گسترده جدا
پذیرفته نشده‌اند. منع مبدأ مرورگر، قطع WAN سرور نیست. recovery در تعویق مالک است، نه موفق.
تکرار متن پاسخ شمارش/qualifier هنوز فرصت پرداخت رابط است؛ بازسازی تازه پنهان نشده و تاریخچه
پذیرش حذف نمی‌شود. فرمان‌های بازتولید کد و ترتیب دقیق ابزار خصوصی در بخش انگلیسی آمده‌اند؛
ابزارها فقط مخصوص همین پنجرهٔ بازبینی‌شده‌اند، نه مجوز عمومی provisioning.
