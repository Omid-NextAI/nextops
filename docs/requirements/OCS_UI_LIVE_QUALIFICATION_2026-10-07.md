# OCS interface live qualification / پذیرش زندهٔ رابط OCS

## English

### Scope and exact artifacts

The owner separately requested live deployment after source-only redesign. This window promotes
only the existing app guest from `ec1ed32` to
`48e3a8a7ec06d25513877085d61a8f7c5ac18e28`. The backend, schema, dependency lock, credentials,
TLS policy and permissions have no source changes. AI API `ec1ed32`, MCP `2a7c8dc`, Qwen3.8-27B
Q8 CPU inference, 16K configured admission, six-turn saved context and disabled thinking remain.
This is a controlled user-testing release, not production or model-quality acceptance.

| Artifact | SHA-256 |
|---|---|
| Exact-source app wheel | `bc11414ec968eddea0048baba774b58ee1446f75fd5feb8a887761a178df5554` |
| Installed application-code identity | `284de2f55e2173a6318495fc800ebdc02e712ae6a1b7a866e91b57f1b7e9d627` |

Every wheel package file was compared byte-for-byte with the committed source. The original
company JPEG hashes match [the source specification](OCS_UI_SIMPLIFICATION_2026-10-07.md).
No preview/test module is packaged. A root-protected sealed bundle installs through the existing
hash-locked Linux wheelhouse with a separate network namespace and no Internet package access.
The old immutable app release is retained; units and application environment are checked unchanged.

### Source and preflight evidence

Source verification: 1,446 unit/API passes, two existing POSIX-specific Windows skips, 101 browser
passes, 152 typed files, lint/format, JavaScript syntax, local documentation/status/artifact checks
and commit-only secret scan. Exact-source CI run `37616454773` passed all five jobs: quality and
dependency audit, PostgreSQL 16 and 17 integration, browser acceptance and full-history secret scan.
The source specification retains exact local commands and fixture screenshot paths. Those tests
are distinct from the real authenticated deployment checks below.

Private fresh app preflight confirmed the expected old identity, active service, no failed units
or pending reboot, verified rollback metadata, 8 guest vCPU, 32,049 MiB usable RAM, zero swap usage,
trusted synchronized time and existing mounts/listeners. The release filesystem had over 20 GiB
available. No datastore allocation, disk change, OS maintenance or infrastructure restart is included.
Offline candidate preparation passed while the old app continued serving.

### Preserved first failure and rollback

The first app promotion passed under an owned 60-minute rollback guard. The browser harness then
failed its Node `APIRequestContext` asset read because that client did not use the installed Windows
CA. Edge HTTPS page navigation succeeded with certificate validation enabled. The old app was
restored, its exact code identity checked, and a fresh authenticated rollback browser passed login,
readiness, secondary-source catalogue, unapproved-source denial, logout and replay rejection.
The failed report remains private. Asset verification now uses the actual trusted browser's
`fetch` and WebCrypto path; certificate checks were not disabled. The unchanged candidate was
reapplied under a fresh guard; that attempt has a separate report.

### Live results and disposition

App-only release `48e3a8a` is retained. A read-only post-retention check at **12:24:45 UTC** found
the exact release selected, app active, automatic restart count zero and the owned rollback timer
inactive. AI API/native/MCP release, PIDs, restart counters, units and environment hashes match
the pre-window record exactly: no AI or connector change/restart. The previous app remains available.

The final fresh, TLS-validated Edge context passed all live browser checks without fixtures,
page errors, failed assets or requests outside the app origin. It verified both unchanged logo
assets; static EN/FA light/dark/mobile login; password visibility and locale; approved secondary
catalogue and unapproved-source denial; model metadata and disabled-thinking denial; saved chat,
reload/resume and exact follow-up; settings/theme sync; busy controls; real secondary monitoring;
evidence filters, selection, tabs, keyboard/focus, copy and mobile drawer; logout, replay denial
and no unauthenticated model-state leak. Five workspace sizes were checked for page overflow.
Actual final evidence desktop/mobile screenshots were opened and inspected. A separate fresh
post-run browser smoke and the restored-source browser also passed.

