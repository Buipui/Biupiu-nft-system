"""AI-70 authority-resolution classifier.
No destructive changes; unresolved candidates remain REVIEW.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; I=ROOT/"intelligence"
CANON={"evidence":"BIUPIU-AI44-REAL-EVIDENCE-GATE.py","routing":"BIUPIU-AI47-GOVERNED-TASK-ROUTER.py","readiness":"BIUPIU-AI48-TASK-TO-RELEASE-CONTROLLER.py","release":"BIUPIU-AI49-CANONICAL-TASK-RELEASE-CONTROLLER.py","regression_index":"BIUPIU-AI46-UNIFIED-REGRESSION-INDEX-CONTROLLER.py","state_machine":"BIUPIU-AI53-GATE-STATE-MACHINE.py","governance_kernel":"BIUPIU-GOVERNANCE-KERNEL-AI56.py"}
def classify():
 out=[]
 for role,fn in CANON.items():
  out.append({"role":role,"authority":fn,"classification":"CANONICAL" if (I/fn).exists() else "REVIEW"})
 return out
def run():
 c=classify()
 unresolved=[x for x in c if x["classification"]!="CANONICAL"]
 return {"gate":"AI-70","classifications":c,"unresolved":unresolved,
         "promotion_allowed":not unresolved and False,
         "reason":"runtime evidence and final human-controlled promotion remain required"}
if __name__=="__main__": print(json.dumps(run(),indent=2,sort_keys=True))
