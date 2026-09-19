# WORLD-ENGINE-RES-01 — Index Entry

**Registered:** 19 September 2026  
**Status:** Architecture and resource registry integrated

Linked records:
- `research/BIUPIU-WORLD-ENGINE-RESOURCE-INTEGRATION-v1.0.md`
- `research/BIUPIU-WORLD-ENGINE-RESOURCE-MANIFEST-v1.0.json`

Coverage:
- RAGE: proprietary reference; lawful read-only research only.
- Unity 6: optional adapter and package-evaluation reference; licence/version checks required.
- Decima: proprietary reference; open research tools isolated from proprietary game assets.
- Open books/learning: engine architecture, rendering, physics, asset pipelines and profiling.

Cross-links: `WORLD-CORE`, `CG-3D`, `RENDER`, `PHYS-SYS`, `DIGITAL-TWIN`, `AI`, `ROBOTICS`, `PROVENANCE`, `TESTING`, `VIDEO-SERIES`.

Promotion remains fail-closed and requires licence, security, compatibility, deterministic regression and human approval gates.


## SEPARATION-03 routing

External engine research is now routed through **Biupiu Intelligence → AI OS proposal → Main OS validation → Digital Twin release manifest → relevant department adapters**. New deterministic promotion routing is implemented at `software/rnd-os-ai/src/biupiu_ai/promotion_router.py` with regression coverage in `software/rnd-os-ai/tests/test_promotion_router.py`.

Only validated ADAPTER/ASSET/DEPENDENCY records may become Digital Twin candidates. REFERENCE/PATTERN records remain knowledge until independently implemented and validated; PROHIBITED records are blocked.
