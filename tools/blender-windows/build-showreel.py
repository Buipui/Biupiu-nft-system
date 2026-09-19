"""Biupiu Windows Blender showreel scene bootstrap."""
import bpy

COLLECTIONS = [
    "BPU_WORLD_GATEWAY", "BPU_REGENERATIVE_AGRI", "BPU_MATERIALS",
    "BPU_BLADE_MICROTURBINE", "BPU_MARINE_AQUA", "BPU_AEROBLADE_GT",
    "BPU_EVTOL", "BPU_HELICOPTER_AEROSPACE", "BPU_AI_ROBOTICS",
    "BPU_PHOTONICS", "BPU_DIGITAL_TWIN", "BPU_WORLD_MONTAGE"
]

for name in COLLECTIONS:
    col = bpy.data.collections.get(name) or bpy.data.collections.new(name)
    if col.name not in bpy.context.scene.collection.children:
        bpy.context.scene.collection.children.link(col)

scene = bpy.context.scene
scene["biupiu_showreel_version"] = "1.0"
scene["biupiu_claim_policy"] = "CONCEPT/RESEARCH labels required until validated"
print("Biupiu showreel scene bootstrap ready")
