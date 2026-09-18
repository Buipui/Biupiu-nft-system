"""PROP-10 integrated cycle + mission + mass screening model.

Research model only; not a certified propulsion design.
"""
from dataclasses import dataclass, asdict
import json

@dataclass
class TurbinePackage:
    name: str
    net_kw: float
    turbine_mass_kg: float
    recuperator_mass_kg: float
    generator_mass_kg: float
    fuel_system_mass_kg: float
    cycle_efficiency: float
    electric_path_eff: float = 0.90

@dataclass
class MissionPhase:
    name: str
    minutes: float
    demand_kw: float

def evaluate(pkg, phases, battery_specific_energy_whkg=220.0,
             battery_specific_power_wkg=1800.0, reserve=0.15):
    energy_gap = 0.0
    peak_gap = 0.0
    for phase in phases:
        gap = max(0.0, phase.demand_kw - pkg.net_kw * pkg.electric_path_eff)
        energy_gap += gap * phase.minutes / 60.0
        peak_gap = max(peak_gap, gap)
    battery_energy_kwh = energy_gap * (1 + reserve)
    battery_mass_energy = battery_energy_kwh * 1000 / battery_specific_energy_whkg
    battery_mass_power = peak_gap * 1000 / battery_specific_power_wkg
    battery_mass = max(battery_mass_energy, battery_mass_power)
    system_mass = (pkg.turbine_mass_kg + pkg.recuperator_mass_kg +
                   pkg.generator_mass_kg + pkg.fuel_system_mass_kg +
                   battery_mass)
    fuel_energy_kwh = (pkg.net_kw / max(pkg.cycle_efficiency, 1e-9)) *                       (sum(p.minutes for p in phases) / 60.0)
    return {
        "package": pkg.name,
        "battery_mass_kg": round(battery_mass, 2),
        "system_mass_kg": round(system_mass, 2),
        "peak_battery_kw": round(peak_gap, 2),
        "battery_energy_kwh_with_reserve": round(battery_energy_kwh, 2),
        "fuel_energy_input_kwh": round(fuel_energy_kwh, 2),
        "system_specific_power_kw_per_kg": round(pkg.net_kw / system_mass, 4),
    }

MISSIONS = {
    "AUTO": [MissionPhase("urban",20,60),MissionPhase("highway",25,110),
             MissionPhase("overtake",1,240),MissionPhase("return",15,80)],
    "MARINE": [MissionPhase("departure",10,130),MissionPhase("cruise",120,110),
               MissionPhase("acceleration",5,220),MissionPhase("cruise",60,110)],
    "EVTOL": [MissionPhase("hover",5,320),MissionPhase("transition",5,260),
              MissionPhase("cruise",30,150),MissionPhase("reserve",10,220)],
    "HELI": [MissionPhase("takeoff",5,380),MissionPhase("climb",10,330),
             MissionPhase("cruise",45,210),MissionPhase("approach",10,280),
             MissionPhase("landing",5,300)],
    "UAV": [MissionPhase("hover",3,65),MissionPhase("climb",5,55),
            MissionPhase("cruise",90,32),MissionPhase("landing",3,60)]
}

if __name__ == "__main__":
    packages = [
        TurbinePackage("BT-70",70,60,35,25,10,.30),
        TurbinePackage("BT-140",140,105,60,40,15,.33),
        TurbinePackage("BT-200",200,145,80,55,20,.35),
        TurbinePackage("BT-300",300,200,110,75,25,.35),
    ]
    for p in packages:
        for name, phases in MISSIONS.items():
            print(json.dumps(evaluate(p, phases)))
