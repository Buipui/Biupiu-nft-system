# AI-10 — Model Integration & Evidence-Grounded Feedback

## Objective
Create the provider boundary that lets a real AI model reason over versioned experiment data and evidence without treating model output as evidence.

## Flow
VERSIONED DATASET + EVIDENCE → CONTEXT BUILDER → MODEL PROVIDER → STRUCTURED AI RESULT → CITATIONS / EVIDENCE STATE

## Implemented foundation
- grounded context object
- model-provider interface
- deterministic development provider
- grounded AI service
- automated tests

## Grounding rules
- No evidence or dataset context → insufficient-evidence state.
- Retrieved evidence remains attributable through source IDs.
- Versioned datasets remain identifiable.
- Model output remains model output and does not automatically become evidence.

## Production model boundary
A live cloud or local model can be plugged into the provider interface without changing research data contracts. Production deployment requires secrets management, model selection, rate limits, privacy controls and evaluation.

## Next gate
AI-11: live model adapter + retrieval/grounding evaluation harness.
