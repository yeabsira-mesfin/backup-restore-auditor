# Backup Restore Auditor

I need to know which backup can actually be restored within a read budget when an incremental backup depends on older copies.

## Required decision command

`python backup.py restore INPUT.json` reads a raw JSON object as shown under input in examples/. Each record is a backup with a unique id, integer day, nonnegative size, boolean verified, and parent (null for full backups). A candidate is usable only if its complete chain exists, is verified, has strictly increasing days from root to tip, and has total size at most budget. Choose the usable tip with greatest day, breaking ties by smallest id. Return the root-to-tip id list, or []. An invalid chain eliminates only its dependent candidates. Reject duplicate ids and invalid scalar types.

Print the JSON decision to stdout. For invalid input return nonzero and write a readable diagnostic to stderr. Use exact JSON types, including rejecting booleans where integers are required. Input ordering must not affect the result. Preserve the inventory CLI.

## Reporting and integration work

Implement a separate explain command that classifies every tip as usable, missing-parent, cycle, day-order, unverified or over-budget. Check in that priority order, with usable as the fallback. Compute chain costs once per node where possible. Add a 10,000-node linear-chain test and avoid recursion limits. Document the reporting CLI, its input schema, one working example, and failure behavior. Exercise both success and failure paths through subprocess tests. Keep input files read-only. Use deterministic output and temporary paths for tests.

## Estimated implementation session

Allow 40 minutes for input modeling, 90 for the decision algorithm, 65 for the reporting feature, 50 for validation and edge cases, 60 for integration and regression tests, and 30 for documentation and reviewer evidence. Total estimate: 5 hours 35 minutes. Record actual time worked.
