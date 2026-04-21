# Raw Extraction: tpws

**2026-01-06T22:29:55 | Dmitrii Burenin**
С приложением YouTube на WebOS еще куда запутаннее: там загрузка интерфейса идет по протоколу HTTPS (TCP порт 443), а видео протоколу QUIC (UDP порт 443). Но в случае, если подключение по QUIC не доступно, тогда приложения, что на Android устройствах, что WebOS переходят на протокол HTTPS. Так чтобы на телевизоре и телефоне YouTube не тормозил при работе с TPWS, необходимо блокировать трафик UDP на порт 443, для того, чтобы заставить приложения подключатся по протоколу HTTPS. Но это не решит проблему с поломкой загрузки интерфейса приложения на WebOS (Android TV) при работе с TPWS.
(c)

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

**2026-02-01T12:23:46 | Nook Scheel**
root@RouteRich:~# ps | grep -E 'nfq|tpws|dvtws'
 1896 root      1340 S    grep -E nfq|tpws|dvtws
 4190 daemon    1940 S    /opt/zapret/nfq/nfqws --user=daemon --dpi-desync-fwmark=0x40000000 --qnum=200 --filter-tcp=443 --dpi-desync=fake fakeddisorder --dpi-desync-split-pos=10,midsld --dpi-desync-fake-tls=/
 4191 daemon    1712 S    /opt/zapret/nfq/nfqws --user=daemon --dpi-desync-fwmark=0x40000000 --qnum=65400 --dpi-desync=fake --dpi-desync-repeats=2


Запрет работает

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

