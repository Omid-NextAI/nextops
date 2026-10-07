/* Static company identity. Visibility control never changes authentication or tracks input. */
(() => {
  "use strict";
  const password=document.getElementById("password");
  const visibility=document.getElementById("passwordVisibility");
  if(!password || !visibility)return;
  function update(){
    const shown=password.type==="text";
    const fa=document.documentElement.lang==="fa";
    visibility.setAttribute("aria-label",fa?(shown?"پنهان‌کردن گذرواژه":"نمایش گذرواژه"):(shown?"Hide password":"Show password"));
    visibility.setAttribute("aria-pressed",String(shown));
  }
  visibility.addEventListener("click",()=>{password.type=password.type==="password"?"text":"password";update();});
  window.NextOpsMotion={update,reset(){password.type="password";update();}};
  update();
})();
