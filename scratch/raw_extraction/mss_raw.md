# Raw Extraction: mss

**2026-01-09T20:16:51 | Maxim Tatarinov**
Вопрос: Чтобы некоторые домены пропускать через Comss.one DNS достаточно в /etc/config/dhcp в config dnsmasq засунуть list server '/gym.openai.com/195.133.25.16' и т.д, ребутнуть dnsmasq и все будет ок?

---

**2026-01-16T23:34:35 | Mike Rizhoff**
Т.е. если я поставлю прошивку с нуля, потом накачу руантиблок, у меня также будут два дублирующихся по функционалу пункта меню, один из которых будет неактивен? Это странно. У меня сейчас в doh-proxy прописаны commss, например, и он работает. Получается руантиблок втыкает ненужный для последней прошивки пункт меню, потому что руантиблок никто не правил, и он ставит пакеты и менюхи как для старой прошивки?

---

**2026-01-18T04:40:11 | Святос**
https://www.comss.ru/page.php?id=18030

---

**2026-01-21T09:56:19 | Mike Rizhoff**
И еще вопрос по Gemini. Несколько дней все работало без вопросов.Со вчерашнего дня запускается однократно после рестарта телефона. Если закрыть, то получаем геоблок. Обход через днс-серверы (в порядке от первого до последнего - google, x-box, comss) и записи (взятые из этого канала для gemini) в руантиблоке.

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

**2026-01-31T12:06:46 | Илья Греков**
Добрый день. Столкнулся с проблемой (очень странная) может знаете решение или в какую сторону смотреть:

