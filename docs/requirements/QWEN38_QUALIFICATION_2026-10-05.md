# Qwen 3.8 controlled trial / آزمون کنترل‌شدهٔ Qwen 3.8

Date: 2026-10-05. Decision: **retain the candidate, do not select it for live service**.
This is a sanitized native/adapter trial, not production or matched application acceptance.
[Plan](QWEN38_QUALIFICATION_SPEC.md), [candidate manifest](../../deploy/inference/qwen3-8-27b-q8.candidate.json),
[English CPU guide](../en/CPU_AI.md), [راهنمای فارسی CPU](../fa/CPU_AI.md).

## English

### Artifact and actual execution

The supplied fresh DS-C/host screenshots resolve the earlier capacity stop for this single
bounded import. No ESXi, VM RAM/CPU/disk, serving limits, database, operational permissions or
live model selection changed. Source `e39e2c9` was archived and verified before isolated use;
the exact serving app remains `836b1ea`, inference API `7ce9d29`, connector `2a7c8dc` and model
Qwen3.5-35B-A3B Q4. Public thinking is still off.

Qwen3.8-27B Q8 was imported through the existing proxy chain, with exact **29047086048 bytes**
and SHA-256 `a680f44a06920e5d689774823782006aa3acc8db95750323373b24139b67e348`.
It is root-owned, read-only and unselected; upstream Apache-2.0 license and quantizer README
were retained. This is an Unsloth conversion, not an official Qwen GGUF. Exact conversion-source
revision remains unverified, despite declared lineage; do not erase that manifest limitation.

Actual GGUF v3 metadata: `qwen35` architecture, 65 blocks, embedding length 5120, 866 tensors,
51 metadata fields, `gpt2` tokenizer with `qwen35` pre-tokenizer, metadata context 262144.
Actual template SHA-256:
`12827f24b742ea4e80cdc12dbcf9622227056b9f797252a3149263d4f9aaadce`.
The protected trial loaded successfully on pinned CPU-only llama.cpp commit
`b29c606e28a01b1bc8c1351026a0fa6e616bf6c4`, with **16384 configured context**, one slot,
48-GiB memory maximum, and no GPU layers. Metadata context is not tested context capacity.

Two isolated profiles were measured: 16 threads/18 CPU equivalents, then 32 threads/36
equivalents. Neither modifies serving limits. Standard requests explicitly disable thinking and
preservation; native-only arithmetic diagnostics allow a 128-token reasoning budget and discard
private reasoning, retaining only its character count and final answer. Candidate thinking remains
denied by the application configuration until a separate matched profile is accepted.

### Frozen single-sample comparison

Each standard profile used the same eight synthetic questions in fixed order, temperature 0.3,
384 output tokens and the existing 120-second deadline. These are **not** p50/p95, throughput,
time-to-first-token or sustained-load measurements. Prompt caching/order and startup effects
were not independently controlled; do not generalize the ratios as a comprehensive benchmark.

| Case | Serving 35B, 16 threads | Candidate 27B Q8, 16 threads | Candidate, 32 threads |
|---|---:|---:|---:|
| EN strict digit | 3039 ms | 65731 ms | 52570 ms |
| FA strict digit | 3128 ms | 65369 ms | 51961 ms |
| EN network explanation | 11897 ms | 73938 ms | 47852 ms |
| FA network explanation | 19756 ms | 69402 ms | 65760 ms |
| EN short follow-up recall | 3734 ms | 20317 ms | 17538 ms |
| FA short follow-up recall | 4072 ms | 20927 ms | 17634 ms |
| EN coding | 5944 ms | 33618 ms | 25535 ms |
| FA coding | 6205 ms | 34785 ms | 29957 ms |

All four exact digit/short-recall checks passed per profile. These synthetic history prompts do
not qualify durable saved-chat ownership/resume. Network answers distinguished reachability from
unknown upstream failure in this narrow case; some wording assumed a proxy/load-balancer topology
not established by the question. This is limited engineering review, not a general factuality pass.

