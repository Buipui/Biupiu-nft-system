"""AI-57 system-wide integration audit — hardened for AI-58."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; INT=ROOT/"intelligence"
DOMAINS=("OS","DMS","INTELLIGENCE","SIMULATORS","CONFIGURATORS","MATH_PHYSICS","DIGITAL_TWIN","PROVENANCE","SECURITY","BLOCKCHAIN","HMI","RESEARCH")
AUTHORITIES={"evidence":"BIUPIU-AI44-REAL-EVIDENCE-GATE.py","release":"BIUPIU-AI49-CANONICAL-TASK-RELEASE-CONTROLLER.py","states":"BIUPIU-AI53-GATE-STATE-MACHINE.py","index":"BIUPIU-AI46-UNIFIED-REGRESSION-INDEX-CONTROLLER.py","routing":"BIUPIU-AI47-GOVERNED-TASK-ROUTER.py","readiness":"BIUPIU-AI48-TASK-TO-RELEASE-CONTROLLER.py","kernel":"BIUPIU-GOVERNANCE-KERNEL-AI56.py"}
def audit():
 missing=[(k,p) for k,p in AUTHORITIES.items() if not (INT/p).is_file()]
 manifest=INT/"BIUPIU-AI58-SYSTEM-INTEGRATION-MANIFEST.json"; manifest_ok=manifest.is_file(); data={}
 if manifest_ok:
  try: data=json.loads(manifest.read_text(encoding="utf-8"))
  except Exception: manifest_ok=False
 listed=set(data.get("domains",{})); orphan=[d for d in DOMAINS if d not in listed] if data else list(DOMAINS)
 contradictions=[]
 sm=INT/AUTHORITIES["states"]
 if sm.is_file() and '"PROMOTED":set()' not in sm.read_text(encoding="utf-8"): contradictions.append("PROMOTED_NOT_TERMINAL")
 return {"status":"CLEAN" if not missing and manifest_ok and not orphan and not contradictions else "BLOCKED","missing_authorities":missing,"manifest_present":manifest_ok,"orphan_domains":orphan,"contradictions":contradictions}
if __name__=="__main__": print(json.dumps(audit(),indent=2,sort_keys=True))
