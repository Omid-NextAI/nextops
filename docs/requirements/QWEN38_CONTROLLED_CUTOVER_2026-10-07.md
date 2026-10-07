# Qwen3.8 controlled cutover / گذار کنترل‌شده به Qwen3.8

## English

### Owner exception and bounded plan — 2026-10-07

The owner explicitly asks to skip the three remaining raw failures and go live. This supersedes
the earlier standard-quality-before-selection hold **only for controlled standard-mode Q8 use**.
The greedy trial still has 13 passed/3 failed: English networking asserts an unverified upstream
condition; Persian stale evidence omits authorized scope; Persian causality lacks an explanatory
hypothesis. Native report SHA256:
`b69e4cf3a9725a344b2eadc92a72bb9ec0090ce971934de5ca051d09ac17926e`.
No failed result becomes passed. Answers require operator verification; this is not a guarantee
of correctness, training, independent business sign-off or production acceptance.

Problem: make the already provisioned Apache-2.0 Qwen3.8-27B Q8 accessible through the existing
authenticated app without rebuilding its UI or weakening security. The pinned conversion's exact
upstream lineage remains unverified; its artifact hash/license identity is retained, not invented.
The ordinary candidate manifest remains unqualified/unselected under normal acceptance rules.
A separate explicit release-status exception records any actual controlled selection.

Requirements: exact retained Q8/no-BLAS build003 hashes, 32 generation/batch workers, one native
slot, one active/two queued application requests, five-second queue wait, 16K **admission ceiling**,
300/330/360-second provider/app/generation-proxy budgets, and public thinking off. The context
ceiling is not a full-window latency/recall acceptance. Base sandbox, loopback egress, local TLS,
credentials, policy, evidence source/time/scope, integrity safeguards and audit remain mandatory.
General model knowledge is still unverified; live evidence cannot inherit model assertions.

Non-goals: new weights, dependencies, VM/storage/ESXi changes, GPU/cloud fallback, new permissions,
private-reasoning retention, higher concurrency, model training or broad production certification.

Tasks/acceptance: fresh private target/artifact/resource/idle preflight; independently review the
exact guarded runbook; install the verified Python wheel from the existing hash-locked offline
bundle without network; validate effective units; arm a timed exact rollback; select only the
affected AI artifacts/profile and matching app/proxy time budgets. Verify fresh real EN/FA final
answers, service authentication and thinking denial, actual context admission, saved-chat resume,
authorized Zabbix evidence/source/time/scope and durable audit. Exercise exact rollback/reapply
before retaining the cutover. Keep simulated/source tests distinct from live/WAN evidence.

Stop/rollback: changed target/hash/mount, unavailable rollback, busy scheduler, swap growth,
insufficient memory, failed startup, private-reasoning exposure, auth/evidence/audit regression or
unresolved timeout. Restore the saved 35B runtime/model/AI source/configuration and original
app/proxy budgets, validate/restart only affected services and confirm fresh readiness/answers.
Do not delete either artifact or historical failures. Report every actual gate and any unrun
server-WAN/reboot/load/privacy/context qualification. Update state, next task, paired CPU guides,
traceability and the canonical release manifest with observed results, never proposed ones.

### Execution result

Not run at this source-plan checkpoint. No new live release is inferred.

## فارسی

### استثنای مالک و برنامهٔ محدود — ۷ اکتبر ۲۰۲۶

مالک صریحاً خواسته است سه شکست باقی‌ماندهٔ پاسخ خام کنار گذاشته شوند و مدل زنده شود. این
دستور، الزام پیشینِ موفقیت کامل کیفیت پیش از انتخاب را **فقط برای استفادهٔ کنترل‌شده و بدون
استدلال از Q8** تغییر می‌دهد. نتیجهٔ آزمون حریصانه همچنان ۱۳ موفق و سه ناموفق است: ادعای
بدون شاهد دربارهٔ بالادست در انگلیسی، حذف دامنهٔ مجاز از شاهد کهنهٔ فارسی و نبود فرضیهٔ
توضیحی در پاسخ علّی فارسی. هش گزارش در بخش انگلیسی آمده است. هیچ شکست، موفق ثبت نمی‌شود.
پاسخ‌ها به بررسی کارشناس نیاز دارند؛ این استثنا تضمین درستی، آموزش مدل، تأیید مستقل سازمان
یا پذیرش کامل بهره‌برداری نیست.

