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
    }

    private void ShowArea(string area) =>
        TitleText.Text = $"BIUPIU R&D OS — {_target.ScreenId} — {area}";

    private void Overview_Click(object sender, System.Windows.RoutedEventArgs e) => ShowArea("OVERVIEW");
    private void Tools_Click(object sender, System.Windows.RoutedEventArgs e) => ShowArea("TOOLS");
    private void Research_Click(object sender, System.Windows.RoutedEventArgs e) => ShowArea("RESEARCH");
    private void Settings_Click(object sender, System.Windows.RoutedEventArgs e) => ShowArea("SETTINGS");
}
