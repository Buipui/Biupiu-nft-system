export type NativeAssetBlueprint = {
  id: string;
  kind: "architectural_prop" | "interactive_prop" | "gate" | "marker";
  interaction?: string;
};

export const MAIN_HUB_ASSET_BLUEPRINTS: readonly NativeAssetBlueprint[] = [
  { id: "hub_arrival_obelisk", kind: "architectural_prop" },
  { id: "civilisation_library_kiosk", kind: "interactive_prop", interaction: "open_library" },
  { id: "farming_gate_arch", kind: "gate" },
  { id: "metallurgy_gate_arch", kind: "gate" },
  { id: "world_map_table", kind: "interactive_prop", interaction: "open_world_map" },
  { id: "research_marker", kind: "marker", interaction: "show_provenance" },
];
