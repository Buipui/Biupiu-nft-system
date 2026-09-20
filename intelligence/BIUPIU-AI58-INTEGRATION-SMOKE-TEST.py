"""AI-58 integration-manifest smoke test."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; INT=ROOT/"intelligence"
def run():
 m=json.loads((INT/"BIUPIU-AI58-SYSTEM-INTEGRATION-MANIFEST.json").read_text())
 required={"OS","DMS","INTELLIGENCE","SIMULATORS","CONFIGURATORS","MATH_PHYSICS","DIGITAL_TWIN","PROVENANCE","SECURITY","BLOCKCHAIN","HMI","RESEARCH"}
 domains=set(m["domains"])
 r={"all_domains_declared":domains==required,"all_have_interfaces":all(m["domains"][d].get("interfaces") for d in required),"all_use_kernel":all(m["domains"][d].get("governance")=="AI-56" for d in required)}
 r["missing_domain_detected"]=set(m["domains"])==required
 return r
if __name__=="__main__":
 r=run(); print(r); raise SystemExit(0 if all(r.values()) else 1)
