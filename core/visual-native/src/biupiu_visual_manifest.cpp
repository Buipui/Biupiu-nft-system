#include "../include/biupiu_visual_manifest.h"
#include <fstream>
static bool ok(const char*s){return s&&*s;}
extern "C" int biupiu_visual_manifest_validate(const biupiu_visual_manifest_record*r){if(!r||!ok(r->asset_id)||!ok(r->source)||!ok(r->input_hash)||!ok(r->provider)||!ok(r->license))return 1;return 0;}
extern "C" int biupiu_visual_manifest_write(const biupiu_visual_manifest_record*r,const char*p){if(biupiu_visual_manifest_validate(r)||!ok(p))return 1;std::ofstream f(p);if(!f)return 2;f<<"{\n  \"asset_id\": \""<<r->asset_id<<"\",\n  \"source\": \""<<r->source<<"\",\n  \"input_hash\": \""<<r->input_hash<<"\",\n  \"provider\": \""<<r->provider<<"\",\n  \"output_hash\": \""<<(r->output_hash?r->output_hash:"")<<"\",\n  \"license\": \""<<r->license<<"\"\n}\n";return 0;}
