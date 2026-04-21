# Raw Extraction: sni

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

**2026-01-05T01:18:53 | Vasa**
бле.. эт жесть

с ВАЛИДНЫМ SNI - домен на серваке - оно не пашет...

с левым типа ya.ru + MUX - запахало....)))

---

**2026-01-05T01:21:46 | Vasa**
ну у меня был один sni... на обоих. щас разделил уже))

---

**2026-01-05T01:23:41 | Vasa**
да эт ппц какой то...

ну я спецом p2p завёл чтоб проверить - банят IP или что то другое...

бан судя по всему по анализу SNI идёт до сих пор

---

**2026-01-05T01:24:06 | Aleksey Vydrin**
а esni уже не будет. всё

---

**2026-01-05T01:25:54 | Vasa**
не, было под домен из белых списков

щас уже свой стоит - вебсокеты и xhttp не пашут)

а с подменой SNI на яндекс - пашут...

---

**2026-01-05T01:26:37 | Vasa**
тоесть я беру вебсокеты с ssl, со своим доменом в SNI - неработает

ставлю яндекс - "небезопастно" - работают)

---

**2026-01-05T01:30:26 | Dark Ghost**
И при этом пашет с яшиным sni. 
Можно мне другие какие-нибудь маты?
А то известные ситуацию полностью описать не способны...

---

**2026-01-05T01:33:46 | Vasa**
не мой сервак... да уже понятно что в бан кидался SNI

я щас разделил проблема ушла

---

**2026-01-05T01:34:14 | Vasa**
недумаю. реалити он пропускает почему то... теперь)

но SNI пришлось сменить, да

---

**2026-01-05T01:38:45 | Dark Ghost**
Там два варианта известны - простой, по анализу sni, с ним прокатывает подобное. И жёсткий - по списку разрешенных подсетей, там только пытаться в них vps раздобыть, но обычному смертному, скорее, нереально.

---

**2026-01-10T15:27:14 | Vasa**
транспорт реалити ?
ну значит SNI меняй

либо перевесь на порт высокий, типа 59823

---

**2026-01-10T15:27:42 | Antonio_273**
уже все попробовал, и порты менял и sni

---

**2026-01-10T15:29:26 | Vasa**
ты высокие порты пробовал? как я написал?

с другого инета не пробовал проверять?

sni какой?

хостинг какой?

---

**2026-01-10T15:30:04 | Antonio_273**
высокие пробовал, sni разные перепробовал, яндексы, вк, майкрософт и т.д.
хостинг senko
год все работало нормально

---

**2026-01-10T15:33:16 | Vasa**
попробуй для теста порт выше 50000

sni оставь вообще пустой

проверь на ПК \ мобиле напрямую

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

**2026-01-11T04:12:36 | Борис**
Получается, не работают белые списки? Или бпла подключился к vless серверу под sni vk.com?

---

**2026-01-11T16:40:19 | Архипов Кирилл Александрович**
Так я тогда к vless с sni не могу подключиться без подкопа) А как подключусь инет появляется)

---

**2026-01-12T01:01:44 | Борис**
Можете меня поздравить. 1 шанс на миллион - был предположением. Реальность другая. Я обошёл белый список на телефоне при помощи домашнего роутера, подключившись к нему по VLESS. Помогла смекалка и бесчисленные попытки: нужно скопировать рабочий публичный конфиг КЛИЕНТА, вплоть до их SNI и соли (shortId), и только поменять там на свои UUID, public key, IP адрес, и можно 1 цифру в shortId заменить, и в принципе всё

---

**2026-01-12T01:30:16 | Борис**
я, наверное, немного сбил вас с толку - целый день трудился, голова уже плохо соображает. Шаблонный конфиг - имеется в виду, шаблонный рабочий конфиг для КЛИЕНТА (для телефона, например). Сервер придётся настраивать самому, шаблонов там особо нет. Главное, чтобы настройки клиент-сервер соответствовали (SNI, UUID, private/public key, short id, IP адрес)

tailscale был плох тем, что он у людей не работал или обрубался (банился протокол wireguard vpn, на котором он работает, поэтому связь с вашим роутером не устанавливалась или терялась)

---

**2026-01-12T01:34:14 | Борис**
может и можно сделать VLESS-тунель без белого IP - например, через CloudFlare Tunnel, но я не до конца разобрался, как этот китайский Vless работает, поэтому там скорее всего хендшейк будет с сервером Couldflare, который встречает и не в курсе этих приколюх про маскировку SNI и так далее...

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

**2026-01-19T01:17:51 | Kiss_My_Axe**
Не, реалити так-то месяца два как валить начали. Тогда и был наплыв.
Потом чота стихло.
По SNI, если память новым годом не отшибло.

---

**2026-01-19T16:32:23 | Панда**
router: duplicate sniff skipped кстати именно из-за этого

---

**2026-01-19T21:05:36 | Vasa**
Надо было починить пылик Xiaomi m40
Нашел этих "ребят". Созвонились, сказали приедут домой посмотрят. 
Ок, чёт якобы у них не вышли, сказали давайте Якурьера пришлём, заберем, так же потом вернем оплатите. 
Ну я чёт повёлся...

отдал в ремонт... ребята пропали )

ТГ игнорят, на звонки отвечают раз в неделю и кормят обещаниями.

Насколько я понял физического "места" у них типо нету. Ну и теперь уже поискав эти сайты нашёл клоны сайта в большинстве городов и по многим  брендам

https://xiaomi-service-center-remont.ru

Я конечно на 100% не уверен, но с учётом что скоро уже как месяц пройдет пылесос можно не ждать)

https://nn.lg-servisniy.center/kontaktyi

https://yaroslavl.gigabyte-servisniy.center/kontaktyi

https://samara.samsung-service-center-remont.ru/kontaktyi

https://kazan.huawei-service-center-remont.ru/kontaktyi

https://chelyabinsk.oneplus-service-center-remont.ru/kontaktyi

---

**2026-01-19T21:12:01 | Святос**
https://otzovik.com/reviews/oficialniy_servisniy_centr_xiaomi_servicecenterxiaomi_ru_russia/

---

**2026-01-19T23:21:15 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r51:
  - Удалены deprecated функции `sniff` и `sniff_override_destination`
  - Увеличен таймаут для offload bittorent до 60с
  - Добавлен Selector для Url_test
  - Добавлено уведомление о подключении к Clash API(Clash API ещё не стартовал, а пользователь уже открыл dashboard)
  - Добавлено тестирование задержки для секций при первом открытии
  - Немного переработан dashboard, теперь нет плашки активен, выбранный сервер отображается на первой карточке
#ZeroBlock

---

**2026-01-21T17:37:48 | Vasa**
отключи подкопы на роутере и проверяй с вифи

скорее всего надо настройку vless поменять \ порт \ sni \ протокол

смотря чё там наверчено у тебя

---

**2026-01-21T17:55:20 | Vasa**
ну пробуй без sni - вообще пустым оставь

либо его менять

либо порт 8443 или выше 50000 - 60000

еще можно чисто для теста сделать вебсокет, без TSL (шифрования) тож на рандомном порту

---

**2026-01-21T17:56:41 | McQueen 95**
Ох я хз как это делать к сожалению, что такое sni и как его убрать

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

**2026-01-23T12:07:55 | Камиль**
нужно ли включать sniffing для YT и discord ?

---

**2026-01-23T22:28:11 | McQueen 95**
Господа, столкнулся с необычной проблемой - перестали работать любые vless конфиги если подключен к вай фаю. Тестил на разных устройствах - ПК, 2 разных айфона на разных iOS 17 и 26. RR 24.10.2
Для проверки гипотез менял SNI (пустой, ya.ru, icloud), обновлял/удалял podkop дабы исключить участника цепочки. Грешил даже на VPS сервак (есть 3х-ui на аеза и 4впс), оказалось что конфиги рабочие т.к. на мобильных данных подключаются все конфиги и сайты грузятся.
Пришел к тому, что всё ломается на уровне роутера/вайфая.

Есть тесты nekoray, где в основном статус "Недоступен". При этом, v2rayTun на ПК говорит, что пинг имеется, конфиги доступны, но при подключении ничего не работает.

