"use strict";

const translations = {
  en: {
    skipMain: "Skip to main content",
    brandTagline: "Local operations intelligence", localEnvironment: "Private local environment",
    languageToggleAria: "Switch interface language", logout: "Sign out",
    companyLabel: "AN OCS TECHNOLOGY PLATFORM", companyName: "Omid System Computer Services",
    evaluationLabel: "CONTROLLED USER EVALUATION",
    loginHeadline: "Operational insight,<br><span>kept inside your network.</span>",
    loginLead: "A private, bilingual operations workspace for evidence-grounded infrastructure intelligence.",
    trustOne: "Local identity", trustTwo: "Encrypted access", trustThree: "CPU-only inference",
    trustOneText: "Organization-controlled access", trustTwoText: "Protected application path", trustThreeText: "No cloud AI fallback",
    secureAccess: "SECURE ACCESS", welcome: "Welcome to NextOps", credentialsPrompt: "Enter your evaluation credentials.", username: "Username",
    password: "Password", signIn: "Sign in securely", privacyNote: "Your session is stored only in this browser tab.",
    workspaceLabel: "NEXTOPS OPERATIONS WORKSPACE", workspaceHeadline: "Ask the local assistant",
    workspaceLead: "Technical guidance for NOC and SOC teams, with live evidence kept distinct from model knowledge.",
    serviceStatus: "Service status",
    appReady: "Application ready", aiChecking: "Checking AI", aiReady: "AI ready", aiUnavailable: "AI unavailable",
    monitoringChecking: "Checking monitoring", monitoringReady: "Monitoring ready", monitoringUnavailable: "Monitoring unavailable",
    assistantLabel: "LOCAL AI ASSISTANT", newQuestion: "New question", questionHelp: "Ask in English or Persian. The answer follows the selected language.",
    answerMode: "Answer mode", generalMode: "General assistant", monitoringMode: "Live monitoring", incidentMode: "Incident investigation",
    generalModeHelp: "Answers the question directly without attaching Zabbix status.",
    monitoringModeHelp: "Uses current read-only Zabbix observations and shows the supporting evidence.",
    incidentModeHelp: "Combines bounded Zabbix history and events with direct read-only Linux diagnostics for one approved host.",
    incidentTarget: "Investigation target", incidentTargetHelp: "Choose one approved host. NextOps will retrieve bounded Zabbix and direct read-only Linux evidence.",
    noIncidentTargets: "No approved investigation target is available.",
    checkingNamedTarget: "Retrieving approved read-only evidence for target",
    targetMismatchError: "The selected host does not match your question. Select the approved host you named and try again.",
    answerLanguage: "Answer language", question: "Question", questionPlaceholder: "Explain a safe first response to a high CPU alert.", askAssistant: "Ask assistant",
    evidenceBoundary: "EVIDENCE BOUNDARY", liveEvidenceTitle: "Intelligence with a clear source",
    liveEvidenceBody: "NextOps keeps model generation, evidence access, and credentials inside separate protected boundaries.",
    boundaryLocal: "Local processing", boundaryLocalText: "No external model API is used.",
    boundaryAuth: "Authenticated path", boundaryAuthText: "The browser never receives the AI service credential.",
    boundaryZabbix: "Qualified evidence", boundaryZabbixText: "Read-only, source-qualified and timestamped.",
    readOnlyTitle: "Read-only by design", readOnlyText: "This evaluation workspace cannot execute infrastructure changes.",
    assistantResponse: "NextOps", generalResponseTitle: "Direct local answer", responseTitle: "Evidence-grounded result",
    modelOnlyBadge: "Local model · no live evidence", liveEvidenceBadge: "Live Zabbix evidence", incidentEvidenceBadge: "Live Zabbix + Linux evidence",
    modelIntegrityNotice: "Model-generated text has no live evidence; verify important facts independently.",
    evidenceIntegrityNotice: "This answer passed bounded source checks, not a factual or relevance review. Verify it against the evidence below.",
    fallbackIntegrityNotice: "The generated answer was incomplete or failed a required check. The evidence-only summary below may not answer your full question.",
    generalFallbackIntegrityNotice: "The model reply failed a required check. The displayed local fallback does not report live infrastructure status.",
    focusedIntegrityNotice: "This is a deterministic, scope-limited summary of approved read-only observations, not a verified model explanation.",
    fileLimitNotice: "System file names and contents are outside the current read-only collector scope. Incident mode can show approved mount capacity only.",
    hostInventoryLimitNotice: "This Zabbix view does not contain reachability states for the authorized host inventory; it cannot identify unavailable hosts.",
    targetLimitNotice: "This evidence belongs to another host and cannot establish the status of the server you asked about.",
    fileListingNotCollected: "No system file names or contents were collected. The complete authorized evidence is available below if you need other diagnostics.",
    redirectIntegrityNotice: "The question requires live evidence and was not answered from model memory. Choose a live evidence mode.",
    source: "Source", host: "Host", collected: "Collected", problems: "Active problems", coverage: "Evidence coverage",
    complete: "Complete", partial: "Partial (bounded)", stale: "stale",
    model: "Model", tokens: "Output tokens", completed: "Completed", requestId: "Request",
    runId: "Durable run", evidenceReference: "Evidence reference", auditEvent: "Audit event",
    linuxSnapshot: "Linux snapshot", zabbixTimeline: "Zabbix timeline", systemLoad: "System load", memoryAvailable: "Memory available",
    uptime: "Uptime", filesystems: "Filesystems", services: "Allowlisted services", recentEvents: "Recent Zabbix events",
    configuredResolvers: "Configured resolvers", recordedRoutes: "Recorded routes", listeningSockets: "Listening sockets",
    criticalJournal: "High-priority journal", noEntries: "No entries in the bounded window", partialReasons: "Partial reasons",
    available: "available", historyPoints: "history points", eventRecords: "events",
    footer: "Private, controlled user-evaluation environment", invalidLogin: "The username or password is incorrect.",
    genericError: "The request could not be completed. Try again.", timeoutError: "The local model took too long. Please try a shorter question.",
    overloadedError: "The local model is busy. Please wait a moment and try again.", dependencyError: "A local service is temporarily unavailable. Please try again.",
    sessionExpired: "Your session expired. Please sign in again.",
    working: "Generating locally…",
    howEvidenceWorks: "How evidence works", youAsked: "You asked", showEvidence: "View evidence and request details", showCompleteEvidence: "Show complete authorized evidence",
    sourceBrief: "Source", collectedBrief: "Collected", linuxCollected: "Linux collected", zabbixCollected: "Zabbix collected", scopeBrief: "Scope", filesystemScope: "Approved filesystem mounts only", fileScope: "File names and contents unavailable", networkScope: "Recorded network observations only", serviceScope: "Recorded service observations only", networkServiceScope: "Recorded network and service observations", incidentScope: "Approved incident target", monitoringScope: "Zabbix monitoring", keyboardHint: " · Enter to send · Shift+Enter for a new line"
  },
  fa: {
    skipMain: "رفتن به محتوای اصلی",
    brandTagline: "هوشمندی داخلی برای عملیات", localEnvironment: "محیط خصوصی و داخلی",
    languageToggleAria: "تغییر زبان رابط", logout: "خروج",
    companyLabel: "یک راهکار فناورانه از OCS", companyName: "شرکت رایانه خدمات امید سیستم",
    evaluationLabel: "محیط کنترل‌شدهٔ ارزیابی کاربران",
    loginHeadline: "شفافیت در عملیات؛<br><span>درون شبکهٔ سازمان شما.</span>",
    loginLead: "فضای کاری خصوصی و دوزبانه برای تحلیل زیرساخت بر پایهٔ شواهد قابل‌ردیابی.",
    trustOne: "هویت داخلی", trustTwo: "دسترسی رمزنگاری‌شده", trustThree: "پردازش صرفاً با CPU",
    trustOneText: "دسترسی تحت کنترل سازمان", trustTwoText: "مسیر محافظت‌شدهٔ برنامه", trustThreeText: "بدون جایگزین ابری برای هوش مصنوعی",
    secureAccess: "دسترسی امن", welcome: "به NextOps خوش آمدید", credentialsPrompt: "مشخصات دسترسی محیط ارزیابی را وارد کنید.", username: "نام کاربری",
    password: "گذرواژه", signIn: "ورود امن", privacyNote: "نشست شما فقط در همین برگه مرورگر نگهداری می‌شود.",
    workspaceLabel: "فضای عملیات NextOps", workspaceHeadline: "از دستیار داخلی بپرسید",
    workspaceLead: "هر بار یک پرسش مطرح کنید. پاسخ‌ها مستقل‌اند و سابقهٔ این صفحه به درخواست بعدی فرستاده نمی‌شود.",
    serviceStatus: "وضعیت سرویس‌ها",
    appReady: "برنامه آماده است", aiChecking: "در حال بررسی سرویس هوش مصنوعی", aiReady: "سرویس هوش مصنوعی آماده است", aiUnavailable: "سرویس هوش مصنوعی در دسترس نیست",
    monitoringChecking: "در حال بررسی سامانه پایش", monitoringReady: "سامانه پایش آماده است", monitoringUnavailable: "سامانه پایش در دسترس نیست",
    assistantLabel: "دستیار هوش مصنوعی داخلی", newQuestion: "پرسش جدید", questionHelp: "پرسش را به فارسی یا انگلیسی بنویسید؛ پاسخ به زبان انتخاب‌شده ارائه می‌شود.",
    answerMode: "شیوهٔ پاسخ", generalMode: "دستیار عمومی", monitoringMode: "پایش زنده", incidentMode: "بررسی رخداد",
    generalModeHelp: "بدون افزودن وضعیت Zabbix، مستقیماً به همان پرسش پاسخ می‌دهد.",
    monitoringModeHelp: "از دادهٔ جاری و فقط‌خواندنی Zabbix استفاده می‌کند و شاهد را نیز نشان می‌دهد.",
    incidentModeHelp: "تاریخچه و رویدادهای محدودشدهٔ Zabbix را با داده‌های تشخیصی مستقیم و فقط‌خواندنی Linux برای یک میزبان مجاز ترکیب می‌کند.",
    incidentTarget: "میزبان بررسی", incidentTargetHelp: "یک میزبان مجاز را انتخاب کنید؛ NextOps شواهد محدودشدهٔ Zabbix و Linux را گردآوری می‌کند.",
    noIncidentTargets: "هیچ میزبان مجاز برای بررسی تعریف نشده است.",
    checkingNamedTarget: "در حال گردآوری شواهد فقط‌خواندنیِ مجاز برای میزبان",
    targetMismatchError: "میزبان انتخاب‌شده با پرسش شما مطابقت ندارد. میزبان مجازی را که نام برده‌اید انتخاب کنید و دوباره بپرسید.",
    answerLanguage: "زبان پاسخ", question: "پرسش", questionPlaceholder: "برای هشدار مصرف بالای پردازنده، یک اقدام اولیه ایمن پیشنهاد کنید.", askAssistant: "ارسال به دستیار",
    evidenceBoundary: "مرز شواهد", liveEvidenceTitle: "هوشمندی با منبع روشن",
    liveEvidenceBody: "NextOps تولید پاسخ، دسترسی به شواهد و اطلاعات ورود را در مرزهای محافظت‌شده و جدا از هم نگه می‌دارد.",
    boundaryLocal: "پردازش داخلی", boundaryLocalText: "هیچ سرویس مدل بیرونی فراخوانی نمی‌شود.",
    boundaryAuth: "مسیر احراز هویت‌شده", boundaryAuthText: "اعتبارنامه سرویس هوش مصنوعی هرگز در اختیار مرورگر قرار نمی‌گیرد.",
    boundaryZabbix: "شواهد دارای اصالت", boundaryZabbixText: "فقط‌خواندنی، دارای منبع مشخص و مُهر زمانی.",
    readOnlyTitle: "فقط‌خواندنی، از ابتدا", readOnlyText: "این فضای ارزیابی امکان اجرای تغییر روی زیرساخت را ندارد.",
    assistantResponse: "پاسخ دستیار", generalResponseTitle: "پاسخ مستقیم مدل محلی", responseTitle: "نتیجه مبتنی بر شواهد",
    modelOnlyBadge: "مدل محلی · بدون شاهد زنده", liveEvidenceBadge: "شواهد زنده Zabbix", incidentEvidenceBadge: "شواهد زنده Zabbix و Linux",
    modelIntegrityNotice: "این متن را مدل و بدون شاهد زنده تولید کرده است؛ اطلاعات مهم را به‌طور مستقل راستی‌آزمایی کنید.",
    evidenceIntegrityNotice: "این پاسخ فقط کنترل‌های محدودِ منبع را گذرانده است، نه بررسی درستی یا ارتباط با پرسش؛ آن را با شواهد زیر تطبیق دهید.",
    fallbackIntegrityNotice: "پاسخ تولیدشده ناتمام بود یا یکی از کنترل‌های لازم را نگذرانده است. خلاصهٔ مبتنی بر شواهد ممکن است به همهٔ بخش‌های پرسش شما پاسخ ندهد.",
    generalFallbackIntegrityNotice: "پاسخ مدل یکی از کنترل‌های لازم را نگذرانده است. متن جایگزینِ داخلی، گزارشی از وضعیت زندهٔ زیرساخت نیست.",
    focusedIntegrityNotice: "این متن، خلاصه‌ای محدود به دامنهٔ مشاهدات فقط‌خواندنیِ مجاز است؛ نه توضیح راستی‌آزمایی‌شدهٔ مدل.",
    fileLimitNotice: "نام و محتوای فایل‌های سیستم در دامنهٔ گردآورندهٔ فقط‌خواندنیِ کنونی نیستند. حالت بررسی رخداد فقط ظرفیت نقاط اتصالِ مجاز را نشان می‌دهد.",
    hostInventoryLimitNotice: "این نمای زبیکس وضعیت دسترسیِ فهرست میزبان‌های مجاز را ندارد و نمی‌تواند میزبان‌های خارج از دسترس را مشخص کند.",
    targetLimitNotice: "این شاهد مربوط به میزبان دیگری است و وضعیت سروری را که دربارهٔ آن پرسیده‌اید مشخص نمی‌کند.",
    fileListingNotCollected: "نام یا محتوای فایل‌های سیستم گردآوری نشده است. اگر به داده‌های تشخیصی دیگر نیاز دارید، می‌توانید شواهد کاملِ مجاز را در بخش پایین باز کنید.",
    redirectIntegrityNotice: "این پرسش به شاهد زنده نیاز دارد و از حافظهٔ مدل پاسخ داده نشد؛ یکی از حالت‌های دارای شاهد زنده را انتخاب کنید.",
    source: "منبع", host: "میزبان", collected: "زمان گردآوری", problems: "مسائل فعال", coverage: "پوشش شواهد",
    complete: "کامل", partial: "جزئی (محدودشده)", stale: "قدیمی",
    model: "مدل", tokens: "توکن‌های خروجی", completed: "زمان تکمیل", requestId: "شناسه درخواست",
    runId: "اجرای ماندگار", evidenceReference: "مرجع شاهد", auditEvent: "رویداد ممیزی",
    linuxSnapshot: "نمای لحظه‌ای Linux", zabbixTimeline: "خط زمانی Zabbix", systemLoad: "بار سامانه", memoryAvailable: "حافظهٔ در دسترس",
    uptime: "مدت کارکرد", filesystems: "فایل‌سیستم‌ها", services: "سرویس‌های مجاز", recentEvents: "رویدادهای اخیر Zabbix",
    configuredResolvers: "نام‌سرورهای پیکربندی‌شده", recordedRoutes: "مسیرهای ثبت‌شده", listeningSockets: "سوکت‌های در حال شنود",
    criticalJournal: "رخدادهای پراهمیت سامانه", noEntries: "در بازهٔ محدودشده موردی ثبت نشده است", partialReasons: "دلایل ناقص بودن شاهد",
    available: "در دسترس", historyPoints: "نقطهٔ تاریخی", eventRecords: "رویداد",
    footer: "محیط خصوصی و کنترل‌شدهٔ ارزیابی کاربران", invalidLogin: "نام کاربری یا گذرواژه صحیح نیست.",
    genericError: "انجام درخواست ممکن نشد. دوباره تلاش کنید.", timeoutError: "زمان پردازش مدل محلی به پایان رسید. لطفاً پرسش کوتاه‌تری مطرح کنید.",
    overloadedError: "مدل محلی در حال پردازش درخواست دیگری است. لطفاً کمی بعد دوباره تلاش کنید.", dependencyError: "یکی از سرویس‌های داخلی موقتاً در دسترس نیست. لطفاً دوباره تلاش کنید.",
    sessionExpired: "نشست شما پایان یافته است. دوباره وارد شوید.",
    working: "در حال تولید پاسخ در محیط داخلی…",
    howEvidenceWorks: "شیوهٔ استفاده از شواهد", youAsked: "پرسش شما", showEvidence: "نمایش شواهد و جزئیات درخواست", showCompleteEvidence: "نمایش همهٔ شواهد مجاز",
    sourceBrief: "منبع", collectedBrief: "زمان گردآوری", linuxCollected: "زمان گردآوری Linux", zabbixCollected: "زمان گردآوری Zabbix", scopeBrief: "دامنه", filesystemScope: "فقط نقاط اتصال فایل‌سیستمِ مجاز", fileScope: "نام و محتوای فایل‌ها در دسترس نیست", networkScope: "فقط مشاهدات ثبت‌شدهٔ شبکه", serviceScope: "فقط مشاهدات ثبت‌شدهٔ سرویس", networkServiceScope: "مشاهدات ثبت‌شدهٔ شبکه و سرویس", incidentScope: "میزبان مجازِ بررسی", monitoringScope: "پایش Zabbix", keyboardHint: " · Enter برای ارسال · Shift+Enter برای سطر تازه"
  }
};

