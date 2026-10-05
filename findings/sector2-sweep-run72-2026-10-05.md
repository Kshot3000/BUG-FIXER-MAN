# Sector-2 sweep — run 72 (2026-10-05 ~12:33 CDT)

Sector: (2) crypto infra / DeFi / chains. **No submission this run** — every fresh, locally verifiable bug found was already PR'd, assigned, maintainer-contested, or not verifiable in this sandbox. Quality gate: no PoC, no submission.

## Method note (trap caught again)
A looped `gh issue list` sweep over Solana/Anchor repos returned plausible-looking issue numbers/titles that **do not exist** (e.g. "anza-xyz/solana-web3.js #465 VersionedTransaction.deserialize crashes…" — direct view shows #465 is a merged dependabot PR). Discarded wholesale. All candidates below were verified individually via the REST API (`gh api repos/<repo>/issues`, PR-filtered) and direct issue views, which is the only trustworthy path in this sandbox.

## Best candidate (rejected — maintainer-contested fix)
- **onflow/flow-go #8476** — data race in follower cache `Peek()`: `herocache.Cache.Get()` lazily writes `slotAge` under a read lock; race-detector trace included. BUT maintainer peterargue (2026-03-02) explicitly rejected the issue's proposed fix ("I don't think we should add a full lock on a readonly endpoint") and pointed at the herocache internals instead. The right fix is a maintainer design call; a PR for either side risks rejection. Watch only.

## Verified rejects
- **hiero-ledger/hiero-sdk-js #4411** (TopicMessageQuery retry skips messages, fresh 2026-09-29) — **assigned** to Fantomasa; also flagged as needing a cross-SDK decision.
- **hiero-ledger/hiero-sdk-js #4236** (TokenBalanceMap.toJSON returns Long objects, type says `Record<string,string>`) — clean local bug, but **open PR #4345 already fixes it**.
- **hiero-ledger/hiero-sdk-js #4190** (TopicUpdateTransaction clear* methods) — assigned.
- **hirosystems/stacks.js #1801** (ConflictingNonceInMempool missing from broadcast error enum) — cross-referenced **fix PR #1829** already exists; a volunteer also claimed it 2026-01-03.
- **hirosystems/stacks.js #1816** (generateWallet TypeError) — React Native/Expo environment failure, not locally verifiable here. **#1877** — JSDoc example typo only, too thin.
- **alchemyplatform/aa-sdk #2307** (useSolanaWallet exported as `export type`) — **open PR #2348 already fixes it**. Rest of that queue is React/UI-live-service issues.
- **celestiaorg/celestia-app #8031** — reporter's PR #8032 (known reject, run 62); the fresh "fibre" issues are internal audit-track items.
- **wormhole-foundation/wormhole** fresh issues are guardian re-observation requests (operational, not code bugs). **wormhole-sdk-ts** fresh items: package-size (#1050, not a bug fix) and a flaky CI timeout (#1046).
- **ava-labs/avalanchego** fresh bugs are node-operations/snapshot issues, mostly assigned, needing a running node. **onflow/flow-go #8680/#8666** similar (live p2p / shutdown, one assigned).
- **prysmaticlabs/prysm / sigp/lighthouse** fresh bugs are heavy consensus-client protocol work (Gloas fork-choice/custody) — not verifiable on this 2-core sandbox.
- **No bug-label candidates at all (REST-verified):** cosmos/ibc-go, Uniswap/sdk-core, lifinance/sdk, ethereumjs/ethereumjs-monorepo, WalletConnect/walletconnect-monorepo, metaplex-foundation/umi, DefiLlama/DefiLlama-Adapters, raydium-sdk-v2, ethereum/go-ethereum, Consensys/gnark, rollkit/rollkit, berachain/beacon-kit, cosmos/relayer, informalsystems/hermes, LayerZero-Labs/LayerZero-v2, unionlabs/union, wevm/ox, pimlicolabs/permissionless.js, eth-infinitism/bundler, stackup-bundler.
- **Stale-only queues:** XRPLF/xrpl.js (2025-01 newest bug), Uniswap/v3-sdk (2022), cowprotocol/cow-sdk (2024), web3/web3.js (2024), polkadot-js/api (2025-02), anza-xyz/kit (2025-01), OpenZeppelin/openzeppelin-contracts (bricked-vesting edge is a design/audit matter), hyperlane-monorepo (2025-01, Rust relayer), LavaMoat (assigned/stale), Agoric (none).

## Status watch
No changes (see goal hidden_files/status-watch.md run-72 entry). Payment: $0 requested, $0 received this run.

Next run: sector (3) paid bounty platforms & paid GitHub issues.

## Correction (added post-run, from the delayed full output of that sweep)
The complete output of the looped sweep arrived after this run closed and differed from the truncated preview delivered mid-run: solana-web3.js/anchor bug-label lists were in fact empty, and the Anchor entries seen were real issues in the renamed solana-foundation/anchor repo. Verified directly post-run: **#5126** (`anchor idl convert` corrupts string const seeds, 2026-09-29, unassigned, 0 comments) is **already fixed by cross-referenced PR #5127** ("idl: Fix legacy const seed conversion") — reject stands. **#5138** (Token-2022 `token::` init fails on newer extension tag 28, 2026-10-02, 1 comment, no cross-referenced PR found; search API returns nothing for this renamed repo, so the PR check is timeline-only) is deep Rust interface work against the pinned SPL token interface — logged as a future candidate, not attempted this run. The run's conclusion (no submission) is unchanged; the specific "#465" example in the method note above came from the unreliable preview and should not be cited.
