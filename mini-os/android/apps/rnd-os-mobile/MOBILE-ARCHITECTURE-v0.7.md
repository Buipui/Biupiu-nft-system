# Biupiu R&D OS Mobile Architecture v0.7

## Purpose

Define the Android application layer for the Biupiu R&D OS without duplicating the server/domain system.

The mobile application is a client of the R&D OS API, not a replacement for the research repository, server, database or Experimental Control Centre.

## Architecture

Android App → Compose UI → Navigation/ViewModels → API repository → HTTPS/API → Biupiu R&D OS Core → PostgreSQL/object storage/AI/simulation/digital-twin connectors.

Device capabilities: camera, files, sensors and notifications.

## Initial screens

1. Sign-in / session
2. Dashboard
3. Projects
4. Research Objects
5. Hypotheses
6. Experimental Control Centre
7. Experiments
8. Evidence capture
9. Failures & Lessons
10. Knowledge Graph
11. IP / confidentiality status
12. Settings / organisation

## Mobile-first capabilities

- Fast experiment creation.
- Photograph/video evidence capture.
- Measurement notes.
- Offline draft queue with explicit sync status.
- Search across authorised tenant data.
- QR/code scanning can later identify experiments, equipment and samples.
- Push notifications can later surface review, replication and approval tasks.

## Security model

The app must never trust a client-supplied organisation identifier. The authenticated API session determines organisation scope and permissions. Sensitive IP and confidential research must be controlled server-side.

## Offline states

- DRAFT_LOCAL
- QUEUED_FOR_SYNC
- SYNCED
- SYNC_CONFLICT
- SYNC_REJECTED

A failed sync must never silently overwrite server research.

## API boundary

The app uses the existing R&D OS API rather than directly accessing PostgreSQL.

Planned services: AuthService, ProjectService, ResearchService, ExperimentService, EvidenceService, KnowledgeGraphService and PackageService.

## Version gates

v0.7: Android foundation, Compose UI shell, navigation and API abstraction.
v0.8: authenticated API session and dashboard data.
v0.9: research/experiment creation, evidence capture and offline queue.
v1.0: knowledge graph, AI assistant entry point, robust sync and production security review.

## Boundary

This is an engineering foundation. It is not a production-ready mobile security implementation, regulated laboratory application or Google Play readiness claim.
