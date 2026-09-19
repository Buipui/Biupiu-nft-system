namespace Biupiu.Desktop;

public sealed record DepartmentModuleTarget(
    string Route,
    string PackageName,
    string LaunchUri,
    string ScreenId);

public static class DepartmentModuleRegistry
{
    public static DepartmentModuleTarget? Resolve(string route) => route switch
    {
        "SMART_FARMING" => new(route, "@biupiu/smart-farming", "biupiu://department/smart-farming", "FARMING_WORLD"),
        "SMART_METAL_WORKSHOP" => new(route, "@biupiu/smart-metallurgy", "biupiu://department/smart-metal-workshop", "METAL_MAKING_WORLD"),
        "RND_OS" => new(route, "@biupiu/rnd-os", "biupiu://department/rnd-os", "RND_OS_HOME"),
        "CREATIVE_AI" => new(route, "@biupiu/firefly", "biupiu://department/creative-ai", "CREATIVE_AI_HOME"),
        _ => null
    };
}
