# microsoft/TypeScript #64661 — class names `eval` / `arguments` not reported in strict mode

- **Project:** microsoft/TypeScript (native Go port, `tsc/internal/binder`)
- **Issue:** https://github.com/microsoft/TypeScript/issues/64661 (filed 2026-10-06 by JLHwung, 0 comments at sweep time, unassigned, no competing PR)
- **Bug:** `bindClassLikeDeclaration` never calls `checkStrictModeEvalOrArguments`, so a class named `eval` or `arguments` gets no diagnostic even though all class code is strict-mode code (ECMA-262 §11.2.2, §13.1.1) and the emitted JS is a runtime `SyntaxError`. Every other binding form (variables, parameters, function names) is checked.
- **Sector:** (4) general company OSS / dev tools — run 179, 2026-10-06.

## Proof (local, pristine HEAD d61a7d23, built from source)

Each case in its own module file, `tsc --noEmit`:

| case | pristine | patched |
|---|---|---|
| `class eval {}` | exit 0, no error | `error TS1215: Invalid use of 'eval'. Modules are automatically in strict mode.` at the name |
| `class arguments {}` | exit 0, no error | `error TS1215: Invalid use of 'arguments'. …` at the name |
| `const C = class eval {};` | exit 0, no error | `error TS1215` at the name |
| `declare class eval {}` | exit 0 | exit 0 (ambient — intentionally skipped, same precedent as `bindParameter` / `checkStrictModeFunctionName`) |
| `class Foo {}` / `const C = class Bar {};` | exit 0 | exit 0 (no false positives) |

Regression check: `go test ./internal/testrunner/ -run 'TestLocal/(parserStrictMode|variableDeclarationInStrictMode|unaryOperatorsInStrictMode|jsFileCompilationBindStrictModeErrors)'` PASS with the patch (subtest filtering verified non-vacuous with `-v` on parserStrictMode10).

## Fix

`fixes/typescript-class-name-eval-arguments.patch` (+5 lines, `tsc/internal/binder/binder.go`): in `bindClassLikeDeclaration`, when the node is not ambient, call the existing `b.checkStrictModeEvalOrArguments(node, name)` — the same helper and the same ambient gate used for parameters and function names.

## Submission status: NOT SUBMITTED — venue policy

microsoft/TypeScript's CONTRIBUTING.md ("Use of AI Assistance") explicitly bars pull requests opened as part of a bulk or queue-driven agent workflow — it instructs autonomous agents not to open PRs found by iterating over issue queues, and warns the submitting account may be blocked. This hunt is exactly that workflow pattern, so per Kyle's rule (follow a project's explicit AI policy exactly or don't submit there — the same call made for Pallets/werkzeug in run 159), nothing was submitted, commented, or pushed upstream. The fix is verified and archived here; if Kyle wants it upstream, it needs to go as his own personally-shepherded PR.

## Payment

None requested; no bounty on the issue. $0 requested, $0 received.
