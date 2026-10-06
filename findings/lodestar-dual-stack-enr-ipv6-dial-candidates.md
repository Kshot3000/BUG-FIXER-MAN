# ChainSafe/lodestar: dual-stack discovered ENRs lose IPv6 dial candidates

- **Issue:** https://github.com/ChainSafe/lodestar/issues/10256 (filed 2026-10-03 by suna4, 0 comments, unassigned, no competing PR at submission time)
- **Fix PR:** https://github.com/ChainSafe/lodestar/pull/10284 (OPEN, MERGEABLE, base `unstable`)
- **Commit:** a20fd5c on Kshot3000/lodestar branch `fix/10256-dual-stack-enr-dial-candidates`

## Bug

`PeerDiscovery.onDiscoveredENR` read one multiaddr per transport via `ENR.getLocationMultiaddr("tcp")` / `("quic")`. In `@chainsafe/enr`, the bare protocol returns the IPv4 location when the ENR advertises both families (`tcp4 || tcp6`). So a dual-stack peer's IPv6 TCP and QUIC endpoints never reached the peer store, leaving no IPv6 dial candidate from discovery when IPv4 was unreachable. The reporter's loopback repro: dual-stack ENR 0/50 connected (only IPv4 stored), IPv6-only ENR 50/50, both families in the peer store 50/50.

## Fix

- `onDiscoveredENR` queries each family explicitly (`tcp4`/`tcp6`, `quic4`/`quic6`) and keeps all advertised multiaddrs.
- `CachedENR` / `handleDiscoveredPeer` carry `multiaddrsTCP` / `multiaddrsQUIC` arrays; `dialPeer` merges all of them into the peer store.
- The libp2p `peer:discovery` path keeps all matching multiaddrs per transport instead of only the first.

## Proof (red to green)

New regression test in `packages/beacon-node/test/unit/network/peers/discover.test.ts`: a dual-stack boot ENR (IPv4 + IPv6, TCP + QUIC) is processed at construction, then dialed via `discoverPeers`, asserting all four multiaddrs reach `peerStore.merge`.

- Unpatched: FAIL, merged list held only the 2 IPv4 multiaddrs (`expected [ ...(2) ] to include '/ip6/::1/tcp/9000'`).
- Patched: 3/3 tests pass in the file; Biome check clean on both changed files.
- Honest limitation (also disclosed in the PR): full package `check-types` not run to green locally, the sandbox lacks built workspace dependencies (281 pre-existing module-resolution errors in unrelated files, none in `discover.ts`); the changed expressions were type-checked in isolation under strict mode with the repo TypeScript. CI is authoritative.

## Submission status / payment

- Submitted as upstream PR #10284 on 2026-10-06. Project AI policy followed: AGENTS.md requires an AI assistance disclosure in the PR description, and one is included.
- No bounty posted on the issue; fix offered freely, tips pointer in the PR footer. $0 requested, $0 received.
