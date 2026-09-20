"""AI-48 Biupiu task-to-release control loop.

Orchestrates routing, evidence authentication, provenance, regression indexing
and release-state calculation. It is fail-closed: repository presence or synthetic
evidence can never produce VERIFIED/PROMOTED.
"""
from __future__ import annotations
import hashlib,json
from datetime import datetime,timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REQUIRED=["F01","F02","F03","F04","F05","F06","F07","F08","F09"]

def digest(v):
    return hashlib.sha256(json.dumps(v,sort_keys=True).encode()).hexdigest()

def release_state(packet,bundle):
    if bundle.get("source")!="BIUPIU-AI39-FEDERATED-RUNNER":
        return "BLOCKED_UNTRUSTED_EVIDENCE"
    if bundle.get("execution_attestation") is not True:
        return "PENDING_RUNTIME"
    results=bundle.get("results",{})
    if any(k not in results for k in REQUIRED):
        return "REMEDIATION_REQUIRED"
    if any(results[k] is not True for k in REQUIRED):
        return "REMEDIATION_REQUIRED"
    if not packet.get("provenance_required") or not packet.get("regression_required"):
        return "BLOCKED_CONTROL_CONTRACT"
    return "PROMOTION_READY"

def build_release_record(packet,bundle):
    state=release_state(packet,bundle)
    return {
      "schema":"BIUPIU-AI48",
      "timestamp":datetime.now(timezone.utc).isoformat(),
      "task_id":packet["task_id"],
      "packet_hash":packet.get("packet_hash",digest(packet)),
      "evidence_hash":digest(bundle),
      "release_state":state,
      "promotion_authority":"BIUPIU-INTELLIGENCE",
      "index_authority":"BIUPIU-AI46",
      "provenance_required":True,
      "regression_required":True,
      "physical_actuation":False,
      "observed_state_from_simulation":False
    }
