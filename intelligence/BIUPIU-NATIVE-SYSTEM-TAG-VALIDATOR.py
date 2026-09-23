"""Validate the canonical native-system catalogue and tag vocabulary.

Static repository validation only. It never claims runtime capability.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = ROOT / "research/BIUPIU-NATIVE-SYSTEM-CATALOGUE-v1.0.json"
TAG_SCHEMA = ROOT / "research/BIUPIU-NATIVE-SYSTEM-TAG-SCHEMA-v1.0.md"

REQUIRED = {"id","name","layer","native_code","capabilities","authority","status","runtime"}

def validate() -> dict:
    data=json.loads(CATALOGUE.read_text(encoding="utf-8"))
    errors=[]
    systems=data.get("systems",[])
    seen=set()
    for s in systems:
        missing=sorted(REQUIRED-set(s))
        if missing: errors.append(f"{s.get('id','<unknown>')}: missing {','.join(missing)}")
        sid=s.get("id","")
        if sid in seen: errors.append(f"duplicate system id: {sid}")
        seen.add(sid)
        if not sid.startswith("BPU.SYS."): errors.append(f"invalid system id: {sid}")
        if not s.get("native_code"): errors.append(f"{sid}: no native_code authority path")
        if not s.get("capabilities"): errors.append(f"{sid}: no capability set")
        if s.get("status")=="RUNTIME_VERIFIED" and s.get("runtime")!="VERIFIED":
            errors.append(f"{sid}: runtime status mismatch")
    if not TAG_SCHEMA.exists(): errors.append("tag schema missing")
    return {"ok":not errors,"system_count":len(systems),"errors":errors}

if __name__=="__main__":
    result=validate()
    print(json.dumps(result,indent=2,sort_keys=True))
    raise SystemExit(0 if result["ok"] else 1)
