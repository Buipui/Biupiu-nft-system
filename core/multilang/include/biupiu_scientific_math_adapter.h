#pragma once
#include <cstdint>
namespace biupiu::scientific {
enum class Provider : std::uint8_t { Native=0, Eigen=1, Gsl=2 };
struct Capability { bool eigen_available; bool gsl_available; Provider selected; };
struct VectorStats { double l2_norm; double dot_self; };
Capability capability();
VectorStats vector_stats(const double* values, std::int32_t count);
}