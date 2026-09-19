import { strict as assert } from "node:assert";
import { readFileSync } from "node:fs";

const index = readFileSync(new URL("./src/index.ts", import.meta.url), "utf8");
const client = readFileSync(new URL("./src/client.ts", import.meta.url), "utf8");
const contract = JSON.parse(
  readFileSync(new URL("./firefly-service-contract-v1.json", import.meta.url), "utf8")
);

const operations = [
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
];

for (const operation of operations) {
  assert.match(index, new RegExp(operation));
  assert.ok(contract.operations.includes(operation), `contract missing ${operation}`);
}

const endpoints = [
  "/v3/images/generate-async",
  "/v4/images/generate-async",
  "/v3/images/generate-similar-async",
  "/v3/images/expand-async",
  "/v3/images/fill-async",
  "/v3/images/generate-object-composite-async",
  "/v3/images/precise-composite",
  "/v3/images/adaptive-composite",
  "/v3/images/upscale",
  "/v3/videos/generate",
  "/v2/storage/image",
  "/v3/status/",
  "/v3/cancel/"
];

for (const endpoint of endpoints) assert.match(client, new RegExp(endpoint.replace(/[.*+?^$()|[\]{}\\]/g, "\\$&")));

assert.equal(contract.apiSpecification.openapi, "3.1.0");
assert.equal(contract.apiSpecification.apiVersion, "3.0.0");
assert.equal(contract.apiSpecification.productionBaseUrl, "https://firefly-api.adobe.io");
assert.equal(contract.apiSpecification.verificationMode, "credential-free-static-contract-check");

assert.match(client, /x-api-key/);
assert.match(client, /x-model-version/);
assert.match(client, /x-access-error/);
assert.match(client, /CANCEL_JOB/);
assert.match(client, /Authorization:/);

console.log("Biupiu Firefly current-release static conformance gate: PASS");