( Что делал что бы исправить: Снес прошивку, обнулил маршрутизатор установил последнюю скаченную тут из форума, ничего не ставил и не настраивал, просто подключил к провайдеру - ошибка воспроизводится. Подключил к другому провайдеру - ошибка воспроизводится. Подключил к другому маршрутизатору routerich на старой (предыдущей прошивке) - ошибка воспроизводится. С ноутбуком - сброс сети, разные браузеры и всё что советовал ИИ, перепробовал кучу вариантов - не помогает (ИИ зашел в тупик, сказал замена оборудования)

запрос составил  ИИ (я допишу курсивом):

У меня наблюдается проблема с доступом к Google Почте (https://mail.google.com/ + гугл таблицы) на одном из ноутбуков в сети через маршрутизатор Routerich. Подробности:

При попытке открыть https://mail.google.com
появляется ошибка:
«Не удается получить доступ к сайту. ERR_FAILED»
Остальные сайты на этом ноутбуке открываются корректно. (Устанавливал подкоп - так же всё работает только не google mail)
На другом ПК (моноблок), подключенном к той же сети и через тот же маршрутизатор, Gmail работает без проблем.
Если подключить проблемный ноутбук через другой маршрутизатор, Gmail работает корректно.
Сброс сетевых настроек Windows на проблемном ноутбуке не помог.
Все устройства используют Windows 10.
Проблема проявляется только на одном устройстве через Routerich (попробовал на двух Routerich с разными провайдерами). По результатам тестов и диагностики предположительно связано с обработкой TCP-пакетов крупных TLS-соединений (MTU/MSS или NAT/flow offload), так как:

Пакеты с размером более ~1400 байт фрагментируются или теряются;
Моноблок и другие устройства работают корректно в тех же условиях;
После изменения маршрутизатора на другой (Xiaomi + какой то от провайдера ) проблема исчезает полностью. Попробовал на другом routerich - проблема повторилась.

Прошу помощи с диагностикой и возможными решениями:

Дальше уже ИИ строит предположения на основе того что я пытался с его помощью решить:

Может ли быть баг в обработке крупных TLS-пакетов или NAT на этом маршрутизаторе? (и на другом так же(!?)... очень подозрительно)

Какие действия на маршрутизаторе можно выполнить, чтобы Gmail заработал на этом ноутбуке без изменения MTU на всех устройствах?

Последнее что не делал это не переустанавливал еще windows...

---

**2026-02-01T16:43:45 | Routerich**
Если у вас работает chatgpt сейчас, то либо у вас что-то запущено где-то, либо comss DNS в настройках днс прописан.

---

**2026-02-05T17:35:21 | Routerich**
Сделайте проще. Добавьте IP компьютера в пункт полностью маршрутизируемые адреса. Обновления скачайте и уберите потом. А легче с comss.ru скачать напрямую

---

**2026-02-07T20:15:21 | Routerich**
Нет, в настройках зероблока добавлять comss dns выбран doh или dot вариант

---

**2026-02-15T12:00:46 | Vasa**
для теста можешь создать отдельную зону и всё там разрешить, включая masquerade и Ограничение MSS

ниже зоны будут входящее \ исходящее
укажи для 2х зон в обоих местах - WAN + LAN

но вообще с самого роутера так то должно работать всё...

эт я выше про межстетевой экран на роутеер говорю

ты же с самого роутера проверяешь?

вообще проще с 2х ПК проверить, там меньше ньюансов

---

**2026-02-22T00:20:29 | Vasa**
убрать из зоны ван

сделать отдельную.

разрешить хождение в лан и ван и обратно

маскард + mss галки

мож так прокатит

---

**2026-03-11T21:01:54 | HiLLL**
ну скачайте с comss https://www.comss.ru/list.php?c=windows10_update

---

**2026-03-28T19:10:02 | HiLLL**
вот мой нестандартный список DOH. С этими днс отключайте список AI. Но смысла особо нет 8.8.8.8 и 9.9.9.9 работают нормально.
dns.comss.one
xbox-dns.ru
dns.malw.link
есть еще в теме на 4pda
https://4pda.to/forum/index.php?act=findpost&pid=137714684&anchor=Spoil-137714684-1

---

**2026-04-01T13:42:36 | Bullet for my valentine Poison**
adding low-priority default empty desync profile we have 1 user defined desync profile(s) and default low priority profile 0 we have 0 user defined desync template(s) profile 1 (noname) lua fake(repeats="6",tcp_ts="-600000",badsum="",blob="blob_tls_clienthello_ticket_rzd_ru" range_in=x0-x0 range_out=a0-a0 payload_type= tls_client_hello) profile 1 (noname) lua multidisorder(pos="1,sniext+1,host+1,midsld,endhost-1" range_in=x0-x0 range_out=a0-a0 payload_type= tls_client_hello)
lists summary:
blobs summary: blob 'fake_default_tls' : size=680 alloc=808 blob 'fake_default_http' : size=263 alloc=263 blob 'fake_default_quic' : size=620 alloc=620
initializing conntrack with timeouts tcp=60:300:60 udp=60 ipcache lifetime 7200s Running as UID=1 GID=1 initializing raw sockets bind-fix4=0 bind-fix6=0 set_socket_buffers fd=3 rcvbuf=2048 sndbuf=32768 fd=3 SO_RCVBUF=4096 fd=3 SO_SNDBUF=65536 set_socket_buffers fd=4 rcvbuf=2048 sndbuf=32768 fd=4 SO_RCVBUF=4096 fd=4 SO_SNDBUF=65536
LUA INIT LUA v5.1 LuaJIT 2.1.1756211046 OpenResty JIT: ON fold cse dce fwd dse narrow loop abc sink fuse LUA REMOVE: os.execute io.popen package.loadlib debug package.loaded.debug LUA BLOB: fake_default_tls (size=680) LUA BLOB: fake_default_http (size=263) LUA BLOB: fake_default_quic (size=620) LUA STR: NFQWS2_VER LUA NUMERIC: qnum desync_fwmark NFQWS2_COMPAT_VER VERDICT_PASS VERDICT_MODIFY VERDICT_DROP VERDICT_MASK VERDICT_PRESERVE_NEXT DEFAULT_MSS IP_BASE_LEN IP6_BASE_LEN TCP_BASE_LEN UDP_BASE_LEN ICMP_BASE_LEN TCP_KIND_END TCP_KIND_NOOP TCP_KIND_MSS TCP_KIND_SCALE TCP_KIND_SACK_PERM TCP_KIND_SACK TCP_KIND_TS TCP_KIND_MD5 TCP_KIND_AO TCP_KIND_FASTOPEN TH_FIN TH_SYN TH_RST TH_PUSH TH_ACK TH_FIN TH_URG TH_ECE TH_CWR IP_RF IP_DF IP_MF IP_OFFMASK IP_FLAGMASK IPTOS_ECN_MASK IPTOS_ECN_NOT_ECT IPTOS_ECN_ECT1 IPTOS_ECN_ECT0 IPTOS_ECN_CE IPTOS_DSCP_MASK IP6F_MORE_FRAG IPV6_FLOWLABEL_MASK IPV6_FLOWINFO_MASK IPPROTO_IP IPPROTO_IPIP IPPROTO_IPV6 IPPROTO_ICMP IPPROTO_TCP IPPROTO_UDP IPPROTO_ICMPV6 IPPROTO_SCTP IPPROTO_HOPOPTS IPPROTO_ROUTING IPPROTO_FRAGMENT IPPROTO_AH IPPROTO_ESP IPPROTO_DSTOPTS IPPROTO_MH IPPROTO_HIP IPPROTO_SHIM6 IPPROTO_NONE ICMP_ECHOREPLY ICMP_DEST_UNREACH ICMP_REDIRECT ICMP_ECHO ICMP_TIME_EXCEEDED ICMP_PARAMETERPROB ICMP_TIMESTAMP ICMP_TIMESTAMPREPLY ICMP_INFO_REQUEST ICMP_INFO_REPLY ICMP_UNREACH_NET ICMP_UNREACH_HOST ICMP_UNREACH_PROTOCOL ICMP_UNREACH_PORT ICMP_UNREACH_NEEDFRAG ICMP_UNREACH_SRCFAIL ICMP_UNREACH_NET_UNKNOWN ICMP_UNREACH_HOST_UNKNOWN ICMP_UNREACH_NET_PROHIB ICMP_UNREACH_HOST_PROHIB ICMP_UNREACH_TOSNET ICMP_UNREACH_TOSHOST ICMP_UNREACH_FILTER_PROHIB ICMP_UNREACH_HOST_PRECEDENCE ICMP_UNREACH_PRECEDENCE_CUTOFF ICMP_REDIRECT_NET ICMP_REDIRECT_HOST ICMP_REDIRECT_TOSNET ICMP_REDIRECT_TOSHOST ICMP_TIMXCEED_INTRANS ICMP_TIMXCEED_REASS ICMP6_ECHO_REQUEST ICMP6_ECHO_REPLY ICMP6_DST_UNREACH ICMP6_PACKET_TOO_BIG ICMP6_TIME_EXCEEDED ICMP6_PARAM_PROB MLD_LISTENER_QUERY MLD_LISTENER_REPORT MLD_LISTENER_REDUCTION ND_ROUTER_SOLICIT ND_ROUTER_ADVERT ND_NEIGHBOR_SOLICIT ND_NEIGHBOR_ADVERT ND_REDIRECT ICMP6_DST_UNREACH_NOROUTE ICMP6_DST_UNREACH_ADMIN ICMP6_DST_UNREACH_BEYONDSCOPE ICMP6_DST_UNREACH_ADDR ICMP6_DST_UNREACH_NOPORT ICMP6_TIME_EXCEED_TRANSIT ICMP6_TIME_EXCEED_REASSEMBLY ICMP6_PARAMPROB_HEADER ICMP6_PARAMPROB_NEXTHEADER ICMP6_PARAMPROB_OPTION LUA BOOL: b_debug b_daemon b_server b_ipcache_hostname b_ctrack_disable LUA RUN FILE: /opt/zapret2/lua/zapret-lib.lua LUA RUN FILE: /opt/zapret2/lua/zapret-antidpi.lua LUA RUN FILE: /opt/zapret2/lua/zapret-auto.lua LUA INIT DONE
opening nfq library handle unbinding existing nf_queue handler for AF_INET (if any) binding nfnetlink_queue as nf_queue handler for AF_INET unbinding existing nf_queue handler for AF_INET6 (if any) binding nfnetlink_queue as nf_queue handler for AF_INET6 binding this socket to queue '65302' setting copy_packet mode set receive buffer size to 1048576

---

**2026-04-11T13:57:59 | Alex Mendez**
тинёк вроде как начал на квн реагировать дерзко (всё как и обещали). На роутере то конечно прекрасно под wifi. Но если нужно что-то разблокировать находясь не под wifi - то как быть то? Приложения видят флаг КВН вкл/выкл и сразу это. 

Пришла в голову идея:
А что если поступить аналогично comss dns - перенаправляя из своего DNS в обёртку, допустим поднять свой DNS на роутере / домашнем сервере и вынудить его проксировать нужное?

Насколько эта задумка осуществима?

Ведь на андроид устройстве не будет никаких системных флагов по поводу того что активен какой-то обход

---

**2026-04-13T10:14:06 | ⁧pcall⁧**
Поставьте dns.comss.one или xbox-dns.ru в DoT конфигурацию стратегии(секции)

---

**2026-04-16T00:02:52 | Алексей Пышкин**
подскажите пожалуйста. нужно ли при настройке awg2 включать маскарадинг и ограничение MSS. В закрепе выше говориться, что нужно отключить, хотя в оф доке awg сказано, что включить нужно

---

