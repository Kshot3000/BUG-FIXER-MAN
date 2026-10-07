# Sector 4 sweep — run 174 (2026-10-06)

**Sector:** (4) general company OSS / dev tools
**Result:** NO submission — ~40 repos swept via direct REST issue listings; every fresh tractable bug is already PR'd (usually within hours), claimed, or reporter/maintainer-owned.

## Deep-checks (each direct-verified: body, comments, timeline cross-references)
- **encode/starlette #3630** (filed 2026-10-05, 0 comments): GZipMiddleware withholds `http.response.start` until the first body chunk even for responses it can never compress (Content-Encoding set / 206 / excluded content type) — silent SSE streams send no headers. REJECTED — already fixed by open PR #3631 (bruno-espino).
- **spf13/cobra #2520** (2026-10-05, 0 comments): generated man pages join flag + description on one line (regression from the go-md2man v2 move). REJECTED — already fixed by open PR #2522 (seflue).
- **pydantic/pydantic #13938** (filed today, 2 comments): JSON Schema for `**kwargs: Unpack[TypedDict]` puts the whole TypedDict under `additionalProperties` instead of merging its fields. REJECTED — commenter pranavpk404 reproduced it, claimed it per the repo's assignment-first contribution policy, and cross-referenced PR #13939 appeared.
- **axios/axios #11295** (filed today, 0 comments): `formToJSON` throws `RangeError: Invalid array length` for nested fields named `length`. REJECTED — already fixed by open PR #11296.
- **expressjs/express #7506** (2026-10-05): `res.redirect()` sets Content-Length when Transfer-Encoding is already set. REJECTED — two competing fix PRs (#7507 closed, #7508 open).
- **gofiber/fiber #4727** (2026-09-30): static partial-wildcard route strips its prefix without a segment boundary. REJECTED — already fixed by open PR #4728.
- **tokio-rs/tokio #8591** (2026-10-04, C-bug): DuplexStream wakes/drops wakers while holding the pipe mutex — a waker that re-enters the pipe deadlocks. REJECTED — reporter-owned: the reporter states "I have a fix ready… Should I open a PR?" and the sibling fixes (#8551/#8553/#8557) were maintainer-handled.
- **sqlalchemy/sqlalchemy #13657** (filed today, 3 comments): failed `BEGIN` leaves `_transaction` set so `close()` rollback masks the original error. REJECTED — maintainer-owned: zzzeek bisected it to a5f4ea7 and a maintainer fix is already proposed on gerrit.
- **marshmallow-code/marshmallow #3068** (filed today, 0 comments): v4 regression — `fields.Date().load()` silently accepts `datetime` instances via the isinstance fast path. REJECTED — reporter's own fix PR #3065 is already open ("Implemented in #3065").
- **sirupsen/logrus #1597** (2026-10-03): DisableTimestamp still renames user-provided time fields. REJECTED — PR #1598 open.
- **python-attrs/attrs #1637** (2026-10-02): explicitly declared slots ignored on attrs classes. REJECTED — PR #1638 open.
- **Textualize/rich #4233** (2026-10-05): `Text.from_ansi` NUL byte between ESC and `[` bypasses the ANSI regex. REJECTED — reporter-owned ("Happy to submit a PR for this if that would help").
- **more-itertools/more-itertools #1308** (filed today): `bucket` discards a supplied validator when the callable is falsey (`validator or (lambda x: True)`). REJECTED — claimed on-thread by DawnofGenX ("/take", confirmed, fix in progress); reporter also offered the fix.
- **PuerkitoBio/goquery #616** (filed today, 0 comments): `Single` FindMatcher returns matches from multiple sibling subtrees (2 vs documented 1). REJECTED — reporter-owned: full local fix + 33 regression subcases already prepared, asking before opening the PR.
- **fsnotify/fsnotify #783/#781** (kqueue races / symlink opens): BSD kqueue-only paths — not verifiable on this Linux sandbox. Skipped on verifiability.
- Rest of the sweep (fastapi, flask, requests, pytest (assigned), docker/cli (assigned e2e), cli/cli, axum, httpx, DRF, celery, django, grpc-go (assigned / xds internals), etcd (assigned), textual, hyper (h2 internals), vitest browser mode, clap (release-policy), gunicorn, tornado, scrapy, validator, goldmark, cast, cachetools, uvicorn): fresh heads are features, docs, assigned, deep-internals, or already-covered items.

## Status watch
NO changes — open-PR count 85; dentalpin #599 / type-coverage #155 MERGED (known); ERCs #2045 OPEN, cake #3671 OPEN, electrum #11012 CLOSED unmerged (known, org blocked); chatwoot #16165, prometheus #19944, gitea #39646 (9bb973c) / #39650, caddy #8163 (5b88382), lodestar #10284, nats.go #2163 OPEN/MERGEABLE; NiceGUI #6372 reviews COMMENTED/COMMENTED/DISMISSED/APPROVED — APPROVED stands. Expensify identical by direct listing: #102072 61 (assignee FitseTLT, Help Wanted stands), #101684 43, #102044 33, #102226 38 — no selection/hire, no melvin-bot contributor-details prompt. Held identical: lighthouse #10226 1 comment / 0 assignees; SatoshiPortal/bullbitcoin #2902 labels=["bug"] only, 0 assignees; formbricks #9526 3 comments. HackerOne: ledger-only.

Payment: $0 requested, $0 received (all-time received still $0).
Next run: sector (5) web apps / other OSS.
