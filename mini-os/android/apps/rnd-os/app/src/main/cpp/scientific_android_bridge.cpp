#include "biupiu_scientific_math_adapter.h"

extern "C" int biupiu_scientific_provider() {
    return static_cast<int>(biupiu::scientific::capability().selected);
}
