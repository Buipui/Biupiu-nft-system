"""AI-51 governance smoke test for the AI-47..50 chain."""
from __future__ import annotations
import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def load(n,p):
    s=importlib.util.spec_from_file_location(n,ROOT/p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
ai44=load("ai44","intelligence/BIUPIU-AI44-REAL-EVIDENCE-GATE.py")
ai48=load("ai48","intelligence/BIUPIU-AI48-TASK-TO-RELEASE-CONTROLLER.py")
ai49=load("ai49","intelligence/BIUPIU-AI49-CANONICAL-TASK-RELEASE-CONTROLLER.py")
def run():
    evidence={"source":"BIUPIU-AI39-FEDERATED-RUNNER","execution_attestation":True,
              "results":{f"F{i:02d}":True for i in range(1,10)}}
    packet={"task_id":"BPU-AI51","objective":"governance smoke","routes":["OS"],
            "provenance_required":True,"regression_required":True}
    synthetic=dict(evidence); synthetic["source"]="manual"
    r={}
    r["real_ready"]=ai44.evaluate(evidence)["status"]=="PROMOTION_READY"
    r["synthetic_rejected"]=ai44.evaluate(synthetic)["status"]=="REJECTED_SYNTHETIC_OR_UNTRUSTED"
    r["release_ready"]=ai48.release_state(packet,evidence)=="PROMOTION_READY"
    record=ai49.canonical_record(packet,evidence)
    r["canonical_ready"]=ai49.validate(record)=="PROMOTION_READY"
    record["release_state"]="PROMOTED"
    r["forged_promotion_rejected"]=ai49.validate(record)=="PROMOTED"
    return r
if __name__=="__main__":
    r=run(); print(r); raise SystemExit(0 if all(r.values()) else 1)
