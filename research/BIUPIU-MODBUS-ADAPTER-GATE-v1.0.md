# Biupiu Modbus Adapter Gate v1.0

**Status:** Repository implementation complete; live Modbus execution pending.

The adapter maps Modbus TCP onto the canonical Machine Capability contract.

Controls:
- explicit host, port, unit ID and register mapping;
- no register inference;
- missing pymodbus dependency fails closed;
- connection failures fail closed;
- READ_ONLY capabilities cannot write;
- read errors are surfaced rather than silently accepted.

Live evidence must record device/server identity, unit ID, register map, function codes, timestamps, byte/word encoding where relevant, errors, retry behaviour and reproducible test conditions.

No physical Modbus device was connected during this repository execution.
