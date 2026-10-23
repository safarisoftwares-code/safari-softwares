# 🔐 Security Log

## 2026-10-23 — Render Security Advisory (CLOSED ✅)

**Advisories:**
- eMudhra CA compromise (private keys for 8 intermediate certs)
- Node.js TLS/hostname-check bypass + Brotli RCE
- PHP2Shell (unauth RCE + memory read)

### Impact Assessment
| Component | In stack? | Affected? | Resolution |
|---|---|---|---|
| Node.js | ❌ none | n/a | n/a |
| PHP | ❌ none | n/a | n/a |
| eMudhra CA | ⚠️ all Python services | YES | Redeploy refreshed CA trust store |
| `certifi` package | ⚠️ 1 old pin found | YES (Docs Recava) | Pinned to `>=2026.10.20` |

### Redeployed Services (2026-10-23)
| Service | Render host | Status |
|---|---|---|
| Safari AI Pro | safari-ai-pro.co.ke | ✅ 200 |
| Safari AI Lite | lite.safari-ai-pro.co.ke | ✅ 200 |
| BuildCore (Brightline Electricals KE) | build-core.onrender.com | ✅ 200 |
| Shylock Capital | shylock-capital-ltd.onrender.com | ✅ 200 |
| Equipment Rental Manager | equips-renta.onrender.com | ✅ 200 |
| Docs Recava (safari-recoveries) | docs-recava.onrender.com | ✅ 200 |
| EPRA Exam Prep | epra-electrician-exam-prep.onrender.com | ✅ 200 |
| Boss & Watu Wamkono | direct-jobs-connection.onrender.com | ✅ 200 |

### Certifi Pinning
- `Safari-Recoveries/backend/requirements.txt` line 10: `certifi>=2026.10.20`
- Commit: `c565039` — "Security: pin certifi>=2026.10.20 (eMudhra CA advisory)"
- Docs Recava confirmed live: `HTTP 200 in 1.29s`

### Notes
- Render confirmed **no breaches/compromises** — advisory was precautionary
- All services verified 200 post-redeploy
- Render free-tier cold-starts (occasional `000` on first request) — normal, not a bug
- Other repos: no `certifi` pin → pip pulls latest at build time (safe default)

### Outstanding (non-urgent)
- [ ] Optional: add `certifi>=2026.10.20` to all other repos for reproducibility
- [ ] Safari AI Lite rate limiting (protect LLM API budget — future)

### References
- Render advisory: in customer email, 2026-10-23
- eMudhra disclosure: 2026-10-19
- Node.js patches: 22.23.4 / 24.22.1 / 26.12.1
- PHP patches: see PHP2Shell advisory