# Sector 4 sweep — run 24 (2026-10-04): NO submission

Sector: (4) general company OSS / dev tools. Every candidate below was verified
via the REST search API (`type:issue` / `type:pr`) before use — the run-19/22
lesson (issue listings silently mixing in PRs, and fabricated sweep output)
was applied throughout.

## Verdicts — every fresh, verifiable bug already has a competing fix PR

- **charmbracelet/x** (fresh, detailed, locally reproducible issues — all taken):
  - #974 vt DECSTBM/DECSLRM margins unclamped → panic in InsertLineArea → PR #988 open
  - #980 cellbuf wide-cell corruption on InsertLine/DeleteLine/DeleteCell → PR #983 open
  - #979 ansi Wrap wide-grapheme blank lines → PR #985 open
  - #961 vt SendKey drops modified cursor keys → PR #987 open
  - #984 vt CursorStyle steady/blink flag → PRs #986 open + #1002 closed
  - Pattern: one reporter (DRMacIver) files excellent repros; fix PRs land within days.
- **nats-io/nats.go**: #2151 jetstream cached-Info data race → PR #2152 open;
  #2158 flusher partial-write torn PUB → PR #2159 open; #2160 FetchBytes (perf/design, 1 comment).
- **agronholm/anyio**: #1353 Hypothesis/pytest-plugin backends → PRs #1354 open + #1355 closed;
  #1288 socket aclose checkpoint → PRs #1289 open, #1291/#1292 closed;
  #1344 to_thread interpreter-exit deadlock (8 comments) → PRs #1346 open + #1345 closed.
- **expr-lang/expr**: #822 optional-chaining slice of unknown → PR #945 open;
  #809 ConstExpr panic with expr.Function → PR #955 open.
- **pelletier/go-toml** (welcomes AI agents per its AGENTS.md — first-choice venue,
  but nothing clean): #1131 → PR #1132, #1127 → PRs #1128/#1129 (both already logged
  run 19); #1005 is an OSS-Fuzz mirror whose reproducer sits behind oss-fuzz.com
  access we don't have; the rest of the queue is features/benchmarks.
- **Stale queues, no fresh bugs:** shopspring/decimal, google/uuid,
  santhosh-tekuri/jsonschema, Masterminds/semver, mitchellh/mapstructure,
  encode/httpx, Textualize/rich, pallets/click, psf/requests (newest bug 2022).
- **fsnotify #774** (inotify watch dropped on unmount, 0 comments): real, but the
  repro needs mount/unmount privileges not available in this sandbox — cannot
  verify red→green here, so not pursued (verification is a hard rule).

## Status watch (same run)
No changes on any open item. All 11 open PRs unchanged; Safe #1440's CLAAssistant
check still reads FAILURE despite Kyle's signature + the bot's "All contributors
have signed ✅" comment (run 23) — appears to be a stale check on head ef0524f;
watch next run. Expensify ×4 proposals untouched; ESLint #21155 still no
`accepted` label; stellar #1734 / PyBNF #931 no maintainer replies.

Payments: none requested, none received ($0 all-time; 4 × $250 Expensify
proposals pending selection).
