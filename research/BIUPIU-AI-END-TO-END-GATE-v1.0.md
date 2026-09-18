# AI-13 — Provider Adapter Boundary & End-to-End Grounding Gate

## Executed foundation

- provider adapter contract with explicit configuration state
- fail-closed provider boundary that does not fabricate remote model output
- deterministic end-to-end test through retrieval benchmark → evidence context → grounded AI service
- automated tests covering disabled-provider behavior and citation propagation

## Security boundary

- API secrets are represented only by environment-variable names
- no API keys or credentials are stored in source code
- remote transport is not claimed to be production-ready
- provider-specific network code remains a separate implementation boundary

## Acceptance criteria

1. Retrieval recall is measurable.
2. Evidence source IDs propagate into model results.
3. Missing provider configuration fails closed.
4. Mobile/client code does not contain provider secrets.
5. A real provider adapter is only enabled after authenticated transport, privacy controls, rate/cost controls, timeout/retry handling and refusal/failure evaluation are implemented.

## Verification status

**Implemented:** repository-level adapter boundary and deterministic end-to-end grounding test.

**Not yet implemented:** live external model transport and real Android end-to-end network test.

## Next gate

AI-14: secure provider implementation test harness and mobile API contract validation.
