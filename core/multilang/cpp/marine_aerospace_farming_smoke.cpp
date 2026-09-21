#include "biupiu_marine_sim.h"
#include "biupiu_aerospace_space_sim.h"
#include "biupiu_farming_sim.h"
#include <cassert>
#include <cmath>
int main(){
 BiupiuMarineInput m{5000,10000,0,500,1025,0.8}; BiupiuMarineState ms{};
 assert(biupiu_marine_step(&m,2,0,0,0.1,&ms)==0); assert(std::isfinite(ms.surge_mps));
 BiupiuAeroInput a{1000,15000,1000,9.81}; BiupiuAeroState as{};
 assert(biupiu_aerospace_step(&a,1000,50,0.1,&as)==0); assert(std::isfinite(as.altitude_m));
 BiupiuFarmInput f{20,5,10,2,0.8}; BiupiuFarmState fs{};
 assert(biupiu_farming_step(&f,1,&fs)==0); assert(fs.soil_moisture>20);
 return 0;
}