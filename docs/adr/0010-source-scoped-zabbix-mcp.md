# ADR 0010 — Additive source-scoped Zabbix MCP / MCP افزوده و محدود به منبع

Status: accepted for source implementation, 2026-10-04; not live promotion.

## English

Context: the owner requests a second API-only Zabbix source and real MCP. The current single-source
HTTP connector and its accepted read-only behavior must remain available.

Decision: retain those routes and client contracts. Add an immutable private source/target registry
and a scoped wrapper around the existing Zabbix reader. Add the official Python SDK as an exact
optional dependency on its maintained 1.x line. A local-stream MCP factory requires an
application-authenticated actor, per-call authorization and mandatory audit ports. It publishes
two named reads, not arbitrary JSON-RPC. Source identity and exact target survive in every result
and audit hash. Protocol metadata cannot authorize access. No unauthenticated network listener or
production entrypoint is added before durable application composition is qualified.

Alternatives: overwriting the old URL/token loses a source; a generic MCP API proxy broadens
authority; replacing the whole connector rebuilds accepted work; treating the current HTTP API as
MCP misstates protocol support. All are rejected. The latest SDK major is not adopted automatically;
an exact compatible maintenance-line release is separately tested and audited.

Consequences/security: source/target IDs are namespaced, endpoint/CA/credential references remain
runner-owned, group membership is verified, output/admission are bounded and audit failure blocks
success. A runtime adapter still needs the real application's authorization/audit implementation,
protected launch and process isolation. An in-memory port test is not durable audit acceptance.

Operations/rollback: optional offline-provisioned dependency only; no runtime resolution or new
schema. Existing deployments omit it and keep the current paths. Live source staging, egress,
fresh bilingual answers, offline restart and exact rollback need MCP-02/03 qualification.

## فارسی

زمینه: مالک اتصال دوم زبیکس را فقط از طریق API و با MCP واقعی می‌خواهد. مسیر HTTP موجود و
رفتار فقط‌خواندنیِ پذیرفته‌شده باید حفظ شوند.

تصمیم: مسیرها و قراردادهای فعلی حفظ و فهرست خصوصی و تغییرناپذیر منابع و مقصدها افزوده می‌شود.
گردآورندهٔ موجود زبیکس پشت لایهٔ محدود به منبع قرار می‌گیرد. SDK رسمی Python از شاخهٔ نگه‌داری‌شدهٔ
1.x با نسخهٔ دقیق و به‌صورت اختیاری افزوده می‌شود. ساخت سرورِ محلی به هویت معتبر برنامه و
مرزهای مجوزِ هر فراخوانی و ممیزیِ الزامی نیاز دارد. دو خواندن نام‌دار ارائه می‌شود، نه JSON-RPC
دلخواه. منشأ و مقصد دقیق در نتیجه و هش ممیزی می‌مانند. فرادادهٔ پروتکل مجوز نیست. پیش از پذیرش
اتصال ماندگار برنامه، شنوندهٔ شبکهٔ بی‌هویت یا نقطهٔ شروع عملیاتی افزوده نمی‌شود.

گزینه‌های ردشده: جایگزینی URL و توکن، منبع موجود را حذف می‌کند؛ پراکسی عمومی MCP اختیار را
گسترش می‌دهد؛ بازسازی اتصال‌دهنده کار پذیرفته‌شده را تکرار می‌کند؛ نامیدن API HTTP به‌عنوان MCP
ادعای نادرست است. نسخهٔ اصلیِ تازهٔ SDK نیز خودکار پذیرفته نمی‌شود.

پیامد امنیتی و عملیاتی: شناسه‌ها به منبع محدودند؛ نشانی، CA و ارجاع اطلاعات ورود نزد اجراکننده
می‌مانند؛ عضویت گروه بررسی، خروجی و پذیرش محدود و موفقیت در شکست ممیزی مسدود می‌شود. سازگارساز
عملیاتی هنوز به مجوز و ممیزی واقعیِ برنامه، اجرای محافظت‌شده و جداسازی فرایند نیاز دارد. آزمون
درون‌حافظه‌ای، پذیرش ممیزی ماندگار نیست. وابستگی از پیش برای آفلاین آماده می‌شود؛ ساختار پایگاه
و استقرار فعلی تغییر نمی‌کنند. آماده‌سازی زنده، خروجی شبکه، پاسخ دوزبانه، شروع آفلاین و بازگشت
دقیق در گام‌های MCP-02/03 پذیرفته می‌شوند.
