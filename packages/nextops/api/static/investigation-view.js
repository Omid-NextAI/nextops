/* Presentation adapter only. Application policy and backend contracts remain authoritative. */
(() => {
  "use strict";
  const el = id => document.getElementById(id);
  const copy = {
    en: {
      investigationOptions:"Investigation options", mainNavigation:"Main navigation", conversation:"Conversation", serviceStatus:"Service status", evidenceDetails:"Evidence details",
      overview:"Overview", ask:"Ask NextOps", investigations:"Investigations", infrastructure:"Infrastructure", knowledge:"Knowledge", connectors:"Connectors", settings:"Settings", support:"Help & support",
      productLine:"by OCS", privateWorkspace:"Private workspace", search:"Search conversations and evidence…", environment:"Authorized environment", searchTitle:"Search this workspace", searchLabel:"Conversation titles and collected evidence", searchScope:"Search is local to this page. It does not query devices or execute actions.", noMatches:"No matching content on this page.",
      newInvestigation:"New conversation", notStarted:"Not started", noEvidence:"No evidence collected", evaluation:"Controlled evaluation", readyToAsk:"Ready to ask", activeAlerts:"Active Alerts", affectedHosts:"Affected Hosts", investigationStatus:"Investigation Status", connectorHealth:"Connector Health", notAvailable:"Not available", completed:"Completed", failed:"Request failed", collecting:"Request in progress", reachable:"API reachable", unavailable:"Unavailable", engineUnknown:"Monitoring-engine health is not established.", scopeCount:"Collected sample · not an estate-wide total", noSeries:"Historical comparison not available", noAffected:"Affected-host inventory is not provided",
      monitoringSummary:"Monitoring summary", evidence:"Evidence", raw:"Raw data", related:"Related", context:"Context", visualize:"Visualize", reviewEvidence:"Review evidence", nextQuestion:"Ask a follow-up", copyQuestion:"Copy question", backInvestigation:"Back to investigation", executionTrace:"Request details", noTrace:"No completed request yet. Private model reasoning is not displayed.", evidenceBoundary:"Evidence boundary", evidenceBoundaryHelp:"An observation is not a cause. Review freshness, scope and missing data before drawing conclusions.",
      observedChange:"Observed change", hostsFinding:"Affected hosts", possibleExplanation:"Possible explanation", nextChecks:"Suggested next checks", noChange:"No structured change or baseline was returned. See the recorded observations below.", noHypothesis:"A structured hypothesis was not returned. The answer above is not proof of a cause.", noChecks:"No structured next-check list was returned. Ask a specific follow-up; no action executes here.", scopedHost:"Evidence collected for", noLive:"General model knowledge · no live infrastructure evidence", noSelected:"No evidence selected", selectEvidence:"Select a numbered observation to inspect its source, time and scope.", source:"Source", observed:"Observed", collected:"Collected", host:"Host", metric:"Metric", value:"Value", threshold:"Threshold", severity:"Severity", freshness:"Freshness", scope:"Authorized scope", notReported:"Not reported", fresh:"Not marked stale", stale:"Stale", partial:"Partial", missing:"Missing", older:"Collection is older than five minutes", rawNotice:"Allowlisted diagnostic fields only", copyRaw:"Copy raw data", copied:"Copied", copyFailed:"Copy unavailable; select and copy the text.", contextHelp:"This observation belongs to the current authorized response. It does not establish causality or permission to mutate.", noChart:"No compatible time series was returned for this observation.", noRelated:"No other observation for this host is available in this response.", noCapability:"This destination is not implemented in the current controlled release. No additional access or integration is implied.", catalogHelp:"Deployment-approved catalogue; approval is not a health check.", knowledgeHelp:"Retrieval from local documents is not connected. General answers use model knowledge, not an invented knowledge base.", settingsHelp:"Theme and interface language are local preferences. Operational configuration is not editable here.", supportHelp:"Contact your organization’s NextOps administrator. This panel has no external support connection.",
      evidenceCollected:"Evidence collected", answerGenerated:"Answer completed", auditRecorded:"Audit record returned", queue:"Reported queue", clientTime:"Browser round trip", cancelWait:"Stop waiting", cancelNotice:"Stopped waiting in this browser. The server may still complete the read-only request; this does not prove remote cancellation. Retry a saved message with the same request identifier.",
      signalGate:"Omid Signal Gate · a decorative network abstraction", pauseMotion:"Pause motion", resumeMotion:"Resume motion", staticMotion:"Static scene · reduced motion", loginBoundary:"Local identity. CPU-only inference. No cloud AI fallback.", showPassword:"Show password", hidePassword:"Hide password", localModel:"Local CPU model", newChat:"New conversation", freshResponse:"Response observations", reference:"Evidence reference", noTraceSaved:"Saved answer · no new execution", attachmentUnavailable:"Attachments are not supported by the current API.",
      navOpen:"Open navigation", navClose:"Close navigation", evidencePrevious:"Previous evidence", evidenceNext:"Next evidence", evidenceClose:"Close evidence", requestDetails:"Request details", accountMenu:"Account menu", closeSearch:"Close search", loginService:"The authentication service is unavailable. Try again later.", loginRate:"Too many sign-in attempts. Wait before trying again.",
      selectedResponse:"Selected response observations", archivedResponse:"Archived response observations · no new collection", selectedContextHelp:"This observation belongs to the selected authorized response. It does not establish causality or permission to mutate."
    },
    fa: {
      investigationOptions:"گزینه‌های بررسی", mainNavigation:"پیمایش اصلی", conversation:"گفت‌وگو", serviceStatus:"وضعیت خدمات", evidenceDetails:"جزئیات شاهد",
      overview:"نمای کلی", ask:"از NextOps بپرسید", investigations:"بررسی رخدادها", infrastructure:"زیرساخت", knowledge:"دانش", connectors:"اتصال‌دهنده‌ها", settings:"تنظیمات", support:"راهنما و پشتیبانی",
      productLine:"از شرکت رایانه خدمات امید", privateWorkspace:"محیط اختصاصی", search:"جست‌وجوی گفتگوها و شواهد…", environment:"محیط مجاز", searchTitle:"جست‌وجو در این محیط", searchLabel:"عنوان گفتگوها و شواهد گردآوری‌شده", searchScope:"جست‌وجو فقط در همین صفحه است؛ به تجهیزات درخواست نمی‌فرستد و عملیاتی اجرا نمی‌کند.", noMatches:"موردی در محتوای این صفحه یافت نشد.",
      newInvestigation:"گفت‌وگوی تازه", notStarted:"هنوز آغاز نشده", noEvidence:"شاهدی گردآوری نشده", evaluation:"ارزیابی کنترل‌شده", readyToAsk:"آمادهٔ دریافت پرسش", activeAlerts:"هشدارهای فعال", affectedHosts:"میزبان‌های متأثر", investigationStatus:"وضعیت بررسی", connectorHealth:"سلامت اتصال‌دهنده", notAvailable:"در دسترس نیست", completed:"پاسخ آماده است", failed:"درخواست ناموفق", collecting:"درخواست در حال پردازش", reachable:"API در دسترس است", unavailable:"در دسترس نیست", engineUnknown:"سلامت موتور پایش اثبات نشده است.", scopeCount:"نمونهٔ گردآوری‌شده؛ نه مجموع کل زیرساخت", noSeries:"مقایسه با سابقه در دسترس نیست", noAffected:"فهرست میزبان‌های متأثر ارائه نشده است",
      monitoringSummary:"خلاصهٔ پایش", evidence:"شواهد", raw:"دادهٔ خام", related:"مرتبط", context:"زمینه", visualize:"نمودار", reviewEvidence:"بررسی شواهد", nextQuestion:"پرسش پیگیری", copyQuestion:"کپی پرسش", backInvestigation:"بازگشت به بررسی", executionTrace:"جزئیات درخواست", noTrace:"هنوز درخواستی کامل نشده است. استدلال خصوصی مدل نمایش داده نمی‌شود.", evidenceBoundary:"حدود اعتبار شواهد", evidenceBoundaryHelp:"مشاهده به‌معنی علت نیست. پیش از نتیجه‌گیری، تازگی، دامنه و داده‌های غایب را بررسی کنید.",
      observedChange:"تغییر مشاهده‌شده", hostsFinding:"میزبان‌های متأثر", possibleExplanation:"توضیح احتمالی", nextChecks:"بررسی‌های پیشنهادی", noChange:"تغییر یا خط مبنای ساختاریافته ارائه نشده است. مشاهدات ثبت‌شده در پایین آمده‌اند.", noHypothesis:"فرضیهٔ ساختاریافته ارائه نشده است. پاسخ بالا علت قطعی را اثبات نمی‌کند.", noChecks:"فهرست ساختاریافتهٔ بررسی بعدی ارائه نشده است. پرسش مشخصی بپرسید؛ اینجا عملیاتی اجرا نمی‌شود.", scopedHost:"شاهد گردآوری‌شده برای", noLive:"دانش عمومی مدل؛ بدون شاهد زندهٔ زیرساخت", noSelected:"شاهدی انتخاب نشده", selectEvidence:"مشاهدهٔ شماره‌دار را انتخاب کنید تا منبع، زمان و دامنهٔ آن نمایش داده شود.", source:"منبع", observed:"زمان مشاهده", collected:"زمان گردآوری", host:"میزبان", metric:"سنجه", value:"مقدار", threshold:"آستانه", severity:"شدت", freshness:"تازگی", scope:"دامنهٔ مجاز", notReported:"گزارش نشده", fresh:"قدیمی علامت‌گذاری نشده", stale:"قدیمی", partial:"ناقص", missing:"غایب", older:"بیش از پنج دقیقه از گردآوری گذشته است", rawNotice:"فقط فیلدهای تشخیصی مجاز", copyRaw:"کپی دادهٔ خام", copied:"کپی شد", copyFailed:"کپی خودکار در دسترس نیست؛ متن را انتخاب و کپی کنید.", contextHelp:"این مشاهده از پاسخ مجاز جاری است؛ علت یا مجوز تغییر را اثبات نمی‌کند.", noChart:"سری زمانی سازگار برای این مشاهده ارائه نشده است.", noRelated:"مشاهدهٔ دیگری برای این میزبان در این پاسخ نیست.", noCapability:"این بخش در انتشار کنترل‌شدهٔ فعلی پیاده‌سازی نشده است؛ به‌معنی دسترسی یا اتصال تازه نیست.", catalogHelp:"فهرست تأییدشدهٔ استقرار؛ تأیید به‌معنی آزمون سلامت نیست.", knowledgeHelp:"بازیابی از اسناد محلی متصل نیست. پاسخ عمومی از دانش مدل است، نه پایگاه دانشِ فرضی.", settingsHelp:"تم و زبان رابط، ترجیح محلی‌اند؛ تنظیمات عملیاتی اینجا ویرایش نمی‌شوند.", supportHelp:"با مدیر NextOps سازمان تماس بگیرید. این پنل به پشتیبانی خارجی متصل نیست.",
      evidenceCollected:"گردآوری شاهد", answerGenerated:"تکمیل پاسخ", auditRecorded:"شناسهٔ ممیزی دریافت شد", queue:"زمان صف گزارش‌شده", clientTime:"رفت‌وبرگشت مرورگر", cancelWait:"توقف انتظار", cancelNotice:"انتظار در این مرورگر متوقف شد؛ درخواست فقط‌خواندنی ممکن است در سرور کامل شود. توقف راه دور اثبات نشده است. برای پیام ذخیره‌شده، پیگیری با همان شناسهٔ درخواست انجام می‌شود.",
      signalGate:"دروازهٔ سیگنال امید؛ طرح نمادین شبکه", pauseMotion:"توقف حرکت", resumeMotion:"ادامهٔ حرکت", staticMotion:"صحنهٔ ثابت؛ حرکت کاهش‌یافته", loginBoundary:"هویت محلی، پردازش فقط با CPU، بدون جایگزین ابری.", showPassword:"نمایش گذرواژه", hidePassword:"پنهان‌کردن گذرواژه", localModel:"مدل محلی CPU", newChat:"گفتگوی تازه", freshResponse:"مشاهدات پاسخ", reference:"مرجع شاهد", noTraceSaved:"پاسخ ذخیره‌شده؛ بدون اجرای تازه", attachmentUnavailable:"API فعلی از پیوست پشتیبانی نمی‌کند.",
      navOpen:"بازکردن پیمایش", navClose:"بستن پیمایش", evidencePrevious:"شاهد قبلی", evidenceNext:"شاهد بعدی", evidenceClose:"بستن شاهد", requestDetails:"جزئیات درخواست", accountMenu:"منوی حساب", closeSearch:"بستن جست‌وجو", loginService:"سرویس احراز هویت در دسترس نیست. بعداً دوباره تلاش کنید.", loginRate:"تعداد تلاش ورود بیش از حد مجاز است. پیش از تلاش دوباره کمی صبر کنید.",
      selectedResponse:"مشاهدات پاسخ انتخاب‌شده", archivedResponse:"مشاهدات پاسخ پیشین؛ بدون گردآوری تازه", selectedContextHelp:"این مشاهده از پاسخ مجاز انتخاب‌شده است؛ علت یا مجوز تغییر را اثبات نمی‌کند."
    }
  };
  let locale = "en", authenticated = false, entries = [], selected = -1, last = null, catalog = [], model = "", returnFocus = null, selectedCard = null, requestFailed = false, connectorAvailable = null;
  let turnEvidence = new WeakMap(), restoreNavFocus = true, destination = "investigations";
  const freshnessWindow = 300000;
  let freshnessTimer = null, pageActive = true;
  const t = key => copy[locale][key] || key;
  const safe = value => String(value ?? "").slice(0, 6000).replace(/\b(Bearer\s+)\S+/gi,"$1[redacted]").replace(/((?:password|passwd|secret|api[_-]?token|authorization)\s*[:=]\s*)[^\s,;]+/gi,"$1[redacted]");
  function node(tag, text, className) { const n = document.createElement(tag); if (text !== undefined) n.textContent = safe(text); if (className) n.className = className; return n; }
  function icon(name) { const n = document.createElementNS("http://www.w3.org/2000/svg", "svg"); n.setAttribute("class", "ui-icon"); n.setAttribute("aria-hidden", "true"); const use = document.createElementNS(n.namespaceURI,"use"); use.setAttribute("href",`#i-${name}`); n.append(use); return n; }
  function time(value) { const date = new Date(value); return Number.isFinite(date.getTime()) ? date.toLocaleString(locale === "fa" ? "fa-IR" : "en-GB", {timeZone:"UTC",timeZoneName:"short",hour12:false}) : t("notReported"); }
  function text(id, value) { const n=el(id); if (n) { n.removeAttribute("data-ui"); n.textContent=value; } }
  function status(entry) { if (!entry) return "missing"; if (entry.stale || Date.now()-Date.parse(entry.collected)>freshnessWindow) return "stale"; if (entry.partial) return "partial"; return entry.observed ? "fresh" : "missing"; }
  function freshnessLabel(entry) { const state=status(entry); return `${t(state)}${entry.partial&&state!=="partial"?` · ${t("partial")}`:""}`; }
  function stopFreshnessTimer() { if(freshnessTimer!==null)clearTimeout(freshnessTimer); freshnessTimer=null; }
  function refreshFreshness() {
    stopFreshnessTimer();
    const inspector=el("evidenceInspector"), entry=entries[selected];
    if(!authenticated || !pageActive || document.hidden || !entry || !inspector?.isConnected || el("workspaceView").classList.contains("hidden") || !inspector.getClientRects().length)return;
    const badge=el("inspectorContent").querySelector(".freshness"), label=el("inspectorContent").querySelector("[data-evidence-freshness]");
    if(!badge || !label)return;
    const state=status(entry), agingTransition=state==="stale"&&!entry.stale&&!badge.classList.contains("stale");
    badge.textContent=t(state);badge.className=`freshness ${state}`;
    if(state==="stale"&&!entry.stale)badge.title=t("older");else badge.removeAttribute("title");
    label.textContent=freshnessLabel(entry);
    if(agingTransition)el("evidenceFreshnessStatus").textContent=`${t("freshness")}: ${freshnessLabel(entry)}. ${t("older")}.`;
    // Age this already-collected observation, never query again or replace its data.
    // One visible selection owns at most one timer; stale entries need no polling.
    const remaining=Date.parse(entry.collected)+freshnessWindow-Date.now()+1;
    if(!entry.stale && Number.isFinite(remaining) && remaining>0)freshnessTimer=setTimeout(refreshFreshness,Math.min(remaining,freshnessWindow));
  }
  function namedUnits(question) {return [...question.matchAll(/(?<![\w@.-])([A-Za-z0-9_@.-]+\.(?:service|socket|timer))(?![\w@.-])/gi)].map(m=>m[1].toLocaleLowerCase("en-US"));}
  function networkGroups(question) {return [/\b(?:dns|resolvers?|nameservers?)\b|نام[‌-]?سرور|دی[‌-]?ان[‌-]?اس/i.test(question),/\b(?:routes?|routing|gateway)\b|مسیر|دروازه/i.test(question),/\b(?:ports?|sockets?|listen(?:ing)?)\b|پورت|سوکت|شنود/i.test(question)];}
  // Only closed diagnostic fields from existing public contracts enter the inspector. Never raw API objects.
  function adapt(evidence, incident, focus, question) {
    if (!evidence) return [];
    const s = incident ? evidence.zabbix.summary : evidence;
    const source = s.source_id || "primary", target = incident ? evidence.target_id : s.target_id || s.host;
    const common = {source:`Zabbix ${s.source_version}`, host:s.host, scope:`${source} / ${target}`, collected:s.collected_at, partial:!!s.is_partial || (incident && !!evidence.zabbix.is_partial)};
    let out = (s.metrics || []).map(m => ({...common, title:m.name, metric:m.key, value:`${m.value}${m.units ? ` ${m.units}` : ""}`, observed:m.measured_at, stale:!!m.stale, series:incident?(evidence.zabbix.history || []).filter(p=>p.key===m.key&&p.units===m.units&&Number.isFinite(Number(p.value))&&Number.isFinite(Date.parse(p.measured_at))).slice(0,200).map(p=>({value:Number(p.value),time:p.measured_at})):[], raw:{name:m.name,key:m.key,value:m.value,units:m.units,measured_at:m.measured_at,stale:m.stale}}));
    out.push(...(s.active_problems || []).map(p => ({...common,title:p.name || p.description || "Zabbix problem",value:t("activeAlerts"),observed:p.started_at || p.occurred_at,severity:p.severity,raw:{name:p.name,severity:p.severity,started_at:p.started_at,event_id:p.event_id}})));
    if (incident) {
      const z=evidence.zabbix, l=evidence.linux;
      out.push(...(z.events || []).map(e => ({...common,title:e.name,value:e.state,observed:e.occurred_at,severity:e.severity,raw:{event_id:e.event_id,name:e.name,state:e.state,severity:e.severity,occurred_at:e.occurred_at}})));
      const linux={source:`Linux ${l.collector_version}`,host:l.hostname,scope:`Linux / ${evidence.target_id || l.target_id}`,collected:l.collected_at,observed:l.collected_at,partial:!!l.is_partial};
      const system=[{title:"System load",metric:"load_1m / load_5m / load_15m",value:`${l.load_1m} / ${l.load_5m} / ${l.load_15m}`,raw:{load_1m:l.load_1m,load_5m:l.load_5m,load_15m:l.load_15m}},{title:"Memory available",metric:"memory_available_bytes",value:`${(l.memory_available_bytes/1024**3).toFixed(1)} GiB`,raw:{memory_available_bytes:l.memory_available_bytes,memory_total_bytes:l.memory_total_bytes}}];
      const services=(l.services || []).map(s => ({title:s.unit,metric:"systemd",value:`${s.active_state} / ${s.sub_state}`,raw:{unit:s.unit,active_state:s.active_state,sub_state:s.sub_state,load_state:s.load_state}}));
      const files=(l.filesystems || []).map(f => ({title:f.path,metric:"Filesystem capacity",value:`${f.used_percent}%`,raw:{path:f.path,used_percent:f.used_percent,available_bytes:f.available_bytes}}));
      const journals=(l.journal || []).map(j => ({title:j.unit,metric:"Journal entry",value:j.message,observed:j.observed_at,raw:{unit:j.unit,message:j.message,observed_at:j.observed_at}}));
      const network=[...(l.nameservers || []).map(n=>({title:n,metric:"Configured resolver",value:n,raw:{resolver:n}})),...(l.routes || []).map(r=>({title:r.destination,metric:"Recorded route",value:`${r.gateway} · ${r.interface}`,raw:{destination:r.destination,gateway:r.gateway,interface:r.interface}})),...(l.listening_sockets || []).map(s=>({title:`${s.address}:${s.port}`,metric:"Listening socket",value:s.family,raw:{address:s.address,port:s.port,family:s.family}}))];
      let selectedLinux=[...system,...services,...files,...journals,...network];
      if (focus==="file_listing") return []; // Do not replace an unavailable file listing with a data dump.
      if (focus==="filesystems") {out=[]; selectedLinux=files;}
      if (focus==="host_status") {out=[]; selectedLinux=[...system,...services];}
      if (["service","network","network_service"].includes(focus)) {
        out=[]; selectedLinux=[];
        if (focus!=="network") {
          const names=namedUnits(question);
          selectedLinux.push(...services.filter(s=>!names.length || names.includes(s.title.toLowerCase())));
          if (/journal|logs?|ژورنال|لاگ|گزارش/i.test(question)) selectedLinux.push(...journals.filter(j=>!names.length || names.includes(j.title.toLowerCase())));
        }
        if(focus!=="service") {const groups=networkGroups(question);selectedLinux.push(...network.filter(n=>!groups.some(Boolean) || groups[["Configured resolver","Recorded route","Listening socket"].indexOf(n.metric)]));}
      }
      out.push(...selectedLinux.map(s=>({...linux,...s})));
    }
    return out.map((item,i)=>({...item,id:String(i),category:Number.isInteger(item.severity)?"problems":item.source.startsWith("Zabbix")?"metrics":"diagnostics",raw:Object.fromEntries(Object.entries({...item.raw,source:item.source,host:item.host,scope:item.scope,collected_at:item.collected}).filter(([,value])=>value!==undefined).map(([key,value])=>[key,typeof value==="string"?safe(value):value]))}));
  }
  function renderRows(card) {
    const list=card.querySelector("[data-evidence-rows]"); list.replaceChildren();
    const labels=locale==="fa"?{all:"همهٔ مشاهدات",problems:"مشکلات",metrics:"سنجه‌ها",empty:"در این پاسخ مشاهده‌ای برای این دسته دریافت نشد؛ این به‌معنی نبود مشکل نیست."}:{all:"All observations",problems:"Problems",metrics:"Metrics",empty:"No observations in this category were returned. This does not prove there are no problems."};
    const filter=card.dataset.evidenceFilter || "all";
    if(entries.length){const group=node("div",undefined,"evidence-filters");group.setAttribute("role","group");group.setAttribute("aria-label",t("evidence"));["all","problems","metrics"].forEach(kind=>{const count=entries.filter(e=>kind==="all"||e.category===kind).length;const b=node("button",`${labels[kind]} (${count})`,"quiet-button");b.type="button";b.dataset.evidenceFilter=kind;b.setAttribute("aria-pressed",String(filter===kind));b.addEventListener("click",()=>{activateTurn(b);card.dataset.evidenceFilter=kind;renderRows(card);card.querySelector(`[data-evidence-filter="${kind}"]`).focus();});group.append(b);});list.append(group);}
    const rows=entries.map((entry,i)=>({entry,i})).filter(({entry})=>filter==="all"||entry.category===filter);
    rows.forEach(({entry,i})=>{ const b=node("button",undefined,"evidence-row"); b.type="button"; b.dataset.evidenceIndex=String(i); b.setAttribute("aria-current",String(i===selected)); const n=node("span",String(i+1),"evidence-number"); const label=node("span",`${entry.title} · ${entry.value}`,"evidence-label"); label.dir="auto"; const tm=node("time",time(entry.observed || entry.collected)); if(entry.observed) tm.dateTime=entry.observed; b.append(n,label,tm); list.append(b); });
    if(entries.length&&!rows.length)list.append(node("p",labels.empty,"rail-help"));
    card.querySelector('[data-followup="evidence"]').textContent=`${t("reviewEvidence")} (${entries.length})`;
  }
  function renderFindings(card, evidence, incident) {
    // The API has no structured findings contract. Do not fill the view with invented
    // structure or four repeated unavailable cards; keep the supported answer and evidence.
    const grid=card.querySelector("[data-findings]");
    grid.replaceChildren(); grid.classList.add("hidden");
  }
  function showEmpty() { stopFreshnessTimer(); const root=el("inspectorContent"); root.replaceChildren(); const box=node("div",undefined,"evidence-empty"); box.append(node("h3",t("noSelected")),node("p",t("selectEvidence"))); root.append(box); el("panel-raw").replaceChildren(node("p",t("noEvidence"))); ["related","context","visualize"].forEach(k=>el(`panel-${k}`).replaceChildren(node("p",t("notAvailable")))); text("evidencePosition",`0 / ${entries.length}`); el("evidencePrevious").disabled=true; el("evidenceNext").disabled=true; }
  function select(index, open=false, origin=null) {
    if(!authenticated || !entries[index]) return;
    selected=index; returnFocus=origin || returnFocus;
    const entry=entries[index], state=status(entry), root=el("inspectorContent"); root.replaceChildren();
    const card=node("section",undefined,"evidence-detail-card"); const badge=node("span",t(state),`freshness ${state}`); if(state==="stale"&&!entry.stale) badge.title=t("older"); card.append(badge,node("h3",entry.title));
    const announcement=node("span",undefined,"sr-only");announcement.id="evidenceFreshnessStatus";announcement.setAttribute("role","status");announcement.setAttribute("aria-live","polite");announcement.setAttribute("aria-atomic","true");card.append(announcement);
    const dl=node("dl"); [["source",entry.source],["observed",time(entry.observed)],["collected",time(entry.collected)],["host",entry.host],["metric",entry.metric || t("notReported")],["value",entry.value],["threshold",t("notReported")],["severity",Number.isInteger(entry.severity)?String(entry.severity):t("notReported")],["freshness",freshnessLabel(entry)],["scope",entry.scope]].forEach(([key,value])=>{ const dt=node("dt",t(key)),dd=node("dd"); const b=node("bdi",value); b.dir=["host","metric","scope"].includes(key)?"ltr":"auto"; if(key==="freshness")b.dataset.evidenceFreshness=""; dd.append(b); dl.append(dt,dd); }); card.append(dl); root.append(card);
    const raw=el("panel-raw"), actions=node("div",undefined,"raw-actions"), button=node("button",t("copyRaw"),"quiet-button"); button.type="button"; button.id="copyRaw"; button.addEventListener("click",async()=>{try{await navigator.clipboard.writeText(JSON.stringify(entry.raw,null,2));text("rawCopyStatus",t("copied"));}catch(_){text("rawCopyStatus",t("copyFailed"));}}); actions.append(node("span",t("rawNotice")),button); const pre=node("pre"), code=node("code");pre.dir="ltr";pre.tabIndex=0;pre.setAttribute("role","region");pre.setAttribute("aria-label",t("raw"));
    // Values were already bounded/redacted by adapt(). Do not clip the serialized object a
    // second time: that produces invalid JSON and makes the displayed data differ from Copy.
    code.textContent=JSON.stringify(entry.raw,null,2);pre.append(code); const msg=node("p",undefined,"rail-help");msg.id="rawCopyStatus";msg.setAttribute("role","status");raw.replaceChildren(actions,pre,msg);
    const related=el("panel-related");related.replaceChildren();entries.forEach((item,i)=>{if(i!==index&&item.host===entry.host){const b=node("button",item.title,"evidence-row");b.type="button";b.dataset.evidenceIndex=String(i);related.append(b);}});if(!related.children.length)related.append(node("p",t("noRelated")));
    el("panel-context").replaceChildren(node("p",t("selectedContextHelp")),node("p",selectedCard===el("resultCard")?t("selectedResponse"):t("archivedResponse")),node("p",`${t("scope")}: ${safe(entry.scope)}`),node("p",`${t("collected")}: ${time(entry.collected)}`));
    const chartPanel=el("panel-visualize");chartPanel.replaceChildren();
    if(entry.series?.length>=2){
      const points=[...entry.series].sort((a,b)=>Date.parse(a.time)-Date.parse(b.time));
      const min=Math.min(...points.map(p=>p.value)),max=Math.max(...points.map(p=>p.value)),start=Date.parse(points[0].time),end=Date.parse(points.at(-1).time);
      if(end>start){const svg=document.createElementNS("http://www.w3.org/2000/svg","svg");svg.setAttribute("viewBox","0 0 320 130");svg.setAttribute("class","evidence-chart");svg.setAttribute("role","img");svg.setAttribute("aria-label",`${entry.title} · ${time(points[0].time)} — ${time(points.at(-1).time)}`);const line=document.createElementNS(svg.namespaceURI,"polyline");line.setAttribute("points",points.map(p=>`${10+(Date.parse(p.time)-start)/(end-start)*300},${115-(p.value-min)/(max-min || 1)*100}`).join(" "));svg.append(line);chartPanel.append(svg);}
      const table=node("table");const caption=node("caption",entry.title);table.append(caption);points.forEach(p=>{const row=node("tr");row.append(node("th",time(p.time)),node("td",String(p.value)));table.append(row);});chartPanel.append(table);
    }else chartPanel.append(node("p",t("noChart"))); // No fabricated series, threshold, baseline or confidence.
    text("evidencePosition",`${index+1} / ${entries.length}`); el("evidencePrevious").disabled=index===0;el("evidenceNext").disabled=index===entries.length-1;
    document.querySelectorAll(".conversation-turn [data-evidence-index]").forEach(n=>n.setAttribute("aria-current",String(n.closest(".conversation-turn")===selectedCard && Number(n.dataset.evidenceIndex)===index)));
    if(open&&matchMedia("(max-width:1449px)").matches) { el("evidenceDialog").append(el("evidenceInspector")); if(!el("evidenceDialog").open)el("evidenceDialog").showModal(); el("evidenceClose").focus(); }
    else if(open) { el("inspectorSlot").classList.remove("inspector-closed"); el("evidenceClose").focus({preventScroll:true}); }
    refreshFreshness();
  }
  function renderTrace(assistant, result, elapsed, saved) {
    const list=el("traceStages");list.replaceChildren();
    if(saved){list.append(node("li",t("noTraceSaved")));text("traceDuration","");return;}
    const stages=[];if(result?.evidence){const s=result.evidence.zabbix?.summary || result.evidence;stages.push(["evidenceCollected",time(s.collected_at)]);}
    if(assistant?.completed_at)stages.push(["answerGenerated",time(assistant.completed_at)]);
    if(result?.audit_event_id)stages.push(["auditRecorded",t("completed")]);
    if(Number.isFinite(assistant?.queue_ms))stages.push(["queue",`${assistant.queue_ms} ms`]);
    stages.forEach(([k,v])=>{const item=node("li");item.append(icon("check"),node("span",`${t(k)} · ${v}`));list.append(item);});
    if(!stages.length)list.append(node("li",t("noTrace")));
    text("traceDuration",Number.isFinite(elapsed)?`${t("clientTime")} · ${(elapsed/1000).toFixed(1)} s`:"");
  }
  function render(assistant, result, question, incident=false, elapsed=null, saved=false) {
    last={assistant,result,question,incident,elapsed,saved};
    document.body.dataset.hasAnswer="true";
    document.body.dataset.hasEvidence=String(!!result?.evidence);
    const evidence=result?.evidence || null;
    entries=adapt(evidence,incident,result?.answer_focus || "overview",question); selected=entries.length?0:-1;
    const card=el("resultCard");
    card.querySelector(".user-message").dataset.userInitial=el("profileInitial").textContent;
    selectedCard=card;turnEvidence.set(card,entries);delete card.dataset.evidenceFilter;renderFindings(card,evidence,incident);renderRows(card);
    const summaryForHeader=evidence?(incident?evidence.zabbix.summary:evidence):null;
    text("openedTime",`${t(summaryForHeader?"collected":"completed")} · ${time(summaryForHeader?.collected_at || assistant.completed_at)}`);
    text("sourceContext",summaryForHeader?`${incident?"Zabbix + Linux":"Zabbix"} · ${summaryForHeader.source_id || "primary"} / ${incident?evidence.target_id:summaryForHeader.target_id || summaryForHeader.host}`:t("noLive"));
    text("investigationState",t("completed"));text("investigationValue",t("completed"));text("investigationValueHelp",t("freshResponse"));
    const summary=evidence?(incident?evidence.zabbix.summary:evidence):null;
    text("alertsValue",summary?String(summary.active_problems.length):"—");text("alertsValueHelp",summary?`${t("scopeCount")}${summary.is_partial?` · ${t("partial")}`:""}`:t("notAvailable"));
    text("hostsValue","—");text("hostsValueHelp",t("noAffected"));
    el("shareInvestigation").disabled=!question;
    el("requestDetailsButton").disabled=false;
    card.querySelector('[data-followup="evidence"]').disabled=!entries.length;
    if(selected>=0)select(selected);else showEmpty();renderTrace(assistant,result,elapsed,saved);
    el("modelStatusLabel").textContent=t("localModel");el("modelStatusLabel").title=assistant.model_id || t("localModel");
    window.NextOpsCapabilities?.locale(locale);
  }
  function clear() {
    stopFreshnessTimer();
    entries=[];selected=-1;last=null;returnFocus=null;selectedCard=null;turnEvidence=new WeakMap();requestFailed=false;["evidenceDialog","searchDialog","navDialog"].forEach(id=>{if(el(id).open)el(id).close();});el("inspectorSlot").append(el("evidenceInspector"));document.body.append(el("appNav"));el("profileMenu").open=false;el("inspectorSlot").classList.add("inspector-closed");
    document.body.dataset.hasAnswer="false";document.body.dataset.hasEvidence="false";
    el("overviewDetails").open=false;el("executionDetails").open=false;
    ["searchInput"].forEach(id=>el(id).value="");el("searchResults").replaceChildren();
    el("resultCard").querySelector(".user-message").removeAttribute("data-user-initial");
    ["alertsValue","hostsValue"].forEach(id=>text(id,"—"));text("alertsValueHelp",t("notAvailable"));text("hostsValueHelp",t("noAffected"));text("investigationValue",t("readyToAsk"));text("investigationValueHelp",t("notStarted"));text("investigationState",t("readyToAsk"));text("openedTime",t("notStarted"));text("sourceContext",t("noEvidence"));text("traceDuration","");el("traceStages").replaceChildren(node("li",t("noTrace")));el("shareInvestigation").disabled=true;el("requestDetailsButton").disabled=true;el("requestDetailsButton").setAttribute("aria-expanded","false");showEmpty();
  }
  function session(actor) { authenticated=!!actor;document.body.dataset.authenticated=String(authenticated);document.querySelectorAll(".auth-only").forEach(n=>n.classList.toggle("hidden",!authenticated));if(authenticated){const name=actor.username || t("privateWorkspace");text("profileName",name);text("profileInitial",actor.username?actor.username.slice(0,1).toUpperCase():"U");navigate("ask",false);}else{catalog=[];model="";connectorAvailable=null;text("connectorValue",t("notAvailable"));text("connectorValueHelp",t("engineUnknown"));text("profileName","");text("profileInitial","");el("environmentSelect").replaceChildren(node("option",t("environment")));el("destinationContent").replaceChildren();text("destinationTitle","");text("destinationHelp","");text("modelStatusLabel",t("localModel"));el("modelStatusLabel").removeAttribute("title");clear();}
    window.NextOpsMotion?.update();
  }
  function setLocale(lang) {
    const previousCard=selectedCard, previousEntries=entries, previousSelected=selected;
    locale=lang;
    document.querySelectorAll("[data-ui]").forEach(n=>n.textContent=t(n.dataset.ui));
    [["navOpen","navOpen"],["navClose","navClose"],["evidencePrevious","evidencePrevious"],
      ["evidenceNext","evidenceNext"],["evidenceClose","evidenceClose"],
      ["requestDetailsButton","requestDetails"],["shareInvestigation","copyQuestion"]]
      .forEach(([id,key])=>el(id).setAttribute("aria-label",t(key)));
    [["#appNav","mainNavigation"],["#navDialog","mainNavigation"],
      ["#conversationFeed","conversation"],[".status-panel","serviceStatus"],
      [".inspector-tabs","evidenceDetails"]]
      .forEach(([selector,key])=>document.querySelector(selector).setAttribute("aria-label",t(key)));
    el("profileMenu").querySelector("summary").setAttribute("aria-label",t("accountMenu"));
    el("searchDialog").querySelector("[data-close-dialog]").setAttribute("aria-label",t("closeSearch"));
    el("modelStatusLabel").textContent=t("localModel");
    el("modelStatusLabel").title=model || t("localModel");
    window.NextOpsCapabilities?.locale(lang);
    if(last)render(last.assistant,last.result,last.question,last.incident,last.elapsed,last.saved);
    else clear();
    if(connectorAvailable!==null){
      text("connectorValue",t(connectorAvailable?"reachable":"unavailable"));
      text("connectorValueHelp",t("engineUnknown"));
    }
    el("globalSearch").setAttribute("aria-label",t("search"));
    attachment?.setAttribute("aria-label",t("attachmentUnavailable"));
    if(previousCard && previousSelected>=0){
      if(previousCard!==el("resultCard")){selectedCard=previousCard;entries=previousEntries;}
      select(previousSelected);
    }
    if(authenticated&&!el("destinationView").classList.contains("hidden"))navigate(destination,false);
    window.NextOpsMotion?.update();
  }
  function navigate(key, moveFocus=true) {
    if(!authenticated)return;
    destination=key;
    if(el("navDialog").open){restoreNavFocus=false;el("navDialog").close();}el("profileMenu").open=false;
    el("usersView").classList.add("hidden");
    document.querySelectorAll("[data-nav]").forEach(n=>{n.classList.toggle("selected",n.dataset.nav===key);if(n.dataset.nav===key)n.setAttribute("aria-current","page");else n.removeAttribute("aria-current");});
    const existing=["investigations","ask","overview"].includes(key);el("workspaceView").classList.toggle("hidden",!existing);el("destinationView").classList.toggle("hidden",existing);
    if(existing){if(moveFocus){if(key==="ask")el("question").focus();else el("workspaceHeading").focus();}return;}
    text("destinationTitle",t(key));let help=t("noCapability");if(key==="knowledge")help=t("knowledgeHelp");if(key==="settings")help=t("settingsHelp");if(key==="support")help=t("supportHelp");if(["infrastructure","connectors"].includes(key))help=t("catalogHelp");text("destinationHelp",help);el("destinationContent").replaceChildren();
    if(["infrastructure","connectors"].includes(key))catalog.forEach(source=>{const c=node("section",undefined,"destination-card");c.append(node("h2",source.label),node("p",`${source.source_id} · ${t("catalogHelp")}`));source.targets.forEach(target=>{const b=node("button",`${t("reviewEvidence")} · ${target.label}`,"quiet-button");b.type="button";b.dataset.inspectSource=source.source_id;b.dataset.inspectTarget=target.target_id;b.addEventListener("click",()=>document.dispatchEvent(new CustomEvent("nextops:inspect-source",{detail:{source_id:source.source_id,target_id:target.target_id}})));c.append(b);});el("destinationContent").append(c);});
    if(key==="settings"){const b=node("button",el("themeButton").querySelector("span").textContent,"quiet-button");b.type="button";b.dataset.themePreference="";b.addEventListener("click",()=>el("themeButton").click());el("destinationContent").append(b);}
    if(moveFocus)el("destinationTitle").focus();
  }
  function search() {if(!authenticated)return;const query=el("searchInput").value.toLocaleLowerCase();const root=el("searchResults");root.replaceChildren();document.querySelectorAll(".saved-chat-button").forEach(chat=>{if(chat.textContent.toLocaleLowerCase().includes(query)){const b=node("button",chat.textContent);b.type="button";b.addEventListener("click",()=>{el("searchDialog").close();navigate("ask");chat.click();});root.append(b);}});entries.forEach((entry,i)=>{if(`${entry.title} ${entry.value}`.toLocaleLowerCase().includes(query)){const b=node("button",entry.title);b.type="button";b.addEventListener("click",()=>{el("searchDialog").close();navigate("ask",false);select(i,true,el("globalSearch"));});root.append(b);}});if(!root.children.length)root.append(node("p",t("noMatches")));}
  function activateTurn(control) {const card=control.closest(".conversation-turn");if(card&&turnEvidence.has(card)){selectedCard=card;entries=turnEvidence.get(card);selected=0;}}
  document.addEventListener("click",event=>{const b=event.target.closest("[data-evidence-index]");if(b){activateTurn(b);select(Number(b.dataset.evidenceIndex),true,b);}const nav=event.target.closest("[data-nav]");if(nav)navigate(nav.dataset.nav);const close=event.target.closest("[data-close-dialog]");if(close)el(close.dataset.closeDialog).close();const follow=event.target.closest("[data-followup]");if(follow){if(follow.dataset.followup==="evidence"){activateTurn(follow);select(selected>=0?selected:0,true,follow);}else el("question").focus();}});
  el("evidencePrevious").addEventListener("click",()=>select(selected-1));el("evidenceNext").addEventListener("click",()=>select(selected+1));
  el("evidenceClose").addEventListener("click",()=>{if(el("evidenceDialog").open)el("evidenceDialog").close();else{el("inspectorSlot").classList.add("inspector-closed");(returnFocus || el("resultCard").querySelector('[data-followup="evidence"]')).focus();}});
  el("evidenceDialog").addEventListener("close",()=>{el("inspectorSlot").append(el("evidenceInspector"));returnFocus?.focus();});
  el("navOpen").addEventListener("click",()=>{restoreNavFocus=true;el("navDialog").append(el("appNav"));el("navDialog").showModal();el("navClose").focus();});el("navClose").addEventListener("click",()=>el("navDialog").close());el("navDialog").addEventListener("close",()=>{document.body.append(el("appNav"));if(authenticated&&restoreNavFocus)el("navOpen").focus();restoreNavFocus=true;});
  el("appNav").addEventListener("click",event=>{if(event.target.closest(".saved-chat-button, #deleteChatButton")&&el("navDialog").open)el("navDialog").close();});
  el("destinationBack").addEventListener("click",()=>navigate("investigations"));
  el("globalSearch").addEventListener("click",()=>{search();el("searchDialog").showModal();el("searchInput").focus();});el("searchInput").addEventListener("input",search);
  el("searchDialog").addEventListener("close",()=>{if(authenticated)el("globalSearch").focus();});
  el("searchDialog").addEventListener("keydown",event=>{if(event.key==="Escape"){event.preventDefault();el("searchDialog").close();}});
  document.addEventListener("keydown",event=>{if(authenticated&&(event.ctrlKey||event.metaKey)&&event.key.toLowerCase()==="k"){event.preventDefault();if(!el("searchDialog").open)el("globalSearch").click();}});
  const tabs=[...document.querySelectorAll("[data-tab]")];function tab(b){tabs.forEach(n=>{const active=n===b;n.setAttribute("aria-selected",String(active));n.tabIndex=active?0:-1;el(`panel-${n.dataset.tab}`).classList.toggle("hidden",!active);});}
  tabs.forEach((b,i)=>{b.addEventListener("click",()=>tab(b));b.addEventListener("keydown",event=>{let index=i;const direction=locale==="fa"?-1:1;if(event.key==="ArrowRight")index=(i+direction+tabs.length)%tabs.length;else if(event.key==="ArrowLeft")index=(i-direction+tabs.length)%tabs.length;else if(event.key==="Home")index=0;else if(event.key==="End")index=tabs.length-1;else return;event.preventDefault();tab(tabs[index]);tabs[index].focus();});});
  el("shareInvestigation").addEventListener("click",async()=>{if(!last)return;try{await navigator.clipboard.writeText(last.question);text("copyStatus",t("copied"));}catch(_){text("copyStatus",t("copyFailed"));}});
  el("requestDetailsButton").setAttribute("aria-controls","evidenceDetails");
  el("requestDetailsButton").setAttribute("aria-expanded","false");
  el("evidenceDetails").addEventListener("toggle",()=>el("requestDetailsButton").setAttribute("aria-expanded",String(el("evidenceDetails").open)));
  el("requestDetailsButton").addEventListener("click",()=>{const details=el("evidenceDetails");if(!el("resultCard").classList.contains("hidden")){details.open=!details.open;el("requestDetailsButton").setAttribute("aria-expanded",String(details.open));if(details.open){details.tabIndex=-1;details.focus();}}});
  // The current contract has one authorized environment, not a cross-environment switch.
  el("environmentSelect").disabled=true;
  document.addEventListener("click",event=>{if(!event.target.closest("#workspaceInputControls"))el("composerOptions").open=false;if(!event.target.closest("#profileMenu, #usersBack"))el("profileMenu").open=false;});
  document.addEventListener("keydown",event=>{if(event.key==="Escape" && el("composerOptions").open){el("composerOptions").open=false;el("composerOptions").querySelector("summary").focus();}});
  el("usersButton").addEventListener("click",()=>el("destinationView").classList.add("hidden"));
  matchMedia("(min-width:1450px)").addEventListener("change",event=>{if(event.matches&&el("evidenceDialog").open){el("inspectorSlot").classList.remove("inspector-closed");el("evidenceDialog").close();}refreshFreshness();});
  matchMedia("(min-width:1101px)").addEventListener("change",event=>{if(event.matches&&el("navDialog").open)el("navDialog").close();});
  const modelLabel=node("button",t("localModel"),"model-status-label");modelLabel.type="button";modelLabel.setAttribute("aria-haspopup","dialog");modelLabel.id="modelStatusLabel";document.querySelector(".workspace-tools").insertBefore(modelLabel,document.querySelector(".environment-select"));
  const attachment=node("button",undefined,"icon-button attachment-control");attachment.type="button";attachment.disabled=true;attachment.title=t("attachmentUnavailable");attachment.setAttribute("aria-label",t("attachmentUnavailable"));attachment.append(icon("plus"));el("assistantForm").prepend(attachment);
  document.addEventListener("visibilitychange",refreshFreshness);
  document.addEventListener("nextops-theme-change",()=>{
    document.querySelectorAll("[data-theme-preference]").forEach(button=>{
      button.textContent=el("themeButton").querySelector("span").textContent;
    });
  });
  window.addEventListener("pagehide",()=>{pageActive=false;stopFreshnessTimer();});
  window.addEventListener("pageshow",()=>{pageActive=true;refreshFreshness();});
  // Watch only container visibility/mount changes, not evidence content or the whole page.
  // This includes the existing account view and the responsive evidence drawer.
  const freshnessVisibility=new MutationObserver(refreshFreshness);
  freshnessVisibility.observe(el("workspaceView"),{attributes:true,attributeFilter:["class"]});
  freshnessVisibility.observe(el("inspectorSlot"),{attributes:true,attributeFilter:["class"],childList:true});
  freshnessVisibility.observe(el("evidenceDialog"),{attributes:true,attributeFilter:["open"],childList:true});
  window.NextOpsView={session,setLocale,render,clear,navigate,t,namedUnits,networkGroups,
    catalog(sources){if(authenticated){catalog=sources;if(["infrastructure","connectors"].includes(destination))navigate(destination,false);}},
    health(kind,ready){if(!authenticated)return;if(kind==="ai"){model=ready?.model_id || "";el("modelStatusLabel").textContent=t("localModel");el("modelStatusLabel").title=model || t("localModel");}else if(kind==="source-selection"){connectorAvailable=null;text("connectorValue",t("notAvailable"));text("connectorValueHelp",t("catalogHelp"));}else{connectorAvailable=!!ready;text("connectorValue",t(ready?"reachable":"unavailable"));text("connectorValueHelp",t("engineUnknown"));}},
    busy(value){
      if(value)requestFailed=false;
      document.body.dataset.requestBusy=String(value);
      const state=t(value?"collecting":requestFailed?"failed":last?"completed":"readyToAsk");
      text("investigationState",state);text("investigationValue",state);
      el("conversationFeed").setAttribute("aria-busy",String(value));
      el("shareInvestigation").disabled=value||!last;
      el("requestDetailsButton").disabled=value||!last;
    },
    failed(){requestFailed=true;text("investigationState",t("failed"));text("investigationValue",t("failed"));},
    archive(original,clone){if(turnEvidence.has(original))turnEvidence.set(clone,turnEvidence.get(original));},
    resumed(assistant,question){render(assistant,null,question,false,null,true);}
  };
  el("evidenceInspector").tabIndex=-1;el("workspaceHeading").tabIndex=-1;el("evidencePosition").dir="ltr";setLocale(document.documentElement.lang==="fa"?"fa":"en");showEmpty();
})();
