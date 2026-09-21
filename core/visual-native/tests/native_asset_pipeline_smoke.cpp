#include "../include/biupiu_visual_assets.h"
#include "../include/biupiu_visual_gpu_pipeline.h"
static int req(bool v,int n){return v?0:n;}
int main(){
 biupiu_image_desc i{1920,1080,4,1,1};biupiu_image_id id=0;
 if(int r=req(biupiu_image_create(&i,&id)==0&&id!=0,1))return r;
 biupiu_image_info info{};if(int r=req(biupiu_image_get(id,&info)==0,2))return r;
 if(int r=req(info.state==BIUPIU_ASSET_CPU_READY&&info.byte_size==1920ull*1080ull*4ull*4ull&&info.content_hash!=0,3))return r;
 if(int r=req(biupiu_image_set_state(id,BIUPIU_ASSET_GPU_READY)==0,4))return r;
 if(int r=req(biupiu_image_get(id,&info)==0&&info.state==BIUPIU_ASSET_GPU_READY,5))return r;
 biupiu_color_transform c{0,2.2f,"sRGB"};if(int r=req(biupiu_color_transform_validate(&c)==0,6))return r;
 biupiu_color_transform bad{0,0,"sRGB"};if(int r=req(biupiu_color_transform_validate(&bad)!=0,7))return r;
 biupiu_pipeline_desc p{1,2,3,1};biupiu_pipeline_id pid=0;if(int r=req(biupiu_pipeline_create(&p,&pid)==0,8))return r;
 if(int r=req(biupiu_pipeline_destroy(pid)==0,9))return r;
 if(int r=req(biupiu_image_destroy(id)==0&&biupiu_image_destroy(id)!=0,10))return r;
 return 0;
}
