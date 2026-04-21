# Raw Extraction: podkop

**2026-01-01T01:02:33 | Василий Фёдорович Конырев**
Ура!!! У меня заработало эта х для ребёнка то есть Roblox! Я удалил всё что связано с роблоксом из http://192.168.1.1/cgi-bin/luci/admin/services/podkop и сделал всё по этой инструкции: https://youtu.be/4FIeIRycVNA

---

**2026-01-01T12:24:26 | Alex EfremoFF**
С Новым годом, друзья!
Ткните носом новичка, для Трубы что лучше использовать - podkop или zapret?
Если есть ссылка на инструкцию, буду вдвойне благодарен!

---

**2026-01-01T15:41:59 | Routerich**
Если есть вторая секция в Podkop можно в неё подкинуть принудительный прокси.

---

**2026-01-01T15:46:16 | Routerich**
https://podkop.net/docs/sections/

---

**2026-01-01T15:53:40 | Александр Рокотов**
Хорошо))
Спасибо)
Тоесть мне тогда нужно создать "третью" секцию в podkop, в ней указать свой ключ VLESS и в ней указать IP консоли?
(а все остальные сервисы будут работать через секции созданные скриптом?)

---

**2026-01-01T20:31:00 | Anna Bagler**
Попробуйте это https://t.me/routerich/3845/386082, если ещё нет в подкопе. Службы - Podkop. Ceкции вы увидите глазами по названиям.

---

**2026-01-02T00:35:43 | Anna Bagler**
Службы - Запрет, отключить, стоп. Система - Планировщик. Удалить 0 4 * * * service zapret restart
Нажать Сохранить.
Cлужбы - Podkop. Секции, main, списки сообщества, добавить YouTube.

---

**2026-01-02T00:52:37 | Anna Bagler**
@EvgenyMak1990 Службы - Podkop.

---

**2026-01-02T02:00:28 | Oleg**
дооброй ночи! а как не просто удаленный доступ к роутеру настроить, а чтобы и интернет из любой точки через роутер шел?)(чтобы можно было по мобильному интернету youtube через podkop смотреть)

---

**2026-01-02T03:24:34 | Routerich**
https://podkop.net/docs/tunnels/awg_settings/ Пакеты ставить не надо, есть в прошивке уже

---

**2026-01-02T05:19:40 | Oleg**
Сейчас я залил новую прошивку и сбросил в ноль роутер, теперь работает

 Анализ запущен: 2026-01-02 05:17:30
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Configuring wget-ssl.

== ПРОВЕРКА DNS  (Прошивка: 24.10.4)
==============================================================
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.0.14

== ИНТЕРФЕЙС awg10 (ДЕТАЛИ)
==============================================================
  Статус                : UP (ON)  ↓2.15 MB / ↑0.30 MB
  Пинг (ya.ru via awg10): 26.619 / 27.484 ms (0 из 10 потеряно)

== ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM)
==============================================================
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/1.1 200 OK) [TLSv1.3]

== СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ)
==============================================================
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | ОТКЛ
  youtubeUnblock  | STOPPED                        | ОТКЛ

== ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ
==============================================================
  !!! КРИТ: Пересечение между podkop и zapret:
    podkop                    : Youtube_Discord
    zapret                    : zapret-hosts-google.txt
    Домены: googlevideo.com youtube.com 

  podkop списки Youtube_Discord: youtube,discord
  podkop списки       main: geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10
==============================================================
== СИСТЕМНЫЕ РЕСУРСЫ
==============================================================
  LAN IP: 192.168.169.1 (Прошивка: 24.10.4)
  CPU: 0.33 | RAM: 21% | NAND: 27% занято / 48.8M доступно
  13 9 * * * /usr/bin/podkop list_update
==============================================================
root@RouteRich:~# 
 

До этого показывало что подкоп работал, но при подключении к инсте, ютубу или дискорду

---

**2026-01-02T12:14:17 | Mister_Ask**
вроде бы да но как бы не все понятно

===== Информация о системе =====
Routerich AX3000
aarch64_cortex-a53
24.10.4

===== Пользовательские пакеты =====
podkop | luci-app-podkop
zapret | luci-app-zapret
unzip | luci-i18n-package-manager-ru
wget-ssl | luci-i18n-wdoc-singbox-ru
luci-app-package-manager | luci-base
doh-proxy | luci-i18n-filemanager-ru
opera-proxy | luci-app-youtubeUnblock
luci-i18n-wdoc-warp-ru | luci-app-wol
sing-box-tiny | luci-i18n-firewall-ru
luci-app-filemanager | luci-app-upnp
luci-i18n-openvpn-ru | luci-app-ttyd
luci-i18n-wdoc-wg-ru | luci-proto-ppp
luci-i18n-zapret2-ru | luci-app-ksmbd
kmod-amneziawg | luci-theme-routerich
luci-i18n-podkop-ru | luci-mod-system
luci-i18n-ksmbd-ru | luci-mod-status
miniupnpd-nftables | luci-i18n-wol-ru
routerich-defaults | luci-app-openvpn
coreutils-base64 | luci-app-firewall
luci-i18n-base-ru | luci-i18n-upnp-ru
luci-i18n-ttyd-ru

===== Flow Offloading =====
HW: on | FIX: yes

===== Проверка GitHub =====
API: ok | Limit: 54

===== Проверка IPv4 / IPv6 =====
Google IPv4: ok (16.723 ms)
Google IPv6: fail

===== Настройки Zapret =====
72.20251227-r1 | запущен
50-stun4all
TCP: 80,443,2053,2083,2087,2096,8443
UDP: 443,19294-19344,50000-50100,88,500,1024-19293,19345-49999,50101-65535

===== Стратегия =====
#v6
#Yv03
--filter-tcp=443
--hostlist=/opt/zapret/ipset/zapret-hosts-google.txt
--dpi-desync=fake,multisplit
--dpi-desync-split-pos=2,sld
--dpi-desync-fake-tls=0x0F0F0F0F
--dpi-desync-fake-tls=/opt/zapret/files/fake/tls_clienthello_www_google_com.bin
--dpi-desync-fake-tls-mod=rnd,dupsid,sni=ggpht.com
--dpi-desync-split-seqovl=620
--dpi-desync-split-seqovl-pattern=/opt/zapret/files/fake/tls_clienthello_www_google_com.bin
--dpi-desync-fooling=badsum,badseq
--new
--filter-tcp=443
--hostlist-exclude=/opt/zapret/ipset/zapret-hosts-user-exclude.txt
--dpi-desync=hostfakesplit
--dpi-desync-hostfakesplit-mod=host=max.ru
--dpi-desync-hostfakesplit-midhost=host-2
--dpi-desync-split-seqovl=726
--dpi-desync-fooling=badsum,badseq
--dpi-desync-badseq-increment=0
--new
--filter-udp=19294-19344,50000-50100
--filter-l7=discord,stun
--dpi-desync=fake
--dpi-desync-repeats=6
--new
--filter-tcp=2053,2083,2087,2096,8443
--hostlist-domains=discord.media
--dpi-desync=multisplit
--dpi-desync-split-seqovl=652
--dpi-desync-split-pos=2
--dpi-desync-split-seqovl-pattern=/opt/zapret/files/fake/tls_clienthello_www_google_com.bin
--new
--filter-udp=88,500,1024-19293,19345-49999,50101-65535
--dpi-desync=fake
--dpi-desync-cutoff=d2
--dpi-desync-any-protocol=1
--dpi-desync-fake-unknown-udp=/opt/zapret/files/fake/quic_initial_www_google_com.bin

===== Доступность сайтов =====
[OK]   gosuslugi.ru              [OK]   nnmclub.to
[OK]   esia.gosuslugi.ru         [OK]   openwrt.org
[OK]   nalog.ru                  [OK]   sxyprn.net
[OK]   lkfl2.nalog.ru            [OK]   pornhub.com
[OK]   rutube.ru                 [OK]   discord.com
[OK]   youtube.com               [OK]   x.com
[OK]   instagram.com             [OK]   filmix.my
[OK]   rutor.info                [OK]   flightradar24.com
[OK]   ntc.party                 [OK]   cdn77.com
[OK]   rutracker.org             [OK]   play.google.com
[OK]   epidemz.net.co            [OK]   genderize.io

---

**2026-01-02T12:25:05 | Gomer Simpson**
Система - планировщик
0 5 * * * service podkop restart

---

**2026-01-02T15:25:15 | 𝔈𝔳𝔦𝔩𝔖𝔞𝔱**
Анализ запущен: 2026-01-02 15:24:07
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Configuring wget-ssl.

== ПРОВЕРКА DNS  (Прошивка: 24.10.4)
==============================================================
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.2.71

== ИНТЕРФЕЙС awg10 (ДЕТАЛИ)
==============================================================
  Статус                : UP (ON)  ↓0.94 MB / ↑413.91 MB
  Пинг (ya.ru via awg10): 15.681 / 23.083 ms (0 из 10 потеряно)

== ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM)
==============================================================
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОФЛАЙН
------------------------------------------------------
  Spider mode enabled. Check if remote file exists.
  --2026-01-02 15:24:32--  https://www.youtube.com/
  Resolving www.youtube.com... 142.250.102.198
  Connecting to www.youtube.com|142.250.102.198|:443... connected.
  Unable to establish SSL connection.
------------------------------------------------------
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 142.250.179.142
--------------------------------------------------------------

== СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ)
==============================================================
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

== ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ
==============================================================
  podkop списки    Discord: discord
  podkop списки       main: geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: dns.adguard-dns.com / 8.8.8.8
  Версия podkop: v0.7.9
==============================================================
== СИСТЕМНЫЕ РЕСУРСЫ
==============================================================
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.36 | RAM: 30% | NAND: 26% занято / 49.2M доступно
  0 4 * * * /etc/init.d/podkop list_update
  0 4 * * * service zapret restart
  13 9 * * * /usr/bin/podkop list_update
==============================================================

---

**2026-01-02T17:20:01 | Anna Bagler**
Стратегии запрета будете пробовать подбирать? Если нет, то запрет отключить и стопнуть. Службы - Запрет в меню роутера.
Службы - Podkop, прокрутиться до секции discord, добавить список yt.

---

**2026-01-02T18:35:10 | Anna Bagler**
Службы - Podkop. Cекции, найти discord, yt крестиком удалить. В секцию main добавить. Применить. Секунд через 40 после применения проверить.

---

**2026-01-02T20:38:15 | Routerich**
Раньше в записях днс прописывался, через CommsDNS, когда оперу прокси не использовали.
А так в Podkop в GeoBlock

---

**2026-01-02T20:59:01 | Routerich**
Здравствуйте.
Пробовать отключить zapret /podkop и проверять.
Если из за него искать что может мешать
А если и так не работает, то добавить домены в Podkop

---

**2026-01-02T21:13:44 | Bullet for my valentine Poison**
https://podkop.net/docs/sections/ читайте

---

**2026-01-03T07:08:24 | Routerich**
Здравствуйте.
https://podkop.net/docs/sections/

---

**2026-01-03T10:45:48 | Roman Vorobev**
Всем добра. Скажите пожалуйста, скрипт№5 ставит Podkop 7.9?

---

**2026-01-03T11:05:49 | Routerich**
Здравствуйте.
Есть в Podkop такой баг, если включить список Cloudflare, то awg WARP отваливается

---

**2026-01-03T14:12:07 | Routerich**
Здравствуйте.
Пробовать отключить zapret, Podkop и проверять без них

---

**2026-01-03T14:12:29 | Routerich**
Здравствуйте.
Podkop не надо, а вот zapret первый можно

---

**2026-01-03T14:25:42 | Alex EfremoFF**
Господа, а доступноть трекеров реально настроить через youtubeUnblock или стоит влетать в podkop/zapret?

---

**2026-01-03T15:08:05 | Egor Mikhaylov**
Добрый день!
Может кто-то подскажет, как решить такую проблему
- Установлен podkop
- Настроена секции с маршрутом для белых списков (есть vless, где работает инет через подмену servername на белый)

Так вот проблема, что если у меня включают белые списки на сотовой сети и не дай бог я перезапущу роутер - то подкоп пойдет обновлять списки с Github, а Github, как вы понимаете не в белых списках.. 
 но даже если Github добавить в ручной список доменов, то при запуске podkop не может скачать списки(подписки), потому-что еще не запустился, а при запуске он сначала получает списки, получается замкнутый круг, это можно побороть вручную, но хотелось бы как-то это бесшовно делать

Есть-ли какие-то способы заставить podkop получать списки (подписки) после своего запуска, чтобы он мог скачать их через поднятый им же vless?

---

**2026-01-03T16:56:31 | Oleg Belskiy**
Приветствую. В общем, приобрёл виртуальную машину. Выдали доменное имя, пароли, ip адрес. И хотелось в Podkop добавить VPS третьей секцией. Да вот не задача, как это сделать?)) Можете подсказать, где почитать пошагово, а лучше посмотреть.

---

**2026-01-03T16:57:44 | ɟlopɐ ɹǝʇʇıɹɔ**
https://podkop.net/docs/sections/

---

**2026-01-03T17:30:09 | Александр Козлов**
Прошил, Podkop поставил и настроил, дурилку для YouTube тоже. Никаких сложностей не возникло. До этого тоже самое на ax3000t и rax делал.

---

**2026-01-03T21:08:06 | Slava Moniava**
Здравствуйте, подскажите,пожалуйста, где почитать про установку SOCKS5, как я понял, он нужен для того, чтобы я мог пользоваться удаленным сервером, типа ProxyLine. Задача быть для работодателя в определенном регионе, находясь при этом физически в РФ. Я установил Podkop, купил там ключ Hysteria2, но ip у меня российский. Как я понял SOCKS5 должен помочь. Надеюсь правильно объяснил ситуацию. У меня Routerich AX3000 (OpenWRT 24.10).

---

**2026-01-03T21:09:26 | Dmitrii Burenin**
Бета версия скрипта для обхода ограничений.
Основное отличие от скрипта №5, что тут  используется система пакетов Watchdog для отслеживания за стабильностью интернета и используемых средств обхода (подробнее тут https://t.me/routerich/173678/342341)

Важно: 
1. Перед запуском сделайте бэкап (Система->Восстановление и обновление->Создать архив)
2. Если у вас всё работает хорошо, в частности youtube не надо его запускать.
3. Если не готовы сбрасывать роутер после неудачной отработки скрипта, лучше не запускайте скрипт.

Если вы всё таки решились запустить его, то от вас мне нужны полные логи запуска скрипта от начала его работы до завершения. Файл с логами будет по пути /root/run.log, можете его скачать через 
Веб морда роутера->NAS->Файловый менеджер->/root/run.log, скачать 
Потом пришлите его, для анализа.

P.S. запустится только на прошивках версии не ниже 24.10.2

Сам код для запуска ниже.
sh <(wget -q -O - https://raw.githubusercontent.com/routerich/RouterichAX3000_configs/refs/heads/wdoctrack/universal_config_new_podkop.sh) 2>&1 | tee /root/run.log

---

**2026-01-03T21:15:18 | Routerich**
https://podkop.net/docs/client-dns/

---

**2026-01-03T21:27:13 | Alex EfremoFF**
Сейчас пришлю скриншоты, в Podkop есть ряд ошибок

---

**2026-01-03T21:28:58 | S B**
Всем привет, не знаю туда ли пишу, но - нужна консультация специалиста по настройке, готов оплатить

Дано - Routerich AX3000 v1.0 FW - RouteRich 24.10.1

Когда купил его то по инструкциям и изрядному пердолингу настроил ютуб анблок + подкоп так, что у меня по автоматически обновляемому списку выборочно использовался мой впн внутри роутера и открывались все сайты без проблем. Плюс исправил ошибку приставки xbox 

несколько дней назад всё полетело по одному месту - начали сильно глючить сервисы (например adobe перестал открываться, Creative Cloud лицензионный вообще отказывался видеть сервер и включаться) - всё, что смог сделать это снести подкоп, но поставить новый уже не получается по инструкции от создателя, выдаёт ошибки при выполнении команд в терминале. При этом все сервисы начинают работать если подключиться через смартфон как модем.

Что мне нужно - я так понимаю сбросить всё до завода, обновить если надо, быстро восстановить настройки сети и порекомендовать (помочь установить) в роутер всё что сейчас есть интересного (параметр конечно странный, согласен, но нет никакой возможности изучать всё досконально). Цель - сделать всё также автоматизированный доступ ко всем сайтам (я так понимаю это и есть главный функционал podkop, включая проброс для xbox (пользователи знают, там гимор большой у консолей не для рынка рф, постоянно приходилось перебирать dns).

Пишите в идеале сразу в личку с ценой на услуги)

---

**2026-01-04T07:47:41 | VK11**
Добрый день. стоит  24.10.4 r28959-29397011cc RR-3.8.2 скрипт 5 после  работы в podkop  v0.7.10-r1 нет ни одной секции, ранее ставил на другой роутер тоже самое там был 6 подкоп и секции всякие активные и дашборд с информацией.

---

**2026-01-04T09:51:27 | Anna Bagler**
Службы - Zapret, отключить и стоп. Службы - Podkop, прокручиваемся до секции discord, добавляем список yt в списках сообщества.

---

**2026-01-04T14:54:14 | Routerich**
Здравствуйте.
В Podkop, в настройках смените провайдера днс, например на гугл.

---

**2026-01-04T17:50:17 | Денис Сурков**
Всем привет, кому ни будь удалось найти данные, которые нужно прописать в podkop, чтобы работал eshop  на консоли Nintendo Switch?

---

**2026-01-04T20:10:57 | Walter White**
кто знает, если стоит podkop с vless, почему ip определяется на 2ip, как от провайдера?

---

**2026-01-04T20:14:02 | Routerich**
Естественно.
Podkop это средство точечной маршрутизации.

---

**2026-01-04T23:44:35 | Anna Bagler**
Если ресурс через podkop, то ограничения не подействуют.

---

**2026-01-04T23:49:49 | Anna Bagler**
Скрипт 5 из Интернет без границ и общие принципы тут https://podkop.net/docs/sections/

---

**2026-01-05T01:14:09 | Макс**
📡 Global check run!━
━━━━━━━━━━━━━━━━━━━━━━━━━━�
�️ System info�
�️ Podkop:        v0.7.10 (latest: 0.7.10)�
�️ LuCI App:      v0.7.10�
� Sing-box:      1.12.12�
� OpenWrt:       RouteRich 24.10.4 r28959-29397011cc RR-3.8.2�
� Device:        Routerich AX3000 v1━
━━━━━━━━━━━━━━━━━━━━━━━━━━➡
️ DNS status✅
 Bootstrap DNS: 8.8.8.8✅
 Main DNS: 8.8.8.8 [doh]✅
 DNS on router⚠
️ dont_touch_dhcp is enabled. 📄 DHCP config:c
onfig dnsmasq 
option domainneeded '1' 
option boguspriv '1' 
option localise_queries '1' 
option rebind_protection '1' 
option rebind_localhost '1' 
option local '/lan/' 
option domain 'lan' 
option expandhosts '1' 
option nonegcache '1' 
option cachesize '0' 
option authoritative '1' 
option readethers '1' 
option leasefile '/tmp/dhcp.leases' 
option resolvfile '/tmp/resolv.conf.d/resolv.conf.auto' 
option nonwildcard '1' 
option localservice '1' 
option ednspacket_max '1232' 
option confdir '/tmp/dnsmasq.d' 
option noresolv '1' 
option strictorder '1' 
option filter_aaaa '1' 
list server '127.0.0.1#5359'━

━━━━━━━━━━━━━━━━━━━━━━━━━━�
� Sing-box status✅
 Sing-box installed✅
 Sing-box version is compatible (newer than 1.12.4)✅
 Sing-box service exist✅
 Sing-box autostart disabled✅
 Sing-box process running✅
 Sing-box listening ports━
━━━━━━━━━━━━━━━━━━━━━━━━━━�
� NFT rules status✅
 Table exist✅
 Rules mangle exist✅
 Rules mangle counters✅
 Rules mangle output exist✅
 Rules mangle output counters✅
 Rules proxy exist✅
 Rules proxy counters✅
 Additional marking rules found━
━━━━━━━━━━━━━━━━━━━━━━━━━━�
� Podkop configc

onfig settings 'settings' 
option dns_type 'doh' 
option dns_server '8.8.8.8' 
option bootstrap_dns_server '8.8.8.8' 
option dns_rewrite_ttl '60' 
option enable_output_network_interface '0' 
option enable_badwan_interface_monitoring '0' 
option enable_yacd '0' 
option disable_quic '1' 
option update_interval '1d' 
option download_lists_via_proxy '1' 
option dont_touch_dhcp '1' 
option config_path '/etc/sing-box/config.json' 
option cache_path '/tmp/sing-box/cache.db' 
option exclude_ntp '1' 
option shutdown_correctly '0' 
option download_lists_via_proxy_section 'main' 
list source_network_interfaces 'br-lan'c

onfig section 'main' 
option connection_type 'proxy' 
option proxy_config_type 'outbound' 
option enable_udp_over_tcp '0' 
option shutdown_correctly '1' 
option user_domain_list_type 'text' 
option user_subnet_list_type 'disabled' 
option mixed_proxy_enabled '0' 
option outbound_json 'MASKED' 
option user_domains_text 'myip.com' 
list community_lists 'geoblock' 
list community_lists 'block' 
list community_lists 'meta' 
list community_lists 'twitter' 
list community_lists 'hdrezka' 
list community_lists 'tiktok' 
list community_lists 'google_ai' 
list community_lists 'telegram'c

onfig section 'Youtube_Discord' 
option connection_type 'vpn' 
option interface 'awg10' 
option domain_resolver_enabled '0' 
option user_domain_list_type 'text' 
option user_subnet_list_type 'disabled' 
option mixed_proxy_enabled '0' 
option user_domains_text 'amazonaws.comt
witch.tvf
unpay.com' 
list community_lists 'youtube' 
list community_lists 'discord'━

━━━━━━━━━━━━━━━━━━━━━━━━━━�
� WAN configc
onfig interface 'wan' 
option device 'eth1' 
option proto 'dhcp'━

━━━━━━━━━━━━━━━━━━━━━━━━━━⚠
️ WARP detected: 162.159.192.10━
━━━━━━━━━━━━━━━━━━━━━━━━━━⚠
️ Zapret detected━
━━━━━━━━━━━━━━━━━━━━━━━━━━�
� FakeIP status✅
 Router DNS is routed through sing-box✅
 Sing-box works with FakeIP: 198.18.0.63

---

**2026-01-05T10:45:19 | Дмитрий Витальевич**
Здравствуйте! Можно ли в podkop добавить список vless ссылок что бы он автоматически подключался к варианту с наименьшим пингом?

---

**2026-01-05T10:47:04 | Dark Ghost**
Попробуйте прочитать документацию: https://podkop.net/

---

**2026-01-05T10:49:47 | Routerich**
Здравствуйте.
URL-Test
https://podkop.net/docs/sections/

---

**2026-01-05T12:11:56 | Kiss_My_Axe**
Что бы я сделал.
1) Скрипт №5 накатить повторно.
2) 
service podkop stop
cp /etc/config/podkop /etc/config/podkop~
cp /etc/config/podkop-opkg /etc/config/podkop
service podkop start
И заново скрипт №5.

---

**2026-01-05T13:36:41 | Anna Bagler**
То, что пустите в подкоп, будет с обходом, что не пустите, не будет https://podkop.net/docs/sections/

---

**2026-01-05T15:31:34 | ㅤ**
Глядика! Эвоно как изогнулся!
И так сейчас о том как подключаться к впн через переподключение к другой сети своего роутера
для началу надобно Sing-box (эй пссс Podkop работает на Sing-box) и свободная подсеть
создаём новую сеть (название пароль все дела)
Создаём новый интерфейс "Статический адрес" в устройство указываем нашу сеть
Далее в "IPv4-адресс" указываем свободный адрес (к примеру 192.168.100.1) и указываем маску 255.255.255.0
В "Настройки межсетевого экрана" указываем "lan" а в "DHCP-сервер" нажимаем настроить "DHCP-сервер" и ничего не трогаем жмём сохранить применить 
Время Sing-box!
В rout.rules пишем
{
    "source_ip_cidr": [
        "192.168.100.0/0"
    ],
    "outbound": ""
}
И в outbound указываем тег вашего outbound
всё

---

**2026-01-05T17:56:42 | Станислав Дмитриев**
podkop

---

**2026-01-05T18:35:26 | Никита Стокгольм**
Добрый вечер, вообщем столкнулся со странной работой роутер, у меня версия на 512 уже наверное около года, на неделе начал отваливаться Podkop. Грешил на сервера, что отваливаются, но я начал заходить в настройки роутера а роутер грузится либо очень медленно, либо с ошибками или вообще не загружает панель. Думал что может кабель где то зажал но нет, по воздуху с телефона такая же фигня. Иногда интернет тоже отваливается. Прошивку сбрасывал, перепрошивал. Роутер вроде не перегревается, из софта стоит только Podkop, остальное всё из коробки

---

**2026-01-05T18:55:09 | Routerich**
https://podkop.net/docs/tunnels/awg_settings/

---

**2026-01-05T19:32:28 | Routerich**
Службы->Podkop->полностью маршртизированные ip адреса и туда добавить ip

---

**2026-01-05T21:22:11 | Routerich**
И добавлять в Podkop

---

**2026-01-05T22:10:21 | Evgeny**
Бонжур 
Заказал роутер месяца 2 назад, наконец-то привезли 


Накатил последний скрипт без ошибок, все завелось, кроме Ютуба на Андроиде (на ios все ок) и на нативном приложении youtube для smart tv Samsung

Добавил лист youtube в podkop (main), завелось везде 

Спасибо всем причастным как к роутеру, так и бесконечной борьбой с роскомпозором, вы - лучшие!

---

**2026-01-05T22:37:51 | Aleksey Vydrin**
—>>>Новый скрипт для обхода блокировок<<<<—

Скрипт №5

Перед запуском скрипта прочитайте внимательно и выполните то, что тут описано https://t.me/routerich/3845/333975

Разработали универсальный скрипт, как для старых версий прошивок, так и для новых он подходит. Он сам определит версию прошивки и запустит нужный скрипт.

Что этот скрипт откроет для Вас

У вас заработают все запрещенные в России сайты, такие как Youtube (будет без рекламы, может и с рекламой), Instagram, Twitter, Facebook, Discord (с голосом, может и без голоса), WhatsApp и Telegram звонки, торрент трекеры, сервисы которые в геоблоке (ChatGPT, Copilot, Обновления Windows, BrawlStars, Xbox).

Так же отказались от ручного ввода данных в запущенном скрипте, теперь данные параметры нужно передавать до запуска скрипта

Первый параметр указывает нужно ли вручную вписать параметры AmneziaWG (если у вас свой сервер или свой конфиг) - y/n
Второй параметр указываем нужно ли установить Podkop, перезаписать конфигурацию Podkop - y/n

Если у вас старая прошивка 23.05.5, 24.10.1, то у вас установится Podkop версии 0.2.5, если у вас новая версия прошивки 24.10.2 и выше, то установится новый Podkop 0.7.10.

Порядок действий для запуска скрипта

1. Заходим на веб морду роутера routerich.lan и авторизуемся. Логин: root, Password: по умолчанию пароля нет
2. Переходим в Службы->Терминал->Вводим Login: root, нажимаем "Enter", Password: по умолчанию пароля нет (если задавали пароль на веб морду, тогда его вводим). При вводе пароль не отображается. После ввода нажимаем "Enter".
3. Копируем код для запуска, который расположен ниже и вставляем в терминал (правой кнопкой мыши нажать и он вставится). 
4. Дождитесь завершения работы скрипта, он вас об этом уведомит
5. Профит. Вы великолепны. 

Код для запуска по умолчанию с автоматической генерацией AWG WARP и установкой Podkop

sh <(wget -q -O - https://raw.githubusercontent.com/routerich/RouterichAX3000_configs/refs/heads/wdoctrack/run_universal_config.sh) 2>&1 | tee /root/run.log

Код для запуска с параметрами ручного ввода конфигурации и установкой Podkop

sh <(wget -O - https://raw.githubusercontent.com/routerich/RouterichAX3000_configs/refs/heads/wdoctrack/run_universal_config.sh) y y

Код для запуска с автоматической генерацией AWG WARP и без установки/замены конфигурации Podkop (подходит для тех, кто повторно запускает, но уже внёс изменения в Podkop (чтобы конфигурация Podkop не затерлась))

sh <(wget -O - https://raw.githubusercontent.com/routerich/RouterichAX3000_configs/refs/heads/wdoctrack/run_universal_config.sh) n n

Для версии Podkop 0.2.5

Те домены, которые заблокировал РКН необходимо добавлять в
Службы->Podkop->Основные настройки->Пользовательские домены-> и в конец списка добавляем свои домены по аналогии с вышестоящими.

Те домены, которые заблокированы по ГЕОблоку необходимо добавлять в
Службы->Podkop->Второй маршрут->Пользовательские домены-> и в конец списка добавляем свои домены по аналогии с вышестоящими.

Выше описанное актуально только для тех, у кого AWG WARP работает, в таком случае будет два маршрута в Podkop, а если у вас после выполнения скрипта, AWG WARP не заработал, то у вас будет только один маршрут, основной и вы только туда вносите домены для обхода, не важно, геоблок или РКН блок, всё туда.

Для версии Podkop 0.7.10

Службы->Podkop->Свои домены добавляйте в секцию Main в пользовательские домены, так же там очень много готовых списков можете их там выбирать, но ни в коем случае не включайте одинаковые списки в разных секциях Podkop, возникнут проблемы.

P.S. если у вас после запуска скрипта не установился Podkop или вы видите какие-то ошибки при работе скрипта, будьте добры выслать логи запуска скрипта они находятся по пути /root/run.log
Чтобы вытащить логи делаем следующее:
1. Открываем веб морду
2. Переходим в раздел NAS->Файловый менеджер
3. Дальше переходим в папку /root/
4. Находим файл run.log и нажимаем на кнопочку с белой стрелкой на синем фоне ⬇️
5. И отправляем скачанный файл в чат

---

**2026-01-06T09:09:42 | Андрей Стыврин**
Через podkop заработало на смартТВ.
Можно как-то настроить ZAPRET2 и PODKOP, чтобы для определённых узлов работало что-то одно?

---

**2026-01-06T09:16:54 | Андрей Стыврин**
PODKOP при этом отключать?

---

**2026-01-06T09:29:11 | Михаил**
К слову. Информации для. У меня отлично работал zapret2 вместе с podkop с доменами  youtube.  Стики на телеках в статику и в исключения podkop. В итоге через podkop в youtube ходят все устройства кроме стиков на телеках, стики через второй запрет. Такая схема довольно живенько отработала. Сейчас до кучи поднял в podkope byedpi, запрет2 теперь держу в офлайне. Так что схема с одновременным использованием на один домен и запрeта2 и подкопа у меня оказалась вполне живуча.

---

**2026-01-06T09:38:56 | Андрей Стыврин**
PODKOP не гасил, Раша инсайд не включена, стратегии нашлись, Ю заработал.
Благодарю!

---

**2026-01-06T11:49:43 | Routerich**
Здравствуйте.
Отслеживать все домены на которые обращения идут и добавлять в Podkop либо полностью устройство в Podkop пускать

---

**2026-01-06T14:23:45 | Anna Bagler**
https://podkop.net/docs/sections/ - после скрипта 5 настраивайте со своим vless.

---

**2026-01-06T14:32:19 | 𝐼𝓁𝓀𝒾𝓃**
мне нужно было второй с podkop а я первый установил..

---

**2026-01-06T14:38:16 | 𝐼𝓁𝓀𝒾𝓃**
не подскажите как удалить запрет?  установил скрипт №5 без podkop...

---

**2026-01-06T15:04:49 | Dugar**
nslookup fakeip.podkop.fyi вот тут прилетает публичный адрес, а не  подкопа.
нейросетка говорит это из-за приоритета ipv6 над ipv4 в убунте. Вот пытаюсь вырубить его. Как бы не вырубить всю убунту))

---

**2026-01-06T15:07:44 | Dugar**
в терминале ПК в ответ на команду. Эту команду из доки подкопа нашёл. Вот тут https://podkop.net/docs/troubleshooting/?utm_source=podkop#diagnostika-na-klientskom-ustrojstve-pk-smartfon

---

**2026-01-06T15:32:43 | Dugar**
Починил.

Дело было в приоритете ipv6 над ipv4.

Диагностировал проблему с вашей помощью (проглядел последнюю строчку, тут сорян) и докой подкопа тут https://podkop.net/docs/troubleshooting/. Проверил получение fakeIP

Ну а далее, поменял приоритет с помощью инструкции https://wiki.tiukov.com/books/linux/page/prioritet-ipv6.

Всё заработало.

Спасибо!

---

**2026-01-06T15:33:43 | Anna Bagler**
Службы - Podkop - Диагностика, запустить диагностику.
Когда вы проверяете стратегии запрета, проверяйте на всех нужных вам устройствах и останавливайтесь, когда везде пошло или не заработало после всех. Тогда можно смотреть дальше.

---

**2026-01-06T16:26:07 | Mikhail Sabinin**
Здравствуйте! Через podkop не работает WhatsApp на iPhone, на android работает. Что может быть?

---

**2026-01-06T18:24:18 | Routerich**
Здравствуйте.
а теперь сравните свой список и список, который в Podkop вшит, именно список YouTube.
https://github.com/itdoginfo/allow-domains/blob/main/Services/youtube.lst

---

**2026-01-06T18:40:29 | mrack**
view_logs 
  [0;36m[2026-01-06 19:40:07] [0m  [0;32mNo 'Starting podkop' message found, showing last 100 lines [0m
Tue Jan  6 17:30:45 2026 daemon.err sing-box[12495]:  [31mERROR [0m[63212] [ [38;5;136m3559156088 [0m 22.46s] connection: open connection to edge-mqtt.facebook.com:443 using outbound/http[main-out]: unexpected status: 502 Bad Gateway
Tue Jan  6 18:55:37 2026 daemon.err sing-box[12495]:  [31mERROR [0m[68304] [ [38;5;205m2272888765 [0m 1.9s] connection: open connection to gameplay.intel.com:443 using outbound/http[main-out]: unexpected status: 502 Bad Gateway
Tue Jan  6 18:55:38 2026 daemon.err sing-box[12495]:  [31mERROR [0m[68305] [ [38;5;221m190258913 [0m 266ms] connection: open connection to gameplay.intel.com:443 using outbound/http[main-out]: unexpected status: 502 Bad Gateway
Tue Jan  6 19:00:38 2026 daemon.err sing-box[12495]:  [31mERROR [0m[68605] [ [38;5;73m3234092857 [0m 299ms] connection: open connection to gameplay.intel.com:443 using outbound/http[main-out]: unexpected status: 502 Bad Gateway
Tue Jan  6 19:00:38 2026 daemon.err sing-box[12495]:  [31mERROR [0m[68605] [ [38;5;192m82544126 [0m 280ms] connection: open connection to gameplay.intel.com:443 using outbound/http[main-out]: unexpected status: 502 Bad Gateway
Tue Jan  6 19:17:23 2026 daemon.err sing-box[12495]:  [31mERROR [0m[69610] [ [38;5;109m751302493 [0m 269ms] connection: open connection to gameplay.intel.com:443 using outbound/http[main-out]: unexpected status: 502 Bad Gateway
Tue Jan  6 19:17:23 2026 daemon.err sing-box[12495]:  [31mERROR [0m[69610] [ [38;5;231m1289687040 [0m 390ms] connection: open connection to gameplay.intel.com:443 using outbound/http[main-out]: unexpected status: 502 Bad Gateway
Tue Jan  6 19:22:24 2026 daemon.err sing-box[12495]:  [31mERROR [0m[69910] [ [38;5;122m3663300205 [0m 257ms] connection: open connection to gameplay.intel.com:443 using outbound/http[main-out]: unexpected status: 502 Bad Gateway
Tue Jan  6 19:22:24 2026 daemon.err sing-box[12495]:  [31mERROR [0m[69911] [ [38;5;87m1033402951 [0m 333ms] connection: open connection to gameplay.intel.com:443 using outbound/http[main-out]: unexpected status: 502 Bad Gateway
Tue Jan  6 19:27:24 2026 daemon.err sing-box[12495]:  [31mERROR [0m[70211] [ [38;5;156m528712523 [0m 232ms] connection: open connection to gameplay.intel.com:443 using outbound/http[main-out]: unexpected status: 502 Bad Gateway
Tue Jan  6 19:27:24 2026 daemon.err sing-box[12495]:  [31mERROR [0m[70211] [ [38;5;222m2436128777 [0m 234ms] connection: open connection to gameplay.intel.com:443 using outbound/http[main-out]: unexpected status: 502 Bad Gateway
Tue Jan  6 19:32:25 2026 daemon.err sing-box[12495]:  [31mERROR [0m[70511] [ [38;5;192m1864280871 [0m 243ms] connection: open connection to gameplay.intel.com:443 using outbound/http[main-out]: unexpected status: 502 Bad Gateway
Tue Jan  6 19:32:25 2026 daemon.err sing-box[12495]:  [31mERROR [0m[70512] [ [38;5;178m2057900706 [0m 316ms] connection: open connection to gameplay.intel.com:443 using outbound/http[main-out]: unexpected status: 502 Bad Gateway
Tue Jan  6 19:37:25 2026 daemon.err sing-box[12495]:  [31mERROR [0m[70812] [ [38;5;75m3091531067 [0m 265ms] connection: open connection to gameplay.intel.com:443 using outbound/http[main-out]: unexpected status: 502 Bad Gateway
Tue Jan  6 19:37:26 2026 daemon.err sing-box[12495]:  [31mERROR [0m[70813] [ [38;5;138m3515144058 [0m 416ms] connection: open connection to gameplay.intel.com:443 using outbound/http[main-out]: unexpected status: 502 Bad Gateway

---

**2026-01-06T20:16:02 | Алексей**
проще описать что я делал

какими то обходами с компа (после установки zapret и podkop на роутере) не пользовался.

установил игру - сразу начал ловить ошибку

попробовал переустановить скрипт (воспроизвел скрипт №5) - ошибка осталась

попробовал отключить zapret - ошибка осталась

дальше я написал сюда

ну и в дополнении то, что после воспроизведения 5 скрипта подкоп странный стал

скрипт запускал командой 
sh <(wget -q -O - https://raw.githubusercontent.com/routerich/RouterichAX3000_configs/refs/heads/wdoctrack/run_universal_config.sh) 2>&1 | tee /root/run.log

---

**2026-01-06T20:54:08 | Роман**
Всё работет, использую podkop, zapret2. Да и не заблокирована игра.

---

**2026-01-06T23:29:01 | Anna Bagler**
https://podkop.net/docs/sections/

---

**2026-01-07T07:17:13 | Routerich**
Здравствуйте.
Логи смотрите что там.
Или просто попробуйте перезапустить Podkop

---

**2026-01-07T13:17:53 | Gomer Simpson**
Система - Автозапуск - Podkop stop.

---

**2026-01-07T13:44:06 | Аркадий Курилов**
Здравствуйте. Сегодня стал плохо работать youtube. До этого только стримы плохо грузились. Сегодня вообще видео еле грузит.
Настраивал по 5 скрипту

Прошивка: RouteRich 24.10.4 r28959-29397011cc RR-3.8.2 / LuCI openwrt-24.10 branch 25.302.55195~bfcef12

Установленные службы:
Podkop
Сервер печати p910nd
Zapret
Интернет-детектор
DNS Сервисы
Wake on LAN
Терминал
UPnP

Статус запрета
Service autorun status:  Включено
Service daemons status:  Выполняется [3/3]
FW type:  nftables
HostLists update mode:  user entries only

Конфиг podkop
config settings 'settings'
        option dns_type 'doh'
        option dns_server 'dns.adguard-dns.com'
        option bootstrap_dns_server '8.8.8.8'
        option dns_rewrite_ttl '60'
        option enable_output_network_interface '0'
        option enable_badwan_interface_monitoring '0'
        option enable_yacd '0'
        option disable_quic '1'
        option update_interval '1d'
        option download_lists_via_proxy '1'
        option dont_touch_dhcp '1'
        option config_path '/etc/sing-box/config.json'
        option cache_path '/tmp/sing-box/cache.db'
        option exclude_ntp '1'
        option shutdown_correctly '0'
        option download_lists_via_proxy_section 'main'
        list source_network_interfaces 'br-lan'

config section 'main'
        option connection_type 'proxy'
        option proxy_config_type 'outbound'
        option enable_udp_over_tcp '0'
        option shutdown_correctly '1'
        option user_domain_list_type 'text'
        option user_subnet_list_type 'disabled'
        option mixed_proxy_enabled '0'
        option outbound_json '{
  "type": "http",
  "tag": "http-proxy",
  "server": "127.0.0.1",
  "server_port": 18080
}'
        option user_domains_text 'myip.com
c10.patreonusercontent.com'
        list community_lists 'geoblock'
        list community_lists 'block'
        list community_lists 'meta'
        list community_lists 'twitter'
        list community_lists 'hdrezka'
        list community_lists 'tiktok'
        list community_lists 'google_ai'
        list community_lists 'youtube'
        list community_lists 'porn'

config section 'Discord'
        option connection_type 'vpn'
        option interface 'awg10'
        option domain_resolver_enabled '0'
        option user_domain_list_type 'text'
        option user_subnet_list_type 'disabled'
        option mixed_proxy_enabled '0'
        list community_lists 'discord'
        option user_domains_text 'amazonaws.com
accounts.google.ru
pypi.nvidia.com'

---

**2026-01-07T16:00:34 | Routerich**
Здравствуйте.
А если остановить Podkop, то нет такой ошибки?

---

**2026-01-07T17:03:52 | Serj Shu**
А тапнуть на плашке Podkop 🤔😁

---

**2026-01-07T20:31:46 | Routerich**
Здравствуйте.
Пустите ютуб через Zapret тогда, а из Podkop уберите

---

**2026-01-07T22:07:19 | Александр**
Добрый вечер. Обновился,а подкоп кажет теперь так:  
view_logs 
 Wed Jan  7 21:55:49 2026 user.notice podkop: [info] Starting podkop
Wed Jan  7 21:55:49 2026 user.notice podkop: [info] Check Requirements
Wed Jan  7 21:55:49 2026 user.notice podkop: [error] Outbound section not found. Please check your configuration file (missing proxy_string, interface, outbound_json, or urltest_proxy_links). Aborted.

---

**2026-01-07T22:42:20 | Anna Bagler**
Если есть цель точечной маршрутизации, свои ссылки  на подписки vpn, стоит podkop поставить. 
Можно, но можно просто остановить и отключить и планировщик проверить.

---

**2026-01-08T10:54:42 | Vasa**
так ктож его знает... мож и поломали

вообще РР бы заняться своими списками. потому что у них всё таки используется несколько другая схема, чем предполагает Podkop изначально

---

**2026-01-08T17:06:12 | Bullet for my valentine Poison**
https://podkop.net

---

**2026-01-08T17:32:45 | Routerich**
Попробуйте сменить DNS провайдера в настройках Podkop  на гугл и проверить

---

**2026-01-08T17:48:06 | Anna Bagler**
Система - Автозапуск. Перезапустить opera-proxy, перезапустить podkop. Если не поможет, ещё раз запустить скрипт 5. Версия прошивки какая?

---

**2026-01-08T17:52:38 | Routerich**
c whatsapp всё сложно.
только локально впн включать или пускать устройство полностью в Podkop

---

**2026-01-08T18:28:55 | Routerich**
Покажите секции Podkop

---

**2026-01-08T19:14:23 | Снежный**
Я читал руководство podkop'а

---

**2026-01-08T19:27:40 | Uintik️️️🐈‍⬛**
Народ, а есть информация что случилось с сайтом podkop.net Уже несколько дней, не открывается.

---

**2026-01-08T19:32:07 | Routerich**
А если Podkop стопнуть? Норм скорость?

---

**2026-01-08T19:59:10 | Vladislav Zhulikov**
📥 Как добавить «Мир Танков» (Lesta) в Podkop на OpenWrt через AmneziaWG
---
1️⃣ Подключись к роутеру по SSH  
ssh root@192.168.1.1
---
2️⃣ Создай папку и файл с подсетями:
mkdir -p /etc/podkop
cat > /etc/podkop/lesta_subnets.txt <<EOF
92.223.0.0/16
185.137.128.0/17
EOF
---
3️⃣ Проверь, что файл создан:
cat /etc/podkop/lesta_subnets.txt
→ Должны отобразиться две строки.
---
4️⃣ Зайди в LuCI: `http://192.168.1.1/cgi-bin/luci/admin/services/podkop` → Службы → Podkop
---
5️⃣ Найди секцию `Youtube_Discord` (или другую, где используется `awg10`)
---
6️⃣ В поле «Список пользовательских доменов» добавь (если ещё не добавлены):
ce-ru.tanki.su login.p1.tanki.su login.p2.tanki.su login.p3.tanki.su login.p4.tanki.su login.p5.tanki.su login.p6.tanki.su login.p8.tanki.su login.p9.tanki.su cm.lesta.ru clientgw-ru.tanki.su rss.tanki.su xmppcs-wotru.lesta.ru cat-lgc.lstprod.net lgcps-ru-nsdb.lesta.ru ix-v-cat-rec-2.fe.lesta.pw www.wotp.vivox.com
---
7️⃣ В поле «Локальные списки подсетей» введи:
/etc/podkop/lesta_subnets.txt
→ Нажми «+» справа от поля.
---
8️⃣ Убедись, что:
- Тип соединения: VPN
- Интерфейс: awg10
- Тип списка подсетей: Текст (или «Включено»)
---
9️⃣ Нажми «Применить» внизу страницы
---
✅ Готово!  
Теперь весь трафик «Мира Танков» (и DNS, и UDP-бои) идёт через AmneziaWG — пинг отображается, лагов нет.
---
🔧 Если нужно обновить список — просто повтори шаг 2 с новыми подсетями.
---
Сохрани эту инструкцию — она работает для Podkop 0.7.0 + OpenWrt 24.10.5 + AmneziaWG.

---

**2026-01-08T20:27:59 | Routerich**
У вас zapret remittor не заработал, работает только опера прокси и WARP.
То есть Discord и YouTube через Podkop. Все должно работать

---

**2026-01-09T00:03:35 | Роман**
https://podkop.net/docs/install/
После установки vless или hysteria2 и собираете листы сообщества. Russia inside ставить не советую.

---

**2026-01-09T02:25:30 | Денис**
Добрый день! В скрипте 5 можно использовать свой shadowsocks сервер с плагином? Чтобы через него шел трафик тсп и юдп по доменам из вайтлиста. Если да, то какие шаги для этого? Те что в "Код для запуска с параметрами ручного ввода конфигурации и установкой Podkop"?

---

**2026-01-09T04:01:09 | Routerich**
Здравствуйте.
Ss можно использовать.
Просто установить первый вариант, а потом зайти в
Службы->Podkop - >в секции main изменить тип конфигурации на URL прокси и ввести свой ключ.

---

**2026-01-09T09:05:41 | ㅤРоман**
13 9 * * * /usr/bin/podkop list_update
из менить на 13 10 как раз время подошо почти

---

**2026-01-09T10:05:54 | Василий**
Приветствую, купил данный роутер по предзаказу, получил его буквально 31го декабря, до сих пор разбираюсь с подарочком)
по инструкции установил скрипт №5.
Всё заработало (на компе, смартфоне, смарт тв) но только проблемы с Discord, при голосовом звонке, и трансляции видео, сессия сбрасывается (пишет что он пытается постоянно подключится) и приходится закрывать полностью Discord и только тогда получается ещё раз созвонится. 
Как я понял у меня всё работает в этот момент через Podkop, через секцию YOUTUBE_DISCORD, а он уже через VPN AmneziaWG. 
Я попробовал вместо VPN AmneziaWG, поставить свой Proxy vless (Московский), история аналогичная, сбрасывается звонок я никого не слышу меня не слышат. 
Дальше я попробовал отключить Podkop, и включить Zapret но через Zapret не работает YOUTUBE на смарт тв, но при этом намного лучше работает Discord, хоть и не без проблем. 
Я короче много чего сам попробовал но так и не заработало как мне надо. 
Два вопроса после всего.
1. Есть ли вариант чтоб Zapret одновременно с Podkop. 
Если да то как пустить только Discord через Zapret.
2. Если будет работать только Podkop, что можно сделать чтоб починить Discord, и он работал без сбрасывания звонков.

---

**2026-01-09T10:09:43 | Routerich**
Здравствуйте.
Возможно.
Из запрет удалить, из настроек хосты Google Host list, оставить там какой нибудь домен заглушку
Из Podkop из секции Discord убрать список Discord и проверять

---

**2026-01-09T10:25:37 | Routerich**
Напишите сюда с логами
https://t.me/itdogchat/81758
В чат разработчика Podkop, может подскажут

---

**2026-01-09T10:30:38 | Routerich**
Мы не разработчики Podkop

---

**2026-01-09T11:16:18 | Routerich**
А список YouTube в секции Podkop выбрали?
Zapret остановили?

---

**2026-01-09T12:40:27 | Василий**
у меня не заработал Discord 
я в Google hostname entries удалил все домены поставил туда придуманный uhfkdjhw.com
обновил Zapret до версии v72.20251227
нажал кнопку Reset settings
И удалил из секции Discord в Podkop, но дискорд не грузится

---

**2026-01-09T13:39:26 | Sergey**
Господа, подскажите пожалуйста: можно ли объединить v2raya + podkop?

---

**2026-01-09T13:48:28 | Sergey**
Создать некий гибрид. Допустим, если v2raya - будет менять IP сайтов из списка на немецкий сервак. То Podkop будет через DPI открывать сайты, которые не указан в списке. Если немецкий сервак упадет, то Podkop подхватит. Хз, надеюсь нормально объяснил.

---

**2026-01-09T13:51:25 | Sergey**
Спасибо Большое! Меня просто друг запутал, а может быть я чего-то не понимаю. Он якобы использует v2raya + podkop. Вот его скриншоты.

---

**2026-01-09T13:59:51 | Sergey**
И что всё-таки лучше использовать? V2raya или Podkop? 
Ну и вдруг дадите совет, а то не знаю, где посоветоваться: суть в чем, у меня в квартире миниПК (интернет DHCP (без привязки к MAC адресу), proxmox (openwrt, agh)), а на даче хочу использовать специальный роутер на OpenWRT ZBT Z8102AX для мобильного интернета. (нет возможности подключить оптику) 
Так вот, я хочу использовать обход на даче с помощью домашнего миниПК. Допустим, через Wireguard. Это хорошая идея? Спасибо!

---

**2026-01-09T14:10:37 | Anna Bagler**
Вы же его добавляли как-то, аналогично удаляйте. Службы - Podkop. Ceкции и дальше глазами ищите.

---

**2026-01-09T14:54:37 | Anna Bagler**
Система - Автозапуск, найти opera-proxy, перезапустить, podkop, перезапустить. У вас что-то не так. Скрипт 5 https://t.me/routerich/3845/245550 точно повторно запускали?

---

**2026-01-09T16:17:45 | Routerich**
Здравствуйте.
Нужно отследить все домены на которые обращается и добавить их в Podkop

---

**2026-01-09T16:42:54 | Routerich**
В пользовательские домены Podkop добавить
roblox.com
rbxcdn.com
robloxdev.com
rbxinfra.net
И проверяйте

---

**2026-01-09T17:05:27 | Routerich**
Здравствуйте.
Для Telegram добавьте в Podkop список Telegram в секцию Discord

---

**2026-01-09T17:07:03 | Routerich**
Здравствуйте.
Для Telegram добавьте список Telegram в секцию Discord если он есть Podkop

---

**2026-01-09T17:34:10 | Routerich**
Значит то, что Podkop видит другой dns, не эталоннаый в настройках dnsmasq

---

**2026-01-09T18:20:26 | dirtybiker**
в работе только sb, podkop, в подкопе юаб, восап (дискорд, майн соотв.). Вобщем штатно с №5. Запрет откл.
 Фишка в чём, рутуб жопой поворачивается при гладкой работе ( ну попробую дома всё стопнуть, но тогда факт заработает, но остальное пабаразде), при ошибках перенаправлений - драсьте, он тут, как тут. Не, ну он так то нафиг нужен, малой мульты и с утуба позырит, прост осадочек такой, типа он при всех равных глохнет, а я понимай , как хочешь.

---

**2026-01-09T20:25:14 | Dmitriy**
но по крайней мере podkop он установил и zapret

---

**2026-01-09T22:50:33 | Umka**
Podkop сейчас

---

**2026-01-09T23:05:20 | Maxim =)))**
Если стоит zapret2 и podkop, норм, можно ставить?

---

**2026-01-10T09:04:10 | Routerich**
Можно либо новую секцию в Podkop добавить, либо существующюю изменить

---

**2026-01-10T09:10:19 | Routerich**
https://podkop.net/docs/

---

**2026-01-10T11:07:29 | Александр**
Добрый. Так и не решилось с этим, подскажите что делать?: view_logs 
 Sat Jan 10 11:06:47 2026 user.notice podkop: [info] Starting podkop
Sat Jan 10 11:06:47 2026 user.notice podkop: [info] Check Requirements
Sat Jan 10 11:06:47 2026 user.notice podkop: [error] Outbound section not found. Please check your configuration file (missing proxy_string, interface, outbound_json, or urltest_proxy_links). Aborted.

---

**2026-01-10T13:33:12 | Slava Moniava**
Привет! Помогите советом, пожалуйста. 
Хочу сделать так, чтобы все девайсы за Routerich AX3000 выходили в инет через казахстанский IP от ProxyLine, включая рабочий ноут с Cisco VPN. 
Сейчас схема подключения такая: Первый роутер к провайдеру - WAN Routerich - мои рабочие девайсы. 
Но проблема такая: На личном ПК со статичным IP+Podkop+hysteria2 работало идеально. А на рабочем ноуте сначала "connecting available", потом "permitted", после подключения корпоративного VPN,корп сеть всё равно видит Россию (утечки где-то есть?).
У меня есть прокси от ProxyLine. Как настроить Routerich, чтобы ВСЁ трафик (в т.ч. через corp VPN) шёл через мой ProxyLine KZ и не было утечек RU IP?
Как я понял Podkop/hysteria2 не подходит, нужен transparent proxy/tinyproxy/Passwall с моим upstream?
Есть ли готовый профиль/гайд есть под такую связку?
Заранее спасибо!

---

**2026-01-10T13:38:24 | Anna Bagler**
https://podkop.net/docs/workvpn/ посмотрите тут.

---

**2026-01-10T13:59:47 | Don Carleone**
Как настроить что бы например Ютуб, Дискорд работал через ByDPI, а все остальное через Passwall? В Podkop'е можно как-то настроить это?

---

**2026-01-10T15:24:27 | Сергей Катасонов**
Анализ запущен: 2026-01-10 15:21:59
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Configuring wget-ssl.

== ПРОВЕРКА DNS  (Прошивка: 24.10.4)
==============================================================
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.0.3

== ИНТЕРФЕЙС awg10 (ДЕТАЛИ)
==============================================================
  Статус                : UP (ON)  ↓0.00 MB / ↑0.06 MB
  Пинг (ya.ru via awg10): 43.777 / 45.811 ms (0 из 10 потеряно)

== ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM)
==============================================================
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/1.1 200 OK) [TLSv1.3]

== СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ)
==============================================================
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  youtubeUnblock  | STOPPED                        | ОТКЛ

== ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ
==============================================================
  podkop списки Youtube_Discord: youtube,discord
  podkop списки       main: geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10
==============================================================
== СИСТЕМНЫЕ РЕСУРСЫ
==============================================================
  LAN IP: 192.168.2.1 (Прошивка: 24.10.4)
  CPU: 0.42 | RAM: 43% | NAND: 26% занято / 49.1M доступно
  13 9 * * * /usr/bin/podkop list_update
==============================================================
root@RouteRich:~#

---

**2026-01-10T16:00:39 | Василий**
уже кажется получилось, обновил через  загрузку пакетов Zapret   v72.20260108
после в Podkop отключил в секции YOUTUBE_DISCORD, сам дискорд, и ресетнул настройки выбрал стратегию 
# Strategy TLS_AUTO_ALT3_by_Flowseal и убрал Host lists Google hostname entries, оставив там домен заглушку, и наконецто у меня заработал 
Discord  через запрет, а всё остальное через Podkop

---

**2026-01-10T16:01:55 | Vasa**
https://telegra.ph/Polnaya-instrukciya-nastrojki-xHTTP-v-Podkop-12-08

---

**2026-01-10T16:05:00 | Viktor**
Добрый день. Можете дать информацию как установить и включить службу podkop

---

**2026-01-10T16:07:21 | Routerich**
https://podkop.net/

---

**2026-01-10T18:11:13 | Routerich**
Если пользуетесь Podkop, то в
Службы->Podkop->Пользовательские домены

---

**2026-01-10T18:14:59 | Routerich**
Значит через Podkop

---

**2026-01-10T18:47:28 | Routerich**
Зайдите в службы - podkop - настройки - dns смените на гугл(у вас adguard сейчас) и нажмите применить и проверяйте

---

**2026-01-10T18:54:12 | Anna Bagler**
Службы - podkop. Диагностика, запустить диагностику. Скриншоты.

---

**2026-01-10T18:55:19 | Anna Bagler**
https://podkop.net/docs/sections/

---

**2026-01-10T19:05:48 | Вадим**
Просто периодами вообще доступ ко всему пропадает. Я понимаю пропадал бы доступ только к заблокированным ресурсам, но перестает работать вообще все. Вот например сейчас  такая же ситуация, ни один сайт не работает:
Sat Jan 10 19:01:56 2026 daemon.err sing-box[12220]:  [31mERROR [0m[1894] [ [38;5;214m2699487942 [0m 5.6s] connection: open connection to fakeip.podkop.fyi:8443 using outbound/direct[direct-out]: dial tcp 64.188.104.86:8443: i/o timeout
Sat Jan 10 19:02:01 2026 daemon.err sing-box[12220]:  [31mERROR [0m[1899] [ [38;5;113m2769574753 [0m 5.7s] connection: open connection to fakeip.podkop.fyi:8443 using outbound/direct[direct-out]: dial tcp 64.188.104.86:8443: i/o timeout
Sat Jan 10 19:02:30 2026 daemon.err sing-box[12220]:  [31mERROR [0m[1928] [ [38;5;192m1111307006 [0m 30.3s] connection: open connection to ip.podkop.fyi:443 using outbound/http[main-out]: unexpected status: 502 Bad Gateway
Sat Jan 10 19:03:59 2026 daemon.err sing-box[12220]:  [31mERROR [0m[2017] [ [38;5;228m166873306 [0m 30.0s] connection: open connection to 57.144.245.32:443 using outbound/http[main-out]: unexpected status: 502 Bad Gateway

---

**2026-01-10T21:30:06 | Евгений**
Подскажите, а Podkop можно поставить через веб или нужно логинется через терминал ?

---

**2026-01-10T21:49:00 | Евгений**
А где Podkop находится, youtubeUnblock в службах отображается, а Podkop нет ?

---

**2026-01-10T21:51:22 | Routerich**
luci-app-podkop пакет поставили?

---

**2026-01-10T21:51:32 | Илья Рябыкин**
в список пользовательских доменов секции MAIN Podkop Службы добавлен адрес ficbook.net
в терминале cmd 
C:\Users\ilya>nslookup ficbook.net
╤хЁтхЁ:  RouteRich.lan
Address:  fd81:8e04:45f9::1

╚ь :     ficbook.net
Address:  198.18.0.7
C:\Users\ilya>ping ficbook.net

Обмен пакетами с ficbook.net [198.18.0.7] с 32 байтами данных:
Превышен интервал ожидания для запроса.
Превышен интервал ожидания для запроса.
в терминале WSL
ilya@ryabykin:~$ nslookup ficbook.net
Server:         10.255.255.254
Address:        10.255.255.254#53

Name:   ficbook.net
Address: 198.18.0.7

ilya@ryabykin:~$ ping ficbook.net
PING ficbook.net (198.18.0.7) 56(84) bytes of data.
^C
--- ficbook.net ping statistics ---
79 packets transmitted, 0 received, 100% packet loss, time 79865ms

---

**2026-01-10T21:59:05 | Глеб**
Сегодня заметил, что Podkop начал резать скорость, с 400 до 20 мбит, при остановке службы скорость восстанавливается. Ранее такого не наблюдалось, прошивка последняя 24.10.4, скрипт базовый, без изменений. Как можно исправить?

---

**2026-01-10T22:16:57 | Глеб**
подскажите нубу, как провалиться в /etc/config/dhcp через терминал, что бы проверить/отредактировать настройки Podkop?
cd /etc/config/dhcp
не сработало

---

**2026-01-10T23:37:32 | Routerich**
https://podkop.net/docs/adguard/ по такому же принципу

---

**2026-01-11T02:47:12 | ufalex**
Доброго времени суток. Помогите пожалуйста советом и словом мудрым. Я устанавливаю игру, которая блочится. Забыл, как называется. Для сына ставил. На Android. Через PcApdroid глянул куда она запросы кидает. Этот момент выяснил. Теперь вопрос: куда в podkop это дело пихать? В VPN или в proxy? Возможно неправильно вопрос задаю, тогда подправьте меня, пожалуйста и подскажите.

---

**2026-01-11T04:24:16 | Routerich**
https://telegra.ph/Polnaya-instrukciya-nastrojki-xHTTP-v-Podkop-12-08

---

**2026-01-11T11:00:16 | Глеб**
Народ, подскажите, что в Podkop в URL конфигурации Proxy должно быть указано? А то вчера настройки на VPN менял и не сохранил.
Скрипт №5 по умолчанию с автоматической генерацией AWG WARP и установкой Podkop v0.7.10

---

**2026-01-11T12:29:01 | Роман**
Podkop со своим vless, если бесплатно - 5й скрипт из закрепа.

---

**2026-01-11T13:54:59 | Алексей**
Добрый день.Можно как то roblox пустить через zapret2.через podkop не хочет.

---

**2026-01-11T15:04:00 | Artur A.**
здравствуйте. при изменении в конфиг подкопа с url на outbound появляется такая ошибка: "Podkop Error
Sun Jan 11 15:00:03 2026 user.notice podkop: [fatal] Sing-box configuration /tmp/tmp.CPAobe is invalid. Aborted." при этом вроде бы все продолжает работать как надо.  прошивка последняя офиц. скрипт 5., все пакеты обновлены. Вопрос сосбвтенно надо ли тут что-то починить и как,если да.(установлен но не запущен запрет, подкоп сконфигурировался через опера прокси. разумеется, было нарушено правило чистой установки.

---

**2026-01-11T18:21:14 | Routerich**
Здравствуйте.
https://podkop.net/docs/sections/#polnostyu-marshrutiziruemye-ip-adresa-ip-for-full-redirection

---

**2026-01-11T19:21:22 | Routerich**
или просто
службы->Podkop->Диагностика->

---

**2026-01-11T19:27:44 | Andrei Ka**
Подскажите, а как с помощью Podkop заблокировать для доступа определенный домен? Нужно для запрета обновления ТВ

---

**2026-01-11T19:31:04 | Routerich**
Здравствуйте.
https://podkop.net/docs/sections/#block

---

**2026-01-11T19:53:31 | Amir**
Анализ запущен: 2026-01-11 19:51:50
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Configuring wget-ssl.

== ПРОВЕРКА DNS  (Прошивка: 24.10.4)
==============================================================
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.0.12

== ИНТЕРФЕЙС awg10 (ДЕТАЛИ)
==============================================================
  Статус                : UP (ON)  ↓0.18 MB / ↑0.55 MB
  Пинг (ya.ru via awg10): 58.520 / 94.784 ms (0 из 10 потеряно)

== ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM)
==============================================================
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/1.1 200 OK) [TLSv1.2]

== СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ)
==============================================================
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  youtubeUnblock  | STOPPED                        | ОТКЛ

== ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ
==============================================================
  podkop списки Youtube_Discord: youtube,discord
  podkop списки       main: geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10
==============================================================
== СИСТЕМНЫЕ РЕСУРСЫ
==============================================================
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.00 | RAM: 20% | NAND: 26% занято / 49.1M доступно
  13 9 * * * /usr/bin/podkop list_update
==============================================================

---

**2026-01-11T22:41:51 | Petr Korpal**
на старой версии podkop вроде работало с моей конфигурацией, сегодня сбрасывал роутер и накатил скрипт, но чет перестал работать

---

**2026-01-11T22:45:45 | Мудрикув Владимир**
Всем привет. 
Вчера пришел роутер. 

Вопрос. 

Текущие преднастройки роутера дают доступ к запрещенному интернету или нужно устанавливать podkop и платить за ключи vlees?

---

**2026-01-11T23:22:40 | Petr Korpal**
Анализ запущен: 2026-01-11 23:21:53
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

== ПРОВЕРКА DNS  (Прошивка: 24.10.4)
==============================================================
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  31.13.72.36

== ИНТЕРФЕЙС awg10 (ДЕТАЛИ)
==============================================================
  Статус                : UP (ON)  ↓0.00 MB / ↑0.10 MB
  Пинг (ya.ru via awg10): 39.073 / 44.132 ms (0 из 10 потеряно)

== ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM)
==============================================================
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОФЛАЙН
------------------------------------------------------
  Spider mode enabled. Check if remote file exists.
  --2026-01-11 23:22:07--  https://www.youtube.com/
  Resolving www.youtube.com... 64.233.162.91, 74.125.205.136, 64.233.164.91, ...
  Connecting to www.youtube.com|64.233.162.91|:443... connected.
  Unable to establish SSL connection.
------------------------------------------------------
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 64.233.161.93
    Name:       youtube.com
    Address: 64.233.161.190
    Name:       youtube.com
    Address: 64.233.161.91
    Name:       youtube.com
    Address: 64.233.161.136
--------------------------------------------------------------

== СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ)
==============================================================
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  youtubeUnblock  | STOPPED                        | ОТКЛ

== ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ
==============================================================
  podkop списки Youtube_Discord: youtube,discord
  podkop списки       main: geoblock,block,meta,twitter,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10
==============================================================
== СИСТЕМНЫЕ РЕСУРСЫ
==============================================================
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.06 | RAM: 20% | NAND: 26% занято / 49.5M доступно
  13 9 * * * /usr/bin/podkop list_update
==============================================================
root@RouteRich:~#

---

**2026-01-12T01:31:01 | ㅤㅤ**
Персональная ссылка в ЛК Adguard? После ее в Podkop вставить?

---

**2026-01-12T02:10:34 | Андрей**
вопрос решился изменением DNS в Podkop 👌
Логи Unity сказали, что не удается скачать файл шаблона по адресу https://download.packages.unity.com/com.unity.template.3d/-/com.unity.template.3d-9.1.0.tgz
в браузере файл тоже не скачивался.
После изменений в настройке DNS Podkop прошло минута-другая и все заработало...

---

**2026-01-12T08:05:20 | Routerich**
Можно в настройках Podkop тут выбрать интерфейс tailscale

---

**2026-01-12T09:42:33 | Routerich**
Здравствуйте.
можно.
Службы->Podkop->Настройки->Исключённые из маршрутизации IP-адреса->Добавляем IP устройства сюда

---

**2026-01-12T11:36:14 | Рузиль**
понял,попробую.У меня еще podkop установлен,его отключать тоже?

---

**2026-01-12T11:42:15 | Рузиль**
когда sh <(wget -qO- "https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/uttoobe/You_Tu_be!") ввел в терминал,надпись появилась,что без podkopa некоторые функции не работать будут,поэтому установил

---

**2026-01-12T12:21:47 | Routerich**
Здравствуйте.
https://podkop.net/docs/workvpn/

---

**2026-01-12T13:52:58 | Дмитрий Дмитриевич**
Через менеджер пакетов. Если это прямо подкоп.. Ищем установленный пакет podkop.

---

**2026-01-12T13:58:29 | Dark Ghost**
Там что-то с контрольными суммами прямо не то, сейчас знакомый тоже пытался:

Downloading https://downloads.openwrt.org/releases/24.10.4/targets/mediatek/filogic/kmods/6.6.110-1-6a9e125268c43e0bae8cecb014c8ab03/Packages.gz
Updated list of available packages in /var/opkg-lists/openwrt_kmods
Downloading https://downloads.openwrt.org/releases/24.10.4/targets/mediatek/filogic/kmods/6.6.110-1-6a9e125268c43e0bae8cecb014c8ab03/Packages.sig
Signature check passed.
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/luci/Packages.gz
Updated list of available packages in /var/opkg-lists/openwrt_luci
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/luci/Packages.sig
Signature check failed.
Remove wrong Signature file.

Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/coreutils_9.7-r1_aarch64_cortex-a53.ipk
Collected errors:
 * opkg_install_pkg: Checksum or size mismatch for package coreutils. Either the opkg or the package index are corrupt. Try 'opkg update'.
 * opkg_install_cmd: Cannot install package podkop.
Installing luci-app-podkop-v0.7.10-r1-all.ipk...
Installing luci-app-podkop (v0.7.10-r1) to root...
Installing coreutils (9.7-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/coreutils_9.7-r1_aarch64_cortex-a53.ipk
Collected errors:
 * opkg_install_pkg: Checksum or size mismatch for package coreutils. Either the opkg or the package index are corrupt. Try 'opkg update'.
 * opkg_install_cmd: Cannot install package luci-app-podkop.
Русский язык интерфейса ставим? y/n (Install the Russian interface language?)
y
No packages removed.
Installing luci-i18n-podkop-ru (0.251203.31812) to root...
Installing coreutils (9.7-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/coreutils_9.7-r1_aarch64_cortex-a53.ipk
Collected errors:
 * opkg_install_pkg: Checksum or size mismatch for package coreutils. Either the opkg or the package index are corrupt. Try 'opkg update'.
 * opkg_install_cmd: Cannot install package luci-i18n-podkop-ru.

---

**2026-01-12T14:16:13 | Anna Bagler**
Система - Автозапуск, найти opera-proxy, перезапустить, podkop перезапустить.

---

**2026-01-12T16:35:40 | Aleksandr**
Установил обратно Podkop, но Tailscale так и не заводится.

---

**2026-01-12T16:45:10 | Anna Bagler**
Службы - Podkop. Ceкции. Main, Списки сообщества и выбираем нужный. Применить. Тут же вверху Диагностика, Запустить диагностику.

---

**2026-01-12T17:49:57 | Aleksandr**
Походу надо будет. Перезагрузил роутер, Podkop рухнул сразу.

---

**2026-01-12T20:15:11 | Владимир**
Не долго...Podkop сломался😔 Один запрет2 работает.

---

**2026-01-12T20:54:22 | Routerich**
Для тг список в Podkop выбрать

---

**2026-01-12T21:03:49 | 𝐼𝓁𝓀𝒾𝓃**
я взял накатил чистый podkop

---

**2026-01-13T03:08:13 | Routerich**
Podkop последний поддерживает, Zeroblock поддерживает

---

**2026-01-13T04:52:39 | Bad Cat**
Podkop Error
Tue Jan 13 04:49:21 2026 user.notice podkop: [error] Download meta list failed

---

**2026-01-13T04:57:00 | Bad Cat**
Podkop
v0.7.9

---

**2026-01-13T07:16:06 | Баир**
Podkop

---

**2026-01-13T09:48:31 | Pavel**
Здравствуйте, подскажите как вернуть PODKOP? пакет установлен а в службах его нет, роутер перегружал не помогло

---

**2026-01-13T09:50:07 | Routerich**
luci-app-podkop?

---

**2026-01-13T09:55:55 | Mikhail Tikhomirov**
Установите luci-app-podkop появится

---

**2026-01-13T10:56:49 | Anna Bagler**
У вас yt через запрет. Запрет остановить и отключить. Podkop, Cекции, main, в списках сообщества выбрать cписок yt. Можно попробовать стратегии для запрет1 или запрет2.

---

**2026-01-13T12:50:43 | Роман**
Podkop сам рулит днс, пусть это делает. 
Ставьте подкоп скриптом от itdog и настраивайте как вам нужно. 
Про то что упадет подкоп и не будет интернета, потому что он утянул за собой днс, это уже другая история. Которая у меня ещё ни разу не случалась 😁

---

**2026-01-13T13:21:43 | GGS**
Как в podkop исключить endpoint warp. В какой настройке?

---

**2026-01-13T20:21:13 | Routerich**
Здравствуйте.
А если Podkop остановить, то скорость нормальная становится?

---

**2026-01-13T20:27:57 | Anna Bagler**
Система - Автозапуск или Службы - Podkop - Диагностика, чуть прокрутить вниз и будет кнопочка.

---

**2026-01-14T05:31:28 | Routerich**
podkop.net изучайте. Сможете установить и пользоваться точечной маршрутизацией

---

**2026-01-14T09:16:02 | Sir**
Как поставили!?
И как интегрировали в Podkop?

---

**2026-01-14T11:52:30 | Anna Bagler**
https://t.me/routerich/227096/425955 - для запрета 1, список yt из подкопа убрать. Или запрет1 так и оставить отключенным, поставить запрет2 вместо него. https://podkop.net/docs/sections/ - тут можете изучить информацию и использовать свой vless.

---

**2026-01-14T12:40:40 | Routerich**
Здравствуйте.
В исключения домены не добавить в Podkop

---

**2026-01-14T12:40:59 | Routerich**
А если остановить Podkop доступ появляется?

---

**2026-01-14T19:03:44 | Routerich**
А если остановить Podkop, когда проблема начинается, как будет?

---

**2026-01-14T21:34:06 | Anna Bagler**
Службы - Podkop - Настройка.

---

**2026-01-14T22:38:14 | Routerich**
Здравствуйте.
А если Podkop остановить? Открывается?

---

**2026-01-15T08:22:02 | Routerich**
Здравствуйте.
скорее всего с тем, что у вас в Podkop в секции main он

---

**2026-01-15T09:07:03 | Routerich**
Службы->Podkop->из секции main удалите список Russian Inside

---

**2026-01-15T10:14:14 | Routerich**
не включать, у вас ютуб в Podkop, в секции Youtube_Discord

---

**2026-01-15T13:08:03 | Aleks Buryi**
Здравствуйте!
Подскажите, где найти гайд по настройке на Routerich ax3000:
- podkop 
-wi-fi камер на ONVIF

---

**2026-01-15T14:40:50 | Routerich**
Здравствуйте.
пустите через Podkop Youtube через WARP

---

**2026-01-15T14:44:46 | Anna Bagler**
Вам скрипт 5 ставить, а потом уже смотреть через секции podkop.

---

**2026-01-15T15:40:13 | Александр**
Podkop вроде не поддерживает xhttp

---

**2026-01-15T18:34:05 | Routerich**
Здравствуйте.
Службы->Podkop->добавить список Viber в список Discord если он есть

---

**2026-01-15T19:02:58 | Дмитрий Воробьев**
Анализ запущен: 2026-01-15 19:01:52
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Configuring wget-ssl.

== ПРОВЕРКА DNS  (Прошивка: 24.10.4)
==============================================================
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.0.12

== ИНТЕРФЕЙС awg10 (ДЕТАЛИ)
==============================================================
  Статус                : UP (ON)  ↓0.00 MB / ↑0.28 MB
  Пинг (ya.ru via awg10): 58.758 / 86.814 ms (0 из 10 потеряно)

== ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM)
==============================================================
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/1.1 200 OK) [TLSv1.3]

== СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ)
==============================================================
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

== ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ
==============================================================
  podkop списки    Discord: discord
  podkop списки       main: geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10
==============================================================
== СИСТЕМНЫЕ РЕСУРСЫ
==============================================================
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.27 | RAM: 21% | NAND: 26% занято / 49.3M доступно
  13 9 * * * /usr/bin/podkop list_update
==============================================================
root@RouteRich:~#

---

**2026-01-15T22:46:18 | Мудрикув Владимир**
Всем привет. Наверняка здесь есть ответ на вопрос "Как заставить работать WhatsApps на телефоне".

Стоит роутер с podkop и vlees ключом.

Выбраны google,meta и russian inside списки, но WhatsApp все равно через раз работает.

Киньте ссылку где описано решение этого вопроса. По поиску чата не нашёл ответ.

Спасибо.

---

**2026-01-15T23:15:18 | Andrew**
Podkop. Да самая большая боль это телевизор. Смотрю ютюбе с него

---

**2026-01-16T10:08:55 | Andrey Lazarev**
Глубокоуважаемая поддержка и члены сообщества, подскажите пожалуйста ответы на несколько вопросов:

1) Если есть желание опробовать zapret2, то нужно ли удалять с роутера пакеты, относящиеся к zapret, podkop и youtube_unblock.

2) В очередной раз "что-то пошло не так" и доступ к "ТыТрубе" пропал сегодня. Если хочется переустановить нужные пакеты (скрипт №5) - нужно ли предварительно удалять пакеты, как и в первом вопросе, zapret-podkop-uy_unblock?

3) Каков минимальный необходимый набор пакетов для деблокирования доступа к YT и популярным игровым сервисам? Достаточно ли будет поставить zapret2 если у меня народ не только YT и связанные с Мета сервисы использует, но и в игры играет (Battlefield, Elite Dangerous - последняя, как я понимаю, частично на облако Амазона опирается, но могу ошибаться)?

---

**2026-01-16T14:37:45 | Әмир**
Через настроенную 5-ым скриптом секцию Podkop не работает

---

**2026-01-16T16:47:40 | Алексей**
У кого-то получалось настроить заворачивание cursor в прокси через podkop?
Если попробовать прописать домен, он криво начинает dns записи подтягивать

---

**2026-01-16T17:30:53 | Данила Мастер**
Подскажите, домены в podkop указаны, но все равно не заходит на них

---

**2026-01-16T17:34:40 | Данила Мастер**
службы - podkop - основные настройки - пользовательские домены. Например nnmclub.to

---

**2026-01-16T17:50:00 | Sergey**
Прошу совета, сам не могу понять в чём проблема.

На роутере работает youtubeUnblock + podkop 7.10 — каких-то проблем не замечено.

Однако есть проблема с определением ДНС имени сервиса Google Аналитики

Подскажите в какую сторону копать и вести диагностику.

— Если отключить youtubeUnblock и podkop — проблема не решается.
— Если отключить автозагрузку youtubeUnblock и podkop, перегрузить роутер — проблема не решается

вывод в консоли такой:
# dig @127.0.0.1 analytics.google.com +short
0.0.0.0

# dig @127.0.0.1 google.com +short
142.250.74.110

---

**2026-01-16T18:37:00 | Sergey**
Благодарю, за ответ.

Там по дефолту — перенаправление на днс-прокси Failsafe, а дальше уже в sing-box или на резервные ДНС tls (stubby) сервера 

Моя проблема решена, наверное просто глюк.

В конфиге podkop заменил ДНС сервера с AdGuard на Cloudflare и всё сразу "поехало" как надо.

Странно, конечно, но вот так.

---

**2026-01-16T19:19:58 | Vladislav (NexHav)**
13 9 * * * /usr/bin/podkop list_update

---

**2026-01-16T19:45:08 | Anna Bagler**
https://podkop.net/docs/sections/ изучайте

---

**2026-01-16T20:05:33 | ‎ ‎ ‎ ‎ ‎stefan ‎ ‎**
ребятки, на podkop настроил ютуб, который роутит на vpn wg. на компе и телефоне работает. на телевизоре нет.
подскажите, куда смотреть?

---

**2026-01-16T20:14:52 | Vadim**
global_check 
 📡 Global check run!
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛠️ System info
🕳️ Podkop:        v0.7.10 (latest: 0.7.10)
🕳️ LuCI App:      v0.7.10
📦 Sing-box:      1.12.12
🛜 OpenWrt:       RouteRich 24.10.4 r28959-29397011cc RR-3.8.2
🛜 Device:        Routerich AX3000 v1
━━━━━━━━━━━━━━━━━━━━━━━━━━━
➡️ DNS status
✅ Bootstrap DNS: 8.8.8.8
✅ Main DNS: 8.8.8.8 [doh]
✅ DNS on router
⚠️ dont_touch_dhcp is enabled. 📄 DHCP config:
config dnsmasq
 option domainneeded '1'
 option boguspriv '1'
 option localise_queries '1'
 option rebind_protection '1'
 option rebind_localhost '1'
 option local '/lan/'
 option domain 'lan'
 option expandhosts '1'
 option nonegcache '1'
 option cachesize '0'
 option authoritative '1'
 option readethers '1'
 option leasefile '/tmp/dhcp.leases'
 option resolvfile '/tmp/resolv.conf.d/resolv.conf.auto'
 option nonwildcard '1'
 option localservice '1'
 option ednspacket_max '1232'
 option confdir '/tmp/dnsmasq.d'
 option noresolv '1'
 option strictorder '1'
 option filter_aaaa '1'
 list server '127.0.0.1#5359'

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 Sing-box status
✅ Sing-box installed
✅ Sing-box version is compatible (newer than 1.12.4)
✅ Sing-box service exist
✅ Sing-box autostart disabled
✅ Sing-box process running
✅ Sing-box listening ports
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧱 NFT rules status
✅ Table exist
✅ Rules mangle exist
✅ Rules mangle counters
✅ Rules mangle output exist
✅ Rules mangle output counters
✅ Rules proxy exist
✅ Rules proxy counters
✅ Additional marking rules found
━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 Podkop config

config settings 'settings'
 option dns_type 'doh'
 option dns_server '8.8.8.8'
 option bootstrap_dns_server '8.8.8.8'
 option dns_rewrite_ttl '60'
 option enable_output_network_interface '0'
 option enable_badwan_interface_monitoring '0'
 option enable_yacd '0'
 option disable_quic '1'
 option update_interval '1d'
 option download_lists_via_proxy '1'
 option dont_touch_dhcp '1'
 option config_path '/etc/sing-box/config.json'
 option cache_path '/tmp/sing-box/cache.db'
 option exclude_ntp '1'
 option shutdown_correctly '0'
 option download_lists_via_proxy_section 'main'
 list source_network_interfaces 'br-lan'

config section 'main'
 option connection_type 'proxy'
 option proxy_config_type 'outbound'
 option enable_udp_over_tcp '0'
 option shutdown_correctly '1'
 option user_domain_list_type 'text'
 option user_subnet_list_type 'disabled'
 option mixed_proxy_enabled '0'
 option outbound_json 'MASKED'
 option user_domains_text 'myip.com'
 list community_lists 'geoblock'
 list community_lists 'block'
 list community_lists 'meta'
 list community_lists 'twitter'
 list community_lists 'hdrezka'
 list community_lists 'tiktok'
 list community_lists 'google_ai'
 list community_lists 'porn'
 list community_lists 'youtube'

config section 'Youtube_Discord'
 option connection_type 'vpn'
 option interface 'awg10'
 option domain_resolver_enabled '0'
 option user_domain_list_type 'text'
 option user_subnet_list_type 'disabled'
 option mixed_proxy_enabled '0'
 list community_lists 'youtube'
 list community_lists 'discord'
 option user_domains_text '2ip.ru amazonaws.com whatsapp.com whatsapp.net whatsapp.biz wa.me seccfl-fota-dn.samsungdm.com
sdk.pushmessage.samsung.com
www.pathofexile.com web.poecdn.com
store.steampowered.com
steamcommunity.com
'
 list remote_subnet_lists 'https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_cidr_ipv4.txt'

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 WAN config
config interface 'wan'
 option proto 'pppoe'
 option device 'eth1'
        option username '******'
        option password '******'
 option pppd_options 'debug'
 option ipv6 'auto'

⚠️ WARP detected: engage.cloudflareclient.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ Zapret detected
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🥸 FakeIP status
✅ Router DNS is routed through sing-box
✅ Sing-box works with FakeIP: 198.18.0.28

---

**2026-01-16T22:11:40 | Тимур️**
Добрый вечер!  Все работало корректно, 5 скрипт. На текущий момент отсутствует доступ до заблокированных ресурсов. Версия прошивки 24.10.4 .  Прошелся по траблшутинге со страницы https://podkop.net/docs/troubleshooting/ .
Что еще проверить ? журнал приаттачил.

---

**2026-01-17T00:24:35 | Андрей ☕️**
На трех устройствах, у разных провайдеров, в двух столицах стоит: чистый openwrt на tp-link, RR usb2, RR usb3. Использую для YouTube, WhatsApp, Instagram  https-dns-proxy + youtubeUnblock. 
Всё стабильно работает. 
Без podkop, zarpet и танцев вокруг них.

---

**2026-01-17T02:17:44 | Олег Щепин**
Анализ запущен: 2026-01-17 02:15:58
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Configuring wget-ssl.

== ПРОВЕРКА DNS  (Прошивка: 24.10.4)
==============================================================
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.0.3

== ИНТЕРФЕЙС awg10 (ДЕТАЛИ)
==============================================================
  Статус                : UP (ON)  ↓0.32 MB / ↑40.37 MB
  Пинг (ya.ru via awg10): 6.248 / 7.384 ms (0 из 10 потеряно)

== ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM)
==============================================================
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/1.1 200 OK) [TLSv1.3]

== СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ)
==============================================================
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  youtubeUnblock  | STOPPED                        | ОТКЛ

== ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ
==============================================================
  podkop списки Youtube_Discord: discord
  podkop списки       main: geoblock,block,meta,twitter,hdrezka,tiktok,google_ai,youtube
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10
==============================================================
== СИСТЕМНЫЕ РЕСУРСЫ
==============================================================
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.09 | RAM: 23% | NAND: 26% занято / 49.1M доступно
  13 9 * * * /usr/bin/podkop list_update
==============================================================
root@RouteRich:~# ^C

root@RouteRich:~#

---

**2026-01-17T03:05:25 | ALeX**
Проверено неоднократно. Периодически падает dns ресолвинг на br-lan интерфейсе. по localhost ресолвит нормально.  При этом диагностика FakeIP в диагностике podkop показывает сбой. WatchDoc (кстати почему Doc а не Dog :) ) кажет "wdoc_singbox: FakeIP DNS: OK" и не переталкивает podkop. ручной перезапуск podkop или интерфейса br-lan решает на какое то время...

---

**2026-01-17T08:28:30 | Евгений**
и что делать? вообще удалить из podkop

---

**2026-01-17T12:46:50 | Anna Bagler**
Если есть строчки, что podkop установлен и запущен, то не надо.

---

**2026-01-17T13:43:53 | Max**
Добрый день! Помогите, пжста, нубу. Работал скрипт 4 на старой прошивке, Пару дней назад перестал работать ютуб, инстаграм. Сегодня обновил прошивку, выполнил подготовку и скрипт 5 (при установке заметил что podkop не заработал).
На телефоне ютуб работает, а на ТВ и ПК нет... 
диагностика Podkop показывает - две ошибки
DHCP содержит DNS сервер 
Браузер не использует FakeIP 
в wiki написано так:

"Пункты «DHCP содержит DNS сервер», «Счётчики правил mangle» и  «Найдены дополнительные правила маркировки» некритичны и могут быть отмечены как ошибки, это безопасно, уверяю вас. А вот пункт «Браузер не использует FakeIP» важен, чтобы его исправить перейдите сюда."

а ссылки "сюда" нет )

---

**2026-01-17T13:59:11 | Anna Bagler**
Проверяйте, что мешает на ПК и ТВ по IP в подкоп. В планировщике оставьте только эту строчку по подкопу 13 9 * * * /usr/bin/podkop list_update

---

**2026-01-17T14:02:57 | slr**
Переустановил podkop, нет конфига где брать?

---

**2026-01-17T14:08:29 | slr**
Sat Jan 17 14:01:24 2026 user.notice podkop: [error] Outbound section not found. Please check your configuration file (missing proxy_string, interface, outbound_json, or urltest_proxy_links). Aborted.

---

**2026-01-17T15:16:23 | 幽灵**
По Roblox перелопатил все вкладки, Podkop домены и подсети, отдельные VPN запреты не решают проблемы блокировки. В Роблокс заходит, а в мини игры нет. Может кто нибудь решил эту проблему другим способом?

---

**2026-01-17T16:49:13 | Dmitry**
Вечер добрый. Установил скрипт 5, всё ок. Подшаманил с своими доменами в podkop. До этого стоял только ютубанблок. Я так понимаю что ютубанблок и установившийся со скриптом zapret, в принципе, можно удалить?

---

**2026-01-17T16:56:20 | Dmitry**
Podkop

---

**2026-01-17T17:15:27 | Routerich**
Здравствуйте.
А если стопнуть Podkop, Zapret так же все?

---

**2026-01-17T19:23:54 | Routerich**
Здравствуйте
Можно в Podkop добавить ip устройства в исключения, но отдельно домены там нельзя

---

**2026-01-17T19:30:02 | Routerich**
Полностью для устройства исключение можете сделать и то только в Podkop.
А так эти инструменты работают точечно, если никуда их не вписать то и не будут они ломаться

---

**2026-01-17T19:40:51 | Routerich**
В Podkop помимо секции main, может быть секция с именем Discord

---

**2026-01-17T21:57:30 | ㅤㅤ**
Есть мануалы по поводу работы секции Main и YouTube в Podkop? Интересная ситуация сейчас с WhatsApp - с роутера не работает, а с мобильного интернета открывает. Недавно были проблемы с медиаконтентом в CapCut, не открывался форум Ruboard.

Качественно подружить роутер с Adguard внутри Podkop так и не получилось. Экспериментировал со списками блокировки в adguard-dns через DoH, пользовательскими списками - реклама появляется.
Фактически нужно ставить полноценный Adguard на роутер и учить их между собой взаимодействовать. Блокировка реклама - штука невероятно полезная.

---

**2026-01-17T22:16:36 | Routerich**
https://podkop.net/

---

**2026-01-18T00:42:51 | Routerich**
https://podkop.net/docs/tunnels/awg_settings/ пункт с установкой пакетов пропускайте

---

**2026-01-18T13:34:01 | Anna Bagler**
Сеть - Интерфейсы, awg10, перезапустить. Если не помогло, можно скрипт 5 повторно прогнать. Если не помогло, Podkop, Cекции, в discord крестиком список убрать, в main добавить, применить. Если не помогло, запрет2 ставить.

---

**2026-01-18T14:40:37 | ALeX**
Sun Jan 18 14:03:03 2026 daemon.info wdoc_singbox: FakeIP DNS: OK
Sun Jan 18 14:03:03 2026 daemon.info wdoc_singbox: Sing-box: OK
Sun Jan 18 14:03:11 2026 daemon.err tailscaled[11232]: 2026/01/18 11:03:11 netcheck: netcheck.runProbe: named node "1002a" has no v6 address
Sun Jan 18 14:03:11 2026 daemon.err tailscaled[11232]: 2026/01/18 11:03:11 netcheck: netcheck.runProbe: named node "1001a" has no v6 address
Sun Jan 18 14:03:18 2026 daemon.err uhttpd[4509]: [info] luci: accepted login on /admin/services/podkop for root from 192.168.21.19

---

**2026-01-18T14:42:34 | ALeX**
https://t.me/routerich/4/444512 собственно вопрос можно решить заставив WatchDoc работать корректно.  Можно ли что то с ним сделать чтобы смотрел не локальный интерфейс, а как в диагностике podkopa?

---

**2026-01-18T16:36:06 | Routerich**
Здравствуйте.
Службы->Podkop->крутим вниз, там будет секция Discord, и там в предустановленные списки добавить список YouTube

---

**2026-01-18T16:57:20 | Владимир Рагулин**
Почитал ветку с похожими проблемами и не увидел конечное решение
Новый вопрос: как обойти эту ошибку при подключении подкопа? Рекомендации выполнил, установил по инструкции, но при заходе ловлю это
Podkop Error
Sun Jan 18 16:49:22 2026 user.notice podkop: [error] Outbound section not found. Please check your configuration file (missing proxy_string, interface, outbound_json, or urltest_proxy_links). Aborted.

---

**2026-01-18T17:13:34 | Борис**
А Zapret2 и podkop будут включать в реестр отечественного ПО?

---

**2026-01-18T18:16:56 | Kirill Y**
Подскажите. Хотел заново всё настроить.Сделал сброс на заводские настройки. После перезагрузки  в службах есть и podkop и zapret. Это нормально?

---

**2026-01-18T18:22:53 | Тимур**
Запарился от dhcp и прописывать вручную адреса хочу поставить podkop но версия openwrt не позволяет, теперь ищу прошивку для openwrt чтоб обновить до последней стабильной версии

---

**2026-01-18T18:57:14 | Михаил Краев**
Здравствуйте. Несколько дней назад пропал голосовой чат в Arc Raiders. Я не слышу - меня не слышат. 
Стоят:
Podkop 0.7.10 (в диагностике все ок)
Zapret 72.20251122
Версия прошивки 24.10.4
В целом обходы работают.
Нашел вот это, но не знаю, как ставить на роутер и стоит ли вообще: https://github.com/Flowseal/zapret-discord-youtube/discussions/8129

---

**2026-01-18T19:33:19 | Виктор**
Спасибо, все работает, но в Подкопе сообщение "Podkop Error
Sun Jan 18 19:18:09 2026 user.notice podkop: [error] Download meta list failed" нужно ли принимать какие то меры?

---

**2026-01-18T19:33:58 | Routerich**
Здравствуйте.
В настройках Podkop уберите галочку/поставьте на скачивать списки через Proxy

---

**2026-01-18T19:37:56 | Stanislav Muradov**
Где найти Podkop

---

**2026-01-18T19:39:00 | Routerich**
Службы->Podkop

---

**2026-01-18T20:15:46 | Routerich**
Здравствуйте.
Сперва это https://t.me/routerich/3845/245550
Потом по чату пройтись и добавить домены /подсети в Podkop

---

**2026-01-18T23:30:13 | Anna Bagler**
Изучайте https://podkop.net/docs/sections/ 
Списки доменов и списки подсетей.

---

**2026-01-19T09:47:15 | Routerich**
пробуйте стопнуть Podkop и смотреть как будет.
вообще возможно провайдер блокирует доступ к домену.

---

**2026-01-19T13:44:48 | Routerich**
Службы->Podkop->Секция Discord->Полностью маршрутизированные IP-адреса->Добавляем IP устройства

---

**2026-01-19T14:03:27 | Koki**
Я в таких случаях делаю так:
- Включаю Yacd
- Открываю веб-панель yacd - Соединения
- Пускаю весь трафик с устройства на котором у меня блокируются приложения в podkop
- Открываю заблокированное приложение и в веб-панели yacd смотрю на какие адреса оно ходит
- Прописываю адреса в Пользовательских списках доменов
- Отключаю перенаправление всего трафика с устройства в Podkop и проверяю работу приложения

---

**2026-01-19T14:07:21 | ㅤㅤ**
Уточните пожалуйста в какую именно пользовательскую секцию Podkop? Ранее экспериментировал безуспешно.

---

**2026-01-19T15:37:22 | Олег Михайлович**
вот такая ошибка появилась Podkop Error
Mon Jan 19 15:32:19 2026 user.notice podkop: [error] Detected https-dns-proxy in DHCP config. Edit /etc/config/dhcp

---

**2026-01-19T17:09:22 | Алексей Лютенко**
В планировщике только 
13 9***/usr/bin/podkop list update

---

**2026-01-19T17:50:02 | Routerich**
По логам проблемы с dnsmasq и doh-proxy + podkop, плюс у вас отвал lan1 порта происходил. Первым делом проверьте кабель в lan1 и блок питания. Далее желательно сделать сброс на заводские и понаблюдать без подкопа, просто работу роутера. Только сделать как я вам присылал выше с логами. Если отвалов не будет то далее ставить подкоп и сделать еще так https://t.me/routerich/3845/293423 и далее наблюдать

---

**2026-01-19T18:18:55 | Михаил Полиенко - Инвестиции в бизнес**
У меня на мобильном Google Chrome выдается подборка интересных страниц.
Когда подключаюсь к RouteRich - ее невозможно обновить, он долго думает, в итоге выдает, что доступа нет. Приходится переключаться на мобильный.
Прошивка 24.10.4
Работает Podkop настроен по скрипту №5. Zapret и youtubeunblock отключены.

---

**2026-01-19T20:16:22 | Anna Bagler**
Перезапустите opera-proxy и podkop. Посмотрите.

---

**2026-01-19T23:08:59 | Ivan Sinik**
как нужно настроить podkop?
включеный. почти в ноль режет скорость с форума 4pda. невозможно скачать файлы

---

**2026-01-20T02:11:42 | Тимур**
Анализ запущен: 2026-01-20 02:10:53
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Configuring wget-ssl.

== ПРОВЕРКА DNS  (Прошивка: 24.10.4)
==============================================================
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.0.174

== ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM)
==============================================================
  OPERA (Proxy): ОФЛАЙН
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 198.18.0.127
--------------------------------------------------------------

== СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ)
==============================================================
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  youtubeUnblock  | RUNNING                        | РАЗРЕШЁН

== ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ
==============================================================
  !!! КРИТ: Пересечение между podkop и youtubeUnblock:
    podkop                    : main
    youtubeUnblock            : YouTube
    Домены: googlevideo.com youtube.com 

  podkop списки       main: !_russia_inside
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 77.88.8.8
  Версия podkop: v0.7.10
==============================================================
== СИСТЕМНЫЕ РЕСУРСЫ
==============================================================
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.62 | RAM: 45% | NAND: 30% занято / 46.4M доступно
  13 9 * * * /usr/bin/podkop list_update
==============================================================
root@RouteRich:~# ^C

---

**2026-01-20T10:24:47 | Игорь Котыс**
Доброго дня! Опять вопрос по 5-му скрипту. На новом роутере  (нет ничего, кроме WG клиента) ставил его. Вроде проверял - YT рабтает. Сейчас друг жалуется - не работает. По предыдущему роутеру помню, что группы youtube должна быть в секции DISCORD подкопа, захожу - его там нет. Решил проверить на роутере, на котором порядка месяца тому запускал "пятый скрипт" - там группа youtube в секции main и при этом я не переносил её сам. 
Вопрос - по какому алгоритму скрипт располагает группу youtube? И если как в моём крайнем случае её нет в Podkop ни в одной из секций, то куда ещё её скрипт мог определить?

---

**2026-01-20T10:27:22 | Routerich**
Здравствуйте.
если в Podkop нет, то он идёт через Zapret.

---

**2026-01-20T10:58:17 | ㅤㅤ**
Похвастался Routerich перед своим товарищем - архитектором в финансовой сфере. 
Задача была подружить Adguard и Podkop, чтобы действительно блокировало рекламу https://podkop.net/docs/adguard/

Но моя идея была раскритикована. Товарищ для себя бы выстроил чистую OpenWRT в виртуальной машине с нужным набором софта (podkop/antizapret - возможно вместе как один из вариантов секции + AdGuard Home в docker + dnsmasq через который идет dhcp/dns в локалку), а после как оно заработает в виртуалке - написать конфиг для сборки и перенести на роутер. 

Выходит, что конфигурация (Routerich + Podkop + AGH) - это костыль поверх OpenWRT и в случае, если что-то в цепи сломается - устанешь искать причины. 

Касаемо секций я и разобрался и нет. Main - это opera-proxy: Youtube-Discord - AmneziaWG
Насколько понял на данный момент оно работает так:

Routerich
       ↓
Dnsmasq роутера (192.168.1.1:53)
       ↓
Sing-box (Podkop) -> FakeIP (198.18.x.x)
       ↓
       ├── Домен НЕ в списках -> Прямой выход в интернет
       │
       ├── Домен в `main` (geoblock, meta и др.) -> opera-proxy (сервер Opera)
       │
       └── Домен в `youtube_discord` -> VPN-туннель (awg0)
Какие преимущества дают сервера Opera и что позволяет в отличии от них AmneziaWG я пока не разбирал. Что если убрать opera-proxy из уравнения и пустить через собственный, контролируемый VPN-туннель, настроенный в Podkop. Тоже самое сделать с Amnezia поменяв VPN на мои VPS-сервера.
Две разные секции меня откровенно напрягают. Предполагаю, что подобное деление служит методом обхода двух разных задач: 1. Когда оно заблокировано у нас. 2. Когда оно заблокировано у них.

Насколько знаю, Routerich трансформировался и методы работы с траффиком менялись от прошивки к прошивке. Ранее в коробке был установлен и ADH? Имеются разные скрипты. Быть может подобные идеи уже воплощались в прошлом. Что стало причиной прихода к данной конфигурации? Предполагаю, что задача стояла в предоставлении конечного пользователю готового бесплатного решения.

---

**2026-01-20T11:41:49 | Владимир Волков**
Для простоты закиньте этот запрос в любую доступную ИИ (гемини, грок, дипсик, чатжпт):
Я настраиваю tailscale на openwrt роутере. Сеть настроена, устройства добавлены, подключения работают. Также включил exit node, в средстве точечной маршрутизации (podkop) интерфейсом-источником выбрал tailscale0.
Проблема: при выборе exit node на телефоне и пк в клиенте tailscale отключается интернет (или нет резолвинга днс), сайты не открываются (ни обычные, ни те, которые должны идти через точечную маршрутизацию).
Напиши подробную пошаговую инструкцию с ping, tracert, nslookup и прочими утилитами на windows.
Предлагаю сделать проверку пинга и трейсов до айпи адресов (1.1.1.1 cloudflare, 8.8.8.8 google, 77.88.8.8 yandex) и затем при наличии пинга проверить резолвинг днс через ping хостнеймов (one.one.one.one, google.com, ya.ru аналогично айпи адресам).
Инструкция должна содержать не только шаги для проверки, но и ожидаемый результат, чтобы любой непродвинутый пользователь мог выполнить такую диагностику. По выполнению команд я пришлю полный вывод в чат - проанализируй его и дай несколько понятных решений проблем, которые не сломают существующие маршруты, не сломают сетевые подключения и настройки адаптеров.
Если для выдачи рекомендаций тебе не хватает какой-либо информации, не додумывай её самостоятельно, запроси её у меня, я предоставлю необходимое. Не придумывай несуществующие команды для windows, мы настраиваем именно эту операционную систему и можем оперировать только командами из комплекта поставки cmd и powershell.

---

**2026-01-20T12:25:43 | Сергей**
podkop zapret

---

**2026-01-20T12:30:35 | Routerich**
а если Podkop еще стопнуть?

---

**2026-01-20T12:32:50 | Routerich**
понял, значит дело в Podkop.

---

**2026-01-20T12:39:34 | Сергей**
Анализ запущен: 2026-01-20 12:38:23
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.0.5

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓0.00 MB / ↑1.87 MB
  Пинг (ya.ru via awg10): ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (77.88.55.242): 56 data bytes

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОФЛАЙН
------------------------------------------------------
  Spider mode enabled. Check if remote file exists.
  --2026-01-20 12:39:00--  https://www.youtube.com/
  Resolving www.youtube.com... 142.250.102.198
  Connecting to www.youtube.com|142.250.102.198|:443... connected.
  Unable to establish SSL connection.
------------------------------------------------------
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 64.233.164.93
    Name:       youtube.com
    Address: 64.233.164.190
    Name:       youtube.com
    Address: 64.233.164.136
    Name:       youtube.com
    Address: 64.233.164.91
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop списки    Discord: discord
  podkop списки       main: geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: dns.adguard-dns.com / 8.8.8.8
  Версия podkop: v0.7.7

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.30 | RAM: 21% | NAND: 26% занято / 49.1M доступно
  0 4 * * * service zapret restart
  13 9 * * * /usr/bin/podkop list_update

root@RouteRich:~# ^C

root@RouteRich:~#

---

**2026-01-20T12:50:47 | Routerich**
попробуйте в настройках Podkop сменить DNS на Google и проверить

---

**2026-01-20T12:54:25 | ㅤㅤ**
Благодарю за ответ! Уже ознакомился с вашей перепиской в "Предложениях по улучшению". не ясно почему вас отправили в оффтоп. Не удивительно, что с таким подходом команды к вопросам клиентов все работает так как работает. Получить грамотную поддержку здесь можно только по самому роутеру. что в целом правильно.

Реализовал ваш совет, экспериментировал с разными списками, но по факту он также толком не блокирует рекламу на сайтах и блокировать не может. По факту это тот же самый подход с AdGuard DNS Upstream. Тот же Яндекс реализовал показ рекламы внутри своего домена /* динамическими ссылками и DNS тут уже не причем, а списки не помогут. Расширения в помощь.

Изначально была задача просто поставить ADH на OpenWRT и направит траффик после Podkop. Наверное, только так оно будет работать как мне надо.

Касаемо второго абзаца о секциях вопрос был риторическим.

---

**2026-01-20T13:43:17 | Sergey Godovich**
Всем привет - сегодня появилось в подкопе Podkop Error
Tue Jan 20 12:37:59 2026 user.notice podkop: [error] Download digitalocean list failed
Podkop Error
Tue Jan 20 12:37:53 2026 user.notice podkop: [error] Download ovh list failed
Podkop Error
Tue Jan 20 12:37:47 2026 user.notice podkop: [error] Download hetzner list failed
Podkop Error
Tue Jan 20 12:37:40 2026 user.notice podkop: [error] Download cloudflare list failed.  Начинать паниковать?

---

**2026-01-20T15:16:49 | ㅤㅤ**
Ну вот вы хоть что-то показываете. А то тут один ass нуб какую х несет и ничего толком не предлагает.

Вот мой результат c настройками роутера на DOH adguard.dns и секцией Adblock в Podkop. У вас судя по всему на устройстве установлен Adguard - он у меня тоже есть с купленной вечной лицензией. Сейчас еще одну штуку попробую - если не работает, то брошу это дело.

---

**2026-01-20T18:01:13 | Routerich**
Здравствуйте.
Да, список Cloudflare не добавляйте, сломалете.
Можно просто пустить полностью устройство в секцию Discord Podkop, получится так же как если бы вы на устройстве включали WARP

---

**2026-01-20T18:16:47 | Антон Баев**
Podkop: v0.6.2

---

**2026-01-20T18:32:22 | Антон Баев**
Podkop: v0.6.2
LuCI App: v0.6.2
Sing-box: 1.12.4
OpenWrt Version: RouteRich 24.10.2 r28739-d9340319c6 RR-3.6.6

---

**2026-01-20T21:47:58 | Vasa**
https://github.com/itdoginfo/podkop

---

**2026-01-21T00:30:24 | Pavel**
а еще podkop стал вот так вот отображаться

---

**2026-01-21T01:36:30 | X**
Да зря взяли за основу podkop, лучше бы v2raya доработали. Там xray-core.

---

**2026-01-21T07:44:03 | Yury Kuzmenko**
https://podkop.net/docs/install/

---

**2026-01-21T09:30:11 | Routerich**
или отключайте и стопайте запрет и добавляйте в Podkop, в секцию Discord список youtube

---

**2026-01-21T13:01:34 | ㅤㅤ**
Сегодня утром после тщательной подготовки и изучения материала удалось подружить Podkop и Adguard с первого раза. После многочисленных тестов вижу, что все работает быстро и стабильно, Доступы к заблокированным сервисам сохранились. 

Немного справки для тех, кто хочет пройти мой путь:

AdGuard Home на роутере - это DNS-блокировщик! Он видит только адрес дома, но не видит содержимое сайта (конкретный путь к картинке баннера).
Допустим, сайты работающие с РСЯ часто используют CNAME-подмену или загружают рекламу с тех же поддоменов, что и основной контент. Такую рекламу можно заблокировать с помощью расширений и приложений на самом клиенте - решения от того же Adguard или uBlock как советовал местный модератор. 

Вместе с тем AGH на роутере экономит трафик, дает определенную защиту домашним устройствам и блокирует ~90% мусора. Ну и родительский контроль реализован неплохо.

---

**2026-01-21T13:02:57 | Kirill K**
Здравствуйте! Подскажите, пожалуйста, где предпочтительнее удалить запись об Youtube, чтобы не было конфликтов, в Podkop или Zapret? Пробовал в Podkop удалять запись и перезагружать роутер, доступ к Ютуб пропадал. Может мало ждал по времени пока сервисы поднимуться.  Так же в в домашней сети стали появляться частые отвалы доступа к Интернету.

---

**2026-01-21T13:12:12 | Фотограф Александр Москаленко**
Анализ запущен: 2026-01-21 13:10:58
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.1/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.1):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  57.144.244.1

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓0.00 MB / ↑2.67 MB
  Пинг (ya.ru via awg10): ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (5.255.255.242): 56 data bytes

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОФЛАЙН
------------------------------------------------------
  Spider mode enabled. Check if remote file exists.
  --2026-01-21 13:11:45--  https://www.youtube.com/
  Resolving www.youtube.com... 108.177.14.198
  Connecting to www.youtube.com|108.177.14.198|:443... connected.
  Unable to establish SSL connection.
------------------------------------------------------
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 172.253.130.91
    Name:       youtube.com
    Address: 172.253.130.136
    Name:       youtube.com
    Address: 172.253.130.190
    Name:       youtube.com
    Address: 172.253.130.93
    Name:       youtube.com
    Address: 2a00:1450:4010:c20::be
    Name:       youtube.com
    Address: 2a00:1450:4010:c20::88
    Name:       youtube.com
    Address: 2a00:1450:4010:c20::5b
    Name:       youtube.com
    Address: 2a00:1450:4010:c20::5d
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | STOPPED                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | РАЗРЕШЁН
  youtubeUnblock  | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!! КРИТ: Пересечение между podkop и youtubeUnblock:
    podkop                    : main
    youtubeUnblock            : Discord
    Домены: discord.com discord.gg discord.media discordapp.com discordapp.net ggpht.com googleapis.com googleusercontent.com googlevideo.com gstatic.com l.google.com play.google.com youtu.be youtube.com ytimg.com 

  Версия podkop: 0.2.5-1

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.1)
  CPU: 0.40 | RAM: 22% | NAND: 23% занято / 56.2M доступно
  0 4 * * * /etc/init.d/podkop list_update

---

**2026-01-21T13:40:11 | Routerich**
Здравствуйте.
Установить 5 скрипт и добавить телеграмм список в Podkop в секцию Discord если она есть или в секцию main

---

**2026-01-21T14:36:44 | Ilia Fertikov**
Какие доп домены нужно добавить в пользовательский список podkop, чтобы заработал whatsapp из маркета?

---

**2026-01-21T14:39:30 | Aleks Buryi**
Добрый день!
Не могу подключить телефон через Tailscale, чтобы трафик шел через роутер и, соотв., настроенный podkop.
Все установил и настроил по мануалу. На телефоне тоже. Exit Node везде включен, везде статус Running и Connected...
Но на телефоне (в мобильной сети конечно) ip не подменяется, в общем не работает. Хотя пингуется по ip Tailscale'а.
В общем, второй день перепроверяю маскирование, настроил НАТ - не работает(
Подскажите, где искать!

---

**2026-01-21T15:10:36 | Ter**
===== Model =====
Routerich AX3000 v1

===== OpenWrt =====
DISTRIB_ID='RouteRich'
DISTRIB_RELEASE='24.10.4'
DISTRIB_REVISION='r28959-29397011cc'
DISTRIB_TARGET='mediatek/filogic'
DISTRIB_ARCH='aarch64_cortex-a53'
DISTRIB_DESCRIPTION='RouteRich 24.10.4 r28959-29397011cc ASU'
DISTRIB_TAINTS=''

===== User Packages =====
luci-i18n-podkop-ru
luci-i18n-wdoc-wg-ru
luci-app-podkop
luci-app-zapret
luci-i18n-wdoc-warp-ru
luci-i18n-wdoc-singbox-ru
podkop
zapret-tpws
zapret
zapret-mdig
sing-box-tiny
zapret-ip2net

===== Flow Offloading =====
SW: on | HW: on

---

**2026-01-21T15:18:10 | Koki**
Судя по всему AGH + Podkop сложно реализуется только если они будут на одном устройстве, у меня AGH стоит на однолетнике Orange Pi Zero 3 и если не считать самой настройки AGH и однолетника вся настройка заключалась в прописывании его ip адреса в качестве DNS в подкопе.

---

**2026-01-21T16:07:26 | Kirill K**
Чтобы Вы посоветовали?                       1. Удалил  запись Youtube (в секции Youtube_Discord) в Podkop и перезагрузил роутер: уровень сигнала Wi-Fi очень слабый, 
youtube на телевизорах работает с большими зависаниями, на телефоне youtube в бесконечной загрузке, на компьютере даже через Tail работает, сбои в работе телеграмм.
2. Вернул запись Youtube (в секции Youtube_Discord) в Podkop, остановил Zapret и выключил его из автозагрузки: Youtube на телевизоре и телефоне работает с частыми подвисаниями по 3 - 5 минут, телеграмм тоже часто отваливается.
Оба варианта тестировал минут через 10 после перезагрузки роутера, минут по 15 каждый.
Zapret сбрасывал на дефолтные настройки перед тестированием.
Обратил внимание, что в последнее время уровень сигнала Wi-Fi сети сильно снизился, точнее стал нестабильным: то слабый сигнал, то сильный сигнал.

---

**2026-01-21T16:13:40 | Kirill K**
Еще бы доступ к vnc.tryhackme.tech восстановить. Прописывал вчера в Podkop в секцию VPN и все работало даже через Tail, сегодня не работает)

---

**2026-01-21T18:06:01 | Routerich**
Почитайте про podkop, смысл тот же + функции которых нет в подкопе сейчас

---

**2026-01-21T18:34:41 | Mikhail Velichko**
Коллеги, подскажите есть вариант подружить podkop с bgp (например antifilter)?

---

**2026-01-21T18:39:55 | Jackie Cupcake**
Добрый вечер подскажите пожалуйста как в podkop сделать в отдельной секции чтобы в ней задать следующее , отдельное устройство чтобы туда полностью шел интернет через впн?

---

**2026-01-21T20:18:07 | SnoweTiger**
не подскажите как-нибудь можно заставить новый podkop 0.7 работать с youtubeunblock? либо какую-нибудь альтернативу для подкопа которая будет рулит трафик на singbox? был не приятно удивлен что на обновленный роутер не ставится старый подкоп 0.2.5

---

**2026-01-21T20:21:15 | Routerich**
Бета версия скрипта для обхода ограничений.

Основное отличие от скрипта №5, что тут  используется последняя версия Podkop (v0.7.14).

Из ключевых отличий этой версии то, что там баг с WARP и CloudFlare починили, добавили исключения и список Roblox можно сразу выбрать.

Важно: 
1. Перед запуском сделайте бэкап (Система->Восстановление и обновление->Создать архив)
2. Если у вас всё работает хорошо, в частности youtube не надо его запускать.
3. Если не готовы сбрасывать роутер после неудачной отработки скрипта, лучше не запускайте скрипт.

Если вы всё таки решились запустить его, то от вас мне нужны полные логи запуска скрипта от начала его работы до завершения. Файл с логами будет по пути /root/run.log, можете его скачать через 
Веб морда роутера->NAS->Файловый менеджер->/root/run.log, скачать 
Потом пришлите его, для анализа.

P.S. запустится только на прошивках версии не ниже 24.10.2

Сам код для запуска ниже.
sh <(wget -q -O - https://raw.githubusercontent.com/routerich/RouterichAX3000_configs/refs/heads/podkop0711/universal_config_new_podkop.sh) 2>&1 | tee /root/run.log

---

**2026-01-21T21:05:52 | Routerich**
Либо как Анна написала либо https://podkop.net/docs/install/ через офф скрипт обновления и encfyjdrb

---

**2026-01-21T21:19:52 | Антон**
@routerich Доброй ночи! Можно будет добавить список Roblox как в Podkope 0.7.11

---

**2026-01-21T22:57:55 | Mikhail Velichko**
В общем-то посмотрел я тему подкопа и bgp - у них там все свелось к "тебе надо - возьми и допили" (по крайней мере тот, что удалось найти). Поэтому все же попытаюсь спросить еще раз - есть ли вариант привязать bgp маршрут к podkop +  hysteria 2 (виртуальный интерфейс не создается в этом режиме)?

---

**2026-01-21T22:59:48 | Mikhail Velichko**
Насколько я понял, podkop в данном случае поднимает trproxy, и заворачивает по своим спискам туда правилами nftables, но вот как в эту цепочку bird встроить?

---

**2026-01-22T09:21:36 | Yaroslav**
Привет. Перестал работать доступ по RDP к моим ВДС. Это может быть связано с настройками в роутере, хотя я ничего там не менял (установлены zapret и podkop)? При смене провайдера на мобильный интернет (не через роутер, через раздачу интернета через моб. телефон) доступ к ВДС восстанавливается. Где искать, почему доступ по RDP к ВДС пропал?

---

**2026-01-22T10:26:24 | Routerich**
нет, у нас в репе не последняя версия Podkop.
можете просто сам Podkop обновить.

---

**2026-01-22T11:18:53 | Ilya Pavlenko**
Ребят привет, подскажите кто-нибудь сталкивался с такой ситуацией:
У меня есть отдельная секция для xbox где только он и полностью завернут в тунель( отдельный vless чисто под него с Турцией)
Основная секция идет через другой сервак 

Вчера заметил что если ставлю скачиваться игру на xbox на apple tv полностью отваливается сеть, не грузит Podkop вообще
Причем на остальных устройствах все окей

---

**2026-01-22T13:26:29 | Панда**
У меня сейчас стоит podkop и он пишет конфиг в /etc/sing-box/config.json

Я положил перед/после свои конфиги и перенастроил сингбокс на загрузку конфига как категорию и норм. 

C zb не понятно оне всё в /tmp хранит

---

**2026-01-22T14:07:38 | Routerich**
https://podkop.net/docs/sections/#nastrojki-sekcij

---

**2026-01-22T14:10:58 | Routerich**
Так как снова обновили Podkop)

---

**2026-01-22T14:17:33 | Kirill K**
Здравствуйте! 
На роутере периодически (1 раз в 15 – 30 мин.) отваливается доступ к сети интернет. Интернет- соединение переходит в статус «Internet: Отключен» (на роутере Статус – Обзор). 
Выполнил следующие действия:
1.  Установил прошивку 3.8.2 без сохранения настроек.
2.  Изменил радиоканал беспроводных сетей (2.4 GHz и 5 GHz) с учётом загруженности радиоканала устройствами соседей.
3.  Установил 5 скрипт (Podkop активен, запрет выгружен и остановлен).
4.  Для себя настроил доступ Tailscale.
Что посоветуете для решения проблемы? Нужно скриншоты предоставить?

---

**2026-01-22T14:20:20 | Routerich**
Обновил версию Podkop до актуальной v0.7.12

---

**2026-01-22T14:36:42 | Nikolay Chuprina**
А где можно почитать про ключевые отличия от Podkop?

---

**2026-01-22T15:02:22 | Amras Amandil**
Всем привет. Обновил Podkop, вот пакеты. А в дигностике пишет, что старая версия (

---

**2026-01-22T16:22:21 | aND**
= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.0.4

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓150.75 MB / ↑48.00 MB
  Пинг (ya.ru via awg10): 85.351 / 86.596 ms (1 из 10 потеряно)

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОФЛАЙН
------------------------------------------------------
  Spider mode enabled. Check if remote file exists.
  --2026-01-22 16:21:10--  https://www.youtube.com/
  Resolving www.youtube.com... 198.18.0.3
  Connecting to www.youtube.com|198.18.0.3|:443... connected.
  Unable to establish SSL connection.
------------------------------------------------------
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 198.18.0.197
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  youtubeUnblock  | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!! КРИТ: Пересечение между podkop и youtubeUnblock:
    podkop                    : Youtube_Discord
    youtubeUnblock            : YouTube
    Домены: googlevideo.com youtube.com 

  podkop списки Youtube_Discord: youtube,discord
  podkop списки       main: geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10

---

**2026-01-22T16:41:58 | Kirill K**
Здравствуйте! 
Помогите, пожалуйста, разобраться в проблеме.
На роутере периодически (1 раз в 15 – 30 мин.) отваливается доступ к сети интернет, интернет- соединение переходит в статус «Internet: Отключен» (Статус – Обзор). 
Выполнил следующие действия:
1.  Установил прошивку 3.8.2 без сохранения настроек.
2.  Изменил радиоканал беспроводных сетей с учётом загруженности радиоканала устройствами соседей.
3.  Установил 5 скрипт (Podkop активен, запрет выгружен и остановлен).
4.  Тип подключения DHCP. Провайдер Билайн.
5.  Подключил двух клиентов по проводу, проблема не исчезла.
6.  Также для себя настраивал доступ через Tailscale и внес одну запись в Podkop. Больше никаких настроек с роутером не производил.

---

**2026-01-22T17:35:34 | Anna Bagler**
Да просто в main добавьте к другим спискам. Podkop - Секции, main, списки сообщества.

---

**2026-01-22T17:45:38 | Редиска на Луне**
podkop может работать без AWG WARP?

---

**2026-01-22T20:53:50 | Kirill K**
Здравствуйте! 
Помогите, пожалуйста, разобраться в проблеме.
На роутере периодически (1 раз в 15 – 30 мин.) отваливается доступ к сети интернет, интернет- соединение переходит в статус «Internet: Отключен» (Статус – Обзор). 
Выполнил следующие действия:
1.  Установил прошивку 3.8.2 без сохранения настроек.
2.  Изменил радиоканал беспроводных сетей с учётом загруженности радиоканала устройствами соседей.
3.  Установил 5 скрипт (Podkop активен, запрет выгружен и остановлен).
4.  Тип подключения DHCP. Провайдер Билайн.
5.  Подключил двух клиентов по проводу, проблема не исчезла.
6.  Также для себя настраивал доступ через Tailscale и внес одну запись в Podkop. Больше никаких настроек с роутером не производил.

---

**2026-01-22T21:16:40 | IfonYa**
Здравствуйте. Установлен подкоп + своя конфигурация AWG. Перестали работать ресурсы из podkop. Долго разбирался. Полез в интерфейс AWG и был очень удивлен когда увидел что там прописана не моя конфигурация. Какбудто кто-то зашел и поменял всё. Изменил обратно на свою. Не заработало. Перезагрузился и снова не моя конфигурация. Остановил AWG , снова импортировал свою конфигурацию , сразу же перезагрузился. Конфигурация применилась и всё заработало.
Удаленного доступа нет. Все порты закрыты по умолчанию. Что может быть? Глюк какой-то или стоит боятся что кто-то/что-то из вне залезло?
Все компы на дебиан. Винду уже лет 5 не включал. На всякий случай соскринил пир конфигурации , которая чудным образом прописалась в моем конфиге.

---

**2026-01-22T21:40:41 | Routerich**
в Podkop добавьте просто список Telegram

---

**2026-01-23T02:16:49 | Artem Mayorov**
У меня тоже ошибку стал выдавать. И перестал работать ютуб ни с того ни с сего. Но у меня на Синг бокс ругается. user.notice podkop: [fatal] Sing-box configuration /tmp/tmp.pFELdb is invalid. Aborted.

---

**2026-01-23T07:16:59 | Routerich**
Здравствуйте.
пускать ютуб через https://t.me/routerich/80283/407345 или через WARP если он у вас работает, и убрать полное проксирование в Podkop

---

**2026-01-23T07:28:41 | Routerich**
Диагностику Podkop покажите

---

**2026-01-23T08:59:49 | Routerich**
Это дело не в Podkop, а в самом скрипте проверки.

---

**2026-01-23T09:02:30 | Андрей**
Я этим скриптом обновлял - все ок, быстро и настройки сохранились все. sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)

---

**2026-01-23T11:59:55 | Николай**
Привет! Подскажите, есть где-то инструкция как настроить Zapret/Podkop для доступа к пользовательскому домену, например к kb.asipto.com?

---

**2026-01-23T12:04:30 | Николай**
А как понять какая секция нужная?)) Я попробовал создать свою такого типа, но там требуется vless///
P.S. У меня Zapret и Podkop настроены по дефолту
P.S.1 Также пробовал добавлять домен в имеющиеся секции в пользовательские списки, не помогло

---

**2026-01-23T13:16:20 | Routerich**
а диагностика Podkop с проблемных устройств что показывает?

---

**2026-01-23T13:42:25 | karat**
Подскажите пожалуйста как включить в работу свои ключи vles...  что-бы не нарушить работу Podkop?

---

**2026-01-23T14:07:09 | Сергей**
Podkop
v0.7.10Устаревшая
Luci App
v0.7.10
Sing-box
1.12.12
OS
RouteRich 24.10.4 r28959-29397011cc RR-3.8.2
Device
Routerich AX3000 v1

Нет обновлений в пакете, как поставить не нашел

---

**2026-01-23T14:31:49 | Anna Bagler**
Вы или бета-скрипт запускаете или у itdog смотрите, podkop, установка.

---

**2026-01-23T17:09:20 | Михаил**
У итдога новая версия podkop - 0.7.13 План "Ни дня без релиза". :))

---

**2026-01-23T17:44:40 | Routerich**
Обновил Podkop до актуальной версии v0.7.13

---

**2026-01-23T18:47:08 | Hellion**
Здравствуйте. Подскажите пожалуйста, обновил прошивку до 24.10.4, так же обновил podkop, теперь при переходе во вкладку podkop открывается страница без настроек.

---

**2026-01-23T20:48:32 | ALEKSEY**
я уже podkop вручную  поставил и перезагрузился, а он тут отсутствует...

---

**2026-01-23T21:25:41 | ALEKSEY**
в секции podkop же. Не нахожу, к сожалению

---

**2026-01-23T21:28:27 | Владимир Задунайский**
Помогите! Стоит PODKOP. ну никак не хочет работать сайт wowhead.com, все перепробовал(

---

**2026-01-23T22:28:11 | McQueen 95**
Господа, столкнулся с необычной проблемой - перестали работать любые vless конфиги если подключен к вай фаю. Тестил на разных устройствах - ПК, 2 разных айфона на разных iOS 17 и 26. RR 24.10.2
Для проверки гипотез менял SNI (пустой, ya.ru, icloud), обновлял/удалял podkop дабы исключить участника цепочки. Грешил даже на VPS сервак (есть 3х-ui на аеза и 4впс), оказалось что конфиги рабочие т.к. на мобильных данных подключаются все конфиги и сайты грузятся.
Пришел к тому, что всё ломается на уровне роутера/вайфая.

Есть тесты nekoray, где в основном статус "Недоступен". При этом, v2rayTun на ПК говорит, что пинг имеется, конфиги доступны, но при подключении ничего не работает.

Это что получается в первую очередь всё равно прошивку менять?(

---

**2026-01-23T23:10:33 | McQueen 95**
Спасибо, разобрался с дипсиком. Теперь ещё больше допускаю, что связано с провайдером.
Так как с помощью вашего совета накатил DNS поверх HTTPS (DoH) cloudflare и включил принудительное перенаправление всех DNS-запросов от устройств через этот защищённый канал.

Осталось развернуть заново Podkop и просунуть туда vless протокол

---

**2026-01-23T23:28:11 | McQueen 95**
После того как накатил Podkop у меня тоже самое
Про ключ имеется в виду конфиг vless?

---

**2026-01-24T09:33:22 | Yury Kuzmenko**
Для подкопа есть свой мануал 
Podkop.net
Для зероблока мануал находится в закрепе темы

---

**2026-01-24T12:24:38 | Роман**
https://github.com/itdoginfo/podkop

---

**2026-01-24T12:25:30 | Роман**
sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)

---

**2026-01-24T13:02:03 | Mart Hamon**
Проще скрипт гитхаба в терминал, он и обновит.

sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)

---

**2026-01-24T13:32:20 | VSPRO**
Всем добра! помогите решить проблему, установил Podkop v0.7.10 при диагностике вылазит ошибка DHCP содержит DNS сервер, это норм или всетаки баг в работе podkopa?

---

**2026-01-24T13:44:44 | VSPRO**
Помогите решить проблему, установил Podkop v0.7.10 при подключении смартфона к вафле смарт выдает вот это...и не подключается к инету через вафлю.

---

**2026-01-24T13:45:13 | VSPRO**
Помогите решить проблему, установил Podkop v0.7.10 при подключении смартфона к вафле смарт выдает вот это...и не подключается к инету через вафлю.

---

**2026-01-24T15:29:44 | Алекс К**
нужна помощь
RR AX3000 v1
что выполнено:
1) выключил ipv6 
2) отключил 2,4 Ггц
3) обновил до RouteRich 24.10.4 r28959-29397011cc RR-3.8.2 / LuCI openwrt-24.10 branch 25.302.55195~bfcef12
4) выполнил установку Бета версии скрипта обхода ограничений (v0.7.13)
5) отключил watchdoc
6) удалил все списки в podkop вставил свой ключ hy2 (так же тест был и vless)
7) выделил каждому устройству ip
8) в podkop включил полную маршрутизацию ip 

полсе этого у двух устройств есть другое ГЕО, но как только подключается еще олно устройсто (Windows) интет падает на всех устройствах.

ЦЕЛЬ: подключение к роутеру мгновенно определение другого гео, без ввода доменов и ссылок

---

**2026-01-24T16:03:43 | Routerich**
https://podkop.net/docs/install/

---

**2026-01-24T17:52:05 | Hellion**
Всем доброго времени суток. Подскажите пожалуйста. Вчера обновил прошивку, установил скрипт №5. Использую vless podkop. Ютуб перестал работать на телевизоре и телефоне, на ноуте нормально работает. Ничего больше не настраивал.

---

**2026-01-24T18:58:55 | makcimov**
Анализ запущен: 2026-01-24 18:58:10
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.0.8

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓0.00 MB / ↑0.06 MB
  Пинг (ya.ru via awg10): 8.685 / 12.442 ms (0 из 10 потеряно)

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/1.1 200 OK) [TLSv1.3]

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | RUNNING                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!! КРИТ: Пересечение между zapret и youtubeUnblock:
    zapret                    : zapret-hosts-google.txt
    youtubeUnblock            : YouTube
    Домены: ggpht.com googleapis.com googleusercontent.com googlevideo.com youtu.be youtube.com ytimg.com 

  podkop списки    Discord: discord
  podkop списки       main: geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.34 | RAM: 22% | NAND: 26% занято / 49.4M доступно
  13 9 * * * /usr/bin/podkop list_update

root@RouteRich:~#

---

**2026-01-24T19:05:02 | Nikita**
без сохранения настроек - можете уточнить, сетевые настройки останутся, пакеты (в том числе podkop, youtubeantiblock)  останутся или наоборот роутер будет как после сброса ?

---

**2026-01-24T19:29:54 | Routerich**
Обновил Podkop до актуальной версии v0.7.14

---

**2026-01-24T19:35:23 | Routerich**
Здравствуйте
Если хотите смотрите логи, вникайте, разбирайтесь
Либо обновите прошивку до актуальной версии и установите актуальный Podkop.

---

**2026-01-24T20:14:27 | Kiss_My_Axe**
если у вас новая версия прошивки 24.10.2 и выше, то установится новый Podkop 0.7.10.

---

**2026-01-24T20:16:51 | McQueen 95**
18.128.0.0/9
13.48.0.0/13
13.24.0.0/13
13.56.0.0/14
13.32.0.0/12
18.128.0.0/9
18.64.0.0/10
8.0.0.0/13
8.8.0.0/22
34.4.16.0/20
34.4.32.0/19
34.4.64.0/19
34.4.96.0/22
34.4.128.0/18
34.6.0.0/15
34.8.0.0/13
34.16.0.0/12
34.32.0.0/11
34.64.0.0/10
34.128.0.0/10
35.184.0.0/13
35.192.0.0/14
35.196.0.0/15
35.198.0.0/16
35.199.0.0/17
35.199.128.0/18
35.200.0.0/13
35.208.0.0/12
35.224.0.0/12
35.240.0.0/13
136.107.0.0/16
136.108.0.0/14
136.112.0.0/13
добавлю немного подсетей
инфа тоже из чата itdog у меня и другого чувака работает
для поиска накину: arc raiders голосовой чат podkop войс чат

---

**2026-01-24T20:17:07 | Kiss_My_Axe**
В верхней секции замените outbound на url и вставьте свой ключ.
Внизу Сохранить, Применить.
Как чо делать в подкопии очень подробно и понятно написано здесь - https://podkop.net/docs/install/

---

**2026-01-24T20:54:33 | username004411**
а игруны в League of Legends тут не имеются? чтото windows клиент стал отвратительно работать - то вовсе не запускается, то запускается с частичной функциональностью (например нельзя посмотреть список друзей), то получается откатать катку, но повторно совсем не хочет запускать подбор. Из того что помогло - неожиданно помогло добавление списков cloudflare в main секцию podkop (обычно она была включена в youtubeunblock, но сейчас совсем похоже там не срабатывает), чтото набегами эксперементирую но удачно-стабильно так и не работает, я канечно понимаю что игра не столь популярная как roblox, но может кто что подскажет?)

---

**2026-01-24T23:51:06 | Routerich**
Вам 1 вариант нужен или лучше из темы бета 
sh <(wget -q -O - https://raw.githubusercontent.com/routerich/RouterichAX3000_configs/refs/heads/podkop0711/universal_config_new_podkop.sh) 2>&1 | tee /root/run.log

---

**2026-01-25T01:19:23 | Nikolaý**
Анализ запущен: 2026-01-25 01:17:54
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.0.3

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.13 MB
  Пинг (ya.ru via awg10): 11.941 / 18.105 ms (0 из 10 потеряно)

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/1.1 200 OK) [TLSv1.3]

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop списки    Discord: discord
  podkop списки       main: geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.08 | RAM: 23% | NAND: 26% занято / 49.1M доступно
  13 9 * * * /usr/bin/podkop list_update

---

**2026-01-25T08:43:19 | Routerich**
можно поверх запустить и потом в списках выбрать Roblox, или просто обновить Podkop, как выше написали.

---

**2026-01-25T09:30:57 | Алекс К**
Добрый день!
Подскажите, пожалуйста, ваша команда занимается настройкой по anydesk? 
У меня не получается поставить vpn vless hy2 на podkop. Сервисы все показывают рф 
Мне для работы необходимо быстро, а я как нуб долго настраиваю. Готов оплатить криптой, если интересно только переводом, могу и переводом , но лучше криптой 

Спасибо 🙏

https://t.me/routerich/4/452547

---

**2026-01-25T10:27:56 | Yury Kuzmenko**
Да. Возможно установите на роутер подкоп и настройте раздельную маршрутизацию

https://podkop.net

---

**2026-01-25T17:38:07 | Sergio K**
global_check 
 📡 Global check run!
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛠️ System info
🕳️ Podkop:        v0.7.12 (latest: 0.7.14)
🕳️ LuCI App:      v0.7.12
📦 Sing-box:      1.12.12
🛜 OpenWrt:       RouteRich 24.10.4 r28959-29397011cc RR-3.8.2
🛜 Device:        Routerich AX3000 v1
━━━━━━━━━━━━━━━━━━━━━━━━━━━
➡️ DNS status
✅ Bootstrap DNS: 8.8.8.8
✅ Main DNS: 8.8.8.8 [doh]
✅ DNS on router
⚠️ dont_touch_dhcp is enabled. 📄 DHCP config:
config dnsmasq
 option domainneeded '1'
 option boguspriv '1'
 option localise_queries '1'
 option rebind_protection '1'
 option rebind_localhost '1'
 option local '/lan/'
 option domain 'lan'
 option expandhosts '1'
 option nonegcache '1'
 option cachesize '0'
 option authoritative '1'
 option readethers '1'
 option leasefile '/tmp/dhcp.leases'
 option resolvfile '/tmp/resolv.conf.d/resolv.conf.auto'
 option nonwildcard '1'
 option localservice '1'
 option ednspacket_max '1232'
 option dnsforwardmax '2048'
 option min_cache_ttl '600'
 option max_cache_ttl '86400'
 option confdir '/tmp/dnsmasq.d'
 option strictorder '1'
 option filter_aaaa '1'
 list server '127.0.0.1#5359'

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 Sing-box status
✅ Sing-box installed
✅ Sing-box version is compatible (newer than 1.12.4)
✅ Sing-box service exist
✅ Sing-box autostart disabled
✅ Sing-box process running
✅ Sing-box listening ports
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧱 NFT rules status
✅ Table exist
✅ Rules mangle exist
✅ Rules mangle counters
✅ Rules mangle output exist
✅ Rules mangle output counters
✅ Rules proxy exist
✅ Rules proxy counters
✅ Additional marking rules found
━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 Podkop config

config settings 'settings'
 option dns_type 'doh'
 option dns_server '8.8.8.8'
 option bootstrap_dns_server '8.8.8.8'
 option dns_rewrite_ttl '60'
 option enable_output_network_interface '0'
 option enable_badwan_interface_monitoring '0'
 option enable_yacd '0'
 option disable_quic '1'
 option update_interval '1d'
 option download_lists_via_proxy '1'
 option dont_touch_dhcp '1'
 option config_path '/etc/sing-box/config.json'
 option cache_path '/tmp/sing-box/cache.db'
 option exclude_ntp '1'
 option shutdown_correctly '0'
 option download_lists_via_proxy_section 'main'
 list source_network_interfaces 'br-lan'
 option log_level 'warn'

config section 'main'
 option connection_type 'proxy'
 option proxy_config_type 'outbound'
 option enable_udp_over_tcp '0'
 option shutdown_correctly '1'
 option user_domain_list_type 'text'
 option user_subnet_list_type 'disabled'
 option mixed_proxy_enabled '0'
 option outbound_json 'MASKED'
 option user_domains_text 'myip.com'
 list community_lists 'geoblock'
 list community_lists 'block'
 list community_lists 'meta'
 list community_lists 'twitter'
 list community_lists 'hdrezka'
 list community_lists 'tiktok'
 list community_lists 'google_ai'
 list community_lists 'porn'

config section 'Discord'
 option connection_type 'vpn'
 option interface 'awg10'
 option domain_resolver_enabled '0'
 option user_domain_list_type 'text'
 option user_subnet_list_type 'disabled'
 option mixed_proxy_enabled '0'
 option user_domains_text '2ip.ru amazonaws.com whatsapp.com whatsapp.net whatsapp.biz wa.me'
 list remote_subnet_lists 'https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_cidr_ipv4.txt'
 list community_lists 'discord'
 list community_lists 'youtube'

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 WAN config
config interface 'wan'
 option proto 'dhcp'
 option device 'eth1'
 option keepalive '5 1'

⚠️ WARP detected: engage.cloudflareclient.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ Zapret detected
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🥸 FakeIP status
✅ Router DNS is routed through sing-box
✅ Sing-box works with FakeIP: 198.18.0.35

---

**2026-01-25T18:24:39 | Routerich**
Здравствуйте.
Службы->Podkop->Настройки->DNS измените на Google.

---

**2026-01-25T18:31:30 | Данила Мастер**
Подскажите, добавил в podkop в секцию MAIN в пользовательские домены kinozal.tv, но все равно не могу на этот сайт попасть

---

**2026-01-25T19:01:52 | Василий**
После прошивки , развалился podkop, делал по закрепленной инструкции. Загрузка ранее сохраненных файлов конфигурации не спасла. Что посоветуете сделать?

---

**2026-01-25T19:04:25 | Василий**
Podkop Error
Sun Jan 25 19:55:48 2026 user.notice podkop: [error] Outbound section not found. Please check your configuration file (missing proxy_string, interface, outbound_json, or urltest_proxy_links). Aborted.

---

**2026-01-25T19:13:03 | Routerich**
Вы можете вручную его включить, убрав из Podkop ютуб, если считаете что через него работает

---

**2026-01-25T19:49:02 | Routerich**
А Podkop у вас обновился? Какая версия сейчас?

---

**2026-01-25T19:51:37 | Владимир**
Обновился. Версия Podkop v0.7.14

---

**2026-01-25T19:53:55 | Владимир**
podkop  v0.7.14-r1
luci-app-podkop  v0.7.14-r1
luci-i18n-podkop-ru  0.260124.35204

---

**2026-01-25T19:58:16 | Anna Bagler**
https://t.me/routerich/3845/245550
И это https://podkop.net/docs/sections/

---

**2026-01-25T20:42:02 | Linar**
У меня написано 
Podkop v0.7.10  Устаревшая 
Он сам должен обновляться?

---

**2026-01-25T21:43:14 | Максим Росошанский**
Анализ запущен: 2026-01-25 21:41:38
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.2/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.2):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.0.24

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.29 MB
  Пинг (ya.ru via awg10): 20.285 / 42.831 ms (0 из 10 потеряно)

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/1.1 200 OK) [TLSv1.2]

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!! КРИТ: Пересечение между podkop и zapret:
    podkop                    : main
    zapret                    : zapret-hosts-google.txt
    Домены: googlevideo.com youtube.com 

  podkop списки      Proxy: geoblock,block,google_ai,meta,telegram
  podkop списки       main: twitter,hdrezka,tiktok,discord,youtube
  podkop DNS/Bootstrap DNS: dns.adguard-dns.com / 8.8.8.8
  Версия podkop: v0.7.9

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.2)
  CPU: 0.28 | RAM: 25% | NAND: 25% занято / 54.0M доступно
  0 4 * * * service zapret restart
  13 9 * * * /usr/bin/podkop list_update

---

**2026-01-25T22:10:11 | Алексей Лютенко**
root@RouteRich:~# # роутер тест
root@RouteRich:~# echo -e "\n===== Model ====="; cat /tmp/sysinfo/model; echo -e "\n===== OpenWrt ====="; cat /etc/openwrt_release; echo -e "\n===== User Packa
ges ====="; awk '/^Package:/ {pkg=$2} /^Status: install user/ {print pkg}' /usr/lib/opkg/status; echo -e "\n===== Flow Offloading ====="; echo "SW: $( [ "$(uci
 get firewall.@defaults[0].flow_offloading 2>/dev/null)" = "1" ] && echo "on"  echo "off" ) | HW: $( [ "$(uci get firewall.@defaults[0].flow_offloading_hw 2>
/dev/null)" = "1" ] && echo "on"  echo "off" )"

===== Model =====
Routerich AX3000

===== OpenWrt =====
DISTRIB_ID='RouteRich'
DISTRIB_RELEASE='24.10.4'
DISTRIB_REVISION='r28959-29397011cc'
DISTRIB_TARGET='mediatek/filogic'
DISTRIB_ARCH='aarch64_cortex-a53'
DISTRIB_DESCRIPTION='RouteRich 24.10.4 r28959-29397011cc RR-3.8.2'
DISTRIB_TAINTS=''

===== User Packages =====
luci-i18n-podkop-ru
luci-app-podkop
podkop
luci-theme-routerich

===== Flow Offloading =====
SW: on | HW: on

---

**2026-01-25T22:21:10 | Алексей Лютенко**
===============================================
opkg update
sort: standard output: Broken pipe
opkg install luci-app-podkop
opkg install luci-theme-routerich
opkg install podkop
opkg install luci-i18n-podkop-ru
===============================================
root@RouteRich:~# 
root@RouteRich:~#

---

**2026-01-25T23:41:09 | Kiss_My_Axe**
Чуется мне, что мы ещё свидимся! :))
Пульните .14 подкоп по этому скрипту.
sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)
Чёрт его знает, вдруг излечит-исцелит.

---

**2026-01-26T05:01:36 | VK11**
Анализ запущен: 2026-01-26 07:00:42
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.0.22

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.68 MB / ↑0.27 MB
  Пинг (ya.ru via awg10): 38.914 / 39.757 ms (0 из 10 потеряно)

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/1.1 200 OK) [TLSv1.3]

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop списки Youtube_Discord: youtube,discord
  podkop списки       main: geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.18 | RAM: 26% | NAND: 34% занято / 43.9M доступно
  13 9 * * * /usr/bin/podkop list_update

---

**2026-01-26T06:44:04 | Routerich**
Здравствуйте.
ну у вас WARP по диагностике не работает.
запустите этот скрипт https://t.me/routerich/173678/449069
он обновит Podkop и установит пакеты для восстановления работоспособности WARP.

---

**2026-01-26T09:27:44 | Роман**
https://github.com/KharunDima/whatsapp-lists

Автоматические списки WhatsApp для  podkop. Честно стырено из темы itdoga 😁
Не забудьте поблагодарить автора (если у вас будет работать) хотя бы 🌟 на гитхабе.
У меня работает.

---

**2026-01-26T11:55:30 | Routerich**
Здравствуйте.
А в логах Podkop что?

---

**2026-01-26T11:58:41 | Zeal Tree**
что конкретно посмотреть? dnsmasq? или podkop?

---

**2026-01-26T12:00:32 | Zeal Tree**
ping по ip работает, но доменам не работает 

root@Svarog:~# ping -c 3 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=107 time=15.433 ms
64 bytes from 8.8.8.8: seq=1 ttl=107 time=15.445 ms
64 bytes from 8.8.8.8: seq=2 ttl=107 time=15.327 ms

--- 8.8.8.8 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 15.327/15.401/15.445 ms


root@Svarog:~# ping -c 3 yandex.ru
ping: bad address 'yandex.ru'

если перезагрузить podkop то бывают секундные просветления, но выключение podkop проблему не решает.

---

**2026-01-26T12:04:42 | Routerich**
Уберите галочку в Podkop, скачивать списки через Proxy и опять попробуйте

---

**2026-01-26T12:16:39 | Антон Татошкин**
Анализ запущен: 2026-01-26 12:15:55
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Configuring wget-ssl.

Error: Device for nexthop is not up.
Error: any valid prefix is expected rather than "/32".
Error: any valid prefix is expected rather than "/32".
= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  2a03:2880:f31b:1:face:b00c:0:25de

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 2a00:1450:4025:807::5d
    Name:       youtube.com
    Address: 2a00:1450:4025:807::5b
    Name:       youtube.com
    Address: 2a00:1450:4025:807::be
    Name:       youtube.com
    Address: 2a00:1450:4025:807::88
    Name:       youtube.com
    Address: 142.251.208.14
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  youtubeUnblock  | RUNNING                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.12.1 (Прошивка: 24.10.4)
  CPU: 0.40 | RAM: 18% | NAND: 1% занято / 65.8M доступно
  13 9 * * * /usr/bin/podkop list_update

---

**2026-01-26T13:04:53 | Антон Татошкин**
Нашел, в podkop, Верно?

---

**2026-01-26T13:05:05 | Anna Bagler**
Службы - Podkop, Секции, main, находите пользовательские домены и туда.

---

**2026-01-26T13:16:04 | Kiss_My_Axe**
В терминале роутера. Вставить, нажать ввод. В конце y и ввод.
sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)

---

**2026-01-26T13:16:31 | Zeal Tree**
Удалил podkop и перезапустил скрипт №5 ... вроде бы пока что починилось, вечером буду разбираться что за фигню я словил

---

**2026-01-26T15:05:37 | Vasa**
Листы для синг-бокса
https://github.com/savely-krasovsky/antizapret-sing-box
https://github.com/1andrevich/Re-filter-lists
https://github.com/itdoginfo/podkop

---

**2026-01-26T15:33:43 | Routerich**
сторонний софт(podkop, zapret/zapret2), собственная разработка (zeroblock)

---

**2026-01-26T18:45:40 | Виталий Комаров**
Доброго времени суток, пара вопросов, пара проблем.
1. Отвалилась машинка Bosch от интернета, даже указывая её IP в "Полностью маршрутизированные IP-адреса" толку 0, указывал и в MAIN и в своей секции Vless, при этом домены все указаны. Приложение на телефоне работает, уведомления от машинки так же приходят, но вот зайти и настроить её уже нельзя, увы не в сети.
2. Некоторые приложения, как наприер кинопаб, отказываются работать без "Полностью маршрутизированные IP-адреса", есть подозрение на то, что используется ipv6.
Вопрос, вижу что после использования скрипта, раннее я использовал только чистую установку podkop, установились такие интерфейсы как awg10 и wan6. Могу ли я безболезненно избавится от ipv6 и остаться на ipv4, раннее на нём всё прекрасно работало?

---

**2026-01-26T19:19:40 | Routerich**
Здравствуйте.
А список Telegram в Podkop добавили?

---

**2026-01-26T19:21:10 | Редиска на Луне**
предварительно необходимо удалить zapret и podkop?

---

**2026-01-26T19:39:49 | Vladimir Turbin**
ставлю через 
sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)
и вылет

---

**2026-01-26T19:45:46 | Камиль**
А подскажите пожалуйста, куда можно смотреть. 
Каждый вечер примерно в 19.00 по местному времени (ЕКБ) через RR + podkop отваливаются сервисы гугла, 
Я уже протестировал разные сервера ситуация аналогичная. Если же подключится к "чистой" сети, благо она есть в доступе, то сервисы гугла оживают. 
Если переключаемся на RR + podkop гугл снова не доступен. Не доступна даже почта, карты и прочее. Но если включить квн, всё начинает работать. 
На следующий день, с утра например в 07.00 уже снова все работает без квн. 
Может кто может намекнуть куда еще смотреть ? Может провайдер что-то смог вычислить и если есть какая-то маскировка, сразу выключают а если маскировки нет гуляй себе дальше

---

**2026-01-26T20:34:26 | Routerich**
только там Podkop v0.7.10

---

**2026-01-26T20:41:09 | None**
Есть где гайд как настроить zapret2 на разные сайты? Не хочу использовать podkop

---

**2026-01-26T21:02:59 | None**
Попробуйте отключить podkop

---

**2026-01-26T21:04:56 | Ilya Vybornov**
root@RouteRich:~# # роутер тест
root@RouteRich:~# echo -e "\n===== Model ====="; cat /tmp/sysinfo/model; echo -e "\n===== OpenWrt ====="; cat /etc/openwrt_release; echo -e "\n===== User Packages ====="; awk '/^Package:/ {pkg=$2} /^Status: install user/ {print pkg}' /usr/lib/opkg/status; echo -e "\n=
==== Flow Offloading ====="; echo "SW: $( [ "$(uci get firewall.@defaults[0].flow_offloading 2>/dev/null)" = "1" ] && echo "on"  echo "off" ) | HW: $( [ "$(uci get firewall.@defaults[0].flow_offloading_hw 2>/dev/null)" = "1" ] && echo "on"  echo "off" )"

===== Model =====
Routerich AX3000

===== OpenWrt =====
DISTRIB_ID='RouteRich'
DISTRIB_RELEASE='24.10.4'
DISTRIB_REVISION='r28959-29397011cc'
DISTRIB_TARGET='mediatek/filogic'
DISTRIB_ARCH='aarch64_cortex-a53'
DISTRIB_DESCRIPTION='RouteRich 24.10.4 r28959-29397011cc RR-3.8.2'
DISTRIB_TAINTS=''

===== User Packages =====
opera-proxy
luci-i18n-podkop-ru
coreutils-base64
luci-i18n-wdoc-wg-ru
luci-app-podkop
luci-app-zapret
tar
luci-i18n-attendedsysupgrade-ru
unzip
tailscale-lite
luci-i18n-wdoc-warp-ru
luci-i18n-wdoc-singbox-ru
kmod-amneziawg
luci-app-youtubeUnblock
luci-app-tailscale
podkop
zapret
luci-i18n-filebrowser-go-ru
sing-box-tiny
luci-i18n-tailscale-ru

===== Flow Offloading =====
SW: on | HW: on
root@RouteRich:~# ^C

root@RouteRich:~#

---

**2026-01-26T21:54:23 | Dmitry Kulakov**
ютуб на ru vps проброшен через podkop

---

**2026-01-26T22:46:29 | Алексей Скрипник**
попробовал без роутерыча в качестве днс включить  адвад и приятно был удивлен, что он благополучно всю рекламу срезал в рутубе и вк. Отсюда вопрос, как роутерыча настроить (Podkop) чтобы при работе с рутубом и вк включался адгвард. Сейчас подобраны такие настройки чтоб gemini и gpt работали

---

**2026-01-26T23:08:11 | Михаил**
А чем podkop мешает божественному zapret2?  Прекрасно сосуществуют жеж, если не устраивать драку за одинаковые домены.

---

**2026-01-26T23:49:59 | Dmitry Kulakov**
Россия.

Из коробки я не запускал скрипт №5.
Установил podkop, luci-app-podkop, добавил свой ru vps для ютуба и дискорда.

Всё работает кроме например wgmods.net. Он доступен без vpn из России.  
Во вкладке devtools в Chrome именно GET wgmods.net STATUS Pending

---

**2026-01-27T08:45:58 | Routerich**
Podkop->настройки->уберите галочку/поставьте с скачивать списки через Proxy

---

**2026-01-27T08:46:01 | Юрий 🏂**
в логах подкопа вот че :
Tue Jan 27 08:41:34 2026 daemon.err podkop[12616]: Downloading 'https://raw.githubusercontent.com/itdoginfo/allow-domains/main/Subnets/IPv4/discord.lst'
Tue Jan 27 08:41:34 2026 daemon.err podkop[12616]: Connecting to 127.0.0.1:4534
Tue Jan 27 08:41:34 2026 daemon.err podkop[12616]: Connection error: Connection failed

---

**2026-01-27T08:47:05 | Юрий 🏂**
Podkop
v0.7.9

---

**2026-01-27T08:50:58 | Юрий 🏂**
Tue Jan 27 08:48:49 2026 daemon.err sing-box[17478]: %3D&jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmVsZWFzZS1hc3NldHMuZ2l0aHVidXNlcmNvbnRlbnQuY29tIiwia2V5Ijoia2V5MSIsImV4cCI6MTc2OTQ5MzE4NywibmJmIjoxNzY5NDkyODg3LCJwYXRoIjoicmVsZWFzZWFzc2V0cHJvZHVjdGlvbi5ibG9iLmNvcmUud2luZG93cy5uZXQifQ.YUIrYPWKCaLUkRn8eFxHTb6vum1PUcAOoRZpWFdgh5A&response-content-disposition=attachment%3B%20filename%3Dblock.srs&response-content-type=application%2Foctet-stream": initialize rule-set[3]: initial rule-set: main-hdrezka-community-ruleset: Get "https://release-assets.githubusercontent.com/github-production-release-asset/661673143/26706754-c498-4f37-883a-c30e89a8907a?sp=r&sv=2018-11-09&sr=b&spr=https&se=2026-01-27T06%3A32%3A33Z&rscd=attachment%3B+filename%3Dhdrezka.srs&rsct=application%2Foctet-stream&skoid=96c2d410-5711-43a1-aedd-ab1947aa7ab0&sktid=398a6654-997b-47e9-b12b-9515b896b4de&skt=2026-01-27T05%3A32%3A18Z&ske=2026-01-27T06%3A32%3A33Z&sks=b&skv=2018-11-09&sig=%2Bp7Y0p2ZspZBx6hslOk1BAdNr%2B5%2F0vIDtlEbqYegLXY
Tue Jan 27 08:48:52 2026 daemon.err podkop[15930]: Failed to send request: Operation not permitted
Tue Jan 27 08:48:52 2026 user.notice podkop: [warn] Attempt 1/3 to download https://raw.githubusercontent.com/itdoginfo/allow-domains/main/Subnets/IPv4/meta.lst failed

---

**2026-01-27T10:03:40 | D S**
тоже появилась эта проблема, убрал галку sing-box какие-то списки скачала с гитхаба. Но где-то еще проблема. Fake-IP Заработал в роутере, но не заработал в браузере. 
Podkop: v0.4.11-r1
LuCI App: v0.4.11-r1
Sing-box: 1.11.15
OpenWrt Version: RouteRich 24.10.2 r28739-d9340319c6 RR-3.6.6
Device Model: Routerich AX3000 v1

---

**2026-01-27T10:20:24 | D S**
мне галку  Proxy download of lists помогло отщелкнуть в доп настройках Podkopа и перезапустить sing-box

---

**2026-01-27T10:45:19 | Sergei Kozlov**
Стоит самая последняя прошивка, скрипт 5 поставлен из чата BETA.

Подскажите пожалуйста, почему при использовании Podkop: MAIN -> Списки сообщества -> Cloudflare отваливается youtube ?

---

**2026-01-27T11:38:37 | Юрий 🏂**
ихууу....

Анализ запущен: 2026-01-27 11:36:26
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.0.6

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.68 MB / ↑0.33 MB
  Пинг (ya.ru via awg10): 122.640 / 123.327 ms (0 из 10 потеряно)

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОФЛАЙН
------------------------------------------------------
  Spider mode enabled. Check if remote file exists.
  --2026-01-27 11:36:57--  https://www.youtube.com/
  Resolving www.youtube.com... 173.194.73.198
  Connecting to www.youtube.com|173.194.73.198|:443... connected.
  Unable to establish SSL connection.
------------------------------------------------------
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 142.251.1.91
    Name:       youtube.com
    Address: 142.251.1.93
    Name:       youtube.com
    Address: 142.251.1.190
    Name:       youtube.com
    Address: 142.251.1.136
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop списки    Discord: discord
  podkop списки       main: geoblock,block,twitter,hdrezka,tiktok,google_ai,meta
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.9

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.46 | RAM: 23% | NAND: 27% занято / 48.9M доступно
  0 4 * * * service zapret restart
  13 9 * * * /usr/bin/podkop list_update

---

**2026-01-27T13:40:30 | Ja Morant🏀**
Всех приветствую,не могу понять что происходит
Хочу установить PodKop
И сразу скрипт 5 
В терминале ничего не происходит постоянно пере запрашивает логин и пароль 
Подскажите пожалуйста 0 понимания что к чему😳😁

---

**2026-01-27T14:11:35 | Ja Morant🏀**
А именно как добавить ps5 в PodKop,куда вводит ip самой приставки?

---

**2026-01-27T16:27:27 | S O**
добавьте к cron - с веб Система - Планировщик 
0 0 * * *  /usr/bin/podkop restart - это раз в день

---

**2026-01-27T16:58:49 | S O**
да добавьте такую строку
0 6 * * *  /usr/bin/podkop restart

---

**2026-01-27T21:07:46 | Александр**
Я использовал 5 скрипт, не помню что он выдал в конце установки, но интернет у меня работает через podkop

Вбил shikimori.one в Службы -> Podkop -> Пользлвательские домены

И после добавления обязательно сохранить и принять настройки. Минуты через 2-3 заработало

---

**2026-01-27T22:23:54 | Routerich**
Здравствуйте.
В нужной секции Podkop прописать в поле полностью маршрутизированные адреса: 192.168.1.1/24
Или свою сеть роутера.

---

**2026-01-28T06:18:07 | Routerich**
В Podkop галочку нужно поставить на "Dont Touch My DHCP!"

---

**2026-01-28T11:42:30 | Михаил Кандудин**
Всем привет. Парни, не работает Kinopub. Добавлении списка доменов в Podkop не помогло. Есть какие-то другие пути решения?
api.teleos.club
kinopub.com
kinopub.net
kino.pub
kinopub.online
proxykp.xyz
kinopub.link
trakt.tv
nuo.sh
dub.sh
git.new
urlr.me
atv4.dnskp.cc
pushbr.com
mos-gorsud.site

---

**2026-01-28T12:39:33 | Bullet for my valentine Poison**
"Код для запуска с автоматической генерацией AWG WARP и без установки/замены конфигурации Podkop (подходит для тех, кто повторно запускает, но уже внёс изменения в Podkop (чтобы конфигурация Podkop не затерлась))" - третий вариант!

---

**2026-01-28T15:59:01 | Андрей**
Здравствуйте. Где-то с 23 января  вечерами ютуб начал тормозить (сначала на ТВ tizen OS, потом и на телефоне заметил), скидывает автоматом качество до 480p, а если выше - то беда. При этом днем (даже вот сейчас еще показывает 1440 , а вот 2160 тормозит) . Прикрепляю вывод test_config_script_nightly и скрин дигностики podkop. Провайдер Ростелеком, прошивка RouteRich 24.10.4 . Сориентируйте план действий, пожалуйста. 
Я так понял, что (дождавшись очередного вечера) можно пробовать отключить podkop (ну либо проверять, чтобы секции не пересекались) и затем перебирать стратегии скриптом zapret_autoconfig_latest или zapret_autoconfig_PR . Если это не поможет (перед НГ при включенном запрете на телеке проблемы были с ютубом), то отключать podkop+zapret и пробовать ставить zapret2 по pdf-инструкции из wiki .  Или пробовать скрипт №5 (Код для запуска с автоматической генерацией AWG WARP и без установки/замены конфигурации Podkop) ? ранее я запускал №5 после обновления системы

---

**2026-01-28T17:14:18 | Святос**
Podkop Error
Wed Jan 28 17:12:55 2026 user.notice podkop: [fatal] Sing-box configuration /tmp/tmp.bGjMEj is invalid. Aborted.

---

**2026-01-28T17:52:05 | Anna Bagler**
Система - Автозапуск. Найти opera-proxy и podkop и перезапустить их.

---

**2026-01-28T18:41:00 | Anna Bagler**
Свою ссылку в секцию подкоп на роутере и списки секции пойдут через нее https://podkop.net/docs/sections/

---

**2026-01-28T18:41:44 | Yury Kuzmenko**
Podkop.net

---

**2026-01-28T18:52:13 | Yury Kuzmenko**
Через пакеты установиье luci-app podkop

---

**2026-01-28T21:11:02 | Routerich**
podkop.net Прочитайте всю документацию предварительно.

---

**2026-01-29T06:07:42 | Routerich**
Здравствуйте.
https://t.me/routerich/3845/245550
Потом добавить список Telegram в Podkop

---

**2026-01-29T09:10:53 | 📮𝟝𝟞**
Здравствуйте, podkopом, на devianart вход можно победить?

---

**2026-01-29T09:15:08 | 📮𝟝𝟞**
Под сервисным заходит, под бесплатными подписками и секцией VPN в podkop — нет🥲

---

**2026-01-29T09:19:07 | Routerich**
потому что надо все домены отловить на который он обращается и добавить их в Podkop

---

**2026-01-29T09:50:54 | Ivan Bezgubov**
А podkop через vless разве не спасают или тоже прикрыли ?

---

**2026-01-29T10:13:13 | Роман**
https://podkop.net/docs/install/

---

**2026-01-29T10:53:31 | Kiss_My_Axe**
Службы - Zapret, Стоп, Отключить.
Службы - Podkop, добавить список Youtube в секцию Discord, Сохранить, Применить.

Если роутер начнёт внезапно перезагружаться ни с того, ни с сего, то:
Система - Пакеты, Фильтр wdoc, вкладка Установлено.
Удалить всё с буквами "wdoc".

---

**2026-01-29T11:06:38 | Kiss_My_Axe**
Задача подкопа - указать чего кому куда по нажатию кнопки Применить, после чего он ваще закрывается.
Из полезного в новом режим "Exclusion".
Обновление - Службы, Podkop, Диагностика.
Верхний правый угол, WiKi, тыкнуть, быренька почитать про установку.

---

**2026-01-29T11:07:59 | Aleksandr G.**
у меня например зависает sing-box и перестает работать resolv через него и соотвественно помогает только рестарт podkop'a, а он в перезапускает sing-box... 

начинает прям подбешивать, когда отваливается днс

---

**2026-01-29T11:45:33 | Kiss_My_Axe**
Даже я сплю. Редко и тревожно, вскрикивая - zeroblock! podkop! куда ты, чёрт возьми, это прописал и зачем?! - но всё же.

---

**2026-01-29T16:20:21 | Routerich**
Скрипт 5 в теме интернет без границ + читайте и смотрите что такое podkop.net

---

**2026-01-29T16:59:31 | Tox**
А где podkop находится , чёт не могу найти , в какой вкладке

---

**2026-01-29T17:58:40 | Техническая Поддержка**
а у тебя получится ? 

#!/bin/sh

DESCRIPTION=$(ubus call system board | jsonfilter -e '@.release.description')
VERSION=$(ubus call system board | jsonfilter -e '@.release.version')
findKey="RouteRich"
findVersion="24.10.2"

if echo "$DESCRIPTION" | grep -qi -- "$findKey" && printf '%s\n%s\n' "$findVersion" "$VERSION" | sort -V | tail -n1 | grep -qx -- "$VERSION"; then
  printf "\033[32;1mThis new firmware. Running new scprit...\033[0m\n"
  wget --no-check-certificate -O /tmp/universal_config_new_podkop.sh https://raw.githubusercontent.com/routerich/RouterichAX3000_configs/refs/heads/wdoctrack/universal_config_new_podkop.sh && chmod +x /tmp/universal_config_new_podkop.sh && /tmp/universal_config_new_podkop.sh $1 $2
else
  printf "\033[32;1mThis old firmware.\nRecommendation, upgrade firmware to actual release...\nSleep 5 sec...\033[0m\n"
  sleep 5
  printf "\033[32;1mRunning old scprit...\033[0m\n"
  wget --no-check-certificate -O /tmp/universal_config.sh https://raw.githubusercontent.com/routerich/RouterichAX3000_configs/refs/heads/wdoctrack/universal_config.sh && chmod +x /tmp/universal_config.sh && /tmp/universal_config.sh $1 $2

---

**2026-01-29T18:13:52 | Ivan Bezgubov**
Можно ли трафик с определенных приложений телефона пустить тоже через podkop , если да то как это можно сделать?

---

**2026-01-29T18:29:22 | Routerich**
Здравствуйте.
Просто выбрать список Discord в Podkop

---

**2026-01-29T18:40:57 | Routerich**
Здравствуйте.
А она блоке.?
Попробуйте остановить Podkop и проверить

---

**2026-01-29T19:15:20 | Михаил**
Что бы обращение к выбранным вами доменам пустить мимо podkop.

---

**2026-01-29T19:18:14 | Routerich**
Podkop.net читаем и устанавливаем

---

**2026-01-29T19:39:21 | Роман**
https://podkop.net/docs/install/

---

**2026-01-29T19:46:54 | Routerich**
а можно посмотреть 
nft list table inet podkop
при полно прокси настройке?

---

**2026-01-29T21:38:01 | Routerich**
Так же проверьте что в Podkop включена галочка Dont My DHCP

---

**2026-01-29T22:34:09 | Vasa**
читай дальше))

можешь сделать сам - open + wg \ awg
https://github.com/GubernievS/AntiZapret-VPN


Sing-box
https://itdog.info/podnimaem-na-openwrt-klient-proksi-vless-shadowsocks-shadowsocks2022-nastrojka-sing-box-i-tun2socks/
https://habr.com/ru/articles/756178/
https://krasovs.ky/2024/08/05/sing-box-bypass.html
Из этих трёх + офф документация Sing собирается рабочий вариант вполне

Листы для синг-бокса
https://github.com/savely-krasovsky/antizapret-sing-box
https://github.com/1andrevich/Re-filter-lists
https://github.com/itdoginfo/podkop

вот такое еще есть
https://habr.com/ru/articles/981698/

https://github.com/GVCoder09/NoDPI/blob/main/README.ru.md

или классика

https://github.com/bol-van/zapret

https://github.com/ValdikSS/GoodbyeDPI

https://github.com/Waujito/youtubeUnblock

---

**2026-01-30T00:00:40 | Andrei Mischouk (Bee)**
напомните где брать форк sing-box, который поддерживает xhttp?
обновил по недосмотру sing-box, теперь podkop не может подключиться к моему vpn с xhttp

---

**2026-01-30T00:03:35 | Anna Bagler**
https://telegra.ph/Polnaya-instrukciya-nastrojki-xHTTP-v-Podkop-12-08
Переходите на zeroblock.

---

**2026-01-30T01:44:17 | FelS**
Анализ запущен: 2026-01-30 01:40:29
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.12 | YouTube IP:  173.194.73.136

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓0.00 MB / ↑0.27 MB
  Пинг (ya.ru via awg10): ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (77.88.55.242): 56 data bytes
  Программы для перезапуска:  podkop zapret2

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОФЛАЙН
------------------------------------------------------
  curl: (28) Connection

---

**2026-01-30T11:48:45 | Routerich**
они нужны если какой-то сайт не работает, то их добавляем в Podkop, для обхода.

---

**2026-01-30T18:35:23 | Yury Kuzmenko**
https://podkop.net
Вот здесь мануал

---

**2026-01-30T18:54:17 | Routerich**
поставьте/снимите галочку в настройках Podkop скачивать списки через Proxy

---

**2026-01-30T19:02:47 | Anna Bagler**
оpera-proxy и podkop перeзапустить в Система - Автозапуск.
И откройте в инкогнито, у вас luci не ту версию показывает.

---

**2026-01-30T19:55:14 | Anna Bagler**
А если cтопнуть podkop, появляется интернет?

---

**2026-01-30T21:42:09 | Ja Morant🏀**
Всех приветствую,может вопрос будет глупый,но перестало пускать в определенную игру,везде пускает,работает на приставке и ютуб и discord,еще одна запрещенная игра,но нужная не работает,может можно как-то это исправить 
В на тройках PodKop указал ip игровой консоли, 3 дня все было отлично,а сегодня перестало пускать,есть предположения что могло случиться или как это попробовать исправить,спасибо 🤝

---

**2026-01-30T23:15:59 | Routerich**
luci-app-podkop

---

**2026-01-30T23:19:34 | Anna Bagler**
Нет, podkop и к нему luci надо.

---

**2026-01-31T08:28:50 | Routerich**
Здравствуйте.
Список Meta, Telegram в Podkop выбрать.

---

**2026-01-31T10:34:11 | Vyacheslav Gorlov**
Использовал вначале скрипт №5, затем когда перестал работать ютюб, к нему добавился скрипт однокнопочного обхода, в котором в последнее время использовался последний метод, через podkop, но несколько дней как он начал вначале работать плохо, а потом и вовсе перестал. Сейчас просматриваю сообщения в телеге и тут много про запрет2. Но не совсем понятно, как его ставить.

---

**2026-01-31T10:39:20 | Vyacheslav Gorlov**
Анализ запущен: 2026-01-31 10:34:29
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.46 | YouTube IP:  198.18.0.47

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓0.00 MB / ↑0.28 MB
  Пинг (ya.ru via awg10): ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (77.88.44.242): 56 data bytes
  Программы для перезапуска:  podkop zapret2

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОФЛАЙН
------------------------------------------------------
  curl: (28) Connection timed out after 5001 milliseconds
  Warning: Problem : timeout. Will retry in 1 seconds. 3 retries left.
  curl: (28) Connection timed out after 5001 milliseconds
  Warning: Problem : timeout. Will retry in 2 seconds. 2 retries left.
  curl: (28) Connection timed out after 5001 milliseconds
  Warning: Problem : timeout. Will retry in 4 seconds. 1 retries left.
  curl: (28) Connection timed out after 5001 milliseconds
------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop списки Youtube_Discord: youtube,discord
  podkop списки       main: geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.14

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.2.1 (Прошивка: 24.10.4)
  CPU: 0.00 | RAM: 45% | NAND: 28% занято / 47.9M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-01-31T10:48:16 | Kiss_My_Axe**
Службы - Podkop. Диагностика. Остановить подкоп.
Службы - Zapret2. Перезапустить.
Проверять ютубий везде.

Этот контент блаблабла - отключить блокировщики рекламы в браузере.

---

**2026-01-31T13:50:22 | Anton M**
Здравствуйте, подскажите, пожалуйста, слабосведущему: обновил прошивку, поставил скрипт №5 (своего ключа vpn нет пока). Все, что нужно, работает, но: скорость youtube оставляет желать лучшего. Пробую вручную выбирать другое качество видео - сразу тормозит практически полностью. Работает только Podkop, если я правильно понимаю. Что могу сделать, чтобы ускорить? (если платный vpn ключ решит проблему, то сделаю. Просто нужно понимать, туда ли копать, или проблема в другом)

---

**2026-01-31T19:26:12 | Routerich**
Заранее хотел написать. Стоит переходить медленно не верно на ZeroBlock. Так как в блажащее время откажемся от PodKop и его поддержки

---

**2026-01-31T19:36:46 | Ultima**
Добрый вечер. Не устанавливается podkop по скрипту №5, кто может помочь?

---

**2026-01-31T21:54:16 | Rom@n**
Решил тоже приобщится к тесту ZB, но поскольку лениво было все с нуля настраивать (решил поэкспериментировать), удалил конфиги podkop и sing-box, собрал ASU без них, но с сохранением настроек. Накатил потом пакеты ZB, настроил и все норм, все работает как часы. Вот жду когда в ASU появится, что бы еще и его в прошивку трамбовало)))

---

**2026-01-31T22:48:10 | Михаил**
Мне не понравилось в byedpi две вещи. Первое - что нельзя тупо выигрышную стратегию взять из byebyedpi, многие параметры стратегии вредят работоспособности byedpi. Второе - byedpi ломает нормальную работу dns через sind-box. Появляется предупреждение, что dns запросы не идут через sing-box.  Для себя использую zapret2, для youtube он работает "из коробки" и мирно сосуществует с podkop.

---

**2026-01-31T23:33:50 | Routerich**
Podkop есть?

---

**2026-02-01T08:48:50 | Routerich**
Здравствуйте.
Критично.
Уберите галку/поставьте в настройках Podkop на скачивание списков через proxy

---

**2026-02-01T08:49:17 | Routerich**
Здравствуйте. 
А если остановить Podkop, то работает?

---

**2026-02-01T08:50:11 | SR**
Podkop 0.7.10 это последняя версия? как обновиться до неё? У меня сейчас стоит Podkop 0.7.7.

---

**2026-02-01T09:20:18 | Routerich**
Тут есть инструкция как добавлять домены в Podkop
https://t.me/routerich/3845/245550

---

**2026-02-01T10:21:59 | Роман**
Прописал сайт в список пользовательских доменов в main podkop, сайт начал прогружаться, но ничего не загружает. (До этого вообще не заходил). Что ещё можно попробовать?

---

**2026-02-01T12:55:59 | Pavel**
Приветствую всех! Давно не был дома и вот вернулся, однако вижу, что инста, тг нынче через роутер не работают. Что-то изменилось в настройках сервисов за последний месяц? 
Версии по:
 openwrt-24.10 branch 25.250.61039~923f8d9

Podkop: v0.6.2 LuCI App: v0.6.2 Sing-box: 1.12.4 OpenWrt Version: RouteRich 24.10.2 r28739-d9340319c6 RR-3.6.6

Zapret   v71.20250708


---
Надо что-то обновлять или удалять?

---

**2026-02-01T14:05:18 | Роман**
18.128.0.0/9
13.48.0.0/13
13.24.0.0/13
13.56.0.0/14
13.32.0.0/12
18.128.0.0/9
18.64.0.0/10
8.0.0.0/13
8.8.0.0/22
34.4.16.0/20
34.4.32.0/19
34.4.64.0/19
34.4.96.0/22
34.4.128.0/18
34.6.0.0/15
34.8.0.0/13
34.16.0.0/12
34.32.0.0/11
34.64.0.0/10
34.128.0.0/10
35.184.0.0/13
35.192.0.0/14
35.196.0.0/15
35.198.0.0/16
35.199.0.0/17
35.199.128.0/18
35.200.0.0/13
35.208.0.0/12
35.224.0.0/12
35.240.0.0/13
136.107.0.0/16
136.108.0.0/14
136.112.0.0/13
добавлю немного подсетей
инфа тоже из чата itdog у меня и другого чувака работает
для поиска накину: arc raiders голосовой чат podkop войс чат

---

**2026-02-01T16:28:51 | 亞歷山大**
Стоит podkop так зделать чтобы торренты без него ишли

---

**2026-02-01T19:10:39 | Routerich**
Здравствуйте.
Установить Podkop, туда подкинуть свой vpn, и потом задать статический ip VR, потом в Podkop добавить его в полностью маршрутизированные ip адреса

---

**2026-02-01T19:33:55 | Александр Атцик**
А как подкинуть VPN в Podkop? Задать статический IP VR могу, а в какой раздел потом его добавить подкопа?

---

**2026-02-01T19:34:40 | Routerich**
podkop.net читайте документацию

---

**2026-02-01T19:35:17 | Routerich**
Здравствуйте.
Да, можно. Надо отследить все домены куда обращаются весы и добавить их в Podkop, в любую секцию.

---

**2026-02-01T19:41:50 | Kiss_My_Axe**
Раз весы куда-то лезут, значит у них есть вайфай и айпи-адрес.
Привязать к ним IP жёстко в роутере и зарулить их полностью в маршрутизируемые адреса подкопа, в ВАРП, свой влесс, или опера-прокси.

Раздел: ПОЛНОСТЬЮ МАРШРУТИЗИРУЕМЫЕ АДРЕСА

https://podkop.net/docs/sections/

---

**2026-02-01T21:46:03 | Владимир Сурков**
Добрый вечер! 
можете мне подсказать 
как я понял чтобы смотреть ютуб есть 2 базовых варианта 
1 с помощью unblok 
2 через podkop (в этом случае работает vpn ну и реклама появляется на ютубе) 

вроде как у меня сейчас работает через unblok 

я в принципе ничего особо в настройках ничего не трогаю 
но периодически у меня есть реклама 
иногда ее нет 

могу я как-то это контролировать ?
я хочу чтобы у меня работал ютуб через подкоп 
т.к. в целом пинг и скорость отличная 
ютуб не должен лагать 
а сейчас он лагает

---

**2026-02-01T21:49:23 | Routerich**
Сможет, либо запустите 
sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)
 это просто скрипт обновления подкопа до последней версии

---

**2026-02-02T08:30:24 | Anna Bagler**
Запрет2, zeroblock или podkop не помогают?

---

**2026-02-02T10:20:37 | Amras Amandil**
Добрый день ) Не могу понять почему у меня не грузится https://9gag.com/. И так и сяк игрался с Podkop - не грузит. Буду благодарен за подсказку.

---

**2026-02-02T12:42:50 | Anna Bagler**
Вы можете почитать на podkop.net.

---

**2026-02-02T16:04:46 | Rom@n**
блин, это проблемно(( и так с подкопа слезал без сброса настроек, просто перед прошивкой по ASU почистил конфиги sing-box и podkop собрал без них, с сохранением настроек, а потом ручками поставил sing-box tiny и zeroblok и все завелось отлично

---

**2026-02-02T19:34:14 | Игорь**
Анализ запущен: 2026-02-02 19:32:58
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.4 | YouTube IP:  198.18.0.5
  Программы в автозапуске:  podkop

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop списки        main prx: geoblock,block,meta,twitter,hdrezka,tiktok,google_ai,youtube
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  $Версия podkop: v0.7.14

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.39 | RAM: 22% | NAND: 34% занято / 44.3M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-02-02T19:43:05 | Routerich**
Поставить галочку и добавить в подкоп интерфейс и добавить нужные списки https://podkop.net/docs/sections/

---

**2026-02-02T22:22:23 | Kiss_My_Axe**
Тогда.
Службы - Podkop, вкладка Диагностика.
Запустить диагностику и вывод показать.

---

**2026-02-02T22:46:37 | Pavel**
Анализ запущен: 2026-02-02 22:45:08
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: !!!_ПЕРЕНАПРАВЛЕНИЯ ОТСУТСТВУЮТ
  Facebook IP:  157.240.205.35 | YouTube IP:  142.250.185.174
  Программы в автозапуске:  podkop

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | STOPPED (MANAGED BY PODKOP)    | РАЗРЕШЁН
  zapret          | STOPPED                        | ОТКЛ
  zapret2         | STOPPED                        | ОТКЛ
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop списки        main vpn: !_russia_inside
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 77.88.8.8
  $Версия podkop: v0.7.10
  zapret2.main.custom_scripts='1'

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.07 | RAM: 19% | NAND: 31% занято / 46.1M доступно
  !!!_WatchDoc установлен

---

**2026-02-02T23:09:56 | Kiss_My_Axe**
Службы - Podkop, вкладка Диагностика. Кнопка Запустить диагностику.

---

**2026-02-03T00:09:20 | Anna Bagler**
Да, так должно быть. Сменить adguard на google в настройках подкопа. Перезапустите opera-proxy и podkop. Посмотрите, нет ли на ПК дополнительного ПО для защиты или обхода.

---

**2026-02-03T07:08:46 | Routerich**
хм, а зачем вам zapret2 если у вас всё через Podkop?
остановите Zapret2 и проверьте как будет работать
если так же, стопните ещё Podkop и посмотрите

---

**2026-02-03T07:35:15 | Routerich**
Здравствуйте.
До перезагрузки Podkop вышлите его диагностику,  в момент проблемы.

---

**2026-02-03T09:22:30 | Zeal Tree**
У меня такое бывает, если я ссылку на vless копирую из Throne, он как то так реформатирует ее, что podkop отказывается принимать. Можно конвертировать в outbound и потом вставить в podkop и воспринимается, но неудобно конечно.

---

**2026-02-03T11:10:06 | Михаил**
Вот вам еще рациональный вариант. Берёте wr3000s или аналог от cudy, настраиваете podkop и zapret. Пользуетесь. И ждете be7200 от Роутерича к середине года.

---

**2026-02-03T12:00:15 | Routerich**
а какая версия прошивки у вас и версия Podkop?

---

**2026-02-03T12:23:49 | Aleksey Drachev**
Вот в этом сообщении написано, что если есть свой vless то ключ от него можно вставить в podkop.  У меня есть свой vds/vless/xray и я хочу это проделать. Вообще, это разумно с моими результатами (логом который я запостил выше)?

---

**2026-02-03T12:31:18 | Routerich**
https://podkop.net/docs/sections/

---

**2026-02-03T14:07:02 | Routerich**
Здравствуйте.
с такими вопросами к разработчику Podkop (https://t.me/itdogchat/81758)
а так можете попробовать это https://t.me/routerich/394153

---

**2026-02-03T17:18:06 | Kiss_My_Axe**
Службы - Zapret, остановить, отключить.
Службы - Podkop, в секцию Дискорд добавить список ютуб.

---

**2026-02-03T19:06:59 | Routerich**
Здравствуйте.
Это нормально, им управляет Podkop

---

**2026-02-03T19:35:00 | Anna Bagler**
У вас nnm не работает, значит, podkop не работает. Вы 5 запускали?

---

**2026-02-04T07:57:39 | Routerich**
а если список Roblox перекинуть в секцию Discord, в Podkop?

---

**2026-02-04T09:31:05 | Routerich**
чтобы он не видел, надо весь траффик роутера пускать в Podkop.

---

**2026-02-04T09:38:02 | Routerich**
Службы->Podkop->Полностью маршрутизированные IP-адреса->добавляем строку 192.168.1.1/24 и применить нажимаем
192.168.1.1/24 - где ваша подсеть роутера

---

**2026-02-04T11:55:14 | Роман**
https://podkop.net/docs/badwan/

Это может помочь при отключении электроэнергии?

---

**2026-02-04T12:01:56 | Routerich**
Здравствуйте.
https://podkop.net/docs/sections/

---

**2026-02-04T12:53:37 | Иван**
https://podkop.net/docs/badwan/ т.е. таким способом будет проверка выбранного соединения и если  будет появляться связь то подкоп будет перезагружаться верно понимаю?

---

**2026-02-04T13:22:25 | Kuz Ka**
А можно ли в Podkop добавить socks5 прокси вместо VPN/VLESS?

У меня есть 
ip:adress@login:password

---

**2026-02-04T13:24:35 | Routerich**
Здравствуйте.
да
https://podkop.net/docs/sections/#proxy

---

**2026-02-04T13:55:14 | Routerich**
Здравствуйте.
а если перезапустить Podkop?

---

**2026-02-04T20:08:22 | Рафаэль**
Так после вставки в папку nas и ввод кода sh /tmp/universal_config_new_podkop.sh
 Жизнь пошла

---

**2026-02-04T21:02:16 | Routerich**
Здравствуйте
Запустить бета скрипт, потом зайти в Podkop, там в секции main, изменить Outbound на URL подключения и вписать свой ключ vless

---

**2026-02-04T22:45:51 | Anna Bagler**
https://podkop.net/docs/sections/ и конкретнее тут общая информация https://podkop.net/docs/sections/#tip-polzovatelskogo-spiska-podsetej-user-subnet-list-type.

---

**2026-02-05T09:24:59 | Routerich**
Здравствуйте.
в настройках Podkop галочку поставьте/снимите на загрузку списков через Proxy

---

**2026-02-05T15:03:34 | Михаил**
И еще. Зеро прекрасно живет с podkop. Главное поставить его на чистый роутер, а подкоп уже вторым. И можно, играясь запусками-стопами,  пускать то, что вам сегодня более удобно.

---

**2026-02-06T00:10:17 | Oleg Shulyakov**
Подскажите пожалуйста, я правильно понял что маршрутизация по DNS именам (как в Keenetic v5+) настраивается как в стандартном OpenWRT через luci-app-pbr + Policy Routing?
Пример настройки с Хабра
Тот же podkop для этого не нужен

---

**2026-02-06T08:51:07 | Антон**
Анализ запущен: 2026-02-06 08:48:08
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.4 | YouTube IP:  198.18.0.236

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.13 MB
  Пинг (ya.ru via awg10): 10.925 / 12.342 ms (0 из 10 потеряно)
  Программы в автозапуске:  podkop

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 301) [TLSv1.3]

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop списки Youtube_Discord vpn: youtube,discord
  podkop списки        main prx: geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  $Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.36 | RAM: 23% | NAND: 26% занято / 49.3M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

root@RouteRich:~#

---

**2026-02-06T11:04:26 | Азамат Ирназаров**
Привет, возникает проблема - после установки последнего скрипта
Многие сайты не подгружаются, либо подгружаются без статики
Помогает добавление в список пользовательских доменов podkop, что можно с этим сделать?

---

**2026-02-06T11:29:39 | 🌶️🌶️**
https://podkop.net/docs/install/

---

**2026-02-06T14:19:21 | Vasa**
podkop \ zeroblock

---

**2026-02-06T17:06:05 | Ilia Fertikov**
Подскажите, пожалуйста, у меня одного несмотря на добавление списка telegram в podkop всё ещё будто бы при отправке видео идёт лаг и они грузятся со скоростью +- 128кб/с. При этом скачивание видосов вроде бы работает норм, проблема только с отправкой. Или в телеге всегда так было и мне чудится?

---

**2026-02-06T19:18:34 | Алексей Омон**
podkopvlessvpzpodkop

---

**2026-02-06T21:03:45 | Routerich**
Здравствуйте.
Просто сейчас по умолчанию не использую Adguard в качестве dns.
Зайдите в настройки Podkop и выберите DNS провайдера Adguard

---

**2026-02-06T21:51:18 | Алексей**
Вопрос в догонку 
youtubeunblock, zapret, podkop можно будет удалить ?

---

**2026-02-06T21:58:30 | Владимир Рагулин**
У кого-нибудь получилось побороть ошибки в Fortnite через Podkop?

---

**2026-02-06T22:20:41 | Владимир**
Я после установки скрипта 5 отключил запрет1, и все нужные ресурсы разнёс по секциям podkop. Получается, можно спокойно устанавливать запрет2 - ему ничего не помешает?

---

**2026-02-06T22:37:44 | V T**
Добрый вечер! В последнее время (пару недель) ютуб очень плохо грузится в качестве 1080р и выше. Иногда и на 720р требуется время, чтобы подгрузить видео. Прям некомфортно стало смотреть. Подскажите, как полечить?

Только что установил zapret2, убрал zapret из автозагрузки и выключил вручную (не знаю, как удалить)
Ещё установлен Podkop версии v0.7.14, в нём активны секции MAIN и DISCORD. В секции MAIN добавлены списки на скрине 1.
Zapret2 запущен, со скоростью интернета тоже проблем нет, скрин 2

---

**2026-02-06T22:41:26 | Anna Bagler**
На podkop.net в секциях можете просмотреть, а потом по доменам ещё дополнительно каждый глянуть.

---

**2026-02-06T22:49:22 | Дитя Вавилона**
Зайдите podkop - дашборд

---

**2026-02-06T23:16:34 | Anna Bagler**
https://podkop.net/docs/sections/#polnostyu-marshrutiziruemye-ip-adresa-fully-routed-ips - вот полная маршрутизация.

---

**2026-02-06T23:32:00 | Роман**
Всем добрый вечер, если у меня есть свой vps сервер, как мне лучше настроить роутер? какой вариант обхода использовать, можно ли просто установить podkop из скрипта и в него вставить свою url или лучше ставить подкоп вручную? или не ставить podkop, можно ли просто засунуть vless ? или поставить на сервер амнезиюВГ и заменить в awg10 ключи на собственные?

---

**2026-02-07T09:30:48 | dissident .**
Добрый день, обновил прошивку до RouteRich 24.10.4 r28959-29397011cc RR-3.8.2 и пропали все службы: Podkop, youtube unblock  и прочие, их просто нет в прошлом меню, в других подменю также не нашел, что я упустил?

---

**2026-02-07T09:59:07 | Роман**
Хронология простая, обновили прошивку, настроили сети, установили пароли. Далее, в прошивке уже установлен youtubeunblock без веб интерфейса - если он не помогает - удаляем его (если ставите 5й скрипт - он сам удалит). Далее если есть свои ключи vless или другое - ставите или zeroblock или podkop. Для Ютуба - zapret2. 
Если всё написанное выше для вас какие-то каракули - скрипт 5 из закреплённых сообщений в ветке интернет без границ, либо скрипт бета из ветки бета.

---

**2026-02-07T11:18:13 | Мудрикув Владимир**
Всем привет. 

Стоит Podkop(платный Vless). Веб версия WhatsApp работает на компьютере, а на Android телефоне в скаченное приложение с официального сайта не приходят сообщения. 

Как решить вопрос, чтобы на телефоне полноценно работал WhatsApp?

---

**2026-02-07T14:26:44 | NITO**
Господа, прошу подсказать как решить задачку
Пытался установить по 5 скрипту podkop но на процессе установки singbox отваливается (не скачивается). Пытался поставить отдельно с гайда №2 для лечения проблемы свежей установки но kmod жалуется на архитектуру. С инетом просто не скачивает. Singbox так-же не дает надежд на установку. Пытался через Zapret по инструкции, тоже труба и по предоставленным инструкциям не хочет заводиться

---

**2026-02-07T16:25:00 | Routerich**
podkop.net изучайте раздел секции

---

**2026-02-07T16:25:36 | Әмир**
Т.е., перенаправление это будет происходить через Podkop?
Отдельный интерфейс с правилами маршрутизации настраивать не нужно?

---

**2026-02-07T23:07:19 | Nook Scheel**
⏺️ Анализ безопасности скрипта analyzer.sh

  Назначение

  Диагностический скрипт для OpenWrt роутера — проверяет DNS, VPN-интерфейс awg10, статус служб (podkop, zapret, sing-box и др.), пересечения доменных списков.

  ---
  Найденные проблемы

  🔴 Критические

  1. Перезапуск сетевого интерфейса без проверки
  ifdown awg10 && ifup awg10  # строка 3
  Сразу при запуске — может оборвать активные соединения.

  2. Удаление лог-файла без подтверждения
  rm -f "$LOG_FILE"  # строка 27
  Потеря предыдущих логов диагностики.

  3. Манипуляции с таблицами маршрутизации
  ip route add default dev "$IFACE" table "$TABLE_ID"
  ip rule add from "$IF_IP4"/32 table "$TABLE_ID"
  # ...
  ip rule del ...
  ip route flush table "$TABLE_ID"
  При прерывании скрипта маршруты останутся "висеть".

  ---
  🟡 Средние

  4. Временные файлы без trap cleanup
  tmp_dir="/tmp/analyzer_parts"; mkdir -p "$tmp_dir"
  rm -rf "$tmp_dir"  # только в конце
  При Ctrl+C — мусор останется.

  5. Скачивание файла на wget без верификации
  TEST_URL="http://speedtest.tele2.net/10MB.zip"
  wget -O /dev/null ... "$TEST_URL"
  HTTP (не HTTPS), но используется только для теста скорости — не критично.

  6. Широкие права на запись конфига
  cat /etc/opkg.conf > "$_tmp_conf"
  echo "option http_timeout $_opkg_timeout" >> "$_tmp_conf"
  Безопасно, но лучше использовать mktemp.

  ---
  🟢 Замечания

  7. Нет валидации переменных
  IF_IP4=$(ip -4 addr show "$IFACE" ...)
  wget ... --bind-address="$IF_IP4"
  Если IF_IP4 пуст — wget упадёт, но это не эксплуатируемо.

  8. exec > >(tee ...)
  exec > >(tee -a "$LOG_FILE") 2>&1
  Process substitution — работает в bash, но заявлен #!/bin/sh. На OpenWrt обычно ash/busybox, может сломаться.

  ---
  Вердикт
  ┌─────────────────┬───────────────────────────────────────────────────────────┐
  │    Категория    │                          Оценка                           │
  ├─────────────────┼───────────────────────────────────────────────────────────┤
  │ Вредоносность   │ ✅ Нет — это легитимный диагностический инструмент        │
  ├─────────────────┼───────────────────────────────────────────────────────────┤
  │ Деструктивность │ ⚠️ Низкая — перезапускает интерфейс, но не удаляет данные │
  ├─────────────────┼───────────────────────────────────────────────────────────┤
  │ Качество кода   │ 🟡 Средне — нет trap, hardcoded пути                      │
  └─────────────────┴───────────────────────────────────────────────────────────┘
  Рекомендации перед запуском

  1. Убери первую строку ifdown awg10 && ifup awg10 если не хочешь обрыва VPN
  2. Добавь trap для cleanup:
  trap 'rm -rf "$tmp_dir"; ip rule del from "$IF_IP4"/32 table "$TABLE_ID" 2>/dev/null' EXIT
  3. Запускай в screen/tmux на случай обрыва SSH

  Скрипт безопасен для использования — это типичная диагностика для роутеров с обходом блокировок (zapret, podkop, sing-box).

---

**2026-02-07T23:29:01 | Кирик**
а как удалить Podkop

---

**2026-02-07T23:29:31 | Routerich**
В Система - пакеты - вкладка установлено - в фильтре написать podkop и удалить

---

**2026-02-08T11:34:10 | Сущенко Валерий**
Здравствуйте! (я "Новичок"). Вопрос. В Меню Службы - Podkop - Диагностика в разделе Системная информация высвечено "Podkop V0.7.10 (устаревшая). Смущает слово "устаревшая",  надо что-то делать или само "рассосется". И еще, В Меню Службы - Podkop - вверху высветилась строка с ошибкой Podkop. Картинку прилагаю. Подскажите, надо - ли что то делать, или это не критично. Спасибо.

---

**2026-02-08T12:02:47 | Роман**
На вашу проблему ответили - поставить/снять галочку на скачивать списки через прокси/ВПН. Устаревшая версия - если работает нормально - не трогать. Если хочется обновить - скрипт бета или руками с гитхаба - https://podkop.net/docs/install/. 
Всё зависит от вас, готовы ли вы возиться, вникать.

---

**2026-02-08T13:50:32 | Kiss_My_Axe**
Службы - Podkop, вкладка Диагностика. Справа вверху "WIKI".
Жмём и читаем от первого пункта меню до пока не надоест.
Там норм описано всё.

---

**2026-02-08T14:21:07 | Alexandr**
'''Анализ запущен: 2026-02-08 14:19:57
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.7 | YouTube IP:  198.18.0.4

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.68 MB / ↑0.36 MB
  Пинг (ya.ru via awg10): 39.972 / 67.504 ms (0 из 10 потеряно)
  Программы в автозапуске:  podkop zapret

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 301) [TLSv1.3]

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!! КРИТ: Пересечение между podkop и zapret:
    podkop                    : main
    zapret                    : zapret-hosts-google.txt
    Домены: googlevideo.com youtube.com 

uci: Entry not found
sh: 0: unknown operand
uci: Entry not found
sh: 0: unknown operand
uci: Entry not found
sh: 0: unknown operand
  podkop списки     Discord vpn: discord
uci: Entry not found
sh: 0: unknown operand
  podkop списки        main prx: geoblock,block,meta,twitter,hdrezka,tiktok,google_ai,youtube
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  $Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.2.1 (Прошивка: 24.10.4)
  CPU: 0.20 | RAM: 22% | NAND: 26% занято / 49.2M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен'''

---

**2026-02-08T15:53:00 | Anna Bagler**
В пакетах обновить списки, podkop по фильтру и он найдет, только смотрите не установленные, а доступные вообще.

---

**2026-02-08T16:27:00 | Anna Bagler**
run.log можете кинуть? Попробуйте поставить из пакетов podkop и luci к нему.

---

**2026-02-08T17:02:03 | Routerich**
podkop.net читайте документацию, ищите в интернете про него, про списки. Зероблок по такому же принципу сделан

---

**2026-02-08T17:09:55 | Mikhail Tikhomirov**
podkop.net

---

**2026-02-08T20:46:30 | Nook Scheel**
= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!! КРИТ: Пересечение между podkop и zapret:
    podkop                    : main
    zapret                    : zapret-hosts-google.txt
    Домены: googlevideo.com youtube.com 

  podkop списки     Discord vpn: discord
  podkop списки        main prx: geoblock,block,meta,twitter,hdrezka,tiktok,google_ai,youtube
  podkop DNS/Bootstrap DNS: dns.adguard-dns.com / 8.8.8.8
  Версия podkop: v0.7.10

---

**2026-02-08T21:25:29 | Nook Scheel**
Анализ запущен: 2026-02-08 21:23:36
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: /mysite.ru/********* /mysite.ru/********* /mysite.ru/********* 127.0.0.1#5359 127.0.0.1#5053
  Facebook IP:  198.18.1.40 | YouTube IP:  173.194.221.190

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.18 MB
  Пинг (ya.ru via awg10): 6.534 / 8.818 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop zapret

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 301) [TLSv1.3]
  Запускаем остановленные службы...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop списки     Discord vpn: discord
  podkop списки        main prx: geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: dns.adguard-dns.com / 8.8.8.8
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 1.03 | RAM: 23% | NAND: 36% занято / 42.4M доступно
  0 4 * * * service zapret restart
  13 9 * * * /usr/bin/podkop list_update

---

**2026-02-08T21:25:52 | Вовчик**
Доброго времени суток. Подскажите пожалуйста, хочу поставить запрет 2, рекомендации перед установкой какие нибудь есть? Например,остановить podkop, удалить старый запрет или удалить unblockyiutubе. Или может удалить все и установить zero а потом запрет 2

---

**2026-02-09T07:57:29 | Routerich**
Здравствуйте.
попробуйте полностью пустить xbox в Podkop, в полностью маршрутизированные IP адреса

---

**2026-02-09T11:01:33 | Routerich**
Discord и YouTube можно повесить на Zapret
С Podkop убрать эти списки

---

**2026-02-09T14:19:26 | Routerich**
А если остановить Podkop, то все работает, серфтикаты создаёт?

---

**2026-02-09T14:33:05 | Routerich**
Хм, возможно проблема вообще не в Podkop, скорее всего в блок попал.

---

**2026-02-09T14:35:26 | Routerich**
Или просто добавьте домены для выпуска в Podkop и проверьте

---

**2026-02-09T14:42:15 | Routerich**
В пользовательские домены в Podkop добавьте

---

**2026-02-09T15:05:51 | Routerich**
тогда можно удалить из Podkop эти домены для выпуска и попробовать через zapret их прогнать
https://t.me/routerich/80283/407345

---

**2026-02-09T17:56:57 | Никита**
подскажите пожалуйста, куда смотреть(или что делать) если один и тот же ключ работает на одном провайдере с пк(через v2rayn) и не работает через роутер(podkop+sing box)

---

**2026-02-09T20:46:46 | Routerich**
Здравствуйте.
Логи Podkop покажите

---

**2026-02-09T21:02:52 | Routerich**
В диагностике Podkop есть логи, вот их скопировать и файлом прислать

---

**2026-02-09T22:02:02 | Aleksey Drachev**
Добрый вечер. У меня хитрая конфигурация сетей, основанная на RR. Может кто-то посоветует как заставить ее работать с подкопом. 
1. Роутер RR дома, настроен скриптом №5, диагностика подкопа - все птички зеленые. Сайты открываются как надо, YACD показывает красивую картину что куда идет
По совместительству это OpenVPN сервер в режиме Multi-point. 10.8.0.1
2. Роутер keenetic giga ii с выходом в интернет через мобильный роутер (т.е. он второй за мобильным). Назовем его "дача". Это клиент OpenVPN, он получает настройку push "redirect-gateway def1" и эта настройка реально пускает трафик в интернет именно через туннель и далее через RR. Это я вижу и это хорошо. 
3. Но мои хотелки идут дальше, и я пытаюсь настроить кинетик и его клиентов на работу через подкоп , запущенный, очевидно на RR. Я добился того, что на клиенте (ПК на "даче") запрос nslookup fakeip.podkop.fyi дает 198.18.0.25 как это и полагается. Напомню, default route на дачном ПК и на дачном роутере ведет в туннель. Поэтому я предположил, что все ок. Но нет.
Сайты вне секций подкопа (яндекс гугл...) которые должны идти мимо секций открываются без проблем. Но myip .com (явно прописан в main) вообще не открывается.Youtube показывает меню слева а в середине "нет подключения к интернету". Короче что-то мешает трафику из туннеля попадать в подкоп/sing-box....
Да, zapret у меня отключен установочным скриптом и надеюсь не вмешивается.

Может мне правильнее в теме Интернет без границ задать вопрос?

---

**2026-02-09T22:12:26 | Aleksey Drachev**
dns ведь отрабатывает как надо (если я правильно понял - тест с fakeip.podkop.fyi показал верную подсетку). Насчет первого предположения - видимо да, но это пока за границей моих познаний))

---

**2026-02-10T00:20:10 | Никита**
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.0.75 | YouTube IP:  198.18.0.76

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.68 MB / ↑0.31 MB
  Пинг (ya.ru via awg10): 100.493 / 101.579 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop zapret

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОФЛАЙН
------------------------------------------------------
  curl: (6) name lookup timed out
  Warning: Problem : timeout. Will retry in 1 seconds. 3 retries left.
  curl: (6) name lookup timed out
  Warning: Problem : timeout. Will retry in 2 seconds. 2 retries left.
  curl: (6) name lookup timed out
  Warning: Problem : timeout. Will retry in 4 seconds. 1 retries left.
  curl: (6) name lookup timed out
------------------------------------------------------
  Запускаем остановленные службы...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 198.18.0.76
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop списки          ds prx: discord
  podkop списки        main prx: google_ai,meta,!_russia_inside,twitter,!_cloudflare
  podkop DNS/Bootstrap DNS: dns.adguard-dns.com / 8.8.8.8
  Версия podkop: v0.7.7

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.2.1 (Прошивка: 24.10.4)
  CPU: 0.39 | RAM: 45% | NAND: 26% занято / 49.3M доступно
  0 4 * * * service zapret restart
  13 9 * * * /usr/bin/podkop list_update

---

**2026-02-10T10:20:04 | Bullet for my valentine Poison**
https://podkop.net/docs/sections/#spiski-soobschestva-community-lists и здесь можно глянуть краткое описание

---

**2026-02-10T14:52:25 | W12123**
Добрый день.
Раньше покупал роутер, ставил последний скрипт из темы интернет без границ и хватало на 6-8 месяцев работы, потом отваливалось. Сейчас период бесперебойной работы меньше месяца. 09.01 скрипт №5 проработал  меньше месяца.
Появились новые ветки zapret2 ZeroBlock. интернет без границ это Podkop? Сейчас есть понимание что ставить предпочтительнее и на дольше хватит?
Сравнил все версии в таблице и не нашел однозначного ответа.

---

**2026-02-10T14:52:38 | W12123**
. zapret2 (Локальный обход DPI)
Это уникальный инструмент, который не требует аренды зарубежных серверов.
• Метод: Использует фрагментацию пакетов, fake-пакеты и изменение порядка сегментов (multidisorder), чтобы DPI провайдера не смог распознать SNI (имя сайта).
• Плюсы: Максимально возможная скорость (ограничена только вашим провайдером) и отсутствие затрат на сервер.
• Минусы: Не обеспечивает анонимности и не помогает, если ресурс заблокирован по IP-адресу.
2. ZeroBlock (Прозрачное проксирование)
Это комплексная система маршрутизации, разработанная RouteRich.
• Метод: Перехватывает трафик к заблокированным ресурсам и направляет его через шифрованные протоколы (VLESS, Shadowsocks, Hysteria2 и др.).
• Особенности: Глубоко интегрирован с другими сервисами. Позволяет в один клик установить zapret2, TrustTunnel, Opera Proxy и настроить AmneziaWG. Имеет встроенную панель управления Dashboard и поддержку Clash API (YACD).
3. Podkop (Управление туннелями)
Система, во многом аналогичная ZeroBlock, так как также базируется на движке sing-box.
• Метод: Работает по схеме FakeIP, выдавая виртуальные адреса для заблокированных доменов, чтобы мгновенно перехватывать трафик.
• Особенности:
    ◦ "Don’t Touch My DHCP!": Опция для тех, кто хочет настраивать dnsmasq вручную.
    ◦ Гибкость хранения: Позволяет выбрать место для конфига и кэша (Flash или RAM).
    ◦ Мониторинг интерфейса: Помогает sing-box не "терять" нестабильные WAN-соединения (например, USB-модемы).
    ◦ Поддерживает скачивание списков доменов через выбранную прокси-секцию, если доступ к GitHub заблокирован.

--------------------------------------------------------------------------------
Основное различие между ZeroBlock и Podkop
Хотя обе системы используют sing-box, ZeroBlock позиционируется как часть экосистемы RouteRich с упором на интеграцию "всё в одном" (включая локальный DPI bypass через zapret2). Podkop же является модульным решением с акцентом на тонкую настройку сетевых параметров (DHCP, пути кэша, специфичные WAN-интерфейсы).

---

**2026-02-10T15:21:40 | IfonYa**
Доброго дня. По ощущениям ТГ замедляют сильно. Я выпал из контекста чата. Это блокировки или сбой ТГ? 
Есть уже списки для podkop? Спасибо.

---

**2026-02-10T15:38:48 | Routerich**
Можно, https://podkop.net/docs/tunnels/awg_settings/ пропускайте установку пакетов

---

**2026-02-10T18:00:26 | Routerich**
Службы - podkop

---

**2026-02-10T18:01:28 | Anna Bagler**
Подкоп установлен? Службы - Podkop Секции, main, списки сообщества.

---

**2026-02-10T20:13:26 | Len Kzn**
Всем доброго Как лучше все обновить ?

Версия прошивки openwrt-24.10 branch (25.302.55195~bfcef12)

установлен  podkop  v0.7.7-r1

установлен  zapret  72.20251022

---

**2026-02-10T21:02:29 | Sergey Kornilov**
Анализ запущен: 2026-02-10 21:01:05
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.21.4-1) to root...
Downloading http://downloads.openwrt.org/releases/23.05.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.21.4-1_aarch64_cortex-a53.ipk
Package curl (8.7.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 23.05.5):
  DNS Server:   188.191.160.253:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  31.13.72.36 | YouTube IP:  198.18.0.19
  Программы в автозапуске: podkop

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН
  Запускаем остановленные службы...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 142.251.1.136
    Name:       youtube.com
    Address: 142.251.1.93
    Name:       youtube.com
    Address: 142.251.1.190
    Name:       youtube.com
    Address: 142.251.1.91
    Name:       youtube.com
    Address: 2a00:1450:4010:c03::88
    Name:       youtube.com
    Address: 2a00:1450:4010:c03::be
    Name:       youtube.com
    Address: 2a00:1450:4010:c03::5d
    Name:       youtube.com
    Address: 2a00:1450:4010:c03::5b
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  Версия podkop: 0.4.6-r1

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 23.05.5)
  CPU: 0.22 | RAM: 35% | NAND: 20% занято / 56.1M доступно

---

**2026-02-10T21:13:56 | Stanislav Gurov**
Добрый вечер!

Использую связку podkop + zapret. Вижу, что сейчас активно рекламируют связку zeroblock + zapret2.

Подскажите, где-то можно ознакомиться со сравнением podkop и zeroblock?

---

**2026-02-11T08:48:09 | Routerich**
Здравствуйте.
а если остановить Podkop?

---

**2026-02-11T09:12:33 | Aleksandr**
Столкнулся с такой ситуацией, что как будто провайдер Билайн блочит интернет для роутера то ли из за того что podkop стоит то ли еще из за чего. Выглядит это примерно так, все ок работает потом в какой то момент интернет пропадает, при этом wan получает ip от провайдера но дальше уже ничего не работает. Если попробовать остановить podkop и перезагрузить роутер то не помогает, но если поменять роутер на другой то начинает работать интернет. Причем такая ситуация за 10 дней два раза повторилась, все ок работает в том числе и все что подкопом проксируется и потом в какой то момент перестает вообще все работать даже ру сайты и отключение подкопа ни как не помогает, только смена роутера.

---

**2026-02-11T11:29:25 | Gambeet**
= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.7 | YouTube IP:  173.194.221.136

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓0.00 MB / ↑0.33 MB
  Пинг (ya.ru via awg10): ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (77.88.44.242): 56 data bytes
  Программы в автозапуске: podkop zapret2

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОФЛАЙН
------------------------------------------------------
  curl: (28) Connection timed out after 5001 milliseconds
  Warning: Problem : timeout. Will retry in 1 seconds. 3 retries left.
  curl: (28) Connection timed out after 5002 milliseconds
  Warning: Problem : timeout. Will retry in 2 seconds. 2 retries left.
  curl: (28) Connection timed out after 5001 milliseconds
  Warning: Problem : timeout. Will retry in 4 seconds. 1 retries left.
  curl: (28) Connection timed out after 5001 milliseconds
------------------------------------------------------
  Запускаем остановленные службы...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 173.194.221.136
    Name:       youtube.com
    Address: 173.194.221.93
    Name:       youtube.com
    Address: 173.194.221.190
    Name:       youtube.com
    Address: 173.194.221.91
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop списки        main prx: geoblock,block,meta,twitter,hdrezka,tiktok,google_ai,anime,porn
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.56 | RAM: 47% | NAND: 27% занято / 48.4M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-02-11T11:32:17 | Alex**
Запущен podkop и zapret. Не загружается на телефоне, подключённом к роутеру,  Google Play. Где нужно поправить?

---

**2026-02-11T11:35:52 | Maxim Mrakov**
Всем привет, при попытке обновить podkop пишет redirecting output to wget-log.1 где он храниться и кому его можно скинуть что бы подсказали что не так :с

---

**2026-02-11T12:18:48 | VK11**
Странности с DNS. Имеем роутер последней версии и прошивкой, накатан скрипт 5. по умолчанию. в случайный момент времени пропадает доступ в интернет с устройств по сети и wifi. диагностика с компа показывает, что dns запрос на роутер уходит (видно в мониторинг - трафик пользователей) но ответа нет. на команду nslookup instagram.com выдается адрес роутера и ожидание ответа. при этом в сеть - диагностика все запросы dns отрабатываются. а podkop диагностика красным только Браузер использует FakeIP. В настройках podkop меняем тип dns с DOH на незащищенный - все нормализуется и начинает работать. Возвращаем настройки в DOH - все продолжает работать до следующего раза. Вопрос собственно куда копать?

---

**2026-02-11T13:10:43 | Anna Bagler**
Перезапустите opera-proxy и podkop. Посмотрите.

---

**2026-02-11T13:17:58 | Sergey Elyutin**
Ребята, есть проблема: OpenCode стабильно падает через 10 секунд, так как трафик идет мимо туннеля напрямую в pppoe-wan (через Outline всё ок). В логах при этом абсолютная тишина, никаких ошибок не фиксируется. Проверка показала, что в nftables полностью отсутствуют правила для sing-box/Podkop, а в конфиге /etc/config/podkop для секции с opencode.ai указан option connection_type 'vpn'.
Посмотрите, пожалуйста, почему не создаются правила перехвата трафика (TProxy/REDIRECT) в fw4. Пакеты просто не попадают в движок и не отображаются в логах проксирования, а улетают в прямой канал, где блокируются провайдером.

---

**2026-02-11T13:43:53 | Владимир Волков**
Очень замудрённое "PodkopTable", если ничего не поменялось

---

**2026-02-11T13:57:42 | Sergey Elyutin**
root@RouteRich:~# nslookup opencode.ai
Server:         127.0.0.1
Address:        127.0.0.1:53
Name:   opencode.ai
Address: 198.18.0.48

root@RouteRich:~# nft get element inet PodkopTable podkop_subnets {198.18.0.48}
Error: Could not process rule: No such file or directory
get element inet PodkopTable podkop_subnets {198.18.0.48}

---

**2026-02-11T14:04:06 | Routerich**
Здравствуйте.
покажите 
Службы->Podkop->диагностика

---

**2026-02-11T14:05:06 | iProxx**
В службах Podkop не появился, только Zapret

---

**2026-02-11T14:06:10 | Mikhail Tikhomirov**
https://podkop.net/docs/yacd/

---

**2026-02-11T14:11:24 | iProxx**
Сделал сразу после установки скрипта. Zapret появился а Podkop нет

---

**2026-02-11T14:17:13 | Routerich**
не вместилось всё в файл
заново запустите и потом после заврешения работы скрипта скриншот последних строк пришлите, где про установка Podkop и выбранной стратегии

---

**2026-02-11T14:32:14 | Sergey Elyutin**
открыл, не попадают, трафик Google и Facebook успешно проксируется, а opencode.ai в списке соединений вообще не появляется. Объясните, пожалуйста, принцип работы подкопа: почему DNS выдает Fake-IP, но этого адреса нет в nft-сете @podkop_subnets

---

**2026-02-11T20:10:09 | Святос**
Так надо сперва podkop подождать...

---

**2026-02-11T20:24:24 | Anna Bagler**
Нет, полностью маршрутизированные - это IP ваших устройств, которые вы хотите насильно пускать в секцию. Вам нужны пользовательские подсети для подсетей и домены - для доменов.
podkop.net Cекции. Изучайте.

---

**2026-02-11T20:28:38 | vladimir**
Доброго времени суток. Есть такой образовательный портал udemy.com. Купил там курс, а смотреть его невозможно, по причине того что видео плохо прогружается. Доступа к порталу вообще не было, пока не воткнул в список пользовательских доменов podkop: udemy.com, udemycdn.com,udemy.extole.io. Может подскажет кто буду признателен🙏

---

**2026-02-11T20:33:35 | Alexander**
Народ, ни у кого ни каких чудес сегодня с роутером не происходит? Интересует МТС Кировская область. Сначала на одном ПК пропал инет, при этом роутер пинговался но инета не было, со второго ПК пинг был, интернет был. Перезагрузил роутер, второй комп отвалился напрочь, роутер не пингуется. Первый комп роутер пингуется, интернета нет. По wifi телефоны не подключается. Помог сброс роутера. НО! Из бэкапа в котором были установлены podkop, zapret ни первый, ни второй не восстановились. Что это такое?) Я просто офигел от такого чуда. Не первый день этим занимаюсь. Просто чудеса какие-то

---

**2026-02-11T20:39:04 | vladimir**
Доброго времени суток. Есть такой образовательный портал udemy.com. Купил там курс, а смотреть его невозможно, по причине того что видео плохо прогружается. Доступа к порталу вообще не было, пока не воткнул в список пользовательских доменов podkop: udemy.com, udemycdn.com,udemy.extole.io. Может подскажет кто буду признателен🙏

---

**2026-02-11T22:44:29 | vladimir**
www.udemy.com
frontends.udemycdn.com
hls-c.udemycdn.com
mp4-c.udemycdn.com
img-c.udemycdn.com
trk.udemy.com
m.stripe.com
m.stripe.network Странно как-то)) Стоит добавить такую штуку в Main Podkopa сразу отлетает Meta с Телегой))) Видимо придется прокачаться до ZeroBlock))) Неохота.... работает же все кроме этого курса будь он неладен))) Всем спасибо за помощь!

---

**2026-02-11T23:28:15 | Inko**
В мануале написано
Перейти в Службы - Podkop - искать Source Network Interface поле "Interface" укажите интерфейс Tailscale (обычно tailscale0) 2

А если там нет вроде этого поля куда идти? Не понятно типо... видимо это старая версия мануала а интерфейс поменялся нет?

---

**2026-02-12T02:00:38 | Anna Bagler**
Это снаружи и внутри. Снаружи не надо брать, если вы тут. И внутри желательно тоже не брать, а брать частями. Но можно, если в одной секции. Почитайте Секции на podkop.net.

---

**2026-02-12T07:18:10 | Максимка**
Здравствуйте. Почему в Podkop configuration пишет "Здесь пока пусто"?

---

**2026-02-12T14:19:18 | Роман**
zeroblock, podkop

---

**2026-02-12T14:47:57 | Nikita**
@RouterichSupport друзья, у меня вопрос родился. саппорт амнезии ответил что openwrt прошивки начиная с 24.10. 3  поддерживают, протокол амнезии 2.0. отсюда вопрос, если podkop не поддерживает их а роутер поддерживает значит как то можно обойти ограничения подкопа? ну или я совсем запутался. объясните дураку

---

**2026-02-12T17:31:20 | Роман**
https://podkop.net/docs/install/

---

**2026-02-12T17:47:43 | Stanislav Gurov**
Спасибо за прошивку, очень ждал)

Только что перепрошился, настроил сеть + WiFi. Мастер настройки - жирный лайк 👍👏

WiFi потестил на iPhone 13 Pro Max возле роутера, по ощущениям ~ на 15% выросла скорость.

Теперь настал момент для тестирования новой связки zeroblock + zapret2 вместо старой podkop + zapret :)

---

**2026-02-12T20:26:17 | Настроить Роутер**
Перед установкой ZeroBlock , обязательно удалять Podkop? Или достаточно, отключить/остановить ?

---

**2026-02-12T20:46:24 | Роман**
https://telegra.ph/Polnaya-instrukciya-nastrojki-xHTTP-v-Podkop-12-08

---

**2026-02-12T21:21:09 | Rustam**
Может кто сталкивался с такой проблемой... После обновления до 3.9.0 перестал работать gemini через подкоп. В диагностике самого подкопа всё впорядке. Конфигурации рабочие, если весь трафик пустить по vpn, то gemini не ругается. Проблема проявляется именно при работе через podkop. Может разработчики могут сразу предположить, в чем может быть дело? На прошлой прошивке всё работало корректно.

---

**2026-02-12T21:35:45 | Anna Bagler**
Идите в Службы - Podkop. Ceкции. Находим секцию discord, yдаляем список YouTube. Поднимаемся в main, cписок добавляем.

---

**2026-02-12T23:12:28 | Stanislav Gurov**
При использовании podkop и tailscale для удаленного доступа к роутеру, в подкопе необходимо было указывать Source Network Interface. Скажите, в ZeroBlock нужно что-то подобное сделать?

---

**2026-02-12T23:19:21 | Роман**
Обновите на 1.3 unblock через пакеты. 
А для обхода по ip вам либо zeroblock, либо podkop.
Или если уже стоит 1.3 - перезапустите.

---

**2026-02-13T06:06:33 | Ivan**
Podkop умеет работать при постоянных белых списках на мобильном интернете?

---

**2026-02-13T08:22:57 | Routerich**
Здравствуйте
по 5-му скрипту ставится Podkop.
при чём тут ZeroBlock?

---

**2026-02-13T10:40:01 | Роман**
База под использование различных пакетов как zeroblock, podkop, zapret2, в виде openwrt есть. Но придется их самому установить и настроить.

---

**2026-02-13T11:40:38 | Routerich**
Здравствуйте.
а интерфейс TailScale добавлен в Podkop/ZeroBlock?

---

**2026-02-13T11:48:35 | Routerich**
Здравствуйте.
можно из Podkop удалить его и попробовать через Zapret2 пустить
или искать домены на которые телевизор обращается, возможно там другие домены или полностью телевизор в VPN пустить

---

**2026-02-13T14:19:56 | Routerich**
Podkop это средство маршрутизации для впн и прокси, запрет2 не требует впн или прокси, на уровне другом работает. Тут вам решать. Статус - мониторинг - журнал URL адресов, там отследить, либо на тв ставить программу для отслеживания, типо pcapdroid и подобные, если реально установить

---

**2026-02-13T14:21:39 | Routerich**
Подкоп или зероблок установить. По подкопу документация на podkop.net . По зероблоку мануал в теме Вики, но для начинающих посложнее  будет. Изучайте

---

**2026-02-13T16:40:27 | Максим**
Этот сайт не может обеспечить безопасное подключение
На сайте chatgpt.com используется неподдерживаемый протокол.
ERR_SSL_VERSION_OR_CIPHER_MISMATCH

Chatgpt перестал работать. Пользовался им через актуальный Podkop (раздел main). До сегодняшнего дня всё отлично работало.

---

**2026-02-13T16:53:43 | Максим**
при переносе chatgpt'шных доменов во вторую секцию podkop'а (awg) ошибка аналогичная.

---

**2026-02-13T17:04:30 | Роман Инжектора KOTYARA**
Wg блокируется тпсу ..недавно проходил это ..амнезия wg работает  пока что 

https://podkop.net/docs/tunnels/awg_settings/

sh <(wget -O - https://raw.githubusercontent.com/Slava-Shchipunov/awg-openwrt/refs/heads/master/amneziawg-install.sh)

---

**2026-02-13T17:26:14 | Михаил**
https://podkop.net/docs/tunnels/wg_settings/
И сразу смотрите там же в сторону awg. Wg нынче блочат.

---

**2026-02-13T20:15:30 | Routerich**
https://podkop.net/docs/install/#avtomaticheskaya-ustanovka-i-obnovlenie и почистить кеш в браузере

---

**2026-02-14T09:23:16 | Андрей**
Podkop, beta или ZB2? Что после обновления прошивки лучше ставить?

---

**2026-02-14T11:58:46 | JB**
Последний скрипт с Podkop на эту прошивку встанет ?

---

**2026-02-14T12:36:06 | Борис**
Доброго дня, я правильно понимаю, что luci-клиентов, поддерживающих обновляемые подписки vless, в данный момент во встроенных репозиториях opkg нет? v2rayA, sing-box (голый), podkop не умеют это делать? Заранее извиняюсь за ленивый вопрос, т.к. я сам мог проверить это методом проб и ошибок, но эти пакеты весят много мегабайт, и я боюсь, что они могут испортить мою конфигурацию при установке. Спасибо

---

**2026-02-14T13:01:43 | Борис**
Понятно. Вроде бы это мне и нужно. Я просто никогда не пользовался подкопом и зероблоком - начинал изучение постепенно, с простых конфигураций, поэтому не знаю их возможностей. Но судя по тому, что вы описали, это то, что мне нужно. И в теории можно bash скрипт написать и поставить в cron, чтобы он "сервера" в подписке обновлял в указанных утилитах. Это если я правильно понял ваш ответ - я могу изначальную подписку загрузить в zb или podkop, она успешно распарсится на список серверов, и этот список никогда не будет обновляться сам по себе

---

**2026-02-14T16:25:57 | Joseph Brodsky**
Збс, весь трафик что идет через Vless в Podkop перестал работать

---

**2026-02-14T16:41:06 | Joseph Brodsky**
Опять трафик в podkop через vless лег (

---

**2026-02-14T16:57:50 | Routerich**
У вас тут параметры что podkop не поддерживает, поэтому и не взлетает, упростите ключ

---

**2026-02-14T17:32:12 | Philipp**
Всем привет, не очень понимаю, если у меня есть свой ключ VLESS, стоит ли запускать скрипт №5 или лучше вручную настроить podkop и zapret?

---

**2026-02-14T17:55:36 | Alex S**
Добрый вечер.Не подскажете почему при включенном youtubeUnblock  у меня не работает  вторая секция Podkop(при диагностике пишет ,что секция YouTube _Discord не отвечает). Соответственно при отключении youtubeUnblock диагностика показывает работу обеих секций.В списках сообщества ,если что, YouTube нет.Второй день перестал работать Roblox,был запущен через Podkop (2-я секция). YoutubeUnblock нужен,так как есть телевизоры и в этом сочетании всё работает.Roblox пока так и не запустил.Podkop самый последний.

---

**2026-02-14T18:39:04 | Salomon**
У меня на телевизоре нормально youtube не заработал пока не удалил анблок, podkop c vless нормально и youtube и roblox были

---

**2026-02-14T18:49:10 | Routerich**
вот эти
https://github.com/KharunDima/whatsapp-lists?tab=readme-ov-file#-для-podkop

---

**2026-02-14T19:18:55 | Виктор Херсонов**
Всем привет. Только что провайдер отключал интернет на 10 мин. После включения перестал работать ютуб. У меня ax3000 прошивка Release 3.8.2 (OpenWrt 24.10.4) — 01.11.2025. Ранее запускал скрипт sh <(wget -q -O - https://raw.githubusercontent.com/routerich/RouterichAX3000_configs/refs/heads/wdoctrack/universal_config_new_podkop.sh) 2>&1 | tee /root/run.log Что можно предпринять?

---

**2026-02-14T20:23:49 | Мудрикув Владимир**
Добрый день. Получилось удалённо подключиться к роутеру через компьютер. 

С телефона не понятно как подключаться. Выбивает программу постоянно. 

Я правильно понимаю, что можно с телефона подключаться к роутеру и весь трафик через него пускать, чтобы он был вместо обычного vpn, который стоит на телефоне? 

Цель, чтобы на улице пользоваться proxy от podkop, который стоит на модеме.

---

**2026-02-14T20:32:42 | Routerich**
podkop.net там есть документация по секциям. В целом и для нашего зероблока основа подойдёт

---

**2026-02-14T20:47:45 | Joseph Brodsky**
Сегодня podkop прям отжигает. Постоянно что-то отваливается

---

**2026-02-14T21:18:47 | Routerich**
Система - автозапуск, найти doh-proxy, DNS failsafe proxy, stubby, podkop. нажать на включено и на стоп. Перезагрузить роутер. Пробовать так открыть допустим тот же гугл

---

**2026-02-14T22:21:52 | Salomon**
Маршрутизация через podkop с vless, Ютюб без немецкой рекламы, блокировка рекламы вобщем, типа Adguard

---

**2026-02-15T01:25:23 | Павел Четвертков**
zeroblock это типа podkop? Раздельное туннелирование?

---

**2026-02-15T08:53:42 | Routerich**
Хорошо, у вас через WARP сейчас ютуб.
Можете попробовать zapret2, предварительно убрав YouTube из Podkop

---

**2026-02-15T12:42:26 | Дмитрий Долотовских**
А завтра в podkop появятся новые фичи, по-моему это вопрос развития.

---

**2026-02-15T15:55:04 | Routerich**
В последнем подкопе есть вариант с исключениями. Podkop.net там есть документация

---

**2026-02-15T16:03:41 | Константин**
Подскажите? А как podkop тут стоит?

---

**2026-02-15T16:33:00 | Александр Грачев**
через podkop

---

**2026-02-15T17:22:19 | panniqi**
Download completed (1035 bytes)
chmod: /opt/zapret/ipset/*.log: No such file or directory

curl: (28) Connection timed out after 120001 milliseconds
zapret not work...
grep: /etc/crontabs/root: No such file or directory
grep: /etc/crontabs/root: No such file or directory

Create and configure tunnel AmneziaWG WARP...
cfg09b847
uci: Entry not found
Zone Create
cfg10dc81
Configured forwarding
cfg11ad58
Automatically including '/usr/share/nftables.d/ruleset-post/537-youtubeUnblock.nft'
Automatically including '/usr/share/nftables.d/table-post/20-miniupnpd.nft'
Automatically including '/usr/share/nftables.d/chain-post/dstnat/20-miniupnpd.nft'
Automatically including '/usr/share/nftables.d/chain-post/forward/20-miniupnpd.nft'
Automatically including '/usr/share/nftables.d/chain-post/srcnat/20-miniupnpd.nft'
Interface awg10 not found
Wait up AWG WARP 10 second...
Create and Check AWG WARP... Attempt #2... Please wait...

Restart service dnsmasq, odhcpd...
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: no lease, failing
Stop and disabled service 'youtubeUnblock' and 'ruantiblock' and 'zapret'...
uci: Entry not found
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: no lease, failing

Start and enable service 'doh-proxy'...
grep: /etc/crontabs/root: No such file or directory
Starting doh-proxy 2025.07.01-r2 instances ✓✓✓✓
Setting trigger for wan ✓
Service Podkop and Sing-Box restart...
crontab: can't open 'root': No such file or directory

AWG self-hosted, пинг с интерфейса не идет.
При повторной настройки AWG все прошло, но в вебке на значения H1-4 просит целые числа, хотя в конфиге AWG там к примеру 593118597-1218006832

---

**2026-02-15T17:46:43 | 𝔅𝔲𝔯𝔦k**
Подскажите, пожалуйста, новичку, в скрипте №5 Podkop и Zapret ставится? Zapret2 отдельно надо ставить? Или если работает Podkop, то Zapret не нужен?

---

**2026-02-15T17:46:51 | Routerich**
https://podkop.net/docs/tunnels/awg_settings/ момент с установкой пакетов пропустить

---

**2026-02-15T17:55:52 | Routerich**
Можно либо бета скрипт запустить либо скрипт с github автора Podkop

---

**2026-02-15T17:56:17 | Simon**
Подскажите как обновить Podkop ? Пишет что устаревшая версия. v0.7.10

---

**2026-02-15T17:57:12 | Ivan Matveev**
Нашел. Оно?
sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)

---

**2026-02-15T17:57:50 | Routerich**
podkop.net раздел установка. Там актуальная ссылка на обновление всегда

---

**2026-02-15T18:23:19 | Routerich**
Здравствуйте.
В Podkop

---

**2026-02-15T18:31:47 | Routerich**
Через
Службы->Podkop->

---

**2026-02-15T19:19:34 | Routerich**
https://podkop.net/docs/dns/ в секции с впн интерфейсом, именно с впн, включить резолвер. Тогда днс запросы к тому что в списке, будут через впн идти. В секции vless его не включить

---

**2026-02-15T20:00:47 | Вячеслав**
Не думал вообще, что клиент на роутере поднять сложнее, чем xray на сервере. Уже с четвертой программой вожусь. v2rayA падал, Passwall2 не работал, так и не разобрался, Podkop вот заработал частично, но кроме ютуба на телефоне и тв, а мне как раз на тв надо. ZeroBlock пока вообще не фурычит

---

**2026-02-15T21:52:16 | Routerich**
https://podkop.net/docs/tunnels/awg_settings/ момент с установкой пакетов пропускайте и внимательно читайте. В wan зону не надо добавлять

---

**2026-02-15T22:35:53 | Nickname**
Сегодня возник вопрос по поводу работы Ютубе. На смартфоне и телевизоре с системами андроид работает без проблем. На винде 7 и 10 запускается нормально,доходит до 1 минуты просмотра и выскакивает окно типа Произошла ошибка,перегрузите страницу. Включен Podkop,ютубанблок выключен. Кто подскажет в решении проблем? Установлен скрипт 5. Переустанавливал его сейчас начисто. Ставил бета 5 скрипт. Прошивка последняя Проблема остаётся

---

**2026-02-16T00:50:35 | Nikolai Korp**
Странно, вчера делал знакомому, zeroblok установил, автонастройка opera, proxy awg, zapret2 галки поставил. подождали 5 минут и YB заработал на ПК и ТВ самсунг(ДомРУ)
У другого сегодня podkop обновил и zapret, через zapretmanager подобрал новые стратегии. тоже YB поднялся

---

**2026-02-16T00:53:18 | Nikolai Korp**
У себя cydy+openwrt. podkop + zapret, работает отлчно(ПРов местный но купленый билайном)
Через 2 дня приедет RR уже свой. буду тоже zeroblok + zapret2 ставить

---

**2026-02-16T07:47:23 | Диншат Валеев**
Вот и я стал счастливым обладателем Routerich'а
Брал на замену AX3000T, перенес свои конфиги Zapret и Podkop и все полетело
Спасибо большое команде Routerich за такое качественное и мощное устройство!

---

**2026-02-16T08:50:29 | Routerich**
Службы->Podkop->секция Discord->Предустановленные списки-> удалите 3 строку

---

**2026-02-16T10:08:08 | Эльчин Тагиев🤓**
= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  youtubeUnblock  | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.02 | RAM: 19% | NAND: 1% занято / 66.1M доступно
  13 9 * * * /usr/bin/podkop list_update

---

**2026-02-16T10:19:56 | Эльчин Тагиев🤓**
= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  youtubeUnblock  | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.25 | RAM: 18% | NAND: 1% занято / 66.2M доступно
  13 9 * * * /usr/bin/podkop list_update

---

**2026-02-16T10:35:10 | Эльчин Тагиев🤓**
= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.11 | YouTube IP:  198.18.0.12

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.68 MB / ↑0.31 MB
  Пинг (ya.ru via awg10): 41.657 / 55.236 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop списки Youtube_Discord vpn: youtube,discord,telegram
  podkop списки        main prx: geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.60 | RAM: 22% | NAND: 26% занято / 49.3M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-02-16T11:19:57 | Симеона**
Здравствуйте! Видит ли провайдер факт использования zapret/podkop/zeroblock?

---

**2026-02-16T11:59:05 | Семьдесят Семь**
что лучше для vless сервера zeroblock или podkop?

---

**2026-02-16T12:02:26 | Routerich**
он у нас не в релизе, а сам скрипт для работы в релизе, сам Podkop до сих пор не в релизе.

---

**2026-02-16T12:05:08 | Дмитрий Кобзарь**
У нас я так понял на выбор три приложения: podkop, zapret, zeroblock. С каким лучше заморочится

---

**2026-02-16T12:06:31 | Routerich**
Здравствуйте.
Podkop,zeroblock Это средства маршрутизации
а zapret это средство обхода DPI

---

**2026-02-16T12:11:17 | Rustam Ikramov**
Здравствуйте всем
Какой сейчас актуальный способ / инструмент обхода? 
Нужно ли сейчас обновляться на что то более актуальное, ставить новые пакеты какие-нибудь?
У меня стоит следующее:
RouteRich 24.10.4 r28959-29397011cc RR-3.8.1 / LuCI openwrt-24.10 branch 25.297.70664~6ce6ec4
Podkop: v0.6.2
LuCI App: v0.6.2
Sing-box: 1.12.4
OpenWrt Version: RouteRich 24.10.4 r28959-29397011cc RR-3.8.1
Device Model: Routerich AX3000 v1

---

**2026-02-16T12:14:17 | Дмитрий Кобзарь**
Т. е. Ставим podkop и zapret?

---

**2026-02-16T14:28:37 | Anna Bagler**
Полный мануал по zb читайте. podkop.net можно почитать по Секциям, т.к. принципы схожи.

---

**2026-02-16T14:49:10 | Andrey**
Всем привет, а есть кто на ростелеком Москва? У меня что-то сегодня странное происходит. Перестал работать podkop, я пытался поиграть с днс, серверами, но не было толку. Решил с нуля установить последнюю прошивку и первое время работал подкоп, а потом опять помер. Сервера vless использую.

---

**2026-02-16T14:49:27 | Михаил**
Всегда говорил, что обходов должно быть как можно больше. Youtubeunblock + zapret2+ podkop с 7-ью разноплановыми секциями по идее должны свести с ума любой ии у провайдера.

---

**2026-02-16T14:52:40 | Routerich**
Здравствуйте.
Покажите диагностику Podkop

---

**2026-02-16T15:33:26 | Roman**
Доброго дня.  5 скрипт все ок работает, списки в podkop не трогал, свои личные настройки впн пока тоже не ставил. Но есть вот что: Кто в курсе почему ютуб лайв видео не грузит и так же на гугл плей приложения не загружает

---

**2026-02-16T17:46:18 | Леонид**
Сталкивался ли кто с проблемой в последнее время:
- у меня 4 роутера РР
- на всех без исключений - падает sing-box - podkop - dhcp
- на одном стоит фирменная оболочка + скрипт 5
- на одном стоит фирменная оболочка + Podkop
- на двух стоит ваниль + Podkop

Было все стабильно неск. месяцев. Но с ~неделю назад начались отвалы. Устройства не получают ip-адрес по wi-fi. Зависает наглухо sing-box. Перезагрузка роутера не помогает. Только ручная перезагрузка podkop / sing-box.

Уже заколебался с этой проблемой. Везде стоит 24.10.5 и последние версии ПО. И свой VLESS (с ним проблем нет).

---

**2026-02-16T18:02:53 | Routerich**
Если нужен последний Podkop то вот этот скрипт запустить
https://t.me/routerich/173678/449069

---

**2026-02-16T18:39:58 | Routerich**
Здравствуйте.
Отследить все домены на которые он обращается и добавить их в Podkop/zeroblock

---

**2026-02-16T18:48:03 | Александр**
Я правильно понимаю, что в Podkop это DISCORD - Список пользовательских доменов или я не туда смотрю?

---

**2026-02-16T19:00:20 | Routerich**
Я имею ввиду через Podkop /zeroblock в полный прокси на крайний случай.

---

**2026-02-16T20:41:34 | Владимир Д.**
У меня пока с podkop все работает, в том числе 20 летний LG.

---

**2026-02-16T20:45:58 | 𝔅𝔲𝔯𝔦k**
Как его с Podkop подружить?

---

**2026-02-16T21:31:51 | Ronso**
Добрый вечер)
Получилось скачать сам роблокс и залогиниться на сайте, однако в саму игру не заходит
Кто-нибудь сталкивался с такой проблемой?)
Использую Podkop

---

**2026-02-16T21:37:17 | Vlad Mi**
А что делать если zapret и podkop не появились после установки пакетов?

---

**2026-02-16T21:38:37 | Ronso**
Да
Юзал
Конкретно данный вариант:

Код для запуска по умолчанию с автоматической генерацией AWG WARP и установкой Podkop

sh <(wget -q -O - https://raw.githubusercontent.com/routerich/RouterichAX3000_configs/refs/heads/wdoctrack/run_universal_config.sh) 2>&1 | tee /root/run.log

---

**2026-02-16T22:28:55 | Артем Погодин**
Пришел сегодня роутер
Уже подключил, обрадовался, что ютуб работает

Но странное поведение через podkop. Подкинул туда подключение через VLESS через прокси со списком Russia inside. 

В какой-то момент Instagram работает. В какой-то очень долго загружает. Иногда до половины видео загрузил, дальше всё. С тик током тоже самое. То никуда не едет, то норм. 

И на vless Finland задержка 54ms. На Kazakhstan до 6000ms доходит почему-то. 

Помогите, как настроить и забыть 😭

---

**2026-02-16T23:21:43 | Дмитрий K.**
opkg remove podkop
opkg install podkop

---

**2026-02-16T23:23:23 | Алексей [markartr]**
Привет! подскажите пж, пытаюсь скачать podkop через mobaxterm

ловлю Connection timed out

кто-то сталкивался с такой проблемой?



root@RouteRich:~# sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/po
dkop/refs/heads/main/install.sh)
Downloading 'https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh'
Connecting to 2606:50c0:8001::154:443

Connection error: Connection timed out

---

**2026-02-17T00:46:03 | Anna Bagler**
Шлем пустить по IP в zeroblock/podkop или не работает?

---

**2026-02-17T12:11:06 | Капацина Андрей**
Добрый день. Подскажите пожалуйста. Настроил по инструкции доступ к веб морде есть удалено . Сейчас хочу подружить с podkop  также по доке. Но чет все равно доступ к сайтам нет.

---

**2026-02-17T12:40:03 | Routerich**
и дело не в Podkop, он же просто средство маршрутизации, а в методах обхода.

---

**2026-02-17T12:55:07 | Алексей**
Здравия желаю!Заранее извиняюсь за тупой вопрос.Товарищи,поясните,пожалуйста,есть-ли какой-то простой способ обновить podkop до последней версии без отката роутера до заводской прошивки и что-бы,при этом,все настройки со старой версии подкопа не сбросились?

---

**2026-02-17T12:57:35 | Роман**
https://podkop.net/docs/install/

---

**2026-02-17T13:00:04 | MMRR**
Народ, подскажите на owrt 24.10.2 сейчас warp настроить можно. Был awg1.5 + warp+ podkop. Все работало. Теперь эта связка не работает.(((

---

**2026-02-17T13:36:55 | Routerich**
Система->Автозапуск->opera-proxy->перезапустить

Службы->Podkop->из секции Main Russian inside убрать

---

**2026-02-17T15:39:03 | Anna Bagler**
podkop.net изучайте. Принципы такие.

---

**2026-02-17T15:39:15 | Routerich**
Система - автозапуск - podkop найдите и нажмите на включено и на стоп - далее перезагрузите роутер и проверьте работу интернета и скрин сеть - интерфейсы пришлите после перезагрузки

---

**2026-02-17T17:15:39 | Routerich**
На сбертв есть проблемы https://podkop.net/docs/client-dns/#sbertv

---

**2026-02-17T18:12:02 | Artur**
Анализ запущен: 2026-02-17 18:09:52
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.46 | YouTube IP:  198.18.0.24

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.21 MB
  Пинг (ya.ru via awg10): 28.593 / 35.477 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop    Youtube_Discord (vpn): youtube,discord,telegram
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.36 | RAM: 24% | NAND: 26% занято / 50.0M доступно
  13 9 * * * /usr/bin/podkop list_update

---

**2026-02-17T18:42:04 | Routerich**
Здравствуйте.
Не использовать список YouTube в Podkop, и общий список Russia inside

---

**2026-02-17T18:45:01 | Routerich**
Форкать список и размещать ссылку на него в Podkop

---

**2026-02-17T18:52:40 | Routerich**
https://podkop.net/docs/sections/#spiski-soobschestva-community-lists тут подкоп но смысл тот же, почитайте внимательно

---

**2026-02-17T19:01:02 | Jr**
Анализ запущен: 2026-02-17 18:58:20
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.64 | YouTube IP:  198.18.0.44

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓0.00 MB / ↑0.39 MB
  Пинг (ya.ru via awg10): ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (77.88.55.242): 56 data bytes
  Программы в автозапуске: podkop zapret

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОФЛАЙН
------------------------------------------------------
  curl: (28) Connection timed out after 5001 milliseconds
  Warning: Problem : timeout. Will retry in 1 seconds. 3 retries left.
  curl: (28) Connection timed out after 5001 milliseconds
  Warning: Problem : timeout. Will retry in 2 seconds. 2 retries left.
  curl: (28) Connection timed out after 5001 milliseconds
  Warning: Problem : timeout. Will retry in 4 seconds. 1 retries left.
  curl: (28) Connection timed out after 5001 milliseconds
------------------------------------------------------
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 198.18.0.44
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Пересечение между podkop и zapret:
    podkop                    : main
    zapret                    : zapret-hosts-google.txt
    Домены: googlevideo.com youtube.com 

  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai,youtube,discord,telegram
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.3.1 (Прошивка: 24.10.5)
  CPU: 0.63 | RAM: 30% | NAND: 26% занято / 49.9M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-02-17T19:23:36 | Артем Погодин**
У меня как-то не получается с кастомными URL в podkop... 

Пытаюсь добавить домены 
x-minus.pro
www.x-minus.pro

Но на сайте 1005 ошибка. Кажется, клаудфлэр не хочет меня пускать. Сам подкоп настроен так с такими списками (скрины). HODCA, как я понял, открывает все домены клауда. А через shadowsocks пытаюсь достучаться до нужных мне урлов.

Урлы прокси намеренно удалил для скринов

---

**2026-02-17T19:28:22 | Stanislav**
Анализ запущен: 2026-02-17 19:25:54
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359 127.0.0.1#5053 127.0.0.1#5054 127.0.0.1#5055 127.0.0.1#5056
  Facebook IP:  31.13.72.36 | YouTube IP:  2a00:1450:4010:c0f::5d

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓0.00 MB / ↑0.00 MB
  Пинг (ya.ru via awg10): ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (2a02:6b8::2:242): 56 data bytes
  Программы в автозапуске:

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН
  awg10 (IPv4) : ОФЛАЙН
------------------------------------------------------
  curl: (28) Connection timed out after 5002 milliseconds
  Warning: Problem : timeout. Will retry in 1 seconds. 3 retries left.
  curl: (28) Connection timed out after 5002 milliseconds
  Warning: Problem : timeout. Will retry in 2 seconds. 2 retries left.
  curl: (28) Connection timed out after 5002 milliseconds
  Warning: Problem : timeout. Will retry in 4 seconds. 1 retries left.
  curl: (28) Connection timed out after 5002 milliseconds
------------------------------------------------------
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 108.177.14.136
    Name:       youtube.com
    Address: 108.177.14.93
    Name:       youtube.com
    Address: 108.177.14.190
    Name:       youtube.com
    Address: 108.177.14.91
    Name:       youtube.com
    Address: 2a00:1450:4010:c0f::5d
    Name:       youtube.com
    Address: 2a00:1450:4010:c0f::be
    Name:       youtube.com
    Address: 2a00:1450:4010:c0f::88
    Name:       youtube.com
    Address: 2a00:1450:4010:c0f::5b
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  youtubeUnblock  | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.45 | RAM: 18% | NAND: 1% занято / 66.6M доступно
  0 4 * * * /etc/init.d/podkop list_update

---

**2026-02-17T19:33:39 | Aidar Safiullin**
Анализ запущен: 2026-02-17 19:32:32
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Collected errors:
 * opkg_download: Failed to download https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk, wget returned 4.
 * opkg_download: Check your network settings and connectivity.

 * opkg_install_pkg: Failed to download wget-ssl. Perhaps you need to run 'opkg update'?
 * opkg_install_cmd: Cannot install package wget-ssl.
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.20 | YouTube IP:  198.18.0.21

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.78 MB / ↑0.37 MB
  Пинг (ya.ru via awg10): 109.109 / 111.497 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop    Youtube_Discord (vpn): youtube,discord,telegram
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.52 | RAM: 21% | NAND: 25% занято / 50.6M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-02-17T19:58:52 | vladimir**
Приветствую Вас! Сегодня получил еще два замечательных роутера!15 минут и оба отправились отцу и тестю в семью, поскольку те, заинтересовавшись открывающимися перед ними возможностями теперь станут выносить мозг нашей любимой техподдержке 🤗🤗🤗😂😂😂Клянусь-своими силами не допускать подобных безобразий и решать возможные возникающие проблемы своими силами, путем курения мануалов(Курение убивает😂😂😂)Ну а уж если и придется обратиться не откажите в любезности направьте в ZeroBlock или Zapret 2😂😂😂p.s("шепотом" правда моим отцам и podkop'a за глаза хватает👍👍👍)

---

**2026-02-17T20:23:14 | Артем Погодин**
Запустил "с автоматической генерацией AWG WARP и установкой Podkop"

Вроде всё заработало
А если захочу через свой vless пустить или докинуть кастомных ip, добавлять отдельную секцию через это?

---

**2026-02-18T01:13:31 | Routerich**
У вас проблема не в драйвере wifi, а в настройках singbox/текущем vless конфиге
Это в другой топик

Ваш Huawei P30 Pro получил IP локальной сети, проверка соединения Android выдала неверный результат из-за сломанного Podkop/Sing-box/Vless сервера

---

**2026-02-18T10:11:00 | Routerich**
Здравствуйте
пускайте их тогда в Podkop/zeroblock

---

**2026-02-18T11:15:50 | Роман**
Дополнительные домены и ip для WhatsApp и Telegram - добавлять в список пользовательских доменов/ip в zeroblock/podkop.

#WhatsApp

IP
31.13.64.0/18
57.141.0.0/20
57.144.0.0/14
66.220.144.0/20
69.63.160.0/19
69.171.192.0/18
74.119.76.0/22
129.134.0.0/17
157.240.0.0/16
163.64.0.0/12
173.252.64.0/18
185.60.216.0/22
204.15.20.0/22


domain
bintray.com
whatsapp.biz
whatsapp.com
whatsapp.net
wa.me


#Telegram

IP
91.108.4.0/22
91.108.8.0/22
91.108.16.0/22
91.108.12.0/22
149.154.160.0/20
91.105.192.0/23
91.108.20.0/22
185.76.151.0/24

domain
t.me
telegram.me
telegram.dog
telegra.ph
telesco.pe
telegramdesktop.com
tdesktop.com
fragment.com
cdn-telegram.org
comments.app
contest.com
graph.org
quiz.directory
telegram-cdn.org
telegram.space
tg.dev
tx.me
usercontent.dev
by Vasa


Так-же можно попробовать добавить автоматически обновляемые списки:
domain
https://raw.githubusercontent.com/KharunDima/whatsapp-lists/main/results/domains.txt

IP
https://raw.githubusercontent.com/KharunDima/whatsapp-lists/main/results/cidr_ipv4.txt

Добавлять в пользовательские списки zeroblock/podkop - вставлять сами ссылки.

Так-же помогает скачать клиент WhatsApp с официального сайта, а не с PlayMarket (не забываем про бэкапы переписок, привязку почты для входа).

---

**2026-02-18T12:06:50 | IVANZZZ**
Анализ запущен: 2026-02-18 11:44:20
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.6 | YouTube IP:  198.18.0.7

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.68 MB / ↑0.16 MB
  Пинг (ya.ru via awg10): Ожидайте, идет замер (10 пакетов)...
  Пинг (ya.ru via awg10): 35.307 / 37.427 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 204) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop    Youtube_Discord (vpn): youtube,discord,telegram
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.14

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.15 | RAM: 21% | NAND: 26% занято / 49.4M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-02-18T12:14:33 | Routerich**
найти домены куда оборудование обращается и добавлять в Podkop/zeroblock в пользовательские домены

---

**2026-02-18T12:15:14 | Routerich**
да как вам угодно, можете потом проверить перекинув обратно или переходите на Zapret2 удалив из Podkop список youtube

---

**2026-02-18T12:22:02 | Routerich**
логи Podkop покажите

---

**2026-02-18T12:26:06 | Routerich**
галочку в настройках Podkop поставить/убрать на скачивание списков через Proxy

---

**2026-02-18T13:27:47 | Routerich**
Здравствуйте.
https://podkop.net/docs/sections/

---

**2026-02-18T14:09:53 | Routerich**
Здравствуйте.
проще пустить полностью в Podkop устройство, на котором играете.

---

**2026-02-18T15:03:39 | Routerich**
Службы->Podkop->

---

**2026-02-18T15:08:12 | Egor**
У подкопа есть инструкция https://podkop.net/docs/tunnels/awg_settings/

---

**2026-02-18T15:34:02 | Роман**
Не зная терминов не следует интересоваться openwrt вообще. Коротко zeroblock лучше. Длиннее расписывать нет смысла т.к вы не знаете терминов. Вам ответит любой в этом чате zeroblock лучше, а в чате itdoga скажут что podkop лучше. Вот и думайте.

---

**2026-02-18T17:27:09 | .**
Всем привет!) 
Друзья, подскажите пожалуйста, ZeroBlock и Podkop, в целом имеют равное назначение? Кто что юзает? 
Вкратце скажите, что будет попроще для освоения?
Podkop так понимаю чуть попроще, а ZeroBlock более жирный в плане функционала?

---

**2026-02-18T19:27:55 | Petr Shcherbinin**
добрый день
иногда перестают открываться все сайты, работает через 5 скрипт с подкопом, делаю на вкладке http://routerich.lan/cgi-bin/luci/admin/services/podkop Restart podkop - тут же отпускает

при этом до рестарта View log не работает - видимо микросервис умирает

можно как-то сделать ему кронджоб на рестарт каждые 5 минут?

---

**2026-02-18T19:47:31 | Routerich**
Здравствуйте.
В бета теме есть скрипт с актуальной версией Podkop

---

**2026-02-18T19:49:41 | Anna Bagler**
0 4  * * * /etc/init.d/podkop restart или ... service podkop restart в планировщике.

---

**2026-02-18T19:50:46 | Максим Бычков**
Ставить podkop можешь по ключевым словам поискать для себя решения

---

**2026-02-18T21:26:21 | Леонид**
Подскажите, как весь траф прокинуть через VPN в Podkop? При добавлении сюда подсети - инета нет.

---

**2026-02-18T21:31:17 | Anna Bagler**
Все может быть, это средство точечной маршрутизации. Изучайте podkop.net.

---

**2026-02-18T22:00:25 | Руслан**
Приветствую! Подскажите пожалуйста, хочу понять направление, в какую сторону двигаться и что изучить, получил сегодня роутер Routerich ax3000 и хочу настроить так, чтобы Дискорд, Ютуб и всё остальное работало, что для этого нужно? Zapret2 или zeroblock или podkop или что-то ещё?

---

**2026-02-18T22:13:35 | Роман**
Поиск доменов и ip:
IPV4OO
Хром - https://chromewebstore.google.com/detail/ipvfoo/ecanpcehffngcegjmadlcijfolapggal?hl=kk
Лиса - https://addons.mozilla.org/ru/firefox/addon/ipvfoo/
Включаем ВПН -> идём на сайт -> копируем домены в zeroblock/podkop.

Браузер
https://www.youtube.com/watch?v=rtXTaClSXR0
Андройд
https://www.youtube.com/watch?v=h7OUgOrezdQ
iOS
https://www.youtube.com/watch?v=-ePERMmabDA
Винда
https://www.youtube.com/watch?v=eIrD5XvDTto
Линукс
https://www.youtube.com/watch?v=TXAayoJ-vpY

---

**2026-02-18T22:25:00 | Anna Bagler**
Тогда мастер настройки, скрипт 5 и изучать материал на podkop.net.

---

**2026-02-18T22:37:36 | Routerich**
Генерируете конфиг в интернете в конфигураторе warp. Далее создаёте интерфейс и добавляете в подкоп или зероблок https://podkop.net/docs/tunnels/awg_settings/ пункт установки пакетов пропустить

---

**2026-02-18T23:07:43 | Routerich**
https://podkop.net/docs/workvpn/

---

**2026-02-19T00:52:12 | Andrew**
Через podkop почему-то вообще впн не хочет работать, хотя вставляю ключ в v2raytun, и все пашет. В чем может быть проблема?

---

**2026-02-19T07:01:18 | Routerich**
@wanderlust178, а диагностика Podkop что показывает? что в логах?
и какой ключ? можете его отправить, без чувствительных данных.

---

**2026-02-19T07:51:28 | Routerich**
Zeroblock, Podkop

---

**2026-02-19T08:22:31 | Routerich**
Здравствуйте.
как и в Podkop, надо сетевой интерфейс TailScale добавлять в "Сетевой интерфейс источника"

---

**2026-02-19T08:30:47 | Павел Четвертков**
А что сейчас самое устойчивое к блокировкам? Вот вижу в podkop есть trojan, hysteria2, socks 4 5. Их в деле еще не пробовал

Ну и по амнезии что скажете?

---

**2026-02-19T08:49:45 | Routerich**
Ну конечно, так не будет работать.
Так как это средство точечной маршрутизации маршрутизации, а вам нужно либо искать домены куда обращаются сайты не рабочие либо полностью устройство в Podkop пускать.

---

**2026-02-19T10:39:52 | Routerich**
Здравствуйте.
Службы->Podkop

---

**2026-02-19T12:23:28 | Routerich**
Службы->Podkop->Настройки->измените DNS провайдера на AdGuard

---

**2026-02-19T12:25:18 | Klmnt**
Всем привет.

✘ DOH (dns.adguard-dns.com) unavailable не подключается-не доступен около 3 часов в podkop

Детали:
Наш роутер подключён к провайдерскому
Провайдер МТС

Информация о версии
Podkop: v0.6.2
LuCI App: v0.6.2
Sing-box: 1.12.4
OpenWrt Version: RouteRich 24.10.4 r28959-29397011cc RR-3.8.2
Device Model: Routerich AX3000 v1


Куда копать ?
Что можно сделать?

---

**2026-02-19T12:26:27 | DG**
грохнуть установленный sing-box  и установить sing-box tiny, podkop с ним тоже будет работать

---

**2026-02-19T14:53:30 | Viza**
Добрый день !
Помогите установить podkop,ошибки вот-такие вылетают

---

**2026-02-19T15:04:43 | ALEKSANDR DJ**
Podkop Error
Thu Feb 19 11:47:57 2026 user.notice podkop: [error] Outbound section not found. Please check your configuration file (missing proxy_string, selector_proxy_links, urltest_proxy_links, outbound_json, or interface). Aborted.

---

**2026-02-19T15:31:19 | ALEKSANDR DJ**
view_logs 
 Thu Feb 19 11:47:55 2026 user.notice podkop: [info] Starting podkop
Thu Feb 19 11:47:55 2026 user.notice podkop: [info] Check Requirements
Thu Feb 19 11:47:57 2026 user.notice podkop: [error] Outbound section not found. Please check your configuration file (missing proxy_string, selector_proxy_links, urltest_proxy_links, outbound_json, or interface). Aborted.

---

**2026-02-19T15:49:13 | Роман**
https://telegra.ph/Polnaya-instrukciya-nastrojki-xHTTP-v-Podkop-12-08

---

**2026-02-19T15:52:46 | Роман**
https://podkop.net/
Где-то там есть список.

---

**2026-02-19T16:39:01 | ALEKSANDR DJ**
view_logs 
 Thu Feb 19 13:30:37 2026 user.notice podkop: [info] Starting podkop
Thu Feb 19 13:30:37 2026 user.notice podkop: [info] Check Requirements
Thu Feb 19 13:30:39 2026 user.notice podkop: [error] Outbound section not found. Please check your configuration file (missing proxy_string, selector_proxy_links, urltest_proxy_links, outbound_json, or interface). Aborted.

---

**2026-02-19T17:32:42 | Григорий Нестеренко**
Добрый день, всем! Установлена версия 24.10.4, скрипт 5, vpn - wire guard свой. Все что нужно работает, но вот whatsapp сообщения не приходят, отключаю wifi, переключаюсь на 4g и сообщения приходят. Настроен podkop, в основных настройках указан список meta. Пробовал убирать, все равно сообщения не приходят. Подскажите, что ещё испробовать?

---

**2026-02-19T17:43:17 | Роман**
Дополнительные домены и ip для WhatsApp и Telegram - добавлять в список пользовательских доменов/ip в zeroblock/podkop.

#WhatsApp

IP
31.13.64.0/18
57.141.0.0/20
57.144.0.0/14
66.220.144.0/20
69.63.160.0/19
69.171.192.0/18
74.119.76.0/22
129.134.0.0/17
157.240.0.0/16
163.64.0.0/12
173.252.64.0/18
185.60.216.0/22
204.15.20.0/22
3.0.0.0/10


domain
bintray.com
whatsapp.biz
whatsapp.com
whatsapp.net
wa.me
whatsapp-plus.info
whatsapp-plus.me
whatsapp-plus.net
whatsapp.cc
whatsapp.info
whatsapp.org
whatsapp.tv
whatsappbrand.com


#Telegram

IP
91.108.4.0/22
91.108.8.0/22
91.108.16.0/22
91.108.12.0/22
149.154.160.0/20
91.105.192.0/23
91.108.20.0/22
185.76.151.0/24

domain
t.me
telegram.me
telegram.dog
telegra.ph
telesco.pe
telegramdesktop.com
tdesktop.com
fragment.com
cdn-telegram.org
comments.app
contest.com
graph.org
quiz.directory
telegram-cdn.org
telegram.space
tg.dev
tx.me
usercontent.dev
by Vasa


Так-же можно попробовать добавить автоматически обновляемые списки:
domain
https://raw.githubusercontent.com/KharunDima/whatsapp-lists/main/results/domains.txt

IP
https://raw.githubusercontent.com/KharunDima/whatsapp-lists/main/results/cidr_ipv4.txt

Добавлять в пользовательские списки zeroblock/podkop - вставлять сами ссылки.

Так-же помогает скачать клиент WhatsApp с официального сайта, а не с PlayMarket (не забываем про бэкапы переписок, привязку почты для входа).

---

**2026-02-19T17:43:49 | Roman**
первое — просто podkop (скрипт 5), второе — Happ на компе

---

**2026-02-19T20:35:59 | Anna Bagler**
Перезапустите opera-proxy и сам podkop. Вообще он стар, как и прошивка.

---

**2026-02-19T20:39:07 | Данила**
На роутериче предустановлен podkop? Я хочу подключить через него vless конфиг и настроить впн маршрутизацию

---

**2026-02-19T20:48:53 | Anna Bagler**
https://podkop.net/docs/workvpn/

---

**2026-02-19T21:12:53 | Routerich**
Здравствуйте.
А чем пользуетесь на роутере? Podkop, zeroblock имеется?

---

**2026-02-19T22:20:31 | Anna Bagler**
Так же как и в podkop. podkop.net Секции.

---

**2026-02-19T22:47:58 | che**
Ребята. Openconnect на работает в работающим zeroblock или podkop. Предполагаю что как то связано с dns. Выключаю zb и доступ в интернет появляется. Как поправить настройку?

---

**2026-02-19T23:11:16 | Andrew**
Ключ:

vless://*****:52340?type=xhttp&encryption=none&path=%2F&host=&mode=auto&security=reality&pbk=*****&fp=chrome&sni=sun6-20.userapi.com&sid=89&spx=*****

Диагностика:

Полные результаты диагностики


Checking GitHub connectivity
────────────────────────────
► Checking GitHub connectivity...
GitHub is accessible
Checking lists availability:
- inside-dnsmasq-nfset.lst: ✓
- outside-dnsmasq-nfset.lst: ✓
- inside-dnsmasq-nfset.lst: ✓
- youtube.lst: ✓
- Twitter.lst: ✓
- Meta.lst: ✓
- Discord.lst: ✓


Checking proxy settings
───────────────────────
► Checking sing-box configuration...
{
  "log": {
    "level": "warn"
  },
  "inbounds": [
    {
      "type": "tproxy",
      "listen": "::",
      "listen_port": 1602,
      "sniff": false
    }
  ],
  "outbounds": [
    {
      "type": "vless",
      "server": "MASKED",
      "server_port": 52340,
      "uuid": "MASKED",
      "packet_encoding": "",
      "domain_strategy": "",
      "tls": {
        "enabled": true,
        "server_name": "MASKED",
        "utls": {
          "enabled": true,
          "fingerprint": "chrome"
        },
        "insecure": false,
        "reality": {
          "enabled": true,
          "public_key": "MASKED",
          "short_id": "MASKED"
        }
      }
    }
  ],
  "route": {
    "auto_detect_interface": true
  }
}
► Checking proxy connection...
Proxy check completed successfully


Checking NFT rules
──────────────────
► Checking PodkopTable rules...
Sets statistics:
- podkop_domains: 7 elements
- podkop_subnets: ✗
- podkop2_domains: ✗
- podkop2_subnets: ✗
- localv4: ✗
Current chains and rules:
 chain mangle {
  iifname "br-lan" ip daddr @podkop_domains meta l4proto tcp meta mark set 0x00000105 counter packets 300 bytes 109374
  iifname "br-lan" ip daddr @podkop_domains meta l4proto udp meta mark set 0x00000105 counter packets 6 bytes 7668
 chain proxy {
  meta mark 0x00000105 meta l4proto tcp tproxy ip to :1602 counter packets 300 bytes 109374
  meta mark 0x00000105 meta l4proto udp tproxy ip to :1602 counter packets 6 bytes 7668
NFT check completed

Full diagnostic check completed


Логи:

Showing podkop logs from system journal...
Thu Feb 19 23:06:26 2026 user.notice podkop: 2026-02-19 23:06:26 Stopping the podkop
Thu Feb 19 23:06:26 2026 user.notice podkop: 2026-02-19 23:06:26 The cron job removed
Thu Feb 19 23:06:26 2026 user.notice podkop: 2026-02-19 23:06:26 Flush nft
Thu Feb 19 23:06:26 2026 user.notice podkop: 2026-02-19 23:06:26 Flush ip rule
Thu Feb 19 23:06:26 2026 user.notice podkop: 2026-02-19 23:06:26 Flush ip route
Thu Feb 19 23:06:26 2026 user.notice podkop: 2026-02-19 23:06:26 Stop sing-box
Thu Feb 19 23:06:26 2026 user.notice podkop: 2026-02-19 23:06:26 Start podkop
Thu Feb 19 23:06:26 2026 user.notice podkop: 2026-02-19 23:06:26 Create marking rule
Thu Feb 19 23:06:26 2026 user.notice podkop: 2026-02-19 23:06:26 Proxy mode
Thu Feb 19 23:06:26 2026 user.notice podkop: 2026-02-19 23:06:26 Added route for tproxy
Thu Feb 19 23:06:26 2026 user.notice podkop: 2026-02-19 23:06:26 Sing-box UCI config OK
Thu Feb 19 23:06:27 2026 user.notice podkop: 2026-02-19 23:06:27 Adding a common domains list
Thu Feb 19 23:06:27 2026 user.notice podkop: 2026-02-19 23:06:27 Create set podkop_domains
Thu Feb 19 23:06:27 2026 user.notice podkop: 2026-02-19 23:06:27 Added nft rule tproxy
Thu Feb 19 23:06:31 2026 user.notice podkop: 2026-02-19 23:06:30 The cron job removed
Thu Feb 19 23:06:31 2026 user.notice podkop: 2026-02-19 23:06:31 The cron job has been created: 0 4 * * * /etc/init.d/podkop list_update
Thu Feb 19 23:06:31 2026 user.notice podkop: 2026-02-19 23:06:31 service_triggers start

---

**2026-02-19T23:34:24 | А. Ч.**
Парни у меня 
Версия встроенного ПО:  RouteRich 24.10.2 r28739-d9340319c6 RR-3.6.6 / LuCI openwrt-24.10 branch 25.250.61039~923f8d9, 
Podkop: v0.4.11-r1 Sing-box: 1.11.15, 
если я просто запущу скрипт № 5 у меня Podkop обновиться? или мне нужно обновлять прошивку роутера полностью?

---

**2026-02-20T11:34:00 | Kirill Y**
Здравствуйте! Напомните пожалуйста, куда именно в podkop прописывать ip?

---

**2026-02-20T12:06:33 | Konstantin Uk**
Добрый день,
Переустановил последнюю версию на заводские настройки и последний скрипт (Podkop v0.7.14)
Все настройки дефолтные, кроме списка пользовательских доменов.

Не работает часть всяких мелких сервисов, в основном связанных с github, всякие разные репозитории, линукс библиотечки и прочее.
Если добавить Cloudflare в списки или Proxy или VPN - они начинают работать, но отваливаются всякие телеграммы и youtube
Не совсем понимаю, какие логи тут могут помочь (если вдруг проблема не известная)

---

**2026-02-20T12:14:57 | Anna Bagler**
podkop.net и списки доменов по категориям у itdog. С какой стороны блок идёт смотрите и с каким IP вашa awg на выходе.

---

**2026-02-20T12:46:03 | Routerich**
Здравствуйте
На все ваши вопросы тут есть ответы
https://podkop.net/

---

**2026-02-20T14:28:24 | Routerich**
попробуйте Podkop остановить и проверить

---

**2026-02-20T17:58:42 | Aidar Safiullin**
Подскажите, пожалуйста, какая версия podkop сейчас актуальная? 
И как её можно обновить?

---

**2026-02-20T18:01:46 | Роман**
Скриптом с podkop.net можно обновить.

---

**2026-02-20T18:08:22 | Aidar Safiullin**
Обновил через скрипт 
Но все равно отображает, что podkop версия устаревшая 
Или это норма?

---

**2026-02-20T18:18:59 | Роман**
Ситема - пакеты - обновить списки - фильтр podkop, установить/обновить 3 пакета.

---

**2026-02-20T19:53:16 | Eugene Esingildinov**
Добрый вечер, поступился принципом "работает - не трожь", обновился до актуальной версии прошивки и поставил zeroblock
Списки кажется те же, что были до обновления в подкопе, но нет доступа к ресурсам.
Проверки вот такое выдают. Подскажите, пожалуйста, в какую сторону смотреть?


= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  31.13.72.36 | YouTube IP:  64.233.165.91

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓0.00 MB / ↑0.44 MB
  Пинг (ya.ru via awg10): ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (5.255.255.242): 56 data bytes
  Программы в автозапуске: zeroblock zapret2

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОФЛАЙН
------------------------------------------------------
  curl: (28) Connection timed out after 5001 milliseconds
  Warning: Problem : timeout. Will retry in 1 seconds. 3 retries left.
  curl: (28) Connection timed out after 5001 milliseconds
  Warning: Problem : timeout. Will retry in 2 seconds. 2 retries left.
  curl: (28) Connection timed out after 5001 milliseconds
  Warning: Problem : timeout. Will retry in 4 seconds. 1 retries left.
  curl: (28) Connection timed out after 5001 milliseconds
------------------------------------------------------
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 64.233.165.136
    Name:       youtube.com
    Address: 64.233.165.91
    Name:       youtube.com
    Address: 64.233.165.93
    Name:       youtube.com
    Address: 64.233.165.190
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock              awg10 (vpn): !_russia_inside,news,anime,discord,meta,twitter,hdrezka,tiktok,telegram,!_cloudflare,google_ai,google_play
  zeroblock          opera (prx out): geoblock,block
  Версия zeroblock: 0.6.4-r8
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.38 | RAM: 25% | NAND: 50% занято / 33.6M доступно
  13 9 * * * /usr/bin/podkop list_update
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-02-20T20:13:17 | Routerich**
Аналогично делается и для Zeroblock
https://podkop.net/docs/faq/#gostevaya-wi-fi-set-i-podkop

---

**2026-02-20T20:24:53 | Anna Bagler**
Перезапустить opera-proxy и сам podkop в Система - Автозапуск. Подождать.
Домены могут быть не все.
Диагностику подкопа не мешало бы посмотреть.

---

**2026-02-20T20:46:34 | Anton Kadochnikov**
Всем привет. Сегодня получил новенький роутер и решил с ним позаниматься. Первичные настройки, в том числе wifi. Домашние устройства подцепились. Пока ковырялся с пакетами (podkop, zapret) заметил, что отключился iphone. Android работает, а этот нет. Из настроек wifi установил канал автомат и шифрование WPA2/WPA3. Если поставить только WPA2, то всё работает. Пробовал сбрасывать и не помогает. Если поставить ax3000t, то с такими же настройками проблем нет. Кто сталкивался с похожим?

---

**2026-02-20T23:01:24 | Anna Bagler**
Подкоп - Секции. podkop.net Секции. Изучайте.

---

**2026-02-21T11:49:11 | Anna Bagler**
В секцию, в которой есть список meta, например. podkop.net Секции, изучайте, пользовательские домены и подсети.

---

**2026-02-21T12:02:03 | Sergey**
Добрый день, уважаемые.

Нужен ваш совет, куда копать и что можно поднастроить, чтобы система заработала корректно.

Настраиваю очередной роутер на RouteRich 24.10.5 и столкнулся с неприятным поведением: Podkop и Tailscale не работают одновременно. Судя по всему, Tailscale при запуске добавляет свои правила маркировки трафика, которые конфликтуют с Podkop.

Podkop обновлён до актуальной версии.

На данном устройстве очень важно иметь и Podkop, и стабильный удалённый доступ.

Сейчас Tailscale отключён — в этом случае Podkop работает штатно.

Удалённый доступ временно организовал через ZeroTier, но он то работает, то нет, похоже, что трафик местами блочится.

Если включить Tailscale, Podkop сразу перестаёт функционировать.
В диагностике Podkop появляется предупреждение «Другие правила маркировки», а проверка
curl -v https://fakeip.podkop.fyi/check — зависает и не проходит.

На предыдущей прошивке RouteRich 24.10.4 с прошлой версией Tailscale таких проблем не было — всё работало корректно.

Буду благодарен за совет, в какую сторону двигаться и как можно подружить Podkop + Tailscale на новой прошивке RouteRich 24.10.5

Спасибо.

---

**2026-02-21T12:32:02 | Роман**
Ищите откуда игра тянет моды, прописывайте домены и ip в zeroblock/podkop.

---

**2026-02-21T12:45:27 | Роман**
Добавить домены и ip телеги в zeroblock/podkop, выбрать в списках сообщества телеграмм.

---

**2026-02-21T15:06:48 | Routerich**
https://podkop.net/docs/tunnels/wg_settings/ проверяйте что всё сделали правильно

---

**2026-02-21T18:15:10 | Сущенко Валерий**
Здравствуйте! "Новичок". У меня не открывается Личный кабинет Триколор (не на Компе не на Смарте). А когда переключаю Смарт на Мобильный интернет,  то в ЛК Ростелекома вхожу. В PodKop в Service List  у меня Russiy  не выбрана. Подскажите в чем проблема? Или от Роутерича это не зависит.

---

**2026-02-21T18:16:29 | Routerich**
Здравствуйте.
Попробуйте отключить Podkop, Zapret и проверить

---

**2026-02-21T18:57:51 | Николай Шахматный BogdanovNikolay**
При диагностике podkop, пишет что YouTube_discord не отвечает

---

**2026-02-21T19:42:52 | Anna Bagler**
Изучайте podkop.net Секции для начала.

---

**2026-02-21T20:00:15 | Илья**
Добрый вечер,могу ли я настроить vpn по этому способу ?
https://redshieldvpn.org/ru/help/vpn_on_routers/openwrt_routers/amneziawg2_openwrt_podkop

---

**2026-02-21T22:12:47 | Роман**
Добавить домены сервера в zeroblock/podkop.

---

**2026-02-21T22:31:52 | Евгений Горбунов**
Устаревший Podkop критично?

---

**2026-02-21T22:33:24 | Routerich**
Это бесплатаные общедоступные варианта прокси и warp +  установка пакета podkop, для нормальной работы требуется произвести действия по ссылке, они применимы и без 5 скрипта для нормальной работы сервисов через впн ваш

---

**2026-02-21T22:34:37 | Илья**
Добрый вечер как прописать chatgpt в podkop?

---

**2026-02-21T22:36:33 | Mitya Zhuravlev**
Понятно, спасибо. а где найти информацию как эти варианты прокси и warp, podkop устанавливать?

---

**2026-02-21T22:42:41 | Артём**
Спасибо, попробую! 

А не подскажите, что сделать, чтобы робот-пылесос европейский смог подключиться к серверу dreame.tech?
Пробовал прописывать сервер в разделы podkop, но так и не смог подключить робот. 
Может что-то неверно делаю?

---

**2026-02-21T23:22:24 | Anna Bagler**
youtubeUnblock может не помочь. Вам нужен zeroblock/podkop как средство точечного обхода.
На роутере есть URL-loger.

---

**2026-02-22T02:37:54 | ;)**
Всем привет обновил Podkop и теперь он показывает вот это

---

**2026-02-22T03:08:09 | Заур**
здраствуйте! был podkop + singbox на ax3000, потом когда ковырлся - все испорти и решил сбросить до заводских. в итоге теперь не могу подкоп установить тк на прошивке 23.05.5 он не хочет устаналиваться. просто хотел поставить на роутер конфиг vless. как быть?

---

**2026-02-22T03:12:21 | Routerich**
Либо обновлять прошивку, либо ставить версию 0.2.5 https://github.com/CodeRoK7/podkop-v0.2.5

---

**2026-02-22T03:33:46 | Заур**
установил подкоп командой "sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)" но в списке служб почему-то не появился (страницу обновлял - не помогло)

---

**2026-02-22T06:27:10 | STIG**
Здравствуйте. Нужна помощь. Купил ключ impVPN для роутера (выбрал вариант hysteria2). В инструкции к vpn указано что необходимо перейти в Services -> Podkop. Зашел в настройки роутера и не могу найти данный раздел. Куда прописывать ключ от vpn?

---

**2026-02-22T06:36:48 | STIG**
Роутер с "коробки". Еще ничего не настраивал и не устанавливал. Первые шаги. Возможно и сам бы разобрался, но не могу найти инструкцию. Нужен ли vpn или есть возможность обойти блокировки сайтов путем установки только podkop?

---

**2026-02-22T07:50:29 | STIG**
Благодарю. Установил скрипт №5. Установился podkop. Добавил строки которые мне прислали impVPN. Все еще не работают сайты (к примеру youtube). Что я делаю не так?

---

**2026-02-22T08:14:21 | Routerich**
Если у вас Hysteria то нужно обновить Podkop, через бета скрипт если что.

---

**2026-02-22T08:25:55 | STIG**
После подключения роутера (без настроек "из коробки"), на смартфоне, через wi-fi, медленно но работали приложения (рассказываю на примере youtube). Без использования vpn. На ПК в браузере youtube не открывался. Сейчас установил Скрипт №5. Также добавил ключ от vpn. Все еще не работает ни на одном устройстве. В настройках смартфона и в браузере ПК выключил использование DNS. На смартфоне youtube запускается только при включении отдельного vpn (на этом устройстве). В настройках роутера перезапустил podkop - не помогло. После прочтения в разделе wiki скрипт № 5, насколько я понял, и так должен был открыть доступ, даже без VPN, я правильно понимаю? В приложении hiddify не проверял.

---

**2026-02-22T08:46:25 | Роман**
Hysteria 2 доступна в подкопе с версии 0.7.14 если мне память не изменяет. Обновить можно запустив либо бета версию скрипта, либо скрипт с  podkop.net.

---

**2026-02-22T08:55:39 | Routerich**
На роутере нет никакого vpn, он ставится как раз скриптом, но это бесплатные решения, так что вполне возможны с ними проблемы.
Вставляйте свой ключ в Podkop

---

**2026-02-22T10:26:10 | Anna Bagler**
Каналы земля и сотовый - разные, ничего удивительного, что на мобильном может открываться, т.к. другие правила блокировки могут быть. Отключите podkop или что ставили для обхода, проверьте хдрезку. Если нормально, включите назад и уберите ее список просто.

---

**2026-02-22T10:40:51 | STIG**
Сбросил настройки роутера до заводских. Пожалйста, проведите меня по всем пунктам, так скажем "за ручку". Первые шаги, что мне делать? Сейчас, без VPN смартфон через wi-fi, прекрасно заходит в приложение youtube (другие сайты будем пробовать уже в процессе дальнейшей настройки). С ПК на сайт youtube не заходит. Мне нужно установить podkop? Скидывали несколько скриптов. Какой нужно устанавливать в терминале? Бету или №5?

---

**2026-02-22T11:37:09 | Routerich**
Здравствуйте.
https://redshieldvpn.org/ru/help/vpn_on_routers/openwrt_routers/amneziawg2_openwrt_podkop

---

**2026-02-22T11:55:27 | 🇧 🇧**
Тоже с этим столкнулся. Причем если включаю списки V1 (от Podkop), с телеграм проблем нет. Наблюдается только если выбрать V2 🤷

---

**2026-02-22T13:10:05 | Сущенко Валерий**
Все сделал с 5 скриптом по написанному. Сейчас в Терминале внизу вот такая конечная запись: .......Start and enable service 'doh-proxy'...
Service Podkop and Sing-Box restart...
Start podkop
service_triggers start
ByPass block for Method 2: AWG WARP + Opera Proxy...Configured completed...
After 10 second AUTOREBOOT ROUTER...
root@RouteRich:~# . Теперь дальше ENtar  нажимать и все. Спасибо.

---

**2026-02-22T13:11:48 | Сущенко Валерий**
Сущенко Валерий, [22.02.2026 13:10]
Все сделал с 5 скриптом по написанному. Сейчас в Терминале внизу вот такая конечная запись: .......Start and enable service 'doh-proxy'...
Service Podkop and Sing-Box restart...
Start podkop
service_triggers start
ByPass block for Method 2: AWG WARP + Opera Proxy...Configured completed...
After 10 second AUTOREBOOT ROUTER...
root@RouteRich:~# . Теперь дальше ENtar  нажимать и все.

---

**2026-02-22T13:21:50 | Andrey**
Ребята подскажите, что-то я запутался. Стоит podkop + vless, остальное все удалил. Какая-то беда с dns походу. Интернет есть, впн есть, но трафик от устройств в сети не идет туда. Включен doh. Прочитал чат, поставил в dns и dhcp forwards 127.0.0.1#5359 стало что-то грузить (карточки видео в ютубе например, но видео и картинки - нет).

---

**2026-02-22T13:26:04 | Anna Bagler**
podkop? Список meta в какой секции, в другую пробовали переносить?

---

**2026-02-22T14:17:19 | Nikolay**
Подскажите, если пользуюсь Tailscale, то в zero block/podkop добавлять его в сетевой интерфейс?

---

**2026-02-22T14:28:20 | Игорь М**
Здравствуйте подскажите как установить podkop?

---

**2026-02-22T14:42:38 | Илья**
Добрый день,установлен podkop,zapret отключен ,в списке установлен russian inside , YouTube работает на телефоне и ноуте,на телевизоре (Samsung) не работает, подскажите куда копать?

---

**2026-02-22T16:01:10 | Белозеров В.А.**
Анализ запущен: 2026-02-22 15:59:49
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.60 | YouTube IP:  64.233.164.190

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.99 MB / ↑0.48 MB
  Пинг (ya.ru via awg10): 86.507 / 92.514 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop zapret

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop            Discord (vpn): discord,telegram
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.2.1 (Прошивка: 24.10.5)
  CPU: 0.23 | RAM: 24% | NAND: 28% занято / 48.7M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-02-22T16:41:28 | Kirill ☕️**
Подскажтие, пож, что означает ошибка?
user.notice podkop: [error] Detected https-dns-proxy in DHCP config. Edit /etc/config/dhcp

---

**2026-02-22T17:54:45 | Routerich**
Здравствуйте

В Podkop/zeroblock в зависимости от того, что используете.

---

**2026-02-22T17:59:16 | Anton**
А что советуете использовать podkop или zeroblock? Роутер только получил, настроил запрет. Но для нескольких ресурсов (git, intellij, chatgpt, Claude code) хочу настроить через впн. Ключ vless уже имеется - до покупки роутера юзал квн на пк под весь трафик

---

**2026-02-22T18:44:19 | Routerich**
Отследите домены на которые он обращаются через PCApdroid, если эти приложения для телефона и добавьте их в Podkop

---

**2026-02-22T20:11:26 | Routerich**
Павел ну так Podkop настроить надо же
если своего ничего нет то запускайте это
https://t.me/routerich/3845/245550
скрипт сам всё сделает

---

**2026-02-22T21:13:57 | Ринат Абдрахманов**
Можно ли обновить Podkop? Интересует наличие сообщества ROBLOX.

---

**2026-02-22T22:12:33 | Chao Kakao**
В общем секция в podkop у меня выглядит следующим образом:

Список пользовательских доменов:
whatsapp.com
whatsapp.net
whatsapp.biz
wa.me
graph.facebook.com
bintray.com
whatsapp-plus.info
whatsapp-plus.me
whatsapp-plus.net
whatsapp.cc
whatsapp.info
whatsapp.org
whatsapp.tv
whatsappbrand.com

Список пользовательских подсетей:
31.13.24.0/21
31.13.64.0/18
57.141.0.0/20
57.144.0.0/14
66.220.144.0/20
69.63.160.0/19
69.171.192.0/18
74.119.76.0/22
129.134.0.0/17
157.240.0.0/16
163.64.0.0/12
173.252.64.0/18
185.60.216.0/22
204.15.20.0/22
3.0.0.0/10

Внешние списки доменов:
https://raw.githubusercontent.com/KharunDima/whatsapp-lists/main/results/domains.txt
https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_domainlist.txt

Внешние списки подсетей:
https://raw.githubusercontent.com/KharunDima/whatsapp-lists/main/results/cidr_ipv4.txt
https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_cidr_ipv4.txt

И всё равно не работает 😩

---

**2026-02-22T23:41:09 | Vitaly**
Ребят, помогите!
Ковырялся в Podkop, сменил тип подключения с Proxy на VPN, потом обратно и все слетело, даже скрин не сделал.

Каккой тип конфигурации стоял по умолчанию и в поле "Конфигурация исходящего соединения" какой скрипт был? 

Скиньте кто-нибудь

---

**2026-02-22T23:41:56 | Vitaly**
Ребят, помогите!
Ковырялся в Podkop, сменил тип подключения с Proxy на VPN, потом обратно и все слетело, даже скрин не сделал.

Каккой тип конфигурации стоял по умолчанию и в поле "Конфигурация исходящего соединения" какой скрипт был? 

Скиньте кто-нибудь

---

**2026-02-23T06:09:58 | Routerich**
Здравствуйте.
Внешние списки доменов, внешние списки подсетей.
Пользовательский список доменов, Пользовательский список подсетей в Podkop

---

**2026-02-23T08:58:02 | Anna Bagler**
https://podkop.net/docs/sections/#proxy

---

**2026-02-23T10:04:44 | Роман**
С Вацапом всё сложно, если через полный ВПН - нормально работает, если через точечную маршрутизацию - он ломится на большой спектр различных серверов - поэтому может и не завестись на zeroblock/podkop.

---

**2026-02-23T10:07:40 | Роман**
Дополнительные домены и ip для WhatsApp и Telegram - добавлять в список пользовательских доменов/ip в zeroblock/podkop.

#WhatsApp

IP
31.13.64.0/18
57.141.0.0/20
57.144.0.0/14
66.220.144.0/20
69.63.160.0/19
69.171.192.0/18
74.119.76.0/22
129.134.0.0/17
157.240.0.0/16
163.64.0.0/12
173.252.64.0/18
185.60.216.0/22
204.15.20.0/22
3.0.0.0/10


domain
bintray.com
whatsapp.biz
whatsapp.com
whatsapp.net
wa.me
whatsapp-plus.info
whatsapp-plus.me
whatsapp-plus.net
whatsapp.cc
whatsapp.info
whatsapp.org
whatsapp.tv
whatsappbrand.com


#Telegram

IP
91.108.4.0/22
91.108.8.0/22
91.108.16.0/22
91.108.12.0/22
149.154.160.0/20
91.105.192.0/23
91.108.20.0/22
185.76.151.0/24

domain
t.me
telegram.me
telegram.dog
telegra.ph
telesco.pe
telegramdesktop.com
tdesktop.com
fragment.com
cdn-telegram.org
comments.app
contest.com
graph.org
quiz.directory
telegram-cdn.org
telegram.space
tg.dev
tx.me
usercontent.dev
by Vasa


Так-же можно попробовать добавить автоматически обновляемые списки:
domain
https://raw.githubusercontent.com/KharunDima/whatsapp-lists/main/results/domains.txt

IP
https://raw.githubusercontent.com/KharunDima/whatsapp-lists/main/results/cidr_ipv4.txt

Для TG
https://core.telegram.org/resources/cidr.txt

Добавлять в пользовательские списки zeroblock/podkop - вставлять сами ссылки.

Так-же помогает скачать клиент WhatsApp с официального сайта, а не с PlayMarket (не забываем про бэкапы переписок, привязку почты для входа).

---

**2026-02-23T11:03:11 | Роман**
Zeroblock/podkop, если лапки скрипт 5, но всё равно домены/ip возможно нужно будет докинуть.

---

**2026-02-23T11:16:26 | Routerich**
https://podkop.net/docs/faq/#gostevaya-wi-fi-set-i-podkop

---

**2026-02-23T11:35:54 | Routerich**
По второму варианту вот
https://podkop.net/docs/sections/#polnostyu-marshrutiziruemye-ip-adresa-fully-routed-ips

---

**2026-02-23T11:37:05 | Роман**
Как мне кажется будет проще всю приставку в туннель завернуть, чем искать куда ходит приставка.
Zeroblock/podkop вам в помощь для этого.

---

**2026-02-23T13:25:16 | Routerich**
https://podkop.net/docs/sections/

---

**2026-02-23T13:30:12 | technique xxxxx**
Добрый день, установил на роутер podkop+zapret, youtube и сайты работают на телевизоре и компьютере,но на телефоне ничего не хочет открывать, в чем может быть причина ? DNS роутера стоит для всех устройств.Спасибо.

---

**2026-02-23T13:35:57 | Евгений Горбунов**
Добрый день, полскажите как попасть в настройку podkopa, не могу отвскать)

---

**2026-02-23T13:36:50 | Routerich**
Службы->Podkop

---

**2026-02-23T13:40:55 | Routerich**
Службы-">Podkop->Предустановленные списки->

---

**2026-02-23T13:43:09 | technique xxxxx**
Добрый день, установил на роутер podkop+zapret, youtube и сайты работают на телевизоре и компьютере,но на телефоне ничего не хочет открывать, в чем может быть причина ? DNS роутера стоит для всех устройств.Спасибо.

---

**2026-02-23T14:57:06 | Роман**
По логике полностью приставку в впн заворачивать. Но пинг вырастет. Через zeroblock/podkop можно реализовать.

---

**2026-02-23T15:03:41 | Роман**
podkop.net

---

**2026-02-23T17:27:14 | Steel_rat**
Добрый день.
Обновил прошивку на 24.10.5 без сохранения настроек. Воспользовался скриптом № 5, вариантом ручного ввода конфигурации и установкой Podkop.
При вводе конфигурации впн он 2 раза спросил настройки и видимо не смог их сохранить.
Сейчас творятся странные вещи - вручную ввожу правильные настройки в разделе "Равноправные узлы", рестартую интерфейс awg10, в "AmneziaWG Статус" вижу, что впн соединился, хендшейк есть. Через 1-2 минуты все отваливается, в настройках узлов вижу незнакомые конченые хосты и порты, например 188.114.96.61:500
В системном журнале такое:
Mon Feb 23 17:23:20 2026 daemon.notice netifd: Network device 'awg10' link is down
Mon Feb 23 17:23:20 2026 daemon.info ModemManager[2255]: hotplug: remove network interface awg10: event processed
Mon Feb 23 17:23:20 2026 daemon.notice netifd: Interface 'awg10' is now down
Mon Feb 23 17:23:22 2026 daemon.notice netifd: Interface 'awg10' is setting up now
Mon Feb 23 17:23:22 2026 user.notice amneziawg: info: using kernel-space kmod-amneziawg for /usr/bin/amneziawg
Mon Feb 23 17:23:22 2026 daemon.warn dnsmasq[1]: failed to create listening socket for 10.8.1.5: Address in use
Mon Feb 23 17:23:22 2026 daemon.notice netifd: Interface 'awg10' is now up
Mon Feb 23 17:23:22 2026 daemon.notice netifd: Network device 'awg10' link is up
Mon Feb 23 17:23:22 2026 daemon.info ModemManager[2753]: hotplug: add network interface awg10: event processed
Mon Feb 23 17:23:22 2026 user.notice firewall: Reloading firewall due to ifup of awg10 (awg10)
Mon Feb 23 17:23:27 2026 daemon.notice netifd: Network device 'awg10' link is down
Mon Feb 23 17:23:27 2026 daemon.info ModemManager[3196]: hotplug: remove network interface awg10: event processed
Mon Feb 23 17:23:27 2026 daemon.notice netifd: Interface 'awg10' is now down
Mon Feb 23 17:23:29 2026 daemon.notice netifd: Interface 'awg10' is setting up now
Mon Feb 23 17:23:29 2026 user.notice amneziawg: info: using kernel-space kmod-amneziawg for /usr/bin/amneziawg
Mon Feb 23 17:23:29 2026 daemon.warn dnsmasq[1]: failed to create listening socket for 10.8.1.5: Address in use
Mon Feb 23 17:23:29 2026 daemon.notice netifd: Interface 'awg10' is now up
Mon Feb 23 17:23:29 2026 daemon.notice netifd: Network device 'awg10' link is up
Mon Feb 23 17:23:29 2026 daemon.info ModemManager[3712]: hotplug: add network interface awg10: event processed
Mon Feb 23 17:23:29 2026 user.notice firewall: Reloading firewall due to ifup of awg10 (awg10)
Mon Feb 23 17:23:29 2026 daemon.err sing-box[10962]:  [31mERROR [0m[8091] [ [38;5;223m3267163615 [0m 0ms] router: UDP is not supported by outbound: main-out
Mon Feb 23 17:23:29 2026 daemon.err sing-box[10962]:  [31mERROR [0m[8091] [ [38;5;157m945614922 [0m 0ms] router: UDP is not supported by outbound: main-out
Mon Feb 23 17:23:30 2026 daemon.err sing-box[10962]:  [31mERROR [0m[8092] [ [38;5;123m2211925100 [0m 0ms] router: UDP is not supported by outbound: main-out
Поиск по чату ничего похожего не дал.
Подскажите, пожалуйста, в чем может быть проблема?

---

**2026-02-23T18:32:17 | Роман**
victronenergy.com
typekit.net
В zeroblock/podkop.

---

**2026-02-23T19:49:01 | Ринат Абдрахманов**
Подскажите, пожалуйста. Не очень понятно, что с онлайн играми, которые недоступны в России. У кого то заработал roblox, у кого то нет. У меня ни одна игра не заработала с podkop. Получал ответ в чате, что бесплатными обходами не получится ничего. А у кого то вроде заработало... Покупал роутер с этой целью. Но за youtube уже большое спасибо!

---

**2026-02-23T20:14:57 | Anna Bagler**
Службы - Podkop - Секции. Находим секцию discord и в ней в списках сообщества выбираем YouTube.

---

**2026-02-23T20:35:35 | Денис**
Ну пока оставлю так, по наблюдаю. Видимо нужно ждать когда в podkop добавят в листы.

---

**2026-02-23T20:48:30 | Routerich**
Прочитайте что я вам написал внимательно и изучайте документацию подкопа podkop.net

---

**2026-02-23T20:57:14 | Денис**
В общем, да. Заработало. Добавляем сеть 16.... в список пользовательских подсетей.
Пока для себя вопрос закрыл работы вотсапа. Напишу в podkop на рассмотрение и возможное добавления в листы.

---

**2026-02-23T20:58:54 | Anna Bagler**
IP в полную маршрутизацию в zeroblock/podkop и проверять.

---

**2026-02-23T21:01:40 | Anna Bagler**
Что вы ставили для обхода zeroblock или podkop скриптом?

---

**2026-02-23T21:19:44 | Benjamin Borovikov**
привет

я перепрошил роутер, начал запускать скрипт №5

он не устанавливатся, постоянно пишет, что я должен устанавливать пакеты вручную. Добрался до пакета podkop, при нажатии установки выдает ошибку отсутствия двух зависимостей:
sing-box и bind-dig.  Пишет, что они не доступны. 

Хочу понять можно ли устанавливать пакет без этих зависимостей? или нужно что-то чинить?

---

**2026-02-23T21:30:23 | Benjamin Borovikov**
привет

я перепрошил роутер, начал запускать скрипт №5

он не устанавливатся, постоянно пишет, что я должен устанавливать пакеты вручную. Добрался до пакета podkop, при нажатии установки выдает ошибку отсутствия двух зависимостей:
sing-box и bind-dig.  Пишет, что они не доступны. 

Хочу понять можно ли устанавливать пакет без этих зависимостей? или нужно что-то чинить?

---

**2026-02-24T01:58:53 | Kinaman**
Здравствуйте. Приобрёл роутер, установил скрипт №5, в службах появились Podkop и Zapret. По умолчанию всё работает, и youtube и discord, но судя по типу подключения - через vpn (см. скриншот). А на моём провайдере youtube и discord нормально работали через один из bat-файлов утилиты zapret-youtube-discord, которую я использовал на ПК до приобретения роутера - без vpn. Можно ли настроить службу zapret в роутере таким образом, чтобы youtube и discord работали без vpn как и раньше, а все остальные ресурсы уже через podkop?

---

**2026-02-24T09:11:19 | Routerich**
Здравствуйте.
возможно конфликт с Podkop, если он есть.
отключить всё обходы  и проверять.

---

**2026-02-24T10:02:39 | None**
Это значит что ютуб работает через podkop.

---

**2026-02-24T12:07:21 | Routerich**
Потом его сможете использовать в Podkop

---

**2026-02-24T12:53:47 | Роман**
Только отключить запрет 1 не забыть, и убрать Ютуб из zb/podkop.

---

**2026-02-24T13:48:06 | Михаил**
В чем тут порядок? В нарушении указаний документации от itdog? Мне кажется, в части использования podkop и zeroblock абсолютно ненужные действия. Нет?

---

**2026-02-24T13:50:34 | Роман**
Закинуть TG в zeroblock/podkop.

---

**2026-02-24T14:07:50 | Роман**
Запрет остановите, у вас пересечение с podkop.

---

**2026-02-24T16:45:13 | Alex**
Всем, привет, подскажите, пожалуйста самый оптимальный vless клиент для routerich, podkop, пробовал, но он  как-то странно работает (не все сайты корректно работают) , смотрю в сторону vrayA, чтобы сильно не нагружал роутер и не падал каждый день ). Может есть уже проверенные и стабильные решения

---

**2026-02-24T19:23:08 | Routerich**
Здравствуйте.
А если остановить Podkop, открываются?

---

**2026-02-24T19:23:54 | Routerich**
Службы->Podkop->Диагностика->остановить

---

**2026-02-24T19:27:22 | Routerich**
Тогда по инструкции к 5-му скрипту, добавьте домены эти в Podkop

---

**2026-02-24T20:01:48 | Александр**
Всем привет. Есть проблема при воспроизведении видео YouTube на смартТВ Lg webos. Периодически тормозит или совсем останавливается на разрешении 720р и выше. На смартфонах таких проблем нет, работает хорошо. Настроено через Podkop
RouteRich 24.10.3 r28872-daca7c049b RR-3.7.2 / LuCI openwrt-24.10 branch 25.280.58391~b7e4a9c
В чем может быть проблема?

---

**2026-02-24T21:03:00 | Михаил**
У себя решил просто. На первом рабочем роутере zapret2 (youtube) и podkop. Далее роутер для экспериментов 2 со zeroblock, в секции AmneziaWG (awg) тоже  youtube. У кого zapret2 на основном роутере не аллё( samsung, lg и айфон), идут на wifi второго роутера. :)

---

**2026-02-24T21:18:19 | Nikolay**
Подскажите, где то видел, настройку, чтобы при отвале podkop, не пропадал интернет. DNS настроить. Не могу найти

---

**2026-02-24T23:14:51 | 𝕾𝖊𝖗𝖌𝖊𝖎 𝕷𝖎𝖘𝖆𝖑𝖔**
Все норм, пашет, но только даунгрейд podkop бесит на 0.7.10.

---

**2026-02-24T23:21:17 | Роман**
В zeroblock/podkop.

---

**2026-02-24T23:58:36 | Виктор ZEUS**
Podkop?

---

**2026-02-25T07:37:18 | Sir**
Добрый день!
Кто то может помочь с discord?
Дискорд запускается, голос мой не слышат.
Скрипт new с Podkop и переустановленным Zapret2

---

**2026-02-25T08:11:51 | Routerich**
например войти через VPN на сайт, и установить расширение в браузере ipvfoo и отследить домены всё и потом в Podkop добавить

---

**2026-02-25T08:43:38 | Александр**
Здравствуйте. Подскажите пожалуйста при установке на RouteRichAX3000  программы  AmneziaWG, нужно устанавливать Podkop?

---

**2026-02-25T09:28:58 | Роман**
Zeroblock, podkop установлен?

---

**2026-02-25T09:38:44 | IM-Garage**
Добрый день 
Подскажите, не работает Gemeni, (youtube, и прочее ок) 
Пишет что страна не та

Переехал за город, и интернет сейчас с mikrotik 
То есть получается у меня двойной NAT 
Может ли быть в этом причина

Podkop работает, DoT используется

---

**2026-02-25T09:53:48 | Роман**
Иногда нужно время что-бы zeroblock/podkop заработали. Иногда нужно чистить кеш страницы.

---

**2026-02-25T10:11:57 | Ivan Bezgubov**
Никто не сталкивался в последнее время с тем что несколько раз в день пропадает доступ до Инстаграмма,Ютуба и тг? Использую vless с podkop. Работало стабильно , но непонятно , то ли в связи с последними новостями начали как то блокировать , то ли у меня какие то проблемы.
Несколько разных ключей пробовал

---

**2026-02-25T11:08:54 | Klmnt**
Подхожу к выводу что стандартные обходы (скрипт № 5-  podkop)  для YT через RR для МТС на Юге чаще не работают.

Клиенты Vless тоже пашут нестабильно. 

Последний Клиент Amnezia  теперь имеет два варианта подключения- Amnezia Legacy и Amnezia WG.  
На линуксе и Мак ОС оба работают.  На 11 Окнах Legacy работает нестабильно. 

на RR Awg  интерфейс либо  не дает подключения к Трубе. Либо только в 360р.

---

**2026-02-25T11:12:47 | Routerich**
статус->просмотр лога->
Службы->podkop->посмотреть логи->

---

**2026-02-25T12:54:08 | Роман**
Это для начала. Или руками ставьте zeroblock, podkop и настраивайте.

---

**2026-02-25T13:25:41 | IfonYa**
Здравствуйте , подскажите. Пользуюсь NotebookLM. Добавил в списки podkop - google.com Без поддомена.
Сам NotebookLM доступен по поддомену-  notebooklm.google.com. На комрьютере всё работает, но на мобилке не пашет , пока принудительно не влючишь VPN/ 
Каковы могут быть причины. Валидно будет в списки Podkop добавлять пользовательские домены с поддоменом и нужно ли это?
Спасибо.

---

**2026-02-25T16:18:16 | Владимир Волков**
https://docs.routerich.ru/ru/remote#%D0%B4%D0%BB%D1%8F-openwrt-%D1%81-podkop

---

**2026-02-25T19:26:36 | Роман**
Для точечной маршрутизации на роутере есть zeroblock/podkop. А на клиенты куча информации в интернете.

---

**2026-02-25T21:08:17 | Routerich**
Если пользуйтесь Podkop, то прям в настройках его укажите dns провайдера

---

**2026-02-25T21:27:29 | Леонид**
Не могу победить проблему - периодически пропадает инет до "ручного перезапуска" podkop. 24.10.5, что ваниль, что фирменная РР, весь софт обновлен и работал без сбоев. Бывает включаешь ПК - инета нет - не может получить IP устройство. Чаще всего - Wi-Fi устройства не получают IP (ТВ, планшет, смартфоны). Никак не пойму, в чем беда - мой провайдер "шалит" или же проблема в чем-то другом? Была проблема с коннектором - я его переобжал, всё надежно. Думал что подкоп падает из-за этого - но нет, не помогло.

Может есть у кого ещё такие проблемы? Беды начались около +-3 недель. До этого всё работало идеально.

---

**2026-02-25T21:28:02 | Леонид**
Уже подумываю пойти курить ZB, вдруг это всё таки чудит Podkop...

---

**2026-02-25T22:14:28 | Anna**
Мне помогло обновить до последней версии Podkop, тк проблема была в нём. В новой версии есть функция Exclude, т.е. исключить из маршрутизации, так и сделала с доменами twitch.

---

**2026-02-25T22:52:42 | Печати и штампы**
Есть ли где ман, где расписано, как работает Podkop и зачем нужна связка с AWG WARP?
А то запустил скрипт "с автоматической генерацией AWG WARP и установкой Podkop", Ютуб работает, на заблоченные сайты заходит, а как? Я даже свой VPS не указывал..

---

**2026-02-25T23:46:35 | Анатолий Шарков**
не открываются некоторые сайты по гео (заблокирован доступ из России). в podkop в разделе MAIN (proxy) добавил домены в список пользовательских доменов - Не помогло, попробовал добавить в разделе VPN - тоже не помогло. 
подскажите, что можно сделать

---

**2026-02-25T23:57:45 | Анатолий Шарков**
Анализ запущен: 2026-02-25 23:56:43
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.134 | YouTube IP:  198.18.0.135

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.68 MB / ↑0.38 MB
  Пинг (ya.ru via awg10): 83.730 / 84.471 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop    Youtube_Discord (vpn): youtube,discord,telegram
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.58 | RAM: 21% | NAND: 26% занято / 49.8M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

root@RouteRich:~#

---

**2026-02-26T05:53:51 | Routerich**
Здравствуйте.
Если есть в Podkop секция YouTube, Discord перенесите туда список Telegram, а в секции main удалите

---

**2026-02-26T08:26:26 | Routerich**
тогда отслеживайте домены на которые она обращается, и добавляйте их в Podkop

---

**2026-02-26T10:14:55 | Павел**
@RouterichSupport , Подскажите, у вас же наверняка есть версия последней официальной прошивки usb2 с уже интегрированным podkop-ом. Можно такую попросить?

---

**2026-02-26T11:27:29 | Павел**
@Routerich 😁У меня ума не хватит собрать рабочую прошивку с интегрированным работающим (!) podkop-ом. Я имею ввиду тот, который заведется после кнопки резет без накатывания скриптов №5

---

**2026-02-26T11:37:12 | Павел**
Накидать пакеты не проблема, а вот вписать настройки - это у меня не получается. Не заводится podkop. Скрипт 5 ставится и все работает. Сравниваю бэкапы обоих прошивок - основные настройки совпадают, но мой не работает. Ваши программисты молодцы, конечно. Я вас понял, в любом случае спасибо за ответы.

---

**2026-02-26T11:53:33 | АнтиМатерия**
День добрый! Пишу этот микрогайд для тех, кто как я хочет поиграть в Elite Dangerous, но не может из-за сами знаете чего.

Шагов 2:
1) Закидываете в podkop следующие адреса
zaonce.net
orerve.net
dler.org
И всё.

2) Если не заработало, в настройках игры поменяйте сетевой адаптер.

---

**2026-02-26T12:20:43 | Vladislav**
Подскажите что лучше Zapret2 или Podkop? Не очень понимаю чем они отличаются

---

**2026-02-26T12:31:16 | Роман**
Запрет 2 режет и меняет (дурит) трафик так, что ТСПУ его пропускает. 
Podkop направляет трафик на VPS сервер точечно по спискам.

---

**2026-02-26T12:49:42 | ALT F4**
podkop работает вместе с zapret2? Диагностика показывает дополнительные правила маркировки (от запрета) в podkop. Влияют друг на друга маркировки?

---

**2026-02-26T13:06:06 | 1v@nk0**
Вопрос чайника, извиняюсь, - чем отличаются сущности? 
1/ ZeroBlock  2/ Zapret   3/ Podkop
Что выбрать для работы с нейронками чтобы снизить вероятность отлететь в бан?

В wiki и руководстве пользователя не нашел - наверно плохо искал

---

**2026-02-26T17:28:00 | Лёша Альшанов**
Народ, подскажите!
Кто какой проверенной связкой сейчас пользуется для интернета "как раньше"? У меня подняты 10 локаций vless reality. Podkop/passwall и др. пробовал, но хочу ещё мнения профи услышать. Заранее благодарю!

---

**2026-02-26T17:37:58 | konnlori**
Всем привет. Во-первых, хочу выразить ну просто огромнейшую благодарность разработчикам пакета. Это просто лучшее, что случалось с обходом блокировок!

Есть пара вопросиков (я читал мануал, если что)
1. Я не могу понять, что за DNS редирект, и где его настраивать
2. Я так полагаю, ошибку с FakeIP я могу проигнорить (у меня бразуер Helium, и DoH там отключён, так что должно всё работать)
3. Zapret2 через интерфейс пока не настраивается?
4. Я не могу отключить zapret2, opera и AWG Warp в настройках
5. Я настроил YouTube, но почему-то он открывается как русский, и аватарок нет (при этом я удалил AWG, Opera и Zapret2 из системы, на Podkop всё нормально было)
6. Не могу удалить предустановленные секции. После перезагрузки страницы они возвращаются (благо отключение вроде как работает)

---

**2026-02-26T18:15:41 | MP**
Здравствуйте!!!!
Если пакеты обновлю, сейчас zapret 72.20251022 и podkop 0.7.7, настройки останутся прежними ?

---

**2026-02-26T19:20:07 | Marseille Geertje**
После сброса до заводских и установки zeroblock и podkop2 у меня даже обновление пакетов перестаёт работать. 😬 Вот так показывает при установке.

---

**2026-02-26T19:56:02 | Александр**
https://github.com/CodeRoK7/podkop-v0.2.5
Вот этот работал у меня

---

**2026-02-26T19:56:38 | Routerich**
Аааа, лучше установите новый Podkop.

---

**2026-02-26T19:57:06 | Routerich**
Потом vless выбирайте в настройках Podkop

---

**2026-02-26T20:13:59 | Роман**
Просто установите подкоп podkop.net, и закиньте свой vless.

---

**2026-02-26T23:44:15 | Алексей**
Не знаю было у кого такое или нет, после установки podkop (и скриптом и вручную) начинает дико всё виснуть, в вебку не зайти. Помогает ребут и удаление пакета. Может кто сталкивался с таким?

---

**2026-02-27T08:19:53 | STIG**
Добрый день. Подскажите кто сталкивался с проблемой?  Podkop выдавал ошибку error. Удалил полностью. Повторно не могу установить. Использую терминал и автоматическую установку. Доходит до скачивания и останавливается.

---

**2026-02-27T11:49:36 | Routerich**
Здравствуйте.
Самый простой в Podkop/zeroblock пустить в полный впн устройство
посложнее искать домены/подсети или использовать готовые из чата и добавлять их

---

**2026-02-27T11:52:12 | Routerich**
https://podkop.net/docs/sections/#polnostyu-marshrutiziruemye-ip-adresa-fully-routed-ips

---

**2026-02-27T14:42:25 | Антон Лузин**
Роутер из коробки. Поставил только podkop. Как подобрать стратегию, есть инструкция по настройке?

---

**2026-02-27T15:23:36 | Михаил**
Искал, искал и вроде бы нашел ошибку zeroblock. 
Есть две секции с awg - вторая и четвертая в списке. Оба интерфейса провереные в podkop - оба работающие. К слову первый из них протон, второй warp. Первая секция opera - она вообще тут не при делах. А вот третья urltest  в ней несколько ссылок ss, hysteria2 и пр. Итог - при активной третьей секции urltest - секция awg перед ней в норме, а после нее - awg не отзывается. Если сделать секцию urltest неактивной - то и второй и червертый awg работают.

---

**2026-02-27T18:55:29 | Routerich**
https://podkop.net/docs/install/

---

**2026-02-27T19:05:22 | Михаил**
У меня и podkop и zeroblock отлично на одном роутере сожительствуют. Через автозапуск то один стопорю и другой запускаю. Пока проблем не было. Зато есть возможность сравнить одно ПО с другим.

---

**2026-02-27T19:31:08 | Kiss_My_Axe**
Ужос! Ютубанблок остановить, что там у вас было установлено, я не знаю, но этого там больше нет.
То есть нет либо ZeroBlock, либо Podkop.
DNS пугающе прекрасны!

Устанавливайте повторно или зероблок, или подкоп.

---

**2026-02-27T20:59:09 | Роман**
podkop.net

---

**2026-02-27T21:45:58 | Lex Luther**
Добрый вечер, хотел уточнить вопрос, пользуюсь podkop. Он создал 2 секции main и youtube_discord. Использую main, перевел в режим vpn, конфиг  сервера добавил, списки свои тоже, выходной интерфейс awg10 и вот меня интересует, точно ли этот интерфейс использовать?

---

**2026-02-27T22:04:55 | Routerich**
zeroblock или podkop остановили?

---

**2026-02-27T22:07:41 | Routerich**
Остановите еще podkop

---

**2026-02-28T03:17:18 | Aidar Safiullin**
Друзья, подскажите, пожалуйста, нестандартный вопрос. 
Играем в UNO Mobile. 
Есть ли для этой игры ip адреса или подсети для добавления в podkop, чтобы показывало рекламу в игре для гринда монеток и всего прочего?

---

**2026-02-28T05:24:05 | Igor**
Спасибо за ссылку, но насколько я понимаю, это какие то конкретные действия в podkop?

---

**2026-02-28T05:28:23 | X**
У меня сейчас podkop просто работает и не глючит. Не особо понятно зачем ставить и быть тестировщиком ZeroBlock. Я бы попробовал что-то новое, может там какие-то полезные функции, но возиться с недоработанными программами желания нет.

---

**2026-02-28T05:29:25 | Routerich**
Podkop так же в состоянии бета если что) Так что вы тестировщик такой же получается

---

**2026-02-28T05:34:07 | Routerich**
https://github.com/itdoginfo/podkop?tab=readme-ov-file#%D0%B2%D0%B5%D1%89%D0%B8-%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D1%8B%D0%B5-%D0%B2%D0%B0%D0%BC-%D0%BD%D1%83%D0%B6%D0%BD%D0%BE-%D0%B7%D0%BD%D0%B0%D1%82%D1%8C-%D0%BF%D0%B5%D1%80%D0%B5%D0%B4-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%BE%D0%B9 а теперь читайте

---

**2026-02-28T07:28:04 | Михаил**
А как у вас в podkope подписки работают? Я в нем  типа конфигурации подписки  не вижу. А вот в zeroblock такой тип  как раз есть.

---

**2026-02-28T07:37:07 | Михаил**
У меня на рабочем(для семьи) podkop, на экспериментальном (для души)и podkop и zeroblock. В zeroblocke возможностей поболе получается.

---

**2026-02-28T09:15:07 | Anna Bagler**
Секция main подкопа, тип сменить на URL и вставить свою ссылку. podkop.net Секции, изучайте.

---

**2026-02-28T09:15:56 | Александр**
PS5. ZeroBlock или podkop, пробовал и то и другое. Весь трафик консоли идёт через VPN wireguard.
Про ip, не понял. Белый ли ip у меня? То я так понимаю нет. Да и у друзей точно нет.

---

**2026-02-28T11:08:46 | Алексей Новиков**
Добрый день!

Обновил podkop, вот сюда добавил домены, диагностика не показывает ошибок, но twitch не завелся

Есть у кого-нибудь ещё идеи что у меня не так?

---

**2026-02-28T12:30:25 | Михаил**
Проверил. При перезапуске zeroblock списки в подписке точно поменялись. Это работает. Если ваши списки меняются на удаленном сервере, к которому вы указали доступ через https, как мне кажется(!), zeroblock ничего не чувствует и продолжает работать со старыми списками. Так что железобетонный способ все же -перезапуск zeroblock. 
В принципе, если бы разработчик поставил бы еще один таймер и дал им управлять, и по нему обновлял бы список, было бы вообще шоколадно. Podkop бы в этом вопросе остался далеко позади.

---

**2026-02-28T13:02:19 | Marseille Geertje**
Я пробовал на сброшенный до заводских настроек ставить только youtubeUnblock и вот в этом случае скорость ютуба меня устраивает. 😁 (пробовал даже после скрипта 5 отключать в вебке podkop и  zapret при одновременном включении youtubeUnblock и тогда ютуб тоже работает приемлемо для меня)
Но загвоздка в том, что остальная запрещёнка тогда либо не работает, либо я не понял что-то. 😁

---

**2026-02-28T13:09:07 | Marseille Geertje**
Удобнее связки Podkop и Zapret (скрипт 5)

---

**2026-02-28T14:13:31 | ㅤㅤ**
Все аналогично. Мой iPad работал. Работал и один iPhone. При этом обозначенные устройства не работали. Значит сидим дальше на Podkop и в свободное время самостоятельно пробуем искать проблему. "У меня работает,  а ты неудачник" - не помощь в решение точно. (не вас имею ввиду)

---

**2026-02-28T14:34:21 | ㅤㅤ**
Все верно. По логам я подробно видел что происходит. Устройства выходили в сеть минуя fakeip на реальные адреса. В первую очередь глядел IPv6 и отсекал, но тщетно. DNS брали с роутера (192.168.1.1). Podkop все решил без танцев.

---

**2026-02-28T16:13:27 | Александр**
Не понимаю, почему RDR2 такой капризный. 😵‍💫
Короче говоря, получилось запустить RDR2 через VPN WireGuard силами роутера получается? 
https://lsetc.ru/openwrt-nastrojka-wireguard-klienta/#%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0_WireGuard_%D0%BA%D0%BB%D0%B8%D0%B5%D0%BD%D1%82%D0%B0_%D0%BD%D0%B0_OpenWRT_%D1%80%D0%BE%D1%83%D1%82%D0%B5%D1%80%D0%B5

Без всяких Podkop/ZeroBlock/V2RayA. Через всё это онлайн в RDR2 не работает.
В других играх ещё не сталкивался,всё всегда работает через ZeroBlock.

Теперь придётся скакать между ZeroBlock и WireGuard на роутере.

---

**2026-02-28T16:23:37 | Александр**
Вот, вот. Это первая игра, которая не хочет работать через VPN через ZeroBlock, Podkop, V2rayA. Даже если в ZeroBlock Wireguard проходит. Хоть убей, не работает только RDR2. Как только напрямую wireguard запустил, всё заработало.

---

**2026-02-28T20:11:36 | Даниил Тихмянов**
Добрый вечер, можете пожалуйста подсказать, куда копать и что сделать, чтобы заработал дискорд? 
Я настроил AmneziaVPN - создал соответствующий интерфейс и межсетевой экран. 
Скачал podkop и настроил его через сетевой интерфейс amnesia. 
Все работает, могу открыть и Rutube, Youtube, Chatgpt, meta, но не могу открыть дискорд.
Еще почему-то не проходит диагностика:

Outbounds проверки:
Проверки не выполнены
main
Не отвечает

Подскажите пожалуйста, что стоит сделать, чтобы решить эту проблему? Буду премного благодарен за помощь.

---

**2026-02-28T20:19:11 | Routerich**
Тогда убирайте общий список, и добавьте список block, и снова проверьте диагностику Podkop

---

**2026-02-28T20:38:22 | Makz Chernov**
Всем еще раз доброго дня. Получил роутер, настроил интернет. все отлично. Настроил Podkop Заработалов все и youtube и все все все. Но так и не решился вопрос в warframe (добавил все домены). Раньше он работал при включенном DurevVPN. (Ругается на проверку портов 4950 и 4955)- пообщался с chatgpt, тот подсказывает что ошибка из за UDP is not supported и что нужно как то прописывать правила по особо. UDP через TCP не помогает. Может кто-то сталкивался и есть решение?

---

**2026-02-28T21:10:00 | Роман**
Смотря что нужно. Zeroblock вам Анна скинула, podkop.net это по подкопу. Для запрета 2 в ветке запрет 2 в закрепленных сообщениях.

---

**2026-02-28T21:14:09 | Anna Bagler**
Zeroblock/Podkop.

---

**2026-02-28T22:56:28 | Zamir**
Анализ запущен: 2026-02-28 22:51:40
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  57.144.244.1 | YouTube IP:  74.125.205.91

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.37 MB
  Пинг (ya.ru via awg10): 88.632 / 91.518 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОФЛАЙН
------------------------------------------------------
  curl: (28) Connection timed out after 5000 milliseconds
  Warning: Problem : timeout. Will retry in 1 seconds. 3 retries left.
  curl: (28) Connection timed out after 5000 milliseconds
  Warning: Problem : timeout. Will retry in 2 seconds. 2 retries left.
  curl: (28) Connection timed out after 5000 milliseconds
  Warning: Problem : timeout. Will retry in 4 seconds. 1 retries left.
  curl: (28) Connection timed out after 5000 milliseconds
------------------------------------------------------
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 74.125.205.93
    Name:       youtube.com
    Address: 74.125.205.91
    Name:       youtube.com
    Address: 74.125.205.190
    Name:       youtube.com
    Address: 74.125.205.136
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop    Youtube_Discord (vpn): discord
  podkop           main (prx out): google_ai,meta,telegram,twitter
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.14

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.12 | RAM: 22% | NAND: 28% занято / 48.1M доступно
  
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

root@RouteRich:~#

---

**2026-02-28T22:59:08 | Dmitry Shirshov**
Подскажите, как настроить Podkop

---

**2026-02-28T22:59:19 | Dmitry Shirshov**
Podkop Error
Sat Feb 28 22:57:42 2026 user.notice podkop: [error] Outbound section not found. Please check your configuration file (missing proxy_string, selector_proxy_links, urltest_proxy_links, outbound_json, or interface). Aborted.

---

**2026-02-28T23:24:21 | Роман**
sh <(wget -q -O - https://raw.githubusercontent.com/routerich/RouterichAX3000_configs/refs/heads/podkop0711/universal_config_new_podkop.sh) 2>&1 | tee /root/run.log
Это в терминал.

---

**2026-03-01T00:02:47 | Денис Азаров**
Приветствую! Подскажите, можно ли использовать в podkop не одну ссылку vless, а несколько, чтобы когда один сервер перестает работать, переключался на другой?

---

**2026-03-01T00:37:11 | Денис Азаров**
opkg remove luci-i18n-podkop-ru, opkg remove luci-app-podkop, opkg remove podkop.

---

**2026-03-01T00:38:17 | Bbvshnv**
Здравствуйте! А как обновить podkop ?

---

**2026-03-01T00:38:33 | Роман**
podkop.net

---

**2026-03-01T00:40:04 | Денис Азаров**
Sun Mar 1 00:33:35 2026 user.notice podkop: [error] Outbound section not found. Please check your configuration file (missing proxy_string, selector_proxy_links, urltest_proxy_links, outbound_json, or interface). Aborted.

---

**2026-03-01T01:04:18 | Роман**
/etc/config/podkop
/etc/init.d/podkop
Возможно там что осталось от старого подкопа, и оно всё в куче и не работает.

---

**2026-03-01T02:15:13 | Денис Азаров**
всё-таки не все гладко - на вкладке диагностика выдает следубщее:
Podkop Error
Sun Mar 1 02:14:05 2026 user.notice podkop: [error] Detected https-dns-proxy in DHCP config. Edit /etc/config/dhcp

---

**2026-03-01T09:54:50 | Routerich**
Здравствуйте.
В Podkop создать отдельную секцию с типом Proxy, и туда вставить ключ vless, потом в предустановленные списки добавить YouTube, а с других секций убрать

---

**2026-03-01T12:26:00 | Zeal Tree**
Не уверен в какую тему это стоит писать, но напишу наверное здесь. Подскажите пожалуйста может быть кто-то с подобным сталкивался:

opkg update
Downloading https://github.com/routerich/packages.routerich/raw/24.10.5/core/Packages.gz
Updated list of available packages in /var/opkg-lists/routerich_core
Downloading https://github.com/routerich/packages.routerich/raw/24.10.5/core/Packages.sig
Signature check passed.
Downloading https://github.com/routerich/packages.routerich/raw/24.10.5/base/Packages.gz
Updated list of available packages in /var/opkg-lists/routerich_base
Downloading https://github.com/routerich/packages.routerich/raw/24.10.5/base/Packages.sig
Signature check passed.
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/luci/Packages.gz
Failed to send request: Operation not permitted
*** Failed to download the package list from https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/luci/Packages.gz

Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/Packages.gz
Failed to send request: Operation not permitted

У меня стоят podkop и zapret, и так понимаю что судя по сообщению в podkop "DNS роутера не проходит через sing-box" видимо между ними какой-то конфликт. Рекомендации из сообщения "Еще Раз Немного Про DNS Failsafe Proxy" выполнял. В DNS Failsafe Proxy
Основной: 127.0.0.42:53
Резервный: 127.0.0.1:5453

Попробовал посмотреть что за ip выдаются

nslookup downloads.openwrt.org
Server:         127.0.0.1
Address:        127.0.0.1:53

Name:   downloads.openwrt.org
Address: 198.18.0.30

ping -c3 198.18.0.30
PING 198.18.0.30 (198.18.0.30): 56 data bytes

--- 198.18.0.30 ping statistics ---
3 packets transmitted, 0 packets received, 100% packet loss

nslookup downloads.openwrt.org 8.8.8.8
Server:         8.8.8.8
Address:        8.8.8.8:53

Non-authoritative answer:
downloads.openwrt.org   canonical name = dualstack.j.sni.global.fastly.net
Name:   dualstack.j.sni.global.fastly.net
Address: 151.101.66.132
Name:   dualstack.j.sni.global.fastly.net
Address: 151.101.130.132
Name:   dualstack.j.sni.global.fastly.net
Address: 151.101.194.132
Name:   dualstack.j.sni.global.fastly.net
Address: 151.101.2.132

Non-authoritative answer:
downloads.openwrt.org   canonical name = dualstack.j.sni.global.fastly.net
Name:   dualstack.j.sni.global.fastly.net
Address: 2a04:4e42:400::644
Name:   dualstack.j.sni.global.fastly.net
Address: 2a04:4e42:600::644
Name:   dualstack.j.sni.global.fastly.net
Address: 2a04:4e42::644
Name:   dualstack.j.sni.global.fastly.net
Address: 2a04:4e42:200::644

ping -c3 151.101.66.132
PING 151.101.66.132 (151.101.66.132): 56 data bytes
64 bytes from 151.101.66.132: seq=0 ttl=53 time=33.544 ms
64 bytes from 151.101.66.132: seq=1 ttl=53 time=33.588 ms
64 bytes from 151.101.66.132: seq=2 ttl=53 time=33.437 ms

--- 151.101.66.132 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 33.437/33.523/33.588 ms

Так понимаю что я в настройках либо podkop либо zapret что-то не довыставил видимо. С устройств, которые подключены к роутеру ссылка нормальная и скачивается https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/luci/Packages.gz

---

**2026-03-01T14:32:25 | Anton Prytkov**
сделал, то же самое, podkop рестартнул

---

**2026-03-01T15:34:27 | Anton Prytkov**
вопрос что значит DNS роутера не проходит через sing-box : днс ходят через тейл? Насколько это для работы podkop критично?

---

**2026-03-01T16:23:18 | Роман**
Здравствуйте. Из коробки может заработать только Ютуб. Если нет, удалять youtubeunblock и ставить запрет 1-2, если только для Ютуба. Если инста - zeroblock/podkop, если лапки - скрипт 5.

---

**2026-03-01T17:34:30 | Михаил**
Прелесть zeroblock, как и podkop, что при правильной настройке эти ресурсы проходят мимо. И маршрутизируются только выбранные в секциях.

---

**2026-03-01T19:53:13 | Евгений**
Здравствуйте. Стоит Podkop + Zapret2. Не работает VoWiFi. Может есть какие то гайды по нему?

DNS гугловские везде

---

**2026-03-01T19:54:56 | Routerich**
Здравствуйте.
А если все остановить, Podkop, Zapret2 то работает?

---

**2026-03-01T19:56:29 | Routerich**
А если запустить Podkop, а zapret2 остановлен?

---

**2026-03-01T20:08:06 | Сергей Ананьев**
Анализ запущен: 2026-03-01 20:05:44
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Попытка обновления списка пакетов: (2/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.1.27 | YouTube IP:  198.18.1.28

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓16.65 MB / ↑0.69 MB
  Пинг (ya.ru via awg10): 15.348 / 16.835 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop    Youtube_Discord (vpn): youtube,discord,telegram
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.79 | RAM: 27% | NAND: 26% занято / 49.9M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-03-01T20:16:16 | Routerich**
И если отключить Podkop, то грузится?

---

**2026-03-01T22:16:26 | Роман**
Ставьте и играйте, кто вам мешает? Ну серьезно?
Я же вам написал, если нужен обход на уровне роутера - ставите zeroblock/podkop - суете туда vless:// или hy:// выбираете список роблокс или games и играете.

---

**2026-03-01T22:48:16 | Михаил**
Там же в podkop проблем так же нет. Изменение dns в dot и doh ситуацию не исправили.

---

**2026-03-02T01:47:10 | Rave**
Получается желательно сменить ВПН? И по моему когда ранее накатывал Podkop вообще не настраивал в нем ничего и все работало "С коробки"
Теперь нету возможности без использования своего ВПНа?

---

**2026-03-02T12:04:46 | TomatHunter 🍅💀**
Добрый день. Лог установки беты (zapret не поставился, скрипт поставил podkop)

---

**2026-03-02T12:12:38 | Routerich**
Здравствуйте. 
https://podkop.net/docs/sections/#polnostyu-marshrutiziruemye-ip-adresa-fully-routed-ips

---

**2026-03-02T14:17:19 | Anna Bagler**
https://podkop.net/docs/sections/#polnostyu-marshrutiziruemye-ip-adresa-fully-routed-ips принцип тот же.

---

**2026-03-02T14:56:12 | Routerich**
Система - пакеты - обновить списки - вкладка обновления - обновить пакеты с amneziawg. Далее https://podkop.net/docs/tunnels/awg_settings/ пункт установка пакетов пропустить

---

**2026-03-02T15:26:01 | Oleg Belskiy**
Здравствуйте. Поставил ZeroBlock на чистую систему, при установке были ошибки  как на скрине, вся запрещёнка при этом открывается. По ощущениям работает лучше Podkop, спасибо вам за это, хотя всё равно лучше конечно посмотреть на длительной дистанции использования. Вот ещё странность, может сможете мне объяснить в чём может быть причина: добавил третью секцию со своим ключом, ничего из списков не выбирал, на Хроме speedtest определяется oslo, то есть идёт через верхний прокси как и должно быть, а вот в Яндексе определяется ip сервиса, который в новой секции. Убираю галочку с третьей секции и Яндекс показывает уже мою локацию и мой ip. Вопрос как? Там же секция с ключом пустая, она же не должна пускать весь трафик через себя по идее. Скрин прилагаю.

---

**2026-03-02T16:48:04 | ᴀʟᴇxᴇʏ ɪꜱᴀᴋᴏᴠ**
Ток я не понял в какой момент, я следом еще Podkop апнул до последней версии

---

**2026-03-02T18:29:51 | Александр**
так вот и озадачен. за год службы ни одного затупа не видел на старой прошивке с podkop старым интерфейсом. помойму от кодерок был скрипт

---

**2026-03-02T18:54:44 | Andrey Pykhonin**
Заработало! Теперь мне просто этот код вставлять в терминал? sh <(wget -q -O - https://raw.githubusercontent.com/routerich/RouterichAX3000_configs/refs/heads/podkop0711/universal_config_new_podkop.sh) 2>&1 | tee /root/run.log

---

**2026-03-02T19:00:24 | Routerich**
Если вам нужен чистый wireguard, то нужно будет установить  пакеты для него. В последних прошивках они выпилены и стоит сразу amneziawg. https://podkop.net/docs/tunnels/ пункты с установкой пакетов для амнезии пропустите

---

**2026-03-02T20:23:41 | ㅤㅤ**
Добрый вечер. Как бы решали вопрос по обходу на iPhone по логике Zapret2|Podkop|ZeroBlock и т.п.

Наткнулся на китайский Quantumult X. Целый день возился с их китайскими конфигами. Штука интересная, но непростая в работе. Конфиг сильно ограничен в синтаксисе. AmneziaWG не поддерживает. Зато работает с VLESS (Reality пока не поддерживает).

Быть может я просто закопался и стоит пойти по более простым путям? Каким образом наладить работу по обходу DPI в достаточно закрытой и ограниченной оси. В этом дилемма.

---

**2026-03-02T21:24:14 | Sir**
Анализ запущен: 2026-03-02 21:20:57
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.3 | YouTube IP:  198.18.0.4

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.68 MB / ↑0.34 MB
  Пинг (ya.ru via awg10): 44.072 / 45.179 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop zapret2

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop    Youtube_Discord (vpn): youtube,discord,telegram
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 9.9.9.9 / 1.1.1.1
  Версия podkop: v0.7.14

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.13 | RAM: 26% | NAND: 27% занято / 49.5M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-03-03T01:24:27 | Anna Bagler**
Они совместимы, если домены не пересекаются. podkop.net Секции, можете изучать.

---

**2026-03-03T08:46:27 | Keeper**
Приобрел уже 5 роутеров у этой шикарной команды! Низкий Вам поклон и бесконечная благодарность за труды!

3 установил у родни в своем регионе, 1 сейчас едет на суровый север страны, 1 лежит в запасе.
Я хоть и фанат Mikrotik, но для установки родне и знакомым выбрал данный девайс, ни разу не пожалел, ибо все максимально просто и понятно для человека с любым уровнем знаний.
Поэтому моя задача - это первоначальные настройки и удаленный доступ на всякий случай, а дальше человек уже сам начинает интересоваться.
Буквальный пример: бывший заводчанин 60+ лет, который ни разу не интересовался технологиями уже сам находит и добавляет в podkop'е домены и CIDR'ы для обхода WA 😁

Команда не просто своевременно выпустила на рынок нужный девайс, но и обеспечила поддержку такого уровня, какого многим более крупным вендорам не достичь уже никогда. Одни подробные мануалы чего стоят!
Устройство разворачивается и начинает приносить пользу буквально в несколько кликов.
Отдельно хотелось бы отметить простых ребят из чата, которые помогают в поддержке, тестировании и в развитии продукта.

Отдельная благодарность за ZeroBlock, поставил на последний аппарат, буду тестировать на живых людях 😈

---

**2026-03-03T09:38:48 | Владимир**
ZeroBlock это форк podkop?

---

**2026-03-03T13:19:50 | Kir**
Здравствуйте подскажите куда копать , секция discord в podkop крашиться 1-2 раза в день, после перезагрузки podkop все начинает работать

---

**2026-03-03T15:00:58 | Mila V**
подскажите что делать, если такое в логах диагностики

  Пинг (ya.ru via awg10): ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (77.88.44.242): 56 data bytes
  Программы в автозапуске: podkop

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОФЛАЙН
------------------------------------------------------
  curl: (28) Connection timed out after 5000 milliseconds
  Warning: Problem : timeout. Will retry in 1 seconds. 3 retries left.

---

**2026-03-03T15:34:03 | Kirill**
Подскажите пожалуйста, имеет смысл обновлять? 
 

и можно обновиться как на гитхабе пишут, вот такой окмандой - sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)

---

**2026-03-03T15:48:56 | Роман**
Есть правило, работает - не лезь. 
Дело ваше. Всего делов скрипт запустить podkop.net.

---

**2026-03-03T18:41:07 | Routerich**
Здравствуйте.
Думаю будет легче так
https://podkop.net/docs/faq/#nastrojka-marshrutizacii-i-spiskov

---

**2026-03-03T19:07:10 | Routerich**
https://podkop.net/docs/tunnels/awg_settings/ пропустить установку пакетов и далее в зероблок секции

---

**2026-03-03T19:39:37 | Никита**
Уже видел ответы по home-connect и технике bosch
Но проблема остается, даже если я делал все, по предыдущим сообщениям.
Короче - в какой-то момент отвалилась стиралка от home connect. Я ее удалил из учетки и не мог снова добавить. Купил роутер. Поставил podkop, внес бошевские домены в список, но ни одно устройство так и не получается добавить. Хотя все остальное ок работает(ютуб, дискорд и т.п.). При добавлении падает ошибка h9208 типо "Соединение с сервером прервано". Мб кто-то сталкивался и находил выход?

---

**2026-03-03T20:14:21 | Дмитрий Коханский**
А получилось ли у кого-нибудь заставить работать mortal kombat 1 с помощью podkop?

---

**2026-03-03T20:45:27 | Routerich**
Да и добавить интерфейс https://podkop.net/docs/tunnels/awg_settings/ пункт установка пакетов пропустить

---

**2026-03-03T21:22:13 | Routerich**
Система - автозапуск - podkop - запустить

---

**2026-03-03T21:39:26 | Alexandr**
сделал эти действия, снова запустил проверку в терминале. Все равно показывает podkop stopped

---

**2026-03-03T22:31:01 | Владимир Волков**
Если не захотите прошиваться, то в терминале роутера (там, где запускаете скрипт диагностики):
service podkop start
Не помню, сразу ли выводит лог, поэтому командой можно вывести дополнительно и посмотреть, стартует ли он вообще:
logread | grep podkop

---

**2026-03-03T22:58:44 | Роман**
В секцию со своим сервером в zeroblock/podkop.

---

**2026-03-04T00:00:01 | Роман**
Через пакеты можно установить. Убрать из секций Ютуб zeroblock/podkop. Отключить youtubeunblock.

---

**2026-03-04T00:00:15 | Anna Bagler**
Ставьте, меняйте на URL и свою ссылку vless туда. podkop.net Ceкции. Запрет - подбирать стратегию. Запрет2 должен взлететь сразу. Только список yt из подкопа убрать.

---

**2026-03-04T00:33:49 | Anna Bagler**
Стратегии пробовать https://t.me/routerich/3845/509958
Или тогда в zeroblock/podkop.

---

**2026-03-04T08:11:20 | Андрей Стыврин**
Добрый день. 
Есть роутер РТК, к которому подключён РР, на нём настроен podkop + zapret. Получил второй РР, подключил его также к роутеру РТК, настроил его, отключил, но теперь через первый РР не работает телега через подкоп. 
Что можно сделать?

---

**2026-03-04T08:16:03 | Anna Bagler**
От временного отключения таких изменений быть не может. Телеграм добавлен в секцию подкопа? Может просто совпало с моментом блокировки у провайдера. Перезапустить opera-proxy и podkop.

---

**2026-03-04T08:26:23 | Anna Bagler**
Куда-то сюда  https://podkop.net/docs/diagnostics/
dhcp в начале для РР норма.

---

**2026-03-04T08:28:00 | Trade Secret**
Здравствуйте как обновить podkop на маршрутизаторе?

---

**2026-03-04T11:00:04 | Maxim Mrakov**
Всем доброе утро, подскажите пожалуйста самый простой способ поднять VPN на роутере, что бы ещё с ним работал podkop и можно было подключить мобильный телефон.

---

**2026-03-04T11:03:13 | Anna Bagler**
Podkop - точечная маршрутизация. У РР есть свой zeroblock c возможностью cекций без списков.

---

**2026-03-04T11:04:44 | Maxim Mrakov**
У меня он как раз настроен точечно на то что мне нужно, по этому хотел понять, как можно быстро поднять vpn и сделать так что бы podkop так же понимал что телефон обращается к ресурсу и перенаправлял его через vless и т.д

---

**2026-03-04T11:10:24 | Maxim Mrakov**
У меня дома настроен podkop на роутере на пк и с домашним wifi все ок.

Я хочу поднять любой VPN который делается +- в 2 клика что бы я условно с работы, мог подключиться к домашней сети и если захочу посмотреть ютуб что бы podkop понял это и направил через vless

---

**2026-03-04T11:11:59 | Dmitrii Burenin**
Podkop настройка забить в гугле.

---

**2026-03-04T11:40:23 | Routerich**
А как вы понимаете что оно не работает?
из-за Podkop может.

---

**2026-03-04T12:04:23 | Anna Bagler**
Если у вас будет conf-файл под амнезию, то импортируете в интерфейс, если ссылка то URL в секции.
podkop.net Секции, изучайте.

---

**2026-03-04T12:37:44 | Andrey Lazarev**
Уважаемые специалисты, можете подсказать - при установленных podkop и zapret2, есть ли простой способ (если вообще есть) обойти замедление телеги сейчас?

---

**2026-03-04T13:22:20 | Владимир Батурин**
кто шарит как в Podkop добавить доменные имена в исключения 
либо ip адреса в исключения 

т.е. мне необходимо какие то опредленные адреса пустить мимо прокси 
Сейчас эти адреса уходят в прокси

в YACD 
67af23f9-4a43-45d4-a2f1-c8c431970590
Host:
5.xxx.xxx.2:443
Sniff Host:
-
Process:
-
Destination:
5.xxx.xxx.2:443
Remote Destination:
-
Rule:
inbound=tproxy-in source_ip_cidr=192.168.1.1/24 => route(main-out)
Chains:
main-out
Type:
tproxy/tproxy-in(tcp)
Network:
tcp
Source:
192.168.1.110:51717
Upload:
295 B
Download:
0 B
Start Time:
less than a minute

---

**2026-03-04T14:47:45 | Routerich**
Здравствуйте.
найти домены этого сервиса и добавить их в Podkop по инструкции к 5-му скрипту

---

**2026-03-04T14:49:01 | Routerich**
Здравствуйте.
либо Podkop, либо zeroblock

---

**2026-03-04T14:56:02 | Routerich**
а если остановить zapret? podkop? работать начинает?

---

**2026-03-04T15:24:38 | Anna Bagler**
ipvfoo в браузер + vpn и потом смотрим, домены второго уровня добавляем в zeroblock/podkop.

---

**2026-03-04T17:04:18 | -Miracle**
opkg install podkop
Installing podkop (v0.7.10-r1) to root...
Ошибки
Collected errors:
 * check_conflicts_for: The following packages conflict with podkop:
 * check_conflicts_for:   https-dns-proxy * 
 * opkg_install_cmd: Cannot install package podkop.
Команда opkg install завершилась с ошибкой с кодом 255.

---

**2026-03-04T17:49:17 | Роман**
Решение найдено для игры MK1, эти домены в zeroblock/podkop:

api.wbgames.com
wb-hydra.wbgames.com
mortalkombat.com
amazonaws.com.
bugs.wbgames.com
telemetry.wbgames.com
cdn.wbgames.com

Плюс скопировать все cidr:

https://github.com/123jjck/cdn-ip-ranges/blob/main/aws/aws_plain_ipv4.txt

Взято из соседнего чата itdog.
#games

---

**2026-03-04T18:52:06 | Shinobino Mono**
Здравствуйте.
Подскажите, пожалуйста, что можно сделать, если после подготовки и установки скрипта №5 на ПК ни один сайт не грузится, и вдобавок не работает Discord, хотя тот же Telegram на ПК вполне работает. Podkop при попытке диагностики выдаёт несколько ошибок, хотя в его настройках изменений не производил после завершения скрипта №5.

---

**2026-03-04T19:05:23 | Routerich**
Хм, а попробуйте в настройках Podkop сменить DNS на яндекс и проверить

---

**2026-03-04T21:08:25 | Smallin**
Добрый день! Подскажите, в чём преимущество ZeroBlock перед Podkop?
В двух словах
Если все устраивает в методе №5, помимо медленной загрузки тг, есть смысл протестировать?

---

**2026-03-04T21:30:51 | Routerich**
А в какой секции Podkop у вас YouTube?

---

**2026-03-04T21:50:54 | Александр**
Так здесь сказано, по аналогии с Podkop.
https://t.me/routerich/499562

Последний пункт оставался. Я так понял, это как раз выбрать гостевую в "Входящие интерфейсы", но только в ZeroBlock. + ещё кто-то мне отвечал из темы вопросов, что нужно выбрать в этом пункте гостевую.

Но даже если убрать галку, на 0.7.0 гостевая не работает при Вкл. ZeroBlock. На 0.6.4 я ковыряю настройки, вроде как завелось. Создавал с нуля гостевой интерфейс.

Сейчас пока эксперементирую перед сном, накатил 0.7.0, всё, гостевая померла.

---

**2026-03-05T05:43:33 | IT**
Zeroblock это более удобная замена podkop? Назначение у них одинаковые, направлять трафик в нужные дырки?

---

**2026-03-05T06:11:15 | Routerich**
Проверьте, потом расскажете.
Возможно будут проблемы если используете Podkop / zeroblock

---

**2026-03-05T08:26:55 | Gleb Alekseevich Shumkin**
Добрый день. Настроил удаленный доступ, включил exit node, запнулся на одном шаге. В инструкции указано, что для настройки через Podkop нужно включить опцию "принимать маршруты", у меня же этой опции нет, меню дополнительных настроек вообще достаточно скудное.  Так же в инструкциях есть скрин для новых версий Podkop, но он у меня не прогружается((( помогите найти эту настройку.

---

**2026-03-05T10:11:41 | Владимир Волков**
Если на днях прогоняли, то свежая должна быть. Система - пакеты - в фильтрах podkop - вкладка "установленные"

---

**2026-03-05T10:14:57 | Gleb Alekseevich Shumkin**
Странно, система предлагает их установить, хотя Podkop уже установлен. Или я чего то не понимаю))

---

**2026-03-05T12:58:40 | @Dr.Medvedolog**
opkg remove luci-i18n-podkop-ru luci-app-podkop podkop, ну и руками можно пройтись и добить выживших, конфиги sing-box и podkop

---

**2026-03-05T13:47:12 | Роман**
Установить zeroblock/podkop и вставить вашу ссылку.

---

**2026-03-05T15:19:42 | Anna Bagler**
Если совсем не хотите разбираться с zeroblock, то обновиться и скрипт 5, как и раньше, будет вам знакомый podkop.

---

**2026-03-05T16:40:15 | Роман**
Отключить обходы, протестировать. Запрет не меняет локацию, вам нужен zeroblock/podkop.

---

**2026-03-05T19:38:19 | Routerich**
Здравствуйте.
Либо искать домены игр и добавлять их в Podkop / zeroblock, либо полностью устройство в VPN пускать

---

**2026-03-05T19:43:44 | Routerich**
https://podkop.net/docs/sections/#polnostyu-marshrutiziruemye-ip-adresa-fully-routed-ips

---

**2026-03-05T21:34:34 | KyM**
Всё куда надо прописываю согласно мануалу но не помогает. А не может ли мешать podkop, правда он отключен на момент опытов с zapret, но может быть всё ровно как то влиять?

---

**2026-03-05T22:41:08 | Михаил**
Для того, что-бы пустить через byedpi только определенные домены. С помощью podkop или zeroblock.

---

**2026-03-06T12:27:53 | Routerich**
Службы->Podkop->Диагностика->Остановить

---

**2026-03-06T12:31:30 | Anna Bagler**
Либо zb настраивайте и удаляйте podkop, либо zb удаляйте и работайте с podkop.

---

**2026-03-06T13:40:11 | Владимир**
podkop остановлен

---

**2026-03-06T15:27:52 | PavelS**
Ip присвоен, а как в podkop добавить, чет не пойму

---

**2026-03-06T18:23:52 | Ivan Matveev**
Часть сайтов/сервисов под WiFi не хотят открываться в принципе или очень долго, но стоит отключить WiFi и все работает/открывается.
Среди «проблемных» сервисов:
1. Apple (погода, магазин)
2. Sony (приложение ps, магазин ps)
3. Сервисы отслеживания цен на игры вроде ps deals.

LuCI openwrt-24.10 branch 25.302.55195~bfcef12
Podkop Luci App v0.7.14
В основном маршуте в режиме прописан свой впн в режиме прокси.

Создается впечатление, словно сам роутер блочит эти сервисы.

---

**2026-03-06T18:27:16 | Ivan Matveev**
Я в курсе. Я имел ввиду, возможно надо что то в настройках podkopa поменять.

---

**2026-03-06T20:03:06 | Александр Сергеевич**
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.6.196 | YouTube IP:  198.18.0.11
  Программы в автозапуске: podkop

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop               main (vpn): !_cloudflare,discord,google_ai,google_play,meta,ovh,telegram,twitter,geoblock,block,youtube,hdrezka,cloudfront,digitalocean,hodca,hetzner
  podkop DNS/Bootstrap DNS: 9.9.9.9 / 77.88.8.8
  Полностью маршрутизированные IP-адреса включены!
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.51 | RAM: 25% | NAND: 26% занято / 50.1M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

root@RouteRich:~# 
подскажите тут всё нормально ? Несколько дней борюсь с тормозами, вчера добавил cdn для udemy, вроде заработало, сегодня опять и в добавок ещё и youtube отвалился. Уже думаю, может на zeroblock перейти, может лучше станет ?

---

**2026-03-06T22:34:50 | Netizen**
ребят, только сегодня получил роутер. в zeroblock можно засунуть свою подписку или vless конфиг или это только через podkop?

---

**2026-03-06T23:02:40 | Routerich**
Здравствуйте.
А если остановить Podkop? Скачивание идёт?

---

**2026-03-07T07:14:25 | Routerich**
Здравствуйте. 
Как отследите все домены, добавите их в пользовательские домены Podkop

---

**2026-03-07T08:08:10 | Ярослав Онищенко**
Приветствую
Прошу сильно не пинать, только разбираюсь. Никак не могу заставить работать роблокс. Использую podkop и zapret2
Много находил, что в подкопе надо просто выбрать список роблокс, но его больше не вижу
Я попробовал определить его домены через впн + f12 в браузере, вкинул список в podkop в строке "Список пользовательских доменов". Сайт роблокса вроде грузится, даже запустил приложение. Но дальше не могу войти ни в одну игру внутри самого роблокса, полагаю какие-то еще домены нужны. И вот тут затуп, не понимаю как мне их выловить
Через запрет вообще не выходит, создал списки с доменами и IP, сделал стратегию - но не работает вообще. В итоге отключил

Нужна помощь разобраться в какую сторону двигаться

---

**2026-03-07T10:01:08 | Aндрей**
А что круче то?

Podkop vs zero block?)

---

**2026-03-07T11:46:37 | Сущенко Валерий**
Подскажите, пожалуйста, в Podkop в таблице Сообщества список Meta - ВЫБРАН, но WhatsAppна смартфоне не работает при включенном Мобильном интернете и Wi Fi  от Роутера. Это причина в настройках Роутера или Смартфона.

---

**2026-03-07T12:51:51 | Андрей Рыжков**
Добрый день. Сегодня около 11 часов отвалился vpn. Podkop перезапуска л, роутер перезагружал.

---

**2026-03-07T15:34:18 | Евгений**
Podkop

---

**2026-03-07T15:55:19 | Igor**
Первую ссылку копировать? "Код для запуска по умолчанию с автоматической генерацией AWG WARP и установкой Podkop"

---

**2026-03-07T19:14:34 | Igor**
= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.7 | YouTube IP:  108.177.14.136

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓0.00 MB / ↑0.22 MB
  Пинг (ya.ru via awg10): ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (77.88.55.242): 56 data bytes
  Программы в автозапуске: podkop zapret

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОФЛАЙН
------------------------------------------------------
  curl: (28) Connection timed out after 5000 milliseconds
  Warning: Problem : timeout. Will retry in 1 seconds. 3 retries left.
  curl: (28) Connection timed out after 5000 milliseconds
  Warning: Problem : timeout. Will retry in 2 seconds. 2 retries left.
  curl: (28) Connection timed out after 5000 milliseconds
  Warning: Problem : timeout. Will retry in 4 seconds. 1 retries left.
  curl: (28) Connection timed out after 5000 milliseconds
------------------------------------------------------
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 108.177.14.91
    Name:       youtube.com
    Address: 108.177.14.136
    Name:       youtube.com
    Address: 108.177.14.93
    Name:       youtube.com
    Address: 108.177.14.190
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai,discord,telegram
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.2.1 (Прошивка: 24.10.5)
  CPU: 0.06 | RAM: 22% | NAND: 26% занято / 50.2M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-03-07T20:36:11 | Алексей [markartr]**
Сделал, снял логи подкопа 
+ сделал диагностику 

Как-будто по таймауту падаю, кто-нибудь сталкивался с такой проблемой? 

Sat Mar  7 20:26:33 2026 user.notice podkop: [info] Nice
Sat Mar  7 20:26:33 2026 user.notice podkop: [info] 🔄 Starting lists update...
Sat Mar  7 20:26:33 2026 user.notice podkop: [info] Backup dnsmasq configuration
Sat Mar  7 20:26:33 2026 user.notice podkop: [info] ✅ DNS check passed
Sat Mar  7 20:26:33 2026 user.notice podkop: [info] Configure dnsmasq for sing-box
Sat Mar  7 20:26:33 2026 daemon.err podkop[17581]: udhcpc: started, v1.36.1
Sat Mar  7 20:26:33 2026 daemon.err podkop[17581]: udhcpc: broadcasting discover
Sat Mar  7 20:26:36 2026 daemon.err podkop[17581]: udhcpc: no lease, failing
Sat Mar  7 20:26:38 2026 user.notice podkop: [info] GitHub is unavailable [1/10] (max-timeout=5)
Sat Mar  7 20:26:43 2026 daemon.err sing-box[18035]:  [33mWARN [0m[0010] router: initialize rule-set take too much time to finish!

---

**2026-03-07T20:37:40 | Алексей [markartr]**
Доп логи:



Sat Mar  7 20:26:46 2026 user.notice podkop: [info] GitHub is unavailable [2/10] (max-timeout=6)
Sat Mar  7 20:26:48 2026 daemon.err sing-box[18035]:  [31mFATAL [0m[0015] start service: initialize rule-set[0]: initial rule-set: main-russia_inside-community-ruleset: Get "https://github.com/itdoginfo/allow-domains/releases/latest/download/russia_inside.srs": net/http: TLS handshake timeout
Sat Mar  7 20:26:54 2026 user.notice podkop: [info] GitHub is unavailable [3/10] (max-timeout=7)
Sat Mar  7 20:27:02 2026 user.notice podkop: [info] GitHub is unavailable [4/10] (max-timeout=8)
Sat Mar  7 20:27:03 2026 daemon.err sing-box[18364]:  [33mWARN [0m[0010] router: initialize rule-set take too much time to finish!
Sat Mar  7 20:27:08 2026 daemon.err sing-box[18364]:  [31mFATAL [0m[0015] start service: initialize rule-set[0]: initial rule-set: main-russia_inside-community-ruleset: Get "https://github.com/itdoginfo/allow-domains/releases/latest/download/russia_inside.srs": net/http: TLS handshake timeout
Sat Mar  7 20:27:10 2026 user.notice podkop: [info] GitHub is unavailable [5/10] (max-timeout=9)
Sat Mar  7 20:27:18 2026 user.notice podkop: [info] GitHub is unavailable [6/10] (max-timeout=10)
Sat Mar  7 20:27:24 2026 daemon.err sing-box[18549]:  [33mWARN [0m[0010] router: initialize rule-set take too much time to finish!
Sat Mar  7 20:27:26 2026 user.notice podkop: [info] GitHub is unavailable [7/10] (max-timeout=10)
Sat Mar  7 20:27:29 2026 daemon.err sing-box[18549]:  [31mFATAL [0m[0015] start service: initialize rule-set[0]: initial rule-set: main-russia_inside-community-ruleset: Get "https://github.com/itdoginfo/allow-domains/releases/latest/download/russia_inside.srs": net/http: TLS handshake timeout
Sat Mar  7 20:27:34 2026 user.notice podkop: [info] GitHub is unavailable [8/10] (max-timeout=10)
Sat Mar  7 20:27:42 2026 user.notice podkop: [info] GitHub is unavailable [9/10] (max-timeout=10)
Sat Mar  7 20:27:44 2026 daemon.err sing-box[18797]:  [33mWARN [0m[0010] router: initialize rule-set take too much time to finish!
Sat Mar  7 20:27:49 2026 daemon.err sing-box[18797]:  [31mFATAL [0m[0015] start service: initialize rule-set[0]: initial rule-set: main-russia_inside-community-ruleset: Get "https://github.com/itdoginfo/allow-domains/releases/latest/download/russia_inside.srs": net/http: TLS handshake timeout
Sat Mar  7 20:27:50 2026 user.notice podkop: [info] GitHub is unavailable [10/10] (max-timeout=10)
Sat Mar  7 20:27:53 2026 user.notice podkop: [info] ❌ GitHub connection check failed after 10 attempts
Sat Mar  7 20:28:04 2026 daemon.err sing-box[18854]:  [33mWARN [0m[0010] router: initialize rule-set take too much time to finish!
Sat Mar  7 20:28:09 2026 daemon.err sing-box[18854]:  [31mFATAL [0m[0015] start service: initialize rule-set[0]: initial rule-set: main-russia_inside-community-ruleset: Get "https://github.com/itdoginfo/allow-domains/releases/latest/download/russia_inside.srs": net/http: TLS handshake timeout
Sat Mar  7 20:28:24 2026 daemon.err sing-box[19005]:  [33mWARN [0m[0010] router: initialize rule-set take too much time to finish!
Sat Mar  7 20:28:29 2026 daemon.err sing-box[19005]:  [31mFATAL [0m[0015] start service: initialize rule-set[0]: initial rule-set: main-russia_inside-community-ruleset: Get "https://github.com/itdoginfo/allow-domains/releases/latest/download/russia_inside.srs": net/http: TLS handshake timeout
Sat Mar  7 20:28:29 2026 daemon.info procd: Instance sing-box::sing-box.main s in a crash loop 6 crashes, 16 seconds since last crash

---

**2026-03-07T20:46:48 | Kirill Y**
Здраствуйте! А если с podkop переходить в zeroblock, то надо до заводских сбрасывать? Или просто добавлять?

---

**2026-03-07T20:53:25 | Nikita Bekmemetev**
Доброго времени суток. Если ставил podkop через терминал ссылкой, то что делать о какой ручной настройке идёт речь?

---

**2026-03-07T22:27:53 | Nikita Bekmemetev**
Я хочу просто podkop один сервер RUS второй EU чтобы дискорд на EU а Ютуб на RUS

---

**2026-03-07T22:42:18 | Nikita Bekmemetev**
Видос от "Давайте про IT" установил podkop купил два сервака один RUS для YT так как YT блочат со стороны России А второй EU для Discord

---

**2026-03-07T22:42:59 | Vlad**
Всем привет. Только взял роутер пытаюсь разобраться в функционале. Столкнулся с проблемой что ютуб работает только на пк через ютубанблок, а на телевизоре LG не хочет открываться, правильно понимаю что сейчас единственный путь это купить vless ключ и установить в podkop или можно как-то проще ?

---

**2026-03-07T22:47:19 | Роман**
podkop.net ставьте подкоп тогда, одним скриптом.

---

**2026-03-07T22:52:58 | Nikita Bekmemetev**
Это что то похожее? я смогу там разобраться? Про Podkop я хоть видео смотрел

---

**2026-03-07T23:01:02 | Nikita Bekmemetev**
Podkop sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)

---

**2026-03-08T09:31:44 | Routerich**
mixed proxy в zb или podkop

---

**2026-03-08T12:50:35 | Роман**
Здравствуйте, ссылки вида ss:// можно использовать в zeroblock/podkop, как и конфиги амнезии.

---

**2026-03-08T13:48:25 | Сергей**
Подскажите как остановить podkop. В меню нету кнопки остановки сервиса. Также не понятно как сохранить настройки для обоих конфигураций URL подключения и URL Test. Когда переключаешься настройки серверов слетают

---

**2026-03-08T13:51:13 | Михаил**
Меню - система-автозапуск-podkop- стоп
Для сохранения настроек url -сохранить и потом применить.

---

**2026-03-08T15:03:34 | Routerich**
opkg remove luci-i18n-podkop-ru luci-app-podkop podkop

---

**2026-03-08T17:33:22 | ZЁма**
Периодически пытаюсь переходить на ZB с Podkop и периодически какие-то проблемы у ZB. Не исключено, что мне не хватает мозгов настроить списки у ZB, но их вполне хватает для настройки Podkop.

---

**2026-03-08T17:39:15 | Routerich**
Или перейдите на списки v1, там как в Podkop они

---

**2026-03-08T19:36:13 | Routerich**
Здравствуйте.
Службы->Podkop->режим proxy->URL ключ->туда вставить свой ключ

---

**2026-03-08T19:36:35 | Д К ||**
тут нет PodKop

---

**2026-03-08T19:37:27 | Routerich**
https://podkop.net/docs/sections/

---

**2026-03-08T20:41:06 | Routerich**
Добавить  тик ток в Podkop

---

**2026-03-08T22:42:25 | Роман**
Установить zeroblock/podkop, настроить, присвоить приставке постоянный ip и пустить её в полный прокси.

---

**2026-03-09T07:50:01 | Routerich**
Ещё в настройках Podkop поставить галочку
Dont Touch My DHCP

---

**2026-03-09T10:02:17 | Garfield**
Вопрос частично не про RR, но все таки ситуация такая: 
RR + podkop: все ок
Другой роутер на owrt + podkop: в firefox не грузит то, что должно через podkop идти, пока не отключишь безопасный DNS в настройках firefox.  (при этом в хром все ок).

я немного запутался в механиках DNS. может кто нибудь объяснить в чем проблема ?

---

**2026-03-09T10:23:49 | Роман**
По диагностике всё хорошо. 
Можно сменить podkop DNS на 9.9.9.9 и bootstrap DNS на Яндекс например.

---

**2026-03-09T10:42:55 | Anna Bagler**
Ну, рутрекер работает через zeroblock/podkop, для zapret2 надо стратегию подбирать. Что у вас стояло до обновления прошивки?

---

**2026-03-09T11:13:54 | Александр**
Подскажите пожалуйста.  Speedtest ни в какую не загружается, уже все домены добавил в списки, игрался по-разному, один фиг не прогружается страница. Куда копать можно?
Стоит zapret2+podkop

---

**2026-03-09T11:15:22 | Александр**
Zapret2/podkop

---

**2026-03-09T15:05:58 | Дмитрий П**
есть у кого нибудь проблемы с выполнением opkg update сегодня? у меня не срабатывает ни через веб-морду, ни через консоль. В веб морде выдает ошибку Невозможно выполнить команду opkg update: SyntaxError: Unexpected end of JSON input. РОутер я уже и перезагружал через веб морду, и передёргивал вилку питания и даже перепрошил на последнюю версию прошивки. Ошибка никуда не ушла. БОлее того сейчас хотел поставить на свежую прошивку подкоп и вылезла ошибка: 
Downloading 'https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh'
Connecting to 185.199.109.133:443
Connection error: Connection timed out.
Прошу помощи, подскажите с чем может быть связано? Все репозитории решили упасть или что?

Доступ в интернет при этом есть

---

**2026-03-09T16:12:57 | Роман**
Установить zeroblock/podkop, настроить, вставить свою ссылку.

---

**2026-03-09T16:15:24 | J Khan**
Это либо zeroblock, либо podkop установить? Правильно понимаю?

---

**2026-03-09T19:24:09 | Alex_ogg**
Доброго дня!
буквально полчаса назад умер awg интерфейс.
Секция КВН в Podkop не работает естественно.

Времени сидеть разбираться особо нет, инетом 2 квартиры пользуются.

Отсюда пара вопросов:
1. Имеет ли смысл запускать beta версию скрипта №5 или достаточно попробовать заново запустить из этой ветки 5-й скрипт?
2. Ну и если умер интерфейс, какова вероятность, что переустановка подкопа поможет?

---

**2026-03-10T03:09:51 | Олег Б**
Подскажите чем ZB лучше podkop? Ну и в целом в чем разница?

---

**2026-03-10T06:13:31 | Routerich**
Здравствуйте. 
А если остановить Podkop, то вылеты прекращаются?

---

**2026-03-10T06:14:55 | Routerich**
Службы->Podkop->Диагностика->Остановить

---

**2026-03-10T07:39:00 | Михаил**
В zeroblock подписки можно использовать. Список ссылок в https. У podkop этого нет.

---

**2026-03-10T08:22:26 | Routerich**
нет, главное чтобы домены не пересекались между Podkop и zapret2

---

**2026-03-10T08:26:58 | Routerich**
вот почитайте про URLTest
в ZB аналогично
https://podkop.net/docs/sections/

---

**2026-03-10T08:29:39 | Routerich**
не понятно.
в Podkop можно добавить ip подсети для проксирования и всё.
узнайте более детально и приходите, либо спросите у тех, кто это предлагает как сделать

---

**2026-03-10T09:06:33 | Routerich**
так же как и в Podkop.

---

**2026-03-10T09:10:28 | Anna Bagler**
podkop.net Секции

---

**2026-03-10T09:34:28 | Routerich**
они путь сменили
https://github.com/KharunDima/whatsapp-lists?tab=readme-ov-file#-%D0%B4%D0%BB%D1%8F-podkop

---

**2026-03-10T10:17:37 | Routerich**
https://podkop.net/docs/settings/#isklyuchennye-iz-marshrutizacii-ip-adresa-routing-excluded-ips

---

**2026-03-10T10:21:55 | Dmitrii Yurevich**
Я присвоил IP компютеру 192.168.0.143, и этот ip в Podkop в вкладке настройки в самом низу добавляю, так?

---

**2026-03-10T13:31:00 | Routerich**
https://podkop.net/docs/dev/singbox-vs-xray-vs-mihomo/

---

**2026-03-10T14:21:28 | Routerich**
https://github.com/itdoginfo/podkop/releases

---

**2026-03-10T16:44:35 | Роман**
https://podkop.net/docs/troubleshooting/

---

**2026-03-10T17:17:39 | Astro768**
Нужно ли выключить podkop если я скачал Zapret2?

---

**2026-03-10T17:32:51 | Astro768**
А если я отключу podkop и включу zapret2, так будет работать? Просто зачем мне вообще zapret2 если есть подкоп? Объясните пожалуйста.

---

**2026-03-10T17:48:30 | ギン**
0 4 * * * service zapret restart
13 9 * * * /usr/bin/podkop list_update

---

**2026-03-10T17:59:21 | Роман**
Я например предпочитаю не нагружать VPS и не гонять через него ютуб в 4к, ведь ютуб можно пустить через запрет2 вместе с дискордом. Для остального ZB/podkop.

---

**2026-03-10T19:18:50 | Nikolay Barkalov**
подскажите 
DNS проверки
Обнаружены проблемы
Bootstrap DNS
8.8.8.8
Основной DNS
8.8.8.8 [doh]
DNS на роутере
DHCP содержит DNS сервер 

ошибка  "DHCP содержит DNS сервер"  в Настройки podkop что делать?

---

**2026-03-10T19:20:00 | Артём Фомин**
Здравствуйте.
Здесь вы продаёте?
https://ozon.ru/t/8qkfpvV

Если это так, скажите пожалуйста, какие будут характеристики при заказе на данный момент? Просто читаю "Вопросы о товаре" и там ответы разные.

Хотелось бы знать, какой процессор на данный момент стоит, сколько оперативной памяти, какая версия USB и какая будет установлена прошивка?

Если прошивка от OpenWrt, то как полагаю, там какая-то специальная сборка? Хотелось бы знать версию OpenWrt и смогу ли я там установить podkop (https://podkop.net/docs/install/)?

---

**2026-03-10T19:32:05 | Роман**
Тогда велика возможность что заработает запрет2. Если youyubeunblock не сработал. Затем, если запрет 2 с несколькими стратегиями не помог, можно попробовать запрет 1. Если и это не поможет - ZeroBlock/podkop.

---

**2026-03-10T21:22:41 | Роман**
Попробуйте ссылки сменить. Разницы то нет, что zeroblock, что podkop - средства маршрутизации.

---

**2026-03-10T23:36:01 | Routerich**
а я понять не могу, почему ошибки синга, но зб падает на запуске
Tue Mar 10 17:39:22 2026 user.notice podkop: [debug] '# This File Date  : 2025-12-18 00:51:31' is not IPv4 or IPv4 CIDR
Tue Mar 10 17:39:22 2026 user.notice podkop: [debug] '# Update Frequency: 24 hours' is not IPv4 or IPv4 CIDR
Tue Mar 10 17:39:22 2026 user.notice podkop: [debug] '# Entries         : 229' is not IPv4 or IPv4 CIDR
Tue Mar 10 17:39:22 2026 user.notice podkop: [debug] '#' is not IPv4 or IPv4 CIDR
Tue Mar 10 17:39:22 2026 user.notice podkop: [debug] '# (C) 2011-2025 HybridNetworks Ltd. -- All Rights Reserved' is not IPv4 or IPv4 CIDR
Tue Mar 10 17:39:22 2026 user.notice podkop: [debug] '#' is not IPv4 or IPv4 CIDR
Tue Mar 10 17:39:22 2026 user.notice podkop: [debug] '# ============================================================' is not IPv4 or IPv4 CIDR
Tue Mar 10 17:39:22 2026 user.notice podkop: [debug] '#' is not IPv4 or IPv4 CIDR
Tue Mar 10 17:39:24 2026 user.notice podkop: [debug] Adding 229 elements to nft set podkop_subnets
Tue Mar 10 17:39:24 2026 user.notice podkop: [info] ✅ Lists update completed successfully
Tue Mar 10 23:07:01 2026 daemon.err zeroblock[7348]: [zeroblock] ZeroBlock stopped successfully
Tue Mar 10 23:07:02 2026 user.notice zeroblock: Starting ZeroBlock...
Tue Mar 10 23:07:02 2026 daemon.err zeroblock[7560]: [zeroblock] Starting ZeroBlock(0.7.0-r28)...
Tue Mar 10 23:07:39 2026 daemon.err zeroblock[7560]: [config_builder] Sing-box failed to start within timeout
Tue Mar 10 23:07:39 2026 daemon.err zeroblock[7560]: [zeroblock] Failed to start ZeroBlock
Tue Mar 10 23:10:02 2026 daemon.err zeroblock[8670]: [clash_api] /proxies failed: Error
Tue Mar 10 23:10:13 2026 daemon.warn odhcpd[2785]: No default route present, setting ra_lifetime to 0!
Tue Mar 10 23:17:56 2026 daemon.warn odhcpd[2785]: No default route present, setting ra_lifetime to 0!
Tue Mar 10 23:18:29 2026 daemon.err uhttpd[2982]: [info] luci: accepted login on /admin/services/podkop for root from 192.168.1.165
Tue Mar 10 23:21:26 2026 daemon.err sing-box[7591]:  [31mERROR [0m[0859] [ [38;5;72m838382392 [0m 0ms] router: UDP is not supported by outbound: main-out
Tue Mar 10 23:21:26 2026 daemon.err sing-box[7591]:  [31mERROR [0m[0860] [ [38;5;120m2648276840 [0m 0ms] router: UDP is not supported by outbound: main-out
Tue Mar 10 23:21:26 2026 daemon.err sing-box[7591]:  [31mERROR [0m[0860] [ [38;5;30m4157589262 [0m 0ms] router: UDP is not supported by outbound: main-out
ue Mar 10 23:07:02 2026 daemon.err zeroblock[7560]: [zeroblock] Starting ZeroBlock(0.7.0-r28)...
Tue Mar 10 23:07:39 2026 daemon.err zeroblock[7560]: [config_builder] Sing-box failed to start within timeout
Tue Mar 10 23:07:39 2026 daemon.err zeroblock[7560]: [zeroblock] Failed to start ZeroBlock
Tue Mar 10 23:10:02 2026 daemon.err zeroblock[8670]: [clash_api] /proxies failed: Error
Tue Mar 10 23:10:13 2026 daemon.warn odhcpd[2785]: No default route present, setting ra_lifetime to 0!
Tue Mar 10 23:17:56 2026 daemon.warn odhcpd[2785]: No default route present, setting ra_lifetime to 0!
Tue Mar 10 23:18:29 2026 daemon.err uhttpd[2982]: [info] luci: accepted login on /admin/services/podkop for root from 192.168.1.165
Tue Mar 10 23:21:30 2026 daemon.err sing-box[7591]:  [31mERROR [0m[0863] [ [38;5;96m1637773392 [0m 0ms] router: UDP is not supported by outbound: main-out
Tue Mar 10 23:25:48 2026 daemon.warn odhcpd[2785]: No default route present, setting ra_lifetime to 0!

---

**2026-03-10T23:42:13 | Den Kihot**
в смысле не удалять (пакет podkop), а только остановить этот процесс

---

**2026-03-10T23:51:47 | HiLLL**
удали подкоп от греха подальше
service podkop stop
opkg remove luci-i18n-podkop-ru luci-app-podkop podkop

---

**2026-03-11T02:04:16 | Артём Фомин**
Да мне нужен только podkop, который я самостоятельно установлю. В остальном хотелось бы, чтобы была просто чистая OpenWRT без лишних патчей. Необходимо, чтобы просто стабильно работал интернет через wi-fi и lan

---

**2026-03-11T08:17:40 | Сергей**
Добрый день
Возможно ли как то настроить роутинг на определенные каналы Youtube (их url адреса) через конкретные vpn-серверы? 
Известно что есть каналы которые ограничивают контент по гео, типичный пример - официальный f1 channel - для "неправильных" юзеров показываются видео только годовой давности (причем не только российских), а для "правильных" свежак. Решается это vpn из правильной страны, но даже это не всегда помогает и не понятно по какому принципу это работает, например, с одного французкого сервера все ок, с другого - режется
YT трафик идет через пул серверов в podkop, и тут не угадаешь какой он выберет автоматом по минимальному пингу, контент может и не отображаться если сервер "неправильный"
Какими доступными средствами это можно настроить?

---

**2026-03-11T09:14:06 | Роман**
https://podkop.net/docs/troubleshooting/

---

**2026-03-11T10:56:22 | Alexey Tselishchev**
Не могу что-то разобраться. А чем принципиально zeroblock отличается от podkop? Подскажите пожалуйста

---

**2026-03-11T11:33:46 | Alex**
Установил скрипт номер 5, который подразумевает для части ресурсов zapret, а для части podkop(vpn)

Все отлично работает на устройствах из локальной сети.
Если я подключаюсь к роутеру через VPN (сервер AmneziaWG на роутере), трафик проходит через zapret, но не через podkop. В какую сторону копать для решения проблемы?

В веб-интерфейсе http://routerich.lan/cgi-bin/luci/admin/services/podkop при подключении через VPN пишет "браузер не использует FakeIP"

Разобрался: в настройках Podkop нужно было добавить интерфейс AmneziaWG в Source Network Interface.

---

**2026-03-11T13:52:50 | Routerich**
Здравствуйте.
Вполне, добавить его домены в Podkop.

---

**2026-03-11T19:19:46 | Routerich**
у вас что-то непонятное с журналом, там пробел в сутки, но это пол беды. роутер не считает что у вас есть проблемы, т.е. интернет не пропадает, по крайней мере именно интернет. когда проблема снова проявится попробуйте перезапустить podkop или остановить его, если это поможет, то будем дальше разбираться, и после остановки/перезапуска снова пришлите системный лог

---

**2026-03-11T19:28:56 | Виктор**
Добрый вечер! После установки Podkop над ним появилось сообщение об ошибке:

Podkop Error
Wed Mar 11 19:10:41 2026 user.notice podkop: [error] Detected https-dns-proxy in DHCP config. Edit /etc/config/dhcp

Подскажите пожалуйста, как исправить ситуацию. Спасибо.

---

**2026-03-11T19:38:44 | Фома Кузьмич**
Подскажите zeroblock кушает vless/xhttp url конфигурацию или только vless/tcp? 
у меня сейчас подкоп 0.7.10 стоит и он xhttp в прокси режиме не хочет кушать ругаеся с ошибкой user.notice podkop [error] Unknown transport 'xhttp' detected

---

**2026-03-11T20:29:08 | Роман**
Странно, обычно такое поле скриптов бывает. Много настроили? Я бы сделал сброс и установил скриптом с podkop.net

---

**2026-03-11T20:32:21 | Roman Krysin**
Не, ну я конечно в podkop прописал домен )

---

**2026-03-11T21:00:14 | Routerich**
здравствуйте
c wifi все хорошо
вам в другую ветку, учитывая что у вас podkop вероятно отвал DNS

---

**2026-03-11T21:29:37 | Алексей**
Что-бы podkop принял xhttp надо обновить sing-box (https://github.com/EikeiDev/OpenWRT-sing-box-extended) и скорвертировать ссылку в JSON (https://github.com/EikeiDev/vless-xtls-converter/blob/main/index.html)

---

**2026-03-11T22:07:50 | None**
здравствуйте
c wifi все хорошо
вам в другую ветку, учитывая что у вас podkop вероятно отвал DNS

---

**2026-03-11T22:44:02 | Дмитрий**
Если в podkop вот так

---

**2026-03-11T23:39:16 | Михаил**
Ага. И то и то. Причем на двух роутерах - основном и экспериментальном. Podkop в стопе, zero в работе. Ситуация требует. Завтра zb забьет на V1 и оставит только V2  для rr, и чего? С голым задом что ли остаться?

---

**2026-03-12T08:41:00 | Дмитрий**
Спасибо! Конечно. Я выше скинул скрин проблемы с podkop. Можно ли через терминал сменить dns в podkop на quad?

---

**2026-03-12T09:09:58 | Дмитрий**
Podkop

---

**2026-03-12T09:53:18 | Viza**
Добрый день.Подскажите как остановить podkop.

---

**2026-03-12T10:44:37 | Павел**
у меня сегодня podkop/sing-box умер на одном RR. Перезагрузка не помогает, улетает в 100% загрузки процессора и не возвращается. Перезагрузка не помогает. А всего 3 дня отработал

---

**2026-03-12T15:46:47 | Андрей Стыврин**
1) Да
2) Podkop
3) Панель управления тейлом на устройстве? Там Use Tailscale DNS отключен

---

**2026-03-12T16:34:29 | Vkom11**
Исправил, нужно было в Podkop выбрать из списка ютубчик и применить.
Спасибо за помощь.

---

**2026-03-12T16:37:28 | Андрей Стыврин**
На РР стоял zapret (Z) и podkop (P), всё работало, решил поставить ZB. Для этого остановил эти сервисы, установил ZB (Z2 был установлен ранее и был остановлен), запустил автоконфигурацию, запустил ZB и Z2, ни один сайт не открывается.
Остановил ZB и Z2, запустил Z и P, снова заработало.
Внимание, вопрос, как заставить работать ZB при остановленных Z и P?

---

**2026-03-12T16:47:15 | Vasa**
тема Zeroblock или Интернет без границ (podkop)

на выбор варианты

---

**2026-03-12T17:16:10 | Роман**
Если вы хотите распространить обход на все устройства в доме, а не запускать на каждом локально, лучше взять роутер. 
Ну установите вы ВПН на VPS, и придется на каждое устройство ставить клиенты. А так установил на роутер zeroblock/podkop, вписал туда свой ключ vless, и все устройства уже с обходами.

---

**2026-03-12T17:20:01 | Роман**
Повторюсь, связка podkop/zapret1/2 работает. Zeroblock/zapret2/1 тоже работает. 
А что вам удобнее - ваш выбор.

---

**2026-03-12T20:12:31 | Роман**
https://podkop.net/docs/troubleshooting/
Здравствуйте. Тут посмотрите.

---

**2026-03-12T20:17:31 | Dmitriy M 🎃**
```undefined
 [0;36m[2026-03-12 20:10:13] [0m  [0;32mCurrent sing-box configuration: [0m
{
  "log": {
    "disabled": false,
    "level": "warn",
    "timestamp": false
  },
  "dns": {
    "servers": [
      {
        "type": "udp",
        "tag": "bootstrap-dns-server",
        "server": "MASKED",
        "server_port": "MASKED"
      },
      {
        "type": "udp",
        "tag": "dns-server",
        "server": "MASKED",
        "server_port": "MASKED"
      },
      {
        "type": "fakeip",
        "tag": "fakeip-server",
        "inet4_range": "198.18.0.0/15"
      }
    ],
    "rules": [
      {
        "action": "reject",
        "query_type": "HTTPS"
      },
      {
        "action": "reject",
        "domain_suffix": "use-application-dns.net"
      },
      {
        "action": "route",
        "server": "MASKED",
        "rewrite_ttl": 60,
        "domain": [
          "fakeip.podkop.fyi",
          "ip.podkop.fyi"
        ],
        "rule_set": [
          "main-discord-community-ruleset",
          "main-google_ai-community-ruleset",
          "main-meta-community-ruleset",
          "main-russia_inside-community-ruleset",
          "main-telegram-community-ruleset",
          "main-user-domains-ruleset"
        ]
      }
    ],
    "final": "dns-server",
    "strategy": "ipv4_only",
    "independent_cache": true
  },
  "ntp": {},
  "certificate": {},
  "endpoints": [],
  "inbounds": [
    {
      "type": "tproxy",
      "tag": "tproxy-in",
      "listen": "127.0.0.1",
      "listen_port": 1602,
      "tcp_fast_open": true,
      "udp_fragment": true
    },
    {
      "type": "direct",
      "tag": "dns-in",
      "listen": "127.0.0.42",
      "listen_port": 53
    }
  ],
  "outbounds": [
    {
      "type": "direct",
      "tag": "direct-out"
    },
    {
      "type": "hysteria2",
      "tag": "main-out",
      "server": "MASKED",
      "server_port": "MASKED",
      "password": "MASKED",
      "obfs": {
        "type": "salamander",
        "password": "MASKED"
      },
      "tls": {
        "enabled": true,
        "server_name": "MASKED"
      }
    }

---

**2026-03-12T23:51:21 | Латентный Сантехник**
у меня есть круче скриншота....

Анализ запущен: 2026-03-12 23:46:20
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   100.100.100.100:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.31 | YouTube IP:  198.18.0.32

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓0.20 MB / ↑0.19 MB
  Пинг (ya.ru via awg10): 113.198 / 115.294 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | STOPPED (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop    Youtube_Discord (vpn): youtube,discord,telegram
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.25 (Прошивка: 24.10.5)
  CPU: 1.70 | RAM: 25% | NAND: 27% занято / 49.2M доступно
  !!!_WatchDoc установлен

---

**2026-03-13T08:14:59 | Андрей**
добрый день. А не подскажете можно ли как-то на podkop настроить anydesk? а то он вообще последнее время ужасно работает

---

**2026-03-13T09:59:54 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.1-r30:
Новые возможности
  - Поддержка протокола AnyTLS + распознавание hysteria2/hy2/anytls в подписках
  - Unified user_lists — объединение доменов и IP в один список с автоопределением типа, поддержка nft sets и grouped JSON
  - Автоконвертация grouped JSON доменов в sing-box ruleset формат
  - Messengers force_cidr — фильтрация только telegram.org IP при неявном CIDR
  - Fallback API для WARP — автоматический retry через резервный сервер
  - Переименована кнопка добавления секции в LuCI
  - Выбор URL для проверки в Settings(приоритет per-section → global → fallback gstatic)
  - Детекция /etc/init.d/podkop при старте с LOG_ERR предупреждением
  - singbox_startup_timeout (5-300с, default 30с) и xray_startup_timeout (1-120с, default 10с) вынесены в UCI
  - YACD кнопка readonly без secret
  - Выбор URL для проверки задержки (Google, Cloudflare, Huawei, Microsoft) — или свой
  - Поддержка reverse proxy (nginx + HTTPS) — dashboard работает за SSL без mixed content

  Исправления
  - Bootstrap DNS: убран ложный warning при UDP, исправлен маппинг dns_bootstrap для секций, bootstrap-dns не создаётся в конфиге когда не нужен
  - Clash API: переход на json-c вместо popen+curl (решён 4K buffer overflow)
  - Xray диагностика: правильные UCI опции + fallback на proxy_string
  - Outbound диагностика: fallback на proxy_string для всех типов
  - Duplicate rule-set tag для URL с одинаковым хостом
  - LuCI: валидатор порта с trailing slash, YACD кнопка readonly без secret, force_update очистка HTTP-кеша
  - SS Outline URL parsing
  - Парсинг URLTest ссылок с пробелами и эмодзи в именах

  Рефакторинг
  - Удалены legacy user_domain_lists/user_subnet_lists, добавлена миграция
#ZeroBlock

---

**2026-03-13T10:28:45 | Routerich**
[zeroblock] podkop detected! It may conflict with ZeroBlock routing/nftables rules
отлично

---

**2026-03-13T10:41:08 | Михаил**
Придется изолировать podkop от zb. Роутеры паровозиком, на первом podkop, на втором zb. Тогда точно фиг поймаешь...

---

**2026-03-13T11:25:32 | Vyacheslav Shirshov**
Телега отвалилась, будут какие-то советы или на podkop возвращаться?

---

**2026-03-13T11:40:16 | Михаил**
0.7.1-r30 уже с чисткой uboot для владельцев podkop? :)

---

**2026-03-13T11:42:57 | Ilya ☀️**
Привет! 
Не работает хромвебстор. Подскажите, пожалуйста, как обновить подкоп и поможет ли это.

System information
Podkop
v0.7.9 Outdated
Luci App
v0.7.9
Sing-box
1.12.12
OS
RouteRich 24.10.4 r28959-29397011cc RR-3.8.2
Device
Routerich AX3000

---

**2026-03-13T12:16:27 | Richard (Роман)**
sh <(wget -O - https://raw.githubusercontent.com/routerich/RouterichAX3000_configs/refs/heads/wdoctrack/run_universal_config.sh) n n

Вот это вписать мне нужно? Это без замены конфигурации podkop'a.

---

**2026-03-13T13:17:26 | Роман**
Все блокировки обходите вы, роутер это инструмент. Сможете найти стратегию для запрет 1/2 - обошли блок. Нашли нормального хостера, подняли сервер, закинули ссылку в zeroblock/podkop - обошли блокировки. 
Сам роутер ничего не делает, он даёт широкие возможности из-за своей прошивки, по сути это мини ПК с Линукс на борту который умеет раздавать интернет.

---

**2026-03-13T14:08:55 | Routerich**
https://podkop.net/docs/tunnels/awg_settings/ пункт с установкой пакетов пропускаем, остальное проверяем

---

**2026-03-13T15:42:01 | 👍**
Здравствуйте, как добавить cloudfare в список podkop, чтобы работали сервера в майнкрафт зарубежные. И еще один вопрос: ютуб стал работать медленнее после установки 5 скрипта чем до него, когда достал из коробки

---

**2026-03-13T16:42:13 | Routerich**
https://podkop.net/docs/adguard/ по такому же принципу

---

**2026-03-13T17:09:08 | Владимир Волков**
- А поддержка подкопа закончится?
- Podkop достаточно эффективно работает у большинства пользователей, в том числе и у меня... За судьбу Podkop, я думаю, что можно не беспокоиться

---

**2026-03-13T19:38:59 | Роман**
В списки пользовательских доменов и ip в podkop.

---

**2026-03-13T20:41:22 | Святос**
Это Podkop ж?

---

**2026-03-13T21:35:10 | Илья**
Спасибо,роутер ребутнул,инет поднялся ,но умер podkop

---

**2026-03-13T21:42:52 | Илья**
global_check 
 📡 Global check run!
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛠 System info
🕳 Podkop:        v0.7.14 (latest: 0.7.14)
🕳 LuCI App:      v0.7.14
📦 Sing-box:      1.12.17
🛜 OpenWrt:       RouteRich 24.10.5 r29087-d9c5716d1d RR-3.9.0
🛜 Device:        Routerich AX3000 v1
━━━━━━━━━━━━━━━━━━━━━━━━━━━
➡️ DNS status
✅ Bootstrap DNS: 8.8.8.8
✅ Main DNS: 8.8.8.8 [doh]
✅ DNS on router
⚠️ dont_touch_dhcp is enabled. 📄 DHCP config:
config dnsmasq
  option domainneeded '1'
  option localise_queries '1'
  option rebind_protection '1'
  option rebind_localhost '1'
  option local '/lan/'
  option domain 'lan'
  option expandhosts '1'
  option nonegcache '1'
  option authoritative '1'
  option readethers '1'
  option leasefile '/tmp/dhcp.leases'
  option localservice '1'
  option ednspacket_max '1232'
  option confdir '/tmp/dnsmasq.d'
  option noresolv '1'
  option cachesize '0'
  option strictorder '1'
  option filter_aaaa '1'
  list podkop_server '127.0.0.1#5359'
  option podkop_noresolv '0'
  option podkop_cachesize '150'
  list server '127.0.0.1#5359'

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 Sing-box status
✅ Sing-box installed
✅ Sing-box version is compatible (newer than 1.12.4)
✅ Sing-box service exist
✅ Sing-box autostart disabled
❌ Sing-box process running
❌ Sing-box listening ports
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧱 NFT rules status
✅ Table exist
✅ Rules mangle exist
⚠️  Rules mangle counters
✅ Rules mangle output exist
⚠️  Rules mangle output counters
✅ Rules proxy exist
⚠️  Rules proxy counters
✅ Additional marking rules found
━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 Podkop config

config settings 'settings'
  option dns_type 'doh'
  option dns_server '8.8.8.8'
  option bootstrap_dns_server '8.8.8.8'
  option dns_rewrite_ttl '60'
  option enable_output_network_interface '0'
  option enable_badwan_interface_monitoring '0'
  option enable_yacd '0'
  option disable_quic '1'
  option update_interval '1d'
  option download_lists_via_proxy '1'
  option dont_touch_dhcp '1'
  option config_path '/etc/sing-box/config.json'
  option cache_path '/tmp/sing-box/cache.db'
  option exclude_ntp '1'
  option shutdown_correctly '0'
  option download_lists_via_proxy_section 'main'
  list source_network_interfaces 'br-lan'
  option log_level 'warn'

config section 'main'
  option connection_type 'vpn'
  option shutdown_correctly '1'
  option user_domain_list_type 'text'
  option user_subnet_list_type 'disabled'
  option mixed_proxy_enabled '0'
  option user_domains_text '2ip.ru
google.com'
  option interface 'VPN'
  option domain_resolver_enabled '0'
  list community_lists 'russia_inside'
  list community_lists 'google_play'
  list community_lists 'telegram'

config section 'Youtube_Discord'
  option connection_type 'vpn'
  option interface 'awg10'
  option domain_resolver_enabled '0'
  option user_domain_list_type 'text'
  option user_subnet_list_type 'disabled'
  option mixed_proxy_enabled '0'
  option user_domains_text '2ip.ru amazonaws.com whatsapp.com whatsapp.net whatsapp.biz wa.me'
  list remote_subnet_lists 'https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_cidr_ipv4.txt'
  list community_lists 'youtube'
  list community_lists 'discord'

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 WAN config
config interface 'wan'
  option device 'eth1'
  option proto 'dhcp'

━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ WARP detected: 162.159.192.10
━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ Zapret detected
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🥸 FakeIP status
⚠️ Router DNS is NOT routed through sing-box
❌ Sing-box does NOT work with FakeIP: ;; communications error to 127.0.0.42#53: connection refused
;; communications error to 127.0.0.42#53: connection refused
;; communications error to 127.0.0.42#53: connection refused
;; no servers could be reached

---

**2026-03-13T22:00:39 | Илья**
global_check 
 📡 Global check run!
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛠 System info
🕳 Podkop:        v0.7.14 (latest: 0.7.14)
🕳 LuCI App:      v0.7.14
📦 Sing-box:      1.12.22
🛜 OpenWrt:       RouteRich 24.10.5 r29087-d9c5716d1d RR-3.9.0
🛜 Device:        Routerich AX3000 v1
━━━━━━━━━━━━━━━━━━━━━━━━━━━
➡️ DNS status
✅ Bootstrap DNS: 8.8.8.8
✅ Main DNS: 8.8.8.8 [doh]
✅ DNS on router
⚠️ dont_touch_dhcp is enabled. 📄 DHCP config:
config dnsmasq
  option domainneeded '1'
  option localise_queries '1'
  option rebind_protection '1'
  option rebind_localhost '1'
  option local '/lan/'
  option domain 'lan'
  option expandhosts '1'
  option nonegcache '1'
  option authoritative '1'
  option readethers '1'
  option leasefile '/tmp/dhcp.leases'
  option localservice '1'
  option ednspacket_max '1232'
  option confdir '/tmp/dnsmasq.d'
  option noresolv '1'
  option cachesize '0'
  option strictorder '1'
  option filter_aaaa '1'
  list podkop_server '127.0.0.1#5359'
  option podkop_noresolv '0'
  option podkop_cachesize '150'
  list server '127.0.0.1#5359'

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 Sing-box status
✅ Sing-box installed
✅ Sing-box version is compatible (newer than 1.12.4)
✅ Sing-box service exist
✅ Sing-box autostart disabled
❌ Sing-box process running
❌ Sing-box listening ports
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧱 NFT rules status
✅ Table exist
✅ Rules mangle exist
✅ Rules mangle counters
✅ Rules mangle output exist
⚠️  Rules mangle output counters
✅ Rules proxy exist
✅ Rules proxy counters
✅ Additional marking rules found
━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 Podkop config

config settings 'settings'
  option dns_type 'doh'
  option dns_server '8.8.8.8'
  option bootstrap_dns_server '8.8.8.8'
  option dns_rewrite_ttl '60'
  option enable_output_network_interface '0'
  option enable_badwan_interface_monitoring '0'
  option enable_yacd '0'
  option disable_quic '1'
  option update_interval '1d'
  option download_lists_via_proxy '1'
  option dont_touch_dhcp '1'
  option config_path '/etc/sing-box/config.json'
  option cache_path '/tmp/sing-box/cache.db'
  option exclude_ntp '1'
  option shutdown_correctly '0'
  option download_lists_via_proxy_section 'main'
  list source_network_interfaces 'br-lan'
  option log_level 'warn'

config section 'main'
  option connection_type 'vpn'
  option shutdown_correctly '1'
  option user_domain_list_type 'text'
  option user_subnet_list_type 'disabled'
  option mixed_proxy_enabled '0'
  option user_domains_text 'myip.com'
  option interface 'VPN'
  option domain_resolver_enabled '0'
  list community_lists 'russia_inside'
  list community_lists 'telegram'

config section 'Youtube_Discord'
  option connection_type 'vpn'
  option interface 'awg10'
  option domain_resolver_enabled '0'
  option user_domain_list_type 'text'
  option user_subnet_list_type 'disabled'
  option mixed_proxy_enabled '0'
  option user_domains_text '2ip.ru amazonaws.com whatsapp.com whatsapp.net whatsapp.biz wa.me'
  list remote_subnet_lists 'https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_cidr_ipv4.txt'
  list community_lists 'youtube'

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 WAN config
config interface 'wan'
  option device 'eth1'
  option proto 'dhcp'

⚠️ WARP detected: engage.cloudflareclient.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ Zapret detected
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🥸 FakeIP status
⚠️ Router DNS is NOT routed through sing-box
❌ Sing-box does NOT work with FakeIP: ;; communications error to 127.0.0.42#53: connection refused
;; communications error to 127.0.0.42#53: connection refused
;; communications error to 127.0.0.42#53: connection refused
;; no servers could be reached

---

**2026-03-14T02:09:39 | Артем Рахаев**
Всем привет! Подскажите, у меня на роутере нет Zapret и Podkop, установлен youtubeUnblock, но YouTube не работает. Нужно ли как-то настраивать YU, есть какой-то мануал?

---

**2026-03-14T05:29:48 | Роман**
добрый день подскажите, что может быть накатил 5 скрипт после сброса, с вечера работало, а с утра отвалился подкоп и такая ошибка podkop: [error] Detected https-dns-proxy in DHCP config. Edit /etc/config/dhcp. остановил ютубанблок и запрет. ошибка остается.

---

**2026-03-14T06:52:21 | Artem**
Я извиняюсь, а zeroblock это где? Есть в Podkop списки сообщества, но там games нету...

---

**2026-03-14T07:35:43 | Artem**
Там стоит галочке на списке Messengers. Может где то еще надо отключить, в podkop например?

---

**2026-03-14T07:38:29 | Artem**
Да, в podkop из секции youtube_discord убрал телеграм и заработало)

---

**2026-03-14T10:48:12 | Роман**
В zeroblock/podkop.

---

**2026-03-14T12:57:27 | Сергей**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.1-r30:
Новые возможности
  - Поддержка протокола AnyTLS + распознавание hysteria2/hy2/anytls в подписках
  - Unified user_lists — объединение доменов и IP в один список с автоопределением типа, поддержка nft sets и grouped JSON
  - Автоконвертация grouped JSON доменов в sing-box ruleset формат
  - Messengers force_cidr — фильтрация только telegram.org IP при неявном CIDR
  - Fallback API для WARP — автоматический retry через резервный сервер
  - Переименована кнопка добавления секции в LuCI
  - Выбор URL для проверки в Settings(приоритет per-section → global → fallback gstatic)
  - Детекция /etc/init.d/podkop при старте с LOG_ERR предупреждением
  - singbox_startup_timeout (5-300с, default 30с) и xray_startup_timeout (1-120с, default 10с) вынесены в UCI
  - YACD кнопка readonly без secret
  - Выбор URL для проверки задержки (Google, Cloudflare, Huawei, Microsoft) — или свой
  - Поддержка reverse proxy (nginx + HTTPS) — dashboard работает за SSL без mixed content

  Исправления
  - Bootstrap DNS: убран ложный warning при UDP, исправлен маппинг dns_bootstrap для секций, bootstrap-dns не создаётся в конфиге когда не нужен
  - Clash API: переход на json-c вместо popen+curl (решён 4K buffer overflow)
  - Xray диагностика: правильные UCI опции + fallback на proxy_string
  - Outbound диагностика: fallback на proxy_string для всех типов
  - Duplicate rule-set tag для URL с одинаковым хостом
  - LuCI: валидатор порта с trailing slash, YACD кнопка readonly без secret, force_update очистка HTTP-кеша
  - SS Outline URL parsing
  - Парсинг URLTest ссылок с пробелами и эмодзи в именах

  Рефакторинг
  - Удалены legacy user_domain_lists/user_subnet_lists, добавлена миграция
#ZeroBlock

---

**2026-03-14T13:33:13 | Дмитрий**
Доброго дня, у меня установлен Podkop
v0.7.7 - в самих настройках роутера написано что это устаревшая версия, имеет ли смысл обновлять? И как можно легко и безболезненно обновить?

---

**2026-03-14T13:35:42 | Routerich**
Если всё работает, можете не обновлять. Если сильно хочется, то https://podkop.net/docs/install/

---

**2026-03-14T13:55:24 | Александр**
Подкоп, но UDP в настройках подкопа вместо DoH ломает дискорд.
По этой инструкции https://podkop.net/docs/adguard/ я так понял, нужно менять днс не для подкопа (последний вариант, где agh сам является днс-сервером).
Или я неправильно понял?

---

**2026-03-14T14:06:52 | Александр**
Ну совет про udp был тут, а не там) То есть по совету из чата тут я попытался выполнить схему "AGH как DNS-сервер в Podkop", и она имеет изъяны (в виде отвала дискорда). 
В последней схеме "AGH как DNS-сервер у клиентов", которую я щас пытаюсь воплотить, про udp ни слова, там смена общего днс роутера в секции DHCP на адрес устройства в сети, которое этим новым днс станет, чтобы схема заработала.
А я не могу найти, куда вбить адрес будущего днс в интерфейсе РР. Вот, прошу меня ткнуть в нужном направлении, ибо я или туплю, или да.

---

**2026-03-14T14:23:50 | Routerich**
я не знаю имени подкоповской таблицы, там типа Podkoptable

---

**2026-03-14T14:32:06 | HiLLL**
Podkoptable

---

**2026-03-14T14:45:42 | Routerich**
PodkopTable

---

**2026-03-14T15:30:16 | Роман**
Если устанавливать podkop на zb, то он работает на tiny версии 😁

---

**2026-03-14T16:11:33 | Routerich**
podkop.net/docs/client-dns/#sbertv у сбера есть такие проблемы

---

**2026-03-14T16:42:15 | Роман**
Выбрать список telgram в podkop, или messengers в zeroblock. Или искать прокси для телеги.

---

**2026-03-14T16:45:17 | Роман**
Здравствуйте. Запрет весь трафик модифицирует. А в zeroblock/podkop можно в исключения добавить ip ноутбуков. И это не только на данном роутере, на любом с openwrt.

---

**2026-03-14T17:33:47 | Andrey B.**
вопрос.  1 - запускаю скрипт 2- выбираю амнезия = no (так как у меня нет настроек) 3 - выбираю yes (для установки podkop) ? Надеюсь я правильно понял

---

**2026-03-14T17:52:51 | Andrei Frolov**
Вот как раз хотел понять есть ли это из коробки. Почитал про podkop, теперь вопросов нет.

---

**2026-03-14T18:01:38 | Александр**
спасибо

и ещё подскажите пж насколько сейчас стабильно работает Zapret роутеровский?

ставить Zapret или Podkop?

---

**2026-03-14T18:03:11 | Routerich**
Podkop это средство маршрутизации для впн и прокси уже с готовыми списками, а Zapret это antiDPI служба что модифицирует трафик, их не сравнить. У нас есть Zapret2 с блокчеком - всё стабильно

---

**2026-03-14T18:11:13 | Ильфат Шайдуллин**
Доброго дня. Обновлял podkop (в роутере была надпись,что текущая версия устарела). После обновления интернет пропал. До всех операций создавал образ,но теперь и его загрузка проблему не решает. Куда копать,подскажите.

---

**2026-03-14T19:23:00 | Nikonow**
Почему podkop не ставится ни через консоль по ssh, ни через ipk?

---

**2026-03-14T19:30:24 | Routerich**
А getdomains зачем удаляете? Его и так нет, для подкопа команда sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)

---

**2026-03-14T19:51:31 | Максим**
Телеграм стал сильно тормозить  через awg. Раньше работал хорошо, теперь как-будто напрямую через провайдера им пользуюсь, даже картинки могут не прогружаться , не говоря уже о видео. Awg перезапускал, podkop тоже.

---

**2026-03-14T22:58:17 | Routerich**
https://podkop.net/docs/faq/#kak-napravit-ves-trafik-s-odnogo-ili-vseh-ustrojstv-cherez-vpn-ili-proksi

---

**2026-03-15T00:30:09 | Ильфат Шайдуллин**
И снова здравствуйте. После обновления podkop до версии 0.7.14 пропал доступ на ютуб и остальное.  Вылазят ошибки download **** list failed и в дашборде sing-box остановлен.  Что делать,подскажите

---

**2026-03-15T07:02:07 | Эдуард**
Зашел в Настройки podkop диагностика есть какие то ошибки может они влияют ?

---

**2026-03-15T07:48:29 | Anna Bagler**
Скопируйте домены пользователя пока в текстовый файлик и уберите их из подкопа. Перезапустите opera-proxy и podkop. И ещё раз запустите диагностику.

---

**2026-03-15T08:25:11 | Routerich**
https://podkop.net/docs/faq/#kak-napravit-ves-trafik-s-odnogo-ili-vseh-ustrojstv-cherez-vpn-ili-proksi

---

**2026-03-15T11:11:52 | Monty**
Для человека который только погрузился в это, отключить zapret? или podkop целиком?

---

**2026-03-15T13:35:46 | Роман**
Запрет, запрет2, полное прокси через podkop/zeroblock.
Приставка пс 5
Задача разблокировать то что заблокировано 
И не мешало играть на пс 5 
Не поднимало пинг и не резало скорость скачивания 
То-же самое, прокси поднимет пинг в любом случае.
Разница между скриптои бета и пятым в версии подкопа, и всё.

---

**2026-03-15T14:53:40 | Дмитрий Шаповалов**
Подскажите как добавить адреса тг в zapret или это бессмысленно?
у меня сейчас настроены в podkop все адреса на личный квн, но видео через раз грузит. На vds все адреса пингуются без потерь

---

**2026-03-15T15:19:44 | Роман**
Я на голом запрете 1 тестировал, без podkop/zeroblock/zapret2, всё отключил.

---

**2026-03-15T15:25:46 | Routerich**
https://podkop.net/docs/tunnels/awg_settings/ установку пакетов пропускайте

---

**2026-03-15T16:38:33 | Routerich**
Или начинайте читать мануалы и смотреть видео по подкопу, которых полно на ютубе и не только, или в дальнейшем останетесь без свободного интернета. Сегодня законы такие, завтра ужесточат, и мы не сможем вам с этим помочь. Заходите в службы - podkop  в секции с названием main выбирайте дополнительно список телеграм. Или есть есть секция с названием discord то там. В обе секции добавлять не надо

---

**2026-03-15T17:01:41 | Routerich**
Службы - zapret - отключить автостарт и остановить. Далее службы - podkop, список YouTube из секции с названием main убрать. В секцию с названием дискорд добавить

---

**2026-03-15T17:15:40 | Alexander**
Привет, кто-то настраивал vless xhttp reality для роутера через podkop?

---

**2026-03-15T17:23:01 | Роман**
https://telegra.ph/Polnaya-instrukciya-nastrojki-xHTTP-v-Podkop-12-08

---

**2026-03-15T17:26:49 | Серёга_44rus**
Добрый день, скажите, а в podkop meta это вацап разблокируется?

---

**2026-03-15T18:21:59 | Routerich**
Для установки на свой сервер у амнезии есть инструкция, а для роутера https://podkop.net/docs/tunnels/awg_settings/ этап установки пакетов пропустить

---

**2026-03-15T19:29:51 | Routerich**
https://podkop.net/docs/diagnostics/#fakeip-proverki

---

**2026-03-15T23:17:47 | AndrewKomarov**
я же верно понял, что zeroblock заменяет podkop теперь?

---

**2026-03-15T23:37:49 | Art**
Всем привет, подскажите пожалуйста, можно как-то сделать отдельный вайфай без podkopa?

---

**2026-03-15T23:41:02 | Routerich**
https://podkop.net/docs/faq/#gostevaya-wi-fi-set-i-podkop

---

**2026-03-16T06:44:47 | Routerich**
https://podkop.net/docs/sections/#polnostyu-marshrutiziruemye-ip-adresa-fully-routed-ips

---

**2026-03-16T09:37:51 | Andrey**
Ребята, может у кого было так. Работает маршрутизация через podkop. Все что за пределами РФ - в прокси (vless или hysteria2). Работало все оч стабильно и хорошо, только иногда сервера менял. Потом началась фигня с тем, что на некоторых устройствах работает инет, на других нет (весь инет, не только обход). Предполагаю проблему с DNS. Настраиваю DNS Failsafe как в закрепе и подбираю dns сервера - все начинает работать стабильно, но на прошлой неделе опять такая же борода. Меняю DoT на DoH, меняю dns сервера, даже частные ставлю - все фигня. Причем одновременно может на каких-то устройствах быть хорошо, а на других нифига. Грешу на fakeip и я бы его выключил, но не смог найти как это сделать.

---

**2026-03-16T14:33:48 | User Friendly**
А чем podkop от zeroblock отличается?

---

**2026-03-16T16:46:28 | Routerich**
https://podkop.net/docs/tunnels/awg_settings/ пункт с установкой пакетов пропускайте, остальное проверьте, выбирать свой конфиг в зероблоке по такому же принципу

---

**2026-03-16T17:32:36 | Vladimir Turbin**
здравствуйте .
а zapret2 с podkop совместно будут работать 
если zapret2 на youtube а podkop на все остальное?

---

**2026-03-16T18:01:31 | Ivan Num**
Подскажите в zeroblock в отличии от podkop списки доменов и подсетей автоматически обновляются в сообществе?

---

**2026-03-16T18:03:28 | Anna Bagler**
podkop.net
Изучайте.

---

**2026-03-16T21:16:30 | Routerich**
https://podkop.net/ изучайте

---

**2026-03-16T21:34:21 | Дмитрий Шаповалов**
Может кто скинуть json для opera proxy который идёт со скриптом 5 для podkop?
Я снес и не сохранил

---

**2026-03-16T21:38:38 | Борис**
Здравствуйте. На роутер можно поставить podkop и zapret :)

Ещё можно поставить zeroblock из соседней темы. Но он так же неустойчив к психическим припадкам и может быть опрометчиво удалён в гневе, так что обходы снова перестанут работать...

---

**2026-03-16T21:39:57 | Andrei Frolov**
привет!

подскажите, пожалуйста, в чем может быть дело и куда копать.
проблема - плохо работают звонки через zoom, ktalk, яндекс.телемост. собеседники жалуются, что мой голос заикается и пропадает иногда.

на роутере имеются настроенный podkop (на свой vless) и zapret2. 
пробовал отключать и то и то, но это результата не принесло.
также из podkop'a удалил discord из списков и это тоже не помогло.

и второй момент, который заметил - с включенным zapret2 исходящая скорость срезается в 5 раз (с 500 мбс до 100 мбс). это ок, что так много?

---

**2026-03-16T22:25:51 | Anna Bagler**
Для них нужен zeroblock или podkop.

---

**2026-03-16T23:37:35 | Routerich**
Стоит PodKop?

---

**2026-03-16T23:38:18 | Денис Мальцев**
Подскажите. Никак не хочет работать KinoPUB на AppleTV. На всех других устройствах работает, а на этой приставке нет. Podkop работает, другие приложения, в том числе YouTube, работают. Но, если я включу vpn на Happ, то KinoPUB запускается. Хотя в подкопе стоит ссылка vless на этот же сервер vpn…

---

**2026-03-16T23:46:44 | Evgeny**
а ZERO-block это PODkop?  или они связаны как то?

---

**2026-03-17T01:45:07 | Routerich**
Тогда сделайте проще. Остановите запрет2 и выключите автозапуск. Далее в службы - podkop - секция с названием discord, там добавляйте список YouTube - применить. И проверяйте

---

**2026-03-17T13:35:31 | HiLLL**
попробуйте установить через терминал
sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)

---

**2026-03-17T17:28:04 | Джалиль**
Здравствуйте. Хочу почистить /etc/hosts. Нужно же оставить только первые 4 строки? Интересно, podkop мог делать такие записи в hosts? Ещё подозрение на кастомный скрипт для подбора конфигурации для zapret-а. Интересно стало) 

А то у меня не работал 4pda.to (чтобы писать негативные отзывы😁). Думал, это после перехода на zeroblock с podkop, в yacd даже и соединения не появлялось, а оказалось, что в hosts старый айпишник был.
127.0.0.1 localhost
::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
185.87.51.182 4pda.to www.4pda.to
130.255.77.28 ntc.party
30.255.77.28 ntc.party
173.245.58.219 rutor.info d.rutor.info
185.39.18.98 lib.rus.ec www.lib.rus.ec
57.144.222.34 instagram.com www.instagram.com
157.240.9.174 instagram.com www.instagram.com
157.240.245.174 instagram.com www.instagram.com
157.240.205.174 instagram.com www.instagram.com
#Gemini
45.155.204.190 gemini.google.com
#Grok
45.155.204.190 grok.com accounts.x.ai assets.grok.com
#OpenAI
45.155.204.190 chatgpt.com ab.chatgpt.com auth.openai.com auth0.openai.com platform.openai.com cdn.oaistatic.com
45.155.204.190 tcr9i.chat.openai.com webrtc.chatgpt.com android.chat.openai.com api.openai.com operator.chatgpt.com
45.155.204.190 sora.chatgpt.com sora.com videos.openai.com ios.chat.openai.com cdn.auth0.com files.oaiusercontent.com
#Microsoft
45.155.204.190 copilot.microsoft.com sydney.bing.com edgeservices.bing.com rewards.bing.com
45.155.204.190 xsts.auth.xboxlive.com xgpuwebf2p.gssv-play-prod.xboxlive.com xgpuweb.gssv-play-prod.xboxlive.com
#ElevenLabs
45.155.204.190 elevenlabs.io api.us.elevenlabs.io elevenreader.io api.elevenlabs.io help.elevenlabs.io
#DeepL
45.155.204.190 deepl.com www.deepl.com www2.deepl.com login-wall.deepl.com w.deepl.com dict.deepl.com ita-free.www.deepl.com
45.155.204.190 write-free.www.deepl.com experimentation.deepl.com experimentation-grpc.deepl.com ita-free.app.deepl.com
45.155.204.190 ott.deepl.com api-free.deepl.com backend.deepl.com clearance.deepl.com errortracking.deepl.com
45.155.204.190 oneshot-free.www.deepl.com checkout.www.deepl.com gtm.deepl.com auth.deepl.com shield.deepl.com
#Claude
45.155.204.190 claude.ai console.anthropic.com api.anthropic.com
#Trae.ai
45.155.204.190 trae-api-sg.mchost.guru api.trae.ai api-sg-central.trae.ai api16-normal-alisg.mchost.guru
#Windsurf
45.155.204.190 windsurf.com codeium.com server.codeium.com web-backend.codeium.com  marketplace.windsurf.com
45.155.204.190 unleash.codeium.com inference.codeium.com windsurf-stable.codeium.com
144.31.14.104 windsurf-telemetry.codeium.com
#Manus
45.155.204.190 manus.im api.manus.im
#Notion
45.155.204.190 www.notion.so calendar.notion.so
#AIStudio
45.155.204.190 aistudio.google.com generativelanguage.googleapis.com aitestkitchen.withgoogle.com aisandbox-pa.googleapis.com xsts.auth.xboxlive.com
45.155.204.190 webchannel-alkalimakersuite-pa.clients6.google.com alkalimakersuite-pa.clients6.google.com assistant-s3-pa.googleapis.com
45.155.204.190 proactivebackend-pa.googleapis.com robinfrontend-pa.googleapis.com o.pki.goog labs.google labs.google.com notebooklm.google
45.155.204.190 notebooklm.google.com jules.google.com stitch.withgoogle.com gemini.google.com copilot.microsoft.com edgeservices.bing.com
45.155.204.190 rewards.bing.com sydney.bing.com xboxdesignlab.xbox.com xgpuweb.gssv-play-prod.xboxlive.com xgpuwebf2p.gssv-play-prod.xboxlive.com
#Instagram
157.240.245.174 instagram.com www.instagram.com b.i.instagram.com z-p42-chat-e2ee-ig.facebook.com help.instagram.com
#ntc.party
#rutor
#lib.rus.e

---

**2026-03-17T19:44:07 | Anna Bagler**
Zeroblock или podkop скриптом ставить.

---

**2026-03-17T22:21:33 | А. Ч.**
Друзья скажите, есть ли возможность указать, например в podkop, определенный сервер/страну vpn, чтобы как бы быть из этой страны? Я сейчас в Нидерландах а мне нужно попасть в Великобританию.

---

**2026-03-18T00:24:21 | Sergey G**
здравствуйте.  есть роутер OpenWrt 24.10.5 с ZeroBlock 0.7.1-r38
в интернет детекторе висит статус WARP отключен
перезапускал интерфейс awg10 и zb - ничего не поменялось

когда запускаю команду - zeroblock awg warp
наблюдаю что интерфейс перезапускается несколько раз
затем выводится сообщение

========================================================================
         WARP CONFIGURATOR - Full AWG Setup
========================================================================

Starting AmneziaWG WARP configuration...
This will:
  1. Request WARP configuration from RouteRich API
  2. Configure network interface (awg10)
  3. Configure firewall zones
  4. Restart firewall service
  5. Bring up interface
  6. Test connectivity and find working endpoint

Automatically including '/usr/share/nftables.d/table-post/20-miniupnpd.nft'
Automatically including '/usr/share/nftables.d/chain-post/dstnat/20-miniupnpd.nft'
Automatically including '/usr/share/nftables.d/chain-post/forward/20-miniupnpd.nft'
Automatically including '/usr/share/nftables.d/chain-post/srcnat/20-miniupnpd.nft'

========================================================================
 ❌ WARP CONFIGURATION FAILED
========================================================================

Status: Connectivity test failed
Message: No working endpoint found

Работает ли  вообще этот генератор конфигов?
Или может дело в в том, что роутер у меня подключен вторым, после роутера OpenWrt 24.10.2, где стоит podkop
Может ли это как то мешать?

---

**2026-03-18T00:41:51 | Sergey G**
я сделал проще, на первом роутере остановил podkop и zapret2
выполнил команду zeroblock awg warp
WARP подключился

---

**2026-03-18T01:24:02 | Sergey G**
можно вопрос
почему в podkop по умолчанию почти все списки выбраны в секции с "proxy" (при этом почти все работает), а в секции с "vpn" всего несколько списков

а в zeroblock наоборот, больше списков выбрано в секции с "vpn"?
и мне показалось теже самые ресурсы через "vpn" открываются медленнее

---

**2026-03-18T09:54:29 | Роман**
В podkop/zeroblock.

---

**2026-03-18T10:00:25 | Teleghost**
podkop есть, но совершенно непонятно, куда там деть обсуждаемый список telegram. В "Основные настройки" - "Дополнительные конфигурации" - "Список пользовательских доменов" можно только по одному адресу вставлять и рядом много вариантов Proxy/VPN и др. Как правильно?

---

**2026-03-18T10:16:53 | Teleghost**
Спасибо! 
Интересно получается... Сделал новый раздел внутри секции "Дополнительные конфигурации" podkop. В нем добавил два текстовых списка с URL и IP и указал им ходить через vpп awg10. Сохранил-перезагрузил. В результате телефон стал соединяться быстрее, но сейчас кажется, что не все подписанные каналы он теперь видит ("вражеских" там нет). .... 

Ан нет. За несколько минут оставшееся прогрузилось. Просто задержка.

---

**2026-03-18T10:26:17 | Александр**
Podkop, вчера скрипт 5 прогонял повторно, так как телега отвалилась дома ранее.

---

**2026-03-18T11:25:11 | Artem**
В podkop и  zeroblock списки включены, а есть ещё какие то решения ?

---

**2026-03-18T18:18:14 | Вячеслав**
Zapret 2 не конфликтует с Podkop?

---

**2026-03-18T19:18:27 | Роман**
Zeroblock/podkop - в обоих вариантах есть списки роблокса. Но желательно со своим сервером. Попробуйте з1, там и для дискорда, ютуба стратегии есть. Может и роблокс заведётся.
sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh)
Это в терминал.
Запрет 2 отключить с автозапуском, если будете пробовать.

---

**2026-03-18T21:51:06 | Andrey**
Добрый вечер, подскажите пожалуйста, как добавить ссылкой свой vless сервер в секцию vpn в podkop?или нужно ставить zeroblock beta?

---

**2026-03-18T22:29:36 | Routerich**
Службы - >Podkop->если есть секция Discord или YouTube/Discord->нажимаем изменить и в предустановленные списках выбираем список Telegram

---

**2026-03-18T22:53:09 | Саша**
Добрый вечер
Перестал работать podkop, ставил амнезию
Пропало питание, роутер частично потерял настройки. Бэкап соответственно не делал 
В чем может быть проблема

---

**2026-03-18T22:53:43 | Саша**
Добрый вечер
Перестал работать podkop, ставил амнезию
Пропало питание, роутер частично потерял настройки. Бэкап соответственно не делал 
В чем может быть проблема

---

**2026-03-19T12:21:17 | Константин**
Можете подсказать как восстановить интернет:у меня проблемы с подкопом(там нет таблицы в podkop_table)

я проверил впн,он передавал данные и есть хендшейк.

Попытался исправить перезапуском подкопа,но что то пошло не так,и интернет пропал……как вернуть интернет назад и починить подкоп?

---

**2026-03-19T13:21:48 | Anna Bagler**
Потенциально можно, изучите podkop.net на предмет корпоративного vpn и полный мануал по zeroblock.

---

**2026-03-19T15:21:00 | Виктор Замиралов**
Здравствуйте, у меня не работает телеграмм на 2ух телефонах из 3ёх. В чём причина и как сделать так, чтобы тг работал на всех устройствах в доме?
У меня есть vds(Финляндия) на HostVDS.com. На сервере установлен amnezia wg с помощью клиента amnezia vpn(self-hosted). На роутере установлен Youtubeunblock(выключен), zapret, podkop, awg. Все телефоны подключены к роутеру по wi-fi. На всех телефонах нет никаких vpn клиентов. В списках podkop выставлен только телеграмм. 
Итог: тг работает только на пк и на телефоне(с таким же аккаунтом как и на пк), а на 2ух других телефонах - не работает. При этом ютуб работает на всех устройствах(zapret).
P.S я мало что понимаю во всех этих делах, настраивал всё по гайдам из ютуба и т.д.
С протоколом vless такая же ситуация.
Если выключить podkop и установить на телефоны amnezia vpn и подключаться через него, то также работает только на том телефоне, у которого акк телеги используется на пк.

---

**2026-03-19T15:59:36 | ILDAR G.**
Добрый вечер. подскажите пожалуйста. Создал сеть wireguard конфиг. Вроде пакетики побежали, в podkop добавля интерфейс этот вирегуард, выбрал списки. Все сохранил, сделал диагностику все ок. Но через впн не ходит, напрямую стучиться. Что не так делаю?

---

**2026-03-19T16:19:52 | PETROVICH**
Добрый день!
Помогите, пожалуйста.
Исходные данные:
- Установлен Podkop v0.7.14 + sing-box 1.12.22
- Подключено несколько VLESS туннелей
- Все работает и маршрутизируется на нужные физические (lan) и витруальные интерфейсы (OpenVPN туннели)

Появилась задача:
- запустить прокси сервер HTTP, SOCKS5, с Авторизаций
- сделал это средствами Podkop и sing-box
'Включить смешанный прокси-сервер, разрешив этому разделу маршрутизировать трафик как через HTTP, так и через SOCKS-прокси.'
- открыл соответствующий TCP порт прокси на Firewall
- все работает
- НО как настроить авторизацию входа прокси?
В этот раздел конфига sing-box/config.json добавляю информацию:
    {
      "type": "mixed",
      "tag": "VLESS-mixed-in",
      "listen": "0.0.0.0",
      "listen_port": 1080,
      "users": [
        {
          "username": "user",
          "password": "pass"
        }
      ]
    }
НО этот конфиг перезаписывается каждый раз при рестарте Podkop (удаляется секция с авторизацией).

ВОПРОС - какой прокси сервер SOCKS5 для внешних клиентов лучше всего поставить на Routerich?
Требования:
- авторизация
- работа с VLESS (внешние прокси клиенты маршрутизируются в туннель)
- обязательно управление в LuCi интерфейсе

---

**2026-03-19T16:40:22 | Anna Bagler**
Просто zeroblock - разработка от РР, т.е. помощь будет более оперативной. Podkop - разработка itdog, скрипт 5 создан РР для упрощения манипуляций по установке подкопа. По функционалу они похожи, zero может то, с чем в подкопе надо ещё позаморачиваться.

---

**2026-03-19T18:00:22 | Anna Bagler**
Через что он у вас? Если podkop и секцию с awg, перезапускайте интерфейс, если через запрет, подбирайте другую стратегию.

---

**2026-03-19T22:17:23 | Виктор Замиралов**
Вобщем как оказалось, всётаки работает телеграмм на телефонах и через клиент амнезии и через awg + podkop на роутере. А думал что на других телефонах не работает, так как слишком долго грузились фото и видео по сравнению с моим телефоном. Возможно проблема с сервером вплане мощностей...(Если так то какое железо нужно чтоб 3 человека могли видео смотреть в телеге?)
И ситуация выглядит так, что у меня всех быстрее всё грузится, на 2ром телефоне - средняя скорость, на 3тьем - низкая...
Можно ли сделать так чтобы все устройства поровну использовали мощность сервера?
P.S Если диагностика подкопа на телефонах означает - зайти с этих телефонов в роутер->сервисы->подкоп и нажать диагностику, тогда я её делал и там неисправностей никаких не вылезло(кроме дополнительных правил маркировок, но я так понял что это из за zapret. И да скрин из пк подкопа, но на телефонах также всё диагностировалось)

---

**2026-03-19T22:38:52 | Антон**
Анализ запущен: 2026-03-19 22:37:36
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.9 | YouTube IP:  108.177.14.190

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.72 MB / ↑0.31 MB
  Пинг (ya.ru via awg10): 11.859 / 16.407 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock podkop zapret2

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY CHAOS!)    | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock              awg10 (vpn): anime,!!!_discord,googleplay,messengers,!!!_meta,news,porn,socials,video
  zeroblock          opera (prx out): !!!_geoblock,ai
  podkop    Youtube_Discord (vpn): youtube,!!!_discord
  podkop           main (prx out): !!!_geoblock,block,!!!_meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.14
  Версия zeroblock: 0.7.1-r52
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.05 | RAM: 28% | NAND: 46% занято / 36.4M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-03-19T22:43:02 | Антон**
Podkop Error
Thu Mar 19 22:38:38 2026 user.notice podkop: [error] Download https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_cidr_ipv4.txt list failed
Podkop Error
Thu Mar 19 22:38:31 2026 user.notice podkop: [error] Download discord list failed
Podkop Error
Thu Mar 19 22:38:24 2026 user.notice podkop: [error] Download twitter list failed
Podkop Error
Thu Mar 19 22:38:17 2026 user.notice podkop: [error] Download meta list failed

---

**2026-03-19T22:53:54 | Антон**
Анализ запущен: 2026-03-19 22:52:23
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.18 | YouTube IP:  108.177.14.136

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.72 MB / ↑0.28 MB
  Пинг (ya.ru via awg10): 7.376 / 9.487 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock zapret2

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  podkop          | STOPPED                        | ОТКЛ
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock              awg10 (vpn): anime,discord,googleplay,messengers,meta,news,porn,socials,video
  zeroblock          opera (prx out): geoblock,ai
  Версия zeroblock: 0.7.1-r52
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.57 | RAM: 24% | NAND: 45% занято / 36.6M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1
  !!!_WatchDoc установлен

---

**2026-03-20T10:19:42 | Роман**
Здравствуйте. Для вас лучше на чистый роутер. Схема podkop/zeroblock на одном устройстве для опытных пользователей.

---

**2026-03-20T11:51:09 | Роман**
После пары дней мучения, нашел способ завести войсчат и проксимити чат в ARC Raiders и APEX Legends. Для этого вставьте в podkop /zeroblock следующие подсети

18.128.0.0/9
13.48.0.0/13
13.24.0.0/13
13.56.0.0/14
13.32.0.0/12
18.128.0.0/9
18.64.0.0/10
8.0.0.0/13
8.8.0.0/22

так же желательно добавить данные домены 
voice-eu1.embark.io
aws-voice-region.amazonaws.com
vivox.com
agora.io
ip.fish
turn.rtcp.on.epicgames.com
turn-eun1.rtcp.on.epicgames.com
turn-euc1.rtcp.on.epicgames.com
rtcp.on.epicgames.com
signaling-service-prod.eun1.live.rtcp.on.epicgames.com
signaling-service-prod.euc1.live.rtcp.on.epicgames.com
signaling-service-prod.use1a.live.rtcp.on.epicgames.com
eos-gateway-prod.ak.epicgames.com
api.epicgames.dev
game.hosting.epicgames.dev
videodelivery.net
cloudflarestream.com
cfargotunnel.com
argotunnel.com


18.128.0.0/9
13.48.0.0/13
13.24.0.0/13
13.56.0.0/14
13.32.0.0/12
18.128.0.0/9
18.64.0.0/10
8.0.0.0/13
8.8.0.0/22
34.4.16.0/20
34.4.32.0/19
34.4.64.0/19
34.4.96.0/22
34.4.128.0/18
34.6.0.0/15
34.8.0.0/13
34.16.0.0/12
34.32.0.0/11
34.64.0.0/10
34.128.0.0/10
35.184.0.0/13
35.192.0.0/14
35.196.0.0/15
35.198.0.0/16
35.199.0.0/17
35.199.128.0/18
35.200.0.0/13
35.208.0.0/12
35.224.0.0/12
35.240.0.0/13
136.107.0.0/16
136.108.0.0/14
136.112.0.0/13

Это допустим решение для войс чата.

---

**2026-03-20T16:52:22 | Alex**
Анализ запущен: 2026-03-20 20:49:42
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.1.34 | YouTube IP:  198.18.2.195

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.72 MB / ↑0.25 MB
  Пинг (ya.ru via awg10): 58.488 / 59.171 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop zapret

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 198.18.2.195
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Пересечение между podkop и zapret:
    podkop                    : Youtube_Discord
    zapret                    : zapret-hosts-google.txt
    Домены: googlevideo.com youtube.com 

  podkop    Youtube_Discord (vpn): youtube,discord,telegram,meta
  podkop           main (prx out): google_ai,twitter,geoblock,block,hdrezka,google_play
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.53 | RAM: 25% | NAND: 27% занято / 49.1M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-03-20T17:27:57 | Артем Михайлов**
Вообщем моя последовательность шагов.
1.  Удалил Podkop и YouTubeUnBlock.
2. Обновил пакеты.
3. Попробовал поставить ZeroBlock - не получилось.
4. Перезапустил роутер. 
Все =))) 
Сча после ребута посмотрим.

---

**2026-03-20T17:46:40 | 715 agent**
а никто случаем не сталкивался вот с такой проблемой  (user.notice podkop: [error] Download https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_cidr_ipv4.txt list failed
user.notice podkop: [error] Download telegram list failed
и т.д
 будто локальный умер.... но что делать я не до конца понял

---

**2026-03-20T20:43:55 | Routerich**
будут, ведь все знают что podkop = zeroblock просто под другим именем

---

**2026-03-20T20:47:20 | Timur**
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.0.95 | YouTube IP:  198.18.0.96
  Программы в автозапуске: podkop

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  youtubeUnblock  | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Пересечение между podkop и youtubeUnblock:
    podkop                    : main
    youtubeUnblock            : YouTube
    Домены: googlevideo.com youtube.com

  podkop           main (prx url): discord,meta,twitter,tiktok,telegram,google_ai,youtube
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 1.1.1.1
  Версия podkop: v0.7.14

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.00 | RAM: 25% | NAND: 30% занято / 47.3M доступно
  13 9 * * * /usr/bin/podkop list_update

---

**2026-03-20T20:48:54 | Dmitry**
все проще, чукча инструкцию до конца не осилил, source interface в podkop включить же надо) все работает, спс

---

**2026-03-20T20:51:32 | Роман**
Установить средство маршрутизации на роутер.
https://t.me/routerich/394153/520562
или
podkop.net

---

**2026-03-20T20:52:01 | Timur**
я с консоли его выключал
/etc/init.d/youtubeUnblock stop
= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.0.95 | YouTube IP:  198.18.0.96
  Программы в автозапуске: podkop

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop           main (prx url): discord,meta,twitter,tiktok,telegram,google_ai,youtube
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 1.1.1.1
  Версия podkop: v0.7.14

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.00 | RAM: 20% | NAND: 30% занято / 47.4M доступно
  13 9 * * * /usr/bin/podkop list_update
c vless все отлично

---

**2026-03-20T21:55:25 | Святос**
podkop.net там в установке, если я всё правильно понял

---

**2026-03-20T22:36:53 | Routerich**
Попробуйте сменить днс провайдера в Podkop

---

**2026-03-20T23:05:58 | Arsen S**
Прогнал скрипт №5, обновил Podkop до версии 0.7.14. Во вкладке Podkop валятся ошибки. Работает только ютуб, но я ранее настраивал Zapret2 возможно это причина. Помогите пожалуйста, что не так.

---

**2026-03-20T23:18:47 | Routerich**
Уберите галочку с скачивать списки через Proxy, в настройках Podkop, сохранить и применить. После проверяйте

---

**2026-03-21T11:48:45 | Nikita**
привет! подскажите chat gpt Unable to load site. в инкогнито работает. в чем может быть проблема? использую 
Podkop: v0.4.11-r1

---

**2026-03-21T11:57:09 | Роман**
Выбрать торренты в podkop/zeroblock.

---

**2026-03-21T12:03:19 | Vladimir Nikolsky**
Анализ запущен: 2026-03-21 12:01:59
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.2.59 | YouTube IP:  198.18.0.138
  Программы в автозапуске: podkop

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  youtubeUnblock  | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Пересечение между podkop и youtubeUnblock:
    podkop                    : main
    youtubeUnblock            : YouTube
    Домены: googlevideo.com youtube.com 

  podkop           main (prx url): discord,hetzner,meta,!_russia_inside,telegram,twitter
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 1.1.1.1
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.32 | RAM: 23% | NAND: 30% занято / 47.5M доступно
  13 9 * * * /usr/bin/podkop list_update

---

**2026-03-21T12:16:57 | Роман**
Тогда и разницы нет для вас, просто лучше и удобнее. Одновременное использование ZB и podkop на ваш страх и риск.

---

**2026-03-21T13:00:11 | Routerich**
https://podkop.net/docs/dev/singbox-vs-xray-vs-mihomo/

---

**2026-03-21T13:11:49 | Борис**
Благодарю) ссылка ведёт на автора Podkop, я ознакомился, концептуально осмыслил проблемы и отличия. Но ведь это аргументы именно автора Podkop, а у уважаемого автора Zeroblock точно такое же мнение? Или выбор в пользу sing-box бы обусловлен тем, чтобы "меньше пердолиться и быстрее выпустить готовый продукт, плюс есть наработки от коллеги (podkop)"? Были ли мысли перейти на xray? Всё же это позволило бы ощутимо сократить занимаемую память... Да и открыло бы (возможно) пространство для творчества, т.к. сейчас зб как бы ограничен возможностями sing-box и протоптанной дорожкой автора Podkopa, или я не прав и все эти "возможности для творчества" лишь иллюзорны и в сущности дадут только лишний гемор и принципиально ничего нового? 

Лично моё мнение, что устанавливать целый комбайн xray ради пары специфических конфигов - выглядит как костыль, и так будто бы не должно быть. Я иногда думал об этом перед сном, но стеснялся задать такой вопрос, потому что ожидаемо в ответ можно получить что-то в духе "ну сделай тогда сам если такой умный" 🤔

---

**2026-03-21T13:32:57 | Artem**
Дело в podkop как я понимаю? Он выключен, но как его полностью удалить не знаю...

---

**2026-03-21T13:40:25 | Artem**
reset роутера всмысле? И накатить по новой zeroblock без podkop?

---

**2026-03-21T13:42:01 | Роман**
Использование ZB с podkop для опытных пользователей. Оставляйте что-то одно. И да, сброс и последняя прошивка желательны.

---

**2026-03-21T14:03:31 | Artem**
Установил последнюю прошивку, podkopa больше нет, но chatgpt так и не работает ...

---

**2026-03-21T14:23:03 | Artem**
Хотя нет, залогиниться всё равно не выходит. Попробую тогда ещё раз, podkop наоборот, вместо zeroblock...

---

**2026-03-21T15:02:43 | Евгений**
Ребятки, всем здарова! Есть смысл менять podkop на zeroblock ? Я так понимаю эту программы в роутере для обхода блокировок. Я просто нуб в этом деле. Мне нужно что бы ютуб , телега да инста работали. Сейчас podkop стоит. В целом все работает но иногда тормозит. Перезагрузка помогает пока что.

---

**2026-03-21T15:42:17 | Роман**
Свои (покупные) сервера с различными панелями, vless, amneziaWG - с последующей интеграцией в podkop/zeroblock.

---

**2026-03-21T16:32:07 | Andrey Shilov**
скрипт 5 не устанавливает awg в podkop (все endpoint not work), только прокси. так и должно быть или что-то не так делаю ?

---

**2026-03-21T16:34:34 | Борис Диденко**
Друзья, что делать, если при диагностике podkop пишет, что "DHCP содержит DNS сервер". Я вычитал, что тут замешана функция don't touch my dhcp. Ее нужно отключить?

---

**2026-03-21T16:35:30 | Борис Диденко**
У меня просто podkop последнее время компромиссно работает, думал в этом дело

---

**2026-03-21T20:04:58 | Yury Kuzmenko**
Podkop не поддерживает xhttp в вашей vless ссылке, переходите на зероблок

---

**2026-03-21T20:11:05 | Роман**
https://telegra.ph/Polnaya-instrukciya-nastrojki-xHTTP-v-Podkop-12-08

---

**2026-03-21T20:35:29 | None**
Podkop Error
Sat Mar 21 20:28:08 2026 user.notice podkop: [error] Download https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_cidr_ipv4.txt list failed
Закрыть
Podkop Error
Sat Mar 21 20:28:00 2026 user.notice podkop: [error] Download telegram list failed
Закрыть
Podkop Error
Sat Mar 21 20:27:53 2026 user.notice podkop: [error] Download discord list failed

---

**2026-03-21T21:13:47 | Routerich**
А вы их точно искали?) https://podkop.net/docs/tunnels/awg_settings/ пункт у установкой пакетов пропустить

---

**2026-03-21T21:35:36 | alx_baike**
Походу придётся в podkop. Свой vless со своим xray сервером развернут под self-steal домен на VPS за бугром, но скорость он конечно режет по сравнению с дурилками. Ну ладно, буду через него. Спасибо ещё раз

---

**2026-03-21T21:43:05 | Андрей**
Привет! Помогите продиагностировать проблему, плиз. В zeroblock работают комьюнити списки, но не работают пользовательские списки доменов. До этого стоял podkop, было точно такое же поведение.

---

**2026-03-21T22:02:55 | Alexey**
обновился с помощью "обновления системы", почему-то в итоге получил podkop старой версии. не проблема, но выглядит странно - откуда она взялась))

---

**2026-03-21T22:04:34 | Routerich**
Здравствуйте.
В нашей репе старая версия Podkop

---

**2026-03-21T23:10:35 | Sergey G**
Подскажите, действительно ли данные настройки могут блокировать какую-то рекламу?
кажется это добавляет podkop (это на роутер с 24.10.2), при выполнении скрипта 5/beta

после установки zeroblock (на роутере с 24.10.5), тут появляется единственная настройка
у нее аналогичная задача или нужно дополнять настройки в данной секции?

---

**2026-03-21T23:43:53 | Роман**
Конечно. Покупаете vps с ip нужной страны, поднимаете нужную панель, настраиваете, закидываете ссылку в zeroblock/podkop.

---

**2026-03-22T00:07:12 | Routerich**
Это нормально, так как им управляет Podkop/zeroblock

---

**2026-03-22T00:20:32 | Routerich**
5-й скрипт все делает как надо, если у вас есть свой peozy/vpn, потом создаёте секцию в Podkop и туда добавляете это и все

---

**2026-03-22T06:00:52 | Alex_Jester**
Такой вопрос. Мне нужно, чтобы то что заблокировано, либо замедлено в РФ шло через VPN, а что не заблочено напрямую. Что будет установить удобнее для этого дела? Я так понимаю podkop это оптимальный вариант?

---

**2026-03-22T06:03:48 | Alex_Jester**
Чем Зероблок лучше podkopa? Вкратце почитал, с Зеро больше пердолинга на порядок, как мне кажется.

---

**2026-03-22T07:48:37 | Routerich**
Ок, теперь в настройках Podkop уберите галочку со скачивать списки через Proxy/vpn

---

**2026-03-22T09:26:47 | Anna Bagler**
Используйте запрет/запрет2 + стратегии, если вам только yt нужен, или ещё zeroblock добавляйте или podkop.

---

**2026-03-22T10:18:48 | 🅓🅜🅘🅣🅡🅨 🏴‍☠️**
Анализ запущен: 2026-03-22 19:15:29
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.0.26 | YouTube IP:  198.18.0.27

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓0.00 MB / ↑0.01 MB
  Пинг (ya.ru via awg10): ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (5.255.255.242): 56 data bytes
  Программы в автозапуске: podkop opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН
  awg10 (IPv4) : ОФЛАЙН
------------------------------------------------------
  curl: (28) Connection timed out after 5002 milliseconds
  Warning: Problem : timeout. Will retry in 1 seconds. 3 retries left.
  curl: (28) Connection timed out after 5002 milliseconds
  Warning: Problem : timeout. Will retry in 2 seconds. 2 retries left.
  curl: (28) Connection timed out after 5002 milliseconds
  Warning: Problem : timeout. Will retry in 4 seconds. 1 retries left.
  curl: (28) Connection timed out after 5002 milliseconds
------------------------------------------------------
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 198.18.0.27
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop          MyVPN (prx url): !_russia_inside
  podkop           main (prx out): block,meta,twitter,hdrezka,tiktok,google_ai,discord,telegram
  podkop DNS/Bootstrap DNS: 1.1.1.1 / 8.8.8.8
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.42 | RAM: 24% | NAND: 26% занято / 49.8M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

root@RouteRich:~# 
root@RouteRich:~#

---

**2026-03-22T11:32:15 | Teleghost**
А как? Можно ссылку на инструкцию?
В том же podkop есть только "Proxy, VPN и Block" и НЕТУ никакого Direct.

---

**2026-03-22T11:44:11 | Teleghost**
Мне наоборот надо ОТКЛЮЧИТЬ прокси до любых попыток применения альтернативных путей. Цель - быть уверенным, что применение podkop, zapret и им подобных никогда не будет влиять на это список сайтов.

 У меня нет никакого vless, хотя интересует возможность сделать такой канал _без_ vps и веб-серверов между двумя частными квартирами.

---

**2026-03-22T11:51:42 | Кирик**
Доброе утро
Подскажите как обновить Podkop на новую версию?

---

**2026-03-22T13:01:54 | Михаил**
не понравились задержки в podkop, интерфейс amnezia выдавал очень уж большие задержки (2.5-3.5 секунды), vless секция тоже чуть больше выдавала задержку 450-800 мм), с обновлением на чистый openWRT задержки по vless сократились до 150-300 мм, а по amnezia до 200-800 мм в зависимости от конфига

---

**2026-03-22T13:03:30 | Teleghost**
Пытаюсь подключиться к серверу налоговой РФ lkfl2.nalog.ru.

Отключил podkop c запретом. В /etc/resolv.conf (на компе linux) прописан только провайдерский DNS. Попытка зайти на lkfl2.nalog.ru, и все отлично первые 5 минут. Потом браузер хром выдает ошибку "Не удалось найти IP-адрес сервера lkfl2.nalog.ru.". DNS на компе только провайдерский. 

Звоню провайдеру "Почему у вас DNS не отвечает"? От провайдера ответ - "DNS работает, но ваш роутер его игнорирует и ломится на все возможные DNS кроме правильного".  

Так почему браузер не может получить ответ от прописанного на ПК провайдерского DNS?  Стандартная конфигурация скрипта 5 как-то подменяет DNS-запросы? 
Routerich + конфигурация скрипта 5 + в подкопе список для телеги добавлен.

---

**2026-03-22T13:22:19 | Anna Bagler**
Посмотрите Секции на сайте podkop.net, чтоб понимать общие принципы. Полный мануал по zeroblock изучите.

---

**2026-03-22T16:17:15 | ZЁма**
Установка ZB с нуля:


1. Если до этого стоял podkop, то создайте резервную копию настроек.
1. Прошиваем RR без сохранения настроек прошивкой 24.10.5 в соответствии с версией USB: USB2.0-белый, USB3.0-синий. Или делаем сброс на заводские настройки.
2. Переходим в "Система" -> "Пакеты" -> "Действия" и прожимаем кнопку "Обновить списки...". Если были ошибки, то повторяем процедуру еще раз.
3. В окне "Фильтр" вводим "you" и во вкладке "Установлено" видим пакет "youtubeUnblock" и удаляем его. Также можно остановить и отключить его в "Система" -> "Автозапуск".
4. В окне "Фильтр" вводим "awg" и во вкладке "Обновления" видим два пакета для обновления и обновляем их, это для установки конфигурации awg2.0.
5. Желательно выполнить обновление прошивки ASU-обновление.
6. Перезагружаем RR.
7. Заходим в RR через окно Инкогнито.
8. Переходим в "Система" -> "Пакеты" -> "Действия" и прожимаем кнопку "Загрузить пакет..." и устанавливаем последний ZB, сначала сам zeroblock, а потом luci-app-zeroblock.

Далее VLESS и AWG2.0

---

**2026-03-22T17:04:49 | Routerich**
В outbounds надо добавлять, по такому принципу https://podkop.net/docs/own-outbound/

---

**2026-03-22T18:13:22 | Marat 🌊🌊 Wave**
А почему Podkop указан как устаревший? Его как то обновить надо?

---

**2026-03-22T18:20:37 | Andrey**
хм, странно, запустил из закрепа "Код для запуска с автоматической генерацией AWG WARP и без установки/замены конфигурации Podkop"
он в итоге затер мне настройки подкопа под 0

---

**2026-03-22T19:25:23 | IIlIlIlIIlIlIlIIIll**
Привет всем. Вопрос: Можно ли поменять регион дефолтного прокси (opera)"podkopа" с EU на US ? Для Xbox надо

---

**2026-03-22T19:49:32 | V**
= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 1.06 | RAM: 25% | NAND: 26% занято / 50.2M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-03-22T19:50:58 | Khamzat**
Всем доброго времени суток!
Сегодня занимался перекатом с podkop на zeroblock: обновил прошивку до 24.10.5 на роутере файлом из соответствующего раздела группы, выполнил первичные настройки, поставил в нужном порядке 2 файла zeroblock из закрепа и следовал в целом инструкции, но столкнулся с тем, что интерфейс awg не хочет создаваться, что и отражено в логах в приложенном файле

Видел, что в топике тут у некоторых людей такая же проблема возникла. Решения для этой проблемы пока нет?

---

**2026-03-22T21:09:20 | Дмитрий**
Командой: sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)

---

**2026-03-23T01:02:09 | Дмитрий Григорьев**
Помогите пожалуйста с проблемой:

Сначала стоял Podkop + Zapret1 (Юутб + Дискорд через запрет, остальное по спискам через туннель)
Всё вроде бы работало, недели две...., вчера заметил, что в дискорде есть дикая потеря пакетов с моей стороны, меня все слышат хорошо, однако я не могу и слова различить
Отключил Podkop, всё заработало, думаю надо же решить проблему.

Ради интереса снёс систему и накатил ZB + Zapret2, Теперь через запрет шёл только Ютуб, так как дискорд я поднять не смог, пустил его через ZB
Такая же шляпа, потеря пакетов в дисе. Отключил ZB, всё работает.

Что можно сделать в такой ситуации, как оживить, ведь всё  до вчерашнего дня работало без нареканий

---

**2026-03-23T01:38:11 | Routerich**
Сначала обновить пакеты amneziawg в Система - пакеты - обновить списки - вкладка обновления. Далее сеть - интерфейсы - там добавить свой конфиг амнезии https://podkop.net/docs/tunnels/awg_settings/#nastrojka-cherez-luci (пункт с установкой пакетов пропустить) - и там импортировать конфиг. Все делать в режиме инкогнито в браузере

---

**2026-03-23T11:25:07 | OnixKid**
= ИНФОРМАЦИЯ О TAILSCALE:
  Версия: 1.86.2          | Статус: STOPPED | Автозапуск: РАЗРЕШЁН

= АНАЛИЗ КОНФИГУРАЦИИ /etc/config/tailscale:

1. ОБЯЗАТЕЛЬНЫЕ ПАРАМЕТРЫ:
  [OK]   enabled                        | 1 [галочка "Включить"]
  [OK]   accept_dns                     | 1 [галочка "Принимать DNS"]
  [КРИТ] accept_routes                  | 0 (должно быть 1) [галочка "Принимать маршруты"]

2. ОПЦИОНАЛЬНЫЕ ПАРАМЕТРЫ:
  [ИНФО] fw_mode                        | nftables [настройка "Режим межсетевого экрана"]
  [ИНФО] log_stdout                     | включен [галочка "Журнал вывода"]
  [ИНФО] log_stderr                     | включен [галочка "Журнал ошибок"]
  [ИНФО] disable_snat_subnet_routes     | не установлен [CLI флаг]

3. ПРОВЕРКА EXIT NODE:
  [OK]   advertise_exit_node            | включен [галочка "Узел выхода"]
  [OK]   advertise_routes               | 192.168.1.0/24 = 192.168.1.0/24 (br-lan) [настройка "Открыть подсети"]
  [КРИТ] podkop (not running)           | интерфейсы  [настройка "Интерфейс источника"]
         Для работы exit node интерфейс tailscale0 должен быть выбран в настройках podkop

= СТАТУС ПОДКЛЮЧЕНИЯ:
  [КРИТ] Tailscale: не запущен

= ДОПОЛНИТЕЛЬНЫЕ ПРОВЕРКИ:
  [КРИТ] Интерфейс tailscale0: не найден

---

**2026-03-23T12:30:38 | VillainRU**
Ребят, привет, помогите пожалуйста. У меня роутер с openwrt, в нём podkop, в подкопе выбраны списки маршрутизации до моего vps с vless. У моего провайдера есть свой dns (10.0.0.101\103), но с ним не работают некоторые игры (дисконнект), если я в настройках сетевой карты принудительно включаю dns яндекса, игры начинают работать, но gemini в браузере уже говорит что страна не подходит. В подкопе выбран dns гугла и bootstrap dns яндекса. Как то можно настроить что бы всё работало на одном днс? Dns adguard так же себя ведёт

---

**2026-03-23T15:46:17 | Andrey**
Приветствую. Нужен совет по общей стратегии настройки роутера. Я в этой теме новичок, поэтому хочу понять какой подход нормальный и в какой последовательности лучше всё настраивать. Насколько я понимаю, возможны разные варианты: например, установить Podkop, настроить списки, затем дополнительно использовать zapret2, Zeroblock и др. Но мне не очень ясно, что действительно нужно ставить вместе, что дублирует друг друга, а с чего лучше начать чтобы не усложнить себе жизнь с самого начала. Понимаю, что многое уже обсуждалось, но буду благодарен, если подскажете именно общую логику действий типа с чего лучше начинать, что ставить в первую очередь и какой сейчас рабочий вариант лучше всего

---

**2026-03-23T15:48:19 | Anna Bagler**
Zeroblock и Podkop - конфликт. Zeroblock + Zapret2.

---

**2026-03-23T16:27:16 | Grigory**
Что сейчас лучше и проще настроить? zeroblock, zapret2 или podkop?

---

**2026-03-23T20:55:25 | Anna Bagler**
Перезапустить opera-proxy и сам podkop.

---

**2026-03-23T22:06:02 | Alexx**
Добрый вечер. Есть пылесос midea и через фирменное приложение в последнее время  "тупит" не с первого раза принимает команды. Подскажите как отследить куда он стучится "домены/сайты" чтобы эту заразу прописать через podkop.

---

**2026-03-24T03:07:17 | Борис**
http://192.168.1.1/cgi-bin/luci/admin/system/startup тут включить автозапуск sing-box и podkop

---

**2026-03-24T07:15:07 | Routerich**
Здравствуйте.
отследить сервера/домены на которые они обращаются и добавить их в podkop/zeroblock

---

**2026-03-24T08:02:10 | Routerich**
Здравствуйте.
а если остановить Podkop, работают?

---

**2026-03-24T08:21:23 | ⓞ ᗰ**
Приветствую всех!
Вчера установлен роутер, из настроек сделала только скрипт 5, домены телеграма вручную добавила в Podkop и добавила стратегии для работы роблокс (спасибо за подсказки). Работает всё что надо: ютуб, дискорд и тд, телега шустрая.
Вопрос, т.к. сталкиваюсь с этим впервые, нужно ли где-то следить чтоб все поддерживалось в актуальном состоянии, или автоматически это как-то происходит?

---

**2026-03-24T10:38:33 | Dmitry**
Здравствуйте. Sing box в последнее время после ночного ежедневного ребута перкстал запускаться, перезапускал podkop помогало , сегодня не помогает sing box не запускается
Podkop
v0.7.7Устаревшая
Luci App
v0.7.7
Sing-box
1.12.12
OS
RouteRich 24.10.4 r28959-29397011cc RR-3.8.2
Device
Routerich AX3000 v1

---

**2026-03-24T18:02:18 | Роман**
Домены для разблокировки lol wild rift, закинуть zeroblock/podkop в список пользовательских доменов.

riotcdn.net
pvp.net
leagueoflegends.com
rgpub.io
rdatasrv.net
akamaihd.net

#games

---

**2026-03-24T18:30:18 | Routerich**
А какие у вас списки выбраны в Podkop?

---

**2026-03-24T19:31:38 | Maxim Mrakov**
Всем добрый вечер, есть тут знатоки podkop может кто-то подсказать, почему не работает gemini на смартфоне? Или в какую сторону можно посмотреть? Не спец в сети, заранее спасибо!

---

**2026-03-24T19:41:26 | ILDAR G.**
спасибо я пользуюсь podkop , он не стабильный?*

---

**2026-03-24T20:46:50 | Alexx**
Добрый вечер. Есть удалёнка рабочая на отдельной загрузочной защищённой флешке (черный ящик), на домашнем интернете перестала работать, на другом ораторе связи работает (видимо оператор стал блокировать). Подскажите вообще такое возможно? Отследить  на Роутериче куда ломится ip ноутбука с удаленкой  и попробовать завернуть удалёнку в Podkop или ещё куда.

---

**2026-03-24T20:59:16 | Oleg Shmyrin**
А подскажите, есть смысл попробовать установить ZeroBlock вместо podkop ?

---

**2026-03-24T21:00:37 | Oleg Shmyrin**
Нет, сегодня провайдер проводил работы, и podkop скис, как я понимаю в области AmneziaWG WRAP, то ли совпало и поменялся публичный ключ/ip

---

**2026-03-24T21:50:43 | Андрей Тябин**
Я же правильно зашел, службы-podkop-секции?

---

**2026-03-24T22:24:44 | Святос**
opkg remove luci-i18n-podkop-ru luci-app-podkop podkop в терминал и пробуйте снова

---

**2026-03-24T23:15:15 | Алексей Михайлов**
= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Пересечение между podkop и zapret:
    podkop                    : main
    zapret                    : zapret-hosts-google.txt
    Домены: googlevideo.com youtube.com 

  podkop            Discord (vpn): discord,anime,!!!_geoblock
  podkop           main (prx out): !!!_geoblock,block,meta,twitter,hdrezka,tiktok,google_ai,youtube,telegram
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  podkop юзерсписки: !!!_segment.com → Discord, main
  podkop юзерсписки: !!!_cookielaw.org → Discord, main
  podkop юзерсписки: !!!_nyaa.si → Discord, main
  podkop юзерсписки: !!!_cdnjs.cloudflare.com → Discord, main
  podkop юзерсписки: !!!_onetrust.com → Discord, main
  podkop юзерсписки: !!!_ipify.org → Discord, main
  podkop юзерсписки: !!!_search.extto.com → Discord, main
  podkop юзерсписки: !!!_crunchyroll.com → Discord, main
  Версия podkop: v0.7.14

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.95 | RAM: 23% | NAND: 27% занято / 49.6M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-03-24T23:46:10 | Игорь**
запущен: 2026-03-24 23:44:42
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.43 | YouTube IP:  74.125.131.190

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓2.46 MB / ↑0.09 MB
  Пинг (ya.ru via awg10): 25.032 / 26.394 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop zapret opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Внутреннее пересечение в podkop:
    podkop                    : Discord (Условия: default)
    Домены: www.crunchyroll.com 

  podkop            Discord (vpn): discord,telegram
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.14

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.16 | RAM: 23% | NAND: 27% занято / 49.6M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

root@RouteRich:~#

---

**2026-03-25T09:22:53 | Routerich**
Здравствуйте.
А у вас Podkop/zeroblock установлен?

---

**2026-03-25T13:58:11 | Артём Фомин**
Наконец-то получил свой долгожданный роутер. YouTube заработал прямо из коробки, однако только на компьютере. На телевизоре и на телефоне ничего не загружается. К тому же на телевизоре появилась проблема в некоторых других приложениях, например в КиноПоиске. КиноПоиск первый раз загружается очень долго — наверное, минут 15 висит заставка КиноПоиска. После начинает открываться быстро. Однако стоит очистить кэш и перезагрузить Smart Box, проблема опять повторяется при первом запуске.

Дополнительно установил только Podkop, где в списках сообщества установил Meta, Telegram и Google AI. YouTube там нет.

Как полагаю, проблема в youtubeUnblock. Установил пакет luci-app-youtubeUnblock, и после в настройках приостановил youtubeUnblock. После этого проблемы с загрузкой других приложений исчезли.

Подскажите, может, у кого была такая же проблема? Хотелось бы, чтобы YouTube работал без VPN на всех устройствах. Могу, конечно, пустить его через Podkop, но реклама заколебала, причём литовская, так как сервер находится именно там.

Прошу помочь в настройке.

---

**2026-03-25T14:45:35 | Артём Фомин**
После установки Zapret2 при диагностике в podkop появилась проблема. Пишет, что найдены дополнительные правила маркировки. При этом podkop работает нормально, заблокированные сайты открываются.

Это нормально, или может необходимо что-то настроить?

---

**2026-03-25T14:55:03 | Артём Фомин**
Народ, как полагаю, ZeroBlock выполняет те же функции что и podkop. Так что лучше из них поставить?

---

**2026-03-25T15:46:12 | Sergio K**
global_check 
 📡 Global check run!
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛠 System info
🕳 Podkop:        v0.7.14 (latest: 0.7.14)
🕳 LuCI App:      v0.7.14
📦 Sing-box:      1.12.22
🛜 OpenWrt:       RouteRich 24.10.5 r29087-d9c5716d1d RR-3.9.0
🛜 Device:        Routerich AX3000
━━━━━━━━━━━━━━━━━━━━━━━━━━━
➡️ DNS status
✅ Bootstrap DNS: 8.8.8.8
✅ Main DNS: 8.8.8.8 [doh]
✅ DNS on router
⚠️ dont_touch_dhcp is enabled. 📄 DHCP config:
config dnsmasq
  option domainneeded '1'
  option localise_queries '1'
  option rebind_protection '1'
  option rebind_localhost '1'
  option local '/lan/'
  option domain 'lan'
  option expandhosts '1'
  option nonegcache '1'
  option cachesize '0'
  option authoritative '1'
  option readethers '1'
  option leasefile '/tmp/dhcp.leases'
  option localservice '1'
  option ednspacket_max '1232'
  option dnsforwardmax '2048'
  option min_cache_ttl '600'
  option max_cache_ttl '86400'
  option confdir '/tmp/dnsmasq.d'
  option strictorder '1'
  option filter_aaaa '1'
  list server '127.0.0.1#5359'

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 Sing-box status
✅ Sing-box installed
✅ Sing-box version is compatible (newer than 1.12.4)
✅ Sing-box service exist
✅ Sing-box autostart disabled
✅ Sing-box process running
✅ Sing-box listening ports
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧱 NFT rules status
✅ Table exist
✅ Rules mangle exist
✅ Rules mangle counters
✅ Rules mangle output exist
✅ Rules mangle output counters
✅ Rules proxy exist
✅ Rules proxy counters
✅ Additional marking rules found
━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 Podkop config

config settings 'settings'
  option dns_type 'doh'
  option dns_server '8.8.8.8'
  option bootstrap_dns_server '8.8.8.8'
  option dns_rewrite_ttl '60'
  option enable_output_network_interface '0'
  option enable_badwan_interface_monitoring '0'
  option enable_yacd '0'
  option disable_quic '1'
  option update_interval '1d'
  option download_lists_via_proxy '1'
  option dont_touch_dhcp '1'
  option config_path '/etc/sing-box/config.json'
  option cache_path '/tmp/sing-box/cache.db'
  option exclude_ntp '1'
  option shutdown_correctly '0'
  option download_lists_via_proxy_section 'main'
  list source_network_interfaces 'br-lan'
  option log_level 'warn'

config section 'main'
  option connection_type 'proxy'
  option proxy_config_type 'outbound'
  option enable_udp_over_tcp '0'
  option shutdown_correctly '1'
  option user_domain_list_type 'text'
  option user_subnet_list_type 'disabled'
  option mixed_proxy_enabled '0'
  option outbound_json 'MASKED'
  option user_domains_text 'myip.com
rutor.info
youtube.com'
  list community_lists 'google_ai'
  list community_lists 'meta'
  list community_lists 'telegram'
  list community_lists 'google_play'
  list community_lists 'geoblock'
  list community_lists 'block'

config section 'Youtube_Discord'
  option connection_type 'vpn'
  option interface 'awg10'
  option domain_resolver_enabled '0'
  option user_domain_list_type 'text'
  option user_subnet_list_type 'disabled'
  option mixed_proxy_enabled '0'
  option user_domains_text '2ip.ru amazonaws.com whatsapp.com whatsapp.net whatsapp.biz wa.me'
  list remote_subnet_lists 'https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_cidr_ipv4.txt'
  list community_lists 'discord'
  list community_lists 'youtube'

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 WAN config
config interface 'wan'
  option device 'wan'
  option proto 'dhcp'
  option metric '40'

━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ WARP detected: 162.159.192.10
━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ Zapret detected
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🥸 FakeIP status
✅ Router DNS is routed through sing-box
✅ Sing-box works with FakeIP: 198.18.0.80

---

**2026-03-25T15:57:17 | Илья**
День добрый, не подскажите, что можно сделать с сегодняшнего дня поперла реклама на ютубе, podkop настроен через собственный прокси.

---

**2026-03-25T16:02:35 | Sergio K**
global_check 
 📡 Global check run!
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛠 System info
🕳 Podkop:        v0.7.14 (latest: 0.7.14)
🕳 LuCI App:      v0.7.14
📦 Sing-box:      1.12.22
🛜 OpenWrt:       RouteRich 24.10.5 r29087-d9c5716d1d RR-3.9.0
🛜 Device:        Routerich AX3000
━━━━━━━━━━━━━━━━━━━━━━━━━━━
➡️ DNS status
✅ Bootstrap DNS: 9.9.9.9
✅ Main DNS: 1.1.1.1 [doh]
✅ DNS on router
⚠️ dont_touch_dhcp is enabled. 📄 DHCP config:
config dnsmasq
  option domainneeded '1'
  option localise_queries '1'
  option rebind_protection '1'
  option rebind_localhost '1'
  option local '/lan/'
  option domain 'lan'
  option expandhosts '1'
  option nonegcache '1'
  option cachesize '0'
  option authoritative '1'
  option readethers '1'
  option leasefile '/tmp/dhcp.leases'
  option localservice '1'
  option ednspacket_max '1232'
  option dnsforwardmax '2048'
  option min_cache_ttl '600'
  option max_cache_ttl '86400'
  option confdir '/tmp/dnsmasq.d'
  option strictorder '1'
  option filter_aaaa '1'
  list server '127.0.0.1#5359'

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 Sing-box status
✅ Sing-box installed
✅ Sing-box version is compatible (newer than 1.12.4)
✅ Sing-box service exist
✅ Sing-box autostart disabled
✅ Sing-box process running
✅ Sing-box listening ports
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧱 NFT rules status
✅ Table exist
✅ Rules mangle exist
✅ Rules mangle counters
✅ Rules mangle output exist
✅ Rules mangle output counters
✅ Rules proxy exist
✅ Rules proxy counters
✅ Additional marking rules found
━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 Podkop config

config settings 'settings'
  option dns_type 'doh'
  option dns_server '1.1.1.1'
  option bootstrap_dns_server '9.9.9.9'
  option dns_rewrite_ttl '60'
  option enable_output_network_interface '0'
  option enable_badwan_interface_monitoring '0'
  option enable_yacd '0'
  option disable_quic '1'
  option update_interval '1d'
  option download_lists_via_proxy '1'
  option dont_touch_dhcp '1'
  option config_path '/etc/sing-box/config.json'
  option cache_path '/tmp/sing-box/cache.db'
  option exclude_ntp '1'
  option shutdown_correctly '0'
  option download_lists_via_proxy_section 'main'
  list source_network_interfaces 'br-lan'
  option log_level 'warn'

config section 'main'
  option connection_type 'proxy'
  option proxy_config_type 'outbound'
  option enable_udp_over_tcp '0'
  option shutdown_correctly '1'
  option user_domain_list_type 'text'
  option user_subnet_list_type 'disabled'
  option mixed_proxy_enabled '0'
  option outbound_json 'MASKED'
  option user_domains_text 'myip.com
rutor.info
youtube.com'
  list community_lists 'google_ai'
  list community_lists 'meta'
  list community_lists 'telegram'
  list community_lists 'google_play'
  list community_lists 'geoblock'
  list community_lists 'block'

config section 'Youtube_Discord'
  option connection_type 'vpn'
  option interface 'awg10'
  option domain_resolver_enabled '0'
  option user_domain_list_type 'text'
  option user_subnet_list_type 'disabled'
  option mixed_proxy_enabled '0'
  option user_domains_text '2ip.ru amazonaws.com whatsapp.com whatsapp.net whatsapp.biz wa.me'
  list remote_subnet_lists 'https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_cidr_ipv4.txt'
  list community_lists 'discord'
  list community_lists 'youtube'

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 WAN config
config interface 'wan'
  option device 'wan'
  option proto 'dhcp'
  option metric '40'

━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ WARP detected: 162.159.192.10
━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ Zapret detected
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🥸 FakeIP status
✅ Router DNS is routed through sing-box
✅ Sing-box works with FakeIP: 198.18.0.34

---

**2026-03-25T17:02:36 | Kiss_My_Axe**
Странно. После установки ZB, или Podkop DoH, на настройках роутера по умолчанию, отмирает самостоятельно.
А если он мешал, значит настройки были не по умолчанию.

---

**2026-03-25T17:42:51 | Михаил Корнев**
Включил автоматическую установку и обновление в терминале:
sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)

---

**2026-03-25T19:22:14 | :)**
Помогите разобраться, используется podkop, на телевизоре LG на web os все работало как и на других устройствах, до сегодняшнего дня,  теперь на тв и про входе в ютуб зависает прогрузка и все, пробовал перезапускать тв, удалял/ставил обратно, выключал из розетки

---

**2026-03-25T21:39:30 | Anna Bagler**
Службы - Podkop, вкладка Настройки. Ищем основной днс и бутстрап, меняем, проверяем.

---

**2026-03-25T22:59:42 | Артём Фомин**
Народ, а ZeroBlock можно поставить на другой роутер? У дочки «Xiaomi Mi Router 3G» с ванильным OpenWRT 24.10.5. Прекрасно работает Podkop. Хотел бы также попробовать в связке ZeroBlock и Zapret2. Оперативной памяти на этом роутере 256 Мб. Процессор двухъядерный MT7621A 880 МГц.

---

**2026-03-25T23:36:24 | Yuriy**
Привет! youtubeunblock полдня работает потом падает.

Routerich AX3000
RouteRich 24.10.5 r29087-d9c5716d1d RR-3.9.0 / LuCI openwrt-24.10 branch 26.081.63927~e56e710

Стоит podkop v0.7.14 

youtubeunblock выдает вот такое:
Wed Mar 25 14:36:43 2026 daemon.info youtubeUnblock[4951]: mnl_cb_run: Operation not permitted 
Wed Mar 25 14:36:43 2026 daemon.info youtubeUnblock[4951]: Probably another instance of youtubeUnblock with the same queue number is running 
Wed Mar 25 14:36:43 2026 daemon.info youtubeUnblock[4951]: Thread 0 exited with status -1: Operation not permitted

Поставил zapret2 после таких вылетов - но он пока выключенный и автозапуск выключен

---

**2026-03-26T09:52:07 | Den Kihot**
podkop точно не работает

---

**2026-03-26T11:05:26 | Linar**
Здравствуйте.
У меня установлен  Podkop 0.7.10.
Написано что устарел. Делаю все по инструкции, но ничего не происходит.

---

**2026-03-26T11:58:07 | Rockey**
всем привет! позавчера взял роутерич, настроил после основого ротера, настроил amnezi wg. все работает!

но теперь пытаюсь разделить трафик амнезии чтобы только на зарубежные сайты шел. А сайты ру открвались без амнезии.
Что лучше для этого использовать?
пытался настроить podkop но там sing-box мешает
чатжпт предлагает PBR? это правильный путь?
или есть ещё варианты?

---

**2026-03-26T12:13:20 | Linar**
Podkop заработал. Ютуб, роблокс и прочее работает. А вот ранее У меня работал rutor.info, а сейчас еле еле открывается

---

**2026-03-26T12:39:00 | Routerich**
Здравствуйте.
а как вы поняли что он через него идёт?
остановили Podkop и проверили?

---

**2026-03-26T13:12:50 | Routerich**
а если Podkop остановить то ок становится?

---

**2026-03-26T19:17:30 | Sandro Flecher**
Добрый день! Подскажите, пожалуйста. Стоит zapret2 + podkop. Раздельная маршрутизация нормально настроена. Но проблемы с blockcheck2, вечная ошибка "curl: (28) Connection timed out after 1500 milliseconds UNAVAILABLE code=28". 
Подскажите куда копать.

---

**2026-03-26T21:37:17 | Sandro Flecher**
Подскажите ещё. Как решить проблему: при перезагрузке роутера с podkop+zapret2 без ручного перезапуска запрета он не работает фактически.

---

**2026-03-26T21:52:34 | Sandro Flecher**
Запрет переустанавливал через репозиторий. Podkop и zapret2 от routerich последней версии. Openwrt 24.10.5. Но спасибо, попробую еще

---

**2026-03-26T23:04:35 | Routerich**
https://podkop.net/docs/tunnels/awg_settings/ пункт установка пакетов пропустить, далее зероблок или подкоп ставьте и там маршрутизируйте

---

**2026-03-27T00:07:57 | Роман**
С чем угодно, хоть zeroblock, хоть podkop. Но со своим сервером.

---

**2026-03-27T20:27:09 | None**
Снести все и переустановить начисто?как конфиги tailscale и podkop зачистить?
Upd podkop глючит 
Основной DNS
family.adguard-dns.com [doh]
Счётчики правил mangle output
Найдены дополнительные правила маркировки
 DNS роутера не проходит через sing-box

---

**2026-03-27T22:05:30 | IIlIlIlIIlIlIlIIIll**
Как только поставил DOH в Podkope и xbox dns и очистил кэш в браузере то все заработало. И еще я очистил в DHCP и ДНС в перенаправлениях все и оставил только  127.0.0.42. спасибо добрым и знающим людям 😀

---

**2026-03-27T23:20:25 | Екатерина**
Анализ запущен: 2026-03-27 23:18:13
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.4.82 | YouTube IP:  198.18.0.151

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.72 MB / ↑0.33 MB
  Пинг (ya.ru via awg10): 7.951 / 15.374 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop zapret opera-proxy youtubeUnblock

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Внутреннее пересечение в podkop:
    podkop                    : Discord (Условия: default)
    podkop                    : main (Условия: default)
    Домены: youtube.com 

  !!!_КРИТ: Пересечение между podkop и zapret:
    podkop                    : main
    zapret                    : zapret-hosts-google.txt
    Домены: googlevideo.com youtube.com 

  !!!_КРИТ: Пересечение между podkop и youtubeUnblock:
    podkop                    : main
    youtubeUnblock            : YouTube
    Домены: googlevideo.com youtube.com 

  !!!_КРИТ: Пересечение между zapret и youtubeUnblock:
    zapret                    : zapret-hosts-google.txt
    youtubeUnblock            : YouTube
    Домены: ggpht.com googleapis.com googleusercontent.com googlevideo.com youtu.be youtube.com ytimg.com 

  podkop            Discord (vpn): discord,telegram
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai,youtube
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  podkop юзерсписки: !!!_roblox.com → Discord, main
  podkop юзерсписки: !!!_youtube.com → Discord, main
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.50 | RAM: 24% | NAND: 27% занято / 49.2M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

root@RouteRich:~# ^C

root@RouteRich:~#

---

**2026-03-28T15:01:49 | Nikita**
подскажите, пожалуйста по вопросу:

роутерич на 256 мб, настроен удаленный доступ по инструкциям тут (remote control, tailscale, роутер стоит очень-очень далеко), прошивка - 24.10.4 - r28959-29397011cc

если я обновлюсь используя ASU - возможность удаленного подключения после обновления останется или нет? критически важно его сохранить + podkop (стоит старая-древняя версия без обновленных списков и фич, хотелось бы удаленно привести все в порядок и починить еще ютуб)

---

**2026-03-28T15:03:48 | Nikita**
как правильно поступить? сейчас из жалоб - сжирается вся оперативка (свободно 5-10 мб буквально), вечно отваливается youtubeunblock/zapret (не хватает памяти по факту), podkop живет кое-как. 

хотелось бы все обновить, сохранив доступы удаленные + настроить все максимально оптимально, чтоб памяти хватало

---

**2026-03-28T15:57:01 | Anna Bagler**
Тогда YouTube убирайте из podkop и пробуйте https://t.me/routerich/3845/509958 для запрета.
Телеграм без звонков - в секцию main перенести. Или свой vless прикрутить к подкопу.

---

**2026-03-28T17:49:49 | Писарев Андрей**
Отличительные характеристики ZeroBlock и Podkop:

Несмотря на то, что оба продукта базируются на движке sing-box и используют технологию FakeIP для прозрачной маршрутизации на OpenWrt, ZeroBlock представляет собой значительно более комплексную и автоматизированную надстройку по сравнению с Podkop.

Вот основные отличительные характеристики, которые разделяют эти две системы:

### 1. Мультидвижковая архитектура
В то время как Podkop ориентирован на чистый sing-box, ZeroBlock использует гибридную схему:
*   Основной движок: sing-box.
*   Вспомогательный движок: xray-core — подключается только для работы с транспортами xhttp и mKCP, которые не поддерживаются основным движком.
*   Собственные туннели: Интеграция с TrustTunnel для создания шифрованных соединений через HTTP/2 и HTTP/3 (QUIC).

### 2. Уровень автоматизации и экосистема (Auto-config)
ZeroBlock нацелен на принцип «поставил и забыл», особенно на устройствах RouteRich:
*   Автонастройка: Наличие вкладки «Автонастройка», которая в один клик устанавливает и настраивает AmneziaWG (WARP), Opera Proxy, Xray, Zapret2 и TrustTunnel.
*   Автозагрузка секций: Поддержка API V2 позволяет роутеру автоматически скачивать готовые наборы правил маршрутизации с сервера, избавляя пользователя от ручного ввода доменов.
*   Health Monitor: В ZeroBlock встроен модуль самовосстановления, который мониторит состояние компонентов (например, пингует WARP или Opera Proxy) и автоматически перезапускает их в случае сбоя.

### 3. Интеграция с DPI-обходом
ZeroBlock имеет нативную совместимость с инструментом zapret2. Система использует специальную метку desync_mark (0x40000000) для координации трафика: это гарантирует, что пакеты, уже прошедшие через прокси, не будут повторно обрабатываться модулем обхода DPI, что критично для стабильности соединения и нагрузки на процессор.

### 4. Расширенное управление списками (API V2)
В отличие от стандартных подходов Podkop, ZeroBlock разделяет списки на API V1 и API V2:
*   API V2 предоставляет расширенные CIDR-списки (подсети) для CDN-провайдеров и мессенджеров, что позволяет корректно маршрутизировать сервисы, работающие напрямую по IP (например, Discord Voice или Telegram).
*   Mixed-списки: ZeroBlock умеет парсить файлы, где домены и IP-адреса перемешаны, автоматически разделяя их для DNS-маршрутизации и правил nftables.

### 5. Дополнительный функционал «из коробки»
ZeroBlock включает в себя модули, которые в Podkop потребовали бы ручной настройки через конфиги:
*   Родительский контроль: Полноценный интерфейс для блокировки интернета или конкретных сайтов по расписанию (время начала/конца, дни недели) для определенных MAC/IP-адресов.
*   URLTest: Встроенный механизм автоматического выбора самого быстрого прокси-сервера из списка на основе текущей задержки.
*   Clash API & YACD: Встроенная поддержка API и графической панели управления для мониторинга трафика в реальном времени и переключения нод прямо из интерфейса роутера.

### 6. Конфликт-менеджмент
ZeroBlock технически осведомлен о существовании конкурента: при запуске система автоматически проверяет наличие установленного Podkop (а также mwan3 или pbr) и предупреждает о возможных конфликтах в правилах nftables.

Резюме: Podkop — это «чистый» инструмент для тех, кто предпочитает ручной контроль. ZeroBlock — это тяжеловесный комбайн с развитой автоматизацией, собственным облачным API для списков и продвинутой системой мониторинга состояния сервисов.

---

**2026-03-28T19:19:21 | Routerich**
Система - пакеты - обновить списки - вкладка обновления - обновить пакеты amneziawg - далее https://podkop.net/docs/tunnels/awg_settings/ пункт установка пакетов пропустить. Создаете интерфейс - испольуете его в подкопе или зероблоке

---

**2026-03-28T20:12:15 | Sanchopance**
Обновите прошивку, накатите tail и zero или podkop

---

**2026-03-29T10:35:03 | Routerich**
запусти подкоп и покажи nft list table inet Podkoptable

---

**2026-03-29T10:37:10 | Routerich**
nft list table inet PodkopTable

---

**2026-03-29T10:37:25 | Arty Soloviev**
root@RouteRich:~# nft list table inet Podkoptable
Error: No such file or directory

---

**2026-03-29T10:39:52 | Routerich**
nft list table inet PodkopTable > /tmp/podkoptable.txt
потом из nas забери

---

**2026-03-29T10:45:50 | Михаил Иванович**
А где лог взять :)


Анализ запущен: 2026-03-29 10:43:11
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.15 | YouTube IP:  198.18.0.16

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.34 MB
  Пинг (ya.ru via awg10): 33.805 / 37.678 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop zapret opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Пересечение между podkop и zapret:
    podkop                    : Youtube_Discord
    zapret                    : zapret-hosts-google.txt
    Домены: googlevideo.com youtube.com 

  podkop    Youtube_Discord (vpn): youtube,discord,telegram
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.01 | RAM: 21% | NAND: 26% занято / 50.0M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

root@RouteRich:~#

---

**2026-03-29T10:49:07 | Kiss_My_Axe**
Службы - Zapret, Стоп, Отключить.
Службы - Podkop, настройки, заменить 8.8.8.8/8.8.8.8 на 9.9.9.9/8.8.8.8
Сохранить, Применить, проверить.

---

**2026-03-29T11:07:24 | Михаил Иванович**
еще раз запустил ваш скрипт:Анализ запущен: 2026-03-29 11:05:09
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.3 | YouTube IP:  198.18.0.4

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.68 MB / ↑0.33 MB
  Пинг (ya.ru via awg10): 32.826 / 35.639 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop    Youtube_Discord (vpn): youtube,discord,telegram
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: 9.9.9.9 / 8.8.8.8
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.34 | RAM: 21% | NAND: 26% занято / 50.3M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

root@RouteRich:~#

---

**2026-03-29T11:19:28 | Alexei**
Подавил podkop с параметрами по умолчанию - ютуб работает, но зависает. Переместил youtube из конфигурации youtube_discord в конфигурацию main - стало работать гораздо быстрее. 😊

---

**2026-03-29T11:25:16 | Alexei**
У меня в службах просто Zapret стоит - я так понимаю, он вместе с podkop встал.

---

**2026-03-29T14:03:55 | Vlad**
Обновил только что прошивку с удалением конфигов. Запустил скрипт №5. Установился не самый свежий подкоп podkop-v0.7.10-r1-all.ipk
Обновился потом до версии v0.7.14

---

**2026-03-29T15:35:12 | Routerich**
На ютубе наберите podkop openwrt, так примерно поймёте как и что делать

---

**2026-03-29T18:48:22 | vanbka9**
0.0.60
Перезапускаем интерфейсы




Анализ запущен: 2026-03-29 18:46:57
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.2.102 | YouTube IP:  198.18.0.11

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.37 MB
  Пинг (ya.ru via awg10): 7.442 / 13.729 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop    Youtube_Discord (vpn): youtube,discord
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai,telegram
Usage: uci [<options>] <command> [<arguments>]

Commands:
        batch
        export     [<config>]
        import     [<config>]
        changes    [<config>]
        commit     [<config>]
        add        <config> <section-type>
        add_list   <config>.<section>.<option>=<string>
        del_list   <config>.<section>.<option>=<string>
        show       [<config>[.<section>[.<option>]]]
        get        <config>.<section>[.<option>]
        set        <config>.<section>[.<option>]=<value>
        delete     <config>[.<section>[[.<option>][=<id>]]]
        rename     <config>.<section>[.<option>]=<name>
        revert     <config>[.<section>[.<option>]]
        reorder    <config>.<section>=<position>

Options:
        -c <path>  set the search path for config files (default: /etc/config)
        -C <path>  set the search path for config override files (default: /var/run/uci)
        -d <str>   set the delimiter for list values in uci show
        -f <file>  use <file> as input instead of stdin
        -m         when importing, merge data into an existing package
        -n         name unnamed sections on export (default)
        -N         don't name unnamed sections
        -p <path>  add a search path for config change files
        -P <path>  add a search path for config change files and use as default
        -t <path>  set save path for config change files
        -q         quiet mode (don't print error messages)
        -s         force strict mode (stop on parser errors, default)
        -S         disable strict mode
        -X         do not use extended syntax on 'show'

  podkop DNS/Bootstrap DNS: () 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.51 | RAM: 25% | NAND: 28% занято / 47.7M доступно
  */10 * * * *  /usr/share/wginstaller/wg.sh cleanup_wginterfaces
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-03-29T21:13:55 | Роман**
Для игры в Infection Free Zone достаточно доменов

openstreetmap.org
jutsugames.com
maptiler.com

Добавлять в список пользовательских доменов zeroblock/podkop.
P.S Open Street Maps сомневаюсь что нужно, закинул докучи 😁
#games

---

**2026-03-29T23:41:55 | KaCD**
Прошу прощения, за моё первое сообщение почему-то получил запрет до 23:39
Вот что команда выдала:

Анализ запущен: 2026-03-29 23:39:36
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

+= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.6 | YouTube IP:  64.233.162.91

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.16 MB
  Пинг (ya.ru via awg10): 15.198 / 16.114 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop zapret opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop            Discord (vpn): discord
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai,telegram
Usage: uci [<options>] <command> [<arguments>]

Commands:
        batch
        export     [<config>]
        import     [<config>]
        changes    [<config>]
        commit     [<config>]
        add        <config> <section-type>
        add_list   <config>.<section>.<option>=<string>
        del_list   <config>.<section>.<option>=<string>
        show       [<config>[.<section>[.<option>]]]
        get        <config>.<section>[.<option>]
        set        <config>.<section>[.<option>]=<value>
        delete     <config>[.<section>[[.<option>][=<id>]]]
        rename     <config>.<section>[.<option>]=<name>
        revert     <config>[.<section>[.<option>]]
        reorder    <config>.<section>=<position>

Options:
        -c <path>  set the search path for config files (default: /etc/config)
        -C <path>  set the search path for config override files (default: /var/run/uci)
        -d <str>   set the delimiter for list values in uci show
        -f <file>  use <file> as input instead of stdin
        -m         when importing, merge data into an existing package
        -n         name unnamed sections on export (default)
        -N         don't name unnamed sections
        -p <path>  add a search path for config change files
        -P <path>  add a search path for config change files and use as default
        -t <path>  set save path for config change files
        -q         quiet mode (don't print error messages)
        -s         force strict mode (stop on parser errors, default)
        -S         disable strict mode
        -X         do not use extended syntax on 'show'

  podkop DNS/Bootstrap DNS: () 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.10.1 (Прошивка: 24.10.4)
  CPU: 0.14 | RAM: 24% | NAND: 26% занято / 49.3M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

root@RouteRich:~# +

---

**2026-03-30T05:27:11 | Владимир**
Анализ запущен: 2026-03-30 09:21:05
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.1.42 | YouTube IP:  198.18.1.33

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.31 MB
  Пинг (ya.ru via awg10): 68.152 / 70.119 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop zapret opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Пересечение между podkop и zapret:
    podkop                    : main
    zapret                    : zapret-hosts-google.txt
    Домены: googlevideo.com youtube.com 

  Версия podkop: v0.6.2

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.2.1 (Прошивка: 24.10.4)
  CPU: 0.38 | RAM: 45% | NAND: 23% занято / 51.1M доступно
  0 4 * * * service zapret restart
  13 9 * * * /usr/bin/podkop list_update

root@RouteRich:~#

---

**2026-03-30T06:05:28 | Владимир**
обновил версии podkop и zapret, теперь вот так

---

**2026-03-30T06:07:00 | Владимир**
Анализ запущен: 2026-03-30 10:01:40
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: !!!_ПЕРЕНАПРАВЛЕНИЯ ОТСУТСТВУЮТ
  Facebook IP:  127.0.0.1 | YouTube IP:  142.251.211.174

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.45 MB
  Пинг (ya.ru via awg10): 72.297 / 74.196 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop sing-box zapret opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | STOPPED (MANAGED BY PODKOP)    | РАЗРЕШЁН
  zapret          | STOPPED                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Пересечение между podkop и zapret:
    podkop                    : main
    zapret                    : zapret-hosts-google.txt
    Домены: googlevideo.com youtube.com 

  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.2.1 (Прошивка: 24.10.4)
  CPU: 0.49 | RAM: 39% | NAND: 26% занято / 49.6M доступно
  0 4 * * * service zapret restart

root@RouteRich:~#

---

**2026-03-30T08:12:02 | ⓞ ᗰ**
Доброго всем дня! Скрипт 5 решил почти все проблемы, благодарю всех причастных! Podkop 👍 Ютуб, дискорд, все работает. Roblox также починился благодаря тутошним советам🫶 Столкнулись теперь с проблемой по Brawl stars. Есть ли сейчас рабочие решения не ломающие всё достигнутое? Если есть, прошу подробно для чайников. Заранее благодарю!

---

**2026-03-30T08:27:15 | Routerich**
Здравствуйте.
отследить домены на которые игра обращается и добавить в Podkop.

---

**2026-03-30T08:53:34 | Routerich**
столбец K
в пользовательские домены Podkop, в секцию main

---

**2026-03-30T10:41:01 | Bullet for my valentine Poison**
Сначала обновить пакеты amneziawg в Система - пакеты - обновить списки - вкладка обновления. Далее сеть - интерфейсы - там добавить свой конфиг амнезии https://podkop.net/docs/tunnels/awg_settings/#nastrojka-cherez-luci (пункт с установкой пакетов пропустить) - и там импортировать конфиг. Все делать в режиме инкогнито в браузере

---

**2026-03-30T12:17:22 | Routerich**
не добавлять их в Podkop

---

**2026-03-30T23:16:31 | Святос**
sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)

---

**2026-03-31T00:36:03 | Jelani**
Всем привет. Подскажите, есть ли какой нибудь нормальный видео туториал по настройке Routerich с полного нуля? Для прям совсем новичков?

Я имею ввиду не первый запуск, а настройку всяких Podkop, Zapret, VLESS, X-ray и что там ещё есть.

Подскажите пожалуйста.

---

**2026-03-31T00:36:47 | Jelani**
Всем привет. Подскажите пжл, есть ли какой нибудь нормальный видео туториал по настройке Routerich с полного нуля? Для прям совсем новичков?

Я имею ввиду не первый запуск, а настройку всяких Podkop, Zapret, VLESS, X-ray и что там ещё есть.

Подскажите пожалуйста.

---

**2026-03-31T00:49:31 | A**
Не дает ничего установить. Пробую podkop и zapret2

---

**2026-03-31T02:19:03 | Дедус Механикус ©**
На сайт Podkop зайти. Найти на главной странице строку для Автоматической установки и обновления. В роутере вставить в терминале и запустить. Profit.

---

**2026-03-31T09:30:04 | Routerich**
Здравствуйте.
Он добавлен у вас в список для обхода скорее всего.
Попробуйте остановить zeroblock/podkop и проверить, сможете войти или нет

---

**2026-03-31T09:30:40 | The Wisest**
Podkop всё?

---

**2026-03-31T09:31:29 | Routerich**
Здравствуйте.
В настройках Podkop поставьте/уберите галочку на скачивать списки через Proxy/VPN

---

**2026-03-31T09:36:08 | Routerich**
А в диагностике Podkop что?

---

**2026-03-31T09:40:50 | Routerich**
https://podkop.net/docs/sections/#polnostyu-marshrutiziruemye-ip-adresa-fully-routed-ips

---

**2026-03-31T09:43:09 | Routerich**
А вы руками ставили Podkop, что у вас в секции main?

---

**2026-03-31T10:39:18 | Evgen**
Подскажите, зказал роутер, там по умолчанию установлены zapret podkop и тд?

---

**2026-03-31T12:08:36 | Evgeny**
не уточнил сразу в podkop. все секции установлены скриптом. насколько я вижу, секция awg реализована через отдельный интерфейс.

---

**2026-03-31T13:10:23 | Routerich**
Ну в настройках Podkop сменить тип протокола dns

---

**2026-03-31T13:26:57 | Сочи**
Мне вообще на него нужно podkop установить, выходила ошибка думал как раз из за интернета, щас попробую еще раз

---

**2026-03-31T15:22:15 | Jelani**
Всем привет ещё раз.

Подскажите пожалуйста... если совсем упростить для чайников, то установка должна выглядеть примерно так по шагам? 

1) Покупаешь роутер и настраиваешь его по базовой инструкции (которая в коробке) - в итоге будет работать самый обычный Wi-Fi + интернет по ethernet кабелю.

2) Потом устанавливаем скрипт #5

3) Потом устанавливаем Zeroblock+Zapret2

*перед установкой чего-л смотрим чтобы Безопасный DNS (в браузере) и Частный DNS (в настройках ПК) был отключен - везде / на всех устройствах где мы хотим чтобы работал VPN
*к тому же смотрим чтобы перед установкой все VPN программы были полностью удалены

Это правильные шаги по идее? Или есть что то важное чего я не указал?

И ещё я не понимаю кое что... Почему все говорят по разному... Некоторые говорят про Podkop, некоторые про Zeroblock, некоторые про Zeroblock opera + awg. У некоторых стоит какой-то youtubeUnblock.

Не ругайте пж за тупой вопрос, но я так понимаю я спрашиваю и нужном месте? 🤔🥸

---

**2026-03-31T19:52:57 | Bullet for my valentine Poison**
Сначала обновить пакеты amneziawg в Система - пакеты - обновить списки - вкладка обновления. Далее сеть - интерфейсы - там добавить свой конфиг амнезии https://podkop.net/docs/tunnels/awg_settings/#nastrojka-cherez-luci (пункт с установкой пакетов пропустить) - и там импортировать конфиг. Все делать в режиме инкогнито в браузере

---

**2026-03-31T20:48:39 | Jelani**
Подскажите как вы решаете что использовать?
Получается есть 2 основных варианта или нет?
1) Установить скрипт #5 (это Podkop)
2) Установить Zeroblock и Zapret2

Или там много разных вариантов просто это два готовых варианта для чайников кто не шарит в сетях?

---

**2026-03-31T23:08:08 | Routerich**
https://podkop.net/docs/sections/#proxy ключи можно

---

**2026-04-01T01:21:26 | Снежный**
Podkop обновлять с v0.7.10 до 0.7.14?
Или не стоит?
Или обновить просто ipk без внешки?

---

**2026-04-01T03:24:49 | Routerich**
https://podkop.net/docs/sections/ это от подкопа но принцип такой же

---

**2026-04-01T10:11:23 | Routerich**
это комбо, и да, в нём Podkop используется.

---

**2026-04-01T10:14:09 | Роман**
recraft.ai
azurefd.net

Эти домены в список пользовательских доменов zeroblock/podkop.

---

**2026-04-01T11:09:13 | Сочи**
Не все так просто походу 😅

Я скачал podkop, вставил туда vless ключ для обхода белых списков, роутер берет интернет от сим карты, думал как раз с впн будет работать интернет там где его глушат, но вот не работает((

Может стоить проверить настройку там где не глушат если все работает, привезти обратно и будет норм?🤔

---

**2026-04-01T16:19:08 | Marseille Gaysin**
Кто нибудь знает где можно найти .srs список для podkop обход FaceTime и сервисы AI

---

**2026-04-01T16:31:10 | Marseille Gaysin**
Вот podkop чтобы он автоматический обновлялся

---

**2026-04-01T16:36:47 | Marseille Gaysin**
аналоги есть podkop ? постоянно вручную добавляю из-за динамического ip адреса и домена. например вчера телега работала, а сегодня нет и пришлось вручную в podkop добавлять из https://iplist.my-handbook.ru/ru

---

**2026-04-01T19:58:43 | Danila**
Здравствуйте! 
Подскажите пожалуйста, стоит следующая задача: разделить трафик на две wifi подсети.
1. Должна быть абсолютно чистой для копроративных устройств, гостей и т.д.
2. Быть максимально свободной.

Для чистой зоны хочу создать гостевую по следующему гайду: https://lsetc.ru/gostevoj-wi-fi-na-openwrt-cherez-luci/
Для свободной зоны планирую использовать Podkop с vless конфигами своими по каскадному типу (я -> РФ -> свобода)

Подскажите, требуются ли какие-то доп настройки для разделения трафика или всё произойдет "автоматически" из-за того, что условный podkop будет смотреть на дефолтный интерфейс?

---

**2026-04-01T20:12:04 | Danila**
То есть правильно ли я понимаю, что если добавлю гостевую сеть и установлю подкоп + ютубанлок, будет выглядеть это так:
1. Гостевая = ютуб анлок
2. Обычная = подкоп + ютуб анлок

Верно?

Если да, меня так устроит, потому что сейчас ютуб анлок стоит и всё ок с корпоративным ноутом.
Важно, чтобы при использовании Podkop трафик не улетел в условную финляндию, потому что тогда будет моментальный бан от ИБ на работе, для этого и хочу разделить сетки.

---

**2026-04-01T22:01:46 | Routerich**
Так, Уже лучше, теперь идите в Система - автозапуск - находите podkop и нажимайте на стоп и на включено. далее сеть - dhcp -dns - перенаправления покажите скрин и чуть дальше файлы resolv и hosts и скрин из службы - dns службы - dns failsafe proxy, 3 скрина от вас

---

**2026-04-02T00:26:57 | Артём Фомин**
Вместо Podkop ставь ZeroBlock. Сделай автонастройку с нужными компонентами, здесь где-то была видеоинструкция, и никакие сторонние VPN не нужны будут

---

**2026-04-02T08:13:56 | Василий**
А по стабильности работы, по вашему мнению, что лучше ZB или podkop?

---

**2026-04-02T09:24:19 | Роман**
Всё зависит от настроек, никакой волшебной кнопки (чтобы всё работало) нет. Podkop/zeroblock лишь инструменты для проксирования трафика, как настроите - так и будет.

---

**2026-04-02T09:32:11 | Роман**
opkg remove podkop
rm -rf /etc/podkop
rm -rf /etc/config/podkop
opkg remove sing-box
reboot 
В терминал.

---

**2026-04-02T10:13:06 | Oleg**
Добрый день! Помогите, плиз! А как можно создать отдельное wi-fi подключение, чтобы оно проходило через podkop целиком , а не только по спискам (иногда такое нужно , когда что-то вдруг не открывается, а нужно )? у меня стоит скрипт 5. Спасибо)

---

**2026-04-02T12:26:51 | Sergei Alekseev**
подскажите плиз кто в теме
настроил wireguard (https://my-handbook.ru/2025/09/06/wireguard-server-openwrt/), трафик русский идет нормально, а вот траф, который должен через впн (podkop) идти,  через него него не идет Где-то видимо какой-то интерфейс нужно пробросить, но не знаю где. Либо телефон не использует DNS роутера

---

**2026-04-02T12:33:09 | Routerich**
Здравствуйте.
В Podkop, нужно добавить интерфейс wireguard, рядом с br-lan

---

**2026-04-02T12:44:56 | karat**
Подскажите пожалуйста, в Zeroblock очередность обработки секций начинается с верхней секции, а как   выставлять приоритет  обработки в секциях Podkop?

---

**2026-04-02T13:14:49 | Юрий**
Читайте закреплённые сообщения, там есть скрипты для установки всего необходимого. Если есть Vless ключ от какого-то приватного впн сервера, то его надо будет вставлять в настройках службы Podkop.

---

**2026-04-02T13:32:20 | karat**
Спасибо. Но я спрашивал за секции в Podkop, а там я подобного не вижу, удалять не хочется, а отключить не получается

---

**2026-04-02T13:38:11 | karat**
Да у меня второй роутер на zeroblock, но в podkop сегодня лучше идет телеграм, решил с ним немножко познакомится

---

**2026-04-02T13:39:36 | Anna Bagler**
https://podkop.net/ - оф. по подкопу.

---

**2026-04-02T13:40:02 | karat**
Хотел проверить свой VPS на podkop? для этого нужно ему сделать приоритет

---

**2026-04-02T14:18:37 | Routerich**
Здравствуйте.
Он может не корректно работать если есть Podkop.
Ставьте zeroblock и ттам родительский контроль есть.

---

**2026-04-02T16:52:55 | Anton Nikolaevich**
Сегодня у меня стал отваливаться Gemini через podkop с 5 скриптом. Настройки никакие не менял. Не подгружает чаты ни на телефоне по Вайфаю, ни через Ethernet на ПК. Через мой сторонний VPN с американским IP - всё пашет. Где копать?

---

**2026-04-02T18:33:29 | Routerich**
Здравствуйте.
Начать со сброса и решить, что вам нужно Podkop или Zeroblock

---

**2026-04-02T20:00:29 | Никита**
Добрый вечер
Где можно найти настройки podkop на самом роутере

---

**2026-04-02T20:02:11 | Anna Bagler**
Службы - Podkop.

---

**2026-04-02T20:03:36 | Anna Bagler**
В меню роутера Службы - Podkop и там уже вкладки, секции, настройки и т.д.

---

**2026-04-02T20:04:03 | Никита**
Нет) как настроить сам podkop внутри?

---

**2026-04-02T20:08:27 | Роман**
Войти в веб интерфейс роутера, службы, podkop. Там настраивайте.

---

**2026-04-02T22:03:59 | Роман**
В подкопе (последней версии) нужно создать новый секцию и в неё вписать исключения. 
podkop.net

---

**2026-04-02T22:24:29 | Anna Bagler**
А если отключить Podkop, я.ру работает?

---

**2026-04-02T23:27:06 | Vlad**
Анализ запущен: 2026-04-02 23:25:05
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.13 | YouTube IP:  142.251.38.110

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓7.44 MB / ↑0.27 MB
  Пинг (ya.ru via awg10): 86.989 / 127.768 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Пересечение между podkop и zapret:
    podkop                    : main
    zapret                    : zapret-hosts-google.txt
    Домены: googleapis.com 

  podkop    Youtube_Discord (vpn): discord
  podkop           main (prx out): geoblock,meta,twitter,hdrezka,google_ai,telegram
  podkop DNS/Bootstrap DNS: (udp) 127.0.0.10 / 8.8.8.8
  Версия podkop: v0.7.14

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.10 | RAM: 30% | NAND: 57% занято / 29.0M доступно
  */2 * * * * /usr/bin/find /tmp -maxdepth 1 -type f -name 'zapret*.log' -size +2600k -exec rm -f {} \;
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-04-02T23:34:05 | Kiss_My_Axe**
= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Пересечение между podkop и zapret:
    podkop                    : main
    zapret                    : zapret-hosts-google.txt
    Домены: googleapis.com 
Неприятное. Как решать - неясно.

Подбирайте. После применения каждой стратегии проверяйте на телефонах-телеках-пека
# СТРАТЕГИИ В ZAPRET1
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)

---

**2026-04-02T23:40:39 | Vlad**
Анализ запущен: 2026-04-02 23:36:27
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.3 | YouTube IP:  142.250.74.14

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓3.70 MB / ↑0.19 MB
  Пинг (ya.ru via awg10): 252.952 / 544.797 ms (0 из 10 потеряно)




Анализ запущен: 2026-04-02 23:37:48
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.3 | YouTube IP:  142.250.74.14

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓2.63 MB / ↑0.16 MB
  Пинг (ya.ru via awg10): 114.104 / 172.952 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop    Youtube_Discord (vpn): discord
  podkop           main (prx out): geoblock,meta,twitter,hdrezka,google_ai,telegram
  podkop DNS/Bootstrap DNS: (udp) 127.0.0.10 / 8.8.8.8
  Версия podkop: v0.7.14

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 1.17 | RAM: 27% | NAND: 57% занято / 29.3M доступно
  */2 * * * * /usr/bin/find /tmp -maxdepth 1 -type f -name 'zapret*.log' -size +2600k -exec rm -f {} \;
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-04-03T00:00:46 | None**
что с ошибкой делать - Podkop Error
Wed Apr 1 19:35:32 2026 user.notice podkop: [error] Outbound section not found. Please check your configuration file (missing proxy_string, selector_proxy_links, urltest_proxy_links, outbound_json, or interface). Aborted.

---

**2026-04-03T07:34:44 | Routerich**
Здравствуйте.
а в Podkop добавили интерфейс TailScale?

---

**2026-04-03T07:37:24 | Routerich**
Службы->Podkop->Настройки->Сетевой интерфейс источника->сюда добавить интерфейс tailscale0

---

**2026-04-03T09:36:38 | Anna Bagler**
Исключить по IP из zero/podkopa.

---

**2026-04-03T10:46:56 | D S**
Добрый день, хотел обновить сегодня Podkop на роутере (RouteRich 24.10.2 r28739-d9340319c6 RR-3.6.6)
- устанавливал Podkop в прошлый раз скриптом #5 (примерно осенью 25го)
Обновлял командой с сайта Podkop (b и еще удалил Getdomains). Пропали все вкладки кроме - основные настройки. Вбил сейчас конфиг, ничего не работает похоже. Подскажите, как переустановить Podkop чтобы в админке Роутера можно было все настроить заново?

---

**2026-04-03T10:52:04 | Артем Погодин**
Теперь другая проблема))
Такого не было с podkop'ом

Есть корпоративный VPN через checkpoint
Вот он не хочет подключаться с включенным zeroBlock. Отключаю - подключается корпоративный

Куда-то что-то в исключения может надо?

---

**2026-04-03T11:06:45 | D S**
вчера отвалилось на проводном инете все кроме яндекса и прочих белосписочных сайтов. Включил запрет 1 на роутере - ютуб заработал. Утром вроде откатили, но я немного сломал Podkop

---

**2026-04-03T12:15:08 | Klmnt**
Всем привет.

Есть кто с МТС из Ростовской области?
Третий день подряд в 9-10 утра  вырубается проводной интернет. Как раз совпадает с временем начала работы. 
после отключения включают примерно с 16 до 19. 


Routerich, воткнут в провайдерский D-link
Podkop
Openwrt 24.10.5

---

**2026-04-03T18:22:31 | Routerich**
https://podkop.net/docs/tunnels/awg_settings/ пункт с установкой пакетов пропускайте и проверяйте

---

**2026-04-03T19:13:08 | Никита**
Если я сброшу модем reset сзади модема 
Слетит что нибудь в модеме 
Например podkop?

---

**2026-04-03T19:14:06 | Никита**
Как из коробки? То есть удалит podkop?

---

**2026-04-03T20:29:17 | Роман**
podkop.net

---

**2026-04-04T00:03:35 | Роман**
Для игры в lineage2ertheia добавьте эти домены и ip в список пользовательских доменов/ip в zeroblock/podkop
lineage2ertheia.com
yani.tv
ajay.app
cloudfront.net
lineage2splendor.com
ip-51-255-64.eu

188.114.97.11
172.67.191.217
51.255.64.201
13.33.216.158
13.33.216.53
188.114.96.11
172.67.191.217
112.175.192.62
Можно ещё добваить CDN:Cloudflare
#games

---

**2026-04-04T10:40:29 | Никита**
Добрый день.

Настроен podkop на роутере (OpenWRT / Routerich AX3000). В целом всё работает корректно:

- интернет есть на всех устройствах  
- ChatGPT, Telegram и другие сервисы открываются  
- sing-box запущен  
- DNS, nftables и outbounds — все проверки проходят успешно  

Однако есть моменты в диагностике и поведении устройств, которые хотелось бы уточнить.

Устройства:
- MacBook Air M1  
- iPhone 13  

---

### 1. Диагностика (LAN / iPhone)

При подключении:
- MacBook Air M1 по LAN  
- iPhone 13 по Wi-Fi  

в диагностике podkop отображается:

> «Прокси-трафик не маршрутизируется через FakeIP»

При этом:
- всё работает стабильно  
- сайты открываются  
- проблем с доступом нет  

---

### 2. Проблема с MacBook Air M1 по Wi-Fi

При подключении MacBook по Wi-Fi:

- открывается только адрес роутера (192.168.1.1)  
- внешние сайты не открываются  

в диагностике отображается:

> «Браузер не использует FakeIP»

При этом:
- прокси на macOS отключён  
- DNS указывает на роутер  
- пробовал DHCP и статический IP — поведение одинаковое  

---

### Вопросы:

Вопрос как починить эти недостатки 

→ «Прокси-трафик не маршрутизируется через FakeIP»
и
→ «Браузер не использует FakeIP»

Буду благодарен за помощь 🙏

---

**2026-04-04T10:44:25 | Name**
У меня тоже сегодня сдох podkop, только через 2vray робит. Изначально подумал сервак заблокирован

---

**2026-04-04T13:06:18 | Роман**
Дополнительные домены и ip для WhatsApp и Telegram - добавлять в список пользовательских доменов/ip в zeroblock/podkop.

#WhatsApp

IP
31.13.64.0/18
57.141.0.0/20
57.144.0.0/14
66.220.144.0/20
69.63.160.0/19
69.171.192.0/18
74.119.76.0/22
129.134.0.0/17
157.240.0.0/16
163.64.0.0/12
173.252.64.0/18
185.60.216.0/22
204.15.20.0/22
3.0.0.0/10


domain
bintray.com
whatsapp.biz
whatsapp.com
whatsapp.net
wa.me
whatsapp-plus.info
whatsapp-plus.me
whatsapp-plus.net
whatsapp.cc
whatsapp.info
whatsapp.org
whatsapp.tv
whatsappbrand.com


#Telegram

IP
91.108.4.0/22
91.108.8.0/22
91.108.16.0/22
91.108.12.0/22
149.154.160.0/20
91.105.192.0/23
91.108.20.0/22
185.76.151.0/24

domain
t.me
telegram.me
telegram.dog
telegra.ph
telesco.pe
telegramdesktop.com
tdesktop.com
fragment.com
cdn-telegram.org
comments.app
contest.com
graph.org
quiz.directory
telegram-cdn.org
telegram.space
tg.dev
tx.me
usercontent.dev
by Vasa


Так-же можно попробовать добавить автоматически обновляемые списки:
domain
https://raw.githubusercontent.com/KharunDima/whatsapp-lists/main/results/domains.txt

IP
https://raw.githubusercontent.com/KharunDima/whatsapp-lists/main/results/cidr_ipv4.txt

Для TG
https://core.telegram.org/resources/cidr.txt

Добавлять в пользовательские списки zeroblock/podkop - вставлять сами ссылки.

Так-же помогает скачать клиент WhatsApp с официального сайта, а не с PlayMarket (не забываем про бэкапы переписок, привязку почты для входа).

---

**2026-04-04T14:33:12 | Владимир Демешко**
Добрый день. В podkop указываем списки для обхода. А кто нибудь знает как сделать, чтобы podkop не трогал вообще списки, которые я пропишу?

---

**2026-04-04T14:57:45 | ㅤㅤ**
Решение найдено для игры MK1, эти домены в zeroblock/podkop:

api.wbgames.com
wb-hydra.wbgames.com
mortalkombat.com
amazonaws.com.
bugs.wbgames.com
telemetry.wbgames.com
cdn.wbgames.com

Плюс скопировать все cidr:

https://github.com/123jjck/cdn-ip-ranges/blob/main/aws/aws_plain_ipv4.txt

Взято из соседнего чата itdog.
#games

---

**2026-04-04T15:16:32 | Данис**
все привет, подскажите в чем проблема, не  работают некоторые сервисы гугл( плеймаркет, гугл докс, почта рваботает) Анализ запущен: 2026-04-04 17:11:01
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.121 | YouTube IP:  198.18.0.122

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.68 MB / ↑0.17 MB
  Пинг (ya.ru via awg10): 36.033 / 41.214 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop zapret opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Пересечение между podkop и zapret:
    podkop                    : Youtube_Discord
    zapret                    : zapret-hosts-google.txt
    Домены: googlevideo.com youtube.com 

  podkop    Youtube_Discord (vpn): youtube,discord
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,telegram
  podkop DNS/Bootstrap DNS: (doh) 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.29 | RAM: 24% | NAND: 36% занято / 43.4M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

root@RouteRich:~# 
root@RouteRich:~#

---

**2026-04-04T15:19:23 | IIlIlIlIIlIlIlIIIll**
Кто знает как сделать так чтобы podkop шел через США, а не как щас через Швецию ? opera-proxy вроде бы поддерживает регион US. Помогите пожалуйста 😔

---

**2026-04-04T17:45:00 | Go Nik**
А вот такие ошибки в Podkop - это нормально?

---

**2026-04-04T19:59:36 | Александр**
А только у меня косяк с сайтом themoviedb.org? Установлена последня прошивка 24.10.5 и zeroblock 0.7.2-r53 если перейти на сайт themoviedb.org то открывается интерфейс роутера. А мне нужен этот сайт для kodi с podkop такой проблемы не было.

---

**2026-04-04T20:00:07 | Денис**
При проверке nslookup fakeip.podkop.fyi выдает по идее правильно

---

**2026-04-04T21:38:20 | Сочи**
пытался настроить впн для обхода белых списков чтобы терминал на точке работал от вай фая принимал оплату, установил podkop поставил vless ключ впн который работает на телефоне и все грузит. На роутере не нет интернета, писал в раздел модемы помогали с насторойками всякое меняли и днс и прочее ничего не помогло

---

**2026-04-05T09:22:04 | Istarot**
Всем добрый день! Подскажите, можно как то what's app реанимировать через podkop?

---

**2026-04-05T10:51:51 | D I**
Уважаемые, вопрос а в чем принципиальная разница Zapret(2)/ZeroBlock/PodKop? и что выбрать, если ничего не стоит/стояло до?

---

**2026-04-05T13:23:08 | Сергей Мокринский**
Анализ запущен: 2026-04-05 13:21:35
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.1.114 | YouTube IP:  198.18.0.21

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.68 MB / ↑0.35 MB
  Пинг (ya.ru via awg10): 38.926 / 46.957 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200 OK) [tlsv1.3] [try: 2]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop    Youtube_Discord (vpn): youtube,discord,telegram
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: (doh) 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10
  Ошибка: DNS и DHCP, Строгий порядок активен!

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.68 | RAM: 22% | NAND: 26% занято / 50.2M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

root@RouteRich:~#

---

**2026-04-05T16:00:59 | YooPita**
добрый день! установил свежую версию скрипта.
иду в podkop/diagnostics, жмякаю run diagostics и вижу, что всё зелёное, кроме DHCP has DNS server — оно почему-то красное

что с этим можно сделать?

---

**2026-04-05T18:19:10 | Routerich**
https://podkop.net/docs/tunnels/awg_settings/ пункт с установкой пакетов пропускайте, ставьте зероблок и там уже выбирайте созданный интерфейс

---

**2026-04-05T18:38:13 | Routerich**
Уберите из списка пакетов podkop пакеты и ещё раз

---

**2026-04-05T22:08:25 | Сущенко Валерий**
Все обновилось. Никаких ошибок не было. Но зашел Система - Службы -  Podkop . Вверху - красная панель - (Podkop Error
Sun Apr 5 22:01:56 2026 user.notice podkop: [error] Download twitter list failed). При этом Ютуб и Телеграмм работают. Что делать?

---

**2026-04-05T22:20:45 | Роман**
Желательно сброс на заводские настройки и на чистую систему устанавливать zeroblock. Но можете удалить способом указанным на podkop.net.

---

**2026-04-05T22:57:25 | Ярослав**
Кстати работает обалдено... 😌 Гораздо быстрее чем через Podkop

---

**2026-04-06T08:00:53 | Slay**
Добрый день! Можете поделиться марулом для podkop пожалуйста

---

**2026-04-06T08:11:08 | Routerich**
Здравствуйте.
https://podkop.net/

---

**2026-04-06T10:17:45 | Routerich**
Ну это одна из секций Podkop)
Ну ок, если ей не пользуетесь.

---

**2026-04-06T10:21:09 | Routerich**
Зайти в Podkop, там выбрать список Telegram

---

**2026-04-06T11:00:04 | Evgeniy Zhukov**
У меня перестал работать podkop (v0.7.14 Sing-box 1.12.22), не подключается к внешнему vless прокси, причем если изнутри сети этого же роутера подключаюсь при помощи Hiddify к этому же Vless прокси то все работает, в podkop проходит все проверки, но выдает ошибку на проверке "Outbounds проверки main Не отвечает" - в чем может быть проблема? До недавних ужесточений (с неделю назад) все работало нормально через podkop.

---

**2026-04-06T11:06:09 | Evgeniy Zhukov**
вот глобал чек с podkop

---

**2026-04-06T11:22:38 | Evgeniy Zhukov**
Как написал в изначальном сообщении - прокси рабочий, подключаюсь к нему клиентом Hiddify, проблема именно при попытке подключения при помощи podkop

---

**2026-04-06T11:32:48 | Evgeniy Zhukov**
Hiddify все-таки более продвинутый клиент чем podkop :(

---

**2026-04-06T11:53:04 | Данила Ступин**
Информация для "счастливых" обладателей умной техники Xiaomi. Как вы уже могли заметить, устройства умного дома перестали подключаться к сети из-за действий "конторы весельчаков".

После долгих поисков решения я наткнулся на информацию с 4pda. Необходимо добавить данные подсети в любую секцию zeroblock/podkop (warp/opera/vless). Zapret мне не помог в данном случае.

107.155.51.0/24
107.155.52.0/24
107.155.53.0/24

После проброса этих сетей в zeroblock (warp) у меня всё заработало. Xiaomi вроде обещали это починить конечно, но ждать можно долго)

---

**2026-04-06T13:48:23 | труляля🧑‍🦲#отвальный #mimilover #create #Print("helloworld")**
Чем отличается podkop от zapret и от zapret 2?

---

**2026-04-06T13:50:02 | Routerich**
Podkop средство маршрутизации
Zapret, Zapret2 это дурилки dpi

---

**2026-04-06T14:48:41 | Bumbon4ik**
Ну роутере установить MTproxy, который будет работать через zeroblock/podkop через amneziawg.

Дальше в телеграме с прописываю свой ip mtproxy, и работаю через него уже.

---

**2026-04-06T15:27:45 | Routerich**
Ну тогда удалить из Podkop список YouTube, и установить zapret2 и подбирать стратегию под него

---

**2026-04-06T18:04:40 | Routerich**
Тогда попробуйте стопнуть Podkop, Zapret открывается приложение?

---

**2026-04-06T18:37:36 | VillainRU**
Ребят подскажите, поставил недавно tailscale, начал ребутаться от нехватки памяти, как починить можно? Стоит podkop если, что, gemini говорит тейлскейл + подкоп много памяти кушают, так же видел инфу что можно с флешки сделать свап памяти и увеличить ОЗУ, насколько это решит проблему, учитывая что скорость флешки меньше гораздо? У меня один из первых ваших ротеров

---

**2026-04-06T18:56:34 | Роман**
https://podkop.net/docs/troubleshooting/

---

**2026-04-06T21:10:37 | Droopy**
Подскажите пожалуйста, в чем мб проблема 
Установил podkop, все списки добавил. Работает все, кроме ютуба и всего гугловского. Отдельно в списки их добавлял, что только уже не делал

---

**2026-04-06T22:37:26 | MeSSiR**
так я с чаем к компу как раз пришёл)) а тут уже всё частично прилегло 😂😂 
для понимания, переход в podkop.net недоступен)))

---

**2026-04-06T22:40:01 | Aleksey Vydrin**
скажу страшное. https://podkop.net/ работает без проблем. в РФ только не резовится

---

**2026-04-06T22:46:09 | Aziz**
У меня в podkope сегодня реклама появилась, до этого не было

---

**2026-04-07T04:23:30 | Константин**
Походу действо связано с днс. У меня локальный днс сервер развернут и не проходят doh запросы к апстрим списку. Попробуйте сменить podkop zeroblock протокол doh апстрим 9.9.9.9 бустрап 78.88.8.8 из списка. Такое временное решение пока работает у меня

---

**2026-04-07T05:28:39 | Routerich**
Попробуйте сменить днс сервере в настройках Podkop на 9.9.9.9

---

**2026-04-07T07:51:22 | Sergei Arnaut**
Для тех у кого не удается войти в  Ubisoft Connect просто добавьте в Podkop в Main(proxy) следующие хосты: akamai.net
akamaized.net
akamaihd.net
edgesuite.net
gvt1.com
google-analytics.com
akamaized.net
authentication.ubisoft.com
awsglobalaccelerator.com
cdn.ubisoft.com
connect.cdn.ubisoft.com
connect.ubisoft.com
dd.ubisoft.com
digicert.com
dmx.upc.ubisoft.com
files.cdn.ubisoft.com
public-ubiservices.ubi.com
public-ws-ubiservices.ubi.com
ubi.com
ubiservices.cdn.ubi.com
ubisoft.com
uplay-pc.ubisoft.com
uplay.com

---

**2026-04-07T08:16:44 | Routerich**
Здравствуйте.
https://podkop.net/docs/tunnels/awg_settings/

---

**2026-04-07T08:48:38 | Grigoriy Orlov**
А если обновить прошивку, или заново запустить скрипт все настройки в podkop слетят?

---

**2026-04-07T09:51:43 | Denis**
user.notice podkop: [error] Download telegram list failed

Галку Скачивать списки через Proxy/VPN снимал/ставил, не помогло. 

Как побороть?

---

**2026-04-07T09:53:38 | Routerich**
а покажите диагностику Podkop

---

**2026-04-07T10:03:10 | Владимир Волков**
Система - пакеты - остановить youtubeunblock, zapret, zeroblock, podkop - попробовать снова

---

**2026-04-07T10:05:43 | Routerich**
в настройках Podkop измените dns на 9.9.9.9

---

**2026-04-07T11:24:54 | Vladimir**
Здравствуйте, не получается обновить podkop, не могу понять что я делаю не так. 
opkg update успешно отрабатывает, у подкопа когда вызываю обновление вообще ничего не происходит, как в пакетах, так и через терминал.

---

**2026-04-07T11:40:14 | Роман**
podkop.net
Скрипт оттуда берите.

---

**2026-04-07T13:07:47 | Routerich**
так же либо стопайте youtubeunblock либо убирайте youtube из Podkop

---

**2026-04-07T13:07:47 | Teleghost**
А где эталонный скрипт для него? 
Я попробую, когда снова поеду к родным. С podkop+zapret и стандартными настройками скрипта 5 в Минске не открывается много сайтов, которые работают в Москве. Приходится отключать.

---

**2026-04-07T13:14:34 | Routerich**
в Podkop->настройки->попробовать для начала сменить тип DNS на DOT

---

**2026-04-07T13:21:12 | Routerich**
да, если на телефоне включен ExitNode и интерфейс добавлен в Podkop/zeroblock (на случай если этот адрес у вас прописан в этих службах)

---

**2026-04-07T13:22:08 | Routerich**
Службы->Podkop->Настройки->Тип протокола DNS->DOT->сохранить и применить
после проверяйте работу

---

**2026-04-07T13:23:18 | Routerich**
так же остановите и отключите zapret, либо уберите youtube из Podkop

---

**2026-04-07T13:25:54 | Routerich**
ну вы запустите youtubeunblock , если не заработает то остановите и выключите автозапуск его
а в Podkop-Юв секцию Discord добавьте список Youtube

---

**2026-04-07T13:32:48 | 😏**
Вернул youtubeUnblock-На пк ютуб вернулся к жизни, на мобильном через Tailscale-нет. Выключил, в том числе автозапуск. Добавил в Podkop список. На ПК заработал, на мобильном-так же лежит

---

**2026-04-07T13:34:16 | Routerich**
вы либо пользуетесь youtubeunblock, либо Podkop
не должно быть и там и там ютуба

---

**2026-04-07T13:35:56 | Routerich**
а в Podkop добавлен интерфейс tailscale?

---

**2026-04-07T13:51:35 | Routerich**
можно.
https://podkop.net/docs/tunnels/awg_settings/

---

**2026-04-07T14:49:44 | Rustam Ikramov**
Здравствуйте. Возможно была инструкция уже , подскажите что делать? Сам по себе ВПН работает, стоит ссылку VLESS перенести в podkop - VPN уже не заводится

---

**2026-04-07T14:50:30 | Routerich**
Здравствуйте.
в настройках Podkop смените тип протокола DNS на DOT и проверяйте

---

**2026-04-07T17:05:17 | Никита**
подскажите куда копать, идея использовать роутер как сервер к которому подключиться с мобильного, по хорошему протоколом со сплит тунеллем и так далее, то есть vless например, на роутере уже есть singbox через podkop, но я так понимаю там нет inbound сервера, нельзя же второй сингбокс рядом поставить?

---

**2026-04-07T17:30:38 | Rus Rodriguez**
Бета версия скрипта для обхода ограничений.

Основное отличие от скрипта №5, что тут  используется последняя версия Podkop (v0.7.14).

Из ключевых отличий этой версии то, что там баг с WARP и CloudFlare починили, добавили исключения и список Roblox можно сразу выбрать.

Важно: 
1. Перед запуском сделайте бэкап (Система->Восстановление и обновление->Создать архив)
2. Если у вас всё работает хорошо, в частности youtube не надо его запускать.
3. Если не готовы сбрасывать роутер после неудачной отработки скрипта, лучше не запускайте скрипт.

Если вы всё таки решились запустить его, то от вас мне нужны полные логи запуска скрипта от начала его работы до завершения. Файл с логами будет по пути /root/run.log, можете его скачать через 
Веб морда роутера->NAS->Файловый менеджер->/root/run.log, скачать 
Потом пришлите его, для анализа.

P.S. запустится только на прошивках версии не ниже 24.10.2

Сам код для запуска ниже.
sh <(wget -q -O - https://raw.githubusercontent.com/routerich/RouterichAX3000_configs/refs/heads/podkop0711/universal_config_new_podkop.sh) 2>&1 | tee /root/run.log

---

**2026-04-07T17:34:05 | Viktor Polesov**
Уважаемое сообщество, прошу прощения, но не реально пересматривать тонны сообщений,  ткните плз.  в ссылку с чего начинать в текущих условиях. Есть RouteRich AX3000 c 24.10.4 c Podkop`ом через vless, который перестал работать. Говорят, что влесс уже не актуален и нужно переходить на  Zeroblock+Zapret2. Что в этом случае надо сделать X-Ray на VPS? Задача минимум вернуть ЮТ на ТВ, возможно-ли это сделать малой кровью, попроще? Или ставить 25-ю прошивку и начинать всё  нуля? Спасибо заранее!)))

---

**2026-04-07T17:44:58 | Viktor Polesov**
Анализ запущен: 2026-04-07 17:40:40
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  57.144.68.1 | YouTube IP:  142.251.209.14

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.68 MB / ↑0.19 MB
  Пинг (ya.ru via awg10): 48.738 / 54.392 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop zapret opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200 OK) [tlsv1.3] [try: 1]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Пересечение между podkop и zapret:
    podkop                    : main
    zapret                    : zapret-hosts-google.txt
    Домены: googlevideo.com youtube.com

  podkop            Discord (vpn): discord,!!!_meta
  podkop           main (prx url): geoblock,block,!!!_meta,twitter,hdrezka,tiktok,google_ai,youtube,google_play,telegram
  podkop DNS/Bootstrap DNS: (doh) 8.8.8.8 / 8.8.8.8
  podkop ⚠️ Router DNS is NOT routed through sing-box
  podkop ❌ Sing-box does NOT work with FakeIP: ;; communications error to 127.0.0.42#53: connection refused
  Версия podkop: v0.7.10
  Ошибка: DNS и DHCP, Строгий порядок активен!

---

**2026-04-07T17:57:57 | Viktor Polesov**
Гмм... Он должен быть выключен, странно. Выключил. В DNS/bootstrap стоял Гугл 8888, поставил Quad9999. Подкоп ругается на списки мета, дискорд, телеграм, твиттер, наверное их можно удалить. Podkop ругается DNS проверки
Обнаружены проблемы
Bootstrap DNS
9.9.9.9
Основной DNS
9.9.9.9 [doh]
DNS на роутере
DHCP содержит DNS сервер
Sing-box проверки
Обнаружены проблемы
Sing-box установлен
Версия Sing-box совместима (новее 1.12.4)
Сервис sing-box существует
Автостарт sing-box отключен
Процесс sing-box запущен
Sing-box слушает порты
Nftables проверки
Обнаружены проблемы
Таблица существует
Правила mangle существуют
Счётчики правил mangle
Правила mangle output существуют
Счётчики правил mangle output
Правила прокси существуют
Счётчики правил proxy
Найдены дополнительные правила маркировки
Outbounds проверки
Не удалось получить результаты проверки Sing-Box не запускается...(((

---

**2026-04-07T18:47:23 | Routerich**
Здравствуйте.
А что-то используете типо Podkop, zeroblock?

---

**2026-04-07T18:47:52 | Viktor Polesov**
📡 Global check run!
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛠 System info
🕳 Podkop:        v0.7.14 (latest: 0.7.14)
🕳 LuCI App:      v0.7.14
📦 Sing-box:      1.12.12
🛜 OpenWrt:       RouteRich 24.10.4 r28959-29397011cc RR-3.8.2
🛜 Device:        Routerich AX3000
━━━━━━━━━━━━━━━━━━━━━━━━━━━
➡️ DNS status
✅ Bootstrap DNS: 9.9.9.9
✅ Main DNS: 9.9.9.9 [doh]
✅ DNS on router
⚠️ dont_touch_dhcp is enabled. 📄 DHCP config:
config dnsmasq
  option domainneeded '1'
  option boguspriv '1'
  option localise_queries '1'
  option rebind_protection '1'
  option rebind_localhost '1'
  option local '/lan/'
  option domain 'lan'
  option expandhosts '1'
  option nonegcache '1'
  option cachesize '0'
  option authoritative '1'
  option readethers '1'
  option leasefile '/tmp/dhcp.leases'
  option resolvfile '/tmp/resolv.conf.d/resolv.conf.auto'
  option nonwildcard '1'
  option localservice '1'
  option ednspacket_max '1232'
  option confdir '/tmp/dnsmasq.d'
  option noresolv '1'
  option filter_aaaa '1'
  option strictorder '1'
  list server '127.0.0.1#5359'

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 Sing-box status
✅ Sing-box installed
✅ Sing-box version is compatible (newer than 1.12.4)
✅ Sing-box service exist
✅ Sing-box autostart disabled
❌ Sing-box process running
❌ Sing-box listening ports
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧱 NFT rules status
✅ Table exist
✅ Rules mangle exist
⚠️  Rules mangle counters
✅ Rules mangle output exist
⚠️  Rules mangle output counters
✅ Rules proxy exist
⚠️  Rules proxy counters
✅ Additional marking rules found
━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 Podkop config

config settings 'settings'
  option dns_type 'doh'
  option dns_server '9.9.9.9'
  option bootstrap_dns_server '9.9.9.9'
  option dns_rewrite_ttl '60'
  option enable_output_network_interface '0'
  option enable_badwan_interface_monitoring '0'
  option enable_yacd '0'
  option disable_quic '1'
  option update_interval '1d'
  option download_lists_via_proxy '1'
  option dont_touch_dhcp '1'
  option config_path '/etc/sing-box/config.json'
  option cache_path '/tmp/sing-box/cache.db'
  option exclude_ntp '1'
  option shutdown_correctly '0'
  option download_lists_via_proxy_section 'main'
  list source_network_interfaces 'br-lan'
  option log_level 'warn'

config section 'main'
  option connection_type 'proxy'
  option proxy_config_type 'url'
  option enable_udp_over_tcp '0'
  option shutdown_correctly '1'
  option user_domain_list_type 'text'
  option user_subnet_list_type 'disabled'
  option mixed_proxy_enabled '0'
  option user_domains_text 'myip.com, dell.com, st.com, gvt1.com, 4pda.to,  WhatsApp.com, 3dtoday.ru'
  option proxy_string 'MASKED'
'
  list community_lists 'geoblock'
  list community_lists 'block'
  list community_lists 'meta'
  list community_lists 'twitter'
  list community_lists 'hdrezka'
  list community_lists 'tiktok'
  list community_lists 'google_ai'
  list community_lists 'youtube'
  list community_lists 'google_play'
  list community_lists 'telegram'

config section 'Discord'
  option connection_type 'vpn'
  option interface 'awg10'
  option domain_resolver_enabled '0'
  option user_domain_list_type 'text'
  option user_subnet_list_type 'disabled'
  option mixed_proxy_enabled '0'
  option user_domains_text '2ip.ru amazonaws.com whatsapp.com whatsapp.net whatsapp.biz wa.me'
  list remote_subnet_lists 'https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_cidr_ipv4.txt'
  list community_lists 'discord'
  list community_lists 'meta'

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 WAN config
config interface 'wan'
  option device 'wan'
  option proto 'dhcp'

⚠️ WARP detected: engage.cloudflareclient.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ Zapret detected
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🥸 FakeIP status
⚠️ Router DNS is NOT routed through sing-box
❌ Sing-box does NOT work with FakeIP: ;; communications error to 127.0.0.42#53: connection refused
;; communications error to 127.0.0.42#53: connection refused
;; communications error to 127.0.0.42#53: connection refused
;; no servers could be reached

---

**2026-04-07T20:53:17 | Sir**
Спасибо большое.
Но всё таки, я что то делаю не так.
Как прописать эти сайты, что бы они не шли через Z2/Podkop ???
Игра работает, но грузится ужасно медленно
Что бы загрузились разные доп.режимы, надо ждать порядка 5 минут

---

**2026-04-07T21:05:13 | Artem**
В podkop DoH на DoT поменяй

---

**2026-04-07T22:33:33 | Keros1n**
что лучше ставить? zeroblock или podkop?

---

**2026-04-07T22:45:47 | @Seeyou**
Отвалился ютуб с пк. и андройд тв что нужно предпринять !? 

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.13 | YouTube IP:  198.18.0.100

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.18 MB
  Пинг (ya.ru via awg10): 8.972 / 33.191 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200 OK) [tlsv1.3] [try: 1]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop    Youtube_Discord (vpn): !!!_youtube,!!!_discord,!!!_telegram
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai,!!!_youtube,!!!_telegram,anime,!!!_discord
  podkop DNS/Bootstrap DNS: (doh) 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10
  Ошибка: DNS и DHCP, Строгий порядок активен!
  Ошибка: DNS и DHCP, Игнорировать файл resolv отключено! 

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 1.15 | RAM: 33% | NAND: 27% занято / 48.6M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-04-08T05:25:03 | Zamir**
Подскажите плз - вот результат проверки скриптом:
Диагностика Tailscale запущена: 2026-04-08 05:20:26
Лог сохраняется в: /root/tailscale_diagnostic.log
--------------------------------------------------------------

= ИНФОРМАЦИЯ О TAILSCALE:
  Версия: 1.90.6          | Статус: RUNNING | Автозапуск: РАЗРЕШЁН

= АНАЛИЗ КОНФИГУРАЦИИ /etc/config/tailscale:

1. ОБЯЗАТЕЛЬНЫЕ ПАРАМЕТРЫ:
  [OK]   enabled                        | 1 [галочка "Включить"]
  [OK]   accept_dns                     | 1 [галочка "Принимать DNS"]
  [OK]   accept_routes                  | 1 [галочка "Принимать маршруты"]

2. ОПЦИОНАЛЬНЫЕ ПАРАМЕТРЫ:
  [ИНФО] fw_mode                        | nftables [настройка "Режим межсетевого экрана"]
  [ИНФО] log_stdout                     | выключен [галочка "Журнал вывода"]
  [ИНФО] log_stderr                     | выключен [галочка "Журнал ошибок"]
  [ИНФО] disable_snat_subnet_routes     | SNAT включен [CLI флаг]

3. ПРОВЕРКА EXIT NODE:
  [OK]   advertise_exit_node            | включен [галочка "Узел выхода"]
  [OK]   advertise_routes               | 192.168.1.0/24 = 192.168.1.0/24 (br-lan) [настройка "Открыть подсети"]
  [OK]   podkop (not running)           | интерфейсы br-lan,tailscale0 [настройка "Интерфейс источника"]

= СТАТУС ПОДКЛЮЧЕНИЯ:
  [OK]   Tailscale: подключен
  IPv4: 100.107.8.148
  IPv6: fd7a:115c:a1e0:ab12:4843:cd96:626b:894

= ДОПОЛНИТЕЛЬНЫЕ ПРОВЕРКИ:
  [OK]   Интерфейс tailscale0: существует

--------------------------------------------------------------
Диагностика завершена: 2026-04-08 05:20:32
root@RouteRich:~# ^C



а на клиентах все равно ошибка 
tailscale could not connect to th 'Russia VPS2' relay server

Из манипуляций делал только временно отключал слжбу zapret для теста и всё

---

**2026-04-08T07:57:09 | Tim Mars**
а чем zeroblock от podkop отличается?

---

**2026-04-08T08:22:02 | Routerich**
Службы->Podkop->cекции->

---

**2026-04-08T08:36:52 | Tim Mars**
не совсем вас понял, из подобного нашел что yacd можно включить в настройках podkop, но оно там выключено

или вы имеете ввиду что логи надо смотреть?

---

**2026-04-08T08:48:22 | Nickname**
podkop, это сторонний продукт, а ZB это родной фирменный продукт от RR

---

**2026-04-08T09:14:15 | Tim Mars**
я же правильно понимаю, если я выключаю podkop то он полностью выключается? там не остается никакой dns и прочее?

---

**2026-04-08T09:35:09 | Routerich**
Службы->Podkop->Настройки->убрать/поставить галочку на скачивать списки через Proxy

---

**2026-04-08T10:03:34 | Сергей Никифоров**
Всем привет!
Ставил Zeroblock по мануалу на чистую новую прошивку, не проходили проверки FakeIP, как в диагностике так и по скрипту.
Поставил podkop так же на чистую новую прошивку скриптом из beta, проверки FakeIP проходят, как в диагностике так и скриптом.
Подскажите, в чем может быть проблема?

---

**2026-04-08T10:11:21 | Routerich**
В настройках Podkop смените тип DNS с DOH на DOT и снова проверьте

---

**2026-04-08T10:48:45 | Александр Король 👑**
Добрый день! Являюсь владельцем устройства с марта. Во первых спасибо за прекрасный девайс. Во вторых есть ряд вопросов, причём достаточно нубских. Сразу после получения обновил все пакеты и поставил zapret, zapret2, podkop и zeroblock. В принципе из того что нужно: tg, wa, youtube, insta, детям сервера brawl stars, торрент-трекеры. И вроде все более менее работает, но каждый день приходится перезапускать службы (в частности podkop) чтобы стали доступны торренты. Может я что-то не так сделал? Куда глянуть?

---

**2026-04-08T11:51:08 | Routerich**
Службы->Podkop->Настройки->тип протокола DNS смените с DOH на DOT, потом сохранить и применить и проверяйте

---

**2026-04-08T13:19:55 | Routerich**
Здравствуйте.
по идеи этого достаточно.
а у вас свои обходы в Podkop или общедоступные которые?

---

**2026-04-08T13:50:07 | Routerich**
только потом созданный интерфейс надо добавлять в Podkop/zeroblock рядом с br-lan, чтобы обходы работали

---

**2026-04-08T17:57:46 | Alex**
Привет. Решил заместить Podkop Зироблоком. По началу было всё ок. Сейчас, несмотря на то, что по дашбордам/диагностики ок, сайты не открываются

---

**2026-04-08T18:04:46 | Gomer Simpson**
Гитхаб. Темы podkop и zapret.

---

**2026-04-08T18:31:27 | Роман**
https://github.com/StressOzz/Zapret-Manager
Это попробуйте, только отключите з2, уберите ютуб и юискорд из ZB/podkop.

---

**2026-04-08T19:24:22 | Bumbon4ik**
а можно на роутере настроить openVPN сервер, что бы он работал через подкоп, и когда я подключаюсь с удалённого устройства по openVPN к роутеру, то внешка работала через Podkop роутера?

---

**2026-04-08T19:33:25 | Routerich**
Надо в настройках Podkop добавить интерфейс openvpn в список интерфейсов рядом с br-lan

---

**2026-04-08T19:35:42 | Anna Bagler**
Ну, замените пару DNS/bootstrap. Перезапустите podkop. Проверку ещё раз.

---

**2026-04-08T19:41:36 | Routerich**
Я про Podkop спрашивал

---

**2026-04-08T19:48:44 | Stasnislav**
Добрый вечер кто подскажет. Podkop  не делает  диагностику. Крутит ,крутит и все. Перезагрузку подкопа делал.Роутер то  же перегрузил.Что делать?

---

**2026-04-08T19:49:35 | Routerich**
Здравствуйте.
Можно, но лучше не ставить.
Zeroblock есть, он будет лучше. Ещё есть Podkop

---

**2026-04-08T19:50:10 | Routerich**
Здравствуйте.
В настройках Podkop изменить dns на Google или 9.9.9.9

---

**2026-04-08T19:51:52 | Routerich**
Ну значит разбирайтесь с этим, Должна быть доступна локалка, чтобы и Podkop работал так

---

**2026-04-08T19:56:38 | Routerich**
Здравствуйте.
Надо добавить интерфейс TailScale в Podkop, в настройках , рядом с br-lan

---

**2026-04-08T20:40:54 | Vadim**
Добрый вечер. Помогите пожалуйста разобраться.  Установил прошивку 24.10.5. Установил podkop. Выдает такую ошибку. Также не мог пройти проверку днс , изменил днс сейчас такой результат проверки

---

**2026-04-08T20:56:56 | Имя Фамилия**
Добрый вечер! 
Подскажите, пожалуйста, у меня установлен podkop, в списках сообщества выбран пункт «Anime”, чтобы иметь доступ к сайту jut.su
Проблема такая, сам сайт открывается, но вот видео не воспроизводится, даже в качестве 360P

---

**2026-04-08T22:05:13 | Routerich**
Сеть->Интерфейсы->awg10->перезапустить
И Podkop перезапустите после и снова диагностику

---

**2026-04-08T23:01:14 | Александр**
Podkop из коробки

---

**2026-04-08T23:46:14 | Фил**
Добрый вечер, только начинаю знакомиться с openwrt и роутерич, скажите пожалуйста на ютубе все используют podkop, а тут zeroblock и на зероблок вообще нет роликов, что лучше или актуальнее использовать? или где можно почитать сравнение?
Спасибо!

---

**2026-04-09T00:17:53 | Роман**
https://github.com/ushan0v/podkop-plus
Подкопий плюс 😁

---

**2026-04-09T08:24:10 | Имя Фамилия**
Установленный клиент Podkop настроен на использование списка сообщества «Anime» для доступа к ресурсу jut.su 
Несмотря на успешное открытие веб-страницы, воспроизведение видеоконтента не осуществляется даже в разрешении 360p. В чем может заключаться причина данной проблемы?

---

**2026-04-09T08:39:29 | Routerich**
в отсутствии доменов нужных
отследите их через например ipvfoo и потом добавьте в Podkop

---

**2026-04-09T10:25:22 | Routerich**
Отследить все домены и добавить их в Podkop/zeroblock

---

**2026-04-09T10:28:32 | Routerich**
https://podkop.net/docs/sections/#tip-polzovatelskogo-spiska-domenov-user-domain-list-type
а сами домены выше.

---

**2026-04-09T11:39:17 | Routerich**
https://podkop.net/docs/install/

---

**2026-04-09T12:14:42 | Серёга_44rus**
Здрасьте) Zeroblock с podkop несовместим?

---

**2026-04-09T12:36:30 | Zamir**
Системная информация
Podkop
v0.7.14Последняя
Luci App
v0.7.14
Sing-box
1.12.12
OS
RouteRich 24.10.4 r28959-29397011cc ASU
Device
Routerich AX3000 v1

---

**2026-04-09T12:55:53 | Routerich**
тогда уж удалить Podkop, sing-box, установить zero block, а потом уже ASU

---

**2026-04-09T13:42:58 | Zamir**
Zamir, [09.04.2026 15:28]
Спасибо!
Пока читаю инфу про не трогать мой DHCP, а проверка вот что дала:
----------------------------------------------------- 
RouteRich 24.10.4, r28959-29397011cc 
-----------------------------------------------------r
oot@RouteRich:~# uci show dhcp.@dnsmasq[0]d
hcp.cfg01411c=dnsmasqd
hcp.cfg01411c.domainneeded='1'd
hcp.cfg01411c.localise_queries='1'd
hcp.cfg01411c.rebind_protection='1'd
hcp.cfg01411c.rebind_localhost='1'd
hcp.cfg01411c.local='/lan/'d
hcp.cfg01411c.domain='lan'd
hcp.cfg01411c.expandhosts='1'd
hcp.cfg01411c.nonegcache='1'd
hcp.cfg01411c.cachesize='0'd
hcp.cfg01411c.authoritative='1'd
hcp.cfg01411c.readethers='1'd
hcp.cfg01411c.leasefile='/tmp/dhcp.leases'd
hcp.cfg01411c.localservice='1'd
hcp.cfg01411c.ednspacket_max='1232'd
hcp.cfg01411c.confdir='/tmp/dnsmasq.d'd
hcp.cfg01411c.noresolv='1'd
hcp.cfg01411c.strictorder='1'd
hcp.cfg01411c.filter_aaaa='1'd
hcp.cfg01411c.server='127.0.0.1#5359'd
hcp.cfg01411c.address='/******** (тут я скрыл).ionscale.net/100.100.100.100'r
oot@RouteRich:~# ^Cr

oot@RouteRich:~#

Podkop AI Assistant, [09.04.2026 15:19]
Судя по логам диагностики, проблема вызвана остаточными правилами от zapret и наличием сторонних DNS-серверов в dnsmasq.

Полностью удалите zapret, так как его правила маркировки конфликтуют с Podkop даже в остановленном состоянии, и проверьте настройки dnsmasq при включенной опции «Не трогать мой DHCP».

Ссылки:
https://podkop.net/docs/troubleshooting/#proverka-pravil-markirovki-i-proksirovaniya-trafika
https://podkop.net/docs/troubleshooting/#proverka-nastroek-dns-na-routere
https://podkop.net/docs/diagnostics/#nftables-proverki

---

**2026-04-09T14:44:38 | Anna Bagler**
Тут поддерживается zeroblock и пока podkop.

---

**2026-04-09T14:46:02 | Routerich**
в Podkop, в настройках, рядом с br-lan добавьте интерфейс openvpn, если он у вас на Роутериче.

---

**2026-04-09T16:31:28 | Антон Чепкасов**
Всем привет, ни у кого интернет по wifi не отваливался? На 2 роутерах РР перестал работать. Один обновил на актуальную прошивку и накатил ZeroBlock + Zapret2, всё работает. Второй ещё не трогал. Раньше настроено было через yotubeunblock и podkop, Интересно вот, проблема в прошивке старой или  yotubeunblock и podkop ?

---

**2026-04-09T16:33:18 | Dr. Strange**
podkop через раздел пакетов можно ставить или лучше по SSH?

---

**2026-04-09T16:52:47 | Валентин**
Читаю тему и никак не могу понять, сейчас актуально использовать zeroblock+zapret2 или podkop+zapret1? Что дальше будет в поддержке и что правильнее настроить?

---

**2026-04-09T16:56:12 | Валентин**
Т.е. сношу podkop и singbox и ставлю zeroblock+zapret2, получается так? И как я понимаю развиваться дальше будет все таки zapret2, не первый?

---

**2026-04-09T17:16:32 | Роман**
Да, устанавливать и настраивать самому.
И можно ли сделать сплит-туннелинг (как понимаю это так называется), чтобы ВПН на роутере включался только при заходе на запрещенные сайты, а отечественные не трогал?
zeroblock/podkop работают по такому принципу.

---

**2026-04-09T17:23:31 | Soawa Feeliny 𓆏ࣩࣩ**
Скажите, а есть возможность поставить не  AMNEZIA WG, а другой VPN для выбора в списках Сетевого интерфейса Podkop?

---

**2026-04-09T17:37:13 | Фирст Нейм**
Работало, когда podkop был с секциями с Main и VPN.

---

**2026-04-09T18:19:05 | Routerich**
Смените в настройках Podkop сервер dns на Google

---

**2026-04-09T18:51:01 | Anna Bagler**
Zeroblock/podkop, отдельная секция с привязкой к интерфейсу и спискам.

---

**2026-04-09T18:55:55 | Роман**
Вы zeroblock/podkop установили? Они рулят списками и трафиком через ваш интерфейс.

---

**2026-04-09T18:56:25 | Владимир Волков**
Раздел Допвозможностей, Exit Node + Podkop или Zeroblock

---

**2026-04-09T18:57:05 | Routerich**
Здравствуйте.
Настройки Podkop сервер dns смените на Google

---

**2026-04-09T19:45:07 | MS**
Здравствуйте! Настроил роутер по видео из интернета, установил podkop добавил ключ (vless) рабочий, имеется свой VPS рабочий, клиенты подключаются всё стабильно работает. Но само устройство при выборе политик которые должны идти в обход блокировок почему-то не запускаются. Самое интересное что ютуб работает, но остальные сайты и приложения ни в какую.
В чем может быть проблема не подскажите?

---

**2026-04-09T20:05:57 | Routerich**
Здравствуйте.
Остановите вае обходы, Podkop /zeroblock, youtubeunblock, zapret, и проверяйте будет работать так или нет

---

**2026-04-09T20:41:51 | HiLLL**
а если так? в терминале service podkop start

---

**2026-04-09T20:44:05 | Kiss_My_Axe**
Не, так не сработает.
Так сработает:
opkg update && opkg install zeroblock luci-app-zeroblock && /etc/init.d/podkop stop && /etc/init.d/podkop disable
Впрочем и так не сработает, сингбокс-конфликт вылезет.

---

**2026-04-09T21:04:31 | Vsevolod Chirkov**
Добрый вечер!
Столкнулся с проблемой в работе podkop, некоторое время назад отвалился discord (при этом работает находящийся в той же секции telegram). Диагностика на уровне службы зависает на стадии "DNS проверки", также таймаут получаю при попытке проверки fakeip. Версию подкопа обновил до актуальной (0.7.14). Перезапускал как саму службу, так и роутер, однако это не помогло. Сейчас прогнал скрипт анализа в терминале, прикладываю скриншот к сообщению. Вы не могли бы помочь разобраться в том, что именно вызывает проблему с DNS?

---

**2026-04-09T21:39:07 | Sadr**
Podkop

---

**2026-04-09T21:45:04 | Vladimir**
Анализ запущен: 2026-04-09 21:43:51
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.30 | YouTube IP:  198.18.1.19

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.33 MB
  Пинг (ya.ru via awg10): 16.784 / 22.898 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop opera-proxy youtubeUnblock

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200 OK) [tlsv1.3] [try: 1]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Внутреннее пересечение в youtubeUnblock:
    youtubeUnblock            : Youtube (Условия: default)
    youtubeUnblock            : Youtube (Условия: default)
    Домены: googlevideo.com youtube.com 

  !!!_КРИТ: Пересечение между podkop и youtubeUnblock:
    podkop                    : Youtube_Discord
    youtubeUnblock            : Youtube
    Домены: googlevideo.com whatsapp.biz whatsapp.com whatsapp.net youtube.com 

  podkop    Youtube_Discord (vpn): youtube,discord
  podkop           main (prx out): geoblock,tiktok,block,meta,twitter,hdrezka,google_ai,porn,telegram
  podkop DNS/Bootstrap DNS: (doh) 8.8.8.8 / 8.8.8.8
  podkop ❌ Bootstrap DNS: 8.8.8.8
  Версия podkop: v0.7.10
uci: Entry not found
  Предупреждение: DNS и DHCP, Строгий порядок активен!

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.25 | RAM: 37% | NAND: 26% занято / 49.2M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

root@RouteRich:~#

---

**2026-04-09T21:46:45 | Gomer Simpson**
Что Podkop?

---

**2026-04-09T21:48:35 | Петр Горбунов**
Подскажите, в чем может быть проблема, раньше был podkop + предыдущая прошивка. Обновился до последней версии, поставил ZeroBlock, настроил работу через vless. Но сейчас если на телефоне подключен wifi и поднят на телефоне vless то ничего не грузится, кроме морды модема. Раньше они не конфликтовали, работало с включенным впн на телефоне.

---

**2026-04-09T22:04:00 | Routerich**
Значит провайдер жестко блочит, пробуйте сами в интернете найти warp generator и сделать конфиг и далее https://podkop.net/docs/tunnels/awg_settings/ пункт установка пакетов пропустить

---

**2026-04-09T22:13:03 | Sharky**
Он сейчас после неудачи отключает секцию YOTUBE
Только  main в podkop

---

**2026-04-10T00:02:14 | Алексей**
Купил устройство, настроил интернет без границ - запусти скрипт. Добавил в подкоп, что было мне необходимо. И вроде все работает. Потом начал читать про zeroblock и zapret2. Вопрос - надо ли перейти с zapret+podkop? На что лучше перейти - zeroblock или zapret2? Как перейти если zeroblock валится в ошибку:
Thu Apr 9 23:45:54 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Thu Apr 9 23:45:59 2026 user.notice zeroblock: No sections configured, restoring DNS and skipping start

---

**2026-04-10T01:14:17 | HiLLL**
https://podkop.net/docs/sections/

---

**2026-04-10T06:44:07 | Routerich**
Здравствуйте.
просто не хватает доменов, нужно отследить все домены на которые этот сайт обращается и добавлять их в Podkop.

---

**2026-04-10T08:51:22 | Санчо Панчо**
Информация для "счастливых" обладателей умной техники Xiaomi. Как вы уже могли заметить, устройства умного дома перестали подключаться к сети из-за действий "конторы весельчаков".

После долгих поисков решения я наткнулся на информацию с 4pda. Необходимо добавить данные подсети в любую секцию zeroblock/podkop (warp/opera/vless). Zapret мне не помог в данном случае.

107.155.51.0/24
107.155.52.0/24
107.155.53.0/24

После проброса этих сетей в zeroblock (warp) у меня всё заработало. Xiaomi вроде обещали это починить конечно, но ждать можно долго)
з.ы: текст не мой, копия сообщения из чата

---

**2026-04-10T09:14:11 | Egor Mikhaylov**
Привет!
Проблема на IOS аналогичная, приложение chatgpt по региону не работает
Есть такое наблюдение:
Это не связано с конкретными доменами, потому-что у меня все домены в файлах и эти же файлы при работе в podkop не вызывали проблем при работе chatgpt, я пока не могу понять, какая опция в zeroBlock может препятствовать работе, потому-что, повторюсь в podkop при тех-же доменах и настройках - chatgpt работал корректно на ios, соответственно никаких изменений на телефона тоже не производилось и Wifi сеть та-же.

---

**2026-04-10T09:37:15 | Routerich**
у вас Podkop или zeroblock?

---

**2026-04-10T10:01:41 | Routerich**
Podkop или ZeroBlock используете?

---

**2026-04-10T10:48:30 | Labrador94**
Перезапустил,выдает ошибку
Fri Apr 10 10:37:26 2026 user.notice podkop: [error] Download meta list failed

---

**2026-04-10T10:53:29 | Алексей Сергеевич**
подскажите глюкнул подкоп 

 global_check 
 📡 Global check run!
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🛠️ System info
🕳️ Podkop:        v0.7.10 (latest: 0.7.14)
🕳️ LuCI App:      v0.7.10
📦 Sing-box:      1.12.22
🛜 OpenWrt:       RouteRich 24.10.5 r29087-d9c5716d1d RR-3.9.0
🛜 Device:        Routerich AX3000 v1
━━━━━━━━━━━━━━━━━━━━━━━━━━━
➡️ DNS status
✅ Bootstrap DNS: 8.8.8.8
✅ Main DNS: 8.8.8.8 [dot]
✅ DNS on router
⚠️ dont_touch_dhcp is enabled. 📄 DHCP config:
config dnsmasq
 option domainneeded '1'
 option localise_queries '1'
 option rebind_protection '0'
 option local '/lan/'
 option domain 'lan'
 option expandhosts '1'
 option nonegcache '1'
 option authoritative '1'
 option readethers '1'
 option leasefile '/tmp/dhcp.leases'
 option localservice '1'
 option ednspacket_max '1232'
 option confdir '/tmp/dnsmasq.d'
 option filter_aaaa '1'
 option strictorder '1'
 option port '53'
 option logqueries '1'
 option cachesize '0'
 option noresolv '1'
 option podkop_noresolv '0'
 option podkop_cachesize '150'
 list server '127.0.0.1#5359'

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📦 Sing-box status
✅ Sing-box installed
✅ Sing-box version is compatible (newer than 1.12.4)
✅ Sing-box service exist
✅ Sing-box autostart disabled
✅ Sing-box process running
✅ Sing-box listening ports
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧱 NFT rules status
✅ Table exist
✅ Rules mangle exist
✅ Rules mangle counters
✅ Rules mangle output exist
✅ Rules mangle output counters
✅ Rules proxy exist
✅ Rules proxy counters
⚠️  Additional marking rules found:
  meta mark & 0x00008000 == 0x00008000 counter packets 0 bytes 0 accept
  iifname "tailscale0*" counter packets 7 bytes 788 meta mark set meta mark & 0xffff04ff | 0x00000400
  meta mark & 0x0000ff00 == 0x00000400 counter packets 7 bytes 788 accept
  meta mark & 0x0000ff00 == 0x00000400 counter packets 0 bytes 0 masquerade
━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 Podkop config

config settings 'settings'
 option dns_type 'dot'
 option dns_server '8.8.8.8'
 option bootstrap_dns_server '8.8.8.8'
 option dns_rewrite_ttl '60'
 option enable_output_network_interface '0'
 option enable_badwan_interface_monitoring '0'
 option enable_yacd '0'
 option disable_quic '1'
 option update_interval '1d'
 option download_lists_via_proxy '0'
 option dont_touch_dhcp '1'
 option config_path '/etc/sing-box/config.json'
 option cache_path '/tmp/sing-box/cache.db'
 option exclude_ntp '1'
 option shutdown_correctly '0'
 option download_lists_via_proxy_section 'main'
 list source_network_interfaces 'br-lan'

config section 'main'
 option connection_type 'proxy'
 option proxy_config_type 'outbound'
 option enable_udp_over_tcp '0'
 option shutdown_correctly '1'
 option user_domain_list_type 'text'
 option user_subnet_list_type 'disabled'
 option mixed_proxy_enabled '0'
 option outbound_json 'MASKED'
 option user_domains_text 'myip.com amazonaws.com whatsapp.com whatsapp.net whatsapp.biz wa.me'
 list community_lists 'geoblock'
 list community_lists 'block'
 list community_lists 'meta'
 list community_lists 'hdrezka'
 list community_lists 'tiktok'
 list community_lists 'google_ai'
 list community_lists 'youtube'
 list community_lists 'telegram'

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📄 WAN config
config interface 'wan'
 option proto 'pppoe'
 option device 'eth1'
        option username '******'
        option password '******'
 option pppd_options 'debug'
 option ipv6 '0'
 option dns '8.8.8.8 8.8.4.4'

⚠️ WARP detected: engage.cloudflareclient.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ Zapret detected
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🥸 FakeIP status
⚠️ Router DNS is NOT routed through sing-box
✅ Sing-box works with FakeIP: 198.18.0.3

---

**2026-04-10T10:54:55 | Alex Bar**
А где выше? 
У меня тоже podkop не работает

---

**2026-04-10T11:04:48 | Сергей Мокринский**
Подскажите, пожалуйста, как переустановить Podkop?

---

**2026-04-10T11:05:36 | Amras Amandil**
А у всех podkop ругается, что какие-то списки подгрузить не может?

---

**2026-04-10T11:08:26 | 𝓐𝓵𝓮𝓴𝓼𝓪𝓷𝓭𝓻**
WARP бесконечно перебирает ip адреса серверов и не может подключиться к Cloudflare для обхода блокировок и шифрования трафика в Podkop.

---

**2026-04-10T11:53:48 | Routerich**
потому что у вас Podkop

---

**2026-04-10T12:00:03 | Александр Миронов**
Здравствуйте всем! Сегодня перестал работать телеграмм с роутера, вчера работал, установлен 5 скрипт, podkop. Прошивка роутера 24.10 . Что попробовать?

---

**2026-04-10T12:05:04 | Routerich**
попробуйте изменить DNS в настройках Podkop на 9.9.9.9

---

**2026-04-10T12:09:39 | Routerich**
Здравствуйте.
перезапустите Podkop

---

**2026-04-10T12:14:00 | Routerich**
в настройках Podkop измените сервер DNS на 9.9.9.9

---

**2026-04-10T12:16:05 | Михаил Корнилов**
При изменении настроек Podkop ошибки:


Podkop Error
Fri Apr 10 12:14:06 2026 user.notice podkop: [error] Download https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_cidr_ipv4.txt list failed

Download telegram list failed
Download discord list failed
Download cloudflare list failed
Download meta list failed


Причём 

https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_cidr_ipv4.txt

в браузере на компе открывается нормально...

---

**2026-04-10T12:16:35 | Routerich**
в настройках Podkop убрать/поставить галочку на скачивать списки через Proxy

---

**2026-04-10T12:27:10 | Александр**
В каком положении надо оставить эту галочку? Вкл или Выкл?
В разделе Podkop такие сообщения об ошибках (возможно, Telegram из-за этого не работает).
+ Скрины из диагностики

---

**2026-04-10T12:36:43 | Roman**
Пробуйте, у кого не работает секция main в podkop. У меня запустилось, но задержка скачет от 1000 до 4000, надеюсь временно. Делал так: в настройках подкопа снимаем галку с Скачивать списки через Proxy/VPN, сохраняем. Затем идем Система-Автозапуск ищем opera-proxy жмем стоп-запустить. Перезагружаем роутер вынимая витание из розетки. Включаем роутер. Если тест в подкопе проходит, ставим обратно галку в настройках подкопа Скачивать списки через Proxy/VPN.

---

**2026-04-10T12:40:03 | Ronso**
Здравствуйте, подскажите, пожалуйста, как победить высокий пинг у прокси сервера? Все медленно грузит(
Podkop

---

**2026-04-10T12:51:38 | Unlock 27**
Народ подскажите роутер Cudy 3000s openwrt podkop через прокси работает все кроме телеги . Хотя тг веб работает .

---

**2026-04-10T13:03:30 | Баир**
Podkop работает

---

**2026-04-10T13:05:38 | А. Ч.**
Друзья, у меня версия Podkop 0.7.10 сам подкоп пишет что она устарела, при этом скрипт №5 обещает поставить именно эту версию. Скажите в итоге надо ли мне обновить Подкоп и как это сделать, если не через скрипт №5?

---

**2026-04-10T14:18:13 | Konstantin Milovanov**
Пробовал по мануалу с podkop + amnesia с сайта подкопа вообще ничего не завелось)

---

**2026-04-10T14:20:46 | Routerich**
https://podkop.net/docs/tunnels/awg_settings/ пункт установку пакетов пропустить, и ещё раз внимательно пройтись

---

**2026-04-10T14:50:44 | Алексей**
1.Podkop-вкладка настройки-скачивать списки через Proxy - галочка стоит
2. Скачивать через выбранную секцию - Discord
3. DNS сервер - 9.9.9.9
4. Bootstrap - 9.9.9.11
5. Тип протокола - DoT
6. Применить
Мне помогло

---

**2026-04-10T14:59:24 | Алексей Сергеевич**
Тоже пропала Youtube_discord после обновления, сейчас вот такая картина, ТГ работает, инста тоже, но ютуб нет, как починить ютуб?
Анализ запущен: 2026-04-10 14:50:28
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  157.240.205.35 | YouTube IP:  64.233.163.91
  Программы в автозапуске: podkop opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН  !!!_ОПЕРА ЗАБЛОКИРОВАЛА РОССИЮ_!!!
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:     127.0.0.1:53
    Name:       youtube.com        Address: 64.233.163.136
    Name:       youtube.com        Address: 64.233.163.190
    Name:       youtube.com        Address: 64.233.163.91
    Name:       youtube.com        Address: 64.233.163.93
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai,discord,telegram,youtube
  podkop DNS/Bootstrap DNS: (doh) 8.8.8.8 / 8.8.8.8
  podkop ⚠️ Router DNS is NOT routed through sing-box
  Версия podkop: v0.7.10
  Предупреждение: DNS и DHCP, Строгий порядок активен!

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.18 | RAM: 25% | NAND: 63% занято / 25.0M доступно
  3 3 12 12 * /usr/bin/nginx-util 'check_ssl'
  13 3 * * * "/root/.acme.sh"/acme.sh --cron --home "/root/.acme.sh" > /dev/null
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

root@RouteRich:~#

---

**2026-04-10T15:07:34 | Nickname**
Прошил бета скрипт.Но что-то пошло не так.Как это исправить                                                                                                                                                             ? = ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  v0.00 MB / ^0.00 MB
  Пинг (ya.ru via awg10): ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (5.255.255.242): 56 data bytes
  Программы в автозапуске: podkop opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН  !!!_ОПЕРА ЗАБЛОКИРОВАЛА РОССИЮ_!!! 
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:     127.0.0.1:53
    Name:       youtube.com        Address: 198.18.0.61
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai,youtube,discord,telegram,google_play
  podkop DNS/Bootstrap DNS: (doh) 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.14
  Предупреждение: DNS и DHCP, Строгий порядок активен!

---

**2026-04-10T15:25:49 | Nickname**
А вот это на другом роутере,прошитом еще ранее,но подсоединенным к той  же сети                                                                   Анализ запущен: 2026-04-10 15:22:31
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.18 | YouTube IP:  198.18.0.19

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.68 MB / ↑0.36 MB
  Пинг (ya.ru via awg10): 29.781 / 38.538 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200 OK) [tlsv1.3] [try: 1]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  zapret2         | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop    Youtube_Discord (vpn): discord,youtube
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai,google_play,porn,telegram
  podkop DNS/Bootstrap DNS: (doh) 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.14
  Предупреждение: DNS и DHCP, Строгий порядок активен!

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.87 | RAM: 21% | NAND: 27% занято / 49.1M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-04-10T15:30:02 | V**
Добрый день!
При установке podkop выходили вот такие сообщения и в итоге показывает ошибки.
Как можно исправить?

---

**2026-04-10T15:33:40 | Nickname**
Прошил бета скрипт.Но что-то пошло не так.Как это исправить                                                                                                                                                             ? = ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  v0.00 MB / ^0.00 MB
  Пинг (ya.ru via awg10): ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (5.255.255.242): 56 data bytes
  Программы в автозапуске: podkop opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН  !!!_ОПЕРА ЗАБЛОКИРОВАЛА РОССИЮ_!!! 
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:     127.0.0.1:53
    Name:       youtube.com        Address: 198.18.0.61
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai,youtube,discord,telegram,google_play
  podkop DNS/Bootstrap DNS: (doh) 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.14
  Предупреждение: DNS и DHCP, Строгий порядок активен!        Этот-только что прошил

---

**2026-04-10T15:49:04 | Kiss_My_Axe**
Не обязательно делать отдельную секцию, но желательно.
И если по каким-то причинам ZeroBlock ну никак не подходит, рассмотрите вариант Podkop-Plus на гите.
Это форк, в котором интерфейс человеческий сделали.

---

**2026-04-10T16:29:47 | Некит**
ребят вопрос, позавчера ставил последнюю прошивку и пропал podkop и zapret, потом всё накатил с помощью zeroBlock, и вопрос в следующем если я сейчас заново накачу прошивку так же всё слетит? Или же как удалить Zeroblock и zapret2, так как непривычно с ними работать? Что вообще надо сделать чтоб остался podkop и zapret?

---

**2026-04-10T16:52:40 | Routerich**
https://podkop.net/docs/tunnels/awg_settings/ пункт установка пакетов пропустить

---

**2026-04-10T16:56:31 | Maxim**
Я удалил Podkop, установил ZeroBlock + Zapret2, изменил DNS на 9.9.9.9 и вроде всё пока что работает.

---

**2026-04-10T17:02:37 | Dmitry F**
Перестал работать podkop

---

**2026-04-10T17:02:49 | Dmitry F**
Перестал работать podkop что можно сделать?

---

**2026-04-10T17:50:41 | Routerich**
Посмотрите на ютубе обзоры про podkop. Так вы поймёте общие принципы работы, дальше уже Зероблок мануал читайте

---

**2026-04-10T18:25:41 | Routerich**
https://podkop.net/

---

**2026-04-10T18:26:09 | Routerich**
Смените в Podkop dns на 9.9.9.9

---

**2026-04-10T18:26:53 | Routerich**
Пропишите в Podkop dns хостера

---

**2026-04-10T18:27:33 | Routerich**
https://podkop.net/docs/sections/ изучайте

---

**2026-04-10T18:28:10 | Routerich**
Здравствуйте.
Службы->Podkop->настройки->сервер DNS измените на 9.9.9.9 и проверяйте

---

**2026-04-10T18:35:06 | Natalia**
Привет! Умные люди, подскажите, пожалуйста, как поправить ошибки? Сегодня перестал работать дискорд и телеграм, Ютуб работает. Диагностику podkop а пробовала запускать, просто висит на этапе "DNS проверки, проверяем, пожалуйста подождите" уже минут 15...

---

**2026-04-10T18:37:59 | Routerich**
Службы->Podkop->настройки->DNS сервер->9.9.9.9

---

**2026-04-10T18:46:37 | Routerich**
Перезапустите Podkop

---

**2026-04-10T18:49:37 | VSPRO**
Всем добра, помогите пожалуйста решить, проблему. При диагностике  podkop, выдает вот такие баги.

---

**2026-04-10T18:51:38 | Routerich**
Перезапустите Podkop

---

**2026-04-10T18:58:30 | Routerich**
Если у вас Podkop, то

переносите Telegram из секции с VPN awg10 (WARP) в секцию с  Opera (Proxy) или в свою секцию (если она есть у вас)
через WARP Telegram болеет.

Если у вас ZeroBlock

перенесите список Messengers из секции awg10 в секцию Opera

---

**2026-04-10T18:58:52 | Routerich**
Надо сменить в настройках Podkop dns на 9.9.9.9

---

**2026-04-10T19:05:14 | Routerich**
Перезапустите Podkop

---

**2026-04-10T19:07:45 | Routerich**
Меняйте dns на 9.9.9.9 в Podkop

---

**2026-04-10T19:08:55 | Routerich**
Смените dns в Podkop на 9.9.9.9

---

**2026-04-10T19:09:26 | Routerich**
Перезапустите Podkop

---

**2026-04-10T19:09:42 | Routerich**
Перезапустите Podkop

---

**2026-04-10T19:12:54 | Kenny**
sh <(wget -q -O - https://raw.githubusercontent.com/routerich/RouterichAX3000_configs/refs/heads/podkop07/run_universal_config.sh) 2>&1 | tee /root/run.log

---

**2026-04-10T19:18:02 | Routerich**
Сменит dns сервер в настройках Podkop на 9.9.9.9

---

**2026-04-10T19:20:04 | Routerich**
В настройках Podkop уберите/поставьте галочку скачивать списки через Proxy

---

**2026-04-10T19:23:30 | Routerich**
Добавить свой квн в Podkop/zeroblock и подкинуть его туда

---

**2026-04-10T19:26:41 | Routerich**
https://t.me/routerich/3845/612833
В Podkop

---

**2026-04-10T19:27:40 | Routerich**
Перезагрузите Podkop

---

**2026-04-10T19:30:11 | Routerich**
Перезапустите Podkop

---

**2026-04-10T19:31:17 | Routerich**
https://podkop.net/docs/own-outbound/#amnezia-vless

---

**2026-04-10T19:33:56 | Routerich**
Галочку уберите/поставьте а настройках Podkop на скачивать списки через Proxy

---

**2026-04-10T19:51:48 | Авто Подбор**
Подскажи как обновить Podkop

---

**2026-04-10T20:00:15 | Shaykhlbarin Dmitry**
Если ставить пакеты - например podkop, запрет и другие по зависимостям - насколько велик шанс, что можно поймать проблемы? И я правильно понимаю, что тут тестовые репы подцепились? По версиям прошивки нет репозиториев?

---

**2026-04-10T20:02:22 | Routerich**
Менять dns сервер в Podkop на 9.9.9.9

---

**2026-04-10T20:03:38 | Routerich**
Здравствуйте.
Podkop перезапустите

---

**2026-04-10T20:08:15 | Ярослав**
с компа через браузер (ну лично мне так удобнее всего) через Zapter2 прекрасно работает! Но на смарте нет. Никак. Даже через Tailscail пробовал - нет. При  попытке вернуть все через Podkop, на компе работает хуже, но все же работает. На смартфоне опять нет. Прошлый раз смарт спустя час наверное прочухался и заработал через Podkop. Но опять же через некоторое время Телеграм везде отвалился. Сейчас опять через Zapret2 пустил, комп пашет - смарт нет. 🤦‍♂️🤦‍♂️🤦‍♂️

---

**2026-04-10T20:30:11 | Некит**
Вообщем я с новым вопросом, заметил что очень часто main не отвечает в podkope, и с тяжестью прогружается YouTube, инста грузит но видосы тоже переодически долго крутит, и отвалилась телега, после обновления почти ничего не менял, только в podkope убирал галочку как было сказано у ребят выше

---

**2026-04-10T20:34:23 | B R**
Подскажите, отвалился podkop, в какой ветке обсуждение? 

И второй вопрос - стоит zapret, стоит ли обновляться на zapret2?

---

**2026-04-10T20:39:10 | Сергей П.**
День добрый, не могу зайти в Cydia для iPad, может кто знает с помощью какого способа podkop или zapper или другой какой работает cydia ?

---

**2026-04-10T20:43:01 | Bumbon4ik**
Подскажите, пришёл роутер, запустил zeroblock вроде настроил всё, всё работает, подключил свой amneziaVPN , все сайты работают, телега работает.
НО telemt MTProxy не может подключиться к серверам телеги почемуто. сейчас удалил zeroblock и установил podkop, с ним MTProxy сразу заработало

---

**2026-04-10T20:46:10 | B R**
Я правильно понял, что podkop и zapret надо поменять на zeroblock и zapret2?

---

**2026-04-10T20:48:03 | Максим**
версия прошивки 24.10.4. Podkop установлен из 5 скрипта. AWG в секции Discord Работает ( но только после того как я заменил настройку скачивания списков через Discord). Main не работает, скачивание списков через него соответственно тоже. Диагностика Подкопа показывает, что  main не отвечает. DNS сменил на 9.9.9.9, галочку со скачивать списки туда-сюда снимал и ставил уже раз пять, подкоп перезапускал раз 10. Что еще сделать чтобы main  (proxy) заработал?

---

**2026-04-10T21:09:40 | Роман**
Подкопа плюс! 
https://github.com/ushan0v/podkop-plus

---

**2026-04-10T21:14:58 | Сергей Ларшин**
А замена podkopa на zeroblock не решит проблему с телегой?

---

**2026-04-10T21:22:26 | Сергей Ларшин**
Да не все нормально работало через podkop , сегодня в 19.30 лег телеграм

---

**2026-04-10T21:31:44 | Павлик🤫**
Всем привет
Собираюсь покупать routerich
Подскажите пожалуйста, из коробки стоит openwrt
Sing box, podkop, passwall2 нужно ставить для работы vless ?

---

**2026-04-10T21:54:52 | Slava Terentev**
С FakeIp пункт, это же из-за отвала мейна? Это влияет на что-то?

При проверке через урлу https://fakeip.podkop.fyi/check пишет, что fakeip = true

Влияет ли это на что-то?

---

**2026-04-10T22:01:11 | Key**
sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)

---

**2026-04-10T22:10:49 | Timur**
Подскажите какой проткоол предпочтительнее на openwrt и podkop?

---

**2026-04-10T22:14:50 | Y@roslav L**
было так же. Перезапустил podkop и ошибка ушла. Может совпадение, конечно.

---

**2026-04-10T22:18:05 | Timur**
а тут смотрели https://podkop.net/docs/troubleshooting/

---

**2026-04-10T23:40:26 | 𝒳**
Когда убираешь telegram из podkop на телефоне работать начинает

---

**2026-04-10T23:54:37 | Routerich**
#opera-proxy

Для обновления пакета opera-proxy запустите данную команду в терминале:

Если у вас установлен скрипт 5/бета:

opkg update && opkg install opera-proxy && service podkop restart

---

**2026-04-11T00:00:41 | 2taghol**
Что делать все равно пишет podkop error и ничего не работает

---

**2026-04-11T00:18:06 | Eugene Baranov**
Для обновления пакета opera-proxy запустите данную команду в терминале:

Если у вас установлен скрипт 5/бета:

opkg update && opkg install opera-proxy && service podkop restart

---

**2026-04-11T00:35:23 | Routerich**
podkop.net читайте документацию

---

**2026-04-11T01:06:27 | Zamir**
Доброй ночи!

А есть пример структуры Json - файла чтобы подкоп в РР его переварил? Видоизменный / частичный / как ссылка подписки и как vless уже пробовал скормить - не хочет,выдает ошибку:

Пodkop Error
Sat Apr 11 00:47:23 2026 user.notice podkop: [fatal] Sing-box configuration /tmp/tmp.JLoJiJ is invalid. Aborted.

, дефолтный маин совсем дефолтный:
{
  "type": "http",
  "tag": "http-proxy",
  "server": "127.0.0.1",
  "server_port": 18080
}

А как распарсенный из Neko-box джэйсон код вписать в outbound для podkop'a

Копировал дефолт конфиг 'core'

---

**2026-04-11T01:25:09 | IIlIlIlIIlIlIlIIIll**
Прошу помогите. Сломался днс сильно. Роутер был восстановлен до заводских. Podkop+zapret установил но opera proxy не установлен. Хэлп плиз

---

**2026-04-11T01:38:02 | Igor**
Сегодня отвалился ютуб.
Попытался было перенастроить podkop. Трр часа читал, пробовал, тыркался... А потом просто решился пройтись скриптом номер 5. И помогло 👍

Как он всё-таки великолепен 👌 Вот именно за это мне нравится Ваш продукт. Хотя, конечно, ковыряться с линуксом было бы интересно. Но не тогда когда семья требует "верни Ютуб", а времени на это нет 😁

Спасибо вашей команде! Отдельно Спасибище тем кто сделал этот великолепный баш-скрипт.

---

**2026-04-11T01:54:08 | Alex_Jester**
На автора podkop

---

**2026-04-11T05:38:35 | ᗩᒪEKᔕEY ᗷᗩTEᗰᗩᑎ**
что за ошибка: Podkop Error
Sat Apr 11 05:37:26 2026 user.notice podkop: [error] Outbound section not found. Please check your configuration file (missing proxy_string, interface, outbound_json, or urltest_proxy_links). Aborted.

---

**2026-04-11T06:40:10 | Белозеров В.А.**
Sat Apr 11 06:32:01 2026 user.notice podkop: [error] Detected https-dns-proxy in DHCP config. Edit /etc/config/dhcp

Подскажите что за ошибка в подкопе? как исправить

---

**2026-04-11T08:03:12 | Белозеров В.А.**
Может кому поможет у кого Podkop (у меня все заработало), делал так:

Перегрузил 5 скрипт:

wget --no-check-certificate -O /tmp/setup.sh https://raw.githubusercontent.com/routerich/scripts/main/setup.sh && chmod +x /tmp/setup.sh && /tmp/setup.sh

Выполнил перезапуск роутера;

Обновил opera-proxy 
opkg update && opkg install opera-proxy && service podkop restart

Выполнил перезапуск роутера; 

Заходим в Службы -> Podkop -> Секции "Main" -> Списки сообщества -> Убрал оттуда ТГ и Ютуб (если у вас были). 

Далее 
Заходим в Службы -> Podkop -> Секции "Discord" -> Списки сообщества у меня там: Discord Telegram Youtube Meta Twitter (X) Google AI 

После каждой сексии необходимо применить настройки!!!

Далее 
Заходим в Службы -> Podkop -> Настройки и ищем пункт "Скачивать списки через выбранную секцию" поставил "Discord"

Как 2 часа на всех устройствах все работает стабильно.

---

**2026-04-11T08:15:35 | Aleksey**
Мне помогло обновление через скрипт 

#opera-proxy

Для обновления пакета opera-proxy запустите данную команду в терминале:

Если у вас установлен скрипт 5/бета:

opkg update && opkg install opera-proxy && service podkop restart

Через "Обновить пакеты" не помогало

---

**2026-04-11T08:15:50 | Белозеров В.А.**
Sat Apr 11 08:14:39 2026 user.notice podkop: [error] Detected https-dns-proxy in DHCP config. Edit /etc/config/dhcp 

Критичная ошибка?

---

**2026-04-11T09:03:22 | Aleksandr Kuzin**
Не нашел YouTube в main podkop, откуда он в отчёте тогда?

---

**2026-04-11T09:13:52 | Kirill Y**
Так в zeroblock скрипта вроде нет.. Или Вы советуете на podkop перейти на 5-й скрипт или бету?

---

**2026-04-11T10:49:37 | Михаил Полиенко - Инвестиции в бизнес**
Помогите разобраться с ошибкой.
Сейчас в поездке, с роутером работаю через tailscale - поэтому перепрошить или сбросить и откатить на бэкап не вариант - если tailscale отвалится, я сразу потеряю доступ. Там на месте человек без рук, который может только ребутнуть.

Симптомы проблемы: В "статусе" интернет показывается доступен, всё хорошо. При этом вообще никакие страницы не открываются. Грешу на весь этот колхоз из sing-box и подкопа.
Еще вчера утром все работало, запрещенка, мессенджеры и т.п., потом в какой-то момент просто весь интернет перестал быть доступен, а диагностика подкопа стала гореть всеми цветами радуги.
После двух перезагрузок имеем следующее состояние:
В диагностике горит красным "DNS роутера не проходит через sing-box"

При тесте через терминал команда "curl -v https://fakeip.podkop.fyi/check" зависает и ничего не возвращает.

Пробовал делать перезапуск подкопа и sing-box в любой последовательности, это ничего не дает.

Цитата из руководства "Убедитесь, что роутер с Podkop является шлюзом для вашего устройства" - это что-то на нерусском, моя не понимать. Вчера все работало.

---

**2026-04-11T11:09:50 | Dark Ghost**
Тогда я подожду ответа экстрасенсов, которые расскажут, куда через что пытается ходить podkop, и прочие его настройки.

---

**2026-04-11T11:13:10 | Qarma Queen**
#opera-proxy

Для обновления пакета opera-proxy запустите данную команду в терминале:

Если у вас установлен скрипт 5/бета:

opkg update && opkg install opera-proxy && service podkop restart
После ребутнуть ровтер

---

**2026-04-11T11:17:16 | Alexx**
Добрый день подскажите пожалуйста, после переустановки Podkop и обновления прокси в Podkop появилась "Найдены дополнительные правила маркировки", Это нормально?

---

**2026-04-11T11:22:00 | Qarma Queen**
#opera-proxy

Для обновления пакета opera-proxy запустите данную команду в терминале:

Если у вас установлен скрипт 5/бета:

opkg update && opkg install opera-proxy && service podkop restart
После ребутнуть ровтер

---

**2026-04-11T11:43:32 | Kiss_My_Axe**
В терминал и воскурить фимиам всем богам, чтобы помогло.😀
sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)

---

**2026-04-11T12:14:09 | Kiss_My_Axe**
Значит конфиги сингбокс сдохли, почти сотка.
Тааак.
Система - Восстановление / Обновление
Верхняя кнопка Создать архив

И только после создания архива запускать код
Код вынесет сингбокс, подкоп и все конфиги
Потом раздел BETA, закреп, скрипт №5
opkg --force-removal-of-dependent-packages --autoremove remove sing-box
opkg --force-removal-of-dependent-packages --autoremove remove podkop
rm -rf /etc/config/sing-box
rm -rf /etc/init.d/sing-box
rm -rf /etc/sing-box
rm -rf /usr/bin/sing-box
rm -rf /usr/share/sing-box

---

**2026-04-11T12:38:49 | Dmitry Red**
добрый день. подскажите ошибка в подкопе что значит? что нужно сделать?

user.notice podkop: [error] Download meta list failed

---

**2026-04-11T12:46:17 | Dmitrii Burenin**
Podkop настройка забить в гугле.

---

**2026-04-11T13:04:10 | Aleksei**
Я правильно понимаю, что бы мне использовать свой vless через podkop, нужно поднять дополнительное новое соединение (обычное tls, a не xhttp)?

---

**2026-04-11T13:08:44 | Sergey Solomatin**
а есть инструкция
если купить себе vps сервер, как его настроить и добавить в podkop?

---

**2026-04-11T13:10:45 | Routerich**
podkop.net Как сделать ключ vless на своем сервере, гуглится за 5 секунд, готовых скриптов куча уже

---

**2026-04-11T13:12:57 | 𝐕𝐥𝐚𝐝𝐢𝐬𝐥𝐚𝐯**
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.15 | YouTube IP:  198.18.0.46

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.21 MB
  Пинг (ya.ru via awg10): Ожидайте, идет замер (10 пакетов)...
  Пинг (ya.ru via awg10): 20.640 / 22.931 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН  !!!_ОПЕРА ЗАБЛОКИРОВАЛА РОССИЮ_!!! 
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200 OK) [tlsv1.3] [try: 1]
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server: 127.0.0.1:53
    Name: youtube.com        Address: 198.18.0.46
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop    Youtube_Discord (vpn): youtube,telegram,discord
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: (doh) 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.14
  Предупреждение: DNS и DHCP, Строгий порядок активен!

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.38 | RAM: 22% | NAND: 26% занято / 49.0M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-04-11T13:42:27 | Routerich**
По логам они у вас подключаются и адреса выдаются им, а дальше проблемы с podkop

---

**2026-04-11T13:47:30 | Routerich**
Система - автозапуск - найдите podkop и если есть zapret или youtubeUnblock нажмите на включено. Перезагрузите роутер. Протестируйте как подключаются Яндекс станции. Без обходов надо убедиться точно в работоспособности нормальной. Далее будем разбираться

---

**2026-04-11T13:48:38 | ZZII | RTK**
что вообще лучше, podkop или zeroblock? просто у меня какие то проблемы с ним, то некоторые сервисы не работают, включаю и отключаю какие то сообщества - начинает работать. что делать, вообще не понимаю

---

**2026-04-11T13:51:04 | Routerich**
Теперь идите в перенаправления обратно. Убирайте там 127.0.0.42 и вписывайте 127.0.0.1#5359 и нажмите + и далее применить. Далее в службы - podkop - настройки. Поставьте галочку на не трогать мой DHCP. Далее Роутер перезагрузите. И проверяйте

---

**2026-04-11T14:09:22 | Альбе́рт Эйнште́йн**
и в podkop добавить новый интерфейс?

---

**2026-04-11T14:36:08 | Роман**
Что показывает диагностика в Podkop?

---

**2026-04-11T14:45:46 | ZZII | RTK**
что вообще лучше, podkop или zeroblock? просто у меня какие то проблемы с ним, то некоторые сервисы не работают, включаю и отключаю какие то сообщества - начинает работать. что делать, вообще не понимаю

---

**2026-04-11T15:22:20 | Ghost**
то есть через podkop ?

---

**2026-04-11T15:52:58 | Evgeny**
а как обновить PODKOP до последней версии?

---

**2026-04-11T16:15:38 | Anton Klimov**
Как можно удалить только podkop на роутере

---

**2026-04-11T16:31:52 | Артем**
Прошу помощи, подкоп дурить начал дурить. Выдает такие ошибки. Podkop Error
Sat Apr 11 16:28:46 2026 user.notice podkop: [error] Download telegram list failed

---

**2026-04-11T16:42:48 | Tim Mars**
а как создать эту секцию в podkop? и, к примеру, добавить новые списки? или эта тема только для zb работает?

---

**2026-04-11T16:45:35 | V T**
Добрый день! Не работает телеграмм через приложение на телефонах. WEB-версия на ПК работает. Подскажите, проблема может быть именно через приложение? Или я с настройками что-то накосячил?

Включен Podkop v0.7.14, поменял Bootstrap DNS-сервер на 9.9.9.9. До секции MAIN пингуется, там подключены списки:
1) Meta;
2) Twitter;
3) Telegram;
4) Заблокировать;
5) Google AI;

Так же установлен ZeroBlock 0.6.1-r150 с двумя секциями маршрутизации:
1) opera - тут полностью маршрутизируется только IP адрес ПК. Списки Geo Block, Заблокировать, Meta, Twitter, Google AI;
2) awg10 - тут полностью маршрутизируются все остальные девайсы И исключён IP адрес ПК. Списки YouTube, Meta, Twitter, Telegram, Google AI. Конфиг для этой секции прикреплю скрином к сообщению;

С телефонов нормально работает ютуб/инстаграмм и прочая запрещёнка, настроенная в списках секции awg10 в ZeroBlock'е, но телеграмм через приложение вообще не работает.

---

**2026-04-11T16:46:13 | Renat**
Единственное версия podkop 0.7.10

---

**2026-04-11T16:54:14 | Renat**
Бета версия скрипта для обхода ограничений.

Основное отличие от скрипта №5, что тут  используется последняя версия Podkop (v0.7.14).

Из ключевых отличий этой версии то, что там баг с WARP и CloudFlare починили, добавили исключения и список Roblox можно сразу выбрать.

Важно: 
1. Перед запуском сделайте бэкап (Система->Восстановление и обновление->Создать архив)
2. Если у вас всё работает хорошо, в частности youtube не надо его запускать.
3. Если не готовы сбрасывать роутер после неудачной отработки скрипта, лучше не запускайте скрипт.

Если вы всё таки решились запустить его, то от вас мне нужны полные логи запуска скрипта от начала его работы до завершения. Файл с логами будет по пути /root/run.log, можете его скачать через 
Веб морда роутера->NAS->Файловый менеджер->/root/run.log, скачать 
Потом пришлите его, для анализа.

P.S. запустится только на прошивках версии не ниже 24.10.2

Сам код для запуска ниже.
sh <(wget -q -O - https://raw.githubusercontent.com/routerich/RouterichAX3000_configs/refs/heads/podkop0711/universal_config_new_podkop.sh) 2>&1 | tee /root/run.log

---

**2026-04-11T16:57:04 | Артем**
Заходите Система-Пакеты. Там кнопка зеленая обновить списки. Жмете и ждете. После завершения закрываете окно которое напишет что обновлено. Далее вкладка обновления, а в поле фильтра вводим podkop. Появится две строки. И кнопки обновить рядом со строчками. Жмем и радуемся.

---

**2026-04-11T17:03:54 | Ilya ☀️**
Sat Apr 11 17:00:53 2026 user.notice podkop: [error] Download https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_cidr_ipv4.txt list failed
Podkop Error
Sat Apr 11 17:00:46 2026 user.notice podkop: [error] Download discord list failed
Podkop Error
Sat Apr 11 17:00:39 2026 user.notice podkop: [error] Download twitter list failed
Podkop Error
Sat Apr 11 17:00:32 2026 user.notice podkop: [error] Download meta list failed

:(

---

**2026-04-11T17:06:00 | Роман**
Если так хочется обновить подкоп, podkop.net обновляйте скриптом с сайта.

---

**2026-04-11T17:26:40 | Renat**
Я в этом вообще не шарю, до этого все делал по инструкции но тг и ютуб именно через приложения на телефоне так и не работали и прочитал что обновив podkop заработает

---

**2026-04-11T17:38:56 | Remember**
Что нужно сделать, что бы в podkop телеграм завёлся\

---

**2026-04-11T17:39:29 | Sergei**
С Telegram мне помогло после вчерашнего, просто перенести лист в podkop с proxy на vpn

---

**2026-04-11T17:41:16 | Sergei**
нет, все на стандарте. У тебя секции vpn нету в podkop, тебе ее создать надо

---

**2026-04-11T17:53:38 | А А**
коллеги возникла проблема с ноутбуком на убунте 25.10, когда стартует машинерия на роутере podkop+dnsmasq и всё остальное, ноут перестает получать от роутера DNS ответы

---

**2026-04-11T18:38:51 | Роман**
Для этого и существуют zeroblock/podkop, они точечно маршрутизируют трфик. Вопрос в том какого вида конфиг.

---

**2026-04-11T18:42:10 | Routerich**
Сделайте так. Система - автозапуск - остановить podkop и zapret, далее выключите ноутбук. через минуту запускайте подкоп и включайте ноут, после полного включения и подключения к сети, присылайте логи Статус - просмотр лога - скачать журнал

---

**2026-04-11T18:51:34 | Kinaman**
Здравствуйте! У меня установлен Podkop и Zapret, до последних дней все основные заблокированные ресурсы работали, но два дня назад перестали открываться Meta (Instagram) и Twitch.tv. Я собрал все сведения о системе. Подскажите, пожалуйста, что можно сделать, чтобы вернуть доступ к ресурсам?

---

**2026-04-11T18:54:56 | Алексей**
Подскажите, что делать. ТГ отвалилась. Перенос из секции podkop в дискорд не помогло 😔

---

**2026-04-11T19:14:05 | Илья_ПапинСовет**
Всем доброго, подскажите пожалуйста после ребута роутера с подкопом не стартует sing- box автоматом, только после принудительного перезапуска podkopa

---

**2026-04-11T19:16:19 | Routerich**
https://podkop.net/docs/tunnels/awg_settings/ пункт установка пакетов пропускайте, и проверьте по списку что всё правильно сделали

---

**2026-04-11T19:34:41 | Andrey Shashev🧑🏻‍💻**
роутер поднял. теперь не работает подкоп. Podkop Error
Sat Apr 11 19:02:41 2026 user.notice podkop: [error] Download https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_cidr_ipv4.txt list failed подскажите как решить

---

**2026-04-11T19:39:22 | Anna Bagler**
podkop.net Секции, изучайте.

---

**2026-04-11T19:47:17 | Routerich**
Смените в  настройках Podkop dns сервер на 9.9.9.9

---

**2026-04-11T20:01:53 | Timur**
сбросил routerich , скажите что лучше ставить podkop или zeroblock?

---

**2026-04-11T20:02:47 | Routerich**
Dns в Podkop смените на 9.9.9.9

---

**2026-04-11T20:03:32 | Routerich**
Это исправлять не надо, а вот в Podkop dns смените на 9.9.9.9

---

**2026-04-11T20:08:22 | Максим**
Подскажите тоже не работает не ютуб не телега. В чем может быть проблема? Анализ запущен: 2026-04-11 20:04:29
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.18 | YouTube IP:  198.18.0.19

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓5.12 MB / ↑0.12 MB
  Пинг (ya.ru via awg10): 31.773 / 33.407 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН  !!!_ОПЕРА ЗАБЛОКИРОВАЛА РОССИЮ_!!! 
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200 OK) [tlsv1.3] [try: 1]
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:     127.0.0.1:53
    Name:       youtube.com        Address: 198.18.0.19
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop    Youtube_Discord (vpn): youtube,discord
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai,telegram
  podkop DNS/Bootstrap DNS: (doh) 9.9.9.9 / 8.8.8.8
  Версия podkop: v0.7.10
uci: Entry not found
  Предупреждение: DNS и DHCP, Строгий порядок активен!

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.31 | RAM: 24% | NAND: 26% занято / 50.0M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-04-11T20:29:36 | Timur**
скажите а где ключ прописать vless? стоит zeroblock. podkop не стоит

---

**2026-04-11T20:39:44 | Anna Bagler**
Если у вас zeroblock, то есть полный мануал, если подкоп - podkop.net Ceкции.

---

**2026-04-11T20:50:21 | Timur**
объясните пожалуйста куда засовывать? до этого на openwrt сидел через podkop

---

**2026-04-11T21:02:53 | Routerich**
В сеть - интерфейсы - изменить напротив вашего интерфейса, и поставить галочку на не создавать маршруты. Сохранить и применить. Далее https://podkop.net/docs/tunnels/awg_settings/ пункт установку пакетов пропустить

---

**2026-04-11T21:34:45 | Тихон**
Спасибо, вот результат

Анализ запущен: 2026-04-11 21:32:10
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Попытка обновления списка пакетов: (1/2)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Package curl (8.12.1-r1) installed in root is up to date.
Configuring wget-ssl.

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.1.128 | YouTube IP:  198.18.0.117

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.68 MB / ↑0.13 MB
  Пинг (ya.ru via awg10): 35.722 / 37.389 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН  !!!_ОПЕРА ЗАБЛОКИРОВАЛА РОССИЮ_!!! 
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200 OK) [tlsv1.3] [try: 2]
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:     127.0.0.1:53
    Name:       youtube.com        Address: 198.18.0.117
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop    Youtube_Discord (vpn): youtube,discord,telegram
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai,cloudfront
  podkop DNS/Bootstrap DNS: (doh) 8.8.8.8 / 8.8.8.8
  Версия podkop: v0.7.10
  Предупреждение: DNS и DHCP, Строгий порядок активен!

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.22 | RAM: 24% | NAND: 26% занято / 49.9M доступно
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

root@RouteRich:~#

---

**2026-04-11T21:39:09 | Dmitriy**
Подскажите, я на роутере давно установил Zapret, Zapret2 и Podkop, вроде все работало хорошо, но вот 2-3 дня назад, когда ркн начали новую волну давления на телеграм у меня телега совсем перестала работать. Постоянно в статусе "обновление" висит и все, иногда на статус "соединение" переходит. 

Кто-то уже знает как починить Podkop/Zapret2? (Я так понял Zapret обычный или не работает или нужен для Zapret2)

---

**2026-04-11T21:41:07 | Dmitriy**
а podkop? я использовал скрипт из канала, когда там он 15 минут крутил и настраивал обходы

---

**2026-04-11T21:42:58 | Dmitriy**
просто у меня podkop отлично работает для других вещей типа ютубчика или чата гпт, я не покупал никаких впнов для его работы

я в целом думал, что это что-то типа goodbyeDPI

---

**2026-04-11T21:46:05 | Routerich**
podkop.net изучайте

---

**2026-04-11T22:10:14 | Timur**
а zeroblock  чем отличается от podkopa?

---

**2026-04-11T22:20:31 | Стас Немченко**
Почему-то появился после загрузки Podkop, но появился — и здорово :^)

---

**2026-04-11T23:24:27 | Василий**
Подскажите, сижу на ZeroBlock , отключил и podkop и zapret. Перенес список Messengers из секции awg10 в секцию Opera, полет нормальной, кроме телеграм на телефоне.

---

**2026-04-11T23:31:16 | ~**
Всем доброго времени суток! Подскажите идей, а то свои уже все перепробовал. Айфон не подключается к wifi, при этом другие семейные айфоны подключились без проблем. Пробовал и канал менять, и частоту менять 160->80->40МГц  - ничего не помогает. При этом к прошлой одноименной сети подключался нормально. А после того как за сеть стал отвечать RR - ни в какую не хочет подключаться. Получение IP и DNS - автоматически от роутера. На роутере подняты Zapret, Podkop, Tailscale. В предыдущей сети было все тоже самое кроме Tailscale. Есть идеи, что еще может влиять на успех подключения (проверить пароль просьба не предлагать)?

---

**2026-04-11T23:32:39 | Routerich**
https://t.me/routerich/80283/468513 Общий принцип можете посмотреть на ютубе про podkop. Смысл тот же, только Зероблок намного шире по функциям

---

**2026-04-11T23:54:21 | Әмир**
3 раза сбрасывал до завода. После чего пытался zeroblock накатить. Из раза в раз происходила такая чехарда с DNS. (5-ый скрипт не применял)
В итоге, забрал с той квартиры роутер, привёз к себе. Подключил также вторым номером, но через первый - Routerich. На первом отключил Podkop перед манипуляциями со вторым роутером.

В итоге, всё встало, vless поднялся с пол тычка 🤷🏻‍♂️
Мистика какая-то

---

**2026-04-12T00:10:58 | Kiss_My_Axe**
Это бест. Но как работать будет - увидим.
Это пульните в терминал.

sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)

---

**2026-04-12T00:50:28 | Routerich**
Podkop + sing-box extended по поиску можно найти

---

**2026-04-12T03:22:50 | Kiss_My_Axe**
В терминал роутера.

service ruantiblock stop
service ruantiblock disable
opkg update
opkg install opera-proxy

sh <(wget -q -O - https://raw.githubusercontent.com/routerich/RouterichAX3000_configs/refs/heads/podkop0711/universal_config_new_podkop.sh) 2>&1 | tee /root/run.log

---

**2026-04-12T04:49:31 | Sergey**
нет у меня podkop

---

**2026-04-12T07:09:11 | Kiss_My_Axe**
Попробуйте вкинуть в терминал это.
sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)
Если не поднимет, тогда сбросим конфиги подкопа, или накатим №5, он должен сам их стереть и первичную настройку произвести.

---

**2026-04-12T07:34:28 | Routerich**
Перезапустить Podkop

---

**2026-04-12T08:40:57 | Routerich**
Сменить DNS в настройках Podkop на 9.9.9.9
Обновите Opera-proxy

---

**2026-04-12T08:43:42 | Kiss_My_Axe**
В терминале роутера

# 
#
opkg update
opkg install opera-proxy
service zeroblock restart
service podkop restart
#
#

---

**2026-04-12T11:03:04 | Stasnislav**
Подскажите пожалуйста. При диагностики podkop поЯвилась вот такая ошибка . Main не отвечает. Что делать

---

**2026-04-12T11:11:04 | Anna Bagler**
Какие именно цифры после 0.7? Должен быть тип исключений. https://podkop.net/docs/sections/#tip-podklyucheniya-connection-type

---

**2026-04-12T12:07:24 | Андрей**
Добрый день, направьте пожалуйста по дальнейшим действиям) Не особо силен в терминах, но постараюсь объяснить.

1) Есть уже один роутер routeRich, на нем еще в декабре ставил прошивку последнюю (на тот момент), потом ставил скрипт №5, в итоге ютуб работал через podkop. 
После нового года купил второй роутер, и вот только сейчас решил его настроить (+ на первом роутере ютуб и телеграмм работают через раз). 
Думаю использовать второй роутер для эксперимента: обновить прошивку, поставить скрипт №5 так же и нахваленный ZeroBlock. Норм вариант или лучше пробовать что-то другое сразу ?

2) Думал, что если получится все настроить на роутере, то затем использовать его как Exit Node (видел такое в теме Remote Control) ,  чтобы мобильные телефоны (вне дома) выходили в заблокированные сайты через роутер. Звучит как будто прекрасным вариантом (в плане того, что одна точка входа и одна настройка для всех устройств). Или такое не получится / лучше так не делать ?

3) И еще: у меня есть подписка на отдельном сервисе, который позволяет:
• сгенерить ключ Stealth Proxies (на телефоне им пользуюсь в режиме Proxy/Vpn) через клиент Hiddify и v2rayNG - телеграмм и ютуб работают (правда, частенько страну подключения приходится менять)
• сгенерить ключик для Amnezia WG (на телефоне через клиент Amnezia WG не работает этот подход) 
Может, лучше будет этот ключ подсунуть в роутер ?

---

**2026-04-12T12:20:03 | Лёша Kempo**
Привет! Скрипт 5 после выполнения заканчивается с этим:

isWorkZapret = 0, isWorkOperaProxy = 1, isWorkWARP = 1
 [32;1mRestart service dnsmasq, odhcpd... [0m
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: no lease, failing
 [32;1mStop and disabled service 'youtubeUnblock' and 'ruantiblock' and 'zapret'... [0m
uci: Entry not found
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: no lease, failing
Downloading 'https://raw.githubusercontent.com/routerich/RouterichAX3000_configs/refs/heads/wdoctrack/config_files/podkopNew'
Connecting to 185.199.111.133:443
Writing to '/etc/config/podkop'

/etc/config/podkop   100% |*******************************|  1814   0:00:00 ETA
Download completed (1814 bytes)
Backup of your config in path '/root/podkop'
Podkop reconfigured...
 [32;1mStart and enable service 'doh-proxy'... [0m
 [32;1mService Podkop and Sing-Box restart... [0m
Start podkop
service_triggers start
 [32;1mByPass block for Method 2: AWG WARP + Opera Proxy...Configured completed... [0m
 [31;1mAfter 10 second AUTOREBOOT ROUTER... [0m

Как лечить?

---

**2026-04-12T12:57:49 | WAXT3R**
Здравствуйте!

Подскажите, стоит ли удалить ZB+Z2 и вернуть podkop?

Отвалилась телега, геоблок почти не работает, все AI тоже перестали робить.

Возвращение на podkop поможет с этим? Или лучше заново переустановить ZB+Z2?

---

**2026-04-12T13:41:29 | Андрей М**
Всем привет. На днях столкнулся с такой проблемой... После отключения питания на роутере при новом подключении нет сети, соединение есть но без доступа в интернет. В Статус пишет что подключено но трафика нет. Решается проблема перезапуском интерфейсов в ручную. После чего всё работает нормально до следующего обесточивания роутера. На роутере стоит скрипт 5, Podkop, Zapret. Провайдер Ростелеком. Всё что мне нужно открывается в этой конфигурации, но каждый раз лезть в роутер для ручного перезапуска интерфейсов - это геморрой. Может кто знает как исправить?

---

**2026-04-12T14:30:24 | Sergey**
помогите пожалуйста настроить роутер, не работает ютуб, инста и т.д. у меня в службах podkop не указан

---

**2026-04-12T14:33:08 | Kiss_My_Axe**
В терминале роутера
#
#
opkg update
opkg install opera-proxy
service zeroblock restart
service podkop restart
#
# 
Потом минут 10 потерпеть.
Телега, скорее всего, на опере работать не будет, но остальное бегает как-то.

---

**2026-04-12T14:42:32 | Sergey**
помогите пожалуйста настроить роутер, не работает ютуб, инста и т.д. у меня в службах podkop не указан

---

**2026-04-12T15:29:59 | Anna Bagler**
Так у вас zero или podkop?

---

**2026-04-12T17:20:40 | PavelS**
Подскажите, в логах скачет такая ошибка на Podkop, это нормально?
daemon  err  sing-box[2508]:  [31mERROR [0m[0041] [ [38;5;195m2412645627 [0m 0ms] router: UDP is not supported by outbound: main-out

---

**2026-04-12T17:24:25 | Виктор**
Приветствую всех! Полгода назад установил скрипт №5. Насколько я понимаю - это установка и настройка podkop. Но последнюю неделю много сайтов перестала работать, в т.ч. и youtube. Есть такое же простое решение для нашего роутера? Почитал, zeroblock советуют. Надо его устанавливать? Podkop отключать?

---

**2026-04-12T18:04:02 | Vasya Mafia**
Всем привет! Осмотрел wiki, не нашел базовой для меня инфы. Отдельно вроде про всё есть: zapret, podkop, zeroblock и тп. Есть ли какая-то между ними взаимозависимости? Я так понимаю что это разные средства для обхода блокировок. У кого-то стоит podkop, а у кого-то zeroblock вместе zapret, они должны быть вместе или одного достаточно? Я только купил роутер, у меня есть vps с поднятым vless, может подскажите что-то простое чтобы использовать его?

---

**2026-04-12T19:27:16 | Routerich**
Так как его в репах нет, можете скрипт с канала itdog взять и обновить его
Или бета скрипт запустить, если не вставляли в Podkop свой конфиг, настройки

---

**2026-04-12T20:35:06 | Илья Абрамов**
Со второго раза скрипт выполнился, но ресурсы недоступны. В разделе Службы- Podkop вот такие ошибки

---

**2026-04-12T20:49:57 | Илья Абрамов**
1 в 1 ситуация. Нажал кнопку "Перезапуск Podkop" - много заработало, кроме телеги)

---

**2026-04-12T20:51:11 | Arsen Kornienko**
О-о, спасибо. Это не podkop, получается, а вместо него ZeroBlock поставить? Или можно через podkop?

---

**2026-04-12T20:53:58 | Dmitry Puzanov**
У меня в podkop так и работает все

---

**2026-04-12T20:54:37 | Артём Фомин**
Думаю можно и через podkop. ZeroBlock просто более продвинутый пакет. Там больше гибкости с настройками и можно добавлять не только vless tcp Reality

---

**2026-04-12T21:35:59 | Routerich**
https://podkop.net/docs/tunnels/awg_settings/ пункт установка пакетов пропустить

---

**2026-04-12T21:37:44 | Сергей К**
Нет. Podkop и Zapret. Его допом установить? Zero Blok в смысле. Я бы уже его давно воткнул, но нет осознанного понимая, что оставить, а что снести.

---

**2026-04-12T22:17:50 | Роман**
https://github.com/StressOzz/Podkop-Manager

---

**2026-04-12T22:32:01 | Oleg Lego**
подскажите ставил скрипт 5 сейчас пишет в диагностике Podkopv0.7.10Устаревшая
если снова скрипт 5 запустить обновит?

---

**2026-04-12T23:01:11 | Anna Bagler**
Либо подкоп не удалять, либо сброс и Zeroblock. Cоздать свой интерфейс по аналогии с awg10, импортировать туда свою конфигурацию, привязать свой интерфейс к секции в podkop/zero. Выбрать нужные списки. Zeroblock гибче.

---

**2026-04-12T23:07:23 | Key**
Откройте терминал и вбейте. Обновит подкоп до максимальной версии
sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)

---

**2026-04-12T23:28:52 | Routerich**
Используйте платный впн/прокси и интерфейс тейлскейла добавлен в podkop?

---

**2026-04-12T23:35:49 | Nikolai Korp**
podkop перезагрузил, заработало, спасибо

---

**2026-04-13T00:13:29 | Stan**
Здравствуйте. Добавил aws в оперу. Увы, Strava не зафунциклировала. Ранее на podkop работала. Что посоветуете?

---

**2026-04-13T05:34:51 | Routerich**
Здравствуйте. 
Пропускаем установку пакетов
https://podkop.net/docs/tunnels/awg_settings/#o-pravilah-faervola

---

**2026-04-13T06:34:34 | Никита Горбачёв**
если честно, то не ясно как

полагаю, что из-за того что службы передергиваются скриптом, на момент диагностики они еще не успевают полностью запуститься 

внутренняя диагностика подкопа через ~30 секунд после старта скрипта выдает все зеленое 

команды
dig fakeip.podkop.fyi
и 
curl -v https://fakeip.podkop.fyi/check
тоже говорят, что фейкайпи поднят

---

**2026-04-13T09:28:02 | Routerich**
включите список Telegram в Podkop

---

**2026-04-13T09:31:36 | Routerich**
обновите opera-proxy через Система->пакеты
смените в настройках Podkop DNS сервер на 9.9.9.9

---

**2026-04-13T09:32:46 | Your_secret_friend**
Добрый день! Подскажите, на роутере v1 работает ли podkop+amneziawg?

---

**2026-04-13T09:43:33 | Routerich**
для телеграмма либо используйте прокси либо платные решения добавляйте в Podkop

---

**2026-04-13T11:32:04 | IIlIlIlIIlIlIlIIIll**
Здравствуйте. почему такое ? на всех дефолтных днс такое в podkop

---

**2026-04-13T11:36:33 | Routerich**
1. обновить opera-proxy через Система->пакеты
2. в настройках Podkop изменить DNS сервер на 9.9.9.9

---

**2026-04-13T11:42:13 | IIlIlIlIIlIlIlIIIll**
днс попробуйте поменять на doh в podkop

---

**2026-04-13T12:24:08 | Routerich**
Здравствуйте.
в настройках Podkop галочку поставьте/уберите с скачивать списки через Proxy/VPN

---

**2026-04-13T12:51:11 | Сущенко Валерий**
Стоит PodKop, не работал ТЛГ. Удалил его из секции MAIN b  и добавил в секцию YUTUBE_DISCORD и ТЛГ заработал и на компе и на смартфоне. Ютуб и Инста тоже работают. Подскажите, я все правильно сделал, ничего не накроется. Можно сохранить настройки в архив.

---

**2026-04-13T13:05:59 | Routerich**
Здравствуйте.
https://podkop.net/docs/tunnels/awg_settings/

---

**2026-04-13T13:09:27 | Сущенко Валерий**
Да, я сам не шарю. Открыл Роутериш - потом вкладки  Службы - Podkop - Вверху написано MAIN - ниже Списки сообщества - в нем Телеграмм (нажал на красный крестик). Спустился ниже -  YUTUBE_DISCORD - Таблица Списки сообществ - Нажал Service List - добавил Телеграмм  и сохранил все - кнопка в самом низу, потом Применил. Телега заработала на компе сейчас с нее печатаю, а то 3 дня с 10 апреля висела. Больше ничего не делал.

---

**2026-04-13T13:42:02 | Routerich**
обновить пакет opera-proxy через система->пакеты
в настройках Podkop->смените dns сервре на 9.9.9.9

---

**2026-04-13T14:00:18 | Vlad**
Всем привет
Настраивал роутер по этой инструкции https://podkop.net/docs/tunnels/awg_settings/
Не работает вот прям ничего из заблокированного. Куда тыкаться непонятно вообще. Скрипт рекомендуемый повсюду выполнил, а как читать и чем он мне поможет не пойму. Хелпаните, пожалуйста, задолбался настраивать роутер)

---

**2026-04-13T14:30:23 | Kiss_My_Axe**
Для авг10 сгенерировать новый конфиг, генератор llimonix warp в google.
А лучше переходите на ZeroBlock, там две галки поставить и половина нужного настроится сама.

Решите перейти на зероблок, удалите подкоп через Система - Пакеты, вкладка Установленные. Фильтр podkop.

---

**2026-04-13T14:35:41 | Роман**
Ставьте подкоп, если хотите. podkop.net

---

**2026-04-13T16:08:21 | Anna Bagler**
https://podkop.net/docs/workvpn/ - принцип одинаков.

---

**2026-04-13T18:38:51 | Routerich**
а теперь покажите диагностику Podkop

---

**2026-04-13T18:40:42 | Routerich**
в настройках Podkop уберите галочку скачивать списки через Proxy

---

**2026-04-13T18:49:32 | Routerich**
Здравствуйте.
Если Podkop то https://github.com/itdoginfo/allow-domains/tree/main

---

**2026-04-13T19:17:34 | Routerich**
В настройках Podkop убрать/поставить галочку на скачивать списки через Proxy

---

**2026-04-13T19:23:39 | Amras Amandil**
Понимаю, что вопрос был, но что-то не получается у меня добавить VLESS на роутер. В podkop в секции добавляю новую секцию, тип proxy, тип конфы - url подключения, URL VLESS добавляю, дальше сохранить, применить и ребут роутера. И такое ощущение, что начинается конфликт с main. Перестаёт работать всё, что работает через main. Может есть скрин правильной настройки?

---

**2026-04-13T19:26:33 | Routerich**
Здравствуйте.
А если Стопнуть Podkop, работают?

---

**2026-04-13T20:05:48 | Ярослав Онищенко**
Podkop и zapret'ы два. Не знаю как не конфликтуют, но всё работает))

---

**2026-04-13T21:19:48 | ARTYOM RISEMAN**
Я вообще не специалист в роутерах. Купил Routerich. Вчера, установил podkop, следуя инструкции. Кое-что заработало, но не всё. Chatgpt не работает, Grok не работает, Telegram не работает. Хотел узнать, что надо установить, подключить, настроить, что бы всё работало?

---

**2026-04-13T21:34:06 | Kiss_My_Axe**
Вот это в терминал роутера.


# --- ТЕРМИНАЛ ---
Службы - Терминал
Login: root
Password: пароль на вход в вебморду роутера, при вводе не отображается.
После авторизации большая надпись роутерич
Теперь можно вставлять ссылку

sh <(wget -q -O - https://raw.githubusercontent.com/routerich/RouterichAX3000_configs/refs/heads/podkop0711/universal_config_new_podkop.sh) 2>&1 | tee /root/run.log
#
#

---

**2026-04-13T21:48:22 | ARTYOM RISEMAN**
Они будут в паре с podkopom работать?

---

**2026-04-13T21:50:30 | ARTYOM RISEMAN**
А. Или одно или другое? Podkop надо будет совсем снести или его просто можно не использовать?

---

**2026-04-13T22:09:20 | ~**
Ну пока 0 )) Не успеваю вики штудировать роутер у меня 5 день, но и работа съедает массу времени. Осваиваюсь потихоньку, пока только Tailscale настроил и, по старой памяти, накатил zapret и podkop. До RR был некоторый опыт работы с OpenWRT на роутерах Xiaomi AX3000T и NanoPI R3S.

---

**2026-04-13T22:53:44 | Сергей**
= ПРОВЕРКА DNS  (Прошивка: 24.10.2):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.3.189 | YouTube IP:  198.18.3.185

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP ENABLED AutoStart: ON | ↓11.86 MB / ↑0.45 MB
  Пинг (ya.ru via awg10): 100.856 / 101.518 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200 OK) [tlsv1.3] [try: 2]
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:     127.0.0.1:53
    Name:       youtube.com        Address: 198.18.3.185
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ
  ruantiblock     | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Внутреннее пересечение в podkop:
    podkop                    : Youtube_Discord (Условия: default)
    podkop                    : Youtube_Discord (Условия: default)
    Домены: facebook.com whatsapp.com 

  podkop    Youtube_Discord (vpn): youtube,discord,telegram,!!!_block
  podkop           main (prx out): geoblock,!!!_block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: (doh) 9.9.9.9 / 8.8.8.8
  Версия podkop: v0.7.10
  Предупреждение: DNS и DHCP, Строгий порядок активен!

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 | uptime: 20 days | (Прошивка: 24.10.2)
  CPU: 0.31 | RAM: 36% | NAND: 32% занято / 48.7M доступно
  0 3 */3 * * /usr/bin/ruantiblock update
  13 9 * * * /usr/bin/podkop list_update
  !!!_WatchDoc установлен

---

**2026-04-13T23:00:08 | Igor**
что делать если при запуске тг без впн он не работает а подкоп пишет это:
Podkop Error
Mon Apr 13 22:55:26 2026 user.notice podkop: [error] Download https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_cidr_ipv4.txt list failed

Podkop Error
Mon Apr 13 22:55:20 2026 user.notice podkop: [error] Download telegram list failed

Podkop Error
Mon Apr 13 22:55:13 2026 user.notice podkop: [error] Download discord list failed

Podkop Error
Mon Apr 13 22:55:06 2026 user.notice podkop: [error] Download twitter list failed

---

**2026-04-13T23:48:09 | Sharky**
Вот тут только один в настройках. Мне нужно вторую сеть так же обрабатывать. Podkop имел такие настройки

---

**2026-04-14T01:26:08 | Артем Федоренко**
на телефоне через этот же vpn даже в белых списках все работает,а в podkop настроить не могу, опять бошка пухнет уже

---

**2026-04-14T05:37:34 | Routerich**
Здравствуйте.
Если у вас есть какие-то проблемы, или что-то такое, что не можете запустить/сделать на Podkop есть смысл переходить, а если и так работает и устраивает все, то нет.

---

**2026-04-14T09:36:38 | Routerich**
обновить opera-proxy через пакеты
поменять в настройках Podkop DNS-сервер на 9.9.9.9

---

**2026-04-14T09:37:04 | Routerich**
https://podkop.net/docs/install/#avtomaticheskaya-ustanovka-i-obnovlenie

---

**2026-04-14T09:37:55 | Routerich**
Здравствуйте.
а если перезапустить Podkop?

---

**2026-04-14T10:54:40 | Егор**
Ребят в целом для работы телеги в т.ч. на Андройде лучше серчить стратегии для Запрета или zeroblock/podkop мучать? Сейчас на Zeroblock, десктоп работает норм а вот на телефоне борода

---

**2026-04-14T11:03:26 | Евгений**
перестал работать ютуб, запустил скрипт 5 (помоему он быстро установился, минуты за 2) ютуб так и не заработал, в подкопе вижу такое сообщение
Podkop Error
Tue Apr 14 14:59:30 2026 user.notice podkop: [fatal] Invalid service in community lists: yotube. Check config and LuCI cache. Aborted.

перевод - Ошибка Podkop Вт 14 апр 14:59:30 2026 user.notice podkop: [fatal] Недопустимая служба в списках сообщества: yotube. Проверьте конфигурацию и кэш LuCI. Прервано.

как Исправить?

---

**2026-04-14T11:23:16 | Евгений**
не знаю что мне помогло, но сделал ваш вариант 2
и по совету ИИ
Исправьте опечатку: проверьте файл конфигурации Podkop (обычно он находится в /etc/config/podkop или доступен через интерфейс LuCI) на наличие в списках упоминаний "yotube" и замените его на youtube.
удалил секцию с названием "yotube" и в выпадающем списке выбрал "youtube"

---

**2026-04-14T11:40:27 | Artem Mayorov**
Здравствуйте! Подскажите пожалуйста, российские сервисы ругаются на ВПН, и как будто то же ВК видео идет через подкоп, потому что медленно грузит.
Жалоб больше нет, кроме не работающего ТГ.
Лог некого скрипта прикладываю.
= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.192 | YouTube IP:  142.251.110.93

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓0.00 MB / ↑0.22 MB
  Пинг (ya.ru via awg10): 139.761 / 1139.234 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop zapret2 opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН  !!!_ОПЕРА ЗАБЛОКИРОВАЛА РОССИЮ_!!! 
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200 OK) [tlsv1.3] [try: 1]
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:     127.0.0.1:53
    Name:       youtube.com        Address: 142.251.110.93
    Name:       youtube.com        Address: 142.251.110.136
    Name:       youtube.com        Address: 142.251.110.190
    Name:       youtube.com        Address: 142.251.110.91
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | RUNNING                        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop        Discord (prx out): telegram,discord
  podkop           main (prx out): !_cloudflare,google_ai,google_play,hodca,meta,!_russia_outside,geoblock
  podkop DNS/Bootstrap DNS: (doh) 9.9.9.9 / 9.9.9.9
  podkop юзерсписки: !!!_amazonaws.com → Discord, main
  Версия podkop: v0.7.10
  Предупреждение: DNS и DHCP, Строгий порядок активен!

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.93 | RAM: 23% | NAND: 28% занято / 47.8M доступно
  0 4 * * * service zapret restart
  13 9 * * * /usr/bin/podkop list_update

---

**2026-04-14T12:17:05 | Artem Mayorov**
Анализ запущен: 2026-04-14 12:15:34
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.192 | YouTube IP:  142.251.13.136

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP ENABLED AutoStart: ON | ↓0.00 MB / ↑0.22 MB
  Пинг (ya.ru via awg10): 649.077 / 3106.550 ms (0 из 10 потеряно)
  Программы в автозапуске: podkop zapret2 opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200 OK) [tlsv1.3] [try: 3]

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop        Discord (prx out): telegram,discord
  podkop           main (prx out): !_cloudflare,google_ai,google_play,hodca,meta,geoblock
  podkop DNS/Bootstrap DNS: (doh) 9.9.9.9 / 9.9.9.9
  podkop юзерсписки: !!!_amazonaws.com → Discord, main
  Версия podkop: v0.7.10
  Предупреждение: DNS и DHCP, Строгий порядок активен!

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 | uptime: 11:28 | (Прошивка: 24.10.4)
  CPU: 0.39 | RAM: 25% | NAND: 28% занято / 47.7M доступно
  0 4 * * * service zapret restart
  13 9 * * * /usr/bin/podkop list_update

---

**2026-04-14T12:19:01 | Вячес**
Добрый день, пропала секция с прокси.Так и должно быть? геоблок не работает. накатывал 5 скрипт с полным сбросом настроек. Podkop
v0.7.10
Luci App
v0.7.10
Sing-box
1.12.22

---

**2026-04-14T12:20:19 | Routerich**
Здравствуйте.
установку пакетов пропускаем
https://podkop.net/docs/tunnels/awg_settings/#o-pravilah-faervola

---

**2026-04-14T12:29:05 | Kiss_My_Axe**
= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop        Discord (prx out): telegram,discord
  podkop           main (prx out): !_cloudflare,google_ai,google_play,hodca,meta,geoblock
Открыть секцию Дискорд.
Выбрать канал VPN
Выбрать интерфейс awg10

Сохранить, Применить.

---

**2026-04-14T13:09:50 | Routerich**
так же добавлять как и в Podkop

---

**2026-04-14T16:09:42 | Oleg Shmyrin**
А куда копнуть если вот такие пироги в podkop ?

---

**2026-04-14T17:13:02 | Oleg Shmyrin**
Не, там все  по-умолчанию после установки podkop ничего не менялось

---

**2026-04-14T17:24:26 | Олег Михайлович**
еще небольшой вопрос, ничего не менял, установлено все только что, откуда пересечение podkop|zapret, но все вроде работает

---

**2026-04-14T17:34:38 | Artem**
А подскажите как починить телеграм? Перестал работать через список podkop

---

**2026-04-14T17:36:11 | Oleg Shmyrin**
А еще вопрос, подниму я VLESS на VPSке и поставлю xray-core на роутере, и натравилю на сервер, что в podkop добавить что бы он использовал VLESS ? Поменять в настройках соединения   "server_port": xray_core_PORT ? И в чем тогда смысл второй секции YOUTUBE_DISCORD ?

---

**2026-04-14T18:16:55 | Routerich**
Система - автозапуск - podkop - нажмите на включено и на стоп. Перезагрузите роутер. Наблюдайте без обходов, будут ли отвалы. По логам у вас подкопу плохо становится, и начинает нагружать систему

---

**2026-04-14T18:29:18 | Routerich**
Здравствуйте.
Ставит Podkop, без выбора.

---

**2026-04-14T19:44:45 | Alex_Jester**
До установки Зероблока устанавливали Скрипт 5 или Podkop?

---

**2026-04-14T19:50:37 | Evgeniy**
Подскажите, плиз, для вывода телефона напрямую , мимо обходов, в интернет достаточно будет присвоить постоянный ip телефону и вписать этот ip в "Исключённые из маршрутизации IP-адреса" в настройках podkop? Или что-то ещё сделать?

---

**2026-04-14T20:24:32 | Anna Bagler**
Конфигурацию у main менять в URL и вставлять свой vless. Или создавать свой интерфейс и использовать его. 
podkop.net Секции.

---

**2026-04-14T22:02:28 | Ivan Egorov**
Всем привет! Большое спасибо всем за ответы и подсказку по pbr. Всё сработало!

Решил двигаться дальше: хочу настроить OpenVPN сервер на роутере, таким образом, чтобы подключенные клиенты (условно мой телефон) получали интернет от домашнего провайдера, а два списка из podkop не знали границ )) Т.е. чтобы мой телефон (с мобильного оператора) после подключения OpenVPN клиентом к OpenVPN серверу на роутере, работал так же, как и находясь в домашней сети.

---

**2026-04-14T23:01:36 | Igor**
Посмотрел - стоит podkop v0.7.10, устаревший. Имеет смысл обновить, это вообще влияет на что-нибудь?

---

**2026-04-14T23:03:56 | Мудрикув Владимир**
Всем привет. 

Нужна помощь. 

Есть два модема(RouterRich и Asus AX4200) с openWRT. На обоих стоит podkop. Но через один модем есть доступ к tiktok, а через другой модем доступа нет. 

Podkop настроен одинаково. Включены списки Russia Inside. 

Не пойму куда копать.

P.S. через RouterRich доступ к TikTok имеется.

---

**2026-04-15T03:44:31 | T-hon**
Всем привет, перестал работать телеграмм даже в вебе, чатГПТ, ютуб
В чём может быть проблема?
Команда nslookup fakeip.podkop.fyi выполняется неверно, так как адрес не соответствует диапазону 198.18.0.0/15

Также команда curl -v https://fakeip.podkop.fyi/check работает неверно так как {"fakeip": false,

---

**2026-04-15T06:22:38 | Routerich**
Здравствуйте.
Он его учитывать не будет, и возможно будут проблемы
Так что лучше его остановить перед запуском, потом убрать из Podkop YouTube или остановить и выключить автозапуск Zapret.
А после уже запустить Zapret2.
Но это случай если у вас zapret2 для ютуба

---

**2026-04-15T06:23:04 | Routerich**
Здравствуйте.
https://podkop.net/docs/tunnels/awg_settings/#o-pravilah-faervola

---

**2026-04-15T06:41:55 | Routerich**
Здравствуйте.
не обзяательно.
для работы телеграмма через Zapret2 вам придётся подбирать под него стратегию и удалять список Telegram из Podkop

---

**2026-04-15T07:03:10 | Сергей**
1. арендовал сервер
2. на телефон поставил AmneziaVPN
3. в Self-hosted настроил тунель , на телефоне  все работает!
4. На телефоне создал файлик .conf
5. на ПК установил AmneziaVPN   закинул в него  amnezia_for_awg.conf , все работает.
6. На роутере  создал интерфейс awg0 по инструкции  с https://podkop.net/ 
7. Забросил в интерфейс awg0  файлик  .conf
8. значения H1 H2 H3 H4  не правильные и помечены  красным . 
в конфиге они  такие  H1 = 310878647-1654349467 .
 Пытался   указывать целые  значения , не работает.
9. В общем  в интерфейсе Получено (Rx): 0 B (0 Пакетов.) , ничего не работает . 
10. Где  допустил ошибку ?

---

**2026-04-15T07:07:06 | VK11**
Добрый день. Имеется в наличии vless ключ с опциями Authentication ML-KEM-768 который работает в клиенте v2raytun на смартфоне, но не работает в podkop + sing-box. вопрос собственно будет ли это работать на zeroblock или никаких вариантов нет?

---

**2026-04-15T07:30:33 | Routerich**
Здравствуйте.
а если остановить Podkop то заходит на сайт?

---

**2026-04-15T07:49:58 | Routerich**
Здравствуйте.
для начала обновите opera-proxy через система->пакеты
потом в настройках Podkop смените DNS сервер на 9.9.9.9
а по Youtube работать должен, интерфейс awg10 жив.

---

**2026-04-15T07:57:52 | Routerich**
ага, значит он в каком списке Podkop висит, поэтому и не открывается.

---

**2026-04-15T08:13:45 | Routerich**
в настройках Podkop уберите/поставьте галочку скачивать списки через Proxy/VPN

---

**2026-04-15T08:20:31 | Routerich**
убирайте список geoblock он там находится
https://github.com/itdoginfo/allow-domains/blob/main/Categories/geoblock.lst

тут либо его форкать, этот список и добавлять его если он вам нужен либо юзать секцию в Podkop "exclusion"

---

**2026-04-15T08:24:30 | Routerich**
подождите, у вас не работает секция main, поэтому и не работает 4pda
обновите opera-proxy через система->пакеты
в настройках Podkop смените DNS на 9.9.9.9
и снова диагностику сделайте

---

**2026-04-15T09:32:27 | Routerich**
Здравствуйте.
https://podkop.net/docs/sections/

---

**2026-04-15T11:41:01 | Routerich**
смените DNS сервер в Podkop на 9.9.9.9
и потом снова диагностику запустите в Podkop

---

**2026-04-15T12:21:54 | Routerich**
Здравствуйте.
https://podkop.net/docs/sections/

---

**2026-04-15T12:44:19 | Routerich**
Здравствуйте.
в настройках Podkop снять/поставить галочку на скачивать списки через Proxy, сохранить и применить и смотреть

---

**2026-04-15T12:50:04 | Routerich**
ну кроме пересечения zapret и Podkop я проблем не вижу.
стопайте и отключайте автозапуск zapret и проверьте
потом можно стопнуть Podkop и проверить работу сервисов будут ли ругаться

---

**2026-04-15T12:52:49 | Routerich**
а Podkop/zeroblock/zapret что-то такое используете?

---

**2026-04-15T14:26:49 | Александр**
Podkop который)

---

**2026-04-15T15:26:59 | Dark Ghost**
Там же, где всегда: https://podkop.net/

---

**2026-04-15T20:02:28 | Routerich**
Здравствуйте.
Обновите Opera-proxy, смените dns в Podkop на 9.9.9.9
На счёт телеги на бесплатных решениях она отвалилась, нужно свои решения добавлять платные/бесплатные

---

**2026-04-15T20:26:37 | .Vadim**
Всем привет! Не обновляются пакеты, вылазит ошибка

Невозможно выполнить команду opkg update: SyntaxError: Unexpected end of JSON input

Так же не устанавливается podkop

Куда копать? Роутер только включил

---

**2026-04-15T20:30:15 | Routerich**
Смените dns на 9.9.9.9 в настройках Podkop

---

**2026-04-15T20:47:29 | Николай**
Может статья с сайта podkop поможет?
https://podkop.net/docs/faq/

Там несколько пунктов предлагают проверить.

---

**2026-04-15T21:46:50 | Anton Лопата**
Подскажите, а можно разделение трафика сделать как в podkop там какие то списки были, тут что то подобное не вижу, а то некоторые ру ресурсы не хотят через вифи грузиться

---

**2026-04-15T21:50:36 | Your_secret_friend**
Добрый вечер! Подскажите, может кто-то сталкивался с проблемой про настройке amneziaWG+podkop… 

Туннель работает, забирает весь трафик. В настройках подкопа убрал список сообщества и указал нужные мне домены, как телеграм, вотсапп, инста и тд, всё сохранил и перезапустил, но трафик так и уходит весь через amneziaWG:(

---

**2026-04-15T21:54:46 | Your_secret_friend**
Need help! 

Добрый вечер! Подскажите, может кто-то сталкивался с проблемой про настройке amneziaWG+podkop… 

Туннель работает, забирает весь трафик. В настройках подкопа убрал список сообщества и указал нужные мне домены, как телеграм, вотсапп, инста и тд, всё сохранил и перезапустил, но трафик так и уходит весь через amneziaWG:(

При диагностике подкопа - всё зеленое, кроме самой последней позиции - Прокси-трафик не маршрутизируется через FakeIP.

---

**2026-04-15T22:10:21 | Anna Bagler**
Если у вас zeroblock, есть полный мануал по нему. Если podkop, то podkop.net Ceкции. Как развернуть/купить готовое подскажет интернет.

---

**2026-04-15T23:25:53 | Alexader**
Доброго всем вечерка.
Камрады, подскажите, может кто сталкивался или киньте ссылкой. 
На полгода выпал из темы.

1. Есть Я-х.ТВ, есть yt, есть RR со скриптом №5. 
Раньше была связка podkop+zapret. Вчера сделал чистую установку прошивки с полным сбросом + скрипт №5.
YouTube работает везде (ноут, планет, телефоны), кроме ТВ. Раньше грешил, что какие-то списки из подкопа пересекаются с запретом, поэтому на ТВ проблема. Но сейчас остался только podkop и ситуация такая-же.  

2. Что за чудесный скрипт, скрины которого часто пуляют в чат, в котором идет проверка DNS, доступов, служб и пересечения списков?

3. Обновлять opkg пакеты до последней версии сейчас безопасно, или в прошивке до сих пор все жестко привязано?

---

**2026-04-15T23:36:56 | Denis**
Свой vps, podkop на роутере, в списке есть в т.ч. Telegram, но пока на телефоне не подключу впн с того же vps, телега не работает.

---

**2026-04-16T05:03:55 | Routerich**
Здравствуйте.
Добавить свой Vpn в Podkop, потом выбрать в списках YouTube, Telegram и он будет только по этим спискам работать, остальные трогать не будет.

---

**2026-04-16T05:07:32 | Routerich**
Остановите Podkop и проверяйте, будут ли тормоза

---

**2026-04-16T05:42:44 | Routerich**
Ну значит не с Podkop связано.

---

**2026-04-16T06:05:37 | Routerich**
Это с запущенным Podkop?

---

**2026-04-16T06:09:27 | Routerich**
Как вариант пробуйте сменить DNS в настройках Podkop и смотреть как будет

---

**2026-04-16T07:18:44 | Evgen**
Понял попробую, еще подскажите есть у меня ключ Vless и амнезии, если получится до репозиториев достучаться, что лучше будет поставить podkop или zeroblock?

---

**2026-04-16T08:39:58 | Routerich**
ага, тогда диагностику Podkop/zeroblock пришлите

---

**2026-04-16T08:46:34 | Routerich**
обновите opera-proxy, потом в настройках Podkop измените DNS сервер на 9.9.9.9

---

**2026-04-16T08:50:56 | Routerich**
стопните Podkop и снова пробуйте

---

**2026-04-16T08:52:36 | Routerich**
https://docs.routerich.ru/ru/remote
Раздел
Настройка Podkop и ZeroBlock (Subnet Router) для маршрутизации

---

**2026-04-16T08:54:06 | Routerich**
в настройках Podkop уберите галочку скачивать списки через Proxy

---

**2026-04-16T09:05:19 | Никита Николаевич**
Добрый день,перестал работать podkop с любой vless конфигурацией со списком  доменов YouTube

---

**2026-04-16T09:07:13 | Никита Николаевич**
Ютуб перестал работать через podkop )

---

**2026-04-16T09:14:51 | Routerich**
которые красными светятся, что не удалось скачать список по ссылке, которые в Podkop выскакивают

---

**2026-04-16T09:50:31 | Routerich**
ага, еще надо либо обновить Podkop либо убрать список cdn_cludflare так как петля возникает, на старой версии Podkop

---

**2026-04-16T09:57:00 | Routerich**
https://podkop.net/docs/install/#avtomaticheskaya-ustanovka-i-obnovlenie

---

**2026-04-16T10:23:35 | Routerich**
Переходить на платные решения, добавлять их в Podkop, сейчас с бесплатными решениями все тяжко.

---

**2026-04-16T11:38:22 | Владислав**
sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)


Вот так обновил

---

**2026-04-16T11:41:07 | Архипов Кирилл Александрович**
Зайдите в систему пакеты, нажмите обновить списки, после чего в фильтр ввидите podkop, скрин сюда. У вас как будто интерфейса нет

А вообще советую ЗБ поставить...

---

**2026-04-16T15:01:36 | Vitaly**
у меня Podkop. и то же выбран только не messengers, а прям Telegram в секции YOUTUBE_DISCORD

---

**2026-04-16T16:04:56 | Helgi M**
Здравствуйте! Вчера был Youtube, X, Gemini на всех устройствах, Telegram не было нигде. Днём всё пропало после "плановых работ по повышению качества работы домашнего интернета" (от Билайна смс приходило). Стоит Podkop. Перезапустил 5-й скрипт, в секции MAIN - тип подключения VPN, сетевой интерфейс - awg10, скачивать списки через Proxy/VPN - галочку убрал. На всех устройствах заработали Youtube, X, на компе появился Telegram.  Gemini нет нигде 😥 Как можно восстановить  Gemini? Подскажите пожалуйста.

---

**2026-04-16T16:18:41 | Helgi M**
Секцию с Proxy здесь добавлять, в настройках Podkop?

---

**2026-04-16T18:27:40 | Dmitry**
Подумываю перебраться с podkopa на zeroblock+zapret2 случайно нет скрипта для автоматической установки и настройки по типу скрипта N5

---

**2026-04-16T19:57:11 | Anna Bagler**
Тогда изучайте небесплатные варианты, которые можно использовать в zeroblock/podkop.

---

**2026-04-16T21:29:55 | Makz Chernov**
Добрый вечер! Подскажите сегодня что-то случилось ввели какие то новые блокировки? Перестал работать podkop.

---

**2026-04-17T01:28:08 | Anna Bagler**
Если у вас подкоп был, то podkop.net Секции, там есть поддерживаемые протоколы и конфигурации.

---

**2026-04-17T05:36:50 | Routerich**
Здравствуйте.
В настройках Podkop поставьте /снимите галочку на скачивать списки через Proxy

---

**2026-04-17T06:40:14 | Anna Bagler**
Zero или podkop?

---

**2026-04-17T07:06:57 | Anna Bagler**
Ставить надо на чистый, а не рядом с podkop. Свой vless или все же интерфейс для awg создавали?

---

**2026-04-17T07:21:49 | Routerich**
вам надо определится либо Podkop, либо ZeroBlock (лучше его)

---

**2026-04-17T07:47:06 | Maksim**
День добрый.
Может кто направит в нужное русло: не хотят устройства сети tailscale использовать exit node как dns сервер. Соответственно с podkop работают  неполноценно: все что в podkop_subnets указывается из общедоступных списков - уходит в vpn (например telegram), все остальное (например списки geoblock или вручную добавленный ifconfig.me) идет мимо. 
Magicdns в админке выключен, Nameserver с адресом роутера добавлен. Флаг --netfilter-mode=off тоже прописан.
Скрин диагностики прилагаю.

Может конечно я зря tailscale виню, а дело в podkop (хотя в локальной сети все работает как должно).

---

**2026-04-17T08:52:32 | Remember**
Что с этим сделать можно? Использую podkop

---

**2026-04-17T10:24:43 | Routerich**
Службы->Podkop - >Диагностика->Запустить диагностику

---

**2026-04-17T10:33:39 | Routerich**
Здравствуйте.
Обновить opera-proxy
Затем в настройках Podkop сервер dns сменить на 9.9.9.9

---

**2026-04-17T11:02:03 | The Wisest**
Здравствуйте!
Хотел бы узнать как установить на него Podkop

---

**2026-04-17T11:03:36 | Routerich**
Но лучше смотрите в сторону Zeroblock, вместо Podkop

---

**2026-04-17T12:10:45 | Виталий**
Здравствуйте.Я новичек в данной теме про routerich.Дома роутер AX3000T,установлен podkop,всё работает.Данный роутер Routerich,чем лучше выше упомянутого роутера?Стоит его рассматривать на замену моему?

---

**2026-04-17T12:25:03 | Routerich**
Здравствуйте.
Перезапустите Podkop

---

**2026-04-17T12:26:33 | Routerich**
Затем покажите диагностику Podkop

---

**2026-04-17T12:32:01 | Routerich**
Галочку в настройках Podkop уберите/поставьте галочку на скачивать списки через Proxy и снова диагностику

---

**2026-04-17T12:43:39 | ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ**
sh <(wget -O - https://raw.githubusercontent.com/itdoginfo/podkop/refs/heads/main/install.sh)
Эта команда?

---

**2026-04-17T12:44:19 | Sergey Lonchakov**
Верно. Так и поступил в podkop. Но не работает к сожалению.

---

**2026-04-17T12:44:53 | Routerich**
Это команда для установки/обновления Podkop, нет.

---

**2026-04-17T17:16:43 | Anna Bagler**
Бесплатные варианты в podkop не работают, надо свое.

---

**2026-04-17T17:52:43 | Виталий (alt+255)**
podkop уже завезли туда ?

---

**2026-04-17T20:28:29 | Anna Bagler**
Vless, awg и прочее. podkop.net Секции - можете посмотреть, что поддерживает подкоп. Можете со сбросом перейти на zeroblock, в нем есть поддержка подписок.

---

**2026-04-17T21:34:27 | Maksim**
Решилось созданием симлинка
rm -f /etc/resolv.conf
ln -s /tmp/resolv.conf /etc/resolv.conf

Теперь DNS роутера проходит через sing-box
root@OpenWrt:~# ls -l /etc/resolv.conf
lrwxrwxrwx    1 root     root            16 Apr 17 17:14 /etc/resolv.conf -> /tmp/resolv.conf

root@OpenWrt:~# cat /etc/resolv.conf
search lan
nameserver 127.0.0.1
nameserver ::1

root@OpenWrt:~# nslookup fakeip.podkop.fyi
Server:         127.0.0.1
Address:        127.0.0.1:53

Name:   fakeip.podkop.fyi
Address: 198.18.0.5

В кабинете MagicDNS и Override Local DNS выключены.
Указан один nameserver - ip роутера 
192.168.3.1

Теперь dns запросы клиентов tailscale корректно обрабатываются на стороне exit node при включенной опции Use Tailscale DNS Settings

---

**2026-04-17T21:56:26 | Дмитрий Шаповалов**
почему gemini, supercell и прочие могут палить рф локацию?
брал скрипт 5, заменил awg10 на свой awg30, в зону awg добавил.
в podkop стандартные настройки, только докинул список пользовательских доменов и подсетей.

---

**2026-04-18T05:17:46 | а к**
Установил vless в podkop. Скажите пожалуйста все ли в порядке.

---

**2026-04-18T09:22:48 | Apple_Butter**
тип пользовательского списка подсетей -> Текстовый список (podkop)

---

**2026-04-18T10:05:14 | Alexey A**
Если у меня установлен podkop, могу ли я установить Zero block, пользоваться зеро блоком, при этом подкоп просто остановить и не удалять? Будет ли так работать

---

**2026-04-18T10:20:18 | Роман**
А на данный момент как дела у zeroblock? Сыроват или уже лучше Podkop'а?

---

**2026-04-18T10:33:32 | Gomer Simpson**
Замечательная штука. Употребляет все подписки и ссылки, сам поднимает отвалившиеся интерфейсы, умеет исключать ненужные подписки (RU, например) из общего списка. Очень много плюсов, по сравнению с podkop.

---

**2026-04-18T14:57:10 | Aziz**
Добрый день. 
Хочу изучить Vless/amnezia или аналог. Чтоб работал прежде всего тг. 
Можете ссылку дать на изучение материала?
Сейчас почти все работает через podkop.
Чтоб vless/amnesia и т.п работало, достаточно подкоп или нужен зероблок?

---

**2026-04-18T15:35:34 | Вячеслав**
Сделал обновление прошивки, слетел Podkop, opkg update не работает из-за ошибки сети, интернет есть. Какое зеркало можно поставить ?

---

**2026-04-18T17:18:24 | Routerich**
Гуглите генератор warp в интернете - получаете конфиг - дальше по инструкции https://podkop.net/docs/tunnels/awg_settings/ пункт установка пакетов пропустить

---

**2026-04-18T19:49:08 | Sharky**
Добрый день. На новый роутер не могу поставить скриптом - дает ошибку скачивания пакетов podkop
По ссылке, которую пытается качать с гитхаб ошибка 404

---

**2026-04-18T20:37:35 | Игорь**
Вам даже не надо ничего самому прошивать - прошивка уже стоит.
Ставим zapret2, podkop и wireguard.

Арендуем VPS с предустановленным 3x-ui, настраиваем, получаем ссылку, копируем в подкоп и всё работает. Сколько можно...

---

**2026-04-18T22:26:58 | Routerich**
А где тут речь про скрипт 5? Я не вижу например, по вашим словам у вас проблема с установкой podkop, а не скрипта 5

---

**2026-04-19T10:12:13 | e k**
Подскажите плиз, какие на данный момент современные\рабочие решения для гибкой настройки впн, сейчас использую точечную маркировку с getdomains, настроенную сколько-то лет назад, всё работает но не гладко, нужно чтобы для одних устройств можно было весь трафик через впн пускать, а для других только частично (для заблокированных ресурсов),  в идеале для selfhosted амнезии, но не обязательно. Есть ли сейчас что-то что позволяет подобное настроить, podkop какой может?

---

**2026-04-19T10:25:40 | Владимир**
Подскажите, можно ли как-то сделать что бы определенный локальный ip проходил отдельно без сервиса podkop(он у меня настроен через ключ влесс)

Ситуация такая что не могу свой 3д принтер bambulab a1mini подключить к компьютеру по локальной сети.

---

**2026-04-19T10:46:10 | vladimir**
Доброго дня. Подскажите в чем может быть проблема? В секции main Podkop-a свой vless-ключ

---

**2026-04-19T11:01:12 | Sergey Lonchakov**
А что лучше zeroblock или podkop?

---

**2026-04-19T11:02:10 | vladimir**
--- НАЧАЛО (скрин отсюда и до слова КОНЕЦ!) --- = 
ПРОВЕРКА DNS  (Прошивка: 24.10.5):  
DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359  
Facebook IP:  198.18.1.203 | YouTube IP:  198.18.0.90= 

ИНТЕРФЕЙС awg10 (ДЕТАЛИ):  
Статус: UP EN AS:ON | ↓10.68 MB / ↑0.28 MB | ya.ru>awg10: 34.998 / 37.996 ms (0 из 10)  
Программы в автозапуске: podkop opera-proxy= 

ПРОВЕРКА ДОСТУПОВ/ИНТЕРФЕЙСОВ (PROTON.ME)  
✅ VLESS+TCP                  xxxx    274ms [ main ]  
✅ vpn awg10                  1280    308ms [ Youtube_Discord ]  
Запускаем остановленные службы, ожидайте...Start podkopse
rvice_triggers start= 

СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):  
podkop          | RUNNING                        | РАЗРЕШЁН  
sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ  
zapret          | STOPPED                        | ОТКЛ  
opera-proxy     | RUNNING                        | РАЗРЕШЁН  
youtubeUnblock  | STOPPED                        | ОТКЛ= 

ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:  
podkop    Youtube_Discord (vpn): discord  
podkop           main (prx url): geoblock,block,meta,hdrezka,tiktok,google_ai,telegram,youtube,porn  
podkop DNS/Bootstrap DNS: (doh) 8.8.8.8 / 8.8.8.8  
podkop ❌ Sing-box does NOT work with FakeIP: ;; communications error to 127.0.0.42#53: connection refused  
Версия podkop: v0.7.14= 

СИСТЕМНЫЕ РЕСУРСЫ:  
LAN IP: 192.168.1.1 | uptime: 1 day | (Прошивка: 24.10.5)  
CPU: 0.03 | RAM: 23% | NAND: 27% занято / 49.4M доступно  
13 9 * * * /usr/bin/podkop list_update  
--- КОНЕЦ! ---

---

**2026-04-19T11:13:39 | Максим**
= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус: UP EN AS:ON | ↓0.00 MB / ↑0.01 MB | ya.ru > awg10: ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (77.88.44.242): 56 data bytes
  Программы в автозапуске: podkop opera-proxy

= ПРОВЕРКА ДОСТУПОВ/ИНТЕРФЕЙСОВ (PROTON.ME)
  ❌ vpn awg10                  1280    ---ms [ Youtube_Discord ]
  ✅ Outb HTTP local:18080      xxxx   4387ms [ main ]
  Запускаем остановленные службы, ожидайте...Start podkop
service_triggers start

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop    Youtube_Discord (vpn): !!!_russia_inside,telegram
  podkop           main (prx out): block,!!!_youtube,meta,tiktok
  podkop DNS/Bootstrap DNS: (doh) 9.9.9.9 / 8.8.8.8
  Версия podkop: v0.7.14
  !!!_SI: "Не создавать маршруты" не установлен в 1

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.2.1 | uptime: 11:49 | (Прошивка: 24.10.5)
  CPU: 0.32 | RAM: 25% | NAND: 26% занято / 49.9M доступно
  13 9 * * * /usr/bin/podkop list_update
  --- КОНЕЦ! --- Всем привет поскажите опять проблемы я уже и свой впн прикрутил так еще хуже стало

---

**2026-04-19T12:14:11 | Sergey Lonchakov**
Господа, привет. В чате не нашёл ответа. Подскажите, может кто сталкивался?
На ноутбуке по wifi работает почти всё - ютуб, телеграм, chat gpt. Но на смартфонах, ничего не работает (разные андройды и айфоны).

Routerich AX3000 v1. Поставлен последний podkop на последнюю прошивку - RouteRich 24.10.5

---

**2026-04-19T14:03:08 | Анатолий Шарков**
Подскажите, пожалуйста:

Планирую использовать внешний прокси (VLESS) через Podkop (секции / ZeroBlock).

Текущая конфигурация:
— RouteRich 24.10.5 (RR-3.9.0)
— Podkop v0.7.10 (помечен как устаревший)
— sing-box 1.12.17

Вопросы:

1. Достаточно ли этой версии Podkop для работы с VLESS?
2. Есть ли рекомендуемая версия Podkop и ПРОШИВКИ под такую схему?
3. Есть ли критичные изменения в новых версиях для секций / outbound?

И как лучше сделать — сначала обновиться, а потом настраивать, или можно сначала всё настроить на текущей версии?

---

**2026-04-19T14:06:51 | Влад**
Добрый день!
Обрисую всю схему, потому что не знаю, где затык - я в этом совсем чайник.
GPON от МГТС - роутер InnboxG93. В бридж не переводится, поэтому DMZ. Вчера купил статический IP.
Routerich в WAN из LANа InnboxG93.
VPS в Финляндии с XRay, на Routerich'е Podkop с ключом от XRay, Russia inside + какие-то свои списки. YoutubeUnblock с Podkop'ом не подружился, поэтому YoutubeUnblock отключил.
Подключаюсь к Routerich по вайфаю, всё работает так, как ожидаю - неположенное через ВПН, остальное напрямую.
В частности работают ТГ, вотсап, Youtube, ChatGPT, X, Instagramm - это из ихних, и Госуслуги и прочие Озоны - из отечественных.
2ip.ru видит наш IP, а какой-нить thesafety.us - финский IP.

Вне дома на всяких устройствах AmneziaVPN c ключами в Финляндию. Работает, но или включать-выключать VPN, или везде настраивать split tunneling - такое себе.
Решил на всякие устройства сделать туннель до дома, чтоб они ходили в интернет через вот это описанное выше домашнее хозяйство.
На Routerich запустил AmneziaWG, на устройства - AmneziaVPN с ключом от этой домашней AmneziaWG.
Теперь на устройствах (не важно, через мобильный интернет или какой-нить вайфай - InnboxG93 или Routerich или ещё какой) отечественное открывается (по крайней мере то, что проверял), а неположенное - абы как. ТГ работает, вотсап нет, Youtube не работает, ChatGPT работает, X не работает, Instagramm работает.
При этом если в настройках Podkop в "Полностью маршрутизированные IP-адреса" укажу туннельные 10.10.0.0/24, то всё с устройств пойдёт через Финляндию - будет открываться всё тамошее, 2ip.ru покажет Финляндию, Озон начнёт ругаться на VPN...
Поскольку чайник, то настраивал всё по информации из интернета и расспрашивая chatgpt, но сейчас chatgpt уже, похоже, сдулся, и со словами "вот щас точно всё заработает!" предлагает всякую разнообразную хрень.

Не понимаю, куда копать, чтоб вот это, пришедшее на Routerich через AmneziaWG работало так же, как пришедшее на Routerich через его вайфай. А сейчас и не работает, и не "не работает".

---

**2026-04-19T15:54:19 | Влад**
Приветствую всех!
Сорри за непрофессиональное объяснение, но суть, думаю, будет понятна. :)

1. телефон > вайфай на Routerich > Podkop (Списки сообщества Russia inside) > VPS > весь интернет. Работает ожидаемо. Открываются наши и все зарубежные сайты из Russia inside.

2. телефон > ВПН AmneziaWG на Routerich > Podkop (Полностью маршрутизированные IP) > VPS > весь интернет. Работает ожидаемо. Всё уходит в туннель до VPS, открываются зарубежные сайты и только часть наших сайтов (озон и прочее ругается на ВПН).

3. телефон > ВПН AmneziaWG на Routerich > Podkop (Списки сообщества Russia inside) > VPS > весь интернет. Работает не так, как ожидаю. Открываются наши и только часть сайтов из Russia inside. 


Куда копать, чтоб решить п. 3 - чтоб открывалось всё наше и всё зарубежное из Russia inside? Т. е. чтоб "телефон > ВПН AmneziaWG на Routerich > Podkop" работало так же, как "телефон > вайфай на Routerich > Podkop"

---

**2026-04-19T16:42:54 | Влад**
--- НАЧАЛО (скрин отсюда и до слова КОНЕЦ!) ---
= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.0.167 | YouTube IP:  198.18.0.168
  Интерфейс awg10 не существует, или отключен.
  Программы в автозапуске: podkop

= ПРОВЕРКА ДОСТУПОВ/ИНТЕРФЕЙСОВ (PROTON.ME)
  ✅ VLESS+TCP                  xxxx    170ms [ main ]
  Запускаем остановленные службы, ожидайте...Start podkop
service_triggers start

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Внутреннее пересечение в podkop:
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    podkop                    : main (Условия: default)
    Домены: t.me teleg.xyz telegram.ai telegram.asia telegram.biz telegram.cloud telegram.cn telegram.co telegram.com telegram.de telegram.dev telegram.dog telegram.eu telegram.fr telegram.host telegram.in telegram.info telegram.io telegram.jp telegram.me telegram.net telegram.org telegram.qa telegram.ru telegram.services telegram.solutions telegram.space telegram.team telegram.tech telegram.uk telegram.us telegram.website telegram.xyz telegramapp.org telesco.pe tg.dev tg.org tgram.org torg.org

  podkop           main (prx url): !_russia_inside
  podkop DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8
  Версия podkop: v0.7.14
  !!!_AWG0: "Не создавать маршруты" не установлен в 1

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.0.1 | uptime: 11:37 | (Прошивка: 24.10.5)
  CPU: 0.00 | RAM: 22% | NAND: 32% занято / 46.1M доступно
  13 9 * * * /usr/bin/podkop list_update
  --- КОНЕЦ! ---

---

**2026-04-19T19:22:58 | Aleksandr Kuzin**
Здравствуйте, подскажите из-за чего может podkop выключаться и не включаться, если автопереподключение включено? Стоит только скрипт 5.

---

**2026-04-19T19:23:37 | Routerich**
Здравствуйте.
Диагностику покажите Podkop

---

**2026-04-19T19:26:25 | Routerich**
Перезагрузите Podkop и снова диагностику покажите

---

**2026-04-19T22:38:49 | Artem P**
Привет, по закрепам прыгать не получается, не переходит по ссылкам 
Подскажите, пожалуйста, есть ли актуальный гайд на установку утилит типа запрета?
В последний раз пользовался скриптом #5, то есть сейчас 1-ая версия zapret стоит. Также пробовал podkop 
Что сейчас разумнее поставить?

---

**2026-04-19T22:53:15 | Влад**
Если вдруг интересно, chatgpt в конечном итоге предложил решение. Добавить выделенную строку, чтоб трафик AWG маркировался как предназначенный для Podkop'а.
Буду ещё смотреть, но пока похоже, что всё заработало, как я и хотел: всякие устройства через AWG идут ко мне домой и дальше всё работает через подкоп так же, как будто я дома подключился к Routerich через вайфай.

---

**2026-04-19T23:34:58 | Виталий Исаев**
Научите, пожалуйста, как подружить Routerich и устройство на Андроид, чтобы трафик c мобильного устройства шёл на роутер, а далее в дело вступал podkop. 

На роутере поставил галочку напротив Exit Node. Но что нужно сделать в приложении Tailscale на телефоне?

---

**2026-04-19T23:49:45 | Василий aka Dem.**
Анализ запущен: 2026-04-19 20:47:30
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
  --- НАЧАЛО (скрин отсюда и до слова КОНЕЦ!) --- 
= ПРОВЕРКА DNS  (Прошивка: 24.10.6):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.0.237 | YouTube IP:  198.18.0.81

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус: DOWN EN AS:ON | ↓0.00 MB / ↑0.00 MB | ya.ru > awg10: ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (5.255.255.242): 56 data bytes
  Программы в автозапуске: podkop zapret opera-proxy youtubeUnblock

= ПРОВЕРКА ДОСТУПОВ/ИНТЕРФЕЙСОВ
  ✅ VLESS+TCP                   xxxx    372ms [ YOUTUBE_DISCORD ]
  ❌ Outb HTTP local:18080       xxxx    ---ms [ main ]

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Внутреннее пересечение в podkop:
    podkop                    : main (Дубли в "Список польз. доменов" )
    default                   :  (Дубли в "Список польз. доменов" )
    podkop                    : main (Дубли в "Список польз. доменов" )
    default                   :  (Дубли в "Список польз. доменов" )
    Домены: googlevideo.com youtube.com 

  podkop YOUTUBE_DISCORD (prx url): telegram
  podkop           main (prx out): hdrezka,!_russia_outside,discord,google_ai,google_play,meta,twitter,youtube
  podkop DNS/Bootstrap DNS: (doh) 9.9.9.9 / 9.9.9.11
  Версия podkop: v0.7.10

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.0.1 | uptime: 5 days | (Прошивка: 24.10.6)
  CPU: 0.42 | RAM: 25% | NAND: 95% занято / 1.5M доступно
  13 9 * * * /usr/bin/podkop list_update
  --- КОНЕЦ! ---

root@OpenWrt:~# [ "${___z_stat}" = "running" ] && /etc/init.d/zapret start >/dev/null
root@OpenWrt:~# [ "${___y_stat}" = "running" ] && /etc/init.d/youtubeUnblock start >/dev/null
root@OpenWrt:~# #
root@OpenWrt:~#

---

**2026-04-19T23:52:11 | Василий aka Dem.**
Package opera-proxy (1.15.1-r1) installed in root is up to date.
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: no lease, failing
Start podkop
service_triggers start
root@OpenWrt:~#

---

**2026-04-20T08:03:22 | Artem Kirillov**
Доброго времени суток. 
Уже неделю пытаюсь починить доступ к ChatGPT. Пробовал добавлять его в секции podkop - не помогает. Сейчас постарался сделать всё по инструкции, которая начинается с "ААА! Помогите ничего не работает...

---

**2026-04-20T08:09:46 | Artem Kirillov**
У меня есть платный ВПН от Happ. Я могу эту ссылку использовать в podkop? Подскажите?

---

**2026-04-20T12:56:43 | Proff-comp**
Добрых дней. Подскажите пожалуйста, хочу попробовать zeroblock, у меня стоит podkop, достаточно будет его просто удалить например через менеджер пакетов и поставить, или все же на чистый роутер нужно, и я как понял с vless он работает. Поправьте если ошибаюсь.

---

**2026-04-20T13:33:50 | Анатолий Шарков**
Добрый день.
Подскажите, какой сейчас рекомендуемый и рабочий вариант обхода блокировок?

Использовал скрипт 5 — часть сайтов перестала открываться.

Сейчас вижу варианты Podkop / Zapret / ZeroBlock — какой из них актуальный?

И нужно ли при переходе на ZeroBlock удалять Podkop (или они могут работать параллельно)?

---

**2026-04-20T14:28:53 | Kiss_My_Axe**
А вот.
https://podkop.net/docs/adguard/

---

**2026-04-20T15:28:34 | Влад**
что делать если при нажатии на диагностика в podkop не проходит проверку?

---

**2026-04-20T15:54:13 | Евгений Макаренко**
Через Podkop небыло так. Настраиваю так же. Похожие настройки.

---

**2026-04-20T19:52:38 | Vit**
Спасибо! Не так давно перешёл с podkop на zeroblock + zapret2. Часть трафика пустил через свой awg. Работает всё что нужно. Ещё раз спасибо! Ещё бы всё это на х86 поднять, вот был бы комбайн.

---

**2026-04-20T20:08:33 | Anna Bagler**
Бесплатные варианты более не работают. Свой vless или ещё что в zeroblock/podkop.

---

**2026-04-20T21:22:24 | 𝒳**
А как починить макс через вай фай если podkop стоит

---

**2026-04-20T21:32:42 | Anna Bagler**
Вам бы обновить и прошивку и podkop. А лучше zeroblock после прошивки.

---

**2026-04-20T21:40:18 | Routerich**
https://podkop.net/docs/faq/#kak-ispolzovat-warp-i-polzovatelskij-spisok-podsetej-cloudflare

---

**2026-04-20T22:21:09 | Виктор**
Анализ запущен: 2026-04-20 22:18:52
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Устанавливаем/обновляем: wget-ssl opera-proxy
Попытка обновления списка пакетов: (1/4)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Command failed: ubus call service delete { "name": "opera-proxy" } (Not found)
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Upgrading opera-proxy on root from 1.15.0-r1 to 1.15.1-r1...
Downloading https://github.com/routerich/packages.routerich/raw/24.10.5/routerich/opera-proxy_1.15.1-r1_aarch64_cortex-a53.ipk
Configuring opera-proxy.
Configuring wget-ssl.
  --- НАЧАЛО (скрин отсюда и до слова КОНЕЦ!) --- 
= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53
 | DNS Redirect: 127.0.0.42
  Facebook IP:  198.18.2.180
 | YouTube IP:  198.18.2.181
= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус: UP EN AS:ON | ↓10.70 MB / ↑0.14 MB | ya.ru
>awg10: 41.511 / 42.446 ms (0 из 10)
  Программы в автозапуске: podkop zapret opera-proxy
= ПРОВЕРКА ДОСТУПОВ/ИНТЕРФЕЙСОВ
  ✅  vpn awg10                  1280    161ms [ Youtube_Discord ]
  ✅  Outb HTTP local:18080      xxxx   2322ms [ main ]
= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  podkop          | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY PODKOP)    | ОТКЛ
  zapret          | STOPPED                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ
= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  podkop    Youtube_Discord (vpn): youtube,discord,telegram
  podkop           main (prx out): geoblock,block,meta,twitter,hdrezka,tiktok,google_ai
  podkop DNS/Bootstrap DNS: (doh) 9.9.9.9
 / 9.9.9.9
  Версия podkop: v0.7.14
= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1
 | uptime: 26 days | (Прошивка: 24.10.5)
  CPU: 0.57 | RAM: 24% | NAND: 27% занято / 49.3M доступно
  13 9 * * * /usr/bin/podkop list_update
  --- КОНЕЦ! ---
root@RouteRich:~# #

---

**2026-04-20T23:03:01 | Routerich**
podkop.net раздел установка

---

**2026-04-21T01:13:13 | Роман**
Для игры Epic Seven нужно добавить эти домены в список прользовательских доменов zeroblock/podkop. Внимание используется cloudfront!
playstove.com
onstove.com
singular.net
81plug.com
cloudfront.net
facebook.com
#games

---

