# Project state / وضعیت پروژه

Current provisioning checkpoint — **2026-10-06; not model acceptance**: exact `293164e` passed
all five CI jobs in [run 37378458739](https://github.com/Omid-NextAI/nextops/actions/runs/37378458739).
The reviewed 122B importer is installed root-owned/mode `0400`, with exact source parity;
main/independent definition checks passed. The first desktop window
`resume-20261006-639268346254710321` failed at `remote_begin`, before any range download or root
start/result record. Read-only reconciliation confirmed stopped transport/absent open handles
and unchanged serving PIDs 2187/2197, restart counts 0/0 and ready/idle state. Isolated runner
tests identified the missing `ProgramData` variable; a distinct reviewed v2 desktop helper and
read-only reconciliation passed. Window `resume-20261006-639268352065353249` **completed one
range**, index 133/268435456 bytes, with protected receipts, recoverable canonical data,
verified-duplicate cleanup and unchanged baseline. The subsequent v2 window
`resume-20261006-639268355159703524` completed indexes **134–137**, each 268435456 bytes;
root finish/stopped reconciliation and the original ready/idle baseline passed. The current
canonical total is **138 ranges/37044092928 bytes**, not complete-shard verification; the prior
134-range snapshot remains historical. The v3 helper passed 430 preparation checks, then its
first actual window `resume-20261006-639268362479556681` failed at `finite_download`, exit 1,
zero accepted ranges. Root stopped/baseline reconciliation was reported true; the failed bodies
are retained and the canonical count is unchanged. No speed gain or import is claimed. The
distinct serial window `resume-20261006-639268366509946555` completed indexes **138–140**,
each 268435456 bytes, at **22:40:16 UTC**, with root finish/stopped/baseline checks passed.
The latest canonical total is **141 ranges/37849399296 bytes**; seven first-shard ranges remain,
not a complete-shard result. No later range or transfer-performance cause is claimed. The
protected one-shard assembler and its newly prepared desktop wrapper remain local-only/unrun;
peer wrapper checks passed 387 mocks, not actual assembly or permission to run. Typed 122B
source registration is implemented/tested, not deployed or accepted:
main reported 1094 source passes/two POSIX skips/126 deselected in 25.99 seconds; lint, format and
Linux-target types passed. The existing AnyIO warning remains recorded. A broad directory secret
scan included ignored trees and reported 18 findings, not a pass. Main's separate new
staged-change Gitleaks check passed exit 0, not a clean-directory claim. Keep the protected
broad-scan report and triage separate from that narrower result and the earlier CI pass.
Live 35B/public thinking-off remain unchanged. See the [paired record](requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md).

گام جاریِ آماده‌سازی — **۶ اکتبر ۲۰۲۶؛ نه پذیرش مدل**: پنج کنترل CI کد دقیقِ `293164e` در
[اجرای 37378458739](https://github.com/Omid-NextAI/nextops/actions/runs/37378458739) موفق‌اند.
ابزار بررسی‌شدهٔ دریافت 122B با مالکیت root و حالت `0400`، با برابری دقیقِ کد نصب شده؛
کنترل‌های تعریفیِ اصلی/مستقل موفق‌اند. نخستین پنجرهٔ رایانهٔ کاربر با شناسهٔ
`resume-20261006-639268346254710321` در `remote_begin`، پیش از دریافت هر بخش و ایجاد رکورد
شروع/نتیجهٔ root شکست خورد. تطبیق صرفاً خواندنی، توقف انتقال، نبود handle باز و ثبات
PIDهای 2187/2197، شمار راه‌اندازی مجدد 0/0 و وضعیت آماده/بی‌درخواست را تأیید کرد. آزمون
جداگانهٔ محیط اجرا، نبود متغیر `ProgramData` را مشخص کرد؛ ابزار مستقلِ نسخهٔ دوم و تطبیق
صرفاً خواندنی موفق‌اند. پنجرهٔ `resume-20261006-639268352065353249` **یک بخش** با اندیس
۱۳۳/۲۶۸۴۳۵۴۵۶ بایت را کامل کرد؛ رسید محافظت‌شده، دادهٔ اصلیِ قابل‌بازیابی، حذف نسخهٔ تکراریِ
تأییدشده و ثبات خط مبنا ثبت شدند. پنجرهٔ بعدیِ نسخهٔ دوم با شناسهٔ
`resume-20261006-639268355159703524` اندیس‌های **۱۳۴ تا ۱۳۷**، هر یک ۲۶۸۴۳۵۴۵۶ بایت، را
کامل کرد؛ پایان root، تطبیق توقف و خط مبنای اصلیِ آماده/بی‌درخواست موفق‌اند. مجموع جاری
**۱۳۸ بخش/۳۷۰۴۴۰۹۲۹۲۸ بایت** است، نه تأیید فایل کامل؛ ثبتِ ۱۳۴بخشیِ قبلی سابقه است.
ابزار مستقلِ نسخهٔ سوم، ۴۳۰ کنترل آماده‌سازی را گذراند؛ سپس نخستین پنجرهٔ واقعیِ آن با
شناسهٔ `resume-20261006-639268362479556681` در `finite_download`، با کد خروج ۱ و صفر بخش
پذیرفته‌شده شکست خورد. تطبیق root برای توقف/خط مبنا با مقدار درست گزارش شد؛ بدنه‌های
ناموفق حفظ‌اند و شمار اصلی تغییر نکرد. بهبود سرعت یا دریافت پذیرفته‌شده ادعا نمی‌شود.
پنجرهٔ سریالِ مستقلِ `resume-20261006-639268366509946555` اندیس‌های **۱۳۸ تا ۱۴۰**، هر یک
۲۶۸۴۳۵۴۵۶ بایت، را در ساعت **۲۲:۴۰:۱۶ UTC** با پایان root/تطبیق توقف/ثبات خط مبنا کامل
کرد. مجموع جدید **۱۴۱ بخش/۳۷۸۴۹۳۹۹۲۹۶ بایت** است؛ هفت بخشِ فایل اول باقی‌اند، نه تأیید
فایل کامل. بخش بعدی یا علت کاراییِ انتقال ادعا نمی‌شود.
ابزار محافظت‌شدهٔ تجمیع یک فایل و ابزار تازهٔ اجرای رایانهٔ کاربر فقط محلی/اجرا‌نشده‌اند؛
۳۸۷ کنترل شبیه‌سازیِ ابزار اجرا در بررسی مستقل موفق‌اند، نه تجمیع واقعی یا مجوز اجرا.
ثبت نوع‌دارِ 122B در کد پیاده‌سازی/آزموده شده، نه مستقر یا پذیرفته:
بازبین اصلی ۱۰۹۴ موفق/دو مورد POSIX اجرا‌نشده/۱۲۶ انتخاب‌نشده در ۲۵٫۹۹ ثانیه ثبت کرد؛
کنترل lint، قالب و نوع برای Linux موفق‌اند. هشدار قبلیِ AnyIO حفظ شده است. بررسی گستردهٔ
اطلاعات محرمانه، درخت‌های ignored را نیز خواند و ۱۸ یافته ثبت کرد، نه نتیجهٔ موفق. بررسی
مستقلِ تغییرهای staged با Gitleaks در اجرای اصلی با کد خروج صفر موفق شد، نه پاک بودن کل
پوشه. گزارش محافظت‌شدهٔ بررسی گسترده و تعیین تکلیف آن جدا از نتیجهٔ محدود و CI قبلی حفظ شوند.
35B زنده و خاموشی استدلال عمومی ثابت‌اند؛ گزارش دوزبانهٔ بالا مرجع است.

Prior native checkpoint — historical / گام بومیِ پیشین — سابقه:

Latest completed native checkpoint, **2026-10-05 at 21:36:41.463473 UTC**: the distinct
`20261006-q5-b94-ub512-noblas-numa-standard-001` trial failed. Fourteen stopped finals returned;
English hypothesis timed out at **120001 ms**, Persian hypothesis was not run. Main/independent
review agree on **nine passes/six failures/one not run**: unsupported network topology, FA coding
type guards and incomplete stale-evidence provenance/scope remain failures. Load/controller took
6002/776965 ms. Owned cleanup and unchanged ready/idle 35B baseline passed; numeric guest NUMA
masks/pages are not physical placement, affinity-success or performance acceptance. Exact
`7f14ba194668ec2e76696b0d328065b9171dcb22` CI passed all five jobs in
[run 37376324673](https://github.com/Omid-NextAI/nextops/actions/runs/37376324673), not model acceptance.
The next bounded Apache-licensed **Qwen3.5-122B-A10B** import-resumption helpers are local and under
review, not uploaded or run at this checkpoint; retained ranges and storage budgets need fresh
verification. No standard/thinking gate or model selection was created; live 35B/public thinking-off
remain unchanged. See the [paired record](requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md).

آخرین گام بومیِ پایان‌یافته در **۵ اکتبر ۲۰۲۶، ساعت ۲۱:۳۶:۴۱٫۴۶۳۴۷۳ UTC**: آزمون مستقلِ
`20261006-q5-b94-ub512-noblas-numa-standard-001` ناموفق شد. چهارده پاسخ نهایی کامل دریافت شد؛
فرضیهٔ انگلیسی در **۱۲۰۰۰۱ میلی‌ثانیه** از مهلت گذشت و پرسش فارسیِ آن اجرا نشد. بازبینی
اصلی/مستقل، **نه موفق/شش ناموفق/یک اجرا‌نشده** ثبت کردند: توپولوژی بدون شاهد، کنترل نوعِ
کدنویسی فارسی و منشأ/دامنهٔ ناکاملِ شاهد کهنه همچنان ناموفق‌اند. بارگذاری/کنترل‌کننده
۶۰۰۲/۷۷۶۹۶۵ میلی‌ثانیه طول کشید. پاک‌سازی و حفظ خط مبنای آماده/بی‌درخواستِ 35B موفق‌اند؛
ماسک/صفحهٔ عددی NUMA مهمان، جای‌گیری فیزیکی، موفقیت affinity یا پذیرش کارایی نیست. پنج کنترل
CI کد دقیقِ بالا در اجرای پیوندشده موفق‌اند، نه پذیرش مدل. ابزار ادامهٔ دریافت محدودِ
**Qwen3.5-122B-A10B** با مجوز Apache، در این گام فقط محلی و در حال بازبینی است؛ بارگذاری روی
میزبان یا اجرا نشده و بخش‌های قبلی/بودجهٔ ذخیره‌سازی به بررسی تازه نیاز دارند. مجوز استاندارد/
استدلال یا انتخاب مدل ساخته نشد؛ 35B زنده و خاموشی استدلال عمومی ثابت‌اند. گزارش دوزبانهٔ بالا مرجع است.

Previous native checkpoint — historical / گام بومیِ پیشین — سابقه:

Latest native checkpoint, 2026-10-05 at 21:14:22 UTC: the distinct exact-`b94a84c` no-BLAS retest
failed after eleven stopped finals. Persian stale/partial exceeded the unchanged 120-second gate
at 120234 ms; four later injection/hypothesis cases were not run. Main/independent review agree on
seven passes/five failures/four not run. EN evidence preserves source/date/collection time now, but
loses authorized scope; both network answers and FA coding still fail. Startup took 6621 ms,
controller 567205 ms; owned cleanup, seven actual project libraries/no BLAS and unchanged ready/idle
baseline passed in their recorded scopes. The earlier `f6cff8f` failure remains preserved. Exact
`f9a4a83` CI passed all five jobs, including PostgreSQL16/17 and isolated browser checks; this is source
evidence, not candidate acceptance. Live 35B/public-thinking-off remain unchanged. A separately
reviewed NUMA comparison started at 21:23:44 UTC, loaded in 6002 ms and is in progress, not accepted. See the
[paired record](requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md).

گام تازهٔ اجرای بومی در ۵ اکتبر ۲۰۲۶، ساعت ۲۱:۱۴:۲۲ UTC: سنجش مستقلِ بدون BLAS با کد
دقیقِ `b94a84c` پس از یازده پاسخ نهایی کامل ناموفق شد. پرسش فارسیِ شاهد کهنه/ناقص در
۱۲۰۲۳۴ میلی‌ثانیه از حد ثابتِ ۱۲۰ ثانیه گذشت؛ چهار پرسش بعدیِ تزریق/فرضیه اجرا نشدند.
بازبینی اصلی/مستقل، هفت موفق/پنج ناموفق/چهار اجرا‌نشده ثبت کردند. پاسخ انگلیسیِ شاهد
اکنون منبع/تاریخ/زمان گردآوری را حفظ می‌کند، اما دامنهٔ مجاز را حذف می‌کند؛ دو پاسخ شبکه
و کدنویسی فارسی همچنان ناموفق‌اند. بارگذاری ۶۶۲۱ و اجرای کنترل‌کننده ۵۶۷۲۰۵ میلی‌ثانیه
طول کشید؛ پاک‌سازی، نگاشت واقعیِ هفت کتابخانه بدون BLAS و حفظ آمادگیِ خط مبنای بی‌درخواست
در دامنهٔ ثبت‌شده موفق‌اند. شکست قبلیِ `f6cff8f` حفظ است. پنج کنترل CI کد دقیقِ `f9a4a83`،
شامل PostgreSQL16/17 و بررسی جداگانهٔ مرورگر، موفق شدند؛ این شاهد کد است نه پذیرش نامزد. 35B زنده و خاموشی
استدلال عمومی ثابت‌اند. مقایسهٔ مستقل و بازبینی‌شدهٔ NUMA ساعت ۲۱:۲۳:۴۴ UTC آغاز و در
۶۰۰۲ میلی‌ثانیه بارگذاری شد؛ اجرا ادامه دارد و پذیرفته نشده است. گزارش دوزبانهٔ بالا مرجع است.

Previous build checkpoint — historical:

Latest build checkpoint, 2026-10-05 at 20:20:41 UTC: fresh no-BLAS build003 completed all 214
steps, exit 0, in 130332 ms. Its recorded sandbox, cleanup and unchanged ready/idle baseline
passed. Read-only inspection of all eight ELF outputs found literal `$ORIGIN` RUNPATHs, with
no temporary absolute or empty search component. Binary SHA:
`eb53d6eef8bdae6f1227a93af1f6caf58542fb5943b03ccc80d136316e6f5721`.
Protected packaging, complete dependency review and native execution remain separate; no model
selection, thinking or context acceptance follows. Preserve rejected build002 and failed build001.

گام تازهٔ ساخت در ۵ اکتبر ۲۰۲۶، ساعت ۲۰:۲۰:۴۱ UTC: ساخت مستقلِ بدون BLAS شمارهٔ ۰۰۳، هر
۲۱۴ گام را با کد صفر در ۱۳۰۳۳۲ میلی‌ثانیه کامل کرد. کنترل محیط اجرا، پاک‌سازی و حفظ آمادگیِ
خط مبنای بدون درخواست موفق‌اند. بررسی صرفاً خواندنیِ هر هشت فایل ELF، مسیر لفظیِ `$ORIGIN`
را بدون مسیر مطلقِ موقت یا بخش خالی نشان داد؛ هش فایل اجرایی در بالا درج شده است.
بسته‌بندیِ محافظت‌شده، بررسی کامل وابستگی و اجرای واقعی جدا باقی می‌مانند؛ انتخاب مدل،
استدلال یا پذیرش زمینه حاصل نشده است. ساخت نپذیرفتهٔ ۰۰۲ و ساخت ناموفقِ ۰۰۱ حفظ شوند.

Previous build checkpoint — historical:

Latest runtime checkpoint, 2026-10-05: isolated no-BLAS build002 compiled successfully in 138380 ms
with verified CPU/OpenMP/native flags, four-CPU/eight-GiB bounds and network-denied DynamicUser.
Cleanup and unchanged live baseline passed. Read-only ELF review rejected its temporary absolute
RUNPATHs and empty path components for relocatable trial packaging. No built runtime was executed
or installed. Preserve build001's earlier configure/cache-guard failure and build002's outputs;
review fresh build003 with literal `$ORIGIN` loader paths before artifact/closure verification.
The opt-in candidate identity verifier preserves original v1.0 behavior/schema and requires separate
external binary/inventory anchors for v1.1. Main checks: 176 focused/1053 source tests passed, two
POSIX skips, 126 deselected in 24.99 seconds; lint/format/Linux-target types passed. This is not
runtime/model acceptance. Exact `23dabae` CI passed all five jobs
([run](https://github.com/Omid-NextAI/nextops/actions/runs/37360223624)). See the paired record below.

گام تازهٔ runtime در ۵ اکتبر ۲۰۲۶: ساخت مستقلِ بدون BLAS شمارهٔ ۰۰۲ در ۱۳۸۳۸۰ میلی‌ثانیه
موفق شد؛ تنظیم CPU/OpenMP/native، حدود چهار CPU/هشت GiB و DynamicUser بدون شبکه بررسی شدند.
پاک‌سازی و حفظ خط مبنای زنده موفق‌اند. بررسی خواندنیِ ELF، مسیر مطلقِ موقت و بخش خالیِ
RUNPATH را برای بسته‌بندیِ قابل‌انتقال نپذیرفت. runtime ساخته‌شده اجرا یا نصب نشد. شکست
پیشینِ کنترل cache در ساخت ۰۰۱ و خروجیِ ساخت ۰۰۲ حفظ شوند؛ ساخت تازهٔ ۰۰۳ با مسیر لفظیِ
`$ORIGIN`، پیش از بررسی فایل/وابستگی بازبینی شود. بازبین صریحِ هویت نامزد، رفتار/schema اصلیِ
نسخهٔ ۱٫۰ را حفظ و برای نسخهٔ ۱٫۱ دو هش مستقلِ فایل اجرایی/فهرست را الزام می‌کند. کنترل
اصلی: ۱۷۶ آزمون مرتبط/۱۰۵۳ آزمون کد موفق، دو مورد POSIX اجرا‌نشده و ۱۲۶ مورد خارج از انتخاب
در ۲۴٫۹۹ ثانیه؛ قالب/lint/نوع با هدف Linux موفق‌اند. این پذیرش runtime/مدل نیست. پنج کنترل
CI کد دقیقِ `23dabae` در اجرای بالا موفق‌اند. گزارش دوزبانهٔ زیر مرجع است.

Latest isolated Q5 outcome, 2026-10-05 at 18:48 UTC: the distinct passive-wait trial failed after
two exact format passes. English networking timed out at 120002 ms; thirteen later cases were not
run. Main/independent review and the offline checker agree. Its owned process/unit/listener are
absent, baseline PID/restart count and ready/idle state unchanged, no standard/thinking gate created.
The separately pinned `b94a84c` source archive/wheel/root staging passed code-digest parity and all
five exact CI jobs ([run](https://github.com/Omid-NextAI/nextops/actions/runs/37356458309)); its native
retest remains unrun. A no-BLAS build of the same pinned CPU runtime is a reviewed experiment,
not an accepted optimization or live runtime change. See the [paired record](requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md).

تازه‌ترین نتیجهٔ مستقل Q5، در ۵ اکتبر ۲۰۲۶ ساعت ۱۸:۴۸ UTC: آزمون جداگانهٔ انتظار غیرفعال
پس از دو پاسخ دقیقِ قالب، ناموفق شد. پرسش انگلیسیِ شبکه در ۱۲۰۰۰۲ میلی‌ثانیه از مهلت گذشت؛
سیزده مورد بعدی اجرا نشد. بازبینی اصلی/مستقل و ابزار آفلاین هم‌نظرند. فرایند، واحد و listener
آزمون باقی نمانده؛ شناسهٔ فرایند/شمار restart و آمادگیِ بیکار خط مبنا ثابت‌اند و مجوز استاندارد/
استدلال ساخته نشد. برابری هش کد در بایگانی/بسته/نگهداری محافظت‌شدهٔ `b94a84c` و پنج کنترل CI
همان کد در اجرای بالا موفق‌اند؛ آزمون بومیِ آن اجرا‌نشده است. ساخت بدون BLAS از همان runtime
ثابتِ CPU، آزمایشی بررسی‌شده است، نه بهینه‌سازیِ پذیرفته‌شده یا تغییر runtime زنده. گزارش بالا مرجع است.

New source-only detailed-answer repair, 2026-10-05: generic instructions now explicitly preserve
supplied provenance/limits without claiming independent verification, avoid invented intermediary
topology, and validate required types before value operations. Short-general and evidence prompts,
frozen questions, template controls, limits, policy and serving releases are unchanged. Independent
review found a mutable test-capture gap; deep snapshots plus a mutation regression now cover it.
Main checks: 118 focused tests and 967 non-browser/non-integration tests passed, two POSIX skips,
126 deselected in 25.34 seconds; formatting/lint and 142-file Linux-target Mypy passed. This is
not model training, a native-answer pass or deployment. Preceding exact `2553288` CI passed five
jobs; CI for this later source increment remains separate. Continue isolated scheduling qualification
with frozen `f6cff8f`, then a separately pinned comparison of this changed source.

اصلاح تازه و صرفاً کدِ پاسخ تفصیلی، در ۵ اکتبر ۲۰۲۶: راهنمای عمومی اکنون حفظ صریحِ منشأ/
محدودیت دادهٔ ارسالی، بدون ادعای تأیید مستقل، پرهیز از توپولوژیِ واسطِ ساختگی و کنترل نوع
پیش از عملیات مقدار را می‌خواهد. راهنمای کوتاهِ عمومی/شاهد، پرسش ثابت، کنترل قالب، حدود،
سیاست و نسخه‌های زنده تغییر نکردند. بازبین مستقل خلأ ثبت ورودیِ تغییرپذیر در آزمون را یافت؛
تصویر مستقل از ورودی و آزمون تغییر بعدی آن را پوشش می‌دهند. کنترل اصلی: ۱۱۸ آزمون مرتبط
و ۹۶۷ آزمون غیرمرورگری/غیرپایگاهی موفق، دو مورد POSIX اجرا‌نشده و ۱۲۶ مورد خارج از انتخاب،
در ۲۵٫۳۴ ثانیه؛ قالب/lint و mypy با هدف Linux برای ۱۴۲ فایل موفق‌اند. این آموزش مدل، پذیرش
پاسخ بومی یا استقرار نیست. پنج کنترل CI کد پیشینِ `2553288` موفق‌اند؛ CI این گام بعدی جداست.
آزمون مستقلِ زمان‌بندی با `f6cff8f` ثابت ادامه یابد، سپس مقایسهٔ جدا با هویت دقیقِ کد تازه انجام شود.

Latest isolated Q5 result, 2026-10-05 at 18:08 UTC: the distinct physical-batch512 trial used the
same exact `f6cff8f` source, frozen corpus, 32 threads/16K/384 output/120-second deadline and no
thinking. Eleven finals returned; Persian stale/partial evidence timed out at 120002 ms and four
subsequent cases were not run. Main and independent review agree: six passes, six failures, four
not run. Failures include both coding type guards, network scope/format and missing evidence
provenance. Cleanup passed; baseline PID/readiness stayed unchanged, no unit/listener/timer remains.
No standard/thinking gate or model selection was created. Exact `ead5e30` CI subsequently passed
all five jobs ([run](https://github.com/Omid-NextAI/nextops/actions/runs/37351635415)); that source
result does not qualify the model. A distinct passive OpenMP waiting-policy diagnostic is being
prepared, not executed or accepted. See the [paired private-evidence summary](requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md).

نتیجهٔ تازهٔ آزمون مستقل Q5، در ۵ اکتبر ۲۰۲۶ ساعت ۱۸:۰۸ UTC: آزمون batch فیزیکیِ ۵۱۲ با
همان کد دقیقِ `f6cff8f`، پرسش ثابت، ۳۲ رشته/زمینهٔ 16K/خروجیِ ۳۸۴/مهلتِ ۱۲۰ ثانیه و
استدلالِ خاموش اجرا شد. یازده پاسخ نهایی دریافت شد؛ پرسش فارسیِ شاهد کهنه/ناقص در ۱۲۰۰۰۲
میلی‌ثانیه از مهلت گذشت و چهار مورد بعدی اجرا نشد. بازبینی اصلی و مستقل هم‌نظرند: شش مورد
موفق، شش مورد ناموفق و چهار مورد اجرا‌نشده. کنترل نوع در هر دو پاسخ کدنویسی، دامنه/قالب
پاسخ شبکه و حفظ منشأ شاهد ناموفق‌اند. پاک‌سازی موفق و شناسهٔ فرایند/آمادگیِ خط مبنا ثابت است؛
واحد، listener یا timer باقی نمانده است. مجوز استاندارد/استدلال یا انتخاب مدل ساخته نشد.
هر پنج کنترل CI کد دقیقِ `ead5e30` در اجرای بالا موفق‌اند؛ موفقیت کد، پذیرش مدل نیست. آزمون
مستقلِ انتظار غیرفعال OpenMP در حال آماده‌سازی است، نه اجرا یا پذیرش. گزارش دوزبانهٔ بالا مرجع است.

Source-test repair, 2026-10-05 at 17:48 UTC: exact `76b92ec` CI recorded two stale partial-import
expectation failures and 969 passes; browser, PostgreSQL16/17 and secret jobs passed. The tests now
construct partial states explicitly and preserve ambiguous-status/selection rejection. Main local
suite: 966 passed, two POSIX skips, 126 deselected in 26.94 seconds; focused lint/format passed.
Repair CI is not yet recorded. A distinct physical-batch512 helper is in private preparation, not
an executed trial. Failed Q5 standard and unrun thinking/context/application/WAN gates remain.

اصلاح آزمون کد در ۵ اکتبر، ساعت ۱۷:۴۸ UTC: CI کد دقیق `76b92ec` دو شکستِ انتظار قدیمیِ
دریافت ناقص و ۹۶۹ موفق داشت؛ مرورگر، PostgreSQL16/17 و کنترل اطلاعات محرمانه موفق بودند.
آزمون اکنون حالت ناقص را صریح می‌سازد و رد وضعیت مبهم/انتخاب را حفظ می‌کند. اجرای محلی:
۹۶۶ موفق، دو مورد POSIX اجرا‌نشده و ۱۲۶ انتخاب‌نشده در ۲۶٫۹۴ ثانیه؛ lint/قالب متمرکز موفق‌اند.
CI اصلاح هنوز ثبت نشده است. ابزار خصوصیِ batch فیزیکیِ ۵۱۲ در آماده‌سازی است، نه آزمون
اجراشده. شکست استاندارد Q5 و معیار اجرا‌نشدهٔ استدلال/زمینه/برنامه/WAN باقی‌اند.

Current Q5 checkpoint, 2026-10-05 at 17:29 UTC: all 74 protected transport ranges were assembled;
the complete 19771509664-byte Qwen3.8-27B UD-Q5_K_M artifact matched its pinned upstream SHA-256.
An independent root-private reader rehashed it and verified actual GGUF3/qwen35 metadata and the
9993-byte template; immutable candidate storage is complete, not model selection. The distinct
32-thread/16K standard trial loaded in 7179 ms and verified protected eight-library mappings,
but its first `en-format` case failed at 120010 ms without an answer; fifteen cases were not run.
Cleanup confirmed unit/process/listener absence and unchanged baseline readiness. No standard
approval or thinking/context/application/offline gate follows. All five exact-`e6af416` CI jobs
passed; this is source verification, not model acceptance.
App `3d92b71`, inference `7ce9d29`, serving 35B, public thinking-off and production status are unchanged.

گام جاری Q5 در ۵ اکتبر ۲۰۲۶، ساعت ۱۷:۲۹ UTC: هر ۷۴ بخش انتقال محافظت‌شده به هم پیوستند؛
فایل کاملِ ۱۹۷۷۱۵۰۹۶۶۴ بایتی Qwen3.8-27B UD-Q5_K_M با SHA-256 ثابتِ منبع اصلی مطابق است.
خوانندهٔ مستقل و خصوصیِ root، هش کامل، فرادادهٔ واقعی GGUF3/qwen35 و قالب ۹۹۹۳ بایتی را
بررسی کرد؛ نگهداری نامزدِ محافظت‌شده تکمیل است، نه انتخاب مدل. آزمون مستقل استاندارد با
۳۲ رشته و زمینهٔ 16K در ۷۱۷۹ میلی‌ثانیه بارگذاری و نگاشت هشت کتابخانهٔ محافظت‌شده بررسی شد؛
اما نخستین پرسش `en-format` در ۱۲۰۰۱۰ میلی‌ثانیه بدون پاسخ از مهلت گذشت؛ پانزده مورد اجرا
نشد. پاک‌سازی، نبود واحد/فرایند/listener و آمادگیِ ثابتِ خط مبنا را تأیید کرد. تأیید استاندارد
یا پذیرش استدلال/زمینه/برنامه/آفلاین حاصل نشده است. هر پنج کنترل CI کد دقیقِ `e6af416` موفق‌اند؛
این بررسی کد است، نه پذیرش مدل.
برنامهٔ `3d92b71`، استنتاج `7ce9d29`، مدل زندهٔ 35B، خاموشی استدلال عمومی و وضعیت تولید ثابت‌اند.

New runtime-review source, 2026-10-05: a read-only protected native-tree checker/schema and 90
explicit filesystem-simulation tests are implemented. Main checks: 962 source tests/two POSIX
skips, 156 related tests and lint/types/docs passed. Actual Linux-root verification passed nine
files/fourteen aliases without runtime changes; live 35B stayed idle without restart. Five preceding
exact-`01637a1` CI jobs passed, not CI for this later source. Tree identity is not build/model/offline/
deployment acceptance. Q5 remains partial; no public thinking or serving-model change occurred.

کد تازهٔ بررسی runtime در ۵ اکتبر: ابزار/طرح فقط‌خواندنیِ درخت بومی و ۹۰ آزمون صریحِ شبیه‌سازی
فایل‌سیستم پیاده شدند. کنترل اصلی: ۹۶۲ آزمون کد موفق/دو مورد POSIX اجرا‌نشده، ۱۵۶ آزمون مرتبط
و lint/نوع/مستندات موفق‌اند. بررسی واقعیِ root در Linux، نه فایل/چهارده پیوند را بدون تغییر
runtime تأیید کرد؛ 35B بی‌درخواست و بدون restart ماند. پنج کنترل CI پیشینِ کد دقیق `01637a1`
موفق‌اند، نه CI کد بعدی این گام. هویت درخت، پذیرش ساخت/مدل/آفلاین/استقرار نیست. Q5 ناقص و
استدلال عمومی/مدل زنده ثابت‌اند.

Latest diagnostic, 2026-10-05: the distinct exact-`f6cff8f` Q8 standard retest failed coding,
source/scope preservation and the 120-second hypothesis deadline. Fourteen final answers were
recorded; the final Persian hypothesis was not run. Trial cleanup and unchanged baseline readiness
passed; no thinking/expanded-context/application acceptance or selection followed. The source
reviewer now rejects non-string operations before their type guard: 872 tests/two POSIX skips.
All five earlier exact-`f6cff8f` CI jobs passed; that is not CI or model acceptance for later work.
Protected Q5 preparation reached 48 canonical ranges (12 GiB), still without a complete hash.
See the [updated permissive record](requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md).
App `3d92b71`, inference `7ce9d29`, serving 35B, public thinking-off and production status remain unchanged.

بررسی تازه در ۵ اکتبر: آزمون استانداردِ مستقل Q8 با کد دقیقِ `f6cff8f` در کدنویسی، حفظ منبع/
دامنه و مهلت ۱۲۰ ثانیهٔ فرضیه ناموفق بود. چهارده پاسخ نهایی ثبت شد؛ فرضیهٔ پایانی فارسی اجرا
نشد. توقف/پاک‌سازی آزمون و آمادگیِ ثابتِ مدل سالم موفق‌اند؛ پذیرش استدلال/زمینهٔ گسترده/برنامه
یا انتخاب انجام نشد. بازبین کد اکنون عملیات ورودی غیررشته‌ای را پیش از کنترل نوع رد می‌کند:
۸۷۲ آزمون موفق/دو مورد POSIX اجرا‌نشده. هر پنج کنترل CI پیشین برای `f6cff8f` موفق‌اند؛ این
پذیرش CI یا مدلِ کار بعدی نیست. آماده‌سازی محافظت‌شدهٔ Q5 به ۴۸ بخش اصلی، برابر ۱۲ GiB رسید؛
هش کامل هنوز تأیید نیست. گزارش مجوز آزادِ به‌روز در بالا مرجع است. برنامهٔ `3d92b71`، استنتاج
`7ce9d29`، مدل زندهٔ 35B، خاموشی استدلال عمومی و وضعیت تولید ثابت‌اند.

Source-only follow-up, 2026-10-05: a distinct pinned Apache Qwen3.8-27B UD-Q5_K_M candidate
and generic defensive-coding guidance are prepared. Main local checks passed 835 non-browser/
non-integration tests, two POSIX-only skips, Ruff and Linux-target Mypy; independent bilingual
coding proposals remain ungraded. Complete Q5 import/load/quality is not accepted. The finite 122B
window ended with 133 canonical transport ranges; first 512-MiB 3.8 Q5 ranges are protected, not a
full hash. Prioritize this separate trial; retain partial 122B and failed Q8 results.
See the [permissive packet](requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md). Live app
`3d92b71`, inference API `7ce9d29`, serving 35B, public thinking-off and production status are unchanged.

پیگیری صرفاً کد در ۵ اکتبر: نامزد مستقل و ثابتِ Apache از Qwen3.8-27B UD-Q5_K_M و راهنمای
عمومیِ کدنویسی دفاعی آماده‌اند. کنترل محلیِ عامل اصلی، ۸۳۵ آزمون غیرمرورگر/غیرintegration
موفق، دو مورد POSIX اجرا‌نشده، Ruff و Mypy برای Linux داشت؛ پیشنهادهای مستقلِ دوزبانه هنوز
ارزیابی نشده‌اند. دریافت/بارگذاری/کیفیت کامل Q5 پذیرفته نیست. پنجرهٔ محدود 122B با ۱۳۳ بخشِ
انتقال پایان یافت؛ ۵۱۲ MiB نخستِ 3.8 Q5 محافظت‌شده است، نه هش کامل. آزمون مستقل آن اولویت
دارد؛ بخش‌های ناقص 122B و شکست Q8 محفوظ‌اند. گزارش مجوز آزاد
بالا مرجع است. برنامهٔ زندهٔ `3d92b71`، API استنتاجِ `7ce9d29`، مدل 35B، خاموشی استدلال
عمومی و وضعیت تولید ثابت‌اند.

Latest controlled app, 2026-10-05: `3d92b71` is serving after the selected-evidence aging/partial labels and contextual accessibility
announcements passed 88 browser tests; the earlier 87/88 fixture-login failure remains recorded
with unconfirmed transport cause. Current combined source passed 738 non-browser/non-integration
tests/two POSIX skips, lint/types and documentation checks. The offline 122B qualification planner
prepares frozen standard/thinking/16K/conditional-32K tests but runs no model and accepts no capacity.
See paired [UI guidance](en/REFERENCE_UI.md) / [راهنمای رابط](fa/REFERENCE_UI.md) and the permissive
packet below. Exact-source CI, offline install, first/final real browser/audit, actual five-minute
aging and exact `f169875` rollback/reapply passed. Final code/package/unit/readiness checks passed;
both guards are stopped. Model/public thinking and unrun server-WAN/cold-start gates are unchanged.

انتشار محدودِ تازه در ۵ اکتبر: برنامهٔ `3d92b71` زنده است. سن‌گذاری شاهد انتخاب‌شده، برچسب ناقص و اعلانِ دسترس‌پذیرِ زمینه‌دار،
۸۸ آزمون مرورگر موفق داشتند؛ شکست پیشینِ ۸۷ از ۸۸ و علت انتقالِ تأییدنشده حفظ است. کد ترکیبی
جاری ۷۳۸ آزمون غیرمرورگر/غیرintegration موفق، دو مورد POSIX اجرا‌نشده و کنترل lint/نوع/مستندات
داشت. برنامه‌ریز آفلاین 122B، پرسش ثابتِ پاسخ استاندارد/استدلال/16K/32K مشروط را آماده می‌کند؛
مدل را اجرا یا ظرفیت را پذیرفته اعلام نمی‌کند. دو راهنمای رابط و گزارش مجوز آزادِ زیر مرجع‌اند.
CI همان کد، نصب آفلاین، مرورگر/ممیزی واقعیِ نخست/نهایی، گذشت واقعیِ پنج دقیقه و بازگشت دقیق به
`f169875`/استقرار دوباره موفق‌اند. هویت کد/بسته/واحد و آمادگی تأیید و هر دو محافظ متوقف‌اند.
مدل، استدلال عمومی و معیارهای اجرا‌نشدهٔ WAN سرور/شروع سرد ثابت‌اند.

Earlier owner-directed UI repair/permissive alternative, 2026-10-05: app `f169875` served after
70 local browser regressions, 716 non-browser/non-integration tests (two POSIX skips), all five
exact-source CI jobs and real browser/audit checks. Three actual subagents repaired responsive login
motion, mobile composer, keyboard/navigation/locale/evidence presentation and reviewed licenses.
Hidden-DOM logout cleanup and native request-details state passed. Exact `836b1ea` rollback/reapply
and final identity/unit/readiness checks passed; the final guard is stopped. The [UI repair record](requirements/UI_REPAIR_LIVE_QUALIFICATION_2026-10-05.md)
preserves failed harness attempts and separates browser-origin restriction from unrun server-WAN/
cold-start gates. Connector `2a7c8dc`, inference API `7ce9d29` and serving 35B remain unchanged.
Qwen3.8 27B's new 48-thread/native-thinking coding sample failed the 120-second deadline at
120102 ms and was stopped/verified. Pinned Apache Qwen3.5-122B-A10B Q5_K_M remains supervised
partial provisioning, not loaded/selected; do not label it 3.8 or resume full custom-license Flash
import. See the [permissive packet](requirements/PERMISSIVE_MODEL_QUALIFICATION_2026-10-05.md).
Public thinking, VM resources and full production-acceptance status are unchanged.

گام پیشینِ درخواستی مالک در ۵ اکتبر: برنامهٔ `f169875` پس از ۷۰ آزمون مرورگر محلی، ۷۱۶ آزمون
غیرمرورگر/غیرintegration (دو مورد POSIX اجرا‌نشده)، پنج کنترل CI همان کد و بررسی واقعی مرورگر/
ممیزی زنده شد. سه عامل واقعی، حرکت ورودِ واکنش‌گرا، کادر پرسش موبایل، پیمایش/تمرکز/زبان و
نمایش شاهد را اصلاح و مجوزها را بررسی کردند. پاک‌سازی DOM پنهان هنگام خروج و همگامی جزئیات
درخواست موفق‌اند. بازگشت دقیق به `836b1ea` و استقرار دوباره، کنترل هویت/واحد/آمادگی نهایی موفق
و محافظ نهایی متوقف است. گزارش اصلاح رابط در بالا، شکست ابزار و نبود آزمون WAN سرور/شروع
سرد را جدا نگه می‌دارد. اتصال‌دهندهٔ `2a7c8dc`، API استنتاجِ `7ce9d29` و مدل زندهٔ 35B ثابت‌اند.
نمونهٔ تازهٔ کدنویسی 27B با ۴۸ رشته و استدلال native در ۱۲۰۱۰۲ میلی‌ثانیه از مهلت گذشت؛ توقف
آن تأیید شد. Qwen3.5-122B-A10B Q5_K_M با مجوز Apache در دریافت ناقصِ تحت نظارت است، نه
بارگذاری یا انتخاب؛ 3.8 نامیده نشود و ورود کامل Flash با مجوز اختصاصی ادامه نیابد. گزارش مجوز
آزادِ بالا مرجع است. استدلال عمومی، منابع ماشین و وضعیت پذیرش کامل تولید تغییر نکرده‌اند.

Flash-Next preparation, 2026-10-05: after the owner-managed resize, direct AI checks show 80 vCPUs,
three guest NUMA nodes and 257905 MiB usable RAM. Only the identified blank added 400-GiB disk was
prepared as a separate protected model volume. The pinned Q8 set totals 151.46 GiB; its complete
small metadata shard passed size/hash/actual metadata checks, and 512 MiB of bounded weight ranges
was staged. Full import, CPU load, complete memory fit and Flash generations are not run. The
owner confirms Bank/customer access; custom-license applicability/organizational review is pending.
Source adds pinned sharded metadata, offline readers/reviewers and frozen EN/FA coding/provenance
regressions: 660 passed, two skips. Retained baseline/27B coding failures remain failed. See the
[exact preparation record](requirements/QWEN38_FLASH_QUALIFICATION_2026-10-05.md). No serving
model/limits/public thinking/app/AI/connector cutover; baseline is ready, no download/trial remains.

آماده‌سازی Flash-Next در ۵ اکتبر: پس از افزایش دستی منابع، ۸۰ vCPU، سه گرهٔ NUMA مهمان و
۲۵۷۹۰۵ MiB حافظهٔ قابل‌استفاده مستقیم مشاهده شد. فقط دیسک تازه و خالیِ ۴۰۰ GiB به حجم مستقل
مدل تبدیل شد. مجموعهٔ Q8 ثابت حدود ۱۵۱٫۴۶ GiB است؛ بخش کوچکِ کامل با اندازه/هش و metadata
واقعی تأیید و ۵۱۲ MiB از وزن، محدود آماده شد. ورود کامل، بارگذاری CPU، مصرف کامل و پاسخ Flash
اجرا نشده‌اند. مالک دسترسی کارکنان بانک/مشتری را تأیید کرده؛ بررسی شمول مجوز اختصاصی و تأیید
سازمانی باقی است. هویت ثابت، ابزار آفلاین و آزمون‌های ثابت دوزبانه افزوده‌اند: ۶۶۰ موفق و دو
اجرا‌نشده. شکست کدنویسی مدل زنده/27B حفظ است. گزارش دقیق بالا مرجع است؛ مدل/سقف/استدلال عمومی
و استقرار برنامه/AI/اتصال‌دهنده تغییر نکرده‌اند. مدل سالم آماده و دریافت/آزمون فعالی باقی نیست.

Controlled Qwen 3.8 result, 2026-10-05: pinned 27B Q8 full-file verification, actual GGUF/template
and isolated CPU loading passed. The [dated trial](requirements/QWEN38_QUALIFICATION_2026-10-05.md)
records eight fixed-order standard samples per profile, four native-only thinking arithmetic samples,
16/32-thread timings, a strict non-string coding invariant failure and a 15360-token context
deadline failure at 120163 ms. This profile is **not selected**. Trial process/listener and ephemeral
unit were stopped/removed; exact duplicate download parts were reclaimed after a complete rehash,
with the immutable candidate and private logs retained. No serving-model/VM/resource or public
thinking change. App `836b1ea`, AI `7ce9d29`, connector `2a7c8dc` and 35B remain unchanged. Five
CI jobs passed at source `e39e2c9`; source success is not candidate application/model acceptance.

نتیجهٔ آزمون کنترل‌شدهٔ Qwen 3.8 در ۵ اکتبر: هش کاملِ 27B Q8، قالب/metadata واقعی و بارگذاری
مستقل CPU موفق بود. گزارش تاریخ‌دار بالا، هشت نمونهٔ استاندارد ثابت برای هر نمایه، چهار نمونهٔ
محاسباتیِ استدلال صرفاً native، زمان‌های ۱۶/۳۲ رشته، شکست معیار کدنویسی برای ورودی غیررشته‌ای
و شکست مهلت زمینهٔ ۱۵۳۶۰ توکنی در ۱۲۰۱۶۳ میلی‌ثانیه را ثبت می‌کند. نامزد **انتخاب نشده است**.
فرایند/listener و خدمت موقت متوقف/حذف و فقط بخش‌های تکراریِ دریافت، پس از هش کامل پاک شدند؛
نامزد تغییرناپذیر و log خصوصی حفظ‌اند. مدل زنده، ماشین، منابع و استدلال عمومی تغییر نکردند؛
برنامهٔ `836b1ea`، AI با `7ce9d29`، اتصال‌دهندهٔ `2a7c8dc` و مدل 35B ثابت‌اند. پنج کنترل CI
کد `e39e2c9` موفق‌اند؛ موفقیت کد، پذیرش مدل/برنامهٔ نامزد نیست.

New resource/model increment, 2026-10-05: the owner supplied fresh DS-C/host screenshots and
reports no reserved space. The earlier missing-capacity checkpoint is resolved for one bounded
27B Q8 precision trial, not for unlimited host consumption. Direct AI preflight confirms 80 online
vCPUs/128769 MiB usable RAM/one guest NUMA node/169557 MiB model-volume free; 96-GiB/18-equivalent
serving limits remain. Pinned proxy-chain provisioning is separate from live selection; see the
[qualification packet](requirements/QWEN38_QUALIFICATION_SPEC.md) and paired CPU guides.
Source adds candidate identity, explicit no-thinking/no-preservation standard template controls
and manifest regression tests. Serving app `836b1ea`, AI `7ce9d29`, 35B model and public flags are
unchanged. No VM resize, production-readiness claim or model-quality acceptance is implied.

گام تازهٔ منابع/مدل، ۵ اکتبر: مالک تصاویر جاریِ DS-C/میزبان و نبود فضای رزروشده را اعلام کرده است.
مانع قبلیِ ظرفیت برای یک آزمون محدودِ 27B Q8 رفع شد، نه مصرف نامحدود میزبان. پیش‌بررسی مستقیم،
۸۰ vCPU، حافظهٔ ۱۲۸۷۶۹ MiB، یک گرهٔ NUMA و فضای آزاد ۱۶۹۵۵۷ MiB حجم مدل را تأیید می‌کند؛
سقف زندهٔ ۹۶ GiB/معادل ۱۸ CPU ثابت است. آماده‌سازی از پراکسی، انتخاب زنده نیست؛ بستهٔ پذیرش
بالا و راهنمای دو زبان مبنا هستند. هویت نامزد، خاموشی صریح استدلال/حفظ آن و آزمون manifest در
کد افزوده‌اند. برنامهٔ `836b1ea`، AI با `7ce9d29`، مدل 35B و گزینه‌های عمومی ثابت‌اند. افزایش
ماشین، پذیرش کیفیت مدل یا آمادگی تولید از این گام استنباط نشود.

Earlier controlled app, 2026-10-05 (Tehran): `836b1ea` served the reference workspace/OCS login.
Five exact-code CI jobs and 47 local browser tests passed. Fresh real login/logout, saved-chat
reload/resume, both Zabbix sources, EN/FA generation, evidence selection and durable hash/audit
matching passed. Exact `2a7c8dc` rollback/reapply passed; final rollback guard is stopped. The
[dated UI record](requirements/REFERENCE_UI_LIVE_QUALIFICATION_2026-10-05.md) retains failed trials
and separates browser network restriction from unrun current-app server-WAN/VM cold-start tests.
Connector remains `2a7c8dc`; AI API `7ce9d29`, runtime, Qwen3.5-35B-A3B, thinking-off and resources
are unchanged. At the earlier pre-import checkpoint, Qwen 3.8 metadata was reviewed, not imported;
the new resource/model increment above supersedes that checkpoint's missing capacity. See the paired
[CPU guide](en/CPU_AI.md) / [راهنمای CPU](fa/CPU_AI.md). This is not full production acceptance.

برنامهٔ کنترل‌شدهٔ پیشین، ۵ اکتبر ۲۰۲۶ به وقت تهران: `836b1ea` محیط مرجع و ورود OCS را ارائه
می‌کرد. پنج کنترل CI همان کد و ۴۷ آزمون مرورگر محلی موفق‌اند. ورود/خروج واقعی، ادامهٔ گفتگو
پس از بارگذاری دوباره، دو منبع زبیکس، تولید دوزبانه، انتخاب شاهد و تطبیق هش/ممیزی موفق بودند.
بازگشت دقیق به `2a7c8dc` و استقرار دوباره موفق و تایمر نهایی متوقف است. گزارش تاریخ‌دارِ بالا
شکست‌ها را حفظ و محدودیت شبکهٔ مرورگر را از آزمون اجرا‌نشدهٔ WAN سرور/شروع سرد این نسخه
جدا می‌کند. اتصال‌دهنده `2a7c8dc`، API هوش مصنوعی `7ce9d29`، runtime، مدل Qwen3.5، استدلالِ
غیرفعال و منابع ثابت‌اند. در گام قبلی، metadataِ Qwen 3.8 بررسی شده بود، نه دریافت یا انتخاب؛
گام تازهٔ منابع/مدل در بالا جایگزین مانع ظرفیت آن شده است. پذیرش کامل تولید ادعا نمی‌شود.

## Historical checkpoints / گام‌های تاریخی

The dated records below describe their observation time; they do not override the current
deployment above. / رکوردهای زیر وضعیت زمان خود را بیان می‌کنند، نه وضعیت استقرار جاری را.

Source-only UI candidate, 2026-10-04: `codex/reference-dashboard` reconstructs the supplied
investigation reference in the existing frontend and adds the original OCS Signal Gate login.
Authentication, owner-scoped chats, read-only evidence, CSP and inference remain unchanged.
See the [source handoff](en/REFERENCE_UI.md) / [گزارش فارسی](fa/REFERENCE_UI.md) for verification
and deliberate missing-data states. No server operation/deployment is included; the current
release identity and unfinished operational gates below remain authoritative.

نامزد رابط در کد منبع، ۴ اکتبر ۲۰۲۶: شاخهٔ `codex/reference-dashboard` تصویر محیط بررسی را
در فرانت‌اند فعلی بازسازی و ورود اختصاصی «دروازهٔ سیگنال امید» را اضافه می‌کند. احراز هویت،
مالکیت گفتگو، شاهد فقط‌خواندنی، CSP و استنتاج ثابت‌اند. نتیجهٔ آزمون و نبودهای صریح در گزارش
دوزبانهٔ بالا ثبت است؛ عملیات سرور یا استقرار انجام نشده و وضعیت زنده و معیارهای ناتمامِ زیر
همچنان مرجع‌اند.

Prior controlled deployment, 2026-10-04: app and connector served `2a7c8dc`. The existing connector
VM is now the authenticated TLS MCP gateway/isolated runner; old HTTP is stopped/disabled, not a
fallback. Approved source selection lists two sources/seven targets, with fresh secondary Zabbix
EN/FA CPU answers, durable hash/audit matching, denial, source failure isolation, app/connector
WAN-blocked restart and exact prior-release rollback/reapply. See the
[dated qualification](requirements/MCP_LIVE_QUALIFICATION_2026-10-04.md) for unsuccessful trials,
latency, package identity and scope. Local checks: 646 non-browser plus 30 browser fixtures;
exact runtime CI passed all five jobs including PostgreSQL 16/17. Users panel and additive migration
0004 are deployed; live list/invalid-input checks passed, but account mutation acceptance is not run.
Five empty secondary groups, broad model semantics, full-system cold start/reboot and production
gates remain unfinished. AI/model/resources are unchanged; PRs 46/51 are not promoted.

استقرار کنترل‌شدهٔ پیشین، ۴ اکتبر ۲۰۲۶: برنامه و اتصال‌دهنده انتشار `2a7c8dc` را ارائه می‌کردند.
همان ماشین اتصال‌دهنده اکنون درگاه MCP احرازشده با TLS و اجراکنندهٔ جداست؛ HTTP قبلی متوقف
و غیرفعال است و مسیر جایگزین نیست. دو منبع و هفت مقصد مجاز، پاسخ تازهٔ دوزبانهٔ CPU از
زبیکس دوم، تطبیق هش/ممیزی ماندگار، رد درخواست، جداسازی خرابی منبع، شروع خدمات برنامه و
اتصال‌دهنده با WAN بسته و بازگشت/استقرار دوبارهٔ دقیق آزموده شدند.
[گزارش پذیرش](requirements/MCP_LIVE_QUALIFICATION_2026-10-04.md) شکست‌های اولیه، تأخیر، هویت
بسته و حدود آزمون را ثبت می‌کند. ۶۴۶ آزمون غیرمرورگر و ۳۰ آزمون مرورگر ساختگی موفق‌اند؛
پنج کنترل CI همان کد، شامل PostgreSQL 16/17، موفق بود. پنل کاربران و migration افزایشی 0004
مستقرند؛ فهرست/رد ورودی زنده آزموده شد، نه تغییر حساب. پنج گروه خالی، کیفیت عمومی مدل،
شروع سرد/reboot کل سامانه و معیارهای تولید ناتمام‌اند. AI/مدل/منابع ثابت و PRهای 46/51
ارتقا نیافته‌اند.

Current integration candidate, 2026-10-04: reviewed PR 53/54 foundations are composed on
`codex/zabbix-mcp-live`. Canonical authenticated TLS MCP, separate peer-verified runner, current
PostgreSQL source policy/audit, namespaced durable evidence and bilingual approved-source controls
are implemented. Local acceptance: 635 non-browser checks passed, two POSIX checks skipped on
Windows; 30 real-browser fixture checks passed; strict Linux-target types passed. Live cutover,
fresh second-source AI answers, offline restart and matched rollback are not yet accepted. The
protected API-only preflight observed three hosts in three populated approved groups; five empty
groups remain unobserved. No model/runtime, ESXi/resource or company account change is included.

نامزد یکپارچه‌سازی جاری، ۴ اکتبر ۲۰۲۶: پایه‌های بازبینی‌شدهٔ PR 53/54 روی شاخهٔ
`codex/zabbix-mcp-live` ترکیب شده‌اند. MCP احرازشده با TLS، اجراکنندهٔ جدا با کنترل UID همتا،
سیاست/ممیزی جاری در PostgreSQL، شاهد ماندگار با منشأ مشخص و کنترل دوزبانهٔ منابع مجاز
پیاده شده‌اند. ۶۳۵ آزمون غیرمرورگر موفق، دو آزمون POSIX در Windows اجرا نشده و ۳۰ آزمون
مرورگر واقعی با شاهد ساختگی موفق‌اند؛ بررسی نوع برای Linux موفق است. گذار زنده، پاسخ تازهٔ
AI از منبع دوم، شروع آفلاین و بازگشت هماهنگ هنوز پذیرفته نشده‌اند. پیش‌بررسی محافظت‌شدهٔ
API سه میزبان در سه گروه مجازِ دارای عضو را مشاهده کرد؛ پنج گروه خالی مشاهده نشده‌اند.
تغییر مدل، runtime، ESXi، منابع یا حساب شرکت در این گام نیست.

Owner-requested user panel, 2026-10-04: admin-only scoped listing, fixed read-only account
creation, non-admin activation and password reset are implemented with atomic audit/session
revocation, stale-version denial and protected administrator identities. Bilingual OCS UI retains
brand/theme and offline assets. Initial user-panel CI passed five jobs; a review repair now audits
malformed JSON/body/path/query after fresh session/role checks and fails closed on audit failure.
Local reruns passed 551 unit/API checks and 33 integration tests (14 focused user tests).
This branch is a source candidate, not live. A separate PR 53
repair (`bf983bf`) resolves its three MCP review findings with 39 focused tests and five passing
CI jobs; it is not merged or deployed. PRs 46/51 remain rejected semantic experiments, not release
approvals. Read-only live inspection found app/AI/tunnels active on the recorded releases, only the
primary connector source and no MCP unit/secondary endpoint. The second token/CA remain protected
desktop material; all-group reader permission and gateway/runner qualification remain unfinished.
Guest observation is 80 online vCPUs and 135024599040 usable RAM bytes, not the older screenshot
allocation. No resource, credential, deployment, model or thinking change was made.

پنل درخواستی مالک، ۴ اکتبر ۲۰۲۶: فهرست محدود به دامنهٔ مدیر، ایجاد حساب با دسترسی ثابت و
فقط‌خواندنی، تغییر وضعیت و تنظیم گذرواژهٔ غیرمدیر، با ممیزی/لغو نشست اتمی، رد نسخهٔ قدیمی و
حفاظت از مدیر پیاده شده‌اند. رابط دوزبانهٔ OCS، نشان، تم و دارایی‌های آفلاین را حفظ می‌کند.
CI نخستِ پنل پنج کنترل را گذراند؛ اصلاحِ بازبینی اکنون رد JSON، بدنه، مسیر و پارامتر نامعتبر
را پس از بررسی تازهٔ نشست/نقش ممیزی و خرابی ممیزی را رد می‌کند. اجرای دوبارهٔ محلیِ ۵۵۱ آزمون
واحد/API و ۳۳ آزمون یکپارچگی (۱۴ مورد متمرکزِ کاربران) موفق بود.
این شاخه نامزد کدی است، نه استقرار زنده. اصلاح جداگانهٔ PR 53 با `bf983bf`، سه ایراد MCP را
با ۳۹ آزمون متمرکز و پنج کنترل CI موفق رفع کرد؛ هنوز ادغام یا مستقر نشده است. PRهای 46/51
آزمایش معناییِ ردشده‌اند، نه انتشار تأییدشده. بازرسی زندهٔ فقط‌خواندنی، برنامه/AI/تونل‌های
فعال روی انتشار ثبت‌شده، تنها منبع اولیهٔ اتصال‌دهنده و نبود واحد MCP/نشانی منبع دوم را یافت.
توکن/CA دوم در رایانهٔ توسعه محافظت‌شده‌اند؛ مجوز خوانندهٔ همهٔ گروه‌ها و پذیرش درگاه/اجراکننده
ناتمام‌اند. مشاهدهٔ مهمان ۸۰ vCPU آنلاین و ۱۳۵۰۲۴۵۹۹۰۴۰ بایت حافظهٔ قابل‌استفاده است، نه
تخصیص تصویر قدیمی. منابع، اعتبارنامه، استقرار، مدل یا گزینهٔ استدلال تغییر نکردند.

Review repair, 2026-10-04: PR 53's three source findings are repaired: cancellation during initial
authorization now attempts bounded terminal audit; problem/event ownership is proven through
bounded event/host linkage; application-owned registry/collector ports keep private connector
configuration outside orchestration. All 39 focused tests passed locally. These are fixture-backed
SDK/source checks, not live MCP or second-source acceptance. The historical findings below remain
as context. Read-only server inspection found the original connector configuration only, no
secondary endpoint or MCP unit; app/AI services and their existing tunnels are active. No live
configuration or model changed.

اصلاح بازبینی، ۴ اکتبر ۲۰۲۶: سه ایراد کدیِ PR 53 اصلاح شدند: لغو هنگام بررسی اولیهٔ مجوز،
تلاش محدود برای ثبت ممیزی پایانی دارد؛ تعلق problem/event با پیوند محدود رویداد و میزبان
اثبات می‌شود؛ رابط‌های فهرست و گردآوریِ متعلق به برنامه، تنظیم خصوصی اتصال‌دهنده را بیرون از
منطق کاربرد نگه می‌دارند. هر ۳۹ آزمون متمرکز محلی موفق بود؛ این آزمون‌های SDK/کد با مقصد
ساختگی، پذیرش MCP زنده یا منبع دوم نیستند. ایرادهای تاریخیِ زیر برای حفظ سابقه باقی‌اند.
بازرسی فقط‌خواندنیِ سرور، تنها تنظیم منبع اولیه را یافت؛ نشانی منبع دوم و واحد MCP موجود نیست.
برنامه، AI و تونل‌های موجود فعال‌اند. تنظیم زنده یا مدل تغییر نکرد.

Design clarification, 2026-10-04: the existing connector VM is the intended MCP gateway/isolated
runner host, not a parallel non-MCP platform. Master sections 5/12, paired architecture/MCP guides
and ADR 0010 now explicitly align with the owner's clarification. The deployed connector is still
HTTP; migration compatibility/rollback is temporary, not a permanent bypass. No live change or
new acceptance is claimed. Three open [PR 53](https://github.com/Omid-NextAI/nextops/pull/53) findings
(authorization cancellation audit, problem/event ownership and dependency direction) need repair
and regression tests before MCP-02 composition. Prior test outcomes are preserved, not invalidated
or treated as proof that these paths are safe.

تصریح طراحی، ۴ اکتبر ۲۰۲۶: ماشین موجودِ اتصال‌دهنده میزبان موردنظرِ درگاه MCP و اجراکننده‌های
جداگانه است، نه سامانهٔ غیر-MCP موازی. بخش‌های ۵ و ۱۲ پرامپت، راهنماهای دوزبانهٔ معماری/MCP و
تصمیم 0010 با تصریح مالک هم‌راستا هستند. اتصال‌دهندهٔ مستقر هنوز HTTP است؛ سازگاری و بازگشت
دورهٔ مهاجرت موقت‌اند، نه مسیر دورزن دائمی. تغییر زنده یا پذیرش تازه ادعا نمی‌شود. سه مورد بازِ
[PR 53](https://github.com/Omid-NextAI/nextops/pull/53)، شامل ممیزی لغو هنگام مجوز، تعلق شواهد
problem/event و جهت وابستگی، پیش از MCP-02 به اصلاح و آزمون بازگشت خطا نیاز دارند. نتایج
آزمون قبلی حفظ‌اند، اما اثبات ایمنیِ این مسیرهای بررسی‌نشده نیستند.

Source increment, 2026-10-04: MCP-01 adds a private, source-scoped Zabbix registry, typed
results, mandatory per-call authorization/audit ports and optional official SDK 1.30.0 adapters.
27 focused local tests include real SDK memory/stdio exchanges and explicit protocol cancellation
with fixture downstream data; five-job CI and a fresh hash-locked offline Windows base-package
installation without MCP also passed. This is not durable PostgreSQL, deployed runner, live second-source
UI or offline acceptance. MCP-02 composition and MCP-03 operational qualification remain open.
The existing controlled app/AI/connector identities below, model and thinking flags are unchanged.
See [specification](requirements/MULTI_SOURCE_MCP_SPEC.md) and [MCP guide](en/MCP.md).

گام کدیِ ۴ اکتبر ۲۰۲۶: MCP-01 فهرست خصوصی و محدود به منبعِ زبیکس، نتیجهٔ دارای نوع، مرزهای
الزامیِ مجوز و ممیزیِ هر درخواست و لایه‌های اختیاری SDK رسمیِ 1.30.0 را افزود. ۲۷ آزمون متمرکز
محلی، تبادل واقعی SDK در حافظه و stdio و اعلان صریحِ لغو را با دادهٔ ساختگی مقصد می‌سنجند.
پنج کنترل CI و نصب تازهٔ آفلاینِ هش‌قفلِ بستهٔ پایه در Windows بدون MCP نیز موفق‌اند.
این شاهد، پذیرش PostgreSQL ماندگار، اجراکنندهٔ مستقر، منبع دوم در رابط زنده یا آفلاین نیست.
اتصال عملیاتی MCP-02 و پذیرش MCP-03 بازند. هویت‌های زندهٔ برنامه/AI/اتصال‌دهنده در ادامه، مدل
و گزینه‌های استدلال تغییر نکرده‌اند. [مشخصات](requirements/MULTI_SOURCE_MCP_SPEC.md) و
[راهنمای MCP](fa/MCP.md) را ببینید.

Verified scoped deployment, 2026-10-04: app/AI `7ce9d29` now serve controlled users with the
unchanged CPU-only35 model and disabled thinking. Five-job CI, 524 local checks, three fresh
hash-locked offline installs, 45 functional browser cases across first/offline/exact69 rollback/
final campaigns, 36 text-free completion audits, nine live hash pairs and bounded admission/
recovery passed. Server-side WAN/proxy denial on all four guests and actual app/native-model/API
restart passed with fresh login, answers and LAN evidence. Two final actual UI fallback/reload
cases passed. Only owned transient network/rollback guards were removed; immutable69 remains.
Four failed candidates were exactly rolled back and retained before this accepted repair. Narrow
supplied-scenario limits are visibly application-owned, not raw model truth guarantees. Broader
PR51 tuning remains unpromoted. This source has no VM reboot/full cold-start acceptance; full
context, thinking, general semantic quality and production acceptance remain open. Details and
exact hashes: [testing](en/TESTING.md); identity: [release manifest](status/current-release.yaml).

استقرار محدودِ تأییدشده، ۴ اکتبر ۲۰۲۶: برنامه و AI نسخهٔ `7ce9d29` با همان مدل35 صرفاً CPU
و استدلال خاموش، برای کاربران کنترل‌شده زنده‌اند. پنج کنترل CI، ۵۲۴ آزمون محلی، سه نصب تازهٔ
آفلاینِ هش‌قفل، ۴۵ مورد کارکردیِ مرورگر در مراحل نخست/آفلاین/بازگشت دقیق به69/نهایی، ۳۶ ممیزیِ
تکمیلِ بی‌متن، نه جفت هشِ زنده و پذیرش/ادامهٔ محدود صف موفق بودند. منع WAN/پراکسی چهار مهمان
و شروع واقعیِ دوبارهٔ برنامه، مدل و API با ورود، پاسخ تازه و شاهد شبکهٔ داخلی موفق بود؛ دو
بررسی نهاییِ رابط و بارگذاری دوبارهٔ پاسخ جایگزین نیز گذشتند. فقط محافظ‌های موقتِ همین آزمون
حذف شدند؛ نسخهٔ تغییرناپذیر69 باقی است. چهار نامزد ناموفق پیش از این اصلاح پذیرفته‌شده، دقیقاً
بازگردانده و حفظ شدند. محدودیتِ مثالِ فرضی آشکارا پاسخ برنامه است، نه تضمین حقیقتِ خام مدل.
تنظیم گستردهٔ PR51 مستقر نشده است. شروع دوبارهٔ VM و شروع کاملاً سردِ این کد پذیرفته نیست؛
زمینهٔ کامل، استدلال، کیفیت عمومیِ معنا و پذیرش تولید بازند. جزئیات و هش در [آزمون](fa/TESTING.md)
و هویت جاری در [رکورد انتشار](status/current-release.yaml) ثبت‌اند.

The following records are dated history; they do not override the verified identity above.
رکوردهای زیر سابقهٔ تاریخ‌دارند و هویت تأییدشدهٔ بالا را تغییر نمی‌دهند.

Thinking requalification, 2026-10-03 — standard app/AI `69c9260` are unchanged and live.
Eight installed-adapter short EN/FA requests completed, but Persian digit-only formatting failed.
A real 14,336-token input plus 2,048 output reservation failed at the fixed 120-second deadline;
native slot release was verified after cancellation, not inferred from wrapper counters. Fresh
standard EN/FA browser recovery, reload and two text-free audit checks passed. Source-only
b06bd30 hardens final JSON and improves four format cases; eight staged requests completed but
technical semantics still failed engineering review. Five-job CI, 467 local checks and 24 browser
fixtures passed for that source; it is not deployed or enabled-thinking acceptance. No runtime,
model, resources, service/profile/proxy/schema change was made. Both flags remain off. Matched
thinking app/history/audit/contention/offline gates remain unrun after failure. Raw private
evidence and earlier failures are retained. [Measured record](en/TESTING.md).

سنجش دوبارهٔ استدلال، ۳ اکتبر ۲۰۲۶ — برنامه و AI معمولیِ `69c9260` بدون تغییر زنده‌اند. هشت
درخواست کوتاهِ دوزبانهٔ لایهٔ نصب‌شده تکمیل شدند، اما قالبِ فقط رقم در فارسی شکست خورد. ورودیِ
واقعیِ ۱۴۳۳۶ توکن با ذخیرهٔ ۲۰۴۸ توکن خروجی در مهلت ثابتِ ۱۲۰ ثانیه پاسخ نهایی نداد؛ آزاد شدن
جایگاه مدل پس از لغو بررسی شد، نه از شمارندهٔ بیرونی استنباط. ادامهٔ پاسخ معمولیِ دوزبانه در
مرورگر تازه، بازکردن دوباره و دو ممیزیِ بدون متن موفق بودند. کدِ صرفاً مرحله‌ایِ b06bd30 قالب
نهاییِ JSON را سخت‌گیرانه‌تر و چهار قالب را بهتر کرد؛ هشت پاسخِ مرحله‌ای تکمیل شدند، ولی معنای
فنی بازبینی مهندسی را نگذرانده است. پنج کنترل CI، ۴۶۷ آزمون محلی و ۲۴ آزمون ساختگی مرورگرِ
آن کد موفق‌اند؛ نه استقرار و نه پذیرش استدلال فعال ادعا می‌شود. مدل، runtime، منابع، سرویس،
نمایه، پراکسی و پایگاه تغییر نکردند. هر دو گزینه خاموش‌اند؛ پس از شکست، معیار هماهنگِ برنامه،
سابقه، ممیزی، اشتغال و آفلاینِ استدلال اجرا نشده است. شاهد خصوصی و شکست قبلی حفظ‌اند.
[رکورد اندازه‌گیری](fa/TESTING.md).

The following checkpoints remain dated history, not a new serving identity.
گام‌های زیر با تاریخ خود حفظ‌اند، نه هویت تازهٔ نسخهٔ در حال خدمت.

Current verified repair, 2026-10-03 — app and AI API `69c9260` are live for controlled users.
The AI-server/Zabbix-host mismatch is repaired by bounded EN/FA approved-target selection,
audited mismatch rejection and a deterministic source-scoped host summary. The exact Persian
question now retrieves the actual AI server. Five-job CI, fresh offline installs, 459 local
unit/API/contract checks, 24 browser fixtures, seven final live functional cases, four final
text-free chat audits/three canonical live hashes and exact b5e74f9 rollback passed. Real bounded
four-request admission/queue recovery and actual over-16K token rejection passed; these are not
sustained load or full-context generation acceptance. OCS logo/palette, standard saved chat,
model/runtime/profile, proxy and schema are unchanged. Only owned transient guards were stopped.
The gated thinking adapter has a 128-token/final-envelope contract, but thinking remains off.
Native drafting/earlier failures and Persian identifier-only format failure are preserved.
Held-out semantics, near-full-context recall/latency and thinking acceptance remain open; no
new WAN/VM test was run for this source. Prior b5e74f9 infrastructure evidence below remains dated.
See [testing](en/TESTING.md) and [thinking specification](en/CONVERSATION_MEMORY_SPEC.md).

اصلاح تأییدشدهٔ جاری، ۳ اکتبر ۲۰۲۶ — برنامه و API هوش مصنوعیِ `69c9260` برای کاربران کنترل‌شده
زنده‌اند. عدم تطابق سرور AI و میزبان Zabbix با انتخاب محدود و دوزبانهٔ هدف مجاز، ردِ قابل‌ممیزیِ
عدم تطابق و خلاصهٔ قطعیِ محدود به منبع اصلاح شد؛ پرسش دقیقِ فارسی اکنون سرور واقعی AI را
بررسی می‌کند. پنج کنترل CI، نصب تازهٔ آفلاین، ۴۵۹ آزمون محلیِ واحد/API/قرارداد، ۲۴ آزمون ساختگی
مرورگر، هفت مورد کارکردیِ نهاییِ زنده، چهار ممیزیِ نهاییِ بدون متن/سه هشِ اصلی و بازگشت دقیق به
b5e74f9 موفق‌اند. پذیرش/ادامهٔ صف در آزمون واقعیِ چهار درخواست و ردِ ورودیِ واقعیِ بیش از 16K
موفق‌اند؛ این‌ها پذیرشِ بار پایدار یا تولید با ظرفیت کامل نیستند. نشان و رنگ OCS، گفت‌وگوی
معمولی، مدل، runtime، نمایه، پراکسی و پایگاه ثابت‌اند؛ فقط محافظ‌های موقتِ همین کار متوقف شدند.
قرارداد تازهٔ استدلال، بودجهٔ ۱۲۸ توکن و قالب نهایی دارد، ولی استدلال خاموش است. افشای پیش‌نویس،
شکست‌های پیشین و شکستِ قالبِ «فقط شناسه» در فارسی حفظ‌اند. درستیِ مستقل، یادآوری/تأخیرِ ظرفیت
کامل و پذیرشِ استدلال بازند؛ برای این نسخه آزمون تازهٔ WAN/VM اجرا نشد. شاهدِ زیرساختِ b5e74f9
در ادامه تاریخ‌دار می‌ماند. [آزمون](fa/TESTING.md) و [مشخصات استدلال](fa/CONVERSATION_MEMORY_SPEC.md)
را ببینید.

The following deployment records are historical, not the current release identity.
رکوردهای استقرارِ زیر تاریخی‌اند، نه هویتِ انتشار جاری.

Current verified deployment, 2026-09-30 — app and AI API b5e74f9 with the unchanged local CPU-only
35B model are live for controlled users. Standard owner-scoped saved conversations, reload/resume,
bounded follow-ups and the bilingual header light/dark switch are enabled. Context is configured
to 16,384 with actual local token admission; thinking failed and stays off at both APIs. Exact
five-job CI, fresh offline installs, staged Nginx validation, seven first/eight final live cases,
12 text-free chat audits, three live evidence/hash pairs, matched app/AI/proxy/profile rollback
with two fresh restored answers, four-guest WAN denial and actual serial guest reboots passed.
Fresh post-boot login, EN/FA generation and real Zabbix reboot-alert evidence passed under WAN
denial. The temporary network rules and only owned rollback timers were removed/disabled after
verification; protected fallback artifacts and additive schema remain. See [English](en/TESTING.md)
and [Persian](fa/TESTING.md) records. This is controlled live service, not full production acceptance.
Technical semantics/brevity, full-budget context quality/latency, admission contention, model
lineage and independent recovery remain unqualified; historical failures below are not erased.

استقرار جاریِ تأییدشده، ۹ مهر ۱۴۰۵ — برنامه و API هوش مصنوعیِ b5e74f9 با همان مدل محلیِ
35B صرفاً CPU برای کاربران کنترل‌شده زنده‌اند. سابقهٔ محلیِ مخصوص مالک، بازکردن و ادامه، پیگیری
محدود و انتخاب روشن/تیرهٔ دوزبانهٔ سربرگ فعال‌اند. زمینهٔ تنظیم‌شده ۱۶۳۸۴ با پذیرش واقعیِ
توکن محلی است؛ استدلال شکست خورده و در هر دو API غیرفعال است. پنج کنترل CI، نصب تازهٔ آفلاین،
نحو مرحله‌ایِ واقعی Nginx، هفت مورد نخست/هشت مورد نهاییِ زنده، دوازده ممیزیِ گفت‌وگوی بدون متن،
سه جفتِ شاهد/هش، بازگشت هماهنگ برنامه، AI، پراکسی و نمایه با دو پاسخ تازهٔ نسخهٔ بازگشته،
منع WAN چهار مهمان و راه‌اندازی دوبارهٔ واقعی و ترتیبی آن‌ها موفق‌اند. ورود تازه، تولید تازهٔ
دوزبانه و شاهد واقعیِ هشدار شروع دوبارهٔ Zabbix پس از boot، زیر منع WAN موفق بودند. پس از
تأیید، قانون موقت شبکه و فقط زمان‌سنج‌های متعلق به این تغییر حذف/غیرفعال شدند؛ نسخه‌های
محافظت‌شدهٔ بازگشت و پایگاه افزایشی باقی‌اند. جزئیات در [فارسی](fa/TESTING.md) و
[انگلیسی](en/TESTING.md) آمده است. این خدمت زندهٔ کنترل‌شده است، نه پذیرش کامل تولید. درستی
و اختصار، کیفیت و تأخیرِ ظرفیت کامل زمینه، اشتغال صف، منشأ مدل و بازیابی مستقل همچنان تأیید
نشده‌اند؛ شکست‌های تاریخیِ زیر حذف نشده‌اند.

Earlier dated checkpoints below are historical; current identity is the release manifest above.
گام‌های تاریخ‌دارِ زیر تاریخی‌اند؛ شناسهٔ جاری در رکورد انتشار ثبت شده است.

258ac65 guarded findings, 2026-09-30 — five-job CI and the real staged Nginx parser passed.
Thinking failed at the unchanged 120-second model deadline and remains disabled. Standard EN/FA
chat, reload and ticket recall ran, but the Persian current-status question using standalone
«الان» missed the deterministic scope redirect. It is fixed in the new candidate with explicit
personal-status checks and negative recall/guidance regressions; all prior results remain private
evidence, not release acceptance. A broad Persian DNS answer was also semantically rejected;
general factual accuracy remains partial. Exact app/AI/proxy/profile rollback restored 810102f/862d311.

یافته‌های آزمونِ محافظت‌شدهٔ 258ac65، ۹ مهر ۱۴۰۵ — پنج کنترل CI و مفسر واقعیِ مرحله‌ایِ Nginx
موفق بودند. استدلال در مهلت ثابتِ ۱۲۰ثانیه‌ای مدل شکست خورد و غیرفعال می‌ماند. گفت‌وگو،
بازکردن دوباره و یادآوری شناسه به دو زبان اجرا شدند؛ اما پرسشِ وضعیت فعلی با «الان» مستقل،
ارجاع قطعی به شاهد زنده را نگرفت. نامزد تازه این مورد و پرسشِ صریحِ وضعیت شخصی را با آزمون
مثبت و کنترل منفیِ یادآوری و راهنمایی اصلاح می‌کند. شاهدهای قبلی حفظ‌اند، نه پذیرش انتشار.
پاسخ عمومیِ فارسی دربارهٔ DNS نیز از نظر معنا رد شد؛ دقت عمومی همچنان ناقص است. بازگشت دقیقِ
برنامه، AI، پراکسی و نمایه، 810102f/862d311 را برگرداند.

Proxy syntax preflight, 2026-09-30 — 95f4de7 passed all five CI jobs in run 36711401339 and
fresh offline desktop/server installs. Nginx's real parser rejected the unquoted quantified route
before reload. The app/proxy rollback restored the untouched serving site; AI/profile was also
restored. No live answer, thinking or offline acceptance is claimed for this attempt. The next
candidate quotes the route and must pass a staged real-server parser check before any switching.

بررسی واقعیِ نحو پراکسی، ۹ مهر ۱۴۰۵ — 95f4de7 هر پنج کنترل CI در اجرای 36711401339 و نصب
آفلاین تازهٔ رایانه و سرورها را گذراند. مفسر واقعی Nginx، مسیر دارای شمارشگرِ بدون علامت نقل‌قول
را پیش از reload رد کرد. برنامه و پراکسی به سایت قبلیِ دست‌نخورده و AI و نمایه نیز به نسخهٔ
قبلی برگشتند. این تلاش، شاهد پاسخ زنده، استدلال یا پذیرش آفلاین نیست. نامزد بعدی مسیر را داخل
نقل‌قول می‌گذارد و پیش از تعویض باید بررسیِ مرحله‌ایِ مفسر واقعی سرور را بگذراند.

Guarded chat/theme trial, 2026-09-30 — c609a83 passed all five CI jobs in run 36707574912,
fresh hash-locked Ubuntu installation and both app/AI offline installs. Additive migration 0003
passed. Live English chat/reload/ticket recall and dark EN/FA mobile UI passed, but thinking hit
the generic Nginx 30-second timeout; the provider continued to its unchanged 120-second deadline
without a final answer. Exact app 810102f/AI 862d311/8192 profile rollback passed two fresh EN/FA
answers; additive tables remain. This is a failed qualification, not accepted thinking. A harness
TLS error exposed one test session in an error log; that exact session was revoked and audited.
The corrected candidate routes saved generation through the existing 180-second inference proxy
policy/rate limit and reduces private reasoning to 384 tokens, based on observed ~8 tokens/second.
The model deadline, queue, credentials and branding are unchanged; new matched acceptance is pending.

آزمون محافظت‌شدهٔ گفت‌وگو و پوسته، ۹ مهر ۱۴۰۵ — c609a83 هر پنج کنترل CI در اجرای
36707574912، نصب تازهٔ Ubuntu با هشِ قفل‌شده و نصب آفلاین روی برنامه و AI را گذراند؛ مهاجرت
افزایشی 0003 موفق بود. گفت‌وگوی انگلیسی، بازکردن دوباره و یادآوری شناسه، و رابط تیرهٔ دوزبانهٔ
موبایل موفق بودند؛ اما استدلال به مهلت عمومیِ ۳۰ثانیه‌ای Nginx رسید و مدل تا مهلت ثابتِ
۱۲۰ ثانیه، بدون پاسخ نهایی ادامه یافت. بازگشت دقیق به برنامهٔ 810102f، API نسخهٔ 862d311 و
زمینهٔ ۸۱۹۲، دو پاسخ تازهٔ فارسی/انگلیسی را گذراند؛ جدول‌های افزوده حفظ شدند. این آزمون ناموفق
است، نه پذیرش استدلال. خطای TLS ابزار آزمون، یک نشست آزمایشی را در گزارش خطا آشکار کرد؛ همان
نشست دقیقاً لغو و ممیزی شد. نامزد اصلاح‌شده مسیر تولیدِ ذخیره‌شده را به سیاستِ موجودِ ۱۸۰ثانیه‌ای
و محدودیت نرخِ استنتاج می‌برد و با اتکا به سرعت حدود هشت توکن در ثانیه، استدلال خصوصی را به
۳۸۴ توکن محدود می‌کند. مهلت مدل، صف، اطلاعات ورود و نشان ثابت‌اند؛ پذیرش تازه هنوز انجام نشده است.

Conversation/model expansion candidate, 2026-09-30 — owner-scoped local PostgreSQL chat,
six-pair/12000-character context, feature-gated thinking, exact-template token admission and
final-only storage are implemented on a separate branch. Flags remain off; the serving release
below is unchanged. Source b0fbfb3 passed all five CI jobs in run 36704531576, including PostgreSQL
16/17 and browser acceptance. The full isolated desktop suite passed 441 tests with two Windows
POSIX skips; the offline desktop package build passed. Read-only live runtime template/tokenization
succeeded for both trusted thinking settings; this is not a generation, quality, longer-context or
offline acceptance result.
Guest preflight observes 64 vCPUs, 193185 MiB usable RAM and one guest NUMA node; no additional resize
or guest topology change was performed. 122B split-artifact metadata is pinned for research only;
download, exact bytes/lineage, CPU performance and semantics are not verified.
See [the packet](en/CONVERSATION_MEMORY_SPEC.md) and [operations](en/CONVERSATIONS.md).

نامزد گسترش گفت‌وگو و مدل، ۹ مهر ۱۴۰۵ — حافظهٔ محلی و مالک‌محور PostgreSQL، زمینهٔ شش جفت و
۱۲ هزار نویسه، استدلال دروازه‌دار، پذیرش بر پایهٔ قالب واقعی و ذخیرهٔ صرفاً پاسخ نهایی در شاخهٔ
جدا پیاده شده‌اند. گزینه‌ها غیرفعال‌اند و نسخهٔ در حال خدمتِ زیر ثابت است.
کد b0fbfb3 هر پنج کنترل CI در اجرای 36704531576، از جمله PostgreSQL نسخه‌های ۱۶ و ۱۷ و
پذیرش مرورگر را گذراند. مجموعهٔ کاملِ ایزولهٔ رایانهٔ توسعه ۴۴۱ آزمون موفق و دو موردِ
POSIX اجرا‌نشده در Windows داشت؛ ساخت آفلاین بسته نیز موفق بود. قالب و توکن‌بندی
واقعی برای هر دو انتخابِ معتبر استدلال موفق بود؛ تولید پاسخ، کیفیت، زمینهٔ بزرگ‌تر یا پذیرش
آفلاین را ثابت نمی‌کند. مهمان اکنون ۶۴ vCPU، حافظهٔ قابل‌استفادهٔ ۱۹۳۱۸۵ MiB و یک گرهٔ NUMA
نشان می‌دهد؛ افزایش مجدد یا تغییر توپولوژی انجام نشد. رکورد دو فایل 122B صرفاً پژوهشی است؛
دریافت، بایت و منشأ دقیق، کارایی CPU و کیفیت هنوز تأیید نشده‌اند.
[مشخصات](fa/CONVERSATION_MEMORY_SPEC.md) و [راهنمای عملیات](fa/CONVERSATIONS.md) مبنا هستند.

Current controlled live workspace, 2026-09-30 — App/API 810102f is serving the unchanged
CPU-only 35B model. Five exact-head CI jobs, a fresh hash-locked offline Ubuntu 24.04 package
install, four first and two final authenticated EN/FA network/named-service browser cases, six
persisted audit/evidence-hash matches and exact app rollback to 862d311 with two fresh restored
answers passed. After re-promotion, wheel/installed-code identity, app/DB/Nginx units and zero
failed units passed; only this change's final rollback timer was stopped. Named-service answers
and the default focused panel show only the requested authorized unit, while canonical full
evidence remains available after explicit expansion. OCS branding and all AI, connector, model,
queue and resource limits are unchanged. Raw model generations can still hit 384 tokens; the
focused application-owned summary does not certify general AI accuracy. Prior semantic and 504
failures remain recorded. Exact-release server-WAN disconnection, VM cold start, independent
recovery and broad technical semantic acceptance remain open. This is live controlled user
testing, **not full production acceptance**.

محیط کنترل‌شدهٔ زنده، ۹ مهر ۱۴۰۵ — برنامه/API نسخهٔ 810102f همان مدل 35B صرفاً CPU را ارائه
می‌کند. پنج کنترل CI برای همین کد، نصب تازهٔ بستهٔ آفلاینِ Ubuntu 24.04 با هشِ قفل‌شده، چهار
مورد نخست و دو مورد نهاییِ مرورگرِ احرازهویت‌شدهٔ شبکه و سرویسِ نام‌برده به دو زبان، شش تطبیق
ممیزیِ ماندگار و هشِ شاهد، و بازگشت دقیقِ برنامه به 862d311 با دو پاسخ تازهٔ نسخهٔ بازگشته
موفق‌اند. پس از استقرار دوباره، شناسهٔ wheel و کد نصب‌شده، سرویس‌های برنامه/پایگاه/Nginx و
نبودِ سرویس ناموفق تأیید شد؛ فقط زمان‌سنجِ بازگشتِ همین تغییر متوقف شد. پاسخِ سرویسِ نام‌برده و
بخشِ متمرکزِ رابط فقط واحدِ مجازِ خواسته‌شده را نشان می‌دهند؛ شاهدِ اصلیِ کامل پس از گشودنِ
صریح در دسترس است. نشان OCS، AI، اتصال، مدل، صف و سقف منابع ثابت‌اند. تولید خامِ مدل ممکن است
هنوز به ۳۸۴ توکن برسد؛ خلاصهٔ متمرکزِ متعلق به برنامه، گواهیِ دقت عمومی AI نیست. شکست‌های
معنایی و ۵۰۴ پیشین ثبت‌اند. قطع WAN سرور، شروع سرد VM همین انتشار، بازیابی مستقل و پذیرشِ
گستردهٔ معناییِ فنی بازند. این، **آزمون زندهٔ کنترل‌شدهٔ کاربران** است، نه پذیرش کامل تولید.

Earlier candidate checkpoints below are historical, not the current serving identity.
گام‌های نامزدِ زیر تاریخی‌اند، نه شناسهٔ در حال خدمتِ کنونی.

Exact-unit repair candidate, 2026-09-30 — The 4d99c2c correction passed five CI jobs and a
fresh hash-locked Ubuntu 24.04 offline installation. Its first guarded live attempt returned a
504 before an answer; the restored 862d311 also returned 504 while the AI scheduler was busy.
A second guarded 4d99c2c attempt, serialized after idle, passed four fresh EN/FA network/service
browser requests, but semantic review rejected it: a named `nextops-app.service` question listed
unrequested PostgreSQL and Nginx units. It was immediately rolled back to healthy 862d311 and
its timer stopped. No durable audit or exact rollback answer pass is claimed for 4d99c2c. The
new source restricts named-unit answers, model prompt and focused UI to the exact observed unit;
an unknown unit stays unknown. Local 399 tests passed, eleven environment-dependent tests skipped,
fourteen browser fixtures passed, lint and typing passed. CI, exact offline package, live audit and
rollback for that then-new source were pending at this checkpoint. Serving was 862d311/35B,
not production accepted.

نامزدِ اصلاحِ واحدِ نام‌برده، ۹ مهر ۱۴۰۵ — اصلاح 4d99c2c پنج کنترل CI و نصب تازهٔ آفلاینِ
Ubuntu 24.04 با هشِ قفل‌شده را گذراند. نخستین آزمون زندهٔ محافظت‌شده پیش از پاسخ، خطای ۵۰۴ داد؛
نسخهٔ بازگشتهٔ 862d311 نیز هنگام اشتغالِ صف AI همین خطا را داد. آزمون دوم پس از خالی‌شدن صف،
چهار درخواست تازهٔ مرورگرِ شبکه و سرویس به فارسی و انگلیسی را گذراند؛ اما بازبینی معنایی آن را
رد کرد: پاسخِ پرسش دربارهٔ `nextops-app.service`، واحدهای درخواست‌نشدهٔ PostgreSQL و Nginx را
نیز آورد. برنامه فوراً به 862d311 سالم بازگشت و زمان‌سنجِ همان تغییر متوقف شد. ممیزی ماندگار یا
آزمونِ کاملِ پاسخ پس از بازگشت برای 4d99c2c ادعا نمی‌شود. کد تازه، پاسخ و ورودیِ مدل و بخشِ
متمرکزِ رابط را به واحدِ دقیقِ مشاهده‌شده محدود می‌کند و وضعیت واحدِ ناشناخته را نامعلوم می‌داند.
۳۹۹ آزمون محلی موفق، یازده آزمون وابسته به محیط کنارگذاشته‌شده، چهارده آزمون مرورگرِ ساختگی و
بررسی lint و نوع موفق بودند. CI، بستهٔ دقیق آفلاین، ممیزی زنده و بازگشتِ آن کد در این نقطه باز
بودند. انتشارِ در حال خدمت در این نقطه 862d311/35B بود و پذیرش تولید ادعا نمی‌شد.

Question-focused incident candidate, 2026-09-30 — A separate app-only source change makes
unambiguous network/service investigations show validated, application-owned Linux observations
first, with distinct Zabbix scope/time and canonical evidence/audit intact. Unrelated sections are
collapsed until explicitly opened. General answer limits, the 35B CPU model, runtime, connector,
credentials and branding are unchanged. Local focused API/browser checks passed; two Persian raw
model probes still truncated at 384 tokens. CI, exact offline packaging, live promotion, durable
audit and rollback for this candidate are not yet recorded. Serving remains 862d311/35B; this
does not make general technical advice or production accepted.

The first e2ea487 live trial was rejected on answer semantics: `0.0.0.0` gateway was phrased as
a hop and a resolver/route question received socket details. Exact app rollback restored healthy
862d311; fresh EN/FA general answers and logout passed. The corrected candidate is source-only
until its own CI, offline package and live gate pass. No complete first-trial browser/audit pass.

نامزدِ تمرکزِ بررسی رخداد، ۹ مهر ۱۴۰۵ — در تغییر جداگانهٔ کدِ برنامه، پرسش روشن دربارهٔ شبکه یا
سرویس ابتدا مشاهدهٔ اعتبارسنجی‌شدهٔ Linux را با زمان و دامنهٔ مستقل Zabbix نشان می‌دهد؛ شاهد اصلی
و ممیزی ثابت‌اند و بخش نامرتبط فقط با گشودنِ صریح دیده می‌شود. سقف پاسخ عمومی، مدل 35B صرفاً CPU،
محیط اجرا، اتصال، اعتبارنامه و نشان و رنگ تغییر نکرده‌اند. آزمون‌های محلیِ API و مرورگرِ متمرکز
موفق بودند؛ دو آزمایش خامِ فارسیِ مدل همچنان در سقف ۳۸۴ توکن قطع شدند. CI، بستهٔ دقیقِ آفلاین،
استقرار زنده، ممیزی ماندگار و بازگشت همین نامزد هنوز ثبت نشده‌اند. انتشارِ در حال خدمت 862d311
و 35B است؛ این نامزد نه مشاورهٔ عمومی را تأیید می‌کند و نه پذیرش تولید را.

نخستین آزمون زندهٔ e2ea487 به‌سبب بیانِ نادرستِ گیت‌وی `0.0.0.0` و نمایشِ سوکتِ درخواست‌نشده
رد شد. بازگشت دقیق، 862d311 سالم را برگرداند؛ دو پاسخ تازهٔ عمومیِ فارسی و انگلیسی و خروج
از نشست موفق بودند. نامزدِ اصلاح‌شده تا گذرِ CI، بستهٔ آفلاین و پذیرش زندهٔ مستقل فقط در کد
است. برای آزمون نخست، موفقیتِ کامل مرورگر یا ممیزی ادعا نمی‌شود.


Earlier controlled workspace, 2026-09-29 — app/API 862d311 served the unchanged CPU-only 35B model.
PR44 passed five CI jobs, exact fresh offline Ubuntu packaging, five first/four final live
browser/API cases, three durable audit/hash pairs and exact source rollback to b346c3e with fresh
EN/FA generation. Local checks: 363 unit/API passes, two Windows POSIX skips, twelve browser
fixtures. Only own guards were stopped after final success; protected package identities and
model selector match, units healthy and queue empty. The OCS logo/palette remain byte-identical.
The conversational UI, general-only bounded follow-ups, NOC/SOC guidance, technical RTL isolation
and named single-check blanket-health correction are live. See paired testing guides for exact
wheel/code identity and 11.1–73.4s request samples, not load percentiles. Advice remains model-only;
independent technical correctness is partial. Retained failures, exact-release server-WAN/VM
cold-start and production gates stay open. No training, retrieval or new device connector.

محیط کنترل‌شدهٔ پیشین، ۷ مهر ۱۴۰۵ — برنامه/API نسخهٔ 862d311 همان مدل 35B را صرفاً روی CPU
ارائه می‌کند. پنج کنترل CI در PR44، بستهٔ دقیق و تازهٔ آفلاین Ubuntu، پنج مورد نخست و چهار
مورد نهاییِ مرورگر/API، سه تطبیق ممیزی و هش و بازگشت دقیق کد به b346c3e با تولید تازهٔ دوزبانه
موفق‌اند. آزمون محلی: ۳۶۳ مورد واحد/API موفق، دو مورد POSIX در Windows کنارگذاشته‌شده و دوازده
مورد مرورگر با دادهٔ ساختگی. فقط زمان‌سنج‌های همین تغییر پس از موفقیت متوقف شدند؛ شناسهٔ بستهٔ
محافظت‌شده و انتخاب مدل درست، سرویس‌ها سالم و صف خالی است. بایت‌های نشان و رنگ‌های OCS ثابت‌اند.
رابط گفت‌وگو، زمینهٔ محدودِ صرفاً عمومی، راهنمای NOC و SOC، جداسازی جهت متن فنی و اصلاح محدودِ
نتیجه‌گیری سلامت از یک بررسی مستقرند. شناسهٔ دقیق بسته و کد و نمونه‌های ۱۱٫۱ تا ۷۳٫۴ ثانیه در
راهنمای آزمون آمده‌اند؛ این بازه صدک آزمون بار نیست. مشاوره صرفاً مدل و صحت فنیِ مستقل ناقص
است. شکست‌های ثبت‌شده و معیارهای WAN سرور، شروع سرد VM همین انتشار و تولید بازند. آموزش،
بازیابی سند یا اتصال تجهیز تازه اضافه نشده است.

Earlier dated checkpoints below are historical, not the current serving identity.
گام‌های تاریخ‌دار زیر تاریخی‌اند، نه شناسهٔ مستقر کنونی.

Latest completion follow-up, 2026-09-29 — PR42 passed five CI jobs and exact offline install;
another DNS sample hit 384 tokens and correctly fell back, so useful completion remains unaccepted.
95c6e50/35B is restored with two fresh EN/FA generation checks. A labeled clipboard-only fixture
proved Windows LF-to-CRLF conversion with otherwise identical content; failed reports remain.
The source-only provider now asks for at most three short points within a bilingual word budget,
without increasing tokens/time/queue or weakening safety. Qualify this exact source before keeping
the redesigned UI live. No model training or infrastructure change is introduced.

ادامهٔ تازهٔ کامل‌شدن پاسخ، ۷ مهر ۱۴۰۵ — پنج کنترل CI در PR42 و نصب دقیق آفلاین موفق شدند؛
نمونهٔ دیگرِ DNS به سقف ۳۸۴ توکن رسید و درست به پیام جایگزین رفت، اما پاسخ مفید پذیرفته نشد.
95c6e50 و 35B با دو تولید تازهٔ دوزبانه برگشتند. آزمون صریحاً ساختگیِ کپی، تبدیل LF به CRLF
در Windows و یکسان بودن باقی متن را ثابت کرد؛ گزارش شکست حفظ است. دستورِ محلیِ تولید، حداکثر
سه نکتهٔ کوتاه با سقف واژهٔ دوزبانه می‌خواهد، بدون افزایش توکن، زمان یا صف یا کاهش ایمنی. پیش از
نگه‌داشتن رابط تازه در محیط زنده، همین کد تأیید شود؛ آموزش مدل یا تغییر زیرساخت اضافه نشده است.

Latest source qualification follow-up, 2026-09-29 — PR41 passed all five CI jobs and exact fresh
offline Ubuntu packaging. The guarded 7ecd7ac app/API trial preserved 35B/CPU but rejected an overly
absolute DNS diagnostic conclusion. Browser/rollback-harness failures are retained separately,
not relabeled model success. Exact source rollback to 95c6e50/35B passed fresh EN/FA generation,
TLS, identity and logout; only own guards were stopped. The bounded source refinement requires
alternative causes, check-scope limits and command time bounds. Both locales now test exactly 6,000
serialized context plus 4,000 question characters. New locked CI/package/live semantic review is
next; the NOC/SOC UI is not yet accepted for live use. Earlier records remain historical.

تازه‌ترین ادامهٔ ارزیابی کد، ۷ مهر ۱۴۰۵ — پنج کنترل CI در PR41 و بستهٔ دقیقِ تازه و آفلاین
Ubuntu موفق شدند. آزمون محافظت‌شدهٔ برنامه/API نسخهٔ 7ecd7ac، مدل 35B و CPU را حفظ کرد، اما
نتیجه‌گیری بیش‌ازحد قطعیِ DNS پذیرفته نشد. شکست ابزار آزمون مرورگر و بازگشت، جدا حفظ شده‌اند
و موفقیت مدل نامیده نمی‌شوند. بازگشت دقیق به 95c6e50 و 35B، تولید تازهٔ فارسی و انگلیسی، TLS،
شناسه‌ها و خروج را گذراند؛ فقط زمان‌سنج‌های همین تغییر متوقف شدند. اصلاح محدودِ کد، علت‌های
جایگزین، محدودیت دامنهٔ بررسی و مهلت فرمان را الزام می‌کند. هر دو زبان با زمینهٔ JSON دقیقاً
شش هزار نویسه و پرسش کامل چهار هزار نویسه آزموده می‌شوند. CI و بسته و بازبینی معنایی تازه لازم
است؛ رابط NOC و SOC هنوز برای استفادهٔ زنده پذیرفته نیست. رکوردهای پیشین تاریخی‌اند.

Current source task, 2026-09-29 — The owner requests a conversational NOC/SOC frontend without
changing the OCS logo/palette. The bounded candidate adds twelve in-memory turns, safe text/code
rendering/copying, operator starters, two bounded untrusted general-context pairs and diagnostic
guidance without new connectors, credentials, dependencies or training. Live modes reject history
and retain fresh collection, scope, audit and deterministic safeguards. Local checks: 357 unit/API
passed, two Windows/POSIX skips; twelve real-browser fixtures passed. A first ambiguous starter
label and an early old-answer assertion were repaired without dropping checks. Fixtures are not
actual model semantics, exact-package deployment or WAN/VM acceptance. Serving app/API remains
95c6e50/35B; qualify the exact new source package and live EN/FA behavior before promotion. See
[the feature packet](requirements/NOC_SOC_WORKSPACE_SPEC.md). Earlier deployment evidence below
remains intact and does not automatically accept this candidate.

کار جاریِ کد، ۷ مهر ۱۴۰۵ — مالک بازطراحیِ گفت‌وگوی NOC و SOC را بدون تغییر نشان و رنگ‌های OCS
خواسته است. نامزد محدود، دوازده نوبت در حافظهٔ صفحه، نمایش و کپی ایمن متن و کد، شروع پرسش، دو
جفت زمینهٔ محدود و تأییدنشدهٔ عمومی و راهنمای تشخیص را اضافه می‌کند؛ اتصال، اطلاعات ورود، وابستگی
یا آموزش تازه ندارد. حالت‌های زنده سابقه را رد می‌کنند و گردآوری تازه، دامنه، ممیزی و کنترل قطعی
را حفظ می‌کنند. ۳۵۷ آزمون محلی واحد/API موفق و دو مورد Windows/POSIX اجرا‌نشده‌اند؛ دوازده آزمون
مرورگر واقعی با دادهٔ ساختگی موفق‌اند. ابهامِ نام یک دکمه و بررسیِ زودهنگام پاسخ قبلی، بدون حذف
کنترل اصلاح شدند. دادهٔ ساختگی، صحت مدل واقعی، استقرار بستهٔ دقیق یا پذیرش WAN و VM نیست.
95c6e50 و 35B مستقرند؛ پیش از ارتقا، بستهٔ دقیق و رفتار زندهٔ فارسی و انگلیسی آزموده شوند.
[مشخصات تغییر](requirements/NOC_SOC_WORKSPACE_SPEC.md) مبناست؛ شواهد پیشین حفظ‌اند و این نامزد
را خودکار نمی‌پذیرند.

Current controlled selection, 2026-09-29 — Qwen3.5-35B-A3B Q4_K_M is serving on the unchanged
CPU-only runtime with app/API 95c6e50, after PR39's five CI jobs and exact offline Ubuntu package
qualification. The corrected trial passed twelve fresh API and twelve strict browser cases,
EN/FA facts/arithmetic, canonical CPU-idle provenance, raw completion, RTL/LTR, local assets and
login/logout. Four bounded read-only database checks matched stored responses, scope, audit and
evidence hashes. Exact model and app/API rollback restored 8d1f1d2/8B with fresh EN/FA generation;
re-promotion passed six fresh final confirmations and four more read-only audit/hash checks. Keep the
first 35B Persian semantic failure and raw collection-time omissions: full bilingual/held-out
quality is partial. API sample latency was 12.7–93.6 seconds; process RSS observation about 35.4
GiB, not a sustained benchmark. No VM/runtime/resource/queue/deadline change; no GPU/cloud/
training. Original 8B/source rollback stays protected. Current-release server-WAN and full-VM
cold start are not run; production is not accepted. The dated checkpoints below are historical.

انتخاب کنترل‌شدهٔ جاری، ۷ مهر ۱۴۰۵ — Qwen3.5 با 35B-A3B و Q4_K_M، روی همان محیط CPU و با
برنامه/API نسخهٔ 95c6e50 مستقر است؛ پنج کنترل CI در PR39 و بستهٔ دقیقِ آفلاین Ubuntu تأیید
شدند. آزمون اصلاح‌شده، دوازده پرسش تازهٔ API و دوازده مورد سخت‌گیرانهٔ مرورگر، واقعیت و محاسبهٔ
دوزبانه، منشأ درستِ بیکاری پردازنده، تولید کامل، RTL/LTR، دارایی محلی و ورود و خروج را گذراند.
چهار بررسی محدود و فقط‌خواندنی پایگاه، پاسخ ذخیره‌شده، دامنه، ممیزی و هش شاهد را تطبیق دادند.
بازگشت دقیق مدل و برنامه/API، 8d1f1d2 و 8B را با تولید تازهٔ دوزبانه برگرداند؛ استقرار مجدد،
شش تأیید تازهٔ نهاییِ API و چهار تطبیق فقط‌خواندنیِ دیگرِ ممیزی و هش را گذراند. شکست معناییِ فارسی در آزمون
نخستِ 35B و حذف زمان گردآوری از متن خام حفظ شوند؛ کیفیت کامل دوزبانه و مستقل هنوز ناقص است.
تأخیر نمونه‌های API، ۱۲٫۷ تا ۹۳٫۶ ثانیه و مشاهدهٔ RSS حدود ۳۵٫۴ GiB بود، نه کارایی پایدار.
ماشین، محیط اجرا، منابع، صف و مهلت تغییر نکردند؛ GPU، ابر یا آموزش مدل اضافه نشد. مدل و کد
اصلی برای بازگشت محافظت‌شده‌اند. WAN سرور و شروع سردِ کامل VM همین انتشار اجرا نشده‌اند و
تولید پذیرفته نیست. گام‌های تاریخ‌دارِ زیر تاریخی‌اند.


Current continuation, 2026-09-29 — The exact 35B-A3B artifact was size/hash-verified on desktop and
AI host and protected; fourteen matched CPU samples completed in 13.5–64.5 seconds. Raw provenance
review remains partial (collection-time omissions). PR38 passed five CI jobs and exact fresh
Ubuntu offline packaging. The guarded bb81109/35B trial completed all twelve fresh API requests
with `stop`, correct code/model identity and logout 204, including both filesystem cases; Persian
CPU prose mislabeled the idle metric. It failed semantic review, not transport. Exact model and
app/API rollback restored 8d1f1d2/8B; fresh EN/FA generation, code identity and logout passed.
The bounded source-only repair owns CPU-idle meaning for unambiguous measurement-only requests,
without trusting free-form metric names. Malformed/missing/ambiguous values fail closed; full
evidence, timestamps, limitations and audit remain intact. Local unit/API: 327 passed, two POSIX
skips, sixteen integration/browser deselections. CI, packaging and fresh guarded requalification
of this repair remain next. No 35B selection or held-out/WAN/VM/production acceptance is claimed.
The dated checkpoints below preserve earlier observations, not current serving instructions.

ادامهٔ جاری، ۷ مهر ۱۴۰۵ — اندازه و هش فایل دقیقِ 35B-A3B در میزکار و میزبان AI تطبیق و فایل
محافظت شد؛ چهارده پرسش همسان CPU در ۱۳٫۵ تا ۶۴٫۵ ثانیه کامل شدند. بازبینی منشأ در متن خام،
به‌دلیل حذف زمان گردآوری، همچنان ناقص است. PR38 پنج کنترل CI و بسته‌بندی تازهٔ آفلاین Ubuntu
را گذراند. آزمون محافظت‌شدهٔ bb81109 و 35B، هر دوازده درخواست تازهٔ API، از جمله هر دو پرسش
فایل‌سیستم را با `stop`، شناسهٔ درست کد و مدل و خروج 204 کامل کرد؛ اما متن فارسی، سنجهٔ بیکاری
پردازنده را نادرست نام‌گذاری کرد. بازبینی معنایی ناموفق بود، نه ارتباط API. بازگشت دقیق مدل
و برنامه/API، 8d1f1d2 و 8B را برگرداند؛ تولید تازهٔ دوزبانه، هش کد و خروج تأیید شدند. اصلاح
محدود که هنوز فقط در کد است، معنای درصد بیکاری پردازنده را برای پرسشِ روشن و صرفاً اندازه‌گیری
در اختیار برنامه می‌گذارد، نه نام آزاد سنجه. مقدار نامعتبر، غایب یا مبهم پذیرفته نمی‌شود؛
شاهد کامل، زمان‌ها، قیدها و ممیزی حفظ‌اند. آزمون محلی واحد/API: ۳۲۷ موفق، دو مورد مختص POSIX
اجرانشده و شانزده مورد integration/browser خارج از انتخاب. CI، بسته‌بندی و بازآزمایی تازهٔ
این اصلاح گام بعدند؛ انتخاب 35B یا پذیرش مستقل، WAN، VM یا تولید ادعا نمی‌شود. گام‌های
تاریخ‌دارِ زیر، مشاهده‌های پیشین‌اند، نه دستور وضعیت مستقر امروز.

Source follow-up, 2026-09-29 — Qwen3.5 compatibility PR37 passed all five CI jobs and merged;
its exact wheel passed fresh Ubuntu offline-index installation and identity/mode/assets probes.
No serving selection followed. The source-only focused prompt now requests at most three short
sentences without enumerating every mount/field; it retains every focused observation, source/time,
partial marker and full authorized response/audit. Eight EN/FA API fixtures passed. Preserve
384-token/120-second limits, deterministic focus and all prior raw/browser failures; actual model
completion must be measured. 8d1f1d2/8B remains serving while Qwen3.5 provisioning continues.

پیگیری کد، ۷ مهر ۱۴۰۵ — پشتیبانی Qwen3.5 در PR37، هر پنج کنترل CI را گذراند و ادغام شد؛
wheel دقیق آن، نصب تازهٔ Ubuntu بدون فهرست اینترنتی و آزمون شناسه، حالت و فایل‌های رابط را
گذراند. مدل مستقر تغییر نکرد. دستور متمرکز، فقط در کد، حداکثر سه جملهٔ کوتاه بدون تکرار همهٔ
نقاط اتصال و فیلدها می‌خواهد؛ همهٔ مشاهده‌های مرتبط، منبع و زمان و قید ناقص‌بودن و پاسخ کاملِ
مجاز و ممیزی حفظ‌اند. هشت آزمون API دوزبانه موفق‌اند. سقف ۳۸۴ توکن و ۱۲۰ ثانیه، کنترل قطعی و
شکست‌های قبلیِ خام و مرورگر حفظ شوند؛ کامل‌شدن مدل واقعی باید سنجیده شود. تا آماده‌شدن
Qwen3.5، نسخهٔ 8d1f1d2 با 8B مستقر می‌ماند.

Current checkpoint, 2026-09-29 — The corrected 8d1f1d2/30B-A3B trial fixed answer direction but
rejected larger-model selection: incorrect Persian technical terminology and repeated raw
filesystem generation at the 384-token ceiling. Twelve API requests completed; eleven strict
browser cases passed before the final raw `length` failure. Four read-only database checks matched
durable runs/audit/scope/model/integrity and evidence hashes. Exact model/source rollback restored
fresh EN/FA generation. Only the verified RTL source repair was re-promoted as 8d1f1d2 with original
8B. Its twelve fresh API requests passed literal/code checks; strict browser again failed raw
Persian filesystem completion after eleven cases. A separate display-only check passed for the
complete application-owned focused answer; this is not a raw-model pass. Controlled testing,
not production acceptance, remains live. 35B-A3B Qwen3.5 artifact provisioning and source-only
non-thinking/identity compatibility are next; no serving selection, runtime/VM/dependency change
or held-out/WAN/VM-reboot acceptance is inferred.

گام جاری، ۷ مهر ۱۴۰۵ — آزمون اصلاح‌شدهٔ 8d1f1d2 و 30B-A3B جهت پاسخ را درست کرد، اما انتخاب
مدل بزرگ‌تر به‌دلیل اصطلاحات فنی نادرستِ فارسی و رسیدن مکرر تولید خامِ فایل‌سیستم به سقف ۳۸۴
توکن رد شد. دوازده درخواست API کامل شدند؛ مرورگر یازده مورد را گذراند و در مورد آخر، شرط
کامل‌شدن متن خام با `length` شکست خورد. چهار بررسی فقط‌خواندنی پایگاه، اجرای ماندگار، ممیزی،
دامنه، مدل، قیدهای صحت و هش شاهد را تطبیق دادند. بازگشت دقیق مدل و کد، تولید تازهٔ فارسی و
انگلیسی را برگرداند. فقط اصلاح آزموده‌شدهٔ جهت پاسخ در 8d1f1d2، با مدل اصلی 8B دوباره مستقر
شد. دوازده پرسش تازهٔ آن، بررسی لفظی و هش را گذراندند؛ مرورگر پس از یازده مورد، همان ناتمامی
خامِ فارسی را ثبت کرد. آزمون مستقلِ نمایش، پاسخ کامل و متمرکزِ ساخته‌شده توسط برنامه را تأیید
کرد؛ این موفقیتِ متن خام مدل نیست. آزمون کنترل‌شده زنده است، نه پذیرش تولید. آماده‌سازی فایل
Qwen3.5 با 35B-A3B و پشتیبانیِ شناسه و حالت بدون تفکر فقط در کد، گام بعد است؛ انتخاب زنده،
تغییر محیط اجرا یا VM یا وابستگی و پذیرش کیفیت مستقل، WAN یا reboot نتیجه گرفته نشود.

Earlier trial checkpoint, 2026-09-29 — 30B-A3B import passed; fourteen matched CPU responses
completed in 1.3–23.7 seconds. Raw source/collection/partial qualifiers and Persian terminology
remain partial. Replaying actual outputs through unchanged assurance preserved typed evidence and
replaced both partial responses. A timed 3deba0d/30B-A3B trial returned twelve HTTP 200 responses
with matching model/code identity. The failed Persian-source literal check expected «زبیکس»
instead of displayed `Zabbix`; its report is retained. Browser review stopped after three cases;
a fresh probe confirmed a Persian answer beginning `SSD` rendered LTR. Exact model and source
rollback restored c4351fd/8B with fresh EN/FA generation. The response-locale fix passed seven
isolated browser fixtures, not a new deployment. Requalification is next; raw outputs stay private
and production, held-out, WAN and VM reboot gates are not inferred.

گام پیشینِ آزمون، ۷ مهر ۱۴۰۵ — ورودِ 30B-A3B تأیید و چهارده پاسخ همسانِ CPU در ۱٫۳ تا ۲۳٫۷
ثانیه کامل شدند. منبع، زمان گردآوری و قید ناقص‌بودن در متن مدل و اصطلاحات فارسی هنوز کاملاً
پذیرفته نیستند. بازپخش خروجی واقعی با کنترل قطعیِ بدون تغییر، شاهد نوع‌دار را حفظ و هر دو پاسخ
شاهد ناقص را جایگزین کرد. آزمون موقتِ 3deba0d و 30B-A3B دوازده پاسخ HTTP 200 با شناسهٔ درست
مدل و هش کد داشت. بررسی لفظیِ ناموفقِ منبع فارسی، «زبیکس» را به‌جای `Zabbix` نمایش‌داده‌شده
انتظار داشت؛ گزارش آن حفظ شده است. مرورگر پس از سه مورد متوقف شد و آزمون تازه تأیید کرد پاسخ
فارسی با `SSD` در ابتدا، اشتباه LTR است. بازگشت دقیق مدل و کد، c4351fd و 8B را با تولید تازهٔ
فارسی و انگلیسی برگرداند. اصلاح جهت بر پایهٔ زبان پاسخ، هفت آزمون ایزولهٔ مرورگر را گذرانده
است، نه استقرار تازه. بازآزمایی گام بعدی است؛ خروجی خام خصوصی می‌ماند و پذیرش تولید، کیفیت
مستقل، قطع WAN یا reboot نتیجه گرفته نشود.

Earlier larger-model checkpoint, 2026-09-29 — The pinned 32B desktop/server import passed. Eleven
same-budget answers completed in 9.9–97.6 seconds, including correct RAM/arithmetic and English
stale qualifiers; Persian stale evidence exceeded the 120-second deadline. Testing stopped before
injection cases; latency failed, semantic review remains partial, and 32B was not selected. Its
temporary unit stopped; c4351fd/8B remains live. Official pinned 30B-A3B provisioning and explicit
source compatibility are next. Its 30.5B total/3.3B active parameters motivate measurement, not
an accuracy/speed claim. Preserve the existing runtime, resources, policy, audit and rollback.

گام پیشینِ مدل بزرگ‌تر، ۷ مهر ۱۴۰۵ — ورودِ تثبیت‌شدهٔ 32B در میزکار و سرور تأیید شد. یازده پاسخ
با همان سقف، در ۹٫۹ تا ۹۷٫۶ ثانیه کامل شدند؛ RAM، محاسبه و قید شاهد قدیمیِ انگلیسی درست بودند.
پرسش فارسیِ شاهد قدیمی از مهلت ۱۲۰ ثانیه گذشت و آزمون پیش از موارد تزریق متوقف شد. تأخیر
ناموفق و بازبینی معنایی ناقص است؛ 32B انتخاب نشد و سرویس موقت متوقف شد. c4351fd/8B زنده ماند.
آماده‌سازی 30B-A3B رسمی و پشتیبانی صریحِ شناسه در کد، گام بعدی است. ۳۰٫۵ میلیارد پارامتر کل و
۳٫۳ میلیارد پارامتر فعال، دلیل اندازه‌گیری‌اند، نه ادعای درستی یا سرعت. محیط اجرا، منابع، سیاست،
ممیزی و امکان بازگشت حفظ شوند.

Earlier larger-model checkpoint, 2026-09-29 — Fourteen matched bilingual cases per model completed with
the corrected app prompts at 384 tokens. Semantic review rejected 14B: incorrect Persian RAM and
50/200 arithmetic, plus source/time/stale omissions. Baseline 8B also failed some stale/source
cases. Serving c4351fd/8B and its safeguards remain unchanged. Official 32B Q4_K_M is pinned and
being provisioned; source-only identity support and protected selection profiles are development
aids, not deployment or acceptance. No runtime, dependency, VM, database or connector change ran.

گام پیشینِ مدل بزرگ‌تر، ۷ مهر ۱۴۰۵ — چهارده موردِ همسان دوزبانه برای هر مدل، با دستورهای اصلاح‌شدهٔ
برنامه و سقف ۳۸۴ توکن کامل شدند. بازبینی معنایی، 14B را به‌دلیل پاسخ نادرستِ فارسی دربارهٔ RAM
و محاسبهٔ ۵۰ تقسیم بر ۲۰۰ و حذفِ منبع، زمان یا قید شاهد قدیمی رد کرد. 8B نیز بعضی مواردِ منبع
و شاهد قدیمی را نگذرانده است. انتشار مستقر c4351fd/8B و کنترل‌های آن تغییر نکرده‌اند. مدل رسمیِ
32B با Q4_K_M تثبیت و در حال آماده‌سازی است؛ شناسه و پروفایل انتخاب فقط در کد، ابزار توسعه‌اند،
نه استقرار یا پذیرش. محیط اجرا، وابستگی، ماشین، پایگاه و اتصال‌دهنده تغییر نکردند.

Earlier live clarity checkpoint, 2026-09-29 — Application and inference API now serve
`nextops-0.1.0-c4351fd` after PR #32 and all five hosted CI jobs passed. Twelve fresh bilingual API
cases passed with matching code digest and logout; the four known focus/scope failures are fixed.
Five general browser cases and a separate two-case filesystem context passed their respective
checks after correcting harness assumptions. Exact app/API rollback restored fresh generation
and the same candidate was re-promoted. Held-out semantics remain partial; exact-release server
WAN isolation and VM cold start have not run. Connector, database and pinned 8B runtime/model
remain unchanged. The 14B model is imported and compared, not selected or production-qualified.
The retired private questionnaire and its prerequisite procedure remain removed.

گام زندهٔ وضوح، ۷ مهر ۱۴۰۵ — برنامه و API استنتاج پس از PR شمارهٔ ۳۲ و موفقیت هر پنج کار CI،
اکنون `nextops-0.1.0-c4351fd` را ارائه می‌کنند. دوازده پرسش تازهٔ دوزبانه با هش درست و خروج
موفق، چهار شکستِ قبلیِ تمرکز و دامنه را رفع کردند. پنج مورد عمومیِ مرورگر و دو مورد فایل‌سیستم
در محیط تازهٔ جدا، پس از اصلاح فرض‌های ابزار آزمون، کنترل‌های مربوط را گذراندند. بازگشتِ دقیق
برنامه/API تولید تازه را برگرداند و همان نامزد دوباره مستقر شد. معیار معناییِ کنارگذاشته‌شده
ناقص است؛ قطع WAN سمت سرور و شروع سرد ماشینِ همین انتشار اجرا نشده‌اند. اتصال‌دهنده، پایگاه،
محیط اجرا و مدل تثبیت‌شدهٔ 8B تغییر نکرده‌اند. مدل 14B وارد و مقایسه شده، نه منتخب یا پذیرفتهٔ
تولید. فرم خصوصیِ کنارگذاشته‌شده و روندِ پیش‌شرط آن حذف‌شده باقی می‌مانند.

Earlier correction checkpoint / گام قبلیِ اصلاح:

Clarity HTTP correction, 2026-09-29 — The first `089e3ad` promotion failed fresh generation:
the inference HTTP schema rejected the gateway's new purpose field. The application and then
inference API were rolled back successfully; all six old-release requests returned 200, while
the four known focus/scope expectations still failed. A corrected authenticated schema and
complete gateway/HTTP/scheduler/provider regression now pass. The desktop suite has 257 passes
and two POSIX-only skips. The 14B artifact import passed, but its bounded bilingual quality
comparison failed and resource comparison is partial; it is not the selected model. The next
step is guarded promotion of the rebuilt correction, not another owner questionnaire.

اصلاح مرز HTTP، ۷ مهر ۱۴۰۵ — نخستین استقرار `089e3ad` در تولید تازه شکست خورد: طرح‌وارهٔ HTTP
استنتاج، فیلد جدیدِ نوع پردازش درگاه را نمی‌پذیرفت. ابتدا برنامه و سپس API استنتاج با موفقیت
برگشتند؛ هر شش درخواست نسخهٔ قبلی پاسخ 200 گرفت، ولی چهار انتظارِ شناخته‌شدهٔ تمرکز و دامنه
همچنان شکست خورد. طرح‌وارهٔ احرازهویت‌شده و آزمون کامل درگاه/HTTP/زمان‌بند/مدل اکنون موفق‌اند.
مجموعهٔ میزکار ۲۵۷ موفقیت و دو موردِ اجرا‌نشدهٔ مختص POSIX دارد. ورود فایل 14B موفق است، اما
مقایسهٔ محدود کیفیت دوزبانه شکست خورده و مقایسهٔ منابع ناقص است؛ این مدل انتخاب نشده است.
گام بعد، استقرار محافظت‌شدهٔ بستهٔ اصلاح‌شده است، نه فرم تازهٔ مالک.

Earlier source checkpoint / گام پیشینِ کد:

AI clarity development, 2026-09-29 — The owner retired the all-at-once decision form; it is no
longer a development prerequisite. The active private copy was moved to a recoverable retired
copy. The candidate separates general/evidence synthesis, retains full accepted question tails,
and raises the UI/application output cap to 384 without increasing concurrency. An eight-case
serial CPU loopback probe using candidate provider code returned complete 8B answers in both
languages, but Persian wording and an omitted evidence-source label still need improvement.
This is bounded synthetic generation, not a serving-app or production pass. A separately pinned
official 14B Q4_K_M candidate is being provisioned and compared; the serving 8B and rollback remain
unchanged. Existing failed/not-run release gates are preserved.

توسعهٔ وضوح پاسخ، ۷ مهر ۱۴۰۵ — مالک فرمِ یک‌جای تصمیم‌ها را کنار گذاشت؛ تکمیل آن دیگر پیش‌شرط
توسعه نیست. نسخهٔ فعال خصوصی به نسخهٔ کنارگذاشته‌شده و قابل‌بازیابی منتقل شد. نامزد، دستور
پرسش عمومی و خلاصه‌سازی شاهد را جدا می‌کند، پایان کامل پرسش را حفظ می‌کند و سقف پاسخ رابط و
برنامه را بدون افزایش هم‌زمانی به ۳۸۴ توکن می‌رساند. هشت پرسش ساختگیِ متوالی با کد نامزد روی
مدل CPU فعلیِ 8B، در هر دو زبان پاسخ کامل گرفتند؛ بااین‌حال، عبارت فارسی و حذف نام منبعِ شاهد
هنوز نیازمند بهبود است. این تولید محدود و ساختگی، پذیرش مسیر برنامهٔ مستقر یا تولید نیست.
مدل رسمیِ 14B با Q4_K_M و رکورد مستقل در حال آماده‌سازی و مقایسه است؛ مدل مستقر 8B و امکان
بازگشت آن تغییر نکرده‌اند. معیارهای ناموفق و اجرا‌نشدهٔ انتشار حفظ شده‌اند.

Repository enforcement audit, 2026-09-28 — At `de52e43`, GitHub's read-only branch metadata
reported `main` unprotected and required status checks off; the repository/inherited ruleset
list was empty. All five check runs succeeded from GitHub Actions app `15368`, but are not
required for merge. The paired development guide and blocker runbook now specify the owner
handoff. No administration setting or serving host changed; release-integrity review stays partial.

ممیزی الزامِ ادغام در مخزن، ۶ مهر ۱۴۰۵ — در `de52e43`، دادهٔ فقط‌خواندنی GitHub، شاخهٔ `main`
را بدون حفاظت و الزام کنترل وضعیت را غیرفعال نشان داد؛ فهرست rulesetهای مخزن و قواعد
به‌ارث‌رسیده خالی بود. هر پنج کنترل از GitHub Actions با شناسهٔ `15368` موفق‌اند، ولی شرط ادغام
نیستند. راهنمای توسعهٔ دوزبانه و راهنمای موانع اکنون اقدام لازمِ مالک را مشخص می‌کنند. تنظیم
مدیریتی یا سروری تغییر نکرد؛ بازبینی یکپارچگی انتشار همچنان ناقص است.

Merged greeting candidate, 2026-09-28 — PR #28 passed all five hosted CI jobs and merged at
`b868e3e`. A new unsigned wheel built without a package index matched its whole-file hash between
Windows and Ubuntu. Its code digest matched the source tree, wheel and fresh Ubuntu 24.04.5
installation. Hash-locked dependencies, `pip check`, API/native imports and ten synthetic
installed-answer checks passed. No live model generation, serving-host operation, WAN isolation
or production gate ran; the serving application's failed semantic gate is unchanged.

نامزد ادغام‌شدهٔ اصلاح سلام، ۶ مهر ۱۴۰۵ — هر پنج کار CI در PR شمارهٔ ۲۸ موفق شد و تغییر در
`b868e3e` ادغام شد. wheel تازه و بدون امضا، بی‌نیاز از فهرست بسته‌ها ساخته شد و هش کل فایل
در Windows و Ubuntu یکسان بود. هش کد نیز میان درخت منبع، wheel و نصب تازهٔ Ubuntu 24.04.5
تطبیق داشت. نصب وابستگی‌های دارای هش، `pip check`، واردکردن API و ماژول‌های بومی و ده آزمون
ساختگیِ پاسخ در بستهٔ نصب‌شده موفق بود. تولید زندهٔ مدل، عملیات سرور، قطع WAN یا معیار تولید
اجرا نشد؛ شکست معیار معناییِ برنامهٔ مستقر تغییری ندارد.

Greeting relevance source guard, 2026-09-27 — The undeployed application source now replaces an
unrelated model response to a greeting-only English/Persian general question with a short localized
greeting. A relevant short model greeting is retained, and the browser fallback notice no longer
suggests that general mode retrieved live evidence. API and local browser fixtures pass. This does not
qualify arbitrary answer relevance or truth, change the serving application's failed semantic
gate, or authorize deployment.

کنترل ارتباطِ پاسخ به سلام، ۵ مهر ۱۴۰۵ — کدِ هنوز مستقرنشدهٔ برنامه، پاسخ نامرتبط مدل به پرسش
عمومیِ محدود به سلام را در فارسی و انگلیسی با سلامی کوتاه و متناسب جایگزین می‌کند. سلام کوتاه و
مرتبطِ خود مدل حفظ می‌شود و اعلانِ پاسخ جایگزین در رابط، دریافت شاهد زنده را القا نمی‌کند.
آزمون‌های API و مرورگرِ محلی با دادهٔ آزمایشی موفق‌اند. این کنترل، درستی یا ارتباط همهٔ پاسخ‌ها را
تأیید نمی‌کند، شکست معیار معناییِ برنامهٔ مستقر را تغییر نمی‌دهد و مجوز استقرار نیست.

Ubuntu candidate qualification, 2026-09-27 — From merged `main` commit `d973785`, an unsigned
`nextops-0.1.0-d973785` candidate wheel was built without a package index. PowerShell and Ubuntu
agreed on its whole-wheel SHA-256; the wheel and its fresh Ubuntu 24.04.5 installation produced
the same application-code digest. The unchanged 25-wheel Linux set revalidated against `uv.lock`
and a fresh WSL2 Python 3.12.3 venv installed its 24 applicable packages with `--no-index` and
`--require-hashes`; the app wheel installed with `--no-index --no-deps`. `pip check` and API/native
imports passed. The detailed record and artifacts are private. WAN was not disconnected, and no
serving host, database, model, browser answer, rollback or production gate was tested. The current
serving application's failed semantic gate and all other release statuses are unchanged.

صلاحیت‌سنجی نامزد در Ubuntu، ۵ مهر ۱۴۰۵ — از commit ادغام‌شدهٔ `d973785` در شاخهٔ اصلی، wheel
نامزدِ بدون امضای `nextops-0.1.0-d973785` بی‌نیاز از فهرست بسته‌ها ساخته شد. هش SHA-256 کل
wheel در Windows و Ubuntu یکسان بود و هش کدِ برنامه نیز میان wheel و نصب تازهٔ Ubuntu 24.04.5
تطبیق داشت. مجموعهٔ تغییرنیافتهٔ ۲۵ wheel لینوکسی دوباره با `uv.lock` سنجیده شد؛ ۲۴ بستهٔ
قابل‌اعمال در محیط تازهٔ Python 3.12.3 روی WSL2 با `--no-index` و `--require-hashes`، و wheel
برنامه با `--no-index --no-deps` نصب شدند. `pip check` و واردکردن API و ماژول‌های بومی موفق
بود. رکورد و فایل‌ها خصوصی‌اند. WAN قطع نشده و هیچ سرورِ در حال خدمت، پایگاه داده، مدل، پاسخ
مرورگر، بازگشت یا معیار تولید آزموده نشده است. شکستِ معیار معناییِ برنامهٔ مستقر و دیگر وضعیت‌های
انتشار تغییری ندارند.

Answer-code correlation, 2026-09-27 — Source-only application code now computes a bounded
SHA-256 over its installed NextOps package source and local UI assets at startup and places it on
successful authenticated answer responses. The private semantic-capture tool requires a matching
expected digest, which can be derived offline from a separately hash-verified wheel. Focused
API, wheel/tree-equivalence and mismatch tests pass; an offline desktop wheel matched the source
tree. This is not an artifact signature, full release/host attestation, live run, semantic pass or
change to the failed serving-release gate. The app candidate must be rebuilt and deployed under
the approved guard before this correlation can be observed on a serving host.

هم‌بستگی کدِ پاسخ، ۵ مهر ۱۴۰۵ — در کدِ هنوز مستقرنشده، هنگام آغاز برنامه هش SHA-256 محدود از
کد بستهٔ نصب‌شدهٔ NextOps و فایل‌های محلیِ رابط محاسبه و به پاسخ موفقِ احرازهویت‌شده افزوده می‌شود.
ابزار خصوصیِ گردآوری پاسخ، هش مورد انتظارِ به‌دست‌آمده از wheel جداگانه تأییدشده را می‌سنجد.
آزمون‌های متمرکز API، برابریِ wheel و درخت کد، و ناسازگاری هش موفق‌اند؛ wheel آفلاینِ میزکار نیز
با درخت کد یکسان بود. این نه امضای انتشار یا گواهِ کاملِ نسخه و میزبان است، نه آزمون زنده یا
موفقیت معنایی؛ شکست معیار برنامهٔ مستقر تغییر نمی‌کند. نامزد باید پس از ساخت دوباره، تنها در
پنجرهٔ مصوب و با محافظ بازگشت مستقر شود تا این هم‌بستگی روی سرور دیده شود.

Semantic capture guard, 2026-09-27 — Source-only live-review tooling now exits nonzero when any
case lacks an automatic expectation or an answer merely echoes a longer question, while retaining
the private report and logout attempt. Focused boundary tests pass. This does not rerun the serving
endpoint, verify its release identity, judge answer truth or change the failed current-app semantic
gate. The corrected application candidate remains undeployed.

کنترل گردآوری پاسخ، ۵ مهر ۱۴۰۵ — ابزارِ فقط‌درکدِ بازبینی زنده اکنون اگر حتی یک پرسش انتظارِ
خودکار نداشته باشد یا پاسخ بلند فقط همان پرسش را تکرار کند، با خطا پایان می‌یابد؛ گزارش خصوصی و
تلاش برای خروج از نشست همچنان حفظ می‌شوند. آزمون‌های مرزیِ متمرکز موفق‌اند. این تغییر مسیرِ زندهٔ
برنامه را دوباره نمی‌آزماید، شناسهٔ انتشار یا درستی پاسخ را اثبات نمی‌کند و شکست معیار معناییِ
انتشار جاری را تغییر نمی‌دهد. برنامهٔ اصلاح‌شده هنوز مستقر نشده است.

Runtime SBOM evidence, 2026-09-27 — A source-only offline checker now verifies each staged
Python wheel's filename, package identity and SHA-256 against `uv.lock`, requires a bundled
license file and reviewable wheel `METADATA` declaration, and matches wheels one-to-one with
CycloneDX 1.5 components. It produced a private derived SBOM with hashes and source-labeled
license declarations for all 25 staged wheels; the derived file passed the CycloneDX 1.5 JSON
schema. Nine boundary tests passed. This resolves the missing license *fields* in that private
SBOM, not the company project-license choice, third-party legal approval, vulnerability review,
artifact signing, serving-host release identity or production acceptance.

شاهد مجوز در SBOM اجرا، ۵ مهر ۱۴۰۵ — ابزار آفلاینِ تازه در کد، نام و هویت و هش SHA-256 هر
wheel پایتون را با `uv.lock` می‌سنجد، وجود متن مجوز و اظهار آن در `METADATA` بسته را
الزامی می‌داند و هر wheel را به یک جزء CycloneDX 1.5 پیوند می‌دهد. SBOM مشتق‌شدهٔ
خصوصی برای هر ۲۵ بسته، هش و مجوزِ اعلام‌شده همراه با منبع آن را ثبت کرد و اعتبارسنجی
طرح‌وارهٔ CycloneDX 1.5 نیز موفق بود. نُه آزمون مرزی گذشت. این کار فقط جای خالیِ
دادهٔ مجوز در آن SBOM خصوصی را برطرف می‌کند؛ انتخاب مجوز خودِ پروژه، تأیید حقوقی
وابستگی‌ها، بررسی آسیب‌پذیری، امضای فایل، شناسهٔ انتشار مستقر و پذیرش تولید همچنان بازند.

Ubuntu lab qualification, 2026-09-27 — After the failed WSL network-install routes recorded
below, a Canonical Ubuntu 24.04.5 WSL image was downloaded over HTTPS, matched its published
SHA-256, and installed as an isolated desktop WSL2 distro. Python 3.12.3 in a fresh virtualenv
installed the pinned Linux requirements from the private wheelhouse using `--no-index`,
`--require-hashes` and binary-only resolution; the application candidate wheel installed
without an index. `pip check` and imports of the API and native dependencies passed. The
minimal image needed a separately hash-verified, lab-only pip bootstrap wheel. This closes the
desktop Ubuntu package-install/import check, **not** server WAN isolation, service behavior,
live answer quality, release integrity, rollback, or production acceptance. The serving hosts
and release manifest are unchanged.

احراز بسته در آزمایشگاه Ubuntu، ۵ مهر ۱۴۰۵ — پس از شکست روش‌های دریافتِ WSL که در بند
بعد ثبت شده‌اند، تصویر Ubuntu 24.04.5 از وبگاه رسمی Canonical دریافت شد؛ هش SHA-256 آن با
مقدار منتشرشده یکسان بود و در محیط جداگانهٔ WSL2 روی میزکار نصب شد. پایتون ۳٫۱۲٫۳ در
محیط مجازی تازه، وابستگی‌های قفل‌شدهٔ Linux را فقط از wheelhouse خصوصی، با
`--no-index`، `--require-hashes` و محدودیت بستهٔ باینری نصب کرد؛ wheel نامزدِ برنامه
نیز بدون فهرست بسته‌ها نصب شد. `pip check` و واردکردن API و وابستگی‌های بومی موفق بودند.
این تصویر کمینه برای آماده‌سازی آزمایشگاه به wheel جداگانه و کنترل‌شدهٔ pip نیاز داشت.
نتیجه فقط نصب و واردکردن بسته روی Ubuntu میزکار را تأیید می‌کند، نه قطع WAN سمت سرور،
کارکرد سرویس، کیفیت پاسخ زنده، تمامیت انتشار، بازگشت یا پذیرش تولید. سرورهای در حال خدمت
و مانیفست انتشار تغییری نکرده‌اند.

Desktop qualification follow-up, 2026-09-27 — Both standard and web-download attempts to install
Ubuntu 24.04 under WSL2 failed before installation with `Wsl/InstallDistro/0x80072f78`; no Linux
runtime test occurred. The Docker client has no reachable local daemon. Private inspection of the
25 staged Linux wheels found a license declaration and bundled license file in every wheel,
including two declaring `LGPL-3.0-only`. This is upstream metadata, not a legal review: the
CycloneDX export still has no license entries, the repository has no approved project license,
and the named legal/security decision is absent. Serving release, acceptance gates and host state
are unchanged.

پیگیریِ آزمون میزکار، ۵ مهر ۱۴۰۵ — نصب Ubuntu 24.04 در WSL2، هم از مسیر معمول و هم از مسیر
دریافت مستقیم، پیش از نصب با خطای `Wsl/InstallDistro/0x80072f78` متوقف شد؛ پس هیچ آزمونی در
محیط Linux انجام نشد. ابزار Docker نیز به سرویس محلیِ آن دسترسی ندارد. بررسی خصوصیِ ۲۵
wheel لینوکس نشان داد همهٔ آن‌ها اظهارنامه و فایل مجوز دارند و مجوز دو بسته
`LGPL-3.0-only` است. این‌ها صرفاً داده‌های منتشرکنندگان بسته‌اند، نه بازبینی حقوقی:
SBOM تولیدشده هنوز اطلاعات مجوز ندارد، مجوز مصوبِ خود پروژه در مخزن ثبت نشده و تصمیم
مسئولان حقوقی و امنیتی نیز ارائه نشده است. انتشار در حال خدمت، معیارهای پذیرش و وضعیت
سرورها تغییری نکرده‌اند.

Provisioning-only dependency checkpoint, 2026-09-27 — The unchanged production lock exported
hash-pinned requirements and a private CycloneDX 1.5 SBOM with 25 components; the SBOM contains no
license entries. Twenty-five Linux-targeted wheels matched their `uv.lock` hashes and resolved
again with the package index disabled. A separate 25-wheel Windows set installed with hash checks
into a fresh Python 3.12 virtualenv alongside the source-matched application wheel; `pip check`,
API imports and the bundled UI asset passed offline. WSL2 has no installed Linux distribution, so
an actual Ubuntu offline install is **not run**. No serving host changed, and license, signing,
live answer quality and production acceptance remain open. The earlier desktop-cache failure below
preceded this deliberate wheelhouse staging.

گام آماده‌سازیِ وابستگی، ۵ مهر ۱۴۰۵ — از قفلِ تغییرنیافتهٔ محیط اجرا، فهرست وابستگی‌های دارای هش
و SBOM خصوصیِ CycloneDX 1.5 با ۲۵ جزء ساخته شد؛ SBOM دادهٔ مجوز ندارد. ۲۵ wheel ویژهٔ لینوکس
با هش‌های `uv.lock` یکسان بودند و بدون دسترسی به فهرست بسته‌ها دوباره حل شدند. مجموعهٔ جداگانهٔ
۲۵تاییِ Windows نیز با کنترل هش، همراه wheel برنامه در محیط تازهٔ پایتون ۳٫۱۲ به‌صورت آفلاین نصب
شد؛ `pip check`، واردکردن ماژول‌های API و وجود فایل رابط موفق بودند. WSL2 توزیع لینوکسیِ نصب‌شده
ندارد؛ بنابراین نصب واقعی روی Ubuntu **انجام نشده است**. سرور در حال خدمت تغییر نکرده و بررسی
مجوز، امضا، کیفیت پاسخ زنده و پذیرش تولید بازند. شکستِ حافظهٔ محلیِ میزکار در یادداشت پایین،
پیش از آماده‌سازیِ این wheelhouse رخ داده بود.

Source-only qualification checkpoint, 2026-09-27 — An offline-built pure-Python application wheel
from `42b35d8` matched the corrected source files byte-for-byte. A fresh offline install on this
Windows desktop failed because its local dependency cache is incomplete; the Linux wheelhouse and
serving hosts were not tested or changed. The semantic-capture tool now supports bounded explicit
expectations. Rechecking the prior private six-case report without a new server request passed two
greetings and failed the same four host-inventory/file-focus cases. This adds no live acceptance;
the serving release's semantic gate remains `failed` and the candidate is not deployed.

گام سنجشِ فقط‌درکد، ۵ مهر ۱۴۰۵ — wheel خالص پایتون از کد `42b35d8` بدون اتصال اینترنت ساخته شد و
فایل‌های اصلاح‌شدهٔ درون آن با منبع یکسان بودند. نصب آفلاین در محیط تازهٔ همین میزکار Windows
به‌دلیل کامل‌نبودن حافظهٔ محلیِ وابستگی‌ها شکست خورد؛ wheelhouse لینوکسی و سرورهای در حال خدمت
آزموده یا تغییر داده نشدند. ابزار گردآوری پاسخ اکنون انتظارهای صریح و محدود را می‌سنجد. بازبینی
آفلاینِ گزارش خصوصیِ شش‌موردیِ پیشین، دو سلام را موفق و همان چهار موردِ فهرست میزبان و تمرکز فایل
را ناموفق نشان داد، بی‌آنکه درخواست تازه‌ای به سرور برود. این کار پذیرش زنده نیست؛ معیار معناییِ
انتشار مستقر همچنان `failed` است و اصلاح هنوز مستقر نشده است.

New live semantic checkpoint, 2026-09-26 — A private, TLS-verified, authenticated six-case run
completed with six HTTP 200 responses and server-side logout 204. English/Persian greetings were
brief without monitoring terms. English/Persian multi-host availability questions fell back to
generic Zabbix counts rather than explaining that the connector does not return host-inventory
reachability. English/Persian file-only incident questions were misclassified as `overview` and
included unrelated context. This is a real serving-endpoint failure; the capture tool did not
independently prove the backend release identity. The release manifest now fails the expanded
answer-quality gate. The source-only repair was merged to `main` in PR #18 after all five CI jobs
passed; it has not changed the deployed application or passed a new live qualification. Full
production acceptance remains unavailable. Entries below are historical checkpoints, not newer
serving-release results.

گام تازهٔ سنجش معناییِ زنده، ۴ مهر ۱۴۰۵ — آزمون خصوصیِ دارای TLS و احراز هویت با شش پرسش،
شش پاسخ HTTP 200 و خروج سمت سرور با کد 204 پایان یافت. سلام‌های فارسی و انگلیسی کوتاه بودند و
اصطلاح پایش را وارد پاسخ نکردند. پرسش‌های دسترسی‌پذیری چند میزبان به‌جای توضیح محدودیت دامنهٔ
اتصال‌دهنده، شمارش کلی زبیکس را برگرداندند. هر دو پرسش «فقط فایل» در حالت بررسی رخداد به‌اشتباه
`overview` تشخیص داده شدند و اطلاعات نامرتبط آوردند. این نقص در مسیر زنده مشاهده شده است؛ ابزار
گردآوری، شناسهٔ کدِ پشت سرویس را مستقلاً ثابت نمی‌کند. معیار گسترش‌یافتهٔ کیفیت پاسخ در مانیفست
ناموفق ثبت شد. اصلاح کد پس از موفقیت هر پنج کار CI با درخواست ادغام شمارهٔ ۱۸ وارد شاخهٔ اصلی
شد؛ برنامهٔ مستقر تغییر نکرده و ارزیابی زندهٔ انتشار تازه نیز انجام نشده است. پذیرش کامل تولید
همچنان ممکن نیست. بندهای بعدی گام‌های تاریخی‌اند، نه نتیجهٔ تازه‌ترِ انتشار در حال خدمت.

Source-only semantic-review checkpoint, 2026-09-26 — A bounded capture tool now records fresh
authenticated questions and responses to a private report for manual English/Persian relevance
and evidence review. Its tests, full local suite, lint, types, release and documentation checks
pass. No serving-app semantic corpus has yet been captured or reviewed; the exact-release
qualification gate remains `not_run`. This code does not change the deployed application.

گام بازبینی معنایی در کد، ۴ مهر ۱۴۰۵ — ابزار محدود، پرسش و پاسخ تازهٔ احرازهویت‌شده را در گزارشی
خصوصی برای بازبینی انسانیِ ارتباط معنایی و شاهد انگلیسی/فارسی ثبت می‌کند. آزمون‌های ابزار و
مجموعهٔ محلی، کنترل سبک و نوع، وضعیت انتشار و مستندات موفق‌اند. هنوز مجموعهٔ معنایی روی برنامهٔ
در حال خدمت گردآوری و بازبینی نشده است؛ معیار انتشار دقیق `not_run` می‌ماند. این کد برنامهٔ
مستقر را تغییر نمی‌دهد.

Owner clarification, 2026-09-26 — The reported verification was an **ESXi VM snapshot restore
only**. The owner performed it, but no dated procedure/result record has been reviewed by this
agent. Do not interpret the statement as an independent backup of either PostgreSQL cluster,
WAL/PITR, artifact/key recovery, or survival of a serving-host/storage failure. The local-delivery
recovery deferral below remains in effect; the recovery profile and full-production gate remain
unqualified. Proceed with the exact serving app's non-recovery answer-quality checkpoint.

توضیح مالک، ۴ مهر ۱۴۰۵ — آزمون گزارش‌شده **فقط بازیابی از snapshot ماشین‌های ESXi** بوده و مالک
آن را انجام داده است؛ گزارش تاریخ‌دارِ روش و نتیجه هنوز در این بازبینی بررسی نشده است. این گفته
اثبات پشتیبان مستقلِ دو پایگاه PostgreSQL، ‏WAL/PITR، بازیابی فایل و کلید یا دوام در برابر خرابی
میزبان و ذخیره‌سازی نیست. تعویق بازیابی در تحویل محلی همچنان برقرار است؛ پروفایل بازیابی و پذیرش
کامل تولید پذیرفته نشده‌اند. کار غیربازیابیِ بعدی، بررسی کیفیت پاسخ انتشار جاری است.

Owner-directed local-delivery scope, 2026-09-26 — The owner reports that ESXi takes daily
snapshots of all four servers and directs NextOps to continue every non-recovery workstream
without treating independent recovery as the first active blocker. Snapshot scheduling, retention,
storage independence and successful restoration were not independently verified. VM snapshots
share the serving hypervisor/storage failure domain and are not evidence of PostgreSQL-aware
backup, WAL/PITR, independent disaster recovery or an isolated restore. The recovery profile and
its `independent_backup`/`isolated_restore` gates remain unqualified, and the full production
acceptance claim remains prohibited. The machine-readable `delivery_scope` records this explicit
deferral; it does not approve a host change or sign off the remaining security and release gates.
The active engineering checkpoint is now the exact serving app's held-out bilingual semantic
review, followed by its exact-release rollback, server-side WAN and cold-start qualification in
an authorized window. Licensing, offline signing, certificate rotation/operator delivery, host
network policy and named sign-off remain separate non-recovery prerequisites.

دامنهٔ فعلی به دستور مالک، ۴ مهر ۱۴۰۵ — مالک می‌گوید از هر چهار سرور هر روز در ESXi ‏snapshot گرفته
می‌شود و خواسته است کارهای غیربازیابی بدون توقف پشت مقصد مستقل ادامه یابند. برنامهٔ snapshot،
نگهداری آن و بازیابی موفق مستقلاً تأیید نشده‌اند. این نسخه‌ها جای پشتیبان آگاه از PostgreSQL،
WAL/PITR یا بازیابی بیرون از دامنهٔ خرابی میزبان را نمی‌گیرند. پروفایل بازیابی و معیارهای پشتیبان
مستقل و restore ایزوله همچنان پذیرفته نیستند؛ پذیرش کامل تولید نیز ممنوع است. گام فعال، بازبینی
معناییِ دوزبانهٔ انتشار جاری و سپس آزمون بازگشت، قطع WAN سمت سرور و شروع سردِ همان انتشار در
پنجرهٔ مجاز است. مجوز پروژه، امضای آفلاین، گواهی و اعلان، سیاست شبکه و تأیید نام‌دار جداگانه بازند.

Source-only production-claim guard, 2026-09-26 — The release-status validator now rejects a
`production_acceptance: passed` claim unless deployment status agrees, every current-app and
release gate is `passed`, and the public recovery profile asserts its complete independent
destination, objectives, offline bundles, key custody and restore gates. Focused negative tests
pass; the checked-in blocked profile continues to validate honestly but cannot support a
production claim. This cross-manifest consistency check is not an off-host backup, isolated
restore, authorization or production sign-off.

Revision-scoped status checkpoint, 2026-09-26 — The public release manifest now separates
historical controlled-campaign gates from a required `current_application_qualification` block
bound to the actual application release and source commit. For `nextops-0.1.0-01755d1`, bounded
live functionality is `passed`; held-out bilingual answer semantics, exact-release rollback,
server-side WAN isolation and VM reboot/cold start are `not_run`. The schema and validator reject
missing gates or mismatched release identity. This records existing evidence more precisely; it
does not run those tests or change the serving release or production status.

Source-only acceptance-harness checkpoint, 2026-09-26 — The live Edge harness now retains the
test-session token after login and, if a later assertion fails, attempts server-side logout before
closing the browser. It records `revoked`, `revocation_failed`, or `revocation_unverified` without
writing the token to its report. Three focused cleanup tests and the complete local suite passed
(185 passed, ten skipped for the same local PostgreSQL/POSIX prerequisites as before). This repair
has not been run against a live failure on the serving release; it does not revoke the two earlier
aborted sessions retroactively or change `nextops-0.1.0-01755d1` production status.

Current controlled app checkpoint, 2026-09-26 — PR #10 passed all five hosted CI jobs and merged
as `b4d2209`. Application release `nextops-0.1.0-01755d1` was built from the same source tree,
verified by SHA-256, installed from the locked local wheelhouse into a fresh immutable virtualenv,
and promoted under a 15-minute rollback timer. AI API and connector remain
`nextops-0.1.0-cdde129`; the CPU model/runtime, database schema, Zabbix and OS packages did not
change. The exact app release passed fresh protected-login/API checks for English/Persian greetings,
Zabbix monitoring, the reported system-file limitation, focused filesystem capacity, evidence
times/hash and durable audit IDs. A fresh Edge browser passed the simplified panel, file focus,
Persian RTL/mobile layout, server logout/new-tab isolation and zero page WAN requests under a deny
proxy. App/database/tunnels are active, release-file integrity passes and the rollback timer is
disarmed. The full held-out semantic corpus, exact-release rollback drill, server-side WAN isolation
and VM reboot were not rerun on this revision. Two earlier browser harness attempts read a hidden
audit field with `innerText` and failed; the corrected test passed. Production remains unaccepted
because independent recovery and the other owner inputs below are unavailable.

Pre-promotion focused-answer and workspace source checkpoint, 2026-09-26 — The owner reported that a request to
show only system files produced an all-data table and that the panel was too complex. This branch
now classifies unambiguous file/filesystem questions without expanding connector access. The Linux
collector exposes approved mount capacity, not arbitrary file names or contents. The model receives
a question-focused bounded view; the displayed focused reply is built deterministically from typed
evidence or explicitly states the file-listing limit. The API labels this `deterministic_focus` and
returns `answer_focus`; the complete authorized evidence, provenance and audit remain available.
The source UI now uses one question/answer column with visible source/time/scope and collapsed full
details. A local browser fixture was visually checked in English and Persian, including narrow-width
layout, the file-listing refusal and the collapsed evidence boundary. The final local run passed
182 tests; 10 were skipped (nine requiring an isolated PostgreSQL URL and one POSIX-only collector
test). Strict typing, lint/format, JavaScript syntax, Markdown parity/local links and release-status
validation passed. Live CPU-model relevance, real-server browser, WAN-disconnected and deployment
qualification for this exact revision were **not run at that source checkpoint**. The later
controlled promotion is recorded above; it does not imply model training or production acceptance.

Pre-promotion answer-quality source checkpoint, 2026-09-26 — The owner reported that a submitted question did
not match the AI response and that the result looked fabricated. A fresh browser capture from the
prior section-by-section audit showed a 128-token incident reply that appeared unfinished while
the interface displayed an evidence-bounded notice; a Persian monitoring fallback was overly
dense with metric text. A second controlled read-only browser reproduction of the same app-host
question returned HTTP 200, `finish_reason=length`, 128 output tokens and a deterministic fallback.
The different labels for a length-limited reply expose the incomplete guard, not proof that one
answer was factually sound. Source inspection found that the live-answer guard checked source and
partial/stale terms but not `finish_reason`, so a length-limited completion could pass. On the
unpromoted `codex/answer-completion-guard` branch, source changes fail closed on truncated
completions and long live-question echoes, shorten evidence-only fallbacks, ask for question-first
plain-text responses, and avoid presenting lexical checks as proof of factual correctness. Focused
local API/browser-fixture tests pass. The owner's exact prompt/response pair, semantic review of a
held-out bilingual corpus, and live release qualification are still needed; the serving releases
and production status have **not** changed. No model weights were trained or replaced.

Latest controlled checkpoint, 2026-09-26 — commit `cdde129` closed a credential-forwarding
redirect risk in the application-to-AI, application-to-connector and connector-to-Zabbix HTTP
clients. Redirects now fail rather than carrying a bearer or API token to another origin. Local
redirect regressions, 161 selected tests, strict typing, lint/format, and all five hosted CI jobs
passed. Immutable application, inference API and connector releases are all
`nextops-0.1.0-cdde129`; the CPU runtime and model did not change. A fresh WAN-denied Edge session
passed login, English/Persian layout, general answer, live Zabbix answer with provenance, logout
and new-tab isolation. The four guests now reject password and direct-root SSH and require public
keys; new operator connections and newly established application tunnels passed. The AI guest's
previously inactive UFW is active with deny-incoming/OpenSSH, matching the other guests. This is
controlled user testing, not production acceptance. The owner confirmed that the independent
recovery destination/lab, approved project license, notification channel/recipients, replacement
certificate pairs and named approvers are not available.

The follow-up OS-origin audit found Agent 2 `7.0.30` on app, AI and connector after Zabbix server
had reached `7.0.31`. All three agents were upgraded serially from the hash-checked cached offline
`7.0.31` package with unchanged configurations and exact prior-package rollback copies. Agent 2
now reports `7.0.31` and active on all four guests, with no passive listener, failed unit, pending
package or reboot marker. A fresh WAN-denied bilingual browser/monitoring run passed afterward.
Because these three agents have no configured apt origin, future Agent 2 versions require a
deliberate reviewed offline import even when `apt list --upgradable` says zero.

Network claim boundary: the historical four-guest WAN-isolation campaign used a temporary
outbound nftables rule that was later removed. On this date direct public IPv4 HTTPS is reachable
from administrative shells on all four guests. The application, AI API and model service units
still enforce loopback-only IP egress. The connector now denies all but loopback and the reviewed
LAN at its process boundary: four fresh authenticated incident requests and a controlled negative
public-egress probe passed. Persistent **host-wide** egress denial remains partial and requires a
verified DNS/time/maintenance-proxy allowlist before guarded deployment.

Updated: 2026-09-26 — The owner resumed production-hardening and recovery scope. The four serving
guests received a serial, rollback-protected package maintenance change. Exact installed packages
were reconstructed before mutation, candidate packages and SHA-256 manifests were retained in
root-only per-host change directories, and local PostgreSQL safety dumps were verified before the
two database-host updates. Every guest now reports `running`, zero failed units, zero pending
packages and no reboot marker. Zabbix is now `7.0.31`; both PostgreSQL deployments remain `16.15`.
These local rollback copies and dumps are change safety material, not independent disaster-recovery
backups.

At that package-maintenance checkpoint, the active application, AI and connector releases were
unchanged. A fresh Edge context with public
WAN denied passed login, English LTR, Persian RTL, general local AI, evidence-grounded monitoring,
provenance identifiers, server-side logout/revocation and new-tab isolation. The first run exposed
an acceptance-harness race: it asserted the login view before the asynchronous revocation request
completed. The harness now waits for the UI transition and requires the actual logout `204`; the
live rerun passed. Direct authenticated checks also preserved greeting relevance, current-state
scope redirect, evidence-bounded monitoring and safe composite-incident fallback.

Supply-chain evidence advanced without changing runtime dependencies. Syft `1.52.0`, verified
against the publisher-provided asset digest, scanned the exact deployed application archive:
SPDX and CycloneDX outputs recorded 27 packages and 26 components. A production-only
`pip-audit 2.10.1` input contained 25 dependencies and reported zero known findings. This is not a
complete operating-system/runtime vulnerability assessment. The inventory also confirmed that the
NextOps project itself has no declared repository/package license; no agent may choose that legal
grant. Release signing, an accepted offline trust root, complete vulnerability evidence and named
legal/security approval remain open.

Production acceptance remains unavailable. No independent recovery destination or isolated restore
lab exists, so pgBackRest/restic installation and restore drills were not fabricated on serving
guests. No real local operator-delivery channel with named recipients exists, replacement
CA-issued certificate pairs/key custody were not supplied, the project license is undecided, and a
human production approver has not signed the bounded profile. The repository recovery contract
continues to fail closed until those external inputs exist.

Earlier checkpoint on 2026-09-26 — The answer-integrity increment was accepted for controlled user
testing.
Application release `nextops-0.1.0-2397581` and inference API release
`nextops-0.1.0-fd3c353` were active at that checkpoint; previous immutable releases remained
available for rollback.
General output is explicitly model-only and potentially incorrect, current infrastructure state is
not answered from model memory, and live answers carry consistent nested evidence labels. Generated
execution claims, unsupported root cause, missing sources, hidden stale/partial qualifiers and long
prompt echo fail closed to a localized deterministic response before persistence. Audit details now
record the integrity outcome and limitations.

All five hosted jobs passed for the final source: quality/unit, PostgreSQL 16, PostgreSQL 17,
browser fixture and secret scan. The final private loopback report passed eight English/Persian
cases and engineering semantic review. A live authenticated app exercise passed `Hi` relevance,
current-status redirect, monitoring evidence, composite incident fallback and immediate test-session
revocation. Zabbix, connector, AI and app then rebooted serially onto kernel `6.8.0-142`; all returned
`running`, zero failed units, no warning-or-higher service journal entries and no reboot marker.
Ubuntu base updates remain pending and were not downloaded because the approved proxy/offline bundle
path was not established in this change; the Zabbix 7.0.31 candidate was not installed or claimed.

At that checkpoint, the owner explicitly deferred all backup, PITR, restore and disaster-recovery
work. The repository
contract and historical evidence remain, but no recovery package or drill will be performed until
that scope is resumed; production acceptance therefore remains unavailable. No SMTP host exists.
Certificate detection and local Zabbix problem visibility remain active, but operator notification
delivery is still unaccepted and no email route is claimed.

Updated: 2026-09-23 — Phase 2 is deployed for controlled user testing with application release
`nextops-0.1.0-eb57241` and connector release `nextops-0.1.0-e2dad3a`. An authenticated operator can
select one of four deployment-owned
targets and receive a durable English or Persian incident explanation grounded in bounded Zabbix
history/events and a direct read-only Linux snapshot. The model and browser receive no target
credentials; authorization, target selection, forced commands, evidence hashing and audit remain
deterministic application/connector controls.

Live English and Persian API investigations passed with the local CPU model, composite evidence and
run/evidence/audit identifiers. All four direct Linux collectors and all four composite connector
paths passed; unauthenticated and unknown-target requests failed closed. App/connector restart,
immutable rollback/forward, server/API WAN denial, the authenticated live browser, Phase 2
dependency loss/recovery and a fresh serial reboot of all four VMs now pass. The browser used normal
TLS verification and denied WAN access, returned bilingual combined evidence and completed RTL,
logout and new-tab isolation checks. The connector outage returned a safe `503` while general AI
remained available, then a fresh audited incident succeeded after recovery. All guests ended
`running`, with zero failed units and no reboot requirement. The live run exposed and corrected an
Nginx route timeout for Phase 2 incident requests; the route now has the bounded 180-second assistant
window and regression coverage. Production acceptance remains blocked by independent off-datastore
backup, WAL/PITR, the remaining certificate rotation/operator-notification gates and
disaster-recovery sign-off.

Recovery source readiness now has an explicit claim boundary. ADR 0008 and the schema-validated
public profile select separate pgBackRest repositories for the application and Zabbix PostgreSQL
16 clusters and restrict restic to approved non-database files. CI rejects shared database
repositories, secret-like public fields, database/WAL input to restic, and any qualified claim that
lacks an independent destination, approved RPO/RTO and retention, verified offline bundles, key
recovery, and passed isolated/offline/negative restore gates. The profile is intentionally valid
but `BLOCKED`; no backup package or job was installed on the serving VMs and production readiness
is not claimed.

A paired English/Persian production-blocker runbook now converts every remaining external decision
into an owner-action checklist with exact safe commands, private-record fields, stop conditions and
handoff evidence. It recommends an independent recovery host plus isolated restore lab, records
recovery objectives and two-person key custody, defines the local notification and certificate
handoff, and names the supply-chain/final approval gates. This is operator guidance only; it does
not turn any blocked, partial or unexecuted gate into a pass.

The next source hardening increment closed browser-only logout. `POST /api/v1/logout` now revokes
exactly the presented durable PostgreSQL session under a row lock and writes one correlated,
append-only audit event without token material. Replay and unknown tokens are idempotent and do not
create an existence oracle; another session for the same identity remains valid. The offline panel
attempts server revocation before clearing `sessionStorage`, with fail-safe local cleanup. Commit
`eb57241` passed all five CI jobs and immutable release `nextops-0.1.0-eb57241` passed live API and
normal-TLS browser logout, former-token rejection, other-session preservation, idempotent replay and
exactly one sanitized audit-event verification. Release `nextops-0.1.0-54c8bb4` remains available
for rollback.

The bounded certificate-expiry detection increment is accepted in the controlled deployment without
adding a runtime network dependency. Commit `f540a9d` passed all five hosted CI jobs. Its guarded
installer deployed the deterministic checker and hardened persistent daily timer to both TLS
frontends under change `certificate-lifecycle-20260923-01`. Each checker has a `2.7 OK` systemd
security score, can read only the public certificate, and cannot read the root-owned mode-`0600`
private key. Both live certificates are healthy under the 90-day policy through 2027-10-24;
isolated one-day and malformed fixtures returned the required distinct failures. Four active-agent
items and six tagged triggers now monitor service result, timer state and missing data in local
Zabbix. A guarded application-timer outage changed the expected trigger to problem, and recovery
returned it to healthy with fresh values from both hosts. Normal application TLS and pinned-CA
Zabbix HTTPS still pass with no external frontend requests. Production status remains partial until
an approved operator delivery route and an observed certificate rotation/rollback drill pass.

## English

### Current controlled user-testing checkpoint

Phase 2 is deployed for controlled user testing at this checkpoint. Its contract resolves four
logical target IDs from deployment configuration, permits only named read operations, and bounds
Zabbix history/events and every Linux diagnostic category. Live provenance, authentication,
partial markers, direct collection, durable model/audit integration, immutable release rollback,
service restart and guarded server/API WAN isolation passed. The browser fixture passed English
LTR, Persian RTL, responsive layout and reduced-motion behavior. The full deployed authenticated
browser, Phase 2 dependency loss/recovery and serial VM reboot gates now also pass. The next
engineering checkpoint is recovery infrastructure, not another Phase 2 feature increment.

The repository-side recovery contract for that checkpoint is implemented under `deploy/recovery`,
with eight focused validator tests and CI enforcement. Its production-only
`--require-qualified` mode currently fails by design. The remaining work begins with an approved
destination outside the serving guest, datastore and hypervisor failure domains, followed by exact
offline bundle verification and real independent restore drills.

The authenticated application and bilingual panel are deployed as immutable release
`nextops-0.1.0-2397581` on the app guest behind private TLS and Nginx. PostgreSQL 16 stores
application identity and session state on
its dedicated verified mount. Bootstrap and recovery endpoints, API documentation and the direct
application listener are not exposed through Nginx. The browser receives neither the AI service
credential nor the Zabbix token.

The dedicated Zabbix guest now runs Zabbix 7.0.30, PostgreSQL 16, Nginx/PHP-FPM and Agent 2. The
default administrator password was rotated. A separate API-only reader has no frontend access, an
allowlist limited to `host.get`, `item.get`, `problem.get`, `history.get` and `event.get`, read
permission for one approved host group and a token stored only on the connector guest. It now sees
exactly four approved hosts: the Zabbix guest plus app, AI and connector. An unrelated read and a
mutation remain denied. The
connector uses verified TLS, bypasses inherited proxies, exposes only named summary and bounded
incident-context operations on loopback and has no generic URL, JSON-RPC, shell or write surface.

The app, AI and connector guests run the exact cached Agent 2 package
`1:7.0.30-1+ubuntu24.04`. Each has a distinct PSK and sends active checks to the source-restricted
Zabbix trapper path. They expose no passive port 10050 and explicitly deny `system.run[*]`. Final
reader validation observed 65, 65 and 58 fresh supported items respectively; these counts are a
point-in-time observation, not a fixed template contract. No repository refresh or unrelated
package upgrade ran. All four hosts retained a `running` system state and zero failed units.

The app reaches AI and connector loopback services through separate pinned-host-key SSH forwards.
Live qualification returned eight fresh self-monitoring measurements with zero stale metrics and no
active problems. The desktop end-to-end test passed login, session authentication, TLS validation,
live evidence retrieval and grounded English and Persian answers. The measured synthesis times were
56.6 seconds and 67.1 seconds for the 128-token ceiling. Visual review confirmed the English and
genuine RTL Persian login layouts. Source version, host, collection time, measurement time, stale
state and active-problem count are shown with the answer.

The first real browser request exposed a mismatch between the panel's 384-token request and the
qualified 120-second CPU generation boundary. It ended as a generic `503` even though readiness and
monitoring were healthy. The deployed repair caps live investigations to 128 tokens in both the
server and panel, preserves safe timeout/overload status across the internal boundary and displays
localized actionable errors. Replaying the exact `hi` request with the old 384-token payload passed
with HTTP 200, live evidence and 128 output tokens in 61.6 seconds. The previous immutable release
remains available for rollback.

That replay proved transport recovery but exposed a separate relevance defect: the panel routed
every question through `/api/v1/investigate`, so even `Hi` produced Zabbix status. Release
`nextops-0.1.0-3d61bf6` now makes **General assistant** the default and keeps **Live monitoring** as
an explicit opt-in mode. General questions use `/api/v1/assistant/generate`, receive no monitoring
evidence and carry a model-only badge; monitoring questions retain the evidence-grounded route and
panel. The exact default-mode request `Hi` returned “Hello! How can I assist you today?” in 14.0
seconds with no Zabbix or system-status content. A Persian greeting also returned a Persian general
answer without monitoring content. The monitoring regression passed with eight fresh metrics and
grounded English and Persian answers. Release `8d31bcb` remains available for rollback.

Release `nextops-0.1.0-fde27bd` completes the missing Stage 1D persistence link without a schema
migration. Before any connector or model call, `/api/v1/investigate` creates a scoped PostgreSQL run.
Successful completion atomically stores the already-bounded Zabbix summary, a canonical SHA-256
evidence reference, the model result and an append-only completion audit; safe failure code and
message metadata are likewise persisted and audited without raw exceptions. The panel exposes the
run, evidence and audit identifiers, and authenticated run retrieval returns the same scoped result.
All 95 non-integration tests and six isolated PostgreSQL tests pass. Live acceptance returned eight
fresh metrics, no active problems and a 128-token answer in 57.2 seconds; stored-run retrieval,
independent evidence-hash verification and audit linkage passed. A direct database check found the
successful `live_monitoring` result, two linked audit events, the 64-character hash and a matching
completion audit ID.

Stage 1E failure qualification promoted connector release `nextops-0.1.0-3d7d725` and app release
`nextops-0.1.0-13a3369`. `MonitoringSummary` now exposes `is_partial` and typed reasons; the current
eight-metric live view reports `metrics_truncated` while retaining separate per-measurement stale
flags. The prompt boundary treats host, metric, value, unit and problem text as untrusted data even
when the API source is authenticated. Isolated cases passed for stale values, partial/no-usable
metrics, over-limit malformed text and embedded prompt instructions.

A temporary token owned by the existing reader identity saw the same four approved hosts, was
denied immediately after revocation and was deleted without changing the live token. During a
brief Zabbix HTTPS/API frontend outage, monitoring summary and investigation returned safe,
retryable `503` responses labeled `connector.summary_unavailable`; the failed run and its audit
event were durably stored while general model-only Q&A still succeeded. The frontend restarted,
fresh monitoring recovered and a later live investigation persisted the partial marker and
independently verified evidence hash in 67.9 seconds. Stopping the Zabbix engine alone did not make
the PHP API unreachable, an important operational distinction. Ruff, strict mypy, 102
non-integration tests and six isolated PostgreSQL tests pass.

This is a controlled user-testing slice, not production acceptance. The four approved Phase 1
guests are now monitored; the wider estate is not. Explicit WAN disconnection passed for the
server/API path, including fresh bilingual model-only answers and new evidence-linked live
investigations. After correcting Zabbix's database shutdown ordering and the application's database
startup ordering, all four guests passed serial clean reboots under the early WAN-deny policy and
returned to `running` with zero failed units. A fresh Microsoft Edge context subsequently passed
with a deny proxy allowing only the private application origin. Cancellation, provider loss,
missing/corrupt artifacts, an isolated `ENOSPC` staging case, sustained load and logical isolated
restores also passed. Certificate detection and local alert recovery now pass; independent
off-datastore backup, WAL/PITR recovery, operator notification, certificate rotation/rollback and
disaster-recovery promotion remain open. Private addresses, tokens, passwords, host keys and raw
evidence remain outside Git.

### Requirements and preserved history

The directly verified Git remote is `Omid-NextAI/nextops`, branch `main`. Earlier records name `AmirMo10/nextops`; current README/install clone commands now use the verified remote, while historical statements remain preserved and the active prompt header still needs a separately versioned repository-identity correction. The owner requested English and native-Persian documentation, a single English active prompt, local CPU-only AI, continued operation after Internet loss, a first useful Zabbix status answer, phased VM allocations, storage limits and a dedicated Zabbix server recommendation. All eleven integrations and the 51 original specification sections remain in scope.

The active [master prompt v3.0](requirements/NEXTOPS_MASTER_PROMPT.md) and [v2 archive](requirements/archive/NEXTOPS_MASTER_PROMPT_v2.0.md) remain unchanged in this update. The new [deployment amendment](requirements/DEPLOYMENT_UPDATE.md) explicitly supersedes only the old small-lab recommendation and combined budgets; non-conflicting security, acceptance and feature requirements remain mandatory. The archive still contains the original Persian specification.

The first deliverable was a new Persian/English question about authorized Zabbix status, answered by local CPU generation from actual evidence, with source times, scope and audit while Internet was blocked. Phase 2 now supplies the planned Linux enrichment. Documentation publication alone does not complete a software phase or establish deployment approval.

The paired [Phase 0 report](en/PHASE_0_REPORT.md) and [Persian report](fa/PHASE_0_REPORT.md) record repository evidence, the accepted four-VM architecture, trust boundaries, module and data contracts, CPU benchmark plan, resource gate, connector roadmap, test plan, blockers and the Stage 1A increments. The repository-grounded [threat model](requirements/nextops-threat-model.md) records TM-001–TM-010. On 2026-09-21 the owner accepted Phase 0 and ADRs 0001–0006, confirming one organization initially, small initial scale with future growth, and the dedicated Zabbix path. Every infrastructure authorization remains separate and pending.

Stage 1A Increments 1 and 2 are implemented in repository source. The code has strict contracts and denial policy, FastAPI, Argon2id identity bootstrap/login/recovery, hashed sessions, PostgreSQL/Alembic state, durable runs, worker leases, append-restricted audit and a bilingual panel. Actor organization, environment, roles and scopes derive from server-side session state. Four guarded scripts define the authenticated offline Ubuntu package layer; they are not a complete product installer. A separately built immutable application release, private TLS listener and connector are live in the controlled environment, while a complete reproducible production bundle remains absent. The pinned AI runtime/model and source service profile are recorded below.

Stage 1B Increment 3 adds a strict runtime-neutral `LLMProvider` contract, authenticated inference API, loopback-only llama.cpp adapter, one-active/two-queued scheduler, bounded input/output/timeouts, cancellation cleanup, safe readiness, and structured overload/dependency failures. A schema-validated YAML manifest pins llama.cpp `v0.4.1` and the official `Qwen3-8B-Q4_K_M.gguf`. The pinned runtime and model are installed with the corrected API release on the qualified AI guest. Controlled live quality, process restart, application/runtime/model rollback, cancellation and dependency recovery, artifact failure, sustained bounded load, explicit WAN disconnection and a clean VM reboot are evidenced. Independent disaster backup and PITR remain production gates.

The native Stage 1B slice supplies separate hardened `nextops-llama` and `nextops-ai` units, two
`LoadCredential` secrets, loopback-only cgroup networking, read-only release trees, explicit
CPU/memory/task limits, a strict credential-file loader, and a versioned Persian/English
qualification corpus and runner. It is now live on the AI guest. The first start exposed an invalid
relocated shared-library search path and an insufficient socket-only readiness gate; the unit now
uses the protected stable runtime library directory and controlled startup waits for authenticated
model health. The owner-authorized deployment account now has full passwordless administration;
direct root SSH remains disabled.

### Supplied hardware and storage evidence

The [hardware record](requirements/HARDWARE_BASELINE.json) preserves the owner's ESXCLI output: ESXi 8.0.3 build 24414501; 4 CPU packages, 112 physical cores, 224 logical threads, active hyperthreading, 4 NUMA nodes and 1,442,743,631,872 memory bytes (calculated about 1343.66 GiB). It includes the partial CPU 0/1 sample, reported speed/cache/microcode and reference mappings documented in [ESXI_BASELINE](en/ESXI_BASELINE.md). Exact marketing SKU, rated speed, all-package consistency, guest ISA and actual per-node distribution are not established by that sample. Arithmetic averages are not observed topology or free resources.

Owner-supplied mounted VMFS rows now establish point-in-time capacity: DS-A 149.75 GiB total / 148.34 GiB free; DS-B 1117.50 / 1109.87; DS-C 3576.75 / 3166.8701171875. Public aliases omit real names, UUIDs and mount paths. [STORAGE_PLAN](STORAGE_PLAN.md) excludes VMFSOS/boot volumes, leaves DS-A/DS-B outside the initial allocation and retains the 3 TB project ceiling. The proposed DS-C free target is 25%, exactly 894.1875 GiB or conservatively about 900 GiB. No datastore reservation, RAID/health inspection or I/O benchmark follows from the supplied listing.

Preserve ESXi; Ubuntu Server 24.04 LTS is the approved guest baseline, not a host replacement. Supplied totals/build/listing should not be requested as missing. Current available CPU/RAM, load/reservations, actual physical NUMA placement, VM compatibility and license limits, storage backing/health/latency, outstanding growth and swap placement remain to be checked at execution time. No direct ESXi host access or compatibility certification was performed.

### Sanitized replacement-guest qualification

On 2026-09-21, authorized read-only SSH preflight reached all four clean replacement guests after the owner supplied their new Ed25519 fingerprints independently and each matched the live handshake. Key-only authentication, strict host-key checking and direct-root denial were verified. The configured vCPU, memory, virtual-disk and dedicated-mount layouts match the public role budgets. All guests run Ubuntu 24.04.5 LTS under VMware. On 2026-09-22 the fleet was rechecked after the AI deployment and a narrow GLib security update on app: every guest reported `running` systemd state, zero failed units, zero pending package upgrades and no reboot requirement. UFW is active on app, connector and Zabbix but inactive on AI; that drift remains a separate hardening item. The AI endpoints remain loopback-only; the later monitoring change added one Zabbix trapper listener on the private service interface with three source-specific firewall rules. The three monitored NextOps guests added no listener, and no public product listener exists.

After explicit owner authorization for connected preparation, each host used its existing strict proxy chain to refresh signed repositories and install only its role package layer. No broad OS upgrade ran. Exact observed direct versions are PostgreSQL 16.15 and Nginx 1.24 on app; GCC 13.3, CMake 3.28, Ninja 1.11 and OpenBLAS 0.3.26 on AI; Python 3.12 venv support on connectors; and Zabbix 7.0.30, PostgreSQL 16.15, Nginx 1.24 and PHP 8.3.6 on Zabbix. The official Zabbix 7.0 Ubuntu 24.04 release bootstrap package was pinned by SHA-256 before repository import. Package post-install starts were blocked and, at that preparation checkpoint, all product/database/web services were inactive and disabled, no PostgreSQL cluster existed, and no listener was added. Since then, the application/database/proxy, AI, connector and Zabbix slices have been deliberately configured and activated for controlled testing, followed by the bounded Agent 2 host-coverage change recorded above. Docker was not installed because the selected native systemd design does not need it and a container socket would enlarge the trust boundary.

Protected non-login service identities and role directories now exist. The pinned llama.cpp commit was built on the qualified AI guest with Release, CPU-native, OpenMP and OpenBLAS settings and no GPU linkage; its promoted binary hash is in the inference manifest. The pinned 5,027,783,488-byte Qwen model matched its expected SHA-256 before and after protected-volume promotion. At that checkpoint, the immutable API release was `nextops-0.1.0-fd3c353`; `nextops-0.1.0-62de8d6` and `417d888` were prior protected releases. A cold process restart restored both services in 109 seconds. The 2026-09-23 campaign additionally verified protected runtime/model rollback copies, client-cancellation cleanup, dependency recovery, fail-closed missing/corrupt model handling and a five-minute two-client load: 98 of 99 requests succeeded, p95 total latency was 6.114 seconds, peak measured service memory was 4,885,475,328 bytes, and the scheduler never exceeded one active/one queued request. Both services remain enabled, unprivileged, CPU-only and limited to `127.0.0.1:8080` and `127.0.0.1:8090`; `systemd-analyze security` reports `2.7 OK` for each. Raw evidence, credentials, addresses and host keys remain outside Git. Dependency-license approval and production sign-off remain open; recovery work is owner-deferred.

### Current proposed deployment

| Role | First needed | vCPU | RAM GiB | Disk GiB |
|---|---|---:|---:|---:|
| nextops-app | Phase 1 | 8 | 32 | 200 |
| nextops-ai | Phase 1 | 24 | 128 | 500 |
| nextops-connectors-ro | Phase 1 | 4 | 8 | 80 |
| **zabbix-server** | **Before Stage 1C live integration** | **4** | **16** | **200** |
| nextops-db | Phase 3, recommended | 8 | 64 | 300 |
| nextops-executor-rw | Phase 7, remediation only | 4 | 16 | 80 |

The new Zabbix VM runs its own monitoring database/frontend/API, not the AI model or the NextOps database. It replaces the earlier 4-vCPU/8-GiB/100-GiB lab fallback for the new-server path. Do not create both; inspect and reuse suitable existing local monitoring instead when available. NextOps-only counts remain 3/4/5; inclusive counts are 4/5/6.

The first combined profile is **40 vCPU / 184 GiB RAM / 980 GiB VMDKs**, plus provisional 184-GiB ESXi swap = **1164 GiB before other overhead**. Later combined profiles are 48/248/1280 (1528 GiB with provisional swap) and 52/264/1360 (1624 GiB). Against unchanged prior DS-C free space, projected free values are 2002.87, 1638.87 and 1542.87 GiB. These are alternative budgets, not cumulative additions, reservations, benchmarks or approval to consume all remaining headroom. Count growth/VMX/snapshot/staging/restore obligations separately and reconcile already-created VMs.

The [new English guide](en/ZABBIX_SERVER.md) and [Persian guide](fa/ZABBIX_SERVER.md) document the proposed native Zabbix 7.0 LTS / PostgreSQL 16 / Nginx / PHP-FPM / Agent 2 stack, full `vg_zabbix` LVM layout, 7-day history / 90-day numeric-trend starting policy, read-only API identity, self-monitoring, offline acceptance and single-host recovery limits. Exact packages, retention settings and VM/LVM configuration are not installed or tested by these documents. Machine-readable proposed values are in [ZABBIX_SERVER_PLAN.json](requirements/ZABBIX_SERVER_PLAN.json), separate from the supplied hardware evidence.

### Per-server deployer dossiers

The versioned [deployment-dossier specification](requirements/SERVER_DEPENDENCY_DOSSIER_SPEC.md), shared [JSON Schema](../deploy/server-dependencies/server-dependency.schema.json), and four human-readable YAML server instances now provide one handoff record for `nextops-app`, `nextops-ai`, `nextops-connectors-ro`, and `zabbix-server`. The paired [English](en/DEPLOYMENT_DOSSIERS.md) and [Persian](fa/DEPLOYMENT_DOSSIERS.md) guides define how a deployer resolves private inputs without committing them.

Each dossier includes authorization state, source records, VM sizing, service identities, software/artifact locks, configuration paths, reference-only secrets, network/storage boundaries, dependency order, read-only or guarded command templates, explicit blocked commands, observability, backup/rollback, required private inputs, acceptance gates, and known limitations. Exact known resources reconcile to 40 vCPU / 184 GiB RAM / 980 GiB VMDKs, and the Zabbix mount/LVM entries reconcile to the 200-GiB proposal. The owner-requested JSON-to-YAML conversion preserved every data value. The repository validator safely parses the four YAML files, checks schema 1.0.0 and the approved server IDs, rejects stale JSON dossier copies, and verifies the combined resource totals.

Each role now has an executable entry script under `deploy/installers`. A shared tested engine authenticates an all-file bundle manifest against a separately supplied SHA-256, requires exact Debian package versions including the dependency closure, isolates APT to the signed local repository, rejects unexpected installs/removals, blocks package-managed service startup and automatic PostgreSQL cluster creation, and verifies installed versions. Apply additionally requires root, Ubuntu 24.04 on VMware, root-owned/non-writable bundle contents, an explicit authorization marker and a change ID. Check mode performs bundle validation only. No real package lock, signing key, repository bundle, or clean-server apply evidence exists in this repository.

These records expose rather than hide the deployment blockers. The controlled application,
PostgreSQL, private reverse proxy/UI, AI, connector, Zabbix state and four-host monitoring coverage
exist. Fresh-browser isolation, artifact rollback, the remaining scoped failure cases, sustained
bounded load and logical restores of both databases now have live evidence. A reproducible complete
production installer, independently stored pgBackRest/WAL repository, restic artifact repository,
PITR drill and disaster-recovery bundle do not. Private configuration, certificates and target
credentials remain only in protected deployment locations; complete production acceptance remains
open.

### Durable agent context

Six repository-scoped Codex skills under `.agents/skills` route project context, server operations, bilingual documentation, bounded change planning, acceptance review and documentation-drift review. [MARKDOWN_CONTEXT_INDEX](MARKDOWN_CONTEXT_INDEX.md) catalogs project-owned Markdown files and maps task types to the relevant sources without loading the entire documentation set into every context window. The documentation validator excludes dependency/build trees and fails on a missing or stale catalog entry; three focused tests cover discovery and catalog reconciliation. These skills are development aids, not application capability, authorization or infrastructure security boundaries.

### Milestones and actual evidence status

| Stage | Required result | Evidence status for this update |
|---|---|---|
| 0 | Architecture/gap/threat report and appropriate approvals | Owner accepted architecture/roadmap and ADRs on 2026-09-21; the clean replacement guests passed read-only qualification, while ESXi/storage refresh and operation-specific authorization remain separate |
| 1A | Local identity, policy, database, durable work and audit | Authenticated app, PostgreSQL migration, private TLS panel and session path are live for controlled testing; durable live-investigation and audit linkage now uses the existing scoped run model |
| 1B | New local CPU answers and offline model cold load | The pinned runtime/model and corrected API release are installed behind hardened loopback-only units; authentication, bilingual quality, five-minute bounded load, cold process restart, clean VM reboot, application/runtime/model rollback, cancellation/dependency/artifact recovery and four-guest WAN isolation passed. Independent disaster backup, PITR and production sign-off remain open |
| Zabbix prerequisite | Dedicated database mount, monitoring, frontend/API and scoped reader before 1C | Zabbix 7.0.30, PostgreSQL, TLS frontend/API and the scoped reader are active; the server plus app, AI and connector are monitored by PSK-authenticated active Agent 2 paths, and the API allowlist/host-scope denials pass |
| 1C | Real bounded read-only evidence with correct counts | Controlled live connector qualification passed with eight fresh measurements, explicit timestamps/staleness and zero active problems; the reader sees all four approved Phase 1 hosts with fresh items, while the full failure matrix remains |
| 1D | New evidence-linked Zabbix answer with audit | English/Persian grounded answers pass; every started live investigation now has a durable scoped run, bounded evidence snapshot/hash, model result, safe failure outcome and append-only audit linkage verified in isolated PostgreSQL and the live path |
| 1E | Offline fresh login/restart, security/failure/capacity tests | Fresh login, bilingual general Q&A, live evidence and audit passed while all four guests were WAN-blocked. A separately WAN-denied fresh browser, revocation, cancellation, dependency/artifact/low-space recovery and five-minute capacity profile pass. After correcting database-cluster ordering, all four guests passed the serial clean-reboot matrix. Production backup/PITR acceptance remains open |
| 2 | Read-only Linux/Zabbix incident investigation | Application release `nextops-0.1.0-2397581` and connector release `nextops-0.1.0-e2dad3a` are live with four immutable targets, distinct forced-command keys, bounded/redacted Linux snapshots, concurrent composite evidence, durable bilingual answers and audit. Live English/Persian API, answer-integrity controls, restart, rollback, server/API WAN denial, authenticated WAN-denied browser, dependency loss/recovery, a fresh four-VM serial reboot and audited session termination all pass. Production recovery gates remain separate and owner-deferred |

The user may perform provisioning independently; verify their actual state before claiming a VM either exists or does not exist. A screenshot of VM settings is not proof of an accepted application workflow. Resume from the next evidenced, authorized incomplete stage rather than resetting progress.

### Scope of this publication and next action

This state records Phase 0 acceptance, the controlled Stage 1 slices and the deployed Phase 2
read-only Linux/Zabbix investigation path. It preserves the source requirements, archived prompt,
diagrams and per-server handoff. It is not a host vulnerability audit, production acceptance,
independent recovery proof or complete provisioning record.

The source slices use Python 3.12.10, uv 0.12.17, Pydantic 2.13.5, FastAPI 0.141.1,
SQLAlchemy 2.0.54, Alembic 1.20.0, Psycopg 3.3.6, Ruff 0.16.8, mypy 1.20.2 and pytest 9.1.1
with a generated `uv.lock`; Playwright 1.63 is a locked development-only browser dependency. The
CI workflow defines digest-pinned PostgreSQL 16.15 and 17.6 jobs. For Phase 2, formatting, lint,
strict typing, 137 local non-integration tests plus one POSIX-only collector check, both PostgreSQL
CI jobs, real-browser fixtures and secret scanning passed. The earlier Stage 1 fresh-browser/offline,
failure-recovery, load and restore
records remain historical evidence, not inferred Phase 2 reruns. Dependency/license approval,
independent backup/PITR and production promotion remain separate gates.

The next engineering checkpoint in [NEXT_TASK](NEXT_TASK.md) is recovery engineering; the three
previously unexecuted Phase 2 qualification gates are now closed without rebuilding the accepted
implementation. Production promotion remains blocked on an approved
off-datastore recovery destination, PostgreSQL-aware repositories/WAL archiving, permitted artifact
backup, independent PITR, recorded RPO/RTO and key recovery, and operational sign-off.

## فارسی

نقطهٔ کنترل‌شدهٔ کنونی، ۴ مهر ۱۴۰۵ — درخواست ادغام شمارهٔ ۱۰ هر پنج کار CI را گذراند و با
`b4d2209` در شاخهٔ اصلی ادغام شد. انتشار برنامه `nextops-0.1.0-01755d1` از همان کد ساخته، با
SHA-256 سنجیده و از بسته‌های قفل‌شدهٔ محلی در محیط مجازی تازه و تغییرناپذیر نصب شد. جابه‌جایی
انتشار زیر حفاظت زمان‌سنج پانزده‌دقیقه‌ای بازگشت انجام گرفت. API هوش مصنوعی و اتصال‌دهنده روی
`nextops-0.1.0-cdde129` مانده‌اند؛ مدل و محیط اجرای CPU، طرح پایگاه داده، Zabbix و بسته‌های سیستم
تغییر نکردند. ورود تازه و آزمون زندهٔ API، سلام فارسی و انگلیسی، پایش Zabbix، توضیح نداشتن دسترسی
به نام فایل‌های سیستم، ظرفیت نقاط اتصالِ مجاز، زمان و هش شاهد و شناسهٔ ممیزی را تأیید کرد. مرورگر
تازهٔ Edge نیز پنل ساده‌شده، پاسخ متمرکز، چیدمان راست‌به‌چپ موبایل، خروج در سرور، جداسازی برگه و
نبودِ درخواست بیرونیِ صفحه با پراکسی منع WAN را گذراند. سرویس برنامه، پایگاه و تونل‌ها فعال‌اند،
تمامیت فایل‌های انتشار برقرار است و زمان‌سنج بازگشت پس از پذیرش محدود خاموش شد. مجموعهٔ کامل
ارزیابی معنایی، تمرین بازگشت همین انتشار، منع WAN سمت سرور و reboot ماشین‌ها برای این نسخه تکرار
نشده‌اند. دو اجرای آغازین ابزار مرورگر به‌سبب خواندن شناسهٔ ممیزیِ پنهان با `innerText` شکست خورد؛
اجرای اصلاح‌شده موفق بود. نبود منابع مستقل بازیابی و سایر ورودی‌های مالک همچنان مانع پذیرش تولید است.

نقطهٔ تاریخیِ پیش از این استقرار، ۴ مهر ۱۴۰۵ — تغییر `cdde129` خطر انتقال اطلاعات احراز هویت در پیِ پاسخ
تغییرمسیر HTTP را در ارتباط برنامه با AI و اتصال‌دهنده و نیز اتصال‌دهنده با Zabbix بست؛ اکنون
تغییرمسیر رد می‌شود و bearer یا توکن API به مقصد دیگر فرستاده نمی‌شود. آزمون بازگشتِ همین مرز،
۱۶۱ آزمون منتخب، بررسی نوع و قالب و هر پنج کار CI موفق بودند. انتشار برنامه، API استنتاج و
اتصال‌دهنده همگی `nextops-0.1.0-cdde129` هستند؛ مدل و محیط اجرای CPU تغییر نکرده‌اند. نشست تازهٔ
Edge با WAN مسدود، ورود، چیدمان فارسی و انگلیسی، پاسخ عمومی، پاسخ زندهٔ Zabbix با منشأ، خروج و
جداسازی برگه را گذراند. هر چهار مهمان اکنون ورود SSH با گذرواژه و ورود مستقیم root را رد می‌کنند
و کلید عمومی می‌خواهند؛ اتصال تازهٔ راهبر و تونل‌های تازهٔ برنامه آزموده شد. UFW میزبان AI که
پیش‌تر غیرفعال بود، اکنون با سیاست رد ورودی و اجازهٔ OpenSSH فعال است. این وضعیت فقط برای
ارزیابی کنترل‌شدهٔ کاربران پذیرفته شده، نه تولید. مالک تأیید کرد مقصد و آزمایشگاه مستقل بازیابی،
مجوز مصوب پروژه، مسیر اعلان و گیرندگان، جفت گواهی جایگزین و تأییدکنندگان نام‌دار در دسترس نیستند.

ممیزی بعدیِ منشأ بسته نشان داد Agent 2 روی برنامه، AI و اتصال‌دهنده پس از رسیدن سرور زبیکس به
`7.0.31` هنوز `7.0.30` بود. هر سه عامل به‌ترتیب از بستهٔ آفلاینِ موجود و بررسی‌شده با هش به
`7.0.31` ارتقا یافتند؛ تنظیمات ثابت و نسخهٔ دقیق پیشین برای بازگشت نگه داشته شد. اکنون عامل هر
چهار مهمان `7.0.31` و فعال است؛ شنوندهٔ منفعل، واحد خراب، بستهٔ در انتظار یا نشانگر reboot وجود
ندارد. پس از تغییر، مرورگر تازهٔ دوزبانه و پایش با WAN مسدود دوباره موفق شد. چون سه عامل منشأ apt
پیکربندی‌شده ندارند، نسخهٔ بعدی باید آگاهانه و آفلاین وارد شود؛ صفر بودن `apt list --upgradable`
به‌تنهایی کافی نیست.

مرز ادعای شبکه: آزمون تاریخی قطع WAN چهار مهمان از قاعدهٔ خروجی nftables موقت استفاده کرده بود
که پس از آزمون حذف شد. اکنون HTTPS مستقیمِ IPv4 عمومی از پوستهٔ مدیریتی هر چهار مهمان در دسترس
است. واحدهای برنامه، API هوش مصنوعی و مدل همچنان خروجی IP را به loopback محدود می‌کنند.
اتصال‌دهنده نیز در مرز فرایند، جز loopback و شبکهٔ داخلیِ بررسی‌شده را رد می‌کند: چهار درخواست
تازهٔ رخداد و آزمون منفیِ کنترل‌شدهٔ خروجی عمومی موفق بودند. منع ماندگار خروجی **کل میزبان**
هنوز ناقص است و پیش از استقرار محافظت‌شده به فهرست معتبر مقصدهای DNS، زمان و پراکسی نگه‌داری
نیاز دارد.

به‌روزرسانی ۴ مهر ۱۴۰۵ — مالک دامنهٔ سخت‌سازی تولید و بازیابی را دوباره فعال کرد. به‌روزرسانی
بسته‌های چهار مهمان سرویس‌دهنده به‌صورت ترتیبی و همراه امکان بازگشت انجام شد. پیش از هر تغییر،
بسته‌های نصب‌شده با همان نسخه بازسازی و بسته‌های نامزد همراه فهرست SHA-256 در پوشهٔ محافظت‌شدهٔ
هر میزبان نگه‌داری شدند؛ پیش از تغییر دو میزبان پایگاه نیز dump محلی PostgreSQL ساخته و امکان
خواندن آن تأیید شد. اکنون هر چهار مهمان `running` هستند، واحد خراب و بستهٔ در انتظار ندارند و
نیازی به reboot گزارش نمی‌شود. Zabbix به `7.0.31` رسید و هر دو PostgreSQL روی `16.15` ماندند.
این dumpها و بسته‌های محلی فقط حفاظ تغییرند و پشتیبان مستقل بازیابی بحران نیستند.

در نقطهٔ نگه‌داری بسته‌ها، انتشارهای فعال برنامه، هوش مصنوعی و اتصال‌دهنده عوض نشده بودند. یک نشست تازهٔ Edge با WAN عمومی
مسدود، ورود، چیدمان چپ‌به‌راست انگلیسی و راست‌به‌چپ فارسی، هوش مصنوعی عمومی محلی، پایش مستند به
شاهد، شناسه‌های منشأ، خروج و لغو نشست در سرور و الزام ورود در برگهٔ تازه را گذراند. اجرای نخست یک
رقابت زمانی در ابزار پذیرش را آشکار کرد: پیش از پایان درخواست ناهمگام لغو نشست، نمای ورود بررسی
می‌شد. ابزار اکنون منتظر تغییر رابط می‌ماند و پاسخ واقعی `204` خروج را الزام می‌کند؛ تکرار زنده
موفق بود. بررسی مستقیم احرازهویت‌شده نیز مرتبط‌بودن سلام، هدایت پرسش وضعیت جاری، پایش محدود به
شاهد و پاسخ جایگزین ایمن رخداد ترکیبی را حفظ کرد.

شاهد زنجیرهٔ تأمین بدون تغییر وابستگی اجرا پیش رفت. Syft نسخهٔ `1.52.0` پس از تطبیق با digest
منتشرشده، همان بایگانی مستقر برنامه را بررسی کرد؛ خروجی‌های SPDX و CycloneDX به‌ترتیب ۲۷ بسته و
۲۶ مؤلفه ثبت کردند. ورودی تولیدی `pip-audit 2.10.1` شامل ۲۵ وابستگی بود و یافتهٔ شناخته‌شده‌ای
گزارش نکرد. این نتیجه پویش کامل سیستم‌عامل و محیط اجرا نیست. موجودی همچنین نشان داد خود پروژهٔ
NextOps در مخزن و بسته مجوز اعلام‌شده ندارد؛ عامل نمی‌تواند این تصمیم حقوقی را به‌جای مالک بگیرد.
امضای انتشار، ریشهٔ اعتماد آفلاین مصوب، شاهد کامل آسیب‌پذیری و تأیید مسئول حقوقی و امنیتی بازند.

پذیرش تولید هنوز ممکن نیست. مقصد مستقل بازیابی و آزمایشگاه restore ایزوله وجود ندارد؛ بنابراین
نصب pgBackRest/restic و تمرین بازیابی روی مهمان سرویس‌دهنده به‌جای شاهد واقعی انجام نشد. مسیر
داخلی واقعی تحویل اعلان با گیرندگان نام‌دار، جفت گواهی تازهٔ صادرشده از CA و حضانت کلید نیز فراهم
نشده، مجوز پروژه تصمیم‌گیری نشده و مسئول انسانی تولید پروفایل محدود را امضا نکرده است. قرارداد
بازیابی مخزن تا دریافت این ورودی‌های بیرونی همچنان fail-closed می‌ماند.

نقطهٔ پیشین در ۴ مهر ۱۴۰۵ — بخش «صحت پاسخ» برای ارزیابی کنترل‌شدهٔ کاربران پذیرفته شد. انتشار برنامه
`nextops-0.1.0-2397581` و انتشار API هوش مصنوعی `nextops-0.1.0-fd3c353` در آن نقطه فعال بودند و نسخه‌های
تغییرناپذیر پیشین برای بازگشت حفظ شده‌اند. پاسخ عمومی به‌روشنی بدون شاهد زنده و دارای احتمال خطا
معرفی می‌شود؛ وضعیت فعلی زیرساخت از حافظهٔ مدل پاسخ داده نمی‌شود؛ و پاسخ زنده در لایهٔ داخلی و
بیرونی برچسب شاهد یکسان دارد. ادعای اجرای عملیات، علت ریشه‌ای بی‌پشتوانه، نبود نام منبع، پنهان‌شدن
شاهد قدیمی یا ناقص و تکرار طولانی پرسش، پیش از ذخیره با پاسخ قطعی و بومی‌سازی‌شده جایگزین می‌شوند.

هر پنج کار CI نهایی شامل کیفیت و واحد، PostgreSQL 16 و 17، fixture مرورگر و پویش راز موفق بودند.
گزارش خصوصی loopback هر هشت مورد فارسی و انگلیسی و بازبینی معنایی مهندسی را گذراند. مسیر زندهٔ
برنامه نیز مرتبط‌بودن پاسخ `Hi`، هدایت پرسش وضعیت فعلی، شاهد پایش، پاسخ جایگزین رخداد ترکیبی و لغو
فوری نشست آزمایشی را تأیید کرد. سپس Zabbix، اتصال‌دهنده، هوش مصنوعی و برنامه به‌ترتیب با kernel
`6.8.0-142` بالا آمدند؛ همه `running`، بدون واحد خراب، بدون هشدار تازه در journal سرویس و بدون
نشانگر reboot بودند. به‌روزرسانی‌های پایهٔ Ubuntu هنوز در انتظارند و چون مسیر مصوب بسته یا پراکسی
در این تغییر آماده نبود، دانلود نشدند؛ نامزد Zabbix 7.0.31 نیز نصب یا پذیرفته نشد.

در آن نقطه، مالک همهٔ کارهای پشتیبان، PITR، restore و بازیابی بحران را موقتاً کنار گذاشته بود. قرارداد مخزن و
شواهد تاریخی حفظ می‌شوند، اما تا بازگشت این دامنه هیچ بسته یا تمرین بازیابی اجرا نمی‌شود؛ بنابراین
پذیرش تولید ممکن نیست. میزبان SMTP نیز وجود ندارد. تشخیص گواهی و نمایش مسئله در Zabbix فعال است،
اما تحویل اعلان به بهره‌بردار همچنان پذیرفته‌نشده و هیچ مسیر ایمیلی ادعا نمی‌شود.

مرحلهٔ دو با انتشار تغییرناپذیر برنامه `nextops-0.1.0-eb57241` و انتشار اتصال‌دهنده
`nextops-0.1.0-e2dad3a` برای ارزیابی کنترل‌شدهٔ کاربران مستقر شده است. بهره‌بردار احرازهویت‌شده
می‌تواند یکی از چهار مقصد منطقی و ازپیش‌تعریف‌شده را برگزیند
و توضیحی ماندگار به فارسی یا انگلیسی دریافت کند که هم به تاریخچه و رویدادهای محدود Zabbix و هم به
تصویر مستقیم و فقط‌خواندنی Linux مستند است. اعتبارنامهٔ مقصد به مدل یا مرورگر نمی‌رسد و مجوزدهی،
انتخاب مقصد، فرمان اجباری، هش شواهد و ممیزی خارج از مدل و به‌صورت قطعی اعمال می‌شوند.

بررسی زندهٔ API به هر دو زبان، گردآوری مستقیم Linux و مسیر ترکیبی اتصال‌دهنده برای هر چهار مقصد،
رد درخواست بدون احرازهویت و مقصد ناشناخته، راه‌اندازی مجدد سرویس‌ها، بازگشت انتشار و مسیر سرور/API
با WAN مسدود موفق بودند. اکنون مرورگر کامل و احرازهویت‌شده با اعتبارسنجی عادی TLS و WAN مسدود،
قطع و بازیابی اتصال‌دهنده و reboot ترتیبیِ تازهٔ هر چهار VM نیز پذیرفته شده‌اند. هنگام قطع
اتصال‌دهنده، بررسی رخداد خطای امن `503` داد، اما دستیار عمومی محلی فعال ماند؛ پس از بازیابی نیز
بررسی تازه و ممیزی‌شده موفق شد. هر چهار مهمان در پایان `running`، بدون واحد خراب و بی‌نیاز از
reboot بودند. اجرای زنده، نقص مهلت مسیر رخداد در Nginx را آشکار کرد؛ مسیر اکنون سقف محدود
۱۸۰ثانیه‌ای و آزمون بازگشت دارد. پذیرش تولید همچنان تا پشتیبان مستقل، WAL/PITR، چرخش/بازگشت
گواهی، تحویل اعلان به بهره‌بردار و تأیید بازیابی بحران مسدود می‌ماند.

آمادگی کد و سند بازیابی اکنون مرز ادعای صریح دارد. ADR 0008 و پروفایل عمومیِ دارای schema برای
دو خوشهٔ PostgreSQL 16 برنامه و Zabbix مخزن‌های جداگانهٔ pgBackRest را انتخاب و restic را به
فایل‌های غیرپایگاهی مصوب محدود می‌کنند. CI مخزن مشترک دو پایگاه، فیلد عمومی شبیه راز، ورود داده یا
WAL پایگاه به restic و هر ادعای صلاحیت بدون مقصد مستقل، RPO/RTO و نگه‌داری مصوب، بستهٔ آفلاین
معتبر، بازیابی کلید و موفقیت آزمون‌های جدا، آفلاین و منفی را رد می‌کند. پروفایل عمداً معتبر اما
`BLOCKED` است؛ هیچ بسته یا job پشتیبان روی VMهای سرویس‌دهنده نصب نشده و آمادگی تولید ادعا نمی‌شود.

راهنمای جفت انگلیسی و فارسیِ موانع تولید، همهٔ تصمیم‌های بیرونی باقی‌مانده را به checklist مالک با
فرمان‌های امن دقیق، فیلدهای پروندهٔ خصوصی، شرط توقف و شاهد تحویل تبدیل کرده است. این راهنما میزبان
مستقل بازیابی و آزمایشگاه restore جدا را پیشنهاد، اهداف بازیابی و حضانت دونفرهٔ کلید را ثبت و
تحویل اعلان محلی، گواهی، زنجیرهٔ تأمین و تأیید نهایی را مشخص می‌کند. این فقط راهنمای بهره‌بردار
است و وضعیت هیچ دروازهٔ مسدود، ناقص یا اجرا‌نشده‌ای را به موفق تغییر نمی‌دهد.

increment بعدی سخت‌سازی، خروج صرفاً مرورگری را اصلاح کرد. مسیر `POST /api/v1/logout`
اکنون فقط همان نشست ماندگار PostgreSQL را زیر قفل سطر لغو می‌کند و یک رویداد ممیزیِ فقط‌افزودنی و
دارای شناسهٔ هم‌بستگی، بدون مادهٔ توکن، می‌نویسد. تکرار درخواست و توکن ناشناخته idempotent هستند و
نشست دیگر همان هویت معتبر می‌ماند. پنل آفلاین پیش از پاک‌کردن `sessionStorage` برای لغو سروری تلاش
می‌کند و پاک‌سازی محلی در حالت خطا نیز انجام می‌شود. commit `eb57241` هر پنج کار CI را گذراند و
انتشار تغییرناپذیر `nextops-0.1.0-eb57241` در API زنده و مرورگر دارای TLS عادی، خروج، رد توکن
قبلی، حفظ نشست دیگر، تکرار idempotent و وجود دقیقاً یک رویداد ممیزی پالایش‌شده را با موفقیت
آزمود. انتشار `nextops-0.1.0-54c8bb4` برای بازگشت باقی است.

increment محدود تشخیص انقضای گواهی بدون وابستگی شبکه‌ای زمان اجرا در استقرار کنترل‌شده پذیرفته
شد. commit `f540a9d` هر پنج کار CI را گذراند و تغییر `certificate-lifecycle-20260923-01`، checker
قطعی و timer ماندگار و سخت‌سازی‌شده را روی هر دو رابط TLS نصب کرد. امتیاز امنیتی هر دو سرویس
`2.7 OK` است؛ هویت checker فقط گواهی عمومی را می‌خواند و به کلید متعلق به root با mode برابر
`0600` دسترسی ندارد. هر دو گواهی زنده با سیاست ۹۰روزه تا ۲۴ اکتبر ۲۰۲۷ سالم‌اند؛ fixture یک‌روزه
و ورودی خراب خطاهای متمایز لازم را دادند. چهار item فعال و شش trigger برچسب‌دار Zabbix، نتیجهٔ
سرویس، وضعیت timer و نبود داده را پایش می‌کنند. قطع محافظت‌شدهٔ timer برنامه trigger را به مشکل
برد و بازیابی آن، دادهٔ تازه و حالت سالم را برگرداند. TLS عادی برنامه و HTTPS زبیکس با CA ثابت نیز
بدون درخواست بیرونی موفق‌اند. تا تحویل اعلان از مسیر مصوب بهره‌بردار و تمرین مشاهده‌شدهٔ
چرخش/بازگشت، دروازهٔ تولید همچنان ناقص است.

### جمع‌بندی کنترل‌شدهٔ مرحلهٔ ۱ در ۱۴۰۵/۰۷/۰۱

در کارزار `stage1-completion-20260922-01`، مرورگر تازه با WAN مسدود، بازگشت برنامه و فایل‌های
محیط اجرا/مدل، لغو درخواست و بازیابی ظرفیت، قطع وابستگی، مدل مفقود یا خراب، کمبود فضای ایزولهٔ
آماده‌سازی، بار پایدار پنج‌دقیقه‌ای و بازیابی منطقی و فقط‌سوکتی هر دو پایگاه PostgreSQL 16 با موفقیت
انجام شدند. ۹۸ درخواست از ۹۹ درخواست بار موفق بود، p95 برابر ۶٫۱۱۴ ثانیه ثبت شد و زمان‌بند از یک
درخواست فعال و یک درخواست در صف فراتر نرفت. هر چهار مهمان در پایان `running`، بدون واحد خراب و
بدون نیاز به راه‌اندازی مجدد بودند. جزئیات در
[گزارش تکمیل مرحلهٔ ۱](fa/STAGE_1_COMPLETION_REPORT.md) آمده است.

این نتیجه به‌معنای پذیرش تولید نیست. dumpهای منطقی دارای checksum بازیابی شدند، اما مقصدی که
استقلال آن از مهمان سرویس‌دهنده، DS-C/G10 و میزبان فیزیکی اثبات شده باشد وجود ندارد؛ بایگانی WAL،
PITR، مخزن فایل با restic و تأیید نهایی بازیابی بحران نیز باقی مانده‌اند. بخش‌های قدیمی‌تر این سند
سوابق مرحله‌ای هستند و این جمع‌بندی و مانیفست وضعیت انتشار بر ادعاهای آمادگی پیشین مقدم‌اند.

### نقطهٔ فعلی برای ارزیابی کنترل‌شدهٔ کاربران

مرحلهٔ دو در این نقطه برای ارزیابی کنترل‌شدهٔ کاربران مستقر است. قرارداد آن چهار شناسهٔ منطقی مقصد
را تنها از پیکربندی استقرار می‌گیرد، فقط خواندن‌های نام‌دار را می‌پذیرد و تاریخچه و رویداد Zabbix
و همهٔ دسته‌های عیب‌یابی Linux را محدود می‌کند. منشأ زنده، احرازهویت، نشان نتیجهٔ ناقص، گردآوری
مستقیم، پیوند ماندگار مدل و ممیزی، بازگشت انتشار، راه‌اندازی مجدد سرویس و قطع WAN در مسیر سرور/API
پذیرفته شدند. افزون بر fixture مرورگر، گردش کامل و احرازهویت‌شدهٔ سامانهٔ زنده، چیدمان فارسی RTL،
جداسازی نشست، reboot ترتیبی مرحلهٔ دو و قطع و بازیابی وابستگی نیز پذیرفته شده‌اند. گام بعدی، مهندسی
بازیابی مستقل است، نه افزودن قابلیت تازه به مرحلهٔ دو.

قرارداد سمت مخزن این نقطه در `deploy/recovery` با هشت آزمون متمرکز و کنترل CI پیاده شده است. حالت
ویژهٔ تولید با گزینهٔ `--require-qualified` اکنون مطابق طراحی شکست می‌خورد. ادامهٔ کار به مقصدی
مصوب و خارج از دامنهٔ خرابی مهمان، datastore و hypervisor سرویس‌دهنده نیاز دارد؛ پس از آن بسته‌های
دقیق آفلاین و تمرین واقعی بازیابی مستقل را می‌توان راستی‌آزمایی کرد.

برنامهٔ احرازهویت‌شده و پنل دوزبانه، در انتشار تغییرناپذیر `nextops-0.1.0-2397581` روی مهمان برنامه و پشت TLS خصوصی
و Nginx فعال‌اند. PostgreSQL 16 هویت و نشست برنامه را روی فضای ذخیره‌سازی مستقل و تأییدشده نگه
می‌دارد. مسیرهای راه‌اندازی اولیه و بازیابی، مستندات API و درگاه مستقیم برنامه از Nginx در دسترس
نیستند. هیچ‌یک از اعتبارنامه‌های سرویس هوش مصنوعی یا Zabbix به مرورگر تحویل نمی‌شود.

مهمان مستقل پایش اکنون Zabbix 7.0.30، PostgreSQL 16، Nginx/PHP-FPM و Agent 2 را اجرا می‌کند.
گذرواژهٔ مدیر پیش‌فرض عوض شده است. خوانشگر جداگانهٔ API به رابط کاربری دسترسی ندارد؛ فقط پنج روش
`host.get`، `item.get`، `problem.get`، `history.get` و `event.get` برایش مجاز است و تنها یک گروه
میزبان مصوب را می‌بیند. اکنون
دقیقاً چهار میزبان مصوب، یعنی Zabbix، برنامه، هوش مصنوعی و اتصال، در دامنهٔ دید آن هستند. یک روش
خواندن خارج از فهرست و یک روش نوشتنی هر دو رد شدند. توکن فقط روی مهمان اتصال نگه‌داری می‌شود.
اتصال نیز فقط از TLS معتبر استفاده می‌کند، پراکسی موروثی را کنار می‌گذارد و روی رابط محلی فقط
عملیات نام‌دارِ خلاصه و بافت رخداد محدود را ارائه می‌دهد؛ نشانی دلخواه، JSON-RPC عمومی، shell یا
عملیات نوشتنی در اختیار مصرف‌کننده نیست.

روی مهمان‌های برنامه، هوش مصنوعی و اتصال، بستهٔ دقیق Agent 2 با نسخهٔ
`1:7.0.30-1+ubuntu24.04` نصب است. هر مهمان PSK مستقل دارد و فقط بررسی فعال را به مسیر محدودشدهٔ
Zabbix می‌فرستد. هیچ‌کدام روی درگاه ۱۰۰۵۰ گوش نمی‌دهند و `system.run[*]` صریحاً بسته است. در بررسی
نهایی خوانشگر، تعداد نقطه‌ای سنجه‌های تازه و پشتیبانی‌شده به‌ترتیب ۶۵، ۶۵ و ۵۸ بود؛ این اعداد
مشاهدهٔ همان لحظه‌اند، نه قرارداد ثابت template. مخزن بسته تازه نشد و ارتقای نامرتبطی انجام نشد.
وضعیت هر چهار میزبان `running` و شمار واحد خراب صفر باقی ماند.

برنامه از دو تونل SSH جدا با کلید میزبان ثابت‌شده به سرویس‌های محلی هوش مصنوعی و اتصال می‌رسد.
صلاحیت‌سنجی زنده، هشت سنجهٔ تازهٔ خودپایشی، بدون سنجهٔ قدیمی و بدون مسئلهٔ فعال بازگرداند. آزمون
سراسری از رایانهٔ کاربر، TLS، ورود و نشست، دریافت شاهد و پاسخ مستند فارسی و انگلیسی را با موفقیت
گذراند. زمان تولید با سقف ۱۲۸ توکن برای انگلیسی ۵۶٫۶ ثانیه و برای فارسی ۶۷٫۱ ثانیه بود. نمایش
انگلیسی و چیدمان راست‌به‌چپ فارسی نیز به‌صورت دیداری بازبینی شد. نسخهٔ منبع، میزبان، زمان گردآوری،
زمان اندازه‌گیری، وضعیت تازگی و شمار مسئله‌های فعال کنار پاسخ نمایش داده می‌شود.

نخستین درخواست واقعی مرورگر، ناسازگاری میان درخواست ۳۸۴ توکنی پنل و مهلت تأییدشدهٔ ۱۲۰ ثانیه‌ای
پردازش روی CPU را آشکار کرد. با وجود سلامت آمادگی و پایش، درخواست در پایان به خطای عمومی `503`
رسید. اصلاح مستقرشده سقف بررسی زنده را در سرور و پنل به ۱۲۸ توکن محدود می‌کند، وضعیت امن پایان
مهلت و اشباع را در مرز داخلی حفظ می‌کند و پیام خطای روشن و بومی‌شده نشان می‌دهد. بازاجرای همان
پرسش `hi` با payload قدیمی ۳۸۴ توکنی، در ۶۱٫۶ ثانیه با HTTP 200، شاهد زنده و ۱۲۸ توکن خروجی موفق
شد. انتشار تغییرناپذیر قبلی نیز برای بازگشت نگه‌داری می‌شود.

این بازآزمایی، ترمیم مسیر فنی را ثابت کرد؛ اما یک اشکال جدا در ارتباط معنایی پاسخ را نیز نشان داد:
پنل همهٔ پرسش‌ها را به `/api/v1/investigate` می‌فرستاد و به همین دلیل حتی `Hi` با گزارش Zabbix
پاسخ داده می‌شد. در انتشار `nextops-0.1.0-3d61bf6`، **دستیار عمومی** حالت پیش‌فرض است و **پایش
زنده** فقط با انتخاب صریح کاربر فعال می‌شود. پرسش عمومی از مسیر `/api/v1/assistant/generate`
می‌گذرد، هیچ شاهد پایشی دریافت نمی‌کند و با نشان «مدل محلی، بدون شاهد زنده» نمایش داده می‌شود؛
مسیر پایش همچنان پاسخ را به شواهد Zabbix مستند می‌کند. درخواست دقیق `Hi` در حالت پیش‌فرض طی ۱۴٫۰
ثانیه پاسخ “Hello! How can I assist you today?” گرفت و هیچ اشاره‌ای به Zabbix یا وضعیت سامانه
نداشت. سلام فارسی نیز پاسخ عمومی فارسی و بدون محتوای پایشی دریافت کرد. آزمون بازگشت پایش زنده با
هشت سنجهٔ تازه و پاسخ مستند انگلیسی و فارسی موفق بود. انتشار `8d31bcb` برای بازگشت محفوظ است.

انتشار `nextops-0.1.0-fde27bd` پیوند ماندگارِ باقی‌مانده از 1D را بدون migration تازه تکمیل می‌کند.
مسیر `/api/v1/investigate` پیش از فراخوانی اتصال یا مدل، اجرای محدود به دامنه را در PostgreSQL
می‌سازد. هنگام موفقیت، خلاصهٔ ازپیش‌محدودشدهٔ Zabbix، مرجع SHA-256 شاهد، نتیجهٔ مدل و رخداد تکمیل
ممیزی به‌صورت اتمی ثبت می‌شوند. در حالت شکست نیز فقط کد و کلید پیام امن ذخیره و ممیزی می‌شود و
خطای خام وارد پایگاه نمی‌شود. پنل شناسهٔ اجرا، شاهد و ممیزی را نمایش می‌دهد و بازیابی
احرازهویت‌شدهٔ اجرا همان نتیجهٔ محدود به دامنه را برمی‌گرداند. هر ۹۵ آزمون غیر‌یکپارچه و شش آزمون
PostgreSQL در پایگاه موقت و جداگانه موفق بودند. آزمون زنده هشت سنجهٔ تازه، بدون مسئلهٔ فعال و پاسخ
۱۲۸ توکنی را در ۵۷٫۲ ثانیه بازگرداند؛ بازیابی نتیجه، محاسبهٔ مستقل هش و پیوند ممیزی نیز موفق بود.
بررسی مستقیم پایگاه، نتیجهٔ `live_monitoring`، دو رویداد ممیزی پیوندخورده، هش ۶۴ نویسه‌ای و تطبیق
شناسهٔ ممیزی تکمیل با نتیجهٔ ذخیره‌شده را تأیید کرد.

در صلاحیت‌سنجی خطای مرحلهٔ 1E، انتشار `nextops-0.1.0-3d7d725` برای اتصال‌دهنده و
`nextops-0.1.0-13a3369` برای برنامه فعال شد. `MonitoringSummary` اکنون با `is_partial` و دلیل‌های
دارای نوع، ناقص‌بودن شاهد را اعلام می‌کند. نمای زندهٔ هشت‌سنجه‌ای فعلی دلیل `metrics_truncated`
دارد و در عین حال قدیمی‌بودن هر اندازه‌گیری را جداگانه نگه می‌دارد. در مرز پرامپت نیز نام میزبان،
سنجه، مقدار، واحد و مسئله، حتی با منبع احرازهویت‌شده، فقط دادهٔ غیرقابل‌اعتمادند. آزمون‌های جداشده
برای مقدار قدیمی، شاهد ناقص یا بدون سنجهٔ قابل‌استفاده، متن بیش‌ازحد بلند و دستور جاسازی‌شده موفق
بودند.

یک توکن موقت متعلق به همان هویت خوانشگر، فقط چهار میزبان مصوب را دید؛ بلافاصله پس از لغو از
دسترسی افتاد و حذف شد، بی‌آنکه توکن فعال تغییر کند. هنگام قطع کوتاه رابط HTTPS و API زبیکس، خلاصه
و بررسی زنده خطای امن و قابل‌تکرار `503` با کلید `connector.summary_unavailable` برگرداندند. اجرای
ناموفق و رویداد ممیزی آن ماندگار شد و هم‌زمان پاسخ‌گویی عمومی و بدون شاهد مدل محلی ادامه یافت.
پس از بازگشت رابط، دریافت دادهٔ تازه برقرار شد و بررسی زندهٔ بعدی، نشان ناقص‌بودن و هش مستقلِ
تأییدشدهٔ شاهد را طی ۶۷٫۹ ثانیه حفظ کرد. توقف موتور Zabbix به‌تنهایی API مبتنی بر PHP را قطع نکرد؛
این تفاوت برای عملیات مهم است. Ruff، mypy سخت‌گیرانه، ۱۰۲ آزمون غیر‌یکپارچه و شش آزمون PostgreSQL
در پایگاه جداگانه موفق‌اند.

این خروجی برای ارزیابی کنترل‌شده است، نه پذیرش تولید. هر چهار مهمان مصوب مرحلهٔ یک پایش می‌شوند،
اما دامنهٔ گسترده‌تر تجهیزات هنوز وارد نشده است. آزمون صریح قطع WAN در مسیر سرور و API موفق بود:
هنگامی که دسترسی مستقیم IPv4 و IPv6 هر چهار مهمان به اینترنت بسته بود، ورود تازه، پاسخ عمومی فارسی
و انگلیسی، آمادگی مدل محلی، دریافت شاهد تازه و پیوند ثبت و ممیزی برقرار ماند. پس از اصلاح ترتیب
خاموش‌شدن پایگاه Zabbix و ترتیب آغاز پایگاه برنامه، هر چهار مهمان یکی‌یکی و زیر سیاست قطع زودهنگام
WAN راه‌اندازی مجدد شدند، با وضعیت `running` و صفر واحد خراب بازگشتند و آزمون سلامت نقش خود را
گذراندند. جداسازی مستقل مرورگر، انقضای گواهی، پایان مهلت یا لغو درخواست، کمبود فضا، بار پایدار،
پشتیبان مستقل، بازیابی و سناریوی بحران همچنان بازند. نشانی‌ها، توکن‌ها، گذرواژه‌ها، کلیدهای میزبان و
شواهد خام بیرون Git مانده‌اند.

### نیازها و سابقهٔ محفوظ

remote بررسی‌شدهٔ مستقیم Git برابر `Omid-NextAI/nextops` و شاخه `main` است. فرمان‌های clone جاری در README و راهنمای نصب اکنون remote درست را دارند؛ رکوردهای تاریخی `AmirMo10/nextops` حفظ می‌شوند و عنوان پرامپت فعال هنوز به اصلاح جداگانه و نسخه‌دار نیاز دارد. مالک مستندات فارسی طبیعی و انگلیسی، یک پرامپت فعال انگلیسی، AI محلی روی CPU، ادامهٔ کار پس از قطع اینترنت، پاسخ وضعیت Zabbix در اولین تحویل، برنامهٔ ماشین‌ها و محدودیت ذخیره‌سازی و سرور مستقل Zabbix را خواسته است. یازده اتصال و ۵۱ بخش مشخصات اولیه در دامنه باقی‌اند.

[پرامپت فعال ۳.۰](requirements/NEXTOPS_MASTER_PROMPT.md) و [بایگانی نسخهٔ ۲](requirements/archive/NEXTOPS_MASTER_PROMPT_v2.0.md) در این تغییر دست‌نخورده‌اند. [اصلاحیهٔ استقرار](requirements/DEPLOYMENT_UPDATE.md) فقط پیشنهاد آزمایشگاه کوچک و مجموع منابع وابسته را صریح جایگزین می‌کند؛ سایر نیازهای امنیت، پذیرش و قابلیت‌ها پابرجا هستند. مشخصات فارسی اولیه همچنان در بایگانی محفوظ است.

نخستین خروجی، پاسخ تازهٔ فارسی یا انگلیسی دربارهٔ وضعیت مجاز Zabbix بود که روی CPU محلی، مستند به دادهٔ واقعی و همراه منبع و زمان و دامنه و ممیزی با اینترنت قطع تولید شد. مرحلهٔ دو اکنون عیب‌یابی Linux برنامه‌ریزی‌شده را فراهم می‌کند. انتشار مستندات به‌تنهایی پایان مرحلهٔ نرم‌افزاری یا اثبات مجوز استقرار نیست.

[گزارش مرحلهٔ صفر انگلیسی](en/PHASE_0_REPORT.md)، [نسخهٔ فارسی](fa/PHASE_0_REPORT.md) و [مدل تهدید](requirements/nextops-threat-model.md) یافتهٔ مخزن، معماری چهارماشینی پذیرفته‌شده، مرز اعتماد، قرارداد ماژول و داده، برنامهٔ سنجش CPU، بودجه، نقشهٔ اتصال، آزمون و گام‌های 1A را ثبت می‌کنند. مالک در ۲۱ سپتامبر ۲۰۲۶ مرحلهٔ صفر و ADRهای 0001 تا 0006 را با تک‌سازمانی بودن فعلی، مقیاس کوچک اولیه با رشد آینده و Zabbix مستقل پذیرفت. همهٔ مجوزهای زیرساخت جدا و در انتظار باقی می‌مانند.

Incrementهای 1 و 2 از 1A در کد مخزن پیاده شده‌اند: قرارداد سخت‌گیر، سیاست رد، FastAPI، هویت Argon2id، نشست hash‌شده، PostgreSQL/Alembic، اجرای ماندگار، lease، ممیزی فقط‌افزودنی و پنل دوزبانه. سازمان، محیط، role و scope از نشست سمت سرور ساخته می‌شوند. چهار اسکریپت محافظت‌شده فقط لایهٔ بستهٔ Ubuntu را تعریف می‌کنند و installer کامل محصول نیستند. انتشار تغییرناپذیر برنامه، TLS خصوصی و اتصال‌دهنده در محیط کنترل‌شده جداگانه فعال‌اند؛ بستهٔ کامل و بازتولیدپذیر تولید هنوز وجود ندارد. محیط اجرا و مدل ثابت هوش مصنوعی در ادامه ثبت شده‌اند.

Increment 3 از 1B قرارداد مستقل و سخت‌گیر `LLMProvider`، API احرازهویت‌شده، رابط فقط‌محلی llama.cpp، صف با یک درخواست فعال و دو درخواست در انتظار، کران ورودی و خروجی و زمان، پاک‌سازی لغو و خطاهای ساخت‌یافته را فراهم می‌کند. پروندهٔ YAML معتبرشده، llama.cpp نسخهٔ `v0.4.1` و فایل رسمی `Qwen3-8B-Q4_K_M.gguf` را تثبیت می‌کند. کیفیت زنده، راه‌اندازی مجدد، بازگشت برنامه/محیط اجرا/مدل، لغو و قطع وابستگی، artifact خراب یا مفقود، بار محدود پنج‌دقیقه‌ای، قطع WAN و مرورگر تازه شاهد دارند. پشتیبان مستقل و PITR همچنان دروازهٔ تولیدند.

برش بومی 1B دو واحد جدا و سخت‌سازی‌شدهٔ `nextops-llama` و `nextops-ai`، دو اعتبارنامهٔ فایل‌محور، محدودیت شبکه به رابط محلی در سطح cgroup، درخت انتشار فقط‌خواندنی، سقف صریح منابع، بارگذاری سخت‌گیرانهٔ اعتبارنامه و مجموعهٔ نسخه‌دار سنجش فارسی و انگلیسی را فراهم می‌کند و اکنون روی مهمان هوش مصنوعی فعال است. نخستین اجرا، مسیر نادرست کتابخانه‌های مشترک پس از جابه‌جایی و ناکافی بودن بررسی صرفِ باز شدن درگاه را آشکار کرد؛ واحد اصلاح‌شده از مسیر ثابت و محافظت‌شدهٔ کتابخانه‌ها استفاده می‌کند و شروع کنترل‌شده تا سلامت احرازهویت‌شدهٔ مدل منتظر می‌ماند. حساب استقرار بنا بر دستور مالک اکنون مدیریت کامل و بدون گذرواژه دارد؛ ورود مستقیم root از راه SSH همچنان بسته است.

### شواهد ارسالی سخت‌افزار و دیسک

[رکورد سخت‌افزار](requirements/HARDWARE_BASELINE.json) خروجی ESXCLI مالک را حفظ می‌کند: ESXi 8.0.3 با ساخت 24414501، چهار بستهٔ پردازنده، ۱۱۲ هسته، ۲۲۴ رشته، Hyperthreading فعال، چهار گرهٔ NUMA و حافظهٔ ۱٬۴۴۲٬۷۴۳٬۶۳۱٬۸۷۲ بایت، تقریباً ۱۳۴۳٫۶۶ GiB. نمونهٔ ناقص CPU 0 و 1، سرعت و cache و microcode ارسالی و نگاشت‌های مرجع در [یادداشت ESXi](fa/ESXI_BASELINE.md) ثبت‌اند. مدل تجاری دقیق، فرکانس اسمی، یکسان بودن همهٔ بسته‌ها، ISA مهمان و توزیع واقعی گره‌ها از نمونه ثابت نمی‌شوند. میانگین حسابی، توپولوژی یا ظرفیت آزاد مشاهده‌شده نیست.

ظرفیت لحظه‌ای VMFS ارسالی: DS-A برابر ۱۴۹٫۷۵ GiB کل و ۱۴۸٫۳۴ آزاد؛ DS-B برابر ۱۱۱۷٫۵۰ و ۱۱۰۹٫۸۷؛ DS-C برابر ۳۵۷۶٫۷۵ و 3166.8701171875. نام واقعی، UUID و مسیر در رکورد عمومی نیستند. [برنامهٔ دیسک](STORAGE_PLAN.md) حجم‌های سیستم و راه‌اندازی را کنار می‌گذارد، DS-A و DS-B را تخصیص نمی‌دهد و سقف سه‌ترابایتی را حفظ می‌کند. هدف پیشنهادی فضای آزاد DS-C برابر ۲۵ درصد، دقیقاً 894.1875 GiB و با گردکردن حدود ۹۰۰ GiB است. فهرست ارسالی، رزرو، سلامت RAID یا سنجش I/O نیست.

ESXi حفظ شود؛ Ubuntu Server 24.04 LTS خط مبنای تأییدشدهٔ مهمان است، نه جایگزین میزبان. مجموع‌ها و نسخه و فهرست دوباره به‌عنوان دادهٔ غایب خواسته نشوند. CPU/RAM آزاد فعلی، بار و رزرو، جای‌گذاری فیزیکی NUMA، سازگاری و محدودیت مجوز، سلامت و تأخیر دیسک، رشد و محل swap باید هنگام اجرا بررسی شوند. اتصال مستقیم به میزبان ESXi یا تأیید سازگاری انجام نشده است.

### صلاحیت‌سنجی پاک‌سازی‌شدهٔ مهمان‌های جایگزین

در ۲۱ سپتامبر ۲۰۲۶، پس از ارسال مستقل اثرانگشت‌های تازهٔ Ed25519 توسط مالک و برابری هرکدام با ارتباط زنده، پیش‌بررسی فقط‌خواندنی مجاز از راه SSH به هر چهار مهمان جایگزین رسید. احراز هویت فقط با کلید، کنترل سخت‌گیرانهٔ کلید میزبان و رد ورود مستقیم root تأیید شد و منابع هر نقش با بودجهٔ عمومی برابر بود. در ۲۲ سپتامبر، پس از استقرار هوش مصنوعی و یک به‌روزرسانی محدود امنیتی GLib روی مهمان برنامه، همهٔ مهمان‌ها دوباره بررسی شدند: وضعیت systemd در هر چهار مورد `running`، شمار واحد خراب و بستهٔ قابل‌ارتقا صفر و راه‌اندازی مجدد لازم نبود. UFW روی مهمان‌های برنامه، اتصال و Zabbix فعال و روی مهمان هوش مصنوعی غیرفعال است؛ اصلاح این ناهمگونی یک کار سخت‌سازی جداگانه است. درگاه‌های هوش مصنوعی همچنان فقط روی رابط محلی‌اند. تغییر بعدی پایش، یک شنوندهٔ دریافت داده را روی رابط خصوصی Zabbix با سه قاعدهٔ دیوارهٔ آتشِ مختص مبدأ افزود؛ سه مهمان NextOps هیچ شنونده‌ای اضافه نکردند و شنوندهٔ عمومی محصول وجود ندارد.

پس از مجوز صریح مالک برای آماده‌سازی متصل، هر میزبان از زنجیرهٔ پراکسی سخت‌گیرانهٔ موجود برای تازه‌سازی مخزن‌های امضاشده و نصب فقط لایهٔ بستهٔ نقش خود استفاده کرد. ارتقای کلی سیستم‌عامل اجرا نشد. نسخه‌های مستقیم مشاهده‌شده عبارت‌اند از PostgreSQL 16.15 و Nginx 1.24 در برنامه؛ GCC 13.3، CMake 3.28، Ninja 1.11 و OpenBLAS 0.3.26 در هوش مصنوعی؛ پشتیبانی محیط مجازی Python 3.12 در connectors؛ و Zabbix 7.0.30، PostgreSQL 16.15، Nginx 1.24 و PHP 8.3.6 در Zabbix. بستهٔ راه‌انداز رسمی Zabbix 7.0 برای Ubuntu 24.04 پیش از افزودن مخزن با SHA-256 ثابت شد. شروع خودکار پس از نصب مسدود بود و در همان نقطهٔ آماده‌سازی، همهٔ سرویس‌های محصول، پایگاه و وب غیرفعال بودند، خوشهٔ PostgreSQL ساخته نشده بود و درگاه تازه‌ای باز نشد. پس از آن، برش‌های برنامه و پایگاه و پراکسی، هوش مصنوعی، اتصال و Zabbix به‌صورت کنترل‌شده تنظیم و فعال شدند و سپس تغییر محدود پوشش چهارمیزبانی Agent 2 اجرا شد. Docker نصب نشد، چون طراحی بومی systemd به آن نیاز ندارد و سوکت کانتینر مرز اعتماد را بزرگ می‌کند.

هویت‌های بدون ورود و مسیرهای محافظت‌شدهٔ نقش ساخته شده‌اند. llama.cpp با Release، اجرای بومی CPU، OpenMP و OpenBLAS و بدون GPU ساخته شد و مدل ۵٬۰۲۷٬۷۸۳٬۴۸۸ بایتی با SHA-256 مصوب برابر است. در آن نقطه، انتشار فعال API، `nextops-0.1.0-fd3c353` بود و `nextops-0.1.0-62de8d6` و `417d888` انتشارهای محافظت‌شدهٔ پیشین بودند. توقف و شروع سرد، بازگشت برنامه و artifact، لغو، قطع وابستگی، مدل خراب/مفقود و تولید پس از بازیابی موفق بودند. در بار پنج‌دقیقه‌ای، ۹۸ درخواست از ۹۹ درخواست موفق، p95 برابر ۶٫۱۱۴ ثانیه و بیشینهٔ زمان‌بند یک فعال/یک صف بود. هر دو سرویس فقط روی CPU و `127.0.0.1:8080` و `127.0.0.1:8090` اجرا می‌شوند و امتیاز systemd آن‌ها `2.7 OK` است. شواهد خام و رازها بیرون Git مانده‌اند. مجوز وابستگی‌ها و تأیید تولید بازند و کار بازیابی به درخواست مالک کنار گذاشته شده است.

### چیدمان فعلیِ پیشنهادی

برنامهٔ NextOps همان ۸ vCPU و ۳۲ GiB و ۲۰۰ GiB؛ AI همان ۲۴ و ۱۲۸ و ۵۰۰؛ اتصال همان ۴ و ۸ و ۸۰ است. **سرور مستقل `zabbix-server` با ۴ vCPU، حافظهٔ ۱۶ GiB و دیسک ۲۰۰ GiB پیش از اتصال زندهٔ 1C** اضافه می‌شود. پایگاه NextOps از مرحلهٔ سه با ۸ و ۶۴ و ۳۰۰ پیشنهاد می‌شود؛ اجرای تغییر فقط در مرحلهٔ هفت و با مجوز، ۴ و ۱۶ و ۸۰ است.

سرور Zabbix پایگاه پایش، رابط و API خودش را دارد، نه مدل یا پایگاه NextOps. در مسیر جدید، جایگزین آزمایشگاه ۴ vCPU و ۸ GiB و ۱۰۰ GiB می‌شود؛ هر دو ساخته نشوند. Zabbix محلی موجودِ مناسب و مجاز ابتدا بررسی و استفاده شود. تعداد ماشین‌های خود NextOps همچنان ۳، ۴ و ۵ و مجموع شامل پایش ۴، ۵ و ۶ است.

چیدمان اولیه **۴۰ vCPU، حافظهٔ ۱۸۴ GiB و دیسک ۹۸۰ GiB** دارد؛ با سهم موقت ESXi swap برابر ۱۸۴ GiB، جمع پیش از سربار **۱۱۶۴ GiB** است. چیدمان‌های بعدی به‌ترتیب ۴۸ و ۲۴۸ و ۱۲۸۰، با جمع ۱۵۲۸ GiB؛ و ۵۲ و ۲۶۴ و ۱۳۶۰، با جمع ۱۶۲۴ GiB هستند. با مصرف قبلی ثابت، فضای آزاد فرضی DS-C برابر ۲۰۰۲٫۸۷، ۱۶۳۸٫۸۷ و ۱۵۴۲٫۸۷ GiB می‌شود. این‌ها بودجه‌های جایگزین‌اند، نه جمع‌شونده، رزرو، سنجش یا مجوز مصرف همهٔ فضا. رشد، VMX، snapshot، ورود فایل و بازیابی جدا و ماشین موجود بدون دوباره‌شماری حساب شوند.

راهنمای [فارسی](fa/ZABBIX_SERVER.md) و [انگلیسی](en/ZABBIX_SERVER.md) نرم‌افزار پیشنهادی Zabbix 7.0 LTS، PostgreSQL 16، Nginx، PHP-FPM و Agent 2، چیدمان کامل `vg_zabbix`، پیشنهاد history هفت‌روزه و trends عددی نودروزه، هویت API محدود، خودپایشی، پذیرش آفلاین و خطر تک‌میزبان را ثبت می‌کنند. بستهٔ دقیق، تنظیم نگهداری و VM/LVM از طریق این مستندات نصب یا آزموده نشده‌اند. اعداد پیشنهادی در [رکورد Zabbix](requirements/ZABBIX_SERVER_PLAN.json) جدا از شاهد سخت‌افزار آمده‌اند.

### پروندهٔ هر سرور برای مسئول استقرار

[مشخصات پرونده](requirements/SERVER_DEPENDENCY_DOSSIER_SPEC.md)، [JSON Schema مشترک](../deploy/server-dependencies/server-dependency.schema.json) و چهار فایل YAML خوانا برای `nextops-app`، `nextops-ai`، `nextops-connectors-ro` و `zabbix-server` اکنون تحویل ماشین‌خوان هر سرور را فراهم می‌کنند. راهنمای [فارسی](fa/DEPLOYMENT_DOSSIERS.md) و [انگلیسی](en/DEPLOYMENT_DOSSIERS.md) روش تکمیل ورودی خصوصی بدون commit آن را شرح می‌دهند.

هر پرونده وضعیت مجوز، منبع، منابع VM، هویت سرویس، قفل نرم‌افزار و artifact، مسیر تنظیمات، secret reference، مرز شبکه و storage، ترتیب سرویس، فرمان فقط‌خواندنی یا الگوی محافظت‌شده، فرمان مسدود، مشاهده‌پذیری، backup و rollback، ورودی لازم، دروازهٔ پذیرش و محدودیت را دارد. مقدارهای معلوم با مجموع ۴۰ vCPU، حافظهٔ ۱۸۴ GiB و دیسک ۹۸۰ GiB سازگارند و mountهای Zabbix با طرح ۲۰۰ GiB تطبیق دارند. تبدیل درخواستی JSON به YAML همهٔ مقدارها را بدون اتلاف حفظ کرد. اعتبارسنج مخزن چهار فایل YAML را ایمن parse می‌کند، schema نسخهٔ ۱.۰.۰ و شناسه‌های پذیرفته‌شده را می‌سنجد، باقی‌ماندن نسخهٔ قدیمی JSON را رد می‌کند و مجموع منابع را تطبیق می‌دهد.

برای هر role یک script اجرایی در `deploy/installers` وجود دارد. موتور مشترک و آزموده، manifest همهٔ فایل‌های bundle را با SHA-256 جداگانه تطبیق می‌دهد، نسخهٔ دقیق همهٔ packageها و وابستگی‌ها را لازم می‌داند، APT را فقط به repository محلی امضاشده محدود می‌کند، نصب یا حذف پیش‌بینی‌نشده را رد می‌کند، شروع خودکار سرویس و ساخت خودکار cluster در PostgreSQL را می‌بندد و نسخهٔ نصب‌شده را می‌سنجد. `--apply` علاوه بر این به root، Ubuntu 24.04 روی VMware، bundle متعلق به root و غیرقابل‌نوشتن برای دیگران، نشان مجوز و change ID نیاز دارد. حالت check فقط bundle را بررسی می‌کند. هیچ lock واقعی package، کلید امضا، bundle مخزن یا شاهد اجرای موفق روی سرور تمیز در این مخزن وجود ندارد.

این پرونده‌ها مانع را پنهان نمی‌کنند. برنامهٔ کنترل‌شده، PostgreSQL، پراکسی خصوصی، هوش مصنوعی،
اتصال، Zabbix و پایش چهار میزبان وجود دارند. مرورگر تازه، بازگشت artifact، خطاهای باقی‌مانده، بار
محدود و بازیابی منطقی هر دو پایگاه نیز شاهد زنده دارند. نصب‌کنندهٔ کامل تولید، مخزن مستقل
pgBackRest/WAL، مخزن restic، آزمون PITR و بستهٔ بازیابی بحران هنوز آماده نیستند. تنظیم خصوصی،
گواهی و اعتبارنامهٔ مقصد در محل محافظت‌شده باقی می‌مانند و پذیرش تولید تکمیل نشده است.

### context ماندگار عامل

شش skill مخصوص مخزن در `.agents/skills`، context پروژه، عملیات سرور، مستندات دوزبانه، برنامه‌ریزی تغییر محدود، بازبینی پذیرش و بررسی انحراف مستندات را مسیردهی می‌کنند. [فهرست context Markdown](MARKDOWN_CONTEXT_INDEX.md) فایل‌های Markdown متعلق به پروژه را ثبت و نوع کار را به منبع مرتبط وصل می‌کند، بدون اینکه همهٔ مستندات هم‌زمان وارد context شوند. اعتبارسنج مستندات پوشه‌های وابستگی و build را حذف می‌کند و نبود یا قدیمی بودن ورودی فهرست را شکست می‌دهد؛ سه آزمون متمرکز نیز discovery و تطبیق فهرست را پوشش می‌دهند. این skillها ابزار توسعه‌اند، نه قابلیت برنامه، مرز مجوز یا مرز امنیت زیرساخت.

### گام‌ها و وضعیت شواهد

معماری و ADRهای مرحلهٔ صفر پذیرفته شده‌اند و چهار مهمان جایگزین از صلاحیت‌سنجی عبور کرده‌اند. برش کنترل‌شدهٔ 1A با برنامه، PostgreSQL، TLS و پنل دوزبانه فعال است؛ 1B مدل محلی را فراهم می‌کند؛ مسیر فقط‌خواندنی 1C فعال و آزموده است؛ و 1D شاهد محدود، اجرای ماندگار و ممیزی پیوندخورده دارد. گام 1E اکنون مرورگر تازه با WAN مسدود، بازگشت، لغو و قطع وابستگی، artifact مفقود/خراب، کمبود فضای ایزوله، بار پنج‌دقیقه‌ای و بازیابی منطقی جدا را نیز گذرانده است. پشتیبان مستقل، WAL/PITR و پذیرش تولید بازند.

ممکن است مالک مستقل ماشین ساخته باشد؛ پیش از ادعای وجود یا نبود آن، وضعیت واقعی بررسی شود. تصویر تنظیمات VM به معنای قبولی مسیر برنامه نیست. ادامه از نخستین گام ناتمامِ دارای شاهد و مجوز باشد، نه پاک کردن پیشرفت.

### دامنهٔ انتشار و کار بعدی

این وضعیت پذیرش مرحلهٔ صفر، برش‌های کنترل‌شدهٔ مرحلهٔ یک و مسیر مستقرشدهٔ بررسی رخداد با شواهد
فقط‌خواندنی Linux و Zabbix در مرحلهٔ دو را ثبت می‌کند. نیازهای منبع، پرامپت بایگانی‌شده، نمودارها
و پرونده‌های تحویل حفظ شده‌اند. این رکورد به‌معنای ممیزی امنیت میزبان، پذیرش تولیدی یا اثبات
بازیابی مستقل نیست.

برش‌های منبع با Python 3.12.10، uv 0.12.17 و زنجیرهٔ قفل‌شده آزموده شدند؛ Playwright 1.63 نیز
وابستگی صرفاً توسعه‌ای است. برای مرحلهٔ دو، Ruff، mypy سخت‌گیرانه، ۱۳۷ آزمون غیر‌یکپارچهٔ محلی
به‌همراه یک کنترل ویژهٔ POSIX، هر دو کار PostgreSQL 16 و 17 در CI، fixture واقعی مرورگر و پویش راز
موفق بودند. شاهدهای پیشین مرحلهٔ یک برای
مرورگر آفلاین، بازیابی خطا، بار و restore سابقه‌اند و به‌عنوان اجرای دوبارهٔ مرحلهٔ دو تلقی
نمی‌شوند. بررسی وابستگی و مجوز، پشتیبان مستقل/PITR و ارتقا به تولید همچنان دروازه‌اند.

نقطهٔ مهندسی بعدی در [کار بعدی](NEXT_TASK.md)، مهندسی بازیابی است؛ سه دروازهٔ پیش‌تر اجرا‌نشدهٔ
مرحلهٔ دو، یعنی مرورگر تازهٔ زنده، reboot ترتیبی و قطع و بازیابی وابستگی، اکنون بسته شده‌اند و
پیاده‌سازی پذیرفته‌شده نباید از نو ساخته شود. ارتقا به تولید تا تصویب مقصد پشتیبان مستقل، مخزن و WAL آگاه از
PostgreSQL، پشتیبان فایل مجاز، PITR مستقل، ثبت RPO/RTO و بازیابی کلید و تأیید عملیات متوقف می‌ماند.
