# AI-23 — Open-Resource Integration & Audit Fail-Closed Gate

## Gate objective

Track external open-source engineering resources without copying upstream code into Biupiu. The registry preserves provenance, licence and intended integration mode.

## 2026 reference set

- NASA F Prime — flight software/component framework; Apache-2.0.
- NASA Core Flight System (cFS) — flight-software framework; Apache-2.0.
- MIT Computational Multicopter Design — geometry/design research code; GPL-2.0.
- MIT Distributed Robotics Laboratory repositories — robotics/optimization research; licence review is repository-specific.
- Wisp Science — scientific-AI workbench; AGPL-3.0-only.
- OpenArm — robotics/physical-AI ecosystem; licence review by repository.
- Unreal Robotics Lab — Unreal/MuJoCo robotics simulation; Apache-2.0.
- Genesis World — embodied-AI physics/simulation; Apache-2.0.
- Webots — robotics simulator; Apache-2.0.
- IR-SIM — robot simulation; MIT.

## Integration rules

1. External repositories remain references unless a separate import/licence gate approves incorporation.
2. GPL/AGPL resources require licence-compatibility review before use in proprietary components.
3. NASA and MIT resources are engineering references, not Biupiu-owned IP.
4. Resource metadata must preserve source and licence information.

## AI-23 gateway boundary

The gateway must fail closed when its configured audit persistence layer is not ready. The current gateway implementation contains this readiness check and retains provider-neutral audit handling.

## Verification boundary

The resource registry and gateway implementation are committed. Live execution of external projects, production provider transport and distributed durable audit infrastructure remain separate validation gates.

## Next gate

AI-24: outbox/queue abstraction, durable retry semantics and resource provenance checks.
