# fix_recava.py - UTF-8. Ensure Docs Recava has the unified-height class.
import io, sys

PATH = "index.html"
with io.open(PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Find the Docs Recava heading
marker = 'Docs Recava'
idx = html.find(marker)

if idx == -1:
    print("[ERR] Docs Recava not found.")
    sys.exit(1)

# Find the start of its card (search backwards for the div)
start = html.rfind('<div', 0, idx)
# Find the class attribute of that div
class_start = html.find('class="', start) + 7
class_end = html.find('"', class_start)
current_classes = html[class_start:class_end]

if 'unified-height' not in current_classes:
    new_classes = current_classes + ' unified-height'
    html = html[:class_start] + new_classes + html[class_end:]
    print("[OK] Added unified-height class to Docs Recava.")
else:
    print("[OK] Docs Recava already has unified-height class.")

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)
print("[DONE] index.html written.")