Это что получается в первую очередь всё равно прошивку менять?(

---

**2026-01-25T17:30:07 | Alex**
Всем привет!
Подскажите, пожалуйста, есть ли решение в связи с применением на оборудовании DPI (СОРМ) новых фильтров (паттернов) для VLESS, SS и т.д. и вытекающим отсюда шейпингом скорости до 2-3 мегабит?
PS. Старые уловки со сменой порта, sni, фингерпринта, транспорта и т.д. не помогают.

---

**2026-01-28T18:38:20 | Техническая Поддержка**
я с ним долго приседал, но в целом sni удалось раздуплить

---

**2026-01-28T22:35:44 | Техническая Поддержка**
так нет же, микротом в тоннель все заворачивается, а тут на уровне ядра пыхтеть приходится с sni

---

**2026-01-29T17:49:03 | Техническая Поддержка**
ну точно не sni/dpi разматываешь, покажи ip route

---

**2026-01-29T18:26:31 | Dark Ghost**
Ща, всё брошу (tm), и IP со SNI покажу, и логин/пароль, и цифры со всех сторон всех карт...

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

**2026-01-31T09:23:03 | Камиль**
hy2://df01e20ffa554305a62a5a143h5gfh43cb0a672aa@1.1.1.1:443/?obfs=salamander&obfs-password=Ml7sdWP31Jmu8a5h6m5hf5jh73V3umXH4dbg8Q8nTLYH&sni=super.ru
а чем ссылка поможет если на 443 ругается ?

---

**2026-01-31T09:45:37 | Камиль**
Методом проб и ошибок, нашел в чем дело

В данной ссылке 
hy2://df01e20ffa554305a62a5a143h5gfh43cb0a672aa@1.1.1.1:443/?obfs=salamander&obfs-password=Ml7sdWP31Jmu8a5h6m5hf5jh73V3umXH4dbg8Q8nTLYH&sni=super.ru
Есть / перед перечислением query параметров ?obfs=salamander&obfs-password=Ml7sdWP31Jmu8a5h6m5hf5jh73V3umXH4dbg8Q8nTLYH&sni=super.ru 
Если из этой ссылки убрать данный слеш т.е. сделать вот так

hy2://df01e20ffa554305a62a5a143h5gfh43cb0a672aa@1.1.1.1:443?obfs=salamander&obfs-password=Ml7sdWP31Jmu8a5h6m5hf5jh73V3umXH4dbg8Q8nTLYH&sni=super.ru

То zero её принимает ! Вдруг будет полезно

---

**2026-01-31T14:32:00 | Routerich**
curl -v https://googlevideo.com
* Host googlevideo.com:443 was resolved.
* IPv6: 2a00:1450:4010:c05::67, 2a00:1450:4010:c05::68, 2a00:1450:4010:c05::63, 2a00:1450:4010:c05::6a
* IPv4: 64.233.162.106, 64.233.162.147, 64.233.162.104, 64.233.162.103, 64.233.162.105, 64.233.162.99
*   Trying [2a00:1450:4010:c05::67]:443...
*   Trying 64.233.162.106:443...
* schannel: disabled automatic use of client certificate
* ALPN: curl offers http/1.1
* schannel: SNI or certificate check failed: SEC_E_WRONG_PRINCIPAL (0x80090322) - Главное конечное имя неверно.
* closing connection #0
curl: (60) schannel: SNI or certificate check failed: SEC_E_WRONG_PRINCIPAL (0x80090322) - Главное конечное имя неверно.
More details here: https://curl.se/docs/sslcerts.html

curl failed to verify the legitimacy of the server and therefore could not
establish a secure connection to it. To learn more about this situation and
how to fix it, please visit the webpage mentioned above.

---

**2026-01-31T16:08:29 | Роман**
Так далеко я не заходил (репиты), обычных стратегий с головой хватает. У меня Ютуб вообще с --lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1 работает.

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

**2026-01-31T16:19:29 | Bullet for my valentine Poison**
И обрати внимание, на вторую строчку страты. Там sni от ржд😅 (Но это уже Фреса подкинул) У нас кстати нет примера страты с подменой sni. Либо я слепой.

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

**2026-01-31T17:07:08 | Rom@n**
проверьте пожалуйста мою vless ссылку кому не сложно, есть ли подключение. Не пойму в чем дело, у меня локально на компе/провайдере что-то или на VPS. Но там вроде все ок. Ссылка тестовая, потом ее грохну.
vless://7945ed72-1a0d-44c3-9cbe-09d9eaf17d60@vpnvless.dedyn.io:443?type=tcp&encryption=none&security=reality&pbk=D0EDuX_2pPDzDjIpgEjoKWpqx7s9kNhHS4CWDOAV0FA&fp=chrome&sni=em-design.cz&sid=81b0e184&spx=%2F&flow=xtls-rprx-vision#wow-test

---

**2026-01-31T17:10:12 | Rom@n**
SNI тоже доступен

---

**2026-01-31T17:26:45 | Vasa**
SNI на хетзнере так то..
а его блочат

---

**2026-01-31T17:27:04 | Rom@n**
Понял начну со SNI

---

**2026-01-31T17:37:28 | Rom@n**
Да проблема была со SNI. Спасибо что подтолкнули. Но странно пол года работало)))

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

**2026-02-02T18:02:31 | Anna Bagler**
@Kydesnik_D тут спросите.

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

**2026-02-09T15:42:39 | Kiss_My_Axe**
Доступ восстанавливает, но список надо прореживать ещё. Мне просто лень. :)
www.androidpolice.com www.xda-developers.com xdaforums.com
adsninja.ca
applets.ebxcdn.com
beacon.tru.am
c1.sentinelpro.com
carrick-ui.advoncommerce.com
cdn.adsninja.ca
cdn.jsdelivr.net
cdn.privacy-mgmt.com
cdn.sentinelpro.com
geo.privacymanager.io
images.valnetcdn.com
in.getclicky.com
launchpad.privacymanager.io
launchpad-wrapper.privacymanager.io
region1.google-analytics.com
sb.scorecardresearch.com
static.getclicky.com
static0.anpoimages.com
static0.srcdn.com
static0.xdaimages.com
static1.xdaimages.com
stats.g.doubleclick.net
tru.am
valnetv3.sentinelpro.com

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

**2026-02-11T13:12:19 | Routerich**
там замедление по cidr+sni и похоже не связанное между собой, тут запрет как бы бесполезен

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

**2026-02-11T16:32:40 | ㅤ**
что бы белых списков поменьше, и не cidr а по SNI и всё в таком духе)

---

**2026-02-12T12:09:05 | Борис**
У меня белые списки, как и у всех Россиян в Краснодарском крае и других областях. Как я подключаюсь к роутеру? Очень просто. Для начала, как я и говорил, нужно настроить xray-сервер на роутере. Также важно иметь белый IP от провайдера на роутере — так можно будет принимать подключения из WAN от других участников телекоммуникационной сети Internet. Затем, на телефоне, находясь, скажем, в Орловской области, я добавляю конфигурацию своего xray-сервера в клиент NekoBox на Android — прописываю адрес роутера, выбранный порт, транспорт, UUID, публичный ключ, отпечаток Reality и всё в таком духе... Напоминаю, что мой телефон находится за 1000 км от роутера, я нахожусь в режиме подавляемого интернета ("белые списки" - только разрешенные ресурсы), поэтому доступ в интернет у меня по сим-карте. Когда конфигурация клиента на Nekobox настроена, я нажимаю кнопку "подключиться", и создаю туннель со своим роутером по протоколу vless reality. Провайдер видит, что я обращаюсь к некоему IP, указывая SNI = "m.vk.com", а поскольку сайт ВКонтакте разрешен в белых списках, провайдер на сим-карте разрешает такое соединение, и я подключаюсь к роутеру за 1000+ км (роутер Routerich отлично ловит!)

---

**2026-02-12T12:13:48 | Роман**
По sni уже давно всё поблочено. Схему выше я уже описал. 
Такое подключение прокатывало на заре становления БС. 
Ещё раз. При БС не помогут никакие sni, только сервера за бс. 
У нас это всё давно прикрыто и поблочено.

---

**2026-02-12T12:24:04 | Stanislav Shram**
Ночью в Крае врядли что то сработает, или просто везение что ip может в подсеть попал разрешенную, так как на sni им все равно, там чисто доступ к айпишникам только

---

**2026-02-12T12:39:31 | Fdoo**
цепочка очень простая на самом деле, просто тестирую разные, например, VPS в Москве клауд.ру
настроен простой WG - прямой доступ и прямой выход. работает всё что не запрещено РКН.
там же - марзбан, щадоусокс - прямой выход. затем там же 3xui  - vless reality tcp 443 порт, тестирую разные SNI.
vless reality tcp / xhttp  - на других портах - редирект что-то на warp,  что-то в финку, чтор-то в германию, что-то в штаты. исключительно спортивный интерес что как работает.
в европе - простой 3xui - c прямым выходом + Amnezia WG Server - тоже для тестов. Всё прекрасно работало до вчерашнего дня

---

**2026-02-12T12:58:49 | Борис**
Вообще для меня здесь много слов непонятных. Я не понимаю, зачем нужны warp, amneziaWg, протокол xhttp. Я предлагаю для теста отключить это всё, сделать самый дубовый конфиг с транспортом tcp, подключение через vless reality, и далее напрямую в интернет. И смотреть, работает ли сам сервер в таком режиме. Далее, если работает, уже пробовать добавить warp на выход и т.д.

Что касается подбора sni, я делал так - есть бесплатные подписки на 4pda, тема называется "суверенный интернет", там 2000+ бесплатных vless reality серверов. Нужно их себе импортировать, пропинговать тестом url, посмотреть, какие из них работают, и точь-в-точь себе скопировать их конфиг, за исключением ip и данных авторизации, естественно. Я с этого начинал 

Мне, как новичку, вообще непонятно, зачем такой оверхед добавлять в виде awg, warp и прочего. Чем сложнее система, тем ниже её устойчивость

---

**2026-02-12T17:15:04 | Vasa**
тут только 2 варианта

либо IP твоего прова, внешний, по какой то неведомой мне пока причине находится в белых списках адресов

либо у тебя не полноценные БС, а просто блоки по SNI

---

**2026-02-12T19:32:35 | Artem**
свой впн перестал работать, уже все sni перепробовал. что делать? какой sni щас работает?

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

**2026-02-13T09:23:38 | Lelik**
Ну так сразу сканить с нужным sni можно, например. Да и в целом приписывать что-то свое. В текущих реалиях уже нужно. Ну или может сделать в виде галки что-то из популярного

---

**2026-02-13T18:09:55 | Artem**
всем привет. свой vless перестал работать, уже все sni перепробовал. что делать?
сменил sni, один раз сайт загрузился и все, опять не работает

---

**2026-02-14T18:33:51 | Alex S**
Прошу прощения,галочка стояла на Fake sni,а на Synfake нет

---

**2026-02-14T21:47:05 | Dmitriy Kharkov**
UNKNOWN 408 Request Timeout
Server: 
Date: Sat, 14 Feb 2026 18:46:21 GMT
Cache-Control: no-cache,no-store,max-age=0
Prama: no-cache
X-Frame-Options: DENY
Expires: 0
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Content-Security-Policy: default-src 'self' 'unsafe-inline' 'unsafe-eval'
Content-Language: en
Content-Type: text/html
Connection: close

            <HTML>
            <HEAD><TITLE>408 Request Timeout</TITLE></HEAD>
            <BODY BGCOLOR="#cc9999" TEXT="#000000" LINK="#2020ff" VLINK="#4040cc">
            <H4>408 Request Timeout</H4>
No request appeared within a reasonable time period.

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

**2026-02-15T03:19:37 | Prefect**
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,1:ip_id=rnd:repeats=20
--payload=tls_client_hello --lua-desync=tcpseg:pos=0,midsld:ip_id=rnd:repeats=20
--payload=tls_client_hello --lua-desync=multidisorder:pos=1,midsld
--payload=tls_client_hello --lua-desync=multidisorder:pos=1,midsld,1220
--payload=tls_client_hello --lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1

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

**2026-02-16T22:53:08 | meow**
ech работает так, что там SNI cloudflare
и дальше cloudflare реальный sni узнает

---

**2026-02-16T22:53:39 | meow**
ECH забанен по sni cloudflare-ech.com
само расширение о наличии sni тспу не читает

