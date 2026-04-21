# Raw Extraction: ttl

**2026-01-01T22:56:38 | Roman**
Выяснилось вот что. Фиксация ttl. Ставишь 64 в модеме, работает только от ПК, через роутер не хочет,(там настройку ттл не трогал никогда даже до проблемы этой) хотя раньше все ок работало. В роутере выставили ттл так же на 64. Все заработало. Ничего не понимаю, очередные гайки оператор мобильный закручивает что-ли.... Может у вас есть ответ на этот вопрос)

---

**2026-01-03T15:07:51 | Саша Восход**
root@RouteRich:~#  nslookup ya.ru 8.8.8.8
Server:         8.8.8.8
Address:        8.8.8.8:53

Non-authoritative answer:
Name:   ya.ru
Address: 5.255.255.242
Name:   ya.ru
Address: 77.88.44.242
Name:   ya.ru
Address: 77.88.55.242

Non-authoritative answer:
Name:   ya.ru
Address: 2a02:6b8::2:242

root@RouteRich:~# ping 2409::
PING 2409:: (2409::): 56 data bytes
64 bytes from 2409::: seq=0 ttl=46 time=327.972 ms
64 bytes from 2409::: seq=1 ttl=46 time=328.709 ms
64 bytes from 2409::: seq=2 ttl=46 time=328.631 ms
64 bytes from 2409::: seq=3 ttl=46 time=328.072 ms
^C
--- 2409:: ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 327.972/328.346/328.709 ms
root@RouteRich:~#

---

**2026-01-03T16:54:10 | А К**
На модеме у вас зафиксирован только исходящий TTL, для МТС нужно фиксировать в обе стороны

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

**2026-01-10T00:33:06 | Борис**
Всё, что написано выше в этой теме — чистая правда, роутер потрясающий. Моя история такова:

Я никого не трогал, играл себе в игрулечки на Playstation 5... Терпел белые списки, неработающие сайты. Как однажды мою любимую сетевую игру заблокировали - невозможно было подключиться к серверам... Я не про Roblox, а про Battlefield 6, но сути это не меняет. По слухам, некая программа Zapret помогала обходить любые ограничения. Но ведь эта программа под Windows и Linux, а я играю на Playstation, и как же быть? Купить роутер на OpenWRT!

Дальше всё как в тумане. Помню, что мой роутер нельзя было прошить на OpenWRT, потому что было мало оперативы. Ozon, строка поиска... Статус заказа - готов к выдаче... Открываю коробку... Несколько минут спустя ютуб открывается, Zapret скачан, спустя ещё пол-часа Battlefield 6 уже работает во всю, прочитал про белые списки, узнал про Vless, узнал, что Wireguard и OpenVPN блокируются по сигнатурам, узнал про Vless, но мне этого было мало, и вот я уже позабыл про депрессию от блокировок и очнулся, когда установил nginx, ddns-клиент, поставил себе xray сервер, через бекдор получил бесплатный белый IP у провайдера и готовлюсь делать маскировку через vless Reality под сайт провайдера, ведь сайты провайдера доступны в режиме белых списков, а у меня IP из подсети провайдера... Стоп.

Чем я там занимался? А, ну да. Я играл в игры и что-то они забарахлили. Ну так вот, роутер прекрасный, для обучения тоже подходит отлично, да и как игрушка тоже замечательный — который день не могу оторваться от исследований... Кстати, я вообще собирался написать отзыв про обновленную чёрную тему в Routerich Luci - в ней проблема с кнопками, они одного цвета, и в этом плане они проигрывают белой теме :)

---

**2026-01-11T19:22:38 | Serj Shu**
А Вот так 🤔
nfqws \
--out-range -s34228 \
--tls \
--dpi-desync=fake,split \
--dpi-desync-fake-tls=fake_default_tls \
--dpi-desync-split-pos=1 \
--dpi-desync-repeats=2 \
--dpi-desync-autottl=2

---

**2026-01-11T19:30:53 | Amir**
ping -c 5 -I awg10 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=119 time=92.770 ms

64 bytes from 8.8.8.8: seq=1 ttl=119 time=68.381 ms
64 bytes from 8.8.8.8: seq=2 ttl=119 time=68.896 ms
64 bytes from 8.8.8.8: seq=3 ttl=119 time=66.913 ms
64 bytes from 8.8.8.8: seq=4 ttl=119 time=67.245 ms

--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 66.913/72.841/92.770 ms
К сожалению, не могу отвечать оперативно из-за ограничений в чате

---

**2026-01-16T10:08:55 | Andrey Lazarev**
Глубокоуважаемая поддержка и члены сообщества, подскажите пожалуйста ответы на несколько вопросов:

1) Если есть желание опробовать zapret2, то нужно ли удалять с роутера пакеты, относящиеся к zapret, podkop и youtube_unblock.

2) В очередной раз "что-то пошло не так" и доступ к "ТыТрубе" пропал сегодня. Если хочется переустановить нужные пакеты (скрипт №5) - нужно ли предварительно удалять пакеты, как и в первом вопросе, zapret-podkop-uy_unblock?

3) Каков минимальный необходимый набор пакетов для деблокирования доступа к YT и популярным игровым сервисам? Достаточно ли будет поставить zapret2 если у меня народ не только YT и связанные с Мета сервисы использует, но и в игры играет (Battlefield, Elite Dangerous - последняя, как я понимаю, частично на облако Амазона опирается, но могу ошибаться)?

---

**2026-01-16T10:24:37 | Юрий Теленков**
packet: id=217 len=132 mark=20000000 ifin=br-lan(11) ifout=wan(6)
IP4: 1.1.1.1 => 149.154.167.99 proto=tcp ttl=127 sport=7294 dport=443 flags=AP seq=3563100834 ack_seq=3678498979
TCP: len=92 : 17 03 03 00 57 E4 0C A1 EB CA 73 4C D1 F0 E4 A8 84 0E 14 F9 DD 8D 50 5A 09 86 D8 A5 BD 64 C7 B4 ... : ....W.....sL..........PZ.....d.. ...
client mode desync profile/ipcache search target ip=149.154.167.99 port=443
using cached desync profile 0 (no_action)
dpi desync src=1.1.1.1:7294 dst=149.154.167.99:443 track_direction=out fixed_direction=out connection_proto=tls payload_type=unknown
no lua functions in this profile
packet: id=217 pass unmodified

packet: id=218 len=428 mark=20000000 ifin=br-lan(11) ifout=wan(6)
IP4: 1.1.1.1 => 149.154.167.99 proto=tcp ttl=127 sport=7294 dport=443 flags=AP seq=3563100926 ack_seq=3678498979
TCP: len=388 : 17 03 03 01 7F 01 9B 81 D9 15 9F 2F 8E EC D9 46 51 82 E4 D1 33 4A 78 6B 8A 5D 4D 79 17 89 EB D2 ... : ........./...FQ...3Jxk.]My.... ...
client mode desync profile/ipcache search target ip=149.154.167.99 port=443
using cached desync profile 0 (no_action)
dpi desync src=1.1.1.1:7294 dst=149.154.167.99:443 track_direction=out fixed_direction=out connection_proto=tls payload_type=unknown
no lua functions in this profile
packet: id=218 pass unmodified

packet: id=219 len=40 mark=20000000 ifin=br-lan(11) ifout=wan(6)
IP4: 1.1.1.1 => 149.154.167.99 proto=tcp ttl=127 sport=7294 dport=443 flags=A seq=3563101314 ack_seq=3678499553
client mode desync profile/ipcache search target ip=149.154.167.99 port=443
using cached desync profile 0 (no_action)
dpi desync src=1.1.1.1:7294 dst=149.154.167.99:443 track_direction=out fixed_direction=out connection_proto=tls payload_type=empty
no lua functions in this profile
packet: id=219 pass unmodified

packet: id=220 len=71 mark=20000000 ifin=br-lan(11) ifout=wan(6)
IP4: 1.1.1.1 => 149.154.167.99 proto=tcp ttl=127 sport=7294 dport=443 flags=AP seq=3563101314 ack_seq=3678499801
TCP: len=31 : 17 03 03 00 1A E0 AD 79 C4 4A 2F 32 1C 7B 84 04 53 FA 80 5F 80 9D 40 31 D6 3C 50 C7 5C 4A 16 : .......y.J/2.{..S.._..@1.<P.\J.
client mode desync profile/ipcache search target ip=149.154.167.99 port=443
using cached desync profile 0 (no_action)
dpi desync src=1.1.1.1:7294 dst=149.154.167.99:443 track_direction=out fixed_direction=out connection_proto=tls payload_type=unknown
no lua functions in this profile
packet: id=220 pass unmodified
root@RouteRich:~#

---

**2026-01-16T17:20:40 | Александр 🔴🔵**
что то там TTLfix?

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

**2026-01-22T16:55:26 | ☭ ktrace**
на втором прекрасно работает
# ping -6 -I pppoe-wanb 2a00:ab00:2000:1::53
PING 2a00:ab00:2000:1::53 (2a00:ab00:2000:1::53): 56 data bytes
64 bytes from 2a00:ab00:2000:1::53: seq=0 ttl=251 time=31.390 ms

---

**2026-01-22T18:23:34 | ☭ ktrace**
интересно, на одном провайдере не работает ipv6. 
# ping -6 -I pppoe-wan 2a00:ab00:2000:1::53
PING 2a00:ab00:2000:1::53 (2a00:ab00:2000:1::53): 56 data bytes
ping: sendto: Network unreachable
на втором прекрасно работает
# ping -6 -I pppoe-wanb 2a00:ab00:2000:1::53
PING 2a00:ab00:2000:1::53 (2a00:ab00:2000:1::53): 56 data bytes
64 bytes from 2a00:ab00:2000:1::53: seq=0 ttl=251 time=31.390 ms
дефолт маршруты есть и там и там. дефолтшлюзы и там и там пингуются

---

**2026-01-23T23:27:30 | пам пам**
TTL 64 или 65 в настройках роутера ставить? Каким способом лучше? luci-app-ttl или что-то другое?

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

**2026-01-27T20:46:34 | Юрий**
 -----------------------------------------------------
 RouteRich 24.10.4, r28959-29397011cc
 -----------------------------------------------------
root@RouteRich:~# ping -I awg10 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=118 time=58.030 ms
64 bytes from 8.8.8.8: seq=1 ttl=118 time=53.800 ms
64 bytes from 8.8.8.8: seq=2 ttl=118 time=54.325 ms
64 bytes from 8.8.8.8: seq=3 ttl=118 time=56.917 ms
64 bytes from 8.8.8.8: seq=4 ttl=118 time=53.926 ms
64 bytes from 8.8.8.8: seq=5 ttl=118 time=57.309 ms
64 bytes from 8.8.8.8: seq=6 ttl=118 time=54.170 ms
64 bytes from 8.8.8.8: seq=7 ttl=118 time=54.452 ms
64 bytes from 8.8.8.8: seq=8 ttl=118 time=53.946 ms
^C
--- 8.8.8.8 ping statistics ---
9 packets transmitted, 9 packets received, 0% packet loss
round-trip min/avg/max = 53.800/55.208/58.030 ms
root@RouteRich:~#

---

**2026-01-28T13:29:24 | Weyland**
Добрый день. Пожалуйста, добавьте в DNS failsafe proxy возможность изменять значение поля TTL ответа. В момент восстановления работы подкопа хочется, чтобы FakeIP заработал быстрее без необходимости чистить днс кэш у всех клиентов вручную. В идеале иметь в настройках DHS failsafe proxy отдельное поле со устанавливаемым значением и возможность включать/выключать правку TTL.

---

**2026-01-28T23:32:15 | mitr**
Поставил версию 24.0.1. Накатил скрипт №5. 

Работает ChatGPT, Gemini. Добавил Google Meet адреса. На макбуке в браузере открывается Youtube, но на телевизоре и айфоне нет. Скидываю скриншоты и настройки. 

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
        option outbound_json '{
  "type": "http",
  "tag": "http-proxy",
  "server": "127.0.0.1",
  "server_port": 18080
}'
        list community_lists 'geoblock'
        list community_lists 'block'
        list community_lists 'meta'
        list community_lists 'twitter'
        list community_lists 'hdrezka'
        list community_lists 'tiktok'
        list community_lists 'google_ai'
        option user_domains_text 'myip.com
