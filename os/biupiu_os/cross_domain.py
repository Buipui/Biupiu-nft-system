from __future__ import annotations
from dataclasses import dataclass
from .units import Quantity
@dataclass
class DomainLink:
    source:str; target:str; mapping:dict[str,str]
class CrossDomainValidator:
    def __init__(self): self.links=[]
    def register(self,source,target,mapping): self.links.append(DomainLink(source,target,dict(mapping)))
    def validate_cycle_to_mission(self,cycle,mission):
        issues=[]
        if cycle.get("status")!="completed": issues.append("CYCLE_NOT_COMPLETED")
        if mission.get("status")!="completed": issues.append("MISSION_NOT_COMPLETED")
        target_kw=cycle.get("target_net_kw"); peak=mission.get("peak_battery_kw")
        if target_kw is None: issues.append("CYCLE_MISSING_TARGET_POWER")
        if peak is not None and peak<0: issues.append("NEGATIVE_PEAK_GAP")
        return {"valid":not issues,"issues":issues,"mapped":{"cycle_target_kw":target_kw,"mission_peak_battery_kw":peak}}
    def validate_quantities(self,quantities):
        issues=[]
        for name,q in quantities.items():
            if not isinstance(q,Quantity): issues.append(f"NOT_QUANTITY:{name}")
            elif q.dimension() is None: issues.append(f"UNKNOWN_UNIT:{name}")
        return {"valid":not issues,"issues":issues}
    def bounds(self,values,bounds):
        issues=[]
        for name,(lo,hi) in bounds.items():
            if name in values and not (lo<=values[name]<=hi): issues.append(f"OUT_OF_BOUNDS:{name}")
        return {"valid":not issues,"issues":issues}
    def fuel_rate_consistency(self,cycle):
        issues=[]
        for key in ("fuel_kg_h","air_kg_s"):
            if key in cycle and cycle[key]<0: issues.append("NEGATIVE_"+key.upper())
        return {"valid":not issues,"issues":issues}