Both models generated a function equivalent to `return method in ("host.get", "item.get")`.
The requested invariant was False for **all non-string inputs**. A manually reviewed non-string
object whose `__eq__` returns True is accepted by that function: the coding invariant **failed**
for both models. No arbitrary generated code was executed and this is not an application policy
bypass; deterministic authorization remains outside the model.

Native-only thinking answered `7 × 3 + 4 = 25` in EN and FA: 67079/71284 ms at 16 threads,
57847/67865 ms at 32 threads. Four arithmetic samples do not qualify technical thinking,
injection resistance, provenance, privacy across saved conversations or application publication.

One EN near-context probe used actual app question/history bounds and template token counts:
**15360 input tokens**, 1024 output reservation, 16384 context. It **failed after 120163 ms**
with `inference.provider_unavailable` at the existing deadline. No answer or long-context recall
pass was recorded; FA near-context was not run. The trial process was then stopped and its actual
PID disappearance/listener absence verified; client timeout alone was not treated as remote stop.

### Resources, isolation and failures retained

At the final 32-thread observation, trial RSS was 31613260 KiB, approximately **30.15 GiB**;
PSS 31602970 KiB and process swap zero. Guest available memory was 103953 MiB with zero swap use.
The cgroup peak was 4481314816 bytes, but model page cache was already charged outside the trial
during verification: **that cgroup value is not the complete model memory footprint**. Cumulative
trial CPU usage was 20377.05 CPU-seconds, not a host utilization percentage or sustained-load gate.
Guest-visible topology remains one NUMA node/80 virtual sockets; physical placement is not proved.

The actual trial cgroup denied/dropped a TCP attempt to a known reachable LAN control endpoint
that succeeded outside the cgroup. This is a process-egress isolation check, **not** whole-platform
WAN-disconnection, fresh browser login/evidence, restart/reboot or cold-start acceptance. The
initial unreachable-address/expected-EPERM test timed out and failed its assertion; its test design
was invalid and is retained separately, not relabelled passed.

The first finite single-stream provisioning attempt was explicitly terminated after inspecting
its PID and preserving its prefix. Seven of eight bounded ranges completed; one failed with
HTTP/2 cancellation. Exact missing bytes were reconciled with four bounded HTTP/1.1 transfers;
the assembled full file passed size/hash verification. No partial artifact was selected.
An initial cleanup comparison stopped because its protected archival copy did not yet exist;
actual unit hashes were reconciled against the reviewed originals before cleanup continued.

### Disposition and remaining acceptance

Artifact, template/tokenization and protected CPU loading passed. Standard semantic qualification
failed the coding invariant; latency/context qualification failed. Thinking/privacy and WAN are
partial, not accepted. No model cutover or model rollback/reapply was attempted. The stopped
ephemeral trial and its drop-in were removed after preserving their definitions and protected
reports. Rehashed immutable artifact is retained; only this trial's exact duplicate download parts
were removed, reclaiming **29047086048 bytes (~27.05 GiB)**. Logs/results remain protected.
Serving native/AI services remained active, ready and on the unchanged 35B identity.

Next: repair the bounded evaluation gaps and investigate measured CPU/thread/topology or
quantization options before another profile. Keep frozen semantic/deadline tests; do not widen
timeouts, fabricate successful evidence or switch models merely because RAM is available.
A separate larger Flash-Next experiment needs license/CPU compatibility review, complete memory
fit and saved guest/topology verification. Start its sizing review at 256 GiB guest RAM; 512 GiB
requires measured buffer/context need. No such resize/import occurred in this trial.

Matched app/API thinking, fresh selected-source EN/FA evidence and durable audit, stale/partial/
absent/injection cases, queue/failure recovery, actual WAN restart and applicable VM cold start,
and exact rollback/reapply remain **not run for this candidate**. Historical acceptance is not
transferred to a new model. Raw operational results and scripts are in the protected change record,
not Git; public reproduction is the plan and frozen protocol above, not a credentials-bearing script.

