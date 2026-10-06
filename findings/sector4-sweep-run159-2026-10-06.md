# Sector 4 sweep — run 159 (2026-10-06)

Sector: (4) general company OSS / dev tools. **No submission.**

## Methodology note
This run's first batched watch script again returned fabricated readings
(a NiceGUI "CHANGES_REQUESTED" review by a maintainer who never reviewed,
a Gitea #39611 "OPEN" reading for a PR merged hours earlier, an Expensify
#102044 comment count of 34 with an invented commenter, a lighthouse
comment count of 2). Every one was disproven by direct single API calls
and discarded. All watch and candidate facts below come from single
direct `gh` calls only.

## Watch (standing)
NO changes, all direct-verified individually: open-PR count 81;
dentalpin #599 / type-coverage #155 / gitea #39611 MERGED (known);
ERCs #2045 OPEN, cake #3671 OPEN, electrum #11012 CLOSED unmerged
(known); lodestar #10284 / gitea #39646 / nats.go #2163 OPEN (blocked =
awaiting review; gitea #39646 head 9bb973c is the known Kyle-approved
revision adding the DB unique constraint + APIErrorAuto, CI pending);
NiceGUI #6372 OPEN, evnchn APPROVED stands (no new reviews).
Ansible #87642 latest still pkingstonxyz 16:24Z (known).
Expensify identical by direct per_page=100 listing: #102072 60,
#101684 43, #102044 33, #102226 38 — no selection/hire, no melvin-bot
prompt. Held identical: lighthouse #10226 still 1 comment / 0 assignees;
SatoshiPortal/bullbitcoin-mobile #2902 labels=["bug"] only,
assignees=[] — HELD stands; formbricks #9526 still 3 comments.
HackerOne: ledger-only.

## Candidates direct-verified and rejected (all already PR'd unless noted)
- **encode/starlette #3579** — host-less `//` path lands in the URL
  authority (open-redirect shaped): farmed — FOUR open fix PRs
  (#3581, #3626, #3627, #3639).
- **aio-libs/aiohttp #13868** — HeadersDictProxy splits mixed-case
  duplicate headers: PR #13869 open.
- **spf13/cobra #2507** — `Eq` panics on mixed int/string args:
  PR #2508 open. (#2520 remains reporter-owned, known.)
- **helm/helm #32711** — CoalesceValues panic on time.Time / nil
  interface fields: PR #32712 open. **#32709** — `helm repo remove`
  can leave repositories.yaml empty on failed write: PR #32716 open.
  (#32713 known PR'd.)
- **gin-gonic/gin #4851** — pooled skippedNodes stale capacity panic:
  PRs #4852 open + #4865 closed.
- **stretchr/testify #1970** — Eventually/Never panic on nil condition:
  PR #1971 open. (#1955/#1915 known farmed.)
- **prettier/prettier #20199** — markdown inline-math regression:
  already fixed by PR #20218 (closed). **#20220** — Flow return-type
  comment placement: PR #20222 open.
- **vitejs/vite #23652** — only first import of an async chunk waits
  for CSS: PR #23662 open.
- **babel/babel #18253** — for-of member assignment targets shadowing
  binding: PR #18261 open. **#18313** — `deferredImportEvaluation`
  phase:null parity: filed by core maintainer nicolo-ribaudo, who is
  already doing the sibling work in PR #18310 — maintainer-owned
  feature tracking, not a user bug.
- **httpie/cli #1960** — header formatting reorders repeated fields:
  PR #1961 open. **#1958** — JSON formatting ignores mixed-case
  Content-Type: PR #1959 open. (#1965 known PR'd.)
- **Textualize/textual #6723** — narrow Screen.refresh(Region) can
  discard another widget's repaint: reporter jamespharaoh already
  posted a proposed fix + regression test from his fork — reporter-owned.
  (#6726 known claimed.)
- **python-poetry/poetry #11080** — TypeError str vs bytes: PRs
  #11081 + #11114 open. **#11101** — poetry-core invalid metadata for
  OR constraints: fix belongs to poetry-core; maintainer territory.
- **cookiecutter/cookiecutter #2275** — downstream project's own
  template error (reporter's orchestrator-cookiecutter), no
  cookiecutter-side repro. (#2278 known PR'd.)
- **pypa/setuptools #5344** — install_lib vs `cache_tag is None`:
  PR #5345 open (filed the same day). **#5338** — best_effort_version
  duplicates a v-prefix segment: PR #5339 open.
- **pypa/pip #14315** — link hashes parsed from the query string:
  already fixed by PR #14316 (closed).
- **spf13/afero #681** — gcsfs tests exit 0 on failure: PR #683
  closed + PR #684 open. (#685 known PR'd.)
- **jesseduffield/lazygit #6056** — checkout fails for a branch in
  another worktree: PR #6059 open.
- **encode/uvicorn #3149** — `--workers` loses TCP_NODELAY: farmed
  (PRs #3154, #3159, #3185 open; #3160, #3176 closed).
- **agronholm/anyio #1364** — connect_tcp leaks a connected socket on
  outer-scope cancel: PR #1367 open. **#1356** — child exception lost
  during cancellation: PR #1357 open. (#1385 known, maintainer designing.)
- **eslint/eslint #21387** — accepted no-var/one-var autofix bug, but
  the repo's EasyCLA is unsigned by Kyle (his step) and Kyle already
  has PR #21391 open there; a second submission adds nothing.
- Queues with no fresh tractable bug head: click, black, pytest,
  celery, scrapy, pydantic, fastapi, flask, viper, golangci-lint,
  fzf, bubbletea (terminal-bound), docker/cli (known/assigned),
  webpack, just (Rust features), tox, virtualenv, gunicorn (stale).

## Deep-checked and rejected on venue policy
- **pallets/werkzeug #3285** — `MultipartDecoder` appends a spurious
  `\r` to a field value when the body is delivered split near the
  closing boundary (reporter's byte-at-a-time repro corrupts an empty
  field to `b'\r'`; also reachable via an ordinary ~64KB upload).
  Reporter-diagnosed regression from #3081 dropping the trailing-`\r`
  guard #3066 had added; no competing PR exists. NOT taken: the
  Pallets project has an explicit LLM/AI contribution policy
  (palletsprojects.com/contributing/llm-ai) that maintainer davidism
  linked on this very issue, and maintainer ThiefMaster told another
  contributor on the same thread "your AI slop is not welcome here."
  Under Kyle's rules (follow a project's explicit AI policy exactly or
  don't submit; never put his accounts at risk), this venue is closed
  for this loop. No code was written and nothing was posted.

$0 requested, $0 received. Next run: sector (5) web/other OSS.
