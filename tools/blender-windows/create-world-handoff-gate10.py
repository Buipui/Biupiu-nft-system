"""Gate 10 — create a downstream handoff only from an explicit APPROVE record."""
import json
def create(decision_path,output_path):
    with open(decision_path,"r",encoding="utf-8") as f: d=json.load(f)
    checks=d.get("checks",{})
    approved=d.get("decision")=="APPROVE" and all(checks.get(k)=="PASS" for k in ("visual","provenance","evidence","asset_rights"))
    handoff={"handoff_id":"BPU-WORLD-HANDOFF-01","package_id":d.get("package_id"),
      "approval":{"decision":"APPROVE" if approved else "PENDING","checks":checks},
      "assets":[],"downstream_targets":["BIUPIU_WORLD","SHOWREEL","DIGITAL_TWIN_CATALOG"],
      "release_gate":"READY_FOR_DOWNSTREAM" if approved else "HOLD"}
    with open(output_path,"w",encoding="utf-8") as f: json.dump(handoff,f,indent=2)
    return handoff
