# Biupiu R&D OS — Cross-Platform Resource Registry v1.0

Updated: 19 September 2026

## Purpose

Curate reusable technology and research references for the Windows + macOS + Linux + Android R&D OS without silently copying third-party code or assets.

## Cross-platform foundations

| Resource | Role | Treatment |
|---|---|---|
| Tauri 2 | desktop/mobile application shell | integration candidate; licence/release review |
| Electron | Windows/macOS/Linux desktop reference | integration candidate/reference |
| OpenUSD | cross-application 3D interchange | external dependency/reference |
| OpenSubdiv | geometry processing | external dependency/reference |
| NASA OSAL | OS abstraction and portability patterns | research/reference |
| NASA GMAT | multi-platform engineering/simulation reference | external open-source candidate |
| NASA Ziggy | reproducible pipeline orchestration | research/reference |
| Code-Cortex-MCP | repository knowledge graph/code indexing | discovery candidate; licence review |
| enowx-rag | local/remote RAG and MCP architecture | discovery candidate; licence review |

## NASA

NASA software records have different release classes, so every NASA item must retain its release type and commercial-use restrictions. GMAT R2026 is listed for Windows, Linux and macOS. NASA OSAL documents an abstraction layer for portability, while Ziggy provides persisted pipeline metadata and provenance.

## MIT

Relevant MIT/CSAIL resources include Drake for model-based robotics, deployable-ML research, distributed robotics, robot planning and open-source robotics work. Repository-specific licences must be checked before incorporation.

## ResearchGate

Use ResearchGate as a literature-discovery and cross-reference layer. Prefer DOI or publisher versions where available. ResearchGate records are discovery/evidence records, not automatic software licences.

## Emerald Insight

Use Emerald Insight as a scholarly discovery layer for software engineering, information systems, AI, interoperability and engineering-management literature. No Emerald paper is treated as an implementation dependency unless the publication, rights and any associated software licence are separately verified.

## Declassified/public records

Use official released records for historical architecture and security lessons. Declassified status does not automatically grant software copyright or reuse rights.

## Patents / expired rights

Patent records are prior-art and freedom-to-operate inputs, not software libraries. Expiration must be verified per jurisdiction and patent family. No patent is classified as expired solely from age.

## GitHub

Every implementation candidate receives repository URL, commit/tag, licence, dependency status, platform support, security status, intended adapter and import/reference decision.

## Integration policy

DISCOVERED -> PROVENANCE_CHECK -> LICENCE_CHECK -> SECURITY_CHECK -> PLATFORM_CHECK -> ISOLATED_ADAPTER -> TEST -> APPROVED_REFERENCE/DEPENDENCY

Third-party code is not copied into the repository merely because it is public on GitHub.

## Source classes

OFFICIAL_OPEN_SOURCE
OFFICIAL_PUBLIC_DOCUMENTATION
SCHOLARLY_DISCOVERY
DECLASSIFIED_PUBLIC_RECORD
PATENT_PRIOR_ART
COMMUNITY_REPOSITORY
PROPRIETARY_REFERENCE

The AI must preserve the source class and never convert a discovery result into an ownership claim.
