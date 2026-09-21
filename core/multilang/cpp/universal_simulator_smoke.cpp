#include "biupiu_universal_simulator.h"
#include <cassert>
#include <cmath>

int main() {
    BiupiuSimContext ctx{"sim-1","universal-1","marine","1.0","commit","SI",0.0,0.01,7};
    BiupiuSimObservation obs{};
    assert(biupiu_sim_record_observation(&ctx, 1.0, 2.0, 0.1, 0.9, 3u, &obs) == 0);
    assert(std::isfinite(obs.confidence));
    assert(biupiu_sim_record_observation(&ctx, 1.0, 2.0, 0.1, 1.1, 0u, &obs) < 0);
    return 0;
}
