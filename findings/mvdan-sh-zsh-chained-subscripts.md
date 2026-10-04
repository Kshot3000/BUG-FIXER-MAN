# mvdan/sh — zsh chained subscripts rejected by the parser

- **Project:** mvdan/sh (shfmt) — https://github.com/mvdan/sh
- **Issue:** #1361 — "zsh: multiple parameter subscripts fail to parse" https://github.com/mvdan/sh/issues/1361
- **Submission:** PR #1430 https://github.com/mvdan/sh/pull/1430 (fork Kshot3000/sh, branch `fix-zsh-chained-subscripts`, two commits per the repo's test-first convention)
- **Bounty:** none — fix offered freely, tips welcome via this repo's README.
- **Status:** OPEN, awaiting maintainer review.

## Bug

In zsh, subscripts chain: `${var[1][2]}` subscripts the result of the
previous subscript (the zsh manual uses this exact form as its
subscripting example). The parser only allowed one subscript and
rejected the second `[` in every language mode:

```
$ printf '%s\n' 'var=(foo)' 'echo ${var[1][2]}' | shfmt -ln=zsh
<stdin>:2:14: not a valid parameter expansion operator: `[`
```

Real zsh 5.9 prints `o` for that input.

## Proof (red → green)

- Reproduced on master 9a79a44 with the reporter's exact input, and at
  the reporter's version; single subscript `${var[1]}` worked.
- Semantics verified against the locally installed zsh 5.9: chained and
  nested forms agree for `${var[1][2]}`, `${arr[-1][2]}`,
  `${s[1,3][2]}`, triple chains, and trailing `:-` / `#` operators;
  the short form `$var[1][2]` treats the second `[2]` as a glob in
  zsh, so it is deliberately unchanged.
- Also checked and rejected as targets in the same sweep:
  mvdan/sh #1429 (`$%` in zsh) is already fixed on master by the
  maintainer (0f6fdc0b, with tests) though the issue is still open;
  yq #2881/#2884/#2851/#2853 and direnv #1619 all already have
  competing fix PRs.

## Fix

`${var[1][2]}` is equivalent by definition to the nested form
`${${var[1]}[2]}`, which the parser/printer already support. After the
first subscript, each further `[...]` in LangZsh wraps the expansion
parsed so far in a new `ParamExp` whose `NestedParam` is the previous
one — no AST changes. Inner expansions share the outer `Rbrace`
position (no `}` of their own in the source). Printing normalizes the
chained form to the nested form, stable across re-parses. Bash/mksh/
POSIX still reject the second subscript with the same errors.

## Tests

- Commit 1 adds an error case asserting the old wrong behavior
  (`For #1361`); commit 2 flips it and adds a file test covering the
  chained and nested forms (`Fixes #1361`).
- `go test ./syntax/ ./syntax/typedjson/` passes; `gofmt -s` and
  `go vet` clean; 30s `FuzzParsePrint` run clean.
- `go test ./interp/` chmod-permission failures in this container
  reproduce identically on unmodified master (tests run as root);
  disclosed in the PR.