stun.l.google.com
stun.cloudflare.com
stun.nextcloud.com'

config section 'Discord'
        option connection_type 'vpn'
        option interface 'awg10'
        option domain_resolver_enabled '0'
        option user_domain_list_type 'text'
        option user_subnet_list_type 'disabled'
        option mixed_proxy_enabled '0'
        list community_lists 'discord'
        option user_domains_text '2ip.ru amazonaws.com whatsapp.com whatsapp.net whatsapp.biz wa.me'
        list remote_subnet_lists 'https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_cidr_ipv4.txt'

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

**2026-01-30T23:28:39 | Routerich**
    --filter-udp=443 --hostlist=list-general.txt --hostlist-exclude=list-exclude.txt \
    --ipset-exclude=ipset-exclude.txt \
    --payload=quic_initial \
    --lua-desync=fake:blob=blob_quic_initial_www_google_com:optional:repeats=6 \
    --new \
    --filter-udp=19294-19344,50000-50100 --filter-l7=discord,stun \
    --payload=discord_ip_discovery \
    --lua-desync=fake:blob=0x00000000000000000000000000000000:repeats=6 \
    --payload=stun \
    --lua-desync=fake:blob=0x00000000000000000000000000000000:repeats=6 \
    --new \
    --filter-tcp=2053,2083,2087,2096,8443 \
    --hostlist-domains=discord.media \
    --payload=tls_client_hello \
    --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_ts=-600000:repeats=6:tls_mod=none \
    --new \
    --filter-tcp=443 --hostlist=list-google.txt \
    --payload=tls_client_hello \
    --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_ts=-600000:repeats=6 \
    --new \
    --filter-tcp=80,443 --hostlist=list-general.txt --hostlist-exclude=list-exclude.txt
    --ipset-exclude=ipset-exclude.txt \
    --payload=tls_client_hello \
    --lua-desync=fake:blob=blob_tls_clienthello_4pda_to:optional:tcp_ts=-600000:repeats=6:tls_mod=none \
    --new \
    --filter-udp=443 --hostlist-exclude=list-exclude.txt \
    --ipset=ipset-all.txt \
    --ipset-exclude=ipset-exclude.txt \
    --payload=quic_initial \
    --lua-desync=fake:blob=blob_quic_initial_www_google_com:optional:repeats=6 \
    --new \
    --filter-tcp=80,443 --hostlist-exclude=list-exclude.txt \
    --ipset=ipset-all.txt \
    --ipset-exclude=ipset-exclude.txt \
    --payload=tls_client_hello \
    --lua-desync=fake:blob=fake_default_tls:tcp_ts=-600000:repeats=6:tls_mod=rnd,sni=www.google.com \
    --lua-desync=fake:blob=blob_tls_clienthello_4pda_to:optional:tcp_ts=-600000:repeats=6:tls_mod=none \
    --new \
    --filter-udp (any-protocol) \
    --ipset=ipset-all.txt \
    --ipset-exclude=ipset-exclude.txt \
    --out-range=-n2 \
    --payload=all \
    --lua-desync=fake:blob=blob_quic_initial_www_google_com:optional:ip_autottl=2,3-20:ip6_autottl=2,3-20:repeats=12

---

**2026-01-31T15:51:46 | Bullet for my valentine Poison**
Я кстати хотел один момент спросить, насчет интерпретации стратегий из Блокчека.
--payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:ip_autottl=-6,3-20:tls_mod=rnd,dupsid,padencap:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1
это он склеил две в одну?

---

**2026-02-01T14:24:36 | John Deere**
С этим конфигом battlefield 6 завелся

---

**2026-02-07T21:05:36 | Routerich**
Роман, 3372h модем старый и прошивок на него сделали сотни за это время. Я так и не понял из вашего описания в чем у вас проблема, но видимо как раз в прошивке. TTL на роутере сам по себе не может перезагружать роутер, не может зависать роутер и.т.д. TTL буквально добавляет инструкцию в nft чтобы у всех пакетов проходящих через такой-то интерфейс изменялся ttl на заданный. В вашем же случае модем это не конечный интерфейс, а rndis. По сути отдельное устройство со своими интерфейсами, своим iptables (вместо nft). То есть, если у вас нормальная прошивка на модеме, вам достаточно выставить нужный вам TTL на самом модеме (в его веб интерфейсе). А TTL на роутере не включать вообще.
Наглядно: вам от оператора приходит пакет, допустим с ttl 1. Далее модем передает пакет следующему устройству, в вашем случае следующий это ваш роутер, что пакет с ttl 0. Роутер не может никуда передать пакет дальше, потому что ttl закончился. Но, если в настройках самого модема у вас указано править TTL (и он при этом действительно правится, а не делает вид), тогда модем получит пакет с ttl 1, исправит на 64 и передаст дальше, в роутер. И у роутера пакет окажется с ttl 63, а не 0, и его можно передавать дальше. Понимаете? При такой схеме роутеру уже не нужно опять править TTL (включать правку TTL в настройках Routerich), его до этого уже поправил модем.
Правка TTL в Routerich существует в основном для модемов у которых нет веб интерфейса и ttl невозможно задать. Например у вас t77w968 - ставьте ttl 64. Другой пример - у вас e3372h-153, но на прошивке без настройки TTL - ставите 65.
В чем разница: в вашем случае 3372h это hilink (rndis). ip адрес от оператора получает сам модем и далее отдает роутеру. Получается схема оператор - модем - роутер. В случае например с t77w968 будет такая схема: оператор - роутер (потому что модем в данном случае лишь железо, а не самостоятельное устройство).
Продолжим разбирать ваш случай. Скорее всего вы выставляете TTL и на модеме и на роутере, что как надеюсь вы уже поняли излишне. Достаточно выставить где-то в одном месте, и в вашем случае я рекомендую вас выставлять только на модеме.
Ну и если предложенный мною вариант у вас не работает, то проблема может быть только в прошивке модема. Могу предложить вам абсолютно точно проверенную прошивку, где абсолютно точно все работает и нет никаких проблем ни с каким функционалом вашего модема. Там не нужно будет устанавливать какие либо дополнительные скрипты с 4pda, там сразу все есть в прошивке.

---

**2026-02-07T21:09:14 | Routerich**
Прошивка для e3372h-153
(прошивать hilink)

В интерфейсе установленной прошивки можно включить меню модификаций, там есть как раз fix ttl 1

https://disk.yandex.ru/d/pLuDPl-S6jk2jA

---

**2026-02-09T11:40:19 | Routerich**
«Soon™»
— Никита Буянов, CEO Battlestate Games

---

**2026-02-15T21:48:51 | Вячеслав**
с терминала роутера:
root@RouteRich:~# ping www.gstatic.com
PING www.gstatic.com (2a00:1450:4010:c0f::5e): 56 data bytes
64 bytes from 2a00:1450:4010:c0f::5e: seq=0 ttl=107 time=18.187 ms
64 bytes from 2a00:1450:4010:c0f::5e: seq=1 ttl=107 time=19.853 ms
64 bytes from 2a00:1450:4010:c0f::5e: seq=2 ttl=107 time=20.093 ms
64 bytes from 2a00:1450:4010:c0f::5e: seq=3 ttl=107 time=20.224 ms
64 bytes from 2a00:1450:4010:c0f::5e: seq=4 ttl=107 time=19.904 ms
64 bytes from 2a00:1450:4010:c0f::5e: seq=5 ttl=107 time=17.578 ms
64 bytes from 2a00:1450:4010:c0f::5e: seq=6 ttl=107 time=19.755 ms

С компа:
Обмен пакетами с www.gstatic.com [216.58.209.195] с 32 байтами данных:
Ответ от 216.58.209.195: число байт=32 время=21мс TTL=113
Ответ от 216.58.209.195: число байт=32 время=21мс TTL=113
Ответ от 216.58.209.195: число байт=32 время=22мс TTL=113
Ответ от 216.58.209.195: число байт=32 время=22мс TTL=113

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

**2026-02-16T11:46:03 | Routerich**

