"""CannaPiu outdoor tent/awning screening solver.

Engineering screening only; not a certification or code-compliance tool.
Uses transparent static-load and cantilever checks with explicit units.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from math import pi
from typing import Dict


@dataclass(frozen=True)
class TentInput:
    span_m: float = 4.0
    bay_length_m: float = 3.0
    height_m: float = 2.6
    pole_area_m2: float = 0.0004
    pole_inertia_m4: float = 1.0e-8
    pole_length_m: float = 2.6
    material_e_pa: float = 70.0e9
    material_allowable_pa: float = 120.0e6
    membrane_mass_kg: float = 45.0
    equipment_mass_kg: float = 60.0
    wind_pressure_pa: float = 600.0
    rain_pressure_pa: float = 250.0
    safety_factor: float = 1.5
    anchor_capacity_n: float = 2500.0


def _positive(name: str, value: float) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def solve(inp: TentInput) -> Dict[str, float | bool | str]:
    for name in ("span_m", "bay_length_m", "height_m", "pole_area_m2", "pole_inertia_m4",
                 "pole_length_m", "material_e_pa", "material_allowable_pa",
                 "safety_factor", "anchor_capacity_n"):
        _positive(name, getattr(inp, name))
    for name in ("membrane_mass_kg", "equipment_mass_kg", "wind_pressure_pa", "rain_pressure_pa"):
        if getattr(inp, name) < 0:
            raise ValueError(f"{name} cannot be negative")

    area = inp.span_m * inp.bay_length_m
    gravity = 9.80665
    dead_n = (inp.membrane_mass_kg + inp.equipment_mass_kg) * gravity
    rain_n = inp.rain_pressure_pa * area
    wind_n = inp.wind_pressure_pa * area
    factored_vertical_n = inp.safety_factor * (dead_n + rain_n)
    factored_horizontal_n = inp.safety_factor * wind_n
    pole_count = 4.0
    axial_n = factored_vertical_n / pole_count
    lateral_n = factored_horizontal_n / pole_count
    moment_nm = lateral_n * inp.pole_length_m / 2.0
    axial_stress_pa = axial_n / inp.pole_area_m2
    bending_stress_pa = moment_nm * (0.5 * (inp.pole_area_m2 ** 0.5)) / inp.pole_inertia_m4
    combined_stress_pa = axial_stress_pa + bending_stress_pa
    utilization = combined_stress_pa / inp.material_allowable_pa
    euler_pcr_n = (pi ** 2 * inp.material_e_pa * inp.pole_inertia_m4) / (inp.pole_length_m ** 2)
    buckling_utilization = axial_n * inp.safety_factor / euler_pcr_n
    anchor_demand_n = factored_horizontal_n / pole_count
    anchor_utilization = anchor_demand_n / inp.anchor_capacity_n
    overturning_nm = factored_horizontal_n * inp.height_m / 2.0
    resisting_nm = factored_vertical_n * inp.span_m / 4.0
    overturning_ratio = resisting_nm / overturning_nm if overturning_nm else float("inf")
    max_utilization = max(utilization, buckling_utilization, anchor_utilization)
    return {
        "area_m2": area,
        "dead_load_n": dead_n,
        "factored_vertical_n": factored_vertical_n,
        "factored_horizontal_n": factored_horizontal_n,
        "axial_stress_pa": axial_stress_pa,
        "bending_stress_pa": bending_stress_pa,
        "combined_stress_pa": combined_stress_pa,
        "stress_utilization": utilization,
        "euler_buckling_load_n": euler_pcr_n,
        "buckling_utilization": buckling_utilization,
        "anchor_demand_n": anchor_demand_n,
        "anchor_utilization": anchor_utilization,
        "overturning_resistance_ratio": overturning_ratio,
        "max_utilization": max_utilization,
        "screening_pass": max_utilization <= 1.0 and overturning_ratio >= 1.0,
        "status": "SCREENING_ONLY",
    }


if __name__ == "__main__":
    import json
    print(json.dumps(solve(TentInput()), indent=2, sort_keys=True))
