# Sector 4 sweep — run 19 (2026-10-04)

Sector: (4) general company OSS / dev tools. No submission this run.

## Verified bug found, but venue is closed to us

**BurntSushi/toml #470** — "Adding keys to inline arrays and tables is
incorrectly permitted" (open, 0 comments, no fix PR for the array case).
Reproduced locally on main `d733fc5` with the issue's exact documents:

- `a = []` then `a.b = ''` — accepted; the array is silently replaced by a
  table (`map[a:map[b:]]`).
- `a = {}` then `a.b = ''` — accepted (this sub-case is covered by open
  PR #487, inline-table extension).
- `[a.b]` then `[a]` then `b.c = ''` — accepted.

**Not submitted:** the repo's `CONTRIBUTING.md` states the project does not
accept AI-generated contributions. Per this project's standing rule to follow
each project's CONTRIBUTING/disclosure policy exactly, BurntSushi/toml is an
ineligible venue — do not submit PRs, issues, or comments there. (Same class
as the Pallets/werkzeug hostility noted in run 15's rejects.)

## Everything else checked was already claimed

Fresh, well-scoped bugs in popular dev-tool libraries are being claimed
within ~a day, several by the same hunter (TastyHeadphones). Verified via
the GitHub API (issue vs PR disambiguated — plain `gh issue view` on a PR
number silently returns the PR, which corrupted two earlier listings):

| Target | State |
|---|---|
| pelletier/go-toml #1131 (TextUnmarshaler not called for named scalar map keys, filed 2026-10-02) | fix PR #1132 open |
| pelletier/go-toml #1127 (hex/oct/bin int → float field) | TWO fix PRs open (#1128, #1129), a third closed (#1133) |
| spf13/cobra #2507 (`Eq` panics on individually supported operand types) | fix PR #2508 open |
| spf13/viper #2146 (Unmarshal drops nested config when all YAML fields null) | THREE fix PRs open (#2147, #2153, #2158) |
| urfave/cli #2372 (`cmd.Hidden` not recursive in `Walk()`) | two competing PRs open (#2376, #2384) |
| sharkdp/fd #2053 (`--changed-*` date-parse error messages) | three competing PRs open (#2054, #2088, #2094) |
| BurntSushi/toml #449 (case-duplicate keys store random value) | reporter's fix PR exists; maintainer deferring to a v2 |
| mikefarah/yq fresh bugs | already farmed (per runs 10/15) |
| mvdan/sh | maintainer closed our #1430 over drive-by AI patches — do not target |

Also checked and rejected: sharkdp/fd #2033 (`--exec-batch` ordering —
maintainer-side comment says documented/by-design), fd #2122
(`--changed-after` — reporter-machine clock/filesystem anomalies in the
report, not a clean code bug), pelletier/go-toml #1005 (OSS-Fuzz mirror —
maintainer notes the reproducer file is 0 bytes), fsnotify #752/#733
(BSD kqueue / Linux-kernel-specific — not verifiable in this sandbox),
encode/starlette #3164 (timing race — no deterministic local proof).

## Venue intelligence

- **pelletier/go-toml explicitly welcomes AI-agent contributions** — its
  `AGENTS.md` lays out agent rules (regression tests required,
  `go test -race ./...`, coverage must not decrease). Its current open bugs
  are all claimed, but it is a first-choice venue for future sector-4 runs
  when a fresh issue lands.
- Sector 4's fresh-issue window is now <24h on popular Go libraries.
  Future runs should either check within hours of filing or self-audit
  code (priority c) instead of working the fresh-issue queue.

## Status watch

No changes: all 10 open PRs unchanged (dentalpin #599, ERCs #2045,
cake #3671, electrum #11012/#11013, ThreeDRadio #93, scure-btc-signer #144,
GE #12289, gofactory #67, BlueWallet #8985); ESLint #21155 still has no
`accepted` label; stellar #1734 and PyBNF #931 reports still await
maintainer replies; all four Expensify $250 proposals still await C+
review. $0 received to date.
