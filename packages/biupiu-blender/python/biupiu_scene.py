"""Minimal Blender-side adapter entry point for Biupiu Digital Twin records."""
import json

def load_digital_twin(path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def apply_metadata(scene, twin):
    scene["biupiu_id"] = twin.get("biupiu_id", "")
    scene["biupiu_version"] = twin.get("version", "")
    scene["biupiu_asset_type"] = twin.get("asset_type", "")
    scene["biupiu_evidence_classification"] = twin.get("evidence_classification", "")
    scene["biupiu_asset_hash"] = twin.get("asset_hash", "")

def register():
    pass
