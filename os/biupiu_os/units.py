from __future__ import annotations
from dataclasses import dataclass
DIMENSIONS={"dimensionless":{},"W":{"power":1},"kW":{"power":1},"kJ/kg":{"energy":1,"mass":-1},"kg/s":{"mass":1,"time":-1},"kg/h":{"mass":1,"time":-1},"K":{"temperature":1},"kPa":{"pressure":1},"m":{"length":1},"m/s":{"length":1,"time":-1},"W/kg":{"power":1,"mass":-1},"kW/kg":{"power":1,"mass":-1}}
SCALE={"dimensionless":1.0,"W":1.0,"kW":1000.0,"kJ/kg":1000.0,"kg/s":1.0,"kg/h":1/3600.0,"K":1.0,"kPa":1000.0,"m":1.0,"m/s":1.0,"W/kg":1.0,"kW/kg":1000.0}
@dataclass(frozen=True)
class Quantity:
    value:float
    unit:str
    def dimension(self): return DIMENSIONS.get(self.unit)
    def to(self,target):
        if self.unit not in DIMENSIONS or target not in DIMENSIONS: raise ValueError("unknown unit")
        if self.dimension()!=DIMENSIONS[target]: raise ValueError(f"dimensional mismatch: {self.unit} -> {target}")
        return Quantity(self.value*SCALE[self.unit]/SCALE[target],target)
def require(q,unit): return q.to(unit).value
def kg_h_to_kg_s(v): return Quantity(v,"kg/h").to("kg/s").value
