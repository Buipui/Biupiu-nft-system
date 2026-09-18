# V-Ray Connector Architecture v1.0

Biupiu adapter boundary:

R&D Asset → Canonical glTF/GLB or DCC Asset → V-Ray Job Adapter → V-Ray Runtime/App SDK → Render Output → Provenance Record

## Adapter responsibilities
1. Validate the render-job schema.
2. Resolve the immutable source asset/version.
3. Convert or consume glTF/GLB where appropriate.
4. Record V-Ray/runtime version and connector version.
5. Submit render parameters.
6. Capture output and render metadata.
7. Store hashes and provenance.
8. Return status/errors without modifying the authoritative research object.

## Separation
The connector does not become an engineering solver. Aerodynamic, CFD, FEA, thermal and propulsion validation remain separate evidence-producing systems.
