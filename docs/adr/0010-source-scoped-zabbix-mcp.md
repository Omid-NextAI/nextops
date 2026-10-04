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

### Placement clarification — 2026-10-04

The owner reaffirmed the existing connector VM's MCP role. This addendum clarifies, rather than
replaces, the decision above and active master sections 5/12. The canonical MCP gateway belongs
on `nextops-connectors-ro`, with separately identified isolated runners reusing existing drivers.
Plan authenticated internal Streamable HTTP over verified TLS from the app; local stdio alone
cannot connect the two VMs. Keep application-owned authorization/durable audit and runner-only
target credentials. A new VM, a permanent parallel non-MCP stack or a direct runner bypass is
not selected. HTTP preservation means staged compatibility and exact rollback, not permanent
architectural divergence or automatic fallback after MCP denial. Compatibility must traverse
the same policy/audit boundary; disable the old interface at qualified cutover. Current HTTP
deployment remains unchanged. MCP-01 open review items and MCP-02/03 qualification still apply.

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

### تصریح جانمایی — ۴ اکتبر ۲۰۲۶

مالک نقش MCP ماشین موجودِ اتصال‌دهنده را دوباره تصریح کرد. این پیوست، تصمیم بالا و بخش‌های
۵ و ۱۲ پرامپت فعال را روشن می‌کند، نه جایگزین. درگاه اصلی MCP روی `nextops-connectors-ro`
قرار می‌گیرد؛ اجراکننده‌ها با فرایند و هویت جدا از گردآورنده‌های موجود استفاده می‌کنند. ارتباط
برنامه با درگاه، Streamable HTTP داخلی با احراز هویت و TLS معتبر در نظر گرفته شده است؛ stdio
محلی به‌تنهایی ارتباط دو ماشین را برقرار نمی‌کند. مجوز و ممیزی ماندگار نزد برنامه و اطلاعات
ورود مقصد فقط نزد اجراکننده می‌مانند. ماشین تازه، سامانهٔ غیر-MCP موازی و دائمی یا مسیر مستقیمِ
دورزن انتخاب نشده‌اند. حفظ HTTP یعنی سازگاریِ دورهٔ گذار و بازگشت دقیق، نه انحراف دائمی معماری
یا جایگزینی خودکار پس از رد MCP. مسیر سازگاری باید از همان مرز سیاست و ممیزی بگذرد و رابط
قدیمی پس از گذارِ پذیرفته‌شده غیرفعال شود. استقرار HTTP فعلی ثابت است؛ موارد بازِ بازبینی
MCP-01 و معیارهای MCP-02/03 همچنان باقی‌اند.

## MCP-02 composition addendum / پیوست اتصال عملیاتی MCP-02

### English

Status: bounded source implementation, pending live qualification. See the
[discovery specification](../requirements/MCP_LIVE_DISCOVERY_SPEC.md).

Decision: the app uses a gateway-specific protected service bearer over verified loopback TLS
inside the existing verified SSH tunnel. It never forwards the browser bearer or a target token.
The gateway binds a fixed, deployment-owned service principal to the approved environment. The
app remains authoritative for the current end user: PostgreSQL session/version/scope checks and
mandatory access/investigation audit occur before collection and publication. Source and target
identities survive in stored evidence and the prompt. The gateway's fsynced text-free journal is
a supplemental service audit, linked by correlation, not a substitute for the app's user audit.

A separate Linux UID owns the read runner. Its Unix socket checks the gateway peer UID; the gateway
also checks the runner UID. Closed named reads reuse existing drivers, including primary Zabbix
and Linux incidents. Only the runner gets target credentials and approved target egress; the
gateway has loopback-only IP access and no target-secret/registry access. At most two runner reads
execute, with bounded protocol frames, native request deadlines and no queue. The old HTTP unit
is disabled only at a qualified cutover and retained for matched rollback, never fallback.

