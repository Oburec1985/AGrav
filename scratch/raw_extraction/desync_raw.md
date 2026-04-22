# Raw Extraction: desync

**2026-01-01T13:46:44 | Bullet for my valentine Poison**
opt/zapret2/files/fake/quic_3.bin --lua-desync=fake:blob=quic_3  ты это имел ввиду?

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

**2026-01-04T14:15:13 | Роман**
В службах создать стратегию discord: 
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1

---

**2026-01-06T05:41:02 | Роман**
Попробовать стратегию:
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1

---

**2026-01-06T23:27:49 | Routerich**
а как мы видим из синтаксиса строк, я не хардкоржил ипв4 в стратегии
--name=blackhole
--filter-tcp=443
--filter-l7=tls
--out-range=-s34228
--payload=tls_client_hello
--hostlist-domains=bla.bla
--lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=100

---

**2026-01-07T22:12:23 | Роман**
Не только у меня, ещё несколько человек отписались что нормально работает. А так согласен, блокировки везде разные. Никто не мешает воспользоваться блокчеком и найти стратегии. 
У меня вообще Ютуб с этим работает 😁
 --lua-desync=multidisorder:pos=1,midsld,endhost-1

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

**2026-01-15T11:30:05 | Bullet for my valentine Poison**
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multisplit:blob=fake_default_tls:tcp_ts=-1000:pos=2:nodrop
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN

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

**2026-01-21T16:13:30 | Routerich**
главное чтобы desync mark был одинаковый

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

**2026-01-22T01:46:09 | Kiss_My_Axe**
Типа. Только верхние четыре строки я бы не трогал. Хотя могу ошибаться тут.
--out-range=-s34228
--in-range=-s5556 --lua-desync=circular:fails=2:maxtime=60
--in-range=x
--payload=tls_client_hello

Далее. 
Эти стратегии ВСЕ не применяются, применяется верхняя. Следовательно если Ю где-то не работает, верхнюю стратегию долой, Сохранить, Применить, дождаться перезапуска Z2, проверить снова.
И так до тех пор, пока не заработает везде.
Если из семи стратегий не подошла ни одна, возврат в блокчек, увеличение итогового количества стратегий и по новой искать-применять.

---

**2026-01-22T02:45:24 | Александр Меркушев**
Вот так например? Т.е

--payload=tls_client_hello 
--lua-desync=multidisorder:pos=1,midsld

для примера

---

**2026-01-25T21:30:46 | Dmitry**
Подскажите пожалуйста. Как пофиксить? Для запрета2 выставил Desync Mark = 0x400000. И все равно ошибка вылезает. И ошибку fakeip клиент никак победить не могу ..

---

**2026-01-26T08:17:42 | Routerich**
если выставлен desync mark именно такой, то поломато. по умолчанию стоит правильный

---

**2026-01-27T18:17:08 | AleXXXey**
судя по логам, он задействует первую страту:

* lua 'circular_1_1' : out pos a0 s1 in range a0-s34228
* lua 'circular_1_1' : payload_type 'tls_client_hello' satisfy filter
* lua 'circular_1_1' : desync
execution plan cancel from 'circular_1_1'
LUA: automate: host record key 'autostate.circular_1_1.content-autofill.googleapis.com'
LUA: circular: start from strategy 1
LUA: circular: current strategy 1.

Ок. А дальше, что?

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

**2026-01-31T16:08:29 | Роман**
Так далеко я не заходил (репиты), обычных стратегий с головой хватает. У меня Ютуб вообще с --lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1 работает.

---

**2026-01-31T16:10:13 | Роман**
Или вообще --lua-desync=multidisorder:pos=1,midsld,endhost-1

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

**2026-02-01T15:25:43 | Виль**
список доменов добавлял, только я так понимаю, я включал его в стратегию для ютуба, а также нашел в сообщениях стратегию для него:
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
вопрос, как это учесть или куда вписывать?

---

**2026-02-02T07:16:59 | Routerich**
я проверил на зависимость desync mark и трафик синга точно должен пролезать, но я не могу сказать на каком этапе работает zapret manager или что там у вас, так что проблема останется неисследованной

---

