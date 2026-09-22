# Biupiu Design Language + Simulator/UI Semantic Audit — 2026-09-22

## Scope
Repository-first audit of Biupiu OS, Biupiu OS AI, native simulator federation, desktop/mobile UI shells, World interaction architecture and governed simulator resource research.

External research was used only to improve architecture patterns. No third-party proprietary assets or unverified code were imported.

## External architecture findings

- Digital Twin Consortium: separate Data, Context, Decision/Process Orchestration and Actuation layers; explicit confidence/authority and simulation-before-actuation are useful patterns for Biupiu's existing DMS/AI/OS chain.
- OpenUSD: layered, composable scene description supports non-destructive asset composition and provenance-aware world pipelines.
- Open-source simulator architecture examples: deterministic simulation, separate presentation/application/domain layers, explicit adapters, event systems, resource managers and UI modules.
- Agentic digital-twin examples: propose -> simulate -> gate -> apply -> audit is compatible with Biupiu's existing fail-closed governance.
- Design-system research: interactive controls require explicit states, hierarchy and constraints; a visually correct button without a governed action contract is not a functional UI.

These patterns are incorporated as architecture principles, not copied implementations.

## Repository findings

### Design language
Existing Gate 26/27/28/29 work already established:

NEUTRAL BASE -> MATERIAL FINISH -> RESTRAINED NATURE ACCENT -> CLEAR INFORMATION

The design system is intended to apply across OS, DMS, Intelligence, Lab, Workshop, Digital Twin, simulators, configurators and World.

### Semantic UI defects found

1. Windows DepartmentModuleWindow had a missing CapabilityPanel named element. The code-behind attempted to add controls to CapabilityPanel, but the XAML did not declare it.
2. Windows capability buttons changed only the title text. They did not have an explicit semantic action result or blocked/not-implemented feedback.
3. Android department action buttons contained empty click handlers. They rendered as controls but did nothing.
4. Android Main Hub exposed RENDER_PIPELINE but openDepartment() silently returned. This was a semantic failure because the visible control had no user-visible reason for not acting.
5. Existing source-level design gates were being treated as architecture contracts, while device/host/UE5 runtime evidence remained pending. The audit preserves this distinction.

## Changes on this branch

- Added canonical design-language code contract: docs/architecture/BIUPIU-DESIGN-LANGUAGE-CODE-CONTRACT-v1.0.json
- Added semantic action contract: research/BIUPIU-UI-SEMANTIC-ACTION-CONTRACT-v1.0.md
- Bound the native simulator module registry to both contracts.
- Fixed the Windows missing capability panel.
- Replaced silent Windows capability clicks with explicit semantic status feedback.
- Replaced Android department no-op buttons with routed capability feedback through CapabilityRouter.
- Made Android RENDER_PIPELINE explicitly report UNKNOWN_CAPABILITY rather than silently failing.
- Added deterministic repository smoke audit and CI workflow.

## Native simulator capability audit

Current native federation is a common metadata/observation boundary, not a universal high-fidelity solver.

The native source currently supports:
- simulator context identity;
- model/version/source-commit metadata;
- unit metadata;
- deterministic timestep validation;
- finite-value checks;
- observation recording;
- residual and confidence recording;
- domain-agnostic simulator federation;
- provenance-oriented observation data.

Existing domain lanes provide source-level foundations for:
- automotive longitudinal vehicle dynamics;
- marine surge/sway/yaw and drag foundations;
- aerospace/space thrust/drag/gravity/altitude foundations;
- farming rainfall/irrigation/infiltration/ET/soil-moisture foundations;
- digital-twin and telemetry boundaries;
- World/UE5 adapter contracts.

They do not establish that the repository currently has a verified high-fidelity solver for every domain.

## Current UI/OS functions established by source

- Main Hub routing and entitlement-aware entry.
- R&D OS shell.
- Department routing for Smart Farming, Smart Metal Workshop and R&D OS.
- Capability registry/router on Android.
- Authentication/session contracts in the mobile OS.
- Semantic state representation.
- Material/colourway abstraction.
- Design-system architecture.
- Simulator adapter registry.
- Federation contracts.
- Digital Twin/World interaction contracts.
- Fail-closed AI/OS promotion architecture.
- Native C/C++/Rust boundary contracts.
- Repository learning/failure/audit architecture.

## Still open

- Windows build execution.
- Android Gradle/device/emulator execution.
- Cross-platform visual conformance.
- Accessibility/contrast automation.
- UE5 import/runtime validation.
- Native simulator host compilation and execution for every lane.
- External simulator execution.
- High-fidelity physics validation.
- Hardware-in-loop.
- Physical actuation.
- Full visual regression/showreel verification.
- Final Biupiu material/PBR validation.

## Promotion rule

A beautiful interface is not considered complete until every visible control has a deterministic semantic path and every claimed backend capability has execution evidence.

SOURCE -> STATIC AUDIT -> BUILD -> SMOKE -> RUNTIME -> DEVICE/HOST -> REGRESSION -> VERIFIED

Audit result: SOURCE-LEVEL UI SEMANTIC DEFECTS IDENTIFIED AND CORRECTED ON THIS BRANCH. RUNTIME VERIFICATION REMAINS OPEN.