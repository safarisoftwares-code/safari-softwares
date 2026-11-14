# clean_investigation_fix.py - UTF-8. Removes the accidental class from the body.
import io, sys

PATH = "index.html"
with io.open(PATH, "r", encoding="utf-8") as f:
    html = f.read()

# We only replace the exact string that is breaking Docs Recava.
bad_html = '<div class="project-body unified-height">'
good_html = '<div class="project-body">'

if bad_html in html:
    html = html.replace(bad_html, good_html)
    print("[OK] Removed 'unified-height' from the inner project-body.")
else:
    print("[WARN] Could not find the bad class string. Maybe it was already fixed?")

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)
print("[DONE] index.html written.")