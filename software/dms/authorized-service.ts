import { DMSService } from "./dms-service.js";
import { AccessContextService } from "./access-context-service.js";
import type { AccessDecision } from "./types.js";

export class AuthorizedService {
  constructor(private readonly context:AccessContextService, private readonly dms=new DMSService()) {}

  async execute<T>(userId:string, featureId:string, handler:(principalId:string)=>Promise<T>|T, scope?:{siteId?:string;productId?:string}):Promise<T|AccessDecision> {
    const principal=await this.context.resolvePrincipal(userId);
    if(!principal) return {allowed:false,reason:"IDENTITY_NOT_FOUND",featureId,principalId:userId,obligations:["AUDIT_REQUIRED"]};
    const decision=this.dms.authorize({principal,featureId,...scope});
    if(!decision.allowed) return decision;
    return handler(principal.id);
  }
}
