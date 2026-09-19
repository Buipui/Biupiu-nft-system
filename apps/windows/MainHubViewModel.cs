namespace Biupiu.Desktop;
public sealed class MainHubViewModel
{
 public IReadOnlyList<RuntimeRouteState> Destinations { get; }
 public MainHubViewModel(RuntimeSession session)
 {
  Destinations=new[]{"SMART_FARMING","SMART_METAL_WORKSHOP","RND_OS","RENDER_PIPELINE"}
   .Select(route=>BiupiuRuntime.ResolveRoute(session,route)).ToList();
 }
}