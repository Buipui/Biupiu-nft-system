import { strict as assert } from "node:assert";
import { readFileSync } from "node:fs";

const index = readFileSync(new URL("./src/index.ts", import.meta.url), "utf8");
const client = readFileSync(new URL("./src/client.ts", import.meta.url), "utf8");

for (const operation of [
  "GENERATE_IMAGE",
  "GENERATE_IMAGE5",
  "EXPAND_IMAGE",
  "FILL_IMAGE",
  "OBJECT_COMPOSITE",
  "PRECISE_COMPOSITE",
  "ADAPTIVE_COMPOSITE",
  "SIMILAR_IMAGES",
  "UPSCALE",
  "GENERATE_VIDEO",
  "UPLOAD_ASSET"
]) assert.match(index, new RegExp(operation));

assert.match(client, /https:\/\/firefly-api\.adobe\.io/);
assert.match(client, /x-api-key/);
assert.match(client, /x-model-version/);
assert.match(client, /x-access-error/);
assert.match(client, /CANCEL_JOB/);

console.log("Biupiu Firefly static smoke test: PASS");
