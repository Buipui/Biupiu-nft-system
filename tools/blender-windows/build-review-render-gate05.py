"""Biupiu World Production Gate 05 — first review-render assembly scaffold.
This generates deterministic Blender scene metadata and render settings for
four review shots. It does not fabricate finished geometry, textures, or
engineering validation.
"""
import bpy, json

SHOTS = [
    ("HERO-01","Hero three-quarter product presentation",(1920,1080),50),
    ("TECH-01","Orthographic technical reference",(1920,1080),70),
    ("DETAIL-01","Macro material/detail study",(1920,1080),85),
    ("REAR-01","Rear/service-side presentation",(1920,1080),55),
]

def build():
    scene=bpy.context.scene
    scene["biupiu_gate"]="WORLD-PRODUCTION-GATE-05"
    scene["review_package_id"]="BPU-HERO-REVIEW-PACKAGE-01"
    scene["render_engine_target"]="BLENDER_WINDOWS_OFFICIAL"
    scene["render_resolution"]="1920x1080"
    scene["render_status"]="REVIEW_RENDER_SCAFFOLD"
    scene["asset_policy"]="APPROVED_OR_LICENSED_ASSET_INPUTS_ONLY"
    scene["provenance_status"]="REQUIRED"
    scene["evidence_status"]=scene.get("evidence_state","UNVALIDATED_VISUALISATION")
    scene["release_gate"]="HOLD_UNTIL_REVIEW"
    scene["shot_register"]=json.dumps([
        {"shot_id":sid,"purpose":purpose,"resolution":list(res),"lens_mm":lens,"status":"READY_FOR_ASSET_INPUT"}
        for sid,purpose,res,lens in SHOTS
    ])
    scene.render.resolution_x=1920
    scene.render.resolution_y=1080
    scene.render.resolution_percentage=50
    return True

if __name__=="__main__":
    build()
