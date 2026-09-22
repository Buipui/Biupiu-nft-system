import json, pathlib, datetime
from jsonschema import Draft202012Validator, FormatChecker

ROOT = pathlib.Path(__file__).resolve().parents[2]
schema_path = ROOT / "buildpui/architecture/BUILDPUI-ARCHITECTURE-SCHEMA-v1.0.schema.json"
fixture_path = ROOT / "buildpui/architecture/fixtures/composite-material.example.json"

schema = json.loads(schema_path.read_text())
fixture = json.loads(fixture_path.read_text())

Draft202012Validator.check_schema(schema)
errors = sorted(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(fixture), key=str)
assert not errors, "\n".join(error.message for error in errors)

assert fixture["evidence_state"] == "RESEARCH-SUPPORTED"
assert fixture["licence"]["status"] == "REVIEW_REQUIRED"
assert "uncertainties" in fixture and "open_questions" in fixture
assert fixture["object_type"] == "CompositeMaterialCard"

print("BUILD PUI SCHEMA TEST: PASS")