const state = {
  language: (() => { try { return localStorage.getItem("nextops-language") === "fa" ? "fa" : "en"; } catch { return "en"; } })(),
  answerLocale: "en",
  answerMode: "general",
  incidentTargets: [],
  sourceCatalog: [],
  lastEvidence: null,
  history: [],
  conversationsEnabled: false,
  thinkingEnabled: false,
  conversationId: null,
  pendingMessage: null,
  busy: false,
  epoch: 0,
  actor: null,
  users: [],
  usersOffset: 0,
  usersNext: null,
  usersBusy: false,
  passwordUser: null,
  token: sessionStorage.getItem("nextops-session") || ""
};
const byId = id => document.getElementById(id);
Object.assign(translations.en, {
  monitoringSource: "Zabbix source", monitoringSourceTarget: "Approved host",
  primaryOverview: "Primary Zabbix · default host", approvedCatalogHelp: "Approved inventory, not a live health check. Sending a question retrieves fresh evidence for this host.",
  sourceCatalogUnavailable: "Additional-source catalogue is unavailable. The primary source remains selectable; no automatic fallback will occur.",
  sourceTargetRequired: "Choose an approved host for this source."
});
Object.assign(translations.fa, {
  monitoringSource: "منبع زبیکس", monitoringSourceTarget: "میزبان مجاز",
  primaryOverview: "زبیکس اصلی · میزبان پیش‌فرض", approvedCatalogHelp: "این فهرست، مقصدهای مجاز را نشان می‌دهد، نه سلامت زندهٔ آن‌ها را. با ارسال پرسش، شاهد تازهٔ همان میزبان گردآوری می‌شود.",
  sourceCatalogUnavailable: "فهرست منابع افزوده در دسترس نیست. منبع اصلی قابل انتخاب است؛ جایگزینی خودکار منبع انجام نمی‌شود.",
  sourceTargetRequired: "برای این منبع، یک میزبان مجاز انتخاب کنید."
});
const resultTemplate = byId("resultCard").cloneNode(true);

Object.assign(translations.en, {
  usersTitle: "Users", usersKicker: "LOCAL ACCESS CONTROL", usersLead: "Manage local accounts. Every change is audited; no infrastructure permissions are granted.",
  usersBack: "Back to assistant", usersAccounts: "Local accounts", usersRefresh: "Refresh", usersPrevious: "Previous", usersNext: "Next", usersCreate: "Create an account", usersRole: "Role",
  usersViewer: "Viewer · Zabbix read", usersOperator: "Operator · Zabbix and Linux read", usersEngineer: "Engineer · Zabbix and Linux read", usersAdmin: "Administrator",
  usersNameHelp: "3–64 lowercase Latin letters, digits, dots, hyphens or underscores; start with a letter.", usersInitialPassword: "Initial password", usersNewPassword: "New password", usersPasswordHelp: "14–256 characters. Deliver securely outside this panel; passwords are never listed.",
  usersProtectedHelp: "Administrator accounts are protected. Role permissions are fixed and read-only.", usersProtected: "Protected administrator", usersActive: "Active", usersDisabled: "Disabled", usersDisable: "Disable account", usersEnable: "Enable account", usersReset: "Reset password", usersCancel: "Cancel",
  usersResetConfirm: "I confirm: this revokes every session for the selected account.", usersChangeConfirm: "Change account status and revoke every session for", usersLoading: "Loading accounts…", usersSaving: "Saving the audited change…", usersSaved: "Change saved and audited.", usersEmpty: "No accounts on this page.",
  usersConflict: "The account changed or its username already exists. Refresh the list before trying again.", usersDenied: "Administrator access is required; protected accounts cannot be changed here.", usersUnknown: "The request could not be confirmed. Refresh to check the account before retrying; do not repeat a password reset blindly."
});
Object.assign(translations.fa, {
  usersTitle: "کاربران", usersKicker: "کنترل دسترسی محلی", usersLead: "حساب‌های محلی را مدیریت کنید. هر تغییر ممیزی می‌شود؛ مجوز تغییر زیرساخت اعطا نمی‌شود.",
  usersBack: "بازگشت به دستیار", usersAccounts: "حساب‌های محلی", usersRefresh: "تازه‌سازی", usersPrevious: "قبلی", usersNext: "بعدی", usersCreate: "ایجاد حساب", usersRole: "نقش",
  usersViewer: "بیننده · مشاهدهٔ Zabbix", usersOperator: "اپراتور · مشاهدهٔ Zabbix و Linux", usersEngineer: "کارشناس · مشاهدهٔ Zabbix و Linux", usersAdmin: "مدیر سامانه",
  usersNameHelp: "۳ تا ۶۴ حرف کوچک لاتین، رقم، نقطه، خط تیره یا زیرخط؛ با حرف آغاز شود.", usersInitialPassword: "گذرواژهٔ اولیه", usersNewPassword: "گذرواژهٔ جدید", usersPasswordHelp: "۱۴ تا ۲۵۶ نویسه؛ از مسیر امن خارج از پنل تحویل دهید. گذرواژه در فهرست نمایش داده نمی‌شود.",
  usersProtectedHelp: "حساب مدیر محافظت شده است. دسترسی نقش‌ها ثابت و فقط‌خواندنی است.", usersProtected: "مدیر محافظت‌شده", usersActive: "فعال", usersDisabled: "غیرفعال", usersDisable: "غیرفعال‌کردن حساب", usersEnable: "فعال‌کردن حساب", usersReset: "تنظیم گذرواژه", usersCancel: "انصراف",
  usersResetConfirm: "تأیید می‌کنم: همهٔ نشست‌های حساب انتخاب‌شده لغو می‌شود.", usersChangeConfirm: "تغییر وضعیت حساب و لغو همهٔ نشست‌های", usersLoading: "در حال دریافت حساب‌ها…", usersSaving: "در حال ثبت تغییر و ممیزی…", usersSaved: "تغییر و ممیزی ثبت شد.", usersEmpty: "در این صفحه حسابی وجود ندارد.",
  usersConflict: "حساب تغییر کرده یا نام کاربری تکراری است؛ پیش از تلاش دوباره فهرست را تازه‌سازی کنید.", usersDenied: "دسترسی مدیر لازم است؛ حساب محافظت‌شده از این بخش قابل تغییر نیست.", usersUnknown: "نتیجهٔ درخواست تأیید نشد. پیش از تکرار، فهرست را تازه‌سازی و وضعیت را بررسی کنید؛ تنظیم گذرواژه را بدون بررسی تکرار نکنید."
});

