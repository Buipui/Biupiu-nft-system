"""Adapter for the existing Biupiu integrated propulsion mission model."""
from pathlib import Path
import importlib.util
def _load():
    p=Path(__file__).resolve().parents[2]/"simulators"/"biupiu_integrated_propulsion_mission_v0_1.py"
    spec=importlib.util.spec_from_file_location("existing_biupiu_mission",p)
    if spec is None or spec.loader is None: raise RuntimeError("mission simulator unavailable")
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
def run(package_name="BT-140", mission="AUTO"):
    m=_load()
    packages={
        "BT-70":m.TurbinePackage("BT-70",70,60,35,25,10,.30),
        "BT-140":m.TurbinePackage("BT-140",140,105,60,40,15,.33),
        "BT-200":m.TurbinePackage("BT-200",200,145,80,55,20,.35),
        "BT-300":m.TurbinePackage("BT-300",300,200,110,75,25,.35),
    }
    if package_name not in packages: raise ValueError("unknown package")
    if mission not in m.MISSIONS: raise ValueError("unknown mission")
    return m.evaluate(packages[package_name],m.MISSIONS[mission])
