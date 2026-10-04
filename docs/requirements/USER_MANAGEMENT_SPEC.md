# Local user management / مدیریت کاربران محلی

Status: bounded source increment; live acceptance not run. Date: 2026-10-04.

## English

### Problem and requirements

Administrators need local account controls in the existing bilingual OCS panel, without SMTP or
a second identity provider. Keep PostgreSQL identity/session/audit authoritative. Revalidate the
active, unexpired session and current administrator role within every transaction. List only the
caller's organization/environment (50-row pages, 500-account creation ceiling). Create viewer,
operator or engineer accounts with fixed server-owned read-only scope profiles. Allow disabling,
re-enabling and password reset of non-administrator accounts. Require 14–256-character passwords.
Status changes and password resets increment credential version and revoke all target sessions.
Use an expected version to reject stale edits. Administrators, including self, cannot be mutated
through these routes. Existing protected administrator recovery remains authoritative.

### Non-goals and threats

No deletion, administrator creation/promotion, role/scope editing, bulk action, invitation, SMTP,
infrastructure credential access or model tool access. UI visibility is not authorization. Deny
cross-scope, expired/revoked/disabled/non-admin callers and reject extra input fields. Never return
or audit password/hash/token values. Audit every authenticated decision, including malformed JSON,
body, path and query rejections. Authenticate/recheck the role before returning validation errors;
an expired session is 401, a non-admin is 403, a valid admin's invalid schema is 422 and an
unavailable required audit is 503. Only a parsed target UUID/error code reaches this denial audit.
Mutation and success audit
commit together or roll back together. Fail closed on database/audit errors. Serialize bounded
creation checks and revalidate permissions after waiting for locks. Do not retry uncertain mutations
automatically. Only the `is_active` column gains an additive application UPDATE grant; roles,
scopes and audit history retain their existing restrictions.

### Plan, tasks and tests

1. Add closed contracts and a separate service using existing tables; add reversible grant 0004.
2. Wire authenticated API and bilingual, responsive admin screen, preserving logo/palette/themes.
3. Test missing/denied sessions, cross-scope IDs, protected admins, duplicates, quota/pagination,
   concurrent stale edits, revocation, schema-denial audits, secret-free responses/audit and atomic
   audit-failure rollback.
4. Run PostgreSQL 16/17, API, real-browser EN/FA/RTL/LTR/mobile/theme/keyboard/logout tests and CI.
5. Document routes, policy, deployment status and rollback; retain the release manifest's live IDs.

### Acceptance and rollback

Local/browser fixtures do not prove database or live acceptance. Before deployment, require CI on
the exact release, isolated PostgreSQL restoration of grant behavior, immutable release rollback,
then fresh TLS-verified admin/non-admin logins and audited create/disable/re-enable/reset checks on
an explicitly approved disposable account, including offline operation. Do not create company users
or change current credentials merely to test this source feature. Roll back application code first;
retain new identities, audit and credential versions. Revocations must never be undone. Revoke the
additive column grant with migration downgrade only in an approved DB change window. No model,
connector, VM or production-readiness claim changes with this increment.

## فارسی

<div dir="rtl">

### مسئله و نیازمندی‌ها

مدیر باید کاربران محلی را در همان پنل دوزبانهٔ OCS مدیریت کند؛ SMTP یا سامانهٔ هویت دوم لازم
نیست. هویت، نشست و ممیزی همچنان در PostgreSQL مرجع‌اند. در هر تراکنش، اعتبار نشست و نقش
فعلی مدیر دوباره بررسی شود. فهرست به سازمان و محیطِ همان مدیر محدود باشد: صفحه‌های ۵۰‌تایی
و سقف ایجاد ۵۰۰ حساب. نقش‌های بیننده، اپراتور و کارشناس با دسترسی‌های فقط‌خواندنیِ ثابتِ سمت
سرور ایجاد شوند. غیرفعال‌سازی، فعال‌سازی دوباره و تنظیم گذرواژهٔ حساب غیرمدیر مجاز باشد؛
گذرواژه ۱۴ تا ۲۵۶ نویسه داشته باشد. تغییر وضعیت یا گذرواژه، نسخهٔ اعتبارنامه را افزایش دهد
و همهٔ نشست‌های آن کاربر را لغو کند. ویرایشِ نسخهٔ قدیمی رد شود. حساب مدیر، از جمله خودِ
درخواست‌کننده، از این مسیرها قابل تغییر نیست؛ بازیابی محافظت‌شدهٔ موجود حفظ می‌شود.

