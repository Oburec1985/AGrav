@echo off
title Заполнение кодов ТН ВЭД
echo Запуск парсера деклараций...
echo.

:: Проверка наличия Python
where py >nul 2>nul
if %errorlevel%==0 (
    py fill_tnved.py
) else (
    where python >nul 2>nul
    if %errorlevel%==0 (
        python fill_tnved.py
    ) else (
        echo ОШИБКА: Python не найден в системе!
        echo Установите Python с сайта python.org
        pause
    )
)
