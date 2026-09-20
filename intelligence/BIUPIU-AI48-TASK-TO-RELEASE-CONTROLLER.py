"""AI-48 task-to-release control loop.

Requires authenticated execution evidence plus explicit downstream challenge,
validation and regression evidence before PROMOTION_READY.
"""
from __future__ import annotations
import hashlib,json
from datetime import datetime,timezone
REQUIRED=[f"F{i:02d}" for i in range(1,10)]
def digest(v): return hashlib.sha256(json.dumps(v,sort_keys=True).encode()).hexdigest()
def release_state(packet,bundle):
    if bundle.get("source")!="BIUPIU-AI39-FEDERATED-RUNNER": return "BLOCKED_UNTRUSTED_EVIDENCE"
    if bundle.get("execution_attestation") is not True: return "PENDING_RUNTIME"
    results=bundle.get("results",{})
    if any(k not in results for k in REQUIRED) or any(results[k] is not True for k in REQUIRED): return "REMEDIATION_REQUIRED"
    required=("challenge_pass","validation_pass","regression_pass","provenance_required")
    if not all(bundle.get(k) is True for k in required[:3]) or not packet.get("provenance_required"): return "REMEDIATION_REQUIRED"
    return "PROMOTION_READY"
def build_release_record(packet,bundle):
    state=release_state(packet,bundle)
    return {"schema":"BIUPIU-AI48-v2","timestamp":datetime.now(timezone.utc).isoformat(),
      "task_id":packet["task_id"],"packet_hash":packet.get("packet_hash",digest(packet)),
      "evidence_hash":digest(bundle),"release_state":state,
      "promotion_authority":"BIUPIU-INTELLIGENCE","index_authority":"BIUPIU-AI46",
      "provenance_required":True,"regression_required":True,"physical_actuation":False,
      "observed_state_from_simulation":False}
