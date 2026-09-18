namespace Biupiu.Desktop;

public sealed record RuntimeSession(
    string SubscriberId,
    string Tier,
    string Status,
    IReadOnlyList<string> Entitlements);

public sealed record RuntimeRouteState(
    string Route,
    bool Enterable,
    string Reason);

public static class BiupiuRuntime
{
    public static RuntimeRouteState ResolveRoute(RuntimeSession session, string route)
    {
        if (session.Status != "active")
            return new(route, false, "INACTIVE_ACCOUNT");

        if (route is "MAIN_HUB" or "RND_OS")
            return new(route, true, "AUTHORIZED");

        var entitlement = route switch
        {
            "SMART_FARMING" => "SMART_FARMING",
            "SMART_METAL_WORKSHOP" => "SMART_METAL_WORKSHOP",
            _ => null
        };

        if (entitlement is null)
            return new(route, false, "NO_ENTITLEMENT");

        var allowed = session.Entitlements.Contains(entitlement);
        return new(route, allowed, allowed ? "AUTHORIZED" : "NO_ENTITLEMENT");
    }
}
