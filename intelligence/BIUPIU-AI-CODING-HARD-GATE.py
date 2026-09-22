"""Fail-closed AI coding governance gate.

This is a machine-checkable boundary, not a code-generation engine.
"""
from __future__ import annotations
import json
from pathlib import Path
from typing import Mapping

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "research/BIUPIU-NATIVE-CODING-PHILOSOPHY-AND-ENGINEERING-MATRIX-v1.0.md"
LANGUAGE_MATRIX = ROOT / "research/BIUPIU-MULTILANGUAGE-NATIVE-CODING-MATRIX-v1.0.md"
HARD_GATE = ROOT / "intelligence/BIUPIU-AI-CODING-HARD-GATE-v1.0.json"

REQUIRED_PIPELINE = (
    "REQUIREMENT","OWNER","LANGUAGE","CONTRACT","PROVENANCE","SECURITY",
    "DEPENDENCIES","SEMANTIC_AUDIT","LANGUAGE_TEST","CROSS_LANGUAGE_TEST",
    "REGRESSION","ROLLBACK","PROMOTION",
)

def check_coding_request(request: Mapping[str, object]) -> dict:
    missing = [k for k in REQUIRED_PIPELINE if not request.get(k)]
    if missing:
        return {"allowed": False, "state": "QUARANTINED", "missing": missing}
    if not all(p.is_file() for p in (MATRIX, LANGUAGE_MATRIX, HARD_GATE)):
        return {"allowed": False, "state": "BLOCKED", "missing": ["governance-files"]}
    if request.get("SECURITY") != "PASS" or request.get("SEMANTIC_AUDIT") != "PASS":
        return {"allowed": False, "state": "BLOCKED", "missing": ["security-or-semantic-gate"]}
    return {"allowed": True, "state": "PROPOSAL_READY", "missing": []}

def verify_hard_gate_manifest() -> bool:
    data = json.loads(HARD_GATE.read_text(encoding="utf-8"))
    return tuple(data["pipeline"]) == REQUIRED_PIPELINE and bool(data["fail_closed"])

if __name__ == "__main__":
    print("PASS" if verify_hard_gate_manifest() else "FAIL")
