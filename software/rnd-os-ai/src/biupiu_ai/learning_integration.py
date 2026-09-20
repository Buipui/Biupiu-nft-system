"""Integration boundary between governed learning and Biupiu OS/AI routing.

Learning emits evidence and proposals. It never writes authoritative OS state.
"""
from dataclasses import dataclass
from typing import Mapping, Sequence
from .learning import FailureObservation, summarize_failure_pattern, fingerprint_failure

@dataclass(frozen=True)
class IntegrationDecision:
    target: str
    action: str
    evidence_state: str
    requires_os_validation: bool
    promotion_allowed: bool
    reason: str

def route_learning_event(event: Mapping[str, object]) -> IntegrationDecision:
    target=str(event.get("target","Biupiu Intelligence"))
    action=str(event.get("action","REVIEW"))
    evidence=str(event.get("evidence_state","INCONCLUSIVE"))
    # Fail closed: learning cannot directly promote authoritative OS state.
    if action == "PROMOTE_CORE":
        return IntegrationDecision(target,action,evidence,True,False,
                                   "Core OS promotion requires an independent OS validation gate.")
    if evidence in {"CONTRADICTED","SPECULATIVE","INCONCLUSIVE"}:
        return IntegrationDecision(target,action,evidence,True,False,
                                   "Evidence is not sufficient for autonomous promotion.")
    return IntegrationDecision(target,action,evidence,True,
                               bool(event.get("human_approved",False)),
                               "Eligible for OS validation; human approval remains required for promotion.")

def build_failure_learning_event(target_id:str,failure_class:str,state_signature:str,
                                 *,platform:str="unknown",fixed:bool=False,
                                 regression_passed:bool=False)->dict:
    fp=fingerprint_failure(failure_class,state_signature,target_id=target_id,platform=platform)
    obs=FailureObservation(target_id,failure_class,fp,state_signature,fixed,regression_passed,platform=platform)
    pattern=summarize_failure_pattern([obs])
    return {
        "target":"Biupiu Intelligence",
        "action":"LEARN",
        "evidence_state":"SUPPORTED" if fixed else "PRELIMINARY",
        "human_approved":False,
        "failure_fingerprint":fp,
        "learning_level":pattern.learning_level,
        "requires_os_validation":True,
    }
