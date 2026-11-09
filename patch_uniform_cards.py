# patch_uniform_cards.py - UTF-8. Uniform card height from Management Systems & ERPs downward.
import re, io, sys

PATH = "index.html"
with io.open(PATH, "r", encoding="utf-8") as f:
    html = f.read()

orig_len = len(html)

css_block = """
        /* --- UNIFORM CARD HEIGHT (Management Systems & ERPs downward) --- */
        :root { --uniform-card-h: 420px; }
        .project-card.unified-height {
            height: var(--uniform-card-h) !important;
            min-height: 380px !important;
            max-height: none !important;
            display: flex !important;
            flex-direction: column !important;
            overflow: hidden !important;
        }
        .project-card.unified-height.trim-half-cm {
            height: calc(var(--uniform-card-h) - 0.5cm) !important;
        }
        .project-card.unified-height .project-body { flex: 1 1 auto !important; overflow: hidden !important; }
        .project-card.unified-height .project-body p {
            flex: 1 1 auto !important; overflow-y: auto !important;
        }
        .project-card.unified-height .project-links { margin-top: auto !important; }
"""

if "UNIFORM CARD HEIGHT" not in html:
    html = html.replace("    </style>", css_block + "    </style>", 1)
    print("[OK] CSS block inserted.")
else:
    print("[SKIP] CSS block already present.")

anchor = "\U0001F3E2 Management Systems & ERPs"
pos = html.find(anchor)
if pos == -1:
    print("[ERR] Anchor not found. Aborting.")
    sys.exit(1)

head, tail = html[:pos], html[pos:]

def tag_card(m):
    cls = m.group(1)
    if "unified-height" in cls:
        return m.group(0)
    return 'class="' + cls + ' unified-height"'

tail_new, n = re.subn(r'class="(project-card[^"]*)"', tag_card, tail)
print("[OK] Cards tagged in tail: %d" % n)

for cid in ('id="watcher-premium"', 'id="watcher"'):
    idx = tail_new.find(cid)
    if idx == -1:
        print("[WARN] %s not found" % cid); continue
    m = re.search(r'class="([^"]*)"', tail_new[idx:idx+400])
    if m and "trim-half-cm" not in m.group(1):
        newcls = m.group(1) + " trim-half-cm"
        tail_new = tail_new[:idx+m.start(1)] + newcls + tail_new[idx+m.end(1):]
        print("[OK] trim-half-cm added to %s" % cid)

html = head + tail_new

js_block = """
        // UNIFORM CARD HEIGHT: measure tallest unified card, apply to all
        (function() {
            function applyUniformHeight() {
                var cards = document.querySelectorAll('.project-card.unified-height');
                if (!cards.length) return;
                document.documentElement.style.setProperty('--uniform-card-h', 'auto');
                cards.forEach(function(c){ c.style.height = 'auto'; });
                var max = 0;
                cards.forEach(function(c){
                    if (c.classList.contains('trim-half-cm')) return;
                    max = Math.max(max, c.getBoundingClientRect().height);
                });
                if (max < 380) max = 380;
                document.documentElement.style.setProperty('--uniform-card-h', max + 'px');
                cards.forEach(function(c){ c.style.height = ''; });
                console.log('[uniform] card height =', max, 'px');
            }
            if (document.fonts && document.fonts.ready) {
                document.fonts.ready.then(applyUniformHeight);
            }
            window.addEventListener('load', applyUniformHeight);
            window.addEventListener('resize', function(){
                clearTimeout(window.__uhT); window.__uhT = setTimeout(applyUniformHeight, 200);
            });
        })();
"""

if "UNIFORM CARD HEIGHT: measure tallest" not in html:
    html = html.replace("    </script>\n</body>", js_block + "    </script>\n</body>", 1)
    print("[OK] JS block inserted.")
else:
    print("[SKIP] JS block already present.")

with io.open(PATH, "w", encoding="utf-8", newline="") as f:
    f.write(html)

print("[DONE] index.html written. bytes: %d -> %d" % (orig_len, len(html)))
print("Next: verify, test locally, deploy.")