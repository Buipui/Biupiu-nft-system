#!/usr/bin/env python3
"""Validate a Biupiu Machine Capability document against the canonical JSON Schema."""
from __future__ import annotations
import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError as exc:
    raise SystemExit("jsonschema is required; install with: python -m pip install jsonschema") from exc

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "machine-capability-v1.0.schema.json"

def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_machine_capability.py <capability.json>", file=sys.stderr)
        return 2
    target = Path(sys.argv[1])
    if not target.is_absolute():
        target = ROOT / target
    with SCHEMA.open(encoding="utf-8") as fh:
        schema = json.load(fh)
    with target.open(encoding="utf-8") as fh:
        document = json.load(fh)
    jsonschema.Draft202012Validator.check_schema(schema)
    validator = jsonschema.Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(document), key=lambda e: list(e.path))
    if errors:
        for error in errors:
            location = ".".join(map(str, error.path)) or "<root>"
            print(f"INVALID {location}: {error.message}", file=sys.stderr)
        return 1
    print(f"VALID {target}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
