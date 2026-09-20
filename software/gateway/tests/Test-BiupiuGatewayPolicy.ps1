# Deterministic repository-side gateway policy test.
[CmdletBinding()]
param([string]$PolicyPath=(Join-Path $PSScriptRoot '..\biupiu-command-policy.json'))
$ErrorActionPreference='Stop'
$policy=Get-Content -Raw -LiteralPath $PolicyPath | ConvertFrom-Json
$checks=@($policy.schema_version -eq '1.0',$policy.basis -eq 'biupiu-dos-command-contract',$policy.mode_default -eq 'dry-run',$policy.arbitrary_command_execution -eq $false,$policy.arbitrary_script_execution -eq $false,$policy.write_requires_approval -eq $true,$policy.network_operations -eq $false,$policy.download_operations -eq $false,$policy.install_operations -eq $false)
if($checks -contains $false){throw 'Gateway policy assertion failed.'}
$gateway=Join-Path $PSScriptRoot '..\Invoke-BiupiuGateway.ps1'
if(-not(Test-Path -LiteralPath $gateway)){throw 'Gateway implementation missing.'}
$source=Get-Content -Raw -LiteralPath $gateway
$forbiddenCommands = [regex]::Matches($source, '(?im)^\s*(?:&\s*)?(Invoke-Expression|iex)\b')
if($forbiddenCommands.Count -gt 0){throw 'Forbidden execution primitive detected in executable command position.'}
$source = Get-Content -Raw -LiteralPath (Join-Path $PSScriptRoot '..\Invoke-BiupiuGateway.ps1')
foreach($required in @('HOST.CAPABILITIES','REPOSITORY.STATUS','REPOSITORY.DIRECTORY','TEST.NAMED','REPOSITORY.WRITE.TEST','-Approve','-Execute')) { if(-not $source.Contains($required)){throw "Required gateway contract missing: $required"} }
Write-Output 'BIUPIU_GATEWAY_POLICY_TEST: PASS'