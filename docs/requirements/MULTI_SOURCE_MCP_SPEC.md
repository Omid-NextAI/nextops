# Source-scoped Zabbix MCP increment / گام MCP چندمنبعی زبیکس

Date: 2026-10-04. Status: MCP-01 source implemented and locally tested; MCP-02/03 not run.
This specification is not deployment authorization. / کد MCP-01 پیاده و محلی آزموده شده؛
MCP-02/03 اجرا نشده‌اند. این سند مجوز استقرار نیست.

## English

### Problem and requirements

The working connector serves one Zabbix source. Adding another must not replace that source,
confuse identical host IDs between servers, expose tokens to the model, or create a generic API
proxy. The owner requested another API-only, read-only source. Its private desktop HTTPS/read
preflight is not connector-process, MCP, application, offline or production acceptance.

MCP-01 implements the additive core and protocol adapter. An immutable private registry binds
organization/environment, source ID, target ID, exact host ID/name, approved numeric group IDs,
HTTPS origin, CA path and credential reference. Missing sources/targets deny; there is no default
or fallback. Only the existing five reviewed reads and unauthenticated version probe are allowed.
Explicit fields, row/byte limits, bounded admission, timeouts and source-qualified typed results
remain mandatory. Host membership is rechecked on collection. Authorization is supplied by a
trusted application port and rechecked for each call, never by tool arguments or annotations.

The official MIT-licensed Python SDK is pinned as an optional extra. It implements actual
initialization, tool discovery, calls and cancellation over local streams/stdio. The server
factory requires an authenticated actor, authorization port and mandatory audit port. No default
audit, anonymous listener, general shell, runtime installer or operational CLI is provided.
Audit intent precedes network/credential use; completion includes the canonical evidence hash.
Audit failure cannot return successful evidence. Tokens exist only in the runner's transport
factory, not SDK requests/results, source manifests, exception text or model context.

### Non-goals, threats and compatibility

No replacement of the current HTTP connector, UI, model, inference profile, database schema or
existing source. No HTTP-token exception, new host SSH, discovery, write tools, automatic group
enrollment or cloud service. Treat source text as untrusted evidence. Test source/target
substitution, duplicate IDs, forged scopes, malformed/oversized data, credential leaks, broken
audit, overload, cancellation/drain and dependency recovery. MCP is not authorization.

### Plan and acceptance

1. MCP-01: private registry/contracts, scoped existing Zabbix client, authorization/audit ports,
   optional official SDK adapter/client, protocol and isolation tests, paired guides and ADR.
2. MCP-02: application-owned durable PostgreSQL authorization/audit composition, protected
   runner credential staging, source selection, protocol-frame/logging limits and process egress;
   preserve the legacy routes.
3. MCP-03: exact offline artifact provisioning, real runner/API and fresh EN/FA browser answers,
   evidence/audit correlation, unavailable-source isolation and guarded rollback.

MCP-01 accepts only locally demonstrated contracts and real SDK protocol exchanges with fixture
downstream data. Local live API preflight remains separately classified. MCP-02/03 are not run
until their complete composition and approved change records exist. Identity/expiry, all approved
group IDs and role restrictions must be reconciled before claiming source-wide access.

Rollback: leave the optional extra and new source path disabled; retain the serving release and
private evidence. No data migration or old-source configuration change is required. Future live
promotion must preserve a compatible prior release/registry/credentials and verify rollback.
Update both MCP guides, state, next task, release manifest, traceability and Markdown inventory.

## فارسی

### مسئله و الزامات

اتصال‌دهندهٔ فعلی یک منبع زبیکس را پشتیبانی می‌کند. افزودن منبع دوم نباید منبع موجود را جایگزین
کند، شناسه‌های مشابهِ میزبان در دو سرور را یکی بداند، توکن را به مدل بدهد یا پراکسی آزاد API
بسازد. درخواست مالک، اتصال فقط‌خواندنی و صرفاً از طریق API است. پیش‌آزمون HTTPS و خواندن در
رایانهٔ توسعه، پذیرش فرایند اتصال‌دهنده، MCP، برنامه، آفلاین یا محیط تولید نیست.

