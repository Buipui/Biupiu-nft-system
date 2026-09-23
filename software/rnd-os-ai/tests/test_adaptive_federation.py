from biupiu_ai.adaptive_federation import (
    CapabilityEvidence, ExecutionPath, ModuleContract, ModuleState,
    ResourceSnapshot, compatibility_manifest, record_telemetry, select_path,
)


def evidence(*paths, capabilities=("render",)):
    return CapabilityEvidence(
        capabilities=frozenset(capabilities),
        validated_paths=frozenset(paths),
        provenance_verified=True,
        regression_passed=True,
        safety_passed=True,
    )


def test_passive_manifest_does_not_activate_modules():
    module = ModuleContract("twin.render", ("render",), (ExecutionPath.GPU, ExecutionPath.CPU))
    manifest = compatibility_manifest([module], {"twin.render": evidence(ExecutionPath.GPU, ExecutionPath.CPU)})
    assert manifest[0].state is ModuleState.PASSIVE


def test_missing_capability_fails_closed():
    module = ModuleContract("twin.ai", ("inference",), (ExecutionPath.NPU, ExecutionPath.CPU))
    decision = select_path(module, ResourceSnapshot(), evidence(ExecutionPath.CPU))
    assert decision.state is ModuleState.DEGRADED
    assert decision.reason == "capability-missing"


def test_validated_path_is_selected_by_resource_pressure():
    module = ModuleContract("twin.render", ("render",), (ExecutionPath.GPU, ExecutionPath.CPU))
    snapshot = ResourceSnapshot(cpu=.8, gpu=.2)
    decision = select_path(module, snapshot, evidence(ExecutionPath.GPU, ExecutionPath.CPU))
    assert decision.state is ModuleState.ACTIVE
    assert decision.path is ExecutionPath.GPU


def test_unverified_provenance_never_activates():
    module = ModuleContract("twin.ai", ("inference",), (ExecutionPath.NPU, ExecutionPath.CPU))
    ev = CapabilityEvidence(capabilities=frozenset({"inference"}),
                            validated_paths=frozenset({ExecutionPath.NPU, ExecutionPath.CPU}),
                            provenance_verified=False, regression_passed=True, safety_passed=True)
    decision = select_path(module, ResourceSnapshot(npu=.1), ev)
    assert decision.state is ModuleState.DEGRADED


def test_telemetry_is_bounded_and_correlated():
    module = ModuleContract("twin.render", ("render",), (ExecutionPath.GPU,))
    decision = select_path(module, ResourceSnapshot(gpu=.1), evidence(ExecutionPath.GPU))
    event = record_telemetry(decision, latency_ms=4.5, resource_pressure=.1,
                             success=True, correlation_id="trace-001")
    assert event.correlation_id == "trace-001"
    assert event.success
