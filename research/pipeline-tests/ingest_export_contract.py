#!/usr/bin/env python3
"""Gate 8: validate an externally supplied machine-readable export artifact.

The artifact is intentionally JSON so exporters/adapters from Blender, Unreal,
OpenUSD tooling, or other DCCs can converge on one comparison interface.
"""
import json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
expected=json.loads((ROOT/"research/pipeline-tests/expected_scene_contract.json").read_text())
if len(sys.argv) != 2:
    raise SystemExit("Usage: ingest_export_contract.py <actual-export.json>")
p=Path(sys.argv[1])
if not p.is_file():
    raise SystemExit("EXPORT ARTIFACT MISSING: "+str(p))
actual=json.loads(p.read_text(encoding="utf-8"))

errors=[]
if actual.get("schemaVersion") != expected["schemaVersion"]:
    errors.append("schemaVersion mismatch")
for key in ("rootPrim","fps","startFrame","endFrame"):
    if actual.get(key) != expected[key]:
        errors.append(f"{key} mismatch: expected {expected[key]!r}, got {actual.get(key)!r}")

exp_prims={x["path"]:x["type"] for x in expected["prims"]}
act_prims={x["path"]:x.get("type") for x in actual.get("prims",[])}
for path,typ in exp_prims.items():
    if path not in act_prims: errors.append("missing prim: "+path)
    elif act_prims[path] != typ: errors.append(f"type mismatch: {path}")
for path in act_prims:
    if path not in exp_prims: errors.append("unexpected prim: "+path)

exp_anim={(x["path"],x["attribute"]):x["samples"] for x in expected["animatedAttributes"]}
act_anim={(x["path"],x["attribute"]):x.get("samples") for x in actual.get("animatedAttributes",[])}
for key,samples in exp_anim.items():
    if key not in act_anim: errors.append("missing animated attribute: "+str(key))
    elif act_anim[key] != samples: errors.append(f"sample-time mismatch: {key}")

if errors:
    print("EXPORT CONTRACT FAILED")
    print("\n".join("- "+e for e in errors))
    raise SystemExit(1)

print("EXPORT CONTRACT PASSED")
print("Provenance:", actual.get("provenance", "UNSPECIFIED"))
