namespace Biupiu.Desktop;

using System.Globalization;

internal static class BiupiuLanguageRegistry
{
    internal static readonly string[] SupportedTags =
    {
        "en","af","xh","zu","st","tn","ts","ar","de","fr","es","pt",
        "it","nl","ru","uk","pl","tr","fa","ur","hi","bn","ta","te",
        "kn","ml","mr","gu","pa","si","ne","zh","ja","ko","th","vi",
        "id","ms","fil","sw","am","ha","ig","yo","he","sr","hr","bg",
        "cs","da","fi","el","hu","is","lt","lv","no","ro","sk","sl","sv"
    };

    internal static string Normalise(string tag)
    {
        var value = tag.Trim().Replace('_', '-');
        if (string.IsNullOrWhiteSpace(value)) throw new ArgumentException("language tag must not be empty");
        return CultureInfo.GetCultureInfo(value).Name;
    }
}
