"""PROP-18: validate PROP-15 records against the evidence-state rules."""
import json
from pathlib import Path
from biupiu_evidence_state_engine_v0_1 import validate_record


def validate_dataset(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    records = data.get("measurements", [])
    results = []
    for record in records:
        check = validate_record(record)
        results.append({"test_id": record.get("test_id"), **check})
    return {
        "schema_version": data.get("schema_version"),
        "record_count": len(records),
        "valid": all(r["valid"] for r in results),
        "records": results,
    }


if __name__ == "__main__":
    import sys
    result = validate_dataset(sys.argv[1] if len(sys.argv) > 1 else
                              "digital-twin/datasets/prop15_test_points_v1.json")
    print(json.dumps(result, indent=2))