---

**2026-02-16T23:00:06 | meow**
можно поднять свой ech сервер и не светить реальный sni

---

**2026-02-16T23:06:13 | meow**
грчц это и не нравится, не получается узнать реальный SNI

---

**2026-02-17T09:56:42 | Максим**
Вот так оставил для LG
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=fake:blob=0x0F0F0F0F:tcp_seq=-10000:tcp_ack=-66000:badsum:strategy=21
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=ggpht.com:strategy=21
--lua-desync=multisplit:pos=2,sld:seqovl=2108:seqovl_pattern=blob_tls_clienthello_www_google_com:strategy=21:final

---

**2026-02-17T09:57:27 | Lelik**
ваще я так понимаю что блокчек абсолютно не нужен сейчас? Или нужен, но старетгии скана надо дописывать обязательно (а как он вообще тогда находит доступные, если они не верные?), подставлять SNI параметр или прочее, сейчас с экстра параметрами можно сразу приписывать что-то типовое

---

**2026-02-17T10:05:20 | Rystick**
Пока всё стабильно на своём sni

---

**2026-02-17T16:02:00 | Борис**
если добавить эти опции (про сертификаты), то nginx вообще будет не нужен, и на стандартом порту 9090 будет работать https... Это, в общем-то, то, чего я добиваюсь - чтобы клеш работал по https

я пробовал 2 подхода:
1) прописать сертификаты через uci - не сработало, не поддерживается зероблоком
2) использовать прокси nginx, чтобы он проксировал с 9443 ssl на http ... 9090. Тоже не сработало, т.к. сам клеш внутри продолжает обращаться к http:9090, даже если его в брауезере открыть по новому адресу https://192.168.1.1:9443

Ну а https мне нужен, потому что я подключаюсь к роутеру с сим-карты иногда (туннель xray reality), и он очень плохо работает с http-сайтами (без сертификата), и вынужден использовать сертификат "донора" (фейкового sni), в итоге всё это очень ужасно работает, поэтому я выбрал просто поставить https на роутер, и всё стало идеально, и доступ к локальной сети полноценный появился через xray извне...

---

**2026-02-18T10:18:16 | Vasa**
если ты реалити делаешь то - 

пробовать перебирать порты - выше 50000 например или ниже 1000

если реалити - пробовать sni перебирать разные

ну или пробовать менять реалити(транспорт) на другой

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

**2026-02-19T10:42:37 | Vasa**
мозги и правильная настройка.

например xHTTP со своим доменом и за revers proxy из nginx \ caddy

впрочем и reality тоже пашет - вопрос с SNI \ IP хостера только

и вебсокет тоже пашет

---

**2026-02-19T22:09:22 | Vasa**
а транспорт какой? реалити чтоли? тогда - а какой SNI а менял ли ты его?

а пробовал ли другой порт?

---

**2026-02-19T22:10:05 | Artem**
реалити
sni менял, не помогло
другой порт не пробовал

---

**2026-02-19T22:12:14 | Vasa**
sni ты какие брал? попробуй просто убрать SNI

порты попробуй 600 и ниже

8443

50000 и выше

---

**2026-02-19T22:14:37 | Artem**
sni отсюда брал https://kmi.aeza.net/sAXAZ6CzAH

---

**2026-02-19T22:17:13 | Vasa**
попробовать вообще без SNI
а так же

cloud.mail.ru

ya.ru

disk.yandex.ru

www.icloud.com

---

**2026-02-19T22:18:28 | Vasa**
в целом SNI вообще можно брать любой от балды, какой заработает такой и оставить. сайтов море в тырнетах

потому что всё равно сервак уже или спалили, или спалят с такими настройками...)

---

**2026-02-19T22:51:36 | Artem**
меняю sni, один сайт загружается, потом перестает работать

---

**2026-02-19T22:58:12 | Леонид**
Ты ссылку на профиль заново добавляешь же?
Ссылка обновляется, её нужно заново копировать, после каждого изменения. И попробуй лучше sni - google.com

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

**2026-02-20T11:56:05 | Bullet for my valentine Poison**
смысл есть комбинировать, fake с блобом и multidisorder/multisplit. Это пока то что я на практике увидел. Но опять же, мне это нужно разобрать для полного понимания.
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost вот тут к примеру мне нужен разбор конкретный. "pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost" - что это, для чего, почему именно такой порядок и куда я могу это припихнуть. И с чем еще можно скомбинировать.😅 Так что я пойду дальше мучить копилота в режиме учебник.

---

**2026-02-21T14:26:50 | Lelik**
впиши в PKTWS доп. параметры в POST sni=www.google.com

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

**2026-02-21T20:17:33 | Bullet for my valentine Poison**
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=fake_default_tls:badsum:tls_mod=sni=rzd.ru:repeat=6

---

**2026-02-23T03:04:07 | Борис**
(если у кого-то возникнет вопрос, почему сразу reality сервер на 443 не поднять - так тоже можно сделать, просто у меня там мой сайт под другим доменом поднят. Таким образом nginx смотрит SNI, и если запрошен мой сайт, то он открывает другой локальный ресурс на другом порту. Если запрашивают m.vk.com, то посылает в зероблок (sing-box)

---

**2026-02-23T03:38:26 | Борис**
Самую мякотку - про то, как всегда бесплатно получать белый IP, и про бесплатный Путинский интернет (sni: vk.com, gosuslugi.ru) я рассказывать, конечно же, не буду...

---

**2026-02-24T12:47:26 | Vasa**
а какой транспорт \ протокол то?

если реалити - пробовать менять SNI \ порт...

---

**2026-02-24T12:50:32 | А**
ТСP, Reality. SNI - google

---

**2026-02-24T12:57:40 | Vasa**
та ничё они не вычисляют....

точнее не только лишь всё )

хотя с SNI типа гугла да, очень быстро)

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

**2026-02-25T14:17:09 | Alex**
0.6.4-r64 по непонятной причине отказывается работать с trojan, не важно в каком виде подсунуть конфиг, URL прокси, JSON, в логах следующие записи:
[proxy_parser] Skipping TROJAN_FL: reality requires public_key
[singbox_gen] Section Trojan: failed to create outbound for proxy[0]
[singbox_gen] Section Trojan: no valid proxies for URLTest (0/1)

url следующего вида:
trojan://09d***@95.xxx.xx.xx:9443?security=reality&sni=suomikauppa.fi&pbk=PVN***&sid=aabbccdd&type=tcp&fp=random#TROJAN_FL

распарсенный конфиг:
{
  "tag": "TROJAN_FL",
  "protocol": "trojan",
  "settings": {
    "address": "95.xxx.xx.xx",
    "port": 9443,
    "password": "09d***"
  },
  "streamSettings": {
    "network": "tcp",
    "security": "reality",
    "realitySettings": {
      "fingerprint": "random",
      "serverName": "suomikauppa.fi",
      "publicKey": "PVN***",
      "shortId": "aabbccdd"
    }
  }
}

---

**2026-02-25T22:27:33 | Routerich**
SNI - да

---

**2026-02-26T21:39:45 | Борис**
минуту, я тут уже всё перепробовал, надо откатиться к самому простому варианту. а то я тут уже и sniff понаписал и всё на свете. пытался сделать хак, чтобы vless inbound отправлялся по новой в route, когда sni становится известен (чтобы маршрутизация vless-клиента была как у самого роутера и его маршрутов, описанных в зероблоке, а то у меня всегда vless в direct уходит)

---

**2026-02-26T23:19:20 | Борис**
я кажется понял... это из-за того, что в вашем конфиге он слушает listen 0.0.0.0:10443 со всех устройств в сети?
потому что у меня слушает 127.0.0.1:10443, а попадает туда запрос так:

Запрос из Интернета (wan) -> nginx на роутере смотрит запрашиваемый SNI. Если SNI = m.vk.com, перенаправляю на 127.0.0.1:10443, иначе в 127.0.0.1:8080
(порты закрыты снаружи, чтобы их нельзя было прозвонить, поэтому использую listen 127.0.0.1)

может из-за этого такое быть, что маршрутизация zeroblock не работает, потому что запрос типа внутренний (из устройства роутера 127.0.0.1, а не с устройства извне) ?

---

**2026-02-27T13:12:42 | Борис**
Конфиг Nginx /etc/nginx/nginx.conf на всякий случай (блок stream, нужен такой установленный модуль)

stream {
  map_hash_bucket_size 64;

  upstream xray_backend {
    server 127.0.0.1:10443;
  }

  upstream nginx_site_backend {
    server 127.0.0.1:41228;
  }

  map $ssl_preread_server_name $backend_name {
    # Если домен соответствует маскировке Reality
    "m.vk.com" xray_backend;

    # Если домен — реальный сайт
    "сайт.на.роутере.fresa" nginx_site_backend;

    # По умолчанию отправляем в xray
    default xray_backend;
  }

  server {
    listen 443;
    proxy_pass $backend_name;
    #proxy_protocol on; # Включает отправку заголовка PROXY protocol
    ssl_preread on; # Обязательно: позволяет читать SNI без дешифровки
  }
}

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

**2026-02-27T16:24:18 | Lelik**
О точно,
tls_mod=rnd,dupsid,sni=google.com
Типо такого. Надо именно так, просто 
tls_mod=sni=google.com
Не работает?

---

**2026-02-27T16:25:58 | Lelik**
Так?
--lua-desync=fake:tls_mod=rnd,dupsid,sni=google.com

---

**2026-02-27T16:28:44 | Lelik**
А блобы надо строго те что пишется в SNI?

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

**2026-03-02T13:43:07 | Роман**
Ip хостера под взором ркн, скоро совсем откиснет или будет плохо работать. Не имеет значения (кроме статической погрешности) какой протокол использовать если рядом с вами на ip тело с SNI Yahoo.com и он тащит кучу трафика через свой vps, качая терабайтами. Блок на всю подсеть прилетает.

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

**2026-03-03T00:50:24 | Борис**
Каким образом? У провайдера стоит dpi и он должен знать, к какому сервису ты подключаешься. Если ты просто подключаешься к 5.12.133.213, то он не даст тебе это сделать, т.к. ты не обозначил свои намерения (не указал sni)

