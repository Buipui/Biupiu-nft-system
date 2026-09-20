# BIUPIU UNITY 6 SEARCH / INTEGRATION GATE v1.0

Date: 20 September 2026
Status: EXECUTED — discovery, provenance classification and repository-side integration; host runtime remains OPEN

## Objective
Add Unity 6 as a controlled optional visual/simulation adapter alongside UE5 without replacing the authoritative Biupiu World contracts.

## Search protocol
1. Unity official documentation/resources.
2. Unity Technologies GitHub repositories.
3. GitHub open-source ecosystem for reusable Unity-compatible code/assets.
4. Open educational/OpenStax material for algorithms, computer systems, GPU/parallel computing and software architecture.
5. Licence/provenance classification before promotion.
6. Route approved resources through Biupiu Intelligence -> AI OS proposal -> Main OS validation -> Digital Twin release manifest -> relevant department adapter.

## High-value resources identified

### Unity official
- Unity 6 Resources Hub: https://unity.com/campaign/unity-6-resources
- Unity 6 documentation: https://docs.unity.com/
- Unity asset import guidance: https://docs.unity.com/en-us/engine/6000.6/manual/assets-and-media/import-assets/importing-assets

### Unity Technologies GitHub
- EntityComponentSystemSamples: https://github.com/Unity-Technologies/EntityComponentSystemSamples
  - Unity 6.2 samples covering Entities, Physics, Netcode and Entities.Graphics.
- Unity-Robotics-Hub: https://github.com/Unity-Technologies/Unity-Robotics-Hub
  - Robotics simulation, URDF import, ROS/ROS 2 integration, articulations and visualization.
- AR Foundation samples: https://github.com/Unity-Technologies/arfoundation-samples
  - Unity 6.0+ sample baseline for AR workflows.
- UI Toolkit manual code examples: https://github.com/Unity-Technologies/ui-toolkit-manual-code-examples
  - Runtime UI, data binding, lists, toggles, custom controls and radial/progress UI patterns.
- DesktopSamples: https://github.com/Unity-Technologies/DesktopSamples
  - MIT-licensed desktop integration examples.
- uGUI: https://github.com/Unity-Technologies/uGUI
  - Unity UI source reference.

### Open educational stream
- OpenStax Introduction to Computer Science:
  https://openstax.org/books/introduction-computer-science/
  Useful sections include algorithms, computer systems, GPU/parallel programming, GUI and software architecture concepts.
- Open educational material remains learning/reference input; copyrighted books are not copied into the repository merely because they are discoverable.

### Open asset candidates
- Quaternius CC0 assets: candidate source for generic characters/props/structures after direct licence and file-level provenance capture.
- Kenney CC0 packs: candidate source for generic UI/audio/prototype assets after direct licence verification.
- Poly Haven CC0: candidate source for HDRIs/materials/environment assets after direct source capture.
- Aetherium's documented asset-sourcing plan is retained as a discovery lead, not as proof of third-party licence beyond the original asset provider's own terms:
  https://github.com/danvanderboom/Aetherium/blob/main/docs/design/unity-sample/assets.md

## Promotion classification

PROMOTE-CANDIDATE:
- Unity official samples/code with compatible licence/terms.
- Unity DOTS/Entities samples for ECS architecture and performance experiments.
- Unity Robotics Hub for robotics/ROS adapter research.
- Unity UI Toolkit examples for Biupiu HMI presentation patterns.
- MIT-licensed DesktopSamples where applicable.
- CC0 assets from their original providers after file-level provenance capture.

REFERENCE-ONLY:
- OpenStax educational material.
- Older Unity sample repositories whose tested versions predate the target Unity 6 configuration.
- Third-party lists that aggregate assets without being the original licence authority.

BLOCKED / DO NOT IMPORT:
- Proprietary Unity/third-party game assets without explicit incorporation rights.
- Assets whose licence cannot be established.
- Proprietary UE5/Decima/RAGE assets or code.
- External packages promoted directly into authoritative engineering logic without validation.

## Biupiu World routing

Unity is an optional provider, not the source of truth.

Biupiu World canonical assets
-> Unity6 adapter
-> scene/render/UI/physics/navigation provider
-> telemetry
-> validation
-> provenance
-> Digital Twin promotion

UE5 and Unity may consume the same approved World asset manifests while retaining independent runtime adapters.

## Host integration note

The user's desktop Visual Studio / Visual Studio Code Insider resources and PowerShell workflow are treated as development-host capabilities. Their presence does not constitute runtime verification. The next host gate must inspect the actual Unity installation, editor version, project compatibility, package resolution, compilation and smoke-test results.

## Result
Search protocol executed and useful Unity/OpenStax/GitHub resources registered. No unverified external binary asset has been claimed as incorporated. Runtime installation, package import, build and visual regression remain OPEN until executed on the development host.


## EXTERMINATE / CONFLICT RECONCILIATION — 20 September 2026

- Engine authority conflict checked: NONE. UE5 and Unity remain optional runtime providers; Biupiu World remains authoritative.
- Asset-provenance conflict checked: external assets remain candidates until file-level source/licence/version evidence exists.
- Visual Studio / VS Code Insider conflict checked: editor/tooling is host infrastructure, not a runtime dependency of the authoritative simulation layer.
- Package-version conflict checked: Unity 6 samples are version-sensitive; current Unity Technologies ECS samples use Unity 6.2 with Entities/Netcode/Physics/Entities.Graphics 1.4, so package resolution must be performed against the installed editor rather than copied blindly. citeturn0search0
- Parallelism/safety review: Unity Jobs/Burst/DOTS candidates remain adapter-level options; deterministic dependencies and safety checks must be preserved. citeturn0search5

**EXTERMINATE RESULT: PASS at repository/architecture level. No conflicting authority, proprietary asset, or unverified runtime dependency was promoted.**

## NEXT GATE — UNITY HOST INTEGRATION

Host execution is required to move from registry status to runtime status. The sequence is fixed:

1. Detect installed Unity Editor and version.
2. Detect Visual Studio / VS Code Insider integration and C# tooling.
3. Inspect existing Unity projects without modifying production files.
4. Create/open isolated Biupiu Unity adapter test project.
5. Resolve Unity packages against the detected editor version.
6. Compile with warnings/errors captured.
7. Connect the Biupiu World adapter contract.
8. Import one approved, provenance-recorded visual resource.
9. Run HMI + asset + scene-load smoke tests.
10. Run Exterminate/conflict scan.
11. Capture logs/build evidence and repository round-trip.
12. Promote only the components directly verified on the host.

**CURRENT STATE: READY FOR HOST EXECUTION — NOT YET HOST-VERIFIED.**
