"""PROP-16 uncertainty propagation, prioritisation and envelope flags."""
from dataclasses import dataclass
import math

@dataclass
class Result:
    value: float
    uncertainty: float

def propagate(*terms):
    variance=sum((t.uncertainty)**2 for t in terms)
    return Result(sum(t.value for t in terms), math.sqrt(variance))

def relative_band(value, fractions):
    sigma=math.sqrt(sum(f*f for f in fractions))
    return {"nominal":value,"low":value*(1-sigma),"high":value*(1+sigma)}

def envelope_flag(value, low, high):
    if value < low: return "BELOW_VALIDATED_ENVELOPE"
    if value > high: return "ABOVE_VALIDATED_ENVELOPE"
    return "WITHIN_VALIDATED_ENVELOPE"

def mission_priority(peak_gap_kw, energy_gap_kwh, uncertainty):
    return (peak_gap_kw * 0.6 + energy_gap_kwh * 0.4) * (1 + uncertainty)
