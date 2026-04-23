# 🤖 Antigravity: Gemini Flash через Proxy

Краткая инструкция по подключению `Gemini Flash` в окружении Antigravity через прокси.

## Вывод

Да, подключить можно, если прокси дает рабочий выход к API Google, а не только открывает обычные сайты.

Для API важен доступ к адресам уровня:
- `generativelanguage.googleapis.com`
- `*.googleapis.com`

Если прокси или серверный выход остаются в RU-географии или режут Google API, `Gemini Flash` не заработает даже при рабочем браузере.

## Что уже есть в AGrav

- Для обхода блокировок ИИ уже описан маршрут через [VLESS Reality](../..//15_Дом/Сети_и_Связь/30_Устройства_и_Клиенты/Настройка_VLESS_Reality.md).
- В инструментах AGrav уже используется официальный Python SDK `google.genai`, см. `00_Система/Инструменты/smart_parse_pdf.py`.

## Рекомендуемый вариант

1. Поднять прокси или туннель с внешним выходом.
2. Получить `GEMINI_API_KEY` в Google AI Studio.
3. В Antigravity использовать официальный SDK `google-genai`.
4. Перед запуском выставить переменные окружения:

```powershell
$env:GEMINI_API_KEY = "YOUR_KEY"
$env:HTTPS_PROXY = "http://user:pass@host:port"
```

5. Если используется SOCKS5, прокинуть его явно через `http_options`.

## Минимальный пример

```python
from google import genai
from google.genai import types

client = genai.Client(
    api_key="YOUR_KEY",
    http_options=types.HttpOptions(
        client_args={"proxy": "socks5://127.0.0.1:1080"},
        async_client_args={"proxy": "socks5://127.0.0.1:1080"},
    ),
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Ping",
)

print(response.text)
```

## Для Antigravity

Если Antigravity запускает Python-утилиты AGrav, обычно достаточно двух сценариев:

1. **HTTP/HTTPS proxy через переменные среды**
   Подходит, если прокси обычный и прозрачно пропускает `googleapis`.

2. **SOCKS5 proxy через `http_options`**
   Подходит для локального клиента `v2rayN`, `Nekoray`, `Clash`, `sing-box` и похожих.

## Практическая схема

Самый реалистичный путь для твоего контура:

1. Поднять маршрут через [VLESS Reality](../..//15_Дом/Сети_и_Связь/30_Устройства_и_Клиенты/Настройка_VLESS_Reality.md).
2. На ПК дать локальный HTTP/SOCKS-порт через клиент.
3. Запустить Antigravity или Python-скрипт с `HTTPS_PROXY` или `socks5`.
4. Проверить коротким запросом `generate_content`.

## Примечания

- Старые материалы в AGrav местами упоминают `gemini-1.5-flash`; для новых интеграций лучше брать актуальную линию `gemini-2.5-flash`, если нет причины держаться за legacy.
- Если нужен не просто proxy, а свой API gateway, официальный SDK также поддерживает `base_url`.

---
[🦊 Настройка Proxy](./Настройка_Proxy.md) | [🛡️ VLESS Reality](../../15_Дом/Сети_и_Связь/30_Устройства_и_Клиенты/Настройка_VLESS_Reality.md) | [⚙️ Системное оглавление](../../00_Система/Оглавление.md)