هدف، دسترسی به مدل موجود Qwen3.8-27B Q8 با مجوز Apache-2.0 از برنامهٔ احرازهویت‌شدهٔ فعلی
است، بدون بازسازی رابط یا کاهش امنیت. نسخهٔ دقیق منبعِ تبدیل هنوز تأیید نشده است؛ هش و هویت
مجوز فایل حفظ می‌شوند و سابقهٔ تبدیل ساخته نمی‌شود. رکورد نامزد طبق معیار عادی همچنان
پذیرفته و انتخاب‌شده نیست؛ انتخاب واقعیِ استثنایی در رکورد جداگانهٔ وضعیت انتشار ثبت می‌شود.

الزامات: هش دقیق فایل و ساخت سومِ runtime بدون BLAS، ۳۲ رشتهٔ تولید و پردازش ورودی، یک
جایگاه، یک درخواست فعال و دو درخواست منتظر، انتظار پنج‌ثانیه‌ای صف، **سقف پذیرش ورودی 16K**،
مهلت‌های مدل/برنامه/پراکسی ۳۰۰/۳۳۰/۳۶۰ ثانیه و استدلال عمومی خاموش. سقف زمینه، پذیرش کیفیت
و تأخیرِ کل پنجره نیست. محدودسازی فرایند، خروجی شبکهٔ loopback، TLS محلی، اطلاعات ورود،
سیاست، منبع/زمان/دامنهٔ شاهد، کنترل صحت و ممیزی لازم می‌مانند. دانش عمومی مدل همچنان
تأییدنشده است و ادعای آن جای شاهد زنده را نمی‌گیرد.

دریافت مدل یا وابستگی تازه، تغییر ماشین و ذخیره‌سازی و ESXi، GPU یا ابر، مجوز تازه، نگه‌داری
استدلال خصوصی، هم‌زمانی بیشتر، آموزش مدل و تأیید کلی بهره‌برداری در دامنه نیستند.

گام‌ها و پذیرش: بررسی تازه و خصوصیِ مقصد، فایل، منابع و نبود درخواست جاری؛ بازبینی مستقلِ
روال دقیق؛ نصب wheel تأییدشده از بستهٔ آفلاینِ قفل‌شده با هش، بدون شبکه؛ کنترل واحدهای مؤثر؛
فعال‌کردن بازگشت زمان‌دار؛ انتخاب فایل و نمایهٔ AI و هماهنگ‌کردن مهلت برنامه و پراکسی.
پاسخ نهایی تازهٔ فارسی/انگلیسی، احراز هویت خدمت، منع استدلال، کنترل واقعی ظرفیت زمینه، ادامهٔ
گفت‌وگوی ذخیره‌شده، شاهد مجاز Zabbix با منبع/زمان/دامنه و ممیزی ماندگار بررسی شوند. بازگشت
دقیق و اعمال دوباره پیش از تثبیت انجام شوند. آزمون کد و شبیه‌سازی از شاهد زنده و قطع WAN جداست.

توقف و بازگشت: تغییر مقصد/هش/حجم، نبود مسیر بازگشت، صف فعال، رشد swap، کمبود حافظه، شکست
شروع، افشای استدلال خصوصی، پسرفت احراز هویت/شاهد/ممیزی یا مهلت نامعلوم. فایل و کد و تنظیم
محفوظ 35B و مهلت‌های قبلی برنامه/پراکسی بازگردند؛ فقط خدمت‌های مرتبط کنترل و راه‌اندازی
شوند و آمادگی و پاسخ تازه بررسی شود. فایل یا شکست تاریخی حذف نشود. هر معیار واقعی و آزمون
اجرانشدهٔ WAN، روشن‌شدن ماشین، بار، حریم خصوصی و زمینه صریح گزارش شود. وضعیت، کار بعد،
راهنمای CPU دو زبان، ردیابی و رکورد اصلی انتشار با مشاهده به‌روز شوند، نه با برنامه.

### نتیجهٔ اجرا

در گام برنامهٔ کد اجرا نشده است؛ انتشار زندهٔ تازه از آن نتیجه گرفته نمی‌شود.