**2026-02-02T17:57:18 | Роман**
Значит искать другую стратегию. 
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
Эту попробуйте.

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

**2026-02-04T12:19:42 | Routerich**
сингбокс -> запрет2 по принципу перехвата. desync mark на выходе из синга не даст трогать пакеты запрету. я для кого трафик маркирую?

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

**2026-02-08T20:57:44 | JustKosha**
ну хз, вот с этим

--lua-desync=multidisorder:pos=1

--lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=1

и вот с этим

fbcdn.net

cdninstagram.com

connect.facebook.net

edge-mqtt-fallback.facebook.com

edge-mqtt.facebook.com

gateway.instagram.com

graph-fallback.instagram.com

graph.facebook.com

graph.instagram.com

i-fallback.instagram.com

i.instagram.com

ig.me

instagram.c10r.instagram.com

instagram.com

lookaside.facebook.com

scontent.cdninstagram.com

web.facebook.com

www.ig.me

www.instagram.com

z-p42-chat-e2ee-ig.facebook.com

супруга юзает через запрет 2

---

**2026-02-09T00:25:28 | Роман**
Метод https get использовали? Там нужно было галочку поставить. И снять ограничение на 5 стратегий, пусть бы искал. 
Я недавней ночью 77 стратегий перебрал, поэтому облегчу вам задачу, авось у вас моя стратегия заработает. 
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1

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

**2026-02-11T17:17:09 | Роман**
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
Эту попробуйте, возможности нет. Применить - перезапустить не забывайте.

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

**2026-02-13T23:15:06 | Routerich**
не получить, трафик из синга не попадает в запрет из-за desync mark

---

**2026-02-13T23:20:01 | Routerich**
необработанный трафик не нуждается в desync mark, потому что он необработанный и не запущен в reroute

---

**2026-02-14T16:52:42 | Роман**
Или эти попробуйте. 
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
--payload=tls_client_hello 
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1

---

**2026-02-15T03:08:37 | Prefect**
--out-range=-s34228
  --payload=tls_client_hello
  --in-range=-s5556 --lua-desync=circular:fails=3:maxtime=60
  --in-range=x

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

**2026-02-15T03:19:37 | Prefect**
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=20
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=20
--payload=tls_client_hello --lua-desync=multidisorder:pos=1,midsld
--payload=tls_client_hello --lua-desync=multidisorder:pos=1,midsld,1220
--payload=tls_client_hello --lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1

---

**2026-02-15T15:45:38 | Валерий**
Правильно я понимаю, что если blockcheck нашел стратегии, например:
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=2
--payload=tls_client_hello --lua-desync=multidisorder:pos=1

В NFQWS я вставляю: 
--out-range=-s34228
--in-range=-s5556 --lua-desync=circular:fails=2:maxtime=60
--in-range=x
--payload=tls_client_hello
--lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=1:strategy=1
--lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=1:strategy=2
--lua-desync=multidisorder:pos=2:strategy=3
--lua-desync=multidisorder:strategy=4

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

**2026-02-18T23:43:52 | А**
--payload=tls_client_hello --lua-desync=multisplit:pos=2
--payload=tls_client_hello --lua-desync=multisplit:pos=1
--payload=tls_client_hello --lua-desync=multisplit:pos=1,midsld
--payload=tls_client_hello --lua-desync=multisplit:pos=1,midsld,1220
--payload=tls_client_hello --lua-desync=multisplit:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--payload=tls_client_hello --lua-desync=multidisorder:pos=2
--payload=tls_client_hello --lua-desync=multidisorder:pos=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+1
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+4
--payload=tls_client_hello --lua-desync=multidisorder:pos=host+1

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

**2026-02-19T03:12:04 | вася778**
из pdf. сменил pppoe на dhcp и стал отваливаться запрет2 при запуске зб. в логе пишет 'Cannot check desync_mark'. на pppoe работает.

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

**2026-02-19T11:34:43 | Lelik**
--lua-desync=circular:fails=2:maxtime=60
Так? Это для всех? У меня везде не правильно стоит

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

**2026-02-19T16:56:22 | Станислав Земляков**
--payload tls_client_hello --lua-desync=fake:blob=fake_default_tls:tcp_ts=-1000

