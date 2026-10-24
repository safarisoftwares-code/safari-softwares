# 📦 Safari Softwares — Portfolio Reference

> Canonical list of all live projects. Last updated 2026-10-24.
> **Naming gotcha:** Docs Recava repo = `safari-recoveries` (not "recova").
> **Boss & Watu:** repo = `direct-connection`, domain = `direct-jobs-connection`.
> **BuildCore** is deployed as **Brightline Electricals Kenya** (personal business instance).

## ✅ Live & Verified

| # | Project | Live URL | Repo | Stack | Notes |
|---|---------|----------|------|-------|-------|
| 1 | Safari AI Pro | safari-ai-pro.co.ke | safari-ai-pro | Python · FastAPI · SQLAlchemy · JS · JWT · AI/LLM | Guest counter, JWT auth, chat history, feedback modal |
| 2 | Safari AI Agent (Lite) | lite.safari-ai-pro.co.ke | safari-ai-agent | Python · AI · Chatbot · API · Web Search | Also at safari-ai-agent.onrender.com. Stateless by design (no DB). |
| 3 | **Safari POS System** ⭐ | (no public URL) | safari-pos-system | FastAPI · JS · POS · Cash · M-Pesa | **Featured**. Card renamed from "Safari POS Lite". Card/Credit removed. |
| 4 | **BuildCore — Construction ERP** ⭐ | build-core.onrender.com | Construction-ERP-Software | Python · Flask · PostgreSQL · Payroll · AI Assistant | **Featured**. Deployed as **Brightline Electricals Kenya** (personal instance). |
| 5 | Equipment Rental Manager | equips-renta.onrender.com | equipment-rental-manager | Rental · Inventory | |
| 6 | The Ngili Calendar | safarisoftwares-code.github.io/The-Ngili-Calendar/ | The-Ngili-Calendar | Calendar · Scheduling | |
| 7 | Docs Recava | docs-recava.onrender.com | **safari-recoveries** | Python · FastAPI · PostgreSQL · JS · Privacy · Kenya | DPA 2019 compliance. PyJWT>=2.15.0, certifi>=2026.10.20. Zero known vulns. |
| 8 | EPRA Electrician Exam Prep | epra-electrician-exam-prep.onrender.com/ | epra-electrician-exam-prep | Education · Exam Prep · Kenya | |
| 9 | Chemistry Practical Simulator | safarisoftwares-code.github.io/kenyan-chemistry-practical-simulator/ | kenyan-chemistry-practical-simulator | Education · Simulation · Kenya | |
| 10 | Pastor's Sermon Assistant | safarisoftwares-code.github.io/Pastors-Sermon-Assistant/ | Pastors-Sermon-Assistant | Ministry · Productivity | |
| 11 | Boss & Watu Wamkono | direct-jobs-connection.onrender.com | **direct-connection** | Networking · Jobs | |
| 12 | Memory Game | safarisoftwares-code.github.io/memory-game/ | memory-game | Game · Frontend | |
| 13 | Shylock Capital (Loan Manager) | shylock-capital-ltd.onrender.com | loan-manager | Fintech · Loans | Cold-start on free tier |
| 14 | Hospital Manager | (no public URL) | hospital-manager | Healthcare · Management | |
| 15 | Cleantex Dry Cleaners | (no public URL) | Cleantex-Dry-Cleaners | Business · POS | |
| 16 | Wallpaper Manager | (no public URL) | wallpaper-manager | Media · Management | |

## 🧩 Placeholder Cards (on live site)

Four transparent dashed-border cards fill grid gaps in "Management Systems" and "Document Management" categories. **Intentional** — not leftovers.

| Card | Label | Link | Purpose |
|------|-------|------|---------|
| Future Project 1 | Coming Soon | (none) | Grid balance |
| Future Project 2 | Coming Soon | (none) | Grid balance |
| Future Project 3 | Coming Soon | (none) | Grid balance |
| Future Project 4 | Coming Soon | (none) | Grid balance |

⚠️ These have `project-card` class (required for search feature) but no `id` — search ignores them, layout uses them.

## 🗑️ Removed from Site

| Project | Reason | Date |
|---------|--------|------|
| Safari POS Pro | GitHub repo deleted (returned 404) | 2026-10-24 |

## 🎨 Site Features (current state)

- **PWA v2.0** — service worker with network-first HTML strategy
- **Refresh App button** — manual cache clear + reload in nav menu
- **Install button** — hides when PWA is installed (localStorage check)
- **Search feature** — DOM-scans `.project-card` elements; new projects must have this class
- **Contact section** — two equal cards: form (#f8fafc) + info (#fffbf5)
- **Hero CTA** — "Ready to start your project? →" pill button scrolls to contact

## 🔍 SEO Status

- ✅ Google — site indexed, appears in search
- ✅ Bing — site indexed (sitemap Success)
- ✅ **Google AI Overview** recognizes "Safari Softwares (Kenya)" as distinct entity from Apple Safari
- ✅ IndexNow key `a02d45861bf79ec3` + `ping-bing.bat` workflow active
- ✅ `sitemap.xml` + `robots.txt` live and submitted to GSC

## 🔮 Upcoming (assigned to other chats)

| Project | Status | Notes |
|---------|--------|-------|
| BuildStock (Multi-Stock Taking) | In planning (separate chat) | BLUE palette (Navy #1e3a8a, Royal #2563eb). Kenyan SMEs. 90-day MVP target. **Not worked on in this chat.** |
| Mobile Apps (TWA) | Planned | Convert PWAs to Play Store apps. |

---

**Verified by:** `curl.exe -s -o NUL -w "%{http_code}"` health check on 2026-10-23.
**Last updated:** 2026-10-24 (POS Pro removed, POS System renamed, BuildCore featured, placeholders added).
**Maintenance:** Re-run health check before each major site update.