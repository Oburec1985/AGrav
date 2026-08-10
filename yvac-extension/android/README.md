# Yandex Video Ad Cleaner for Kiwi Browser Android

Это отдельная Android/Kiwi-версия расширения.

## Как установить в Kiwi

1. Скопируй папку `android` на телефон.
2. Открой Kiwi Browser.
3. Открой `chrome://extensions`.
4. Включи `Developer mode`.
5. Нажми `+(from .zip/.crx/.user.js)` или `Load unpacked`, если этот пункт есть в твоей версии Kiwi.
6. Выбери папку `android` или ZIP-архив этой папки.
7. Открой `yandex.ru/video` и проверь ролик.

## Если Kiwi просит ZIP

На ПК можно создать ZIP из этой папки:

```powershell
Compress-Archive -Path .\yvac-extension\android\* -DestinationPath .\yvac-extension\yvac-kiwi-android.zip -Force
```

Потом перенеси `yvac-kiwi-android.zip` на телефон и выбери его в Kiwi.

## Ограничения Android

Chrome Android расширения не поддерживает. Эта версия рассчитана именно на Kiwi Browser.
Сетевые блокировки сделаны через Manifest V3 `declarativeNetRequest`, а авто-пропуск и чистка плеера работают через content script.
