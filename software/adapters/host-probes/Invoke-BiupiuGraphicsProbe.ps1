[CmdletBinding()]
param(
    [string]$OutputPath = ".\biupiu-graphics-capabilities.json"
)

$ErrorActionPreference = "Stop"

function Get-CommandPathSafe([string]$Name) {
    $cmd = Get-Command $Name -ErrorAction SilentlyContinue
    if ($null -eq $cmd) { return $null }
    return $cmd.Source
}

$gpu = Get-CimInstance Win32_VideoController -ErrorAction SilentlyContinue |
    Select-Object Name, DriverVersion, AdapterRAM, VideoProcessor

$result = [ordered]@{
    schema_version = "0.1"
    probe_id = "biupiu.graphics.host"
    timestamp_utc = [DateTime]::UtcNow.ToString("o")
    platform = [Environment]::OSVersion.VersionString
    powershell = $PSVersionTable.PSVersion.ToString()
    executables = [ordered]@{
        cmake = Get-CommandPathSafe "cmake"
        git = Get-CommandPathSafe "git"
        dotnet = Get-CommandPathSafe "dotnet"
        cargo = Get-CommandPathSafe "cargo"
    }
    gpu = @($gpu)
    status = "OBSERVATION-ONLY"
    promotion = "UNVERIFIED"
}

$parent = Split-Path -Parent $OutputPath
if ($parent -and -not (Test-Path $parent)) {
    New-Item -ItemType Directory -Path $parent -Force | Out-Null
}

$result | ConvertTo-Json -Depth 6 | Set-Content -Path $OutputPath -Encoding UTF8
Write-Output "Wrote capability observation to $OutputPath"
