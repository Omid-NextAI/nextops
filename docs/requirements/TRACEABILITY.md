# Original-requirement traceability / ردیابی نیازهای اولیه

CAP-01–CAP-06 (2026-10-03) map to [capability specification](../en/AI_CAPABILITY_SPEC.md),
`inference/advisory_prompt.py`, conversation selector/contracts, provider/API tests and the fresh
18-case `qualify_thinking.py --scope capabilities` corpus. Source implemented; 502 local tests
and five CI jobs pass. Native18 completions/four exact checks pass, but technical/coding semantics
fail and four offline guard redirects expose an intent gap. No promotion. See [testing](../en/TESTING.md).
CM-03's whole-pair/six-turn/12K bounds and
omissions remain; oversized pairs may now be skipped for older fitting pairs. Original integrations,
live-evidence permissions and offline gates are preserved.

CAP-01 تا CAP-06 (۳ اکتبر ۲۰۲۶) به [مشخصات](../fa/AI_CAPABILITY_SPEC.md)، سیاست عمومی،
انتخاب‌گر/قرارداد گفت‌وگو، آزمون provider/API و مجموعهٔ تازهٔ ۱۸موردیِ
`qualify_thinking.py --scope capabilities` متصل‌اند. کد پیاده، ۵۰۲ آزمون محلی و پنج کنترل CI
موفق‌اند. هجده تولید/چهار کنترل دقیق موفق‌اند، اما معنا/کدنویسی شکست خورد و چهار تغییر پاسخ
در بازپخش، شکاف قصد را نشان داد. استقرار انجام نشد؛ [آزمون](../fa/TESTING.md) مبناست.
جفت کامل، سقف شش تبادل/۱۲ هزار نویسه و اعلام حذفِ CM-03 حفظ‌اند؛ جفت بزرگ
می‌تواند به سود جفت قدیمی‌ترِ جاگرفتنی کنار رود. اتصال اولیه، مجوز شاهد زنده و معیار آفلاین حفظ‌اند.

MU-01–MU-09 (original sections 9, 17, 25, 27; 2026-10-03) map to
[MODEL_UPGRADE_SPEC](../en/MODEL_UPGRADE_SPEC.md), the pinned Qwen3.6 candidate/schema,
expanded-inference and qualification-runner tests. Fixed source alias, trusted no-reasoning-memory
controls, candidate-port exclusion and new fourteen-case corpus are implemented in source only.
491 local tests and all five source CI jobs pass, including PostgreSQL16/17. Full desktop/server
integrity, protected import and CPU load passed. All 56 synthetic requests completed; exact
arithmetic/short recall and thinking final envelopes passed, but standard/thinking technical
accuracy failed for both models. New-model context, matched user-facing/offline/rollback gates
remain not_run. Owner-bounded total 500-GiB growth includes staging; no resize occurred.
Serving69/current35, disabled thinking, failed earlier gates and original integrations remain unchanged.

MU-01 تا MU-09 (بخش‌های اصلی ۹، ۱۷، ۲۵ و ۲۷؛ ۳ اکتبر ۲۰۲۶) به
[مشخصات ارتقای مدل](../fa/MODEL_UPGRADE_SPEC.md)، رکورد و schema ثابتِ Qwen3.6 و آزمون لایهٔ
استنتاج و ابزار سنجش متصل‌اند. شناسهٔ ثابت، منع نگه‌داری استدلال، ردِ پورت خدمت جاری و مجموعهٔ
تازهٔ چهارده‌موردی فقط در کد پیاده شده‌اند. ۴۹۱ آزمون محلی و پنج کنترل CI، از جمله PostgreSQL16/17،
موفق‌اند. تمامیت دسکتاپ/سرور، ورود محافظت‌شده و بارگذاری CPU موفق شدند. هر ۵۶ پاسخ آزمایشی
تکمیل شد؛ محاسبه/یادآوری کوتاهِ دقیق و قالب نهایی موفق‌اند، اما درستی فنیِ معمولی و استدلالی
در هر دو مدل شکست خورد. زمینه، مرز کاربر، آفلاین و بازگشتِ مدل تازه اجرا نشده‌اند. سقف رشدِ
مجموعاً ۵۰۰ GiB مالک، فایل موقت را هم شامل می‌شود؛ منابع افزایش نیافتند. خدمت69/مدل35،
استدلال خاموش، شکست قبلی و همهٔ اتصال‌های اصلی بدون تغییر حفظ شده‌اند.

CM-05/CM-06 requalification, 2026-10-03: installed 69c9260 thinking digit-format and real
near-16K deadline failed. Source-only envelope/format hardening maps to expanded-inference tests;
the opt-in exact-prompt/token runner maps to `tests/unit/test_thinking_qualification.py`.
Post-timeout standard browser/history/two text-free audits passed, not enabled-thinking acceptance.
Current [testing](../en/TESTING.md) and release gates preserve failures and all not-run dependencies.

سنجش دوبارهٔ CM-05/CM-06، ۳ اکتبر ۲۰۲۶: قالبِ فقط رقم و مهلت واقعیِ نزدیک 16K در استدلالِ
نصب‌شدهٔ 69c9260 شکست خوردند. سخت‌گیریِ صرفاً کدیِ قالب/شکل خروجی به آزمون استنتاجِ گسترش‌یافته
و ابزارِ دارای انتخاب صریح و همان پرسش/توکن به `tests/unit/test_thinking_qualification.py`
متصل‌اند. مرورگر/سابقهٔ معمولی و دو ممیزیِ بدون متن پس از پایان مهلت موفق‌اند، نه پذیرشِ
استدلال فعال. [آزمون](../fa/TESTING.md) و معیارهای انتشار، شکست و وابستگیِ اجرا‌نشده را حفظ‌اند.

