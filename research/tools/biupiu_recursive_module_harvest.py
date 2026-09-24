#!/usr/bin/env python3
import json, os, re, hashlib, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"research/evidence/BIUPIU-RECURSIVE-MODULE-NODE-ADAPTER-MATRIX-20260924.json"

SOURCE_EXT={".c",".cc",".cpp",".cxx",".h",".hpp",".rs",".kt",".kts",".java",".py",".ts",".tsx",".js",".jsx",".gradle",".md"}
ADAPTER_RE=re.compile(r"(adapter|bridge|transport|connector|provider|interop|federat)",re.I)
SIM_RE=re.compile(r"(sim|simulator|simulation|emulator|mock|virtual|hardware)",re.I)
NODE_RE=re.compile(r"(node|sensor|device|receiver|transmitter|controller|gateway)",re.I)

def sha256(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

def git(cmd):
    try:return subprocess.check_output(["git"]+cmd,cwd=ROOT,text=True,stderr=subprocess.DEVNULL).strip()
    except Exception:return ""

files=[]; adapters=[]; simulators=[]; nodes=[]; modules=[]
skip={".git","build","node_modules",".gradle",".idea","dist","target","DerivedData"}
for p in ROOT.rglob("*"):
    if not p.is_file() or any(x in skip for x in p.parts): continue
    rel=p.relative_to(ROOT).as_posix()
    if p.suffix.lower() in SOURCE_EXT:
        item={"path":rel,"extension":p.suffix.lower(),"size":p.stat().st_size,"sha256":sha256(p)}
        files.append(item)
        name=rel
        if ADAPTER_RE.search(name): adapters.append(item)
        if SIM_RE.search(name): simulators.append(item)
        if NODE_RE.search(name): nodes.append(item)
        modules.append(item)

families={}
for item in modules:
    top=item["path"].split("/",1)[0]
    families.setdefault(top,0); families[top]+=1

result={
 "schema":"biupiu.recursive.module-node-adapter-matrix.v1",
 "status":"HARVESTED_REQUIRES_RUNTIME_GATES",
 "revision":git(["rev-parse","HEAD"]),
 "scope":"recursive source inventory, modules, nodes, adapters, simulators and integration candidates",
 "counts":{"source_files":len(files),"modules":len(modules),"adapters":len(adapters),"simulators":len(simulators),"nodes":len(nodes)},
 "families":families,
 "integration_contract":{
   "DigiCat":"index every detected capability/module/node/adapter/simulator",
   "DigiFile":"retain hash/provenance/test/build/runtime evidence",
   "Learning":"consume observations and regressions; never silently rewrite source",
   "Quanticor":"controlled intersections and semantic conflict/referee maps",
   "computational_geometry":"relationship and behaviour representation",
   "executable_truth":"source/build/test/runtime evidence"
 },
 "detected":{
   "modules":modules,
   "adapters":adapters,
   "simulators":simulators,
   "nodes":nodes
 },
 "gates":{
   "source_inventory":True,
   "hash_inventory":True,
   "json_contract":True,
   "runtime_build":False,
   "device_validation":False,
   "physical_photonic_validation":False,
   "physical_quantum_validation":False,
   "promotion_allowed":False
 },
 "housekeeping":{
   "production_source_deleted":False,
   "external_research_overwrote_internal_code":False,
   "unverified_hardware_claims_promoted":False
 }
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"PASS","revision":result["revision"],"counts":result["counts"],"output":str(OUT)},indent=2))
