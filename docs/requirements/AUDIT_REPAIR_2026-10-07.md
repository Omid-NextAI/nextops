# Audit repair and controlled shipping / اصلاح ممیزی و انتشار کنترل‌شده

Date: 2026-10-07. Status: implementation and qualification in progress, not a deployed release.

## English

### Problem and authority

The owner asks to fix the audited defects and ship the qualified changes to the existing live
guests. The audit at fc271ce found thirteen items: UI-01 through UI-05, AI-01 through AI-03,
SEC-01 through SEC-03, GOV-01 and DOC-01. Private reproductions remain outside Git. The existing
OCS interface and Qwen3.8 selection are working controlled capabilities, not a reason to rebuild.

### Requirements and threat considerations

- Fail closed on login-script/storage failure; never serialize credentials in a URL.
- Retain inference admission ownership through actual native transport drain. A caller timeout
  or cancellation is not remote termination. Reconcile native idle with the pinned local metric
  contract; unknown/malformed state denies new generation. Preserve one active/two queued,
  existing deadlines, CPU-only isolation and the selected native runtime/model.
- Sanitize source-controlled free text before prompts, hashes, storage and responses, including
  common Basic/Bearer/JSON credential forms. Keep explicit redaction and original provenance.
- Revalidate the current session/account/permissions and exact target at the authoritative
  completion/read transaction. Required user-access audit must fail closed.
- End cancelled saved generations with bounded nonce-owned cleanup and text-free audit.
- Supply deterministic scoped counts before model projection; disclose any omitted rows or
  meaningful clipping separately from source partiality. Do not infer reachability or a cause.
- Repair session/chat/account lifetime collisions, evidence cursor synchronization, replaced
  disclosure accessibility state and application-generated Persian labels.
- Correct paired active documentation without rewriting historical acceptance. Treat repository
  administration as its own permission boundary; unavailable administration leaves GOV-01 open.

### Non-goals

No model weights, native system template or Q8 general prompt/sampling/thinking/context settings,
resource expansion, schema
migration, new dependency, GPU/cloud provider, broader target permission, account mutation or
remediation capability. No replacement frontend/authentication. Recovery stays owner-deferred;
raw13/16, thinking/privacy/full-context and other historical unaccepted gates stay visible.

Bounded application evidence-projection instructions change to carry deterministic counts and
honest row/field clipping. This does not change native model prompts or inference profiles.

### Sequence and ownership

1. Add failing deterministic regressions at the actual transport, API/service and browser boundary.
2. Independently repair native scheduler/transport, security/backend and static UI slices.
3. Review integrated changes; run locked lint/types/unit/API/browser and PostgreSQL16/17 CI.
4. Build exact committed artifacts; prove fresh offline installation and package contents.
5. Review the actual protected multi-role publication tools. Preserve root-owned sealed artifacts,
   known-good releases, immutable configs/credentials and owned rollback guards. A separately
   installed Linux collector needs a code-only atomic update, not its provisioning installer.
6. Fresh authorized preflight; drain traffic and promote compatible roles in dependency order,
   preserving native model/runtime PID/settings where the operation permits. Verify exact code,
   real EN/FA answers, saved follow-up, approved secondary evidence/hash/audit, failure recovery,
   source denial, logout/replay and actual rollback before guarded retention.
7. Record sanitized observations, failures, gate status and next unfinished work.

### Acceptance and rollback

Local fixture success is source acceptance only; hosted PostgreSQL is not live database proof.
Browser-origin blocking is not server-WAN acceptance. New contract fields require accepting callers
before emitting providers and reverse rollback order. Abnormal native state requires reconciliation,
not blind retries. Revert only the affected code artifact/collector script to its protected exact
original; no schema downgrade or data deletion. An unhealthy candidate must not prevent restoring
the old release. Do not disarm an owned rollback guard before restoration and verification succeed.

Document every item as passed, failed, partial or not_run. A raw model-quality exception is not an
authorization/audit waiver or general correctness certificate.

## فارسی

