import type { ProviderAdapter, ProviderAdapterId } from "./provider-adapter";

export const PROVIDER_IDS:ProviderAdapterId[]=[
  "BLENDER","UNREAL_ENGINE_5","TWINMOTION","KEYSHOT","ADOBE","FIREFLY","RUNWAY"
];

export class ProviderRegistry {
  private adapters=new Map<ProviderAdapterId,ProviderAdapter>();

  register(adapter:ProviderAdapter){
    this.adapters.set(adapter.id,adapter);
  }

  get(id:ProviderAdapterId){
    return this.adapters.get(id);
  }

  has(id:ProviderAdapterId){
    return this.adapters.has(id);
  }
}
