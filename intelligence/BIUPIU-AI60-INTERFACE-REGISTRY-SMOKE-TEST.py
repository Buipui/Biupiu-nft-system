"""AI-60 registry smoke test."""
import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("v",ROOT/"intelligence/BIUPIU-AI60-INTERFACE-REGISTRY-VALIDATOR.py"); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
def run():
 r=m.validate()
 return {"registry_valid":r["status"]=="CLEAN","no_missing":not r["missing"],"no_extra":not r["extra"],"no_malformed":not r["malformed"]}
if __name__=="__main__":
 r=run(); print(r); raise SystemExit(0 if all(r.values()) else 1)
