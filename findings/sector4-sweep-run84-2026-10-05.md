# Sector 4 sweep — run 84 (2026-10-05)

**Sector:** (4) general company OSS / dev tools
**Result:** NO submission. Watch: NO changes.

## Status watch (direct-verified)
Body-listed PRs unchanged: dentalpin #599 / type-coverage #155 MERGED (known); ERCs #2045 OPEN c=1, cake #3671 OPEN c=0, electrum #11012/#11013 OPEN c=0. Spot checks identical: NiceGUI #6372 OPEN c=1 r=3; gitea #39611 c=0; payload #18509 c=0; AppKit #5813 c=5; gofactory #67 OPEN; socket-plugs #162 OPEN c=0; eslint #21391 OPEN c=4; chatwoot #16130 c=0; vikunja #4107 OPEN c=0; vyper #5294 OPEN r=3. Expensify counts identical by direct REST listing: #102072 55, #101684 38, #102044 29 (FitseTLT "Reviewing" stands), #102226 38 — no C+ selection/assignment/hire, no melvin-bot prompt to Kshot3000. HackerOne: ledger-only (no browser check this run).

## Hunt — candidates verified and rejected
- **mikefarah/yq #2884** (2026-09-28, sort/sort_by silently accept map/array keys that `max` rejects) — already fixed by OPEN PR #2885 ("reject unsupported comparison keys when sorting"). Do not duplicate.
- **helm/helm #32673** (2026-09-21, storage drivers don't return ErrReleaseNotFound from Update; SQL silently loses the update) — already fixed by OPEN PR #32676. Do not duplicate.
- **npm/cli #10054** (2026-09-30, ERESOLVE with transitive peer deps on primeng@18) — arborist resolver internals; repro depends on live registry state and the reporter's `min-release-age` config is a confounder. Maintainer territory, no clean verifiable fix.
- **argoproj/argo-cd #30020 / #30018** (filed today: hard-refresh race, cluster-cache latent defects) — heavy Go monorepo, race-condition class not locally verifiable here; same-day audit-issue pair pattern.
- **sqlalchemy #13650 / #13644 / #13643** (filed Oct 4–5) — 4–11 comments each, active maintainer discussion; not clean targets.
- **golangci-lint / hugo / pre-commit** fresh bug queues — assigned, upstream-linter issues (staticcheck SA4023), or years-stale.
- **uv / ruff / starship / eza / nushell / mise** fresh bugs — Rust; no cargo/rustc toolchain in this sandbox.
- A looped `gh issue list` sweep returned misaligned numbers/titles again (e.g. "uv #16840" resolved to a version-bump PR) — caught by direct REST verification and discarded, per the standing fabrication trap.

Next run: sector (5) web apps / other OSS.
