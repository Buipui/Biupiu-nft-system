# Research Library Gate 2 — Live Source Harvester

Date: 2026-09-19

## Purpose
Upgrade the reference library from a static harvest into a refreshable, provenance-first scholarly intake layer.

## Source pipeline
1. Crossref REST API — DOI metadata, dates, licences and updates.
2. OpenAlex — scholarly discovery and open-access location data.
3. Publisher/repository landing page — final licence and file verification.
4. Popular Mechanics — secondary discovery/reference only.
5. InvestSA — government-sector/investment reference routing.

Crossref's public REST API exposes scholarly metadata including licence information and supports filters for dates and other properties. Open-access discovery should use OpenAlex/Unpaywall-style OA metadata, followed by direct publisher/repository verification.

## Promotion states
DISCOVERED -> METADATA_VERIFIED -> OA_VERIFIED -> LICENCE_VERIFIED -> ROUTED -> DOWNLOAD_ELIGIBLE -> DOWNLOADED -> CONTENT_VALIDATED -> IMPLEMENTATION_CANDIDATE

## Safety / provenance
- Never bypass paywalls, login controls, robots restrictions or technical access controls.
- Never treat a DOI record as proof that the full text is legally downloadable.
- Preserve DOI, publisher URL, repository URL, licence, retrieval date and checksum when a file is legally downloaded.
- Store one canonical record and route it to multiple departments through references.

## Department routing
Commercial: AGRI, HEMP, TEXTILES, ADVANCED_MATERIALS, ROBOTICS, MANUFACTURING, CAD_SIM, DIGITAL_TWIN, AI_OS, ENERGY, INVESTSA.
Personal: AERO, ADVANCED_ENERGY, QUANTUM_MATERIALS, PHOTONICS, SPECULATIVE_PHYSICS and other explicitly isolated R&D.

## Next implementation gate
Add scheduled metadata refresh, DOI/OA verification, duplicate detection, licence capture, checksum/provenance records and department queue generation. Do not auto-promote research into production code or product designs.
