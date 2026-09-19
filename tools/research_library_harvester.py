"""Biupiu Research Library Harvester v1.0.
Policy-safe metadata/download framework. Downloads are permitted only when a
source explicitly provides an open-access file and licence conditions allow it.
Never bypass paywalls, logins, robots restrictions, or access controls.
"""
from pathlib import Path
import json

def load_manifest(path="library/research/2026-09-19-harvest-v1.0.json"):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def download_policy(record):
    if record.get("source") == "Popular Mechanics":
        return "metadata-only"
    if record.get("open_access") is True:
        return "eligible-after-direct-file-and-licence-check"
    return "metadata-only"

if __name__ == "__main__":
    for r in load_manifest()["records"]:
        print(r["id"], download_policy(r))
