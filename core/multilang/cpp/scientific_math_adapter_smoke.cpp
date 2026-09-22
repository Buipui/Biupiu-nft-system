#include "biupiu_scientific_math_adapter.h"
#include <cassert>
int main(){ const double values[]={3.0,4.0}; const auto caps=biupiu::scientific::capability(); const auto stats=biupiu::scientific::vector_stats(values,2); assert(stats.l2_norm==5.0); assert(stats.dot_self==25.0); (void)caps; return 0; }