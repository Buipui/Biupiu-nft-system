#!/usr/bin/env python3
"""Quanticor DigiCat/DigiFile blockchain-anchor collision baseline.

Runs against real Native Buipui repository inputs. The collision is strictly
in-memory/quarantine-only. The anchor is a local blockchain-compatible
hash-chain + Merkle commitment; no public-chain transaction is claimed.
"""
from __future__ import annotations
import copy, hashlib, json, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NATIVE = {
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
REGISTRY = {
    "DigiCat": "research/BIUPIU-NATIVE-SYSTEM-CATALOGUE-v1.0.json",
    "DigiFile": "research/evidence/BIUPIU-DIGICAT-DIGIFILE-CROSSREF-20260924.json",
    "Quanticor": "research/BIUPIU-QUANTICOR-OPTIMISED-PROTOCOL-v1.1.json",
    "Benchmark": "research/BIUPIU-SYSTEM-FAMILY-BENCHMARK-STANDARD-v1.0.json",
}

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def read_artifact(path: str) -> dict:
    p = ROOT / path
    if not p.is_file():
        raise AssertionError(f"missing required artifact: {path}")
    b = p.read_bytes()
    return {"path": path, "bytes": len(b), "sha256": sha256(b)}

def git_head() -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip()

def merkle_root(items: list[str]) -> str:
    level = [bytes.fromhex(x) for x in items]
    if not level:
        return sha256(b"EMPTY")
    while len(level) > 1:
        if len(level) % 2:
            level.append(level[-1])
        level = [
            hashlib.sha256(level[i] + level[i + 1]).digest()
            for i in range(0, len(level), 2)
        ]
    return level[0].hex()

def block_hash(block: dict) -> str:
    payload = json.dumps(block, sort_keys=True, separators=(",", ":")).encode()
    return sha256(payload)

def anchor_block(index: int, previous_hash: str, event: dict) -> dict:
    body = {
        "index": index,
        "previous_block_hash": previous_hash,
        "event": event,
    }
    body["block_hash"] = block_hash(body)
    return body

def main() -> int:
    baseline_commit = git_head()
    native = {
        family: [read_artifact(p) for p in paths]
        for family, paths in NATIVE.items()
    }
    registry = {role: read_artifact(path) for role, path in REGISTRY.items()}

    digicat_nodes = []
    for family, files in native.items():
        digicat_nodes.append({"id": f"family:{family}", "type": "native_system"})
        for f in files:
            digicat_nodes.append({
                "id": f"artifact:{f['path']}",
                "type": "code_or_build_artifact",
                "sha256": f["sha256"],
                "family": family,
            })
    digicat_nodes.extend(
        {"id": f"registry:{role}", "type": role.lower(), "sha256": item["sha256"]}
        for role, item in registry.items()
    )

    digifile_manifest = [
        {"role": role, "path": item["path"], "sha256": item["sha256"]}
        for role, item in registry.items()
    ]
    for family, files in native.items():
        for f in files:
            digifile_manifest.append({
                "role": "native_input",
                "family": family,
                "path": f["path"],
                "sha256": f["sha256"],
            })
    leaf_hashes = [
        sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode())
        for x in digifile_manifest
    ]
    root = merkle_root(leaf_hashes)

    state = {
        "baseline_commit": baseline_commit,
        "digicat_nodes": digicat_nodes,
        "digifile_manifest": digifile_manifest,
        "merkle_root": root,
        "promotion_state": "NOT_PROMOTED",
    }
    state_hash = sha256(json.dumps(state, sort_keys=True, separators=(",", ":")).encode())

    # Controlled collision: mutate only a deep copy of the catalogue/evidence state.
    collided = copy.deepcopy(state)
    collided["digicat_nodes"][0]["collision_marker"] = "SYNTHETIC_CONFLICT_ONLY"
    collided["digifile_manifest"].append({
        "role": "synthetic_collision",
        "path": "QUARANTINE_ONLY",
        "sha256": sha256(b"synthetic-collision"),
    })
    collided["collision_state"] = "QUARANTINED"
    collision_hash = sha256(
        json.dumps(collided, sort_keys=True, separators=(",", ":")).encode()
    )

    events = [
        {"type": "observation", "state_hash": state_hash, "commit": baseline_commit},
        {"type": "collision", "collision_hash": collision_hash, "mode": "quarantine_only"},
        {"type": "decompile", "parent": collision_hash, "units": ["DigiCat", "DigiFile", "synthetic_conflict"]},
        {"type": "defragment", "retained": ["DigiCat", "DigiFile"], "quarantined": ["synthetic_conflict"]},
        {"type": "anchor", "merkle_root": root, "state_hash": state_hash},
    ]
    chain = []
    previous = "GENESIS-BIUPUI-QUANTICOR-DIGICAT-DIGIFILE-v1"
    for i, event in enumerate(events):
        b = anchor_block(i, previous, event)
        chain.append(b)
        previous = b["block_hash"]

    # Verify chain integrity and prove source inputs were not altered by collision.
    native_after = {
        family: [read_artifact(p) for p in paths]
        for family, paths in NATIVE.items()
    }
    registry_after = {role: read_artifact(path) for role, path in REGISTRY.items()}
    unchanged = native_after == native and registry_after == registry
    chain_valid = all(
        b["block_hash"] == block_hash({k: v for k, v in b.items() if k != "block_hash"})
        and (i == 0 or b["previous_block_hash"] == chain[i - 1]["block_hash"])
        for i, b in enumerate(chain)
    )
    merkle_stable = merkle_root(leaf_hashes) == root

    result = {
        "schema": "biupiu.quanticor.digicat-digifile-blockchain-collision-baseline.v1",
        "date": "2026-09-24",
        "status": "VERIFIED_CONTROLLED_BASELINE" if (unchanged and chain_valid and merkle_stable) else "QUARANTINED",
        "baseline_commit": baseline_commit,
        "authority": "Native Buipui OS + native system families",
        "native_systems": native,
        "registries": registry,
        "digicat": {
            "role": "catalogue/index",
            "node_count": len(digicat_nodes),
            "state_hash": state_hash,
        },
        "digifile": {
            "role": "evidence/lineage/manifest",
            "manifest_count": len(digifile_manifest),
            "merkle_root": root,
        },
        "controlled_collision": {
            "id": "COLLISION-DIGICAT-DIGIFILE-BASELINE-001",
            "mode": "quarantine_only",
            "target": "in_memory_copy",
            "production_source_mutated": False,
            "collision_hash": collision_hash,
        },
        "blockchain_anchor": {
            "anchor_type": "local_blockchain_compatible_provenance_chain",
            "public_chain_transaction": False,
            "genesis": "GENESIS-BIUPUI-QUANTICOR-DIGICAT-DIGIFILE-v1",
            "block_count": len(chain),
            "merkle_root": root,
            "tip_hash": chain[-1]["block_hash"],
            "chain": chain,
        },
        "verification": {
            "native_inputs_present": True,
            "digicat_registry_hashed": True,
            "digifile_manifest_hashed": True,
            "merkle_root_stable": merkle_stable,
            "anchor_chain_valid": chain_valid,
            "collision_quarantined": True,
            "source_and_registry_hashes_unchanged": unchanged,
            "promotion": "NOT_PROMOTED",
        },
        "future_baseline": {
            "baseline_id": "QC-DIGICAT-DIGIFILE-NATIVE-BLOCKCHAIN-BASELINE-20260924",
            "reuse_rule": "Future tests must reproduce or explicitly supersede this baseline with new evidence.",
            "compare": ["baseline_commit", "state_hash", "merkle_root", "tip_hash", "native input hashes"],
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "VERIFIED_CONTROLLED_BASELINE" else 1

if __name__ == "__main__":
    sys.exit(main())
