# NOC/SOC conversational workspace / محیط گفت‌وگوی NOC و SOC

## Bounded answer-depth amendment / اصلاح محدودِ عمق پاسخ — 2026-09-29

Problem: the serving 384-token general model can stop before a useful complex explanation;
generic incident prompts can bury the requested service/network observations in unrelated data.
Requirement: test at most 512 general output tokens, the existing contract ceiling, while live
monitoring/incidents remain 384. Select only existing authorized Linux service, journal, socket,
route or resolver observations relevant to the incident question, with distinct Zabbix/Linux
scope and timestamps. Keep full canonical evidence, hash and audit unchanged. If the selected
model view is shortened, mark it explicitly; do not infer firewall/VPN/remote state or cause.

Non-goals: no new model, training, retrieval, connector, device credentials, arbitrary shell,
Internet use, VM/runtime/queue/deadline increase, or claim of universally correct answers.
Threats: longer unsupported prose, truncation, prompt injection in collected fields, mistaken
Zabbix/Linux host equivalence and treating a socket/route/resolver as service or path health.
Acceptance: EN/FA unit/API/browser scope and exclusion tests, bounded serialization, exact offline
package and locked CI, held-out human technical review of raw model output, fresh authenticated
live evidence/audit, measured completion and exact APP/AI source rollback. If model semantics or
deadline fail, retain the serving 384-token release. No ADR is needed for this prompt projection:
it neither widens evidence collection nor changes authority or the immutable artifact architecture.

مسئله: پاسخ عمومی با سقف ۳۸۴ توکن گاهی پیش از توضیح کاربردیِ پرسش پیچیده ناتمام می‌ماند؛
متنِ عمومی رخداد نیز ممکن است مشاهدهٔ سرویس یا شبکهٔ خواسته‌شده را میان داده‌های نامرتبط پنهان
کند. نیاز: سقف ۵۱۲ توکن، یعنی حداکثر قرارداد فعلی، فقط برای حالت عمومی آزموده شود و پایش و
رخداد روی ۳۸۴ بمانند. از مشاهده‌های موجود و مجازِ Linux دربارهٔ سرویس، ژورنال، سوکت، مسیر یا
نام‌سرور فقط موارد مرتبط با پرسش انتخاب شوند؛ دامنه و زمانِ جداگانهٔ Zabbix و Linux روشن باشد.
شاهد اصلی، هش و ممیزی ثابت و کوتاه‌شدنِ نمای مدل آشکار بماند. سلامت سرویس یا مسیر، علت قطعی،
سیاست فایروال، وضعیت VPN و تجهیزات راه دور از یک مشاهده حدس زده نشوند.

افزودن مدل، آموزش، بازیابی سند، اتصال، اطلاعات ورود، اجرای آزاد فرمان، اینترنت یا افزایش VM،
محیط اجرا، صف و مهلت هدف نیست. خطرها عبارت‌اند از متنِ بلند اما بی‌پشتوانه، ناتمامی پاسخ،
تزریق دستور در شاهد، یکسان دانستن میزبان Zabbix و Linux و برداشتِ سلامت از سوکت، مسیر یا
نام‌سرور. پذیرش به آزمون دوزبانهٔ واحد و API و مرورگر برای دامنه و استثنا، اندازهٔ محدودِ متن،
بستهٔ دقیق آفلاین، CI قفل‌شده، بازبینی انسانیِ پاسخ خام به پرسش‌های کنارگذاشته‌شده، شاهد زنده
و ممیزیِ تازه، زمان‌سنجی و بازگشت دقیق کدِ برنامه/API نیاز دارد. شکست معنا یا مهلت، نسخهٔ
مستقرِ ۳۸۴ توکنی را حفظ می‌کند. ADR تازه لازم نیست؛ این انتخابِ متن، گردآوری شاهد، مرز مجوز
یا معماریِ فایلِ تغییرناپذیر را عوض نمی‌کند.

Status: bounded implemented/controlled qualification, 2026-09-29; exact 862d311 app/API with unchanged
35B, five CI jobs, fresh offline package, nine live browser/API cases, three audit/hash pairs and
exact b346c3e source rollback passed. Full independent technical quality remains partial; no
exact-release server-WAN/VM cold-start or production acceptance. The owner requests a clearer conversational
frontend and broader technical guidance while keeping the existing OCS palette and logo. This is
not authorization for new device connectors, infrastructure changes, training, external AI or
unrestricted command execution. Current serving identity remains in
[the release manifest](../status/current-release.yaml).