---

**2026-02-20T11:56:05 | Bullet for my valentine Poison**
смысл есть комбинировать, fake с блобом и multidisorder/multisplit. Это пока то что я на практике увидел. Но опять же, мне это нужно разобрать для полного понимания.
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost вот тут к примеру мне нужен разбор конкретный. "pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost" - что это, для чего, почему именно такой порядок и куда я могу это припихнуть. И с чем еще можно скомбинировать.😅 Так что я пойду дальше мучить копилота в режиме учебник.

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

**2026-02-21T17:55:49 | HiLLL**
Вам ютуб через запрет нужен? Попробуйте только ютубовская страта 
--out-range=-s34228
--payload=tls_client_hello
--in-range=x
--lua-desync=multisplit:pos=1,sniext+1:seqovl=12:strategy=1:final

---

**2026-02-21T19:14:47 | ㅤㅤHer01n 4dd1ct10n**
у меня не получается применить стратегии я глупенький(
вроде как бы и получил рабочие страты: 
--lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=1
--lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=1
--lua-desync=multidisorder:pos=2
--lua-desync=multidisorder:pos=1
--lua-desync=multidisorder:pos=sniext+1
--lua-desync=multidisorder:pos=sniext+4
но однако, применив их по инструкции ни к чему не пришел, но подозреваю что я делаю что-то неверно

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

**2026-02-22T00:31:39 | Aleksey Lip**
Здравствуйте, в зероблок при диагностике на zapret2 пишет "Cannot read desync_mark" в чем ступил?

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

**2026-02-24T21:15:50 | Роман**
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN
--lua-desync=multidisorder:pos=2,midsld:seqovl=1:seqovl_pattern=fake_default_tls

Эту стратегию попробуйте.

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

**2026-02-26T14:33:03 | XaleX**
пример --payload=tls_client_hello --lua-desync=multisplit:pos=2
откуда мне остальные значения взять

---

**2026-02-26T14:37:16 | XaleX**
мне выдало только 15 и большинство из них это desync

---

**2026-02-26T15:06:42 | Bullet for my valentine Poison**
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN
--lua-desync=multidisorder:pos=2,midsld:seqovl=1:seqovl_pattern=fake_default_tls
И вот пример моей страты для дс. Сначала идет строка с фэйком, а потом строка с мультидисордером.

---

**2026-02-26T15:33:51 | Routerich**
desync mark

---

**2026-02-26T15:36:19 | Routerich**
routing_mark = desync mark
    {
      "type": "direct",
      "tag": "awg10",
      "bind_interface": "awg10",
      "routing_mark": 1073741824,
      "domain_resolver": "dns-awg10"
    }

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

**2026-02-28T23:03:19 | Garsia**
Всем привет! Подскажите, плиз, как пользоваться Blockcheck2 - почему-то у меня ни фига не работает ни одна найденная им стратегия.
Делаю всё по мануалу:
1) Запускаю поиск стратегий для rutracker.org;
2) Найдены следующие:
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=2
--payload=tls_client_hello --lua-desync=multidisorder:pos=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+1
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+4
3) Создаю стратегию настройках запрета, выбираю заранее созданный список хостов "rutracker.org"
4) Вставляю в поле "Опции NFQWS" найденные стратегии (всё, что указано выше).
5) Сохранить, применить.

Но rutracker после этого всё равно не открывается.

Что я делаю не так?

---

**2026-02-28T23:38:01 | Garsia**
Можно вопрос?
Вот он мне выдал стратегии:
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=2
--payload=tls_client_hello --lua-desync=multidisorder:pos=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+1
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+4
Достаточно вставить всё это в поле "Опции NFQWS"? Или что-то ещё нужно? В мануале написано "Вставьте найденные стратегии...". Но тут в переписке ещё про какие-то шаблоны говорится

---

**2026-02-28T23:39:48 | Александр**
--payload=tls_client_hello --lua-desync=multidisorder:pos=2
--payload=tls_client_hello --lua-desync=multidisorder:pos=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=1,midsld
--payload=tls_client_hello --lua-desync=multidisorder:pos=1,midsld,1220
--payload=tls_client_hello --lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
  у меня просто так выглядит. Но это для Ютуба

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

