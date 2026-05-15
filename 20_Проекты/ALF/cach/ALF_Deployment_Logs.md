# ALF Project: Integration & Deployment Log (May 2026)

## 📌 Context
Integration of Telegram bot into FastAPI lifecycle and preparation for Amvera Cloud deployment.

## 🛠 Key Changes & Architecture
- **Unified Backend**: Telegram bot (aiogram) now runs as an `asyncio.create_task` during FastAPI `on_startup`.
  - [main.py](file:///c:/Oburec/Antigravity/Projects/ALF/backend/app/main.py)
- **Database Conflict Resolution**:
  - Local Docker Postgres moved to port **5433** to avoid conflict with Windows native Postgres (port 5432).
  - [docker-compose.yml](file:///c:/Oburec/Antigravity/Projects/ALF/docker-compose.yml)
- **Local Automation**:
  - `run_alf.bat` updated to handle venv, dependencies, port 5433, and concurrent launch of Backend/Bot and Frontend.
  - [run_alf.bat](file:///c:/Oburec/Antigravity/Projects/ALF/run_alf.bat)
- **Amvera Config**:
  - Added persistent volume for `static/uploads` to preserve user images.
  - [amvera.yml](file:///c:/Oburec/Antigravity/Projects/ALF/backend/amvera.yml)

## 🔧 Troubleshooting Tips (Local)
- **Auth Error**: If password fails after `.env` change, run:
  `docker exec alf_db psql -U alf_user -d alf_database -c "ALTER USER alf_user WITH PASSWORD 'alf_password';"`
- **Port 5432 conflict**: If Docker fails to bind 5432, it's likely Windows Postgres Service. Check with `netstat -ano | findstr :5432`.

## 🚀 Amvera Deployment Checklist
- [ ] Set `DATABASE_URL` (Internal Amvera DB)
- [ ] Set `TELEGRAM_BOT_TOKEN`
- [ ] Set `SMTP_PASSWORD` (Mail.ru app password)
- [ ] Set `BACKEND_URL` (e.g., `https://alf-backend-oburec.amvera.io`)
- [ ] Ensure `python-dotenv` is in `requirements.txt`.

---
*Last updated: 2026-05-15 by Antigravity AI*
