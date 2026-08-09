---
memory_id: 09bcca41-a2f6-4dfe-b063-038529e7b5ec
hash: ab56792ca1a33bcd32d44fc6e233a92c
last_indexed: '2026-07-07T09:37:14.473853'
---
# Инструмент локализации Delphi проектов (dxgettext)

Этот инструмент автоматизирует процесс локализации Delphi проектов с использованием `dxgettext` и современного `GNU Gettext`.
Основано на руководстве: [localization_guide.md](../../20_Проекты/Разработка_Delphi/Localization/localization_guide.md)

## Скрипты

Скрипты находятся в папке `Локализация_dxgettext` рядом с этой заметкой. Их нужно скопировать в корень локализуемого проекта и запускать оттуда.

### 1. `extract_po.bat` (Сбор строк)
Сканирует исходники проекта (включая файлы `.pas`, `.dpr`, `.dfm`) и извлекает строки для перевода.
- Обязательно использует флаг `--nonascii` для поддержки кириллицы.
- Создает структуру папок `locale\en\LC_MESSAGES\` и файл `default.po`.

### 2. `compile_mo.bat` (Компиляция)
Компилирует переведенный файл `default.po` в бинарный `default.mo`, который используется приложением.
- Использует современную версию `msgfmt.exe` из `c:\Oburec\OburecGH\sharedUtils\utils\locTools\`.

## Использование
1. Скопируйте `extract_po.bat` и `compile_mo.bat` в корень вашего Delphi проекта.
2. Запустите `extract_po.bat` для сбора строк (создаст/обновит `default.po`).
3. Переведите строки в файле `locale\en\LC_MESSAGES\default.po`.
4. Запустите `compile_mo.bat` для генерации файла `.mo`.
