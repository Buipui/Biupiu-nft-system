"""AI-NATIVE-03 deterministic cross-gate dependency/regression graph."""
from dataclasses import dataclass
from enum import Enum
from hashlib import sha256

class Edge(str,Enum):
    DEPENDS="depends"; CONFLICTS="conflicts"; PROMOTES="promotes"

@dataclass(frozen=True)
class Gate:
    gate:str
    status:str
    dependencies:tuple[str,...]=()
    authority:str="native"

@dataclass(frozen=True)
class Finding:
    source:str
    target:str
    edge:Edge
    classification:str
    digest:str

def audit(gates:list[Gate])->list[Finding]:
    known={g.gate:g for g in gates}; out=[]
    for g in gates:
        for d in g.dependencies:
            if d not in known:
                raw=f"{g.gate}|{d}|missing"
                out.append(Finding(g.gate,d,Edge.DEPENDS,"BLOCKED",sha256(raw.encode()).hexdigest()))
            else:
                raw=f"{g.gate}|{d}|dependency"
                out.append(Finding(g.gate,d,Edge.DEPENDS,"PASS",sha256(raw.encode()).hexdigest()))
        if g.authority=="external" and g.status=="authoritative":
            raw=f"{g.gate}|external-authority"
            out.append(Finding(g.gate,g.gate,Edge.CONFLICTS,"CONFLICT",sha256(raw.encode()).hexdigest()))
    return out

def deterministic_order(gates:list[Gate])->list[str]:
    known={g.gate:g for g in gates}; pending=set(known); ordered=[]
    while pending:
        ready=sorted(g for g in pending if all(d not in pending for d in known[g].dependencies))
        if not ready:
            raise ValueError("dependency cycle")
        ordered.extend(ready); pending.difference_update(ready)
    return ordered
