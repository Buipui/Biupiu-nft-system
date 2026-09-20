"""AI-50 canonical control-chain negative/self-test.

Tests only deterministic control logic; no network, provider, hardware, or actuation.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

ev=load("ai44","intelligence/BIUPIU-AI44-REAL-EVIDENCE-GATE.py")
rel=load("ai48","intelligence/BIUPIU-AI48-TASK-TO-RELEASE-CONTROLLER.py")
canon=load("ai49","intelligence/BIUPIU-AI49-CANONICAL-TASK-RELEASE-CONTROLLER.py")

def run():
    results={}
    trusted={ "source":"BIUPIU-AI39-FEDERATED-RUNNER",
              "execution_attestation":True,
              "results":{k:True for k in ["F01","F02","F03","F04","F05","F06","F07","F08","F09"]}}
    synthetic=dict(trusted); synthetic["source"]="manual"
    incomplete=dict(trusted); incomplete["results"]={"F01":True}
    failed=dict(trusted); failed["results"]=dict(trusted["results"]); failed["results"]["F05"]=False

    results["N01"]=ev.evaluate(synthetic)["status"]=="REJECTED_SYNTHETIC_OR_UNTRUSTED"
    results["N02"]=ev.evaluate(incomplete)["status"]=="EXECUTED_FAIL"
    results["N03"]=ev.evaluate(failed)["status"]=="REMEDIATION_REQUIRED"
    results["N04"]=rel.release_state({"provenance_required":True,"regression_required":True},synthetic)=="BLOCKED_UNTRUSTED_EVIDENCE"
    results["N05"]=rel.release_state({"provenance_required":True,"regression_required":True},incomplete)=="REMEDIATION_REQUIRED"
    packet={"task_id":"BPU-AI50","objective":"negative self-test","routes":["OS"],"provenance_required":True,"regression_required":True}
    record=canon.canonical_record(packet,trusted,"PROMOTION_READY")
    results["N06"]=canon.validate(record)=="PROMOTION_READY"
    record["required_controls"]["regression"]=False
    results["N07"]=canon.validate(record)=="BLOCKED_CONTROL_CONTRACT"
    return results

if __name__=="__main__":
    r=run(); print(r); raise SystemExit(0 if all(r.values()) else 1)
