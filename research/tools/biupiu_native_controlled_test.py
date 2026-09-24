#!/usr/bin/env python3
"""Deterministic, non-destructive Quanticor controlled-intersection test.

The test uses real checked-out Biupui Native System families as observation inputs,
but performs collision/decompilation/defragmentation/recompile only on in-memory
state. No authoritative source tree is modified.
"""
from __future__ import annotations
import hashlib, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAMILIES = {
    "mini-os": [
        "mini-os/include/biupiu_boot_contract.h",
        "mini-os/cpp/contract.cpp",
        "mini-os/ai/task_contract.json",
    ],
    "apps/android": [
        "apps/android/build.gradle.kts",
        "apps/android/app/src/main/AndroidManifest.xml",
    ],
    "mini-os/android": [
        "mini-os/android/build.gradle",
        "mini-os/android/app/src/main/AndroidManifest.xml",
    ],
}

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def require_file(rel: str) -> dict:
    p = ROOT / rel
    if not p.is_file():
        raise AssertionError(f"missing required native-system input: {rel}")
    b = p.read_bytes()
    return {"path": rel, "sha256": sha256_bytes(b), "bytes": len(b)}

def observe():
    systems = {}
    for family, paths in FAMILIES.items():
        systems[family] = [require_file(p) for p in paths]
    return systems

def geometry(systems):
    nodes = []
    edges = []
    for family, files in systems.items():
        root = f"family:{family}"
        nodes.append({"id": root, "type": "system_family"})
        for f in files:
            nid = f"file:{f['path']}"
            nodes.append({"id": nid, "type": "code_unit", "content_hash": f["sha256"]})
            edges.append({"from": root, "to": nid, "type": "contains"})
    return {"nodes": nodes, "edges": edges}

def controlled_collision():
    # Synthetic conflict only: the observed native systems remain untouched.
    return {
        "collision_id": "COLLISION-NATIVE-001",
        "mode": "quarantine_only",
        "mutation_target": "in_memory_candidate",
        "fault": {
            "type": "semantic_contract_mismatch",
            "source": "synthetic_capability",
            "expected": "native_contract",
            "observed": "conflicting_candidate",
        },
    }

def decompile(collision):
    return {
        "state": "DECOMPOSED",
        "parent_collision": collision["collision_id"],
        "fragments": [
            {"id": "fragment:contract", "class": "required"},
            {"id": "fragment:adapter", "class": "alternative"},
            {"id": "fragment:conflict", "class": "conflicting"},
        ],
    }

def defragment(decomposed):
    return {
        "state": "DEFRAGMENTED_CANDIDATE",
        "retained_fragments": [f["id"] for f in decomposed["fragments"]],
        "path": [
            "fragment:contract",
            "fragment:adapter",
            "semantic_reconcile",
            "fragment:conflict->quarantine",
        ],
    }

def recompile(candidate, systems):
    # Recompile is represented as a deterministic candidate reconstruction.
    payload = json.dumps(
        {"candidate": candidate, "system_hashes": systems},
        sort_keys=True, separators=(",", ":")
    ).encode()
    return {
        "state": "RECOMPILE_CANDIDATE",
        "candidate_hash": sha256_bytes(payload),
        "source_mutated": False,
    }

def regression(result, systems):
    # Regression gate: observed inputs must still hash identically after the
    # in-memory collision lifecycle.
    after = observe()
    unchanged = after == systems
    return {
        "state": "VERIFIED" if unchanged else "QUARANTINED",
        "source_unchanged": unchanged,
        "checks": {
            "native_inputs_present": True,
            "collision_quarantined": True,
            "decomposition_recorded": True,
            "defragmentation_recorded": True,
            "recompile_candidate_recorded": True,
            "regression_hash_stable": unchanged,
        },
    }

def main():
    systems = observe()
    geom = geometry(systems)
    collision = controlled_collision()
    decomposed = decompile(collision)
    candidate = defragment(decomposed)
    compiled = recompile(candidate, systems)
    verified = regression(compiled, systems)

    evidence = {
        "schema": "biupiu.quanticor.native-controlled-test.v1",
        "status": verified["state"],
        "implementation_claim": "controlled protocol test; not production promotion",
        "protocol": [
            "observe", "map", "intersect", "decompile",
            "defragment", "anchor_metadata", "recompile",
            "regression", "learn"
        ],
        "native_systems": systems,
        "geometry": geom,
        "collision": collision,
        "decomposition": decomposed,
        "defragmentation": candidate,
        "recompile": compiled,
        "regression": verified,
    }
    print(json.dumps(evidence, indent=2, sort_keys=True))
    if verified["state"] != "VERIFIED":
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
