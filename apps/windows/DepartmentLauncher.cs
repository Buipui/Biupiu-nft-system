namespace Biupiu.Desktop;

public sealed record DepartmentLaunchResult(
    string Route,
    string PackageName,
    bool Started,
    string Reason);

public static class DepartmentLauncher
{
    public static DepartmentLaunchResult Launch(RuntimeSession session, string route)
    {
        var runtime = DepartmentRuntime.Resolve(session, route);
        return new(
            route,
            runtime.Target.PackageName,
            runtime.CanStart,
            runtime.CanStart ? "STARTED" : runtime.Reason);
    }
}
