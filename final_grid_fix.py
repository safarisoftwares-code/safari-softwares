# final_grid_fix.py - UTF-8. Restore Heavenly Wonders, delete Future placeholder.
import io, sys, re

PATH = "index.html"
with io.open(PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. DELETE THE PLACEHOLDER (comment + div)
# We look for the exact block starting with the comment and ending before the next card.
placeholder_pattern = r'<!-- Future Project 1 -->.*?</div>\s*</div>\s*</div>'
html, n = re.subn(placeholder_pattern, '', html, flags=re.DOTALL)
if n > 0:
    print("[OK] Removed 'Future Project 1' placeholder block.")
else:
    print("[WARN] 'Future Project 1' block not found via regex. Manual check needed.")

# 2. RESTORE HEAVENLY WONDERS (if it got deleted in the previous step)
if 'id="heavenly-wonders"' not in html:
    print("[INFO] Heavenly Wonders card missing. Re-injecting...")
    # Find Safari POS System card to insert it right after
    pos_marker = 'id="safari-pos-system"'
    pos = html.find(pos_marker)
    if pos != -1:
        # Find the end of the POS card
        start = html.rfind('<div', 0, pos)
        depth = 0; i = start; end = -1
        while i < len(html):
            if html.startswith('<div', i):
                depth += 1; i += 4
            elif html.startswith('</div>', i):
                depth -= 1; i += 6
                if depth == 0:
                    end = i; break
            else:
                i += 1
        
        # Build the card
        ministry_card = (
'                <div id="heavenly-wonders" class="project-card featured unified-height" style="background:linear-gradient(135deg,#ffffff,#fdf4ff); border:2px solid #c026d3;">\n'
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
'                </div>\n'
        )
        html = html[:end] + ministry_card + html[end:]
        print("[OK] Heavenly Wonders card restored.")
else:
    print("[OK] Heavenly Wonders card is already present.")

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)

print("[DONE] index.html written.")