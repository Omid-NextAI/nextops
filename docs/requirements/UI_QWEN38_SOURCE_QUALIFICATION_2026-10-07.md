# Enabled-model UI and secondary-source inspection / رابط مدل فعال و بررسی منبع دوم

## Problem, scope and requirements / مسئله، دامنه و نیازها

The serving Qwen3.8 model was labelled generically; mode/source controls were buried and evidence
rows limited to three. Make actual capabilities and approved secondary-source reads discoverable,
without changing the model, policy, credentials, inference budgets or existing MCP deployment.
Keep local CPU inference, authenticated owner-scoped chats, EN/FA, source/time/scope qualifiers,
safe text rendering, durable audit and bounded evidence. A catalogue is not a health check.

مدل Qwen3.8 فعال، برچسب عمومی داشت؛ حالت پاسخ و انتخاب منبع پنهان بود و فقط سه ردیف شاهد
دیده می‌شد. قابلیت واقعی و خواندن مجاز منبع دوم باید آشکار شود، بدون تغییر مدل، سیاست،
اطلاعات ورود، بودجهٔ پردازش یا استقرار MCP. پردازش محلی CPU، گفت‌وگوی احرازهویت‌شده و مختص
مالک، دو زبان، منبع/زمان/دامنه، نمایش امن متن، ممیزی ماندگار و شاهد محدود حفظ شوند.
فهرست مجاز به‌معنی آزمون سلامت نیست.

## Implementation and non-goals / پیاده‌سازی و موارد خارج از دامنه

Source `e3ecf2170182da77df3c230b8bbeee15ca8e73af` first added modular `capabilities.js`, an authenticated
model dialog, visible source/host controls, explicit problem/metric/status question shortcuts,
approved-host navigation and filters over returned evidence. Shortcuts prepare drafts; they do
not execute automatically. No model text is guessed into structured findings. Empty or partial
evidence is never labelled healthy. Selected-source requests cannot inherit primary-source health.

`configured_context_tokens` is nullable readiness metadata, not a claim of full-window quality.
New app accepts old providers that omit it. Old app schema is strict: promote app before API;
roll back API before app. Thinking remains denied, saved context remains six turns/12,000 characters
and 30-day retention; 16,384 tokens remains configured admission, not maximum-context acceptance.
No new package manager, remote assets, GPU, cloud fallback, database migration, native restart,
model download, target enrolment, Zabbix SSH, credentials/TLS change or remediation is included.

کد بالا، ماژول `capabilities.js`، پنجرهٔ احرازهویت‌شدهٔ مدل، کنترل آشکار منبع/میزبان،
میان‌بر صریحِ پرسش دربارهٔ مشکلات/سنجه‌ها/وضعیت، پیمایش میزبان مجاز و فیلتر شاهد دریافتی
را اضافه می‌کند. میان‌بر فقط پیش‌نویس می‌سازد و اجرا نمی‌کند؛ یافتهٔ ساختاریافته از متن
مدل حدس زده نمی‌شود. شاهد ناقص یا خالی، وضعیت سالم نیست؛ منبع انتخاب‌شده وضعیت منبع اصلی
را به ارث نمی‌برد.

فیلد آمادگی بالا، اختیاری است و پذیرش کیفیت کل زمینه نیست. برنامهٔ جدید، provider قدیمی
بدون این فیلد را می‌پذیرد؛ انتخاب ابتدا برنامه سپس API و بازگشت ابتدا API سپس برنامه است.
استدلال ممنوع می‌ماند؛ زمینهٔ ذخیره‌شده شش نوبت/۱۲٬۰۰۰ نویسه و نگه‌داری ۳۰ روز است.
۱۶٬۳۸۴ توکن، سقف تنظیم‌شدهٔ پذیرش است. ابزار بستهٔ جدید، فایل بیرونی، GPU، جایگزین ابری،
تغییر پایگاه، شروع مجدد runtime، دانلود مدل، ثبت مقصد، SSH زبیکس، تغییر اطلاعات ورود/TLS
یا اجرای اصلاح در این کار نیست.

