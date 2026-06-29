@echo off
chcp 65001 > nul
set PYTHONPATH=%~dp0
python src/test_local.py
pause
