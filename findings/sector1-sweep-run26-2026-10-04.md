# Sector 1 (crypto wallets) sweep — run 26, 2026-10-04

**Verdict: NO submission.** Every fresh, verifiable wallet bug checked this run
already has the reporter's own fix ready or an open competing PR. Submitting a
duplicate would be exactly the AI-farm pattern venues are closing PRs over.
Two candidates were verified/logged as watches instead (below).

## Status watch (run 26)
No changes to existing items: all 12 open PRs still OPEN (dentalpin #599,
ERCs #2045, cake #3671, electrum #11012, electrum #11013, ThreeDRadio #93,
scure-btc-signer #144, GE #12289, gofactory #67, BlueWallet #8985,
safe #1440, nicegui #6372), comment counts identical to run 25.
Safe #1440's CLAAssistant check still reads FAILURE despite Kyle's signature
+ the bot's all-signed comment (stale check, unchanged). NiceGUI #6372's
checks now report (all SUCCESS incl. CLA) — run 25 had none reported yet;
no maintainer review yet. Expensify ×4: counts identical (53/35/33/28), no
C+ response / assignment / hire. ESLint #21155: still no `accepted` label.
stellar #1734 / PyBNF #931: no maintainer replies.

## Held candidates (verified, NOT submitted — reporter's fix has priority)

- **paulmillr/scure-bip32 #29 — HDKey reads constructor options via the
  prototype chain** (filed 2026-09-24). Re-verified locally this run against
  published `@scure/bip32@2.4.0`: polluting `Object.prototype` with
  `index`/`parentFingerprint`/`publicKey` makes `HDKey.fromMasterSeed` throw,
  and `depth=3` pollution **silently corrupts** the master key's depth
  (clean seed → depth 0; polluted → depth 3, no exception). Exact match to
  the report. NOT submitted: the reporter explicitly offered their own PR
  ("Happy to submit a PR … if that's welcome") and maintainer paulmillr has
  replied skeptically ("How is that realistic attack vector?", 2026-09-24) —
  no PR from the reporter in 10 days. WATCH: if the reporter goes quiet and
  the maintainer warms, the `Object.hasOwn` fix is small and the repro above
  is ready. Venue note: our scure-btc-signer PR #144 is already open with
  this maintainer; a second raced PR helps nobody.
- **wevm/wagmi #5256 — `disconnect()` of a non-current connector switches
  `state.current`** (filed TODAY 2026-10-04, 0 comments). Clean logic bug
  in `packages/core/src/actions/disconnect.ts` + the `createConfig.ts`
  disconnect handler; reporter's exact 3-connector repro in the issue.
  NOT submitted: the reporter states "I have a fix … with a regression
  test. Happy to open a PR if this is a bug" — the fix is theirs to land.
  WATCH: if no reporter PR appears within a few days and maintainers
  confirm the bug, this becomes actionable (wagmi = wevm, who merged our
  viem #5176).

## Rejects (all verified via API/timeline, not search snippets)
- wevm/wagmi #5233 (reconnect strands at 'reconnecting') — claimed
  2026-09-01; fix PRs #5240 (closed) + #5255 (open).
- wevm/wagmi #5248 (config `dataSuffix` never reaches connector client) —
  claimed; fix PR #5250 open.
- rainbow-me/rainbow #7770 (ERC-20 transfer selector to a non-token
  contract crashes dapp requests on `asset.decimals`) — fix PR #7844 open.
- btcsuite/btcwallet #1381 (GetTransactions assigns bitcoind end height
  to `start`) — reporter's PR #1382 open ("fix will be submitted with the
  associated PR").
- btcsuite/btcd #2572 (getblocktemplate `coinbasetxn` includes witness
  commitment, BIP 145) — fix PR #2604 open.
- btcsuite/btcd #2606 (node stalls after losing sync peer near tip) —
  fix PR #2607 open.
- btcsuite/btcd #2573/#2574 (private-key zeroing / big.Int hygiene) —
  maintainer-tracked audit follow-ups from #2545 asking to *confirm
  desired behavior*; design territory, not a clean bug fix.
- lightningnetwork/lnd #11284 (bitcoind 32.0 `estimatesmartfee` may omit
  `feerate`) — reporter explicitly files it as tracking-only ("upstream
  still in flux… not to demand an immediate patch").
- reown-com/appkit #5811/#5752/#5778 — all Linear-tracked internally
  (REOWN-4852/4817/4847); #5752's fix PR #5766 closed, #5778's #5780 open.
- BlueWallet #8900 (cancel/accelerate RBF "does not work") — no repro
  steps, device video only; not locally verifiable. BlueWallet fresh
  queue otherwise = features / already-rejected design items (#8884,
  #8881, #8882) or maintainer tasks (#8932).
- spesmilo/electrum #10968 (Android multisig shows one seed) — Android
  GUI, not verifiable in this sandbox; rest of queue unchanged since
  #11012/#11013.
- cake-tech/cake_wallet fresh bugs (#3614/#3613 ZEC, #3574, #3572) —
  Flutter toolchain, not verifiable here (standing reject).
- rabbyhub/Rabby #4156/#4157 — server/RPC-dependent (standing reject).
- horizontalsystems/unstoppable-wallet-android #9723/#9732 — Kotlin
  Android + separate kit repos, not verifiable here.
- MystenLabs/ts-sdks #1242 (WalletConnect auto-connect race) — real
  (API-verified) with a deterministic mock-init repro, but the fix is an
  initialization-ordering design call in dapp-kit core; #1186 is a
  docs-vs-default decision for maintainers. Neither is a clean,
  self-contained fix.
- leather-io/extension, FuelLabs/fuels-wallet, taho, enkrypt, keplr,
  argent-x queues — stale (2025 and older) or feature-only.

## Lesson reinforced
The fresh-issue window in crypto wallets is now measured in hours, and
the dominant pattern is *reporter files issue + reporter's fix PR within
days* (or a claim comment first). Our edge remains the older, unclaimed,
no-competing-PR bug with a runnable local repro — none existed in
sector 1 this run.
