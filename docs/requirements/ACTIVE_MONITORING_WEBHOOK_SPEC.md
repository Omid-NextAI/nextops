# Active-monitoring webhook feature packet / مشخصات پایش فعال با Webhook

Version 0.1 · 2026-10-31 · **proposed, documentation only / پیشنهادی، فقط مستندات**.

## Problem and outcome / مسئله و خروجی

Operators currently initiate evidence investigations. The owner requests a complete team handoff
for source-driven Splunk/Zabbix notifications and bounded automatic evidence analysis. Existing
MCP, deterministic authorization, local CPU inference, identity and audit must be preserved.

اکنون اپراتور بررسی شواهد را آغاز می‌کند. مالک سند کامل تحویل به تیم برای اعلان رخدادمحور
Splunk/Zabbix و تحلیل خودکار محدود می‌خواهد؛ MCP، مجوز قطعی، مدل CPU محلی، هویت و ممیزی موجود
باید حفظ شوند.

## Detailed contract / قرارداد تفصیلی

- [English team handoff](../en/ACTIVE_MONITORING_WEBHOOKS.md)
- [راهنمای کامل فارسی برای تیم](../fa/ACTIVE_MONITORING_WEBHOOKS.md)
- Existing boundaries / مرزهای موجود: [architecture](../en/ARCHITECTURE.md),
  [MCP](../en/MCP.md), [security](../en/SECURITY.md), [offline](../en/OFFLINE_RUNTIME.md).

The paired guides define the same proposed contract. This packet supplies shared requirement IDs,
work packages and the acceptance matrix; it does not create another runtime or release manifest.

دو راهنمای جفت، یک قرارداد پیشنهادی را تعریف می‌کنند. این پرونده شناسهٔ مشترک نیازمندی، بستهٔ
کار و ماتریس پذیرش را می‌دهد؛ runtime یا manifest انتشار دیگری ایجاد نمی‌کند.

## Requirements / نیازمندی‌ها

| ID | Requirement / نیازمندی |
|---|---|
| AW-R01 | Preserve working app/AI/MCP and target credential isolation; no cloud fallback or new VM. / حفظ سامانهٔ موجود و جداسازی اعتبارنامه؛ بدون ابر یا VM تازه. |
| AW-R02 | Authenticate the exact source profile over verified TLS; payload is never authorization. / احراز نمایهٔ دقیق منبع با TLS معتبر؛ payload مجوز نیست. |
| AW-R03 | Commit inbox, required audit and work item atomically before success. / commit اتمی inbox، ممیزی و کار پیش از موفقیت. |
| AW-R04 | Bound bytes, rate, queues, leases, retries, retention, source calls and shared inference. / محدودیت حجم، نرخ، صف، lease، retry، نگهداری، فراخوانی منبع و مدل مشترک. |
| AW-R05 | Separate delivery, source revision and incident identity; reconcile duplicates/order/recovery/gaps. / تفکیک هویت تحویل، revision و incident؛ تطبیق تکرار، ترتیب، بازیابی و شکاف. |
| AW-R06 | Recheck source/target/index permission at collection/publication and each operator view. / بازبینی مجوز منبع/مقصد/index هنگام دریافت، انتشار و نمایش اپراتور. |
| AW-R07 | Preserve provenance, source/receive/collection times, evidence hashes and partial/stale states. / حفظ منشأ، زمان‌های مجزا، هش شاهد و وضعیت ناقص/قدیمی. |
| AW-R08 | Treat log text as untrusted; redact before storage/AI; never execute model-selected SPL/URLs. / متن لاگ غیرقابل‌اعتماد؛ پالایش پیش از ذخیره/AI؛ بدون SPL/URL انتخابی مدل. |
| AW-R09 | Keep general Q&A usable; source facts survive unavailable AI; EN/FA and accessible UI. / حفظ چت عمومی؛ حفظ واقعیت منبع در قطعی AI؛ پنل دوزبانه و دسترس‌پذیر. |
| AW-R10 | Resume committed work offline/restart, prove exact rollback and record every unrun gate. / ادامهٔ کار ثبت‌شده در آفلاین/restart، اثبات بازگشت دقیق و ثبت معیار اجرا‌نشده. |
| AW-R11 | Match native payload/authentication/retry to installed versions; never assume native custom headers. / تطبیق payload/هویت/retry با نسخه؛ بدون فرض header سفارشی بومی. |
| AW-R12 | No source mutation or automatic incident cause claim; notification delivery is separately qualified. / بدون تغییر منبع یا علت قطعی خودکار؛ پذیرش جدا برای تحویل اعلان. |

## Threats and non-goals / تهدیدها و موارد خارج از دامنه

