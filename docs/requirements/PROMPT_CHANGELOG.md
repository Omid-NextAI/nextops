# Prompt version history / تاریخچهٔ نسخه‌های پرامپت

## Owner bounded response-time amendment — 2026-10-06

The owner explicitly requests longer answering time for actual Qwen3.8. Prospectively allow an
opt-in 300-second Qwen3.8 candidate deadline, with a 330-second app caller and 360-second
generation-route proxy budget. This supersedes earlier no-deadline-widening instructions only
for this new timing profile. Historical 120-second failures remain failed. Preserve the frozen
questions, semantic requirements, 16K context, output limits, five-second queue wait, one active/
two queued requests, CPU-only execution, authentication and private-thinking denial. A separate
watched two-case EN/FA hypothesis diagnostic is permitted on the retained Q5; fourteen other
cases remain not run in that diagnostic. No quality waiver, model promotion, new VM resources,
download, public thinking or live timeout change follows from source profiles alone.

مالک صریحاً افزایش زمان پاسخ‌گویی برای Qwen3.8 واقعی را خواست. از این پس، نمایهٔ اختیاریِ
نامزد Qwen3.8 می‌تواند مهلت ۳۰۰ ثانیه‌ای داشته باشد؛ مهلت فراخوان برنامه ۳۳۰ ثانیه و مهلت
پراکسیِ مسیر تولید پاسخ ۳۶۰ ثانیه است. دستورهای پیشینِ منع افزایش مهلت، فقط برای این نمایهٔ
جدید کنار گذاشته می‌شوند؛ شکست‌های تاریخیِ ۱۲۰ ثانیه‌ای همچنان ناموفق‌اند. پرسش‌های ثابت،
معیار معنایی، زمینهٔ 16K، سقف خروجی، انتظار پنج‌ثانیه‌ای صف، یک درخواست فعال/دو درخواست
منتظر، اجرای CPU، احراز هویت و منع استدلال خصوصی حفظ می‌شوند. آزمون تشخیصیِ جدا و تحت
نظارت برای دو پرسش فرضیهٔ انگلیسی/فارسی روی Q5 موجود مجاز است؛ چهارده مورد دیگر در این
آزمون اجرا نشده‌اند. نمایهٔ کد به‌تنهایی مجوز حذف معیار کیفیت، انتخاب مدل زنده، منابع تازهٔ
VM، دریافت مدل، استدلال عمومی یا تغییر مهلت سامانهٔ زنده نیست.

## Owner connector-role clarification — 2026-10-04

The owner specifies that the existing connector VM must fulfil the MCP role from the original
design. This reaffirms active master sections 5 and 12; the master body/version and immutable v2
archive are unchanged. The canonical gateway and isolated runners share the existing connector VM,
not a new permanent parallel stack. Keep application policy authoritative, target credentials
runner-only, real MCP protocol and offline provisioning. Current HTTP is explicitly transitional
compatibility/rollback, not relabelled MCP or a bypass. The design correction grants no new server
mutation, acceptance waiver or production-readiness claim. See
[the bounded requirements](MULTI_SOURCE_MCP_SPEC.md) and ADR 0010's dated clarification.

مالک تصریح کرد که ماشین موجودِ اتصال‌دهنده باید نقش MCP را مطابق طرح اولیه ایفا کند. این
دستور، بخش‌های ۵ و ۱۲ پرامپت فعال را تأکید می‌کند؛ متن و نسخهٔ پرامپت و بایگانی تغییرناپذیر v2
ثابت‌اند. درگاه اصلی و اجراکننده‌های جداگانه روی همان ماشین قرار می‌گیرند، نه سامانهٔ موازیِ
دائمی. مرجع مجوز، برنامه است؛ اطلاعات ورود مقصد فقط نزد اجراکننده می‌ماند و پروتکل واقعی MCP
و آماده‌سازی آفلاین حفظ می‌شوند. HTTP فعلی صریحاً برای سازگاری و بازگشتِ دورهٔ گذار است؛ MCP
نامیده نمی‌شود و مسیر دورزن نیست. اصلاح طراحی، مجوز تغییر تازهٔ سرور یا حذف معیار پذیرش و
ادعای آمادگی تولید نمی‌دهد. [الزامات محدود](MULTI_SOURCE_MCP_SPEC.md) و پیوست تاریخ‌دارِ
تصمیم 0010 مبنا هستند.

## Owner repair/deployment loop — 2026-10-04

The owner requests gap repair and a loop to successful deployment. This authorizes bounded
existing-guest qualification and guarded release with exact rollback, not blind retries or waived
security/offline/accuracy gates. After capability-v2 raw diagnostic failures, isolate an
application-only safeguard; do not promote that broader failed provider/history candidate.

