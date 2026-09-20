"""BIUPIU Governance Kernel — AI-56.

Loads canonical governance authorities and performs fail-closed consistency checks.
No provider invocation, secret handling, physical actuation, or automatic promotion.
"""
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
AUTHORITIES={
 "evidence":"intelligence/BIUPIU-AI44-REAL-EVIDENCE-GATE.py",
 "release":"intelligence/BIUPIU-AI49-CANONICAL-TASK-RELEASE-CONTROLLER.py",
 "states":"intelligence/BIUPIU-AI53-GATE-STATE-MACHINE.py",
 "index":"intelligence/BIUPIU-AI46-UNIFIED-REGRESSION-INDEX-CONTROLLER.py",
 "routing":"intelligence/BIUPIU-AI47-GOVERNED-TASK-ROUTER.py",
 "readiness":"intelligence/BIUPIU-AI48-TASK-TO-RELEASE-CONTROLLER.py",
}
REQUIRED=("evidence","release","states","index","routing","readiness")
def sha(v): return hashlib.sha256(json.dumps(v,sort_keys=True).encode()).hexdigest()
def inspect():
 findings=[]
 loaded={}
 for name,path in AUTHORITIES.items():
  f=ROOT/path
  if not f.exists(): findings.append(("MISSING_AUTHORITY",name,str(path))); continue
  loaded[name]=sha(f.read_text(encoding="utf-8"))
 if tuple(loaded)!=REQUIRED: findings.append(("AUTHORITY_SET_INCOMPLETE",sorted(set(REQUIRED)-set(loaded))))
 try:
  sm=loaded and __import__("importlib.util").util.spec_from_file_location("bpu_sm",ROOT/AUTHORITIES["states"])
  mod=__import__("importlib.util").util.module_from_spec(sm); sm.loader.exec_module(mod)
  if "PROMOTED" not in mod.STATES or mod.TRANSITIONS.get("PROMOTED")!=set():
   findings.append(("STATE_MACHINE_CONFLICT","PROMOTED must be terminal"))
 except Exception as e: findings.append(("LOAD_ERROR","states",type(e).__name__))
 return {"status":"CLEAN" if not findings else "BLOCKED","findings":findings,
         "authority_hashes":loaded,"kernel_hash":sha(loaded)}
def gate(task,evidence):
 check=inspect()
 if check["status"]!="CLEAN": return {"state":"BLOCKED_CONTROL_CONTRACT","kernel":check}
 return {"state":"DELEGATED_TO_CANONICAL_RELEASE_GATE","kernel":check,"task_id":task.get("task_id")}
if __name__=="__main__": print(json.dumps(inspect(),sort_keys=True,indent=2))
