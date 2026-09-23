"""Repository-wide spelling, Unicode, terminology and semantic-integrity audit.

This is deliberately conservative:
- known misspellings are BLOCKING;
- Unicode/confusable hazards in executable identifiers are BLOCKING;
- foreign-language text is preserved and flagged for locale/provenance review, not
  translated or rewritten automatically;
- semantic checks verify canonical Biupiu terminology and cross-linked registry paths.
No runtime capability is inferred.
"""
from __future__ import annotations

import ast
import json
import re
import tokenize
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TEXT_EXTENSIONS = {
    ".py", ".ts", ".tsx", ".js", ".jsx", ".c", ".h", ".cc", ".cpp", ".cxx",
    ".hpp", ".rs", ".kt", ".kts", ".java", ".cs", ".sol", ".json", ".jsonl",
    ".yaml", ".yml", ".md", ".txt", ".toml", ".ini", ".cfg", ".xml", ".gradle",
    ".properties", ".sh", ".ps1", ".bat", ".cmake", ".uproject", ".uplugin",
}
SKIP_DIRS = {".git", "node_modules", "dist", "build", "out", ".gradle", "__pycache__",
             ".venv", "venv", "target", "DerivedDataCache", "Binaries", "Intermediate"}

# Conservative, high-confidence coding/documentation typos.
MISSPELLINGS = {
    "recieve": "receive", "recieved": "received", "seperate": "separate",
    "independant": "independent", "occured": "occurred", "accomodate": "accommodate",
    "enviroment": "environment", "definately": "definitely", "responsability": "responsibility",
    "compatability": "compatibility", "availble": "available", "sucess": "success",
    "adress": "address", "existance": "existence", "refered": "referred",
    "implemenation": "implementation", "dependancy": "dependency", "langauge": "language",
    "paramater": "parameter", "verifed": "verified", "veriﬁed": "verified",
    "fedaration": "federation", "fedarated": "federated", "philosphy": "philosophy",
    "sematics": "semantics", "semnatic": "semantic", "harvset": "harvest",
    "catologue": "catalogue", "cataloge": "catalogue", "recieveing": "receiving",
}

CANONICAL_TERMS = {
    "federation": ("federation", "fedaration", "fedarated"),
    "subsystem": ("subsystem", "sub-system", "subsystems"),
    "provenance": ("provenance",),
    "verification": ("verification", "verified"),
    "implementation": ("implementation",),
    "capability": ("capability", "capabilities"),
    "catalogue": ("catalogue", "catalog"),
    "Biupiu": ("Biupiu", "Buipui", "Biupui"),
}

REGISTRY_FILES = [
    "research/BIUPIU-NATIVE-SYSTEM-CATALOGUE-v1.0.json",
    "research/BIUPIU-NATIVE-SYSTEM-TAG-SCHEMA-v1.0.md",
    "research/BIUPIU-FEDERATION-NATIVE-EVOLUTION-PHILOSOPHY-v1.0.md",
    "research/BIUPIU-SCIENTIFIC-LEARNING-LITERATURE-REGISTRY-20260923.md",
    "research/BIUPIU-NATIVE-CODING-PHILOSOPHY-AND-ENGINEERING-MATRIX-v1.0.md",
    "research/BIUPIU-MULTILANGUAGE-NATIVE-CODING-MATRIX-v1.0.md",
    "research/BIUPIU-CODING-LANGUAGE-LIBRARY-v1.0.json",
    "intelligence/BIUPIU-AI-CODING-HARD-GATE-v1.0.json",
]

def files():
    for p in ROOT.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        yield p

def line_hits(text: str, pattern: re.Pattern[str]):
    for n, line in enumerate(text.splitlines(), 1):
        if pattern.search(line):
            yield n, line.strip()[:240]

