# Biupiu OS Execution Gate v0.3

The kernel can now discover a simulator, load it through an isolated module boundary, locate its `run` or `execute` entrypoint, execute it through the kernel, apply evidence governance, and record the result.

A controlled smoke module is included for regression testing.

Failure policy: simulator exceptions are captured as failed execution records rather than crashing the kernel. Validation/certification claims remain guarded by measured-evidence and review requirements.

This gate proves orchestration mechanics only. It does not validate any scientific model or external engine.
