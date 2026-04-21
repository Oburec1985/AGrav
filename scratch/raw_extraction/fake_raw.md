# Raw Extraction: fake

**2026-01-01T13:46:44 | Bullet for my valentine Poison**
opt/zapret2/files/fake/quic_3.bin --lua-desync=fake:blob=quic_3  ты это имел ввиду?

---

**2026-01-01T13:56:13 | Routerich**
давай я 1 разъ поясню, а при похожих вопросах мут на подумать дам. есть основной инстанс, тот, которому ты пишешь стратегии, он помимо собственной работы поднимает скрипты, отдельными инстансами. они ничего не знают о том, что и как ты включаешь или отключаешь, они нюхают трафик на наличие пейлоад и сравнивают со своей предустановкой. opt/zapret2/files/fake/quic_3.bin вот это инициирует блоб для квика(включает его)

---

**2026-01-01T21:06:41 | Anna Bagler**
Не видно полноценно версию прошивки, если позволяет, то запустить скрипт 5 ещё раз, чтоб версию подкопа сменить, по fakeip проверить https://t.me/routerich/3845/333975

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

**2026-01-02T18:32:46 | Anna Bagler**
Все нормально. Попробуйте перезапустить интерфейс awg10. Если не поможет, перенесите список yt из discord в main (в двух секциях не оставляйте). Диагностика подкопа на fakeip не ругается?

---

**2026-01-03T11:06:04 | Алексей**
Всех с наступившим Новым годом.В чем может быть причина периодической ошибки "браузер не использует fakeip"?

---

**2026-01-03T18:34:23 | Anna Bagler**
Достаточно google.com. Проверьте свой vless в приложении на смартфоне. Диагностика подкопа не ругается на fakeip?

---

**2026-01-03T21:31:02 | Anna Bagler**
Надо с проблемного, чтоб fakeip глянуть по диагностике.

---

**2026-01-04T14:15:13 | Роман**
В службах создать стратегию discord: 
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1

---

**2026-01-04T15:22:01 | Anna Bagler**
Это не диагностика. Меня интересует fakeip в диагностике.

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

**2026-01-05T23:06:17 | Владимир Волков**
Техподдержка умная, я - определённо нет. Но если у вас есть ВПН интерфейс, куда вы хотите всё перенаправить, но исключить определённые сайты, то почему это не должно работать? Из-за fakeip технологии в новых подкопах? Ну тогда поставить PBR - на Хабре, кажется, по нему даже статья была с примером WG и except ru, если правильно помню. Давно было.

---

**2026-01-06T04:28:41 | Трантипуй**
Проверил, сейчас отвалился именно fake ip

---

**2026-01-06T05:41:02 | Роман**
Попробовать стратегию:
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1

---

**2026-01-06T15:04:49 | Dugar**
nslookup fakeip.podkop.fyi вот тут прилетает публичный адрес, а не  подкопа.
нейросетка говорит это из-за приоритета ipv6 над ipv4 в убунте. Вот пытаюсь вырубить его. Как бы не вырубить всю убунту))

---

**2026-01-06T15:25:33 | Anna Bagler**
Диагностику подкопа с телефона сделайте, чтоб посмотреть на проверки по fakeip. После выбора стратегии проверяли ТВ и телефон?

---

**2026-01-06T15:32:43 | Dugar**
Починил.

Дело было в приоритете ipv6 над ipv4.

Диагностировал проблему с вашей помощью (проглядел последнюю строчку, тут сорян) и докой подкопа тут https://podkop.net/docs/troubleshooting/. Проверил получение fakeIP

Ну а далее, поменял приоритет с помощью инструкции https://wiki.tiukov.com/books/linux/page/prioritet-ipv6.

Всё заработало.

Спасибо!

---

**2026-01-06T15:41:49 | Anna Bagler**
А ещё ниже fakeip?

---

**2026-01-06T22:14:24 | Anna Bagler**
Низ на fakeip не ругается?

---

**2026-01-07T00:01:52 | Alex Mendez**
у грока спросил совет, сунул ему мой лог. FakeIP включен. Там все тесты проходит кроме пары которые всегда и у всех валятся.

---

**2026-01-08T10:52:33 | Anna Bagler**
Диагностику подкопа, чтоб было видно низ с fakeip.

---

**2026-01-08T12:25:35 | Anna Bagler**
Тогда не обращайте внимание. Диагностику подкопа можно с этого устройства посмотреть по проверкам fakeip.

---

**2026-01-08T14:27:18 | Alx Tlv**
от первого диагностика отличается тем что браузер не использует fakeIP

---

**2026-01-08T14:28:56 | Anna Bagler**
Тут явно ругается на fakeip. https://t.me/routerich/3845/333975 - пройтись по этому списку и доп. ПО/расширения на ПК проверить.

---

**2026-01-09T14:53:42 | Роман**
--payload=tls_client_hello 
--lua-desync=fake:blob=fake_default_tls:tcp_ts=-1000:repeats=1

--payload=tls_client_hello 
--lua-desync=multisplit:blob=fake_default_tls:tcp_ts=-1000:pos=2:nodrop:repeats=1

--payload=tls_client_hello 
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1

--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1

Эти стратегии пробуйте.

---

**2026-01-10T01:34:54 | Роман**
Либо 4pda сменили алгоритмы защиты от ддос, и запросы с fakeIP не проходят. Но это так, предложения. Потому как несколько часов назад читал закрытую тему, все было а порядке.

---

