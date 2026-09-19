# Biupiu World Metaverse Adapter Contract v1.0

## Authority
Biupiu OS remains authoritative. Metaverse clients never directly mutate authoritative state.

## Core entities
- World
- Scene
- DigitalTwin
- Entity
- Avatar
- Session
- Interaction
- TelemetryEvent
- AssetReference
- EconomyEvent
- Permission

## State flow
AUTHORITATIVE OS → WORLD STATE → SESSION REPLICA → CLIENT/XR → INTERACTION REQUEST → VALIDATION → AUTHORITATIVE COMMIT → TELEMETRY/REPLAY

## Simulator federation
A department simulator publishes versioned state snapshots and telemetry through adapters. Biupiu World consumes them without importing simulator-specific authority.

Supported adapter classes:
- AUTO
- AERO
- MARINE
- AGRI
- ROBOTICS
- ADV-MFG
- PHYS-SYS
- CG-3D
- TRAINING

## Network boundary
WebSocket is the preferred state/event transport abstraction. WebRTC is an optional real-time media/data adapter. WebXR is the immersive presentation/input adapter.

## Safety
Untrusted client input is never authoritative. Physical systems require independent safety controls. AI proposals require OS validation and audit.

## Economy
NFT/token/blockchain functions are optional adapters. Financial/accounting truth remains off-chain unless explicitly promoted through a validated ledger integration.

## Provenance
Every promoted World entity should retain source, version, owner, licence and transformation metadata.

**Status: WORLD-METAVERSE-01 IMPLEMENTED.**
