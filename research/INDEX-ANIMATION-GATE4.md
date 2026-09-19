# Biupiu Animation Research Index — Gate 4
**Version:** 1.0  
**Date:** 2026-09-19  
**Status:** IMPLEMENTED — VALIDATOR SYNCHRONIZED; CI WORKFLOW ADDED

## Gate 4
The validator was synchronized with the repository's actual OTIO manifest structure. It now validates the USD/OTIO static contract without requiring a DCC runtime.

### Checks
- USDA header/default prim
- Animated camera declaration
- Animated transform declaration
- OTIO Timeline.1 schema
- One Video track and one clip
- 48 frames at 24 fps
- External test media target

A dedicated GitHub Actions workflow was added with both push/pull-request path triggers and manual dispatch.

## Verification boundary
The repository changes are committed. A CI pass is not claimed until an actual workflow run and logs are available.

## Next gate
Gate 5: execute/inspect CI results and, after a successful static gate, introduce configured USD/Blender/Unreal interchange tests.
