# Biupiu PowerShell Gateway v1.0
# DOS-derived deterministic command boundary. Default: read-only dry-run.
[CmdletBinding()]
param(
  [Parameter(Mandatory=$true)]
  [ValidateSet("HOST.CAPABILITIES","REPOSITORY.STATUS","REPOSITORY.DIRECTORY","TEST.NAMED","REPOSITORY.WRITE.TEST")]
  [string]$Operation,
  [string]$RepositoryPath = (Get-Location).Path,
  [string]$RelativePath = ".",
  [string]$TestName = "gateway-policy",
  [switch]$Approve,
  [switch]$Execute,
  [switch]$Json,
  [string]$RequestId = ([guid]::NewGuid().ToString("N"))
)
$ErrorActionPreference = 'Stop'
$PolicyVersion = '1.0'

function New-Evidence([string]$status, [object]$data = $null) {
  [pscustomobject]@{ timestamp_utc=(Get-Date).ToUniversalTime().ToString('o'); request_id=$RequestId; operation=$Operation; mode=if($Execute){'execute'}else{'dry-run'}; status=$status; host=$env:COMPUTERNAME; policy_version=$PolicyVersion; powershell=[pscustomobject]@{edition=$PSVersionTable.PSEdition;version=$PSVersionTable.PSVersion.ToString();platform=$PSVersionTable.Platform}; data=$data }
}

function Assert-RepositoryPath {
  $resolved=(Resolve-Path -LiteralPath $RepositoryPath -ErrorAction Stop).Path
  if(-not (Test-Path -LiteralPath (Join-Path $resolved '.git'))){throw 'Configured repository path is not a Git working tree.'}
  return $resolved
}

function Invoke-NamedTest {
  if($TestName -ne 'gateway-policy'){throw 'Test is not registered.'}
  $policy=Join-Path $PSScriptRoot 'biupiu-command-policy.json'
  if(-not(Test-Path -LiteralPath $policy)){throw 'Gateway policy manifest is missing.'}
  $obj=Get-Content -Raw -LiteralPath $policy | ConvertFrom-Json
  if($obj.arbitrary_command_execution -ne $false){throw 'Policy violation: arbitrary command execution.'}
  if($obj.arbitrary_script_execution -ne $false){throw 'Policy violation: arbitrary script execution.'}
  if($obj.write_requires_approval -ne $true){throw 'Policy violation: write approval missing.'}
  [pscustomobject]@{test=$TestName;policy_valid=$true}
}

try {
  if($Operation -eq 'REPOSITORY.WRITE.TEST' -and -not $Approve){throw 'Write operation requires -Approve.'}
  if(-not $Execute){
    if($Operation -eq 'REPOSITORY.WRITE.TEST'){New-Evidence 'APPROVAL_REQUIRED' | ConvertTo-Json -Depth 8; exit 0}
    New-Evidence 'DRY_RUN_READY' @{repository=$RepositoryPath;path=$RelativePath;test=$TestName} | ConvertTo-Json -Depth 8; exit 0
  }
  if($Operation -eq 'TEST.NAMED' -and $Execute -and -not $Approve){ throw 'Named test execution requires -Approve.' }
  switch($Operation){
    'HOST.CAPABILITIES' { New-Evidence 'EXECUTED' @{os=[Environment]::OSVersion.VersionString;computer=$env:COMPUTERNAME;architecture=$env:PROCESSOR_ARCHITECTURE;execution_policy=(Get-ExecutionPolicy -Scope Process);execution_policy_list=(Get-ExecutionPolicy -List | ForEach-Object { [pscustomobject]@{scope=$_.Scope;policy=$_.ExecutionPolicy} })} | ConvertTo-Json -Depth 8 }
    'REPOSITORY.STATUS' { $root=Assert-RepositoryPath; $status=@(git -C $root status --short); New-Evidence 'EXECUTED' @{repository=$root;clean=($status.Count -eq 0);status=$status} | ConvertTo-Json -Depth 8 }
    'REPOSITORY.DIRECTORY' { $root=Assert-RepositoryPath; $target=Join-Path $root $RelativePath; $items=@(Get-ChildItem -LiteralPath $target -Force | Select-Object Name,Length,Mode); New-Evidence 'EXECUTED' @{path=$target;items=$items} | ConvertTo-Json -Depth 8 }
    'TEST.NAMED' { New-Evidence 'EXECUTED' (Invoke-NamedTest) | ConvertTo-Json -Depth 8 }
    'REPOSITORY.WRITE.TEST' { $root=Assert-RepositoryPath; $dir=Join-Path $root 'software/gateway/tests/runtime-evidence'; New-Item -ItemType Directory -Path $dir -Force | Out-Null; $file=Join-Path $dir 'approved-write-test.json'; @{request_id=$RequestId;timestamp_utc=(Get-Date).ToUniversalTime().ToString('o');gateway=$PolicyVersion} | ConvertTo-Json | Set-Content -LiteralPath $file -Encoding utf8; New-Evidence 'EXECUTED' @{file=$file} | ConvertTo-Json -Depth 8 }
  }
} catch { New-Evidence 'DENIED_OR_FAILED' @{error=$_.Exception.Message} | ConvertTo-Json -Depth 8; exit 1 }