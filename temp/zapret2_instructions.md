# Инструкция по настройке Zapret2 (YouTube Bypass)

В этом файле приведены параметры для ручной настройки `zapret2` через LuCI (веб-интерфейс) или текстовый файл `/etc/config/zapret2`, а также готовый блок текста для копирования в стратегию YouTube.

## 1. Таблица параметров (основные настройки)

Эти параметры необходимо задать в разделе **Main** (основные настройки zapret2):

| Параметр в LuCI | Опция в UCI (`/etc/config/zapret2`) | Рекомендуемое значение | Описание |
| :--- | :--- | :--- | :--- |
| **Enabled** | `enabled` | `1` | Включить службу `zapret2` |
| **Debug** | `debug` | `0` (или `1` для отладки) | Логирование отладки в `/tmp/zapret2/` |
| **Desync mark** | `desync_mark` | `0x2` | Маркер пакетов (во избежание конфликтов и петель с ZeroBlock/Sing-box) |
| **Desync mark postnat** | `desync_mark_postnat` | `0x20000000` | Маркер для POSTNAT |
| **Postnat** | `postnat` | `1` | Включить режим POSTNAT |
| **NFQWS ports TCP** | `nfqws_ports_tcp` | `80,443` | Порты TCP для перехвата |
| **NFQWS ports UDP** | `nfqws_ports_udp` | `443` | Порты UDP для перехвата |
| **Qnum** | `qnum` | `300` | Номер очереди NFQUEUE |
| **Custom scripts** | `custom_scripts` | `1` | Включить использование кастомных скриптов |

---

## 2. Блок текста для вставки в стратегию `youtube`

Создайте в веб-интерфейсе LuCI (или найдите в `/etc/config/zapret2`) стратегию с именем **youtube** и примените к ней следующие настройки:
* **Protocol**: `tcp`
* **Port**: `443`
* **Filter L3**: `ipv4`
* **Filter L7**: `tls`
* **Hostlist**: `list_hosts_youtube` (файл должен содержать домены: `googlevideo.com`, `youtube.com`, `ytimg.com`, `ggpht.com` и т.д.)

### Текст для поля "Script" / "Опции desync" (скопируйте целиком):

```text
--out-range=-s34228
--in-range=-s5556 --lua-desync=circular:fails=2:maxtime=60
--in-range=x
--payload=tls_client_hello
--lua-desync=multidisorder:pos=2:strategy=1
--lua-desync=multidisorder:pos=1:strategy=2
--lua-desync=multidisorder:pos=midsld:strategy=3
--lua-desync=multidisorder:pos=1,midsld:strategy=4
--lua-desync=tcpseg:pos=0,-1:seqovl=1:strategy=5
--lua-desync=drop:strategy=5
--lua-desync=multisplit:pos=10:seqovl=1:strategy=6
--lua-desync=fake:blob=fake_default_tls:ip_ttl=2:tls_mod=rnd,dupsid,padencap:repeats=1:strategy=7
--lua-desync=fake:blob=fake_default_tls:badsum:repeats=1:strategy=8
--lua-desync=fake:blob=0x00000000:badsum:repeats=1:strategy=9
--lua-desync=fake:blob=fake_default_tls:badsum:tls_mod=rnd,dupsid:repeats=1:strategy=9
--lua-desync=multisplit:blob=fake_default_tls:badsum:pos=2:nodrop:repeats=1:strategy=10
```
