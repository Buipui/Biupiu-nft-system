export interface LinuxCapabilities {
  posix: boolean;
  shell: "bash" | "sh";
  pathSeparator: "/";
  supportsSystemd: boolean;
  supportsContainers: boolean;
}

export function linuxCapabilities(platform = process.platform): LinuxCapabilities | null {
  if (platform !== "linux") return null;
  return {
    posix: true,
    shell: "bash",
    pathSeparator: "/",
    supportsSystemd: true,
    supportsContainers: true,
  };
}

export function isLinux(): boolean {
  return process.platform === "linux";
}
