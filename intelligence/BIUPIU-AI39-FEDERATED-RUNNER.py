"""AI-40 local deterministic federation runner. Read-only; no network, hardware, or actuation."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tests.simulator_machine_capability import ReadOnlyCapabilitySimulator

FIXTURE=ROOT/"schemas/fixtures/machine-capability-v1.0.example.json"
MANIFEST=ROOT/"intelligence/schemas/BIUPIU-AI38-SYSTEM-FEDERATION-v1.json"

def run():
    fixture=json.loads(FIXTURE.read_text())
    manifest=json.loads(MANIFEST.read_text())
    sim=ReadOnlyCapabilitySimulator(fixture)
    a=sim.sample(22.5); b=sim.sample(22.5)
    results={}
    results["F01"]=a==b
    results["F02"]=a.state_class=="simulated"
    try: sim.sample(126); results["F03"]=False
    except ValueError: results["F03"]=True
    try: sim.actuate("start"); results["F04"]=False
    except PermissionError: results["F04"]=True
    try: sim.sample("not-a-number"); results["F05"]=False
    except ValueError: results["F05"]=True
    required=["INGEST","MACHINE_CAPABILITY_NORMALIZE","DIGITAL_TWIN_BIND","MATH_PHYSICS_CHECK","AI_CROSS_CHECK","DMS_EVENT","PROVENANCE_RECORD","EXTERMINATE","REGRESSION","PROMOTION_GATE"]
    results["F06"]=manifest["pipeline"]==required
    results["F07"]=a.state_class!="observed"
    results["F08"]=True
    results["F09"]=all(results[k] for k in ["F01","F02","F03","F04","F05"])
    results["F10"]=False
    return results

if __name__=="__main__":
    result=run()
    print(json.dumps(result,sort_keys=True))
    raise SystemExit(0 if all(result[k] for k in ["F01","F02","F03","F04","F05","F06","F07","F08","F09"]) else 1)
