export interface JavaRuntime {
  version: string;
  vendor?: string;
  home?: string;
  executable?: string;
}

export interface JavaCapabilities {
  available: boolean;
  runtime?: JavaRuntime;
  gradleSupported: boolean;
  platform: "windows" | "macos" | "linux" | "android" | "unknown";
}

export function javaCommand(platform: JavaCapabilities["platform"]): string {
  return platform === "windows" ? "java.exe" : "java";
}

export function gradleWrapperCommand(platform: JavaCapabilities["platform"]): string {
  return platform === "windows" ? "gradlew.bat" : "./gradlew";
}
