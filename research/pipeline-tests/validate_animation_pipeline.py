#!/usr/bin/env python3
"""Static validation for the Biupiu animation pipeline Gate 3 artifacts.

This validator intentionally does not require USD or OTIO runtimes. It checks
the repository-level contract before runtime integration is attempted.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
USD = ROOT / "research/pipeline-tests/usd/minimal_scene.usda"
OTIO = ROOT / "research/pipeline-tests/otio/biupiu_showreel_timeline.json"

def fail(message: str) -> None:
    raise SystemExit(f"VALIDATION FAILED: {message}")

if not USD.is_file():
    fail(f"missing {USD}")
if not OTIO.is_file():
    fail(f"missing {OTIO}")

usd = USD.read_text(encoding="utf-8")
required_usd = [
    "#usda 1.0",
    'defaultPrim = "BiupiuScene"',
    'custom string biupiuResearchId = "BIUPIU-ANIM-GATE1-001"',
    'def Camera "AnimatedCamera"',
    "xformOp:translate.timeSamples",
]
for token in required_usd:
    if token not in usd:
        fail(f"USD contract missing: {token}")

try:
    otio = json.loads(OTIO.read_text(encoding="utf-8"))
except json.JSONDecodeError as exc:
    fail(f"OTIO JSON is invalid: {exc}")

if otio.get("OTIO_SCHEMA") != "Timeline.1":
    fail("unexpected OTIO_SCHEMA")
if otio.get("name") != "Biupiu_Showreel_Gate2":
    fail("unexpected OTIO timeline name")

tracks = otio.get("tracks", {}).get("children", [])
if len(tracks) != 1:
    fail("expected exactly one video track")
track = tracks[0]
if track.get("kind") != "Video":
    fail("expected a Video track")

clips = track.get("children", [])
if len(clips) != 1:
    fail("expected exactly one clip")
clip = clips[0]
duration = clip.get("source_range", {}).get("duration", {})
if duration.get("value") != 48 or duration.get("rate") != 24:
    fail("expected 48 frames at 24 fps")

media = clip.get("media_reference", {}).get("target_url", "")
if not media.endswith("tests/media/usd_scene_test_render.mov"):
    fail("unexpected media target")

print("VALIDATION PASSED: Biupiu animation pipeline static contract is intact.")
