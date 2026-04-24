$path = 'e:\Oburec\AGrav\temp\visual basic\zad_koman\Formzad_kom.frm'
$content = Get-Content $path -Encoding Default
$content = $content -replace 'Shell "priem.exe", 1', "'Shell ""priem.exe"", 1"
$content | Set-Content $path -Encoding Default
Write-Host "Replaced successfully"
