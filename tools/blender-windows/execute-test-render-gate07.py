"""Biupiu Gate 07 — controlled Blender test-render execution harness."""
import bpy, json, os, hashlib
from datetime import datetime, timezone
SHOTS=[("HERO-01","Hero three-quarter",50),("TECH-01","Technical reference",70),("DETAIL-01","Macro detail",85),("REAR-01","Rear/service",55)]
def fingerprint(scene):
    keys=["biupiu_id","digital_twin_ref","evidence_state","claim_class","provenance","licence_status"]
    return hashlib.sha256(json.dumps({k:scene.get(k) for k in keys},sort_keys=True).encode()).hexdigest()
def execute(output_dir="//biupiu_gate07_output"):
    scene=bpy.context.scene; out=bpy.path.abspath(output_dir); os.makedirs(out,exist_ok=True)
    scene["biupiu_gate"]="WORLD-PRODUCTION-GATE-07"; scene["gate07_execution_timestamp"]=datetime.now(timezone.utc).isoformat()
    scene["gate07_scene_fingerprint"]=fingerprint(scene); scene["gate07_render_engine"]="BLENDER_WINDOWS_OFFICIAL"
    scene["gate07_resolution"]="1920x1080"; scene["gate07_release_gate"]="HOLD_UNTIL_QA"
    records=[]
    for sid,purpose,lens in SHOTS:
        scene.render.resolution_x=1920; scene.render.resolution_y=1080; scene.render.resolution_percentage=50
        path=os.path.join(out,sid+".png"); scene.render.filepath=path; scene["active_review_shot"]=sid
        bpy.ops.render.render(write_still=True)
        records.append({"shot_id":sid,"purpose":purpose,"lens_mm":lens,"output_path":path,
                        "status":"RENDERED" if os.path.exists(path) else "RENDER_FAILED"})
    manifest={"gate":"07","package_id":"BPU-TEST-RENDER-PACKAGE-01","scene_fingerprint":scene["gate07_scene_fingerprint"],
              "records":records,"release_gate":"HOLD_UNTIL_QA"}
    with open(os.path.join(out,"gate07-manifest.json"),"w",encoding="utf-8") as f: json.dump(manifest,f,indent=2)
    return manifest
if __name__=="__main__": execute()
