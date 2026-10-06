# Sector 4 sweep — run 154 (2026-10-06)

Sector: (4) general company OSS / dev tools. **No submission.**

## Methodology note
An initial batched multi-repo scan returned mismatched number/title pairs
(e.g. it paired helm #31812 with an unrelated title, and prometheus #18268
with a TSDB title when the item is a maintainer-add PR). The scan was
discarded wholesale; every candidate below was verified by a single direct
`gh issue view` + competing-PR search, per the standing lesson from runs
127/134.

## Candidates direct-verified and rejected
- **astral-sh/uv #22237** — "Preserve compound extra guards in dependency
  overrides": filed by Astral-side contributor, assigned, and a bot comment
  shows a linked PR already changing the test inventory. Reporter/staff-owned.
- **celery/celery #10761** — `EagerResult.get()` after `revoke()` raises
  `Exception(<return value>)` instead of `TaskRevokedError`: real and cleanly
  reproduced in the report, but already fixed — reporter's own PR #10772
  MERGED (competing PR #10765 closed).
- **aio-libs/aiohttp #13495** — `MultipartWriter.as_bytes()` ignores part
  Content-Encoding / Content-Transfer-Encoding: TWO open fix PRs (#13496
  reporter-owned, #13688).
- **aio-libs/aiohttp #13433** — dynamic routes with percent-encodable fixed
  segments unreachable: open PR #13498 (plus closed attempt #13459).
- **aio-libs/aiohttp #13364** — multiple Content-Encoding codings not decoded:
  open PR #13400 by a maintainer (Dreamsorcerer).
- **stretchr/testify #1955** — `assert.Empty` regression for pointer-to-interface
  (v1.11.0 `isEmpty` rewrite): TWO open PRs (#1956 reporter-owned, #1973).
- **stretchr/testify #1915** — `EqualExportedValues` stack overflow on recursive
  structures: farmed — THREE open PRs (#1916, #1939, #1968) plus closed attempts.
- **helm/prometheus/cobra/docker-cli/starlette/gin queues** — fresh bug-labelled
  heads are maintainer items, PRs miscategorised by the discarded scan, or empty.
- **scrapy/scrapy, hashicorp/hcl** — bug-labelled heads are years-old stale items.
- **astral-sh/ruff** — freshest bug #29106 is the known maintainer suppression
  cluster (run 119); remaining fresh items are Rust linter/formatter internals
  with fast upstream competition — not verifiable to a quality fix in one run.
- **python/mypy** — fresh bugs are deep type-checker internals (circular-import
  `__getattr__`, exhaustiveness), not tractable to a verified fix in one run.

## Watch (standing)
NO changes, all direct-verified individually: open-PR count 81;
dentalpin #599 / type-coverage #155 MERGED (known); ERCs #2045 OPEN,
cake #3671 OPEN, electrum #11012 CLOSED unmerged (known); lodestar #10284,
gitea #39646, nats.go #2163 OPEN/MERGEABLE; NiceGUI #6372 reviews include
APPROVED (evnchn stands), issue-comments = 1 (own). Expensify identical by
direct per_page=100 listing: #102072 60, #101684 43, #102044 33, #102226 38 —
no selection/hire, no melvin-bot prompt. (A `--paginate` count reading
61/44/34/39 was a +1-per-page artifact and was discarded.) Held identical:
lighthouse #10226 still 1 comment / 0 assignees; SatoshiPortal/bullbitcoin-mobile
#2902 labels=["bug"] only, assignees=[] — HELD stands; formbricks #9526 still
3 comments. HackerOne: ledger-only.

$0 requested, $0 received. Next run: sector (5) web/other OSS.
