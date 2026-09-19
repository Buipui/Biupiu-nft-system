"""Biupiu World Production Gate 03 — structured hero scene scaffold.
Run inside Blender's Python environment. Produces review-ready scene metadata,
material slots, camera shot register and Digital Twin validation without
claiming final engineering validation or final renders.
"""
import bpy, json

SCENE_ID="BPU_HERO_BLADE_MICROTURBINE"
DT_REF="DT-BPU-BLADE-MICROTURBINE-01"

REQUIRED_META={
 "biupiu_gate":"WORLD-PRODUCTION-GATE-03","biupiu_id":"BPU-BLADE-MICROTURBINE-HERO-01",
 "asset_type":"product","evidence_state":"UNVALIDATED_VISUALISATION",
 "claim_class":"DESIGN STUDY","provenance":"Biupiu procedural hero-scene scaffold",
 "licence_status":"INTERNAL_SCAFFOLD_ONLY","digital_twin_ref":DT_REF,
 "units":"metres","forward_axis":"+Y","up_axis":"+Z"
}
MATERIAL_SLOTS=[
 ("MAT-BODY-SHELL","Body shell","PLACEHOLDER"),
 ("MAT-BLADE-COMPOSITE","Blade/composite","PLACEHOLDER"),
 ("MAT-METAL","Metallic technical surfaces","PLACEHOLDER"),
 ("MAT-ACCENT","Biupiu presentation accent","PLACEHOLDER")
]
SHOTS=[
 ("HERO-01","Hero three-quarter product presentation",50),
 ("TECH-01","Orthographic technical reference",70),
 ("DETAIL-01","Macro material/detail study",85),
 ("REAR-01","Rear/service-side presentation",55)
]

def validate():
    checks={
      "metadata_pass": all(k in bpy.context.scene for k in REQUIRED_META),
      "materials_pass": len(MATERIAL_SLOTS)==4,
      "cameras_pass": len(SHOTS)==4
    }
    return checks, all(checks.values())

def build():
    scene=bpy.context.scene
    for k,v in REQUIRED_META.items(): scene[k]=v
    for cname in ("BPU_HERO_ASSEMBLY","BPU_HERO_MATERIAL_SLOTS","BPU_HERO_CAMERAS"):
        col=bpy.data.collections.get(cname) or bpy.data.collections.new(cname)
        if col.name not in scene.collection.children: scene.collection.children.link(col)
    for sid,role,status in MATERIAL_SLOTS: scene["material."+sid]={"role":role,"status":status}
    scene["camera_shot_register"]=json.dumps([{"shot_id":s,"purpose":p,"lens_mm":l} for s,p,l in SHOTS])
    checks,passed=validate()
    scene["gate03_validation"]=json.dumps({"passed":passed,"checks":checks})
    scene["review_status"]="READY_FOR_REVIEW" if passed else "REVIEW_REQUIRED"
    return passed

if __name__=="__main__":
    build()