Consider forged/replayed messages, source impersonation, SSRF, prompt injection, payload bombs,
event floods, cross-scope data leakage, timing/order ambiguity, poisoned deduplication keys,
source-result expiry, worker duplication, native-call drain, secrets in diagnostics and audit failure.
No raw-log replication, SIEM replacement, unrestricted search, automatic remediation, model/runtime
replacement, hidden network broadening, or claimed exactly-once processing is authorized.

پیام جعلی/بازپخش، جعل هویت، SSRF، تزریق پرامپت، payload حجیم، سیل رخداد، نشت بین دامنه‌ها، ابهام
زمان/ترتیب، کلید تکرار مخرب، انقضای نتیجه منبع، worker تکراری، drain، secret در لاگ و شکست ممیزی
بررسی شوند. تکثیر خام، جایگزینی SIEM، جست‌وجوی آزاد، اصلاح خودکار، جایگزینی مدل/runtime، گسترش
پنهان شبکه و ادعای exactly-once مجاز نیستند.

## Work packages / بسته‌های کار

| Package | Work and exit evidence / کار و شاهد خروج |
|---|---|
| AW-P0 | Private source dossier, authentication compatibility and owner approvals. / پروندهٔ خصوصی منبع، سازگاری هویت و تأیید مسئول‌ها. |
| AW-P1 | Closed native/canonical schemas and sanitized fixtures; no operational access. / schema بسته و fixture پالایش‌شده؛ بدون دسترسی عملیاتی. |
| AW-P2 | Restricted PostgreSQL migration, atomic inbox/audit/outbox, leases and cursor tests. / migration محدود، transaction اتمی، lease و تست نشانگر. |
| AW-P3 | Authenticated bounded receiver, worker, retry/reconciliation; disabled flags by default. / گیرنده و worker محدود احرازشده، retry/تطبیق؛ flag پیش‌فرض خاموش. |
| AW-P4 | Version-qualified Splunk reader, preserved Zabbix MCP and shared-model admission. / خواندن Splunk سازگار با نسخه، حفظ MCP زبیکس و پذیرش مشترک مدل. |
| AW-P5 | Scoped EN/FA incident UI, local notification, evidence/analysis distinction. / پنل دوزبانه محدود، اعلان محلی، تفکیک شاهد و تحلیل. |
| AW-P6 | Isolated lab and separately authorized one-source pilot, rollback and operator sign-off. / lab جدا و pilot تک‌منبع با مجوز مستقل، بازگشت و تأیید اپراتور. |

## Acceptance matrix / ماتریس پذیرش

Every row is **`not_run` for this feature**. The documentation publication changes none to passed.
Record actual command/test ID, exact artifact/policy/adapter, scope, timestamp and protected evidence
reference when executing. Unit fixtures, real PostgreSQL, lab devices and live pilot are different
evidence classes. Thresholds in the guide are proposed starting values, not measured service levels.

تمام ردیف‌ها برای این قابلیت **`not_run`** هستند؛ انتشار سند هیچ ردیفی را موفق نمی‌کند. هنگام اجرا،
فرمان/شناسه تست، artifact/سیاست/adapter دقیق، دامنه، زمان و ارجاع شاهد خصوصی ثبت شود. fixture،
PostgreSQL واقعی، تجهیز lab و pilot زنده، شاهد یکسان نیستند. عددهای راهنما نقطهٔ شروع پیشنهادی‌اند.

