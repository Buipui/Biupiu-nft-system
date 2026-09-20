"""AI-67 integrity smoke test."""
import importlib.util
from pathlib import Path
I=Path(__file__).resolve().parents[1]/"intelligence"
s=importlib.util.spec_from_file_location("v",I/"BIUPIU-AI67-CANONICAL-INTEGRITY-VALIDATOR.py"); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
def run():
 r=m.validate()
 return {"valid":r["status"] in ("CLEAN","BLOCKED"),"chain_complete":r["chain_complete"],"authorities_unique":r["unique_authorities"]}
if __name__=="__main__":
 r=run(); print(r); raise SystemExit(0 if all(r.values()) else 1)
