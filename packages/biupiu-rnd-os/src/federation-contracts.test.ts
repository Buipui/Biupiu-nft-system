import { strict as assert } from "node:assert";
import type { FederationCapability, FederationObservation } from "./federation-contracts.js";

const capability: FederationCapability = {
  id: "test.transport",
  version: "1.0.0",
  enabled: true,
  authority: "OBSERVE",
  supportedSchemas: ["biupiu.observation.v1"],
  transports: ["TEST"]
};
assert.equal(capability.authority, "OBSERVE");

const observation: FederationObservation = {
  simulationId: "sim-1",
  simulatorId: "simulator-1",
  domain: "TEST",
  modelVersion: "1.0.0",
  sourceCommit: "test",
  inputHash: "input",
  outputHash: "output",
  timestamp: "2026-09-22T16:00:00Z",
  units: ["SI"],
  assumptions: [],
  evidenceClass: "SIMULATED",
  licenceState: "VERIFIED",
  schema: {name:"biupiu.observation",version:"1",contentType:"application/json",schemaHash:"test"},
  trace: {traceId:"trace",spanId:"span",correlationId:"corr"}
};
assert.equal(observation.evidenceClass, "SIMULATED");
assert.equal(observation.licenceState, "VERIFIED");
assert.match(observation.timestamp, /^\\d{4}-\\d{2}-\\d{2}T/);
console.log("PASS federation-contracts smoke");
