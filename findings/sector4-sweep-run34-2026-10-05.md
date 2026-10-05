# Sector 4 sweep — run 34 (2026-10-05)

**Sector:** (4) general company OSS / dev tools. **Result: NO submission** — every fresh, verifiable bug found already has a competing fix PR, most filed within hours of the issue. Same pattern as runs 19, 24, 29: the fresh-issue window on popular dev-tool repos is now under ~24h.

## Status watch (no changes)
All 14 open BUG FIXER MAN PRs still OPEN (dentalpin #599, ERCs #2045, cake #3671, electrum #11012/#11013, ThreeDRadio #93, scure-btc-signer #144, GE #12289, gofactory #67, BlueWallet #8985, safe #1440, nicegui #6372, ethers #5198, da-codec #72). da-codec #72's updatedAt bump is only the CodeRabbit bot summary comment; Safe #1440 CLAAssistant check still stale FAILURE. Expensify ×4 comment counts identical (55/35/33/28) — no C+ response, assignment, or hire. ESLint #21155 still has no `accepted` label. stellar #1734 / PyBNF #931: no maintainer replies. HackerOne: ledger-only.

## Candidates checked and rejected (all already PR'd)
- **labstack/echo #3153** (filed 2026-10-04, 0 comments): `Group.Use()` silently overwrites an explicitly registered group RouteNotFound handler — clean repro in the issue. Already fixed by open PR #3154.
- **a-h/templ #1449** (2026-10-02): component call in text position after literal text renders its source as literal text. Already addressed by open PR #1450.
- **alecthomas/kong #666** (2026-09-28, 0 comments): NamedMapper defaults decoded for non-selected commands (`[foo bar]` instead of `[foo]`), full Go reproducer in the issue. Already fixed by open PR #667.
- **go-git/go-git #2460** (2026-10-03, 0 comments): sparse-checkout branch switch leaves skip-worktree index entries at the previous branch, corrupting the next commit. Already fixed by open PR #2462.
- **pelletier/go-toml #1131** (2026-10-02, 0 comments): `encoding.TextUnmarshaler` never called for named scalar map-key types (`makeMapKey` kind-switch precedes the interface probe). AI-welcoming venue, but already fixed by open PR #1132.
- **nats-io/nats.go #2160 / #2158**: both claimed in-thread by other contributors with fix plans.
- **quic-go/quic-go #5909**: congestion-control packet-number-space comparison — deep protocol work, maintainer territory, not cleanly verifiable in this sandbox.
- **charmbracelet/bubbletea #1838 / #1822, rivo/tview #1169**: TUI rendering/scrolling bugs — not reliably verifiable headless here.
- **sqlalchemy #13640 / #13641**: maintainer (zzzeek) already traced and proposed fixes via Gerrit within hours.
- **mvdan/sh #1429**: already fixed on master by the maintainer (0f6fdc0b); issue just not yet closed. Venue also closed to drive-by patches (run 10).
- No fresh bug-labeled issues at all (since 2026-09-20) in: spf13/cobra, spf13/viper, spf13/pflag, spf13/cast, fsnotify, grpc-go, prometheus/client_golang, logrus, zap, pallets/click, httpx, rich, mapstructure, go-yaml, gin, fasthttp, uuid, go-cmp, go-spew, goccy/go-yaml, fxamacker/cbor, urfave/cli, sarama, kafka-go, memberlist, tcell, gofuzz.

## Takeaway
Sector 4 remains the most heavily farmed sector: four separate hunters' PRs were found on four separate fresh issues this run alone. Future sector-4 runs should either check within hours of issue creation or pivot to older, deeper issues in mid-size repos rather than fresh-issue sniping.
