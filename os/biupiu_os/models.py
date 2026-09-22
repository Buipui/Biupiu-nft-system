from dataclasses import dataclass,field,asdict
from typing import Any,Optional
VALID_EVIDENCE=("planned","simulated","measured","bench_tested","validated","certified")
@dataclass(frozen=True)
class Capability:
    name:str; domain:str; provider:str; status:str="implemented"; version:str="0.1"; license:str="proprietary-or-adapter"; entrypoint:Optional[str]=None; notes:str=""
@dataclass
class EnvironmentState:
    name:str; timestep_s:float=0.0; variables:dict[str,float]=field(default_factory=dict); entities:dict[str,dict[str,Any]]=field(default_factory=dict); living_systems:dict[str,dict[str,Any]]=field(default_factory=dict); constraints:dict[str,Any]=field(default_factory=dict)
@dataclass
class EvidenceRecord:
    execution_id:str; module:str; evidence_state:str; inputs:dict[str,Any]; outputs:dict[str,Any]; warnings:list[str]=field(default_factory=list); provenance:list[str]=field(default_factory=list); review_passed:bool=False
    def to_dict(self): return asdict(self)
