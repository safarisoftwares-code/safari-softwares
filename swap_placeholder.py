# swap_placeholder.py - UTF-8. Safely moves Heavenly Wonders to Future 1's slot.
import io, sys

PATH = "index.html"
with io.open(PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Locate the Heavenly Wonders card and DELETE it from its current (floating) position
marker_hw = 'id="heavenly-wonders"'
idx_hw = html.find(marker_hw)

if idx_hw != -1:
    start_hw = html.rfind('<div', 0, idx_hw)
    depth = 0
    i = start_hw
    end_hw = -1
    while i < len(html):
        if html.startswith('<div', i):
            depth += 1; i += 4
        elif html.startswith('</div>', i):
            depth -= 1; i += 6
            if depth == 0:
                end_hw = i; break
        else:
            i += 1
    # Remove it from the file
    html = html[:start_hw] + html[end_hw:]
    print("[OK] Removed floating Heavenly Wonders card.")
else:
    print("[INFO] Heavenly Wonders card not currently in file, proceeding to insert.")

# 2. Locate the Future Project 1 placeholder and replace it
marker_fp = '<!-- Future Project 1 -->'
idx_fp = html.find(marker_fp)

if idx_fp == -1:
    print("[ERR] Could not find '<!-- Future Project 1 -->' comment.")
    sys.exit(1)

# Find the enclosing <div> of the placeholder
start_fp = idx_fp # Start at the comment
depth = 0
i = html.find('<div', idx_fp)
# We actually just want to grab the div directly AFTER the comment
start_fp = i
end_fp = -1
while i < len(html):
    if html.startswith('<div', i):
        depth += 1; i += 4
    elif html.startswith('</div>', i):
        depth -= 1; i += 6
        if depth == 0:
            end_fp = i; break
    else:
        i += 1

if end_fp == -1:
    print("[ERR] Could not match closing </div> for Future Project 1.")
    sys.exit(1)

# The perfectly structured Heavenly Wonders card (links properly nested inside project-body)
new_card = (
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
'                            <a href="https://heavenlywonders.co.ke" target="_blank" rel="noopener" class="project-link" style="color:#c026d3;">\U0001F310 Visit Website \u2197</a>\n'
'                            <a href="https://github.com/safarisoftwares-code/Bible-Study-Helper" target="_blank" rel="noopener" class="project-link" style="color:#c026d3;">\U0001F419 View on GitHub \u2197</a>\n'
'                        </div>\n'
'                    </div>\n'
'                </div>'
)

# Replace the placeholder block (including the comment) with the new card
html = html[:idx_fp] + new_card + html[end_fp:]
print("[OK] Inserted Heavenly Wonders into the Future Project 1 slot.")

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)
print("[DONE] index.html written.")