### خارج از دامنه و تهدیدها

حذف، ایجاد یا ارتقای مدیر، ویرایش نقش و دسترسی، اقدام گروهی، دعوت، SMTP، دسترسی به اطلاعات
ورود زیرساخت و ابزار مدل خارج از دامنه‌اند. دیده‌شدن دکمه مجوز نیست. شناسهٔ خارج از دامنه و
نشست منقضی، لغوشده، غیرفعال یا غیرمدیر رد شوند؛ فیلد اضافی پذیرفته نشود. گذرواژه، hash و
توکن در پاسخ یا ممیزی نیایند. تصمیم دربارهٔ کاربر احرازهویت‌شده، از جمله رد JSON، بدنه،
مسیر یا پارامتر نامعتبر، ممیزی شود. پیش از پاسخ اعتبارسنجی، نشست و نقش دوباره بررسی شوند:
نشست منقضی 401، غیرمدیر 403، ورودی نامعتبرِ مدیر معتبر 422 و نبود ممیزی الزامی 503 است.
در ممیزی این رد فقط UUID معتبرِ مقصد و کد خطا ثبت شوند. تغییر و ممیزی
موفقیت در یک تراکنش ثبت یا هر دو بازگردانده شوند. خطای پایگاه/ممیزی به موفقیت تبدیل نشود.
کنترل سقف ایجاد سریالی و مجوز پس از انتظار قفل دوباره بررسی شود؛ تغییر مبهم خودکار تکرار
نشود. فقط مجوز UPDATE ستون `is_active` به نقش برنامه افزوده می‌شود؛ محدودیت نقش‌ها،
دسترسی‌ها و تاریخچهٔ ممیزی ثابت است.

### برنامه، کارها و آزمون‌ها

۱. قرارداد بسته، سرویس جدا با جدول‌های موجود و migration برگشت‌پذیرِ مجوز 0004 افزوده شود.
۲. API محافظت‌شده و نمای مدیریت دوزبانه و واکنش‌گرا، با حفظ لوگو، رنگ‌ها و تم‌ها متصل شوند.
۳. نبود/رد نشست، دامنهٔ نادرست، مدیر محافظت‌شده، نام تکراری، سقف/صفحه‌بندی، ویرایش هم‌زمان
قدیمی، لغو نشست، ممیزیِ رد ورودی نامعتبر، نبود راز در پاسخ/ممیزی و بازگشت اتمی هنگام خطای
ممیزی آزموده شوند.
۴. PostgreSQL 16/17، API، مرورگر واقعی، فارسی/انگلیسی، RTL/LTR، موبایل، تم، صفحه‌کلید و خروج
در CI بررسی شوند.
۵. مسیرها، سیاست، وضعیت استقرار و بازگشت مستند شوند؛ هویت انتشار زنده در manifest ثابت بماند.

### پذیرش و بازگشت

آزمون محلی/مرورگر با دادهٔ ساختگی، پذیرش پایگاه یا محیط زنده نیست. پیش از استقرار، CI همان
انتشار، بررسی مجوزها در PostgreSQL جدا و بازگشت به انتشار تغییرناپذیر لازم است؛ سپس ورود
تازهٔ مدیر/غیرمدیر با TLS معتبر و ایجاد، غیرفعال‌سازی، فعال‌سازی و تنظیم گذرواژه با ممیزی روی
حساب آزمایشیِ صریحاً مجاز، از جمله در حالت آفلاین، بررسی شود. صرفاً برای آزمون این قابلیت،
کاربر شرکت ایجاد یا اطلاعات ورود فعلی عوض نشود. ابتدا کد برنامه بازگردد؛ هویت‌ها، ممیزی و
نسخهٔ اعتبارنامه حفظ شوند. لغو نشست هرگز معکوس نشود. حذف مجوز ستون با downgrade تنها در
پنجرهٔ تغییر مجاز پایگاه انجام شود. مدل، اتصال‌دهنده، VM و ادعای آمادگی تولید تغییر نمی‌کنند.

</div>
