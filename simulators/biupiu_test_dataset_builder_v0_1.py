"""PROP-15 machine-readable experiment dataset builder."""
from dataclasses import dataclass, asdict
import json

@dataclass
class Measurement:
    test_id: str
    module: str
    application: str
    altitude_m: float
    pressure_ratio: float
    recuperator_efficiency: float
    target_kw: float
    uncertainty_fraction: float
    validation_status: str = "planned"

def build():
    apps = ["AUTO","MARINE","EVTOL","HELI","UAV"]
    rows=[]
    n=1
    for module,kw in (("BT-70",70),("BT-140",140),("BT-200",200),("BT-300",300)):
        for app in apps:
            rows.append(asdict(Measurement(
                f"PROP15-{n:04d}",module,app,0,5.0,0.70,kw,0.10)))
            n+=1
    return rows

if __name__=="__main__":
    print(json.dumps({"schema_version":"PROP-15-v1.0","measurements":build()},indent=2))
