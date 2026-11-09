# patch_bible_rebrand.py - UTF-8. Update Bible Study Helper + Safari Reference Bible cards.
import io, sys, re

PATH = "index.html"
with io.open(PATH, "r", encoding="utf-8") as f:
    html = f.read()

orig_len = len(html)

NEW_APP   = "https://safarisoftwares-code.github.io/Bible-Study-Helper/"
NEW_BIBLE = "https://safarisoftwares-code.github.io/Bible-Study-Helper/bible.html"
NEW_REPO  = "https://github.com/safarisoftwares-code/Bible-Study-Helper"

# ---------- Replace Card 1: pastors-assistant ----------
old_card1_marker = 'id="pastors-assistant"'
idx = html.find(old_card1_marker)
if idx == -1:
    print("[ERR] pastors-assistant card not found"); sys.exit(1)

# find enclosing <div ...> ... </div> (the card). We locate the block by
# finding the opening div that contains the marker, then matching to its closing.
start = html.rfind('<div', 0, idx)
# naive depth match for divs
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
    print("[ERR] Could not match closing </div> for pastors-assistant"); sys.exit(1)

old_block = html[start:end]

# Preserve the exact class attribute (with unified-height already in it)
m_class = re.search(r'class="([^"]*)"', old_block)
old_class = m_class.group(1) if m_class else 'project-card'
# ensure unified-height stays
if 'unified-height' not in old_class:
    old_class += ' unified-height'

new_block = (
'<div id="pastors-assistant" class="' + old_class + '">\n'
'                    <div class="project-img" style="background:#1e40af; color:#dbeafe;">📖</div>\n'
'                    <div class="project-body">\n'
'                        <h3>Bible Study Helper</h3>\n'
'                        <p>A complete Bible study platform for everyone \u2014 not just pastors. Browse 24+ study topics with outlines and notes, and click any scripture reference to open the Safari Reference Bible in a new tab, auto-scrolled to that exact verse with a permanent green highlight. Rebranded from "Pastor\'s Sermon Assistant" and rebuilt from scratch for everyday church members and study groups.</p>\n'
'                        <div class="tech-tags">\n'
'                            <span class="tech-tag">Bible Study</span>\n'
'                            <span class="tech-tag" style="background:#f0fdf4; color:#166534; border:1px solid #22c55e;">\U0001F4D6 Bible Integrated</span>\n'
'                            <span class="tech-tag">Scripture Links</span>\n'
'                        </div>\n'
'                        <div class="project-links">\n'
'                            <a href="' + NEW_APP + '" target="_blank" rel="noopener" class="project-link">\U0001F310 Visit Live Site \u2197</a>\n'
'                            <a href="' + NEW_REPO + '" target="_blank" rel="noopener" class="project-link">\U0001F419 View on GitHub \u2197</a>\n'
'                            <a href="' + NEW_BIBLE + '" target="_blank" rel="noopener" class="project-link" style="color:#059669;">\U0001F4D6 Read the Bible \u2197</a>\n'
'                        </div>\n'
'                    </div>\n'
'                </div>'
)

html = html[:start] + new_block + html[end:]
print("[OK] pastors-assistant card rewritten as Bible Study Helper.")

# ---------- Replace Card 2: reference-bible (links + description) ----------
# Only touch this card's block
rb_idx = html.find('id="reference-bible"')
if rb_idx == -1:
    print("[ERR] reference-bible card not found"); sys.exit(1)
start = html.rfind('<div', 0, rb_idx)
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
if end == -1:
    print("[ERR] Could not match closing </div> for reference-bible"); sys.exit(1)

rb_block = html[start:end]

# Ensure unified-height present
m_class = re.search(r'class="([^"]*)"', rb_block)
if m_class and 'unified-height' not in m_class.group(1):
    rb_block = rb_block.replace(m_class.group(1), m_class.group(1) + ' unified-height', 1)
elif not m_class:
    rb_block = rb_block.replace('<div id="reference-bible"', '<div id="reference-bible" class="project-card unified-height"', 1)

# Repoint all old Pastors-Sermon-Assistant links to new Bible Study Helper paths
rb_block = rb_block.replace(
    'https://safarisoftwares-code.github.io/Pastors-Sermon-Assistant/bible.html',
    NEW_BIBLE)
rb_block = rb_block.replace(
    'https://safarisoftwares-code.github.io/Pastors-Sermon-Assistant/',
    NEW_APP)
# Relabel Sermon Assistant link
rb_block = rb_block.replace('\U0001F64F Sermon Assistant \u2197', '\U0001F4D6 Bible Study Helper \u2197')

# Enrich description (append the 16-verse restoration sentence)
if '16 missing verses' not in rb_block:
    rb_block = rb_block.replace(
        'and shareable verse URLs with auto-scroll highlighting.',
        'shareable verse URLs with auto-scroll highlighting, dark mode, font-size controls, and 16 missing WEB verses (including Acts 8:37) restored from KJV with perfect numbering alignment.',
        1)

html = html[:start] + rb_block + html[end:]
print("[OK] reference-bible card links + description updated.")

# ---------- Sanity: no old URLs left ----------
leftover = html.count('Pastors-Sermon-Assistant')
print("[CHECK] Remaining 'Pastors-Sermon-Assistant' references: %d" % leftover)
if leftover:
    print("[WARN] Old URLs still present \u2014 manual review needed.")

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)

print("[DONE] index.html written. bytes: %d -> %d" % (orig_len, len(html)))