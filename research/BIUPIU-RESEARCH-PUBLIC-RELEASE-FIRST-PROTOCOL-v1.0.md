# Biupiu Research Protocol: Public Release First v1.0

Date: 19 September 2026

## Purpose
Prevent wasted research cycles when an official vendor/project has already publicly released source, binaries, SDKs, firmware, specifications, historical dumps or architecture material.

## Discovery sequence
1. Official vendor/project release pages and public repositories.
2. Official archives, historical repositories and publicly documented source dumps.
3. Standards/specification repositories.
4. Authoritative open-source projects.
5. Secondary/community projects only when they provide missing implementation evidence.

## Evidence classes
PUBLIC-OFFICIAL-SOURCE
PUBLIC-OFFICIAL-BINARY
PUBLIC-HISTORICAL-DUMP
OFFICIAL-SPECIFICATION
OPEN-SOURCE-REFERENCE
COMMUNITY-REFERENCE
UNVERIFIED

## Reuse decision
- PUBLIC-OFFICIAL-SOURCE: index immediately; reuse only after applicable licence/terms and technical compatibility are recorded.
- PUBLIC-OFFICIAL-BINARY: use for compatibility testing where permitted; do not reverse engineer or redistribute beyond applicable rights.
- PUBLIC-HISTORICAL-DUMP: index and study; provenance and rights are recorded separately.
- OFFICIAL-SPECIFICATION: architectural reference.
- OPEN-SOURCE-REFERENCE: candidate implementation subject to licence/security/dependency review.
- COMMUNITY-REFERENCE: research only until independently validated.

## Current examples
Microsoft's MS-DOS archive publicly provides historical MS-DOS 1.25/2.0/4.0 source and binaries under MIT, but it is explicitly historical and archived. DOS-History publicly maintains reconstructed/preserved early DOS repositories. DOSBox-X publicly provides source and cross-platform releases. TianoCore EDK II is a public cross-platform UEFI/PI development environment with a documented BSD-2-Clause Plus Patent base and additional component licences.

These sources should therefore enter the research pipeline immediately rather than waiting for a generic open-source search.

## Rule
Licence verification becomes a targeted reuse gate, not a discovery gate. Never claim that public availability alone makes every use unrestricted.
