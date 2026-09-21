from biupiu_ai.compute_federation import ComputeClass, ComputeUnit, HostTopology, Workload
from biupiu_ai.federated_machine_runtime import FederatedMachineRuntime
from biupiu_ai.machine_capability import MachineCapability, Transport

def runtime():
    return FederatedMachineRuntime(HostTopology(
        "Biupiu-test", "x86_64",
        (ComputeUnit("cpu-p", ComputeClass.PERFORMANCE, 2.0),
         ComputeUnit("gpu-0", ComputeClass.GPU, 8.0)),
    ))

def test_capability_validation_is_fail_closed():
    rt = runtime()
    rt.register_capability(MachineCapability(
        "vehicle.coolant_temperature", "temperature", "degC",
        Transport.VIRTUAL, minimum=-40, maximum=150,
    ))
    assert rt.validate_capability("vehicle.coolant_temperature", 90).accepted
    rejected = rt.validate_capability("vehicle.coolant_temperature", 180)
    assert not rejected.accepted
    assert rejected.reason == "above-range"

def test_validated_machine_workload_uses_gpu():
    rt = runtime()
    rt.register_capability(MachineCapability(
        "machine.load", "load", "percent", Transport.VIRTUAL,
        minimum=0, maximum=100,
    ))
    assert rt.validate_capability("machine.load", 50).accepted
    result = rt.dispatch(
        Workload("physics", 10, preferred=(ComputeClass.GPU,), minimum=(ComputeClass.GPU,)),
        lambda work, unit: (work.workload_id, unit.unit_id),
    )
    assert result == ("physics", "gpu-0")
