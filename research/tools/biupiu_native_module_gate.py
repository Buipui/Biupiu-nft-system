#!/usr/bin/env python3
import json, os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAMILIES = [
    "mini-os",
    "apps/android",
    "mini-os/android",
    "smart-farming/android",
    "software/rnd-os-mobile",
    "apps/windows",
]
REQUIRED_ROLES = ["DigiCat", "DigiFile", "Learning"]

def exists(rel):
    return (ROOT / rel).exists()

def files_under(rel):
    p = ROOT / rel
    return [x for x in p.rglob("*") if x.is_file()] if p.exists() else []

def find_tokens(rel, tokens):
    out = {t: [] for t in tokens}
    for f in files_under(rel):
        if f.suffix.lower() not in {".kt",".kts",".java",".cpp",".h",".hpp",".rs",".py",".json",".md",".yml",".yaml",".gradle",".xml"}:
            continue
        try:
            s = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for t in tokens:
            if re.search(re.escape(t), s, re.I):
                out[t].append(str(f.relative_to(ROOT)).replace("\\","/"))
    return out

def family_audit(rel):
    fs = files_under(rel)
    tokens = find_tokens(rel, REQUIRED_ROLES + ["NetworkTransport","ExternalTransportAdapter","CMakeLists.txt","settings.gradle","build.gradle"])
    return {
        "family": rel,
        "present": (ROOT / rel).exists(),
        "file_count": len(fs),
        "roles": {k: bool(v) for k,v in tokens.items() if k in REQUIRED_ROLES},
        "role_evidence": {k:v[:8] for k,v in tokens.items() if k in REQUIRED_ROLES},
        "module_signals": {k:v[:8] for k,v in tokens.items() if k not in REQUIRED_ROLES},
    }

def main():
    result = {
        "schema": "biupiu.native-module-gate.v1",
        "status": "SOURCE_GATE",
        "repository": "Buipui/Biupiu-nft-system",
        "scope": FAMILIES,
        "authority": {
            "source_code": "executable_truth",
            "computational_geometry": "relationship_proposal",
            "regression": "acceptance_gate",
            "digicat": "catalogue",
            "digifile": "evidence",
            "learning": "governed_learning",
            "quanticor": "controlled_intersection_referee",
        },
        "families": [family_audit(x) for x in FAMILIES],
        "adapter_check": {
            "network_transport": exists("mini-os/android/app/src/main/java/com/biupui/minios/federation/NetworkTransport.java"),
            "external_transport_adapter": exists("mini-os/android/app/src/main/java/com/biupui/minios/federation/ExternalTransportAdapter.java"),
            "okhttp_transport": exists("mini-os/android/app/src/main/java/com/biupui/minios/federation/OkHttpNetworkTransport.java"),
            "stale_root_adapter_path_absent": not exists("mini-os/android/federation/ExternalTransportAdapter.java"),
        },
        "native_build_check": {
            "apps_android_cmake": exists("apps/android/app/CMakeLists.txt"),
            "scientific_bridge": exists("apps/android/app/src/main/cpp/scientific_android_bridge.cpp"),
            "mini_os_rust_manifest": exists("mini-os/rust/Cargo.toml"),
            "mini_os_rust_source": exists("mini-os/rust/src/lib.rs"),
        },
        "promotion_allowed": False,
    }
    result["open_gate"] = [
        "build/test evidence must execute on CI",
        "device/runtime evidence remains separate",
        "family-level DigiCat/DigiFile/Learning mappings require explicit canonical interface records",
        "no physical quantum or photonic capability is inferred from research-only material",
    ]
    out = ROOT / "research/evidence/BIUPIU-NATIVE-MODULE-GATE-20260924.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
