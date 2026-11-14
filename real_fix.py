# real_fix.py - UTF-8. Kills the ghost stretching and fixes Heavenly Wonders links.
import io, sys, re

PATH = "index.html"
with io.open(PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Fix the Heavenly Wonders card HTML so the links are inside the body
marker = 'id="heavenly-wonders"'
idx = html.find(marker)
if idx != -1:
    tech_tags_end = html.find('</div>', html.find('class="tech-tags"', idx)) + 6
    links_start = html.find('<div class="project-links">', idx)
    if links_start != -1:
        links_end = html.find('</div>', links_start) + 6
        links_block = html[links_start:links_end]
        # Rebuild the inner section so links are safely inside the body
        new_inner = '\n                        ' + links_block + '\n                    </div>\n                </div>'
        html = html[:tech_tags_end] + new_inner + html[links_end:]
        print("[OK] Fixed Heavenly Wonders HTML nesting.")

# 2. Replace the CSS with rules that prevent ghosting (no flex-grow on text)
css_start = html.find("/* --- UNIFORM CARD HEIGHT")
if css_start == -1:
    css_start = html.find("/* --- UNIFORM CARD HEIGHT")
    
# Find the end of the CSS block (just before the closing style tag)
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
        
        /* 1. Text and tags stay tight at the top (NO flex-grow) */
        .project-card.unified-height .project-body h3,
        .project-card.unified-height .project-body p,
        .project-card.unified-height .project-body .tech-tags {
            flex: 0 0 auto !important; 
            overflow-y: auto !important;
        }
        
        /* 2. The space between the tags and the links stretches to fill the gap */
        .project-card.unified-height .project-links { 
            flex: 1 1 auto !important;
            display: flex !important;
            flex-direction: column !important;
            justify-content: flex-end !important; /* Pushes the links to the bottom */
            margin-top: 0 !important; 
        }
    """
    html = html[:css_start] + new_css + html[css_end:]
    print("[OK] CSS updated. Text is tight, links stretch to fill the gap.")

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)
print("[DONE] index.html written.")