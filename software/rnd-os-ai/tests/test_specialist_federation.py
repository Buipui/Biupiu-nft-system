from biupiu_ai.specialist_federation import Capability, Result, SpecialistRegistry, Task

class DemoSpecialist:
    capability = Capability("agriculture-ai", "1.0", ("agriculture","water"), autonomous=True, resident=True)
    def execute(self, task):
        return Result(task.task_id, self.capability.name, "completed", {"handled": task.domain}, confidence=0.9)

def test_specialist_is_resident_and_autonomous():
    registry = SpecialistRegistry()
    registry.register(DemoSpecialist())
    assert len(registry.resident("agriculture")) == 1
    result = registry.dispatch(Task("t1", "agriculture", {"crop":"hemp"}))
    assert result.status == "completed"
    assert result.specialist == "agriculture-ai"

def test_unresolved_domain_does_not_fail_other_specialists():
    registry = SpecialistRegistry()
    registry.register(DemoSpecialist())
    result = registry.dispatch(Task("t2", "aerospace", {}))
    assert result.status == "unresolved"