Conversation expansion (sections 3, 9, 17, 25, 27; 2026-09-30): owner-scoped PostgreSQL memory,
bounded six-pair context and actual token admission serve controlled b5e74f9/35B standard chat.
CM-01–CM-08 map to conversation unit/integration/browser tests and
[the bounded packet](../en/CONVERSATION_MEMORY_SPEC.md). Short bilingual follow-ups, audit,
matched rollback and four-guest WAN/reboot passed. Thinking failed and is disabled; full-budget
context and broad answer semantics are not accepted. The header light/dark switch is live with
unchanged OCS assets; [testing](../en/TESTING.md) distinguishes fixture and live evidence.

گسترش گفت‌وگو (بخش‌های ۳، ۹، ۱۷، ۲۵ و ۲۷؛ ۹ مهر ۱۴۰۵): حافظهٔ مالک‌محور PostgreSQL، زمینهٔ
حداکثر شش جفت و پذیرش واقعی توکن در گفت‌وگوی معمولیِ کنترل‌شدهٔ b5e74f9/35B زنده‌اند.
CM-01 تا CM-08 به آزمون واحد، پایگاه و مرورگر و [مشخصات](../fa/CONVERSATION_MEMORY_SPEC.md)
متصل‌اند. پیگیری کوتاهِ دوزبانه، ممیزی، بازگشت هماهنگ و قطع WAN/شروع دوبارهٔ چهار مهمان
موفق‌اند. استدلال شکست خورده و غیرفعال است؛ زمینهٔ ظرفیت کامل و معنای گستردهٔ پاسخ پذیرفته
نیستند. دکمهٔ روشن/تیره با نشان ثابت OCS زنده است؛ [آزمون](../fa/TESTING.md) شاهد ساختگی و
زنده را جدا می‌کند.

Controlled NOC/SOC increment (sections 3, 9, 17, 25, 27; 2026-09-29): exact 862d311/35B preserves
OCS brand and provides responsive conversation, safe text/code/copy and bounded general-only context; no persistent memory schema,
retrieval or new connector. 363 unit/API checks (two Windows POSIX skips), twelve browser fixtures,
five CI jobs, exact fresh offline package, nine live browser/API cases, three audit/hash pairs and
exact b346c3e source rollback passed. Technical RTL isolation and the named EN/FA blanket-health
guard are live; independent technical quality remains partial. Current-state/history cannot
authorize access or become live evidence. The [bounded packet](NOC_SOC_WORKSPACE_SPEC.md) and paired
testing guides govern this bounded acceptance; exact-release WAN/VM gates remain not run. Earlier
35B and unrun/failed qualification records remain authoritative for their exact revisions.

برش کنترل‌شدهٔ NOC و SOC (بخش‌های ۳، ۹، ۱۷، ۲۵ و ۲۷؛ ۷ مهر ۱۴۰۵): نسخهٔ دقیق 862d311 و 35B،
نشان و رنگ OCS را حفظ کرده و گفت‌وگوی واکنش‌گرا، نمایش و کپی ایمن متن و کد و زمینهٔ محدودِ
صرفاً عمومی را ارائه می‌کند؛ ساختار حافظهٔ ماندگار،
بازیابی سند یا اتصال تازه نداریم. ۳۶۳ آزمون واحد/API با دو مورد POSIX کنارگذاشته‌شده در Windows،
دوازده مورد مرورگرِ ساختگی، پنج کنترل CI، بستهٔ تازهٔ آفلاین، نُه مورد زنده، سه تطبیق ممیزی و هش
و بازگشت دقیق کد به b346c3e موفق‌اند. جداسازی جهت متن فنی و کنترل مشخصِ دوزبانهٔ نتیجه‌گیری
سلامت مستقرند؛ صحت فنیِ مستقل ناقص است. سابقه مجوز یا شاهد زنده نمی‌سازد.
[مشخصات](NOC_SOC_WORKSPACE_SPEC.md) و راهنمای آزمون دوزبانه مبنای پذیرش محدودند؛ WAN و VM همین
انتشار اجرا نشده‌اند. رکوردهای 35B و پذیرش اجرا‌نشده یا ناموفقِ نسخه‌های قبلی حفظ‌اند.

Selected 35B trace (sections 9, 10, 19, 25; 2026-09-29): protected pinned artifact, exact source
95c6e50/offline wheel and five CI jobs passed. Twelve API and twelve browser cases plus eight
read-only audit/hash pairs, exact 8B/app/API rollback and six final re-promotion confirmations
passed. Canonical CPU/file-focus ownership and all authorization/resource/offline-design boundaries
remain. Metadata identity/context/template/lineage limits are tracked. Prior raw failures are
preserved; held-out semantics are partial and current server-WAN/full-VM gates are not run.
Controlled selection is not production acceptance. Current source state supersedes dated records below.

ردیابی 35B منتخب (بخش‌های ۹، ۱۰، ۱۹ و ۲۵؛ ۷ مهر ۱۴۰۵): فایل تثبیت‌شده و محافظت‌شده، کد دقیق
95c6e50، wheel آفلاین و پنج کنترل CI تأیید شدند. دوازده آزمون API و دوازده مورد مرورگر، هشت
تطبیق فقط‌خواندنیِ ممیزی و هش، بازگشت دقیق 8B و برنامه/API و شش تأیید نهاییِ استقرار مجدد
موفق‌اند. معنای CPU و تمرکز فایل در اختیار برنامه و مرزهای مجوز، منابع و طراحی آفلاین حفظ‌اند.
شناسهٔ فراداده، context، قالب و محدودیت زنجیرهٔ تبدیل ثبت‌اند. شکست‌های خام پیشین حفظ شده‌اند؛
معنای مستقل ناقص و WAN سرور و شروع سردِ کامل VM همین انتشار اجرا‌نشده‌اند. انتخاب کنترل‌شده،
پذیرش تولید نیست. وضعیت جاری بر رکوردهای تاریخ‌دارِ زیر تقدم دارد.

