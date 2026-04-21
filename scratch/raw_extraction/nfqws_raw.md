# Raw Extraction: nfqws

**2026-01-01T23:57:56 | Ярослав**
понял, спасибо большое. Настройки фильтра L7 и протокола такие-же как и для ютуба? Меняются только Опции NFQWS, которые подбираются через blockcheck?

---

**2026-01-03T19:04:28 | Святос**
На Самсунге так и не удалось. Ставьте nfqws-keenetic и смотрите везде

---

**2026-01-05T02:17:26 | BaTTr ;/**
Да все получилось но в итоге не фурычит zapret2 с авто стратегии по какой причине хз, ща поставил первый zapret там также костыли пошли либо я не догоняю что, через  nfqws протыкал разные стратегии на гитахбе, в итоге либо работают все но только на телеке и компе или  на iOS и телеке и то только ютуб и инста

---

**2026-01-05T21:10:26 | Снежный**
речь идёт про изменение опции NFQWS?

---

**2026-01-06T12:52:15 | Routerich**
out-range и in-range нужны для оркестрации, для базового применения они не нужны. отсечка будет по параметру NFQWS2_TCP_PKT_OUT + Number of retransmissions autohostlist

---

**2026-01-06T23:14:19 | Борис**
Ребятишки. Вряд ли это кому-то вообще понадобится. Но я целый день пердолился, чтобы заставить работать zapret2 на youtube ipv6. Может, моя инструкция кому-то поможет:
1) в папке /opt/zapret2 редактируете файлы config и config.template таким образом, чтобы был установлен параметр DISABLE_IPV6=0 (по умолчанию поддержка ipv6 выключена, вы её должны включить)
2) поскольку в веб-интерфейсе luci не поддерживается подбор и тестирование стратегий для ipv6, вы должны из командной строки запустить /opt/zapret2/blockcheck2.sh и в утилите прописать ipv6 для подбора, когда она об этом спросит (см. скриншот) 
3) когда утилита начнёт подбор и тестирование, копируйте параметры для nfqws2 из какой-нибудь стратегии, которая помечена как ! AVAILABLE !
4) Доп. скрипты я у себя выключил, т.к. не пользуюсь дискордом, и этот кастомный скрипт discord_media выключал поддержку ipv6 (возможно, это работало только в пределах скрипта, но я всё равно его вырубил от греха подальше)

---

**2026-01-06T23:38:40 | Alexey**
Накатил скрипт 5, но что-то нет youtube на мобилках, меняю NFQWS_OPT через luci в Services/Zapret, но судя по ps -w, nfqws стартуют со своим конфигом и фиолетово им на мои правки, это норма?

---

**2026-01-07T08:03:06 | Anton**
В дачном доме есть два кинетика, в меш сети. На главном развернут nfqws (он же zapret). В последнее время на Ростелекоме эти обходы работают не стабильно, нужно постоянно менять стратегию. В первую очередь мне это нужно для системы видеонаблюдения reolink (они ушли из РФ и достучаться до их серверов можно только с бубном). Так же у меня есть vps с vless. На кинетик как я понял его развернуть тоже не очень просто.
Вопросы:
1. Насколько просто замаршрутизировать часть трафика через vps?
2. Заработает ли меш с кинетиком?

---

**2026-01-07T19:52:51 | Роман**
В опции NFQWS

---

**2026-01-09T17:25:14 | Andrey Yushkov**
Creating ip list table (firewall type nftables)
setting high oom kill priority
reloading nftables set backend (no-update)
Inserting nftables ipv4 rule for nfqws postrouting (qnum 200) : tcp dport {80,443} ct original packets 1-9
Inserting nftables ipv4 rule for nfqws prerouting (qnum 200) : tcp sport {80,443} ct reply packets 1-3
Inserting nftables ipv4 rule for nfqws postrouting (qnum 200) : udp dport {443} ct original packets 1-9
Inserting nftables ipv4 rule for nfqws postrouting (qnum 65400) : udp length >= 28 @ih,32,32 0x2112A442 @ih,0,2 0 @ih,30,2 0
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:--  0:00:55 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:01:21 --:--:--     0

это нормальное поведение скрипта?

---

**2026-01-11T18:31:11 | None**
Я читал это все. Но там не понятно, удалять ли старый запрет или что с ним делать...тот же подкоп обновился одной командой в терминале...а с запретом все глухо. Хорошо хоть даже на старый запрет разраб выкатил новые nfqws_opt и с ними ютуб снова заработал. А подкоп я отключил с ним в ютубе реклама...

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

**2026-01-12T14:03:39 | Routerich**
в nfqws

---

**2026-01-16T10:28:47 | Routerich**
ps |grep nfqws покажет сколько инстанций работает

---

**2026-01-16T10:30:45 | Юрий Теленков**
7500 root      1336 S    grep nfqws
root@RouteRich:~#

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

**2026-01-16T10:35:00 | Routerich**
и на запущенном покажите 
cat /proc/$(pgrep -o nfqws2)/cmdline | tr '\0' '\n'

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

**2026-01-16T16:54:01 | Ванечкхап**
не могу найти Опции NFSQWA. 

в zapret2->Настройки с этими буквами есть NFQWS PORTS TCP и. PORTS UDP.

Опции или OPTIONS нету. в других вкладках тоже не нашел.

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

**2026-01-19T20:46:21 | Святос**
nfqws keenetic still work

---

**2026-01-21T00:43:33 | Routerich**
поздравляю, ты изобрел nfqws

---

**2026-01-21T23:29:41 | Святос**
А Вы обновите и проверьте nfqws-keenetic, там и поговорим

---

**2026-01-27T00:16:48 | Routerich**
по роутеру, потому что постнат и nfqws не в курсе про клиентов. кидается запрос, смотрится ответ, принимается решение. решение держится не помню точно где, мб в контракте мб в самом луа, скорее второе, потому что там прям в логах пишется что достигнут предел работы и пропуск пакетов

---

**2026-01-27T14:19:50 | Kiss_My_Axe**
Да. У него то, что отображается в NFQWS (текстбокс стратегии) пишется в отдельный файл, напрямую не связанный с тем, что читает основной код. Для синхронизации в /opt/zapret есть отдельный скрипт, который по Применить и Перезапустить активируется, читает /etc/config/zapret и мержит его с реальным конфигом.

---

**2026-02-01T00:00:51 | Routerich**
да, трафик и так и так пойдёт через nfqws2 но не будет поломат

---

**2026-02-01T00:06:09 | Routerich**
cat /proc/$(pgrep -o nfqws2)/cmdline | tr '\0' '\n'

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

**2026-02-02T04:00:40 | Routerich**
Гуглите nfqws keenetic и xkeen и подобное

---

**2026-02-03T14:12:14 | Lelik**
Ну хз, не особо селен в целом
nfqws2: поддержка icmp и raw ip
Из интересного как буто

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

**2026-02-11T11:00:56 | Routerich**
поэтому он и nfqws - nftables filter queue window size, по моему как-то так расшифровывается

---

**2026-02-11T16:56:45 | Роман**
Нет, в опции NFQWS

---

**2026-02-14T22:08:02 | Святос**
Тогда не повезло, стратегии менять до посинения. Или удалять Zapret2 и накатывать nfqws-keenetic, обычно дружит с Самсами

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

**2026-02-15T21:40:34 | Марат**
Ну я ожидал работу как в nfqws. Где ютюб работает и без впн.

---

**2026-02-15T21:45:58 | Марат**
Я могу путаться в терминах и прочем, так как я в эту. Тему въехал недели две назад. 
На ином роутере с кинетик я поставил nfqws2 и все. Не вводя свой профиль впн в роутер. И все, ютюб и все что мне надо работало.

---

**2026-02-16T07:38:57 | Lelik**
Я снова вернулся с офигительной идеей.
Нужно сделать скан по текущим листам (на выбор) и по своему собственному списку.
Зачем: нужно для разделения сайтов на разные списки для подбора стратегий для разных доменов. У моего провайдера уже давно разные стратегии на разные домены, приходится вручную подбирать списки и постоянно перебрасывать домены между списками.
Если будет автоматом сам раскидывать домены между списками - вообще конфетка, но я согласен и на ручное.
ПОдобная сканилка есть уже вот тут:
https://github.com/nfqws/nfqws2-keenetic

---

**2026-02-17T16:05:41 | А К**
Ситуация следующая:

curl_test_https_tls13: nfqws strategy for ipv4 rr5---sn-385ou-8v1s.googlevideo.com not found

clearing nfqws redirection

* SUMMARY
curl_test_https_tls12 ipv4 rr5---sn-385ou-8v1s.googlevideo.com : nfqws not working
curl_test_https_tls13 ipv4 rr5---sn-385ou-8v1s.googlevideo.com : nfqws not working

Please note this SUMMARY does not guarantee a magic pill for you to copy/paste and be happy.
Understanding how strategies work is very desirable.
This knowledge allows to understand better which strategies to prefer and which to avoid if possible, how to combine strategies.
Blockcheck does it's best to prioritize good strategies but it's not bullet-proof.
It was designed not as magic pill maker but as a DPI bypass test tool.

=== КОНЕЦ ПОИСКА СТРАТЕГИЙ ===

[ERROR] Ошибка: не удалось извлечь стратегию

[INFO] Завершение работы...
root@RouteRich:~# 


что с этим делать дальше?...

---

**2026-02-17T19:24:25 | Святос**
Владельцам ТВ Самсунг, Сони и ЛЖ вместо Zapret: https://github.com/Anonym-tsk/nfqws-keenetic

---

**2026-02-18T09:59:02 | Vladimir Shubin**
Здравствуйте. 
Купил данный роутер, он будет работать в другом городе.
Сейчас хочу сделать первоначальную настройку, обновить при необходимости прошивку, поставить Зероблок (его одного достаточно,  или желательно ещё скрипт 5 ?).
На данный момент у меня основной роутер кинетик (с nfqws).
Как лучше подключить РР? Поменять мак и подключить вместо кинетика?
Или есть другие варианты?

---

**2026-02-18T23:24:14 | Святос**
Вот например из zapret2 дискорд
--new
--filter-tcp=80,443,1080,2053,2083,2087,2096,8443
--hostlist=/opt/etc/nfqws2/lists/discord.list
--out-range=-d10
--lua-desync=hostfakesplit_multi:hosts=google.com,vimeo.com:tcp_ts=-1000:tcp_md5:repeats=2

---

**2026-02-18T23:37:13 | Святос**
https://github.com/nfqws/nfqws2-keenetic
У нас тут дискорд всё ещё работает, не могу ничего потестировать, пробуйте за меня

---

**2026-02-18T23:56:17 | А**
Извините за тупой вопрос - это теперь можно просто добавить новыми строчками в конец Опции NFQWS ?

---

**2026-02-19T00:15:00 | Марат**
Не знаю как, но пока все работает) амнезия и отдельно поставил nfqws2

---

**2026-02-22T17:27:01 | Routerich**
Cannot install package luci-app-zeroblock
  Cannot install package nfqws
  Cannot install package nfqws2
Это тоже твое ?

---

**2026-02-23T04:44:45 | Борис**
Речь про стратегии в одной секции опций NFQWS, которые переключаются циклически, или про отдельные стратегии, которые отдельно в uci хранятся?

---

**2026-02-26T14:07:05 | Bullet for my valentine Poison**
Те страты что напихали в Nfqws ваши с блокчека?

---

**2026-02-26T20:18:16 | Борис**
у тебя на скрине какая-то системная ошибка 
nfq_create_queue(): Operation not permitted

у тебя наверное запущен запрет в то время, пока блокчек работает? если дать команду в терминале, что выдаёт?
ps | grep nfqws

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

**2026-02-28T23:20:23 | Garsia**
Если честно, половину слов не понял.
В пункте 30 говорится про "типовые", а мне надо для конкретного сайта. Или я чего-то не понимаю? Он подобрал мне пять штук для рутректера. Правильно ли я понимаю, что просто вставить их в Опции NFQWS недостаточно?

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

**2026-03-02T00:02:19 | V I T Λ L Y**
Ага нашел, опции NFQWS

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

**2026-03-04T10:10:20 | Святос**
Удалите или остановите запрет 2, проверьте https://github.com/nfqws/nfqws2-keenetic

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

**2026-03-05T11:26:04 | Святос**
Опции NFQWS

---

**2026-03-05T11:55:04 | Роман**
Где в опциях NFQWS порты?

---

**2026-03-05T11:58:11 | Routerich**
чисто технически, это всё nfqws option просто вам это преподнесено иначе

---

**2026-03-05T14:44:10 | IT**
Так понял эти закарючки и есть "стратегии" и именно их пихать в поле NFQWS

---

**2026-03-05T20:52:04 | KyM**
Подскажите куда прописывать стратегии которые нашли blockchech.sh и blockchech2.sh ? прописываю в поле NFQWS_OPT на вкладке Zapret - Settings ->
NFQWS options, но сайты которые были указаны в стратегиях по прежнему не работают.

---

**2026-03-05T22:40:35 | Aндрей**
Давайте определимся с терминами - что мы подразумеваем под словом «стратегия»? Команды в поле «Опции NFQWS» в zapret 2? Верно?

---

**2026-03-06T16:38:00 | Святос**
https://github.com/whxtelxs/nfqws-zapret-converter

---

**2026-03-18T20:13:24 | Святос**
Испытайте пакет nfqws2-keenetic, если уж там не поползет, то они будут самыми злыми

---

**2026-03-19T14:13:01 | Chezok**
строка youtube редактировать, в самом низу "Опции NFQWS" очистить и вписать что выше скинул

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

**2026-03-21T20:28:47 | Борис**
Мне кажется у тебя неправильно написаны опции для nfqws. Ты там дублируешь фильтр L7, фильтр tcp. Стратегия начинается с --payload

---

**2026-03-21T20:28:57 | Bullet for my valentine Poison**
Ну вот первый совет, открыть мануал по запрету на 30 пункте и посмотреть как пишутся опции NFQWS. Ибо у вас там хаос...оно походу и ломает. Плюс порты указываются выше и на главной странице запрета.

---

**2026-03-21T23:42:27 | Борис**
Через утилиту service разработчик не все команды правильно обозначил, поэтому может что-то неправильно отображаться. Можно в консоли написать ps | grep zapret или ps | grep nfqws и там будет точно показывать, работает он или нет

---

**2026-03-21T23:43:31 | Routerich**
nfqws2/nfqws

---

**2026-03-21T23:49:29 | Kiss_My_Axe**
Тестить запрет по nfqws? Эт вы широко так загребли. :)

---

**2026-03-21T23:51:04 | Routerich**
такого софта не существует, это всё обертки для nfqws

---

**2026-03-21T23:56:34 | Борис**
Если читать буквально то, что написано, то у тебя на роутере установлено 10 запретов. Назовём их условно zapret, zapret2, zapret3 и т.д. Мы выяснили, что программа zapret в каком бы то ни было виде не отображается в процессах через ps. Под капотом она обращается к другой программе - nfqws. Это значит, что этот запущенный nfqws в одном экземпляре прикреплён ко всем 10 запретам (даже к zapret10). Получается одним выстрелом можно kill 10 зайцев. Но лучше все-таки один запрет в системе оставить

---

**2026-03-21T23:58:02 | Routerich**
ня, можно сейвить в переменную и толкать nfqws/nfqws2 через эту переменную
 cat /proc/$(pgrep -o nfqws2)/cmdline | tr '\0' '\n'

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

**2026-03-23T07:53:42 | Vladimir Shubin**
Доброго времени суток. Что надо сделать, чтобы заработал инстаграмм? (на кинетике через nfqws работает). 
Так же на роутере установлен Zapret2.

---

**2026-03-27T01:50:00 | Kiss_My_Axe**
А можно переопределять расположение зависимостей? Того же nfqws2?
Понятно, что можно ссылку создать, но зачем. 😀

---

**2026-03-28T20:11:59 | Станислав Земляков**
Если надо гонять на роутере, есть --via фича. Оператива утилизируется локально, nfqws2 локально поднимается, а траффик через роутер

---

**2026-03-28T23:50:56 | Станислав Земляков**
Домен не резолвится на уровне DNS. Это не SNI/DPI блокировка — zapret2/nfqws2 здесь бессилен. Решение - смена DNS-резолвера (DoH/DoT), а не anti-DPI.

---

**2026-03-29T00:18:07 | Станислав Земляков**
Согласен полностью, но zapret2(nfqws2) - тем и хорош, что это не КВН. Не надо переключать туда-суда, когда хочешь открыть, например, банковское приложение. Это L2, а значит можно вообще жить в отрыве от КВН стэка. Короче, свои плюсы тоже есть

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

**2026-04-01T13:42:46 | Bullet for my valentine Poison**
Из лога видно:
•   Блоб рандомный:
 — в прошлый раз был другой, теперь RZD, значит выбор из списка реально крутится.
•   multidisorder тоже рандомный:
 — подмножество из нашего набора, каждый раз будет другой.
•   Отдельный профиль, отдельный qnum:
 +  — это именно наш кастомный nfqws для Tarkov-портов.

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

**2026-04-05T07:28:29 | Константин Волчек**
Доброе утро. На ночь ставил поиск стратегий для discord и в самом низу он выдал это:
curl_test_https_tls12: nfqws2 strategy for ipv4 discord.com not found

clearing nfqws2 redirection

* SUMMARY
curl_test_https_tls12 ipv4 discord.com : nfqws2 not working

Please note this SUMMARY does not guarantee a magic pill for you to copy/paste and be happy.
Understanding how strategies work is very desirable.
This knowledge allows to understand better which strategies to prefer and which to avoid if possible, how to combine strategies.
Blockcheck does it's best to prioritize good strategies but it's not bullet-proof.
It was designed not as magic pill maker but as a DPI bypass test tool.

все плохо?

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

**2026-04-07T10:20:00 | Rom@n**
NFQWS_OPT_DESYNC_WG="${NFQWS_OPT_DESYNC_WG:---dpi-desync=fake --dpi-desync-repeats=2}"

---

**2026-04-09T15:35:51 | Vitaly**
Всем привет,
прошу помощи,
есть Routerich AX3000 v1 RouteRich 24.10.5 (r29087-d9c5716d1d) RR-3.9.0
подключил его по PPPoE к провайдеру,
что нужно сделать чтобы завести Ютуп ?
Обычно Кинетик + nfqws2 пользовал.
Первым делом DoT и DoH запустить ?
Есть какой мануал ?

---

**2026-04-10T16:41:09 | Andrey Maklakov**
я про 403 и явный таймаут на Inserting nftables ipv4 rule for nfqws postrouting (qnum 65400) : udp length >= 28 @ih,32,32 0x2112A442 @ih,0,2 0 @ih,30,2

---

**2026-04-10T16:41:18 | Дмитрий Б.**
вот ○  zapret (nfqws)  Не запущено

---

**2026-04-12T01:38:33 | support**
Подскажите почему это не работает адекватно, ютюб работает, но все остально что на скринах пугает. 
NFQWS2_OPT="--filter-udp=443 --filter-l7=quic --hostlist-domains=youtube.com,googlevideo.com,youtu.be,googleapis.com,ytimg.com,ggpht.com,gstatic.com,google.com --out-range=-s34228 --payload=quic_initial --lua-desync=fake:blob=quic_initial:ip_ttl=6 --new --filter-udp=443 --filter-l7=quic --hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt --out-range=-s34228 --payload=quic_initial --lua-desync=fake:blob=quic_initial:repeats=6 --new --filter-tcp=80 --filter-l7=http --hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt --out-range=-s34228 --payload=http_req --lua-desync=fake:blob=http:tcp_md5 --lua-desync=multisplit:pos=method+2 --new --filter-tcp=443 --filter-l7=tls --hostlist-domains=youtube.com,googlevideo.com,youtu.be,googleapis.com,ytimg.com,ggpht.com,gstatic.com,google.com --out-range=-s34228 --in-range=-s5556 --lua-desync=circular:fails=1:maxtime=5 --in-range=x --payload=tls_client_hello --lua-desync=multidisorder:pos=1,midsld:strategy=1 --lua-desync=multidisorder:pos=1:seqovl=681:seqovl_pattern=tls_clienthello:strategy=2 --lua-desync=multidisorder:pos=10,midsld:seqovl=336:seqovl_pattern=tls_clienthello:strategy=3 --lua-desync=multisplit:pos=1,sniext+1:seqovl=1:strategy=4 --lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=www.google.com:strategy=5 --lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=google.com:strategy=6 --lua-desync=fakedsplit:pos=midsld:strategy=7 --lua-desync=multidisorder:pos=1,midsld,sniext:strategy=8 --lua-desync=multidisorder:pos=1,sniext+1,midsld-2,midsld,midsld+2:strategy=9 --lua-desync=fake:blob=tls_clienthello:ip_ttl=6:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=rzd.ru:repeats=4:strategy=9 --lua-desync=multidisorder:pos=2,5,105,sniext+5,midsld-1:strategy=10 --lua-desync=multisplit:pos=10:seqovl=1:strategy=11 --new --filter-tcp=443 --filter-l7=tls --hostlist=/opt/zapret2/ipset/zapret-hosts-user.txt --out-range=-s34228 --payload=tls_client_hello --lua-desync=fake:blob=tls_clienthello:tls_mod=rnd,dupsid,sni=2gis.com --lua-desync=multisplit:pos=2 --new --filter-l7=mtproto --payload=mtproto_initial --lua-desync=fake:blob=0x00000000 --new --filter-tcp=443 --filter-l7=tls --ipset=/opt/zapret2/ipset/zapret-ips-user.txt --out-range=-s34228 --payload=tls_client_hello --lua-desync=multidisorder:pos=1,sniext+1,midsld-2,midsld,midsld+2 --lua-desync=fake:blob=tls_clienthello:ip_ttl=6:tcp_seq=-10000:tcp_ack=-66000:tls_mod=rnd,dupsid,sni=rzd.ru:repeats=4"

---

**2026-04-12T11:55:38 | Роман**
Создать список доменов роблокса, создать стратегию на главной и выбрать там список с доменами роблокса. Вписать стратегию в поле nfqws.

---

**2026-04-14T10:06:07 | VecH.Pro**
поставил пакет nfqws2-keenetic (для openwrt) с его web мордой

побаловался и удалил

теперь пытаюсь зайти в luci и вижу что она у меня куда то отъехала )))

---

**2026-04-15T15:49:09 | 01000000**
Привет. Опять Нинтендо. Опять игра мк8d. Вот что я делаю не так?
В запрете2 в списках в юзер добавил домены Нинтендо что нашел. Сохранил применил.
В настройках добавил список юзер, включил его, установил как в гайде тср, tls и тд, и тп. Еще добавил список авто ТК начитался в инструкции что в него автоматом добавляются домены сайтов куда не можешь зайти. Сохранил применил.
В блокчеке2 по очереди и вводил домены Нинтендо и запускал тест. По гайду включал get https.
Вводил всякие  —payload... и — lua... в настройках в списке юзер. Включил в нем автолист. Сохранить применить.
А дальше как в гайде. Запустил, проверил, удалил эту страту нерабочую сохранил применил проверил и тд
И ничего.
Пошел в поиск стратегий. Запускаю тест. Проходит 904 чего-то там. Запускается уже сам поиск стратегий. Одновременно на Нинтендо пытаюсь зайти в онлайн. Вылетаю из онлайн. И обычно на 9-й стратегии, о чудо, происходит заход в онлайн.
Я копирую — lua... и — payload... nfqws2 списка юзер проверяю и не работает!
И так все время. Ждешь 47 минут пока в тесте в поиске стратегий пройдет 904 шага, запускаешь нинтенду ина 9-й стратегии происходит вход в онлайн! Как закрепить полученные результаты чтобы по 50 минут не ждать впредь?
Список ip не делал потому что у Нинтендо динамические адреса.
Ну я накатал, пойду отдохну. Извиняюсь.

Аа, еще телеграм подтупливает.

---

**2026-04-16T13:34:48 | Ruslan Bilyk**
Провёл блокчек2 проверку. В конце выдало/
'''
* SUMMARY
curl_test_https_tls12 ipv4 discord.com : nfqws2 not working
'''
Что это значит? Что у меня что-то не так сделано?

---

**2026-04-16T14:59:25 | Ruslan Bilyk**
Я перепутал. Уже разобрался почти со всем. Только с тем, что у меня blockcheck2 не находит ничего сколько бы времени я не искал.
* SUMMARY
curl_test_https_tls12 ipv4 discord.com : nfqws2 not working

---

**2026-04-16T22:34:57 | Vitaly**
я так понимаю нужно в блоке опций NFQWS, полностью все заменить ?
( а не заменить какой то блок, или дописать в конце )

---

**2026-04-17T21:46:20 | The Wisest**
В Опции NFQWS вставить steampowered.com?

---

**2026-04-18T21:21:51 | Игорь**
потестите тоже, возможно они пересекается с тут встречающимися стратегиями. Но у меня только это в опциях NFQWS

---

**2026-04-19T20:42:05 | 𝕮𝖞𝖇𝖊𝖗 𝕮𝖗𝖔𝖜**
Вот мне 5 страт вроде накидал. 
Я правильно понял, что мне их надо в "Опции NFQWS"  вставить в конце уже существующего списка, сохранить и перезапустить шарманку?

---

**2026-04-19T21:32:30 | Maxim =)))**
Меняю в секции youtube, а именно - Опции NFQWS
потом сохраняю, применяю, перезапускаю и иду на youtube

---

