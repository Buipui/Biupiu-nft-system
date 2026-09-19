# Biupiu 3D Open-Resource Integration v1.0

**Gate:** 3D-OPEN-01  
**Date:** 19 September 2026  
**Status:** IMPLEMENTED — resource registry, adapter package and reusable engineering templates committed.

## Scope
This gate treats the requested 03DE stream as the 3D engineering/computational-geometry resource stream. External engines are referenced rather than copied into Biupiu.

## Open-book layer
- OpenSCAD User Manual / Wikibooks — procedural solid modelling, language reference, transforms, import/export and command-line workflows. citeturn1search1turn1search8
- Engineering Statics: Open and Interactive — vectors, equilibrium, rigid bodies, structures, inertia and three-dimensional mechanics. citeturn1search2turn1search15
- Mechanics Map — open statics/dynamics material including rigid-body kinematics/dynamics and vibrations. citeturn1search12

## GitHub layer
- OpenSCAD — scriptable solid CAD and reproducible parameter-driven geometry. citeturn0search0
- BelfrySCAD — hybrid procedural CAD and WYSIWYG reference. citeturn0search1
- FreeCAD, Blender, OpenSCAD and build123d are cross-tool CAD/procedural references. citeturn0search2turn0search3
- CADAM — text-to-CAD architecture reference using OpenSCAD WASM and Three.js/React. citeturn0search4
- PythonSCAD — Python-oriented scriptable CAD reference. citeturn0search5

## Implemented code
`packages/biupiu-3d-engine/` provides a renderer-neutral model manifest, validation, OpenSCAD generation, bounding-radius checking and reusable micro-turbine, marine-propulsor and eVTOL blockout templates.

## Department routing
GEOMETRY/COMPUTE → parametric geometry and reproducibility.  
AERO → aircraft/eVTOL/helicopter geometry and downstream flight adapters.  
MARINE → hull, propulsor and hydrofoil concept geometry.  
ENERGY → turbines and rotating-machine geometry.  
COMPOSITES/MATERIALS → component envelopes and manufacturing handoff.  
ADV-MFG/ROBOTICS → fabrication envelopes, fixtures and machine-cell geometry.  
DIGITAL-TWIN → canonical manifests and model lineage.  
AI → future parameter search and surrogate optimisation.  
NFT-ART/NFT-PROV → only after research/IP/provenance gates.

## Boundary
Generated models are conceptual/research artefacts unless independently validated. External source code/assets remain external until licence, security, dependency and validation gates pass.

**3D-OPEN-01: EXECUTED.**
