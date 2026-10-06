# Sector 5 sweep — run 115 (2026-10-06)

**Sector:** (5) web / other OSS. **Result: NO submission.** Every fresh,
verifiable bug found is already fixed by an open PR, assigned, reporter-owned,
or not locally verifiable. Watch: NO changes.

## Status watch (direct REST-verified)
All open PRs identical to run 114: dentalpin #599 / type-coverage #155 MERGED
(known); ERCs #2045 OPEN c=1, cake #3671 OPEN c=0, electrum #11012/#11013 OPEN
c=0; ansible #87642 OPEN c=1; NiceGUI #6372 OPEN c=1, reviews
COMMENTED,COMMENTED,DISMISSED,APPROVED (evnchn APPROVED stands — awaiting
merge); vyper #5294 OPEN c=1 reviews COMMENTED,COMMENTED,COMMENTED,COMMENTED;
memos #6435 OPEN c=2 reviews 1; prysm #17626 OPEN c=1 (CLA-assistant not
signed = Kyle's step) reviews 0; diffy #89 OPEN c=0 reviews 0; vikunja
#4107/#4110, socket-plugs #162, gitea #39611, payload #18509, chatwoot #16130,
gofactory #67, lodestar #10264 OPEN c=0; AppKit #5813 c=5.
Expensify identical (direct listing): #102072 60, #101684 42, #102044 30,
#102226 38 — no selection/hire, no melvin-bot prompt to Kshot3000.
HackerOne: ledger-only (no browser check this run).

## Sweep (~45 repos: chatwoot, payload, gitea, memos, vikunja, listmonk,
linkwarden, nocodb, directus, formbricks, cal.com, documenso, plausible,
umami, appsmith, twenty, appwrite, pocketbase, immich, paperless, Ghost,
outline, saleor, medusa, strapi, novu, trigger.dev, inngest, n8n, navidrome,
miniflux, searxng, mealie, FreshRSS, woodpecker, actual, shlink, wallabag,
authelia, open-webui, khoj, bruno, hoppscotch, BookStack, Trilium, coolify,
discourse, mastodon)

### Already PR'd (verified by cross-reference)
- mealie #8635 (AI translate zeroes servings/yield) → reporter's PR #8636
- searxng #6797 (sogou `resp.next_request` after curl_cffi migration) → PRs #6800/#6802
- woodpecker #7205 (Bitbucket hooks pagination loops to 429) → PR #7210
- twenty #27344 (create-tool schemas mark defaulted fields required) → PR #27345
- payload #18521 → PR #18526; chatwoot #16122 → PR #16123; listmonk #3250 → PR #3256 (all known)

### Assigned / reporter-owned / venue-blocked
- twenty #27334 (app install fails on case-only UUID mismatch — strict `!==`
  compare confirmed in `application-package-fetcher.service.ts`) — ASSIGNED
  to prastoin (maintainer); not ours to take.
- coolify #12101 (malformed `coolify-log-filters` localStorage crashes the
  runtime log viewer) — reporter already has the fix + regression tests in
  their fork draft (darkzmaj/coolify#1); upstream PR creation is
  collaborator-limited.
- gitea #39623 (Bleve `.zap` files locked by Gitea itself) — Windows-only file
  locking, not reproducible in this Linux sandbox.

### Candidates noted (no action)
- **medusajs/medusa #17149** — localized query results stay stale until cache
  TTL after a translation changes; labelled bug + help-wanted, bot triage
  points at `apply-translations.ts` caching without invalidation tags. Held:
  reporter is unsure whether this is a bug or an intended TTL trade-off, and
  the fix is a cache-invalidation design call for maintainers.
- **nocodb/nocodb #14761** — Excel download returns an `http://` dltemp URL
  behind an HTTPS reverse proxy (mixed-content block). Held: URL generation
  sits in `PresignedUrl`/attachment controllers inside a heavy NestJS
  monorepo; the correct fix (forwarded-proto vs configured base URL) is a
  maintainer design choice and not locally verifiable here.
- coolify #12104 — database proxy keeps the container's old IP after restart
  (nginx upstream resolved once at startup). Real, but verification needs a
  live Docker/Coolify instance.

### Standing rejects re-confirmed
chatwoot #16139/#16133, payload #18497/#18490, directus fresh queue,
umami #4570 (claimed) / #4563 (fixed), actual #9104 (race, unverifiable),
navidrome #6276/#6273 (assessed run 110), documenso #3425 (detail-free
security report), immich fresh (iOS-only), mastodon fresh (new-UI reports).

## Money
$0 requested, $0 received. No bounty attached to any candidate above.
