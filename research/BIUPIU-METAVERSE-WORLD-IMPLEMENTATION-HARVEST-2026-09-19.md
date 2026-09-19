# Biupiu World Metaverse Implementation Harvest — 2026-09-19

## METAVERSE-HARVEST-01
Research-to-implementation gate for Biupiu World.

### Key architecture evidence
- ResearchGate/ISPRS: geospatial virtual worlds are proposed as a modular combination of access, world and integration layers, with WebXR, WebSocket, WebRTC, real-time sensor data, digital twins, location services, persistence and multi-user interaction. The paper is CC BY 4.0. https://www.researchgate.net/publication/389736249_The_Metaverse_Is_Geospatial_A_System_Model_Architecture_Integrating_Spatial_Computing_Digital_Twins_and_Virtual_Worlds
- WebXR: browser standard foundation for XR device/input detection and immersive presentation. https://github.com/immersive-web/webxr
- Immersive Web SDK: current open-source Three.js-based immersive web stack with ECS, WebXR, spatial UI, locomotion, physics, spatial audio and desktop emulation; MIT licensed according to repository metadata. https://github.com/facebook/immersive-web-sdk
- XREngine: open-source metaverse infrastructure reference covering realtime worlds, avatars, inventory, social functions, WebRTC, networked physics and optional blockchain integration. https://github.com/XRFoundation/XREngine
- NASA MRET v2.0: mixed-reality framework integrating engineering/CAD models, AR/VR, telemetry and collaboration. https://software.nasa.gov/software/GSC-18602-1

### Biupiu World implementation model
1. Authoritative Biupiu OS state
2. World scene graph / Digital Twin
3. Persistent world state
4. Identity + avatar adapter
5. Multi-user session layer
6. Spatial interaction/XR adapter
7. WebRTC voice/video adapter
8. WebSocket/state-sync adapter
9. Economy/provenance boundary
10. Telemetry/replay
11. Security/moderation
12. Department simulator adapters

### Promotion rule
External frameworks are references/adapters until licence, dependency, security, compatibility and regression gates pass. Do not copy third-party code or assets into Biupiu merely because a project is open source.

### Exterminate result
Overlapping metaverse concepts are consolidated into one Biupiu World architecture. Speculative token-market capitalization is not treated as revenue. Blockchain is an optional provenance/economy adapter, not authoritative world state.

### Recommended implementation order
WORLD-01 persistent scene state → WORLD-02 entity identity/avatar contract → WORLD-03 WebSocket state sync → WORLD-04 WebRTC media boundary → WORLD-05 WebXR adapter → WORLD-06 permissions/moderation → WORLD-07 replay/telemetry → WORLD-08 department simulator federation.

**Status: research harvest complete; implementation contracts added in next gate.**
