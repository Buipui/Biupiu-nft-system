export interface GraphicsProviderContract {
  id: "opengl" | "opengles" | "private-native";
  source: string;
  license: string;
  capabilities: readonly string[];
  state: "INTEGRATED" | "REGISTERED" | "VERIFIED";
}

const PROVIDERS: readonly GraphicsProviderContract[] = [
  {
    id: "opengl",
    source: "https://registry.khronos.org/OpenGL/",
    license: "Khronos-registry/specification terms; component review required",
    capabilities: ["OpenGL-4.6-api", "GLSL", "ARB-extensions", "GLX", "WGL"],
    state: "INTEGRATED",
  },
  {
    id: "opengles",
    source: "https://registry.khronos.org/OpenGL/index_es.php",
    license: "Khronos-registry/specification terms; component review required",
    capabilities: ["OpenGL-ES-3.2", "GLSL-ES", "mobile-rendering"],
    state: "INTEGRATED",
  },
  {
    id: "private-native",
    source: "biupiu://private-native-render-contract",
    license: "Biupiu-proprietary",
    capabilities: ["provider-neutral-render-contract", "digital-twin-visualisation"],
    state: "INTEGRATED",
  },
];

export function listGraphicsProviders(): readonly GraphicsProviderContract[] {
  return PROVIDERS.map((provider) => ({ ...provider, capabilities: [...provider.capabilities] }));
}

export function graphicsProviderSmokeTest(): boolean {
  const providers = listGraphicsProviders();
  return (
    providers.length === 3 &&
    providers.some((provider) => provider.id === "opengl") &&
    providers.some((provider) => provider.id === "opengles") &&
    providers.every((provider) => provider.capabilities.length > 0)
  );
}
