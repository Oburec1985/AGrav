# Raw Extraction: zapret

**2026-01-01T05:57:44 | Kiss_My_Axe**
Попробуйте насканить страт для запрета.
Запустить, после установки нажать 1 ввод.
Начнётся поиск. Он может быть долгим, если чо ложитесь спать.
Как закончит поиск нажмите 2 и ввод.
Будут предлагаться для проверки страты. Как зелёным напишет - запускайте на телефоне/телеке ютуб.
Не работает - ввод. Работает 1 и ввод.
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-01-01T12:24:26 | Alex EfremoFF**
С Новым годом, друзья!
Ткните носом новичка, для Трубы что лучше использовать - podkop или zapret?
Если есть ссылка на инструкцию, буду вдвойне благодарен!

---

**2026-01-01T13:05:33 | Bullet for my valentine Poison**
🎄Всех с Новым годом!🔥 Zapret2. Для телевизоров LG, Samsung и т.д. Попробуйте такой вариант: 
Создайте доп. конфиг к основному Youtube.(Настройки на скринах)
Потом нажать на blobs и выбрать blob_quic_initial_www_google_com Сохранить, применить и перезапустить Zapret2

---

**2026-01-01T13:13:44 | Vasa**
попробуйте это добавить в обход
https://github.com/GubernievS/AntiZapret-VPN/blob/main/setup/root/antizapret/download/whatsapp-ips.txt

---

**2026-01-01T13:25:53 | Vasa**
вот эти

https://github.com/GubernievS/AntiZapret-VPN/blob/main/setup/root/antizapret/download/whatsapp-ips.txt

что там по умолчанию я без понятия

---

**2026-01-01T13:46:44 | Bullet for my valentine Poison**
opt/zapret2/files/fake/quic_3.bin --lua-desync=fake:blob=quic_3  ты это имел ввиду?

---

**2026-01-01T13:56:13 | Routerich**
давай я 1 разъ поясню, а при похожих вопросах мут на подумать дам. есть основной инстанс, тот, которому ты пишешь стратегии, он помимо собственной работы поднимает скрипты, отдельными инстансами. они ничего не знают о том, что и как ты включаешь или отключаешь, они нюхают трафик на наличие пейлоад и сравнивают со своей предустановкой. opt/zapret2/files/fake/quic_3.bin вот это инициирует блоб для квика(включает его)

---

**2026-01-01T14:04:30 | Bullet for my valentine Poison**
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-01-01T15:12:00 | Михаил**
Советую zapret 2 попробовать. Версии не ниже 0.8. Тут выше ссылку давали. Там автор подбор стратегий для доступа к ресурсу сделал. У меня на ютуб десяток успешных стратегий  нашел. Теперь ютуб работает. Самые лучшие впечатления от запрета2.

---

**2026-01-01T16:48:41 | bm**
Достал из коробки и подключил
Обновил все пакеты (Начал снизу вверх)
Ребутнул (GUI с белого поменялось на синий, ок так задумано)
Стопнул и деактивировал автозагрузку ЮтубАнблок.
Установил все три пакета Zapret2
Сделал рестарт службы Zapres2.
Зашел в броузер все работает.

---

**2026-01-01T20:41:30 | Αλέξανδρος**
https://t.me/routerich/173678/418184
Такая же проблема возникла после обновления zapret2 до v0.8, только циферки другие.
Удаление/установка не помогла.
Сброс в завод, перепрошивка в ASU не решила проблемы.
Браузеры менял, инкогнито, CTL+F5 пробовал.

---

**2026-01-01T21:10:45 | Routerich**
Удалите текущие 3 пакета zapret2 и установите оба из этого поста(перевод ставить отдельно не нужно, теперь он вшит в luci-app-zapret2). Если всё ещё ошибка при входе в интерфейс или на вкладки blockcheck2 и debug log, то 
rm -rf /tmp/luci-*; /etc/init.d/uhttpd restart
и очистите кеш браузера. 
Если всё ещё не помогает, то удалите пакеты, выполните 
rm -rf /tmp/luci-* /www/luci-static/resources/view/zapret2/*"
и заново установите пакеты из поста

---

**2026-01-01T21:20:55 | Вадим**
После установки и захода zapret2 выдает теперь такое

---

**2026-01-01T21:32:45 | Вадим**
SyntaxError
Invalid regular expression: missing /
  in http://192.168.2.1/luci-static/resources/view/zapret2/debuglog.js?v=25.302.55195~bfcef12:?
  at http://192.168.2.1/luci-static/resources/luci.js?v=25.302.55195~bfcef12-1767292290:172:29
  at async Promise.all (index 9)

---

**2026-01-01T21:41:52 | Вадим**
Сброс на заводские и новая установка, при входе в zapret2 выдает точно такую же ошибку

---

**2026-01-01T21:46:04 | Ярослав**
+, тоже несколько раз удалил и поставил с репы, также ошибка Blockcheck2 и журнала отладки

 RouteRich 24.10.4 r28959-29397011cc RR-3.8.2 / LuCI openwrt-24.10 branch 25.302.55195~bfcef12
SyntaxError
Invalid regular expression: missing /
  in http://192.168.1.1/luci-static/resources/view/zapret2/debuglog.js?v=25.302.55195~bfcef12:?
  at http://192.168.1.1/luci-static/resources/luci.js?v=25.302.55195~bfcef12-1767292842:172:29

---

**2026-01-01T23:23:31 | Prosto_Vasia77 🇷🇺**
Добрый вечер, а когда планируется zapret2 0.8 добавить в asu?

---

**2026-01-01T23:30:06 | Αλέξανδρος**
Морда другая, и ошибка другая. Кн."3акрыть" не закрывает.
Может конфиг из zapret2-opkg задействовать,

---

**2026-01-01T23:47:59 | Prosto_Vasia77 🇷🇺**
Invalid regular expression: missing /
  in http://192.168.1.1/luci-static/resources/view/zapret2/debuglog.js?v=25.360.60166~f71b938:?
  at http://192.168.1.1/luci-static/resources/luci.js?v=25.360.60166~f71b938-1767300343:172:29
  at async Promise.all (index 9)

---

**2026-01-01T23:48:31 | Prosto_Vasia77 🇷🇺**
это на обновлённом zapret2

---

**2026-01-02T00:06:09 | Kiss_My_Axe**
Система - Планировщик. Удалить 0 4 * * * service zapret restart
Нажать Сохранить.

---

**2026-01-02T00:22:36 | Αλέξανδρος**
Еще попрошу маленькое уточнение, чтобы не залезать в backup. Собираюсь загрузить backup настроек. Там конфиг предыдущего Zapret2 есть?

---

**2026-01-02T00:24:54 | Routerich**
а не, нету /etc/config/zapret2
/opt/zapret2/ipset/zapret_hosts_user.txt
/opt/zapret2/ipset/zapret_hosts_user_exclude.txt
/opt/zapret2/ipset/zapret_hosts_youtube.txt
/opt/zapret2/ipset/zapret_hosts_auto.txt
/opt/zapret2/init.d/openwrt/custom.d/

---

**2026-01-02T00:33:51 | Kiss_My_Axe**
Система - Планировщик. Удалить 0 4 * * * service zapret restart
Нажать Сохранить.

---

**2026-01-02T00:35:43 | Anna Bagler**
Службы - Запрет, отключить, стоп. Система - Планировщик. Удалить 0 4 * * * service zapret restart
Нажать Сохранить.
Cлужбы - Podkop. Секции, main, списки сообщества, добавить YouTube.

---

**2026-01-02T00:38:09 | Anna Bagler**
Удалите строчки с упоминанием zapret.

---

**2026-01-02T00:40:21 | Anna Bagler**
Закончите с Планировщиком для начала. Видите строчку с zapret. Выделяете ее, delete на клавиатуре. Потом сохранить обязательно.

---

**2026-01-02T00:42:44 | Maxim Mrakov**
Всем привет, кто нибудь знает как отключить рекламу в ютубе? Использую подкоп с vless, zapret или ютуб анаблок не использую по причине, что их включение вызывает аномалии с интернетом в виде задержек или не доступности какого-то сайта😣

---

**2026-01-02T02:15:55 | Oleg Kobzev**
По моему Zapret установился этим скриптом?

---

**2026-01-02T02:16:47 | Kiss_My_Axe**
# АВТОКОНФИГУРАТОР ZAPRET

Попробуйте насканить страт для запрета.
Запустить, после установки нажать 1 ввод.
Начнётся поиск. Он может быть долгим, если чо ложитесь спать.
Как закончит поиск нажмите 2 и ввод.
Будут предлагаться для проверки страты. Как зелёным напишет - запускайте на телефоне/телеке ютуб.
Не работает - ввод. Работает 1 и ввод.
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

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

**2026-01-02T08:39:55 | Routerich**
Здравствуйте.
Система->Планировщик->
Посмотрите есть ли там zapret, если есть строка с ним то удалите её и все.

---

**2026-01-02T10:04:51 | Evgeniy**
Нужно ли к обновлённым пакетам zapret2 устанавливать руссификатор?

---

**2026-01-02T10:43:09 | Gomer Simpson**
Если ютуб через Zapret - используйте это: https://t.me/routerich/3845/420612
После каждой удачной стратегии, проверять работу Ю на всех девайсах.

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

**2026-01-02T12:16:14 | Bullet for my valentine Poison**
Угощайтесь уже релизом. :)
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-01-02T12:34:42 | Anna Bagler**
Запрет стопнуть. Строчку с restart zapret из Планировщика удалить и сохранить. Проверить.

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

**2026-01-02T15:25:17 | Kiss_My_Axe**
В терминал
service zapret stop && service zapret disable
service youtubeUnblock stop && service youtubeUnblock disable
reboot

---

**2026-01-02T15:29:53 | Anna Bagler**
Отключить и стопнуть запрет. Добавить список yt в секцию discord. Сменить в Настройке подкопа днс на гугл. В Планировщике убрать строчку с zapret restart и одно обновление списков в подкоп, сохранить. Проверить.

---

**2026-01-02T16:28:28 | Anna Bagler**
Домены добавляйте без www.
Ссылку на список подсетей добавляли? Попробуйте эту https://github.com/GubernievS/AntiZapret-VPN/blob/main/setup/root/antizapret/download/whatsapp-ips.txt

---

**2026-01-02T16:59:11 | Anna Bagler**
https://github.com/GubernievS/AntiZapret-VPN/blob/main/setup/root/antizapret/download/whatsapp-ips.txt - попробуйте это вместо внешнего списка подсетей. Там ниже есть.

---

**2026-01-02T17:42:23 | Gomer Simpson**
Включайте Zapret и пробуйте это: https://t.me/routerich/3845/420612

---

**2026-01-02T17:48:29 | Денис Ф.**
Помогло после этого   sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-01-02T20:59:01 | Routerich**
Здравствуйте.
Пробовать отключить zapret /podkop и проверять.
Если из за него искать что может мешать
А если и так не работает, то добавить домены в Podkop

---

**2026-01-03T10:40:16 | Rost**
Привет , тыкните плиз где описаны настройки openwrt ( unlock YouTube или zapret), после новых блокировок 27.12.25? У меня AX3000 с openwrt

---

**2026-01-03T11:31:31 | Ян Фимушин**
Я после установки ничего не делал дополнительно (за исключением несколько своих списков в zapret) 🤷‍♂️. Ну опять же, оказывается только на мобилке не работает. Все остальные устройства работают, так что пока терпит))

---

**2026-01-03T13:00:42 | Gomer Simpson**
Zapret животворящий!

---

**2026-01-03T13:04:51 | Mihey**
Сейчас кстати запустился АВТОКОНФИГУРАТОР ZAPRET. Не крашится как раньше. Посмотрю что найдёт.

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

**2026-01-03T15:50:04 | Андрей**
zapret2 помогите установить

---

**2026-01-03T22:22:47 | Prosto_Vasia77 🇷🇺**
Вечер добрый, а когда можно ожидать починенный zapret2 0.8 в репе?

---

**2026-01-03T22:35:35 | Gomer Simpson**
С zapret ютуб, обычно, лучше работает. Скрипт автоподбора стратегий найдите в теме.

---

**2026-01-04T07:37:07 | Макс**
для автоматического рестарта запрета2 просто добавить 2 к zapret получается? А то каждое утро он отваливается и ручками надо лезть и перезапускать запрет2

---

**2026-01-04T07:39:27 | Routerich**
Здравствуйте.
Скорее всего он отваливается из-за того, что там рестарт zapret уже.
Попробуйте просто эту строку убрать и посмотреть как будет

---

**2026-01-04T09:44:44 | Kiss_My_Axe**
As u wish.
Попробуйте насканить страт для запрета.
Запустить, после установки нажать 1 ввод.
Начнётся поиск. Он может быть долгим, если чо ложитесь спать.
Как закончит поиск нажмите 2 и ввод.
Будут предлагаться для проверки страты. Как зелёным напишет - запускайте на телефоне/телеке ютуб.
Не работает - ввод. Работает 1 и ввод.
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-01-04T09:51:27 | Anna Bagler**
Службы - Zapret, отключить и стоп. Службы - Podkop, прокручиваемся до секции discord, добавляем список yt в списках сообщества.

---

**2026-01-04T14:53:13 | Денис**
День добрый, есть вопрос
На сайте Русторка не поработать с блокировщиком рекламы, куда и как добавить сайт русторки в исключение на блокировку рекламы, чтобы можно было без проблем серфить по сайту?
Роутер на 5 скрипте и zapret2

---

**2026-01-04T15:15:15 | Alexey S**
Добрый день! Пытаюсь в хроме завести Gemini (https://gemini.google.com/), прошивка чистая, роутер только с печки.
Установил скрипт 5, в подкопе добавил в main список google play + google AI, а в zapret в google hosts внёc хосты из списка (https://github.com/itdoginfo/allow-domains/blob/main/Services/google_ai.lst)

у вас после этого заработал гемини или что-то ещё я упустил?

---

**2026-01-04T16:07:06 | Aidar Safiullin**
Друзья, доброго дня! 
Подскажите, пожалуйста, для того чтобы играть в BF6 на консоли PS5 - какие необходимо манипуляции на роутере провернуть? Я так понимаю необходимо накатить zapret?
Или уже со стоковых настроек все запоёт?
Благодарю!

---

**2026-01-04T16:34:15 | Routerich**
Ну скорее всего через Zapret у вас ютуб, если по 5-му скрипту ставили.

---

**2026-01-04T16:40:57 | Александр 🔴🔵**
как запустить в Zapret  - стратегию alt6  для игры надо

---

**2026-01-04T17:13:52 | Gomer Simpson**
Выглядит, как стратегия для Zapret 2.

---

**2026-01-04T18:09:30 | Sigma**
Добрый вечер, пытаюсь победить фильтрацию UDP на Zapret2. Версия 0.8-r28, из этого топика. В талмуде из WIKI про дурение UDP ни слова. В логах очень трудно выловить упоминания UDP пакетов. Подскажите рабочие стратегии?

---

**2026-01-04T18:12:31 | Bullet for my valentine Poison**
https://github.com/bol-van/zapret2/blob/master/docs/manual.md

---

**2026-01-04T19:24:51 | Sigma**
Спасибо за участие, сложно даётся Zapret2. Попробую позже, когда он наберёт большую популярность и инструкций будет по-больше. Благо, zapret1 всё ещё справляется

---

**2026-01-04T19:41:10 | Routerich**
В теме есть скрипт автоподбора стратегий для 1 запрета, его использовать. Либо же попробовать  удалить запрет, и установить zapret2. Там легче найти рабочий вариант стратегии

---

**2026-01-04T19:43:15 | Anna Bagler**
Попробуйте насканить страт для запрета.
Запустить, после установки нажать 1 ввод.
Начнётся поиск. Он может быть долгим, если чо ложитесь спать.
Как закончит поиск нажмите 2 и ввод.
Будут предлагаться для проверки страты. Как зелёным напишет - запускайте на телефоне/телеке ютуб.
Не работает - ввод. Работает 1 и ввод.
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-01-04T20:41:38 | Ivan**
Я в этом случае удалил zapret и поставил zapret 2. Не знаю прав ли был, но мне помогло :-)

---

**2026-01-04T21:07:36 | BaTTr ;/**
Приветствую забрал сегодня роутер, настроил поставил Zapret2 через пакетный менеджер в итоге не работает Blockcheck2 может есть инфа по исправлению ???

---

**2026-01-04T22:35:19 | Routerich**
обновили zapret2 в репозитории, можно с ним собирать

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

**2026-01-05T02:17:26 | BaTTr ;/**
Да все получилось но в итоге не фурычит zapret2 с авто стратегии по какой причине хз, ща поставил первый zapret там также костыли пошли либо я не догоняю что, через  nfqws протыкал разные стратегии на гитахбе, в итоге либо работают все но только на телеке и компе или  на iOS и телеке и то только ютуб и инста

---

**2026-01-05T11:43:16 | Kiss_My_Axe**
Попробуйте это. Ютуб из подкопа убрать. Варп душат.

Попробуйте насканить страт для запрета.
Запустить, после установки нажать 1 ввод.
Начнётся поиск. Он может быть долгим, если чо ложитесь спать.
Как закончит поиск нажмите 2 и ввод.
Будут предлагаться для проверки страты. Как зелёным напишет - запускайте на телефоне/телеке ютуб.
Не работает - ввод. Работает 1 и ввод.
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-01-05T15:09:12 | Anna Bagler**
Попробуйте это. Ютуб из подкопа убрать. Варп душат.

Попробуйте насканить страт для запрета.
Запустить, после установки нажать 1 ввод.
Начнётся поиск. Он может быть долгим, если чо ложитесь спать.
Как закончит поиск нажмите 2 и ввод.
Будут предлагаться для проверки страты. Как зелёным напишет - запускайте на телефоне/телеке ютуб.
Не работает - ввод. Работает 1 и ввод.
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-01-05T15:41:14 | Трантипуй**
Удалите текущие 3 пакета zapret2 и установите оба из этого поста(перевод ставить отдельно не нужно, теперь он вшит в luci-app-zapret2). Если всё ещё ошибка при входе в интерфейс или на вкладки blockcheck2 и debug log, то 
rm -rf /tmp/luci-*; /etc/init.d/uhttpd restart
и очистите кеш браузера. 
Если всё ещё не помогает, то удалите пакеты, выполните 
rm -rf /tmp/luci-* /www/luci-static/resources/view/zapret2/*"
и заново установите пакеты из поста

---

**2026-01-05T19:46:07 | Снежный**
Привет.  Где можно скачать запрет2? В вики только через репу, но она не работает, пытаюсь поставить через ipk.
нашёл только у парня - https://github.com/remittor/zapret-openwrt/releases

---

**2026-01-05T19:46:59 | Routerich**
Здравствуйте.
Пробуйте ставить zapret2 и потом запускать blockcheck для поиска стратегий и проверять

---

**2026-01-05T20:03:04 | Снежный**
Была ошибка при установке Zapret
opkg install /tmp/upload.ipk

Installing zapret2 (0.8-r30) to root...
Creating /opt/zapret2/ipset/zapret_hosts_user_exclude.txt from default
Creating /opt/zapret2/ipset/zapret_hosts_youtube.txt from default
Starting zapret2...
Config generated: /opt/zapret2/config
Strategies: 0
Installing libpcap1 (1.10.5-r2) to root...
Downloading https://downloads.openwrt.org/releases/24.10.0/packages/aarch64_cortex-a53/base/libpcap1_1.10.5-r2_aarch64_cortex-a53.ipk
Installing ncat (7.95-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.0/packages/aarch64_cortex-a53/packages/ncat_7.95-r1_aarch64_cortex-a53.ipk
Configuring libpcap1.
Configuring ncat.
Configuring zapret2.

Ошибки

Collected errors:
 * resolve_conffiles: Existing conffile /etc/config/zapret2 is different from the conffile in the new package. The new conffile will be placed at /etc/config/zapret2-opkg.
 * resolve_conffiles: Existing conffile /opt/zapret2/config is different from the conffile in the new package. The new conffile will be placed at /opt/zapret2/config-opkg.

---

**2026-01-05T20:29:32 | Alex Mendez**
ребзя, а вот если zapret2 (да и древний youtubeunblock ранее), в целом ютубку отлично бустил, но иногда встречаются примерно на каждом пятом видео где-то уходы в бесконечную загрузку, приходится переключать видео на другое и прыгать обратно. То против такого можно каким-то автоматическим скриптом перебрать стратегии до получения успешного опыта?

---

**2026-01-05T20:31:11 | Routerich**
Подбирайте стратегию
В zapret2 есть встроенный blockcheck

---

**2026-01-05T21:03:47 | Ибра**
Здравствуйте все! Что будет если я отключу zapret в службах?

---

**2026-01-05T21:17:00 | Снежный**
Пока маюсь только с zapret2

---

**2026-01-05T21:43:37 | Bot_never_bot**
как выбрать между скрипт №5 и zapret 2 ?

---

**2026-01-05T21:44:09 | Routerich**
А что выбирать? Zapret2 не обойдёт вам геоблок)

---

**2026-01-05T21:50:12 | Routerich**
А что вам мешает после поставить zapret2?

---

**2026-01-05T22:57:24 | Kiss_My_Axe**
Красивое. Ютуб в майн, или это:

Попробуйте насканить страт для запрета.
Запустить, после установки нажать 1 ввод.
Начнётся поиск. Он может быть долгим, если чо ложитесь спать.
Как закончит поиск нажмите 2 и ввод.
Будут предлагаться для проверки страты. Как зелёным напишет - запускайте на телефоне/телеке ютуб.
Не работает - ввод. Работает 1 и ввод.
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-01-06T00:47:19 | Bullet for my valentine Poison**
Угощайтесь уже релизом. :)
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-01-06T05:06:46 | Артём Лаврентьев**
Доброго времени суток. Может быть кто то подскажет. Поставил zapret2 и с такой проблемой столкнулся. У меня после установки с дефолтными настройками не заводится discord
Кажется что скрипты там из коробки на него есть, но возможно что нужно ещё что то
В документации к zapret2 не нашёл ответа

---

**2026-01-06T07:44:19 | Игорь**
Подскажите пожалуйста, певый zapret нужно удалять, перед установкой второго?

---

**2026-01-06T09:04:54 | Kiss_My_Axe**
Может Ю чудить, потому что он через zapret1 ходит.

---

**2026-01-06T09:09:42 | Андрей Стыврин**
Через podkop заработало на смартТВ.
Можно как-то настроить ZAPRET2 и PODKOP, чтобы для определённых узлов работало что-то одно?

---

**2026-01-06T09:14:08 | Kiss_My_Axe**
Попробуйте насканить страт для запрета.
Запустить, после установки нажать 1 ввод.
Начнётся поиск. Он может быть долгим, если чо ложитесь спать.
Как закончит поиск нажмите 2 и ввод.
Будут предлагаться для проверки страты. Как зелёным напишет - запускайте на телефоне/телеке ютуб.
Не работает - ввод. Работает 1 и ввод.
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-01-06T09:29:11 | Михаил**
К слову. Информации для. У меня отлично работал zapret2 вместе с podkop с доменами  youtube.  Стики на телеках в статику и в исключения podkop. В итоге через podkop в youtube ходят все устройства кроме стиков на телеках, стики через второй запрет. Такая схема довольно живенько отработала. Сейчас до кучи поднял в podkope byedpi, запрет2 теперь держу в офлайне. Так что схема с одновременным использованием на один домен и запрeта2 и подкопа у меня оказалась вполне живуча.

---

**2026-01-06T12:43:30 | Bullet for my valentine Poison**
В самом мануале Fresa так же показывает "примеры". https://github.com/bol-van/zapret2/blob/master/docs/manual.md вот тут можно еще попытаться, что-то уловить)

---

**2026-01-06T12:44:09 | Ансвер Ответович**
Фуух, через скрипт подбора стратегий zapret  заютубились таки телеки LG.   :)  Где этот любитель поцелуев с топором? Спасибо за подсказку!

---

**2026-01-06T12:49:59 | Dmitrii Burenin**
Так zapret2 сам найдёт стратегии и при желании сам включит работающую.

---

**2026-01-06T14:04:50 | Vasa**
возможно еще нужен амазон и cloudflare

https://github.com/GubernievS/AntiZapret-VPN/tree/main/setup/root/antizapret/download

---

**2026-01-06T14:38:49 | Борис**
Привет всем. Может, кому-то поможет. Я обновил прошивку роутера на последнюю стабильную (раньше был YouTube Unblock и zapret), затем я удалил yub и zapret, и поставил zapret2. Я пытался настроить zapret2 по инструкции из wiki, но он никак не хотел открывать ютуб по факту - blockcheck2 находил удачные стратегии, я их вставлял в свой конфиг, но по факту ничего не открывалось... Ради интереса я зашел в журнал url-адресов и увидел, что мой телефон (с которого я проверял доступность YouTube) получал ipv6 по домену https://youtube.com (напомню, что в логе подбора стратегий curl тестировал доступность ipv4). Я решил отключить ipv6 в разделе Интерфейсов на роутере (ppoe-wan в моем случае), и ура - запрет2 заработал...
Вывод: если после успешного подбора стратегий сайт все равно не открывается, проверьте журнал url в роутере, возможно там используются ipv6 адреса. Можно было бы добавить это в wiki, в статью про zapret2

Ну и вопрос от меня: а можно как-то продолжить пользоваться ipv6 и запретом2, или у нас в стране в принципе ipv6 соединения банятся провайдерами? (я чайник, извините за тупой вопрос)

---

**2026-01-06T15:02:05 | 𝐼𝓁𝓀𝒾𝓃**
я запустил вот этот скрипт:
sh <(wget -q -O - https://raw.githubusercontent.com/routerich/RouterichAX3000_configs/refs/heads/wdoctrack/run_universal_config.sh) 2>&1 | tee /root/run.log
и у меня только появился zapret

---

**2026-01-06T15:06:16 | Дмитрий**
отключил и остановил. А в планировщике просто удалить эту строку? - 0 4 * * * service zapret restart

---

**2026-01-06T15:07:40 | Борис**
Я правильно понял, что zapret2 может делать обходы по ipv6 тоже, но blockcheck2 захардкожен на проверку доступности по ipv4? Потому что я открываю YouTube ipv6 с включенным запретом, и тот не работает, но когда я открываю ютуб ipv6 с включенным byebyeDpi на телефоне (аналог запрета для Android), то у меня YouTube ipv6 работает отлично...

---

**2026-01-06T16:01:35 | Routerich**
Сделайте так. Службы - zapret - остановить и выключить автозапуск. Далее службы - подкоп - промотать вниз до секции с названием дискорд, там будет выбран список дискорд, там же выбрать список ютуб - применить. И проверяйте

---

**2026-01-06T16:16:40 | Anna Bagler**
Ещё проверьте тогда, чтобы в Система - Планировшик не было строчек со словом zapret. Если есть, удалить всю строку и сохранить.

---

**2026-01-06T17:36:24 | Борис**
а мне нужно как-то портировать стратегии специально для ipv6? насколько я понял, мне нужно использовать параметр --filter-l3=ipv6 в описании стратегии, ну и в bash-скрипте blockcheck2.sh переопределить параметры $1 и $2 и т.д. для курла, чтобы он нужную версию протокола использовал при проверке доступности... В общем, есть какая-то быстрая инструкция в несколько шагов, или это прям жёсткий гемор? Не представляю пока объём пердолинга, но вроде как zapret2 поддерживает ipv6 и можно (в теории) несколько параметров поменять, в моем случае...

---

**2026-01-06T17:44:03 | Bullet for my valentine Poison**
Быстрой инструкции нет, есть только это: https://github.com/bol-van/zapret2/blob/master/docs/manual.md

---

**2026-01-06T18:22:13 | Routerich**
можно оставить только скрипт 5
так как для работы zapret2 надо стопать zapret и отключать автозапуск, и с планировщика удалять

---

**2026-01-06T18:30:16 | Routerich**
https://github.com/remittor/zapret-openwrt/discussions/168?ysclid=mk2qx26l6q216202817

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

**2026-01-06T20:36:34 | Алексей**
Подкоп починил

По поводу вашего вопроса - я без понятия. Друг использует обычный zapret (который zapret-youtube-discord). У него работает с ним и без него

---

**2026-01-06T20:54:08 | Роман**
Всё работет, использую podkop, zapret2. Да и не заблокирована игра.

---

**2026-01-06T22:13:18 | Роман**
https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_domainlist.txt

https://github.com/HybridNetworks/whatsapp-cidr/blob/main/WhatsApp%2Fwhatsapp_cidr_ipv4.txt

https://github.com/GubernievS/AntiZapret-VPN/blob/main/setup/root/antizapret/download/whatsapp-ips.txt

Попробовать это добавить. 
Я победил Вацап на сяоми и реалми, но s24 ultra работает только через ВПН.

---

**2026-01-06T22:21:33 | Anna Bagler**
Службы - Zapret.

---

**2026-01-06T22:28:48 | Alex Mendez**
у меня такая же проблема у как у предыдущего комментатора, просьба помочь разобраться. Ребут раз в ~20 минут стабильно. Прошивка 24.10.4 r28959-29397011cc RR-3.8.2 (роутер usb 2.0) + 5 скрипт + удален zapret и установлен zapret2.
4 крайних ребута это оно.

---

**2026-01-06T23:14:19 | Борис**
Ребятишки. Вряд ли это кому-то вообще понадобится. Но я целый день пердолился, чтобы заставить работать zapret2 на youtube ipv6. Может, моя инструкция кому-то поможет:
1) в папке /opt/zapret2 редактируете файлы config и config.template таким образом, чтобы был установлен параметр DISABLE_IPV6=0 (по умолчанию поддержка ipv6 выключена, вы её должны включить)
2) поскольку в веб-интерфейсе luci не поддерживается подбор и тестирование стратегий для ipv6, вы должны из командной строки запустить /opt/zapret2/blockcheck2.sh и в утилите прописать ipv6 для подбора, когда она об этом спросит (см. скриншот) 
3) когда утилита начнёт подбор и тестирование, копируйте параметры для nfqws2 из какой-нибудь стратегии, которая помечена как ! AVAILABLE !
4) Доп. скрипты я у себя выключил, т.к. не пользуюсь дискордом, и этот кастомный скрипт discord_media выключал поддержку ipv6 (возможно, это работало только в пределах скрипта, но я всё равно его вырубил от греха подальше)

---

**2026-01-06T23:31:03 | Alex Mendez**
помогло, но ведь эта настройка наверняка у всех "с завода" стоит после 5 скрипта... почему у меня ребутает с ней то 🤔
Я разве что "Защиту от DNS rebinding" отключал и Zapret на Zapret2 целиком заменил, остальное несущественно.

---

**2026-01-06T23:38:40 | Alexey**
Накатил скрипт 5, но что-то нет youtube на мобилках, меняю NFQWS_OPT через luci в Services/Zapret, но судя по ps -w, nfqws стартуют со своим конфигом и фиолетово им на мои правки, это норма?

---

**2026-01-07T00:23:44 | Andrey Khrushchev**
Добрый ыечер, попробовал поиском, к сожалению не нашёл, есть стратегия для zapret под Ростелеком, недавно получил роутер, утсановил zapret2 и пока не пойму как перенести прежнюю стратегии в новый zapret. В прошлый раз ставил вручную с гитлаба, в этот по инструкции через opkg. На первый взгляд синтаксис команд чуть отличается, нет ли у кого совета или готового гайда?

---

**2026-01-07T00:35:19 | Anna Bagler**
C zapret2 так не выйдет. Читайте тут https://t.me/routerich/80283/407345

---

**2026-01-07T07:36:43 | Kiss_My_Axe**
Попробуйте насканить страт для запрета.
Запустить, после установки нажать 1 ввод.
Начнётся поиск. Он может быть долгим, если чо ложитесь спать.
Как закончит поиск нажмите 2 и ввод.
Будут предлагаться для проверки страты. Как зелёным напишет - запускайте на телефоне/телеке ютуб.
Не работает - ввод. Работает 1 и ввод.
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-01-07T08:03:06 | Anton**
В дачном доме есть два кинетика, в меш сети. На главном развернут nfqws (он же zapret). В последнее время на Ростелекоме эти обходы работают не стабильно, нужно постоянно менять стратегию. В первую очередь мне это нужно для системы видеонаблюдения reolink (они ушли из РФ и достучаться до их серверов можно только с бубном). Так же у меня есть vps с vless. На кинетик как я понял его развернуть тоже не очень просто.
Вопросы:
1. Насколько просто замаршрутизировать часть трафика через vps?
2. Заработает ли меш с кинетиком?

---

**2026-01-07T13:11:50 | Роман**
Я не читал талмуд Болвана, просто удалял верхние стратегии пока не заработало, из чего сделал вывод о чтении сверху. Но вы можете прочесть мануал. Где то в чате есть короткая версия. 
https://github.com/bol-van/zapret2/blob/master/docs%2Fmanual.md

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

**2026-01-07T13:45:47 | DMITRIY**
Как установить zapret?

---

**2026-01-07T14:59:46 | awesome51**
Сегодня при просмотре twitch начала всплывать реклама. На роутере установлено из обходов: Zapret2+DOH Xbox. Из-за чего может появляться реклама? DOH виноват?

---

**2026-01-07T15:19:29 | 💵morfey💵**
Юзаю zapret ,все работает

---

**2026-01-07T16:17:16 | Routerich**
Интересно, а zapret если стопнуть?

---

**2026-01-07T19:49:10 | awesome51**
попробовал удалить DOH Xbox, не помогло. Отключаю Zapret2 тоже не работает сайт, на роутере ничего более не установлено

---

**2026-01-07T19:52:22 | awesome51**
Добрый вечер. Столкнулся с такой проблемой на Твиче. На самом роутере установлен Zapret2 + DOH Xbox. Отключал, включал пакеты, ничего не помогает, ошибка не исчезает, кто может с этим помочь, что-то еще проверить?

---

**2026-01-07T20:31:46 | Routerich**
Здравствуйте.
Пустите ютуб через Zapret тогда, а из Podkop уберите

---

**2026-01-07T20:42:00 | awesome51**
переустановил прошивку на роутер + zapret. ситуация повторяется, твич работает около 5 минут, далее превращается всё в следующий вид

---

**2026-01-07T20:50:18 | Evg**
А как в Zapret его вписать подскажите

---

**2026-01-07T20:53:39 | Routerich**
он по умолчанию есть в Zapret, ютуб.

---

**2026-01-07T21:54:01 | awesome51**
Не использовал скрипт (работало ранее с Unblock, затем с Zapret2), но теперь задумываюсь про скрипт, да, вы правы

---

**2026-01-07T22:25:11 | Vasili Pinchuk**
Добрый вечер. Где может быть проблема youtube на на всех планшетах/телефонах летает на всех устройствах и ПК в браузере "нет подключения…".  

Включены Zapret(2) и youtubeUnblock куда копать, что поставить/удалить/настроить, что читать в новом 26 году?

---

**2026-01-07T22:38:39 | Vasili Pinchuk**
О, только с оставленным Zapret2 работает и в браузерах.
Спасибо большое.
1) Подкоп есть смысл ставить или работает - не трогать?
2) Что выключено я так понял можно удалить и запрет2 и 1 не связаны?
Ещё раз спасибо!

---

**2026-01-07T22:47:44 | Vasili Pinchuk**
discord и по мелочам с zapret2 он недоступен :(

---

**2026-01-07T22:49:04 | Anna Bagler**
discord тут вроде с zapret2 поднимали, поищите.

---

**2026-01-07T23:31:22 | Vasili Pinchuk**
Это как может быть почти на чистой системе после установки только zapret2?

---

**2026-01-08T10:31:34 | Дмитрий Лисиенко**
Здравствуйте, подскажите этот скрипт sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest) ищет стратегии к ютубу, а что поменять что бы он искал стратегии к чату gpt  или к другому сайту? Через вайфай чат gtp работает, а вот через lan нет

---

**2026-01-08T10:43:35 | Gomer Simpson**
Пустите Ю через Zapret. В этой теме поиском найдите АВТОКОНФИГУРАТОР. Подберите стратегию - бой окончен.

---

**2026-01-08T10:49:51 | Vasa**
проверь чё в списке дискорда

там есть эти IP ?
https://github.com/GubernievS/AntiZapret-VPN/blob/main/setup/root/antizapret/download/discord-ips.txt

и куда у тебя дискорд идёт в warp или опера-прокси?

---

**2026-01-08T12:35:56 | Алексей Омон**
сижу на подкопе ..  вроде как  zapret 72.6 вышла уже  . .партировать бы

---

**2026-01-08T14:54:42 | Михаил gl**
Добрый день. Подскажите пожалуйста, возник вопрос по zapret2. Где находится файл zapret_ipset_*.txt или где его нужно создать, что бы внести в него список ip адресов, для исключения из стратегии? Потому что при нажатии на кнопку выбора, пишет, что нет доступных ip адресов.

---

**2026-01-08T15:50:59 | Михаил gl**
Да это сделал благодарю. Но возникла другая проблема, которую никак не могу решить. Направьте пожалуйста по верному пути решения, а то у меня уже идеи закончились. Обрисую ситуацию. У меня на роутриче настроено всё через подкоп. Есть свой vless через который открывается всё заблокированное. В списках выбран Russia inside. Также в подкопе прописаны полностью маршрутизированные IP-адреса устройств, которые принудительно используют только vless, мне очень важен этот момент. Всё это работает как надо, за исключением Ютуба, который больше почему то не работает. Установил Zapret2 что бы только ютуб через него шел. Всё остальное так же через подкоп. В запрете добавил айпи адреса устройств, которые должны игнорировать его, как раз те, которые только через vless пущены. Итог, Ютуб работает, всё остальное не работает, причем те устройства которые идут принудительно через vless тоже перестают работать, хотя их айпи адреса добавлены в исключения в запрете. Пробовал убирать Russia inside из списка, менять на geoblock , meta и так далее, результата положительного не дало. Всегда что то начинает работать, а что то при этом отваливается. Подскажите куда копать? или то, что я описал, реализовать изначально не получится?

---

**2026-01-08T15:58:38 | Михаил gl**
Подскажите в таком случае, как правильно сдружить подкоп с запретом2, так, что бы ютуб шел только через запрет а весь остальной трафик через подкоп. При этом устройства, которые принудительно используют только vless так же не задействовались zapretom? Просто я думал, что если ввести в списки исключений запрета айпи устройств, он будет их игнорировать.

---

**2026-01-08T16:12:05 | 🎊🈵🎭**
а подскажите, пожалуйста, как сделать 4 пункт? (4. Найдите пакеты через поиск zapret2 или загрузите .ipk файлы через Upload Package) по zapret2/ z d,bdf. я вбиваю в поиск запрет2, а у меня вылезает ошибка. я ничего не понимаю

---

**2026-01-08T16:13:17 | Bullet for my valentine Poison**
Справа - обновить пакеты.А потом  в фильтре - Zapret2

---

**2026-01-08T17:44:26 | Routerich**
Ещё из
Система-->Планировщик ->
Убрать строчку про zapret если она там есть

---

**2026-01-08T17:49:51 | Anna Bagler**
Нет его рестарта в Планировщике вроде.
 @Mihkateddyazovrostov Система - Планировщик, есть строчки с zapret?

---

**2026-01-08T18:34:29 | Routerich**
Ну надо установить пакет
luci-app-zapret2

---

**2026-01-08T18:57:17 | Bullet for my valentine Poison**
почитайте внимательно мануал. https://github.com/bol-van/zapret2/blob/master/docs/manual.md вот оригинал, но там еще сложнее

---

**2026-01-08T19:24:05 | Alex Mendez**
вот примерно подтверждение этого направления пытаюсь найти. Настолько ли он нужен если откл. Так понял снимает нагрузку с CPU, но создает кучу других проблем включая с обходами. Выше сказано про "фикс", что за фикс и полностью ли снимает этот вопрос в направлении zapret2 🤷🏻‍♂️

---

**2026-01-08T19:40:20 | Bullet for my valentine Poison**
https://github.com/bol-van/zapret2/blob/master/docs/manual.md и вот это советую сохранить в закладки.

---

**2026-01-08T20:27:59 | Routerich**
У вас zapret remittor не заработал, работает только опера прокси и WARP.
То есть Discord и YouTube через Podkop. Все должно работать

---

**2026-01-08T20:55:57 | Роман**
У меня подкоп с собственным ключём hysteria2, zapret2. В подкопе список мета и три внешних листа с доменами и ip.

---

**2026-01-08T20:59:01 | Борис**
Привет всем, кто-то пробовал zapret2 настроить таким образом, чтобы он НЕ работал для конкретных локальных клиентов? У меня PlayStation™ 5 не может нормально с запретом запускать сетевые игры, я хотел бы полностью zapret2 для нее отключить (я знаю, что можно исключать домены в стратегии, но мне это не подходит, т.к. я не собираюсь для каждой новой игры дебажить и находить какие домены она использует)

---

**2026-01-08T21:28:13 | Кирилл Устимов**
Я не хочу чтобы ДС работал через opera proxy, а через zapret2, как мне убрать ДС из opera proxy

---

**2026-01-08T21:33:37 | Борис**
В общем, свою проблему я решил таким образом, что комп у меня ходит по ipv6 адресам, а Playstation работает только на ipv4. Поэтому я в своих стратегиях для zapret2 прописал в начале параметр --filter-l3=ipv6. И таким образом мои стратегии не касаются адресов ipv4 на Playstation

---

**2026-01-08T22:30:02 | Gomer Simpson**
В сторону Zapret. И АВТОКОНФИГУРАТОР к нему - поиск в теме.

---

**2026-01-09T00:24:44 | Gomer Simpson**
Всё так. Очевидно, Zapret на вашем провайдере не работает. Придётся использовать подкоп.

---

**2026-01-09T00:27:24 | Gomer Simpson**
Есть смысл, если 5-10 не сработали. Но 25...  Тут уж, видимо, бессмысленно. Попробуйте Zapret2. В WIKI есть мануал.

---

**2026-01-09T09:30:28 | Alex Mendez**
Под ночь ютуб нонстопом гонял, утром тоже, с нескольких устройств уже. Ни одного виса. Зачем гуглвидео в хостлистах добавляют тогда - не ясно, типа "давай добавим всё вдруг сработает" 💁‍♂️. Возможно конкретно этот тспу так так реагирует на излишние попытки обхода 🤷🏻‍♂️ Тот случай когда overkill только вредит.

Причем началось это где-то в начале декабря, раньше хавало и так, в старом ютубанблоке у меня он тоже в списке хостов был, но первым делом решил прыгнуть на топовое решение (zapret2) чтобы исключить вариант отсталости обхода.

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

**2026-01-09T13:49:47 | Артём**
Меня просто не устраивает встроенный в роутер zapret, его можно как то отключить, я хочу что бы весь трафик шёл через WireGuard туннель.

---

**2026-01-09T16:18:37 | Anna Bagler**
Система - Пакеты, обновить списки, в поле фильтра вписать zapret2 и ok.

---

**2026-01-09T16:30:46 | Andrey Matveev**
Установил согласно инструкции. В сервисе только zapret, zapret2 не появился

---

**2026-01-09T18:34:02 | Andrey Semehin**
Ошибка 279 была когда добавил в zapret домены и сети. Если в секцию дискорда в подкопе то вообще не входило

---

**2026-01-09T18:56:09 | Mihey**
Добрый вечер.Хотел поставить Zapret 2 согласно руководству что скачал из вики, но сразу столкнулся что у меня нет Zapret 2 в списке доступных пакетов после "Обновления списков пакетов". Есть только просто Zapret и показано что он уже установлен. Версия системы: RouteRich 24.10.2 r28739-d9340319c6 RR-3.6.6 / LuCI openwrt-24.10 branch 25.250.61039~923f8d9

---

**2026-01-09T18:59:47 | K**
Привет, всё проще чем кажется. У вас прошивка устарела для zapret2

---

**2026-01-09T19:00:47 | K**
Инструкция включает полуобщие условия, репозитории для нашего роутера включают zapret2 с 24.10.3 oWRT

---

**2026-01-09T19:11:09 | Дмитрий Кравченко**
https://t.me/routerich/80283/407345
Добрый вечер, я может чет туплю, но в пункте 28.1. написано:
1. Откройте Services → Zapret2 → Service
2. В таблице Strategies найдите нужную стратегию или создайте новую
3. В поле Script вставьте параметры из SUMMARY:
Нету ни одной кнопки Service, да и поля Script тоже)

---

**2026-01-09T19:54:02 | Matvey**
Добрый вечер! Скажите, пожалуйста, есть ли какие-то варианты оживить ютуб на телевизоре с LG в Zapret2? Пробовал сделать как здесь и не завелось(

---

**2026-01-09T20:09:11 | Михаил Бузинов**
Zapret поставил - ютуб на телефоне и ноуте заработал .

А на телевизорах( на смарте ) нет.😭

Подскажите что сделать?

---

**2026-01-09T20:11:49 | Anna Bagler**
Именно zapret2?

---

**2026-01-09T20:25:14 | Dmitriy**
но по крайней мере podkop он установил и zapret

---

**2026-01-09T23:05:20 | Maxim =)))**
Если стоит zapret2 и podkop, норм, можно ставить?

---

**2026-01-09T23:17:21 | Mallory**
Подскажите, пожалуйста, при попытке установить zapret2 требуются gzip, ncat. Но их в репозитарии я не вижу. Как надо действовать в таком случае?

---

**2026-01-09T23:43:33 | Георгий Корнилов**
Подскажите, пожалуйста: роутер с USB 2.0, обновил прошивку на 24.10.4 без сохранения настроек, потом решил запустить скрипт № 5, но получаю такую ошибку:

zapret not installed. Installing zapret...
Installing zapret (72.20251122) to root...
Collected errors:
 * opkg_install_pkg: Checksum or size mismatch for package libnetfilter-queue1. Either the opkg or the package index are corrupt. Try 'opkg update'.
 * opkg_install_cmd: Cannot install package zapret.
Downloading https://github.com/routerich/packages.routerich/raw/24.10.4/routerich/zapret_72.20251122_aarch64_cortex-a53.ipk
Installing libnetfilter-queue1 (1.0.5-r4) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/libnetfilter-queue1_1.0.5-r4_aarch64_cortex-a53.ipk
Error installing zapret. Please, install zapret manually and run the script again.

opkg update отрабатывает, но если через UI попробовать установить libnetfilter-queue1 или zapret, то получаю 255 ошибку.

---

**2026-01-10T00:33:06 | Борис**
Всё, что написано выше в этой теме — чистая правда, роутер потрясающий. Моя история такова:

Я никого не трогал, играл себе в игрулечки на Playstation 5... Терпел белые списки, неработающие сайты. Как однажды мою любимую сетевую игру заблокировали - невозможно было подключиться к серверам... Я не про Roblox, а про Battlefield 6, но сути это не меняет. По слухам, некая программа Zapret помогала обходить любые ограничения. Но ведь эта программа под Windows и Linux, а я играю на Playstation, и как же быть? Купить роутер на OpenWRT!

Дальше всё как в тумане. Помню, что мой роутер нельзя было прошить на OpenWRT, потому что было мало оперативы. Ozon, строка поиска... Статус заказа - готов к выдаче... Открываю коробку... Несколько минут спустя ютуб открывается, Zapret скачан, спустя ещё пол-часа Battlefield 6 уже работает во всю, прочитал про белые списки, узнал про Vless, узнал, что Wireguard и OpenVPN блокируются по сигнатурам, узнал про Vless, но мне этого было мало, и вот я уже позабыл про депрессию от блокировок и очнулся, когда установил nginx, ddns-клиент, поставил себе xray сервер, через бекдор получил бесплатный белый IP у провайдера и готовлюсь делать маскировку через vless Reality под сайт провайдера, ведь сайты провайдера доступны в режиме белых списков, а у меня IP из подсети провайдера... Стоп.

Чем я там занимался? А, ну да. Я играл в игры и что-то они забарахлили. Ну так вот, роутер прекрасный, для обучения тоже подходит отлично, да и как игрушка тоже замечательный — который день не могу оторваться от исследований... Кстати, я вообще собирался написать отзыв про обновленную чёрную тему в Routerich Luci - в ней проблема с кнопками, они одного цвета, и в этом плане они проигрывают белой теме :)

---

**2026-01-10T10:41:37 | Vasa**
я этим пользуюсь. там уже автор всё сделал. списки каждый день обновляются сами
https://github.com/GubernievS/AntiZapret-VPN

---

**2026-01-10T10:47:30 | Vasa**
тут частные списки. именно под проект

https://github.com/GubernievS/AntiZapret-VPN/tree/main/setup/root/antizapret/download

тут в скрипте видно что загружается
https://github.com/GubernievS/AntiZapret-VPN/blob/main/setup/root/antizapret/update.sh

---

**2026-01-10T10:53:00 | Vasa**
амазон этот добавлял?
https://github.com/GubernievS/AntiZapret-VPN/blob/main/setup/root/antizapret/download/amazon-ips.txt
и CF
https://github.com/GubernievS/AntiZapret-VPN/blob/main/setup/root/antizapret/download/cloudflare-ips.txt

---

**2026-01-10T13:05:26 | Nikolay Barkalov**
подскажите zapret нужен при использовании скрипта 5?

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

**2026-01-10T15:48:49 | Routerich**
Здравствуйте.
Судя по логу, у вас zapret не работает.
А что вы хотите сделать?

---

**2026-01-10T16:00:39 | Василий**
уже кажется получилось, обновил через  загрузку пакетов Zapret   v72.20260108
после в Podkop отключил в секции YOUTUBE_DISCORD, сам дискорд, и ресетнул настройки выбрал стратегию 
# Strategy TLS_AUTO_ALT3_by_Flowseal и убрал Host lists Google hostname entries, оставив там домен заглушку, и наконецто у меня заработал 
Discord  через запрет, а всё остальное через Podkop

---

**2026-01-10T18:37:05 | Routerich**
https://github.com/remittor/zapret-openwrt/discussions/168

---

**2026-01-10T19:02:58 | Routerich**
Зайдите ещё в Система - планировщик и удалите там строчку где написано zapret log - нажмите применить

---

**2026-01-10T23:10:40 | Linar**
Можно чуть-чуть поподробнее. Это в графе Zapret надо что-то включить?

---

**2026-01-11T13:54:59 | Алексей**
Добрый день.Можно как то roblox пустить через zapret2.через podkop не хочет.

---

**2026-01-11T14:39:56 | Gomer Simpson**
Образ со всеми пакетами. Zapret2 обновлял позже.

---

**2026-01-11T14:45:18 | Egor Nepomnashi**
Zapret2, ютуб при установке сразу частично работает. . Не отрабатывает на тв LG, и SmartTube.   Если кто то решал подобные проблемы, подскажите

---

**2026-01-11T17:05:28 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.5.0r133 🚀 

  Новая функция:
  • proxy_router_traffic — маршрутизация трафика самого роутера через прокси (LuCI: Services → ZeroBlock → Router Traffic)

  Исправления:

  • Two-stage start — исправлена ошибка "port already in use" при двухэтапном запуске

  • DNS — исправлена работа DNS при включённом disable_fakeip на всех секциях

  • Zapret совместимость — разделение меток: direct-out (0x2) идёт в zapret, прокси используют 0x40000000

  • Port forwarding — трафик на проброшенные порты не перехватывается прокси (ct status dnat)

  • WireGuard/AWG — эндпоинты VPN исключены из маркировки в mangle_output

---

**2026-01-11T17:25:16 | Vasa**
если не хочется подкопов и прочего можно попроще вот
там ТГ найдете уже ссылку

https://github.com/GubernievS/AntiZapret-VPN

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

**2026-01-11T20:50:24 | Mallory**
Подскажите пожалуйста, перешёл на Zapret2 и перестал работать YouTube Revanced на дефолтных стратегиях и на найденных. В чем может быть проблема? Официальный YouTube работает.

---

**2026-01-11T22:44:12 | Vasa**
https://github.com/1andrevich/antifilter-geoip

https://github.com/1andrevich/antifilter-domain

https://github.com/savely-krasovsky/antizapret-sing-box

---

**2026-01-11T23:07:03 | Vasa**
вообще когда я людям делал, я ставил просто эти списки

https://github.com/1andrevich/antifilter-geoip

https://github.com/1andrevich/antifilter-domain

https://github.com/savely-krasovsky/antizapret-sing-box

вроде бы хватает всего в 90% случаев

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

**2026-01-12T01:19:21 | Борис**
Получается, есть ещё один способ для Remote Control - это xray-сервер на роутере, использующий некий шаблонный конфиг Vless. Преимущества:
1) Всегда работает, в отличие от Wireguard
2) Работает на телефоне, даже когда тот в режиме Белых списков и добрых сайтов
3) Работает как Exit node, разблокируя все сайты при помощи zapret и т.д. на телефоне (типа бесплатный "VPN")
4) Это бесплатно
Недостатки:
1) необходим белый IP
2) не все протоколы доступны в локальной сети
3) сложная настройка, нет инструкций

---

**2026-01-12T10:13:00 | Gomer Simpson**
Zapret'ы с этим гораздо лучше справляются.

---

**2026-01-12T10:33:53 | Sergey Solomatin**
ну да, стоит zapret...
но я щас поставил на вируталку без всего 
чтоб ни касперского там не было ни чего
такая же проблема :(

---

**2026-01-12T10:53:50 | Anna Bagler**
Не даёт скачать? Ставьте просто из пакетов. Система - Пакеты. Обновить списки. Потом в поле фильтра  zapret2 и ok. Установите zapret2 и luci-i18n-zapret2-ru.

---

**2026-01-12T11:02:26 | Mikhail Tikhomirov**
Да, в это поле вводите zapret2

---

**2026-01-12T11:31:49 | Тарас Смыслов**
As u wish.
Попробуйте насканить страт для запрета.
Запустить, после установки нажать 1 ввод.
Начнётся поиск. Он может быть долгим, если чо ложитесь спать.
Как закончит поиск нажмите 2 и ввод.
Будут предлагаться для проверки страты. Как зелёным напишет - запускайте на телефоне/телеке ютуб.
Не работает - ввод. Работает 1 и ввод.
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-01-12T11:35:03 | Anna Bagler**
Тогда youtubeUnblock отключайте и останавливайте в Система - Автозапуск. Ставьте zapret2 и проверяйте.

---

**2026-01-12T13:01:54 | Anna Bagler**
Посмотрите и уберите, если есть, чтоб не мешал. Если скрипт 5 запускали повторно до установки zapret2, то надо проверить отключение первой версии запрета.

---

**2026-01-12T14:44:07 | Gomer Simpson**
Так ставьте Z на роутер. Есть АВТОКОНФИГУРАТОР для Z1 и Blockcheck в Z2. Итого: WARP, proxy и Zapret работают параллельно и не мешают друг-другу.

---

**2026-01-12T15:19:20 | Mallory**
Интересно, что на первом запрете все идеально работает  (и старые RVX extended версии) на такой стратегии

# youtube
--filter-tcp=443
--hostlist=/opt/zapret/ipset/zapret-hosts-google.txt
--hostlist=/opt/zapret/ipset/zapret-hosts-user.txt
--hostlist-exclude-domains=openwrt.org
--dpi-desync=fake
--dpi-desync-fooling=badseq
--dpi-desync-fake-tls=0x00000000
--dpi-desync-fake-tls=!
--dpi-desync-fake-tls-mod=rnd,rndsni,dupsid

Как эту стратегию перенести из Z1 в Z2 я пока так и не освоил.

---

**2026-01-12T16:40:44 | Anna Bagler**
Запрет остановить, строку из Планировщика с zapret убрать. Список news в подкопе убрать. Проверить проблемные сайты.

---

**2026-01-12T16:45:00 | а к**
строку из Планировщика с zapret убрать вот это незнаю где

---

**2026-01-12T20:10:12 | Mallory**
А можно поставить одновременно zapret и zapret 2 и переключать их? Я в силу своей нубости так и не смог освоить второй, но научится хочется. Хочу поставить основным первый вариант и в свободное время экспериментировать со вторым

---

**2026-01-12T20:56:28 | Routerich**
Пользуйтесь zapret2 или в main перекиньте.

---

**2026-01-12T22:59:20 | Anatoly К**
https://github.com/remittor/zapret-openwrt/discussions/168
Я отсюда подставлял, поиском по lg. Завелось на webos lg, mac, ios, win android. 4k без тормозов.

---

**2026-01-13T03:55:47 | Mallory**
Да я тоже это заметил, как только удалил, заработал нормально Zapret

---

**2026-01-13T05:20:50 | AleXXXey**
Ссори, если вопрос покажется глупым или если не раз уже спрашивали. 

Планируется ли в 5м скрипте(или в последующих) замена zapret на zapret2? 

И ещё. 

Если не помог рефреш 5го скрипта (при работе с ютубом), поможет ли мне бета скрипт?

---

**2026-01-13T13:34:14 | Федор Седов**
Привет! Вроде прошивка актуально, но ничего из 3х перечисленных (подкоп, zapret, ytanblock) нету.Снова прошивку обновить нужно?

---

**2026-01-13T14:56:34 | Святос**
Из волнующих там разве что zapret2, с ним должно пройти?

---

**2026-01-13T14:58:26 | Святос**
Generate local signing keys...
Generate local certificate...
Package list missing or not up-to-date, generating it.

Building package index...
Downloading file:/local-repos/24.10.4/core/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/routerich_core
Downloading file:/local-repos/24.10.4/routerich/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/routerich
Downloading file:/local-repos/24.10.4/openwrt/base/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/openwrt_base
Downloading file:/local-repos/24.10.4/openwrt/luci/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/openwrt_luci
Downloading file:/local-repos/24.10.4/openwrt/packages/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/openwrt_packages
Downloading file:/local-repos/24.10.4/openwrt/routing/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/openwrt_routing
Downloading file:/local-repos/24.10.4/openwrt/telephony/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/openwrt_telephony
Downloading file:packages/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/imagebuilder
Collected errors:
 * check_data_file_clashes: Package luci-i18n-zapret2-ru wants to install file /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/usr/lib/lua/luci/i18n/zapret2.ru.lmo
  But that file is already provided by package  * luci-app-zapret2
 * opkg_install_cmd: Cannot install package luci-i18n-zapret2-ru.
make[2]: *** [Makefile:234: package_install] Error 255
make[1]: *** [Makefile:171: _call_manifest] Error 2
make: *** [Makefile:349: manifest] Error 2

---

**2026-01-13T19:01:11 | Сергей**
(Сейчас на пк хватает "zapret" для работы YT. ЧатГПТ и т.п. работают через TechnitiumDNS (подмена днс на DoH))

---

**2026-01-13T21:47:04 | Алексей**
Здравствуйте скажите где zapret2 загрузить

---

**2026-01-13T21:57:57 | Anna Bagler**
Пакеты, обновить списки, в поле фильтра zapret2, ok.

---

**2026-01-14T11:20:57 | Михаил**
Всем привет. Никто не сталкивался с тем, что на iOS в приложении youtube видео включаются долго(3-5сек)? На компьютере открывается моментально. 
Установлен на роутер только Zapret через Zapret Manager.

---

**2026-01-14T12:07:57 | Anna Bagler**
zapret - запрет 1, zapret2 - запрет 2.

---

**2026-01-14T12:08:31 | Nikolay**
У меня просто zapret, без цифр

---

**2026-01-14T12:15:47 | Vladimir**
У меня не всегда пакеты обновляются с первого раза, некоторые провайдеры могут блокировать доступ к репозитариям. В wiki по моему есть решение, ставим zapret из архива и настройки для доступа к обновлениям.
https://t.me/routerich/80283/356884?single

---

**2026-01-14T19:32:02 | Routerich**
Zapret/Zapret2 ставьте и стратегии перебирайте для ютуба

---

**2026-01-14T20:54:43 | Routerich**
Инструкцию не успели поправить. Ставьте пакет luci-app-zapret2

---

**2026-01-14T21:16:31 | Kirill K**
Пробовал вот такой скрипт sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_PR)

---

**2026-01-14T23:27:26 | Алексей**
Такой вопрос zapret2 поставил YouTube работает на всех устройствах кроме lg smart tv что делать?

---

**2026-01-15T10:07:15 | Routerich**
Здравствуйте.
Службы->Zapret оставновить, отключить автозапуск

---

**2026-01-15T10:07:36 | Routerich**
система->Планировщик->удалить строку с zapret, если она там есть

---

**2026-01-15T10:16:09 | Routerich**
система->Пакеты->zapret2->установлено->удалить

---

**2026-01-15T10:20:49 | Routerich**
Здравствуйте.
https://github.com/remittor/zapret-openwrt/discussions/168

---

**2026-01-15T10:23:09 | Routerich**
Попробуйте насканить страт для запрета.
Запустить, после установки нажать 1 ввод.
Начнётся поиск. Он может быть долгим, если чо ложитесь спать.
Как закончит поиск нажмите 2 и ввод.
Будут предлагаться для проверки страты. Как зелёным напишет - запускайте на телефоне/телеке ютуб.
Не работает - ввод. Работает 1 и ввод.
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-01-15T15:59:59 | Rikitikitavi**
Странно. Zapret я останавливал и отключал. Щас снова работает.

---

**2026-01-15T17:00:53 | Routerich**
Zapret отключить совсем временно. Далее проверить диагностику в подкопе с телефона

---

**2026-01-15T17:17:18 | Тарантино**
В Службах отключить Zapret?

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

**2026-01-15T22:44:55 | Gomer Simpson**
Zapret с АВТОКОНФИГУРАТОР вам может помочь. Или Zapret2.

---

**2026-01-16T06:54:01 | AleXXXey**
Всем привет) ✌️

Решился наконец-то поставить zapret2. И был приятно удивлен, как с ним Ютуб летает) в варпе он уже плохо себя чувствует. 

респект нашей тех поддержке РР🔥😎

Принцип такого обхода поверхностно понятен. Но я немного застопорился на списках) 

Как я это понимаю. Все домены, что указаны в этих списках, проходят через дурилку. И, соответственно, не должны пересекаться с доменами в подкопе. Но меня смутило имя списка user hosts exclude(точно не помню названия). Типа, исключения, верно? 
Если это исключения, то что этот список делает в списке для "обдуривания"?
Почитал инструкцию. Там, действительно подтвердилось, что именно этот список, как исключение работает. Но тогда, как за‌прет2 понимает, что этот список исключений, а тот для обдуривания, если они находятся в одном разделе?

---

**2026-01-16T09:15:51 | Юрий Теленков**
Установил и настроил zapret2, все работает! но, если в вебке (спустя какое-то время работы роутера) зайти в раздел zapret2, то страница наглухо зависает и хром выплевывает ошибку "страница не отвечает". Если туда не ходить, то все норм. Кто-то сталкивался с таким? Чтоб снова можно было зайти на страницу zapret2, помогает только ребут.

---

**2026-01-16T09:51:09 | Oleg Wer**
Здравствуйте! Хочу установить zapret2 ткните носом пжлст на инструкцию или ссылочку?

---

**2026-01-16T10:04:47 | Юрий Теленков**
может кто знает рабочую стратегию для zapret2 для webOS?

---

**2026-01-16T10:08:55 | Andrey Lazarev**
Глубокоуважаемая поддержка и члены сообщества, подскажите пожалуйста ответы на несколько вопросов:

1) Если есть желание опробовать zapret2, то нужно ли удалять с роутера пакеты, относящиеся к zapret, podkop и youtube_unblock.

2) В очередной раз "что-то пошло не так" и доступ к "ТыТрубе" пропал сегодня. Если хочется переустановить нужные пакеты (скрипт №5) - нужно ли предварительно удалять пакеты, как и в первом вопросе, zapret-podkop-uy_unblock?

3) Каков минимальный необходимый набор пакетов для деблокирования доступа к YT и популярным игровым сервисам? Достаточно ли будет поставить zapret2 если у меня народ не только YT и связанные с Мета сервисы использует, но и в игры играет (Battlefield, Elite Dangerous - последняя, как я понимаю, частично на облако Амазона опирается, но могу ошибаться)?

---

**2026-01-16T10:19:52 | Юрий Теленков**
но сейчас ккакое-то странное поведение, zapret2 работает 30 сек (+-), а потом вырубается, но в эти 30 сек ютуб работает

---

**2026-01-16T10:27:38 | Юрий Теленков**
да, т.е я не вижу причины почему запрет самопроизвольно стопится, смотрю в лог /tmp/zapret2/main.log

---

**2026-01-16T10:31:13 | Routerich**
/opt/zapret2/nfq/nfqws2 -v

---

**2026-01-16T10:31:51 | Юрий Теленков**
вот когда запустил опять root@RouteRich:~# ps |grep nfqws
 8237 daemon    1380 S    /opt/zapret2/nfq2/nfqws2 --debug=@/tmp/zapret2/main.log --user=daemon --fwmark=0x40000000 --lua-init=@/opt/zapret2/lua/
 8238 daemon    1360 S    /opt/zapret2/nfq2/nfqws2 --debug=@/tmp/zapret2/50-discord_media.log --user=daemon --fwmark=0x40000000 --lua-init=@/opt/
 8239 daemon    1360 S    /opt/zapret2/nfq2/nfqws2 --debug=@/tmp/zapret2/50-quic4all.log --user=daemon --fwmark=0x40000000 --lua-init=@/opt/zapre
 8240 daemon    1360 S    /opt/zapret2/nfq2/nfqws2 --debug=@/tmp/zapret2/50-stun4all.log --user=daemon --fwmark=0x40000000 --lua-init=@/opt/zapre
 8306 root      1336 S    grep nfqws
root@RouteRich:~#

---

**2026-01-16T10:32:52 | Юрий Теленков**
нет такого root@RouteRich:~# /opt/zapret2/nfq/nfqws2 -v
-ash: /opt/zapret2/nfq/nfqws2: not found
root@RouteRich:~#

---

**2026-01-16T10:33:24 | Routerich**
/opt/zapret2/nfq2/nfqws2 -v

---

**2026-01-16T10:36:52 | Юрий Теленков**
обновил, но все равно падает. root@RouteRich:~# cat /proc/$(pgrep -o nfqws2)/cmdline | tr '\0' '\n'
/opt/zapret2/nfq2/nfqws2
--debug=@/tmp/zapret2/main.log
--user=daemon
--fwmark=0x40000000
--lua-init=@/opt/zapret2/lua/zapret-lib.lua
--lua-init=@/opt/zapret2/lua/zapret-antidpi.lua
--lua-init=@/opt/zapret2/lua/zapret-auto.lua
--qnum=300
--lua-gc=600
--blob=blob_tls_clienthello_www_google_com:@/opt/zapret2/files/fake/tls_clienthello_www_google_com.bin
--blob=blob_tls_clienthello_t2_ru:@/opt/zapret2/files/fake/tls_clienthello_t2_ru.bin
--blob=blob_tls_clienthello_vk_com:@/opt/zapret2/files/fake/tls_clienthello_vk_com.bin
--blob=blob_tls_clienthello_gosuslugi_ru:@/opt/zapret2/files/fake/tls_clienthello_gosuslugi_ru.bin
--blob=blob_tls_clienthello_www_4pda_to:@/opt/zapret2/files/fake/tls_clienthello_www_4pda_to.bin
--blob=blob_tls_clienthello_www_max_ru:@/opt/zapret2/files/fake/tls_clienthello_www_max_ru.bin
--name=youtube
--filter-tcp=443
--filter-l3=ipv4
--filter-l7=tls
--hostlist=/opt/zapret2/ipset/zapret_hosts_youtube.txt
--hostlist=/opt/zapret2/ipset/zapret_hosts_youtube_music.txt
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=fake_default_tls:badsum:tls_mod=sni=rzd.ru:repeat=4
--lua-desync=multisplit:blob=fake_default_tls:badsum:pos=2:nodrop
--lua-desync=fakedsplit:pos=method+2:tcp_flags_set=SYN:repeat=2
root@RouteRich:~#

---

**2026-01-16T11:19:45 | Navisal**
Стратегия zapret2 только для Youtube, работает на всех девайсах, включая "Яндекс ТВ станция Basic" с ее встроенным Ютуб-клиентом, провайдер Ростелеком:

--lua-desync=fake:blob=0x00000000:repeats=2:tcp_seq=-10000
--lua-desync=fake:blob=fake_default_tls:repeats=2:tcp_seq=-10000:tls_mod=rnd,dupsid,sni=www.google.com
--lua-desync=multisplit:pos=1,midsld

---

**2026-01-16T14:37:24 | Әмир**
Кто-нибудь может поделиться настройками Zapret или Zapret2 для работы дискорда на Ростелекоме?

---

**2026-01-16T15:43:49 | Routerich**
он пока на тестах, прост вкину.

ZeroBlock 0.6.0-r1: Масштабная оптимизация завершена

  Завершена большая работа по оптимизации ZeroBlock — замена shell-вызовов на нативный C код.

  📊 Результаты:
  - Было: ~114 вызовов bash
  - Стало: 62 вызова
  - Заменено: 52 вызова на нативный C

  ⚡️ Что было оптимизировано (20 фаз):

  Файловые операции:
  • mkdir -p, rm -rf, which → POSIX функции
  • sysctl -w → прямая запись в /proc/sys

  Сетевые операции:
  • ping → raw ICMP socket
  • ip route/rule → libmnl (Netlink)
  • ip addr, ip link → getifaddrs(), Netlink
  • netstat, nslookup → /proc/net/tcp, getaddrinfo()

  HTTP запросы:
  • curl → libcurl (http_client.c)
  • Clash API, GitHub проверки, DPI checker — всё через нативный HTTP

  Логирование:
  • logread | tail, tail -n → прямое чтение файлов

  UCI конфигурация:
  • uci get/show → libuci API

  NFTables:
  • nft команды → libnftables

  Последняя фаза (20):
  • zapret_manager.c: curl → http_get(), ls → readdir()+fnmatch()

  🔧 Дополнительные исправления:
  • Парсинг доменов в пользовательских списках теперь поддерживает запятые как разделитель (раньше только переводы строк)
  • Исправлена категоризация логов для zeroblock/singbox
  • Логи zeroblock/singbox пишутся теперь в системный лог вместе согласно настройкам
  • Исправлено отображение имени серверов в подписке
  • Исправлено поведение опции "Отключить FakeIP"
  • Исправлено поведение кнопки перезапустить(в некоторых случаях она могла не сразу обновлять свой статус)
 
  💡 Преимущества:
  - Меньше fork/exec накладных расходов
  - Быстрее выполнение на слабых роутерах
  - Меньше зависимостей от shell утилит
  - Более надёжная обработка ошибок
#ZeroBlock

---

**2026-01-16T16:54:01 | Ванечкхап**
не могу найти Опции NFSQWA. 

в zapret2->Настройки с этими буквами есть NFQWS PORTS TCP и. PORTS UDP.

Опции или OPTIONS нету. в других вкладках тоже не нашел.

---

**2026-01-16T19:21:53 | Anna Bagler**
Нет, там где zapret restart есть в строке, обновление списков подкопа не трогайте.

---

**2026-01-16T19:27:46 | Anna Bagler**
В система - планировщик строчки со словами zapret найти и удалить, сохранить.

---

**2026-01-16T19:28:16 | Vladislav (NexHav)**
0 4 * * * service zapret restart
эта строчка?

---

**2026-01-16T19:35:14 | Sir**
А когда ждать скрипт #6 с Zapret2 ???
🤔

---

**2026-01-16T19:36:34 | Routerich**
Будет зероблок + zapret 2

---

**2026-01-16T19:38:37 | Andrey Lazarev**
Уважаемая поддержка и эксперты, снова нужна ваша помощь, не хватает знаний :(

Поставил после рекомендаций сегодняшних zapret2 (отдельная благодарность за мануал!) - но никак не пойму, как бы включить "обход" ("доступ"??) для серверов amazon/cloudflare, к которым идет подключение по 5222 портам (вроде бы только UDP). Это игровые сервера Elite Dangerouse. Со стратегиями "из коробки" не пашет. Списки хостов я вроде как добавил в /opt/zapret2/ipset/zapret_hosts_user.txt через CLI - но не пашет 😞

---

**2026-01-16T20:06:58 | Усатый Бро**
Нету в спике zapret или у него другное название?

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

**2026-01-16T20:47:39 | Anna Bagler**
Система - Пакеты, обновить списки, в поле фильтра zapret и ok. Дальше смотрите, что вам надо.

---

**2026-01-16T21:02:32 | Михаил**
Всем привет! Подскажите, кто нибудь сталкивался с тем, что на мобильном устройстве(iOS) на чистой актуальной прошивке роутера с zapret(установил через Zapret Manager) видео и шортсы открываются с задержкой? 
На ПК и на телефоне(браузер) открывается все идеально быстро, а вот в мобильном приложении youtube есть 3-5 секунды задержки при включении видео/шортса(сама скорость загрузки видео быстрая, 2к видео моментально грузит при перемотке)?

---

**2026-01-16T21:03:53 | Михаил**
youtubeUnlocker и прочих аналогов Zapret’a нет
Настройки Zapret проставлены из скрипта Zapret Manager

---

**2026-01-16T21:06:16 | Михаил**
Пытался и на Zapret и на youtubeUnlocker, перебирал разные стратегии из публичного доступа(более 30шт), задержка осталась

---

**2026-01-16T21:12:00 | Михаил**
Там как будто проблема в том, что в приложении есть какие то оптимизации для загрузки, и они ломаются при включении Zapret

В целом терпимо, тем более что рекламы нет)

---

**2026-01-16T21:59:19 | Кирилл Евсеев**
может отключить запрет и поставить ютубанблок ?
на 2м скрипте раньше все отлично работало
а для чего вообще zapret, я до сих пор не могу понять?

---

**2026-01-16T22:04:22 | Кирилл Евсеев**
кстати при установке скрипта, при проверке zapret - 2 минуты была проверка, а потом написало что-то типа "zapret doesnt work", но установка продолжилась дальше

---

**2026-01-16T22:56:16 | ユージーン**
Доброй ночи.
на Zapret 1 работает для игр вот эта стратегия:
--filter-udp=1024-65535
--dpi-desync=fake
--dpi-desync-cutoff=d2
--dpi-desync-any-protocol=1
--dpi-desync-fake-unknown-udp=/opt/zapret/files/fake/quic_initial_www_google_com.bin
как её перенести в Zapret2_0.8.4

сделал так, но не работает

---

**2026-01-16T23:38:23 | Routerich**
Пробуйте другие стратегии, или zapret2 с блокчеком, через блокчек подбирая стратегию

---

**2026-01-17T02:10:13 | Routerich**
Система - автозапуск - найти zapret и нажать на включено и на стоп и проверить работу всего

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

**2026-01-17T02:31:02 | None**
и запрет1 не работает и подкоп, единственное, что работает это zapret2, но я не уверен можно ли с него зарегистрироваться в инсте и сидеть спокойно.

---

**2026-01-17T12:42:33 | Dmitriy M 🎃**
Adding to nfset zapret : /opt/zapret/ipset/zapret-ip.txt /opt/zapret/ipset/zapret-ip-user.txt  
Adding to nfset ipban : /opt/zapret/ipset/zapret-ip-ipban.txt /opt/zapret/ipset/zapret-ip-user-ipban.txt  
Adding to nfset nozapret : /opt/zapret/ipset/zapret-ip-exclude.txt   
Inserting nftables ipv4 rule for nfqws postrouting (qnum 200) : tcp dport {80,443} ct original packets 1-9
Error: syntax error, unexpected !=
insert rule inet zapret postnat oifname @wanif mark and != 0 tcp dport {80,443} ct original packets 1-9 ip daddr != @nozapret meta mark set meta mark or 0x20000000 ct mark set ct mark or 0x40000000 queue num 200 bypass
                                                        ^^
Error: syntax error, unexpected !=
add rule inet zapret flow_offload mark and != 0 tcp dport {80,443} ct original packets 1-9 ip daddr != @nozapret return comment "direct flow offloading exemption"
                                           ^^
Inserting nftables ipv4 rule for nfqws prerouting (qnum 200) : tcp sport {80,443} ct reply packets 1-3
Inserting nftables ipv4 rule for nfqws postrouting (qnum 200) : udp dport {443} ct original packets 1-9
Error: syntax error, unexpected !=
insert rule inet zapret postnat oifname @wanif mark and != 0 udp dport {443} ct original packets 1-9 ip daddr != @nozapret meta mark set meta mark or 0x20000000 ct mark set ct mark or 0x40000000 queue num 200 bypass
                                                        ^^
Error: syntax error, unexpected !=
add rule inet zapret flow_offload mark and != 0 udp dport {443} ct original packets 1-9 ip daddr != @nozapret return comment "direct flow offloading exemption"
                                           ^^
Inserting nftables

---

**2026-01-17T13:07:32 | Bullet for my valentine Poison**
выше ваш скрин, что напротив luci-app-zapret2?

---

**2026-01-17T15:07:20 | Routerich**
Ну тогда щупайте zapret2 или добавляйте в первую секцию YouTube, только из второй удалить

---

**2026-01-17T16:49:13 | Dmitry**
Вечер добрый. Установил скрипт 5, всё ок. Подшаманил с своими доменами в podkop. До этого стоял только ютубанблок. Я так понимаю что ютубанблок и установившийся со скриптом zapret, в принципе, можно удалить?

---

**2026-01-17T17:15:27 | Routerich**
Здравствуйте.
А если стопнуть Podkop, Zapret так же все?

---

**2026-01-17T17:24:06 | ㅤ ㅤ**
Встает только Zapret

---

**2026-01-17T18:12:14 | Александр Меркушев**
Добрый вечер. Спасибо большое, остановка запрета помогла. Просто в голову не приходило, что в нем может быть дело. 2 недели мучался, а все решалось одним кликом. Перезапустил 5й скрипт, заметил в консоле zapret not working.  При этом труба странным образом работает

---

**2026-01-17T18:13:08 | Routerich**
Не через Zapret

---

**2026-01-17T21:02:22 | Alexey**
Конкретные ссылки нужно предоставить? Еще хотел уточнить, нужно ли качать и устанавливать пакеты zapret2 после установки 5-го скрипта?

---

**2026-01-18T13:24:17 | OlegPers**
Добрый, подскажите как ютуб починить без 5 скрипта (уже стоит) и без zapret2? или уже нужен запрет 2 в любом случае?

---

**2026-01-18T14:19:16 | Routerich**
я использую zeroblock+zapret2 на постоянной основе и сам нахожу глубокие косяки в правилах nft, остальное находят пользователи по примеру вашего фидбека о селекторе или кастомного path в днс. и могу сказать что связка работает стабильно

---

**2026-01-18T15:06:43 | Wenzel Perminov**
проблема с zapret'ом. Zapret стал ломать интернет, на гитхабе людям с той же проблемой предлагают сменить стратегию, я сменил и через пару дней снова включение zapreta ломает интернет. С zapret2 вроде такого не происходит, но стратегия по умолчанию для ютуба работает не стабильно, открывается все через раз. У кого есть для zapret2 стабильные стратегии для ютуда, сам я так и не понял по какому принципу стратегии подбирают

---

**2026-01-18T15:16:48 | Wenzel Perminov**
для zapret есть готовые стратегии, есть хоть что перебирать, для zapret2 как то не густо, видимо вокруг него нет комьюнити пока активного

---

**2026-01-18T15:31:21 | Kiss_My_Axe**
Для запрет есть сканер стратегий. Он их в автомате ищет и в полуавтомате применяет.
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

В запрет2 сканер стратегий вообще встроен. Рыть инет в поисках страт - прошлый век.

---

**2026-01-18T16:10:11 | Kiss_My_Axe**
Для нормального поиска надо отключить все обходы. Запреты оба, ютубанблок и прочие антидипиай-системы, как минимум.
Из подкопа убрать ютуб.

Вообще в текущем варианте автоконфиг ищет страты только для ютуба. Если необходимо всё гонять через запрет, то либо запрет2, либо zapret4rocket.
Но с z4r могут всплыть проблемы с некоторыми сайтами. Однако да, он прям волшебство творит.

---

**2026-01-18T17:13:34 | Борис**
А Zapret2 и podkop будут включать в реестр отечественного ПО?

---

**2026-01-18T18:16:56 | Kirill Y**
Подскажите. Хотел заново всё настроить.Сделал сброс на заводские настройки. После перезагрузки  в службах есть и podkop и zapret. Это нормально?

---

**2026-01-18T18:44:10 | Виктор**
Приветствую! Только вчера подключил роутер, информации море, не знаю что важно, а что нет. Начал с установки zapret2, к сожалению доступ к сайтам не появился, мало того перестал работать BueBueDPI на Андроиде. Что делал: подобрал стратегии в Blockcheck2, вставил строчки в стратегию default (настройки на скрине). Что еще пробовать? Подробнее пожалуйста.

---

**2026-01-18T18:47:51 | Виктор**
zapret пока отключить?

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

**2026-01-18T20:01:19 | Андрей**
установил со 2 попытки (после удаления пакетов Zapret2),

---

**2026-01-18T20:01:53 | Святос**
Пакет перевода Zapret 2 мешает

---

**2026-01-18T20:06:19 | Андрей**
как скачать zapret2?

---

**2026-01-18T20:08:33 | Андрей**
Installing zapret2 (0.8.4-r2) to root...
Downloading https://github.com/routerich/packages.routerich/raw/24.10.4/routerich/zapret2_0.8.4-r2_aarch64_cortex-a53.ipk
Installing kmod-nfnetlink-queue (6.6.110-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/targets/mediatek/filogic/kmods/6.6.110-1-6a9e125268c43e0bae8cecb014c8ab03/kmod-nfnetlink-queue_6.6.110-r1_aarch64_cortex-a53.ipk
Installing kmod-nft-queue (6.6.110-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/targets/mediatek/filogic/kmods/6.6.110-1-6a9e125268c43e0bae8cecb014c8ab03/kmod-nft-queue_6.6.110-r1_aarch64_cortex-a53.ipk
Installing gzip (1.14-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/gzip_1.14-r1_aarch64_cortex-a53.ipk
Installing libpcap1 (1.10.5-r2) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/base/libpcap1_1.10.5-r2_aarch64_cortex-a53.ipk
Installing ncat (7.95-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.4/packages/aarch64_cortex-a53/packages/ncat_7.95-r1_aarch64_cortex-a53.ipkKeeping existing /opt/zapret2/ipset/zapret_hosts_user_exclude.txt
Keeping existing /opt/zapret2/ipset/zapret_hosts_youtube.txt
Starting zapret2...
Config generated: /opt/zapret2/config
Strategies: 2

Configuring kmod-nfnetlink-queue.
Configuring kmod-nft-queue.
Configuring gzip.
Configuring libpcap1.
Configuring ncat.
Configuring zapret2.
Ошибки
Collected errors:
 * resolve_conffiles: Existing conffile /etc/config/zapret2 is different from the conffile in the new package. The new conffile will be placed at /etc/config/zapret2-opkg.
 * resolve_conffiles: Existing conffile /opt/zapret2/config is different from the conffile in the new package. The new conffile will be placed at /opt/zapret2/config-opkg.

---

**2026-01-18T21:49:13 | Денисов Егор**
а есть гайды или может уже задавили вопросы - не нашел, как почистить хвосты от zapret? службу остановил и удалил перед установкой скрипта

---

**2026-01-19T15:35:51 | ユージーン**
Добрый день !
Подскажите как завести игры с Zapret 2
делаю новый блок с
--out-range=-d2
--lua-desync=fake:blob=blob_quic_initial_www_google_com
ставлю UPD
1024-65535
галочка в blob стоит
но не чего не заводится

---

**2026-01-19T17:44:16 | Владимир Греков**
Установил через веб интерфейс. В службах zapret2 не появился

---

**2026-01-19T17:48:36 | ユージーン**
Раз уж речь пошла про Zapret 2, подскажите как сделать, что-бы игры BF6 и Roblox стали работать...
https://t.me/routerich/3845/445628

---

**2026-01-19T17:49:16 | Владимир Греков**
zapret 2 и luci-app-zapret 2 установил, 3 пакет не устанавливается, пишет что не доступен

---

**2026-01-19T18:18:55 | Михаил Полиенко - Инвестиции в бизнес**
У меня на мобильном Google Chrome выдается подборка интересных страниц.
Когда подключаюсь к RouteRich - ее невозможно обновить, он долго думает, в итоге выдает, что доступа нет. Приходится переключаться на мобильный.
Прошивка 24.10.4
Работает Podkop настроен по скрипту №5. Zapret и youtubeunblock отключены.

---

**2026-01-19T19:29:22 | Степан Тарасов**
здраствуйте, можно ли как то настроить zapret что бы работал roblox

---

**2026-01-19T20:39:43 | Linar**
Подскажите где инструкция для установки Zapret2 ?

---

**2026-01-19T20:40:41 | Святос**
В Крылатском тоже Zapret not work

---

**2026-01-19T20:42:33 | Роман**
Система - Пакеты - обновить списки. Фильтр zapret2 - установить 2 пакета, перезайти в web интерфейс.

---

**2026-01-19T21:20:44 | Святос**
https://github.com/Flowseal/zapret-discord-youtube/issues/7381

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

**2026-01-20T11:44:01 | Vasa**
https://github.com/GubernievS/AntiZapret-VPN

---

**2026-01-20T12:18:35 | Routerich**
если у вас в Zapret прописан ютуб, то да.

---

**2026-01-20T12:25:43 | Сергей**
podkop zapret

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

**2026-01-20T16:22:00 | Kiss_My_Axe**
Если zapret не используете, то в Система - Планировщик удалить запись о перезапуске zapret. Нажать Сохранить.
Подкоп - Настройки, сменить adguard DNS на Google DNS. Но это по вашему выбору. Либо меньше рекламы и больше глюков, либо больше рекламы и меньше глюков.

---

**2026-01-20T19:02:39 | Routerich**
Удалите список ютуб из секции дискорд, у вас warp не работает, zapret2 перезапустите. Пока подождите - возможно warp через время заработает

---

**2026-01-20T20:34:40 | Панда**
zapret/sing-box и тд глняь

---

**2026-01-20T20:55:54 | Routerich**
zapret донатим

---

**2026-01-20T21:51:01 | Routerich**
кстати, не относится к теме, но тут чище всего. из-за того, что варп маскируется под quic, у zapret2 каменеет пониже живота и он начинает трогать handshake из-за чего ломается варп. выхода пока знаю два:
удалить quic.sh скрипт
удалить I1 параметр и обмазаться wg4all.sh скриптом из оригинальной репы запрет2

---

**2026-01-21T00:41:52 | Kiss_My_Axe**
Можно насканить страт для запрета этим:
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)
А можно остановить и отключить запрет и в секцию дискорд подкопа добавить список ютуб.

---

**2026-01-21T02:42:40 | Святос**
Вот у меня дома не надо настраивать запры, отъедешь в соседний район - Zapret not work

---

**2026-01-21T09:28:39 | Routerich**
Здравствуйте.
скорее всего что-то подкрутили.
попробуйте подобрать стратегию для zapret, так как ютуб у вас через него

---

**2026-01-21T13:02:57 | Kirill K**
Здравствуйте! Подскажите, пожалуйста, где предпочтительнее удалить запись об Youtube, чтобы не было конфликтов, в Podkop или Zapret? Пробовал в Podkop удалять запись и перезагружать роутер, доступ к Ютуб пропадал. Может мало ждал по времени пока сервисы поднимуться.  Так же в в домашней сети стали появляться частые отвалы доступа к Интернету.

---

**2026-01-21T13:31:08 | Andrew Arzaev**
Всем здравствуйте!
Подскажите пожалуйста, а zapret2 нужно будет отдельно устанавливать или он есть в каком то скрипте установки ?

---

**2026-01-21T13:38:35 | Andrew Arzaev**
Вот такой вопрос, в zapret2 есть предустановленные скрипты - они уже применены или нет ?
Будет ли как раньше скрипт для установки всего (подкоп или зероблок с новым запретом)?
Нужно ли отключать другие списки если включаю Autohostlist ?

---

**2026-01-21T13:41:03 | Андрей**
Последний zapret2 так и должен выглядеть ? До обновления итерфейс был другой.

---

**2026-01-21T13:48:03 | Борис**
проблема действительно в серверах гугла. Я вот, например, врубаю Zapret2 и помогаю этим серверам корректно работать - они сразу прогружают мне все видео за секунду

---

**2026-01-21T13:49:33 | Борис**
там правда, сама программа Zapret2 шлёт такой трафик, который оборудование моего интернет-провайдера неспособно опознать, но сами сервера ютуба опознают мой трафик прекрасно, но это уже вопрос десятый...

---

**2026-01-21T14:46:14 | Vasa**
у меня ж этот проект развернут

https://github.com/GubernievS/AntiZapret-VPN

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

**2026-01-21T15:14:52 | Kiss_My_Axe**
zapret-ip2net
zapret-mdig
zapret-tpws
Это, если не используете, удалить.
По софту норм, просто иногда устанавливают всё подряд и покаааа оно запустится можно помереть.

Сделать хард-ресет, зубочистка, кнопка ресет сзади.
Затем не внося никаких изменений в настройки пару раз ребутнуть роутер с замером времени ребута.
Если и на голом роутере время запуска 3-4 минуты, то проблема, скорее, хардварная.

---

**2026-01-21T15:59:20 | Михаил**
А с zapret дружит zeroblock?

---

**2026-01-21T16:07:26 | Kirill K**
Чтобы Вы посоветовали?                       1. Удалил  запись Youtube (в секции Youtube_Discord) в Podkop и перезагрузил роутер: уровень сигнала Wi-Fi очень слабый, 
youtube на телевизорах работает с большими зависаниями, на телефоне youtube в бесконечной загрузке, на компьютере даже через Tail работает, сбои в работе телеграмм.
2. Вернул запись Youtube (в секции Youtube_Discord) в Podkop, остановил Zapret и выключил его из автозагрузки: Youtube на телевизоре и телефоне работает с частыми подвисаниями по 3 - 5 минут, телеграмм тоже часто отваливается.
Оба варианта тестировал минут через 10 после перезагрузки роутера, минут по 15 каждый.
Zapret сбрасывал на дефолтные настройки перед тестированием.
Обратил внимание, что в последнее время уровень сигнала Wi-Fi сети сильно снизился, точнее стал нестабильным: то слабый сигнал, то сильный сигнал.

---

**2026-01-21T16:10:05 | Антон**
Вроде все норм работает с StressOzz/Zapret-Manager

---

**2026-01-21T17:28:25 | Routerich**
zapret2

---

**2026-01-21T17:49:55 | Routerich**
Установите zapret2 и уже будет дефолтный конфиг и на гитхаб идти не надо

---

**2026-01-21T17:56:36 | Михаил**
Действительно помогло, огромное спасибо!

Вообще крутой инструмент, с помощью него удалось избавиться от задержки при открытии видео через iOS приложение youtube(задержка появлялась после Zapret'a или аналога)

Возможно, кому-то поможет

1) Устанавливаете zeroblock
2) ZeroBlock -> Автонастройка -> Галочка на WARP
3) ZeroBlock -> Секции маршрутизации -> для awg10(он же WARP) в списки добавляете Youtube
4) В этой же секции можете прокинуть исключения, чтобы только телефон ходил через WARP в Youtube(если с остальными устройствами все ок)
4) Если есть свой AWG VPN, то добавляете его сначала в Сеть -> Интерфейсы, а потом и в Секции маршрутизации, и настраиваете необходимые списки под ваши требования
5) Устанавливаете Zapret или youtubeUnlocker и тд

В итоге получаете молниеносный Youtube на iOS(идет через WARP, а значит рекламы не будет), на ПК и остальных устройствах Youtube работает через Zapret

Огромное спасибо команде Роутерич за помощь!

---

**2026-01-21T17:59:03 | Routerich**
Zapret2 для всех

---

**2026-01-21T18:00:25 | zloybob**
root@OpenWrt:~# opkg install zapret2
Unknown package 'zapret2'.
Collected errors:
 * opkg_install_cmd: Cannot install package zapret2.

---

**2026-01-21T18:13:46 | Михаил**
Без подкопа, верно, но чтобы варп заработал, мне нужен был zapret(иначе не коннектит)

---

**2026-01-21T18:18:37 | Михаил**
Если сложно, можешь попробовать на чистый роутер без youtubeUnlocker накатить Zapret Manager, выбираешь 8ой пункт в скрипте, и все за тебя делается

У многих знакомых все завелось без бубнов)

---

**2026-01-21T19:33:39 | Kiss_My_Axe**
Список Discord убрать либо из main, либо из Discord  в подкопе.
Список Cloudflare из main подкопа убрать, он мешает работе awg10, через который у вас пущен Discord по второй секции подкопа.
Подкоп - Настройки, DNS adguard заменить на гугл (если адгард не сами включили, чтобы рекламу резало).
Система - Планировщик. Удалить 0 4 * * * service zapret restart нажать Сохранить.

---

**2026-01-21T20:28:31 | Anna Bagler**
Для запрета есть такое.
Попробуйте насканить страт для запрета.
Запустить, после установки нажать 1 ввод.
Начнётся поиск. Он может быть долгим, если чо ложитесь спать.
Как закончит поиск нажмите 2 и ввод.
Будут предлагаться для проверки страты. Как зелёным напишет - запускайте на телефоне/телеке ютуб.
Не работает - ввод. Работает 1 и ввод.
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-01-21T21:36:09 | Александр Меркушев**
Добрый вечер, думаю все же попробовать. Хочется чем-то помочь в разработке хоть немного. Не совсем понял, если вот так обновиться - это надо 5й скрипт будет запускать или тот, который из бета? И Подкоп отдельно ставить или там вшит аналлог, ZeroBliock уже сразу? И еще - Zapret 2 скриптом сам настроится как с 5м скриптом или шаманить ручками надо?

---

**2026-01-21T21:57:05 | Kiss_My_Axe**
Система - Пакеты, Обновить списки, Фильтр zapret2
Куды вас всё время труба зовёт то?

---

**2026-01-21T22:03:13 | Routerich**
--out-range=-s34228 \
--payload=tls_client_hello \
--in-range=-s5556 --lua-desync=circular:fails=2:time=60 \
--in-range=x \
--lua-desync=fake:blob=0x00000000:tcp_ack=-66000:strategy=1 \
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:tls_mod=rnd,dupsid,rndsni,padencap:tcp_ack=-66000:strategy=1 \
--lua-desync=multisplit:pos=2,endhost:strategy=1 \
--lua-desync=multisplit:pos=1:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:ip_id=zero:strategy=2 \
--lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=3 \
--lua-desync=multisplit:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=4 \
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=fonts.google.com:strategy=5 \
--lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=5 \
--lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=5 \
--lua-desync=multidisorder:pos=7,sld+1:strategy=6 \
--lua-desync=multidisorder:pos=1,midsld,endhost-1:strategy=7 \
--lua-desync=fake:blob=0x00000000:tcp_seq=-10000:tcp_ack=-66000:repeats=2:strategy=8 \
--lua-desync=fake:blob=fake_default_tls:tcp_seq=-10000:tcp_ack=-66000:repeats=2:tls_mod=rnd,dupsid,sni=www.google.com:strategy=8 \
--lua-desync=multisplit:pos=1,midsld:strategy=8 \
--lua-desync=multidisorder:pos=1,midsld:strategy=9 \
--lua-desync=multisplit:pos=1,2:seqovl=4:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=10 \
--lua-desync=multidisorder:pos=2,5,105,host+5,sld-1,endsld-5,endsld:strategy=11 \
--lua-desync=fake:blob=0x0F0F0F0F:badsum:tcp_seq=-10000:tcp_ack=-66000:strategy=12 \
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:badsum:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=12 \
--lua-desync=multisplit:pos=2,sld:seqovl=2108:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=12:final

дефолт стратегия zapret2. Заработает у вас конкретно или нет никто не знает

---

**2026-01-21T22:13:30 | пам пам**
Как вычислять домены, куда посылаются запросы при заходе на сайт, чтоб закинуть их в хостлист zapret'а?

---

**2026-01-22T00:14:21 | Routerich**
система - планировщик, удалить строку про zapret

---

**2026-01-22T08:31:22 | Routerich**
если проверка покажет что zapret работает, то ютуб через него будет.
но там просто zapret, не zapret2

---

**2026-01-22T09:21:36 | Yaroslav**
Привет. Перестал работать доступ по RDP к моим ВДС. Это может быть связано с настройками в роутере, хотя я ничего там не менял (установлены zapret и podkop)? При смене провайдера на мобильный интернет (не через роутер, через раздачу интернета через моб. телефон) доступ к ВДС восстанавливается. Где искать, почему доступ по RDP к ВДС пропал?

---

**2026-01-22T16:16:01 | Олег Михайлович**
Всем доброго времени суток, вчера на роутер поставил zapret2, сегодня начал дальше разбираться что к чему, через 2-3 секунды страница роутера намертво виснет(инкогнито пробовал), затем не работает WhatsApp и Xbox

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

**2026-01-22T16:57:08 | Kiss_My_Axe**
В подкопе, секция Ютуб_Дискорд. Убрать список ютуб. Сохранить, Применить.
Службы - zapret - Включить, Запустить.
Проверить ютуб с компа (скорее всего вообще не заработает).

В терминале роутера:
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

Инструкция:
Запустить, после установки нажать 1 ввод.
Начнётся поиск.
Как закончит поиск нажмите 2 и ввод.
Будут предлагаться для проверки страты. Как зелёным напишет - запускайте на телефоне/телеке ютуб.
Не работает - ввод. Работает 1 и ввод.

---

**2026-01-22T20:07:00 | Routerich**
Ну да, там используется первый zapret.

---

**2026-01-22T23:09:55 | Amras Amandil**
Крч, для понимания - на компе работает ) Уот это пробовал - не робит -> 
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)
. Может есть скрипт для диагностики?

---

**2026-01-22T23:11:41 | Amras Amandil**
Понял, пока мучаю скрипт выше - 
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-01-23T08:33:30 | Routerich**
Здравствуйте.
проверьте на компьютере не включен ли частный днс, безопасный днс в браузере, сторонние программы (типо zapret,warp) чтобы были отключены

---

**2026-01-23T11:59:55 | Николай**
Привет! Подскажите, есть где-то инструкция как настроить Zapret/Podkop для доступа к пользовательскому домену, например к kb.asipto.com?

---

**2026-01-23T12:04:30 | Николай**
А как понять какая секция нужная?)) Я попробовал создать свою такого типа, но там требуется vless///
P.S. У меня Zapret и Podkop настроены по дефолту
P.S.1 Также пробовал добавлять домен в имеющиеся секции в пользовательские списки, не помогло

---

**2026-01-23T18:27:59 | Vladimir Frait**
установливаю через терминал подкод в приложение не показывает подкопа показывает только zapret

---

**2026-01-24T04:40:45 | Kiss_My_Axe**
Обычно помогает рестарт интерфейса awg10, но можно попробовать по третьей ссылке перенакатить, вреда не будет.
У меня вообще ютуб везде работает и через zapret, и через zapret2. Пока.
Ну и на всякий случай запустите тестовый скрипт, скрин результата пришлите.
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/test_config_script/test_config_script_nightly)

---

**2026-01-24T08:41:02 | AleXXXey**
Всё. Починил работу и загрузку play market/гугл-сервисов.

(!!!)Актуально тем, у кого запрет2.

Из zapret_hosts_youtube.txt удалил следующие домены: 

play.google.com
google-analytics.com
googleusercontent.com
gstatic.com
gvt1.com
gvt2.com
gvt3.com
ggpht.com

Перезагрузил списки. Перезагрузил запрет2. И, вуаля! Заколосилось!


(!!!)P.S. этим же методом починился и YT revanced.  Вот, где собака зарыта, а не в устаревших версиях rv, gmscore/microG или нерабочей стратегии. 

За revanced буду пока наблюдать. 

Техподдержка, добавьте об этом в вики или уберите из пакета запрет2 эти домены.

---

**2026-01-24T10:32:59 | Yury Kuzmenko**
Тогда еще раз убираете список ютуба. Включаете запрет и в терминал роутера закидываете
Запустите в терминале роутера
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)
Появится меню.
Нажать 1 - ввод
ЖДАТЬ
Как меню появится вновь, нажать 2
Дождаться зелёной надписи, проверить на телефоне. Заработало - 1 ввод. Не заработало - просто ввод, зелёное, проверка.
И так пока все стратегии (если они есть) не закончатся.

---

**2026-01-24T10:38:38 | Yury Kuzmenko**
Тогда нужно менять стратегию для запрета

Запустите в терминале роутера
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)
Появится меню.
Нажать 1 - ввод
ЖДАТЬ
Как меню появится вновь, нажать 2
Дождаться зелёной надписи, проверить на телефоне. Заработало - 1 ввод. Не заработало - просто ввод, зелёное, проверка.
И так пока все стратегии (если они есть) не закончатся.

---

**2026-01-24T11:42:15 | Владимир**
Это моя личная рекомендация и как сейчас работает у меня. Убрал списки youtube, discord из подкопа, запустил в терминале 
sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh)
Нажал 8. Можете проверить, может сразу со стандартной настройкой все полетит, если нет. Потом в меню стратегий подбирал стратегии для ютуба пока не нашлась что открывает моментально (некоторые будет писать рабочие, но надо проверять насколько). В стратегиях дискорда выбрал 50-stun. И вот пока проблем не знаю. Не факт что заработает, но такое решение я для себя нашел.
В подкопе ютуб будет с задержками, не смог победить, можно кинуть в верхний путь, но тогда появляется реклама

---

**2026-01-24T13:57:02 | Kiss_My_Axe**
Перезапустить интерфейс awg10, повторить проверку, красного при пингах быть не должно.
Открыть zapret2, снять галку с раздела "default", сохранить, применить.

---

**2026-01-24T13:59:14 | Kiss_My_Axe**
Запрет остановить и отключить. В настройках подкопа адгард днс заменить на гугл.
Система - Планировщик. Удалить 0 4 * * * service zapret restart

---

**2026-01-24T14:18:26 | Xrist89**
Добрый день. Настроил теил , вроде всё работает, кроме ютьюба. На роутере ютьюб работает через zapret2, Я так понимаю нужно где-то как в подкопе,  сетевой интерфейс источника добавить tailscale0, но в zapret'e такого не нашел.

---

**2026-01-24T18:00:16 | Routerich**
Запустите в терминале роутера
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)
Появится меню.
Нажать 1 - ввод
ЖДАТЬ
Как меню появится вновь, нажать 2
Дождаться зелёной надписи, проверить на телефоне. Заработало - 1 ввод. Не заработало - просто ввод, зелёное, проверка.
И так пока все стратегии (если они есть) не закончатся.

Попробуйте так.

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

**2026-01-24T19:02:05 | Kiss_My_Axe**
Могу предположить, что у вас ютуб отлично работал через ютубанблок. После наката скрипта №5 добавился конкурент zapret.
Предлагаю в Службы - Zapret нажать Стоп и Отключить, проверить Ютуб. Если всё норм, то в 
Службы - Ютубанблок нажать Старт и Енабле.
На этом пока остановиться.

---

**2026-01-24T19:30:22 | Routerich**
Здравствуйте.
может zapret2?

---

**2026-01-24T20:06:20 | Виталий Комаров**
Обновил, теперь в подкопе пусто, но версия новая) зато появился Zapret

---

**2026-01-24T23:25:33 | Prosto_Vasia77 🇷🇺**
Добрый вечер, подскажите как звонки в телеге через zapret2 завести?

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

**2026-01-25T13:05:49 | Kiss_My_Axe**
Службы, zapret, стоп.
Службы zapret2, стоп, отключить автозапуск.

И вот это ещё в терминале:
# Проверка на битый конфиг
for x in /etc/config/*; do uci show "${x##*/}" >/dev/null || echo "$x is broken"; done

---

**2026-01-25T13:07:20 | Олег Михайлович**
zapret2 не могу отключить, сразу на странице зависает

---

**2026-01-25T13:12:28 | Kiss_My_Axe**
Система - Автозапуск.
Найти zapret и zapret2.
Нажать на Включено, чтобы стало Отключено.
И там же стоп.
Или роутер перезагрузить.

---

**2026-01-25T13:45:39 | Anna Bagler**
Должны быть остановлены запрет 1 (просто zapret), анблок, убрать из подкопа yt, не важно, в какой он секции, чтоб его вообще не было в подкопе и потом только запрет2.

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

**2026-01-25T19:03:38 | Kirill Ivansky**
запустил скрипт, он мне сказал zapret not work \
хотя с ним как раз телевизор работал )
очень что-то странное, но подожду пока закончит

---

**2026-01-25T19:13:14 | Routerich**
Или пробуйте zapret2

---

**2026-01-25T20:44:42 | Igor Zorin**
Народ, кто-нибудь пользуется youtubeUnblock? Знаю, что для Zapret есть скрипт подбора стратегий, а есть ли подобное под youtubeUnblock? Интересует настройка протокола QUIC, который нужен для просмотра через PotPlayer и скачивания через yt-dlp.

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

**2026-01-25T21:45:57 | Kiss_My_Axe**
Либо остановить и отключить запрет, включая удаление 0 4 * * * service zapret restart из Система - Планировщик, либо убрать ютуб из подкопа.
В настройках подкопа заменить dns.adguard-dns.com на гугл, к примеру. В общем на что угодно, кроме адгарда.

---

**2026-01-25T22:20:39 | 🅵 ФЕРЗЬ**
Роутер: Xiaomi Router BE3600 2.5G
Прошивка: сток (OpenWRT на него нет)
Поставил zapret отсюда:
https://github.com/commensal/rdx-zapret2
Установил через SSH, всё завелось, но дальше упёрся в непонимание.
На 4pda человек написал следующее:
Кто пользуется консольной игрушкой zapret:
Обновил в файле бинарники до v72.5 + изменил дефолтные стратегии и обновил fake данные (из репо remittor).
Мессенджеры со звонками работают, тытруба и вреднограмм летают. Не делайте так! А-та-та!.
Я хочу повторить обновление бинарников, как у него, но не понимаю, о чём речь:

какие именно бинарники, где они лежат и как их обновлять в рамках zapret на стоковой прошивке.

Если кто реально шарит в zapret и стоковом Xiaomi, подскажите, пожалуйста.


Упд: у меня просто лично звонки не хотят работать в тг, и дискорд не работает и некоторые сайты отваливаются(SSL) из-за агрессивной стратегии

---

**2026-01-26T00:17:27 | None**
Я подкоп вооьще отключил. Zapret2 имба.

---

**2026-01-26T00:20:58 | Dmitry Kulakov**
Разобрался. Дело было во включенном zapret.

---

**2026-01-26T00:24:04 | Kiss_My_Axe**
Система - Планировщик. Удалить 
0 4 * * * service zapret restart
Нажать Сохранить.

---

**2026-01-26T00:25:37 | Dmitry Kulakov**
А вот у моего товарища нет zapret. А проблема та же

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

**2026-01-26T08:39:54 | Routerich**
ну его либо менять не надо было, либо просто копировать из zapret2

---

**2026-01-26T09:29:29 | Routerich**
https://www.reddit.com/r/youtube/comments/1qfn9dy/this_content_isnt_available_try_again_later/?tl=ru
https://github.com/Flowseal/zapret-discord-youtube/issues/5395

---

**2026-01-26T15:05:37 | Vasa**
Листы для синг-бокса
https://github.com/savely-krasovsky/antizapret-sing-box
https://github.com/1andrevich/Re-filter-lists
https://github.com/itdoginfo/podkop

---

**2026-01-26T15:28:49 | Kiss_My_Axe**
Будет.
Но имейте ввиду, вам ВСЮ коробку игровую придётся запихивать в впн.
Возможно как-то решится через zapret2, но это довольно призрачно.

---

**2026-01-26T15:33:43 | Routerich**
сторонний софт(podkop, zapret/zapret2), собственная разработка (zeroblock)

---

**2026-01-26T15:37:30 | Святос**
https://github.com/remittor/zapret-openwrt/discussions/467

---

**2026-01-26T19:08:19 | Редиска на Луне**
Добрый день!
Запустил скрипт №5 все работает, подскажите пожалуйста как убрать работу сайтов через operaproxy (у меня мобильный провайдер,инет не быстрый), некоторые сайты в т.ч. ютуб медленно работают. ip все правьльно опеределяет,трафик идет через opera vpn.  Возможно сделать их работу чеерз zapret минуя  operaproxy?

---

**2026-01-26T19:21:10 | Редиска на Луне**
предварительно необходимо удалить zapret и podkop?

---

**2026-01-26T20:41:09 | None**
Есть где гайд как настроить zapret2 на разные сайты? Не хочу использовать podkop

---

**2026-01-26T20:48:42 | None**
Спасибо вам большое. Настроил инстаграм по отдельной стратегии. Zapret2 просто имба

---

**2026-01-26T21:03:36 | None**
А ютуб запустите через zapret2

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

**2026-01-26T21:09:37 | None**
Подкоп не панацея. Я его вообще не использую. Есть божественный zapret2

---

**2026-01-26T23:08:11 | Михаил**
А чем podkop мешает божественному zapret2?  Прекрасно сосуществуют жеж, если не устраивать драку за одинаковые домены.

---

**2026-01-26T23:50:14 | Mojo Man**
Zapret 2 ютуб подгружал видосы по 10 -20 секунд, иногда не грузил вовсе, снес и вернулся на Запрет 1 в прошлом месяце

---

**2026-01-27T03:43:53 | S W**
Была такая же проблема с чатами, но с zapret2 не хотелось возиться, из этого же поста взял список, прописал в пользовательские домены и все завелось, спасибо

---

**2026-01-27T06:51:33 | Routerich**
Здравствуйте.
проверьте отключен ли частный днс, сторонние программы не установлены, zapret и так далее локально не установлен

---

**2026-01-27T07:02:16 | Routerich**
https://github.com/remittor/zapret-openwrt/discussions/168

---

**2026-01-27T10:03:43 | Vasa**
попробуй
https://github.com/GubernievS/AntiZapret-VPN/blob/main/setup/root/antizapret/download/discord-ips.txt

---

**2026-01-27T10:10:12 | Редиска на Луне**
Добрый день!
Прошивка  24.10.4. 
Zapret2 0.8.4-r3
Все по умолчанию в Zapret2.
Включена стратегия youtube. Сделал копию стратегии default со списком user (там 2 домена web.whatsapp.com lostfilm.tv), blockcheck2 выдал 6 стратегий. Добавил их в блок Опций,но сайты всеравно не открываются из списка user. Подскажите что не так?

---

**2026-01-27T10:32:36 | Bullet for my valentine Poison**
И не обязательно собирать циркулярку. Потренируйтесь на сборке стандартной. Найдите сначала рабочий вариант с одной или двумя разными. Потренируйтесь на ютубе к примеру. https://github.com/bol-van/zapret2/blob/master/docs/manual.md и вот тут почитайте. Запрет2 не такой простой в понимании.

---

**2026-01-27T11:26:24 | Михаил**
Всем привет! Подскажите, а можно ли как то awg10(WARP который) пустить через Zapret? Без Zapret'a плохо работает, рвет соединение часто

---

**2026-01-27T11:29:00 | Михаил**
После перезагрузки awg10 не получает в ответ пакеты, судя данным из Интерфейса
Также во время использования(Youtube через него смотрю), может перестать принимать пакеты

Грешу на то, что без Zapret'a не работает нормально, тк если на ПК запускать WARP без запрета, то не устанавливает соединение

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

**2026-01-27T13:48:28 | Kiss_My_Axe**
Реквест для zapret2
Хосты в списках через пробел, и/или запятую. Как в ZB, удобнее группировать домены одного ресурса.
Если не сложно.

---

**2026-01-27T14:19:50 | Kiss_My_Axe**
Да. У него то, что отображается в NFQWS (текстбокс стратегии) пишется в отдельный файл, напрямую не связанный с тем, что читает основной код. Для синхронизации в /opt/zapret есть отдельный скрипт, который по Применить и Перезапустить активируется, читает /etc/config/zapret и мержит его с реальным конфигом.

---

**2026-01-27T15:11:33 | S W**
Ну так как проблема решена, не стал удалять. 
Просто как факт, что как только указал домены вручную - сразу же чаты подгрузились, после применения настроек. 

Сидел с такой проблемой около недели (было лень заниматься, войс то работал). Как руки дошли, первым делом обновил прошивку и установил бету, но проблема осталась. Пока читал что люди пишут тут, нашел пост с доменами для zapret2 и просто решил попробовать указать домены вручную, мало ли заработет.

---

**2026-01-27T16:55:42 | Ал Каш**
Спасибо за совет, помогла простая установка пакета zapret2.

---

**2026-01-27T17:03:27 | AleXXXey**
Подскажите шопоруку, если хочу запрет2 перезагружать, например каждый день в 6 утра, то верна ли такая команда?

0 6 * * * /etc/init.d/zapret2 restart

---

**2026-01-27T21:58:16 | Илья Николаевич**
zapret v72.20260125

---

**2026-01-27T22:21:43 | Evgenii**
Добрый!
Может направите меня куда копать. Настроил zapret2 на роуторе. Пока испытываю на примере сайта рутрекер. На телефоне работает, открывается, а вот на компьютере под Виндой ни в какую.

---

**2026-01-28T01:23:49 | Kiss_My_Axe**
Я тут малость очешуел.
Удалил curl, нужно для теста было.
Теперь у меня нет zapret2 и zeroblock.
ШТААААААААААААА?????

---

**2026-01-28T02:29:16 | Kiss_My_Axe**
Добавить список YouTube в секцию Discord. Сохранить, Применить.
Службы - Zapret, Стоп, Отключить. 

Проверить Ю.
Ну и можно будет потом попробовать запрет2.

---

**2026-01-28T14:35:45 | Арсений Горлов**
Аналогично вчера было,отвалился ютуб и дискорд...весели на варпе.Докучи походу watchdoc несколько конфигов перебрал не работало ни в какую(даже генератором варп отдельный конфиг делал и скармливал безтолку ).В итоге откатился на бекап который делал день назад и взлетело,ютую же на всякий через zapret2 пустил.Что удивительное как раз пару дней назад до бекапа на zapret2 не работал тот же ютуб только через vless самое адекватное,щас же наоборот с vless и варп с ним траблы.А с zapret2 всё отлично работает.

---

**2026-01-28T15:57:18 | Prosto_Vasia77 🇷🇺**
Здравствуйте, подскажите пожалуйста что то файлы в телегу стали гу очень медленно загружаться, скачиваются норм, ZB + Zapret?

---

**2026-01-28T15:59:01 | Андрей**
Здравствуйте. Где-то с 23 января  вечерами ютуб начал тормозить (сначала на ТВ tizen OS, потом и на телефоне заметил), скидывает автоматом качество до 480p, а если выше - то беда. При этом днем (даже вот сейчас еще показывает 1440 , а вот 2160 тормозит) . Прикрепляю вывод test_config_script_nightly и скрин дигностики podkop. Провайдер Ростелеком, прошивка RouteRich 24.10.4 . Сориентируйте план действий, пожалуйста. 
Я так понял, что (дождавшись очередного вечера) можно пробовать отключить podkop (ну либо проверять, чтобы секции не пересекались) и затем перебирать стратегии скриптом zapret_autoconfig_latest или zapret_autoconfig_PR . Если это не поможет (перед НГ при включенном запрете на телеке проблемы были с ютубом), то отключать podkop+zapret и пробовать ставить zapret2 по pdf-инструкции из wiki .  Или пробовать скрипт №5 (Код для запуска с автоматической генерацией AWG WARP и без установки/замены конфигурации Podkop) ? ранее я запускал №5 после обновления системы

---

**2026-01-28T21:04:46 | Asd**
Есть предложение создать отдельную тему по Zapret, Zapret 2. А то если запустить поиск по запрету, например, в теме интернет без границ, то в основном находятся сообщения с советом отключить запрет.

---

**2026-01-28T22:33:03 | Kiss_My_Axe**
Открыть настройки zapret2.
Скрипты. Снять галку на их включение, Сохранить, Применить, Перезапустить zapret2.
Проверить что как работает.

Правда у вас нет проблем явных с awg10, но мало ли. Вернуть на место всегда успеется.

---

**2026-01-29T00:28:29 | Kiss_My_Axe**
zapret2, Скрипты, снять галку включения скриптов.
Сохранить, Применить, Перезапустить.

И повторная диагностика.

---

**2026-01-29T08:33:39 | Артём Соловьёв**
Подскажите, почему если включить zapret2, у меня отпадывает awg10. Запускал бета скрипт

---

**2026-01-29T08:35:31 | Артём Соловьёв**
с отключенным zapret2 всё ок. в нём ничего не менял после установки

---

**2026-01-29T08:42:13 | Артём Соловьёв**
диагностика подкоп в включенным zapret2. с выключенным вся зеленая

---

**2026-01-29T10:53:31 | Kiss_My_Axe**
Службы - Zapret, Стоп, Отключить.
Службы - Podkop, добавить список Youtube в секцию Discord, Сохранить, Применить.

Если роутер начнёт внезапно перезагружаться ни с того, ни с сего, то:
Система - Пакеты, Фильтр wdoc, вкладка Установлено.
Удалить всё с буквами "wdoc".

---

**2026-01-29T11:22:14 | Kiss_My_Axe**
Возможно сервисы Failsafe DNS работают некорректно. Или подкоп переписал перенаправление DNS на себя.
Перенакатить скрипт №5 по ссылке 3. Убьёт настройки zapret, если используете, архивнитесь.

---

**2026-01-29T12:27:28 | Routerich**
а так его скорее всего и нет. zapret ловит пакеты инициализации и подменяет, сервер авг к такому не готов и всё ломается. можешь у себя проверить удалив I1 из awg

---

**2026-01-29T12:33:31 | Dmitrii Burenin**
Красивое. Ютуб в майн, или это:

Попробуйте насканить страт для запрета.
Запустить, после установки нажать 1 ввод.
Начнётся поиск. Он может быть долгим, если чо ложитесь спать.
Как закончит поиск нажмите 2 и ввод.
Будут предлагаться для проверки страты. Как зелёным напишет - запускайте на телефоне/телеке ютуб.
Не работает - ввод. Работает 1 и ввод.
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-01-29T17:23:04 | Антон**
ВсЁ работает норм с Zapret2

---

**2026-01-29T19:28:00 | Артур**
Третий день бьюсь с НеВКВидео. Перебор стратегий в zapret, последняя версия youtubeunblock, zapret2 - везде одно и то же: нажимаю на видео в фиде - получаю это. Обновляю страницу - начинает показывать. У кого-нибудь есть такое, или приколы моего провайдера?

---

**2026-01-29T22:27:46 | Wenzel Perminov**




Анализ запущен: 2026-01-30 00:24:46
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
  Facebook IP:  198.18.0.8 | YouTube IP:  173.194.221.93

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓0.00 MB / ↑0.33 MB
  Пинг (ya.ru via awg10): ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (77.88.44.242): 56 data bytes
  Программы для перезапуска:  zeroblock zapret2

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
  awg10 (IPv6) : ОФЛАЙН
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 173.194.221.136
    Name:       youtube.com
    Address: 173.194.221.190
    Name:       youtube.com
    Address: 173.194.221.93
    Name:       youtube.com
    Address: 173.194.221.91
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock списки      awg10: !_cloudflare
  zeroblock списки      opera: geoblock,block,meta,tiktok
  zeroblock DNS/Bootstrap DNS: 8.8.8.8 / 77.88.8.8
  zapret2.main.custom_scripts='1'

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.08 | RAM: 47% | NAND: 25% занято / 50.1M доступно
  # ZeroBlock Lists Update
  13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

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

**2026-01-29T23:07:34 | Kiss_My_Axe**
/opt/zapret2/init.d/openwrt/custom.d/50-quic4all.sh

---

**2026-01-29T23:42:37 | Kiss_My_Axe**
Система свежешитая, руками настроен доступ в инет и вайфай.
Zapret2 0.8.6-r1
Скрипты активны.
Интерфейс авг10 поднимается, байтики бегут.
ping -I awg10 ya.ru
PING ya.ru (5.255.255.242): 56 data bytes
64 bytes from 5.255.255.242: seq=0 ttl=56 time=14.649 ms
64 bytes from 5.255.255.242: seq=1 ttl=56 time=13.097 ms
64 bytes from 5.255.255.242: seq=2 ttl=56 time=13.990 ms
64 bytes from 5.255.255.242: seq=3 ttl=56 time=13.097 ms
64 bytes from 5.255.255.242: seq=4 ttl=56 time=24.567 ms
64 bytes from 5.255.255.242: seq=5 ttl=56 time=12.933 ms
64 bytes from 5.255.255.242: seq=6 ttl=56 time=13.531 ms
64 bytes from 5.255.255.242: seq=7 ttl=56 time=13.474 ms
Есть одно но - вот то, что выше, это ВСЕ прошедшие пинги. :)
Дальше морозится, а панель ЗероБлок показывает скрин.

---

**2026-01-29T23:54:42 | Wenzel Perminov**
Анализ запущен: 2026-01-30 01:50:50
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359 /mask.icloud.com/ /mask-h2.icloud.com/ /use-application-dns.net/ 127.0.0.1#5053 127.0.0.1#5054 127.0.0.1#5055
  Facebook IP:  57.144.222.1 | YouTube IP:  173.194.73.93

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓3.13 MB / ↑0.15 MB
  Пинг (ya.ru via awg10): 39.089 / 42.128 ms (0 из 10 потеряно)
  Программы для перезапуска:  zeroblock

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 301) [TLSv1.3]
  awg10 (IPv6) : ОФЛАЙН

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | STOPPED                        | ОТКЛ
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock списки      awg10: block,porn,news,anime,discord,meta,twitter,hdrezka,!_cloudflare,google_ai,hetzner,ovh,digitalocean,cloudfront
  zeroblock списки      opera: geoblock,tiktok
  zeroblock DNS/Bootstrap DNS: 9.9.9.9 / 77.88.8.8
  zapret2.main.custom_scripts='0'

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.02 | RAM: 44% | NAND: 28% занято / 48.1M доступно
  # ZeroBlock BadWAN Monitor
  */10 * * * * /usr/bin/zeroblock badwan_check >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

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

**2026-01-30T10:28:40 | Vasa**
сколько раз можно скидывать ужо...
https://raw.githubusercontent.com/itdoginfo/allow-domains/refs/heads/main/Services/meta.lst
https://github.com/GubernievS/AntiZapret-VPN/blob/main/setup/root/antizapret/download/whatsapp-ips.txt

---

**2026-01-30T13:58:09 | Роман**
Останавливаете youtubeunblock. Устанавливаете zapret2 через: система - пакеты - обновить списки - фильтр zapret2 - установить 2 пакета.

---

**2026-01-30T15:20:38 | Kiss_My_Axe**
У вас доступ к ютуб через авг10. Так как финка недалеко, варп считает ваш айпи финским и точку выхода оформляет в Финляндии.
А там и ютубий вас финнализирует. Потому вы и видите рекламу финскую.
Решение - zapret2.

---

**2026-01-30T17:35:04 | Anna Bagler**
Проконтролировать, чтобы был отключен и остановлен запрет. Убрать список ютуба из подкопа. Далее Система - Пакеты, обновить списки. Потом в поле фильтра zapret2, поставить сам запрет и luci к нему. Проверить.

---

**2026-01-30T19:49:11 | Wessty**
Всем привет, я помню, что тут давали ссылку на git с обсуждением стратегий для zapret2, но не могу найти. Может у кого завалялась ссылочка?

---

**2026-01-30T19:49:30 | Routerich**
zapret2 в поиск

---

**2026-01-30T22:13:38 | Anthony**
you tube не работает с zapret2 - не поможете со сценарием?

---

**2026-01-30T22:54:24 | Anthony**
zapret 2 работает но на телефоне и на ноуте но не работает на телевизоре Samsung, мне бы помощь со сценарием

---

**2026-01-30T23:06:50 | Anthony**
оно отключено просто чтоб проверять zapret2 и тестить

---

**2026-01-30T23:08:25 | Anthony**
я прочитал мануал по Zapretu Но там явно нужно профильное образование и понимание сетей

---

**2026-01-30T23:19:54 | Routerich**
start "zapret: %~n0" /min "%BIN%winws.exe" --wf-tcp=80,443,2053,2083,2087,2096,8443,%GameFilter% --wf-udp=443,19294-19344,50000-50100,%GameFilter% ^
--filter-udp=443 --hostlist="%LISTS%list-general.txt" --hostlist-exclude="%LISTS%list-exclude.txt" --ipset-exclude="%LISTS%ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="%BIN%quic_initial_www_google_com.bin" --new ^
--filter-udp=19294-19344,50000-50100 --filter-l7=discord,stun --dpi-desync=fake --dpi-desync-repeats=6 --new ^
--filter-tcp=2053,2083,2087,2096,8443 --hostlist-domains=discord.media --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fooling=ts --dpi-desync-fake-tls="%BIN%tls_clienthello_www_google_com.bin" --dpi-desync-fake-tls-mod=none --new ^
--filter-tcp=443 --hostlist="%LISTS%list-google.txt" --ip-id=zero --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fooling=ts --dpi-desync-fake-tls="%BIN%tls_clienthello_www_google_com.bin" --new ^
--filter-tcp=80,443 --hostlist="%LISTS%list-general.txt" --hostlist-exclude="%LISTS%list-exclude.txt" --ipset-exclude="%LISTS%ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fooling=ts --dpi-desync-fake-tls="%BIN%tls_clienthello_4pda_to.bin" --dpi-desync-fake-tls-mod=none --new ^
--filter-udp=443 --ipset="%LISTS%ipset-all.txt" --hostlist-exclude="%LISTS%list-exclude.txt" --ipset-exclude="%LISTS%ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fake-quic="%BIN%quic_initial_www_google_com.bin" --new ^
--filter-tcp=80,443,%GameFilter% --ipset="%LISTS%ipset-all.txt" --hostlist-exclude="%LISTS%list-exclude.txt" --ipset-exclude="%LISTS%ipset-exclude.txt" --dpi-desync=fake --dpi-desync-repeats=6 --dpi-desync-fooling=ts --dpi-desync-fake-tls=^! --dpi-desync-fake-tls-mod=rnd,sni=www.google.com --dpi-desync-fake-tls="%BIN%tls_clienthello_4pda_to.bin" --dpi-desync-fake-tls-mod=none --new ^
--filter-udp=%GameFilter% --ipset="%LISTS%ipset-all.txt" --ipset-exclude="%LISTS%ipset-exclude.txt" --dpi-desync=fake --dpi-desync-autottl=2 --dpi-desync-repeats=12 --dpi-desync-any-protocol=1 --dpi-desync-fake-unknown-udp="%BIN%quic_initial_www_google_com.bin" --dpi-desync-cutoff=n2

---

**2026-01-31T10:36:47 | Роман**
Код выше запустите в терминале.
В ставить система - пакеты - обновить списки - фильтр zapret2 - установить 2 пакета

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

**2026-01-31T11:22:06 | Gomer Simpson**
Попробовать Zapret2.

---

**2026-01-31T11:23:25 | Gomer Simpson**
Пакеты - Обновить списки - фильтр "zapret2".

---

**2026-01-31T11:30:07 | Василий Фёдорович Конырев**
тут https://tenchat.ru/media/4713017-roblox-ne-zapuskayetsya-s-zapret-v-rossii--chto-delat-yesli-ne-rabotayet-server-30012026
разъяснения но от них не легче...

---

**2026-01-31T12:33:23 | Egor Sorokin**
Я когда пользовался одним сервисом от zapret, то я искал в гитхабе решения, как я понял там надо добавить домены и айпи, возможно я смогу конечно найти сайт со всеми блокировками, но вряд ли поможет.

---

**2026-01-31T13:09:04 | 𝒢𝑒𝒻𝑒𝓈𝓉**
Подскажите пожалуйста, почему у меня трафик не идет через Tailscale-Exit Node (мой RouteRich - секции последнего ZeroBlock), при этом Youtube проходит через Zapret2 того же роутера в том же режиме.

---

**2026-01-31T14:11:05 | Routerich**
Здесь будет информация о выходе новых версии. 
Тут вы можете обсуждать и делиться своими стратегиями и получать помощь в решении вопросов о zapret2
#Zapret2

---

**2026-01-31T16:53:50 | Kiss_My_Axe**
Баг.
В архив системы не попадают юзерсписки Zapret2.

---

**2026-01-31T19:21:57 | Routerich**
Службы - zapret - отключить автозапуск и остановить запрет - проверять в инкогнито работу ютуба

---

**2026-01-31T19:59:55 | Anna Bagler**
Прописывать не надо. Выбирайте в списках сообщества. Найдите в Службах Zapret, остановите и отключите, если работает. Cписок YouTube есть в секции discord подкопа?

---

**2026-01-31T20:23:17 | Gomer Simpson**
Zapret2 попробуйте.

---

**2026-01-31T20:24:07 | Виктор ZEUS**
Zapret2 ? У меня какой-то стоит, после скрипта 5я

---

**2026-01-31T20:34:41 | Routerich**
Ну тут всё ок, варп видимо перестаёт вытягивать такую нагрузку уже, тут только своё что-то использовать либо zapret/zapret2 настраивать

---

**2026-01-31T20:35:27 | Виктор ZEUS**
а zapret2  где взять ? А то у меня как я понял обычный запрет

---

**2026-01-31T21:56:45 | Михаил**
К слову. Если а вас lg с webos или samsung с tizen, то через zapret2  у вас ютуб будет таки пускаться через встроенный в ОС браузер. :)

---

**2026-01-31T22:48:10 | Михаил**
Мне не понравилось в byedpi две вещи. Первое - что нельзя тупо выигрышную стратегию взять из byebyedpi, многие параметры стратегии вредят работоспособности byedpi. Второе - byedpi ломает нормальную работу dns через sind-box. Появляется предупреждение, что dns запросы не идут через sing-box.  Для себя использую zapret2, для youtube он работает "из коробки" и мирно сосуществует с podkop.

---

**2026-01-31T23:36:38 | John Deere**
Здравствуйте! Скрипт с первого zapret для BF6 во второй подходит? Я его и туда закинул но без толку, сразу неудача подключения к серверам EA. Мануал читал. Пробовал blockcheck2 к ec2-54-80-239-234.compute-1.amazonaws.com так ничего и не нашло (code 28 и 60). Первый zapret отвалился после прогонки 5 скрипта

---

**2026-01-31T23:37:04 | ユージーン**
Добрый вечер !
а стратегия для игр будет ?
что бы дурить UDP трафик
В Zapret 1 вот с этим работает BF 6, Apex, Roblox...
--filter-udp=88,500,1024-65535
--dpi-desync=fake
--dpi-desync-cutoff=d2
--dpi-desync-any-protocol=1
--dpi-desync-fake-unknown-udp=/opt/zapret/files/fake/quic_initial_www_google_com.bin

---

**2026-01-31T23:41:24 | Роман**
--filter-udp=88,500,1024-65535
--dpi-desync=fake
--dpi-desync-cutoff=d2
--dpi-desync-any-protocol=1
--dpi-desync-fake-unknown-udp=/opt/zapret/files/fake/quic_initial_www_google_com.bin

Жесть стратегия, ломает трафик на всех портах с 1024 по 65535.

---

**2026-01-31T23:46:29 | ユージーン**
так это понятно, но не получается...
в Zapret 2 от remittor, работает, а тут нет
что надо прописать, в новом листе не совсем понятно,
не саму стратегию, а пункты в нём типа L7 и так далее

---

**2026-02-01T10:27:10 | Vasa**
если список пустой, то вот подсети телеги которые надо в впн добавлять

https://github.com/GubernievS/AntiZapret-VPN/blob/main/setup/root/antizapret/download/telegram-ips.txt

---

**2026-02-01T10:51:18 | Kiss_My_Axe**
Подкоп - Настройки. 
Заменить adguard DNS на Google DNS
Сохранить, Применить

Система - Планировщик. Удалить 
0 4 * * * service zapret restart
Нажать Сохранить.

И по тормозам - у вас используется Опера-прокси, может она перегружена и поэтому всё тормозит, а может наши оберегатели скорость до неё режут, тут неясно.

---

**2026-02-01T11:44:59 | Gomer Simpson**
Я бы сперва попробовал АВТОКОНФИГУРАТОР для первого zapret. Он у вас уже есть. Если не справится - останавливайте z и ставьте z2. АВТОКОНФИГУРАТОР ищем в теме Интернет без границ.

---

**2026-02-01T12:18:34 | Роман**
Порядок 50
Название quic4all

# NOTE: @ih requires nft 1.0.1+ and updated kernel version. it's confirmed to work on 5.15 (openwrt 23) and not work on 5.10 (openwrt 22)

# can override in config :
NFQWS_OPT_DESYNC_QUIC="${NFQWS_OPT_DESYNC_QUIC:---payload quic_initial --blob=quic_3:@/opt/zapret2/files/fake/quic_3.bin --lua-desync=fake:blob=quic_3}"

alloc_dnum DNUM_QUIC4ALL
alloc_qnum QNUM_QUIC4ALL

zapret_custom_daemons()
{
 # $1 - 1 - add, 0 - stop

 local opt="--qnum=$QNUM_QUIC4ALL $NFQWS_OPT_DESYNC_QUIC"
 do_nfqws $1 $DNUM_QUIC4ALL "$opt"
}
zapret_custom_firewall()
{
 # $1 - 1 - run, 0 - stop

 local f='-p udp -m u32 --u32'
 fw_nfqws_post $1 "$f 0>>22&0x3C@4>>16=264:65535&&0>>22&0x3C@8>>28=0xC&&0>>22&0x3C@9=0x00000001" "$f 44>>16=264:65535&&48>>28=0xC&&49=0x00000001" $QNUM_QUIC4ALL
}
zapret_custom_firewall_nft()
{
 # stop logic is not required

 local f="udp length >= 264 @ih,0,4 0xC @ih,8,32 0x00000001"
 nft_fw_nfqws_post "$f" "$f" $QNUM_QUIC4ALL
}


Оставлю скрипт тут, вдруг кому нужно будет.

---

**2026-02-01T12:21:13 | Nook Scheel**
root@RouteRich:~# logread | grep -i zapret
Fri Jan 30 04:00:00 2026 cron.err crond[4006]: USER root pid 5673 cmd service zapret restart
Sat Jan 31 04:00:00 2026 cron.err crond[4006]: USER root pid 2933 cmd service zapret restart
Sun Feb  1 04:00:00 2026 cron.err crond[4006]: USER root pid 9425 cmd service zapret restart

---

**2026-02-01T12:23:46 | Nook Scheel**
root@RouteRich:~# ps | grep -E 'nfq|tpws|dvtws'
 1896 root      1340 S    grep -E nfq|tpws|dvtws
 4190 daemon    1940 S    /opt/zapret/nfq/nfqws --user=daemon --dpi-desync-fwmark=0x40000000 --qnum=200 --filter-tcp=443 --dpi-desync=fake fakeddisorder --dpi-desync-split-pos=10,midsld --dpi-desync-fake-tls=/
 4191 daemon    1712 S    /opt/zapret/nfq/nfqws --user=daemon --dpi-desync-fwmark=0x40000000 --qnum=65400 --dpi-desync=fake --dpi-desync-repeats=2


Запрет работает

---

**2026-02-01T12:43:04 | Kiss_My_Axe**
Так-то по тесту вы либо после установки и настройки по скрипту №5 зашли в подкоп и всё настроили "как надо", либо у вас скрипт №5 не отработал до конца, либо вы запустили скрипт №5 по ссылке 3. Потому он не исправил красные проблемы.

1 список - 1 секция. А у вас Ютуб в секции дискорд, секции майн и сверху ещё zapret для надёжного слома доступа к ютубу.

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

**2026-02-01T13:24:19 | ㅤРоман**
⚠️Другая маркировка  zapret2
я наверно пропустил сообщения когда спрашивали, это норм зеро и запрет2?

---

**2026-02-01T13:44:18 | Vasa**
в сотый раз...
для роблокса

https://github.com/GubernievS/AntiZapret-VPN/blob/main/setup/root/antizapret/download/roblox-ips.txt

roblox.com

Незнаю точно влияет или нет Клоудфларе, но он тоже в впн идёт, весь целиком и полностью

---

**2026-02-01T13:52:28 | Роман**
https://github.com/Flowseal/zapret-discord-youtube/issues/6859#issuecomment-3613952365

Пробовал на запрет2 завести роблокс (в качестве теста), думал подсунуть ему домены и ip, наткнулся на такое якобы решение. Вот и всё.

---

**2026-02-01T14:07:19 | Routerich**
@ded_ikar В амбассадора Zapret2 хочешь попасть я так понимаю ?)

---

**2026-02-01T15:21:52 | Виль**
Добрый день, сейчас пытаюсь вместо подкопа перейти на zapret2 (по причине высокой задержки), начал читать мануал, после того как накатил его, ютуб сразу заработал без каких-либо проблем, а дискорд не работает, в мануале написано что есть скрипт для него дефолтный, но он не работает, может кто чинил дискорд и может подсказать что делать

---

**2026-02-01T18:02:00 | Камиль**
Еще меня конечно интересует вот такая ерунда
Sun Feb 1 17:50:34 2026 daemon.warn zeroblock[21171]: bash_executor_run_timeout: script killed by signal 15
[config_builder] Xray config validation failed, xray proxies will be unavailable
[singbox_gen] Section Main: proxy[3] requires xray-core (transport=xhttp), skipping
[singbox_gen] Section Main: proxy[6] requires xray-core (transport=xhttp), skipping
[http_client] Failed to rename /tmp/zeroblock/rulesets/remote-awg10-domains.txt.tmp to /tmp/zeroblock/rulesets/remote-awg10-domains.txt
[lists_loader] Failed to download https://raw.githubusercontent.com/KharunDima/whatsapp-lists/main/results/domains.txt
[lists_loader] Section awg10: failed to convert domain txt to json: https://raw.githubusercontent.com/KharunDima/whatsapp-lists/main/results/domains.txt
[lists_loader] Section awg10: list unavailable: remote-awg10-domains
Sun Feb 1 18:04:47 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[zeroblock] ZeroBlock started successfully
Sun Feb 1 18:05:16 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_user_text Error: No such file or directory
Sun Feb 1 18:05:22 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_domains Error: No such file or directory
Sun Feb 1 18:05:33 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_domains Error: No such file or directory
Sun Feb 1 18:05:54 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Sun Feb 1 18:05:54 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[zeroblock] ZeroBlock started successfully
Sun Feb 1 18:07:15 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_hodca Error: No such file or directory
что-то перестало списки подтягивать похоже, вчера еще все работало 😁 даже звонки починились

тут как-то так 

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.140 | YouTube IP:  64.233.162.136

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓0.00 MB / ↑0.08 MB
  Пинг (ya.ru via awg10): 55.249 / 59.199 ms (0 из 10 потеряно)
  Программы в автозапуске:  zeroblock zapret

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 301) [TLSv1.3]

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock списки        Main prx: geoblock,block,news,anime,meta,twitter,hdrezka,tiktok,google_ai
  zeroblock списки       awg10 vpn: telegram,google_play,hodca
  Версия zeroblock: 0.6.1-r106
  zeroblock DNS/Bootstrap DNS: 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.28 | RAM: 23% | NAND: 45% занято / 36.8M доступно
  # ZeroBlock Lists Update
  13 * * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

P.S Zero перезапускал

---

**2026-02-01T20:19:54 | Михаил**
Информационно. Через пару часов вернулся на zapret2. У меня новый youtubeunlock просадил задержку при обращении к AWG раз этак в 10. Причем не только warp но и proton. Вернул все в зад...

---

**2026-02-01T20:55:51 | Vladimir P**
После установки скрипта zapret, youtubeUnblock и sing-box "отключено". Надо все три запустить?

---

**2026-02-01T21:02:53 | Anna Bagler**
Zapret - нет, xray - если нужно.

---

**2026-02-02T06:44:02 | Камиль**
Выдался свободный часок, я выяснил в чем дело. 
Сбросил систему - обновил все через ASU - установил zero полет нормальный 
+ No such file or directory похоже больше не летят точнее был пока один, но это вроде норм 
Mon Feb  2 06:33:00 2026 daemon.info zeroblock[9891]: [config_builder ] Starting sing-box...
Mon Feb  2 06:33:00 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_domains Error: No such file or directory
Mon Feb  2 06:33:01 2026 daemon.info zeroblock[9891]: [config_builder ] Sing-box started successfully
После каждой процедуры проверял программы для квн и обнаружил что все ломает запрет, как только я включаю запрет + квн ничего не работает, выключаю запрет и здравствуй о чудный новый мир
https://github.com/StressOzz/Zapret-Manager
Надеюсь с вашей версией такой неприятности не будет, спасибо за продукт!

---

**2026-02-02T07:16:59 | Routerich**
я проверил на зависимость desync mark и трафик синга точно должен пролезать, но я не могу сказать на каком этапе работает zapret manager или что там у вас, так что проблема останется неисследованной

---

**2026-02-02T09:36:20 | Камиль**
Да с zapret2 все поехало как нужно, подключаются приложения для квн и даже рабочий квн поехал как нужно, либо первый запрет работает не так либо zapret manager  что-то мутит

---

**2026-02-02T12:01:08 | 🅰️🅻🅴🆇🅰️🅽🅳🅴🆁**
Не могу установить пишет:
Unknown package 'zapret2'.
Unknown package 'luci-app-zapret2'.

---

**2026-02-02T12:49:32 | Bullet for my valentine Poison**
Зайти в пакеты, нажать обновить (зеленая кнопка). В фильтр вписать Zapret2 и установить.

---

**2026-02-02T15:01:02 | Bullet for my valentine Poison**
Или Zeroblock + Zapret2 (все равно скоро будет релиз, Буянов обещал)

---

**2026-02-02T17:05:13 | Роман**
А zapret2?

---

**2026-02-02T17:06:49 | Роман**
Тогда править надпись - "Установить Zapret2"

---

**2026-02-02T17:38:30 | Vasa**
https://github.com/GubernievS/AntiZapret-VPN/blob/main/setup/root/antizapret/download/whatsapp-ips.txt

это там есть?

---

**2026-02-02T18:08:38 | Anna Bagler**
Если ни одна стратегия не пробивается, попробуйте zapret2.

---

**2026-02-02T18:12:07 | 乂乂乂 🐋**
[INFO] Запуск zapret_autoconfig v0.1.1 (latest)

ВАЖНО: Создайте полную резервную копию настроек роутера!

Создана ли резервная копия? (y/N): [ERROR] Резервная копия не создана. Выход.

---

**2026-02-02T20:31:34 | Kiss_My_Axe**
Да. Но ютуб будет работать через zapret.

---

**2026-02-02T22:07:16 | Kiss_My_Axe**
Службы, Zapret, Стоп, Отключить.
Службы, подкоп, Настройка. Сменить adguard DNS на Google DNS.

---

**2026-02-02T22:41:54 | Pavel**
zapret2.main.custom_scripts='1'
root@RouteRich:~# 
root@RouteRich:~# # --- БЛОК 7: СИСТЕМНЫЕ РЕСУРСЫ ---
root@RouteRich:~# 
root@RouteRich:~# echo ""

root@RouteRich:~# echo "= СИСТЕМНЫЕ РЕСУРСЫ:"
= СИСТЕМНЫЕ РЕСУРСЫ:
root@RouteRich:~# printf "  LAN IP: %s\n" "$LAN_IP (Прошивка: ${VERSION})"
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
root@RouteRich:~# printf "  CPU: %s | RAM: %s%% | NAND: %s занято / %s доступно\n" "$LOAD" "$MEM_P" "$NAND_PCT" "$NAND_FREE"
  CPU: 0.28 | RAM: 18% | NAND: 31% занято / 46.0M доступно
root@RouteRich:~# crontab -l | sed 's/^/  /'
root@RouteRich:~# if opkg list-installed | grep -q "wdoc"; then
> printf "  ${RED_BRIGHT}!!!_WatchDoc установлен${CLR_OFF}\n"
> fi
  !!!_WatchDoc установлен
root@RouteRich:~# 
root@RouteRich:~# 
root@RouteRich:~# # Блок 8: Очистка лога
root@RouteRich:~# if [ -f "$LOG_FILE" ]; then sed -i 's/\x1b\[[0-9;?]*[a-zA-Z]//g' "$LOG_FILE"; fi
root@RouteRich:~# echo ""

root@RouteRich:~#

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

**2026-02-03T07:08:46 | Routerich**
хм, а зачем вам zapret2 если у вас всё через Podkop?
остановите Zapret2 и проверьте как будет работать
если так же, стопните ещё Podkop и посмотрите

---

**2026-02-03T07:51:25 | D**
Не работает онлайн в игре Dark Souls 2. Нашёл такое решение. Вопрос, можно ли подобное прописать в роутере?  
1)Используем Zapret, точнее заходим в папку и выбираем service.bat
2)Прописываем 6 (switch game filter), чтобы было "enabled"
3)Прописываем 7 (Switch ipset), чтобы было "loaded" или "any" (В зависимости от версии zapret)
4)Прописываем 8 (update ipset list)
5)Выходим из service.bat
6)Запускаем игру из стима.
7)После запуска игры в папке с Zapret открываем general.bat, который без всяких приписок (Не знаю, насколько приписки важны и работает ли с другими, но я использовал чистый general.bat)
8)Играем.

---

**2026-02-03T09:15:02 | Routerich**
zapret2 0.9.0-r2
Автоперезапуск сервиса через ucitrack
  - При нажатии "Сохранить и применить" в LuCI сервис zapret2 перезапускается автоматически
ожидайте в репозитории

---

**2026-02-03T11:10:06 | Михаил**
Вот вам еще рациональный вариант. Берёте wr3000s или аналог от cudy, настраиваете podkop и zapret. Пользуетесь. И ждете be7200 от Роутерича к середине года.

---

**2026-02-03T11:16:42 | Роман**
То-есть дядя Вася берет роутер что-бы смотреть Ютуб, при этом ему надо попасть на замедленный Ютуб что-бы прошить роутер, накатить подкоп, настроить его? Так?
Да даже тот-же zeroblock  и zapret2 (с отличным веб интерфейсом и блокчеком) собственной разработки уже стоят того, что я "переплатил" - по вашему мнению. 
ИМХО, кому что нравится - тот то и берет. Без негатива естественно 😁

---

**2026-02-03T12:13:23 | Aleksey Drachev**
Zapret показало что не работает - это значит для конкретного сайта (какого-то тестового http запроса) он не работает? Или он вовсе после этой неудачной проверки был отключен и не будет использоваться ни для каких сайтов? Я просто не разобрался пока что zapret делает...

---

**2026-02-03T13:42:52 | Роман**
Ого! Проект ожил, обновы! 
А что за сервис восстанавливает данная функция? Сам ZB или сервисы из автоустановки - opera, warp, xray, zapret2?

---

**2026-02-03T13:58:08 | Lelik**
Всех приветствую, когда пакет zapret2 планируется обновить?

---

**2026-02-03T13:58:55 | Lelik**
Всех приветствую, когда пакет zapret2 планируется обновить?

---

**2026-02-03T16:18:06 | Gomer Simpson**
А ещё лучше, это:https://t.me/routerich/3845/420612

Zapret у вас уже стоит, так что, просто насканировать стратегий и проверять.

---

**2026-02-03T16:49:21 | Anna Bagler**
Нет, это просто zapret от болвана, запрет2 с правками от Fresa - это РР.

---

**2026-02-03T17:18:06 | Kiss_My_Axe**
Службы - Zapret, остановить, отключить.
Службы - Podkop, в секцию Дискорд добавить список ютуб.

---

**2026-02-03T17:22:35 | EVGENY**
На мобильном Ютуб запустился. Сейчас буду смотреть на телеках
Спасибо. А отключения Zapreta , что себе отрезал ?

---

**2026-02-03T17:27:09 | EVGENY**
Через zapret быстрее должен в теории работать ?

---

**2026-02-03T17:32:40 | Yury Kuzmenko**
В терминал 

wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest

---

**2026-02-03T17:43:03 | EVGENY**
wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest

---

**2026-02-03T17:44:21 | Anna Bagler**
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-02-03T17:44:35 | EVGENY**
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest

---

**2026-02-03T19:42:06 | Gomer Simpson**
Zapret2 шлифуют.

---

**2026-02-03T20:36:32 | Kiss_My_Axe**
В раздел внешних пользовательских подсетей подкопа добавьте ссылку. Секция Discord.
https://raw.githubusercontent.com/GubernievS/AntiZapret-VPN/refs/heads/main/setup/root/antizapret/download/whatsapp-ips.txt

---

**2026-02-03T23:51:18 | @Dr.Medvedolog**
Если было ретроспективно, то ткните пожалуйста, какие ограничения у ZB в случае установки на условный Xiaomi, ну кроме невозможности автоматически запустить opera/awg/zapret2. Списки тоже не отдаются и надо руками raw.githubuserconent?

---

**2026-02-04T01:21:26 | Kiss_My_Axe**
TAD -  Target All Domains удобный термин из ютубанблока. Означает перевод ЮАБ в режим перехвата и обработки всех доменов.

Что-то там с ДНС не то, кмк.
Залил чистую прошивку и установил только Zapret2.
Секцию ютуб выключил,  секцию дефолт включил.
Скормил дефолту список из нескольких, проверенных ранее на открытие через запрет2, доменов. 
Не открываются.

Восстановился из фуллбэкап (zapret2, zeroblock)
Тот ж список доменов, тот же дефолт в запрет2.
Всё открывается.
Отключил зероблок и перезагрузил роутер - открываются.
Удалил зероблок и перезагрузил роутер - не открываются.

Койкого рожна этому всему ннада, мне вовсе непонятно

---

**2026-02-04T07:49:21 | VecH.Pro**
https://t.me/routerich/80283/354565

Для запуска всё выполнено в zapret стратегия подобрана, ютуб работает

а roblox (будь он неладен) не хочет
Стартовую страничку вижу, а в игры не заходит

---

**2026-02-04T08:26:30 | Pavel**
Привет всем!
Установлено: RouteRich 24.10.2 r28739-d9340319c6 RR-3.6.6 / LuCI openwrt-24.10 branch 25.250.61039~923f8d9

+ стоит Zapret   v71.20250708

пытаюсь поставить zapret2, делаю по инструкции из пдф файла, однако не могу найти нужный пакет: см скрин, также и на команды в терминале - не находит запрет2

---

**2026-02-04T11:39:30 | K**
Заказал себе роутер🔥

Хочу начать впитывать инфу.

В WIKI почитаю основную инфу о роутере и настройках.

А какую доп инфу почитать, что сейчас наиболее применимо:
Zapret 
Zapret2 
Zeroblock?

---

**2026-02-04T12:11:31 | Kiss_My_Axe**
Есть уже почти уверенность в том, что наличие переноса строки в конце списка хостов, оказывает влияние на работу zapret2.
Явно заметно на списках с одним доменом.
viber.com
перенос строки
нет соединения вайбера

viber.com нет переноса строки
соединение устанавливается

---

**2026-02-04T12:55:03 | Routerich**
пакеты  | полный мануал 
ZeroBlock 0.6.1-r130:
  Исправления:
  - Трафик xray-core теперь маркируется 0x40000000, чтобы Zapret2 его не обрабатывал (как
  sing-box и VPN интерфейсы)
#ZeroBlock

---

**2026-02-04T15:21:42 | Routerich**
# this custom script runs desync to all wireguard handshake initiation packets
# NOTE: this works for original wireguard and may not work for 3rd party implementations such as xray
# NOTE: @ih requires nft 1.0.1+ and updated kernel version. it's confirmed to work on 5.15 (openwrt 23) and not work on 5.10 (openwrt 22)

# can override in config :
NFQWS_OPT_DESYNC_WG="${NFQWS_OPT_DESYNC_WG:---payload wireguard_initiation --blob=quic_3:@/opt/zapret2/files/fake/quic_3.bin --lua-desync=fake:blob=quic_3:repeats=4}"

alloc_dnum DNUM_WG4ALL
alloc_qnum QNUM_WG4ALL

zapret_custom_daemons()
{
  # $1 - 1 - add, 0 - stop

  local opt="--qnum=$QNUM_WG4ALL $NFQWS_OPT_DESYNC_WG"
  do_nfqws $1 $DNUM_WG4ALL "$opt"
}
# size = 156 (8 udp header + 148 payload) && payload starts with 0x01000000
zapret_custom_firewall()
{
  # $1 - 1 - run, 0 - stop

  local f='-p udp -m u32 --u32'
  fw_nfqws_post $1 "$f 0>>22&0x3C@4>>16=156&&0>>22&0x3C@8=0x01000000" "$f 44>>16=156&&48=0x01000000" $QNUM_WG4ALL
  fw_nfqws_post $1 "$f 0>>22&0x3C@4>>16=100&&0>>22&0x3C@8=0x02000000" "$f 44>>16=100&&48=0x02000000" $QNUM_WG4ALL
  fw_nfqws_post $1 "$f 0>>22&0x3C@4>>16=72&&0>>22&0x3C@8=0x03000000" "$f 44>>16=72&&48=0x03000000" $QNUM_WG4ALL
}
zapret_custom_firewall_nft()
{
  # stop logic is not required

  local f="udp length 156 @ih,0,32 0x01000000"
  nft_fw_nfqws_post "$f" "$f" $QNUM_WG4ALL
  local f="udp length 100 @ih,0,32 0x02000000"
  nft_fw_nfqws_post "$f" "$f" $QNUM_WG4ALL
  local f="udp length 72 @ih,0,32 0x03000000"
  nft_fw_nfqws_post "$f" "$f" $QNUM_WG4ALL
}

---

**2026-02-04T16:11:16 | Антон**
Добрый день! Подскажите установил Zero- Zapret2 работает со всеми скриптами +поставил галки на youtube и  defult все прекрасно работает это баг

---

**2026-02-04T17:49:13 | Bullet for my valentine Poison**
и по вкусу добавить Zapret2

---

**2026-02-04T18:14:47 | Bullet for my valentine Poison**
# АВТОКОНФИГУРАТОР ZAPRET

Попробуйте насканить страт для запрета.
Запустить, после установки нажать 1 ввод.
Начнётся поиск. Он может быть долгим, если чо ложитесь спать.
Как закончит поиск нажмите 2 и ввод.
Будут предлагаться для проверки страты. Как зелёным напишет - запускайте на телефоне/телеке ютуб.
Не работает - ввод. Работает 1 и ввод.
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-02-04T19:25:22 | solopups**
Здраствуйте, такая проблема, не могу понять работу  Zapret2, мануал читал, про виды и применение стратегий тоже. Взял в пример сайт rutracker, создал ему отдельный список и через Blockcheck2 пробил, и скопировал стратегии. Дальше в настройках сделал отдельную настройку и выбрал "Circular стратегии" с автоматическим перебором(как в ютубе и дефолтном). Все сделал, но сайт так и не работает

---

**2026-02-04T21:01:48 | Dmitriy M 🎃**
Никак не получается оживить вотсап. Установил Zapret, ввел свой ключ  Vless в секции Opera, выбрал в секции списки по максимуму. Секцию  AWG10 отключил. Итог: опять все работает кроме Вотсапа. В другом чате посоветовали сайт для генерации списков https://iplist.opencck.org/ru/ Кто пользовался, подскажите в каком формате нужно вывести список, чтобы можно было добавить в запрет? Хочу для Вотсапа попробовать сгенерировать

---

**2026-02-04T21:13:51 | Николаич**
Добрый вечер. Как установить Zapret2

---

**2026-02-05T09:15:45 | Raux**
Добрый день.

Окончательно решил приобрести сие устройство, т.к. вижу за полтора года, огромный прогресс, обновили ревизии устройств, запланировали выпуск новой модели, допилили базу знаний. Да и в целом хочется поковыряться в устройстве. 

Можно перед заказом получить мини консультацию? Чтобы понимать смогу ли я осуществить то что крутится в голове. Я нуп и руки из жопы.

Что есть сейчас ax6000, на который не накатить openWRT 😞 В нем 10 портов лан, т.к. куча проводных устройств по всему дому. На компе zapret с прописанными адресами для нужных сайтов + amnezia free, для пары иных сайтов, где не помогает запрет. 
Что хочу - сие устройство, на нем zapret2 + амнезия или warp(хз что лучше будет работать), но как запилить конфиг чтобы через амнезию не шло то что идет через запрет я не вкурил, смотря ветку в ТГ. После рича мой AX6000, в режиме точки доступа, в него все лан провода + через него WiFi(или уже нет никаких проблем с вафлей?)

---

**2026-02-05T09:28:15 | Routerich**
Здравствуйте.
да, это всё осуществимо, что вы хотите.
5-й скрипт из соседней темы как раз ставит WARP.
+ есть гайд как установить и настроить zapret2 на роутере

---

**2026-02-05T10:38:40 | Vasa**
поставишь 5й скрипт \ зероблок

там банально будет 2 разных окошка, типа warp - такие домены списко,  zapret2 - такие домен список

ax6000 - отключишь dhcp , подкинешь ему на LAN адрес из подсети роутерича, подключишь их lan >> lan  и подключай в ax6000 кабель и вафлю

---

**2026-02-05T18:40:48 | Олег?**
Здравствуйте, кто то пробовал устанавливать Entware + zapret на роутер Asus RT-AX53U или любой другой? Может можете поделиться опытом или советами как там что, стоит ли?

---

**2026-02-05T18:59:57 | Vasa**
я ставил туда опенврт, если я модель не путаю...

и sing-box со своим сервером

под Кинетик прошивку я бы проект Antizapret юзал, опять же со своим сервером и подключение WG \ AWG
@Olegkul12

запреты и прочую дичь в Кины я не ставил, т.к. не считаю Entware адекватным

вообще под кны же есть nfqws
https://github.com/Anonym-tsk/nfqws-keenetic
https://habr.com/ru/articles/834826/

---

**2026-02-05T20:06:18 | Антон**
Добрый вечер ! Zapret 2 не все DPI обходит как исправить

---

**2026-02-05T21:24:35 | Nikita**
коллеги, привет, ткните ссылочкой, наверняка уже что-то похожее было
при включенном запрете и подкопе периодически начинают тупить сайты, которые не должны обходиться никак, то есть например на пикабу видос еле грузит, или файл в maven репозитория еле тянется (еле - это значит меньше 2кб в секунду), но стоит только перезапустить запрет - всё полетело... я так понимаю часов на 8-10 хватает
может кто сталкивался с подобным поведением? как решать?
zapret2 0.8.4-r3 (вижу есть обновление, я конечно попробую, но подобная история была даже год назад на youtubeUnblock)

---

**2026-02-06T02:10:04 | Andrey Zubov**
доброй ночи, подскажите пожалуйста, пытаюсь настроить Zapret2 на Debian 12. В чем собственно говоря проблема, есть сайт с которого если я пытаюсь скачать изображение размером 50кб то скачивается первые сколько то килобайт и загрузка встает, я предположил что срабатывает блокировка на 16кб. Запускаю blockcheck2.sh выбираю ссылку для тестирования example.com/image.jpg который через curl у меня полностью не закачивается и запускаю подбор стратегии. В итоге на первом же шаге я получаю
* curl_test_https_tls12 ipv4 example.com/index.jpg
- checking without DPI bypass
[attempt 1] AVAILABLE
[attempt 2] AVAILABLE
!!!!! AVAILABLE !!!!!
и соответственно я не понимаю, почему если я пытаюсь скачать изображение своим curl у меня оно не скачивается зависая в процессе, при этом блокчек утверждает что никакой блокировки вообще нет, в чем может быть проблема?

---

**2026-02-06T06:34:14 | Камиль**
А в чем может быть дело, многие забугорные сайты просто не открываются, приходится все в секцию кидать. Если открыть с мобильного интернета, сайты открываются.
Использую zapret2 + zero (zapret = youtube, discord) zero 2 секции 
Анализ запущен: 2026-02-06 06:28:31
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.1.232 | YouTube IP:  173.194.220.91

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓0.00 MB / ↑0.01 MB
  Пинг (ya.ru via awg10): Ожидайте, идет замер (10 пакетов)...
  Пинг (ya.ru via awg10): 29.206 / 29.640 ms (0 из 10 потеряно)
  Программы в автозапуске:  zeroblock zapret2

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 301) [TLSv1.3]

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock списки        main prx: geoblock,block,porn,news,anime,meta,twitter,hdrezka,tiktok,google_ai,hodca
  zeroblock списки          ru prx: telegram,google_play
  Версия zeroblock: 0.6.1-r114
  zeroblock DNS/Bootstrap DNS: 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.20 | RAM: 26% | NAND: 43% занято / 38.4M доступно
  # ZeroBlock Lists Update
  13 * * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1
Для main секции FakeIP включен (чек бокс не активен)
Для ru секции FakeIP включен (чек бокс не активен)
Правда у меня еще версия Zero 114 может ли быть дело в этом ?
P.S awg секцию не использую

---

**2026-02-06T07:26:31 | Routerich**
Здравствуйте.
пустить ютуб в zero.
zapret отключить.

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

**2026-02-06T08:51:42 | Антон**
и zapret

---

**2026-02-06T09:08:21 | Камиль**
Если использовать Zero без awg, нужно выключать watchdog? 
Т.е. я сейчас сбросил до заводских, хотел обновить через asu но похоже там проблемы. Установил Zero тыкнул галки Xray + Zapret2.
Нужно ли мне выключать интернет детектор ? Потому-что по дефолту он включен
Из своих пакетов только openssh-sftp-server

---

**2026-02-06T09:10:39 | Камиль**
Я пробовал такие сценарии:
Выключить просто zero -> сайт открылся 
Выключить zapret -> сайт открылся 
Включить zapret -> сайт открылся
Включить zero -> сайт не открылся 
Выключить все -> сайт открылся 
Мобильный интернет -> сайт открылся

---

**2026-02-06T09:17:55 | Камиль**
Да я вроде многое через zero пускаю. Я помню начало еще, zapret у жены рабочие сайты ломал... Я всё еще под прицелом, со своими игрушками😁

---

**2026-02-06T10:47:34 | Bullet for my valentine Poison**
Zapret2 + Zeroblock. И настраиваете.

---

**2026-02-06T14:10:05 | Bullet for my valentine Poison**
Zero и Zapret2 отключены.🙄

---

**2026-02-06T15:45:20 | Роман**
Ну я вместо сброса прошил 3.8.2, накатил zb - r150, zapret2 - 0.8.6-r2 - всё в порядке. В чем было дело - непонятно.

---

**2026-02-06T16:45:09 | Lelik**
Я понял почему у меня не видит обновлений zapret2. У меня mediatek/filogic

---

**2026-02-06T21:45:16 | Routerich**
Я так понимаю Discord через Zapret2, ищите стратегию через blockcheck, на которой будет везде работать

---

**2026-02-06T21:51:18 | Алексей**
Вопрос в догонку 
youtubeunblock, zapret, podkop можно будет удалить ?

---

**2026-02-06T22:19:32 | Anna Bagler**
Там подсети меняются, наверное. Но пробуйте подобрать стратегии. Спросите в теме zapret2.

---

**2026-02-06T22:26:17 | Bullet for my valentine Poison**
Узнайте на каких доменах ваш роблокс. И пробуйте блокчекером. Возможно в стратегии нужно будет первым пускать фэйк с блобом. А затем уже что-то вторичное. А может у вас на дефолте заработает. Если то, что я написал, для вас какие-то непонятные слова, читайте-учите мануал. Плюс загуглите Zapret2 Bol-van manual github. и тоже читайте (но там более обширно). Пока не поймете хотя бы минимально, как это работает. Потренируйтесь на Дискорде.

---

**2026-02-06T22:37:44 | V T**
Добрый вечер! В последнее время (пару недель) ютуб очень плохо грузится в качестве 1080р и выше. Иногда и на 720р требуется время, чтобы подгрузить видео. Прям некомфортно стало смотреть. Подскажите, как полечить?

Только что установил zapret2, убрал zapret из автозагрузки и выключил вручную (не знаю, как удалить)
Ещё установлен Podkop версии v0.7.14, в нём активны секции MAIN и DISCORD. В секции MAIN добавлены списки на скрине 1.
Zapret2 запущен, со скоростью интернета тоже проблем нет, скрин 2

---

**2026-02-07T09:59:07 | Роман**
Хронология простая, обновили прошивку, настроили сети, установили пароли. Далее, в прошивке уже установлен youtubeunblock без веб интерфейса - если он не помогает - удаляем его (если ставите 5й скрипт - он сам удалит). Далее если есть свои ключи vless или другое - ставите или zeroblock или podkop. Для Ютуба - zapret2. 
Если всё написанное выше для вас какие-то каракули - скрипт 5 из закреплённых сообщений в ветке интернет без границ, либо скрипт бета из ветки бета.

---

**2026-02-07T12:37:40 | Anna Bagler**
Как обычно ставят пакеты. Система - Пакеты, кнопочка Обновить списки, в поле фильтра zapret2 и ok, потом установить, что надо.

---

**2026-02-07T14:26:44 | NITO**
Господа, прошу подсказать как решить задачку
Пытался установить по 5 скрипту podkop но на процессе установки singbox отваливается (не скачивается). Пытался поставить отдельно с гайда №2 для лечения проблемы свежей установки но kmod жалуется на архитектуру. С инетом просто не скачивает. Singbox так-же не дает надежд на установку. Пытался через Zapret по инструкции, тоже труба и по предоставленным инструкциям не хочет заводиться

---

**2026-02-07T14:41:15 | Routerich**
пакеты  | полный мануал 
ZeroBlock 0.6.2-r30:
  Новые возможности:
  - Интеграция TrustTunnel — поддержка протокола через socks5, автоматическая генерация TOML-конфигов, управление процессами
  - Версии opera proxy, xray, zapret2 в диагностике(для trusttunnel не реализовано в апстриме)
  - Hostname TrustTunnel и тип подключения на дашборде
  - Теперь в dashboard в "Информация о сервисах" не отображаются сервисы, которые не требуются в данной конфигурации

  Исправления:
  - desync_mark return стал безусловным в mangle_output
  - Пропуск отключённых секций при валидации дубликатов в LuCI
  - Парсинг user_domains_text теперь поддерживает разделение пробелами

  Рефакторинг:
  - Удалена дублирующая обработка user_subnets в disable_fakeip
  - Оптимизация fully_routed_ips и обработки Block-секций
  PS
  за trust tunnel пользователь следит сам, потому что получить версию из пакета нельзя и поэтому узнать нужно обновление или нет, невозможно. Качать каждый раз бинарник при старте невыгодно по причине насилования флеш-памяти. Как только upstream реализует версию, или переделаю кнопку или реализую проверку при запуске
#ZeroBlock

---

**2026-02-07T15:47:40 | Routerich**
Новые возможности:
  - Подключение собственных lua скриптов
  - Перезапуск сервиса при нажатии "применить"
  - Рефакторинг работы с lists

Обновляйтесь из репозитория
#zapret2

---

**2026-02-07T16:23:59 | Әмир**
Коллеги, добрый день
Сейчас на моём роутере установлено всё, согласно 5-му скрипту, при этом я удалил Zapret
Т.е., состояние текущее: 5-ый скрипт и отсутствие Zapret

Я арендовал VPS сервер
Есть ли мануал где-нибудь, который помог бы мне грамотно настроить перенаправление части трафика (сортированного по доменным именам и ip-адресам) через vpn-туннель, чтобы не создать конфликт с Zapret и настроенным DNS over https?

---

**2026-02-07T17:45:26 | Vasya77**
Добрый вечер, подскажите последние пару дней заметил что очень медленно стали скачиватся обновления в центре обновлений windows 11, установлен ZB + Zapret2?

---

**2026-02-07T18:44:02 | Vasa**
вот список адресов Амазона, уже ужатый...
но тут много
https://github.com/GubernievS/AntiZapret-VPN/blob/main/setup/root/antizapret/download/amazon-ips.txt

---

**2026-02-07T19:00:22 | Routerich**
полный мануал по zapret2 обновлён

---

**2026-02-07T19:05:35 | Vasa**
Да ладно... серьезно?? я бы никогда не поверил...

и как вы догадались
https://github.com/GubernievS/AntiZapret-VPN/blob/main/setup/root/antizapret/download/roblox-ips.txt

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

**2026-02-08T00:43:06 | Bullet for my valentine Poison**
либо на первом запрете подбирать страты. Более сложный вариант ковырять Zapret2. Либо по интернету поискать бесплатные подписки для Zeroblock'a. (4pda) В идеале несколько рабочих вариантов. Блокировки все время меняются, нужно что-то иметь на черный день. Вплоть до платных подписок. (Насчет того что кто-то советовал, изначально вам дается гарантия на то, что роутер будет работать, как обычный роутер. А все свистоперделки для обходов вы ставите и настраиваете самостоятельно.На свой страх и риск) Ну и если где-то у вас затык, не стесняйтесь писать в чат, обязательно помогут. Главное не хамить😊

---

**2026-02-08T06:02:19 | Камиль**
А в логи Zero запрет тоже выводится ?
[zeroblock] Starting ZeroBlock...
[zeroblock] ZeroBlock started successfully
Sun Feb 8 06:00:00 2026 cron.err crond[3388]: USER root pid 7368 cmd /usr/bin/zeroblock system_monitor >/dev/null 2>&1
[http_client] curl_easy_perform failed: Error
[dpi_checker] Failed (HTTP 200, no data)
[http_client] curl_easy_perform failed: Error
[dpi_checker] Failed (HTTP 200, no data)
[http_client] curl_easy_perform failed: Error
[http_client] curl_easy_perform failed: Error
[dpi_checker] Failed (HTTP 200, no data)
[dpi_checker] Failed (HTTP 202, no data)
[http_client] Response size exceeds maximum (2097152 bytes)
[http_client] curl_easy_perform failed: Error
[dpi_checker] Failed (HTTP 200, no data)
[http_client] curl_easy_perform failed: Error
[dpi_checker] Failed (HTTP 200, no data)
[dpi_checker] Invalid or unsafe URL: https://media-assets.stryker.com/is/image/stryker/gateway_1?$max_width_1410$
[dpi_checker] HTTP error 404
[http_client] curl_easy_perform failed: Error
[dpi_checker] Failed (HTTP 200, no data)
[http_client] curl_easy_perform failed: Error
[dpi_checker] Failed (HTTP 200, no data)
[zapret2_manager] Failed to parse JSON
Или я снова где-то накосячил

---

**2026-02-08T08:09:37 | Bullet for my valentine Poison**
Но Zapret2 греет душу.😁

---

**2026-02-08T08:51:41 | Routerich**
пакеты  | полный мануал 
ZeroBlock 0.6.2-r37:
  Новые возможности:
  LuCI интерфейс
  — Переименование секций в окне редактирования(в самом низу окна)
  — Компактные textarea, адаптивная ширина колонок в секциях
  — Полноширинные контейнеры, выровненные секции
  — Стили диагностики и системной информации

  Community Subnets
  — Автоматические nft sets и mangle правила для подсетей community lists
  — TCP всегда, UDP — только для протоколов с поддержкой UDP(HTTP не умеет в udp и правила не создаются)

  Discord Voice
  — Новая опция discord_voice в настройках
  — При выключении — голосовой трафик Discord (UDP 50000-65535) идёт напрямую или через zapret
  — По умолчанию включена при обновлении через postinst

  Исправления
  — Парсинг разделителей в disable_fakeip(снова работаю пробелы и запятые)
  — Очистка конфигов xray/trusttunnel при остановке
#ZeroBlock

---

**2026-02-08T10:28:46 | Кирилл**
Странно, а мне версия 1.3.0.1 зашла - работает не хуже zapret2. Жаль, что на неё больше ставку не делают. Но разраба тоже можно понять: в целях унификации стандартного набора пакетов действительно лучше выбрать один продукт и его уже вшивать в прошивку, особенно с прицелом на то, что репы OpenWRT в теории легко могут попасть под блокировку... А более кастомизируемое решение всё-таки является лучшим решением в условиях неопределённости будущих разновидностей блокировок.

---

**2026-02-08T11:29:39 | Andrey Zubov**
подскажите пожалуйста, а как правильно подбирать стратегию в zapret2 на youtube? Ведь для работы blockcheck2 требуется ссылка которая либо не открывается, либо ссылка которая фактически не получает полный контент. Что лучше использовать при поиске стратегий блокчеком2?

---

**2026-02-08T12:14:29 | Bullet for my valentine Poison**
Сделайте сброс или перепрошейте на завод. Потом установите ASU и через него обновите все пакеты. После попробуйте Zeroblock + Zapret2. Может будет лучше. Все надо пробовать. Провайдеры у всех делают разные блокировки.

---

**2026-02-08T13:01:48 | Kiss_My_Axe**
Службы - Zapret, Стоп, Отключить.

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

**2026-02-08T15:18:34 | Kiss_My_Axe**
Ютуб через zapret.
Остальное в подкоп.

---

**2026-02-08T16:18:55 | Вячеслав Шевченко**
еще вопрос. купив ваш роутер что именно я получу? впн? или vless или функцию zapret discord/youtube  ?

---

**2026-02-08T20:45:04 | Andrey**
Для оптимизации! :)
Автор zapret советует максимально рано фильтровать потоки.
В идеале в ядре.
У меня фильтр по портам, например 433,8443,9443,10433.
Потом идёт стратегия 1 на порт 443 и список доменов youtube и стратегия 2 на порт ~433

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

**2026-02-08T21:20:05 | Nook Scheel**
Применяем стратегию 1 из 30
=============================
Запускаю синхронизацию конфигов
Запускаю zapret... 1.2✗ 1.3✗ ********* стратегия.

---

**2026-02-08T21:22:33 | Nook Scheel**
Причем на винде https://github.com/Flowseal/zapret-discord-youtube/blob/main/general%20(ALT).bat шуршит эта стратегия нормально

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

**2026-02-08T21:29:15 | Kiss_My_Axe**
Так-то всё красиво...
И ютуб должен, по идее, работать при наличии списка ютуб в секции Discord и выключенном zapret.

---

**2026-02-08T21:30:57 | solopups**
когда zapret обновляешь, надо ли галочку ставить "Разрешить перезапись конфликтующих файлов пакетов"

---

**2026-02-08T21:52:33 | Nook Scheel**
Я правильно понимаю, что сейчас мне на zapret положить большой продолговатый предмет и искать решение в zapret2 но в этот момент youtube сносить из второй секции?

---

**2026-02-08T21:54:25 | Nook Scheel**
Спасибо, ушел курить zapret2 )

---

**2026-02-08T22:15:50 | Anna Bagler**
Ставьте чистую систему, не трогайте обновление пакетов. Смотрите на работу. Скрипт 5/бета или zeroblock, zapret2. Больше ничего не трогайте.

---

**2026-02-09T07:10:53 | Routerich**
- Возможность указания inverted port number

Обновляйтесь из репозитория. версии рассинхронизированы, в следующих релизах поправим
#zapret2

---

**2026-02-09T11:01:33 | Routerich**
Discord и YouTube можно повесить на Zapret
С Podkop убрать эти списки

---

**2026-02-09T11:08:00 | K**
Вопрос (роутер пока не приехал, но хочу чуть быть в курсе).

Моя задача:
1. Пустить трафик YT через обход DPI
2. Все остальные сервисы, железо которых одномоментно устарело через виртуальный сервер.

Что для этого мне нужно:
1. Установить Zapret2 и добавить только YT.
2. Установить Zeroblock, поместить в него списки и убрать от туда YT.

Правильно я понимаю принцип работы?

---

**2026-02-09T11:45:24 | VecH.Pro**
с Roblox какое то решение появилось? (если zapret заставить работать)

---

**2026-02-09T15:05:51 | Routerich**
тогда можно удалить из Podkop эти домены для выпуска и попробовать через zapret их прогнать
https://t.me/routerich/80283/407345

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

**2026-02-10T00:28:35 | Nook Scheel**
Хотелка чисто потестировать zapret2 и не разламывать основные сценарии, т.к домашние отлупят и будут бегать по квартире

---

**2026-02-10T10:19:19 | Геннадий**
Zapret

---

**2026-02-10T13:58:07 | Routerich**
а если zapret2 стопнуть?

---

**2026-02-10T14:47:23 | Nook Scheel**
Добрый вечер, а есть у кого zapret2 под 6.6.119? )

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

**2026-02-10T17:39:22 | VLADIMIR**
У меня zapret

---

**2026-02-10T17:50:37 | Писарев Андрей**
Отключил всё, Tailscale, ZeroBlock, Zapret2, роутер перезагрузил, так-же ничего не работает с этим скриптом.
Обновление списка пакетов вылетает с ошибкой, скрипты не запускаются.
Проблема видать не в программах.
Может в файерволе что надо подкрутить? Какие-то запросы куда-то не пускает.

---

**2026-02-10T20:13:26 | Len Kzn**
Всем доброго Как лучше все обновить ?

Версия прошивки openwrt-24.10 branch (25.302.55195~bfcef12)

установлен  podkop  v0.7.7-r1

установлен  zapret  72.20251022

---

**2026-02-10T21:13:56 | Stanislav Gurov**
Добрый вечер!

Использую связку podkop + zapret. Вижу, что сейчас активно рекламируют связку zeroblock + zapret2.

Подскажите, где-то можно ознакомиться со сравнением podkop и zeroblock?

---

**2026-02-11T11:08:22 | Gambeet**
Всех приветствую, подскажите пожалуйста что то интетнет стал отваливаться сегодня утром, секунд на тридцать, потом опять появляется, что может быть? Стоит последняя прошивка + бета скрипт+zapret2

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

**2026-02-11T12:21:29 | Routerich**
и как это связано с zapret2?

---

**2026-02-11T13:54:20 | Routerich**
новые стратегии для zapret2:
youtube
  --out-range=-s34228
  --payload=tls_client_hello
  --in-range=-s5556 --lua-desync=circular:fails=3:maxtime=60
  --in-range=x
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=1
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=1
  --lua-desync=multisplit:pos=2,sld:seqovl=620:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=1
  --lua-desync=multidisorder:pos=1,midsld:strategy=2
  --lua-desync=tls_client_hello_clone:blob=cloned_tls:fallback=fake_default_tls:strategy=3
  --lua-desync=fake:blob=cloned_tls:optional:tcp_seq=10000000:tcp_ack=-66000:repeats=2:tls_mod=rnd,dupsid,sni=fonts.google.com:strategy=3
  --lua-desync=multidisorder:pos=1:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=3
  --lua-desync=fake:blob=0x00000000:tcp_seq=-10000:tcp_ack=-66000:strategy=4
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:strategy=4
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=fonts.google.com:strategy=4
  --lua-desync=multidisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=4
  --lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=5
  --lua-desync=fakeddisorder:pos=method+2:tcp_md5:strategy=6
  --lua-desync=tls_client_hello_clone:blob=cloned_tls:fallback=fake_default_tls:strategy=7
  --lua-desync=fake:blob=cloned_tls:optional:tcp_ts=-600000:tls_mod=rnd,dupsid,sni=www.google.com:strategy=7
  --lua-desync=hostfakesplit:ip_id=zero:host=www.google.com:altorder=1:tcp_ts=-600000:strategy=7
  --lua-desync=hostfakesplit:host=google.com:tcp_ts=-600000:strategy=8
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_ts=-600000:repeats=6:strategy=9
  --lua-desync=fakedsplit:ip_id=zero:pattern=0x00:tcp_ts=-600000:strategy=9
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_ts=-600000:repeats=8:strategy=10
  --lua-desync=multisplit:pos=1:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:ip_id=zero:strategy=10
  --lua-desync=multisplit:pos=1:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:ip_id=zero:strategy=11
  --lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=12
  --lua-desync=multisplit:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=13
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=fonts.google.com:strategy=14
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=14
  --lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=14
  --lua-desync=multidisorder:pos=7,sld+1:nodrop:strategy=15
  --lua-desync=multidisorder:pos=1,midsld,endhost-1:strategy=16
  --lua-desync=fake:blob=0x00000000:tcp_seq=-10000:tcp_ack=-66000:repeats=2:strategy=17
  --lua-desync=fake:blob=fake_default_tls:tcp_seq=-10000:tcp_ack=-66000:repeats=2:tls_mod=rnd,dupsid,sni=www.google.com:strategy=17
  --lua-desync=multisplit:pos=1,midsld:strategy=17
  --lua-desync=multidisorder:pos=1,midsld:strategy=18
  --lua-desync=multisplit:pos=1,2:seqovl=4:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=19
  --lua-desync=multidisorder:pos=2,5,105,host+5,sld-1,endsld-5,endsld:strategy=20
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=21
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=21
  --lua-desync=multisplit:pos=2,sld:seqovl=2108:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=21:final

---

**2026-02-11T14:03:14 | iProxx**
Привет. Установил бета версию скрипта отсюда.
Предварительно сделал сброс до заводских.
В службах Zapret появился. Ютуб работает, как добиться работы остальной запрещенки (Instagram, Telegram и т.п.)?

---

**2026-02-11T14:05:06 | iProxx**
В службах Podkop не появился, только Zapret

---

**2026-02-11T14:11:24 | iProxx**
Сделал сразу после установки скрипта. Zapret появился а Podkop нет

---

**2026-02-11T14:31:49 | Вячеслав Шевченко**
Добрый день. а кто нибудь знает почему решение zapret работает только на юбтуб и дискорд? там планируют расширятся например воцап и тг ?

---

**2026-02-11T14:37:03 | Dmitrii Burenin**
https://github.com/Flowseal/zapret-discord-youtube/discussions/8673

---

**2026-02-11T14:42:35 | Sag**
Вопросик возник в подкопе доп раздел с ютубом и дискорт обрабатывается AwG.
Так вот не которые клиенты Ютуба типа revansed стали себя плохо вести затыки остановки в проигрывание роликов, замечу родной клиент работает хорошо .Так вот думаю если Ютуб отдать на обработку zapret2 ? Как думаете исправит ли данную проблему с revansed ? У кого Ютуб на запрете висит как  себя ведёт он?

---

**2026-02-11T14:44:16 | Bullet for my valentine Poison**
https://ntc.party/t/zapret2-обсуждение/21161/676 в самом конце есть кусочек инфы

---

**2026-02-11T14:58:53 | Кирилл**
А какой домен-то? telegram.org? Так он не под блокировками (нормально открывается). Нужна ж конкретная CDNка (или их семейство), или даже пул конкретных ip адресов. https://github.com/GubernievS/AntiZapret-VPN/tree/main/setup/root/antizapret/download здесь их есть и много - но все перебирать проблематично

---

**2026-02-11T15:19:39 | MichaelN_29**
Добрый день. Подскажите в zapret2 настроен обход youtube. Работает на ПК, телефоне и тв lg. Через какое-то время на тв отваливается, на остальном работает. Нажимаю "Перезапустить" в запрете - на тв опять начинает работать. Может кто сталкивался уже?

---

**2026-02-11T19:41:56 | Святос**
Пока что failed to install zapret2, он установлен, а в меню нету

---

**2026-02-11T20:33:35 | Alexander**
Народ, ни у кого ни каких чудес сегодня с роутером не происходит? Интересует МТС Кировская область. Сначала на одном ПК пропал инет, при этом роутер пинговался но инета не было, со второго ПК пинг был, интернет был. Перезагрузил роутер, второй комп отвалился напрочь, роутер не пингуется. Первый комп роутер пингуется, интернета нет. По wifi телефоны не подключается. Помог сброс роутера. НО! Из бэкапа в котором были установлены podkop, zapret ни первый, ни второй не восстановились. Что это такое?) Я просто офигел от такого чуда. Не первый день этим занимаюсь. Просто чудеса какие-то

---

**2026-02-11T21:01:21 | Novo**
Был бы какой скрипт импорта существующих стратегий для zapret1. Понятно, что 1 в 1 перенести не получится, потому, что поменялась логика работы приложения

---

**2026-02-11T22:37:08 | Kiss_My_Axe**
Не, чото не то с АВГ10.
Можно перезапустить скрипт №5 ссылка 3 из закрепа Интернет без границ. Есть вероятность лечения проблемы.
Можно перенести список ютуб в секцию main.
Можно убрать ютуб из подкопа, включить zapret2, он Ю открывает хорошо, без особых проблем. Обычно.

---

**2026-02-11T22:42:25 | Виталий Беляков**
Если нужен только ютуб, ставить zapret2?

---

**2026-02-11T23:10:51 | Kiss_My_Axe**
desync profile search for tcp target=151.101.66.132:443 l7proto=tls ssid='' hostname='downloads.openwrt.org'
* hostlist check for profile 1
[/opt/zapret/ipset/zapret-hosts-google.txt] include hostlist check for downloads.openwrt.org : negative
hostlist check for openwrt.org : negative
hostlist check for org : negative
desync profile 2 matches
* hostlist check for profile 2
[/opt/zapret/ipset/zapret-hosts-user-exclude.txt] exclude hostlist check for downloads.openwrt.org : negative
hostlist check for openwrt.org : positive
not applying tampering to this request
packet: id=138 pass unmodified

---

**2026-02-12T06:34:15 | АЛЕКСАНДР**
Вопрос Можно ли устанавливать совместно с zapret 2 ?

---

**2026-02-12T06:36:57 | К И М**
Ну пакет zapret2 например поставь, и ютуб возможно сразу оживёт, у меня ожил

---

**2026-02-12T09:44:58 | Routerich**
попробуйте остановить zapret и снова нажать обновить списки

---

**2026-02-12T12:20:04 | Камиль**
А помогите пожалуйста разобраться скрипт выдает это
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/test_config_script/test_config_script_nightly)
1) Скрин первый текущая ситуация
= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.37 | YouTube IP:  173.194.220.93
  Программы в автозапуске: zeroblock zapret2

= ПРОВЕРКА ДОСТУПОВ (YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН
  Запускаем остановленные службы...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:    127.0.0.1
    Address:  127.0.0.1:53
    Name:  youtube.com
    Address: 209.85.233.93
    Name:  youtube.com
    Address: 209.85.233.190
    Name:  youtube.com
    Address: 209.85.233.91
    Name:  youtube.com
    Address: 209.85.233.136
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock списки        main prx: geoblock,block,porn,news,anime,meta,twitter,hdrezka,tiktok,!_cloudflare,cloudfront,hetzner,ovh,digitalocean,google_ai,hodca
  zeroblock списки          ru prx: telegram,google_play
  Полностью маршрутизированные IP-адреса включены!
  Версия zeroblock: 0.6.2-r53
  zeroblock DNS/Bootstrap DNS: 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.27 | RAM: 29% | NAND: 43% занято / 38.6M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 * * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1


Убрал пересечение 
= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock списки        main prx: geoblock,block,porn,news,anime,meta,twitter,hdrezka,tiktok,cloudfront,hetzner,ovh,digitalocean,google_ai,hodca
  zeroblock списки          ru prx: telegram,google_play

2) Скрин 2 теперь в Канаде Cloudflare Detected*
Далее выключил все кроме HODCA 
= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock списки        main prx: geoblock,block,porn,news,anime,meta,twitter,hdrezka,tiktok,google_ai,hodca
  zeroblock списки          ru prx: telegram,google_play
  Полностью маршрутизированные IP-адреса включены!

3) Скрин только hodca включена

---

**2026-02-12T13:32:25 | Vasa**
https://github.com/GubernievS/AntiZapret-VPN/tree/main/setup/root/antizapret/download

---

**2026-02-12T16:39:57 | Роман**
Установил начисто 24.10.5 - пароль, время, индикаторы настроил. Далее установил морду для youtubeunblock - отключил его, не удалял. Установил zb r53 - оттуда установил zapret2 - удалился unblock - морда от него осталась.

---

**2026-02-12T17:47:43 | Stanislav Gurov**
Спасибо за прошивку, очень ждал)

Только что перепрошился, настроил сеть + WiFi. Мастер настройки - жирный лайк 👍👏

WiFi потестил на iPhone 13 Pro Max возле роутера, по ощущениям ~ на 15% выросла скорость.

Теперь настал момент для тестирования новой связки zeroblock + zapret2 вместо старой podkop + zapret :)

---

**2026-02-12T18:50:56 | Борис**
Ну и зря. В том же Zapret2 нельзя выставлять правила для отдельных устройств в локальной сети - чтобы для одних стратегия работала, а для других нет. Я как раз обхожу это через разделение ipv4 и ipv6 - у меня консоль Playstation 5 работает только по ipv4, соответственно моя мега-турбо стратегия ipv6 не распространяется на неё, поэтому у меня и на компе работает всё как надо, и на плойке нет срывов соединения из-за испорченных пакетов

---

**2026-02-12T20:24:48 | bm**
Я только Zapret2 использую. Подкоп даже не смотрел.

---

**2026-02-12T20:26:39 | Anna Bagler**
Тогда в ветку Zapret2 и ищите решения там. Подбирайте стратегию.

---

**2026-02-12T20:29:37 | bm**
Привет! К вам отправили, подскажите что для ТГ можно прикрутить в Zapret2, есть стратки?)

---

**2026-02-12T21:24:51 | Andrey**
Добрый вечер!
Большая просьба:
1. доделать обработку ~ перед номером порта в скрипте /opt/zapret2/init.d/openwrt/uci2config
2. Посмотреть, почему в поле ввода портов не даёт вводить ~

---

**2026-02-12T21:27:27 | Routerich**
Здравствуйте.
Тут уже zapret2. Читайте манул и вперёд

---

**2026-02-13T08:21:05 | Routerich**
zapret2 0.9.2-r24
  Добавлено сканирование ipv4+ipv6 в blockcheck2
  Доделана инверсия портов в luci и config
  Добавлены новые стратегии(отдельно уже выкладывал)
ожидайте в репозитории
#Zapret2

---

**2026-02-13T10:10:24 | Lelik**
https://github.com/bol-van/zapret/discussions/1716#discussioncomment-14803615

---

**2026-02-13T10:40:01 | Роман**
База под использование различных пакетов как zeroblock, podkop, zapret2, в виде openwrt есть. Но придется их самому установить и настроить.

---

**2026-02-13T11:06:20 | Gomer Simpson**
Я обновлялся без сохранения, но бэкап конфига сделал. На чистую поставил ZB, через него Zapret2, ещё там чего по мелочи, потом восстановил бэкап - всё работает, в том числе ютуб и гемини, с которым тоже у кого-то были проблемы, после обновы на 24.10.5.

---

**2026-02-13T11:48:35 | Routerich**
Здравствуйте.
можно из Podkop удалить его и попробовать через Zapret2 пустить
или искать домены на которые телевизор обращается, возможно там другие домены или полностью телевизор в VPN пустить

---

**2026-02-13T12:01:38 | Routerich**
а случаем zapret нет?
если есть стопните и проверьте
youtubeunblock тоже стопните

---

**2026-02-13T15:19:06 | Rom@n**
Fressa, не пойму почему после перепрошивке РР на 24.10.5 и установки ZB + автонастройка AWG10, Zapret2, Opera Proxy у меня игра eve online начала ходить через AWG10, в секции не выбирал не чего такого, что бы с ней было связано, на 24.10.4 такого не было.

---

**2026-02-13T19:58:53 | Routerich**
Стабильного ничего нет. Каждый день отлетает то одно, то другое. Для ютуба можете поставить zapret2, там есть blockcheck и легче подобрать стратегию.

---

**2026-02-13T20:57:30 | Дима Чуйков**
сделал сброс, удалил ЮАБ, накатил ZB. в автонастройке сначала только opera и AWG поставил. в оперу кроме базовых GeoBlock и заблокировать попробовал добавить телегу и ютуб.
сохранил, роутер перезапустил - ютуб не грузился (как и до всех манипуляций).
дальше в автонастройке поставил Zapret2, и изменения секций в опере вернул в исходное.
сохранил, роутер перезагрузил.
больше настроек не менял.

в итоге ютуб ожил (на всех устройствах). выборочно заблоченные сайты потыкал - открываются.

правильно понимаю, что больше можно настройки не трогать без особой надобности и каких-то проблем? 🤔

---

**2026-02-13T21:32:48 | Bullet for my valentine Poison**
Ну это же логично, человек пилит одновременно Zapret2 и Zeroblock. На все нужно время.

---

**2026-02-13T22:06:11 | Konstantin**
Подскажите, как исправить ситуацию? на Routerich AX3000 поставил zapret v72.20260207 (последний), на пк все работает хорошо, но на ТВ (LG) ютуб и кинопаб никак не хотят работать.
ставил все по гайду https://github.com/remittor/zapret-openwrt/wiki/Installing-zapret%E2%80%90openwrt-package

---

**2026-02-13T22:07:16 | Konstantin**
Подскажите, как исправить ситуацию? на Routerich AX3000 поставил zapret v72.20260207 (последний), на пк все работает хорошо, но на ТВ (LG) ютуб и кинопаб никак не хотят работать.
ставил все по гайду https://github.com/remittor/zapret-openwrt/wiki/Installing-zapret%E2%80%90openwrt-package

---

**2026-02-13T22:11:44 | Gft Gft**
если я правильно разобрался то через ZB (Instagram, WhatsApp, AI-сервисы). через zapret2 (YouTube, Telegram, Discord, TikTok)? вроде ничего не забыл.

---

**2026-02-13T22:12:41 | Anna Bagler**
Вам надо самостоятельно подбирать стратегии для zapret2/zapret самостоятельно, т.к. LG капризен. Можно пробовать zeroblock или радикально - приставка на андроид к вашему ТВ и потом уже обходы.

---

**2026-02-13T22:48:38 | Vasa**
https://github.com/GubernievS/AntiZapret-VPN

---

**2026-02-13T22:52:36 | Kiss_My_Axe**
Видимо рестарт авг10 и опера зарешал.
Но с правилами вам надо серьёзно поработать.
1 домен - 1 секция. НИКАКИХ ДУБЛЕЙ. Все дубли в конфиге выглядят так !!!_КРАСНОЕ_СТРАШНОЕ.
Russia outside убрать и забыть.

Система - Планировщик. Убрать строку с перезапуском zapret, нажать кнопку Сохранить.

---

**2026-02-13T23:01:13 | Routerich**
Смотрите. На роутер можно поставить средство маршрутизации и в него воткнуть ваш платный впн, или бесплатный. Можно поставить zapret, это средство не впн, а анти dpi, почитайте про него. У вас будет работать ютуб без рекламы на ру регионе. И вам не нужно будет ставить впн на каждое устройство. Роутер поддерживает все современные протоколы.

---

**2026-02-14T00:07:14 | Anna Bagler**
Zapret удалить. Zeroblock и свежий youtubeUnblock поставить.

---

**2026-02-14T08:08:18 | Aleksandr**
Zapret2 apk можно на гитхабе скачать?

---

**2026-02-14T10:04:13 | Vasa**
akamai - 
https://github.com/GubernievS/AntiZapret-VPN/blob/main/setup/root/antizapret/download/akamai-ips.txt

fastly
https://github.com/GubernievS/AntiZapret-VPN/blob/main/setup/root/antizapret/download/fastly-ips.txt

ovh
https://github.com/GubernievS/AntiZapret-VPN/blob/main/setup/root/antizapret/download/ovh-ips.txt


google
https://github.com/GubernievS/AntiZapret-VPN/blob/main/setup/root/antizapret/download/google-ips.txt

digitalOcean
https://github.com/GubernievS/AntiZapret-VPN/blob/main/setup/root/antizapret/download/digitalocean-ips.txt

Естественно отдельными списками, а то блоки у кого как.

Список ТГ должен выглядеть так - то что в подкопе не у всех работает судя по чату
domain
telegram.org
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

IP
91.108.56.0/22
91.108.4.0/22
91.108.8.0/22
91.108.16.0/22
91.108.12.0/22
149.154.160.0/20
91.105.192.0/23
91.108.20.0/22
185.76.151.0/24

---

**2026-02-14T10:07:45 | Vasa**
я еще использую список антизапрета, там то что РКН блочил. обычно почти все вопросы снимает
если захотите отдельно

чтоб не вписывать кучу сайтов

https://krasovs.ky/sing-box/antizapret-ruleset.json

https://github.com/savely-krasovsky/antizapret-sing-box

---

**2026-02-14T10:16:05 | Gomer Simpson**
Нет. Там Zapret.

---

**2026-02-14T11:00:01 | Роман**
Можете установить через пакеты zapret2. 
Или отключить ЮАБ, и включить Ютуб в zeroblock. Главное чтобы не было никаких пересечений.

---

**2026-02-14T15:26:30 | Anna Bagler**
В полную маршрутизацию его или мучить zapret2.

---

**2026-02-14T15:28:52 | Sergey Kolosov**
zapret2 проработал пару недель и перестал...

---

**2026-02-14T15:32:12 | Sergey Kolosov**
Подкоп не стоит, использовал ранее по порядку, youtubeunblock, zapret, zapret2.

---

**2026-02-14T16:07:14 | Павел Строков**
zapret2
https://github.com/remittor/zapret-openwrt/releases

---

**2026-02-14T16:54:13 | Роман**
Zapret2 для Ютуба и дискорда, zeroblock для телеги.

---

**2026-02-14T17:32:12 | Philipp**
Всем привет, не очень понимаю, если у меня есть свой ключ VLESS, стоит ли запускать скрипт №5 или лучше вручную настроить podkop и zapret?

---

**2026-02-14T18:13:46 | Марат**
Привет всем. Только пришел роутер. Подключил модем - все работает. Теперь очередь за разблокировкой сайтов. Как алгоритм действий? Ставить скрипт номер 5? Есть своя амнезия, zapret  юзал.

---

**2026-02-14T18:16:32 | Midas**
Отвечу сам себе. Виноват был запущенный zapret на ПК.

---

**2026-02-14T18:34:38 | Routerich**
тогда пробуйте другие стратегии, либо пробуйте zapret2

---

**2026-02-14T19:29:12 | Александр**
Анализ запущен: 2026-02-14 19:27:18
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  157.240.205.35 | YouTube IP:  74.125.131.136

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.30 MB
  Пинг (ya.ru via awg10): 7.637 / 10.196 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock zapret2

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
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
  Запускаем остановленные службы...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 74.125.131.136
    Name:       youtube.com
    Address: 74.125.131.190
    Name:       youtube.com
    Address: 74.125.131.93
    Name:       youtube.com
    Address: 74.125.131.91
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock списки       awg10 vpn: discord,meta
  zeroblock списки       opera prx: geoblock,block,porn,news,hdrezka,google_ai,google_play,hodca
  Версия zeroblock: 0.6.2-r66
  zeroblock DNS/Bootstrap DNS: 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.70 | RAM: 32% | NAND: 43% занято / 38.7M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-02-14T19:44:20 | Routerich**
подбирать стратегию zapret2

---

**2026-02-14T20:53:13 | Anna Bagler**
Настроить с нуля надо теперь... Если прошивку верную зашили. И вопросы тогда не в этой теме, тут Zapret2.

---

**2026-02-14T21:07:37 | Баир**
Zapret2 установить надо да?

---

**2026-02-14T22:08:02 | Святос**
Тогда не повезло, стратегии менять до посинения. Или удалять Zapret2 и накатывать nfqws-keenetic, обычно дружит с Самсами

---

**2026-02-14T22:25:05 | Routerich**
Ютуб настраивайте через youtubeUnblock/zapret(2). В зероблоке или подкопе ключ vless вставляйте и выбирайте списки кроме ютуба и кроме Russia и Ukraine в названии.

---

**2026-02-14T23:06:11 | Bullet for my valentine Poison**
https://github.com/bol-van/zapret2/blob/master/docs/manual.md#введение вот это по хорошему, хотя бы просмотреть. Тут более подробно все описано.

---

**2026-02-15T08:53:42 | Routerich**
Хорошо, у вас через WARP сейчас ютуб.
Можете попробовать zapret2, предварительно убрав YouTube из Podkop

---

**2026-02-15T11:52:19 | K**
Прошивка роутера, Zapret2, ZeroBlock и прочие пакеты каким образом обновляются?

Где то будет кнопка обновить или как этот принцип в Openwrt реализован?

---

**2026-02-15T14:29:51 | Валерий**
zapert и zapret2 устанавливал только, предварительно удалил youtubeclock. В интерфейсинтерфейс перезаходил

---

**2026-02-15T15:10:47 | Святос**
Это скорее всего Zapret с такой стратегией

---

**2026-02-15T17:11:30 | Nicky**
Добрый день! Приобрел роутер, настроил zapret2, ютуб работает, а вот с дискордом возникли сложности, настроил по пдфке все, стратегии скопировал из авточек список стратегий, не сработало
вопрос: что делать, и кто ....)

--==мы здесь ==--

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

**2026-02-15T18:45:08 | Tox**
Zapret 2

---

**2026-02-15T18:46:56 | Dmitrii Burenin**
Это zapret 2

---

**2026-02-15T21:47:00 | Routerich**
тогда удалите зероблок и используйте zapret2

---

**2026-02-16T00:50:35 | Nikolai Korp**
Странно, вчера делал знакомому, zeroblok установил, автонастройка opera, proxy awg, zapret2 галки поставил. подождали 5 минут и YB заработал на ПК и ТВ самсунг(ДомРУ)
У другого сегодня podkop обновил и zapret, через zapretmanager подобрал новые стратегии. тоже YB поднялся

---

**2026-02-16T00:53:18 | Nikolai Korp**
У себя cydy+openwrt. podkop + zapret, работает отлчно(ПРов местный но купленый билайном)
Через 2 дня приедет RR уже свой. буду тоже zeroblok + zapret2 ставить

---

**2026-02-16T00:55:31 | Nikolai Korp**
У второго постаивл бы zeroblok + zapret2 но удаленно делала а у него прошивка 24,10,4 на 24.10,5 просит сбросить настройки, а сами уже они не настроят инет)

---

**2026-02-16T07:47:23 | Диншат Валеев**
Вот и я стал счастливым обладателем Routerich'а
Брал на замену AX3000T, перенес свои конфиги Zapret и Podkop и все полетело
Спасибо большое команде Routerich за такое качественное и мощное устройство!

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

**2026-02-16T11:44:16 | sergey**
Анализ запущен: 2026-02-16 15:21:29
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  157.240.205.35 | YouTube IP:  108.177.14.93

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.73 MB / ↑0.39 MB
  Пинг (ya.ru via awg10): Ожидайте, идет замер (10 пакетов)...
  Пинг (ya.ru via awg10): 50.298 / 51.981 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock zapret2 zapret

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret          | RUNNING                        | РАЗРЕШЁН
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  Файл zapret-hosts-user.txt пустой! 
  !!!_КРИТ: Пересечение между zeroblock и zapret:
    zeroblock                 : awg10
    zapret                    : zapret-hosts-google.txt
    Домены: googlevideo.com youtube.com 

  zeroblock списки       awg10 vpn: youtube,meta,telegram
  zeroblock списки       opera prx: geoblock,block
  Версия zeroblock: 0.6.2-r66
  zeroblock DNS/Bootstrap DNS: 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.00 | RAM: 44% | NAND: 27% занято / 49.3M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1
Здравствуйте, гляньте все Ок?

---

**2026-02-16T11:44:31 | Bullet for my valentine Poison**
packet: id=151 len=223 mark=20000000 ifin=br-lan(11) ifout=wan(6)
IP4: 46.147.103.192 => 108.177.14.198 proto=tcp ttl=127 sport=55824 dport=443 flags=AP seq=1749458665 ack_seq=2006399212
TCP: len=171 : 16 03 03 00 A6 01 00 00 A2 03 03 69 92 D7 FB B8 5D FD 6D 8C AD 35 F7 28 57 D0 3B 1E AA 57 F0 BC ... : ...........i....].m..5.(W.;..W.. ...
client mode desync profile/ipcache search target ip=108.177.14.198 port=443
using cached desync profile 0 (no_action)
packet contains tls_client_hello payload
TLS client hello is FULL
TLS record layer version : TLS 1.2
TLS handshake version : TLS 1.2
TLS supported versions ext : not present
TLS ALPN ext : not present
TLS ECH ext : not present
hostname: www.youtube.com
discovered l7 protocol
discovered hostname
desync profile search for tcp ip=108.177.14.198 port=443 icmp=255:255 l7proto=tls ssid='' hostname='www.youtube.com'
* hostlist check for profile 1 (MAXLG)
[/opt/zapret2/ipset/zapret_hosts_youtube.txt] include hostlist check for www.youtube.com : negative
hostlist check for youtube.com : positive
desync profile 1 (MAXLG) matches
desync profile changed by revealed l7 protocol or hostname !
dpi desync src=46.147.103.192:55824 dst=108.177.14.198:443 track_direction=out fixed_direction=out connection_proto=tls payload_type=tls_client_hello
* lua 'multidisorder_1_1' : out pos a0 s1 in range a0-s34228
* lua 'multidisorder_1_1' : payload_type 'tls_client_hello' satisfy filter
* lua 'multidisorder_1_1' : desync
instance cutoff for 'multidisorder_1_1' in=1 out=0
LUA: multidisorder: split pos: 1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
LUA: multidisorder: resolved split pos: 1 91 96 100 102 104 109
LUA: multidisorder: sending part 8 109-170 len=62 seqovl=0 : 6D 00 0A 00 08 00 06 00 1D 00 17 00 18 00 0B 00 02 01 00 00 0D 00 1A 00 18 08 04 08 05 08 06 04 ... m............................... ... 
rawsend_dissect repeats=1 size=114 badsum=0 ifout=wan fwmark=60000000
LUA: multidisorder: sending part 7 104-108 len=5 seqovl=0 : 62 65 2E 63 6F  be.co
rawsend_dissect repeats=1 size=57 badsum=0 ifout=wan fwmark=60000000
LUA: multidisorder: sending part 6 102-103 len=2 seqovl=0 : 74 75  tu
rawsend_dissect repeats=1 size=54 badsum=0 ifout=wan fwmark=60000000
LUA: multidisorder: sending part 5 100-101 len=2 seqovl=0 : 6F 75  ou
rawsend_dissect repeats=1 size=54 badsum=0 ifout=wan fwmark=60000000
LUA: multidisorder: sending part 4 96-99 len=4 seqovl=0 : 77 77 2E 79  ww.y
rawsend_dissect repeats=1 size=56 badsum=0 ifout=wan fwmark=60000000
LUA: multidisorder: sending part 3 91-95 len=5 seqovl=0 : 12 00 00 0F 77  ....w
rawsend_dissect repeats=1 size=57 badsum=0 ifout=wan fwmark=60000000
LUA: multidisorder: sending part 2 1-90 len=90 seqovl=0 : 03 03 00 A6 01 00 00 A2 03 03 69 92 D7 FB B8 5D FD 6D 8C AD 35 F7 28 57 D0 3B 1E AA 57 F0 BC 85 ... ..........i....].m..5.(W.;..W... ... 
rawsend_dissect repeats=1 size=142 badsum=0 ifout=wan fwmark=60000000
LUA: multidisorder: sending part 1 0-0 len=1 seqovl=0 : 16  .
rawsend_dissect repeats=1 size=53 badsum=0 ifout=wan fwmark=60000000
* lua 'fake_1_2' : out pos a0 s1 in range a0-s34228
* lua 'fake_1_2' : payload_type 'tls_client_hello' satisfy filter
* lua 'fake_1_2' : desync
instance cutoff for 'fake_1_2' in=1 out=0
tls extensions length offset : 114
change SNI : www.microsoft.com => rzd.ru size_delta=-11
LUA: fake: 16 03 01 02 98 01 00 02 94 03 03 41 88 82 2D 4F FD 81 48 9E E7 90 65 1F BA 05 7B FF A7 5A F9 5B ... ...........A..-O..H...e...{..Z.[ ... 
rawsend_dissect repeats=1 size=721 badsum=1 ifout=wan fwmark=60000000
packet: id=151 drop
вот внимательно посмотри.

---

**2026-02-16T11:46:03 | Routerich**
packet: id=59 len=855 mark=20000000 ifin=eth1.1(90) ifout=pppoe-domru(100)
IP4: 176.214.167.99 => 178.18.232.139 proto=tcp ttl=127 sport=55891 dport=443 flags=AP seq=2186540364 ack_seq=478824273
TCP: len=803 : BC 09 8A 41 47 09 29 19 AF F9 FD 4C D3 B0 7D 2D F1 B7 18 07 4E 03 B1 D5 0E 6C AE 1F BC D8 9F 20 ... : ...AG.)....L..}-....N....l.....  ...
client mode desync profile/ipcache search target ip=178.18.232.139 port=443
using cached desync profile 0 (no_action)
reassemble : feeding data payload size=803. now we have 2175/2175
TLS client hello is FULL
TLS record layer version : TLS 1.0
TLS handshake version : TLS 1.2
TLS supported versions ext : GREASE
TLS supported versions ext : TLS 1.3
TLS supported versions ext : TLS 1.2
TLS ALPN ext : h2
TLS ALPN ext : http/1.1
TLS ECH ext : present
DELAY desync until reasm is complete (#2)
REPLAYING delayed packet #1 offset 0
REPLAY IP4: 176.214.167.99 => 178.18.232.139 proto=tcp ttl=127 sport=55891 dport=443 flags=A seq=2186538992 ack_seq=478824273
TCP: len=1372 : 16 03 01 08 7A 01 00 08 76 03 03 08 8E 69 2D 7F 46 D8 2D D6 9D 9F E0 46 6C 31 92 2E 00 AD A4 2E ... : ....z...v....i-F.-....Fl1...... ...
client mode desync profile/ipcache search target ip=178.18.232.139 port=443
using cached desync profile 0 (no_action)
TLS client hello is FULL
TLS record layer version : TLS 1.0
TLS handshake version : TLS 1.2
TLS supported versions ext : GREASE
TLS supported versions ext : TLS 1.3
TLS supported versions ext : TLS 1.2
TLS ALPN ext : h2
TLS ALPN ext : http/1.1
TLS ECH ext : present
hostname: easylist-downloads.adblockplus.org
discovered l7 protocol
discovered hostname
desync profile search for tcp ip=178.18.232.139 port=443 icmp=255:255 l7proto=tls ssid='' hostname='easylist-downloads.adblockplus.org'
* hostlist check for profile 1 (youtube)
[/opt/zapret2/ipset/zapret_hosts_youtube.txt] include hostlist check for easylist-downloads.adblockplus.org : negative
hostlist check for adblockplus.org : negative
hostlist check for org : negative
* hostlist check for profile 2 (fake)
[/opt/zapret2/ipset/zapret_hosts_xcom.txt] include hostlist check for easylist-downloads.adblockplus.org : negative
hostlist check for adblockplus.org : negative
hostlist check for org : negative
* hostlist check for profile 3 (fake_disorder_work)
[/opt/zapret2/ipset/zapret_hosts_user.txt] include hostlist check for easylist-downloads.adblockplus.org : negative
hostlist check for adblockplus.org : positive
desync profile 3 (fake_disorder_work) matches
desync profile changed by revealed l7 protocol or hostname !
dpi desync src=176.214.167.99:55891 dst=178.18.232.139:443 track_direction=out fixed_direction=out connection_proto=tls payload_type=tls_client_hello
* lua 'fake_3_1' : out pos a0 a0 in range a0-a0
* lua 'fake_3_1' : payload_type 'tls_client_hello' satisfy filter
* lua 'fake_3_1' : desync
instance cutoff for 'fake_3_1' in=1 out=0
LUA: fake: 16 03 01 01 17 01 00 01 13 03 03 D5 AD 55 2B 42 C4 C6 A2 D5 46 22 F3 1B 3C 41 F6 E5 D9 F4 8F 86 ... .............U+B....F"..<A...... ... 
rawsend_dissect repeats=6 size=336 badsum=0 ifout=pppoe-domru fwmark=60000000
* lua 'multidisorder_3_2' : out pos a0 a0 in range a0-a0
* lua 'multidisorder_3_2' : payload_type 'tls_client_hello' satisfy filter
* lua 'multidisorder_3_2' : desync
instance cutoff for 'multidisorder_3_2' in=1 out=0
LUA: multidisorder: split pos: midsld+1
LUA: multidisorder: resolved split pos: 201
LUA: multidisorder: sending part 2 201-2174 len=1974 seqovl=0 : 6B 70 6C 75 73 2E 6F 72 67 00 33 04 EF 04 ED AA AA 00 01 00 11 EC 04 C0 05 C7 3E 3E 5C 1B FD 44 ... kplus.org.3...............>>\..D ... 
rawsend_dissect repeats=1 size=1424 badsum=0 ifout=pppoe-domru fwmark=60000000
rawsend_dissect repeats=1 size=654 badsum=0 ifout=pppoe-domru fwmark=60000000
LUA: multidisorder: sending part 1 0-200 len=201 seqovl=0 : 16 03 01 08 7A 01 00 08 76 03 03 08 8E 69 2D 7F 46 D8 2D D6 9D 9F E0 46 6C 31 92 2E 00 AD A4 2E ... ....z...v....i-F.-....Fl1...... ... 
rawsend_dissect repeats=1 size=253 badsum=0 ifout=pppoe-domru fwmark=60000000
DROPPING delayed packet #1

---

**2026-02-16T12:05:08 | Дмитрий Кобзарь**
У нас я так понял на выбор три приложения: podkop, zapret, zeroblock. С каким лучше заморочится

---

**2026-02-16T12:06:31 | Routerich**
Здравствуйте.
Podkop,zeroblock Это средства маршрутизации
а zapret это средство обхода DPI

---

**2026-02-16T12:14:17 | Дмитрий Кобзарь**
Т. е. Ставим podkop и zapret?

---

**2026-02-16T12:47:35 | Routerich**
пакеты  | полный мануал 
ZeroBlock 0.6.2-r91:
Надёжность загрузки
  - MAX_MULTI_ITEMS 64→256 (37 списков × 3 файла = 111 запросов)
  - HTTP_MAX_RESPONSE_SIZE 2MB→32MB (cdn_aws_ipv6.json — 17.6MB)
  - Поддержка прокси при загрузке community index в two-stage режиме

  Мониторинг и zapret2
  - Еженедельный интервал мониторинга
  - Безопасное восстановление zapret2: сохранение пользовательских стратегий, откат при провале DPI-теста(скоро)
  - Разделение установки zapret2 и мониторинга (zapret2_auto_strategies)

  Прочее
  - Корректная очистка cron-задач при остановке
  - Увеличен буфер nft batch до 10MB для больших рулсетов
  - Актуализирован список сообщества с github
  - Поправлен визуал списка стратегий(кнопки больше не живут своей жизнью)
#ZeroBlock

---

**2026-02-16T13:22:49 | Routerich**
zapret2 0.9.2-r39
  Полный рефакторинг теста на ограниченный поиск стратегий в blockcheck
  Добавлены поля pre/post в blockcheck
  Редизайн настроек и blockcheck
  Новые стратегии в базе
ожидайте в репозитории

---

**2026-02-16T13:41:59 | Скептик**
Анализ запущен: 2026-02-16 17:39:04
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.146 | YouTube IP:  64.233.164.93

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓0.00 MB / ↑0.22 MB
  Пинг (ya.ru via awg10): ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (77.88.55.242): 56 data bytes
  Программы в автозапуске: zeroblock zapret2

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
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
  Запускаем остановленные службы...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 64.233.164.93
    Name:       youtube.com
    Address: 64.233.164.190
    Name:       youtube.com
    Address: 64.233.164.91
    Name:       youtube.com
    Address: 64.233.164.136
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock списки       awg10 vpn: meta
  zeroblock списки     my_list vpn: porn,discord,twitter,hdrezka,tiktok,telegram,!_cloudflare,google_ai,google_play
  zeroblock списки       opera prx: geoblock,block
  Версия zeroblock: 0.6.2-r91
  zeroblock DNS/Bootstrap DNS: 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.2.1 (Прошивка: 24.10.5)
  CPU: 0.18 | RAM: 29% | NAND: 53% занято / 32.0M доступно
  # Автоматический рестарт tailscale
  0 6,18 * * * /etc/init.d/tailscale restart
  # Пингование тейла через Планировщик:
  */5 * * * * ping -c 3 100.93.0.151 > /dev/null 2>&1
  # Перезагрузка роутера по понедельникам в 3 утра.
  0 3 * * 1 sleep 70 && touch /etc/banner && reboot
  # ZeroBlock Bad Interface Monitor
  */10 * * * * /usr/bin/zeroblock bad_interface_check >/dev/null 2>&1
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-02-16T14:03:05 | Виктор Миронов**
Ну я сделал по инструкции настроил, потом  была ошибка или не ошибка хз Awg10   отображало N/A а не  мс  залез в полный мануал установил Zapret2  и TrustTunnel стал мс Awg под 300+

---

**2026-02-16T14:06:52 | Скептик**
Анализ запущен: 2026-02-16 18:04:16
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.84 | YouTube IP:  64.233.164.91

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.83 MB / ↑0.24 MB
  Пинг (ya.ru via awg10): 58.147 / 68.855 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock zapret2

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock списки       awg10 vpn: meta
  zeroblock списки     my_list vpn: porn,discord,twitter,hdrezka,tiktok,telegram,google_ai,google_play
  zeroblock списки       opera prx: geoblock,block
  Версия zeroblock: 0.6.2-r91
  zeroblock DNS/Bootstrap DNS: 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.2.1 (Прошивка: 24.10.5)
  CPU: 0.22 | RAM: 28% | NAND: 53% занято / 32.0M доступно
  # Автоматический рестарт tailscale
  0 6,18 * * * /etc/init.d/tailscale restart
  # Пингование тейла через Планировщик:
  */5 * * * * ping -c 3 100.93.0.151 > /dev/null 2>&1
  # Перезагрузка роутера по понедельникам в 3 утра.
  0 3 * * 1 sleep 70 && touch /etc/banner && reboot
  # ZeroBlock Bad Interface Monitor
  */10 * * * * /usr/bin/zeroblock bad_interface_check >/dev/null 2>&1
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-02-16T14:49:27 | Михаил**
Всегда говорил, что обходов должно быть как можно больше. Youtubeunblock + zapret2+ podkop с 7-ью разноплановыми секциями по идее должны свести с ума любой ии у провайдера.

---

**2026-02-16T15:42:54 | Anna Bagler**
Это вам, наверное, в теме zapret2 лучше написать, чтоб Fresa посмотрел, вдруг маркировку трафика надо подкрутить.

---

**2026-02-16T17:32:29 | DMITRIY**
И установить zapret и podcop

---

**2026-02-16T17:33:45 | DMITRIY**
Где скачать zapret2?

---

**2026-02-16T18:03:10 | Роман**
Система, пакеты, обновить списки, фильтр zapret2, установить 2 пакета.

---

**2026-02-16T18:14:01 | Максим**
А где стратегии искать? Вот тот же zapret2 работает везде, кроме телеков

---

**2026-02-16T18:14:28 | Anna Bagler**
Не надо бездумно все обновлять. Zapret2 как обычно в пакетах. Zero руками.

---

**2026-02-16T18:42:10 | OlegPers**
На компьютере тоже так же, работает только YouTube 
Как проверить что мешает? Дома весь день не был, пришел и вот не работаете, стоит zapret2

---

**2026-02-16T18:51:28 | Антон**
Вы не один я мучался долго и ни как установил Zapret1 от Stressozz

---

**2026-02-16T19:43:29 | Антон**
Да я на хистерии2 запускал все норм хочется бесплатно и нашел вариант Zapret от Stresozz бесплатно и все работает

---

**2026-02-16T20:20:09 | михаил**
Добрый вечер всем! Сегодня получил два этих замечательных девайса. Сижу разбираюсь. Вопрос, мне нужно настроить zapret2, по инструкции к запрету захожу в services, а там его нет. Перелопатил много тут уже сообщений. Подскажите как установить модули Запрета)

---

**2026-02-16T20:36:37 | Ильнур Фархутдинов**
Добрый вечер, помогите пожалуйста 
На роутере установлен форк zapret4rocket
На телефоне под iOS запрещенка работает 
На телевизоре TCL работает только Кинопоиск и вк Видео, даже попытка загрузки инструкции к телевизору выдает ошибку об отсутствии интернета...
В чем может быть причина?

---

**2026-02-16T20:48:24 | Валерий**
У меня вчера телек 30 мин на сером экране висел через zapret2, потом загрузился

---

**2026-02-16T21:37:17 | Vlad Mi**
А что делать если zapret и podkop не появились после установки пакетов?

---

**2026-02-16T22:21:00 | Ikа**
Ребят, помогите, пожалуйста, не могу понять в чем дело, в впн или настройки не докручиваю в роутере

Есть сайт, на котором блокируются по стране некоторые сериалы (пишет 404 server error), но если выбрать, например, Польшу, то все показывает.
В ВПН уверен, т.к. если тот же самый ключ вставляю в телефоне через приложение v2RayTun, то все работает на телефоне, а если вставляю его в секции (не важно, подпиской или чисто vless ключ) и указываю именно этот сайт для впн, то не работает все равно. Для теста, в эту секцию добавляю еще 2ip, он показывает что мое местоположение Польша, пробую в режиме инкогнито, чтобы кэш не мешал

У меня на чистую прошивку установлен только zeroblock 0.6.2-r30 и темная тема, в автонастройках еще zapret2

---

**2026-02-16T22:22:03 | Roman Vorobev**
Добрый вечер. Извините за глупый вопрос. В мануале на Зероблок написано:
Включите нужные опции:
• Install Opera Proxy — для секции opera
• Configure AmneziaWG WARP — для секции awg10
• Install Xray-core — опционально, для транспортов xhttp/mKCP
• Install TrustTunnel — опционально, TrustTunnel proxy
• Install Zapret2 — опционально, для обхода DPI

Вопрос такой, установка Xray-core и TrustTunnel желательна или нежелательна при том, что я не знаю что это и не понимаю надо это или нет? Ставить буду на чистый роутер от RR  прошитый последней прошивкой.

---

**2026-02-16T23:19:11 | Kiss_My_Axe**
Несколько странное, но спишем на глюки скрипта, он адаптируется под новые решения. :)
У вас zapret2 конфликтует со списком youtube в секции opera зероблока.
Или запрет2 стоп, или ютуб из опера убрать.

Секция awg10 в "Ловить всё"-режим переведена сознательно? Если нет, то вообще с неё галку снимите.

---

**2026-02-17T03:17:47 | sergey**
Здравствуйте. Ставил Zapret2 а смотрю пакеты там еще и zapret и luci-app-zapret установлены, так и должно быть или их удалить ?

---

**2026-02-17T13:59:00 | Dmitriev Viktor**
Привет! Скажите пожалуйста где проверить и что поменять, поставил Zapret2, на телефонах и ноутбуке ютуб открывается, на телевизоре нет. ВайФай рутерих на телеке переподключил...

---

**2026-02-17T16:10:11 | Kiss_My_Axe**
Поставьте руками запрет от ремиттор, если вам запрет2 не подходит.
remittor zapret github
После установки в морде запрета жмите ресет, там все галки как есть оставьте, а вот стратегии переключайте.
Выбрав страту соглашайтесь и проверяйте доступ.
Нет доступа - ресет и следующая страта.
Так победим! :)

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

**2026-02-17T19:23:29 | Anna Bagler**
Пробуйте отключить и остановить youtubeUnblock и поставить zapret2. Проверить. Если не поможет, то закрепы темы zeroblock и через него.

---

**2026-02-17T19:24:25 | Святос**
Владельцам ТВ Самсунг, Сони и ЛЖ вместо Zapret: https://github.com/Anonym-tsk/nfqws-keenetic

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

**2026-02-17T19:44:40 | Андрей Константинов**
Не хочет zapret2 ставить

---

**2026-02-17T19:58:11 | Mikhail Tikhomirov**
Сначала идете система - пакеты, жмёте обновить список пакетов, потом в фильтре zapret2 и ставите сам запрет и люси к нему

---

**2026-02-17T19:58:52 | vladimir**
Приветствую Вас! Сегодня получил еще два замечательных роутера!15 минут и оба отправились отцу и тестю в семью, поскольку те, заинтересовавшись открывающимися перед ними возможностями теперь станут выносить мозг нашей любимой техподдержке 🤗🤗🤗😂😂😂Клянусь-своими силами не допускать подобных безобразий и решать возможные возникающие проблемы своими силами, путем курения мануалов(Курение убивает😂😂😂)Ну а уж если и придется обратиться не откажите в любезности направьте в ZeroBlock или Zapret 2😂😂😂p.s("шепотом" правда моим отцам и podkop'a за глаза хватает👍👍👍)

---

**2026-02-17T20:18:24 | Симеона**
В ZeroBlock пинг в секции opera - 364ms и в секции awg10 -  486ms - это нормально? Все работает, только Zapret2 нигде не появился, хотя стоит галочка, что установлен. Сверху справа в интерфейсе надпись "Обновляется" очень долго висит. Нужно ждать, пока она уйдет?

---

**2026-02-17T20:28:33 | Bullet for my valentine Poison**
Так в нем надо еще работать с подбором стратегий, для этого нужно читать мануал. Попутно тыкая в интерфейс Запрета. Плюс бонусом сюда смотреть. https://github.com/bol-van/zapret2/blob/master/docs/manual.md#введение

---

**2026-02-17T21:44:21 | Maksim**
Такой вопрос
сегодня обновил роутер
я по умл ставлю только Zapret
и не понимаю с чем связано
до обновления дискорд работал нормально
после обновления роутера работает все кроме дискорда
если запускаю стратегию чисто на компьютере, дискорд нормально открывается
добавляю эту стратегию уже в роутер, то бескончится крутится на проверке обновления

upd. разобрался в чем дело
всему виновник youtubeUnblock, который я думал, что не установлен, так как в GUI в службах не обновлялся
его удаление все исправило

---

**2026-02-17T23:41:34 | А**
Добрый вечер.  Установил  Zapret2, ютуб с телефона работает, а на телевизоре через андройд-приставку нет. Куда копать?

---

**2026-02-18T12:03:43 | Routerich**
а если zapret стопнуть?
если не поможет тогда перекидывать список youtube в секцию opera, но будет реклама на ютубе

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

**2026-02-18T12:15:14 | Routerich**
да как вам угодно, можете потом проверить перекинув обратно или переходите на Zapret2 удалив из Podkop список youtube

---

**2026-02-18T12:16:41 | Routerich**
сложно сказать, для zapret нужно искать стратегии пробовать, читать мануал.

---

**2026-02-18T13:23:54 | Василий**
Добрый день. В Zapret2 можно настроить что-то подобное по образу-подобию Zapret-Manager, чтобы весь трафик шел в запрет кроме исключений? За дурилки не сильно шарю

---

**2026-02-18T13:58:56 | Routerich**
а если остановить zapret2 работает?

---

**2026-02-18T14:48:38 | Anna Bagler**
Zeroblock и zapret2.

---

**2026-02-18T16:36:50 | Алексей**
Ребята, привет

Давно слежу за проектом, ещё с тех пор когда в прошивке не было всяких обходов. Учитывая текущие законы в РФ в плане ответственности за рекламу/распространение способов обхода блокировок, возникает резонный вопрос: как проект, оформленный на российское ИП, продолжает существовать, учитывая эти факторы? 

Как разработчиков ещё не "прижали" за встроенный Zapret и прочее? Не хочу никого обидеть, просто интересно, как проект смог выжить в текущих реалиях

---

**2026-02-18T17:16:18 | Борис**
Я правильно понимаю, что если для стратегии не выбрать домены/ip для применения, то zapret2 будет перехватывать весь трафик, даже предназначенный для локальной сети? localhost и 192.1.*

---

**2026-02-18T18:10:54 | Anna Bagler**
Запрет отключить и остановить. В планировщике строчку с restart zapret удалить.

---

**2026-02-18T18:45:13 | Bullet for my valentine Poison**
https://github.com/bol-van/zapret2/blob/master/docs/manual.md#введение тут можно почитать.

---

**2026-02-18T20:22:06 | Bullet for my valentine Poison**
https://github.com/bol-van/zapret2/blob/master/docs/manual.md#введение это раз.

---

**2026-02-18T20:30:59 | Denis Pishchur**
Zapret после выполнения скрипта №5 установился, но отключен. Так и должно быть?

---

**2026-02-18T20:36:32 | Anna Bagler**
Это не проблема, если хотите именно через запрет, то убирайте список yt из подкопа и ищите тут автоконфигуратор для zapret, пусть подбирает вам стратегии, а вы проверяйте.

---

**2026-02-18T22:00:25 | Руслан**
Приветствую! Подскажите пожалуйста, хочу понять направление, в какую сторону двигаться и что изучить, получил сегодня роутер Routerich ax3000 и хочу настроить так, чтобы Дискорд, Ютуб и всё остальное работало, что для этого нужно? Zapret2 или zeroblock или podkop или что-то ещё?

---

**2026-02-18T23:03:09 | Александр П.**
Оставлю это тут.  zapret сам по себе доступ к Инсте не даёт, ему нужно "помогать" в файле hosts, по другому я не смог.
Идеально работала Инста долгое время, пока в феврале что-то снова не сломалось, перестала работать на ПК в браузере. 
При этом "zapret" спокойно её маскировал в телефонной версии и она работала. Изменение конфига zapret к результату не приводило.

Решение: в файле hosts был прописан конкретный IP инсты, а именно: 157.240.245.174.
Вместо 157.240.245.174 (который теперь не пингуется, может раньше тоже не пинговался) прописать 31.13.84.174 (Hungary, Nyiregyhaza)
И на ПК снова заработала инста:

31.13.84.174 instagram.com
31.13.84.174 www.instagram.com
31.13.84.174 b.i.instagram.com
31.13.84.174 z-p42-chat-e2ee-ig.facebook.com
31.13.84.174 help.instagram.com

---

**2026-02-18T23:24:14 | Святос**
Вот например из zapret2 дискорд
--new
--filter-tcp=80,443,1080,2053,2083,2087,2096,8443
--hostlist=/opt/etc/nfqws2/lists/discord.list
--out-range=-d10
--lua-desync=hostfakesplit_multi:hosts=google.com,vimeo.com:tcp_ts=-1000:tcp_md5:repeats=2

---

**2026-02-19T06:16:53 | Danil**
С такой же ситуацией столкнулся вчера после обновления. Были конфликты со старыми файлами (conffile) singbox, zeroblock и ещё что-то там. ZB после установки не запустился. Сначала удалил zapret2, так как думал, что это в нем проблема, но это не помогло. После этого и zapret2 через zeroblock не хотел устанавливаться. 
Решил действовать кардинально. Обновил прошивку до последней без сохранения настроек. Потом накатил zeroblock. Все заработало.

---

**2026-02-19T10:49:25 | Скептик**
Парни, а есть какой-то вариант, не углубляясь в изучение структуры стратегий, транслировать стратегию из ByeDPI в Zapret2?
Есть старые рабочие стратегии оттуда...

---

**2026-02-19T10:53:18 | Routerich**
нет, из всех людей я знаю только разработчика zapret2, он их на лету конвертит в голове. а так думаю будет очень сложно, потому что байдпи основывается на особенностях хост системы очень сильно

---

**2026-02-19T11:01:15 | Petr Shcherbinin**
Анализ запущен: 2026-02-19 10:58:52
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
  Facebook IP:  198.18.1.231 | YouTube IP:  198.18.2.30

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.18 MB
  Пинг (ya.ru via awg10): 6.666 / 13.109 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock zapret2

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Внутреннее пересечение в zeroblock:
    zeroblock                 : vless (Условия: default)
    zeroblock                 : vless (Условия: default)
    Домены: googlevideo.com youtube.com 

  zeroblock          vless (prx url): !!!_russia_inside,!_russia_outside,geoblock,block,porn,news,!!!_youtube,discord,meta,twitter,hdrezka,telegram,!_cloudflare,hetzner,digitalocean,google_ai,google_play
  Версия zeroblock: 0.6.4-r8
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.73 | RAM: 25% | NAND: 47% занято / 35.5M доступно
  # ZeroBlock Bad Interface Monitor
  */10 * * * * /usr/bin/zeroblock bad_interface_check >/dev/null 2>&1
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 * * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

root@RouteRich:~#

---

**2026-02-19T12:05:10 | Routerich**
Здравствуйте.
https://github.com/bol-van/zapret2#%D1%87%D0%B5%D0%BC-%D1%8D%D1%82%D0%BE-%D0%BE%D1%82%D0%BB%D0%B8%D1%87%D0%B0%D0%B5%D1%82%D1%81%D1%8F-%D0%BE%D1%82-zapret1

---

**2026-02-19T12:11:47 | Павел**
Спасибо! А для ещё только вставших на путь стремления к совершенству (тупых, короче) там нет что-то типа ZapretManager, с помощью которого я подбираю стратегии для обычного запрета? Там сей процесс сложнее?

---

**2026-02-19T12:39:10 | Vasa**
если честно, то его нету.  по факту это "реальный опыт сетевого инженера" от 10 лет...))

можете почитать на офф  страницах  на гитхабе

про подкоп

и про Zapret2

и как они устроены и работают

---

**2026-02-19T13:34:32 | Борис**
Кто-нибудь сталкивался с тем, что запрет мешает программе Postman работать? такая комбинация postman + zapret не гуглится в интернете, и в поиске по сообщениям не нашёл. Может быть кто-то сталкивался и мог победить это у себя? Пробовал в список исключений добавлять очень много его доменов (мониторил сеть и обращения), всё равно postman начинает работать только если отключить запрет (причём полностью)...

---

**2026-02-19T16:01:14 | Кирилл**
Привет, установил на роутер zeroblock и zapret2. zeroblock ругался при диагностике на youtubeUnblock, вырубил его. И вроде как сейчас все работает (не знаю на сколько качественно еще), кроме телеги. подскажите пожалуйста как пофиксить телегу и что еще нужно сделать, чтоб было огонь)

---

**2026-02-19T16:21:19 | Станислав Земляков**
Всем привет. Набросал прототип MCP сервера для zapret2, может кому интересно было бы подключить к своему агенту. Тут ссылки на гитхаб оставлять можно?

---

**2026-02-19T16:37:45 | Станислав Земляков**
Мне помогло настроить, может ещё кому поможет: https://github.com/rcd27/zapret2-mcp

---

**2026-02-19T16:56:35 | Rom@n**
root@RouteRich:~# zeroblock global_check

══════════════════════════════════════════════════════════════
              GLOBAL CHECK - ZeroBlock
══════════════════════════════════════════════════════════════

-- Core Services -----------------------------------------

Internet (ICMP)          ✓ OK
Sing-box Process         ✓ Running (PID: 28942)
Sing-box DNS Port        ✓ 127.0.0.42:53
Sing-box TPROXY Port     ✓ :2154

-- DNS ---------------------------------------------------

DNS Resolution           ✓ OK
FakeIP:
  One                  ✓ facebook.com -> 198.18.1.40
  opera                - No domains
  awg10                - Disabled
  ProtonAWG            - No domains
  Podpiska             ✓ rutracker.org -> 198.18.1.41
Bootstrap DNS            ✓ 77.88.8.8 working
Dnsmasq Config           ✓ Configured

-- NFTables ----------------------------------------------

NFT Table                ✓ inet zeroblock
NFT Chains               ✓ 4 chains
External Mark Rules      ✓ 6 rules

-- Policy Routing ----------------------------------------

IP Rule (fwmark)         ✓ Active
Route Table              ✓ Configured
TPROXY Local Route       ✓ Active

-- Proxy & VPN -------------------------------------------

VPN Interfaces:
  awg10                  ✓ UP (awg10)
    └─ Ping              ✓ OK
  ProtonAWG              ✓ UP (ProtonAWG)
    └─ Ping              ✓ OK
Opera Proxy              ✓ Running
  └─ HTTP via Proxy      ✓ OK
Zapret2 (DPI)            ✓ Running
  └─ DPI Test            ✓ Bypassed

-- Configuration -----------------------------------------

Routing Sections         ✓ 5 configured
Sing-box Config          ✓ 5 files
Clash API                ✓ 20 proxies
WG Endpoints             ✓ 3 configured

══════════════════════════════════════════════════════════════
  TOTAL:  OK: 27    Errors: 0     Skipped: 3
══════════════════════════════════════════════════════════════

  ✓ All systems are working normally

---

**2026-02-19T18:41:40 | Денис**
роутер xiaomi r4a openwrt 24.10.5
скрипт на установку Zapret   v72.20260207

---

**2026-02-19T19:19:58 | Fos**
В общем сейчас перепрошил роутер с нуля и ютуб заработал на приставке. Вчера просто из коробки накатил ZB+Zapret2. Всё взлетело на ПК, смартфонах, но на приставке не работал ютуб. 

Сейчас сбросил на завод и сначала накатил скрипт 5, затем ZB+Zapret2 (подкоп выключил). И почему-то ютуб завелся и на приставке тоже. 

Правда, ASU не хочет сборку давать, ошибка, но это уже другая история

PS Zapret1 остановлен, как и подкоп

---

**2026-02-19T21:17:02 | Андрей Константинов**
Недолго музыка играла, после устоновки и включения zapreta2 и скрипта 5 вчера перестал вкл ютуб, сбросил настройки установил бету, ютуб работал ровно один вечер, сейчас даже не заходит в приложение на ТВ

---

**2026-02-20T10:05:07 | Routerich**
Здравствуйте.
Возможно у вас ещё что то установлено для ютуба.
Youtubeunblock, Zapret, zapret2?

---

**2026-02-20T10:15:55 | リンゴ**
Анализ запущен: 2026-02-20 10:14:36
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  57.144.68.1 | YouTube IP:  198.18.0.43

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.17 MB
  Пинг (ya.ru via awg10): 25.563 / 26.649 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock zapret2

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock              awg10 (vpn): meta
  zeroblock          opera (prx out): geoblock,block,youtube
  Версия zeroblock: 0.6.4-r8
  zeroblock DNS/Bootstrap DNS: (doh) extended.dns.mullvad.net/dns-query / 9.9.9.9

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.72 | RAM: 24% | NAND: 51% занято / 32.7M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

теперь нидерланды показывает на ютюбе после проверки...

---

**2026-02-20T10:18:12 | Routerich**
У вас zapret2 установлен и функционирует.
Вам надо галочку с автонастройки zapret2 снять, и выключить его и остановить.

---

**2026-02-20T10:34:09 | Kiss_My_Axe**
/etc/config/zapret <- файл
/opt/zapret <- директория

Забрать с одного, положить на другой.

---

**2026-02-20T14:28:29 | Routerich**
zapret тоже

---

**2026-02-20T17:48:08 | Kiss_My_Axe**
Откройте терминал.
Вставьте строку
service zapret2 stop && service zapret2 disable

---

**2026-02-20T19:18:11 | Routerich**
нет, zapret в дефолте работает по том и 443, он не имеет отношения в смерти авг

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

**2026-02-20T19:57:30 | ProstoDjonni**
Добрый день, как и обещал сегодня как только получил роутер сделал тестирование тытрубы на лыже. Входные данные: провайдер МТС (оптика), WebOS 04.40.92. тытруба от 02/10/2023. Zapret2------В основной список(лист) добавил следующие строки:    accounts.youtube.com
i.ytimg.com
s.youtube.com
googleads.g.doubleclick.net

---

**2026-02-20T20:02:30 | ProstoDjonni**
на zapret  (обычный)--- Изменил только 1 параметр: MODE_FILTER   = autohostlist.  Обратил внимание что в таких конфигах, тытруба с Z2 работает на лыже (было 2 подвисания на 5 сек), на мобиле (прогрузка карточек примерно 30 сек) , но в мазиле-через раз. обычный Z у меня повел себя нормально. попробую при обновлении тытрубы на лыже перехватить ссылкуна установочный пакет и ipk и посмотреть основной домен какой, и через эмуляцию прочекать еще какие есть.

---

**2026-02-20T20:46:34 | Anton Kadochnikov**
Всем привет. Сегодня получил новенький роутер и решил с ним позаниматься. Первичные настройки, в том числе wifi. Домашние устройства подцепились. Пока ковырялся с пакетами (podkop, zapret) заметил, что отключился iphone. Android работает, а этот нет. Из настроек wifi установил канал автомат и шифрование WPA2/WPA3. Если поставить только WPA2, то всё работает. Пробовал сбрасывать и не помогает. Если поставить ax3000t, то с такими же настройками проблем нет. Кто сталкивался с похожим?

---

**2026-02-20T20:55:18 | Dim-soft**
Подскажите, реально запустить ZeroBlock на FriendlyElec NanoPi R3Sпод FriendlyWrt ?
автоустановка не сработает, но если opera proxy и zapret2 руками установить ?

---

**2026-02-20T21:13:45 | Kiss_My_Axe**
Службы - Zapret2
Первая вкладка слева.
Первая кнопка слева - Включить автозапуск.
Нажать.

---

**2026-02-20T21:38:35 | S W**
Ну сначала хочу выразить свою благодарность за ответ, спасибо, уже не в первый раз выручаете 

Мне первый вариант больше нравился, но не успел дочитать)
Сервер просто слабый в нидерландах (100 руб в месяц), не хотел бы его грузить всем трафиком

Думаю над реализацией VLESS + zapret2 (дискорд, ну и в целом все для udp (игры там))

---

**2026-02-20T22:51:58 | это губер**
Я же правильно понимаю что при использовании зероблока действие zapret2 распространяется только на заблокированные сайты? Бывает что с ним не открываются некоторые сайты

---

**2026-02-21T14:03:03 | Роман**
Из коробки стоит youtubeunblock, установить к нему веб интерфейс через система - пакеты - обновить списки - фильтр youtubeunblock - установить второй файл. Остановить youtubeunblock, через пакеты скачать zapret2 и протестировать его.

---

**2026-02-21T14:44:36 | Anton Kadochnikov**
Есть ещё жестче - где проблемы с play market и с google. Я когда пользовался на ПК программой вроде zapret, то замечал, что не так часто приходится менять стратегии. Иногда какие-то сайты не хотят открываться (например openwrt.org), но уже привык.

---

**2026-02-21T15:09:24 | Anna Bagler**
Галочку на zapret2 можете поставить в автонастройке и посмотреть на YouTube.

---

**2026-02-21T15:20:41 | 🐙**
Здравствуйте, подскажите пожалуйста, куда нужно вставлять стратегии из Zapret2, чтобы работал ютуб?

---

**2026-02-21T15:44:30 | Борис**
Для пк есть инструкция по конфигурации zapret специально для роблокса: https://github.com/Flowseal/zapret-discord-youtube/discussions/8673

А также есть отдельный форк zapret-roblox https://github.com/Lux1de/zapret-roblox

Нюанс: эти программы сделаны под windows. Но под капотом используют всё тот же zapret с его инструкциями. Поэтому на вашем месте я бы сделал реверс-инжиниринг и портировал эти стратегии к себе на роутер. Уверен, вы сможете

---

**2026-02-21T16:41:11 | Routerich**
Подбирайте стратегию для ютуба в zapret2  через blockcheck

---

**2026-02-21T17:13:01 | Marseille Geertje**
А что значит использовать запрет? Где почитать? 🤔 Скрипт 5 же это устанавливает. И пункт Zapret появляется в службах. И он запущен написано.

---

**2026-02-21T18:16:29 | Routerich**
Здравствуйте.
Попробуйте отключить Podkop, Zapret и проверить

---

**2026-02-21T18:34:19 | Routerich**
Через Zapret идёт?

---

**2026-02-21T18:38:39 | Routerich**
Ну тогда используйте WARP, зачем вам zapret?

---

**2026-02-21T20:46:29 | Марсель Сайфиев**
Ребят, сразу извиняюсь за глупый вопрос. Но тут появились темы про zapret2 и zeroblock. На что стоит переходить? Или лучше оставаться на стандартных версиях?

---

**2026-02-21T21:41:14 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.6.4-r39:
  API v2(недоступно для не RouteRich устройств)
  - API v2 по умолчанию + переключатель V1/V2 в LuCI
  - Выбор типа cidr в настройках  для дополнительной маршртизации(ipv4/ipv6)
  - Детекция смены API версии через кэш индекса — автоинвалидация при переключении
  - Списки сообщества от RouteRich
  - Недоступность v2-only опций (sections_auto_load, zapret2_auto_strategies) при API v1

  Автонастройка стратегий Zapret2(api v2)(скачивает уже новые, если они есть, стратегии)
  - Скачивание blob/lua архивов через API
  - Динамический URL DPI проверки вместо хардкода
  - Таймаут DPI вынесен в UCI (dpi_check_timeout, дефолт 15 сек)
  - Исправлен rollback стратегий при неудачном recovery — отключение вместо удаления
  - Удаление luci-app-youtubeUnblock при автоустановке zapret2

  Секции и дедупликация
  - Автозагрузка секций каждый перезапуск пытается привести секции к ответу сервера
  - Дедупликация серверных секций с пользовательскими (7 полей)
  - force_enabled от сервера для принудительного включения секций
  - Пустые секции после дедупликации автоматически отключаются
  - Пропуск секций с неустановленными зависимостями (Opera/awg10)
  - Кроссекционная дедупликация text полей: разбор comma-separated значений
  - Блокировка сохранения при дубликатах в DynamicList

  Сеть и маршрутизация
  - Миграция fwmark/ct mark на высокие биты (16-18) — устранение конфликтов с mwan3(не тестировалось)
  - Mixed proxy на всех source_network_interfaces вместо хардкода br-lan(fallback 0.0.0.0/0)
  - Фильтрация LAN интерфейсов в Custom Output по source_network_interfaces
  - Умная фильтрация Incoming Interfaces — скрытие портов бриджей

  Прокси
  - Исправлена генерация TLS для shadowsocks (sing-box не поддерживает)
  - Force CIDR для messengers и discord(если включен discord voice) в inline ruleset
  - PID-файлы для xray/trusttunnel — убивать только свои процессы

  Custom sing-box конфиг
  - Пользовательские JSON фрагменты из /etc/zeroblock/sing-box.d/
  - Копирование с префиксом 50-custom-*, права 600

  Прочее
  - Устранены утечки памяти в LuCI (dashboard, diagnostic store subscriptions)
  - Порядок очистки в config_stop — удаление dnsmasq конфигов до перезапуска
  - Метка (wan) в выборе интерфейсов
#ZeroBlock

---

**2026-02-21T23:42:55 | Vasa**
у меня отсюда
https://github.com/GubernievS/AntiZapret-VPN/tree/main/setup/root/antizapret/download

---

**2026-02-22T00:31:39 | Aleksey Lip**
Здравствуйте, в зероблок при диагностике на zapret2 пишет "Cannot read desync_mark" в чем ступил?

---

**2026-02-22T12:50:51 | Александр Ткаченко**
Добрый день, установил новый Zb поставил авто настройку zapret2 по итогу Ютуб сломался, если возвращать галочку на просто Ютуб то начинает работать, подскажите в чем может быть проблема ?

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

**2026-02-22T16:03:00 | Routerich**
Службы - zapret - остановить и выключить автозапуск, далее в подкопе в секции с названием дискорд добавить список YouTube - применить

---

**2026-02-22T16:11:15 | Dark Ghost**
Народ, ай нид юр хелп, плиииз...
В чём, помимо проверенного и указанного ниже может быть проблема?
Железо - "v0" (256 мб)
Прошивка - RouteRich 24.10.5 r29087-d9c5716d1d RR-3.9.0 / LuCI openwrt-24.10 branch 26.039.68875~ec3d818 
Сверху - zeroblock 0.6.4-r39 + luci-app-zeroblock 0.6.4-r39 и zapret2 0.9.4.1-r2 + luci-app-zapret2  0.9.4.1-r2
Wan6 - получает свои честные 2a00: и PD
Локальные хосты - получают свои 2а00:, построенные из PD (ну и "местные" из ULA, естественно)
Ни один сайт с диагностикой, типа 2ip.ru, whatismyip.help и т.д отображать v6 не желает, test-ipv6.com и www.ipv6-test.com - тупо пытаются что-то проверить, но сваливают по таймауту.
disable_ipv6 в автозагрузке, естественно, отключен.
Проверил "Фильтровать IPv6-записи типа AAAA" - отключено.
В "Правила для трафика" - тоже не вижу ничего, что могло бы не пускать наружу.
Куда ещё можно/нужно посмотреть?

---

**2026-02-22T18:17:42 | Routerich**
Аналог goodbye dpi, zapret. Поставьте пакет luci-app-youtubeUnblock

---

**2026-02-22T18:45:29 | Routerich**
Здравствуйте.
Пробуйте zapret2

---

**2026-02-22T20:29:06 | Борис**
я отчёт в теме wifi не стал создавать - решил ещё потестить. В общем, моя лампочка "плохо" работала из-за Zapret2 (стоит стратегия на весь трафик кроме исключений). Но вот я зашёл в Статус - Мониторинг - Журнал URL адресов и вижу такой домен "mijia cloud" - как это вообще возможно? Я про пробел. И как это в запрет загнать...

---

**2026-02-22T21:37:54 | Routerich**
я использую богомерзкий fakeip только из-за chatgpt, волосы мягкие и шелковистые
══════════════════════════════════════════════════════════════
              GLOBAL CHECK - ZeroBlock
══════════════════════════════════════════════════════════════

-- Core Services -----------------------------------------

Internet (ICMP)          ✓ OK
Sing-box Process         ✓ Running (PID: 26170)
Sing-box DNS Port        ✓ 127.0.0.42:53
Sing-box TPROXY Port     ✓ :2154

-- DNS ---------------------------------------------------

DNS Resolution           ✓ OK
FakeIP:
  tun2opera            ✓ chatgpt.com -> 198.18.0.6
  tun2xray             - Disabled
  tun2tor              - Disabled
  warp                 - Disabled
  dns_from_vps         - Disabled
  dns_malw_link        - Disabled
  subscription         ✓ bla.cadabra -> 198.18.1.218
  url_test             ✓ babla.ctm -> 198.18.1.219
  from_coder           - Disabled
  trust_tunnel         ✓ babbb.la -> 198.18.1.221
Bootstrap DNS            ✓ 77.88.8.1 working
Dnsmasq Config           ✓ Configured

-- NFTables ----------------------------------------------

NFT Table                ✓ inet zeroblock
NFT Chains               ✓ 4 chains
External Mark Rules      ✓ 13 rules

-- Policy Routing ----------------------------------------

IP Rule (fwmark)         ✓ Active
Route Table              ✓ Configured
TPROXY Local Route       ✓ Active

-- Proxy & VPN -------------------------------------------

VPN Interfaces:
  warp                   ✓ UP (warp)
    └─ Ping              ✓ OK
  pppoe-domru            ✓ UP (dns_from_vps)
    └─ Ping              ✓ OK
  tun2opera              ✓ UP (dns_malw_link)
    └─ Ping              ✗ No response
Opera Proxy              ✓ Running
  └─ HTTP via Proxy      ✓ OK
Zapret2 (DPI)            ✓ Running
  └─ DPI Test            ✓ Bypassed

-- Configuration -----------------------------------------

Routing Sections         ✓ 13 configured
Sing-box Config          ✓ 5 files
Clash API                ✓ 49 proxies
WG Endpoints             ✓ 7 configured

══════════════════════════════════════════════════════════════
  TOTAL:  OK: 30    Errors: 1     Skipped: 6
══════════════════════════════════════════════════════════════

  ✗ Problems detected: 1

---

**2026-02-22T22:22:08 | Black-Angel**
Всем привет. Установил Zapret 2  настроил, всё работает кроме instagrama, не могу подобрать стратегию.

---

**2026-02-22T23:27:52 | Vadim**
Добрый день! При установке скрипта №5 на новый роутер вылетела ошибка:
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:--  0:02:00 --:--:--     0
curl: (28) Connection timed out after 120002 milliseconds
zapret not work...
Так и должно быть? Если нет, то как это исправлять? Установка завершилась успешно, но служба запрет остановлена.

Подключение к провайдеру по статическому IP. Интернет работает, основные закрытые сайты после установки скрипта №5 заработали.

---

**2026-02-23T04:00:48 | Максим Красовский**
Добре!
Установил последнюю прошивку.
Мастер начальной настройки - это выше всяких похвал!
Настроил wifi, отключил ip6 и проверил автозагрузку, удалил p910, добавил zapret2+luci+руссификация, добавил luci для ютубблока и выключил его, поставил время и зону, дал имя роутеру, обновил пакеты и установил некоторые.
Все страницы (обзор, инфо, ...) работают быстро и точно быстрее декабрьской прошивки.
Две штуки ещё не сделал - не нашёл поле куда в подкопе свой список вставлю (шикимори всякие и тп) и ещё потерял сообщение парня где он расписал пакеты для удаления модемного всего.
Ютуб работает. Ради этого всё и писалось (с).
Спасибо.

---

**2026-02-23T06:13:51 | Routerich**
Здравствуйте.
А youtubeunblock при этом работает?
Zapret2 галочку ставили на установку его?

---

**2026-02-23T08:31:26 | Юрий**
Отключал в секции awg10 youtube, решил попробовать через zapret2. Затем отключил  запрет и вернул ютуб в секции авг. После проверки скриптом появилось внутреннее пересечение доменов. Откуда взялось пересечение? 
И второй вопрос:  разве пинг до ya.ru должен идти через фейкфайпи? 
nslookup ya.ru
╤хЁтхЁ:  RouteRich.lan
Address:  192.168.1.1

╚ь :     ya.ru
Address:  198.18.0.23

---

**2026-02-23T10:30:15 | Ø**
всем привет. сегодня установил последнюю версию прошивки, а также zapret2 и zeroblock, и всё из списков zeroblock работает нормально, кроме всего, что связано с гугловским ИИ. любые другие геоблокнутые сайты (chatgpt, grok, intel.com) работают нормально. в инкогнито на gemini.google.com при попытке сгенерировать ответ получаю 1060. на пятом скрипте с подкопом, до того как я обновился, всё работало. ручной список из доменов с itdoginfo/allow-domains создавать пробовал, тоже не помогло

---

**2026-02-23T12:55:44 | Mongolor**
Добрый день! Обновил прошивку со сбросом настроек на 3.9.0 usb 2.0

установил zapret2 и гуи для него, внутри включил дефолт галочку. 
на заблокированные сайты теперь сеть ходит через иностранные ip адреса. 
хотелось бы понимать через что это работает. 

Спасибо!

---

**2026-02-23T13:30:12 | technique xxxxx**
Добрый день, установил на роутер podkop+zapret, youtube и сайты работают на телевизоре и компьютере,но на телефоне ничего не хочет открывать, в чем может быть причина ? DNS роутера стоит для всех устройств.Спасибо.

---

**2026-02-23T13:43:09 | technique xxxxx**
Добрый день, установил на роутер podkop+zapret, youtube и сайты работают на телевизоре и компьютере,но на телефоне ничего не хочет открывать, в чем может быть причина ? DNS роутера стоит для всех устройств.Спасибо.

---

**2026-02-23T17:39:29 | Rom@n**
Фреса такой вопрос, а ZB может мне как то списки восстановить/создать в zapret 2 или галочка в автонастройке (Автонастройка стратегий Zapret2) не об этом. Просто собрал прошивку чрез ASU запихал туда в том числе и запрет 2, потом ручками накатывал ZB. Открываю некоторые сайты и не понимаю по чему они не открываются (те которые должны ходить на прямую, например сайт Росреестра). Ну начал отключать зероблок, все равно не открываются, дошел до запрета 2 смотрю, а там списков нет совсем.

---

**2026-02-23T17:52:44 | Илья Семашко**
Все оказалось до стыдного банально🤦‍♂️ пол года назад ставил службу zapret. Отключил и забыл, в какой то момент она решила включиться))

---

**2026-02-23T18:45:54 | Rom@n**
Интересно, а как так получилось, что установленная прошивка через ASU в котором есть пакет zapret2 имеет стратегии но не имеет списки. Можно как то восстановить как по умолчанию?

---

**2026-02-23T19:46:43 | Nikita Prokofev**
Правильным ли я путем иду? Накидываю все что мне надо в zapret2 или это эникей?

---

**2026-02-23T20:09:27 | Tema**
Здравствуйте, имею два роутера routerich ax3000 v1, один роутер с прошивкой 24.10.4, на нем настроен zapret и https-dns-proxy, работает YouTube, discord и тд. На втором роутере прошивка 24.10.5, установлен zapret и https-dns-proxy, с теми же настройками как у первого роутера, только тут не работает YouTube и discord. Интернет и компьютер один и тот же, ни как не могу понять почему на втором ни чего не работает

---

**2026-02-23T21:42:16 | Den**
С включенными Автозагрузкой секций и Автоматическим мониторингом и восстановление стратегий Zapret2 через API после перезагрузки ZB все галки выбора разделов в секциях опера и авг возвращаются к исходному состоянию. Т.е. если я там поотключал ненужные разделы, то после перезагрузки ZB они снова включены...

---

**2026-02-23T22:19:33 | Den**
Не нашел такой. Есть Автозагрузка секций и Автонастройка стратегий Zapret2, Zapret отключен.

---

**2026-02-23T22:45:42 | Vasa**
ну можешь отправить им весь амазон + cf + digitalocean + hetzner + akamai + fastly в впн и все проблемы решатся на 99% сразу

тупо отсюда все CDN ))
https://github.com/GubernievS/AntiZapret-VPN/tree/main/setup/root/antizapret/download

---

**2026-02-23T23:55:50 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.6.4-r60:
  Диагностика Outbounds — полностью новая(но старые космические значения)
  - Параллельная проверка доступности всех proxy/VPN серверов (TCP connect + netlink)
  - Для subscription/urltest — определение активного прокси через Clash API
  - LuCI показывает статус, протокол, адрес и латентность каждого outbound

  FakeIP — автоматическая защита
  - Catch-all секция без exclusions автоматически отключает FakeIP, чтобы устройства получали реальные IP
  - Early DNS bypass перенесён из singbox_generator в lists_loader с domain-фильтрацией (source_ip_cidr + rule_set → dns-main)
  - Добавлен dns-local (dnsmasq fallback) для fully_routed устройств — .lan, /etc/hosts, кастомные записи

  NFT community subnets + DNS bypass
  - Исправлен fallback на JSON формат v2 API — NFT sets теперь создаются корректно
  - aggregate_ipv4_to_24 сохраняет широкие CIDR (маска ≤24) без изменений
  - NFT DNAT rules: fully_routed IPs → sing-box dns-in напрямую (минуя dnsmasq, сохраняя source IP)(полный прокси для секций без fakeip)

  LuCI улучшения
  - Динамические readonly условия: Auto-load Sections разблокируется при включении Opera/AWG; Auto-load Zapret2 — при включении Zapret2
  - Валидация URL подписок теперь принимает формат без path (https://host?param=value)
  - Серверные данные не перезаписывают пользовательские поля

  Прочие исправления
  - DNS проверки поддерживают dns_strategy=ipv6_only (AAAA записи)

  Изменения в листах
  - IP merge до /24 и /40
  - googleapi.com вынесен в cdn_google
  - Исправлено ошибочное попадание fakeip в листы, из-за чего ломался правильный роутинг(в sing-box попадали домены, которых не было в списках)
#ZeroBlock

---

**2026-02-24T01:58:53 | Kinaman**
Здравствуйте. Приобрёл роутер, установил скрипт №5, в службах появились Podkop и Zapret. По умолчанию всё работает, и youtube и discord, но судя по типу подключения - через vpn (см. скриншот). А на моём провайдере youtube и discord нормально работали через один из bat-файлов утилиты zapret-youtube-discord, которую я использовал на ПК до приобретения роутера - без vpn. Можно ли настроить службу zapret в роутере таким образом, чтобы youtube и discord работали без vpn как и раньше, а все остальные ресурсы уже через podkop?

---

**2026-02-24T02:02:37 | Routerich**
Можете, в секции на скрине убрать списки ютуб и дискорд и далее в разделе Службы - Zapret включить автозапуск и запустить запрет - подбирать стратегии для работы ютуба и дискорда и плюс добавить домены дискорда в список. Но я вам советую оставить список дискорд в подкопе а для запрета воспользоваться https://t.me/routerich/3845/420612

---

**2026-02-24T06:35:49 | Камиль**
Анализ запущен: 2026-02-24 06:27:20
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.4):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.4.149 | YouTube IP:  74.125.131.93
  Программы в автозапуске: zeroblock zapret2

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:    127.0.0.1
    Address:  127.0.0.1:53
    Name:  youtube.com
    Address: 74.125.131.190
    Name:  youtube.com
    Address: 74.125.131.136
    Name:  youtube.com
    Address: 74.125.131.91
    Name:  youtube.com
    Address: 74.125.131.93
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock             ai (prx url): ai,block,geoblock
  zeroblock           main (prx url): anime,art,music,news,repo,shop,tools,torrent,cdn_akamai,cdn_aws,cdn_azure,cdn_cdn77,!_cdn_cloudflare,cdn_digitalocean,cdn_fastly,cdn_github,cdn_gcore,cdn_ovh,cdn_vultr,cdn_bunny,cdn_hetzner,cdn_linode,cdn_oracle,cdn_scaleway
  zeroblock             ru (prx url): googleplay,messengers
  zeroblock        socials (prx url): meta,socials
  Полностью маршрутизированные IP-адреса включены!
  zeroblock.ru.fully_routed_ips='192.168.1.200'
  Версия zeroblock: 0.6.4-r64
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.32 | RAM: 25% | NAND: 44% занято / 38.1M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 * * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

Похоже где то дубли есть, посмотреть бы списки по cdn по отдельности

---

**2026-02-24T09:12:21 | Daniil**
Добрый день.Приобрел данный роутер по предзаказу.Приехал быстро в Санкт Петербург.Накатил zeroblock+zapret2.Youtube закрутился(даже на телеке), SoundCloud и Mixcloud заиграли.Продолжаю изучать устройство и мануалы.Спасибо за отличный продукт.Низкий поклон поддержке.

---

**2026-02-24T10:39:24 | Камиль**
Перешел на v1(опять), discord через zapret2 снова поехал

---

**2026-02-24T12:12:45 | Kiss_My_Axe**
Стратегия по умолчанию в запрет1, включённая в скрипт №5 немножко уже несколько месяцев не рабочая.
Запрет2 - норм, типа, однако не у всех взлетает с комплектными стратами.
А блок автообновления страт для Z2 в ЗероБлок пока не работает.
То есть либо самому, либо что-то иное юзать.
Я пока остановился на Запрет1 от remittor.
github remittor zapret в гугол и потом у него описание почитать. В инструкции по установке есть "быстрая установка", одну строку в терминал роутера воткнуть.
Ну как-то так.

---

**2026-02-24T13:30:58 | Роман**
Для запрет2 искать самому, для первого можно установить от ztressozz (предварительно удалить запрет1) - у него несколько стратегий уже есть.
https://github.com/StressOzz/Zapret-Manager

---

**2026-02-24T13:45:06 | Marseille Geertje**
https://dtf.ru/id65155/4570569-ustanovka-zapret2-na-openwrt-s-luci

---

**2026-02-24T13:49:47 | Tempt Me**
в вебе в пакетах сделай поиск по zapret2

---

**2026-02-24T14:42:54 | Иван**
Как продиагнострировать проблему, с ПК не грузится ютуб, на телефоне и ТВ хорошо работает, DNS в CHROME выключен, VPN на ПК нет, в другом браузере тоже не открывается ютуб
сижу через ZAPRET2 по ZeroBlock
Дискорд работает, ютуб нет

---

**2026-02-24T16:18:36 | Nook Scheel**
Зная хоть чуть чут как устроен openwrt прочитав 2 инструкции на github zapret2 и на zeroblock все встает даж на чистый openwrt

---

**2026-02-24T18:22:24 | Raux**
В итоге, я применил ту команду, которую месяц назад у вас и нашел в этой ветке. В моем случае, все заработало, в одном из конфигов. Летает в 4к. Еще раз спасибо.

sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-02-24T18:41:27 | GT_6**
Всем доброго вечера. Подскажите не опытному. Стоит zeroblock все работает как часы. Youtube работает через zapret. Но у меня проблема с Ubisoft коннектом,через раз коннектится к игре. Собрать лобби с друзьями не получается. Приходится использовать КВН. Поиском искал и не нашел где можно взять стратегии. Пытался скачать прогу warp но она не коннектится

---

**2026-02-24T18:58:18 | Routerich**
Здравствуйте.
подбирать стратегии к zapret на которой везде будет работать.

---

**2026-02-24T19:05:22 | KaPally3**
Можно чуточку подробнее?
На просторах канала нашел еще вот этот скрипт: 
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)
upd: Скрипт, скинутый @Az098yosflasd7tow4(Kiss_My_Axe) в одну из веток, помог. Спасибо)

---

**2026-02-24T19:28:29 | Routerich**
У вас старый zapret, его надо обновить чтобы появилось либо пользуйтесь zapret2, там уже есть сканер стратегий в веб интерфейсе

---

**2026-02-24T19:43:47 | Artem Mayorov**
в Zapret2 разбираюсь со сканером стратегий. Запустил. Сканируеет чего то там. ищет.))

---

**2026-02-24T19:57:19 | GT_6**
Zapret2

---

**2026-02-24T20:00:58 | Роман**
Для игр, из того что я знаю на роутер, есть этот запрет 

https://github.com/StressOzz/Zapret-Manager

---

**2026-02-24T20:21:24 | lxstwxrden**
Всем добрый вечер. Хочу узнать, откуда можно заранее скачать пакеты с zapret1 и zapret2? Т.к роутер забрал и буду устанавливать его только завтра, чтобы сразу поставить без танцев с интернетом

---

**2026-02-24T21:03:00 | Михаил**
У себя решил просто. На первом рабочем роутере zapret2 (youtube) и podkop. Далее роутер для экспериментов 2 со zeroblock, в секции AmneziaWG (awg) тоже  youtube. У кого zapret2 на основном роутере не аллё( samsung, lg и айфон), идут на wifi второго роутера. :)

---

**2026-02-24T21:43:24 | Gomer Simpson**
Если уже надоело - пробуйте АВТОКОНФИГУРАТОР для zapret (поиск в этой теме), или автоподбор стратегий для ютубанблока - это в WIKI.

---

**2026-02-24T22:22:01 | Александр**
Такая sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-02-24T23:44:25 | Виктор ZEUS**
Подскажите , а где скачать и установить этот zapret2 и чем он лучше чем zapret обычный

---

**2026-02-24T23:49:54 | Роман**
Система, пакеты, обновить списки, фильтр zapret2, установить два пакета.

---

**2026-02-25T01:04:50 | Den**
Анализ запущен: 2026-02-25 01:01:22
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
  Facebook IP:  57.144.110.1 | YouTube IP:  142.250.130.190

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.70 MB / ↑0.22 MB
  Пинг (ya.ru via awg10): 69.536 / 70.117 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock zapret2

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock              awg10 (vpn): news,porn,video
  zeroblock          opera (prx out): ai,block,geoblock
  Версия zeroblock: 0.6.4-r64
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.22 | RAM: 23% | NAND: 53% занято / 31.8M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-02-25T07:24:56 | Yury Kuzmenko**
Так это уже есть называется zapret2

---

**2026-02-25T07:37:18 | Sir**
Добрый день!
Кто то может помочь с discord?
Дискорд запускается, голос мой не слышат.
Скрипт new с Podkop и переустановленным Zapret2

---

**2026-02-25T09:46:03 | ProstoDjonni**
У меня двойной нат- zapret работает

---

**2026-02-25T10:15:39 | Алексей Новиков**
Только Zapret

С ним до этого работал твич

---

**2026-02-25T11:11:23 | Bkmz**
Подскажите пожалуйста, а почему Zapret2 не отображается в службах?. Сейчас ваш диалог выше дочитал и вроде все шло отлично, но вот Zapret2 вообще отказывается отображаться где либо (списки обновил-установил- в установленных отображается)

---

**2026-02-25T14:00:22 | Bkmz**
= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  57.144.222.1 | YouTube IP:  64.233.164.91

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓0.02 MB / ↑0.02 MB
  Пинг (ya.ru via awg10): 177.159 / 200.768 ms (2 из 10 потеряно)
  Программы в автозапуске: zeroblock

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock              awg10 (vpn): anime,discord,games,messengers,meta,news,porn,socials,youtube
  Версия zeroblock: 0.6.4-r64
  zeroblock DNS/Bootstrap DNS: (doh) 1.1.1.1 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.04 | RAM: 22% | NAND: 24% занято / 51.3M доступно
  # ZeroBlock Bad Interface Monitor
  */10 * * * * /usr/bin/zeroblock bad_interface_check >/dev/null 2>&1
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-02-25T14:43:43 | AleXXXey**
WhatsApp можно загнать в zapret2? Или эт долгая песня?

---

**2026-02-25T15:52:00 | Aleksei**
Ребята, а подскажите, пожалуйста, для новеньких.

Скрипт №5 или ZeroBlock?
Что лучше? ZeroBlock не заменяет zapret? Их можно использовать вместе?

---

**2026-02-25T18:21:26 | Kiss_My_Axe**
Интересовались? Распишитесь в получении!
# СТРАТЕГИИ В ZAPRET1
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)

---

**2026-02-25T18:25:39 | Вячеслав Шевченко**
как я понял я делаю всё по пунктам
1. арендую сервер для установки в нем своего личного VPN
2. закидываю свой впн в роутрич.
3. там в нем настраиваю или подкоп или зероблок. (для того что бы мой впн стал умным и работал только на запрещенных сайтах рф. а остальные сайты,не заблоченные, работали без впн)
4. по поводу zapret2  не знаю делать или нет (пусть тут подскажут ребята)
ну и готово

---

**2026-02-25T18:40:53 | Александр**
Наподобие этого АВТОКОНФИГУРАТОР ZAPRET

---

**2026-02-25T18:57:58 | Алексей Мазок**
подскажите, на OpenWrt 23.05.5 r24106-10cc5fcd00 / LuCI c344ad02a0 branch git-24.284.60835-e6cb537 можно поставить zapret2 или посоветуете чего для телеги\дискорда?
ВГ есть и пока работает, может как-то можно на него пускать трафик по pbr?

---

**2026-02-25T20:35:59 | Bullet for my valentine Poison**
Его нет, есть только священное писание https://github.com/bol-van/zapret2/blob/master/docs/manual.md#введение

---

**2026-02-25T21:23:32 | Routerich**
Здравствуйте
Zapret это средство для обхода тспу, то есть это средство для модернизации пакетов, то есть интернет будет работать на скорости провайдера.

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

**2026-02-26T01:12:05 | Роман**
Через система пакеты обновить списки фильтр zapret2, установить 2 пакета, убрать Ютуб из подкопа zeroblock.

---

**2026-02-26T07:39:10 | KawaiiKiller**
Zapret Какая версия лучше

---

**2026-02-26T07:39:42 | Routerich**
Здравствуйте.
zapret2

---

**2026-02-26T09:22:34 | Lelik**
Вот еще кому может понадобится - полезная картинка. Это только для zapret1

---

**2026-02-26T10:35:21 | Вячеслав Шевченко**
Подскажите пожалуйста я сейчас ссылку оставлю на гитхаб. это и есть тот самый запрет2 который мы используем в роутриче только для пк ? https://github.com/youtubediscord/zapret/releases?page=1

---

**2026-02-26T10:37:50 | Вячеслав Шевченко**
https://github.com/flowseal/zapret-discord-youtube/releases этот для меня самый первый.

---

**2026-02-26T12:20:43 | Vladislav**
Подскажите что лучше Zapret2 или Podkop? Не очень понимаю чем они отличаются

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

**2026-02-26T13:07:28 | XaleX**
Блокчек обязательно устанавливать для работы zapret?

---

**2026-02-26T14:42:18 | Routerich**
поднять awg10 на классическом wireguard, использовать zapret2 для обфускации

---

**2026-02-26T17:30:43 | Wenzel Perminov**
тут у меня опять youtube через zapret2 отвалился, но на Андройде где стоит ByeDPI одна стратегия долго живет. Я подумал может можно в качестве альтернативы запрету добавить, пакеты скомпилированные под openwrt есть на github, сам ByeDPI маршрутезировать не умеет, но создает прокси через которую может zeroblock маршрутизировать.

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

**2026-02-26T17:50:20 | konnlori**
Так, стопэ. Я нажал поставить zapret2, у меня оно поставилось в пакетах, а в менюшке нет :/ Как понимать. Страницу с кэшем перезагружал

---

**2026-02-26T18:06:25 | konnlori**
Ладно, всё-таки придётся самому скрипт писать с zapret-discord-youtube, просто думал уже есть готовое решение) Но если бы разаботчики ZeroBlock такое добавили я бы не отказался

---

**2026-02-26T18:15:41 | MP**
Здравствуйте!!!!
Если пакеты обновлю, сейчас zapret 72.20251022 и podkop 0.7.7, настройки останутся прежними ?

---

**2026-02-26T21:17:39 | Bullet for my valentine Poison**
Через пакеты в роутере. Обновить список, а потом в фильтре вписать Zapret2.

---

**2026-02-26T21:18:23 | Anna Bagler**
Система - Пакеты, кнопочка Обновить списки. Потом в поле фильтра zapret2 и ok. И установить.

---

**2026-02-26T22:51:09 | Pavel**
Кто-нибудь пробовал вот эту прогу, как альтернатива zapret?

---

**2026-02-27T08:31:55 | John Deere**
Добрый день! Стоит zapret2 и zeroblock, после обновы до zeroblock с API v2 YouTube перестал работать на некоторых устройствах. YouTube unblock в автозагрузке отключен, в списке только запрета не зироблока, cidr вкл/выкл разницы нет. Попробовать убрать ют с запрета и выбрать его в зироблоке или есть другие решения?

---

**2026-02-27T10:47:31 | Kiss_My_Axe**
Щикааарно!
root@roskomnadzor:~# nft list tables
table inet fw4
table inet zapret
table inet zeroblock
root@roskomnadzor:~# nft list tables
table inet fw4
table inet zapret
root@roskomnadzor:~#

---

**2026-02-27T15:10:20 | konnlori**
Раз уж вы тут заговорили про IP. Вчера накалякал скрипт для обновления IP диапазонов с этого репозитория. Может кому полезно будет

Я засунул на авто-обнову его в полночь
0 0 * * * /bin/sh /opt/zapret2/ipset/get_cdn_ip_ranges.sh > /dev/null 2>&1

---

**2026-02-27T16:17:45 | Lion**
Всем привет!

Подскажите, что сейчас стоит использовать для обхода блокировок на openwrt роутере?
Год назад был только zapret, а сейчас всякие подкопы и прочее появились)

---

**2026-02-27T16:19:23 | Anna Bagler**
На РР популярна связка zeroblock и zapret2.

---

**2026-02-27T16:20:17 | Lelik**
Ну аналог на Zapret2ском как будет, не могу понять
--dpi-desync-fake-tls-mod=sni=www.google.com
По ману SNI нигде не фигурирует вроде, скорее всего не напрямую как-то указано

---

**2026-02-27T16:28:06 | Lelik**
LUA ERROR: /opt/zapret2/lua/zapret-antidpi.lua:444: fake: 'blob' arg required
desync ERROR. passing packet unmodified.
LUA ERROR: /opt/zapret2/lua/zapret-antidpi.lua:444: fake: 'blob' arg required
desync ERROR. passing packet unmodified.
LUA ERROR: /opt/zapret2/lua/zapret-antidpi.lua:444: fake: 'blob' arg required
desync ERROR. passing packet unmodified.
LUA ERROR: /opt/zapret2/lua/zapret-antidpi.lua:444: fake: 'blob' arg required
desync ERROR. passing packet unmodified.
Блокчек и затребовал, так бы вот всегда

---

**2026-02-27T16:36:45 | Lelik**
--lua-desync=fake:blob=/opt/zapret2/files/fake/tls_clienthello_t2_ru.bin:tls_mod=rnd,dupsid,sni=m.ok.ru
Типо такого

---

**2026-02-27T17:16:40 | Антон**
Zapret1

---

**2026-02-27T19:57:28 | Dmitry Tretiakov**
Небольшая история в тему работы приложения ютуба на android TV приставке (может кому полезно будет).

Обновил роутер на последнюю прошивку, сбросил, поставил zapret2, подкоп. Ютуб приложение на android TV не заработало, сайт через браузер работает. На всех других устройствах всё ОК. Столько всего перепробовал, что не дай бог, уже подумал что всё кончено. Приложение показывало, что нет подключения к интернету. Конечно же я пытался удалять запрет ручками, ставить снова, проверял конфиги.

Сделал tcpdump с роутера в момент открытия приложения ютуба, проанализировал все стратегии запрета и таблицы маршрутизации для youtube. Оказалось что параллельно с zapret2 продолжал работать youtubeUnblock и маркировал пакеты из приложения по-своему, обходя запрет. (@RouterichSupport  возможно стоит добавить похожую проверку в диагностику? что нет конфликтов сервисов).

Приложение использует другие правила общения с серверами ютуба и проходит несколько хэндшейков перед показом контента. Часть хендшейков ломалась неправильной маркировкой.

В итоге вручную отключив youtubeunblock и удалив правила маркировки, всё чудесным образом завелось)

Итог и пара рекомендаций: Проверяйте что действительно отключён youtubeunblock после установке запрета и нет оставшихся правил маркировки (можно погуглить как это делается через терминал). На ТВ обязательно в настройках должен сети должен быть прописан днс роутера.

---

**2026-02-27T20:36:02 | Dmitry Tretiakov**
И имеет приоритет над правилами zapret2 (до тех пор пока youtubeunblock и его демоны живы)

---

**2026-02-27T20:40:00 | Dmitry Tretiakov**
Да, zapret2 и youtubeunblock оба пытались использовать очередь одну и ту же в момент обработки трафика. юаб брал верх всегда

---

**2026-02-27T21:49:25 | Роман**
https://github.com/StressOzz/Zapret-Manager
Это через терминал, там подбирайте стратегии.

---

**2026-02-27T21:52:39 | Routerich**
попробуйте отключить zapret и singbox

---

**2026-02-28T07:19:37 | Михаил**
Не. Все по дефолту, домены только youtube. Версия крайняя - 1.3  вроде. Я, честно говоря, даже разбираться не стал, youtubeblock в стоп, zapret2 в перезапуск. И все отлично.
Но осадочек то остался...

---

**2026-02-28T11:17:48 | DG**
zapret не установлен

---

**2026-02-28T12:52:51 | Михаил**
А zapret2 не пробовали? И дешевле и, скорее всего, эффективнее. Я про youtube.

---

**2026-02-28T12:55:00 | Marseille Geertje**
Пробовал. У меня два роутера. Один со скриптом 5, второй с zeroblock и zapret2. И то и то работает плохо в части скорости ютуба. А на втором ещё и rutracker не работает без браузерного плагина. 🤷🏻‍♂️

---

**2026-02-28T12:56:59 | Роман**
Первый запрет тоже хорошо до сих пор работает и для Ютуба, и для дискорда. 
https://github.com/StressOzz/Zapret-Manager
Вот например, пробовали?

---

**2026-02-28T13:02:19 | Marseille Geertje**
Я пробовал на сброшенный до заводских настроек ставить только youtubeUnblock и вот в этом случае скорость ютуба меня устраивает. 😁 (пробовал даже после скрипта 5 отключать в вебке podkop и  zapret при одновременном включении youtubeUnblock и тогда ютуб тоже работает приемлемо для меня)
Но загвоздка в том, что остальная запрещёнка тогда либо не работает, либо я не понял что-то. 😁

---

**2026-02-28T13:08:32 | Marseille Geertje**
Спасибо. Сейчас попробую.
А правильно ли я понимаю, что связка ZeroBlock и Zapret2 удобнее в части ковыряний в настройках в которых я ничего не смыслю. 😄

---

**2026-02-28T13:09:07 | Marseille Geertje**
Удобнее связки Podkop и Zapret (скрипт 5)

---

**2026-02-28T13:35:57 | Михаил**
Из плюсов zapret2 перед первым - автоматический поиск стратегий. Непосредственно встроенный в запрет2.

---

**2026-02-28T13:50:59 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.6.4-r94:
  Исправления:
  - Убран domain_resolver с proxy outbound — устранена циклическая DNS зависимость(url прокси теперь умеет в доменные имена серверов)
  - force_disable_fakeip=0 теперь корректно сбрасывает disable_fakeip(управление disable fakeip c сервера)
  - Сброс флагов auto_config после установки пакетов(при установке на уже существующий конфиг каскад из opkg установок ломал luci(unexpected json что-то там))
  - Исправлен backup/restore noresolv в failsafe-proxy ветке dns_manager(noresolv теперь управляется zeroblock)
  - Асинхронный запуск и проверка zapret2 при автоустановке(больше не блокирует запуск основного процесса)

  Новое:
  - Health-check AWG/Opera/TrustTunnel при запуске — автоматическая проверка и восстановление интерфейсов, если они существуют
  - Автообновление TrustTunnel при запуске (сравнение локальной и удалённой версий через GitHub API)
  - Убрана кнопка "Update TrustTunnel" из LuCI — обновление теперь полностью автоматическое
  - Отображение версии TrustTunnel в диагностике
  - Автоустановка zapret2 теперь только устанавливает пакет, остальной работой занимается мониторинг
  - При автостратегиях на api=v2 теперь zapret2 получает стратегию rr_blackhole, которая позволяет работать скриптам без основного zapret2

  Работа со списками:
  - Дополнен список ipv4/ipv6 для discord voice
#ZeroBlock

---

**2026-02-28T14:31:02 | Maxim Mrakov**
Всем привет, подскажите, есть какой-то универсальный конфиг для Zapret   v72.20251122 что бы конектило к игровым серверам которые могут быть в блокировке?

---

**2026-02-28T14:44:04 | AlexChus**
А что на роутере используется? Zb, pdkop, zapret ? Я в ВА ничего не прописывал.

---

**2026-02-28T16:00:43 | Роман**
Подбор стратегии для Zapret1 от ув.Kiss_My_Axe

sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)
В терминал и перебирать стратегии.

---

**2026-02-28T17:59:36 | Anna Bagler**
Если помогает обычный перезапуск, добавьте задачу на restart zapret2 в планировщик и понаблюдайте.

---

**2026-02-28T18:00:24 | Ivan**
Zapret2 устанавливал месяц назад.

---

**2026-02-28T18:03:54 | Anna Bagler**
0 4 * * * service zapret2 restart - попробуйте так.

---

**2026-02-28T22:46:05 | Роман**
Если ютуб не будет работать - отключить youtubeunblock, включить запрет - подобрать стратегию для него скриптом - 
Подбор стратегии для Zapret1 от ув.Kiss_My_Axe

sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)

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

**2026-02-28T23:11:01 | Роман**
sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh) 
ЮАБ отключить.
Это в терминал - скришот сюда.

---

**2026-03-01T10:44:55 | Роман**
Подбор стратегии для Zapret1 от ув. Kiss_My_Axe - требует установленного запрета.

sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)


Целый комбайн для запрета от ztressozz - сам установит, обновит, настроит, но можно и руками поиграться.

sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh)

---

**2026-03-01T10:45:51 | Артем**
а запрет так и должен быть выключен?
и ещё вопрос: чтобы discord и youtube работали через zapret, а все остальные заблокированные ресурсы из списка работали через прописанный мною vless, мне что нужно сделать?

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

**2026-03-01T12:39:33 | Zeal Tree**
Полный вывод такой, но думаю главное вот что 
⚠️ Zapret detected
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🥸 FakeIP status
❌ Failed to get FakeIP info
✅ Sing-box works with FakeIP: 198.18.0.7

---

**2026-03-01T13:51:40 | Вячеслав Шевченко**
Здравствуйте. с чего начать? я вот вот подключил роутер к сети. интернет есть. хочу попробовать поставить zapret2 как его поставить? может роутер обновить сначала? и что означает кнопка "обновляется" вверху справа?

---

**2026-03-01T16:55:21 | Zeal Tree**
У меня такое было, помог zapret manager, там перебирал стратегии youtube пока не стал работать на lg youtube.

---

**2026-03-01T17:25:25 | Anna Bagler**
Ах, да, он же в запрете у вас.
 @EsoNua user hostname должен быть не пустым, если перетягивает что-то на себя, но как в zapret2 точно, не подскажу.

---

**2026-03-01T19:22:35 | Роман**
В канал упирается, zeroblock и zapret2.

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

**2026-03-01T21:08:21 | Routerich**
Если вы zapret используете то это норм

---

**2026-03-01T21:50:39 | lxstwxrden**
Всем привет. Есть в zapret2 возможность включить ICMP трассировку обратно? Просто в zapret1 есть такое, а в zapret2 такой функции из под люси я не нашёл, а надо сделать трассировку по UDP протоколу до сервака, а из-за этой функции - сделать это невозможно

---

**2026-03-01T22:10:32 | Леонид**
А есть ли какая готовая актуальная прошивка, с предустановленным ZB + filsafe proxy и без всякого хлама, потипу yt unblock, zapret и т.п.?

---

**2026-03-01T22:16:53 | Vladimir Rychenkov**
надо разделить на 2 этапа: поставить его можно из Microsoft Store без всяких обходов, а вот зайти - это уже через zapret. домены и айпи

---

**2026-03-01T22:51:45 | Михаил**
Zapret на отдыхе, youtubeunblock вооюще отсутствует

---

**2026-03-01T23:14:14 | Михаил**
Еще до кучи. Второй zapret только на youtube на первом роутере. Этот второй, для экспериментов. Схема паровозиком с натами.

---

**2026-03-01T23:28:09 | Роман**
Если для ютуба - ставтье через пакеты zapret 2, ютуб убрать из подкопа, запрет 1 остановить, остановить автозапуск.

---

**2026-03-02T01:35:46 | Святос**
Решил попробовать сразу в nfqws2 опции конфиг вписать, над которым страдали у бол-вана. И получил полную неработоспособность:
--blob=tls_4pda:@/opt/zapret2/files/fake/4pda.bin
--blob=quic_google:@/opt/zapret2/files/fake/quic_initial_www_google_com.bin
--blob=tls_google:@/opt/zapret2/files/fake/tls_clienthello_www_google_com.bin
--blob=fake_stun:@/opt/zapret2/files/fake/stun.bin
--blob=tls_max:@/opt/zapret2/files/fake/max.bin

--filter-udp=19294-19344,50000-50100
--filter-l7=discord,stun,quic
--payload=quic_initial,discord_ip_discovery,stun
--lua-desync=fake:blob=quic_google:repeats=6
--lua-desync=multisplit:repeats=6
--new

--filter-tcp=2053,2083,2087,2096,8443
--filter-l7=http,tls
--hostlist-domains=discord.media
--payload=tls_client_hello,http_req
--lua-desync=fake:blob=tls_google:tcp_ts=-10000:tcp_seq=400:repeats=8
--lua-desync=multisplit:ip_id=zero:repeats=8
--new

--filter-tcp=443
--filter-l7=http,tls
--hostlist=/opt/zapret2/ipset/zapret-hosts-google.txt
--payload=tls_client_hello,http_req
--lua-desync=fake:ip_id=zero:blob=tls_google:tcp_ts=-10000:tcp_seq=400:repeats=6
--lua-desync=multisplit:ip_id=zero:repeats=6
--new

--filter-tcp=443
--filter-l7=tls
--hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt
--hostlist-exclude=/opt/zapret2/ipset/zapret-hosts-user-exclude.txt
--ipset-exclude=/opt/zapret2/ipset/zapret-ip-exclude.txt
--payload=tls_client_hello
--lua-desync=fake:blob=tls_4pda:tcp_ts=-10000:repeats=6
--new

--filter-tcp=80
--filter-l7=http
--hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt
--hostlist-exclude=/opt/zapret2/ipset/zapret-hosts-user-exclude.txt
--ipset-exclude=/opt/zapret2/ipset/zapret-ip-exclude.txt
--payload=http_req
--lua-desync=fake:blob=tls_max:tcp_ts=-10000:repeats=6
--new

--filter-udp=50000-50100
--filter-l7=mtproto
--payload=mtproto_initial
--lua-desync=fake:blob=quic_google:repeats=6:tcp_ts=-10000
--new

--filter-udp=443
--filter-l7=quic
--hostlist=/opt/zapret2/ipset/zapret-hosts-google.txt
--payload=quic_initial
--lua-desync=fake:blob=quic_google:repeats=8
--new

--filter-udp=443
--filter-l7=quic
--hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt
--hostlist-exclude=/opt/zapret2/ipset/zapret-hosts-user-exclude.txt
--ipset-exclude=/opt/zapret2/ipset/zapret-ip-exclude.txt
--payload=quic_initial
--lua-desync=fake:blob=quic_google:repeats=6
--new

--filter-tcp=80,443,1024-65535
--ipset=/opt/zapret2/ipset/zapret-ip-user.txt
--hostlist-exclude=/opt/zapret2/ipset/zapret-hosts-user-exclude.txt
--ipset-exclude=/opt/zapret2/ipset/zapret-ip-exclude.txt
--payload=tls_client_hello
--lua-desync=fake:blob=tls_4pda:repeats=6:tls_mod=rnd,sni=www.google.com:tcp_ts=-10000
--new

--filter-udp=1024-19293,19345-49999,50101-65535
--ipset=/opt/zapret2/ipset/zapret-ip-user.txt
--ipset-exclude=/opt/zapret2/ipset/zapret-ip-exclude.txt
--payload=unknown
--out-range=-d2
--lua-desync=fake:blob=quic_google:repeats=12

---

**2026-03-02T05:50:03 | Routerich**
Здравствуйте.
Это длительны процесс, и этот процесс отдаётся на пользователя, так как в скрипт выстраивать blockcheck нет необходимости.
Вы всегда лжете руками запустить после скрипта поиск стратегий и установку её в zapret.

---

**2026-03-02T10:13:13 | Sag**
То есть Вам не понравился? Странно а то на форумах наоборот пишут якобы проще и лучше чем zapret , Вот только памяти вроде больше отжирает.
Попробую если что снести не долго

---

**2026-03-02T10:15:27 | Роман**
Совершенно верно, не понравился. Связка zeroblock и zapret2 с автохостлистом полностью покрывает мои нужды.

---

**2026-03-02T12:04:46 | TomatHunter 🍅💀**
Добрый день. Лог установки беты (zapret не поставился, скрипт поставил podkop)

---

**2026-03-02T12:41:35 | Bullet for my valentine Poison**
Итак пошаговый мануал для владельцев Routerich, как завести Zeroblock+Zapret2 на дефолтных настройках.
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки"и ждем, закрываем появившуюся табличку нажав на кнопку "ОК".
3. Качаем два файла (zeroblock_*** и luci-app-***) из закрепа темы "Zeroblock" и сохраняем в папку на рабочем столе.
4. Возвращаемся в разделы Система-пакеты и жмем на кнопку "Загрузить пакет". И по очереди ставим скачанные пакеты: Zeroblock_*** а затем luci-app***.(Табличку с надписью Error игнорируем)
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4,6,7. Жмем по очереди на кнопки: сохранить и применить.(Если вдруг 6 и 7 пункт не активны, проверьте в разделе настройки пункт "Версия API", должна стоять V2)
7. Далее ждем примерно 5 минут, очищаем кэш браузера и обновляем страницу. Пока в разделе Службы не появится пункт "Zapret2".
8. Возвращаемся в Zeroblock, открываем вкладку Автонастройка и убираем галки с 6 и 7 пункта.(Автозагрузка) Иначе мы не сможем вносить изменения в секциях со списками. Сохранить, применить.
9. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
10. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
11. Проверяете работу Youtube на всех устройствах. (так же желательно в браузерах отключить функцию "Частный/безопасный DNS")
Ссылка на пакеты для скачки: https://t.me/routerich/394153/432061?single

---

**2026-03-02T13:23:54 | Bullet for my valentine Poison**
Возможно подгрузка, у вас ютуб идет через dpi-дурилку. Можно для теста зайти в Zapret2 и нажать перезапустить. Вчера просто двух человек перевел на такой же конфиг Зеро+запрет2 (ютуб + дискорд) - жалоб нет.

---

**2026-03-02T14:01:59 | Vitaly Krasnyuk**
Установил скрипт №5. Появился zapret, он включен. На всякий перезагрузил роутер. По прежнему работает только ютуб на телефонах и ноуте. Другие - FB, Insta, chatgpt без впн не открываются.

---

**2026-03-02T17:28:17 | Routerich**
В секции с названием дискорд убрать список ютуб  и далее в разделе Службы - Zapret включить автозапуск и запустить запрет - подбирать стратеги для запрета воспользоваться https://t.me/routerich/3845/420612

---

**2026-03-02T19:24:10 | Routerich**
Здравствуйте.
Стратегию подбирать zapret2
https://t.me/routerich/80283/407345

---

**2026-03-02T20:23:41 | ㅤㅤ**
Добрый вечер. Как бы решали вопрос по обходу на iPhone по логике Zapret2|Podkop|ZeroBlock и т.п.

Наткнулся на китайский Quantumult X. Целый день возился с их китайскими конфигами. Штука интересная, но непростая в работе. Конфиг сильно ограничен в синтаксисе. AmneziaWG не поддерживает. Зато работает с VLESS (Reality пока не поддерживает).

Быть может я просто закопался и стоит пойти по более простым путям? Каким образом наладить работу по обходу DPI в достаточно закрытой и ограниченной оси. В этом дилемма.

---

**2026-03-02T20:44:43 | Vitaly Krasnyuk**
Да, схема подключения такая. Как только отключил zapret, браузеры включились)

---

**2026-03-02T21:13:21 | Bullet for my valentine Poison**
Итак пошаговый мануал для владельцев Routerich, как завести Zeroblock+Zapret2 на дефолтных настройках.
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки"и ждем, закрываем появившуюся табличку нажав на кнопку "ОК".
3. Качаем два файла (zeroblock_*** и luci-app-***) из закрепа темы "Zeroblock" и сохраняем в папку на рабочем столе.
4. Возвращаемся в разделы Система-пакеты и жмем на кнопку "Загрузить пакет". И по очереди ставим скачанные пакеты: Zeroblock_*** а затем luci-app***.(Табличку с надписью Error игнорируем)
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4,6,7. Жмем по очереди на кнопки: сохранить и применить.(Если вдруг 6 и 7 пункт не активны, проверьте в разделе настройки пункт "Версия API", должна стоять V2)
7. Далее ждем примерно 5 минут, очищаем кэш браузера и обновляем страницу. Пока в разделе Службы не появится пункт "Zapret2".
8. Возвращаемся в Zeroblock, открываем вкладку Автонастройка и убираем галки с 6 и 7 пункта.(Автозагрузка) Иначе мы не сможем вносить изменения в секциях со списками. Сохранить, применить.
9. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
10. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
11. Проверяете работу Youtube на всех устройствах. (так же желательно в браузерах отключить функцию "Частный/безопасный DNS")

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

**2026-03-02T23:34:11 | Борис**
Я себе на роутере сделал vless reality сервер. Это бесплатно и помогает обходить белые списки с телефона. Работает это так, что роутер выступает в роли сервера, телефон в роли клиента. Клиент подключается к серверу по протоколу vless с примочками для reality (дополнительные атрибуты в отправляемых пакетах). Из-за того, что клиент сообщает, что идёт на m.vk.com (это неправда), провайдер пускает его трафик до моего роутера, думая, что это сайт ВКонтакте. На деле же роутер выступает выходной нодой для интернета (на роутере в свою очередь установлены zapret2 и zeroblock, позволяющие открывать ютуб, chatgpt и прочие плохие вещи)

---

**2026-03-03T00:40:30 | Anna Bagler**
Присваивайте IP телевизору на роутере, чтоб не менялся, идите в подкоп, секция discord, полностью маршрутизированные IP-адреса и там вписывайте адрес ТВ. Если не поможет или будет не очень стабильно, то сброс настроек роутера и переход на zeroblock. Может и @BFMVPoison тогда поможет с zapret2 для LG.
Если ТВ старый, рассмотрите возможность покупки тв-бокса на андроиде к нему.

---

**2026-03-03T00:50:24 | Борис**
Каким образом? У провайдера стоит dpi и он должен знать, к какому сервису ты подключаешься. Если ты просто подключаешься к 5.12.133.213, то он не даст тебе это сделать, т.к. ты не обозначил свои намерения (не указал sni)

А в целом сейчас скорее по фейксни бан схлопочешь. Живой пример ютубанблок.

Тоже не понимаю, о чём речь. Если сервер настроен правильно, он будет устойчив к краулерам и методам активного зондирования. Технология reality устроена так, что если зайти на маскировочный ip с указанным sni (как попытается сделать провайдер), то сервер ответит реальным маскировочным сайтом с реальным сертификатом

Живой пример ютубанблок.

youTubeUnblock - это система для обхода dpi, и этот инструмент не имеет ничего общего с подменой sni. Системы обхода dpi (zapret, byeDpi, youTubeUnblock) работают таким образом, что изменяют структуру и/или атрибуты пакетов, делая их нечитаемыми для DPI провайдера. Провайдер, если работает не в системе белых списков, рассуждает так: "за интернет было уплачено, и я не могу доказать, что это запрещённый сайт, поэтому я разрешу такой запрос"

В системе белых списков провайдер рассуждает наоборот: "не удаётся подтвердить, что это разрешённый социальный ресурс, поэтому я заблокирую его"

---

**2026-03-03T00:52:45 | Anna Bagler**
Сброс настроек и zeroblock+zapret2, youtubeUnblock удалить.

---

**2026-03-03T01:26:35 | Anna Bagler**
Да, yt лучше в zapret2, если вам важно высокое разрешение. Дискорд тоже, но по желанию.

---

**2026-03-03T04:01:07 | Иван Серебряков**
Попробовал. Что-то не так с листами — ломает какой-то очень специфический айпишник/url, из-за которого не робит любимая игрушка семьи.
На скрипте5@Zapret всё робит норм

---

**2026-03-03T05:12:35 | De1Dev**
Другой мой старый роутер, на OpenWrt работает.
Этот я подруге заказал, хотел настроить ZeroBlock и Zapret и отдать ей.😅
Но даже не добрался в luci.🥲

---

**2026-03-03T09:25:41 | Brs**
Здравствуйте! Как можно настроить роутер так чтобы можно было обновить пакеты, чтобы работал доступ к гитхаб и остальным ресурсам?
Сижу с мобильного модема в hilink
При попытке обновить пакеты проходит некоторое время и как правило выдаёт ошибку что не удалось выполнить JSON и всё.
Крайне редко удаётся обновить пакеты и что-то скачать с репозитария.
Гитхаб работает странно, с мобильных устройств по WIFI удаётся зайти почти по всем ссылкам на гитхаб, а с ноута по WIFI в основном только  на главную страницу. Также с ноута иногда удаётся зайти на гугл.ком и на ещё ряд сайтов. В основном не удаётся.
По инструкции из ВИКИ ставил zapret1, удалось обновить пакеты и установить zapret2 и всё, больше пакеты не обновляются.
На данный момент у меня прошивка сток, zapret2 со стандартными настройками,  отключен youtubeunblock (из-за него у меня на смартфоне не работал ютуб, даже с byebyedpi не работал).
Рядом в рукак смартфон и его мобильный интернет и там таких ограничений нет. Там обычные ограничения роскомнадзора.
Цель настроить роутер так, чтобы можно было нормально пользоваться интернетом. Обновлять пакеты, ставить ZB, подбирать стратегии и обходить ограничения.
Сейчас же, роутер использует 10% своего потенциала.

---

**2026-03-03T09:27:42 | Brs**
ZB поставить не могу, не удаётся выкачать недостающие пакеты.
В распоряжении только zapret2

---

**2026-03-03T11:47:08 | Усатый Бро**
Перебирал стратегии через  скрипт wget -O /tmp/Zapret-Manager.sh https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh && sh /tmp/Zapret-Manager.sh

ни одна не помогает всегда один итог.

---

**2026-03-03T11:54:29 | Denis**
Зачем при дефолтной установке zeroblock вместе с zapret2 в секции awg10 установлен youtube Community List? Awg же могут конфликтовать с zapret2 за дележ трафика youtube

---

**2026-03-03T11:59:53 | Denis**
не, я прочел там раздел Community Lists  и поискал  по слову zapret )
Сейчас еще раз почитаю

---

**2026-03-03T12:50:50 | Никита**
А можно в кратце отличия zero block, zapret2 и тд в чем разница, вчера установил 5 скрипт, пока все работает😁на будущее малолм сломается)

---

**2026-03-03T15:06:28 | Aleksandr**
Routerich поставил первым. Чтобы зарегаться в сети провайдера указал статический IP и прочие мелочи. Теперь ранее настроенные плюшки на ZB при 192.168.1.1 не работают. Нужно заново поставить ZB и Zapret2?

---

**2026-03-03T16:47:14 | Bullet for my valentine Poison**
Итак пошаговый мануал для владельцев Routerich, как завести Zeroblock+Zapret2 на дефолтных настройках.
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки"и ждем, закрываем появившуюся табличку нажав на кнопку "ОК".
3. Качаем два файла (zeroblock_*** и luci-app-***) из закрепа темы "Zeroblock" и сохраняем в папку на рабочем столе.
4. Возвращаемся в разделы Система-пакеты и жмем на кнопку "Загрузить пакет". И по очереди ставим скачанные пакеты: Zeroblock_*** а затем luci-app***.(Табличку с надписью Error игнорируем)
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4,6,7. Жмем по очереди на кнопки: сохранить и применить.(Если вдруг 6 и 7 пункт не активны, проверьте в разделе настройки пункт "Версия API", должна стоять V2)
7. Далее ждем примерно 5 минут, очищаем кэш браузера и обновляем страницу. Пока в разделе Службы не появится пункт "Zapret2".
8. Возвращаемся в Zeroblock, открываем вкладку Автонастройка и убираем галки с 6 и 7 пункта.(Автозагрузка) Иначе мы не сможем вносить изменения в секциях со списками. Сохранить, применить.
9. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
10. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
11. Проверяете работу Youtube на всех устройствах. (так же желательно в браузерах отключить функцию "Частный/безопасный DNS")

---

**2026-03-03T17:21:04 | Routerich**
Время на роутере проверить и синхронизировать, отключить zapret если есть, проверить без него

---

**2026-03-03T18:24:23 | Антон**
@ded_ikar вы не могли бы сделать стратегию для zapret2 roblox на вас вся надежда

---

**2026-03-03T18:31:13 | Routerich**
Искать домены игры и добавлять их в Zapret, а с Zeroblock убрать

---

**2026-03-03T18:49:59 | Bullet for my valentine Poison**
Итак пошаговый мануал для владельцев Routerich, как завести Zeroblock+Zapret2 на дефолтных настройках.
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки"и ждем, закрываем появившуюся табличку нажав на кнопку "ОК".
3. Качаем два файла (zeroblock_*** и luci-app-***) из закрепа темы "Zeroblock" и сохраняем в папку на рабочем столе.
4. Возвращаемся в разделы Система-пакеты и жмем на кнопку "Загрузить пакет". И по очереди ставим скачанные пакеты: Zeroblock_*** а затем luci-app***.(Табличку с надписью Error игнорируем)
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4,6,7. Жмем по очереди на кнопки: сохранить и применить.(Если вдруг 6 и 7 пункт не активны, проверьте в разделе настройки пункт "Версия API", должна стоять V2)
7. Далее ждем примерно 5 минут, очищаем кэш браузера и обновляем страницу. Пока в разделе Службы не появится пункт "Zapret2".
8. Возвращаемся в Zeroblock, открываем вкладку Автонастройка и убираем галки с 6 и 7 пункта.(Автозагрузка) Иначе мы не сможем вносить изменения в секциях со списками. Сохранить, применить.
9. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
10. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
11. Проверяете работу Youtube на всех устройствах. (так же желательно в браузерах отключить функцию "Частный/безопасный DNS")

---

**2026-03-03T18:56:59 | Aleksandr**
Купил роутер от Роутерич. Накатил ZB и Zapret2 и радуйся жизни!)

---

**2026-03-03T19:32:20 | Bullet for my valentine Poison**
При автостратегиях на api=v2 теперь zapret2 получает стратегию rr_blackhole, которая позволяет работать скриптам без основного zapret2
ааа, тогда да. Нужная вещь

---

**2026-03-03T22:35:33 | Mallory**
Спасибо за мануал, если честно его чтение подвигло снова пытаться разобраться с Zapret2. Не ради критики - а с точки зрения нуба - для меня Z2 и его блокчек - темный лес, а именно перенос найденных стратегий.

Скажу, что совершенно не понимал и сейчас начал хоть маленько понимать с помощью Gemini:

- секция начала
- нумерация стратегий
- параллельные команды в рамках стратегии

По сути - вопрос прост - если я подобрал стратегии с помощью Blockchek2 то как это это перенести в настройки? Удалять ли полностью дефолтную секцию, или оставить шапку (какую?). Если удалять - то что добавить к найденным строчкам чтобы оно завелось? Если не удалять дефолт, то как дописать найденные строчки.

Это я не к критике, а что новичку очень сложно разобраться. Если что-то подобное будет отражено на пальцах в мануале, это будет прекрасно.

---

**2026-03-03T22:38:24 | 𝓐𝓵𝓮𝓴𝓼𝓪𝓷𝓭𝓻**
установил zapret2 ,на компьютере плохо ютуб работает а на телевизоре вобще не работает

---

**2026-03-03T22:40:43 | 𝓐𝓵𝓮𝓴𝓼𝓪𝓷𝓭𝓻**
это в зероблоке или zapret2,где убрать?

---

**2026-03-03T23:02:37 | Bullet for my valentine Poison**
По мануалу. Кэш и прочее.
Итак пошаговый мануал для владельцев Routerich, как завести Zeroblock+Zapret2 на дефолтных настройках.
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки"и ждем, закрываем появившуюся табличку нажав на кнопку "ОК".
3. Качаем два файла (zeroblock_*** и luci-app-***) из закрепа темы "Zeroblock" и сохраняем в папку на рабочем столе.
4. Возвращаемся в разделы Система-пакеты и жмем на кнопку "Загрузить пакет". И по очереди ставим скачанные пакеты: Zeroblock_*** а затем luci-app***.(Табличку с надписью Error игнорируем)
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4,6,7. Жмем по очереди на кнопки: сохранить и применить.(Если вдруг 6 и 7 пункт не активны, проверьте в разделе настройки пункт "Версия API", должна стоять V2)
7. Далее ждем примерно 5 минут, очищаем кэш браузера и обновляем страницу. Пока в разделе Службы не появится пункт "Zapret2".
8. Возвращаемся в Zeroblock, открываем вкладку Автонастройка и убираем галки с 6 и 7 пункта.(Автозагрузка) Иначе мы не сможем вносить изменения в секциях со списками. Сохранить, применить.
9. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
10. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
11. Проверяете работу Youtube на всех устройствах. (так же желательно в браузерах отключить функцию "Частный/безопасный DNS")

---

**2026-03-03T23:09:46 | 𝓐𝓵𝓮𝓴𝓼𝓪𝓷𝓭𝓻**
Почему только в компьютере ютуб работает через zapret2,а на мобильном и смар тв нет?

---

**2026-03-04T00:32:03 | Swh1te**
Подскажите пожалуйста, использую Zapret (первой версии) и ютюб на телевизоре Самсунг работать отказывается, как победить?

---

**2026-03-04T08:11:20 | Андрей Стыврин**
Добрый день. 
Есть роутер РТК, к которому подключён РР, на нём настроен podkop + zapret. Получил второй РР, подключил его также к роутеру РТК, настроил его, отключил, но теперь через первый РР не работает телега через подкоп. 
Что можно сделать?

---

**2026-03-04T10:53:20 | Garsia**
Помогите, плиз, разобраться в ситуации. 
У меня стоит Zapret2 (включена секция Ютуба) и ZeroBlock. В ZB Опера прокси и AWG10 (те, что по умолчанию) отключены. 

Добавил свой конфиг AWG (создал новый интерфейс) и через него в ZB пустил несколько списков сообщества (AI, Meta и др.), но не Ютуб. При этом в Ютубе появилась реклама (той страны, в которой мой сервер с AWG).

Почему такое может быть, и куда копать? 
Самое интересное: если в секции маршрутизации выключить все списки сообщества и оставить только свои домены, реклама в Ютубе уходит.

---

**2026-03-04T11:00:38 | Anna Bagler**
Тогда странно, а если zb и zapret2 перезапустить?

---

**2026-03-04T11:01:26 | Garsia**
Всё пробовал. Если ZB отключить и оставить Zapret2, реклама пропадает.

Странно, я поэтому сюда и пишу. Может, у кого-то было такое

---

**2026-03-04T11:18:36 | Vasilii Pavlenko**
Добрый день, сегодня получил роутер, первичную настройку сделал, запустил Zero+Zapret2.  Ютубы/телеги заработали норм.Теперь вопрос по сути. Я живу в Крыму, из-за санкций имеется блок со стороны Blizzard и прочих США компаний. Чтобы получить доступ к Battle.net использую на своих девайсах КВН в виде 3х-ui панель Vless +reality  на  VPS в Нидерландах + клиент V2RayNG на моих клиентах (ПК +тел)  . Как мне теперь это все завернуть через Роутерич, а не поднимать на каждом девайсе клиента V2Ray? Какую службу я должен поднять на роутере и закинуть туда конфиг файл ? Заранее спасибо

---

**2026-03-04T11:25:34 | Евгений**
Итак пошаговый мануал для владельцев Routerich, как завести Zeroblock+Zapret2 на дефолтных настройках.
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки"и ждем, закрываем появившуюся табличку нажав на кнопку "ОК".
3. Качаем два файла (zeroblock_*** и luci-app-***) из закрепа темы "Zeroblock" и сохраняем в папку на рабочем столе.
4. Возвращаемся в разделы Система-пакеты и жмем на кнопку "Загрузить пакет". И по очереди ставим скачанные пакеты: Zeroblock_*** а затем luci-app***.(Табличку с надписью Error игнорируем)
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4,6,7. Жмем по очереди на кнопки: сохранить и применить.(Если вдруг 6 и 7 пункт не активны, проверьте в разделе настройки пункт "Версия API", должна стоять V2)
7. Далее ждем примерно 5 минут, очищаем кэш браузера и обновляем страницу. Пока в разделе Службы не появится пункт "Zapret2".
8. Возвращаемся в Zeroblock, открываем вкладку Автонастройка и убираем галки с 6 и 7 пункта.(Автозагрузка) Иначе мы не сможем вносить изменения в секциях со списками. Сохранить, применить.
9. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
10. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
11. Проверяете работу Youtube на всех устройствах. (так же желательно в браузерах отключить функцию "Частный/безопасный DNS")

---

**2026-03-04T11:50:44 | Евгений**
и дискорд отключите если не пользуетесь, если пользуетесь, то переведите в zapret2

---

**2026-03-04T11:54:16 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.0-r2:
  Поддержка IDN-доменов(собственный конвертер, возможны ошибки)
  - Теперь можно вводить кириллические домены прямо в настройках: яндекс.рф, привет.рф и т.д. ZeroBlock автоматически конвертирует их в Punycode (xn--...) перед добавлением в конфиг sing-box. Работает во всех полях: user_domains, excluded_domains, custom domain_list, текстовые списки, JSON/txt файлы. Реализован полный алгоритм RFC 3492 + NFC нормализация (корректная обработка составных символов й, ё).

  Детальная диагностика секций
  - check_outbounds теперь показывает полную информацию: community_lists, user_domains, user_subnets, excluded_domains, excluded_ips, catch_all, disable_fakeip и все остальные параметры. FakeIP статус виден прямо рядом с именем секции.

  Диагностика
  - Новая кнопка для принудительного обновление индекса и списков

  Диагностика Zapret/Zapret2
  - Новая карточка в диагностике: показывает NFQWS_OPT из zapret v1 и strategy секции с hostlist из zapret2.

  Auto-detect формата списков
  - При скачивании пользовательских списков доменов ZeroBlock теперь автоматически определяет формат (JSON ruleset или plain text) и обрабатывает соответственно.
  
  DPI check
  — YouTube Stream Check в DPI-диагностике: двухфазная проверка (Innertube API → скачивание 5MB видео), управляет стратегией rr_youtube в zapret2
  
  Добавлена новая зависимость conntrack, чтобы родительский контроль применялся сразу, не дожидаясь смерти соединения

  Исправления
  - Поддержка XHTTP mode и extra параметров
  - Буфер для proxy_string увеличен с value (обычный буфер) до proxy_buf[4096] (для длинных XHTTP extra URL)
  - Исправлена ошибка, когда AAAA-запросы ломали FakeIP DNS при выключенном IPv6 — теперь FakeIP правила матчат только query_type=A.
  - Пустые route rules (при 404 URL списка) теперь автоматически удаляются — защита от случайного catch-all, когда весь трафик уходил в VPN.
  — sections_loader сохраняет порядок секций при обновлении (больше не пересоздаёт)
  — excluded_source_ips сохраняется при автозагрузке секций с сервера
  — init.d разрешает старт без секций при awg_auto_config / opera_auto_config
  - Списки IP-адресов по URL с query string (например opencck.org) не загружались — json-c парсил IP-адрес как число, файл не конвертировался в JSON и sing-box не стартовал
  - Секция с привязанными domain_list ошибочно определялась как catch-all — привязанные списки доменов игнорировались
  - Автоустановка теперь отслеживает какой компонент выбран для установки и забирает с сервера необходимую секцию. первоначальная настройка не требует включения автозагрузки секций
#ZeroBlock

---

**2026-03-04T12:16:09 | Routerich**
rm /etc/config/zeroblock* /tmp/zeroblock_status.json && rm -rf /tmp/zeroblock /etc/sing-box/subscriptions /etc/zeroblock
rm /etc/config/zapret2* && rm -rf /opt/zapret2

---

**2026-03-04T12:31:20 | Роман**
Не сочтите за наглость, можно ешё команду для удаления zapret2, а то остатки остались.

---

**2026-03-04T12:32:20 | Святос**
opkg remove --autoremove zapret2 наверное

---

**2026-03-04T12:37:44 | Andrey Lazarev**
Уважаемые специалисты, можете подсказать - при установленных podkop и zapret2, есть ли простой способ (если вообще есть) обойти замедление телеги сейчас?

---

**2026-03-04T12:38:07 | Роман**
Удалил через пакеты zapret2, zeroblock, затем вашу команду в терминал для удаления остатков zeroblock.
Установил последний zb, в нем поставил галку скачать zapret2, он скачался, а мои секции остались. Вопрос, как полностью удалить zapret2 с роутера?

---

**2026-03-04T12:40:21 | Святос**
opkg files zapret2
rm -rf /etc/config или где надет

---

**2026-03-04T13:05:31 | Wenzel Perminov**
 DPI check
  — YouTube Stream Check в DPI-диагностике: двухфазная проверка (Innertube API → скачивание 5MB видео), управляет стратегией rr_youtube в zapret2
а как это для пользователя выглядит, галочку где-то ставить надо или что то прожимать?

---

**2026-03-04T13:50:24 | Anna Bagler**
Мастер, zeroblock+ zapret2, потом mesh.

---

**2026-03-04T13:53:20 | Роман**
Zapret2.
ватсап
Zeroblock.
доступ к амазоновским сервакам для сетевых игр
Тут уж что добавите в zb, то и будет работать.

---

**2026-03-04T14:56:02 | Routerich**
а если остановить zapret? podkop? работать начинает?

---

**2026-03-04T15:55:33 | Petr Shcherbinin**
root@RouteRich:~# du -h /tmp
0       /tmp/usr/lib/opkg/info
0       /tmp/usr/lib/opkg
0       /tmp/usr/lib
0       /tmp/usr
0       /tmp/opkg-lists
241.4M  /tmp/zapret2
20.0K   /tmp/zeroblock/sing-box.d
60.0K   /tmp/zeroblock/cache
16.0K   /tmp/zeroblock/rulesets
308.0K  /tmp/zeroblock
0       /tmp/urllogger.lck
0       /tmp/amneziawg
0       /tmp/spool/sms/sent
0       /tmp/spool/sms/failed
0       /tmp/spool/sms/checked
0       /tmp/spool/sms/outgoing
0       /tmp/spool/sms/incoming
0       /tmp/spool/sms
0       /tmp/spool/cron
0       /tmp/spool
4.0K    /tmp/odhcpd-piofolder
0       /tmp/dnsmasq.d
4.0K    /tmp/lib/dbus
0       /tmp/lib/misc
4.0K    /tmp/lib
4.0K    /tmp/hosts
4.0K    /tmp/etc/ksmbd
0       /tmp/etc/uhttpd
4.0K    /tmp/etc/stubby
8.0K    /tmp/etc/ssl
24.0K   /tmp/etc
4.0K    /tmp/resolv.conf.d
0       /tmp/.uci
0       /tmp/tmp
0       /tmp/log
0       /tmp/overlay
0       /tmp/extroot
8.0K    /tmp/sysinfo
8.0K    /tmp/state
0       /tmp/lock
16.0K   /tmp/run/internet-detector
4.0K    /tmp/run/avahi-daemon
0       /tmp/run/xl2tpd
0       /tmp/run/dbus
0       /tmp/run/wpa_supplicant
0       /tmp/run/hostapd
8.0K    /tmp/run/modemmanager
4.0K    /tmp/run/dnsmasq
0       /tmp/run/rpcd/snapshot-delta
0       /tmp/run/rpcd/snapshot-files
0       /tmp/run/rpcd/uci-575626180842fdef38cc4d3b1927885d
0       /tmp/run/rpcd/sessions
0       /tmp/run/rpcd
0       /tmp/run/ubus
100.0K  /tmp/run
0       /tmp/shm
242.5M  /tmp

---

**2026-03-04T17:04:01 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.0-r2:
  Добавлена новая зависимость conntrack, чтобы родительский контроль применялся сразу, не дожидаясь смерти соединения
  Вывод версии при запуске
  Статус работы zapret/zapret2 не является ошибкой/не ошибкой
  При установленном dns-failsafe-proxy в dnsmasq устанавливается перенаправление на него
#ZeroBlock

---

**2026-03-04T18:33:46 | Андрей**
Подскажите как заставить работать (Автозагрузка новой стратегии Zapret2) ?

---

**2026-03-04T18:52:49 | K**
В ZB поставил галочку установить Zapret2. Кэш почистил, перезашел, но в списке установленных не появился. Что делать?

Просто из пакетов установил.

---

**2026-03-04T21:06:15 | Святос**
https://github.com/youtubediscord/magisk-zapret2

---

**2026-03-04T21:39:44 | Routerich**
Или пробуйте zapret2

---

**2026-03-04T22:59:05 | Aндрей**
10. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.

после этого ютуб погас

---

**2026-03-05T05:52:43 | IT**
Zeroblock не конфликтует с Zapret2. Могу и то и то включить?

---

**2026-03-05T06:00:54 | Евгений Фролов**
root@RouteRich:~# zeroblock system_moni
tor

========================================================================
         ЗАПУСК МОНИТОРИНГА СИСТЕМ...  
========================================================================


========================================================================
         ВЫБОРОЧНЫЙ МОНИТОРИНГ СИСТЕМ  
========================================================================

🌐 Интернет: ✅ Доступен

🔹 WARP (AmneziaWG): ⏭️  Мониторинг отключен
🔹 Opera Proxy: ⏭️  Мониторинг отключен
🔹 Zapret (DPI):
──── YouTube Stream Check ────────────────────────────────────────
  YouTube: api_blocked ❌ (0 bytes, API: 5003ms, Stream: 0ms)
─────────────────────────────────────────────────────────────────
И после этого отключает стратегию ютуб. И остаюсь без запрета.

---

**2026-03-05T11:21:27 | IT**
В настройках zapret2 не видно стратегий. Только ютуб и дефолный список. Ну вкладки списки и скрипты

---

**2026-03-05T11:22:14 | Anna Bagler**
Изучать мануал по zapret2 и использование блокчек.

---

**2026-03-05T12:20:20 | Серёга Богданов**
Добрый день!, через подкоп ютуб плохо грузил, я его удалил оттуда и включил zapret, запустил скрипт по подбору стратегий и в конце он выдал такое:

---

**2026-03-05T13:08:08 | Вячеслав Шевченко**
Здравствуйте. а инстаграмм и роблокс реально сделать имея zeroblock+zapret2 ?

---

**2026-03-05T13:39:08 | Никита**
У меня у zapret после установки 0.7.0, висит 0.9.4.3, пока разбираюсь

---

**2026-03-05T13:58:32 | Anna Bagler**
Если у вас LG, то вам в запрет2 и просить о помощи @BFMVPoison 
В любом случае лучше использовать связку zeroblock и zapret2.

---

**2026-03-05T19:18:34 | JR Kirill**
Не помогало ничего в целом) Вернул всё обратно со скрипта5, ток снес zapret и поставил zapret2. Обновил все пакеты какие есть стало лучше запускать на сервера в подборе игроков

---

**2026-03-05T19:29:56 | Владимир Волков**
снес zapret и поставил zapret2

---

**2026-03-05T20:52:04 | KyM**
Подскажите куда прописывать стратегии которые нашли blockchech.sh и blockchech2.sh ? прописываю в поле NFQWS_OPT на вкладке Zapret - Settings ->
NFQWS options, но сайты которые были указаны в стратегиях по прежнему не работают.

---

**2026-03-05T21:34:34 | KyM**
Всё куда надо прописываю согласно мануалу но не помогает. А не может ли мешать podkop, правда он отключен на момент опытов с zapret, но может быть всё ровно как то влиять?

---

**2026-03-05T21:37:21 | Gomer Simpson**
Если у вас Zapret - поищите в теме Интернет без границ АВТОКОНФИГУРАТОР. Если Zapret2 - в инструкции есть типы стратегий - вот от них вам нужны стандартные шапки, и только потом вставляете найденные строчки.

---

**2026-03-05T22:24:57 | Роман**
https://github.com/StressOzz/Zapret-Manager
Этот скрипт пробовали?

---

**2026-03-05T22:40:35 | Aндрей**
Давайте определимся с терминами - что мы подразумеваем под словом «стратегия»? Команды в поле «Опции NFQWS» в zapret 2? Верно?

---

**2026-03-06T00:21:34 | Vasa**
например как тут реализовано
https://github.com/GubernievS/AntiZapret-VPN

---

**2026-03-06T09:12:18 | Vasa**
Ты весь гугл чтоли в маршруты загнал?
Там же большой пулл адресов

Вообще тебе нужен проект типа антизапрета, с раздельным впн и нормальным определением по днс запросу. 

Вот тут такое есть например. На кинетиках точно работает

https://github.com/GubernievS/AntiZapret-VPN

---

**2026-03-06T11:38:51 | Камиль**
Он меня этой идеей заразил 😁 я хотел бы пустить почти все через zapret2, а что не идёт или геоблок, то уже в прокси. Но пока времени нету эксперименты устраивать 😢

---

**2026-03-06T12:50:06 | Anna Bagler**
Пробуйте поставить zapret и подобрать стратегию https://t.me/routerich/3845/509958

---

**2026-03-06T13:01:03 | Anna Bagler**
Cистема - Пакеты, кнопочка Обновить списки, в поле фильтра zapret, установить.
По стратегиям код запускаете из сообщения и проверяете на устройствах.
https://t.me/routerich/4/530652

---

**2026-03-06T13:05:34 | Anna Bagler**
Cистема - Пакеты, кнопочка Обновить списки, в поле фильтра zapret, установить.
По стратегиям код запускаете из сообщения и проверяете на устройствах.

---

**2026-03-06T13:11:50 | Anna Bagler**
100% нет, но попробовать стоит с zeroblock и zapret2.

---

**2026-03-06T13:17:43 | Anna Bagler**
Только zapret и luci к нему.

---

**2026-03-06T13:33:18 | Marina V**
Добрый день! Следуя инструкции установила Zeroblok и zapret2. Из awg исключила ютуб (всё по пунктам). Какое-то время ютуб работал, потом перестал (подключался только с впн). Сегодня вернула галочку в awg - всё опять нормально работает. Что-то может при настройке упустила? Хотя в конце делала диагностику - везде стояли зелёные галочки

---

**2026-03-06T16:38:00 | Святос**
https://github.com/whxtelxs/nfqws-zapret-converter

---

**2026-03-06T16:53:09 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.0-r18:
  Исправления:
  - DPI проверки ждут полного запуска zapret2. Решает проблему ложного stream_blocked когда zapret2 ещё не загрузил правила.
  - Ошибочный статус нерабоспособности Mangle rules и Proxy rules.
  - bootstrap и основной DNS проверяются через реальный DNS-запрос вместо ping.
  - Убраны повторы проверки fakeip в диагностике.
  - dynamic nft sets. обновление таймера при обращении к IP.
#ZeroBlock

---

**2026-03-06T17:15:44 | Netizen**
Теперь из коробки не идут никакие ZeroBlock, zapret, youtubeublock и тп?

---

**2026-03-06T17:26:48 | Anna Bagler**
Пробуйте перезапустить zapret2.

---

**2026-03-06T17:36:23 | Anna Bagler**
Пробуйте обновить zapret2 в Система - Пакеты. Обновить списки. Вкладка Обновление.

---

**2026-03-06T17:38:44 | Anna Bagler**
Обновить списки. И потом в поле фильтра zapret2 и Обновления.

---

**2026-03-06T17:50:49 | Anna Bagler**
Остались файлы от старых версий. Попробуйте через поле фильтра удалить все по zapret2, а потом поставить вновь.

---

**2026-03-06T17:53:13 | Anna Bagler**
В поле фильтра zapret2, Вкладка Установлено, удалить то, что будет по zapret2.

---

**2026-03-06T17:56:36 | Anna Bagler**
Теперь Обновить списки, снова фильтр и ставьте 2 файла по zapret2.

---

**2026-03-06T18:04:33 | Anna Bagler**
@BFMVPoison, @ded_ikar  подскажите человеку по zapret2 для YouTube.

---

**2026-03-06T18:31:05 | Роман**
Значит отключайте запрет2, включайте запрет 1, это в терминал и перебирайте стратегии.
sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh)
Discord в секции Youtube_Discord в подкопе замените на аниме допустим или чем другим, но не тем что есть в секции main. Дискорд убрать потому что запрет 1 настроен и на ютуб, и на дискорд.

---

**2026-03-06T18:46:10 | Роман**
sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh)

---

**2026-03-06T18:55:05 | Nikita Bekmemetev**
Доброго времени суток. Роутер с коробки в службах отсутствует youtubeUnblock. Нужно самостоятельно ставить luci app youtubeunblock? А также каков шанс что добавив Discord к youtubeUnblock он будет работать? или лучше zapret-manager ?

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

**2026-03-06T21:13:53 | Михаил**
Подскажите. Выставленый в zeroblock doh или dot скрывает dns обращения всего трафика, проходящего через роутер, или только обращения к доменам из списков zapret2+zeroblock, или вообще лишь zeroblock?

---

**2026-03-06T21:25:31 | KyM**
Метка в Zapret2

---

**2026-03-06T21:28:48 | Anton Spodineyko**
Уважаемые знатоки, вопрос: кто знает какие IP и домены надо прописать в исключения что бы начал норм работать Fortnite?
Через поиск нашел пару вопросов, но нормального ответа нет. Все вопросы пропускались. Единственный нормальный совет был про Zapret 2. Это единственный вариант?

---

**2026-03-06T21:52:44 | Сергей**
Что-то сегодня начал Zapret2 себя по-другому вести. До сегодняшнего дня всё работало, а сегодня как-то не так)
Сижу, смотрю себе ролики на Youtube. Вдруг раз и пропало всё - видео не грузятся. Остальные сайты глянул - работают. Пошел посмотреть что в настройках, а там у запрета все галки со всех стратегий сняты. Ну, думаю, ладно, мало ли что там у него случилось - поставил галку обратно на rr_youtube. Всё завелось, сижу, смотрю дальше. 
Через несколько часов ситуация повторилась. Только теперь в запрете добавилась стратегия rr_blackhole и она была включена. 
В логах ZB ошибки от dpi_checker и http_client (см. скрин).
Я так понимаю, это связано с настройкой ZB "Автозагрузка новой стратегии Zapret2"? И тогда почему она вырубает ту стратегию, которая у меня работает? Или я вообще всё неправильно понял?😅

---

**2026-03-07T05:09:44 | Anna Bagler**
Ручное прописывание убрать. Из секций пока убрать. Перезапустить запрет2, посмотреть. Если не поможет, тогда запрет2 остановить и отключить, YouTube и cdn google в awg.   Или подбирать стратегию для zapret2.

---

**2026-03-07T08:08:10 | Ярослав Онищенко**
Приветствую
Прошу сильно не пинать, только разбираюсь. Никак не могу заставить работать роблокс. Использую podkop и zapret2
Много находил, что в подкопе надо просто выбрать список роблокс, но его больше не вижу
Я попробовал определить его домены через впн + f12 в браузере, вкинул список в podkop в строке "Список пользовательских доменов". Сайт роблокса вроде грузится, даже запустил приложение. Но дальше не могу войти ни в одну игру внутри самого роблокса, полагаю какие-то еще домены нужны. И вот тут затуп, не понимаю как мне их выловить
Через запрет вообще не выходит, создал списки с доменами и IP, сделал стратегию - но не работает вообще. В итоге отключил

Нужна помощь разобраться в какую сторону двигаться

---

**2026-03-07T09:22:25 | Роман**
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки"и ждем, закрываем появившуюся табличку нажав на кнопку "ОК".
3. Качаем два файла (zeroblock_*** и luci-app-***) из закрепа темы "Zeroblock" и сохраняем в папку на рабочем столе.
4. Возвращаемся в разделы Система-пакеты и жмем на кнопку "Загрузить пакет". И по очереди ставим скачанные пакеты: Zeroblock_*** а затем luci-app***.(Табличку с надписью Error игнорируем)
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4,6,7. Жмем по очереди на кнопки: сохранить и применить.(Если вдруг 6 и 7 пункт не активны, проверьте в разделе настройки пункт "Версия API", должна стоять V2)
7. Далее ждем примерно 5 минут, очищаем кэш браузера и обновляем страницу. Пока в разделе Службы не появится пункт "Zapret2".
8. Возвращаемся в Zeroblock, открываем вкладку Автонастройка и убираем галки с 6 и 7 пункта.(Автозагрузка) Иначе мы не сможем вносить изменения в секциях со списками. Сохранить, применить.
9. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
10. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
11. Проверяете работу Youtube на всех устройствах. (так же желательно в браузерах отключить функцию "Частный/безопасный DNS")
Ссылка на пакеты для скачки: https://t.me/routerich/394153/432061?single

---

**2026-03-07T10:15:24 | Aндрей**
Zapret2 - он для чего нужен, подскажите пожалуйста

---

**2026-03-07T11:58:15 | Роман**
Если нет, тогда либо самому подбирать через блокчек, либо певый запрет с https://github.com/StressOzz/Zapret-Manager

---

**2026-03-07T12:11:29 | Егор**
Всем привет! Полистал чаты, но не нашел обсуждения этого вопроса:
Есть ли какой то рабочий прокси для ТГ по типу zapret? От кого то слышал, что есть, но подтверждения найти не могу..

---

**2026-03-07T14:58:59 | Mallory**
обновился до 0.7.0-r18, стоит Zapret2, стратегия  youtube - Enabled, в диагностике пишет Disabled

---

**2026-03-07T15:04:58 | Anna Bagler**
Отключить пока zeroblock и zapret2. Проверить обновление списков.

---

**2026-03-07T17:16:16 | Andrew**
Youtubeunblock подбирал скриптом стратегии, на телефоне smarttube работает, на atv нет, та же самая версия. Через zapret пробовал, тоже самое.

---

**2026-03-07T18:09:32 | Роман**
sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh)
Попробуйте установить 1й запрет этим скриптом и проверьте работу ютуба. Второй отключить на время работы первого.

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

**2026-03-07T22:49:52 | Михаил**
Zapret2  на lg и samsung со  стратегией @BFMVPoison на ура ютуб поднимает.

---

**2026-03-08T00:07:41 | Prosto_Vasia77 🇷🇺**
ZB + Zapret2

---

**2026-03-08T00:10:40 | Дмитрий Григорьев**
Всем привет, такой вопрос, я только приобрёл роутер и начинаю во всём разбираться, Поставил ZB + Zapret2 по инструкции, Выкинул из списков Ютуб и Дискорд, запрет не пашет, Кинуть VLESS ключ пока не пробовал, хочу сначала разобраться с запретом. Есть ли какие-то доп инструкции, что бы это всё запахало, возможно выбор стратегий в запрете и тд, пока чёт вообще ничего не понимаю

И можно ли бахнуть первый запрет вместо второго, что бы работал в паре с Zeroblock?

---

**2026-03-08T01:22:53 | Serg**
Анализ запущен: 2026-03-08 01:15:18
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.72 | YouTube IP:  173.194.221.190

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.22 MB
  Пинг (ya.ru via awg10): 6.068 / 7.759 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock zapret2

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock              awg10 (vpn): anime,discord,googleplay,messengers,meta,news,porn,socials,video
  zeroblock          opera (prx out): ai,geoblock,shop,torrent,cdn_akamai,cdn_aws,cdn_cdn77,!_cdn_cloudflare,cdn_digitalocean,cdn_gcore,cdn_hetzner,cdn_oracle,cdn_ovh,cdn_scaleway,cdn_vultr
  Версия zeroblock: 0.7.0-r18
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.10.1 (Прошивка: 24.10.5)
  CPU: 0.40 | RAM: 24% | NAND: 44% занято / 37.9M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-03-08T08:06:53 | Pushkin**
Zapret2  v0.9.20260226 стоит версия, смотрю мануалы, есть раздел Blockcheck2, а у меня отсутствует - где взять?)

---

**2026-03-08T08:50:43 | Grigory**
Анализ запущен: 2026-03-08 08:48:23
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
  Facebook IP:  198.18.3.83 | YouTube IP:  142.251.143.110

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.68 MB / ↑0.14 MB
  Пинг (ya.ru via awg10): 63.985 / 81.013 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock zapret2

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock              awg10 (vpn): porn,news,anime,youtube,discord,video,messengers,googleplay
  zeroblock          vless (prx url): ai,block,geoblock,meta,socials
  Версия zeroblock: 0.7.0-r18
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.2.1 (Прошивка: 24.10.5)
  CPU: 0.93 | RAM: 31% | NAND: 28% занято / 48.3M доступно
  0 0 * * * /bin/sh /tmp/zapret_autoconfig.sh
  24 3 */2 * * /opt/zapret/ipset/get_config.sh
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-03-08T11:09:52 | Stanislav Sheshunov**
Как обновиться на zapret 2 с первой версии? Спасибо

---

**2026-03-08T11:27:47 | Sergey**
При попытке установить по  Zeroblock ,  Zapret2 не установился. Попробовал установить пакеты отдельно, выдаёт ошибку. Подскажите, что делать?

---

**2026-03-08T15:56:54 | Артём Давыдов**
Установил zeroblok_0 и luc, в автонастройке поставил галки, но в службах zapret2 так и не появился🤔🤔

---

**2026-03-08T17:42:57 | Александр**
Большое спасибо. С запретом разобрался
А как пустить трафик через по нужным сайтам через amnezia? Zapret например, ни в какую не открывает speedtest, хотя нужные домена прописаны. При этом, с остальными прописанными ресурсами все ок

---

**2026-03-08T19:08:38 | Alex Alex**
а сколько ждать появления в службах zapret2, за 10 мин не появился

---

**2026-03-08T22:14:04 | Михаил**
Zapret2

---

**2026-03-08T23:40:14 | X**
Теперь zapret2 в службах не появляется, в автонастройке zb пишет установлено, сделал далее как в гайде прописано - ютуб без впн везде стал открываться.

---

**2026-03-09T04:36:52 | Anna Bagler**
Если ничего не ставили, то анблок, он мог не подхватить ТВ, рассмотрите связку zeroblock+zapret2 для установки. Анблок тогда отключить. Он есть, но нет luci к нему.

---

**2026-03-09T04:46:45 | Anna Bagler**
Можете пробовать копать. Но я бы удалила и поставила zeroblock c галочкой на zapret2.

---

**2026-03-09T05:52:20 | Михаил**
Бесплатные обходы нагружены сильно. Особенно в выходные и по вечерам. Пробуйте zapret2, если заведется, пошустрее станет.

---

**2026-03-09T06:02:19 | Михаил**
Стратегию от @BFMVPoison в теме zapret2 найдите. У меня на ней и андроид и  айфон и телики завелись.

---

**2026-03-09T10:38:20 | Артём Давыдов**
Установил вчера после обновления прошивки  Zapret2.
Перестал работать rutracker, strava.
Как включить обратно?🤔

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

**2026-03-09T11:49:05 | Александр**
Работает ли связка ZeroBlock/zapret2 при использовании 4g модема?) вопрос особо актуален для регионов

---

**2026-03-09T12:17:48 | Aleksandr Kuznetsov**
Добрый день!
После покупки роутера поставил ZB, все нормально установилось, но ютуб нормально не завелся. Потом времени как то не было возится, отложил на потом.
Сейчас решил все по новой сделать, сбросил роутер до заводских, установил все пошагово по инстукции - службы ZeroBlock и Zapret2 есть, но нет секции awg10, только opera.
Что делаю не так?

---

**2026-03-09T12:29:21 | Pavel**
Zapret2 устанавливается с ошибкой несколькими ошибками, переустановка не помогла, удаление других тоже не дало результатов

---

**2026-03-09T12:46:35 | Routerich**
посмотрите как реализован детект автолиста в zapret2 он там как-то считает пакеты, потому что подтверждений нет

---

**2026-03-09T12:48:08 | Игорь Щеголев**
У меня также ZeroBlock и Zapret2 есть, но нет секции awg10, только opera. И ASU обновление не работает, крутится колёсико бесконечно.😱

---

**2026-03-09T12:57:46 | РУЗОВ Дмитрий**
Ребята,: 
- лучше сразу смотреть в сторону Zeroblock+Zapret2, чтобы не переучиваться еще раз.
- если устанавливать Zeroblock+Zapret2, то в иструкции написано, что установка долгая. Правильно понимаю, что в этот момет роутер отрубит всю сетку? Т.е если сейчас по сети смотрят ТВ, то отрубится соединение

---

**2026-03-09T13:00:06 | РУЗОВ Дмитрий**
лучше сразу смотреть в сторону Zeroblock+Zapret2 - это направление правильное

---

**2026-03-09T13:24:16 | РУЗОВ Дмитрий**
Если установлю пакеты по инструкции из тем в чате  Zeroblock+Zapret2 могу решить такую потребность:
- полноценная работа Телеги
- внедрить квн на RR , чтобы можно было не включать на устройствах (ключи работающие есть разных типов vMess, Vless)

---

**2026-03-09T13:42:08 | Anna Bagler**
Zeroblock можно, исключения по IP, zapret - нет.

---

**2026-03-09T14:26:09 | Anna Bagler**
Zapret2 и отдельная тема для него. Инстаграм не выйдет.

---

**2026-03-09T15:05:57 | Anna Bagler**
Можете ставить, но для начала стоит попробовать стратегии для zapret1.

---

**2026-03-09T15:46:44 | РУЗОВ Дмитрий**
Ставллю, не могу добиться появления в службах undefined
"Zapret2

---

**2026-03-09T15:52:42 | РУЗОВ Дмитрий**
Ребят, не могу добисться появления пункта в Службах Zapret2, что делаю не так?

---

**2026-03-09T16:59:34 | D Ch**
Всем привет!
Я правильно понимаю что zapret2 никак не конфликтует с подкопом? Раньше любая дурилка все ломала в подкопе

---

**2026-03-09T17:09:28 | D Ch**
https://github.com/vernette/ss-zapret2

---

**2026-03-09T17:28:33 | Роман**
Так ставьте из пакетов zapret2 тогда.

---

**2026-03-09T17:31:06 | D Ch**
Нет в пакетах zapret2

---

**2026-03-09T19:14:23 | Никита Веселов**
Привет, только приобрел Routerich AX3000. Неделю читал мануалы и хочу сказать огромное спасибо! ZeroBlock + Zapret2 выбрал для обхода. И все заработало чуть ли не с первого раза (пришлось список для AWG10 расширить)) Теперь везде все работает и даже Meta VR. Низкий поклон☺️

---

**2026-03-09T19:23:37 | Роман**
sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh)
Можно этим скриптом стратегии подобрать, но это для заперт 1. Второй пока отключить.

---

**2026-03-09T19:27:25 | D Ch**
или имеется ввиду снести zapret2, установить zapret и через скрипт подобрать стратегию? и потом накатить zapret2

---

**2026-03-09T20:23:04 | РУЗОВ Дмитрий**
Поставил Zeroblock+Zapret2 по иструкции, все получилось. Ютуб заработал.
Подскажите пожалуйста, где можно в Zapret2 вставить свой ключ?

---

**2026-03-09T20:24:09 | Routerich**
Здравствуйте.
В zapret2 не ставится ключ.
А вот в zeroblock можно
Службы->zeroblock->создайте там отдельную секцию и туда закиньте ключ

---

**2026-03-09T21:20:39 | VLADIMIR**
vr и в первом zapret работает но классно что разобрался , я не смог

---

**2026-03-10T08:22:26 | Routerich**
нет, главное чтобы домены не пересекались между Podkop и zapret2

---

**2026-03-10T09:15:01 | Routerich**
по умолчанию настраивается на opera-proxy + Amnezia WG (если работает) + zapret (если работает)

---

**2026-03-10T09:55:05 | Anna Bagler**
Если у вас только прокси, то zapret2 или zapret с подбором стратегий.

---

**2026-03-10T10:18:47 | IT**
Обновил до версии 7.
А как сделать чтобы в zapret2 новые стратегии прилетели?
Или предварительно надо было удалить все от старого?

---

**2026-03-10T10:23:46 | Routerich**
выбрать режим версию API 2, и включить автоконфигурацию zapret2

---

**2026-03-10T11:49:07 | D Ch**
Прошил вчера последним реализом, накатил zapret2, перебрал стратегии из подобранных, пока забил

---

**2026-03-10T12:12:23 | РУЗОВ Дмитрий**
Рома, приветсвую. Если правильно понимаю, то для обхода ZB+Zapret2

---

**2026-03-10T12:15:45 | Евгений Могилевский**
День добрый. Подскажите, пожалуйста, на Xbox вылезла ошибка с регионом после установки routerich. Стоит main+zeroblock+zapret2 (по инструкции ставил), все работает, а региональная ошибка вот вылезла. До этого сидел на кинетиках, там просто прописал по инструкции с Xbox DNS правило и в ус не дул. Как и куда запихнуть DNS адреса, или правило с DNS, раздел какой, или поставить что нужно дополнительно? Заранее благодарен.

---

**2026-03-10T12:36:49 | Михаил**
Копать в сторону zapret2

---

**2026-03-10T13:15:22 | Anna Bagler**
Ставьте сразу zeroblock и zapret2. И потом смотрите. Анблок отключить или крутите его.

---

**2026-03-10T13:39:55 | Routerich**
Юзать zapret2, он сразу идёт в комплекте с ним, если галочку поставить.

---

**2026-03-10T14:30:18 | Евгений Могилевский**
Смотрю прямо сейчас, подкоп не использую. На чистую систему поставил по инструкции zeroblock+zapret2, все завелось по умолчанию без дополнительных настроек. Проверил в браузере, apple tv 4k, android mi box. Единственное, что не завелось, apple tv3, прописывать/разбираться не стал.

---

**2026-03-10T16:26:33 | Astro768**
Всем здравствуйте. Поставил новую прошивку, запустил скрипт из BETA, интернет есть, но youtube и discord не работают. Как починить? Нужно ли ставить zapret2 вместо zapret?

---

**2026-03-10T16:42:24 | Astro768**
Попробую сделать zapret2, как это сделать?

---

**2026-03-10T16:45:40 | Astro768**
Я просто сам принцип работы не понимаю видимо, в диагностике написано, что zapret не включен, но он не по этому не работает?

---

**2026-03-10T17:10:03 | KyM**
Добрый день, может кто сталкивался, с работающим Zapret2 перестает загружается на Андройд (ТВ и телефон) приложение LAMPA при этом через браузер (на ТВ и телефон) нормально работает с сайта lampa.mx

---

**2026-03-10T17:12:36 | Routerich**
например в  zapret

---

**2026-03-10T17:17:39 | Astro768**
Нужно ли выключить podkop если я скачал Zapret2?

---

**2026-03-10T17:26:18 | Astro768**
А как понять робит ли zapret2 или zapret1?

---

**2026-03-10T17:28:41 | Astro768**
Не очень понимаю, я же выше кидал скрин, и там написано, что у меня zapret отключен, а ютуб все равно работает.

---

**2026-03-10T17:29:15 | РУЗОВ Дмитрий**
Анализ запущен: 2026-03-10 17:26:30
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
  Facebook IP:  198.18.3.27 | YouTube IP:  64.233.164.91

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.70 MB / ↑0.37 MB
  Пинг (ya.ru via awg10): 42.676 / 58.419 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock zapret2

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock              awg10 (vpn): anime,googleplay,messengers,meta,news,porn,socials,video
  zeroblock          opera (prx out): geoblock,ai
  Версия zeroblock: 0.7.0-r28
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.76.2 (Прошивка: 24.10.5)
  CPU: 0.11 | RAM: 25% | NAND: 50% занято / 33.9M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

root@myLAN:~#

---

**2026-03-10T17:32:51 | Astro768**
А если я отключу podkop и включу zapret2, так будет работать? Просто зачем мне вообще zapret2 если есть подкоп? Объясните пожалуйста.

---

**2026-03-10T17:36:32 | РУЗОВ Дмитрий**
при установлке ZB+Zapreta2 не могло удлатить youtubeUnblock

---

**2026-03-10T17:38:46 | Роман**
Zapret отключите.

---

**2026-03-10T17:48:30 | ギン**
0 4 * * * service zapret restart
13 9 * * * /usr/bin/podkop list_update

---

**2026-03-10T17:56:31 | РУЗОВ Дмитрий**
все правильно, Zapret2 и там стоит ютуб, ютубанблок я отключал, а оказалось, что он у меня удален. Не пойму как это произлошло.

---

**2026-03-10T18:01:35 | Николаич**
Благодарю, тезка. А в Zapret2 аналогично?

---

**2026-03-10T18:08:32 | Anna Bagler**
zeroblock и zapret2. Анблок отключить и остановить или удалить. Остальное по вашим целям.

---

**2026-03-10T18:11:30 | Николаич**
Спасибо за инфу. У меня ютуб работает через Zapret 2

---

**2026-03-10T19:21:28 | KyM**
надо не просто домены в список exclude прописать, но и добавит сам список exclude в стратегии ключом --hostlist-exclude=/opt/zapret2/ipset/zapret-hosts-user.txt

---

**2026-03-10T19:28:22 | Nikolay Barkalov**
что сейчас юзать? zapret2 или скрипт5?

---

**2026-03-10T20:08:24 | KyM**
Снес  версию GitHub - поставил "Нашу" - не появляется в службах 🤷‍♂️.  (поставил сперва zapret2, затем luci-app-zapret2)

---

**2026-03-10T20:10:50 | РУЗОВ Дмитрий**
Скачал мануалы, буду курить их. Коротко можно понять ZB и Zapret2 они связаны между собой и в мануалах я могу понять что и как.

---

**2026-03-10T20:15:45 | KyM**
с "Нашим" zapret 2 и Lampa работает сразу. Всем Спасибо за подсказки!👍

---

**2026-03-10T20:33:27 | HiLLL**
2 пакета установили zapret2?

---

**2026-03-10T21:08:09 | Роман**
Здравствуйте. Да. Попробуйте это
https://github.com/StressOzz/Zapret-Manager
Там есть игровой режим. Возможно вам он поможет.

---

**2026-03-10T21:27:44 | D Ch**
Нашел такую тему
https://github.com/remittor/zapret-openwrt/issues/382#issuecomment-3692819512

Но никакого решения

---

**2026-03-10T22:59:01 | Den Kihot**
Добрый вечер. Пытаюсь установить Zeroblock. В логах ошибки, Zapret2 так и не появляется. Можете помочь?

---

**2026-03-10T23:02:41 | Den Kihot**
Спасибо. Zapret2 появился, но в логах Zeroblock эти ошибки остались. Это норм?

---

**2026-03-11T09:01:57 | Александр**
Всем привет! Второй день за ночь отваливается ZeroBlock и zapret2 (не открываются нужные сайты при этом службы запущены). Захожу в панель, а там "WARP: Отключено"
Помогает перезапуск нужных служб. В чем может быть проблема?

---

**2026-03-11T10:46:07 | Marina V**
Подскажите, какие Community Lists ставить в секцию awg10, и как её использовать вместе с zapret2?” Также вопрос по опере. Вставила туда свои домены - дополнительные по gpt (которые жпт сам и рекомендовал). Браузерная версия открывается без проблем, а вот app всё равно видит гео

---

**2026-03-11T10:51:55 | Святос**
Zapret в настройках хранит свои списки, а коммунистический лист - свои, вот так их работа и не пересекается

---

**2026-03-11T11:33:46 | Alex**
Установил скрипт номер 5, который подразумевает для части ресурсов zapret, а для части podkop(vpn)

Все отлично работает на устройствах из локальной сети.
Если я подключаюсь к роутеру через VPN (сервер AmneziaWG на роутере), трафик проходит через zapret, но не через podkop. В какую сторону копать для решения проблемы?

В веб-интерфейсе http://routerich.lan/cgi-bin/luci/admin/services/podkop при подключении через VPN пишет "браузер не использует FakeIP"

Разобрался: в настройках Podkop нужно было добавить интерфейс AmneziaWG в Source Network Interface.

---

**2026-03-11T12:24:41 | Роман**
sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh)
Можно первым запретом попробовать. Второй отключить, с первым не использовать.

---

**2026-03-11T17:56:07 | Anna Bagler**
Ставьте пока возле proxy, warp, zapret2 и автозагрузка стратегии zapret2.

---

**2026-03-12T00:29:29 | IM**
Добрый вечер. Если на роутер с zeroblock и zapret2 поднять сервер wireguard и извне подключаться к нему со смартфона, я правильно понимаю, что весь трафик смартфона будет идти через домашнюю сеть? То есть на смартфоне после подключения по wireguard с роутеру заработают youtube и т.д.?

---

**2026-03-12T00:59:44 | Petr Shcherbinin**
доброй ночи, немного запутался
поднял на иностранном впс https://github.com/GubernievS/AntiZapret-VPN?tab=readme-ov-file, получил конфиг амнезии

хочу роутер натравить целиком на свой сервер, чтобы спискам управял он 

мне надо в зироблок сделать новую секцию, туда добавить свой впн (заранее добавленный в интерфейсы) и принудительно как-то направить весь трафик без всяких списков через "Fully Routed IPs"? или есть путь проще?

---

**2026-03-12T09:03:34 | Anna Bagler**
Меняйте в настройках самого подкопа. Отключайте и останавливайте youtubeUnblock. Подбирайте стратегию для zapret.

---

**2026-03-12T09:59:51 | I/O**
Здравствуйте. Подскажите пожалуйста по моей задаче? У меня сейчас стоит zeroblock, настроил по инструкции, которую здесь часто кидают. В секциях отключил работу awg и оперу (вроде как пока не нужно если есть свой сервер), сделал секцию со своим vless. Через vless у меня сейчас идут списки Ютуб, мессенджеры итд, остальное идёт напрямую. Хотелось бы попробовать вариант чтобы пустить обход блокировки Ютуба по dpi, а не через ВПН (остальное можно оставить на ВПН). Подскажите последовательность действий, какими инструментами лучше пользоваться, как маршрут настроить? Вместе с зероблоком установился zapret2, я так понимаю его как-то настроить можно? Или лучше через youtubeunblock? Заранее благодарю за инфу.

---

**2026-03-12T10:34:01 | Anna Bagler**
В теме zapret2 посмотрите решения и попробуйте у себя.

---

**2026-03-12T10:56:04 | Димон**
Добрый день. Подскажите zapret2 может мешать работе anydesk? не могу подключиться.

---

**2026-03-12T11:01:39 | Димон**
Тоже слышал, знать бы точно, кто работает с anydesk и zapret, чтоб понять проблему.

---

**2026-03-12T11:36:56 | Petr Shcherbinin**
https://telegra.ph/AntiZapret-WireGuardAmneziaWG-on-OpenWrt-03-16

по этому гайду пересоздал впн-подключение, все отлично завелось при работе на виндовой тачке, не работает на устройствах ios

просто держу в курсе

---

**2026-03-12T12:08:50 | Никита Веселов**
Получилось подключиться, а Zapret2 при таком подключении учавствует?

---

**2026-03-12T12:42:09 | Anna Bagler**
1. Попробуйте перенести список meta в секцию proxy. 2. Попробуйте другую стратегию для zapret2. Можно посмотреть в теме Zapret2.

---

**2026-03-12T14:20:57 | Anna Bagler**
Тогда вам первый запрет отключать, ставить запрет2 и пробовать стратегию от @BFMVPoison, она есть в теме zapret2.

---

**2026-03-12T16:28:13 | Bullet for my valentine Poison**
https://ntc.rkn.quest/t/zapret2-обсуждение/21161/762 а так?

---

**2026-03-12T16:30:04 | Bullet for my valentine Poison**
https://ntc.party/t/zapret2-ipv6-16кб-тспу-блокировки/22707 уже вовсю юзают)

---

**2026-03-12T16:35:24 | Gomer Simpson**
ZB+Zapret2.

---

**2026-03-12T16:37:28 | Андрей Стыврин**
На РР стоял zapret (Z) и podkop (P), всё работало, решил поставить ZB. Для этого остановил эти сервисы, установил ZB (Z2 был установлен ранее и был остановлен), запустил автоконфигурацию, запустил ZB и Z2, ни один сайт не открывается.
Остановил ZB и Z2, запустил Z и P, снова заработало.
Внимание, вопрос, как заставить работать ZB при остановленных Z и P?

---

**2026-03-12T16:44:59 | Роман**
Кто ж спорит. Работает с zb и zapret2 и в ус не дует.

---

**2026-03-12T16:46:26 | Gomer Simpson**
У вас неверное понимание задачи. Вы планировали переключаться между ZB и подкопом/между Zapret и Zapret2? Если ваши обходы отвалятся в подкопе - в ZB они не взлетят по мановению волшебной палочки.

---

**2026-03-12T17:10:22 | Никита Байдин (DOOMGUY)**
Не уж-то пора переходить Zapret2 или ZeroBlock?

---

**2026-03-12T17:17:17 | Никита Байдин (DOOMGUY)**
Был уже. Не пора уже переходить на Zapret2 или ZeroBlock...

---

**2026-03-12T17:20:01 | Роман**
Повторюсь, связка podkop/zapret1/2 работает. Zeroblock/zapret2/1 тоже работает. 
А что вам удобнее - ваш выбор.

---

**2026-03-12T17:22:48 | Арсений Спиридонов**
zapret может мешать вообще любому транспорту, потому что его задача - именно "ломать" трафик
где когда и как сервер начнёт считать запросы невалидными (причём оправданно) - никто не знает

---

**2026-03-12T20:02:08 | Роман**
rm /etc/config/zeroblock* /tmp/zeroblock_status.json && rm -rf /tmp/zeroblock /etc/sing-box/subscriptions /etc/zeroblock
rm /etc/config/zapret2* && rm -rf /opt/zapret2
Мне такие команды дал разработчик.

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

**2026-03-13T09:03:47 | ᅠ ᅠ**
Ну чё сказать, я перекатился с подкопа на зб и всё пашет прям из коробки (из мануала тоесь)
Пункт 10. 
Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
Это не выполнил, но всё равно работает, ну и пусть работает вощемто

---

**2026-03-13T09:05:16 | Andrew**
Здравствуйте. На роутере стоит zeroblock + zapret2. Можно ли это все дело подружить с adguard home? Я ещё не пробовал его ставить, решил сначала узнать можно ли это сделать в принципе?

---

**2026-03-13T09:05:37 | Anna Bagler**
Если вы список YouTube не убрали из zb и поставили zapret2, то будет конфликт.

---

**2026-03-13T14:40:13 | Molodoy Makkonehi**
а подскажите как добавить discord в zapret2 ? думал он из под коробки там в конфигах, но как только исключил его из всех секций, то ютуб продолжил свою работу, а дискорд сразу вывалился

---

**2026-03-13T18:46:06 | Anna Bagler**
Влад и zapret отключите и остановите. Или наоборот, уoutube из подкопа убирайте и стратегию для запрет подбирайте.

---

**2026-03-13T20:04:39 | Gomer Simpson**
sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh)

---

**2026-03-13T20:44:57 | Артём Власкин**
Добрый день!

Помогите с настройкой роутера. Apple TV по проводу не прогружает YouTube и кинопаб. Apple TV по wifi загружает Youtube, но не грузит кинопаб. C мобильных устройств (планшеты, телефоны) все работает. В список пользовательских доменов добавил уже адреса кинопаба (api.kinopub.com, api.teleos.club и тд). Zapret отключил. Прикладываю скриншоты работы скрипта и диагностики подкопа.

---

**2026-03-13T20:49:39 | Egor Sorokin**
потыкал, проверил стратегии, тесты меня не радовали так что я просто удалил :)  установил заново zapret 2 и оно заработало, почему, как не знаю, но спасибо тебе за помощь, открыл мне новую команду в колекцию)

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

**2026-03-13T21:46:31 | X**
у меня zb, ну и zapret2 после установки zb. там это можно сделать? я для ps5 делал присвоение ip и добавлял в секции в полная маршрутизация. я так понимаю надо ip приставки таким же образом добавить, только куда? в запрете получается ?

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

**2026-03-13T23:36:02 | Egor Sorokin**
* checking system
Linux/openwrt detected
kernel: Linux version 6.6.119 (builder@buildhost) (aarch64-openwrt-linux-musl-gcc (OpenWrt GCC 13.3.0 r29087-d9c5716d1d) 13.3.0, GNU ld (GNU Binutils) 2.42) #0 SMP Wed Dec 17 21:08:22 2025
distro: RouteRich 24.10.5
openwrt release: RouteRich 24.10.5 r29087-d9c5716d1d RR-3.9.0
openwrt board: mediatek/filogic
openwrt arch: aarch64_cortex-a53
firewall type is nftables
CURL=curl
curl 8.12.1 (aarch64-openwrt-linux-gnu) libcurl/8.12.1 mbedTLS/3.6.5 nghttp2/1.63.0
Release-Date: 2025-02-13
Protocols: file ftp ftps http https ipfs ipns mqtt
Features: alt-svc HSTS HTTP2 HTTPS-proxy IPv6 Largefile SSL threadsafe UnixSockets
* checking already running DPI bypass processes
* checking privileges
* checking prerequisites
* checking DNS
system DNS is working
comparing system resolver to public DNS : 8.8.8.8
pornhub.com : OK
ej.ru : OK
rutracker.org : OK
www.torproject.org : MISMATCH
-- system resolver :
198.18.23.20
-- 8.8.8.8 :
204.8.99.146
116.202.120.165
116.202.120.166
95.216.163.36
204.8.99.144
-- POSSIBLE DNS HIJACK DETECTED. ZAPRET WILL NOT HELP YOU IN CASE DNS IS SPOOFED !!!
-- DNS CHANGE OR DNSCRYPT MAY BE REQUIRED
* searching working DoH server
https://cloudflare-dns.com/dns-query : FAIL
https://dns.google/dns-query : FAIL
https://dns.quad9.net/dns-query : FAIL
https://dns.adguard.com/dns-query : FAIL
https://common.dot.dns.yandex.net/dns-query : FAIL
all DoH servers failed
could not find working DoH server. exiting.
это же не очень хорошо?
upd: не знаю правильно или нет но он ищет еще с порнушки, хз почему

---

**2026-03-14T02:09:39 | Артем Рахаев**
Всем привет! Подскажите, у меня на роутере нет Zapret и Podkop, установлен youtubeUnblock, но YouTube не работает. Нужно ли как-то настраивать YU, есть какой-то мануал?

---

**2026-03-14T09:33:31 | Evgenij B**
Подскажите, купил только роутер, не вижу службы zapret в списке служб, в интерфейсе, запустить надо чтобы отображалось и можно было в интерфейсе управлять ?

---

**2026-03-14T10:09:34 | Иван**
Sat Mar 14 09:53:26 2026 user.notice TTL: TTL reload
Sat Mar 14 09:53:26 2026 daemon.info dnsmasq[1]: read /etc/hosts - 12 names
Sat Mar 14 09:53:26 2026 daemon.info dnsmasq[1]: read /tmp/hosts/dhcp.cfg01411c - 4 names
Sat Mar 14 09:53:26 2026 daemon.info dnsmasq[1]: read /tmp/hosts/odhcpd - 4 names
Sat Mar 14 09:53:26 2026 daemon.info dnsmasq-dhcp[1]: read /etc/ethers - 0 addresses
Sat Mar 14 09:53:26 2026 daemon.info internet-detector[6470]: WARP: started
Sat Mar 14 09:53:26 2026 daemon.info internet-detector[6469]: internet: started
Sat Mar 14 09:53:26 2026 daemon.notice ksmbd: Stopping Ksmbd userspace service.
Sat Mar 14 09:53:26 2026 daemon.notice ksmbd: Starting Ksmbd userspace service.
Sat Mar 14 09:53:27 2026 daemon.notice procd: /etc/rc.d/S98urllogger: start ok
Sat Mar 14 09:53:27 2026 daemon.warn odhcpd[2910]: No default route present, overriding ra_lifetime to 0!
Sat Mar 14 09:53:27 2026 user.notice MMconfig: MMConfig started
Sat Mar 14 09:53:57 2026 daemon.warn odhcpd[2910]: No default route present, overriding ra_lifetime to 0!
Sat Mar 14 09:53:58 2026 user.notice zeroblock: Starting ZeroBlock...
Sat Mar 14 09:53:58 2026 daemon.err zeroblock[7456]: [zeroblock] Starting ZeroBlock(0.7.1-r30)...
Sat Mar 14 09:53:58 2026 daemon.notice procd: /etc/rc.d/S99zeroblock:
Sat Mar 14 09:54:02 2026 daemon.err uhttpd[3108]: [info] luci: accepted login on / for root from 192.168.1.196
Sat Mar 14 09:54:02 2026 user.notice luci-app-smstools3: invalid pin
Sat Mar 14 09:54:11 2026 daemon.err zeroblock[7456]: [opkg_manager] Failed to install package 'luci-app-zapret2'
Sat Mar 14 09:54:11 2026 daemon.err zeroblock[7456]: [zapret2_manager] Failed to install zapret2
Sat Mar 14 09:54:11 2026 daemon.warn zeroblock[7456]: [zeroblock] Zapret auto-install failed: Zapret2 installation failed
Sat Mar 14 09:54:17 2026 daemon.info dnsmasq[1]: exiting on receipt of SIGTERM
Sat Mar 14 09:54:18 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: udhcpc: started, v1.36.1
Sat Mar 14 09:54:18 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: udhcpc: broadcasting discover
Sat Mar 14 09:54:20 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: udhcpc: no lease, failing
Sat Mar 14 09:54:20 2026 daemon.err zeroblock[7456]: [zeroblock] ZeroBlock started successfully
Sat Mar 14 09:54:20 2026 daemon.info dnsmasq[1]: started, version 2.90 cache disabled
Sat Mar 14 09:54:20 2026 daemon.info dnsmasq[1]: DNS service limited to local subnets
Sat Mar 14 09:54:20 2026 daemon.info dnsmasq[1]: compile time options: IPv6 GNU-getopt no-DBus UBus no-i18n no-IDN DHCP DHCPv6 no-Lua TFTP conntrack no-ipset nftset auth cryptohash DNSSEC no-ID loop-detect inotify dumpfile
Sat Mar 14 09:54:20 2026 daemon.info dnsmasq[1]: UBus support enabled: connected to system bus
Sat Mar 14 09:54:20 2026 daemon.info dnsmasq-dhcp[1]: DHCP, IP range 192.168.1.100 -- 192.168.1.249, lease time 12h
Sat Mar 14 09:54:20 2026 daemon.info dnsmasq[1]: using nameserver 127.0.0.1#5359
Sat Mar 14 09:54:20 2026 daemon.info dnsmasq[1]: using only locally-known addresses for test
Sat Mar 14 09:54:20 2026 daemon.info dnsmasq[1]: using only locally-known addresses for onion
Sat Mar 14 09:54:20 2026 daemon.info dnsmasq[1]: using only locally-known addresses for localhost
Sat Mar 14 09:54:20 2026 daemon.info dnsmasq[1]: using only locally-known addresses for local
Sat Mar 14 09:54:20 2026 daemon.info dnsmasq[1]: using only locally-known addresses for invalid
Sat Mar 14 09:54:20 2026 daemon.info dnsmasq[1]: using only locally-known addresses for bind
Sat Mar 14 09:54:20 2026 daemon.info dnsmasq[1]: using only locally-known addresses for lan
Sat Mar 14 09:54:20 2026 daemon.info dnsmasq[1]: read /etc/hosts - 12 names
Sat Mar 14 09:54:20 2026 daemon.info dnsmasq[1]: read /tmp/hosts/dhcp.cfg01411c - 4 names
Sat Mar 14 09:54:20 2026 daemon.info dnsmasq[1]: read /tmp/hosts/odhcpd - 4 names
Sat Mar 14 09:54:20 2026 daemon.info dnsmasq-dhcp[1]: read /etc/ethers - 0 addresses
Sat Mar 14 09:54:23 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: ========================================================================

---

**2026-03-14T10:09:44 | Иван**
Sat Mar 14 09:54:23 2026 daemon.notice procd: /etc/rc.d/S99zeroblock:           ZAPRET AUTO-INSTALLATION
Sat Mar 14 09:54:23 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: ========================================================================
Sat Mar 14 09:54:23 2026 daemon.notice procd: /etc/rc.d/S99zeroblock:
Sat Mar 14 09:54:23 2026 daemon.notice procd: /etc/rc.d/S99zeroblock:
Sat Mar 14 09:54:23 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: ========================================================================
Sat Mar 14 09:54:23 2026 daemon.notice procd: /etc/rc.d/S99zeroblock:   STEP [4/6]: Installing Zapret2
Sat Mar 14 09:54:23 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: ========================================================================
Sat Mar 14 09:54:23 2026 daemon.notice procd: /etc/rc.d/S99zeroblock:
Sat Mar 14 09:54:23 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: [4.1] Checking/installing zapret2...
Sat Mar 14 09:54:23 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: ❌ Failed to install/update zapret2
Sat Mar 14 09:54:23 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: ========================================================================
Sat Mar 14 09:54:23 2026 daemon.notice procd: /etc/rc.d/S99zeroblock:           ROUTING SECTIONS AUTO-LOAD
Sat Mar 14 09:54:23 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: ========================================================================
Sat Mar 14 09:54:23 2026 daemon.notice procd: /etc/rc.d/S99zeroblock:
Sat Mar 14 09:54:23 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: Fetching routing sections from server...
Sat Mar 14 09:54:23 2026 daemon.notice procd: /etc/rc.d/S99zeroblock:
Sat Mar 14 09:54:23 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: ✅ Successfully loaded 2 routing section(s)
Sat Mar 14 09:54:23 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: ✅ Loaded 2 routing section(s) from server
Sat Mar 14 09:54:23 2026 cron.err crond[8488]: crond (busybox 1.36.1) started, log level 5
Sat Mar 14 09:54:23 2026 daemon.notice procd: /etc/rc.d/S99zerotier: disabled in config
Sat Mar 14 09:54:23 2026 daemon.info procd: - init complete -
Sat Mar 14 09:54:25 2026 auth.err passwd: password for root changed by root
Sat Mar 14 09:54:30 2026 daemon.info procd: Instance smstools3::instance1 s in a crash loop 6 crashes, 0 seconds since last crash
Sat Mar 14 09:57:01 2026 daemon.err uhttpd[3108]: [info] luci: accepted login on /admin/system/system for root from 192.168.1.196
Sat Mar 14 09:57:50 2026 user.notice zeroblock: Stopping ZeroBlock...
Sat Mar 14 09:57:50 2026 daemon.err zeroblock[9734]: [zeroblock] Stopping ZeroBlock...
Sat Mar 14 09:57:51 2026 daemon.info dnsmasq[1]: exiting on receipt of SIGTERM
Sat Mar 14 09:57:53 2026 daemon.info dnsmasq[1]: started, version 2.90 cache disabled
Sat Mar 14 09:57:53 2026 daemon.info dnsmasq[1]: DNS service limited to local subnets
Sat Mar 14 09:57:53 2026 daemon.info dnsmasq[1]: compile time options: IPv6 GNU-getopt no-DBus UBus no-i18n no-IDN DHCP DHCPv6 no-Lua TFTP conntrack no-ipset nftset auth cryptohash DNSSEC no-ID loop-detect inotify dumpfile

---

**2026-03-14T10:36:57 | Иван**
вот логи из ЗБ, запрет не встает Sat Mar 14 10:21:02 2026 user.notice zeroblock: Enabled monitoring by default
Sat Mar 14 10:21:02 2026 user.notice zeroblock: No sections configured, restoring DNS and skipping start
Sat Mar 14 10:21:30 2026 user.notice ucitrack: Setting up /etc/config/zeroblock reload trigger for non-procd /etc/init.d/zeroblock
[clash_api] /proxies failed: Error
[clash_api] /proxies failed: Error
[clash_api] /proxies failed: Error
[clash_api] /proxies failed: Error
[clash_api] /proxies failed: Error
[clash_api] /proxies failed: Error
[clash_api] /proxies failed: Error
[clash_api] /proxies failed: Error
[clash_api] /proxies failed: Error
Sat Mar 14 10:22:22 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[cron_manager] Cron file not found: /etc/crontabs/root
[zeroblock] ZeroBlock stopped successfully
Sat Mar 14 10:22:27 2026 user.notice zeroblock: No sections yet, but auto-config enabled
Sat Mar 14 10:22:27 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock(0.7.1-r30)...
[clash_api] /proxies failed: Error
[clash_api] /proxies failed: Error
[opkg_manager] Failed to install package 'luci-app-zapret2'
[zapret2_manager] Failed to install zapret2
[zeroblock] Zapret auto-install failed: Zapret2 installation failed
[zeroblock] ZeroBlock started successfully
[cron_manager] Cron file not found: /etc/crontabs/root
luci: accepted login on /admin/services/zeroblock for root from 192.168.1.196
luci: accepted login on /admin/services/zeroblock for root from 192.168.1.196
Sat Mar 14 10:30:07 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Sat Mar 14 10:30:13 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock(0.7.1-r30)...
[opkg_manager] Failed to install package 'luci-app-zapret2'
[zapret2_manager] Failed to install zapret2
[zeroblock] Zapret auto-install failed: Zapret2 installation failed
[clash_api] /proxies failed: Error
Sat Mar 14 10:30:17 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Sat Mar 14 10:30:22 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock(0.7.1-r30)...
[opkg_manager] Failed to install package 'luci-app-zapret2'
[zapret2_manager] Failed to install zapret2
[zeroblock] Zapret auto-install failed: Zapret2 installation failed
[zeroblock] ZeroBlock started successfully
[zeroblock] ZeroBlock started successfully
Sat Mar 14 10:32:39 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Sat Mar 14 10:32:44 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock(0.7.1-r30)...
[clash_api] /proxies failed: Error
[clash_api] /proxies failed: Error
[opkg_manager] Failed to install package 'luci-app-zapret2'
[zapret2_manager] Failed to install zapret2
[zeroblock] Zapret auto-install failed: Zapret2 installation failed

---

**2026-03-14T10:42:28 | Роман**
Есть 2 запрета, 1 и 2 соответственно. На втором есть несколько стратегий в чате по запрет2, для запрет1 тоже есть скрипты подбора стратегий. 
Этот например. 

https://github.com/StressOzz/Zapret-Manager

---

**2026-03-14T10:47:50 | Данила Ступин**
Здравствуйте! Может кто сталкивался с такой проблемой и нашёл решение. Установлены zapret2 и zeroblock. На каждом настроены свои секции. Но есть небольшое количество сайтов, которые после установки запрета и зероблока начинают бесконечно загружаться (к примеру у меня одним из таких сайтов является https://calibre-ebook.com/). При этом этих сайтов нет в секциях запрета и зероблока (и РКН их не блокировал). Добавление доменов этих сайтов в запрет или зероблок также не помогает. И даже, если остановить обе этих службы, то сайты все равно грузиться не будет. 

Раньше я подобное наблюдал, если установить запрет через zapret manager, где все сайты принудительно идут через него. Но там это решалось включением режима работы только с заблокированными сайтами. Но zapret2 у меня и так работает в таком режиме.

И вот я даже не знаю куда копать. Единственное, что я выяснил, так это то, что у некоторых сайтов (rutracker к примеру) происходит dns hijacking. Проверял я это через специальную утилиту. Если не добавить такие сайты со всеми их доменами в zb (zapret2 использовать), то происходит перехват dns запроса оператором. Но этого быть не должно, так как роутер по умолчанию (а я сбрасывал настройки) вроде и так использует google dns. Может проблема, описанная выше, связана с этим, а может нет. В общем, если кто сталкивался с этим - буду рад любой помощи.

---

**2026-03-14T13:06:46 | Сергей**
При автостратегиях на api=v2 теперь zapret2 получает стратегию rr_blackhole, которая позволяет работать скриптам без основного zapret2

---

**2026-03-14T14:04:48 | Никита Веселов**
Настроен VPN в zeroblock и дискорд оттуда убран. Настроены домены дискорда через Zapret2. Но трафик через Zeroblock все равно идет в дискорд. Не понимаю почему такое может быть

---

**2026-03-14T14:59:00 | Виталий Александрович**
Перед тем как открыть ее же нужно создать новую? После установки zb+zapret2 доступно только две секции opera и awg10

---

**2026-03-14T16:42:19 | Andrei Frolov**
Привет!
Думаю приобрести Routerich AX3000. 
Глупый вопрос - но можно ли отдельно настроить политики для определенных устройств, чтобы они всегда шли наружу сразу через провайдера (нужно для рабочих ноутбуков)?
Т.е. чтобы траффик этого устройства не проходил через vpn, zapret и тд.

---

**2026-03-14T17:53:14 | Александр**
Добрый день, хочу купить роутер Routerich

нужна помощь

хочу реализовать схему

Интернет → (Мой роутер) → ПК (Zapret)
                ↓
          Второй роутер(Routerich) (zapret) → Wi‑Fi / ТВ

надо ли zapret ставить на роуетер или на флешку и потом в роутер?

и можно ли реализовать схему которую я сделал ?

---

**2026-03-14T17:59:44 | Александр**
я знаю что так тоже могу просто настройка zapret на ПК более гибкая, обновления почаще выходят, а вот роутеровский и отвалится может, и апдейт ждать на него, по этому раз мне в любом случае покупать роутер от Routerich чтобы Zapret потсавить

Интернет →  (Мой роутер, нет USB порта, нет поддержки OpenWRT ) → ПК
                ↓
          Второй роутер Routerich (zapret) → Wi‑Fi / ТВ

Итог ПК сам всё настаиваю, ТВ WIFI роутер делает

---

**2026-03-14T18:01:38 | Александр**
спасибо

и ещё подскажите пж насколько сейчас стабильно работает Zapret роутеровский?

ставить Zapret или Podkop?

---

**2026-03-14T18:03:11 | Routerich**
Podkop это средство маршрутизации для впн и прокси уже с готовыми списками, а Zapret это antiDPI служба что модифицирует трафик, их не сравнить. У нас есть Zapret2 с блокчеком - всё стабильно

---

**2026-03-14T19:24:21 | Egor Sorokin**
config_builder] Cleaning up dnsmasq configs...
[disable_fakeip] Cleaned up 0 disable_fakeip files
[config_builder] Restoring DNS configuration...
[dns_manager] No DNS backup found, nothing to restore
[config_builder] DNS configuration restored
[dns_manager] Restarting dnsmasq...
[config_builder] Sing-box failed to start in bootstrap mode (port 19999)
[zeroblock] Failed to start ZeroBlock
[dns_manager] dnsmasq restarted successfully
[config_builder] Removing NFTables rules...
[nft_manager] Tearing down TPROXY routing for table zeroblock
[nft_manager] TPROXY routing teardown complete
[config_builder] NFTables rules removed
[config_builder] Stopping sing-box...
[config_builder] Sing-box was not running
[config_builder] Removing policy routing...
[interface_monitor] Tearing down policy routing for table 100
[interface_monitor] Flushing routing table 100
[interface_monitor] Routing table flushed, deleted 0 routes
[interface_monitor] Policy routing teardown complete (IPv4 + IPv6)
[config_builder] Policy routing removed (fwmark=0x10000)
[config_builder] Removing cron jobs...
[cron_manager] Lists update cron job not found
[cron_manager] ZeroBlock cron job not found
[cron_manager] Cron job not found, nothing to remove
[cron_manager] Bad Interface monitor cron job not found
[config_builder] Cron jobs removed
[config_builder] ========================================================================
[config_builder] ZEROBLOCK STOPPED SUCCESSFULLY
[config_builder] ========================================================================
[zeroblock] ZeroBlock stopped successfully
Sat Mar 14 19:23:50 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock(0.7.1-r30)...
[zeroblock] Auto-config flags: AWG=0, Opera=0, Zapret=0, Sections=1, Xray=0, TT=0
[uci_manager] Committed changes to package: zeroblock
[zeroblock] Running sections auto-load...
[http_client] Executing HTTP request: GET
[config_builder] Sing-box failed to start in bootstrap mode (port 19999)
[zeroblock] Failed to start ZeroBlock

---

**2026-03-14T21:18:42 | K**
А если в списке нет zapret2 что нужно сделать? Списки обновлены. (Куди)

---

**2026-03-14T22:29:47 | ユージーン**
в SSH (это добавит пакеты PP)
sed -i 's/option check_signature/# option check_signature/' /etc/opkg.conf && echo 'src/gz routerich https://github.com/routerich/packages.routerich/raw/24.10.5/routerich' > /etc/opkg/customfeeds.conf && opkg update
или
sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Z2R/main/z2r.sh)
это установит Zapret 2 от PP

---

**2026-03-14T23:03:49 | Дмитрий**
Zeroblock + Zapret2. Копался только в ZB, в запрете ютуб по дефолту

---

**2026-03-14T23:43:36 | Nick**
Завтра будем zeroblock  вкорячивать. До сегодня обходился постом, молитвой и zapret.
Да и то последнего недели три как роставил

---

**2026-03-15T09:15:25 | ARTEM**
Обновился на версию r33 и ютуб через zapret лагать начал,через awg пустил всё норм, как через zapret опять сделать включены в запрете rr youtube,youtube,rr blackhole

---

**2026-03-15T11:07:38 | Anna Bagler**
Так если все, что надо, работает, пусть себе работает. Если прям хотите, обновляйтесь и zeroblock и zapret2.

---

**2026-03-15T11:11:52 | Monty**
Для человека который только погрузился в это, отключить zapret? или podkop целиком?

---

**2026-03-15T12:13:31 | Илья 🎮**
а куда делись zapret и zapret2 из пакетов??

---

**2026-03-15T12:16:21 | Роман**
И что показывает когда вводите например zapret?

---

**2026-03-15T12:46:54 | Виталий Александрович**
https://github.com/Flowseal/zapret-discord-youtube

кажется отсюда настраивал, но не точно

---

**2026-03-15T13:07:09 | Виталий Александрович**
Объясните пожалуйста, если я хочу открыть доступ к какому нибудь запрещенному ресурсу, то в принципе куда надо писать пользовательские домены и списки? 
opera, awg10 или создать там новую секцию со своими списками?
Или в zapret2 необходимо создать свой список доменов?

---

**2026-03-15T13:34:46 | Anna Bagler**
Zeroblock+zapret2.

---

**2026-03-15T14:00:22 | Роман**
Радостные вести для всех любителей роблокса принёс я! 
Его можно разблокировать запретом 1 от ztressozz.
Параметры на скриншоте.
sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh)

---

**2026-03-15T14:53:40 | Дмитрий Шаповалов**
Подскажите как добавить адреса тг в zapret или это бессмысленно?
у меня сейчас настроены в podkop все адреса на личный квн, но видео через раз грузит. На vds все адреса пингуются без потерь

---

**2026-03-15T15:18:21 | Виталий Александрович**
изначально устанавливал только zb и zapret2
zapret2 отключил и поставил zapret1

---

**2026-03-15T15:19:44 | Роман**
Я на голом запрете 1 тестировал, без podkop/zeroblock/zapret2, всё отключил.

---

**2026-03-15T15:29:35 | Виталий Александрович**
теперь как подружить zb  и zapret1  чтобы оба работали и не мешали друг другу? )

---

**2026-03-15T17:01:41 | Routerich**
Службы - zapret - отключить автостарт и остановить. Далее службы - podkop, список YouTube из секции с названием main убрать. В секцию с названием дискорд добавить

---

**2026-03-15T17:14:50 | Александр**
Добрый день, купил сегодня роутер Routerich, я хочу релизовать Схему

Интернет → Мой Роутер(1) → ПК (чистый интернет)
                         ↓
                   роутер Routerich(2) (zapret) → Wi‑Fi → ТВ

На Routerich просто стоит OpenWRT или там уже есть zapret?

надо ли подключать его по инстукции или я могу просто с Lan моего первого роутера(1) закинуть в WAN Routerich(2)?  

какая то иная настройка а моём случае или то же самое просто LAN(1)>WAN(2) и по инстуркции следовать или же снять на вермя мой роутер(1), настоить Routerich(2) потом уже сделать связку?

там по IP проблемма ещё будет надо сделать 192.168.2.1
для этого мне надо только один роутер оставить чтобы на нём поменять потом подключить второй?

---

**2026-03-15T17:16:38 | Routerich**
С lan в wan роутерича, zapret нужно установить на роутериче, можете сразу zapret2 из Система - пакеты установить

---

**2026-03-15T17:20:02 | Александр**
по поводу Zapret и Zapret2

информации не нашёл про то что лучше ставить, но знаю что есть Zapret manager им лего ставить первый Zapret а пот Zapret2 не в курсе, насколько он хорош? стоит ли его поставить? можно ли оба посавить сразу и тестировать ?

---

**2026-03-15T17:22:34 | Александр**
Zapret1 насколько я знаю поможет и На WIFI и ТВ разблокировать что надо
Zapret2 так же? лучше ?

---

**2026-03-15T17:22:42 | Routerich**
У zapret2 есть блокчек, с помощью которого рабочую стратегию можно найти, можете и то и то поставить для теста, но работать должен только один

---

**2026-03-15T17:26:42 | Routerich**
Zapret2 более гибкий и в дальнейшем с ужесточением блокировок и прочего под него можно будет много что вкусного сделать, с заделом на будущее он, а так для zapret есть автоконфигуратор например от нашего участника чата https://t.me/routerich/3845/420612

---

**2026-03-15T19:36:40 | Александр**
Подскажите сможет ли zapret или zapret2 сделать так чтобы Ютуб Заработал на SmartTV?

---

**2026-03-15T19:42:42 | Александр**
подскажите кто то смог сделать обход Instagram через Zapret? у меня на ПК не на одном ALT не работает

---

**2026-03-15T19:44:01 | Роман**
sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh)
Это в терминал, потом пункт 8 - удалить - установить - настроить называется.

---

**2026-03-15T20:05:03 | Александр**
а как надо ставить (по SSH знаю как)? это отличается от zapret manager-а? это дефолтный Zapret? можно ли поставить и его и zapret manager и zapret2 , и один включать ?

---

**2026-03-15T20:49:12 | Vadim**
Тоже пытаюсь гран туризмо починить на пс5
безрезультатно.

единственно что у меня кое кое завелся теккен на этой стратегии.


--filter-tcp=443 --filter-l7=tls --ipset=/opt/zapret2/ipset/ipset-all.txt --payload=tls_client_hello --lua-desync=hostfakesplit:host=2gis.ru:midhost=host-2:badsum:tcp_ack=-66000:tcp_ts_up

---

**2026-03-15T21:14:27 | Александр**
есть у кого Стратегия? а то я Zapret2 поставил а стратегии нету

---

**2026-03-15T21:27:13 | Александр**
я Zapret1 поставил протестировал вроде гуд работает

Zapret2 нету менеджера, вижу одну дефолтную стратегию которая  не работает 

вот эту стратегию нашёл

Стратегия на Zapret2 
--comment=Strategy__v6_by_StressOzz__ported_to_zapret2

--lua-init=@/opt/zapret2/lua/zapret-lib.lua
--lua-init=@/opt/zapret2/lua/zapret-antidpi.lua

--blob=quic_google:@/opt/zapret2/files/fake/quic_initial_www_google_com.bin
--blob=tls_www_google:@/opt/zapret2/files/fake/tls_clienthello_www_google_com.bin

--filter-tcp=443
--filter-l7=tls
--hostlist=/opt/zapret2/ipset/zapret-hosts-google.txt
--payload=tls_client_hello
--lua-desync=multisplit:pos=1,sniext+1:seqovl=1

--new
--filter-tcp=443
--filter-l7=tls
--hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt
--payload=tls_client_hello
--lua-desync=hostfakesplit:host=rzd.ru:midhost=host-2:seqovl=726:badsum:tcp_seq=-10000

--new
--filter-udp=443
--filter-l7=quic
--hostlist=/opt/zapret2/ipset/zapret-hosts-google.txt
--payload=quic_initial
--lua-desync=fake:blob=quic_google:repeats=6

--new
--filter-udp=19294-19344,50000-50100
--filter-l7=discord,stun
--hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt
--payload=stun,discord_ip_discovery
--lua-desync=fake:blob=0x00000000000000000000000000000000:repeats=6

--new
--filter-tcp=2053,2083,2087,2096,8443
--filter-l7=tls
--hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt
--payload=tls_client_hello
--lua-desync=multisplit:pos=2:seqovl=652:seqovl_pattern=tls_www_google

Ютуб заработал на zapret2, но честно говоря пока что zapret1 работает, работает корректно и есть Менеджер удобный

буду сидеть на zapret1

если у кого есть какая то информация полезная, по типу Телеграм раблокировать через Zapret2
буду рас прочитать

P.S Дс не работает

---

**2026-03-15T23:00:49 | AndrewKomarov**
Вопрос.
На чистый RR сейчас накатил скрипт5 ( он же еще относительно актуален?) Теперь надо запрет сносить и ставить Zeroblock+Zapret2 (где про него почитать?)

---

**2026-03-16T11:53:07 | Anna Bagler**
Zb - точечная маршрутизация, zapret2 - дурилка, в основном для yt. Обычно в паре.

---

**2026-03-16T12:43:41 | Anna Bagler**
У вас ютуб и через zeroblock, и через zapret2. Уберите из секции zeroblock. И проверьте.

---

**2026-03-16T14:13:14 | Ruslan**
Иду по пунктам инструкции. На п.7 не появляется zapret2 в службах. Жду уже 30 минут, очищаю кэш, перевхожу... Что делать с этим?

---

**2026-03-16T14:37:33 | Роман**
https://github.com/bol-van/zapret2/blob/master/docs/manual.md
Вот сложно. А тут в чате цветочки.

---

**2026-03-16T14:44:01 | Ruslan**
Не находит. В списке нет ничего с именем "zapret"

---

**2026-03-16T16:00:12 | Egor Sorokin**
* checking system
Linux/openwrt detected
kernel: Linux version 6.6.119 (builder@buildhost) (aarch64-openwrt-linux-musl-gcc (OpenWrt GCC 13.3.0 r29087-d9c5716d1d) 13.3.0, GNU ld (GNU Binutils) 2.42) #0 SMP Wed Dec 17 21:08:22 2025
distro: RouteRich 24.10.5
openwrt release: RouteRich 24.10.5 r29087-d9c5716d1d RR-3.9.0
openwrt board: mediatek/filogic
openwrt arch: aarch64_cortex-a53
firewall type is nftables
CURL=curl
curl 8.12.1 (aarch64-openwrt-linux-gnu) libcurl/8.12.1 mbedTLS/3.6.5 nghttp2/1.63.0
Release-Date: 2025-02-13
Protocols: file ftp ftps http https ipfs ipns mqtt
Features: alt-svc HSTS HTTP2 HTTPS-proxy IPv6 Largefile SSL threadsafe UnixSockets
* checking already running DPI bypass processes
* checking privileges
* checking prerequisites
* checking DNS
system DNS is working
comparing system resolver to public DNS : 8.8.8.8
pornhub.com : OK
ej.ru : OK
rutracker.org : OK
www.torproject.org : MISMATCH
-- system resolver :
198.18.23.20
-- 8.8.8.8 :
204.8.99.144
95.216.163.36
116.202.120.165
116.202.120.166
204.8.99.146
-- POSSIBLE DNS HIJACK DETECTED. ZAPRET WILL NOT HELP YOU IN CASE DNS IS SPOOFED !!!
-- DNS CHANGE OR DNSCRYPT MAY BE REQUIRED
* searching working DoH server
https://cloudflare-dns.com/dns-query : FAIL
https://dns.google/dns-query : FAIL
https://dns.quad9.net/dns-query : FAIL
https://dns.adguard.com/dns-query : FAIL
https://common.dot.dns.yandex.net/dns-query : FAIL
all DoH servers failed
could not find working DoH server. exiting.

мне кажется или что все dns over http которые не прошли, ухудшают работу, не так ли?

---

**2026-03-16T17:28:55 | Дмитрий**
Не подскажешь, что надежнее в плане обходов: просто накататит 5 скрипт или настроить по твоему совету(мануалу) в одной из веток zb и zapret2?

---

**2026-03-16T17:32:36 | Vladimir Turbin**
здравствуйте .
а zapret2 с podkop совместно будут работать 
если zapret2 на youtube а podkop на все остальное?

---

**2026-03-16T18:46:00 | Борис**
Нужно отключить adblock и zapret

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

**2026-03-16T22:11:20 | Andrei Frolov**
скрипт 5 применил, а потом сам поставил zapret2. больше ничего не делал

---

**2026-03-16T22:25:07 | Виктор ZEUS**
Здравствуйте , подскажите плиз , как сделать чтобы работал ChatGPt и Gemini ? Стоит Zapret 2

---

**2026-03-17T06:36:34 | Александр**
Выяснил, всё переустановил с нуля, когда работает Zapret2 телек не коннектится к смарт приложениям. Хотя в ZB добавил в исключения, получается в запрете добавить телек в исключения надо, а как непонятно. Надо политику под телек чтобы чистый  инет гнал, а как это сделать не пойму.

---

**2026-03-17T07:56:28 | Дмитрий**
Ссылки не найду сейчас наверное, а вот текст скопировал. Права на него принадлежат человеку с ником "bullet for my valentine poison ")
————

Итак пошаговый мануал для владельцев Routerich, как завести Zeroblock+Zapret2 на дефолтных настройках.
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки"и ждем, закрываем появившуюся табличку нажав на кнопку "ОК".
3. Качаем два файла (zeroblock_* и luci-app-*) из закрепа темы "Zeroblock" и сохраняем в папку на рабочем столе.
4. Возвращаемся в разделы Система-пакеты и жмем на кнопку "Загрузить пакет". И по очереди ставим скачанные пакеты: Zeroblock_* а затем luci-app*.(Табличку с надписью Error игнорируем)
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4,6,7. Жмем по очереди на кнопки: сохранить и применить.(Если вдруг 6 и 7 пункт не активны, проверьте в разделе настройки пункт "Версия API", должна стоять V2)
7. Далее ждем примерно 5 минут, очищаем кэш браузера и обновляем страницу. Пока в разделе Службы не появится пункт "Zapret2".
8. Возвращаемся в Zeroblock, открываем вкладку Автонастройка и убираем галки с 6 и 7 пункта.(Автозагрузка) Иначе мы не сможем вносить изменения в секциях со списками. Сохранить, применить.
9. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
10. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
11. Проверяете работу Youtube на всех устройствах. (так же желательно в браузерах отключить функцию "Частный/безопасный DNS")
Ссылка на пакеты для скачки: https://t.me/routerich/394153/432061?single

---

**2026-03-17T08:03:29 | Николаич**
Спасибо. А через Zapret 2 как организовать работу Телеграм

---

**2026-03-17T08:09:34 | Николаич**
Здравствуйте. Как настроить чтобы Телеграм работал через Zapret 2

---

**2026-03-17T09:14:56 | lxstwxrden**
Веб-версию ещё можно заставить работать быстро на другом IP телеги, и вписать домены в zapret тоже дабы обойти замедление по SNI

---

**2026-03-17T11:14:47 | Gomer Simpson**
Пусть это вам поставит: https://github.com/StressOzz/Zapret-Manager, а youtubeUnblock отключит.

---

**2026-03-17T12:30:29 | iProxx**
Всем привет. Есть проблема с установкой бета скрипта. Сначала как обычно устанавливается zapret, затем при настройке AWG Warp роутер не может подключиться к ip адресам, и перебирая 10 адресов выдает ошибку. После этого настраивает Opera Proxy и установка скрипта завершается перезагрузкой.
Примерно с неделю все работало (Youtube, Whatsapp, Telegram и т.п.) а после перестало.
Проблема с установкой скрипта наблюдается через Ростелеком.
Причем с другим провайдером (Уфанет) такой проблемы нет.
Есть какое то решение?

---

**2026-03-17T13:40:53 | Антон**
Еще раз, добрый день! Установил zapret2, discord отвязался. Помогите , плиз!

---

**2026-03-17T13:46:53 | Anna Bagler**
В теме zapret2 ищите стратегию и домены для discord или блокчеком подбирайте свою.

---

**2026-03-17T13:50:17 | Anna Bagler**
Тема Zapret2 рядышком, по ключевому слову ищите сообщения. Там же есть инструкция от Романа по блокчеку для чайников.

---

**2026-03-17T14:17:26 | Routerich**
https://github.com/remittor/zapret-openwrt

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

**2026-03-17T19:50:06 | Bullet for my valentine Poison**
Итак пошаговый мануал для владельцев Routerich, как завести Zeroblock+Zapret2 на дефолтных настройках.
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки"и ждем, закрываем появившуюся табличку нажав на кнопку "ОК".
3. Качаем два файла (zeroblock_* и luci-app-*) из закрепа темы "Zeroblock" и сохраняем в папку на рабочем столе.
4. Возвращаемся в разделы Система-пакеты и жмем на кнопку "Загрузить пакет". И по очереди ставим скачанные пакеты: Zeroblock_* а затем luci-app*.(Табличку с надписью Error игнорируем)
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4,6,7. Жмем по очереди на кнопки: сохранить и применить.(Если вдруг 6 и 7 пункт не активны, проверьте в разделе настройки пункт "Версия API", должна стоять V2)
7. Далее ждем примерно 5 минут, очищаем кэш браузера и обновляем страницу. Пока в разделе Службы не появится пункт "Zapret2".
8. Возвращаемся в Zeroblock, открываем вкладку Автонастройка и убираем галки с 6 и 7 пункта.(Автозагрузка) Иначе мы не сможем вносить изменения в секциях со списками. Сохранить, применить.
9. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
10. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
11. Проверяете работу Youtube на всех устройствах. (так же желательно в браузерах отключить функцию "Частный/безопасный DNS")
Ссылка на пакеты для скачки: https://t.me/routerich/394153/432061?single

---

**2026-03-18T00:37:51 | Sergey G**
списки ваши чем то лучше списков подкопа? у вас есть v1 и v2 есть ли плюсы от использования v2?
подкоп честно говоря пока вопросов не вызывал)
youtube там работает через zapret2

---

**2026-03-18T00:41:51 | Sergey G**
я сделал проще, на первом роутере остановил podkop и zapret2
выполнил команду zeroblock awg warp
WARP подключился

---

**2026-03-18T01:40:23 | Никита Веселов**
А как работает автозагрузка Zapret2 стратегий в zeroblock? галки стоят, а rr_ стратегии не появляются в запрете

---

**2026-03-18T01:40:39 | Александр**
Доброй ночи. Подскажите  Zapret2 работает на весь трафик при установленном ZB по умолчанию или только срабатывает на YT ? А то смарт телевизор не грузит приложения, а чистый инет нормально работает.

---

**2026-03-18T09:53:13 | Teleghost**
Службы - Zapret - Настройки - Host lists - User hostname entries
Это конфигурация скрипта №5 после сброса настроек.

---

**2026-03-18T11:03:55 | Routerich**
zapret2

---

**2026-03-18T12:11:12 | Anna Bagler**
Пробуйте пустить через zapret2 или использовать свою платную конфигурацию.

---

**2026-03-18T12:15:27 | Yaroslav Muss**
Итак пошаговый мануал для владельцев Routerich, как завести Zeroblock+Zapret2 на дефолтных настройках.
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки"и ждем, закрываем появившуюся табличку нажав на кнопку "ОК".
3. Качаем два файла (zeroblock_*** и luci-app-***) из закрепа темы "Zeroblock" и сохраняем в папку на рабочем столе.
4. Возвращаемся в разделы Система-пакеты и жмем на кнопку "Загрузить пакет". И по очереди ставим скачанные пакеты: Zeroblock_*** а затем luci-app***.(Табличку с надписью Error игнорируем)
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4,6,7. Жмем по очереди на кнопки: сохранить и применить.(Если вдруг 6 и 7 пункт не активны, проверьте в разделе настройки пункт "Версия API", должна стоять V2)
7. Далее ждем примерно 5 минут, очищаем кэш браузера и обновляем страницу. Пока в разделе Службы не появится пункт "Zapret2".
8. Возвращаемся в Zeroblock, открываем вкладку Автонастройка и убираем галки с 6 и 7 пункта.(Автозагрузка) Иначе мы не сможем вносить изменения в секциях со списками. Сохранить, применить.
9. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
10. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
11. Проверяете работу Youtube на всех устройствах. (так же желательно в браузерах отключить функцию "Частный/безопасный DNS")
Ссылка на пакеты для скачки: https://t.me/routerich/394153/432061?single

---

**2026-03-18T12:34:51 | Aleksei**
Друзья, а подскажите, пожалуйста, как привести Zapret2 от состояния с 2 стратегиями по умолчанию к состоянию со стратегиями rr_youtube / rr_default / rr_blackhole?

Запрет ставился автоматом из ZB, но стратегии не появились(

---

**2026-03-18T14:06:56 | IT**
Не особо ясно, что это означает:
При автостратегиях на api=v2 теперь zapret2 получает стратегию rr_blackhole, которая позволяет работать скриптам без основного zapret2

---

**2026-03-18T17:03:20 | Pavel I Vorobev 🦝**
А где взять такую красоту? В репе Ремиттора обычная Люся как для zapret1, без галочек.

---

**2026-03-18T18:15:32 | Вячеслав**
Добрый всем вечер. Такой вопрос, Zapret 2 не впн, хотел бы уточнить как разграничить трафик: есть зарубежные сервисы недоступные внутри из-за ухода из страны - через впн; есть зарубежные сервисы которые замедляют уже внутренние DPI - через Zapret 2.😤

---

**2026-03-18T18:18:14 | Вячеслав**
Zapret 2 не конфликтует с Podkop?

---

**2026-03-18T18:48:50 | Yaroslav Muss**
Что то у меня zapret2 не появляется, минут 20 уже обновляю страницу

---

**2026-03-18T18:57:21 | Владимир**
там сейчас так написано, или нет надписи что "запрет2 уже установлен"? + через пакеты по названию zapret2 можно глянуть

---

**2026-03-18T18:59:20 | Yaroslav Muss**
А zapret2 нет

---

**2026-03-18T19:03:36 | Anna Bagler**
Система - Пакеты, кнопочка Обновить списки, в поле фильтра zapret2, ok и что в Установлено покажет.

---

**2026-03-18T19:15:15 | Ivan Smirnov**
Друзья. Не очень понимаю как ZeroBlock работает.
Воткнул скрипт №5 с вариантом установки по дефолту без параметров.
Поменял конфиг у появившейся амнезии на свой с ВПСки (он рабочий)
В службы залетели Zapret2 и ZeroBlock.
Ютубчик работает, дискорд тоже. А вот те же ИИшки например - нет.
Хотя заблоченный Terraform работает (https://developer.hashicorp.com/terraform), а Sonatype Nexus (https://help.sonatype.com/en/sonatype-nexus-repository.html) - нет.
Не могу понять принцип..
Открывал настройки секции awg10 и добавлял туда пользовательские домены - ничего не поменялось.

---

**2026-03-18T19:18:27 | Роман**
Zeroblock/podkop - в обоих вариантах есть списки роблокса. Но желательно со своим сервером. Попробуйте з1, там и для дискорда, ютуба стратегии есть. Может и роблокс заведётся.
sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh)
Это в терминал.
Запрет 2 отключить с автозапуском, если будете пробовать.

---

**2026-03-19T09:26:11 | Sergey G**
Привет всем! После обновления прошивки 24.10.4 -> 24.10.5 исчезли службы Podpop и Zapret, это нормально? Или надо их как-то еще подчистить, может в фоне остались? Они не нужны на данный момент (ZB+Z2 стратегия), в автозагрузке их нет, Интерфейс AWG сохранился, остальные настройки тоже

---

**2026-03-19T12:11:48 | Gomer Simpson**
Мне эти причины ещё более непонятны. У меня Ю через Zapret2.

---

**2026-03-19T13:49:43 | Andrey 🐸**
Подскажите что лучше ставить чтобы все разблокировать, zapret или скрипт 5?

---

**2026-03-19T13:54:55 | Алексей Сергеевич**
YouTube пустить через Zapret2, telegram через awg

---

**2026-03-19T13:57:01 | Алексей Сергеевич**
Нет, Zeroblock это автонастройка, в которой можно отметить установку Zapret2

---

**2026-03-19T14:01:19 | Алексей Сергеевич**
Мне zeroblock больше нравится, не каких скриптов запускать не нужно, сбросил роутер, обновил пакеты, поставил 2 приложения, отметил 3 галочки opera, awg и zapret2 и готово. + в настройках выставил списки куда ходить, geo блок через opera остальное awg, YouTube через Zapret2

---

**2026-03-19T14:47:14 | iProxx**
Привет всем! По инструкции выше настроил Zeroblock + Zapret2 на последнюю прошивку. Youtube и Whatsapp работают. А как добавить Telegram? В списке сообществ его нет

---

**2026-03-19T15:21:00 | Виктор Замиралов**
Здравствуйте, у меня не работает телеграмм на 2ух телефонах из 3ёх. В чём причина и как сделать так, чтобы тг работал на всех устройствах в доме?
У меня есть vds(Финляндия) на HostVDS.com. На сервере установлен amnezia wg с помощью клиента amnezia vpn(self-hosted). На роутере установлен Youtubeunblock(выключен), zapret, podkop, awg. Все телефоны подключены к роутеру по wi-fi. На всех телефонах нет никаких vpn клиентов. В списках podkop выставлен только телеграмм. 
Итог: тг работает только на пк и на телефоне(с таким же аккаунтом как и на пк), а на 2ух других телефонах - не работает. При этом ютуб работает на всех устройствах(zapret).
P.S я мало что понимаю во всех этих делах, настраивал всё по гайдам из ютуба и т.д.
С протоколом vless такая же ситуация.
Если выключить podkop и установить на телефоны amnezia vpn и подключаться через него, то также работает только на том телефоне, у которого акк телеги используется на пк.

---

**2026-03-19T19:30:06 | Serg**
Не работает YouTube через Exit Node Tailscale (роутер Routerich, OpenWrt)

Здравствуйте. Помогите, пожалуйста, разобраться с удалённым доступом.

Что сделано и настроено:

1. Роутер Routerich AX3000 (прошивка OpenWrt). Настроен и работает интернет.
2. Установлен и настроен Zeroblock+Zapret2 для обхода блокировок. На домашнем Wi-Fi YouTube и другие сервисы работают отлично (на всех устройствах).
3. Настроил RemoteRouteRich (Tailscale) строго по вашей документации:
   · Создал сеть (rrpj7qaaa), сохранил ключи.
   · На роутере в разделе VPN → Tailscale указал сервер https://rc.routerich.ru/, ввёл Device Auth Key, служба включена.
   · В расширенных настройках роутера включил опцию «Узел выхода» (Exit Node).
4. На телефоне (Android, приложение Tailscale v1.94.2):
   · Указал тот же сервер https://rc.routerich.ru/.
   · Авторизовался тем же ключом.
   · Активировал Exit Node: нажал на устройство routerich в списке и включил там переключатель «Run as exit node». Также включил «Allow LAN access».
   · После этого на главном экране приложения появилась надпись «EXIT NODE: Running on this device» (скриншоты прилагаю).

Проблема:
Несмотря на то, что в приложении Tailscale на телефоне отображается активный Exit Node, YouTube (и другие заблокированные сайты) не работают при отключённом Wi-Fi (только мобильный интернет). Обычные сайты открываются.

Вопрос:
1. В чём может быть причина? В настройках роутера или приложения?
2. Нужно ли вручную добавлять правило для tailscale0 в межсетевом экране с включением Masquerading? Если да, то как правильно это сделать для моей модели?
3. Может быть, проблема в совместимости с Zeroblock/Zapret2? Нужно ли что-то дополнительно настраивать в Zeroblock (например, указать интерфейс tailscale0 во входящих интерфейсах)?

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

**2026-03-20T00:01:10 | ᚢᚹᛟᛈᛠᛋᛠᛊ ᛖᛊᚺᚱ**
Как будто без разницы, как я понял zeroblock использует zapret

---

**2026-03-20T08:55:17 | Роман**
Для теста попробуйте 

https://github.com/StressOzz/Zapret-Manager

---

**2026-03-20T08:58:20 | Alex Korshun**
Роман, спуститесь в тему Zapret2 и прочитайте мои последние сообщения.

---

**2026-03-20T09:12:05 | S V**
И так подготовил пакет.  Согласно инструкции  установил оба файла.  В пукте 6. " .... проставляем галки на пунктах: 1,2,3,4,6,7. Жмем по очереди на кнопки: сохранить и применить. Возможно не совсем правильно понял : выполнил поэтапно каждый пункт. 6. и 7. Прогружаться отказались. Ссылка на ошибку.  В службе появились: Zeroblock и  Zapret 2.  После установки  галочки    пропали со всем пунктов. Скрины. сечас подготовлю и вышлю.

---

**2026-03-20T11:08:42 | Bullet for my valentine Poison**
https://github.com/bol-van/zapret2/blob/master/docs/manual.md

---

**2026-03-20T11:36:07 | Борис**
Насчёт iptv не знаю, все остальное что ты перечислил будет работать. Я через этот роутер завёл Battlefield 6, когда его осенью блокировали (был на серверах амазона) через zapret, всё получилось - мог играть. Играл, к слову, на ps5, соответственно там с сетью тоже никаких проблем. Если что, просто настроишь, исключения добавишь в zapret. Ютуб тоже работает с этим роутером, телеграм тоже (я сейчас им пользуюсь). "Vpn" используется у меня только для telegram, всё остальное, включаяя игры и psn работает через zapret (система обхода dpi), а значит я использую свой российский ip и у меня нет дополнительных задержек из-за использования каких-то дополнительных серверов

---

**2026-03-20T11:37:44 | Борис**
Сейчас Battlefield 6 вроде как ушел с amazon, у него ресурсы на akamai, и там пока нет блокировок, можно без всяких обходов играть. Arc raiders я не знаю, но судя по тому, что ты сказал, там есть некий отдельный сервер для голосового чата, ты сможешь при помощи отладки его обнаружить и как-то добавить в zapret, либо просто загуглить "zapret arc raiders"

---

**2026-03-20T11:48:39 | Роман**
Не всё с помощью запрета делается. Чат арка подкопом вскрывается со всеми вытекающими. 
и как-то добавить в zapret
Шедеврально. А потом будет по чату бегать и спрашивать - а как так-то? Мне сказали что всё хорошо будет, а оно не работает. 
У всех блокировки разные.

---

**2026-03-20T13:23:31 | Alex Korshun**
Исключено на самом деле. Весь мусор с ПК был удален, все на роутере теперь. Но это и не важно, потому что снова ни шиша не работает :D 
Время от времени у моего провайдера такое бывает ага. Хотя что удивительно, у соседей тоже ТТК, но у них zapret1 вкрученный на ПК работает

---

**2026-03-20T13:40:38 | Vasilii Pavlenko**
хм, странно,  ZB стоит, работает, а в пакетах не вижу, только zapret2 фигурирует

---

**2026-03-20T14:37:19 | Святос**
Zapret2 закреп

---

**2026-03-20T15:19:26 | Борис**
К сожалению сейчас попал в такую ситуацию. Всё настроил, всё работает и не приходится ничего делать. А эти блокировки и белые списки - курам насмех, обходятся в два счёта. Даже скучно как-то, что оппонент в лице Регулятора оказался таким слабым. Жду новых блокировок, а пока не обновляю ни Zeroblock, ни Zapret2 - хорошее, стабильное ПО

---

**2026-03-20T15:51:50 | александр маслов**
отвалился тг  на телефоне  !!! говорит не в сети .на пк работает в браузере . zapret1

---

**2026-03-20T15:56:02 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.1-r56:
  Исправления:
  - YACD Dashboard — исправлена генерация URL для панели мониторинга. Теперь используется единая функция вместо ручной сборки адреса.

  Новое
  - DPI-обход для подключения к прокси (desync_bypass) — новая per-section настройка(на удивление в настройках), решающая проблему совместимости ZeroBlock с zapret2.
  Проблема: ZeroBlock ставил routing_mark 0x40000000 на все исходящие подключения к прокси-серверам. Этот mark совпадает с mark nfqws — zapret2 считал такие пакеты уже обработанными и пропускал их. В результате для CDN-прокси (например Cloudflare), чьи домены заблокированы провайдером, TLS handshake не проходил — DPI блокировал подключение.
  Решение: в настройках ZeroBlock появился multiselect "DPI обход для подключения к прокси". Для выбранных секций routing_mark не ставится, и zapret2 обрабатывает TLS handshake к прокси-серверу, обходя блокировку.
  По умолчанию поведение не изменилось — все секции работают как раньше. Опция нужна только для прокси с заблокированными доменами.
#ZeroBlock

---

**2026-03-20T16:04:07 | Святос**
Настроил статический маршрут между сетями двух роутеров, как будто бы перестал работать Zapret со второго роутера

---

**2026-03-20T16:18:57 | Вадим**
И работает ли обход через zapret2?

---

**2026-03-20T16:35:20 | Routerich**
как минимум подождать или толкнуть к перезапуску zapret

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

**2026-03-20T17:48:19 | Bullet for my valentine Poison**
Zapret2.😊

---

**2026-03-20T18:11:53 | Slay**
Добрый день!
Можете пожалуйста подсказать, у меня не отображается Zapret2 в службах потому что я не обновил прошивку?

---

**2026-03-20T18:16:25 | Dmitrii Burenin**
Система-Пакеты. Обновить список. Zapret2 в фильтр

---

**2026-03-20T18:24:58 | Роман**
Вот когда будет "комбайн" с полной интеграцией, тогда можно и ZeroZapret2.0 устанавливать, а не отдельно.

---

**2026-03-20T18:59:24 | Степан Павлюченков**
Добрый вечер)
Поставил zapret2, всё работает на ПК
На телефоне - через родное приложение видео грузит, а вот ReVanced почему то перестал работать.
Использую скрипт из закрепа.
Может сталкивался кто?

---

**2026-03-20T21:06:13 | Mstislav**
Спасибо, по ссылке была инструкция: Итак пошаговый мануал для владельцев Routerich, как завести Zeroblock+Zapret2 на дефолтных настройках.
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки"и ждем, закрываем появившуюся табличку нажав на кнопку "ОК".
3. Качаем два файла (zeroblock_*** и luci-app-***) из закрепа темы "Zeroblock" и сохраняем в папку на рабочем столе.
4. Возвращаемся в разделы Система-пакеты и жмем на кнопку "Загрузить пакет". И по очереди ставим скачанные пакеты: Zeroblock_*** а затем luci-app***.(Табличку с надписью Error игнорируем)

---

**2026-03-20T23:05:58 | Arsen S**
Прогнал скрипт №5, обновил Podkop до версии 0.7.14. Во вкладке Podkop валятся ошибки. Работает только ютуб, но я ранее настраивал Zapret2 возможно это причина. Помогите пожалуйста, что не так.

---

**2026-03-20T23:31:39 | Routerich**
Посмотреть логи нажмите и пришлите вывод оттуда
Попробуйте остановить zapret/zapret2

---

**2026-03-20T23:41:13 | Routerich**
Полная, детальная инструкция к zapret2_finder(новый blockcheck2) в zapret2 от Routerich. upd 23.41 17.04.2026

---

**2026-03-20T23:44:33 | Routerich**
потому что 👆. Вот вам полная, детальная инструкция к несуществующему компоненту zapret2.

---

**2026-03-21T00:32:55 | Alex Korshun**
Я его рот бомбил... После обновления до r56 перестала проходить команда opkg update. Ссылалась на ошибку синтаксиса что-то там... 
Пришлось делать полный сброс и все по новой. Понимаю, будь это мои руки из....., но кроме zapret2, zb и asu ничего более на роутере не было установлено🐒

---

**2026-03-21T00:36:14 | Dmitry**
Только получил ещё 1 роутер….
Подскажите что на данный момент лучше ставить zapret2, zeroblock или старый добрый интернет без границ?

---

**2026-03-21T11:14:50 | Константин**
Подскажите пожалуйста, стоит zeroblock и zapret, все вроде работает за исключением wats app 🤔

---

**2026-03-21T12:20:39 | Alex Korshun**
Справедливое замечание, на самом деле. 
Сегодня глюк словил с обновлением пакетов через LuCi. Вообще ни в какую не хотела исполняться команда, всё ссылалась на ошибку JSON, что-то там, хотя через терминал было норм... 
Пробовал и в инкогнито, и через другой браузер, даже со смартфона зашел в морду — и тоже ничего. Около часа так долбился. 
Что стало причиной, я так и не выяснил, просто сделал сброс. 
Притом что на роутере, кроме ASU, zapret2 и zb, больше ничего не установлено.

---

**2026-03-21T13:34:51 | Роман**
sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh)
Это в терминал, запрет 2 отключить с автозапуском.

---

**2026-03-21T14:55:33 | Bullet for my valentine Poison**
Итак пошаговый мануал для владельцев Routerich, как завести Zeroblock+Zapret2 на дефолтных настройках.
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки"и ждем, закрываем появившуюся табличку нажав на кнопку "ОК".
3. Качаем два файла (zeroblock_*** и luci-app-***) из закрепа темы "Zeroblock" и сохраняем в папку на рабочем столе.
4. Возвращаемся в разделы Система-пакеты и жмем на кнопку "Загрузить пакет". И по очереди ставим скачанные пакеты: Zeroblock_*** а затем luci-app***.(Табличку с надписью Error игнорируем)
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4,6,7. Жмем по очереди на кнопки: сохранить и применить.(Если вдруг 6 и 7 пункт не активны, проверьте в разделе настройки пункт "Версия API", должна стоять V2)
7. Далее ждем примерно 5 минут, очищаем кэш браузера и обновляем страницу. Пока в разделе Службы не появится пункт "Zapret2".
8. Возвращаемся в Zeroblock, открываем вкладку Автонастройка и убираем галки с 6 и 7 пункта.(Автозагрузка) Иначе мы не сможем вносить изменения в секциях со списками. Сохранить, применить.
9. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
10. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
11. Проверяете работу Youtube на всех устройствах. (так же желательно в браузерах отключить функцию "Частный/безопасный DNS")

---

**2026-03-21T17:39:03 | Anatoly К**
Показано 1-7 из 7
»
Имя пакета Версия Размер (.ipk) Описание  
zapret 72.20251122 159.81 KiB zapret 
Установить…
zapret-ip2net 72.20251122 5.37 KiB ip2net 
Установить…
zapret-mdig 72.20251122 6.35 KiB mdig 
Установить…
zapret-tpws 72.20251122 48.29 KiB tpws 
Установить…
zapret2 0.9.4.3-r7 502.58 KiB zapret2 is a DPI bypass tool using nfqws2.… 
Установлено
luci-app-zapret 72.20251122-r1 13.42 KiB LuCI support for zapret 
Установить…
luci-app-zapret2 0.9.4.3-r7 29.06 KiB Web interface for managing zapret2 DPI bypass tool.…что за пакеты запрет ???

---

**2026-03-21T17:40:26 | Роман**
Запрет. Zapret. Zapret2. Пакеты для установки в роутер.

---

**2026-03-21T17:41:01 | Anatoly К**
zapret-ip2net 72.20251122 5.37 KiB ip2net 
Установить…
zapret-mdig 72.20251122 6.35 KiB mdig 
Установить…
zapret-tpws

---

**2026-03-21T17:42:15 | Anatoly К**
zapret-ip2net 72.20251122 5.37 KiB ip2net 
Установить…
zapret-mdig 72.20251122 6.35 KiB mdig 
Установить…
zapret-tpws

---

**2026-03-21T17:44:02 | Anatoly К**
zapret  zapret2

---

**2026-03-21T18:01:24 | Denis**
Здравствуйте! планируется ли скрипт с zapret2?

---

**2026-03-21T18:41:04 | MidnightCocoa**
Анализ запущен: 2026-03-21 18:39:09
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
  Facebook IP:  157.240.205.35 | YouTube IP:  173.194.221.190

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.68 MB / ↑0.21 MB
  Пинг (ya.ru via awg10): 56.796 / 59.988 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock zapret2 opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock              awg10 (vpn): anime,art,discord,games,googleplay,messengers,meta,music,news,porn,repo,shop,socials,tools,torrent,video,cdn_akamai,cdn_aws,cdn_azure,cdn_bunny,cdn_cdn77,!_cdn_cloudflare,cdn_digitalocean,cdn_fastly,cdn_gcore,cdn_google,cdn_hetzner,cdn_linode,cdn_oracle,cdn_ovh,cdn_scaleway,cdn_selectel,cdn_vultr,cdn_yandex
  zeroblock          opera (prx out): ai,block,geoblock
  Версия zeroblock: 0.7.1-r56
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.32 | RAM: 24% | NAND: 30% занято / 42.8M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

root@RouteRich:~#

---

**2026-03-21T19:51:42 | Alexey**
Всем привет. Поясните плиз. Разве провайдер не видит, когда юзер с помощью zapret2 уходит от блокировки? Если видит, то это значит надо чекать списки экстремистских ресурсов, чтобы не попасть случайно на такой?

---

**2026-03-21T20:39:54 | Routerich**
имейте уважение не показывать огрызки окон, вы в одну стратегию напихали несколько. это не запрещается, но если вы так делаете, вы должны понимать что вы делаете, список волшебным образом на вашу писанину не натянется. посмотрите либо /etc/config/zapret2 либо /opt/zapret2/config и поймите что ваши --new стратегии работают по всему трафику

---

**2026-03-21T21:08:42 | Vlad Goo**
Всем привет!
Подскажите пожалуйста, настроил VLESS через подкоп, ютуб работает, тг и вотсап - нет, полный ноль. Я пробовал вручную настроить маршруты для тг, убирать zapret/zapret2, ничего не помогает.. 
Диагностику прикладываю

---

**2026-03-21T21:50:05 | V I T Λ L Y**
Камрады, проблема с Apple music остается, на роутере не хочет музыку грузить. Переключаюсь на мобильную - сразу включает. Стоит zeroblock и zapret2...может кто сталкивался?

---

**2026-03-21T21:52:54 | Routerich**
Здравствуйте.
А если остановить zeroblock, zapret грузится начинает?

---

**2026-03-21T21:54:22 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.2-r3:
  Изменения:
  - Two-stage-sub — если на роутере установлена Opera Proxy (GeoBlock), подписки автоматически загружаются через неё. Это решает проблему с недоступными URL подписок на заблокированных сайтах.
  - HWID — при загрузке подписок автоматически отправляется заголовок x-hwid (MD5 от MAC-адреса). Необходимо для панелей управления (Remnawave, Marzban), которые ограничивают количество устройств.
  - Фильтрация по тегам — новая per-section опция subscription_ignore_tags. После первого запуска ZeroBlock извлекает теги (страны/префиксы) из имён прокси. В LuCI появляется MultiValue список, где можно выбрать какие теги игнорировать (например RU, 未知). Выбранные прокси отбрасываются при следующем запуске.
  - Per-section User-Agent — каждая секция с подпиской может иметь свой User-Agent. Глобальная опция убрана.
  - Таймаут загрузки — новая UCI опция subscription_timeout (по умолчанию 30 сек, диапазон 5-120 сек). Добавляется автоматически при обновлении пакета через postinst.
  - Параллельный DNS resolve — endpoint'ы прокси-серверов из подписок теперь резолвятся параллельно через pthreads. 81 домен за 5 секунд вместо ~2 минут.

  LuCI
  - Табы в модальном окне секции — параметры сгруппированы по 4 вкладкам: General, DNS, Lists, Advanced. Parental Control отображается в General при выборе типа Block.
  - Табы в Show Config — sing-box конфигурация разбита на вкладки: Log, Experimental, DNS, Inbounds, Outbounds, Route, Custom. Каждая вкладка показывает отдельный файл. Copy/Download работают с полным конфигом.
  - Маскировка данных — password, uuid, private_key, secret, short_id маскируются в Show Config (первые 4 символа + ****).

  Custom Config
  - Префикс not-add — файлы с именем not-add-*.json в директории custom config копируются в sing-box, но их inbound теги не добавляются автоматически в route rules. Пользователь сам управляет маршрутизацией.

  Исправления
  - Fix: xtls-rprx-vision-udp443 flow отфильтровывается (не поддерживается sing-box)
  - Fix: desync_bypass MultiValue — при снятии всех выборов корректно очищает секции
  - Health monitor: DPI check выполняется только при включённой автозагрузке стратегий zapret2
#ZeroBlock

---

**2026-03-21T23:42:27 | Борис**
Через утилиту service разработчик не все команды правильно обозначил, поэтому может что-то неправильно отображаться. Можно в консоли написать ps | grep zapret или ps | grep nfqws и там будет точно показывать, работает он или нет

---

**2026-03-21T23:56:34 | Борис**
Если читать буквально то, что написано, то у тебя на роутере установлено 10 запретов. Назовём их условно zapret, zapret2, zapret3 и т.д. Мы выяснили, что программа zapret в каком бы то ни было виде не отображается в процессах через ps. Под капотом она обращается к другой программе - nfqws. Это значит, что этот запущенный nfqws в одном экземпляре прикреплён ко всем 10 запретам (даже к zapret10). Получается одним выстрелом можно kill 10 зайцев. Но лучше все-таки один запрет в системе оставить

---

**2026-03-22T01:07:50 | A̴͂ ̖͔͎͍͔̮̌̾̈̓̇̅͗̓̒̌̉̀̕͠͝ ̧̙͕̬̦̩̞ͅͅv̸̡̡̬̬͔͕̰̖̻̄́̎̽ͅř̸̆̓͛̉̋̈́̔̔̔͂**
Уважаемые коллеги!

Использую роутер Routerich с установленными Zeroblock и Zapret2.

Столкнулся со следующей проблемой: на консоли PS5 не скачиваются обновления игр и системного ПО (консоль подключена по wifi). 

Проблема сохраняется:

На дефолтных настройках;
При добавлении IP-адреса консоли в секцию с прокси и WG в список «Исключённые из секции IP-адреса»;
При добавлении того же IP в глобальные исключения («исключённые IP») в настройках Zeroblock;
При создании новой секции типа VPN с сетевым интерфейсом eth1 (WAN) и записью IP в поле "Полная маршрутизация";
При отключении обеих стандартных секций;
Zapret2 также полностью отключался — без изменений.

В то же время при использовании роутера Xiaomi 4A со стандартными настройками обновления на PS5 скачиваются без проблем.

Что я делаю не так?

Заранее благодарю за помощь.

---

**2026-03-22T01:20:55 | A̴͂ ̖͔͎͍͔̮̌̾̈̓̇̅͗̓̒̌̉̀̕͠͝ ̧̙͕̬̦̩̞ͅͅv̸̡̡̬̬͔͕̰̖̻̄́̎̽ͅř̸̆̓͛̉̋̈́̔̔̔͂**
Да, на xiaomi качает без проблем

Пробовал разные комбинации настроек на случай если это баг

Пробовал отключить Zapret, Zeroblock - безрезультатно

FakeIP тоже отключал в специальной секции eth0 WAN для консоли

Где сохраняется этот отчет test_config_script_nightly ? В root файла analyzer.log нет

---

**2026-03-22T01:30:39 | A̴͂ ̖͔͎͍͔̮̌̾̈̓̇̅͗̓̒̌̉̀̕͠͝ ̧̙͕̬̦̩̞ͅͅv̸̡̡̬̬͔͕̰̖̻̄́̎̽ͅř̸̆̓͛̉̋̈́̔̔̔͂**
Анализ запущен: 2026-03-22 01:28:33
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.195 | YouTube IP:  64.233.164.190

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.38 MB
  Пинг (ya.ru via awg10): Ожидайте, идет замер (10 пакетов)...
  Пинг (ya.ru via awg10): 14.162 / 14.565 ms (8 из 10 потеряно)
  Программы в автозапуске: zeroblock zapret2 opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:  127.0.0.1
    Address: 127.0.0.1:53
    Name: youtube.com
    Address: 74.125.205.136
    Name: youtube.com
    Address: 74.125.205.91
    Name: youtube.com
    Address: 74.125.205.93
    Name: youtube.com
    Address: 74.125.205.190
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock              awg10 (vpn): anime,art,googleplay,messengers,news,socials,torrent
  zeroblock          opera (prx out): ai,meta
  Секция в режиме catch-all: tests
  Полностью маршрутизированные IP-адреса включены!
  zeroblock.tests.fully_routed_ips='192.168.1.222'
  Версия zeroblock: 0.7.1-r56
  zeroblock DNS/Bootstrap DNS: (doh) 1.1.1.1 / 8.8.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.39 | RAM: 27% | NAND: 50% занято / 34.0M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1
  !!!_WatchDoc установлен

---

**2026-03-22T07:56:36 | ВПН НА ТЕЛЕВИЗОР ФИЛИПС**
Привет всем, может ли быть разное поведение одной и той же стратегии на линухе и на винде?
Есть линух, физ устройство, к нему как к шлюзу подключены другие, раньше на втором запрете была страта + маскарад на основе 1 фейка+блоба, все работало, переустановил линух.. "все не работает"...
Такая страта первого запрета на винде открывает все:
--filter-udp=443 --hostlist="%LISTS%list-general.txt" --dpi-desync=fake --dpi-desync-repeats=11 --dpi-desync-fake-quic="%BIN%quic_initial_www_google_com.bin" --new ^
--filter-tcp=80,443 --hostlist="%LISTS%list-general.txt" --dpi-desync=fake --dpi-desync-fooling=ts --dpi-desync-repeats=8
Такая страта второго запрета на линухе нихрена не делает:
NFQWS2_OPT="
    --debug=@/opt/zapret2/zapret.log
    --blob=tls_google:@/opt/zapret2/blobs/tls_google.bin

    $USER_LIST --filter-tcp=443,80  --filter-l7=tls --payload=tls_client_hello --lua-desync=fake:blob=tls_google:tcp_ts=-1000:repeats=11
    $USER_LIST --filter-udp=443 --filter-l7=quic --payload=quic_initial --lua-desync=fake:repeats=8
"
Есть у кого варианты почему может быть разное поведение? И я не думаю что проблема в самой стратегии, т.к суть для пробития одна - фейк + блоб, если к квику добавить блоб ничего не изменяется
Может ли быть дело в bbr? forwarding? 
И главное по дебагу вроде как дурилка к сайтам применяется, на она просто не работает...
На винде можно и до такого стратегию упростить:
--filter-udp=443 --dpi-desync=fake --dpi-desync-repeats=4 --new ^
--filter-tcp=80,443 --dpi-desync=fake --dpi-desync-fooling=ts --dpi-desync-repeats=4

---

**2026-03-22T08:07:18 | Routerich**
Вам сюда 
https://github.com/bol-van/zapret2

---

**2026-03-22T08:53:22 | ВПН НА ТЕЛЕВИЗОР ФИЛИПС**
Вроде как, тут используется моя стратегия что была раннее + перехват через tproxy (вместе с михомо)
packet: id=14 len=552 mark=20000190 ifin=(0) ifout=eth0(2)
IP4: 192.168.1.5 => 74.125.131.198 proto=tcp ttl=64 sport=36604 dport=443 flags=AP seq=2021405631 ack_seq=868322246
TCP: len=500 : 87 5E 9B CB 9C 34 28 DF 5A 21 29 6D 42 FD 00 04 29 D9 97 2C 12 CA D0 97 27 D7 FF FC AC C9 2E E4 ... : .^...4(.Z!)mB...)..,....'....... ...
client mode desync profile/ipcache search target ip=74.125.131.198 port=443
using cached desync profile 0 (no_action)
reassemble : feeding data payload size=500. now we have 1900/1900
TLS client hello is FULL
TLS record layer version : TLS 1.0
TLS handshake version : TLS 1.2
TLS supported versions ext : TLS 1.3
TLS supported versions ext : TLS 1.2
TLS ALPN ext : h2
TLS ALPN ext : http/1.1
TLS ECH ext : present
DELAY desync until reasm is complete (#2)
REPLAYING delayed packet #1 offset 0
REPLAY IP4: 192.168.1.5 => 74.125.131.198 proto=tcp ttl=64 sport=36604 dport=443 flags=A seq=2021404231 ack_seq=868322246
TCP: len=1400 : 16 03 01 07 67 01 00 07 63 03 03 B4 60 59 A8 12 F3 7E D6 D3 1F B1 E7 67 1A 1D 97 32 0D E0 5B 2F ... : ....g...c...`Y...~.....g...2..[/ ...
client mode desync profile/ipcache search target ip=74.125.131.198 port=443
using cached desync profile 0 (no_action)
TLS client hello is FULL
TLS record layer version : TLS 1.0
TLS handshake version : TLS 1.2
TLS supported versions ext : TLS 1.3
TLS supported versions ext : TLS 1.2
TLS ALPN ext : h2
TLS ALPN ext : http/1.1
TLS ECH ext : present
hostname: www.youtube.com
discovered l7 protocol
discovered hostname
desync profile search for tcp ip=74.125.131.198 port=443 icmp=255:255 l7proto=tls ssid='' hostname='www.youtube.com'
* hostlist check for profile 1 (noname)
[/opt/zapret2/lists/user.list] include hostlist check for www.youtube.com : negative
hostlist check for youtube.com : positive
desync profile 1 (noname) matches
desync profile changed by revealed l7 protocol or hostname !
dpi desync src=192.168.1.5:36604 dst=74.125.131.198:443 track_direction=out fixed_direction=out connection_proto=tls payload_type=tls_client_hello
* lua 'fake_1_1' : out pos a0 n3 in range a0-n3
* lua 'fake_1_1' : payload_type 'tls_client_hello' satisfy filter
* lua 'fake_1_1' : desync
instance cutoff for 'fake_1_1' in=1 out=0
LUA: fake: 16 03 01 02 3F 01 00 02 3F 03 03 53 1B 5B 3F 35 3F 71 3F 3F 3F 3F 3C 3F 2B 03 1B 3F 3F 3F 3F 7D ... ....?...?..S.[?5?q????<?+..????} ...
rawsend_dissect repeats=1 size=740 badsum=0 ifout=eth0 fwmark=60000190
* lua 'http_methodeol_1_2' : out pos a0 n3 in range a0-n3
* lua 'http_methodeol_1_2' : payload_type 'tls_client_hello' does not satisfy filter
SENDING delayed packet #1 unmodified
REPLAYING delayed packet #2 offset 1400
REPLAY IP4: 192.168.1.5 => 74.125.131.198 proto=tcp ttl=64 sport=36604 dport=443 flags=AP seq=2021405631 ack_seq=868322246
TCP: len=500 : 87 5E 9B CB 9C 34 28 DF 5A 21 29 6D 42 FD 00 04 29 D9 97 2C 12 CA D0 97 27 D7 FF FC AC C9 2E E4 ... : .^...4(.Z!)mB...)..,....'....... ...
client mode desync profile/ipcache search target ip=74.125.131.198 port=443
using cached desync profile 1 (noname)
TLS client hello is FULL
TLS record layer version : TLS 1.0
TLS handshake version : TLS 1.2
TLS supported versions ext : TLS 1.3
TLS supported versions ext : TLS 1.2
TLS ALPN ext : h2
TLS ALPN ext : http/1.1
TLS ECH ext : present
hostname: www.youtube.com
dpi desync src=192.168.1.5:36604 dst=74.125.131.198:443 track_direction=out fixed_direction=out connection_proto=tls payload_type=tls_client_hello
* lua 'fake_1_1' : out pos a0 n4 overflow 0 0 is beyond range a0-n3 (ctrack enabled)
* lua 'http_methodeol_1_2' : out pos a0 n4 overflow 0 0 is beyond range a0-n3 (ctrack enabled)
all out desync functions reached cutoff condition
SENDING delayed packet #2 unmodified
reassemble session finished
packet: id=14 drop

---

**2026-03-22T09:34:25 | ВПН НА ТЕЛЕВИЗОР ФИЛИПС**
Это может ломать как-то? Я хрен знает
#!/usr/sbin/nft -f

table inet zapret2_masquerade {
        chain postrouting_nat {
                type nat hook postrouting priority srcnat; policy accept;
                oifname "eth0" masquerade
        }
}

---

**2026-03-22T09:59:44 | ВПН НА ТЕЛЕВИЗОР ФИЛИПС**
Я забыл шлюз на линух поставить) Но оно конечно, не помогло, т.к я и от лица малинки сайты чекал
admin@raspberrypi:/opt/zapret2 $ sudo tcpdump -i eth0 -nn -vvv 'tcp port 80 or tcp port 443'
tcpdump: listening on eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
09:57:17.279986 IP (tos 0x0, ttl 128, id 47724, offset 0, flags [DF], proto TCP (6), length 40)
    192.168.1.10.58870 > 20.54.232.160.443: Flags [.], cksum 0x6d43 (correct), seq 144558303, ack 237942955, win 1024, length 0
09:57:17.280014 IP (tos 0x0, ttl 127, id 47724, offset 0, flags [DF], proto TCP (6), length 40)
    192.168.1.10.58870 > 20.54.232.160.443: Flags [.], cksum 0x6d43 (correct), seq 0, ack 1, win 1024, length 0
09:57:17.466954 IP (tos 0x0, ttl 128, id 11603, offset 0, flags [DF], proto TCP (6), length 461)
    192.168.1.10.58957 > 91.105.192.100.443: Flags [P.], cksum 0x7538 (correct), seq 671086406:671086815, ack 770438050, win 1025, options [nop,nop,TS val 46595696 ecr 1503591263], length 409
09:57:17.466988 IP (tos 0x0, ttl 127, id 11603, offset 0, flags [DF], proto TCP (6), length 461)
    192.168.1.10.58957 > 91.105.192.100.443: Flags [P.], cksum 0x7538 (correct), seq 0:409, ack 1, win 1025, options [nop,nop,TS val 46595696 ecr 1503591263], length 409
09:57:17.517143 IP (tos 0x0, ttl 64, id 55483, offset 0, flags [DF], proto TCP (6), length 1440)
    192.168.1.5.53434 > 104.16.249.249.443: Flags [.], cksum 0xd866 (correct), seq 1553711465:1553712853, ack 562771646, win 502, options [nop,nop,TS val 2618241732 ecr 1343882748], length 1388
09:57:17.517169 IP (tos 0x0, ttl 64, id 39965, offset 0, flags [DF], proto TCP (6), length 1440)
    192.168.1.5.37954 > 104.16.249.249.443: Flags [.], cksum 0xb432 (correct), seq 1054744181:1054745569, ack 950521067, win 502, options [nop,nop,TS val 2618241732 ecr 1279889869], length 1388
09:57:17.538785 IP (tos 0x0, ttl 128, id 29744, offset 0, flags [DF], proto TCP (6), length 41)
    192.168.1.10.58937 > 173.194.222.198.443: Flags [.], cksum 0x902f (correct), seq 2031403503:2031403504, ack 4244352367, win 1028, length 1
09:57:17.538804 IP (tos 0x0, ttl 127, id 29744, offset 0, flags [DF], proto TCP (6), length 41)
    192.168.1.10.58937 > 173.194.222.198.443: Flags [.], cksum 0x902f (correct), seq 0:1, ack 1, win 1028, length 1
09:57:18.170749 IP (tos 0x0, ttl 128, id 28280, offset 0, flags [DF], proto TCP (6), length 1456)
    192.168.1.10.58832 > 45.155.204.190.443: Flags [.], cksum 0x3a54 (correct), seq 2192502884:2192504288, ack 3030512868, win 1021, options [nop,nop,TS val 46596400 ecr 1773419627], length 1404
09:57:18.170750 IP (tos 0x0, ttl 128, id 28281, offset 0, flags [DF], proto TCP (6), length 1456)
    192.168.1.10.58832 > 45.155.204.190.443: Flags [.], cksum 0x9c28 (correct), seq 1404:2808, ack 1, win 1021, options [nop,nop,TS val 46596400 ecr 1773419627], length 1404
Ну вот как-то так выглядит, такое чувство что через сам роутер ничего не ходит..

---

**2026-03-22T10:09:20 | Bullet for my valentine Poison**
https://ntc.party/t/zapret2-%D0%BE%D0%B1%D1%81%D1%83%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5/21161 я думаю вам сюда.

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

**2026-03-22T11:33:00 | Bullet for my valentine Poison**
он в теме Zapret2. И работает через Zapret1

---

**2026-03-22T11:36:50 | Владимир Ионов**
Анализ запущен: 2026-03-22 11:35:20
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
  Facebook IP:  198.18.0.147 | YouTube IP:  142.250.150.136

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.70 MB / ↑0.35 MB
  Пинг (ya.ru via awg10): 78.636 / 81.203 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock zapret2 opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock              awg10 (vpn): anime,discord,googleplay,messengers,meta,news,porn,socials,video
  zeroblock          opera (prx out): geoblock,ai
  Версия zeroblock: 0.7.2-r4
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.132.2 (Прошивка: 24.10.5)
  CPU: 0.26 | RAM: 23% | NAND: 46% занято / 36.7M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

root@RouteRich:~#

---

**2026-03-22T11:36:57 | Anna Bagler**
Заходите на страницу zapret2 в службах отключайте автозапуск для него и останавливайте службу. Знакомьтесь с меню, которое перед вами. Полезно.

---

**2026-03-22T11:44:11 | Teleghost**
Мне наоборот надо ОТКЛЮЧИТЬ прокси до любых попыток применения альтернативных путей. Цель - быть уверенным, что применение podkop, zapret и им подобных никогда не будет влиять на это список сайтов.

 У меня нет никакого vless, хотя интересует возможность сделать такой канал _без_ vps и веб-серверов между двумя частными квартирами.

---

**2026-03-22T11:59:41 | S V**
Анализ запущен: 2026-03-22 09:13:10 Лог сохраняется в: /root/analyzer.log -------------------------------------------------------------- Попытка обновления списка пакетов: (1/2) Списки обновлены успешно Installing wget-ssl (1.24.5-r1) to root... Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk Package curl (8.12.1-r1) installed in root is up to date. Configuring wget-ssl. = ПРОВЕРКА DNS (Прошивка: 24.10.5): DNS Server: 127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359 Facebook IP: 198.18.4.15 | YouTube IP: 108.177.14.93 = ИНТЕРФЕЙС awg10 (ДЕТАЛИ): Статус : UP (ON) ↓10.69 MB / ↑0.21 MB Пинг (ya.ru via awg10): 10.882 / 12.208 ms (0 из 10 потеряно) Программы в автозапуске: zeroblock zapret2 opera-proxy = ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM): OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK) awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3] awg10 (IPv6) : ОФЛАЙН Запускаем остановленные службы, ожидайте... = СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ): zeroblock | RUNNING | РАЗРЕШЁН sing-box | RUNNING (MANAGED BY ZB) | ОТКЛ zapret2 | RUNNING | РАЗРЕШЁН opera-proxy | RUNNING | РАЗРЕШЁН = ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ: zeroblock awg10 (vpn): anime,discord,googleplay,messengers,meta,news,porn,socials,video zeroblock opera (prx out): ai,geoblock Версия zeroblock: 0.7.1-r53 zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8 = СИСТЕМНЫЕ РЕСУРСЫ: LAN IP: 192.168.1.1 (Прошивка: 24.10.5) CPU: 0.30 | RAM: 23% | NAND: 50% занято / 34.1M доступно # ZeroBlock Monitor 0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1 # ZeroBlock Lists Update 0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1 root@RouteRich:~#

---

**2026-03-22T13:25:12 | Marat 🌊🌊 Wave**
При установке скрипта выдало zapret not work. Как проверить, zapret функционирует или нет?

---

**2026-03-22T13:47:10 | Alex Korshun**
Как будто что-то из установленного переехало в системное. 
Раньше zapret2+zeroblock занимали ±22мб памяти.

---

**2026-03-22T14:08:52 | Anna Bagler**
Анблок отключайте. Ставьте связку zeroblock + zapret2.

---

**2026-03-22T14:12:25 | Wenzel Perminov**
сталкиваюсь с такой фигней уже не первый раз, Zapret2 сегодня обновил и Smarttube( все не использующие quic альтернативные клиенты так же) нормально буферит, а через пару дней станет буферить хуже  и смотреть станет невозможно. Такое поведение есть у Zapret2 и кажется раньше какая-то деградация есть у youtubeunblock. как с таким бороться настройками, так как стратегия работает, а буфер происходит реже чем надо

---

**2026-03-22T14:15:45 | Stepan**
Добрый день, начал настраивать по этой инструкции, дошел до 7 пункта, за 30 минут zapret2 в службах так и не появился, но при этом все сервисы вроде как работают. Можете пожалуйста объяснить, зачем нужен еще и zapret2? И чем чревато оставить все как есть, то есть маршрутизацию чисто через zeroblock?

---

**2026-03-22T14:17:41 | Anna Bagler**
Обновлять прошивку до актуальной и запускать скрипт ещё раз или zeroblock + zapret2.

---

**2026-03-22T15:27:22 | Дмитрий Григорьев**
У кого то дискорд вообще пашет со вторым запретом, или это общая трабла, что он не в какую не запускается
Ставил по инструкции ZB + Zapret2 (Настроил ZB выкинул из список Discord и YouTube)
YouTube пашет нормально, взял отсюда стратегию
А вот Дискорд никак, через поиск стратегий не выходит, discord.com не пробиваемый) либо я мало жду

---

**2026-03-22T16:11:58 | Anna Bagler**
В теме zapret2 найдите списки для discord.

---

**2026-03-22T16:59:48 | Anna Bagler**
Если у вас YouTube пущен через zapret2, то пробуйте другую стратегию для него. Например, в закрепах темы Zapret2 есть.

---

**2026-03-22T17:04:18 | Виталий**
Нет zapret2 не устанавливал 🤷‍♂

---

**2026-03-22T18:13:14 | Dmitry**
Поставил zeroblock. Я правильно понимаю что свои домены надо вносить в zapret2 - списки - user ?

---

**2026-03-22T18:16:11 | Dmitry**
Логично..) в awg10?

А zapret2 тогда как резерв или для каких целей?

---

**2026-03-22T19:10:39 | Aleksei P**
А уже есть готовый скрипт по установке и настройке zapret 2?

---

**2026-03-22T19:26:17 | Безнадёжный Ватник**
тогда подойдёт просто zapret

---

**2026-03-22T20:27:55 | ARTEM**
Хочу сделать новую стратегию через zapret2 finder , так как что в шапке стратегия что в rr-youtube, когда захожу на ютуб долго прогружается превьюшки а через awg в zeroblock пускать не хочу потому что 4к лагать начинает
--
Вот щяс вставил домены ютуба и убрал sni prob и все в blocked упали
Как правильно запустить finder чтобы найти стратегию только для ютуба ?

---

**2026-03-22T22:09:58 | Kiss_My_Axe**
  zapret          | RUNNING                        | РАЗРЕШЁН
  zapret2         | RUNNING                        | РАЗРЕШЁН
Остановите и отключите автозагрузку обоих запретов. Ютуб и заработает.

---

**2026-03-22T22:27:03 | K**
Прошу совета. 

Стоит ZB + Zapret2.

На пк, телефоне, телевизоре YT отлично работает. 

Но на планшете Ipad ни в какую. Какие действия предпринять?

---

**2026-03-22T22:59:49 | 🆂🅷🅾🅳🅸🅼🅰🆂🆃🅴🆁**
дело в том что она и не работала на zeroblock+zapret с чистого роутера. Но если скрипт номер 5 поверх вкорячить то работает. FakeIP постоянно красный крестих без подкопа

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

**2026-03-23T01:04:10 | Дмитрий Григорьев**
Пробовал в Zapret2 выключить скрипты обхода дискорда, что бы он никак на него не влиял, та же шляпа.
При чём все остальное прекрасно работает, проблема лишь с ним, Packet Loss проверял в отладке самого дискорда

---

**2026-03-23T01:06:58 | Bullet for my valentine Poison**
Там Zapret2 обновился. Добавили поиск стратегий, попробуйте поискать для discord.com

---

**2026-03-23T01:10:51 | Дмитрий Григорьев**
Такой вкладки не вижу, скрин скинул, как у меня это выглядит
Zapret ставил через автонастройку ZB

---

**2026-03-23T06:45:03 | Alex Korshun**
В общих настройках zapret2 не забудьте активировать Blob "blob_tls_clienthello_google_com_tlsrec" чтобы заработало.

---

**2026-03-23T07:53:42 | Vladimir Shubin**
Доброго времени суток. Что надо сделать, чтобы заработал инстаграмм? (на кинетике через nfqws работает). 
Так же на роутере установлен Zapret2.

---

**2026-03-23T09:56:23 | Руслан**
Здравствуйте! Скажите, а нужно ли после установки на чистый RR ZeroBlock+Zapret2 скрипт №5 или Бета?

---

**2026-03-23T11:08:34 | Anna Bagler**
Zeroblock+zapret2 лучше. Подкоп скриптом, если с навыками все плохо.
https://t.me/routerich/394153/520562

---

**2026-03-23T11:15:27 | Anna Bagler**
Разные вещи. Zeroblock - точечная маршрутизация. Zapret - дурилка, как написали выше.

---

**2026-03-23T11:43:14 | Anna Bagler**
Обновите сам zapret2. Пробуйте подобрать стратегию для zapret2.

---

**2026-03-23T15:15:06 | Anna Bagler**
Установка через Система - Пакеты. Кнопочка Обновить списки, потом в поле фильтра zapret2 и ok.

---

**2026-03-23T15:46:17 | Andrey**
Приветствую. Нужен совет по общей стратегии настройки роутера. Я в этой теме новичок, поэтому хочу понять какой подход нормальный и в какой последовательности лучше всё настраивать. Насколько я понимаю, возможны разные варианты: например, установить Podkop, настроить списки, затем дополнительно использовать zapret2, Zeroblock и др. Но мне не очень ясно, что действительно нужно ставить вместе, что дублирует друг друга, а с чего лучше начать чтобы не усложнить себе жизнь с самого начала. Понимаю, что многое уже обсуждалось, но буду благодарен, если подскажете именно общую логику действий типа с чего лучше начинать, что ставить в первую очередь и какой сейчас рабочий вариант лучше всего

---

**2026-03-23T15:48:19 | Anna Bagler**
Zeroblock и Podkop - конфликт. Zeroblock + Zapret2.

---

**2026-03-23T15:59:50 | Andrey**
Хорошо спасибо. Еще вопрос про Zapret2-finder, я так понимаю, что ее надо поставить в дополнение, чтобы Zapret2 лучше подбирал стратегию обхода DPI или она не обязательна?

---

**2026-03-23T16:03:03 | Anna Bagler**
Разработчик zeroblock и zapret2 с плюшками для РР.

---

**2026-03-23T16:27:16 | Grigory**
Что сейчас лучше и проще настроить? zeroblock, zapret2 или podkop?

---

**2026-03-23T16:33:13 | Anna Bagler**
Zeroblock+Zapret2.

---

**2026-03-23T16:41:34 | Alex_Jester**
Чтобы понять, что это такое нужно лезть в pdf файл. А с ходу даже я не понял. Думал, что это что-то уровня zapret и не более

---

**2026-03-23T16:43:36 | Routerich**
система - пакеты в поиске zapret2 скриншот

---

**2026-03-23T17:28:59 | Роман**
Zeroblock + zapret2.
AI, Block, Geoblock, Porn, Torrent, Games, Messengers, Meta списки.
▾

---

**2026-03-23T17:38:59 | Anna Bagler**
Вы пробовали стратегию из закрепа темы Zapret2?

---

**2026-03-23T17:40:23 | Anna Bagler**
Есть великая стратегия от @BFMVPoison в теме Zapret2.

---

**2026-03-23T17:51:27 | Anna Bagler**
Вам тогда изучать полный мануал по zapret2 и идти в тему по нему.

---

**2026-03-23T18:58:39 | Serge**
Здравствуйте! AWG сервер поднял, работает. Как трафик отправлять через ZB и Zapret? Создать правило "Сервер" -> awg10?

---

**2026-03-23T19:29:42 | Anna Bagler**
Все должно работать, youtubeUnblock отключайте и останавливайте, zeroblock и zapret2 ставьте.

---

**2026-03-23T19:41:04 | Anna Bagler**
По умолчанию на РР только youtubeUnblock. Он может не работать с настройками по умолчанию. Пробуйте связку zeroblock+zapret2 или только zapret2 для YouTube. Анблок тогда удалить или остановить и отключить.

---

**2026-03-23T19:43:26 | Wenzel Perminov**
https://github.com/bol-van/zapret2/discussions/168   я создал может так мне помогут с моей проблемой когда Smarttube плохо буферит с zapret2

---

**2026-03-23T19:57:46 | Gomer Simpson**
MicroG или GmsCore и будет вам весь гуголь на хуавее. А Zapret1 попробуйте. В теме Интернет без границ поиском найдите АВТОКОНФИГУРАТОР.

---

**2026-03-23T20:17:56 | Vasa**
конечно. опенвпн же есть изкаропки в кинетике

https://github.com/GubernievS/AntiZapret-VPN

---

**2026-03-23T20:59:46 | Алексей Лобачев**
Подскажите, стоит ZB+Zapret2. Zapret остановлен, автозапуск отключен, но каждый день он включается сам по себе с дефолтными уставками. Что его может запускать? Автонастройки в ZB отключены, теряюсь

---

**2026-03-23T21:04:11 | Anna Bagler**
И? Либо сам пакет zapret2 не под ту luci.

---

**2026-03-23T21:15:03 | Борис**
Ну тебе все равно надо удалить zapret1, luci-app-zapret и поставить zapret2 и luci-app-zapret2. Потому что запрет2 будет конфликтовать с первым

---

**2026-03-23T21:16:15 | HiLLL**
в терминале запустите
opkg update
opkg remove zapret luci-app-zapret zapret2 luci-app-zapret2
opkg install zapret2 luci-app-zapret2

---

**2026-03-23T21:34:59 | Anna Bagler**
Да, luci для zapret2 ставьте уже.

---

**2026-03-23T21:40:14 | Anna Bagler**
Без luci для zapret2 в меню он не появится...

---

**2026-03-23T22:09:58 | DmitrO**
Можете подтвердить, правильно ли я решил проблему и стоит ли так делать в будущем?

Предусловия: ZeroBlock + Zapret2 (все настройки стандартные, кроме стратегии youtube Zapret2 в и включение ip6).
Проблема: Не работал Postman (клиент не грузится и сайт выдает ERR_CONNECTION_RESET), маркетплейс VSCode не грезил расширения.
Как решил:
- В Журнале URL-адресов собрал все домены, к которым обращались приложения.
- В ZeroBlock (секция opera) добавил их в Список пользовательских доменов.

Сейчас заметил, что сайт steamdb.info тоже выдает ERR_CONNECTION_RESET и надо понимать так же решать или нет.

---

**2026-03-23T22:30:19 | Дмитрий Григорьев**
Дам краткую и простую инструкцию как завёл у себя дискорд, возможно помогу другим.

1. Zapret2 -> Списки , Создаём свой список, Тип списка - Список Доменов, туда кидаем свои домены, я след сообщением прикреплю свой список, взятый из general Zapret1 от Flowseal.
2. Zapret2 -> Настройки -> Стратегии , Создаешь новую либо редактируешь Default, Вставляешь свою стратегию, можешь попробовать взять как у меня, спасибо BFMVPoison'у. След сообщением прикреплю
3. Сохранить И Применить, проверяй работает ли, если нет ищи стратегию в этой теме либо через Вкладку в Zapret "Поиск Стратегий" вбив туда discord.com и запустив тест(подробно как искать было расписано выше в теме).

---

**2026-03-23T22:40:17 | DmitrO**
У меня с отключённым Zapret2 и  ZeroBlock не открывает, да и с ними тоже(

---

**2026-03-24T08:27:44 | Александр**
Просьба не пинать,я в том деле можно сказать совсем не шарю) установлен zeroblock и zapret2, ютуб,телега работают нормально,хотелось бы узнать как можно добавить определенные сайты,что бы они тоже открывались.Например рутрекер?

---

**2026-03-24T09:06:36 | Anna Bagler**
Дело не в прошивке, пробуйте стратегии для запрет или запрет2, или zeroblock и zapret2.

---

**2026-03-24T16:46:44 | Bumbon4ik**
Подскажите, с телефона подключаюсь  к роутеру, используя RouterichRemote, он же tailscale, если делать роутер exit нодой , пускаю трафик через подкоп, а zapret при этом будет использоваться?

---

**2026-03-24T16:59:37 | Алексей Сергеевич**
Итак пошаговый мануал для владельцев Routerich, как завести Zeroblock+Zapret2 на дефолтных настройках.
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки"и ждем, закрываем появившуюся табличку нажав на кнопку "ОК".
3. Качаем два файла (zeroblock_*** и luci-app-***) из закрепа темы "Zeroblock" и сохраняем в папку на рабочем столе.
4. Возвращаемся в разделы Система-пакеты и жмем на кнопку "Загрузить пакет". И по очереди ставим скачанные пакеты: Zeroblock_*** а затем luci-app***.(Табличку с надписью Error игнорируем)
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4,6,7. Жмем по очереди на кнопки: сохранить и применить.(Если вдруг 6 и 7 пункт не активны, проверьте в разделе настройки пункт "Версия API", должна стоять V2)
7. Далее ждем примерно 5 минут, очищаем кэш браузера и обновляем страницу. Пока в разделе Службы не появится пункт "Zapret2".
8. Возвращаемся в Zeroblock, открываем вкладку Автонастройка и убираем галки с 6 и 7 пункта.(Автозагрузка) Иначе мы не сможем вносить изменения в секциях со списками. Сохранить, применить.
9. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
10. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
11. Проверяете работу Youtube на всех устройствах. (так же желательно в браузерах отключить функцию "Частный/безопасный DNS")

Из-за нового api v2 старые списки не будут работать, нужно либо перевыбрать нужные списки, либо переключить обратно api на v1. Если вам нужна именно точечная маршрутизация, то не используйте cidr в настройках. Полный перечень списков с расшифровкой в мануале в wiki

---

**2026-03-24T17:53:32 | Kiss_My_Axe**
# СТРАТЕГИИ В ZAPRET1
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)

---

**2026-03-24T18:43:49 | Kiss_My_Axe**
# СТРАТЕГИИ В ZAPRET1
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)

---

**2026-03-24T19:40:57 | Bullet for my valentine Poison**
Zeroblock+Zapret2.

---

**2026-03-24T19:45:49 | Routerich**
/tmp/zapret2-finder.log

---

**2026-03-24T20:04:22 | Alexey Zh**
в zapret2 в Edit List: user_exclude
добавил: 
store.akamai.steamstatic.com
store.cloudflare.steamstatic.com
store.fastly.steamstatic.com
steamcommunity.com
store.steampowered.com

---

**2026-03-24T20:06:40 | Artur Shvydko**
Всем привет. Подскажите пожалуйста, есть ли кто-нибудь кто играет в where winds meet? Если да, может быть знаете, можно ли добавить какие то сервера для стабильной работы игры, постоянно наблюдается пинг. Сейчас установлен zapret2 + zeroblock, возможно там можно прописать в настройках маршрутизации какие то сервера? Например как с mortal kombat 1

---

**2026-03-24T20:14:06 | ILDAR G.**
Подскажите пожалуйста, не могу найти пакет zapret2-finder , где он находится?

---

**2026-03-24T20:14:51 | Anna Bagler**
Он идёт з zapret2.

---

**2026-03-24T20:16:16 | ILDAR G.**
Вот я установил zapret2 , а finder нету

---

**2026-03-24T20:50:27 | ARTEM**
Пока что не существует способа в телеграме звонки и картинки через zapret сделать ?

---

**2026-03-24T22:37:09 | Sergey**
При смене  24.10.4 на 24.10.5 можно сохранить настройки?  установленный zapret надо будет переустановить?

---

**2026-03-24T22:40:28 | Святос**
В репозитории есть Zapret2, вроде ж с ним собирается

---

**2026-03-24T22:40:47 | Bullet for my valentine Poison**
А мог бы почувствовать себя молодым, сидя на Zapret2

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

**2026-03-25T00:48:32 | Den Kihot**
Уточните, пожалуйста, правильно ли я понимаю - при таком раскладе запрос сначала идет через секцию прокси, и если там есть совпадение по спискам, то в впн он уже не идет? А если ресурс не указан ни в прокси, ни в впн — тогда пакет отправляется на обработку в zapret?

---

**2026-03-25T00:50:27 | Тимур Акименко**
= ПРОВЕРКА DNS  (Прошивка: 24.10.5):

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.16 MB
  Пинг (ya.ru via awg10): ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (2a02:6b8::2:242): 56 data bytes
  Программы в автозапуске: zeroblock zapret2 opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 198.18.4.210
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock              awg10 (vpn): meta
  zeroblock          opera (prx out): geoblock,block,youtube,discord,telegram,google_ai,google_play
  Версия zeroblock: 0.6.2-r66
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.20 | RAM: 27% | NAND: 41% занято / 39.7M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-03-25T01:08:03 | Kiss_My_Axe**
2 применительно к этому:
А если ресурс не указан ни в прокси, ни в впн — тогда пакет отправляется на обработку в zapret?
Ничего никуда сознательно не отправляется, просто ZB на этот пакет не реагирует.

---

**2026-03-25T09:09:06 | Routerich**
ок, я перечитал сообщение и отвечу. 
Цепочка 
sing-box - zapret
внутри sing-box приоритеты route. то что попало в route не попадает в zapret.
трафик не указанный в sing-box проходит через zapret, тот анализирует и решает что делать
трафик ошибочно прошедший в sing-box идёт в direct-out и тоже попадает в zapret

---

**2026-03-25T09:41:59 | Udo**
Добрый день. Я так понял все разработки в данном ТГК в том числе и ZeroBlock вместе с Zapret2-finder залочены на фирменный роутер и их невозможно запустить на ванильной OpenWRT ?

---

**2026-03-25T11:13:01 | ARTEM**
Как изменить dns именно для zapret ?

---

**2026-03-25T11:57:29 | Никита Веселов**
На телефонах при подключении к роутеру не приходят Push уведомления например от того же ВК. Настроен zeroblock + zapret2. Из за чего такое может быть? При подключении к мобильной сети сразу куча уведомлений приходит.

---

**2026-03-25T11:59:45 | Routerich**
Здравствуйте.
а если остановить ZeroBlock, Zapret2 приходят?

---

**2026-03-25T12:21:20 | Bullet for my valentine Poison**
Ну и все. Пользуйтесь.  https://github.com/bol-van/zapret2/blob/master/docs/manual.md

---

**2026-03-25T12:23:03 | Виталий Александрович**
Всем здравствуйте) после первоначальной настройки, установил zeroblok + zapret2 все норм все работает👍 сделал backup роутера.
Потом руки потянулись не туда ну и в итоге нарукожопил где то и часть запрещенных сервисов перестали работать...
Вопрос, я могу через меню восстановления просто восстановится из ранее сделанного бэкапа или лучше сделать сброс на заводские?

---

**2026-03-25T12:32:56 | Роман**
Для игр попробуйте этот скрипт, там есть игровые стратегии.
sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh)

---

**2026-03-25T12:34:02 | VK11**
Тупой вопрос. стоит скрипт 5 и усе работает. Читаю тут для zapret2 появилась типа утилита zapret2-finder, мануал замечательный по ней. поставил zapret2, и чет нигде не обнаружил эту утилиту для поиска стратегий. может еще чего надо поставить?

---

**2026-03-25T12:34:43 | Routerich**
Здравствуйте.
Установите zapret2 с нашей официальной репы.

---

**2026-03-25T13:01:30 | Routerich**
У многих.
Попробуйте его обновить
Или перейти на Zapret2

---

**2026-03-25T13:21:09 | Anna Bagler**
Вы уверены что tg поможет zapret2?

---

**2026-03-25T14:00:14 | Routerich**
Смотрите в сторону zapret2

---

**2026-03-25T14:03:45 | Артём Фомин**
То есть, необходимо удалить youtubeUnblock и установить zapret2? Он у меня не установлен. Прошу прощения, за банальные вопросы, но для меня это всё в новинку.

---

**2026-03-25T14:11:12 | Артём Фомин**
Можете подсказать? Если установлю zapret2, то youtubeUnblock надо удалять? Они как-то конфликтуют или нет?

---

**2026-03-25T14:30:20 | Артём Фомин**
Спасибо за подсказки. Удалил youtubeUnblock и установил zapret2. После этого YouTube на телевизоре и на компьютере сразу заработал нормально. Никакие настройки в zapret2 вообще не менял.

---

**2026-03-25T14:45:35 | Артём Фомин**
После установки Zapret2 при диагностике в podkop появилась проблема. Пишет, что найдены дополнительные правила маркировки. При этом podkop работает нормально, заблокированные сайты открываются.

Это нормально, или может необходимо что-то настроить?

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

**2026-03-25T16:10:27 | Anna Bagler**
Отключить и остановить zapret и youtubeUnblock. Проверить.

---

**2026-03-25T16:28:13 | Anna Bagler**
https://t.me/routerich/3845/509958 - подбирайте стратегию для zapret. Следите, чтоб списка YouTube не было в подкопе.
Либо ставьте zapret2.

---

**2026-03-25T17:38:08 | Grigory**
Я вроде уже спрашивал, но есть ли способ разблокировать chatgpt и gemini? На zeroblock+zapret2. Сейчас как я понял обход работает только на grok

---

**2026-03-25T18:16:15 | Anna Bagler**
Связка идёт обычно zeroblock+zapret2.

---

**2026-03-25T19:01:32 | Bullet for my valentine Poison**
Через Zapret1 идет.Поиском пройдитесь, уже кидали несколько раз.

---

**2026-03-25T19:35:23 | Kiss_My_Axe**
# СТРАТЕГИИ В ZAPRET1
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)
Перебирайте, проверяйте.

---

**2026-03-25T19:53:47 | Anna Bagler**
Стратегии все перебрали для zapret1?

---

**2026-03-25T20:18:23 | Александр**
Подскажите а как установить zapret2??? Последняя версия прошивки...

---

**2026-03-25T20:26:54 | Артём Фомин**
Народ, подскажите, пожалуйста.

Я установил ZeroBlock. После в автонастройках отметил галочками «Установить Opera Proxy», «Настроить AmneziaWG WARP», «Установить Zapret2», «Автозагрузка секций» и «Автозагрузка новой стратегии Zapret2». У меня заработал YouTube, Facebook, Instagram и другие сайты. Всё, больше вообще ничего не менял. Приятно впечатлён, что всё это без платных сервисов.

Хотелось бы уточнения по некоторым настройкам. Скажите, в данном случае необходимо или, может, желательно установить Xray через автонастройку? Xray будет использоваться с такими настройками?

---

**2026-03-25T20:46:02 | Артём Фомин**
Народ, подскажите. По какой причине YouTube может не работать одном на телефоне, при этом работает на другом телефоне, на телевизоре и на компьютере? В Zapret2 всё по умолчанию.

---

**2026-03-25T21:24:44 | ㅤㅤ**
Глюки были с установкой ZB+Zapret2. Обычно трачу не более пяти минут и занимаюсь следующим. Но одна зараза начнет мозг выносить.

---

**2026-03-25T22:00:09 | Bullet for my valentine Poison**
Так удали его, через пакеты. И там же впиши Zapret2!

---

**2026-03-25T22:02:20 | Routerich**
Система - пакеты - обновить списки - вкладка доступно - в фильтре пишем zapret2, устанавливаем два пакета. Перезаходим в настройки роутера

---

**2026-03-25T22:33:51 | Gomer Simpson**
Я из темы Zapret2 наставил, что нашёл, они до сих пор работают.

---

**2026-03-25T22:39:14 | Святос**
Несчастный Zapret2

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

**2026-03-26T08:21:55 | Routerich**
Здравствуйте.
я считаю, что через zapret гонять нужно ютуб, чтобы рекламы не было и скорость норм была, а остальное через VPS.
и zapret геоблок не обойдёт

---

**2026-03-26T13:22:48 | Александр**
По прошествии пары недель уже можно написать отзыв) С покупкой и получением проблем не возникло,две недели борьбы с onu,дабы не зависеть от провайдерского оборудования,в итоге победили))Подключил роутер,установил zeroblock и zapret 2,практически не составило труда,хотя я далек от этой сферы деятельности,ютуб,телеграм,инстаграм,на телефонах и телевизорах работает на ура,дети в шоке,говорят все летает как раньше) Еще большой плюс в сообществе в телеграм,где подскажут в каком направлении двигаться,если что то не работает.Вообщем годная тема,главное что бы "товарищи" которые сами знаете,не обрубили совсем интернет.

---

**2026-03-26T13:22:59 | Anna Bagler**
Планшет только ругается или интернета действительно нет? По ТВ Самсунг смотрите стратегию от @BFMVPoison в закрепе zapret2 или там ещё были. Пробуйте.

---

**2026-03-26T13:50:08 | Роман**
https://github.com/bol-van/zapret2/blob/master/docs/manual.md

---

**2026-03-26T14:38:37 | Anna Bagler**
У вас же Роутерич? Тогда Система - Пакеты, кнопочка Обновить списки. Потом в поле фильтра zapret2 и ok.
youtubeUnblock отключить и остановить или удалить через пакеты.

---

**2026-03-26T15:17:09 | Garfield**
сори за тупой вопрос.

подскажите, а тот zapret2, что ставит ZB, он "ванильный" ?) просто когда я последний раз я себе ставил zapret2, он был куда беднее по возможностям

---

**2026-03-26T16:32:10 | Alex Korshun**
Кто-нибудь глядел, что нового в версии zapret2 0.9.4.5-r26?

---

**2026-03-26T16:43:35 | Alex Korshun**
Я не знал, что Фреса разрабатывает еще и zapret2. Буду знать, спасибо.

---

**2026-03-26T16:51:03 | SCORPION**
БЛИИН! СПАСИБО ОГРОМНОЕ!!!!!!!
после ребута RR на всех устройствах ютуп заработал )))
ТОлько теперь вопрос: преимущество ZeroBlock + Zapret2  перед скриптом5, если нужны только соц сети и ютуп?

---

**2026-03-26T17:39:44 | Anna Bagler**
Пробуйте стратегии для zapret2 от @BFMVPoison в теме zapret2. Приложение стандартное, обновлённое? Другое не пробовали?

---

**2026-03-26T17:53:29 | Anna Bagler**
Убирать анблок, ставить zeroblock и zapret2.

---

**2026-03-26T18:17:46 | 007**
подскажите пожалуйста, убрал ютуб из подкопа, включил zapret. а куда стратегию втыкать?

---

**2026-03-26T18:20:29 | Роман**
Подбор стратегии для Zapret1 от ув. Kiss_My_Axe - требует установленного запрета.

sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)

---

**2026-03-26T18:20:56 | Роман**
Целый комбайн для запрета от ztressozz - сам установит, обновит, настроит, но можно и руками поиграться.

sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh)

---

**2026-03-26T18:44:23 | Игорь**
Выражаю огромную благодарность всей команде Routerich, за возврат в беззаботное прошлое👍 Настроил zeroblock и zapret 2 - всё летает👌Ещё раз всем СПАСИБО !

---

**2026-03-26T19:17:30 | Sandro Flecher**
Добрый день! Подскажите, пожалуйста. Стоит zapret2 + podkop. Раздельная маршрутизация нормально настроена. Но проблемы с blockcheck2, вечная ошибка "curl: (28) Connection timed out after 1500 milliseconds UNAVAILABLE code=28". 
Подскажите куда копать.

---

**2026-03-26T19:38:10 | Anna Bagler**
Стратегию из закрепа zapret2 попробуйте.

---

**2026-03-26T21:37:17 | Sandro Flecher**
Подскажите ещё. Как решить проблему: при перезагрузке роутера с podkop+zapret2 без ручного перезапуска запрета он не работает фактически.

---

**2026-03-26T21:38:14 | Дмитрий Григорьев**
Zapret1 / Zapret2

---

**2026-03-26T21:52:34 | Sandro Flecher**
Запрет переустанавливал через репозиторий. Podkop и zapret2 от routerich последней версии. Openwrt 24.10.5. Но спасибо, попробую еще

---

**2026-03-26T22:53:24 | Anna Bagler**
Тогда вам точно как минимум запрет2 нужен. Как раз поставите zeroblock и zapret2 по краткой инструкции, а потом можно будет смотреть.

---

**2026-03-26T23:59:05 | Kiss_My_Axe**
И к нему вот это:
# СТРАТЕГИИ В ZAPRET1
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)

---

**2026-03-27T00:02:29 | Kiss_My_Axe**
Система - Пакеты, Обновить списки, Фильтр zapret

---

**2026-03-27T00:47:33 | Anna Bagler**
Службы - zapret и там смотрите.

---

**2026-03-27T00:55:11 | Kiss_My_Axe**
Службы - zapret2, Стоп, Отключить автозагрузку.
А то будет потом кишмиш.

---

**2026-03-27T00:56:27 | Kiss_My_Axe**
Ну Службы - zapret, далее по этому пути, добавить rambler.ru в User hostname entries.
А то бобошка вскочит, без шуток. Но - на роутере.

---

**2026-03-27T00:56:58 | Routerich**
luci-app-zapret

---

**2026-03-27T00:57:55 | Anna Bagler**
Система - Пакеты, кнопочка Обновить списки в поле фильтра zapret.

---

**2026-03-27T01:08:12 | Никита Лелецкий**
Ну Службы - zapret, далее по этому пути, добавить rambler.ru в User hostname entries.
А то бобошка вскочит, без шуток. Но - на роутере. 
- вы писали и хочу применить чтобы потом "бобошка не вскочила)"

---

**2026-03-27T01:47:56 | Станислав Земляков**
А у zapret2 есть?

---

**2026-03-27T08:13:39 | Sandro Flecher**
В zapret2_0.9.4.5-r26_aarch64 в https://github.com/routerich/packages.routerich/tree/24.10.4/routerich  - zapret2-finder нету почему-то. Не подвезли еще ?

---

**2026-03-27T10:29:08 | Sandro Flecher**
Ставил так: 1. Добавил ключ подписи printf 'untrusted comment: routerich public key\nRWQuck AB+2WRb9rwzhWarTedFmsv y8y5kxAS3A0KXe3yUou9V/ Nfbqty\n'> /etc/opkg/keys/ 2e724001fb65916f
2. Добавил репозиторий echo "src/gz routerich https: //raw.githubusercontent.com /routerich/packages.routerich /24.10.5/routerich" >>/etc/ opkg/customfeeds.conf
3. Обновил списки пакетов opkg update
4. Установил zapret2 и luci-app-zapret2_0.9.4.5-r26_all.ipk. Работает, но zapret2-finder нету.

---

**2026-03-27T10:35:19 | Sandro Flecher**
Понял. Странно, что сам пакет для zapret2 от routerich не эксклюзив, вроде более удобного графического нету.

---

**2026-03-27T10:49:08 | Виталий Александрович**
Всем привет. Помогите разобраться почему не открывается rutracker.
Установлены zeroblock+zapret2
Причем изначально после установки пакетов, rutracker c компа открывался, а сейчас ни с компа ни с телефона не работает. nnmclub тоже туда же

---

**2026-03-27T11:01:13 | Bullet for my valentine Poison**
/opt/zapret2/ipset/ ты наверное удалил папку, проверь.

---

**2026-03-27T13:26:28 | Yrii**
Здравствуйте. Если я поставлю zeroblock  то Ютуб перестанет работать на zapret2

---

**2026-03-27T13:31:59 | Yrii**
Здравствуйте. Если поставлю на роутер zeroblock то утюб будет работать на  zapret2

---

**2026-03-27T13:54:02 | Роман**
Если запрет 1, то в терминал sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh)
там пункт 8.

---

**2026-03-27T14:07:20 | I**
Да вроде нет , никаких драйверов не обновлял,  только пакеты ставил zapret2, zeroblock

---

**2026-03-27T14:16:40 | Alex Korshun**
Буллет, к тебе такой вопрос. 
Может ли быть такое, что из-за обрыва интернета и с последующим восстановлением сервиса перестает работать zapret2, пока его не перезагрузить?

---

**2026-03-27T14:18:05 | Alex Korshun**
Сегодня только на моей линии отключился интернет, буквально минут на 10. После как включили, дискорд и ютьюб отвалились. 
Думал было дело провайдер что-то подкрутил или фильтры DPI обновил. Однако zapret2 через терминал перезапустил и все снова поехало🧐

---

**2026-03-27T14:55:06 | Kirill Kulikov**
Здравствуйте. Подскажите, в чем проблема может быть? Роутер routerich AX3000, накатил zeroblock+zapret2. Вопрос касается нейронок, в частности Gemini. С пк работает корректно, но на телефоне Samsung S25 по wifi поработал пару дней и отлетел, стал ругаться на неподдерживаемую страну

---

**2026-03-27T16:11:40 | Михаил**
7. Далее ждем примерно 5 минут, очищаем кэш браузера и обновляем страницу. Пока в разделе Службы не появится пункт "Zapret2".

---

**2026-03-27T16:29:58 | Andrew**
Здравствуйте. Хочу настроить резалку рекламы. Сейчас стоит zeroblock+zapret2,  установил из пакетов Adblock, как настроить чтобы это все вместе работало? Сейчас похоже не работает, хотя служба adblock активна. Настройках адблока надо интерфейс для запуска выбирать?

---

**2026-03-27T17:16:39 | Дмитрий**
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-03-27T17:27:35 | Роман**
Так сидели бы на первом. 
Целый комбайн для запрета от ztressozz - сам установит, обновит, настроит, но можно и руками поиграться.

sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh)

---

**2026-03-27T17:45:47 | ARTEM**
Zapret для ютуба и варп в зероблоке по спискам без cdn но как я понимаю в этом приложении nvidia app какие то другие домены нежели скачивать в ручную с сайта

---

**2026-03-27T18:00:47 | Kiss_My_Axe**
Подбирайте. После применения каждой стратегии проверяйте на телефонах-телеках-пека
# СТРАТЕГИИ В ZAPRET1
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)

---

**2026-03-27T18:27:50 | Ilia Kotovich**
Я на чистый routerich установил zeroblock + zapret2. Далее я добавляю интерфейс с моим конфигом amnezia, но в RX всегда 0 (и handshake never). Что-то не так делаю?

---

**2026-03-27T20:52:35 | Vladimir Sever**
Пункт 7
Уже 11 минут прошло а zapret2 так и не появился

---

**2026-03-27T21:02:54 | Routerich**
Тогда Система - пакеты - обновить списки - вкладка доступно - в фильтре напишите Zapret2 и установите пакеты

---

**2026-03-27T21:44:41 | Zorg**
Всем привет. Подскажите, пожалуйста. Только подключил новый роутер. Почитал темы. Не понял что сейчас устанавливать - ZeroBlock, Zapret2, podcop, всё вместе? Дайте направление о чем дальше читать)

---

**2026-03-27T21:49:07 | IIlIlIlIIlIlIlIIIll**
у меня zapret-manager от StressOzz сам поставил это для xbox dns

---

**2026-03-27T21:57:31 | HiLLL**
а лучше удалите https-dns-proxy через тот же zapret-manager от StressOzz

---

**2026-03-27T22:59:39 | Роман**
sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh)
Нормально скопируйте и вставьте.

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

**2026-03-27T23:51:52 | Zorg**
подскажите, как посмотреть процесс загрузки служб ( или пакетов?). По инструкции к ЗБ и запрету выполнил всё до пункта
7. Далее ждем примерно 5 минут, очищаем кэш браузера и обновляем страницу. Пока в разделе Службы не появится пункт "Zapret2". , а служба запрет так и не появляется.

---

**2026-03-27T23:59:43 | Anna Bagler**
Тогда ставьте zapret2 через система - пакеты.

---

**2026-03-28T00:16:04 | V1r00z**
через костыль завелось у меня в автозагрзке происал 


# Начало блока для zapret2
(
    # Ждем 60 секунд для общей загрузки системы
    sleep 60
    
    # Пытаемся поймать интернет (пингуем Google 20 раз с паузой)
    attempts=0
    while ! ping -c 1 -W 2 8.8.8.8 > /dev/null && [ $attempts -lt 20 ]; do
        sleep 5
        attempts=$((attempts + 1))
    done
    
    # Как только интернет появился, ждем еще 5 сек для стабильности и рестартуем
    sleep 5
    /etc/init.d/zapret2 restart
    logger -t "AUTORUN" "Zapret2 was restarted after internet check"
) &
# Конец блока

---

**2026-03-28T00:28:32 | Роман**
Это либо к создателю -
https://ntc.rkn.quest/t/zapret2-%D0%BE%D0%B1%D1%81%D1%83%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5/21161/804
Либо тут выкладывайте, есть тут пара знатоков.

---

**2026-03-28T00:32:43 | Anna Bagler**
luci для zapret2 не потеряйте.

---

**2026-03-28T00:35:54 | Zorg**
Ошибкиundefined
Collected errors:
 * opkg_install_pkg: Checksum or size mismatch for package gzip. Either the opkg or the package index are corrupt. Try 'opkg update'.
 * opkg_install_cmd: Cannot install package zapret2.

Команда opkg install завершилась с ошибкой с кодом 255.

---

**2026-03-28T09:09:08 | Дмитрий З**
Я же правильно понимаю, что если на свежекупленном позавчера РР с установленным ZB + Zapret2 всё работает изумительно , кроме Youtube на ТВ Samsung на tizen os - то проверять только перебором стратегий? Или вообще забить на родное tizen приложение и думать что-то еще? Перепробовал , по моему, все предложенные в чате страты, почти все они более-менее работают на ПК и на всех андроидах в доме (+- меняется скорость первоначального открытия видео, но есть страты где всё мгновенно открывается), а вот на этом сраном ТВ никак. Приложение или вылетает или висит на стартовом экране.

---

**2026-03-28T10:35:47 | Kiss_My_Axe**
Вы тоже только по одной строке зараз пишете? И ждёте предложений, чтобы ответить - это я уже делал?

Система - Пакеты, Обновить списки
В Фильтр вписать zapret2
Вкладка Установленные, удалить zapret2
Вкладка Доступно, установить zapret2 и luci-app-zapret2

---

**2026-03-28T11:14:58 | Routerich**
Sat Mar 28 10:43:59 2026 daemon.info zeroblock[31104]: ========================================================================
Sat Mar 28 10:43:59 2026 daemon.info zeroblock[31104]:          HEALTH MONITOR
Sat Mar 28 10:43:59 2026 daemon.info zeroblock[31104]: ========================================================================
Sat Mar 28 10:43:59 2026 daemon.info zeroblock[31104]:
Sat Mar 28 10:44:03 2026 daemon.info zeroblock[31104]: [health_monitor] Internet is accessible
Sat Mar 28 10:44:03 2026 daemon.info zeroblock[31104]: [health_monitor] Checking WARP via awg10 to 1.1.1.1
Sat Mar 28 10:44:03 2026 daemon.info zeroblock[31104]: Internet:          OK
Sat Mar 28 10:44:06 2026 daemon.info zeroblock[31104]: [health_monitor] WARP is working (ping successful)
Sat Mar 28 10:44:06 2026 daemon.info zeroblock[31104]: [health_monitor] Checking Opera Proxy via HTTP proxy 127.0.0.1:18080
Sat Mar 28 10:44:06 2026 daemon.info zeroblock[31104]: WARP (AmneziaWG):  OK
Sat Mar 28 10:44:07 2026 daemon.info zeroblock[31104]: [health_monitor] Opera Proxy is working
Sat Mar 28 10:44:07 2026 daemon.info zeroblock[31104]: [health_monitor] Found 2 routing sections
Sat Mar 28 10:44:07 2026 daemon.info zeroblock[31104]: Opera Proxy:       OK
Sat Mar 28 10:44:07 2026 daemon.info zeroblock[31104]: Zapret (DPI):      Skipped (disabled)
Sat Mar 28 10:44:07 2026 daemon.info zeroblock[31104]: Routing Sections:  OK (2 sections)
Sat Mar 28 10:44:07 2026 daemon.info zeroblock[31104]:
Sat Mar 28 10:44:07 2026 daemon.info zeroblock[31104]: [daemon] Health: warp=OK opera=OK dpi=0/0
Sat Mar 28 10:44:07 2026 daemon.info zeroblock[31104]: ========================================================================
Sat Mar 28 10:44:07 2026 daemon.info zeroblock[31104]: All checked systems are working
Sat Mar 28 10:44:07 2026 daemon.info zeroblock[31104]: ========================================================================
Sat Mar 28 10:44:07 2026 daemon.info zeroblock[31104]:
Sat Mar 28 10:44:08 2026 daemon.info zeroblock[31104]: [daemon] Health worker completed (#111)
Sat Mar 28 10:46:02 2026 daemon.warn odhcpd[4315]: No default route present, setting ra_lifetime to 0!
Sat Mar 28 10:49:08 2026 daemon.info zeroblock[31104]: [daemon] Health worker started
Sat Mar 28 10:49:08 2026 daemon.info zeroblock[31104]: [health_monitor] Installed components: AWG=1, Opera=1, Zapret=0, Sections=1
Sat Mar 28 10:49:08 2026 daemon.info zeroblock[31104]: [health_monitor] Checking internet via ping to 8.8.8.8 and 1.1.1.1
Sat Mar 28 10:49:08 2026 daemon.info zeroblock[31104]:
Sat Mar 28 10:49:08 2026 daemon.info zeroblock[31104]: ========================================================================
Sat Mar 28 10:49:08 2026 daemon.info zeroblock[31104]:          HEALTH MONITOR
Sat Mar 28 10:49:08 2026 daemon.info zeroblock[31104]: ========================================================================
Sat Mar 28 10:49:08 2026 daemon.info zeroblock[31104]:
Sat Mar 28 10:49:12 2026 daemon.info zeroblock[31104]: [health_monitor] Internet is accessible
Sat Mar 28 10:49:12 2026 daemon.info zeroblock[31104]: [health_monitor] Checking WARP via awg10 to 1.1.1.1
Sat Mar 28 10:49:12 2026 daemon.info zeroblock[31104]: Internet:          OK
Sat Mar 28 10:49:15 2026 daemon.info zeroblock[31104]: [health_monitor] WARP is working (ping successful)
Sat Mar 28 10:49:15 2026 daemon.info zeroblock[31104]: [health_monitor] Checking Opera Proxy via HTTP proxy 127.0.0.1:18080
Sat Mar 28 10:49:15 2026 daemon.info zeroblock[31104]: WARP (AmneziaWG):  OK
Sat Mar 28 10:49:16 2026 daemon.info zeroblock[31104]: [health_monitor] Opera Proxy is working
Sat Mar 28 10:49:16 2026 daemon.info zeroblock[31104]: [health_monitor] Found 2 routing sections
Sat Mar 28 10:49:16 2026 daemon.info zeroblock[31104]: Opera Proxy:       OK
Sat Mar 28 10:49:16 2026 daemon.info zeroblock[31104]: Zapret (DPI):      Skipped (disabled)
Sat Mar 28 10:49:16 2026 daemon.info zeroblock[31104]: [daemon] Health: warp=OK opera=OK dpi=0/0
Sat Mar 28 10:49:16 2026 daemon.info zeroblock[31104]: Routing Sections:  OK (2 sections)

---

**2026-03-28T12:29:46 | Serge**
Здравствуйте! Почему отключаются стратегии? Я включаю, сохраняю, через какое-то время отваливается инста и ютьюб. Захожу в Zapret - чекбоксы без галок.
Обновление стратегии а ЗБ выключены

---

**2026-03-28T12:56:01 | Anna Bagler**
Прошивка у вас актуальная. Связка zeroblock+zapret2 или zeroblock и zapret.

---

**2026-03-28T13:24:05 | Anna Bagler**
Стратегии для discord можно посмотреть в теме Zapret2. И попробовать. Нет, вернуть галку.

---

**2026-03-28T13:28:49 | Միխայիլ Կուլագին**
Когда в руках оказался молоток, то теперь всё кажется гвоздём (с)
Изучив по диагонали https://github.com/bol-van/zapret2/blob/master/docs/manual.md , я офигел от возможностей, которые открылись, а фантазии не хватает.

Вопрос: а для каких ещё ресурсов вы применяете zapret2? По чату выше вижу, что для discord'а и roblox'а (два неизвестных мне продукта), а для чего-то ещё полезного может пригодиться?

---

**2026-03-28T15:03:48 | Nikita**
как правильно поступить? сейчас из жалоб - сжирается вся оперативка (свободно 5-10 мб буквально), вечно отваливается youtubeunblock/zapret (не хватает памяти по факту), podkop живет кое-как. 

хотелось бы все обновить, сохранив доступы удаленные + настроить все максимально оптимально, чтоб памяти хватало

---

**2026-03-28T16:27:39 | Bullet for my valentine Poison**
https://github.com/bol-van/zapret2/blob/master/docs/manual.md вот, почитайте.

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

**2026-03-28T17:54:06 | мерзость**
Здравствуйте, пытаюсь установить Zeroblock+Zapret2 но в службах после автонастройки и не появляется Zapret2. Как быть?

---

**2026-03-28T18:16:10 | Николаич**
Спецы такой вопрос: обновив zeroblock надо так же через пакеты обновлять zapret2?

---

**2026-03-28T18:59:36 | Артём Фомин**
Всем привет.
Как я полагаю, zapret2 и zeroblock лучше периодически обновлять. Подскажите, после обновления всё надо будет настраивать заново, или настройки сохраняться?

---

**2026-03-28T19:33:18 | Роман**
Это тебе  https://github.com/rcd27/zapret2-mcp

---

**2026-03-28T19:43:36 | Ilya Sukhorukov**
Добрый вечер

Подскажите, а как найти zapret2-finder? Версия zapret 0.9.4.5-r27, версия прошивки 24.10.5

---

**2026-03-28T23:05:05 | Роман**
У тебя Zapret Finder есть, играйся 😁

---

**2026-03-28T23:05:44 | Святос**
Пропали все списки из Zapret2, жму загрузку и ничего

---

**2026-03-28T23:07:56 | Kiss_My_Axe**
Система - Восстановление / Обновление
Вкладка Config
добавь /opt/zapret2 # или как там

---

**2026-03-28T23:17:09 | Святос**
# /etc/example.conf
# /etc/openvpn/
# /opt/zapret2


Вот так вот?

---

**2026-03-28T23:31:48 | Kiss_My_Axe**
# <—- комментарий

Вот так
# Здеся мы архивируем запрет2
/opt/zapret2

---

**2026-03-28T23:40:11 | HiLLL**
А в автозагрузке выбрал Автозагрузка новой стратегии Zapret2?

---

**2026-03-28T23:42:00 | Станислав Земляков**
Кстати юзайте status фичу после того, как приняли правила для zapret2

---

**2026-03-28T23:43:25 | Макс**
Привет! а как вот этот лог ограничить? 
241.1M  /tmp/zapret2/main.log

---

**2026-03-28T23:50:56 | Станислав Земляков**
Домен не резолвится на уровне DNS. Это не SNI/DPI блокировка — zapret2/nfqws2 здесь бессилен. Решение - смена DNS-резолвера (DoH/DoT), а не anti-DPI.

---

**2026-03-28T23:52:41 | Routerich**
zapret2

---

**2026-03-29T00:03:43 | Святос**
Произошло что-то произошедшее и неясное. Уничтожена папка /opt/zapret2, запросил новый через Зэроблок и он хороший. Из репозиториев плохой, получается

---

**2026-03-29T00:18:07 | Станислав Земляков**
Согласен полностью, но zapret2(nfqws2) - тем и хорош, что это не КВН. Не надо переключать туда-суда, когда хочешь открыть, например, банковское приложение. Это L2, а значит можно вообще жить в отрыве от КВН стэка. Короче, свои плюсы тоже есть

---

**2026-03-29T00:20:03 | Станислав Земляков**
Вот тут-то магия zapret2  и отрабатывает на 146%

---

**2026-03-29T09:55:14 | De**
Добрый день подскажите пожалуйста. Роутеррич подключен к asus роутеру в который подключен провайдер. В квартире все подключено к роутеррич кроме ПК который подключен по проводу к asus. Я думал чтобы не увеличивать пинг в игре подключу напрямую к Асус. И запущу оплаченный гирап. Чтобы routerich не влиял на хороший. В итоге все глючит. Выключил zeoblock и zapret 2 не помогло. Только перезагрузка asus помогла. Как-то возможно чтобы не отрубать роутеррич для комфортной игры. Или это не возможно.

---

**2026-03-29T10:18:11 | karat**
Помогите пожалуйста запустить свой VPS.
Что делал.
На чистую прошивку устанавливаю Zeroblock, в сеции Автонастройка отмечаю  Настроить AmneziaWG WARP 
Снимаю галочки - Автозагрузка секций,- Автозагрузка новой стратегии Zapret2
Интерфейсы -> awg10 --> Импорт конфигурации --> переписываю существующий конфиг штатной amnezia WG своим конфигом.
Убрать галку с fake ip - убрал
Поставить галку не создавать маршруты - поставил
Чуть-чуть настроить фаервол - проверяю настройки фаервола согласно скриншотам https://t.me/routerich/4/573119
И не заводится. Открывает некоторые заблокированные сайты но с задержкой до 30 сек.
Нашел в советах "в разделе службы - watchdoc - warp снять галочку с включить - применить"
но не нашел где эта галочка?

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

**2026-03-29T11:25:16 | Alexei**
У меня в службах просто Zapret стоит - я так понимаю, он вместе с podkop встал.

---

**2026-03-29T11:36:38 | AleXXXey**
Кароч. тема такая.
Помнишь я писал в ветке ЗБ про баг в запрет2, что у меня во вкладке "списки", нету списков?

Так вот. Вчера я писал, что ЮТ отрыгнул через запрет2.

Думал дефолтная стратегия протухла. Мучался с подбором новой стратегии. И на 3 часу зависло на домене googlevideo. Остановил, терпения не хватило.

Думаю, дай-ка удалю обратно списки zapret_hosts_youtube.txt и zapret_hosts_user_exclude.txt из папки запрета.

Только удалил, запрет перезапустил. Ютуб заколосился на дефолтной стратегии.


Похоже, у меня какой-то индивидуальный баг.

Причём, когда добавляю эти два списка обратно в папку, то ютуб может сразу отрыгнуть, а может через 2-3 часа.


Совет "сброс на завод", думаю, в моём случае, не имеет смысла. Так как это проявляется и до сброса и после сброса.

Либо у меня слишком кривые ручки.🤷🏿‍♂️

---

**2026-03-29T16:38:11 | Anna Bagler**
Zeroblock стоит с zapret2?

---

**2026-03-29T17:03:45 | Роман**
В инкогнито открывали? Кеш? В пакетах есть zapret2?

---

**2026-03-29T17:17:58 | ARTEM**
Как пустить весь трафик через zapret а после него через zeroblock ?

Такая проблема ютуб работает через zapret, но именно когда первый раз открываешь ютуб на любом устройстве прогружается долго потом уже нормально,хочу убрать этот так называемый "спящий режим" zapret

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

**2026-03-29T20:16:04 | Алексей Храбрых**
День добрый. Настроил по инструкции Zeroblock+zapret2. Из списков Music - Tidal не робит что-то,на разных устройствах.  Пишет на сайте Your request was blocked. Куда копать? Soundcloud нормально все

---

**2026-03-29T20:51:54 | Alex_Jester**
Я правильно понимаю, что Zapret2 в Zeroblock используется только для Youtube. И если я планирую пускать трафик Ютуба через VPN, то можно Запрет и не устанавливать (не ставить галочку №4)

---

**2026-03-29T21:01:01 | Alex_Jester**
Т.е. если Zapret не ставить, то можно включить пункт автозагрузка секций для автоматического обновления списков машрутизации?

---

**2026-03-29T21:33:51 | Gomer Simpson**
00 5 * * *  service zapret2 restart

---

**2026-03-29T22:28:51 | ㅤㅤ**
Добрый! Zapret2 0.9.4.3-r7 под OpenWRT 25.* никто не собирал? apk требуется.

---

**2026-03-29T22:51:59 | Sandro Flecher**
https://github.com/remittor/zapret-openwrt/releases/tag/v0.9.20260307 посмотри. В архиве должен лежать

---

**2026-03-29T22:59:40 | ㅤㅤ**
Благодарю! remittor ставил, но вроде по сути это Zapret 1 нет?

Все разобрался!

---

**2026-03-29T23:29:51 | Red Cat🐈**
Подскажите, а почему дашборд (или что это?) состоит просто из серых прямоугольников? 

В диагностике все зелёное, кроме fakeip client (ну и zapret не установлен)

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

**2026-03-29T23:45:26 | Routerich**
Zapret остановите и выключите автозапуск. В подкопе в секции дискорд выберите список ютуб и телевизоры перезагрузите

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

**2026-03-30T12:51:19 | Роман**
Просто продолжайте настройку. Никакие пакеты обновлять массово не стоит, для этого есть (как заметили выше) ASU (но это потом, как разберётесь немного). 
Такие пакеты как zeroblock, zapret2 - можно обновить.

---

**2026-03-30T13:16:32 | Роман**
Система пакеты обновить списки фильтр zapret2 установить 2 пакета, релог.

---

**2026-03-30T14:49:07 | Святос**
Зероблок стоит обновлять и Zapret2, остальное ждём большим обновлением

---

**2026-03-30T14:54:18 | Anna Bagler**
Если у вас все работает, то можно даже связку zeroblock+zapret2 не обновлять.

---

**2026-03-30T15:48:52 | Grigory**
grok по умолчанию вроде работает в стандартной конфигурации без настроек, zapret2+zeroblock с включенным списком ai

---

**2026-03-30T16:05:47 | Grigory**
zapret2 zeroblock и вроде там опера включена, остальное стандартное ничего не настраивал

---

**2026-03-30T16:56:14 | Vasa**
наконец то пригодится zapret )

---

**2026-03-30T18:35:48 | Ivan Num**
Просто по инструкции настроил zeroblock. Zapret2 получается установлен тоже. Летает быстрее чем на скрипт 5

---

**2026-03-30T20:17:21 | Данил**
Это помогло, но сделал только до пункта 8, в службе zapret2 нет раздела Секции маршрутизации

---

**2026-03-30T21:54:51 | Anna Bagler**
Он был через zapret2.

---

**2026-03-30T23:30:27 | HiLLL**
zapret это костыль для ютуба, если варп в блоке провайдера

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

**2026-03-31T00:37:56 | Роман**
Через пакеты, система пакеты обновить списки фильтр zapret2, установить два пакета.

---

**2026-03-31T00:46:16 | Роман**
Установите запрет 2. Система -> пакеты -> обновить списки -> в поле фильтр вписать zapret2 -> установить 2 пакета сверху вниз.
Для ютуба, если будете делать по видео.

---

**2026-03-31T00:49:31 | A**
Не дает ничего установить. Пробую podkop и zapret2

---

**2026-03-31T02:17:05 | Alex_Jester**
Итак пошаговый мануал для владельцев Routerich, как завести Zeroblock+Zapret2 на дефолтных настройках.
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки" и ждем, закрываем появившуюся табличку нажав на кнопку "Закрыть".
3. Вводим в окне "Фильтр" (слева) Zeroblock. Внизу должны появиться два пакета: Zeroblock и luci-app-zeroblock.
4. Нажимаем кнопку "Установить" напротив каждого пакета.(Первым идет Zeroblock, а затем luci-app). В появившемcя окне жмем еще раз установить. После завершения закрываем окно. 
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4. Жмем по очереди на кнопки: сохранить и применить.
7. Далее ждем примерно 5 минут, очищаем кэш браузера и обновляем страницу. Пока в разделе Службы не появится пункт "Zapret2".
8. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
9. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
10. Проверяете работу Youtube на всех устройствах. (так же желательно в браузерах отключить функцию "Частный/безопасный DNS")

---

**2026-03-31T02:17:19 | Anna Bagler**
Обновить прошивку без сохранения настроек. Настроить. Поставить и настроить zeroblock+zapret2.

---

**2026-03-31T06:33:18 | Routerich**
лишён права использовать zapret2

---

**2026-03-31T10:29:08 | В.В.**
Сначала luci-app-zapret а потом сам запрет или наоборот?

---

**2026-03-31T10:39:18 | Evgen**
Подскажите, зказал роутер, там по умолчанию установлены zapret podkop и тд?

---

**2026-03-31T10:45:16 | Bullet for my valentine Poison**
Зайти в фаловый менеджер, и засунуть в папку /opt/zapret2/ipset

---

**2026-03-31T11:52:18 | Andrew**
Добрый день. Подскажите возможно ли на роутере поднять впн, и чтобы другие клиенты могли подключиться к нему и смотреть Ютуб с настроенным на роутере обходом zeroblock+zapret2? Ширина канала позволяет. Если это возможно, то сколько клиентов он потянет?

---

**2026-03-31T13:14:54 | Evgen**
с zapret первой версии можно обойти ограничения тг для ios?

---

**2026-03-31T14:17:41 | Anna Bagler**
Итак пошаговый мануал для владельцев Routerich, как завести Zeroblock+Zapret2 на дефолтных настройках.
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки" и ждем, закрываем появившуюся табличку нажав на кнопку "Закрыть".
3. Вводим в окне "Фильтр" (слева) Zeroblock. Внизу должны появиться два пакета: Zeroblock и luci-app-zeroblock.
4. Нажимаем кнопку "Установить" напротив каждого пакета.(Первым идет Zeroblock, а затем luci-app). В появившемcя окне жмем еще раз установить. После завершения закрываем окно. 
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4. Жмем по очереди на кнопки: сохранить и применить.
7. Далее ждем примерно 5 минут, очищаем кэш браузера и обновляем страницу. Пока в разделе Службы не появится пункт "Zapret2".
8. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
9. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
10. Проверяете работу Youtube на всех устройствах. (так же желательно в браузерах отключить функцию "Частный/безопасный DNS")

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

**2026-03-31T16:19:49 | Anna Bagler**
Пусть он вам и поможет тогда, наверняка настраивал, раз посоветовал.
Убирайте YouTube из zeroblock, разбирайтесь, как вносить стратегию в zapret2 Включайте zapret2 и пробуйте стратегию из закрепа темы Zapret2.

---

**2026-03-31T16:19:49 | Yury Kuzmenko**
opkg_install_cmd: Cannot install package luci-i18n-zapret2-ru.

---

**2026-03-31T16:38:06 | Routerich**
пакета давно не существует
Cannot install package luci-i18n-zapret2-ru.

---

**2026-03-31T16:38:30 | Evgen**
а тг через zepoblock и zapret2 пашет на ios?

---

**2026-03-31T17:16:37 | Anna Bagler**
Потом пробуете стратегии, если будете на zapret2 YouTube пробовать.

---

**2026-03-31T18:28:48 | Routerich**
Лишён права использовать Zapret2, пересадить принудительно на awg

---

**2026-03-31T18:38:15 | Роман**
Если в запрете 2 другие стратегии пробуйте, может придётся использовать запрет 1 от ztressozz. 

https://github.com/StressOzz/Zapret-Manager

---

**2026-03-31T18:45:30 | Роман**
Если только ютуб - установить zapret2 через пакеты, отключить youtubeunblock.

---

**2026-03-31T19:07:37 | A V**
Здрасьте. Youtubeunblock перестал работать с телефонами, работает только с приставкой для телевизора, и то начались какие-,то зависания переодически. Поставил zapret2. Он не настроен, Youtubeunblock работает параллельно с ним пока. Прочитал, что есть утилита zapret2-finder для настройки. Прочитал описание, но саму утилиту не нашёл в репозитории. Куда двигаться дальше?

---

**2026-03-31T19:09:10 | Routerich**
Здравствуйте.
установите zapret2 с нашей репы, потом в zapret2 заходите, там вкладка "поиск стратегий"

---

**2026-03-31T19:13:18 | A V**
Чего-то не нашёл. Я даж и не знаю, из какого репозитория скачивал. Просто в система-пакеты в поиске задал zapret2, и скачал 2 файла, сам запрет, и для Люси закладку.

---

**2026-03-31T19:13:53 | Routerich**
скриншот покажите пакета zapret2

---

**2026-03-31T19:17:02 | A V**
Хм.. zapret2 в репо это был.

---

**2026-03-31T19:44:15 | A V**
А смысл использовать, если есть zapret2? Я так понял, что это то же самое, но более продвинутое?

---

**2026-03-31T20:30:33 | A V**
Накатил Zapret2. Там уже стратегия стоит пользовательская,Ютуба, плюс два скрипта diskord_media и stun4all. И ничего не работает, конечно. Запустил поиск стратегий. Ищет. Чего делать-то когда найдёт? В Люсе, если что, не по bash.

---

**2026-03-31T20:48:39 | Jelani**
Подскажите как вы решаете что использовать?
Получается есть 2 основных варианта или нет?
1) Установить скрипт #5 (это Podkop)
2) Установить Zeroblock и Zapret2

Или там много разных вариантов просто это два готовых варианта для чайников кто не шарит в сетях?

---

**2026-03-31T20:53:23 | Максим**
Добрый вечер, прошу прощения за тупой вопрос, а facetime как через zapret2 запустить?

---

**2026-03-31T22:18:04 | Артём Фомин**
Так зачем, если YouTube заработал? А что вообще делает этот код? Как-то перенастраивает Zapret2?

---

**2026-04-01T00:12:08 | Ft**
Добрый вечер, не работает или очень плохо работает WhatsApp  , конфигурация Zeroblok , Zapret 2.
Может кто подскажет куда копать?

---

**2026-04-01T03:07:07 | Routerich**
Zapret

---

**2026-04-01T06:20:17 | Albert**
Здравствуйте. Я правильно понимаю, что из-за работы компонента "автозагрузка новой стратегии Zapret2" происходит периодическое выключение rr_youtube, и включение rr_default и rr_blackhole из-за чего падает ютуб. По утрам начал в последние два дня замечать, раньше нормально было. Приходится заходить в "службы"-"zapret2" и заново каждый раз включать галку возле rr_youtube" и выключать у rr_default и rr_blackhole. Но если я выключу автозагрузку, тогда при "смерти" стратегии судя по названию пункта он не будет автоматом заменен? Хочу понять из-за чего автоматом происходит отключение галки "rr_youtube" и включение двух вышеназванных. Кстати, когда позавчера возился с авг10 я вырубил автозагрузку секции в зероблоке, может оно сказалось (по крайней мере по таймингу совпадает). Подскажите пожалуйста что делать

---

**2026-04-01T06:47:36 | Routerich**
Здравствуйте.
убрать галочку с "Автозагрузка новой стратегии Zapret2"

---

**2026-04-01T07:12:40 | Routerich**
Здравствуйте.
Если пользуетесь Zapret2, то искать другую стратегию

---

**2026-04-01T08:09:02 | Routerich**
Здравствуйте.
сможете, zapret2 по умолчанию точечно работает, по тому, что вы ему укажете в списках доменов.

---

**2026-04-01T10:11:39 | Фотограф Александр Москаленко**
и еще я включил zapret у меня в верху написано "обновляется" уже долго . Нужно подождать или он уже включился ?

---

**2026-04-01T10:19:21 | 🆂🅷🅾🅳🅸🅼🅰🆂🆃🅴🆁**
Привет присутствующим. Подскажите пожалуйста откуда появляются в zapret2 отдельные секции rr_youtube и блэкхол. У меня раньше были. Как то из ставил. Сейчас нету. Автозагрузку в зероблоке включаю выключаю не появляется ничего (предполагал что от туда ставится)

---

**2026-04-01T10:20:55 | Routerich**
"Автозагрузка новой стратегии Zapret2"

---

**2026-04-01T12:00:23 | Routerich**
Здравствуйте.
пробуйте эту стратегию для zapret2
https://t.me/routerich/462347/522134

---

**2026-04-01T13:16:55 | Bullet for my valentine Poison**
я тут на неделе страдал фигней. Может кому-то захочется потыкать, или сделать лучше.
полноценный рабочий custom.d‑скрипт, который:
•   выбирает случайный TLS ClientHello blob из твоего списка
•   генерирует случайный набор позиций multidisorder
•   передаёт всё это в NFQWS
•   работает на всех нужных портах Tarkov
•   не конфликтует с другими стратегиями
•   не требует UCI‑стратегий вообще

Создай файл:
nano /opt/zapret2/init.d/openwrt/custom.d/60-tarktest.sh

Вставить в  файл:
#!/bin/sh

# Randomized TLS ClientHello desync for Tarkov ports

# --- RANDOM BLOB SELECTION ---
pick_blob() {
    # список твоих блобов
    BLOBS="
blob_tls_clienthello_2gis_com
blob_tls_clienthello_2gis_ru
blob_tls_clienthello_alfabank_ru
blob_tls_clienthello_api_photo_2gis_com
blob_tls_clienthello_barclays_co_uk
blob_tls_clienthello_commba_mail_ru
blob_tls_clienthello_escapefromtarkov_com
blob_tls_clienthello_google_com_tlsrec
blob_tls_clienthello_gosuslugi_ru
blob_tls_clienthello_iana_org
blob_tls_clienthello_iana_org_bigsize
blob_tls_clienthello_moskva_taximaxim_ru
blob_tls_clienthello_rutracker_org_kyber
blob_tls_clienthello_sberbank_ru
blob_tls_clienthello_static_lemanapro_ru
blob_tls_clienthello_t2_ru
blob_tls_clienthello_ticket_rzd_ru
blob_tls_clienthello_vk_com
blob_tls_clienthello_vk_com_kyber
blob_tls_clienthello_www_4pda_to
blob_tls_clienthello_www_google_com
blob_tls_clienthello_www_max_ru
"

    set -- $BLOBS
    COUNT=$#
    IDX=$(( RANDOM % COUNT + 1 ))
    eval echo "\${$IDX}"
}

# --- RANDOM MULTIDISORDER POSITIONS ---
pick_md() {
    POS="
1
sniext+1
host+1
midsld-2
midsld
midsld+2
endhost-1
"

    set -- $POS
    OUT=""
    for p in "$@"; do
        if [ $(( RANDOM % 2 )) -eq 1 ]; then
            [ -z "$OUT" ] && OUT="$p" || OUT="$OUT,$p"
        fi
    done

    # если ничего не выбралось — выбираем один случайный
    if [ -z "$OUT" ]; then
        COUNT=$#
        IDX=$(( RANDOM % COUNT + 1 ))
        eval OUT="\${$IDX}"
    fi

    echo "$OUT"
}

# --- BUILD FINAL NFQWS OPTIONS ---
RANDBLOB=$(pick_blob)
RANDMD=$(pick_md)

NFQWS_OPT_TARKTEST="--payload=tls_client_hello \
--lua-desync=fake:blob=$RANDBLOB:badsum:tcp_ts=-600000:repeats=6 \
--lua-desync=multidisorder:pos=$RANDMD"

alloc_dnum DNUM_TARKTEST
alloc_qnum QNUM_TARKTEST

zapret_custom_daemons() {
    local opt="--qnum=$QNUM_TARKTEST $NFQWS_OPT_TARKTEST"
    do_nfqws $1 $DNUM_TARKTEST "$opt"
}

zapret_custom_firewall() {
    local ftcp='-p tcp -m multiport --dports 443,17000:18000,27014:27020,50000:60000'
    local fudp='-p udp -m multiport --dports 443,17000:18000,27014:27020,50000:60000'
    fw_nfqws_post $1 "$ftcp" "$fudp" $QNUM_TARKTEST
}

zapret_custom_firewall_nft() {
    local f='(tcp dport {443,17000-18000,27014-27020,50000-60000} || udp dport {443,17000-18000,27014-27020,50000-60000})'
    nft_fw_nfqws_post "$f" "$f" $QNUM_TARKTEST
}

Сохраняем.

Делаем исполняемым
chmod +x /opt/zapret2/init.d/openwrt/custom.d/60-tarktest.sh

Перезапуск:
/etc/init.d/zapret2 restart

P.S. Работает по всему трафику, при перезапуске меняет рандомно блоб из списка. (Ну и опции мультидиза)

---

**2026-04-01T13:28:36 | Станислав Земляков**
Псть, это ты с ИИ агентом писал? Есть MCP для zapret2 ;)

---

**2026-04-01T13:42:36 | Bullet for my valentine Poison**
adding low-priority default empty desync profile we have 1 user defined desync profile(s) and default low priority profile 0 we have 0 user defined desync template(s) profile 1 (noname) lua fake(repeats="6",tcp_ts="-600000",badsum="",blob="blob_tls_clienthello_ticket_rzd_ru" range_in=x0-x0 range_out=a0-a0 payload_type= tls_client_hello) profile 1 (noname) lua multidisorder(pos="1,sniext+1,host+1,midsld,endhost-1" range_in=x0-x0 range_out=a0-a0 payload_type= tls_client_hello)
lists summary:
blobs summary: blob 'fake_default_tls' : size=680 alloc=808 blob 'fake_default_http' : size=263 alloc=263 blob 'fake_default_quic' : size=620 alloc=620
initializing conntrack with timeouts tcp=60:300:60 udp=60 ipcache lifetime 7200s Running as UID=1 GID=1 initializing raw sockets bind-fix4=0 bind-fix6=0 set_socket_buffers fd=3 rcvbuf=2048 sndbuf=32768 fd=3 SO_RCVBUF=4096 fd=3 SO_SNDBUF=65536 set_socket_buffers fd=4 rcvbuf=2048 sndbuf=32768 fd=4 SO_RCVBUF=4096 fd=4 SO_SNDBUF=65536
LUA INIT LUA v5.1 LuaJIT 2.1.1756211046 OpenResty JIT: ON fold cse dce fwd dse narrow loop abc sink fuse LUA REMOVE: os.execute io.popen package.loadlib debug package.loaded.debug LUA BLOB: fake_default_tls (size=680) LUA BLOB: fake_default_http (size=263) LUA BLOB: fake_default_quic (size=620) LUA STR: NFQWS2_VER LUA NUMERIC: qnum desync_fwmark NFQWS2_COMPAT_VER VERDICT_PASS VERDICT_MODIFY VERDICT_DROP VERDICT_MASK VERDICT_PRESERVE_NEXT DEFAULT_MSS IP_BASE_LEN IP6_BASE_LEN TCP_BASE_LEN UDP_BASE_LEN ICMP_BASE_LEN TCP_KIND_END TCP_KIND_NOOP TCP_KIND_MSS TCP_KIND_SCALE TCP_KIND_SACK_PERM TCP_KIND_SACK TCP_KIND_TS TCP_KIND_MD5 TCP_KIND_AO TCP_KIND_FASTOPEN TH_FIN TH_SYN TH_RST TH_PUSH TH_ACK TH_FIN TH_URG TH_ECE TH_CWR IP_RF IP_DF IP_MF IP_OFFMASK IP_FLAGMASK IPTOS_ECN_MASK IPTOS_ECN_NOT_ECT IPTOS_ECN_ECT1 IPTOS_ECN_ECT0 IPTOS_ECN_CE IPTOS_DSCP_MASK IP6F_MORE_FRAG IPV6_FLOWLABEL_MASK IPV6_FLOWINFO_MASK IPPROTO_IP IPPROTO_IPIP IPPROTO_IPV6 IPPROTO_ICMP IPPROTO_TCP IPPROTO_UDP IPPROTO_ICMPV6 IPPROTO_SCTP IPPROTO_HOPOPTS IPPROTO_ROUTING IPPROTO_FRAGMENT IPPROTO_AH IPPROTO_ESP IPPROTO_DSTOPTS IPPROTO_MH IPPROTO_HIP IPPROTO_SHIM6 IPPROTO_NONE ICMP_ECHOREPLY ICMP_DEST_UNREACH ICMP_REDIRECT ICMP_ECHO ICMP_TIME_EXCEEDED ICMP_PARAMETERPROB ICMP_TIMESTAMP ICMP_TIMESTAMPREPLY ICMP_INFO_REQUEST ICMP_INFO_REPLY ICMP_UNREACH_NET ICMP_UNREACH_HOST ICMP_UNREACH_PROTOCOL ICMP_UNREACH_PORT ICMP_UNREACH_NEEDFRAG ICMP_UNREACH_SRCFAIL ICMP_UNREACH_NET_UNKNOWN ICMP_UNREACH_HOST_UNKNOWN ICMP_UNREACH_NET_PROHIB ICMP_UNREACH_HOST_PROHIB ICMP_UNREACH_TOSNET ICMP_UNREACH_TOSHOST ICMP_UNREACH_FILTER_PROHIB ICMP_UNREACH_HOST_PRECEDENCE ICMP_UNREACH_PRECEDENCE_CUTOFF ICMP_REDIRECT_NET ICMP_REDIRECT_HOST ICMP_REDIRECT_TOSNET ICMP_REDIRECT_TOSHOST ICMP_TIMXCEED_INTRANS ICMP_TIMXCEED_REASS ICMP6_ECHO_REQUEST ICMP6_ECHO_REPLY ICMP6_DST_UNREACH ICMP6_PACKET_TOO_BIG ICMP6_TIME_EXCEEDED ICMP6_PARAM_PROB MLD_LISTENER_QUERY MLD_LISTENER_REPORT MLD_LISTENER_REDUCTION ND_ROUTER_SOLICIT ND_ROUTER_ADVERT ND_NEIGHBOR_SOLICIT ND_NEIGHBOR_ADVERT ND_REDIRECT ICMP6_DST_UNREACH_NOROUTE ICMP6_DST_UNREACH_ADMIN ICMP6_DST_UNREACH_BEYONDSCOPE ICMP6_DST_UNREACH_ADDR ICMP6_DST_UNREACH_NOPORT ICMP6_TIME_EXCEED_TRANSIT ICMP6_TIME_EXCEED_REASSEMBLY ICMP6_PARAMPROB_HEADER ICMP6_PARAMPROB_NEXTHEADER ICMP6_PARAMPROB_OPTION LUA BOOL: b_debug b_daemon b_server b_ipcache_hostname b_ctrack_disable LUA RUN FILE: /opt/zapret2/lua/zapret-lib.lua LUA RUN FILE: /opt/zapret2/lua/zapret-antidpi.lua LUA RUN FILE: /opt/zapret2/lua/zapret-auto.lua LUA INIT DONE
opening nfq library handle unbinding existing nf_queue handler for AF_INET (if any) binding nfnetlink_queue as nf_queue handler for AF_INET unbinding existing nf_queue handler for AF_INET6 (if any) binding nfnetlink_queue as nf_queue handler for AF_INET6 binding this socket to queue '65302' setting copy_packet mode set receive buffer size to 1048576

---

**2026-04-01T13:58:56 | Routerich**
надо каждый объявить
--blob=quic_3:@/opt/zapret2/files/fake/quic_3.bin

---

**2026-04-01T14:18:54 | Вячеслав**
Подскажите, стоит zapret2+zeroblok, на дефолтных настройках ютуб работает везде кроме тв Samsung (tizen), попробовал стратегии из закрепов ситуация не поменялась.

---

**2026-04-01T14:20:34 | Станислав Земляков**
Вячеслав  rcd27/zapret2-mcp · GitHub
https://github.com/rcd27/zapret2-mcp/blob/main/knowledge/troubleshooting/smart-tv-youtube.md

---

**2026-04-01T15:05:41 | Anna Bagler**
В теме Zapret2 смотрите.

---

**2026-04-01T16:00:47 | Bullet for my valentine Poison**
#!/bin/sh

# Randomized TLS ClientHello desync for Tarkov ports

# --- RANDOM BLOB SELECTION ---
pick_blob() {
    BLOBS="
blob_tls_clienthello_2gis_com
blob_tls_clienthello_2gis_ru
blob_tls_clienthello_alfabank_ru
blob_tls_clienthello_api_photo_2gis_com
blob_tls_clienthello_barclays_co_uk
blob_tls_clienthello_commba_mail_ru
blob_tls_clienthello_escapefromtarkov_com
blob_tls_clienthello_google_com_tlsrec
blob_tls_clienthello_gosuslugi_ru
blob_tls_clienthello_iana_org
blob_tls_clienthello_iana_org_bigsize
blob_tls_clienthello_moskva_taximaxim_ru
blob_tls_clienthello_rutracker_org_kyber
blob_tls_clienthello_sberbank_ru
blob_tls_clienthello_static_lemanapro_ru
blob_tls_clienthello_t2_ru
blob_tls_clienthello_ticket_rzd_ru
blob_tls_clienthello_vk_com
blob_tls_clienthello_vk_com_kyber
blob_tls_clienthello_www_4pda_to
blob_tls_clienthello_www_google_com
blob_tls_clienthello_www_max_ru
"
    set -- $BLOBS
    COUNT=$#
    IDX=$(( RANDOM % COUNT + 1 ))
    eval echo "\${$IDX}"
}

# --- RANDOM MULTIDISORDER POSITIONS ---
pick_md() {
    POS="
1
sniext+1
host+1
midsld-2
midsld
midsld+2
endhost-1
"
    set -- $POS
    OUT=""
    for p in "$@"; do
        if [ $(( RANDOM % 2 )) -eq 1 ]; then
            [ -z "$OUT" ] && OUT="$p" || OUT="$OUT,$p"
        fi
    done
    [ -z "$OUT" ] && OUT="$1"
    echo "$OUT"
}

# --- BUILD BLOB DECLARATIONS ---
build_blob_decls() {
    for b in \
blob_tls_clienthello_2gis_com \
blob_tls_clienthello_2gis_ru \
blob_tls_clienthello_alfabank_ru \
blob_tls_clienthello_api_photo_2gis_com \
blob_tls_clienthello_barclays_co_uk \
blob_tls_clienthello_commba_mail_ru \
blob_tls_clienthello_escapefromtarkov_com \
blob_tls_clienthello_google_com_tlsrec \
blob_tls_clienthello_gosuslugi_ru \
blob_tls_clienthello_iana_org \
blob_tls_clienthello_iana_org_bigsize \
blob_tls_clienthello_moskva_taximaxim_ru \
blob_tls_clienthello_rutracker_org_kyber \
blob_tls_clienthello_sberbank_ru \
blob_tls_clienthello_static_lemanapro_ru \
blob_tls_clienthello_t2_ru \
blob_tls_clienthello_ticket_rzd_ru \
blob_tls_clienthello_vk_com \
blob_tls_clienthello_vk_com_kyber \
blob_tls_clienthello_www_4pda_to \
blob_tls_clienthello_www_google_com \
blob_tls_clienthello_www_max_ru
    do
        echo "--blob=$b:@/opt/zapret2/files/fake/${b#blob_}.bin"
    done
}

BLOB_DECLS=$(build_blob_decls)
RANDBLOB=$(pick_blob)
RANDMD=$(pick_md)

# --- FINAL NFQWS OPTIONS ---
NFQWS_OPT_TARKTEST="$BLOB_DECLS \
--payload=tls_client_hello \
--payload-disable=stun \
--lua-desync=fake:blob=$RANDBLOB:badsum:tcp_ts=-600000:repeats=6 \
--lua-desync=multidisorder:pos=$RANDMD"

alloc_dnum DNUM_TARKTEST
alloc_qnum QNUM_TARKTEST

zapret_custom_daemons() {
    local opt="--qnum=$QNUM_TARKTEST $NFQWS_OPT_TARKTEST"
    do_nfqws $1 $DNUM_TARKTEST "$opt"
}

# --- FIREWALL (Discord Voice excluded, Tarkov fully included) ---
zapret_custom_firewall() {
    local ftcp='-p tcp -m multiport --dports 443,17000:18000,27014:27020,50100:60000'
    local fudp='-p udp -m multiport --dports 443,17000:18000,27014:27020,50100:60000'
    fw_nfqws_post $1 "$ftcp" "$fudp" $QNUM_TARKTEST
}

zapret_custom_firewall_nft() {
    local f='(tcp dport {443,17000-18000,27014-27020,50100-60000} || udp dport {443,17000-18000,27014-27020,50100-60000})'
    nft_fw_nfqws_post "$f" "$f" $QNUM_TARKTEST
}
только ногами не бей😅

---

**2026-04-01T19:51:54 | Yuri Kovalev**
Здравствуйте, подскажите пожалуйста. Установил zapret2 через ZB (галочка в автонастройке) и в разделе "Службы" он так и не появился, хотя в пакетах видно что стоит и сам zapret2 и пакет для него для Luci. Куда смотреть?

---

**2026-04-01T20:28:14 | Yuri Kovalev**
Я отключил YouTube в zapret2 и включил YouTube в zb для awg10, на всех устройствах ютюб работает а на телевизоре не работает

---

**2026-04-01T22:33:49 | ㅤㅤ**
Зачем? По каким скриптам автоматизируется установка Opera Proxy, AWG10, Zapret2 в секции автонастройка можно узнать или это коммерческая тайна?

---

**2026-04-01T23:14:32 | Роман**
По каким скриптам автоматизируется установка Opera Proxy, AWG10, Zapret2 в секции автонастройка можно узнать или это коммерческая тайна?

---

**2026-04-01T23:33:24 | Роман**
zapret

---

**2026-04-01T23:45:13 | Gomer Simpson**
Для ютуба Zapret2 существует. Или Zapret.

---

**2026-04-02T00:14:19 | Артём Фомин**
Пустил YouTube через ZeroBlock/awg10 и всё залетало. Не хочет через Zapret2 нормально работать. Видео грузится очень долго и постоянно зависает.

---

**2026-04-02T00:21:02 | Роман**
Ещё раз, то что откроет прокси (подкоп/zeroblock) - не откроет zapret (грубо говоря). Точечная маршрутизация и дурение разные вещи. Списки из подкопа никак не помогут в запрете.

---

**2026-04-02T10:36:37 | Vadim**
Если не трудно то можно в инструкцию по zapret2 добавить как блобы подбирать.
Хотя бы поверхностно

---

**2026-04-02T11:22:08 | ⓞ ᗰ**
Zapret2 - как запустить Roblox? 🤦🏼‍♀️

---

**2026-04-02T11:23:20 | Bullet for my valentine Poison**
Использовать первый zapret.

---

**2026-04-02T11:27:36 | ⓞ ᗰ**
Только zapret или еще какие-то пакеты надо ставить? Первый раз скриптом ставила, не знаю..

---

**2026-04-02T11:28:14 | Yury Kuzmenko**
https://github.com/StressOzz/Zapret-Manager

---

**2026-04-02T11:34:54 | ㅤ**
Здравствуйте
понадобился мне zapret2 дай думаю поставляю ZB
значится поставил я этот ваш самый ZeroBlock
У меня стоял sing-box 1.13.3 из за него не ставился ZB удалил синг поставил тот что tiny зб установился но мой кфг для синга не работает с tiny
вопрос можно ли поставить ZB на обычный синг?
вопрос зачем конструкция
{
      "type": "direct",
      "tag": "dns-in",
      "listen": "127.0.0.42",
      "listen_port": 53
}
{
        "inbound": "dns-in",
        "action": "hijack-dns"
}
hijack-dns и так перехватит dns
вопрос в zapret2 так сказать есть стратегия "youtube" и "rr_youtube" есть ли разница?
вопрос Blockcheck2 и "поиск стратегий" что лучше?(или это для разного?)

---

**2026-04-02T11:42:35 | A V**
Zapret2 стоит жеж.

---

**2026-04-02T12:08:34 | ㅤ**
кста zapret или zapret2?

---

**2026-04-02T12:12:05 | ㅤ**
ну зачем то zapret2 выпускали же?

---

**2026-04-02T12:17:59 | Bullet for my valentine Poison**
https://ntc.rkn.quest/t/zapret2-обсуждение/21161/802 вот тут почитай, подумай. ПОспрашивай.

---

**2026-04-02T12:19:48 | Карлсончик**
Теперь подбираем стратегии для Ютьюба в zapret2

---

**2026-04-02T12:26:23 | Stanislav Gurov**
https://github.com/bol-van/zapret

---

**2026-04-02T15:34:31 | Александр**
Назрел очередной вопрос,установлен zeroblock zapret2.Нужно зайти на сайт xiaomi.eu,открывается только при включении впн в браузере.Пните в нужном направлении где что включить ,прописать,что бы был свободный доступ.

---

**2026-04-02T15:54:18 | Руслан**
root@RouteRich:~# zapret2-finder--builtin
-ash: zapret2-finder--builtin: not found почему так ?

---

**2026-04-02T16:00:20 | Bullet for my valentine Poison**
/opt/zapret2/zapret2-finder --builtin   -потому что так.

---

**2026-04-02T16:33:54 | Vasilii Pavlenko**
Подскажите пожалуйста, надо устанавливать ZB+Zapret2 из шапки или как сейчас в инструкции, через фильтр-доступные пакеты? Месяц назад помню настраивал на другом роуткре - там подкидывал вручную. Как правильно?

---

**2026-04-02T17:56:45 | Bullet for my valentine Poison**
Я б за Fresa голосовал. Он Zeroblock с Zapretom2 нашаманил.😂

---

**2026-04-02T19:36:29 | Gomer Simpson**
Разбор вредоносного форка Zapret2..

---

**2026-04-02T20:28:31 | HiLLL**
эти? zapret-discord-youtube

---

**2026-04-02T20:30:17 | HiLLL**
На бабочке какие то сборки еще есть. Посмотри по поиску zapret

---

**2026-04-02T20:52:12 | Iceking**
Здравствуйте. На YouTube есть реклама, посмотрел поиском треда, надо отключить youtube, rr_youtube в Zapret2? В ZeroBlock awg YouTube есть в списке, стоит галочка
Правильно все понял или ошибаюсь?

---

**2026-04-02T21:09:49 | Dmitry L.**
Доброго времени суток)

Добрался до следующего этапа с настройкой ZeroBlock

Спасибо за помощь в настройке всем причастным

В итоге вот, что помогло:


После первого запуска настроить на RR

uci set network.lan.proto='static'
uci set network.lan.device='br-lan'
uci set network.lan.ipaddr='192.168.1.2'
uci set network.lan.netmask='255.255.255.0'
uci set network.lan.gateway='192.168.1.254'
uci del network.lan.dns
uci add_list network.lan.dns='192.168.1.254'
uci add_list network.lan.dns='8.8.8.8'

uci set dhcp.lan.ignore='1'

uci delete network.wan
uci delete network.wan6

uci commit network
uci commit dhcp
reboot


По предыстории: подключал RR через lan от основного роутthа и прокидывал шлюз


Собственно вопрос: 
Настроил всё по инструкции "как завести Zeroblock+Zapret2 на дефолтных настройках.", но ютуб не загружается
Подскажите, может по настройкам что-то изменилось с учетом последних событий?

---

**2026-04-02T21:14:33 | Dmitry L.**
Кошмар.. 😄

т.е. zapret2 мне в такой схеме не суждено использовать?

---

**2026-04-02T21:20:32 | Iceking**
То есть убрать список из avg,  а в Zapret оставить как есть?

---

**2026-04-02T21:52:59 | Iceking**
Отключил в ZeroBlock, оставил в Zapret2 - не работает
Отключил в Zapret2, оставил в ZeroBlock - не работает
Включил в Zapret2 и ZeroBlock - YouTube открывается, но с рекламой
Куда смотреть?

---

**2026-04-02T21:53:40 | Святос**
Надо посмотреть на стройку Zapret2

---

**2026-04-02T22:09:18 | Iceking**
Через Zapret2

---

**2026-04-02T22:31:23 | Сергей Ермаков**
Здравствуйте, где можно найти исходники этого?
https://github.com/routerich/packages.routerich/blob/24.10.5/routerich/zapret2_0.9.4.6-r2_aarch64_cortex-a53.ipk

---

**2026-04-02T22:37:53 | Iceking**
Понял, спасибо, почему-то через Zapret2 вообще перестал открываться YouTube, работает только через ZeroBlock

---

**2026-04-02T22:44:05 | Iceking**
Да моя ошибка 100%. Зашел ZeroBlock, секции, квн, списки, убираю галочку YouTube
Zapret2. youtube, rr_youtube со стандартными настройками включены. Еще включено rr_blackhole
Так YouTube работает, только не могу залогиниться (см.видео)

---

**2026-04-02T23:21:46 | Vlad**
Ютуб работал через впн, но хочу, чтоб через Zapret. Удалил из списка впн, запустил запрет. И ничего... Лог пишется, длиннющий, значит делает вид, что работает. Может как за запрет в подкопе должен быть прописан?

---

**2026-04-02T23:23:07 | Alon Zone**
После того как установил zeroblock , zapret 2 , еще что то надо делать ?

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

**2026-04-02T23:44:03 | Артем Погодин**
Устанавливаю по инструкции
Дошел до 7 пункта. 
Минут 10 уже прошло, а пункта zapret2 в службах не появилось. При этом установлен в автозапуске. Это норм?

---

**2026-04-03T13:51:14 | iProxx**
Всем привет! Сегодня после ночного отключения электроэнергии обнаружил что на Роутериче не пашет ни один обход.
Зайдя вебморду увидел отвал zapret, opera proxy и sing box.
Вручную перезапустил службы, все поднялось. 
Вообще очень странно, ведь в настройках служб включен автозапуск.
Вопрос, как  можно автоматизировать это все без ручного вмешательства?

---

**2026-04-03T14:34:13 | Алексей Сергеевич**
1. Накатить последнюю пошивку (сбросив к заводским настройкам) и поставить

ZeroBlock:
opkg update && opkg install $(opkg list | grep zeroblock | awk '{print $1}' | xargs -n999)

2. Включить в "Автонастройке": 
Opera Proxy
AWG10
Zapret2
Xray
TrustTunnel
Автозагрузка новой стратегии Zapret2

3. В "Секции маршрутизации": 

Opera Proxy:
AI
Block
Geoblock
Google Play

 AWG10:
Messengers
Meta

4. Для стабильной работы WhatsApp и Telegram добавить в Opera Proxy списки:

### IP
3.0.0.0/10
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
5.28.192.0/18
91.105.192.0/23
91.108.4.0/22
91.108.8.0/22
91.108.12.0/22
91.108.16.0/22
91.108.20.0/22
91.108.56.0/22
95.161.64.0/20
149.154.160.0/20
185.76.151.0/24

### Domain
bintray.com
wa.me
whatsapp-plus.info
whatsapp-plus.me
whatsapp-plus.net
whatsapp.biz
whatsapp.cc
whatsapp.com
whatsapp.info
whatsapp.net
whatsapp.org
whatsapp.tv
whatsappbrand.com
cdn-telegram.org
comments.app
contest.com
fragment.com
graph.org
nicegram.app
quiz.directory
stel.com
t.co
t.me
tdesktop.com
telega.one
telegra.ph
teleg.xyz
telegram-cdn.org
telegram.ai
telegram.app
telegram.asia
telegram.biz
telegram.cloud
telegram.cn
telegram.co
telegram.com
telegram.de
telegram.dev
telegram.dog
telegram.eu
telegram.fr
telegram.host
telegram.in
telegram.info
telegram.io
telegram.jp
telegram.me
telegram.net
telegram.org
telegram.qa
telegram.ru
telegram.services
telegram.solutions
telegram.space
telegram.team
telegram.tech
telegram.uk
telegram.us
telegram.website
telegram.xyz
telegramapp.org
telegramdesktop.com
telegramdownload.com
telesco.pe
tg.dev
tg.org
tgram.org
torg.org
tx.me
usercontent.dev

---

**2026-04-03T14:39:49 | Роман**
Установить запрет 2 через пакеты. Система -> пакеты -> обновить списки -> в поле фильтр вписать zapret2 -> установить 2 пакета сверху вниз.1

---

**2026-04-03T15:22:05 | ㅤ**
Здравствуйте
как поставить zapret1/2 и sing-box?
вообщем я поставил синг и запрет всё по отдельности работает а вместе нет
когда запущенны вместе то сайты по сингу (те что идут в прокси) работают а те что на direct (в синге) не работают
мне кажется дело в маршрутах и во всём таком, это ведь так?

---

**2026-04-03T15:22:10 | Vlad Maker**
Добрый день. Поставил ZeroBlock и Zapret2 пару дней назад, дефот настройки. Все работало без проблем. 
Сегодня не грузит Ютуб в браузере ПК и Телефона(в приложении работает). После перезагрузки роутера в Хроме на ПК какое то время работает. Хэлп.

---

**2026-04-03T15:28:44 | Anna Bagler**
Пробуйте другую стратегию из здесь представленных или подбирайте свою. Напишите задачу на перезапуск zapret2 в планировщик.

---

**2026-04-03T15:56:58 | Akira Yamaoka**
Привет. А где почитать про zeroblock и zapret2? Ну что это? чем отличается от скрипта #5, в каких случаях что лучше использовать? Есть такое описание где то?

---

**2026-04-03T16:04:46 | Роман**
zapret 2 - дурилка, zerpblock - прокси/впн - разные вещи, соответственно сферы применения разные.

---

**2026-04-03T17:00:53 | Камиль**
Речь же про https://github.com/rcd27/zapret2-mcp ? Этот mcp не получилось с https://github.com/QwenLM/qwen-code подружить?

---

**2026-04-03T17:25:37 | Станислав Земляков**
Проще говоря, вы докидываете контекст по zapret2 в ИИ модель

---

**2026-04-03T20:11:08 | Vasa**
без мам пап и подкопов..
амнезия тут вроде 1,5 версия
https://github.com/GubernievS/AntiZapret-VPN

---

**2026-04-03T20:19:15 | Дмитрий**
Всем привет, не подскажете, zapret 2 распространяется на Discord и Телеграмм?
Я просто в этом мало что понимаю

---

**2026-04-03T21:26:40 | Bullet for my valentine Poison**
Ток zapret1

---

**2026-04-04T00:16:11 | Роман**
Будьте добры подскажите еще,  все делал по пунктам,  протыкал первые 4 пункта,  сохранил применил. Прошло уже минут 15,  но Zapret2 в службах так и не появился :(

---

**2026-04-04T10:44:18 | Сергей Матвеев**
Не могу поставить zapret2. Сделал все по инструкции. В службах не появляется.

---

**2026-04-04T10:53:24 | Bullet for my valentine Poison**
Система-пакеты. В фильтр вписать Zapret2. Еще режим инкогнито. Или открыть с телефона раздел службы

---

**2026-04-04T12:14:50 | Dmitriy**
Здравствуйте. почему то в этой инструкции про Ютуб не увидел. Понимаю, что это по чатси zapret2, но как при этом именно управление трафиком Ютуба через zapret2 осуществляется?

---

**2026-04-04T12:26:26 | Dmitriy**
а может кто подсказать , можно ли на телефоне реализовать аналогичную схему как на роутериче с zapret2 для ютуба + zeroblock ? просто одновременно включить сразу vpn клиент и byebyedpi нельзя или это проще через на роутере накатить и через tailscale?

---

**2026-04-04T12:26:56 | Anna Bagler**
А если отключить zb и zapret2 открывается? У меня, например, ругается на ошибку базы данных.

---

**2026-04-04T12:27:08 | Routerich**
root+zapret+vpn

---

**2026-04-04T12:32:52 | Routerich**
root ваш аппарат, дальше zapret android magisk

---

**2026-04-04T12:58:18 | Сергей Матвеев**
Понятно, я просто не понял что надо сделать в zapret что бы roblox работал

---

**2026-04-04T14:08:52 | Loraool**
Добрый день. Вопрос, увидел в пакетах "Adguard home". Насколько эффективно он работает? Или лучше на устройство ставить блокировщик рекламы, а не на роутер. Не будет ли конфликтов в zeroblock+zapret2?

---

**2026-04-04T14:55:05 | Алексей Сергеевич**
Там есть стратегия в zapret2 rr_default или rr_YouTube попробуйте ту или ту настроить, потом перезапустить Zapret2

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

**2026-04-04T16:12:24 | Виталий Александрович**
подскажите пожалуйста списки в zapret2 сами обновляются или надо руками обновлять?

---

**2026-04-04T16:17:46 | Виталий Александрович**
Подскажите еще пожалуйста на счет пакета zapret2-finder
не нашел его в пакетах для установки

---

**2026-04-04T16:31:01 | Vasa**
да, но шалости. описанные тут
сплит тунелинг там итд
https://github.com/GubernievS/AntiZapret-VPN

---

**2026-04-04T20:09:16 | Anna Bagler**
В теме zapret2 cмотрите стратегию и список доменов для него.

---

**2026-04-04T21:41:06 | труляля🧑‍🦲#отвальный #mimilover #create #Print("helloworld")**
Проблема на 7 шаге. Zapret2 так и не появился. В чем может быть проблема?

---

**2026-04-04T22:10:12 | Константин Волчек**
Роман, у меня похожая проблема, только не работает дискорд, а не ютуб. До этого делал стандартную установку ZeroBlock + Zapret 2

---

**2026-04-04T23:23:19 | Vasa**
https://github.com/GubernievS/AntiZapret-VPN/tree/main/setup/root/antizapret/download

---

**2026-04-05T00:48:51 | Митсумото Сузуки**
@ded_ikar делаю все по манулу, подождал минут 10, почистил кэш, перезашел в роутер, но Zapret 2 не появляется в службах

---

**2026-04-05T01:57:22 | Anna Bagler**
Секции маршрутизации в zeroblock, awg, cписок мессенджеров.
По discord есть стратегии в теме zapret2. Можете его отключить и остановить. Вернуть просто запрет и ваши стратегии.

---

**2026-04-05T01:57:53 | Роман**
https://github.com/StressOzz/Zapret-Manager
Для вас самый подходящий вариант.

---

**2026-04-05T02:49:46 | Anna Bagler**
Можно попробовать готовые стратегии из темы Zapret2 или для начала перезапустить zapret2 и посмотреть.

---

**2026-04-05T08:09:42 | Константин Волчек**
пока пытался настроить работу дискорда через zapret2 умер ютуб

---

**2026-04-05T08:38:16 | Константин Волчек**
сделал все по основному гайду zeroblock + zapret2

---

**2026-04-05T08:44:14 | Vasilii Pavlenko**
Добрый день. Подскажите пожалуйста. Живу в Крыму. Установлен RR USB3. 0. Поднято ZB+Zapret2. Есть саундбар Samsung hw-q930d, брал из Китая. Девайс не хочет обновиться по сети. Периодически пишет, что есть обновление, прожимаю обновить - пишет нечего обновлять. Но версия ПО точно не последняя, есть более поздняя. На форуме много народа пишет, что самсунг блокирует работу SmartThings в России и нужен впн (у меня есть свой на 3x-ui на vps, секцию запускал в zb но ситуацию не спасло) . Явно надо подсунуть  обход блока. В журнал url's роутера вижу такие обращения с саундбара. Куда эти сайты правильно прописать (какие секции и какой раздел),. Я так думаю в zb-opera Помогите плиз

---

**2026-04-05T09:29:38 | Константин**
Подскажите пожалуйста, если установлен Zeroblock и Zapret 2 то пс 5 полную маршрутизацию сделать в оперу или aw10?
Спасибо

---

**2026-04-05T10:51:51 | D I**
Уважаемые, вопрос а в чем принципиальная разница Zapret(2)/ZeroBlock/PodKop? и что выбрать, если ничего не стоит/стояло до?

---

**2026-04-05T10:53:09 | Nick**
Zeroblock  и zapret2
В комплекте

---

**2026-04-05T11:02:32 | Дмитрий**
прописал только в одну секцию awg10, добавил там еще галочку на youtube. В Zapret 2 убрал галочки с youtube

---

**2026-04-05T11:16:34 | Andrey Kuznetsov**
Всем привет! Вчера стал обладателем сего чуда. Из коробки заработал Ютуб на компе, но на ТВ не работал. Установил zapret2 и пакет ui. Как слепой котенок догадался что Ютуб из коробки обеспечивает YouTubeunblock и они они конфликтуют с запретом. После стопа unblock завелся и на телеке только с запретом. Есть ли инструкция к этому ui zapret2? Что то не могу понять как применять стратегии да и вообще как с ним работать. До этого только пытался на viva подымать на консоли, но после пары дней мучений решил найти просто роутер с OWRT.
Дайте инструкцию, пожалуйста, с настройкой через ui запрета2 если она существует

---

**2026-04-05T12:51:03 | Navisal**
на роутере Routerich штатными средствами поднят OpenVPN сервер, подключено несколько клиентов, которые прекрасно ходят в инет через Zeroblock и Zapret2.
Вопрос: Как можно посмотреть статус OpenVPN клиентов? Желательно через Luci, через морду какую-нибудь ) Ну или просто командой

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

**2026-04-05T13:59:09 | 🌶️🌶️**
Анализ запущен: 2026-04-05 13:56:33
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.6.13 | YouTube IP:  198.18.4.143

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.68 MB / ↑0.17 MB
  Пинг (ya.ru via awg10): ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (2a02:6b8::2:242): 56 data bytes
  Программы в автозапуске: zeroblock sing-box zapret2 opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200 OK) [tlsv1.3] [try: 2]
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:     127.0.0.1:53
    Name:       youtube.com        Address: 198.18.4.143
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | РАЗРЕШЁН
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
/dev/fd/64: line 938: root@RouteRich:~# 
root@RouteRich:~# syntax error: unexpected end of file (expecting "done")


2 вопроса: почему ошибка пинга я.ру и почему ошибка синтаксиса в конце?

---

**2026-04-05T15:37:12 | Anna Bagler**
Если вам нужен именно первый запрет для дальнейших манипуляций, то галочками zapret2 и его стратегии не ставьте.

---

**2026-04-05T16:40:55 | Anna Bagler**
Смотрите для zapret2 cтратегию для дискорд в соответствующей теме. Для игр свой vless, hy2 и домены/подсети в zеroblock.

---

**2026-04-05T17:26:33 | Данила Ступин**
Не знаю делал ли так кто-нибудь уже или нет, но я (с помощью ИИ) адаптировал стратегию v1 из Zapret-Manager для zapret2 (может кого заинтересует).

Параметры стратегии можно увидеть на скриншоте.

Опции NFQWS:
--payload=tls_client_hello,http_req
--lua-desync=multisplit:pos=2:seqovl=681:seqovl_pattern=blob_stun

Для её работы нужно обязательно зайти в меню "Blobs" (кнопка под списком стратегий) и включить там blob_stun (по умолчанию он выключен) -> сохранить -> применить.

Кроме того, нужно в самом запрете создать список исключений (у меня он называется user_exclude3) и скопировать туда список доменов отсюда, после этого сохранить->применить.

И всё должно заработать... Для YouTube отдельная стратегия не нужна (стратегия работает в режиме catch-all).

Отвечая на вопрос "Зачем это нужно и чем это лучше стандартной стратегии?", могу сказать, что у меня v1 работает стабильнее default и rr_default (со стандартными у меня некоторые сайты не открывались). Но опять же это всё субъективно и варьируется от провайдера к провайдеру.

---

**2026-04-05T17:36:24 | Никита**
Тормозит приложение ютуба на iPhone . Ютуб стоит через zapret2. Подскажите пожалуйста как сделать чтобы не лагало?🙌🏻

---

**2026-04-05T18:07:41 | Алексей**
Перешёл с шитого cudy на routerich. Подкупило 512 оперативы и конечно же активная поддержка своего продукта! Отдельное спасибо за zb и zapret2!🤝

---

**2026-04-05T20:40:43 | Илья**
Еще один наверное странный вопрос. Почему после автонастройки zeroblock не появляется пункт zapret 2

---

**2026-04-05T20:46:41 | Routerich**
Система - пакеты - вкладка установлено - в фильтре напишите zapret2 и покажите скрин

---

**2026-04-05T21:33:32 | Виталя**
Всем привет, только забрал с озона роутер подскажите пожалуйста что лучше ставить Zeroblock+Zapret2 или  скрипт 5 ?

---

**2026-04-05T21:50:25 | Вадим Ободов**
Всем привет.Может кто сталкивался с такой проблемой.Стоит прошивка 24.10.5 и установил zeroblock и zapret2 .Всё работает, но ютуб на телевизоре lg c1 перестал работать.Ютуб через zapret2 работает.Ютуб на пк и смартфонах прекрасно работает

---

**2026-04-05T21:51:27 | Bullet for my valentine Poison**
Пробуйте стратегии из закрепа темы Zapret2

---

**2026-04-05T22:05:02 | Вадим Ободов**
Всем привет.Может кто сталкивался с такой проблемой.Стоит прошивка 24.10.5 и установил zeroblock и zapret2 .Всё работает, но ютуб на телевизоре lg c1 перестал работать.Ютуб через zapret2 работает.Ютуб на пк и смартфонах прекрасно работает

---

**2026-04-05T22:32:36 | Роман**
https://github.com/StressOzz/Zapret-Manager
Один скрипт в терминал, там разберётесь. И не забыть отключить з2 и его автостарт.

---

**2026-04-05T22:35:57 | Bullet for my valentine Poison**
Так он на Zapret1 будет, думаю там без проблем будет работать. Я себе поставил в лаунчере автоопределение и не страдаю.

---

**2026-04-05T22:52:30 | Ярослав**
Вроде работает. Я пошел на сайт iplist.opencck.org и оттуда взял все IP и домены, внес их в списки и разнес списки по соответствующим разделам на Zapret2.
Далее там уже были прописаны Опции NFQWS по дефолту:
--payload=tls_client_hello
--in-range=-s5556 --lua-desync=circular:fails=3:maxtime=60
--in-range=x
--lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=1
--lua-desync=multisplit:pos=2,sld:seqovl=620:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=1
--lua-desync=multidisorder:pos=1,midsld:strategy=2
--lua-desync=tls_client_hello_clone:blob=cloned_tls:fallback=fake_default_tls:strategy=3
--lua-desync=fake:blob=cloned_tls:optional:tcp_seq=10000000:tcp_ack=-66000:repeats=2:tls_mod=rnd,dupsid,sni=fonts.google.com:strategy=3
--lua-desync=multidisorder:pos=1:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=3
--lua-desync=fake:blob=0x00000000:tcp_seq=-10000:tcp_ack=-66000:strategy=4
--lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:strategy=4
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=fonts.google.com:strategy=4
--lua-desync=multidisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=4
--lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=5
--lua-desync=fakeddisorder:pos=method+2:tcp_md5:strategy=6
--lua-desync=tls_client_hello_clone:blob=cloned_tls:fallback=fake_default_tls:strategy=7
--lua-desync=fake:blob=cloned_tls:optional:tcp_ts=-600000:tls_mod=rnd,dupsid,sni=www.google.com:strategy=7
--lua-desync=hostfakesplit:ip_id=zero:host=www.google.com:altorder=1:tcp_ts=-600000:strategy=7
--lua-desync=hostfakesplit:host=google.com:tcp_ts=-600000:strategy=8
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_ts=-600000:repeats=6:strategy=9
--lua-desync=fakedsplit:ip_id=zero:pattern=0x00:tcp_ts=-600000:strategy=9
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_ts=-600000:repeats=8:strategy=10
--lua-desync=multisplit:pos=1:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:ip_id=zero:strategy=10
--lua-desync=multisplit:pos=1:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:ip_id=zero:strategy=11
--lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=12
--lua-desync=multisplit:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=13
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=fonts.google.com:strategy=14
--lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=14
--lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=14
--lua-desync=multidisorder:pos=7,sld+1:nodrop:strategy=15
--lua-desync=multidisorder:pos=1,midsld,endhost-1:strategy=16
--lua-desync=fake:blob=0x00000000:tcp_seq=-10000:tcp_ack=-66000:repeats=2:strategy=17
--lua-desync=fake:blob=fake_default_tls:tcp_seq=-10000:tcp_ack=-66000:repeats=2:tls_mod=rnd,dupsid,sni=www.google.com:strategy=17
--lua-desync=multisplit:pos=1,midsld:strategy=17
--lua-desync=multidisorder:pos=1,midsld:strategy=18
--lua-desync=multisplit:pos=1,2:seqovl=4:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=19
--lua-desync=multidisorder:pos=2,5,105,host+5,sld-1,endsld-5,endsld:strategy=20
--lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=21
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=21
--lua-desync=multisplit:pos=2,sld:seqovl=2108:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=21:final

---

**2026-04-06T00:14:34 | Роман**
Нормальный vless не нуждается ни в каких обмазках. Если вам нужно дурить Ютуб - устанавливайте это  - https://github.com/StressOzz/Zapret-Manager и настраивайте, там проще чем во втором.

---

**2026-04-06T03:45:55 | Михаил**
Интернет восстановил ( позже напишу как добился этого) .
Скажите по мануалу про zero block + zapret 2 не могу найти раздел Секции маршрутизации ( 8 пункт мануала )

---

**2026-04-06T08:36:41 | Сергей Ермаков**
это из документации zapret2 с github'а?

---

**2026-04-06T09:51:19 | Bullet for my valentine Poison**
Ты в теме Zapret2, тут токсичная и не дружелюбная атмосфера. Как сам Zapret2))

---

**2026-04-06T11:53:04 | Данила Ступин**
Информация для "счастливых" обладателей умной техники Xiaomi. Как вы уже могли заметить, устройства умного дома перестали подключаться к сети из-за действий "конторы весельчаков".

После долгих поисков решения я наткнулся на информацию с 4pda. Необходимо добавить данные подсети в любую секцию zeroblock/podkop (warp/opera/vless). Zapret мне не помог в данном случае.

107.155.51.0/24
107.155.52.0/24
107.155.53.0/24

После проброса этих сетей в zeroblock (warp) у меня всё заработало. Xiaomi вроде обещали это починить конечно, но ждать можно долго)

---

**2026-04-06T12:00:52 | Данила Ступин**
Я вчера его часа 4 пытался починить на Zapret2, но у меня ничего не получилось (никакие стратегии не помогают). В итоге психанул и просто прокинул подсети с доменами в zeroblock) Хотя вроде как по заверениям автора Zapret-Manager всё должно работать нормально со стратегией v1 + gamefilter (но там zapret1).

---

**2026-04-06T12:03:07 | Роман**
Там комплексное решение в zapret manager, его просто так (как мне кажется) не перенести в з2.

---

**2026-04-06T12:11:54 | Vasa**
а конфиг \ маскировка AWG2 какая?

это изучал?
https://publish.obsidian.md/zapret/amnezia-2-0/reference#%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B+%D0%BA%D0%BE%D0%BD%D1%84%D0%B8%D0%B3%D1%83%D1%80%D0%B0%D1%86%D0%B8%D0%B9

---

**2026-04-06T12:12:54 | Vasa**
даже лучше отсюда
https://publish.obsidian.md/zapret/amnezia-2-0/reference#%D0%9F%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B+%D0%BA%D0%BE%D0%BD%D1%84%D0%B8%D0%B3%D1%83%D1%80%D0%B0%D1%86%D0%B8%D0%B9

---

**2026-04-06T13:30:33 | Gomer Simpson**
Вот такое имею в планировщике: 
00 5 * * * service zeroblock restart
11 5 * * * service zapret2 restart
15 5 * * * service tailscale restart

---

**2026-04-06T13:43:37 | Routerich**
Здравствуйте.
Если у вас ютуб через Zapret2 то так не будет работать.

---

**2026-04-06T13:44:20 | Routerich**
Отключайте zapret2, добавляйте список в zeroblock и проверяйте

---

**2026-04-06T13:48:23 | труляля🧑‍🦲#отвальный #mimilover #create #Print("helloworld")**
Чем отличается podkop от zapret и от zapret 2?

---

**2026-04-06T13:50:02 | Routerich**
Podkop средство маршрутизации
Zapret, Zapret2 это дурилки dpi

---

**2026-04-06T14:06:49 | Routerich**
Можно через родительский контроль блокнуть домен ютуб,как вариант и проверить.
Если zapret2 отключать не хотите и переносить ютуб в zeroblock

---

**2026-04-06T15:26:26 | Anna Bagler**
От ваших блокировок многое зависит. Для запрет вы можете подобрать стратегии https://t.me/routerich/3845/509958
Попробуйте zeroblock и zapret2, но со сбросом роутера.

---

**2026-04-06T15:27:45 | Routerich**
Ну тогда удалить из Podkop список YouTube, и установить zapret2 и подбирать стратегию под него

---

**2026-04-06T15:37:09 | Anna Bagler**
От YouTube через awg мы избавляемся, если вы пустите его в свой vless или zapret2.

---

**2026-04-06T17:36:14 | Anna Bagler**
Если YouTube убираем из awg, то подбираем стратегию для zapret, если возвращаем в awg, то отключаем и останавливаем zapret.

---

**2026-04-06T18:04:40 | Routerich**
Тогда попробуйте стопнуть Podkop, Zapret открывается приложение?

---

**2026-04-06T19:38:17 | Александр Юг**
Доброго времени суток! Подскажите, что сейчас лучше поставить на новый роутер Скрипт 5 или zeroblock+zapret2?

---

**2026-04-06T19:57:28 | Bullet for my valentine Poison**
Я на 256 сижу (полная прошивка) + Zeroblock c Zapretom. Всегда занято 150-160мб. И проблем как бы не наблюдаю. Учитывая что у меня сейчас Zapret и Zeroblock не вшиты в прошивку.

---

**2026-04-06T21:32:30 | Loraool**
Добрый вечер. Позавчера настроил zb + zapret2, работало отлично, сейчас отвалился ТГ, висит обновление, остальное все работает. С чего начать исправление? Перезагрузить роутер?

---

**2026-04-06T22:15:17 | Дмитрий Григорьев**
ZB + Zapret2

---

**2026-04-06T22:30:30 | Gomer Simpson**
Ютуб - только в православный Zapret. (Zapret2)

---

**2026-04-07T04:27:31 | Yrii**
Единственное что у меня был уже установлен zapret2.

---

**2026-04-07T07:51:18 | Aleksei**
Ребята, а почему могут слететь галки в стратегиях Zapret2: rr_default, rr_youtube? Остается только rr_blackhole.

Из-за включенной Автозагрузка новой стратегии в Zeroblock?

Как раз после 3 утра часть сайтов отвалилась вместе с галками в zapret2

---

**2026-04-07T08:38:24 | Данила Ступин**
Здравствуйте! Если zapret2 работает в режиме catch-all и при этом в zeroblock так же настроены секции на определенные домены, то будет ли конфликт без настроенных исключений в запрете или это не имеет значения?

---

**2026-04-07T08:57:17 | Routerich**
И если в zeroblock его нет, то значит он через Zapret2 идёт?

---

**2026-04-07T09:04:34 | -Miracle**
доброго времени, подскажите пожалуйста при покупке и настройке роутера начала появляться такая беда. Есть ли решение ?
стоит Zero block,Zapret.

---

**2026-04-07T09:44:03 | Rom@n**
да у меня даже варп обернут скриптом в zapret2

---

**2026-04-07T09:55:48 | 𝓐𝓵𝓮𝓴𝓼𝓪𝓷𝓭𝓻**
Привет,кто подскажет список действующих доменов и ip адресов youtybe чтобы подобрать стратегию для zapret2

---

**2026-04-07T10:03:10 | Владимир Волков**
Система - пакеты - остановить youtubeunblock, zapret, zeroblock, podkop - попробовать снова

---

**2026-04-07T10:15:35 | Routerich**
1. Zapret2

2. zeroblock + vless

---

**2026-04-07T10:22:13 | Rom@n**
Но у меня zapret2

---

**2026-04-07T10:24:16 | Rom@n**
вот от сюда https://github.com/bol-van/zapret/blob/master/init.d/custom.d.examples.linux/50-wg4all

---

**2026-04-07T10:25:00 | Routerich**
https://github.com/bol-van/zapret2/blob/master/init.d/custom.d.examples.linux/50-wg4all

---

**2026-04-07T11:02:59 | Rom@n**
awg10 вообще не трогал с перепрошивки, но да в zapret2 запихал скрипт не правильный, но теперь то я его удалил, да и запрет отключил для проверки. Так сейчас все перезагружу и еще раз проверю

---

**2026-04-07T11:19:19 | Vitalii Nikopolidi**
Приветствую, пытаюсь разобраться что такое этот Zapret2
Если в Zeroblock примено понятно что есть какие-то списки с хостами и тд, то для чего нужен Zapret 2 и на какие сервис как он применяется. понимаю что он для обхода DPI, но как и куда он применяется, весь трафик прооняет или как

 и куда пихать такие скриты
https://t.me/routerich/462347/583412

это для ютуба специфично?

---

**2026-04-07T11:39:16 | Константин**
выполнил команду Анализ запущен: 2026-04-07 11:37:16
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
  Facebook IP:  198.18.29.37 | YouTube IP:  64.233.161.190

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.68 MB / ↑0.20 MB
  Пинг (ya.ru via awg10): 33.025 / 35.832 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock zapret2 opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200 OK) [tlsv1.3] [try: 1]
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock              awg10 (vpn): anime,googleplay,messengers,meta,news,porn,socials,video
  zeroblock          opera (prx out): ai,geoblock
  zeroblock        DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8
  Полностью маршрутизированные IP-адреса включены!
  zeroblock.Ps5.fully_routed_ips='192.168.1.247' '192.168.1.192'
  Версия zeroblock: 0.7.1-r33

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.25 | RAM: 26% | NAND: 43% занято / 38.6M доступно
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

root@RouteRich:~#

---

**2026-04-07T12:05:05 | Routerich**
zapret2 rr_blackhole

---

**2026-04-07T12:13:18 | Роман Лобарев**
Добрый день!  Роутер стоит в районе где "белый список" 100%, есть смысл пытаться Zeroblock или zapret2 настраивать? или только vless подключить через лазейку остается?

---

**2026-04-07T12:36:27 | Георгий Новожилов**
Спасибо большое за помощь с обновлением прошивки и установкой ZeroBlock + Zapret2! Всё завелось с первого раза на всех устройствах: мануал очень подробный

У меня остался последний вопрос: на прошлой версии прошивки у меня были проставлены форварды на домашний сервер, в том числе и WireGuard. Прокинул все необходимые порты - работают и SSH, и DNS, но WG не отдаёт пакеты:

# из локалки пингую сервер через публичный привязанный домен
$ nmap -sU -p 51820 mydns.org
Starting Nmap 7.98 ( https://nmap.org ) at 2026-04-07 12:27 +0300
Nmap scan report for mydns.org (my ip)
Host is up (0.0010s latency).

PORT      STATE         SERVICE
51820/udp open|filtered unknown

Nmap done: 1 IP address (1 host up) scanned in 1.40 seconds

Подскажите, пожалуйста, нужно ли что-то где-то менять? Как я понимаю, то трафик пришёл на сервер, но отдавать не получается

---

**2026-04-07T13:07:47 | Teleghost**
А где эталонный скрипт для него? 
Я попробую, когда снова поеду к родным. С podkop+zapret и стандартными настройками скрипта 5 в Минске не открывается много сайтов, которые работают в Москве. Приходится отключать.

---

**2026-04-07T13:23:18 | Routerich**
так же остановите и отключите zapret, либо уберите youtube из Podkop

---

**2026-04-07T14:10:21 | Vadim**
Привет! Только получил роутер и конечно же судорожно принялся устанавливать все подряд из этого форума - и скрипт №5, и Zeroblock, и Zapret2. Подскажите, плиз, для тупых - выполнения скрипта №5 достаточно для базового пользования? В Zeroblock лезть не нужно было?
Нужно ли как-то удалять пакеты и откатывать установки/ресетить роутер или достаточно отключить эти службы?

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

**2026-04-07T18:06:49 | Алексей Сергеевич**
Zapret2 нужен для обхода DPI, обычно используют для YouTube так как заворачивать его в Opera Proxy или AWG10 не рентабельно. Opera Proxy используется для обхода блокировок с российских ip адресов(ai, geoblock). Awg10 для обхода блокировок РКН(Telegram, WhatsApp и тд.)

---

**2026-04-07T18:43:54 | Николаич**
Здравствуйте. Перестал работать Ютуб на Zapret 2, настройки дефолтные. Как реанимировать подскажите плиз...

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

**2026-04-07T19:08:46 | Vasa**
привет. я бы настраивал - антизапрет. должен работать плюс \ минус из коропки
https://github.com/GubernievS/AntiZapret-VPN - тут же есть ТГ группа

По белым спискам. Тут скорее всего да, только xkeen + покупной ключ
https://github.com/Corvus-Malus/XKeen -  там тоже есть ТГшная группа

белые списки ты не обойдешь сам, если IP твоего VPS не входит в этот список собтсвенно)

---

**2026-04-07T19:48:32 | Никита**
Привет всем. Я новичок в этой теме, поэтому прошу сильно не ругать.

Подскажите, пожалуйста, как сделать так, чтобы YouTube работал через Zapret 2 без лагов. Сейчас он у меня очень сильно тормозит: видео долго грузятся, подвисают, нормально смотреть почти невозможно. Сам я пока не понимаю, в чем проблема и как это правильно настроить.

Если кто-то может объяснить простыми словами, что и где нужно проверить или поменять, буду очень благодарен.

---

**2026-04-07T20:37:23 | Максим**
Новую стратегию мне помогли поставить, ZeroBlock и Zapret2

---

**2026-04-07T21:31:54 | Alex_Jester**
Обновил вручную через меню пакеты zeroblock и zapret2, при их обновлении выдавало ошибки, там было сказано, что-то про то что конфиги не совпадают. Так и должно быть? Нужно просто проигнорировать ошибки?

---

**2026-04-07T22:05:35 | ARTEM**
Я запустил эту команду 
"opkg list-installed | awk '{print $1}' | while read -r pkg; do
  if opkg info "$pkg" | grep -q 'install ok installed'; then
    opkg remove --autoremove "$pkg" 2>/dev/null || true
  fi
done"
 хотел удалить старые конфигурации zapret так как он каждый раз востанавливается при настройке теперь у меня постоянно висит первоначальная настройка на роутере как исправить ?

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

**2026-04-07T23:21:20 | Alex_Jester**
Надо ли перезагружать роутер при обновлении пакетов zeroblock и zapret 2, или это лишнее?

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

**2026-04-08T06:57:42 | Виталий**
День добрый. Получил вчера роутер. Обновил, поставил zeroblock и zapret2. Все отлично, но не работает стимовская версия albion. При этом если запустить awg на компе, то все работает. Подскажите пожалуйста, может кто сталкивался, куда и что прописать чтобы заработало? =)

---

**2026-04-08T08:58:27 | Routerich**
ну это уже надо смотреть в других службах, youtubeunblock, zapret,zapret2 в зависимости от того что установлено

---

**2026-04-08T10:14:06 | Routerich**
Здравствуйте.
удалить и стопнуть и отключить автозапуск zapret, потом установить zapret2

---

**2026-04-08T10:48:45 | Александр Король 👑**
Добрый день! Являюсь владельцем устройства с марта. Во первых спасибо за прекрасный девайс. Во вторых есть ряд вопросов, причём достаточно нубских. Сразу после получения обновил все пакеты и поставил zapret, zapret2, podkop и zeroblock. В принципе из того что нужно: tg, wa, youtube, insta, детям сервера brawl stars, торрент-трекеры. И вроде все более менее работает, но каждый день приходится перезапускать службы (в частности podkop) чтобы стали доступны торренты. Может я что-то не так сделал? Куда глянуть?

---

**2026-04-08T12:25:03 | Никита**
Привет всем. Я новичок в этой теме, поэтому прошу сильно не ругать.

Подскажите, пожалуйста, как сделать так, чтобы YouTube работал через Zapret 2 без лагов. Сейчас он у меня очень сильно тормозит: видео долго грузятся, подвисают, нормально смотреть почти невозможно. Сам я пока не понимаю, в чем проблема и как это правильно настроить.

Если кто-то может объяснить простыми словами, что и где нужно проверить или поменять, буду очень благодарен.

---

**2026-04-08T12:38:04 | Никита**
Есть инструкция как правильно настроить zapret2?

---

**2026-04-08T13:04:15 | Necessary**
Не появляется окно Zapret2

---

**2026-04-08T13:11:37 | Bullet for my valentine Poison**
"как правильно настроить zapret2?" я просто туда даже не смотрел))

---

**2026-04-08T13:21:46 | Routerich**
а может zapret, youtubeunblock мешают?

---

**2026-04-08T14:15:41 | Роман**
Нашло бой менее чем за минуту, пинг до 50, нормально играется.
Установлен zeroblock, zapret 2.

---

**2026-04-08T14:19:15 | Max**
Вопрос в тему-вацап сообщения уходят/приходят, но не скачиваются картинки/ файлы. Настройки стандартные, zeroblock zapret2. Что можно сделать?

---

**2026-04-08T15:54:03 | Routerich**
Что-то web ui от Trasnmission отвалился после обновления zeroblcok и zapret, может конечно так совпало. Не подскажете куда копать?

---

**2026-04-08T17:35:29 | Alex_Jester**
Итак пошаговый мануал для владельцев Routerich, как завести Zeroblock+Zapret2 на дефолтных настройках.
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки" и ждем, закрываем появившуюся табличку нажав на кнопку "Закрыть".
3. Вводим в окне "Фильтр" (слева) Zeroblock. Внизу должны появиться два пакета: Zeroblock и luci-app-zeroblock.
4. Нажимаем кнопку "Установить" напротив каждого пакета.(Первым идет Zeroblock, а затем luci-app). В появившемcя окне жмем еще раз установить. После завершения закрываем окно. 
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4. Жмем по очереди на кнопки: сохранить и применить.
7. Далее ждем примерно 5 минут, выходим и обратно входим в интерфейс роутера. В разделе Службы должен появиться пункт "Zapret2".
8. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
9. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
10. Проверяете работу Youtube на всех устройствах. (так же желательно в браузерах отключить функцию "Частный/безопасный DNS")

---

**2026-04-08T17:48:27 | Артём Фомин**
Народ, а есть какой-нибудь гайд, как правильно искать стратегии в Zapret2?

---

**2026-04-08T18:04:46 | Gomer Simpson**
Гитхаб. Темы podkop и zapret.

---

**2026-04-08T18:31:27 | Роман**
https://github.com/StressOzz/Zapret-Manager
Это попробуйте, только отключите з2, уберите ютуб и юискорд из ZB/podkop.

---

**2026-04-08T20:01:27 | Anna Bagler**
Zapret отключите и остановите.

---

**2026-04-08T20:21:40 | Kiss_My_Axe**
Запустить.
Ввести 777, нажать ентер.
Как всё установится - нажать ентер, там написано будет.
Перебирать страты 1-10, после применения проверять доступ к трубе.
Сохраняйте рекомендации, мы на второй круг пошли.
# СТРАТЕГИИ В ZAPRET1
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)

---

**2026-04-09T02:26:40 | Fedor**
Свежий RR, накануне из коробки. 
По инструкции в закрепе успешно установлены ZB/Zapret2. 
Далее, оттуда же..
---
8. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
9. Жмем на Списки сообщества и убираем оттуда Youtube..
---
Делал так неоднократно, убирал, однако галка на Youtube после сохранения/применения неизменно остается активна. Что это может значить? Сам ЮТ рабочий на всех устройствах, но за него ведь отвечает Zapret2, верно?
Стоит ли в Автонастройке активировать боксы Автозагрузка секций / Автозагрузка новой стратегии Zapret2?
Стоит ли сейчас беспокоится об обновлении прошивки с текущей 24.10.5? Совместимы ли ZeroBlock/Zapret2 c 25.12.2?
Спасибо

---

**2026-04-09T06:22:17 | supadupa**
Поделюсь опытом, может пригодится кому-то около начинающему, как я. 

Сидел на предустановленной стратегии youtube, где 21 стратегия перебиралась в режиме циркуляр, потому что я не мог нормально воспользоваться поиском стратегий (там тысяча sni + несколько тысяч страт перебирались 10 часов, я устал). Я ничего в этом не понимаю, какие страты при поиске исключать, какие оставлять, сколько повторов, ТЛС 1.2 или 1.3, я хз, ОЧЕНЬ СЛОЖНЫЕ термины, даже с мануалом. 

В браузере на ПК ютуб работал идеально с моментальной прогрузкой 4к. На устройствах apple были прогрузки по 30-40 секунд при запуске приложения. Периодически видео начинало лагать во время просмотра. Подумал, что надо проверить каждую страту отдельно из 21, а не запускать поиск страт на 7000 в тестере стратегий. 

Порылся, нашел в папке opt/zapret2 файл blockcheck2.sh, порылся в папках глубже, нашел папки custom и standart с листами, куда можно прописать стратегии и точечно их протестировать. Ну я и прописал туда всю эту циркулярку

Короче, запустил блокчек скрипт прям в терминале, протестил только ютуб.ком, увидел какие страты не работают вообще, ну и фейлс и макстайм сильно снизил (если быстро с первого раза не сработала, зачем этой стратой долбить ТСПУ?). Методом исключения составил для себя такой список

--out-range=-s34228
--payload=tls_client_hello
--in-range=-s5556 
--lua-desync=circular:fails=1:maxtime=5
--in-range=x
--lua-desync=multidisorder:pos=1,midsld:strategy=1
--lua-desync=multidisorder:pos=1:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=2
--lua-desync=multidisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=3
--lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=4
--lua-desync=hostfakesplit:ip_id=zero:host=www.google.com:altorder=1:tcp_ts=-600000:strategy=5
--lua-desync=hostfakesplit:host=google.com:tcp_ts=-600000:strategy=6
--lua-desync=fakedsplit:ip_id=zero:pattern=0x00:tcp_ts=-600000:strategy=7
--lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=8
--lua-desync=multidisorder:pos=1,midsld,endhost-1:strategy=9
--lua-desync=multidisorder:pos=1,midsld:strategy=10
--lua-desync=multidisorder:pos=2,5,105,host+5,sld-1,endsld-5,endsld:strategy=11.

В итоге серверы гугла ускорились до космических скоростей даже на айфоне 🚀 

Хотел бы для себя разобраться, как все-таки работает галочка автообновления стратегий запрет2 в зероблоке и есть ли в ней смысл? Это решение для самых маленьких пользователей, чтобы юпуп работал хоть как-нибудь криво-косо?

---

**2026-04-09T08:34:46 | Routerich**
Здравствуйте.
службы->zeroblock->автонастройка->Автозагрузка новой стратегии Zapret2->галочку убираем, сохраняем и применяем

---

**2026-04-09T08:47:07 | 𝓐̅ ̅𝓵̅ ̅𝓮̅ ̅𝓴̅ ̅𝓼̅ ̅𝓪̅ ̅𝓷̅ ̅𝓭̅ ̅𝓻̅ ̅**
Я так понимаю пскет zapret2 от routerich на роктеры не routerich не встанет?

---

**2026-04-09T08:51:55 | 𝓐̅ ̅𝓵̅ ̅𝓮̅ ̅𝓴̅ ̅𝓼̅ ̅𝓪̅ ̅𝓷̅ ̅𝓭̅ ̅𝓻̅ ̅**
Я так понимаю пскет zapret2 от routerich на роктеры не routerich не встанет?

---

**2026-04-09T13:09:42 | Routerich**
Здравствуйте.
по пунктам проверяйте
https://t.me/routerich/3845/333975
ещё надо все следы Zapret с компа удалять, в том числе из реестра

---

**2026-04-09T13:16:06 | Роман**
У вас только ютубанблок работает, он может и не справляться с блокировками. 
Можете (раз у вас запрет установлен уже) подобрать стратегию для запрета, а ЮАБ отключить.

Подбор стратегии для Zapret1 от ув. Kiss_My_Axe - требует установленного запрета.

sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)


Целый комбайн для запрета от ztressozz - сам установит, обновит, настроит.

sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh)

---

**2026-04-09T13:29:25 | Zamir**
Ребят, а как удалить Zapret  с роутера?

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

**2026-04-09T14:29:28 | DedLovesFrogs**
Здравствуйте, уважаемые члены сообщества, подскажите по опыту: что лучше ставить на роутер (буду ставить extroot) - B4 (Bye Bye Big Brother) или zapret2/spoofdpi (и что там советует сообщество)? Ставлю целью также настроить это совместно с geo-файлами, так что хотелось услышать мнение сообщества.

---

**2026-04-09T14:38:54 | Kiss_My_Axe**
Задачи? Только ютуб - пробуйте это.
Запустить.
Ввести 777, нажать ентер.
Как всё установится - нажать ентер, там написано будет.
Перебирать страты 1-10, после применения проверять доступ к трубе.

# СТРАТЕГИИ В ZAPRET1
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)

---

**2026-04-09T15:03:42 | Kiss_My_Axe**
Cкопировать. Вставить в терминал роутера.
Ввести 777, нажать ентер.
Как всё установится - нажать ентер, там написано будет.
Перебирать страты 1-10, после применения проверять доступ к трубе.
# СТРАТЕГИИ В ZAPRET1
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)
#

---

**2026-04-09T15:14:39 | Петр**
Всем привет! Попробовал настроить ZereBlock + Zapret2, но дс не грузится на этапе загрузки обновлений, попробовал откл и на ПК прогнать zapret-discord-youtube и тоже ругается на discord update. Можете подсказать или кинуть гайд по настройке, спасибо

---

**2026-04-09T15:53:05 | Vitaly**
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4. Жмем по очереди на кнопки: сохранить и применить.
7. Далее ждем примерно 5 минут, выходим и обратно входим в интерфейс роутера. В разделе Службы должен появиться пункт "Zapret2".
это сделал и Ютуп заработал,
сделал 8 и дальше - перестал работать.
Перезагрузить и кэш почистить ?

---

**2026-04-09T15:56:41 | Anna Bagler**
Либо вернуть YouTube в zeroblock, но awg в бесплатном варианте может часто падать, либо подбирать стратегию для zapret2.

---

**2026-04-09T16:31:28 | Антон Чепкасов**
Всем привет, ни у кого интернет по wifi не отваливался? На 2 роутерах РР перестал работать. Один обновил на актуальную прошивку и накатил ZeroBlock + Zapret2, всё работает. Второй ещё не трогал. Раньше настроено было через yotubeunblock и podkop, Интересно вот, проблема в прошивке старой или  yotubeunblock и podkop ?

---

**2026-04-09T16:52:47 | Валентин**
Читаю тему и никак не могу понять, сейчас актуально использовать zeroblock+zapret2 или podkop+zapret1? Что дальше будет в поддержке и что правильнее настроить?

---

**2026-04-09T16:54:09 | Anna Bagler**
Zeroblock. Zapret2/1 - что вам нужнее.

---

**2026-04-09T16:56:12 | Валентин**
Т.е. сношу podkop и singbox и ставлю zeroblock+zapret2, получается так? И как я понимаю развиваться дальше будет все таки zapret2, не первый?

---

**2026-04-09T17:04:53 | Роман**
Многим, полностью код переделан, LUA внедрено. Хотите подробнее - https://github.com/bol-van/zapret2/blob/master/docs/manual.md

---

**2026-04-09T17:44:56 | ᅠ ᅠᅠ ᅠᅠ ᅠ**
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки" и ждем, закрываем появившуюся табличку нажав на кнопку "Закрыть".
3. Вводим в окне "Фильтр" (слева) Zeroblock. Внизу должны появиться два пакета: Zeroblock и luci-app-zeroblock.
4. Нажимаем кнопку "Установить" напротив каждого пакета.(Первым идет Zeroblock, а затем luci-app). В появившемcя окне жмем еще раз установить. После завершения закрываем окно. 
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4. Жмем по очереди на кнопки: сохранить и применить.
7. Далее ждем примерно 5 минут, выходим и обратно входим в интерфейс роутера. В разделе Службы должен появиться пункт "Zapret2".
8. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
9. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
10. Проверяете работу Youtube на всех устройствах. (так же желательно в браузерах отключить функцию "Частный/безопасный DNS")

---

**2026-04-09T18:16:32 | 𝐕𝐚𝐧𝐞𝐬 𝐒𝐦𝐢𝐫𝐧𝐨𝐯**
День добрый, подскажите пожалуйста. Настроил как написано, zapret2+ZB, списки сообщества добавил, все необходимое работает, кроме netflix. Причем он как будто бы единственный прописан в секции awg10 в окне, не в списках) 
Куда копать, что делать?

---

**2026-04-09T18:17:34 | Роман**
zeroblock и zapret разные вещи, zb работает с прокси/впн, запрет "дурит" трафик.

---

**2026-04-09T19:26:53 | Александр Кормановский**
добрый день, вопрос куда лучше добавлять свои домены
• установлен ZeroBlock, там есть секции opera и awg10, и в каждой из них есть вкладка Списки, и там можно указать Пользовательские домены
• еще установлен zapret2, и там тоже есть вкладка Списки, где в секции user (/opt/zapret2/ipset/zapret_hosts_user.txt) я как понимаю тоже можно добавить домены

---

**2026-04-09T20:05:57 | Routerich**
Здравствуйте.
Остановите вае обходы, Podkop /zeroblock, youtubeunblock, zapret, и проверяйте будет работать так или нет

---

**2026-04-09T20:07:16 | Anna Bagler**
Обновляйте zapret2 через Пакеты.

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

**2026-04-09T21:49:17 | Gomer Simpson**
Zapret для ютуба используйте.

---

**2026-04-09T21:51:04 | Gomer Simpson**
Пакеты - фильтр zapret - установить все пакеты. Выход/вход. Службы - терминал - туда это:https://t.me/routerich/3845/420612

---

**2026-04-09T21:51:35 | Kiss_My_Axe**
Cкопировать. Вставить в терминал роутера.
Ввести 777, нажать ентер.
Как всё установится - нажать ентер, там написано будет.
Перебирать страты 1-10, после применения проверять доступ к трубе.
# СТРАТЕГИИ В ZAPRET1
#
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)
#

---

**2026-04-10T00:02:14 | Алексей**
Купил устройство, настроил интернет без границ - запусти скрипт. Добавил в подкоп, что было мне необходимо. И вроде все работает. Потом начал читать про zeroblock и zapret2. Вопрос - надо ли перейти с zapret+podkop? На что лучше перейти - zeroblock или zapret2? Как перейти если zeroblock валится в ошибку:
Thu Apr 9 23:45:54 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Thu Apr 9 23:45:59 2026 user.notice zeroblock: No sections configured, restoring DNS and skipping start

---

**2026-04-10T00:02:49 | Петр**
А можете пж поделиться гайдами по настройке ZB/Zapret2 для Nintendo Switch серверов?

---

**2026-04-10T00:17:22 | Алексей**
С английского не нужен, а на понятный пригодится )) 
Но помогите сперва понять - если у меня и так все на zapret работает, имеет ли смысл доп телодвижения делать? Что мне это даст? Стабильность? Скорость? Или пусть все пока остается как есть (zeroblock остановлю или снесу)?

---

**2026-04-10T07:40:03 | Routerich**
Стопните zapret2 и проверьте

---

**2026-04-10T07:58:00 | Routerich**
Zapret отключить и остановить

---

**2026-04-10T08:39:11 | Routerich**
он напрямую работать должен.
попробуйте ZeroBlock, zapret2 остановить и проверить работу

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

**2026-04-10T09:37:17 | Сергей Матвеев**
Всё сделал. Всё заработало. Подскажите как мне zapret первый установить? В пакетах?

---

**2026-04-10T10:07:18 | Михаил**
Zero Block + zapret 2 установлен  и еще запланированная перезагрузка установлена

---

**2026-04-10T10:17:04 | Mikhail Velichko**
Извините за глупый вопрос, но как пустить что-то именно через Zapret? Или правила Zapret срабатывают после правил Zeroblock? Ну то есть если я хочу дискорд через запрет, то исключаю его из списка секций и добавляю соответствующий список в правила пункта Zapret2, так?

---

**2026-04-10T10:24:53 | Mikhail Velichko**
Только zapret2, который тянется вместе с zeroblok

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

**2026-04-10T10:55:01 | Gomer Simpson**
Телегу, в Opera-proxy. Ютуб в Zapret, или Zapret2.

---

**2026-04-10T11:03:28 | Александр Нагорный**
Стоит 2 роутера дома и на работе. На одном зероблок на втором запрет 2. Телега отвалилась на двух. Где зероблок помог перенос из awg10 на opera. А вот на Zapret 2 вообще не помогает ничего. Что делать?

---

**2026-04-10T11:05:27 | Bullet for my valentine Poison**
https://github.com/bol-van/zapret2/blob/master/docs/manual.md

---

**2026-04-10T11:37:23 | Тимур Шамиладзе**
Подскажите. Первоначальная настройка. Запустил скрипт 5. Заработал ютуб, инста и chatgpt, но через пол часа опять перестал. 
Посмотрел вчера поддержка здесь дала совет при запуске: "Итак пошаговый мануал для владельцев Routerich, как завести Zeroblock+Zapret2 на дефолтных настройках".  
Я дошел до пункта что через 5 минут появится Zapret2 в службах, но ничего не произошло и не появился Zapret2. Еще раз запустил скрипт5, но все по-прежнему к закрытым сайтам доступа нет.
Что нужно сделать чтобы заработало?

---

**2026-04-10T12:51:34 | Игорь**
Слушай а мне поставить zeroblock и zapret 2 лучше роутер откатить на заводские ? Щас у меня, тока скрипт 5 и вроде стратегии для ютуба делал через терминал

---

**2026-04-10T13:39:42 | Алексей Росляков**
Доброго времени суток, аналогичная проблема, Zeroblok встал после прошивки, а вот zapret2 никак

---

**2026-04-10T14:10:50 | Ярослав**
Пустить через Zapret\Zapret2 У меня так ютуп и инста работают, прям летают

---

**2026-04-10T14:25:29 | Vasa**
я ему отправил, в чате антизапрета. тебе дублирую

вроде всё учёл, но на чистом роутере не проверял

https://github.com/drno88/AntiZapret-VPN-Instructions

---

**2026-04-10T14:49:53 | DedLovesFrogs**
И то верно. Ничто не вечно под луной.

Я как-то раз сравнивал awg, vless reality xhttp, zapret1

Самый стабильный результат по пользованию показывал всегда zapret, но с оговорками.
awg - быстро, но не совсем стабильно
vless xhttp - ну это xray-core, тут все ясно, средне по скорости (3/5 скорости канала), но при этом стабильность запрета.

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

**2026-04-10T15:02:32 | Simon**
# СТРАТЕГИИ В ZAPRET1
#
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)
#

Помогло

---

**2026-04-10T15:04:04 | Anna Bagler**
В теме zapret2 есть стратегии, ищите по ключевому слову. Или подбирать свою.

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

**2026-04-10T15:12:56 | Ярослав**
Решил запустить Телеграм через Zapret2, пошел на сайт https://iplist.opencck.org/ru/
Скопировал оттуда IP CIDR и домены, копировал дефолтную стратегию YouTub. Все летает на компе, но на смартфонах подключенных по Wi-Fi не работает почему то.
--payload=tls_client_hello
--in-range=-s5556 --lua-desync=circular:fails=3:maxtime=60
--in-range=x
--lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=1
--lua-desync=multisplit:pos=2,sld:seqovl=620:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=1
--lua-desync=multidisorder:pos=1,midsld:strategy=2
--lua-desync=tls_client_hello_clone:blob=cloned_tls:fallback=fake_default_tls:strategy=3
--lua-desync=fake:blob=cloned_tls:optional:tcp_seq=10000000:tcp_ack=-66000:repeats=2:tls_mod=rnd,dupsid,sni=fonts.google.com:strategy=3
--lua-desync=multidisorder:pos=1:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=3
--lua-desync=fake:blob=0x00000000:tcp_seq=-10000:tcp_ack=-66000:strategy=4
--lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:strategy=4
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=fonts.google.com:strategy=4
--lua-desync=multidisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=4
--lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=5
--lua-desync=fakeddisorder:pos=method+2:tcp_md5:strategy=6
--lua-desync=tls_client_hello_clone:blob=cloned_tls:fallback=fake_default_tls:strategy=7
--lua-desync=fake:blob=cloned_tls:optional:tcp_ts=-600000:tls_mod=rnd,dupsid,sni=www.google.com:strategy=7
--lua-desync=hostfakesplit:ip_id=zero:host=www.google.com:altorder=1:tcp_ts=-600000:strategy=7
--lua-desync=hostfakesplit:host=google.com:tcp_ts=-600000:strategy=8
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_ts=-600000:repeats=6:strategy=9
--lua-desync=fakedsplit:ip_id=zero:pattern=0x00:tcp_ts=-600000:strategy=9
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_ts=-600000:repeats=8:strategy=10
--lua-desync=multisplit:pos=1:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:ip_id=zero:strategy=10
--lua-desync=multisplit:pos=1:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:ip_id=zero:strategy=11
--lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=12
--lua-desync=multisplit:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=13
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=fonts.google.com:strategy=14
--lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=14
--lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=14
--lua-desync=multidisorder:pos=7,sld+1:nodrop:strategy=15
--lua-desync=multidisorder:pos=1,midsld,endhost-1:strategy=16
--lua-desync=fake:blob=0x00000000:tcp_seq=-10000:tcp_ack=-66000:repeats=2:strategy=17
--lua-desync=fake:blob=fake_default_tls:tcp_seq=-10000:tcp_ack=-66000:repeats=2:tls_mod=rnd,dupsid,sni=www.google.com:strategy=17
--lua-desync=multisplit:pos=1,midsld:strategy=17
--lua-desync=multidisorder:pos=1,midsld:strategy=18
--lua-desync=multisplit:pos=1,2:seqovl=4:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=19
--lua-desync=multidisorder:pos=2,5,105,host+5,sld-1,endsld-5,endsld:strategy=20
--lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=21
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=21
--lua-desync=multisplit:pos=2,sld:seqovl=2108:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=21:final

---

**2026-04-10T15:19:42 | Grigory**
Есть люди у кого провайдер билайн и роутерыч(zeroblock+zapret2)?

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

**2026-04-10T15:33:01 | DedLovesFrogs**
А можно мне обьяснить вот этот стек:
1. zapret2 - понятно, самый быстрый обход всякого-всякого.
2. awg - геоблок, понятно.

А что делает opera-proxy и почему на её отвал все так жалуются?
Я что-то в документации этого нихрена не понял.

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

**2026-04-10T15:35:32 | Ярослав**
Кто нибудь вкурсе почему Телеграм на ура пашет через Zapret2 на компе (кабелем к роутеру) и не хочет на смартфоне по Wi-Fi?

---

**2026-04-10T16:27:08 | Anna Bagler**
Останавливаем zeroblock. Cмотрим на обычные ресурсы. Потом останавливаем zapret2. Cмотрим. Это можно сделать на соответствующих страничках в Службах.

---

**2026-04-10T16:29:47 | Некит**
ребят вопрос, позавчера ставил последнюю прошивку и пропал podkop и zapret, потом всё накатил с помощью zeroBlock, и вопрос в следующем если я сейчас заново накачу прошивку так же всё слетит? Или же как удалить Zeroblock и zapret2, так как непривычно с ними работать? Что вообще надо сделать чтоб остался podkop и zapret?

---

**2026-04-10T16:41:00 | Дмитрий Б.**
Zapret проверки — Активный

---

**2026-04-10T16:41:18 | Дмитрий Б.**
вот ○  zapret (nfqws)  Не запущено

---

**2026-04-10T16:55:26 | ㅤㅤ**
Может ZB + Zapret2? Или старовер?

---

**2026-04-10T16:56:31 | Maxim**
Я удалил Podkop, установил ZeroBlock + Zapret2, изменил DNS на 9.9.9.9 и вроде всё пока что работает.

---

**2026-04-10T17:16:16 | Виталий Александрович**
Спасибо, гуглу это помогло, а вот телеге не совсем. На телефонах тупит но работает, а на компе даже страница авторизации не открывается.
Куда унести телегу? В zapret2 ?

---

**2026-04-10T17:51:24 | Anna Bagler**
Если у вас нет своего vless или ещё чего, то zb вам не поможет. Можно попробовать через zapret1.

---

**2026-04-10T18:16:01 | Anna Bagler**
Тогда вам надо пробовать стратегию от @BFMVPoison в закрепах темы Zapret2.

---

**2026-04-10T18:17:44 | Pavel**
Добрый вечер всем! 
Давеча тут обновил прошивку и накатил скрипт из данного раздела. Кроме этого ещё запрет и ютубанблок стоят... 
И вот какой вопрос возник, а есть ли какая-то статья/методики с bestpractics? 
Субъективно ощущение что после обновления прошивки роутера и запуска всех пакетов инста стала тормозить при просмотре видео 

Надо ли при установленном zapret2 держать включенным и вообще установленным zapret?

---

**2026-04-10T18:19:06 | Anna Bagler**
youtubeUnblock отключайте и останавливайте или удаляйте вообще. И прижмите галочки для запрет2 в автонастройках zeroblock. Потом стратегию для zapret2 пробовать.

---

**2026-04-10T18:27:25 | Дима Чуйков**
идут "Метка Desync (zapret2)" и сразу "Исключённые IP"

---

**2026-04-10T19:22:17 | Ярослав**
Возможное решение проблемы работы телеграма на телефоне, это из списков Zapret2 убрать все IP и CIDR, оставить только список доменов:
comments.app
contest.com
fragment.com
graph.org
quiz.directory
t.me
tdesktop.com
telega.one
telegra.ph
telegram-cdn.org
telegram.dog
telegram.me
telegram.org
telegram.space
telesco.pe
tg.dev
tx.me
usercontent.dev
ton.org

---

**2026-04-10T19:37:28 | Ярослав**
так это тема про Zapret2!!!

---

**2026-04-10T19:50:01 | Виталий Александрович**
в соседнем чате говорят что можно через zapret2, попробовал у меня не полетела,  в итоге пришлось через влес пускать

---

**2026-04-10T20:08:15 | Ярослав**
с компа через браузер (ну лично мне так удобнее всего) через Zapter2 прекрасно работает! Но на смарте нет. Никак. Даже через Tailscail пробовал - нет. При  попытке вернуть все через Podkop, на компе работает хуже, но все же работает. На смартфоне опять нет. Прошлый раз смарт спустя час наверное прочухался и заработал через Podkop. Но опять же через некоторое время Телеграм везде отвалился. Сейчас опять через Zapret2 пустил, комп пашет - смарт нет. 🤦‍♂️🤦‍♂️🤦‍♂️

---

**2026-04-10T20:18:42 | Maxim**
ZeroBlock + Zapret2 и всё работает (пока что).

---

**2026-04-10T20:23:54 | Роман**
https://github.com/StressOzz/Zapret-Manager
Есть решение с ТГ через этот скрипт, но медиа там не грузит, только текст.

---

**2026-04-10T20:34:23 | B R**
Подскажите, отвалился podkop, в какой ветке обсуждение? 

И второй вопрос - стоит zapret, стоит ли обновляться на zapret2?

---

**2026-04-10T20:40:01 | Maxim**
Пробуйте ZeroBlock + Zapret2

---

**2026-04-10T20:44:21 | Николаич**
Вечер добрый. Как удалить полностью Zapret2 c роутера.

---

**2026-04-10T20:46:10 | B R**
Я правильно понял, что podkop и zapret надо поменять на zeroblock и zapret2?

---

**2026-04-10T20:55:09 | Николаич**
Вопрос остался без ответа; Какую ссылку ввести в терминал для удаления хвостов от Zapret2? Поделитесь плиз...

---

**2026-04-10T20:58:28 | Gomer Simpson**
rm /etc/config/zapret2* && rm -rf /opt/zapret2

---

**2026-04-10T21:03:19 | B R**
Ага, спасибо, завтра попробую. 

Еще вопрос - я все это добро ставил скриптом номер 5, теперь zeroblock и zapret2 ставлю руками после сброса роутера в дефолт. Верно? 

Для zeroblock инструкцию уже нашел, читаю :) 

Всем спасибо, что помогаете новичкам. Встретить нетоксичное рукомьюнити прям удивительно для меня)

---

**2026-04-10T21:05:23 | Ярослав**
кстати пуши на смартфон через Zapret2 приходят, но сам смарт сеть по-прежнему не видит... Может дело в каком интерфейсе входном\выходном у Zapret2?

---

**2026-04-10T21:32:25 | Alex_Jester**
Установите по этой инструкции, что может быть проще?

1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки" и ждем, закрываем появившуюся табличку нажав на кнопку "Закрыть".
3. Вводим в окне "Фильтр" (слева) Zeroblock. Внизу должны появиться два пакета: Zeroblock и luci-app-zeroblock.
4. Нажимаем кнопку "Установить" напротив каждого пакета.(Первым идет Zeroblock, а затем luci-app). В появившемcя окне жмем еще раз установить. После завершения закрываем окно. 
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4. Жмем по очереди на кнопки: сохранить и применить.
7. Далее ждем примерно 5 минут, выходим и обратно входим в интерфейс роутера. В разделе Службы должен появиться пункт "Zapret2".
8. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
9. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
10. Проверяете работу Youtube на всех устройствах. (так же желательно в браузерах отключить функцию "Частный/безопасный DNS")

---

**2026-04-10T21:34:54 | Ярослав**
Нет, я сперва пробовал через вай-фай, потом пробовал через сотовую и через tail. DNS на смартфоне авто пробовал и отключать пробовал. У меня закончились идеи. Никак вообще не хочет. А так жаль, через Zapret2 прям шикарно работает на компе

---

**2026-04-10T21:37:59 | Gomer Simpson**
ZeroBlock + Zapret2. Соседние темы. Везде есть подробные инструкции .PDF

---

**2026-04-10T21:49:27 | Alex_Jester**
Я правильно понимаю, если youtube выбран в секции awg, то он будет иметь приоритет перед zapret2? И в запрете не надо снимать галку с ютуба?

---

**2026-04-10T21:50:02 | Валерий**
Приветствую. С февраля приобрёл роутер, накатил скрипт 5 и больше ничего не менял кроме, списков в секциях main и vpn. Все работает, щас вот телега не работает в main, перебросил в её в vpn. Заработала. Вообщем-то вопрос: zapret2, zeroblok есть смысл менять на них

---

**2026-04-10T22:09:54 | Vasa**
https://github.com/GubernievS/AntiZapret-VPN

---

**2026-04-10T22:11:04 | Алексей**
Ребята,сегодня установил Zeroblock.Действовал по мануалу для чайников из закрепленного сообщения.Вроде разобрался со всем этим хозяйством,хоть и со скрипом мозга,но почему-то в вебморде в разделе Службы никак не хочет появляться zapret2.Список пакетов успешно обновляется и там указано,что zapret2 и lucy zapret2 установлена,а в разделе Службы на вебморде он так и не появился(И ещё Телеграмм стал очень плохо работать.На последней версии Подкопа как-то всё повеселее было до сегодняшнего дня.Но вот сегодня с утра совсем всё плохо с интернетом стало.Видимо РКН там очередной рубильник выключили.Пришлось заморачиваться с установкой Zeroblock

---

**2026-04-10T22:41:08 | Key**
Хорошо что хоть ютуб пущен через zapret

---

**2026-04-10T22:45:10 | труляля🧑‍🦲#отвальный #mimilover #create #Print("helloworld")**
Подскажите, как настроить роутер, что бы работал телеграм. Базовая настройка совершена, zapret2 и amnezia wg установлены, но все равно не пашет

---

**2026-04-10T22:46:41 | Alex_Jester**
А чтобы Дискорд работал через zapret, а не через awg достаточно в списках awg снять галку и все или нужно в запрете еще что-то настраивать?

---

**2026-04-10T22:47:46 | Артём**
Начал ставить zeroblock+zapret2 по мануалу, но в п.6 не отображаются активными 1 и 2 (вроде как установлены). Следовательно в 7 пункт данного манула не появляется zapret 2 в службах.

А в Zeroblock такие логи.

Сайты вроде rutracker, YouTube не открываются. А хотелось бы)

---

**2026-04-10T23:21:08 | Алена Мос**
Помогите пожалуйста чайнику!!! Пытаюсь по мануалу установить zapret2. Пункт 6 из мануала, в автонастройках в пункт первый и второй не дает поставить Галки (пишет что все установлено) Галки проставлены в 3 и 4 -сохранить применить - 5 минут  подождать- зашла заново - zapret2 не появился

---

**2026-04-11T00:44:22 | Woohard**
Заработал тг на телефоне.
Сегодня снес настройки в завод, поставил метод ZeroBlock плюс Zapret 2, когда все у всех отвалилось. СИдел на пятом скрипте до этого всегда.
Всё заработало, кроме тг на телефоне.
Сейчас поставил по приколу поверх этого всего пятый скрипт снова, телегу убрал из списков подкопа, вроде работает теперь на телефоне тг

---

**2026-04-11T00:57:06 | Woohard**
Заработал тг на телефоне.
Сегодня снес настройки в завод, поставил метод ZeroBlock плюс Zapret 2, когда все у всех отвалилось. Сидел на пятом скрипте до этого всегда.
Всё заработало, кроме тг на телефоне.
Сейчас поставил по приколу поверх этого всего пятый скрипт снова, телегу убрал из списков подкопа, вроде работает теперь на телефоне тг.
НО отвалился только что дискорд. мде.
Удалил секцию дискорда из Подкопа полностью, работает.
Пока посижу на таком варианте франкенштейн-обхода, понаблюдаю.
Мб кому будет полезно

---

**2026-04-11T01:25:09 | IIlIlIlIIlIlIlIIIll**
Прошу помогите. Сломался днс сильно. Роутер был восстановлен до заводских. Podkop+zapret установил но opera proxy не установлен. Хэлп плиз

---

**2026-04-11T01:47:33 | Anton**
@BWasilii

#battlefield #battlefield6 #bf6 #батла #бф #бф6 #ea #eagames #eaapp


Посниффил трафик с запушенного bf6.exe, получил следующее:

ea.com
blaze.ea.com
gameservices.ea.com
data.ea.com
tnt-ea.com
grpc.ea.com
social.ea.com
ac.ea.com
akamaihd.net

13.57.10.150/32
3.40.130.0/24
3.210.214.0/24
3.219.175.0/24
3.229.170.0/24
3.33.187.0/24
13.219.156.0/24
13.248.213.0/24
23.73.2.0/24
44.212.230.0/24
52.4.203.0/24
52.215.171.0/24
54.82.163.0/24
54.210.180.0/24
54.229.157.0/24
99.81.53.0/24
99.83.184.0/24
100.51.38.0/24
166.117.23.0/24


Zapret стоит на роутере, ни одна стратегия не помогла. Пустил это добро в туннель до ВПН сервера. Играю - полет отличный, без вылетов.
Через нейронку набросал чекер доступности для доменов и айпи вышеуказанных (кладем в папку - ПКМ по свободному месту в открытой папке куда положили - открыть терминал - ./check_ea.ps1 )

---

**2026-04-11T06:30:24 | Андрей Константинов**
Вчера поставил zero block и zapret 2, делал все по инструкции, но вот с 8 пункта ничего не могу увидеть куда идти дальше

---

**2026-04-11T08:55:59 | Андрей Константинов**
После полного отвала telegram, YouTube,  с командой Routerich  🙏установил zero block и zapret 2, все запустилось кроме робота пылесоса, он подключился ездит но карты нет, помогите люди добрые, пожалуйста

---

**2026-04-11T09:51:15 | Yury Kuzmenko**
https://github.com/bol-van/zapret2/blob/master/docs/manual.md
Только через полный мануал по запрет2 там есть описание как стратегию запрет1 перевести в запрет2

---

**2026-04-11T10:08:37 | Роман**
Здравствуйте. Если на ПК запрет 1, а вы хотите перевести на запрет 2, то только полностью изучать мануалы, возможно нейронки могут помочь (но это не точно). Есть тема на https://ntc.rkn.quest/t/zapret2-%D0%BE%D0%B1%D1%81%D1%83%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5/21161 есть мануал в Вики.

---

**2026-04-11T10:10:16 | ㅤㅤ**
Youtube у меня стабилен на всех устройствах. ZB + Zapret2 + свои VLESS. Youtube все время шел через ZP2 вроде как с вашей бессмертной стратегией.

---

**2026-04-11T10:18:18 | Aleksei P**
Всем привет. А ни у кого нет проблем с доступом к Хабру, с настроенным Zapret2 на роутере?

---

**2026-04-11T10:24:57 | Юрий 🏂**
Привет!
Подскажите что не так делаю при установке ZAPRET2, сделал все по интрукции в закрепе, подождал минут 10 но запрет2 так и не появился

---

**2026-04-11T10:27:19 | Bullet for my valentine Poison**
Тогда зайти в пакеты и в фильтр вписать zapret2. Если установлено, то чистите браузер. Если нет, то вручную

---

**2026-04-11T12:14:42 | Александр Ёлохов**
Добрый день.
Поставил себе Zeroblock и Zapret2, ютуб, мета, дискорд, все работает, но не работает телеграмм, подскажете что сделать можно?

---

**2026-04-11T12:16:07 | Kirill**
Логику понимаю. Но как вариант у меня фейсбук открывается и он в Main. 

Установлен так же zapret - он помогает октрытию?)

---

**2026-04-11T12:59:20 | GREY**
Странная проблема.
При включенном Zeroblock, Xbox 360 выдает MTU Error (даже если консоль в исключениях или в полной маршрутизации). 
При выключенном, подключается без проблем (без VPN или чего-либо еще).
По сути роутер чистый, устанавливался только zeroblock и zapret2.
Есть идеи?

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

**2026-04-11T13:18:47 | ᅠ ᅠ**
Щас сделал так, чтобы появился Zeroblock и zapret2

---

**2026-04-11T13:47:30 | Routerich**
Система - автозапуск - найдите podkop и если есть zapret или youtubeUnblock нажмите на включено. Перезагрузите роутер. Протестируйте как подключаются Яндекс станции. Без обходов надо убедиться точно в работоспособности нормальной. Далее будем разбираться

---

**2026-04-11T13:49:38 | Александр**
Всем привет, поскажите как на типовом RR с zb, zapret2, opera и wg10 реализовать маршрутизацию, чтобы если клиенское устройство в сети wifi2 трафик до ютьюба шел бы через opera (с иностранных ip)  а если в сети wifi5 через zapret или wg10. Суть вопроса в том заработает ли схема если списки youtube будут в разных секциях одновременно но источник трафика с разных интерфейсов?

---

**2026-04-11T14:24:53 | Алексей Сергеевич**
Анализ запущен: 2026-04-11 14:23:37
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
  Facebook IP:  198.18.1.93 | YouTube IP:  64.233.162.136
  Программы в автозапуске: zeroblock zapret2 opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН  !!!_ОПЕРА ЗАБЛОКИРОВАЛА РОССИЮ_!!! 
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:     100.100.100.100:53
    Name:       youtube.com        Address: 142.250.150.136
    Name:       youtube.com        Address: 142.250.150.93
    Name:       youtube.com        Address: 142.250.150.91
    Name:       youtube.com        Address: 142.250.150.190
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock              awg20 (vpn): ai,block,geoblock,googleplay,messengers,meta
  zeroblock        DNS/Bootstrap DNS: (doh) 1.1.1.3 / 1.0.0.3
  Версия zeroblock: 0.7.2-r55
  !!!_Интерфейс awg20: nohostroute не установлен в 1 (создание маршрутов включено!)

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.2.1 (Прошивка: 24.10.5)
  CPU: 0.52 | RAM: 30% | NAND: 51% занято / 33.2M доступно
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-04-11T14:29:32 | Aidar Safiullin**
Анализ запущен: 2026-04-11 14:28:03
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
  Facebook IP:  198.18.0.160 | YouTube IP:  108.177.14.91

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.44 MB
  Пинг (ya.ru via awg10): 103.104 / 103.819 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock zapret2 opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН  !!!_ОПЕРА ЗАБЛОКИРОВАЛА РОССИЮ_!!! 
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200 OK) [tlsv1.3] [try: 1]
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:     127.0.0.1:53
    Name:       youtube.com        Address: 108.177.14.93
    Name:       youtube.com        Address: 108.177.14.190
    Name:       youtube.com        Address: 108.177.14.136
    Name:       youtube.com        Address: 108.177.14.91
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock              awg10 (vpn): anime,block,discord,googleplay,messengers,meta,news,porn,socials,video
  zeroblock          opera (prx out): geoblock,ai
  zeroblock        DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8
  Версия zeroblock: 0.7.2-r55

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.46 | RAM: 24% | NAND: 44% занято / 37.9M доступно
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-04-11T15:02:46 | Anna Bagler**
Стратегию для zapret2 пробуйте сменить.

---

**2026-04-11T15:16:25 | Dmitriy Vavilov**
Пришел роутер, в службах zapret2 не было
установил пакет zapret2, в службах  zapret2 не появился - что делать?

---

**2026-04-11T15:17:16 | Ghost**
подскажите пож-та у кого получилось настроить доступ к Copilot через ZeroBlock/Zapret2 - как вы этого добились?

---

**2026-04-11T15:22:00 | Ghost**
да, все настройки сделал по этим шагам, разве что xray и zapret2 автонастройкой не установились - установил через opkg. Но не понял как это отвечает на мой вопрос?

---

**2026-04-11T16:03:15 | Dmitriy Vavilov**
Оказалось, что когда установил zapret2 и оно работает (позволяет ютуб) не работает ДОСТУПНО
Отключаешь - работает доступно, но Установление не работает - нету связи
что то пошло не так
Есть процедура ОЧИСТКИ от всех пакетов?

---

**2026-04-11T16:48:28 | Routerich**
Попробуйте
/etc/init.d/zapret2 stop
/etc/init.d/youtubeUnblock stop
/etc/init.d/stubby stop
/etc/init.d/doh-proxy stop
Проверяете сеть на твбоксе
Как закончите тест то включить так
/etc/init.d/zapret2 start
/etc/init.d/youtubeUnblock start
/etc/init.d/stubby start
/etc/init.d/doh-proxy start

---

**2026-04-11T17:52:42 | iProxx**
Кстати нет. Реклама на немецком лезла когда Youtube в туннеле приложения был. Сейчас оставил его в Zapret2. Пока работает

---

**2026-04-11T18:09:43 | Роман**
https://github.com/StressOzz/Zapret-Manager
Тележка без картинок, зато нахаляву!

---

**2026-04-11T18:42:10 | Routerich**
Сделайте так. Система - автозапуск - остановить podkop и zapret, далее выключите ноутбук. через минуту запускайте подкоп и включайте ноут, после полного включения и подключения к сети, присылайте логи Статус - просмотр лога - скачать журнал

---

**2026-04-11T18:51:34 | Kinaman**
Здравствуйте! У меня установлен Podkop и Zapret, до последних дней все основные заблокированные ресурсы работали, но два дня назад перестали открываться Meta (Instagram) и Twitch.tv. Я собрал все сведения о системе. Подскажите, пожалуйста, что можно сделать, чтобы вернуть доступ к ресурсам?

---

**2026-04-11T19:00:15 | Никита**
Всем привет
: SmartTube — меню грузится, видео на 0:00
Routerich AX3000 + ZeroBlock + Zapret 2. На телефоне и в официальном YouTube всё работает. На Ugoos X4 Pro в SmartTube меню открывается, а видео не стартует (стоит на 0:00, чёрный экран).
Пробовал: все домены для googlevideo, ручной профиль, отключение IPv6, очистка кэша.
Подскажите рабочие стратегии Zapret 2 именно под видео-стримы SmartTube или решение через PowerTunnel.

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

**2026-04-11T20:51:30 | Timur**
сейчас zero и zapret2

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

**2026-04-11T21:42:21 | Роман**
Для ютуба попробуйте zapret2. Предварительно убрать ютуб из подкопа.

---

**2026-04-11T22:06:29 | Степан**
В самом менеджере Zapret ozz какие стратегии бирюзовым цветом стоят? Для работы телеги

---

**2026-04-11T22:39:14 | Bullet for my valentine Poison**
Итак пошаговый мануал для владельцев Routerich, как завести Zeroblock+Zapret2 на дефолтных настройках.
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки" и ждем, закрываем появившуюся табличку нажав на кнопку "Закрыть".
3. Вводим в окне "Фильтр" (слева) Zeroblock. Внизу должны появиться два пакета: Zeroblock и luci-app-zeroblock.
4. Нажимаем кнопку "Установить" напротив каждого пакета.(Первым идет Zeroblock, а затем luci-app). В появившемcя окне жмем еще раз установить. После завершения закрываем окно. 
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4. Жмем по очереди на кнопки: сохранить и применить.
7. Далее ждем примерно 5 минут, выходим и обратно входим в интерфейс роутера. В разделе Службы должен появиться пункт "Zapret2".
8. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
9. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
10. Проверяете работу Youtube на всех устройствах. (так же желательно в браузерах отключить функцию "Частный/безопасный DNS")

---

**2026-04-11T23:24:27 | Василий**
Подскажите, сижу на ZeroBlock , отключил и podkop и zapret. Перенес список Messengers из секции awg10 в секцию Opera, полет нормальной, кроме телеграм на телефоне.

---

**2026-04-11T23:31:16 | ~**
Всем доброго времени суток! Подскажите идей, а то свои уже все перепробовал. Айфон не подключается к wifi, при этом другие семейные айфоны подключились без проблем. Пробовал и канал менять, и частоту менять 160->80->40МГц  - ничего не помогает. При этом к прошлой одноименной сети подключался нормально. А после того как за сеть стал отвечать RR - ни в какую не хочет подключаться. Получение IP и DNS - автоматически от роутера. На роутере подняты Zapret, Podkop, Tailscale. В предыдущей сети было все тоже самое кроме Tailscale. Есть идеи, что еще может влиять на успех подключения (проверить пароль просьба не предлагать)?

---

**2026-04-11T23:37:34 | Mike**
у меня на меге работает таже связка только еще zapret . но работает. пока

---

**2026-04-12T00:07:52 | Routerich**
В теме wiki есть мануалы по zapret2, подбирайте стратегии

---

**2026-04-12T00:08:05 | Kiss_My_Axe**
Один список ОБЯЗАН быть только В ОДНОЙ секции. А у вас сплошные дубли.
За что подкоп и не люблю.
Убирайте МЕТА и ГЕОБЛОК из ЮТУБ_ДИСКОРД (проверим, может наоборот надо сейчас).
А ТЕЛЕГРАМ убирайте из MAIN.

2ip.ru один откуда угодно уберите.

Службы - Zapret, СТОП, ОТКЛЮЧИТЬ.

---

**2026-04-12T00:12:25 | Константин Волчек**
как зайти в настройки zapret1 через терминал? там надо было три буквы ввести, забыл какие)

---

**2026-04-12T00:15:31 | ~**
https://github.com/StressOzz/Zapret-Manager

---

**2026-04-12T01:38:33 | support**
Подскажите почему это не работает адекватно, ютюб работает, но все остально что на скринах пугает. 
NFQWS2_OPT="--filter-udp=443 --filter-l7=quic --hostlist-domains=youtube.com,googlevideo.com,youtu.be,googleapis.com,ytimg.com,ggpht.com,gstatic.com,google.com --out-range=-s34228 --payload=quic_initial --lua-desync=fake:blob=quic_initial:ip_ttl=6 --new --filter-udp=443 --filter-l7=quic --hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt --out-range=-s34228 --payload=quic_initial --lua-desync=fake:blob=quic_initial:repeats=6 --new --filter-tcp=80 --filter-l7=http --hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt --out-range=-s34228 --payload=http_req --lua-desync=fake:blob=http:tcp_md5 --lua-desync=multisplit:pos=method+2 --new --filter-tcp=443 --filter-l7=tls --hostlist-domains=youtube.com,googlevideo.com,youtu.be,googleapis.com,ytimg.com,ggpht.com,gstatic.com,google.com --out-range=-s34228 --in-range=-s5556 --lua-desync=circular:fails=1:maxtime=5 --in-range=x --payload=tls_client_hello --lua-desync=multidisorder:pos=1,midsld:strategy=1 --lua-desync=multidisorder:pos=1:seqovl=681:seqovl_pattern=tls_clienthello:strategy=2 --lua-desync=multidisorder:pos=10,midsld:seqovl=336:seqovl_pattern=tls_clienthello:strategy=3 --lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=4 --lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=www.google.com:strategy=5 --lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=google.com:strategy=6 --lua-desync=fakedsplit:pos=midsld:strategy=7 --lua-desync=multidisorder:pos=1,midsld,sniext:strategy=8 --lua-desync=multidisorder:pos=1,sniext+1,midsld-2,midsld,midsld+2:strategy=9 --lua-desync=fake:blob=tls_clienthello:ip_ttl=6:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=rzd.ru:repeats=4:strategy=9 --lua-desync=multidisorder:pos=2,5,105,sniext+5,midsld-1:strategy=10 --lua-desync=multisplit:pos=10:seqovl=1:strategy=11 --new --filter-tcp=443 --filter-l7=tls --hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt --out-range=-s34228 --payload=tls_client_hello --lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=2gis.com --lua-desync=multisplit:pos=2 --new --filter-l7=mtproto --payload=mtproto_initial --lua-desync=fake:blob=0x00000000 --new --filter-tcp=443 --filter-l7=tls --ipset=/opt/zapret2/ipset/zapret-ips-user.txt --out-range=-s34228 --payload=tls_client_hello --lua-desync=multidisorder:pos=1,sniext+1,midsld-2,midsld,midsld+2 --lua-desync=fake:blob=tls_clienthello:ip_ttl=6:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=rzd.ru:repeats=4"

---

**2026-04-12T02:06:07 | Maksim**
подскажите для чего нужен zapret2 ?
ну то есть, он ставится вместе с zb, появляется пункт в списке служб, если делать всё по инструкции по установке zeroblock.
но я не пойму зачем zapret2 нужен 🗿😁
у меня что с запретом2, что без него, всё один фиг работает плохо c утра пятницы 10 апреля.
даже со своим квн прикрученным к rr через zb все равно всё плохо пашет
но блин нафига всё таки нужен запрет2 😁
можно его вырубить или от него есть толк какой то? я прост думаю что он может конфликтовать с zb или я ошибаюсь?

---

**2026-04-12T02:15:08 | Anna Bagler**
Много для одного Ютуба. Отключайте и останавливайте youtubeUnblock и zapret. Смените adguard на девятки или единицы. opera-proxy обновите через система-пакеты.

---

**2026-04-12T02:17:32 | Kiss_My_Axe**
opkg remove youtubeUnblock
service zapret stop
service zapret disable

в терминал.

---

**2026-04-12T05:52:43 | Key**
Если нужен один ютуб, то вообще особо и проблем нет. Zapret2 из установщика пакетов прекрасно работает. Сижу на штатной стратегии с декабря прошлого года. Телегу запустил, удалив ее из других секций и добавил ее в отдельную, подключение сделал на свой vless ключ.

---

**2026-04-12T08:33:31 | Василий**
Доброе утро. Обновился до новой прошивки. Что-то сделал не так, что после прошивки не встал ZB и Zapret2. Установил их отдкльно по инструкции. Все встало, но нет awg10 интерфейса в ZB. В автонастройке написано, что он уже существует. Как авг10 отобразить в секциях?

---

**2026-04-12T09:37:14 | Smallin**
Вроде ничего кроме sing и zeroblock zapret amnezia tailscale не ставил))
Что он хочет?
hdp.getServiceInfo is not a function

---

**2026-04-12T10:58:45 | S N**
У меня не работает vless при включенной opera proxy, подскажите плиз нубу куда копать🙏. Хочу чтобы только телега через vless работала, а остальное через zapret и так работает. Создано отдельную секцию для vless, но нет подключения пока опера работает...

---

**2026-04-12T11:50:30 | Радик**
Добрый день подскажите пожалуйста в нынешних реалиях что лучше установить? Скрипт 5 или zapret что бы можно было пользоваться ТГ, Инстаграм, заранее спасибо

---

**2026-04-12T12:01:16 | ⒿⒶⓏⓏ ⒷⒶⓈⓈ**
Я собирал прошивку сразу с этим
opera-proxy
xray-core
zapret2
luci-app-zapret2
sing-box-tiny
Потом уже настраивал. Единственное, что настройки оставил. Может в этом дело?

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

**2026-04-12T12:23:28 | Timur**
скажите какие dns лучше прописать в роутере? сейчас гугловский, может есть еще какие рекомендации. Через vless  открывает вс е в принципе и ютуб через zapret работает пока.

---

**2026-04-12T12:30:13 | Никита Байдин (DOOMGUY)**
Бляха. Я уже час долблюс с этим ZeroBlockом а он Zapret2 не хочет ставить

---

**2026-04-12T12:33:13 | Bullet for my valentine Poison**
Система - пакеты. В фильтр вписать Zapret2

---

**2026-04-12T13:41:29 | Андрей М**
Всем привет. На днях столкнулся с такой проблемой... После отключения питания на роутере при новом подключении нет сети, соединение есть но без доступа в интернет. В Статус пишет что подключено но трафика нет. Решается проблема перезапуском интерфейсов в ручную. После чего всё работает нормально до следующего обесточивания роутера. На роутере стоит скрипт 5, Podkop, Zapret. Провайдер Ростелеком. Всё что мне нужно открывается в этой конфигурации, но каждый раз лезть в роутер для ручного перезапуска интерфейсов - это геморрой. Может кто знает как исправить?

---

**2026-04-12T15:19:32 | Alexey Zh**
запустил 
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/test_config_script/test_config_script_nightly)
норм что DNS Server:   100.100.100.100:53 ?

Анализ запущен: 2026-04-12 15:10:12
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   100.100.100.100:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  31.13.72.36 | YouTube IP:  209.85.233.91

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.35 MB
  Пинг (ya.ru via awg10): 7.522 / 8.941 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock zapret2 opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН  !!!_ОПЕРА ЗАБЛОКИРОВАЛА РОССИЮ_!!! 
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200 OK) [tlsv1.3] [try: 2]
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:     100.100.100.100:53
    Name:       youtube.com        Address: 209.85.233.190
    Name:       youtube.com        Address: 209.85.233.93
    Name:       youtube.com        Address: 209.85.233.136
    Name:       youtube.com        Address: 209.85.233.91
    Name:       youtube.com        Address: 2a00:1450:4010:c03::be
    Name:       youtube.com        Address: 2a00:1450:4010:c03::5b
    Name:       youtube.com        Address: 2a00:1450:4010:c03::5d
    Server: 2a00:1450:4010:c03::88
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ

---

**2026-04-12T16:21:27 | Роман**
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки" и ждем, закрываем появившуюся табличку нажав на кнопку "Закрыть".
3. Вводим в окне "Фильтр" (слева) Zeroblock. Внизу должны появиться два пакета: Zeroblock и luci-app-zeroblock.
4. Нажимаем кнопку "Установить" напротив каждого пакета.(Первым идет Zeroblock, а затем luci-app). В появившемcя окне жмем еще раз установить. После завершения закрываем окно. 
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4. Жмем по очереди на кнопки: сохранить и применить.
7. Далее ждем примерно 5 минут, выходим и обратно входим в интерфейс роутера. В разделе Службы должен появиться пункт "Zapret2".
8. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
9. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
10. Проверяете работу Youtube на всех устройствах. (так же желательно в браузерах отключить функцию "Частный/безопасный DNS")

---

**2026-04-12T16:27:44 | ㅤㅤ**
Сбросил роутер. Поставил через автонастройку Zeroblock + Zapret2 с обновленными пакетами opera_proxy, amneziaWG и т.д. Больше ничего не менял. Работает opera_proxy. Работает Gemini. Спасибо команде, можно со спокойной душой улетать в отпуск 🙏🏻

---

**2026-04-12T16:29:45 | Вячеслав Синельников**
Подскажите через zeroblock zapret2 на роутере не работает телега постоянно висит соединение и все при том что ютуб летает что можно покрутить настроить чтоб телега заработала ?

---

**2026-04-12T17:07:19 | Алексей**
Я прошу прощения, но Опера прокси уже установлен, Амнезия существует, и пункт Zapret2 в разделе Службы не появился, спасите-помогите!

---

**2026-04-12T17:16:47 | Bullet for my valentine Poison**
Тогда зайти в систему-пакеты, обновить списки и в фильтр слева вписать zapret2

---

**2026-04-12T17:29:21 | Алексей**
Появился в службах Zapret2. Там нет Секций маршрутизации. Зато они есть в Zeroblokе. Но там пусто. Я в правильном месте задаю свои детские вопросы, ничего, что я тут на Пасху высоколобую поддержку мучаю?

---

**2026-04-12T18:04:02 | Vasya Mafia**
Всем привет! Осмотрел wiki, не нашел базовой для меня инфы. Отдельно вроде про всё есть: zapret, podkop, zeroblock и тп. Есть ли какая-то между ними взаимозависимости? Я так понимаю что это разные средства для обхода блокировок. У кого-то стоит podkop, а у кого-то zeroblock вместе zapret, они должны быть вместе или одного достаточно? Я только купил роутер, у меня есть vps с поднятым vless, может подскажите что-то простое чтобы использовать его?

---

**2026-04-12T19:03:01 | Ярослав**
Кстати вот что мне ответил автор zapret2 на тему почему с десктопа все летает, а на мобиле нет:
"Скорее всего это связано с недоисправленным handshake мобильного клиента.
У меня тоже десктопная версия работает через fake tls proxy, а ведроидная нет.
Помогает только дурение со стороны сервака, и то не на всех провайдерах."

---

**2026-04-12T19:21:55 | Александр**
В интерфейсе zapret2 (RR) есть две вкладки blockcheck2 и "Поиск стратегий". Подскажите, плз, в чём их отличия?

---

**2026-04-12T19:23:36 | Routerich**
Здравствуйте.
Если пересечений нет, и zapret2 настроен точечно бить, то все ок

---

**2026-04-12T19:24:38 | Routerich**
Zapret остановите и проверяйте

---

**2026-04-12T20:20:51 | Alexey S**
Можно ли залить в zapret свою стратегию? Не нашёл ни на гитхабе, ни в веб панели

---

**2026-04-12T20:52:45 | Михаил**
чёт я пропустил. а гдевзять пакет zapret2 ?

---

**2026-04-12T21:03:13 | Сергей К**
Добрый день. Роутер с прошивкой 24.10.4 как купил установил скрипт N5 и больше ничего не трогал по принципу "работает -не трожь"  Последние несколько дней начал YouTube подтупливать, Телега отвалилась напрочь и работает только через платный vpn. По телеге наверное решения нет, как я понял? Или ошибаюсь? Вопрос по скрипту N5. Там что-то нужно обновлять или вообще необходимо все сносить и устанавливать уже zapret2 или zero Blok? Тут уже столько сообщений, что поиск по темам выдает большую кучу информации. Прошу простить за вероятно дилетантские вопросы, но уже трудно понять в каком направлении двигаться.

---

**2026-04-12T21:37:44 | Сергей К**
Нет. Podkop и Zapret. Его допом установить? Zero Blok в смысле. Я бы уже его давно воткнул, но нет осознанного понимая, что оставить, а что снести.

---

**2026-04-13T02:09:08 | Bullet for my valentine Poison**
Вам в тему вопросы. Тут обсуждается zapret2

---

**2026-04-13T09:00:26 | Routerich**
а если остановить zeroblock,zapret2 начинают сайты открываться?

---

**2026-04-13T09:47:44 | Роман**
Для обновления того, что нужно. Zapret2, zeroblock, фиксы WiFi, оперу фиксили недавно.

---

**2026-04-13T10:37:57 | Pavel**
Добрый день, делаю все по закрепленному сообщению, zapret2 не появляется

---

**2026-04-13T10:39:03 | Bullet for my valentine Poison**
перезайти в веб-морду. Либо проверить еще в пакетах на наличие, через фильтр Zapret2

---

**2026-04-13T10:40:37 | Pavel**
В пакетах нет zapret2

---

**2026-04-13T10:50:03 | Bullet for my valentine Poison**
инкогнито(кэш надо хорошо почистить) и оба пакета?Zapret2 и luci?

---

**2026-04-13T10:58:59 | Bullet for my valentine Poison**
оба пакета?Zapret2 и luci?

---

**2026-04-13T12:20:06 | Александр Черкашин**
Добрый день, подскажите наиболее оптимальный способ поиска работающих стратегий для Zapret2, встроенный "Поиск стратегий" перебирает 3900+ вариантов, есть ли способ сделать это быстрее?

---

**2026-04-13T12:26:47 | Gomer Simpson**
Ну, подкопа нет, но Zapret висит. Стало быть, просто подкоп удалили и всё на этом? Не-не, так не надо. Надо после подкопа сброс и чистую прошивоньку залить.

---

**2026-04-13T12:29:19 | Gomer Simpson**
Я следствие провожу. Zapret вы ж не специально ставили на свежую прошивку? Есть подозрение, что он остался от скрипта №5.

---

**2026-04-13T13:30:24 | Fos**
Добрый день. Телега не работает на мобилках. Решил попробовать через подкоп ее пустить. Роутер через АСУ обновлял неделю назад, всё остальное через ZB+Zapret2. Куда копать, чтобы подкоп завести?

---

**2026-04-13T14:22:44 | Gomer Simpson**
Дело ваше. Zapret2 - 4k на тв через SmartTube без тормозов.

---

**2026-04-13T16:59:48 | ᅠ ᅠ**
Привет
Подскажи пожалуйста что делать, телега не подымается
Анализ запущен: 2026-04-13 16:55:31
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Устанавливаем/обновляем: wget
Попытка обновления списка пакетов: (1/4)
Списки обновлены успешно
Package uclient-fetch (2024.10.22~88ae8f20-r1) installed in root is up to date.

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.5.205 | YouTube IP:  172.217.19.238

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.21 MB
  Пинг (ya.ru via awg10): 50.057 / 54.499 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock zapret2 opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200 OK) [tlsv1.3] [try: 2]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock              awg10 (vpn): anime,block,discord,googleplay,meta,news,porn,socials,video
  zeroblock          opera (prx out): ai,geoblock,messengers
  zeroblock        DNS/Bootstrap DNS: (doh) 9.9.9.9 / 77.88.8.8
  Версия zeroblock: 0.7.2-r55

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.2 | uptime:  4:32 | (Прошивка: 24.10.5)
  CPU: 0.44 | RAM: 25% | NAND: 42% занято / 39.4M доступно
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-04-13T17:01:22 | Иван Порошин**
Как заменить podcop на ZB и zapret на zapret 2 не сбрасывая роутер?

---

**2026-04-13T17:05:38 | Routerich**
Итак пошаговый мануал для владельцев Routerich, как завести Zeroblock+Zapret2 на дефолтных настройках.
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки" и ждем, закрываем появившуюся табличку нажав на кнопку "Закрыть".
3. Вводим в окне "Фильтр" (слева) Zeroblock. Внизу должны появиться два пакета: Zeroblock и luci-app-zeroblock.
4. Нажимаем кнопку "Установить" напротив каждого пакета.(Первым идет Zeroblock, а затем luci-app). В появившемcя окне жмем еще раз установить. После завершения закрываем окно. 
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4. Жмем по очереди на кнопки: сохранить и применить.
7. Далее ждем примерно 5 минут, выходим и обратно входим в интерфейс роутера. В разделе Службы должен появиться пункт "Zapret2".
8. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
9. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
10. Проверяете работу Youtube на всех устройствах. (так же желательно в браузерах отключить функцию "Частный/безопасный DNS")

---

**2026-04-13T17:22:57 | Алексей Микоянов**
Господа, вдруг кому-то поможет с #Gemini / #NotebookLM. 
Сегодня весь день потратил. После известных событий с отвалом Warp/Opera перешёл на ZeroBlock + Zapret2 + свой VPN на vless. 
Всё заработало, но почему-то не хотели работать Gemini / NotebookLM - not supported in this region. Даже напрямую через VPN, даже США.
Помогло, согласно https://xbox-dns.ru/#setup -> выставить xbox-dns.ru в качестве DoT. 
Причем (вдруг у вас такая же магия получится) - сначала выставил DoT - не помогло. 
Плюнул, выставил 176.99.11.77  в обычном UDP (этот DNS выдаётся через TG-канал их поддержки) - помогло. 
Выставил на DoT, сбросил кэш - по-прежнему работает.


Итого, сейчас секции выглядят так:

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock      Frankfurt (prx url): ai,geoblock,messengers
  zeroblock             NL (prx url): anime
  zeroblock              awg10 (vpn): art,block,discord,googleplay,meta,news,socials,video,youtube
  zeroblock        DNS/Bootstrap DNS: (dot) xbox-dns.ru / 77.88.8.8
  Версия zeroblock: 0.7.2-r55

---

**2026-04-13T18:18:16 | frnchesko178 (Влад)**
У меня тут сбой на пункте 7.
Эти пункты уже установлены в zeroblock, но Zapret2 не появился в службах

---

**2026-04-13T18:41:21 | Routerich**
Здравствуйте.
система->пакеты->обновить списки->
zapret2->установить

---

**2026-04-13T18:51:18 | Cheka**
Извините, что туплю, а куда дальше идти? Где именно zapret2 установить

---

**2026-04-13T18:51:56 | Routerich**
В поле ввода введите zapret2, потом нажимайте установить, там будет два пакета надо оба ставить

---

**2026-04-13T18:52:03 | Timur**
и может лучше zapret 2 не ставить если есть zeroblock?

---

**2026-04-13T18:55:39 | Timur**
в zapret2  что за ?

---

**2026-04-13T19:22:29 | Николаич**
Други добрый вечер. Youtube идет через zapret2 или нет? Стоит искать стратегии через Blockcheck2 - ничего не получается даже с сылками...

---

**2026-04-13T19:39:13 | Anna Bagler**
Поставьте zapret2/1 и подберите стратегию.

---

**2026-04-13T20:05:48 | Ярослав Онищенко**
Podkop и zapret'ы два. Не знаю как не конфликтуют, но всё работает))

---

**2026-04-13T20:12:11 | Роман**
https://github.com/StressOzz/Zapret-Manager
Этим попробуйте обойти блок, там игровые стратегии есть. 
Если не поможет - искать домены игры и добавлять их в подкоп. 
Либо ждать когда выйдет улучшенный zeroblock, там есть фича запуска приложений и игр в обход через политики windows. 
Скрипт может вам что-то сломать, раз вы сами не знаете как оно работает.

---

**2026-04-13T20:29:45 | Gomer Simpson**
ZeroBlock. Из ZeroBlock установить Zapret2.

---

**2026-04-13T20:56:04 | Kiss_My_Axe**
Я вам щас дам, вы попробуете.
Может уже и не надо анблок будет.

Cкопировать. Вставить в терминал роутера.
Ввести 777, нажать ентер.
Как всё установится - нажать ентер, там написано будет.
Перебирать страты 1-10, после применения проверять доступ к трубе.
# СТРАТЕГИИ В ZAPRET1
#
sh <(wget -qO- https://raw.githubusercontent.com/kkkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)
#
#

---

**2026-04-13T20:56:16 | Anna Bagler**
Анблок удаляйте и ставьте zapret2 или zapret. Потом можно пробовать стратегии.

---

**2026-04-13T21:01:00 | Routerich**
Ставьте сразу zapret 2, там легче подобрать стратегию будет

---

**2026-04-13T21:05:27 | Anna Bagler**
Ставьте zapret2, потом проверяйте YouTube на устройствах. Вон Кисс вам все дал для запрет1. Можете пробовать.

---

**2026-04-13T21:10:38 | Routerich**
И luci-app-zapret2. Стратегии обхода. В wiki теме есть мануал. Любой нейронке скормите, по пунктам разжевать сможет

---

**2026-04-13T21:11:19 | Bullet for my valentine Poison**
Zapret2

---

**2026-04-13T21:23:54 | Kiss_My_Axe**
Cкопировать. Вставить в терминал роутера.
Ввести 777, нажать ентер.
Как всё установится - нажать ентер, там написано будет.
Перебирать страты 1-10, после применения КАЖДОЙ проверять доступ к трубе.
# СТРАТЕГИИ В ZAPRET1
#
sh <(wget -qO- https://raw.githubusercontent.com/kkkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)
#
#

---

**2026-04-13T21:52:49 | .**
Где находится этот раздел? В Zapret2&

---

**2026-04-13T22:09:20 | ~**
Ну пока 0 )) Не успеваю вики штудировать роутер у меня 5 день, но и работа съедает массу времени. Осваиваюсь потихоньку, пока только Tailscale настроил и, по старой памяти, накатил zapret и podkop. До RR был некоторый опыт работы с OpenWRT на роутерах Xiaomi AX3000T и NanoPI R3S.

---

**2026-04-13T22:10:38 | bm**
Обновил прошивку на последнюю 24.10.5, естественно Zapret2 отвалился, удалил пакет, обновил систему. Перенакатил Zapret2, выяснил что в базовой стратегии конфликт параметров с range, помогло и взлетело после того как закоментировал все три строки с range.

---

**2026-04-13T22:12:46 | ~**
Ребят, а если не очень сложно, можно в двух словах, чем zapret от zapret2 отличается и чем 2 лучше? Видел тут такие утверждения. Документацию качнул, но, честно, пока не успел ознакомиться.

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

**2026-04-14T00:05:50 | Ярослав**
Для компа легко пробивается zapret2. В соответствующей теме я все расписал.

---

**2026-04-14T00:19:15 | Gomer Simpson**
Если только ютуб и дискорд, ну, может, роблокс ещё - zapret. Есть скрипты с автоподбором стратегий. Для всего остального, кроме телеги, стандартного подкопа вам хватит. Телегу бесплатно почти невозможно завести. Свой впн - лучшее решение. Его тоже можно в подкоп запихать.

---

**2026-04-14T00:58:41 | Роман**
Все в zeroblocke будем! ASU и Zapret братья навек! 😁

---

**2026-04-14T01:03:51 | ufalex**
Ок, подскажите как конкретно на телегу подобрать zapret2? Ибо дофига же доменов или как их там

---

**2026-04-14T01:14:36 | Артем Федоренко**
zapret 2 с vless работает??? может там че куда надо прописать??? 🤯

---

**2026-04-14T09:38:28 | Николаич**
Была рекомендация как установить Zapret1. Не могу разобраться.
Cкопировать. Вставить в терминал роутера.
Ввести 777, нажать ентер.
Как всё установится - нажать ентер, там написано будет.
Перебирать страты 1-10, после применения КАЖДОЙ проверять доступ к трубе.
# СТРАТЕГИИ В ZAPRET1
#
sh <(wget -qO- https://raw.githubusercontent.com/kkkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)
#
#

---

**2026-04-14T10:14:41 | Sharky**
Ок. Но это же получается на конкретный хост - как например ютуб сделан.
А чтобы применялось для всего заблокированного? Zeroblock + zapret2 стоит и то есть ютуб но нет ничего другого, то наоборот. Уже задолбался искать описание и понять что за чем и почему не работает

---

**2026-04-14T10:48:33 | Gomer Simpson**
Есть такое же для Zapret.

---

**2026-04-14T11:05:32 | Gomer Simpson**
Не. Это для Zapret. Просто Zapret. Без цифры 2.

---

**2026-04-14T11:24:38 | Gomer Simpson**
Вы, всё-таки, попробуйте этот скрипт на себе, на своём роутере. Убедитесь, что всё просто. На этом основании порекомендуете своим. Алгоритмы zapret справляются с блоком ютуб лучше, чем юанблок.

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

**2026-04-14T12:28:56 | Михаил Краев**
Подскажите, пожалуйста. 
Вчера ночью настроил zeroblock:
awg10 и proxy со своим vless. Zapret2 выключен. После проверки все ок работало - списки отрабатывали корректно. Сегодня (часов через 10-12) начал отваливаться/пытаться пере подключиться WiFi от разных устройств. Грешу на какие то настройки, возможно в списках CDN cloudflare/google в awg10

---

**2026-04-14T12:36:28 | Artem Mayorov**
Здравствуйте! Имеется данная Великая стратегия. Все супер. На телеках Самсунг работает, но каждое утро приходится перезапускать Zapret2 . Это нормальная история? Мне не в напряг конечно, но все равно... Мало ли...
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4

---

**2026-04-14T12:41:56 | Gomer Simpson**
Система - Планировщик - вставить: 11 5 * * * service zapret2 restart     Первые две цифры минуты, третья часы. Но, что приходится перезапускать, это, конечно не хорошо.

---

**2026-04-14T12:50:41 | Gomer Simpson**
Нет ничего плохого в рестарте сервисов. У меня еженощный ребут ровтера и рестарт ЗероБлок, Zapret2 и Tailscale. Всё работает без проблем.

---

**2026-04-14T13:03:02 | Gomer Simpson**
Рестарт zapret2. Для ребута роутера другая команда.

---

**2026-04-14T13:25:04 | Вадим Гумурзаков**
Поключил zeroblock с zapret2, внес ссылку на свои ключи через "Подписка (удаленный список прокси)". Ключи добавились, пинг отображется. Но кроме YouTube ничего не работает, ни телеграм, ни инстаграм и т.п.

---

**2026-04-14T13:35:27 | Yiliam**
Насчёт тг на андроиде, еле как работает на Zeroblock в секции awg. В  zaprete2 со стратегией ютуба не пошёл, страты не ищет часами ни в блокчеке ни в поиске, крутит крутит без результата, даже те которые раньше находило, по торент доменам например. Оператор мтс. Поитогу работает только ютуб через запрет и немного тг через зероблок, торенты не работают через зероблок.

---

**2026-04-14T13:36:13 | Алексей Микоянов**
кстати, а есть информация, как работают правила в Zapret при наличии правил в подписке Happ? 
Вот допустим есть у меня интерфейс AWG (или любой другой), туда идёт условный IP 89.40.204.117 - то есть, 89.40.204.117 должна идти через AWG
И есть подписка Happ, в которой 89.40.204.117 прописано как direct ( Match: ip ; Action: direct) - то есть, роутить через локальный интерфейс. Каковы действия zapret - через что будет роутить?

---

**2026-04-14T16:20:06 | Anna Bagler**
Локация вашего vpn точно зарубеж? YouTube уберите из списков или отключите и остановите zapret2. xbox в полную маршрутизацию.

---

**2026-04-14T16:47:23 | Sergio Yakovlev**
В YouTube не все грузиться поскажите где чё подправить ZeroBlock или в  zapret

---

**2026-04-14T16:49:44 | Sergio Yakovlev**
Установлен ZeroBlock и zapret

---

**2026-04-14T17:24:26 | Олег Михайлович**
еще небольшой вопрос, ничего не менял, установлено все только что, откуда пересечение podkop|zapret, но все вроде работает

---

**2026-04-14T17:30:49 | .**
добавил zeroblock и zapret2 по инструкции, работает только ютуб и инста по сути. могу ли я как-то добавлять сервисы и сайты куда-то, чтобы оно работало? есть впн wireguard, но я для того, чтобы избавиться от него дома и купил данный роутер. может кто помочь с настройкой? или хотябы объяснить что к чему тут вообще. информации море, я ничерта не понимаю. был бы очень благодарен.

---

**2026-04-14T17:44:26 | .**
приветствую
добавил zeroblock и zapret2 по инструкции, работает только ютуб и инста по сути. могу ли я как-то добавлять сервисы и сайты куда-то, чтобы оно работало? есть впн wireguard, но я для того, чтобы избавиться от него дома и купил данный роутер. может кто помочь с настройкой? или хотябы объяснить что к чему тут вообще. информации море, я ничерта не понимаю. был бы очень благодарен.

---

**2026-04-14T18:40:50 | Volshur**
Спасибо за ответ . Буду пробовать ставить zeroblock+zapret 2. Приобрел сегодня Ваш роутер. На старом стоит подкоп+zapret.  Если не  трудно подскажите, можно ли собрать прошивку сразу с нужными пакетами например с zeroblock+zapret2? Если да то это делать через тестовый сервер ASU?

---

**2026-04-14T18:45:57 | .**
Настроил zeroblock и zapret2
Вроде работает. Есть впн от wireguard, но как его накатывать на роутер вообще не понимаю. Все еще и терминами с абривиатурами сыпят, так что ничего не понятно. На ютубе аналогично. Понял, что нужно впн на влесс ставить, а как - гадай. 
У меня претензий нет, оборудование отличное, веб интерфейс удобный и приятный, но вот с технической точки зрения я совсем не подкован. Думал будет все проще.

---

**2026-04-14T20:26:41 | Михаил Коновалов**
а zapret 1/2 не поможет?) я вообще роутер брал для запрета и как будто он не актуален или мне кажется

---

**2026-04-14T21:26:02 | Bullet for my valentine Poison**
Это вам в первый zapret

---

**2026-04-14T21:37:26 | Anna Bagler**
Cтратегию для zapret2 добавляйте. Вам выше писали уже об этом.

---

**2026-04-14T21:41:09 | Yuriy Krivosheev**
Всем добрый вечер. 
Подскажите пожалуйста, по ситуации ниже. 
Купил роутер, установил по инструкции ZeroBlock, отключил Zapret2. 
Затем добавил новую секцию (остальные отключил), и в новой секции вбил:
Тип подключения - Сервер прокси; 
Тип конфигурации - Подписка;
Ввел URL Vless подписки. 
На вкладке "Списки" все списки сообщения убрал. 
Проверил на вкладке "Панель управления", увидел хосты по Vless подписке, выбрал нужный, сохранил и применил настройки. 
Проверил работу телеги и ютуба на 2х устройствах, все работает без проблем. 

Подскажите, пожалуйста, если я хочу маршрутизировать трафик для духовных и бездуховных (ютуб/тг/прочее) сервисов, правильно ли я понимаю что это мне необходимо делать с помощью вкладки "Секции маршрутизации" и необходимо создавать отдельные секции под каждый тип хостов/списков? 
Мне просто не совсем понятно как работает вкладки "Списки - Списки сообщества". Это хосты, которые должны работать на этой секции? Или наоборот, это список тех, кто на этой секции заблокирован и трафик проходить не должен по ней? 

Или я вообще не туда думаю и есть способ проще? 
Если необходимо скинуть какую-то фактуру, сообщите, пожалуйста. 
Заранее спасибо.

---

**2026-04-15T00:14:23 | Алексей Микоянов**
Господа, тут, кажется, Operу помаленьку начало попускать (по крайней мере, у меня), но я уже перешёл на ZeroBlock / Zapret2. В целом полёт отличный, но хотелось бы пускать NoteBookLM через Оперу. (через свой квн в Немеччине слетает авторизация). 
Вопрос - как-то можно подружить opera-proxy и ZeroBlock, кто-то уже проходил этот путь?  Или не стоит пока пытаться даже?

---

**2026-04-15T01:45:57 | iProxx**
У tuvio на Яндекс ТВ не родной гугловский клиент Ютуба а его модификация. Если через Zapret Ютуб работает на других устройствах (смартфоны, комп) можно и на Я ТВ его завести без подбора стратегий. Для этого достаточно установить на телек TizenTube Cobalt

---

**2026-04-15T06:07:01 | VecH.Pro**
Если при настроенном zapret2
запустить крипт №5, он поломает zapret ?

---

**2026-04-15T06:22:38 | Routerich**
Здравствуйте.
Он его учитывать не будет, и возможно будут проблемы
Так что лучше его остановить перед запуском, потом убрать из Podkop YouTube или остановить и выключить автозапуск Zapret.
А после уже запустить Zapret2.
Но это случай если у вас zapret2 для ютуба

---

**2026-04-15T06:41:55 | Routerich**
Здравствуйте.
не обзяательно.
для работы телеграмма через Zapret2 вам придётся подбирать под него стратегию и удалять список Telegram из Podkop

---

**2026-04-15T09:19:29 | Andrey**
Настроил новый роутер на работу с zeroblock + zapret2 + amneziawg. Хочу вместо амнезии арендовать свой vps и через него трафик пускать. Ткните, пожалуйста, в инструкцию как это сделать 🙂

---

**2026-04-15T09:46:46 | Eduard Ivanov**
Доброе утро. Сделал настройку zeroblock и zapret2. НО! Я так и не понял как дать доступ к сайтам, которые заблочены. Через опера и авг10? ну я пробовал добовлять сайт в список и 0 толку, мб не тот список . Дискорд доступ я так и не смог получить, возможно я как то неправильно перебираю стратегии @_@.  Подскажите пж. 😱😱

---

**2026-04-15T11:53:36 | Aldov27**
Пробую установить zapret 2, как мне написали. Дохожу до этого пункта: пишет, что опера и амнезия установленны. Дальше ставлю галочки, применить, установить. Запрет 2 не появляется. Что может быть не так?

---

**2026-04-15T12:32:56 | Routerich**
luci-app-zapret
только это

---

**2026-04-15T12:33:16 | Routerich**
он по идеи сам подтянет zapret

---

**2026-04-15T12:50:04 | Routerich**
ну кроме пересечения zapret и Podkop я проблем не вижу.
стопайте и отключайте автозапуск zapret и проверьте
потом можно стопнуть Podkop и проверить работу сервисов будут ли ругаться

---

**2026-04-15T12:52:49 | Routerich**
а Podkop/zeroblock/zapret что-то такое используете?

---

**2026-04-15T14:37:05 | Anna Bagler**
Тогда все нужные списки в свою секции. Остальные секции удалить.
YouTube не добавляйте в zeroblock. У вас zapret2 запущен.

---

**2026-04-15T14:58:42 | Sergey**
Проверить что ютуба нет в подкопе и настроить стратегии запрет: 

# АВТОКОНФИГУРАТОР ZAPRET

Попробуйте насканить страт для запрета.
Запустить, после установки нажать 1 ввод.
Начнётся поиск. Он может быть долгим, если чо ложитесь спать.
Как закончит поиск нажмите 2 и ввод.
Будут предлагаться для проверки страты. Как зелёным напишет - запускайте на телефоне/телеке ютуб.
Не работает - ввод. Работает 1 и ввод.
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/zapret_autoconfig/zapret_autoconfig_latest)

---

**2026-04-15T18:59:15 | Anna Bagler**
Отключайте zero, zapret2, что у вас ещё есть. И проверьте.

---

**2026-04-15T19:01:27 | Олег **
Добрый вечер! В телеграмме не грузятся фото, картинки, видео. Как можно исправить? стоит ZeroBlock и Zapret2.

---

**2026-04-15T19:43:49 | Anna Bagler**
Cписки изучайте и добавляйте, discord или в zapret2, или в zero.

---

**2026-04-15T20:04:21 | Docvspb 🇷🇺**
Друзья, я установил Zeroblock, Zapret 2. У меня заработало все: Youtube, Instagram, десктопный и мобильный Whatsapp. Все работает на хорошем уровне (СПб). 
Тут пишут про скрипт 5. Напомните, пож, для чего он? Мне он нужен? 

Если все так и останется (хотя не верится даже), то я задумываюсь только о доступе к роутеру извне, с телефона, на котором подключен мобильный интернет (если это возможно, конечно 🤔).

---

**2026-04-15T20:33:54 | Дмитрий Григорьев**
Всё норм здесь, да, искать стратегию, не иначе
первый запрет не пробовали? Через Zapret-manager можно стратежки перебирать от Flowseal например, но после второго запрета уже не то пальто

---

**2026-04-15T20:35:38 | Ruslan Bilyk**
Я до роутера пользовался zapret от flowseal. Alt 3. Можно как-то его перенести в zapret2? ))

---

**2026-04-15T20:37:21 | Дмитрий Григорьев**
А там уже как по накатанной, ставить zapret-manager через терминал и тыкать тест стратегий

---

**2026-04-15T21:05:12 | Николай**
Здравствуйте, подскажите пожалуйста, хочу воспользоваться vpn, через платный конфиг файл.
Отключил awg10
Создал интерфейс awg0, поставил в настройках AmnesiaWGVPN, вставил конфиг файл. Но трафик не проходит через него. Всё  подкоп, zeroblock, zapret и тд отключал.

---

**2026-04-15T21:51:20 | Роман**
Очень странно. Zapret manager использовали?

---

**2026-04-15T21:57:22 | Николай Каменных**
Привет!
Такой вопрос 
При переносе в секцию с впн подпиской YouTube надо что-то ещё дополнительно переносить?
И надо ли отключить zapret2?

---

**2026-04-15T22:08:01 | Ruslan Bilyk**
Как решить крит. ошибку?
= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  31.13.72.36 | YouTube IP:  172.253.130.190
  Интерфейс awg10 не существует, или отключен.
  Программы в автозапуске: zeroblock zapret2 opera-proxy youtubeUnblock

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Внутреннее пересечение в youtubeUnblock:
    youtubeUnblock            : YouTube (Условия: default)
    youtubeUnblock            : YouTube (Условия: default)
    Домены: googlevideo.com youtube.com

  zeroblock               AWG2 (vpn): ai,anime,block,geoblock,messengers,meta,porn,socials
  zeroblock        DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8
  Версия zeroblock: 0.7.2-r55

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 | uptime:  4:56 | (Прошивка: 24.10.5)
  CPU: 0.21 | RAM: 25% | NAND: 24% занято / 51.3M доступно
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

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

**2026-04-16T06:37:25 | Denis**
Хороший вопрос. Как минимум отключить zapret, в скрипте прописать.

---

**2026-04-16T09:45:59 | Андрей**
Всем доброе утро!
Увидел закономерность при включённом zapret 2 перестают открываться сайты 2ip.ru, 2ip.io, whoer... Если выключить его, всё открывается. zapret 2 на дефолте, только секция для youtube. С этим можно что-то сделать?

---

**2026-04-16T10:26:41 | Скептик**
Доброго дня!
Подскажите - что не так? Сегодня YT отвалился. awg10 отключен мной, его заменил интерфейс на моём ключе AmneziaWG20:
Анализ запущен: 2026-04-16 14:21:03
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.1.8 | YouTube IP:  172.217.19.238

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP ENABLED AutoStart: ON | ↓0.00 MB / ↑0.22 MB
  Пинг (ya.ru via awg10): ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (77.88.44.242): 56 data bytes
  Программы в автозапуске: zeroblock zapret2 opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОФЛАЙН
--------------------------------------------------------------
  curl: (28) Connection timed out after 5000 milliseconds
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:     127.0.0.1:53
    Name:       youtube.com        Address: 172.217.19.238

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock       AmneziaWG_20 (vpn): ai,art,discord,games,googleplay,messengers,meta,music,news,porn,repo,socials,tools,video
  zeroblock          opera (prx out): geoblock,block
  zeroblock        DNS/Bootstrap DNS: (doh) 9.9.9.9 / 77.88.8.8
  Версия zeroblock: 0.7.2-r55
  !!!_AmneziaWG20: "Не создавать маршруты" не установлен в 1

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.2.1 | uptime: 41 min | (Прошивка: 24.10.5)
  CPU: 5.32 | RAM: 32% | NAND: 68% занято / 21.9M доступно
  */10 * * * * /usr/bin/zeroblock bad_interface_check >/dev/null 2>&1
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-04-16T11:12:42 | Vasa**
https://github.com/GubernievS/AntiZapret-VPN

---

**2026-04-16T11:44:23 | Скептик**
Доброго дня!
В "Интернете без границ", видимо, ответа нет - задам сюда, в профильную ветку.
Подскажите - что не так? Сегодня YT отвалился. awg10 отключен мной, его заменил интерфейс на моём ключе AmneziaWG_20:
Анализ запущен: 2026-04-16 14:21:03
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.1.8 | YouTube IP:  172.217.19.238

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP ENABLED AutoStart: ON | ↓0.00 MB / ↑0.22 MB
  Пинг (ya.ru via awg10): ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (77.88.44.242): 56 data bytes
  Программы в автозапуске: zeroblock zapret2 opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОФЛАЙН
--------------------------------------------------------------
  curl: (28) Connection timed out after 5000 milliseconds
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:     127.0.0.1:53
    Name:       youtube.com        Address: 172.217.19.238

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | RUNNING                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock       AmneziaWG_20 (vpn): ai,art,discord,games,googleplay,messengers,meta,music,news,porn,repo,socials,tools,video
  zeroblock          opera (prx out): geoblock,block
  zeroblock        DNS/Bootstrap DNS: (doh) 9.9.9.9 / 77.88.8.8
  Версия zeroblock: 0.7.2-r55
  !!!_AmneziaWG20: "Не создавать маршруты" не установлен в 1

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.2.1 | uptime: 41 min | (Прошивка: 24.10.5)
  CPU: 5.32 | RAM: 32% | NAND: 68% занято / 21.9M доступно
  */10 * * * * /usr/bin/zeroblock bad_interface_check >/dev/null 2>&1
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-04-16T12:01:41 | Bullet for my valentine Poison**
Амнезию купить и не страдать. Или идти на ntc.party в тему zapret2

---

**2026-04-16T12:17:33 | Anna Bagler**
Он у вас точно через awg20 или через zapret2 пытается?

---

**2026-04-16T13:56:19 | Ruslan Bilyk**
Добрый день! Помогите пожалуйста! Во вкладке zapret2 если нажму на эту кнопку, то сброшу все настройки роутера или только zapret2?

---

**2026-04-16T14:00:48 | Anna Bagler**
Логично, что для zapret2.

---

**2026-04-16T14:04:20 | Alex L**
Аналогично , поставил ZeroBlock + Zapret2  , создал секцию прокси с платным  vless  .  awg и оперу удалил  . Всё работает ( 9999/dot , mgts/gpon ) кроме gemini  , но им редко пользуюсь . Когда надо - запускаю cisco anyconnect через Германию .  Пробовал прописать в ZB , создав интерфейс на опенконнект и секцию в ZB , но через неё работают только соцсети - fb, insta  , больше практически ничего и youtubе тоже не работает , секция всегда красная , не знаю как настроить и куда ещё смотреть в настройках.

---

**2026-04-16T14:16:14 | Ruslan Bilyk**
Ребят, а списки сообщества в zapret2 можно где-то посмотреть?

---

**2026-04-16T14:54:46 | Денис Сурков**
Всем привет, наверное уже есть решение, но в чате не смог найти. У меня стоит ZeroBlock + Zapret2, настроенное remote control с телефона до роутера. А проблема в том, что телеграм на телефоне очень долго крутит обновление, подключение быстро проходит, но вот обновление очень долго, может так минут 7-10 висеть. Есть уже решение по такой проблеме?

---

**2026-04-16T15:40:58 | Денис**
В закрепе Zapret2

---

**2026-04-16T15:44:54 | Ярослав**
Пробовал zapret2 на t.me Ростелеком Москва. Кто нибудь будет проверять на работоспособность?
--payload=tls_client_hello --lua-desync=fake:blob=0x00000000:tcp_flags_unset=ACK:repeats=1 --lua-desync=fake:blob=fake_default_tls:tcp_flags_unset=ACK:tls_mod=rnd,dupsid:repeats=1

---

**2026-04-16T16:52:32 | Денис**
Добрый день, вчера получил роутер, настроил по гайду zeroblok и zapret 2 вчера все работало ок сегодня плохо работает ютуб на телевизоне не все видео грузит, и не работает 4pda не загружаеться сайт c мобильного инета все оке.
я новичек в этой теме по этому если  нужно что то скинуть то сделаю

---

**2026-04-16T17:28:51 | Сергей Замогильный**
Товарищи здравствуйте, подскажите пожалуйста установил Zapret2, а он не появился у меня в службах. Его как то переустановить можно? Спасибо заранее.

---

**2026-04-16T17:40:45 | Роман**
Система пакеты обновить списки фильтр zapret2 - что там?

---

**2026-04-16T17:42:30 | Docvspb 🇷🇺**
Я роутер на днях получил. Делал всё по инструкции: Zeroblock, Zapret2. Больше ничего не менял. Все работало отлично. Я не готов к экспериментам: боюсь все сломать. Мне нужно чётко понимать: доустановить пакет / удалить пакет, и что получится в результате? Если можете подсказать более конкретно, был бы благодарен...

---

**2026-04-16T17:45:41 | iProxx**
Если Zeroblock ставили то Youtube работает через Zapret2, а не через Youtubeunblock как на дефолтных настройках.

---

**2026-04-16T17:48:46 | ⓞ ᗰ**
Почему Zapret после перезагрузки устройства остается выключенным? В автозапусках вот так ☝️

---

**2026-04-16T18:20:56 | Ruslan Bilyk**
Причём Discord у меня не работает ни в zapret2 ни в ZB через AWG. Когда я его в ZB включаю. А zapret2 только в самом начала нашел стратегии быстро на discord. Я вставил их, проверил - не работает. Не знал, что нужно по одной удалять и удалил все. После этого он не находит ни одной...

---

**2026-04-16T18:27:40 | Dmitry**
Подумываю перебраться с podkopa на zeroblock+zapret2 случайно нет скрипта для автоматической установки и настройки по типу скрипта N5

---

**2026-04-16T18:33:15 | Ruslan Bilyk**
Вот что пишет в начале.
* checking system
Linux/openwrt detected
kernel: Linux version 6.6.119 (builder@buildhost) (aarch64-openwrt-linux-musl-gcc (OpenWrt GCC 13.3.0 r29087-d9c5716d1d) 13.3.0, GNU ld (GNU Binutils) 2.42) #0 SMP Wed Dec 17 21:08:22 2025
distro: RouteRich 24.10.5
openwrt release: RouteRich 24.10.5 r29087-d9c5716d1d RR-3.9.0
openwrt board: mediatek/filogic
openwrt arch: aarch64_cortex-a53
firewall type is nftables
CURL=curl
curl 8.12.1 (aarch64-openwrt-linux-gnu) libcurl/8.12.1 mbedTLS/3.6.5 nghttp2/1.63.0
Release-Date: 2025-02-13
Protocols: file ftp ftps http https ipfs ipns mqtt
Features: alt-svc HSTS HTTP2 HTTPS-proxy IPv6 Largefile SSL threadsafe UnixSockets
* checking already running DPI bypass processes
* checking privileges
* checking prerequisites
* checking DNS
system DNS is working
comparing system resolver to public DNS : 8.8.8.8
pornhub.com : OK
ej.ru : OK
rutracker.org : OK
www.torproject.org : OK
bbc.com : OK
checking resolved IP uniqueness for : pornhub.com ej.ru rutracker.org www.torproject.org bbc.com
censor's DNS can return equal result for multiple blocked domains.
all resolved IPs are unique
-- DNS looks good
-- NOTE this check is Russia targeted. In your country other domains may be blocked.
* checking virtualization
cannot detect

NOTE ! this test should be run with zapret or any other bypass software disabled, without VPN



* port block tests ipv4 discord.com:443
ncat -z -w 2 162.159.128.233 443
162.159.128.233 connects
ncat -z -w 2 162.159.137.232 443
162.159.137.232 connects
ncat -z -w 2 162.159.136.232 443
162.159.136.232 connects
ncat -z -w 2 162.159.135.232 443
162.159.135.232 connects
ncat -z -w 2 162.159.138.232 443
162.159.138.232 connects

---

**2026-04-16T19:18:19 | Bullet for my valentine Poison**
Поставьте вручную, система-пакеты. И в фильтр вписать zapret2

---

**2026-04-16T20:11:20 | Gomer Simpson**
Угу. Blockcheck от второго Zapret'а.

---

**2026-04-16T20:56:53 | Bullet for my valentine Poison**
Это нормально, zapret2 сложен в освоении. Потом проще будет.

---

**2026-04-16T20:58:49 | Key**
Система - пакеты.
Фильтр на Zapret2. Устанавливаете zapret2 и zapret2-luci. Все остальное что может корректировать ваш ютуб траффик либо удаляйте, либо выключайте

---

**2026-04-16T21:03:06 | Bullet for my valentine Poison**
И в фильтр Zapret2

---

**2026-04-16T21:07:58 | Ruslan Bilyk**
Чем можно попробовать заменить zapret2, если он не работает. Zeroblock тоже не работает когда я включаю в нём discord. Ну точнее дискорд не работает

---

**2026-04-16T21:08:42 | Gomer Simpson**
Zapret 1 попробуйте. К нему есть скрипты автоподбора стратегий.

---

**2026-04-16T21:09:32 | Bullet for my valentine Poison**
ну в фильтр введите полностью zapret2

---

**2026-04-16T21:17:13 | Александр**
zapret2 должен появиться в разделе "службы " я так понимаю  ?

---

**2026-04-16T21:19:09 | Ruslan Bilyk**
Ну у меня иногда в браузере на ноунейм сайтах пишет, что что-то с dns. Мол проверьте dns over https и т.д.
Вот я и подумал, может это как-то связано с тем, что zapret2 не видит discord.com

---

**2026-04-16T21:23:16 | Ruslan Bilyk**
Ладно, я не знаю уже. Голова кипит. У меня и на телефоне и на компе одинаковая ситуация. Значит что-то в роутере. Почему-то zapret2 не получает домен. Но со списками всё нормально

---

**2026-04-16T21:28:19 | Ruslan Bilyk**
Я отключил zapret2 и zeroblock, а сайт всё равно не открывается. Который про какую-то игру. И я почти уверен, что он не заблокирован и т.д.

---

**2026-04-16T21:57:32 | Vitaly**
Всем привет,
есть,
Routerich AX3000 v1
RouteRich 24.10.5 (r29087-d9c5716d1d) RR-3.9.0
прошу подсказать  
если просто проставить пакет \ службу Zapret2
Ютуп будет из коробки работать ?
( интернет ЦФО - ДомРУ)
( пока Запрет2 и ЗероБлок - отключил )

---

**2026-04-16T22:07:43 | Honest Fox**
Здравствуйте, почитал мануал к zeroblock, поставилось zeroblock+zapret2 и вроде всё работает, но можно мне тыкнуть пальцем куда можно ткнуть свой впн ( типа подписка, там ссылку только дают) в zeroblock, сказали что так можно, но я никак не найду

---

**2026-04-17T07:24:50 | Molodoy Makkonehi**
zeroblock удобнее:
1. удобнее рбаотать с секциями
2. из под коробки поддерживает саб линки с автосвапом
3. xray (хз подкоп ворде только vless)
4. автоматом ставит zapret2
это то что прям маст хев. поправьте если чтото не так написал

---

**2026-04-17T09:32:52 | Kuz Ka**
И zapret2 тоже отдельно ставят?

---

**2026-04-17T09:35:06 | Александр Самсонов**
При подборе стратегий, в самом начале ругается на днс 
"comparing system resolver to public DNS: 8.8.8.8 
bbc.com: MISMATCH - possible DNS hijack!
  WARNING: DNS spoofing detected. ZAPRET may not help without DNS fix." как пофиксить, если это критично?

---

**2026-04-17T09:47:59 | Роман**
Zeroblock со своими серверами, zapret2 для Дискорда и Ютуба, стандартнаые списки, никаких специальных доменов не вносил.

---

**2026-04-17T11:34:51 | Виктор**
Обновил прошивку, установил Zeroblock. Не все сайты доступны. В Zapret2 запустил вечером поиск стратегий, утром все искал, может ищет до сих пор. Это нормально? И интернет сильно тупил.

---

**2026-04-17T11:47:14 | The Wisest**
Нажал на эти пункты, три поставились без проблем, а Zapret2 — нет

---

**2026-04-17T11:47:52 | The Wisest**
Именно с Zapret2 возникает эта ошибка

---

**2026-04-17T11:56:25 | Bullet for my valentine Poison**
А отвлекся. Зайдите в система-пакеты. Нажмите обновить списки. Потом слева в фильтр впишите Zapret2 и установите. После очистить кэш и перезайти в веб-морду. В службах появится Запрет2. После вернуться в автонастройку Зероблока и поставить галки на Автозагрузку (там два пункта), сохранить и применить.

---

**2026-04-17T16:17:31 | IT**
Правильно, что я обновляются периодически только:
zeroblock
zapret2
operaproxy
amnezia
Больше ничего особе не надо обновлять из реп?

---

**2026-04-17T17:19:43 | Routerich**
Zapret 1/2

---

**2026-04-17T19:21:33 | The Wisest**
Можно в Zapret2 добавить стратегию для дискока?

---

**2026-04-17T19:22:45 | Anna Bagler**
В теме zapret2 посмотрите готовые. Или тогда подбирайте свою.

---

**2026-04-17T21:27:32 | Routerich**
В теме wiki есть мануал по zapret 2, почитайте. Конфликтует

---

**2026-04-17T21:46:49 | Routerich**
С lg сложно. Вам лучше сделать так. Система - пакеты - вкладка установлено, в фильтре написать youtubeUnblock и удалить. Далее обновить списки и поставить zapret2. В теме zapret2 есть стратегии разные уже готовые в закрепе. Их пробовать

---

**2026-04-17T21:47:40 | Gomer Simpson**
Попробуйте Zapret2. Для тв LG есть стратегия. На лыжи вообще сложно что-то рабочее подобрать. https://t.me/routerich/462347/522134

---

**2026-04-17T22:22:48 | Александр Овсянников**
Всем доброго вечера.
Сейчас стоит 5ый скрипт, до последней недели всё было хорошо, а с прошлой пятницы начались проблемы.
Секция Дискорд не работает.
Main вроде ворочается но очень туго, если правильно понял сейчас все переходят на zeroblock + zapret2(если не прав поправьте)
Существует какой-то скрипт? Или может быть подробная инструкция?
Версия так же 24.10.4 остаётся?

---

**2026-04-17T22:31:38 | Gomer Simpson**
Система - Пакеты. Фильтр zapret2.

---

**2026-04-17T22:32:49 | М П**
zapret2 и luci-app-zapret2 тоже надо устанавливать ?

---

**2026-04-17T22:40:37 | М П**
пожалуйста подскажите ( Перейдите в Services → Zapret2
3. В разделе Settings:
• Включите Enabled) я в разделе настроек что включить туплю не могу понять

---

**2026-04-17T23:21:13 | Docvspb 🇷🇺**
Здесь часто пишут, что бесплатные варианты более не работают. Я могу сказать, что делал все по инструкции на роутере из коробки (ZeroBlock, Zapret 2). Не меняя ничего больше. 
Работают на ПК и телефоне Youtube, Instagram, Linkedin, Whatsapp. Telegram работает на телефоне. Только почему-то в группе этой не загружаются скриншоты. С остальными пользователями могу ими обмениваться. Браузерная версия Telegram тоже работает, но в ней я могу и скриншоты просматривать. 
Короче, все базовые приложения и сайты работают у меня без платных ключей/подписок.

---

**2026-04-18T00:24:04 | Tony Montana**
Всем привет.
Ребят подскажите что не так, после покупки роутера установил себе zapret. Всё было отлично вся МЕТА вселенная работала в том числе и ютуб. 
Позавчера разом все перестало работать. Запустил запрет заново, с телефона работает а с телика нет.
 Решил установить zeroblock, всё сделал по инструкции! Почему то запрещена так и не работает. Ещё почему то из списков сообществ убираю ютуб, сохраняю применяю. А он всё равно в списках остаётся!
Что сделал не так??

---

**2026-04-18T03:03:33 | Routerich**
Отключите zapret и Зероблок временно и попробуйте ещё раз скрипт запустить

---

**2026-04-18T04:06:50 | Kiss_My_Axe**
Выкатил, крч, 0.1.0. Переделал схему чека доступов, теперь проверяются не только авг10 и опера, но и влесс, и прочее.
Маленький рефакторинг рефакнул, а то всё из лоскутков было сшито, в процессе добавления новых фич просто впиливал кусок кода и многие части дублировались, ибо лень, да и нафиг не надо. Подкудрявил-причесал.

Ссылки на всякий гит лучше делать типа так (но это уже прям монструоз страфный, зато работает).
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# Скопируйте ВЕСЬ этот текст нажав на полоску верху (рамка сообщения), или кнопку "скопировать код" в клиенте на телефоне.
# Вставьте в терминал роутер и дождитесь завершения выполнения, cкрин-фото-текст результата пришлите.
#
#
___z_stat=$(/etc/init.d/zapret status)
___y_stat=$(/etc/init.d/youtubeUnblock status)
/etc/init.d/zapret stop
/etc/init.d/youtubeUnblock stop
sh <(wget -qO- https://raw.githubusercontent.com/kkkkkCampbell/master/refs/heads/test_config_script/test_config_script_nightly)
[ "${___z_stat}" = "running" ] && /etc/init.d/zapret start >/dev/null
[ "${___y_stat}" = "running" ] && /etc/init.d/youtubeUnblock start >/dev/null
#

---

**2026-04-18T08:19:43 | Николаич**
После сброса на заводские установил zeroblock + zapret2. В zapret2 нет дефолтных страт, как установить?

---

**2026-04-18T11:03:25 | Gomer Simpson**
Я вам щас дам, вы попробуете.
Может уже и не надо анблок будет.

Cкопировать. Вставить в терминал роутера.
Ввести 777, нажать ентер.
Как всё установится - нажать ентер, там написано будет.
Перебирать страты 1-10, после применения проверять доступ к трубе.
# СТРАТЕГИИ В ZAPRET1
#
sh <(wget -qO- https://raw.githubusercontent.com/kkkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)
#
#

---

**2026-04-18T11:06:14 | Andrew**
Здравствуйте.  Вчера обновил прошивку до 24.10.5 USB 2.0 со сбросом настроек. Установил Zapret в итоге на компьютере через браузер ЮТЮБ РАБОТАЕТ, на телефоне Google Pixel 8 ( Android 16) ЮТЮБ РАБОТАЕТ. Остальная запрещенка ФБ, ИНСТА, , telegram и тд HE РАБОТАЕТ НИГДЕ, НЕ С ТЕЛЕФОНА НИ ЧЕРЕЗ БРАУЗЕР.  Но самое обидное что на компьютере, телефоне ЮТЮБ РАБОТАЕТ, а на телевизоре на базе ANDROID 7, увы ЮТЮБ НЕ РАБОТАЕТ, также же телевизор на значке Wi-Fi показывает что нет интернета, но Интернет по факту на телевизоре есть работает рутуб, гуглплей, другие онлайн кинотеатры.
Что можно подшаманить с настройками чтобы ютюб на телевизоре заработал ? 😇

---

**2026-04-18T11:29:03 | Alexx**
А кто то  пробовал пустить BatleFileld 4 через Zapret 2? А то в Wiki есть скрипт для BF6 и Zapret 1

---

**2026-04-18T11:46:55 | Roman**
здравствуйте, подскажите, пожалуйста, как установить zapret2. прошивка новая и скрипт 5

---

**2026-04-18T11:51:11 | Bullet for my valentine Poison**
Система-Пакеты-Нажать кнопку "Обновить списки"-В фильтр слева вписать Zapret2-установить 2 пакета-перезайти в веб-морду

---

**2026-04-18T13:15:35 | Сергей🇷🇺**
попробую поставить zapret manager тогда

---

**2026-04-18T13:28:18 | Константин**
В нашей локации ну это видимо пока. Трём товарищам посоветовал, все завелось из коробки так же как и у меня, операторы разные.  Ютуб так вообще сразу с базовым анблоком. Тестил zeroblock+zapret2 awg opera proxy так же все без проблем подтянулось и заработало. Сейчас все это конечно настроено под себя, ненужное убрано типа awg и opera добавлены свои каналы так скажем.

---

**2026-04-18T13:51:54 | Alexx**
Добрый день. Стоит Zeroblok и Zapret2 + внешний КВН на Amnezia2.0. Даже почти все работает (Телега, Ютуб, Diskort) одна проблема хотел поиграть в BF4 ничего не работает (не видит серваков). Подскажите пожалуйста куда копать? Уже голову сломал не могу понять почему.

---

**2026-04-18T14:18:42 | Timur**
подскажите пожалуйста как подобрать под своего провайдера настройки zapret2?

---

**2026-04-18T14:27:36 | Николаич**
Еще  вопрос, не могу определить ютуб идет через z2 или awg10? Открываю YACD, там awg10, Zapret2 нет. Если стопану zeroblock ютуб падает. В списках awg10 включен Google Play и CDN Google. Если их уберу из списка  ютуб не работает. Как вылечить?

---

**2026-04-18T14:38:59 | Vadim**
Подскажите как добавить конркетный IP чтобы он шёл в обход РКН? 
Сейчас настроено zeroblock и zapret2

Вроде простая задача, но никто не смог помочь. 

Поэтому думай взять обычный роутер и на нём настроить wireguard на конретный IP, потому не знаю как это сделать на routerich

---

**2026-04-18T15:38:04 | Андрей**
Добрый день, подскажите пожалуйста почему почему отсутствует zapret2? Обновление списка не помогает...

---

**2026-04-18T16:46:06 | Марк**
подскажите из-за чего может не скачиваться zapret 2? после нажатия сохранить и принять происходит маленькая прогрузка и все. Заходил и через 5 минут и через 10, кэш чистил, но ничего не появляется в службах. Единственное что не проставил галочки на первых двух функциях, ибо они уже устновлены

---

**2026-04-18T16:47:40 | Bullet for my valentine Poison**
Бывает, зайдите в система-пакеты. Там слева в фильтр вбить Zapret2 и нажать кнопку Обновить списки. Появятся два пакета, их установить.

---

**2026-04-18T17:30:05 | Vladislav Ivshin**
всем привет, пытаюсь найти рабочую стратегию для запрета, использую zapret2-finder(или Поиск стратегии в гуи), можете подсказать, что значит fixed и broken, и может ли быть fixed 14/14?
[21/4050] fake_default_tls_ttl4_ackdrop
          --payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:ip_ttl=4:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1
          fixed:  +10/14 SE.AKM-01(3.1M), US.CDN77-01(64K), US.CF-01(149K), US.CF-02(100K), LU.GCORE-01(121K), FI.HE-02(146K), FI.HE-03(1.0M), NL.SW-01(167K), DE.VLTR-01(623K), US.VLTR-01(76K)
          broken: !8/19 FR.CNTB-01(15K), FR.CNTB-02(15K), US.DO-01(0B), US.DO-02(0B), US.DO-03(0B), US.MBCOM-01(19K), FR.OVH-01(0B), FR.OVH-02(0B)

---

**2026-04-18T17:58:21 | ~**
Нейронки как раз лучше через свой запустить. Рекомендую пакеты AI и Messenders пустить через секцию со своим vless. А со всем остальным вполне справляются zapret2 и awg10.

---

**2026-04-18T19:08:44 | Gomer Simpson**
Не, я слишком ленив. Опера работала, авг, вроде, сам менял конфиги при перезапуске ZB, и Zapret'ы не подводят.

---

**2026-04-18T19:52:47 | Volshur**
Было у кого так же? По умолчанию zapret2 со стандартной стратегией ломает пол интернета? Сайты выдают ERR_CONNECTION_RESET. ,(Ютюб при этом работал)  Ковырял ZB менял днсы итд ИТП  не туда копал. Вырубил zapret2 и стало все работать, поменял стратегию в zapret2 и стало все норм. Использую запрет только для Ютюба.

---

**2026-04-18T20:37:35 | Игорь**
Вам даже не надо ничего самому прошивать - прошивка уже стоит.
Ставим zapret2, podkop и wireguard.

Арендуем VPS с предустановленным 3x-ui, настраиваем, получаем ссылку, копируем в подкоп и всё работает. Сколько можно...

---

**2026-04-18T21:11:01 | Дестападор**
Добрый день, есть какие-то хорошие схемы разблокировки ТГ на уровне роутера без ВПН/проксей? Сейчас стоит zeroblock и zapret2, может что обновить можно?

---

**2026-04-18T21:11:44 | Anna Bagler**
Ставить запрет2 и стратегию из темы zapret2, анблок удалять.

---

**2026-04-18T23:25:48 | Митсумото Сузуки**
Если не поможет можно снести Зб и Запрет 2

Поставить Запрет 1 с меню

sh <(wget -O - https://raw.githubusercontent.com/StressOzz/Zapret-Manager/main/Zapret-Manager.sh)

В меню выбираем:
9) Удалить-установить-настроить Zapret

И скачай отдельно пакет https-dns-proxy

---

**2026-04-19T00:23:18 | Ilya G**
Друзья, подскажите какие домены нужно добавить для telegram?

Я использовал вот эти 
https://github.com/Flowseal/zapret-discord-youtube/issues/5820

Но у меня только текстовые сообщения отображаются. А картинки и видео - нет. Крутится прелоадер и без результата.

---

**2026-04-19T00:23:28 | Gomer Simpson**
Впн у вас не очень, наверное. А для ютуба Zapret'ы существуют. Там в 4k без тормозов.

---

**2026-04-19T00:27:55 | 𝕮𝖞𝖇𝖊𝖗 𝕮𝖗𝖔𝖜**
Ну и как мне и зероблок и zapret настроить в таком случае для разных сценариев? 
Или мне их туда-сюда щелкать?

---

**2026-04-19T00:34:17 | iProxx**
Ютуб через Zapret работает в 4K. Не надо его через Vless пускать

---

**2026-04-19T00:34:56 | Vladislav Arturovich**
просто Zapret поставить в службы, верно же понимаю ?

---

**2026-04-19T00:36:18 | iProxx**
Ставьте Zeroblock. В нем уже есть Zapret2, и потом свою секцию с Vless добавьте

---

**2026-04-19T07:22:20 | Виталий**
Здравствуйте! Сбросил роутер до заводских, хочу подключить модем E3372.
Есть свой Vless, нужно ли сначала подключать роутер по проводу от провайдера и ставить Zeroblock и Zapret, или сразу воткнуть модем и всё устанавливать подключившись к модему?

---

**2026-04-19T08:46:56 | Руслан Покатилов**
Можно ли как-то настроить zeroblock и zapret 2 что бы скорость не падала почти в половину?

---

**2026-04-19T10:56:18 | Kiss_My_Axe**
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# Скопируйте ВЕСЬ этот текст нажав на полоску верху (рамка сообщения)
# Вставьте в терминал роутер и дождитесь завершения выполнения, cкрин-фото-текст результата пришлите.
#
#
___z_stat=$(/etc/init.d/zapret status)
___y_stat=$(/etc/init.d/youtubeUnblock status)
/etc/init.d/zapret stop
/etc/init.d/youtubeUnblock stop
sh <(wget -qO- https://raw.githubusercontent.com/kkkkkCampbell/master/refs/heads/test_config_script/test_config_script_nightly)
[ "${___z_stat}" = "running" ] && /etc/init.d/zapret start >/dev/null
[ "${___y_stat}" = "running" ] && /etc/init.d/youtubeUnblock start >/dev/null
#

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

**2026-04-19T12:29:50 | Bullet for my valentine Poison**
Открыть система-пакеты. Нажать "Обновить списки", слева в фильтр вписать Zapret2 и установить два пакета

---

**2026-04-19T12:29:53 | Gomer Simpson**
Система - Пакеты. Фильтр zapret2. Установить два пакета.

---

**2026-04-19T12:31:59 | Gomer Simpson**
5 скрипт поставит zapret 1

---

**2026-04-19T15:48:46 | ~**
Всем привет!
Читаю мануал по zapret2-finder и никак понять не могу, предполагается же что настройки выполняются через терминал? Пытаюсь выполнить команды, что из корневой папки, что из папки с zapret2, но всё время получаю:
-ash: zapret2-finder: not found
Что делаю не так?

---

**2026-04-19T16:28:53 | Алексей**
Добрый день. Наблюдаю проблему подключения к WebEx. Установлен zeroblock + zapret2. В какую сторону смотреть?

---

**2026-04-19T16:31:55 | Routerich**
Время на роутере проверьте и отключите youtubeUnblock или Zapret если они у вас есть и пробуйте заново

---

**2026-04-19T16:34:33 | Igor Korsakov**
не подскажите, у меня проблемы с zapret2?

---

**2026-04-19T16:50:48 | Дмитрий З**
Логично же, что раз ЭТО в ветке про Zapret2 - то туда и запихивать?

---

**2026-04-19T16:51:28 | Марк**
очень остроумно, но речь шла конкретно в какую строку в zapret 2 это запихивать)

---

**2026-04-19T17:40:34 | Igor Korsakov**
изначально у меня телега не работает, вот и ковыряюсь и дошёл до команды, которая показывает, что не не запущен zapret2. Я видимо не понимаю, о чём вы говорили "в инкогнито проверяйте"

---

**2026-04-19T18:30:49 | Вячеслав Шевченко**
awg10 это бесплатный впн я его отрубил вместо него MyAmnezia. и не ясно почему показывает zapret2 статус остановлен. в то время когда на самом деле он запущен

---

**2026-04-19T18:54:07 | Routerich**
А у вас он в Zeroblock выбран или в zapret2?

---

**2026-04-19T18:55:24 | Kiss_My_Axe**
Тогда помогалочка.

# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# Скопируйте ВЕСЬ этот текст нажав на полоску верху (рамка сообщения), или кнопку "скопировать код" в клиенте на телефоне.
# Вставьте в терминал роутер и дождитесь завершения выполнения, cкрин-фото-текст результата пришлите.
#
#
___z_stat=$(/etc/init.d/zapret status)
___y_stat=$(/etc/init.d/youtubeUnblock status)
/etc/init.d/zapret stop
/etc/init.d/youtubeUnblock stop
sh <(wget -qO- https://raw.githubusercontent.com/kkkkkCampbell/master/refs/heads/test_config_script/test_config_script_nightly)
[ "${___z_stat}" = "running" ] && /etc/init.d/zapret start >/dev/null
[ "${___y_stat}" = "running" ] && /etc/init.d/youtubeUnblock start >/dev/null
#

---

**2026-04-19T18:59:17 | Maxim =)))**
Вопрос, что с Zapret2 делать 🤷‍♂️

---

**2026-04-19T19:01:43 | iProxx**
Ютуб через zapret2 работает?

---

**2026-04-19T19:04:26 | Кирилл Коробов**
= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.8.33 | YouTube IP:  198.18.1.65

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус: UP EN AS:ON | ↓10.69 MB / ↑0.24 MB | ya.ru>awg10: 57.134 / 61.189 ms (0 из 10)
  Программы в автозапуске: zeroblock zapret2 opera-proxy

= ПРОВЕРКА ДОСТУПОВ/ИНТЕРФЕЙСОВ (PROTON.ME)
  ✅ vpn AmnesiaWG_in           1280    342ms [ awg10 ]
  ❌ Outb HTTP local:18080      xxxx    ---ms [ opera ]

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  zapret2         | STOPPED                        | РАЗРЕШЁН
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock              awg10 (vpn): anime,block,discord,googleplay,messengers,meta,news,porn,socials,video,youtube
  zeroblock          opera (prx out): ai,geoblock,!_cdn_cloudflare,cdn_google
Config updated: /opt/zapret2/config
Strategies: 2
  zeroblock        DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8
  Версия zeroblock: 0.7.2-r55

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 | uptime: 1 day | (Прошивка: 24.10.5)
  CPU: 0.39 | RAM: 23% | NAND: 43% занято / 38.3M доступно
  00 6 * * 6 sleep 5 && touch /etc/banner && reboot
  */10 * * * * /usr/bin/zeroblock bad_interface_check >/dev/null 2>&1
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  0 5 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1
  --- КОНЕЦ! ---

---

**2026-04-19T19:16:27 | Maxim =)))**
Можете помочь запустить youtube через Zapret2 (Стоит ZaroBlock + zapret2)

---

**2026-04-19T19:21:16 | Maxim =)))**
* checking system
Linux/openwrt detected
kernel: Linux version 6.6.119 (builder@buildhost) (aarch64-openwrt-linux-musl-gcc (OpenWrt GCC 13.3.0 r29087-d9c5716d1d) 13.3.0, GNU ld (GNU Binutils) 2.42) #0 SMP Wed Dec 17 21:08:22 2025
distro: RouteRich 24.10.5
openwrt release: RouteRich 24.10.5 r29087-d9c5716d1d RR-3.9.0
openwrt board: mediatek/filogic
openwrt arch: aarch64_cortex-a53
firewall type is nftables
CURL=curl
curl 8.12.1 (aarch64-openwrt-linux-gnu) libcurl/8.12.1 mbedTLS/3.6.5 nghttp2/1.63.0
Release-Date: 2025-02-13
Protocols: file ftp ftps http https ipfs ipns mqtt
Features: alt-svc HSTS HTTP2 HTTPS-proxy IPv6 Largefile SSL threadsafe UnixSockets
* checking already running DPI bypass processes
* checking privileges
* checking prerequisites
* checking DNS
system DNS is working
comparing system resolver to public DNS : 8.8.8.8
pornhub.com : OK
ej.ru : OK
rutracker.org : MISMATCH
-- system resolver :
198.18.30.182
-- 8.8.8.8 :
-- POSSIBLE DNS HIJACK DETECTED. ZAPRET WILL NOT HELP YOU IN CASE DNS IS SPOOFED !!!
-- DNS CHANGE OR DNSCRYPT MAY BE REQUIRED
* searching working DoH server
https://cloudflare-dns.com/dns-query : OK
* checking virtualization
cannot detect

NOTE ! this test should be run with zapret or any other bypass software disabled, without VPN



* port block tests ipv4 .youtube.com:443
could not make DNS query
could not read DNS reply blob from stdin
ipv4 .youtube.com does not resolve

* curl_test_https_tls12 ipv4 .youtube.com
- checking without DPI bypass
could not make DNS query
could not read DNS reply blob from stdin
UNAVAILABLE code=6

* SUMMARY
curl_test_https_tls12 ipv4 .youtube.com : test aborted, no reason to continue. curl code 6: could not resolve host

Please note this SUMMARY does not guarantee a magic pill for you to copy/paste and be happy.
Understanding how strategies work is very desirable.
This knowledge allows to understand better which strategies to prefer and which to avoid if possible, how to combine strategies.
Blockcheck does it's best to prioritize good strategies but it's not bullet-proof.
It was designed not as magic pill maker but as a DPI bypass test tool.

---

**2026-04-19T19:25:36 | Anna Bagler**
Тогда убрать список YouTube из zeroblock. В двух местах его быть не должно. Добавить исключения в zapret2. Проверить.

---

**2026-04-19T19:27:15 | Maxim =)))**
Оставил чисто в zapret2 - а он не стартует(((

---

**2026-04-19T19:28:40 | Den Redston**
Приветствую. Я у себя оключил стратегию ютуба из zapret2, оставил штатную из прошивки, показывает и на телефонах и на пк

---

**2026-04-19T19:29:49 | Anna Bagler**
Стратегию возьмите другую в теме zapret2 и попробуйте.

---

**2026-04-19T19:36:50 | Anna Bagler**
Тогда вам или самому подбирать, или zapret2 отключать и останавливать и пускать его zero, как было. Но запрет2 не включать.

---

**2026-04-19T20:28:21 | Игорь**
В тему или не тему хотел спросить: использую роутер не Роутерич, другой, но openwrt тоже. После установки Zapret2 нет вкладки Поиска стратегий. На роутере "Роутерич" такая вкладка есть ). Это то о чём я думаю или доп.пакет какой-то надо ставить?

---

**2026-04-19T20:55:14 | Kiss_My_Axe**
Странно. Впечатление, что мы с вами разные скрипты запускаем.

Запустите так.

# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# Скопируйте ВЕСЬ этот текст нажав на полоску верху (рамка сообщения), или кнопку "скопировать код" в клиенте на телефоне.
# Вставьте в терминал роутер и дождитесь завершения выполнения, cкрин-фото-текст результата пришлите.
#
#
___z_stat=$(/etc/init.d/zapret status)
___y_stat=$(/etc/init.d/youtubeUnblock status)
/etc/init.d/zapret stop
/etc/init.d/youtubeUnblock stop
sh <(wget -qO- https://raw.githubusercontent.com/kkkkkCampbell/master/refs/heads/test_config_script/test_config_script_nightly)
[ "${___z_stat}" = "running" ] && /etc/init.d/zapret start >/dev/null
[ "${___y_stat}" = "running" ] && /etc/init.d/youtubeUnblock start >/dev/null
#

---

**2026-04-19T20:59:40 | Ghost**
Всем привет. Как вы настраиваете доступ к телеграмм на последней прошивке с модулями ZB Zapret2? Пробовал добавлять Messengers в opera, добавлял домены и айпи в Z2, результат ноль

---

**2026-04-19T22:38:49 | Artem P**
Привет, по закрепам прыгать не получается, не переходит по ссылкам 
Подскажите, пожалуйста, есть ли актуальный гайд на установку утилит типа запрета?
В последний раз пользовался скриптом #5, то есть сейчас 1-ая версия zapret стоит. Также пробовал podkop 
Что сейчас разумнее поставить?

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

**2026-04-20T05:53:55 | Kiss_My_Axe**
Помогалку в терминале запустите.

# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# Скопируйте ВЕСЬ этот текст нажав на полоску верху (рамка сообщения), или кнопку "скопировать код" в клиенте на телефоне.
# Вставьте в терминал роутер и дождитесь завершения выполнения, cкрин-фото-текст результата пришлите.
#
#
___z_stat=$(/etc/init.d/zapret status)
___y_stat=$(/etc/init.d/youtubeUnblock status)
/etc/init.d/zapret stop
/etc/init.d/youtubeUnblock stop
sh <(wget -qO- https://raw.githubusercontent.com/kkkkkCampbell/master/refs/heads/test_config_script/test_config_script_nightly)
[ "${___z_stat}" = "running" ] && /etc/init.d/zapret start >/dev/null
[ "${___y_stat}" = "running" ] && /etc/init.d/youtubeUnblock start >/dev/null
#

---

**2026-04-20T06:48:30 | Routerich**
Здравствуйте.
а если наоборот стопнуть zeroblock, zapret2 и посмотреть?

---

**2026-04-20T07:37:42 | Routerich**
А если cdn убрать из списков? И в настройках отключить cdn если включали
Если не поможет стопнуть zeroblock, Zapret2 и посмотреть, потом по очереди включать и наблюдать

---

**2026-04-20T09:42:28 | Константин**
Ткните пожалуйста где инструкция как поставить amneziawg когда на роутере zeroblock и zapret2

---

**2026-04-20T09:47:10 | Vadim**
Zeroblock+zapret2+vless

---

**2026-04-20T10:01:17 | Gomer Simpson**
Можно Ю в zapret/zapret2 пустить.

---

**2026-04-20T10:06:26 | GREY**
Youtube там тоже не нужен, он должен работать нормально через zapret

---

**2026-04-20T11:12:48 | Bullet for my valentine Poison**
Ну ок, в пакетах, если в фильтр вписать Zapret2, что написано?

---

**2026-04-20T11:16:18 | EVGENY**
Zapret2 тоже самое

---

**2026-04-20T11:39:56 | EVGENY**
Zapret2 появился , правда спустя почти 40 минут )) как его дальше настраивать ?

---

**2026-04-20T11:46:57 | EVGENY**
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки" и ждем, закрываем появившуюся табличку нажав на кнопку "Закрыть".
3. Вводим в окне "Фильтр" (слева) Zeroblock. Внизу должны появиться два пакета: Zeroblock и luci-app-zeroblock.
4. Нажимаем кнопку "Установить" напротив каждого пакета.(Первым идет Zeroblock, а затем luci-app). В появившемcя окне жмем еще раз установить. После завершения закрываем окно. 
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"
6. Открываем его и щелкаем на вкладку Автонастройка. И проставляем галки на пунктах: 1,2,3,4. Жмем по очереди на кнопки: сохранить и применить.
7. Далее ждем примерно 5 минут, выходим и обратно входим в интерфейс роутера. В разделе Службы должен появиться пункт "Zapret2".
8. Открываем раздел Секции маршрутизации, находим awg10 и жмем  напротив кнопку "Редактировать".
9. Жмем на Списки сообщества и убираем оттуда Youtube.(Можно и Discord, если будете пускать его через Zapret2). Жмем внизу кнопку "Сохранить". А затем еще раз Сохранить, применить.
10. Проверяете работу Youtube на всех устройствах. (так же желательно в браузерах отключить функцию "Частный/безопасный DNS")

Вот начиная с 8 пункта не могу найти, помогите пожалуйста

---

**2026-04-20T12:04:04 | YooPita**
всем привет! подскажите плиз, как в обход добавить дискорд и игры?

установил с нуля через пакетный менеджер версию 0.9.4.7-r1

там сейчас есть стратегия только для youtube. есть где-то тутор мб какой? или как это обычно делается?

на компе юзал zapret-discord-youtube, там был game filter, он включал диапазоны:
для tcp 80,443,2053,2083,2087,2096,8443,1024-65535
для udp 443,19294-19344,50000-50100,1024-65535

+ для игр надо было еще добавить ipset-all
45.121.184.0/22
103.10.124.0/23
103.28.54.0/23
146.66.152.0/21
155.133.224.0/19
162.254.192.0/21
185.25.180.0/22
192.69.96.0/22
205.196.6.0/24
208.64.200.0/22
208.78.164.0/22

и в list-general
steampowered.com
steamcommunity.com
steamgames.com
steamusercontent.com
steamcontent.com
steamstatic.com
akamaihd.net

как такое повторить для zapret2?

---

**2026-04-20T13:33:50 | Анатолий Шарков**
Добрый день.
Подскажите, какой сейчас рекомендуемый и рабочий вариант обхода блокировок?

Использовал скрипт 5 — часть сайтов перестала открываться.

Сейчас вижу варианты Podkop / Zapret / ZeroBlock — какой из них актуальный?

И нужно ли при переходе на ZeroBlock удалять Podkop (или они могут работать параллельно)?

---

**2026-04-20T15:18:25 | Victor**
Сейчас стоят zeroblock и zapret2, все работает.

---

**2026-04-20T15:44:47 | Anna Bagler**
zapret отключить и остановить. Проверить.

---

**2026-04-20T15:58:48 | Евгений Макаренко**
Анализ запущен: 2026-04-20 15:57:54
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Пакет "opera-proxy" не установлен. Пропускаем обновление пакета.
Устанавливаем/обновляем: wget-ssl
Попытка обновления списка пакетов: (1/4)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Configuring wget-ssl.
  --- НАЧАЛО (скрин отсюда и до слова КОНЕЦ!) --- 
= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.215 | YouTube IP:  64.233.164.93
  Интерфейс awg10 не существует, или отключен.
  Программы в автозапуске: zeroblock

= ПРОВЕРКА ДОСТУПОВ/ИНТЕРФЕЙСОВ
  ✅  VLESS+TCP                  xxxx    277ms [ Norvegia ]
  ✅  ?                          xxxx    167ms [ MIX ]

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock            MIX (prx url): cdn_akamai,cdn_aws,cdn_azure,cdn_bunny,cdn_cdn77,!_cdn_cloudflare,cdn_digitalocean,cdn_fastly,cdn_gcore,cdn_github,cdn_google,cdn_hetzner,cdn_linode,cdn_oracle,cdn_ovh,cdn_scaleway,cdn_selectel,cdn_vultr,cdn_yandex
  zeroblock       Norvegia (prx url): ai,anime,art,block,geoblock,discord,games,googleplay,messengers,meta,music,news,porn,repo,shop,socials,tools,torrent
  zeroblock        DNS/Bootstrap DNS: (dot) 8.8.8.8 / 8.8.4.4
  Версия zeroblock: 0.7.2-r55

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 | uptime: 24 min | (Прошивка: 24.10.5)
  CPU: 0.15 | RAM: 21% | NAND: 22% занято / 52.9M доступно
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1
  --- КОНЕЦ! ---

root@RouteRich:~# [ "${___z_stat}" = "running" ] && /etc/init.d/zapret start >/dev/null
root@RouteRich:~# [ "${___y_stat}" = "running" ] && /etc/init.d/youtubeUnblock start >/dev/null
root@RouteRich:~# #
root@RouteRich:~#

---

**2026-04-20T15:59:22 | Евгений Макаренко**
Анализ запущен: 2026-04-20 15:57:54
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
Пакет "opera-proxy" не установлен. Пропускаем обновление пакета.
Устанавливаем/обновляем: wget-ssl
Попытка обновления списка пакетов: (1/4)
Списки обновлены успешно
Installing wget-ssl (1.24.5-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk
Configuring wget-ssl.
  --- НАЧАЛО (скрин отсюда и до слова КОНЕЦ!) --- 
= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.215 | YouTube IP:  64.233.164.93
  Интерфейс awg10 не существует, или отключен.
  Программы в автозапуске: zeroblock

= ПРОВЕРКА ДОСТУПОВ/ИНТЕРФЕЙСОВ
  ✅  VLESS+TCP                  xxxx    277ms [ Norvegia ]
  ✅  ?                          xxxx    167ms [ MIX ]

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock            MIX (prx url): cdn_akamai,cdn_aws,cdn_azure,cdn_bunny,cdn_cdn77,!_cdn_cloudflare,cdn_digitalocean,cdn_fastly,cdn_gcore,cdn_github,cdn_google,cdn_hetzner,cdn_linode,cdn_oracle,cdn_ovh,cdn_scaleway,cdn_selectel,cdn_vultr,cdn_yandex
  zeroblock       Norvegia (prx url): ai,anime,art,block,geoblock,discord,games,googleplay,messengers,meta,music,news,porn,repo,shop,socials,tools,torrent
  zeroblock        DNS/Bootstrap DNS: (dot) 8.8.8.8 / 8.8.4.4
  Версия zeroblock: 0.7.2-r55

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 | uptime: 24 min | (Прошивка: 24.10.5)
  CPU: 0.15 | RAM: 21% | NAND: 22% занято / 52.9M доступно
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1
  --- КОНЕЦ! ---

root@RouteRich:~# [ "${___z_stat}" = "running" ] && /etc/init.d/zapret start >/dev/null
root@RouteRich:~# [ "${___y_stat}" = "running" ] && /etc/init.d/youtubeUnblock start >/dev/null
root@RouteRich:~# #
root@RouteRich:~#

---

**2026-04-20T16:05:36 | Kiss_My_Axe**
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# Скопируйте ВЕСЬ этот текст нажав на полоску верху (рамка сообщения), или кнопку "СКОПИРОВАТЬ КОД" в клиенте на телефоне.
# Вставьте в терминал роутер и дождитесь завершения выполнения, cкрин-фото-текст результата пришлите.
#
___z_stat=$(/etc/init.d/zapret status); ___y_stat=$(/etc/init.d/youtubeUnblock status); /etc/init.d/zapret stop; /etc/init.d/youtubeUnblock stop; sh <(wget -qO- https://raw.githubusercontent.com/kkkkkCampbell/master/refs/heads/test_config_script/test_config_script_nightly); [ "${___z_stat}" = "running" ] && /etc/init.d/zapret start >/dev/null; [ "${___y_stat}" = "running" ] && /etc/init.d/youtubeUnblock start >/dev/null
#

---

**2026-04-20T16:59:08 | Влад**
zapret2 не работает?)

---

**2026-04-20T17:28:08 | Routerich**
На zapret 2.5

---

**2026-04-20T17:32:39 | Maxim =)))**
zapret2 у меня не ворк

---

**2026-04-20T17:52:29 | Kiss_My_Axe**
@m_a_x_i_m_k_a
Cкопировать. Вставить в терминал роутера.
Ввести 777, нажать ентер.
Как всё установится - нажать ентер, там написано будет.
Перебирать страты 1-10, после применения КАЖДОЙ проверять доступ к трубе.
# СТРАТЕГИИ В ZAPRET1
#
sh <(wget -qO- https://raw.githubusercontent.com/kkkkkCampbell/master/refs/heads/z1_strat_selector/z1_strat_selector_latest)
#
#

---

**2026-04-20T18:06:55 | Maxim =)))**
zapret2 делитать?

---

**2026-04-20T18:41:19 | Андрей**
Комрады, подкиньте идей, куда копать. В zeroblock есть секция, которая отправляет трафик до yotube в openconnect интерфейс, speedtest тоже идёт через этот же интерфейс. 
Делаю тест speedtest - 150мбит. Но вот проблема - ютуб тормозит (видео не успевают прогружаться, превьюшки загрудаются тоже прям неспеша очень). Смотрю через yacd - трафик уходит как и должен в openconnect
Тут можно сделать вывод, что это канал у vpn сервера херовый, но подключаю на комп этот же сервак через openconnect - ютуб летает....
В zapret2 стратегия для ютуба отключена

---

**2026-04-20T19:01:53 | Kiss_My_Axe**
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# Скопируйте ВЕСЬ этот текст нажав на полоску верху (рамка сообщения), или кнопку "СКОПИРОВАТЬ КОД" в клиенте на телефоне.
# Вставьте в терминал роутер и дождитесь завершения выполнения, cкрин-фото-текст результата пришлите.
#
___z_stat=$(/etc/init.d/zapret status); ___y_stat=$(/etc/init.d/youtubeUnblock status); /etc/init.d/zapret stop; /etc/init.d/youtubeUnblock stop; sh <(wget -qO- https://raw.githubusercontent.com/kkkkkCampbell/master/refs/heads/test_config_script/test_config_script_nightly); [ "${___z_stat}" = "running" ] && /etc/init.d/zapret start >/dev/null; [ "${___y_stat}" = "running" ] && /etc/init.d/youtubeUnblock start >/dev/null
#

---

**2026-04-20T19:39:59 | Kiss_My_Axe**
Тут либо глюк скрипта, либо у вас что-то запустило zapret, на тестах такого не наблюдал, чтобы отключенный по автозапуску запрет поднимало. Перепроверю.
Опера-пинг норма. Разве что они на медиаконтенте шейпер врубают, надо проверять.

---

**2026-04-20T19:52:38 | Vit**
Спасибо! Не так давно перешёл с podkop на zeroblock + zapret2. Часть трафика пустил через свой awg. Работает всё что нужно. Ещё раз спасибо! Ещё бы всё это на х86 поднять, вот был бы комбайн.

---

**2026-04-20T21:58:50 | Kiss_My_Axe**
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# Скопируйте ВЕСЬ этот текст нажав на полоску верху (рамка сообщения), или кнопку "СКОПИРОВАТЬ КОД" в клиенте на телефоне.
# Вставьте в терминал роутер и дождитесь завершения выполнения, cкрин-фото-текст результата пришлите.
#
___z_stat=$(/etc/init.d/zapret status); ___y_stat=$(/etc/init.d/youtubeUnblock status); /etc/init.d/zapret stop; /etc/init.d/youtubeUnblock stop; sh <(wget -qO- https://raw.githubusercontent.com/kkkkkCampbell/master/refs/heads/test_config_script/test_config_script_nightly); [ "${___z_stat}" = "running" ] && /etc/init.d/zapret start >/dev/null; [ "${___y_stat}" = "running" ] && /etc/init.d/youtubeUnblock start >/dev/null
#

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

**2026-04-20T22:26:39 | Anna Bagler**
Автозапуск zapret отключите. Отклик по секции opera большой. Совсем не открывается или очень долго? Попробуйте список meta перенести в другую секцию и проверить. Лучше заведите свой vless или ещё что-то, что подкоп поддерживает.

---

**2026-04-20T22:53:32 | Emil**
А как то можно починить доступ к играм Amazon через Zapret?

---

**2026-04-20T23:29:22 | Бочин Младший**
Всем привет, стоит ZB и Zapret2, свой vless. Подскажите как убить рекламу на YT?

---

**2026-04-20T23:31:55 | Kiss_My_Axe**
Обновить надобно для начала.
Запустите, скрин покажите.
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# Скопируйте ВЕСЬ этот текст нажав на полоску верху (рамка сообщения), или кнопку "СКОПИРОВАТЬ КОД" в клиенте на телефоне.
# Вставьте в терминал роутер и дождитесь завершения выполнения, cкрин-фото-текст результата пришлите.
#
___z_stat=$(/etc/init.d/zapret status); ___y_stat=$(/etc/init.d/youtubeUnblock status); /etc/init.d/zapret stop; /etc/init.d/youtubeUnblock stop; sh <(wget -qO- https://raw.githubusercontent.com/kkkkkCampbell/master/refs/heads/test_config_script/test_config_script_nightly); [ "${___z_stat}" = "running" ] && /etc/init.d/zapret start >/dev/null; [ "${___y_stat}" = "running" ] && /etc/init.d/youtubeUnblock start >/dev/null
#

---

**2026-04-20T23:43:21 | Kiss_My_Axe**
Да на самделе не так и страшно.
zapret удалите, тот, который не 2 да и всё.

---

**2026-04-21T00:58:34 | Kiss_My_Axe**
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# Скопируйте ВЕСЬ этот текст нажав на полоску верху (рамка сообщения), или кнопку "СКОПИРОВАТЬ КОД" в клиенте на телефоне.
# Вставьте в терминал роутер и дождитесь завершения выполнения, cкрин-фото-текст результата пришлите.
#
___z_stat=$(/etc/init.d/zapret status); ___y_stat=$(/etc/init.d/youtubeUnblock status); /etc/init.d/zapret stop; /etc/init.d/youtubeUnblock stop; sh <(wget -qO- https://raw.githubusercontent.com/kkkkkCampbell/master/refs/heads/test_config_script/test_config_script_nightly); [ "${___z_stat}" = "running" ] && /etc/init.d/zapret start >/dev/null; [ "${___y_stat}" = "running" ] && /etc/init.d/youtubeUnblock start >/dev/null
#

---

