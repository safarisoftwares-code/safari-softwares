# fix_heavenly_links.py - UTF-8. Move Heavenly Wonders before Bible, apply correct links.
import io, sys, re

PATH = "index.html"
with io.open(PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Helper: Extract a card by ID
def extract_card(html, card_id):
    marker = 'id="' + card_id + '"'
    idx = html.find(marker)
    if idx == -1: return html, None
    start = html.rfind('<div', 0, idx)
    depth = 0; i = start; end = -1
    while i < len(html):
        if html.startswith('<div', i): depth += 1; i += 4
        elif html.startswith('</div>', i):
            depth -= 1; i += 6
            if depth == 0: end = i; break
        else: i += 1
    return html[:start] + html[end:], html[start:end]

# 1. Clean up the accidental links injected into Safari Bible in the previous step
bible_idx = html.find('id="reference-bible"')
if bible_idx != -1:
    # Remove the mistakenly injected links block
    html = html.replace(
        '\n                        <div class="project-links">\n                            <a href="https://safarisoftwares-code.github.io/Bible-Study-Helper/bible.html" target="_blank" rel="noopener" class="project-link" style="color:#059669;">\U0001F4D6 Read the Bible \u2197</a>\n                            <a href="https://safarisoftwares-code.github.io/Bible-Study-Helper/" target="_blank" rel="noopener" class="project-link" style="color:#4a1d6e;">\U0001F4D6 Bible Study Helper \u2197</a>\n                        </div>',
        '', 1
    )

# 2. Extract Heavenly Wonders
html, ministry_card = extract_card(html, 'heavenly-wonders')
if not ministry_card:
    print("[ERR] Heavenly Wonders card not found.")
    sys.exit(1)

# 3. Apply the correct links to Heavenly Wonders
# We replace whatever links it currently has with the correct ones.
if 'class="project-links"' in ministry_card:
    start_links = ministry_card.find('<div class="project-links">')
    end_links = ministry_card.find('</div>', start_links) + 6
    ministry_card = ministry_card[:start_links] + '' + ministry_card[end_links:]

correct_links = (
'<div class="project-links">\n'
'                            <a href="https://heavenlywonders.co.ke" target="_blank" rel="noopener" class="project-link" style="color:#c026d3;">\U0001F310 Visit Website \u2197</a>\n'
'                            <a href="https://github.com/safarisoftwares-code/Bible-Study-Helper" target="_blank" rel="noopener" class="project-link" style="color:#c026d3;">\U0001F419 View on GitHub \u2197</a>\n'
'                        </div>'
)

# Insert the correct links just before the end of the project-body
body_end = ministry_card.rfind('</div>\n                    </div>')
if body_end == -1:
    body_end = ministry_card.rfind('</div>')
ministry_card = ministry_card[:body_end] + '\n                        ' + correct_links + '\n                    ' + ministry_card[body_end:]
print("[OK] Correct links applied to Heavenly Wonders.")

# 4. Insert Heavenly Wonders exactly before the Safari Reference Bible
bible_idx = html.find('id="reference-bible"')
if bible_idx == -1:
    print("[ERR] Safari Reference Bible not found.")
    sys.exit(1)

start_bible = html.rfind('<div', 0, bible_idx)
html = html[:start_bible] + ministry_card + '\n                ' + html[start_bible:]
print("[OK] Heavenly Wonders moved to sit just before Safari Reference Bible.")

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)
print("[DONE] index.html written.")