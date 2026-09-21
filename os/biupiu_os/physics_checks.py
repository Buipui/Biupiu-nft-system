from __future__ import annotations
from dataclasses import dataclass
@dataclass
class CheckResult:
    valid:bool
    issues:list[str]
    metrics:dict
def cycle_energy_balance(result,cp=1005.0,lhv_kjkg=43000.0,tolerance=0.02):
    issues=[]; metrics={}
    required=("air_kg_s","fuel_kg_h","target_net_kw","specific_electric_work_kj_kg")
    missing=[k for k in required if k not in result]
    if missing: return CheckResult(False,["MISSING:"+k for k in missing],metrics)
    air=result["air_kg_s"]; fuel=result["fuel_kg_h"]/3600.0; target=result["target_net_kw"]
    specific=result["specific_electric_work_kj_kg"]
    predicted_kw=air*specific
    metrics.update({"predicted_net_kw":predicted_kw,"target_net_kw":target,"relative_power_residual":(predicted_kw-target)/max(abs(target),1e-9)})
    if abs(metrics["relative_power_residual"])>tolerance: issues.append("POWER_BALANCE_RESIDUAL")
    if air<=0: issues.append("NONPOSITIVE_AIR_FLOW")
    if fuel<0: issues.append("NEGATIVE_FUEL_FLOW")
    if lhv_kjkg<=0: issues.append("INVALID_LHV")
    metrics["fuel_thermal_kw"]=fuel*lhv_kjkg
    if metrics["fuel_thermal_kw"]<target: issues.append("THERMAL_INPUT_BELOW_TARGET_OUTPUT")
    return CheckResult(not issues,issues,metrics)
def temperature_order(result):
    issues=[]
    vals={k:result.get(k) for k in ("ambient_K","T2_K","T3_K","T5_K")}
    if any(v is None for v in vals.values()): return CheckResult(False,["MISSING_TEMPERATURE"],{})
    if vals["ambient_K"]<=0 or any(v<=0 for v in vals.values()): issues.append("NONPOSITIVE_TEMPERATURE")
    if vals["T3_K"]<vals["T2_K"]: issues.append("RECUPERATOR_TEMPERATURE_REVERSAL")
    return CheckResult(not issues,issues,vals)
