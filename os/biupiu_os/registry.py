import importlib.util
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
            status="loadable"; note=""
            try:
                spec=importlib.util.spec_from_file_location(name,p)
                module=importlib.util.module_from_spec(spec)
                if spec.loader is None: raise ImportError("no loader")
                spec.loader.exec_module(module)
                note=module.__doc__.strip().splitlines()[0] if module.__doc__ else ""
            except Exception as exc:
                status="discovered-but-load-failed"; note=str(exc)
            found.append(Capability(name,"simulator","existing-repository",status,"0.1","repository",str(p.relative_to(repo_root)),note))
        for c in found: self.register(c)
        return found
    def as_dict(self): return [asdict(x) for x in self.all()]
