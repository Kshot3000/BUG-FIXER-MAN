# Sector 5 (web / other OSS) sweep — run 85, 2026-10-05

**Result: NO submission.** Every fresh, verifiable candidate checked this run already has a fix PR open or merged, is claimed, or is a maintainer design call. Watch: ONE change (eslint PR #21391 closed unmerged — see status-watch).

## Watch change
- **eslint/eslint PR #21391 CLOSED unmerged** 2026-10-05T20:42:03Z by DMartens: "The issue is assigned to someone else, so I am going to close this PR. In the future please follow our contribution guidelines…" (issue #21385 had been assigned to another contributor). No reply sent (no arguing/nagging rule). The verified fix remains on the fork branch. BFM open PR count drops by one.
- Expensify counts re-verified with `per_page=100`: #102072 55, #101684 38, #102044 29, #102226 38 — identical to run 84. (A default-pagination read of 30/page was caught and discarded as an artifact.)
- All other body-listed / spot-checked PRs unchanged: dentalpin #599 & type-coverage #155 MERGED (known); ERCs #2045 OPEN c=1; cake #3671 OPEN c=0; electrum #11012/#11013 OPEN c=0; NiceGUI #6372 OPEN c=1 r=3; gitea #39611 c=0; payload #18509 c=0; AppKit #5813 c=5; gofactory #67 OPEN; socket-plugs #162 c=0; chatwoot #16130 c=0; vikunja #4107 c=0; vyper #5294 r=3.

## Candidates checked and rejected
- **outline/outline #13746** (Markdown ZIP import attachment keys end in literal "null") — already fixed by merged PR #13750.
- **outline/outline #13824** (orphaned attachment rows on failed upload) — two competing fix PRs already open: #13875 and #13914.
- **listmonk #3250** (one-click unsubscribe on double opt-in mail reports success, changes nothing; filed 2026-10-03, unassigned) — fix PR #3256 already open ("Fixes #3250, fixes #3063").
- **umami #4563** (MCP `filters.event` returns zeros on pageview tools) — fix PR #4565 MERGED 2026-09-29; issue still open but the merged fix makes any new PR maintainer territory.
- **umami #4570** (metrics endpoint 503 from UI, 200 via API key) — claimed in-thread by another contributor with the reporter's blessing; root cause not yet isolated.
- **TryGhost/Ghost #30830** (comped member upgrading to same tier ends up paid with no tier) — fix PR #30832 already open.
- **directus** fresh queue — same as prior runs: #28318→maintainer PR, #28295 claimed + live PG/WS, rest known.
- **formbricks #8715 / nocodb / twenty / cal.com / documenso / memos / BookStack / Trilium / hedgedoc / pocketbase / n8n** — no fresh unassigned, un-PR'd bug-label issues verifiable in this sandbox.
- **mealie #8589, uptime-kuma #7841/#7895** — standing rejects (competing PRs from prior sweeps).

No bounty requested, no payment received. $0 this run.
