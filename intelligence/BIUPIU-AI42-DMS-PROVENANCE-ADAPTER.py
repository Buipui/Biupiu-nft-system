"""AI-42 Biupiu Intelligence/DMS provenance and failure-learning adapter."""
from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SCHEMA=ROOT/"intelligence/schemas/BIUPIU-AI42-EVIDENCE-DMS-PROVENANCE-v1.json"

def sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True).encode()).hexdigest()

def make_event(task_id, gate, bundle, promotion):
    checks=bundle.get("checks",bundle.get("results",{}))
    failed=[k for k,v in checks.items() if k.startswith("F") and v is False]
    failure_class="runtime_unavailable" if promotion["status"]=="PENDING_RUNTIME" else ("model_contract" if failed else "none")
    return {
      "event_id":f"bpu-{gate.lower()}-{sha(bundle)[:12]}",
      "timestamp":datetime.now(timezone.utc).isoformat(),
      "task_id":task_id,"gate":gate,
      "input_hash":sha(bundle),
      "result_hash":sha(promotion),
      "state_class":"simulated",
      "checks":checks,
      "promotion_state":promotion["status"],
      "failure_class":failure_class,
      "remediation":None if not failed else {"required":True,"reproduce_before_close":True},
      "regression":{"required":True,"confirmed":False},
      "source":"Biupiu controlled validation pipeline"
    }

def write_event(path,bundle,promotion):
    event=make_event("BPU-AI42-FEDERATED", "AI-42", bundle, promotion)
    Path(path).write_text(json.dumps(event,indent=2,sort_keys=True),encoding="utf-8")
    return event