REPLAYING delayed packet #2 offset 1372
REPLAY IP4: 176.214.167.99 => 178.18.232.139 proto=tcp ttl=127 sport=55891 dport=443 flags=AP seq=2186540364 ack_seq=478824273
TCP: len=803 : BC 09 8A 41 47 09 29 19 AF F9 FD 4C D3 B0 7D 2D F1 B7 18 07 4E 03 B1 D5 0E 6C AE 1F BC D8 9F 20 ... : ...AG.)....L..}-....N....l.....  ...
client mode desync profile/ipcache search target ip=178.18.232.139 port=443
using cached desync profile 3 (fake_disorder_work)
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
dpi desync src=176.214.167.99:55891 dst=178.18.232.139:443 track_direction=out fixed_direction=out connection_proto=tls payload_type=tls_client_hello
* lua 'fake_3_1' : out pos a0 a0 in range a0-a0
* lua 'fake_3_1' : payload_type 'tls_client_hello' satisfy filter
* lua 'fake_3_1' : desync
instance cutoff for 'fake_3_1' in=1 out=0
LUA: fake: not acting on further replay pieces
* lua 'multidisorder_3_2' : out pos a0 a0 in range a0-a0
* lua 'multidisorder_3_2' : payload_type 'tls_client_hello' satisfy filter
* lua 'multidisorder_3_2' : desync
instance cutoff for 'multidisorder_3_2' in=1 out=0
LUA: multidisorder: not acting on further replay pieces
LUA: dropping replay packet because reasm was already sent
DROPPING delayed packet #2
reassemble session finished
packet: id=59 drop

---

**2026-02-18T14:08:42 | Максим Бычков**
Добрый день, сегодня возникла проблема. При подключении к серверам Battlefield 6 или Rainbow Six Siege выдает ошибку подключения, якобы из-за того что нет интернета. Хотя дс с ютубом летают.

---

**2026-02-18T19:16:03 | Дмитрий Витальевич**
Интернет через свисток e8372-153 шитый со своим ttl, единственное из впн это tailscale

---

**2026-02-18T20:13:52 | Bullet for my valentine Poison**
--payload=tls_client_hello
--lua-desync=fake:blob=blob_tls_clienthello_google:badseq:badseq_incr=1000000:repeats=6

--payload=quic_initial
--lua-desync=fake:blob=blob_quic_initial_google:anyproto:autottl=2:repeats=9:cutoff=n2
думаешь это верно?

---

**2026-02-19T14:32:58 | Lelik**
Нейронка вот такое выдает
--blob=quic_google:@/data/adb/modules/ZDT-D/strategic/bin/quic_initial_www_google_com.bin \
--blob=zero4:0x00000000 \
\
--filter-udp=443,3478,50000-50100 \
--hostlist=/data/adb/modules/ZDT-D/strategic/list/discord.txt \
--payload=quic_initial,known,unknown \
--out-range=-d10 \
--lua-desync=circular:fails=2:maxtime=60 \
--lua-desync=fake:blob=quic_google:repeats=6:ip_autottl=0,3-20 \
--lua-desync=fake:blob=zero4:repeats=8:payload=all \
--lua-desync=udplen:increment=2:min=50:pattern=zero4 \
--new

---

**2026-02-21T14:22:59 | Lelik**
Как будто вот с этим вылетает
packet: id=2068 len=569 mark=20000000 ifin=br-lan(8) ifout=wan(6)
IP4: 176.192.206.182 => 109.122.198.235 proto=tcp ttl=63 sport=28256 dport=443 flags=AP seq=825750052 ack_seq=949037982
TCP: len=517 : 16 03 01 02 00 01 00 01 FC 03 03 71 CE 08 FF 7D BC C7 14 EB F9 2C D9 CF D2 D9 91 8F 18 E1 47 3C ... : ...........q...}.....,........G< ...
client mode desync profile/ipcache search target ip=109.122.198.235 port=443
using cached desync profile 0 (no_action)
packet contains tls_client_hello payload
TLS client hello is FULL
TLS record layer version : TLS 1.0
TLS handshake version : TLS 1.2
TLS supported versions ext : GREASE
TLS supported versions ext : TLS 1.3
TLS supported versions ext : TLS 1.2
TLS ALPN ext : h2
TLS ALPN ext : http/1.1
TLS ECH ext : not present
hostname: www.googletagmanager.com
dpi desync src=176.192.206.182:28256 dst=109.122.198.235:443 track_direction=out fixed_direction=out connection_proto=tls payload_type=tls_client_hello
no lua functions in this profile
packet: id=2068 pass unmodified
quit requested
unbinding from queue 300
closing nfq library handle
LUA SHUTDOWN

---

**2026-02-22T16:11:51 | Роман**
blizzard.com
googlesyndication.com
blz-contentstack.com
akamaized.net
optimizely.com
cloudfront.net
googleapis.com
gstatic.com
battle.net
Закинуть в список пользовательских доменов.

---

**2026-02-25T12:46:10 | K**
Проблема 1: при использовании V2 без CIDR не работал Battlefield 6.

Проблема 2: при использовании V2 с CIDR заработал Battlefield 6, но Youtube ушел в страну VPS.

Как решил: добавил в список исключенных доменов youtube.com.

Все так сделал или все по новой?)

---

**2026-02-25T12:56:34 | K**
Дискорд перестал работать через запрет2, сегодня попробую новую страту найти. 

Вопрос что делать с Battlefield 6, если убираю CIDR - начинаются вылеты.

---

**2026-02-25T15:29:17 | Azizkhan**
Помогите)
Созданы vlan'ы на lan1 порту, они идут в циско, но даже с вай-фай роутера наблюдается такая картина:
PS C:\Users\Lenovo> ping google.com

Обмен пакетами с google.com [142.251.209.14] с 32 байтами данных:
Ответ от 142.251.209.14: число байт=32 время=119мс TTL=115
Ответ от 142.251.209.14: число байт=32 время=112мс TTL=115
Ответ от 142.251.209.14: число байт=32 время=112мс TTL=115
Ответ от 142.251.209.14: число байт=32 время=99мс TTL=115

Статистика Ping для 142.251.209.14:
    Пакетов: отправлено = 4, получено = 4, потеряно = 0
    (0% потерь)
Приблизительное время приема-передачи в мс:
    Минимальное = 99мсек, Максимальное = 119 мсек, Среднее = 110 мсек
PS C:\Users\Lenovo> nslookup google.com
DNS request timed out.
    timeout was 2 seconds.
╤хЁтхЁ:  UnKnown
Address:  192.168.88.1

DNS request timed out.
    timeout was 2 seconds.
DNS request timed out.
    timeout was 2 seconds.
DNS request timed out.
    timeout was 2 seconds.
DNS request timed out.
    timeout was 2 seconds.
*** Превышено время ожидания запроса UnKnown

---

**2026-02-25T15:30:13 | Azizkhan**
На самом роутере картина выглядит так:
root@RouteRich-iLink:~# ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=108 time=49.403 ms
64 bytes from 8.8.8.8: seq=1 ttl=108 time=49.155 ms
^C
--- 8.8.8.8 ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 49.155/49.279/49.403 ms
root@RouteRich-iLink:~# ping google.com
PING google.com (209.85.233.100): 56 data bytes
64 bytes from 209.85.233.100: seq=0 ttl=110 time=57.261 ms
64 bytes from 209.85.233.100: seq=1 ttl=110 time=57.317 ms
^C
--- google.com ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 57.261/57.289/57.317 ms
root@RouteRich-iLink:~# nslookup google.com
Server:         109.194.32.1
Address:        109.194.32.1:53

Non-authoritative answer:
Name:   google.com
Address: 209.85.233.138
Name:   google.com
Address: 209.85.233.100
Name:   google.com
Address: 209.85.233.101
Name:   google.com
Address: 209.85.233.139
Name:   google.com
Address: 209.85.233.113
Name:   google.com
Address: 209.85.233.102

Non-authoritative answer:
Name:   google.com
Address: 2a00:1450:4010:c03::66
Name:   google.com
Address: 2a00:1450:4010:c03::8a
Name:   google.com
Address: 2a00:1450:4010:c03::65
Name:   google.com
Address: 2a00:1450:4010:c03::8b

---

**2026-02-25T16:37:36 | Валерий**
packet: id=81 len=60 mark=00000000 ifin=br-lan(11) ifout=pppoe-wan(16)
IP4: 192.168.1.233 => 193.46.255.29 proto=tcp ttl=127 sport=63665 dport=443 flags=S seq=2628547509 ack_seq=0
client mode desync profile/ipcache search target ip=193.46.255.29 port=443
desync profile search for tcp ip=193.46.255.29 port=443 icmp=255:255 l7proto=unknown ssid='' hostname=''
desync profile 0 (no_action) matches
dpi desync src=192.168.1.233:63665 dst=193.46.255.29:443 track_direction=out fixed_direction=out connection_proto=unknown payload_type=empty
no lua functions in this profile
packet: id=81 pass unmodified

packet: id=82 len=60 mark=00000000 ifin=br-lan(11) ifout=pppoe-wan(16)
IP4: 192.168.1.233 => 193.46.255.29 proto=tcp ttl=127 sport=50326 dport=443 flags=S seq=1606717897 ack_seq=0
client mode desync profile/ipcache search target ip=193.46.255.29 port=443
desync profile search for tcp ip=193.46.255.29 port=443 icmp=255:255 l7proto=unknown ssid='' hostname=''
desync profile 0 (no_action) matches
dpi desync src=192.168.1.233:50326 dst=193.46.255.29:443 track_direction=out fixed_direction=out connection_proto=unknown payload_type=empty
no lua functions in this profile
packet: id=82 pass unmodified
Сори, не понял вопроса)
Такое вижу в логах

---

