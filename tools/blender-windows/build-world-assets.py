"""Biupiu World procedural production scaffold for official Blender Windows."""
import bpy

CHARACTERS = [
    ("WORLD_GUIDE_BASE","BRAND"),
    ("FARMING_CHAR_01","CONCEPT"),
    ("METALLURGY_CHAR_01","CONCEPT"),
    ("TEXTILES_CHAR_01","CONCEPT"),
    ("MATERIALS_CHAR_01","RESEARCH CONCEPT"),
]
ENVIRONMENTS=["MAIN_HUB","FARMING_WORLD","SMART_METAL_WORKSHOP","TEXTILE_FIBRE_INNOVATION","ADVANCED_MATERIALS_LAB","BIOTECH_RESEARCH","PHOTONICS_LAB","AI_ROBOTICS_LAB","MARINE_AQUA","AUTOMOTIVE_SHOWROOM","EVTOL_AEROSPACE","RESEARCH_ARCHIVE"]
PRODUCTS=[("BLADE_MICROTURBINE","DESIGN STUDY"),("AEROBLADE_GT","DESIGN STUDY"),("MARINE_AQUA","CONCEPT"),("EVTOL","CONCEPT"),("HELICOPTER_AEROSPACE","CONCEPT"),("REGENERATIVE_AGRI_EQUIPMENT","CONCEPT")]

def collection(name):
    c=bpy.data.collections.get(name)
    if not c:
        c=bpy.data.collections.new(name); bpy.context.scene.collection.children.link(c)
    return c

def marker(name,loc,col,claim):
    bpy.ops.mesh.primitive_cube_add(size=1,location=loc)
    o=bpy.context.object; o.name=name; o.scale=(1,1,.15)
    o["biupiu_id"]="BPU-"+name; o["claim_class"]=claim
    o["evidence_state"]="UNVALIDATED_VISUALISATION"
    o["provenance"]="Biupiu procedural production scaffold"
    for c in list(o.users_collection): c.objects.unlink(o)
    col.objects.link(o)

scene=bpy.context.scene
scene["biupiu_gate"]="WORLD-PRODUCTION-GATE-01"
scene["biupiu_engine"]="BLENDER-WINDOWS-OFFICIAL"
scene["biupiu_claim_policy"]="Labels required until validated"

collection("BPU_WORLD_PRODUCTION"); collection("BPU_CHARACTERS"); collection("BPU_ENVIRONMENTS"); collection("BPU_PRODUCTS")
for i,(n,claim) in enumerate(CHARACTERS): marker(n,(i*2.5,0,.5),collection("CHAR_"+n),claim)
for i,n in enumerate(ENVIRONMENTS): marker(n,(i%4*3,i//4*3,.5),collection("ENV_"+n),"CONCEPT")
for i,(n,claim) in enumerate(PRODUCTS): marker(n,(i*3,-5,.5),collection("PRODUCT_"+n),claim)

if "BPU_PRODUCTION_CAMERA" not in bpy.data.objects:
    bpy.ops.object.camera_add(location=(18,-24,16)); cam=bpy.context.object; cam.name="BPU_PRODUCTION_CAMERA"; scene.camera=cam
if "BPU_KEY_LIGHT" not in bpy.data.objects:
    bpy.ops.object.light_add(type="AREA",location=(4,-6,12)); light=bpy.context.object; light.name="BPU_KEY_LIGHT"; light.data.energy=1500; light.data.size=8
print("Biupiu World production scaffold generated.")
