"""Biupiu World Production Gate 06 — controlled test-render package.
Creates a deterministic test-render manifest and validation report. The script
does not claim that Blender executed a render unless run in Blender.
"""
import bpy, json, hashlib

SHOTS=("HERO-01","TECH-01","DETAIL-01","REAR-01")

def scene_fingerprint(scene):
    payload={k:scene[k] for k in scene.keys() if k.startswith("biupiu_") or k in {"review_package_id","evidence_state","claim_class"}}
    return hashlib.sha256(json.dumps(payload,sort_keys=True,default=str).encode()).hexdigest()

def build():
    scene=bpy.context.scene
    scene["biupiu_gate"]="WORLD-PRODUCTION-GATE-06"
    scene["test_render_package_id"]="BPU-TEST-RENDER-PACKAGE-01"
    scene["render_execution"]="NOT_EXECUTED_BY_REPOSITORY_WRITE"
    scene["render_target"]="BLENDER_WINDOWS_OFFICIAL"
    scene["resolution"]="1920x1080"
    scene["percentage"]=50
    scene["asset_validation"]="PENDING"
    scene["provenance_validation"]="PENDING"
    scene["evidence_validation"]="PENDING"
    scene["visual_qc"]="PENDING"
    scene["release_gate"]="HOLD"
    scene["scene_fingerprint"]=scene_fingerprint(scene)
    scene["test_render_manifest"]=json.dumps([
      {"shot_id":sid,"status":"READY_FOR_CONTROLLED_TEST_RENDER","output_type":"PNG_OR_EXR_REVIEW_FRAME"}
      for sid in SHOTS
    ])
    return True

if __name__=="__main__":
    build()
