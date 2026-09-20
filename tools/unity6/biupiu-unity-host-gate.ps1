# Biupiu Unity 6 Host Gate
# Read-only discovery by default. Run from a PowerShell terminal on the development desktop.
[CmdletBinding()]
param(
  [string]$ProjectPath = "",
  [switch]$Build
)
$ErrorActionPreference = "Continue"
$root = if ($ProjectPath) { (Resolve-Path $ProjectPath).Path } else { (Get-Location).Path }
$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$out = Join-Path $root "biupiu-unity-gate-$stamp"
New-Item -ItemType Directory -Force -Path $out | Out-Null
"Biupiu Unity host gate $stamp" | Set-Content (Join-Path $out "gate.txt")

$commands = @(
  @{Name="powershell"; Cmd="powershell"; Args=@("-NoProfile","-Command","$PSVersionTable | Out-String")},
  @{Name="dotnet"; Cmd="dotnet"; Args=@("--info")},
  @{Name="git"; Cmd="git"; Args=@("--version")},
  @{Name="code"; Cmd="code"; Args=@("--version")},
  @{Name="unity"; Cmd="Unity.exe"; Args=@("-version")}
)
foreach($c in $commands){
  $p = Get-Command $c.Cmd -ErrorAction SilentlyContinue
  if($p){
    & $p.Source @($c.Args) 2>&1 | Tee-Object -FilePath (Join-Path $out "$($c.Name).log")
  } else {
    "NOT FOUND: $($c.Cmd)" | Set-Content (Join-Path $out "$($c.Name).log")
  }
}

if(Test-Path (Join-Path $root "ProjectSettings/ProjectVersion.txt")){
  Copy-Item (Join-Path $root "ProjectSettings/ProjectVersion.txt") (Join-Path $out "ProjectVersion.txt")
}
if(Test-Path (Join-Path $root "Packages/manifest.json")){
  Copy-Item (Join-Path $root "Packages/manifest.json") (Join-Path $out "manifest.json")
}
if(Test-Path (Join-Path $root "Packages/packages-lock.json")){
  Copy-Item (Join-Path $root "Packages/packages-lock.json") (Join-Path $out "packages-lock.json")
}

if($Build){
  $unity = Get-Command Unity.exe -ErrorAction SilentlyContinue
  if($unity -and (Test-Path (Join-Path $root "Assets"))){
    & $unity.Source -batchmode -quit -projectPath $root -logFile (Join-Path $out "unity-build.log")
    "Unity exit code: $LASTEXITCODE" | Set-Content (Join-Path $out "unity-exit-code.txt")
  } else {
    "Build skipped: Unity.exe or Unity project not detected." | Set-Content (Join-Path $out "unity-build.log")
  }
}
"HOST GATE COMPLETE — inspect logs before promotion." | Set-Content (Join-Path $out "RESULT.txt")
Write-Host "Gate evidence written to $out"
