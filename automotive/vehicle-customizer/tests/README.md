# Vehicle Customizer Preliminary Tests

## Gate A — Schema
Verify every vehicle has a Twin ID, base vehicle, part records, material records, performance state and provenance.

## Gate B — Compatibility
Reject incompatible parts and missing attachment points before applying a configuration.

## Gate C — Reversibility
Every configuration change must be undoable by restoring a prior revision.

## Gate D — Simulation sanity
Flag impossible or suspicious values such as negative mass, invalid gear ratios, impossible wheel clearance or non-finite aerodynamic values.

## Gate E — Asset provenance
Reject assets without licence/provenance metadata from commercial-ready builds.

## Gate F — Isolation
Third-party code is kept in an external/reference namespace until licence, dependency and security review passes.

## Result
The current prototype is a development tool, not an engineering certification system. Real vehicles require professional engineering validation and applicable regulatory testing.
