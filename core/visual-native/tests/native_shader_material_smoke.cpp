#include "../include/biupiu_native_shader.h"
#include "../include/biupiu_visual_material.h"
#include <cstdint>
#include <limits>
static int req(bool v,int n){return v?0:n;}
int main(){
 const uint32_t valid[]={0x07230203u,0x00010600u,0u,16u,0u};
 biupiu_shader_desc s{BIUPIU_SHADER_SPIRV,valid,sizeof(valid),"main","spirv"};
 biupiu_spirv_binary b{};
 if(int r=req(biupiu_shader_compile(&s,&b)==0,1))return r;
 biupiu_shader_free(&b);
 biupiu_material_desc m{{1,1,1,1},0.0f,0.5f,{0,0,0},1};
 biupiu_material_id id=0;
 if(int r=req(biupiu_material_create(&m,&id)==0&&id!=0,2))return r;
 biupiu_material_info info{};
 if(int r=req(biupiu_material_get(id,&info)==0,3))return r;
 if(int r=req(info.canonical_hash!=0&&info.desc.roughness==0.5f,4))return r;
 biupiu_material_desc bad=m; bad.roughness=2.0f;
 if(int r=req(biupiu_material_validate(&bad)!=0,5))return r;
 bad=m; bad.base_color[0]=std::numeric_limits<float>::quiet_NaN();
 if(int r=req(biupiu_material_validate(&bad)!=0,6))return r;
 if(int r=req(biupiu_material_destroy(id)==0,7))return r;
 if(int r=req(biupiu_material_get(id,&info)!=0,8))return r;
 return 0;
}
