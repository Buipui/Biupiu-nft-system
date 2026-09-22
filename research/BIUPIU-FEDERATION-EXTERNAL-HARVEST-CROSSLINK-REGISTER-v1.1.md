# BIUPIU FEDERATION EXTERNAL HARVEST & INTERNAL CROSS-LINK REGISTER v1.1

Date: 2026-09-22
Status: REGISTERED / CANDIDATE HARVEST — runtime promotion pending

## Purpose
Extend the federation external-harvest lane with current potentially usable open resources, then cross-link each candidate against existing Biupiu modules before integration. External resources remain references/adapters until the evidence ladder passes.

## External candidates
| Candidate | Evidence observed | Proposed Biupiu use | Internal cross-link | State |
|---|---|---|---|---|
| Genesis World | Public robotics/embodied-AI simulator with multi-physics, renderer and cross-platform compiler | Physics/simulation architecture reference; isolated simulator adapter; benchmark comparison | MATH/PHYS-SYS, DIGITAL-TWIN, simulator boundary, World | CANDIDATE |
| DART 6 LTS | Open-source C++ robotics/animation/ML physics toolkit; stable LTS identified by project | Physics/kinematics baseline and numerical comparison; possible adapter | MATH, GEOMETRY, ROBOTICS, PHYS-SYS | CANDIDATE |
| CRISP | C++20 contact-rich robotics physics engine with mesh/SDF/DSF geometry and contact solvers | Contact/geometry solver research and simulator comparison | GEOMETRY, PHYS-SYS, ROBOTICS | CANDIDATE |
| OpenTelemetry | Trace/context and semantic-event patterns | Federation observability pattern; keep core dependency-light | F18 observability, trace/correlation, learning events | PATTERN/REFERENCE |
| Agent Flight Recorder | Research prototype for tamper-evident agent audit trails and on-chain anchoring | Audit/provenance and blockchain-anchor reference | provenance, learning events, blockchain registry | PATTERN/REFERENCE |
| OpenFab | Reproducible build, signed provenance, AI/human attribution and acceptance criteria | Build/release/provenance pattern | coding matrix, release gates, learning checkpoints | PATTERN/REFERENCE |
| Halofy | Agent identity/policy/provenance/audit boundary pattern | Identity, policy and governed retrieval reference | DMS identity, security, federation authority | PATTERN/REFERENCE |
| Provenance data-mesh project | Contracts, lineage, governance and AI-agent participation pattern | Federated contract/lineage reference | federation contracts, DMS provenance | PATTERN/REFERENCE |
| NiuTrans LMT | 2026 multilingual translation resources covering 60 languages/234 directions | Multilingual retrieval/translation benchmark/reference | multilingual research lane, learning/indexing | CANDIDATE |
| SHIFT | 2026 multilingual retrieval correction method with public tests/benchmarks | Language-bias mitigation experiment for cross-language retrieval | multilingual index, retrieval/evidence graph | CANDIDATE |

## Selection rule
No external candidate is copied into authoritative Biupiu core merely because it is current, popular, open-source or technically strong. First compare against existing native modules. Prefer the Biupiu implementation where it satisfies the contract and evidence requirements; otherwise retain the external project as an adapter/reference candidate.

## Internal cross-link map
- packages/biupiu-rnd-os/src/federation-contracts.ts — canonical transport-neutral contract boundary.
- packages/biupiu-rnd-os/src/federation-contracts.test.ts — contract smoke test source.
- packages/biupiu-rnd-os/src/federation-harvest-gate.ts — fail-closed external harvest validator.
- software/digital-orchestra/orchestra.py — coordination/workflow execution layer.
- software/digital-orchestra/workflows/core-harvest.yaml — harvest workflow.
- research/BIUPIU-NATIVE-CODING-PHILOSOPHY-AND-ENGINEERING-MATRIX-v1.0.md — native coding rules.
- research/BIUPIU-GATE-LEARNING-ARCHITECTURE-v1.0.md — learning/evidence loop.
- research/BIUPIU-OS-DMS-SUBSYSTEM-MASTER-INDEX-v1.0.md — subsystem ownership/index.
- research/BIUPIU-SYSTEM-CROSS-LINK-DIGEST-v1.1.md — derived system digest.
- research/BIUPIU-INTELLIGENCE-ARCHITECTURE-v1.1.md — learning/provenance authority boundary.
- research/BIUPIU-COMPANY-ALGORITHM-NETWORK-v1.0.md — algorithm lineage and release identity.
- contracts/BiupiuLearningRegistry.sol — approved learning checkpoint anchor target.

## Verification state
- Architecture/source inspection: COMPLETE for this harvest record.
- Licence/IP review: project-specific review REQUIRED before import/adaptation.
- Static/unit/integration/regression/runtime verification: PENDING.
- Hardware/device correlation: NOT CLAIMED.
- Production promotion: NOT CLAIMED.

## Learning rule
For every candidate that proceeds to testing, record prior internal implementation, external version/commit, environment, expected/actual result, failure signature, compatibility impact, licence state, regression result, promotion decision and rollback reference.

## Blockchain rule
Prepare an anchor manifest only after repository evidence is frozen. Anchor release ID, resource IDs, internal module IDs and manifest hashes; do not put source code, private research, secrets, credentials, raw learning data or unpublished IP on-chain. No live blockchain transaction is claimed by this file.

## Gate
FEDERATION-EXTERNAL-HARVEST-2026-09-22-V1.1

State: CANDIDATE HARVEST REGISTERED; INTEGRATION/TEST GATES OPEN.
## Testing-protocol reconciliation — 22 September 2026
The recent module-testing protocols are now consolidated through `research/BIUPIU-HARVEST-MODULE-TESTING-PROTOCOL-REGISTRY-2026-09-22.json`. The executable promotion gate and CI workflow are cross-linked to this registry. No candidate may be marked VERIFIED-WORKING from registry presence alone; execution evidence remains required.

## Guided Fault-Finding Harvest — 22 September 2026
Internal harvest consolidated native failure-learning, federation, health, fault-healing and harvest-promotion controls into one guided diagnostic boundary. External harvest added NASA assurance/IV&V and OpenTelemetry trace/context correlation as reference patterns.
Cross-links: guided-fault-finder.ts; guided_fault_finding.py; existing learning.py; federation_protocol.py; federation-harvest-gate.ts; fault-healing-envelope-v1.json.
Promotion remains fail-closed. External patterns are not executable dependencies. Fresh CI/runtime evidence is required before VERIFIED-WORKING.
