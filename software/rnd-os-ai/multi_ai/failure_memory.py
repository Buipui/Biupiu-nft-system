"""AI-NATIVE-04 deterministic failure-learning and regression memory."""
from dataclasses import dataclass,asdict
from hashlib import sha256
import json

@dataclass(frozen=True)
class Failure:
    failure_id:str
    gate:str
    category:str
    message:str
    evidence_digest:str
    resolution:str=""
    resolved:bool=False

class FailureMemory:
    def __init__(self): self._items={}
    def record(self,gate,category,message,evidence,resolution="",resolved=False):
        digest=sha256(evidence.encode()).hexdigest()
        fid=sha256(f"{gate}|{category}|{message}|{digest}".encode()).hexdigest()
        item=Failure(fid,gate,category,message,digest,resolution,resolved)
        self._items[fid]=item
        return item
    def resolve(self,failure_id,resolution):
        if failure_id not in self._items: raise KeyError(failure_id)
        old=self._items[failure_id]
        self._items[failure_id]=Failure(old.failure_id,old.gate,old.category,old.message,old.evidence_digest,resolution,True)
        return self._items[failure_id]
    def regressions_for(self,gate):
        return [asdict(x) for x in self._items.values() if x.gate==gate]
    def export(self):
        return json.dumps([asdict(x) for x in sorted(self._items.values(),key=lambda x:x.failure_id)],sort_keys=True,separators=(",",":"))
