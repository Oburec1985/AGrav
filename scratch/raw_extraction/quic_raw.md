# Raw Extraction: quic

**2026-01-01T13:05:33 | Bullet for my valentine Poison**
🎄Всех с Новым годом!🔥 Zapret2. Для телевизоров LG, Samsung и т.д. Попробуйте такой вариант: 
Создайте доп. конфиг к основному Youtube.(Настройки на скринах)
Потом нажать на blobs и выбрать blob_quic_initial_www_google_com Сохранить, применить и перезапустить Zapret2

---

**2026-01-01T13:46:44 | Bullet for my valentine Poison**
opt/zapret2/files/fake/quic_3.bin --lua-desync=fake:blob=quic_3  ты это имел ввиду?

---

**2026-01-01T13:56:13 | Routerich**
давай я 1 разъ поясню, а при похожих вопросах мут на подумать дам. есть основной инстанс, тот, которому ты пишешь стратегии, он помимо собственной работы поднимает скрипты, отдельными инстансами. они ничего не знают о том, что и как ты включаешь или отключаешь, они нюхают трафик на наличие пейлоад и сравнивают со своей предустановкой. opt/zapret2/files/fake/quic_3.bin вот это инициирует блоб для квика(включает его)

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

**2026-01-06T22:29:55 | Dmitrii Burenin**
С приложением YouTube на WebOS еще куда запутаннее: там загрузка интерфейса идет по протоколу HTTPS (TCP порт 443), а видео протоколу QUIC (UDP порт 443). Но в случае, если подключение по QUIC не доступно, тогда приложения, что на Android устройствах, что WebOS переходят на протокол HTTPS. Так чтобы на телевизоре и телефоне YouTube не тормозил при работе с TPWS, необходимо блокировать трафик UDP на порт 443, для того, чтобы заставить приложения подключатся по протоколу HTTPS. Но это не решит проблему с поломкой загрузки интерфейса приложения на WebOS (Android TV) при работе с TPWS.
(c)

---

**2026-01-06T22:41:10 | Vasa**
всё верно. quick надо блочить

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

**2026-01-08T19:13:06 | Vasa**
ты quick обрезал исходящий ?

---

**2026-01-08T21:18:14 | Umka**
Может кто имел дело с xpenology  как обмануть систему quickconnect (не работает так как перед роутеричем ещё модем) 
Либо как выплюнуть через роутерич ip  нас сервака во внешку безопасно?

---

**2026-01-10T20:15:54 | L_E_G_I_O_N**
Инструкция по однокнопочному подбору стратегии для youtubeUnblock(Выражаем благодарность @Az098yosflasd7tow4).

В терминал скопировать
sh <(wget -qO- "https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/uttoobe/You_Tu_be!")
и нажать ввод.

Будет выведен список доступных стратегий:
Выберите стратегию:

1 - Стратегия по умолчанию (из коробки)
2 - Стратегия pastseq - Disable Fake SNI
3 - Стратегия pastseq - Disable Fake SNI+QUIC DROP
4 - Стратегия randseq - fake sni seq len=5, fragmentation strategy=ip, seg2delay=3
5 - Стратегия tcp_check - fake_sni_type=random, seg2delay=3, udp_filter_quic=all

0 - Выход
>

Введите число, нажмите ввод, скрипт перенастроит youtubeUnblock, остановит и выключит запрет, также выключит в подкопе "Списки сообщества - YouTube" чтобы они не мешали работе youtubeUnblock.

Как проверять.
Выбрали стратегию, нажали ввод, дождались окончания работы скрипта, открыли youtube.com, запустили ролик. Если воспроизведение не запустится, попробуйте открыть ещё пару роликов. При неудаче перезапустите скрипт в терминале, выберите следующую стратегию и вновь проверьте работу youtube.com минимум на паре ДРУГИХ роликов. И так далее.

То есть при выборе новой стратегии ВСЕГДА запускать на воспроизведение те видеоролики, которые вы не запускали ранее.

---

**2026-01-11T11:18:34 | Vasa**
ну дурилки ДПИ могут где то работать, где то не работать или работать плохо...

так что пользуйтесь впн

для теста можете - заблокировать quick в роутере
отключить ipv6

---

**2026-01-11T11:20:15 | Artamonich92**
Это было сделано сразу после скрипта 5.Касаемо Ipv6. (Через службу в автозапуске).
А вот что касается quic- так он после применения скрипта по дефолту вырублен (2 правила на исходящий трафик сделаны на 443 и 80 порт udp сделаны).

---

**2026-01-11T19:46:33 | Serj Shu**
Тогда гвоздями...
#!/bin/sh

# === НАСТРОЙКИ ===
DOMAIN1="tv.com"
DOMAIN2="firmware.tv.com"

# === DNS BLOCK ===
uci add_list dhcp.@dnsmasq[0].address="/$DOMAIN1/0.0.0.0"
uci add_list dhcp.@dnsmasq[0].address="/$DOMAIN2/0.0.0.0"

uci commit dhcp
/etc/init.d/dnsmasq restart

# === BLOCK QUIC (UDP 443) ===
iptables -C FORWARD -p udp --dport 443 -j DROP 2>/dev/null || \
iptables -A FORWARD -p udp --dport 443 -j DROP

exit 0


Пишем скрипт...
Дальше chmod +x block_tv.sh

Запускаем ... Проверяем. В секциях domain 1, и domain 2, вставляем домены телевизора

---

**2026-01-11T21:59:04 | Routerich**
Это блокировка протокола Quic для корректно работы YouTube

---

**2026-01-11T21:59:11 | Routerich**
Quic трафик внутри локалки блочит, для лучше работы дурилок для тв. Давно уже

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

**2026-01-16T12:06:36 | Юрий Теленков**
а сама стратегия Running with flags: --queue-num=537 --threads=1 --packet-mark=32768 --silent --tls=disabled --sni-domains=<trie of 157 vertexes> --sni-detection=parse --synfake=0 --udp-filter-quic=disabled --udp-stun-filter --fbegin --tls=enabled --frag=tcp --frag-sni-reverse=1 --frag-sni-faked=0 --frag-middle-sni=1 --frag-sni-pos=1 --fk-winsize=0 --fake-sni=1 --fake-sni-seq-len=1 --fake-sni-type=default --faking-strategy=pastseq --fake-seq-offset=10000 --seg2delay=0 --sni-domains=<trie of 29 vertexes> --sni-detection=parse --synfake=0 --udp-filter-quic=disabled --fend --fbegin --tls=enabled --frag=none --frag-sni-reverse=0 --frag-sni-faked=0 --frag-middle-sni=0 --frag-sni-pos=1 --fk-winsize=0 --fake-sni=1 --fake-sni-seq-len=1 --fake-sni-type=default --faking-strategy=tcp_check --seg2delay=0 --sni-domains=<trie of 418 vertexes> --sni-detection=parse --synfake=0 --udp-filter-quic=all --udp-mode=fake --udp-fake-seq-len=6 --udp-faking-strategy=none --fend

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

**2026-01-16T23:28:44 | Святос**
https://dns.geohide.ru:444/dns-query
DNS-over-TLS:
dns.geohide.ru
или
tls://dns.geohide.ru
DNS-over-QUIC:
quic://dns.geohide.ru

---

**2026-01-17T00:53:02 | Андрей ☕️**
config section                                                                       option name 'YouTube'                                                        option enabled '1'                                                           option tls_enabled '1'                                                       option fake_sni '1'                                                          option faking_strategy 'tcp_check'                                           option fake_sni_seq_len '1'                                                  option fake_sni_type 'random'                                                option frag 'tcp'                                                            option frag_sni_reverse '1'                                                  option frag_sni_faked '0'                                                    option frag_middle_sni '1'                                                   option frag_sni_pos '1'                                                      option seg2delay '3'                                                         option fk_winsize '0'                                                        option synfake '0'                                                           option sni_detection 'parse'                                                 option all_domains '0'                                                       option quic_drop '0'                                                         option udp_mode 'fake'                                                       option udp_fake_seq_len '6'                                                  option udp_fake_len '64'                                                     option udp_filter_quic 'all'                                                 option udp_faking_strategy 'none'                                            option udp_stun_filter '0'                                                   list sni_domains 'googlevideo.com'                                           list sni_domains 'youtubei.googleapis.com'                                   list sni_domains 'ytimg.com'                                                 list sni_domains 'yt3.ggpht.com'                                             list sni_domains 'yt4.ggpht.com'                                             list sni_domains 'youtube.com'                                               list sni_domains 'youtubeembeddedplayer.googleapis.com'                      list sni_domains 'ytimg.l.google.com'                                        list sni_domains 'jnn-pa.googleapis.com'                                     list sni_domains 'youtube-nocookie.com'                                      list sni_domains 'youtube-ui.l.google.com'                                   list sni_domains 'yt-video-upload.l.google.com'                              list sni_domains 'wide-youtube.l.google.com'                                 list sni_domains 'youtu.be'                                                  list sni_domains 'youtube.googleapis.com'                                    list sni_domains 'yt.be'                                                     list sni_domains 'withyoutube.com'                                           list sni_domains 'youtubeeducation.com'                                      list sni_domains 'youtubefanfest.com'                                        list sni_domains 'youtubegaming.com'                                         list sni_domains 'youtubekids.com'                                           list sni_domains 'youtubemobilesupport.com'

