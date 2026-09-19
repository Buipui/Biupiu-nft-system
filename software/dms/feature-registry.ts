import type { FeatureDefinition, Role, SubscriptionTier } from "./types.js";
const ALL_ROLES: Role[]=["ROOT","PLATFORM_ADMIN","DEPARTMENT_ADMIN","SITE_MANAGER","STAFF_OPERATOR","RND_USER","CUSTOMER","CUSTOMER_RND","DEVICE_SERVICE"];
const ALL_TIERS: SubscriptionTier[]=["CORE","STANDARD","PRO","ENTERPRISE","RND_PARTNER"];

export const FEATURE_REGISTRY: Record<string,FeatureDefinition> = {
"dms.profile.read":{id:"dms.profile.read",module:"IDENTITY",action:"READ",safetyClass:"ESSENTIAL",roles:ALL_ROLES,tiers:ALL_TIERS},
"agri.operations":{id:"agri.operations",module:"AGRI",action:"OPERATE",safetyClass:"ESSENTIAL",roles:["ROOT","PLATFORM_ADMIN","DEPARTMENT_ADMIN","SITE_MANAGER","STAFF_OPERATOR"],tiers:["CORE","STANDARD","PRO","ENTERPRISE"]},
"hemp.traceability":{id:"hemp.traceability",module:"HEMP",action:"TRACE",safetyClass:"ESSENTIAL",roles:["ROOT","PLATFORM_ADMIN","DEPARTMENT_ADMIN","SITE_MANAGER","STAFF_OPERATOR","CUSTOMER"],tiers:["CORE","STANDARD","PRO","ENTERPRISE"]},
"hemp.processing":{id:"hemp.processing",module:"HEMP",action:"PROCESS",safetyClass:"ESSENTIAL",roles:["ROOT","PLATFORM_ADMIN","DEPARTMENT_ADMIN","SITE_MANAGER","STAFF_OPERATOR"],tiers:["CORE","STANDARD","PRO","ENTERPRISE"]},
"manufacturing.production":{id:"manufacturing.production",module:"MAN",action:"PRODUCE",safetyClass:"ESSENTIAL",roles:["ROOT","PLATFORM_ADMIN","DEPARTMENT_ADMIN","SITE_MANAGER","STAFF_OPERATOR"],tiers:["CORE","STANDARD","PRO","ENTERPRISE"]},
"manufacturing.advanced-analytics":{id:"manufacturing.advanced-analytics",module:"MAN",action:"ANALYZE",safetyClass:"OPTIONAL",roles:["ROOT","PLATFORM_ADMIN","DEPARTMENT_ADMIN","SITE_MANAGER"],tiers:["PRO","ENTERPRISE"]},
"inventory.operations":{id:"inventory.operations",module:"INV",action:"OPERATE",safetyClass:"ESSENTIAL",roles:["ROOT","PLATFORM_ADMIN","DEPARTMENT_ADMIN","SITE_MANAGER","STAFF_OPERATOR"],tiers:["CORE","STANDARD","PRO","ENTERPRISE"]},
"quality.release":{id:"quality.release",module:"QA",action:"RELEASE",safetyClass:"ESSENTIAL",roles:["ROOT","PLATFORM_ADMIN","DEPARTMENT_ADMIN","SITE_MANAGER"],tiers:["CORE","STANDARD","PRO","ENTERPRISE"],requiresMfa:true},
"maintenance.management":{id:"maintenance.management",module:"MNT",action:"MANAGE",safetyClass:"ESSENTIAL",roles:["ROOT","PLATFORM_ADMIN","DEPARTMENT_ADMIN","SITE_MANAGER","STAFF_OPERATOR"],tiers:["CORE","STANDARD","PRO","ENTERPRISE"]},
"rnd.experiment-management":{id:"rnd.experiment-management",module:"RND",action:"MANAGE",safetyClass:"EXPERIMENTAL",roles:["ROOT","PLATFORM_ADMIN","DEPARTMENT_ADMIN","RND_USER","CUSTOMER_RND"],tiers:["RND_PARTNER","ENTERPRISE"]},
"engineering.simulation":{id:"engineering.simulation",module:"ENG",action:"SIMULATE",safetyClass:"OPTIONAL",roles:["ROOT","PLATFORM_ADMIN","DEPARTMENT_ADMIN","RND_USER"],tiers:["PRO","ENTERPRISE","RND_PARTNER"]},
"ai.forecasting":{id:"ai.forecasting",module:"AI",action:"FORECAST",safetyClass:"OPTIONAL",roles:["ROOT","PLATFORM_ADMIN","DEPARTMENT_ADMIN","SITE_MANAGER"],tiers:["PRO","ENTERPRISE"]},
"robotics.orchestration":{id:"robotics.orchestration",module:"ROB",action:"ORCHESTRATE",safetyClass:"OPTIONAL",roles:["ROOT","PLATFORM_ADMIN","DEPARTMENT_ADMIN","SITE_MANAGER"],tiers:["PRO","ENTERPRISE"]},
"digital-twin.advanced":{id:"digital-twin.advanced",module:"DTM",action:"ADVANCED",safetyClass:"OPTIONAL",roles:["ROOT","PLATFORM_ADMIN","DEPARTMENT_ADMIN","SITE_MANAGER","RND_USER"],tiers:["PRO","ENTERPRISE","RND_PARTNER"]},
"dms.multi-site":{id:"dms.multi-site",module:"DMS",action:"MULTI_SITE",safetyClass:"OPTIONAL",roles:["ROOT","PLATFORM_ADMIN"],tiers:["ENTERPRISE"]},
"customer.rnd-participation":{id:"customer.rnd-participation",module:"CRM",action:"CONTRIBUTE",safetyClass:"EXPERIMENTAL",roles:["ROOT","CUSTOMER_RND"],tiers:["RND_PARTNER","ENTERPRISE"]}
};