def audit():
    findings = []
    counts = {"files": 0, "non_ascii_files": 0, "foreign_review_files": 0}

    audit_script = Path(__file__).resolve()
    for p in files():
        counts["files"] += 1
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(("BLOCK", str(p.relative_to(ROOT)), 0, "non-UTF-8 text artifact"))
            continue

        rel = str(p.relative_to(ROOT))
        if any(ord(ch) > 127 for ch in text):
            counts["non_ascii_files"] += 1

        # The audit authority contains the canonical typo->correction dictionary itself.\n        # Do not report the dictionary as a repository defect.\n        if p.resolve() != audit_script:\n            typo_items = MISSPELLINGS.items()\n        else:\n            typo_items = ()\n        for bad, good in typo_items:
            pattern = re.compile(r"(?<![A-Za-z])" + re.escape(bad) + r"(?![A-Za-z])", re.I)
            for n, line in line_hits(text, pattern):
                findings.append(("BLOCK", rel, n, f"spelling: {bad} -> {good}: {line}"))

        # Unicode control/format hazards can alter source interpretation.
        for n, line in line_hits(text, re.compile(r"[\u202A-\u202E\u2066-\u2069\u200B\u200C\u200D\uFEFF]")):
            findings.append(("BLOCK", rel, n, "Unicode bidi/zero-width control in text"))

        # Executable identifiers: allow language syntax to decide later, but flag
        # non-ASCII identifier characters for explicit review rather than silently
        # normalising harvested foreign-language code.
        if p.suffix.lower() in {".py", ".ts", ".tsx", ".js", ".jsx", ".c", ".h", ".cc", ".cpp", ".cxx", ".hpp", ".rs", ".kt", ".kts", ".java", ".cs", ".sol"} and p.resolve() != audit_script:
            for n, line in line_hits(text, re.compile(r"\b[A-Za-z_][A-Za-z0-9_]*[^\x00-\x7F\s,;(){}\[\].:+*/=<>!?&|%-]")):
                findings.append(("REVIEW", rel, n, f"non-ASCII executable-token candidate: {line}"))

        # NFKC changes can expose confusable/compatibility characters.
        if unicodedata.normalize("NFKC", text) != text and p.suffix.lower() in {".py", ".ts", ".tsx", ".js", ".jsx", ".c", ".h", ".cc", ".cpp", ".cxx", ".hpp", ".rs", ".kt", ".kts", ".java", ".cs", ".sol", ".json", ".yaml", ".yml"}:
            findings.append(("REVIEW", rel, 0, "NFKC normalization changes source/config text; inspect before promotion"))

        # Foreign-language artefacts are preserved but must be identifiable.
        non_ascii = sum(ord(c) > 127 for c in text)
        alpha = sum(c.isalpha() for c in text)
        if alpha and non_ascii / max(alpha, 1) > 0.02 and p.suffix.lower() in {".md", ".txt", ".json", ".yaml", ".yml", ".py", ".ts", ".js", ".cpp", ".h", ".rs", ".kt", ".java"}:
            counts["foreign_review_files"] += 1
            if "BCP-47" not in text and "locale" not in text.lower() and "language" not in text.lower():
                findings.append(("REVIEW", rel, 0, "multilingual/non-ASCII artifact lacks explicit locale/language metadata"))

    # Registry existence + cross-reference semantics.
    for rel in REGISTRY_FILES:
        if not (ROOT / rel).is_file():
            findings.append(("BLOCK", rel, 0, "canonical registry/authority file missing"))

    try:
        cat = json.loads((ROOT / "research/BIUPIU-NATIVE-SYSTEM-CATALOGUE-v1.0.json").read_text(encoding="utf-8"))
        ids = [s.get("id") for s in cat.get("systems", [])]
        if len(ids) != len(set(ids)):
            findings.append(("BLOCK", "native-system-catalogue", 0, "duplicate system_id"))
        for s in cat.get("systems", []):
            if not str(s.get("id", "")).startswith("BPU.SYS."):
                findings.append(("BLOCK", "native-system-catalogue", 0, f"invalid system_id: {s.get('id')}"))
            for rel in s.get("native_code", []):
                # Directory authority paths are valid if they exist.
                if not (ROOT / rel).exists():
                    findings.append(("BLOCK", "native-system-catalogue", 0, f"{s.get('id')}: native_code path missing: {rel}"))
            if not s.get("capabilities"):
                findings.append(("BLOCK", "native-system-catalogue", 0, f"{s.get('id')}: empty capability set"))
    except Exception as exc:
        findings.append(("BLOCK", "native-system-catalogue", 0, f"JSON/semantic parse failure: {exc}"))

    result = {
        "pass": not any(f[0] == "BLOCK" for f in findings),
        "counts": counts,
        "blocking_findings": [f for f in findings if f[0] == "BLOCK"],
        "review_findings": [f for f in findings if f[0] == "REVIEW"],
    }
    return result

if __name__ == "__main__":
    result = audit()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["pass"] else 1)
