#include "../include/biupiu_mini_os.h"
#include <type_traits>

static_assert(std::is_standard_layout<biupiu_mini_capability>::value,
              "Mini-OS capability ABI must remain standard-layout");

int main() {
    biupiu_mini_capability cap{};
    return biupiu_mini_get_capability(&cap) == BIUPIU_MINI_OK ? 0 : 1;
}
