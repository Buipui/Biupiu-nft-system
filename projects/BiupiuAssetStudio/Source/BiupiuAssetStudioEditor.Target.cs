using UnrealBuildTool;

public class BiupiuAssetStudioEditorTarget : TargetRules
{
    public BiupiuAssetStudioEditorTarget(TargetInfo Target) : base(Target)
    {
        Type = TargetType.Editor;
        DefaultBuildSettings = BuildSettingsVersion.V5;
        IncludeOrderVersion = EngineIncludeOrderVersion.Latest;
        ExtraModuleNames.Add("BiupiuAssetStudio");
    }
}
