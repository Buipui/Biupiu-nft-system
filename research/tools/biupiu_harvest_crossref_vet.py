#!/usr/bin/env python3
import json, hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
internal=[
 {"id":"I-Q1.1","source":"research/BIUPIU-QUANTICOR-OPTIMISED-PROTOCOL-v1.1.json","domain":"controlled intersection, decompile, defragment, regression, provenance"},
 {"id":"I-BENCH","source":"research/BIUPIU-SYSTEM-FAMILY-BENCHMARK-STANDARD-v1.0.json","domain":"functional equivalence, build/runtime evidence, performance dimensions"},
 {"id":"I-NATIVE","source":"research/evidence/BIUPIU-SYSTEM-FAMILY-NATIVE-AUDIT-20260924.json","domain":"family/module/adapter integration and evidence gaps"},
 {"id":"I-HARVEST","source":"research/evidence/BIUPIU-DEEP-HARVEST-CROSS-TEST-LOG-20260924.json","domain":"external harvest classification and retest gates"},
]
external=[
 {"id":"E-PHOTONIC","domain":"photonic interconnect bandwidth/energy density","source":"Nature Photonics 2025"},
 {"id":"E-SIPHONIC","domain":"silicon photonics/CMOS integration and co-design","source":"Nature Reviews Electrical Engineering 2026"},
 {"id":"E-QUANTUM-NET","domain":"quantum optical routing/control/measurement/digital twin","source":"NIST 2026"},
 {"id":"E-PROB-PHOT","domain":"photonic probabilistic computing and hardware/software co-design","source":"Nature Computational Science 2025"},
]
cross=[
 {"internal":"I-BENCH","external":["E-PHOTONIC","E-SIPHONIC"],"mapped_metrics":["latency","throughput","energy_per_bit","bandwidth_density","thermal/resource cost"],"vet":"PERFORMANCE_SCHEMA_SUPPORTED"},
 {"internal":"I-Q1.1","external":["E-QUANTUM-NET","E-PROB-PHOT"],"mapped_metrics":["path quality","routing/control latency","resource availability","fault/recovery","measurement evidence"],"vet":"CONTROL_MODEL_SUPPORTED"},
 {"internal":"I-NATIVE","external":["E-SIPHONIC","E-QUANTUM-NET"],"mapped_metrics":["native/federated boundary","adapter health","build reproducibility","runtime evidence"],"vet":"INTEGRATION_SCHEMA_SUPPORTED"},
 {"internal":"I-HARVEST","external":["E-PHOTONIC","E-QUANTUM-NET"],"mapped_metrics":["source provenance","licence status","semantic compatibility","reproducibility"],"vet":"RESEARCH_ONLY_UNTIL_GATED"},
]
families=["mini-os","apps/android","mini-os/android","smart-farming/android","software/rnd-os-mobile","apps/windows"]
result={
 "schema":"biupiu.harvest-crossref-vet.v1",
 "status":"CROSS_REFERENCED_VET_REGISTERED",
 "authority":{"DigiCat":"catalogue/cross-library index","DigiFile":"evidence/provenance/hash chain","Learning":"proposal/regression learning","source":"executable truth","geometry":"relationship/path proposal","regression":"acceptance gate"},
 "internal_library":internal,
 "external_library":external,
 "cross_reference":cross,
 "family_vet_matrix":[
   {"family":f,"DigiCat":"REGISTERED","DigiFile":"REQUIRED","Learning":"SHARED_CORE","performance":"PENDING_EXECUTABLE_EVIDENCE","external_harvest":"ADAPTER_OR_RESEARCH_ONLY"} for f in families
 ],
 "rules":[
   "External research cannot overwrite internal executable truth.",
   "Research claims become test hypotheses, not performance results.",
   "Computational geometry proposes candidate paths; executable regression accepts them.",
   "Performance comparisons require functionally equivalent workloads and measured evidence.",
   "Quantum and photonic findings remain model/adapter inputs until hardware/runtime evidence exists.",
   "DigiFile records source identity, licence/provenance, hashes, test evidence and promotion state.",
   "DigiCat cross-indexes internal and external knowledge without becoming execution authority."
 ],
 "promotion_allowed":False
}
raw=json.dumps(result,sort_keys=True).encode()
result["content_hash"]=hashlib.sha256(raw).hexdigest()
out=ROOT/"research/evidence/BIUPIU-HARVEST-CROSSREF-VET-20260924.json"
out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
