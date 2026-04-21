# Raw Extraction: fragment

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

**2026-02-11T22:21:27 | Vasa**
У меня нет Зероблок

но я себе прибил вот такими настройками ТГ, гвоздями)

##TG

##IP
91.108.56.0/22
91.108.4.0/22
91.108.8.0/22
91.108.16.0/22
91.108.12.0/22
149.154.160.0/20
91.105.192.0/23
91.108.20.0/22
185.76.151.0/24

##domain

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

**2026-02-14T10:24:32 | Роман**
Свой ключ vless, всё работает отлично.
Попробуйте добавить эти домены и ip в список пользовательских доменов и ip. Но возможны пересечения со списком телеграмм.

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
```91.108.56.0/22
91.108.4.0/22
91.108.8.0/22
91.108.16.0/22
91.108.12.0/22
149.154.160.0/20
91.105.192.0/23
91.108.20.0/22
185.76.151.0/24`

---

**2026-02-14T11:19:39 | Vasa**
попробуй в дополнение к списку добавить

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

**2026-02-14T23:58:47 | Vasa**
в ту же секцию, где у тебя добавлен список от подкопа, добавть ручные - 

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

**2026-02-17T12:34:26 | Vasa**
попробуй в дополнение к списку добавить

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

**2026-02-19T10:49:04 | Vasa**
попробуй для теста добавить в ту же секцию где у тебя выбран список ТГ в подкопе

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

**2026-02-22T11:13:08 | Vasa**
попробуй в дополнение к списку добавить
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

**2026-02-28T14:19:02 | Святос**
cdn-telegram.org
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
91.108.56.0/22
91.108.4.0/22
91.108.8.0/22
91.108.16.0/22
91.108.12.0/22
149.154.160.0/20
91.105.192.0/23
91.108.20.0/22
185.76.151.0/24
2001:b28:f23d::/48
2001:b28:f23f::/48
2001:67c:4e8::/48
2001:b28:f23c::/48
2a0a:f280::/32

---

**2026-03-09T13:44:57 | Святос**
cdn-telegram.org
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
k.telegram.org
web.telegram.org
z.telegram.org
91.105.192.0/23
91.108.4.0/22
91.108.8.0/22
91.108.12.0/22
91.108.16.0/22
91.108.20.0/22
91.108.56.0/22
95.161.64.0/20
149.154.160.0/20
149.154.162.0/23
149.154.164.0/23
149.154.166.0/23
185.76.151.0/24
2001:67c:4e8::/48
2001:b28:f23c::/48
2001:b28:f23d::/48
2001:b28:f23f::/48
2a0a:f280::/32

---

**2026-03-09T18:22:51 | Forward**
Подскажи пожалуйста. Пытаюсь добавить
"fragment": {
  "interval": "10-20",
  "length": "50-100",
  "packets": "1-3"
}
Пробовал добавлять в outbound, но он не применяется. Через JSON тоже не получилось. Как это правильно реализовать?
Ремнавей

---

**2026-03-09T20:12:44 | Forward**
а щас нужно  fragment настрроить в ремнавей

---

