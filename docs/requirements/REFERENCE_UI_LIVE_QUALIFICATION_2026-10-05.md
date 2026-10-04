# Reference UI live qualification / پذیرش زندهٔ رابط مرجع

## English

Observed 2026-10-05 (Tehran), following the owner's explicit deployment request. This is bounded
application acceptance, not production certification or a model/thinking upgrade. Real credentials,
endpoints, account identifiers, screenshots and raw evidence remain in the protected change record.

### Installed identity and unchanged boundaries

Application: `nextops-0.1.0-836b1ea`, source `836b1eaa77e09505e2f97bdb4470d9bc101fadf1`,
[PR 56](https://github.com/Omid-NextAI/nextops/pull/56).
Wheel SHA-256: `fdee1a9c88dec5d3a545db0c4d824df3e509f9d96dc9599293cb80e1e89f611f`.
Source archive SHA-256: `8185be112a1f5c4d0e1913e7c5e2c67c132dc3d4d230d17ef10a3ad3a21d7286`.
Installed code digest: `cc00fb6aa00c0fe0c1c5465142881aaab3fe42276350368daae8b52526a3b7cc`;
authenticated response headers matched this digest.

Connector `2a7c8dc`, inference API `7ce9d29`, llama.cpp `b29c606e`, Qwen3.5-35B-A3B Q4_K_M,
thinking disabled, database schema, credentials, units, network policy and resource limits are
unchanged. The immutable prior app `2a7c8dc` remains available. Only the app process was restarted.
No VM, datastore allocation, OS package upgrade, new permission or account mutation was performed.

The new app occupied less than 200 MB within its existing filesystem. Offline installation used
the existing 40 Linux wheels, unchanged hash-locked requirements, `--offline --no-index` and
`--require-hashes` inside `unshare --net`. All 41 installed distributions passed dependency checks.
All nine frontend assets matched the built wheel; no test fixture/preview module was packaged.

### Failures retained and repaired

1. Initial `e59c42c` CI browser acceptance failed because the sidebar footer covered saved-chat
   deletion. `9740868` prevents flex-content shrinking and adds EN/FA short-viewport regressions.
2. The first live `9740868` trial failed Users Back: the open profile menu intercepted the button.
   The app was rolled back to `2a7c8dc`; fresh login/catalogue/CPU generation passed. `836b1ea`
   closes the popup when entering Users and adds four EN/FA desktop navigation regressions.
3. Final qualification initially stopped on test-harness assumptions: duplicate saved-chat titles
   and a wrong response nesting path. Both failed reports are preserved. The corrected harness
   selects the newest title and verifies its exact backend conversation ID; no product bypass,
   forced click or production-data deletion was used.

### Actual acceptance

Exact packaged-source [CI run 37237831784](https://github.com/Omid-NextAI/nextops/actions/runs/37237831784)
passed all five jobs: quality/unit/API, PostgreSQL 16, PostgreSQL 17, browser and secret scan.
Local `.venv/Scripts/python.exe -m pytest -m browser -q` passed **47 tests in 144.66s**. These browser
tests use isolated fixtures; they are separate from the real checks below. Earlier complete-suite
results and sanitized design screenshots remain in the paired [UI handoff](../en/REFERENCE_UI.md).

The protected `browser-live.py --phase first`, `--phase rollback` and corrected `--phase final`
passed. Each used a fresh Edge browser context, verified TLS, blocked service workers, and allowed
only the application origin. Public network requests and page errors were both zero. This proves
browser-local asset behavior, **not server-side WAN isolation or offline VM cold start**.

Real checks passed: login/logout and sensitive-view clearing; primary summary; two sources/seven
approved targets; unapproved-source denial; read-only Users list/Back; a new saved general answer
and reload/resume; secondary Zabbix 7.0.29 EN/FA CPU generations; LTR/RTL; selected evidence and
Context tab; theme and 390-pixel reflow. No company account was created, disabled or reset.

| Final fresh request | End-to-end seconds | Scope |
|---|---:|---|
| Saved DNS question | 3.700 | General model knowledge, not live infrastructure |
| Secondary Zabbix, English | 39.880 | Selected-source, partial evidence |
| Secondary Zabbix, Persian | 51.140 | Selected-source, partial evidence |

Both final investigation hashes matched durable runs and audit records (2/2). The first trial's
two hashes also matched. Answers acknowledge an active agent problem and incomplete metrics;
they do not establish complete monitoring-engine health. This narrow review is not held-out
NOC/SOC/coding quality acceptance. Model tokens were nonzero and CPU-only flags remained true.

### Rollback and limits

Root-protected scripts under `/var/lib/nextops/ui-qualification/836b1ea/` validated exact old/new
artifacts and unchanged units. Cutovers used a 35-minute automatic rollback guard and atomic
release links. The new release was rolled back to `2a7c8dc`, verified with a fresh login and CPU
answer, then reapplied and tested again. Final artifact/code identity, app readiness, unchanged
unit configuration and zero failed units passed. The final rollback timer was explicitly stopped;
no unattended timer remains for this change. Databases and saved-history records were preserved.

Current-release server-WAN isolation, VM reboot/cold start, sustained load, account mutations,
complete semantic qualification and independent recovery are not newly passed. The
[2026-10-04 MCP report](MCP_LIVE_QUALIFICATION_2026-10-04.md) retains its own historical offline
outcomes. The [release manifest](../status/current-release.yaml) is revision-specific. Qwen 3.8
is reviewed in the paired [CPU guide](../en/CPU_AI.md), but no weights were imported or selected.

## فارسی

این رکورد در ۵ اکتبر ۲۰۲۶ به وقت تهران، پس از درخواست صریح مالک برای استقرار ثبت شد. نتیجه،
پذیرش محدودِ رابط برنامه است؛ نه تأیید آمادگی تولید و نه ارتقای مدل یا فعال‌سازی استدلال.
اعتبارنامه، نشانی، شناسهٔ حساب، تصویر و شاهد خام در رکورد محافظت‌شدهٔ تغییر باقی می‌مانند.

برنامهٔ `nextops-0.1.0-836b1ea` از commit کاملِ ثبت‌شدهٔ بالا مستقر است. هش wheel، بایگانی
منبع و کد نصب‌شده در بخش انگلیسی بدون تغییرِ شناسه درج شده‌اند؛ سربرگ پاسخ احرازشده با هش
کد تطبیق داشت. اتصال‌دهندهٔ `2a7c8dc`، API استنتاجِ `7ce9d29`، runtime ثابت، مدل Qwen3.5،
گزینهٔ استدلال غیرفعال، طرح پایگاه، اعتبارنامه، واحدها، سیاست شبکه و سقف منابع ثابت ماندند.
فقط فرایند برنامه دوباره راه‌اندازی شد؛ ماشین، تخصیص datastore، بستهٔ سیستم‌عامل، مجوز یا
حساب شرکت تغییر نکرد. انتشار قبلیِ برنامه برای بازگشت دقیق محفوظ است.

انتشار تازه کمتر از ۲۰۰ MB در فایل‌سیستم موجود مصرف کرد. نصب در فضای نام شبکهٔ جدا، با
۴۰ wheel موجودِ Linux، نیازمندی قفل‌شدهٔ بدون تغییر و گزینه‌های نصب آفلاین/کنترل هش انجام شد.
سازگاری ۴۱ توزیع نصب‌شده موفق بود. هر نه دارایی رابط با بسته تطبیق داشت؛ دادهٔ ساختگی یا
ماژول پیش‌نمایشِ آزمون در بستهٔ عملیاتی نیست.

شکست‌های اولیه حفظ شدند: CI نسخهٔ `e59c42c` پوشیده‌شدن حذف گفتگو زیر بخش پایینی نوار کناری
را یافت؛ `9740868` آن را اصلاح کرد. آزمون زندهٔ این نسخه، پوشیده‌شدن دکمهٔ بازگشت کاربران
زیر منوی حساب را نشان داد؛ بازگشت به `2a7c8dc` و ورود/پاسخ تازه موفق بود. `836b1ea` هنگام
ورود به پنل کاربران، منو را می‌بندد و آزمون دوزبانهٔ دو عرض دسکتاپ دارد. دو توقف بعدی مربوط
به فرض اشتباهِ ابزار آزمون دربارهٔ عنوان تکراریِ گفتگو و تو‌در‌تویی پاسخ بودند؛ گزارششان
حفظ شد. ابزار اصلاح‌شده، شناسهٔ دقیق گفتگوی تازه را کنترل می‌کند، نه کلیک اجباری یا حذف داده.

پنج کنترل CI همان کدِ بسته‌بندی‌شده، شامل PostgreSQL 16/17، موفق‌اند. اجرای محلیِ ۴۷ آزمون
مرورگر در ۱۴۴٫۶۶ ثانیه موفق بود؛ داده‌های این مجموعه ساختگی‌اند و با آزمون زنده یکی نیستند.
سه گامِ آزمون اولیه، بازگشت و آزمون نهایی در مرورگر تازه با TLS معتبر موفق شدند. فقط مبدأ
برنامه مجاز بود؛ درخواست عمومی و خطای صفحه صفر بود. این محدودیت مرورگر، قطع WAN سرورها
یا شروع سرد آفلاین ماشین‌ها را اثبات نمی‌کند.

ورود/خروج و پاک‌شدن نمای حساس، خلاصهٔ منبع اول، دو منبع/هفت مقصد مجاز، رد منبع غیرمجاز،
فهرست فقط‌خواندنی کاربران و بازگشت، پاسخ تازهٔ عمومی و ادامهٔ گفتگوی ذخیره‌شده، پاسخ CPU
فارسی/انگلیسی از زبیکس دوم 7.0.29، جهت متن، انتخاب شاهد/زبانهٔ زمینه، تم و نمای ۳۹۰ پیکسلی
موفق بودند. هیچ حساب شرکتی ایجاد، غیرفعال یا بازنشانی نشد. تأخیر نهاییِ DNS برابر ۳٫۷۰۰،
زبیکس انگلیسی ۳۹٫۸۸۰ و فارسی ۵۱٫۱۴۰ ثانیه بود؛ DNS دانش عمومی مدل است، نه شاهد زنده.

هش هر دو بررسی نهایی با رکورد ماندگار و ممیزی تطبیق داشت؛ دو مورد آزمون اولیه نیز تطبیق
داشتند. پاسخ‌ها، مشکل فعالِ عامل و ناقص‌بودن سنجه‌ها را بیان می‌کنند، نه سلامت کامل موتور
پایش. این بررسی محدود، پذیرش کیفیت عمومی NOC/SOC یا کدنویسی نیست.

گذار با پیوند اتمی و بازگشت خودکارِ ۳۵ دقیقه‌ای محافظت شد. بازگشت واقعی از نسخهٔ تازه به
`2a7c8dc`، ورود و تولید پاسخ تازه، سپس استقرار دوباره و آزمون نهایی موفق بودند. هویت بسته/کد،
آمادگی برنامه، ثابت‌بودن واحد و نبود خدمت ناموفق کنترل شد. تایمر نهایی صریحاً متوقف است؛
تایمر بدون نظارت از این تغییر باقی نمانده است. پایگاه و سابقهٔ گفتگو محفوظ‌اند.

قطع WAN سرورها برای انتشار جاری، reboot/شروع سرد، بار پایدار، تغییر حساب، کیفیت معنایی
کامل و بازیابی مستقل در این گام موفق اعلام نمی‌شوند. گزارش MCP روز قبل، شاهد تاریخی خود
را حفظ می‌کند و manifest وضعیتِ همین نسخه را نشان می‌دهد. Qwen 3.8 در
[راهنمای CPU](../fa/CPU_AI.md) بررسی شده، اما وزن تازه دریافت یا انتخاب نشده است.
