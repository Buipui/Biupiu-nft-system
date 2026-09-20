"""AI-64 full contract-to-governance regression gate."""
from __future__ import annotations
import json,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; I=ROOT/"intelligence"; A=I/"adapters"
def load(path,name):
 s=importlib.util.spec_from_file_location(name,I/path); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def run():
 reg=json.loads((I/"BIUPIU-AI60-INTERFACE-REGISTRY.json").read_text())
 man=json.loads((I/"BIUPIU-AI58-SYSTEM-INTEGRATION-MANIFEST.json").read_text())
 v=load("BIUPIU-AI60-INTERFACE-REGISTRY-VALIDATOR.py","r")
 e=load("BIUPIU-AI44-REAL-EVIDENCE-GATE.py","e")
 st=load("BIUPIU-AI53-GATE-STATE-MACHINE.py","s")
 checks={}
 checks["registry_clean"]=v.validate()["status"]=="CLEAN"
 checks["manifest_registry_match"]=set(reg["interfaces"])=={x for d in man["domains"].values() for x in d["interfaces"]}
 checks["valid_path"]=st.validate_path(["DISCOVERED","ASSIGNED","EXECUTING","CHALLENGED","VALIDATED","REGRESSION_PASS","PROMOTION_READY"])
 checks["invalid_jump_blocked"]=not st.validate_path(["DISCOVERED","PROMOTED"])
 checks["missing_evidence_blocks"]=e.evaluate({"source":"BIUPIU-AI39-FEDERATED-RUNNER","execution_attestation":False})["status"]=="PENDING_RUNTIME"
 checks["untrusted_evidence_blocks"]=e.evaluate({"source":"UNTRUSTED","execution_attestation":True})["status"]=="BLOCKED_UNTRUSTED_EVIDENCE"
 return checks
if __name__=="__main__":
 r=run(); print(json.dumps(r,sort_keys=True)); raise SystemExit(0 if all(r.values()) else 1)
