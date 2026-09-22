export interface LLVMClangProviderContract {
  id: string;
  family: "llvm" | "clang" | "android-toolchain";
  source: string;
  license: "Apache-2.0-with-LLVM-exception";
  capabilities: readonly string[];
  state: "REFERENCE" | "INTEGRATED_CONTRACT";
}

export const LLVM_CLANG_PROVIDERS: readonly LLVMClangProviderContract[] = [
  {
    id: "llvm-project",
    family: "llvm",
    source: "https://llvm.org/docs/",
    license: "Apache-2.0-with-LLVM-exception",
    capabilities: [
      "ir",
      "optimizer",
      "target-code-generation",
      "compiler-runtime",
      "lld",
      "llvm-profdata",
      "llvm-lto",
      "sanitizers",
      "cross-target-toolchain",
    ],
    state: "INTEGRATED_CONTRACT",
  },
  {
    id: "clang",
    family: "clang",
    source: "https://clang.llvm.org/docs/",
    license: "Apache-2.0-with-LLVM-exception",
    capabilities: [
      "c-family-front-end",
      "preprocessing",
      "semantic-analysis",
      "llvm-ir-generation",
      "integrated-assembler",
      "cross-compilation",
      "static-analysis",
      "clang-format",
      "clang-tidy",
      "libclang",
      "libtooling",
    ],
    state: "INTEGRATED_CONTRACT",
  },
  {
    id: "android-llvm-clang",
    family: "android-toolchain",
    source: "https://android.googlesource.com/toolchain/llvm_android/",
    license: "Apache-2.0-with-LLVM-exception",
    capabilities: [
      "android-platform-build",
      "android-kernel-build",
      "android-ndk-toolchain",
      "rolling-upstream-llvm-integration",
      "profile-guided-optimization",
      "thinlto",
      "mlgo",
    ],
    state: "INTEGRATED_CONTRACT",
  },
];

export interface NativeCompilerGate {
  id: string;
  sequence: readonly string[];
  failClosed: boolean;
}

export const BIUPIU_NATIVE_COMPILER_GATE: NativeCompilerGate = {
  id: "llvm-clang-semantic-build-gate-v1",
  sequence: [
    "language-contract",
    "target-triple",
    "sysroot-and-dependency-resolution",
    "semantic-analysis",
    "llvm-ir",
    "optimizer",
    "codegen",
    "link",
    "static-analysis",
    "unit-test",
    "cross-language-contract-test",
    "regression",
    "runtime/device-build",
    "promotion",
  ],
  failClosed: true,
};

export function llvmClangContractSmokeTest(): boolean {
  return LLVM_CLANG_PROVIDERS.length === 3 &&
    LLVM_CLANG_PROVIDERS.every((provider) => provider.state === "INTEGRATED_CONTRACT") &&
    BIUPIU_NATIVE_COMPILER_GATE.failClosed;
}
