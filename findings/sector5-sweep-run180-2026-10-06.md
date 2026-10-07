# Sector 5 (web / other OSS) sweep — run 180, 2026-10-06

**Result: NO submission.** Status watch: no changes (85 open PRs; Expensify
61/43/33/38 identical, #102072 latest still the melvin-bot overdue nudge —
not a contributor-details prompt; all tracked PRs OPEN/MERGEABLE at known
heads; held items identical). $0 requested, $0 received.

## Deep-check 1 — karakeep-app/karakeep #3145 (REST 401 after mobile pairing)

Filed 2026-10-05 by enzomaximusuniversal, 0 comments, unassigned, no
competing PR. Symptom: after `apiKeys.exchange` (mobile pairing), every
`/api/v1/*` request 401s for all keys (incl. newly created ones), persists
across restarts, while tRPC clients validate the same keys fine.

Code audit at v0.33.2 (reporter's version) and main:

- REST 401s come from `packages/api/middlewares/auth.ts` when `ctx.user`
  is null; ctx is built once for both REST and tRPC in
  `apps/web/app/api/[[...route]]/route.ts` via `createContextFromRequest`,
  which calls the shared `authenticateApiKey` (`packages/trpc/auth.ts`) and
  falls through to cookie auth on any throw.
- Scope failures are 403, not 401 (`apiKeyScopes.ts`, scoped procedures in
  `packages/trpc/index.ts`); rate limiting is 429. `authenticateApiKey`
  itself is per-key (keyId lookup + sha256/bcrypt compare) — nothing in
  `exchange`/`generateApiKey` mutates other keys, the user row, or any
  shared persistent state that the REST path depends on and the tRPC path
  does not.
- The next-auth → better-auth migration (#3140, 2026-10-04) landed a day
  before the reporter's image pull but is not in v0.33.2's auth path for
  API keys (`client.ts` identical between v0.33.2 and main).

**Verdict: NOT SUBMITTED.** No code-level root cause found that explains a
REST-only, exchange-triggered, persistent failure; the trigger may be
deployment-specific. A verified local PoC would need the full Karakeep
stack (Next + DB + workers). Logged as a candidate for a future run with a
runnable stack, or for Kyle to shepherd. No comment posted (no verified
finding to add — substance only).

## Deep-check 2 — shlinkio/shlink #2657 (invalid UTF-8 path → 500)

Filed 2026-09-11, bug label, 0 comments, unassigned, no competing PR.
Short-code path segments with invalid UTF-8 bytes reach Postgres as a query
parameter (`SQLSTATE[22021]`) and return 500 instead of the not-found 404.
Diagnosis in the issue is sound (short codes are an ASCII alphabet, so such
a path can never match).

**Verdict: NOT SUBMITTED — environment gap.** PHP and Postgres are not
available in this container, so the bug cannot be reproduced or the fix
tested locally, and this loop's rule is verified-PoC-or-don't-submit.
Strong candidate for any environment with PHP 8.4 + Postgres.

## Also checked, rejected

- karakeep #3146 (embedding jobs "active" with no model configured) —
  reporter-framed UX/logging improvement (log level + admin status
  semantics), a maintainer design call, not a clean verified bug.
- vaultwarden #7794 (group `manage` escalation via collections/details) —
  reporter-owned: "PR follows", one-line fix already tested by reporter.
- umami fresh heads all labelled "fixed in dev"; mastodon fresh = redesign
  UI issues; FreshRSS #9416 unconfirmed websub; hedgedoc/gotify/navidrome/
  uptime-kuma fresh heads = features, questions, assigned, or triage.
