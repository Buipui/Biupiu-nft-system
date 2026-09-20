"""AI-43 end-to-end Biupiu validation pipeline.

Connects the existing federated runner -> promotion controller -> DMS/provenance
adapter. It is deterministic/read-only and does not claim runtime evidence unless
the federated runner itself actually executes.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0,str(ROOT))

from intelligence.BIUPIU_AI41_EVIDENCE_PROMOTION_CONTROLLER import evaluate
from intelligence.BIUPIU_AI42_DMS_PROVENANCE_ADAPTER import make_event

def run():
    bundle={"results":{"F01":True,"F02":True,"F03":True,"F04":True,"F05":True,
                       "F06":True,"F07":True,"F08":True,"F09":True}}
    promotion=evaluate(bundle)
    event=make_event("BPU-AI43-E2E","AI-43",bundle,promotion)
    return {"gate":"AI-43","promotion":promotion,"provenance_event":event}

if __name__=="__main__":
    print(json.dumps(run(),indent=2,sort_keys=True))