А в целом сейчас скорее по фейксни бан схлопочешь. Живой пример ютубанблок.

Тоже не понимаю, о чём речь. Если сервер настроен правильно, он будет устойчив к краулерам и методам активного зондирования. Технология reality устроена так, что если зайти на маскировочный ip с указанным sni (как попытается сделать провайдер), то сервер ответит реальным маскировочным сайтом с реальным сертификатом

Живой пример ютубанблок.

youTubeUnblock - это система для обхода dpi, и этот инструмент не имеет ничего общего с подменой sni. Системы обхода dpi (zapret, byeDpi, youTubeUnblock) работают таким образом, что изменяют структуру и/или атрибуты пакетов, делая их нечитаемыми для DPI провайдера. Провайдер, если работает не в системе белых списков, рассуждает так: "за интернет было уплачено, и я не могу доказать, что это запрещённый сайт, поэтому я разрешу такой запрос"

В системе белых списков провайдер рассуждает наоборот: "не удаётся подтвердить, что это разрешённый социальный ресурс, поэтому я заблокирую его"

---

**2026-03-03T01:05:58 | Kiss_My_Axe**
Они не ответ проверяют давно, а соответствие IP с SNI.
До НГ ещё обламывать начали. Просто до вас, видимо, пока не долетело.
У меня после гашения GGC и первых робких непущаний на ютуб, последний был ещё три месяца доступен напрямую, а потом щёлк и всё.
И в анблоке есть стратегии с фейксни.

Вот чего я действительно не понимаю, так это когда технически-подкованный человек, знающий, что ТСПУ отличаются по "способностям" даже у провайдера, к которому подключен сосед по лестничной площадке, пространно убеждает другого в том, что он не прав, потому что у меня вот так, а значит у всех вот так.

---

**2026-03-03T01:17:28 | Борис**
Речи о том, что при установлении соединения с неким IP, провайдер проверяет ответ сервера, не было. Провайдер действительно "активно" проверяет ip и sni для каждого соединения. Метод активного зондирования, который я описал выше, когда краулер от провайдера заходит на подозрительный ip и проверяет ответ — это пассивная процедура. Это означает, что провайдер очень даже не спеша, попивая кофе, "проходится" по подозрительным ip из своего блокнота и смотрит ответ. То что процедура называется "active probing" (активное зондирование), не означает, что провайдер спешит проверить ответ сразу, когда кто-то пытается обратиться к серверу :)

И от этой процедуры нельзя "отказаться давно", я скажу больше — её внедрили совсем недавно. Потому что процедура сама по себе очень эффективная. Можно в пассивном режиме обходить подозрительные ip и проверять, а открыт ли там 22 порт? А открыт ли 8080 порт? А почему это якобы сайт m.vk.com, а работает на 44443 порту? Все эти "расстёгнутые ширинки" у горе-админов выдают их с потрохами, и позволяют активно банить публичные и приватные vless reality сервера (они попадают в чёрный список навсегда, и простым работягам становится всё труднее и труднее "найти" рабочий белый ip (как они считают), хотя на самом деле неопытные простофили просто скомпрометировали кучи нормальных IP и ими больше нельзя пользоваться, поэтому складывается впечатление, что провайдер научился различать vless reality трафик)

---

**2026-03-03T01:28:31 | Kiss_My_Axe**
Любите вы многословить.

Весь ваш спич сводится к: 
1) тспу не сопоставляет SNI ни с чем, а просто по предварительно созданному IP-блэклисту ресетит соединение.
1.1) При этом наличие SNI, скорее, увеличивает вероятность бана.
2) если в блэклисте нет IP назначения, то _любой_ SNI признаётся валидным и система защиты интернета от граждан РФ допускает установку соединения.

---

**2026-03-03T01:38:28 | Борис**
тспу — это просто весёлые коробочки с весёлым программным обеспечением на борту. Как мы выяснили на практике, у нас есть:

1) "обычный интернет" - назовём его режимом черных списков, где можно открыть google.com, но нельзя открыть youtube.com
2) "белые списки" - открыть google.com невозможно, а youtube подавно

Так вот, для тех, кто невнимательно читал, повторю ещё раз — в режиме черных списков трафик пропускается, если не доказано, что запрашиваем запрещённый ресурс.
В режиме белых списков - запрещаем любой трафик, если не доказано, что идем на разрешенный ресурс.

Немного о "весёлых коробочках тспу". Как мы выяснили, это просто такой узел на пути от нашего дома до интернета. Эти коробочки читают весь трафик, который через них проходит. Обычно (в режиме чёрных списков) они работают только в режиме DPI (Deep Package Inspection) - проверяют сетевые пакеты, извлекают sni или пытаются "определить" тип трафика (например, wireguard), и применяют меры. Но коробочки 📦 становятся очень злыми и агрессивными после захода солнца - когда включают белые списки. Они не просто смотрят sni, они пытаются понять, действительно ли ip может принадлежать этому ресурсу, смотрят количество отправляемых данных, длину сессий, делают connection reset. Обойти их сложно, но возможно.

---

**2026-03-03T02:01:47 | Борис**
К сожалению (или к счастью) от блокировки сайтов по IP давно отказались, так как это оказалось неэффективным по целому ряду причин:
1) IP имеют ротацию и сайт легко может поменять IP, перейдя к другому провайдеру или просто сменив vps
2) В эпоху https и ipv4 считается нормальным, когда на одном IP расположено много сайтов. Поэтому, если просто заблокировать IP, то можно отправить в бан ни в чём не повинные сайты, которые просто были на том же сервере
3) CDN. Решения Content Delivery Network начали набирать популярность, а это означало, что огромное количество сайтов имело IP cdn-провайдера, который "встречал" запросы пользователей на первом этапе, прежде чем послать пользователя по месту назначения. А это означало, что реальный IP сайтов узнать стало невозможно (вместо этого можно только забанить IP CDN и положить миллион сайтов на нем)

Поэтому от примитивной блокировки по IP провайдеры отказались. Им пришлось раскошелиться на мощные аппаратные комплексы, которые перехватывали все запросы пользователей в реальном времени и пытались извлечь SNI из пакетов ClientHello (такой алгоритм требует приличных мощностей, т.к. трафик https зашифрован и приходится прилагать определенные усилия, чтобы в зашифрованной каше обнаружить SNI)

---

**2026-03-03T02:32:50 | Борис**
Как мы уже выяснили, youTubeUnblock является инструментом для обхода DPI, который изменяет структуру и атрибуты сетевых пакетов. То, что у юаб есть стратегия "с фейк сни" — не значит, что с помощью этой программы наше устройство пытается "попасть на Ютуб", указывая другой домен (как мы обсуждали с vless reality, когда клиент подключается к туннелю-серверу, указывая поддельный sni). В обычном World Wide Web у вас не получится "зайти на сайт", указав неправильное имя для него — сервер с сайтом не поймёт такой запрос. У сервера есть только сайт youtube.com, а вы ему скажите "дай мне yandex.ru", он тебе ответит "ты куку? Тут такой не проживает."

Так как же это работало в youTubeUnblock и прочих? Очень просто. У сетевых пакетов есть такой атрибут, как ttl (time to live). Этот атрибут означает, сколько "прыжков" между сетевыми узлами пакет способен пережить. Так вот, YUB указывал в пакете sni = yandex.ru и при этом ttl = 3 (я не знаю сколько, но очень маленькое число). Таким образом ТСПУ был узлом #2 и он пускал такой трафик дальше, ведь яндекс для него — это круто и молодёжно. Но реальность в том, что пакет с таким sni умирал сразу после тспу, а до ютуба доходили уже "реальные" намерения человека — "дай мне youtube.com"

Эту лазейку с fake sni быстро прикрыли, так как провайдеру достаточно было выпустить небольшой патч, в котором проверялся не только sni, но и ttl пакета (чтобы сразу видеть, что ему пытаются скормить "обманку")

---

**2026-03-03T16:35:27 | Denis**
Вот этот ключ не работает в виде ссылки, в JSON все ок.
В passwall2 и во всех Xray клиентах ссылка нормально используется.

vless://UUID-REPLACED@example.com:443?security=reality&type=xhttp&headerType=&path=%2Fcbkfox&host=&mode=stream-one&extra=%7B%22xmux%22%3A%7B%22cMaxReuseTimes%22%3A%221000-3000%22%2C%22maxConcurrency%22%3A%223-5%22%2C%22maxConnections%22%3A0%2C%22hKeepAlivePeriod%22%3A0%2C%22hMaxRequestTimes%22%3A%22400-700%22%2C%22hMaxReusableSecs%22%3A%221200-1800%22%7D%2C%22headers%22%3A%7B%7D%2C%22noGRPCHeader%22%3Afalse%2C%22xPaddingBytes%22%3A%22400-800%22%2C%22scMaxEachPostBytes%22%3A1500000%2C%22scMinPostsIntervalMs%22%3A20%2C%22scStreamUpServerSecs%22%3A%2260-240%22%7D&sni=example.com&fp=chrome&pbk=PUBLIC_KEY_REPLACED&sid=SHORT_ID_REPLACED&spx=%2F#vlessXHTTPrealityEXTRA-autoXRAY

---

**2026-03-03T19:52:29 | ㅤ**
если в кратце то
Vless + Reality + SNI (нужного домена)

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

**2026-03-04T00:21:02 | Bullet for my valentine Poison**
А можешь хоть бутерброд сделать (фэйк-мульти-фэйк), не уверен что он будет работать нормально. Но все же.  это я молчу про мелкие детали, там всякие sni,pos,nodrop,tls и прочее

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

**2026-03-04T12:58:41 | Bullet for my valentine Poison**
зачем, там же везде одна строчка одинаковая. К ней еще одну с блобом лепи и перебирай, на какой вариации блоба залетит.Ну там еще всякие sni. ПРимеры можно у стандартных профилей подсмотреть.

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

**2026-03-04T15:30:22 | Bullet for my valentine Poison**
sni можешь любой писать. мэйла, маха  и т.д.

---

**2026-03-05T00:52:52 | Vasa**
тут очень многое нужно объяснять, чтоб было понимание. про сети. как они устроены и работают итд.

если в общем и целом - 

на примере 3x-ui панели

