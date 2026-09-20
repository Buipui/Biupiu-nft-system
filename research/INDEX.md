

## GRAPHICS / AUDIO / HDR ADAPTER INTEGRATION GATE — 20 September 2026

### Gate objective
Integrate only reusable, licence-compatible modules and architecture patterns into the Biupiu OS / Biupiu AI / Biupiu Intelligence learning layer. Vendor-specific software remains external; adapters and capability probes are preferred.

### Approved integration boundary
- **NVIDIA OptiX / RTX:** register a ray-tracing backend contract and GPU capability-probe interface. NVIDIA OptiX SDK, headers and samples remain licence-gated; no proprietary header or sample code is copied into Biupiu core. Official references: NVIDIA optix-sdk, optix-dev and OptiX Toolkit.
- **Ray tracing pipeline:** Biupiu Render Contract -> capability probe -> DXR/Vulkan/OptiX backend -> acceleration structures -> ray generation/intersection/shading -> denoiser/upscaling -> visual QA -> telemetry.
- **Lenovo Legion:** register performance, thermal, lighting and device-control capabilities as a hardware-adapter schema. No Lenovo proprietary software is embedded.
- **ASUS ROG:** register Armoury Crate/Aura capability categories. Legacy third-party Aura bindings remain isolated and unpromoted until current API, dependency and security checks pass.
- **Dell Alienware:** register AlienFX lighting and thermal/performance adapter categories. Open-source implementations must be checked individually for licence, reverse-engineering restrictions, device compatibility and security before use.
- **Sony 360 Reality Audio:** register object-based spatial-audio scene concepts; proprietary Sony SDKs remain licensing-gated.
- **Dolby Atmos / Dolby Vision:** register spatial-audio, HDR metadata, profile/device capability and visual-QA concepts. Dolby SDKs and technologies remain licensing-gated and are not treated as open-source dependencies.

### Reusable modules promoted to architecture knowledge (not runtime code)
1. GPU capability probe interface: vendor, device, driver, API support, ray-tracing support, VRAM, feature flags and confidence/evidence state.
2. Rendering backend interface: initialise, capability query, scene upload, acceleration-structure build, render, denoise, shutdown and diagnostic reporting.
3. Spatial-audio object model: object ID, position, velocity, gain, spread, priority, routing and measured/estimated state.
4. HDR/visual validation record: display profile, colour space, transfer function, metadata, frame hash, device profile, visual defects and pass/fail evidence.
5. Hardware adapter manifest: manufacturer, model family, supported controls, transport/API, dependency list, licence status, safety limits and rollback behaviour.
6. Intelligence learning record: capability, interface, dependency, licence, evidence, adapter pattern, regression rule and promotion state.

### Controlled code policy
No external third-party code is copied into Biupiu core during this gate. Candidate repositories are linked as external dependencies or isolated research inputs until licence and build validation are completed. NVIDIA OptiX repositories explicitly include proprietary/licence-controlled material, so they remain reference dependencies only. OptiX Toolkit requires a compatible C++/CUDA/CMake environment and must be tested on the development host before any adapter promotion.

### Exterminate result
- Architecture-level module contracts: **IMPLEMENTED IN DOCUMENTATION**.
- Third-party code integration: **NOT PROMOTED** pending licence/dependency review.
- GPU/device detection: **HOST-DEPENDENT / NOT VERIFIED**.
- Compilation and runtime rendering: **NOT VERIFIED**.
- Physical device, audio and HDR validation: **NOT VERIFIED**.
- Repository index update: **COMMITTED**.

**NEXT GATE:** create isolated adapter projects, run host capability probes, compile only licence-approved dependencies, execute deterministic smoke tests, collect evidence, then promote modules individually.
## POWERSHELL / DOS GATEWAY + DIGITAL TWIN — 20 September 2026

### Gate objective
Build a controlled Windows PowerShell execution gateway from the existing Biupiu DOS command/compatibility layer, then expose its state through the Digital Twin without making PowerShell authoritative.

### Repository execution
- DOS command/permission model reused as the gateway basis: **IMPLEMENTED**.
- PowerShell Gateway README/policy/source: **COMMITTED**.
- Deterministic gateway policy test: **COMMITTED**.
- PowerShell Gateway Digital Twin schema: **COMMITTED**.
- Default mode: **DRY-RUN**.
- Arbitrary command/script execution: **DENIED BY POLICY**.
- Network/download/install operations: **DENIED BY BASE POLICY**.
- Write operations: **EXPLICIT APPROVAL REQUIRED**.
- Structured evidence output: **IMPLEMENTED**.
- Credentials/secrets in gateway: **NONE**.

### Existing gate reconciliation
- External graphics adapter boundary: **COMMITTED**.
- Graphics candidate manifest: **COMMITTED**.
- Graphics host probe: **COMMITTED / HOST-EXECUTION-PENDING**.
- Third-party vendor code copied into Core: **NO**.
- GPU/driver/CMake/CUDA/DXR/Vulkan host detection: **UNVERIFIED**.
- DOS compatibility runtime: **ARCHITECTURE + RESOURCE REGISTRY EXECUTED; HOST RUNTIME OPEN**.
- Digital Twin promotion contract: **REGISTERED**.
- Recursive Digital Twin architecture: **INTEGRATED**.

### Digital Twin route
OS Twin -> DOS command contract -> PowerShell Gateway Twin -> host observations/evidence -> Digital Twin -> validated department routing

The Digital Twin mirrors evidence and lineage. It cannot elevate an unverified host observation into authoritative OS state.

### Exterminate / security
The gateway does not expose Invoke-Expression, arbitrary script paths, unrestricted process execution, download/install mutation, or unapproved network execution. PowerShell execution policy is treated only as defence-in-depth because Microsoft documents that execution policy is not a security boundary.

### Verification boundary
Repository implementation/read-back: **COMMITTED**.
Windows PowerShell runtime: **PENDING / UNVERIFIED**.
Actual GPU/driver/Unity/UE5/Visual Studio/VS Code discovery through gateway: **PENDING / UNVERIFIED**.
Android-to-Windows live control: **NOT IMPLEMENTED**.
Production promotion: **OPEN**.

**NEXT GATE:** execute the gateway and graphics probe on the Windows development host, capture JSON evidence, run named tests, reconcile the evidence into the Digital Twin, then promote only evidence-backed capabilities.
## POWERSHELL GATE 02 — CI REGRESSION + DIGITAL TWIN VALIDATION — 20 September 2026
- Windows GitHub Actions regression workflow: **COMMITTED**.
- Deterministic gateway policy test wired into CI: **IMPLEMENTED**.
- Gateway dry-run smoke test wired into CI: **IMPLEMENTED**.
- Forbidden execution primitive check wired into CI: **IMPLEMENTED**.
- Digital Twin schema validation wired into CI: **IMPLEMENTED**.
- CI workflow execution result: **PENDING**.
- Windows development-host runtime: **PENDING / UNVERIFIED**.
- GPU/driver/Unity/UE5/Visual Studio/VS Code host discovery: **PENDING / UNVERIFIED**.
- Android-to-Windows live control: **NOT IMPLEMENTED**.

**NEXT GATE:** obtain the GitHub Actions run result; then, on the Windows development host, execute the gateway plus graphics probe and reconcile host evidence into the Digital Twin.