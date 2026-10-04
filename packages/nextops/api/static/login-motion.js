/* Decorative motion preferences only; never reads credentials or pointer/keystroke data. */
(() => {
  "use strict";
  const button=document.getElementById("motionButton"), password=document.getElementById("password"), visibility=document.getElementById("passwordVisibility");
  const reduced=matchMedia("(prefers-reduced-motion: reduce)");
  let paused=false;try{paused=localStorage.getItem("nextops-motion")==="paused";}catch(_){}
  function label(key){return window.NextOpsView?.t(key) || ({pauseMotion:"Pause motion",resumeMotion:"Resume motion",staticMotion:"Static scene · reduced motion",showPassword:"Show password",hidePassword:"Hide password"}[key]);}
  function update(){const hidden=document.hidden || document.body.dataset.authenticated==="true";document.body.dataset.motion=paused || reduced.matches || hidden?"paused":"playing";button.setAttribute("aria-pressed",String(paused));button.querySelector("span").textContent=label(reduced.matches?"staticMotion":paused?"resumeMotion":"pauseMotion");button.disabled=reduced.matches;visibility.setAttribute("aria-label",label(password.type==="password"?"showPassword":"hidePassword"));}
  button.addEventListener("click",()=>{paused=!paused;try{localStorage.setItem("nextops-motion",paused?"paused":"playing");}catch(_){}update();});
  visibility.addEventListener("click",()=>{password.type=password.type==="password"?"text":"password";visibility.setAttribute("aria-pressed",String(password.type==="text"));update();});
  document.addEventListener("visibilitychange",update);reduced.addEventListener("change",update);
  window.NextOpsMotion={update,reset(){password.type="password";visibility.setAttribute("aria-pressed","false");update();}};
  update();
})();
