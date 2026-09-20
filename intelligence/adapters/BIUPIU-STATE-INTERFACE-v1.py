"""Registered state adapter backed by AI-53."""
from pathlib import Path
import importlib.util
P=Path(__file__).resolve().parents[1]/"BIUPIU-AI53-GATE-STATE-MACHINE.py"
s=importlib.util.spec_from_file_location("ai53",P); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
CONTRACT=["state","state_path"]
def handle(value):
 if isinstance(value,list): return {"valid":m.validate_path(value)}
 return {"state":value,"known":value in m.STATES}