| Gate | Required proof / شاهد لازم | Class | Status |
|---|---|---|---|
| AW-01 | Valid native messages for both source adapters normalize without invented fields. / تبدیل پیام بومی هر دو منبع بدون فیلد ساختگی. | unit | not_run |
| AW-02 | Missing, bad, expired or revoked credentials fail without fallback. / رد اعتبارنامه غایب، بد، منقضی یا باطل بدون جایگزین. | unit/lab | not_run |
| AW-03 | Trusted TLS/hostname pass; wrong CA, expired cert and redirects fail. / TLS معتبر موفق و CA/گواهی/redirect نامعتبر رد. | lab | not_run |
| AW-04 | Replay window, key rotation and fresh-signed delayed retry are correct. / پنجره بازپخش، تعویض کلید و retry دیرهنگامِ امضاشده درست. | unit/lab | not_run |
| AW-05 | Oversized, compressed, malformed, deep/unknown-field messages stay bounded. / کنترل پیام بزرگ، فشرده، خراب، عمیق و فیلد ناشناخته. | unit/API | not_run |
| AW-06 | No 2xx before atomic inbox/audit/work-item commit; failure returns honestly. / بدون 2xx پیش از commit اتمی؛ خطا صادقانه. | PostgreSQL | not_run |
| AW-07 | Lost ACK then retry creates one logical job; changed-body duplicate is rejected. / retry پس از ACK گم‌شده یک کار بسازد؛ تکرار ناسازگار رد. | PostgreSQL/API | not_run |
| AW-08 | Cross-organization/environment/source/target/index access is denied. / رد دسترسی بین سازمان/محیط/منبع/مقصد/index. | policy/integration | not_run |
| AW-09 | Sender cannot choose actor, destination, privileged scope or callback fetch. / فرستنده actor، مقصد، دامنه بیشتر یا callback دلخواه تعیین نکند. | unit/API | not_run |
| AW-10 | Rates/backlogs cap atomically; arbitrary identities cannot grow counters unbounded. / سقف اتمی نرخ/صف؛ هویت دلخواه شمارنده نامحدود نسازد. | integration/load | not_run |
| AW-11 | Worker crash/lease expiry cannot duplicate an in-flight native call. / crash/lease فراخوانی بومی درحال‌اجرا را تکرار نکند. | integration/fault | not_run |
| AW-12 | Cancellation retains admission until actual drain; uncertain jobs reconcile. / حفظ ظرفیت تا drain واقعی و تطبیق کار نامطمئن. | integration/fault | not_run |
| AW-13 | Retry terminates; held/dead-letter records remain inspectable and scoped. / retry محدود و خطای held قابل‌بررسی و محدود به مجوز. | integration | not_run |
| AW-14 | Recovery-before-problem, duplicates and late updates preserve valid lifecycle. / ترتیب بازیابی/مشکل و تغییر دیررس چرخه را خراب نکند. | unit/integration | not_run |
| AW-15 | Cursor commits only persisted pages; overlap handles late indexing. / نشانگر فقط با صفحه ثبت‌شده جلو رود؛ هم‌پوشانی داده دیررس را پوشش دهد. | integration | not_run |
| AW-16 | Truncated/unavailable/expired source results expose gaps, not completeness. / داده بریده/غایب/منقضی شکاف نشان دهد، نه پوشش کامل. | lab | not_run |
| AW-17 | Splunk authenticates with a proven version-specific profile; API/HEC/MCP tokens are not mixed. / احراز نسخه‌مند Splunk و عدم اختلاط توکن‌ها. | lab/source team | not_run |
| AW-18 | Actual Zabbix actions deliver problem/update/recovery within approved scope. / action واقعی زبیکس سه وضعیت را در دامنه مجاز تحویل دهد. | lab/source team | not_run |
| AW-19 | Full Splunk enrichment remains within approved templates/time/row/byte limits. / شاهد Splunk در الگو و سقف زمان/ردیف/بایت مجاز بماند. | lab/source team | not_run |
| AW-20 | Prompt injection, hostile log text and secret fixtures do not escape/redact incorrectly. / تزریق، متن مخرب و secret آزمایشی نشت نکنند و درست پالایش شوند. | security/unit | not_run |
| AW-21 | Evidence retains provenance, separate timestamps, scope and canonical hash. / حفظ منشأ، زمان مجزا، دامنه و هش استاندارد شاهد. | integration | not_run |
| AW-22 | Required late audit/policy failure blocks publication and revoked users lose access. / شکست ممیزی/سیاست دیرهنگام نمایش را ببندد؛ کاربر باطل دسترسی نداشته باشد. | PostgreSQL/API | not_run |
| AW-23 | AI outage/timeout preserves facts and honest partial/unavailable analysis. / قطعی/timeout مدل واقعیت منبع و وضعیت صادقانه را حفظ کند. | fault/browser | not_run |
| AW-24 | Shared one-active/two-queued model bounds and interactive fairness survive storms. / سقف مشترک مدل و انصاف چت در طوفان رخداد حفظ شود. | load | not_run |
| AW-25 | Fresh EN/FA summaries cite evidence and separate observations from hypotheses. / تحلیل تازه فارسی/انگلیسی با شاهد و جداسازی فرضیه. | local model/lab | not_run |
| AW-26 | EN/FA, RTL/LTR, keyboard, mobile and non-color states work. / زبان، جهت، صفحه‌کلید، موبایل و وضعیت بدون اتکای صرف به رنگ. | browser/manual | not_run |
| AW-27 | Fresh login/generation/evidence and worker restart work with actual WAN denied, LAN allowed. / ورود/تولید/شاهد تازه و restart با WAN واقعاً قطع و LAN مجاز. | authorized lab | not_run |
| AW-28 | Cold start and source recovery resume only committed authorized work. / cold start و بازیابی منبع فقط کار مجاز ثبت‌شده را ادامه دهند. | authorized lab | not_run |
| AW-29 | Retention/quotas/purge do not erase required audit or permit replay after dedup expiry. / نگهداری/سهمیه/purge ممیزی لازم را حذف یا بازپخش را ممکن نکند. | PostgreSQL/fault | not_run |
| AW-30 | Exact rollback preserves inbox/audit and existing login/chat/Zabbix behavior. / بازگشت دقیق، inbox/ممیزی و رفتار قبلی را حفظ کند. | lab/pilot | not_run |
| AW-31 | Panel notification delivery/failure is visible; external channels stay disabled. / تحویل/شکست اعلان پنل آشکار؛ کانال بیرونی خاموش. | browser/lab | not_run |
| AW-32 | Source/platform/network/privacy/operations owners sign the scoped pilot record. / تأیید مسئول منبع/شبکه/حریم خصوصی/عملیات در رکورد pilot محدود. | owner review | not_run |