**2026-02-26T09:21:43 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.6.4-r82:
  Новые возможности:
  - custom_inbound_tags — автоматическое определение inbound тегов из custom config файлов (sing-box.d/*.json), без ручной настройки в UCI
  - IPv6 user_subnets — поддержка IPv6 CIDR в nft sets для пользовательских подсетей (отдельные наборы с суффиксом *6)
  - timeout_dnsmasq_restart — UCI-опция для настройки таймаута перезапуска dnsmasq (5-300 сек, по умолчанию 15)
  - subscription_user_agent — UCI-опция для кастомного User-Agent при загрузке подписок
  - Декомпиляция .srs — remote и local .srs rule-set файлы декомпилируются для извлечения IP в nft sets

  Исправления:
  - cdn_* списки теперь всегда скачивают свои cidr, остальные только при выборе CIDR списки сообщества = ipv4/ipv6
  - nft sets для user_subnet_lists — создание наборов для tproxy маркировки с парсингом скачанных JSON
  - User-Agent для подписок clash-verge/v2.0.0 — совместимость со Snowfall и другими провайдерами(опция в uci)
  - UCI list для текстовых полей (user_domains_text, user_subnets_text и др.) — сохранение переносов строк
  - Fully Routed DNS: fallback парсит локальные домены из UCI (dnsmasq domain, address= записи)
  - Валидация доменов и CIDR в disable_fakeip — фильтрация невалидных данных в парсерах и генераторах
  - dnsmasq nftset stale handles — рестарт dnsmasq после setup_nftables_batch сбрасывает кэш невалидных handle(фикс race condition в редких случаях)
  - Фильтрация невалидных CIDR в local JSON файлах
  - scandir вместо хардкода в show_sing_box_config + smart merge (собирает пользовательские фрагменты и основной конфиг в диагностике)
  - Trim whitespace в proxy_parser — fix крэша SID, поддержка trojan+reality (pbk, sid, spx)
  - Валидация IP в collect_all_fully_routed_ips — hostname больше не ломает sing-box конфиг
  - force_cidr загрузка IP в singbox конфиг
  - Фильтрация flow="undefined" и flow="none" в VLESS outbounds

  Работа с списками сообщества:
  - Уменьшен лист youtube
  - Переделан лист cidr telegram
  - Добавлено
    games:     "brawlstars.com", "ea.com.battlefield1", "ea.com.battlefield2042", "ea.com.cdn", "r.e.p.o", "steampowered.com"
    ai:        "scira.ai"
    block:     "patreonusercontent.com"
  - Убрано 
    messengers:"mattermost.com", "signal"
#ZeroBlock

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

**2026-03-01T21:56:31 | lxstwxrden**
Просто в z1 есть функция - FILTER_TTL_EXPIRED_ICMP, и выключение его моментально решало проблему, а в z2 такого не увидел

---

**2026-03-02T17:52:24 | Kiss_My_Axe**
варп свернул ipv6 штоле?
root@roskomnadzor:~# ping -6 -I awg10 www.youtube.com
PING www.youtube.com (2a00:1450:400e:80a::200e): 56 data bytes
ping: sendto: Network unreachable

root@roskomnadzor:~# ping -I awg10 www.youtube.com
PING www.youtube.com (172.217.171.110): 56 data bytes
64 bytes from 172.217.171.110: seq=0 ttl=118 time=55.170 ms

---

**2026-03-03T02:32:50 | Борис**
Как мы уже выяснили, youTubeUnblock является инструментом для обхода DPI, который изменяет структуру и атрибуты сетевых пакетов. То, что у юаб есть стратегия "с фейк сни" — не значит, что с помощью этой программы наше устройство пытается "попасть на Ютуб", указывая другой домен (как мы обсуждали с vless reality, когда клиент подключается к туннелю-серверу, указывая поддельный sni). В обычном World Wide Web у вас не получится "зайти на сайт", указав неправильное имя для него — сервер с сайтом не поймёт такой запрос. У сервера есть только сайт youtube.com, а вы ему скажите "дай мне yandex.ru", он тебе ответит "ты куку? Тут такой не проживает."

Так как же это работало в youTubeUnblock и прочих? Очень просто. У сетевых пакетов есть такой атрибут, как ttl (time to live). Этот атрибут означает, сколько "прыжков" между сетевыми узлами пакет способен пережить. Так вот, YUB указывал в пакете sni = yandex.ru и при этом ttl = 3 (я не знаю сколько, но очень маленькое число). Таким образом ТСПУ был узлом #2 и он пускал такой трафик дальше, ведь яндекс для него — это круто и молодёжно. Но реальность в том, что пакет с таким sni умирал сразу после тспу, а до ютуба доходили уже "реальные" намерения человека — "дай мне youtube.com"

Эту лазейку с fake sni быстро прикрыли, так как провайдеру достаточно было выпустить небольшой патч, в котором проверялся не только sni, но и ttl пакета (чтобы сразу видеть, что ему пытаются скормить "обманку")

---

**2026-03-03T07:24:35 | АЛЕКСАНДР**
После обновления Z2  появились настройки Filter TTL Expired ICMP, Flow Offloading  Первая по умолчанию включено Для чего вторая ?

---

**2026-03-03T09:56:00 | Kiss_My_Axe**
Допустим trippy, допустим выяснили, что пятый хоп проблемный, что даёт это знание, кроме прописывания 6 в TTL-страте?

---

**2026-03-03T15:15:25 | Kiss_My_Axe**
А вот ща конфига

Роуте алловед=1
Шлюз по умолчанию=1
Метрика шлюза=4999
Не создавать маршруты=1

сработала.
# ping -6 -I awg10 www.youtube.com
PING www.youtube.com (2a00:1450:400e:806::200e): 56 data bytes
64 bytes from 2a00:1450:400e:806::200e: seq=0 ttl=118 time=58.245 ms
64 bytes from 2a00:1450:400e:806::200e: seq=1 ttl=118 time=59.466 ms
64 bytes from 2a00:1450:400e:806::200e: seq=2 ttl=118 time=55.841 ms
Ура, штоле?

---

**2026-03-04T11:18:36 | Vasilii Pavlenko**
Добрый день, сегодня получил роутер, первичную настройку сделал, запустил Zero+Zapret2.  Ютубы/телеги заработали норм.Теперь вопрос по сути. Я живу в Крыму, из-за санкций имеется блок со стороны Blizzard и прочих США компаний. Чтобы получить доступ к Battle.net использую на своих девайсах КВН в виде 3х-ui панель Vless +reality  на  VPS в Нидерландах + клиент V2RayNG на моих клиентах (ПК +тел)  . Как мне теперь это все завернуть через Роутерич, а не поднимать на каждом девайсе клиента V2Ray? Какую службу я должен поднять на роутере и закинуть туда конфиг файл ? Заранее спасибо

---

**2026-03-04T11:42:00 | Vasilii Pavlenko**
Ага, то есть нужны ip battle.net и Hearthstone в  моем случае?

---

**2026-03-04T11:52:28 | Vasilii Pavlenko**
Добавил battle.net и пошло) Еще раз спасибо)

---

**2026-03-07T18:31:23 | Routerich**
я слышал что некоторые сайты на cloudflare в угоду скорости не отбрасывают фейковые пакеты, т.е. работать может только ttl или что-то очень сильно поломанное(но его уже может и тспу вычислить)

---

**2026-03-11T00:04:28 | Միխայիլ Կուլագին**
// я не настоящий сварщик, пока просто пытаюсь разобраться
Вопрос: а почему многие протоколы пытаются имитировать именно HTTPS?
Я пока нигде не встречал вариант имитации под SMTPS (или STMP+STARTTLS) для короткоживущих коннектов или IMAPS для долгоживущих... Я просто плохо искал или эта идея чем-то нерабочая?

---

**2026-03-12T08:07:07 | Petr Shcherbinin**
ок, включил секцию в ЗБ через свой впн

- работает чатгпт, сделал до него пинг

PING chatgpt.com (8.47.69.6): 56 data bytes
64 bytes from 8.47.69.6: seq=0 ttl=56 time=22.791 ms
64 bytes from 8.47.69.6: seq=1 ttl=56 time=3.816 ms
64 bytes from 8.47.69.6: seq=2 ttl=56 time=1.725 ms
64 bytes from 8.47.69.6: seq=3 ttl=56 time=1.737 ms
64 bytes from 8.47.69.6: seq=4 ttl=56 time=17.875 ms

--- chatgpt.com ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 1.725/9.588/22.791 ms

- не открывается сайт гемини вообще

PING gemini.google.com (108.177.14.100): 56 data bytes
64 bytes from 108.177.14.100: seq=0 ttl=107 time=23.568 ms
64 bytes from 108.177.14.100: seq=1 ttl=107 time=31.341 ms
64 bytes from 108.177.14.100: seq=2 ttl=107 time=15.473 ms
64 bytes from 108.177.14.100: seq=3 ttl=107 time=33.023 ms
64 bytes from 108.177.14.100: seq=4 ttl=107 time=15.115 ms

--- gemini.google.com ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 15.115/23.704/33.023 ms

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

**2026-03-13T23:54:29 | Egor Sorokin**
packet: id=1272 len=1278 mark=20000000 ifin=br-lan(11) ifout=eth1(3)
IP4: 192.168.1.64 => 64.233.165.198 proto=udp ttl=127 sport=60738 dport=443
UDP: len=1250 : CC 00 00 00 01 08 F0 D1 D5 03 FC CE 53 75 00 00 44 D0 C9 E3 AB 3C 46 DC DA 95 10 05 7D 16 FA 11 ... : ............Su..D....<F.....}... ...
client mode desync profile/ipcache search target ip=64.233.165.198 port=443
using cached desync profile 0 (no_action)
packet contains quic_initial payload
reassemble : feeding data payload size=1215. now we have 2430/16384
QUIC initial contains CRYPTO with full fragment coverage
packet contains full TLS ClientHello
TLS handshake version : TLS 1.2
TLS supported versions ext : TLS 1.3
TLS ALPN ext : h3
TLS ECH ext : present
DELAY desync until reasm is complete (#2)
REPLAYING delayed packet #1 offset 0
REPLAY IP4: 192.168.1.64 => 64.233.165.198 proto=udp ttl=127 sport=60738 dport=443
UDP: len=1250 : CD 00 00 00 01 08 F0 D1 D5 03 FC CE 53 75 00 00 44 D0 49 DC 2C 63 D8 9E B3 2E 82 AD 2B 5B 86 59 ... : ............Su..D.I.,c......+[.Y ...
client mode desync profile/ipcache search target ip=64.233.165.198 port=443
using cached desync profile 0 (no_action)
packet contains quic_initial payload
QUIC initial contains CRYPTO with full fragment coverage
packet contains full TLS ClientHello
TLS handshake version : TLS 1.2
TLS supported versions ext : TLS 1.3
TLS ALPN ext : h3
TLS ECH ext : present
hostname: www.youtube.com
discovered l7 protocol
discovered hostname
desync profile search for udp ip=64.233.165.198 port=443 icmp=255:255 l7proto=quic ssid='' hostname='www.youtube.com'
desync profile 0 (no_action) matches
dpi desync src=192.168.1.64:60738 dst=64.233.165.198:443 track_direction=out fixed_direction=out connection_proto=quic payload_type=quic_initial
no lua functions in this profile
SENDING delayed packet #1 unmodified
REPLAYING delayed packet #2 offset 1250
REPLAY IP4: 192.168.1.64 => 64.233.165.198 proto=udp ttl=127 sport=60738 dport=443
UDP: len=1250 : CC 00 00 00 01 08 F0 D1 D5 03 FC CE 53 75 00 00 44 D0 C9 E3 AB 3C 46 DC DA 95 10 05 7D 16 FA 11 ... : ............Su..D....<F.....}... ...
client mode desync profile/ipcache search target ip=64.233.165.198 port=443
using cached desync profile 0 (no_action)
packet contains quic_initial payload
QUIC initial contains CRYPTO with full fragment coverage
packet contains full TLS ClientHello
TLS handshake version : TLS 1.2
TLS supported versions ext : TLS 1.3
TLS ALPN ext : h3
TLS ECH ext : present
hostname: www.youtube.com
dpi desync src=192.168.1.64:60738 dst=64.233.165.198:443 track_direction=out fixed_direction=out connection_proto=quic payload_type=quic_initial
no lua functions in this profile
SENDING delayed packet #2 unmodified
reassemble session finished
packet: id=1272 drop

packet: id=1273 len=1278 mark=20000000 ifin=br-lan(11) ifout=eth1(3)
IP4: 192.168.1.64 => 64.233.165.198 proto=udp ttl=127 sport=60738 dport=443
UDP: len=1250 : CC 00 00 00 01 08 F0 D1 D5 03 FC CE 53 75 00 00 44 D0 7E 7D 70 67 7F 80 8E 7B EB B7 3A A0 92 8B ... : ............Su..D.~}pg..{..:... ...
client mode desync profile/ipcache search target ip=64.233.165.198 port=443
using cached desync profile 0 (no_action)
packet contains quic_initial payload
QUIC initial contains CRYPTO with partial fragment coverage
starting reassemble. now we have 1215/16384
DELAY desync until reasm is complete (#1)
packet: id=1273 drop

журнал, категория основные

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

**2026-03-15T15:40:48 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.1-r38:
  Изменения:

  uci-defaults: полный набор дефолтов
  Все 47 опций теперь гарантированно создаются при чистой установке:
  - DNS: dns_type, dns_server, bootstrap_dns_server, dns_rewrite_ttl, dns_strategy
  - Флаги: disable_quic, dns_hijack, discord_voice, exclude_bittorrent, exclude_ntp, ipv6_enabled, proxy_router_traffic и др.
  - Пути: xray_path, trusttunnel_path
  - Таймауты: xray_startup_timeout (10 сек), singbox_startup_timeout, dpi_check_timeout
  - Прочее: clash_api_port, log_level, update_interval, subscription_user_agent
  Изменения:
  UCI опции: полная согласованность
  - Исправлена проблема рассинхронизации между LuCI и backend — при включении checkbox в LuCI опция удалялась из UCI (совпадала с дефолтом), а backend считал её выключенной. Теперь все Flag-опции имеют rmempty=false и всегда записывают 0 или 1 в UCI.
#ZeroBlock

---

**2026-03-16T01:20:35 | Gremlins**
Смотрите ваши настроенные DNS
ping ya.ru
PING ya.ru (77.88.55.242): 56 data bytes
64 bytes from 77.88.55.242: seq=0 ttl=55 time=8.491 ms
64 bytes from 77.88.55.242: seq=1 ttl=55 time=8.419 ms
64 bytes from 77.88.55.242: seq=2 ttl=55 time=8.432 ms
64 bytes from 77.88.55.242: seq=3 ttl=55 time=8.433 ms
64 bytes from 77.88.55.242: seq=4 ttl=55 time=8.414 ms
64 bytes from 77.88.55.242: seq=5 ttl=55 time=8.385 ms
64 bytes from 77.88.55.242: seq=6 ttl=55 time=8.433 ms
64 bytes from 77.88.55.242: seq=7 ttl=55 time=8.428 ms
64 bytes from 77.88.55.242: seq=8 ttl=55 time=8.425 ms
64 bytes from 77.88.55.242: seq=9 ttl=55 time=8.398 ms
^C
--- ya.ru ping statistics ---
10 packets transmitted, 10 packets received, 0% packet loss
round-trip min/avg/max = 8.385/8.425/8.491 ms
root@RouteRich:~# cat /etc/resolv.conf
search lan
nameserver 127.0.0.1
nameserver ::1
root@RouteRich:~#
root@RouteRich:~#
root@RouteRich:~# dig @127.0.0.1 +short ya.ru
77.88.44.242
77.88.55.242
5.255.255.242
root@RouteRich:~#

---

**2026-03-16T10:43:43 | Andrey Voloshin**
остановил ZB, сразу вот
root@OpenWrt:~# ping ya.ru
PING ya.ru (77.88.55.242): 56 data bytes
64 bytes from 77.88.55.242: seq=0 ttl=56 time=33.448 ms
64 bytes from 77.88.55.242: seq=1 ttl=56 time=33.238 ms

---

**2026-03-16T14:49:31 | Rom@n**
Вот он мне нашел, я по одной строчке вставляю, например так и пробую запускать дискорд:
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=1
--in-range=-s1 --lua-desync=oob:urp=b
--in-range=-s1 --lua-desync=oob:urp=0
--in-range=-s1 --lua-desync=oob:urp=2
--in-range=-s1 --lua-desync=oob:urp=midsld
--payload=tls_client_hello --lua-desync=multidisorder:pos=2
--payload=tls_client_hello --lua-desync=multidisorder:pos=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+1
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+4
--payload=tls_client_hello --lua-desync=multidisorder:pos=host+1
--payload=tls_client_hello --lua-desync=multidisorder:pos=midsld
--payload=tls_client_hello --lua-desync=multidisorder:pos=1,midsld
--payload=tls_client_hello --lua-desync=multidisorder:pos=1,midsld,1220
--payload=tls_client_hello --lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,-1:seqovl=1 --lua-desync=drop
--payload=tls_client_hello --lua-desync=multisplit:pos=10:seqovl=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=2:seqovl=1
--lua-init=fake_default_tls=tls_mod(fake_default_tls,'rnd') --payload=tls_client_hello --lua-desync=multidisorder:pos=2:seqovl=1:seqovl_pattern=fake_default_tls
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+1:seqovl=sniext
--lua-init=fake_default_tls=tls_mod(fake_default_tls,'rnd') --payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+1:seqovl=sniext:seqovl_pattern=fake_default_tls
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+4:seqovl=sniext+3
--lua-init=fake_default_tls=tls_mod(fake_default_tls,'rnd') --payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+4:seqovl=sniext+3:seqovl_pattern=fake_default_tls
--payload=tls_client_hello --lua-desync=multidisorder:pos=midsld:seqovl=midsld-1
--lua-init=fake_default_tls=tls_mod(fake_default_tls,'rnd') --payload=tls_client_hello --lua-desync=multidisorder:pos=midsld:seqovl=midsld-1:seqovl_pattern=fake_default_tls
--payload=tls_client_hello --lua-desync=multidisorder:pos=2,midsld:seqovl=1
--lua-init=fake_default_tls=tls_mod(fake_default_tls,'rnd') --payload=tls_client_hello --lua-desync=multidisorder:pos=2,midsld:seqovl=1:seqovl_pattern=fake_default_tls
--lua-desync=syndata --payload=tls_client_hello --lua-desync=multisplit
--lua-desync=syndata:blob=0x1603 --payload=tls_client_hello --lua-desync=multisplit
--lua-desync=syndata --payload=tls_client_hello --lua-desync=multidisorder
--lua-desync=syndata:blob=0x1603 --payload=tls_client_hello --lua-desync=multidisorder
--payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:ip_ttl=5:tls_mod=rnd,dupsid,padencap:repeats=1
--payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:tcp_md5:tls_mod=rnd,dupsid,padencap:repeats=1
--payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:tcp_md5:repeats=1 --payload=empty --out-range=<s1 --lua-desync=send:tcp_md5
--payload=tls_client_hello --lua-desync=fake:blob=0x00000000:tcp_md5:repeats=1 --lua-desync=fake:blob=fake_default_tls:tcp_md5:tls_mod=rnd,dupsid:repeats=1 --payload=empty --out-range=<s1 --lua-desync=send:tcp_md5
--payload=tls_client_hello --lua-desync=multisplit:blob=fake_default_tls:tcp_md5:pos=2:nodrop:repeats=1 --payload=empty --out-range=<s1 --lua-desync=send:tcp_md5
--payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:tcp_md5:tls_mod=rnd,dupsid,padencap:repeats=1 --payload=empty --out-range=<s1 --lua-desync=send:tcp_md5
--payload=tls_client_hello --lua-desync=fake:blob=0x00000000:tcp_seq=-3000:repeats=1 --lua-desync=fake:blob=fake_default_tls:tcp_seq=-3000:tls_mod=rnd,dupsid:repeats=1
--payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
--payload=tls_client_hello --lua-desync=fake:blob=0x00000000:tcp_seq=1000000:repeats=1 --lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:tls_mod=rnd,dupsid:repeats=1

---

**2026-03-18T13:05:43 | Alex Korshun**
Фреса, нужно ли подкручивать настройки TTL в bc2 итд? Просто я негодую, ни одной рабочей стратегии за несколько часов поиска, ну вообще 0 (для discord'а). 
Думал было вообще тотальный блок со стороны провайдера (ТТК), но нет, IP адрес пингуется. 
Будь добр, подскажи, пожалуйста.🎉

---

**2026-03-18T13:39:17 | Alex Korshun**
TTL не подкручивали?

---

**2026-03-20T10:34:47 | Tim Mars**
ребят, привет
сорри, возможно за глупые вопросы, но, хотел уточнить у вас по поводу роутра ибо ранее с этим не сталкивался

хочу приобрести его для игр, iptv и прочего, так как мой региональный провайдер надоел и видимо на нас тестируют самые разные варианты блокировок, отсюда и половина интернета не работает и тут вопрос, решит ли проблему роутер с:
– iptv смотрю через телевизор, и тут нужен нативный пинг/задержка, в противном случае будет тормозить и плохо показывать
– игрушки, по типу battlefield 6 (читал, что вроде как есть вариант решения, но переспрошу, будет ли работать онлайн), arc raiders (голосовой чат), ea fc 26 (будет ли менятся ping или нет? пробовал заводить через warp от cloudflare что логично помогает в работе но увеличивает ping почти в два раза или больше)
– будет ли работать корректно xbox/psn network на PS5 (сегодня у меня, например, не пускает в лк и пишет что нет соединения с сервером, с впн нормально все работает)
– ютуб, телеграм и прочие сервисы насколько будут стабильны в работе? к примеру через vpn последнее время telegram работает плохо, только через mtpproxy но их нужно постоянно обновлять искать новые

в большей степени, конечно, интересует работа и задержка при работе с медиа (игры/фильмы/ip тв)

заранее благодарю за ответ

---

**2026-03-20T11:36:07 | Борис**
Насчёт iptv не знаю, все остальное что ты перечислил будет работать. Я через этот роутер завёл Battlefield 6, когда его осенью блокировали (был на серверах амазона) через zapret, всё получилось - мог играть. Играл, к слову, на ps5, соответственно там с сетью тоже никаких проблем. Если что, просто настроишь, исключения добавишь в zapret. Ютуб тоже работает с этим роутером, телеграм тоже (я сейчас им пользуюсь). "Vpn" используется у меня только для telegram, всё остальное, включаяя игры и psn работает через zapret (система обхода dpi), а значит я использую свой российский ip и у меня нет дополнительных задержек из-за использования каких-то дополнительных серверов

---

**2026-03-20T11:37:44 | Борис**
Сейчас Battlefield 6 вроде как ушел с amazon, у него ресурсы на akamai, и там пока нет блокировок, можно без всяких обходов играть. Arc raiders я не знаю, но судя по тому, что ты сказал, там есть некий отдельный сервер для голосового чата, ты сможешь при помощи отладки его обнаружить и как-то добавить в zapret, либо просто загуглить "zapret arc raiders"

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

**2026-03-23T12:08:18 | Kiss_My_Axe**
И вот ещё прикол из винды. Кэш днс очищен.
ДНСом в ЗБ 10.8.12.1

C:\Windows\System32>nslookup ya.ru
╤хЁтхЁ:  roskomnadzor.lan
Address:  192.168.10.1

DNS request timed out.
    timeout was 2 seconds.
DNS request timed out.
    timeout was 2 seconds.
*** Превышено время ожидания запроса roskomnadzor.lan

C:\Windows\System32>ping ya.ru

Обмен пакетами с ya.ru [5.255.255.242] с 32 байтами данных:
Ответ от 5.255.255.242: число байт=32 время=13мс TTL=55
Ответ от 5.255.255.242: число байт=32 время=14мс TTL=55
Ответ от 5.255.255.242: число байт=32 время=14мс TTL=55
Ответ от 5.255.255.242: число байт=32 время=13мс TTL=55

---

**2026-03-24T15:37:20 | Святос**
--lua-desync=fake:blob=fake_default_tls:ip_ttl=2:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1 и как вот это писать

---

**2026-03-24T15:41:56 | Routerich**
такое писать примерно так
--lua-desync=fake:blob=fake_default_tls:ip_ttl=2:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1

---

**2026-03-24T16:08:14 | Святос**
--out-range=-s34228
--payload=tls_client_hello
--in-range=-s5556 
--lua-desync=circular:fails=3:maxtime=60
--lua-desync=fake:blob=fake_default_tls:ip_ttl=2:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1:strategy=1
--lua-desync=fake:blob=fake_default_tls:ip_ttl=3:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1:strategy=2
--lua-desync=fake:blob=fake_default_tls:ip_ttl=4:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1:strategy=3
--lua-desync=fake:blob=fake_default_tls:ip_ttl=5:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1:strategy=4
--lua-desync=fake:blob=fake_default_tls:ip_ttl=6:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1:strategy=5
--lua-desync=fake:blob=fake_default_tls:ip_ttl=7:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1:strategy=6
--lua-desync=fake:blob=fake_default_tls:ip_ttl=8:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1:strategy=7
--lua-desync=fake:blob=fake_default_tls:badsum:repeats=1:strategy=8
--lua-desync=fake:blob=fake_default_tls:tcp_ts=-1000:repeats=1:strategy=9:final

---

**2026-03-24T16:43:20 | Святос**
--out-range=-s34228
--payload=tls_client_hello
--in-range=-s5556 
--lua-desync=circular:fails=3:maxtime=60
--in-range=x
--lua-desync=fake:blob=fake_default_tls:ip_ttl=2:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1:strategy=1
--lua-desync=fake:blob=fake_default_tls:ip_ttl=3:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1:strategy=2
--lua-desync=fake:blob=fake_default_tls:ip_ttl=4:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1:strategy=3
--lua-desync=fake:blob=fake_default_tls:ip_ttl=5:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1:strategy=4
--lua-desync=fake:blob=fake_default_tls:ip_ttl=6:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1:strategy=5
--lua-desync=fake:blob=fake_default_tls:ip_ttl=7:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1:strategy=6
--lua-desync=fake:blob=fake_default_tls:ip_ttl=8:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1:strategy=7
--lua-desync=fake:blob=fake_default_tls:badsum:repeats=1:strategy=8
--lua-desync=fake:blob=fake_default_tls:tcp_ts=-1000:repeats=1:strategy=9
--lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=fonts.google.com:tcp_seq=10000:strategy=10
--lua-desync=multisplit:pos=1,midsld:seqovl=1:seqovl_pattern=tls_clienthello:tcp_ts_up:strategy=10
--lua-desync=fake:blob=0x00000000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=www.google.com:repeats=2:strategy=11
--lua-desync=multisplit:pos=1,midsld:strategy=11
--lua-desync=hostfakesplit:host=ozon.ru:midhost=host-2:seqovl=sniext+3:seqovl_pattern=tls_clienthello:badsum:tcp_md5:tcp_ts_up:strategy=12
--lua-desync=hostfakesplit:tcp_md5:tcp_ts_up:strategy=12:final

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

**2026-03-26T11:02:33 | Routerich**
ttl крутните больше в настройках

---

**2026-04-01T09:14:21 | HiLLL**
Список исключений Epicgames взят у StressOzz. Не знаю зачем, но придумай, что с этим делать.
easy.ac
fab.com
quixel.se
quixel.com
eac-cdn.com
paragon.com
spyjinx.com
3lateral.com
fortnite.com
epicgames.com
epicgames.dev
hyprsense.com
sketchfab.com
artstation.com
roborecall.com
twinmotion.com
cubicmotion.com
playparagon.com
realityscan.com
epicgamescdn.com
radgametools.com
unrealengine.com
easyanticheat.net
shadowcomplex.com
battlebreakers.com
capturingreality.com
unrealtournament.com

---

**2026-04-01T21:57:55 | Артем Погодин**
До 8.8.8.8: 
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=110 time=13.208 ms
64 bytes from 8.8.8.8: seq=1 ttl=110 time=13.163 ms
64 bytes from 8.8.8.8: seq=2 ttl=110 time=13.175 ms
64 bytes from 8.8.8.8: seq=3 ttl=110 time=13.828 ms
64 bytes from 8.8.8.8: seq=4 ttl=110 time=13.250 ms

--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 13.163/13.324/13.828 ms

До ya.ru пишет неверный адрес

---

**2026-04-01T22:29:36 | Артем Погодин**
С телефона не заходит на запрещенные ресурсы
На ya.ru - заходит

ya.ru пингуется:
PING ya.ru (5.255.255.242): 56 data bytes
64 bytes from 5.255.255.242: seq=0 ttl=58 time=3.753 ms
64 bytes from 5.255.255.242: seq=1 ttl=58 time=3.692 ms
64 bytes from 5.255.255.242: seq=2 ttl=58 time=3.822 ms
64 bytes from 5.255.255.242: seq=3 ttl=58 time=3.785 ms
64 bytes from 5.255.255.242: seq=4 ttl=58 time=3.717 ms

--- ya.ru ping statistics ---
5 packets transmitted, 5 packets received, 0% packet loss
round-trip min/avg/max = 3.692/3.753/3.822 ms

---

**2026-04-02T00:50:55 | Dark Ghost**
Это называется OMFG...
Кто бы мог подумать...
C:\>ipconfig /flushdns

Настройка протокола IP для Windows

Кэш сопоставителя DNS успешно очищен.

C:\>ping ya.ru

Обмен пакетами с ya.ru [77.88.55.242] с 32 байтами данных:
Ответ от 77.88.55.242: число байт=32 время=16мс TTL=55
Ответ от 77.88.55.242: число байт=32 время=14мс TTL=55
Ответ от 77.88.55.242: число байт=32 время=9мс TTL=55
Ответ от 77.88.55.242: число байт=32 время=43мс TTL=55

Статистика Ping для 77.88.55.242:
    Пакетов: отправлено = 4, получено = 4, потеряно = 0
    (0% потерь)
Приблизительное время приема-передачи в мс:
    Минимальное = 9мсек, Максимальное = 43 мсек, Среднее = 20 мсек

---

**2026-04-02T10:29:46 | Двуногий**
Ttl фиксировали на роутере?

---

**2026-04-02T10:33:25 | Двуногий**
Попробуйте с другой симкой/оператором

Я такое встречал только на смартфонных симках без ttl. Причем у вас раз в сутки, а бывает каждый час-полтора повисает

---

**2026-04-03T19:49:31 | Routerich**
вот конфиг демона, часть опций есть и в старом зероблоке, иногда полезно смотреть мануал и конфиги трогать
config settings 'settings'
  option log_level 'warn'
  option health_interval '600'
  option health_dns_check '1'
  option health_ping_ip '1.1.1.1 8.8.8.8'
  option health_opera_host 'ya.ru google.com'
  option update_interval '1d'
  option timeout_dnsmasq_restart '15'
  option api 'v2'
  option health_enabled '1'
  option update_time '09:00'
  option enable_bad_interface_monitoring '0'
  option download_lists_via_proxy '0'
  option auto_fallback_two_stage '1'
  option subscription_update_interval 'off'

config engine 'engine'
  option dns_type 'doh'
  option dns_server '8.8.8.8'
  option bootstrap_dns_server '77.88.8.8'
  option dns_rewrite_ttl '60'
  option dns_strategy 'ipv4_only'
  option clash_api_enabled '1'
  option clash_api_port '9090'
  option tproxy_mark '0x10000'
  option direct_mark '0x20000'
  option bt_mark '0x40000'
  option ctmark_dns '0x10000'
  option ctmark_bt '0x40000'
  option disable_quic '1'
  option desync_mark '0x40000000'
  option log_level 'warn'
  option dont_touch_dhcp '0'
  option dns_hijack '1'
  option enable_output_network_interface '0'
  option proxy_router_traffic '0'
  option ipv6_enabled '0'
  option discord_voice '1'
  option exclude_bittorrent '1'
  option exclude_ntp '1'
  option singbox_logging '0'
  option xray_logging '0'
  option trusttunnel_logging '0'
  option fakeip_query_type_filter '1'
  option xray_path '/usr/bin/xray'
  option trusttunnel_path '/usr/bin/trusttunnel_client'
  option custom_config_dir '/etc/zeroblock/sing-box.d'
  option dpi_check_timeout '15'
  option singbox_startup_timeout '30000'
  option xray_startup_timeout '10000'
  option subscription_timeout '30000'
  option subscription_max_proxies '100'
  option subscription_user_agent 'clash-verge/v2.0.0'
  list source_network_interfaces 'br-lan'
  option testing_url 'http://www.gstatic.com/generate_204'

---

**2026-04-05T14:15:19 | 🌶️🌶️**
PING ya.ru

Обмен пакетами с ya.ru [77.88.55.242] с 32 байтами данных:
Ответ от 77.88.55.242: число байт=32 время=26мс TTL=57
Ответ от 77.88.55.242: число байт=32 время=26мс TTL=57
Ответ от 77.88.55.242: число байт=32 время=27мс TTL=57
Ответ от 77.88.55.242: число байт=32 время=27мс TTL=57

    Пакетов: отправлено = 4, получено = 4, потеряно = 0
    (0% потерь)
Приблизительное время приема-передачи в мс:
    Минимальное = 26мсек, Максимальное = 27 мсек, Среднее = 26 мсек

---

**2026-04-05T14:20:34 | 🌶️🌶️**
ping ya.ru -l 56

Обмен пакетами с ya.ru [5.255.255.242] с 56 байтами данных:
Ответ от 5.255.255.242: число байт=56 время=33мс TTL=57
Ответ от 5.255.255.242: число байт=56 время=34мс TTL=57
Ответ от 5.255.255.242: число байт=56 время=33мс TTL=57
Ответ от 5.255.255.242: число байт=56 время=34мс TTL=57

Статистика Ping для 5.255.255.242:
    Пакетов: отправлено = 4, получено = 4, потеряно = 0
    (0% потерь)
Приблизительное время приема-передачи в мс:
    Минимальное = 33мсек, Максимальное = 34 мсек, Среднее = 33 мсек

---

**2026-04-05T18:05:54 | Vasa**
пабг вроде немного

kraftonde.com
playbattlegrounds.com
pubg.com
pubg1.battleye.com

---

**2026-04-06T03:20:04 | Степанов Владимир**
Не нашел тут ответа, может кто подскажет как настроить чтоб сервера Battlefield 6 снова стали работать!

---

**2026-04-06T21:52:10 | Макс**
в Сибири как всегда в первую очередь начали новые блокировки вводить. Отвалился EA app, battle net. Кто нибудь пробовал фиксить это? Есть какие то варианты?

---

**2026-04-06T21:56:13 | Vladimir**
Множество сервисов упало по всей России — официальной причины ещё нет

Steam, Discord, Valorant, Battle.Net и другие популярные сервисы сейчас недоступны у части пользователей.

---

**2026-04-06T22:03:30 | Макс**
⚡️Рунет умер в России — тонны сайтов попросту перестали загружаться, среди них: банки, соцсети и игровые сервисы, вроде Steam и Battle net.

Блокировка всего, наконец-то.

🕹КиберТопор — Подписаться

---

**2026-04-07T10:30:11 | Владимир Волков**
Инженер психанул, что все мессенджеры живут по чужим правилам, и написал свой

Когда Telegram падает, облако лежит, а условия сервиса меняются без предупреждения — это не ваш канал связи, это аренда. Автор решил это исправить: PWA-мессенджер на собственном бэкенде, без инвесторов и презентаций.
Внутри оказалось куда интереснее, чем «просто чатик»:

— идемпотентность доставки и дедупликация, потому что «отправил» ≠ «дошло»;
— race condition между потоками онлайн-статуса;
— optimistic update против серверной истины на нескольких устройствах сразу;
— graceful degradation для клиентов с сетью «между EDGE и молитвой».

Плюс живое сравнение двух SQL-запросов для полнотекстового поиска: наивный вариант против варианта с partial GIN-индексом — разница на реальном объёме 10x и выше.

Ещё — UIN-рулетка до регистрации в духе ICQ: снаружи фан, внутри резервация ресурса с TTL и защитой от ботнета.

---

**2026-04-07T10:52:38 | Ilya Palienko**
а можно чуть-чуть поконкретнее? это "Перезапись TTL для DNS"?

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

**2026-04-07T18:56:00 | FelS**
подскажите как-то можно "Hetzner Online GmbH" пропроксировать или тип того, на их серваках стоит сеть серверов arma этот к примеру (https://www.battlemetrics.com/servers/reforger/32751518)

---

**2026-04-08T21:43:45 | Vasa**
ну это список доменов EA

насколько он полный я хз, проверять мне негде

попробуй в ручной список добавить домены для батлы, хотя мне кажется этого нехватит

battlefield.com
battlefield1943.com
battlefield3.com
battlefield4.com
battlefield5.com
battlefieldheroes.com
battlefieldv.com
battlelog.com

battlefieldbadcompany2.com
battlefront2.com
battlefrontii.com

---

**2026-04-09T15:34:31 | Albert**
#battlefield, #bf, #вылет, #игра, #ea

Всем привет, может кому поможет с проблемами с вылетом баттлы. У меня конкретно в Battlefield 1 (бф1) помогло. Алгоритм такой был: запускаю игру, захожу в сервер-играю-вылетаю (случайно через 1,3,5,15 сек или через 5 мин). После этого сразу захожу в веб-панель роутера-система-мониторинг-вкладка "журнал URL", самый низ и там увидел, что запросы вот туда или оттуда идут: gateway.ea.com
bam.nr-data.net
autopatch.juno.ea.com
sparta-gw.battlelog.com
bf1-terminator.ops.dice.se
sparta-gw.battlelog.com
eaassets-a.akamaihd.net
ratt.juno.ea.com
accounts.ea.com
diceprodblapp-09.ea.com
winter15.gosredirector.ea.com
data1.origin.com
api1.origin.com
qos-prod-bio-syd-common-common.gos.ea.com
qos-prod-m3d-brz-common-common.gos.ea.com
qos-prod-i3d-hkg-common-common.gos.ea.com
qos-prod-aws-fra-common-common.gs.ea.com Решил добавить в свой влесс в зероблоке след. домены: sparta-gw.battlelog.com
bam.nr-data.net
bf1-terminator.ops.dice.se
eaassets-a.akamaihd.net
data1.origin.com
api1.origin.com
ea.com

---

**2026-04-09T16:31:31 | Routerich**
живее всех живых
root@OpenWrt:~# ping -I warp 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=107 time=54.599 ms

root@OpenWrt:~# ping -I warp_nl 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=118 time=87.440 ms

root@OpenWrt:~# ping -I warp_limon_ru 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=107 time=65.240 ms

root@OpenWrt:~# ping -I warp_ru_backup 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: seq=0 ttl=108 time=64.104 ms

---

**2026-04-10T09:01:32 | Danya Co**
Решили проблему с вылетов battlefield 6?

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

**2026-04-11T17:23:10 | Stefan Lapin**
-----------------------------------------------------
 RouteRich 24.10.5, r29087-d9c5716d1d
 -----------------------------------------------------
root@RouteRich:~# ping 192.168.2.166 -c 4
PING 192.168.2.166 (192.168.2.166): 56 data bytes
64 bytes from 192.168.2.166: seq=0 ttl=64 time=3.485 ms
64 bytes from 192.168.2.166: seq=1 ttl=64 time=2.651 ms
64 bytes from 192.168.2.166: seq=2 ttl=64 time=3.102 ms
64 bytes from 192.168.2.166: seq=3 ttl=64 time=2.083 ms

--- 192.168.2.166 ping statistics ---
4 packets transmitted, 4 packets received, 0% packet loss
round-trip min/avg/max = 2.083/2.830/3.485 ms
root@RouteRich:~#

---

**2026-04-11T18:51:45 | Kinaman**
Версия встроенного ПО: RouteRich 24.10.5 r29087-d9c5716d1d RR-3.9.0 / LuCI openwrt-24.10 branch 26.039.68875~ec3d818


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
        option outbound_json '{
  "type": "http",
  "tag": "http-proxy",
  "server": "127.0.0.1",
  "server_port": 18080
}'
        option user_domains_text 'myip.com'
        list community_lists 'geoblock'
        list community_lists 'block'
        list community_lists 'meta'
        list community_lists 'twitter'
        list community_lists 'hdrezka'
        list community_lists 'tiktok'
        list community_lists 'google_ai'

config section 'Youtube_Discord'
        option connection_type 'vpn'
        option interface 'awg10'
        option domain_resolver_enabled '0'
        option user_domain_list_type 'text'
        option user_subnet_list_type 'disabled'
        option mixed_proxy_enabled '0'
        option user_domains_text '2ip.ru
amazonaws.com
whatsapp.com
whatsapp.net
whatsapp.biz
wa.me
quiz.com
vd6s.com
rutracker.org
zophar.net
auphonic.com
thecoverproject.net
engsbk.mahjongsoul.com
ext-twitch.tv
jtvnw.net
live-video.net
ttvnw.net
twitch.tv
twitchcdn.net
twitchsvc.net'
        list remote_subnet_lists 'https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_cidr_ipv4.txt'
        list community_lists 'telegram'
        list community_lists 'discord'
        list community_lists 'meta'

---

**2026-04-12T01:38:33 | support**
Подскажите почему это не работает адекватно, ютюб работает, но все остально что на скринах пугает. 
NFQWS2_OPT="--filter-udp=443 --filter-l7=quic --hostlist-domains=youtube.com,googlevideo.com,youtu.be,googleapis.com,ytimg.com,ggpht.com,gstatic.com,google.com --out-range=-s34228 --payload=quic_initial --lua-desync=fake:blob=quic_initial:ip_ttl=6 --new --filter-udp=443 --filter-l7=quic --hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt --out-range=-s34228 --payload=quic_initial --lua-desync=fake:blob=quic_initial:repeats=6 --new --filter-tcp=80 --filter-l7=http --hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt --out-range=-s34228 --payload=http_req --lua-desync=fake:blob=http:tcp_md5 --lua-desync=multisplit:pos=method+2 --new --filter-tcp=443 --filter-l7=tls --hostlist-domains=youtube.com,googlevideo.com,youtu.be,googleapis.com,ytimg.com,ggpht.com,gstatic.com,google.com --out-range=-s34228 --in-range=-s5556 --lua-desync=circular:fails=1:maxtime=5 --in-range=x --payload=tls_client_hello --lua-desync=multidisorder:pos=1,midsld:strategy=1 --lua-desync=multidisorder:pos=1:seqovl=681:seqovl_pattern=tls_clienthello:strategy=2 --lua-desync=multidisorder:pos=10,midsld:seqovl=336:seqovl_pattern=tls_clienthello:strategy=3 --lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=4 --lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=www.google.com:strategy=5 --lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=google.com:strategy=6 --lua-desync=fakedsplit:pos=midsld:strategy=7 --lua-desync=multidisorder:pos=1,midsld,sniext:strategy=8 --lua-desync=multidisorder:pos=1,sniext+1,midsld-2,midsld,midsld+2:strategy=9 --lua-desync=fake:blob=tls_clienthello:ip_ttl=6:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=rzd.ru:repeats=4:strategy=9 --lua-desync=multidisorder:pos=2,5,105,sniext+5,midsld-1:strategy=10 --lua-desync=multisplit:pos=10:seqovl=1:strategy=11 --new --filter-tcp=443 --filter-l7=tls --hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt --out-range=-s34228 --payload=tls_client_hello --lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=2gis.com --lua-desync=multisplit:pos=2 --new --filter-l7=mtproto --payload=mtproto_initial --lua-desync=fake:blob=0x00000000 --new --filter-tcp=443 --filter-l7=tls --ipset=/opt/zapret2/ipset/zapret-ips-user.txt --out-range=-s34228 --payload=tls_client_hello --lua-desync=multidisorder:pos=1,sniext+1,midsld-2,midsld,midsld+2 --lua-desync=fake:blob=tls_clienthello:ip_ttl=6:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=rzd.ru:repeats=4"

---

**2026-04-13T08:52:13 | Андрей**
root@RouteRich:~# ping 2ip.io
PING 2ip.io (188.40.167.81): 56 data bytes
64 bytes from 188.40.167.81: seq=0 ttl=56 time=44.691 ms
64 bytes from 188.40.167.81: seq=1 ttl=56 time=44.682 ms
64 bytes from 188.40.167.81: seq=2 ttl=56 time=44.658 ms
64 bytes from 188.40.167.81: seq=3 ttl=56 time=44.483 ms
64 bytes from 188.40.167.81: seq=4 ttl=56 time=44.627 ms
64 bytes from 188.40.167.81: seq=5 ttl=56 time=44.896 ms
^C
--- 2ip.io ping statistics ---
6 packets transmitted, 6 packets received, 0% packet loss
round-trip min/avg/max = 44.483/44.672/44.896 ms
root@RouteRich:~#

Всем доброе утро!
Помогите найти причину.
Не открываются сайты 2ip.ru, 2ip.io. whoer.net

---

**2026-04-13T21:54:52 | ­**
Добрый вечер, подскажите пожалуйста, я провел тест и он мне написал стратегии, мне нужно эти стратегии как то реализовать? И как?
--payload=http_req --lua-desync=http_methodeol
--lua-desync=syndata
--lua-desync=syndata --payload=http_req --lua-desync=multisplit
--lua-desync=syndata --payload=http_req --lua-desync=multidisorder
--payload=http_req --lua-desync=fake:blob=fake_default_http:ip_ttl=2:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1

---

**2026-04-14T19:51:35 | Evgeniy**
Игра Total battle туго идет

---

**2026-04-15T19:06:40 | 01000000**
9/4590] fake_default_tls_ttl2_ackdrop
          --payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:ip_ttl=2:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1
          fixed:  +6/11 SE.AKM-01(3.1M), US.CDN77-01(64K), FI.HE-02(146K), FI.HE-03(1.0M), NL.SW-01(167K), US.VLTR-01(76K)
          broken: !7/22 FR.CNTB-01(15K), FR.CNTB-02(15K), US.DO-01(0B), US.DO-03(0B), US.MBCOM-01(19K), FR.OVH-01(0B), FR.OVH-02(0B)
  [10/4590 STRATEGIES

---

**2026-04-15T19:06:50 | 01000000**
--lua-desync=fake:blob=fake_default_tls:ip_ttl=2:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1

---

**2026-04-16T19:01:19 | Ruslan Bilyk**
--payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:ip_ttl=4:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1
--payload=tls_client_hello --lua-desync=multisplit:blob=fake_default_tls:ip_ttl=4:pos=2:nodrop:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1
--payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:tcp_md5:repeats=1 --payload=empty --out-range=<s1 --lua-desync=send:tcp_md5
--payload=tls_client_hello --lua-desync=multisplit:blob=fake_default_tls:tcp_md5:pos=2:nodrop:repeats=1 --payload=empty --out-range=<s1 --lua-desync=send:tcp_md5
--payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
--payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN:repeats=1
--payload=tls_client_hello --lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1
--payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:ip_autottl=-2,3-20:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1
--payload=tls_client_hello --lua-desync=multisplit:blob=fake_default_tls:ip_autottl=-2,3-20:pos=2:nodrop:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1
--payload=tls_client_hello --lua-desync=multisplit:blob=fake_default_tls:ip_autottl=-3,3-20:pos=2:nodrop:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1
--payload=tls_client_hello --lua-desync=multisplit:blob=fake_default_tls:ip_autottl=-4,3-20:pos=2:nodrop:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1
--payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:ip_autottl=-5,3-20:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1
--payload=tls_client_hello --lua-desync=multisplit:blob=fake_default_tls:ip_autottl=-5,3-20:pos=2:nodrop:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1
--payload=tls_client_hello --lua-desync=fakedsplit:pos=sniext+4:ip_ttl=6:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1
--payload=tls_client_hello --lua-desync=fakedsplit:pos=1,midsld:tcp_seq=1000000

---

**2026-04-16T19:28:53 | Gremlin**
как в модемах с TTL

---

**2026-04-17T15:24:47 | Dmitrij Romanov**
Сегодня был один разрыв сессии.
В логах только
nf_ct_snmp: dropping packet: parser failed
[3636257.091599]  IN= OUT= SRC=95.31.12.65 DST=172.235.174.97 LEN=1308 TOS=0x00 PREC=0x00 TTL=63 ID=0 DF PROTO=UDP SPT=51919 DPT=161 LEN=1288

Из-за того, чот dmesg не пишет текущее время, не понятно это оно или не оно.

---

**2026-04-18T14:03:40 | Routerich**
Вообще если интерфейс модема видно, можно проверить есть ли например пинг.

ping 192.168.8.1

Если пинг есть, надо посмотерть как устроены маршруты:

route

По уму, default должен идти через gateway eth2 (или что в вашем случае, какой интерфейс у модема).
Можно попробовать задать TTL, может в этом проблема:
В настройках роутера, зайти в Модем - Интерфейс - Настройки. Там поставить галочку TTL-fix, выставить руками значение 63 (для модемов которые сетевые карты), нажать применить.

Прошить модем не самая плохая идея. На 3272 прошивок было сделано чуть меньше чем на 3372. А значит там зоопарк прошивок сделаных разной степенью умелости умельцами. Лучше прошить то чем я сам в свое время пользовался. Когда-то, очень давно, у меня был такой модем.

---

**2026-04-18T17:30:05 | Vladislav Ivshin**
всем привет, пытаюсь найти рабочую стратегию для запрета, использую zapret2-finder(или Поиск стратегии в гуи), можете подсказать, что значит fixed и broken, и может ли быть fixed 14/14?
[21/4050] fake_default_tls_ttl4_ackdrop
          --payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:ip_ttl=4:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1
          fixed:  +10/14 SE.AKM-01(3.1M), US.CDN77-01(64K), US.CF-01(149K), US.CF-02(100K), LU.GCORE-01(121K), FI.HE-02(146K), FI.HE-03(1.0M), NL.SW-01(167K), DE.VLTR-01(623K), US.VLTR-01(76K)
          broken: !8/19 FR.CNTB-01(15K), FR.CNTB-02(15K), US.DO-01(0B), US.DO-02(0B), US.DO-03(0B), US.MBCOM-01(19K), FR.OVH-01(0B), FR.OVH-02(0B)

---

**2026-04-18T21:59:40 | Алексей Микоянов**
Hwid ограничивает, так сказать, количество provider-facing устройств, но не конечных устройств (коих за роутером может быть великое множество). А так - запретил раздавать с роутеров, прикольно же. Ну, как запрет тетеринга на мобилке по TTL. Дешево и сердито.  Работы на 3 минуты, а шекели - текут исправно.

---

