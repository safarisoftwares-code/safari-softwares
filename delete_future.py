# delete_future_placeholder.py - UTF-8. Remove the Future Project 1 placeholder card.
import io, sys

PATH = "index.html"
with io.open(PATH, "r", encoding="utf-8") as f:
    html = f.read()

orig_len = len(html)
marker = "Future Project 1"

idx = html.find(marker)
if idx == -1:
    print("[OK] Placeholder already deleted! (Not found in file).")
    sys.exit(0)

# Find the enclosing <div> block for this card
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

# Remove the block completely
html = html[:start] + html[end:]

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)

print("[OK] Successfully deleted 'Future Project 1' placeholder.")
print("[DONE] index.html written. bytes: %d -> %d" % (orig_len, len(html)))