namespace Biupiu.Desktop;

using System.Globalization;

public partial class MainWindow : System.Windows.Window
{
    private readonly RuntimeSession _session =
        new("local-preview", "PUBLIC", "active", Array.Empty<string>());

    public MainWindow()
    {
        InitializeComponent();
        LanguageSelector.ItemsSource = BiupiuLanguageRegistry.SupportedTags;
        LanguageSelector.SelectedItem = BiupiuLanguageRegistry.Normalise(CultureInfo.CurrentUICulture.Name);
        ApplyEntitlements();
    }

    private void ApplyEntitlements()
    {
        FarmingButton.IsEnabled = BiupiuRuntime.ResolveRoute(_session, "SMART_FARMING").Enterable;
        MetallurgyButton.IsEnabled = BiupiuRuntime.ResolveRoute(_session, "SMART_METAL_WORKSHOP").Enterable;
        RndButton.IsEnabled = BiupiuRuntime.ResolveRoute(_session, "RND_OS").Enterable;
    }

    private void OpenDepartment(string route)
    {
        var state = BiupiuRuntime.ResolveRoute(_session, route);
        if (!state.Enterable) return;

        var target = DepartmentModuleRegistry.Resolve(route);
        if (target is null) return;

        new DepartmentModuleWindow(target).Show();
    }

    private void FarmingButton_Click(object sender, System.Windows.RoutedEventArgs e) =>
        OpenDepartment("SMART_FARMING");

    private void MetallurgyButton_Click(object sender, System.Windows.RoutedEventArgs e) =>
        OpenDepartment("SMART_METAL_WORKSHOP");

    private void RndButton_Click(object sender, System.Windows.RoutedEventArgs e) =>
        OpenDepartment("RND_OS");
}


    private void LanguageSelector_SelectionChanged(object sender, System.Windows.Controls.SelectionChangedEventArgs e)
    {
        if (LanguageSelector.SelectedItem is not string tag) return;
        var canonical = BiupiuLanguageRegistry.Normalise(tag);
        CultureInfo.CurrentUICulture = CultureInfo.GetCultureInfo(canonical);
        CultureInfo.CurrentCulture = CultureInfo.GetCultureInfo(canonical);
    }
