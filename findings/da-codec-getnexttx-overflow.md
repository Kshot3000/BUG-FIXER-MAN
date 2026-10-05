# scroll-tech/da-codec — `getNextTx` panics on an overflowing RLP payload length

- **Project:** scroll-tech/da-codec (Scroll L2 DA blob codec, Go)
- **Issue:** [#71](https://github.com/scroll-tech/da-codec/issues/71) — "DecodeBlob panics on an overflowing RLP transaction length", filed 2026-09-23 by trackoor (canonical-encoding audit cluster), unassigned, no competing PR. Maintainer Thegaram confirmed the report is factually accurate (2026-09-23) while downplaying impact; the issue stayed open.
- **PR:** [#72](https://github.com/scroll-tech/da-codec/pull/72) — OPEN / MERGEABLE (2026-10-04)
- **Payment:** none posted on the issue; fix offered freely, tips welcome. $0 requested, $0 received.

## Bug

In the long-form branch of `getNextTx` (`encoding/da.go`), the RLP payload length is read as `uint64`, then narrowed to `int` for both the bounds check and the slice:

```go
payloadLen := binary.BigEndian.Uint64(lenBytes)
if length < index+1+lenPayloadLen+int(payloadLen) { ... }
txBytes = append(txBytes, bytes[index:index+1+lenPayloadLen+int(payloadLen)]...)
```

A declared length of 2^63 narrows to a negative `int` (and lengths near 2^63 wrap in the header-plus-length addition), so the bounds check passes and the slice panics — a malformed tx inside a v7 blob crashes `Codec.DecodeBlob` instead of returning an error. Sibling check: this is the only attacker-controlled `uint64`→`int` narrowing in the repo (codecv0's length is a `uint32`).

## Proof (red → green, main 5492978 = the commit the issue cites)

Reproduction with the issue's exact bytes `ff8000000000000000` (long-form header, 8-byte length declaring 2^63 payload bytes, none present):

- Unpatched: `panic: runtime error: slice bounds out of range [:-9223372036854775799]` — character-for-character the panic in the issue report.
- New regression test `TestGetNextTxPayloadLengthOverflow` (4 cases: 2^63, MaxUint64, 2^63−1, plain over-length control): unpatched, the three overflow cases panic and the control already errors; patched, all four return `errSmallLength`.
- Full suite: `go test ./...` ok; `go test -race -gcflags="-l" ./encoding/` (Makefile flags) ok (86s); gofmt/go vet clean. (One earlier backgrounded race run failed while overlapping other heavy sandbox work; two subsequent foreground race runs pass — treated as a load flake, disclosed here for honesty.)

## Fix

Compare the declared length against the remaining input without narrowing first: `if payloadLen > uint64(length-index-1-lenPayloadLen)` → `errSmallLength`. The header length is already bounds-checked above, so the subtraction cannot underflow; after the check `payloadLen` provably fits in an `int` and the existing slice code is unchanged. First attempt used an addition-based uint64 comparison, which itself wraps for MaxUint64 — the test caught it and the subtraction form replaced it.

Patch: `fixes/da-codec-getnexttx-overflow.patch` (branch `Kshot3000/da-codec@fix/71-getnexttx-overflow`, commit 20c7a43).

## Same-run sector-2 rejects (trackoor cluster follow-through)

- MystenLabs/ts-sdks #1283/#1284 (BCS boolean / ULEB128 canonicality): CLOSED — fixed by ts-sdks PR #1290.
- LFDT-Lineth/lineth-monorepo #4003/#4004 (v0 blob decompression panics): still open, 0 comments — heavy monorepo, held as future candidates.
- polydawn/refmt #69 (CBOR non-canonical): open, 0 comments — lenient-vs-strict decoding is a maintainer philosophy call; deprioritized.
- near/borsh-rs #384 (unbounded recursion on nested input): open, 0 comments — fix is a depth-limit design decision; deprioritized.
