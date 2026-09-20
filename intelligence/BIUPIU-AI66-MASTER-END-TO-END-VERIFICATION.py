"""AI-66 master end-to-end verification harness."""
from __future__ import annotations
import json,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; I=ROOT/"intelligence"
def load(file,name):
 s=importlib.util.spec_from_file_location(name,I/file); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def run():
 k=load("BIUPIU-GOVERNANCE-KERNEL-AI56.py","k")
 e=load("BIUPIU-AI44-REAL-EVIDENCE-GATE.py","e")
 st=load("BIUPIU-AI53-GATE-STATE-MACHINE.py","st")
 cases={}
 cases["baseline_kernel"]=k.inspect()["status"] in ("CLEAN","BLOCKED")
 cases["invalid_state_blocks"]=not st.validate_path(["DISCOVERED","PROMOTED"])
 cases["missing_attestation_blocks"]=e.evaluate({"source":"BIUPIU-AI39-FEDERATED-RUNNER","execution_attestation":False})["status"]=="PENDING_RUNTIME"
 cases["untrusted_evidence_blocks"]=e.evaluate({"source":"UNTRUSTED","execution_attestation":True})["status"]=="BLOCKED_UNTRUSTED_EVIDENCE"
 # Controlled corruption: temporarily point the kernel at a nonexistent gate.
 old=k.REGRESSION; k.REGRESSION="AI66-NONEXISTENT-REGRESSION.py"
 cases["missing_gate_blocks"]=k.inspect()["status"]=="BLOCKED"
 k.REGRESSION=old
 return cases
if __name__=="__main__":
 r=run(); print(json.dumps(r,indent=2,sort_keys=True)); raise SystemExit(0 if all(r.values()) else 1)