CPU semantic repair trace (sections 9, 19, 25; 2026-09-29): 35B protected import and fourteen
bounded completions passed; first guarded twelve API completions passed, but Persian CPU-idle
meaning failed. Exact model/source rollback restored fresh 8d1f1d2/8B. Source-only deterministic
CPU focus validates reviewed keys, units, range and ambiguity, preserves provenance/audit and
refuses unavailable observations. 327 local tests passed with two POSIX skips; new live/CI/package
acceptance remains next. Historical failures and independent/offline gates are not erased.

ردیابی اصلاح معنای CPU (بخش‌های ۹، ۱۹ و ۲۵؛ ۷ مهر ۱۴۰۵): ورود محافظت‌شدهٔ 35B و چهارده تولید
محدود موفق بودند؛ دوازده تولید API در آزمون محافظت‌شدهٔ نخست کامل شدند، اما معنای فارسیِ
بیکاری پردازنده ناموفق بود. بازگشت دقیق مدل و کد، 8d1f1d2 و 8B را با تولید تازه برگرداند.
کنترلِ تمرکز CPU که هنوز فقط در کد است، کلید بررسی‌شده، واحد، دامنهٔ عدد و ابهام را می‌سنجد؛
منشأ و ممیزی را حفظ و شاهد غیرقابل‌استفاده را رد می‌کند. ۳۲۷ آزمون محلی موفق و دو مورد POSIX
اجرانشده‌اند؛ پذیرش تازهٔ زنده، CI و بسته گام بعد است. شکست‌های تاریخی و معیار مستقل و آفلاین حفظ‌اند.

Focused-prompt trace (sections 9, 19, 25; 2026-09-29): source-only concise output instruction,
eight EN/FA/API fixtures, no removed focused evidence/provenance, no budget/audit/guard change.
Actual raw completion and existing failed browser/semantic gates remain unaccepted.

ردیابی دستور متمرکز (بخش‌های ۹، ۱۹ و ۲۵؛ ۷ مهر ۱۴۰۵): دستور خروجی کوتاه فقط در کد و هشت
آزمون API دوزبانه؛ شاهد مرتبط یا منشأ حذف و سقف و ممیزی و کنترل‌ها تغییر نکرده‌اند. کامل‌شدن
خامِ واقعی و معیارهای ناموفق قبلیِ مرورگر و معنایی هنوز پذیرفته نیستند.

Current continuation trace (sections 9, 10, 19, 25; 2026-09-29): corrected 30B-A3B selection rejected
for Persian technical errors and repeated raw completion failure. Exact rollback passed; source
8d1f1d2/original 8B retains the independently verified direction fix. Twelve API literal/code checks
and four stored audit/hash pairs passed; strict raw-completion browser failed final Persian
filesystem case after eleven checks. Baseline 8B reproduced that ceiling. A separate display-only
check passed, not raw completion. Qwen3.5-35B-A3B pinned quantizer/provenance and source-only trusted
non-thinking compatibility are in progress; import/quality/serving acceptance are not inferred.

ردیابی جاریِ ادامه (بخش‌های ۹، ۱۰، ۱۹ و ۲۵؛ ۷ مهر ۱۴۰۵): انتخاب اصلاح‌شدهٔ 30B-A3B به‌دلیل
خطای فنی فارسی و شکست مکررِ کامل‌شدن متن خام رد شد. بازگشت دقیق تأیید شد؛ 8d1f1d2 و 8B اصلی،
اصلاح مستقلِ جهت پاسخ را حفظ می‌کنند. دوازده بررسی لفظی و هشِ API و چهار جفت ممیزی و هش
ذخیره‌شده موفق بودند؛ مرورگر سخت‌گیرانه پس از یازده مورد، تولید خامِ فایل‌سیستم فارسی را
نگذراند. خط مبنای 8B نیز به همین سقف رسید. آزمون جداگانهٔ نمایش موفق بود، نه کامل‌شدن مدل.
تثبیت سازنده و منبعِ Qwen3.5 با 35B-A3B و پشتیبانیِ حالت بدون تفکرِ معتبر فقط در کد در جریان
است؛ ورود، کیفیت یا انتخاب زنده نتیجه گرفته نشوند.

Earlier trial trace (sections 9, 10, 19, 25; 2026-09-29): 30B-A3B import/deadline checks passed;
raw qualifier/Persian review is partial. The guarded app trial returned twelve authenticated
responses, but Latin-prefix Persian LTR rendering failed browser review. Exact model and app/API
rollback restored c4351fd/8B with fresh generation. The response-locale fix passed seven local
browser fixtures; live requalification, full semantic, WAN and VM gates are not inferred.

ردیابی پیشینِ آزمون (بخش‌های ۹، ۱۰، ۱۹ و ۲۵؛ ۷ مهر ۱۴۰۵): فایل و مهلت 30B-A3B تأیید شدند؛
قیدهای متن مدل و کیفیت فارسی هنوز کاملاً پذیرفته نیستند. آزمون موقت برنامه دوازده پاسخ
احرازهویت‌شده داشت، اما نمایش LTR پاسخ فارسی با واژهٔ لاتین در ابتدا، آزمون مرورگر را
نگذراند. بازگشت دقیق مدل و برنامه/API، c4351fd و 8B را با تولید تازه برگرداند. اصلاح جهت بر
پایهٔ زبان پاسخ، هفت آزمون محلی مرورگر را گذرانده است؛ پذیرش زنده، کیفیت کامل، WAN و VM
نتیجه گرفته نشوند.

Earlier 32B trace (sections 9, 10, 19, 25; 2026-09-29): 32B protected size/hash import
passed, eleven matched answers completed, then Persian stale evidence exceeded 120 seconds.
Latency failed; quality is partial and injection cases unrun. Serving 8B is unchanged. Official
30B-A3B is separately pinned for bounded provisioning/comparison under identical CPU/runtime,
prompt, deadline and queue limits. Source alias support is not selection or production acceptance.

