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
| eMudhra CA | all Python services | YES | Redeploy refreshed CA trust store |
| certifi package | 1 old pin found | YES (Docs Recava) | Pinned to >=2026.10.20 |

### Redeployed Services (2026-10-23)
| Service | Render host | Status |
|---|---|---|
| Safari AI Pro | safari-ai-pro.co.ke | 200 OK |
| Safari AI Lite | lite.safari-ai-pro.co.ke | 200 OK |
| BuildCore (Brightline Electricals KE) | build-core.onrender.com | 200 OK |
| Shylock Capital | shylock-capital-ltd.onrender.com | 200 OK |
| Equipment Rental Manager | equips-renta.onrender.com | 200 OK |
| Docs Recava (safari-recoveries) | docs-recava.onrender.com | 200 OK |
| EPRA Exam Prep | epra-electrician-exam-prep.onrender.com | 200 OK |
| Boss & Watu Wamkono | direct-jobs-connection.onrender.com | 200 OK |

### eMudhra Context
- 8 intermediate CA private keys compromised (disclosed 2026-10-19)
- Forged leaf certs could impersonate any domain during exposure window
- No breach confirmed on Render. No exploit known against Safari Softwares.
- Mitigation: redeploy (fresh OS CA store) + certifi>=2026.10.20
- Monitor: browser trust status for eMudhra; possible CA/Browser Forum action
- Recommendation: do NOT purchase eMudhra-issued TLS certs for any future project

### 2026-10-23 (continued) — Docs Recava Auth Hardening

Ran pip-audit on Docs Recava backend. Found 3 vulnerabilities:
- ecdsa 0.19.2 (PYSEC-2026-1325 x2)
- python-jose 3.5.0 (PYSEC-2026-4298)

**Decision:** Migrate python-jose -> PyJWT (python-jose is semi-abandoned
with recurring CVEs; PyJWT is actively maintained and API-compatible).

**Changes (commit 6b1b3de in safari-recoveries repo):**
- backend/app/core/security.py:
  - `from jose import JWTError, jwt` -> `import jwt; from jwt.exceptions import InvalidTokenError as JWTError`
- backend/requirements.txt:
  - Removed python-jose==3.5.0, ecdsa==0.19.2
  - Added PyJWT>=2.15.0 (installed 2.15.1)
- Also bumped PyJWT from an initial 2.10.1 pin (which had 22 advisories)
  to >=2.15.0 (highest fix version required by any advisory)

**Verification:**
- Local token round-trip: TOKEN_OK + DECODE_OK (pass)
- pip-audit -r backend/requirements.txt -> No known vulnerabilities found
- Live: docs-recava.onrender.com -> HTTP 200
- Login flow tested in production (verified: dashboard loads with real user session, 1 document)
- Auth token creation & validation confirmed working end-to-end

**Result:** Docs Recava has zero known vulnerabilities in its Python dependency graph.
Combined with the earlier certifi>=2026.10.20 pin, the service is fully patched
against the 2026-10-23 Render advisory and its auth stack is on an actively-maintained library.

### Outstanding
- [x] Test login flow in production (confirmed 2026-10-23)
- [ ] Test token refresh after ~10 min idle (auto-refresh path)
- [ ] Consider datetime.utcnow() -> datetime.now(timezone.utc) in security.py
      (Python 3.12+ deprecation, not a security issue, future cleanup)

### References
- Render advisory: in customer email, 2026-10-23
- eMudhra disclosure: 2026-10-19
- Node.js patches: 22.23.4 / 24.22.1 / 26.12.1
- PHP patches: see PHP2Shell advisory