#!/usr/bin/env python3
"""Deterministic repository-level validator for Biupiu adapter manifests/fixtures.
Does not execute third-party solvers/simulators.
"""
import json, math, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
MANIFESTS = ROOT / "adapters/manifests"
FIXTURES = ROOT / "adapters/fixtures"
required = {
 "sundials": ("SUNDIALS-TV-001", "sundials-tv-001.json"),
 "open3d": ("OPEN3D-TV-001", "open3d-tv-001.json"),
 "assimp": ("ASSIMP-TV-001", "assimp-tv-001.obj"),
 "gazebo": ("GAZEBO-TV-001", "gazebo-tv-001.json"),
 "chrono": ("CHRONO-TV-001", "chrono-tv-001.json"),
}
errors=[]
for stem,(tv,fixture) in required.items():
    p=MANIFESTS/(stem+".json")
    if not p.exists(): errors.append(f"missing manifest: {p}"); continue
    try: m=json.loads(p.read_text())
    except Exception as e: errors.append(f"invalid JSON {p}: {e}"); continue
    if m.get("test_vector_id") != tv: errors.append(f"{p}: test_vector_id mismatch")
    for k in ("provenance_required","security","promotion_state","licence_boundary"):
        if k not in m: errors.append(f"{p}: missing {k}")
    if m.get("security",{}).get("os_authority") is not False: errors.append(f"{p}: OS authority must be false")
    if not (FIXTURES/fixture).exists(): errors.append(f"missing fixture: {fixture}")
for p in FIXTURES.glob("*.json"):
    try: json.loads(p.read_text())
    except Exception as e: errors.append(f"invalid JSON {p}: {e}")
obj=(FIXTURES/"assimp-tv-001.obj").read_text().splitlines()
if sum(x.startswith("v ") for x in obj)!=3: errors.append("Assimp fixture must have 3 vertices")
if sum(x.startswith("f ") for x in obj)!=1: errors.append("Assimp fixture must have 1 face")
s=json.loads((FIXTURES/"sundials-tv-001.json").read_text())
expected=math.exp(-s["k"]*s["t"])
if abs(expected-s["expected"]["y"])>s["tolerance"]: errors.append("SUNDIALS analytic reference mismatch")
if errors:
    print("FAIL")
    print("\n".join(errors))
    sys.exit(1)
print("PASS")
print("Validated manifests: 5")
print("Validated JSON fixtures: 4")
print("Validated OBJ fixture: 1")
print("Validated SUNDIALS analytic reference")
print("Third-party runtime execution: NOT PERFORMED")
