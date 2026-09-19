from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from simulator_adapters import SimulatorAdapter, backend_matrix


def test_missing_backend_is_fail_safe():
    result = SimulatorAdapter("missing", "__biupiu_missing_executable__").probe()
    assert not result.available
    assert result.status == "not-installed"
    assert result.command == ()


def test_nul_arguments_are_rejected():
    adapter = SimulatorAdapter("python", "python")
    try:
        adapter.command("bad\x00argument")
    except ValueError:
        return
    raise AssertionError("NUL argument was accepted")


def test_non_string_arguments_are_rejected():
    adapter = SimulatorAdapter("python", "python")
    try:
        adapter.command("--ok", 123)
    except TypeError:
        return
    raise AssertionError("non-string argument was accepted")


def test_invalid_adapter_definition_is_rejected():
    try:
        SimulatorAdapter("", "python")
    except ValueError:
        return
    raise AssertionError("empty backend definition was accepted")


def test_backend_matrix_has_safe_statuses():
    matrix = backend_matrix()
    assert set(matrix) == {"gazebo"}
    assert matrix["gazebo"].status in {"ready", "not-installed"}
