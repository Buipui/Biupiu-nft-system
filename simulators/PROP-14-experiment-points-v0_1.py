"""PROP-14 experiment-point generator for Biupiu microturbines.
Research/test-planning model only.
"""
from dataclasses import dataclass, asdict
import json

@dataclass
class TestPoint:
    module: str
    altitude_m: float
    pressure_ratio: float
    turbine_inlet_K: float
    recuperator_eff: float
    target_electric_kw: float

def generate():
    return [
        TestPoint(module, alt, pr, 1100, recup, kw)
        for module, kw in (("BT-70",70),("BT-140",140),("BT-200",200),("BT-300",300))
        for alt in (0,2000,5000)
        for pr in (4.0,5.0,6.0)
        for recup in (0.60,0.70,0.80)
    ]

if __name__ == "__main__":
    print(json.dumps([asdict(p) for p in generate()], indent=2))
