# gofactory — `(*T)(x)` reported even when x already points at a T

- **Project:** maranqz/gofactory — a Go analyzer (golangci-lint plugin) that checks structs are created through their factory — https://github.com/maranqz/gofactory
- **Issue:** #66 — "Skip (*T)(x) when x already points at a T" https://github.com/maranqz/gofactory/issues/66 (filed 2026-10-04 from the maintainer's review of #65; unassigned, 0 comments, "can start immediately")
- **Submission:** **PR #67 OPEN (2026-10-04): https://github.com/maranqz/gofactory/pull/67** (fork branch `Kshot3000/gofactory@fix/skip-retype-pointer-conversion`, commit 888b60e, based on main 4b2b3b2)
- **Bounty:** none — OSS fix offered freely, tips welcome.
- **Status:** PR #67 OPEN, awaiting maintainer review.

## Bug

`checkConversion` reported a conversion to `*T` whose argument already points at a `T` — it creates nothing, it only retypes an existing pointer. The skip list only covered an argument of the *identical* type, and a defined pointer type with underlying `*T` is not identical to `*T`. Asymmetric with the reverse direction (`DefinedStructPtr(p)` stays silent) and with the plain assignment `var p *nested.Struct = dp`, which is also silent. Three forms were reported as `Use factory for nested.Struct`:

- `(*nested.Struct)(dp)` with `dp DefinedStructPtr` (`type DefinedStructPtr *nested.Struct`)
- `StructPtr(dp)`, through the alias `type StructPtr = *nested.Struct`
- `(*nested.Struct)(sp)` with `sp` of an imported defined pointer type `type StructPtr *Struct`

## Proof (main 4b2b3b2, red first)

Added only the acceptance-criteria testdata (three silent forms next to `DefinedPointerConversion` in `testdata/module/simple/pointer_alias.go`, plus the imported `type StructPtr *Struct` in `testdata/module/simple/nested/nested.go`) and ran the suite unpatched:

```
analysistest.go:654: pointer_alias.go:37:6: unexpected diagnostic: Use factory for nested.Struct
analysistest.go:654: pointer_alias.go:38:6: unexpected diagnostic: Use factory for nested.Struct
analysistest.go:654: pointer_alias.go:39:6: unexpected diagnostic: Use factory for nested.Struct
```

Exactly the three retype lines failed (both the flags and plugin harness variants); every other expectation held, including the still-reported and known-false-positive cases below.

## Fix

In `checkConversion`, after the identical-type skip: if the argument's underlying type is a `*types.Pointer` whose element is identical to the target's pointee, return silently — the `T` behind the pointer was built elsewhere, where it is checked. Docs updated per the issue: the rule joins `checkConversion`'s silent-conversions list, and `pointee` now reads "builds the T behind one pointer, *unless x already points at a T*".

No bypass is lost — a pointer to another type is not a retype and stays reported.

## Verification

- Red→green in analysistest: the three forms are silent post-fix.
- Still reported, pinned with `// want`: `(*nested.Struct)(&l)` and `StructPtr(&l)` (`&l` is `*struct{}`).
- Out-of-scope case pinned as a known false positive with `// want`: a type-parameter argument `P ~*nested.Struct` — its underlying type is the constraint interface, not `*T`, so it stays reported, exactly as the issue specifies.
- Full suite: **`go test -race ./...` green**; `gofmt -l` clean; `go vet ./...` clean.
