from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")

def main() -> None:
    design = read("docs/architecture/BIUPIU-DESIGN-LANGUAGE-CODE-CONTRACT-v1.0.json")
    action = read("research/BIUPIU-UI-SEMANTIC-ACTION-CONTRACT-v1.0.md")
    win_xaml = read("apps/windows/DepartmentModuleWindow.xaml")
    win_cs = read("apps/windows/DepartmentModuleWindow.xaml.cs")
    android = read("apps/android/app/src/main/java/com/biupiu/rndos/DepartmentScreenActivity.kt")
    hub = read("apps/android/app/src/main/java/com/biupiu/rndos/MainHubActivity.kt")
    sim = read("software/rnd-os-ai/src/simulator_module_registry.py")

    assert "NEUTRAL_BASE -> MATERIAL_FINISH -> RESTRAINED_NATURE_ACCENT -> CLEAR_INFORMATION" in design
    assert "INTENT -> ROUTE -> AUTHORISE -> VALIDATE -> EXECUTE_OR_SIMULATE -> OBSERVE -> FEEDBACK -> AUDIT" in action
    assert 'x:Name="CapabilityPanel"' in win_xaml
    assert "HandleCapability(capability)" in win_cs
    assert "setOnClickListener { }" not in android
    assert "RENDER_PIPELINE — NOT REGISTERED" in hub
    assert "design_contract" in sim
    assert "interaction_contract" in sim

    print("BIUPIU design-language/UI semantic audit: PASS")

if __name__ == "__main__":
    main()
