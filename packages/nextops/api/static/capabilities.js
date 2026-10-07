/* Authenticated presentation metadata only. Never changes inference or target policy. */
"use strict";
(() => {
  const el = id => document.getElementById(id);
  const copy = {
    en: {title:"Enabled local capabilities",close:"Close capabilities",model:"Serving model",unknown:"Not reported",context:"Configured token ceiling",contextHelp:"Admission limit, not qualification of the entire context window. Questions remain limited to 4,000 characters.",memory:"Saved-chat context",turns:"recent turns",characters:"characters",retention:"Conversation retention",days:"days",thinking:"Thinking mode",disabled:"Disabled in this release",enabled:"Enabled by server policy",queue:"Generation admission",active:"active",queued:"queued",knowledge:"General, coding and technical answers",knowledgeHelp:"Local model knowledge; not live infrastructure facts. Verify important answers independently.",evidence:"Monitoring evidence",evidenceHelp:"Only the selected approved Zabbix source and host. Read-only; no remediation. Partial or unavailable data is not healthy status.",problems:"Inspect active problems",metrics:"Inspect current metrics",status:"Inspect status and limits",sourcePending:"Selected source · not checked",sourceReady:"Selected source · evidence retrieved",sourceFailed:"Selected-source request failed",problemsQuestion:"Show the active problems and their severity for the selected host. Explain what the evidence supports and any missing or partial data. Do not infer root causes.",metricsQuestion:"In at most 60 words, summarize at most two returned monitoring metrics for the selected host, with values and units. State partial, stale or missing-data limits. Other returned observations remain in the evidence panel; do not infer health or causes.",statusQuestion:"Check the current status of the selected host. Distinguish host configuration from reachability and explain the evidence limitations."},
    fa: {title:"قابلیت‌های فعالِ مدل محلی",close:"بستن قابلیت‌ها",model:"مدل پاسخ‌گو",unknown:"گزارش نشده",context:"سقف تنظیم‌شدهٔ توکن",contextHelp:"این سقفِ پذیرش ورودی است، نه تأیید کیفیت کل زمینه. هر پرسش همچنان تا ۴٬۰۰۰ نویسه است.",memory:"زمینهٔ گفت‌وگوی ذخیره‌شده",turns:"نوبت اخیر",characters:"نویسه",retention:"مدت نگه‌داری گفت‌وگو",days:"روز",thinking:"حالت استدلال",disabled:"در این انتشار غیرفعال است",enabled:"با سیاست سرور فعال است",queue:"پذیرش درخواست تولید پاسخ",active:"فعال",queued:"در انتظار",knowledge:"پاسخ عمومی، کدنویسی و راهنمایی فنی",knowledgeHelp:"دانش مدل محلی است، نه وضعیت زندهٔ زیرساخت. پاسخ‌های مهم را مستقل بررسی کنید.",evidence:"شاهد پایش",evidenceHelp:"فقط منبع Zabbix و میزبان مجازِ انتخاب‌شده؛ دسترسی فقط‌خواندنی و بدون اجرای تغییر. دادهٔ ناقص یا غایب، وضعیت سالم نیست.",problems:"بررسی مشکلات فعال",metrics:"بررسی سنجه‌های جاری",status:"بررسی وضعیت و محدودیت‌ها",sourcePending:"منبع انتخاب‌شده؛ هنوز بررسی نشده",sourceReady:"منبع انتخاب‌شده؛ شاهد دریافت شد",sourceFailed:"درخواست منبع انتخاب‌شده ناموفق بود",problemsQuestion:"مشکلات فعال میزبان انتخاب‌شده و شدت آن‌ها را نشان بده. بگو شواهد چه چیزی را تأیید می‌کنند و کدام داده‌ها ناقص یا غایب‌اند. علت ریشه‌ای را حدس قطعی نزن.",metricsQuestion:"در حداکثر ۶۰ واژه، حداکثر دو سنجهٔ پایشِ دریافت‌شده برای میزبان انتخابی را با مقدار و واحد خلاصه کن. محدودیت دادهٔ ناقص، قدیمی یا غایب را بگو. سایر مشاهدات دریافتی در پنل شاهد باقی‌اند؛ سلامت یا علت را نتیجه نگیر.",statusQuestion:"وضعیت فعلی میزبان انتخاب‌شده را بررسی کن. فعال بودن تنظیم میزبان را از دسترسی‌پذیری جدا کن و محدودیت شواهد را توضیح بده."}
  };
  let locale="en", readiness=null, conversation=null, sourceState=null;
  const t = key => copy[locale][key];
  function node(tag,text,className){const n=document.createElement(tag);if(text!==undefined)n.textContent=text;if(className)n.className=className;return n;}
  function modelName(id){if(typeof id!=="string")return t("unknown");return id==="nextops-qwen3-8-27b-q8-0"?"Qwen3.8-27B · Q8 · CPU":id.replace(/^nextops-/,"");}
  const dialog=node("dialog",undefined,"search-dialog capabilities-dialog");dialog.id="modelCapabilitiesDialog";dialog.setAttribute("aria-labelledby","capabilitiesTitle");
  const heading=node("h2");heading.id="capabilitiesTitle";const close=node("button",undefined,"quiet-button");close.type="button";close.id="closeCapabilities";
  const content=node("div");content.id="capabilitiesContent";dialog.append(heading,content,close);document.body.append(dialog);
  close.addEventListener("click",()=>dialog.close());dialog.addEventListener("close",()=>{if(document.body.dataset.authenticated==="true")el("modelStatusLabel")?.focus();});
  document.addEventListener("click",event=>{if(event.target.closest("#modelStatusLabel")&&document.body.dataset.authenticated==="true"){render();dialog.showModal();close.focus();}});
  // Keep mode and approved-source controls outside the collapsed advanced options.
  const controls=node("section",undefined,"workspace-input-controls");controls.id="workspaceInputControls";
  controls.append(el("assistantForm").querySelector(".mode-field"),el("sourceSelectionField"),el("incidentTargetField"),el("composerOptions"));el("assistantForm").before(controls);
  const actions=node("div",undefined,"monitoring-shortcuts");
  ["problems","metrics","status"].forEach(kind=>{const b=node("button",undefined,"quiet-button");b.type="button";b.dataset.monitoringShortcut=kind;b.addEventListener("click",()=>{if(b.disabled)return;el("question").value=t(kind+"Question");el("question").dispatchEvent(new Event("input",{bubbles:true}));el("question").focus();});actions.append(b);});
  el("sourceSelectionField").append(actions);
  function render(){
    heading.textContent=t("title");close.textContent=t("close");content.replaceChildren();
    if(document.body.dataset.authenticated!=="true")return;
    const label=el("modelStatusLabel");if(label){label.textContent=readiness?modelName(readiness.model_id):t("unknown");label.title=readiness?.model_id || t("unknown");label.setAttribute("aria-label",`${t("title")} · ${label.textContent}`);}
    const dl=node("dl");
    const fields=[["model",readiness?modelName(readiness.model_id):t("unknown")],
      ["context",Number.isInteger(readiness?.configured_context_tokens)?readiness.configured_context_tokens.toLocaleString(locale==="fa"?"fa-IR":"en-GB"):t("unknown")],
      ["memory",conversation?.enabled&&Number.isInteger(conversation.context_turns)&&Number.isInteger(conversation.context_characters)?`${conversation.context_turns} ${t("turns")} · ${conversation.context_characters.toLocaleString()} ${t("characters")}`:t("unknown")],
      ["retention",conversation?.enabled&&Number.isInteger(conversation.retention_days)?`${conversation.retention_days} ${t("days")}`:t("unknown")],
      ["thinking",conversation? t(conversation.thinking_enabled===true?"enabled":"disabled"):t("unknown")],
      ["queue",readiness?`${readiness.max_active_requests} ${t("active")} · ${readiness.max_queued_requests} ${t("queued")}`:t("unknown")]];
    fields.forEach(([key,value])=>{dl.append(node("dt",t(key)),node("dd",value));});content.append(dl,node("p",t("contextHelp")),node("h3",t("knowledge")),node("p",t("knowledgeHelp")),node("h3",t("evidence")),node("p",t("evidenceHelp")));
    actions.querySelectorAll("button").forEach(b=>b.textContent=t(b.dataset.monitoringShortcut));
    if(sourceState)sourceHealth(sourceState);
  }
  function sourceHealth(key){sourceState=key;const pill=el("monitoringStatus");pill.className=`status-pill ${key==="sourceReady"?"ready":key==="sourceFailed"?"failed":"checking"}`;const label=pill.querySelector("span");label.removeAttribute("data-i18n");label.textContent=t(key);}
  window.NextOpsCapabilities={
    ready(value){readiness=value;render();},conversation(value){conversation=value;render();},locale(value){locale=value;render();},
    sourceHealth,busy(value){actions.querySelectorAll("button").forEach(b=>b.disabled=value);render();},
    reset(){readiness=null;conversation=null;sourceState=null;content.replaceChildren();el("modelStatusLabel")?.removeAttribute("aria-label");if(dialog.open)dialog.close();},
    sourceSelection(){sourceState=el("monitoringSource").value?"sourcePending":null;if(sourceState){sourceHealth(sourceState);window.NextOpsView?.health("source-selection",null);}}
  };
})();