---

**2026-01-17T10:50:16 | Виталий Беляков**
запустил скрипт со стратегией, сработал второй вариант. пока ютуб летает и на windows и на ios. буду дальше наблюдать

Инструкция по однокнопочному подбору стратегии для youtubeUnblock(Выражаем благодарность @Az098yosflasd7tow4).

В терминал скопировать
sh <(wget -qO- "https://raw.githubusercontent.com/kkkkCampbell/trash/refs/heads/uttoobe/You_Tu_be!")
и нажать ввод.

Будет выведен список доступных стратегий:
Выберите стратегию:

1 - Стратегия по умолчанию (из коробки)
2 - Стратегия pastseq - Disable Fake SNI
3 - Стратегия pastseq - Disable Fake SNI+QUIC DROP
4 - Стратегия randseq - fake sni seq len=5, fragmentation strategy=ip, seg2delay=3
5 - Стратегия tcp_check - fake_sni_type=random, seg2delay=3, udp_filter_quic=all

0 - Выход
>

Введите число, нажмите ввод, скрипт перенастроит youtubeUnblock, остановит и выключит запрет, также выключит в подкопе "Списки сообщества - YouTube" чтобы они не мешали работе youtubeUnblock.

Как проверять.
Выбрали стратегию, нажали ввод, дождались окончания работы скрипта, открыли youtube.com, запустили ролик. Если воспроизведение не запустится, попробуйте открыть ещё пару роликов. При неудаче перезапустите скрипт в терминале, выберите следующую стратегию и вновь проверьте работу youtube.com минимум на паре ДРУГИХ роликов. И так далее.

То есть при выборе новой стратегии ВСЕГДА запускать на воспроизведение те видеоролики, которые вы не запускали ранее.

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

**2026-01-20T21:51:01 | Routerich**
кстати, не относится к теме, но тут чище всего. из-за того, что варп маскируется под quic, у zapret2 каменеет пониже живота и он начинает трогать handshake из-за чего ломается варп. выхода пока знаю два:
удалить quic.sh скрипт
удалить I1 параметр и обмазаться wg4all.sh скриптом из оригинальной репы запрет2

---

**2026-01-21T21:45:11 | Роман**
сейчас такой

# Strategy default

--filter-tcp=80 
--filter-l7=http 
--hostlist=<HOSTLIST>
--out-range=-s34228 
--payload=http_req 
--lua-desync=fake:blob=http:tcp_md5 
--lua-desync=multisplit:pos=2

--new
--filter-tcp=443
--filter-l7=tls
--hostlist=<HOSTLIST>
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=fake:blob=tls_clienthello:tcp_md5
--lua-desync=multisplit:pos=midsld

--new
--filter-udp=443
--filter-l7=quic <HOSTLIST_NOAUTO>
--payload=quic_initial
--lua-desync=fake:blob=fake_default_quic:repeats=6

---

**2026-01-22T01:12:41 | Kiss_My_Axe**
А, ну и кастрированная по горло прошивка радует. Захотел синкфолдер установить для автобэкапа полезного на ноут, а шиш тебе, некоторые модули из прошивки вырезаны и синк из-за этого работать отказывается. То же и с tvQuickActions, сама прога работает, но функционал урезан из-за китайских пыток над прошивкой.

---

**2026-01-23T02:23:49 | Kiss_My_Axe**
Походу клиент ютуба для андроеда крепко сел на QUIC и, если quic не алёкает, то эта зараза будет секунд под 50 тупить перед запуском видео по tcp.

---

**2026-01-23T02:40:24 | Kiss_My_Axe**
Дропнул QUIC в ZB и клиент ютуба на андроеде заявил, что интернета у тя нет, иди сеть настраивай.
Приехали...

---

**2026-01-23T11:26:55 | Юрий**
Попробуй в настройках ревансенда отключить подмену потоковых данных. Также попробуй вкл или наоборот откл QUIC.

---

**2026-01-23T11:37:20 | AleXXXey**
крч, перетыкнул туда-обратно подмену и quic - заработало) 
спасибо за рабочий метод)👍

я подозревал, что у реванседа какой-то конфликт в паре с запретом2. Видимо, ревансед тоже пытается обходить ограничения.

---

**2026-01-23T13:44:56 | Kiss_My_Axe**
Что делать с QUIC?
Ютубей своими клиентами по квику прёт уже как по тракту. Нет квика? Жди загрузки видео до утра.
Блок тоже не помогает, клиенту похрен.
Пикапдроид показывает стену квик-запросов со статусом "Ошибка", но клиент на тцп переходит краааайне неохотно.

---

**2026-01-23T14:12:37 | AleXXXey**
Галя, у нас отмена.

Спустя пару часов снова отрыгнул ют ревансед. Передёргивание подмены и quic не помогает.

Чё ж этому реванседу надо🤨

---

**2026-01-23T20:22:34 | Kiss_My_Axe**
Дык вродеж понятно всё.
Ставим пикапдроид, натравливаем на юклиента, запускаем юклиента, стартуем видео.
Получаем чорни икран.
Ждём секунд 30 до набора статистики и идём в пикапдроид.
Видим там стену из попыток по QUIC 443 добраться до видеохостинга трубы, типа таких адресов
https://rr2---sn-385ou-8v1l.googlevideo.com
Так же видим, что все попытки в статусе "Ошибка", потому что квик на роутере заблокирован.
Ждём минутки три-пять, видео не запускается.
Вывод - на TCP этот урод не перейдёт никогда.

Ну и остаётся только квн, получается, или альтернативный клиент трубы, с которыми труба ща воют как с врагами Родины.

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

**2026-01-25T20:44:42 | Igor Zorin**
Народ, кто-нибудь пользуется youtubeUnblock? Знаю, что для Zapret есть скрипт подбора стратегий, а есть ли подобное под youtubeUnblock? Интересует настройка протокола QUIC, который нужен для просмотра через PotPlayer и скачивания через yt-dlp.

---

**2026-01-25T21:01:08 | Igor Zorin**
Супер! На второй стратегии QUIC заработал.

---

**2026-01-27T01:02:47 | Vasa**
И там по протоколу quick всё…

Досвидания…

---

**2026-01-27T11:30:53 | Routerich**
какой именно варп? 1,5 с I1?  его может запрет ломать потому что амнезия мимикрирует под quick

---

**2026-01-27T11:32:11 | Routerich**
1.5 смотрите кастомный скрипт в запрете, который  quic он ломает

---

**2026-01-27T11:43:58 | Routerich**
маскировка под quick

---

**2026-01-27T15:02:14 | Routerich**
quic я в курсе

---

**2026-01-27T15:04:15 | Routerich**
там есть надежда что последний фикс в детекте quic поможет, но это надо ручками подсовывать биарник, у нас сборщика пока нет

---

**2026-01-27T16:55:02 | Artem**
Может кому пригодится, скрипт №5, далее отключение запрета, ставим luci youtubeunblock, после тестов помог такой конфиг, ютуб работает на всех устройствах и тв. 
Так же создав новую секцию можно завести инст. Убрать meta из подкоп, в ютуб анблок создаем новую секцию+quic drop галочка. Работает быстрее чем через подкоп

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

**2026-01-29T09:35:31 | Routerich**
custom script удалить quick4all.sh

---

**2026-01-29T10:59:34 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.1-r80:
  Новое:
  - Catch-all секция — первая секция без доменов становится финальным outbound для всего трафика. Секции после catch-all полностью игнорируются
  - Проверка FakeIP клиента через домен fakeip-check.zeroblock.best

  Рефакторинг:
  - Полная переработка auto fallback. Теперь через mixed_port первой активной секции при недоступности напрямую

  Исправления FakeIP:
  - FakeIP клиент теперь работает(но нужны тесты)
  - proxy_router_traffic проксирует весь OUTPUT для catch-all секций
  - Трафик роутера для FakeIP маршрутизируется независимо от proxy_router_traffic

  Исправления LuCI:
  - Восстановление значений при ошибке валидации в модальном окне(ранее настройки сохранялись, но окно не закрывалось)
  - Скрыта опция disable_fakeip для BLOCK секций
  - BLOCK секции исключены из выбора прокси для загрузки для auto fallback
  - Улучшены описания опций
  - Исправлено некорректное поведение disable quic