ردیابی پیشینِ 32B (بخش‌های ۹، ۱۰، ۱۹ و ۲۵؛ ۷ مهر ۱۴۰۵): ورود محافظت‌شدهٔ 32B با اندازه
و هش تأیید و یازده پاسخ همسان کامل شدند؛ سپس پرسش فارسیِ شاهد قدیمی از ۱۲۰ ثانیه گذشت. تأخیر
ناموفق، کیفیت ناقص و موارد تزریق اجرا‌نشده‌اند. 8B مستقر تغییر نکرد. 30B-A3B رسمی جداگانه برای
آماده‌سازی و مقایسهٔ محدود تثبیت شده است؛ CPU، محیط اجرا، دستور، مهلت و صف ثابت می‌مانند.
پشتیبانی شناسه در کد، انتخاب مدل یا پذیرش تولید نیست.

Earlier larger-model trace (sections 9, 10, 19, 25; 2026-09-29): matched 8B/14B development review used
fourteen bilingual cases per model at 384 tokens. Both completed, but 14B factual/arithmetic and
evidence-qualifier failures prohibit selection. Official 32B has pinned source/license/size/hash
metadata and source-only typed identity support; its provisioning is not verified import or live
acceptance. Existing CPU runtime, 8B serving path, resources, policy, audit and rollback persist.

ردیابی پیشینِ مدل بزرگ‌تر (بخش‌های ۹، ۱۰، ۱۹ و ۲۵؛ ۷ مهر ۱۴۰۵): بازبینی توسعه‌ایِ همسان 8B و 14B،
چهارده مورد دوزبانه برای هر مدل با سقف ۳۸۴ توکن داشت. هر دو کامل شدند، اما واقعیت و محاسبهٔ
نادرست و ضعف قیدِ شاهد در 14B مانع انتخاب است. منبع، مجوز، اندازه و هشِ 32B رسمی تثبیت و
شناسهٔ نوع‌دار آن فقط در کد اضافه شده است؛ آماده‌سازی، ورودِ تأییدشده یا پذیرش زنده نیست.
محیط CPU، مسیر مستقر 8B، منابع، سیاست، ممیزی و امکان بازگشت حفظ شده‌اند.

Live clarity trace (sections 9, 19, 25; 2026-09-29): `c4351fd` now serves application and inference
API. Twelve fresh bilingual authenticated API cases and seven browser cases across two contexts
cover the named greeting, general-knowledge, unknown-live-state and focus/scope regressions.
Code-digest correlation, ordered app/API rollback and re-promotion were verified. Full held-out
quality is partial, exact-release WAN/VM cold start unrun, and larger-model quality unaccepted.
The 14B artifact import is verified; selected CPU 8B, bounded concurrency and credential isolation
are unchanged. Historical failed promotion and answer findings remain recorded in the test guide.

ردیابی وضوح زنده (بخش‌های ۹، ۱۹ و ۲۵؛ ۷ مهر ۱۴۰۵): برنامه و API استنتاج اکنون `c4351fd` هستند.
دوازده پرسش تازهٔ API و هفت مورد مرورگر در دو محیط، بازآزمایی‌های مشخصِ سلام، دانش عمومی، وضعیت
زندهٔ نامعلوم و تمرکز و دامنه را پوشش می‌دهند. تطبیق هش کد، بازگشت ترتیبی برنامه/API و استقرار
مجدد بررسی شد. کیفیت کامل ناقص، قطع WAN و شروع سردِ همین انتشار اجرا‌نشده و کیفیت مدل بزرگ‌تر
پذیرفته نیست. ورود فایل 14B تأیید شده است؛ CPU 8B منتخب، هم‌زمانی محدود و جداسازی اطلاعات ورود
تغییر نکرده‌اند. استقرار ناموفق و یافته‌های پاسخ در تاریخچهٔ راهنمای آزمون حفظ شده‌اند.

Clarity/workflow trace (sections 9, 19, 25; 2026-09-29): the owner retired the unrelated
questionnaire prerequisite. The candidate separates application-owned general/evidence purpose,
retains the full accepted question and permits bounded 384-token answers; browser clients cannot
set provider controls. The official 14B candidate has immutable source/size/hash metadata and a
local-only alias. Eight synthetic 8B loopback generations completed, with Persian/source-label
issues retained for comparison. These observations do not close the failed serving semantic gate
or any exact-release offline, rollback, recovery or production gate.

ردیابی وضوح و روند توسعه (بخش‌های ۹، ۱۹ و ۲۵؛ ۷ مهر ۱۴۰۵): مالک پیش‌شرطِ پرسش‌نامهٔ نامرتبط را
حذف کرد. نامزد، نوع پردازش عمومی و شاهد را در اختیار برنامه جدا می‌کند، پرسش کامل را حفظ می‌کند
و پاسخ محدودِ ۳۸۴توکنی می‌دهد؛ کاربرِ مرورگر نمی‌تواند تنظیم‌های مدل را تعیین کند. نامزد رسمی
14B رکورد منبع، اندازه و هش تغییرناپذیر و شناسهٔ صرفاً محلی دارد. هشت تولید ساختگی روی 8B کامل
شدند و اشکال عبارت فارسی و برچسب منبع برای مقایسه حفظ شد. این مشاهده‌ها شکست معیار معناییِ
برنامهٔ مستقر یا معیارهای آفلاین، بازگشت، بازیابی و تولید را نمی‌بندند.

Repository-policy trace (active prompt section 8, 2026-09-28): read-only GitHub branch and
ruleset results confirm absent merge enforcement despite five successful trusted CI checks.
The paired development/runbook handoff covers administrator setup and denied-merge verification;
no setting changed and `release_supply_chain_review` remains partial.