Alternatives: a new distributed grant database would enlarge this read-only increment without
adding end-user authority beyond the existing app. Forwarding user tokens creates an audience
violation. Combining runner/gateway identities violates credential isolation. These are rejected.
This private app-only bearer profile is not a general third-party OAuth service; external MCP
clients or write operations require a separately reviewed authorization design.

Consequences: a compromised app/service bearer remains a trusted-boundary compromise, limited to
approved read-only tools and targets. Deployment must prove protected delivery and tunnel binding,
group scoping, service isolation, durable audit, offline restart and matched rollback. Local tests
alone cannot establish those facts. No new database schema beyond additive user migration 0004.

### فارسی

وضعیت: پیاده‌سازی محدود در کد؛ پذیرش زنده هنوز لازم است.
[مشخصات کشف](../requirements/MCP_LIVE_DISCOVERY_SPEC.md) مرجع این گام است.

تصمیم: برنامه، توکن خدمتِ اختصاصی درگاه را روی TLS معتبرِ loopback درون تونل SSH با هویت
تأییدشده به کار می‌گیرد؛ توکن مرورگر یا مقصد ارسال نمی‌شود. هویت خدمت درگاه در استقرار به
محیط مجاز محدود است. مرجع کاربر نهایی همچنان برنامه است: نشست، نسخهٔ اطلاعات ورود و دامنه
در PostgreSQL بررسی و دسترسی/تحقیق پیش از گردآوری و انتشار ممیزی می‌شوند. شناسهٔ منبع و
مقصد در شاهد ذخیره‌شده و پرامپت می‌ماند. دفتر بدون متن شاهد و با fsync درگاه، ممیزی تکمیلی
خدمت است که با شناسهٔ هم‌بستگی پیوند می‌خورد؛ جایگزین ممیزی کاربر در برنامه نیست.

اجراکننده UID جدا دارد. سوکت Unix آن UID درگاه را بررسی می‌کند و درگاه نیز UID اجراکننده
را می‌سنجد. خواندن‌های بسته و نام‌دار، گردآورنده‌های فعلیِ زبیکس اصلی و بررسی Linux را حفظ
می‌کنند. اطلاعات ورود و خروجی شبکهٔ مقصد فقط نزد اجراکننده‌اند؛ درگاه صرفاً loopback دارد و
به اطلاعات ورود یا فهرست خصوصی مقصد دسترسی ندارد. حداکثر دو خواندن اجرا می‌شود؛ پیام، مهلت
درخواست و خروجی محدودند و صفی وجود ندارد. unit قبلی HTTP فقط پس از گذار پذیرفته‌شده غیرفعال
و برای بازگشتِ هماهنگ حفظ می‌شود، نه جایگزینی خودکار.

گزینه‌های ردشده: پایگاه تازهٔ مجوز توزیع‌شده دامنهٔ این گام فقط‌خواندنی را بی‌دلیل گسترش
می‌دهد؛ ارسال توکن کاربر با مخاطب آن ناسازگار است؛ یکی کردن هویت درگاه و اجراکننده جداسازی
اطلاعات ورود را از بین می‌برد. این نمایهٔ خصوصیِ مختص برنامه، خدمت عمومی OAuth نیست؛ مشتری
MCP بیرونی یا عملیات نوشتن به طراحی مجوزِ جدا و بازبینی‌شده نیاز دارد.

پیامد: نفوذ به برنامه یا توکن خدمت، نفوذ به یک مرز اعتماد است، اما اختیار همچنان به ابزار
فقط‌خواندنی و مقصد مجاز محدود می‌ماند. تحویل محافظت‌شده، تونل، دامنهٔ گروه، جداسازی خدمت،
ممیزی ماندگار، شروع آفلاین و بازگشت هماهنگ باید در استقرار اثبات شوند. آزمون محلی این موارد
را اثبات نمی‌کند. جز migration افزایشیِ مدیریت کاربر 0004، ساختار تازهٔ پایگاه لازم نیست.
