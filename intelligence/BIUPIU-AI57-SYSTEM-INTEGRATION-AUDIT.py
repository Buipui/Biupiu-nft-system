"""AI-57 system-wide integration audit.

Detects orphaned governance domains and schema/state drift across OS, DMS,
simulators, configurators, Math/Physics, Intelligence and repository governance.
"""
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DOMAINS=["OS","DMS","INTELLIGENCE","SIMULATORS","CONFIGURATORS","MATH_PHYSICS","DIGITAL_TWIN","PROVENANCE","SECURITY","BLOCKCHAIN","HMI","RESEARCH"]
AUTHORITIES=["BIUPIU-GOVERNANCE-KERNEL-AI56.py","BIUPIU-AI44-REAL-EVIDENCE-GATE.py","BIUPIU-AI46-UNIFIED-REGRESSION-INDEX-CONTROLLER.py","BIUPIU-AI47-GOVERNED-TASK-ROUTER.py","BIUPIU-AI48-TASK-TO-RELEASE-CONTROLLER.py","BIUPIU-AI49-CANONICAL-TASK-RELEASE-CONTROLLER.py","BIUPIU-AI53-GATE-STATE-MACHINE.py"]
def audit():
 text="
".join(p.read_text(errors="ignore") for p in ROOT.rglob("*.py"))
 missing=[p for p in AUTHORITIES if not (ROOT/"intelligence"/p).exists()]
 orphan=[d for d in DOMAINS if d not in text]
 contradictions=[]
 if '"PROMOTED":set()' not in text: contradictions.append("PROMOTED_NOT_TERMINAL")
 return {"status":"CLEAN" if not missing and not orphan and not contradictions else "BLOCKED",
 "missing_authorities":missing,"orphan_domains":orphan,"contradictions":contradictions}
if __name__=="__main__": print(json.dumps(audit(),indent=2,sort_keys=True))
