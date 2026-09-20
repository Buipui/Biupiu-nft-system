import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "schemas" / "fixtures" / "machine-capability-v1.0.example.json"
VALIDATOR = ROOT / "tests" / "validate_machine_capability.py"

def run_validator(path: Path):
    return subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )

def test_machine_capability_fixture_is_valid():
    result = run_validator(FIXTURE)
    assert result.returncode == 0, result.stderr
    assert "VALID" in result.stdout

def test_unknown_capability_field_fails_closed(tmp_path):
    document = json.loads(FIXTURE.read_text(encoding="utf-8"))
    document["unexpected_field"] = True
    candidate = tmp_path / "invalid.json"
    candidate.write_text(json.dumps(document), encoding="utf-8")
    result = run_validator(candidate)
    assert result.returncode == 1
    assert "unexpected_field" in result.stderr