function closeUserPassword() {
  state.passwordUser = null;
  byId("userPasswordForm").reset();
  byId("userPasswordName").textContent = "";
  byId("userPasswordForm").classList.add("hidden");
}

function renderUsers() {
  const t = translations[state.language];
  byId("usersList").replaceChildren();
  for (const user of state.users) {
    const row = document.createElement("li"); row.className = "user-row";
    const name = document.createElement("bdi"); name.dir = "ltr"; name.textContent = user.username;
    const detail = document.createElement("p");
    const roleLabels = { viewer: t.usersViewer, operator: t.usersOperator, engineer: t.usersEngineer, admin: t.usersAdmin };
    detail.textContent = `${user.roles.map(role => roleLabels[role] || role).join(" · ")} · ${user.is_active ? t.usersActive : t.usersDisabled}`;
    row.append(name, detail);
    if (user.manageable) {
      const actions = document.createElement("div"); actions.className = "user-actions";
      const status = document.createElement("button"); status.type = "button"; status.className = `quiet-button ${user.is_active ? "user-disable" : ""}`; status.textContent = user.is_active ? t.usersDisable : t.usersEnable;
      status.addEventListener("click", () => {
        if (!state.usersBusy && window.confirm(`${translations[state.language].usersChangeConfirm} ${user.username}?`)) {
          userMutation(`/api/v1/users/${user.identity_id}`, "PATCH", { is_active: !user.is_active, expected_version: user.credential_version });
        }
      });
      const password = document.createElement("button"); password.type = "button"; password.className = "quiet-button"; password.textContent = t.usersReset;
      password.addEventListener("click", () => {
        closeUserPassword(); state.passwordUser = user;
        byId("userPasswordName").textContent = user.username;
        byId("userPasswordForm").classList.remove("hidden"); byId("userResetPassword").focus();
      });
      status.disabled = password.disabled = state.usersBusy;
      actions.append(status, password); row.append(actions);
    } else {
      const protectedNote = document.createElement("p"); protectedNote.textContent = t.usersProtected; row.append(protectedNote);
    }
    byId("usersList").append(row);
  }
  byId("usersPrevious").disabled = state.usersBusy || state.usersOffset === 0;
  byId("usersNext").disabled = state.usersBusy || state.usersNext === null;
}

function setUsersBusy(busy) {
  state.usersBusy = busy;
  byId("usersView").setAttribute("aria-busy", String(busy));
  byId("usersView").querySelectorAll("input, select, button:not(#usersBack)").forEach(control => { control.disabled = busy; });
  renderUsers();
}

function userError(error) {
  const t = translations[state.language];
  byId("usersError").textContent = error.status === 409 ? t.usersConflict : error.status === 403 ? t.usersDenied : t.usersUnknown;
  byId("usersError").focus();
}

async function refreshUsers(offset = state.usersOffset) {
  if (state.usersBusy) return false;
  const epoch = state.epoch;
  setUsersBusy(true); byId("usersError").textContent = "";
  byId("usersStatus").textContent = translations[state.language].usersLoading;
  try {
    const page = await api(`/api/v1/users?offset=${offset}`);
    if (epoch !== state.epoch) return false;
    state.users = page.users; state.usersOffset = offset; state.usersNext = page.next_offset;
    closeUserPassword(); renderUsers();
    byId("usersStatus").textContent = page.users.length ? "" : translations[state.language].usersEmpty;
    return true;
  } catch (error) {
    if (epoch === state.epoch && state.token) { byId("usersStatus").textContent = ""; userError(error); }
    return false;
  } finally { if (epoch === state.epoch) setUsersBusy(false); }
}

async function userMutation(path, method, payload) {
  if (state.usersBusy) return;
  const epoch = state.epoch;
  byId("userCreatePassword").value = ""; byId("userResetPassword").value = "";
  byId("userResetConfirm").checked = false;
  setUsersBusy(true); byId("usersError").textContent = "";
  byId("usersStatus").textContent = translations[state.language].usersSaving;
  try {
    await api(path, { method, body: JSON.stringify(payload) });
    if (epoch !== state.epoch) return;
    closeUserPassword(); byId("userCreateForm").reset();
    setUsersBusy(false);
    if (await refreshUsers()) {
      byId("usersStatus").textContent = translations[state.language].usersSaved;
      byId(path === "/api/v1/users" ? "userCreateName" : "usersRefresh").focus();
    }
  } catch (error) {
    if (epoch === state.epoch && state.token) { byId("usersStatus").textContent = ""; userError(error); }
  } finally { if (epoch === state.epoch) setUsersBusy(false); }
}

byId("usersButton").addEventListener("click", () => {
  if (!state.actor?.roles.includes("admin")) return;
  byId("profileMenu").open = false;
  byId("workspaceView").classList.add("hidden"); byId("usersView").classList.remove("hidden");
  byId("usersHeading").focus(); refreshUsers();
});
byId("usersBack").addEventListener("click", () => {
  closeUserPassword(); byId("userCreateForm").reset();
  byId("usersView").classList.add("hidden"); byId("workspaceView").classList.remove("hidden");
  queueMicrotask(() => { byId("profileMenu").open = true; byId("usersButton").focus(); });
});
byId("usersRefresh").addEventListener("click", () => refreshUsers());
byId("usersPrevious").addEventListener("click", () => refreshUsers(Math.max(0, state.usersOffset - 50)));
byId("usersNext").addEventListener("click", () => { if (state.usersNext !== null) refreshUsers(state.usersNext); });
byId("userResetCancel").addEventListener("click", closeUserPassword);
byId("userCreateForm").addEventListener("submit", event => {
  event.preventDefault(); userMutation("/api/v1/users", "POST", { username: byId("userCreateName").value, password: byId("userCreatePassword").value, role: byId("userCreateRole").value });
});
byId("userPasswordForm").addEventListener("submit", event => {
  event.preventDefault();
  const user = state.passwordUser;
  if (user && byId("userResetConfirm").checked) userMutation(`/api/v1/users/${user.identity_id}/password`, "POST", { new_password: byId("userResetPassword").value, expected_version: user.credential_version });
});

Object.assign(translations.en, {
  savedChats: "YOUR CONVERSATIONS", savedPrivacy: "Private to your account · retained for 30 days. Do not paste secrets.",
  deleteChat: "Delete this conversation", deleteChatConfirm: "Delete this saved conversation permanently? Audit metadata will remain.",
  savedContextHelp: "Saved locally for 30 days. Follow-ups use up to six recent exchanges; live requests always fetch new evidence.",
  savedContextOmitted: "Older or oversized exchanges were left out of model context. Include any missing detail in your question.",
  savedChatsUnavailable: "Saved conversations are unavailable. The current chat cannot be saved.",
  olderMessages: "Showing the latest 12 exchanges. Earlier exchanges remain saved.",
  savedHistoryUnavailable: "The history list is temporarily unavailable. Your answer was saved.",
  thinkingMode: "Response mode", standardResponse: "Standard", thinkingResponse: "Think more · slower",
  thinkingHelp: "Local, bounded reasoning. Only the final answer is shown and saved; thinking does not verify facts.",
  conflictError: "This conversation already has a pending request. Wait before retrying.",
  contextExceeded: "This question and its context exceed the model limit. Start a new conversation or shorten the question."
});
Object.assign(translations.fa, {
  savedChats: "گفت‌وگوهای شما", savedPrivacy: "فقط برای حساب شما · نگهداری تا ۳۰ روز. اطلاعات محرمانه وارد نکنید.",
  deleteChat: "حذف این گفت‌وگو", deleteChatConfirm: "این گفت‌وگو برای همیشه حذف شود؟ فرادادهٔ ممیزی باقی می‌ماند.",
  savedContextHelp: "گفت‌وگو تا ۳۰ روز به‌صورت محلی ذخیره می‌شود. پیگیری از حداکثر شش پرسش‌وپاسخ اخیر استفاده می‌کند؛ درخواست زنده همیشه شاهد تازه می‌گیرد.",
  savedContextOmitted: "بخشی از گفت‌وگوهای قدیمی یا طولانی از زمینهٔ مدل کنار گذاشته شده است. جزئیات لازم را در پرسش خود بیاورید.",
  savedChatsUnavailable: "گفت‌وگوهای ذخیره‌شده در دسترس نیستند؛ گفت‌وگوی فعلی ذخیره نمی‌شود.",
  olderMessages: "۱۲ پرسش‌وپاسخ آخر نمایش داده می‌شود؛ موارد قبلی همچنان ذخیره هستند.",
  savedHistoryUnavailable: "فهرست گفت‌وگوها موقتاً در دسترس نیست؛ پاسخ شما ذخیره شده است.",
  thinkingMode: "شیوهٔ پاسخ", standardResponse: "معمولی", thinkingResponse: "بررسی بیشتر · کندتر",
  thinkingHelp: "استدلال محلی با بودجهٔ محدود انجام می‌شود. فقط پاسخ نهایی نمایش و ذخیره می‌شود؛ این حالت، صحت اطلاعات را تضمین نمی‌کند.",
  conflictError: "در این گفت‌وگو درخواست دیگری در حال پردازش است؛ پیش از تلاش دوباره صبر کنید.",
  contextExceeded: "پرسش و زمینهٔ آن از ظرفیت مدل بیشتر است. گفت‌وگوی تازه‌ای آغاز کنید یا پرسش را کوتاه‌تر بنویسید."
});

