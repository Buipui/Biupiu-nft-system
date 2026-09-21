#ifndef BIUPIU_VISUAL_SUBDIVISION_H
#define BIUPIU_VISUAL_SUBDIVISION_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif
typedef enum { BIUPIU_SUBDIV_NONE=0, BIUPIU_SUBDIV_PROVIDER=1 } biupiu_subdivision_mode;
typedef struct { biupiu_subdivision_mode mode; uint32_t level; } biupiu_subdivision_desc;
int biupiu_subdivision_validate(const biupiu_subdivision_desc* desc);
#ifdef __cplusplus
}
#endif
#endif
