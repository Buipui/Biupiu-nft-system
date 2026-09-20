"""AI-61 adapter implementation-readiness verifier.

A registered adapter is READY only when an explicit implementation module exists
and exports the declared adapter contract. No name/token matching is accepted.
"""
from __future__ import annotations
import json,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; INT=ROOT/"intelligence"
REG=INT/"BIUPIU-AI60-INTERFACE-REGISTRY.json"
ADAPTER_DIR=INT/"adapters"
def verify():
 data=json.loads(REG.read_text(encoding="utf-8")); rows=[]; blocked=[]
 for iface,spec in data["interfaces"].items():
  module_name=spec["adapter"].lower().replace("-","_")
  path=ADAPTER_DIR/(module_name+".py")
  required=spec["contract"]
  if not path.is_file():
   rows.append({"interface":iface,"adapter":spec["adapter"],"status":"MISSING_IMPLEMENTATION","required":required}); blocked.append(iface); continue
  try:
   s=importlib.util.spec_from_file_location(module_name,path); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
   contract=getattr(m,"CONTRACT",[])
   handler=getattr(m,"handle",None)
   ok=isinstance(contract,list) and set(required)<=set(contract) and callable(handler)
   status="READY" if ok else "CONTRACT_MISMATCH"
  except Exception as e:
   status="LOAD_ERROR"
  rows.append({"interface":iface,"adapter":spec["adapter"],"status":status,"required":required})
  if status!="READY": blocked.append(iface)
 return {"status":"CLEAN" if not blocked else "BLOCKED","ready":len(rows)-len(blocked),"blocked":blocked,"matrix":rows}
if __name__=="__main__":
 print(json.dumps(verify(),indent=2,sort_keys=True))
