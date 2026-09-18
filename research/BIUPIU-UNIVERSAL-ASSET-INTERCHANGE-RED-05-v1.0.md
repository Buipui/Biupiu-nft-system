# Biupiu Universal Asset Interchange — RED-05

**Gate:** RED-05  
**Status:** Integrated — live provider execution remains environment-gated.

## Objective
Create a provider-neutral asset envelope so one authoritative Biupiu model can be packaged for different render applications without losing source identity, model version, material identity, evidence state, IP state, licence state or provenance.

## Canonical flow
SOURCE ASSET → UNIVERSAL ASSET MANIFEST → INTERCHANGE PACKAGE → PROVIDER ADAPTER → PROVIDER SCENE → RENDER OUTPUT → PROVENANCE RECORD

## Interchange policy
- The authoritative source asset remains outside provider derivatives.
- sourceAssetId and sourceModelVersion are immutable lineage fields.
- Material slots retain stable materialId values.
- Geometry records units, coordinate system and up-axis.
- Research, evidence, IP and licence states travel with the manifest.
- Provider-specific settings are stored as adapter/package metadata.
- Lossy conversion, unsupported material features and failed imports must be recorded rather than silently substituted.
- Rendered derivatives may never overwrite the authoritative source.
- No measured material property may be inferred from a visual shader.

## Formats
The contract allows GLTF, FBX and USD as interchange targets and also permits OBJ, USDZ and provider-native formats where an adapter requires them. Format support is an adapter responsibility; the manifest does not claim feature parity across providers.

## Material layer
Materials use stable IDs plus a compact PBR description. Texture assets are referenced by asset ID where present. Licence state is mandatory so distributable packages can be blocked until clearance.

## Provider packaging
RED-04 providers are represented by the same envelope: Blender, Unreal Engine 5, Redshift, V-Ray, Octane, Lumion and KeyShot. The broader render pipeline contract also retains Cinema 4D, Twinmotion, Adobe, Firefly and Runway.

## Acceptance criteria
1. Source asset identity survives every package operation.
2. Model version survives every package operation.
3. Material identity survives provider packaging.
4. Research/evidence/IP/licence state is preserved.
5. Units and coordinate metadata are explicit.
6. Provider settings are recorded.
7. Derivatives cannot replace the source asset.
8. Live conversion/render acceptance is performed only on connected provider hosts.

## Current state
The software contract, fixture and RED-05 test are committed. Live cross-provider conversion remains gated until the corresponding provider environments are connected and measured outputs are available.
