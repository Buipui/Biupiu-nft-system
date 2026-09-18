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
