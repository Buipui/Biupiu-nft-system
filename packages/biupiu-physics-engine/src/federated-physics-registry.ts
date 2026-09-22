export type PhysicsProvider =
  | "jolt-physics"
  | "bullet3"
  | "private-native";

export interface PhysicsProviderContract {
  id: PhysicsProvider;
  source: string;
  license: string;
  capabilities: readonly string[];
  state: "INTEGRATED" | "REGISTERED" | "VERIFIED";
  runtimeRequired: boolean;
}

const PROVIDERS: readonly PhysicsProviderContract[] = [
  {
    id: "jolt-physics",
    source: "https://github.com/jrouwe/JoltPhysics",
    license: "MIT",
    capabilities: [
      "rigid-body-dynamics",
      "collision-detection",
      "constraints",
      "vehicle-hooks",
      "multithread-friendly-simulation",
    ],
    state: "INTEGRATED",
    runtimeRequired: true,
  },
  {
    id: "bullet3",
    source: "https://github.com/bulletphysics/bullet3",
    license: "ZLIB",
    capabilities: [
      "collision-detection",
      "rigid-body-dynamics",
      "soft-body-dynamics",
      "vehicle-dynamics",
      "robotics-validation",
    ],
    state: "INTEGRATED",
    runtimeRequired: true,
  },
  {
    id: "private-native",
    source: "biupiu://private-native-physics-kernel",
    license: "Biupiu-proprietary",
    capabilities: ["deterministic-baseline", "dependency-free-core"],
    state: "INTEGRATED",
    runtimeRequired: false,
  },
];

export function listPhysicsProviders(): readonly PhysicsProviderContract[] {
  return PROVIDERS.map((provider) => ({ ...provider, capabilities: [...provider.capabilities] }));
}

export function physicsProviderSmokeTest(): boolean {
  const providers = listPhysicsProviders();
  const ids = new Set(providers.map((provider) => provider.id));
  return (
    providers.length === 3 &&
    ids.has("jolt-physics") &&
    ids.has("bullet3") &&
    ids.has("private-native") &&
    providers.every((provider) => provider.capabilities.length > 0)
  );
}
