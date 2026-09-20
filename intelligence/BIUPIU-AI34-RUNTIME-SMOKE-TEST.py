"""AI-34 controlled runtime smoke tests for the existing read-only simulator contract."""
from pathlib import Path
import json
from tests.simulator_machine_capability import ReadOnlyCapabilitySimulator

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "schemas/fixtures/machine-capability-v1.0.example.json"

def load():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))

def main():
    sim = ReadOnlyCapabilitySimulator(load())
    a = sim.sample(22.5)
    b = sim.sample(22.5)
    assert a == b
    assert a.state_class == "simulated"
    assert a.unit == "degC"
    assert a.quality == "GOOD"
    try:
        sim.actuate("start")
    except PermissionError:
        pass
    else:
        raise AssertionError("read-only simulator permitted actuation")
    try:
        sim.sample(126)
    except ValueError:
        pass
    else:
        raise AssertionError("out-of-range input was accepted")
    return {"deterministic": True, "state_class": a.state_class, "actuation_blocked": True, "fault_rejected": True}

if __name__ == "__main__":
    print(main())