## Problem and requirements

The previous screen replaced each answer and sent independent questions. Improve continuity and
readability without turning prior prose into current operational evidence:

- Preserve the exact locally embedded OCS mark and all existing brand/semantic color tokens.
- Keep the local static frontend; no framework migration, font/CDN download or new dependency.
- Add a responsive conversation thread, compact composer, new-conversation control, safe text/code
  formatting, copy controls, explicit modes and bilingual NOC/SOC starter questions.
- Keep at most twelve visible completed turns in browser memory. No persisted conversation storage;
  clear it on new conversation, logout or session expiry. Refresh begins a new conversation.
- General Q&A may submit at most two prior general question/answer pairs, each field at most 2,000
  characters and serialized JSON at most 6,000 characters. Never silently clip an accepted question.
  Label browser context untrusted and model-only; it cannot supply roles, tools, authority or facts.
- Live Zabbix and Linux investigations remain independent fresh collections. They reject history
  fields. Do not mix earlier live evidence or failed/redirected answers into general-model context.
- NOC/SOC guidance covers servers/services, network diagnostics and defensive security concepts:
  answer first, prefer read-only checks, identify assumptions and hypotheses, ask one useful missing
  detail, request redacted diagnostics, never invent execution/compromise/device access/advisories.
  A failed check must not uniquely establish a cause; successful checks establish only their own
  scope. Keep alternatives open and bound diagnostic commands where appropriate.
  A bounded deterministic guard rejects named affirmative single-check blanket health/security
  conclusions. It does not certify all advice or treat unrecognized prose as verified.
- Preserve deterministic guards, typed evidence, scope, audit, stale/partial warnings, unknowns,
  authenticated routes, 384 output tokens, 120 seconds and one active/two queued requests.

## Non-goals and threats

No universal-answer or ChatGPT-equivalence claim. No new firewall/network/VMware connector, retrieval
store, durable chat schema, streaming endpoint, file upload, training or automatic remediation.
General advice remains unverified model knowledge. New connectors still require scoped identities,
allowlists, bounded outputs and their own reviewed acceptance. Agent/prompt instructions are not
security boundaries.

Treat questions, prior answers and diagnostics as untrusted text. Render with DOM text nodes, never
model-supplied HTML, executable links, remote images or scripts. System/provider/purpose overrides
remain forbidden. Prevent double submission and discard late responses after logout/session changes.
Never expose credentials, save transcripts to localStorage, or claim client elapsed time proves a
server processing phase. A failed request retains the question for explicit retry, not blind retry.

## Plan and acceptance

1. Extend only the general request with a closed, bounded context contract and local advisory prompt.
2. Improve the existing static frontend with preserved branding, progressive evidence disclosure,
   bounded in-memory turns, keyboard/IME behavior and native RTL/LTR/code isolation.
3. Add API tests for old-client compatibility, context bounds, forged roles, authorization,
   full-question preservation and live-mode separation. Browser fixtures cover conversation/context,
   no evidence carry-over, hostile HTML, copying, expiry/logout races, mobile and reduced motion.
4. Run formatting/types/unit/API/browser/docs checks and locked CI. Fixtures validate boundaries,
   not actual model accuracy. Exact-package live EN/FA, NOC/SOC relevance, deadline, audit and rollback
   qualification remains a separate deployment gate; keep earlier failed/not-run evidence.

Rollback: restore the exact previous immutable app/API packages without database migration; deploy
inference before app and roll back app before inference. Older general clients omit history and
continue working. Do not change the selected 35B model, runtime, resources, target credentials or
recovery disposition. Update paired UI/API/integrity/test guides, state, next task and traceability.
No new ADR is needed: this is optional, nonpersistent, untrusted request context behind the existing
application/provider boundaries, not a new orchestration or memory architecture.

## فارسی

وضعیت: پیاده‌سازی و پذیرش محدودِ کنترل‌شدهٔ برنامه/API نسخهٔ 862d311 با مدل ثابتِ 35B. پنج
کنترل CI، بستهٔ تازهٔ آفلاین، نُه مورد زندهٔ مرورگر/API، سه تطبیق ممیزی و هش و بازگشت دقیق کد
به b346c3e موفق‌اند. صحت فنیِ مستقلِ کامل ناقص است؛ پذیرش WAN سرور، شروع سرد VM همین انتشار
یا تولید ادعا نمی‌شود.

