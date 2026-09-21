"""AI-73 adapter closure smoke test."""
from pathlib import Path
p=Path(__file__).resolve().parent/"BIUPIU-AI73-ADAPTER-AUTHORITY-CLOSURE-AUDIT.py"
assert p.exists()
s=p.read_text()
assert '"runtime_contract_verified":False' in s
assert '"promotion_allowed":False' in s
print({"gate":"AI-73","smoke_test":"PASS","runtime_contract":"UNVERIFIED","barrier":"ACTIVE"})
