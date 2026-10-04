# Reference workspace and Omid Signal Gate / محیط بررسی و دروازهٔ سیگنال امید

Status: bounded source-only UI candidate, 2026-10-04. This is not a deployment or production gate.
وضعیت: نامزد محدودِ رابط در کد منبع، ۴ اکتبر ۲۰۲۶؛ نه استقرار و نه پذیرش محیط عملیاتی.

## Problem and requirements / مسئله و الزامات

The owner supplied a 1672 × 941 investigation reference and requested working semantic controls,
not a screenshot interface. Preserve the deployed vanilla frontend, identity/session contracts,
saved-chat ownership, evidence integrity and read-only boundaries. Separately create an original
OCS teal/gold login scene. This overrides the prior single-palette presentation for authenticated
product chrome only; corporate tokens and the exact embedded OCS mark remain unchanged.

مالک، تصویر مرجعِ ۱۶۷۲ × ۹۴۱ و رابط تعاملی خواسته است، نه تصویری با ناحیه‌های کلیک پنهان.
فرانت‌اند فعلی، قرارداد ورود و نشست، مالکیت گفتگو، صحت شواهد و مرز فقط‌خواندنی حفظ می‌شوند.
صحنهٔ ورود مستقل با سبزآبی و طلایی OCS ساخته می‌شود. رنگ بنفش/آبی فقط به محیط محصول پس از
ورود اختصاص دارد؛ مقادیر پایهٔ برند و نشان اصلی شرکت بدون تغییر می‌مانند.

| ID | Requirement / الزام | Source and acceptance / کد و پذیرش |
| --- | --- | --- |
| UI-R01 | Reference proportions; real controls / تناسب مرجع و کنترل واقعی | `index.html`, `workspace.css`; 238px sidebar, 64px topbar, 392px inspector at 1672px; responsive screenshots |
| UI-R02 | Truthful provenance, missing/stale/partial states / منشأ و وضعیت صادقانهٔ شاهد | `investigation-view.js`; archived-turn selection, raw-field allowlist, scoped rows, tabs and copy browser tests |
| UI-R03 | Original corporate login and bounded motion / ورود اختصاصی و حرکت محدود | `login.css`, `login-motion.js`; 700ms reveal, 18s/4px float, 12–16s packets; pause, visibility and reduced-motion checks |
| UI-R04 | EN/FA, RTL/LTR, accessible drawers / دوزبانگی و کشوهای دسترس‌پذیر | Native dialogs, tabs, labels, focus restoration; five viewport sizes, keyboard and zoom-equivalent reflow |
| UI-R05 | No security/backend regression / عدم پسرفت امنیت و بک‌اند | Existing API/unit/PostgreSQL/browser tests, login errors, expiry/logout, owner isolation, IME, duplicate/cancellation handling |
| UI-R06 | Local assets and no production fixtures / دارایی محلی و جداسازی دادهٔ آزمایشی | Unchanged CSP; fresh contexts with non-loopback destinations blocked; API asset tests and wheel inventory |

## Non-goals and threat considerations / خارج از دامنه و ملاحظات تهدید

No React/framework migration, new runtime dependency, authentication replacement, persistent token
storage, service worker, connector change, schema change, model/prompt/profile change, live credentials,
server operation or deployment. Agents and UI visibility are not authorization boundaries.

هیچ مهاجرت چارچوب، وابستگی اجرایی تازه، جایگزینی احراز هویت، ذخیرهٔ دائمی توکن، service worker،
تغییر اتصال‌دهنده، schema، مدل، پرامپت، نمایهٔ استنتاج یا عملیات سرور در دامنه نیست. نمایش یا
پنهان‌بودن دکمه، مرز مجوز نیست؛ سیاست قطعی بک‌اند همچنان تصمیم می‌گیرد.

Untrusted model/evidence text uses safe text rendering. The inspector takes explicit diagnostic
fields, not complete API objects/private drafts. Fixture activation is server-side in test modules
only, visibly labelled “Demo data — not live”; there is no client toggle or failed-live-to-demo path.
Search uses already permitted page content. Follow-ups focus the composer or open evidence; no
remediation is executed. Stopping browser waiting does not prove remote cancellation or authorize
blind retries. Required audit failures retain the existing backend behavior.

متن مدل و شاهد غیرقابل‌اعتماد، امن و به‌صورت متن نمایش داده می‌شود. پنل شواهد فقط فیلدهای
تشخیصی مشخص را می‌گیرد، نه کل پاسخ API یا پیش‌نویس خصوصی مدل. دادهٔ ساختگی فقط در سرور آزمون
فعال و آشکارا برچسب‌گذاری می‌شود؛ انتخابگر تولید یا جایگزینِ پنهان برای خرابی زنده ندارد.
جست‌وجو محدود به محتوای مجاز صفحه است. پیگیری فقط پرسش یا نمایش شاهد است؛ اصلاح زیرساخت اجرا
نمی‌شود. توقف انتظار مرورگر، توقف راه دور یا مجوز تکرار کورکورانه را اثبات نمی‌کند.

