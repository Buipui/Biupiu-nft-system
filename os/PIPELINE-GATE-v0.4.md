# Biupiu OS Pipeline Gate v0.4

The kernel now supports controlled multi-module execution with:
- input/output schema guards,
- deterministic state passing,
- pipeline stop-on-failure,
- provenance propagation,
- evidence-state governance across every stage.

The included material/load modules are synthetic smoke-test models only. They demonstrate pipeline mechanics and must not be treated as engineering validation.

Next verification target: run the complete CI suite, then adapt an existing real Biupiu simulator to this contract and compare its outputs against its existing tests.
