# ethers.js — RLP decoder accepts a single byte wrapped in a string header

- **Project:** ethers-io/ethers.js (ethers v6) — https://github.com/ethers-io/ethers.js
- **Issue:** #5194 — "RLP decoder accepts a single byte wrapped in a string header" https://github.com/ethers-io/ethers.js/issues/5194 (filed 2026-09-23 by trackoor, 0 comments, unassigned, no competing PR; part of the reporter's cross-repo canonical-decoding audit, umbrella #5196 since closed)
- **Submission:** **PR #5198 OPEN (2026-10-04): https://github.com/ethers-io/ethers.js/pull/5198** (fork branch `Kshot3000/ethers.js@fix/5194-rlp-single-byte-canonical`, commit 1f43dc2)
- **Bounty:** none — OSS fix offered freely, tips welcome.
- **Status:** PR #5198 OPEN, awaiting maintainer review + CI.

## Bug

RLP encodes a single byte below `0x80` as itself. `decodeRlp` (`src.ts/utils/rlp-decode.ts`) accepted that byte wrapped in a string header — a second encoding of the same value that the library's own encoder never produces, so decode/encode were not symmetric on it. Any system treating the encoding as identifying (content addressing, signature preimages, deduplication) can be shown two encodings of one value.

## Proof (main 3ea4c22, v6.17.0; repro harness against the built `lib.esm`)

Unpatched — all accepted, all re-encode differently:

```
FAIL 0x8118   decoded="0x18"    re-encode=0x18    REENCODE-DIFFERS   (the issue's witness)
FAIL 0x812c   decoded="0x2c"    re-encode=0x2c    REENCODE-DIFFERS   (umbrella witness)
FAIL 0xc28118 decoded=["0x18"]  re-encode=0xc118  REENCODE-DIFFERS   (nested in a list)
FAIL 0xb80118 decoded="0x18"    re-encode=0x18    REENCODE-DIFFERS   (long-form string header)
```

Canonical controls decode and round-trip byte-identically both before and after the fix: `0x18`, `0x8180` (byte 0x80 *needs* the header), `0x81ff`, `0x80`, `0xc20102`, `0xc0`.

## Fix

In `_decode`, both string branches (short-form `0x80–0xb7` and long-form `0xb8–0xbf`) now reject a one-byte payload whose byte is below `0x80`:

```ts
assertArgument(length !== 1 || data[offset + 1] >= 0x80,
    "non-canonical rlp: single byte below 0x80 must be encoded as itself", "data", hexlify(data));
```

Error shape matches the repo's conventions and the sibling fix in flight: `INVALID_ARGUMENT`, message prefixed `non-canonical rlp`, argument `data`. Nested occurrences are caught because list children decode through the same `_decode`.

**Scope note:** this is the `rlp-single-byte-minimal` rule only. The sibling `rlp-length-minimal` rule (#5193) already has an open fix PR, #5197 by bingtang9 — deliberately not duplicated; the checks are independent (the only overlap is a long-form length-1 string header, which both rules reject). If #5197 merges first, this branch rebases cleanly (adjacent, non-overlapping hunks in the long-form branch).

## Tests

- 3 regression tests added to the "Test bad RLP Data" block in `src.ts/_tests/test-rlp.ts` (top-level witness, nested witness, canonical wrapped-byte controls ≥ 0x80).
- RLP suite: **130/130 passing** patched (127 baseline + 3 new).
- Downstream regression: `test-transaction` (canonical raw-transaction RLP parsing) — **51,717 passing, 0 failing**, full suite run locally to completion (5m; it outlasted two earlier bounded sampling runs, which is why the PR originally said "CI authoritative" — the PR body was updated once the full result landed).
- Patch: `fixes/ethers-rlp-single-byte-noncanonical.patch`.

## Same-run rejects (sector 1)

- ethers #5193 (non-minimal length prefixes) — fix PR #5197 already open; not duplicated.
- bitcoinjs-lib #2350 (CompactSize non-minimal) — same reporter/audit; the defect lives in the `varuint-bitcoin` dependency package, not in bitcoinjs-lib's own code, so a clean in-repo fix isn't available; umbrella #2352 also open there.
- MetaMask/core #10667 (ERC-7715 grant fails on Robinhood Chain) — root cause is a pinned `@metamask/delegation-deployments` version missing a chain entry; fix is a dependency/registry update in another package, maintainer territory, not locally verifiable end-to-end.
- MetaMask extension #46856 (wrong native balance blocks confirm) — UI/confirmation flow, no local repro path in the extension monorepo.
- family/connectkit #525 — no repro, "package broken" only.
- Rabby #4156/#4157 (standing reject, server/RPC-dependent), Cake fresh bugs (Flutter), BlueWallet fresh queue (already swept runs 16/26 — config/feature/design), Wasabi coordinator bugs (.NET coordinator logic, no toolchain-verifiable repro here), eclair #3383–#3386 (Scala protocol-acceptance features), Safe wallet monorepo #8808 (needs contract-signature chain state).
