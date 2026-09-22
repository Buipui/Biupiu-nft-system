# Adapter fixtures

Fixtures are intentionally self-contained and contain no third-party binaries or proprietary assets.

## Validation
- JSON fixtures must parse.
- OBJ fixture must contain exactly 3 vertices and 1 face.
- Expected values are deterministic reference vectors, not evidence of third-party runtime execution.
- External solver/simulator PASS requires an actual supported runner and captured toolchain/dependency/commit/exit-code evidence.

## Promotion
Fixtures support ADAPTER-READY/SANDBOXED validation only until runtime evidence exists.
