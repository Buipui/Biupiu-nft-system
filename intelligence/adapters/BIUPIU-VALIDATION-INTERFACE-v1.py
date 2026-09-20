"""Registered validation adapter backed by AI-49."""
from pathlib import Path
import importlib.util
P=Path(__file__).resolve().parents[1]/"BIUPIU-AI49-CANONICAL-TASK-RELEASE-CONTROLLER.py"
s=importlib.util.spec_from_file_location("ai49",P); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
CONTRACT=["validation_pass"]
def handle(record): return {"validation_pass":m.validate(record) not in ("BLOCKED_CONTROL_CONTRACT",)}
