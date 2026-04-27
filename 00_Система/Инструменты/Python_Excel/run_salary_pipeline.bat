@echo off
chcp 65001 >nul
setlocal EnableExtensions
cd /d "%~dp0"

echo === 1. Prepare result.csv ===
set "RUN_PARSE=N"
set /p "RUN_PARSE=Run image parsing and rebuild result.csv? [y/N]: "
if /I "%RUN_PARSE%"=="Y" (
    call :run_python parse_zp_image.py
    if errorlevel 1 goto :fail
) else (
    echo Skipping image parsing. Existing result.csv/results.csv will be used.
)

echo.
echo === 2. Select Excel file ===
set "SELECT_FILE=%TEMP%\agrav_selected_excel.txt"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0select_excel_file.ps1" -OutFile "%SELECT_FILE%"
if errorlevel 1 goto :fail

set /p "SELECTED_EXCEL="<"%SELECT_FILE%"
if not exist "%SELECTED_EXCEL%" (
    echo Excel file not found: "%SELECTED_EXCEL%"
    goto :fail
)

echo Selected file: "%SELECTED_EXCEL%"
echo.
echo === 3. Excel update parameters ===
set "SHEET_NAME="
set "NAME_COL=B"
set "TARGET_COL=H"
set "START_ROW=1"

set /p "SHEET_NAME=Sheet name [default from script]: "

set /p "NAME_COL=Name column [B]: "
if "%NAME_COL%"=="" set "NAME_COL=B"

set /p "TARGET_COL=Amount column [H]: "
if "%TARGET_COL%"=="" set "TARGET_COL=H"

set /p "START_ROW=Start row [1]: "
if "%START_ROW%"=="" set "START_ROW=1"

echo.
echo === 4. Write result.csv to Excel ===
if "%SHEET_NAME%"=="" (
    call :run_python update_excel_template.py "%SELECTED_EXCEL%" --name-col "%NAME_COL%" --target-col "%TARGET_COL%" --start-row "%START_ROW%" --output "%SELECTED_EXCEL%" --value-divisor 1000
) else (
    call :run_python update_excel_template.py "%SELECTED_EXCEL%" --sheet "%SHEET_NAME%" --name-col "%NAME_COL%" --target-col "%TARGET_COL%" --start-row "%START_ROW%" --output "%SELECTED_EXCEL%" --value-divisor 1000
)
if errorlevel 1 goto :fail

echo.
echo Done.
pause
exit /b 0

:run_python
where py >nul 2>nul
if not errorlevel 1 (
    py -c "import sys" >nul 2>nul
    if errorlevel 1 goto :try_python
    py %*
    exit /b %errorlevel%
)

:try_python
where python >nul 2>nul
if not errorlevel 1 (
    python -c "import sys" >nul 2>nul
    if errorlevel 1 goto :try_file_assoc
    python %*
    exit /b %errorlevel%
)

:try_file_assoc
%*
exit /b %errorlevel%

:fail
echo.
echo Failed. Check messages above.
pause
exit /b 1
