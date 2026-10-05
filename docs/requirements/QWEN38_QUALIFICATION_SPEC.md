# Qwen 3.8 qualification / پذیرش فنی Qwen 3.8

Status: bounded existing-guest trial, authorized by the owner's upgrade/resource instructions
on 2026-10-05. Not a serving-model selection, new production acceptance or permission to erase
other workloads. [CPU guide](../en/CPU_AI.md) / [راهنمای CPU](../fa/CPU_AI.md).

## English

### Problem and requirements

Improve actual EN/FA instruction following, technical/coding answers, follow-ups and useful
bounded thinking. Compare the serving 35B baseline with a pinned Qwen3.8-27B Q8 precision trial,
not an assertion that 27B is the largest model or that vendor scores prove NextOps accuracy.
The owner supplies a fresh DS-C Storage screenshot (rounded 3.49 TB capacity, 1.79 TB provisioned,
1.71 TB free) and reports no reserved space. Host screenshot: 1.31 TB RAM total, 213.64 GB used,
1.1 TB free; 112 CPUs labelled Xeon Platinum 8280. These are supplied observations/attestation,
not formal all-VM growth accounting, sustained capacity or verified physical NUMA placement.

Direct guest preflight: 80 online vCPUs, 128769 MiB usable RAM, 107664 MiB available, no swap use,
one guest NUMA node/80 virtual sockets, AVX-512/VNNI visible, 169557 MiB available model volume.
The working native runtime remains capped at 96 GiB/18 CPU equivalents. Unused host RAM is not
guest RAM. One 29047086048-byte candidate and its bounded range/assembly workspace fit the
existing model volume; no VM, disk, reservation or serving resource-limit change is required.
The 900-GiB DS-C free-space target is a safety target, not a configured reservation. Keep the
3-TB project ceiling and preserve ESXi, app, connector, databases and Zabbix capacity.

### Non-goals, threats and dependencies

No cloud/GPU, replacement framework, new target tools, operational permissions, schema change,
unbounded output/context/queue, private reasoning display/storage, runtime downloads or live
telemetry inference from host screenshots. Pinned llama.cpp and baseline artifacts remain intact.
Untrusted model bytes, templates, monitoring text and generated code do not grant authorization.
Third-party GGUF declares Qwen3.8-27B lineage; exact conversion-source revision is still unverified.
Keep this uncertainty in the manifest. Do not call a quantizer artifact an official Qwen GGUF.
Record Apache-2.0 licensing; Flash-Next's custom license requires separate applicability review.

### Plan and tasks

1. Record private change scope, fresh supplied capacity and direct guest/mount/runtime checks.
2. Provision **one** immutable Q8 artifact at the pinned source revision through the existing
   proxy chain. Bound transfers and verify exact complete size/SHA-256. Preserve partial attempts;
   never select a partial file. Eight-range continuation is provisioning, not runtime downloading.
3. Inspect actual GGUF architecture, tokenizer/template, lineage and embedded metadata after hash
   verification. Use a separate protected loopback-only CPU trial, one slot, explicit memory/CPU/
   time limits and idle-baseline checks; no target credentials. Stop/clean up the trial at handoff.
4. Reuse the existing adapter with the exact candidate identity. Trusted standard template flags
   disable default thinking and preserved thinking; serving model selection stays unchanged.
   Thinking remains denied for this candidate until a separate matched profile is qualified.
5. Freeze EN/FA format/arithmetic, saved follow-up, DNS/TCP/HTTP/firewall/service, coding and
   provenance/stale/partial/missing/injection cases. Record final answers and resource/timing data;
   discard private reasoning immediately. Review semantics, not merely HTTP 200 or token count.
6. Benchmark thread counts within a bounded isolated profile before changing serving limits.
   Review Flash-Next separately for actual CPU compatibility, complete memory fit and license.
   A proposed 256–512-GiB guest trial is not an applied resize or a promised optimum.
7. Only after usefulness/privacy/deadline gates pass, qualify matched app/API behavior, fresh
   authorized EN/FA evidence/audit, WAN-offline start/restart, failure/queue and rollback/reapply.
   Record any applicable VM reboot/cold-start gap as not run, not passed.

### Acceptance, rollback and documentation