مالک خواسته است ظاهر و تجربهٔ گفت‌وگو بهتر شود و راهنمایی فنیِ شبکه و امنیت گسترش یابد، بدون
تغییر نشان و رنگ‌های OCS. این کار مجوز افزودن اتصال به تجهیزات، اجرای آزاد فرمان، آموزش مدل یا
استفاده از هوش مصنوعی خارجی نیست. راهنمایی عمومی از دانش مدل است و وضعیت زندهٔ زیرساخت نیست.

رابط ایستای محلی حفظ می‌شود؛ گفت‌وگوی خوانا، کادر نوشتن ساده، شروع گفت‌وگوی تازه، کپی پاسخ و
نمایش ایمن متن و کد اضافه می‌شوند. حداکثر دوازده نوبت کامل فقط در حافظهٔ همین صفحه می‌مانند و با
گفت‌وگوی تازه، خروج، پایان نشست یا بارگذاری مجدد پاک می‌شوند. هیچ متن گفت‌وگویی در localStorage
ذخیره نمی‌شود. در حالت عمومی، حداکثر دو جفت پرسش و پاسخ قبلی ارسال می‌شود؛ هر بخش حداکثر دو
هزار نویسه و JSON مجموع حداکثر شش هزار نویسه است. متن پذیرفته‌شده بی‌اعلان کوتاه نمی‌شود.
این سابقه صرفاً زمینهٔ تأییدنشده است، نه شاهد، مجوز یا اثبات اجرای عملیات. حالت‌های پایش و بررسی
رخداد سابقه را نمی‌پذیرند و همچنان شاهد تازهٔ مجاز می‌گیرند. پاسخ ناموفق یا ارجاعی وارد زمینه نمی‌شود.

دستیار برای سرور، سرویس، شبکه و امنیت دفاعی، ابتدا پاسخ مرتبط و کوتاه می‌دهد، مشاهده را از فرضیه
جدا می‌کند، بررسی فقط‌خواندنی پیشنهاد می‌دهد و در صورت نیاز یک سؤال روشن می‌پرسد. سیستم‌عامل،
نسخه، توپولوژی، نفوذ قطعی یا دسترسی به تجهیزات را حدس نمی‌زند؛ رمز یا کلید نمی‌خواهد و ادعای
اجرای فرمان، تغییر فایروال یا مشاهدهٔ مستقیم نمی‌کند. خروجی تشخیصی باید پالایش‌شده باشد؛ مشاوره
مجوز تغییر نیست. درستی تمام پاسخ‌ها یا هم‌ارزی با ChatGPT تضمین نمی‌شود.
ناموفق بودن یک بررسی، به‌تنهایی علت قطعی را ثابت نمی‌کند؛ موفق بودن آن نیز فقط در دامنهٔ همان
بررسی معتبر است. علت‌های جایگزین و مهلت مناسبِ فرمان تشخیصی باید روشن بمانند.
کنترل قطعیِ محدود، نتیجه‌گیری مثبتِ سلامت یا امنیت کلی از یک بررسی را رد می‌کند؛ همهٔ مشاوره‌ها
را تأیید نمی‌کند و متنِ شناسایی‌نشده را راستی‌آزمایی‌شده نمی‌نامد.

رنگ‌ها و نشان، فارسی RTL و انگلیسی LTR، جداسازی کد، کنترل قطعیِ مجوز، منشأ شاهد، ممیزی، قیدهای
قدیمی/ناقص و سقف ۳۸۴ توکن و ۱۲۰ ثانیه ثابت‌اند. متن مدل با گرهٔ متن نمایش داده می‌شود، نه HTML
یا پیوند اجرایی. ارسال هم‌زمان تکراری و نمایش پاسخ دیررس پس از خروج باید مهار شوند. آزمون API و
مرورگر، مرزها و ظاهر را می‌سنجد، نه صحت مدل واقعی. استقرار زنده با بستهٔ دقیق، پرسش تازهٔ دوزبانه،
زمان پاسخ، ممیزی و بازگشت، گام جداست. بازگشت با بستهٔ قبلی و بدون مهاجرت پایگاه انجام می‌شود؛
مدل، محیط CPU، منابع، اطلاعات ورود مقصد و وضعیت تعویق بازیابی تغییر نمی‌کنند. راهنماهای دوزبانه،
وضعیت، کار بعدی و ردیابی در همین تغییر به‌روز می‌شوند.