## Rollback and documentation / بازگشت و مستندات

Use the guide's non-destructive rollback: disable only new admission, coordinate source actions,
drain/hold, retain inbox/audit/cursors, restore exact prior artifacts and verify existing operations.
Implementation must update paired guides, traceability, current state/next task and the release
manifest only for evidence actually obtained. Independent recovery and all older open gates remain
open. Documentation-only validation does not require contacting any managed server.

بازگشت بدون حذف طبق راهنما: توقف پذیرش جدید، هماهنگی action منبع، drain/held، حفظ inbox/ممیزی/
نشانگر، بازگرداندن artifact دقیق و آزمون رفتار موجود. در پیاده‌سازی، دو راهنما، ردیابی، وضعیت/
گام بعد و manifest فقط مطابق شاهد واقعی تغییر کنند. بازیابی مستقل و معیارهای باز قبلی باز
می‌مانند. بررسی صرف مستندات نیازی به تماس با سرور مدیریت‌شده ندارد.

## Open decisions / تصمیم‌های باز

Before implementation: exact source versions and private endpoints; per-source authentication;
source target/index scope; service principal and recipient permissions; approved latency/retention/
rate budgets; migration/lease semantics; Splunk adapter placement; recovery/backfill tolerance;
local notification owner; pilot window and rollback owner. Proposals are not filled with guesses.

پیش از پیاده‌سازی: نسخه و endpoint خصوصی منابع، احراز هر منبع، دامنهٔ مقصد/index، هویت service و
مجوز گیرنده، سقف تأخیر/نگهداری/نرخ، معنای migration/lease، محل adapter اسپلانک، تحمل بازیابی/
جبران، مسئول اعلان محلی و پنجره pilot/مسئول بازگشت تعیین شوند؛ مقدار غایب حدس زده نشود.

## Publication validation / بررسی انتشار سند

On 2026-10-31, local documentation validation passed for 149 Markdown files and 40 EN/FA guide
pairs; release-status validation and `git diff --check` passed. A separate local structural check
confirmed 21 paired guide sections, five identical technical code blocks, parseable JSON, 32 unique
runtime gates all marked `not_run`, and no private IPv4 addresses/private-key blocks in the new
documents. Manual review checked language parity and the proposed/current-state distinction.

در ۳۱ اکتبر ۲۰۲۶، بررسی محلی مستندات برای ۱۴۹ Markdown و ۴۰ جفت راهنما، بررسی manifest و
`git diff --check` موفق بود. بررسی ساختاری جدا، ۲۱ بخش متناظر، پنج code block فنی یکسان، JSON
قابل‌خواندن، ۳۲ معیار یکتای `not_run` و نبود IPv4 خصوصی/کلید خصوصی در سندهای تازه را تأیید کرد.
برابری معنایی زبان و تفکیک پیشنهاد از وضعیت جاری دستی مرور شد.

```powershell
$env:PYTHONUTF8 = '1'
uv run --no-sync python scripts/check_docs.py
uv run --no-sync python scripts/check_release_status.py
git diff --check
```

The first Windows documentation invocation reached the structural pass but failed while printing
Persian through a CP1252 console; setting `PYTHONUTF8=1` resolved it without changing source. These
checks are documentation-only; vendor delivery, webhook API, AI, browser, load, server and offline
qualification were not run or credited.

The staged documentation-only diff also passed `gitleaks git --staged --redact --no-banner --no-color`
with no detected leaks. This is a secret-scan result, not a complete security assessment.

اجرای نخست ویندوز پس از عبور ساختاری، هنگام چاپ فارسی در کنسول CP1252 خطا داد؛ تنظیم
`PYTHONUTF8=1` بدون تغییر کد آن را رفع کرد. این بررسی‌ها فقط مستندات‌اند؛ تحویل سازنده، API
Webhook، AI، مرورگر، بار، سرور و پذیرش آفلاین اجرا یا موفق محسوب نشده‌اند.

تغییرات staged صرفاً مستنداتی، اسکن Gitleaks بالا را نیز بدون مورد شناسایی‌شده گذراندند؛ این
نتیجهٔ اسکن secret است، نه ارزیابی کامل امنیت.
