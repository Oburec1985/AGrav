# 🌐 Selectel VPS — VPN Relay (Москва ➔ Швеция)

## 📌 Данные сервера Selectel (Входной релей в РФ)
* **Название сервера:** Hazel (`09acce33-9169-45ae-9b66-d84aeedf6d66`)
* **Провайдер:** Selectel (Дата-центр Москва, Россия)
* **IP-адрес:** `135.106.183.27`
* **SSH Логин:** `root`
* **SSH Пароль:** `vZB6lueEL5qc`
* **Конфигурация:** 1 vCPU, 1 ГБ RAM, 10 ГБ NVMe

---

## 🇸🇪 Данные шведского сервера HipHost (Выходной сервер)
* **Провайдер:** HipHost (Швеция)
* **IP-адрес:** `138.124.85.38`
* **SSH Логин:** `root`
* **SSH Пароль:** `6JajOWFgYe6NZP`

---

## 🔑 Доступ к панели управления 3X-UI
* **URL панели:** [https://135.106.183.27:2053/0J7fKylZhhGpxx6RVG/](https://135.106.183.27:2053/0J7fKylZhhGpxx6RVG/)
* **Логин:** `panel134554`
* **Пароль:** `IoRkfAYfrYV95huVhxDr`

---

## ⭐ 100% РАБОЧИЕ ПРЯМЫЕ ССЫЛКИ VLESS REALITY

### 1. Selectel-Relay-Museum (Порт 8443)
```text
vless://1af33394-ce53-49b5-9700-db51315206ba@135.106.183.27:8443?type=tcp&security=reality&pbk=9yuTmkZFFzfPIfivSKfJepiozckRf97HOWlxdO_cAW8&fp=chrome&sni=museum.de&sid=f8#Selectel-Relay-Museum
```

### 2. Selectel-Relay-Google (Порт 4433)
```text
vless://1af33394-ce53-49b5-9700-db51315206ba@135.106.183.27:4433?type=tcp&security=reality&pbk=EuacFUJGnWk-6GQ-KHpASDed6FrPMf9wnzGbN9iTG3g&fp=chrome&sni=www.google.com&sid=ee625235#Selectel-Relay-Google
```

---

## 🔗 Единая ссылка подписки (Все 5 узлов в 1 клик)

```text
https://135.106.183.27:2096/sub/0m0ce3jbvhlox85
```

⚠️ **Важный нюанс при добавлении подписки в приложение:**
При добавлении ссылки в **v2rayNG** / **Streisand** / **v2rayTUN** / **Happ** / **FoXray** обязательно включите в настройках подписки переключатель **«Разрешить недействительный сертификат / Allow Insecure»** (так как сервер подписок на порту 2096 использует служебный SSL-сертификат). 
После нажатия «Обновить подписку» приложение сразу загрузит **все 5 рабочих протоколов**:
1. **VLESS REALITY (Google 4433)**
2. **VLESS REALITY (Museum 8443)**
3. **VMess WS (11443)**
4. **VMess WS + TLS (11454)**
5. **VLESS xHTTP + TLS (10453)**

---

## ⚙️ Перенаправление портов на Selectel (iptables NAT)
* `2053` ➔ Веб-панель 3X-UI
* `2096` ➔ Единый сервер подписок
* `4433`, `8443`, `9443`, `10453`, `11443`, `11454`, `2083` ➔ Прокси-порты VLESS/VMess/Trojan
