# fix_recava_size.py - UTF-8. Removes the bad class and enforces strict height.
import io, sys

PATH = "index.html"
with io.open(PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Fix the HTML error on Docs Recava
# It currently says: <div class="project-body unified-height">
# We change it to: <div class="project-body">
html = html.replace('<div class="project-body unified-height">', '<div class="project-body">')
print("[OK] Removed accidental 'unified-height' class from Docs Recava body.")

# 2. Enforce the exact size via CSS, overriding any flexbox stretching
css_start = html.find("/* --- UNIFORM CARD HEIGHT")
css_end = html.find("</style>", css_start)

if css_start != -1 and css_end != -1:
    new_css = """
        /* --- UNIFORM CARD HEIGHT --- */
        :root { --uniform-card-h: calc(420px + 3.2cm); }
        
        /* Force ALL cards in the grid to this exact height */
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
        
        /* The body expands, but doesn't push the card bigger */
        .project-card.unified-height .project-body { 
            flex: 1 1 auto !important; 
            display: flex !important;
            flex-direction: column !important;
            overflow: hidden !important; 
            padding: 1.5rem !important;
        }
        
        /* The text takes up available space and scrolls if too long */
        .project-card.unified-height .project-body p {
            flex: 1 1 auto !important; 
            overflow-y: auto !important;
            margin-bottom: 0 !important;
        }
        
        /* Links stay pinned to the bottom */
        .project-card.unified-height .project-links { 
            flex: 0 0 auto !important;
            margin-top: auto !important; 
            padding-top: 10px !important;
        }
    """
    html = html[:css_start] + new_css + html[css_end:]
    print("[OK] CSS strictly enforces height and text scrolling.")

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)
print("[DONE] index.html written.")