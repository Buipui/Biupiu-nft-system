namespace Biupiu.Desktop;

public partial class DepartmentModuleWindow : System.Windows.Window
{
    public DepartmentModuleWindow(DepartmentModuleTarget target)
    {
        InitializeComponent();
        Title = $"Biupiu — {target.ScreenId}";
        ScreenText.Text = $"BIUPIU R&D OS\n{target.ScreenId}\n{target.PackageName}";
    }
}
