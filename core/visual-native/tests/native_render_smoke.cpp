#include "../include/biupiu_native_render.h"
#include <cassert>
int main(){biupiu_gpu_caps c{};assert(biupiu_render_probe(BIUPIU_GPU_VULKAN,&c)==0);biupiu_render_device_id d=0;assert(biupiu_render_create_device(BIUPIU_GPU_VULKAN,&d)==0);biupiu_render_target_desc td{320,180,0,1,0};biupiu_render_target_id t=0;assert(biupiu_render_create_target(d,&td,&t)==0);biupiu_render_context ctx{d,t,0};assert(biupiu_render_begin(&ctx)==0);assert(biupiu_render_end(&ctx)==0);assert(biupiu_render_destroy_device(d)==0);return 0;}
