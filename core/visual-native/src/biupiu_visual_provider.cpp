#include "../include/biupiu_visual_provider.h"
#include <mutex>
#include <string>
#include <vector>
static std::mutex m; static std::vector<biupiu_visual_provider> providers;
extern "C" int biupiu_visual_provider_register(const biupiu_visual_provider*p){if(!p||!p->info.id||!p->probe)return 1;if(p->probe()!=0)return 3;std::lock_guard<std::mutex>l(m);for(auto&x:providers)if(std::string(x.info.id)==p->info.id)return 4;providers.push_back(*p);return 0;}
extern "C" int biupiu_visual_provider_select(uint32_t req,biupiu_visual_provider_info*out){if(!out)return 1;std::lock_guard<std::mutex>l(m);for(auto&x:providers)if((x.info.capabilities&req)==req){*out=x.info;return 0;}return 2;}
