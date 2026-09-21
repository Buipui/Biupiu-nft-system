#include "../include/biupiu_native_shader.h"
#include "../include/biupiu_visual_material.h"
#include <cassert>
int main(){biupiu_shader_desc s{BIUPIU_SHADER_SPIRV,"12345678","main","spirv"};biupiu_spirv_binary b{};assert(biupiu_shader_compile(&s,&b)==0);assert(b.word_count==2);biupiu_shader_free(&b);biupiu_material_desc m{{1,1,1,1},0.0f,0.5f,{0,0,0},1};biupiu_material_id id=0;assert(biupiu_material_create(&m,&id)==0);assert(biupiu_material_destroy(id)==0);return 0;}
