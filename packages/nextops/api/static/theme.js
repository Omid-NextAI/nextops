// Apply a local-only preference before styles paint. No account data is stored here.
(() => {
  const media = window.matchMedia("(prefers-color-scheme: dark)");
  let explicit = null;
  try {
    const value = localStorage.getItem("nextops-theme");
    if (value === "light" || value === "dark") explicit = value;
  } catch { /* Restricted storage must not prevent using the app. */ }

  function apply(theme) {
    document.documentElement.dataset.theme = theme;
    document.documentElement.style.colorScheme = theme;
    const color = document.querySelector('meta[name="theme-color"]');
    if (color) color.content = theme === "dark" ? "#101b20" : "#007986";
    updateControl();
  }

  function updateControl() {
    const button = document.getElementById("themeButton");
    if (!button) return;
    const dark = document.documentElement.dataset.theme === "dark";
    const fa = document.documentElement.lang === "fa";
    button.setAttribute("aria-pressed", String(dark));
    button.setAttribute("aria-label", fa ? "پوستهٔ تیره" : "Dark theme");
    button.title = fa ? (dark ? "استفاده از پوستهٔ روشن" : "استفاده از پوستهٔ تیره")
      : (dark ? "Use light theme" : "Use dark theme");
    button.querySelector("span").textContent = button.title;
    document.dispatchEvent(new Event("nextops-theme-change"));
  }

  window.NextOpsTheme = { updateControl };
  apply(explicit || (media.matches ? "dark" : "light"));
  media.addEventListener("change", () => {
    if (!explicit) apply(media.matches ? "dark" : "light");
  });
  document.addEventListener("DOMContentLoaded", () => {
    updateControl();
    document.getElementById("themeButton").addEventListener("click", () => {
      explicit = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
      try { localStorage.setItem("nextops-theme", explicit); } catch { /* Tab-only fallback. */ }
      apply(explicit);
    });
  });
})();
