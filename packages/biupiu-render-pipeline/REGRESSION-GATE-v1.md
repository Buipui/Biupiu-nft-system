# Render Pipeline Regression Gate v1

Every change touching the render pipeline, access contracts or render runtime contracts should pass JSON validation and architectural invariant checks.

The gate verifies:
- contracts remain valid JSON
- server authority and secret isolation remain declared
- provenance remains required
- entitlement/default-deny safeguards remain present
- recovery remains bounded and reviewable

This is a structural regression gate; provider credentials and external services are never required for this CI check.