#ZeroBlock

---

**2026-01-29T11:56:27 | Routerich**
а у тебя свой авг? зероблочный? quic4all есть же в запрете? I1 есть параметр в awg?

---

**2026-01-29T17:54:38 | Vasa**
покажите скрином плз дроп quick для ВРТхи.. как там верно

---

**2026-01-29T17:59:32 | Routerich**
https://lsetc.ru/otkljuchit-quic-v-lokalnoj-seti-na-openwrt/ это?

---

**2026-01-29T20:12:23 | Yury Kuzmenko**
и на другом адресе где нет скриптов на QUIC умер AWG

---

**2026-01-29T23:07:34 | Kiss_My_Axe**
/opt/zapret2/init.d/openwrt/custom.d/50-quic4all.sh

---

**2026-01-30T01:48:12 | Routerich**
Службы - запрет2 - скрипты - удалить скрипт с названием quic4all - применить - перезапустить службу - В Система - планировщик удалите строку с ruantiblock update - Далее сеть - интерфейсы - перезапустить awg10 и проверять

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

**2026-01-31T23:39:55 | ユージーン**
так она есть, только как её припаять, другой вопрос...
--filter-udp=1024-65535
--out-range=-d2
--lua-desync=fake:blob=quic_google

---

**2026-01-31T23:41:24 | Роман**
--filter-udp=88,500,1024-65535
--dpi-desync=fake
--dpi-desync-cutoff=d2
--dpi-desync-any-protocol=1
--dpi-desync-fake-unknown-udp=/opt/zapret/files/fake/quic_initial_www_google_com.bin

Жесть стратегия, ломает трафик на всех портах с 1024 по 65535.

---

**2026-01-31T23:43:55 | Routerich**
--filter-udp=88,500,1024-65535 \
--out-range=-d2 \
--payload=all \
--lua-desync=fake:blob=blob_quic_initial_www_google_com

---

**2026-02-01T00:13:43 | ユージーン**
ххммм
странно 
--new
--name=game
--filter-udp=443
--filter-l3=ipv4
--out-range=-d2
--payload=all
--lua-desync=fake:blob=blob_quic_initial_www_google_com
порты не прописываются

---

**2026-02-01T00:50:35 | ユージーン**
сейчас прописывает, но на сервера не пускает...
--new
--name=game
--filter-udp=1024-65535
--filter-l3=ipv4
--out-range=-d2
--payload=all
--lua-desync=fake:blob=blob_quic_initial_www_google_com
Спасибо, буду дальше копать ))

---

**2026-02-01T12:04:58 | Роман**
Скрипт quic4all убрали? Или баг?

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

**2026-02-01T13:00:32 | ⓐⓥ**
Само собой это было сделано. У меня в youtubeUnblock все торренты добавлены и Blockchek2 на это сразу бы выругался. В стоковой конфигурации (там где 14 стратегий) домены открываются, но сильно подлагивают. Для youtubeUnblock сработала стратегия 2, в uci выглядит так:
youtubeUnblock.@section[2].name='YouTube'
youtubeUnblock.@section[2].enabled='1'
youtubeUnblock.@section[2].tls_enabled='1'
youtubeUnblock.@section[2].fake_sni='0'
youtubeUnblock.@section[2].faking_strategy='pastseq'
youtubeUnblock.@section[2].fake_sni_seq_len='1'
youtubeUnblock.@section[2].fake_sni_type='default'
youtubeUnblock.@section[2].frag='tcp'
youtubeUnblock.@section[2].frag_sni_reverse='1'
youtubeUnblock.@section[2].frag_sni_faked='0'
youtubeUnblock.@section[2].frag_middle_sni='1'
youtubeUnblock.@section[2].frag_sni_pos='1'
youtubeUnblock.@section[2].seg2delay='0'
youtubeUnblock.@section[2].fk_winsize='0'
youtubeUnblock.@section[2].synfake='0'
youtubeUnblock.@section[2].sni_detection='parse'
youtubeUnblock.@section[2].all_domains='0'
youtubeUnblock.@section[2].quic_drop='0'
youtubeUnblock.@section[2].udp_mode='fake'
youtubeUnblock.@section[2].udp_fake_seq_len='6'
youtubeUnblock.@section[2].udp_fake_len='64'
youtubeUnblock.@section[2].udp_filter_quic='disabled'
youtubeUnblock.@section[2].udp_faking_strategy='none'
Вот думаю это как-то в параметры Запрета транспонировать.

---

**2026-02-02T06:07:14 | Wenzel Perminov**
можно сюда добавить хост лист под ютуб, а то второй способ отсюда у меня не заработал, а smartube без quic не работает, не грузит . Если да как его прописать
https://t.me/routerich/394153/447428

---

**2026-02-02T06:52:16 | Yury Kuzmenko**
А марка запрета и зб совпадает? Включен ли скрипт на quic?

---

**2026-02-02T06:53:07 | Камиль**
Совпадала, quic через запрет не запрещал

---

**2026-02-02T07:57:14 | Wenzel Perminov**
Переделать скрипт с all quic на host_list YouTube quic, без скрипта smartube не работает, видео не грузится

---

**2026-02-02T08:08:19 | Routerich**
нет, там поиск по паттерну, нужен точечный quic делайте свою стратегию

---

**2026-02-02T18:52:54 | Serj Shu**
Попробуйте отключить QUIC...

---

**2026-02-02T23:58:58 | Kiss_My_Axe**
Сам авг работает, это показывает тест доступа к ютуб. Во время этого теста все мешающие сервисы остановлены.
Их два, зероблок и запрет2. В запрете мешает скрипт quick4all (но его после первого прогона не стало), в зероблок, возможно, список cloudflare.

---

**2026-02-04T15:09:38 | Slava Zverev**
Добрый день!
Может кто скинуть скрипт дефолтный 50-quic4all.sh, либо подсказать где оно может быть? 
После моих вчерашних манипуляций он пропал, хочу восстановить

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

**2026-02-05T21:31:04 | Kiss_My_Axe**
Удалит quick4all скрипт из запрет2, который в новых дистрибутивах искаропки отсутствует.

---

**2026-02-08T21:26:41 | Kiss_My_Axe**
Тогда запрет2.
Вообще надо бы в фаерволле ещё обрубить UDP на порт 443 в правиле "из LAN в любое место".
А то офклиенты ютуба на quic садятся и сидят до посинячки, а квик уже давно у нас похоронен и камень поставлен.
https://lsetc.ru/otkljuchit-quic-v-lokalnoj-seti-na-openwrt/

---

**2026-02-09T11:14:47 | Oleg Isaev**
Добрый день! Вчера столкнулся с проблемой - при попытке открыть сайты
https://www.androidpolice.com/
https://www.xda-developers.com/
https://xdaforums.com/
в разных браузерах отображается ошибка "ERR_HTTP2_PROTOCOL_ERROR"
Причём, если я открываю их через впн, открываются нормально. Напрямую - никак. Пробовал со смартфона через мобильную сеть - такая же ситуация, напрямую не идут.
Погуглил проблему - рекомендуют проверить время на устройстве, обновить ПО, отключить QUIC, использовать режим инкогнито - ничего не помогло.
Спросил чатгпт - рекомендовал понизить MTU до 1400, но тоже мимо.
Вроде бы ресурсы эти ни в каких списках блокировок не присутствуют, и должны открываться без "костылей". Полагаю, помимо этих 3 сайтов, может быть гораздо больше, а то и все на HTTP 2 версии.
Провайдеры проводной - Ростелеком Москва, мобильный - Мегафон Москва. На работе проводной МГТС - то же самое.
Может, кто может у себя проверить, или сталкивался с таким, и знает, как пофиксить?
Не хочется все забугорные сайты через впн гнать.

---

**2026-02-09T22:44:16 | Калинин**
Если у кого-то не работает скачивание музыки в geometry dash или проблемы с cloudflare не решились, вот список доменов которые мне помогли:

