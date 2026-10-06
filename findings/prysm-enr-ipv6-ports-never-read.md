# OffchainLabs/prysm — peer ENR tcp6/udp6/quic6 ports are never read; IPv6-only peers are never dialed

- **Project:** OffchainLabs/prysm (Ethereum consensus client; Go), sector 2 (crypto infra)
- **Issue:** [#17613](https://github.com/OffchainLabs/prysm/issues/17613) — filed 2026-10-03, 0 comments, unassigned, no competing PR (verified twice, incl. immediately before opening the PR)
- **PR:** [#17626](https://github.com/OffchainLabs/prysm/pull/17626) — OPEN / MERGEABLE, base `develop`, commit 533e5a5 (GitHub-verified signature). CLA-assistant shows "not signed" — signing is Kyle's step (legal), not done by the agent.
- **Payment:** no bounty posted on the issue; fix offered freely with tips welcome via the PR footer. $0 requested, $0 received.

## Bug

When Prysm builds dial addresses from a peer's ENR, `getPort` in
`beacon-chain/p2p/discovery.go` read only the `tcp`, `udp` and `quic` keys,
while `retrieveMultiAddrsFromNode` pairs the returned port with
`node.IP()` — go-ethereum's *selected* IP. Two results, both reproduced in
the issue from isolated-netns runs against Lighthouse/Teku peers:

- an IPv6-only peer (`ip6` + `tcp6`, no `tcp`) produced no dial address at
  all and was never dialed (0 of 3 runs);
- a dual-stack peer whose `tcp6` differs from `tcp` (192.168.77.2/tcp 30304,
  2001:db8::2/tcp6 30324) was dialed on `/ip6/2001:db8::2/tcp/30304` and
  refused (3 of 3).

`convertToUdpMultiAddr` had the same family mix-up in the other direction:
it paired both the `ip4` and the `ip6` address with `node.UDP()`, which
go-ethereum resolves against the selected family only — the non-selected
family's address could carry the other family's UDP port.

## Fix

- `getPort` selects the port entry by the family of the node's selected IP:
  for IPv6 endpoints the `tcp6`/`udp6`/`quic6` entry (new `quic6Protocol`
  ENR type; `enr.TCP6`/`enr.UDP6` from go-ethereum) takes precedence,
  falling back to the IPv4 entry — mirroring go-ethereum's `enode.Node`
  selection (`setIP6` loads TCP6/UDP6 with TCP/UDP fallback). IPv4
  endpoints are byte-for-byte the old behaviour.
- `convertToUdpMultiAddr`: the IPv4 address takes the `udp` entry, the
  IPv6 address takes `udp6` when present (previous `node.UDP()` value as
  fallback).
- Changelog fragment `changelog/kshot3000_fix-enr-ipv6-ports.md` per
  Prysm's unclog requirement.

## Proof (red → green)

Six new tests in `beacon-chain/p2p/discovery_test.go` (Go 1.26.5):

- Unpatched logic (pristine `getPort`/`convertToUdpMultiAddr` + the new
  `quic6` type so the tree compiles): `TestGetPort_IPv6OnlyPeer`,
  `TestGetPort_DualStackPrefersIPv6Ports` (the reporter's exact case),
  `TestRetrieveMultiAddrsFromNode_IPv6OnlyPeer`,
  `TestConvertToUdpMultiAddr_PairsPortsByFamily` all **FAIL**; the two
  controls (`TestGetPort_IPv6FallsBackToIPv4Entries`,
  `TestGetPort_IPv4IgnoresIPv6Entries`) pass.
- Patched: all 6 pass, plus pre-existing `TestGetPort_ZeroPortTreatedAsAbsent`
  and `TestIPV6Support` — 8/8. `gofmt`/`go vet` clean.
- Full `go test ./beacon-chain/p2p/`: the only failures are 8
  network-dependent tests (`TestStartDiscV5_*`, `TestListenForNewNodes`,
  `TestHostIsResolved`, `TestVerifyConnectivity`, `TestCreateLocalNode`,
  `TestPeer_BelowMaxLimit`,
  `TestService_BroadcastAttestationWithDiscoveryAttempts`) that fail
  **identically on pristine `develop` fea24b4** in this sandbox (no usable
  external networking; two are on the repo's own known-flaky list,
  per an in-repo changelog fragment). Disclosed in the PR body.

## Sector-2 sweep notes (run 112, 2026-10-06)

~30 infra/DeFi queues re-checked. Rejects: teku #11412 (filed today;
assigned to tbenr + cross-referenced, and Java — no JDK in sandbox);
besu #11475/#11474/#11480 (Java, no JDK; #11480 spells its own pattern
fix); lighthouse #10214 (known SSE-capacity design item), #10201
(discv5 dial-fallback, Rust, 1 comment — plausible future target);
prysm #17619 (live-validator timing, unverifiable locally); nitro
#4760 → PR #4761 (known); wormhole fresh = live-network re-observation
requests; celestia fibre items are maintainer audit work; cometbft /
cosmos-sdk / aave / uniswap / chainlink / across / hyperlane / near /
stacks / aptos queues stale, empty, or maintainer territory; reth fresh
items are our own #27734/#27735.
