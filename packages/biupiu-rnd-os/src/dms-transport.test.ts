import test from "node:test";
import assert from "node:assert/strict";
import { validateDmsAuthContext, validateTwinEnvelope } from "./dms-transport.js";

test("DMS auth context rejects embedded/empty credentials", () => {
  assert.throws(() => validateDmsAuthContext({ accessTokenRef:"", subjectRef:"user", scopes:["digital-twin.read"] }));
  assert.doesNotThrow(() => validateDmsAuthContext({ accessTokenRef:"secret-ref://dms/session", subjectRef:"user-ref", scopes:["digital-twin.write"] }));
});

test("twin envelope requires site, asset, provenance and idempotency", () => {
  assert.throws(() => validateTwinEnvelope({
    twinId:"t1",siteId:"site1",assetId:"asset1",modelVersion:"m1",
    provenanceRefs:[],payloadRef:"p1",idempotencyKey:"event1"
  }));
  assert.doesNotThrow(() => validateTwinEnvelope({
    twinId:"t1",siteId:"site1",assetId:"asset1",modelVersion:"m1",
    provenanceRefs:["repo:abc"],payloadRef:"p1",idempotencyKey:"event1"
  }));
});
