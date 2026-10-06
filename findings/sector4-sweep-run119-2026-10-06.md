# Sector-4 sweep — run 119 (2026-10-06)

Sector: (4) general company OSS / dev tools. **No submission.**

## Watch
NO changes. All PRs direct REST-verified identical to run 118: dentalpin #599 / type-coverage #155 MERGED (known); ERCs #2045 OPEN c=1, cake #3671 OPEN c=0, electrum #11012 OPEN c=0; optimism #23214 OPEN c=0, diffy #89 OPEN c=0, prysm #17626 OPEN c=1 (CLA-assistant = Kyle's step), memos #6435 OPEN c=2 reviews 1, NiceGUI #6372 OPEN c=1 reviews 4 (evnchn APPROVED stands — awaiting merge), vyper #5294 OPEN c=1 reviews 4, ansible #87642 OPEN, vikunja #4107/#4110 OPEN. Expensify identical: #102072 60, #101684 42, #102044 30, #102226 38 — no selection/hire, no melvin-bot prompt to Kshot3000. HackerOne: ledger-only.

## Candidates assessed
- **astral-sh/ruff #29106** (filed 2026-10-05): `RUF104` unmatched-suppression-comment violations cannot be ignored — a trailing `# ruff: ignore[RUF104]` on a `# ruff: disable[...]` line is itself reported, plus a knock-on `RUF100`. Rejected: maintainer ntBre already engaged and places it in a tracked suppression-comment cluster (#26282, #21877, #23191); the fix is design-level work in the suppression machinery (which suppressions may suppress suppression diagnostics, RUF100 interplay), not a clean local fix.
- **ansible/ansible-lint #5198** (name[casing] handler regression): already fixed by open PR #5201. Rejected (PR'd).
- **ansible/ansible-lint #5190**: `--fix` rewrites `when: "{{ item.when }}"` to `when: "item.when"`, changing semantics when `item.when` itself holds a condition string. No competing PR and unassigned, but the brace-stripping transform for `when` is deliberate, the issue has no maintainer engagement (labels `new,bug`, only a reporter workaround comment), and the correct fix shape is a maintainer design call. Not attempted.
- **ansible/ansible-lint #5199**: "would be helpful if ansible-lint could catch duplicated filters" — feature request, not a verified bug. Rejected.
- **sqlalchemy/sqlalchemy #13637** (PostgreSQL multihost URL with bracketed IPv6 hosts raises ValueError): still venue-gated — labels remain `bug,postgresql,engine` with no "open for pull requests" label (the gate that auto-closed the first fix PR #13653); a third contributor has also reproduced it and pinpointed `_split_multihost_from_url`. WATCH stands; do not submit until the label lands.
- **textualize/rich #4233**: still HELD — only comment remains the reporter's PR offer; no maintainer approval under rich's AI policy.
- **cookiecutter/cookiecutter #2232** (failed `gh:` clone deletes the local template dir): farmed — seven cross-referenced PRs (#2233/#2236/#2238/#2245/#2248/#2265/#2270). **#2259** (XDG dirs) already has PR #2260. Rejected.
- Fresh `bug`-label queues re-checked across ~35 dev-tool repos (click, black, starlette, pip, pre-commit, golangci-lint, cobra, yq, BurntSushi/toml, go-toml, mvdan/sh [venue closed to us], helm, docker/cli, pytest, attrs, httpx, httpie, ansible-lint, mkdocs, spacy, fastapi, pydantic, poetry, pdm, uv): empty, stale, or already covered by earlier runs' rejects (yq #2884→PR #2885, helm #32673→PR #32676, BurntSushi/toml via PRs #486/#487, uv #22186/#22185 Rust/no-toolchain + design).

## Payment
$0 requested, $0 received.
