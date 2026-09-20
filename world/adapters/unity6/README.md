# Biupiu World — Unity 6 Adapter

Status: IMPLEMENTED — adapter contract/documentation scaffold; runtime NOT VERIFIED

## Purpose
Provide an optional Unity 6 presentation/simulation adapter without moving authoritative Biupiu state, engineering truth or provenance into Unity-specific code.

## Contract
Input:
- Biupiu World asset manifest
- approved asset/provenance records
- world coordinate conventions
- scene/environment metadata
- telemetry contracts
- department adapter manifests

Unity responsibilities:
- scene presentation
- visual materials/shaders
- UI/HMI presentation
- navigation/interaction
- optional physics-provider experiments
- desktop/mobile visual prototypes where supported

Biupiu responsibilities:
- authoritative state
- engineering calculations
- validation
- provenance/licensing
- promotion decisions
- Digital Twin release manifests

## Initial resource adapters
- DOTS/Entities/Physics samples
- Robotics Hub / URDF / ROS integration
- UI Toolkit
- approved CC0 visual assets
- approved texture/HDRI sources

## Safety
No automatic import of arbitrary Asset Store/GitHub content.
Every dependency requires source URL, version/commit, licence, compatibility result and provenance record.

## Next host gate
1. Detect installed Unity version.
2. Create/open isolated Unity 6 adapter test project.
3. Resolve packages.
4. Compile.
5. Import one approved sample/resource.
6. Run deterministic smoke test.
7. Verify HMI/asset bridge.
8. Record logs and hashes.
9. Update promotion state only from direct evidence.
