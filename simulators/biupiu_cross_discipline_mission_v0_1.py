"""Biupiu cross-discipline microturbine mission model v0.1.

Conceptual screening model only. It compares a common turbine-generator
family across automotive, marine, eVTOL, helicopter and UAV mission cases.
No certification or performance guarantee is implied.
"""

from dataclasses import dataclass


@dataclass
class Turbine:
    name: str
    net_electric_kw: float
    thermal_efficiency: float
    generator_efficiency: float = 0.94
    auxiliary_kw: float = 2.0
    mass_kg: float = 180.0


@dataclass
class Mission:
    name: str
    average_propulsive_kw: float
    peak_propulsive_kw: float
    duration_h: float
    electric_path_efficiency: float = 0.90


def evaluate(t: Turbine, m: Mission) -> dict:
    usable_kw = max(0.0, t.net_electric_kw - t.auxiliary_kw)
    fuel_kw = usable_kw / max(t.thermal_efficiency, 1e-9)
    fuel_kwh = fuel_kw * m.duration_h
    prop_from_turbine = usable_kw * m.electric_path_efficiency

    peak_gap = max(0.0, m.peak_propulsive_kw - prop_from_turbine)
    avg_gap = max(0.0, m.average_propulsive_kw - prop_from_turbine)

    return {
        "mission": m.name,
        "turbine": t.name,
        "net_electric_kw": round(usable_kw, 2),
        "propulsive_kw_from_turbine": round(prop_from_turbine, 2),
        "average_peak_gap_kw": round(avg_gap, 2),
        "peak_power_gap_kw": round(peak_gap, 2),
        "fuel_input_kw": round(fuel_kw, 2),
        "fuel_energy_kwh": round(fuel_kwh, 2),
        "specific_power_kw_per_kg": round(usable_kw / t.mass_kg, 4),
    }


if __name__ == "__main__":
    turbines = [
        Turbine("BT-70", 70, 0.30, mass_kg=120),
        Turbine("BT-140", 140, 0.33, mass_kg=210),
        Turbine("BT-200", 200, 0.35, mass_kg=290),
        Turbine("BT-300", 300, 0.35, mass_kg=400),
    ]

    missions = [
        Mission("Automotive range-extender", 80, 220, 1.0),
        Mission("Marine hybrid cruise", 110, 180, 4.0),
        Mission("eVTOL cruise/transition", 150, 350, 0.75),
        Mission("Helicopter hybrid-electric study", 180, 400, 1.5),
        Mission("UAV endurance extender", 35, 70, 3.0),
    ]

    for turbine in turbines:
        for mission in missions:
            print(evaluate(turbine, mission))
