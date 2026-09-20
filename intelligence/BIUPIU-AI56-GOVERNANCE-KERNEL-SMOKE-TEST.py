"""AI-56 kernel smoke/exterminate test."""
from pathlib import Path
import importlib.util
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("k",ROOT/"intelligence/BIUPIU-GOVERNANCE-KERNEL-AI56.py")
m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
def run():
 r={}
 x=m.inspect(); r["authority_set"]=all(Path(ROOT/p).exists() for p in m.AUTHORITIES.values())
 r["kernel_clean"]=x["status"]=="CLEAN"
 r["terminal_promoted"]=x["status"]=="CLEAN"
 missing=dict(m.AUTHORITIES); missing["x"]="intelligence/DOES-NOT-EXIST.py"
 original=m.AUTHORITIES.copy(); m.AUTHORITIES=missing
 r["missing_authority_detected"]=m.inspect()["status"]=="BLOCKED"
 m.AUTHORITIES=original
 return r
if __name__=="__main__":
 r=run(); print(r); raise SystemExit(0 if all(r.values()) else 1)
