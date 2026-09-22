from copy import deepcopy
from .models import EnvironmentState
class EnvironmentEngine:
    def step(self,env,dt_s,updates=None):
        if dt_s<0: raise ValueError("dt_s must be non-negative")
        env=deepcopy(env); env.timestep_s+=dt_s
        if updates: env.variables.update(updates)
        return env
    def add_entity(self,env,entity_id,state):
        env=deepcopy(env); env.entities[entity_id]=dict(state); return env
    def add_living_system(self,env,system_id,state):
        env=deepcopy(env); env.living_systems[system_id]=dict(state); return env
