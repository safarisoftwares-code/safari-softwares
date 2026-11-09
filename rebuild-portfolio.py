import io
import re

path = r"C:\Users\HomePC\Desktop\safari-softwares-website\index.html"

with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Apply the strict CSS (Reduce header by 1.8cm, force uniform height)
css = """
        /* --- FINAL REBUILD CSS --- */
        .project-img {
            height: 82px !important; /* Reduced by 1.8cm */
            min-height: 82px !important;
            font-size: 2rem !important;
        }
        .project-card {
            display: flex !important;
            flex-direction: column !important;
            height: 325px !important; 
            min-height: 325px !important;
            max-height: 325px !important;
            overflow: hidden !important; 
        }
        .project-body {
            flex: 1 1 auto !important;
            display: flex !important;
            flex-direction: column !important;
            overflow: hidden !important;
            padding: 15px !important;
        }
        .project-body p {
            flex: 1 1 auto !important;
            overflow-y: auto !important;
            font-size: 0.85rem !important;
        }
        .project-body p::-webkit-scrollbar { width: 3px; }
        .project-body p::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 3px; }
        .project-links {
            margin-top: auto !important;
            padding-top: 10px !important;
            font-size: 0.8rem !important;
        }
"""
if "/* --- FINAL REBUILD CSS --- */" not in content:
    content = content.replace('</style>', css + '\n    </style>')

