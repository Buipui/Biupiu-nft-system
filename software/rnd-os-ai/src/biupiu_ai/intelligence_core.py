"""Core deterministic intelligence primitives for Biupiu Intelligence."""
from dataclasses import dataclass
from enum import Enum
from typing import Iterable

EVIDENCE_STATES=("ESTABLISHED","SUPPORTED","PRELIMINARY","HYPOTHESIS","SPECULATIVE","CONTRADICTED","INCONCLUSIVE","UNSUPPORTED")
RELATIONS=("SUPPORTS","CONTRADICTS","REFINES","BUILDS_ON","DERIVED_FROM","TESTS","PRODUCES","DEPENDS_ON")

class TaskStatus(str, Enum):
    NEW="new"; EXECUTING="executing"; EXECUTION_DONE="executionDone"; COMPLETE="complete"
    ON_HOLD="onHold"; FAILED="failed"; INCOMPLETE="incomplete"; STALE="stale"
    FLAGGED_HUMAN="flaggedHuman"; FLAGGED_AI="flaggedAi"; REMOVED="removed"

class Autonomy(str, Enum):
    FULL="Full"; SUPERVISED="Supervised"; LOCKED="Locked"

@dataclass(frozen=True)
class EvidenceEdge:
    source_id:str; target_id:str; relation:str; evidence_state:str; provenance_refs:tuple[str,...]=()

@dataclass(frozen=True)
class AgentTask:
    task_id:str; objective:str; domains:tuple[str,...]; irreversible:bool=False
    evidence_refs:tuple[str,...]=(); dependencies:tuple[str,...]=()
    purpose:str=""; status:TaskStatus=TaskStatus.NEW

@dataclass(frozen=True)
class RouteDecision:
    domains:tuple[str,...]; requires_human_approval:bool; allowed_actions:tuple[str,...]

def make_edge(source_id:str,target_id:str,relation:str,evidence_state:str,provenance_refs:Iterable[str]=())->EvidenceEdge:
    if not source_id or not target_id: raise ValueError("source_id and target_id are required")
    if relation not in RELATIONS: raise ValueError(f"invalid relation: {relation}")
    if evidence_state not in EVIDENCE_STATES: raise ValueError(f"invalid evidence_state: {evidence_state}")
    return EvidenceEdge(source_id,target_id,relation,evidence_state,tuple(provenance_refs))

def grounded(edge:EvidenceEdge)->bool:
    return edge.evidence_state in {"ESTABLISHED","SUPPORTED","PRELIMINARY"}

def dependency_closure(root:str,edges:Iterable[EvidenceEdge])->set[str]:
    adjacency={}
    for edge in edges:
        if edge.relation in {"DEPENDS_ON","PRODUCES"}: adjacency.setdefault(edge.source_id,set()).add(edge.target_id)
    seen=set(); stack=[root]
    while stack:
        node=stack.pop()
        if node in seen: continue
        seen.add(node); stack.extend(adjacency.get(node,()))
    return seen

def route_task(task:AgentTask)->RouteDecision:
    if not task.task_id or not task.objective: raise ValueError("task_id and objective are required")
    return RouteDecision(tuple(dict.fromkeys(task.domains)),task.irreversible,("retrieve","analyse","simulate","propose"))

def validate_agent_result(*,evidence_refs:Iterable[str],evidence_state:str,human_approved:bool,irreversible:bool)->bool:
    if evidence_state not in EVIDENCE_STATES or not tuple(evidence_refs): return False
    if evidence_state in {"UNSUPPORTED","CONTRADICTED"}: return False
    return not irreversible or human_approved
