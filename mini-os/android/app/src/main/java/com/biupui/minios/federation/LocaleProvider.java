package com.biupui.minios.federation;

import android.content.Context;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.core.os.LocaleListCompat;

/** AndroidX is the primary per-app locale API; Lingver is compatibility-only. */
public final class LocaleProvider implements ExternalTransportAdapter {
    public void setApplicationLanguage(String languageTag) {
        if (languageTag == null || languageTag.trim().isEmpty()) AppCompatDelegate.setApplicationLocales(LocaleListCompat.getEmptyLocaleList());
        else AppCompatDelegate.setApplicationLocales(LocaleListCompat.forLanguageTags(languageTag));
    }
    public String currentLanguageTags() { return AppCompatDelegate.getApplicationLocales().toLanguageTags(); }
    public void apply(Context context) { if (context == null) throw new IllegalArgumentException("context == null"); }
    @Override public String id() { return "locale.androidx"; }
    @Override public boolean isAvailable() { return true; }
    @Override public String diagnosticState() { return "IMPLEMENTED; AndroidX per-app locale API; Lingver compatibility isolated"; }
}
