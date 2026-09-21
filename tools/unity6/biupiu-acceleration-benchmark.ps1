[CmdletBinding()]
param(
  [string]$ProjectPath = "",
  [switch]$Build
)
$ErrorActionPreference = "Continue"
$root = if ($ProjectPath) { (Resolve-Path $ProjectPath).Path } else { (Get-Location).Path }
$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$out = Join-Path $root "biupiu-acceleration-benchmark-$stamp"
New-Item -ItemType Directory -Force -Path $out | Out-Null

function Probe([string]$Name,[string]$Command,[string[]]$Args) {
  $path = Get-Command $Command -ErrorAction SilentlyContinue
  if(-not $path){
    @{name=$Name; command=$Command; status="NOT_FOUND"} |
      ConvertTo-Json -Compress | Add-Content (Join-Path $out "host-probes.jsonl")
    return
  }
  $sw = [Diagnostics.Stopwatch]::StartNew()
  $text = & $path.Source @Args 2>&1 | Out-String
  $code = $LASTEXITCODE
  $sw.Stop()
  @{name=$Name; command=$Command; status="FOUND"; exit_code=$code; elapsed_ms=$sw.ElapsedMilliseconds; output=$text.Trim()} |
    ConvertTo-Json -Compress | Add-Content (Join-Path $out "host-probes.jsonl")
}

Probe "powershell" "powershell" @("-NoProfile","-Command","$PSVersionTable.PSVersion.ToString()")
Probe "dotnet" "dotnet" @("--version")
Probe "git" "git" @("--version")
Probe "code" "code" @("--version")
Probe "unity" "Unity.exe" @("-version")

if(Test-Path (Join-Path $root "ProjectSettings/ProjectVersion.txt")){
  Copy-Item (Join-Path $root "ProjectSettings/ProjectVersion.txt") (Join-Path $out "ProjectVersion.txt")
}
if(Test-Path (Join-Path $root "Packages/manifest.json")){
  Copy-Item (Join-Path $root "Packages/manifest.json") (Join-Path $out "manifest.json")
}
if(Test-Path (Join-Path $root "Packages/packages-lock.json")){
  Copy-Item (Join-Path $root "Packages/packages-lock.json") (Join-Path $out "packages-lock.json")
}

$unity = Get-Command Unity.exe -ErrorAction SilentlyContinue
$projectDetected = Test-Path (Join-Path $root "Assets")
$buildStatus = "NOT_RUN"

if($Build -and $unity -and $projectDetected){
  $log = Join-Path $out "unity-build.log"
  $sw = [Diagnostics.Stopwatch]::StartNew()
  & $unity.Source -batchmode -quit -projectPath $root -logFile $log
  $code = $LASTEXITCODE
  $sw.Stop()
  @{status=if($code -eq 0){"PASS"}else{"FAIL"}; exit_code=$code; elapsed_ms=$sw.ElapsedMilliseconds} |
    ConvertTo-Json | Set-Content (Join-Path $out "unity-build-result.json")
  $buildStatus = if($code -eq 0){"PASS"}else{"FAIL"}
} elseif($Build){
  "BLOCKED: Unity.exe or Unity Assets directory not detected." | Set-Content (Join-Path $out "unity-build.log")
  $buildStatus = "BLOCKED"
}

$result = [ordered]@{
  gate="ACCEL-02"
  timestamp=$stamp
  project=$root
  project_detected=$projectDetected
  unity_build=$buildStatus
  promotion="RUNTIME-VERIFICATION-PENDING"
  evidence_boundary="No acceleration claim without reproducible runtime evidence."
}
$result | ConvertTo-Json | Set-Content (Join-Path $out "RESULT.json")
Write-Host "Biupiu acceleration benchmark evidence: $out"
