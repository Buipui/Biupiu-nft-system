"""Biupiu Gate 09 — auditable review decision record generator.
Creates a decision template from actual archive records. It never auto-approves.
"""
import json,os
from datetime import datetime,timezone

def create(index_path,output_path):
    with open(index_path,"r",encoding="utf-8") as f: index=json.load(f)
    missing=[x["shot_id"] for x in index.get("records",[]) if x.get("status")!="PRESENT"]
    decision={
      "package_id":index.get("package_id","BPU-REVIEW-ARCHIVE-01"),
      "decision":"PENDING","reviewer_role":"HUMAN_REVIEWER",
      "checks":{"visual":"PENDING","provenance":"PENDING","evidence":"PENDING","asset_rights":"PENDING"},
      "notes":"Human review required. Missing frames: "+(", ".join(missing) if missing else "none"),
      "release_gate":"HOLD","created_utc":datetime.now(timezone.utc).isoformat()
    }
    with open(output_path,"w",encoding="utf-8") as f: json.dump(decision,f,indent=2)
    return decision
