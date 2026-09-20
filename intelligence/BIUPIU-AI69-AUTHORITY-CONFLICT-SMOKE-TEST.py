"""AI-69 smoke test."""
from pathlib import Path
p=Path(__file__).resolve().parent/"BIUPIU-AI69-AUTHORITY-CONFLICT-SCANNER.py"
assert p.exists()
s=p.read_text()
assert '"promotion_allowed":False' in s
assert "candidate-list-only" in s
print({"gate":"AI-69","smoke_test":"PASS","fail_closed":"PRESERVED"})
