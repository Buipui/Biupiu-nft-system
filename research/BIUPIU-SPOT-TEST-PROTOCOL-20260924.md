# Biupiu Spot-Test Protocol — 2026-09-24

## Scope
Controlled spot-test of currently executable/source-verifiable Biupiu components after the Quantum AI information-stack update.

## Environment
- Local execution environment: Linux container
- Repository clone: unavailable because external GitHub network resolution is unavailable in this execution environment.
- Therefore tests below were executed against source reconstructed from the exact repository content returned by the GitHub connector, not against a full local checkout.
- No Android device, Windows host, UE5/GPU host, physical hardware or QPU was activated.

## Protocol
1. Verify provider registry cardinality and identities.
2. Verify Quantum AI fail-closed policy.
3. Verify capability routing does not enable hardware.
4. Verify Federation preferred-class ordering.
5. Verify Federation minimum-class filtering.
6. Measure deterministic call/planning overhead.
7. Check current CI evidence for the resulting branch.
8. Record every non-executable gate explicitly rather than infer completion.

## Measured results

### Quantum provider registry
- Iterations: 10,000
- Failures: 0
- Mean registry-call time: 104.8 ns
- P95: 120.0 ns
- Minimum: 90 ns
- Maximum: 28,954 ns
- Result: PASS

Assertions:
- 8 registered provider boundaries: PASS
- All providers hardware_enabled=False: PASS
- execution_policy=SIMULATOR_VALIDATE: PASS
- learning_mode=PASSIVE_OBSERVATION: PASS
- promotion_state=REFERENCE_ONLY: PASS
- QNN capability routes only Qiskit/PennyLane: PASS
- Hardware-capable declarations remain non-executing: PASS

### Compute Federation scheduler
- Iterations: 5,000
- Failures: 0
- Mean planning time: 2,962.6 ns
- P95: 2,975.0 ns
- Minimum: 2,664 ns
- Maximum: 51,899 ns
- Result: PASS

Assertions:
- Ordered GPU preference over PERFORMANCE CPU: PASS
- Ordered NPU preference over GPU: PASS
- Minimum GPU constraint: PASS

## Current benchmark baseline
The existing Baseline A remains authoritative for its own harness:
- L0: 10,000 iterations, 0 failures, mean 7.5331269 us, P95 6.866 us
- L1: 5,000 iterations, 0 failures, mean 6.781629 us, P95 6.850 us
- L2: 3,000 iterations, 0 failures, mean 7.5321717 us, P95 7.262 us
- L3: 2,000 iterations, 0 failures, mean 7.5305965 us, P95 7.109 us
- L4: 1,000 iterations, 0 failures, mean 7.0815400 us, P95 7.114 us
- Existing geometry invariance checks: PASS
- Existing QPU activation: DISABLED

The new spot measurements are not substituted for Baseline A because they measure different operations.

## CI / runtime evidence
- Latest Quantum AI branch commit had no associated pull-request workflow runs exposed by the GitHub API at test time.
- Consequently CI PASS is not claimed.

## Outstanding runtime-dependent gates
These remain OPEN because the required execution environment was not available:
- Full repository test suite
- Remote CI execution
- Android Gradle/SDK/device execution
- Windows PC build/runtime
- UE5/GPU runtime
- NPU/GPU/DSP hardware execution
- Digital Twin live runtime
- HIL/physical validation
- Cloud/QPU execution
- Physical quantum validation
- Production promotion

## Gate rule
SOURCE IMPLEMENTED != TEST EXECUTED != CI VERIFIED != RUNTIME VERIFIED != PHYSICALLY VERIFIED.

## Result
**SPOT-TEST PASS for executable isolated Quantum provider and Compute Federation checks.**
**OUTSTANDING ENVIRONMENT-DEPENDENT TESTS remain OPEN.**
No unsupported gate closure was made.
