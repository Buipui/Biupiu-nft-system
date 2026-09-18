# AI-11 — Model Adapter & Grounding Evaluation

## Objective
Create a controlled model-provider boundary and an evaluation harness for evidence grounding.

## Implemented
- evaluation-case schema
- source-grounding evaluator
- expected evidence-state comparison
- configured provider boundary
- fail-closed development fallback
- automated grounding tests

## Evaluation dimensions
1. Expected source coverage
2. Evidence-state correctness
3. Missing-source detection

## Production boundary
The configured provider reads model configuration from environment variables. No API keys or credentials are committed to the repository. The current fallback remains deterministic until a production model adapter is explicitly configured and evaluated.

## Next gate
AI-12: production model adapter, retrieval benchmark and end-to-end mobile AI test.
