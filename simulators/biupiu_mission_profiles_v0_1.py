"""PROP-08 mission profiles and battery-buffer screening.
Conceptual research model. Inputs are illustrative and must be replaced with
measured/validated aircraft, marine and vehicle data before engineering use.
"""
from dataclasses import dataclass, asdict
import json

@dataclass
class Phase:
    name: str
    duration_min: float
    demand_kw: float

@dataclass
class Mission:
    name: str
    phases: list
    reserve_fraction: float = 0.15

def battery_buffer(turbine_kw, mission):
    energy_kwh = 0.0
    peak_gap_kw = 0.0
    for p in mission.phases:
        dt_h = p.duration_min / 60.0
        gap = max(0.0, p.demand_kw - turbine_kw)
        peak_gap_kw = max(peak_gap_kw, gap)
        energy_kwh += gap * dt_h
    return {"mission": mission.name, "turbine_kw": turbine_kw,
            "peak_battery_power_kw": round(peak_gap_kw, 2),
            "battery_energy_kwh_with_reserve": round(energy_kwh * (1.0 + mission.reserve_fraction), 2),
            "phases": [asdict(p) for p in mission.phases]}

MISSIONS = [
    Mission("Automotive drive cycle", [Phase("urban",20,60), Phase("highway",25,110), Phase("overtake",1,240), Phase("return",15,80)]),
    Mission("Marine hybrid", [Phase("departure",10,130), Phase("cruise",120,110), Phase("acceleration",5,220), Phase("cruise",60,110)]),
    Mission("eVTOL", [Phase("hover",5,320), Phase("transition",5,260), Phase("cruise",30,150), Phase("reserve",10,220)]),
    Mission("Helicopter hybrid study", [Phase("takeoff",5,380), Phase("climb",10,330), Phase("cruise",45,210), Phase("approach",10,280), Phase("landing",5,300)]),
    Mission("UAV VTOL", [Phase("hover",3,65), Phase("climb",5,55), Phase("cruise",90,32), Phase("landing",3,60)]),
]

if __name__ == "__main__":
    for kw in (70, 140, 200, 300):
        for mission in MISSIONS:
            print(json.dumps(battery_buffer(kw, mission)))