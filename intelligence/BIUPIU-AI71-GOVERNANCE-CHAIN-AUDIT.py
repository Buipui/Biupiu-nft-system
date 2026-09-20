"""AI-71 governance-chain consistency audit.
Repository/static verification only; promotion remains blocked.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; I=ROOT/"intelligence"
CHAIN=["AI58","AI59","AI60","AI61","AI62","AI63","AI64","AI65","AI66","AI67","AI68","AI69","AI70"]
def run():
 names={p.name for p in I.iterdir()}
 presence={g:any(g in n for n in names) for g in CHAIN}
 missing=[g for g,v in presence.items() if not v]
 required=[
  "BIUPIU-AI58-SYSTEM-INTEGRATION-MANIFEST.json",
  "BIUPIU-AI60-INTERFACE-REGISTRY.json",
  "BIUPIU-GOVERNANCE-KERNEL-AI56.py",
  "BIUPIU-AI67-CANONICAL-INTEGRITY-VALIDATOR.py",
  "BIUPIU-AI68-RUNTIME-VERIFICATION-HARNESS.py",
  "BIUPIU-AI69-AUTHORITY-CONFLICT-SCANNER.py",
  "BIUPIU-AI70-AUTHORITY-RESOLUTION-GATE.py"]
 missing_required=[x for x in required if not (I/x).exists()]
 return {"gate":"AI-71","chain":presence,"missing_gates":missing,
 "missing_required_artifacts":missing_required,
 "chain_consistent":not missing and not missing_required,
 "promotion_barrier":"ACTIVE",
 "promotion_allowed":False,
 "verification_level":"STATIC_REPOSITORY"}
if __name__=="__main__": print(json.dumps(run(),indent=2,sort_keys=True))
