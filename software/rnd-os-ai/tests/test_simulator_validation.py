from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from simulator_validation import validate_backends


def test_validation_is_non_executing_and_not_production_approved():
    result = validate_backends()
    assert result["gate"] == "SIM-OSS-03"
    assert result["mode"] == "non-executing-local-probe"
    assert result["production_approved"] is False
    assert result["records"]
    for record in result["records"]:
        assert record["status"] in {"ready", "not-installed"}
