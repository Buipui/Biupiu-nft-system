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
                Padding = new System.Windows.Thickness(18, 10, 18, 10)
            };
            button.Click += (_, _) => TitleText.Text = $"BIUPIU R&D OS — {_target.ScreenId} — {capability}";
            CapabilityPanel.Children.Add(button);
        }
    }

    private static IReadOnlyList<string> ResolveCapabilities(string route) => route switch
    {
        "SMART_FARMING" => new[] { "WORLD", "FARMING_SYSTEMS", "AUTOMATION", "AI", "SETTINGS" },
        "SMART_METAL_WORKSHOP" => new[] { "WORLD", "METAL_WORKSHOP", "AUTOMATION", "AI", "SETTINGS" },
        "RND_OS" => new[] { "WORLD", "RESEARCH_REPOSITORY", "COMPUTATIONAL_ENGINEERING", "AUTOMATION", "AI", "SETTINGS" },
        _ => Array.Empty<string>()
    };
}