# 2. Define the clean HTML for ALL categories
new_portfolio_html = '''
            <!-- AI & Advanced Solutions -->
            <span class="subsection-label">🤖 AI & Advanced Solutions</span>
            <div class="portfolio-grid">
                <div id="safari-ai-pro" class="project-card featured">
                    <div class="project-img" style="background:linear-gradient(135deg,#78350f,#d97706); color:#fef3c7;">🦁</div>
                    <div class="project-body">
                        <h3>Safari AI Pro</h3>
                        <p>A professional, modular AI agent with advanced reasoning, multi-source web search, voice input, document upload (PDF/DOCX), JWT authentication, server-side guest limits, multi-chat tabs, admin panel, and user dashboard. Production-ready.</p>
                        <div class="tech-tags"><span class="tech-tag">Python</span><span class="tech-tag">FastAPI</span><span class="tech-tag">AI/LLM</span></div>
                        <div class="project-links">
                            <a href="https://safari-ai-pro.co.ke" target="_blank" class="project-link">🌐 Visit Live Site ↗</a>
                            <a href="https://github.com/safarisoftwares-code/safari-ai-pro" target="_blank" class="project-link">🐙 View on GitHub ↗</a>
                        </div>
                    </div>
                </div>
                <div id="safari-ai-agent" class="project-card">
                    <div class="project-img" style="background:#1e3a8a; color:#bfdbfe;">🤖</div>
                    <div class="project-body">
                        <h3>Safari AI Agent (Lite)</h3>
                        <p>A professional AI-powered chatbot agent for data retrieval, web search, and API integration. Built with Python for seamless AI interactions.</p>
                        <div class="tech-tags"><span class="tech-tag">Python</span><span class="tech-tag">Chatbot</span></div>
                        <div class="project-links">
                            <a href="https://lite.safari-ai-pro.co.ke" target="_blank" class="project-link">🌐 Visit Live Site ↗</a>
                            <a href="https://github.com/safarisoftwares-code/safari-ai-agent" target="_blank" class="project-link">🐙 View on GitHub ↗</a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Management Systems -->
            <span class="subsection-label">🏢 Management Systems & ERPs</span>
            <div class="portfolio-grid">
                <div id="safari-pos-system" class="project-card featured">
                    <div class="project-img" style="background:linear-gradient(135deg,#ffffff,#fff7ed); color:#d97706; font-size:3rem;">🛒</div>
                    <div class="project-body">
                        <h3>Safari POS System</h3>
                        <p>The complete Point of Sale solution. Features barcode scanner support, stock protection, multiple payment methods (Cash, M-Pesa), KRA-compliant receipts with VAT, and full backup & restore. Built with FastAPI + JavaScript.</p>
                        <div class="tech-tags"><span class="tech-tag">FastAPI</span><span class="tech-tag">M-Pesa</span><span class="tech-tag">KRA</span></div>
                        <div class="project-links">
                            <a href="https://github.com/safarisoftwares-code/safari-pos-system" target="_blank" class="project-link">🐙 View on GitHub ↗</a>
                        </div>
                    </div>
                </div>
                <div id="buildcore" class="project-card featured">
                    <div class="project-img" style="background:linear-gradient(135deg,#ffffff,#fef3c7); color:#b45309; font-size:3rem;">🏗️</div>
                    <div class="project-body">
                        <h3>BuildCore — Construction ERP</h3>
                        <p>Connecting the Jobsite to the Office. Full construction and electrical management in one platform: projects, worker payroll, materials, invoicing with tax, and an AI-powered assistant.</p>
                        <div class="tech-tags"><span class="tech-tag">Python</span><span class="tech-tag">Flask</span><span class="tech-tag">PostgreSQL</span></div>
                        <div class="project-links">
                            <a href="https://build-core.onrender.com" target="_blank" class="project-link">🌐 Visit Live Site ↗</a>
                            <a href="https://github.com/safarisoftwares-code/Construction-ERP-Software" target="_blank" class="project-link">🐙 View on GitHub ↗</a>
                        </div>
                    </div>
                </div>
                <div id="hospital-manager" class="project-card">
                    <div class="project-img" style="background:#1e293b; color:#94a3b8;">🏥</div>
                    <div class="project-body">
                        <h3>Hospital Manager</h3>
                        <p>A hospital management system handling patient records, appointments, billing, and staff management — designed for clinics and small hospitals.</p>
                        <div class="tech-tags"><span class="tech-tag">Healthcare</span><span class="tech-tag">Management</span></div>
                        <div class="project-links">
                            <a href="https://github.com/safarisoftwares-code/hospital-manager" target="_blank" class="project-link">🐙 View on GitHub ↗</a>
                        </div>
                    </div>
                </div>
                <div id="shylock-capital" class="project-card">
                    <div class="project-img" style="background:#3b0764; color:#e9d5ff;">💰</div>
                    <div class="project-body">
                        <h3>Shylock Capital (Loan Manager)</h3>
                        <p>A loan tracking and management system with borrower records, repayment schedules, interest calculations, and automated reminders.</p>
                        <div class="tech-tags"><span class="tech-tag">Fintech</span><span class="tech-tag">Loans</span></div>
                        <div class="project-links">
                            <a href="https://shylock-capital-ltd.onrender.com" target="_blank" class="project-link">🌐 Visit Live Site ↗</a>
                            <a href="https://github.com/safarisoftwares-code/loan-manager" target="_blank" class="project-link">🐙 View on GitHub ↗</a>
                        </div>
                    </div>
                </div>
                <div id="equipment-rental" class="project-card">
                    <div class="project-img" style="background:#78350f; color:#fcd34d;">🔧</div>
                    <div class="project-body">
                        <h3>Equipment Rental Manager</h3>
                        <p>A system for managing equipment rental businesses — inventory tracking, booking calendar, customer management, and rental history.</p>
                        <div class="tech-tags"><span class="tech-tag">Rental</span><span class="tech-tag">Inventory</span></div>
                        <div class="project-links">
                            <a href="https://equips-renta.onrender.com/" target="_blank" class="project-link">🌐 Visit Live Site ↗</a>
                            <a href="https://github.com/safarisoftwares-code/equipment-rental-manager" target="_blank" class="project-link">🐙 View on GitHub ↗</a>
                        </div>
                    </div>
                </div>
                <div id="cleantex" class="project-card">
                    <div class="project-img" style="background:#1e40af; color:#bfdbfe;">👔</div>
                    <div class="project-body">
                        <h3>Cleantex Dry Cleaners</h3>
                        <p>A management system for a dry cleaning business — order tracking, customer notifications, pickup/delivery scheduling, and invoicing.</p>
                        <div class="tech-tags"><span class="tech-tag">Business</span><span class="tech-tag">POS</span></div>
                        <div class="project-links">
                            <a href="https://github.com/safarisoftwares-code/Cleantex-Dry-Cleaners" target="_blank" class="project-link">🐙 View on GitHub ↗</a>
                        </div>
                    </div>
                </div>
                <div id="ngili-calendar" class="project-card">
                    <div class="project-img" style="background:#4c1d95; color:#ddd6fe;">📅</div>
                    <div class="project-body">
                        <h3>The Ngili Calendar</h3>
                        <p>A custom calendar and scheduling application with event management, reminders, and a clean interface for personal or organizational use.</p>
                        <div class="tech-tags"><span class="tech-tag">Calendar</span><span class="tech-tag">Scheduling</span></div>
                        <div class="project-links">
                            <a href="https://safarisoftwares-code.github.io/The-Ngili-Calendar/" target="_blank" class="project-link">🌐 Visit Live Site ↗</a>
                            <a href="https://github.com/safarisoftwares-code/The-Ngili-Calendar" target="_blank" class="project-link">🐙 View on GitHub ↗</a>
                        </div>
                    </div>
                </div>
                <div id="reference-bible" class="project-card" style="position:relative; border:2px solid #059669; background:linear-gradient(135deg,#ffffff,#ecfdf5);">
                    <div style="position:absolute; top:12px; right:12px; background:#059669; color:white; padding:4px 10px; border-radius:999px; font-size:0.7rem; font-weight:700; letter-spacing:0.5px; z-index:2;">📖 SAFARI BIBLE</div>
                    <div class="project-img" style="background:linear-gradient(135deg, #064e3b, #059669); color:#ecfdf5; font-size:3rem;">📖</div>
                    <div class="project-body">
                        <h3>Safari Reference Bible</h3>
                        <p>A completely ad-free, offline-ready Bible application. Features 31,102 verses in both World English Bible (WEB) and King James Version (KJV). Includes instant search, dark mode, and shareable verse URLs with auto-scroll highlighting.</p>
                        <div class="tech-tags"><span class="tech-tag">31,102 Verses</span><span class="tech-tag">WEB & KJV</span><span class="tech-tag">Zero Tracking</span></div>
                        <div class="project-links">
                            <a href="https://safarisoftwares-code.github.io/Pastors-Sermon-Assistant/bible.html" target="_blank" class="project-link" style="color:#059669;">📖 Read the Bible ↗</a>
                            <a href="https://safarisoftwares-code.github.io/Pastors-Sermon-Assistant/" target="_blank" class="project-link" style="color:#4a1d6e;">🙏 Sermon Assistant ↗</a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Document Management & Dev Tools -->
            <span class="subsection-label">🔐 Document Management & Dev Tools</span>
            <div class="portfolio-grid">
                <div id="docs-recava" class="project-card featured">
                    <div class="project-img" style="background:linear-gradient(135deg,#78350f,#d97706); color:#fef3c7;">🪪</div>
                    <div class="project-body">
                        <h3>Docs Recava</h3>
                        <p>Track your documents, get expiry reminders, and recover lost ones — anonymously. Register IDs, passports, licences, and permits; get reminders before each expires; and if one is lost, connect anonymously.</p>
                        <div class="tech-tags"><span class="tech-tag">Python</span><span class="tech-tag">FastAPI</span><span class="tech-tag">PostgreSQL</span></div>
                        <div class="project-links">
                            <a href="https://docs-recava.onrender.com" target="_blank" class="project-link">🌐 Visit Live Site ↗</a>
                            <a href="https://github.com/safarisoftwares-code/safari-recoveries" target="_blank" class="project-link">🐙 View on GitHub ↗</a>
                        </div>
                    </div>
                </div>
                <div id="watcher-premium" class="project-card featured" style="background:linear-gradient(135deg,#fffbeb,#fef3c7); border:2px solid #d4a017; position:relative;">
                    <div style="position:absolute; top:0; left:0; right:0; height:4px; background:linear-gradient(90deg,#d4a017,#fbbf24,#d4a017); z-index:3;"></div>
                    <div style="position:absolute; top:12px; right:12px; background:#d4a017; color:white; padding:4px 10px; border-radius:999px; font-size:0.7rem; font-weight:700; letter-spacing:0.5px; z-index:2;">👑 PREMIUM</div>
                    <div class="project-img" style="background:linear-gradient(135deg,#b45309,#d97706); color:#fef3c7; font-size:3rem;">🛠️</div>
                    <div class="project-body">
                        <h3>Watcher Premium</h3>
                        <p>Pro monitoring with email alerts. Built on Watcher's zero-data-collection architecture — plus private workspaces, sub-5-minute pings, and instant DOWN/RECOVERED notifications via branded HTML email (Resend).</p>
                        <div class="tech-tags"><span class="tech-tag">Cloudflare Workers</span><span class="tech-tag">D1</span><span class="tech-tag">Resend</span></div>
                        <div class="project-links">
                            <a href="https://watcher.safari-pos.co.ke/" target="_blank" class="project-link">🌐 Visit Live Site ↗</a>
                            <a href="https://github.com/safarisoftwares-code/watcher" target="_blank" class="project-link">🐙 View on GitHub ↗</a>
                        </div>
                    </div>
                </div>
                <div id="watcher" class="project-card featured" style="background:linear-gradient(135deg,#ffffff,#f5f3ff); border:2px solid #8b5cf6; position:relative;">
                    <div style="position:absolute; top:12px; left:12px; background:#8b5cf6; color:white; padding:4px 10px; border-radius:999px; font-size:0.7rem; font-weight:700; letter-spacing:0.5px; z-index:2;">🛠️ DEVELOPER TOOL</div>
                    <div class="project-img" style="background:linear-gradient(135deg,#8b5cf6,#6366f1); color:white; font-size:3rem;">🛠️</div>
                    <div class="project-body">
                        <h3>Watcher</h3>
                        <p>Proprietary infrastructure keep-alive service for free-tier hosted apps. Custom Cloudflare Workers + D1 dashboard pings apps on a schedule to prevent cold-start sleep. Zero-cost, zero-data-collection architecture.</p>
                        <div class="tech-tags"><span class="tech-tag">Cloudflare Workers</span><span class="tech-tag">D1</span><span class="tech-tag">SSRF</span></div>
                        <div class="project-links">
                            <a href="https://watcher.safari-pos.co.ke/" target="_blank" class="project-link">🌐 Visit Live Site ↗</a>
                            <a href="https://github.com/safarisoftwares-code/watcher" target="_blank" class="project-link">🐙 View on GitHub ↗</a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Educational & Other -->
            <span class="subsection-label">🎓 Educational & Other Projects</span>
            <div class="portfolio-grid">
                <div id="epra-prep" class="project-card">
                    <div class="project-img" style="background:#1e3a8a; color:#bfdbfe;">⚡</div>
                    <div class="project-body">
                        <h3>EPRA Electrician Exam Prep</h3>
                        <p>An exam preparation platform for electricians taking the EPRA certification in Kenya — practice questions, mock exams, and progress tracking.</p>
                        <div class="tech-tags"><span class="tech-tag">Education</span><span class="tech-tag">Exam Prep</span></div>
                        <div class="project-links">
                            <a href="https://epra-electrician-exam-prep.onrender.com/" target="_blank" class="project-link">🌐 Visit Live Site ↗</a>
                            <a href="https://github.com/safarisoftwares-code/epra-electrician-exam-prep" target="_blank" class="project-link">🐙 View on GitHub ↗</a>
                        </div>
                    </div>
                </div>
                <div id="chemistry-sim" class="project-card">
                    <div class="project-img" style="background:#0f766e; color:#ccfbf1;">🧪</div>
                    <div class="project-body">
                        <h3>Kenyan Chemistry Practical Simulator</h3>
                        <p>An interactive simulator for Kenyan chemistry practical exams — virtual lab experiments, step-by-step procedures, and practice for students.</p>
                        <div class="tech-tags"><span class="tech-tag">Education</span><span class="tech-tag">Simulation</span></div>
                        <div class="project-links">
                            <a href="https://safarisoftwares-code.github.io/kenyan-chemistry-practical-simulator/" target="_blank" class="project-link">🌐 Visit Live Site ↗</a>
                            <a href="https://github.com/safarisoftwares-code/kenyan-chemistry-practical-simulator" target="_blank" class="project-link">🐙 View on GitHub ↗</a>
                        </div>
                    </div>
                </div>
                <div id="pastors-assistant" class="project-card">
                    <div class="project-img" style="background:#4a1d6e; color:#d8b4fe;">🙏</div>
                    <div class="project-body">
                        <h3>Pastor's Sermon Assistant</h3>
                        <p>A complete sermon preparation platform with 24 study topics, outlines, and a built-in Reference Bible integration. Click any scripture reference to open the verse instantly.</p>
                        <div class="tech-tags"><span class="tech-tag">Ministry</span><span class="tech-tag" style="background:#f0fdf4; color:#166534; border:1px solid #22c55e;">📖 Bible Integrated</span></div>
                        <div class="project-links">
                            <a href="https://safarisoftwares-code.github.io/Pastors-Sermon-Assistant/" target="_blank" class="project-link">🌐 Visit Live Site ↗</a>
                            <a href="https://github.com/safarisoftwares-code/Pastors-Sermon-Assistant" target="_blank" class="project-link">🐙 View on GitHub ↗</a>
                        </div>
                    </div>
                </div>
                <div id="wallpaper-manager" class="project-card">
                    <div class="project-img" style="background:#1e1b4b; color:#c4b5fd;">🖼️</div>
                    <div class="project-body">
                        <h3>Wallpaper Manager</h3>
                        <p>A wallpaper management application — organize, categorize, and manage wallpaper collections with tagging and search functionality.</p>
                        <div class="tech-tags"><span class="tech-tag">Media</span><span class="tech-tag">Management</span></div>
                        <div class="project-links">
                            <a href="https://github.com/safarisoftwares-code/wallpaper-manager" target="_blank" class="project-link">🐙 View on GitHub ↗</a>
                        </div>
                    </div>
                </div>
                <div id="boss-watu" class="project-card">
                    <div class="project-img" style="background:#1e293b; color:#94a3b8;">🤝</div>
                    <div class="project-body">
                        <h3>Boss & Watu Wamkono</h3>
                        <p>A direct jobs connection platform linking employers with skilled manual workers — peer-to-peer connections, job matching, and messaging.</p>
                        <div class="tech-tags"><span class="tech-tag">Networking</span><span class="tech-tag">Jobs</span></div>
                        <div class="project-links">
                            <a href="https://direct-jobs-connection.onrender.com" target="_blank" class="project-link">🌐 Visit Live Site ↗</a>
                            <a href="https://github.com/safarisoftwares-code/direct-connection" target="_blank" class="project-link">🐙 View on GitHub ↗</a>
                        </div>
                    </div>
                </div>
                <div id="memory-game" class="project-card">
                    <div class="project-img" style="background:#3b0764; color:#e9d5ff;">🧠</div>
                    <div class="project-body">
                        <h3>Memory Game</h3>
                        <p>An interactive memory card matching game — fun, responsive, and built with clean code. A demonstration of front-end development skills.</p>
                        <div class="tech-tags"><span class="tech-tag">Game</span><span class="tech-tag">Frontend</span></div>
                        <div class="project-links">
                            <a href="https://safarisoftwares-code.github.io/memory-game/" target="_blank" class="project-link">🌐 Visit Live Site ↗</a>
                            <a href="https://github.com/safarisoftwares-code/memory-game" target="_blank" class="project-link">🐙 View on GitHub ↗</a>
                        </div>
                    </div>
                </div>
            </div>
'''

# 3. Find the whole portfolio section and replace it
# We look for the first subsection label and the final closing div of the portfolio section
pattern = re.compile(r'<!-- AI & Advanced Solutions -->.*?</div>\s*<!-- Placeholder for future project -->.*?</div>\s*</div>\s*</div>', re.DOTALL)
# Fallback if placeholders were removed: match from the first subsection label to the 'View all repositories' link
pattern_fallback = re.compile(r'(<span class="subsection-label">🤖 AI & Advanced Solutions</span>).*?(<a href="https://github.com/safarisoftwares-code" target="_blank" class="cta-button">)', re.DOTALL)

if pattern.search(content):
    content = pattern.sub(new_portfolio_html + '\n\n            ', content)
    print("SUCCESS: Replaced entire portfolio grid (found full block).")
elif pattern_fallback.search(content):
    content = pattern_fallback.sub(r'\1\n' + new_portfolio_html + '\n\n            ' + r'\2', content)
    print("SUCCESS: Replaced entire portfolio grid (found fallback block).")
else:
    print("ERROR: Could not find the portfolio section to replace.")

with io.open(path, "w", encoding="utf-8", newline="") as f:
    f.write(content)
print("Done! File saved.")