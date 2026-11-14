# final_uniform_fix.py - UTF-8. Enforce strict grid limits and fix Heavenly Wonders bottom links.
import io, sys

PATH = "index.html"
with io.open(PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Enforce the strict card height and body scrolling in CSS
# We replace the old CSS block with a bulletproof one.
css_start = html.find("/* --- UNIFORM CARD HEIGHT (Management Systems & ERPs downward) --- */")
css_end = html.find("</style>")

if css_start != -1 and css_end != -1:
    new_css = """
        /* --- UNIFORM CARD HEIGHT (Management Systems & ERPs downward) --- */
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
        }
        
        /* Force the paragraph to scroll if it's too long (fixes Docs Recava) */
        .project-card.unified-height .project-body p {
            flex: 1 1 auto !important; 
            overflow-y: auto !important;
            margin-bottom: 0 !important;
        }
        
        /* Push the links to the very bottom (fixes Heavenly Wonders design) */
        .project-card.unified-height .project-links { 
            margin-top: auto !important; 
            padding-top: 10px !important;
        }
    """
    html = html[:css_start] + new_css + html[css_end:]
    print("[OK] CSS updated: Strict height, scrolling text, bottom-aligned links.")

# 2. Fix the JS measurement (override it so it doesn't mess with our fixed size)
html = html.replace(
    "document.documentElement.style.setProperty('--uniform-card-h', 'calc(420px + 2cm)');",
    "document.documentElement.style.setProperty('--uniform-card-h', 'calc(420px + 3.2cm)');"
)
html = html.replace(
    "document.documentElement.style.setProperty('--uniform-card-h', max + 'px');",
    "document.documentElement.style.setProperty('--uniform-card-h', 'calc(420px + 3.2cm)');"
)

# 3. Fix the links block in Heavenly Wonders to ensure it has the exact same classes
marker = 'id="heavenly-wonders"'
idx = html.find(marker)
if idx != -1:
    start = html.find('<div class="project-links">', idx)
    if start != -1:
        end = html.find('</div>', start) + 6
        # Replace with perfectly formatted links
        correct_links = (
'<div class="project-links">\n'
'                            <a href="https://heavenlywonders.co.ke" target="_blank" rel="noopener" class="project-link" style="color:#c026d3;">\U0001F310 Visit Website \u2197</a>\n'
'                            <a href="https://github.com/safarisoftwares-code/Bible-Study-Helper" target="_blank" rel="noopener" class="project-link" style="color:#c026d3;">\U0001F419 View on GitHub \u2197</a>\n'
'                        </div>'
        )
        html = html[:start] + correct_links + html[end:]
        print("[OK] Heavenly Wonders links fixed and bottom-aligned.")

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)
print("[DONE] index.html written.")