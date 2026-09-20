#include "biupiu_native_contract.hpp"

class TestSubsystem final : public biupiu::native::NativeSubsystem {
public:
    biupiu::native::Capability capability() const noexcept override {
        return {1u, 0u};
    }

    bool validate() const noexcept override { return true; }
};

int main() {
    TestSubsystem subsystem;
    const auto capability = subsystem.capability();
    return (capability.abi_version == 1u && subsystem.validate()) ? 0 : 1;
}
