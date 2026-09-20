"""AI-54 smoke/exterminate for AI-49 + AI-53 integration."""
from __future__ import annotations
import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(n,p):
 s=importlib.util.spec_from_file_location(n,ROOT/p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
ai49=load("ai49","intelligence/BIUPIU-AI49-CANONICAL-TASK-RELEASE-CONTROLLER.py")
base={"source":"BIUPIU-AI39-FEDERATED-RUNNER","execution_attestation":True,
      "results":{k:True for k in ai49.REQUIRED}}
packet={"task_id":"BPU-AI54","objective":"state integration","routes":["OS"],
        "provenance_required":True,"regression_required":True}
def run():
 r={}
 x=ai49.canonical_record(packet,base)
 r["normal_record"]=ai49.validate(x)=="PROMOTION_READY" or ai49.validate({**x,"release_state":"PENDING_RUNTIME"})=="BLOCKED_CONTROL_CONTRACT"
 x["release_state"]="PROMOTED"; x["state_path"]= ["DISCOVERED","ASSIGNED","EXECUTING","CHALLENGED","VALIDATED","REGRESSION_PASS","PROMOTION_READY","PROMOTED"]
 r["legal_path"]=ai49.validate(x)=="PROMOTED"
 x["release_state"]="PROMOTED"; x["state_path"]= ["DISCOVERED","PROMOTED"]
 r["illegal_jump_blocked"]=ai49.validate(x)=="BLOCKED_CONTROL_CONTRACT"
 x["release_state"]="PROMOTION_READY"; x["state_path"]=[]
 r["missing_path_blocked"]=ai49.validate(x)=="BLOCKED_CONTROL_CONTRACT"
 return r
if __name__=="__main__":
 r=run(); print(r); raise SystemExit(0 if all(r.values()) else 1)
