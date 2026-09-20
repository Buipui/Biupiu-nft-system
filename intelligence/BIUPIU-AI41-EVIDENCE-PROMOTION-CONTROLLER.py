"""AI-41 evidence promotion controller. Deterministic, read-only, no actuation."""

from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REQUIRED=["F01","F02","F03","F04","F05","F06","F07","F08","F09"]

def evaluate(bundle: dict) -> dict:
    checks=bundle.get("checks", bundle.get("results", {}))
    if not checks:
        return {"status":"PENDING_RUNTIME","promotion":False,"reason":"no executable result bundle"}
    missing=[k for k in REQUIRED if k not in checks]
    if missing:
        return {"status":"EXECUTED_FAIL","promotion":False,"reason":"missing checks","missing":missing}
    failed=[k for k in REQUIRED if checks[k] is not True]
    if failed:
        return {"status":"REMEDIATION_REQUIRED","promotion":False,"reason":"required checks failed","failed":failed}
    return {"status":"PROMOTION_READY","promotion":True,"reason":"all required executable checks passed","blocked":["F10"]}

if __name__=="__main__":
    import sys
    p=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/"intelligence/BIUPIU-AI40-EXECUTION-RESULT-BUNDLE.json"
    bundle=json.loads(p.read_text())
    print(json.dumps(evaluate(bundle),sort_keys=True))
