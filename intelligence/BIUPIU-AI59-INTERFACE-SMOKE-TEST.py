"""AI-59 interface validator smoke test."""
from pathlib import Path
import importlib.util
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("v",ROOT/"intelligence/BIUPIU-AI59-INTERFACE-CONTRACT-VALIDATOR.py"); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
def run():
 r=m.validate()
 # The validator may legitimately BLOCK on unimplemented interfaces; it must never crash.
 return {"status_valid":r["status"] in ("CLEAN","BLOCKED"),"checked_domains":r["checked_domains"]==12,"findings_structured":all({"domain","interface","reason"}<=set(x) for x in r["findings"])}
if __name__=="__main__":
 r=run(); print(r); raise SystemExit(0 if all(r.values()) else 1)
