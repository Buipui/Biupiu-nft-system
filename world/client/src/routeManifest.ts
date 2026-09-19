export type DestinationId = "farming_world" | "metal_making_world";

export type DestinationRoute = {
  id: DestinationId;
  label: string;
  gate: "farming_gate" | "metallurgy_gate";
  departmentScope: "SMART_FARMING" | "SMART_METAL_WORKSHOP";
  entryRequires: readonly ["subscriber", string];
};

export const DESTINATION_ROUTES: readonly DestinationRoute[] = [
  {
    id: "farming_world",
    label: "FARMING WORLD",
    gate: "farming_gate",
    departmentScope: "SMART_FARMING",
    entryRequires: ["subscriber", "SMART_FARMING"],
  },
  {
    id: "metal_making_world",
    label: "METAL MAKING WORLD",
    gate: "metallurgy_gate",
    departmentScope: "SMART_METAL_WORKSHOP",
    entryRequires: ["subscriber", "SMART_METAL_WORKSHOP"],
  },
];
