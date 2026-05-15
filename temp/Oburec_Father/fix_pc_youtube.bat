@echo off
setlocal
:: Проверка прав администратора
net session >nul 2>&1
if %errorLevel% == 0 (
    echo [OK] Запущено с правами администратора.
) else (
    echo [!] Требуются права администратора. Запрашиваю...
    powershell -Command "Start-Process '%0' -Verb RunAs"
    exit /b
)

echo ==================================================
echo       YouTube PC Fixer (DPI Bypass Prep)
echo ==================================================
echo.

echo [1/4] Отключение IPv6 на активных адаптерах...
powershell -Command "Get-NetAdapter | Where-Object { $_.Status -eq 'Up' } | ForEach-Object { Disable-NetAdapterBinding -Name $_.Name -ComponentID ms_tcpip6 -ErrorAction SilentlyContinue }"

echo [2/4] Сброс DNS-кэша...
ipconfig /flushdns

echo [3/4] Сброс сетевого стека...
netsh int ip reset >nul
netsh winsock reset >nul

echo [4/4] Проверка статуса IPv6...
powershell -Command "Get-NetAdapterBinding -ComponentID ms_tcpip6 | Select-Object Name, Enabled"

echo.
echo ==================================================
echo ГОТОВО! 
echo 1. Убедитесь, что v2RayTun / Amnezia ВЫКЛЮЧЕНЫ.
echo 2. ПОЛНОСТЬЮ перезапустите браузер.
echo 3. Проверьте YouTube.
echo ==================================================
pause