не юзай стандартный SNI
не юзай SNI крупняков типа google \ амазон итд...
можешь попробовать тупо пустой SNI
можешь попробовать порты не 443, а например 8443, выше 50000, ниже 600
да, хостер может быть в "сером" списке и проще тогда сменить хостера
необязательно использовать реалити, можно юзать xHTTP \ вебсокет с беслпаными доменами 3го уровня(но лучше со своим)

итд итп...

у меня вообще опенвпн работает втупую и всё )

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

**2026-03-06T18:25:00 | Azizkhan**
Тут ситуация странноватая:
Клиент - Роутер - Интернет
Влесс на роутере настроен на example.com сервер со sni yahoo.com
Клиент запускает влесс с этим же ключом грубо говоря и его соединения создают петли

Соединения переваливают за 3700 и ООМ приходит за сингбоксом

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

**2026-03-08T15:46:59 | Dmitriy M 🎃**
hy2://ae3b42782d2740ad81cf481409251c9c@144.31.128.194:443/?obfs=salamander&obfs-password=*********g8Q8nTLYH&sni=h2norw.impio.ru#impVPN%20%7C%20%D0%9D%D0%BE%D1%80%D0%B2%D0%B5%D0%B3%D0%B8%D1%8F%20%F0%9F%87%B3%F0%9F%87%B4

---

**2026-03-11T16:15:30 | Artur A.**
Забудьте про изоляцию в Wi-Fi.

Годами мы лепили гостевые SSID, ставили галочку AP Isolation и верили, что юзеры внутри одной подсети изолированы друг от друга. Оказалось - показалось 😬

На симпозиуме NDSS 2026 показали атаку AirSnitch, которая умножает на ноль всю изоляцию Wi-Fi клиентов. Причем делает это не брутфорсом, а фундаментальным обманом логики работы коммутаторов на первом и втором уровнях модели OSI. Уязвимы практически все протестированные железки... Cisco, Ubiquiti, Netgear, D-Link, а также кастомные прошивки OpenWrt и DD-WRT.

Суть атаки... Атакующий подключается к точке доступа, подделывая MAC-адрес жертвы. AP обновляет таблицу коммутации, связывая виртуальный порт атакующего с MAC-адресом жертвы. В результате весь входящий трафик начинает литься хакеру. Но чтобы сделать атаку двусторонней и не сбросить жертву окончательно, хакер использует хитрый трюк... он отправляет ICMP-пинг с рандомного MAC-адреса, завернутый в общий групповой ключ сети. Это заставляет точку доступа переключить маршрутизацию обратно на жертву. Постоянно жонглируя этими состояниями, атакующий незаметно встает посередине канала.

Самая дичь заключается в том, что атака работает даже за пределами одного BSSID. Злоумышленник может сидеть на гостевом SSID, а ломать клиента из корпоративного SSID, если они обслуживаются одной точкой доступа. В энтерпрайз-сетях ситуация еще хуже, т.к. AirSnitch позволяет перехватывать трафик между пользователями, подключенными к разным физическим точкам доступа, если они делят общую проводную распределительную сеть. Разделение по VLAN помогает далеко не всегда, так как многие вендоры криво реализуют изоляцию между L2 и L3. Исследователи даже продемонстрировали, как с помощью этого метода перехватить RADIUS-пакеты и поднять фейкового двойника корпоративной WPA3-Enterprise сети.

Что со всем этим делать - пока вопрос открытый. Проблема кроется в самой архитектуре обработки фреймов, и некоторые производители железа уже говорят, что починить это программно невозможно и нужны фиксы в Wi-Fi чипах. Патчи будут, но до тех пор любая открытая или слабо защищенная сеть (даже с изоляцией) - это ваши риски уже сейчас.

---

**2026-03-11T16:31:31 | Routerich**
Есть блокировки по sni, это обходится, а есть блокировки по ip, так вот по второму надо чтобы ip vpn был из белых списков

---

**2026-03-11T16:33:29 | Routerich**
Проверять доступность различных vpn сервисов.
Vless с белым sni

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

**2026-03-16T12:54:40 | Yrii**
Mon Mar 16 12:52:34 2026 daemon.info youtubeUnblock[10767]: youtubeUnblock 1.3.0-1
Mon Mar 16 12:52:34 2026 daemon.info youtubeUnblock[10767]: Bypasses deep packet inspection systems that rely on SNI
Mon Mar 16 12:52:34 2026 daemon.info youtubeUnblock[10767]:
Mon Mar 16 12:52:34 2026 daemon.info youtubeUnblock[10767]: Running with flags: --queue-num=537 --threads=1 --packet-mark=32768 --silent --tls=enabled --frag=tcp --frag-sni-reverse=1 --frag-sni-faked=0 --frag-middle-sni=1 --frag-sni-pos=1 --fk-winsize=0 --fake-sni=1 --fake-sni-seq-len=1 --fake-sni-type=default --seg2delay=0 --faking-strategy=pastseq,  --sni-domains=<trie of 106 vertexes> --sni-detection=parse --synfake=0 --udp-filter-quic=disabled --fbegin --tls=disabled --sni-domains=<trie of 157 vertexes> --sni-detection=parse --synfake=0 --udp-filter-quic=disabled --udp-stun-filter --fend --fbegin --tls=enabled --frag=tcp --frag-sni-reverse=1 --frag-sni-faked=0 --frag-middle-sni=1 --frag-sni-pos=1 --fk-winsize=0 --fake-sni=1 --fake-sni-seq-len=1 --fake-sni-type=default --seg2delay=0 --faking-strategy=pastseq,  --sni-domains=<trie of 29 vertexes> --sni-detection=parse --synfake=0 --udp-filter-quic=disabled --fend
Mon Mar 16 12:52:34 2026 daemon.info youtubeUnblock[10767]: Queue 537 started

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

**2026-03-17T09:14:56 | lxstwxrden**
Веб-версию ещё можно заставить работать быстро на другом IP телеги, и вписать домены в zapret тоже дабы обойти замедление по SNI

---

**2026-03-17T17:41:19 | Роман**
Не использовать SNI, использовать self steal. https://github.com/Akiyamov/xray-vps-setup
Как пример. 
Порт 51547 ну совсем не палевный, ага.
Или на канале давайте про it посмотрите как маскировать прокси под свой сайт. Это частично работает, потому как вас персонально искать никто не будет, а вот ваши соседи с SNI yandex.ru, max.ru и прочее (конечно яндекс хостится на левом хостинге лол 😁) палятся, и вся подсеть в блок улетает.
А про БС - отдельная тема на 4PDA - суверенный интернет.

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

**2026-03-18T19:05:26 | Colin MacLaughlin**
Такое недельки 2-3. Этот роутер подерживает амнезию или мне меня SNI с портом на Vless?

---

**2026-03-18T19:06:23 | Владимир Волков**
Амнезию поддерживает, даже новую. Влессы нужно правильно настраивать под себя - sni могут не работать, домен свой использовать, порты менять, транспорт менять, вариаций море

---

**2026-03-18T19:34:05 | Colin MacLaughlin**
У меня именно он, просто думаю SNI стоит самый банальный (гугл).

---

**2026-03-18T22:06:21 | Роман**
Какой жирный тролль. А начиналось всё с историй о том, как БС обходить SNI подменяя. 
Вы уж определитесь, вы за обходы блокировок или в MAX свой идите со своими агитационными материалами. 
Хватит пытаться вызвать негатив своими сообщениями.

---

**2026-03-19T14:11:03 | Chezok**
мне помогла магическая стратегия, йутуб залетал на всём
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4

---

**2026-03-19T16:29:39 | Routerich**
В теории может пустить, если 1 - у вас белый IP и в подсети белых списков, и нет блокировки по sni дополнительно. 2 - шанс такого - 0,01. Так что ответ - нет

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

**2026-03-20T23:01:51 | Gomer Simpson**
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1

---

