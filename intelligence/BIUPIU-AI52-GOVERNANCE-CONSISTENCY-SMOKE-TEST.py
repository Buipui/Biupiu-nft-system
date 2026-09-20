"""AI-52 governance consistency/fuzz smoke test.

Validates fail-closed invariants without requiring a runtime or external provider.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(n,p):
    s=importlib.util.spec_from_file_location(n,ROOT/p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
ai44=load("ai44","intelligence/BIUPIU-AI44-REAL-EVIDENCE-GATE.py")
ai49=load("ai49","intelligence/BIUPIU-AI49-CANONICAL-TASK-RELEASE-CONTROLLER.py")
REQ=ai49.REQUIRED
def run():
    base={"source":"BIUPIU-AI39-FEDERATED-RUNNER","execution_attestation":True,
          "results":{k:True for k in REQ}}
    packet={"task_id":"BPU-AI52","objective":"governance consistency","routes":["OS","DMS"],
            "provenance_required":True,"regression_required":True}
    checks={}
    checks["complete"]=ai49.evidence_state(base)=="PROMOTION_READY"
    for key in REQ:
        x={**base,"results":dict(base["results"])}; x["results"][key]=False
        checks[f"fail_{key}"]=ai49.evidence_state(x)=="REMEDIATION_REQUIRED"
    missing={**base,"results":dict(base["results"])}; missing["results"].pop(REQ[0])
    checks["missing"]=ai49.evidence_state(missing)=="REMEDIATION_REQUIRED"
    untrusted={**base,"source":"manual"}
    checks["untrusted"]=ai44.evaluate(untrusted)["status"]=="REJECTED_SYNTHETIC_OR_UNTRUSTED"
    no_att={**base,"execution_attestation":False}
    checks["no_attestation"]=ai44.evaluate(no_att)["status"]=="PENDING_RUNTIME"
    record=ai49.canonical_record(packet,base)
    checks["canonical"]=ai49.validate(record)=="PROMOTION_READY"
    return checks
if __name__=="__main__":
    r=run(); print(r); raise SystemExit(0 if all(r.values()) else 1)
