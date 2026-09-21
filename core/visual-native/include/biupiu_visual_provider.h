#ifndef BIUPIU_VISUAL_PROVIDER_H
#define BIUPIU_VISUAL_PROVIDER_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef struct { const char* id; const char* version; uint32_t capabilities; } biupiu_visual_provider_info;
typedef struct { biupiu_visual_provider_info info; int (*probe)(void); int (*render)(uint64_t job); int (*animate)(uint64_t job); int (*encode)(uint64_t job); } biupiu_visual_provider;
int biupiu_visual_provider_register(const biupiu_visual_provider* provider);
int biupiu_visual_provider_select(uint32_t required_capabilities,biupiu_visual_provider_info* out);
#ifdef __cplusplus
}
#endif
#endif
