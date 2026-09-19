# Biupiu Robotics / MoveIt 2 Adapter Contract v1.0

Architecture:
BIUPIU ROBOT MODEL -> STATE -> MATH/GEOMETRY -> MOVEIT 2 -> TRAJECTORY -> DIGITAL TWIN -> VALIDATION

MoveIt 2 is retained as an external ROS 2 dependency. The adapter records model, joint state, target pose, collision model, planner, constraints, solver and simulation versions.

The adapter produces trajectory candidates for simulation and validation. It does not directly command physical actuators.

Promotion:
DISCOVERED -> ADAPTER_DEFINED -> DEPENDENCY_REVIEW -> SIMULATION_TEST -> VALIDATED
