import { FederationReplayStore, type FederatedTwinEnvelope } from "../../../packages/biupiu-rnd-os/src/federation-transport.js";

export interface SiteNodeSender {
  send(item:FederatedTwinEnvelope):Promise<"ACK"|"RETRYABLE_FAILURE"|"CONFLICT">;
}

export class SiteNodeFederationQueue {
  private readonly store = new FederationReplayStore();
  private readonly items = new Map<string,FederatedTwinEnvelope>();

  enqueue(item:FederatedTwinEnvelope):"QUEUED"|"DUPLICATE"|"CONFLICT" {
    const ack=this.store.accept(item);
    if(item.state==="CONFLICT") return "CONFLICT";
    this.items.set(item.eventId,item);
    return ack ? "DUPLICATE" : "QUEUED";
  }

  async sync(sender:SiteNodeSender):Promise<{acked:number;retryable:number;conflicts:number}> {
    let acked=0,retryable=0,conflicts=0;
    for(const item of this.items.values()){
      const state=this.store.state(item.eventId);
      if(state!=="QUEUED" && state!=="RETRYABLE_FAILURE") continue;
      this.store.markSent(item.eventId);
      const result=await sender.send(item);
      if(result==="ACK"){this.store.markAcked(item.eventId);item.state="ACKED";acked++;}
      else if(result==="RETRYABLE_FAILURE"){this.store.markRetryable(item.eventId);item.state="RETRYABLE_FAILURE";retryable++;}
      else {item.state="CONFLICT";conflicts++;}
    }
    return {acked,retryable,conflicts};
  }

  state(eventId:string){ return this.store.state(eventId); }
}
