# AI-12 — Production Model Adapter, Retrieval Benchmark & Mobile Test

## Implemented foundation
- retrieval benchmark with expected-source recall scoring
- automated benchmark test

## Production requirements
A production model adapter and end-to-end Android test remain gated on selecting a provider, configuring secure authentication, defining privacy controls, and validating latency, cost, grounding, refusal behavior and failure handling.

## Acceptance criteria
- measurable retrieval recall and source attribution
- no secrets in mobile source code
- authenticated transport
- offline and network-failure handling
- human review for consequential research actions

## Next gate
AI-13: provider adapter evaluation and end-to-end integration test.
