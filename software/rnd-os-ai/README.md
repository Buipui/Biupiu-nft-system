# Biupiu R&D OS AI Core

Development foundation for the Intelligence Layer.

## Design
The AI core is provider-agnostic. The application supplies structured R&D context; the provider returns structured assistant output. Durable research changes are validated by the R&D OS API rather than written directly by the model.

## Planned modules
- provider interface
- prompt/context assembly
- repository retrieval adapter
- evidence-aware response schema
- agent router
- experiment-generation adapter
- audit/event adapter

## Gate AI-01
This directory currently defines the implementation boundary. Provider credentials, production model selection and production deployment are intentionally not hard-coded.

## SELF-HEAL-01 — Intelligence Integration Contract

Biupiu AI includes a bounded failure-learning/self-healing controller linked to the existing learning/provenance layer. It may identify failures, select approved remediation rules, run repairs through an injected host executor, verify results and record outcomes.

The controller cannot grant itself new privileges, bypass protected-file checks, omit required regression tests for code patches, or promote production changes without the OS approval boundary.

SELF-HEAL-01: IMPLEMENTED — feature branch pending mainline verification.