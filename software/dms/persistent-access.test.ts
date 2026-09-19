import { InMemoryDMSRepository } from "./repository-store.js";
import { AccessContextService } from "./access-context-service.js";
import { AuthorizedService } from "./authorized-service.js";

const repo=new InMemoryDMSRepository(
  [{userId:"u1",customerId:"c1",role:"SITE_MANAGER",siteIds:["S1"],productIds:["P1"],accountStatus:"ACTIVE",mfaVerified:true}],
  [{subscriptionId:"s1",customerId:"c1",plan:"PRO",status:"ACTIVE"}],
  [{customerId:"c1",featureId:"ai.forecasting",state:"GRANTED"}]
);
const service=new AuthorizedService(new AccessContextService(repo));
const result=await service.execute("u1","ai.forecasting",()=> "FORECAST_EXECUTED",{siteId:"S1"});
if(result!=="FORECAST_EXECUTED") throw new Error("persistent PRO access should execute");
const denied=await service.execute("u1","robotics.orchestration",()=> "ROBOTICS_EXECUTED",{siteId:"S1"});
if(typeof denied!=="object" || denied.allowed!==false) throw new Error("unentitled function should be denied");
console.log("Persistent DMS access-context test: PASS");
