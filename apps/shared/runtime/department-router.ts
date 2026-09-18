export type DepartmentRoute =
  | "SMART_FARMING"
  | "SMART_METAL_WORKSHOP"
  | "RND_OS"
  | "CREATIVE_AI";

export interface DepartmentTarget {
  route: DepartmentRoute;
  packageName: string;
  packagePath: string;
  scope?: string;
}

const targets: Record<DepartmentRoute, DepartmentTarget> = {
  SMART_FARMING: {
    route: "SMART_FARMING",
    packageName: "@biupiu/smart-farming",
    packagePath: "packages/biupiu-smart-farming",
    scope: "SMART_FARMING"
  },
  SMART_METAL_WORKSHOP: {
    route: "SMART_METAL_WORKSHOP",
    packageName: "@biupiu/smart-metallurgy",
    packagePath: "packages/biupiu-smart-metallurgy",
    scope: "SMART_METAL_WORKSHOP"
  },
  RND_OS: {
    route: "RND_OS",
    packageName: "@biupiu/rnd-os",
    packagePath: "packages/biupiu-rnd-os"
  },
  CREATIVE_AI: {
    route: "CREATIVE_AI",
    packageName: "@biupiu/firefly",
    packagePath: "packages/biupiu-firefly",
    scope: "CREATIVE_AI"
  }
};

export function resolveDepartment(route: DepartmentRoute): DepartmentTarget {
  return targets[route];
}