## Threats, rollout and rollback / تهدید، انتخاب و بازگشت

Untrusted host/problem text stays text, not HTML or instructions. Secrets stay at existing runner
boundaries. Capability content and model identity clear on logout. No fixture fallback or
production demo toggle exists; sanitized screenshots are explicitly demo, not live.
Ship one exact offline wheel under each existing hashed dependency lock. Protect staging parents,
verify old/new package digests and unchanged units/environment/native PID; arm owned rollback
timers before atomic source selection. Test fresh authenticated reads, saved-chat resume, denials,
evidence/audit equality, exact API/app source rollback and reapply before retention. No schema or
credential rollback is required because neither changes. Retain old immutable releases.

متن نامطمئن میزبان/مشکل، متن باقی می‌ماند، نه HTML یا دستور. اسرار نزد runner می‌مانند؛
اطلاعات قابلیت و هویت مدل با خروج پاک می‌شود. پاسخ ساختگیِ جایگزین یا کلید آزمایشی در
انتشار عملیاتی وجود ندارد؛ تصاویر آزمون صریحاً آزمایشی‌اند. wheel آفلاین دقیق با قفل هش‌دار
قبلی هر نقش نصب شود؛ والد staging محافظت، هش نسخه‌ها و ثبات واحد/محیط/PID بومی کنترل و
بازگشت زمان‌دار پیش از انتخاب اتمی فعال شود. خواندن تازه، بازگشایی گفت‌وگو، منع دسترسی،
تطبیق شاهد/ممیزی و بازگشت/اعمال دقیق کد پیش از تثبیت لازم‌اند. پایگاه و اطلاعات ورود ثابت‌اند؛
نسخه‌های تغییرناپذیر قبلی حفظ شوند.

## Source acceptance / پذیرش کد

- `python -m pytest -m 'not integration and not browser' -q --tb=short`: 1,446 passed,
  two Windows/POSIX-specific skips, 132 deselected in40.63 seconds on `ec1ed32`;
  one existing AnyIO deprecation warning.
- `python -m pytest tests/browser -q --tb=short`: 94 passed in377.02 seconds on `ec1ed32`.
  Updated screenshot/keyboard/logout cases rechecked separately: two passed, 30 deselected
  in11.60 seconds. Earlier source also passed94 in325.16 seconds.
- `python -m mypy --platform linux packages tests scripts deploy/installers`: 151 files passed.
- Ruff check/format, JS syntax, docs/catalogue and diff checks passed. Local Gitleaks reported no
  leaks in scanned text; historical DOCX text-conversion warnings limit that local scan.
- Exact-source CI runs `37598666531` (`e3ecf21`) and `37601040171` (`ec1ed32`):
  quality/dependency audit, PostgreSQL 16 and17 integration,
  browser acceptance and secret scan all passed. Source CI is not live infrastructure acceptance.
- Fixture captures: `artifacts/q38-ui-sync/{secondary,controls,capabilities}-<locale>-<size>.png`;
  EN/FA desktop/mobile were inspected. Captures are ignored by Git; no production fixtures included.
- Final manifest/document handoff rerun:1,446 unit/API passed, two POSIX skips,132 deselected,
  one existing warning in27.37s; types151, lint/format157, docs142/39 pairs, status/artifact and
  JS syntax/diff checks passed. Manifest regressions now use the explicit historical API suffix
  and the two recorded Q8 code identities, without relaxing the schema or quality exception.
- Documentation head `5f9aac8` CI secret scan failed on one `generic-api-key` finding: the public
  `ec1ed32…` Git source commit compared in a variable named `api_source`, not a credential. The
  exact commit/path/rule/line fingerprint was reviewed against Git and the status manifest. Rename
  it `serving_commit`; retain one exact historical fingerprint exception because full-history
  scanning cannot be repaired by deleting a current line. No rule/path/value-wide exemption or
  history rewrite. A failed scan is not relabelled passed; subsequent scan results are separate.
  That head's other four CI jobs passed. The reviewed correction passed34 focused regressions
  in3.89s, lint/format/docs/diff and the local pinned8.30.1 full-history text scan (264 commits,
  ~7.77MB, no findings); historical DOCX conversion warnings remain a local coverage limitation.

