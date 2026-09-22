"""Repository-wide native semantic/code governance audit.

Source-level audit only: passing this script does not claim build, runtime,
device, hardware or HIL verification. The audit is intentionally language-
agnostic at the inventory layer and adds focused semantic checks for the
native language families used by Biupiu.
"""
from __future__ import annotations

import ast
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NATIVE_EXTENSIONS = {
    ".py": "python",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".js": "javascript",
    ".jsx": "javascript",
    ".rs": "rust",
    ".c": "c",
    ".h": "c",
    ".cc": "cpp",
    ".cpp": "cpp",
    ".cxx": "cpp",
    ".hpp": "cpp",
    ".hh": "cpp",
    ".kt": "kotlin",
    ".kts": "kotlin",
    ".java": "java",
    ".cs": "csharp",
    ".swift": "swift",
}

EXCLUDED_PARTS = {
    ".git", "node_modules", "dist", "build", "target", "__pycache__",
    ".gradle", "vendor", "third_party",
}

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

def _source_files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*")
        if p.is_file()
        and p.suffix.lower() in NATIVE_EXTENSIONS
        and not any(part in EXCLUDED_PARTS for part in p.parts)
    )

def _python_files() -> list[Path]:
    return [p for p in _source_files() if p.suffix == ".py"]

def _ts_files() -> list[Path]:
    return [p for p in _source_files() if p.suffix in {".ts", ".tsx"}]

def _rust_safety_findings() -> list[str]:
    findings = []
    for p in _source_files():
        if p.suffix != ".rs":
            continue
        lines = p.read_text(encoding="utf-8").splitlines()
        for i, line in enumerate(lines):
            if re.search(r"\bunsafe\s*\{", line):
                context = "\n".join(lines[max(0, i - 5):i])
                if "SAFETY:" not in context:
                    findings.append(
                        f"{p.relative_to(ROOT)}:{i + 1}: unsafe block lacks nearby SAFETY comment"
                    )
    return findings

def _language_inventory() -> dict[str, int]:
    inventory: dict[str, int] = {}
    for p in _source_files():
        language = NATIVE_EXTENSIONS[p.suffix.lower()]
        inventory[language] = inventory.get(language, 0) + 1
    return dict(sorted(inventory.items()))

def run() -> dict:
    results = []

    for p in REQUIRED_FILES:
        results.append(
            ("required-file", str(p.relative_to(ROOT)),
             "PASS" if p.is_file() else "FAIL")
        )

    for rel, tokens in REQUIRED_TOKENS.items():
        p = ROOT / rel
        if not p.is_file():
            results.append(("contract", rel, "FAIL", "missing"))
            continue
        source = p.read_text(encoding="utf-8")
        missing = [t for t in tokens if t not in source]
        if p.suffix == ".py":
            try:
                ast.parse(source, filename=str(p))
            except SyntaxError as exc:
                missing.append("SYNTAX:" + str(exc))
        results.append(("contract", rel, "PASS" if not missing else "FAIL", missing))

    syntax_failures = []
    for p in _python_files():
        try:
            ast.parse(p.read_text(encoding="utf-8"), filename=str(p))
        except SyntaxError as exc:
            syntax_failures.append(f"{p.relative_to(ROOT)}: {exc}")
    results.append(
        ("python-syntax", "repository-native-sources",
         "PASS" if not syntax_failures else "FAIL", syntax_failures)
    )

    ts_failures = []
    for p in _ts_files():
        source = p.read_text(encoding="utf-8")
        for token in ("eval(", "new Function("):
            if token in source:
                ts_failures.append(f"{p.relative_to(ROOT)}: forbidden {token}")
    results.append(
        ("typescript-safety", "repository-native-sources",
         "PASS" if not ts_failures else "FAIL", ts_failures)
    )

    rust_safety = _rust_safety_findings()
    results.append(
        ("rust-safety-comments", "repository-native-sources",
         "PASS" if not rust_safety else "FAIL", rust_safety)
    )

    inventory = _language_inventory()
    expected_languages = {
        "c", "cpp", "rust", "python", "typescript", "javascript",
        "kotlin", "java", "csharp",
    }
    missing_languages = sorted(expected_languages - set(inventory))
    results.append(
        ("language-coverage", "native-extension-inventory",
         "PASS" if not missing_languages else "FAIL",
         {"inventory": inventory, "missing_expected": missing_languages})
    )

    try:
        manifest = json.loads(
            (ROOT / "intelligence/BIUPIU-AI-CODING-HARD-GATE-v1.0.json")
            .read_text(encoding="utf-8")
        )
        pipeline = manifest.get("pipeline", [])
        gate_ok = manifest.get("fail_closed") is True and len(pipeline) >= 10
    except Exception as exc:
        gate_ok = False
        results.append(("ai-hard-gate", "manifest", "FAIL", str(exc)))
    else:
        results.append(
            ("ai-hard-gate", "manifest", "PASS" if gate_ok else "FAIL")
        )

    return {
        "pass": all(row[2] == "PASS" for row in results),
        "inventory": inventory,
        "results": results,
    }

if __name__ == "__main__":
    report = run()
    print("NATIVE_LANGUAGE_INVENTORY", report["inventory"])
    for row in report["results"]:
        print(" | ".join(map(str, row)))
    raise SystemExit(0 if report["pass"] else 1)
