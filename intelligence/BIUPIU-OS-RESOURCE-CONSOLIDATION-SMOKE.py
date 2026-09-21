import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = ROOT / "research/BIUPIU-OS-RESOURCE-CONSOLIDATION-GATE-29.json"

def main():
    data = json.loads(manifest.read_text(encoding="utf-8"))
    assert data["gate"] == "29"
    assert data["status"] == "IMPLEMENTED"
    for path in data["canonical_paths"]:
        assert (ROOT / path).exists(), path
    assert "extend-existing-contracts-first" in data["rules"]
    assert "no-parallel-authorities" in data["rules"]
    print("BIUPIU OS resource consolidation smoke: PASS")

if __name__ == "__main__":
    main()
