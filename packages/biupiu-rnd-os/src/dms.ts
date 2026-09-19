export type DmsDataClass = "PUBLIC"|"INTERNAL"|"CONFIDENTIAL"|"RESTRICTED";

export interface DmsTwinRoute {
  apiVersion: "v1";
  endpoint: "/api/v1/digital-twins";
  featureId: "digital-twin.advanced";
  dataClass: DmsDataClass;
  siteScoped: boolean;
  auditRequired: true;
}

export const DMS_TWIN_ROUTE: DmsTwinRoute = {
  apiVersion: "v1",
  endpoint: "/api/v1/digital-twins",
  featureId: "digital-twin.advanced",
  dataClass: "CONFIDENTIAL",
  siteScoped: true,
  auditRequired: true,
};

export function twinDmsRoute(twinId: string): string {
  if (!twinId.trim()) throw new Error("twinId is required");
  return `/api/v1/digital-twins/${encodeURIComponent(twinId)}`;
}
