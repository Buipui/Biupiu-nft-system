export type DepartmentShellAction = "OVERVIEW" | "TOOLS" | "RESEARCH" | "SETTINGS";

export interface DepartmentShell {
  id: string;
  title: string;
  packageName: string;
  screenId: string;
  actions: readonly DepartmentShellAction[];
  capabilities: readonly string[];
}

const SHELLS: readonly DepartmentShell[] = [
  {
    id: "SMART_FARMING",
    title: "Smart Farming",
    packageName: "@biupiu/smart-farming",
    screenId: "FARMING_WORLD",
    actions: ["OVERVIEW", "TOOLS", "RESEARCH", "SETTINGS"],
    capabilities: ["WORLD", "FARMING_SYSTEMS", "AUTOMATION", "AI", "SETTINGS"]
  },
  {
    id: "SMART_METAL_WORKSHOP",
    title: "Smart Metal Workshop",
    packageName: "@biupiu/smart-metallurgy",
    screenId: "METAL_MAKING_WORLD",
    actions: ["OVERVIEW", "TOOLS", "RESEARCH", "SETTINGS"],
    capabilities: ["WORLD", "METAL_WORKSHOP", "AUTOMATION", "AI", "SETTINGS"]
  },
  {
    id: "RND_OS",
    title: "Biupiu R&D OS",
    packageName: "@biupiu/rnd-os",
    screenId: "RND_OS_HOME",
    actions: ["OVERVIEW", "TOOLS", "RESEARCH", "SETTINGS"],
    capabilities: ["WORLD", "RESEARCH_REPOSITORY", "COMPUTATIONAL_ENGINEERING", "AUTOMATION", "AI", "SETTINGS"]
  }
];

export function resolveDepartmentShell(id: string): DepartmentShell | null {
  return SHELLS.find(shell => shell.id === id) ?? null;
}
