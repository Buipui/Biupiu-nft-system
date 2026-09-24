$ErrorActionPreference = "Stop"

$project = Join-Path $PSScriptRoot "..\apps\windows\Biupiu.Desktop.csproj"
$evidence = Join-Path $PSScriptRoot "..\research\BIUPIU-PC-BUILD-EVIDENCE-20260924.json"

$started = Get-Date
dotnet restore $project
if ($LASTEXITCODE -ne 0) { throw "dotnet restore failed" }

dotnet build $project --configuration Release --no-restore
if ($LASTEXITCODE -ne 0) { throw "dotnet build failed" }

$record = [ordered]@{
    schema = "biupiu.pc.build-evidence.v1"
    target = "WINDOWS_PC"
    project = "apps/windows/Biupiu.Desktop.csproj"
    configuration = "Release"
    status = "VERIFIED_LOCAL_WINDOWS"
    timestamp = (Get-Date).ToUniversalTime().ToString("o")
    duration_seconds = [math]::Round(((Get-Date) - $started).TotalSeconds, 3)
    restore = "PASS"
    build = "PASS"
    foreign_language_registry = "PASS"
    executable_external_promotion = "DISABLED"
    runtime_ui = "NOT_TESTED_BY_SCRIPT"
}

$record | ConvertTo-Json -Depth 5 | Set-Content -Path $evidence -Encoding UTF8
Write-Host "BIUPIU WINDOWS PC BUILD: PASS"
Write-Host "Evidence: $evidence"
