"""Gate 11: fail-closed registration of an explicitly approved World asset."""

import hashlib, json
from pathlib import Path

REQUIRED = ("visual", "provenance", "evidence", "asset_rights")

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def register(handoff_path: Path, asset_id: str, digital_twin_id: str,
             source_path: Path, registry_path: Path) -> dict:
    handoff = json.loads(handoff_path.read_text(encoding="utf-8"))
    approval = handoff.get("approval", {})
    if approval.get("decision") != "APPROVE":
        raise ValueError("BLOCKED: handoff approval decision is not APPROVE")
    missing = [k for k in REQUIRED if approval.get(k) != "PASS"]
    if missing:
        raise ValueError("BLOCKED: required QA checks not PASS: " + ", ".join(missing))
    if not source_path.is_file():
        raise FileNotFoundError("BLOCKED: approved source asset does not exist")

    registry = json.loads(registry_path.read_text(encoding="utf-8")) if registry_path.exists() else []
    if any(x.get("biupiu_asset_id") == asset_id for x in registry):
        raise ValueError("BLOCKED: asset ID already registered; registry is append-only")

    record = {
        "registry_version": "1.0",
        "biupiu_asset_id": asset_id,
        "registration_state": "REGISTERED",
        "handoff": {"handoff_id": handoff.get("handoff_id", ""), "approval": approval},
        "digital_twin": {"id": digital_twin_id},
        "provenance": handoff.get("provenance", {}),
        "claim": handoff.get("claim", {}),
        "targets": handoff.get("targets", {"world": True}),
        "integrity": {
            "source_hash": sha256(source_path),
            "manifest_hash": sha256(handoff_path)
        }
    }
    registry.append(record)
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    registry_path.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")
    return record

if __name__ == "__main__":
    raise SystemExit("Gate 11 is an execution module; invoke register(...) from the controlled pipeline.")