**2026-03-21T14:03:59 | А К**
Товарищи, а как сделать подмену sni? теперь и на домашнем интернете будет белый список((

---

**2026-03-21T14:13:52 | Роман**
Тогда подмена SNI вам не поможет.

---

**2026-03-21T14:20:15 | Роман**
К какому большинству? Вы понимаете как работают БС? Запрещено всё что не в белом списке. Подмена SNI не поможет, если нет сервера за "белым" ip - ничего не поможет, даже vpn не поможет.

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

**2026-03-21T23:30:01 | Борис**
Брат! Тебе нужно открыть 4pda, тему "суверенный интернет". Там люди выложили 2000+ бесплатных vless-серверов (подписок на них). Ты должен просканировать все эти 2000 со своего lte, затем посмотреть, какие sni пропускает твой провайдер (в идеале - на 2ip.ru глянуть, какой хостинг они используют) и скопировать себе их рабочие конфиги. Если даже так все равно не сможешь подключиться, значит меняй IP своего VDS (ты очень богат, я вижу), либо меняй провайдера VDS, потому что никогда и ни за что ты к этому серверу с телефона не подключишься, ни с каким транспортом. Он не подходит под критерий белого списка Tele2

---

**2026-03-21T23:47:10 | Routerich**
Будет или нет зависит от типа блокировки по sni или по ip, в первом случае да, во втором надо искать сервер из белых списков подсетей

---

**2026-03-22T00:25:27 | Alexey Zh**
я в целом там ничего не трогал кроме rr_youtube 
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4

---

**2026-03-22T10:57:37 | Alex**
время правильное,

root@RouteRich:~# nslookup downloads.openwrt.org
Server:         127.0.0.1
Address:        127.0.0.1:53

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

root@RouteRich:~# 

root@RouteRich:~# nslookup github.com
Server:         127.0.0.1
Address:        127.0.0.1:53

Non-authoritative answer:

Non-authoritative answer:
Name:   github.com
Address: 140.82.121.3

 IPv6 - отключен

---

**2026-03-22T20:27:55 | ARTEM**
Хочу сделать новую стратегию через zapret2 finder , так как что в шапке стратегия что в rr-youtube, когда захожу на ютуб долго прогружается превьюшки а через awg в zeroblock пускать не хочу потому что 4к лагать начинает
--
Вот щяс вставил домены ютуба и убрал sni prob и все в blocked упали
Как правильно запустить finder чтобы найти стратегию только для ютуба ?

---

**2026-03-23T20:26:28 | Borys Celich**
у меня вон голый вайргуард живет вполне на одном из серверов уже не знаю года 3, а некоторые влессы за неделю отлетают и нужно sni менять на другой

---

**2026-03-23T20:40:28 | 88**
не помогает, мегафон кроме SNI еще и IP проверяет

---

**2026-03-23T20:42:36 | Борис**
Ну и что? Это не отменяет того факта, что ты можешь подобрать vless или trojan сервер, у которого эти параметры соответствуют. Просканируй бесплатные сервера с 4pda, тема "суверенный интернет". Таким образом увидишь, какие sni и ip любит твой провайдер

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

**2026-03-28T23:50:56 | Станислав Земляков**
Домен не резолвится на уровне DNS. Это не SNI/DPI блокировка — zapret2/nfqws2 здесь бессилен. Решение - смена DNS-резолвера (DoH/DoT), а не anti-DPI.

---

**2026-03-29T12:40:13 | Routerich**
curl -v https://googlevideo.com
* Host googlevideo.com:443 was resolved.
* IPv6: 2a00:1450:4010:c03::69, 2a00:1450:4010:c03::93, 2a00:1450:4010:c03::67, 2a00:1450:4010:c03::6a
* IPv4: 209.85.233.105, 209.85.233.99, 209.85.233.106, 209.85.233.104, 209.85.233.103, 209.85.233.147
*   Trying [2a00:1450:4010:c03::69]:443...
*   Trying 209.85.233.105:443...
* schannel: disabled automatic use of client certificate
* ALPN: curl offers http/1.1
* schannel: SNI or certificate check failed: SEC_E_WRONG_PRINCIPAL (0x80090322) - Главное конечное имя неверно.
* closing connection #0
curl: (60) schannel: SNI or certificate check failed: SEC_E_WRONG_PRINCIPAL (0x80090322) - Главное конечное имя неверно.
More details here: https://curl.se/docs/sslcerts.html

curl failed to verify the legitimacy of the server and therefore could not
establish a secure connection to it. To learn more about this situation and
how to fix it, please visit the webpage mentioned above.

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

**2026-03-30T21:32:20 | А К**
Не всегда кстати, многие до сих пор по sni бс обходят, там где вышки это позволяют и трафик может быть иностранным. Но чаще всего конечно внутренний

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

**2026-03-31T07:15:04 | AleXXXey**
vless://UUID@SERVER_IP:443?encryption=none&security=reality&flow=xtls-rprx-vision&sni=www.yandex.com&fp=chrome&pbk=PUBLIC_KEY&sid=SHORT_ID#AmneziaVPN

---

**2026-03-31T07:19:56 | Yury Kuzmenko**
vless://UUID@SERVER_IP:443?encryption=none&flow=xtls-rprx-vision&security=reality&fp=chrome&sni=www.googletagmanager.com&pbk=PUBLIC_KEY=SHORT_IDtype=tcp#xray-vless
Вот моя ссылка, похоже у вас проблема в том что почему то нет транспорта в ссылку

---

**2026-03-31T07:34:26 | Routerich**
vless://UUID@SERVER_IP:443?encryption=none&flow=xtls-rprx-vision&security=reality&fp=chrome&sni=www.googletagmanager.com&pbk=PUBLIC_KEY=SHORT_ID&type=tcp#xray-vless

Вы пропустили символ & перед транспортом.

---

**2026-04-01T04:12:22 | Max Himitsu**
надеюсь Амнезийцы уже думают над этим) Но пробные ключики я уже видел +\- из чего они, в основном SNI белые списки,  кажется не сложно) Только не хватает доп функции от ТСПУ, чтобы конфигурацию расширили до 3-4 белых списков,.... Смотреть ютуб в 2К как-то подозрительно 3 часа под одним SNI vk.com или ads.x5 (валим всё на Сеть Магазинов)

---

**2026-04-01T04:12:49 | Max Himitsu**
смена SNI 1 раз в 20 минут автоматом, хороший ход для чёрных ящиков

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

**2026-04-01T14:38:55 | Routerich**
Ну вот и выяснили, что скорее всего оператор блокнул ip, или sni под который прятались

---

**2026-04-01T15:25:36 | Антон Баев**
Разобрался
Оказывается по sni чет перестало им нравится
Поменял и всё завелось на 443

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

**2026-04-01T17:17:59 | Антон Баев**
да тоже уже разобрался
SNI поменял и полетело

---

**2026-04-01T17:24:02 | Роман**
Какой sni использовали?

---

**2026-04-01T17:26:10 | Vasa**
убери sni вообще. и попробуй

---

**2026-04-01T17:26:29 | Роман**
Вообще sni не нужно использовать.

---

**2026-04-01T20:40:23 | Дмитрий Григорьев**
А ну и SNI, шо по поводу RU доменов, или классика google/github и тд?

---

**2026-04-02T10:44:52 | Bullet for my valentine Poison**
Низя. Блобы делаются из адресов, которые white, например список white sni берем и тупо методом перебора проверяем через чекалку хостов. И то это не всегда работает. 😅

---

**2026-04-02T11:33:42 | Andrey**
а че там Sni не sni? надо чет?

---

**2026-04-02T11:34:06 | Yury Kuzmenko**
Хз там у всех по разному у кого с sni наоборот хуже работает

---

**2026-04-02T11:35:28 | Vasa**
а, из староверов...

попробуй убрать вообще sni

---

**2026-04-02T11:37:54 | Andrey**
ну без sni заработало

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

**2026-04-02T14:07:33 | Andrey**
@BWasilii я переделал это все на подписки в панели чтоб не бегать по 500 раз на дню. хоть без sni это пока работает

---

**2026-04-03T11:46:06 | Dark Ghost**
99% палятся из за sni, которые прописывали массово гуглами, да яндексами, не соображая, что соответствие ip для них давно в табличках прописано...
Да и характер трафа на них сильно иной...

---

**2026-04-03T12:29:51 | Vasa**
у vless - убрать SNI вообще

xHTTP со своим доменом за nginx - должно неплохо работать

---

**2026-04-03T17:00:06 | Yury Kuzmenko**
Сначала без sni проверю, может пчелайн на sni ругается

---

**2026-04-04T17:37:43 | Vasa**
зависит от хостера. как он следит за траффиком

вообще впринципе необязаетльно делать reality... и вообще SNI для него тоже)

---

**2026-04-04T21:31:04 | Роман**
За восемь месяцев 1 хостера (у меня) накрыло, всё остальное работает. Возможно у вас sni гугл или макс - вот и палят.

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

**2026-04-06T14:36:02 | Routerich**
v0.9.4.7 (31 марта)
nfqws2 не падает при ошибке tls_mod dupsid/rndsni/padencap
поиск стратегий — опция Combo reverse (split first, then fake)

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

**2026-04-06T18:43:20 | Mike**
https://overclockers.ru/blog/molexandr/show/252589/Ceny-na-operativnuju-pamyat-rezko-snizilis-iz-za-neopredelennosti-na-rynke

---

**2026-04-06T21:37:15 | HiLLL**
Тут спорное утвержение. Я когда установил запрет у меня не завелось с той портянкой которая была по дефолту, а с милиписюшной стратой полетело. https://t.me/routerich/4/599472
--lua-desync=multisplit:pos=1,sniext+1:seqovl=12

---

**2026-04-06T22:35:44 | splashsnake splashsnake**
Тогда вопрос если white list то как его обойти. Dpi? Sni? На Яндекс прописывать

---

**2026-04-07T16:38:11 | Gremlin**
мне SNi амазон нравятся. Они изначально не работают в России 🤣

---

**2026-04-07T23:16:42 | Dmitrii Burenin**
Имеете в виду списки по sni?

---

**2026-04-08T12:09:21 | S W**
Ребят, подскажите пожалуйста, вне дома на пк использовал nekoray от MatsuriDayo на пк, но, не знаю точно с чем связано, перестал работать 
(если кратко, то сначал думал что провайдер начал блокировать из-за подмены sni мой vps с vless+reality. Но с телефона (v2rayNG) и дома (zeroblock, настроенная секция) все работает штатно, вышел на то что прооблемы с клиентом nekoray (nekobox))

Решил заменить на другой, вижу есть какой то форк от qr243vbi (так и называется nekobox), версия  5.10.34 (будто наследовал от MatsuriDayo), но выглядит сомнительно. Так же поискал по чату и люди говорят о Throne как он официальном(?) форке-продолжении nekoray, насколько этому можно верить и вообще что по итогу лучше использовать на пк?

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

**2026-04-08T19:40:31 | Vasa**
SNI пробовал поменять?

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

**2026-04-09T08:32:30 | Routerich**
если будет блокировка по sni и при этом у вас будет vless с белым sni всё будет ок, а если будет по IP то уже никуда подключиться не сможете, соответственно sing-box не стартанет

---

**2026-04-09T08:37:59 | D Ch**
Белый sni max.ru (например) это автобан со стороны провайдера. А подобрать домен в одной подсети с квн помоему противоречит сути бс

---

**2026-04-09T12:19:56 | Aleksandr U**
Здравствуйте, вопрос а если забугорный сервер влесс + реалити (со sni из бс), на него быстро блоки поставят?

---

**2026-04-09T12:23:42 | Aleksandr U**
Пока только в мыслях )) жалко 600 р за сервак отдавать, тем более если его закрою на следующий день 😅. Проще тогда sni забугорный думаю и пережидать БС

---

**2026-04-09T20:18:06 | Евгений**
домен SNI не могу понять что написано

---

**2026-04-10T13:17:21 | Nook Scheel**
Это по сути sni proxy

---

**2026-04-10T14:33:44 | Vasa**
да вполне себе работает... возможно надо просто использовать не реалити или другой SNI

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

**2026-04-10T15:50:41 | Vasa**
ничего. либо пробуй пустой SNI либо вообще про это забыть можно

ну или сидеть SNI подбирать

---

**2026-04-11T10:05:14 | Руслан**
Через XHttps очень низкая скорость. Норм протокол который сейчас установил для openwrt для айфонов и андроид .sni через свой домен

---

**2026-04-11T10:13:09 | Yury Kuzmenko**
Блочат то что люди на публичных sni сидят

---

