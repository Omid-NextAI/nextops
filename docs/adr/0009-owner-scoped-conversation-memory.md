# ADR 0009 — Owner-scoped conversation memory

Status: accepted for source implementation, 2026-09-30, following the owner's persistent-chat and
thinking request. Deployment/model acceptance is separate. No accepted earlier ADR is replaced.

## English

Context: two browser-supplied transient pairs cannot resume chat after reload or local login.
The owner requests persistence and follow-ups without weakening offline or evidence boundaries.

Decision: reuse authoritative local PostgreSQL with additive owner/organization/environment-scoped
tables. Store only final model-only results. Application code owns bounded context, idempotency,
generation leases, current-session rechecks, retention/deletion and atomic text-free audit.
Keep live investigations separate. Gate local thinking and token expansion on matched qualified
profiles; never display/store private reasoning.

Alternatives: browser-only storage lacks durable ownership/audit; remote memory violates the offline
contract; shared model session memory risks cross-user leakage; an agent framework is unnecessary.

Consequences/security: transcripts become sensitive local data. Even admins cannot read another
owner's chat through these APIs. History is untrusted and not live truth, authorization or training.
Budgets, omissions, expiry and deletion are explicit; source tests do not prove factual correctness.

Operations: additive schema migration precedes feature enablement. Preserve independent database
backup policy without claiming the owner's ESXi snapshot is PostgreSQL restore acceptance.
No scheduled secure deletion claim is made for inactive accounts or retained backup copies.

Rollback/migration: restore old source/flags/profile and retain additive tables. Dropping tables
loses transcript data and requires a protected export and separately authorized downgrade.

## فارسی

زمینه: دو جفت موقتِ ارسالی مرورگر برای ادامهٔ گفت‌وگو پس از بازکردن صفحه یا ورود تازه کافی نیست.
مالک حافظهٔ ماندگار و پیگیری را بدون تضعیف مرزهای آفلاین و شاهد خواسته است.

تصمیم: از PostgreSQL محلیِ مرجع و جدول‌های افزایشیِ محدود به مالک، سازمان و محیط استفاده شود.
فقط نتیجهٔ نهاییِ صرفاً عمومی ذخیره شود. زمینهٔ محدود، تکرار ایمن، مهلت تولید، بازبینی نشست،
نگهداری و حذف و ممیزیِ اتمیِ بدون متن در اختیار کد برنامه باشند. بررسی زنده جدا بماند. استدلال
محلی و گسترش توکن فقط با نمایهٔ هماهنگ و پذیرفته‌شده فعال شوند؛ استدلال خصوصی نمایش و ذخیره نشود.

گزینه‌ها: ذخیرهٔ مرورگری مالکیت و ممیزی ماندگار ندارد؛ حافظهٔ ابری با الزام آفلاین ناسازگار است؛
نشست مشترک مدل خطر نشت میان کاربران دارد؛ چارچوب عاملِ تازه نیز لازم نیست.

پیامد امنیتی: متن گفت‌وگو دادهٔ حساس محلی است. حتی مدیر از این APIها به سابقهٔ مالک دیگر دسترسی
ندارد. تاریخچه تأییدنشده است، نه حقیقت زنده، مجوز یا آموزش مدل. سقف، حذف زمینه، انقضا و حذف
صریح‌اند؛ آزمون کد اثبات درستی همهٔ پاسخ‌ها نیست.

عملیات: مهاجرت افزایشی پیش از فعال‌سازی انجام شود. سیاست مستقل پشتیبان پایگاه حفظ شود؛ snapshot
ESXi مالک به معنی پذیرش بازیابی PostgreSQL نیست. حذف امن و زمان‌بندی‌شدهٔ حساب غیرفعال یا
نسخه‌های پشتیبان ادعا نمی‌شود.

بازگشت: کد، گزینه‌ها و نمایهٔ قبلی برگردند و جدول‌های افزوده باقی بمانند. حذف جدول، متن‌ها را
از بین می‌برد و خروجی محافظت‌شده و downgrade با اجازهٔ جداگانه می‌خواهد.
