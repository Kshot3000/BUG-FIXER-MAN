# Sector 1 (crypto wallets) sweep — run 41, 2026-10-05

**Verdict: NO submission.** Every fresh, verifiable wallet bug checked this
run already has an open competing PR — in most cases the reporter's own,
filed the same day as the issue. Submitting duplicates would be exactly
the AI-farm pattern venues are closing PRs over.

## Status watch (run 41)
No changes to existing items: all 17 BUG FIXER MAN PRs still OPEN
(dentalpin #599, ERCs #2045, cake #3671, electrum #11012, electrum #11013,
ThreeDRadio #93, scure-btc-signer #144, GE #12289, gofactory #67,
BlueWallet #8985, safe #1440, nicegui #6372, ethers #5198, da-codec #72,
MetaMask/core #10671, vyper #5294, chatwoot #16124). Spot checks:
chatwoot #16124 checks SUCCESS, 0 comments; nicegui #6372 still APPROVED
(evnchn), awaiting merge; Safe #1440 8 comments (unchanged).
Expensify ×4 counts identical (#102072 55, #102226 35, #101684 33,
#102044 28) — no C+ response / assignment / hire. ESLint #21155 still
no `accepted` label. stellar #1734 / PyBNF #931: 1 comment each (ours).
HackerOne: ledger-only.

## Watch resolution
- **wevm/wagmi #5256** (held candidate from run 26 — `disconnect()` of a
  non-current connector switches `state.current`): the reporter's fix
  landed as **PR #5257** (opened 2026-10-05T05:45Z, "Preserve the active
  connection when another connector disconnects", closes #5256, with
  regression tests + changeset). Watch closed — do not duplicate.

## Rejects (all verified via per-repo REST API, not search snippets)
- **Rainbow-Me/rainbowkit #2700** — account modal `aria-labelledby`
  points at `rk_account_modal_title`, which nothing renders
  (ProfileDetails hardcodes `rk_profile_title` on two `<h1>`s). Detailed,
  verifiable — but reporter owenpkent already has PR #2702 open
  (#2701 closed) and the issue is Linear-tracked (RK-222).
- **family/connectkit #520 / #521** — same a11y auditor, same pattern:
  modal dialog has no accessible name (#520) and the wrong-network
  warning SVG is unlabeled (#521). Reporter's own PRs #522 / #523 are
  already open for both.
- **safe-global/safe-core-sdk #1438** — `connect()` drops the current
  signer when no signer is passed: reporter's PR #1439 already open.
  (#1424 remains a maintainer design call, per run 22.)
- **ethers-io/ethers.js #5193** — RLP non-minimal length prefixes:
  sibling PR #5197 still open (unmerged); our #5198 covers #5194.
- **bitcoinjs/bitcoinjs-lib #2350** — CompactSize non-minimal encodings:
  standing reject (run 31) — the defect lives in the `varuint-bitcoin`
  dependency, no clean in-repo fix. (PR #2353 is an unrelated PSBT fix.)
- **MetaMask/metamask-extension #46856** — standing reject (run 36):
  UI confirmation flow, no local repro. Rest of the fresh queue is
  internal controller-upgrade / yarn-audit bot issues.
- **MetaMask/core #10667** — standing reject (run 36): dependency /
  registry bump for another package, not a code fix.
- **BlueWallet** fresh queue (#8982 iOS file-handler config, #8964
  screenshare frames) — platform behavior, not verifiable here;
  #8975/#8974 are feature requests. **Electrum** queue unchanged —
  the freshest real bugs (#10998, #10969) are already ours
  (#11012/#11013). **Cake Wallet** — no fresh bug issues (BOLT12 is a
  feature request; Flutter toolchain standing reject). **Rabby**
  #4156/#4157 — server/RPC-dependent standing rejects.
- **paulmillr/scure-bip32 #29** — unchanged (1 comment, 2026-09-24):
  reporter's own PR still offered, maintainer still skeptical.
  Our verified repro from run 26 stands; do not race it.
- **xrplf/xrpl.js #3518–#3528** — "security vulnerabilities in old
  versions" = dependency-audit spam, not code bugs.
- **anza-xyz/solana-sdk #978 / #961** — Rust soundness discussions
  with maintainer engagement (5 comments on #978); design territory,
  heavy toolchain.
- **polkadot-js/extension #1618** — stale (2026-05), metadata-version
  signing crash; no clean local repro path.

## Tooling lesson (third occurrence — runs 22, 26, now 41)
`gh issue list` inside a multi-repo shell loop returned **fabricated
issue numbers and titles** for several repos this run (viem #5190/#5195/
#5200, MetaMask/core #10678/#10684/#10687, scure-btc-signer #147 —
every one 404s via the REST API). All candidates above were verified
with per-repo REST calls (`repos/<owner>/<repo>/issues`, filtering out
`pull_request` entries) plus direct PR lookups before any conclusion
was drawn. Never trust a looped `gh issue list` listing on its own.