**2026-04-11T15:47:49 | M D**
vless://79c58bf9-21c9-4a4c-8527-912e3360a68e@lvn.externet.org:443?security=reality&sni=www.microsoft.com&fp=chrome&pbk=gPYyAl_vwMzKONbwy88LfVc0N_8LPcqNxX1pADtlUhI&sid=4625e48b6e8839de&type=tcp&flow=xtls-rprx-vision&encryption=none#externet.org вот эта работает?

---

**2026-04-11T16:04:14 | Андрей Орлов**
Проверьте ссылку пожалуйста. vless://5afe1163-968a-4db2-bb32-97a9521a150d@45.140.205.106:443?type=tcp&encryption=none&security=reality&pbk=CWh7DZWZKCqBI79NFaZgc9nUPbJ7zNDVTSjSxEsRuQs&fp=chrome&sni=ethz.ch%3A443&sid=df80aac1730511&spx=%2F&flow=xtls-rprx-vision#Vless-reality-Client_veqonik

---

**2026-04-11T17:26:22 | Роман**
Нет, своих не сдаём. Придёт условный Васян, накатит 3xui, поставит SNI - MAX.RU - и вся сеть в блок отлетит. Без негатива к Василиям, они хорошие и умные люди.

---

**2026-04-11T21:56:12 | Routerich**
Сейчас по IP бс, поэтому только на IP в России, раньше когда по sni были бс, можно было обойти подменой

---

**2026-04-12T01:38:33 | support**
Подскажите почему это не работает адекватно, ютюб работает, но все остально что на скринах пугает. 
NFQWS2_OPT="--filter-udp=443 --filter-l7=quic --hostlist-domains=youtube.com,googlevideo.com,youtu.be,googleapis.com,ytimg.com,ggpht.com,gstatic.com,google.com --out-range=-s34228 --payload=quic_initial --lua-desync=fake:blob=quic_initial:ip_ttl=6 --new --filter-udp=443 --filter-l7=quic --hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt --out-range=-s34228 --payload=quic_initial --lua-desync=fake:blob=quic_initial:repeats=6 --new --filter-tcp=80 --filter-l7=http --hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt --out-range=-s34228 --payload=http_req --lua-desync=fake:blob=http:tcp_md5 --lua-desync=multisplit:pos=method+2 --new --filter-tcp=443 --filter-l7=tls --hostlist-domains=youtube.com,googlevideo.com,youtu.be,googleapis.com,ytimg.com,ggpht.com,gstatic.com,google.com --out-range=-s34228 --in-range=-s5556 --lua-desync=circular:fails=1:maxtime=5 --in-range=x --payload=tls_client_hello --lua-desync=multidisorder:pos=1,midsld:strategy=1 --lua-desync=multidisorder:pos=1:seqovl=681:seqovl_pattern=tls_clienthello:strategy=2 --lua-desync=multidisorder:pos=10,midsld:seqovl=336:seqovl_pattern=tls_clienthello:strategy=3 --lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=4 --lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=www.google.com:strategy=5 --lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=google.com:strategy=6 --lua-desync=fakedsplit:pos=midsld:strategy=7 --lua-desync=multidisorder:pos=1,midsld,sniext:strategy=8 --lua-desync=multidisorder:pos=1,sniext+1,midsld-2,midsld,midsld+2:strategy=9 --lua-desync=fake:blob=tls_clienthello:ip_ttl=6:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=rzd.ru:repeats=4:strategy=9 --lua-desync=multidisorder:pos=2,5,105,sniext+5,midsld-1:strategy=10 --lua-desync=multisplit:pos=10:seqovl=1:strategy=11 --new --filter-tcp=443 --filter-l7=tls --hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt --out-range=-s34228 --payload=tls_client_hello --lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=2gis.com --lua-desync=multisplit:pos=2 --new --filter-l7=mtproto --payload=mtproto_initial --lua-desync=fake:blob=0x00000000 --new --filter-tcp=443 --filter-l7=tls --ipset=/opt/zapret2/ipset/zapret-ips-user.txt --out-range=-s34228 --payload=tls_client_hello --lua-desync=multidisorder:pos=1,sniext+1,midsld-2,midsld,midsld+2 --lua-desync=fake:blob=tls_clienthello:ip_ttl=6:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=rzd.ru:repeats=4"

---

**2026-04-12T12:43:56 | Gremlin**
эмм, а SNI не из БС. Поставь хоть ya.ru для теста

---

**2026-04-12T13:12:16 | Vasa**
над делать сноску что SNI необходимо нормально подбирать. или вообще пустой юзать

---

**2026-04-12T13:17:22 | Vasa**
нет не пойдет. адреса подобных сервисов известны обычно, они опубличены.

и смешно видеть на каком то немецком мелком хостинге, при сканировании, домены типа мс \ яху \ нвидии итд ))

я бы рекомендовал реалити тупо юзать без SNI вообще наверно. хоть какая то "защита"

либо использовать другие транспорты

но в целом пока работает - пофигу. потом просто сервак \ ip сменишь если что

---

**2026-04-12T13:47:37 | Роман**
Не использовать SNI вообще, маскировка под свой сайт на 443 порту лучше.

---

**2026-04-12T15:17:54 | ㅤㅤ**
Я уже отвечал кому-то здесь на этот счёт, но всё, кажется, потёрли.

Постараюсь написать настолько коротко, насколько это вообще возможно. Но доступно.

Цензор, судя по всему, научился сопоставлять SNI и IP, на которые они должны резолвиться (по крайней мере для крупных ресурсов).

Народ же продолжает по глупости своей настолько бездумно выбирать целевые сайты для маскировки, что это уже становится проблемой. Причём массовой.

RPRX, разработчик Reality, уже устал всех предупреждать и просто начал делать коммиты типа 157e65b: "REALITY config: Print Warning when user is choosing apple/icloud as the target or listening on non-443 ports", - который прямо сейчас уже стал частью ядра Xray актуальной версии.

Да, VLESS Reality умеет маскироваться под сёрфинг чужих сайтов, однако есть пара НО:
- Способность маскироваться под чужой сайт изначально была создана преимущественно ради возможности пробивки белых списков SNI (в некоторых комбинациях выбора сервера с его настройкой - и белых списков SNI + IP). В остальных же случаях идеальным вариантом было и остаётся только использование конфигурации steal_oneself.
- Если всё же и маскироваться под чужой SNI (больше вынужденно), то только под реальный сайт (с TLS 1.3 и HTTP2) на IP, расположенном в одной подсети с вашим сервером, причём желательно максимально близко к IP вашего сервера. И не под какой-нибудь условный yahoo.com, под который маскируется ваш сосед по подсети. Вы должны осознавать, что никакие крупные ресурсы никогда не хостятся на бомж-хостингах.

Но, к сожалению, возможность VLESS Reality маскироваться под чужой сайт превратили в полную анархию. И в откровенную проблему, сильно злоупотребляя ею.

Потому что вы сегодня имеете сервер с IP от хостинга "Вася Пупкин". И гоните тонну трафика якобы до/со SNI yahoo.com.

Думаете, это вот вообще не палевно, да?

 "Контора солнышек" такая: "А куда это в действительности резолвится домен yahoo.com?" - и проверяет, а потом такая: "Что-то результат проверки не совпал с IP этого сервера у хостера "Вася Пупкин!" - миллисекундное размышление, и гневный возглас: "Ах ты ж подлый VPN'щик!" - и подсеть вашего сервера подвергается полному сканирование на предмет "гениев", подобных вам. Их много? Что ж, вся подсеть вашего сервера у хостера "Вася Пупкин" начинает систематически "морщиться".

И это уже происходит. Но люди упорно продолжают сами себе "ср*ть в штаны" (простите меня за мой "французский"), надеясь на чудо.
Ещё и всякими дырявыми MTProxy недавно спалили свои серваки лишний раз.

---

**2026-04-12T15:28:00 | Vasa**
почему я и гвоорю - просто уберите SNI и всё. пустой оставьте, совсем. вот целиком и полностью

---

**2026-04-12T16:03:36 | Yury Kuzmenko**
Либо реалити скан делать и искать sni в одной подсети с тобой

---

**2026-04-12T21:28:49 | Дмитрий**
--out-range=-s34228
--payload=tls_client_hello
--lua-desync=multidisorder:pos=1,sniext+1,host+1,midsld-2,midsld,midsld+2,endhost-1
--lua-desync=fake:blob=blob_tls_clienthello_www_google_com:optional:tcp_seq=-10000:tcp_ack=-66000:badsum:tls_mod=rnd,dupsid,sni=rzd.ru:repeat=4

---

**2026-04-13T12:03:43 | Kiss_My_Axe**
Только шпроту находят по расхождению SNI-IP, т. к. мамкины шпротники сни ставят гугалком, ониж мудрые, шо там!

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

**2026-04-15T08:39:35 | Алексей Микоянов**
Господа, а вот ещё вопрос. Есть валидная ссылка на vless - её, как минимум, кушает vray2tun. Роутер не цепляет, говорит Invalid vless url

vless://19ccc3ee-c1e3-4635-b9b0-7217f8a9e26f@11.100.111.111:443?encryption=none&flow=xtls-rprx-vision&security=reality&sni=eh1.vk.com&pbk=Ib1FPzB1EhfUioXwCS9jAy7oUyC0GNN4Oew55GkVO0Q&sid=6a54828c472f593e&fp=chrome&spx=/#test
(IP/ключ немного изменён, конечно же)
Что-то можно сделать, кроме как использовать другие ссылки?

---

**2026-04-15T08:50:23 | Yury Kuzmenko**
vless://fa1883f5-f8d9-4a41-9c60-054bcdfee12a@222.222.22.222:51817?type=xhttp&encryption=none&path=%2F&host=&mode=auto&security=reality&pbk=GEIRWYHeMdl3_bo031A-Jvk7BBGgcJY0XNHjdVs1ZGo&fp=chrome&sni=www.amd.com&sid=b3673af577fa&spx=%2F#VASA-ls8blyds

---

**2026-04-15T08:54:43 | Yury Kuzmenko**
Так любые конфиги поддерживаются, с шифрованием и без. Тут у меня был для теста реалити без sni

---

**2026-04-15T09:18:38 | Алексей Микоянов**
Из соседней ветки рекомендовали сюда вопрос перенести. 

