"""Minimal dependency-free validation of the shared AUTO-CMP schema contract."""
import json
from pathlib import Path

SCHEMA = json.loads((Path(__file__).parent / "AUTO-CMP-SHARED-INPUT-SCHEMA-v1.0.json").read_text())

REQUIRED = set(SCHEMA["required"])
ENUMS = {k: set(v["enum"]) for k, v in SCHEMA["properties"].items() if "enum" in v}

def test_schema_has_required_contract():
    expected = {
        "asset_id","revision","source_provenance","evidence_class","units",
        "inputs","assumptions","boundary_conditions","solver_version",
        "uncertainty","validation_status","promotion_status"
    }
    assert REQUIRED == expected
    assert SCHEMA["properties"]["units"]["const"] == "SI"

def test_schema_status_enums_are_closed():
    assert ENUMS["evidence_class"] == {"established","supported_research","plausible_model","unresolved"}
    assert ENUMS["validation_status"] == {"untested","screening","correlated","independently_reviewed"}
    assert ENUMS["promotion_status"] == {"research_only","prototype_candidate","engineering_candidate","released"}
