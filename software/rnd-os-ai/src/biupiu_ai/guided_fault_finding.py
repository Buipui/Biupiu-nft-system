"""Native bounded guided fault finding for Intelligence, native ML and federation."""
from dataclasses import dataclass
from typing import Mapping, Sequence
from .learning import FailureObservation, fingerprint_failure, summarize_failure_pattern
from .learning_federation_bridge import AppendOnlyLearningLog, make_event

_NEXT={"TRANSPORT":"verify delivery/TTL/backpressure","DEPENDENCY":"compare dependency/version lock state","CONTRACT":"validate schema/version/content-type","VALIDATION":"re-run the failing validation with captured inputs","AUTHORITY":"identify canonical owner and open reconciliation","MODEL":"compare assumptions, units and model version","DATA":"validate provenance/schema/range/unit constraints","RUNTIME":"capture trace/span and environment","SECURITY":"quarantine affected path and run integrity checks"}
_FAILURE_CLASS_MAP={"TRANSPORT":"integration","DEPENDENCY":"dependency","CONTRACT":"interface","VALIDATION":"logic","AUTHORITY":"provenance","MODEL":"numerical","DATA":"data","RUNTIME":"runtime","SECURITY":"provenance"}

@dataclass(frozen=True)
class FaultFixRule:
    fault_class:str
    diagnostic_action:str
    fix_action:str
    validation_action:str
    regression_required:bool=True
    human_promotion_required:bool=True

_FAULT_FIX_MATRIX={
    "TRANSPORT": FaultFixRule("TRANSPORT","capture delivery/TTL/backpressure evidence","repair routing/queue policy only after evidence","replay the failing delivery path"),
    "DEPENDENCY": FaultFixRule("DEPENDENCY","compare dependency/version lock state","restore a compatible pinned version or isolate the dependency","clean-build and dependency regression"),
    "CONTRACT": FaultFixRule("CONTRACT","validate schema/version/content-type","repair the contract boundary without changing authority","contract and compatibility regression"),
    "VALIDATION": FaultFixRule("VALIDATION","re-run the failing validation with captured inputs","correct the smallest validated logic defect","unit plus regression test"),
    "AUTHORITY": FaultFixRule("AUTHORITY","identify canonical owner and conflicting state","reconcile through the owning system; never overwrite silently","authority/reconciliation regression"),
    "MODEL": FaultFixRule("MODEL","compare assumptions, units and model version","correct model/configuration with explicit assumptions","numerical/model regression"),
    "DATA": FaultFixRule("DATA","validate provenance/schema/range/unit constraints","quarantine or repair invalid data at the boundary","data-contract regression"),
    "RUNTIME": FaultFixRule("RUNTIME","capture trace/span and environment","apply the smallest reversible runtime fix","runtime smoke and regression"),
    "SECURITY": FaultFixRule("SECURITY","quarantine affected path and run integrity checks","do not auto-repair; route to security review","security regression and human release"),
}

@dataclass(frozen=True)
class GuidedFault:
    fault_id:str; fault_class:str; state:str; confidence:float; next_step:str
    candidate_causes:Sequence[str]; required_evidence:Sequence[str]

def guide_fault(event:Mapping[str,object])->GuidedFault:
    c=str(event.get("fault_class","RUNTIME")).strip().upper()
    if c not in _NEXT: raise ValueError("unsupported fault_class")
    e=tuple(str(x) for x in event.get("evidence_refs",()) if str(x))
    return GuidedFault(str(event.get("fault_id","unknown")),c,"QUARANTINED" if c=="SECURITY" else "TRIAGING",.7 if e else .35,_NEXT[c],(str(event.get("message","")),str(event.get("state_signature",""))),(_NEXT[c],"record result and residual error","regression-test before closure"))

def learn_fault(event:Mapping[str,object])->dict:
    target=str(event.get("target_id","unknown")); c=str(event.get("fault_class","RUNTIME")).strip().upper()
    if c not in _FAILURE_CLASS_MAP: raise ValueError("unsupported fault_class")
    fc=_FAILURE_CLASS_MAP[c]; sig=str(event.get("state_signature","")); platform=str(event.get("platform","unknown"))
    fp=fingerprint_failure(fc,sig,target_id=target,platform=platform)
    obs=FailureObservation(target,fc,fp,sig,bool(event.get("fixed",False)),bool(event.get("regression_passed",False)),platform=platform,evidence_refs=tuple(str(x) for x in event.get("evidence_refs",()) if str(x)))
    p=summarize_failure_pattern([obs])
    return {"failure_fingerprint":fp,"failure_class":fc,"learning_level":p.learning_level,"requires_os_validation":True,"promotion_allowed":False}

def federate_fault(log:AppendOnlyLearningLog,event:Mapping[str,object])->dict:
    finding=guide_fault(event); learned=learn_fault(event)
    refs=tuple(str(x) for x in event.get("evidence_refs",()) if str(x))
    if not refs: raise ValueError("evidence_refs are required for federation logging")
    envelope=make_event("FAILURE","guided-fault-finder",str(event.get("target_id","unknown")),"guided-fault-v1",{"fault_id":finding.fault_id,"fault_class":finding.fault_class,"state":finding.state,"next_step":finding.next_step,"failure_fingerprint":learned["failure_fingerprint"],"learning_level":learned["learning_level"],"promotion_allowed":False},refs)
    log.append(envelope)
    return {"event_id":envelope.event_id,"fault_id":finding.fault_id,"state":finding.state,"failure_fingerprint":learned["failure_fingerprint"],"learning_level":learned["learning_level"],"promotion_allowed":False,"requires_os_validation":True}

def fault_fix_rule(fault_class:str)->FaultFixRule:
    key=str(fault_class).strip().upper()
    try: return _FAULT_FIX_MATRIX[key]
    except KeyError as exc: raise ValueError("unsupported fault_class") from exc
