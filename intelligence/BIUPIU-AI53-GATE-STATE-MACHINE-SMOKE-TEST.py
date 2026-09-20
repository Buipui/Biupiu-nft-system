"""AI-53 state-machine smoke test."""
from __future__ import annotations
import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("sm","intelligence/BIUPIU-AI53-GATE-STATE-MACHINE.py")
m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
def run():
    checks={}
    valid=["DISCOVERED","ASSIGNED","EXECUTING","CHALLENGED","VALIDATED","REGRESSION_PASS","PROMOTION_READY","PROMOTED"]
    checks["valid_path"]=m.validate_path(valid)
    checks["forged_discovered_promoted"]=not m.allowed("DISCOVERED","PROMOTED")
    checks["forged_validated_promoted"]=not m.allowed("VALIDATED","PROMOTED")
    checks["promoted_terminal"]=not m.allowed("PROMOTED","EXECUTING")
    checks["remediation_recovery"]=m.allowed("REMEDIATION_REQUIRED","EXECUTING")
    checks["runtime_recovery"]=m.allowed("PENDING_RUNTIME","EXECUTING")
    checks["blocked_untrusted_cannot_promote"]=not m.allowed("BLOCKED_UNTRUSTED_EVIDENCE","PROMOTED")
    return checks
if __name__=="__main__":
    r=run(); print(r); raise SystemExit(0 if all(r.values()) else 1)