ردیابی سیاست مخزن (بخش ۸ پرامپت فعال، ۶ مهر ۱۴۰۵): دادهٔ فقط‌خواندنی شاخه و rulesetهای GitHub،
نبود الزام ادغام را با وجود پنج کنترل موفق و معتبرِ CI تأیید کرد. راهنمای دوزبانهٔ توسعه و موانع،
تنظیم توسط مدیر و آزمون رد ادغام را مشخص می‌کند؛ تنظیمی تغییر نکرد و `release_supply_chain_review`
همچنان ناقص است.

Source: [master prompt, original Appendix A](NEXTOPS_MASTER_PROMPT.md). All 51 original sections are retained. Paths below are planned or now-started implementation locations. `P` = planned; `D` = documentation drafted; `A` = owner-accepted documentation gate, not runtime implementation; `I` = a tested implementation slice exists but the full requirement is incomplete. Phase numbers follow the revised roadmap, not the original fourteen-phase order.

Current delivery exception (2026-09-26): the owner deferred independent recovery from the local
delivery work queue and reports daily ESXi snapshots. The backup, restore and disaster-recovery
requirements below remain traceable and unaccepted; the snapshot schedule and restore record have
not been independently reviewed. The active next task and release manifest identify non-recovery qualification separately.

Owner clarification: the owner tested ESXi VM snapshot restoration only. The test report was not
reviewed here and does not close the independent PostgreSQL/WAL/PITR or isolated-restore rows.

Answer-quality trace (section 25, 2026-09-27): the private live-capture source now requires at
least one configured automatic expectation per case for a successful command exit and flags a
longer question echoed as its answer. This source test does not repair the failed serving-release
semantic gate, verify backend identity or replace held-out human review.

Greeting-relevance trace (section 25, 2026-09-27): source-only API fixtures now reject unrelated
operational or non-greeting replies to greeting-only English/Persian questions. The application
shows a labelled local fallback without live-status claims; a local browser fixture confirms the
notice. Deployment and live semantic review
remain open.

Merged-package trace (sections 21, 25 and 44, 2026-09-28): `b868e3e` passed source CI and its
unsigned wheel installed with hash-locked dependencies in fresh Ubuntu without a package index.
Whole-wheel hashes agreed between Windows and Ubuntu; source/wheel/installed code digests matched.
Ten synthetic installed-answer checks passed, not live model or serving-release acceptance.

Release-correlation trace (sections 25 and 44, 2026-09-27): source-only code computes a bounded
package-source/local-asset digest at application start and returns it only with successful
authenticated answer responses. The private capture compares it to an offline candidate-wheel
digest and fails on mismatch. This identifies code bytes, not a signed full release, and remains
unobserved on the serving host; the failed semantic and unrun exact-release gates do not change.

Packaging trace (sections 21, 25 and 44, 2026-09-27): merged commit `d973785` produced a private,
unsigned wheel whose whole-file SHA-256 agreed between Windows and Ubuntu. A fresh Ubuntu 24.04.5
desktop venv installed the unchanged hash-locked Linux dependencies and candidate wheel with the
package index disabled; package checks/imports and wheel-to-installed code-digest equality passed.
This is not serving-host deployment, live AI/evidence acceptance or release signing.

منبع: پیوست اولیهٔ پرامپت. هر ۵۱ بخش حفظ شده است. مسیرها محل برنامه‌ریزی‌شده یا شروع‌شده‌اند. `P` یعنی برنامه‌ریزی‌شده، `D` یعنی مستندات آماده، `A` یعنی دروازهٔ مستندات با پذیرش مالک و بدون ادعای runtime، و `I` یعنی یک برش پیاده‌سازی آزموده وجود دارد ولی نیاز کامل نشده است. شمارهٔ مرحله بر اساس نقشهٔ راه جدید است.

ردیابی کیفیت پاسخ (بخش ۲۵، ۵ مهر ۱۴۰۵): فرمانِ گردآوری زنده برای خروج موفق باید برای هر پرسش
دست‌کم یک انتظارِ خودکار داشته باشد و تکرارِ پرسش بلند به‌عنوان پاسخ را نیز خطا می‌داند. این
آزمونِ کد، شکست معیار معناییِ انتشار مستقر را برطرف نمی‌کند، شناسهٔ کدِ پشت سرویس را تأیید
نمی‌کند و جای بازبینی انسانیِ پرسش‌های کنارگذاشته‌شده را نمی‌گیرد.

ردیابیِ پاسخ به سلام (بخش ۲۵، ۵ مهر ۱۴۰۵): آزمون‌های API با دادهٔ آزمایشی اکنون پاسخِ عملیاتیِ
ناخواسته یا پاسخِ غیرسلام به پرسشِ محدود به سلام را در فارسی و انگلیسی رد می‌کنند. برنامه
جایگزینی محلی و دارای برچسب نشان می‌دهد و آزمون مرورگرِ محلی نیز اعلان آن را بررسی می‌کند،
بی‌آنکه وضعیت زنده ادعا شود؛ استقرار و بازبینی معناییِ
زنده هنوز باقی است.

ردیابی بستهٔ ادغام‌شده (بخش‌های ۲۱، ۲۵ و ۴۴، ۶ مهر ۱۴۰۵): کدِ `b868e3e`، آزمون CI را گذراند
و wheel بدون امضای آن همراه وابستگی‌های دارای هش، در Ubuntu تازه بدون فهرست بسته‌ها نصب شد.
هش کل wheel در Windows و Ubuntu یکسان و هش کدِ منبع، wheel و نصب نیز منطبق بود. ده آزمون
ساختگیِ پاسخ در بستهٔ نصب‌شده موفق بود؛ این نتیجه پذیرش مدل زنده یا انتشارِ در حال خدمت نیست.

