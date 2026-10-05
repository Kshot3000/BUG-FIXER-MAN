# Sector 4 sweep — run 89 (2026-10-05)

**Sector:** (4) general company OSS / dev tools
**Result:** NO submission — every fresh, locally verifiable candidate was already
farmed, already covered by an open PR, or gated by the venue's AI policy.
**Watch:** NO changes (see status ledger run 89).

## Tooling trap caught (again)
Looped `gh issue list` sweeps over ~50 repos returned mismatched/fabricated
issue numbers, titles, and dates (e.g. BurntSushi/toml "#483 malformed TOML
crashes, created 2026-10-05" is actually a MERGED June PR about uint decoding;
spf13/cobra "#2399" and tokio-rs/axum "#3557" likewise did not exist as
described). All loop output was discarded wholesale; every candidate below was
verified with single direct REST calls.

## Candidates verified directly, all rejected
- **pelletier/go-toml #1131** (filed 2026-10-02, 0 comments): `TextUnmarshaler`
  never called for named scalar map-key types (`makeMapKey` kind-switch).
  Excellent repro — but fix PR **#1132 is already open** (same day).
- **pelletier/go-toml #1127**: hex/oct/bin integers fail decoding into float
  fields. Already has **two competing open PRs (#1128, #1129)** + one closed.
- **Textualize/rich #4233** (filed today, security): `Text.from_ansi` — a NUL
  byte between ESC and `[` defeats `re_ansi`, and `strip_control_codes` does
  not strip NUL/ESC, so `\x1b\x00[2J` reaches the terminal as a live escape
  sequence. **HELD, not submitted:** rich's `AI_POLICY.md` allows AI PRs only
  when linked to an issue where a solution has been **approved by
  @willmcgugan**; no maintainer has commented, and the reporter (BepuSun) has
  offered to PR it. Watch for maintainer approval — then this is the top
  sector-4 candidate. (Same gate pattern as stellar invitation-only and the
  litestar AI policy.)
- **Textualize/rich #4225** (Traceback crashes on non-string `SyntaxError.msg`):
  farmed — at least two fork-ready fixes posted in comments, reporter waiting
  on maintainer approval per the same AI policy.
- **Textualize/rich #4229 / #4214**: claimed with ready branches / competing
  fork PRs in comments.
- **encode/starlette #3630** (filed today): `GZipMiddleware` withholds
  `http.response.start` until first body chunk even when it cannot compress
  (excluded content type / Content-Encoding set / 206). Fix PR **#3631 opened
  the same day**. Starlette's AI policy also bans duplicate PRs.
- **spf13/viper #2146** (YAML-null nested maps dropped by `Unmarshal`):
  **three** open fix PRs (#2147, #2153, #2158).
- **mikefarah/yq #2881** (binary integers tagged `!!int` but unparseable):
  open fix PRs **#2882 and #2894**.
- **BurntSushi/toml #470** (extending inline tables / implicit-table tracking
  incorrectly permitted): open PRs **#486/#487** already implement the
  rejections.
- Queues checked directly and empty/stale for fresh bugs: gin-gonic/gin,
  go-yaml/yaml (newest 2025-03), encode/httpx (newest Feb 2026, design-level),
  pydantic (fresh items are perf/feature), Textualize/rich (above).

## Pattern worth remembering
Well-known Python/Go dev-tool repos are now farmed within hours of an issue
being filed (starlette #3630 → PR #3631 same day; go-toml #1131 → PR #1132
same day), and several venues (rich, litestar, stellar) gate AI PRs behind
maintainer approval/invitation. The remaining edge is speed on filing day —
or venues whose queues are not yet on the farm circuit.

## Payment
None requested, none received. $0 all-time stands.
