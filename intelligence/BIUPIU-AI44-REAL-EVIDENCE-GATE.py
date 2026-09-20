"""AI-44 real-evidence authentication gate.

AI-44 authenticates execution evidence only. It does not grant release or
promotion status; downstream governance gates decide regression/promotion.
"""
from __future__ import annotations
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=[f"F{i:02d}" for i in range(1,10)]
def evaluate(bundle):
    if bundle.get("source")!="BIUPIU-AI39-FEDERATED-RUNNER":
        return {"status":"BLOCKED_UNTRUSTED_EVIDENCE","promotion":False}
    if bundle.get("execution_attestation") is not True:
        return {"status":"PENDING_RUNTIME","promotion":False,"reason":"missing execution attestation"}
    results=bundle.get("results",{})
    missing=[k for k in REQUIRED if k not in results]
    failed=[k for k in REQUIRED if results.get(k) is not True]
    if missing or failed:
        return {"status":"REMEDIATION_REQUIRED","promotion":False,
                "missing":missing,"failed":failed}
    return {"status":"EXECUTED","promotion":False,"evidence_authenticated":True}
if __name__=="__main__":
    p=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/"intelligence/BIUPIU-AI40-EXECUTION-RESULT-BUNDLE.json"
    print(json.dumps(evaluate(json.loads(p.read_text())),sort_keys=True))
