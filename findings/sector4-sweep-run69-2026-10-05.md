# Sector-4 sweep — run 69 (2026-10-05)

Sector: (4) general company OSS / dev tools. **No submission** — every concrete
candidate was already PR'd, claimed, assigned, or under maintainer design
debate. One candidate was verified to root cause locally before being
rejected as already-covered.

## Deep-verified, then rejected as already covered: gitleaks/gitleaks #2281

Issue: `gitleaks git --pre-commit --staged` reports "0 commits scanned. no
leaks found." on staged files that `detect --no-git` correctly flags
(filed 2026-09-22, 0 comments, unassigned, label bug).

Local verification (built master from source, Go 1.26.6):

- The issue's exact repro in a plain repo (fresh or with history) **works**
  — leak found. `sources/git.go` is byte-identical between v8.30.1 (the
  reporter's version) and master, so it is not a code regression.
- Reproduced the reporter's **exact** output ("0 commits scanned.",
  "scanned ~0 bytes", "no leaks found") by setting `color.diff=always` +
  `color.ui=always` in git config: git then emits ANSI escapes into the
  piped diff, `gitdiff.Parse` yields zero files, and the scan silently
  scans nothing.
- Root cause therefore confirmed — but **PR #2284** ("fix: force
  --no-color on git diff/log so forced color config doesn't break
  parsing", OPEN/MERGEABLE, explicitly "Fixes #2281", with its own
  regression test) already covers all four diff/log invocations.
  Submitting a duplicate would be noise. REJECTED.

## Other candidates checked and rejected (all API-verified)

- **google/go-jsonnet #660** (parseYaml stray null when the stream starts
  with a comment): two open fix PRs already — #867 and #875. Farmed.
- **sharkdp/bat #3845 / #4039** (capacity-overflow panic on huge
  `--line-range` offsets): SIX open fix PRs (#3848, #3855, #3860, #4037,
  #4041, #4046); sibling #3844 has #3847/#3875/#3886. Repo is farmed.
- **sharkdp/fd #2122** (`--changed-after` boundary semantics): a
  collaborator says it is "not ready for implementation" (backwards-compat
  concern, semantics still debated with the maintainer), and PR #2123
  already implements the inclusive bound. Design call + taken.
- **trufflesecurity/trufflehog #5299** (tunnel dummy-key FP): claimed by
  a volunteer 2026-09-11; #5379 is Windows-only (unverifiable here).
- **norwoodj/helm-docs #349 / #286**: assigned (2 assignees each).
- **gitleaks #2239** (fingerprint by position): open PR #2286 adds
  content-specific fingerprints — same territory.
- Standing/old/platform-bound: fzf #4260/#2021 (Windows/old), glow queue
  (2023–24, stale), pre-commit queue (Windows/old), uv fresh issues
  (heavy Rust resolver work, unverifiable scope), ripgrep #3222
  (maintainer-driven repo), watchexec #1131 (pager/process-wrap,
  not verifiable headless).

## Status watch

No changes: body-listed PRs unchanged (dentalpin #599 and
type-coverage #155 merged, known; ERCs #2045, cake_wallet #3671,
electrum #11012 OPEN). Expensify #102072 still OPEN at 55 comments —
no C+ response, assignment, or hire. HackerOne: ledger-only.

Payments: none requested, none received ($0 to date).
