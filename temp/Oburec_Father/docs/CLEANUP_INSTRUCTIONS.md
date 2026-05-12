# 🧹 Инструкция по очистке "хвостов" Zapret (для переустановки)

Если при установке через `opkg install zapret` возникает ошибка:
`Collected errors: * pkg_run_script: package "zapret" preinst script returned status 44.`

Это означает, что на роутере остались файлы от предыдущей ручной установки, которые блокируют пакетный менеджер.

### Шаги для полной очистки:

Выполните следующие команды через SSH (или используя `ssh_manager.py`):

1. **Остановка сервиса**:
   ```bash
   /etc/init.d/zapret stop
   ```

2. **Удаление файлов и ссылок**:
   ```bash
   rm -rf /opt/zapret
   rm -f /etc/init.d/zapret
   rm -f /etc/rc.d/S*zapret*
   rm -f /etc/nftables.d/10-zapret.nft
   ```

3. **(Опционально) Удаление конфликтующего zapret2**:
   ```bash
   opkg remove luci-app-zapret2 zapret2
   rm -rf /opt/zapret2
   rm -f /etc/config/zapret2
   ```

### После очистки:
Теперь вы можете зайти в LuCI (Система -> Программное обеспечение) или выполнить `opkg install zapret` — установка должна пройти без ошибок.

---
*Документ подготовлен для проекта **Oburec_Father***