**2026-03-02T13:53:37 | Lelik**
Всем привет. Где местные гуру?
Насканил стратегии блокчеком
blockcheck.sh
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=20
--payload=tls_client_hello --lua-desync=multidisorder:pos=2
--payload=tls_client_hello --lua-desync=multidisorder:pos=midsld
--payload=tls_client_hello --lua-desync=multidisorder:pos=1,midsld
По факту они не работают, где тут опечатки или что тут править что бы оно заработало?

---

**2026-03-02T14:00:38 | Роман**
--lua-desync=fake:blob=fake_default_tls:tcp_flags_set=SYN
--lua-desync=multidisorder:pos=2,midsld:seqovl=1:seqovl_pattern=fake_default_tls

--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1

Эти попробуйте.

---

**2026-03-02T14:18:23 | Lelik**
--payload=tls_client_hello --lua-desync=multisplit:blob=fake_default_tls:tcp_seq=1000000:pos=2:nodrop:repeats=1 --lua-desync=multisplit:pos=2
Ну хорошо, а здесь можно просто заменить параметр
blob=fake_default_tls
На какой-то конкретный блоб и скорее всего заработает?

---

**2026-03-02T21:48:00 | Routerich**
великая стратегия от самого известного должника @BFMVPoison, ходят легенды что на ней работает youtube на айфонах, телевизорах lg, пк и в редких случаях микроволновках
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4

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

**2026-03-03T23:26:03 | HiLLL**
у кого меньше?
--out-range=-s34228
--payload=tls_client_hello
--in-range=x
--lua-desync=multisplit:pos=1,sniext+1:seqovl=12

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

**2026-03-03T23:29:29 | Routerich**
--payload=tls_client_hello
--hostlist-domains=bla.bla
--lua-desync=tcpseg
а работать должно?

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

**2026-03-04T00:12:59 | Mallory**
я бы все-таки в мануале для домохозяек написал:

Получили стратегии в окошке Found Strategies, например

--payload=tls_client_hello --lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=1

Модифицируем их так (для youtube):

1. Добавляем шапку
--out-range=-s34228 --payload=tls_client_hello

2. К концу каждой стратегии добавляем запись с номером стратегии
:strategy=1 и т.д.

3. Помечаем последнюю стратегию
:final

В итоге получаем

# Общие настройки для всех последующих стратегий
--out-range=-s34228 --payload=tls_client_hello

# Первая стратегия
--lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=1:strategy=1

# Вторая и последняя стратегия (если первая не сработала)
--lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=1:strategy=2:final

---

**2026-03-04T12:38:46 | Bullet for my valentine Poison**
apis.rbxcdn.com (6):
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=2
--payload=tls_client_hello --lua-desync=multidisorder:pos=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+1
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+4

apis.roblox.com (6):
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=2
--payload=tls_client_hello --lua-desync=multidisorder:pos=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+1
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+4

gamejoin.roblox.com (5):
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=2
--payload=tls_client_hello --lua-desync=multidisorder:pos=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+1

roblox.com: working without bypass

www.roblox.com (5):
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=2
--payload=tls_client_hello --lua-desync=multidisorder:pos=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+1
смотри, вдумчиво смотри! внимательно!

---

**2026-03-04T12:42:07 | Bullet for my valentine Poison**
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+1

---

**2026-03-04T13:57:43 | Роман**
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=2
--payload=tls_client_hello --lua-desync=multidisorder:pos=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+1
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+4
--payload=tls_client_hello --lua-desync=multidisorder:pos=host+1

apis.roblox.com (6):
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=2
--payload=tls_client_hello --lua-desync=multidisorder:pos=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+1
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+4

gamejoin.roblox.com (5):
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=2
--payload=tls_client_hello --lua-desync=multidisorder:pos=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+1

roblox.com (6):
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=multisplit:pos=2
--payload=tls_client_hello --lua-desync=multisplit:pos=1
--payload=tls_client_hello --lua-desync=multisplit:pos=sniext+1
--payload=tls_client_hello --lua-desync=multisplit:pos=sniext+4