**2026-03-09T20:13:59 | Forward**
"fragment": {
    "interval": "10-20",
    "length": "50-100",
    "packets": "1-3"

---

**2026-03-12T17:03:07 | Святос**
Собирал по разным местам, у меня ipv6 отключено, поэтому подсетей этих нет, файлы от меня улетают почти со скоростью 100 Мб так быстро у меня телега очень давно не работала  cdn-telegram.org
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
telegram.ai
telegram.asia
telegram.biz
telegram.cloud
telegram.cn
telegram.co
telegram.com
telegram.de
telegram.dev
telegram.eu
telegram.fr
telegram.host
telegram.in
telegram.info
telegram.io
telegram.jp
telegram.net
telegram.qa
telegram.ru
telegram.services
telegram.solutions
telegram.team
telegram.tech
telegram.uk
telegram.us
telegram.website
telegram.xyz
telesco.pe
tg.dev
tg.org
tx.me
t.co
usercontent.dev
teleg.xyz
telegramapp.org
nicegram.app
tgram.org
torg.org
stel.com
telegramdownload.com
91.108.56.0/22
91.108.4.0/22
91.108.8.0/22
91.108.16.0/22
91.108.12.0/22
149.154.160.0/20
91.105.192.0/23
91.108.20.0/22
185.76.151.0/24
5.28.192.0/18
95.161.64.0/20

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

**2026-03-18T19:53:32 | Routerich**
zeroblock + fragment (как создавать в changelog) 
либо подкоп и mixed proxy. последний в любом из двух пакетов есть

---

**2026-03-19T14:26:21 | Chezok**
я долго с этим боролся, помогло следующее (не помню кто посоветовал тут)
в awg10 добавляем группу Messengers

в прокси Opera делаем пользовательские списки, в домены вписываем это:
telegram.org
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
telegram.ai
telegram.asia
telegram.biz
telegram.cloud
telegram.cn
telegram.co
telegram.com
telegram.de
telegram.dev
telegram.eu
telegram.fr
telegram.host
telegram.in
telegram.info
telegram.io
telegram.jp
telegram.net
telegram.qa
telegram.ru
telegram.services
telegram.solutions
telegram.team
telegram.tech
telegram.uk
telegram.us
telegram.website
telegram.xyz
telesco.pe
tg.dev
tg.org
tx.me
t.co
usercontent.dev
teleg.xyz
telegramapp.org
nicegram.app
tgram.org
torg.org
stel.com
telegramdownload.com

А в подсети пользовательские это:

91.108.56.0/22
91.108.4.0/22
91.108.8.0/22
91.108.16.0/22
91.108.12.0/22
149.154.160.0/20
91.105.192.0/23
91.108.20.0/22
185.76.151.0/24
5.28.192.0/18
95.161.64.0/20

---

**2026-03-20T09:41:57 | Роман**
Собирал по разным местам, у меня ipv6 отключено, поэтому подсетей этих нет, файлы от меня улетают почти со скоростью 100 Мб так быстро у меня телега очень давно не работала  

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
telegram.ai
telegram.asia
telegram.biz
telegram.cloud
telegram.cn
telegram.co
telegram.com
telegram.de
telegram.dev
telegram.eu
telegram.fr
telegram.host
telegram.in
telegram.info
telegram.io
telegram.jp
telegram.net
telegram.qa
telegram.ru
telegram.services
telegram.solutions
telegram.team
telegram.tech
telegram.uk
telegram.us
telegram.website
telegram.xyz
telesco.pe
tg.dev
tg.org
tx.me
t.co
usercontent.dev
teleg.xyz
telegramapp.org
nicegram.app
tgram.org
torg.org
stel.com
telegramdownload.com

91.108.4.0/22
91.108.8.0/22
91.108.16.0/22
91.108.12.0/22
149.154.160.0/20
91.105.192.0/23
91.108.20.0/22
185.76.151.0/24
5.28.192.0/18
95.161.64.0/20

---

**2026-03-20T12:37:08 | Anna Bagler**
Собирал по разным местам, у меня ipv6 отключено, поэтому подсетей этих нет, файлы от меня улетают почти со скоростью 100 Мб так быстро у меня телега очень давно не работала 
cdn-telegram.org
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
telegram.ai
telegram.asia
telegram.biz
telegram.cloud
telegram.cn
telegram.co
telegram.com
telegram.de
telegram.dev
telegram.eu
telegram.fr
telegram.host
telegram.in
telegram.info
telegram.io
telegram.jp
telegram.net
telegram.qa
telegram.ru
telegram.services
telegram.solutions
telegram.team
telegram.tech
telegram.uk
telegram.us
telegram.website
telegram.xyz
telesco.pe
tg.dev
tg.org
tx.me
t.co
usercontent.dev
teleg.xyz
telegramapp.org
nicegram.app
tgram.org
torg.org
stel.com
telegramdownload.com
Подсети, что-то код не оборачивается.
91.108.56.0/22
91.108.4.0/22
91.108.8.0/22
91.108.16.0/22
91.108.12.0/22
149.154.160.0/20
91.105.192.0/23
91.108.20.0/22
185.76.151.0/24
5.28.192.0/18
95.161.64.0/20

---

**2026-03-20T17:01:04 | Bullet for my valentine Poison**
Собирал по разным местам, у меня ipv6 отключено, поэтому подсетей этих нет, файлы от меня улетают почти со скоростью 100 Мб так быстро у меня телега очень давно не работала  cdn-telegram.org
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
telegram.ai
telegram.asia
telegram.biz
telegram.cloud
telegram.cn
telegram.co
telegram.com
telegram.de
telegram.dev
telegram.eu
telegram.fr
telegram.host
telegram.in
telegram.info
telegram.io
telegram.jp
telegram.net
telegram.qa
telegram.ru
telegram.services
telegram.solutions
telegram.team
telegram.tech
telegram.uk
telegram.us
telegram.website
telegram.xyz
telesco.pe
tg.dev
tg.org
tx.me
t.co
usercontent.dev
teleg.xyz
telegramapp.org
nicegram.app
tgram.org
torg.org
stel.com
telegramdownload.com
91.108.56.0/22
91.108.4.0/22
91.108.8.0/22
91.108.16.0/22
91.108.12.0/22
149.154.160.0/20
91.105.192.0/23
91.108.20.0/22
185.76.151.0/24
5.28.192.0/18
95.161.64.0/20

---

**2026-03-20T17:16:32 | Gomer Simpson**
Собирал по разным местам, у меня ipv6 отключено, поэтому подсетей этих нет, файлы от меня улетают почти со скоростью 100 Мб так быстро у меня телега очень давно не работала  cdn-telegram.org
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
telegram.ai
telegram.asia
telegram.biz
telegram.cloud
telegram.cn
telegram.co
telegram.com
telegram.de
telegram.dev
telegram.eu
telegram.fr
telegram.host
telegram.in
telegram.info
telegram.io
telegram.jp
telegram.net
telegram.qa
telegram.ru
telegram.services
telegram.solutions
telegram.team
telegram.tech
telegram.uk
telegram.us
telegram.website
telegram.xyz
telesco.pe
tg.dev
tg.org
tx.me
t.co
usercontent.dev
teleg.xyz
telegramapp.org
nicegram.app
tgram.org
torg.org
stel.com
telegramdownload.com
91.108.56.0/22
91.108.4.0/22
91.108.8.0/22
91.108.16.0/22
91.108.12.0/22
149.154.160.0/20
91.105.192.0/23
91.108.20.0/22
185.76.151.0/24
5.28.192.0/18
95.161.64.0/20

---

**2026-03-20T17:42:34 | Мишка Тедди Ростовые Куклы**
Я читаю , убрал все с секции дескорд. В секции main вставил информацию сообщение 
Собирал по разным местам, у меня ipv6 отключено, поэтому подсетей этих нет, файлы от меня улетают почти со скоростью 100 Мб так быстро у меня телега очень давно не работала  cdn-telegram.org
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
telegram.ai
telegram.asia
telegram.biz
telegram.cloud
telegram.cn
telegram.co
telegram.com
telegram.de
telegram.dev
telegram.eu
telegram.fr
telegram.host
telegram.in
telegram.info
telegram.io
telegram.jp
telegram.net
telegram.qa
telegram.ru
telegram.services
telegram.solutions
telegram.team
telegram.tech
telegram.uk
telegram.us
telegram.website
telegram.xyz
telesco.pe
tg.dev
tg.org
tx.me
t.co
usercontent.dev
teleg.xyz
telegramapp.org
nicegram.app
tgram.org
torg.org
stel.com
telegramdownload.com
91.108.56.0/22
91.108.4.0/22
91.108.8.0/22
91.108.16.0/22
91.108.12.0/22
149.154.160.0/20
91.105.192.0/23
91.108.20.0/22
185.76.151.0/24
5.28.192.0/18
95.161.64.0/20

---

**2026-03-22T15:22:34 | ㅤㅤ**
Собирал по разным местам, у меня ipv6 отключено, поэтому подсетей этих нет, файлы от меня улетают почти со скоростью 100 Мб так быстро у меня телега очень давно не работала  cdn-telegram.org
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
telegram.ai
telegram.asia
telegram.biz
telegram.cloud
telegram.cn
telegram.co
telegram.com
telegram.de
telegram.dev
telegram.eu
telegram.fr
telegram.host
telegram.in
telegram.info
telegram.io
telegram.jp
telegram.net
telegram.qa
telegram.ru
telegram.services
telegram.solutions
telegram.team
telegram.tech
telegram.uk
telegram.us
telegram.website
telegram.xyz
telesco.pe
tg.dev
tg.org
tx.me
t.co
usercontent.dev
teleg.xyz
telegramapp.org
nicegram.app
tgram.org
torg.org
stel.com
telegramdownload.com
91.108.56.0/22
91.108.4.0/22
91.108.8.0/22
91.108.16.0/22
91.108.12.0/22
149.154.160.0/20
91.105.192.0/23
91.108.20.0/22
185.76.151.0/24
5.28.192.0/18
95.161.64.0/20

---

**2026-03-22T17:30:45 | Иван Порошин**
для тех кто искал полный список доменов и пулл айпи для тг

cdn-telegram.org // Сеть доставки контента (фото, видео)
comments.app // Сервис комментариев для каналов
contest.com // Платформа для проведения конкурсов Telegram
fragment.com // Платформа для покупки имен и номеров (TON)
graph.org // Зеркало редактора статей Telegraph
quiz.directory // Сервис для создания опросов и викторин
t.me // Основной домен коротких ссылок
tdesktop.com // Официальный сайт Telegram Desktop
telega.one // Старое зеркало для коротких ссылок
telegra.ph // Редактор статей и постов
telegram-cdn.org // Резервный домен сети доставки контента
telegram.dog // Официальный короткий домен (часто для имен пользователей)
telegram.me // Один из основных доменов для ссылок на профили
telegram.org // Главный официальный сайт проекта
telegram.space // Резервный технический домен
telegram.ai // Домен для сервисов на базе ИИ
telegram.asia // Региональный технический домен (Азия)
telegram.biz // Резервный домен для бизнес-функций
telegram.cloud // Технический домен облачного хранилища
telegram.cn // Региональный домен (Китай)
telegram.co // Резервный домен (Колумбия/Общий)
telegram.de // Региональный домен (Германия)
telegram.dev // Домен для разработчиков и документации API
telegram.eu // Региональный домен (Европа)
telegram.fr // Региональный домен (Франция)
telegram.host // Вспомогательный хостинг-домен
telegram.in // Региональный домен (Индия)
telegram.info // Информационный домен
telegram.io // Технический домен для API/разработки
telegram.jp // Региональный домен (Япония)
telegram.net // Технический домен инфраструктуры сети
telegram.qa // Региональный домен (Катар)
telegram.ru // Региональный домен (Россия)
telegram.services // Домен для служебных микросервисов
telegram.solutions // Резервный домен для бизнес-решений
telegram.team // Внутренний домен для команды разработки
telegram.tech // Домен для технических спецификаций
telegram.uk // Региональный домен (Великобритания)
telegram.us // Региональный домен (США)
telegram.website // Вспомогательный веб-домен
telegram.xyz // Экспериментальный технический домен
telesco.pe // Хостинг для видеосообщений («кружочков»)
tg.dev // Главный ресурс для разработчиков
tg.org // Резервный короткий домен организации
tx.me // Служебный домен для прокси и обхода блокировок
usercontent.dev // Хостинг пользовательского контента
teleg.xyz // Резервный технический домен
telegramapp.org // Вспомогательный домен приложения
nicegram.app // Ресурс стороннего клиента Nicegram
tgram.org // Резервный домен (сообщество)
torg.org // Старый технический домен
stel.com // Домен, связанный с регистрацией имен
telegramdownload.com // Ресурс для скачивания дистрибутивов
api.telegram.org // Главный сервер для работы всех ботов
web.telegram.org // Основной адрес веб-версии мессенджера
web.t.me // Зеркало для доступа к веб-версии
venus.web.telegram.org // Балансировщик нагрузки веб-клиента
pluto.web.telegram.org // Балансировщик нагрузки веб-клиента
flora.web.telegram.org // Балансировщик нагрузки веб-клиента
atlanta.web.telegram.org // Балансировщик нагрузки веб-клиента
t-me.red // Резервный домен для коротких ссылок
cdn-telegram.me // Дополнительный узел доставки контента
stickers.tdesktop.com // Сервер синхронизации стикеров в приложении

---

**2026-03-27T14:30:34 | Bullet for my valentine Poison**
cdn-telegram.org
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
telegram.ai
telegram.asia
telegram.biz
telegram.cloud
telegram.cn
telegram.co
telegram.de
telegram.dev
telegram.eu
telegram.fr
telegram.host
telegram.in
telegram.info
telegram.io
telegram.jp
telegram.net
telegram.qa
telegram.ru
telegram.services
telegram.solutions
telegram.team
telegram.tech
telegram.uk
telegram.us
telegram.website
telegram.xyz
telesco.pe
tg.dev
tg.org
tx.me
usercontent.dev
teleg.xyz
telegramapp.org
nicegram.app
tgram.org
torg.org
stel.com
telegramdownload.com
api.telegram.org
web.telegram.org
web.t.me
venus.web.telegram.org
pluto.web.telegram.org
flora.web.telegram.org
atlanta.web.telegram.org
t-me.red
cdn-telegram.me
stickers.tdesktop.com
у вас есть поиск стратегий и мощные роутеры) Вперед)

