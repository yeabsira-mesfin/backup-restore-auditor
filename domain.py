"""Domain validation for catalog evidence envelopes."""

from evidence_catalog.validation import (
    ValidationError, boolean, fields, identifier, integer, text,
)

PROJECT = 'backup-restore-auditor'


def validate_payload(payload):

    fields(payload, ("id", "day", "size", "verified", "parent"))
    identifier(payload["id"], "backup id")
    integer(payload["day"], "backup day")
    integer(payload["size"], "backup size", 0)
    boolean(payload["verified"], "verified")
    if payload["parent"] is not None:
        identifier(payload["parent"], "parent")


def example_payload():
    return {'id': 'full-01', 'day': 1, 'size': 50, 'verified': True, 'parent': None}
