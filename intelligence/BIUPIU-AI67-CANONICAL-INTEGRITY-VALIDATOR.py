"""AI-67 canonical integrity manifest validator."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; I=ROOT/"intelligence"
def validate():
 m=json.loads((I/"BIUPIU-SYSTEM-INTEGRITY-MANIFEST-v1.json").read_text())
 required=["AI-58","AI-59","AI-60","AI-61","AI-62","AI-63","AI-64","AI-65","AI-66"]
 files={f.stem for f in I.glob("*")}
 missing=[g for g in required if not any(g in x for x in files)]
 auth=m["canonical_authorities"]
 unique=len(set(auth.values()))==len(auth)
 return {"status":"CLEAN" if not missing and unique else "BLOCKED","missing_gates":missing,"unique_authorities":unique,"chain_complete":not missing}
if __name__=="__main__":
 print(json.dumps(validate(),indent=2,sort_keys=True))
