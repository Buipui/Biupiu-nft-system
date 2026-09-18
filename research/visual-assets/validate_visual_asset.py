#!/usr/bin/env python3
"""Validate a Biupiu visual asset manifest and enforce licence/provenance gates."""
import json, sys
from pathlib import Path

def validate_basic(doc):
    required = {"asset_id","asset_type","source","licence","files","provenance","pipeline"}
    missing = required - doc.keys()
    errors = [f"missing required field: {x}" for x in sorted(missing)]
    if doc.get("licence", {}).get("status") != "verified":
        errors.append("licence.status must be verified for production promotion")
    if not doc.get("source", {}).get("url"): errors.append("source.url is required")
    if not doc.get("provenance", {}).get("acquired_at"): errors.append("provenance.acquired_at is required")
    if not isinstance(doc.get("provenance", {}).get("transformation_log"), list): errors.append("provenance.transformation_log must be an array")
    if not doc.get("pipeline", {}).get("targets"): errors.append("pipeline.targets must contain at least one target")
    return errors

def main():
    if len(sys.argv) != 2:
        print("usage: validate_visual_asset.py <manifest.json>"); return 2
    doc = json.loads(Path(sys.argv[1]).read_text())
    errors = validate_basic(doc)
    if errors:
        print("\n".join("FAIL: "+e for e in errors)); return 1
    print(f"PASS: {doc["asset_id"]} is eligible for production-pipeline review.")
    return 0

if __name__ == "__main__": raise SystemExit(main())