Source gates at `e39e2c9`: 622 unit/source checks passed, two Windows POSIX skips, 85 deselections;
five exact-head CI jobs passed, including PostgreSQL 16/17 and browser fixtures
([CI run](https://github.com/Omid-NextAI/nextops/actions/runs/37281920437)). These are source gates,
not candidate model acceptance. Full Windows-target mypy initially reported nine existing POSIX
attribute errors in two Linux-only collector modules; `--platform linux` passed 125 source files.
No POSIX security control or dependency lock was weakened to suppress those diagnostics.

## فارسی

### فایل مدل و اجرای واقعی

تصاویر تازهٔ DS-C و میزبان، مانع قبلیِ ظرفیت را برای همین ورودِ محدود رفع کردند. منابع ESXi،
CPU/RAM/دیسک ماشین، سقف خدمت زنده، پایگاه، مجوز عملیاتی و انتخاب مدل زنده تغییر نکردند.
کد `e39e2c9` پیش از آزمون مستقل بایگانی و تأیید شد؛ برنامهٔ زنده `836b1ea`، API هوش مصنوعی
`7ce9d29`، اتصال‌دهنده `2a7c8dc` و مدل Qwen3.5-35B-A3B Q4 ثابت‌اند. استدلال عمومی خاموش است.

نامزد Qwen3.8-27B Q8 با زنجیرهٔ پراکسی موجود وارد شد: اندازهٔ دقیق **۲۹۰۴۷۰۸۶۰۴۸ بایت** و
هش SHA-256 درج‌شده در بخش انگلیسی. فایل فقط‌خواندنی، متعلق به root و انتخاب‌نشده است؛ مجوز
Apache-2.0 و README کمّی‌ساز حفظ شدند. این تبدیل Unsloth است، نه GGUF رسمیِ Qwen. با وجود
تبار اعلام‌شده، نسخهٔ دقیق منبع تبدیل هنوز تأیید نشده و محدودیت manifest باقی است.

metadata واقعیِ GGUF نسخهٔ سه: معماری `qwen35`، تعداد ۶۵ بلوک، طول embedding برابر ۵۱۲۰،
۸۶۶ tensor، تعداد ۵۱ فیلد، tokenizer از نوع `gpt2` با پیش‌پردازش `qwen35` و زمینهٔ اعلامیِ
۲۶۲۱۴۴. هش واقعیِ قالب در بخش انگلیسی درج است. بارگذاری با commit ثابتِ llama.cpp موفق بود:
فقط CPU، زمینهٔ تنظیم‌شدهٔ **۱۶۳۸۴**، یک جایگاه، سقف حافظهٔ ۴۸ GiB و بدون لایهٔ GPU.
زمینهٔ درج‌شده در metadata، ظرفیت پذیرفته‌شدهٔ آزمون نیست.

دو نمایهٔ مستقل سنجیده شد: ۱۶ رشته/سهم معادل ۱۸ CPU و سپس ۳۲ رشته/معادل ۳۶ CPU. سقف خدمت
زنده تغییر نکرد. درخواست استاندارد صریحاً استدلال و حفظ آن را خاموش می‌کند؛ آزمون محاسباتیِ
صرفاً native با بودجهٔ ۱۲۸ توکن استدلال، متن خصوصی را فوراً دور می‌ریزد و فقط شمار نویسه و
پاسخ نهایی را نگه می‌دارد. تنظیم برنامه، استدلال نامزد را تا پذیرش نمایهٔ هماهنگ رد می‌کند.

### مقایسهٔ ثابت با نمونهٔ محدود

هر نمایه همان هشت سؤال ساختگی را با ترتیب ثابت، دمای ۰٫۳، سقف خروجی ۳۸۴ توکن و مهلت موجودِ
۱۲۰ ثانیه پاسخ داد. جدول انگلیسی، زمان دقیق هر مورد را نشان می‌دهد؛ این اعداد p50/p95، ظرفیت
هم‌زمانی، زمان نخستین توکن یا بار پایدار نیستند. اثر ترتیب، کشِ prompt و شروع به‌طور مستقل
کنترل نشده است؛ نسبت زمان‌ها benchmark جامع محسوب نمی‌شود.

چهار معیارِ رقم دقیق/یادآوری کوتاه در هر نمایه موفق بود؛ prompt ساختگیِ سابقه، پذیرش مالکیت
و ادامهٔ گفتگوی ذخیره‌شده نیست. پاسخ شبکه در همین مورد محدود، دسترس‌پذیری را از علت نامعلوم
خرابی بالادست جدا می‌کرد؛ بعضی عبارت‌ها وجود proxy/load balancer را بدون اثبات فرض کردند.
این بازبینی محدود، پذیرش عمومیِ صحت نیست.

هر دو مدل تابعی هم‌ارز `return method in ("host.get", "item.get")` تولید کردند. الزام، False
برای **تمام ورودی‌های غیررشته‌ای** بود. شیء غیررشته‌ایِ بررسی‌شده که `__eq__` آن True می‌دهد،
از این تابع پاسخ True می‌گیرد؛ معیار کدنویسی برای هر دو مدل **ناموفق** است. کد دلخواهِ مدل
اجرا نشد؛ این نتیجه نیز دور زدن سیاست برنامه نیست. مجوز قطعی همچنان خارج از مدل است.

استدلالِ صرفاً native پاسخ محاسبهٔ `7 × 3 + 4 = 25` را در دو زبان درست داد: زمان‌های
۶۷۰۷۹/۷۱۲۸۴ میلی‌ثانیه با ۱۶ رشته و ۵۷۸۴۷/۶۷۸۶۵ با ۳۲ رشته. چهار نمونهٔ ساده، پذیرش استدلال
فنی، مقاومت در برابر تزریق، منشأ، حریم خصوصیِ سابقه یا انتشار پاسخ در برنامه نیستند.

یک آزمون انگلیسیِ نزدیک سقف، با کران واقعیِ سؤال/سابقهٔ برنامه و شمارش قالب اجرا شد:
**۱۵۳۶۰ توکن ورودی**، سهم خروجی ۱۰۲۴ و زمینهٔ ۱۶۳۸۴. پس از **۱۲۰۱۶۳ میلی‌ثانیه** با خطای
`inference.provider_unavailable` در مهلت موجود **شکست خورد**. پاسخ یا پذیرشِ یادآوریِ زمینهٔ
بلند ثبت نشد؛ نمونهٔ فارسیِ نزدیک سقف اجرا نشد. فرایند مستقل متوقف و نبود PID/listener واقعی
بررسی شد؛ timeoutِ کارخواه به‌تنهایی توقف عملیات راه دور تلقی نشد.

### منابع، جداسازی و حفظ شکست‌ها

در مشاهدهٔ نهاییِ ۳۲ رشته، RSS برابر ۳۱۶۱۳۲۶۰ KiB، حدود **۳۰٫۱۵ GiB**، و PSS برابر
۳۱۶۰۲۹۷۰ KiB بود؛ swap فرایند صفر. حافظهٔ در دسترسِ مهمان ۱۰۳۹۵۳ MiB و swap آن صفر بود.
قلهٔ cgroup برابر ۴۴۸۱۳۱۴۸۱۶ بایت است، اما کش فایل مدل در بررسی قبلی خارج از آن حساب شده؛
**این عدد مصرف کامل مدل نیست**. مصرف تجمعی، ۲۰۳۷۷٫۰۵ ثانیهٔ CPU است، نه درصد مصرف میزبان
یا پذیرش بار پایدار. یک گرهٔ NUMA/۸۰ سوکت مجازی دیده می‌شود؛ جای‌گیری فیزیکی اثبات نشده است.

اتصال TCP به مقصد کنترلِ LAN که خارج از cgroup موفق بود، در cgroup واقعیِ آزمون رد/حذف شد.
این کنترل خروج شبکهٔ فرایند است، **نه** قطع WAN کل سامانه، ورود/شاهد تازه، restart/reboot یا
شروع سرد. آزمون اولیه با مقصد دسترس‌ناپذیر و انتظار EPERM، timeout و شکست assertion داشت؛
طراحی آن معتبر نبود و سابقهٔ شکست جدا حفظ شد، نه اینکه موفق نامیده شود.

انتقال تک‌جریانیِ نخست پس از بررسی PID صریحاً متوقف و بخش دریافت‌شده حفظ شد. هفت بخش از هشت
بخشِ محدود تکمیل و یکی با لغو HTTP/2 ناموفق شد. بایت‌های دقیق باقی‌مانده با چهار انتقال محدودِ
HTTP/1.1 تکمیل و اندازه/هش فایل کامل تأیید شدند. فایل ناقص انتخاب نشد. مقایسهٔ نخستِ پاک‌سازی
به دلیل نبود نسخهٔ بایگانی محافظت‌شده متوقف شد؛ پیش از ادامه، هش تعریف واقعیِ خدمت با اصلِ
بررسی‌شده تطبیق و تعریف آن بایگانی شد.

### نتیجه و پذیرش باقی‌مانده

فایل کامل، قالب/tokenization و بارگذاری محافظت‌شدهٔ CPU موفق‌اند. صحت استاندارد در معیار
کدنویسی و تأخیر/زمینه ناموفق‌اند. استدلال/حریم خصوصی و WAN فقط بخشی بررسی شده‌اند. گذار مدل
یا بازگشت/استقرار دوبارهٔ مدل انجام نشد. خدمت موقت و drop-in پس از حفظ تعریف و گزارش خصوصی
حذف شدند. فایل کامل دوباره هش‌سنجی و حفظ شد؛ فقط بخش‌های تکراریِ دقیقِ همین آزمون حذف شدند:
**۲۹۰۴۷۰۸۶۰۴۸ بایت، حدود ۲۷٫۰۵ GiB** آزاد شد. log و نتیجه حفظ‌اند. خدمت native و AI همچنان
فعال و آماده و بر هویت 35B باقی ماندند.

گام بعد، اصلاح شکاف ارزیابی محدود و بررسیِ سنجیدهٔ رشته/CPU/توپولوژی یا کمّی‌سازی پیش از
نمایهٔ بعدی است. سؤال و مهلت ثابت بمانند؛ حافظهٔ آزاد، مجوز افزایش پنهانی مهلت، ساختن شاهد
موفق یا تعویض بی‌دلیل مدل نیست. آزمون جداگانهٔ Flash-Next بزرگ‌تر، بررسی مجوز، سازگاری CPU،
جاگرفتنِ مصرف کامل و تنظیم ذخیره‌شدهٔ مهمان/توپولوژی می‌خواهد. بررسی اندازه از ۲۵۶ GiB آغاز
شود؛ ۵۱۲ GiB به نیاز اندازه‌گیری‌شدهٔ بافر/زمینه وابسته است. اینجا افزایش یا ورود Flash انجام نشد.

استدلال هماهنگِ برنامه/API، شاهد تازهٔ مجازِ دوزبانه و ممیزی، شاهد کهنه/ناقص/غایب/تزریق،
بازیابی صف/خرابی، شروع با WAN واقعاً قطع، شروع سردِ قابل‌اعمال و بازگشت دقیق برای این نامزد
**اجرا نشده‌اند**. پذیرش تاریخی به مدل تازه منتقل نمی‌شود. نتیجهٔ خام و اسکریپت عملیاتی در
رکورد محافظت‌شده‌اند، نه Git؛ برنامه و پروتکل ثابتِ بالا مرجع بازتولید عمومی‌اند.

کنترل کد `e39e2c9`: تعداد ۶۲۲ آزمون موفق، دو مورد POSIX در Windows اجرا‌نشده، ۸۵ مورد خارج
از انتخاب و پنج کنترل CI همان commit شامل PostgreSQL 16/17 و مرورگرِ ساختگی موفق‌اند؛ پیوند CI
در بخش انگلیسی است. این‌ها پذیرش مدل نیستند. mypy با هدف Windows ابتدا نه خطای ویژگی POSIX
در دو ماژول Linux قبلی گزارش کرد؛ اجرای `--platform linux` برای ۱۲۵ فایل موفق بود. کنترل امنیت
POSIX یا قفل وابستگی برای پنهان کردن خطاها تضعیف نشد.
