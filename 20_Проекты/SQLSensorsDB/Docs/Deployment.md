# Инструкция по развертыванию

Этот документ поможет быстро запустить систему Sensors DB на новом рабочем месте.

---

## 1. Подготовка окружения
Убедитесь, что установлены **Python 3.10+** и **Node.js 18+**.

---

## 2. Развертывание и Запуск

### Шаг 1: Наполнение базы (Импорт)
Это основной шаг. Скрипт сам создаст файл базы данных, настроит категории и импортирует датчики из Obsidian.
```bash
cd c:\Oburec\Antigravity\Projects\SQLSensorsDB\src\backend
python import_obsidian.py
```

### Шаг 2: Запуск Бэкенда (API)
Сервер будет доступен по адресу: `http://127.0.0.1:8888`.
```bash
cd c:\Oburec\Antigravity\Projects\SQLSensorsDB\src\backend
python -m uvicorn app.main:app --reload --port 8888
```

### Шаг 3: Запуск Фронтенда (UI)
Интерфейс откроется в браузере (обычно `http://localhost:5173`).
```bash
cd c:\Oburec\Antigravity\Projects\SQLSensorsDB\src\frontend
npm run dev
```

---

## 📂 Вспомогательные скрипты
- **`seed_db.bat`**: Сброс базы к тестовому состоянию (удаляет всё и создает один пример). Использовать только для отладки UI без реальных данных.

---
*Инструкция актуальна на 2026-04-13.*
