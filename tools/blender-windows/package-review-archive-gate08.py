"""Biupiu Gate 08 — review archive/index generator.
Run after Gate 07 Blender renders. Packages only files that actually exist and
records SHA-256 hashes; it never invents missing renders or approves release.
"""
import os,json,hashlib
from datetime import datetime,timezone

SHOTS=("HERO-01","TECH-01","DETAIL-01","REAR-01")
def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def package(render_dir,archive_dir):
    os.makedirs(archive_dir,exist_ok=True)
    records=[]
    for sid in SHOTS:
        path=os.path.join(render_dir,sid+".png")
        if os.path.exists(path):
            records.append({"shot_id":sid,"status":"PRESENT","sha256":sha256(path),"source":path})
        else:
            records.append({"shot_id":sid,"status":"MISSING","source":path})
    manifest={"gate":"08","package_id":"BPU-REVIEW-ARCHIVE-01",
      "created_utc":datetime.now(timezone.utc).isoformat(),"records":records,
      "visual_qa":"PENDING","provenance_qa":"PENDING","evidence_qa":"PENDING",
      "release_gate":"HOLD_UNTIL_HUMAN_QA"}
    with open(os.path.join(archive_dir,"review-index.json"),"w",encoding="utf-8") as f: json.dump(manifest,f,indent=2)
    return manifest
