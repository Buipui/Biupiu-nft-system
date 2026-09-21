#include "biupiu_marine_sim.h"
#include <cmath>
int biupiu_marine_step(const BiupiuMarineInput* in,double u,double v,double r,double dt,BiupiuMarineState* out){
 if(!in||!out||!std::isfinite(u)||!std::isfinite(v)||!std::isfinite(r)||!std::isfinite(dt)||dt<=0||in->mass_kg<=0||in->water_density_kg_m3<0||in->drag_coeff<0)return 1;
 const double drag=0.5*in->water_density_kg_m3*in->drag_coeff*u*std::abs(u);
 const double a=(in->surge_force_n-drag)/in->mass_kg;
 out->surge_mps=u+a*dt; out->sway_mps=v+(in->sway_force_n/in->mass_kg)*dt;
 out->yaw_rate_rps=r+(in->yaw_moment_nm/in->mass_kg)*dt; out->surge_accel_mps2=a; return 0;
}
