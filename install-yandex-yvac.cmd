@echo off
setlocal

set "PROJECT_DIR=%~dp0"
set "EXTENSION_DIR=%PROJECT_DIR%yvac-extension"
set "INSTALL_PS1=%EXTENSION_DIR%\install-yvac.ps1"

if not exist "%EXTENSION_DIR%\manifest.json" (
  echo Extension manifest not found:
  echo %EXTENSION_DIR%\manifest.json
  pause
  exit /b 1
)

if not exist "%INSTALL_PS1%" (
  echo Installer helper not found:
  echo %INSTALL_PS1%
  pause
  exit /b 1
)

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%INSTALL_PS1%" -ExtensionDir "%EXTENSION_DIR%"

echo.
echo Done. Use the desktop shortcut "Yandex Browser - YVAC" to start Yandex with the extension.
pause
