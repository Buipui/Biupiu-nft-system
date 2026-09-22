"""Biupiu Digital Orchestra — dependency-light native orchestration seed."""
from __future__ import annotations
from dataclasses import dataclass, field, asdict
from enum import Enum
from hashlib import sha256
from typing import Any, Iterable
import json
import time
import uuid

class Evidence(str, Enum):
    ESTABLISHED="ESTABLISHED"; SUPPORTED="SUPPORTED"; PRELIMINARY="PRELIMINARY"
    HYPOTHESIS="HYPOTHESIS"; SPECULATIVE="SPECULATIVE"; CONTRADICTED="CONTRADICTED"; INCONCLUSIVE="INCONCLUSIVE"

class WorkState(str, Enum):
    DISCOVERED="DISCOVERED"; CLASSIFIED="CLASSIFIED"; PLANNED="PLANNED"; ROUTED="ROUTED"
    EXECUTING="EXECUTING"; OBSERVED="OBSERVED"; VERIFIED="VERIFIED"; DIGESTED="DIGESTED"
    FILED="FILED"; LEARNED="LEARNED"; PROMOTED="PROMOTED"; QUARANTINED="QUARANTINED"

@dataclass(frozen=True)
class Provenance:
    source_uri: str
    source_kind: str
    language: str = "en"
    licence: str = "UNKNOWN"
    retrieved_at: float = field(default_factory=time.time)
    source_commit: str | None = None
    notes: str = ""

@dataclass
class WorkItem:
    title: str
    capability: str
    evidence: Evidence
    provenance: Provenance
    state: WorkState = WorkState.DISCOVERED
    correlation_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    inputs: dict[str, Any] = field(default_factory=dict)
    outputs: dict[str, Any] = field(default_factory=dict)
    history: list[dict[str, Any]] = field(default_factory=list)

    def transition(self, target: WorkState, reason: str = "") -> None:
        allowed = {
            WorkState.DISCOVERED:{WorkState.CLASSIFIED,WorkState.QUARANTINED},
            WorkState.CLASSIFIED:{WorkState.PLANNED,WorkState.QUARANTINED},
            WorkState.PLANNED:{WorkState.ROUTED,WorkState.QUARANTINED},
            WorkState.ROUTED:{WorkState.EXECUTING,WorkState.QUARANTINED},
            WorkState.EXECUTING:{WorkState.OBSERVED,WorkState.QUARANTINED},
            WorkState.OBSERVED:{WorkState.VERIFIED,WorkState.DIGESTED,WorkState.QUARANTINED},
            WorkState.VERIFIED:{WorkState.DIGESTED},
            WorkState.DIGESTED:{WorkState.FILED,WorkState.LEARNED},
            WorkState.FILED:{WorkState.LEARNED,WorkState.PROMOTED},
            WorkState.LEARNED:{WorkState.PROMOTED},
            WorkState.PROMOTED:set(),
            WorkState.QUARANTINED:{WorkState.CLASSIFIED},
        }
        if target not in allowed[self.state]:
            raise ValueError(f"Invalid transition {self.state} -> {target}")
        self.history.append({"from":self.state.value,"to":target.value,"reason":reason,"timestamp":time.time()})
        self.state=target

    def fingerprint(self) -> str:
        payload=json.dumps({
            "title":self.title,"capability":self.capability,"evidence":self.evidence.value,
            "provenance":asdict(self.provenance),"inputs":self.inputs,"outputs":self.outputs
        },sort_keys=True,default=str).encode()
        return sha256(payload).hexdigest()

class DigitalOrchestra:
    """Coordinates governed work; authority remains outside the router."""
    def __init__(self) -> None:
        self.items: dict[str,WorkItem]={}
        self.events:list[dict[str,Any]]=[]

    def register(self,item:WorkItem)->str:
        if item.correlation_id in self.items: raise ValueError("duplicate correlation_id")
        self.items[item.correlation_id]=item
        self._event("REGISTER",item,{"fingerprint":item.fingerprint()})
        return item.correlation_id

    def route(self,correlation_id:str,route:Iterable[str])->None:
        item=self.items[correlation_id]
        item.outputs["route"]=list(route)
        item.transition(WorkState.CLASSIFIED,"orchestra classification")
        item.transition(WorkState.PLANNED,"orchestra planning")
        item.transition(WorkState.ROUTED,"orchestra route locked")
        self._event("ROUTE",item,{"route":item.outputs["route"]})

    def observe(self,correlation_id:str,result:dict[str,Any])->None:
        item=self.items[correlation_id]
        item.outputs.update(result)
        item.transition(WorkState.EXECUTING,"execution started")
        item.transition(WorkState.OBSERVED,"execution result recorded")
        self._event("OBSERVE",item,result)

    def verify(self,correlation_id:str,passed:bool,evidence:Evidence)->None:
        item=self.items[correlation_id]; item.evidence=evidence
        item.transition(WorkState.VERIFIED if passed else WorkState.QUARANTINED,
                        "verification passed" if passed else "verification failed")
        self._event("VERIFY",item,{"passed":passed,"evidence":evidence.value})

    def digest_and_file(self,correlation_id:str,filing_path:str)->None:
        item=self.items[correlation_id]
        if item.state not in {WorkState.VERIFIED,WorkState.OBSERVED}:
            raise ValueError("digest requires observed or verified evidence")
        item.outputs["filing_path"]=filing_path
        item.transition(WorkState.DIGESTED,"knowledge digest created")
        item.transition(WorkState.FILED,"canonical filing recorded")
        self._event("FILE",item,{"filing_path":filing_path})

    def _event(self,event_type:str,item:WorkItem,payload:dict[str,Any])->None:
        self.events.append({"event_id":str(uuid.uuid4()),"event_type":event_type,
            "correlation_id":item.correlation_id,"evidence_state":item.evidence.value,
            "payload":payload,"timestamp":time.time()})

    def export_journal(self)->str:
        return json.dumps(self.events,indent=2,sort_keys=True,default=str)

def make_harvest_item(title:str,uri:str,language:str,licence:str,
                      source_kind:str="EXTERNAL_REPOSITORY")->WorkItem:
    return WorkItem(title=title,capability="external-harvest",evidence=Evidence.PRELIMINARY,
        provenance=Provenance(source_uri=uri,source_kind=source_kind,language=language,licence=licence))