مالک رفع کاستی و چرخه تا استقرار موفق را خواسته است. آزمون محدود در مهمان موجود و انتشار
محافظت‌شده با بازگشت دقیق مجاز است، نه تکرار کور یا حذف معیار امنیت/آفلاین/درستی. پس از شکست
تشخیصیِ خام نسخهٔ دوم، کنترل صرفاً برنامه‌ای جدا شود؛ دستور/سابقهٔ گستردهٔ ناموفق مستقر نشود.

## Owner live-chat/theme instruction — 2026-09-30

The owner explicitly requests the work needed to take the conversation candidate live and a dark
theme switch. This authorizes a bounded guarded app/AI/schema/profile qualification and promotion
on the existing controlled guests, with exact rollback. It does not waive failed quality/offline
gates or authorize new ESXi resources, destructive database downgrade or unrelated integrations.
Recovery remains owner-deferred; this task is not an attestation of full production acceptance.

مالک صریحاً آماده‌سازی نامزد گفت‌وگو برای استقرار زنده و دکمهٔ پوستهٔ تیره را خواسته است. این
دستور، آزمون و استقرار محدود و محافظت‌شدهٔ برنامه، AI، پایگاه و نمایه در مهمان‌های موجود را با
بازگشت دقیق مجاز می‌کند؛ شکست کیفیت یا آفلاین را حذف و منابع تازهٔ ESXi، بازگردانی مخربِ پایگاه
یا اتصال نامرتبط را مجاز نمی‌کند. بازیابی همچنان در تعویق است و پذیرش کامل تولید ادعا نمی‌شود.

## Owner conversation/model expansion amendment — 2026-09-30

The owner requests more context, local thinking, persistent chat and consecutive follow-up answers,
reports expanded AI resources and directs implementation. The new bounded conversation packet
supersedes the previous general-only nonpersistent-memory non-goal; live evidence, policy, CPU-only,
offline and resource safeguards are unchanged. New candidate budgets are a separate qualification,
not reinterpretation of earlier failed tests. More RAM/vCPU is not an accuracy or topology pass.
See [the specification](../en/CONVERSATION_MEMORY_SPEC.md). No serving-profile promotion is implied.

مالک زمینهٔ بزرگ‌تر، استدلال محلی، حافظهٔ گفت‌وگو و پاسخ پی‌درپی را خواسته، افزایش منابع AI را
اعلام کرده و شروع پیاده‌سازی را درخواست کرده است. مشخصات تازه، خارج‌ازدامنه بودن حافظهٔ ماندگار
در برش عمومی قبلی را جایگزین می‌کند؛ شاهد زنده، سیاست، CPU-only، آفلاین و محدودیت منابع حفظ
می‌شوند. بودجهٔ نامزد جدید جداگانه سنجیده می‌شود و شکست قبلی را بازتفسیر نمی‌کند. افزایش منابع
اثبات کیفیت یا توپولوژی نیست. [مشخصات فارسی](../fa/CONVERSATION_MEMORY_SPEC.md) مبناست؛ انتخاب
نمایهٔ تازه برای نسخهٔ در حال خدمت از این دستور استنباط نمی‌شود.

## Owner development-workflow amendment — 2026-09-29

The owner explicitly removes the all-at-once private decision form and its prerequisite procedure
and requests continued development toward a usable live deployment and clearer answers from a
larger CPU-local candidate. Only inputs actually needed by the next operation may block it.
Engineering may record the explicit task authorization directly and generate its own change ID.
This does not waive tested authorization, audit, verified artifacts, bounded resources or rollback,
and it does not turn a failed or unrun acceptance gate into a pass. Recovery stays owner-deferred.

مالک صریحاً فرم خصوصیِ یک‌جای تصمیم‌ها و روندِ پیش‌شرط آن را حذف کرده و ادامهٔ توسعه برای استقرار
زندهٔ قابل‌استفاده و پاسخ روشن‌تر با مدل بزرگ‌ترِ محلیِ CPU را خواسته است. فقط ورودی لازمِ عملیات
بعدی می‌تواند مانع همان عملیات باشد. عامل مهندسی اجازهٔ صریحِ کار را مستقیم ثبت و شناسهٔ تغییر
را خودش تولید می‌کند. احراز مجوز، ممیزی، فایل تأییدشده، منابع محدود و امکان بازگشت حذف نمی‌شوند
و آزمون ناموفق یا اجرا‌نشده موفق شمرده نمی‌شود. بازیابی همچنان به دستور مالک به تعویق افتاده است.

## Owner clarification of the recovery claim — 2026-09-26

The owner clarified that the verification was restoration from an ESXi VM snapshot only. It does
not evidence independent PostgreSQL backup, WAL/PITR, isolated database restore, key/artifact
recovery or survival of loss of the serving hypervisor/storage. The active non-recovery delivery
sequence is unchanged, and the full-production recovery gates remain unpassed.

