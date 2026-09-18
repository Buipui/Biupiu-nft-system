"""Biupiu World Production Gate 04.
Builds a review-render package scaffold around approved/licensed asset inputs.
No third-party asset is imported automatically and no engineering validation is implied.
"""
import bpy, json

REQUIRED=("biupiu_id","digital_twin_ref","evidence_state","claim_class","provenance","licence_status","units","forward_axis","up_axis")
SHOT_IDS=("HERO-01","TECH-01","DETAIL-01","REAR-01")

def validate(scene):
    metadata=all(k in scene for k in REQUIRED)
    evidence=scene.get("evidence_state") in {"UNVALIDATED_VISUALISATION","RESEARCH_CONCEPT","PROTOTYPE","VALIDATED_PRODUCT"}
    licence=scene.get("licence_status") not in {None,"UNVERIFIED","UNKNOWN"}
    shots=all(scene.get("shot."+sid+".status") in {"PLACEHOLDER","READY"} for sid in SHOT_IDS)
    return {"metadata_pass":metadata,"evidence_pass":evidence,"licence_state_recorded":licence,"shot_register_pass":shots}

def build():
    scene=bpy.context.scene
    scene["biupiu_gate"]="WORLD-PRODUCTION-GATE-04"
    scene["review_package_id"]="BPU-HERO-REVIEW-PACKAGE-01"
    scene["render_status"]="SCAFFOLD_ONLY"
    scene["asset_import_policy"]="MANUAL_APPROVED_ASSET_ONLY"
    scene["engineering_validation"]="NOT_ESTABLISHED"
    scene["provenance_review"]="REQUIRED_BEFORE_RELEASE"
    for sid in SHOT_IDS:
        if "shot."+sid+".status" not in scene:
            scene["shot."+sid+".status"]="PLACEHOLDER"
    result=validate(scene)
    scene["gate04_validation"]=json.dumps(result)
    scene["review_release"]="HOLD_UNTIL_ASSET_AND_PROVENANCE_REVIEW"
    return result

if __name__=="__main__":
    build()
