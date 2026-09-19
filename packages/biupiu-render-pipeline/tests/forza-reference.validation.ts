import { forzaFm6Reference } from "../src/forza-reference";

describe("Forza FM6 reference adapter", () => {
  it("is reference-only and blocks proprietary dependencies", () => {
    expect(forzaFm6Reference.status).toBe("reference-only");
    expect(forzaFm6Reference.prohibitedDependencies).toContain("proprietary-game-assets");
    expect(forzaFm6Reference.prohibitedDependencies).toContain("proprietary-keys");
  });

  it("targets the existing Biupiu renderer ecosystem", () => {
    expect(forzaFm6Reference.targets).toContain("unreal-engine-5");
    expect(forzaFm6Reference.targets).toContain("blender");
    expect(forzaFm6Reference.targets).toContain("redshift");
    expect(forzaFm6Reference.targets).toContain("lumion");
  });
});
