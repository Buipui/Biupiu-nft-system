import test from "node:test";
import assert from "node:assert/strict";
import {createFederatedEnvelope,deterministicEventId,FederationReplayStore} from "./federation-transport.js";

const base={twinId:"t1",siteId:"site1",assetId:"a1",modelVersion:"m1",provenanceRefs:["repo:b","repo:a"],payloadRef:"payload:1",idempotencyKey:"event:1"};
const node={nodeId:"node-android-01",platform:"ANDROID" as const,protocolVersion:"federation-v1",siteId:"site1",capabilities:["digital-twin","dms-sync"]};

test("deterministic event identity is stable across provenance ordering",()=>{
 const a={...base,provenanceRefs:["repo:a","repo:b"]};
 assert.equal(deterministicEventId(base),deterministicEventId(a));
});

test("federated envelope enforces site scope and sequence",()=>{
 assert.throws(()=>createFederatedEnvelope({...node,siteId:"other"},base,1,"2026-09-21T00:00:00.000Z"));
 assert.throws(()=>createFederatedEnvelope(node,base,0,"2026-09-21T00:00:00.000Z"));
 assert.equal(createFederatedEnvelope(node,base,1,"2026-09-21T00:00:00.000Z").state,"CREATED");
});

test("replay is idempotent and conflicting reuse is blocked",()=>{
 const store=new FederationReplayStore();
 const first=createFederatedEnvelope(node,base,1,"2026-09-21T00:00:00.000Z");
 assert.equal(store.accept(first),undefined);
 store.markSent(first.eventId); store.markAcked(first.eventId);
 const duplicate=createFederatedEnvelope(node,base,2,"2026-09-21T00:01:00.000Z");
 duplicate.eventId=first.eventId;
 const ack=store.accept(duplicate);
 assert.equal(ack?.duplicate,true);
 assert.equal(duplicate.state,"ACKED");
 const conflict=createFederatedEnvelope(node,{...base,payloadRef:"payload:DIFFERENT"},3,"2026-09-21T00:02:00.000Z");
 conflict.eventId=first.eventId;
 assert.equal(store.accept(conflict),undefined);
 assert.equal(conflict.state,"CONFLICT");
 assert.equal(store.state(first.eventId),"CONFLICT");
});
