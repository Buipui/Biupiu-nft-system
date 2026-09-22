"""Native bounded guided fault finding for Intelligence and native ML."""
from dataclasses import dataclass
from typing import Mapping,Sequence
from .learning import FailureObservation,fingerprint_failure,summarize_failure_pattern
_NEXT={"TRANSPORT":"verify delivery/TTL/backpressure","DEPENDENCY":"compare dependency/version lock state","CONTRACT":"validate schema/version/content-type","VALIDATION":"re-run the failing validation with captured inputs","AUTHORITY":"identify canonical owner and open reconciliation","MODEL":"compare assumptions, units and model version","DATA":"validate provenance/schema/range/unit constraints","RUNTIME":"capture trace/span and environment","SECURITY":"quarantine affected path and run integrity checks"}
@dataclass(frozen=True)
class GuidedFault:
    fault_id:str;fault_class:str;state:str;confidence:float;next_step:str;candidate_causes:Sequence[str];required_evidence:Sequence[str]
def guide_fault(event:Mapping[str,object])->GuidedFault:
    c=str(event.get("fault_class","RUNTIME"))
    if c not in _NEXT: raise ValueError("unsupported fault_class")
    e=tuple(str(x) for x in event.get("evidence_refs",()) if str(x))
    return GuidedFault(str(event.get("fault_id","unknown")),c,"QUARANTINED" if c=="SECURITY" else "TRIAGING",.7 if e else .35,_NEXT[c],(str(event.get("message","")),str(event.get("state_signature",""))),(_NEXT[c],"record result and residual error","regression-test before closure"))
def learn_fault(event:Mapping[str,object])->dict:
    target=str(event.get("target_id","unknown"));c=str(event.get("fault_class","unknown")).lower();sig=str(event.get("state_signature",""));platform=str(event.get("platform","unknown"))
    fp=fingerprint_failure(c,sig,target_id=target,platform=platform);obs=FailureObservation(target,c,fp,sig,bool(event.get("fixed",False)),bool(event.get("regression_passed",False)),platform=platform);p=summarize_failure_pattern([obs])
    return {"failure_fingerprint":fp,"learning_level":p.learning_level,"requires_os_validation":True,"promotion_allowed":False}
