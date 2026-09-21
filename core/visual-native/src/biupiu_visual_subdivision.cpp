#include "../include/biupiu_visual_subdivision.h"
extern "C" int biupiu_subdivision_validate(const biupiu_subdivision_desc*d){if(!d)return 1;if(d->mode>BIUPIU_SUBDIV_PROVIDER)return 2;if(d->level>32)return 3;return 0;}
