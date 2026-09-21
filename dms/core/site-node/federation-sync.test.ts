import test from "node:test";
import assert from "node:assert/strict";
import {createFederatedEnvelope} from "../../../packages/biupiu-rnd-os/src/federation-transport.js";
import {SiteNodeFederationQueue} from "./federation-sync.js";

const node={nodeId:"site-node-01",platform:"ANDROID" as const,protocolVersion:"federation-v1",siteId:"site1",capabilities:["digital-twin"]};
const envelope={twinId:"t1",siteId:"site1",assetId:"a1",modelVersion:"m1",provenanceRefs:["repo:a"],payloadRef:"p1",idempotencyKey:"e1"};

test("site node queues and acknowledges a federated twin event",async()=>{
 const q=new SiteNodeFederationQueue();
 const item=createFederatedEnvelope(node,envelope,1,"2026-09-21T00:00:00.000Z");
 assert.equal(q.enqueue(item),"QUEUED");
 const result=await q.sync({send:async()=> "ACK"});
 assert.deepEqual(result,{acked:1,retryable:0,conflicts:0});
 assert.equal(q.state(item.eventId),"ACKED");
});

test("site node preserves retryable failures for later replay",async()=>{
 const q=new SiteNodeFederationQueue();
 const item=createFederatedEnvelope(node,{...envelope,idempotencyKey:"e2"},2,"2026-09-21T00:00:00.000Z");
 q.enqueue(item);
 assert.deepEqual(await q.sync({send:async()=> "RETRYABLE_FAILURE"}),{acked:0,retryable:1,conflicts:0});
 assert.equal(q.state(item.eventId),"RETRYABLE_FAILURE");
 assert.deepEqual(await q.sync({send:async()=> "ACK"}),{acked:1,retryable:0,conflicts:0});
});
