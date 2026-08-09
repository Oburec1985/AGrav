@echo off
setlocal

set "ROOT=%~dp0"
set "ANDROID_DIR=%ROOT%android"
set "ZIP=%ROOT%yvac-kiwi-android.zip"

if not exist "%ANDROID_DIR%\manifest.json" (
  echo Android extension manifest not found:
  echo %ANDROID_DIR%\manifest.json
  pause
  exit /b 1
)

powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "Compress-Archive -Path '%ANDROID_DIR%\*' -DestinationPath '%ZIP%' -Force"

echo Created:
echo %ZIP%
pause
