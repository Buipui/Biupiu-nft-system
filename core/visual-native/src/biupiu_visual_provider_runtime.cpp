#include "../include/biupiu_visual_provider_runtime.h"
extern "C" int biupiu_runtime_provider_probe(const biupiu_runtime_provider*p){if(!p||!p->name||!*p->name||!p->probe)return 1;return p->probe();}