آزمون کد، ۱٬۴۴۶ مورد موفق، دو مورد مختص POSIX اجرا‌نشده در Windows و ۱۳۲ مورد خارج از
انتخاب در۴۰٫۶۳ ثانیه دارد؛ هشدار قدیمی AnyIO باقی است. ۹۴ آزمون مرورگر کد اصلاح‌شده در
۳۷۷٫۰۲ ثانیه موفق‌اند و دو مورد تازهٔ تصویر/صفحه‌کلید/پاک‌سازی نیز جدا در۱۱٫۶۰ ثانیه اجرا
شدند. نتیجهٔ۹۴ موردِ کد پیشین در۳۲۵٫۱۶ ثانیه حفظ است. کنترل نوعِ Linux روی ۱۵۱ فایل، Ruff، نحو JS، اسناد و
diff موفق‌اند. Gitleaks در متنِ اسکن‌شده موردی نیافت؛ هشدار تبدیل DOCX تاریخی، اسکن محلی را
محدود می‌کند. هر پنج کار CI هر دو کد دقیق، شامل دو نسخهٔ PostgreSQL، موفق‌اند؛ CI پذیرش زنده نیست.
تصاویر دو زبان و موبایل بررسی شده‌اند، آزمایشی و خارج از Git هستند.
بازاجرای نهاییِ تحویل سند/وضعیت،۱٬۴۴۶ موفق، دو اجرا‌نشدهٔ POSIX،۱۳۲ انتخاب‌نشده و یک هشدار
موجود در۲۷٫۳۷ ثانیه داشت؛ کنترل نوع۱۵۱ فایل، lint/قالب۱۵۷، اسناد۱۴۲/۳۹ جفت، وضعیت/فایل،
نحو JS و diff موفق‌اند. آزمون منفیِ وضعیت اکنون پسوند تاریخی API را صریح بررسی می‌کند و
کنترل Q8 دو شناسهٔ کد ثبت‌شده را می‌پذیرد؛ schema یا استثنای کیفیت آسان‌تر نشده است.
اسکن اسرار CI کد سندِ `5f9aac8` یک یافتهٔ `generic-api-key` داشت: شناسهٔ عمومی commit برابر
`ec1ed32…` در مقایسهٔ متغیر `api_source`، نه اطلاعات ورود. اثرانگشت دقیقِ commit/مسیر/قاعده/
خط با Git و وضعیت انتشار بررسی شد. نام به `serving_commit` تغییر می‌کند؛ فقط همان یافتهٔ
تاریخی مستثناست، زیرا حذف خط جاری، اسکن کل تاریخچه را اصلاح نمی‌کند. قاعده، مسیر یا مقدار
به‌طور عمومی مستثنا و تاریخ بازنویسی نمی‌شود؛ اسکن ناموفق، موفق نام نمی‌گیرد و نتیجهٔ بعدی جداست.
چهار کار دیگر CI آن کد موفق‌اند. اصلاح بازبینی‌شده،۳۴ آزمون محدود در۳٫۸۹ ثانیه، lint/قالب/
اسناد/diff و اسکن متنِ کل تاریخ با نسخهٔ قفل‌شدهٔ8.30.1 را گذراند:۲۶۴ commit، حدود۷٫۷۷MB
و بدون یافته. هشدار تبدیل DOCX تاریخی، محدودیت پوشش اسکن محلی باقی است.

## Live observations / مشاهدات زنده

First guarded revision: saved initial/reloaded follow-up passed in21.844/22.157 seconds; fresh
secondary problem inspection passed in166.969 seconds. Persian metrics timed out, with durable
error `inference.upstream_timeout`; the overall first runner failed. Exact API-then-app source
rollback passed. Its fresh Q8 general answer completed in125.282 seconds; the rollback browser
runner then failed an incorrect assertion that the pre-login generic model tooltip must be absent.
Separate unauthenticated inspection confirmed only "Local CPU model", hidden workspace and no
serving-model identity. Preserve both failed reports, not fabricated passes.

