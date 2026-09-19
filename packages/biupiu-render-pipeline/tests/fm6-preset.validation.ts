import preset from "../../../research/BIUPIU-FM6-AUTOMOTIVE-PRESET-EXAMPLE-v1.0.json";

describe("FM6 reference automotive preset", () => {
  it("remains reference-only", () => { expect(preset.reference_state).toBe("FM6-REFERENCE-ONLY"); });
  it("contains scalable LOD policy and validated material controls", () => {
    expect(preset.lod.levels.length).toBeGreaterThanOrEqual(3);
    expect(preset.material.normal_tangent_validation).toBe(true);
  });
  it("targets the existing renderer stack", () => {
    expect(preset.targets).toEqual(expect.arrayContaining(["unreal-engine-5","blender","redshift","lumion","keyshot"]));
  });
});
