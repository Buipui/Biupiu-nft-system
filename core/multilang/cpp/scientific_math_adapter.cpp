#include "biupiu_scientific_math_adapter.h"
#include <cmath>
#include <stdexcept>
#if __has_include(<Eigen/Core>)
#define BIUPIU_HAS_EIGEN 1
#include <Eigen/Core>
#else
#define BIUPIU_HAS_EIGEN 0
#endif
#if __has_include(<gsl/gsl_blas.h>) && __has_include(<gsl/gsl_vector.h>)
#define BIUPIU_HAS_GSL 1
#include <gsl/gsl_blas.h>
#include <gsl/gsl_vector.h>
#else
#define BIUPIU_HAS_GSL 0
#endif
namespace biupiu::scientific {
Capability capability() {
#if BIUPIU_HAS_EIGEN
 return {true, BIUPIU_HAS_GSL != 0, Provider::Eigen};
#elif BIUPIU_HAS_GSL
 return {false, true, Provider::Gsl};
#else
 return {false, false, Provider::Native};
#endif
}
VectorStats vector_stats(const double* values, std::int32_t count) {
 if (values == nullptr || count < 0) throw std::invalid_argument("invalid scientific vector");
 if (count == 0) return {0.0,0.0};
#if BIUPIU_HAS_EIGEN
 Eigen::Map<const Eigen::VectorXd> v(values, count);
 const double d=v.dot(v); return {std::sqrt(d),d};
#elif BIUPIU_HAS_GSL
 gsl_vector_const_view view=gsl_vector_const_view_array(values, static_cast<std::size_t>(count));
 double d=0.0;
 if(gsl_blas_ddot(&view.vector,&view.vector,&d)!=GSL_SUCCESS) throw std::runtime_error("GSL dot product failed");
 return {std::sqrt(d),d};
#else
 double d=0.0; for(std::int32_t i=0;i<count;++i) d+=values[i]*values[i];
 return {std::sqrt(d),d};
#endif
}
}