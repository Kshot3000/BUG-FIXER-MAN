# Sector-4 sweep — run 104 (2026-10-06)

Sector: (4) general company OSS / dev tools. Result: **NO submission** — every fresh, verifiable bug found already has an open fix PR (most filed by the reporter within a day), the one held candidate still lacks the maintainer approval its venue requires, and the rest are platform-bound or unverifiable in this sandbox.

## Status watch (direct REST-verified, vs run 103)
**NO changes.** dentalpin #599 / type-coverage #155 MERGED (known); ERCs #2045 OPEN c=1, cake #3671 OPEN c=0, electrum #11012/#11013 OPEN c=0; ansible #87642 OPEN c=1; NiceGUI #6372 OPEN c=1, reviews 4 (evnchn APPROVED stands, awaiting merge); vyper #5294 reviews 3; vikunja #4107 / socket-plugs #162 / gitea #39611 / payload #18509 / chatwoot #16130 / gofactory #67 OPEN c=0. AppKit #5813: pull-endpoint `comments` field read 7, but the direct issue-comment listing shows the same 5 known comments (3 bots + Kshot3000's two CTA email-reply posts) and 0 reviews — field artifact, discarded; CTA check still FAILURE (unchanged, Kyle-only clean direct comment). Expensify identical: #102072 60 (tail = bconnnnn proposal, no C+ selection, no melvin-bot prompt to Kshot3000), #101684 41, #102044 30, #102226 38. HackerOne: ledger-only.

## Hunt detail
Held candidate re-checked:
- **Textualize/rich #4233** (from_ansi NUL/ESC terminal-escape bypass) — still HELD: 1 comment total, only the reporter's own PR offer (2026-10-05T18:56Z); no maintainer approval, which rich's AI_POLICY requires before an AI-authored PR. No change.

Fresh candidates, all already covered by an open fix PR (timeline cross-reference verified for each):
- pytest-dev/pytest #15132 (native TOML numeric `faulthandler_timeout` rejected, filed Oct 5) → reporter's PR #15133.
- spf13/cobra #2520 (GenMan flags/descriptions on one line, filed Oct 5) → PR #2522.
- helm/helm #32713 (`--set key={}` yields `[""]` not `[]`) → PR #32714.
- anchore/syft #5371 (gradle.lockfile comment line catalogued as a package) → PR #5372; #5378 (bun.lock duplicate-name nondeterministic dev-only drop) → PR #5380; #5379 needs Chrome binary fixtures.
- docker/cli #7332 (`docker context export` truncated tar) → TWO competing PRs #7334 and #7341.
- alecthomas/kong #666 (NamedMapper defaults from non-selected commands) → PR #667.
- Masterminds/semver #317 (`^*` documented as any, matches only 0.0.0) → PR #319 open (#321 closed duplicate).
- expr-lang/expr #990 (`in` ignores `expr` tags) → PR #991; #989 (find/first/get nil-return type-checking) → PR #992.
- python-attrs/attrs #1637 (own `__slots__` lost on slotted class) → PR #1638.
- sirupsen/logrus #1595 (writer hook swallows short writes) → PR #1596; #1597 (DisableTimestamp still renames user `time` field) → PR #1598.
- BurntSushi/toml #451 (implicit-table redefinition) → PR #486 open (class already covered; run 89).
- encode/starlette #3630 → PR #3631 (known, run 89). pelletier/go-toml #1131/#1127, mikefarah/yq #2884/#2881 → PR'd (known).

Rejected on verifiability/scope:
- fsnotify #783/#781 kqueue races (BSD-only, no runtime here), #774 inotify unmount (kernel-level, nondeterministic).
- sqlalchemy fresh bugs (#13650 c=12, #13642, #13637, #13636) — active maintainer discussion / design territory.
- psf/requests #7629 Windows registry proxy bypass (winreg path, not verifiable on Linux); #7631 is a test-infra timing issue.
- gopsutil fresh = Windows/FreeBSD platform items; google/uuid fresh = spam/proposals; fsnotify/click/pflag/testify/gin/chi/mux/validator/echo queues empty of fresh tractable bugs; pydantic #13919 is pydantic-core (Rust) territory.

Pattern note: sector 4's fresh-bug pipeline is now effectively instantaneous — reporters (several of them prolific fix contributors) land a PR within ~a day of filing. Our edge has to be bugs *without* a public issue or same-day coverage, not the fresh-issue queue.

$0 requested, $0 received. Next run: sector (5) web / other OSS.