Final new generations took **22.656s** (saved initial), **22.281s** (follow-up) and **82.094s**
(secondary English count question). The monitoring answer reported one returned active problem,
with partial/truncated-metrics coverage, not overall health or a proven cause. Read-only PostgreSQL
verification matched both owner-scoped conversation audits and the canonical evidence/result/audit
hash pair. These three completions do not qualify broad factual, coding or reasoning quality.

Across the preserved attempts, eleven fresh finals completed, including one Persian secondary
answer; **one repeated Persian request returned HTTP 504 after 301.625s**. The app was restored
three times and reapplied without changing model settings or inflating timeouts. Final bounded
generation and readiness recovered, but intermittent model latency remains unresolved. Earlier
browser reports failed asset trust or copy assertions: the first used the wrong CA path; copy
assertions were subsequently changed to wait for completion, and the completed-copy comparison
was proven to differ only by Windows CRLF. The final test waits for the real copied status and
proves equality after CRLF-to-LF
normalization (11 CRLFs); it does not disable TLS, inject a clipboard fallback or change app code.
Failed reports remain failures; successful subchecks are not relabelled as whole-run passes.

The protected command sequence used the reviewed private helpers: `desktop.py prepare/promote`,
`browser-live.py first -005`, `desktop.py audit first`, `browser-live.py smoke`,
`preserve-services.py after`, `desktop.py verify/authorize-retention/retain`. Only the app service
was selected/restarted. Real screenshots, exact protected commands, target data, credentials and
audit identifiers remain outside Git in the dated private qualification folder; sanitized source
screenshots and reproducible isolated preview commands are in [REFERENCE_UI](../en/REFERENCE_UI.md).
Browser-origin blocking is not server-WAN acceptance. Same-release server-WAN, VM-reboot/cold-start,
broader load, full-context, thinking/privacy and held-out model semantic gates remain separately
unqualified. Historical quality failures and the existing owner exception are not rewritten.

### Post-retention repository checks

In the existing locked environment, the following commands passed. The full unit/API run returned
**1,446 passed, two existing POSIX-only Windows skips, 139 deselected, one existing AnyIO warning**
in28.26s. Ruff reported153 formatted files; Linux-target typing passed152 source files. Documentation
validation covered144 Markdown files/39 EN/FA pairs. No application source changed after `48e3a8a`.
The manifest test now binds this exact app-only revision to the unchanged API and recorded gate,
without allowing arbitrary app/API mismatches or production acceptance.
The complete staged handoff also passed Gitleaks8.30.1 (`git --pre-commit --staged --redact`),
with no new findings. The exact-source CI above remains evidence for deployed `48e3a8a`, not an
unrun CI claim for the later documentation-only handoff commit.

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

## فارسی

### دامنه و فایل دقیق

مالک پس از بازطراحیِ فقط کد، استقرار زنده را جداگانه خواست. این پنجره فقط برنامهٔ مهمان موجود
را از `ec1ed32` به شناسهٔ کامل `48e3a8a` بالا می‌برد. backend، schema، قفل وابستگی، اطلاعات
ورود، سیاست TLS و مجوزها در کد تغییر ندارند. API مدل `ec1ed32`، MCP با `2a7c8dc`،
Qwen3.8-27B Q8 روی CPU، پذیرش تنظیم‌شدهٔ 16K، سابقهٔ شش نوبت و منع thinking ثابت‌اند.
این انتشار برای آزمون کنترل‌شدهٔ کاربر است، نه پذیرش production یا کیفیت مدل.

هش wheel و هویت کد در جدول بالا آمده‌اند؛ همهٔ فایل‌های بسته با commit دقیق، بایت‌به‌بایت
تطبیق شدند. هش JPEGهای اصلی شرکت مطابق مشخصات کد است و ماژول پیش‌نمایش/آزمون بسته‌بندی
نمی‌شود. بستهٔ مهرشده با مالکیت root از wheelhouse قبلی با قفل هش، فضای شبکهٔ جدا و بدون
دریافت اینترنتی نصب می‌شود. انتشار تغییرناپذیر قبلی حفظ و ثبات واحد و محیط برنامه کنترل می‌شود.

### شاهد کد و بررسی پیش از اجرا

