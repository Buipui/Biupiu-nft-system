#!/usr/bin/env python3
import json, math, pathlib, sys
root=pathlib.Path(__file__).resolve().parents[1]
if not (root/"adapters").is_dir():
    print("FAIL: repository root/adapters not found")
    sys.exit(2)
m=root/"adapters/manifests"; f=root/"adapters/fixtures"; errors=[]
pairs=[("sundials","SUNDIALS-TV-001","sundials-tv-001.json"),("open3d","OPEN3D-TV-001","open3d-tv-001.json"),("assimp","ASSIMP-TV-001","assimp-tv-001.obj"),("gazebo","GAZEBO-TV-001","gazebo-tv-001.json"),("chrono","CHRONO-TV-001","chrono-tv-001.json")]
for stem,tv,fx in pairs:
 p=m/(stem+".json")
 if not p.exists(): errors.append("missing manifest "+str(p)); continue
 try: x=json.loads(p.read_text())
 except Exception as e: errors.append("invalid manifest "+stem+": "+str(e)); continue
 if x.get("test_vector_id")!=tv: errors.append("test vector mismatch "+stem)
 if x.get("security",{}).get("os_authority") is not False: errors.append("OS authority not false "+stem)
 if not (f/fx).exists(): errors.append("missing fixture "+fx)
for p in f.glob("*.json"):
 try: json.loads(p.read_text())
 except Exception as e: errors.append("invalid fixture "+str(p)+": "+str(e))
obj=(f/"assimp-tv-001.obj").read_text().splitlines()
if sum(x.startswith("v ") for x in obj)!=3: errors.append("Assimp vertex count")
if sum(x.startswith("f ") for x in obj)!=1: errors.append("Assimp face count")
s=json.loads((f/"sundials-tv-001.json").read_text())
if abs(math.exp(-s["k"]*s["t"])-s["expected"]["y"])>s["tolerance"]: errors.append("SUNDIALS reference")
if errors:
 print("FAIL"); print("\n".join(errors)); sys.exit(1)
print("OFFLINE VALIDATION PASS")
print("5 manifests; 5 fixtures; deterministic reference checks complete")
print("This does not validate third-party runtime execution.")
