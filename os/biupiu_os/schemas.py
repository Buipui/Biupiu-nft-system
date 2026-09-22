from __future__ import annotations
from typing import Any
NUMERIC=(int,float)
def validate_mapping(data:dict[str,Any],required:tuple[str,...]=(),numeric:tuple[str,...]=()):
    if not isinstance(data,dict): raise TypeError("payload must be a mapping")
    missing=[k for k in required if k not in data]
    if missing: raise ValueError("missing required fields: "+",".join(missing))
    bad=[k for k in numeric if k in data and (not isinstance(data[k],NUMERIC) or isinstance(data[k],bool))]
    if bad: raise TypeError("numeric fields invalid: "+",".join(bad))
    return True
def validate_outputs(data:dict[str,Any]):
    if not isinstance(data,dict): raise TypeError("module output must be a mapping")
    return True
