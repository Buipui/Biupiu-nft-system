export type LicenceState = "PENDING" | "CLEARED" | "RESTRICTED";
export type IPState = "PUBLIC" | "INTERNAL" | "CONFIDENTIAL" | "PRE-PATENT";

export interface FM6DigitalTwinBinding {
  presetId: string;
  sourceAssetId: string;
  sourceModelVersion: string;
  digitalTwinId: string;
  department: "automotive" | "aerospace" | "world";
  licenceState: LicenceState;
  ipState: IPState;
  referenceState: "FM6-REFERENCE-ONLY";
  providerTargets: string[];
}

export const validateFM6DigitalTwinBinding = (b: FM6DigitalTwinBinding): void => {
  if (b.referenceState !== "FM6-REFERENCE-ONLY") throw new Error("FM6 binding must remain reference-only.");
  if (!b.sourceAssetId || !b.sourceModelVersion || !b.digitalTwinId) throw new Error("Source asset, model version and Digital Twin ID are required.");
  if (b.licenceState === "RESTRICTED") throw new Error("Restricted assets cannot enter a renderer package.");
  if (b.providerTargets.length === 0) throw new Error("At least one provider target is required.");
};