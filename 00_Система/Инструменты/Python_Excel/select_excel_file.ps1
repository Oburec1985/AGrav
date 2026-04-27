param(
    [string]$Mask = "",

    [Parameter(Mandatory = $true)]
    [string]$OutFile,

    [switch]$Interactive
)

$ErrorActionPreference = "Stop"

function Get-CmdSafePath {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Path
    )

    try {
        $fso = New-Object -ComObject Scripting.FileSystemObject
        if (Test-Path -LiteralPath $Path -PathType Leaf) {
            return $fso.GetFile($Path).ShortPath
        }
        if (Test-Path -LiteralPath $Path -PathType Container) {
            return $fso.GetFolder($Path).ShortPath
        }
    }
    catch {
        return $Path
    }

    return $Path
}

if ([string]::IsNullOrWhiteSpace($Mask)) {
    $Mask = "РСС"
}

$files = Get-ChildItem -LiteralPath (Get-Location) -File -Filter "*.xlsx" |
    Where-Object {
        $_.Name -notlike "~$*" -and
        $_.Name -notlike "*_updated.xlsx" -and
        $_.Name -like ("*" + $Mask + "*")
    } |
    Sort-Object Name

if (-not $files) {
    Write-Host "Excel files not found by substring: $Mask"
    $manual = Read-Host "Enter Excel path manually"
    $manualForCmd = Get-CmdSafePath -Path $manual
    [System.IO.File]::WriteAllText($OutFile, $manualForCmd, [System.Text.UTF8Encoding]::new($false))
    exit 0
}

Write-Host "Found Excel files:"
for ($i = 0; $i -lt $files.Count; $i++) {
    Write-Host ("[{0}] {1}" -f ($i + 1), $files[$i].Name)
}

if (-not $Interactive) {
    $selected = $files[0].FullName
}
else {
    $choice = Read-Host ("Choose number or press Enter for first: " + $files[0].Name)

    if ([string]::IsNullOrWhiteSpace($choice)) {
        $selected = $files[0].FullName
    }
    elseif ($choice -match "^\d+$" -and [int]$choice -ge 1 -and [int]$choice -le $files.Count) {
        $selected = $files[[int]$choice - 1].FullName
    }
    else {
        $selected = $choice
    }
}

Write-Host "Selected Excel file: $selected"
$selectedForCmd = Get-CmdSafePath -Path $selected
Write-Host "Path for cmd: $selectedForCmd"
[System.IO.File]::WriteAllText($OutFile, $selectedForCmd, [System.Text.UTF8Encoding]::new($false))