## Plan, tasks and deviations / برنامه، کارها و تفاوت‌ها

1. Inspect Git, current contracts/assets and authoritative state; capture the old UI.
2. Keep the current stack; separate foundation, workspace, evidence, presentation adapter and motion.
3. Reconstruct geometry, connect existing flows, then implement the corporate login.
4. Inspect/refine multiple deterministic EN/FA, desktop/mobile/static passes.
5. Re-run regression, type/lint, offline asset and package checks; update paired guides and indexes.

۱. بررسی Git، قراردادها و وضعیت معتبر و ثبت تصویر رابط قبلی؛ ۲. حفظ فناوری فعلی و تفکیک
پایه، محیط، شواهد، نگاشت نمایشی و حرکت؛ ۳. بازسازی چیدمان و اتصال گردش‌کارها و سپس ورود؛
۴. چند دور بازبینی تصویر قطعی در دو زبان و اندازه‌های مختلف؛ ۵. آزمون پسرفت، دارایی و بسته
و به‌روزرسانی راهنماها و فهرست اسناد.

Intentional corrections: local CPU label instead of GPT-4o; private/read-only organization card
instead of subscription/quota; actual scoped counts instead of example numbers; freshness/support
instead of confidence; no inferred cause, fabricated history or unrecorded execution stages.
Missing structured findings explain their absence rather than guessing from prose. Copy question
replaces share because no permitted share-link contract exists. System fonts replace the image's
unidentified font; no licensed Vazirmatn artifact was provisioned. Layout is reference-matched,
not a claim of pixel identity. No ADR is needed: existing architecture/security decisions remain.
Functional input/dialog borders have stronger contrast than the reference; the decorative panel
borders and base corporate colors are unchanged.

اصلاحات آگاهانه: مدل CPU محلی به‌جای GPT-4o؛ کارت محیط اختصاصی/فقط‌خواندنی به‌جای اشتراک و
سهمیه؛ شمارش واقعیِ نمونهٔ مجاز به‌جای اعداد تصویر؛ تازگی شاهد به‌جای ضریب اطمینان؛ و حذف
علت، سابقه یا مرحلهٔ اجراییِ ساختگی. نبود یافتهٔ ساختاریافته توضیح داده می‌شود، نه اینکه
از نثر مدل حدس زده شود. «کپی پرسش» جای اشتراک‌گذاری است، چون قرارداد لینک اشتراک نداریم.
فونت محلی سیستم استفاده می‌شود؛ فایل دارای مجوز Vazirmatn فراهم نشده است. تطبیق چیدمان،
ادعای برابری تک‌تک پیکسل‌ها نیست. معماری و تصمیم‌های امنیتی تغییر نکرده‌اند؛ ADR تازه لازم نیست.
مرز ورودی و پنجرهٔ تعاملی برای کنتراست بهتر از مرجع قوی‌تر است؛ مرز تزئینی کارت و رنگ پایهٔ
شرکت ثابت می‌ماند.

## Acceptance and rollback / پذیرش و بازگشت

Subsequent owner-authorized deployment: [2026-10-05 record](REFERENCE_UI_LIVE_QUALIFICATION_2026-10-05.md)
documents real app `836b1ea` rollback/reapply, browser/audit acceptance and the explicit unrun gates.
The original source-only scope and historical statements below describe the earlier handoff.

استقرار مستقلِ بعدی با مجوز مالک در گزارش ۵ اکتبر ثبت است: بازگشت/استقرار دوبارهٔ واقعیِ
`836b1ea`، پذیرش مرورگر/ممیزی و معیارهای اجرا‌نشده. دامنه و عبارت‌های تحویل صرفاً کدیِ زیر،
سابقهٔ گام قبلی‌اند.

See the paired [English record](../en/REFERENCE_UI.md) / [گزارش فارسی](../fa/REFERENCE_UI.md) for
commands, results, screenshot paths and limits. Existing live acceptance is not overwritten.
WAN-blocked browser fixtures prove local UI assets only, not real model/LAN/offline cold start.
Full assistive-technology review and live deployment qualification remain separate.

Rollback is a reviewed source revert of this bounded UI change and a rebuild through the existing
package process. No database migration or operational credential change is needed. Do not reset
unrelated work or deploy a revert without a separate change window. Exact live rollback was not run.

بازگشت، revert بازبینی‌شدهٔ همین تغییر رابط و ساخت دوباره با روال بسته‌بندی فعلی است؛ migration
پایگاه یا تغییر اطلاعات ورود لازم نیست. کار نامرتبط پاک نشود و بازگشت روی سرور بدون پنجرهٔ
تغییرِ جدا اجرا نشود. بازگشت زنده در این کار آزموده نشده است.
