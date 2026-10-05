# Sector 4 sweep — run 44 (2026-10-05)

**Sector:** (4) general company OSS / dev tools
**Outcome:** NO submission. ~45 repos swept across Go / Python / JS / Ruby / Rust dev tools.
Every fresh verifiable bug was already PR'd (usually the reporter's own fix, within
hours), ruled not-a-bug by the maintainer, offered by the reporter with a full diff,
or not verifiable in this sandbox.

## Watch (standing status check)
NO changes. All 18 BUG FIXER MAN PRs OPEN. NiceGUI #6372: evnchn's review still
DISMISSED (head 2a8fe03, her suggested test) — awaiting her re-review, no action.
lodestar #10264 / chatwoot #16124 / MetaMask #10671 / vyper #5294: 0 maintainer
comments. Safe #1440: 8 comments, unchanged. Expensify ×4 comment counts identical
(#102072 55, #102226 35, #101684 33, #102044 28) — no C+ response / assignment / hire.
ESLint #21155: still no `accepted` label. stellar #1734 / PyBNF #931: only our
comments. HackerOne: ledger-only.

## Candidates checked and rejected
| Candidate | Verdict |
|---|---|
| golang-jwt/jwt #542 — CR/LF in signature segment passes validation (RFC 7515 §5.2), filed today | Reporter's fix PR #543 already open (maintainer oxisto engaged) |
| golang-jwt/jwt #539 — MapClaims rejects int64 exp/nbf/iat | Fix PR #540 already open |
| helm/helm #32713 — `--set key={}` yields `[""]` instead of `[]` (strvals `valList`) | Reporter's fix PR #32714 already open |
| gofiber/fiber #4727 — static partial-wildcard strips prefix across segment boundary | Fix PR #4728 already open |
| markedjs/marked #4120 — `walkTokens` quadratic (concat copy per token) | Fix PR #4121 already open |
| python-openxml/python-docx #1622 — empty core-property date element raises TypeError | Reporter's PR #1623 opened 8 min after the issue |
| bmatcuk/doublestar #118 — `Glob` duplicates for `a/**/**` / overlapping alternatives | Maintainer ruled NOT a bug (2026-09-27); fix PR #119 closed. Venue verdict stands |
| rivo/tview #1169 — Table horizontal scroll jumps back when remaining columns fit | Reporter (a regular contributor) published a complete proposed diff and explicitly offered to open the PR himself pending maintainer interest — do not poach |
| tokio-rs/tracing #3621 / #3620 — `#[instrument]` dup-arg guards test `args.target`; `log_internal_errors` default mismatch | Reporter has an active fork of tracing (pushed 2026-09-30, after filing) — PR likely in progress; also no Rust toolchain in this sandbox to verify with |
| yargs/yargs #2600 — pkgConf skips dotted directory names | Two fix PRs already attempted (#2601, #2605, both closed); maintainer actively policing AI-generated issues |
| Python-Markdown/markdown #1643 — HTML comment in inline raw HTML malforms output | Open fix PR #1648 + deep maintainer design discussion (waylan/facelessuser) — maintainer territory |
| nedbat/coveragepy #2313 / #2310 / #2324 | C-tracer segfault / SIGTERM deadlock / C-extension reimport desync — deep C concurrency, not reliably verifiable here |
| redis/go-redis #4065 / #4066 — FailoverClient sentinel failover / pub-sub dial timeout | Needs live Sentinel infra to verify; #4062 is an explicit maintainer compatibility decision |
| rubocop #15803 — Lint/UselessAssignment FP in begin/rescue | Deep dataflow cop work; held as backup only |
| esbuild #4545 / #4544 | Maintainer implements fixes himself historically; deep compiler internals |
| tidwall/gjson #401 — data race on global Disable* vars | API-design discussion (6 comments), not a clean fix |
| commander.js #2645 | Repo just opened an "AI Policy (work in progress)" issue — venue caution |
| go-git #2460, bubbletea #1838, lipgloss #749 | Already PR'd / design-territory (runs 34/39) |

Also swept clean (no fresh unclaimed bug issues): go-toml, cobra, viper, gin, echo,
nats.go, expr, httpx, requests, scrapy, pydantic, tornado, moto, pgx, validator,
zap, zerolog, grpc-go, badger, pflag, logrus, charmbracelet/x, mapstructure,
golangci-lint, buf, tidwall/{sjson,match,pretty}, gojq, jsonparser, fastjson,
uvicorn, pika, paramiko, delve, arrow, otel-go (#9055 is spec-blocked),
grpc-gateway, fasthttp, msw, nock, TanStack/query, python-telegram-bot,
python-multipart, cattrs, structlog, ws, multer, sinon, prettier #20220 (deep
printer work, held), clap #6544/#6537 (triage queue), notify #1018 (macOS
fsevent — unverifiable on Linux), futures-rs.

## Pattern (unchanged since run 19)
Sector 4's fresh-issue window is now measured in hours: reporters ship their own
fix PRs almost immediately (helm: same day; python-docx: 8 minutes; jwt: same
morning). The remaining unclaimed pool is maintainer-design territory or
infrastructure-dependent. Quiet run; no payment requested, $0 received.