ردیابیِ هم‌بستگی انتشار (بخش‌های ۲۵ و ۴۴، ۵ مهر ۱۴۰۵): کدِ هنوز مستقرنشده هنگام آغاز برنامه
هش محدودِ کد بسته و فایل‌های محلیِ رابط را محاسبه و فقط همراه پاسخ موفقِ احرازهویت‌شده برمی‌گرداند.
ابزار خصوصی، آن را با هش wheel آفلاینِ نامزد تطبیق می‌دهد و ناسازگاری را خطا می‌داند. این
شناسهٔ بایت‌های کد است، نه امضای کل انتشار؛ هنوز روی سرور دیده نشده و شکستِ معیار معنایی و
آزمون‌نشدن معیارهای وابسته به نسخه را تغییر نمی‌دهد.

ردیابی بسته‌بندی (بخش‌های ۲۱، ۲۵ و ۴۴، ۵ مهر ۱۴۰۵): از commit ادغام‌شدهٔ `d973785` یک wheel
خصوصی و بدون امضا ساخته شد که هش کل آن در Windows و Ubuntu یکسان بود. در محیط تازهٔ Ubuntu
24.04.5 میزکار، وابستگی‌های لینوکسیِ قفل‌شده و wheel نامزد بدون دسترسی به فهرست بسته‌ها نصب
شدند؛ بررسی بسته‌ها، واردکردن ماژول‌ها و برابری هش کدِ wheel و نصب موفق بود. این کار استقرار روی
سرور، پذیرش پاسخ و شاهدِ زنده یا امضای انتشار نیست.

استثنای تحویل جاری (۴ مهر ۱۴۰۵): مالک بازیابی مستقل را از صف کار تحویل محلی به تعویق انداخته و از
snapshot روزانهٔ ESXi خبر داده است. نیازهای پشتیبان و بازیابی و بحران در جدول همچنان قابل ردیابی و
پذیرفته‌نشده‌اند؛ برنامهٔ snapshot و گزارش بازیابی آن مستقلاً بررسی نشده‌اند. کار فعال بعدی و مانیفست انتشار،
صلاحیت‌سنجی غیربازیابی را جدا نشان می‌دهند.

مالک روشن کرد که فقط بازیابی از snapshot ماشین ESXi را آزموده است. گزارش این آزمون در این بازبینی
بررسی نشده و معیارهای پشتیبان مستقل PostgreSQL، ‏WAL/PITR و restore ایزوله را کامل نمی‌کند.