Object.assign(translations.en, {
  newChat: "New conversation", operatorTools: "OPERATOR STARTERS",
  starterHelp: "Choose a starting point, then add your details.",
  starterServices: "Servers & services", starterNetwork: "Network & DNS",
  starterFirewall: "Firewalls & VPN", starterSecurity: "Defensive security",
  connectedEvidence: "AVAILABLE EVIDENCE",
  capabilityText: "Live: authorized Zabbix and Linux. Other devices: technical guidance only, not connected access.",
  welcomeTitle: "How can I help?",
  welcomeHelp: "Ask a technical question, or choose live monitoring to inspect your systems.",
  starterTriage: "Triage a service failure", starterTriageHelp: "Safe first checks, before changing anything.",
  starterLatency: "Investigate network latency", starterLatencyHelp: "Separate DNS, routing and application delays.",
  starterAlerts: "Review Zabbix evidence", starterAlertsHelp: "Use fresh, scoped Zabbix evidence.",
  starterSecurityHelp: "Assess suspicious activity without assuming compromise.",
  copyAnswer: "Copy answer", copyCode: "Copy code", copied: "Copied to clipboard.",
  copyFailed: "Clipboard unavailable. Select the text and copy it manually.",
  adviceNotExecution: "Advice and observations · no action executed",
  contextHelp: "General follow-ups use up to two recent turns. Live requests fetch new evidence independently.",
  contextOmitted: "The previous turn was too long for follow-up context; include the relevant detail in your next question.",
  conversationLabel: "Conversation", answerReady: "Answer ready.", elapsed: "seconds elapsed",
  blankQuestion: "Please enter a question.",
  generalModeHelp: "Technical advice and follow-ups from local model knowledge, not live device facts."
});
Object.assign(translations.en, {
  monitoringChecking: "Checking Zabbix data", monitoringReady: "Zabbix data reachable",
  monitoringUnavailable: "Zabbix data unavailable",
  deniedError: "This request is denied by application policy. Choose an authorized target or contact your administrator."
});
Object.assign(translations.fa, {
  workspaceLead: "راهنمایی فنی برای تیم‌های عملیات شبکه و امنیت؛ با جداسازی روشن دانش مدل از شواهد زنده.",
  newChat: "گفت‌وگوی تازه", operatorTools: "شروع کار اپراتور",
  starterHelp: "یک موضوع انتخاب کنید و جزئیات خود را اضافه کنید.",
  starterServices: "سرورها و سرویس‌ها", starterNetwork: "شبکه و DNS",
  starterFirewall: "فایروال و VPN", starterSecurity: "امنیت دفاعی",
  connectedEvidence: "شواهد در دسترس",
  capabilityText: "دادهٔ زنده: Zabbix و Linux مجاز. برای سایر تجهیزات، فقط راهنمایی فنی ارائه می‌شود؛ اتصال مستقیم وجود ندارد.",
  welcomeTitle: "چطور می‌توانم کمک کنم؟",
  welcomeHelp: "پرسش فنی بپرسید یا برای بررسی سامانه‌ها، پایش زنده را انتخاب کنید.",
  starterTriage: "بررسی خرابی سرویس", starterTriageHelp: "بررسی‌های ایمن اولیه، پیش از هر تغییر.",
  starterLatency: "بررسی تأخیر شبکه", starterLatencyHelp: "تفکیک تأخیر DNS، مسیر و برنامه.",
  starterAlerts: "مرور شواهد Zabbix", starterAlertsHelp: "با شاهد تازه و محدود به دامنهٔ مجاز Zabbix.",
  starterSecurityHelp: "ارزیابی فعالیت مشکوک، بدون فرضِ نفوذ قطعی.",
  copyAnswer: "کپی پاسخ", copyCode: "کپی کد", copied: "در کلیپ‌بورد کپی شد.",
  copyFailed: "کلیپ‌بورد در دسترس نیست؛ متن را انتخاب و دستی کپی کنید.",
  adviceNotExecution: "مشاوره و مشاهده · هیچ عملیاتی اجرا نشده است",
  contextHelp: "پیگیری عمومی از حداکثر دو نوبت اخیر استفاده می‌کند؛ درخواست زنده، شاهد تازه و مستقل می‌گیرد.",
  contextOmitted: "نوبت قبلی برای زمینهٔ پیگیری طولانی بود؛ جزئیات مرتبط را در پرسش بعدی بنویسید.",
  conversationLabel: "گفت‌وگو", answerReady: "پاسخ آماده است.", elapsed: "ثانیه سپری شده",
  blankQuestion: "لطفاً پرسش خود را بنویسید.",
  generalModeHelp: "مشاورهٔ فنی و پیگیری از دانش مدل محلی، نه گزارش وضعیت زندهٔ تجهیزات."
});
Object.assign(translations.fa, {
  monitoringChecking: "بررسی دسترسی به دادهٔ Zabbix", monitoringReady: "دادهٔ Zabbix در دسترس است",
  monitoringUnavailable: "دادهٔ Zabbix در دسترس نیست",
  deniedError: "سیاست برنامه این درخواست را مجاز نمی‌داند؛ میزبان مجاز انتخاب کنید یا با مدیر سامانه تماس بگیرید."
});

Object.assign(translations.en, {
  loginHeadline: "Welcome back.", loginLead: "Your infrastructure. One clear workspace.",
  welcome: "Sign in to NextOps", credentialsPrompt: "Use your organization account.",
  signIn: "Sign in", privacyNote: "Session stays in this browser tab.",
  workspaceHeadline: "Ask NextOps", savedChats: "Recent conversations",
  savedPrivacy: "Only you can see these. Avoid sharing secrets.",
  generalMode: "Chat", monitoringMode: "Live monitoring", incidentMode: "Investigate",
  questionPlaceholder: "Ask about your systems...",
  starterTriage: "Servers & services", starterLatency: "Network & DNS",
  starterAlerts: "Zabbix alerts", starterSecurity: "Security",
  askAssistant: "Send question"
});
Object.assign(translations.fa, {
  loginHeadline: "خوش آمدید.", loginLead: "زیرساخت شما، در یک محیط روشن و ساده.",
  welcome: "ورود به NextOps", credentialsPrompt: "با حساب سازمانی خود وارد شوید.",
  signIn: "ورود", privacyNote: "نشست فقط در این زبانهٔ مرورگر نگه‌داری می‌شود.",
  workspaceHeadline: "از NextOps بپرسید", savedChats: "گفت‌وگوهای اخیر",
  savedPrivacy: "فقط برای شما قابل مشاهده‌اند. اطلاعات محرمانه وارد نکنید.",
  generalMode: "گفت‌وگو", monitoringMode: "پایش زنده", incidentMode: "بررسی رخداد",
  questionPlaceholder: "دربارهٔ سامانه‌ها بپرسید...",
  starterTriage: "سرورها و سرویس‌ها", starterLatency: "شبکه و DNS",
  starterAlerts: "هشدارهای Zabbix", starterSecurity: "امنیت",
  askAssistant: "ارسال پرسش"
});

const starters = {
  en: {
    services: ["general", "How can I safely diagnose a Linux service that fails to start? Explain the first read-only checks and what their results mean."],
    network: ["general", "How can I distinguish a DNS failure from a routing or TCP connection problem? Give a short, safe diagnostic checklist."],
    firewall: ["general", "How can I diagnose a VPN connection blocked by a firewall without changing any rules? What vendor and redacted diagnostics do you need?"],
    security: ["general", "How should a SOC analyst triage repeated failed logins? Separate evidence, possible causes and safe checks; do not assume a confirmed breach."],
    triage: ["general", "How can I safely diagnose a Linux service that fails to start? Explain the first read-only checks and what their results mean."],
    latency: ["general", "How can I investigate intermittent network latency? Distinguish packet loss, DNS delay and application response time without assuming a root cause."],
    alerts: ["monitoring", "What do the current authorized Zabbix observations show? Include their source, times, scope and any stale or partial limitations."]
  },
  fa: {
    services: ["general", "چگونه سرویسی در Linux را که شروع نمی‌شود، به‌صورت ایمن عیب‌یابی کنم؟ بررسی‌های فقط‌خواندنیِ اولیه و معنی نتیجهٔ آن‌ها را توضیح بده."],
    network: ["general", "چگونه خطای DNS را از مشکل مسیریابی یا اتصال TCP تشخیص دهم؟ یک فهرست کوتاه از بررسی‌های ایمن ارائه کن."],
    firewall: ["general", "چگونه مشکل اتصال VPN را که احتمالاً به فایروال مربوط است، بدون تغییر هیچ قاعده‌ای بررسی کنم؟ به نام سازنده و چه خروجی پالایش‌شده‌ای نیاز داری؟"],
    security: ["general", "تحلیلگر SOC چگونه تلاش‌های ناموفقِ مکرر برای ورود را بررسی کند؟ شاهد، علت احتمالی و بررسی ایمن را جدا کن؛ نفوذ قطعی را فرض نکن."],
    triage: ["general", "چگونه سرویسی در Linux را که شروع نمی‌شود، به‌صورت ایمن عیب‌یابی کنم؟ بررسی‌های فقط‌خواندنیِ اولیه و معنی نتیجهٔ آن‌ها را توضیح بده."],
    latency: ["general", "چگونه تأخیر متناوب شبکه را بررسی کنم؟ افت بسته، تأخیر DNS و زمان پاسخ برنامه را جدا کن و علت قطعی را حدس نزن."],
    alerts: ["monitoring", "مشاهدات جاری و مجاز Zabbix چه چیزی نشان می‌دهند؟ منبع، زمان‌ها، دامنه و محدودیت شواهد قدیمی یا ناقص را نیز بیان کن."]
  }
};

function clearConversation() {
  window.NextOpsView?.clear();
  state.conversationId = null;
  state.pendingMessage = null;
  state.history = [];
  state.lastEvidence = null;
  byId("conversationHistory").replaceChildren();
  const fresh = resultTemplate.cloneNode(true);
  fresh.querySelectorAll("[data-i18n]").forEach(node => { node.textContent = translations[state.language][node.dataset.i18n] || node.textContent; });
  byId("resultCard").replaceWith(fresh);
  byId("conversationWelcome").classList.remove("hidden");
  byId("question").value = "";
  byId("characterCount").textContent = "0 / 4000";
  byId("assistantError").textContent = "";
  byId("copyStatus").textContent = "";
  byId("requestStatus").textContent = "";
  window.NextOpsCapabilities?.locale(state.language);
  setContextNotice(state.conversationsEnabled ? "savedContextHelp" : "contextHelp");
  byId("deleteChatButton").classList.add("hidden");
  document.querySelectorAll(".saved-chat-button").forEach(node => node.removeAttribute("aria-current"));
}

function setContextNotice(key) {
  byId("contextNotice").dataset.i18n = key;
  byId("contextNotice").textContent = translations[state.language][key];
}

function setBusy(busy) {
  window.NextOpsView?.busy(busy);
  window.NextOpsCapabilities?.busy(busy);
  byId("cancelRequest")?.classList.toggle("hidden", !busy);
  state.busy = busy;
  byId("question").readOnly = busy;
  document.querySelectorAll("#askButton, #newChatButton, .mode-choice, .locale-choice, [data-starter], #languageButton, #incidentTarget, #thinkingMode, #deleteChatButton, .saved-chat-button").forEach(node => {
    node.disabled = busy || (node.id === "incidentTarget" && !state.incidentTargets.length);
  });
  byId("askButton").toggleAttribute("aria-busy", busy);
  byId("monitoringSource").disabled = busy || !state.sourceCatalog.length;
  byId("monitoringSourceTarget").disabled = busy || !byId("monitoringSource").value;
  byId("askButton").querySelector("span").textContent = translations[state.language][busy ? "working" : "askAssistant"];
}