۱٬۴۴۶ آزمون واحد/API، ۱۰۱ مرورگر و کنترل نوعِ ۱۵۲ فایل موفق‌اند؛ دو مورد مختص POSIX در Windows
اجرا نمی‌شوند. lint/قالب، نحو JS، اسناد/وضعیت/فایل و اسکن commit موفق‌اند. هر پنج کار CI دقیق
بالا، شامل کیفیت/وابستگی، PostgreSQL 16 و 17، مرورگر و اسکن کل تاریخ موفق‌اند. فرمان‌ها و
مسیر تصاویر ساختگی در مشخصات کد حفظ‌اند؛ این آزمون‌ها از بررسی احرازهویت‌شدهٔ زنده جدا هستند.

بررسی تازهٔ خصوصی برنامه، هویت قبلی، خدمت فعال، نبود واحد ناموفق/نیاز به reboot، هش بازگشت،
۸ vCPU، حافظهٔ قابل استفادهٔ۳۲٬۰۴۹ MiB، swap صفر، زمان هماهنگ و mount/listener موجود را تأیید
کرد. فضای فایل‌سیستم انتشار بیش از۲۰ GiB بود. تخصیص datastore، تغییر دیسک، نگه‌داری OS یا
شروع مجدد زیرساخت در دامنه نیست. آماده‌سازی آفلاین نامزد با ادامهٔ خدمت نسخهٔ قبلی موفق شد.

### شکست اول و بازگشتِ حفظ‌شده

انتخاب اول برنامه با محافظ بازگشت۶۰‌دقیقه‌ای موفق شد؛ سپس خواندن فایل با Node
`APIRequestContext` به‌دلیل استفاده نکردن آن ابزار از CA نصب‌شدهٔ Windows شکست خورد.
ورود صفحه در Edge با اعتبارسنجی گواهی موفق بود. برنامهٔ قبلی بازگردانده و هویت دقیق بررسی شد؛
مرورگر تازه، ورود، آمادگی، فهرست منبع دوم، منع منبع غیرمجاز، خروج و رد استفادهٔ دوبارهٔ نشست
را گذراند. گزارش ناموفق خصوصی حفظ است. بررسی فایل اکنون از `fetch` و WebCrypto همان مرورگر
مورد اعتماد استفاده می‌کند؛ بررسی گواهی خاموش نشد. همان نامزد بدون تغییر با محافظ تازه دوباره
اعمال و گزارش کوشش جدا ثبت می‌شود.

### نتیجهٔ زنده و وضعیت

انتشار فقط برنامهٔ `48e3a8a` تثبیت شد. کنترل فقط‌خواندنی ساعت **۱۲:۲۴:۴۵ UTC**، انتخاب کد
دقیق، خدمت فعال، شمارندهٔ شروع خودکار صفر و محافظ بازگشت غیرفعال را نشان داد. نسخه/PID/
شمارندهٔ شروع/هش واحد و محیطِ API مدل، runtime و MCP دقیقاً با پیش از پنجره برابرند؛ مدل
و اتصال‌دهنده تغییر یا شروع مجدد نداشتند. انتشار قبلی برنامه برای بازگشت حفظ است.

مرورگر نهاییِ تازهٔ Edge با TLS معتبر، همهٔ کنترل‌های زنده را بدون دادهٔ ساختگی، خطای صفحه،
فایل ناموفق یا درخواست خارج مبدأ برنامه گذراند: دو نشان اصلی؛ ورود ثابت فارسی/انگلیسی،
روشن/تیره/موبایل؛ نمایش رمز و زبان؛ فهرست منبع دوم و منع منبع غیرمجاز؛ فرادادهٔ مدل و منع
استدلال؛ ذخیره/بازگشایی/ادامهٔ دقیق گفت‌وگو؛ هماهنگی تنظیم/تم و وضعیت انتظار؛ پایش واقعی؛
فیلتر/انتخاب/زبانه/کپی شاهد، صفحه‌کلید/تمرکز و پنجرهٔ موبایل؛ خروج، رد نشست قبلی و عدم
افشای مدل پیش از ورود. پنج اندازهٔ فضای کار از نظر سرریز بررسی شدند. تصاویر واقعیِ شاهد
دسکتاپ/موبایل باز و مشاهده شدند؛ smoke تازه و مرورگر نسخهٔ بازگردانده‌شده نیز موفق‌اند.

