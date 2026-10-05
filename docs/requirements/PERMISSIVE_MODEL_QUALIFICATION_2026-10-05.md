# Permissively licensed model qualification / پذیرش فنی مدل با مجوز آزاد

Date: **2026-10-05**. Status: **source preparation and partial provisioning; no model cutover**.
تاریخ: **۵ اکتبر ۲۰۲۶**. وضعیت: **آماده‌سازی کد و ورود ناقص فایل؛ بدون تغییر مدل زنده**.

[English CPU guide](../en/CPU_AI.md) / [راهنمای فارسی CPU](../fa/CPU_AI.md).
The [27B result](QWEN38_QUALIFICATION_2026-10-05.md) and
[Flash preparation](QWEN38_FLASH_QUALIFICATION_2026-10-05.md) remain dated evidence, not erased.

## English

### Problem, owner scope and non-goals

The owner confirms planned Bank/customer staff access and explicitly requests a permissively
licensed alternative alongside useful context, final-only thinking and better technical/coding
answers. This authorizes bounded qualification, not unlicensed exposure, unlimited resource use,
automatic promotion or removal of failed gates. Improve measured answers rather than maximizing
parameter count alone. Preserve CPU-only inference, offline operation, deterministic policy,
credential isolation, source/time/scope, audit, response-integrity controls and the exact rollback.

No cloud/GPU dependency, silent runtime download, new target permission, model-owned credential,
private reasoning display/storage, database migration, ESXi change or replacement runtime is part
of this increment. The partial Flash files and historical failures remain protected. This record
is not full production acceptance or a claim of independently verified disaster recovery.

### Official releases and license decision

