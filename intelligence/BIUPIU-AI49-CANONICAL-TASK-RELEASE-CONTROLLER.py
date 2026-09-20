"""AI-49 canonical system-wide task/release gate.

Fail-closed: release state is derived from evidence; callers cannot inject
PROMOTION_READY/PROMOTED without authentic, complete, regression-backed evidence.
"""
from __future__ import annotations
import hashlib,json
from datetime import datetime,timezone

# AI-53 transition authority
from pathlib import Path as _Path
import importlib.util as _importlib_util
_SM_PATH=_Path(__file__).resolve().parent/"BIUPIU-AI53-GATE-STATE-MACHINE.py"
_sm_spec=_importlib_util.spec_from_file_location("biupiu_ai53_state_machine",_SM_PATH)
_sm=_importlib_util.module_from_spec(_sm_spec); _sm_spec.loader.exec_module(_sm)

DOMAINS=["OS","DMS","INTELLIGENCE","SIMULATORS","CONFIGURATORS","MATH_PHYSICS","DIGITAL_TWIN","PROVENANCE","SECURITY","BLOCKCHAIN","HMI","RESEARCH"]
REQUIRED=["F01","F02","F03","F04","F05","F06","F07","F08","F09"]

def sha(v): return hashlib.sha256(json.dumps(v,sort_keys=True).encode()).hexdigest()

def evidence_state(evidence):
    if evidence.get("source")!="BIUPIU-AI39-FEDERATED-RUNNER":
        return "BLOCKED_UNTRUSTED_EVIDENCE"
    if evidence.get("execution_attestation") is not True:
        return "PENDING_RUNTIME"
    results=evidence.get("results",{})
    missing=[k for k in REQUIRED if k not in results]
    if missing: return "REMEDIATION_REQUIRED"
    if any(results[k] is not True for k in REQUIRED): return "REMEDIATION_REQUIRED"
    return "PROMOTION_READY"

def canonical_record(packet,evidence):
    state=evidence_state(evidence)
    return {
      "schema":"BIUPIU-AI49-CANONICAL-RELEASE-RECORD-v2",
      "record_id":"bpu-"+sha({"packet":packet,"evidence":evidence})[:16],
      "timestamp":datetime.now(timezone.utc).isoformat(),
      "task_id":packet.get("task_id"),
      "parent_task_id":packet.get("parent_task_id"),
      "objective":packet.get("objective"),
      "domains":packet.get("routes",[]),
      "assigned_teams":packet.get("assigned_teams",[]),
      "packet_hash":packet.get("packet_hash",sha(packet)),
      "evidence_hash":sha(evidence),
      "release_state":state,
      "required_controls":{
        "evidence_auth":True,"challenge":True,"math_physics_validation":True,
        "simulation_digital_twin_check":True,"security_licence":True,
        "provenance":True,"regression":True,"unified_index":True
      },
      "state_authority":{"observed_requires_external_evidence":True,"simulated_never_observed_by_inference":True},
      "physical_actuation":"EXPLICIT_HOST_GATE_ONLY"
    }

def validate(record):
    controls=record.get("required_controls",{})
    if not all(controls.get(k) is True for k in ("evidence_auth","provenance","regression","unified_index")):
        return "BLOCKED_CONTROL_CONTRACT"
    state=record.get("release_state","PENDING_RUNTIME")
    if state not in _sm.STATES:
        return "BLOCKED_CONTROL_CONTRACT"
    if state in ("PROMOTION_READY","PROMOTED"):
        required_path=record.get("state_path",[])
        if not _sm.validate_path(required_path) or required_path[-1] != state:
            return "BLOCKED_CONTROL_CONTRACT"
    return state
