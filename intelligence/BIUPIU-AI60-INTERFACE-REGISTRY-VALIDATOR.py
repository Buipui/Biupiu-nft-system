"""AI-60 explicit interface registry validator."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; INT=ROOT/"intelligence"
REG=INT/"BIUPIU-AI60-INTERFACE-REGISTRY.json"; MAN=INT/"BIUPIU-AI58-SYSTEM-INTEGRATION-MANIFEST.json"
def validate():
 r=json.loads(REG.read_text()); m=json.loads(MAN.read_text())
 declared={x for d in m["domains"].values() for x in d["interfaces"]}
 registered=set(r["interfaces"])
 missing=sorted(declared-registered); extra=sorted(registered-declared)
 malformed=[k for k,v in r["interfaces"].items() if not v.get("adapter") or not v.get("contract")]
 return {"status":"CLEAN" if not missing and not extra and not malformed else "BLOCKED","missing":missing,"extra":extra,"malformed":malformed,"registered":len(registered)}
if __name__=="__main__": print(json.dumps(validate(),indent=2,sort_keys=True))
