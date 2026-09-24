namespace Biupiu.Desktop;

internal enum ForeignEvidenceClass
{
    Reference,
    SecondaryReference,
    Candidate
}

internal sealed record ForeignLanguageEvidence(
    string Language,
    string Locale,
    string SourceClass,
    string Topic,
    ForeignEvidenceClass EvidenceClass,
    bool CanPromoteExecutableCode);

internal static class ForeignLanguageHarvestRegistry
{
    internal static readonly IReadOnlyList<ForeignLanguageEvidence> Sources =
    [
        new("Chinese", "zh", "AOSP localized", "Android 17 release/module architecture", ForeignEvidenceClass.Reference, false),
        new("Traditional Chinese", "zh-Hant", "AOSP Mainline localized", "APEX/APK modules, atomic update/rollback, stable interfaces", ForeignEvidenceClass.Candidate, false),
        new("Japanese", "ja", "Android release/security notes", "ARM v8-A/x86-64 support and dated security/release evidence", ForeignEvidenceClass.Reference, false),
        new("Korean", "ko", "Android security notes", "Security patch level and vulnerability classification", ForeignEvidenceClass.Reference, false),
        new("Portuguese", "pt", "AOSP Mainline localized", "Stable SDK/system/C/AIDL interfaces and atomic update/revert", ForeignEvidenceClass.Reference, false),
        new("Russian", "ru", "Secondary reporting", "AOSP release cadence/trunk-stable context", ForeignEvidenceClass.SecondaryReference, false)
    ];

    internal static readonly IReadOnlyList<string> FaultChecks =
    [
        "TRANSLATION_FACT_COLLAPSE",
        "LANGUAGE_PROVENANCE_LOSS",
        "SECONDARY_SOURCE_AUTHORITY_LEAK",
        "VERSION_LINEAGE_COLLAPSE",
        "LICENCE_TRANSLATION_GAP",
        "SECURITY_DATE_COLLAPSE",
        "MODULE_SCOPE_OVERCLAIM",
        "RUNTIME_FROM_DOC_ERROR"
    ];

    internal static string ProvenanceFlow =>
        "SOURCE_LANGUAGE -> ORIGINAL_SOURCE -> TRANSLATION/INTERPRETATION -> CLAIM -> EVIDENCE_CLASS -> INTERNAL_MATCH -> MODULE/CAPABILITY -> TEST -> RESULT -> PROVENANCE -> PROMOTION_STATE";

    internal static bool IsPromotionAllowed(ForeignLanguageEvidence evidence) =>
        evidence.CanPromoteExecutableCode && evidence.EvidenceClass == ForeignEvidenceClass.Candidate;

    internal static string Status =>
        $"FOREIGN HARVEST: {Sources.Count} language lanes registered; " +
        "source evidence integrated; executable promotion disabled; runtime verification open.";
}
