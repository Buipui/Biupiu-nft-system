#!/usr/bin/env python3
"""Non-destructive Biupiu repository housekeeping/exterminate runner."""

from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKIP = {".git", ".gradle", "node_modules", "build", "dist", "vendor"}
TEXT_EXT = {".md", ".json", ".py", ".js", ".ts", ".tsx", ".kt", ".kts", ".sol", ".yml", ".yaml"}

def files():
    for p in ROOT.rglob("*"):
        if not p.is_file() or any(part in SKIP for part in p.parts):
            continue
        yield p

def json_check(p, findings):
    try:
        json.loads(p.read_text(encoding="utf-8"))
    except Exception as exc:
        findings.append(f"JSON_INVALID {p.relative_to(ROOT)}: {exc}")

def duplicate_hashes(findings):
    seen = {}
    for p in files():
        if p.suffix.lower() not in TEXT_EXT:
            continue
        try:
            digest = hashlib.sha256(p.read_bytes()).hexdigest()
        except OSError:
            continue
        seen.setdefault(digest, []).append(p)
    for digest, paths in seen.items():
        if len(paths) > 1:
            findings.append("DUPLICATE_CONTENT " + digest[:16] + " :: " +
                            " | ".join(str(x.relative_to(ROOT)) for x in paths))

def scan(findings):
    for p in files():
        if p.suffix.lower() == ".json":
            json_check(p, findings)
        if p.suffix.lower() in TEXT_EXT:
            try:
                text = p.read_text(encoding="utf-8")
            except Exception:
                continue
            if re.search(r"(?i)(api[_-]?key|secret|private[_-]?key|password)\s*[:=]\s*['\"][^'\"]{8,}", text):
                findings.append(f"POSSIBLE_SECRET {p.relative_to(ROOT)}")
            if re.search(r"(?i)TODO|FIXME", text) and "vendor" not in p.parts:
                findings.append(f"TODO_OR_FIXME {p.relative_to(ROOT)}")
    duplicate_hashes(findings)

def main():
    findings = []
    scan(findings)
    print("# BIUPIU EXTERMINATE REPORT")
    print(f"root={ROOT}")
    print(f"findings={len(findings)}")
    for item in findings:
        print(item)
    print("NON_DESTRUCTIVE=true")
    print("No files were deleted or rewritten by this runner.")

if __name__ == "__main__":
    main()
