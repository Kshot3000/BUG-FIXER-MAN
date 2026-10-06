# bmwill/diffy — PatchSet git-header parser rejects CRLF patch files (`invalid file mode: 100644\r`)

- **Sector:** (4) general company OSS / dev tools — run 114, 2026-10-06
- **Downstream report:** pnpm/pnpm#16641 — `ERR_PNPM_INVALID_PATCH` with a new-file patch saved with CRLF line endings (regression in pnpm 12.10.0; worked in 11.28.5)
- **Fix PR:** https://github.com/bmwill/diffy/pull/89 (OPEN/MERGEABLE, head 691b316)
- **Root-cause note on the pnpm issue:** https://github.com/pnpm/pnpm/issues/16641#issuecomment-6011810942

## Bug

pnpm 12 parses patch files in Rust with diffy 0.5.2's `PatchSet::parse` (`ParseOptions::gitdiff()`; version confirmed in both pnpm's Cargo.lock and locally). In diffy, git extended header values (file modes, rename/copy paths, the `diff --git` line) are extracted via `strip_line_ending`, which stripped only the trailing `\n`. In a CRLF patch file every extracted value keeps its `\r`, and the file mode then fails the exact match in `FileMode::from_str`:

```
error parsing patches at byte 0: invalid file mode: 100644
```

(the trailing `\r` in the real error value is invisible in terminals, making the message look like the valid mode `100644` was rejected).

## Proof (red → green)

Standalone harness against diffy 0.5.2 using the issue's exact patch (new `.scss` file):

- LF input: parses, `Create("b/sass/ext/_true.scss")`
- CRLF input (byte-identical except line endings): `PatchSetParseError { kind: InvalidFileMode("100644\r"), span: 0..0 }`
- A CRLF mode-change patch (`old mode 100644` / `new mode 100755`) fails identically; both parse after the fix, with operations and modes matching the LF equivalents exactly.

The helper's own TODO already noted GNU patch strips trailing CRs from CRLF patches. Fix: `strip_line_ending` also strips a trailing `\r` — scoped to git extended header lines only; hunk content is untouched (a patch whose content legitimately ends lines in `\r` keeps it). This complements diffy#87 (merged), which fixed the same class of bug for `---`/`+++` headers in the classic `Patch` parser.

## Fix + tests

- `src/patch_set/parse.rs`: strip `\r` after `\n` in `strip_line_ending` (+ comment updated).
- New regression tests `crlf_new_file_with_content` and `crlf_mode_only_change` in `src/patch_set/tests.rs`: both fail unpatched, pass patched.
- Full suite `cargo test --all-features`: 131 lib tests pass (129 before + 2 new), integration + doc tests pass; `cargo fmt --check` clean.

## Submission

- PR bmwill/diffy#89 via fork Kshot3000/diffy, branch `fix/patch-set-crlf-git-headers`. No bounty (diffy has none; pnpm pays none for this issue) — fix offered freely, tips welcome via PR footer.
- One root-cause comment posted on pnpm/pnpm#16641 so pnpm can pick the fix up via a diffy bump; noted there that pnpm-side line-ending normalization was considered and rejected (it would corrupt hunk content lines that legitimately end in `\r`).

## Same-run sector-4 rejects

- sqlalchemy#13637 (PostgreSQL multihost bracketed-IPv6 URL ValueError): real and reproduced in-thread, but the venue gates PRs behind a maintainer "open for pull requests" label — the first fix PR (#13653) was auto-closed for exactly that, and the issue is still unlabeled. Watch candidate only; do not PR until labeled.
- sqlalchemy#13650: maintainer handling internally; #13651 feature/operator territory.
- black#5488: commenter who traced the preview-style mechanism stepped back; deep formatter internals, still unclaimed — not attempted.
- rich#4233: still held (only the reporter's PR offer; rich's AI policy needs maintainer approval first). rich#4229: another contributor's fix branch already offered.
- pre-commit#3664: maintainer explicitly bars AI-agent PRs on the issue — venue closed to us.
- mvdan/sh#1429: maintainer previously closed Kyle's PR as an unwanted drive-by — skip.
- git-lfs#6358: maintainer could not reproduce; contested auth-flow report.
- rclone#10047: claimed in-thread by another contributor; #10049 filed today, VFS-deep.
- Everything else fresh was already PR'd: starlette#3630, mkdocs#4221→#4222, yq#2884→#2885, vite#23652→#23662, ansible-lint#5204→#5205, pnpm#16638→#16639, syncthing#10909 (maintainer-contested perf framing).

## Watch (run 114)

NO changes vs run 113. All open PRs direct REST-verified in the same states (dentalpin#599 / type-coverage#155 MERGED known; NiceGUI#6372 APPROVED stands; vyper#5294 reviews 4 / comments 1 — the run-113 Sporarum item; memos#6435 comments 2 = CodeRabbit summary + our run-112 follow-up; prysm#17626 comments 1 = CLA-assistant, Kyle's step). Expensify identical: #102072 60, #101684 42, #102044 30, #102226 38 — no selection/hire, no melvin-bot prompt to Kshot3000. NEW: diffy#89 added to watch. $0 requested / $0 received.
