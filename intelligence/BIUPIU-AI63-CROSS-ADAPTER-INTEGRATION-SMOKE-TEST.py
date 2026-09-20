"""AI-63 cross-adapter integration gate.

Exercises the canonical adapter chain with positive and negative evidence.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; A=ROOT/"intelligence/adapters"
def load(name):
 p=A/name; s=importlib.util.spec_from_file_location(name,p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def run():
 evidence=load("BIUPIU-EVIDENCE-INTERFACE-v1.py")
 state=load("BIUPIU-STATE-INTERFACE-v1.py")
 release=load("BIUPIU-RELEASE-INTERFACE-v1.py")
 validation=load("BIUPIU-VALIDATION-INTERFACE-v1.py")
 regression=load("BIUPIU-REGRESSION-INTERFACE-v1.py")
 good={"source":"BIUPIU-AI39-FEDERATED-RUNNER","execution_attestation":True,
       "results":{f"F{i:02d}":True for i in range(1,10)}}
 bad={**good,"execution_attestation":False}
 packet={"task_id":"BPU-AI63","objective":"cross-adapter integration","routes":["INTELLIGENCE"],
         "provenance_required":True}
 ev=evidence.handle(good); blocked=evidence.handle(bad)
 rec=release.handle(packet,good)
 v=validation.handle(rec)
 idx=regression.handle([{"domain":"INTELLIGENCE","state":"REGRESSION_PASS"}])
 return {
  "evidence_positive":ev.get("evidence_authenticated") is True,
  "evidence_negative_blocks":blocked.get("status")=="PENDING_RUNTIME",
  "release_record_created":rec.get("schema","").startswith("BIUPIU-AI49"),
  "validation_returns":isinstance(v,dict) and "validation_pass" in v,
  "regression_adapter_returns":isinstance(idx,dict) and "index" in idx,
  "no_observed_from_simulation":rec.get("state_authority",{}).get("simulated_never_observed_by_inference") is True
 }
if __name__=="__main__":
 r=run(); print(r); raise SystemExit(0 if all(r.values()) else 1)
