"""AI-47 governed task router.

Maps a task to the existing Biupiu AI teams and emits a task packet compatible
with AI-31 and the AI-46 unified index. Read-only: no provider calls or actuation.
"""
from __future__ import annotations
import json, hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"intelligence/BIUPIU-AI-TEAM-MANIFEST-v1.json"

def route(task_id, objective, routes):
    manifest=json.loads(MANIFEST.read_text(encoding="utf-8"))
    selected=[]
    for team in manifest["teams"]:
        if "ALL" in team["routes"] or any(r in team["routes"] for r in routes):
            selected.append({"id":team["id"],"members":team["members"],"routes":team["routes"]})
    packet={
      "task_id":task_id,
      "objective":objective,
      "routes":routes,
      "assigned_teams":selected,
      "evidence_required":True,
      "challenge_required":True,
      "regression_required":True,
      "provenance_required":True,
      "promotion_authority":"BIUPIU-INTELLIGENCE",
      "execution_boundary":manifest["execution_boundary"]
    }
    packet["packet_hash"]=hashlib.sha256(json.dumps(packet,sort_keys=True).encode()).hexdigest()
    return packet

if __name__=="__main__":
    print(json.dumps(route("BPU-AI47-SELFTEST","Validate unified orchestration routing",["OS","DMS","SIMULATORS","MATH"]),indent=2,sort_keys=True))
