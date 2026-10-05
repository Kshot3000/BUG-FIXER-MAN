# Sector-4 sweep — run 79 (2026-10-05)

Sector: (4) general company OSS / dev tools. **No submission.**

## Watch (run 79)
NO changes. Body-listed PRs direct-verified unchanged: dentalpin #599 /
type-coverage #155 MERGED (known); ERCs #2045 OPEN c=1, cake #3671 OPEN c=0,
electrum #11012/#11013 OPEN c=0. Spot checks unchanged: NiceGUI #6372 c=1 r=3
awaiting re-review; gitea #39611 c=0; payload #18509 c=0; AppKit #5813 c=5;
gofactory #67 OPEN. One artifact caught + discarded: GraphQL counted
socket-plugs #162 as c=1 — REST shows 0 issue comments / 0 reviews (unchanged).
Expensify counts identical by direct REST listing: #102072 55, #101684 38,
#102044 29 (FitseTLT "Reviewing" stands), #102226 38 — no C+ selection /
assignment / hire; the melvin-bot prompt on #102072 is the known Oct-3 one
(Kyle's contributor details were already posted). HackerOne: ledger-only.

## Hunt — every candidate verified individually via REST, all rejected

Already has an open fix PR (the dominant pattern — most filed <2 weeks ago):
- mikefarah/yq #2884 → PR #2885; #2851 → PR #2854
- helm/helm #32673 (storage drivers don't return ErrReleaseNotFound from
  Update) → PR #32676
- BurntSushi/toml #451 → PRs #468/#473/#477/#486/#515; #449 → #458/#478/#481
- stretchr/testify #1955 (Empty regression, pointer-to-interface) → PRs
  #1956/#1973; #1915 (EqualExportedValues stack overflow) → PRs
  #1916/#1968 (+2 closed)
- expr-lang/expr #990 (`in` ignores expr tags) → PR #991; #989 → PR #992
- Masterminds/semver #317 (^* matches only 0.0.0) → PR #319 (+#321 closed);
  #272 → PR #322
- go-chi/chi #1188 → PR #1189; #1069 (compress Accept-Encoding q=0) →
  ELEVEN fix PRs (#1070/#1074/#1099/#1104/#1114/#1123/#1133/#1142/#1176/
  #1177/#1198/#1200)
- go-git/go-git #2460 → PR #2462; #2409 → PRs #2410/#2411; #2399 → PRs
  #2404/#2474
- valyala/fastjson #110 (FastFloat sci-notation precision) → PR #124;
  #119 (Validate vs Parse) → PRs #125/#126
- evanphx/json-patch #217 (EnsurePathExistsOnAdd + ~1 escape) → PR #221
- goccy/go-yaml #940 → PR #941; #930 → PR #931
- sergi/go-diff #157 (PatchMake panic, invalid UTF-8) → PRs #158/#159
- more-itertools #1268 → fixed by PR #1294 (merged)
- npm/node-semver #908 → PRs #910/#912; #906 → PR #907; #909 → covered by
  PR #901 per commenter verification
- santhosh-tekuri/jsonschema #275 (Validate panics on 1e9999999) → PR #277;
  #276 → PR #278 (closed)

Maintainer-ruled / disputed / by-design:
- expr-lang/expr #961 — maintainer: "this is how floats work"
- Masterminds/semver #275 — maintainer ruled per semver spec precedence
- shopspring/decimal #385 / #388 — commenters could not reproduce
- tidwall/gjson #393 — ForEach yielding all duplicate keys is its iteration
  contract; Get-first is a policy call for the maintainer, not a clean fix

No usable repro:
- jesseduffield/lazygit #6086 — startup YAML error, reporter's config.yml
  is blank; error file/line cannot be identified from the report

Already fixed upstream (issue stale, verified by bisection):
- sergi/go-diff #151 (line-diff missing deletes, garbage inserts) —
  reproduced BROKEN on v1.2.0/v1.3.1 (reconstruction checks fail) and
  CORRECT on v1.1.0 and on current master 57c41f4 (v1.4.0): proper
  Delete/Insert ops, both reconstructions exact. Fixed by a674b30
  "Fix line diff by using runes without separators" (+ test 74798f5).
  Issue simply never closed — no fix to submit.

Other queues swept, empty/stale/OS-specific: httpie/cli, spf13/cobra,
docker/cli, spf13/viper, go-yaml/yaml, pelletier/go-toml, urfave/cli/v3,
alecthomas/kong, encode/httpx, pallets/click, fastapi/typer, Textualize/
textual (stale), fsnotify (inotify/macOS/Windows-specific), google/go-cmp
(features), hashicorp/hcl + zclconf/go-cty (ancient), goreleaser (1 issue),
securego/gosec (no bug-label issues), google/go-containerregistry (hangs,
network-dependent), tidwall/sjson (features/questions), ohler55/ojg (none),
websockets/ws (ancient feature requests), labstack/echo #3099 (2c, routing
design discussion), go-chi/chi and go-git queues beyond the above.

$0 requested / $0 received. No X post. Next run: sector (5) web/other OSS.
