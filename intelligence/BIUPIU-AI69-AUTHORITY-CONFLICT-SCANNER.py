"""AI-69 authority/conflict/orphan scanner.
Static repository scan only; never treats naming similarity as proof of authority.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; I=ROOT/"intelligence"
CANON={"evidence":"BIUPIU-AI44-REAL-EVIDENCE-GATE.py","routing":"BIUPIU-AI47-GOVERNED-TASK-ROUTER.py","readiness":"BIUPIU-AI48-TASK-TO-RELEASE-CONTROLLER.py","release":"BIUPIU-AI49-CANONICAL-TASK-RELEASE-CONTROLLER.py","regression_index":"BIUPIU-AI46-UNIFIED-REGRESSION-INDEX-CONTROLLER.py","state_machine":"BIUPIU-AI53-GATE-STATE-MACHINE.py","governance_kernel":"BIUPIU-GOVERNANCE-KERNEL-AI56.py"}
def run():
 files={p.name for p in I.glob("*.py")}
 missing={k:v for k,v in CANON.items() if v not in files}
 governance=[p.name for p in I.glob("*GOVERNANCE*.py")]
 release=[p.name for p in I.glob("*RELEASE*.py")]
 state=[p.name for p in I.glob("*STATE*.py")]
 duplicate_candidates={"governance":governance,"release":release,"state":state}
 return {"gate":"AI-69","canonical_missing":missing,"duplicate_candidates":duplicate_candidates,
         "status":"BLOCKED" if missing else "CLEAN",
         "orphan_detection":"candidate-list-only",
         "promotion_allowed":False}
if __name__=="__main__": print(json.dumps(run(),indent=2,sort_keys=True))
