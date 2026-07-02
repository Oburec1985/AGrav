# RecorderLnxUtf8Restore

Восстановление кириллицы в `.pas` RecorderLnx после поломки кодировки (`???` в комментариях).

## Когда использовать

- В `uMainForm.pas` или другом модуле комментарии стали `???`.
- AI/Cursor diff испортил UTF-8 или CP1251 файл.
- Нужно вернуть текст из git и перевести модуль на UTF-8.

## Скрипты

### uMainForm (комментарии `???`)

Путь: `OburecGH/Lazarus/RecorderLnx/cach/_fix_umainform_encoding.py`

```powershell
cd D:\works\OburecGH\Lazarus\RecorderLnx
python cach\_fix_umainform_encoding.py
```

Делает:
1. `git show origin/master:Lazarus/RecorderLnx/UI/uMainForm.pas` → decode **cp1251**;
2. `{$codepage UTF8}`, запись UTF-8;
3. Повторное применение актуальных правок кода (uses, `SetupStatusBanner`, …).

### Новый UI-модуль: mojibake в Caption (`РќР°…`)

Путь: `OburecGH/Lazarus/RecorderLnx/cach/_fix_oscillogram_settings_encoding.py`

```powershell
python cach\_fix_oscillogram_settings_encoding.py
```

Делает для `UI/uRecorderOscillogramSettingsDialog.pas`:
1. `{$codepage UTF8}` вместо cp1251;
2. снимает `CP1251ToUTF8(...)` с литералов;
3. убирает `LConvEncoding` из uses;
4. сохраняет UTF-8, CRLF, без BOM.

Для другого модуля — скопировать скрипт и поменять `TARGET`.

## Проверка

```powershell
python -c "t=open('UI/uMainForm.pas',encoding='utf-8').read(); print('???', t.count('???'))"
C:\lazarus\lazbuild.exe -B RecorderLnx.lpi
```

## Профилактика

См. `RecorderLnx/Docs/source-encoding.md` и AGrav `10_Кодировка_Исходников.md`.

Связано: [[20_Проекты/Разработка_Delphi/Lazarus/RecorderLnx/Docs/10_Кодировка_Исходников]]
