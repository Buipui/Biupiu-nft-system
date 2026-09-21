from __future__ import annotations
from dataclasses import dataclass
from .units import kg_h_to_kg_s
@dataclass
class DomainLink:
    source:str; target:str; mapping:dict[str,str]
class CrossDomainValidator:
    def __init__(self): self.links=[]
    def register(self,source,target,mapping):
        self.links.append(DomainLink(source,target,dict(mapping)))
    def validate_cycle_to_mission(self,cycle,mission):
        issues=[]
        if cycle.get("status")!="completed": issues.append("CYCLE_NOT_COMPLETED")
        if mission.get("status")!="completed": issues.append("MISSION_NOT_COMPLETED")
        target_kw=cycle.get("target_net_kw")
        if target_kw is None: issues.append("CYCLE_MISSING_TARGET_POWER")
        peak=mission.get("peak_battery_kw")
        if peak is not None and target_kw is not None and peak<0: issues.append("NEGATIVE_PEAK_GAP")
        return {"valid":not issues,"issues":issues,"mapped":{"cycle_target_kw":target_kw,"mission_peak_battery_kw":peak}}
    def fuel_rate_consistency(self,cycle):
        issues=[]
        if "fuel_kg_h" in cycle and cycle["fuel_kg_h"]<0: issues.append("NEGATIVE_FUEL_RATE")
        if "air_kg_s" in cycle and cycle["air_kg_s"]<0: issues.append("NEGATIVE_AIR_FLOW")
        return {"valid":not issues,"issues":issues}
