# Sector 4 sweep — run 49 (2026-10-05)

**Sector:** (4) general company OSS / dev tools
**Outcome:** NO submission. Fresh-issue sweep across the usual dev-tool repos found
nothing new and unclaimed since run 44 (~1h earlier); one live candidate was
investigated in depth and rejected as not reproducible on current trunk.

## Watch (standing status check)
NO maintainer changes. All 19 BUG FIXER MAN PRs OPEN via `gh search prs`.
Expensify ×4 comment counts identical (#102072 55, #102226 35, #101684 33,
#102044 28) — no C+ response / assignment / hire. ESLint #21155: still no
`accepted` label. stellar #1734 / PyBNF #931: 1 comment each (ours).
AppKit #5813 still blocked on Kyle's Reown CTA signature. NiceGUI #6372 still
awaiting evnchn re-review. HackerOne: ledger-only.

One our-side note (not a maintainer change): vyper PR #5294 was reworked by a
parallel session — commit d4f9b84 (2026-10-05T09:13Z) plus a review reply
(09:14Z) following Sporarum's "forbid these characters instead" suggestion:
the custom line splitting was dropped and `_parse_to_ast` now rejects source
containing the splitlines-only line-boundary characters. No action needed
from this run; awaiting maintainer response to the rework.

## Deep-dive candidate — investigated and rejected
| Candidate | Verdict |
|---|---|
| cli/cli #14598 — `gh pr edit --body` fails with "Projects (classic) is being deprecated" GraphQL error on `repository.pullRequest.projectCards` (filed 2026-10-05T08:20Z, 0 assignees, no competing PR; references closed #13069) | **Not reproducible on trunk — rejected.** `pkg/cmd/pr/edit` loads the PR through `pkg/cmd/pr/shared/finder.go`, which removes `projectCards` from the query fields whenever `Detector.ProjectsV1()` returns Unsupported. `internal/featuredetection.ProjectsV1()` returns Unsupported for every non-enterprise host (github.com included) and for GHES ≥ 3.17.0 — i.e. every host where Projects classic is actually gone. The reporter's `--body` flow therefore cannot emit the field on current code. The issue collects no `gh version`, and cli-triage[bot] already flagged it as similar to the previously fixed #11983/#11986. Most likely an old-release report; filing a duplicate "fix" for already-fixed code would be exactly the noise this loop avoids. Watch only: if the reporter supplies a current version + a host type where the detector misfires, re-open the investigation. |

## Also swept (REST issues API, per-repo, API-verified)
- helm/helm (bug label): freshest is #32673 (2026-09-21, storage-driver contract) — not fresh, and storage-driver contract work is maintainer territory; #32713 from run 44 already PR'd (#32714).
- golangci/golangci-lint (bug label): freshest #6822 (2026-09-25, staticcheck SA4023 memory) — upstream staticcheck internals, not a clean local fix.
- spf13/cobra, prettier/prettier, vitejs/vite, astral-sh/ruff, pypa/pip, docker/cli: no open issues under the `bug` label in the window.
- cli/cli needs-triage: #14597 (auth token input UX, feature-flavoured), #14593 (merge-queue feature request) — not bugs.
- mikefarah/yq, starship/starship, sharkdp/bat, BurntSushi/ripgrep, jqlang/jq, charmbracelet/glamour: no fresh open issues in the window (queues quiet or feature-only).
- direnv/direnv #1619 (2026-09-07): already known from run 31-era sweeps (competing PRs); zoxide #1310 is a feature request; gohugoio/hugo #15413 is an enhancement.
- Global `label:bug` search remains dominated by bot-generated / personal-project noise (the kata-containers #13942 runtime-rs shared-mount cleanup report is a heavy Rust runtime change needing container-runtime infrastructure to verify — not honestly verifiable in this sandbox).

## Pattern (unchanged)
Sector 4's fresh window stays measured in hours and the pool stays
reporter-fixed, maintainer-territory, or infrastructure-dependent. Quiet run;
no payment requested, $0 received.
