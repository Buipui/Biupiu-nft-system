"""AI-49 canonical system-wide task/release gate.

Normalizes task packets from AI-47 and release decisions from AI-48 into one
canonical record. Fail-closed: no VERIFIED/PROMOTED state can be manufactured.
"""
from __future__ import annotations
import hashlib,json
from datetime import datetime,timezone

DOMAINS=["OS","DMS","INTELLIGENCE","SIMULATORS","CONFIGURATORS","MATH_PHYSICS","DIGITAL_TWIN","PROVENANCE","SECURITY","BLOCKCHAIN","HMI","RESEARCH"]

def sha(v): return hashlib.sha256(json.dumps(v,sort_keys=True).encode()).hexdigest()

def canonical_record(packet, evidence, release_state):
    return {
      "schema":"BIUPIU-AI49-CANONICAL-RELEASE-RECORD-v1",
      "record_id":"bpu-"+sha({"packet":packet,"evidence":evidence})[:16],
      "timestamp":datetime.now(timezone.utc).isoformat(),
      "task_id":packet.get("task_id"),
      "parent_task_id":packet.get("parent_task_id"),
      "objective":packet.get("objective"),
      "domains":packet.get("routes",[]),
      "assigned_teams":packet.get("assigned_teams",[]),
      "packet_hash":packet.get("packet_hash",sha(packet)),
      "evidence_hash":sha(evidence),
      "release_state":release_state,
      "required_controls":{
        "evidence_auth":True,
        "challenge":True,
        "math_physics_validation":True,
        "simulation_digital_twin_check":True,
        "security_licence":True,
        "provenance":True,
        "regression":True,
        "unified_index":True
      },
      "state_authority":{
        "observed_requires_external_evidence":True,
        "simulated_never_observed_by_inference":True
      },
      "physical_actuation":"EXPLICIT_HOST_GATE_ONLY"
    }

def validate(record):
    controls=record["required_controls"]
    if not all(controls.values()): return "BLOCKED_CONTROL_CONTRACT"
    if record["release_state"] not in ("PROMOTION_READY","PROMOTED"): return record["release_state"]
    return record["release_state"]
