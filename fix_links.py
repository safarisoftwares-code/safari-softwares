# fix_bible_links.py - UTF-8. Restore the missing links to the Safari Reference Bible card.
import io, sys

PATH = "index.html"
with io.open(PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Find the Safari Reference Bible card
marker = 'id="reference-bible"'
idx = html.find(marker)
if idx == -1:
    print("[ERR] Safari Reference Bible card not found.")
    sys.exit(1)

# Find the closing of the project-body inside this card
start = html.find('<div class="project-body">', idx)
end_body = html.find('</div>\n                </div>', start)
if end_body == -1:
    # Try finding the exact match based on our previous re-insert
    end_body = html.find('</div>', start) 

# Let's just insert the links before the last closing divs of the card
# First, find where the tech-tags end
tag_end = html.find('</div>', html.find('class="tech-tags"', idx)) + 6

# Build the links block
links_block = (
'\n                        <div class="project-links">\n'
'                            <a href="https://safarisoftwares-code.github.io/Bible-Study-Helper/bible.html" target="_blank" rel="noopener" class="project-link" style="color:#059669;">\U0001F4D6 Read the Bible \u2197</a>\n'
'                            <a href="https://safarisoftwares-code.github.io/Bible-Study-Helper/" target="_blank" rel="noopener" class="project-link" style="color:#4a1d6e;">\U0001F4D6 Bible Study Helper \u2197</a>\n'
'                        </div>'
)

# Check if links already exist (just in case)
if 'Bible-Study-Helper/bible.html' not in html[start:tag_end+500]:
    html = html[:tag_end] + links_block + html[tag_end:]
    print("[OK] Links restored to Safari Reference Bible card.")
else:
    print("[OK] Links already present.")

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)

print("[DONE] index.html written.")