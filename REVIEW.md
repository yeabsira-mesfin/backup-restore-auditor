# Task description

I need to know which backup can actually be restored within a read budget when an incremental backup depends on older copies. The existing Python application inventories records. Implement `python backup.py restore INPUT.json` as specified in ASSIGNMENT.md. Implement a separate explain command that classifies every tip as usable, missing-parent, cycle, day-order, unverified or over-budget. Check in that priority order, with usable as the fallback. Compute chain costs once per node where possible. Add a 10,000-node linear-chain test and avoid recursion limits.

## How to judge completion

Run `python -m unittest discover -s tests -v` and `python acceptance.py` from the repository root. All existing tests, new tests and 72 decision cases should pass. Inspect backup.py, acceptance.py, tests/, README.md and any new implementation modules. Exercise the documented reporting command with a fresh synthetic example, reverse the input records, and compare the outputs. Feed invalid types and verify a nonzero exit, a stderr diagnostic and unchanged input. Check the reporting feature independently of the example matrix.

## Other notes for reviewers

Use synthetic data and temporary files. The expected values belong only to the acceptance runner. Check the algorithm on unseen inputs and record the actual commands and results.

## Final questionnaire

Copy the new live compare problem ID from the platform. Enter actual active hours (minutes divided by 60). Primary language: Python. Task type: feature implementation and regression testing. Source: a new MIT-licensed starter prepared with Codex. Use the sections above for task description, how to judge completion and reviewer notes. Record actual outcome, completion evidence, changed files, commands, turn count, flag count and observed flag categories. Include exact quotes or turn references when explaining a flag. Leave run-specific fields open until the session ends.

## Existing baseline to preserve

The codebase now includes the evidence catalog documented in CATALOG.md. Preserve its import transactions, tenant scoping, reports, snapshots and bundle validation. The assignment adds the decision workflow and reporting described above. Verify the original inventory command, the catalog walkthrough and all existing tests after implementing the feature.