Revised source `ec1ed325b73d63840e788720364ca9694897422e` changes only the metrics **draft question**
to a compact summary of at most two returned metrics/60 words. All returned observations remain
inspectable; custom questions, trusted prompts and inference budgets are unchanged. The new
textarea assertion was corrected to check its value rather than DOM text. Revised rollout is
retained after actual rollback/reapply. The first revised live browser passed five finals:
saved initial53.453s, reload/follow-up27.953s, secondary problems EN178.687s, compact metrics
FA199.812s and the third approved target's status EN246.609s. Every generation finished with
`stop` and positive token usage. Denied source/target/thinking, filtered evidence selection,
mobile reflow, logout/replay rejection and no browser external requests/page errors passed.
Read-only PostgreSQL verification matched two conversation audits and three evidence hash pairs.
Manual review found the third target's answer overstates host reachability from ICMP destination
results; those observations do not independently prove the monitored host's reachability. This
is a retained semantic limitation, not a passing factual-quality gate. Partial returned data is
labelled partial, and the app adds authoritative source/time/scope qualifiers outside the model.
Native Q8/model/runtime, units, environment and MCP
remain unchanged. Preparation first stopped before installation because the proposed parent was
service-writable; the sealed bundle moved beneath a root-protected parent without weakening checks.

Exact AI-then-app rollback restored the original package identities, with a fresh Q8 general answer
in19.906s. App-then-AI reapply armed new owned guards. The final fresh browser passed secondary
problems FA183.750s and status EN105.703s; read-only PostgreSQL matched two more evidence/audit hash
pairs. Thus the revised three contexts produced eight fresh finals, two conversation audits and
five evidence hash pairs, not a load benchmark. Final Persian problem prose adds an unverified
`High` label to numeric severity3; the DTO/inspector retains3 and does not supply that label. Treat
the model-added label as unsupported, not authoritative monitoring data. No new waiver or passing
semantic result is claimed. This release retains the earlier owner's controlled standard-mode
model selection, not a model-quality approval.

At09:59:08 UTC both package roles were retained; source/code digests, units/environment and native
PID were reconciled unchanged where required. Both current and first-revision owned timers were
inactive. App/API/native services were active, automatic restart counters0, swap0, readiness
ready/active0/queued0. The MCP, credentials/TLS, target registry and schema were not changed.
No Zabbix-host SSH, service restart, target scan or new group enrollment was performed. Browser
requests were restricted to the local app origin; this is **not server-host WAN-isolation proof**.
Old immutable app/API releases remain available.

در نسخهٔ اول، ذخیره/بازگشایی و ادامهٔ گفت‌وگو به‌ترتیب۲۱٫۸۴۴/۲۲٫۱۵۷ ثانیه و بررسی مشکل منبع
دوم۱۶۶٫۹۶۹ ثانیه موفق بود. پرسش فارسیِ سنجه‌ها با خطای ماندگار بالا پایان مهلت داشت؛ ابزار
اول در مجموع ناموفق است. بازگشت دقیق API سپس برنامه موفق شد و پاسخ عمومی تازهٔ Q8 در
۱۲۵٫۲۸۲ ثانیه کامل شد. ابزار مرورگرِ بازگشت، سپس با انتظار نادرستِ نبودِ tooltip عمومی پیش
از ورود ناموفق شد؛ بررسی جدا، فقط برچسب عمومی CPU و محیط کاری پنهان را تأیید کرد، نه هویت
مدل فعال. هر دو گزارش ناموفق حفظ شوند و موفق نام نگیرند.

