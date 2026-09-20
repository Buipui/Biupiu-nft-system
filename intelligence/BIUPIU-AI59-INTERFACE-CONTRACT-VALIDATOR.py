"""AI-59 Interface Contract Validator.

Validates declared interface contracts against repository implementation signals.
This is static repository verification; it does not claim live runtime capability.
"""
from __future__ import annotations
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; INT=ROOT/"intelligence"
MANIFEST=INT/"BIUPIU-AI58-SYSTEM-INTEGRATION-MANIFEST.json"
TOKEN_MAP={
"task":["task","TASK"],"state":["state","STATE"],"provenance":["provenance","PROVENANCE"],
"routing":["routing","route"],"evidence":["evidence","EVIDENCE"],"release":["release","PROMOTION_READY"],
"validation":["validation","validate"],"observed-state-boundary":["observed_state","observed-state-boundary"],
"configuration":["configuration","config"],"uncertainty":["uncertainty","residual"],"regression":["regression","REGRESSION"],
"simulation":["simulation","simulator"],"hash":["hash","sha256"],"lineage":["lineage","provenance"],
"licence":["licence","license"],"dependency":["dependency","dependencies"],"promotion-record":["promotion","release_record"],
"human-gate":["human","approval","gate"],"citation":["citation","source"]
}
def validate():
 data=json.loads(MANIFEST.read_text(encoding="utf-8"))
 source="
".join(p.read_text(errors="ignore") for p in INT.glob("*.py"))
 findings=[]
 for domain, spec in data["domains"].items():
  for iface in spec["interfaces"]:
   tokens=TOKEN_MAP.get(iface,[iface])
   if not any(t.lower() in source.lower() for t in tokens):
    findings.append({"domain":domain,"interface":iface,"reason":"NO_IMPLEMENTATION_SIGNAL"})
 return {"status":"CLEAN" if not findings else "BLOCKED","findings":findings,"checked_domains":len(data["domains"])}
if __name__=="__main__": print(json.dumps(validate(),indent=2,sort_keys=True))
