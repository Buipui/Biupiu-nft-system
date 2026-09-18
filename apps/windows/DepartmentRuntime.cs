namespace Biupiu.Desktop;

public sealed record DepartmentRuntimeTarget(string Route, string PackageName, string? Scope);
public sealed record DepartmentRuntimeState(DepartmentRuntimeTarget Target, bool CanStart, string Reason);

public static class DepartmentRuntime
{
    public static DepartmentRuntimeState Resolve(RuntimeSession session, string route)
    {
        if (session.Status != "active") return new(Target(route), false, "INACTIVE_ACCOUNT");
        var allowed = route is "RND_OS" || session.Entitlements.Contains(route);
        return new(Target(route), allowed, allowed ? "AUTHORIZED" : "NO_ENTITLEMENT");
    }

    private static DepartmentRuntimeTarget Target(string route) => route switch
    {
        "SMART_FARMING" => new(route, "@biupiu/smart-farming", "SMART_FARMING"),
        "SMART_METAL_WORKSHOP" => new(route, "@biupiu/smart-metallurgy", "SMART_METAL_WORKSHOP"),
        "RND_OS" => new(route, "@biupiu/rnd-os", null),
        _ => new(route, "UNRESOLVED", null)
    };
}
