"""AI-75 governed autonomous orchestration reference.

Deterministic planning only. No network, secrets, deployment or physical actuation.
"""
from __future__ import annotations
import hashlib, json
from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class Decision:
    action: str
    authority: str
    requires_human: bool
    reason: str

SAFE_AUTONOMY = {
    "observe","classify","deduplicate","route","harvest","cross_check",
    "schedule_test","record_learning","update_index","run_regression"
}
HUMAN_GATED = {
    "promote","release","publish","deploy_contract","spend","handle_secret",
    "change_security_boundary","physical_actuation"
}

def plan(actions, authority_ok=True, evidence_ok=True, regression_ok=True):
    out=[]
    for action in actions:
        if action in SAFE_AUTONOMY and authority_ok:
            out.append(Decision(action,"BIUPIU-INTELLIGENCE",False,"governed autonomous action"))
        elif action in HUMAN_GATED:
            out.append(Decision(action,"BIUPIU-GOVERNANCE",True,"irreversible or high-impact action"))
        else:
            out.append(Decision(action,"BIUPIU-GOVERNANCE",True,"authority/evidence/regression boundary not satisfied"))
    packet={"decisions":[asdict(x) for x in out]}
    packet["packet_hash"]=hashlib.sha256(json.dumps(packet,sort_keys=True).encode()).hexdigest()
    return packet

if __name__=="__main__":
    print(json.dumps(plan(["observe","harvest","cross_check","record_learning","update_index","promote"]),indent=2,sort_keys=True))
