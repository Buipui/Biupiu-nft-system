const assert = require("node:assert/strict");
const { planGodotExecution } = require("../src/index.ts");

const clean = planGodotExecution(
  { sourceId: "godot-engine", sceneId: "biupiu-world", capabilities: ["scene", "render"], provenanceHash: "sha256:test" },
  { id: "godot-engine", url: "https://github.com/godotengine/godot", license: "MIT", gate: "adapter-target", capabilities: ["scene", "render", "mobile", "physics"] }
);
assert.equal(clean.releaseBlocked, false);

const blocked = planGodotExecution(
  { sourceId: "godot-tps-demo", sceneId: "tps-reference", capabilities: ["render"], provenanceHash: "sha256:test" },
  { id: "godot-tps-demo", url: "https://github.com/godotengine/tps-demo", license: "mixed", gate: "asset-review-required", capabilities: ["render"] }
);
assert.equal(blocked.releaseBlocked, true);

const noHash = planGodotExecution(
  { sourceId: "godot-engine", sceneId: "untracked", capabilities: ["scene"] },
  { id: "godot-engine", url: "https://github.com/godotengine/godot", license: "MIT", gate: "adapter-target", capabilities: ["scene"] }
);
assert.equal(noHash.releaseBlocked, true);

console.log("Godot bridge contract tests passed");
