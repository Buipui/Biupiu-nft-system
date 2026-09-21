export type BiupiuPlatform = "windows" | "macos" | "linux" | "android" | "ios" | "web" | "unknown";
export type CpuFamily = "x86_64" | "arm64" | "riscv64" | "unknown";
export type ComputeAccelerator = "cpu" | "gpu" | "npu" | "vector";

export interface PlatformCapabilities {
  platform: BiupiuPlatform;
  arch: string;
  cpuFamily: CpuFamily;
  node: string;
  shell: "powershell" | "bash" | "unknown";
  pathSeparator: "/" | "\\";
  nativeAcceleration: ComputeAccelerator[];
  spatialEndpoint: boolean;
}

export function detectPlatform(
  platform = process.platform,
  arch = process.arch,
  nodeVersion = process.version,
): PlatformCapabilities {
  const map: Record<string, BiupiuPlatform> = {
    win32: "windows", darwin: "macos", linux: "linux", android: "android",
    ios: "ios", web: "web",
  };
  const normalized = map[platform] ?? "unknown";
  const cpuFamily: CpuFamily =
    arch === "x64" ? "x86_64" :
    arch === "arm64" ? "arm64" :
    arch === "riscv64" ? "riscv64" : "unknown";
  const nativeAcceleration: ComputeAccelerator[] = ["cpu"];
  if (cpuFamily === "x86_64" || cpuFamily === "arm64") nativeAcceleration.push("vector");
  return {
    platform: normalized,
    arch,
    cpuFamily,
    node: nodeVersion,
    shell: normalized === "windows" ? "powershell" :
      normalized === "linux" || normalized === "macos" || normalized === "android" ? "bash" : "unknown",
    pathSeparator: normalized === "windows" ? "\\" : "/",
    nativeAcceleration,
    spatialEndpoint: normalized === "android" || normalized === "ios" || normalized === "web",
  };
}

export function supportedDesktopPlatform(platform: BiupiuPlatform): boolean {
  return platform === "windows" || platform === "macos" || platform === "linux";
}

export function supportsNativeFamily(capabilities: PlatformCapabilities, family: CpuFamily): boolean {
  return capabilities.cpuFamily === family;
}
