#include "biupiu_aerospace_space_sim.h"
#include <cmath>
int biupiu_aerospace_step(const BiupiuAeroInput* in,double h,double v,double dt,BiupiuAeroState* out){
 if(!in||!out||!std::isfinite(h)||!std::isfinite(v)||!std::isfinite(dt)||dt<=0||in->mass_kg<=0||in->gravity_mps2<0)return 1;
 const double a=(in->thrust_n-in->drag_n)/in->mass_kg-in->gravity_mps2;
 out->acceleration_mps2=a; out->velocity_mps=v+a*dt; out->altitude_m=h+out->velocity_mps*dt; return 0;
}
