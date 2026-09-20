"""BIUPIU Governance Kernel — AI-65 hardened master gate."""
from __future__ import annotations
import hashlib,json,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; INT=ROOT/"intelligence"
AUTHORITIES={"evidence":"BIUPIU-AI44-REAL-EVIDENCE-GATE.py","release":"BIUPIU-AI49-CANONICAL-TASK-RELEASE-CONTROLLER.py","states":"BIUPIU-AI53-GATE-STATE-MACHINE.py","index":"BIUPIU-AI46-UNIFIED-REGRESSION-INDEX-CONTROLLER.py","routing":"BIUPIU-AI47-GOVERNED-TASK-ROUTER.py","readiness":"BIUPIU-AI48-TASK-TO-RELEASE-CONTROLLER.py"}
REGISTRY="BIUPIU-AI60-INTERFACE-REGISTRY.json"; MANIFEST="BIUPIU-AI58-SYSTEM-INTEGRATION-MANIFEST.json"; REGRESSION="BIUPIU-AI64-FULL-CONTRACT-GOVERNANCE-REGRESSION-TEST.py"
def sha(v): return hashlib.sha256(json.dumps(v,sort_keys=True).encode()).hexdigest()
def inspect():
 findings=[]; loaded={}
 for n,p in AUTHORITIES.items():
  f=INT/p
  if not f.is_file(): findings.append(("MISSING_AUTHORITY",n,p))
  else: loaded[n]=hashlib.sha256(f.read_bytes()).hexdigest()
 for p in (REGISTRY,MANIFEST,REGRESSION):
  if not (INT/p).is_file(): findings.append(("MISSING_GATE_ARTIFACT",p))
 sm=INT/AUTHORITIES["states"]
 try:
  s=importlib.util.spec_from_file_location("sm",sm); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
  if "PROMOTED" not in m.STATES or m.TRANSITIONS.get("PROMOTED")!=set(): findings.append(("STATE_CONFLICT","PROMOTED_NOT_TERMINAL"))
 except Exception as e: findings.append(("STATE_LOAD_ERROR",type(e).__name__))
 return {"status":"CLEAN" if not findings else "BLOCKED","findings":findings,"authority_hashes":loaded,"kernel_hash":sha(loaded)}
def gate(task,evidence=None):
 c=inspect()
 if c["status"]!="CLEAN": return {"state":"BLOCKED_CONTROL_CONTRACT","kernel":c,"task_id":task.get("task_id")}
 return {"state":"DELEGATED_TO_AI64_REGRESSION_AND_CANONICAL_RELEASE","kernel":c,"task_id":task.get("task_id")}
if __name__=="__main__": print(json.dumps(inspect(),indent=2,sort_keys=True))