کد اصلاح‌شدهٔ بالا فقط **پیش‌نویس پرسش** سنجه‌ها را به حداکثر دو سنجه/۶۰ واژه محدود می‌کند؛
همهٔ مشاهدات دریافتی قابل بررسی‌اند و پرسش دلخواه، دستور معتبر و بودجهٔ پردازش ثابت‌اند.
آزمون textarea نیز مقدار ورودی را به‌جای متن DOM بررسی می‌کند. انتخاب اصلاح پس از بازگشت/
اعمال واقعی تثبیت شد. مرورگر زندهٔ اصلاح‌شده پنج پاسخ کامل داشت: ذخیره۵۳٫۴۵۳، بازگشایی/ادامه۲۷٫۹۵۳،
مشکلِ انگلیسی۱۷۸٫۶۸۷، سنجهٔ فارسی۱۹۹٫۸۱۲ و وضعیت انگلیسیِ مقصد سوم۲۴۶٫۶۰۹ ثانیه.
همه با `stop` و توکن مصرف‌شدهٔ مثبت پایان یافتند. منع منبع/مقصد/استدلال، انتخاب شاهد
فیلترشده، موبایل، خروج و رد نشست قبلی موفق و درخواست بیرونی/خطای صفحه صفر بود. بررسی
فقط‌خواندنی PostgreSQL، دو ممیزی گفت‌وگو و سه جفت هش شاهد را تطبیق داد. بازبینی دستی نشان
داد پاسخ مقصد سوم از نتیجهٔ ICMP مقصدها، دسترسی‌پذیری خودِ میزبان را بیش از حد نتیجه گرفته
است؛ آن مشاهدات مستقلاً دسترسی‌پذیری میزبان پایش‌شده را ثابت نمی‌کنند. این محدودیت معنایی
حفظ می‌شود و موفقیتِ واقع‌گویی نیست. دادهٔ ناقص با همین عنوان و مشخصات معتبرِ منبع/زمان/دامنه
به‌وسیلهٔ برنامه نمایش داده می‌شود. فایل/تنظیم/PID مدل، واحدها، محیط و MCP ثابت‌اند؛ کنترل مالکیت در انتقال
بستهٔ همین کار به والد محافظت‌شده تضعیف نشد.

بازگشت دقیقِ ابتدا AI و سپس برنامه، شناسهٔ بسته‌های قبلی را بازگرداند؛ پاسخ عمومیِ تازهٔ
Q8 در۱۹٫۹۰۶ ثانیه کامل شد. اعمال ابتدا برنامه و سپس AI، محافظ‌های اختصاصیِ تازه را فعال
کرد. مرورگر نهایی، مشکل فارسی در۱۸۳٫۷۵۰ و وضعیت انگلیسی در۱۰۵٫۷۰۳ ثانیه را گذراند؛ بررسی
فقط‌خواندنیِ پایگاه، دو جفت هش دیگر را تطبیق داد. سه مرورگر اصلاح، در مجموع هشت پاسخ تازه،
دو ممیزی گفت‌وگو و پنج جفت هش شاهد دارند؛ این معیار بار نیست. متن فارسیِ مشکل، برچسب
تأییدنشدهٔ `High` را به شدت عددی۳ اضافه می‌کند؛ DTO/پنل عدد۳ را حفظ می‌کنند و آن برچسب
را نداده‌اند. برچسب افزودهٔ مدل، شاهد معتبرِ پایش نیست. استثنای تازه یا موفقیت معنایی
اعلام نمی‌شود؛ انتخاب کنترل‌شدهٔ مدل بر اساس استثنای پیشین مالک باقی است، نه تأیید کیفیت مدل.

ساعت۰۹:۵۹:۰۸ UTC هر دو نقش تثبیت شدند؛ کد، واحد/محیط و PID بومی مطابق الزام کنترل شدند.
محافظ‌های نسخهٔ جاری و اول غیرفعال، خدمات برنامه/API/بومی فعال، شمارندهٔ شروع خودکار صفر،
swap صفر و آمادگیِ بدون درخواست/صف تأیید شد. MCP، اطلاعات ورود/TLS، فهرست مقصد و پایگاه
تغییر نکردند. SSH یا شروع دوبارهٔ میزبان زبیکس، پویش مقصد یا ثبت گروه تازه انجام نشد.
درخواست مرورگر به مبدأ محلیِ برنامه محدود بود؛ این **اثبات قطع WAN سرورها نیست**.
نسخه‌های تغییرناپذیر قبلیِ برنامه/API برای بازگشت حفظ‌اند.

