# go-gitea/gitea — commit-status lookup builds an OR expression per SHA, breaking SQLite on >1000-commit lists

- **Issue:** https://github.com/go-gitea/gitea/issues/39606 (filed 2026-10-05, label type/bug, 0 comments, unassigned, no competing PR at submission time)
- **PR:** https://github.com/go-gitea/gitea/pull/39611 — OPEN (2026-10-05, base main)
- **Payment:** none posted on the issue; fix offered freely, tips welcome via the PR footer. Not a bounty request.

## Bug
`processGitCommits` (compare/PR/commit pages) → `ConvertFromGitCommit` → `ParseCommitsWithStatus` → `git_model.GetLatestCommitStatusForRepoCommitIDs`. That function built `builder.Or(builder.Eq{"sha": sha}, ...)` with one condition per commit, and a second `Or` of `(index, sha)` pairs for the follow-up fetch. With 1,772 commits the generated expression tree exceeded SQLite's `SQLITE_MAX_EXPR_DEPTH` (1000), so creating/viewing a PR whose head is >~1000 commits ahead failed with HTTP 500: `processGitCommits, SQL logic error: Expression tree is too large (maximum depth 1000) (1)`. The commit count is what matters (the reporter's branch had only 16 distinct authors — the email lookups were not the problem).

## Proof (red → green)
New regression test `TestGetLatestCommitStatusForRepoCommitIDsManySHAs` calls the function with 2,001 SHAs (one fixture SHA with real statuses + 2,000 synthetic) against Gitea's SQLite test database:
- Unpatched (upstream main 6654604): fails with the issue's exact error — `SQL logic error: Expression tree is too large (maximum depth 1000) (1)`.
- Patched: passes, and the fixture SHA still returns its statuses.
- Full `go test ./models/git/` passes; `go build ./services/git/ ./models/git/` OK; gofmt/vet clean.
- Environment note: Gitea's test harness refuses to run as root and strips `GITEA_*` env vars, so tests were run as user `nobody` with the Go caches shared read/write — test results unaffected.

## Fix
In `models/git/commit_status.go` (`GetLatestCommitStatusForRepoCommitIDs` only):
- Max-index lookup: SHAs queried in chunks of 500 via `builder.In("sha", chunk)` — a flat expression, no depth growth, and within SQLite variable limits.
- Follow-up fetch: `(index, sha)` pairs queried in chunks of 100 `Or` conditions.
Results are merged in order and grouped exactly as before. The sibling `GetLatestCommitStatusForPairs` has the same pattern; left untouched to keep the PR scoped to the reported bug (worth a follow-up if maintainers ask).

## Submission
Fork PR from `Kshot3000/gitea@fix/39606-commit-status-expr-depth` (commit 2eb540a), Conventional-Commits title, `Assisted-by` trailer per the repo's AGENTS.md, minimal PR body with the full issue URL.
