#requires -Version 5.1
[CmdletBinding()]
param([switch]$Strict)
$ErrorActionPreference = "Stop"
$root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$manifest = Join-Path $root "windows\BIUPIU-WINDOWS-SYSTEM-TREE-v1.0.json"
if (-not (Test-Path $manifest)) { throw "Missing Windows system tree manifest: $manifest" }
$tree = Get-Content $manifest -Raw | ConvertFrom-Json
$required = $tree.nodes | Where-Object { $_.status -eq "REQUIRED" }
$missing = @($required | Where-Object { -not (Test-Path (Join-Path $root $_.path)) })
[ordered]@{
    schema=$tree.schema
    timestamp_utc=[DateTime]::UtcNow.ToString("o")
    required_nodes=$required.Count
    missing_nodes=$missing.Count
    missing_paths=@($missing.path)
} | ConvertTo-Json -Depth 8
if ($Strict -and $missing.Count -gt 0) { exit 2 }
