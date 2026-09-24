#requires -Version 5.1
[CmdletBinding()]
param(
    [switch]$SkipNpmInstall,
    [switch]$SkipAudit,
    [switch]$SkipTests,
    [switch]$Strict,
    [string]$EvidenceRoot = "$(Join-Path (Get-Location) 'build/evidence/windows')"
)

$ErrorActionPreference = "Stop"
$repo = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
New-Item -ItemType Directory -Force -Path $EvidenceRoot | Out-Null

$results = [ordered]@{
    schema = "biupiu.windows-build-evidence.v1"
    timestamp_utc = [DateTime]::UtcNow.ToString("o")
    host = [ordered]@{
        os = [Environment]::OSVersion.VersionString
        powershell = $PSVersionTable.PSVersion.ToString()
        computer = $env:COMPUTERNAME
    }
    gates = @()
}

function Add-Gate([string]$Id,[string]$Status,[string]$Detail) {
    $script:results.gates += [ordered]@{
        id=$Id; status=$Status; detail=$Detail
    }
}

function Invoke-Checked([string]$Id,[string]$File,[string[]]$Arguments) {
    try {
        & $File @Arguments
        if ($LASTEXITCODE -ne 0) { throw "$File exited with code $LASTEXITCODE" }
        Add-Gate $Id "PASS" "$File completed"
    } catch {
        Add-Gate $Id "FAIL" $_.Exception.Message
        if ($Strict) { throw }
    }
}

Push-Location $repo
try {
    foreach ($tool in @("git","node","npm","python")) {
        $cmd = Get-Command $tool -ErrorAction SilentlyContinue
        if ($cmd) {
            Add-Gate "WIN.TOOL.$tool" "PASS" $cmd.Source
        } else {
            Add-Gate "WIN.TOOL.$tool" "MISSING" "Tool not found on PATH"
        }
    }

    $git = (Get-Command git -ErrorAction SilentlyContinue)
    if ($git) {
        Add-Gate "WIN.REPO.IDENTITY" "PASS" (& git rev-parse --show-toplevel).Trim()
        Add-Gate "WIN.REPO.HEAD" "PASS" (& git rev-parse HEAD).Trim()
        Add-Gate "WIN.REPO.BRANCH" "PASS" (& git branch --show-current).Trim()
    } else {
        Add-Gate "WIN.REPO.IDENTITY" "BLOCKED" "Git unavailable"
    }

    if (-not $SkipAudit -and (Test-Path "intelligence/BIUPIU-REPOSITORY-SPELLING-SEMANTIC-AUDIT.py")) {
        Invoke-Checked "WIN.AUDIT.SEMANTIC" "python" @("intelligence/BIUPIU-REPOSITORY-SPELLING-SEMANTIC-AUDIT.py")
    }

    if (-not $SkipNpmInstall -and (Test-Path "package.json")) {
        if (Test-Path "package-lock.json") {
            Invoke-Checked "WIN.NPM.INSTALL" "npm" @("ci")
        } else {
            Invoke-Checked "WIN.NPM.INSTALL" "npm" @("install","--no-audit","--no-fund")
        }
    }

    if (Test-Path "package.json") {
        $pkg = Get-Content "package.json" -Raw | ConvertFrom-Json
        if ($pkg.scripts.compile) { Invoke-Checked "WIN.BUILD.SOLIDITY" "npm" @("run","compile") }
        if (-not $SkipTests -and $pkg.scripts.test) { Invoke-Checked "WIN.TEST.CONTRACTS" "npm" @("test") }
        if ($pkg.scripts."build:packages" -and (Test-Path "tsconfig.json")) {
            Invoke-Checked "WIN.BUILD.PACKAGES" "npm" @("run","build:packages")
        } else {
            Add-Gate "WIN.BUILD.PACKAGES" "NOT_APPLICABLE" "No root tsconfig.json/workspace build target detected"
        }
    }

    $ueCandidates = @(
        "D:\UnrealEngine\UnrealEngine-release",
        "D:\UnrealEngine",
        "C:\UnrealEngine"
    )
    $ue = $ueCandidates | Where-Object { Test-Path (Join-Path $_ "Engine\Build\BatchFiles\Build.bat") } | Select-Object -First 1
    if ($ue) {
        Add-Gate "WIN.UE.SOURCE.DETECT" "DETECTED" $ue
    } else {
        Add-Gate "WIN.UE.SOURCE.DETECT" "NOT_DETECTED" "No known UE source tree detected; local UE path remains runtime-dependent"
    }

    $results | ConvertTo-Json -Depth 8 | Set-Content -Encoding utf8 (Join-Path $EvidenceRoot "windows-build-evidence.json")
    $results | ConvertTo-Json -Depth 8
} finally {
    Pop-Location
}
