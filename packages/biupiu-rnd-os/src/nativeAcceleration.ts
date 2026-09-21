import type { CpuFamily, ComputeAccelerator, PlatformCapabilities } from "./platform";

export interface NativeAccelerationContract {
  cpuFamily: CpuFamily;
  accelerators: ComputeAccelerator[];
  backend: "portable" | "amd" | "intel" | "apple" | "generic-arm" | "riscv";
  spatial: boolean;
}

export function nativeAccelerationContract(c: PlatformCapabilities): NativeAccelerationContract {
  if (c.cpuFamily === "x86_64") {
    return {
      cpuFamily: c.cpuFamily,
      accelerators: c.nativeAcceleration,
      backend: "portable",
      spatial: c.spatialEndpoint,
    };
  }
  if (c.cpuFamily === "arm64" && c.platform === "macos") {
    return {
      cpuFamily: c.cpuFamily,
      accelerators: c.nativeAcceleration,
      backend: "apple",
      spatial: c.spatialEndpoint,
    };
  }
  if (c.cpuFamily === "arm64") {
    return {
      cpuFamily: c.cpuFamily,
      accelerators: c.nativeAcceleration,
      backend: "generic-arm",
      spatial: c.spatialEndpoint,
    };
  }
  if (c.cpuFamily === "riscv64") {
    return {
      cpuFamily: c.cpuFamily,
      accelerators: c.nativeAcceleration,
      backend: "riscv",
      spatial: c.spatialEndpoint,
    };
  }
  return {
    cpuFamily: "unknown",
    accelerators: ["cpu"],
    backend: "portable",
    spatial: c.spatialEndpoint,
  };
}