function archiveLastTurn() {
  const latest = byId("resultCard");
  if (latest.classList.contains("hidden")) return;
  const archived = latest.cloneNode(true);
  archived.removeAttribute("id");
  archived.querySelectorAll("[id]").forEach(node => node.removeAttribute("id"));
  byId("conversationHistory").append(archived);
  window.NextOpsView?.archive(latest, archived);
  // Bound DOM size independently of the server's durable transcript.
  while (byId("conversationHistory").children.length > 11) {
    byId("conversationHistory").firstElementChild.remove();
  }
}

function rememberGeneralTurn(question, assistant) {
  if (assistant.integrity_status !== "model_unverified" || assistant.evidence_mode !== "model_only") {
    state.history = [];
    return;
  }
  const pair = { question, answer: assistant.answer };
  if (question.length > 2000 || assistant.answer.length > 2000) {
    state.history = [];
    byId("contextNotice").dataset.i18n = "contextOmitted";
    byId("contextNotice").textContent = translations[state.language].contextOmitted;
    return;
  }
  state.history.push(pair);
  while (state.history.length > 2 || JSON.stringify(state.history).length > 6000) state.history.shift();
  byId("contextNotice").dataset.i18n = "contextHelp";
  byId("contextNotice").textContent = translations[state.language].contextHelp;
}

function appendTechnicalText(node, text) {
  // Display isolation only, never validation or rewriting of untrusted values.
  const tokens = text.split(/(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})|\b(?:\d{1,3}\.){3}\d{1,3}(?:\/\d{1,2})?\b|\b\d+(?:\.\d+)?%)/g);
  tokens.forEach((token, index) => {
    if (index % 2) {
      const value = document.createElement("bdi");
      value.dir = "ltr";
      value.textContent = token;
      node.append(value);
    } else node.append(document.createTextNode(token));
  });
}

function renderAnswer(text, locale) {
  const answer = byId("answer");
  answer.replaceChildren();
  answer.dir = locale === "fa" ? "rtl" : "ltr";
  answer.lang = locale;
  answer.dataset.rawText = text;
  // Deliberately small formatter: no HTML, URLs, images or executable Markdown.
  const parts = text.split(/(```[\s\S]*?(?:```|$))/g);
  parts.filter(Boolean).forEach(part => {
    if (part.startsWith("```")) {
      const body = part.slice(3).replace(/```$/, "");
      const firstLine = body.indexOf("\n");
      const language = firstLine >= 0 ? body.slice(0, firstLine).trim() : "";
      const codeText = firstLine >= 0 ? body.slice(firstLine + 1) : body;
      const block = document.createElement("div");
      block.className = "code-block";
      const heading = document.createElement("div");
      heading.className = "code-heading";
      const label = document.createElement("bdi");
      label.dir = "ltr";
      label.textContent = /^[\w+-]{1,24}$/.test(language) ? language : "code";
      const copy = document.createElement("button");
      copy.type = "button";
      copy.className = "quiet-button";
      copy.dataset.copyCode = "";
      copy.dataset.i18n = "copyCode";
      copy.textContent = translations[state.language].copyCode;
      heading.append(label, copy);
      const pre = document.createElement("pre");
      pre.dir = "ltr";
      const code = document.createElement("code");
      code.textContent = codeText;
      pre.append(code);
      block.append(heading, pre);
      answer.append(block);
    } else {
      const paragraph = document.createElement("p");
      part.split(/(`[^`\n]+`)/g).forEach(fragment => {
        if (fragment.startsWith("`") && fragment.endsWith("`") && fragment.length > 2) {
          const code = document.createElement("code");
          code.dir = "ltr";
          code.textContent = fragment.slice(1, -1);
          paragraph.append(code);
        } else appendTechnicalText(paragraph, fragment);
      });
      answer.append(paragraph);
    }
  });
}

function installBrandIcon() {
  byId("appIcon").href = "/assets/ocs-logo-light.jpg";
}

function applyLanguage(language) {
  state.language = language;
  window.NextOpsView?.setLocale(language);
  window.NextOpsCapabilities?.locale(language);
  try { localStorage.setItem("nextops-language", language); } catch { /* Tab-only preference. */ }
  document.documentElement.lang = language;
  document.documentElement.dir = language === "fa" ? "rtl" : "ltr";
  window.NextOpsTheme.updateControl();
  window.NextOpsMotion?.update();
  renderUsers();
  byId("copyStatus").textContent = "";
  byId("languageButton").textContent = language === "fa" ? "English" : "فارسی";
  byId("languageButton").setAttribute("aria-label", translations[language].languageToggleAria);
  document.querySelectorAll("[data-i18n]").forEach(node => {
    const value = translations[language][node.dataset.i18n];
    if (value !== undefined) node.innerHTML = value;
  });
  document.querySelectorAll("[data-i18n-placeholder]").forEach(node => {
    node.placeholder = translations[language][node.dataset.i18nPlaceholder];
  });
  document.querySelector(".mode-field .segmented-control").setAttribute("aria-label", translations[language].answerMode);
  document.querySelector(".locale-control").setAttribute("aria-label", translations[language].answerLanguage);
  document.querySelector(".status-panel").setAttribute("aria-label", translations[language].serviceStatus);
  byId("conversationFeed").setAttribute("aria-label", translations[language].conversationLabel);
  state.answerLocale = language;
  document.querySelectorAll(".locale-choice").forEach(item => {
    item.classList.toggle("active", item.dataset.locale === language);
    item.setAttribute("aria-pressed", item.dataset.locale === language ? "true" : "false");
  });
  if (state.lastEvidence) {
    if (state.lastEvidence.incident) renderIncidentEvidence(state.lastEvidence.evidence, state.lastEvidence.focus, state.lastEvidence.question);
    else renderEvidence(state.lastEvidence.evidence);
    updateEvidenceBrief();
  }
}

async function api(path, options = {}) {
  const token = state.token;
  const headers = { "Content-Type": "application/json", ...(options.headers || {}) };
  if (state.token) headers.Authorization = `Bearer ${state.token}`;
  const response = await fetch(path, { ...options, headers, cache: "no-store" });
  let body = null;
  try { body = await response.json(); } catch (_) { body = {}; }
  if (!response.ok) {
    const error = new Error(body?.error?.message_key || "request.failed");
    error.status = response.status;
    error.code = body?.error?.code || "internal_error";
    if (response.status === 401 && token && state.token === token) showLogin(translations[state.language].sessionExpired);
    throw error;
  }
  return body;
}

function showLogin(message = "") {
  window.NextOpsView?.session(null);
  window.NextOpsCapabilities?.reset();
  window.NextOpsMotion?.reset();
  byId("destinationView").classList.add("hidden");
  state.epoch += 1;
  state.token = "";
  state.actor = null; state.users = []; state.usersOffset = 0; state.usersNext = null;
  state.usersBusy = false; closeUserPassword(); byId("userCreateForm").reset();
  byId("usersList").replaceChildren(); byId("usersStatus").textContent = ""; byId("usersError").textContent = "";
  byId("usersView").classList.add("hidden"); byId("usersButton").classList.add("hidden");
  state.lastEvidence = null;
  state.conversationsEnabled = false;
  state.thinkingEnabled = false;
  state.sourceCatalog = [];
  byId("monitoringSource").replaceChildren();
  byId("monitoringSourceTarget").replaceChildren();
  byId("sourceSelectionField").classList.add("hidden");
  byId("savedChatsList").replaceChildren();
  byId("savedChatsPanel").classList.add("hidden");
  byId("thinkingField").classList.add("hidden");
  sessionStorage.removeItem("nextops-session");
  byId("loginView").classList.remove("hidden");
  byId("workspaceView").classList.add("hidden");
  byId("logoutButton").classList.add("hidden");
  byId("loginError").textContent = message;
  clearConversation();
  setBusy(false);
}

function updateEvidenceBrief() {
  if (!state.lastEvidence) return;
  const { evidence, incident, focus } = state.lastEvidence;
  const displayTime = value => new Date(value).toLocaleString(state.language === "fa" ? "fa-IR" : "en-GB", { timeZone: "UTC", timeZoneName: "short" });
  const scopeKey = incident ? ({ filesystems: "filesystemScope", file_listing: "fileScope", network: "networkScope", service: "serviceScope", network_service: "networkServiceScope" }[focus] || "incidentScope") : "monitoringScope";
  const fields = [
    ["sourceBrief", incident ? "Zabbix + Linux" : evidence.source_id ? `Zabbix · ${evidence.source_id} / ${evidence.target_id}` : "Zabbix", true],
    ...(incident ? [
      ["linuxCollected", displayTime(evidence.linux.collected_at), true],
      ["zabbixCollected", displayTime(evidence.zabbix.collected_at), true]
    ] : [["collectedBrief", displayTime(evidence.collected_at), true]]),
    ["scopeBrief", translations[state.language][scopeKey], false]
  ];
  const brief = byId("evidenceBrief");
  brief.replaceChildren();
  fields.forEach(([labelKey, value, technical]) => {
    const field = document.createElement("span");
    const label = document.createElement("small");
    label.textContent = translations[state.language][labelKey];
    const content = document.createElement(technical ? "bdi" : "strong");
    if (technical) content.dir = "ltr";
    content.textContent = value;
    field.append(label, content);
    brief.append(field);
  });
}

async function showWorkspace() {
  const identityEpoch = state.epoch;
  const actor = await api("/api/v1/me");
  if (identityEpoch !== state.epoch || !state.token) return;
  state.actor = actor;
  window.NextOpsView?.session(actor);
  byId("usersButton").classList.toggle("hidden", !actor.roles?.includes("admin"));
  byId("usersView").classList.add("hidden");
  byId("loginView").classList.add("hidden");
  byId("workspaceView").classList.remove("hidden");
  byId("logoutButton").classList.remove("hidden");
  checkAi();
  checkMonitoring();
  loadIncidentTargets();
  loadSourceCatalog();
  const epoch = state.epoch;
  try {
    const config = await api("/api/v1/conversations/config");
    if (epoch !== state.epoch) return;
    state.conversationsEnabled = config.enabled === true;
    state.thinkingEnabled = config.thinking_enabled === true;
    window.NextOpsCapabilities?.conversation(config);
    byId("savedChatsPanel").classList.toggle("hidden", !state.conversationsEnabled);
    byId("thinkingField").classList.toggle("hidden", !state.thinkingEnabled || state.answerMode !== "general");
    if (state.conversationsEnabled) {
      setContextNotice("savedContextHelp");
      await refreshSavedChats();
    }
  } catch (error) {
    if (epoch === state.epoch && error.status !== 401) setContextNotice("savedChatsUnavailable");
  }
}

async function refreshSavedChats() {
  const epoch = state.epoch;
  const conversations = await api("/api/v1/conversations");
  if (epoch !== state.epoch) return;
  byId("savedChatsList").replaceChildren();
  conversations.forEach(chat => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "saved-chat-button";
    button.textContent = chat.title;
    button.dir = "auto";
    button.disabled = state.busy;
    if (chat.conversation_id === state.conversationId) button.setAttribute("aria-current", "true");
    button.addEventListener("click", () => openSavedChat(chat.conversation_id));
    byId("savedChatsList").append(button);
  });
  byId("deleteChatButton").classList.toggle("hidden", !state.conversationId);
}

