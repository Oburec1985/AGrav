$ErrorActionPreference = 'Stop'

$hosts = 'C:\Windows\System32\drivers\etc\hosts'
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$backup = "$hosts.yvac-backup-$stamp"
$entries = @(
  '0.0.0.0 lotory.top',
  '0.0.0.0 cdn.lotory.top',
  '0.0.0.0 p0sembed.com',
  '0.0.0.0 www.p0sembed.com',
  '0.0.0.0 iwad.cachefly.net',
  '0.0.0.0 assets.ahmybid.net'
)

Copy-Item -LiteralPath $hosts -Destination $backup -Force

$content = Get-Content -LiteralPath $hosts -Raw
$toAdd = @()
foreach ($entry in $entries) {
  $hostName = ($entry -split '\s+')[-1]
  $pattern = "(?m)^\s*(0\.0\.0\.0|127\.0\.0\.1)\s+$([regex]::Escape($hostName))\s*(#.*)?$"
  if ($content -notmatch $pattern) {
    $toAdd += $entry
  }
}

if ($toAdd.Count -gt 0) {
  Add-Content -LiteralPath $hosts -Value ('', '# Yandex Video Ad Cleaner', ($toAdd -join [Environment]::NewLine)) -Encoding ASCII
}

ipconfig /flushdns | Out-Null

"backup=$backup" | Set-Content -LiteralPath "$env:TEMP\yvac-hosts-result.txt" -Encoding UTF8
"added=$($toAdd -join ', ')" | Add-Content -LiteralPath "$env:TEMP\yvac-hosts-result.txt" -Encoding UTF8
