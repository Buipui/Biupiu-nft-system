# Biupiu Housekeeping Tooling

This directory defines the repository housekeeping contract.

## Intended checks

A future executable housekeeping runner should report, without destructive changes:

- malformed JSON;
- broken local Markdown links;
- duplicate identifiers;
- duplicate research-record hashes where available;
- missing provenance fields in governed records;
- stale release/index references;
- TODO/FIXME markers in first-party code;
- generated/build artifacts accidentally tracked;
- obvious secret-pattern matches;
- inconsistent version/date metadata.

Vendor directories are excluded from automatic TODO/FIXME remediation.

## Non-destructive rule

The housekeeping runner should produce a report first. Any deletion, migration, or research supersession must be explicit and reviewable.

## Suggested command

`python tools/housekeeping/run.py`

The runner may be expanded as the repository's package structure stabilizes.
