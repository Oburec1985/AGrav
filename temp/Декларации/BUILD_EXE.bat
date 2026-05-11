@echo off
title Build EXE (PyInstaller)

echo Step 1: Installing/Updating PyInstaller and dependencies...
python -m pip install --upgrade pip
python -m pip install pyinstaller pdfplumber openpyxl pandas

echo.
echo Step 2: Building EXE file...
echo This may take a few minutes. Please wait...
python -m PyInstaller --onefile --name "Parser_GTD" fill_tnved.py

echo.
if exist dist\Parser_GTD.exe (
    echo [SUCCESS] Your EXE file is ready in: dist\Parser_GTD.exe
    echo You can now copy this file to any other PC.
) else (
    echo [ERROR] Build failed. Please check the messages above.
)

pause
