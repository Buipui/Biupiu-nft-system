#!/usr/bin/env python3
"""Gate 4 repository-level validation for the Biupiu USD/OTIO test contract."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
USD = ROOT / "research/pipeline-tests/usd/minimal_scene.usda"
OTIO = ROOT / "research/pipeline-tests/otio/biupiu_showreel_timeline.json"
def check(condition, message):
    if not condition: raise SystemExit("VALIDATION FAILED: " + message)
check(USD.is_file(), "USD test scene missing")
check(OTIO.is_file(), "OTIO test manifest missing")
usd = USD.read_text(encoding="utf-8")
for token in ("#usda 1.0", 'defaultPrim = "BiupiuScene"', 'def Camera "AnimatedCamera"', "xformOp:translate.timeSamples"):
    check(token in usd, "USD contract missing: " + token)
timeline = json.loads(OTIO.read_text(encoding="utf-8"))
check(timeline.get("OTIO_SCHEMA") == "Timeline.1", "OTIO schema mismatch")
tracks = timeline.get("tracks", [])
check(len(tracks) == 1 and tracks[0].get("kind") == "Video", "expected exactly one Video track")
clips = tracks[0].get("children", [])
check(len(clips) == 1, "expected exactly one clip")
duration = clips[0].get("source_range", {}).get("duration", {})
check(duration.get("value") == 48 and duration.get("rate") == 24, "expected 48 frames at 24 fps")
target = clips[0].get("media_reference", {}).get("target_url", "")
check(target.endswith("tests/media/usd_scene_test_render.mov"), "unexpected media target")
print("VALIDATION PASSED: Gate 4 static USD/OTIO contract.")
