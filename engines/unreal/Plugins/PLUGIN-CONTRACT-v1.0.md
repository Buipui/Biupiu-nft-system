# UE5 Plugin Contract v1.0

Biupiu plugins must remain modular and avoid embedding research claims directly into presentation code.

Required practices:
- versioned interfaces
- explicit dependencies
- schema compatibility checks
- provenance identifiers for imported research/3D assets
- platform capability checks
- deterministic test fixtures where practical
- no secrets or private keys in source

Scientific/engineering validation remains external to the visualization layer.
