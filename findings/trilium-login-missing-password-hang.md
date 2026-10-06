# TriliumNext/Trilium — POST /login without a password hangs forever (unhandled rejection on null-result-handler routes)

- **Project:** TriliumNext/Trilium (self-hosted personal knowledge base, TypeScript/Express monorepo)
- **Issue:** [#11919](https://github.com/TriliumNext/Trilium/issues/11919) — filed 2026-10-06, 0 comments, unassigned, no competing PR
- **PR:** [#11920](https://github.com/TriliumNext/Trilium/pull/11920) — OPEN / MERGEABLE, commit 2247c1b GitHub-verified (SSH signature valid)
- **Bounty:** none posted on the issue; fix offered freely, tips welcome via the PR footer. $0 requested, $0 received.

## Bug

Any `POST /login` whose body has no `password` field never got a response — the request hung until the client/proxy timed out, and the app broadcast an "unhandled-error" over the websocket. Minor unauthenticated DoS: each such request pins a server socket (and an upstream proxy socket).

Cause (reported, confirmed in source at main 5775528c): `login` calls `verifyLoginCredentials(undefined, undefined)` → `passwordEncryptionService.verifyPassword(undefined)` → `scryptSync` throws a TypeError on the invalid argument. The throw becomes a rejected promise, and `internalRoute` (`apps/server/src/routes/route_api.ts`) returned early for routes registered with a `null` result handler — `if (!resultHandler) return;` — so the promise was never awaited and had no `.catch`. Three async routes are registered that way and all were exposed: `POST /login`, `POST /set-password` (e.g. a missing field makes `.trim()` throw), and `POST /api/llm-chat/stream`.

## Fix

- `apps/server/src/routes/route_api.ts`: in the no-result-handler branch, consume the handler's promise and route rejections to the existing `handleException` (logs the error; answers with the `HttpError` status or 500 unless the handler already sent a response) — mirroring what the result-handler branch already does.
- `apps/server/src/routes/login.ts`: a missing or non-string password is treated as a failed login — `401` via `sendLoginError`, so it counts toward the login rate limiter like a wrong password — instead of reaching scrypt with an invalid argument.

## Proof (red → green)

- New `route_api.spec.ts` describe ("internalRoute with no result handler"): unpatched, the rejecting-handler test **hangs until the vitest timeout** and vitest reports an **Unhandled Rejection** ("handler blew up") originating at `route_api.ts:98` — the reported bug reproduced exactly (suite: 1 failed / 14 passed). Patched, the route answers `500` with the error message, and a control handler that writes its own response is left untouched.
- New `login.spec.ts` case: `POST /login` with an empty body returns `401` (fixture app, real session/rate-limiter stack).
- Patched: `vitest run src/routes/route_api.spec.ts src/routes/login.spec.ts` — **33/33 pass**; `tsc -b` solution build clean.
- Local-run note (also in the PR): these specs import `session_secret`, which generates a secret via the crypto provider at import time if `spec/db/session_secret.txt` (gitignored) doesn't exist yet — a single-file run on a fresh checkout needs that file present, as it is once any app-building spec has run.

## Same-run sector-5 rejects

- chatwoot #16145 (automation-rule `andLOWER` SQL syntax error, filed today) → reporter's fix PR #16146 already open (timeline-verified); listmonk #3253 (GetList 2× subscriber_count) → fix PR #3255 already open; mealie #8635 already PR'd (#8636, known); twenty #27344 assigned + cross-referenced; medusa #17149 (held candidate, bug-vs-tradeoff + cache-invalidation design) and nocodb #14761 (held, heavy monorepo/proxy design) stand; coolify #12104 held (Laravel, infra repro); actual #9104 standing race reject; searxng #6819 engine rate-limit (network-bound); outline #13967 Android print CSS; logseq #13596 a bare security claim with no repro detail; appwrite #14143 PHP/heavy; mattermost #39013 email-content Go monorepo, unverified in one run.

## Watch (run 120)

NO changes: all PR states direct-verified identical to run 119 (dentalpin #599 / type-coverage #155 MERGED known; ERCs #2045 OPEN c=1, cake #3671 OPEN c=0, electrum #11012 OPEN c=0; optimism #23214 OPEN c=0, diffy #89 OPEN c=0, prysm #17626 OPEN c=1 (CLA-assistant = Kyle's step), memos #6435 OPEN c=2 reviews 1, NiceGUI #6372 OPEN c=1 reviews 4 (evnchn APPROVED stands — awaiting merge), vyper #5294 OPEN c=1 reviews 4, ansible #87642 OPEN c=1, vikunja #4107/#4110 OPEN c=0). Expensify identical: #102072 60, #101684 42, #102044 30, #102226 38 — no selection/hire, no melvin-bot prompt to Kshot3000. HackerOne: ledger-only. **NEW watch item: trilium PR #11920.** (Caught this run: a batched `gh api` loop reported dentalpin #599 / type-coverage #155 as OPEN/unmerged — direct individual calls prove both MERGED; the batched output was discarded, as in prior runs.)
