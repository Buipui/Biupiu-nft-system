from __future__ import annotations
from dataclasses import dataclass
@dataclass(frozen=True)
class Quantity:
    value: float
    unit: str
UNIT_ALIASES={"kw":"kW","kW":"kW","kg/s":"kg/s","kg_h":"kg/h","kg/h":"kg/h","m":"m","m/s":"m/s","kPa":"kPa","K":"K"}
def require(q,unit):
    if q.unit not in UNIT_ALIASES or UNIT_ALIASES[q.unit]!=unit: raise ValueError(f"unit mismatch: expected {unit}, got {q.unit}")
    return q.value
def kg_h_to_kg_s(v): return v/3600.0
