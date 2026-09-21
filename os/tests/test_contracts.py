import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT))
from biupiu_os import SimulationRequest,validate_request,system_health,BiupiuKernel
from biupiu_os.adapters import default_adapters

def test_request_contract():
    req=validate_request(SimulationRequest("demo",{"mass_kg":10}))
    assert req.module=="demo"

def test_adapter_boundary_fails_closed():
    adapter=default_adapters()[0]
    assert adapter.health()["runtime_available"] is False
    try: adapter.execute({})
    except RuntimeError as exc: assert "runtime is not installed" in str(exc)
    else: raise AssertionError("adapter must not pretend external runtime exists")

def test_system_health():
    h=system_health(BiupiuKernel(ROOT))
    assert h["verification_policy"]["validated_requires_measurement"] is True
    assert len(h["adapters"]) >= 6
