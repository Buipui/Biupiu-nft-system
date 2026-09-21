# BIUPIU OS DESIGN DIGEST — 2026-09-21

## Gate 26 — Neutral Premium Design Standard

**Status:** IMPLEMENTED — repository source updated; runtime/device verification pending.

### Decision

The Biupiu visual philosophy is now formally simplified. The earlier colour-wheel exploration remains a research/reference layer, but it is no longer the default presentation strategy. Biupiu OS uses a neutral premium foundation and controlled material finishes.

### Canonical formula

**NEUTRAL BASE → MATERIAL FINISH → RESTRAINED NATURE ACCENT → CLEAR INFORMATION**

### References used

Ferrari Tailor Made demonstrates deliberate material selection, craftsmanship and curated collections; Pagani is used as a reference for high-end configuration and material presentation. These references inform principles only. Android Compose supports custom Material 3 colour schemes and custom design systems, so Biupiu can retain its own visual authority while using native Compose components. Compose Canvas/drawing APIs provide the technical path for future restrained material treatments without requiring a complicated UI framework.

### Repository changes

Implemented:
- authoritative neutral Biupiu Material 3 colour scheme;
- simplified native Android shell;
- neutral material cards for Workshop;
- restrained nature accents;
- centralised design tokens;
- universal design-philosophy document;
- OS/DMS index update;
- master Intelligence index update.

### Design rejection rule

Reject unnecessary rainbow palettes, excessive gradients, decorative complexity, gaming-style UI clutter, colour used as the only state indicator, and fake claims of physical/PBR material accuracy.

Prefer graphite, titanium, aluminium, warm white, stone/sand, bronze, muted green/patina, precise typography, simple cards, obvious controls, clear state and reversible configuration.

### Scope

This is now a **Biupiu OS-wide and subsystem-wide design principle**, not an Android-only preference. It applies to the OS shell, DMS, Intelligence, Research/Lab, Workshop, Digital Twin, simulators, configurators, departmental applications, and future desktop, embedded and cross-platform shells.

### Verification

**IMPLEMENTED:** source-level design contract and Android implementation.

**PENDING:** build, emulator/device rendering, accessibility/contrast automation and cross-platform conformance.

No runtime capability is inferred from this design gate.