async function openSavedChat(id) {
  if (state.busy) return;
  const epoch = ++state.epoch;
  setBusy(true);
  try {
    const page = await api(`/api/v1/conversations/${id}`);
    if (epoch !== state.epoch) return;
    clearConversation();
    state.conversationId = id;
    setAnswerMode("general");
    page.messages.slice(-12).forEach(message => {
      archiveLastTurn();
      byId("askedQuestion").textContent = message.question;
      byId("askedQuestion").dir = "auto";
      renderAnswer(message.assistant.answer, message.assistant.locale);
      byId("modelId").textContent = message.assistant.model_id;
      byId("tokenCount").textContent = message.assistant.completion_tokens;
      byId("completedAt").textContent = new Date(message.assistant.completed_at).toLocaleString(state.language === "fa" ? "fa-IR" : "en-GB", { timeZone: "UTC", timeZoneName: "short" });
      byId("requestId").textContent = message.assistant.request_id;
      window.NextOpsView?.resumed(message.assistant, message.question);
      const key = message.assistant.integrity_status === "model_unverified" ? "modelIntegrityNotice" :
        message.assistant.integrity_status === "scope_redirect" ? "redirectIntegrityNotice" : "generalFallbackIntegrityNotice";
      byId("integrityNotice").dataset.i18n = key;
      byId("integrityNotice").textContent = translations[state.language][key];
      byId("resultCard").classList.remove("hidden");
      byId("conversationWelcome").classList.add("hidden");
    });
    byId("savedChatsStatus").textContent = page.before_sequence || page.messages.length > 12 ? translations[state.language].olderMessages : "";
    await refreshSavedChats();
    byId("question").focus();
  } catch (error) {
    if (epoch === state.epoch) byId("assistantError").textContent = safeRequestError(error);
  } finally {
    if (epoch === state.epoch) setBusy(false);
  }
}

byId("deleteChatButton").addEventListener("click", async () => {
  if (state.busy || !state.conversationId || !window.confirm(translations[state.language].deleteChatConfirm)) return;
  const epoch = ++state.epoch;
  setBusy(true);
  try {
    await api(`/api/v1/conversations/${state.conversationId}`, { method: "DELETE" });
    if (epoch !== state.epoch) return;
    clearConversation();
    await refreshSavedChats();
    byId("question").focus();
  } catch (error) {
    if (epoch === state.epoch) byId("assistantError").textContent = safeRequestError(error);
  } finally {
    if (epoch === state.epoch) setBusy(false);
  }
});

async function logout() {
  const token = state.token;
  showLogin(); // Remove private content immediately, before a network round trip.
  try {
    if (token) await api("/api/v1/logout", { method: "POST", headers: { Authorization: `Bearer ${token}` } });
  } catch (_) {
    // Local token removal remains fail-safe if the server is temporarily unavailable.
  }
}

function populateSourceTargets() {
  const source = state.sourceCatalog.find(item => item.source_id === byId("monitoringSource").value);
  const select = byId("monitoringSourceTarget");
  select.replaceChildren();
  (source?.targets || []).forEach(target => {
    const option = document.createElement("option");
    option.value = target.target_id;
    option.textContent = target.label;
    option.dir = "auto";
    select.append(option);
  });
  select.disabled = !source || state.busy;
  select.classList.toggle("hidden", !source);
  document.querySelector('label[for="monitoringSourceTarget"]').classList.toggle("hidden", !source);
}
async function loadSourceCatalog() {
  const epoch = state.epoch;
  const select = byId("monitoringSource");
  select.replaceChildren();
  const primary = document.createElement("option");
  primary.value = "";
  primary.dataset.i18n = "primaryOverview";
  primary.textContent = translations[state.language].primaryOverview;
  select.append(primary);
  try {
    const catalog = await api("/api/v1/monitoring/sources");
    if (epoch !== state.epoch || !state.token) return;
    state.sourceCatalog = catalog.sources || [];
    state.sourceCatalog.forEach(source => {
      const option = document.createElement("option");
      option.value = source.source_id;
      option.textContent = source.label;
      option.dir = "auto";
      select.append(option);
    });
    byId("sourceCatalogNotice").dataset.i18n = "approvedCatalogHelp";
  } catch (error) {
    if (epoch !== state.epoch || !state.token) return;
    state.sourceCatalog = [];
    byId("sourceCatalogNotice").dataset.i18n = "sourceCatalogUnavailable";
  }
  byId("sourceCatalogNotice").textContent = translations[state.language][byId("sourceCatalogNotice").dataset.i18n];
  select.disabled = state.busy;
  populateSourceTargets();
  window.NextOpsView?.catalog(state.sourceCatalog);
}
byId("monitoringSource").addEventListener("change", () => {
  populateSourceTargets();
  window.NextOpsCapabilities?.sourceSelection();
  if (!byId("monitoringSource").value) checkMonitoring();
});
byId("monitoringSourceTarget").addEventListener("change", () => window.NextOpsCapabilities?.sourceSelection());
document.addEventListener("nextops:inspect-source", event => {
  if (state.busy || !state.token) return;
  const { source_id, target_id } = event.detail || {};
  const source = state.sourceCatalog.find(item => item.source_id === source_id);
  if (!source?.targets.some(item => item.target_id === target_id)) return;
  window.NextOpsView?.navigate("ask", false);
  setAnswerMode("monitoring");
  byId("monitoringSource").value = source_id;
  populateSourceTargets();
  byId("monitoringSourceTarget").value = target_id;
  window.NextOpsCapabilities?.sourceSelection();
  document.querySelector('[data-monitoring-shortcut="problems"]').click();
});

async function loadIncidentTargets() {
  const epoch = state.epoch;
  const select = byId("incidentTarget");
  select.disabled = true;
  select.replaceChildren();
  try {
    const response = await api("/api/v1/incidents/targets");
    if (epoch !== state.epoch || !state.token) return;
    state.incidentTargets = response.targets || [];
    state.incidentTargets.forEach(targetId => {
      const option = document.createElement("option");
      option.value = targetId;
      option.textContent = targetId;
      option.dir = "ltr";
      select.append(option);
    });
    select.disabled = state.incidentTargets.length === 0;
  } catch (_) {
    state.incidentTargets = [];
  }
}

async function checkAi() {
  const epoch = state.epoch;
  const pill = byId("aiStatus");
  try {
    const ready = await api("/api/v1/assistant/ready");
    if (epoch !== state.epoch || !state.token) return;
    window.NextOpsView?.health("ai", ready);
    window.NextOpsCapabilities?.ready(ready);
    const ok = ready.state === "ready";
    const statusKey = ok ? "aiReady" : "aiUnavailable";
    pill.className = `status-pill ${ok ? "ready" : "failed"}`;
    pill.querySelector("span").dataset.i18n = statusKey;
    pill.querySelector("span").textContent = translations[state.language][statusKey];
  } catch (_) {
    if (epoch !== state.epoch || !state.token) return;
    window.NextOpsView?.health("ai", null);
    window.NextOpsCapabilities?.ready(null);
    pill.className = "status-pill failed";
    pill.querySelector("span").dataset.i18n = "aiUnavailable";
    pill.querySelector("span").textContent = translations[state.language].aiUnavailable;
  }
}

async function checkMonitoring() {
  const epoch = state.epoch;
  const pill = byId("monitoringStatus");
  try {
    const summary = await api("/api/v1/monitoring/summary");
    if (epoch !== state.epoch || !state.token || byId("monitoringSource").value) return;
    window.NextOpsView?.health("connector", summary);
    const ok = summary.source === "zabbix";
    const statusKey = ok ? "monitoringReady" : "monitoringUnavailable";
    pill.className = `status-pill ${ok ? "ready" : "failed"}`;
    pill.querySelector("span").dataset.i18n = statusKey;
    pill.querySelector("span").textContent = translations[state.language][statusKey];
  } catch (_) {
    if (epoch !== state.epoch || !state.token || byId("monitoringSource").value) return;
    window.NextOpsView?.health("connector", null);
    pill.className = "status-pill failed";
    pill.querySelector("span").dataset.i18n = "monitoringUnavailable";
    pill.querySelector("span").textContent = translations[state.language].monitoringUnavailable;
  }
}

function renderEvidence(evidence) {
  const locale = state.language === "fa" ? "fa-IR" : "en-GB";
  byId("evidenceSource").textContent = `Zabbix ${evidence.source_version}${evidence.source_id ? ` · ${evidence.source_id} / ${evidence.target_id}` : ""}`;
  byId("evidenceHost").textContent = evidence.host;
  byId("evidenceCollected").textContent = new Date(evidence.collected_at).toLocaleString(locale, { timeZone: "UTC", timeZoneName: "short" });
  byId("problemCount").textContent = evidence.active_problems.length;
  byId("evidenceCoverage").textContent = translations[state.language][evidence.is_partial ? "partial" : "complete"];
  byId("evidenceCoverage").title = evidence.partial_reasons.join(", ");
  const list = byId("metricList");
  list.classList.remove("hidden");
  list.replaceChildren();
  byId("incidentDetail").classList.add("hidden");
  byId("incidentDetail").replaceChildren();
  evidence.metrics.forEach(metric => {
    const item = document.createElement("div");
    item.className = "metric-item";
    const title = document.createElement("strong");
    title.textContent = metric.name;
    const value = document.createElement("span");
    value.textContent = `${metric.value}${metric.units ? ` ${metric.units}` : ""}`;
    const time = document.createElement("small");
    time.textContent = `${new Date(metric.measured_at).toLocaleString(locale, { timeZone: "UTC", timeZoneName: "short" })}${metric.stale ? ` · ${translations[state.language].stale}` : ""}`;
    item.append(title, value, time);
    list.append(item);
  });
}

function formatBytes(value) {
  const gibibytes = Number(value) / (1024 ** 3);
  return `${new Intl.NumberFormat(state.language === "fa" ? "fa-IR" : "en-GB", { maximumFractionDigits: 1 }).format(gibibytes)} GiB`;
}

function formatDuration(seconds) {
  const hours = Math.floor(Number(seconds) / 3600);
  const days = Math.floor(hours / 24);
  if (state.language === "fa") return days > 0 ? `${days} روز و ${hours % 24} ساعت` : `${hours} ساعت`;
  return days > 0 ? `${days}d ${hours % 24}h` : `${hours}h`;
}

function evidenceSection(titleText, rows) {
  const section = document.createElement("section");
  section.className = "incident-section";
  const title = document.createElement("h3");
  title.textContent = titleText;
  const list = document.createElement("div");
  list.className = "incident-list";
  if (rows.length === 0) {
    const empty = document.createElement("p");
    empty.className = "empty-evidence";
    empty.textContent = translations[state.language].noEntries;
    list.append(empty);
  } else {
    rows.forEach(row => {
      const item = document.createElement("div");
      item.className = "incident-row";
      const label = document.createElement("strong");
      label.textContent = row.label;
      const value = document.createElement("span");
      value.textContent = row.value;
      if (row.detail) {
        const detail = document.createElement("small");
        detail.textContent = row.detail;
        item.append(label, value, detail);
      } else {
        item.append(label, value);
      }
      list.append(item);
    });
  }
  section.append(title, list);
  return section;
}

