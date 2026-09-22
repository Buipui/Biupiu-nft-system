"""Biupiu Digital Filing Cabinet — standalone metadata catalogue."""
from dataclasses import dataclass, field, asdict
from hashlib import sha256
from typing import Any
import json, time, uuid

@dataclass
class FilingRecord:
    title: str
    artifact_type: str
    source_uri: str
    language: str = "en"
    licence: str = "UNKNOWN"
    evidence_state: str = "PRELIMINARY"
    authority_system: str = "DIGITAL_FILING_CABINET"
    artifact_id: str = field(default_factory=lambda: "ART-"+uuid.uuid4().hex)
    source_commit: str|None = None
    domain: str|None = None
    capability_ids: list[str] = field(default_factory=list)
    parent_id: str|None = None
    related_ids: list[str] = field(default_factory=list)
    validation_level: str = "UNVERIFIED"
    implementation_state: str = "REFERENCE_ONLY"
    metadata: dict[str,Any] = field(default_factory=dict)
    retrieved_at: float = field(default_factory=time.time)

    def fingerprint(self)->str:
        return sha256(json.dumps(asdict(self),sort_keys=True,default=str).encode()).hexdigest()

class DigitalFilingCabinet:
    def __init__(self):
        self.records: dict[str,FilingRecord]={}
        self.links: dict[str,set[str]]={}
    def file(self, record:FilingRecord)->str:
        if record.licence=="UNKNOWN" or not record.source_uri:
            raise ValueError("record requires provenance/licence classification")
        self.records[record.artifact_id]=record
        self.links.setdefault(record.artifact_id,set())
        return record.artifact_id
    def link(self,a:str,b:str,relation:str="related")->None:
        if a not in self.records or b not in self.records: raise KeyError("unknown artifact")
        self.links.setdefault(a,set()).add(b)
        self.records[a].metadata.setdefault("relations",[]).append({"to":b,"type":relation})
    def export_catalogue(self)->str:
        return json.dumps([asdict(x) for x in self.records.values()],indent=2,sort_keys=True,default=str)
