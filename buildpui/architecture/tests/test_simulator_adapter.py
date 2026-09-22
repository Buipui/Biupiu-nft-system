import json
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
module_path = ROOT / "buildpui/architecture/BUILDPUI-SIMULATOR-ADAPTER-v1.0.py"

spec = importlib.util.spec_from_file_location("buildpui_adapter", module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

adapter = module.BuildPuiSchemaAdapter()
fixture = json.loads(
    (ROOT / "buildpui/architecture/fixtures/composite-material.example.json")
    .read_text(encoding="utf-8")
)

validated = adapter.validate_object(fixture)
assert validated["object_id"] == "BP-COMP-EXAMPLE-001"
assert adapter.simulation_permission(validated) is False
assert adapter.engineering_validation_allowed(validated) is False

invalid = dict(fixture)
invalid.pop("provenance")
try:
    adapter.validate_object(invalid)
except module.BuildPuiSchemaError:
    pass
else:
    raise AssertionError("Invalid object was accepted")

print("BUILD PUI ADAPTER CONTRACT TEST: PASS")
