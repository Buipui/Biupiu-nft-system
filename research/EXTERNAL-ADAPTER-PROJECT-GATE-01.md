# External Adapter Project Gate 01 — 20 September 2026

## Status
- Adapter boundary: COMMITTED
- Graphics candidate manifest: COMMITTED
- Windows host probe: COMMITTED / HOST-EXECUTION-PENDING
- Vendor code copied into Biupiu Core: NO
- Licence approval: PARTIAL / PER-CANDIDATE REVIEW REQUIRED
- Local GPU, driver, CMake, CUDA, DXR and Vulkan detection: UNVERIFIED

## Created files
- `software/adapters/README.md`
- `software/adapters/graphics/adapter-manifest.json`
- `software/adapters/host-probes/Invoke-BiupiuGraphicsProbe.ps1`

## Existing capability reuse
The existing provider-neutral simulator adapter pattern is retained as the baseline for safe executable discovery and argument validation. The existing AI evidence/provenance boundary remains authoritative; external modules cannot bypass validation or promotion gates.

## Candidate integration boundary
NVRHI is registered as an external rendering abstraction candidate. RTXDI and OptiX remain isolated research/reference candidates pending per-version licence, dependency, security and build checks. DXR and Vulkan remain host backend targets.

## Exterminate
No third-party vendor code was copied into Biupiu Core. The PowerShell probe is observation-only and does not install, download or execute external backends. Host execution and runtime rendering remain unverified until evidence is collected from the development desktop.

## Next gate
1. Read back all created files.
2. Add deterministic tests for manifest validation and probe output shape.
3. Run the PowerShell probe on the Windows host.
4. Compile only licence-approved dependencies.
5. Promote each adapter independently after evidence review.
