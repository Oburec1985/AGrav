@echo off
set DXGETTEXT="C:\Program Files (x86)\dxgettext\dxgettext.exe"
set OUT_DIR=locale\en\LC_MESSAGES
if not exist "%OUT_DIR%" mkdir "%OUT_DIR%"
%DXGETTEXT% --delphi -b . -o "%OUT_DIR%"\ --nonascii
pause
