package com.biupiu.world.data

data class ShowcaseDevelopment(
    val id: String,
    val department: String,
    val scene: String,
    val title: String,
    val status: String,
    val claimClass: String
)

object ShowcaseRegistry {
    val developments = listOf(
        ShowcaseDevelopment("AQUA-01-HYDROFOIL","Marine & Hydrofoil","MAR-01","Biupiu Glass Hydrofoil","CONCEPT","DESIGN_REFERENCE"),
        ShowcaseDevelopment("REGENERATIVE-AGRI","Regenerative Agriculture","AGR-01","Regenerative Farming Systems","RESEARCH","SYSTEM_RESEARCH"),
        ShowcaseDevelopment("HEMP-CARBON","Advanced Materials","MAR-01","HempCarbon Materials","RESEARCH","MATERIAL_RESEARCH"),
        ShowcaseDevelopment("BIOBLADE","Energy Systems","AIR-01","Bioblade Microturbine","CONCEPT","ENGINEERING_CONCEPT"),
        ShowcaseDevelopment("INTELLIGENCE-HUB","AI / Intelligence Hub","AI-01","Biupiu Intelligence Hub","RESEARCH","SOFTWARE_RESEARCH"),
        ShowcaseDevelopment("PHOTONICS","Photonics & Optical Communications","AI-01","Photonics Research","RESEARCH","RESEARCH"),
        ShowcaseDevelopment("DIGITAL-LAB","R&D / Digital Lab","AI-01","Biupiu Digital Laboratory","RESEARCH","PLATFORM_RESEARCH"),
        ShowcaseDevelopment("BIUPIU-WORLD","Digital World","AI-01","Biupiu World","CONCEPT","DIGITAL_PLATFORM")
    )
}
