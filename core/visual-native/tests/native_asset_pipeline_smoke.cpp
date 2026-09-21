#include "../include/biupiu_visual_assets.h"
#include "../include/biupiu_visual_gpu_pipeline.h"
#include <cassert>
int main(){biupiu_image_desc i{1920,1080,4,1,1};biupiu_image_id id=0;assert(biupiu_image_create(&i,&id)==0);biupiu_color_transform c{0,2.2f,"sRGB"};assert(biupiu_color_transform_validate(&c)==0);biupiu_pipeline_desc p{1,2,3,1};biupiu_pipeline_id pid=0;assert(biupiu_pipeline_create(&p,&pid)==0);assert(biupiu_pipeline_destroy(pid)==0);assert(biupiu_image_destroy(id)==0);return 0;}
