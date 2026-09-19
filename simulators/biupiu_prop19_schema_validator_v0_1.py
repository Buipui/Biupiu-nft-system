"""PROP-19 schema cross-validator.

Checks required fields and validation-state evidence gates without creating
or upgrading physical evidence.
"""
import json
from pathlib import Path

ALLOWED = {"planned", "measured", "bench_tested", "validated", "certified"}

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def validate(record, schema):
    errors = []
    for field in schema.get("required", []):
        if field not in record:
            errors.append(f"MISSING:{field}")
    status = record.get("validation_status")
    if status not in ALLOWED:
        errors.append("INVALID_VALIDATION_STATUS")
    if status in {"validated", "certified"}:
        if record.get("measured_evidence_complete") is not True:
            errors.append("VALIDATED_REQUIRES_MEASURED_EVIDENCE")
        if record.get("review_passed") is not True:
            errors.append("VALIDATED_REQUIRES_REVIEW")
    return errors

def validate_dataset(dataset_path, schema_path):
    data, schema = load(dataset_path), load(schema_path)
    records = data.get("measurements", [])
    results = [{"test_id": r.get("test_id"), "errors": validate(r, schema)}
               for r in records]
    return {"valid": all(not x["errors"] for x in results),
            "record_count": len(records), "records": results}

if __name__ == "__main__":
    import sys
    result = validate_dataset(
        sys.argv[1] if len(sys.argv) > 1 else "digital-twin/datasets/prop15_test_points_v1.json",
        sys.argv[2] if len(sys.argv) > 2 else "digital-twin/schemas/microturbine_test_data_v1.json")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["valid"] else 1)
