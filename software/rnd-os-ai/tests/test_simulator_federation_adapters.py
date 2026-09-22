"""Source-level smoke tests for the federated simulator adapter registry."""
from software.rnd_os_ai.src.simulator_adapters import (
    CHRONO, ENERGYPLUS, OPENSTUDIO, OPENSIM, backend_matrix,
)


def test_registered_backends_are_fail_closed():
    matrix = backend_matrix()
    assert set(matrix) == {"gazebo", "chrono", "openstudio", "energyplus", "opensim"}
    for result in matrix.values():
        assert result.status in {"ready", "not-installed"}
        assert result.available == (result.executable is not None)


def test_adapter_command_rejects_unsafe_arguments():
    for adapter in (CHRONO, OPENSTUDIO, ENERGYPLUS, OPENSIM):
        try:
            adapter.command("\x00")
        except ValueError:
            pass
        else:
            raise AssertionError(f"{adapter.backend} accepted a NUL byte")