مالک روشن کرد که آزمون انجام‌شده فقط بازیابی از snapshot ماشین ESXi بوده است. این آزمون شاهدِ
پشتیبان مستقلِ PostgreSQL، ‏WAL/PITR، بازیابی ایزولهٔ پایگاه، بازیابی کلید و فایل یا دوام در برابر
خرابی میزبان و ذخیره‌سازی نیست. ترتیب تحویل غیربازیابی تغییر نمی‌کند و معیارهای بازیابیِ پذیرش
کامل تولید همچنان پذیرفته نشده‌اند.

## Owner scope amendment — 2026-09-26

The owner reports daily ESXi snapshots of all four local servers and directs the team to complete
non-recovery work without treating independent recovery as the first active blocker. This later
instruction changes the current delivery sequence, not the historical v3.0/v2.0 text or the
meaning of a passed backup/restore test. Snapshot configuration and successful restoration have
not been verified. The checked-in recovery profile remains blocked, and full production acceptance
cannot be claimed under its existing contract. Other security, quality, offline and approval gates
are unchanged. The release manifest records the owner-directed scope explicitly.

مالک اعلام کرده است که از هر چهار سرور محلی هر روز در ESXi snapshot گرفته می‌شود و خواسته است کارهای
غیربازیابی، بدون قرار دادن مقصد مستقل بازیابی در ابتدای صف، ادامه یابند. این دستورِ جدید ترتیب
تحویل فعلی را تغییر می‌دهد، نه متن تاریخی نسخه‌های ۳ و ۲ یا معنای آزمون موفق پشتیبان و بازیابی را.
پیکربندی snapshot و بازیابی موفق آن مستقلاً تأیید نشده‌اند؛ پروفایل بازیابی همچنان مسدود است و
ادعای پذیرش کامل تولید مجاز نیست. سایر دروازه‌های کیفیت، امنیت، کارکرد آفلاین و تأیید انسانی
برقرارند. دامنهٔ جدید در مانیفست انتشار ثبت شده است.

## v3.0 — 2026-09-20

[Active prompt](NEXTOPS_MASTER_PROMPT.md) · [Preserved v2.0](archive/NEXTOPS_MASTER_PROMPT_v2.0.md) · [Source provenance](SOURCES.md)

### English

Owner authorization: update the prompt as needed after the hardware, datastore and deployment discussions. This is a documentation revision only; it does not approve provisioning or complete any implementation phase.

| Topic | Reconciled instruction |
|---|---|
| Repository | Use the existing `AmirMo10/nextops`; inspect its current work instead of assuming no repository exists. |
| Hardware evidence | Use 4 packages, 112 physical cores, 224 threads, 4 NUMA nodes and 1,442,743,631,872 bytes RAM; retain source and uncertainty labels. |
| Host/guest boundary | Preserve ESXi 8.0.3 build 24414501. Ubuntu Server 24.04 LTS is the proposed guest, not an ESXi replacement. |
| First milestone | Phase 1 finishes with a real offline local-CPU answer about authorized Zabbix status. Linux enrichment remains Phase 2. |
| Starting stages | 1A application/security; 1B local model; 1C restricted Zabbix evidence; 1D answer; 1E offline acceptance. |
| VM creation | App first, AI second, read-only connectors third; 8/24/4 vCPU, 32/128/8 GiB RAM, 200/500/80 GiB disk. |
| Initial totals | 3 NextOps VMs, 36 vCPU, 168 GiB RAM, 780 GiB VMDKs; not actual reservations or measured minimums. |
| Storage | Retain 3 TB project ceiling and DS-C-specific evidence; initial provisional VMDK-plus-swap subtotal 948 GiB; exact 25% DS-C free target 894.1875 GiB, conservatively about 900. |
| Offline behavior | Normal CPU-local generation online or offline, fresh login, cold start/reboot, local assets and protected key access; no external AI fallback. |
| Evidence and tests | Preserve status semantics, deterministic counts, source/time/scope reporting, ZBX-01–ZBX-08 and applicable OFF-01–OFF-10; all tests remain unrun until evidence is recorded. |
| Source preservation | Archive the complete previous prompt using its existing Git blob; keep the original Persian appendix intact and no new prompt translation. |
| Continuation | Resume the next unfinished authorized checkpoint; do not repeat supplied discovery or restart Phase 0 after it is actually approved and complete. |

The active prompt keeps the original 26 engineering sections and explicitly incorporates non-conflicting detailed v2 requirements. All 51 original sections and eleven integrations remain traceable; this update does not reduce their scope. Current v3 decisions override stale hardware, sequencing or cloud examples and older statements forbidding any prompt edit. Such immutability now applies to the archived v2 source.

