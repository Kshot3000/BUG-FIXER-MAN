# Sector 4 sweep — run 39 (2026-10-05)

Sector: (4) general company OSS / dev tools. **No submission.**

~40 repos swept for bugs filed since mid-September 2026. Every fresh,
locally verifiable bug already has a competing fix PR (usually opened
within hours of the issue), is claimed by its reporter with a ready
branch, or is a maintainer design call. Pattern identical to runs
19 / 24 / 29 / 34: the fresh-issue window on popular dev-tool repos is
now measured in hours.

## Already PR'd (verified via PR search, do not duplicate)

| Issue | Competing PR |
|---|---|
| pelletier/go-toml #1131 TextUnmarshaler map keys | #1132 |
| labstack/echo #3153 Group.Use RouteNotFound | #3154 |
| gin-gonic/gin #4851 pooled skippedNodes panic | #4852 (+ closed #4865) |
| gin-gonic/gin #4844 wildcard vs trailing-slash | #4848 |
| stretchr/testify #1970 Eventually/Never nil panic | #1971 (+ closed #1980) |
| go-git/go-git #2460 sparse-checkout skip-worktree | #2462 |
| go-git/go-git #2409 shallow-repo Log/MergeBase | #2411 |
| go-git/go-git #2441 Worktree.Add full walk (help wanted) | #2444 (claimed in-thread) |
| a-h/templ #1449 component call in text position | #1450 |
| nats-io/nats.go #2158 partial-write torn PUB | #2159 |
| nats-io/nats.go #2151 jetstream Info data race | #2152 |
| prometheus/client_golang #2147 Gather vec RLock | #2148 |
| go-chi/chi #1188 regexp placeholder suffix matches `/` | #1189 |
| etcd-io/bbolt #1282 MoveBucket into itself | maintainer PR #1283 (ahrtr, "Resolved in #1283") |
| etcd-io/bbolt #1284 unaligned LoadBucket cast | #1285 and #1287 |
| python-attrs/attrs #1637 slots ignored/lost | #1638 |
| sirupsen/logrus #1597 DisableTimestamp renames time field | #1598 |
| sirupsen/logrus #1595 writer hook short writes | #1596 |
| go-playground/validator #1650 panic on `any` field | #1651 |

## Rejected on inspection

- **quic-go/quic-go #5909** (congestion control compares packet numbers
  across packet number spaces) — filed by maintainer marten-seemann
  himself as a tracking note; no repro detail; his to fix.
- **nats-io/nats.go #2160** (FetchBytes 1M-message batch → ~30 MiB/call)
  — real, but the fix is a new public API shape; a commenter already
  claimed it and is waiting on the maintainers' API preference.
- **Textualize/rich #4229** (highlight_words([]) zero-length matches) —
  reporter's tested fix branch is already prepared and offered; they are
  awaiting a maintainer response on AI-assisted contributions.
- **fsnotify/fsnotify #783 / #781** (kqueue races / symlink opens) —
  kqueue is BSD/macOS-only; cannot be reproduced or tested on this
  Linux sandbox.
- **No fresh bugs at all** in the window: spf13/cobra, spf13/viper,
  spf13/pflag, urfave/cli, expr-lang/expr, pallets/click, fastapi/typer,
  encode/httpx, hynek/structlog, rs/zerolog, gorilla/websocket,
  minio/minio-go, cockroachdb/errors.

## Watch (same run)

No changes: all 16 open BUG FIXER MAN PRs remain open (NiceGUI #6372's
maintainer approval was recorded in run 38); Expensify's four $250
proposals unchanged (comment counts 55 / 35 / 33 / 28 — no C+ response,
assignment, or hire); ESLint #21155 still has no `accepted` label;
stellar #1734 and PyBNF #931 still carry only our report comments.
$0 received to date; nothing requested this run.
