# paradigmxyz/reth — discv5 discovered peer's TCP port is chosen by the local RLPx address family, not the session's (#27734)

- **Project:** paradigmxyz/reth, crate `reth-discv5` (`crates/net/discv5/src/lib.rs`)
- **Issue:** https://github.com/paradigmxyz/reth/issues/27734 — filed 2026-10-05 with a full isolated-netns reproduction table (official v2.7.0 binary), 0 comments, unassigned, no competing PR (verified via pulls list + issue timeline: no cross-references). Sibling #27649 is a different mechanism (address forwarding in `crates/net/network/src/discovery.rs`), already covered by the reporter's PR #27731 — not duplicated.
- **Sector:** (2) crypto infra / DeFi / chains — run 57, 2026-10-05

## Bug

`Discv5::try_into_reachable` builds the dialable `NodeRecord` from the session socket's IP (`socket.ip()`) but selects the TCP port by the **local node's** RLPx listen family: `IpMode::Ip4 => enr.tcp4()`, `IpMode::Ip6 => enr.tcp6()`, falling back to the session's UDP port when that field is absent. When the session's family differs from the local listen family, the IP and port do not belong together (issue's table: both mismatched rows connect 0 of 3; the reporter's count of the 2026-10-05 `all.mainnet.ethdisco.net` ENR list found 54 IPv4-session peers that would get wrong ports under an IPv6 local `--addr`). The `DualStack` local mode also hit `unimplemented!()` on this path. Verified verbatim on main `42fa3c5` — the exact commit the issue cites as unchanged.

## Fix (branch `Kshot3000/reth@fix/27734-discv5-session-family-tcp-port`, commit 63a1c8d)

Pair the port with the address it belongs to — select by the **session socket's** family, per the issue's stated expectation:

- IPv4 session → `enr.tcp4()`
- IPv6 session → `enr.tcp6()`, falling back to `enr.tcp4()` when no `tcp6` is advertised
- No matching TCP port in the ENR → the long-standing fallback to the session's UDP port (unchanged)

This also removes the `unimplemented!()` DualStack panic from this path. `rlpx_ip_mode` is untouched elsewhere (local ENR construction + `ip_mode()` accessor keep their meaning: how the *local* node advertises itself).

## Verification (red → green, Rust 1.98.1)

New regression tests in the crate's existing test module (3 tests: both mismatched rows of the issue's table under both local modes; the IPv6-session `tcp` fallback; the missing-port UDP fallback control):

- **Unpatched:** 2 fail exactly as reported — IPv6 session with local IPv4 mode dials 30304 (`tcp`) instead of 30306 (`tcp6`); a `tcp`-only ENR over an IPv6 session falls back to the session UDP port 30307 instead of 30304. The UDP-fallback control passes.
- **Patched:** all 3 pass; full `reth-discv5` lib suite 15 passed with the only failure `test::discv5`, which fails **identically on the pristine tree** in this sandbox (it needs live UDP session establishment between two nodes — verified via `git stash` A/B) and is disclosed in the PR; CI authoritative for that one.
- `cargo clippy -p reth-discv5 --lib --tests` clean; `cargo fmt -p reth-discv5` applied.

## Submission status

**PR #27735 OPEN** (2026-10-05): https://github.com/paradigmxyz/reth/pull/27735 — follows the repo's AGENTS.md (conventional title, regression coverage in existing tests, affected package checked first). Spare candidate logged for a later sector-2 run: OffchainLabs/prysm #17613 (same ENR-port family theme, Go).

## Payment

None — no bounty posted on #27734; fix offered freely with tips welcome. $0 requested, $0 received.
