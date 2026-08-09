param(
  [Parameter(Mandatory = $true)]
  [string] $ExtensionDir
)

$ErrorActionPreference = 'Stop'

$extension = (Resolve-Path -LiteralPath $ExtensionDir).Path
$manifest = Join-Path $extension 'manifest.json'
$hostsScript = Join-Path $extension 'update-hosts.ps1'

if (-not (Test-Path -LiteralPath $manifest)) {
  throw "manifest.json not found: $manifest"
}

$browserCandidates = @(
  'C:\Program Files (x86)\Yandex\YandexBrowser\Application\browser.exe',
  'C:\Program Files\Yandex\YandexBrowser\Application\browser.exe',
  (Join-Path $env:LOCALAPPDATA 'Yandex\YandexBrowser\Application\browser.exe')
)

$browser = $browserCandidates | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1
if (-not $browser) {
  throw 'Yandex Browser was not found in standard locations.'
}

if (Test-Path -LiteralPath $hostsScript) {
  Start-Process -FilePath 'powershell.exe' -ArgumentList @(
    '-NoProfile',
    '-ExecutionPolicy',
    'Bypass',
    '-File',
    $hostsScript
  ) -Verb RunAs -Wait
}

$shortcutTargets = @(
  (Join-Path ([Environment]::GetFolderPath('Desktop')) 'Yandex Browser - YVAC.lnk'),
  (Join-Path ([Environment]::GetFolderPath('StartMenu')) 'Programs\Yandex Browser - YVAC.lnk')
)

$shell = New-Object -ComObject WScript.Shell
foreach ($target in $shortcutTargets) {
  $dir = Split-Path -Parent $target
  if (-not (Test-Path -LiteralPath $dir)) {
    New-Item -ItemType Directory -Path $dir -Force | Out-Null
  }

  $shortcut = $shell.CreateShortcut($target)
  $shortcut.TargetPath = $browser
  $shortcut.Arguments = "--load-extension=`"$extension`""
  $shortcut.WorkingDirectory = Split-Path -Parent $browser
  $shortcut.IconLocation = "$browser,0"
  $shortcut.Description = 'Yandex Browser with Yandex Video Ad Cleaner'
  $shortcut.Save()
}

Write-Host "Browser: $browser"
Write-Host "Extension: $extension"
Write-Host 'Shortcuts created:'
$shortcutTargets | ForEach-Object { Write-Host "  $_" }

Start-Process -FilePath $browser -ArgumentList @("--load-extension=$extension", 'browser://extensions')
