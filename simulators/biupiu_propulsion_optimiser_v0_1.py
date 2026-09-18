"""PROP-11 parameter sweep / feasibility screening.

Research-only optimisation scaffold. It does not certify a propulsion system.
"""
from dataclasses import dataclass, asdict
import json

@dataclass
class Point:
    turbine_kw: float
    battery_kwh: float
    pressure_ratio: float
    tit_k: float
    recuperator_eff: float
    altitude_m: float

def screen(p):
    # First-order screening penalties/bonuses; replace with validated maps later.
    alt_factor = max(0.55, 1.0 - 0.000045 * p.altitude_m)
    thermal_factor = min(1.0, max(0.65, p.recuperator_eff / 0.75))
    pr_factor = min(1.05, max(0.70, p.pressure_ratio / 6.0))
    tit_factor = min(1.10, max(0.70, p.tit_k / 1200.0))
    effective_kw = p.turbine_kw * alt_factor * thermal_factor * pr_factor * tit_factor
    feasible_power = effective_kw >= 0.75 * p.turbine_kw
    feasible_battery = p.battery_kwh >= 10.0
    feasible_thermal = p.tit_k <= 1250.0 and p.recuperator_eff >= 0.55
    return {
        "point": asdict(p),
        "effective_net_kw_screen": round(effective_kw, 2),
        "power_flag": feasible_power,
        "battery_flag": feasible_battery,
        "thermal_flag": feasible_thermal,
        "feasible": feasible_power and feasible_battery and feasible_thermal,
    }

def sweep():
    out=[]
    for kw in (70,140,200,300):
        for batt in (20,50,100,200):
            for pr in (4.0,5.0,6.0):
                for tit in (1000,1100,1200):
                    for recup in (0.60,0.70,0.80):
                        for alt in (0,2000,5000):
                            out.append(screen(Point(kw,batt,pr,tit,recup,alt)))
    return out

if __name__=="__main__":
    results=sweep()
    print(json.dumps({"schema_version":"PROP-11-v1.0","count":len(results),"results":results}, indent=2))
