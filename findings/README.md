# Findings

One file per **verified** find, named `<project>-<short-slug>.md`.

A find is only recorded here when it has been reproduced locally with proof. Candidates that have not been verified go in the internal pipeline, not here.

Use this template:

```markdown
# <Project> — <bug title>

- **Project / repo:** <link>
- **Issue / bounty:** <link, or "found by audit">
- **Found:** <date>
- **Severity / type:** <e.g. correctness, crash, security — with scope note>
- **Bug:** <what is wrong, in plain terms>
- **Proof:** <failing test / log / minimal repro — or a link to it>
- **Fix:** <what was changed; patch in ../fixes/ when applicable>
- **Tests:** <what was run, result>
- **Submission:** <PR / platform report link and status — submitted, merged, resolved, rejected>
- **Payment:** <requested: amount + channel | received: amount + date — never list a request as a receipt>
- **Disclosure:** <private until resolved / public with project consent / n-a>
```