**2026-01-10T19:05:48 | Вадим**
Просто периодами вообще доступ ко всему пропадает. Я понимаю пропадал бы доступ только к заблокированным ресурсам, но перестает работать вообще все. Вот например сейчас  такая же ситуация, ни один сайт не работает:
Sat Jan 10 19:01:56 2026 daemon.err sing-box[12220]:  [31mERROR [0m[1894] [ [38;5;214m2699487942 [0m 5.6s] connection: open connection to fakeip.podkop.fyi:8443 using outbound/direct[direct-out]: dial tcp 64.188.104.86:8443: i/o timeout
Sat Jan 10 19:02:01 2026 daemon.err sing-box[12220]:  [31mERROR [0m[1899] [ [38;5;113m2769574753 [0m 5.7s] connection: open connection to fakeip.podkop.fyi:8443 using outbound/direct[direct-out]: dial tcp 64.188.104.86:8443: i/o timeout
Sat Jan 10 19:02:30 2026 daemon.err sing-box[12220]:  [31mERROR [0m[1928] [ [38;5;192m1111307006 [0m 30.3s] connection: open connection to ip.podkop.fyi:443 using outbound/http[main-out]: unexpected status: 502 Bad Gateway
Sat Jan 10 19:03:59 2026 daemon.err sing-box[12220]:  [31mERROR [0m[2017] [ [38;5;228m166873306 [0m 30.0s] connection: open connection to 57.144.245.32:443 using outbound/http[main-out]: unexpected status: 502 Bad Gateway

---

**2026-01-10T19:10:17 | Routerich**
Удалите секцию main временно, и проверяйте. У вас не может нормально отработать fakeip из-за проблем с опера прокси и дальше ошибки

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

**2026-01-10T21:36:36 | Routerich**
Не влияет, fakeip браузерная ошибка из-за другого

---

**2026-01-11T12:56:36 | khozorgan**
Здравствуйте, С наступившими праздниками, задавал вопрос FakeIP не проходит проверку, причина в блокировщике рекламы адгуард,из трея удалил,посмотрел в диспетчере а он запущен, прибил процесс и проверку прошёл на ноуте, может пригодится кому либо.

---

**2026-01-11T14:49:12 | Routerich**
потому что предыдущая бета не пыталась исправить постоянно отваливающийся fakeip у клиентов и не умела отключать fakeip, функционал расширяется, что-то надламывается. обновитесь последним билдом из поста и протестируйте

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

**2026-01-11T18:50:15 | Роман**
--payload=tls_client_hello 
--lua-desync=fake:blob=fake_default_tls:tcp_ts=-1000:repeats=1

--payload=tls_client_hello 
--lua-desync=multisplit:blob=fake_default_tls:tcp_ts=-1000:pos=2:nodrop:repeats=1

--payload=tls_client_hello 
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1

--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1

Попробовать эти стратегии.

---

**2026-01-11T19:12:36 | Bullet for my valentine Poison**
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multisplit:blob=fake_default_tls:tcp_ts=-1000:pos=2:nodrop
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN

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

**2026-01-12T11:47:00 | Routerich**
https://t.me/routerich/394153/432059
● ZeroBlock v0.5.0-r141

  Новые возможности:

  Подписки (Subscriptions)
  Теперь можно использовать URL подписки с несколькими прокси:
  - URLTest - автовыбор лучшего по задержке
  - Selector - ручной выбор через Clash API
  - First - использовать только первый прокси

  Dashboard
  - Новая вкладка с виджетами трафика, соединений и статуса
  - Тест задержки для всех секций одной кнопкой
  - Добавлена плашка «Активен: server-name 169ms» для секций с автовыбором сервера (URLTest, подписки)

  Автонастройка
  - Автопроверка: если Opera Proxy или AWG10 уже установлены - галочки заблокированы

  ---
  Исправления:

  - Отключённые секции не отображаются в Dashboard
  - DNS теперь корректно работает при disable_fakeip=1
 -  Исправлено добавление задачи в crontab
#ZeroBlock

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

**2026-01-12T15:30:53 | Routerich**
    --payload=tls_client_hello \
    --lua-desync=fake:blob=0x00000000:tcp_seq=-10000:tcp_ack=-66000 \
    --lua-desync=fake:blob=fake_default_tls:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,rndsni,dupsid
проверяйте

---

**2026-01-12T16:47:55 | Danil**
Доброго времени суток, стоит запрет2, все работает, на телефоне и пк, но не работает на lg смарт тв, помогите исправить, или может где взять другую стратегию на пробу

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

---

**2026-01-13T14:57:04 | Routerich**
Решение по доступу к доменам из списков h.o.d.c.a или cloudflare! 
Вариант 1:
Добавлять их в секцию awg10(если она жива) и выключать fakeip для этой секции, тогда домены резолвятся напрямую и работают через awg10 туннель. 
Вариант 2:
Включить в настройках zeroblock "Проксировать трафик роутера", тогда роутер будет так же работать по спискам секций.
Я постараюсь подумать над обходным решением, чтобы эти списки можно было использовать в других секциях.

---

**2026-01-13T18:43:16 | Routerich**
это связано с fakeip, т.е. c zeroblock

---

**2026-01-14T11:10:35 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock v0.5.0-r159
  - Исправлена петля трафика tproxy-tproxy
  - FakeIP выключен по умолчанию для VPN секций(как решение работы opkg, если в списках есть github и производные), включен для Proxy(если в прокси будет github, то сломается opkg)
подробнее о последнем https://t.me/routerich/394153/438385
#ZeroBlock

---

**2026-01-14T22:16:02 | Anna Bagler**
По fakeip что-то мешает на устройстве, проверяйте. По discord пробуйте позже скрипт 5 запустить или свой платный конфиг использовать для awg.

---

**2026-01-15T11:24:31 | Тарантино**
Всем доброго дня! Я так понимаю у многих Подкоп не работает? Переставил уже раз десять....... DNS роутера не проходит через sing-box
Браузер не использует FakeIP.  Такие ошибки?

---

**2026-01-15T11:30:05 | Bullet for my valentine Poison**
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multisplit:blob=fake_default_tls:tcp_ts=-1000:pos=2:nodrop
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN

---

**2026-01-15T20:22:45 | Routerich**
так, пройдёмся. скорость чем меряется? fakeip на авг по дефолту выключен, чтобы не ломать роутер. списки точно не работают или это всё же относится к fakeip?

---

**2026-01-15T20:34:12 | ㅤРоман**
для проверки fakeip в списки вношу (если нету) 2ip.io и 2ip.ru в разные что бы видеть что работает а что нет. вот в опере работало а в авг10 нет, как вы выше написали это не баг а отключенно.

---

**2026-01-16T10:05:38 | Routerich**
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:badsum:tcp_seq=10000000:tls_mod=sni=rzd.ru:repeats=4
--lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum
--lua-desync=multisplit:blob_tls_clienthello_www_google_com:pos=2:nodrop
--lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=4
--lua-desync=fakedsplit:pos=method+2:tcp_flags_set=SYN

---

**2026-01-16T10:12:51 | Routerich**
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=fake_default_tls:badsum:tls_mod=sni=rzd.ru:repeat=4
--lua-desync=multisplit:blob=fake_default_tls:badsum:pos=2:nodrop
--lua-desync=fakedsplit:pos=method+2:tcp_flags_set=SYN:repeat=2

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

**2026-01-16T11:28:00 | Bullet for my valentine Poison**
--out-range=-s34228 
--payload=tls_client_hello 
--lua-desync=fake:blob=fake_default_tls:badsum:tls_mod=sni=max.ru 
--lua-desync=multisplit:blob=fake_default_tls:badsum:pos=2:nodrop

попробуйте эту.Но она не полноценная для Лыжи. В акк даст доступ или нет?

---

**2026-01-16T12:06:36 | Юрий Теленков**
а сама стратегия Running with flags: --queue-num=537 --threads=1 --packet-mark=32768 --silent --tls=disabled --sni-domains=<trie of 157 vertexes> --sni-detection=parse --synfake=0 --udp-filter-quic=disabled --udp-stun-filter --fbegin --tls=enabled --frag=tcp --frag-sni-reverse=1 --frag-sni-faked=0 --frag-middle-sni=1 --frag-sni-pos=1 --fk-winsize=0 --fake-sni=1 --fake-sni-seq-len=1 --fake-sni-type=default --faking-strategy=pastseq --fake-seq-offset=10000 --seg2delay=0 --sni-domains=<trie of 29 vertexes> --sni-detection=parse --synfake=0 --udp-filter-quic=disabled --fend --fbegin --tls=enabled --frag=none --frag-sni-reverse=0 --frag-sni-faked=0 --frag-middle-sni=0 --frag-sni-pos=1 --fk-winsize=0 --fake-sni=1 --fake-sni-seq-len=1 --fake-sni-type=default --faking-strategy=tcp_check --seg2delay=0 --sni-domains=<trie of 418 vertexes> --sni-detection=parse --synfake=0 --udp-filter-quic=all --udp-mode=fake --udp-fake-seq-len=6 --udp-faking-strategy=none --fend

---

**2026-01-16T13:11:05 | D-man**
Собственно заработал fake ip

---

**2026-01-16T13:36:14 | D-man**
Ну у меня fake ip не работал через тейл, я вот что смог наковырял) может кому полезно будет, но теперь роутер из сети доступен по 192.168.1.1 😂

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

**2026-01-16T18:13:29 | Anna Bagler**
Ниже что по fakeip?

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

**2026-01-16T21:33:10 | Сергей**
DNS проверки
Обнаружены проблемы
Bootstrap DNS
8.8.8.8
Основной DNS
8.8.8.8 [doh]
DNS на роутере
DHCP содержит DNS сервер
Sing-box проверки
Проверки пройдены
Sing-box установлен
Версия Sing-box совместима (новее 1.12.4)
Сервис sing-box существует
Автостарт sing-box отключен
Процесс sing-box запущен
Sing-box слушает порты
Nftables проверки
Проверки пройдены
Таблица существует
Правила mangle существуют
Счётчики правил mangle
Правила mangle output существуют
Счётчики правил mangle output
Правила прокси существуют
Счётчики правил proxy
Другие правила маркировки не найдены
Outbounds проверки
Обнаружены проблемы
main
547 ms
Youtube_Discord
Не отвечает
FakeIP проверки
Проверки пройдены
DNS роутера проходит через sing-box
Браузер не использует FakeIP

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

**2026-01-16T23:44:35 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r26:
  - Исправлено отображение имени серверов в подписке
  - Исправлено поведение опции "Отключить FakeIP"
  - Исправлено поведение кнопки перезапустить(в некоторых случаях она могла не сразу обновлять свой статус)
  - Исправлена очистка и добавление правил nft
  - Исправлена работа DNS в секции при указании "полностью маршрутизированное устройство"
#ZeroBlock

---

**2026-01-17T00:53:02 | Андрей ☕️**
config section                                                                       option name 'YouTube'                                                        option enabled '1'                                                           option tls_enabled '1'                                                       option fake_sni '1'                                                          option faking_strategy 'tcp_check'                                           option fake_sni_seq_len '1'                                                  option fake_sni_type 'random'                                                option frag 'tcp'                                                            option frag_sni_reverse '1'                                                  option frag_sni_faked '0'                                                    option frag_middle_sni '1'                                                   option frag_sni_pos '1'                                                      option seg2delay '3'                                                         option fk_winsize '0'                                                        option synfake '0'                                                           option sni_detection 'parse'                                                 option all_domains '0'                                                       option quic_drop '0'                                                         option udp_mode 'fake'                                                       option udp_fake_seq_len '6'                                                  option udp_fake_len '64'                                                     option udp_filter_quic 'all'                                                 option udp_faking_strategy 'none'                                            option udp_stun_filter '0'                                                   list sni_domains 'googlevideo.com'                                           list sni_domains 'youtubei.googleapis.com'                                   list sni_domains 'ytimg.com'                                                 list sni_domains 'yt3.ggpht.com'                                             list sni_domains 'yt4.ggpht.com'                                             list sni_domains 'youtube.com'                                               list sni_domains 'youtubeembeddedplayer.googleapis.com'                      list sni_domains 'ytimg.l.google.com'                                        list sni_domains 'jnn-pa.googleapis.com'                                     list sni_domains 'youtube-nocookie.com'                                      list sni_domains 'youtube-ui.l.google.com'                                   list sni_domains 'yt-video-upload.l.google.com'                              list sni_domains 'wide-youtube.l.google.com'                                 list sni_domains 'youtu.be'                                                  list sni_domains 'youtube.googleapis.com'                                    list sni_domains 'yt.be'                                                     list sni_domains 'withyoutube.com'                                           list sni_domains 'youtubeeducation.com'                                      list sni_domains 'youtubefanfest.com'                                        list sni_domains 'youtubegaming.com'                                         list sni_domains 'youtubekids.com'                                           list sni_domains 'youtubemobilesupport.com'

---

**2026-01-17T03:05:25 | ALeX**
Проверено неоднократно. Периодически падает dns ресолвинг на br-lan интерфейсе. по localhost ресолвит нормально.  При этом диагностика FakeIP в диагностике podkop показывает сбой. WatchDoc (кстати почему Doc а не Dog :) ) кажет "wdoc_singbox: FakeIP DNS: OK" и не переталкивает podkop. ручной перезапуск podkop или интерфейса br-lan решает на какое то время...

---

**2026-01-17T09:20:44 | Navisal**
что с fakeip?  Обходы работают

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

**2026-01-17T11:01:29 | Антон**
Все норм работает в диагностике FakeIP (роутер) неактивен

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

**2026-01-17T17:14:31 | Владимир Оралов**
в чекере "Прокси-трафик не маршрутизируется через FakeIP"

---

**2026-01-17T23:37:50 | Dmitrii Burenin**
FakeIP ялярм

---

**2026-01-18T14:20:27 | Sh1nn**
Кстати, обратил внимание, что если отключить FakeIP хоть на одной секции, то запущенный торрент клиент в домашней сети начинает нехило так насиловать роутер, особенно если соединений к пирам >500. Это адекватное поведение или у меня лапки?

---

**2026-01-18T14:40:37 | ALeX**
Sun Jan 18 14:03:03 2026 daemon.info wdoc_singbox: FakeIP DNS: OK
Sun Jan 18 14:03:03 2026 daemon.info wdoc_singbox: Sing-box: OK
Sun Jan 18 14:03:11 2026 daemon.err tailscaled[11232]: 2026/01/18 11:03:11 netcheck: netcheck.runProbe: named node "1002a" has no v6 address
Sun Jan 18 14:03:11 2026 daemon.err tailscaled[11232]: 2026/01/18 11:03:11 netcheck: netcheck.runProbe: named node "1001a" has no v6 address
Sun Jan 18 14:03:18 2026 daemon.err uhttpd[4509]: [info] luci: accepted login on /admin/services/podkop for root from 192.168.21.19

---

**2026-01-18T15:01:39 | Sh1nn**
Достаточно просто FakeIP на всех секциях включить и всё приходит в норму

---

**2026-01-18T15:04:26 | Routerich**
поясню, при выключении fakeip все запросы уводятся на тпроски, который уже принимает решения куда трафик кидать, да это может создавать нагрузку

---

**2026-01-18T15:36:40 | Routerich**
а если включить проксирование для роутера и выключить fakeip какое поведение?

---

**2026-01-18T16:09:08 | Anna Bagler**
Запрет остановить и отключить пока. В система - планировщик убрать строку по нему. Добавить yt в секцию discord, если не поможет - в main. По fakeip пройтись по пунктам https://t.me/routerich/3845/333975 или ещё что-то на ПК мешает.

---

**2026-01-18T21:48:00 | ㅤРоман**
сегодня добрался до роутера, снес прошивку. начисто поставил 0.6.0-r35 , очь долго ставилась опера и авг, по итогу скорость не режется 800 прием 900 отдача из обещанных провайдером гигабита. в диагностике только вот это смущает "FakeIP (клиент)  Не удалось проверить: Failed to fetch" а так вроде все работает. на подкопе раз в сутки падал инет и сингбокс сыпал разного рода ошибки. сейчас, тьфу тьфу тьфу ошибок в логах нет. жду упадет ли инет как в подкопе 😄

---

**2026-01-18T21:53:52 | ㅤРоман**
еще и такая была 
"sing-box[14837]:  [31mERROR [0m[5585] [ [38;5;229m4021226242 [0m 0ms] router: missing fakeip record, try enable experimental.cache_file"
это подкоповские. на зеро тоже такие же?

---

**2026-01-18T23:40:22 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r40:
  - Изменена логика опции "Исключить BitTorrent", теперь она создаёт отдельный outbound и пытается сделать offload силами nftables(Попытка избежать торрент нагрузки при отключенном fakeip)
Да, первые пакеты всё-равно попадут в tproxy, но на продолжительных раздачах это должно сказаться. Нужна обратная связь, возможно таймаут слишком мал(30 сек)
#ZeroBlock

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

**2026-01-19T18:45:03 | Routerich**
zeroblock check_fakeip

---

**2026-01-20T01:41:50 | Routerich**
Fakeip в подкопе

---

**2026-01-20T03:40:12 | Kiss_My_Axe**
DNS и fakeip норм работают.
Хм...

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

**2026-01-20T16:04:34 | Routerich**
@BFMVPoison Gomer а кто-нибудь логи запрета смотрел? костыль ввиде fakeip отключен для awg10? либо же гитхаб исключен из списков зб?

---

**2026-01-20T16:25:11 | Gomer Simpson**
Логи смотреть уже не актуально. Вечером вчера сбросился и №5 накатил. Гитхаба в списках Z не было точно. Fakeip поискал сейчас - не нашёл.

---

**2026-01-20T19:37:22 | Routerich**
оно всё в yacd. потому что без fakeip всё идёт через синг

---

**2026-01-20T19:43:13 | Юрий**
а то, что у меня fakeip только на awg отключен, имеет какое-то значение?

---

**2026-01-20T19:47:49 | Routerich**
нет, чтобы синг знал что куда, метится весь трафик, если гитхаб и его подомены работают нормально, можно включить fakeip всё будет по старому

---

**2026-01-20T21:45:58 | Игорь Котыс**
А вот пункт «Браузер не использует FakeIP» важен, чтобы его исправить перейдите сюда.
"Сюда" забыли вставить ссылку

---

**2026-01-21T06:47:16 | Routerich**
основа не подкоп, а синг. а основное "за" за синг это fakeip

---

**2026-01-21T09:30:01 | Евгений**
а это как исправить : Браузер не использует FakeIP

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

**2026-01-22T07:03:32 | Routerich**
проверьте нагрузку на роутер через htop, может быть дело в отключённом fakeip

---

**2026-01-22T18:12:39 | Алекс К**
1 DNS проверки 
❌DHCP содержит DNS сервер
2 Sing-Box - green 
3 Nftables проверки - green 
4 Outbounds проверки - green
5 FakeIP - green

---

**2026-01-22T22:13:48 | Alex Pavloff**
С включенным fake ip не работает. Отключил, вроде начал грузить...

---

**2026-01-23T00:47:19 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r77:
  - Полная переработка выключенного fakeip. теперь трафик не из листов и подсетей не попадает в tproxy. Exclude Bittorrent оставлен как рудимент на всякий случай
  - Исправлена очередность nft правил
#ZeroBlock

---

**2026-01-23T11:36:20 | Bullet for my valentine Poison**
В интернете в поиске вбить: подкоп ошибка fake ip мануал itdog. И там будет инструкция, как проверить и прочее

---

**2026-01-23T13:45:18 | Anna Bagler**
У вас проблемы с секцией discord, список yt из неё стоит перенести в main. Но есть проблема с fakeip. На устройстве заблокированные сайты не работают.

---

**2026-01-23T14:00:43 | Andrey**
спасибо за помощь. Список YT вообще нигде не был добавлен. Добавил его в main. Проблема с fakeip ушла

---

**2026-01-24T15:44:48 | Bullet for my valentine Poison**
ну Fresa вроде с ней воюет. Галка отключить Fake Ip стоит по умолчанию.Должно работать по идее. Я напихал бесплатных подписок разных типов и авг мне почти не нужен) На нем сейчас Гугл плей висит.

---

**2026-01-24T23:36:44 | Routerich**
интересно почему на моей врт, которая пережила 3 апгрейда, где миксованные fake ip на туннелях и проксях всё работает, а у вас нет?

---

**2026-01-25T15:47:28 | Routerich**
суть в fakeip и dns hijack. все запросы перехватываются и отправляются в цепочку dnsmasq -> dns-failsafe-proxy -> singbox. роутер работает по этой же цепочке, и он получает резолв  fakeip но его трафик не проксируется

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

**2026-01-25T18:24:31 | Alex**
уж не знаю что поменялось между билдами 81 и 91 но неожиданно прямо полноценно заработало перенаправление трафика в ovpn туннель. люто плюсую, теперь наконец-то можно пользоваться православной родной прошивкой не ограничивая себя сценариями маршрутизации (ovpn нужен был по работе).

вдруг кому пригодится - мини-гайд по настройке туннелирования секции через ovpn соединение:
- идём "VPN" -> "OpenVpn" и импортируем конфиг через "Загрузка конфигурационного файла OVPN".

- заходим внутрь добавленного конфига через "изменить" и добавляем строку 
pull-filter ignore redirect-gateway
 чтобы не пускать весь трафик роутера через соединение. Сохраняем, запускаем конфиг кнопкой "start"
- идём "Сеть" -> "Интерфейсы", создаем новый интерфейс, называем, например "ovpn" и в протоколе выбираем "Неуправляемый". Из списка устройств выбираем то, что было создано после того как Вы успешно запустили конфиг OpenVpn (вероятно это будет tun0).  Жмем "Создать интерфейс". В открывшемся окне - "Сохранить". Вне модалки - сохраняем-применяем.

- Идём в "Сеть" -> "Межсетевой экран" -> "Основные настройки". Жмем "Добавить". Название - "ovpn", входящий трафик - отколнять, исходящий трафик - принимать, внутризональная пересылка - отклонять. Маскардинг - включить, ограничение MSS - включить, охватываемые сети - выбираем свежесозданный интерфейс (если как в предыдущем шаге, то он будет называться ovpn). Разрешить перенаправление в 'зоны назначения' - оставляем пустым. Разрешить перенаправление из 'зон источников' - добавляем lan.

- Переходим на вкладку "Расширенные настройки", Охватываемые устройства - выбираем наш адаптер (например, tun0), отключаем "Маскарадинг IPv6", "Использовать протокол" - только IPv4. Сохраняем в модалке, сохраняем на списке зон, применяем.

- Идем в "Службы" - "ZeroBlock" - "Секции маршрутизации" - "Добавить". Тип подключения - "VPN-интерфейс", в списке ниже выбираем по названию созданного после запуска vpn устройства (tun0, например). Тип протокола DNS - UDP, DNS сервер по-вкусу. Отключить FakeIP - включаем галку. "Ввод пользовательских доменов" - текстовое поле. Список пользовательских доменов - перечисляем через запятую без пробелов. Сохраняем, применяем, сохраняем, перезапускаем ZeroBlock.

---

**2026-01-25T19:12:56 | Anna Bagler**
Ну, fakeip отрабатывает.

---

**2026-01-25T21:30:46 | Dmitry**
Подскажите пожалуйста. Как пофиксить? Для запрета2 выставил Desync Mark = 0x400000. И все равно ошибка вылезает. И ошибку fakeip клиент никак победить не могу ..

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

**2026-01-25T23:39:00 | Jazzzcore**
Вообщем что. 
Перезагрузил просто телефон🤡
И инстаграм и ютуб работают. 
Спасибо вам большое добрые люди💪

P. S. Но трафик так же не проходит через fake ip. 
Роутер тоже перезагружал. Хз нужно ли это? Если всё фурычит пока и так🤔

---

**2026-01-26T04:50:54 | VK11**
Может кто пояснит что это за сообщения, с чем связаны и как решить. Их там много в течении часа. Появляются часто и помногу. И в подкопе все по умолчанию после пятого скрипта. Mon Jan 26 03:35:29 2026 daemon.err sing-box[24198]:  [31mERROR [0m[337518] [ [38;5;195m4174731771 [0m 0ms] router: missing fakeip record, try enable experimental.cache_file
Mon Jan 26 03:46:49 2026 daemon.err sing-box[24198]:  [31mERROR [0m[338198] [ [38;5;192m1888791550 [0m 0ms] router: UDP is not supported by outbound: main-out
Mon Jan 26 03:46:50 2026 daemon.err sing-box[24198]:  [31mERROR [0m[338199] [ [38;5;100m1462722132 [0m 0ms] router: UDP is not supported by outbound: main-out

---

**2026-01-26T04:59:45 | Kiss_My_Axe**
Opera-proxy не желает работать с udp. UDP заблокирован на удалённой стороне и повлиять на это невозможно.

missing fakeip record, try enable experimental.cache_file
Какие-то глюки с фейкайпи.


Запустите это в терминале роутера, cкрин-фото-текст результата пришлите.
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/test_config_script/test_config_script_nightly)

---

**2026-01-26T11:00:07 | Routerich**
да я уже прям задумываюсь стоило ли реализовывать отключение fakeip чет муторно оно всё

---

**2026-01-26T11:24:46 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r107:
  - automerge в nft при пересечении ip диапазонов в списках(исправление необязательное, если вы не используете отключение fakeip)
#ZeroBlock

---

**2026-01-26T14:12:33 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r111:
  - Дедупликация доменов в одной секции для отключенного fakeip(если домен есть в предустановленном листе, введённый вручную дубль отбрасывается)
  - Увеличены буферы всех пользовательских списков до динамических 64kb(~2000 доменов) и добавлен warning при переполнении
#ZeroBlock

---

**2026-01-26T16:16:17 | Kiss_My_Axe**
Тест.
В ZB только один раздел. Выход опера-прокси.
В разделе включен список МЕТА и добавлены эти внешние списки с гита:
https://raw.githubusercontent.com/KharunDima/whatsapp-lists/main/lists/domains.txt
https://raw.githubusercontent.com/KharunDima/whatsapp-lists/main/lists/cidr.txt
Больше там нет ничего.
Клиент ваззапа на мобиле при отправке сообщения вешает часики навечно.
То же самое в подкопии - работает сразу и безоговорочно.

А вот если в ZB отключить fakeip, то опача! Заработало!
Вот так на сейчас.

---

**2026-01-26T17:03:16 | Routerich**
не качает = не работает, логично же
Mon Jan 26 15:11:45 2026 daemon.err zeroblock[16276]: [disable_fakeip ] Decompile failed for /tmp/zeroblock/rulesets/telegram.srs:  [31mFATAL [0m[0000] EOF
Mon Jan 26 15:11:45 2026 daemon.err zeroblock[16276]: [disable_fakeip ] Failed to decompile: /tmp/zeroblock/rulesets/telegram.srs
Mon Jan 26 15:11:50 2026 daemon.err zeroblock[16276]: [http_client    ] curl_easy_perform failed: Error
Mon Jan 26 15:11:52 2026 daemon.err zeroblock[16276]: [disable_fakeip ] Decompile failed for /tmp/zeroblock/rulesets/telegram.srs:  [31mFATAL [0m[0000] EOF
Mon Jan 26 15:11:52 2026 daemon.err zeroblock[16276]: [zeroblock      ] ZeroBlock started successfully
Mon Jan 26 15:11:52 2026 cron.err crond[16661]: crond (busybox 1.36.1) started, log level 7
Mon Jan 26 15:12:27 2026 daemon.err zeroblock[16055]: [disable_fakeip ] Download failed for https://github.com/itdoginfo/allow-domains/releases/latest/download/telegram.srs: Error
Mon Jan 26 15:12:27 2026 daemon.err zeroblock[16055]: [disable_fakeip ] Failed to download SRS for telegram
Mon Jan 26 15:12:32 2026 daemon.err zeroblock[16055]: [lists_loader   ] Failed to download https://raw.githubusercontent.com/KharunDima/whatsapp-lists/main/lists/domains.txt

---

**2026-01-26T17:09:36 | Kiss_My_Axe**
fakeip включен, ваззап-клиент телефона не отправляет сообщения

---

**2026-01-26T17:26:16 | Routerich**
это наводит на мысль что fakeip не срабатывает, а прямого роутинга нет, потому что fakeip включен

---

**2026-01-26T17:47:08 | Routerich**
zeroblock check_fakeip whatsapp.com
что покажет?

---

**2026-01-26T17:47:58 | Kiss_My_Axe**
root@roskomnadzor:~# zeroblock check_fakeip whatsapp.com
{"fakeip":1,"IP":"198.18.0.3"}

---

**2026-01-26T19:26:40 | Routerich**
могу сказать что у меня через варп, без fakeip, и иногда срабатывает какая-то блокировка, потому что все работает кроме ва и инст, поговаривали про тспу на нодах клауда

---

**2026-01-26T20:05:03 | ㅤРоман**
в последней версии не срабатывает галка в авг  "Отключить FakeIP", галка стоит но все равно что вписано в "Список пользовательских доменов" идет через фейкайпи.  это же не правильно? или я не так понимаю эти настройки.

---

**2026-01-26T20:14:58 | Routerich**
ну правильно fakeip для клиентов, а не для резолвинга

---

**2026-01-26T22:51:57 | Routerich**
и немножко пояснения на основе существующих секций
  Как работает FakeIP

  Клиент → DNS запрос (A или AAAA)
         ↓
  sing-box → FakeIP ответ (198.18.x.x или fc00::x)
         ↓
  Клиент → TCP/UDP к FakeIP адресу
         ↓
  nftables → маркировка → TPROXY
         ↓
  sing-box → смотрит FakeIP таблицу → узнаёт реальный домен
         ↓
  sing-box → резолвит реальный IP домена → подключается через VPN

  Ключевой момент

  FakeIP адрес (fc00::x) - это просто "метка", а не реальный адрес назначения.

  Когда sing-box получает пакет на fc00::3, он:
  1. Смотрит в FakeIP таблицу: fc00::3 → example.com
  2. Резолвит example.com → получает реальный IP
  3. Подключается к реальному IP через VPN outbound

  Если VPN не умеет IPv6

  Зависит от dns_strategy:
  ┌──────────────┬───────────────────────┬───────────────────────────┐
  │ dns_strategy │    Реальный резолв    │ Результат с IPv4-only VPN │
  ├──────────────┼───────────────────────┼───────────────────────────┤
  │ ipv4_only    │ Только A записи       │ ✔️ Работает               │
  ├──────────────┼───────────────────────┼───────────────────────────┤
  │ prefer_ipv4  │ A предпочтительнее    │ ✔️ Работает (обычно)      │
  ├──────────────┼───────────────────────┼───────────────────────────┤
  │ prefer_ipv6  │ AAAA предпочтительнее │ ⚠️ Может не работать      │
  ├──────────────┼───────────────────────┼───────────────────────────┤
  │ ipv6_only    │ Только AAAA           │ ❌ Не работает            │
  └──────────────┴───────────────────────┴───────────────────────────┘
  Рекомендация

  Если VPN (Opera, AWG) не поддерживает IPv6:

  dns_strategy = ipv4_only  или  prefer_ipv4

  Тогда:
  - Клиент получает FakeIP6 fc00::3 для AAAA запроса ✔️
  - sing-box резолвит реальный домен только в IPv4 ✔️
  - Подключение через VPN по IPv4 ✔️

  Итог: IPv6 на стороне клиента работает, даже если VPN только IPv4. Главное - правильная
  dns_strategy.

❯  prefer_ipv6 почему может не работать?

● Разберём детальнее:

  Сценарий с prefer_ipv6

  1. Клиент запрашивает AAAA для youtube.com
  2. sing-box возвращает FakeIP6: fc00::5
  3. Клиент подключается к fc00::5
  4. sing-box видит: fc00::5 → youtube.com
  5. sing-box резолвит youtube.com с prefer_ipv6:
     → получает 2607:f8b0:4004:800::200e (реальный IPv6 Google)
  6. sing-box пытается подключиться к этому IPv6 через VPN outbound

  Зависит от типа outbound

  WireGuard/AmneziaWG (туннель):
  - Если в конфиге WG нет Address = fd00::1/128 и AllowedIPs не включает ::/0
  - IPv6 пакеты не пойдут через туннель
  - Результат: network unreachable или timeout

  Прокси (Opera, VLESS, Shadowsocks, Trojan):
  - sing-box отправляет доменное имя на прокси сервер
  - Прокси сервер сам резолвит и подключается
  - Если прокси сервер имеет IPv6 → будет работать
  - dns_strategy здесь не влияет на реальное подключение!

  Уточнение

  Для прокси протоколов (Opera, VLESS и т.д.) dns_strategy влияет только на:
  1. FakeIP ответы клиенту
  2. direct outbound (прямые подключения)

  Прокси сервер получает домен и сам решает как подключаться.

  Когда реально не работает

  VPN: WireGuard без IPv6
  dns_strategy: prefer_ipv6
  Клиент: запросил сайт который имеет только AAAA запись (редко, но бывает)
  Результат: sing-box резолвит в IPv6 → WG не может отправить → timeout

  Вывод

  С прокси (Opera/VLESS): prefer_ipv6 безопасен
  С туннелем (WG/AWG без IPv6): лучше ipv4_only или prefer_ipv4

---

**2026-01-27T10:03:40 | D S**
тоже появилась эта проблема, убрал галку sing-box какие-то списки скачала с гитхаба. Но где-то еще проблема. Fake-IP Заработал в роутере, но не заработал в браузере. 
Podkop: v0.4.11-r1
LuCI App: v0.4.11-r1
Sing-box: 1.11.15
OpenWrt Version: RouteRich 24.10.2 r28739-d9340319c6 RR-3.6.6
Device Model: Routerich AX3000 v1

---

**2026-01-27T10:16:47 | Юрий 🏂**
меня вот что смущает :
🥸 FakeIP status
❌ Failed to get FakeIP info
❌ Sing-box does NOT work with FakeIP: ;; communications error to 127.0.0.42#53: connection refused
;; communications error to 127.0.0.42#53: connection refused
;; communications error to 127.0.0.42#53: connection refused
;; no servers could be reached

---

**2026-01-27T11:35:25 | Юрий 🏂**
но при этом : 
FakeIP проверки
Проверки пройдены
DNS роутера проходит через sing-box
Браузер использует FakeIP
Прокси-трафик направляется через FakeIP

---

**2026-01-27T12:17:03 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.1-r8:
 Новая фича auto fallback two stage(для плавающих блокировок или проблем с маршрутизацией провайдера):
 Теперь если прямо не указано качать списки через секцию, при ошибке скачивания списков активируется two stage, который ищет первую включенную секцию, перестраивает роутер на неё и качает списки. если у пользователя github в постоянном блоке, то рекомендуется самостоятельно включить скачивание через секцию.
 
  Исправления:
  - Увеличен таймаут nftables set до 60 минут(проблема браузеров)
  - Исправлена проблема доменов исключений для отключенного fakeip
#ZeroBlock

---

**2026-01-27T14:27:36 | Yury Kuzmenko**
Кстати а есть инсайд какой нибудь по доменам HODCA с FakeIP?

---

**2026-01-27T20:53:28 | Юрий**
коннекты есть. Иногда в журнале урл адресов, фуй какойто появляется fakeip.zeroblock.fyi 😁

---

**2026-01-28T13:29:24 | Weyland**
Добрый день. Пожалуйста, добавьте в DNS failsafe proxy возможность изменять значение поля TTL ответа. В момент восстановления работы подкопа хочется, чтобы FakeIP заработал быстрее без необходимости чистить днс кэш у всех клиентов вручную. В идеале иметь в настройках DHS failsafe proxy отдельное поле со устанавливаемым значением и возможность включать/выключать правку TTL.

---

**2026-01-28T14:00:21 | Andrey Matveev**
Браузер не использует fakeip

---

**2026-01-28T15:32:03 | Routerich**
проверяйте clash api либо домен скидывает в direct-bt либо контрак не держит коннект. сейчас nft set на 60 минут, т.е. роутинг работает ещё 60 минут после резолва, если мы говорим о секции с отключенным fakeip, все остальные вопросы к сингбоксу

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

**2026-01-29T11:36:13 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.1-r81:
  Исправление
  - FakeIP для пользовательских доменов не работал для самого роутера
#ZeroBlock

---

**2026-01-29T20:44:52 | Anna Bagler**
Fakeip отрабатывает. Попробуйте отключить ipv6.

---

**2026-01-30T12:21:58 | Routerich**
а, так вы хотели это, тогда вот:
ZeroBlock– инструмент для маршрутизации трафика через прокси и VPN на основе списков
доменов. Использует sing-box в качестве ядра маршрутизации.
Основные возможности
• Маршрутизация по спискам доменов
• Поддержка прокси-протоколов: VLESS, VMess, Trojan, Shadowsocks, Hysteria2, SOCKS4/5,
HTTP(S)
• Поддержка VPN-интерфейсов: WireGuard, AmneziaWG, OpenVPN, GRE, L2TP, PPTP и др.
• Автоматический выбор лучшего прокси (URLTest)
• Прозрачная маршрутизация через FakeIP
• Панель управления YACD

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

**2026-01-31T14:16:00 | Sergey Solomatin**
стратегия для дискорда :)
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1

---

**2026-01-31T15:51:46 | Bullet for my valentine Poison**
Я кстати хотел один момент спросить, насчет интерпретации стратегий из Блокчека.
--payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:ip_autottl=-6,3-20:tls_mod=rnd,dupsid,padencap:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1
это он склеил две в одну?

---

**2026-01-31T16:13:59 | Bullet for my valentine Poison**
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=fake_default_tls:badsum:tls_mod=sni=rzd.ru:repeat=4
--lua-desync=multisplit:blob=fake_default_tls:badsum:pos=2:nodrop
--lua-desync=fakedsplit:pos=method+2:tcp_flags_set=SYN:repeat=2
я здесь распишу, чтобы было понятно. Хоть страта и кривая.
Первые две строчки мне дали загрузить Окно для входа в акк на тв.
С третьей строчкой и четвертой строчкой я добился прогрузки картинок и лого в ютубе.
А добавив репиты избавился от зависания видосов на 5-10 секунде и дальнейшего черного экрана.
(шапка по дефолту)

---

**2026-01-31T16:25:12 | Routerich**
--out-range=-s34228
--payload=tls_client_hello
--in-range=-s5556 --lua-desync=circular:fails=2:time=60
--in-range=x
--lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=1
--lua-desync=multisplit:pos=2,sld:seqovl=620:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=1
--lua-desync=fake:blob=0x00000000:tcp_ack=-66000:strategy=2
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:tls_mod=rnd,dupsid,rndsni,padencap:tcp_ack=-66000:strategy=2
--lua-desync=multisplit:pos=2,endhost:strategy=2
--lua-desync=multisplit:pos=1:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:ip_id=zero:strategy=3
--lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=4
--lua-desync=multisplit:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=5
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=fonts.google.com:strategy=6
--lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=6
--lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=6
--lua-desync=multidisorder:pos=7,sld+1:strategy=7
--lua-desync=multidisorder:pos=1,midsld,endhost-1:strategy=8
--lua-desync=fake:blob=0x00000000:tcp_seq=-10000:tcp_ack=-66000:repeats=2:strategy=9
--lua-desync=fake:blob=fake_default_tls:tcp_seq=-10000:tcp_ack=-66000:repeats=2:tls_mod=rnd,dupsid,sni=www.google.com:strategy=9
--lua-desync=multisplit:pos=1,midsld:strategy=9
--lua-desync=multidisorder:pos=1,midsld:strategy=10
--lua-desync=multisplit:pos=1,2:seqovl=4:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=11
--lua-desync=multidisorder:pos=2,5,105,host+5,sld-1,endsld-5,endsld:strategy=12
--lua-desync=fake:blob=0x0F0F0F0F:badsum:tcp_seq=-10000:tcp_ack=-66000:strategy=13
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:badsum:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=13
--lua-desync=multisplit:pos=2,sld:seqovl=2108:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=13
--lua-desync=hostfakesplit:midhost=host-2:host=rzd.ru:tcp_seq=0:tcp_ack=-66000:badsum:strategy=14:final

---

**2026-01-31T17:14:00 | Kiss_My_Axe**
FakeIP не работает. Это допустимо на ZB, но на подкопе это, кажется, невозможно. Надо смотреть состояние подкопа в его Диагностике.

---

**2026-01-31T17:44:13 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.1-r103:
  - DHCP picker — выбор IP из списка аренд DHCP для "Полностью маршрутизированные IP-адреса", "Исключённые из секции IP-адреса" и "Исключённые IP"
  - Декомпиляция .srs в JSON для секций с отключенным fakeip

  FakeIP улучшения:
  - Умное создание dns-fakeip только когда нужно

  Исправления:
  - Логические route rules для excluded_source_ips(вместо 2 правил, теперь 1)
  - Валидация IP, подсетей, доменов и интерфейсов(если есть такие, кто трогает конфиг zeroblock руками)
  - Байпас proxy endpoint для routing loops(как для awg10 и с банановым вкусом)
  - Логика взаимоисключения download_lists_via_proxy и auto_fallback

  Рефакторинг:
  - libcurl для latency test вместо wget(просто убран системный вызов)
  - Переход на L.Poll вместо setInterval(стандартно для Luci)
#ZeroBlock

---

**2026-01-31T20:29:40 | Yury Kuzmenko**
Надеюсь к релизу победят fake ip и hodca

---

**2026-01-31T20:33:04 | Yury Kuzmenko**
В секциях с fake ip

---

**2026-01-31T20:36:20 | Дмитрий**
Добрый вечер
Провел вчерашний, и сегодняшний вечера в настройках Роблокса под ЗероБлоком...
Результат отсутствует :)
Так еще и FakeIP (роутера) отвалился...
Есть специалисты, которые в этом могли бы проконсультировать?
Внук очень хочет Роблокс...

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

**2026-02-01T12:23:46 | Nook Scheel**
root@RouteRich:~# ps | grep -E 'nfq|tpws|dvtws'
 1896 root      1340 S    grep -E nfq|tpws|dvtws
 4190 daemon    1940 S    /opt/zapret/nfq/nfqws --user=daemon --dpi-desync-fwmark=0x40000000 --qnum=200 --filter-tcp=443 --dpi-desync=fake fakeddisorder --dpi-desync-split-pos=10,midsld --dpi-desync-fake-tls=/
 4191 daemon    1712 S    /opt/zapret/nfq/nfqws --user=daemon --dpi-desync-fwmark=0x40000000 --qnum=65400 --dpi-desync=fake --dpi-desync-repeats=2


Запрет работает

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

**2026-02-01T15:25:43 | Виль**
список доменов добавлял, только я так понимаю, я включал его в стратегию для ютуба, а также нашел в сообщениях стратегию для него:
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
вопрос, как это учесть или куда вписывать?

---

**2026-02-01T21:50:53 | Камиль**
В авг секции:
Тип протокола DoH
Cтавлю чек бокс отключить FakeIp 
Летят 
[zeroblock] ZeroBlock started successfully
Sun Feb 1 21:30:23 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_domains Error: No such file or directory
Sun Feb 1 21:30:33 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_domains Error: No such file or directory
Sun Feb 1 21:32:06 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_hodca Error: No such file or directory
Sun Feb 1 21:32:15 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_hodca Error: No such file or directory
Sun Feb 1 21:39:00 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_google_play Error: No such file or directory
Sun Feb 1 21:39:02 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_google_play Error: No such file or directory
Sun Feb 1 21:39:03 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_hodca Error: No such file or directory
Sun Feb 1 21:40:19 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
Обновление через Proxy секцию каждый час(было бы удобно кнопку добавить обновить списки в ручную) 

Оставляю все тоже самое, убираю чек бокс отключить FakeIp  и похоже ничего не летит

---

**2026-02-02T14:34:30 | Камиль**
Вроде как, когда выключил fakeIP для авг секции и сменил на udp ролики стали лучше грузиться🫩 но в консоли ерунда
No such file or directory

---

**2026-02-02T16:40:46 | Hump Dog**
А можно для задних парт коротко для чего нужен fakeip в принципе?

---

**2026-02-02T16:53:38 | Камиль**
А можно прям для Камчатки, может есть какие-то эталонные настройки? Нужен ли в целом awg? Нужно ли оставлять чек бокс у fakeip в awg ? Нужно doh оставлять или можно и нужно менять ? 
😐 
Я как будто все возможные варианты проверил все равно no such летят..

---

**2026-02-02T16:57:06 | Routerich**
нет понятия эталон, выключать fakeip нужно для всяких консолей

---

**2026-02-02T17:57:18 | Роман**
Значит искать другую стратегию. 
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
Эту попробуйте.

---

**2026-02-02T18:12:14 | Камиль**
У меня есть своя амнезия на ru vps, есть сервис где можно взять разные виды подписок и там и там пробовал. 
У меня чехарда начинается именно когда я выключаю(чек бокс выкл) fakeIP (no such) летят, если fakeIP (чек бокс активный) у меня плохо работаю запрещенные соц.сети, на разных устройствах дома. Поэтому даже уже не знаю что еще может быть.

---

**2026-02-02T19:23:38 | Routerich**
из какого скрипта? который открывал связь с марсом? это удп трафик, там нечего  сплитать, fake blob и репиты, достаточно

---

**2026-02-02T22:12:27 | Routerich**
ну fakeip с клиента проверьте на роутере

---

**2026-02-02T23:02:59 | Den**
Ща еще fakeip проверю

---

**2026-02-03T00:20:00 | Routerich**
только мета в опере, а там fakeip

---

**2026-02-03T00:21:13 | Routerich**
и я сильно сомневаюсь что его выключали, и как-то одновременно выключился fakeip и Ютуб отрезолвился в ipv6

---

**2026-02-03T00:56:35 | Artamonich92**
А на Опере fakeip не нужно отключать?

---

**2026-02-03T11:01:57 | Kiss_My_Axe**
А вот нет признака catch-all.
zeroblock.catch_all=section
zeroblock.catch_all.connection_type='vpn'
zeroblock.catch_all.interface='awg10'
zeroblock.catch_all.dns_type='dot'
zeroblock.catch_all.dns_server='8.8.8.8'
zeroblock.catch_all.bootstrap_dns_server='77.88.8.8'
zeroblock.catch_all.disable_fakeip='0'
zeroblock.catch_all.user_domain_list_type='disabled'
zeroblock.catch_all.user_subnet_list_type='disabled'
zeroblock.catch_all.enabled='0'

---

**2026-02-03T12:07:05 | Routerich**
мало вводных, нужно пнимание где там fakeip и в каком он состоянии

---

**2026-02-03T14:19:04 | Routerich**
вот помню первую версию отключенного fakeip, которая роутер ложила

---

**2026-02-04T08:55:22 | Pavel**
Спасибо! помогло!
Ещё вопрос возник - в ходе диагностики показывает что браузер не использует fakeip  + myip.com показывает реальный IP адрес.
как это исправить?

---

**2026-02-04T10:23:44 | Azizkhan**
Подскажите пожалуйста есть ли статья по работе DNS на роутере в купе с подкопом? Хочу добавить xbox сервера и comms и сделать их приоритетными, как бы это сделать?
Прикладываю скрин текущих настроек. Сейчас иногда fakeip будто не срабатывает, в подкопе настроен 2 vless ключа на различные локации и Meta всё равно иногда блочит к некоторым страничкам из-за локации со своей стороны, хотя если включить этот же впн напрямую на клиентском устройстве, то локация правильно ими воспринимается и всё проходит чётко.

---

**2026-02-04T11:11:51 | Pavel**
Привет всём, подскажите пожалуйста как отключить безопасный ДНС и настроить fakeip в гугл хроме? 
Подозреваю где-то тут: но какой урл указывать?

---

**2026-02-04T11:20:56 | Bullet for my valentine Poison**
Итак, упростил я свою страту. (не уверен что все правильно, но работает)
Как было изначально:
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1 
--lua-desync=fake:blob=fake_default_tls:badsum:tls_mod=sni=rzd.ru:repeat=4
--lua-desync=multisplit:blob=fake_default_tls:badsum:pos=2:nodrop
--lua-desync=fakedsplit:pos=method+2:tcp_flags_set=SYN:repeat=2

убрал лишнее:

--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1 
--lua-desync=fake:blob=fake_default_tls:badsum:pos=2:nodrop:tls_mod=sni=rzd.ru:repeat=4

---

**2026-02-04T11:58:20 | Bullet for my valentine Poison**
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1 
--lua-desync=fake:blob=fake_default_tls:badsum:tls_mod=sni=rzd.ru:repeat=4

---

**2026-02-04T11:59:22 | Routerich**
оригинальный ман с гита 
--filter-tcp=80,443 --filter-l7=http,tls
--out-range=-s34228
--in-range=-s5556 --lua-desync=circular
--in-range=x
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:badsum:strategy=1
--lua-desync=multidisorder:strategy=2
--payload=http_req
--lua-desync=fake:blob=fake_default_http:badsum:strategy=1
--lua-desync=multisplit:strategy=2

---

**2026-02-04T12:04:21 | Routerich**
отбой, я по первому считал, а теперь вон оно как
Другое важное отличие - отсутствие жестко определенных фаз десинхронизации. То, что вы раньше писали как fake,multisplit реализуется двумя последовательно вызываемыми Lua функциями. Их может быть столько, сколько нужно, учитывая логику прохождения пакетов и операций с ними, и у каждой могут быть свои параметры. Может даже несколько раз вызываться одна и так же функция с разными параметрами. Так, например, можно послать несколько фейков, причем с разными фулингами. Конкретный вызов --lua-desync функции называется инстансом. Инстанс - это связка имени функции, номера вызова внутри профиля и номера самого профиля. Это похоже на одну программу, которую можно запустить много раз с разными параметрами.

---

**2026-02-04T12:47:57 | Kiss_My_Axe**
Не баг, но фича.

Режим Полностью маршрутизированные IP-адреса игнорирует fakeip.
До тех пор, пока домены не пропишешь в Список пользовательских доменов, или не выберешь список, включающий в себя эти домены.

---

**2026-02-04T12:56:56 | Routerich**
fakeip я ж так понимаю включен для секции?

---

**2026-02-04T13:24:38 | Routerich**
пакеты  | полный мануал 
ZeroBlock 0.6.1-r131:
  Исправления:
  - Полностью маршрутизированные IP-адреса игнорировали fakeip
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

**2026-02-04T21:42:47 | Dmitriy M 🎃**
Блин! Отключил галку Fake IP и Вотсап сразу заработал

---

**2026-02-05T09:47:00 | Routerich**
пакеты  | полный мануал 
ZeroBlock 0.6.1-r143:
  Новое:
  - Parental Control — блокировка по расписанию с фильтрацией по устройствам
  - Отображение времени роутера в LuCI при настройке PC
  - Режим "block all" — полная блокировка интернета без указания доменов/списков/ip
  Исправление:
  - fakeip-check работал через fallback, а не как ожидалось
  - Отображение текущего outbound для proxy секций
  Доп пояснение
  - Если одна PC секция — положение в LuCI не важно
  - Если несколько PC секций — порядок определяет приоритет блокировки

#ZeroBlock

---

**2026-02-05T13:00:37 | Routerich**
вывод покажите и что насчёт fakeip для секции?
nft list table inet zeroblock

---

**2026-02-05T13:39:24 | Routerich**
пакеты  | полный мануал 
ZeroBlock 0.6.1-r146:
  Исправление:
  - user_subnets теперь маркируются в nftables независимо от disable_fakeip
#ZeroBlock

---

**2026-02-05T16:26:48 | Routerich**
пакеты  | полный мануал 
ZeroBlock 0.6.1-r150:
  Исправление:
  - Удалены правила conntrack(до лучших времен)
  - Убран дубликат создания правил для disable_fakeip=1 секций
#ZeroBlock

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

**2026-02-06T13:28:36 | Routerich**
у меня почти всё без fakeip и я тестил оба варианта прокси роутера, одинаково долго при подключении, потому что сеты ненаполнены, но дальше работает стабильно

---

**2026-02-06T20:53:19 | Routerich**
если в секции выключен fakeip браузер надо перезапустить, или ждать пока он не соизволит попросить адрес у роутера

---

**2026-02-06T23:25:32 | Сергей**
Комарады, если я правильно понимаю, fakeip в общем случае надо включать на всех секциях. А в каких сценариях его надо выключать для секции?

---

**2026-02-07T00:07:28 | Сергей**
А в случае с обычным веб серфингом , получается , что fakeip всегда включаем. Я прав?

---

**2026-02-07T00:20:33 | Routerich**
всё, по желанию. fakeip позволяет обойти блокировки сервисов  сидящих на cdn

---

**2026-02-07T00:46:26 | Nic**
Проработал несколько минут, и снова отвалился, когда я начал страницы поактивнее открывать. На этот раз переподключение к wifi на устройстве сработало (раньше не помогало), однако в логе такие ошибки (раньше не было): 10 Sat Feb  7 00:36:36 2026 daemon err hostapd: nl80211: kernel reports: key addition failed
11 Sat Feb  7 00:36:36 2026 daemon err hostapd: nl80211: kernel reports: key addition failed
12 Sat Feb  7 00:36:56 2026 daemon err hostapd: nl80211: kernel reports: key addition failed
13 Sat Feb  7 00:36:56 2026 daemon err hostapd: nl80211: kernel reports: key addition failed
14 Sat Feb  7 00:38:56 2026 daemon err sing-box[9578]:  [31mERROR [0m[2012] [ [38;5;187m71954220 [0m 0ms] router: missing fakeip record, try enable experimental.cache_file

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

**2026-02-07T16:42:08 | Kiss_My_Axe**
Ну и в режиме РоутеРич первый, Кинетик второй, клиенты подключены к кинетику, скорее всего fakeip работать не будет.
Надо или убирать кина вовсе, или РР ставить после кина.
Тем более у кина порт ван на 100мбит макс, а судя по всему вы тариф-то со скоростью 100+ приобрели.

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

**2026-02-08T21:45:49 | Anna Bagler**
Из-за полной маршрутизации диагностика подкопа может ругаться на fakeip, это нормально. Проверьте ссылку.

---

**2026-02-09T00:25:28 | Роман**
Метод https get использовали? Там нужно было галочку поставить. И снять ограничение на 5 стратегий, пусть бы искал. 
Я недавней ночью 77 стратегий перебрал, поэтому облегчу вам задачу, авось у вас моя стратегия заработает. 
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1

---

**2026-02-09T12:28:08 | Azizkhan**
почему-то не срабатывает FakeIP

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

**2026-02-10T20:13:18 | Routerich**
ага, а что насчёт fakeip(клиент)?

---

**2026-02-10T20:16:54 | Routerich**
это меня не интересует, мне бы знать использует ли клиент fakeip, на этом я пойду спатки

---

**2026-02-10T21:06:43 | Sergey Kornilov**
Статус FakeIP
! не работает в браузере
✔ работает на роутере
Статус DNS
✔ DOT (8.8.8.8) available
✔ DNS роутера работает
Config: RouteR
! таймаут

---

**2026-02-11T12:18:48 | VK11**
Странности с DNS. Имеем роутер последней версии и прошивкой, накатан скрипт 5. по умолчанию. в случайный момент времени пропадает доступ в интернет с устройств по сети и wifi. диагностика с компа показывает, что dns запрос на роутер уходит (видно в мониторинг - трафик пользователей) но ответа нет. на команду nslookup instagram.com выдается адрес роутера и ожидание ответа. при этом в сеть - диагностика все запросы dns отрабатываются. а podkop диагностика красным только Браузер использует FakeIP. В настройках podkop меняем тип dns с DOH на незащищенный - все нормализуется и начинает работать. Возвращаем настройки в DOH - все продолжает работать до следующего раза. Вопрос собственно куда копать?

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

**2026-02-11T13:54:20 | Routerich**
default
  --out-range=-s34228
  --payload=tls_client_hello
  --in-range=-s5556 --lua-desync=circular:fails=3:maxtime=60
  --in-range=x
  --lua-desync=multisplit:seqovl=681:seqovl_pattern=blob_stun:strategy=1
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=fonts.google.com:strategy=2
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=2
  --lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=2
  --lua-desync=fake:blob=blob_tls_clienthello_t2_ru:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=m.ok.ru:strategy=3
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=3
  --lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=3
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:strategy=4
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=google.com:strategy=4
  --lua-desync=multisplit:pos=2,sld:seqovl=2108:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=4
  --lua-desync=fake:blob=blob_stun:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=5
  --lua-desync=fakeddisorder:pos=1:pattern=blob_tls_clienthello_www_google_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=5
  --lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=6
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=7
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=7
  --lua-desync=multisplit:pos=2,sld:seqovl=620:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=7
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=8
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=8
  --lua-desync=multisplit:pos=2,sld:seqovl=620:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=8
  --lua-desync=hostfakesplit:host=mapgl.2gis.com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=9
  --lua-desync=fake:blob=blob_tls_clienthello_www_4pda_to:optional:tcp_ts=-600000:tls_mod=none:strategy=10
  --lua-desync=fake:blob=blob_stun:optional:tcp_seq=0:tcp_ack=-66000:badsum:strategy=11
  --lua-desync=multisplit:pos=1:seqovl=654:seqovl_pattern=blob_stun:strategy=11
  --lua-desync=hostfakesplit:midhost=host-2:host=i2.photo.2gis.com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=12
  --lua-desync=multisplit:pos=1:seqovl=582:seqovl_pattern=blob_stun:strategy=13:final

---

**2026-02-11T14:32:14 | Sergey Elyutin**
открыл, не попадают, трафик Google и Facebook успешно проксируется, а opencode.ai в списке соединений вообще не появляется. Объясните, пожалуйста, принцип работы подкопа: почему DNS выдает Fake-IP, но этого адреса нет в nft-сете @podkop_subnets

---

**2026-02-11T17:17:09 | Роман**
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
Эту попробуйте, возможности нет. Применить - перезапустить не забывайте.

---

**2026-02-11T20:00:33 | Vasa**
Повышаем стабильность Telegram: поднимаем партизанский MTProxy с Fake TLS / Хабр https://habr.com/ru/articles/994934/

---

**2026-02-12T13:30:58 | zhkaa**
как починить DNS redirect Not configured и fakeip client?

---

**2026-02-12T13:59:25 | zhkaa**
сделал перенаправление на sing-box, fakeip все еще пишет cannot check

---

**2026-02-12T14:43:45 | Vasa**
тот же вопрос задаю, когда мне сервер по опенвпн просто пушит все маршруты нужные... и поднимает fakeDNS )

---

**2026-02-12T15:45:40 | Routerich**
нет, разбираться почему он там, трафик сам по себе туда не попадает, только по спискам. либо просто fakeip везде включите, если уж и тогда трафик полезет, то дело в списках

---

**2026-02-12T18:12:01 | Камиль**
У меня еще теория есть по поводу fakeIP может ему fakeIP не нравится. 
Ну и не только ему... каждый 2-ой сайт пока список не подберешь не открывается

---

**2026-02-12T19:13:28 | Routerich**
пакеты  | полный мануал 
ZeroBlock 0.6.2-r66:
  Новое:
  — URLTest Check Interval — вместо фиксированного выпадающего списка теперь можно
  задать произвольный интервал проверки (например 45s, 2m, 1h). При вводе числа без
  суффикса автоматически добавляются минуты

  Исправления:
  — Переполнение буфера в DNS, утечки сокетов и event-дескрипторов
  — TrustTunnel: NFT-маркировка работает независимо от proxy_router_traffic
  — Graceful timeout — корректная обработка таймаутов без зависания сервиса
  — FakeIP: повторная проверка при DNS-кеше, увеличен таймаут(в диагностике)
  — Clash API: унифицирован URL для тестирования задержки (gstatic.com/generate_204)
  — Частичная запись конфигов: некорректные файлы удаляются вместо сохранения
#ZeroBlock

---

**2026-02-13T10:09:34 | @Dr.Medvedolog**
Ну нет смысла аналог 3X-UI городить, завтра тспу снова научатся FakeTLS MTPROXY банить и все.

---

**2026-02-13T10:44:09 | @Dr.Medvedolog**
А чем это технически отличается от уже зашитой MTPROXY FakeTLS

---

**2026-02-13T12:12:10 | Степан**
Как решить проблему счётчиков и fake ip на последней прошивке?

---

**2026-02-13T12:23:40 | Степан**
Как включить fake ip для браузера?

---

**2026-02-14T13:55:20 | Slava**
добрый день, как можно пофиксить fakeip клиент?

---

**2026-02-14T14:26:29 | Slava**
понимать бы как фиксить эти таблицы. Только с Fakeip разобрался (сбросил конфиг и переустановил пакеты).  Все кроме gemini работает, он только через инкогнито открывается

---

**2026-02-14T16:52:42 | Роман**
Или эти попробуйте. 
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
--payload=tls_client_hello 
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1

---

**2026-02-14T18:24:36 | Routerich**
Галочку на SynFake не ставили ?

---

**2026-02-14T18:33:51 | Alex S**
Прошу прощения,галочка стояла на Fake sni,а на Synfake нет

---

**2026-02-15T03:15:35 | Prefect**
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=20
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=20
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

---

**2026-02-15T03:18:11 | Routerich**
что-нибудь такое пробуйте, блобами поиграйтесь, 
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:repeats=4:badsum:tcp_seq=1000000
--lua-desync=multidisorder:pos=midsld,endhost:seqovl=2

---

**2026-02-15T13:03:42 | Александр**
Подскажите, до этого стоял запрет, вроде бы его удалил, сейчас в ZB две ошибки - fakeip client и dns. По инструкции сделал:
/etc/init.d/dnsmasq restart
И получил
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: no lease, failing

---

**2026-02-15T20:39:29 | Вячеслав**
Ошибка с перенаправлением DNS исчезла,  FakeIP (клиент) Не удалось проверить: Failed to fetch - осталась. Обход пока не работает

---

**2026-02-15T21:35:07 | Вячеслав**
Нихрена не понимаю. Прям на мгновение заработало, с другим прокси. Они оба рабочие. С листом Russia Inside. Подумал может дело в этом, поменял на первом прокси на этот же лист и запустил с ним. УВЫ, нифига. Вернулся на второй и тут облом - тоже теперь не работает. Как так, а? в чем проблема может быть? А с поверкой на FakeIP мне оказывается мюблок мешал

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

**2026-02-16T14:13:02 | Скептик**
Но почему при всех отключенных "галках" на FakeIP реальные IP показывает?

---

**2026-02-16T14:15:29 | Anna Bagler**
Ну, так вы же отключаете fakeip, а не включаете его...

---

**2026-02-16T14:44:24 | Anna Bagler**
Галочка отключает fakeip. Сами ресурсы по проверке IP в секциях есть?

---

**2026-02-16T16:40:23 | Михаил**
Протокол старта zeroblock: Starting ZeroBlock...
[ruleset_manager] API request failed (ret: 0, code: 400, size: 95)
[disable_fakeip] Failed to open dnsmasq config: /tmp/dnsmasq.d/zeroblock-awg20-meta.conf
[disable_fakeip] Failed to open dnsmasq config: /tmp/dnsmasq.d/zeroblock-awg20-twitter.conf
[zeroblock] ZeroBlock started successfully

---

**2026-02-16T16:41:46 | Routerich**
Михаил awg20 это переименованный awg10? disable fakeip поди включен?

---

**2026-02-16T16:43:01 | Михаил**
Да. Протокол проверки с zero самый благостный.   Fakeip весь зеленый

---

**2026-02-16T19:46:58 | Денис**
Можно помощи? awg10 не заводится. Поставил, включил автонастройку.FakeIp из awg10 убрал.


Анализ запущен: 2026-02-16 19:35:16
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
  Facebook IP:  198.18.1.173 | YouTube IP:  198.18.1.174

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.19 MB
  Пинг (ya.ru via awg10): 24.553 / 44.262 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОФЛАЙН
------------------------------------------------------
  curl: (28) Connection timed out after 5001 milliseconds
  Warning: Problem : timeout. Will retry in 1 seconds. 3 retries left.
  curl: (28) Connection timed out after 5001 milliseconds
  Warning: Problem : timeout. Will retry in 2 seconds. 2 retries left.
  curl: (28) Connection timed out after 5002 milliseconds
  Warning: Problem : timeout. Will retry in 4 seconds. 1 retries left.
  curl: (28) Connection timed out after 5001 milliseconds
------------------------------------------------------
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 198.18.1.174
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Пересечение между zeroblock и youtubeUnblock:
    zeroblock                 : opera
    youtubeUnblock            : YouTube
    Домены: googlevideo.com youtube.com 

  zeroblock              awg10 (vpn): meta,tiktok
uci: Entry not found
  zeroblock             opera (prx ): geoblock,block,youtube
  Версия zeroblock: 0.6.2-r91
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.45 | RAM: 44% | NAND: 23% занято / 51.7M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

root@RouteRich:~#

---

**2026-02-16T20:53:54 | Максим**
Вроде бы понял про стратегии. Подскажите, можно ли —lua списком вставить или нужно по одной? В доке вижу 30.5. Комбинированная стратегия
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=fake:blob=tls_clienthello:tcp_md5:tcp_seq=-10000
--lua-desync=fakeddisorder:pos=10,midsld:seqovl=336
Принцип: Fake + обратный порядок + sequence overlap.
то есть несколько

---

**2026-02-16T20:56:21 | Роман**
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
Откопал из секретных архивов )

---

**2026-02-16T22:25:01 | Павел Великов**
Получил RouteRich 24.10.5
Установил Zeroblock - включил Amnezia, Opera
При диагностике обнаружены проблемы
  FakeIP (клиент)  Не удалось проверить: Failed to fetch
  Другая маркировка  youtubeUnblock

норм или нет?
Часть сервисов meta открывается, youtube не грузит
Как корректно настроить?

---

**2026-02-16T22:32:50 | Павел Великов**
Ребут починил youtubeunblock, а вот FakeIP - нет)

---

**2026-02-16T22:39:17 | Andrey**
У меня тоже не работает fakeip, хотя на том же 2ip он нормально подменяется на ip vps. Хз он ваще должен на vless собственном работать или нет. Хотя по словам фресы, у меня вообще ничего работать не должно😁

---

**2026-02-16T22:50:23 | Den**
В РР заходите с компа или со смартфона? У меня на компе все норм, а со смартфона FakeIP в диагностике Failled to fetch.

---

**2026-02-17T09:56:42 | Максим**
Вот так оставил для LG
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=21
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=21
--lua-desync=multisplit:pos=2,sld:seqovl=2108:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=21:final

---

**2026-02-17T10:06:54 | Routerich**
30.5. Комбинированная стратегия
Принцип: Fake-пакет с неверной контрольной суммой. Сервер отбросит, DPI может принять.
Принцип: Разбиение на части и отправка в обратном порядке.

--out-range=-s34228
--payload=tls_client_hello
--lua-desync=fake:blob=tls_clienthello:tcp_md5:tcp_seq=-10000
--lua-desync=fakeddisorder:pos=10,midsld:seqovl=336

---

**2026-02-17T20:51:43 | Alexey**
не, эти нули есть в дефолтном 'youtube' и варп больше не пробивает. помогло вот это - --lua-desync=hostfakesplit:tcp_md5:host=ozon.ru

---

**2026-02-17T21:57:43 | Routerich**
обычного fake достаточно

---

**2026-02-18T01:12:43 | Андрей**
 config section 'igareck'
  option connection_type 'proxy'
  option proxy_config_type 'subscription'
  option subscription_url 'https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/BLACK_VLESS_RUS_mobile.txt'
  option urltest_check_interval '60m'
  option urltest_tolerance '50'
  option urltest_testing_url 'https://www.gstatic.com/generate_204'
  option enable_mixed_proxy '1'
  option mixed_port '2081'
  option disable_fakeip '0'
  option user_domain_list_type 'dynamic'
  option user_subnet_list_type 'disabled'
  option enabled '1'
  list user_domains 'q.co'
  list user_domains '2ip.ru'
  list user_domains '2ip.io'
  list user_domains 'qms.ru'

---

**2026-02-18T18:56:50 | Дмитрий Витальевич**
Здравствуйте! Подскажите почему может не проходить проверку FakeIP? Пробовал и перезагружать и искал ютубанблок как рекомендовали выше ( он не установлен), но все равно не проходит.

---

**2026-02-18T19:49:12 | Ａｌｅｘａｎｄｅｒ**
Есть несколько моментов после установки, не знаю баги это или нет..
при общей диагностики выявилось следующее
1. Вопрос, устанавливать ли DNS Failsafe Proxy? Или там и без него днс маршрутизируется
2. Проверку FakeIP не прошел со стороны клиента. Пишет NetworkError when attempting to fetch resource.

---

**2026-02-18T20:03:34 | Ａｌｅｘａｎｄｅｒ**
да что-тo он сам не подтягивает. Установил ручками
а что по поводу fakeip? есть решение?

---

**2026-02-18T20:13:52 | Bullet for my valentine Poison**
--payload=tls_client_hello
--lua-desync=fake:blob=blob_tls_clienthello_google:badseq:badseq_incr=1000000:repeats=6

--payload=quic_initial
--lua-desync=fake:blob=blob_quic_initial_google:anyproto:autottl=2:repeats=9:cutoff=n2
думаешь это верно?

---

**2026-02-18T23:23:35 | Роман**
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1

--payload=tls_client_hello 
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1

---

**2026-02-18T23:24:14 | Святос**
Вот например из zapret2 дискорд
--new
--filter-tcp=80,443,1080,2053,2083,2087,2096,8443
--hostlist=/opt/etc/nfqws2/lists/discord.list
--out-range=-d10
--lua-desync=hostfakesplit_multi:hosts=google.com,vimeo.com:tcp_ts=-1000:tcp_md5:repeats=2

---

**2026-02-18T23:50:51 | Bullet for my valentine Poison**
--lua-desync=fake:blob=tls_clienthello:tcp_badsum:tcp_seq=-10000:repeat=4
 --lua-desync=multisplit:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
2-й вариант
--lua-desync=fake:blob=fake_default_tls:badsum:tls_mod=sni=max.ru:repeat=6
--lua-desync=multidisorder:pos=host+1

попробуйте так. Но я бы еще насканил, чтобы было больше по типу разных.

---

**2026-02-19T00:20:09 | Роман**
--lua-desync=hostfakesplit:midhost=host-2:host=rzd.ru:tcp_seq=0:tcp_ack=-66000:badsum
Просто 1 стратегия. 
Можно добавить (я думаю) ещё  --payload=tls_client_hello.

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

**2026-02-19T10:39:49 | Petr Shcherbinin**
подскажите, пожалуйста
есть goodreads.com, они банят по рф адресам

я в zb добавил домен в секцию (она уменя одна, там влесс ключ платнтого внп)

goodreads.com не открывается, в логах yacd:
[2696696371 0ms] dns: exchange failed for www.goodreads.com. IN HTTPS: only IP queries are supported by fakeip

проверил в терминале роутера:

root@RouteRich:~# nslookup goodreads.com 127.0.0.42
Server:         127.0.0.42
Address:        127.0.0.42:53


Name:   goodreads.com
Address: 198.18.0.27

root@RouteRich:~#

---

**2026-02-19T14:24:19 | Lelik**
--lua-desync=circular:fails=2:maxtime=60
--lua-desync=circular:fails=2:time=60 \
--lua-desync=fake:blob=quic_google:repeats=7 \
--lua-desync=fake:blob=quic_google:repeats=6

---

**2026-02-19T14:26:49 | Lelik**
Соменваюсь что стратегия уровня
-out-range=-s34228--in-range=-s5556--lua-desync=circular:fails=2:maxtime=60--in-range=x--payload=tls_client_hello--lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=1--lua-desync=multisplit:pos=2,sld:seqovl=620:strategy=1--lua-desync=fake:blob=0x00000000:tcp_ack=-66000:strategy=2--lua-desync=multisplit:pos=2,endhost:strategy=2--lua-desync=multisplit:pos=1:seqovl=681:ip_id=zero:strategy=3
Так же настраивается и для UDP

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

**2026-02-19T16:17:58 | ALT F4**
Добрый день всем, вопросик. Роутер последней поставки, поставил скрипт №5 (вари ант с автогенерацией варп). Указал в секции подкопа Youtube_Discord -  HODCA. Это норма что whois сервис 2ip.ru видит моего провайдера как cloudflare? Дело в fakeip или маршрутизации awg интерфейса?

---

**2026-02-19T16:43:27 | Камиль**
Когда повторится проблема сделаю. Сейчас fakeip перехватывает 
ПК
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
Name:   chatgpt.com
Address: 198.18.0.62
Router
Server:    127.0.0.1
Address:  127.0.0.1:53

Name:  chatgpt.com
Address: 198.18.0.62

---

**2026-02-19T16:54:36 | Rom@n**
т.е. не через FakeIP

---

**2026-02-19T16:56:22 | Станислав Земляков**
--payload tls_client_hello --lua-desync=fake:blob=fake_default_tls:tcp_ts=-1000

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

**2026-02-19T18:41:29 | Anna Bagler**
Fakeip - что-то мешает на устройстве потенциально. Перенаправление DNS ругаться не должны, если вы до этого ничего с ними не делали.

---

**2026-02-19T18:44:38 | Routerich**
отключите fakeip на этой секции

---

**2026-02-19T18:53:10 | Rom@n**
Вообще странно с отключенным fakeip домен в дерект улетает

---

**2026-02-19T18:57:55 | Maxim =)))**
Осталось только - ⚠️  FakeIP (клиент)  Не удалось проверить: Failed to fetch

---

**2026-02-19T19:10:02 | HiLLL**
Фреса, зачем FakeIP откличен по дефолту в сеции awg? Редко когда надо отключать, кому надо сам отключет.

---

**2026-02-19T19:17:10 | Anna Bagler**
Что с галочками fakeip в секциях?

---

**2026-02-19T19:21:01 | Anna Bagler**
Настройки галочек fake IP по секциям. Подозреваю, что вы fakeip отключили.

---

**2026-02-19T19:23:06 | Maxim =)))**
Галку на Fake ip оставляю и выбираю сервисы, верно?

---

**2026-02-19T19:37:08 | Anna Bagler**
По скрину выше должен быть ответ по fakeip. Не образайте вывод.

---

**2026-02-19T19:40:21 | Anna Bagler**
У вас не срабатывает fakeip, поэтому и не ходит на запрещенку. Точно галочки сняты в настройках?

---

**2026-02-19T20:03:26 | Anna Bagler**
У вас раньше его там не было. Запрет2 тогда отключайте. У вас не срабатывает fakeip. Делать сброс вы не хотите. Если Fresa захочет, посмотрит.

---

**2026-02-19T20:20:21 | Maxim =)))**
⚠️  FakeIP (клиент)  Не удалось проверить: Failed to fetch

Тоже слетел

---

**2026-02-19T20:22:23 | Maxim =)))**
FakeIP (клиент)  Не удалось проверить: Failed to fetch

---

**2026-02-19T20:48:24 | Maxim =)))**
Зашибись, ребутнул роутер отключив на нем IPV6 и все, перестал FakeIP (клиент) работать

---

**2026-02-19T20:53:48 | Bullet for my valentine Poison**
не, мы там обсуждали момент когда в скобках пишется (fake_default_tls, "rnd") и нахрена.😂 А изначально же тыкал в нее циркуляркой для udp. Короче все смешалось в кучу)

---

**2026-02-19T21:01:26 | Anna Bagler**
Не работает fakeip.

---

**2026-02-20T07:40:17 | Дмитрий Витальевич**
Списки никакие не применял, хочу весь трафик гнать через одну секцию с подпиской. Еще пробовал FakeIP отключать. Это нужно для обхода БС. Жаль что нельзя секцию включать по времени, днем когда ограничений нет, работало бы через основные секции, а вечером допустим в 20:00 переходило на секцию с подпиской))

---

**2026-02-20T09:25:58 | Routerich**
на первой же странице гугла есть ответ
При использовании FakeIP (когда DNS возвращает фиктивные локальные IP, например, 198.18.0.0/15) CORS-политика браузера продолжает действовать, так как она проверяет домен/порт, а не реальный IP. Ошибка «CORS error» возникает, если запрос идет с site.com на 198.18.x.x (FakeIP), а сервер не вернул заголовок Access-Control-Allow-Origin

---

**2026-02-20T09:29:26 | Azizkhan**
ну так по этой причине не работает сервис, как это побороть?) отключить полностью fakeip? тогда другие вещи перестанут ведь работать

---

**2026-02-20T09:31:11 | Routerich**
создайте ему отдельную секцию без fakeip или настройте браузер отключив защиту

---

**2026-02-20T10:41:52 | Kiss_My_Axe**
Создаёте секцию "Указанные сайты".
Указываете канал, через который указанные сайты должны ходить в инет.
Указываете в секции "Указанные сайты" указанные сайты.
Секцию "Указанные сайты" размещаете в самом верху.

Под ней создаёте секцию "Всё остальное".
В ней только канал выхода устанавливаете, ну и может FakeIP включить/выключить, что нужно.
Сохранить, Применить.

---

**2026-02-20T11:56:05 | Bullet for my valentine Poison**
смысл есть комбинировать, fake с блобом и multidisorder/multisplit. Это пока то что я на практике увидел. Но опять же, мне это нужно разобрать для полного понимания.
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost вот тут к примеру мне нужен разбор конкретный. "pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost" - что это, для чего, почему именно такой порядок и куда я могу это припихнуть. И с чем еще можно скомбинировать.😅 Так что я пойду дальше мучить копилота в режиме учебник.

---

**2026-02-20T16:59:54 | Kiss_My_Axe**
В секции awg10 попробовать включить fakeip.

---

**2026-02-21T00:23:50 | это губер**
Только по Fake ip client

---

**2026-02-21T00:24:56 | Bullet for my valentine Poison**
Логи. Fake ip проверяйте ваш браузер. Частный/безопасный днс отрубайте.

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

**2026-02-21T13:48:26 | dirtybiker**
tailscale up \ 
 --netfilter-mode=off (и прочие флаги опционально). А интерфейс можно и в luci создать в интерфейсах и разрешить ему там лан ван опционально. Если вообще без него не пойдёт. У меня на 10.5 синг дропал без добавления, на 10.4 - штиль, и без интерфейса стабильно держалось. А в подкопе не знаю меню люси, я в 10.5 зверобоок накатил и ему сказал  чтоб пускал все, что без fakeip

---

**2026-02-21T16:02:27 | Андрей**
⚠️  FakeIP (клиент)  Не удалось проверить: Failed to fetch  из за этого обход не работает

---

**2026-02-21T20:06:26 | Роман**
Я не знаю как у тебя настроено, но у меня завелось только такого вида твоя стратегия:
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN
--lua-desync=multidisorder:pos=2,midsld:seqovl=1:seqovl_pattern=fake_default_tls

---

**2026-02-21T20:17:33 | Bullet for my valentine Poison**
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=fake_default_tls:badsum:tls_mod=sni=rzd.ru:repeat=6

---

**2026-02-21T21:45:10 | Александр**
Нет компа для проверки.

Вот всё с чистого листа.
В VPN что сделано:
Добавлена подписка и поставлена галка на "Отключить FakeIP"

В RU VLESS: Поставлена галка на "Отключить FakeIP", выбран список YouTube.

Всё. Телефон ходит в сеть без обходов, Web YouTube не грузит. Сайты определения IP определяют мою локацию.

Что дальше нужно сделать?

---

**2026-02-21T22:02:22 | Yury Kuzmenko**
Так конечно сайты определяет у вас была врублена галка выключить fake ip. Секция без доменов ловила все
Теперь вы галку убрали, добавили домен и секция гоняет через впн только этот домен. Вот для сравнения добавьте сейчас 2ip.io откройте в инкогнито

---

**2026-02-21T22:12:35 | Yury Kuzmenko**
В обоих местах проверяете чтобы не было галки fake ip все тогда должно заработать

---

**2026-02-21T23:44:31 | Владимир Волков**
Мне походу нужен краткий ликбез по fakeip - несколько часов коту под хвост, не пойму, почему тейл никак не хочет работать с подкопом 7.14

---

**2026-02-22T05:16:02 | Oleg Mi**
Попробуйте убрать в настройках секции галочку с «Disable FakeIP»
У меня на секции с awg10 ютуб тоже долго прогружался и тормозил только на айфоне. Галочку убрал уже пару дней все норм

---

**2026-02-22T11:02:20 | HiLLL**
Если вы ставили списки в awg10, то там  надо еще снять галку с Отключить FakeIP и и отключить днс . А так да проблема с сидорами есть.

---

**2026-02-22T12:28:44 | Routerich**
я  исследую, но думаю дело в том что полное исключение клиента создаёт правило для непопадание трафика клиента в tproxy, а catch-all подразумевает попадание всего трафика. и получается то что елиент исключен из тпрокси, но его запросы попадают в сингбокс, тот резолвит их в fakeip и они не могут никуда выйти, потому что такого в интернетах не существует

---

**2026-02-22T17:50:38 | Владимир Волков**
Объяснишь в пяти словах, как заполняются нфт сеты при отключенном fakeip на авг?
nslookup myip.com (добавлен в авг) возвращает 198.18.1.56, выглядит как фейкайпи.
А в каждом сэте авг прописан 198.18.1.0/24.
Я чёт осознать не могу, почему вообще вижу фейк

---

**2026-02-22T18:33:12 | Kirill Y**
Подскажите пожалуста, в разделе zeroblock -awg10- отключить fakeIP галка должна стоять или нет?

---

**2026-02-22T18:33:43 | Routerich**
так на авг нет fakeip из коробки. вы мне из разных секций чтоли фоточки делаете?

---

**2026-02-22T18:51:07 | Routerich**
а в fakeip cache 60

---

**2026-02-22T21:17:04 | Владимир Волков**
Интересно, что с fakeip на опере сайты-чекеры возвращают ипв6 адрес, а без фейка - ипв4. Но тейл маршрутизируется в обоих случаях

---

**2026-02-22T21:26:54 | Владимир Волков**
1) Прошить/сбросить роутер
2) Настроить тейл (прям запустить его и проверить ноду на телефоне)
3) Поставить Зероблок (тут я словил json ошибки, попробовал поставить через терминал, а он написал, что стоит)
4) В ЗБ в автоконфиге поставить галочку на оперу и авг - сохранить - применить - попить чай 10 минут - вернуться, увидеть, что авг не встал, а опера есть
5) В ЗБ в автоконфиге поставил галочку на автосекции, сохранил, применил, попил чай пару минут, убрал галочку с автосекций
6) Перейти во вкладку роутинга, вписать myip.com и ifconfig.me в юзерлисты оперы, поставить тут же галочку на выключение fakeip (можно оставить пустой, но для чистоты эксперимента я б поставил) - сохранить - сохранить - применить - попить чай
7) Проверить ноду на телефоне (без запретов)
8) В Настройках ЗБ добавить интерфейс тейла, поставить галочку под ним на проксирование трафика роутера - сохранить - применить - попить чай
9) nslookup myip.com - вернул не фейковый адрес
10)  nft list ruleset | grep -A 6 user_text
адрес myip.com из п.9 добавился как элемент сэта
11) Проверить ноду на телефоне, открыть на нём myip.com и посмотреть, открывается ли, домашний там адрес или нидерланды
12) ⚡️⚡️⚡️В С Ё ⚡️⚡️⚡️(или нет)

