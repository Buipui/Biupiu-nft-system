"""PROP-13 map dataset and uncertainty interface.
Research-only: published values are reference anchors, not Biupiu measurements.
"""
from dataclasses import dataclass

@dataclass
class MapPoint:
    corrected_speed: float
    corrected_flow: float
    pressure_ratio: float
    efficiency: float

@dataclass
class Evidence:
    source_id: str
    source_type: str
    status: str
    notes: str

REFERENCE_EVIDENCE = [
    Evidence("RG-2026-10kWe-mgt", "ResearchGate", "reference", "2026 study uses normalized compressor/turbine maps and experimental recuperator calibration."),
    Evidence("RG-2017-recuperator-review", "ResearchGate", "reference", "Review identifies effectiveness versus pressure-loss trade-off."),
    Evidence("RG-2017-EV-range-extender", "ResearchGate", "reference", "Range-extender study uses compressor/turbine maps and operating-envelope checks."),
]

def interpolate_linear(x0,x1,y0,y1,x):
    if x1 == x0: return y0
    return y0 + (y1-y0)*(x-x0)/(x1-x0)

def uncertainty_band(value, relative=0.10):
    return {"nominal":value,"low":value*(1-relative),"high":value*(1+relative)}