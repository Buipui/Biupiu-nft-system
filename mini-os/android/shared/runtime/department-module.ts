export type DepartmentModuleId = "SMART_FARMING" | "SMART_METAL_WORKSHOP" | "RND_OS";

export interface DepartmentModule {
  id: DepartmentModuleId;
  route: string;
  packageName: string;
  launchUri: string;
  screenId: string;
}

const MODULES: readonly DepartmentModule[] = [
  { id: "SMART_FARMING", route: "smart-farming", packageName: "@biupiu/smart-farming", launchUri: "biupiu://department/smart-farming", screenId: "FARMING_WORLD" },
  { id: "SMART_METAL_WORKSHOP", route: "smart-metal-workshop", packageName: "@biupiu/smart-metallurgy", launchUri: "biupiu://department/smart-metal-workshop", screenId: "METAL_MAKING_WORLD" },
  { id: "RND_OS", route: "rnd-os", packageName: "@biupiu/rnd-os", launchUri: "biupiu://department/rnd-os", screenId: "RND_OS_HOME" }
];

export function resolveDepartmentModule(id: string): DepartmentModule | null {
  return MODULES.find(module => module.id === id) ?? null;
}

export function listDepartmentModules(): readonly DepartmentModule[] {
  return MODULES;
}
