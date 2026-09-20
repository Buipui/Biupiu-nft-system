"""Registered evidence adapter backed by AI-44."""
from pathlib import Path
import importlib.util
P=Path(__file__).resolve().parents[1]/"BIUPIU-AI44-REAL-EVIDENCE-GATE.py"
s=importlib.util.spec_from_file_location("ai44",P); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
CONTRACT=["execution_attestation","results"]
def handle(bundle): return m.evaluate(bundle)
