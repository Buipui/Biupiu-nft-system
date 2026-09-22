"""Executable tests for the machine-checkable AI coding governance boundary."""
from __future__ import annotations
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("biupiu_ai_coding_hard_gate", ROOT / "intelligence/BIUPIU-AI-CODING-HARD-GATE.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)

def test_manifest_is_fail_closed():
    assert MODULE.verify_hard_gate_manifest()

def test_missing_evidence_is_quarantined():
    result = MODULE.check_coding_request({})
    assert result["allowed"] is False
    assert result["state"] == "QUARANTINED"

def test_security_or_semantic_failure_blocks():
    request = {k: True for k in MODULE.REQUIRED_PIPELINE}
    request["SECURITY"] = "FAIL"
    request["SEMANTIC_AUDIT"] = "PASS"
    result = MODULE.check_coding_request(request)
    assert result["allowed"] is False
    assert result["state"] == "BLOCKED"


if __name__ == "__main__":
    test_manifest_is_fail_closed()
    test_missing_evidence_is_quarantined()
    test_security_or_semantic_failure_blocks()
    print("PASS")
