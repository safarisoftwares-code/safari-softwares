# patch_add_image.py - UTF-8. Swap gradient for image in Heavenly Wonders card.
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

# Locate the .project-img div inside this card
start = html.find('<div class="project-img"', idx)
end = html.find('</div>', start) + 6
if start == -1 or end == 5:
    print("[ERR] Could not find .project-img inside the card.")
    sys.exit(1)

# Construct the new image div (uses the renamed image, adds cover to fill the 82px space)
new_img_div = (
'<div class="project-img" style="background-image: url(\'images/ministry-header.png\'); '
'background-size: cover; background-position: center 20%; border-bottom: 2px solid #c026d3;">'
'</div>'
)

# Replace the old gradient div with the new image div
html = html[:start] + new_img_div + html[end:]
print("[OK] Swapped gradient for image in Heavenly Wonders card.")

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)

print("[DONE] index.html written.")