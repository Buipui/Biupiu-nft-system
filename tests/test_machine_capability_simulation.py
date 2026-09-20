import json
from pathlib import Path
import pytest
from simulator_machine_capability import ReadOnlyCapabilitySimulator

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "schemas/fixtures/machine-capability-v1.0.example.json"

def load_fixture():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))

def test_simulation_is_deterministic_and_separates_state():
    sim = ReadOnlyCapabilitySimulator(load_fixture())
    first = sim.sample(22.5)
    second = sim.sample(22.5)
    assert first == second
    assert first.state_class == "simulated"
    assert first.unit == "degC"
    assert first.quality == "GOOD"

def test_limits_are_enforced():
    sim = ReadOnlyCapabilitySimulator(load_fixture())
    with pytest.raises(ValueError):
        sim.sample(126)

def test_read_only_cannot_actuate():
    sim = ReadOnlyCapabilitySimulator(load_fixture())
    with pytest.raises(PermissionError):
        sim.actuate("start")

def test_invalid_value_is_rejected():
    sim = ReadOnlyCapabilitySimulator(load_fixture())
    with pytest.raises(ValueError):
        sim.sample("not-a-number")
