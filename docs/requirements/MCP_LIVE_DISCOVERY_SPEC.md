# MCP-02/03 — Approved source discovery / کشف منابع مجاز

## English

Problem: the reviewed source-scoped reader is not composed into the deployed application. The
owner requests completion and visibility of the second API-only Zabbix source in the app and AI.

Requirements: use the existing connector VM, official pinned MCP SDK, authenticated internal
Streamable HTTP over verified TLS and the existing verified SSH tunnel. A separately identified
runner alone owns target tokens, endpoints and Linux credentials. Its Unix socket accepts only
the gateway UID, closed named operations and bounded messages. The app authorizes the current
session before collection and again before publication; durable PostgreSQL investigation audit
is mandatory. The gateway additionally fsyncs text-free service/correlation/source audit records.
No browser or model receives service credentials. No automatic source fallback is permitted.

Bind app, gateway and runner manifests with an opaque canonical SHA-256 over each exact source
and target configuration (tenant, environment, endpoint, CA/credential references, host and groups).
Carry and verify this identity through MCP and the peer-verified socket before collection and
publication. Reject missing live catalogue identities and drift; logical names alone are insufficient.
This metadata digest is not a secret, artifact signature or replacement for verified TLS.

Discovery means listing approved, immutable logical source/target metadata, not scanning networks,
auto-enrolling groups or granting new access. Display an approved catalogue separately from live
health. Empty/unobserved groups are not qualified. Namespace selected-source provenance in stored
evidence, prompts and UI. Preserve the primary monitoring and Linux drivers with named MCP reads;
disable the old credential-bearing HTTP service at the qualified cutover, retaining exact rollback.

Non-goals: new model, thinking promotion, new VMs, ESXi/storage changes, write tools, automatic
remediation, remote AI, or production certification. The failed model PRs remain unpromoted.

Threats: stolen service bearer, socket impersonation, inventory injection, source/host collisions,
revoked user sessions, missing audit, unbounded queues and TLS downgrade. Use protected credentials,
peer UID checks, root-owned manifests, typed identities, permission rechecks, fail-closed audit,
two active reads/no queue and fixed verified HTTPS origins. Tool descriptions cannot authorize.

Plan/tasks: compose runner and gateway; adapt primary/incident client; expose an authorized source
catalogue and selected-source investigation; add bilingual controls; test protocol, policy, failure,
provenance and browser boundaries; provision exact offline artifacts; run guarded live acceptance.

Acceptance: local contract/API/real PostgreSQL/browser tests; current-source regression; second-source
fresh Persian/English questions with source/time/scope/audit; denied/invalid requests; unavailable
source isolation; credential/process isolation; Internet-blocked fresh login/generation/evidence;
restart and exact rollback. Record outcomes, latency and resource observations. Simulations are
not live/offline acceptance. A catalogue entry is not proof of a healthy monitoring engine.

Rollback: protected previous release/config/units, automatic bounded rollback timer during cutover;
restore the old tunnel/service and app atomically. User-management migration 0004 is additive;
preserve accounts/data and do not blindly downgrade. Stop on artifact, identity or scope mismatch.

Documentation: paired MCP/operator/testing guides, state/next task, release manifest and traceability.
This bounded increment extends MCP-01's discovery non-goal; it does not authorize dynamic enrollment.

## فارسی

مسئله: خوانندهٔ محدود به منبع بازبینی شده، اما هنوز به برنامهٔ مستقر متصل نیست. مالک تکمیل
این کار و نمایش منبع دوم زبیکس، فقط از طریق API، در برنامه و پاسخ هوش مصنوعی را خواسته است.

الزامات: ماشین موجودِ اتصال‌دهنده، SDK رسمی با نسخهٔ ثابت، Streamable HTTP داخلیِ احرازشده
با TLS معتبر و تونل SSH با هویت تأییدشده حفظ شوند. تنها اجراکننده با فرایند و هویت جدا، توکن،
نشانی مقصد و کلیدهای Linux را دارد. سوکت Unix فقط UID درگاه، عملیات نام‌دار و پیام محدود را
می‌پذیرد. برنامه پیش از گردآوری و پیش از انتشار، نشست جاری را دوباره بررسی می‌کند؛ ممیزی
تحقیق در PostgreSQL الزامی است. درگاه نیز رخدادهای بدون متن شاهد را با شناسهٔ هم‌بستگی،
منبع و هش، به‌صورت ماندگار و با fsync ثبت می‌کند. اطلاعات ورود به مرورگر یا مدل نمی‌رسند.
جایگزینی خودکار منبع ممنوع است.

