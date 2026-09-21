#ifndef BIUPIU_VISUAL_PROVIDER_RUNTIME_H
#define BIUPIU_VISUAL_PROVIDER_RUNTIME_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef struct { const char* name; const char* version; uint32_t capabilities; int (*probe)(void); } biupiu_runtime_provider;
int biupiu_runtime_provider_probe(const biupiu_runtime_provider* p);
#ifdef __cplusplus
}
#endif
#endif
