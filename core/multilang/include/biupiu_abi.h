#ifndef BIUPIU_ABI_H
#define BIUPIU_ABI_H
#include <stdint.h>
#ifdef __cplusplus
extern "C" {
#endif

#define BIUPIU_ABI_VERSION 1u

typedef enum {
    BIUPIU_OK = 0,
    BIUPIU_INVALID_ARGUMENT = 1,
    BIUPIU_NOT_READY = 2,
    BIUPIU_CONFLICT = 3,
    BIUPIU_PERMISSION_DENIED = 4
} biupiu_status_t;

typedef struct {
    uint32_t abi_version;
    uint32_t struct_size;
    uint64_t capability_bits;
} biupiu_capability_t;

typedef struct {
    const void *data;
    uint64_t size;
} biupiu_bytes_t;

biupiu_status_t biupiu_core_get_capability(biupiu_capability_t *out);
biupiu_status_t biupiu_core_validate_buffer(biupiu_bytes_t input);

#ifdef __cplusplus
}
#endif
#endif
