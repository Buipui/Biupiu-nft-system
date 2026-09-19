# Biupiu Microsoft Discovery Integration v1.0
Date: 2026-09-19
Status: IMPLEMENTED — verification pending

Biupiu adopts compatible architectural patterns from Microsoft's public Discovery project without copying third-party source code.

Adapted patterns:
- research task DAG with explicit dependencies and readiness/blocked states
- explicit task lifecycle including stale, incomplete and failure states
- specialist agent registration by domain
- tool/capability registration
- autonomy and human-approval policy boundary
- governed external-resource incorporation
- graph-based research orchestration

Routing: Research question -> Intelligence Orchestrator -> Task Graph -> Retrieval/Evidence -> Specialist Agent/Tool -> Evaluation -> Learning Memory -> OS validation -> promotion.

Integration: Intelligence owns orchestration; AI OS exposes model/tool adapters; Main/OS owns validation and authoritative state; Biupiu OS remains the stable system-of-record/platform boundary.

Microsoft Discovery remains an external reference. Individual code/components require licence, provenance, security and compatibility review before incorporation.

The new Python module was committed to main. Runtime test execution is not claimed by this gate; local CI is the next verification step.
