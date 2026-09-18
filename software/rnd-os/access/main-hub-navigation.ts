import { SubscriberAccount, DepartmentScope, canEnterDepartment } from "./subscriber-model";
export type HubGateState = "PUBLIC_INFO" | "LOCKED" | "ENTERABLE" | "ACTIVE";
export interface HubDestination { id:string; label:string; department:DepartmentScope; state:HubGateState; }
const destinations:Omit<HubDestination,"state">[]=[{id:"farming_world",label:"FARMING WORLD",department:"SMART_FARMING"},{id:"metal_making_world",label:"METAL MAKING WORLD",department:"SMART_METAL_WORKSHOP"}];
export function buildMainHubNavigation(account:SubscriberAccount):HubDestination[]{return destinations.map(d=>({...d,state:canEnterDepartment(account,d.department)?"ENTERABLE":"LOCKED"}));}
