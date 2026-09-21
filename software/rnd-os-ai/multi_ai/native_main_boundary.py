"""AI-NATIVE-02 Native-vs-Main OS boundary audit."""
from dataclasses import dataclass
from enum import Enum
from hashlib import sha256

class Authority(str,Enum):
    NATIVE="native"; MAIN="main"; SHARED="shared"; EXTERNAL="external"

@dataclass(frozen=True)
class Module:
    name:str
    authority:Authority
    interface:str
    status:str

@dataclass(frozen=True)
class BoundaryFinding:
    module:str
    classification:str
    reason:str
    digest:str

def audit(modules:list[Module])->list[BoundaryFinding]:
    out=[]
    for m in modules:
        if not m.interface or not m.name:
            out.append(BoundaryFinding(m.name,"BLOCKED","missing authority/interface",sha256(repr(m).encode()).hexdigest()))
        elif m.authority is Authority.EXTERNAL and m.status=="authoritative":
            out.append(BoundaryFinding(m.name,"CONFLICT","external module cannot be authoritative",sha256(repr(m).encode()).hexdigest()))
        elif m.authority is Authority.SHARED and not m.interface.startswith("CABI:"):
            out.append(BoundaryFinding(m.name,"REVIEW","shared authority requires explicit C ABI boundary",sha256(repr(m).encode()).hexdigest()))
        else:
            out.append(BoundaryFinding(m.name,"PASS","authority and interface are explicit",sha256(repr(m).encode()).hexdigest()))
    return out
