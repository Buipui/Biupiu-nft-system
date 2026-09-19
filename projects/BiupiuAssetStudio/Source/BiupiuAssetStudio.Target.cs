using UnrealBuildTool;

public class BiupiuAssetStudioTarget : TargetRules
{
    public BiupiuAssetStudioTarget(TargetInfo Target) : base(Target)
    {
        Type = TargetType.Game;
        DefaultBuildSettings = BuildSettingsVersion.V5;
        IncludeOrderVersion = EngineIncludeOrderVersion.Latest;
        ExtraModuleNames.Add("BiupiuAssetStudio");
    }
}
