#pragma once
#include <cstdint>

namespace biupiu::native {

struct Capability {
    std::uint32_t abi_version{};
    std::uint64_t capability_bits{};
};

class NativeSubsystem {
public:
    virtual ~NativeSubsystem() = default;
    virtual Capability capability() const noexcept = 0;
    virtual bool validate() const noexcept = 0;
};

} // namespace biupiu::native
