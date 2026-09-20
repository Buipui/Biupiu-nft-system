"""AI-44 real-evidence gate.

The pipeline accepts only a result bundle produced by the federated runner and
requires an execution_attestation. Synthetic/hand-authored check maps are rejected.
"""
from __future__ import annotations
import json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REQUIRED=["F01","F02","F03","F04","F05","F06","F07","F08","F09"]

def evaluate(bundle):
    if bundle.get("source")!="BIUPIU-AI39-FEDERATED-RUNNER":
        return {"status":"REJECTED_SYNTHETIC_OR_UNTRUSTED","promotion":False}
    if bundle.get("execution_attestation") is not True:
        return {"status":"PENDING_RUNTIME","promotion":False,"reason":"missing execution attestation"}
    results=bundle.get("results",{})
    missing=[k for k in REQUIRED if k not in results]
    failed=[k for k in REQUIRED if results.get(k) is not True]
    if missing:
        return {"status":"EXECUTED_FAIL","promotion":False,"missing":missing}
    if failed:
        return {"status":"REMEDIATION_REQUIRED","promotion":False,"failed":failed}
    return {"status":"PROMOTION_READY","promotion":True,"blocked":["F10"]}

if __name__=="__main__":
    p=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/"intelligence/BIUPIU-AI40-EXECUTION-RESULT-BUNDLE.json"
    print(json.dumps(evaluate(json.loads(p.read_text())),sort_keys=True))