www.roblox.com (5):
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=2
--payload=tls_client_hello --lua-desync=multidisorder:pos=1
--payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+1
У меня так.

---

**2026-03-04T14:56:47 | Bullet for my valentine Poison**
--payload=tls_client_hello
--lua-desync=multisplit:blob=fake_default_tls:tcp_ts=-1000:pos=2:nodrop:repeats=2
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4
у кого там Роблокс под рукой. Чекните, запуск нормально идет?

---

**2026-03-04T15:14:46 | Bullet for my valentine Poison**
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1:repeats=2 попробуй заменить мультисплит.

---

**2026-03-04T22:49:25 | Святос**
--payload=tls_client_hello,http_req
--lua-desync=hostfakesplit:host=ya.ru:midhost=host-4:altorder=0:badsum:md5sig:badseq:badseq_increment=0:ip_id=seqgroup:tcp_ts_up
--out-range=-n6 --new

---

**2026-03-05T12:06:33 | Gomer Simpson**
Если есть желающие, вот моя стратегия: shell
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1

   Работает на всём: кампуктер, тв TCL А11, тв-бокс А14, смартфоны А15 и А16, официальный клиент, ReVanced, RVX, Vanced, SmartTube. А вот яблоков нету - за зиму сгрызли.

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

**2026-03-05T23:03:53 | Усатый Бро**
Подскажите в чем проблема cannot read desync_mark

---

**2026-03-06T07:18:14 | K**
великая стратегия от самого известного должника @BFMVPoison, ходят легенды что на ней работает youtube на айфонах, телевизорах lg, пк и в редких случаях микроволновках
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4

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

**2026-03-06T21:25:13 | KyM**
Метка Desync  в ZB и Z2 идентичны 0x40000000

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

**2026-03-12T10:34:34 | Роман**
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1
Здравствуйте. Эти стратегии попробуйте.

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

**2026-03-16T13:24:03 | Rom@n**
Искал и долго искал, вот например последние:
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=1
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=1
--in-range=-s1 --lua-desync=oob:urp=b
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
Но не одна не заработала

---

**2026-03-16T13:32:53 | Rom@n**
Ну я пробывал например это добавлять перед тем что нашёл Blockcheck2, например так:
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,midsld
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=1

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

**2026-03-16T14:50:19 | Rom@n**
например так:
--payload=tls_client_hello 
--lua-desync=multidisorder:pos=sniext+4:seqovl=sniext+3

---

**2026-03-18T14:21:18 | Bullet for my valentine Poison**
ты имеешь ввиду 
--payload=tls_client_hello --lua-desync=fake:blob=fake_default_tls:tcp_md5:tls_mod=rnd,dupsid,padencap:repeats=1 --payload=empty --out-range=<s1 --lua-desync=send:tcp_md5
это?

---

