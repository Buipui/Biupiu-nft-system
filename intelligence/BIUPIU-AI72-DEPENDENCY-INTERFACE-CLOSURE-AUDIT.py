"""AI-72 dependency/interface closure audit.
Static AST/text inspection only; no arbitrary execution or promotion.
"""
import ast,json
from pathlib import Path
I=Path(__file__).resolve().parents[1]/"intelligence"
TARGETS={
"AI44":"BIUPIU-AI44-REAL-EVIDENCE-GATE.py","AI46":"BIUPIU-AI46-UNIFIED-REGRESSION-INDEX-CONTROLLER.py",
"AI47":"BIUPIU-AI47-GOVERNED-TASK-ROUTER.py","AI48":"BIUPIU-AI48-TASK-TO-RELEASE-CONTROLLER.py",
"AI49":"BIUPIU-AI49-CANONICAL-TASK-RELEASE-CONTROLLER.py","AI53":"BIUPIU-AI53-GATE-STATE-MACHINE.py",
"AI65":"BIUPIU-GOVERNANCE-KERNEL-AI56.py"}
def imports(path):
 try:
  t=ast.parse(path.read_text())
  return sorted({n.module or n.names[0].name for n in ast.walk(t) if isinstance(n,ast.ImportFrom) and n.module})
 except Exception:return []
def run():
 rows=[]
 for k,f in TARGETS.items():
  p=I/f; rows.append({"authority":k,"file":f,"exists":p.exists(),"imports":imports(p) if p.exists() else [],"closure":"PRESENT" if p.exists() else "MISSING"})
 return {"gate":"AI-72","authorities":rows,"missing":[x["authority"] for x in rows if not x["exists"]],
 "status":"STATIC-CLOSURE-CHECK","promotion_allowed":False,
 "runtime_execution":"NOT_CLAIMED"}
if __name__=="__main__": print(json.dumps(run(),indent=2,sort_keys=True))
