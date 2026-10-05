# MetaMask/core — RpcBalanceFetcher reports a failed native/staked balance read as success:true, value:0 (zeroes real balances)

- **Project:** MetaMask/core (`@metamask/assets-controllers`) — https://github.com/MetaMask/core
- **Issue:** #10043 (filed 2026-09-01 by gomesalexandre, 0 comments, unassigned, no competing PR) — https://github.com/MetaMask/core/issues/10043
- **Submission:** PR #10671 OPEN (2026-10-05) — https://github.com/MetaMask/core/pull/10671 — branch `Kshot3000/core@fix/10043-rpc-balance-fetcher-failed-read-as-zero` (commits a3fbb8c + changelog-link follow-up)
- **Bounty/payment:** none posted on the issue; fix offered freely, tips welcome via this hub's README. $0 requested, $0 received.

## Bug
`RpcBalanceFetcher.fetch` built native and staked entries for every requested account with `success: true` hard-coded, substituting `new BN('0')` when the multicall result had no entry for the account. But the multicall layer records a native entry only for a successful read (a genuine zero is an explicit `BN(0)` from `aggregate3`/`getBalance`), and the fallbacks behave the same — so a missing entry ⟺ the read failed. The fabricated successful zero flowed through `TokenBalancesController` (which forwards `success && token === ZERO_ADDRESS` entries) to `AccountTrackerController.updateNativeBalances`, persisting `balance = '0x0'`: one failed RPC read erased the user's known balance. The staked branch had the same flaw plus a deeper one: `getStakedBalancesForAddresses` dropped successful zero-share reads entirely (returned `{}` for all-zero and for total failure alike), so absence was ambiguous at that layer.

## Fix
- `rpc-balance-fetcher.ts`: native/staked entries with no recorded balance are reported `{ success: false }` with no value — the ERC-20 branch's existing shape (`success: bn !== null`) and `AccountsApiBalanceFetcher`'s failure shape. All three `TokenBalancesController` consumers already skip unsuccessful entries, so a failed read now preserves the previous balance; a genuine zero (explicit `BN(0)`) still lands as a successful zero.
- `multicall.ts`: `getStakedBalancesForAddresses` records an explicit `BN(0)` for every address whose shares call succeeded with zero shares; only failed reads leave an address out. Uniform contract across all paths (aggregate3 native/ERC-20, both fallbacks, staked): **entry present ⟺ read succeeded**.

## Proof (red → green, local, repo-pinned tooling)
- Tests first per the repo's AGENTS.md: new/updated fetcher + multicall tests failed pre-fix (5 failures: native absence, native partial failure, staked absence, both multicall zero-share shapes), pass post-fix (101/101 in the two suites).
- Full `@metamask/assets-controllers` suite post-fix: **45/45 suites, 1810/1810 tests pass**. (The one failure seen in an intermediate full run, `codefi-v2` onBreak, fails intermittently on the clean tree too — unrelated token-prices timing test.)
- `TokenBalancesController` suite initially failed 27 tests: every diff was only the two synthesized zero entries (native + staking token) missing from expected state. Migration: 25 mocks now return explicit zero entries for healthy zero reads (expectations unchanged — the same pattern three pre-existing passing mocks already used); 3 failure-simulation tests had expectations updated to assert no fabricated zeros; 1 event test renamed to its new premise. Suite: 185/185.
- `tsc --build packages/assets-controllers/tsconfig.build.json`: clean. `oxlint` on all touched files: 0 errors (fetcher-test suppression counts refreshed: id-length 17→24, no-unsafe-call 13→16, no-unsafe-member-access 21→24 — same pre-existing patterns, new instances from the added tests). `oxfmt --check`: clean. Changelog `[Unreleased] → Fixed` entry added.
- Sandbox notes: yarn install needed `YARN_HTTP(S)_PROXY` env (the egress proxy) or every fetch died with TLS EPROTO; install's final step still prints `command not found: yarn` (a root script expects a yarn shim) but linking completes and all tooling runs from `node_modules/.bin`.

## Sector-1 sweep rejects (same run)
ethers.js #5178 (THREE competing PRs #5179/#5180/#5182), wagmi #5248 (claimed + PR #5250), wagmi #5233 (claimed + PR #5255), wagmi #5256 (already watched; reporter fix pending), MetaMask/core #9964 (PR #9965), bitcoinjs #2350 (known reject — defect lives in varuint-bitcoin), BlueWallet/Cake/Electrum queues (no fresh verifiable bugs; standing rejects), Rabby #4156/#4157 (server-dependent, standing reject), Taho (stale queue).
