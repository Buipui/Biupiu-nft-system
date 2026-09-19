import test from "node:test";
import assert from "node:assert/strict";
import {canPromoteEvidence,createTwinEvent,dmsDigitalTwinFeatureId} from "./digital-twin.js";
import {twinDmsRoute,validateDmsTwinScope} from "./dms.js";

test("evidence promotion is strictly sequential",()=>{assert.equal(canPromoteEvidence("T0","T1"),true);assert.equal(canPromoteEvidence("T0","T2"),false);assert.equal(canPromoteEvidence("T8","T9"),true);assert.equal(canPromoteEvidence("T9","T9"),false);});
test("twin events reject missing provenance",()=>{assert.throws(()=>createTwinEvent({twinId:"t1",eventType:"SIMULATION",occurredAt:"2026-09-19T00:00:00.000Z",source:"SIMULATION",payloadRef:"p1",modelVersion:"m1",provenanceRefs:[]}));});
test("twin events reject invalid timestamps",()=>{assert.throws(()=>createTwinEvent({twinId:"t1",eventType:"SIMULATION",occurredAt:"invalid",source:"SIMULATION",payloadRef:"p1",modelVersion:"m1",provenanceRefs:["r1"]}));});
test("DMS scope is mandatory",()=>{assert.throws(()=>validateDmsTwinScope("","asset"));assert.throws(()=>validateDmsTwinScope("site",""));validateDmsTwinScope("site","asset");});
test("DMS route is stable",()=>{assert.equal(dmsDigitalTwinFeatureId(),"digital-twin.advanced");assert.equal(twinDmsRoute("twin/001"),"/api/v1/digital-twins/twin%2F001");});
