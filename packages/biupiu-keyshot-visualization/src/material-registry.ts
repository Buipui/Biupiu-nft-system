export type MaterialFamily =
  | "automotive-paint-composite" | "marine-coating" | "aerospace-finish"
  | "microturbine-metal-thermal" | "hemp-fibre-composite" | "bio-resin-adhesive"
  | "textile-fibre" | "ceramic" | "glass" | "packaging-product";

export interface MaterialRecord {
  materialId:string; family:MaterialFamily; displayName:string; sourceType:string;
  sourceUri?:string|null; authorVendor?:string|null; license:string;
  redistributionAllowed:boolean; modificationAllowed:boolean;
  provenanceStatus:"verified"|"pending-review"|"reference-only"|"restricted";
}

export function validateMaterial(record: MaterialRecord): string[] {
  const errors:string[] = [];
  if(!record.materialId || !/^mat-[a-z0-9-]+$/.test(record.materialId)) errors.push("invalid materialId");
  if(!record.license?.trim()) errors.push("license required");
  if(record.redistributionAllowed && record.provenanceStatus !== "verified") errors.push("redistributable material must be verified");
  if(record.sourceType === "reference-only" && record.redistributionAllowed) errors.push("reference-only material cannot be redistributed");
  return errors;
}