function renderIncidentEvidence(evidence, focus = "overview", question = "") {
  const locale = state.language === "fa" ? "fa-IR" : "en-GB";
  renderEvidence(evidence.zabbix.summary);
  byId("evidenceSource").textContent = `Zabbix ${evidence.zabbix.source_version} + Linux ${evidence.linux.collector_version}`;
  byId("evidenceHost").textContent = `${evidence.zabbix.host} · ${evidence.linux.hostname}`;
  byId("evidenceCollected").textContent = new Date(evidence.linux.collected_at).toLocaleString(locale, { timeZone: "UTC", timeZoneName: "short" });
  byId("evidenceCoverage").textContent = translations[state.language][evidence.is_partial ? "partial" : "complete"];
  byId("evidenceCoverage").title = evidence.partial_reasons.join(", ");

  const detail = byId("incidentDetail");
  const stats = document.createElement("div");
  stats.className = "incident-stats";
  [
    [translations[state.language].systemLoad, `${evidence.linux.load_1m} / ${evidence.linux.load_5m} / ${evidence.linux.load_15m}`],
    [translations[state.language].memoryAvailable, `${formatBytes(evidence.linux.memory_available_bytes)} / ${formatBytes(evidence.linux.memory_total_bytes)}`],
    [translations[state.language].uptime, formatDuration(evidence.linux.uptime_seconds)],
    [translations[state.language].zabbixTimeline, `${evidence.zabbix.history.length} ${translations[state.language].historyPoints} · ${evidence.zabbix.events.length} ${translations[state.language].eventRecords}`]
  ].forEach(([labelText, valueText]) => {
    const item = document.createElement("span");
    const label = document.createElement("small");
    label.textContent = labelText;
    const value = document.createElement("strong");
    value.textContent = valueText;
    item.append(label, value);
    stats.append(item);
  });

  const sections = document.createElement("div");
  sections.className = "incident-sections";
  sections.append(
    evidenceSection(translations[state.language].filesystems, evidence.linux.filesystems.map(filesystem => ({
      label: filesystem.path,
      value: `${filesystem.used_percent}%`,
      detail: `${formatBytes(filesystem.available_bytes)} ${translations[state.language].available}`
    }))),
    evidenceSection(translations[state.language].services, evidence.linux.services.map(service => ({
      label: service.unit,
      value: `${service.active_state} / ${service.sub_state}`,
      detail: service.load_state
    }))),
    evidenceSection(translations[state.language].recentEvents, evidence.zabbix.events.map(event => ({
      label: event.name,
      value: event.state,
      detail: new Date(event.occurred_at).toLocaleString(locale, { timeZone: "UTC", timeZoneName: "short" })
    }))),
    evidenceSection(translations[state.language].criticalJournal, evidence.linux.journal.map(entry => ({
      label: entry.unit,
      value: entry.message,
      detail: new Date(entry.observed_at).toLocaleString(locale, { timeZone: "UTC", timeZoneName: "short" })
    })))
  );
  const networkSections = document.createElement("div");
  networkSections.className = "incident-sections";
  networkSections.append(
    evidenceSection(translations[state.language].configuredResolvers, evidence.linux.nameservers.map(value => ({ label: value, value: "" }))),
    evidenceSection(translations[state.language].recordedRoutes, evidence.linux.routes.map(route => ({ label: route.destination, value: route.gateway, detail: route.interface }))),
    evidenceSection(translations[state.language].listeningSockets, evidence.linux.listening_sockets.map(socket => ({ label: `${socket.address}:${socket.port}`, value: socket.family })))
  );
  if (focus === "overview") {
    detail.replaceChildren(stats, sections, networkSections);
  } else {
    const complete = document.createElement("details");
    complete.className = "complete-evidence";
    const summary = document.createElement("summary");
    summary.dataset.i18n = "showCompleteEvidence";
    summary.textContent = translations[state.language].showCompleteEvidence;
    const allMetrics = byId("metricList").cloneNode(true);
    allMetrics.removeAttribute("id");
    complete.append(summary, allMetrics, stats, sections, networkSections);
    const focused = focus === "file_listing" ? document.createElement("p") : document.createElement("div");
    if (focus === "file_listing") {
      focused.className = "empty-evidence";
      focused.dataset.i18n = "fileListingNotCollected";
      focused.textContent = translations[state.language].fileListingNotCollected;
    } else if (focus === "filesystems") {
      focused.append(sections.children[0].cloneNode(true));
    } else if (focus === "host_status") {
      const hostStats = stats.cloneNode(true);
      hostStats.lastElementChild.remove(); // Zabbix history may belong to a different host.
      focused.append(hostStats, sections.children[1].cloneNode(true));
    } else {
      focused.className = "incident-sections";
      if (focus === "service" || focus === "network_service") {
        const namedUnits = window.NextOpsView.namedUnits(question);
        const selectedServices = namedUnits.length
          ? evidence.linux.services.filter(item => namedUnits.includes(item.unit.toLocaleLowerCase("en-US")))
          : evidence.linux.services;
        focused.append(evidenceSection(translations[state.language].services, selectedServices.map(service => ({
          label: service.unit,
          value: `${service.active_state} / ${service.sub_state}`,
          detail: service.load_state
        }))));
        if (/\b(?:journal|logs?)\b|ژورنال|لاگ|گزارش/i.test(question)) {
          const selectedJournal = namedUnits.length
            ? evidence.linux.journal.filter(item => namedUnits.includes(item.unit.toLocaleLowerCase("en-US")))
            : evidence.linux.journal;
          focused.append(evidenceSection(translations[state.language].criticalJournal, selectedJournal.map(entry => ({
            label: entry.unit,
            value: entry.message,
            detail: new Date(entry.observed_at).toLocaleString(locale, { timeZone: "UTC", timeZoneName: "short" })
          }))));
        }
      }
      if (focus === "network" || focus === "network_service") {
        const requested = window.NextOpsView.networkGroups(question);
        const showAll = !requested.some(Boolean);
        networkSections.querySelectorAll(":scope > section").forEach((section, index) => {
          if (showAll || requested[index]) focused.append(section.cloneNode(true));
        });
      }
    }
    detail.replaceChildren(focused, complete);
    byId("metricList").classList.add("hidden");
  }
  if (evidence.partial_reasons.length > 0) {
    const warning = document.createElement("p");
    warning.className = "partial-warning";
    warning.textContent = `${translations[state.language].partialReasons}: ${evidence.partial_reasons.join(", ")}`;
    detail.append(warning);
  }
  detail.classList.remove("hidden");
}

function safeRequestError(error) {
  if (error.message === "inference.context_exceeded") return translations[state.language].contextExceeded;
  if (error.message === "incident.target_question_mismatch") return translations[state.language].targetMismatchError;
  if (error.code === "conflict") return translations[state.language].conflictError;
  const keyByCode = {
    timeout: "timeoutError",
    overloaded: "overloadedError",
    dependency_unavailable: "dependencyError",
    forbidden: "deniedError"
  };
  return translations[state.language][keyByCode[error.code] || "genericError"];
}

function requestedHostStatus(question) {
  // Intent only: the authenticated target list and server policy remain authoritative.
  if (!/\b(?:status|state|health|current|latest|now)\b|وضعیت|سلامت|فعلی|آخرین|الان/i.test(question)) return null;
  if (/\b(?:why|explain|mean(?:ing|s)?|compare|difference|how)\b|چرا|توضیح|معنی|معنا|مقایسه|تفاوت|چطور|چگونه/i.test(question)) return null;
  if (/\b(?:cpu|ram|memory|disk|file(?:s|systems?)?|network|dns|ports?|logs?|journal|services?)\b|پردازنده|حافظه|دیسک|فایل|شبکه|پورت|لاگ|ژورنال|سرویس/i.test(question)) return null;
  const aliases = { ai: "ai|هوش\\s*مصنوعی", app: "app|application|برنامه", connector: "connectors?|کانکتور|اتصال", zabbix: "zabbix|زبیکس" };
  const roles = Object.entries(aliases).filter(([role, names]) => new RegExp(
    `(?<![\\p{L}\\p{N}_@.-])(?:nextops-${role}(?![\\p{L}\\p{N}_@.-])|(?:server|host|vm|سرور|میزبان)\\s+(?:${names})|(?:${names})\\s+(?:server|host|vm|سرور|میزبان))(?![\\p{L}\\p{N}_-])`, "iu"
  ).test(question));
  return roles.length === 1 ? roles[0][0] : null;
}

function setAnswerMode(mode) {
  if (state.answerMode !== mode) state.history = [];
  state.answerMode = mode;
  document.querySelectorAll(".mode-choice").forEach(item => {
    item.classList.toggle("active", item.dataset.mode === mode);
    item.setAttribute("aria-pressed", item.dataset.mode === mode ? "true" : "false");
  });
  const helpKey = mode === "incident" ? "incidentModeHelp" : mode === "monitoring" ? "monitoringModeHelp" : "generalModeHelp";
  byId("modeHelp").dataset.i18n = helpKey;
  byId("modeHelp").textContent = translations[state.language][helpKey];
  byId("incidentTargetField").classList.toggle("hidden", mode !== "incident");
  byId("sourceSelectionField").classList.toggle("hidden", mode !== "monitoring");
  byId("thinkingField").classList.toggle("hidden", !state.thinkingEnabled || mode !== "general");
}

byId("languageButton").addEventListener("click", () => applyLanguage(state.language === "en" ? "fa" : "en"));
byId("logoutButton").addEventListener("click", logout);
byId("newChatButton").addEventListener("click", () => {
  if (state.busy) return;
  state.epoch += 1;
  clearConversation();
  byId("question").focus();
});
document.querySelectorAll("[data-starter]").forEach(button => button.addEventListener("click", () => {
  if (state.busy) return;
  const [mode, question] = starters[state.answerLocale][button.dataset.starter];
  setAnswerMode(mode);
  byId("question").value = question;
  byId("characterCount").textContent = `${question.length} / 4000`;
  byId("question").focus();
}));
byId("conversationFeed").addEventListener("click", async event => {
  const button = event.target.closest("[data-copy-answer], [data-copy-code]");
  if (!button) return;
  const text = button.hasAttribute("data-copy-code")
    ? button.closest(".code-block").querySelector("code").textContent
    : button.closest(".conversation-turn").querySelector(".answer").dataset.rawText;
  try {
    await navigator.clipboard.writeText(text);
    byId("copyStatus").textContent = translations[state.language].copied;
  } catch (_) {
    byId("copyStatus").textContent = translations[state.language].copyFailed;
  }
});
byId("loginForm").addEventListener("submit", async event => {
  event.preventDefault();
  const button = event.currentTarget.querySelector("button[type=submit]");
  byId("loginError").textContent = "";
  button.disabled = true;
  button.setAttribute("aria-busy", "true");
  try {
    const result = await api("/api/v1/login", { method: "POST", body: JSON.stringify({ username: byId("username").value, password: byId("password").value }) });
    state.token = result.session.access_token;
    sessionStorage.setItem("nextops-session", state.token);
    byId("password").value = "";
    await showWorkspace();
  } catch (error) {
    byId("loginError").textContent = error.status === 401 || error.status === 422
      ? translations[state.language].invalidLogin
      : window.NextOpsView.t(error.status === 429 ? "loginRate" : "loginService");
  } finally {
    button.disabled = false;
    button.removeAttribute("aria-busy");
  }
});

