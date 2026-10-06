# Sector 5 sweep — run 125 (2026-10-06)

**Sector:** (5) web / other OSS. **Result: NO submission.** Every fresh,
verifiable bug found is already fixed by an open PR, assigned to a
maintainer, or not locally verifiable. Watch: NO changes.

## Status watch (direct REST-verified)
All PRs identical to run 124 (corrected): dentalpin #599 / type-coverage
#155 MERGED (known); ERCs #2045 OPEN c=1, cake #3671 OPEN c=0, electrum
#11012 CLOSED unmerged (known), trilium #11920 CLOSED unmerged (known,
eliandoran — "we'll handle it in #11921"); viem #5196 OPEN (bot comments
only), optimism #23214 OPEN c=0, diffy #89 OPEN c=0, prysm #17626 OPEN c=1
(CLA-assistant not signed = Kyle's step), memos #6435 OPEN c=2, NiceGUI
#6372 OPEN c=1 (evnchn APPROVED stands — awaiting merge), vyper #5294 OPEN
c=2, ansible #87642 OPEN c=1, vikunja #4107/#4110 OPEN c=0.
Expensify identical (direct listing): #102072 60, #101684 42, #102044 30,
#102226 38 — no selection/hire, no melvin-bot prompt to Kshot3000.
HackerOne: ledger-only (no browser check this run).

## Sweep (per-repo bug queues, ~35 repos: chatwoot, listmonk, memos,
vikunja, payload, Ghost, outline, mealie, searxng, twenty, medusa, nocodb,
coolify, actual, logseq, gitea, navidrome, jellyfin, woodpecker, umami,
linkwarden, trilium, immich, supabase, appwrite, cal.com, documenso,
formbricks)

### Already PR'd (verified by cross-reference, direct timeline checks)
- chatwoot #16145 (automation assignee-presence condition glued to the
  next condition — `andLOWER` PG::SyntaxError, filed today 04:14Z) →
  PR #16146 already open.
- listmonk #3253 (GetList subscriber_count at 2x) → PR #3255.
- mealie #8589 (PATCH recipe returns 400 "Recipe already exists" when
  tags/category non-empty) → PRs #8600 and #8610.
- payload #18498 (plugin-ecommerce variant joins capped at 10) →
  cross-reference is our own PR #18509, already submitted.

### Assigned / not verifiable / rejected
- outline #13967 (Android print includes the document-options pane,
  filed today) — assigned to tommoor (maintainer) on filing; not ours.
- navidrome #6273 (Add-to-Playlist dialog doesn't list all playlists,
  filed 2026-10-05) — DEEP CHECK, no root cause found: the dialog's
  `useGetList('playlist', {page:1, perPage:-1}, sort name ASC,
  {smart:false})` sends `_start=0&_end=-1`; deluan/rest v1.0.1 clamps
  `Max = max(0, end-start) = 0`, and the persistence layer treats
  `Max=0` as no LIMIT, so the server returns all playlists; the
  `smart:false` filter and `canChangeTracks` (writable, non-smart,
  non-synced) behave as coded. The report gives no playlist count,
  names, or logs, so there is nothing deterministic to reproduce —
  same no-repro class as navidrome #6276 (smart-playlist import,
  external file share, no repro steps) and #6275 (reporter's own log
  contradicts the claimed version, known). Not submitted.
- immich #27739 — Android native (Cronet) write-after-free crash;
  native/mobile, not locally verifiable here.
- A batched second-tier scan returned a nocodb #14766 entry that
  direct REST + GraphQL checks prove does not exist (404 / could not
  resolve) — discarded as a fabrication artifact, not acted on.

## Payment
None requested, none received. $0 this run.
