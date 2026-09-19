import type { DestinationId, DestinationRoute } from "./routeManifest";

export type RouteIntent = {
  status: "READY_FOR_AUTHORIZATION" | "DENIED";
  destination: DestinationRoute;
  reason?: string;
};

export function requestDestination(
  destination: DestinationId,
  entitlements: readonly string[],
): RouteIntent {
  const routes: Record<DestinationId, DestinationRoute> = {
    farming_world: {
      id: "farming_world",
      label: "FARMING WORLD",
      gate: "farming_gate",
      departmentScope: "SMART_FARMING",
      entryRequires: ["subscriber", "SMART_FARMING"],
    },
    metal_making_world: {
      id: "metal_making_world",
      label: "METAL MAKING WORLD",
      gate: "metallurgy_gate",
      departmentScope: "SMART_METAL_WORKSHOP",
      entryRequires: ["subscriber", "SMART_METAL_WORKSHOP"],
    },
  };
  const route = routes[destination];
  const allowed = route.entryRequires.every((required) =>
    entitlements.includes(required),
  );
  return allowed
    ? { status: "READY_FOR_AUTHORIZATION", destination: route }
    : {
        status: "DENIED",
        destination: route,
        reason: "Required entitlement is absent. Client routing never grants authorization.",
      };
}
