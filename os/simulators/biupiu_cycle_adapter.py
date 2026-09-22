"""Adapter for the existing Biupiu cycle-physics screening model."""
from pathlib import Path
import importlib.util
def _load():
    p=Path(__file__).resolve().parents[2]/"simulators"/"biupiu_cycle_physics_v0_1.py"
    spec=importlib.util.spec_from_file_location("existing_biupiu_cycle",p)
    if spec is None or spec.loader is None: raise RuntimeError("cycle simulator unavailable")
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
def run(target_kw=140.0, altitude_m=0.0, pressure_ratio=5.0, compressor_eff=.78, turbine_eff=.80,
        recuperator_eff=.70, cold_dp_frac=.03, hot_dp_frac=.03, turbine_inlet_K=1100.0,
        generator_eff=.94, accessory_kw=3.0, lhv_kjkg=43000.0):
    m=_load()
    c=m.Cycle(pressure_ratio,compressor_eff,turbine_eff,recuperator_eff,cold_dp_frac,
              hot_dp_frac,turbine_inlet_K,generator_eff,accessory_kw)
    return m.screen(c,target_kw,altitude_m,lhv_kjkg)