---

**2026-02-22T21:34:50 | Routerich**
у вас нет fakeip поэтому диагностика и считает это проблемой, на деле проблем нет

---

**2026-02-22T21:36:15 | Viktor**
Всё работало отлично, вдруг перестал Ютуб работать везде, никак не могу понять в чем проблема, диагностика пишет, что не перенаправляется Dns и с FakeIp проблема какая то

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

**2026-02-22T23:33:23 | Anna Bagler**
Согласно этому не в main. Но у вас проблема с fakeip. Что-то мешает.

---

**2026-02-22T23:35:55 | ㅤㅤHer01n 4dd1ct10n**
Прокси трафик не маршрутизируется через Fakeip

---

**2026-02-23T10:38:52 | vladimir**
Ну подскажите на что мета и fake ip ругаются

---

**2026-02-23T21:44:05 | Михаил**
Всем привет!
0.6.4-r46, в секции с ВПН забугорным стоит AI, геоблок и прочие сервисы, fakeip вкл. ChatGPT не пускает к себе. Если на ПК через VPN клиент весь трафик гоню(VPS юзается та же, что и в секции), то все отлично открывается. Пытался ручками добавить домены/сабдомены, результат нулевой. Есть идеи как пофиксить?

---

**2026-02-23T21:52:06 | isinva**
Я пробовал: влючать/отключать автонастройки, разные версии ip, fakeip включать/отключать, естественно чистил все кэши, перезагружал все устройства - пофиг. Сайт telegram.org попадает в yacd, остальное нет.

