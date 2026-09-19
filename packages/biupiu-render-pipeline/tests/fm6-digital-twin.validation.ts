import { validateFM6DigitalTwinBinding } from "../src/fm6-digital-twin";

describe("FM6 Digital Twin binding", () => {
  const base = {
    presetId:"BIU-AUTO-FM6REF-STUDIO-001", sourceAssetId:"BIU-VEH-001",
    sourceModelVersion:"1.0.0", digitalTwinId:"DT-AUTO-001",
    department:"automotive" as const, licenceState:"CLEARED" as const,
    ipState:"INTERNAL" as const, referenceState:"FM6-REFERENCE-ONLY" as const,
    providerTargets:["unreal-engine-5","blender"]
  };
  it("requires authoritative lineage and preserves reference-only state", () => {
    expect(() => validateFM6DigitalTwinBinding(base)).not.toThrow();
  });
  it("blocks restricted assets", () => {
    expect(() => validateFM6DigitalTwinBinding({...base, licenceState:"RESTRICTED"})).toThrow();
  });
  it("requires a Digital Twin ID", () => {
    expect(() => validateFM6DigitalTwinBinding({...base, digitalTwinId:""})).toThrow();
  });
});