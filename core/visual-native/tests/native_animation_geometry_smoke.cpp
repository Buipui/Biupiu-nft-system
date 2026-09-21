#include "../include/biupiu_visual_animation.h"
#include "../include/biupiu_visual_geometry.h"
#include "../include/biupiu_visual_subdivision.h"
#include <cassert>
int main(){biupiu_animation_id a=0;assert(biupiu_animation_create(&a)==0);biupiu_keyframe k0{0,{0,0,0,0}},k1{1,{10,20,30,40}};assert(biupiu_animation_add_key(a,&k0,BIUPIU_INTERP_LINEAR)==0);assert(biupiu_animation_add_key(a,&k1,BIUPIU_INTERP_LINEAR)==0);double v[4]{};assert(biupiu_animation_sample(a,.5,v)==0);assert(v[0]==5&&v[1]==10);assert(biupiu_animation_destroy(a)==0);float p[]={0,0,0,1,0,0,0,1,0};uint32_t ix[]={0,1,2};biupiu_mesh_desc m{p,3,ix,3};biupiu_mesh_id id=0;assert(biupiu_mesh_create(&m,&id)==0);assert(biupiu_mesh_destroy(id)==0);biupiu_subdivision_desc s{BIUPIU_SUBDIV_PROVIDER,2};assert(biupiu_subdivision_validate(&s)==0);return 0;}
