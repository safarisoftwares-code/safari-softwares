# rebalance_cards.py - UTF-8. Swap Heavenly Wonders and Reference Bible positions.
import io, sys, re

PATH = "index.html"
with io.open(PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Helper function to extract and remove a card by its ID
def extract_card(html, card_id):
    marker = 'id="' + card_id + '"'
    idx = html.find(marker)
    if idx == -1:
        return html, None
    start = html.rfind('<div', 0, idx)
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
    card_html = html[start:end]
    # Ensure it has unified-height
    if 'unified-height' not in card_html:
        card_html = card_html.replace('class="project-card', 'class="project-card unified-height', 1)
    return html[:start] + html[end:], card_html

# 1. Extract both cards
html, ministry_card = extract_card(html, 'heavenly-wonders')
html, bible_card = extract_card(html, 'reference-bible')

if not ministry_card or not bible_card:
    print("[ERR] Could not find one or both cards. Aborting.")
    sys.exit(1)

print("[OK] Extracted Heavenly Wonders and Safari Bible cards.")

# 2. Re-insert Safari Reference Bible right after Ngili Calendar
ngili_marker = 'id="ngili-calendar"'
idx = html.find(ngili_marker)
if idx == -1:
    print("[ERR] Ngili Calendar not found. Cannot place Bible.")
    sys.exit(1)

# Find the end of the Ngili calendar card
start = html.rfind('<div', 0, idx)
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

html = html[:end] + '\n' + bible_card + html[end:]
print("[OK] Inserted Safari Bible right after Ngili Calendar.")

# 3. Re-insert Heavenly Wonders back into the grid (right after Safari POS System, or wherever it looks balanced)
pos_marker = 'id="safari-pos-system"'
idx = html.find(pos_marker)
if idx == -1:
    # Fallback: insert before the closing of the first portfolio-grid
    grid_end = html.find('</div>', html.find('id="ngili-calendar"')) 
    html = html[:grid_end] + ministry_card + html[grid_end:]
else:
    start = html.rfind('<div', 0, idx)
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
    html = html[:end] + '\n' + ministry_card + html[end:]

print("[OK] Re-inserted Heavenly Wonders into the grid.")

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)

print("[DONE] index.html written. Grid rebalanced.")