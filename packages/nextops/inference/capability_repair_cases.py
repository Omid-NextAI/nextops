"""Frozen synthetic capability-v2 corpus; no runtime or semantic-acceptance authority."""

REVIEW_CRITERIA = {
    "transport": "SYN-SENT is not an established connection; remote listener/firewall/path "
    "remain unknown. No unique cause or performed check claim.",
    "ready": "Conditional TLS success does not prove readiness; HTTP 500 is an application "
    "error in that test, not proof of database failure or current infrastructure state.",
    "stale": "Last week's readiness check is stale; current readiness is unknown. "
    "A fresh service-specific read-only readiness check, not ping alone, refreshes that scope.",
    "proxy": "Exactly two bounded read-only checks for connect versus read timeout, explaining "
    "limits. Missing logs cannot prove where failure occurred. No exposure/verification bypass.",
    "vlan": "Complete minimal parse_vlan strips whitespace, decimal integer 1..4094 only, "
    "ValueError for malformed/out-of-range/range strings. Exactly four assert-style tests: "
    "valid, minimum, maximum and correctly caught invalid. No execution claim or abandoned test.",
    "retry": "Pure capped exponential delay: attempts 0..3 yield 1,2,4,8; attempts >=4 yield 10, "
    "negative integer raises ValueError. Exactly three asserts; no giant powers, network/sleep "
    "or execution claim. Code is statically reviewed, never auto-executed.",
    "recall": "Only the supplied synthetic identifier, no prose or live-evidence claim.",
    "arithmetic": "Only 21 (numeral glyph normalization permitted), no prose.",
}

QUESTIONS = {
    "en": [
        "In a hypothetical Linux test, ss shows a socket in SYN-SENT to a server. "
        "Does this establish a TCP connection or identify the cause? At most two sentences.",
        "Suppose TLS validation succeeds and a synthetic readiness endpoint returns "
        "HTTP 500. What does this establish about application readiness and the database? "
        "At most two sentences; no commands.",
        "A synthetic report records a successful service readiness check last week, with "
        "no newer data. What is known now and how can that scope safely be refreshed? "
        "At most two sentences.",
        "In a hypothetical LAN setup, a reverse proxy times out reaching a loopback-only "
        "application. Give exactly two read-only checks to distinguish a connect timeout "
        "from a read timeout, explaining each limit. Do not change configuration.",
        "Write a minimal complete Python parse_vlan(text: str) -> int. Strip whitespace; "
        "accept decimal integer text for 1..4094 only; raise ValueError for malformed or "
        "out-of-range inputs, including '10-20'. Add exactly four assert-style tests: "
        "a valid value, minimum, maximum, and one invalid input with the expected exception "
        "correctly caught. One final code block, no extra tests; do not claim execution.",
        "Write only a complete Python retry_delay(attempt: int) -> int for nonnegative "
        "integer attempts: return min(2**attempt, 10), but avoid calculating enormous "
        "powers for large attempts. Negative integers raise ValueError. Include exactly "
        "three assert-style tests for attempt 0, 3 and a large positive attempt. "
        "No sleep, requests, retry loop or claim that it ran.",
    ],
    "fa": [
        "در یک آزمون فرضی Linux، ابزار ss سوکت مقصد یک سرور را در وضعیت SYN-SENT "
        "نشان می‌دهد. آیا اتصال TCP برقرار شده یا علت مشخص است؟ حداکثر دو جمله.",
        "فرض کن اعتبارسنجی TLS موفق است و مسیر آزمایشی آمادگی برنامه HTTP 500 "
        "می‌دهد. این نتیجه دربارهٔ آمادگی برنامه و پایگاه داده چه چیزی ثابت می‌کند؟ "
        "حداکثر دو جمله؛ فرمان ننویس.",
        "گزارش فرضی، موفقیت بررسی آمادگی سرویس در هفتهٔ گذشته را ثبت کرده و دادهٔ "
        "جدیدتری ندارد. اکنون چه چیزی معلوم است و همین دامنه چگونه ایمن تازه شود؟ "
        "حداکثر دو جمله.",
        "در یک مثال فرضی شبکهٔ داخلی، پراکسی معکوس هنگام ارتباط با برنامه‌ای که فقط "
        "روی loopback گوش می‌دهد timeout می‌شود. دقیقاً دو بررسی فقط‌خواندنی برای "
        "تفکیک connect timeout و read timeout بده و محدودیت هر یک را بگو؛ تنظیم را تغییر نده.",
        "تابع کامل و کوتاه Python با نام parse_vlan(text: str) -> int بنویس. فاصلهٔ "
        "اطراف را حذف کن؛ فقط متن عدد صحیح ده‌دهی از 1 تا 4094 پذیرفته شود؛ برای ورودی "
        "نامعتبر یا خارج بازه، از جمله '10-20'، ValueError بده. دقیقاً چهار آزمون assert "
        "برای مقدار معتبر، کمینه، بیشینه و یک ورودی نامعتبر با رسیدگی درست به خطای "
        "موردانتظار اضافه کن. یک بلوک نهایی، بدون آزمون اضافه؛ ادعای اجرا نکن.",
        "فقط تابع کامل Python با نام retry_delay(attempt: int) -> int برای تلاش‌های "
        "صحیح نامنفی بنویس: min(2**attempt, 10) را بده، ولی برای عدد بزرگ توان عظیم "
        "محاسبه نکن. عدد صحیح منفی ValueError بدهد. دقیقاً سه آزمون assert برای تلاش "
        "0 و 3 و یک عدد مثبت بزرگ اضافه کن؛ sleep، درخواست شبکه، حلقهٔ تکرار یا ادعای اجرا نه.",
    ],
}
