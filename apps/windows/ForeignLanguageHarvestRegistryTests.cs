namespace Biupiu.Desktop;

internal static class ForeignLanguageHarvestRegistryTests
{
    internal static void Run()
    {
        if (ForeignLanguageHarvestRegistry.Sources.Count != 6)
            throw new InvalidOperationException("foreign-language source registry is incomplete");

        if (ForeignLanguageHarvestRegistry.Sources.Any(ForeignLanguageHarvestRegistry.IsPromotionAllowed))
            throw new InvalidOperationException("foreign-language evidence bypassed promotion gate");

        if (ForeignLanguageHarvestRegistry.FaultChecks.Count != 8)
            throw new InvalidOperationException("foreign-language fault-check registry is incomplete");

        if (!ForeignLanguageHarvestRegistry.ProvenanceFlow.Contains("ORIGINAL_SOURCE", StringComparison.Ordinal))
            throw new InvalidOperationException("original-source provenance was lost");
    }
}
