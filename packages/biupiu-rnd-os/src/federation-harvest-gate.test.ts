import { strict as assert } from "node:assert";
import {
  evaluateHarvestPromotion,
  quarantineHarvest,
  type HarvestRecord
} from "./federation-harvest-gate.js";

const base: HarvestRecord = {
  id: "harvest.test",
  name: "test-adapter",
  version: "1.0.0",
  repositoryPath: "research/test-adapter",
  status: "CANDIDATE",
  evidence: {
    source: "https://example.invalid/source",
    licenceReviewed: true,
    provenanceRecorded: true,
    versionCompared: true,
    dependencyCheckPassed: true,
    normalisationPassed: true,
    staticTestPassed: true,
    buildPassed: true,
    securityReviewPassed: true,
    integrationTestPassed: true,
    regressionPassed: true,
    runtimeTestPassed: true,
    rollbackReference: "commit://baseline",
    testReferences: ["test://federation-harvest-gate"]
  }
};

assert.deepEqual(evaluateHarvestPromotion(base), { promotable: true, reasons: [] });

const missingSource: HarvestRecord = {
  ...base,
  evidence: { ...base.evidence, source: "" }
};
assert.equal(evaluateHarvestPromotion(missingSource).promotable, false);
assert.match(
  evaluateHarvestPromotion(missingSource).reasons.join(";"),
  /harvest source is missing/
);

const emptyPlacement: HarvestRecord = { ...base, repositoryPath: "   " };
assert.equal(evaluateHarvestPromotion(emptyPlacement).promotable, false);

const quarantined = quarantineHarvest(base, "incompatible dependency boundary");
assert.equal(quarantined.status, "QUARANTINED");
assert.equal(quarantined.quarantineReason, "incompatible dependency boundary");
assert.throws(() => quarantineHarvest(base, "   "), /quarantine reason is required/);

console.log("PASS federation-harvest-gate smoke");


const missingProtocolGate: HarvestRecord = {
  ...base,
  evidence: { ...base.evidence, integrationTestPassed: false }
};
assert.equal(evaluateHarvestPromotion(missingProtocolGate).promotable, false);
assert.match(
  evaluateHarvestPromotion(missingProtocolGate).reasons.join(";"),
  /integration tests have not passed/
);

const missingRollback: HarvestRecord = {
  ...base,
  evidence: { ...base.evidence, rollbackReference: "" }
};
assert.equal(evaluateHarvestPromotion(missingRollback).promotable, false);
assert.match(
  evaluateHarvestPromotion(missingRollback).reasons.join(";"),
  /rollback reference is missing/
);

const missingVersionCompare: HarvestRecord = {
  ...base,
  evidence: { ...base.evidence, versionCompared: false }
};
assert.equal(evaluateHarvestPromotion(missingVersionCompare).promotable, false);
assert.match(
  evaluateHarvestPromotion(missingVersionCompare).reasons.join(";"),
  /version comparison is incomplete/
);

console.log("PASS federation-harvest-gate extended module-testing protocol");
