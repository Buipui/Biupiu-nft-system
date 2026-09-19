import test from "node:test";
import assert from "node:assert/strict";
import { canPromoteEvidence, createTwinEvent, dmsDigitalTwinFeatureId } from "./digital-twin.js";
import { twinDmsRoute } from "./dms.js";

test("digital twin evidence promotion is sequential", () => {
  assert.equal(canPromoteEvidence("T0", "T1"), true);
  assert.equal(canPromoteEvidence("T0", "T2"), false);
  assert.equal(canPromoteEvidence("T8", "T9"), true);
});

test("digital twin events require model/provenance references", () => {
  const event = createTwinEvent({
    twinId: "twin-001",
    eventType: "SIMULATION",
    occurredAt: "2026-09-19T00:00:00.000Z",
    source: "SIMULATION",
    payloadRef: "sim-001",
    modelVersion: "model-1",
    provenanceRefs: ["repo:abc"],
  });
  assert.equal(event.modelVersion, "model-1");
  assert.deepEqual(event.provenanceRefs, ["repo:abc"]);
});

test("DMS route is stable and feature-gated", () => {
  assert.equal(dmsDigitalTwinFeatureId(), "digital-twin.advanced");
  assert.equal(twinDmsRoute("twin/001"), "/api/v1/digital-twins/twin%2F001");
});