| Original | Requirement / نیاز | Planned owner/location | Phase | Acceptance evidence / شاهد پذیرش | Status |
|---|---|---|---|---|---|
| 1 | Inspect before changes / بررسی پیش از تغییر | `docs/en/PHASE_0_REPORT.md`, `docs/fa/PHASE_0_REPORT.md` | 0 | Owner-accepted repository report; private live preflight remains / گزارش پذیرفته‌شده؛ بررسی خصوصی باقی است | A |
| 2 | Product objective / هدف محصول | `apps/api`, `application` | 2–8 | Evidence-linked end-to-end flow / جریان کامل مستند | P |
| 3 | Persian/English / فارسی و انگلیسی | `localization`, `apps/web` | 1–8 | Native wording and RTL/LTR tests / آزمون زبان و جهت | P |
| 4 | Core architecture / معماری اصلی | `packages/nextops/domain`, `contracts`, `policy`; future `application`, `infrastructure` | 0–1 | Accepted boundaries plus tested contract/policy slice / مرز پذیرفته و برش آزموده | I |
| 5 | Independent integrations / اتصال مستقل | `connectors` | 2–5 | Eleven versioned capability records / پروندهٔ یازده اتصال | P |
| 6 | Central MCP gateway / درگاه مرکزی | `apps/mcp_gateway` | 1–2 | Auth, routing, limits, failure isolation / هویت و محدودیت و جداسازی | P |
| 7 | RBAC / نقش و دسترسی | `packages/nextops/policy`, `packages/nextops/application` | 1 | Deny-by-default policy plus server-derived durable actor/session and cross-scope tests; full administration remains / سیاست رد و هویت ماندگار سمت سرور؛ مدیریت کامل باقی است | I |
| 8 | Approval / تأیید عملیات | `application`, `policy` | 1,7 | Exact digest, replay and expiry tests / هش دقیق و انقضا و بازپخش | P |
| 9 | Secrets / اطلاعات محرمانه | `infrastructure` | 1 | Boundary-local credentials, no leaks / مرز اطلاعات ورود و عدم نشت | P |
| 10 | Audit / ممیزی | `packages/nextops/persistence`, `application`; future `observability` | 1 | Transactional append-restricted events and rollback tests exist; browsing/export/checkpoints remain / رخداد ماندگار و rollback آزموده؛ مرور و checkpoint باقی است | I |
| 11 | Linux MCP / اتصال لینوکس | `connectors/linux` | 2 | Bounded diagnostics, simulator/lab evidence / عیب‌یابی محدود و شاهد | P |
| 12 | Windows MCP / اتصال ویندوز | `connectors/windows` | 3 | Constrained authenticated operations / عملیات محدود و دارای هویت | P |
| 13 | Cisco MCP / اتصال سیسکو | `connectors/cisco` | 3 | Version-specific read diagnostics / خواندن وابسته به نسخه | P |
| 14 | Juniper MCP / اتصال جونیپر | `connectors/juniper` | 3 | Junos contract/diff/commit-state tests / قرارداد و وضعیت تنظیمات | P |
| 15 | FortiGate MCP / اتصال فورتی‌گیت | `connectors/fortigate` | 4 | Scoped VPN/routing/policy evidence / شواهد محدود شبکه و سیاست | P |
| 16 | Sophos MCP / اتصال سوفوس | `connectors/sophos` | 4 | Verified API coverage and explicit limits / پوشش و محدودیت روشن API | P |
| 17 | Zabbix MCP / اتصال زبیکس | `connectors/zabbix` | 1–2 | Phase 1 status reads and bounded Phase 2 history/events are live on the controlled server path; durable model/browser acceptance remains / خواندن وضعیت مرحلهٔ یک و تاریخچه و رویداد محدود مرحلهٔ دو در مسیر کنترل‌شدهٔ سرور زنده‌اند؛ پذیرش ماندگار مدل و مرورگر باقی است | I |
| 18 | Grafana MCP / اتصال گرافانا | `connectors/grafana` | 3 | Authorized datasource queries / پرس‌وجوی منبع مجاز | P |
| 19 | SQL Server MCP / اتصال SQL Server | `connectors/sqlserver` | 5 | Read-only identity, DMV/limits tests / هویت فقط‌خواندنی و محدودیت | P |
| 20 | MySQL MCP / اتصال MySQL | `connectors/mysql` | 5 | Engine/version and bounded SQL tests / موتور و نسخه و SQL محدود | P |
| 21 | ESXi MCP / اتصال ESXi | `connectors/esxi` | 5 | Version/license-aware diagnostics / تشخیص سازگار با نسخه و مجوز | P |
| 22 | Topology / توپولوژی | `knowledge` | 3,6 | Provenance/freshness on relationships / منبع و تازگی رابطه | P |
| 23 | Incident correlation / هم‌بستگی رخداد | `knowledge`, `application` | 2,6 | Time-windowed cross-source evidence / شواهد چندمنبعی زمان‌مند | P |
| 24 | RCA / تحلیل علت ریشه‌ای | `knowledge`, `application` | 2,6 | Hypotheses versus verified causes / تفکیک فرضیه و علت تأییدشده | P |
| 25 | LLM abstraction / رابط مدل | `packages/nextops/inference`, `packages/nextops/api/answer_integrity.py`, `scripts/evaluate_live_app_semantics.py` | 1–2 | Pinned local CPU model and bounded scheduler remain deployed; the six-case live semantic probe failed on file focus and multi-host scope. Optional literal checks reproduce four failures from the saved report without new server access; source repair is not deployed and held-out human review remains / مدل محلی و صف محدود مستقرند؛ سنجش زندهٔ شش‌موردی در تمرکز فایل و دامنهٔ چند میزبان شکست خورد. کنترل واژگانیِ اختیاری چهار شکست گزارش پیشین را بی‌دسترسی تازه به سرور بازتولید می‌کند؛ اصلاح مستقر نشده و بازبینی انسانیِ مستقل باقی است | I |
| 26 | Offline mode / حالت آفلاین | `deploy/server-dependencies`, `deploy/inference`, `scripts` | 1,2,8 | Earlier Internet-blocked cold start passed. Hash-locked Linux wheels and the candidate installed in a fresh Ubuntu 24.04.5 desktop lab with the index disabled; current-app server-side WAN/reboot and permanent host egress remain unqualified / شروع سردِ بدون اینترنت در کارزار پیشین موفق بود. wheelهای لینوکسیِ دارای هش و نامزد برنامه در آزمایشگاه تازهٔ Ubuntu 24.04.5 میزکار، بدون فهرست بسته‌ها نصب شدند؛ آزمون WAN و راه‌اندازیِ انتشار جاری در سرور و سیاست دائمی خروج میزبان هنوز پذیرفته نیستند | I |
| 27 | Memory / حافظه | `knowledge` | 6 | Scoped, fresh conversation/incident memory / حافظهٔ محدود و تازه | P |
| 28 | Database abstraction / رابط پایگاه داده | `packages/nextops/persistence`, `migrations` | 1 | Baseline, roles and durability tested on real PostgreSQL; production lock/backup and alternatives remain / migration و role آزموده؛ تولید و جایگزین باقی است | I |
| 29 | API / رابط برنامه | `packages/nextops/api`, `packages/nextops/inference`, `contracts` | 1–2 | Authenticated app and inference routes, correlation, safe readiness and structured errors tested; later domains remain / مسیر برنامه و inference و خطای ساخت‌یافته آزموده؛ دامنه‌های بعدی باقی است | I |
| 30 | UI / رابط کاربری | `packages/nextops/api/static`; future operations console | 2–8 | Controlled release `01755d1` serves the bilingual question/answer flow, but live file-only routing failed. A source-only browser change shows focused evidence first and complete authorized evidence on explicit reveal; deployment remains / انتشار کنترل‌شدهٔ `01755d1` مسیر دوزبانه را دارد، ولی تشخیص زندهٔ «فقط فایل» شکست خورد. اصلاح رابط در کد ابتدا شاهد مرتبط و با بازکردن صریح، همهٔ شواهد مجاز را نشان می‌دهد؛ استقرار باقی است | I |
| 31 | Configuration / پیکربندی | `packages/nextops/configuration.py`, `packages/nextops/inference/configuration.py`, `deploy/**/*.yaml` | 1 | Typed fail-closed app/inference settings plus schema-validated deployer records; production secrets remain private / تنظیم سخت‌گیر و پروندهٔ معتبر؛ secret تولید خصوصی است | I |
| 32 | Inventory / موجودی تجهیزات | `packages/nextops/contracts`, `persistence`; future connectors | 1–2 | Immutable scoped target plus persisted fixture and denial tests; real inventory synchronization remains / هدف محدود و fixture ماندگار؛ همگام‌سازی واقعی باقی است | I |
| 33 | Health checks / بررسی سلامت | `packages/nextops/api`, `packages/nextops/inference` | 1–5 | App liveness, AI and connector tunnel readiness passed on controlled release `01755d1`; broader production recovery/observability remains / سلامت برنامه و آمادگی تونل‌های AI و اتصال‌دهنده روی انتشار کنترل‌شدهٔ `01755d1` موفق بود؛ بازیابی و پایش تولیدی باقی است | I |
| 34 | Error handling / مدیریت خطا | `packages/nextops/contracts`, `application`, `api` | 1–5 | Typed application/API errors, correlation and dependency failure tested; broader retry/isolation remains / خطا و correlation آزموده؛ retry گسترده باقی است | I |
| 35 | Observability / مشاهده‌پذیری | `observability` | 1,8 | Metrics/logs and audit distinction / تفکیک متریک و لاگ و ممیزی | P |
| 36 | Testing / آزمون | `tests`, `scripts`, future `evals` | 1–8 | CI unit/API/browser, PostgreSQL 16/17 and secret checks; nine offline SBOM-evidence boundary tests; exact-release live, signing, legal and recovery gates remain / آزمون‌های واحد، API، مرورگر، PostgreSQL 16 و 17 و اسکن محرمانه در CI؛ نُه آزمون مرزیِ شاهد SBOM؛ معیارهای زندهٔ همان انتشار، امضا، حقوقی و بازیابی باقی‌اند | I |
| 37 | Docker / کانتینر | `deploy/compose` | 1,8 | Restricted clean install and offline test / نصب محدود و آفلاین | P |
| 38 | Installation docs / مستندات نصب | `docs/en/INSTALL.md`, `docs/fa/INSTALL.md`, paired `DEPLOYMENT_DOSSIERS.md`, `deploy/server-dependencies`, `deploy/installers` | 0–8 | Four validated handoffs and guarded offline OS-package workflows exist; approved role bundles, complete application installers and clean-server evidence remain / چهار پرونده و نصب بستهٔ محافظت‌شده موجود؛ bundle و نصب کامل و شاهد سرور تمیز باقی است | I |
| 39 | Native Persian docs / مستندات فارسی طبیعی | `docs/fa`, `docs/en` | 0–8 | Paired guides and language review / همتای دو زبان و بازبینی | D |
| 40 | Lifecycle scripts / اسکریپت چرخهٔ عمر | `scripts`, `deploy/server-dependencies/*.yaml`, `deploy/installers` | 1,8 | Exact offline OS-package installation is guarded, idempotent and tested; application setup/start/stop/test/backup/restore remain / نصب دقیق package آفلاین محافظت‌شده و آزموده است؛ چرخهٔ کامل برنامه باقی است | I |
| 41 | Systemd / سرویس بومی | `deploy/systemd` | 1,8 | Units, hardening, resource and recovery tests / آزمون واحد سرویس و بازیابی | P |
| 42 | Security docs / مستندات امنیت | `docs/en/SECURITY.md`, `docs/fa/SECURITY.md` | 0–8 | Documented RBAC/secrets/TLS/audit/backup / راهنمای کنترل‌های امنیت | D |
| 43 | README / معرفی پروژه | `README.md`, `README_FA.md` | 0–8 | Honest status and bilingual navigation / وضعیت واقعی و مسیر دو زبان | D |
| 44 | Development rules / قواعد توسعه | `AGENTS.md`, `.agents/skills`, `docs/MARKDOWN_CONTEXT_INDEX.md`, `CONTRIBUTING.md` | 0–8 | Six repo skills, complete Markdown routing/catalog tests, types, reviews and no credential commits / شش skill مخزن، catalog آزموده، نوع و بازبینی | I |
| 45 | Real MCP interface / پروتکل واقعی MCP | `contracts`, `connectors/base` | 1–2 | SDK/protocol conformance tests / آزمون انطباق | P |
| 46 | Tool risk / ریسک ابزار | `packages/nextops/domain`, `packages/nextops/policy` | 1 | Trusted risk registry; request/model actor and risk fields rejected; all mutation classes denied / ریسک معتبر و رد تغییر | I |
| 47 | Decision workflow / گردش تصمیم | `application` | 1–2 | Bounded persisted state machine / ماشین حالت محدود و ماندگار | P |
| 48 | Self-verification / بررسی نتیجه | `application`, `connectors` | 2,7 | Fresh postconditions; unknown-outcome reconciliation / نتیجهٔ تازه و رفع ابهام | P |
| 49 | Phased delivery / تحویل مرحله‌ای | `docs/en/ROADMAP.md`, `docs/fa/ROADMAP.md` | 0–8 | Revised gates, all original scope retained / معیار جدید و حفظ دامنه | D |
| 50 | Phase completion / پایان مرحله | `docs/PROJECT_STATE.md`, `tests` | 0–8 | Phase 0, two Stage 1A increments and the Stage 1B repository foundation have evidence; server qualification and later phases remain / مرحلهٔ صفر، دو برش 1A و پایهٔ 1B شاهد دارند؛ سرور و مراحل بعدی باقی است | I |
| 51 | First architecture report / گزارش معماری نخست | `docs/en/PHASE_0_REPORT.md`, `docs/fa/PHASE_0_REPORT.md` | 0 | Owner accepted on 2026-09-21; infrastructure authorization remains separate / پذیرش مالک؛ مجوز زیرساخت جداست | A |

## Explicit revisions / اصلاحات صریح

Early security and CPU/offline validation; complete integration slices; local providers only; PostgreSQL-first; no admin or read-only shortcut; qualified rather than invented RCA probabilities; concise decision summaries rather than unrestricted reasoning traces; and no false single-host HA. These revisions come from the supplied enhanced prompt. See [ADRs](../adr/README.md).

امنیت و آفلاین از ابتدا، جریان کامل اتصال، مدل صرفاً محلی، PostgreSQL اولیه، نبود میان‌بُر مدیر یا خواندن، اطمینان مستند به‌جای احتمال ساختگی، خلاصهٔ تصمیم به‌جای نمایش نامحدود استدلال و عدم ادعای HA تک‌میزبان، اصلاحات صریح پرامپت بهبودیافته‌اند.
