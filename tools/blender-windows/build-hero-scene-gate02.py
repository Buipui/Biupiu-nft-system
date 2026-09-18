"""Gate 02 placeholder-safe hero scene builder for Blender Windows."""
import bpy

SCENE_NAME = "BPU_HERO_BLADE_MICROTURBINE"

def ensure_collection(name):
    col = bpy.data.collections.get(name)
    if col is None:
        col = bpy.data.collections.new(name)
        bpy.context.scene.collection.children.link(col)
    return col

scene = bpy.context.scene
scene.name = SCENE_NAME
scene["biupiu_gate"] = "WORLD-PRODUCTION-GATE-02"
scene["biupiu_id"] = "BPU-BLADE-MICROTURBINE-HERO-01"
scene["asset_type"] = "product"
scene["evidence_state"] = "UNVALIDATED_VISUALISATION"
scene["claim_class"] = "DESIGN STUDY"
scene["provenance"] = "Biupiu procedural hero-scene scaffold"
scene["licence_status"] = "INTERNAL_SCAFFOLD_ONLY"
scene["digital_twin_ref"] = "DT-BPU-BLADE-MICROTURBINE-01"

for name in ("ASSEMBLY", "MATERIAL_SLOTS", "TECHNICAL_OVERLAYS", "CAMERAS", "METADATA"):
    ensure_collection("BPU_HERO_" + name)

bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=1.5, depth=4.0, location=(0, 0, 0))
body = bpy.context.object
body.name = "BPU_HERO_PLACEHOLDER_BODY"
body["role"] = "placeholder assembly geometry"
body["claim_class"] = "DESIGN STUDY"
for col in list(body.users_collection):
    col.objects.unlink(body)
ensure_collection("BPU_HERO_ASSEMBLY").objects.link(body)

if "BPU_HERO_CAMERA" not in bpy.data.objects:
    bpy.ops.object.camera_add(location=(9, -11, 7))
    cam = bpy.context.object
    cam.name = "BPU_HERO_CAMERA"
    scene.camera = cam

print("Gate 02 hero scene scaffold generated; replace placeholder geometry only after review.")
