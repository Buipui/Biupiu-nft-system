"""Biupiu Multi-AI Architecture Builder v1.0."""
from __future__ import annotations
from dataclasses import dataclass, field, asdict
from enum import Enum
from hashlib import sha256
from typing import Iterable

class Role(str, Enum):
    HARVESTER="harvester"; ARCHITECT="architect"; RESEARCHER="researcher"
    IMPLEMENTER="implementer"; VERIFIER="verifier"; SECURITY="security"
    INTEGRATOR="integrator"; AUDITOR="auditor"

class State(str, Enum):
    DISCOVERED="discovered"; HARVESTED="harvested"; PROPOSED="proposed"
    IMPLEMENTED="implemented"; VERIFIED="verified"; REJECTED="rejected"; BLOCKED="blocked"

@dataclass(frozen=True)
class Evidence:
    source:str; kind:str; digest:str; licence:str="unknown"; reproducibility:str="unknown"
    @staticmethod
    def from_text(source:str, kind:str, text:str, licence:str="unknown")->"Evidence":
        return Evidence(source,kind,sha256(text.encode("utf-8")).hexdigest(),licence,"deterministic-input")

@dataclass
class WorkItem:
    item_id:str; objective:str; state:State=State.DISCOVERED
    roles:list[Role]=field(default_factory=list); evidence:list[Evidence]=field(default_factory=list)
    dependencies:list[str]=field(default_factory=list); failures:list[str]=field(default_factory=list)
    decisions:list[str]=field(default_factory=list)
    def signature(self)->str:
        payload=f"{self.item_id}|{self.objective}|{self.state}|{self.dependencies}|{self.decisions}"
        return sha256(payload.encode("utf-8")).hexdigest()

class MultiAIOrchestrator:
    REQUIRED_ROLES=(Role.HARVESTER,Role.ARCHITECT,Role.RESEARCHER,Role.IMPLEMENTER,
                    Role.VERIFIER,Role.SECURITY,Role.INTEGRATOR,Role.AUDITOR)
    def create(self,item_id:str,objective:str,dependencies:Iterable[str]=())->WorkItem:
        return WorkItem(item_id,objective,dependencies=list(dependencies),roles=list(self.REQUIRED_ROLES))
    def harvest(self,item:WorkItem,evidence:Iterable[Evidence])->WorkItem:
        item.evidence.extend(evidence); item.state=State.HARVESTED; return item
    def propose(self,item:WorkItem,decision:str)->WorkItem:
        if item.state not in (State.HARVESTED,State.PROPOSED): raise ValueError("proposal requires harvested evidence")
        item.decisions.append(decision); item.state=State.PROPOSED; return item
    def implement(self,item:WorkItem)->WorkItem:
        if item.state!=State.PROPOSED: raise ValueError("implementation requires an approved proposal")
        item.state=State.IMPLEMENTED; return item
    def verify(self,item:WorkItem,passed:bool,failure:str|None=None)->WorkItem:
        if item.state!=State.IMPLEMENTED: raise ValueError("verification requires implementation")
        if passed: item.state=State.VERIFIED
        else:
            item.state=State.BLOCKED
            if failure: item.failures.append(failure)
        return item
    def audit_record(self,item:WorkItem)->dict:
        return asdict(item)|{"signature":item.signature()}