**2026-03-18T15:11:20 | Routerich**
* lua 'multisplit_2_2' : out pos a0 s1 in range a0-s34228
* lua 'multisplit_2_2' : payload_type 'tls_client_hello' satisfy filter
* lua 'multisplit_2_2' : desync
instance cutoff for 'multisplit_2_2' in=1 out=0
LUA: multisplit: split pos: sniext+1
LUA: multisplit: resolved split pos: 
LUA: multisplit: no valid split positions
* lua 'multisplit_2_3' : out pos a0 s1 in range a0-s34228
* lua 'multisplit_2_3' : payload_type 'tls_client_hello' satisfy filter
* lua 'multisplit_2_3' : desync
instance cutoff for 'multisplit_2_3' in=1 out=0
LUA: multisplit: split pos: sniext+4
LUA: multisplit: resolved split pos: 
LUA: multisplit: no valid split positions
* lua 'multisplit_2_4' : out pos a0 s1 in range a0-s34228
* lua 'multisplit_2_4' : payload_type 'tls_client_hello' satisfy filter
* lua 'multisplit_2_4' : desync
instance cutoff for 'multisplit_2_4' in=1 out=0
LUA: multisplit: split pos: host+1
LUA: multisplit: resolved split pos: 
LUA: multisplit: no valid split positions
* lua 'multisplit_2_5' : out pos a0 s1 in range a0-s34228
* lua 'multisplit_2_5' : payload_type 'tls_client_hello' satisfy filter
* lua 'multisplit_2_5' : desync
instance cutoff for 'multisplit_2_5' in=1 out=0
LUA: multisplit: split pos: midsld
LUA: multisplit: resolved split pos: 
LUA: multisplit: no valid split positions
* lua 'multisplit_2_6' : out pos a0 s1 in range a0-s34228
* lua 'multisplit_2_6' : payload_type 'tls_client_hello' satisfy filter
* lua 'multisplit_2_6' : desync
instance cutoff for 'multisplit_2_6' in=1 out=0
* lua 'multidisorder_2_11' : out pos a0 s1 in range a0-s34228
* lua 'multidisorder_2_11' : payload_type 'tls_client_hello' satisfy filter
* lua 'multidisorder_2_11' : desync
instance cutoff for 'multidisorder_2_11' in=1 out=0
LUA: multidisorder: split pos: sniext+1
LUA: multidisorder: resolved split pos: 
LUA: multidisorder: no valid split positions
* lua 'multidisorder_2_12' : out pos a0 s1 in range a0-s34228
* lua 'multidisorder_2_12' : payload_type 'tls_client_hello' satisfy filter
* lua 'multidisorder_2_12' : desync
instance cutoff for 'multidisorder_2_12' in=1 out=0
LUA: multidisorder: split pos: sniext+4
LUA: multidisorder: resolved split pos: 
LUA: multidisorder: no valid split positions
* lua 'multidisorder_2_13' : out pos a0 s1 in range a0-s34228
* lua 'multidisorder_2_13' : payload_type 'tls_client_hello' satisfy filter
* lua 'multidisorder_2_13' : desync
instance cutoff for 'multidisorder_2_13' in=1 out=0
LUA: multidisorder: split pos: host+1
LUA: multidisorder: resolved split pos: 
LUA: multidisorder: no valid split positions
packet: id=215 drop

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

**2026-03-20T08:56:00 | Alex Korshun**
Сейчас bc2 бегает на этих настройках и за 10 минут найдено пока 3 стратегии. 
--in-range=-s1 --lua-desync=oob:urp=b
--lua-desync=wssize:wsize=1:scale=6 --payload=tls_client_hello --lua-desync=multidisorder:pos=host+1
--lua-desync=wssize:wsize=1:scale=6 --payload=tls_client_hello --lua-desync=multisplit:pos=10,midsld:seqovl=1

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

**2026-03-20T23:01:51 | Gomer Simpson**
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1

---

**2026-03-20T23:33:28 | Routerich**
--out-range=-s34228
--payload=tls_client_hello
--in-range=-s5556 --lua-desync=circular:fails=3:maxtime=60
--in-range=x
--lua-desync=drop:strategy=1
--lua-desync=send:strategy=2:final
ня

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

**2026-03-22T00:25:27 | Alexey Zh**
я в целом там ничего не трогал кроме rr_youtube 
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4

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

**2026-03-24T16:41:20 | Святос**
--lua-desync=circular:fails=2:time=300:retrans=3:nld=2   и вот эдак написано

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

**2026-03-25T18:56:33 | Дмитрий**
МО, мегафон запрет2 "--payload=tls_client_hello --lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=1"

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

**2026-03-25T22:20:43 | Дмитрий**
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4
Этот пробовал?

---

**2026-03-26T09:09:17 | Святос**
Desync надо напяливать на VPN

---

**2026-03-26T10:47:27 | Artem Mayorov**
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4

Вот эта у меня. Эта два в одном?

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

**2026-03-27T22:47:23 | Святос**
--payload=tls_client_hello
--lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=fonts.google.com:tcp_seq=10000
--lua-desync=multisplit:pos=1,midsld:seqovl=1:seqovl_pattern=tls_clienthello:tcp_ts_up --new

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

