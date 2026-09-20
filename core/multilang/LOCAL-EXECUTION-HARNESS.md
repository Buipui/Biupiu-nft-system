# Biupiu Local Multi-Language Execution Harness

Purpose: provide a deterministic execution path when repository Actions runs are unavailable.

## Commands
- Rust: `cargo fmt --check && cargo test && cargo clippy --all-targets --all-features -- -D warnings`
- C: `gcc -std=c11 -Wall -Wextra -Werror -Icore/multilang/include -fsyntax-only core/multilang/c/abi_smoke.c`
- C++: `g++ -std=c++17 -Wall -Wextra -Werror -Icore/multilang/cpp -fsyntax-only core/multilang/cpp/contract_compile.cpp`

## Evidence rule
Record stdout/stderr, toolchain versions, exit codes and commit SHA. Do not mark BUILD_VERIFIED without those records.

## Multi-AI response
Any failure is classified by layer (Rust/C/C++/ABI/toolchain/dependency/integration), then patched minimally and rerun.
