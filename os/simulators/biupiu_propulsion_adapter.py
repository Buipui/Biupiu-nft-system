"""Adapter for the existing Biupiu propulsion concept simulator; model code is not copied."""
from pathlib import Path
import importlib.util
def _load():
    p=Path(__file__).resolve().parents[2]/"simulators"/"biupiu_propulsion_simulator.py"
    spec=importlib.util.spec_from_file_location("existing_biupiu_propulsion",p)
    if spec is None or spec.loader is None: raise RuntimeError("propulsion simulator unavailable")
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
def run(rpm=2000.0,throttle=1.0,speed_kph=60.0,battery_assist_kw=0.0,grade=0.0):
    m=_load(); sim=m.PropulsionSimulator()
    return sim.run_point(rpm,throttle,speed_kph,battery_assist_kw,grade)