سه پاسخ نهایی **۲۲٫۶۵۶**، **۲۲٫۲۸۱** و **۸۲٫۰۹۴ ثانیه** طول کشیدند. پرسش شمارش انگلیسی
منبع دوم، یک مشکل فعالِ دریافتی را با پوشش ناقصِ سنجه نشان داد، نه سلامت کلی یا علت قطعی.
PostgreSQL فقط‌خواندنی، دو ممیزی مختص مالک و جفت هش شاهد/نتیجه/ممیزی را تطبیق داد. این سه
پاسخ، پذیرش کیفیت عمومیِ حقیقت، کد یا استدلال نیستند.

در کوشش‌های حفظ‌شده، یازده پاسخ تازه، شامل یک پاسخ فارسیِ منبع دوم کامل شدند؛ **یک درخواست
تکراری فارسی پس از۳۰۱٫۶۲۵ ثانیه HTTP 504 داد**. برنامه سه بار بازگردانده و بدون تغییر مدل
یا افزایش مهلت دوباره اعمال شد. آمادگی و تولید محدود بازگشت، ولی کندی متناوب مدل حل نشده
است. ابزار اول از مسیر CA نامناسب خواند؛ انتظار تکمیل به بررسی کپی افزوده شد و ثابت شد
مقایسهٔ بعد از تکمیل فقط با CRLF ویندوز تفاوت داشت. ابزار نهایی منتظر وضعیت واقعی کپی می‌ماند و برابری پس
از تبدیل CRLF به LF را برای۱۱ مورد ثابت می‌کند؛ TLS خاموش، مسیر ساختگی کپی یا کد برنامه
عوض نشد. گزارش‌های شکست محفوظ‌اند و موفقیت جزء، موفقیت کل گزارش نامیده نمی‌شود.

ترتیب فرمان‌های خصوصیِ بازبینی‌شده در بخش انگلیسی آمده است؛ فقط خدمت برنامه انتخاب/شروع
مجدد شد. تصویر واقعی، فرمان محافظت‌شده، دادهٔ مقصد، اطلاعات ورود و شناسهٔ ممیزی خارج Git
و در پوشهٔ خصوصیِ تاریخ‌دار باقی‌اند. فرمان پیش‌نمایش جدا و تصاویر پالایش‌شده در راهنمای
REFERENCE_UI هستند. محدودیت مبدأ مرورگر، پذیرش WAN سرور نیست. معیارهای server-WAN،
reboot/cold-start، بار گسترده، کل زمینه، thinking/حریم خصوصی و معنای پاسخ هنوز جداگانه
پذیرفته نشده‌اند؛ شکست کیفیت و استثنای قبلی مالک بازنویسی نمی‌شوند.

### کنترل مخزن پس از تثبیت

فرمان‌های دقیقِ بخش انگلیسی در محیط موجود موفق‌اند: **۱٬۴۴۶ موفق، دو مورد مختص POSIX در
Windows اجرا‌نشده،۱۳۹ انتخاب‌نشده و یک هشدار موجود AnyIO** در۲۸٫۲۶ ثانیه. Ruff تعداد۱۵۳
فایل قالب‌بندی‌شده، کنترل نوعِ Linux تعداد۱۵۲ فایل و کنترل اسناد۱۴۴ Markdown/۳۹ جفت زبان
را گذراندند. کد برنامه پس از `48e3a8a` عوض نشد. آزمون manifest فقط همین نسخهٔ دقیقِ
برنامه را به API ثابت و معیار ثبت‌شده وصل می‌کند؛ عدم تطبیق دلخواه یا پذیرش تولید مجاز نیست.
تمام تغییرات تحویل نیز با Gitleaks8.30.1 و فرمان بخش انگلیسی، بدون یافتهٔ تازه بررسی شد.
CI کد دقیقِ بالا شاهد `48e3a8a` مستقر است، نه ادعای CI اجرا‌نشدهٔ commit بعدیِ اسناد.