**2026-03-30T23:40:18 | Роман**
--lua-desync=wssize:wsize=1:scale=6 --payload=tls_client_hello --lua-desync=multidisorder:pos=midsld
--lua-desync=wssize:wsize=1:scale=6 --payload=tls_client_hello --lua-desync=multidisorder:pos=1,midsld
--lua-desync=wssize:wsize=1:scale=6 --payload=tls_client_hello --lua-desync=multidisorder:pos=1
--lua-desync=wssize:wsize=1:scale=6 --payload=tls_client_hello --lua-desync=multidisorder:pos=sniext+1
Ну эти пять работают (у меня) ютуб.

---

**2026-03-30T23:50:00 | Роман**
--lua-init=fake_default_tls=tls_mod(fake_default_tls,'rnd') --payload=tls_client_hello --lua-desync=multidisorder:pos=2,midsld:seqovl=1:seqovl_pattern=fake_default_tls
--payload=tls_client_hello --lua-desync=multisplit:pos=10,sniext+1:seqovl=1
--lua-desync=syndata --payload=tls_client_hello --lua-desync=multisplit
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=100
Протестируйте кому не лень на ютубе.

---

**2026-03-31T19:09:51 | Роман**
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1

ttps://t.me/routerich/462347/462502

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

**2026-04-02T21:53:47 | Дмитрий Губанков**
Спасибо. Но видимо всё не так просто. Тем более, если посмотреть на те --lua-desync которые прописаны в стратегии youtube (там их много, а тут для телеграм всего одно... странно как-то). Наверное придётся потратить недельку-другую на изучение документации ))

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

**2026-04-04T21:06:41 | Роман**
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
--payload=tls_client_hello 
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1

Для начала 2 стратегии для Дискорда.

---

**2026-04-05T09:58:38 | Роман**
--lua-init=fake_default_tls=tls_mod(fake_default_tls,'rnd') --lua-desync=wssize:wsize=1:scale=6 --payload=tls_client_hello --lua-desync=multidisorder:pos=2:seqovl=1:seqovl_pattern=fake_default_tls

--lua-init=fake_default_tls=tls_mod(fake_default_tls,'rnd') --lua-desync=wssize:wsize=1:scale=6 --payload=tls_client_hello --lua-desync=multidisorder:pos=midsld:seqovl=midsld-1:seqovl_pattern=fake_default_tls

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

**2026-04-05T23:51:51 | Роман**
Ещё раз, вставляете стратегии - одна стратегия - одна строчка в блокчеке.
Например:
--lua-desync=wssize:wsize=1:scale=6 --payload=tls_client_hello --lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
Это одна стратегия. 

--lua-desync=wssize:wsize=1:scale=6 --payload=tls_client_hello --lua-desync=multidisorder:pos=midsld

Это вторая. 
Так и перебираете перезагружая ютуб.

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

**2026-04-06T21:37:15 | HiLLL**
Тут спорное утвержение. Я когда установил запрет у меня не завелось с той портянкой которая была по дефолту, а с милиписюшной стратой полетело. https://t.me/routerich/4/599472
--lua-desync=multisplit:pos=1,sniext+1:seqovl=12

---

**2026-04-06T22:21:46 | Роман**
--lua-desync=wssize:wsize=1:scale=6 --payload=tls_client_hello --lua-desync=multisplit:pos=10,midsld:seqovl=1

---

**2026-04-07T08:41:23 | Routerich**
всё что идёт в direct-out трогается запретом. конфликтов нет из-за desync mark

---

**2026-04-07T10:20:00 | Rom@n**
NFQWS_OPT_DESYNC_WG="${NFQWS_OPT_DESYNC_WG:---dpi-desync=fake --dpi-desync-repeats=2}"

---

**2026-04-07T12:30:37 | Артём**
ребят я намучился с роблоксом и у меня получилось сделать рабочим заход в приложение, а к серверам не конектит выдаёт ошибку 279 кто сможет исправить пинганите меня потом, вот сама стратегия:"--lua-desync=multidisorder:pos=1,midsld:seqovl=681:seqovl_pattern=fake_default_tls
--lua-desync=fake:blob=fake_default_tls:repeats=2"

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

**2026-04-10T18:27:25 | Дима Чуйков**
идут "Метка Desync (zapret2)" и сразу "Исключённые IP"

---

