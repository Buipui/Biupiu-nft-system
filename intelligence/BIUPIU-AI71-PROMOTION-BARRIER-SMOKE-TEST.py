"""AI-71 promotion-barrier smoke test."""
from pathlib import Path
p=Path(__file__).resolve().parent/"BIUPIU-AI71-GOVERNANCE-CHAIN-AUDIT.py"
assert p.exists()
s=p.read_text()
assert '"promotion_allowed":False' in s
assert '"STATIC_REPOSITORY"' in s
print({"gate":"AI-71","smoke_test":"PASS","barrier":"ACTIVE"})