---

**2026-02-23T22:07:03 | Yury Kuzmenko**
А с точки зрения процесса почему yacd пишет прямой доступ, а nslookup fake ip показывает или это сложно?

---

**2026-02-23T22:20:33 | Routerich**
тут только fakeip спасет

---

**2026-02-23T22:21:13 | Routerich**
использовать fakeip для своей секции или не использовать cidr(но скорее всего не поможет)

---

**2026-02-23T22:21:59 | Rom@n**
для awg10? Просто ведь не рекомендовалось в инструкции для нее fakeip

---

**2026-02-23T22:24:44 | isinva**
С отключенным fakeip тг работает как полагается, но отваливается например devolutions.com, f1tv.formula1.com На v1 работает все в одной куче.

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

**2026-02-24T00:32:21 | kk**
[singbox_gen] Added loopback protection rule
[sing_box_routing] >>> ENTER sing_box_cm_add_route_rule()
[sing_box_routing] Added route rule idx=4 -> outbound=direct-out
[sing_box_routing] <<< EXIT sing_box_cm_add_route_rule() -> 4
[singbox_gen] Added FakeIP check route rule -> direct-out (override to 127.0.0.1)
[singbox_gen] >>> ENTER collect_vpn_endpoints()
[singbox_gen] No WG/AWG endpoints found
[singbox_gen] <<< EXIT collect_vpn_endpoints() -> 0
[singbox_gen] Proxy endpoint IP: 111.222.333.444 (parsed from vless-TEST)
[singbox_gen] >>> ENTER add_vpn_endpoint_bypass()
[sing_box_routing] >>> ENTER sing_box_cm_add_route_rule()
[sing_box_routing] Added route rule idx=5 -> outbound=direct-out
[sing_box_routing] <<< EXIT sing_box_cm_add_route_rule() -> 5
[singbox_gen] Added VPN endpoint bypass route rule (IPs: 1, domains: 0)
[singbox_gen] <<< EXIT add_vpn_endpoint_bypass() -> 0
[singbox_gen] Added bypass rules for 1 VPN/Proxy endpoint(s)

не видит AWG endpoints (awg10, 162.159.192.1)
vless-TEST норм - inbound=tproxy-in ip_cidr=111.222.333.444/32 route(direct-out)

---

**2026-02-24T01:05:56 | Routerich**
я нашёл проблему попадания ресурсов в тпрокси, которые ошибочно резолвились в fakeip, дело было в fakeip в самих списках

---

**2026-02-24T01:19:47 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.6.4-r64:
  Исправления:
  - Исправлена dns петля для fully routed в секции c отключенным fakeip
  - Исправлено некорректная запись пользовательских доменов/подсетей
#ZeroBlock

---

**2026-02-24T13:07:33 | Роман**
А если эту стратегию? Только старую сохранить.

  --payload=tls_client_hello
  --in-range=-s5556 --lua-desync=circular:fails=3:maxtime=60
  --in-range=x
  --lua-desync=multisplit:seqovl=681:seqovl_pattern=blob_stun:strategy=1
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=fonts.google.com:strategy=2
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=2
  --lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=2
  --lua-desync=fake:blob=blob_tls_clienthello_t2_ru:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=m.ok.ru:strategy=3
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=3
  --lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=3
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:strategy=4
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=google.com:strategy=4
  --lua-desync=multisplit:pos=2,sld:seqovl=2108:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=4
  --lua-desync=fake:blob=blob_stun:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=5
  --lua-desync=fakeddisorder:pos=1:pattern=blob_tls_clienthello_www_google_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=5
  --lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=6
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=7
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=7
  --lua-desync=multisplit:pos=2,sld:seqovl=620:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=7
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=8
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=8
  --lua-desync=multisplit:pos=2,sld:seqovl=620:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=8
  --lua-desync=hostfakesplit:host=mapgl.2gis.com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=9
  --lua-desync=fake:blob=blob_tls_clienthello_www_4pda_to:optional:tcp_ts=-600000:tls_mod=none:strategy=10
  --lua-desync=fake:blob=blob_stun:optional:tcp_seq=0:tcp_ack=-66000:badsum:strategy=11
  --lua-desync=multisplit:pos=1:seqovl=654:seqovl_pattern=blob_stun:strategy=11
  --lua-desync=hostfakesplit:midhost=host-2:host=i2.photo.2gis.com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=12
  --lua-desync=multisplit:pos=1:seqovl=582:seqovl_pattern=blob_stun:strategy=13:final

---

**2026-02-24T13:51:04 | Routerich**
а включи fakeip для секции и проверь

---

**2026-02-24T21:15:50 | Роман**
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN
--lua-desync=multidisorder:pos=2,midsld:seqovl=1:seqovl_pattern=fake_default_tls

Эту стратегию попробуйте.

---

**2026-02-25T00:26:53 | HiLLL**
Разобрался. Не работает с FakeIP. А хотелось бы. Отключил и полетело. Закинул all ссылку для теста, буду наблюдать.

---

**2026-02-25T16:13:56 | Routerich**
если использовать без fakeip и роутинга по ип, может ещё и прокатит

---

