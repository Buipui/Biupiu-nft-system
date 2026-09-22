# Buipiu Mini OS — Simulator Federation Registry

## Registered capability adapters
| ID | Domain | Adapter | Execution policy |
|---|---|---|---|
| chrono | vehicle / multiphysics | Project Chrono | probe-only until native build/runtime evidence |
| openstudio | architecture / building / design | OpenStudio | probe-only until native build/runtime evidence |
| energyplus | building energy | EnergyPlus | probe-only until native build/runtime evidence |
| opensim | movement / biomechanics / environment agents | OpenSim | probe-only until native build/runtime evidence |

## Android contract
The Android Mini OS exposes these as capability identities and job/state exchange contracts. It does not silently package third-party desktop binaries. A backend becomes executable only after the corresponding native Android-compatible build, ABI/dependency, smoke and regression gates pass.

## Cross-system links
- Vehicle -> Digital Twin -> Chrono adapter
- Architecture/Building -> Digital Twin -> OpenStudio/EnergyPlus adapters
- Farming/Environment/World -> Digital Twin -> OpenSim adapter
- Android -> Federation -> capability discovery/job/state exchange
- World -> visualization/presentation only

## Evidence boundary
REGISTERED / SOURCE-INTEGRATED / SOURCE-SMOKE-PASS / RUNTIME-OPEN
