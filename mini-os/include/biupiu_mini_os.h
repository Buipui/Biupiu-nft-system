#ifndef BIUPIU_MINI_OS_H
#define BIUPIU_MINI_OS_H

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

#define BIUPIU_MINI_OS_ABI_VERSION 1u

typedef enum {
    BIUPIU_MINI_OK = 0,
    BIUPIU_MINI_INVALID_ARGUMENT = 1,
    BIUPIU_MINI_NOT_READY = 2,
    BIUPIU_MINI_CONFLICT = 3,
    BIUPIU_MINI_PERMISSION_DENIED = 4
} biupiu_mini_status;

typedef struct {
    uint32_t abi_version;
    uint32_t struct_size;
    uint64_t capability_bits;
} biupiu_mini_capability;

biupiu_mini_status biupiu_mini_get_capability(biupiu_mini_capability *out);

#ifdef __cplusplus
}
#endif

#endif