Есть работоспособный конфиг (v2raytun кушает и работает) vless. Но его нельзя вставить в интерфейсе ZB - видимо, какая-то regexp некорректно отрабатывает и называет ссылку невалидной. 
Можно как-то поправить? 

Ссылка (с модифицированной чувствительной информацией)
vless://19aaa3ee-c1a3-4635-b9b0-7217f8a9e26f@11.111.111.111:111?encryption=none&flow=xtls-rprx-vision&security=reality&sni=eh1.vk.com&pbk=Ib1FPzB1EhfUioXwCS9jAy7oUyC0GNN4Oew55GkVO0Q&sid=6a54828c472f593e&fp=chrome&spx=/#test

---

**2026-04-15T15:51:17 | Routerich**
запомнить какой sni он выбрал. вписать руками и пропустить sni

---

**2026-04-15T16:05:35 | 01000000**
Спасибо за ответ. А можно по пальцам. Как пример. Или в инструкции про этот sni почитать. Куда его вписывать, в какой вкладке, Как стратегию на cdn направить? Делаю пошагово: компетенции считай нет.

---

**2026-04-15T19:07:39 | 01000000**
Из этого всего это копировать вокно sni?

---

**2026-04-15T19:21:13 | 01000000**
Sni

---

**2026-04-15T19:33:20 | 01000000**
sni=support.biz.mail.ru:repeats=1 это? Или как включить отображение только доменов без обходов?

---

**2026-04-15T20:59:23 | Дмитрий Григорьев**
К сожалению очень много ламеров ставят в свой vless+ reality sni популярных сайтов по типу google.com или max.ru
Такие vps'ки вскрывают на раз два, но в след за ней летит вся подсеть ip адресов
Могу только подсказать искать практически ноунейм хостеров либо жёстко маскироваться на обычном хостере

---

**2026-04-15T21:04:40 | Дмитрий Григорьев**
Не светить портами и панелями (лишние порты закрыть, панели перевести на localhost), ставить нормальные не популярные sni, использовать не только reality а попробовать xhttp транспорт
В идеале сделать маскировку с nginx что любой не vless трафик идём на сайт заглушку, так же нужен домен, либо искать бесплатный либо покупать свой (A-запись на ip адрес сервера)

---

**2026-04-15T21:28:52 | .Vadim**
OPENWRT
root@RouteRich:~# nslookup downloads.openwrt.org
Server:  127.0.0.1
Address: 127.0.0.1:53

Non-authoritative answer:
downloads.openwrt.org canonical name = dualstack.j.sni.global.fastly.net

Non-authoritative answer:
downloads.openwrt.org canonical name = dualstack.j.sni.global.fastly.net
Name: dualstack.j.sni.global.fastly.net
Address: 151.101.194.132
Name: dualstack.j.sni.global.fastly.net
Address: 151.101.2.132
Name: dualstack.j.sni.global.fastly.net
Address: 151.101.130.132
Name: dualstack.j.sni.global.fastly.net
Address: 151.101.66.132

GITHUB
root@RouteRich:~# nslookup github.com
Server:  127.0.0.1
Address: 127.0.0.1:53

Non-authoritative answer:

Non-authoritative answer:
Name: github.com
Address: 140.82.121.4


RAW GITHUB
root@RouteRich:~# nslookup raw.githubusercontent.co
Server:  127.0.0.1
Address: 127.0.0.1:53

Non-authoritative answer:
Name: raw.githubusercontent.co
Address: 103.224.212.201

Non-authoritative answer:

---

**2026-04-15T23:12:11 | Vasa**
ну дык это не tcp ))  а реалити

1. - в конфиге юзера в панели указан реалити?
2. SNI попробуй поменять
3. порт в фаерволе на сервере открыт?   сделай ufw disable

---

**2026-04-15T23:16:50 | Vasa**
порт какой?
SNI попробуй пустой тупо оставить

попробуй отдельный инбаунд созадть, вебсокет нешифрованный на любом рандомном порту и протестить

---

**2026-04-15T23:20:03 | Gremlin**
вчера интересный SNI на опыте погонял, МАХа который ( oneme.ru )  Я на мобильном таких скоростей ни разу не видел в нашей деревне. 160 давил. Но одна засада - за 5 минут работы и два замера гиг паразитного трафика нагнал.  Подключение быстрое. Как тест можно пользовать, но на свой страх и риск

---

**2026-04-16T00:10:11 | Дмитрий Григорьев**
Не светить портами и панелями (лишние порты закрыть, панели перевести на localhost), ставить нормальные не популярные sni, использовать не только reality а попробовать xhttp транспорт
В идеале сделать маскировку с nginx что любой не vless трафик идёт на сайт заглушку, так же нужен домен, либо искать бесплатный либо покупать свой (A-запись на ip адрес сервера)

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

**2026-04-16T23:21:17 | Routerich**
короткий ликбез. браузер - tcp пакет - dnsmasq resolv - singbox sniff - fakeip/nofakeip - отправка серверу по ip

---

**2026-04-17T16:23:32 | Вадим Красовский**
Потому что делать нечего с другими протоколами на которых нет sni

---

**2026-04-17T16:25:02 | Vasa**
нах тебе SNI..

---

**2026-04-17T16:26:29 | Вадим Красовский**
Без sni не один протокол больше месяца у тебя не проживет

---

**2026-04-17T16:27:39 | Кирилл**
А ты думаешь, что Роскомпозор будет долго додумываться, что SNI можно анализировать отдельно, и если пакет летит на IP, который с заявленным SNI никак не связан - то его можно сразу дропать? ИМХО это их следующая задача

---

**2026-04-17T16:28:55 | Vasa**
Так. Рассказываю для чего придуман vless reality

Влесс реалити был придуман для обхода простых БС, когда у тебя IP сервака доступен, но раздрешены только ОПРЕДЕЛЕННЫЕ домены

В этом случае ты подменяешь SNI и у тебя всё начинает работать

---

**2026-04-17T16:30:01 | Vasa**
Когда тебе нет надобности обходить блок по SNI, то лучше юзать другое

вебсокеты \ xhttp со своим доменом итд

---

**2026-04-17T16:47:47 | Владимир Волков**
Вы же сами про каскады говорите. Ну постройте несколько хопов, где первый будет в РФ, а конечный - в зарубежье, пока это возможно. Один фиг нормальная белка орехи перегрызёт, никакой sni вам там не поможет никак

---

**2026-04-17T17:41:06 | Vasa**
ясно.. ну я не удивлён. поробуй просто SNI убрать

оставить пустым для теста

---

**2026-04-18T21:20:58 | Игорь**
Из стратегий для запрет2 я всё отключил стандартное, создал новую стратегию и использую только эти три:

--lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=3

--lua-desync=multidisorder:pos=1,midsld:strategy=9

--lua-desync=hostfakesplit:midhost=host-2:host=rzd.ru:tcp_seq=0:tcp_ack=-66000:badsum:strategy=13:final

---

**2026-04-19T13:16:51 | Вадим Красовский**
хз там же тоже sni

---

**2026-04-19T17:00:24 | Yury Kuzmenko**
Вам сервак так скоро блокнут из-за sni

---

**2026-04-19T17:16:57 | Yury Kuzmenko**
а еще более плавно что с sni гугл ходит сайт на мелком хостере в другой подсети

---

**2026-04-19T17:19:23 | Yury Kuzmenko**
Ну это да. Но не нужно палить еще сильнее таким sni лучше вообще без реалити гонять

---

**2026-04-19T21:17:03 | Gremlin**
sni vless пропиши api.oneme.ru  - интересный фифект будет. 😁 Скорость отличная, правда не долго и канал забивается на 100 процентов. Опыты делать там где не жалко. Но как ни странно сервак еще не в блоке. Хотя у "некоторых" и за меньшее блочили

---

**2026-04-19T21:24:54 | Docvspb 🇷🇺**
Ознакомился. Идея хороша в своем безумии. ))

Автор описывает рискованный эксперимент с использованием подмены SNI (Server Name Indication) для протокола VLESS. Он маскирует свой трафик под домен api.oneme.ru (принадлежащий мессенджеру MAX), но натыкается на жесткие технические ограничения и риски блокировки. Разберем по порядку.

🛡️ Что такое SNI и VLESS?

· VLESS: Легковесный протокол для обхода DPI, который делает трафик "невидимым". В отличие от OpenVPN, он не создает характерных для VPN паттернов, что долго позволяло ему оставаться незаметным для систем блокировки.
· SNI (Server Name Indication): Это как табличка с адресом на TLS-рукопожатии, которая сообщает серверу, какой сайт вы хотите открыть (например, google.com).
· Связка в обход блокировок: При подключении к VLESS в настройках часто указывают домен легального сайта (например, VK.com) в поле SNI. Система DPI видит этот "разрешенный" адрес и пропускает ваш зашифрованный трафик, полагая, что вы просто зашли на легальный сайт.

🧪 Что значит "интересный эффект" с api.oneme.ru?

Автор использовал домен api.oneme.ru в качестве маскировки для VLESS. В этом кроется главная хитрость и риск:

· Бэкдор в мессенджере MAX: api.oneme.ru — это API-домен российского мессенджера MAX, который, как выяснили специалисты, скрыто проверяет, использует ли пользователь VPN, отправляя туда служебные запросы.
· Скрытность: Оборудование DPI обычно фильтрует трафик по "белым спискам" и редко блокирует свои локальные сервисы. Маскируясь под служебный домен MAX, автор пытается сделать свой прокси незаметным.

🔥 Почему "канал забивается на 100 процентов"?

· Срабатывание систем защиты: При больших объемах трафика DPI может начать подозревать аномалии. Если пакеты с SNI api.oneme.ru идут на зарубежный IP-адрес, происходит SNI/IP-корреляция — система мгновенно сбрасывает такое соединение.
· DDOS-защита домена: Оборудование api.oneme.ru может посчитать интенсивный прокси-трафик сетевой атакой и начать сбрасывать пакеты, чтобы защитить себя.

⚠️ Почему "эксперименты проводить там, где не жалко"?

Автор называет это опытом, потому что это очень ненадежно. Система либо быстро заблокирует подозрительный трафик по корреляции SNI/IP, либо "забьет канал", защищаясь от ложной атаки. К тому же, если разработчики MAX сменят IP, их бывший "безопасный" домен может оказаться в черном списке.

---

