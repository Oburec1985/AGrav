@echo off
title GTD Parser Starter

:: 1. Check if Python is already installed
python --version >nul 2>&1
if %errorlevel% == 0 (
    set "PY_EXE=python"
    goto :run
)

py --version >nul 2>&1
if %errorlevel% == 0 (
    set "PY_EXE=py"
    goto :run
)

:: 2. If not found, try to install
echo Python not found. Attempting automatic installation...

where winget >nul 2>&1
if %errorlevel% == 0 (
    echo Installing via winget...
    winget install --id Python.Python.3.12 --exact --silent --accept-source-agreements --accept-package-agreements
    if %errorlevel% == 0 (
        echo Installation started. Please RESTART this file after it finishes.
        pause
        exit /b
    )
)

echo Downloading installer via curl...
curl -L "https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe" -o py_inst.exe
if exist py_inst.exe (
    echo Running installer...
    start /wait py_inst.exe /quiet PrependPath=1
    del py_inst.exe
    echo Done. Please RESTART this file to apply changes.
    pause
    exit /b
)

echo ERROR: Could not install Python automatically.
echo Please install it manually from https://www.python.org/
pause
exit /b

:run
echo Starting parser...
%PY_EXE% fill_tnved.py
if %errorlevel% neq 0 (
    echo.
    echo Parser finished with error.
    pause
)