گام MCP-01 هسته و لایهٔ پروتکلِ افزوده را پیاده می‌کند. فهرست خصوصی و تغییرناپذیر، سازمان و محیط،
شناسهٔ منبع و مقصد، شناسه و نام دقیق میزبان، شناسه‌های عددی گروه‌های مجاز، نشانی HTTPS، مسیر CA
و ارجاع اطلاعات ورود را به هم متصل می‌کند. منبع یا مقصد ناشناخته رد می‌شود؛ جایگزین پنهان وجود
ندارد. فقط پنج روش خواندنِ بازبینی‌شده و بررسی نسخه بدون احراز هویت مجازند. فیلدهای صریح، سقف
سطر و بایت، پذیرش محدود، مهلت و نتیجهٔ دارای نوع و منشأ الزامی‌اند. عضویت گروه هنگام گردآوری
دوباره بررسی می‌شود. مجوز از مرز معتبر برنامه می‌آید و در هر درخواست بازبینی می‌شود، نه از
آرگومان ابزار یا برچسب فقط‌خواندنی آن.

SDK رسمی Python با مجوز MIT، به‌صورت وابستگی اختیاری و نسخهٔ ثابت افزوده می‌شود. آغاز ارتباط،
معرفی ابزار، فراخوانی و لغو واقعاً از پروتکل MCP استفاده می‌کنند. ساخت سرور به هویت معتبر و
مرزهای الزامیِ مجوز و ممیزی نیاز دارد؛ ممیزی پیش‌فرض، شنوندهٔ بی‌هویت، shell عمومی، نصب زمان
اجرا یا فرمان عملیاتی ارائه نمی‌شود. قصد خواندن پیش از شبکه و دسترسی به اطلاعات ورود ثبت و
تکمیل همراه هش شواهد ممیزی می‌شود. شکست ممیزی اجازهٔ پاسخ موفق نمی‌دهد. توکن فقط نزد کارخانهٔ
انتقالِ اجراکننده است، نه در درخواست و نتیجهٔ SDK، فهرست منابع، متن خطا یا زمینهٔ مدل.

### حدود، تهدیدها و پذیرش

مسیر HTTP، رابط، مدل، نمایهٔ پردازش، ساختار پایگاه و منبع موجود تغییر نمی‌کنند. انتقال توکن روی
HTTP، SSH سرور جدید، پویش آزاد، ابزار نوشتنی، عضویت خودکار گروه و سرویس ابری خارج از دامنه‌اند.
تعویض منبع و مقصد، شناسهٔ تکراری، دامنهٔ جعلی، دادهٔ خراب یا بزرگ، افشای اطلاعات ورود، شکست
ممیزی، ازدحام، لغو و آزاد شدن واقعی ظرفیت و ادامه پس از خرابی آزموده می‌شوند. MCP مجوز نیست.

گام MCP-01 شامل قرارداد و فهرست منابع، محدودسازی کارخواه زبیکس، مرز مجوز و ممیزی، لایهٔ SDK،
آزمون پروتکل و جداسازی و مستندات است. گام MCP-02، اتصال به مجوز و ممیزی ماندگار PostgreSQL،
آماده‌سازی امن اجراکننده، انتخاب منبع، سقف پیام/گزارش پروتکل و خروجی شبکهٔ فرایند را انجام می‌دهد. گام MCP-03 به نصب
دقیق آفلاین، پاسخ تازهٔ فارسی و انگلیسی در مرورگر، تطبیق شاهد و ممیزی، جداسازی خرابی و بازگشت
محافظت‌شده اختصاص دارد. معیارهای عملیاتیِ اجرا‌نشده، موفق نامیده نمی‌شوند.

پذیرش MCP-01 فقط برای قرارداد محلی و تبادل واقعی SDK با دادهٔ ساختگی مقصد است. پیش‌آزمون زندهٔ
API جدا ثبت می‌شود. پیش از ادعای دسترسی کامل، هویت و انقضای توکن، شناسهٔ همهٔ گروه‌های مجاز و
محدودیت نقش تأیید شوند. بازگشت با غیرفعال نگه داشتن مسیر و وابستگی اختیاری انجام می‌شود؛ انتشار
زنده و شواهد خصوصی حفظ می‌شوند. مهاجرت داده یا تغییر منبع قدیمی لازم نیست. راهنماهای دوزبانه،
وضعیت، گام بعد، رکورد انتشار، ردیابی و فهرست Markdown هم‌زمان به‌روز می‌شوند.