**2026-02-26T00:13:35 | Den**
Thu Feb 26 00:05:15 2026 user.notice sing-box: +0000 2026-02-25 21:05:15  [31mERROR [0m [ [38;5;77m2729413437 [0m 0ms] dns: exchange failed for 2ip.ru. IN HTTPS: only IP queries are supported by fakeip
Thu Feb 26 00:05:15 2026 user.notice sing-box: +0000 2026-02-25 21:05:15  [31mERROR [0m [ [38;5;77m2729413437 [0m 0ms] router: process DNS packet: only IP queries are supported by fakeip
Thu Feb 26 00:05:16 2026 user.notice sing-box: +0000 2026-02-25 21:05:16  [31mERROR [0m [ [38;5;123m3983046251 [0m 0ms] dns: exchange failed for www.bestsecret.com. IN HTTPS: only IP queries are supported by fakeip
Thu Feb 26 00:05:16 2026 user.notice sing-box: +0000 2026-02-25 21:05:16  [31mERROR [0m [ [38;5;123m3983046251 [0m 0ms] router: process DNS packet: only IP queries are supported by fakeip
Thu Feb 26 00:05:18 2026 user.notice sing-box: +0000 2026-02-25 21:05:18  [31mERROR [0m [ [38;5;44m1848337651 [0m 3ms] dns: exchange failed for picture.bestsecret.com. IN HTTPS: only IP queries are supported by fakeip
Thu Feb 26 00:05:18 2026 user.notice sing-box: +0000 2026-02-25 21:05:18  [31mERROR [0m [ [38;5;44m1848337651 [0m 4ms] router: process DNS packet: only IP queries are supported by fakeip
Thu Feb 26 00:05:18 2026 user.notice sing-box: +0000 2026-02-25 21:05:18  [31mERROR [0m [ [38;5;28m2063617548 [0m 0ms] dns: exchange failed for acq-api-prod.bestsecret.com. IN HTTPS: only IP queries are supported by fakeip
Thu Feb 26 00:05:18 2026 user.notice sing-box: +0000 2026-02-25 21:05:18  [31mERROR [0m [ [38;5;28m2063617548 [0m 0ms] router: process DNS packet: only IP queries are supported by fakeip
Thu Feb 26 00:07:58 2026 user.notice sing-box: +0000 2026-02-25 21:07:58  [31mERROR [0m [ [38;5;227m1457613275 [0m 0ms] dns: exchange failed for www.bestsecret.com. IN HTTPS: only IP queries are supported by fakeip
Thu Feb 26 00:07:58 2026 user.notice sing-box: +0000 2026-02-25 21:07:58  [31mERROR [0m [ [38;5;227m1457613275 [0m 0ms] router: process DNS packet: only IP queries are supported by fakeip
Thu Feb 26 00:08:00 2026 user.notice sing-box: +0000 2026-02-25 21:08:00  [31mERROR [0m [ [38;5;87m3288113296 [0m 0ms] dns: exchange failed for picture.bestsecret.com. IN HTTPS: only IP queries are supported by fakeip
Thu Feb 26 00:08:00 2026 user.notice sing-box: +0000 2026-02-25 21:08:00  [31mERROR [0m [ [38;5;87m3288113296 [0m 0ms] router: process DNS packet: only IP queries are supported by fakeip
Thu Feb 26 00:08:00 2026 user.notice sing-box: +0000 2026-02-25 21:08:00  [31mERROR [0m [ [38;5;190m3009684265 [0m 0ms] dns: exchange failed for acq-api-prod.bestsecret.com. IN HTTPS: only IP queries are supported by fakeip
Thu Feb 26 00:08:00 2026 user.notice sing-box: +0000 2026-02-25 21:08:00  [31mERROR [0m [ [38;5;190m3009684265 [0m 0ms] router: process DNS packet: only IP queries are supported by fakeip
Thu Feb 26 00:11:13 2026 user.notice sing-box: +0000 2026-02-25 21:11:13  [31mERROR [0m [ [38;5;107m2318690139 [0m 0ms] dns: exchange failed for www.bestsecret.com. IN HTTPS: only IP queries are supported by fakeip
Thu Feb 26 00:11:13 2026 user.notice sing-box: +0000 2026-02-25 21:11:13  [31mERROR [0m [ [38;5;107m2318690139 [0m 0ms] router: process DNS packet: only IP queries are supported by fakeip

---

**2026-02-26T00:18:21 | Den**
отключил fakeip, пока работает все... на сегодня монолог закончен. спать...

---

**2026-02-26T00:20:16 | Routerich**
если без fakeip работает, а с ним нети, то это проблема клиентского утсройства, т.к. в yacd ничего, значит ваши запросы идут мимо сингбокса и он ничего не маршрутизирует

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

**2026-02-26T10:04:41 | HiLLL**
Спасибо. Теперь работает список подсетей ULR с FakeIP. Я этого джва года ждал👍

---

**2026-02-26T10:58:56 | kk**
в js - vpnProtoPattern и vpnProtoPattern - (...|pppossh) 
+ изменить генерацию имён инт-сов, чтобы из Luci в uci уходило
полное имя (pppossh-blablassh23, такое же как и в системе)
если нужен дебаг/ip a и тд. - пиши
p/s хочется  ssh как catchall использовать

проверял на таком конфиге. 
zeroblock.ssh1=section
zeroblock.ssh1.enabled='1'
zeroblock.ssh1.connection_type='vpn'
zeroblock.ssh1.interface='pppossh-ssh1'
zeroblock.ssh1.disable_fakeip='1'
zeroblock.ssh1.user_domain_list_type='text'
zeroblock.ssh1.user_subnet_list_type='disabled'
zeroblock.ssh1.user_domains_text='microsoft.com

---

**2026-02-26T12:03:21 | Routerich**
так значит fakeip выключен

---

**2026-02-26T12:05:36 | Yury Kuzmenko**
включен, другие сайты из списка AI в fake ip

---

**2026-02-26T12:18:37 | Yury Kuzmenko**
Так почему nslookup не показывает fake ip?

---

**2026-02-26T12:20:57 | Yury Kuzmenko**
так а что можно сделать, чтобы в fake ip ушло это все?

---

**2026-02-26T13:21:31 | Aleksei**
это нормальное состояние ZeroBlock? 
дашборд не грузится(
хотя по диагностике, всё зелёное, кроме FakeIP (клиент). И диагностика показывает пинг до VLESS-сервера

---

**2026-02-26T13:50:40 | Роман**
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN
--lua-desync=multidisorder:pos=2,midsld:seqovl=1:seqovl_pattern=fake_default_tls

Эту попробуйте для начала.

---

**2026-02-26T13:53:36 | Роман**
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1

---

**2026-02-26T15:06:42 | Bullet for my valentine Poison**
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN
--lua-desync=multidisorder:pos=2,midsld:seqovl=1:seqovl_pattern=fake_default_tls
И вот пример моей страты для дс. Сначала идет строка с фэйком, а потом строка с мультидисордером.

---

**2026-02-26T16:51:01 | M D**
[singbox_gen] Catch-all section opera: auto-disabled FakeIP (no exclusions)
[singbox_gen] Catch-all section opera has disable_fakeip but no DNS config, using dns-main

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

**2026-02-26T18:57:29 | Routerich**
Галочку с отключить fakeip уберите в секции awg10

---

**2026-02-26T21:42:54 | Den**
Добрый вечер. Помогите пожалуйста выявить/устранить причину, по которой блокируемые сайты открываются только с отключенным Fake IP в секции опера. Версия ZB последняя из шапки

---

**2026-02-26T22:30:16 | Routerich**
из 1 любой секции, где включен fakeip

---

**2026-02-27T09:02:16 | Инженер Проектировщик**
Приветствую! почему zeroblock не парсит подписку?

[zeroblock] Starting ZeroBlock... [subscription_parser] HTTP 500 from subscription server [singbox_gen] Catch-all section Liberty_VLESS: auto-disabled FakeIP (no exclusions) [singbox_gen] Catch-all section Liberty_VLESS has disable_fakeip but no DNS config, using dns-main [singbox_gen] Section Liberty_VLESS: no parsed proxies from subscription

Секция urltest работает нормально, но вот секция Подписка как будто не видит конфиги по ссылке, хотя они там есть и приложухи типа V2Ray по этим ссылкам все добавляют. 

Как решить этот вопрос?

---

**2026-02-27T09:07:22 | Инженер Проектировщик**
Приветствую! почему zeroblock не парсит подписку?

[zeroblock] Starting ZeroBlock... [subscription_parser] HTTP 500 from subscription server [singbox_gen] Catch-all section Liberty_VLESS: auto-disabled FakeIP (no exclusions) [singbox_gen] Catch-all section Liberty_VLESS has disable_fakeip but no DNS config, using dns-main [singbox_gen] Section Liberty_VLESS: no parsed proxies from subscription

Секция urltest работает нормально, но вот секция Подписка как будто не видит конфиги по ссылке, хотя они там есть и приложухи типа V2Ray по этим ссылкам все добавляют. 

Как решить этот вопрос?

---

**2026-02-27T11:31:48 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.6.4-r85:
  Исправления:
  - Маскирование чувствительных данных при выгрузке конфига из диагностики для пользовательских конфигов(custom fragment)
  - VPN интерфейсы в секциях теперь отображают pppossh
  - Извлечение uuid/password из query-параметров HTTP/HTTPS proxy URL(очередные "бесплатные" подписки)
  - catch-all секция без dns_type/dns_server теперь использует глобальный DNS (fallback работает для VPN и PROXY типов, не только VPN)
  - fakeip_query_type_filter UCI опция: добавляет query_type ["A","AAAA"] к DNS правилам направляющим в dns-fakeip (фильтрует HTTPS/SVCB запросы)

Если пользователю нужен FakeIP на catch-all — ему нужно добавить хотя бы один exclusion (excluded_ips или excluded_domains), тогда auto-disable не сработает.
#ZeroBlock

---

**2026-02-27T13:30:59 | Routerich**
что и как именно настроено что оно работает, что по fakeip?

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

**2026-02-27T16:01:44 | Routerich**
он отвечает мусором, на тот мусор что вы ему даёте. я уже писал что просто написать sni= не даст ничего потому что sni является параметром для fake

---

**2026-02-27T16:02:33 | Lelik**
да я уже пофиксил до
--dpi-desync-fake-tls-mod=sni=www.google.com
Так вроде правильно?

---

**2026-02-27T16:20:17 | Lelik**
Ну аналог на Zapret2ском как будет, не могу понять
--dpi-desync-fake-tls-mod=sni=www.google.com
По ману SNI нигде не фигурирует вроде, скорее всего не напрямую как-то указано

---

**2026-02-27T16:25:58 | Lelik**
Так?
--lua-desync=fake:tls_mod=rnd,dupsid,sni=google.com

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

**2026-02-28T14:34:21 | ㅤㅤ**
Все верно. По логам я подробно видел что происходит. Устройства выходили в сеть минуя fakeip на реальные адреса. В первую очередь глядел IPv6 и отсекал, но тщетно. DNS брали с роутера (192.168.1.1). Podkop все решил без танцев.

---

**2026-02-28T19:34:57 | Routerich**
если насчёт версии, я ещё могу поверить в кеш, то насчет сервера который якобы отвечает на запрос нет. у вас где-то настроено спрашивать dns у 1.1.1.1, а fakeip вы скорее всего получаете, потому что запросы перехватываются сингбоксом

---

**2026-02-28T20:10:31 | Routerich**
отключить fakeip уберите галку

---

**2026-03-01T02:42:05 | Kiss_My_Axe**
В общем суть проблемы.
Если на винде нет шлюза (как минимум для адресов IPv6), то системный резолвер... скрывает ответы ДН-сервера!
Вот такое вот, поражающее своею элегантностию решение было принято в Редмонде сразу по возвращению с одного интересного острова, видимо. Или даже на самом острове. Владелец того острова ещё в камере повесился потом. Вроде.

Отсюда - если провайдер не предоставляет IPv6, то роутер не зашлёт на клиента IPv6 шлюз (или если в интерфейсах удалили IPv6 wan, например). Следовательно винда скроет IPv6 адрес хоста от браузеров итп.
Из-за этого ДАЖЕ ПРИ НАЛИЧИИ на роутере вспомогательных интерфейсов с поддержкой IPv6 хосты, доступные исключительно по IPv6, открываться не будут. Ни ка гда.

Но в подкопе же работает! - скажете вы. Ну да, работает. Потому что у него ВСЕ обходы исключительно через fakeip, который всегда IPv4. Кроме случая работы через смешной прокси, да и то не уверен.

Итог сей басни: виндазклиенты не смогут работать с IPv6 без костылей. Которые ещё и придумать надо.

---

**2026-03-01T11:11:59 | Kiss_My_Axe**
Тут вот что вылезает, и это главное - ЗБ пока не умеет в IPv6 маршрутизацию-то...
Потому что если бы да, то ntc.party + fakeip + маршрут в корректный интерфейс (awg10) = открывается. Даже вообще без v6 на клиентском интерфейсе.
А он - не открывается.
Тут надо что-то сделать, потому что этот вопрос станет подниматься, применительно именно к вооон тому домену.

Допускаю, что проблема в - ZB пытается маршрутить в IPv4, а так как его нет, то и не маршрутит.
Или маршрут IPv6 пытается пропихать в IPv4 интерфейса, а роутер этому удивляется и отказывается.

---

**2026-03-01T12:39:33 | Zeal Tree**
Полный вывод такой, но думаю главное вот что 
⚠️ Zapret detected
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🥸 FakeIP status
❌ Failed to get FakeIP info
✅ Sing-box works with FakeIP: 198.18.0.7

---

**2026-03-01T14:04:34 | Routerich**
до тех пор пока клиент не увидит нормальный prefix delegation. клиент будет сам выбирать что спрашивать с роутера, это нереализуемо силами зероблока, при fakeip это работает внутри сингбокса, который сам делает fallback на ipv6

---

**2026-03-01T15:24:39 | Kiss_My_Axe**
Зайти в новосозданную секцию опера в зероблок. Снять галку "Отключить FakeIP"
Сохранить, Применить.

---

**2026-03-01T15:54:12 | Kiss_My_Axe**
Судя по IP фейсбука и ютуба у вас на Zeroblock не работает фейкайпи. Совсем.
В секции party точно снята галка "Отключить FakeIP"?

---

**2026-03-01T16:34:17 | Kiss_My_Axe**
В секции party точно снята галка "Отключить FakeIP"?
Снята!

---

**2026-03-01T17:46:33 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.6.4-r97:
  Исправления:
  - Исправлена работа dns_hijack для IPv6 fully_routed адресов и excluded IP. IPv6 fully_routed теперь корректно перенаправляются через redirect to :53 (dnsmasq), excluded клиенты получают реальные DNS-ответы.
  - Добавлены переводы и исправлена валидация IPv6 для user_subnets в веб-интерфейсе.
  - Утечка IPv6 при disable_fakeip — при dns_strategy=prefer_ipv4 и ipv6_enabled=0 sing-box мог возвращать AAAA-записи в dnsmasq, но nftset захватывал только IPv4 — IPv6-трафик шёл мимо туннеля. Теперь ZeroBlock автоматически добавляет AAAA reject DNS-правила, блокируя AAAA-ответы для disable_fakeip доменов.

Поясню про последнее, раньше при dns_strategy=prefer_ipv4 и ipv6_enabled=0 получать ipv6 резолвинг можно было, теперь нельзя. нужен резолвинг, ставим dns_strategy=prefer_ipv6
#ZeroBlock

---

**2026-03-01T18:00:34 | Routerich**
через оперу с fakeip ntc работает при prefer ipv6

---

**2026-03-01T18:08:57 | Anna Bagler**
У вас ругается на fakeip, что-то мешает. На смартфоне проверяли?

---

**2026-03-01T18:14:03 | Andrey**
А галка в секции на отключить fakeip снята или стоять должна? Или и так и так тестить?

---

**2026-03-01T19:41:02 | Routerich**
потому что авг без fakeip и пока вы не настроите правильно роутер, работать оно не будет, потому что работает на уровне системы, а не на уровне магии сингбокса

---

**2026-03-01T23:59:41 | Роман**
Попробуйте эту стратегию для запрет 2, старую сохраните.
  --payload=tls_client_hello
  --in-range=-s5556 --lua-desync=circular:fails=3:maxtime=60
  --in-range=x
  --lua-desync=multisplit:seqovl=681:seqovl_pattern=blob_stun:strategy=1
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=fonts.google.com:strategy=2
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=2
  --lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=2
  --lua-desync=fake:blob=blob_tls_clienthello_t2_ru:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=m.ok.ru:strategy=3
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=3
  --lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=3
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:strategy=4
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=google.com:strategy=4
  --lua-desync=multisplit:pos=2,sld:seqovl=2108:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=4
  --lua-desync=fake:blob=blob_stun:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=5
  --lua-desync=fakeddisorder:pos=1:pattern=blob_tls_clienthello_www_google_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=5
  --lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=6
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=7
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=7
  --lua-desync=multisplit:pos=2,sld:seqovl=620:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=7
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=8
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=8
  --lua-desync=multisplit:pos=2,sld:seqovl=620:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=8
  --lua-desync=hostfakesplit:host=mapgl.2gis.com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=9
  --lua-desync=fake:blob=blob_tls_clienthello_www_4pda_to:optional:tcp_ts=-600000:tls_mod=none:strategy=10
  --lua-desync=fake:blob=blob_stun:optional:tcp_seq=0:tcp_ack=-66000:badsum:strategy=11
  --lua-desync=multisplit:pos=1:seqovl=654:seqovl_pattern=blob_stun:strategy=11
  --lua-desync=hostfakesplit:midhost=host-2:host=i2.photo.2gis.com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=12
  --lua-desync=multisplit:pos=1:seqovl=582:seqovl_pattern=blob_stun:strategy=13:final

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

**2026-03-02T10:57:04 | kk**
проверил себя ещё раз. поведение не изменилось.
я пытаюсь показать, что в имени инт-са всегда будет "тип" (pppossh-blablabla, pppossh-pppOssh) и он обрезается. в данный момент всё сохранится, но работать не будет:
zeroblock.ssh1=section
zeroblock.ssh1.connection_type='vpn'
zeroblock.ssh1.interface='pppOssh'
zeroblock.ssh1.disable_fakeip='1'
zeroblock.ssh1.user_domain_list_type='text'
zeroblock.ssh1.user_domains_text='microsoft.com'
а должен быть zeroblock.ssh1.interface='pppossh-pppOssh'  (pppossh-всёчтоугоднотут)

---

**2026-03-02T13:55:44 | Routerich**
в секции отключить fakeip галку уберите

---

**2026-03-02T14:00:38 | Роман**
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN
--lua-desync=multidisorder:pos=2,midsld:seqovl=1:seqovl_pattern=fake_default_tls

--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1

Эти попробуйте.

---

**2026-03-02T14:01:33 | Lelik**
Эти тоже работать не будут, надо 
blob=fake_default_tls
менять

---

**2026-03-02T14:18:23 | Lelik**
--payload=tls_client_hello --lua-desync=multisplit:blob=fake_default_tls:tcp_seq=1000000:pos=2:nodrop:repeats=1 --lua-desync=multisplit:pos=2
Ну хорошо, а здесь можно просто заменить параметр
blob=fake_default_tls
На какой-то конкретный блоб и скорее всего заработает?

---

**2026-03-02T15:54:54 | Routerich**
я уже писал, fakeip и google play что мне ещё нужно написать?

---

**2026-03-02T15:57:23 | Routerich**
на скрине из yacd udp трафик, который затёк по причине резолвинга одного из доменов списка. тут только fakeip поможет

---

**2026-03-02T19:36:17 | HiLLL**
галку сверху FakeIP попробуйте выключить

---

**2026-03-02T20:08:17 | Лебедь**
Вот тут сказано про FakeIP
И на скрине так же 

Это пример правильной работы или наоборот?

---

**2026-03-02T21:48:00 | Routerich**
великая стратегия от самого известного должника @BFMVPoison, ходят легенды что на ней работает youtube на айфонах, телевизорах lg, пк и в редких случаях микроволновках
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4

---

**2026-03-02T23:41:59 | Kiss_My_Axe**
Наверное с записочком от Иван Иваныча в кармане ходите. Или на телефон её приклеили.
Шобы опсосы видели - не прост, далеко не прост Борис!
И такие - ну ладно, мы бы его и так пустили, но раз он хочет, то пусть думает, что fake-SNI до сих пор работает. :)

---

**2026-03-03T00:07:48 | Yury Kuzmenko**
Нет ну где то работает по крайней мере в комментах с подпиской писали что в части регионов только fake sni помогает но это супер редко

---

**2026-03-03T01:01:38 | Anna Bagler**
Ну так список ai в секции прокси есть? Fakeip для прокси не должен быть отключен.

---

**2026-03-03T02:32:50 | Борис**
Как мы уже выяснили, youTubeUnblock является инструментом для обхода DPI, который изменяет структуру и атрибуты сетевых пакетов. То, что у юаб есть стратегия "с фейк сни" — не значит, что с помощью этой программы наше устройство пытается "попасть на Ютуб", указывая другой домен (как мы обсуждали с vless reality, когда клиент подключается к туннелю-серверу, указывая поддельный sni). В обычном World Wide Web у вас не получится "зайти на сайт", указав неправильное имя для него — сервер с сайтом не поймёт такой запрос. У сервера есть только сайт youtube.com, а вы ему скажите "дай мне yandex.ru", он тебе ответит "ты куку? Тут такой не проживает."

Так как же это работало в youTubeUnblock и прочих? Очень просто. У сетевых пакетов есть такой атрибут, как ttl (time to live). Этот атрибут означает, сколько "прыжков" между сетевыми узлами пакет способен пережить. Так вот, YUB указывал в пакете sni = yandex.ru и при этом ttl = 3 (я не знаю сколько, но очень маленькое число). Таким образом ТСПУ был узлом #2 и он пускал такой трафик дальше, ведь яндекс для него — это круто и молодёжно. Но реальность в том, что пакет с таким sni умирал сразу после тспу, а до ютуба доходили уже "реальные" намерения человека — "дай мне youtube.com"

Эту лазейку с fake sni быстро прикрыли, так как провайдеру достаточно было выпустить небольшой патч, в котором проверялся не только sni, но и ttl пакета (чтобы сразу видеть, что ему пытаются скормить "обманку")

---

**2026-03-03T03:06:50 | Евгений Фролов**
Обязательно ли надо
zeroblock.WARP.disable_fakeip='1'
Для секции с туннелем awg10?

---

**2026-03-03T06:44:33 | ᅠ ᅠ**
Говорит, что устарел подкоп + FakeIP красный + outbounds не отвечает дискорд

---

**2026-03-03T15:36:32 | Routerich**
зероблок реализует 2 подхода, fakeip и системный резолвинг, для второго идеально plain text, через конвертацию json/srs

---

**2026-03-03T22:49:00 | Mallory**
спасибо, она мой мозг и сломала, например

29. Применение найденной стратегии
29.1. Через веб-интерфейс
...
3. В поле NFQWS Options вставьте параметры из SUMMARY:
--out-range=-s34228 --payload=tls_client_hello \ 
--lua-desync=fake:blob=tls_clienthello:tcp_md5 \ 
--lua-desync=multisplit:pos=midsld

Начнем с того, что я не нашел в блокчеке блока SUMMARY и кроме того, в нем идут строки без заголовка 
--out-range=-s34228 --payload=tls_client_hello

---

**2026-03-03T23:21:29 | Роман**
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN
--lua-desync=multidisorder:pos=2,midsld:seqovl=1:seqovl_pattern=fake_default_tls

--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1

--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1

---

**2026-03-03T23:27:27 | Святос**
--payload=tls_client_hello
--lua-desync=circular:fails=2:time=300:retrans=3:nld=2
# Strategy 1
--lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=fonts.google.com:tcp_seq=10000:strategy=1
--lua-desync=multisplit:pos=1,midsld:seqovl=1:seqovl_pattern=tls_clienthello:tcp_ts_up:strategy=1
# Strategy 2
--lua-desync=fake:blob=0x00000000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=www.google.com:repeats=2:strategy=2
--lua-desync=multisplit:pos=1,midsld:strategy=2
# Strategy 3
--lua-desync=hostfakesplit:host=ozon.ru:midhost=host-2:seqovl=sniext+3:seqovl_pattern=tls_clienthello:badsum:tcp_md5:tcp_ts_up:strategy=3
--lua-desync=hostfakesplit:tcp_md5:tcp_ts_up:strategy=3

---

**2026-03-03T23:30:32 | Bullet for my valentine Poison**
--out-range=-s34228
--payload=tls_client_hello
--in-range=-s5556 --lua-desync=circular:fails=2:time=60
--in-range=x
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN:strategy=1
--lua-desync=multidisorder:pos=2,midsld:seqovl=1:seqovl_pattern=fake_default_tls:strategy=1
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1:strategy=2
--lua-desync=multidisorder:pos=2,midsld:seqovl=1:seqovl_pattern=fake_default_tls:strategy=2
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1:strategy=3:final

---

**2026-03-04T00:20:56 | Mallory**
я только в начале пути
как я понял - для комби сначала идут мусорные fake (какое-то количество), затем затем рабочая стратегия

я не видел чтобы блокчек подбирал фейки, но я могу ошибаться

---

**2026-03-04T07:37:54 | Anna Bagler**
Со стороны роутера проблемы нет. Fakeip отрабатывает у proxy. Можете Мету возвращать назад. Ищите, что мешает в браузере.

---

**2026-03-04T09:29:04 | Anna Bagler**
Пинга нет по awg, вопрос был по geoblok в proxy и список ai вчера там был, fakeip по ним отрабатывал.
Ага, увидела и ниже.

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

**2026-03-04T14:13:43 | Azizkhan**
[zeroblock] ZeroBlock started successfully
[ [38;5;181m1834919333 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;50m253425145 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;150m467216518 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;119m1662764135 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;50m3655290361 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;117m4131448165 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;194m701229349 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;29m3549903076 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;157m749566093 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;225m4178729693 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;30m1059545573 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;32m2816918800 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;223m3921136392 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;117m1941428069 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;215m966124487 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;202m1526016442 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;226m1154021842 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;87m1127608135 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;169m2179646105 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;183m3941245095 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;185m123675049 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;29m1938556685 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;231m657839319 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;47m2577011743 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;46m3528291102 [0m 247ms] dns: exchange failed for static.doubleclick.net. IN HTTPS: unexpected status: 403 Forbidden
[ [38;5;46m3528291102 [0m 247ms] router: process DNS packet: unexpected status: 403 Forbidden
[ [38;5;138m2135953786 [0m 247ms] dns: exchange failed for static.doubleclick.net. IN A: unexpected status: 403 Forbidden
[ [38;5;138m2135953786 [0m 247ms] router: process DNS packet: unexpected status: 403 Forbidden
[ [38;5;76m3568988732 [0m 247ms] dns: exchange failed for static.doubleclick.net. IN HTTPS: unexpected status: 403 Forbidden
[ [38;5;76m3568988732 [0m 247ms] router: process DNS packet: unexpected status: 403 Forbidden
[ [38;5;220m2277636363 [0m 247ms] dns: exchange failed for static.doubleclick.net. IN A: unexpected status: 403 Forbidden
[ [38;5;220m2277636363 [0m 247ms] router: process DNS packet: unexpected status: 403 Forbidden
[ [38;5;70m3148671798 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;146m1281149826 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`
[ [38;5;79m2620033599 [0m 0ms] router: missing fakeip record, try enable `experimental.cache_file`

---

**2026-03-04T14:14:01 | Azizkhan**
почему может быть такой лог с missing fakeip record?

---

**2026-03-04T14:56:47 | Bullet for my valentine Poison**
--payload=tls_client_hello
--lua-desync=multisplit:blob=fake_default_tls:tcp_ts=-1000:pos=2:nodrop:repeats=2
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4
у кого там Роблокс под рукой. Чекните, запуск нормально идет?

---

**2026-03-04T17:49:28 | HiLLL**
Fresa, психанул? FakeIP по дефолту включен в секции awg. Оказалось консольщиков раз два и обчелся, а сколько гемороя было в чате из-за этой галки 👌

---

**2026-03-04T22:49:25 | Святос**
--payload=tls_client_hello,http_req
--lua-desync=hostfakesplit:host=ya.ru:midhost=host-4:altorder=0:badsum:md5sig:badseq:badseq_increment=0:ip_id=seqgroup:tcp_ts_up
--out-range=-n6 --new

---

**2026-03-04T23:19:31 | Routerich**
fakeip это по факту единственное преимущество в роутинге. остальные это поддержка всяких прокси ссылок и странных вещей по типу trust tunnel

---

**2026-03-05T09:15:22 | HiLLL**
а FakeIP включен?

---

**2026-03-05T09:21:05 | Aндрей**
В прокси выключена галочка fake ip

---

**2026-03-05T09:28:59 | Anna Bagler**
Список ai, если v2 в opera, fakeip должен быть, т.е. галочка снята. Если у вас своя конфигурация для awg с зарубежной локацией, тоже будет работать.

---

**2026-03-05T17:43:37 | Владимир Волков**
Если вы почистили секции, а добавили ключ на место оперы, то там галочка fakeip стоит. С ней Нидерланды показывают ипв6. Хз почему...

---

**2026-03-05T19:53:29 | Stas Ivanov**
А fakeIP в логах? Может надо его галочкой отключить?

---

**2026-03-05T19:55:14 | Routerich**
fakeip для catch-all отключается, в логах же написано

---

**2026-03-05T20:50:26 | HiLLL**
снимите галку с FakeIP

---

**2026-03-05T22:34:39 | Роман**
--payload=tls_client_hello
  --in-range=-s5556 --lua-desync=circular:fails=3:maxtime=60
  --in-range=x
  --lua-desync=multisplit:seqovl=681:seqovl_pattern=blob_stun:strategy=1
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=fonts.google.com:strategy=2
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=2
  --lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=2
  --lua-desync=fake:blob=blob_tls_clienthello_t2_ru:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=m.ok.ru:strategy=3
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=3
  --lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=3
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:strategy=4
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=google.com:strategy=4
  --lua-desync=multisplit:pos=2,sld:seqovl=2108:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=4
  --lua-desync=fake:blob=blob_stun:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=5
  --lua-desync=fakeddisorder:pos=1:pattern=blob_tls_clienthello_www_google_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=5
  --lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=6
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=7
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=7
  --lua-desync=multisplit:pos=2,sld:seqovl=620:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=7
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=8
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=8
  --lua-desync=multisplit:pos=2,sld:seqovl=620:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=8
  --lua-desync=hostfakesplit:host=mapgl.2gis.com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=9
  --lua-desync=fake:blob=blob_tls_clienthello_www_4pda_to:optional:tcp_ts=-600000:tls_mod=none:strategy=10
  --lua-desync=fake:blob=blob_stun:optional:tcp_seq=0:tcp_ack=-66000:badsum:strategy=11
  --lua-desync=multisplit:pos=1:seqovl=654:seqovl_pattern=blob_stun:strategy=11
  --lua-desync=hostfakesplit:midhost=host-2:host=i2.photo.2gis.com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=12
  --lua-desync=multisplit:pos=1:seqovl=582:seqovl_pattern=blob_stun:strategy=13:final

Эту попробуйте, старую стратегию сохраните.

---

**2026-03-06T07:18:14 | K**
великая стратегия от самого известного должника @BFMVPoison, ходят легенды что на ней работает youtube на айфонах, телевизорах lg, пк и в редких случаях микроволновках
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4

---

**2026-03-06T10:22:25 | Uintik️️️🐈‍⬛**
Добрый день всем. Подскажите судя по логу лег сайт для получения фэйк IP: Fri Mar 6 10:17:51 2026 user.notice ucitrack: Setting up /etc/config/zeroblock reload trigger for non-procd /etc/init.d/zeroblock
Fri Mar 6 10:18:03 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[singbox_gen] Catch-all section wg: auto-disabled FakeIP (no exclusions)
Fri Mar 6 10:18:07 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: udhcpc: started, v1.36.1
Fri Mar 6 10:18:07 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: udhcpc: broadcasting discover
Fri Mar 6 10:18:09 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: udhcpc: no lease, failing
[zeroblock] ZeroBlock started successfully
[clash_api] /wg/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 503
[clash_api] /wg/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 504
[clash_api] /wg/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 504
[clash_api] /wg/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 504
Fri Mar 6 10:20:00 2026 cron.err crond[7713]: USER root pid 8628 cmd /usr/bin/zeroblock bad_interface_check >/dev/null 2>&1

---

**2026-03-06T15:34:55 | Routerich**
fakeip?

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

**2026-03-06T18:15:51 | Роман**
--payload=tls_client_hello
  --in-range=-s5556 --lua-desync=circular:fails=3:maxtime=60
  --in-range=x
  --lua-desync=multisplit:seqovl=681:seqovl_pattern=blob_stun:strategy=1
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=fonts.google.com:strategy=2
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=2
  --lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=2
  --lua-desync=fake:blob=blob_tls_clienthello_t2_ru:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=m.ok.ru:strategy=3
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=3
  --lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=3
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:strategy=4
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=google.com:strategy=4
  --lua-desync=multisplit:pos=2,sld:seqovl=2108:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=4
  --lua-desync=fake:blob=blob_stun:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=5
  --lua-desync=fakeddisorder:pos=1:pattern=blob_tls_clienthello_www_google_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=5
  --lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=6
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=7
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=7
  --lua-desync=multisplit:pos=2,sld:seqovl=620:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=7
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=8
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=8
  --lua-desync=multisplit:pos=2,sld:seqovl=620:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=8
  --lua-desync=hostfakesplit:host=mapgl.2gis.com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=9
  --lua-desync=fake:blob=blob_tls_clienthello_www_4pda_to:optional:tcp_ts=-600000:tls_mod=none:strategy=10
  --lua-desync=fake:blob=blob_stun:optional:tcp_seq=0:tcp_ack=-66000:badsum:strategy=11
  --lua-desync=multisplit:pos=1:seqovl=654:seqovl_pattern=blob_stun:strategy=11
  --lua-desync=hostfakesplit:midhost=host-2:host=i2.photo.2gis.com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=12
  --lua-desync=multisplit:pos=1:seqovl=582:seqovl_pattern=blob_stun:strategy=13:final

Поробуйте эту стратегию, старую сохранить на всякий случай.

---

**2026-03-07T04:11:30 | twiNn**
fakeip почему то не использует браузер, хотя вчера всё было хорошо.

---

**2026-03-07T04:38:12 | Anna Bagler**
fakeip отрабатывает. Попробуйте в браузере, который обычно не используете.

---

**2026-03-07T11:03:55 | Anna Bagler**
Галка на отключение fakeip есть?

---

**2026-03-07T11:04:48 | Aндрей**
зачем мне fake ip включать? или я туплю

---

**2026-03-07T11:17:35 | Aндрей**
1. убрал галочку "отключить fake ip"
2. перезапустил зероблок
3. открыл инкогнито в новом браузере гпт

---

**2026-03-07T11:52:04 | Роман**
--payload=tls_client_hello
  --in-range=-s5556 --lua-desync=circular:fails=3:maxtime=60
  --in-range=x
  --lua-desync=multisplit:seqovl=681:seqovl_pattern=blob_stun:strategy=1
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=fonts.google.com:strategy=2
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=2
  --lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=2
  --lua-desync=fake:blob=blob_tls_clienthello_t2_ru:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=m.ok.ru:strategy=3
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=3
  --lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=3
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:strategy=4
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=google.com:strategy=4
  --lua-desync=multisplit:pos=2,sld:seqovl=2108:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=4
  --lua-desync=fake:blob=blob_stun:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=5
  --lua-desync=fakeddisorder:pos=1:pattern=blob_tls_clienthello_www_google_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=5
  --lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=6
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=7
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=7
  --lua-desync=multisplit:pos=2,sld:seqovl=620:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=7
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=8
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=8
  --lua-desync=multisplit:pos=2,sld:seqovl=620:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=8
  --lua-desync=hostfakesplit:host=mapgl.2gis.com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=9
  --lua-desync=fake:blob=blob_tls_clienthello_www_4pda_to:optional:tcp_ts=-600000:tls_mod=none:strategy=10
  --lua-desync=fake:blob=blob_stun:optional:tcp_seq=0:tcp_ack=-66000:badsum:strategy=11
  --lua-desync=multisplit:pos=1:seqovl=654:seqovl_pattern=blob_stun:strategy=11
  --lua-desync=hostfakesplit:midhost=host-2:host=i2.photo.2gis.com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=12
  --lua-desync=multisplit:pos=1:seqovl=582:seqovl_pattern=blob_stun:strategy=13:final

Попробуйте эту, старую сохранить.

---

**2026-03-07T18:34:47 | HiLLL**
галка снята с Отключить FakeIP?

---

**2026-03-08T08:26:24 | Grigory**
в чем может быть дело?
Версия: 0.7.0-r18
FakeIP (клиент) не проходит проверку в диагности и соответственно на устройствах не работает ничего

---

**2026-03-08T08:29:05 | HiLLL**
убрать галку в секции с Отключить FakeIP ?

---

**2026-03-08T08:30:08 | Dmitrii Burenin**
FakeIP точно включен?

---

**2026-03-08T08:35:02 | Anna Bagler**
Да, у awg можно fakeip отключить и посмотреть.

---

**2026-03-08T08:46:26 | Anna Bagler**
fakeip отрабатывает. В другом браузере смотрели? На смартфоне?

---

**2026-03-08T09:38:50 | HiLLL**
у берите галку в awg10 с Отключить FakeIP проверьте в инкогнито Ctrl+Shift+N

---

**2026-03-08T09:40:51 | Tox**
Там нет fakeip

---

**2026-03-08T13:32:59 | Владимир Волков**
На всём работает, если правильно настроено. Основные затыки встречал разве что с включением fakeip

---

**2026-03-08T21:50:37 | Inko**
ребят а что с fake ip случилось gemini отвалилась чет... пишет что не для нашей страны...

---

**2026-03-10T00:11:47 | m**
Светлый фон - десктопный Chrome. На последнем скрине: запустил диагностику из Safari iOS: там все зеленое кроме fake ip, он - желтым

---

**2026-03-10T09:01:08 | Yury Kuzmenko**
Интересно вообще почему ИИ считает что подкоп не умеет в Fake IP

---

**2026-03-10T11:25:45 | Yury Kuzmenko**
про отключение fake ip было только в начале там это со списком клауда связано но вроде фикс уже был

---

**2026-03-10T11:29:19 | Yury Kuzmenko**
да не было этого на общую тему, отключат fake ip надо было только для hodca и то это было 2 месяца назад

---

**2026-03-10T16:18:39 | @Dr.Medvedolog**
но при включении Proxy Router Traffic
Proxy router's own outgoing traffic for sections with Disable FakeIP. FakeIP sections always proxy router traffic automatically. - должен и opkg через Outband гулять?

---

**2026-03-10T16:45:51 | Routerich**
заблочен гит на вышестоящем. отакое имеем в списках, ибо я не знаю что там сейчас в ходке. получаем отлуп по спискам. получаем секцию и переключаемся, скачиваем. опкг работает, если fakeip на секции, проксирует сам

---

**2026-03-10T16:47:55 | Роман**
Нет, не поэтому. Браузер не использует fake ip, что-то мешает. Проведите тест на смартфоне отключив частный DNS.
И не пишите не ра-бо-та-ет, это триггер для бота.

---

**2026-03-10T23:27:51 | Владимир Волков**
Это уже вопросы к настройке Ютуба, через что он идёт и как. Может у вас авг не пашет. Или не проксируется. Или юаб/запрет, если через него. Если через авг, то я бы ставил на fakeip.

---

**2026-03-11T00:49:52 | Routerich**
fake+multidisorder

---

**2026-03-11T08:51:29 | AleXXXey**
В подкопе ж никак не отключить fakeip для определённых доменов?

---

**2026-03-11T08:52:06 | Routerich**
Не отключается там fakeip, в принципе.

---

**2026-03-11T11:33:46 | Alex**
Установил скрипт номер 5, который подразумевает для части ресурсов zapret, а для части podkop(vpn)

Все отлично работает на устройствах из локальной сети.
Если я подключаюсь к роутеру через VPN (сервер AmneziaWG на роутере), трафик проходит через zapret, но не через podkop. В какую сторону копать для решения проблемы?

В веб-интерфейсе http://routerich.lan/cgi-bin/luci/admin/services/podkop при подключении через VPN пишет "браузер не использует FakeIP"

Разобрался: в настройках Podkop нужно было добавить интерфейс AmneziaWG в Source Network Interface.

---

**2026-03-12T01:14:32 | Petr Shcherbinin**
в секции выбран dns over https и снята галочка disable fake ip

---

**2026-03-12T01:17:18 | Рустам**
Может из-за fakeip?

---

**2026-03-12T10:34:34 | Роман**
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1
Здравствуйте. Эти стратегии попробуйте.

---

**2026-03-12T15:32:55 | Владимир Волков**
1) Телега пущена в обход?
2) Чем для обхода пользуетесь? Подкоп, зероблок? Бесплатные обходы или свой ключ/подписка? Прокси? Используется ли fakeip в секциях?
3) В панели управления тейлом ДНС настраивали? Подобно скрину выше. Также можно отключить Magic DNS и проверить

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

**2026-03-12T22:00:01 | Михаил**
Вторая вкладка в awg - удалить все dns. В последней вкладке проверить keep alive - должно быть 25. Ну и в zb галка отплючить fakeip выключена. И до кучи смотреть на заполнение обфукации - параметры I1-I5, диапазоны в h1-h4 и пр...

---

**2026-03-12T23:24:21 | Кирилл**
⚠️ WARP detected: engage.cloudflareclient.com
━━━━━━━━━━━━━━━━━━━━━━━━━━━
🥸 FakeIP status
⚠️ Router DNS is NOT routed through sing-box
❌ Sing-box does NOT work with FakeIP: 64.188.104.86

Не работает Fake ip, что можно предпринять?

---

**2026-03-13T02:29:22 | Рустам**
В подкоп вроде все нормально проходит кроме прокси трафика fakeip

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

**2026-03-14T16:51:14 | HiLLL**
и FakeIP включите, сняв галку в секции

---

**2026-03-14T18:31:57 | AleXXXey**
А если я продублирую секцию авг и пущу туда только мета с отключенным fakeip? или так не стоит делать?

Сейчас WA проверил. Если девайсы в домашней сети, то всё ок. А если один в домашней, а второй в квн, то видеозвонки не коннектятся, но сообщения влёт улетают.

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

**2026-03-14T19:45:54 | Garsia**
Подскажите, плиз, из-за чего может быть такое (в "Диагностике"):
FakeIP (клиент)  Не удалось проверить: Failed to fetch

Логи чуть выше выложил. Конфиг AWG рабочий, интерфейс пингуется.

---

**2026-03-14T20:11:23 | AleXXXey**
ещё один нюанс)
при выкл FakeIP у инсты видосы зависают через сек 5 и лента не обновляется.

---

**2026-03-14T20:19:27 | AleXXXey**
ну неее. это потому что Мета) 

если выкл fakeIP, то инста оживает, а WA снова помирает

---

**2026-03-14T21:29:41 | Routerich**
роутер резолвит в fakeip?

---

**2026-03-14T23:23:52 | РУЗОВ Дмитрий**
а переключатель Fake IP (вкл/выкл)

---

**2026-03-15T12:02:34 | Александр Масло**
Привет. Поломался fakeip утром, частично перестали обходы работать. Ничего не трогал. В чем может быть беда?

---

**2026-03-15T12:40:44 | ꧁ 𝓐𝓷𝓽𝓸𝓷 𝓑𝓮𝔃𝓴𝓪𝓹𝓾𝓼𝓽𝓲𝓷 ꧂**
Есть пара технических вопросов по ЗБ, в рамках самообразования:
1. Почему по умолчанию активирована опция "Отключить QUIC"? У меня один из outbound - socks5 с поддержкой udp, по идее Ютуб через QUIC должен бодрее гоняться в этом случае, разве нет? Как работает в целом эта опция? (При включенном "Отключить QUIC" не нашел в конфиге sing-box ничего, что могло бы быть добавлено этой опцией)
2. Относительно работы Fake IP - верно ли я понимаю, что нормально трафик будет перенаправляться только если на северной стороне удастся сниффингом получить домен, к которому идёт обращение? (Т.е. условный ncat domain.in.list.for.routing.com 1234 работать не будет)

---

**2026-03-15T13:15:38 | ꧁ 𝓐𝓷𝓽𝓸𝓷 𝓑𝓮𝔃𝓴𝓪𝓹𝓾𝓼𝓽𝓲𝓷 ꧂**
За ответ спасибо, но не до конца понял проблему - как я понимаю в тпрокси закидывается просто весь трафик где destip относится к сети fake ip. Какая разница tcp он или udp?

А на второй мой исходный вопрос про fake ip ответите?

---

**2026-03-15T13:16:29 | Routerich**
нет, для fakeip есть option fakeip_query_type_filter '1'

---

**2026-03-15T13:22:27 | Nikita**
А если у меня awg свой сервак, 1 секция и отключен fake ip, в этом случае могу оставить quic работающим? И к чему это приведёт?

---

**2026-03-15T13:23:01 | ꧁ 𝓐𝓷𝓽𝓸𝓷 𝓑𝓮𝔃𝓴𝓪𝓹𝓾𝓼𝓽𝓲𝓷 ꧂**
Т.е. по fake ip ситуация следующая:
Когда в синг попадает пакет с dest=fakeip, он берет домен сниффингом из пакета, резолвит его и на сервер отправляет уже пакет с реальным dest IP, так?

---

**2026-03-15T13:24:05 | Routerich**
нет, всё работает по резолвингу, резолвит в fakeip, безоговорочно заворачивает в синг, а тот уже внутри себя снифает и роутит

---

**2026-03-15T13:27:11 | Александр Масло**
Методом тыка выяснилось что мешает другая секция с прокси. Там стоит галка отключить fakeip. Секция выше авг10 в списке секций. Если ее поставить ниже или выключить, то проверка проходит нормально и обходы через авг10 начинают работать нормально.
Разве секции не должны работать полностью раздельно? Порядок секций как-то влияет?

---

**2026-03-15T13:30:10 | Routerich**
без fakeip это nftables, стандартный резолвинг, шлёт в синг все что на одном ip. проверка fakeip самое первое правило. секции лучше расположить 
fakeip
не fakeip

---

**2026-03-15T13:30:45 | Routerich**
нет, fakeip для клиента, с другой стороны стандартный роутинг

---

**2026-03-15T13:32:12 | Routerich**
fakeip для клиента позволяет разделить dst ip в разные маршруты внутри тпрокси

---

**2026-03-15T13:35:56 | Nikita**
Тогда не понятно, учитывая, что интерфейс vpn, fake ip выключен, значит резолв по nft в реальные IP, зачем тогда сингу домен в пакете udp, если IP уже отрезовлен?

---

**2026-03-15T13:44:06 | Александр Масло**
странно что до сегодняшнего дня все работало и так
прокси fakeip откл
авг10 fakeip вкл

при том что никто ничего не трогал...

---

**2026-03-15T15:11:32 | Виталий Александрович**
сделал тест стратегий по домену roblox.com в итоге скрипт нашел 3 рабочих стартегии
general (SIMPLE FAKE ALT) → 1/1
general (FAKE TLS AUTO ALT3) → 1/1
general (ALT10) → 1/1

по очереди попробовал каждую и нифига не запустилась игра.
вот только вопрос возник после выбора другой стратегии надо ли как то запрет перезапускать?

---

**2026-03-15T16:47:30 | AleXXXey**
Попытка №2😁

Кажется,я решил свою проблему с полноценной работой WhatsApp/Instagram. Напишу, может поможет кому.

Как сказал ранее, продублировал секцию авг для WA. В ней внёс все домены WhatsApp. Fakeip - ВЫКЛ. 

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
wl.co

А в основную авг - внёс домены инсты, фб, окулус (FakeIP - ВКЛ):

cdninstagram.com
facebook.com
facebook.com.es
facebook.com.vn
facebook.fr
facebook.net
fb.com
fb.me
fbcdn.net
fbsbx.com
ig.me
instagram.com
internalfb.com
messenger.com
meta.com
oculus.com
tfbnw.net
thefacebook.com
threads.net

В списках сообщества Meta убрал, добавил cdn AWS, Messengers и в исключённые домены добавил WA:

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
wl.co

Тестирую сутки. Пока всё работает.

P.S.  ZeroBlock - ОГОНЬ!😎🔥

---

**2026-03-15T19:24:24 | Lysandr Mortimer**
Прокси-трафик не маршрутизируется через FakeIP как то можно  исправить?

---

**2026-03-15T19:29:51 | Routerich**
https://podkop.net/docs/diagnostics/#fakeip-proverki

---

**2026-03-15T20:49:12 | Vadim**
Тоже пытаюсь гран туризмо починить на пс5
безрезультатно.

единственно что у меня кое кое завелся теккен на этой стратегии.


--filter-tcp=443 --filter-l7=tls --ipset=/opt/zapret2/ipset/ipset-all.txt --payload=tls_client_hello --lua-desync=hostfakesplit:host=2gis.ru:midhost=host-2:badsum:tcp_ack=-66000:tcp_ts_up

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

**2026-03-15T23:39:09 | Роман**
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1

---

**2026-03-15T23:46:48 | Святос**
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

**2026-03-16T09:37:51 | Andrey**
Ребята, может у кого было так. Работает маршрутизация через podkop. Все что за пределами РФ - в прокси (vless или hysteria2). Работало все оч стабильно и хорошо, только иногда сервера менял. Потом началась фигня с тем, что на некоторых устройствах работает инет, на других нет (весь инет, не только обход). Предполагаю проблему с DNS. Настраиваю DNS Failsafe как в закрепе и подбираю dns сервера - все начинает работать стабильно, но на прошлой неделе опять такая же борода. Меняю DoT на DoH, меняю dns сервера, даже частные ставлю - все фигня. Причем одновременно может на каких-то устройствах быть хорошо, а на других нифига. Грешу на fakeip и я бы его выключил, но не смог найти как это сделать.

---

**2026-03-16T12:54:40 | Yrii**
Mon Mar 16 12:52:34 2026 daemon.info youtubeUnblock[10767]: youtubeUnblock 1.3.0-1
Mon Mar 16 12:52:34 2026 daemon.info youtubeUnblock[10767]: Bypasses deep packet inspection systems that rely on SNI
Mon Mar 16 12:52:34 2026 daemon.info youtubeUnblock[10767]:
Mon Mar 16 12:52:34 2026 daemon.info youtubeUnblock[10767]: Running with flags: --queue-num=537 --threads=1 --packet-mark=32768 --silent --tls=enabled --frag=tcp --frag-sni-reverse=1 --frag-sni-faked=0 --frag-middle-sni=1 --frag-sni-pos=1 --fk-winsize=0 --fake-sni=1 --fake-sni-seq-len=1 --fake-sni-type=default --seg2delay=0 --faking-strategy=pastseq,  --sni-domains=<trie of 106 vertexes> --sni-detection=parse --synfake=0 --udp-filter-quic=disabled --fbegin --tls=disabled --sni-domains=<trie of 157 vertexes> --sni-detection=parse --synfake=0 --udp-filter-quic=disabled --udp-stun-filter --fend --fbegin --tls=enabled --frag=tcp --frag-sni-reverse=1 --frag-sni-faked=0 --frag-middle-sni=1 --frag-sni-pos=1 --fk-winsize=0 --fake-sni=1 --fake-sni-seq-len=1 --fake-sni-type=default --seg2delay=0 --faking-strategy=pastseq,  --sni-domains=<trie of 29 vertexes> --sni-detection=parse --synfake=0 --udp-filter-quic=disabled --fend
Mon Mar 16 12:52:34 2026 daemon.info youtubeUnblock[10767]: Queue 537 started

---

**2026-03-16T13:18:30 | Bullet for my valentine Poison**
так это чужие. Пробуйте свои подобрать. Строчку с fake оставьте и ищите вторую. К примеру не мультисплит а мультидисордер.(через блокчек)

---

**2026-03-16T13:40:36 | Bullet for my valentine Poison**
-- payload
-- lua-desync=fake
-- lua-desync=**

что в этом сложного? Вы просто заменяете вторую и третью строчку, по ситуации. Еще можно их местами менять. На лыжне так работает.

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

**2026-03-16T21:10:42 | Роман**
Каждый раз обновляюсь до посденей версии в надежде, что проблема уйдёт. Свой awg закидывал, отключал включал везде fake ip, но ничего не помогает.

---

**2026-03-16T22:01:46 | Роман**
И еще плс один вопрос. Возможно обсуждалось. В секции awg галочка "отключить fake ip" должна стоять? И по поводу секции опера-прокси такой же вопрос. А то я запутался уже какие настройки выставлены по умолчанию.

---

**2026-03-16T22:26:34 | Wenzel Perminov**
zeroblock invoked oom-killer: gfp_mask=0x40cc0(GFP_KERNEL|__GFP_COMP), order=0, oom_score_adj=0
CPU: 1 PID: 18083 Comm: zeroblock Tainted: G O 6.6.119 #0
[ 17749] 0 17749 385 32 32768 0 0 zeroblock
[ 18083] 0 18083 23959 22304 217088 0 0 zeroblock
[ 18200] 0 18200 1386 64 36864 0 0 zeroblock
oom-kill:constraint=CONSTRAINT_NONE,nodemask=(null),cpuset=/,mems_allowed=0,global_oom,task_memcg=/,task=zeroblock,pid=18083,uid=0
Out of memory: Killed process 18083 (zeroblock) total-vm:95836kB, anon-rss:89088kB, file-rss:128kB, shmem-rss:0kB, UID:0 pgtables:212kB oom_score_adj:0

случилась такая ерунда на роутерич usb 2 он не мог переварить 30 списков в секциях при отключённой fake ip, перезагрузки не помогали и обновления появилось пока я понимал в чем дело, тоже не помогло. Причину нашёл методом случайного перебора вариантов (выключал секции и начинало работать, увидел что включена отключение фейк ип, убрал галочку тоже заработало)

---

**2026-03-17T13:39:15 | HiLLL**
галка снята в секции с Отключить FakeIP ?

---

**2026-03-17T16:52:23 | 𝕾𝖊𝖗𝖌𝖊𝖎 𝕷𝖎𝖘𝖆𝖑𝖔**
вопросик можно глупый?!:) 
а домены которые через API v2 подгружаются обновляются хорошо? в частности секция Games. Дети просят, все работало и перестало, я все обновил, раньше через секцию awg прекрасно летало. Fake IP отключен для секции, уж не знаю на что думать еще, может какие cdn надо в секцию еще ткнуть? На работе тоже роутерич, поставил даже себе на тест на смартфон игрушку, все настроил в ZB и ситуация такая же, error 279. Что еще посмотреть можно?

---

**2026-03-17T19:14:58 | AleXXXey**
А теперь попробуйте поюзать инсту) без fakeIP инста не взлетает, а с fakeIP - вотсапп не колосится

---

**2026-03-18T14:21:18 | Bullet for my valentine Poison**
ты имеешь ввиду 
--payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:tcp_md5:tls_mod=rnd,dupsid,padencap:repeats=1 --payload=empty --out-range=<s1 --lua-desync=send:tcp_md5
это?

---

**2026-03-18T15:21:47 | Yury Kuzmenko**
А вот когда стратегии такого вида

--lua-init=fake_default_tls=tls_mod(fake_default_tls,'rnd') --payload=tls_client_hello --lua-desync=multidisorder:pos=2:seqovl=1:seqovl_pattern=fake_default_tls
правильно их разбить на 3 строки?
 --payload=tls_client_hello
--lua-init=fake_default_tls=tls_mod(fake_default_tls,'rnd') 
 --lua-desync=multidisorder:pos=2:seqovl=1:seqovl_pattern=fake_default_tls

---

**2026-03-19T14:11:03 | Chezok**
мне помогла магическая стратегия, йутуб залетал на всём
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4

---

**2026-03-19T20:21:58 | AleXXXey**
оставил только оперу. fakeIP сработал. чатгпт открылся.

Конфликты?

---

**2026-03-19T23:29:51 | Bullet for my valentine Poison**
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=fake_default_tls:badsum:tls_mod=sni=rzd.ru:repeat=8

---

**2026-03-20T00:34:39 | Bullet for my valentine Poison**
--out-range=-s34228
--payload=tls_client_hello
--in-range=-s5556 --lua-desync=circular:fails=3:maxtime=60
--in-range=x
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1:strategy=1
--lua-desync=fake:blob=fake_default_tls:badsum:tls_mod=sni=rzd.ru:repeat=8:strategy=1
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1:strategy=2
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4:strategy=2:final

---

**2026-03-20T18:17:25 | Ilya Vybornov**
Други выручайте, последние 3 дня отвалились проверки Fake IP, ну и соответственно не работает часть нужных сайтов и игр. я уже всю голову сломал, что не так.

---

**2026-03-21T19:46:22 | ꧁ 𝓐𝓷𝓽𝓸𝓷 𝓑𝓮𝔃𝓴𝓪𝓹𝓾𝓼𝓽𝓲𝓷 ꧂**
Привет, друзья
Вопросик есть по добавлению кастомных инбаундов и роутов:
Значит создал я свои inbounds.json и route.json в /etc/zeroblock/sing-box.d
inbounds.json содержит один сокс inbound
в route.json прописал правила - всё что относится к телеге на нужный outbound, всё остальное - в reject.

Проблема такая: ЗБ во всех своих роутах где inbound был tproxy-in, добавил туда ещё и мой кастомный inbound  (/tmp/zeroblock/sing-box.d/40-route.json). Таким образом для кастомного inbound начинают работать списки, т.к. мои правила из route.json имеют меньший приоритет.

Зачем ЗБ так делает? Как ни будь можно ему сказать, чтоб он оставил мой inbound в покое? Я сам хочу правила для него разрулить...

Вот кусочек конфига, что бы понятно было что я имею ввиду:

"rules": [
  {
    "action": "sniff",
    "inbound": "tproxy-in"
  },
  {
    "inbound": "dns-in",
    "action": "hijack-dns"
  },
  {
    "inbound": [
      "tproxy-in",
      "socks-telega-in"
    ],
    "protocol": "dns",
    "action": "hijack-dns"
  },
  {
    "inbound": [
      "tproxy-in",
      "socks-telega-in"
    ],
    "ip_cidr": [
      "127.0.0.0/8"
    ],
    "action": "reject"
  },
  {
    "inbound": [
      "tproxy-in",
      "socks-telega-in"
    ],
    "domain": [
      "fakeip-check.zeroblock.best"
    ],
    "override_address": "127.0.0.1",
    "outbound": "direct-out"
  },
  {
    "inbound": [
      "tproxy-in",
      "socks-telega-in"
    ],
    "outbound": "Socks",
    "rule_set": [
      "community-Socks-ai",
      "community-Socks-games",
      "community-Socks-messengers",
      "community-ip-Socks-messengers",
      "community-Socks-youtube",
      "user-domains-text-Socks",
      "user-subnets-text-Socks"
    ]
  },
  {
    "inbound": [
      "tproxy-in",
      "socks-telega-in"
    ],
    "outbound": "Vless",
    "rule_set": [
      "community-Vless-meta",
      "user-domains-text-Vless"
    ]
  },
  {
    "inbound": [
      "tproxy-in",
      "socks-telega-in"
    ],
    "protocol": "bittorrent",
    "outbound": "direct-bt"
  },
  {
    "inbound": [
      "socks-telega-in"
    ],
    "action": "sniff"
  },
  {
    "inbound": [
      "socks-telega-in"
    ],
    "rule_set": [
      "tg-domains",
      "tg-ips"
    ],
    "outbound": "Socks"
  },
  {
    "inbound": [
      "socks-telega-in"
    ],
    "action": "reject"
  }
]

---

**2026-03-21T20:15:26 | Борис**
Не совсем. Он скорее не может понять, что происходит. Это косвенно может говорить об обходе блокировки, и в то же время может не означать этого (например, он может подумать, что используется какой-то новый протокол для эффективной торговли пирожками). А если ты используешь стратегии на подобие fake sni, то он ещё и не видит (а точнее - неправильно определяет) какие сайты ты посещаешь

---

**2026-03-21T21:10:58 | Aндрей**
Впн платный, свой сервак, Испания. 100% работает, поэтому убрал галочку fakeip

---

**2026-03-21T21:31:36 | Роман**
А почему стоит отключить fake ip?

---

**2026-03-22T00:25:27 | Alexey Zh**
я в целом там ничего не трогал кроме rr_youtube 
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4

---

**2026-03-22T01:17:33 | HiLLL**
если инфа не устарела, Fresa говорил, что нужно отключить FakeIP для консолек

---

**2026-03-22T01:20:55 | A̴͂ ̖͔͎͍͔̮̌̾̈̓̇̅͗̓̒̌̉̀̕͠͝ ̧̙͕̬̦̩̞ͅͅv̸̡̡̬̬͔͕̰̖̻̄́̎̽ͅř̸̆̓͛̉̋̈́̔̔̔͂**
Да, на xiaomi качает без проблем

Пробовал разные комбинации настроек на случай если это баг

Пробовал отключить Zapret, Zeroblock - безрезультатно

FakeIP тоже отключал в специальной секции eth0 WAN для консоли

Где сохраняется этот отчет test_config_script_nightly ? В root файла analyzer.log нет

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

**2026-03-22T09:20:32 | ВПН НА ТЕЛЕВИЗОР ФИЛИПС**
Сейчас ради интереса убрал на пк шлюз на линух, сделал такую страту:
--filter-udp=443 --hostlist="%LISTS%list-general.txt" --dpi-desync=fake --dpi-desync-repeats=1 --dpi-desync-fake-quic="%BIN%quic_initial_www_google_com.bin" --new ^
--filter-tcp=80,443 --hostlist="%LISTS%list-general.txt" --dpi-desync=fake --dpi-desync-fooling=ts --dpi-desync-fake-tls="%BIN%tls_clienthello_www_google_com.bin" --dpi-desync-repeats=1
И все работает идеально

---

**2026-03-22T12:34:11 | Александр 🔴🔵**
--filter-tcp=3724,8085,8090,8100,8903,8904 --dpi-desync=syndata --dpi-desync-fake-syndata="%BIN%tls_clienthello_4pda_to.bin" --new ^

---

**2026-03-22T14:29:56 | Routerich**
нет, мне хватило скрещивания системного роутинга и fakeip

---

**2026-03-22T15:41:54 | Роман**
Работает на этих.
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1

--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1

---

**2026-03-22T15:47:47 | Bullet for my valentine Poison**
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN
--lua-desync=multidisorder:pos=2,midsld:seqovl=1:seqovl_pattern=fake_default_tls
и на этих!А еще на тех!)

---

**2026-03-22T17:34:26 | Anna Bagler**
Приложение официальное, обновлённое или какое-то стороннее? fakeip специально отключали?

---

**2026-03-22T18:06:30 | Андрей**
А что делать с Fakeip? Забить?

---

**2026-03-22T18:06:37 | Marat 🌊🌊 Wave**
FakeIP что мешает? А где посмотреть?

---

**2026-03-22T22:59:49 | 🆂🅷🅾🅳🅸🅼🅰🆂🆃🅴🆁**
дело в том что она и не работала на zeroblock+zapret с чистого роутера. Но если скрипт номер 5 поверх вкорячить то работает. FakeIP постоянно красный крестих без подкопа

---

**2026-03-22T23:33:38 | 🆂🅷🅾🅳🅸🅼🅰🆂🆃🅴🆁**
Если его начисто ставить он тоже проблемный. А если поверх зероблока то всё ок, но куча всяких служб смущает перфекционизм)) что то в скрипте номер 5 делается что fakeip воскресает. Думал может есть решение чтобы не ставить скрипт тот

---

**2026-03-22T23:35:22 | Kiss_My_Axe**
Это и есть фейкайпи.
198.18.x.x

А у вас в секциях ZB просто установлена галка "Отключить Fakeip".

---

**2026-03-22T23:38:45 | 🆂🅷🅾🅳🅸🅼🅰🆂🆃🅴🆁**
О кстати. Fakeip клиент галочку получил. В аутбаунд тайм-аут выкидывает

---

**2026-03-23T06:42:33 | Alex Korshun**
--out-range=-s34228
--in-range=-s5556
--lua-desync=circular:fails=3:maxtime=90
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1:strategy=1
--lua-desync=multisplit:pos=2:strategy=1
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1:strategy=2
--lua-desync=multisplit:pos=midsld:strategy=2
--lua-desync=fake:blob=fake_default_tls:badsum:repeats=1:strategy=3
--lua-desync=hostfakesplit:badsum:repeats=1:strategy=3
--lua-desync=fake:blob=fake_default_tls:tcp_flags_unset=ACK:repeats=1:strategy=4
--lua-desync=hostfakesplit:disorder_after:tcp_flags_unset=ACK:repeats=1:strategy=4
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN:repeats=1:strategy=5
--lua-desync=hostfakesplit:midhost=midsld:tcp_flags_set=SYN:repeats=1:strategy=5:final

---

**2026-03-23T12:16:29 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.2-r23:
  Изменения:
  - Parental Control
  Полностью переработана архитектура блокировки по расписанию:
  PC секции теперь блокируют только через nftables — sing-box reject rule убран. Раньше sing-box блокировал трафик постоянно, игнорируя расписание. Теперь блокировка работает строго по времени через nft правила с meta hour и meta day.
  - Cron conntrack flush — при наступлении времени блокировки автоматически разрываются существующие соединения для source IP из PC секции через conntrack -D. Без этого уже установленные TCP соединения продолжали работать после начала блокировки.
  - PC nftset timeout 2 минуты вместо 60 минут — предотвращает ложные срабатывания из-за переиспользования FakeIP адресов sing-box.
  - Обычные BLOCK секции (без PC) теперь поддерживают fully_routed_ips и excluded_source_ips с инверсией — можно блокировать для всех кроме определённых устройств.
  - Счётчики добавлены ко всем PC nft правилам для диагностики.
  - Mixed Proxy
  Авторизация — новые поля Username и Password. При включении Authentication sing-box создаёт mixed inbound с users для SOCKS5/HTTP авторизации.
  Выбор интерфейсов — MultiValue список интерфейсов для прослушивания. Можно выбрать конкретные интерфейсы или "All interfaces (0.0.0.0)" вместо привязки ко всем source_network_interfaces.

  Подписки
  - short_id sanitize — обрезка до первого не-hex символа (макс 16). Подписки со спамом в параметрах Reality (рекламные Telegram-ссылки в short_id) больше не ломают sing-box.
  - Ignore Tags: DynamicList — вместо MultiValue теперь dropdown с предложениями из подписки плюс возможность ввести свой тег
  вручную.
#ZeroBlock

---

**2026-03-23T22:31:54 | Дмитрий Григорьев**
Стратегия 
--out-range=-s34228
--in-range=-s5556
--lua-desync=circular:fails=3:maxtime=90
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1:strategy=1
--lua-desync=multisplit:pos=2:strategy=1
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1:strategy=2
--lua-desync=multisplit:pos=midsld:strategy=2
--lua-desync=fake:blob=fake_default_tls:badsum:repeats=1:strategy=3
--lua-desync=hostfakesplit:badsum:repeats=1:strategy=3
--lua-desync=fake:blob=fake_default_tls:tcp_flags_unset=ACK:repeats=1:strategy=4
--lua-desync=hostfakesplit:disorder_after:tcp_flags_unset=ACK:repeats=1:strategy=4
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN:repeats=1:strategy=5
--lua-desync=hostfakesplit:midhost=midsld:tcp_flags_set=SYN:repeats=1:strategy=5:final

---

**2026-03-23T23:49:20 | Роман**
--in-range=-s5556 --lua-desync=circular:fails=3:maxtime=60
  --in-range=x
  --lua-desync=multisplit:seqovl=681:seqovl_pattern=blob_stun:strategy=1
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=fonts.google.com:strategy=2
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=2
  --lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=2
  --lua-desync=fake:blob=blob_tls_clienthello_t2_ru:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=m.ok.ru:strategy=3
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=3
  --lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=3
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:strategy=4
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=google.com:strategy=4
  --lua-desync=multisplit:pos=2,sld:seqovl=2108:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=4
  --lua-desync=fake:blob=blob_stun:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=5
  --lua-desync=fakeddisorder:pos=1:pattern=blob_tls_clienthello_www_google_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=5
  --lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=6
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=7
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=7
  --lua-desync=multisplit:pos=2,sld:seqovl=620:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=7
  --lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=8
  --lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=8
  --lua-desync=multisplit:pos=2,sld:seqovl=620:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=8
  --lua-desync=hostfakesplit:host=mapgl.2gis.com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=9
  --lua-desync=fake:blob=blob_tls_clienthello_www_4pda_to:optional:tcp_ts=-600000:tls_mod=none:strategy=10
  --lua-desync=fake:blob=blob_stun:optional:tcp_seq=0:tcp_ack=-66000:badsum:strategy=11
  --lua-desync=multisplit:pos=1:seqovl=654:seqovl_pattern=blob_stun:strategy=11
  --lua-desync=hostfakesplit:midhost=host-2:host=i2.photo.2gis.com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=12
  --lua-desync=multisplit:pos=1:seqovl=582:seqovl_pattern=blob_stun:strategy=13:final

--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4

---

**2026-03-24T14:50:03 | Святос**
--out-range=-s34228
--payload=tls_client_hello
--in-range=-s5556 --lua-desync=circular:fails=3:maxtime=60
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1:strategy=1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4:strategy=1
--lua-desync=fake:blob=0x00000000:tcp_seq=-10000:tcp_ack=-66000:strategy=2
--lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:strategy=2
--lua-desync=fake:blob=fake_default_tls:badsum:repeats=1:strategy=3
--lua-desync=fake:blob=fake_default_tls:tcp_ts=-1000:repeats=1:strategy=4:final

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

**2026-03-24T16:34:48 | Святос**
 # Strategy 1
            --lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=fonts.google.com:tcp_seq=10000:strategy=1
            --lua-desync=multisplit:pos=1,midsld:seqovl=1:seqovl_pattern=tls_clienthello:tcp_ts_up:strategy=1
            # Strategy 2
            --lua-desync=fake:blob=0x00000000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=www.google.com:repeats=2:strategy=2
            --lua-desync=multisplit:pos=1,midsld:strategy=2
            # Strategy 3
            --lua-desync=hostfakesplit:host=ozon.ru:midhost=host-2:seqovl=sniext+3:seqovl_pattern=tls_clienthello:badsum:tcp_md5:tcp_ts_up:strategy=3
            --lua-desync=hostfakesplit:tcp_md5:tcp_ts_up:strategy=3

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

**2026-03-24T18:50:29 | Anna Bagler**
fakeip отрабатывает. Проверьте сайт со смартфона.

---

**2026-03-24T21:17:19 | Anna Bagler**
А fakeip для facebook и остального в секции не отрабатывал.

---

**2026-03-24T21:23:54 | Роман**
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1

--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1

--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN
--lua-desync=multidisorder:pos=2,midsld:seqovl=1:seqovl_pattern=fake_default_tls
Эти попробуйте.

---

**2026-03-24T21:25:32 | Святос**
--lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=fonts.google.com:tcp_seq=10000:strategy=1
--lua-desync=multisplit:pos=1,midsld:seqovl=1:seqovl_pattern=tls_clienthello:tcp_ts_up:strategy=1
--lua-desync=fake:blob=0x00000000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=www.google.com:repeats=2:strategy=2
--lua-desync=multisplit:pos=1,midsld:strategy=2
--lua-desync=hostfakesplit:host=ozon.ru:midhost=host-2:seqovl=sniext+3:seqovl_pattern=tls_clienthello:badsum:tcp_md5:tcp_ts_up:strategy=3
--lua-desync=hostfakesplit:tcp_md5:tcp_ts_up:strategy=3

---

**2026-03-24T22:35:05 | Святос**
--out-range=-s34228
--payload=tls_client_hello
--in-range=-s5556 
--lua-desync=circular:fails=3:maxtime=50
--in-range=x
--lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=fonts.google.com:tcp_seq=10000:strategy=1
--lua-desync=multisplit:pos=1,midsld:seqovl=1:seqovl_pattern=tls_clienthello:tcp_ts_up:strategy=1
--lua-desync=fake:blob=0x00000000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=www.google.com:repeats=2:strategy=2
--lua-desync=multisplit:pos=1,midsld:strategy=2
--lua-desync=hostfakesplit:host=ozon.ru:midhost=host-2:seqovl=sniext+3:seqovl_pattern=tls_clienthello:badsum:tcp_md5:tcp_ts_up:strategy=3
--lua-desync=hostfakesplit:tcp_md5:tcp_ts_up:strategy=3
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1:strategy=4
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1:strategy=5
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN:strategy=6
--lua-desync=multidisorder:pos=2,midsld:seqovl=1:seqovl_pattern=fake_default_tls:strategy=6:final

---

**2026-03-25T00:10:39 | HiLLL**
посмотри в диагностику, что с fakeip

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

**2026-03-25T19:08:23 | Artem Mayorov**
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4
вот эту мне дали

---

**2026-03-25T19:42:13 | Bullet for my valentine Poison**
--out-range=-s34228
--payload=tls_client_hello
--in-range=-s5556 --lua-desync=circular:fails=3:maxtime=60
--in-range=x
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1:strategy=1
--lua-desync=fake:blob=fake_default_tls:badsum:tls_mod=sni=rzd.ru:repeat=8:strategy=1
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1:strategy=2
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4:strategy=2:final
продублирую. 2 в 1

---

**2026-03-25T19:45:37 | Routerich**
fakeip_query_type_filter мб поможет или потуши fakeip в секции

---

**2026-03-25T20:53:36 | Bullet for my valentine Poison**
--out-range=-s34228
--payload=tls_client_hello
--in-range=-s5556 --lua-desync=circular:fails=3:maxtime=60
--in-range=x
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1:strategy=1
--lua-desync=fake:blob=fake_default_tls:badsum:tls_mod=sni=rzd.ru:repeat=8:strategy=1
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1:strategy=2
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4:strategy=2:final

---

**2026-03-25T21:36:40 | Святос**
Fake TLS

---

**2026-03-25T22:20:43 | Дмитрий**
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4
Этот пробовал?

---

**2026-03-26T05:13:02 | Камиль**
Мой последний эксперимент как раз с fakeIP связан. Решил пока его выключить для данной секции, посмотрим. Cdn списки тоже выключил. А по поводу порядка секций, интересное предложение... Не знал что zb работает по приоритету в секциях.
Спасибо!

---

**2026-03-26T06:06:19 | AleXXXey**
какая-то брехняшка происходит после обновления с 0.7.1-r56  на крайнюю(без претензий). Whatsapp отрыгнул. Даже на whatsapp.com не пускает. Остальные метовские сайты работают.

Уже перекидывал домены ВА на свой сервак(через авг20) - тож ничего не открывается. Как будто правила конфликтуют\не применяются, но в YACD всё ок, вроде, ходит.

Через квн с девайса - всё ок.

UPD. С включением FakeIP для доменов ВА - начинает пускать на whatsapp.com , а сама приложуха упёрто показывает фигушку.

---

**2026-03-26T08:58:32 | AleXXXey**
я пробовал по такой метОде. Такая стратегия не сработала.

Мне ВА и инсту пришлось делить на 2 секции, т.к. инста не работала без fakeip, а ВА, наоборот, отказывается трудиться с fakeip

---

**2026-03-26T09:21:11 | AleXXXey**
fakeip - выкл?
инста - шевелится?

---

**2026-03-26T10:03:05 | Роман**
Zeroblock юзер френдли, просто нужно создать новый интерфейс Amnezia, импортировать туда свой конфиг (.conf перетянуть в окошко), поставить галку не создавать маршруты, чуть-чуть настроить фаервол (скриншоты попозже могу скинуть), создать новую секцию в ZB, убрать галку с fake ip, выбрать список с тем что пойдет через Amnezia, и в принципе готово 😁

---

**2026-03-26T10:47:27 | Artem Mayorov**
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4

Вот эта у меня. Эта два в одном?

---

**2026-03-26T11:01:23 | Routerich**
почему коннекты по минуте? вы похоже проваливаетесь мимо окна fakeip и получаете реальный адрес, который не роутится сингбоксом

---

**2026-03-26T11:29:43 | Anna Bagler**
Ну, fakeip отрабатывает, что проверялка IP показывает в этой же секции?

---

**2026-03-26T11:47:03 | Роман**
Значит в ЗБ новую секцию, там выбрать свой интерфейс, убрать fake ip, выбрать списки (кроме CDN) и наслаждаться работой zeroblock 😁

---

**2026-03-26T12:16:21 | Kiss_My_Axe**
Там, конечно, написато:
Proxy router's own outgoing traffic for sections with Disable FakeIP. FakeIP sections always proxy router traffic automatically.
Но каг убедитсо?

---

**2026-03-27T10:48:02 | Vet**
Подскажите, zeroblock каки подкоп юзает fakeip?

---

**2026-03-27T14:20:56 | Bullet for my valentine Poison**
--payload=tls_client_hello
--lua-desync=fake:blob=blob_tls_clienthello_escapefromtarkov_com:badsum:tcp_ts=-600000:repeats=6
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
https://nnmclub.to  и https://rutracker.org/forum/index.php прекрасно открываются без зероблока.

---

**2026-03-27T14:37:37 | Bullet for my valentine Poison**
двухступенчатый гибрид, где сначала идёт fake‑инстанс, а затем multidisorder‑инстанс, и каждый из них выполняет свою роль в разрушении DPI‑парсера.
Я разложу всё по инстансам, по параметрам, по функциям, и по эффектам на DPI — так, как ты любишь: чётко, глубоко и без воды.

🟦 ИНСТАНС №1

🎯 Что делает этот инстанс в целом
Он создаёт и отправляет фейковый ClientHello, основанный на blob’е , и делает это 6 раз подряд, каждый раз с битым TCP checksum и сильно смещённым timestamp.
Это классический fake‑desync, который должен:
•   заставить DPI принять фейковый ClientHello за настоящий
•   сбить его state‑machine
•   заставить DPI «залипнуть» на ложном потоке
•   а настоящий ClientHello уйдёт позже — уже под multidisorder

🔍 Параметры по отдельности
1) 
Фейковый ClientHello берётся из заранее подготовленного блоба.
Функция:
•   DPI видит валидный TLS ClientHello, но не соответствующий реальному домену
•   DPI начинает парсить его и уходит в неверное состояние
•   DPI может ошибочно кэшировать SNI или fingerprint

2) 
Фейковый пакет отправляется с битой TCP checksum.
Функция:
•   DPI часто игнорирует checksum, потому что работает до TCP‑стека
•   но сервер и ОС отбрасывают пакет
•   DPI остаётся «в ловушке», а сервер — нет
Это классический split‑brain: DPI думает, что видел ClientHello, а сервер — нет.

3) 
Сдвиг TCP timestamp на минус 600 тысяч.
Функция:
•   DPI часто не проверяет корректность TSval/TSecr
•   но сервер отбрасывает пакет как слишком старый
•   DPI снова остаётся в ложном состоянии

4) 
Фейковый ClientHello отправляется 6 раз подряд.
Функция:
•   повышает шанс, что DPI «схватит» один из фейков
•   создаёт «шум» в TCP‑потоке
•   увеличивает вероятность рассинхронизации state‑machine DPI

🟦 Итог по инстансу №1
Это агрессивный фейковый спам, который:
•   создаёт ложный TLS‑контекст
•   ломает DPI‑парсер
•   не влияет на сервер
•   подготавливает почву для multidisorder

🟦 ИНСТАНС №2

🎯 Что делает этот инстанс в целом
Он работает уже с реальным ClientHello, и создаёт несколько несовместимых версий одного и того же пакета, меняя позиции ключевых полей.
Это многоточечный L7‑desync, который:
•   ломает DPI‑парсер TLS
•   создаёт несовпадение между тем, что видит DPI и сервер
•   делает ClientHello «непарсабельным» для большинства DPI

🔍 Параметры по отдельности
1) 
Первый split/shift происходит в самом начале ClientHello.
Функция:
•   ломает DPI, который ожидает фиксированную структуру TLS record header
•   создаёт несовместимость между длиной и фактическим содержимым

2) 
Сдвиг в области Server Name Indication extension.
Функция:
•   DPI не может корректно извлечь SNI
•   DPI не может применить правила блокировки по домену
•   сервер при этом получает корректный ClientHello

3) 
Сдвиг в области hostname внутри SNI.
Функция:
•   ломает DPI‑парсер, который ищет строку домена
•   DPI может увидеть обрезанный или повреждённый hostname
•   сервер получает нормальный hostname

4) , , 
Три точки в области middle of second-level domain.
Функция:
•   создаёт три несовместимых варианта ClientHello
•   DPI не может собрать целостную структуру
•   DPI не может определить fingerprint (JA3/JA4)
•   DPI не может извлечь домен
•   сервер получает нормальный пакет
Это ядро multidisorder: многократное рассогласование структуры.

5) 
Сдвиг в конце hostname.
Функция:
•   ломает DPI, который пытается проверить длину SNI
•   DPI может решить, что ClientHello повреждён
•   сервер получает корректный пакет

🟦 Итог по инстансу №2
Этот инстанс:
•   создаёт несколько несовместимых версий реального ClientHello
•   ломает DPI‑парсер TLS на уровне структуры
•   делает невозможным извлечение SNI
•   делает невозможным JA3‑анализ
•   не мешает серверу

🟦 Общий итог стратегии
🔥 Что делает вся стратегия целиком
1) Fake‑инстанс
•   создаёт ложный ClientHello
•   заставляет DPI «залипнуть»
•   сервер его игнорирует
2) Multidisorder‑инстанс
•   ломает DPI‑парсер реального ClientHello
•   делает невозможным анализ SNI
•   делает невозможным JA3
•   сервер получает чистый пакет

---

**2026-03-27T19:02:02 | AleXXXey**
В моём случае, как минимум, 2 секции мне нужны были, для вотсапа, например. Так как часть меты умеет с fakeip, другая часть - не умеет🤷

---

**2026-03-27T21:40:36 | IIlIlIlIIlIlIlIIIll**
привет. как исправить то что fakeIP не работает ?

---

**2026-03-27T22:47:23 | Святос**
--payload=tls_client_hello
--lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=fonts.google.com:tcp_seq=10000
--lua-desync=multisplit:pos=1,midsld:seqovl=1:seqovl_pattern=tls_clienthello:tcp_ts_up --new

---

**2026-03-27T23:21:15 | Kirill Y**
И телеграмм перестал работать.. В диагностике fake ip (клиент) не работает..

---

**2026-03-28T11:12:21 | Дмитрий Григорьев**
Стратегия 
--out-range=-s34228
--in-range=-s5556
--lua-desync=circular:fails=3:maxtime=90
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1:strategy=1
--lua-desync=multisplit:pos=2:strategy=1
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1:strategy=2
--lua-desync=multisplit:pos=midsld:strategy=2
--lua-desync=fake:blob=fake_default_tls:badsum:repeats=1:strategy=3
--lua-desync=hostfakesplit:badsum:repeats=1:strategy=3
--lua-desync=fake:blob=fake_default_tls:tcp_flags_unset=ACK:repeats=1:strategy=4
--lua-desync=hostfakesplit:disorder_after:tcp_flags_unset=ACK:repeats=1:strategy=4
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN:repeats=1:strategy=5
--lua-desync=hostfakesplit:midhost=midsld:tcp_flags_set=SYN:repeats=1:strategy=5:final

---

**2026-03-28T12:11:14 | HiLLL**
Где эта настройка в морде находится? Сравниваю конфиги и не могу понять где она
option fakeip_query_type_filter '1'

---

**2026-03-28T16:14:39 | Александр**
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

**2026-03-29T00:43:47 | Станислав Земляков**
scan стратегий — это TCP handshake (SYN→SYN/ACK→ACK) + TLS Client Hello с модифицированными параметрами (split, disorder, fake). Если от сервера пришёл Server Hello — стратегия прошла DPI. Никаких данных не передаётся, соединение закрывается. Это не нагрузочное тестирование, это probe. 1024 воркера × ~150 стратегий/сек — для любого CDN это шум уровня одного браузера.

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

**2026-03-29T23:29:51 | Red Cat🐈**
Подскажите, а почему дашборд (или что это?) состоит просто из серых прямоугольников? 

В диагностике все зелёное, кроме fakeip client (ну и zapret не установлен)

---

**2026-03-30T09:29:46 | AleXXXey**
Ранее писал об этом, но изменить сообщение уже не даёт. Поэтому, продублирую своё сообщение с небольшим изменением.


Кажется,я решил свою проблему с полноценной работой WhatsApp/Instagram. Напишу, может поможет кому.

Как сказал ранее, продублировал секцию авг для WA. В ней внёс все домены WhatsApp. Fakeip - ВЫКЛ. 

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
wl.co

А в основную авг - внёс домены инсты, фб, окулус (FakeIP - ВКЛ):

cdninstagram.com
facebook.com
facebook.com.es
facebook.com.vn
facebook.fr
facebook.net
fb.com
fb.me
fbcdn.net
fbsbx.com
ig.me
instagram.com
internalfb.com
messenger.com
meta.com
oculus.com
tfbnw.net
thefacebook.com
threads.net

В списках сообщества Meta убрал, добавил cdn AWS и в исключённые домены добавил WA:

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
wl.co

Причина разделения Меты на разные секции - Инста не умеет работать без FakeIP, а WA, наоборот, с FakeIP конфликтует.

!!! UPD.  Предупреждаю, это мега костыль.
Если такая стратегия не завела WA, то идём в настройки ЗБ и включаем API v2 и CIDR списки сообщества ipv4+ipv6. Сохранить, применить. Чекаем WA  с инстой. Должно заколоситься. Идём в настройки ЗБ и  вырубаем  CIDR ipv4+ipv6. Сохранить, применить. 

Такая схема работает ровно до перезагрузки роутера. Если перезагрузили - снова повторяем последнее.

ПыСы. Версия: 0.7.1-r30

---

**2026-03-30T10:00:49 | AleXXXey**
К сожалению, мне список мета не помог. Вся мета работала, кроме WA. Отключаю fakeIP, инста помирает, WA колосится.

Видимо, провайдер жестит.

---

**2026-03-30T10:11:04 | Inko**
--out-range=-s34228
--payload=tls_client_hello
--in-range=-s5556 --lua-desync=circular:fails=2:maxtime=20
--in-range=x
--lua-desync=multidisorder:pos=1,midsld:strategy=1
--lua-desync=multisplit:seqovl=681:seqovl_pattern=blob_stun:strategy=2
--lua-desync=hostfakesplit:host=mapgl.2gis.com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=3
--lua-desync=fake:blob=blob_tls_clienthello_www_4pda_to:optional:tcp_ts=-600000:tls_mod=none:strategy=4
--lua-desync=fakeddisorder:pos=method+2:tcp_md5:strategy=5
--lua-desync=hostfakesplit:midhost=host-2:host=rzd.ru:tcp_seq=0:tcp_ack=-66000:badsum:strategy=6
--lua-desync=hostfakesplit:midhost=host-2:host=i2.photo.2gis.com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=7
--lua-desync=multisplit:pos=1:seqovl=582:seqovl_pattern=blob_stun:strategy=8
--lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=9
--lua-desync=multisplit:pos=1:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:ip_id=zero:strategy=10
--lua-desync=multidisorder:pos=7,sld+1:nodrop:strategy=11
--lua-desync=multidisorder:pos=1,midsld,endhost-1:strategy=12
--lua-desync=fake:blob=blob_stun:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=13
--lua-desync=fakeddisorder:pos=1:pattern=blob_tls_clienthello_www_google_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=13
--lua-desync=fake:blob=blob_stun:optional:tcp_seq=0:tcp_ack=-66000:badsum:strategy=14
--lua-desync=multisplit:pos=1:seqovl=654:seqovl_pattern=blob_stun:strategy=14
--lua-desync=hostfakesplit:host=google.com:tcp_ts=-600000:strategy=15
--lua-desync=multisplit:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=16
--lua-desync=tls_client_hello_clone:blob=cloned_tls:fallback=fake_default_tls:strategy=17
--lua-desync=fake:blob=cloned_tls:optional:tcp_seq=10000000:tcp_ack=-66000:repeats=2:tls_mod=rnd,dupsid,sni=fonts.google.com:strategy=17
--lua-desync=multidisorder:pos=1:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=17
--lua-desync=multidisorder:pos=2,5,105,host+5,sld-1,endsld-5,endsld:strategy=18
--lua-desync=multisplit:pos=1,2:seqovl=4:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=19
--lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=20
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=20
--lua-desync=multisplit:pos=2,sld:seqovl=620:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=20


целиком не влезает в два сообщения ловите...

---

**2026-03-30T10:11:18 | Inko**
--lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=21
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=21
--lua-desync=multisplit:pos=2,sld:seqovl=2108:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=21
--lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:strategy=22
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=google.com:strategy=22
--lua-desync=multisplit:pos=2,sld:seqovl=2108:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=22
--lua-desync=tls_client_hello_clone:blob=cloned_tls:fallback=fake_default_tls:strategy=23
--lua-desync=fake:blob=cloned_tls:optional:tcp_ts=-600000:tls_mod=rnd,dupsid,sni=www.google.com:strategy=23
--lua-desync=hostfakesplit:ip_id=zero:host=www.google.com:altorder=1:tcp_ts=-600000:strategy=23
--lua-desync=fake:blob=0x00000000:tcp_seq=-10000:tcp_ack=-66000:repeats=2:strategy=24
--lua-desync=fake:blob=fake_default_tls:tcp_seq=-10000:tcp_ack=-66000:repeats=2:tls_mod=rnd,dupsid,sni=www.google.com:strategy=24
--lua-desync=multisplit:pos=1,midsld:strategy=24
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_ts=-600000:repeats=6:strategy=25
--lua-desync=fakedsplit:ip_id=zero:pattern=0x00:tcp_ts=-600000:strategy=25
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=fonts.google.com:strategy=26
--lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=26
--lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=26
--lua-desync=fake:blob=blob_tls_clienthello_t2_ru:optional:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=m.ok.ru:strategy=27
--lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=0:tcp_ack=-66000:badsum:tls_mod=none:strategy=27
--lua-desync=fakeddisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_gosuslugi_ru:pattern=blob_tls_clienthello_vk_com:tcp_seq=0:tcp_ack=-66000:badsum:strategy=27
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_ts=-600000:repeats=8:strategy=28
--lua-desync=multisplit:pos=1:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:ip_id=zero:strategy=28
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1:strategy=29
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4:strategy=29
--lua-desync=fake:blob=0x00000000:tcp_seq=-10000:tcp_ack=-66000:strategy=30
--lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:strategy=30
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=fonts.google.com:strategy=30
--lua-desync=multidisorder:pos=10,midsld:seqovl=336:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=30
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1:strategy=31
--lua-desync=fake:blob=fake_default_tls:badsum:tls_mod=sni=rzd.ru:repeat=8:strategy=31:final

---

**2026-03-30T15:02:58 | Bullet for my valentine Poison**
Fakeip включить или выключить?

---

**2026-03-30T23:50:00 | Роман**
--lua-init=fake_default_tls=tls_mod(fake_default_tls,'rnd') --payload=tls_client_hello --lua-desync=multidisorder:pos=2,midsld:seqovl=1:seqovl_pattern=fake_default_tls
--payload=tls_client_hello --lua-desync=multisplit:pos=10,sniext+1:seqovl=1
--lua-desync=syndata --payload=tls_client_hello --lua-desync=multisplit
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=100
Протестируйте кому не лень на ютубе.

---

**2026-03-31T01:01:58 | Станислав Земляков**
Первые две - работают. В третьей смутило то, что нет blob=fake_default_tls к syndata. В четвёртой: repeats=100

---

**2026-03-31T12:08:54 | HiLLL**
а FakeIP отлетает?

---

**2026-03-31T12:50:31 | Владимир Волков**
Опять же, ждать, пока раздуплится. А ещё лучше - проверять с выключенным fakeip. Гоните меня, насмехайтесь, но всё ещё считаю, что работает с ним странно

---

**2026-03-31T16:32:54 | AleXXXey**
В авг: 
fakeIP - вкл/выкл? WhatsApp работает? На метовские сайты ходит?

---

**2026-03-31T16:41:32 | ㅤРоман**
fakeip включен(галка не стоит), вотсапп не пользуюсь но в приложении вверху слово "подключение" быстро пропадает, наверно работает. что за ментовские сайты? 😁 метовские....

---

**2026-03-31T16:56:16 | AleXXXey**
(опять заподозрили, что я дядя майор)😂


Работу вотсапп я проверяю так - захожу в чат с любым контактом и, если под именем появляется время последнего его нахождения в сети, то работает (при условии, если у контакта не скрыт статус или у вас).

У меня немного другая ситуэйшн. В семье пользуются вотсаппом(по работе) и инстой. Поэтому мне нужны обе социалки. 

А для рабочей инсты достаточно списка мета и включённого fakeIP (в любой секции), но эт в моём случае(с провайдером).

---

**2026-03-31T17:29:26 | AleXXXey**
Днс починить, в смысле, поменять на другой?


Когда у меня стоит в секции список мета, fakeip вкл, то через nslookup  whatsapp.com - fakeip отрабатывает. Могу сейчас ещё раз проверить.

Или я неправильно понял?

---

**2026-03-31T17:40:15 | Роман**
У меня под WhatsApp отдельная секция с amnezia 2.0, с отключенным fakeIP, довольно быстро работает.

---

**2026-03-31T17:51:34 | AleXXXey**
Крч. продублировал секцию с авг. Добавил мету и cdn aws в списки. fakeip вкл. Поменял днс с гугла на CF (1111 и 1001). 
nslookup - ок.

Результат: тю-тю

---

**2026-03-31T19:09:51 | Роман**
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1

ttps://t.me/routerich/462347/462502

---

**2026-04-01T13:00:05 | Routerich**
из нововведений новая опция, которая принесёт ещё больше проблем. это что-то типа полного прокси ip, но уже для доменов секции при выключенном fakeip, игроманам может понадобиться

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

**2026-04-01T14:35:23 | Vasa**
Вендоры DPI выработали эвристики, определяющие MTProxy Fake-TLS

Вероятно, без фиксов на клиентах Telegram смысла править что-то на стороне telemt нет

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

**2026-04-01T19:57:51 | Routerich**
С fake tls норм

---

**2026-04-01T20:35:26 | Дмитрий Григорьев**
443 Порт занят Xray
Шо делать, или это только для fake tls?

---

**2026-04-02T12:00:33 | Stanislav Gurov**
Могу поделиться своей циркуляркой для ютуба, у меня работает везде, в том числе на телевизоре Samsung с Tizen OS. На айфоне иногда подтормаживает, но в целом приемлемо.
--out-range=-s34228
--payload=tls_client_hello
--in-range=-s5556
--lua-desync=circular:fails=3:maxtime=60
--in-range=x
--lua-desync=fake:blob=fake_default_tls:tls_mod=rnd,dupsid,sni=www.google.com:tcp_ts=-1000:ip_id=zero:repeats=8:strategy=1
--lua-desync=multisplit:pos=1:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:ip_id=zero:strategy=1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:tcp_ts=-1000:ip_id=zero:repeats=6:strategy=2:final

Важное замечание: здесь используется стратегия с ts, которая требует предварительного включения временных меток в TCP/IP в Windows (в остальных ОС уже включены по умолчанию). Необходимо выполнить следующую команду в командной строке:
netsh interface tcp set global timestamps=enabled

---

**2026-04-02T23:52:21 | Роман**
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1
Эти попробуйте. Но так - да, перебором.

---

**2026-04-03T00:01:14 | ㅤㅤ**
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
 --out-range=<s1 --lua-desync=send:tcp_md5
--payload=tls_client_hello
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1

---

**2026-04-03T15:04:50 | Мирослав**
Здравствуйте, не получается настроить подписку влесс чтобы через нее работал aistudio. на компе работает через трон.
Думаю на рр днс нужно донастроить.
Нужно ли выключать fakeip?

---

**2026-04-03T15:33:20 | Роман**
У меня с meta работает, но с отдельным ВПН Amnezia 2.0 и с отключённым fake ip.

---

**2026-04-03T17:45:22 | Anna Bagler**
Интересно, по 4pda fakeip у вас не отрабатывает. Попробуйте сменить пару DNS/bootstrap. А если именно на роутере послать dns-запрос на 4pda, что показывает?

---

**2026-04-03T19:26:37 | Мирослав**
похоже у вас включен fakeip?

---

**2026-04-03T19:45:20 | Yury Kuzmenko**
включите fake Ip и закиньте ютуб в секцию, есть реклама значит вас видит как зарубеж, нет рекламы значит только менять сервак

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

**2026-04-04T10:18:28 | Marina V**
Уважаемые согрупники, такой вопрос. Вчера на Рутериче вырубило сеть. Подумала сбой в доме, но нет. Пробовала перезагрузить и прочие танцы с бубнами. Решила уже звонить в Ростелеком, но на всякий случай перед звонком поменяла на свой старенький. И о чудо, сеть есть, всё работает! Слышала, что РКН дал указание блокировать подозрительные IP (на рутериче стоит fake ip mode). Это значит докапался Ростелеком и блокирнул или что-то в настройках самого роутера слетело?

---

**2026-04-04T10:18:34 | Никита**
Пожалуйста, помогите с fake IP-адреса. На ноутбуке не удаётся получить доступ к сайтам, а на телефоне появляется ошибка, но при этом всё работает нормально.

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

**2026-04-04T17:49:03 | Anna Bagler**
Интересные результаты по fakeip. Диагностику подкопа с устройств покажите.

---

**2026-04-04T19:34:26 | Денис**
Так и осталась ошибка Fake Ip

---

**2026-04-04T20:00:07 | Денис**
При проверке nslookup fakeip.podkop.fyi выдает по идее правильно

---

**2026-04-04T20:12:07 | Routerich**
нельзя пинговать fakeip

---

**2026-04-04T21:06:41 | Роман**
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
--payload=tls_client_hello 
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1

Для начала 2 стратегии для Дискорда.

---

**2026-04-04T22:18:54 | Денис**
За что вообще отвечает Fake Ip. Для чего он нужен? У меня работает ютуб, инстаграм, тг, гпт

---

**2026-04-04T23:02:13 | Kiss_My_Axe**
Ну в процессе буду добавлять, не смертельно.
Пока тестскрипт запускает оналллизатор подкопа и грепает оттуда
⚠️ Router DNS is NOT routed through sing-box
❌ Sing-box does NOT work with FakeIP: ;; communications error to 127.0.0.42#53: connection refused

Потом, возможно, через case перевод воткну.

---

**2026-04-05T09:58:38 | Роман**
--lua-init=fake_default_tls=tls_mod(fake_default_tls,'rnd') --lua-desync=wssize:wsize=1:scale=6 --payload=tls_client_hello --lua-desync=multidisorder:pos=2:seqovl=1:seqovl_pattern=fake_default_tls

--lua-init=fake_default_tls=tls_mod(fake_default_tls,'rnd') --lua-desync=wssize:wsize=1:scale=6 --payload=tls_client_hello --lua-desync=multidisorder:pos=midsld:seqovl=midsld-1:seqovl_pattern=fake_default_tls

---

**2026-04-05T14:43:13 | Георгйи**
как можно исправить ошибку Proxy traffic is not routed via FakeIP?

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

**2026-04-06T12:10:17 | Роман**
--lua-init=fake_default_tls=tls_mod(fake_default_tls,'rnd') --lua-desync=wssize:wsize=1:scale=6 --payload=tls_client_hello --lua-desync=multidisorder:pos=2:seqovl=1:seqovl_pattern=fake_default_tls

--payload=tls_client_hello --lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1

---

**2026-04-06T13:58:08 | Bullet for my valentine Poison**
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN
--lua-desync=multidisorder:pos=2,midsld:seqovl=1:seqovl_pattern=fake_default_tls

---

**2026-04-06T14:36:02 | Routerich**
v0.9.4.7 (31 марта)
nfqws2 не падает при ошибке tls_mod dupsid/rndsni/padencap
поиск стратегий — опция Combo reverse (split first, then fake)

---

**2026-04-06T16:56:42 | Yury Kuzmenko**
#1 fixed: 2
  nfqws2 --payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN:repeats=1 --lua-desync=multidisorder:pos=midsld
  hosts: discord.com, discord.com работает

  #2 fixed: 2
  nfqws2 --payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:tcp_ts=-1000:repeats=1 --lua-desync=hostfakesplit:midhost=midsld:tcp_ts=-1000:repeats=1
  hosts: discord.com, discord.com 
Стратегии под дс

---

**2026-04-06T17:15:07 | Святос**
Во если на всех, то смотрите в закрепе великую стратегию, или...

--out-range=-s34228
--payload=tls_client_hello
--in-range=-s5556
--lua-desync=circular:fails=3:maxtime=60
--in-range=x
--lua-desync=fake:blob=fake_default_tls:tls_mod=rnd,dupsid,sni=www.google.com:tcp_ts=-1000:ip_id=zero:repeats=8:strategy=1
--lua-desync=multisplit:pos=1:seqovl=681:seqovl_pattern=blob_tls_clienthello_www_google_com:ip_id=zero:strategy=1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:tcp_ts=-1000:ip_id=zero:repeats=6:strategy=2:final

---

**2026-04-06T19:20:46 | AleXXXey**
шо-то у мня траблы со стимом🤷🏿‍♂️
не грузит ни шиша.

я ж правильно понимаю, что в nslookup стим не должен отдавать fakeIP, если в секцию не добавлен?

---

**2026-04-06T19:29:40 | Routerich**
тогда не может он fakeip показывать

---

**2026-04-07T00:15:45 | Сергей Никифоров**
Всем привет! После запуска диагностики, проверка FakeIP (клиент) завершилась с ошибкой Не удалось проверить: Load failed
Подскажите, в чем может быть проблема?
Openwrt 24.10.5
Zeroblock 0.7.2-r52

---

**2026-04-07T05:31:15 | AleXXXey**
крч. обратил внимание в логах, что синг бокс пытается дать fakeIP стиму и эпику. Потом выдаёт response rejected и получает реальный IP. Зачем? Почему пытается фэйкапить, если их нет в списках?

Фигня какая-то. Понимаю, что я глуповатенький. Ну хоть ты тресни по моей бошке, не понимаю, что мешает открыться стиму, эпикам и мелкомягким. Похоже на конфликт пересечений. Но пересечений нет.

Предположил, мож cdn AWS  мешает, но его отключение тож эффекта не дало.

ЗБ стопорю или включаю сидры - стим\эпик\майки полетели.

🤯

---

**2026-04-07T10:20:00 | Rom@n**
NFQWS_OPT_DESYNC_WG="${NFQWS_OPT_DESYNC_WG:---dpi-desync=fake --dpi-desync-repeats=2}"

---

**2026-04-07T11:57:18 | Routerich**
скрины
DNS проверки
Sing-box проверки
Outbounds проверки
FakeIP проверки

---

**2026-04-07T12:30:37 | Артём**
ребят я намучился с роблоксом и у меня получилось сделать рабочим заход в приложение, а к серверам не конектит выдаёт ошибку 279 кто сможет исправить пинганите меня потом, вот сама стратегия:"--lua-desync=multidisorder:pos=1,midsld:seqovl=681:seqovl_pattern=fake_default_tls
--lua-desync=fake:blob=fake_default_tls:repeats=2"

---

**2026-04-07T15:41:13 | Andrey Volgin**
а можете пожалуйста поделиться настройками в RR по awg20, с телефона meta работает, а вот в RR не хочет.

Настроил отдельный интерфейс по пример awg10 (галочка не создавать маршруты стоит), импортировал конфиг, handshake проходит в разделе VPN, добавил его в zb, убрал fake ip остальные настройки аналогично awg10, список meta не работает, куда копать?

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

**2026-04-08T10:03:34 | Сергей Никифоров**
Всем привет!
Ставил Zeroblock по мануалу на чистую новую прошивку, не проходили проверки FakeIP, как в диагностике так и по скрипту.
Поставил podkop так же на чистую новую прошивку скриптом из beta, проверки FakeIP проходят, как в диагностике так и скриптом.
Подскажите, в чем может быть проблема?

---

**2026-04-08T14:30:56 | Роман**
Я сделал отдельную секцию с Amnezia 2.0, с отключенным FakeIP, с одним списком Meta.

---

**2026-04-08T18:34:54 | R4KN_tyan**
Не знаю сюда или нет вопрос , не могу понять почему при такой настройке , где serv - это сервер wg, при конекте на роутер через РТ сеть zb нормально даёт прописанный днс fakeip и прекрасно роутит , а если я пытаюсь через мегафон - то он в тоннеле пихает свои DNS ip , вследствии чего zb не раскидывает роутинг.

---

**2026-04-08T22:06:08 | IM-Garage**
AWG не работает уже месяца два, проблем с FakeIP не было

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

**2026-04-09T11:30:29 | Роман**
похоже fakeip не срабатывает

---

**2026-04-09T15:26:52 | Anna Bagler**
fakeip отрабатывает. Проверьте сейчас на ПК.

---

**2026-04-09T21:04:31 | Vsevolod Chirkov**
Добрый вечер!
Столкнулся с проблемой в работе podkop, некоторое время назад отвалился discord (при этом работает находящийся в той же секции telegram). Диагностика на уровне службы зависает на стадии "DNS проверки", также таймаут получаю при попытке проверки fakeip. Версию подкопа обновил до актуальной (0.7.14). Перезапускал как саму службу, так и роутер, однако это не помогло. Сейчас прогнал скрипт анализа в терминале, прикладываю скриншот к сообщению. Вы не могли бы помочь разобраться в том, что именно вызывает проблему с DNS?

---

**2026-04-10T07:42:52 | Сергей Матвеев**
Что проверить? Fakeip пишет проблемы

---

**2026-04-10T10:53:13 | Dance4Life**
Ну кстати на компе телега работает только в той вкладке, что была открыта до падения. В новой пишет ERR_CONNECTION_RESET
И еще подкоп считает, что Прокси-трафик не маршрутизируется через FakeIP

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

**2026-04-10T11:16:19 | Arsen S**
Всем привет! Друзья, помогите плиз. В диагностике подкопа в Outbounds main Не отвечает и как следствие "Прокси трафик не маршрутизируется через FakeID". Sand-box рестартил, подкоп тоже. В настройки месяца полтора не лазил.

---

**2026-04-10T11:44:43 | Gomer Simpson**
Попробуйте DNS а ZB поменять на 9.9.9.9. И убедитесь, что в секции proxy FakeIP включён.

---

**2026-04-10T11:50:30 | Александр Кручинин**
🥸 FakeIP status
⚠️ Router DNS is NOT routed through sing-box
❌ Sing-box does NOT work with FakeIP: ;; communications error to 127.0.0.42#53: connection refused
;; communications error to 127.0.0.42#53: connection refused
;; communications error to 127.0.0.42#53: connection refused
;; no servers could be reached
  
 ```

---

**2026-04-10T11:51:52 | Vlad**
Поменял, проверил - FakeIP включен. Но гемини всё ещё не работает(

---

**2026-04-10T12:47:23 | дмитрий**
Что делать с fakeIP кто нибудь знает ?

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

**2026-04-10T17:42:33 | Anna Bagler**
Да. По fakeip нормально. Должно работать. В самом тг прокси не включен?

---

**2026-04-10T18:54:36 | ㅤㅤ**
У меня в секции awg10 работает, просто список Torrent
Диагностику ZB проводили? FakeIP

---

**2026-04-10T18:55:47 | Артём Буданов**
Приветствую! А где этот FakeIP?

---

**2026-04-10T20:46:22 | lexus**
бред какой то, обновил прошивку, сбросил, поставил бета скрипт сначало fake ip проверка была норм, телега не работала, перезагрузил, телега заработала, но вот опять

---

**2026-04-10T21:46:34 | Сергей. Техадмин GC, Salebot, AMO**
Сделал. Осталось только main не отвечает . FakeIp тоже везде ок, кроме прокси трафик не маршрутизируется

---

**2026-04-10T21:54:52 | Slava Terentev**
С FakeIp пункт, это же из-за отвала мейна? Это влияет на что-то?

При проверке через урлу https://fakeip.podkop.fyi/check пишет, что fakeip = true

Влияет ли это на что-то?

---

**2026-04-11T10:27:41 | Andrey L**
Вопрос - при диагностике красное сообщение, что браузер не использует fakeip.
Пробовал по букварям и понял, что у меня вообще этот адрес не резолвится. Это теперь такая ситуация или пров мощно блочит?

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

**2026-04-11T11:14:42 | Миша Луничев**
Все привет подскажите пожалуйста в чём может быть беда и куда копать, вчера отвалился подкоп не заглужал list телеги клаудфаера и меты, установил  zeroblock вроде более менее настроил дигноситка показывает всё кул кроме   
FakeIP (клиент)  Не удалось проверить: Failed to fetch
Но на mac по wifi всё работает вроде стабильно, а на телефоне не открывается ни тг ни тик ток ни некоторые игры, при том что если закинуть домены игр в оперу 1 открывается другая нет, щас упала опера и не поднимается, закинул и домены в qwg  и ip нужных приложений не спасло, по логам кроме того что опера померла всё ок вроде. Подскажите куда смотреть пожалуйста

---

**2026-04-11T13:08:09 | Anna Bagler**
fakeip отрабатывает. Новости оставьте только в одной секции.

---

**2026-04-11T16:57:21 | Ilya ☀️**
Со вчерашнего дня перестал работать юпуп, твитч твиттер итд. Все последней версии, при диагностике пишет Proxy traffic is not routed via FakeIP

---

**2026-04-11T21:51:23 | Anna Bagler**
Ну, выключите/включите fakeip в секции. Посмотрите.

---

**2026-04-11T23:12:32 | Garsia**
А для чего отключать FakeIP?

---

**2026-04-11T23:28:04 | Garsia**
Это необходимо для сервисов, которые проверяют соответствие DNS и реального IP (банки,
CDN, игровые консоли).
Вот что там написано. Но для чего отключать FakeIP, если с ним всё работает - и работает быстрее?

---

**2026-04-12T01:38:33 | support**
Подскажите почему это не работает адекватно, ютюб работает, но все остально что на скринах пугает. 
NFQWS2_OPT="--filter-udp=443 --filter-l7=quic --hostlist-domains=youtube.com,googlevideo.com,youtu.be,googleapis.com,ytimg.com,ggpht.com,gstatic.com,google.com --out-range=-s34228 --payload=quic_initial --lua-desync=fake:blob=quic_initial:ip_ttl=6 --new --filter-udp=443 --filter-l7=quic --hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt --out-range=-s34228 --payload=quic_initial --lua-desync=fake:blob=quic_initial:repeats=6 --new --filter-tcp=80 --filter-l7=http --hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt --out-range=-s34228 --payload=http_req --lua-desync=fake:blob=http:tcp_md5 --lua-desync=multisplit:pos=method+2 --new --filter-tcp=443 --filter-l7=tls --hostlist-domains=youtube.com,googlevideo.com,youtu.be,googleapis.com,ytimg.com,ggpht.com,gstatic.com,google.com --out-range=-s34228 --in-range=-s5556 --lua-desync=circular:fails=1:maxtime=5 --in-range=x --payload=tls_client_hello --lua-desync=multidisorder:pos=1,midsld:strategy=1 --lua-desync=multidisorder:pos=1:seqovl=681:seqovl_pattern=tls_clienthello:strategy=2 --lua-desync=multidisorder:pos=10,midsld:seqovl=336:seqovl_pattern=tls_clienthello:strategy=3 --lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=4 --lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=www.google.com:strategy=5 --lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=google.com:strategy=6 --lua-desync=fakedsplit:pos=midsld:strategy=7 --lua-desync=multidisorder:pos=1,midsld,sniext:strategy=8 --lua-desync=multidisorder:pos=1,sniext+1,midsld-2,midsld,midsld+2:strategy=9 --lua-desync=fake:blob=tls_clienthello:ip_ttl=6:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=rzd.ru:repeats=4:strategy=9 --lua-desync=multidisorder:pos=2,5,105,sniext+5,midsld-1:strategy=10 --lua-desync=multisplit:pos=10:seqovl=1:strategy=11 --new --filter-tcp=443 --filter-l7=tls --hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt --out-range=-s34228 --payload=tls_client_hello --lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=2gis.com --lua-desync=multisplit:pos=2 --new --filter-l7=mtproto --payload=mtproto_initial --lua-desync=fake:blob=0x00000000 --new --filter-tcp=443 --filter-l7=tls --ipset=/opt/zapret2/ipset/zapret-ips-user.txt --out-range=-s34228 --payload=tls_client_hello --lua-desync=multidisorder:pos=1,sniext+1,midsld-2,midsld,midsld+2 --lua-desync=fake:blob=tls_clienthello:ip_ttl=6:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=rzd.ru:repeats=4"

---

**2026-04-12T13:33:34 | Bezrabotnый**
но у меня при таилскейле еще на sing-box в fake ip жалуется но вроде все работает

---

**2026-04-12T16:20:21 | Виталя**
Sun Apr 12 15:38:57 2026 user.notice ucitrack: Setting up /etc/config/zeroblock reload trigger for non-procd /etc/init.d/zeroblock
Sun Apr 12 15:39:43 2026 user.notice zeroblock: Starting ZeroBlock...
Sun Apr 12 15:39:43 2026 daemon.err zeroblock[7696]: [zeroblock] Starting ZeroBlock(0.7.2-r55)...
Sun Apr 12 15:39:46 2026 daemon.warn zeroblock[7696]: [health_monitor] Opera Proxy is not working
Sun Apr 12 15:39:48 2026 daemon.warn zeroblock[7696]: [subscription_parser] HTTP 502 from subscription server
Sun Apr 12 15:39:48 2026 daemon.err zeroblock[7696]: [singbox_gen] Section Norm: no parsed proxies from subscription
Sun Apr 12 15:39:56 2026 daemon.warn zeroblock[7752]: [health_monitor] Opera Proxy is not working
Sun Apr 12 15:39:56 2026 daemon.warn zeroblock[7752]: [health_monitor] Failed to recover Opera Proxy
Sun Apr 12 15:40:21 2026 daemon.err zeroblock[7696]: [config_builder] Sing-box failed to start within timeout
Sun Apr 12 15:40:21 2026 daemon.err zeroblock[7696]: [zeroblock] Failed to start ZeroBlock
Sun Apr 12 15:40:21 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: Error: Failed to start ZeroBlock
Sun Apr 12 15:41:28 2026 user.notice zeroblock: Stopping ZeroBlock...
Sun Apr 12 15:41:28 2026 daemon.err zeroblock[9204]: [zeroblock] Stopping ZeroBlock...
Sun Apr 12 15:41:32 2026 daemon.err zeroblock[9204]: [zeroblock] ZeroBlock stopped successfully
Sun Apr 12 15:41:33 2026 user.notice zeroblock: Starting ZeroBlock...
Sun Apr 12 15:41:33 2026 daemon.err zeroblock[9475]: [zeroblock] Starting ZeroBlock(0.7.2-r55)...
Sun Apr 12 15:41:36 2026 daemon.warn zeroblock[9475]: [health_monitor] Opera Proxy is not working
Sun Apr 12 15:41:40 2026 daemon.err zeroblock[9475]: [zeroblock] ZeroBlock started successfully
Sun Apr 12 15:41:46 2026 daemon.warn zeroblock[9557]: [health_monitor] Opera Proxy is not working
Sun Apr 12 15:41:46 2026 daemon.warn zeroblock[9557]: [health_monitor] Failed to recover Opera Proxy
Sun Apr 12 16:17:05 2026 daemon.err uhttpd[3176]: [info] luci: accepted login on /admin/services/zeroblock for root from 192.168.1.210
Sun Apr 12 16:17:40 2026 user.notice zeroblock: Stopping ZeroBlock...
Sun Apr 12 16:17:40 2026 daemon.err zeroblock[20351]: [zeroblock] Stopping ZeroBlock...
Sun Apr 12 16:17:43 2026 daemon.err zeroblock[20351]: [zeroblock] ZeroBlock stopped successfully
Sun Apr 12 16:17:45 2026 user.notice zeroblock: Starting ZeroBlock...
Sun Apr 12 16:17:45 2026 daemon.err zeroblock[20785]: [zeroblock] Starting ZeroBlock(0.7.2-r55)...
Sun Apr 12 16:17:49 2026 daemon.warn zeroblock[20785]: [subscription_parser] HTTP 502 from subscription server
Sun Apr 12 16:17:49 2026 daemon.warn zeroblock[20785]: [singbox_gen] Catch-all section norm: auto-disabled FakeIP (no exclusions)
Sun Apr 12 16:17:49 2026 daemon.err zeroblock[20785]: [singbox_gen] Section norm: no parsed proxies from subscription
Sun Apr 12 16:18:22 2026 daemon.err zeroblock[20785]: [config_builder] Sing-box failed to start within timeout
Sun Apr 12 16:18:22 2026 daemon.err zeroblock[20785]: [zeroblock] Failed to start ZeroBlock
Sun Apr 12 16:18:49 2026 user.notice zeroblock: Starting ZeroBlock...
Sun Apr 12 16:18:49 2026 daemon.err zeroblock[21221]: [zeroblock] Starting ZeroBlock(0.7.2-r55)...
Sun Apr 12 16:18:54 2026 daemon.warn zeroblock[21221]: [subscription_parser] HTTP 502 from subscription server
Sun Apr 12 16:18:54 2026 daemon.warn zeroblock[21221]: [singbox_gen] Catch-all section norm: auto-disabled FakeIP (no exclusions)
Sun Apr 12 16:18:54 2026 daemon.err zeroblock[21221]: [singbox_gen] Section norm: no parsed proxies from subscription

это при повторной попытке запуска

---

**2026-04-12T19:03:01 | Ярослав**
Кстати вот что мне ответил автор zapret2 на тему почему с десктопа все летает, а на мобиле нет:
"Скорее всего это связано с недоисправленным handshake мобильного клиента.
У меня тоже десктопная версия работает через fake tls proxy, а ведроидная нет.
Помогает только дурение со стороны сервака, и то не на всех провайдерах."

---

**2026-04-12T21:28:49 | Дмитрий**
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4

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

**2026-04-13T11:32:39 | IIlIlIlIIlIlIlIIIll**
fake ip работал

---

**2026-04-13T12:22:55 | Ivan Num**
Подскажите при добавлении vless нужно ли ставить галку fake ip ,?

---

**2026-04-13T12:59:51 | Ярослав**
Мне тут написали вот что: Скорее всего это связано с недоисправленным handshake мобильного клиента.
У меня тоже десктопная версия работает через fake tls proxy, а ведроидная нет.

---

**2026-04-13T16:21:28 | Routerich**
и fakeip не выключен на этой секции?

---

**2026-04-13T19:18:45 | Pavel**
Ааа, все пон) fakeip надо отключить или нет?

---

**2026-04-13T19:42:00 | Василий**
11. Если все хорошо, напротив AWG20 будет изменяться количество полученных и переданных пакетов.
12. Идем в Службы - ZeroBlock. Открываем раздел Секции маршрутизации , вводим имя новой секции AWG2 и жмем добавить секцию . Проверяем тип подключения - VPN- интерфейс, а сетевой интерфейс AWG20 . Проверяем, что включена галочка отключить FakeIP . И имя секции AWG2 .
13. Далее вкладка DNS - Тип протокола днс - через https (doh) , dns сервер 9.9.9.9(QUAD9) , Bootstrap DNS сервер - 9.9.9.9 (QUAD9) . Далее вкладка списки - там есть готовые списки сообщества. Выбираем по вкусу кому что нужно. «Ввод пользовательских доменов» - текстовое поле и ниже прописываем еще вручную дреса сайтов, что нам нужны (в рамках закона РФ!). Для проверки вписал 2ip.ru . Сохранить, Сохранить, Перезапустить (вверху справа).
14. Сеть - межсетевой экран . Напротив AWG нажимаем изменить . Ставим галочку на Маскарадинг . Проверяем пункт Охватываемые сети - AWG20 . Ниже Разрешить перенаправление из «зон источников» - ставим галочку Lan . Сохранить . Далее изменяем wan - Напротив WAN нажимаем Изменить . Ставим галочку на Маскарадинг . Охватываемые сети - оставляем галочку только wan . Разрешить перенаправление из «зон источников» - галочка Lan . Сохранить . Далее переходим к Lan - нажимаем изменить . Охватываемые сети - только lan . Разрешить перенаправление в 'зоны назначения' : AWG(AWG20) и wan(wan) . Убираем галочку на Маскарадинг . Сохраняем , сохраняем , применяем .

Проверяем работу ютуба, заходим в режиме инкогнито на 2ip.ru и 2ip.io
т.к. мы первый домен пускаем через впн, то там покажет айпи впн. а на втором сайте покажет домашний ip
Значит все работает!

Если плохо работает ютуб и почта гугл, то в ростелекоме помогло
следующее:
Система , автозапуск , найти youtubeUnblock СТОП ВКЛЮЧЕНО. Нажать на зелёную включено, чтобы она стала красной .

---

**2026-04-13T21:54:52 | ­**
Добрый вечер, подскажите пожалуйста, я провел тест и он мне написал стратегии, мне нужно эти стратегии как то реализовать? И как?
--payload=http_req --lua-desync=http_methodeol
--lua-desync=syndata
--lua-desync=syndata --payload=http_req --lua-desync=multisplit
--lua-desync=syndata --payload=http_req --lua-desync=multidisorder
--payload=http_req --lua-desync=fake:blob=fake_default_http:ip_ttl=2:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1

---

**2026-04-13T22:32:37 | iProxx**
Кстати, по поводу FakeIP. Ее нужно отключать в своей секции независимо от типа подключения (Proxy или VPN) ?
Просто в Zeroblock в секциях awg10 и opera proxy по умолчанию галочка снята.

---

**2026-04-13T22:34:21 | Роман**
Я например отключил fake ip для секции где WhatsApp, так приложение быстрее работает. В секции амнезия 2.0.

---

**2026-04-14T09:38:25 | Δ 𐌼 Î Ŧ ᚱ Ỵ**
В диагностике подкопа все нормально, кроме Fake IP

---

**2026-04-14T12:36:28 | Artem Mayorov**
Здравствуйте! Имеется данная Великая стратегия. Все супер. На телеках Самсунг работает, но каждое утро приходится перезапускать Zapret2 . Это нормальная история? Мне не в напряг конечно, но все равно... Мало ли...
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4

---

**2026-04-14T12:42:31 | Artem Mayorov**
специяльно скопировал сейчас прямиком из запрета 
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4

---

**2026-04-14T12:44:37 | Artem Mayorov**
есть еще вот такая сохраненная. Но я ее не тестировал:
--out-range=-s34228
--payload=tls_client_hello
--in-range=-s5556 --lua-desync=circular:fails=3:maxtime=60
--in-range=x
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1:strategy=1
--lua-desync=fake:blob=fake_default_tls:badsum:tls_mod=sni=rzd.ru:repeat=8:strategy=1
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1:strategy=2
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4:strategy=2:final

---

**2026-04-14T15:42:02 | Anna Bagler**
Fakeip отрабатывает. Хорошо проверяйте настройки браузера.

---

**2026-04-14T17:17:53 | Pavel**
Подскажите когда свой vless добавляешь галку нужно ставить на отключение fakeip? Не до конца понимаю толк этой штуки

---

**2026-04-14T20:51:08 | Роман**
С Вацапом я поступил кардинально, выделил ему целую секцию с амнезией и отключённым fake ip, приложение с сайта, всё работает, видеозвонки, сообщения.

---

**2026-04-14T20:57:00 | Роман**
--payload=tls_client_hello 
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
Две стратегии для Дискорда.

---

**2026-04-14T21:00:17 | Виктор**
Добрый вечер! Обновил прошивку, поставил ZeroBlock. Диагностику проходит, ошибок нет. Смущает, что секцию наобум создал и FakeIP не используется. В мануале только  пункты настроек, никаких рекомендаций. Может где подробнее почитать можно?

---

**2026-04-15T03:44:31 | T-hon**
Всем привет, перестал работать телеграмм даже в вебе, чатГПТ, ютуб
В чём может быть проблема?
Команда nslookup fakeip.podkop.fyi выполняется неверно, так как адрес не соответствует диапазону 198.18.0.0/15

Также команда curl -v https://fakeip.podkop.fyi/check работает неверно так как {"fakeip": false,

---

**2026-04-15T07:29:14 | Yury Kuzmenko**
Попробуйте в настройках секции убрать галку fake ip

---

**2026-04-15T07:29:32 | HiLLL**
в секциии Отключить FakeIP убрана галка?

---

**2026-04-15T15:28:11 | Routerich**
если 192.18.x.x значит работает, если fakeip не выключен
nslookup сайт

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

**2026-04-15T19:57:42 | Дмитрий Григорьев**
--out-range=-s34228
--in-range=-s5556
--lua-desync=circular:fails=3:maxtime=90
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1:strategy=1
--lua-desync=multisplit:pos=2:strategy=1
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1:strategy=2
--lua-desync=multisplit:pos=midsld:strategy=2
--lua-desync=fake:blob=fake_default_tls:badsum:repeats=1:strategy=3
--lua-desync=hostfakesplit:badsum:repeats=1:strategy=3
--lua-desync=fake:blob=fake_default_tls:tcp_flags_unset=ACK:repeats=1:strategy=4
--lua-desync=hostfakesplit:disorder_after:tcp_flags_unset=ACK:repeats=1:strategy=4
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN:repeats=1:strategy=5
--lua-desync=hostfakesplit:midhost=midsld:tcp_flags_set=SYN:repeats=1:strategy=5:final

---

**2026-04-15T20:30:47 | Роман**
Если на этом дискорд не запускается, значит нужно использовать другое.
--payload=tls_client_hello 
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1

---

**2026-04-15T20:59:59 | Routerich**
а выключи fakeip для секции

---

**2026-04-15T21:54:46 | Your_secret_friend**
Need help! 

Добрый вечер! Подскажите, может кто-то сталкивался с проблемой про настройке amneziaWG+podkop… 

Туннель работает, забирает весь трафик. В настройках подкопа убрал список сообщества и указал нужные мне домены, как телеграм, вотсапп, инста и тд, всё сохранил и перезапустил, но трафик так и уходит весь через amneziaWG:(

При диагностике подкопа - всё зеленое, кроме самой последней позиции - Прокси-трафик не маршрутизируется через FakeIP.

---

**2026-04-16T14:44:21 | Paradigm Shifter**
Тоже часто стал отваливаться fake ip. Использовал код который скинули выше, и сейчас заработало.

---

**2026-04-16T15:44:54 | Ярослав**
Пробовал zapret2 на t.me Ростелеком Москва. Кто нибудь будет проверять на работоспособность?
--payload=tls_client_hello --lua-desync=fake:blob=0x00000000:tcp_flags_unset=ACK:repeats=1 --lua-desync=fake:blob=fake_default_tls:tcp_flags_unset=ACK:tls_mod=rnd,dupsid:repeats=1

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

**2026-04-16T19:08:32 | Bullet for my valentine Poison**
--out-range=-s34228
--payload=tls_client_hello
--in-range=-s5556 --lua-desync=circular:fails=3:maxtime=60
--in-range=x
--payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1:strategy=1
--payload=tls_client_hello --lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1:strategy=1
--payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN:repeats=1:strategy=2
--payload=tls_client_hello --lua-desync=fakedsplit:pos=1,midsld:tcp_seq=1000000:strategy=2
пробуй так. Я соединил 4 и поделил на 2. Список для DS брал отсюда?

---

**2026-04-16T19:14:46 | Bullet for my valentine Poison**
--out-range=-s34228
--payload=tls_client_hello
--in-range=-s5556 --lua-desync=circular:fails=3:maxtime=60
--in-range=x
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1:strategy=1
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1:strategy=1
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN:repeats=1:strategy=2
--lua-desync=fakedsplit:pos=1,midsld:tcp_seq=1000000:strategy=2

---

**2026-04-16T19:47:19 | Сергей**
Я там восстановил профиль по умолчанию, который завалился вниз
Вот страта, вроде самый дефолт из дефолтов

 --out-range=-s34228
--payload=tls_client_hello
--in-range=-s5556 --lua-desync=circular:fails=3:maxtime=60
--in-range=x
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1:strategy=1
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1:strategy=1
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN:repeats=1:strategy=2
--lua-desync=fakedsplit:pos=1,midsld:tcp_seq=1000000:strategy=2

---

**2026-04-16T20:35:44 | Егор**
У меня с дискордом подобная проблема. Пока ковырял настройки, выяснилось что после манипуляций с запретом стоит перезагрузить роутер. Почему-то даже на относительно рабочую страту дискорд без этого не запускался. В процессе поисков сработала эта стратегия
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
но звонки в ней работают через раз (не может к серверу подключиться) и медиа типа аватарок частично не прогружается. Пока хочу блокчек помучать, который тоже странно работает. То ищет, то нет. То что находит, запуску не помогает.

---

**2026-04-16T20:43:40 | Bullet for my valentine Poison**
Тогда сделай так:

--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1

--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN:repeats=1
--lua-desync=fakedsplit:pos=1,midsld:tcp_seq=1000000
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1

--payload=tls_client_hello
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1

--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN:repeats=1

--payload=tls_client_hello
--lua-desync=fakedsplit:pos=1,midsld:tcp_seq=1000000
еще можешь repeats=1 увеличить (2,4,6)

---

**2026-04-16T23:21:17 | Routerich**
короткий ликбез. браузер - tcp пакет - dnsmasq resolv - singbox sniff - fakeip/nofakeip - отправка серверу по ip

---

**2026-04-17T12:24:17 | яркек**
провайдеры отключали сейчас сеть (или какой-то сбой, тут хз)
после этого поднялся дискорд, но упали FakeIP

---

**2026-04-17T14:27:02 | Boris Gorshkov**
обновил пакет DNS Failsafe Proxy
далее сделал все по этой инструкции
в диагностике подкопа висит теперь ошибка
"Браузер не использует FakeIP" 
подскажите что не доделал ?

---

**2026-04-17T20:18:29 | Dallas13**
Вот это fakeip это для чего? Вроде все работает, но эта ошибка волнует

---

**2026-04-17T20:54:11 | Anna Bagler**
Есть. Тогда странно. Попробуйте включить/отключить fakeip для секции.

---

**2026-04-17T20:58:35 | Nick Chernobaev**
убрал fakeip. все также осталось. А что это значит? Проблема в amnezia конфиге?

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

**2026-04-17T23:50:43 | Andrew Arzaev**
все спасибо, нужно было указать dns, снять галочку (Отключить FakeIP для этой секции) и ребунуть

---

**2026-04-18T00:02:08 | Anna Bagler**
Fakeip отрабатывает. Внесите какой-то домен с проверкой IP в вашу секцию. И посмотрите, какой IP получаете.
Безопасный днс отключать в браузере.

---

**2026-04-18T00:08:17 | Михаил Краев**
Не могу побороть Spotify - а именно авторизацию у них через веб, не пускает регион блок (в апп все работает отлично).  Что пробовал, со своим прокси в zeroblock:
1. Основная (единственная) секция с нужными листами - включал Music. Не помогает. Добавлял кучу доменов - аналогично. 
2. Добавил новую секцию выше первой. Отключил fakeip. Добавил те же домены. Результат точно такой же.

---

**2026-04-18T14:43:12 | Алексей**
Здравствуйте! На новом роутере поставил скрипт № 5. Ютуб не заработал, и все остальное тоже. Поставил зероблок. Но у меня не настроены секции outbound и fakelp,  как их настроить?

---

**2026-04-18T15:46:46 | Роман**
Для вацапа отдельная секция с отключенным fake ip, всё работает включая видеозвонки. Apk с сайта обновляю руками,

---

**2026-04-18T15:49:54 | Aziz**
т.е с опера/awg убираете вотсап. 
Создаете новую секцию, ставите галочку fakeip и все работает в телефоне? даже видеозвонки?

---

**2026-04-18T16:02:05 | Aziz**
я думал конфиг для вотсапа отличается одной галочкой FakeIP. 
Если внутри еще сложности, то тогда вопросов нет.

---

**2026-04-18T17:30:05 | Vladislav Ivshin**
всем привет, пытаюсь найти рабочую стратегию для запрета, использую zapret2-finder(или Поиск стратегии в гуи), можете подсказать, что значит fixed и broken, и может ли быть fixed 14/14?
[21/4050] fake_default_tls_ttl4_ackdrop
          --payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:ip_ttl=4:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1
          fixed:  +10/14 SE.AKM-01(3.1M), US.CDN77-01(64K), US.CF-01(149K), US.CF-02(100K), LU.GCORE-01(121K), FI.HE-02(146K), FI.HE-03(1.0M), NL.SW-01(167K), DE.VLTR-01(623K), US.VLTR-01(76K)
          broken: !8/19 FR.CNTB-01(15K), FR.CNTB-02(15K), US.DO-01(0B), US.DO-02(0B), US.DO-03(0B), US.MBCOM-01(19K), FR.OVH-01(0B), FR.OVH-02(0B)

---

**2026-04-18T21:20:58 | Игорь**
Из стратегий для запрет2 я всё отключил стандартное, создал новую стратегию и использую только эти три:

--lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=3

--lua-desync=multidisorder:pos=1,midsld:strategy=9

--lua-desync=hostfakesplit:midhost=host-2:host=rzd.ru:tcp_seq=0:tcp_ack=-66000:badsum:strategy=13:final

---

**2026-04-19T01:03:22 | Anna Bagler**
@G_N_Mor fakeip не пробовали включить у секции и посмотреть?

---

**2026-04-19T03:02:21 | Routerich**
а мож fakeip починить?

---

**2026-04-19T09:37:29 | Роман**
Fake ip отключён, dns через outbound - зачем?

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

**2026-04-19T21:22:06 | Bullet for my valentine Poison**
Убрал кривое. Пробуй комбинировать:
--lua-desync=multi
--lua-desync=fake:blob

и можешь их менять местами, еще.
Нет, бери по одной строчке.
Вот пример как должно быть:
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN
--lua-desync=multidisorder:pos=2,midsld:seqovl=1:seqovl_pattern=fake_default_tls

---

**2026-04-19T23:08:47 | Владимир Волков**
Если используете новый подкоп, то там есть секции. В секциях есть галочка отключений fakeip. Надо пробовать включать/выключать/менять списки, не забывайте сохранять и применять настройки, перезапускать подкоп, роутер, и ждать минут 10 применения настроек (потому что днс кэш). Более подробно не сориентируем, потому что не знаем, как у вас там всё настроено.

---

**2026-04-20T01:56:52 | Павел**
Как-то непонятно работает секция оперы. Был подкоп - в нем все стабильно, все что в секциях - открывается. Перешел на ЗБ (подкоп отключен). Секция оперы открывает чатгпт, проверочные 2ipб которые там вписаны, все норм. Но рутрекер вообще ни в какую, ggsel (вписан руками - через зб не открывает). Включаю подкоп - все работает, как надо и быстро. Переустановить оперу или зб или что-то в настройках? fakeip нужен в опере? днс как там прописывать, 9.9.9.9?

---

**2026-04-20T11:45:59 | HiLLL**
попробуйте включить в секции FakeIP, снимите галку

---

**2026-04-20T11:49:18 | HiLLL**
всегда так, она ломает FakeIP

---

**2026-04-20T14:49:14 | Routerich**
Он и не должен пинговаться внутри fakeip

---

**2026-04-20T14:50:06 | Ivan Num**
Fake ip влияет на скорость и пинг?

---

**2026-04-20T23:18:46 | Docvspb 🇷🇺**
Камнями не кидайте, я на разбираюсь в деталях. Но Deepseek мне так написал о причинах:


Telegram — это сложная система, которая для разных задач использует разные серверы. Для медиафайлов в больших группах и каналах он часто обращается к своей CDN (сети доставки контента), IP-адреса которой могут меняться или отличаться от основных серверов мессенджера. 

Проблема в том, что ваш Zeroblock в режиме FakeIP пытается применить правила обхода (например, отправить трафик в VPN-туннель awg10) ко всем этим серверам. Но для конкретного CDN-сервера, который использует проблемная группа, этот маршрут по каким-то причинам не срабатывает. Возможно, этот сервер блокирует подключение из вашего VPN, или же пакеты теряются из-за особенностей работы туннеля.

Приложение Telegram на iPhone, в отличие от веб-версии, может быть более чувствительно к таким сбоям при загрузке медиа, что и приводит к ошибке.

---

