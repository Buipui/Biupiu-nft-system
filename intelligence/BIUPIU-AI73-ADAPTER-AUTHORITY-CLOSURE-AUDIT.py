"""AI-73 adapter-to-authority contract closure audit.
Static inspection only. No runtime compatibility is inferred.
"""
import ast,json
from pathlib import Path
I=Path(__file__).resolve().parents[1]/"intelligence"
MAP={
"BIUPIU-EVIDENCE-INTERFACE-v1.py":"BIUPIU-AI44-REAL-EVIDENCE-GATE.py",
"BIUPIU-STATE-INTERFACE-v1.py":"BIUPIU-AI53-GATE-STATE-MACHINE.py",
"BIUPIU-RELEASE-INTERFACE-v1.py":"BIUPIU-AI49-CANONICAL-TASK-RELEASE-CONTROLLER.py",
"BIUPIU-VALIDATION-INTERFACE-v1.py":"BIUPIU-AI49-CANONICAL-TASK-RELEASE-CONTROLLER.py",
"BIUPIU-REGRESSION-INTERFACE-v1.py":"BIUPIU-AI46-UNIFIED-REGRESSION-INDEX-CONTROLLER.py"}
def symbols(p):
 try:
  t=ast.parse(p.read_text()); out=[]
  for n in ast.walk(t):
   if isinstance(n,ast.ImportFrom): out += [x.name for x in n.names]
  return sorted(set(out))
 except Exception:return []
def run():
 rows=[]
 for adapter,target in MAP.items():
  p=I/"adapters"/adapter; t=I/target
  rows.append({"adapter":adapter,"target":target,"adapter_exists":p.exists(),"target_exists":t.exists(),
               "adapter_imports":symbols(p) if p.exists() else [],
               "classification":"STATIC-PRESENT" if p.exists() and t.exists() else "BLOCKED"})
 return {"gate":"AI-73","adapters":rows,"runtime_contract_verified":False,
         "status":"STATIC-CONTRACT-CLOSURE","promotion_allowed":False}
if __name__=="__main__": print(json.dumps(run(),indent=2,sort_keys=True))
