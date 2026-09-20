"""AI-61 readiness verifier smoke test."""
import importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("v",ROOT/"intelligence/BIUPIU-AI61-ADAPTER-READINESS-VERIFIER.py"); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
def run():
 r=m.verify()
 return {"valid_status":r["status"] in ("CLEAN","BLOCKED"),"matrix_complete":len(r["matrix"])==19,"blocked_is_fail_closed":(r["status"]=="CLEAN" or bool(r["blocked"]))}
if __name__=="__main__":
 r=run(); print(r); raise SystemExit(0 if all(r.values()) else 1)