فهرست برنامه، درگاه و اجراکننده با SHA-256 قطعیِ پیکربندی دقیقِ هر منبع و مقصد پیوند داده شود:
سازمان، محیط، نشانی، مرجع گواهی و اطلاعات ورود، میزبان و گروه‌ها. این هویت از MCP و سوکت
با UID تأییدشده عبور کند و پیش از گردآوری و انتشار کنترل شود. نبود هویت در فهرست زنده یا
اختلاف پیکربندی موجب رد درخواست شود؛ نام منطقی به‌تنهایی کافی نیست. هش فراداده نه محرمانه
است، نه امضای فایل، و جایگزین TLS معتبر نیز نیست.

کشف در این گام، نمایش فهرست تغییرناپذیرِ منابع و مقصدهای تأییدشده است؛ نه پویش شبکه، ثبت
خودکار گروه یا افزایش دسترسی. فهرست مجاز از سلامت زنده جدا نمایش داده شود. گروه خالی یا
مشاهده‌نشده پذیرفته‌شده محسوب نمی‌شود. منشأ انتخاب‌شده در شاهد ذخیره‌شده، پرامپت و رابط بماند.
گردآورندهٔ اصلی و Linux با خواندن‌های نام‌دار MCP حفظ و خدمت HTTP دارای اطلاعات ورود، پس
از گذار پذیرفته‌شده غیرفعال شود؛ بازگشت دقیق به نسخهٔ قبل ممکن بماند.

خارج از دامنه: مدل تازه، ارتقای حالت تفکر، VM جدید، تغییر ESXi یا ذخیره‌سازی، عملیات نوشتن،
اصلاح خودکار، هوش مصنوعی خارجی و ادعای پذیرش تولید. PRهای شکست‌خوردهٔ مدل ارتقا نمی‌یابند.

تهدیدها: سرقت توکن خدمت، جعل هویت سوکت، تزریق در فهرست، تداخل شناسه‌ها، ابطال نشست، نبود
ممیزی، صف نامحدود و تنزل TLS. کنترل‌ها شامل اطلاعات ورود محافظت‌شده، UID همتا، فهرست متعلق
به root، قرارداد دارای نوع، بازبینی مجوز، شکست بستهٔ ممیزی، دو خواندن فعال بدون صف و HTTPS
ثابت و معتبرند. توضیح ابزار مجوز نیست.

برنامه: اتصال اجراکننده و درگاه؛ سازگارسازی مسیر اصلی و بررسی رخداد؛ فهرست مجاز و تحقیق
محدود به منبع؛ کنترل دوزبانه؛ آزمون پروتکل، سیاست، خرابی، منشأ و مرورگر؛ آماده‌سازی آفلاین
فایل‌های دقیق؛ سپس پذیرش زندهٔ محافظت‌شده.

پذیرش: آزمون محلی قرارداد/API/PostgreSQL واقعی/مرورگر؛ عدم پسرفت منبع فعلی؛ پرسش تازهٔ فارسی
و انگلیسی از منبع دوم با منبع، زمان، دامنه و ممیزی؛ رد درخواست نامعتبر؛ جداسازی خرابی منبع؛
جداسازی اطلاعات ورود و فرایند؛ ورود، تولید و گردآوری تازه با اینترنت بسته؛ شروع مجدد و
بازگشت دقیق. نتیجه، تأخیر و مصرف منابع ثبت شوند. شبیه‌سازی پذیرش زنده/آفلاین نیست؛ وجود در
فهرست نیز سلامت موتور پایش را اثبات نمی‌کند.

بازگشت: نسخه، پیکربندی و unit قبلی محافظت شوند؛ هنگام گذار تایمر محدودِ بازگشت خودکار برقرار
باشد. خدمت، تونل و برنامهٔ قبلی بازگردند. migration شمارهٔ 0004 افزایشی است؛ حساب‌ها و داده
حفظ شوند و ساختار پایگاه کورکورانه پایین آورده نشود. در اختلاف هویت، فایل یا دامنه توقف شود.

مستندات: راهنمای جفت MCP/عملیات/آزمون، وضعیت، کار بعدی، manifest و ردیابی به‌روز شوند. این
گام محدود، بخش «عدم کشف» MCP-01 را گسترش می‌دهد، نه اینکه ثبت پویای منابع را مجاز کند.