Full-file hash, CPU load and template tests are separate gates. Each answer has the existing
120-second deadline; a timeout is a failure, not a reason to silently widen it. Preserve one active/
two queued requests, context admission, session/owner isolation, source/time/scope and integrity
guards. Model knowledge is not fresh infrastructure evidence; no source substitution on failure.
No unattended trial unit, download or rollback timer remains after handoff. Import rollback needs
no live service restart: baseline links/config are untouched. A later selected-profile change needs
exact retained artifacts/config, timed rollback and fresh authenticated generation/evidence/audit
checks. No destructive schema downgrade or automatic model/snapshot deletion.

Maintain paired CPU guides, project state/next task, the pinned candidate manifest, local tests and
this index entry. Preserve the prior failed-thinking and UI deployment records. Update the serving
release manifest only for an actually accepted identity change, not source registration.

## فارسی

### مسئله و الزامات

هدف، بهبود واقعیِ پیروی از دستور، پاسخ فنی و کدنویسی، ادامهٔ گفتگو و استدلالِ محدود در هر دو
زبان است. مدل زندهٔ 35B با نامزد دقیق‌ترِ Qwen3.8-27B Q8 مقایسه می‌شود؛ 27B بزرگ‌ترین مدل
نیست و امتیاز سازنده، درستی پاسخ NextOps را اثبات نمی‌کند. تصویر تازهٔ مالک برای DS-C، ظرفیت
گردشدهٔ ۳٫۴۹ TB، تخصیص ۱٫۷۹ TB و فضای آزاد ۱٫۷۱ TB را نشان می‌دهد؛ مالک نبود فضای رزروشده
را اعلام کرده است. تصویر میزبان، حافظهٔ کل ۱٫۳۱ TB، مصرف ۲۱۳٫۶۴ GB، آزاد ۱٫۱ TB و ۱۱۲ CPU
با نام Platinum 8280 را نشان می‌دهد. این‌ها شاهد ارسالی و اظهار مالک‌اند، نه حسابرسی کامل رشد
ماشین‌ها، ظرفیت پایدار یا تأیید جای‌گیری فیزیکی NUMA.

پیش‌بررسی مستقیم مهمان: ۸۰ vCPU آنلاین، حافظهٔ قابل‌استفادهٔ ۱۲۸۷۶۹ MiB، مقدار در دسترس
۱۰۷۶۶۴ MiB، مصرف صفر swap، یک گرهٔ NUMA/۸۰ سوکت مجازی، قابلیت AVX-512/VNNI و فضای آزاد
۱۶۹۵۵۷ MiB در حجم مدل. سقف خدمت زنده همچنان ۹۶ GiB و سهم CPU معادل ۱۸ است. حافظهٔ آزاد
میزبان، حافظهٔ تخصیص‌یافته به مهمان نیست. یک نامزدِ ۲۹۰۴۷۰۸۶۰۴۸ بایتی و فضای محدودِ بخش‌ها/
مونتاژ آن در حجم موجود جا می‌گیرند؛ افزایش ماشین، دیسک، رزرو یا سقف خدمت لازم نیست. حاشیهٔ
۹۰۰ GiB برای DS-C هدف ایمنی است، نه رزرو تنظیم‌شده. سقف سه‌ترابایتی و منابع ESXi، برنامه،
اتصال‌دهنده، پایگاه‌ها و زبیکس حفظ شوند.

### موارد خارج از دامنه، تهدیدها و وابستگی‌ها

ابر/GPU، چارچوب جایگزین، ابزار یا مجوز عملیاتی تازه، تغییر schema، خروجی/زمینه/صف نامحدود،
نمایش یا ذخیرهٔ استدلال خصوصی و دانلود زمان اجرا مجاز نیستند. از تصاویر میزبان، وضعیت زندهٔ
زیرساخت برای پاسخ ساخته نشود. runtime ثابت و مدل سالم حفظ شوند. فایل مدل، قالب، متن پایش و
کد تولیدشده غیرقابل‌اعتمادند و مجوز نمی‌دهند. GGUF شخص ثالث، تبار Qwen3.8-27B را اعلام می‌کند؛
نسخهٔ دقیقِ منبع تبدیل هنوز تأیید نشده و این محدودیت باید ثبت بماند. این artifact انتشار رسمیِ
GGUF از Qwen نامیده نشود. Apache-2.0 ثبت شود؛ شرایط مجوز اختصاصی Flash جدا بررسی شوند.

