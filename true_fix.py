# true_fix.py - UTF-8. Removes JS measurement and enforces scrolling on Docs Recava.
import io, sys, re

PATH = "index.html"
with io.open(PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove the buggy JavaScript measurement block entirely
# We find the script from "// UNIFORM CARD HEIGHT: measure tallest" down to "})();"
js_start = html.find("// UNIFORM CARD HEIGHT: measure tallest")
js_end = html.find("})();", js_start) + 5
if js_start != -1 and js_end != -1:
    html = html[:js_start] + "// JS measurement removed - using strict CSS heights\n" + html[js_end:]
    print("[OK] Removed buggy JavaScript measurement loop.")

# 2. Ensure the CSS rules force the text to scroll and not stretch the card
css_start = html.find("/* --- UNIFORM CARD HEIGHT --- */")
css_end = html.find("</style>", css_start)

if css_start != -1 and css_end != -1:
    new_css = """
        /* --- UNIFORM CARD HEIGHT --- */
        :root { --uniform-card-h: calc(420px + 3.2cm); }
        
        .project-card.unified-height {
            height: var(--uniform-card-h) !important;
            min-height: var(--uniform-card-h) !important;
            max-height: var(--uniform-card-h) !important;
            display: flex !important;
            flex-direction: column !important;
            overflow: hidden !important;
        }
        
        .project-card.unified-height.trim-half-cm {
            height: calc(var(--uniform-card-h) - 0.5cm) !important;
            min-height: calc(var(--uniform-card-h) - 0.5cm) !important;
            max-height: calc(var(--uniform-card-h) - 0.5cm) !important;
        }
        
        .project-card.unified-height .project-body {
            flex: 1 1 auto !important;
            display: flex !important;
            flex-direction: column !important;
            overflow: hidden !important;
            padding: 1.5rem !important;
        }
        
        /* This forces the text (like Docs Recava) to scroll inside the card */
        .project-card.unified-height .project-body p {
            flex: 1 1 auto !important;
            overflow-y: auto !important;
            margin-bottom: 0 !important;
        }
        
        .project-card.unified-height .project-links {
            flex: 0 0 auto !important;
            margin-top: auto !important;
            padding-top: 10px !important;
        }
    """
    html = html[:css_start] + new_css + html[css_end:]
    print("[OK] CSS updated to strictly enforce height and text scrolling.")

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)
print("[DONE] index.html written.")