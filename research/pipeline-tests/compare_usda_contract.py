#!/usr/bin/env python3
"""Compare the canonical Gate 6 scene contract against the minimal USDA fixture."""
import json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
usd=(ROOT/"research/pipeline-tests/usd/minimal_scene.usda").read_text(encoding="utf-8")
expected=json.loads((ROOT/"research/pipeline-tests/expected_scene_contract.json").read_text(encoding="utf-8"))
def check(c,m):
    if not c: raise SystemExit("CONTRACT FAILED: "+m)
check('defaultPrim = "BiupiuScene"' in usd,"default prim")
check('def Xform "Environment"' in usd,"Environment prim")
check('def Xform "VehiclePlaceholder"' in usd,"VehiclePlaceholder prim")
check('def Camera "AnimatedCamera"' in usd,"AnimatedCamera prim")
check('timeCodesPerSecond = 24' in usd,"24 fps")
check('startTimeCode = 1' in usd and 'endTimeCode = 48' in usd,"frame range")
for item in expected["animatedAttributes"]:
    name=item["path"].split("/")[-1]
    check(name in usd, "animated prim "+item["path"])
    check("xformOp:translate.timeSamples" in usd, "animated translate samples")
check(len(re.findall(r'\b1:\s*\(',usd)) >= 2 and len(re.findall(r'\b48:\s*\(',usd)) >= 2,"frame samples")
print("CONTRACT PASSED: canonical Gate 6 scene contract matches minimal USDA fixture.")
