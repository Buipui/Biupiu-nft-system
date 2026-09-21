# Biupiu Smart Systems Federation Harvest — 2026-09-21

## Sources harvested
### International standards
ISO 11783 is directly relevant to the farming priority. ISO describes it as an open interconnected system for agricultural/forestry onboard electronics, enabling ECUs to communicate using standardized mechanisms. ISO 11783-3:2026 is the current published Part 3 and covers application, transport and network layers mapped to CAN. ISO 11783-10 covers Task Controller interchange; Part 12 covers diagnostics and is currently at FDIS stage.

### DARPA
Assured Autonomy emphasizes continual assurance of learning-enabled cyber-physical systems: safety and functional correctness are evaluated at design time and continuously during operation. This is adopted as an architectural reference, not as a claim that Biupiu has equivalent assurance.

CODE emphasizes modular software architectures that tolerate communication limitations and integrate with existing standards. This supports Biupiu's modular-controller and gateway principle.

### NASA / MIT
Existing Biupiu resource registry already contains NASA and MIT architecture/education references. This gate preserves them as reference material and applies the repository's evidence/provenance rules rather than promoting external material directly into executable code.

### Foreign-language research
The existing Biupiu multilingual research protocol remains the route for non-English harvesting. Foreign-language material is candidate evidence until translated, provenance-checked, independently corroborated and classified.

## Federation synthesis
The strongest reusable pattern is not a single protocol. It is the combination:
modular device functions + standardized message contracts + deterministic local control + gatewaying + diagnostics + digital twin + continual assurance + evidence-backed learning.

## Repository integration targets
- intelligence/
- intelligence/schemas/
- intelligence/tasks/
- research/
- smart-farming/
- software/dms/
- packages/biupiu-rnd-os/

## No silent promotion
External architectures are not treated as verified Biupiu implementations. Runtime tests, hardware tests, CI and license/provenance checks remain promotion gates.