## Exact identities and protected evidence / شناسهٔ دقیق و شواهد محفوظ

Serving source: `ec1ed325b73d63840e788720364ca9694897422e`, both package roles
`nextops-0.1.0-ec1ed32`. Package-code SHA256:
`4dda213187582cf1f2a7105623ce1bf22b9559dfc8996919ef8b6489c5ed2c16`.
Wheel SHA256: `a49201e961415386ac20e190c42c05ff7b5347d6fc33ef948b935d3cb970f08c`.
Exact source archive SHA256: `45f02492433bde609e6ca026e91cdbd7727794fd6fc965bdddf1c164e1adf259`.
App dependency-lock SHA256: `74802e32a9601b7c306669ffed2cda63edf19c72f8b4040dd0734acad3690abd`;
AI lock: `705271a647e028b172bc5cffa1b584f1f98d4188ea0d4027b5aff8571daf69a9`.
Installation used each existing verified offline wheelhouse under a network namespace without
network, then checked dependencies and protected release ownership. No new dependency or download.
The preceding [cutover record](QWEN38_CONTROLLED_CUTOVER_2026-10-07.md) retains unchanged model/
runtime hashes, profile and the distinct earlier35B **model** rollback.

Private browser report SHA256s, first/source-rollback/final respectively:

- `b1707ca7becac29147ffc99d136de009d20eb09dea35ab01c9f73435f4cf2c7d`
- `a60b2a77c4e032e785ecdaa723f261d25f109f5ffa7330c1cb7b0d23ffe359a3`
- `195266348d9300c1abbc83e9ce2504765d12cf9f5ca5c0a6dc525ac65011f5e8`

The root-protected lifecycle controller SHA256 is
`44d28923edf397c6a913f1baeac7043b950a018ba809a70fb181ffca71718e1e`;
its role configuration is `107ab266b7a9aad5b571adb38afd9bd3271a0e915fb558ea6a3ef8c7657d1b3f`.
Reviewed read-only audit verifier: `f6e786fbf90ea4d4cfec635894a74cfad9aa29c8a16a40bdd88c42a4a5b22a0b`.
Protected local directory: `C:/Users/Admin/.nextops/production-qualification/ui-q38-secondary-20261007/v2`.
Browser screenshots: `capabilities-{first,final}.png`, `workspace-<phase>-<logical-target>-<locale>.png`,
`mobile-{first,final}.png`. Real EN/FA desktop and mobile captures were inspected; raw inventory,
transcripts, credentials and private runbooks are not published to Git.

کد و شناسهٔ انتشار هر دو نقش، هش بسته/کد/آرشیو و قفل هر نقش در بالا دقیق ثبت‌اند. نصب از
wheelhouse تأییدشدهٔ موجود در فضای شبکهٔ جدا و بدون شبکه انجام و وابستگی و مالکیت محافظت‌شده
کنترل شد؛ وابستگی یا دانلود تازه‌ای اضافه نشد. رکورد گذار پیشین، هش/نمایهٔ ثابت مدل و runtime
و بازگشتِ جداگانهٔ **مدل** به35B را حفظ می‌کند. سه هش گزارش به‌ترتیب مرورگر اولیه، بازگشت کد
و نهایی‌اند. کنترل‌کننده، پیکربندی نقش و بررسی فقط‌خواندنیِ ممیزی بازبینی و محافظت شده‌اند.
تصویرهای واقعیِ دو زبان و موبایل بررسی شدند؛ موجودی خام، متن گفت‌وگو، اطلاعات ورود و ابزار
خصوصی در Git منتشر نمی‌شوند. مسیر محفوظ و الگوی نام تصویرها در بالا آمده است.

Raw13/16 remains failed under the earlier owner exception. This work does not qualify enabled
thinking, full-window context, host-side WAN isolation, VM cold start, load, recovery or production.

نتیجهٔ خام۱۳ از۱۶ با استثنای پیشین مالک همچنان ناموفق است. این کار، پذیرش استدلال فعال،
کل زمینه، قطع WAN سرورها، شروع سرد VM، بار، بازیابی یا تولید نیست.
