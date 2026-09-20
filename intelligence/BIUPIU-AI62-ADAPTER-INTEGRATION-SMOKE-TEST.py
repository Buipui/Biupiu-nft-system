"""AI-62 canonical adapter integration smoke test."""
from pathlib import Path
import importlib.util
ROOT=Path(__file__).resolve().parents[1]; A=ROOT/"intelligence/adapters"
FILES=["BIUPIU-EVIDENCE-INTERFACE-v1.py","BIUPIU-STATE-INTERFACE-v1.py","BIUPIU-RELEASE-INTERFACE-v1.py","BIUPIU-VALIDATION-INTERFACE-v1.py","BIUPIU-REGRESSION-INTERFACE-v1.py"]
def load(p):
 s=importlib.util.spec_from_file_location(p.stem,p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def run():
 rows=[]
 for n in FILES:
  p=A/n; m=load(p); rows.append((n,p.is_file(),isinstance(m.CONTRACT,list),callable(m.handle)))
 return {"all_present":all(x[1] for x in rows),"all_contracts":all(x[2] for x in rows),"all_handlers":all(x[3] for x in rows),"rows":rows}
if __name__=="__main__":
 r=run(); print(r); raise SystemExit(0 if all(r[k] for k in ("all_present","all_contracts","all_handlers")) else 1)