**2026-04-12T01:38:33 | support**
Подскажите почему это не работает адекватно, ютюб работает, но все остально что на скринах пугает. 
NFQWS2_OPT="--filter-udp=443 --filter-l7=quic --hostlist-domains=youtube.com,googlevideo.com,youtu.be,googleapis.com,ytimg.com,ggpht.com,gstatic.com,google.com --out-range=-s34228 --payload=quic_initial --lua-desync=fake:blob=quic_initial:ip_ttl=6 --new --filter-udp=443 --filter-l7=quic --hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt --out-range=-s34228 --payload=quic_initial --lua-desync=fake:blob=quic_initial:repeats=6 --new --filter-tcp=80 --filter-l7=http --hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt --out-range=-s34228 --payload=http_req --lua-desync=fake:blob=http:tcp_md5 --lua-desync=multisplit:pos=method+2 --new --filter-tcp=443 --filter-l7=tls --hostlist-domains=youtube.com,googlevideo.com,youtu.be,googleapis.com,ytimg.com,ggpht.com,gstatic.com,google.com --out-range=-s34228 --in-range=-s5556 --lua-desync=circular:fails=1:maxtime=5 --in-range=x --payload=tls_client_hello --lua-desync=multidisorder:pos=1,midsld:strategy=1 --lua-desync=multidisorder:pos=1:seqovl=681:seqovl_pattern=tls_clienthello:strategy=2 --lua-desync=multidisorder:pos=10,midsld:seqovl=336:seqovl_pattern=tls_clienthello:strategy=3 --lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=4 --lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=www.google.com:strategy=5 --lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=google.com:strategy=6 --lua-desync=fakedsplit:pos=midsld:strategy=7 --lua-desync=multidisorder:pos=1,midsld,sniext:strategy=8 --lua-desync=multidisorder:pos=1,sniext+1,midsld-2,midsld,midsld+2:strategy=9 --lua-desync=fake:blob=tls_clienthello:ip_ttl=6:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=rzd.ru:repeats=4:strategy=9 --lua-desync=multidisorder:pos=2,5,105,sniext+5,midsld-1:strategy=10 --lua-desync=multisplit:pos=10:seqovl=1:strategy=11 --new --filter-tcp=443 --filter-l7=tls --hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt --out-range=-s34228 --payload=tls_client_hello --lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=2gis.com --lua-desync=multisplit:pos=2 --new --filter-l7=mtproto --payload=mtproto_initial --lua-desync=fake:blob=0x00000000 --new --filter-tcp=443 --filter-l7=tls --ipset=/opt/zapret2/ipset/zapret-ips-user.txt --out-range=-s34228 --payload=tls_client_hello --lua-desync=multidisorder:pos=1,sniext+1,midsld-2,midsld,midsld+2 --lua-desync=fake:blob=tls_clienthello:ip_ttl=6:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=rzd.ru:repeats=4"

---

**2026-04-12T21:28:49 | Дмитрий**
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4

---

**2026-04-13T21:54:52 | ­**
Добрый вечер, подскажите пожалуйста, я провел тест и он мне написал стратегии, мне нужно эти стратегии как то реализовать? И как?
--payload=http_req --lua-desync=http_methodeol
--lua-desync=syndata
--lua-desync=syndata --payload=http_req --lua-desync=multisplit
--lua-desync=syndata --payload=http_req --lua-desync=multidisorder
--payload=http_req --lua-desync=fake:blob=fake_default_http:ip_ttl=2:repeats=1 --payload=empty --out-range=s1<d1 --lua-desync=pktmod:ip_ttl=1

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

**2026-04-14T20:57:00 | Роман**
--payload=tls_client_hello 
--lua-desync=multisplit:blob=fake_default_tls:tcp_flags_set=SYN:pos=2:nodrop:repeats=1
--payload=tls_client_hello
--lua-desync=fake:blob=fake_default_tls:tcp_seq=1000000:repeats=1
Две стратегии для Дискорда.

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

**2026-04-15T20:36:35 | Дмитрий Григорьев**
В этом не шарю, потенциально можно отключить второй запрет и поставить первый, метки Desync вроде там тоже есть

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

