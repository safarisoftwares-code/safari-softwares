# patch_add_ministry.py - UTF-8. Replace Future Project 1 with Heavenly Wonders Ministry.
import io, sys, re

PATH = "index.html"
with io.open(PATH, "r", encoding="utf-8") as f:
    html = f.read()

orig_len = len(html)

marker = "Future Project 1"
idx = html.find(marker)
if idx == -1:
    print("[ERR] 'Future Project 1' card not found. It may have already been replaced.")
    sys.exit(1)

start = html.rfind('<div', 0, idx)
depth = 0
i = start
end = -1
while i < len(html):
    if html.startswith('<div', i):
        depth += 1
        i += 4
    elif html.startswith('</div>', i):
        depth -= 1
        i += 6
        if depth == 0:
            end = i
            break
    else:
        i += 1

if end == -1:
    print("[ERR] Could not match closing </div> for Future Project 1")
    sys.exit(1)

new_card = (
'<div id="heavenly-wonders" class="project-card featured unified-height" style="background:linear-gradient(135deg,#ffffff,#fdf4ff); border:2px solid #c026d3;">\n'
'                    <div class="project-img" style="background:linear-gradient(135deg,#701a75,#c026d3); color:#fae8ff; font-size:3rem;">\n'
'                        \U0001F932\n'
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

html = html[:start] + new_card + html[end:]
print("[OK] Replaced 'Future Project 1' with Heavenly Wonders Ministry.")

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)

print("[DONE] index.html written.")