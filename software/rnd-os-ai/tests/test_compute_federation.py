from biupiu_ai.compute_federation import ComputeClass, ComputeFederation, ComputeUnit, HostTopology, Workload

def test_heterogeneous_capacity_aware_plan():
    topology = HostTopology("Biupiu-discovered", "x86_64", (
        ComputeUnit("cpu-p", ComputeClass.PERFORMANCE, 2.0),
        ComputeUnit("cpu-e", ComputeClass.EFFICIENCY, 1.0),
        ComputeUnit("gpu-0", ComputeClass.GPU, 8.0),
    ))
    plan = ComputeFederation(topology).plan([
        Workload("physics", 8, preferred=(ComputeClass.GPU, ComputeClass.PERFORMANCE)),
        Workload("ui", 2, minimum=(ComputeClass.EFFICIENCY, ComputeClass.PERFORMANCE)),
    ])
    assert plan["physics"] == "gpu-0"
    assert plan["ui"] in {"cpu-p", "cpu-e"}

def test_required_accelerator_fails_closed():
    topology = HostTopology("unknown", "arm64", (ComputeUnit("cpu", ComputeClass.PERFORMANCE),))
    try:
        ComputeFederation(topology).plan([Workload("npu-required", 1, minimum=(ComputeClass.NPU,))])
    except RuntimeError as exc:
        assert "npu-required" in str(exc)
    else:
        raise AssertionError("missing required accelerator must fail closed")
