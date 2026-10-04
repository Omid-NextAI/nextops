# Controlled MCP live qualification / پذیرش محدود MCP زنده

## English

Observed 2026-10-04, 17:48–18:02 UTC. This record qualifies approved source selection on the
existing app/connector guests, not full production, all-group access, model semantics or recovery.
Private credentials, endpoints, tenant identifiers, inventory and browser evidence stay outside Git.

### Installed identity and controls

App and connector: `nextops-0.1.0-2a7c8dc`, source
`2a7c8dc5dc99ebf203748380b7ab8ea7f89ac690`.
Wheel SHA-256: `319ea3330714fcce78a5dd5a996d0a14b575de689997664d7b13cd7d31a31ddc`.
Installed application code SHA-256:
`c810efc04fe7f6b3c14bea4b6b27c2ebdc207c5d894983c254e80c36358a1375`.
Source archive SHA-256: `84581d19184a0a8438a659b87078013d216cb0c6505587a7c4595b79cca6659d`.
The selected-source answer route returns the installed-code header; the browser verifies it.

The existing connector VM now runs the official pinned SDK gateway and peer-UID-verified Unix
socket runner under separate service identities. Gateway credentials are only its TLS key and
application-service bearer; runner credentials are the two Zabbix tokens and existing four scoped
Linux keys. The app mounts neither Zabbix token nor Linux key. Gateway egress permits loopback
only; runner egress permits loopback and exact approved LAN destinations, with default denial.
Protected per-target binding digests are checked across app, gateway and runner before reads and
publication. The old HTTP connector is stopped/disabled, with immutable rollback artifacts retained.
No new VM, container, model, runtime, ESXi or resource allocation is included.

Offline package installation used pre-staged, hash-locked Linux wheels with `--offline --no-index`
and `--require-hashes`. An isolated network namespace additionally proved installation/imports
without networking; 41 distributions passed dependency consistency checks. This package-layer test
is separate from live WAN tests. Additive migration `0004_user_status` grants only the required
identity-status column and retains account/data history across application rollback.

### Actual results

| Gate | Result and boundary |
|---|---|
| Local/CI | 646 non-browser tests passed; two POSIX checks skipped on Windows. Thirty browser fixtures passed. Linux-target strict types passed. Exact runtime commit passed five CI jobs, including real PostgreSQL 16/17, browser and Gitleaks. |
| Approved discovery | Two logical sources, seven approved targets. Secondary source exposes three hosts in three populated approved groups. Five empty groups remain unobserved, not accepted. Catalogues are authorization-scoped metadata, not health/discovery scans. |
| Fresh secondary EN/FA | Six fresh selected Zabbix-host generations over three browser sessions returned `evidence_bounded`, real CPU prompt/completion counts, source/target/version/time and partial-evidence warnings. Final EN 39.813 s; FA 54.625 s. |
| Additional targets | Fresh Internet-SLA 39.890 s and FortiGate 39.563 s collected the correct source/target. Both answers used the integrity guard's transparent `deterministic_fallback`; unrestricted model interpretation is **not** accepted. |
| Existing paths | Primary summary retained its own version; AI-host investigation retrieved the correct primary Zabbix plus Linux evidence in 29.172 s (`deterministic_focus`). |
| Policy/UI | Unapproved source returned 403; malformed user input returned 422. Admin Users list was visible. EN/FA direction, selected-source persistence and 375-pixel overflow checks passed; final Persian screenshot reviewed. No company account was mutated. |
| Failure isolation | Controlled connector-side rejection of secondary API traffic returned typed 503 in 0.203 s, with no source fallback. Primary collection remained available; fresh general CPU generation returned 43 in 0.609 s. The owned rule was removed. |
| WAN/restart | Temporary app/connector output rules rejected non-management IPv4/IPv6 WAN traffic; fresh public connection probes failed. With management LAN and the exact secondary API allowed, services were stopped/started and a fresh verified-TLS browser login plus new EN/FA evidence/generations passed (40.172/51.188 s). No external browser request occurred. |
| Exact rollback/reapply | Prior app `7ce9d29` and connector `cdde129`, units, tunnel, SSH restrictions and Nginx were restored; fresh login and primary evidence worked. Additive schema/data remained. Candidate was reapplied and fresh EN/FA generation passed while the temporary WAN rules were still active. |
| Durable evidence/audit | Eight successful secondary-source investigations matched returned and stored SHA-256 with durable start/completion records. The gateway's separate, fsynced, text-free source journal correlated the same reads; its envelope hash is distinct from the application's normalized evidence hash. |
| Resource observation | Gateway memory peak 78,012,416 bytes; runner 71,929,856 bytes. Both configured at two reads/no waiting queue, CPU 100%, MemoryMax 256 MiB. These are point-in-time service observations, not sustained-load/NUMA qualification. |

