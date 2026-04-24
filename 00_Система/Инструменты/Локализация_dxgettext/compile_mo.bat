@echo off
set MSGFMT="c:\Oburec\OburecGH\sharedUtils\utils\locTools\msgfmt.exe"
set PO_FILE=locale\en\LC_MESSAGES\default.po
set MO_FILE=locale\en\LC_MESSAGES\default.mo
echo Compiling %PO_FILE%...
%MSGFMT% -o "%MO_FILE%" "%PO_FILE%"
pause
