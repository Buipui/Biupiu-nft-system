"""PROP-12 component-map interface scaffold.

Interfaces are intentionally data-driven so measured compressor, turbine,
generator and recuperator maps can replace placeholders without changing
the mission/digital-twin architecture.
"""
from dataclasses import dataclass
from typing import Callable, Optional

@dataclass
class OperatingPoint:
    corrected_speed: float
    corrected_flow: float
    pressure_ratio: float

@dataclass
class ComponentResult:
    efficiency: float
    pressure_ratio: float
    pressure_loss: float = 0.0
    valid: bool = True

class MapInterface:
    def __init__(self, evaluator: Optional[Callable]=None):
        self.evaluator = evaluator

    def evaluate(self, point: OperatingPoint) -> ComponentResult:
        if self.evaluator:
            return self.evaluator(point)
        return ComponentResult(0.0, point.pressure_ratio, 0.0, False)

def map_validity(result: ComponentResult) -> str:
    if not result.valid:
        return "NO_MAP_DATA"
    if not 0.0 < result.efficiency <= 1.0:
        return "INVALID_EFFICIENCY"
    if result.pressure_ratio <= 1.0:
        return "INVALID_PRESSURE_RATIO"
    return "VALID_SCREENING_POINT"
