#include "biupiu_abi.h"

int main(void) {
    biupiu_capability_t cap = {0};
    if (biupiu_core_get_capability(&cap) != BIUPIU_OK) return 1;
    if (cap.abi_version != BIUPIU_ABI_VERSION) return 2;
    if (cap.struct_size != sizeof(cap)) return 3;

    biupiu_bytes_t empty = {0};
    if (biupiu_core_validate_buffer(empty) != BIUPIU_OK) return 4;

    return 0;
}
