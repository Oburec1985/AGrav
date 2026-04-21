# 🛡️ Инструкция: VLESS + Reality

Протокол VLESS с технологией Reality — это один из самых эффективных и простых способов обхода DPI, не требующий собственного домена и настройки SSL-сертификатов на стороне сервера.

## Как это работает
Вместо того чтобы выпускать свой сертификат, Reality «заимствует» (клонирует) сертификат у существующего популярного ресурса (например, `google.com` или `microsoft.com`). При анализе со стороны провайдера соединение выглядит как обычное посещение этого сайта.

## Параметры подключения (для ручной настройки)
*   **Protocol:** `vless`
*   **Port:** `8445` (порт 8443 был занят)
*   **Flow:** `xtls-rprx-vision` (рекомендуется для ПК)
*   **Transport:** `TCP`
*   **Security:** `reality`
*   **SNI:** `www.google.com`
*   **Fingerprint:** `chrome`
*   **Public Key:** `x_rNm4e7-Y6X7d1cA0Dns-UHIFkMZhtshCbf6vWaShw`
*   **ShortId:** `5760`

## Рекомендуемые приложения
1. **Windows:** [v2rayN](https://github.com/2dust/v2rayN/releases)
2. **Android:** [v2rayNG](https://github.com/2dust/v2rayNG/releases) или [Nekobox](https://github.com/MatsuriDayo/NekoBoxForAndroid/releases)
3. **iOS:** [Shadowrocket](https://apps.apple.com/app/shadowrocket/id932747118) (платное) или [Streisand](https://apps.apple.com/app/streisand/id6450534064)
4. **macOS:** [V2RayXS](https://github.com/tzm6/V2RayXS) или [FoXray](https://apps.apple.com/app/foxray/id6448898396)

---

## 🤖 Обход блокировок ИИ (Gemini, Claude, OpenAI)
На сервере настроен **Cloudflare WARP**, который позволяет обходить региональные ограничения для следующих сервисов:
- **Google Gemini** (`gemini.google.com`, `aistudio.google.com`)
- **Anthropic Claude** (`claude.ai`, `anthropic.com`)
- **OpenAI / ChatGPT** (`chatgpt.com`, `openai.com`)

> [!TIP]
> **Памятка по расширению:** Если вы захотите направить ВЕСЬ трафик через WARP, зайдите в панель 3x-ui -> Настройки Xray -> Правила. Измените правило `AI-Bypass` или создайте новое, указав `warp` в качестве исходящего тега для всех доменов.

---
*Создано в рамках настройки сервера 138.124.85.38. 2026-04-16.*
