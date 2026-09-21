# Specialist Federation Gate 5 — Learning/Provenance Integration

Status: IMPLEMENTED + REPOSITORY-VERIFIED

Gate 5 connects specialist results to the existing deterministic learning architecture. Results are converted into learning events carrying evidence class, drift status, regression status, validation status and provenance state. Unvalidated outputs remain candidates; only validated, provenance-complete results with acceptable drift/regression status enter the promotion queue.

The bridge deliberately does not execute third-party ML packages or silently promote models. It provides the contract between resident specialist AIs, the existing learning core, evidence/provenance, and the human-controlled promotion gate.

Repository evidence recovered during this gate confirms the existing learning core has CI verification and already defines failure fingerprints, EWMA drift detection, candidate scoring, provenance/licence/human promotion checks, plus the learning pipeline from evidence/provenance through evaluation/drift and OS validation.