cloudflare-ech.com
encryptedsni.com
cloudflareaccess.com
cloudflareapps.com
cloudflarebolt.com
cloudflareclient.com
cloudflareinsights.com
cloudflareok.com
cloudflarepartners.com
cloudflareportal.com
cloudflarepreview.com
cloudflareresolve.com
cloudflaressl.com
cloudflarestatus.com
cloudflarestorage.com
cloudflarestream.com
cloudflaretest.com
dis.gd
frankerfacez.com
ffzap.com
betterttv.net
7tv.app
7tv.io
newgrounds.com
ungrounded.net
ns1.ungrounded.net
ns2.ungrounded.net
mcreator.net
www.newgrounds.com
gatortots.newgrounds.com
system17.ungrounded.net
system16.ungrounded.net
ns5009982.ip-15-235-14.net
system15.ungrounded.net
aspmx.l.google.com
aspmx2.googlemail.com
aspmx3.googlemail.com
proxy.ungrounded.net
ngfiles.com
audio.ngfiles.com
js.ngfiles.com
css.ngfiles.con
aicon.ngfiles.com
img.ngfiles.com
uimg.ngfiles.com
ngcdn.com
signin.aws.amazon.com
cloudfront.net
s3.amazonaws.com
awsstatic.com
console.aws.a2z.com
amazonaws.com
awsapps.com
sso.amazonaws.com
cloudfront.net
deadbydaylight.com
deadbydaylight.fandom.com
argotunnel.com
cfargotunnel.com
cfl.re
cloudflare-dns.com
cloudflare-ech.com
cloudflare-esni.com
cloudflare-gateway.com
cloudflare-quic.com
cloudflare.com
cloudflare.net
cloudflare.tv
cloudflareaccess.com
cloudflareapps.com
cloudflarebolt.com
cloudflareclient.com
cloudflareinsights.com
cloudflareok.com
cloudflarepartners.com
cloudflareportal.com
cloudflarepreview.com
cloudflareresolve.com
cloudflaressl.com
cloudflarestatus.com
cloudflarestorage.com
cloudflarestream.com
cloudflaretest.com
cloudflarewarp.com
every1dns.net
isbgpsafeyet.com
one.one.one.one
one.one.one
pacloudflare.com
pages.dev
trycloudflare.com
videodelivery.net
warp.plus
workers.dev
7tv.app
7tv.io
newgrounds.com
ungrounded.net
ns1.ungrounded.net
ns2.ungrounded.net
mcreator.net
www.newgrounds.com
gatortots.newgrounds.com
system17.ungrounded.net
system16.ungrounded.net
ns5009982.ip-15-235-14.net
system15.ungrounded.net
aspmx.l.google.com
aspmx2.googlemail.com
aspmx3.googlemail.com
proxy.ungrounded.net
ngfiles.com
audio.ngfiles.com
aicon.ngfiles.com
ngfiles-proxy.b-cdn.net
www.robtopgames.org
boomlings.com

---

**2026-02-12T13:33:49 | Routerich**
quick drop?

---

**2026-02-12T18:26:55 | Routerich**
нет обрезанный режим это поиск по 5 стратегиям, а то яно он находит 1 и успокаивается это quick. так что то, что он нашёл вам стратегию подходящую ко всему это ошибка выжившего

---

**2026-02-12T20:05:51 | Роман**
7. Поддерживаемые протоколы
7.1 VLESS
Современный протокол с минимальным оверхедом и поддержкой Reality.
Формат URL:
vless://uuid@host:port?type=tcp&security=reality&pbk=key&fp=chrome
&sni=domain&sid=id&flow=xtls-rprx-vision#Name
7.2 VMess
Протокол V2Ray с шифрованием.
Формат URL:
vmess://base64(json)
JSON формат:
{
"v": "2",
"ps": "Name",
"add": "server.com",
"port": "443",
"id": "uuid",
"aid": "0",
"scy": "auto",
"net": "ws",
"type": "none",
"host": "example.com",
"path": "/path",
"tls": "tls",
"sni": "example.com"
}
7.3 Trojan
Протокол с маскировкой под HTTPS.
Формат URL:
trojan://password@host:port?sni=example.com&allowInsecure=0#Name
7.4 Shadowsocks
Классический протокол шифрования.
Формат URL:
ss://method:password@host:port#Name
Методы шифрования: - aes-128-gcm, aes-256-gcm - chacha20-ietf-poly1305 - 2022-blake3-aes128-gcm, 2022-blake3-aes-256-gcm
Поддержка плагинов: да (через параметр plugin=name;opts в URL)
21
7.5 Hysteria2
Высокопроизводительный протокол на базе QUIC.
Формат URL:
hysteria2://password@host:port?sni=example.com&insecure=0#Name
7.6 SOCKS4/5
Классический SOCKS прокси.
Формат URL:
socks5://user:password@host:port#Name
socks4://host:port#Name
7.7 HTTP/HTTPS
HTTP прокси с опциональной авторизацией.
Формат URL:
http://user:password@host:port#Name
https://user:password@host:port#Name
7.8 Xray-core транспорты
VLESS/VMess с транспортами xhttp и mKCP маршрутизируются через xray-core с SOCKS5-
мостом.
xhttp транспорт:
vless://uuid@host:port?type=xhttp&path=/path&security=tls#Name
mKCP транспорт:
vless://uuid@host:port?type=kcp&seed=seed&headerType=wireguard#Name

---

**2026-02-12T20:37:42 | Vasa**
Есть сложность.

Есть сокс-прокси разные. Надо чтоб через них работал webRTC и quick

