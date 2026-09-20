import importlib
from dataclasses import asdict
from pathlib import Path
from .models import Capability
class CapabilityRegistry:
    def __init__(self): self._capabilities={}
    def register(self,capability): 
        if not capability.name.strip(): raise ValueError("capability name cannot be empty")
        self._capabilities[capability.name]=capability
    def all(self): return sorted(self._capabilities.values(),key=lambda x:x.name)
    def discover_existing_simulators(self,repo_root):
        d=Path(repo_root)/"simulators"
        if not d.exists(): return []
        found=[]
        for p in sorted(d.glob("biupiu_*.py")):
            name=p.stem
            try:
                m=importlib.import_module(f"simulators.{name}")
                note=m.__doc__.strip().splitlines()[0] if m.__doc__ else ""
                status="loadable"
            except Exception as exc:
                note=str(exc); status="discovered-but-load-failed"
            found.append(Capability(name,"simulator","existing-repository",status,"0.1","repository",f"simulators.{name}",note))
        for c in found: self.register(c)
        return found
    def as_dict(self): return [asdict(x) for x in self.all()]
