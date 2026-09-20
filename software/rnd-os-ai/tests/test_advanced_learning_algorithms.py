from biupiu_ai.ml.continual_adaptation import blend_predictions, reference_anchored_parameter_update
from biupiu_ai.ml.quantum_ml import fidelity_quantum_kernel, kernel_nearest_label, quantum_kernel_matrix

def test_reference_anchored_update_is_bounded():
    out = reference_anchored_parameter_update(
        {"w": 1.0}, {"w": 1.0}, {"w": 100.0},
        learning_rate=1.0, anchor_strength=0.0, max_step=0.05,
    )
    assert abs(out["w"] - 1.0) <= 0.05

def test_teacher_weight_is_reduced_by_drift():
    low = blend_predictions([0.1,0.9],[0.2,0.8],teacher_confidence=1.0,drift_score=0.0)
    high = blend_predictions([0.1,0.9],[0.2,0.8],teacher_confidence=1.0,drift_score=2.0)
    assert high.adaptation_weight < low.adaptation_weight
    assert high.rollback_required is False

def test_quantum_kernel_is_symmetric_and_bounded():
    a = [0.1, 0.4]
    b = [0.7, -0.2]
    assert 0.0 <= fidelity_quantum_kernel(a,b) <= 1.0
    assert fidelity_quantum_kernel(a,b) == fidelity_quantum_kernel(b,a)
    m = quantum_kernel_matrix([a,b])
    assert m[0][1] == m[1][0]

def test_quantum_kernel_baseline_classifier():
    label = kernel_nearest_label([[0.0,0.0],[3.0,3.0]],["A","B"],[0.1,0.1])
    assert label == "A"
