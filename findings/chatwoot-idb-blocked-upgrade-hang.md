# chatwoot/chatwoot — dashboard stores never load when another tab blocks the IndexedDB cache upgrade

- **Issue:** https://github.com/chatwoot/chatwoot/issues/16163 (filed 2026-10-06, 0 comments, unassigned, no competing PR at submission time)
- **PR:** https://github.com/chatwoot/chatwoot/pull/16165 — OPEN / MERGEABLE, commit `e09e711` (GitHub-verified)
- **Sector:** (5) web/other OSS — run 170, 2026-10-06

## Bug

`DataManager.initDb()` (`app/javascript/dashboard/helper/CacheHelper/DataManager.js`) called `openDB(name, DATA_VERSION, { upgrade })` with no `blocked` / `blocking` handlers. When another tab still holds the database at the older version (a tab left open across the v4.17.1 → v4.18.0 deploy, which bumped `DATA_VERSION`), the new tab's open is blocked: an IndexedDB open blocked by a version change neither resolves nor rejects. `CacheEnabledApiClient.getFromCache()` only falls back to the network when `initDb()` *rejects*, so `inboxes` / `labels` / `teams` reads stalled before any network request — empty sidebar stores, and no attachment/voice-recorder button in the reply box (`inboxes/getInbox` returns `{}`).

## Proof (red → green, real file)

Standalone harness loading the **real** `DataManager.js` against `fake-indexeddb` v6 + `idb` v8 (the repo's own versions; the repo vitest setup uses `fake-indexeddb/auto` the same way), two connections per database; the only shim is the extensionless `./version` import and a `localStorage` stub:

- Pristine: scenario 1 (old connection holds v1, never closes) — `initDb()` **pending past 2.5 s** (the reported hang); scenario 2 (open patched-version connection, then a newer open at `DATA_VERSION + 1`) — upgrade **pending past 2.5 s**.
- Patched: scenario 1 — `initDb()` **rejects immediately** with "Opening cw-store-acct1 is blocked by another tab holding an older version", and a retry after the old tab closes succeeds at `DATA_VERSION`; scenario 2 — the newer upgrade **resolves immediately**; normal push/get/replace/setCacheKeys behaviour unchanged; harness re-run green twice.

## Fix

In `initDb()` only (+40/−1, `DataManager.js`): pass `blocked` (rejects the open attempt, so existing callers degrade to their network fallback) and `blocking` (this connection closes itself when a newer tab wants to upgrade) handlers to `openDB`; a blocked open that later goes through in the background is closed again if nothing adopted it, so it cannot block the next upgrade. Per the repo's AGENTS.md, the change is kept to the single production file (no new spec files); the harness above is the verification.

Honest limitation (disclosed in the PR): the full vitest suite was not run locally — it needs the full monorepo pnpm install in this environment; CI is authoritative.

## Payment

No bounty posted on #16163; fix offered freely with tips welcome via the PR footer. $0 requested, $0 received.
