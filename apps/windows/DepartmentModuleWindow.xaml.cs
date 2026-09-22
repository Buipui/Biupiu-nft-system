namespace Biupiu.Desktop;

public partial class DepartmentModuleWindow : System.Windows.Window
{
    private readonly DepartmentModuleTarget _target;

    public DepartmentModuleWindow(DepartmentModuleTarget target)
    {
        InitializeComponent();
        _target = target;
        Title = $"Biupiu — {target.ScreenId}";
        TitleText.Text = $"BIUPIU R&D OS — {target.ScreenId}";
        IdentityText.Text = $"{target.PackageName}  •  {target.LaunchUri}";

        foreach (var capability in ResolveCapabilities(target.Route))
        {
            var button = new System.Windows.Controls.Button
            {
                Content = capability.Replace('_', ' '),
                Margin = new System.Windows.Thickness(8),
                Padding = new System.Windows.Thickness(18, 10, 18, 10),
                MinHeight = 52
            };
            button.Click += (_, _) => HandleCapability(capability);
            CapabilityPanel.Children.Add(button);
        }

        StatusText.Text = "READY — choose a capability";
    }

    private void HandleCapability(string capability)
    {
        var result = ResolveAction(_target.Route, capability);
        TitleText.Text = $"BIUPIU R&D OS — {_target.ScreenId} — {capability}";

        StatusText.Text = result switch
        {
            "AUTHORIZED" => $"AUTHORIZED — {capability.Replace('_', ' ')}",
            "SIMULATION_ONLY" => $"SIMULATION ONLY — {capability.Replace('_', ' ')}",
            "ACTION_NOT_IMPLEMENTED" => $"REGISTERED — {capability.Replace('_', ' ')} has no executable handler yet",
            _ => $"ACTION BLOCKED — {result}"
        };
    }

    private static string ResolveAction(string route, string capability) => capability switch
    {
        "WORLD" when route is "SMART_FARMING" or "SMART_METAL_WORKSHOP" or "RND_OS" => "AUTHORIZED",
        "AI" => "SIMULATION_ONLY",
        "SETTINGS" => "AUTHORIZED",
        _ => "ACTION_NOT_IMPLEMENTED"
    };

    private static IReadOnlyList<string> ResolveCapabilities(string route) => route switch
    {
        "SMART_FARMING" => new[] { "WORLD", "FARMING_SYSTEMS", "AUTOMATION", "AI", "SETTINGS" },
        "SMART_METAL_WORKSHOP" => new[] { "WORLD", "METAL_WORKSHOP", "AUTOMATION", "AI", "SETTINGS" },
        "RND_OS" => new[] { "WORLD", "RESEARCH_REPOSITORY", "COMPUTATIONAL_ENGINEERING", "AUTOMATION", "AI", "SETTINGS" },
        _ => Array.Empty<string>()
    };
}
