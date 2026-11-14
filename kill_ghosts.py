# kill_ghosts.py - UTF-8. Fixes the ghosting by grouping content tightly and fixing Heavenly Wonders HTML.
import io, sys

PATH = "index.html"
with io.open(PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Fix the Heavenly Wonders card HTML (put links back INSIDE the body)
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
        print("[OK] Fixed Heavenly Wonders HTML nesting (no more floating links).")

# 2. Update CSS to prevent ghosting (group content tight, push extra space to the bottom)
css_start = html.find("/* --- UNIFORM CARD HEIGHT (Management Systems & ERPs downward) --- */")
css_end = html.find("</style>")

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
        
        /* THIS KILLS THE GHOSTS: Wrap text/tags tightly at the top */
        .project-card.unified-height .project-body-content {
            flex: 0 1 auto !important; 
            display: flex;
            flex-direction: column;
            overflow-y: auto; /* Scrolls if too long */
        }
        
        /* This takes up the empty space so the text doesn't stretch */
        .project-card.unified-height .project-spacer {
            flex: 1 1 auto !important;
        }
        
        /* Push the links to the very bottom */
        .project-card.unified-height .project-links { 
            flex: 0 0 auto !important;
            margin-top: 10px !important; 
        }
    """
    html = html[:css_start] + new_css + html[css_end:]
    print("[OK] CSS updated to kill ghosts (grouped content).")

# 3. Wrap the inner content of all unified cards in a content div and add a spacer
# This requires a regex to find <h3>...</h3> up to <div class="project-links"> and wrap it
def wrap_content(match):
    inner_text = match.group(1)
    return f'<div class="project-body-content">{inner_text}</div><div class="project-spacer"></div>'

# Find all unified cards and wrap their inner text/tags
pattern = r'(<h3.*?</h3>.*?<div class="tech-tags">.*?</div>)'
# We only apply this to the unified cards to be safe
parts = html.split('<div class="project-card')
for i in range(1, len(parts)):
    if 'unified-height' in parts[i][:100]:
        parts[i] = re.sub(pattern, wrap_content, parts[i], count=1, flags=re.DOTALL)
html = '<div class="project-card'.join(parts)
print("[OK] Wrapped all card contents to prevent stretching.")

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)
print("[DONE] index.html written.")