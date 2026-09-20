"""Registered release adapter backed by AI-49."""
from pathlib import Path
import importlib.util
P=Path(__file__).resolve().parents[1]/"BIUPIU-AI49-CANONICAL-TASK-RELEASE-CONTROLLER.py"
s=importlib.util.spec_from_file_location("ai49",P); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
CONTRACT=["release_state"]
def handle(packet,evidence): return m.canonical_record(packet,evidence)
