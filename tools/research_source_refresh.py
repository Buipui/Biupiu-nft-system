"""Biupiu Research Library Gate 2 refresh scaffold.

Uses public scholarly metadata endpoints only. Full-text download is deliberately
left behind an explicit licence/file verification step.
"""
from datetime import datetime, timezone
import json
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

MANIFEST = Path("library/research/2026-09-19-harvest-v1.0.json")
OUT = Path("library/research/source-refresh-log.json")


def crossref_doi(doi: str):
    url = "https://api.crossref.org/works/" + quote(doi, safe="")
    req = Request(url, headers={"User-Agent": "BiupiuResearchLibrary/1.0"})
    with urlopen(req, timeout=20) as response:
        return json.load(response)["message"]


def refresh():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    results = []
    for record in data["records"]:
        doi = record.get("doi")
        if not doi:
            results.append({"id": record["id"], "status": "no-doi-metadata-refresh", "url": record.get("url")})
            continue
        try:
            meta = crossref_doi(doi)
            results.append({
                "id": record["id"],
                "doi": doi,
                "status": "metadata-verified",
                "title": meta.get("title", [None])[0],
                "publisher": meta.get("publisher"),
                "published": meta.get("published-print") or meta.get("published-online") or meta.get("published"),
                "license": meta.get("license", []),
                "retrieved_utc": datetime.now(timezone.utc).isoformat()
            })
        except Exception as exc:
            results.append({"id": record["id"], "doi": doi, "status": "refresh-error", "error": str(exc)})
    OUT.write_text(json.dumps({"version":"1.0","generated_utc":datetime.now(timezone.utc).isoformat(),"records":results}, indent=2), encoding="utf-8")


if __name__ == "__main__":
    refresh()