مالک رفع موارد ممیزی و انتشار تغییر پذیرفته‌شده روی مهمان‌های موجود را خواسته است. ممیزی کد
fc271ce سیزده مورد UI-01 تاUI-05، AI-01 تاAI-03، SEC-01 تاSEC-03، GOV-01 و DOC-01 دارد.
رابط فعلی OCS و انتخاب Qwen3.8 بازسازی نمی‌شوند؛ ابزارها و شاهد خصوصی خارج Git باقی‌اند.

ورود با شکست script/storage نباید اطلاعات ورود در URL بدهد. ظرفیت استنتاج تا پایان واقعی کار
بومی متعلق به درخواست است؛ لغو انتظار، توقف دوردست را ثابت نمی‌کند. idle بومی با قرارداد سنجهٔ
نسخهٔ ثابت کنترل شود و وضعیت غایب/نامعتبر تولید تازه را رد کند. یک فعال/دو منتظر، زمان‌ها، CPU،
مدل و isolation ثابت‌اند. متن آزاد منبع پیش از prompt، هش، ذخیره و پاسخ، با پوشش Basic/Bearer/JSON
پالایش و علامت redaction آشکار شود. نشست/حساب/مجوز/هدف در transaction معتبر تکمیل و خواندن دوباره
کنترل و ممیزی الزامی بسته اجرا شود. لغو سابقه cleanup محدود با nonce و audit بی‌متن دارد.
شمارش دامنه پیش از projection قطعی و حذف/کوتاه‌سازی از ناقص‌بودن منبع جدا اعلام شود؛ علت و
reachability از آن ساخته نشوند. race نشست/گفت‌وگو/کاربر، cursor شاهد، aria جزئیات و label فارسی
اصلاح شوند. راهنمای فعال جفت اصلاح، تاریخچه حفظ و نبود مجوز admin برای GOV-01 پنهان نشود.

وزن مدل، قالب بومی و prompt عمومی Q8، sampler، thinking/context، منابع، پایگاه، وابستگی، GPU/ابر، target scope، حساب و
توان تغییر تجهیز خارج دامنه‌اند. frontend و ورود جایگزین نمی‌شوند. recovery در تعویق مالک و
خام۱۳/۱۶ و معیارهای پذیرفته‌نشدهٔ تاریخی ثابت می‌مانند.

دستورهای محدود projection شاهد برنامه برای شمارش قطعی و اعلام حذف سطر/کوتاه‌سازی field اصلاح
می‌شوند؛ این تغییر به معنای تغییر prompt بومی مدل یا profile استنتاج نیست.

ترتیب کار: regression واقعی و محدود؛ اصلاح مستقل سه بخش؛ review مشترک و lint/types/unit/API/browser
و CI پایگاه16/17؛ artifact کد commitشده و نصب تازهٔ آفلاین؛ بازبینی ابزار انتشار محافظت‌شدهٔ چندنقشی.
collector مستقل با جایگزینی اتمی فقط script منتشر شود، نه اجرای installer حساب/کلید/config.
پیش از انتشار، preflight تازه و drain، ترتیب سازگار سرویس و بازگشت دقیق لازم است. مدل/تنظیم/PID
بومی تا حد مجاز عملیات ثابت بماند. پاسخ واقعی EN/FA، ادامهٔ سابقه، منبع دوم، hash/audit، خطا/بازیابی،
رد scope و logout/replay و rollback پیش از retention بررسی شوند؛ شاهد پالایش‌شده و گام بعد ثبت شود.

موفقیت fixture فقط پذیرش کد و CI پایگاه جای شاهد پایگاه زنده نیست. منع origin مرورگر، WAN سرور
نیست. برای field تازه، مصرف‌کننده پیش از تولیدکننده منتشر و برعکس برگردانده شود. وضعیت بومی
نامعلوم تطبیق می‌خواهد، نه تکرار کور. بازگشت فقط artifact یا script دقیق قبلی است؛ schema/data
حذف نشود. خرابی candidate نباید بازگرداندن نسخهٔ قدیم را متوقف کند و guard پیش از تأیید بازگشت
غیرفعال نشود. هر مورد passed/failed/partial/not_run ثبت شود؛ استثنای کیفیت، حذف امنیت نیست.
