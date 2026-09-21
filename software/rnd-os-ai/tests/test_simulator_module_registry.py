from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from simulator_module_registry import activation_candidates, module_matrix


def test_discovered_modules_are_registered_without_activation():
    matrix = module_matrix()
    assert {"gazebo", "mujoco", "openusd", "3dgs"} <= set(matrix)
    assert all(not item.executable_activation for item in matrix.values())


def test_external_activation_is_fail_closed():
    assert activation_candidates() == ()


def test_all_modules_have_promotion_gates():
    for module in module_matrix().values():
        assert {"provenance", "licence", "dependency", "security"} <= set(module.required_gates)
