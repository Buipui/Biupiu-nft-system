from pathlib import Path
import json, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
smoke=ROOT/"intelligence/BIUPIU-AI72-CLOSURE-SMOKE-TEST.py"
audit=ROOT/"intelligence/BIUPIU-AI72-DEPENDENCY-INTERFACE-CLOSURE-AUDIT.py"
assert smoke.exists() and audit.exists()
p=subprocess.run([sys.executable,str(smoke)],cwd=ROOT,capture_output=True,text=True)
assert p.returncode==0, p.stdout+p.stderr
print(json.dumps({"gate":"AI-73","ai72_smoke":"PASS","ci_execution_required":True,"promotion_allowed":False},sort_keys=True))
