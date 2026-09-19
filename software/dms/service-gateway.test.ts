import { DMSServiceGateway } from "./service-gateway.js";
import type { Principal } from "./types.js";

const coreOperator: Principal = {
  id:"operator", role:"STAFF_OPERATOR", accountStatus:"ACTIVE",
  siteIds:["SITE-01"], productIds:["PRODUCT-01"], subscription:"CORE"
};
const proManager: Principal = {
  id:"manager", role:"SITE_MANAGER", accountStatus:"ACTIVE",
  siteIds:["SITE-01"], productIds:["PRODUCT-01"], subscription:"PRO", mfaVerified:true
};

const gateway = new DMSServiceGateway("smart-metallurgy", [
  "manufacturing.production","manufacturing.advanced-analytics","maintenance.management"
]);

const production = gateway.invoke("manufacturing.production",{principal:coreOperator,siteId:"SITE-01"},()=> "PRODUCTION_EXECUTED");
if(production !== "PRODUCTION_EXECUTED") throw new Error("core operator lost essential production access");

const analytics = gateway.invoke("manufacturing.advanced-analytics",{principal:coreOperator,siteId:"SITE-01"},()=> "ANALYTICS_EXECUTED");
if(typeof analytics !== "object" || analytics.allowed !== false) throw new Error("core operator incorrectly received advanced analytics");

const managerAnalytics = gateway.invoke("manufacturing.advanced-analytics",{principal:proManager,siteId:"SITE-01"},()=> "ANALYTICS_EXECUTED");
if(managerAnalytics !== "ANALYTICS_EXECUTED") throw new Error("pro manager should receive advanced analytics");

console.log("DMS service gateway test: PASS");
