"""Repository-wide native semantic/code governance audit.

The audit checks syntax and mandatory governance contracts. It is intentionally
source-level: passing this script does not claim runtime/device/hardware proof.
"""
from __future__ import annotations
import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NATIVE_ROOTS = (
    ROOT / "software/rnd-os-ai",
    ROOT / "packages/biupiu-rnd-os",
    ROOT / "intelligence",
    ROOT / "core/multilang",
    ROOT / "simulators",
    ROOT / "smart-farming",
    ROOT / "apps/shared",
)
REQUIRED_FILES = (
    ROOT / "research/BIUPIU-NATIVE-CODING-PHILOSOPHY-AND-ENGINEERING-MATRIX-v1.0.md",
    ROOT / "research/BIUPIU-MULTILANGUAGE-NATIVE-CODING-MATRIX-v1.0.md",
    ROOT / "intelligence/BIUPIU-AI-CODING-HARD-GATE-v1.0.json",
    ROOT / "intelligence/BIUPIU-AI-CODING-HARD-GATE.py",
    ROOT / "intelligence/BIUPIU-BLOCKCHAIN-ANCHOR-BOUNDARY.py",
    ROOT / "software/rnd-os-ai/src/biupiu_ai/learning.py",
)
REQUIRED_TOKENS = {
    "software/rnd-os-ai/src/biupiu_ai/guided_fault_finding.py": (
        "promotion_allowed", "requires_os_validation", "evidence_refs"
    ),
    "software/rnd-os-ai/src/biupiu_ai/learning_federation_bridge.py": (
        "provenance_hash", "ADAPTATION_PROPOSAL", "append"
    ),
    "software/rnd-os-ai/src/biupiu_ai/federation_protocol.py": (
        "gate_passes", "federation_ready", "VERIFIED"
    ),
    "packages/biupiu-rnd-os/src/guided-fault-finder.ts": (
        "QUARANTINED", "stopConditions", "evidenceRefs"
    ),
    "packages/biupiu-rnd-os/src/federation-contracts.ts": (
        "schemaVersion", "provenance", "correlation"
    ),
    "intelligence/BIUPIU-BLOCKCHAIN-ANCHOR-BOUNDARY.py": (
        "merkle_root", "promotion_ready", "inclusion_proof"
    ),
}

def _python_files() -> list[Path]:
    return sorted({
        p for root in NATIVE_ROOTS if root.is_dir() for p in root.rglob("*.py")
        if ".git" not in p.parts and "__pycache__" not in p.parts
    })

def _ts_files() -> list[Path]:
    root = ROOT / "packages/biupiu-rnd-os/src"
    return sorted(root.rglob("*.ts")) if root.is_dir() else []

def run() -> dict:
    results = []
    for p in REQUIRED_FILES:
        results.append(("required-file", str(p.relative_to(ROOT)), "PASS" if p.is_file() else "FAIL"))

    for rel, tokens in REQUIRED_TOKENS.items():
        p = ROOT / rel
        if not p.is_file():
            results.append(("contract", rel, "FAIL", "missing"))
            continue
        s = p.read_text(encoding="utf-8")
        missing = [t for t in tokens if t not in s]
        if p.suffix == ".py":
            try:
                ast.parse(s, filename=str(p))
            except SyntaxError as exc:
                missing.append("SYNTAX:" + str(exc))
        results.append(("contract", rel, "PASS" if not missing else "FAIL", missing))

    syntax_failures = []
    for p in _python_files():
        try:
            ast.parse(p.read_text(encoding="utf-8"), filename=str(p))
        except SyntaxError as exc:
            syntax_failures.append(f"{p.relative_to(ROOT)}: {exc}")
    results.append(("python-syntax", "native-roots", "PASS" if not syntax_failures else "FAIL", syntax_failures))

    # TypeScript source is checked for obvious forbidden authoritative shortcuts.
    ts_failures = []
    forbidden = ("eval(", "new Function(")
    for p in _ts_files():
        s = p.read_text(encoding="utf-8")
        for token in forbidden:
            if token in s:
                ts_failures.append(f"{p.relative_to(ROOT)}: forbidden {token}")
    results.append(("typescript-safety", "packages/biupiu-rnd-os/src", "PASS" if not ts_failures else "FAIL", ts_failures))

    try:
        manifest = json.loads((ROOT / "intelligence/BIUPIU-AI-CODING-HARD-GATE-v1.0.json").read_text(encoding="utf-8"))
        pipeline = manifest.get("pipeline", [])
        gate_ok = manifest.get("fail_closed") is True and len(pipeline) >= 10
    except Exception as exc:
        gate_ok = False
        results.append(("ai-hard-gate", "manifest", "FAIL", str(exc)))
    else:
        results.append(("ai-hard-gate", "manifest", "PASS" if gate_ok else "FAIL"))

    return {"pass": all(r[2] == "PASS" for r in results), "results": results}

if __name__ == "__main__":
    report = run()
    for row in report["results"]:
        print(" | ".join(map(str, row)))
    raise SystemExit(0 if report["pass"] else 1)