### برنامه و گام‌ها

۱. دامنهٔ تغییر خصوصی، ظرفیت تازهٔ ارسالی و کنترل مستقیم مهمان، mount و runtime ثبت شوند.
۲. فقط یک artifactِ Q8 از نسخهٔ ثابت، با زنجیرهٔ پراکسی موجود آماده شود. انتقال محدود و اندازه/
هش کامل بررسی شوند. تلاش ناقص حفظ شود و هرگز انتخاب نشود؛ ادامهٔ هشت‌بخشی، آماده‌سازی است،
نه دانلود زمان اجرا.
۳. پس از تأیید هش، معماری و قالب/tokenizer و metadata واقعی بررسی شوند. آزمون مستقلِ CPU فقط
روی loopback، با یک جایگاه، سقف صریح حافظه/CPU/زمان، کنترل بیکار بودن مدل زنده و بدون اطلاعات
ورود مقصد اجرا شود؛ هنگام تحویل، فرایند آزمایشی متوقف باشد.
۴. رابط موجود با هویت دقیق نامزد استفاده شود. گزینه‌های قابل‌اعتمادِ استاندارد، استدلال و حفظ
آن را خاموش کنند؛ انتخاب مدل زنده ثابت بماند. استدلال نامزد تا پذیرش نمایهٔ هماهنگ ممنوع است.
۵. پرسش‌های ثابتِ دوزبانه برای قالب/محاسبه، پیگیری گفتگو، DNS/TCP/HTTP/فایروال/خدمت، کدنویسی
و منشأ/شاهد کهنه، ناقص، غایب و تزریق ثبت شوند. پاسخ نهایی و مصرف/زمان اندازه‌گیری و استدلال
خصوصی فوراً دور ریخته شود. صحت معنا بررسی شود، نه فقط HTTP 200 یا شمار توکن.
۶. پیش از تغییر خدمت، تعداد رشته در آزمون مستقل و محدود سنجیده شود. Flash-Next از نظر سازگاری
واقعی CPU، مصرف کامل و مجوز جدا بررسی شود. پیشنهاد ۲۵۶ تا ۵۱۲ GiB، تغییر اجراشده یا مقدار
بهینهٔ تضمین‌شده نیست.
۷. تنها پس از موفقیتِ کاربردپذیری، حریم خصوصی و مهلت، مسیر هماهنگ برنامه/API، شاهد تازهٔ مجاز
فارسی/انگلیسی و ممیزی، شروع/راه‌اندازی دوباره بدون WAN، خرابی/صف و بازگشت/استقرار دوباره
پذیرفته شوند. شکاف reboot/شروع سردِ قابل‌اعمال، اجرا‌نشده ثبت شود، نه موفق.

### پذیرش، بازگشت و مستندات

هش کامل، بارگذاری CPU و قالب، معیارهای جدا هستند. مهلت موجودِ هر پاسخ ۱۲۰ ثانیه است؛ timeout
شکست است و به افزایش پنهانی مهلت منجر نمی‌شود. یک درخواست فعال/دو منتظر، کنترل زمینه، جداسازی
نشست/مالک، منشأ/زمان/دامنه و کنترل صحت حفظ شوند. دانش مدل شاهد زنده نیست و منبع خراب با منبع
دیگر جایگزین نشود. هنگام تحویل، فرایند دانلود، خدمت آزمایشی یا تایمر بدون نظارت باقی نماند.
بازگشتِ ورود فایل به restart خدمت نیاز ندارد؛ لینک و تنظیم مدل سالم تغییر نکرده‌اند. انتخاب
بعدیِ نمایه، artifact/تنظیم دقیق، بازگشت زمان‌دار و آزمون تازهٔ ورود، پاسخ، شاهد و ممیزی لازم
دارد. downgrade مخرب یا حذف خودکار مدل/snapshot ممنوع است.

راهنمای CPU دو زبان، وضعیت/کار بعدی، manifest نامزد، آزمون‌های محلی و فهرست context به‌روز
شوند. سابقهٔ شکست استدلال و استقرار رابط حفظ شود. ثبت هویت در کد، تغییر مدل زنده نیست؛ manifest
انتشار زنده فقط با تغییر پذیرفته‌شدهٔ واقعی به‌روز شود.
