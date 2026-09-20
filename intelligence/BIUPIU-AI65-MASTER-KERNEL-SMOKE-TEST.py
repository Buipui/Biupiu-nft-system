"""AI-65 master-kernel smoke/exterminate test."""
import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; P=ROOT/"intelligence/BIUPIU-GOVERNANCE-KERNEL-AI56.py"
s=importlib.util.spec_from_file_location("k",P); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
def run():
 c=m.inspect(); r={}
 r["clean_or_blocked"]=c["status"] in ("CLEAN","BLOCKED")
 r["required_gates_present"]=not any(x[0] in ("MISSING_AUTHORITY","MISSING_GATE_ARTIFACT") for x in c["findings"])
 # Exterminate: inject missing artifact and confirm fail-closed.
 old=m.REGRESSION; m.REGRESSION="DOES-NOT-EXIST.py"
 r["missing_regression_blocks"]=m.inspect()["status"]=="BLOCKED"; m.REGRESSION=old
 return r
if __name__=="__main__":
 r=run(); print(r); raise SystemExit(0 if all(r.values()) else 1)