document.querySelectorAll(".locale-choice").forEach(button => button.addEventListener("click", () => {
  document.querySelectorAll(".locale-choice").forEach(item => {
    item.classList.remove("active");
    item.setAttribute("aria-pressed", "false");
  });
  button.classList.add("active");
  button.setAttribute("aria-pressed", "true");
  state.answerLocale = button.dataset.locale;
}));
document.querySelectorAll(".mode-choice").forEach(button => button.addEventListener("click", () => {
  setAnswerMode(button.dataset.mode);
}));
byId("question").addEventListener("input", event => { byId("characterCount").textContent = `${event.target.value.length} / 4000`; });
byId("question").addEventListener("keydown", event => {
  if (event.key === "Enter" && !event.shiftKey && !event.isComposing && event.keyCode !== 229) {
    event.preventDefault();
    if (!byId("askButton").disabled) byId("assistantForm").requestSubmit();
  }
});
let activeRequest = null;
const cancelRequest = document.createElement("button");
cancelRequest.id = "cancelRequest";
cancelRequest.type = "button";
cancelRequest.className = "quiet-button hidden";
cancelRequest.dataset.ui = "cancelWait";
cancelRequest.textContent = window.NextOpsView.t("cancelWait");
cancelRequest.addEventListener("click", () => activeRequest?.abort());
byId("assistantForm").querySelector(".prompt-footer").append(cancelRequest);

byId("assistantForm").addEventListener("submit", async event => {
  event.preventDefault();
  if (state.busy) return;
  const errorNode = byId("assistantError");
  errorNode.textContent = "";
  const question = byId("question").value;
  if (!question.trim()) { errorNode.textContent = translations[state.language].blankQuestion; return; }
  byId("composerOptions").open = false;
  const namedTarget = requestedHostStatus(question);
  if (namedTarget && state.incidentTargets.includes(namedTarget) && !(state.answerMode === "monitoring" && byId("monitoringSource").value)) {
    byId("incidentTarget").value = namedTarget;
    setAnswerMode("incident");
  }
  const epoch = state.epoch;
  setBusy(true);
  const started = performance.now();
  const requestController = new AbortController();
  activeRequest = requestController;
  byId("requestStatus").textContent = namedTarget && state.answerMode === "incident"
    ? `${translations[state.language].checkingNamedTarget} ${byId("incidentTarget").value}…`
    : translations[state.language].working;
  const clock = document.createElement("span");
  clock.setAttribute("aria-hidden", "true");
  byId("requestStatus").append(clock);
  const timer = setInterval(() => { clock.textContent = ` · ${Math.floor((performance.now() - started) / 1000)} ${translations[state.language].elapsed}`; }, 1000);
  try {
    const monitoring = state.answerMode === "monitoring";
    const incident = state.answerMode === "incident";
    if (incident && !byId("incidentTarget").value) throw new Error("incident.target_missing");
    const saved = !incident && !monitoring && state.conversationsEnabled;
    let path = incident ? "/api/v1/incidents/investigate" : monitoring ? "/api/v1/investigate" : "/api/v1/assistant/generate";
    let payload = { locale: state.answerLocale, question, max_output_tokens: 384 };
    if (monitoring && byId("monitoringSource").value) {
      if (!byId("monitoringSourceTarget").value) throw new Error(translations[state.language].sourceTargetRequired);
      payload.source_id = byId("monitoringSource").value;
      payload.target_id = byId("monitoringSourceTarget").value;
      path = "/api/v1/monitoring/investigate";
    }
    if (incident) payload.target_id = byId("incidentTarget").value;
    if (!monitoring && !incident && !saved && state.history.length) payload.history = state.history;
    if (saved) {
      if (!state.conversationId) {
        const chat = await api("/api/v1/conversations", { method: "POST", body: JSON.stringify({ locale: state.answerLocale }) });
        if (epoch !== state.epoch) return;
        state.conversationId = chat.conversation_id;
      }
      const thinking = state.thinkingEnabled && byId("thinkingMode").value === "thinking";
      const previous = state.pendingMessage;
      payload = previous && previous.question === question && previous.locale === state.answerLocale && previous.thinking === thinking
        ? previous : { request_id: crypto.randomUUID(), locale: state.answerLocale, question, thinking };
      state.pendingMessage = payload;
      path = `/api/v1/conversations/${state.conversationId}/messages`;
    }
    const result = await api(path, { method: "POST", body: JSON.stringify(payload), signal: requestController.signal });
    if (epoch !== state.epoch) return; // A late result must not resurrect a signed-out session.
    const evidenceBacked = monitoring || incident;
    const assistant = saved ? result.message.assistant : evidenceBacked ? result.assistant : result;
    archiveLastTurn();
    byId("askedQuestion").textContent = payload.question;
    byId("askedQuestion").dir = "auto";
    renderAnswer(assistant.answer, assistant.locale);
    byId("modelId").textContent = assistant.model_id;
    byId("tokenCount").textContent = assistant.completion_tokens;
    byId("completedAt").textContent = new Date(assistant.completed_at).toLocaleString(state.language === "fa" ? "fa-IR" : "en-GB", { timeZone: "UTC", timeZoneName: "short" });
    byId("requestId").textContent = assistant.request_id;
    const integrityKeys = {
      model_unverified: "modelIntegrityNotice",
      evidence_bounded: "evidenceIntegrityNotice",
      deterministic_fallback: "fallbackIntegrityNotice",
      deterministic_focus: "focusedIntegrityNotice",
      scope_redirect: "redirectIntegrityNotice"
    };
    let integrityKey = integrityKeys[assistant.integrity_status] || (evidenceBacked ? "unknownIntegrityNotice" : "modelIntegrityNotice");
    if (!evidenceBacked && assistant.integrity_status === "deterministic_fallback") integrityKey = "generalFallbackIntegrityNotice";
    if (assistant.limitations?.includes("host_inventory_unavailable")) integrityKey = "hostInventoryLimitNotice";
    if (assistant.limitations?.includes("requested_target_not_in_evidence")) integrityKey = "targetLimitNotice";
    if (assistant.limitations?.includes("file_listing_unavailable")) integrityKey = "fileLimitNotice";
    byId("integrityNotice").dataset.i18n = integrityKey;
    byId("integrityNotice").textContent = translations[state.language][integrityKey];
    byId("integrityNotice").classList.toggle("fallback", ["deterministic_fallback", "deterministic_focus"].includes(assistant.integrity_status));
    const titleKey = evidenceBacked ? "responseTitle" : "generalResponseTitle";
    const badgeKey = incident ? "incidentEvidenceBadge" : monitoring ? "liveEvidenceBadge" : "modelOnlyBadge";
    byId("responseTitle").dataset.i18n = titleKey;
    byId("responseTitle").textContent = translations[state.language][titleKey];
    byId("evidenceBadge").dataset.i18n = badgeKey;
    byId("evidenceBadge").textContent = translations[state.language][badgeKey];
    byId("evidenceBadge").classList.toggle("live", evidenceBacked);
    byId("evidencePanel").classList.toggle("hidden", !evidenceBacked);
    byId("evidenceDetails").open = false;
    document.querySelectorAll(".monitoring-meta").forEach(node => node.classList.toggle("hidden", !evidenceBacked));
    if (evidenceBacked) {
      if (incident) renderIncidentEvidence(result.evidence, result.answer_focus || "overview", question);
      else renderEvidence(result.evidence);
      if (monitoring && payload.source_id) {
        window.NextOpsCapabilities?.sourceHealth("sourceReady");
        window.NextOpsView?.health("connector", result.evidence);
      }
      state.lastEvidence = { evidence: result.evidence, incident, focus: result.answer_focus || "overview", question };
      updateEvidenceBrief();
      byId("evidenceBrief").classList.remove("hidden");
      byId("runId").textContent = result.run_id;
      byId("runId").title = result.run_id;
      byId("evidenceReference").textContent = result.evidence_reference;
      byId("evidenceReference").title = `${result.evidence_reference} · sha256:${result.evidence_sha256}`;
      byId("auditEventId").textContent = result.audit_event_id;
      byId("auditEventId").title = result.audit_event_id;
    } else {
      state.lastEvidence = null;
      byId("evidenceBrief").classList.add("hidden");
      if (saved) {
        state.pendingMessage = null;
        setContextNotice(result.message.context_omitted ? "savedContextOmitted" : "savedContextHelp");
        try { await refreshSavedChats(); }
        catch (error) { if (error.status !== 401) byId("savedChatsStatus").textContent = translations[state.language].savedHistoryUnavailable; }
        if (epoch !== state.epoch) return;
      } else rememberGeneralTurn(payload.question, assistant);
    }
    window.NextOpsView?.render(assistant, evidenceBacked ? result : null, payload.question, incident, performance.now() - started);
    window.NextOpsCapabilities?.locale(state.language);
    byId("conversationWelcome").classList.add("hidden");
    byId("resultCard").classList.remove("hidden");
    byId("question").value = "";
    byId("characterCount").textContent = "0 / 4000";
    byId("requestStatus").textContent = translations[state.language].answerReady;
    const focus = document.activeElement;
    if ([byId("question"), byId("askButton"), document.body].includes(focus)) {
      byId("resultCard").tabIndex = -1;
      byId("resultCard").focus({ preventScroll: true });
      byId("resultCard").scrollIntoView({ behavior: "instant", block: "start" });
    }
  } catch (error) {
    if (epoch !== state.epoch) return;
    byId("requestStatus").textContent = "";
    state.history = []; // Do not resolve a later follow-up against a failed request.
    if (error.status === 401) showLogin(translations[state.language].sessionExpired);
    else if (error.message === "incident.target_missing") errorNode.textContent = translations[state.language].noIncidentTargets;
    else errorNode.textContent = error.name === "AbortError" ? window.NextOpsView.t("cancelNotice") : safeRequestError(error);
    if (state.answerMode === "monitoring" && byId("monitoringSource").value && error.name !== "AbortError" && error.status !== 401) {
      window.NextOpsCapabilities?.sourceHealth("sourceFailed");
      window.NextOpsView?.health("source-selection", null);
    }
    window.NextOpsView?.failed();
  } finally {
    if (activeRequest === requestController) activeRequest = null;
    clearInterval(timer);
    if (epoch === state.epoch) setBusy(false);
  }
});

Object.assign(translations.en, {
  unknownIntegrityNotice: "Response integrity was not reported; evidence alone does not prove answer accuracy.",
  aiReady: "Local CPU ready",
  companyName: "Omid Computer Services",
  loginHeadline: "Welcome back.",
  loginLead: "Your infrastructure. One clear workspace.",
  credentialsPrompt: "Use your organization account.",
  workspaceHeadline: "Ask NextOps"
});
Object.assign(translations.fa, {
  unknownIntegrityNotice: "وضعیت کنترل پاسخ گزارش نشده است؛ شاهد به‌تنهایی درستی پاسخ را اثبات نمی‌کند.",
  aiReady: "CPU محلی آماده است",
  companyName: "شرکت رایانه خدمات امید",
  loginHeadline: "خوش آمدید.",
  loginLead: "زیرساخت شما، در یک محیط روشن و ساده.",
  credentialsPrompt: "با حساب سازمانی خود وارد شوید.",
  workspaceHeadline: "از NextOps بپرسید"
});
applyLanguage(state.language);
installBrandIcon();
setAnswerMode(state.answerMode);
if (state.token) showWorkspace().catch(() => showLogin(translations[state.language].sessionExpired));
