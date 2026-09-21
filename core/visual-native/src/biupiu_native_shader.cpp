#include "../include/biupiu_native_shader.h"
#include <cstdlib>
#include <cstring>
static bool ok(const char*s){return s&&*s;}
extern "C" int biupiu_shader_validate(const biupiu_shader_desc*d){if(!d||!ok(d->source)||!ok(d->entry)||!ok(d->target))return 1;if(d->language<BIUPIU_SHADER_HLSL||d->language>BIUPIU_SHADER_SPIRV)return 2;return 0;}
extern "C" int biupiu_shader_compile(const biupiu_shader_desc*d,biupiu_spirv_binary*out){if(!out)return 1;out->words=nullptr;out->word_count=0;if(biupiu_shader_validate(d))return 2;if(d->language==BIUPIU_SHADER_SPIRV){size_t n=std::strlen(d->source);if(n%4)return 3;auto*p=(uint32_t*)std::malloc(n);if(!p)return 4;std::memcpy(p,d->source,n);out->words=p;out->word_count=(uint32_t)(n/4);return 0;}return 5;}
extern "C" void biupiu_shader_free(biupiu_spirv_binary*b){if(!b)return;std::free((void*)b->words);b->words=nullptr;b->word_count=0;}
