"""Deterministic source-level smoke audit for Biupiu's systemwide module graph."""
from __future__ import annotations
import ast, json, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
REQUIRED = [
"docs/architecture/BIUPIU-DESIGN-LANGUAGE-CODE-CONTRACT-v1.0.json",
"docs/architecture/BIUPIU-ANDROID-CROSS-SYSTEM-FUNCTION-GRAPH-2026-09-22.md",
"docs/architecture/BIUPIU-CROSS-SYSTEM-MODULE-HARVEST-MATRIX-2026-09-22.json",
"docs/architecture/BIUPIU-SYSTEMWIDE-MODULE-REGISTRY-v1.0.json",
"research/BIUPIU-UI-SEMANTIC-ACTION-CONTRACT-v1.0.md",
"research/BIUPIU-DESIGN-TWIN-FEDERATED-LEARNING-HARD-CODE-GATE-2026-09-22.md",
"software/rnd-os-ai/src/biupiu_ai/learning_federation_bridge.py",
"packages/biupiu-rnd-os/src/digital-twin.ts",
"packages/biupiu-rnd-os/src/federation-transport.ts",
"apps/android/app/src/main/java/com/biupiu/rndos/CapabilityRouter.kt",
"apps/android/app/src/main/java/com/biupiu/rndos/DepartmentModuleRegistry.kt",
"apps/android/app/src/main/AndroidManifest.xml"]
def fail(msg): print("FAIL:", msg); raise SystemExit(1)
for rel in REQUIRED:
    if not (ROOT/rel).is_file(): fail(f"missing integration anchor: {rel}")
for rel in [p for p in REQUIRED if p.endswith(".json")]:
    try: json.loads((ROOT/rel).read_text(encoding="utf-8"))
    except Exception as exc: fail(f"invalid JSON {rel}: {exc}")
for path in (ROOT/"software").rglob("*.py"):
    try: ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError as exc: fail(f"Python syntax error {path}: {exc}")
hub=(ROOT/"apps/android/app/src/main/java/com/biupiu/rndos/MainHubActivity.kt").read_text(encoding="utf-8")
if "when (module.screenId)" not in hub or "startActivity(Intent(this, activityClass))" not in hub: fail("Android semantic route handler incomplete")
registry=(ROOT/"apps/android/app/src/main/java/com/biupiu/rndos/DepartmentModuleRegistry.kt").read_text(encoding="utf-8")
for route in ["SMART_FARMING","SMART_METAL_WORKSHOP","RND_OS","RENDER_PIPELINE","CREATIVE_AI"]:
    if route not in registry: fail(f"missing Android route: {route}")
for path in (ROOT/"apps/android").rglob("*.kt"):
    if re.search(r"onClick\s*=\s*\{\s*\}", path.read_text(encoding="utf-8")): fail(f"empty Android click handler: {path}")
print("PASS: required module anchors present")
print("PASS: JSON manifests parse")
print("PASS: Python source parses")
print("PASS: Android route/semantic-handler checks")
print("PASS: no empty Android click handlers")
print("BOUNDARY: device/UE5/GPU/HIL/runtime verification remains separate")