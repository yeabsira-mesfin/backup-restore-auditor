# Backup Restore Auditor

I need to know which backup can actually be restored within a read budget when an incremental backup depends on older copies.

The starter inventories synthetic records. Implement the decision command and reporting workflow described in [ASSIGNMENT.md](ASSIGNMENT.md). Use Python 3.10 or newer with the standard library.

```sh
python backup.py inventory examples/depth-2/budget-0-intact.json
python -m unittest discover -s tests -v
python acceptance.py --inventory
```

Example files contain input and expected results. The acceptance runner passes only the input to your implementation.
