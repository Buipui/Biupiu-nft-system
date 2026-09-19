export type BiupiuPlatform = "windows" | "macos" | "linux" | "android" | "unknown";

export interface PlatformCapabilities {
  platform: BiupiuPlatform;
  arch: string;
  node: string;
  shell: "powershell" | "bash" | "unknown";
  pathSeparator: "/" | "\\";
}

export function detectPlatform(
  platform = process.platform,
  arch = process.arch,
  nodeVersion = process.version,
): PlatformCapabilities {
  const map: Record<string, BiupiuPlatform> = {
    win32: "windows",
    darwin: "macos",
    linux: "linux",
    android: "android",
  };
  const normalized = map[platform] ?? "unknown";
  return {
    platform: normalized,
    arch,
    node: nodeVersion,
    shell: normalized === "windows" ? "powershell" : normalized === "linux" || normalized === "macos" || normalized === "android" ? "bash" : "unknown",
    pathSeparator: normalized === "windows" ? "\\" : "/",
  };
}

export function supportedDesktopPlatform(platform: BiupiuPlatform): boolean {
  return platform === "windows" || platform === "macos" || platform === "linux";
}
