# OS-G03 Scheduler / Process Contract v1.0
Status: CONTRACT IMPLEMENTED; runtime OPEN

Define process states NEW, READY, RUNNING, BLOCKED, TERMINATED; priority/quantum fields; context ownership; PID lifecycle; and scheduler invariants. The scheduler must not expose direct hardware mutation to higher services. Initial target: x86_64 VM/hosted harness; ARM64/RISC-V64 adapters later.