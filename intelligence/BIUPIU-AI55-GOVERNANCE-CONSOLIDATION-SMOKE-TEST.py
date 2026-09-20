"""AI-55 governance-stack smoke/exterminate test."""
from __future__ import annotations
import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(n,p):
 s=importlib.util.spec_from_file_location(n,ROOT/p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
ai44=load("ai44","intelligence/BIUPIU-AI44-REAL-EVIDENCE-GATE.py")
ai48=load("ai48","intelligence/BIUPIU-AI48-TASK-TO-RELEASE-CONTROLLER.py")
ai49=load("ai49","intelligence/BIUPIU-AI49-CANONICAL-TASK-RELEASE-CONTROLLER.py")
def run():
 ev={"source":"BIUPIU-AI39-FEDERATED-RUNNER","execution_attestation":True,
     "results":{f"F{i:02d}":True for i in range(1,10)},"challenge_pass":True,
     "validation_pass":True,"regression_pass":True}
 pkt={"task_id":"BPU-AI55","objective":"governance smoke","routes":["OS"],
      "provenance_required":True,"regression_required":True}
 r={}
 r["ai44_auth_only"]=ai44.evaluate(ev)["status"]=="EXECUTED"
 r["ai48_release_requires_checks"]=ai48.release_state(pkt,ev)=="PROMOTION_READY"
 r["ai48_blocks_missing_regression"]=ai48.release_state(pkt,{**ev,"regression_pass":False})=="REMEDIATION_REQUIRED"
 rec=ai49.canonical_record(pkt,ev)
 r["ai49_blocks_missing_path"]=ai49.validate(rec)=="BLOCKED_CONTROL_CONTRACT"
 r["ai49_legal_path"]=ai49.validate({**rec,"state_path":["DISCOVERED","ASSIGNED","EXECUTING","CHALLENGED","VALIDATED","REGRESSION_PASS","PROMOTION_READY"]})=="PROMOTION_READY"
 r["ai49_blocks_forged_jump"]=ai49.validate({**rec,"release_state":"PROMOTED","state_path":["DISCOVERED","PROMOTED"]})=="BLOCKED_CONTROL_CONTRACT"
 return r
if __name__=="__main__":
 r=run(); print(r); raise SystemExit(0 if all(r.values()) else 1)
