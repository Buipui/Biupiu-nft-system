namespace Biupiu.Desktop;

public static class DeepLinkRouter
{
    public static string? Resolve(string uri)
    {
        const string prefix = "biupiu://department/";
        if (!uri.StartsWith(prefix, StringComparison.OrdinalIgnoreCase))
            return null;

        var route = uri[prefix.Length..].TrimEnd('/');
        return route switch
        {
            "smart-farming" => "SMART_FARMING",
            "smart-metal-workshop" => "SMART_METAL_WORKSHOP",
            "rnd-os" => "RND_OS",
            _ => null
        };
    }
}