Archive Git blob: `d6420b4436907c8a9daa5599dc8e7398b540b280`.
Archive SHA-256: `35d7f8be94145bacc53ca4447695abbcab6115b1a3812a087251ddc2850c54c4`.

Validation boundary: source/archive identity and Git changes can be checked independently of application tests. The documentation-only update performs no VM creation, host inspection, model download/run, benchmark, Zabbix call, patch installation, network shutdown, offline restart or restore test. It does not claim a full repository checkout/test run when unavailable.

### فارسی

مجوز مالک، به‌روزرسانی پرامپت پس از گفت‌وگو دربارهٔ سخت‌افزار، ذخیره‌سازی و ترتیب شروع است. این کار فقط بازنگری مستندات است؛ نه اجازهٔ ساخت ماشین و نه تکمیل مرحله‌ای از پیاده‌سازی.

نسخهٔ ۳، مخزن موجود، مشخصات ارسالیِ ۱۱۲ هسته و ۲۲۴ رشته و چهار گره، نسخهٔ ESXi و نقش Ubuntu به‌عنوان مهمان را مبنا قرار می‌دهد. اولین خروجی باید در پایان مرحلهٔ یک، پاسخ واقعی و مستند هوش مصنوعی محلی دربارهٔ Zabbix با اینترنت قطع باشد؛ بررسی تکمیلی Linux در مرحلهٔ دو باقی می‌ماند.

ترتیب ساخت، برنامه سپس AI و سپس اتصال فقط‌خواندنی است: به‌ترتیب ۸، ۲۴ و ۴ vCPU؛ حافظهٔ ۳۲، ۱۲۸ و ۸ GiB؛ دیسک ۲۰۰، ۵۰۰ و ۸۰ GiB. مجموع اولیه ۳ ماشین، ۳۶ vCPU، حافظهٔ ۱۶۸ GiB و دیسک ۷۸۰ GiB است. مراحل 1A تا 1E پایهٔ امنیت، مدل محلی، شواهد محدود Zabbix، پاسخ کاربردی و پذیرش آفلاین را پوشش می‌دهند.

سقف سه‌ترابایتی پروژه و محل پیشنهادی DS-C حفظ شده‌اند. با سهم موقت swap، جمع اولیه ۹۴۸ GiB است. هدف دقیق حاشیهٔ آزادِ ۲۵ درصد روی DS-C برابر ۸۹۴٫۱۸۷۵ GiB است که محافظه‌کارانه حدود ۹۰۰ در نظر گرفته می‌شود. این اعداد پیشنهاد و محاسبه‌اند؛ نه رزرو اعمال‌شده یا حداقل اندازه‌گیری‌شده.

تولید پاسخ همیشه محلی و مبتنی بر CPU است؛ ورود تازه، شروع از حالت متوقف، روشن شدن دوباره، فایل‌های رابط و دسترسی امن به کلیدها نباید اینترنت بخواهند. معیارهای ZBX و OFF، شمارش قطعی و نمایش منبع و زمان و دامنه برقرارند. آزمون بدون شاهد واقعی، قبول‌شده معرفی نمی‌شود.

ساختار ۲۶بخشی مهندسی حفظ شده و جزئیات بدون تعارضِ نسخهٔ ۲ همچنان الزامی‌اند. تمام ۵۱ بخش اولیه و یازده اتصال باقی می‌مانند. نسخهٔ کامل قبلی با همان شناسهٔ Git بالا در بایگانی نگهداری می‌شود؛ پیوست فارسی آن دست‌نخورده است و ترجمهٔ تازه‌ای از پرامپت تهیه نشده است. عبارت‌های قدیمی دربارهٔ ثابت ماندن پرامپت از این پس به همین نسخهٔ بایگانی‌شده اشاره دارند.

عامل باید از نخستین گام ناتمامِ دارای مجوز ادامه دهد؛ نه اطلاعات ارسال‌شده را دوباره بخواهد و نه مرحلهٔ صفرِ واقعاً تأیید و تکمیل‌شده را بی‌پایان تکرار کند. این تغییر هیچ VM، مدل اجرایی، تماس با Zabbix، آزمون کارایی، تغییر شبکه یا آزمون بازیابی ایجاد یا اجرا نمی‌کند. بررسی هویت منبع و تغییرات Git با آزمون محصول یکی نیست.

## v2.0 — prepared 2026-09-19

The prior complete engineering prompt and its original Persian appendix are preserved in the linked archive. Later owner clarifications now live in v3.0 and the dated evidence records.

نسخهٔ کامل پیشین و پیوست فارسی اولیه در بایگانی بالا حفظ شده‌اند. توضیحات بعدی مالک در نسخهٔ ۳.۰ و رکوردهای تاریخ‌دار شواهد اعمال شده‌اند.
