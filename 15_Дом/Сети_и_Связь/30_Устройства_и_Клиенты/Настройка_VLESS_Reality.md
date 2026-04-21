# 🛡️ Инструкция: Подключение через VLESS Reality

Практическое руководство по настройке клиентских приложений для работы с персональным сервером. О теории протокола Reality читайте в [[10_Теория_и_Методы/DPI_и_Методы_Обхода|Методах обхода]].

## Параметры подключения (для ручной настройки)
*   **Protocol:** `vless`
*   **Port:** `8445`
*   **Flow:** `xtls-rprx-vision` (рекомендуется для ПК)
*   **Security:** `reality`
*   **SNI:** `www.google.com`
*   **Fingerprint:** `chrome`
*   **Public Key:** `x_rNm4e7-Y6X7d1cA0Dns-UHIFkMZhtshCbf6vWaShw`
*   **ShortId:** `5760`

---

## Рекомендуемые приложения

| Платформа | Приложение | Ссылка |
| :--- | :--- | :--- |
| **Windows** | v2rayN | [GitHub Releases](https://github.com/2dust/v2rayN/releases) |
| **Android** | v2rayNG / Nekobox | [v2rayNG](https://github.com/2dust/v2rayNG/releases) |
| **iOS** | Shadowrocket / Streisand | [App Store](https://apps.apple.com/app/shadowrocket/id932747118) |
| **macOS** | V2RayXS / FoXray | [GitHub](https://github.com/tzm6/V2RayXS) |

---

## 🤖 Обход блокировок ИИ (Gemini, Claude, OpenAI)
На сервере настроен выход через **Cloudflare WARP**, что автоматически открывает доступ к:
- **Google Gemini** (`gemini.google.com`)
- **Anthropic Claude** (`claude.ai`)
- **OpenAI / ChatGPT** (`chatgpt.com`)

> [!TIP]
> **Маршрутизация:** Чтобы направить ВЕСЬ трафик через WARP на стороне сервера, используйте правила в панели 3x-ui (инструкция в карточке [[20_Инфраструктура_и_Серверы/Hiplet_138.124.85.38|сервера]]).

---
*Документ актуализирован: 2026-04-21*
