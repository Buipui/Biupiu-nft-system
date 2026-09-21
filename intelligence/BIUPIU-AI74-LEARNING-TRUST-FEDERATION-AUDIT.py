"""AI-74 deterministic audit for learning -> trust -> optional anchor federation.

Read-only. No network, wallet, key, contract, or physical actuation.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = {
    "learning_protocol": ROOT / "intelligence/BIUPIU-LEARNING-PROTOCOL-v2.md",
    "promotion_controller": ROOT / "intelligence/BIUPIU-AI41-EVIDENCE-PROMOTION-CONTROLLER.py",
    "provenance_adapter": ROOT / "intelligence/BIUPIU-AI42-DMS-PROVENANCE-ADAPTER.py",
    "trust_algorithm": ROOT / "trust/ALGORITHM-v1.md",
    "trust_protocol": ROOT / "trust/TRUST-PROTOCOL-v1.md",
    "federation_gate": ROOT / "intelligence/BIUPIU-AI38-SYSTEM-FEDERATION-GATE-v1.0.md",
}

def sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()

def merkle_root(items: list[str]) -> str:
    if not items:
        return sha256("")
    layer = [sha256(x) for x in items]
    while len(layer) > 1:
        if len(layer) % 2:
            layer.append(layer[-1])
        layer = [sha256(layer[i] + layer[i + 1]) for i in range(0, len(layer), 2)]
    return layer[0]

def run() -> dict:
    presence = {name: path.exists() for name, path in REQUIRED.items()}
    sample_events = [
        "learning:event:failure-fingerprint:v2",
        "learning:event:cross-validation-success:v2",
        "evidence:promotion:verified:v1",
    ]
    root = merkle_root(sample_events)
    return {
        "gate": "AI-74",
        "required_artifacts_present": all(presence.values()),
        "artifact_presence": presence,
        "learning_to_trust_boundary": all(presence.values()),
        "historical_mutation_policy": "append-only",
        "checkpoint_algorithm": "deterministic-merkle-root",
        "external_blockchain_mode": "optional-anchor-only",
        "live_blockchain_transaction_verified": False,
        "production_signing_verified": False,
        "runtime_verified": False,
        "sample_checkpoint_root": root,
        "promotion_allowed": False,
        "verification_level": "STATIC_DETERMINISTIC",
    }

if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
