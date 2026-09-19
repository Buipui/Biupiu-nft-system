# Biupiu Game Physics Adapter Registry v1.0

## Preliminary integration target

The physics engine now has a neutral vehicle-handling adapter for research against
game-mod physics systems. It is designed to compare *concepts and measurable
parameters*, not copy proprietary game code or assets.

### Reference families

- **Forza:** suspension/handling parameterisation and telemetry-oriented workflows.
  SUSP.OS demonstrates a physics-based suspension solve and game-specific quantisation.
- **GTA V:** handling.meta exposes mass, drivetrain, grip, brakes, suspension and
  related handling parameters; real-time editors demonstrate rapid parameter iteration.
- **The Witcher 3:** WolvenKit provides an open-source research/modding toolkit for
  REDengine formats. It is treated here as an asset/mod integration reference,
  not as a source of proprietary physics code.

### Adapter architecture

Game/mod reference -> parameter normalisation -> Biupiu physics kernel ->
benchmark cases -> candidate profile -> engine-specific export layer.

### Safety and licensing boundary

Only original Biupiu code, generic equations, public documentation, and
appropriately licensed open-source code should enter the reusable engine.
Proprietary game binaries, extracted copyrighted assets, or copied closed-source
implementation details are not imported.

### Preliminary status

PASS for:
1. common vehicle parameter schema;
2. straight-line acceleration sanity check;
3. bicycle-model cornering sanity check;
4. longitudinal load-transfer calculation;
5. neutral profile-difference comparison.

NOT YET CLAIMED:
- in-game behavioural equivalence;
- compatibility with a particular game version;
- validated tyre model;
- validated suspension model;
- production-ready mod export.

### Next gate

Add per-title calibration datasets using user-owned/test-legal data, then run
repeatable regression benchmarks before any engine-specific export is enabled.
