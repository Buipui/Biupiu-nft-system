# BIUPIU Licensed / Restricted External Asset Library Register v1.0

Date: 20 September 2026
Status: IMPLEMENTED — reference library
Purpose: Preserve useful knowledge about systems that are valuable but may not be redistributable, may contain mixed licences, or may require paid/shared access.

## Library rule

Store metadata, capabilities, provenance, official links, licence/access conditions, interoperability notes and substitute mappings. Do not copy proprietary binaries, source, models, textures or documentation unless the licence explicitly permits storage and redistribution.

## Register

### EXT-R2-001 — NVIDIA Isaac Sim / Omniverse components
- Role: robotics simulation, synthetic data, OpenUSD integration.
- Source class: R2.
- Key finding: Isaac Sim source in its GitHub repository is Apache 2.0, while additional build/runtime components such as Omniverse Kit SDK, models and textures have separate terms.
- Biupiu use: internal R&D / simulator adapter; do not assume unrestricted redistribution of the full stack.
- Substitute: Gazebo for a more fully open robotics simulation path; OpenUSD for scene/data interoperability.
- Official reference: https://docs.isaacsim.omniverse.nvidia.com/

### EXT-R2-002 — Siemens Xcelerator APIs / SDKs
- Role: industrial APIs, anomaly detection SDKs, IIoT integrations.
- Source class: R2.
- Key finding: Siemens provides a developer portal and publishes SDKs, but use is governed by product/API terms and account access.
- Biupiu use: adapter/reference, licensed integration if required.
- Substitute: OPC UA/MQTT-compatible open tooling and open-source industrial middleware where feasible.
- Official reference: https://developer.siemens.com/

### EXT-R2-003 — Unity Industry / Studio
- Role: real-time 3D, industrial visualization, internal digital-twin applications.
- Source class: R2.
- Key finding: commercial use and deployment depend on plan/industry terms; internal deployment provisions and licensing changed in 2026.
- Biupiu use: reference/optional commercial toolchain; never bake Unity licensing assumptions into OS ownership.
- Substitute: Unreal Engine under its EULA, OpenUSD-based pipelines, Gazebo, Blender, or other permitted tools depending on target.
- Official reference: https://unity.com/legal/industry-terms-of-service

### EXT-R2-004 — Unreal Engine
- Role: Biupiu World and immersive simulation/visualisation.
- Source class: R2.
- Key finding: proprietary software governed by Epic's EULA; commercial usage is allowed under applicable EULA conditions.
- Biupiu use: external engine integration; project IP remains governed separately from engine rights.
- Substitute: open-source scene/rendering pipelines where licensing or deployment constraints require it.
- Official reference: https://www.unrealengine.com/eula/unreal

### EXT-R3-001 — Elmer CSC
- Role: multiphysics research and engineering.
- Source class: R3/R1 depending component.
- Key finding: open source, with GPL and LGPL-covered components; CSC documents potential support/customisation routes.
- Biupiu use: solver/reference; isolate where GPL boundary affects proprietary composition.
- Substitute: SUNDIALS for solver kernels, Chrono for dynamics, OpenFOAM for CFD, or a separately licensed solver.
- Official reference: https://docs.csc.fi/apps/elmer/

## Promotion rule

A restricted or mixed-license system can be useful without being integrated. Its knowledge record may feed Intelligence, Digital Twin capability matching, simulator selection and substitute discovery while executable use stays behind licence/access gates.