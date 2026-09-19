"""PROP-18 regression guards for evidence-state integrity."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "simulators"))

from biupiu_evidence_state_engine_v0_1 import Observation, anomaly, state_transition, validate_record


def test_planned_observation_cannot_be_treated_as_measured():
    result = anomaly(Observation("T1", "power", planned=70, measured=None))
    assert result["flag"] == "INSUFFICIENT_DATA"


def test_validation_requires_measured_evidence_and_review():
    record = {
        "test_id": "T1", "module": "BT-70", "application": "AUTO",
        "validation_status": "validated",
        "measured_evidence_complete": False, "review_passed": False
    }
    result = validate_record(record)
    assert not result["valid"]


def test_planned_state_does_not_promote_from_simulation_only():
    assert state_transition("planned", False, False) == "planned"


def test_validated_state_is_not_downgraded_by_new_screening():
    assert state_transition("validated", False, False) == "validated"
