# fix_ministry_card.py - UTF-8. Restore the body content to Heavenly Wonders card.
import io, sys

PATH = "index.html"
with io.open(PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Find the Heavenly Wonders card
marker = 'id="heavenly-wonders"'
idx = html.find(marker)
if idx == -1:
    print("[ERR] Heavenly Wonders card not found.")
    sys.exit(1)

# Find the image div inside this card
start = html.find('<div class="project-img"', idx)
# Find the closing div of the image div (we know it's empty now)
end = html.find('</div>', start) + 6

# The full correct card content
full_card = (
'<div id="heavenly-wonders" class="project-card featured unified-height" style="background:linear-gradient(135deg,#ffffff,#fdf4ff); border:2px solid #c026d3;">\n'
'                    <div class="project-img" style="background-image: url(\'images/ministry-header.png\'); background-size: cover; background-position: center 20%; border-bottom: 2px solid #c026d3;">\n'
'                    </div>\n'
'                    <div class="project-body">\n'
'                        <h3 style="color:#701a75;">Heavenly Wonders Ministry</h3>\n'
'                        <p>A complete digital ecosystem for a ministry, featuring a public-facing website and a secure, unified admin dashboard. Includes a sermon library, testimony approvals, prayer requests, newsletter subscription with protected JSON storage, and a PWA for mobile installs. Built with PHP.</p>\n'
'                        <div class="tech-tags">\n'
'                            <span class="tech-tag" style="background:#fdf4ff; color:#701a75; border:1px solid #c026d3;">\U0001F418 PHP</span>\n'
'                            <span class="tech-tag" style="background:#fdf4ff; color:#701a75; border:1px solid #c026d3;">\U0001F510 Admin Dashboard</span>\n'
'                            <span class="tech-tag" style="background:#fdf4ff; color:#701a75; border:1px solid #c026d3;">\U0001F4F1 PWA</span>\n'
'                            <span class="tech-tag" style="background:#fdf4ff; color:#701a75; border:1px solid #c026d3;">\u26EA Ministry</span>\n'
'                        </div>\n'
'                        <div class="project-links">\n'
'                            <a href="https://heavenlywonders.co.ke" target="_blank" rel="noopener" class="project-link" style="color:#c026d3;">\U0001F310 Visit Live Site \u2197</a>\n'
'                            <a href="https://heavenlywonders.co.ke/dashboard.html" target="_blank" rel="noopener" class="project-link" style="color:#c026d3;">\U0001F510 View Dashboard \u2197</a>\n'
'                        </div>\n'
'                    </div>\n'
'                </div>'
)

# We replace the entire block from the start of the ID to the end of the broken image div
html = html[:start] + full_card + html[end:]

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)

print("[OK] Restored full body content to Heavenly Wonders card.")