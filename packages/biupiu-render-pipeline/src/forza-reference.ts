/**
 * Biupiu Forza/FM6 graphics reference adapter.
 *
 * This is a provider-neutral REFERENCE contract. It does not parse, ship,
 * decrypt, or redistribute proprietary Forza assets.
 */

export const forzaFm6Reference = {
  id: "forza-fm6-reference",
  version: "1.0.0",
  status: "reference-only",
  sourceFamilies: ["ForzaTechStudio", "ForzaTech-extraction-tools"],
  permittedUses: [
    "graphics-research",
    "lod-study",
    "material-parameter-study",
    "automotive-camera-study",
    "lighting-study",
    "resource-optimization-study"
  ],
  prohibitedDependencies: [
    "proprietary-game-assets",
    "extracted-game-assets",
    "encrypted-game-resources",
    "proprietary-keys",
    "unlicensed-shaders",
    "game-binaries"
  ],
  targets: [
    "unreal-engine-5",
    "blender",
    "redshift",
    "v-ray",
    "octane",
    "lumion",
    "keyshot"
  ]
} as const;
