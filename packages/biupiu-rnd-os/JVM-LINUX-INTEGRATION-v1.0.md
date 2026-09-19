# Biupiu R&D OS — JVM + Linux Integration v1.0

Java is an optional first-class execution/runtime layer for cross-platform scientific tools, robotics/simulation adapters, data processing, NASA/space-science resources, JVM-compatible services and Gradle builds.

Java does not replace the TypeScript core.

Linux is a first-class target for development/CI, scientific/HPC workloads, server-side AI/RAG services, robotics/device integration, containers and POSIX adapters.

## Build contract
Use Gradle Wrapper for reproducible JVM builds:
- Linux/macOS: ./gradlew
- Windows: gradlew.bat

## NASA Java references
- GMAT R2026: Windows/Linux/macOS with Java/Python interfaces.
- NASA World Wind Java: 3D/geospatial Java reference.
- NASA PDS4 Java Library and Tools: Java data tooling.
- NASA OpenVSP3Plugin: Mac/Linux/Windows Java integration reference.

## Integration boundary
TypeScript, Java, Rust and Python communicate through stable contracts, CLI processes, local IPC or HTTP/MCP services. No language directly depends on another language's internal implementation.

## Exit criteria
Compilation, tests, platform smoke test, dependency/licence scan, provenance record and CI execution.