а он не хочет, в синг боксе настроил их (

---

**2026-02-14T13:35:55 | Vasa**
мне надо проверить теорию с пассволом..

короче суть такая - есть резидентные прокси, socks5

я их завел в синг-бокс, выделил отдельный вифи и подсеть под это

проблема такая - не ходит через него webRTC и QUICK

а в антидетект браузере когда эти прокси юзаешь - всё ходит....

---

**2026-02-18T20:13:52 | Bullet for my valentine Poison**
--payload=tls_client_hello
--lua-desync=fake:blob=blob_tls_clienthello_google:badseq:badseq_incr=1000000:repeats=6

--payload=quic_initial
--lua-desync=fake:blob=blob_quic_initial_google:anyproto:autottl=2:repeats=9:cutoff=n2
думаешь это верно?

---

**2026-02-19T02:21:44 | Bullet for my valentine Poison**
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=circular:fails=2:time=60
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:repeat=3:tls_mod=sni=www.google.com:strategy=1
--lua-desync=multisplit:pos=2:strategy=1
--lua-desync=fake:blob=blob_tls_clienthello_vk_com_kyber:repeat=4:tls_mod=sni=vk.com:strategy=2
--lua-desync=multisplit:pos=1:strategy=2
--lua-desync=fake:blob=blob_tls_clienthello_yandex_com:tcp_ts=-600000:repeat=5:tls_mod=sni=yandex.com:strategy=3
--lua-desync=multisplit:pos=1,midsld:strategy=3
--lua-desync=fake:blob=blob_quic_initial_www_google_com:repeat=3:strategy=4
--lua-desync=multisplit:pos=1,midsld:seqovl=1220:strategy=4
--lua-desync=fake:blob=blob_tls_clienthello_vk_com:tcp_seq=1000000:tcp_ack=-66000:badsum:repeat=4:tls_mod=sni=vk.com:strategy=5
--lua-desync=multisplit:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1:strategy=5
--lua-desync=fake:blob=blob_tls_clienthello_gosuslugi_ru:badsum:repeat=2:tls_mod=sni=gosuslugi.ru:strategy=6
--lua-desync=multidisorder:pos=2:strategy=6
--lua-desync=fake:blob=blob_tls_clienthello_ticket_rzd_ru:tcp_seq=1000000:repeat=3:tls_mod=sni=ticket.rzd.ru:strategy=7
--lua-desync=multidisorder:pos=1:strategy=7
--lua-desync=fake:blob=blob_tls_clienthello_www_4pda_to:tcp_ts=-1000:repeat=3:tls_mod=sni=www.4pda.to:strategy=8
--lua-desync=multidisorder:pos=sniext+1:strategy=8
--lua-desync=fake:blob=blob_tls_clienthello_www_max_ru:badsum:tcp_seq=-3000:repeat=2:tls_mod=sni=www.max.ru:strategy=9
--lua-desync=multidisorder:pos=sniext+4:strategy=9
--lua-desync=fake:blob=blob_tls_clienthello_sberbank_ru:tcp_ack=-66000:repeat=2:tls_mod=sni=sberbank.ru:strategy=10:final

---

**2026-02-19T09:10:20 | Lelik**
Кто напомнит как правлиьно писать для udp пакетов?
--out-range=-s34228 \
--payload=tls_client_hello \
--in-range=-s5556 --lua-desync=circular:fails=2:time=60 \
--in-range=x \
--lua-desync=fake:blob=quic_google:repeats=7

---

**2026-02-19T09:18:26 | Lelik**
Вот так вроде правильно будет?
--lua-desync=circular:fails=2:time=60 \
--lua-desync=fake:blob=quic_google:repeats=7

---

**2026-02-19T09:32:27 | Lelik**
--lua-desync=circular:fails=2:time=60 \
--lua-desync=fake:blob=quic_google:repeats=7 \
--lua-desync=fake:blob=quic_google:repeats=6
ну вот так, напярмую укажу что у меня много стратегий

---

**2026-02-19T14:24:19 | Lelik**
--lua-desync=circular:fails=2:maxtime=60
--lua-desync=circular:fails=2:time=60 \
--lua-desync=fake:blob=quic_google:repeats=7 \
--lua-desync=fake:blob=quic_google:repeats=6

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

**2026-02-21T23:37:28 | Rom@n**
А это я правильно понял Рутрекер хочет что бы я QUIC отключил? Но на предыдущей версии ZB и так работало.

---

**2026-02-25T13:33:38 | Anatoly К**
Так же давно уже на  LG. Практически: для LG webOS нельзя просто «задушить» QUIC, как на Android/PC — там клиент уходит на TCP, а webOS‑клиент во многих кейсах вообще не работает без нормального UDP 443

---

**2026-02-25T14:52:45 | Routerich**
отключите quic в анблоке

---

**2026-02-26T17:18:41 | ㅤㅤ**
Решаю вопрос удаленно, чуть позже попробую и отпишусь. 

На данный момент проверили отключение iCloud Private Relay (Частный узел) и Limit IP Address Tracking

Также нужно перепроверить работает ли там ZeroBlock с IPv6 так как Apple и LG любят туда лезть. Попробую его наглухо отключить.

Гляну "частный DNS" и QUIC в Chrome, в Safari «Скрывать IP-адрес от трекеров».

---

**2026-02-27T15:59:40 | ㅤㅤ**
💻 Итак вопрос по работе обхода Youtube с ZeroBlock на устройствах Apple и телевизоре решился!

Apple MacBook Pro 16 MUW63
LG OLED65C9PLA
iPhone 15 Pro Max (iOS 26.2.1)

Устройства Apple очень любят ходить по IPv6. Устройства выходят в интернет со своими адресами игнорируя FakeIP,

ЧЕК-ЛИСТ:
- iCloud Private Relay: Выключен 
- Лимит трекинга IP (Limit IP Tracking): Отключен
- Частный адрес Wi-Fi (MAC-адрес): Установлен в значение «Выкл» или «Фиксированный».
- IPv6: Переведен в режим «Link-local only» или выключен

Google Chrome:
- Протокол QUIC: Отключен в chrome://flags 
- Безопасный DNS (DoH): Отключен в настройках Chrome

- Системный DNS: В настройках IP твоего роутера 192.168.1.1
- Очистка кэша: Выполнен сброс DNS-кэша через Терминал 

sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder

Само собой после каждой операции старайтесь перезапускать соединение. 

Выполнили⁉️ Зря потратили время. Потому что у вас все равно ничего не будет работать в итоге.

А теперь сносите останавливайте и отключайте ZeroBlock, убирайте его из автозагрузки, применяйте скрипт №5 и на ваших устройствах все заведется.

---

**2026-02-27T18:35:59 | Routerich**
Стратегию подбирайте, обновите приложение до последней версии, quic отключите в приложении

---

**2026-02-27T18:41:31 | K163R**
QUIC - отключил

обновить не получилось, лог в ошибках

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

**2026-03-03T18:01:03 | Routerich**
Обновить приложение, почистить кеш, отключить quic

---

**2026-03-04T16:17:46 | HiLLL**
Fresa, прибил гвоздями ru локу. Отключив quic в браузере.

---

**2026-03-04T21:31:42 | Artur A.**
война и мир. я правильно понимаю.что минимально необходимо и достаточно сделать это :вводим в Фильтр “igmp”, находим строку с пакетом igmpproxy и в ней нажимаем Установить, опять Установить во всплывающем окне, закрываем окно с логом установки.
 
8. Идём в Службы -> Терминал, вводим в терминале логин и пароль от вашего роутера (нажимая Enter после каждого ввода), затем вводим (или копируем/вставляем ПКМ) команду 
nano /etc/config/igmpproxy

Открывается содержимое этого файла в текстовом редакторе nano. В нём меняем строку
option network wan
на
option network br_wan_int

и ещё меняем строку
list altnet 192.168.1.0/24
на
list altnet 0.0.0.0/0

Для вставки из буфера обмена в нужное место нужно стрелочками на клавиатуре поместить курсор в место вставки и нажать ПКМ -> Вставить.
 
По окончании редактирования нажимаем Ctrl+O, затем Enter для подтверждения перезаписи, затем Ctrl+X для выхода. 

Если ограничить altnet отдельными IP, на каких-то каналах попадётся запрещённый IP и IPTV перестанет работать. А в логе роутера появится запись типа 
igmpproxy[4621]: The source address 78.107.196.36 for group 233.33.210.54, is not in any valid net for upstream VIF[0].
Маска 0.0.0.0/0 разрешает все IP источников мультикаста.

Включённый quickleave (по умолчанию включён) не оказал негативного эффекта в моих тестах при одновременной работе нескольких IPTV-приставок (старых, от Билайн).

9. Идём в Сеть -> Интерфейсы, во вкладку Устройства. Там должны быть два устройства типа Мост: br-lan и br-wan. В каждом из них нажимаем Настроить, переходим во вкладку Дополнительные опции устройства, и устанавливаем флажок Включить IGMP Snooping, затем нажимаем Сохранить.

---

**2026-03-04T23:05:16 | Святос**
# 5222 - TCP порт telegram, иногда используется вместо 443
# 2053,2083,2087,2096,8443 - Discord
TCP_PORTS=80,443,2053,2083,2087,2096,5222,8443
# 443 (UDP) - YouTube (QUIC), а также маскирующиеся прокси Telegram и Discord
# 590-600 - Telegram звонки исходящие
# 1400 - Telegram STUN звоннки исходящие
# 3478-3481, 5349 - STUN/TURN звонки Discord и мб где-то еще
# 19294-19344 - Discord Voice (основной рабочий диапазон для голоса и стримов "Go Live")
# 50000-65535 - Игровой диапазон (Dota 2, CS2, Valorant и др., а также резервные порты Discord)
UDP_PORTS=443,590:600,1400,3478:3481,5349,19294:19344,50000:65535

---

**2026-03-10T16:52:30 | D Ch**
Примечательно что стратегия из закрепа прекрасно работает из браузеров телефонов. Значит что-то с quick?

Потому как стандартное ютубное приложение на любом ролике - это всегда плюс 4 секунды

---

**2026-03-11T00:14:02 | Роман**
Вот почему имитация под почтовые протоколы — это «путь боли»:

1. Доступность портов (Белый список)
HTTPS — это единственный протокол, который разрешен везде.

В публичных Wi-Fi, корпоративных сетях или отелях порты почты (465, 587, 993) часто закрыты по умолчанию, чтобы предотвратить рассылку спама или утечку данных.

Если ты попытаешься поднять туннель через 993 порт в корпоративной сети, он, скорее всего, просто не заведется. Порт 443 не закроют никогда — иначе «интернет сломается».

2. Объём «стога сена» (Статистический анализ)
Главная задача обфускации — затеряться в толпе.

HTTPS — это огромный океан трафика. Через него гоняют видео, картинки, JSON, файлы, сокеты. Любая аномалия в поведении твоего протокола (например, странные тайминги или объем данных) легко списывается на «ну, это просто какой-то тяжелый веб-сервис».

SMTPS/IMAPS — это очень специфический трафик. Там есть понятные паттерны: клиент спросил, сервер ответил короткими строками. Если ты начнешь через «почтовый» порт качать 4K-видео с YouTube в течение двух часов, любая система DPI (Deep Packet Inspection) тут же поднимет тревогу: «Почтовый протокол так себя не ведет».

3. Инфраструктура и CDN
HTTPS дает тебе легальный «чит» — возможность использовать CDN (Cloudflare, Akamai и др.) или Fronting.

Ты можешь направить свой трафик на IP-адрес Cloudflare, и для провайдера это будет выглядеть как обычный запрос к легитимному сайту.

Провернуть такое с IMAPS гораздо сложнее и дороже, так как большинство бесплатных уровней CDN работают только с HTTP/HTTPS трафиком.

4. Проблема ALPN и TLS Fingerprinting
Современные системы анализа трафика смотрят не только на порт, но и на ALPN (Application-Layer Protocol Negotiation) внутри TLS-хендшейка.

Если твой софт имитирует IMAPS, он должен идеально повторять поведение почтового клиента (например, Outlook или Thunderbird) на уровне TLS-отпечатков (JA3/JA3S).

Сделать это для HTTPS проще, так как браузеров много и их поведение крайне разнообразно.

Бывают ли исключения?
На самом деле, имитация других протоколов существует, но она специфична:

DNS (порт 53): Используется для обхода авторизации в платных Wi-Fi сетях (медленно, но работает).

ICMP (пинг): Старый добрый метод «туннеля в пингах».

QUIC: Сейчас это модное направление, так как он работает поверх UDP и выглядит как новый стандарт веба, что дает еще больше гибкости.

Резюме: Идея с IMAPS рабочая, но она делает тебя «белой вороной». На фоне 1000 соединений по HTTPS твое одно соединение по 443 порту незаметно. На фоне 10 почтовых сессий твоя одна сессия, качающая гигабайты данных, выглядит как взлом или утечка.

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

**2026-03-14T11:19:56 | HiLLL**
@BWasilii слушай, хорошо что ты напомнил, яж сам с дури когда то включил quic и забыл. Он мне геоблок ломал. В итоге я его выключил, но уже не тестировал ТТ. Сейчас проверил, все ОК с геоблоком.

---

**2026-03-15T12:40:44 | ꧁ 𝓐𝓷𝓽𝓸𝓷 𝓑𝓮𝔃𝓴𝓪𝓹𝓾𝓼𝓽𝓲𝓷 ꧂**
Есть пара технических вопросов по ЗБ, в рамках самообразования:
1. Почему по умолчанию активирована опция "Отключить QUIC"? У меня один из outbound - socks5 с поддержкой udp, по идее Ютуб через QUIC должен бодрее гоняться в этом случае, разве нет? Как работает в целом эта опция? (При включенном "Отключить QUIC" не нашел в конфиге sing-box ничего, что могло бы быть добавлено этой опцией)
2. Относительно работы Fake IP - верно ли я понимаю, что нормально трафик будет перенаправляться только если на северной стороне удастся сниффингом получить домен, к которому идёт обращение? (Т.е. условный ncat domain.in.list.for.routing.com 1234 работать не будет)

---

**2026-03-15T13:22:27 | Nikita**
А если у меня awg свой сервак, 1 секция и отключен fake ip, в этом случае могу оставить quic работающим? И к чему это приведёт?

---

**2026-03-15T14:48:06 | Nikita**
так а зачем тогда в интерфейсе есть этот чекбокс, который можно снять, что приводит только к проблемам?
Точнее для какого use case нужно включение quic?

---

**2026-03-15T15:21:55 | Nikita**
Ты имеешь ввиду у тебя стоит чекбокс disable quic?
Так может тогда выпилить это из интерфейса, если нет никого способа эту проблему решить?

Поставил себе чекбокс disable quic обратно, посмотрел лог, сингбокс начал сыпать этим:
96  Sun Mar 15 15:20:21 2026  user  notice  sing-box:  [31mERROR [0m[0035] [ [38;5;130m2889874546 [0m 0ms] router: process DNS packet: drop connections by rule
97  Sun Mar 15 15:20:25 2026  user  notice  sing-box:  [31mERROR [0m[0040] [ [38;5;44m1894516252 [0m 0ms] router: process DNS packet: drop connections by rule
98  Sun Mar 15 15:20:30 2026  user  notice  sing-box:  [31mERROR [0m[0045] [ [38;5;148m354200708 [0m 0ms] router: process DNS packet: drop connections by rule
99  Sun Mar 15 15:20:33 2026  user  notice  sing-box:  [31mERROR [0m[0047] [ [38;5;81m1121918785 [0m 0ms] router: process DNS packet: drop connections by rule

Не понимаю про какой rule он говорит 😅

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

**2026-03-15T15:45:05 | Routerich**
ну либо ipv6 либо quic, ещё вариант запроса того что синг не хочет получать

---

**2026-03-15T16:05:07 | Nikita**
Да вроде бы ничего нет связанного с v6:
Это с пк:
PS C:\Users\Nikita> nslookup 2ip.ru
Server:  UnKnown
Address:  192.168.1.1

Non-authoritative answer:
Name:    2ip.ru
Address:  188.40.167.82

PS C:\Users\Nikita> nslookup google.com
Server:  UnKnown
Address:  192.168.1.1

Non-authoritative answer:
Name:    google.com
Addresses:  108.177.14.113
          108.177.14.102
          108.177.14.138
          108.177.14.139
          108.177.14.101
          108.177.14.100

Это с роутера:
root@RouteRich:~# nslookup ya.ru
Server:         100.100.100.100
Address:        100.100.100.100:53

Non-authoritative answer:
Name:   ya.ru
Address: 5.255.255.242
Name:   ya.ru
Address: 77.88.44.242
Name:   ya.ru
Address: 77.88.55.242

Non-authoritative answer:

root@RouteRich:~# nslookup google.com
Server:         100.100.100.100
Address:        100.100.100.100:53

Non-authoritative answer:
Name:   google.com
Address: 108.177.14.139
Name:   google.com
Address: 108.177.14.102
Name:   google.com
Address: 108.177.14.101
Name:   google.com
Address: 108.177.14.100
Name:   google.com
Address: 108.177.14.138
Name:   google.com
Address: 108.177.14.113

Non-authoritative answer:

root@RouteRich:~#

quic тоже отключен

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

**2026-03-16T12:54:40 | Yrii**
Mon Mar 16 12:52:34 2026 daemon.info youtubeUnblock[10767]: youtubeUnblock 1.3.0-1
Mon Mar 16 12:52:34 2026 daemon.info youtubeUnblock[10767]: Bypasses deep packet inspection systems that rely on SNI
Mon Mar 16 12:52:34 2026 daemon.info youtubeUnblock[10767]:
Mon Mar 16 12:52:34 2026 daemon.info youtubeUnblock[10767]: Running with flags: --queue-num=537 --threads=1 --packet-mark=32768 --silent --tls=enabled --frag=tcp --frag-sni-reverse=1 --frag-sni-faked=0 --frag-middle-sni=1 --frag-sni-pos=1 --fk-winsize=0 --fake-sni=1 --fake-sni-seq-len=1 --fake-sni-type=default --seg2delay=0 --faking-strategy=pastseq,  --sni-domains=<trie of 106 vertexes> --sni-detection=parse --synfake=0 --udp-filter-quic=disabled --fbegin --tls=disabled --sni-domains=<trie of 157 vertexes> --sni-detection=parse --synfake=0 --udp-filter-quic=disabled --udp-stun-filter --fend --fbegin --tls=enabled --frag=tcp --frag-sni-reverse=1 --frag-sni-faked=0 --frag-middle-sni=1 --frag-sni-pos=1 --fk-winsize=0 --fake-sni=1 --fake-sni-seq-len=1 --fake-sni-type=default --seg2delay=0 --faking-strategy=pastseq,  --sni-domains=<trie of 29 vertexes> --sni-detection=parse --synfake=0 --udp-filter-quic=disabled --fend
Mon Mar 16 12:52:34 2026 daemon.info youtubeUnblock[10767]: Queue 537 started

---

**2026-03-19T10:53:49 | Дмитрий**
Да я так и понял) В принципе доступ к Nas так то есть и через quickconnect, но хотелось всех запихнуть в сеть RR.😁

---

**2026-03-21T19:10:48 | HiLLL**
еще бывает фейкип ломает включенный безопасный днс в браузере, иногда включенный quic

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

**2026-03-22T09:20:32 | ВПН НА ТЕЛЕВИЗОР ФИЛИПС**
Сейчас ради интереса убрал на пк шлюз на линух, сделал такую страту:
--filter-udp=443 --hostlist="%LISTS%list-general.txt" --dpi-desync=fake --dpi-desync-repeats=1 --dpi-desync-fake-quic="%BIN%quic_initial_www_google_com.bin" --new ^
--filter-tcp=80,443 --hostlist="%LISTS%list-general.txt" --dpi-desync=fake --dpi-desync-fooling=ts --dpi-desync-fake-tls="%BIN%tls_clienthello_www_google_com.bin" --dpi-desync-repeats=1
И все работает идеально

---

**2026-03-22T14:12:25 | Wenzel Perminov**
сталкиваюсь с такой фигней уже не первый раз, Zapret2 сегодня обновил и Smarttube( все не использующие quic альтернативные клиенты так же) нормально буферит, а через пару дней станет буферить хуже  и смотреть станет невозможно. Такое поведение есть у Zapret2 и кажется раньше какая-то деградация есть у youtubeunblock. как с таким бороться настройками, так как стратегия работает, а буфер происходит реже чем надо

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

**2026-03-25T21:05:07 | Yury Kuzmenko**
А почему именно она? Я думал у нас quick банится вообще

---

**2026-03-25T21:06:13 | Routerich**
пишет человек пользующийся амнезией, которая мимикрирует под quic

---

**2026-03-26T11:11:34 | Routerich**
ну логично, она не умеет в udp а gpt видимо хочет quic

---

**2026-03-27T20:45:15 | Dmitry**
а с дискордом может быть связано с quic ?

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

**2026-04-01T13:01:15 | Роман**
Не знаю как в первой версии запрета, но во второй есть определение протокола mtproxy (на котором и работает телеграм)
Исходя из этого, мы можем дурить только его

NFQWS2_OPT="
--name=http --filter-tcp=80 --filter-l7=http --payload http_req --lua-desync=http_methodeol --new
--name=youtube --filter-tcp=443 --filter-l7=tls --payload=tls_client_hello --hostlist-domains=youtube.com,googlevideo.com,youtubei.googleapis.com --lua-desync=multisplit:pos=10:seqovl=1 --new
--name=discord-updates --filter-tcp=443 --filter-l7=tls --payload=tls_client_hello --hostlist-domains=updates.discord.com --lua-desync=fakedsplit:pos=1:tcp_ack=-66000 --new
--name https --filter-tcp=443 --filter-l7=tls --payload=tls_client_hello --lua-desync=multisplit:blob=fake_default_tls:tcp_ts=-1000:pos=2:nodrop --new
--name=telegram-media --filter-l7=mtproto --payload=mtproto_initial --lua-desync=fake:blob=0x00000000 --new
--name=quic --filter-udp=443 --filter-l7=quic --payload=quic_initial --lua-desync=fake:blob=fake_default_quic:repeats=6
"

---

**2026-04-01T13:42:36 | Bullet for my valentine Poison**
adding low-priority default empty desync profile we have 1 user defined desync profile(s) and default low priority profile 0 we have 0 user defined desync template(s) profile 1 (noname) lua fake(repeats="6",tcp_ts="-600000",badsum="",blob="blob_tls_clienthello_ticket_rzd_ru" range_in=x0-x0 range_out=a0-a0 payload_type= tls_client_hello) profile 1 (noname) lua multidisorder(pos="1,sniext+1,host+1,midsld,endhost-1" range_in=x0-x0 range_out=a0-a0 payload_type= tls_client_hello)
lists summary:
blobs summary: blob 'fake_default_tls' : size=680 alloc=808 blob 'fake_default_http' : size=263 alloc=263 blob 'fake_default_quic' : size=620 alloc=620
initializing conntrack with timeouts tcp=60:300:60 udp=60 ipcache lifetime 7200s Running as UID=1 GID=1 initializing raw sockets bind-fix4=0 bind-fix6=0 set_socket_buffers fd=3 rcvbuf=2048 sndbuf=32768 fd=3 SO_RCVBUF=4096 fd=3 SO_SNDBUF=65536 set_socket_buffers fd=4 rcvbuf=2048 sndbuf=32768 fd=4 SO_RCVBUF=4096 fd=4 SO_SNDBUF=65536
LUA INIT LUA v5.1 LuaJIT 2.1.1756211046 OpenResty JIT: ON fold cse dce fwd dse narrow loop abc sink fuse LUA REMOVE: os.execute io.popen package.loadlib debug package.loaded.debug LUA BLOB: fake_default_tls (size=680) LUA BLOB: fake_default_http (size=263) LUA BLOB: fake_default_quic (size=620) LUA STR: NFQWS2_VER LUA NUMERIC: qnum desync_fwmark NFQWS2_COMPAT_VER VERDICT_PASS VERDICT_MODIFY VERDICT_DROP VERDICT_MASK VERDICT_PRESERVE_NEXT DEFAULT_MSS IP_BASE_LEN IP6_BASE_LEN TCP_BASE_LEN UDP_BASE_LEN ICMP_BASE_LEN TCP_KIND_END TCP_KIND_NOOP TCP_KIND_MSS TCP_KIND_SCALE TCP_KIND_SACK_PERM TCP_KIND_SACK TCP_KIND_TS TCP_KIND_MD5 TCP_KIND_AO TCP_KIND_FASTOPEN TH_FIN TH_SYN TH_RST TH_PUSH TH_ACK TH_FIN TH_URG TH_ECE TH_CWR IP_RF IP_DF IP_MF IP_OFFMASK IP_FLAGMASK IPTOS_ECN_MASK IPTOS_ECN_NOT_ECT IPTOS_ECN_ECT1 IPTOS_ECN_ECT0 IPTOS_ECN_CE IPTOS_DSCP_MASK IP6F_MORE_FRAG IPV6_FLOWLABEL_MASK IPV6_FLOWINFO_MASK IPPROTO_IP IPPROTO_IPIP IPPROTO_IPV6 IPPROTO_ICMP IPPROTO_TCP IPPROTO_UDP IPPROTO_ICMPV6 IPPROTO_SCTP IPPROTO_HOPOPTS IPPROTO_ROUTING IPPROTO_FRAGMENT IPPROTO_AH IPPROTO_ESP IPPROTO_DSTOPTS IPPROTO_MH IPPROTO_HIP IPPROTO_SHIM6 IPPROTO_NONE ICMP_ECHOREPLY ICMP_DEST_UNREACH ICMP_REDIRECT ICMP_ECHO ICMP_TIME_EXCEEDED ICMP_PARAMETERPROB ICMP_TIMESTAMP ICMP_TIMESTAMPREPLY ICMP_INFO_REQUEST ICMP_INFO_REPLY ICMP_UNREACH_NET ICMP_UNREACH_HOST ICMP_UNREACH_PROTOCOL ICMP_UNREACH_PORT ICMP_UNREACH_NEEDFRAG ICMP_UNREACH_SRCFAIL ICMP_UNREACH_NET_UNKNOWN ICMP_UNREACH_HOST_UNKNOWN ICMP_UNREACH_NET_PROHIB ICMP_UNREACH_HOST_PROHIB ICMP_UNREACH_TOSNET ICMP_UNREACH_TOSHOST ICMP_UNREACH_FILTER_PROHIB ICMP_UNREACH_HOST_PRECEDENCE ICMP_UNREACH_PRECEDENCE_CUTOFF ICMP_REDIRECT_NET ICMP_REDIRECT_HOST ICMP_REDIRECT_TOSNET ICMP_REDIRECT_TOSHOST ICMP_TIMXCEED_INTRANS ICMP_TIMXCEED_REASS ICMP6_ECHO_REQUEST ICMP6_ECHO_REPLY ICMP6_DST_UNREACH ICMP6_PACKET_TOO_BIG ICMP6_TIME_EXCEEDED ICMP6_PARAM_PROB MLD_LISTENER_QUERY MLD_LISTENER_REPORT MLD_LISTENER_REDUCTION ND_ROUTER_SOLICIT ND_ROUTER_ADVERT ND_NEIGHBOR_SOLICIT ND_NEIGHBOR_ADVERT ND_REDIRECT ICMP6_DST_UNREACH_NOROUTE ICMP6_DST_UNREACH_ADMIN ICMP6_DST_UNREACH_BEYONDSCOPE ICMP6_DST_UNREACH_ADDR ICMP6_DST_UNREACH_NOPORT ICMP6_TIME_EXCEED_TRANSIT ICMP6_TIME_EXCEED_REASSEMBLY ICMP6_PARAMPROB_HEADER ICMP6_PARAMPROB_NEXTHEADER ICMP6_PARAMPROB_OPTION LUA BOOL: b_debug b_daemon b_server b_ipcache_hostname b_ctrack_disable LUA RUN FILE: /opt/zapret2/lua/zapret-lib.lua LUA RUN FILE: /opt/zapret2/lua/zapret-antidpi.lua LUA RUN FILE: /opt/zapret2/lua/zapret-auto.lua LUA INIT DONE
opening nfq library handle unbinding existing nf_queue handler for AF_INET (if any) binding nfnetlink_queue as nf_queue handler for AF_INET unbinding existing nf_queue handler for AF_INET6 (if any) binding nfnetlink_queue as nf_queue handler for AF_INET6 binding this socket to queue '65302' setting copy_packet mode set receive buffer size to 1048576

---

**2026-04-01T13:55:20 | Routerich**
и хде твои хвалёные блобы?
lists summary:

blobs summary:
blob 'fake_default_tls' : size=680 alloc=808
blob 'fake_default_http' : size=263 alloc=263
blob 'fake_default_quic' : size=620 alloc=620

---

**2026-04-01T13:58:56 | Routerich**
надо каждый объявить
--blob=quic_3:@/opt/zapret2/files/fake/quic_3.bin

---

**2026-04-02T14:44:12 | Vasa**
для Клауду папку для эксперементов...

ждем...
"хочу попробовать запустить этот проект. можешь сделать нужное?
https://docs.llmvtuber.com/en/docs/quick-start/
https://github.com/Open-LLM-VTuber/Open-LLM-VTuber"

---

**2026-04-03T16:55:12 | Андрей**
Блокировка со стороны ркн. Но тут дело чуть сложнее, чем просто проксирование. Дело в том, что meet активно пытается в  разные стратегии для передачи данных (udp/quick/tcp). Ну и вопрос - а какие проксировать домены ип? Т.к. только meet.google.com будет точно недостаточно- это просто фронт

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

**2026-04-03T20:27:34 | Vasa**
не, h должен быть одинаковый, насколько я знаю. я про маскировку под протокол quick \ https итд

---

**2026-04-04T12:11:17 | Vasa**
кстати с маскировкой под quick скорость ниже примерно на 30%

---

**2026-04-04T16:25:18 | Vasa**
ну не только.

еще дело в параметрах JC и в мимикрии

например мимикрия под https даёт лучшую скорость чем под quick

---

**2026-04-06T00:21:05 | вася778**
https://github.com/telemt/telemt/blob/main/docs/QUICK_START_GUIDE.ru.md

---

**2026-04-06T19:13:02 | lxstwxrden**
QUIC выбираем свой. Говорю сразу - QUIC гугла не сработает

---

**2026-04-07T10:41:23 | Routerich**
пользоваться и дальше и не пользоваться скриптом запрета, тольку от него 0. кста из-за маскировки quic4all ломает амнезию. ну или пользоваться ванильным вг

---

**2026-04-07T10:44:19 | Routerich**
ну для quic

---

**2026-04-07T10:46:51 | Routerich**
видишь, работает quic на замедленном сервере. но вот владельцам авг такая магия не светит

---

**2026-04-07T13:28:23 | Роман**
QUIC выбираем свой. Говорю сразу - QUIC гугла не сработает, это слова автора.

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

**2026-04-08T13:30:37 | ARTEM**
Вот запарсил приложение whatsapp во время попытки сделать бэкап, може мне какой то cdn включить ?
76.221.179.35.in-addr.arpa
a106.r.akamai.net
a1072.dscg.akamai.net
a1640.dscg2.akamai.net
a1670.dscna.akamai.net
a1855.w7.akamai.net
a1915.dscw7.akamai.net
backup.googleapis.com
clients3.google.com
ec2-35-179-221-76.eu-west-2.compute.amazonaws.com
j.sni.global.fastly.net
juskykey.net
k.sni.global.fastly.net
m.sni.global.fastly.net
quic.map.fastly.net
stun.cloudflare.com
stun.l.google.com
stun.nextcloud.com
stun.voip.blackberry.com
www.domeideadatahere.com
www.juicychasecosmic.com

---

**2026-04-08T18:45:23 | Mikhail Velichko**
А подскажите по какой причине по дефолту отключен QUIC и в каких случаях его включать?

---

**2026-04-08T21:42:06 | Uintik️️️🐈‍⬛**
Подскажите пожалуйста, планируется ли, добавленения в следующую сборку прошивки. Библиотек, для подержки: DNS-over-QUIC. Вопрос возник, в саязи с блокировкой DNS-over-HTTPS. От: Adguard.

---

**2026-04-10T08:04:04 | Mikhail Timonenkov**
А чтобы в finder quic работал нужно свой curl собирать?

---

**2026-04-10T10:04:11 | Viktor Polesov**
Прошу прощения за повтор. После замены в Подкопе типа конфигурации с URL подключения на конфигурацию Outboubd, не работает нормальным образом Firefox. При обращении к роутеру - XHR request aborted by browser,  сайты открываются оч. медленно и не все сайты загружаются, в том числе и в режиме инкогнито(!). QUIC (network http, http3) переключен в false. Что ещё нужно настроить в Мозилле или в самом Подкопе? Уж, очень не хочется сбрасывать Firefox и не уверен, что это поможет...

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

**2026-04-10T21:46:26 | ARTEM**
Включение Quic для ютуба это полезно или вредно ? 🤔

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

**2026-04-14T12:08:35 | Кирилл**
Для желающих поэкспериментировать - можно просто воспользоваться командой из разделе ручной установки через Systemd вручную: https://github.com/telemt/telemt/blob/main/docs/Quick_start/QUICK_START_GUIDE.ru.md#telemt-%D1%87%D0%B5%D1%80%D0%B5%D0%B7-systemd-%D0%B2%D1%80%D1%83%D1%87%D0%BD%D1%83%D1%8E Единственная разница - перемещать файл нужно не в /bin, а в /usr/bin Ну и не забыть, что перед обновлением сервис лучше остановить, а после обновления - запустить 😅

---

**2026-04-16T20:19:54 | Bullet for my valentine Poison**
а зачем?))) сделай по новой лог. И не открывай в браузере. Пока по логу видно только что пакет с дискорда udp\quick

---

**2026-04-17T14:08:27 | Bullet for my valentine Poison**
Xray – это платформа проксирования, разработанная на основе V2Ray, но с улучшенными функциями и более сложной архитектурой. Основная задача Xray – предоставить пользователям инструменты для обхода интернет-цензуры и обеспечения безопасного доступа к информации, даже в условиях строгих ограничений.

Xray работает на основе нескольких ключевых принципов, которые обеспечивают его эффективность в обходе блокировок и защите конфиденциальности.

Одним из основных преимуществ Xray является его способность маскировать трафик под обычный HTTPS трафик. Это достигается путем использования протокола TLS (Transport Layer Security) и технологии CDN (Content Delivery Network). Благодаря этому, трафик Xray практически невозможно отличить от обычного трафика веб-сайтов, что значительно усложняет его блокировку.

Xray поддерживает различные транспортные протоколы, такие как TCP, mKCP, WebSocket и QUIC. Это позволяет пользователям выбирать наиболее подходящий протокол в зависимости от их сетевых условий и требований к производительности. Например, WebSocket часто используется для обхода блокировок, а QUIC обеспечивает более высокую скорость и надежность соединения.

Xray предоставляет пользователям широкие возможности для настройки параметров подключения. Это позволяет адаптировать протокол под конкретные нужды и условия сети. Например, можно настроить шифрование трафика, изменить порт подключения и использовать различные методы обфускации.

Как и любой другой VPN-протокол, Xray имеет свои преимущества и недостатки. Важно учитывать их при выборе протокола для обеспечения безопасности и конфиденциальности в интернете.

*  Высокая степень защиты от блокировок: Благодаря маскировке трафика и поддержке различных транспортных протоколов, Xray эффективно обходит большинство видов интернет-цензуры.

*  Гибкость и настраиваемость: Пользователи могут адаптировать параметры подключения под свои нужды и условия сети.

*  Высокая производительность: Поддержка протокола QUIC обеспечивает высокую скорость и надежность соединения.

*  Бесплатность и открытый исходный код: Xray является бесплатным и открытым программным обеспечением, что позволяет любому пользователю проверить его безопасность и надежность.

*  Сложность настройки: Настройка Xray может быть сложной для начинающих пользователей, так как требует определенных технических знаний.

*  Необходимость в собственном сервере: Для использования Xray необходимо иметь собственный сервер или арендовать его у хостинг-провайдера.

*  Ограниченная поддержка в VPN-сервисах: Xray не так широко поддерживается VPN-сервисами, как более распространенные протоколы, такие как OpenVPN или WireGuard. Впрочем, для тех, кто ищет альтернативу с высокой степенью защиты, это может быть оправданным.

VPN протокол Xray особенно полезен в следующих ситуациях:

*  Обход интернет-цензуры: Если вы живете в стране с жесткой интернет-цензурой, Xray поможет вам получить доступ к заблокированным веб-сайтам и сервисам.

*  Защита конфиденциальности: Xray шифрует ваш интернет-трафик и скрывает ваш IP-адрес, что обеспечивает защиту вашей конфиденциальности в интернете.

*  Безопасное подключение к публичным Wi-Fi сетям: Xray защищает ваш трафик от перехвата при подключении к публичным Wi-Fi сетям.

*  Доступ к контенту с географическими ограничениями: Xray позволяет вам получить доступ к контенту, который доступен только в определенных странах.

---

**2026-04-18T22:21:41 | Алексей Микоянов**
Ещё один слой абстракции для создания зашифрованных туннелей, работающих поверх стандартных веб-протоколов HTTP2 и HTTP3. Применяется там, где блочат VLESS, Hysteria2 и прочую теперь уже попсу. 
Маскируется под обычный браузинг. Срабатывает там, где не фильтруют HTTP3 (QUIC)

---

**2026-04-20T17:42:24 | Aleksey Vydrin**
QUIC придумали и ниче не захотелось никому

---