The current [official Qwen listing](https://github.com/QwenLM/Qwen3.8) identifies Qwen3.8-27B,
Flash-Next and 2.4T-A95B families. Among these reviewed model-weight releases, **27B is the largest
Apache-2.0 Qwen3.8 option**; its FP8 variant does not increase parameters. The
[27B weight license](https://huggingface.co/Qwen/Qwen3.8-27B/blob/1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0/LICENSE)
is Apache-2.0. The GitHub source-code license is not evidence for another model's weight license.

[Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next/blob/de4b8e4d43b917e7706784d8bb445c9af86a3540/LICENSE)
uses Qwen Community License 1.0; the
[2.4T-A95B license](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/blob/207bd685a7e3696cfaff12ded7c6a7ea0f88c996/LICENSE)
is a custom Qwen3.8-Max license. Neither is Apache/MIT-equivalent permissive licensing. Their
business/branding provisions require separate applicability review; customer access must not be
treated as internal-only use. This decision does not declare every customer use prohibited.

The bounded alternative is **Qwen3.5-122B-A10B Q5_K_M**, correctly labeled **3.5**, not renamed
3.8. The [official model](https://huggingface.co/Qwen/Qwen3.5-122B-A10B) advertises 122B total and
10B activated parameters. Its pinned
[weight license](https://huggingface.co/Qwen/Qwen3.5-122B-A10B/blob/dc4d348443bc740c68e2d77492492c11606384d5/LICENSE)
is Apache-2.0. License metadata is reviewed, not model quality or broader organizational clearance.
The protected upstream license copy was verified on the AI guest: **11544 bytes**, SHA-256
`bbedc3fda3305820b977265f01b8619d87570a6739de3a5582c3464840f1e57a`.

### Actual additional 27B attempt

After the earlier 16/32-thread results, one isolated native-only 27B Q8 sample used **48 threads,
16384 context, 256 reasoning-budget tokens and 768 output tokens**. It submitted the unchanged
frozen English coding question. The request exceeded the existing deadline at **120102 ms**;
no accepted final coding answer was obtained. This is a failed timing gate, not a completed
semantic pass or an EN/FA application qualification. Increasing threads and thinking budget
did not establish useful improvement in this sample; no latency percentile is inferred.

The trial PID **5250** was verified stopped and its listener absent. Baseline PID **2187** remained
ready and unchanged at that observation. These are dated process observations, not durable
identifiers or a promise of future availability. The original failed non-string coding invariant
and 15360-input-token/120163-ms near-context result remain in the earlier record. Deadlines and
frozen questions were not relaxed to manufacture acceptance.

### Pinned Q5 identity and source implementation

The [new sibling manifest](../../deploy/inference/qwen3-5-122b-a10b-q5-k-m.candidate.json) pins:

- Quantizer: `bartowski/Qwen_Qwen3.5-122B-A10B-GGUF` at
  `fec8b222a2eddc3346d6b6d7f7c85efea93cd6bf`.
- Upstream reference: `Qwen/Qwen3.5-122B-A10B` at
  `dc4d348443bc740c68e2d77492492c11606384d5`.
- Three Q5_K_M shards: **90429454752 bytes, about 84.22 GiB**. Exact filenames, sizes and SHA-256
  are in the manifest and the
  [pinned quantizer metadata](https://huggingface.co/api/models/bartowski/Qwen_Qwen3.5-122B-A10B-GGUF/revision/fec8b222a2eddc3346d6b6d7f7c85efea93cd6bf?blobs=true).
- The quantizer declares the base-model name and llama.cpp `b9222` quantization, but publishes no
  exact conversion-source revision. `conversion_source_revision_verified=false` remains explicit.
  This is a third-party GGUF, not a Qwen-published GGUF or reproduced conversion.
- Expected architecture `qwen35moe` comes from reviewed lineage. Actual Q5 GGUF/template/CPU loading
  remain unverified; a source architecture enum or a related serving model is not a load test.

The strict sibling schema, artifact validator and mutation-regression tests protect exact identity,
license, all shards and safety bounds. They do not select or approve a model. The original Q4
research record and failed 27B/Flash history remain unchanged. The manifest disallows live selection,
public thinking, GPU layers and runtime downloads; it records 16K context, 2048 output, 128 request
reasoning-budget tokens, 120 seconds and one active/two queued requests. These are trial bounds,
not accepted public capabilities. Schema-valid metadata is not complete-artifact verification.

### Provisioning and resource budget

At this record, protected range provisioning is **in progress and partial**, under supervision.
No complete Q5 shard set has passed full size/hash verification. Partial ranges, successful HTTP
responses or range-local hashes are not a verified model. Transfers use the existing proxy chain
and pinned TLS-verified source; no unattended continuation or runtime download is implied.

The first eight-stream window completed 17179869184 bytes (16 GiB). A bounded 16-stream
comparison hit the 240-second transfer deadline; after all workers stopped, reconciliation found
74 authenticated ranges totalling 19864223744 bytes and six incomplete attempts totalling
1142509656 bytes retained separately. Provisioning returned to finite eight-stream windows.
This is a transfer failure/resource comparison, not an AI request deadline or full artifact hash.

Observed guest: **80 vCPUs, 257905 MiB usable RAM (about 251.86 GiB), three guest NUMA nodes**.
The added protected 400-GiB volume is already prepared; do not format it again. Guest NUMA does
not prove physical placement. Retain the datastore free-space guard, project ceiling and other
services' headroom; no extra storage/VM allocation is inferred from this packet.

Proposed isolated Q5 trial: **128-GiB MemoryMax**, initially 32 threads/CPU equivalents, then a
bounded 48-thread/quota comparison if observed headroom permits; 16K context and the 120-second
deadline remain. These are **not applied or benchmark-optimal settings**. Baseline MemoryMax
remains 96 GiB/18 CPU equivalents. The two memory maxima total 224 GiB, leaving about 27.86 GiB
before OS/API/other needs. Actual resident weights, recurrent state, attention cache, prefill
buffers, allocator and page cache must be measured before any claim of fit.

Q8 weights would be about 123.49 GiB, 39.27 GiB larger than Q5. Q5 may reduce bandwidth and memory
pressure, but quantization/dequantization affects CPU behavior: neither speed nor accuracy is
guaranteed. Precharged model page cache can make cgroup peaks undercount the complete footprint.
Observe RSS/PSS, cgroup current/peak, guest available memory, swap and pressure together; avoid
double counting shared cache. Stop and reconcile the trial on pressure, baseline degradation or
deadline failure. Do not increase a limit to conceal failure.

### Next tasks, acceptance, rollback and evidence

1. Reconcile exact existing ranges, complete the finite import and verify every full shard's size
   and SHA-256. Preserve incomplete attempts; never select them.
2. Inspect verified actual GGUF metadata, tokenizer/template and CPU compatibility with pinned
   llama.cpp `v0.4.1` / `b29c606e28a01b1bc8c1351026a0fa6e616bf6c4` before protected loading.
3. Qualify complete memory fit and matched frozen EN/FA standard/coding/technical cases. Then test
   final-only thinking/privacy and context admission within the same deadlines and queue bounds.
4. Only after useful semantic results, qualify matched app/API, owner-scoped saved conversations,
   fresh selected-source evidence/audit, stale/partial/absent/injection behavior, dependency/queue
   recovery, actual WAN-isolated fresh generation/restart, applicable VM cold start and exact rollback.

| Gate | Outcome at this record |
|---|---|
| Pinned permissive weight-license metadata/copy | passed within stated license-metadata scope |
| New 27B 48-thread native coding sample | failed deadline; no accepted final answer |
| Q5 source manifest/schema/regression validation | implemented; source tests, not model acceptance |
| Complete Q5 import/hash | partial provisioning; complete set unverified |
| Actual Q5 metadata/template/CPU load/full memory fit | not_run |
| Q5 EN/FA standard/thinking/context semantics and latency | not_run |
| Q5 matched application/evidence/audit/WAN/rollback | not_run |
| Public Q5 thinking/model selection | disabled; no cutover |

Serving model remains `nextops-qwen3-5-35b-a3b-q4-k-m`; native runtime, baseline limits and public
thinking-off remain unchanged. Import rollback requires no live restart because serving links/config
are untouched. Preserve exact baseline artifacts and private staged ranges. A later live profile
change requires recorded acceptance, retained exact configuration and timed rollback/reapply;
no automatic deletion, schema downgrade or private reasoning retention. Keep private transfer logs,
credentials and infrastructure inventory outside Git. Current state/index updates must point here
without rewriting historical acceptance or claiming these unrun gates passed.

<div dir="rtl">

## فارسی

### مسئله، دامنهٔ مجاز و موارد خارج از این گام

مالک، دسترسی آیندهٔ کارکنان بانک و مشتری را تأیید کرده و صریحاً نامزدی با مجوز آزاد خواسته است؛
همراه با زمینهٔ کاربردی، استدلال با نمایش صرفاً پاسخ نهایی و پاسخ فنی/کدنویسی بهتر. این درخواست،
مجوز آزمون محدود است، نه ارائهٔ بدون مجوز، مصرف نامحدود منابع، انتخاب خودکار یا حذف معیار ناموفق.
هدف، بهبود اندازه‌گیری‌شدهٔ پاسخ است، نه صرفاً افزایش شمار پارامتر. پردازش CPU محلی، کارکرد آفلاین،
سیاست قطعی، جداسازی اعتبارنامه، منشأ/زمان/دامنه، ممیزی، کنترل صحت پاسخ و بازگشت دقیق حفظ می‌شوند.

وابستگی ابر/GPU، دریافت پنهانی در زمان اجرا، مجوز مقصد تازه، اعتبارنامه در اختیار مدل، نمایش یا
ذخیرهٔ استدلال خصوصی، migration پایگاه، تغییر ESXi یا جایگزینی runtime در دامنه نیست. فایل‌های
ناقص Flash و شکست‌های پیشین حفظ‌اند. این گزارش پذیرش کامل تولید یا اثبات مستقل بازیابی بحران نیست.

### انتشار رسمی و تصمیم مربوط به مجوز

[فهرست رسمی Qwen](https://github.com/QwenLM/Qwen3.8)، خانواده‌های Qwen3.8-27B، Flash-Next و
2.4T-A95B را معرفی می‌کند. در انتشار وزن‌های بررسی‌شده، **27B بزرگ‌ترین گزینهٔ Qwen3.8 با مجوز
Apache-2.0 است**؛ نسخهٔ FP8 آن پارامتر بیشتری ندارد.
[مجوز وزن 27B](https://huggingface.co/Qwen/Qwen3.8-27B/blob/1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0/LICENSE)
Apache-2.0 است؛ مجوز کد GitHub، مجوز وزن مدل دیگری را ثابت نمی‌کند.

[Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next/blob/de4b8e4d43b917e7706784d8bb445c9af86a3540/LICENSE)
از Qwen Community License 1.0 و
[2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/blob/207bd685a7e3696cfaff12ded7c6a7ea0f88c996/LICENSE)
از مجوز اختصاصی Qwen3.8-Max استفاده می‌کنند. هیچ‌کدام معادل مجوز آزاد Apache/MIT نیستند؛ شمول
شرط‌های کسب‌وکار و نام‌گذاری جدا بررسی شود. دسترسی مشتری، استفادهٔ صرفاً داخلی محسوب نشود؛ از این
نتیجه نیز ممنوع‌بودن همهٔ کاربردهای مشتری استنباط نمی‌شود.

نامزد محدود، **Qwen3.5-122B-A10B Q5_K_M** است؛ نام درست آن **3.5** است، نه 3.8.
[مدل رسمی](https://huggingface.co/Qwen/Qwen3.5-122B-A10B)، ۱۲۲ میلیارد پارامتر کل و ۱۰ میلیارد
پارامتر فعال را اعلام می‌کند.
[مجوز ثابت وزن](https://huggingface.co/Qwen/Qwen3.5-122B-A10B/blob/dc4d348443bc740c68e2d77492492c11606384d5/LICENSE)
Apache-2.0 است. بازبینی فرادادهٔ مجوز، پذیرش کیفیت یا تأیید جامع سازمانی نیست. نسخهٔ محافظت‌شدهٔ
مجوز اصلی روی مهمان AI با اندازهٔ **۱۱۵۴۴ بایت** و SHA-256 زیر تأیید شد:
`bbedc3fda3305820b977265f01b8619d87570a6739de3a5582c3464840f1e57a`.

### تلاش تازهٔ واقعی با 27B

پس از آزمون‌های ۱۶/۳۲ رشته، یک نمونهٔ مستقل و صرفاً native از 27B Q8 با **۴۸ رشته، زمینهٔ
۱۶۳۸۴، بودجهٔ ۲۵۶ توکن استدلال و سقف ۷۶۸ توکن خروجی**، همان پرسش ثابتِ انگلیسی کدنویسی را
دریافت کرد. درخواست در **۱۲۰۱۰۲ میلی‌ثانیه** از مهلت گذشت؛ پاسخ نهاییِ پذیرفته‌شده‌ای به دست
نیامد. این شکست معیار زمان است، نه موفقیت معنایی یا پذیرش دوزبانهٔ برنامه. افزایش رشته و بودجهٔ
استدلال، بهبود کاربردی این نمونه را ثابت نکرد؛ صدک تأخیر نیز از آن استنباط نمی‌شود.

توقف PID آزمایشی **5250** و نبود listener تأیید شد؛ PID خط مبنا **2187** در همان مشاهده آماده
و بدون تغییر بود. این شناسه‌ها مشاهدهٔ تاریخ‌دارند، نه شناسهٔ ماندگار یا تضمین دسترس‌پذیری آینده.
شکست پیشینِ شرط ورودی غیررشته‌ای و آزمون زمینهٔ ۱۵۳۶۰ توکنی با ۱۲۰۱۶۳ میلی‌ثانیه در گزارش قبلی
باقی‌اند. برای ساختن نتیجهٔ موفق، مهلت یا پرسش ثابت تغییر نکرد.

### هویت ثابت Q5 و پیاده‌سازی در کد

[manifest مستقل تازه](../../deploy/inference/qwen3-5-122b-a10b-q5-k-m.candidate.json) موارد زیر را
ثبت می‌کند:

- تبدیل‌کننده: `bartowski/Qwen_Qwen3.5-122B-A10B-GGUF` با نسخهٔ
  `fec8b222a2eddc3346d6b6d7f7c85efea93cd6bf`.
- مرجع مدل اصلی: `Qwen/Qwen3.5-122B-A10B` با نسخهٔ
  `dc4d348443bc740c68e2d77492492c11606384d5`.
- سه فایل Q5_K_M: **۹۰۴۲۹۴۵۴۷۵۲ بایت، حدود ۸۴٫۲۲ GiB**. نام، اندازه و SHA-256 دقیق در
  manifest و [فرادادهٔ نسخهٔ ثابت](https://huggingface.co/api/models/bartowski/Qwen_Qwen3.5-122B-A10B-GGUF/revision/fec8b222a2eddc3346d6b6d7f7c85efea93cd6bf?blobs=true) آمده‌اند.
- تبدیل‌کننده، نام مدل پایه و کوانتیزه‌سازی با llama.cpp `b9222` را اعلام می‌کند، اما نسخهٔ دقیق
  منبع تبدیل را منتشر نکرده است؛ `conversion_source_revision_verified=false` صریح باقی می‌ماند.
  این GGUF شخص ثالث است، نه انتشار GGUF توسط Qwen یا تبدیلِ بازتولیدشده.
- معماری موردانتظار `qwen35moe` از تبار اعلامی می‌آید. GGUF، قالب و بارگذاری CPU این Q5 هنوز
  تأیید نشده‌اند؛ enum کد یا اجرای مدل هم‌خانواده، آزمون بارگذاری این فایل نیست.

schema سخت‌گیرانهٔ مستقل، اعتبارسنج فایل و آزمون‌های تغییر نامعتبر، هویت، مجوز، همهٔ فایل‌ها و
حدود ایمنی را حفظ می‌کنند؛ انتخاب یا پذیرش مدل انجام نمی‌دهند. رکورد پژوهشی Q4 و شکست‌های
27B/Flash بدون تغییرند. انتخاب زنده، استدلال عمومی، لایهٔ GPU و دانلود زمان اجرا ممنوع‌اند؛ حدود
آزمون شامل زمینهٔ 16K، خروجی ۲۰۴۸، بودجهٔ درخواست استدلال ۱۲۸، مهلت ۱۲۰ ثانیه، یک درخواست فعال
و دو درخواست منتظر است. این حدود، قابلیت عمومی پذیرفته‌شده نیستند؛ صحت schema، هش کامل وزن نیست.

### آماده‌سازی فایل و بودجهٔ منابع

در زمان این گزارش، دریافت محافظت‌شدهٔ بخش‌ها **در حال اجرا و ناقص** است و نظارت می‌شود. مجموعهٔ
کامل Q5 هنوز اندازه/هش کاملِ موفق ندارد. بخش ناقص، پاسخ HTTP موفق یا هشِ بخش، مدل تأییدشده نیست.
انتقال از زنجیرهٔ پراکسی موجود و منبع ثابت با TLS معتبر انجام می‌شود؛ ادامهٔ بدون نظارت یا دریافت
زمان اجرا از این مشاهده استنباط نشود.

نخستین پنجرهٔ هشت‌انتقالی، ۱۷۱۷۹۸۶۹۱۸۴ بایت، یعنی ۱۶ GiB را کامل کرد. مقایسهٔ محدود با
۱۶ انتقال از مهلت ۲۴۰ ثانیهٔ دریافت گذشت. پس از توقف همهٔ فرایندهای انتقال، تطبیق، ۷۴ بخش
با هش محلی و مجموع ۱۹۸۶۴۲۲۳۷۴۴ بایت و شش تلاش ناقص با مجموع ۱۱۴۲۵۰۹۶۵۶ بایت را نشان داد؛
تلاش‌های ناقص جدا حفظ شدند. آماده‌سازی به پنجره‌های محدودِ هشت‌انتقالی برگشت. این شکست دریافت
و مقایسهٔ منابع است، نه مهلت درخواست AI یا هش کامل مدل.

مشاهدهٔ مهمان: **۸۰ vCPU، حافظهٔ قابل‌استفادهٔ ۲۵۷۹۰۵ MiB، حدود ۲۵۱٫۸۶ GiB و سه گرهٔ NUMA
مهمان**. حجم محافظت‌شدهٔ ۴۰۰ GiB قبلاً آماده شده و دوباره قالب‌بندی نشود. NUMA مهمان، جای‌گیری
فیزیکی را ثابت نمی‌کند. حاشیهٔ آزاد datastore، سقف پروژه و منابع دیگر خدمات حفظ شوند؛ تخصیص تازهٔ
دیسک/ماشین از این بسته مجاز یا اجراشده تلقی نشود.

آزمون مستقل پیشنهادی Q5: **MemoryMax برابر ۱۲۸ GiB**، ابتدا ۳۲ رشته/سهم معادل CPU و سپس، تنها
با حاشیهٔ مشاهده‌شده، مقایسهٔ محدود ۴۸ رشته/سهم CPU؛ زمینهٔ 16K و مهلت ۱۲۰ ثانیه حفظ می‌شوند.
این‌ها **تنظیم اجراشده یا بهینهٔ اثبات‌شده نیستند**. سقف خط مبنا ۹۶ GiB و معادل ۱۸ CPU است؛
جمع دو سقف حافظه ۲۲۴ GiB و حاشیهٔ اولیه حدود ۲۷٫۸۶ GiB پیش از نیاز سیستم‌عامل/API/دیگر مصرف‌هاست.
وزن مقیم، حالت بازگشتی، کش attention، بافر prefill، تخصیص‌دهنده و کش فایل باید واقعاً اندازه‌گیری
شوند تا جا شدن مدل قابل ادعا باشد.

وزن Q8 حدود ۱۲۳٫۴۹ GiB، یعنی ۳۹٫۲۷ GiB بیشتر از Q5 است. Q5 ممکن است فشار حافظه/پهنای‌باند را
کم کند، اما رفتار کوانتیزه‌سازی و بازگشایی آن روی CPU سنجیده شود؛ سرعت یا درستی تضمین نیست.
کش فایل که پیش‌تر حساب شده، ممکن است اوج cgroup را کمتر از مصرف کامل نشان دهد. RSS/PSS، مصرف
جاری/اوج cgroup، حافظهٔ در دسترس مهمان، swap و فشار با هم دیده و کش مشترک دوباره‌شماری نشود.
با فشار منابع، افت خط مبنا یا شکست مهلت، آزمون متوقف و وضعیت تطبیق داده شود؛ سقف برای پنهان‌کردن
شکست بزرگ نشود.

### گام بعد، پذیرش، بازگشت و شواهد

۱. بخش‌های موجود دقیق تطبیق، ورود محدود تکمیل و اندازه/SHA-256 کاملِ هر فایل تأیید شود؛ تلاش
ناقص حفظ و هرگز انتخاب نشود.
۲. GGUF واقعیِ تأییدشده، tokenizer/قالب و سازگاری CPU با llama.cpp ثابتِ `v0.4.1` و commit
`b29c606e28a01b1bc8c1351026a0fa6e616bf6c4` پیش از بارگذاری محافظت‌شده بررسی شوند.
۳. مصرف کامل و پرسش‌های ثابتِ همسان دوزبانه برای پاسخ استاندارد، فنی و کدنویسی پذیرفته شوند؛ سپس
استدلال با خروجی صرفاً نهایی، حریم خصوصی و پذیرش زمینه در همان مهلت/صف سنجیده شوند.
۴. فقط پس از نتیجهٔ معنایی کاربردی، مسیر برنامه/API، مالکیت گفتگو، شاهد تازهٔ منبع انتخاب‌شده و
ممیزی، شاهد کهنه/ناقص/غایب/تزریق، خرابی/بازیابی وابستگی و صف، پاسخ تازه و restart با WAN مسدود،
شروع سرد VMِ قابل‌اعمال و بازگشت دقیق جدا پذیرفته شوند.

| معیار | نتیجه در زمان گزارش |
|---|---|
| فراداده/نسخهٔ ثابتِ مجوز آزاد وزن | موفق در همان دامنهٔ مجوز/فراداده |
| نمونهٔ native کدنویسی 27B با ۴۸ رشته | شکست مهلت؛ بدون پاسخ نهایی پذیرفته‌شده |
| manifest/schema/آزمون پسرفت Q5 | پیاده‌سازی در کد؛ آزمون کد، نه پذیرش مدل |
| ورود/هش کامل Q5 | آماده‌سازی ناقص؛ مجموعهٔ کامل تأیید نشده |
| metadata/قالب/بارگذاری CPU/مصرف کامل Q5 | اجرا‌نشده |
| معنا و زمان پاسخ استاندارد/استدلال/زمینهٔ دوزبانه Q5 | اجرا‌نشده |
| برنامه/شاهد/ممیزی/WAN/بازگشت Q5 | اجرا‌نشده |
| استدلال عمومی و انتخاب Q5 | غیرفعال؛ بدون گذار زنده |

مدل زنده `nextops-qwen3-5-35b-a3b-q4-k-m` است؛ runtime، حدود خط مبنا و خاموشی استدلال عمومی
ثابت‌اند. بازگشتِ آماده‌سازی فایل به restart نیاز ندارد؛ لینک/تنظیم زنده دست‌نخورده‌اند. فایل دقیق
خط مبنا و بخش‌های خصوصی حفظ شوند. تغییر زندهٔ بعدی به پذیرش ثبت‌شده، تنظیم دقیقِ محفوظ و بازگشت/
استقرار دوبارهٔ زمان‌دار نیاز دارد؛ حذف خودکار، downgrade پایگاه یا حفظ استدلال خصوصی مجاز نیست.
log انتقال، اعتبارنامه و موجودی خصوصی بیرون Git بمانند. وضعیت/فهرست جاری به این گزارش ارجاع دهند،
بدون بازنویسی پذیرش تاریخی یا موفق نامیدن معیار اجرا‌نشده.

</div>
