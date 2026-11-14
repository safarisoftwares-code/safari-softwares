# exact_layout_fix.py - UTF-8. Fix Heavenly Wonders HTML nesting and enforce strict heights.
import io, sys

PATH = "index.html"
with io.open(PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Fix the HTML nesting for Heavenly Wonders
marker = 'id="heavenly-wonders"'
idx = html.find(marker)
if idx != -1:
    # Find the tech-tags closing div and the project-body closing div
    tech_tags_end = html.find('</div>', html.find('class="tech-tags"', idx)) + 6
    
    # Look for the links block
    links_start = html.find('<div class="project-links">', idx)
    links_end = html.find('</div>', links_start) + 6
    
    if links_start != -1:
        # Grab the links block
        links_block = html[links_start:links_end]
        # Remove the prematurely closed divs and the floating links
        # We replace the space between tech_tags_end and links_end
        # with just the links, properly nested inside project-body
        new_inner = '\n                        ' + links_block + '\n                    </div>\n                </div>'
        
        # The text between tech_tags_end and links_end currently has the stray </div>
        html = html[:tech_tags_end] + new_inner + html[links_end:]
        print("[OK] Fixed Heavenly Wonders HTML nesting (links moved inside project-body).")

# 2. Update CSS to strictly force flex behavior on the text
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
            padding: 1.5rem !important;
        }
        
        /* This forces long text (like Docs Recava) to scroll without expanding the card */
        .project-card.unified-height .project-body p {
            flex: 1 1 auto !important; 
            overflow-y: auto !important;
            margin-bottom: 0 !important;
        }
        
        .project-card.unified-height .project-links { 
            margin-top: auto !important; 
            padding-top: 10px !important;
        }
    """
    html = html[:css_start] + new_css + html[css_end:]
    print("[OK] CSS hard-enforced: strict heights, scrolling text, bottom links.")

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)
print("[DONE] index.html written.")