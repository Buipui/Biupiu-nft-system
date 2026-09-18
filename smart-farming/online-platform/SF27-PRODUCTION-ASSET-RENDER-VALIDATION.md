# SF-27 — Production Asset & Render Validation

## Purpose
Validate every asset required by Biupiu World Episode 01 before final assembly.

Status: VALIDATION GATE / NO FINAL VIDEO CLAIM

## Asset register
| Asset | ID | Required validation |
|---|---|---|
| World Gateway | WORLD-GATEWAY-01 | visual identity, provenance, rights |
| Advanced Mobility aircraft | biu-veh-air-001 | concept label, provenance, rights |
| Marine hydrofoil | biu-veh-marine-001 | research-concept label, provenance, rights |
| Smart farming vehicle | biu-veh-agri-001 | research-prototype label, provenance, rights |
| Conservation vehicle | biu-veh-offroad-001 | concept label, provenance, rights |
| AI/robotics vehicle | biu-veh-ai-001 | research-concept label, provenance, rights |
| Biupiu logo/identity | BIUPIU-BRAND-01 | approved brand source |
| Environment scenes | AIR-01/MAR-01/AGR-01/CONS-01/AI-01 | original/licensed source |

## Validation sequence
SOURCE → PROVENANCE → RIGHTS → CLAIM STATUS → VISUAL IDENTITY → TECHNICAL QUALITY → SAFE AREA → RENDER → HUMAN REVIEW → RELEASE

## Technical render targets
- Master: 16:9 cinematic render
- Vertical: 9:16
- Campaign: 4:5
- Trailer: 30 seconds
- Teaser: 15 seconds
- Department cutdowns: approximately 20 seconds each
- Still hero frames for every department

## Mandatory checks
- No unlicensed game/mod assets.
- No extracted proprietary game assets.
- Concept visuals retain appropriate claim labels.
- Logo and typography remain legible.
- PBR/material treatment remains coherent across scenes.
- No accidental watermarks or source-platform UI.
- Camera continuity is consistent with SF-22/SF-25.
- Third-party permissions are documented before publication.

## Release states
BLOCKED → VALIDATION_REQUIRED → RENDER_READY → HUMAN_REVIEW → APPROVED_FOR_ASSEMBLY → PUBLISHED

No asset may enter APPROVED_FOR_ASSEMBLY solely because it looks correct; provenance and rights must also be cleared.
