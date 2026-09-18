# Biupiu Animation Research Index — Gate 3

**Version:** 1.0  
**Date:** 2026-09-18  
**Status:** IMPLEMENTED — CI VALIDATION CONFIGURED; RUNTIME DCC/USD VALIDATION PENDING

## Gate 3 scope

Gate 3 converts the Gate 2 artifact contract into a repeatable repository-level static validation layer.

### Added
- `research/pipeline-tests/validate_animation_pipeline.py`
- `.github/workflows/animation-pipeline-validation.yml`

### Validation contract
The validator checks:
1. Minimal USD scene exists and contains the expected scene, camera, research ID and animated transform declarations.
2. OTIO manifest is valid JSON with the expected timeline schema/name.
3. The OTIO manifest contains one video track and one clip.
4. Clip duration is 48 frames at 24 fps.
5. The external media target remains the declared test-render placeholder.

## External technology alignment

OpenTimelineIO is an editorial interchange format/API and references external media rather than embedding media; its current upstream project documents Python support and integration with VFX/DCC/game-engine workflows. See the upstream project documentation before runtime adoption.

## Boundary

This gate performs **static contract validation only**. It does not claim that USD, Blender, Unreal, OTIO, or any renderer has been installed or executed.

## Next gate

Gate 4: execute the repository validator through GitHub Actions, then add runtime adapters/interchange tests for the configured DCC/render environment. Runtime results must be recorded from actual workflow logs rather than inferred from repository structure.