---

**2026-03-31T08:21:22 | meow**
можете оплатить через https://fragment.com/

---

**2026-04-01T13:42:36 | Bullet for my valentine Poison**
adding low-priority default empty desync profile we have 1 user defined desync profile(s) and default low priority profile 0 we have 0 user defined desync template(s) profile 1 (noname) lua fake(repeats="6",tcp_ts="-600000",badsum="",blob="blob_tls_clienthello_ticket_rzd_ru" range_in=x0-x0 range_out=a0-a0 payload_type= tls_client_hello) profile 1 (noname) lua multidisorder(pos="1,sniext+1,host+1,midsld,endhost-1" range_in=x0-x0 range_out=a0-a0 payload_type= tls_client_hello)
lists summary:
blobs summary: blob 'fake_default_tls' : size=680 alloc=808 blob 'fake_default_http' : size=263 alloc=263 blob 'fake_default_quic' : size=620 alloc=620
initializing conntrack with timeouts tcp=60:300:60 udp=60 ipcache lifetime 7200s Running as UID=1 GID=1 initializing raw sockets bind-fix4=0 bind-fix6=0 set_socket_buffers fd=3 rcvbuf=2048 sndbuf=32768 fd=3 SO_RCVBUF=4096 fd=3 SO_SNDBUF=65536 set_socket_buffers fd=4 rcvbuf=2048 sndbuf=32768 fd=4 SO_RCVBUF=4096 fd=4 SO_SNDBUF=65536
LUA INIT LUA v5.1 LuaJIT 2.1.1756211046 OpenResty JIT: ON fold cse dce fwd dse narrow loop abc sink fuse LUA REMOVE: os.execute io.popen package.loadlib debug package.loaded.debug LUA BLOB: fake_default_tls (size=680) LUA BLOB: fake_default_http (size=263) LUA BLOB: fake_default_quic (size=620) LUA STR: NFQWS2_VER LUA NUMERIC: qnum desync_fwmark NFQWS2_COMPAT_VER VERDICT_PASS VERDICT_MODIFY VERDICT_DROP VERDICT_MASK VERDICT_PRESERVE_NEXT DEFAULT_MSS IP_BASE_LEN IP6_BASE_LEN TCP_BASE_LEN UDP_BASE_LEN ICMP_BASE_LEN TCP_KIND_END TCP_KIND_NOOP TCP_KIND_MSS TCP_KIND_SCALE TCP_KIND_SACK_PERM TCP_KIND_SACK TCP_KIND_TS TCP_KIND_MD5 TCP_KIND_AO TCP_KIND_FASTOPEN TH_FIN TH_SYN TH_RST TH_PUSH TH_ACK TH_FIN TH_URG TH_ECE TH_CWR IP_RF IP_DF IP_MF IP_OFFMASK IP_FLAGMASK IPTOS_ECN_MASK IPTOS_ECN_NOT_ECT IPTOS_ECN_ECT1 IPTOS_ECN_ECT0 IPTOS_ECN_CE IPTOS_DSCP_MASK IP6F_MORE_FRAG IPV6_FLOWLABEL_MASK IPV6_FLOWINFO_MASK IPPROTO_IP IPPROTO_IPIP IPPROTO_IPV6 IPPROTO_ICMP IPPROTO_TCP IPPROTO_UDP IPPROTO_ICMPV6 IPPROTO_SCTP IPPROTO_HOPOPTS IPPROTO_ROUTING IPPROTO_FRAGMENT IPPROTO_AH IPPROTO_ESP IPPROTO_DSTOPTS IPPROTO_MH IPPROTO_HIP IPPROTO_SHIM6 IPPROTO_NONE ICMP_ECHOREPLY ICMP_DEST_UNREACH ICMP_REDIRECT ICMP_ECHO ICMP_TIME_EXCEEDED ICMP_PARAMETERPROB ICMP_TIMESTAMP ICMP_TIMESTAMPREPLY ICMP_INFO_REQUEST ICMP_INFO_REPLY ICMP_UNREACH_NET ICMP_UNREACH_HOST ICMP_UNREACH_PROTOCOL ICMP_UNREACH_PORT ICMP_UNREACH_NEEDFRAG ICMP_UNREACH_SRCFAIL ICMP_UNREACH_NET_UNKNOWN ICMP_UNREACH_HOST_UNKNOWN ICMP_UNREACH_NET_PROHIB ICMP_UNREACH_HOST_PROHIB ICMP_UNREACH_TOSNET ICMP_UNREACH_TOSHOST ICMP_UNREACH_FILTER_PROHIB ICMP_UNREACH_HOST_PRECEDENCE ICMP_UNREACH_PRECEDENCE_CUTOFF ICMP_REDIRECT_NET ICMP_REDIRECT_HOST ICMP_REDIRECT_TOSNET ICMP_REDIRECT_TOSHOST ICMP_TIMXCEED_INTRANS ICMP_TIMXCEED_REASS ICMP6_ECHO_REQUEST ICMP6_ECHO_REPLY ICMP6_DST_UNREACH ICMP6_PACKET_TOO_BIG ICMP6_TIME_EXCEEDED ICMP6_PARAM_PROB MLD_LISTENER_QUERY MLD_LISTENER_REPORT MLD_LISTENER_REDUCTION ND_ROUTER_SOLICIT ND_ROUTER_ADVERT ND_NEIGHBOR_SOLICIT ND_NEIGHBOR_ADVERT ND_REDIRECT ICMP6_DST_UNREACH_NOROUTE ICMP6_DST_UNREACH_ADMIN ICMP6_DST_UNREACH_BEYONDSCOPE ICMP6_DST_UNREACH_ADDR ICMP6_DST_UNREACH_NOPORT ICMP6_TIME_EXCEED_TRANSIT ICMP6_TIME_EXCEED_REASSEMBLY ICMP6_PARAMPROB_HEADER ICMP6_PARAMPROB_NEXTHEADER ICMP6_PARAMPROB_OPTION LUA BOOL: b_debug b_daemon b_server b_ipcache_hostname b_ctrack_disable LUA RUN FILE: /opt/zapret2/lua/zapret-lib.lua LUA RUN FILE: /opt/zapret2/lua/zapret-antidpi.lua LUA RUN FILE: /opt/zapret2/lua/zapret-auto.lua LUA INIT DONE
opening nfq library handle unbinding existing nf_queue handler for AF_INET (if any) binding nfnetlink_queue as nf_queue handler for AF_INET unbinding existing nf_queue handler for AF_INET6 (if any) binding nfnetlink_queue as nf_queue handler for AF_INET6 binding this socket to queue '65302' setting copy_packet mode set receive buffer size to 1048576

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

**2026-04-10T22:18:03 | dirtybiker**
Натевам скольчо было. В секцию с авг распихайте. У меня с ними вроде вертит, но рисунки всё равно туго читает. 
91.108.4.0/22
91.108.8.0/22
91.108.16.0/22
91.108.12.0/22
149.154.160.0/20
91.105.192.0/23
91.108.20.0/22
185.76.151.0/24

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

---

**2026-04-11T23:06:11 | Routerich**
кокие ваши докозателства?
    "domains": [
        "cdn-telegram.org",
        "comments.app",
        "contest.com",
        "fragment.com",
        "graph.org",
        "quiz.directory",
        "t.me",
        "tdesktop.com",
        "telega.one",
        "telegra.ph",
        "telegram-cdn.org",
        "telegram.dog",
        "telegram.me",
        "telegram.org",
        "telegram.space",
        "telesco.pe",
        "tg.dev",
        "ton.org",
        "tx.me",
        "usercontent.dev"
    ],

---

**2026-04-19T15:01:54 | Георгий Новожилов**
стандарт хосты, присылали в чат

cdn-telegram.org
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

---

