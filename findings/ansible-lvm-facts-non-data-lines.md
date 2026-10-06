# Ansible — get_lvm_facts IndexError on non-data lines in LVM output

- **Project:** ansible/ansible (IT automation platform, Python)
- **Issue:** [#87640](https://github.com/ansible/ansible/issues/87640) — `IndexError('list index out of range')` gathering `mounts` from unexpected `lvs` output; open, unassigned, no competing fix PR (the only related open PR, #87189, adds duplicate-name warnings and does not touch this crash)
- **PR:** [#87642](https://github.com/ansible/ansible/pull/87642) — OPEN (2026-10-05, base `devel`, fork branch `Kshot3000/ansible@fix/87640-lvm-facts-non-data-lines`, commit `c0c0480`)
- **Bounty:** none posted; fix offered freely, tips welcome via the PR footer.
- **Note:** the fix was developed and verified in an earlier run that timed out before submitting; this entry completes that interrupted submission (run-94 timeout item).

## Bug

`LinuxHardware.get_lvm_facts()` (`lib/ansible/module_utils/facts/hardware/linux.py`) parses the stdout of `vgs`, `lvs` and `pvs` assuming every line is a comma-separated data row. LVM utilities can print informational lines to stdout — the reporter hit:

```
  Retrying metadata scan.
  osd-block-5651...,ceph-...,-wi-a-----,7153.95,,,,,,,,
```

For the informational line, `"Retrying metadata scan.".split(',')` yields a single field, so `items[1]` (`vg_name = items[1]`) raises `IndexError: list index out of range`. The exception aborted hardware fact gathering entirely — `ansible_mounts` silently came back empty on the reporter's Ceph storage node.

## Fix

Skip lines with fewer fields than a valid data row in all three parsers, immediately after splitting:

- `vgs`: require ≥ 7 fields
- `lvs`: require ≥ 11 fields
- `pvs`: require ≥ 6 fields

Valid rows parse exactly as before. A changelog fragment (`changelogs/fragments/87640-lvm-facts-non-data-lines.yml`) is included per Ansible convention.

## Proof (red → green)

New `TestFactsLinuxHardwareGetLvmFacts.test_get_lvm_facts_skips_non_data_lines` (`test/units/module_utils/facts/hardware/test_linux.py`) mocks `vgs`/`lvs`/`pvs`, with the report's exact `Retrying metadata scan.` line in the `lvs` output:

- Unpatched: test fails with `IndexError: list index out of range` at `lib/ansible/module_utils/facts/hardware/linux.py:906` (`vg_name = items[1]`) — the exact failure from the issue.
- Patched: full test file passes — **12/12** (`pytest test/units/module_utils/facts/hardware/test_linux.py`), and the parsed facts contain both valid LVs, the VG, and the PV around the skipped line.
