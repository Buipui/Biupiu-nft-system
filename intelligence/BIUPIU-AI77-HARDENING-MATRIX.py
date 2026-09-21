"""AI-77 deterministic hardening matrix; planning/static audit only."""
HARDENING={
"kernel":["self_protection","module_control","LSM","seccomp"],
"process":["namespaces","cgroups","Landlock","no_new_privs"],
"boot":["secure_boot","measured_boot","verified_chain"],
"update":["atomic_update","rollback","integrity"],
"isolation":["capability_least_authority","sandbox","VM_domain"],
"trust":["audit","provenance","hash_chain"],
"autonomy":["safe_actions_only","human_gates","fail_closed"]}
BLOCKED=["runtime_execution","physical_actuation","secret_handling","production_release"]
def plan():
    return {"hardening":HARDENING,"blocked":BLOCKED,"runtime_verified":False}