Operational test commands used the protected deployment record's reviewed `cutover-role.sh`,
`rollback-role.sh` and owned-network trial scripts; private browser commands were
`uv run python <protected>/browser-live.py --phase failure --failure`,
`--phase offline --quick`, and `--phase final --quick`. Reports/screenshots remain protected.
Repository verification: `uv run pytest -m "not browser"`, `uv run ruff check .`,
`uv run ruff format --check .`, `uv run mypy --platform linux`,
`uv run python scripts/check_docs.py` and `uv run python scripts/check_release_status.py`.
[Runtime CI 37221712291](https://github.com/Omid-NextAI/nextops/actions/runs/37221712291)
is exact-commit source evidence, not a substitute for the live outcomes above.

### Repairs and limits — do not hide unsuccessful trials

Guarded early trials were restored before correction: the legacy HTTP environment setting needed
a later private environment-file override; SSH forwarding needed both key and sshd restrictions
updated together; the selected-source Nginx route needed the existing bounded assistant timeout
and rate limit; and successful responses needed the installed-code identity header. All are fixed
in the installed candidate. During manual rollback, restoring the app tunnel before connector
SSH policy left an established connection with the old forwarding restriction. Restarting the
tunnel after both restorations recovered primary reads. **Coordinated rollback order: connector,
then app/tunnel; otherwise restart the app tunnel after connector restoration.** Healthz alone is
insufficient; require a fresh authenticated primary read.

The first broad browser run failed a strict number-only general-answer check. A later candidate
probe answered 43, but the restored previous release answered 43 plus unnecessary follow-up text.
Do not mark general instruction-following or held-out semantics passed. Monitoring snapshots were
partial; two additional-target answers were guarded fallbacks, not high-quality generated answers.
No relaxed safety guard, new model or thinking enablement was used to make these tests pass.

WAN rules covered the app and connector guests, not a physical WAN disconnection or all four VM
reboots. AI generation still used the unchanged local CPU service under its existing local-only
network policy. Secondary Zabbix's own upstream network was not changed. Full-system offline cold
start, current-release VM reboot, all-group qualification, sustained load, broad model semantics,
live account creation/reset/disable with an explicitly disposable account, company PKI and
independent recovery remain separate gates. No production certification is claimed.

Temporary source/WAN tables and their rollback timers were removed after successful bounded
checks. Release rollback timers were stopped after final acceptance; app/gateway/runner/tunnel
were active and no failed unit was observed. Protected originals and prior artifacts are retained.

## فارسی

این گزارش حاصل مشاهدهٔ ۴ اکتبر ۲۰۲۶، ساعت ۱۷:۴۸ تا ۱۸:۰۲ UTC است و انتخاب منابع مجاز را
روی ماشین‌های موجودِ برنامه و اتصال‌دهنده تأیید می‌کند؛ نه پذیرش کامل تولید، همهٔ گروه‌ها،
کیفیت عمومی مدل یا بازیابی. اعتبارنامه، نشانی خصوصی، شناسهٔ سازمان، فهرست زیرساخت و شواهد
مرورگر خارج از Git و در محل محافظت‌شده نگه‌داری می‌شوند.

برنامه و اتصال‌دهنده روی انتشار `nextops-0.1.0-2a7c8dc` با commit و هش‌های دقیقِ بخش انگلیسی
مستقرند. مرورگر هش کد نصب‌شده را از سربرگ پاسخ کنترل می‌کند. همان ماشین اتصال‌دهنده میزبان
درگاه SDK رسمی و اجراکنندهٔ جدا با کنترل UID سوکت Unix است. درگاه فقط کلید TLS و توکن خدمت
برنامه را دارد؛ توکن‌های زبیکس و چهار کلید محدود Linux فقط نزد اجراکننده‌اند. برنامه هیچ‌یک
از اعتبارنامه‌های مقصد را دریافت نمی‌کند. خروجی شبکهٔ درگاه فقط loopback است و اجراکننده
تنها مقصدهای دقیقِ مجاز LAN را دارد. هش پیکربندی هر منبع/مقصد در هر سه مرز کنترل می‌شود.
خدمت HTTP قبلی متوقف و غیرفعال است؛ فایل‌های تغییرناپذیرِ بازگشت حفظ شده‌اند. VM، کانتینر،
مدل، runtime، ESXi یا تخصیص منابع تغییر نکرده است.

وابستگی‌های Linux از wheelهای ازپیش‌آماده، با کنترل هش و بدون شبکه نصب شدند؛ نصب/ورود در
فضای نام شبکهٔ جدا نیز موفق و سازگاری ۴۱ بسته تأیید شد. این شاهدِ نصب جای آزمون WAN زنده
نیست. migration افزایشیِ `0004_user_status` فقط مجوز ستون لازم را می‌دهد؛ بازگشت برنامه،
حساب‌ها یا داده‌ها را حذف نمی‌کند.

نتایج واقعی: ۶۴۶ آزمون غیرمرورگر و ۳۰ آزمون مرورگرِ دارای مقصد ساختگی موفق شدند؛ دو آزمون
POSIX در Windows اجرا نشدند. بررسی نوع Linux و پنج کار CI همان commit، شامل PostgreSQL
نسخه‌های 16/17، مرورگر و Gitleaks موفق‌اند. دو منبع و هفت مقصدِ مجاز در فهرست دیده شدند.
منبع دوم سه میزبان در سه گروه دارای عضو دارد؛ پنج گروه خالی هنوز مشاهده و پذیرفته نشده‌اند.
فهرست به‌معنی پویش شبکه یا اثبات سلامت نیست.

شش پاسخ تازهٔ فارسی/انگلیسی برای میزبان زبیکسِ منبع دوم، در سه نشست مرورگر، با تولید واقعی
روی CPU، منشأ/مقصد/نسخه/زمان و هشدار شاهد ناقص دریافت شدند. پاسخ‌های نهایی انگلیسی و فارسی
به‌ترتیب ۳۹٫۸۱۳ و ۵۴٫۶۲۵ ثانیه زمان بردند. Internet-SLA و FortiGate به‌ترتیب در ۳۹٫۸۹۰ و
۳۹٫۵۶۳ ثانیه شاهد مقصد درست را گرفتند، اما پاسخ هر دو `deterministic_fallback` بود؛ کیفیت
تفسیر آزاد مدل برای آن‌ها پذیرفته نیست. مسیر اصلی و شاهد Linux سرور AI نیز حفظ شد؛ بررسی
AI در ۲۹٫۱۷۲ ثانیه با `deterministic_focus` پایان یافت.

منبع غیرمجاز با 403 و ورودی نامعتبرِ کاربر با 422 رد شد. مدیر فهرست «کاربران» را دید؛ جهت
فارسی/انگلیسی، حفظ انتخاب منبع و چیدمان ۳۷۵ پیکسلی آزموده و تصویر نهایی فارسی بازبینی شد.
هیچ حساب شرکتی برای آزمون تغییر نکرد. قطع کنترل‌شدهٔ API منبع دوم، پاسخ روشنِ 503 در
۰٫۲۰۳ ثانیه داد؛ دادهٔ منبع دیگر جای آن ننشست. منبع اصلی کار کرد و AI عمومی پاسخ تازهٔ 43
را در ۰٫۶۰۹ ثانیه تولید کرد. قانون آزمایشی سپس حذف شد.

خروجی WAN ماشین‌های برنامه و اتصال‌دهنده، برای IPv4/IPv6 بسته شد و تلاش تازهٔ اتصال عمومی
ناموفق بود. با حفظ شبکهٔ مدیریت و API دقیقِ منبع دوم، خدمات متوقف/شروع شدند؛ ورود تازه با
TLS معتبر و پاسخ تازهٔ فارسی/انگلیسی در ۵۱٫۱۸۸ و ۴۰٫۱۷۲ ثانیه موفق بودند. درخواست خارجی
مرورگر ثبت نشد. بازگشت، انتشار قبلیِ برنامه `7ce9d29` و اتصال‌دهنده `cdde129`، unitها، تونل،
محدودیت SSH و Nginx را برگرداند؛ ورود و گردآوری تازهٔ منبع اصلی کار کردند و داده/ساختار
افزایشی حفظ شد. استقرار دوبارهٔ نامزد و پاسخ تازهٔ دوزبانه با WAN همچنان بسته موفق بود.

هش شاهدِ هشت تحقیق موفقِ منبع دوم با پاسخ، دادهٔ ذخیره‌شده و رخدادهای آغاز/پایانِ PostgreSQL
مطابقت داشت. دفتر بدون متنِ درگاه نیز خواندن‌ها را با همان شناسهٔ پیگیری و fsync ثبت کرد؛
هش envelope درگاه با هش شاهد نرمال‌شدهٔ برنامه متفاوت است. اوج حافظهٔ مشاهده‌شدهٔ درگاه
۷۸٬۰۱۲٬۴۱۶ و اجراکننده ۷۱٬۹۲۹٬۸۵۶ بایت بود؛ سقف هر خدمت ۲۵۶ MiB و دو خواندن بدون صف است.
این مشاهدهٔ مقطعی جای پذیرش بار مداوم یا NUMA نیست. فرمان‌های آزمون و محل محافظت‌شدهٔ
گزارش‌ها در بخش انگلیسی آمده‌اند؛ خروجی خصوصی در مخزن منتشر نشده است.

آزمون‌های نخست ناموفق پنهان نشده‌اند: تنظیم قدیمی HTTP به فایل محیطیِ خصوصیِ دارای تقدم
نیاز داشت؛ محدودیت forwarding باید هم در کلید و هم در sshd اصلاح می‌شد؛ مسیر تازهٔ Nginx
باید timeout و محدودیت نرخِ موجودِ دستیار را به کار می‌گرفت؛ سربرگ هویت کد نیز لازم بود.
همه در نامزد نصب‌شده اصلاح شدند. در بازگشت دستی، شروع تونل پیش از بازگرداندن سیاست SSH
اتصال‌دهنده، اتصال قدیمی را با محدودیت قبلی نگه داشت. شروع دوبارهٔ تونل پس از بازگرداندن
هر دو طرف، خواندن اصلی را بازیابی کرد. **ترتیب بازگشت هماهنگ: ابتدا اتصال‌دهنده، سپس برنامه
و تونل؛ در ترتیب دیگر، تونل پس از بازگرداندن اتصال‌دهنده دوباره شروع شود.** healthz به‌تنهایی
کافی نیست؛ خواندن تازهٔ احرازشدهٔ منبع اصلی لازم است.

آزمون گستردهٔ نخست در پاسخ صرفاً عددیِ AI عمومی ناموفق بود. نامزد بعداً 43 پاسخ داد، اما
انتشار قبلیِ بازگردانده‌شده، علاوه بر 43 متن پیگیریِ غیرضروری افزود. پیروی عمومی از دستور
یا کیفیت معنایی پذیرفته اعلام نشود. شاهدها ناقص و دو پاسخ مقصد اضافی جایگزینِ قطعی و شفاف
بودند، نه پاسخ تولیدیِ باکیفیت. هیچ کنترل امنیتی شُل، مدل تازه یا حالت تفکر برای موفق نشان
دادن آزمون فعال نشد.

آزمون WAN فقط برنامه و اتصال‌دهنده را پوشش داد؛ قطع فیزیکی WAN یا reboot همهٔ چهار VM
نبود. AI از خدمت CPU محلیِ بدون تغییر و سیاست شبکهٔ محلیِ موجود استفاده کرد؛ شبکهٔ بالادست
زبیکس دوم تغییر نکرد. شروع سردِ کامل، reboot انتشار جاری، همهٔ گروه‌ها، بار مداوم، کیفیت
عمومی مدل، ایجاد/تنظیم گذرواژه/تغییر وضعیتِ زنده با حساب آزمایشیِ صریحاً مجاز، PKI شرکت و
بازیابی مستقل، معیارهای جدا و ناتمام‌اند. پذیرش تولید ادعا نمی‌شود. قوانین شبکه و تایمرهای
آزمایشی پس از آزمون حذف/متوقف شدند؛ خدمات فعال و واحد ناموفق مشاهده نشد. نسخه‌ها و اصل
فایل‌های محافظت‌شده برای بازگشت حفظ‌اند.
