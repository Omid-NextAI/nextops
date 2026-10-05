/* Decorative motion preferences only; no credential, pointer or keystroke tracking. */
(() => {
  "use strict";

  const button = document.getElementById("motionButton");
  const password = document.getElementById("password");
  const visibility = document.getElementById("passwordVisibility");
  if (!button || !password || !visibility) return;

  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)");
  const fallbackLabels = {
    pauseMotion: "Pause motion",
    resumeMotion: "Resume motion",
    staticMotion: "Static scene · reduced motion",
    showPassword: "Show password",
    hidePassword: "Hide password",
  };
  let paused = false;
  try {
    paused = localStorage.getItem("nextops-motion") === "paused";
  } catch { /* Restricted preference storage must not prevent login. */ }

  function label(key) {
    return window.NextOpsView?.t(key) || fallbackLabels[key];
  }

  function update() {
    // A visual pause is not a session state and never changes authentication.
    const authenticated = document.body.dataset.authenticated === "true";
    const reason = authenticated ? "authenticated" : document.hidden ? "hidden"
      : reduced.matches ? "reduced" : paused ? "preference" : "playing";
    document.body.dataset.motion = reason === "playing" ? "playing" : "paused";
    document.body.dataset.motionReason = reason;
    // Pause/resume must not restart the entrance and make already-readable copy disappear.
    // An interrupted entrance resolves immediately to the composed, readable still state.
    if (reason !== "playing") document.body.dataset.motionIntro = "complete";

    const action = label(reduced.matches ? "staticMotion" : paused ? "resumeMotion" : "pauseMotion");
    button.querySelector("span").textContent = action;
    button.title = action;
    button.setAttribute("aria-pressed", String(paused));
    button.disabled = reduced.matches;
    // Reuse the existing local icon sprite; no remote icons or assets.
    button.querySelector("use")?.setAttribute("href", paused ? "#i-chevron" : "#i-pause");
    visibility.setAttribute("aria-label", label(password.type === "password" ? "showPassword" : "hidePassword"));
  }

  button.addEventListener("click", () => {
    paused = !paused;
    try {
      localStorage.setItem("nextops-motion", paused ? "paused" : "playing");
    } catch { /* Keep a usable tab-local preference when storage is restricted. */ }
    update();
  });
  visibility.addEventListener("click", () => {
    password.type = password.type === "password" ? "text" : "password";
    visibility.setAttribute("aria-pressed", String(password.type === "text"));
    update();
  });
  document.addEventListener("visibilitychange", update);
  reduced.addEventListener("change", update);
  window.addEventListener("pageshow", update);

  window.NextOpsMotion = {
    update,
    reset() {
      password.type = "password";
      visibility.setAttribute("aria-pressed", "false");
      update();
    },
  };
  update();
})();
