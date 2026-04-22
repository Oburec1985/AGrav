# Raw Extraction: zeroblock

**2026-01-01T12:15:20 | ZЁма**
С Новым Годом!!!🍾
Подскажите почему периодически отключается WARP?
Подключается после перезагрузки интерфейса awg10.
РР 24.10.4 -> ZeroBlock -> Модем Vertell Cat.12 VT-STATION-X12 -> Оператор Т2

---

**2026-01-01T19:43:01 | Routerich**
● 🚀 ZeroBlock 0.5.0

  Мы запускаем второй этап бета-тестирования!

  ⚠️ Важно понимать:

  Устанавливая пакет, вы соглашаетесь с тем, что это бета-версия. Возможны ошибки, нестабильная работа или непредвиденное поведение.

  📋 Требования к участникам:

  Если вы решаетесь участвовать, при обнаружении проблем обязательно предоставьте:

  • Подробное описание проблемы
  • Последовательность действий, которые к ней привели
  • Скриншоты интерфейса
  • Логи (без приватных ключей и адресов серверов)
  • Диагностическую информацию

  🚫 Правила

  Сообщения формата «я тут жамкнул и всё полегло» и вопросы, которые покрывает инструкция будут безжалостно удаляться, а пользователь — наказываться.
Заметка
Для того чтобы Вам могли помочь нужны логи уровня debug(включаются внизу страницы настроек). Предоставьте лог файл после перезапуска zeroblock

---

**2026-01-01T22:35:23 | Антон**
ТехПО с НГ не томите в этом месяце будет ZeroBlock уж жду жду

---

**2026-01-02T12:23:28 | Routerich**
С новым годом 2026! Хотим поздравить вас, наши дорогие пользователи.

За 2025 год осуществлено множество важных решений для нашего устройства. Мы разработали анонимный удалённый доступ для всех маршрутизаторов на базе tailscale, а также расширили штат сотрудников службы поддержки — это одна из ключевых особенностей, отличающих нас от конкурентов.

Мы столкнулись с тем, что некоторые лица пытаются установить нашу прошивку и получить техническую поддержку без надлежащей авторизации. С 2026 года мы начнём активную работу в этом направлении, чтобы обеспечить вам быстрые и качественные ответы на ваши вопросы.

Дополнительно обновлён дизайн упаковки; в 2026 году планируем завершить обновление самого корпуса роутера. По состоянию на настоящий момент работа над BE7200 идёт в позитивном ключе, однако требуется дополнительное время на доводку для обеспечения наилучшей стабильности.

Мы приобрели оборудование не только для прошивки и сборки роутеров в РФ, но и для упаковки в термо-пленку, что дополнительно защитит ваши посылки.

Планы на 2026 год

Выпуск релиза ZeroBlock: система будет функционировать автономно, настраиваться без скриптов, мониторить работоспособность и, при необходимости, восстанавливать настройки с сервера.

Введение мастера настроек: пошаговая настройка для более удобного использования.

Модуль диагностики и чат-бот: вы сможете отправлять файлы в специальный раздел чата Telegram, и бот будет анализировать их и сообщать об ошибках.

MESH: решены проблемы взаимодействия главного маршрутизатора с точками доступа, обновление по требованию и получение информации с точек доступа. Было выявлено существенное ограничение в OpenWrt: передача WED по Mesh уменьшала скорость. Работаем над устранением этой проблемы — она будет учтена в ближайшей прошивке.

А так же многое другое.. 
Благодарим каждого из вас за поддержку 
Вместе мы станем лучше ваш RR

---

**2026-01-03T22:28:13 | Антон**
Cил и терпения больше нет охота уже опробовать совместно с ZeroBlock

---

**2026-01-07T16:40:57 | Алексей**
А zeroblock если ставить, его поверх скрипта нужно или можно сразу поставить?

---

**2026-01-07T16:41:45 | Anna Bagler**
Zeroblock без скрипта 5 или подкоп отключайте.

---

**2026-01-08T19:23:30 | ZЁма**
Такой пакет установлен, но обновления не требует. АСУ делал когда стоял ZeroBlock. Там после обновления собранной прошивки тема тёмная сразу появилась.

---

**2026-01-09T20:25:30 | Routerich**
Пост выше обязателен к прочтению! выше микро мануал
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
#ZeroBlock

---

**2026-01-09T20:42:50 | Routerich**
Сперва устанавливаем zeroblock, а только потом luci-app-zeroblock

---

**2026-01-09T20:43:48 | Routerich**
Предварительно обновите список пакетов, потом устанавливайте zeroblock

---

**2026-01-09T21:27:05 | Slesh**
Наступает ночь, просыпаются тестеры? ) Тоже поставил ручками sing box, выдавало 255, скинул еще раз, обновил списки и поставил сразу zeroblock, он подтянул sing-box, потом поставил LuCi

---

**2026-01-09T21:29:22 | Routerich**
opkg update && opkg install --cache /tmp /tmp/zeroblock_0.5.0-r103_aarch64_cortex-a53.ipk

---

**2026-01-10T02:26:30 | Wenzel Perminov**
минут через 20 отлетает, в логах за этот период пусто, если перезапустить ZeroBlock все заработает

---

**2026-01-10T04:53:55 | Wenzel Perminov**
все работало, я стартанул zeroblock (лог с этого момента) проверил, все работает, через 5 минут еще одна проверка уже браузеры не открывают ругаются на днс, я остановил и все заработало

---

**2026-01-10T08:51:34 | Wenzel Perminov**
yacd непонятно как лог достать. Лог zeroblock может не информативен этот. В воскресенье вечером смогу только сделать новый

---

**2026-01-10T12:27:44 | Aleksandr**
Попробовал. Снова прошил роутер и заново установил Zeroblock) и сразу как все понятно стало) спасибо.

---

**2026-01-10T20:31:23 | Yar**
какой бы я порт ни поставил, в логах всегда присутствует запись, что порт используется

Sat Jan 10 20:30:05 2026 daemon.warn zeroblock[16676]: [singbox_gen    ] Section netherlands: mixed port 2081 is already in use by another application, skipping

---

**2026-01-10T20:37:20 | Yar**
root@RouteRich:~# netstat -tulnp | grep 2081
root@RouteRich:~# cat "/etc/config/zeroblock" | grep mixed_port
        option mixed_port '2081'
        option mixed_port '3080'
        option mixed_port '4080'
        option mixed_port '6080'
        option mixed_port '5080'
root@RouteRich:~#

---

**2026-01-10T21:45:26 | Routerich**
где логи, у меня не воспроизводится
root@RouteRich:~# netstat -tulpn |grep 208
netstat: showing only processes with your user ID
tcp        0      0 0.0.0.0:2081            0.0.0.0:*               LISTEN      14471/sing-box
tcp        0      0 0.0.0.0:2080            0.0.0.0:*               LISTEN      14471/sing-box
root@RouteRich:~# cat "/etc/config/zeroblock" | grep mixed_port
        option mixed_port '2080'
        option mixed_port '2081'

---

**2026-01-10T22:57:13 | Писарев Андрей**
Добрый вечер!
Подкоп не поддерживает IPv6, а как дела с этим у ZeroBlock?
Если нет, то планируется ли поддержка?

---

**2026-01-11T13:56:54 | Gomer Simpson**
Очевидно, у нас с @YurAn72 ситуация идентична. Снёс ZeroBlock, после нескольких отвалов интернета и перезапусков всех интерфейсов.

---

**2026-01-11T14:29:46 | Юрий**
# ZeroBlock BadWAN Monitor
*/10 * * * * /usr/bin/zeroblock badwan_check >/dev/null 2>&1

# ZeroBlock Lists Update
13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1
root@RouteRich:~#

---

**2026-01-11T14:33:02 | Routerich**
где?
Sun Jan 11 13:20:08 2026 cron.err crond[9483]: crond (busybox 1.36.1) started, log level 5
Sun Jan 11 13:20:09 2026 daemon.debug zeroblock[9296]: bash_executor_run_timeout: exit code 0
Sun Jan 11 13:20:09 2026 daemon.info zeroblock[9296]: [cron_manager   ] BadWAN monitor cron job installed: */10 * * * * /usr/bin/zeroblock badwan_check
Sun Jan 11 13:20:09 2026 daemon.info zeroblock[9296]: [config_builder ] Configuration applied successfully
Sun Jan 11 13:20:09 2026 daemon.info zeroblock[9296]: ZeroBlock started successfully
Sun Jan 11 13:20:09 2026 daemon.info zeroblock[9296]: [cron_manager   ] ZeroBlock cron job not found
Sun Jan 11 13:20:09 2026 daemon.info zeroblock[9296]: Installing lists update cron job: 1d
Sun Jan 11 13:20:09 2026 daemon.debug zeroblock[9296]: bash_executor_run_timeout: executing with timeout 10 seconds
Sun Jan 11 13:20:09 2026 cron.err crond[9540]: crond (busybox 1.36.1) started, log level 5
Sun Jan 11 13:20:09 2026 daemon.debug zeroblock[9296]: bash_executor_run_timeout: exit code 0
Sun Jan 11 13:20:09 2026 daemon.info zeroblock[9296]: [cron_manager   ] Lists update cron job installed: 13 9 * * * /usr/bin/zeroblock update_lists
Sun Jan 11 13:20:09 2026 daemon.info zeroblock[9296]: Lists update cron job installed successfully

---

**2026-01-11T16:16:17 | Архипов Кирилл Александрович**
Вопрос к РР: обнаружил, что при белых списках синг бокс из подкопа не запускается при включённых списках сообщества. Т.к. нет доступа к гиту, соответственно их подгрузка отваливается.
Вопрос: можно ли в ZeroBlock указать свои списки? 

Спустя столько времени еще не дошёл до его тестирования😅

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

**2026-01-11T19:11:55 | Matvey**
ладно, спасибо. еще повожусь, в крайнем случае в ZeroBlock закину)

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

**2026-01-12T12:01:44 | Ilya Gorbunov**
да её информативность конечно такая себе
Upgrading luci-app-zeroblock on root from 0.5.0-r133 to 0.5.0-r141...
Collected errors:
 * wfopen: ./luci-app-zeroblock_0.5.0-r141_all.ipk: No such file or directory.
 * pkg_get_installed_files: Error extracting file list from ./luci-app-zeroblock_0.5.0-r141_all.ipk.
 * opkg_install_cmd: Cannot install package luci-app-zeroblock.

---

**2026-01-12T15:24:03 | Routerich**
https://t.me/routerich/394153/432059
  ZeroBlock v0.5.0-r143

  - Исправлен запуск после reboot — правила NFTables теперь применяются корректно
  - Исправлена ошибка "unknown transport type: raw"
  - Dashboard показывает тип транспорта (ws/grpc/h2)
#ZeroBlock

---

**2026-01-12T18:52:50 | Mallory**
Mon Jan 12 18:50:14 2026 daemon.debug zeroblock[8504]: bash_executor_run_timeout: executing with timeout 5 seconds
Mon Jan 12 18:50:14 2026 daemon.debug zeroblock[8504]: bash_executor_run_timeout: exit code 0
Mon Jan 12 18:50:16 2026 daemon.err zeroblock[8375]: [config_builder ] Sing-box failed to start within timeout
Mon Jan 12 18:50:16 2026 daemon.err zeroblock[8375]: Failed to start ZeroBlock
Mon Jan 12 18:50:16 2026 daemon.debug zeroblock[8521]: bash_executor_run_timeout: executing with timeout 5 seconds
Mon Jan 12 18:50:16 2026 daemon.debug zeroblock[8521]: bash_executor_run_timeout: exit code 0

После обновления на 143 (с какой-то версии типа 140), перестал стартовать sing-box

---

**2026-01-12T22:48:38 | Routerich**
https://t.me/routerich/394153/432059
  ZeroBlock v0.5.0-r148
  - Исправлена проблема отображения логов и конфига
если всё ещё не будет работать, то 
rm -rf /tmp/luci-* && /etc/init.d/rpcd reload
#ZeroBlock

---

**2026-01-12T23:48:11 | Routerich**
https://t.me/routerich/394153/432059
  ZeroBlock v0.5.0-r149
  - Убран отладочный вывод bash_executor_run_timeout
  - Добавлен вывод типа транспорта в подписке/url/url_test
#ZeroBlock

---

**2026-01-13T03:08:13 | Routerich**
Podkop последний поддерживает, Zeroblock поддерживает

---

**2026-01-13T11:33:19 | Routerich**
вопросы есть?
Tue Jan 13 11:27:47 2026 daemon.warn zeroblock[3613]: [proxy_parser   ] Unsupported transport type 'xhttp', falling back to tcp

---

**2026-01-13T12:58:51 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock v0.5.0-r150
  - Исправлена обработка комментариев в пользовательских списках(теперь через #)
  - Реализовано дробление конфига для sing-box и расположение в /tmp/zeroblock/conf.d
  - Убран бесполезный popup о запуске/остановке/ошибке
  - В дашборде теперь отображается тип vpn интерфейса
#ZeroBlock 
если всё ещё не будет работать, то 
rm -rf /tmp/luci-* && /etc/init.d/rpcd reload
и по классике очистить кеш арбузера(браузера)

---

**2026-01-13T13:50:27 | Bullet for my valentine Poison**
как накатил сверху пакет и выполнил доп. команду. Еще несколько раз перезапустил и оно завелось. Сейчас еще словил ошибку при изменении порога пинга в подписках(300), при попытке сохранить и применить.
Tue Jan 13 13:43:24 2026 daemon.warn odhcpd[2976]: No default route present, setting ra_lifetime to 0!
Tue Jan 13 13:43:29 2026 daemon.warn zeroblock[25386]: bash_executor_run_timeout: script killed by timeout
Tue Jan 13 13:43:29 2026 daemon.warn zeroblock[25389]: bash_executor_run_timeout: script killed by timeout
Tue Jan 13 13:43:29 2026 daemon.notice hostapd: nl80211: nl80211_recv_beacons->nl_recvmsgs failed: -5
Tue Jan 13 13:44:20 2026 daemon.warn zeroblock[25482]: bash_executor_run_timeout: script killed by timeout
Tue Jan 13 13:44:20 2026 daemon.warn zeroblock[25481]: bash_executor_run_timeout: script killed by timeout
Tue Jan 13 13:44:20 2026 daemon.notice hostapd: nl80211: nl80211_recv_beacons->nl_recvmsgs failed: -5
Tue Jan 13 13:45:07 2026 daemon.notice hostapd: nl80211: nl80211_recv_beacons->nl_recvmsgs failed: -5
Tue Jan 13 13:50:02 2026 daemon.warn odhcpd[2976]: No default route present, setting ra_lifetime to 0!

---

**2026-01-13T14:06:38 | Wenzel Perminov**
еще нашел, пока zeroblock включен  opkg update не проходит

---

**2026-01-13T14:28:21 | Арсений Спиридонов**
С ZeroBlock это никак не связано, у вас opkg достучаться не может 
Попробуйте ping -с 1 downloads.openwrt.org сделать, там понятно будет, с сетью проблема или самим opkg

---

**2026-01-13T14:57:04 | Routerich**
Решение по доступу к доменам из списков h.o.d.c.a или cloudflare! 
Вариант 1:
Добавлять их в секцию awg10(если она жива) и выключать fakeip для этой секции, тогда домены резолвятся напрямую и работают через awg10 туннель. 
Вариант 2:
Включить в настройках zeroblock "Проксировать трафик роутера", тогда роутер будет так же работать по спискам секций.
Я постараюсь подумать над обходным решением, чтобы эти списки можно было использовать в других секциях.

---

**2026-01-13T17:03:37 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock v0.5.0-r152
  - Исправлен парсинг подписок в url_test
  - Исправлена ошибка Batch syntax check failed при создании nft правил
#ZeroBlock

---

**2026-01-13T18:43:16 | Routerich**
это связано с fakeip, т.е. c zeroblock

---

**2026-01-13T19:16:13 | Routerich**
да, зероблок создаёт директории и конфиги в /tmp/zeroblock/conf.d и кормит ими сингбокс. файл в etc будет всегда, потому что его тащит сам сингбокс, не вижу смысла удалять его

---

**2026-01-13T20:23:48 | Yar**
Необычное поведение в последних паре версий. Создается громадное количество соединений, от чего большая нагрузка н процессор и память утекает... 
И конфиг в диагностике выглядит неполностью
top | grep sing-box
17500     1 root     S    1229m 524%  43% sing-box run -C /tmp/zeroblock/conf.d
17500     1 root     S    1229m 524%  54% sing-box run -C /tmp/zeroblock/conf.d
17500     1 root     S    1229m 524%  53% sing-box run -C /tmp/zeroblock/conf.d
17500     1 root     S    1229m 524%  49% sing-box run -C /tmp/zeroblock/conf.d
17500     1 root     S    1229m 524%  56% sing-box run -C /tmp/zeroblock/conf.d

---

**2026-01-14T11:10:35 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock v0.5.0-r159
  - Исправлена петля трафика tproxy-tproxy
  - FakeIP выключен по умолчанию для VPN секций(как решение работы opkg, если в списках есть github и производные), включен для Proxy(если в прокси будет github, то сломается opkg)
подробнее о последнем https://t.me/routerich/394153/438385
#ZeroBlock

---

**2026-01-14T13:01:32 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock v0.5.0-r160
  - Исправлено определение работы tproxy в диагностике
  - Исправлен парсинг списков во многих местах
#ZeroBlock

---

**2026-01-14T17:02:52 | Bullet for my valentine Poison**
Так, пока отходил от компа Зероблок решил откинуться.
Wed Jan 14 14:39:26 2026 daemon.info zeroblock[8746]: Installing lists update cron job: 1d
Wed Jan 14 14:39:26 2026 daemon.info zeroblock[8746]: [cron_manager   ] Lists update cron job installed: 13 9 * * * /usr/bin/zeroblock update_lists
Wed Jan 14 14:39:26 2026 daemon.info zeroblock[8746]: Lists update cron job installed successfully
Wed Jan 14 16:50:34 2026 kern.warn kernel: [19564.135666] sing-box invoked oom-killer: gfp_mask=0x140cca(GFP_HIGHUSER_MOVABLE|__GFP_COMP), order=0, oom_score_adj=0
Wed Jan 14 16:50:34 2026 kern.debug kernel: [19564.146303] CPU: 1 PID: 8807 Comm: sing-box Tainted: G           O       6.6.110 #0
Wed Jan 14 16:50:34 2026 kern.info kernel: [19564.739428] [   8800]     0  8800   315097    14652   258048        0             0 sing-box
Wed Jan 14 16:50:34 2026 kern.info kernel: [19564.808096] oom-kill:constraint=CONSTRAINT_NONE,nodemask=(null),cpuset=/,mems_allowed=0,global_oom,task_memcg=/,task=sing-box,pid=8800,uid=0
Wed Jan 14 16:50:34 2026 kern.err kernel: [19564.820913] Out of memory: Killed process 8800 (sing-box) total-vm:1260388kB, anon-rss:58608kB, file-rss:0kB, shmem-rss:0kB, UID:0 pgtables:252kB oom_score_adj:0
В итоге, вся морда поломалась и зависла. Отрубил конфиг с влессом.

---

**2026-01-14T18:29:33 | Routerich**
Проблема в подкопе, сейчас есть баг, если есть warp(awg10) в одной из секции, и ты добавляешь в другую секцию список cloudflare, то получается петля и warp перестаёт работать, следовательно и ютуб в этой секции. Можете установить zeroblock, в теме zeroblock всё описано, там нет этого бага

---

**2026-01-14T20:28:13 | Routerich**
Посмотрите на тему Zeroblock, там есть подписки и многое другое

---

**2026-01-14T22:24:38 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock v0.5.0-r162
  - Доработан dashboard:
  - Теперь для subscription с urltest показывается только:
  - Группа "Auto"
  - Текущий активный прокси (now)
  - Для selector - все прокси (для выбора).

  - Добавлена обработка неподдерживаемых сингбоксом типов транспортов для подписки, теперь он не падает, а игнорирует неподдерживаемую ссылку из подписки
  - Добавлено кеширование подписок в /etc/sing-box/subscriptions/ с fallback при ошибках сети
  - Исправлена ошибка reality подписок: добавлен дефолтный fingerprint "chrome" если не указан в URL
  - DNS правила переведены на новый формат с "action": "route"
  - Убран устаревший block outbound, заменён на "action": "reject" в правилах маршрутизации
#ZeroBlock

---

**2026-01-14T22:38:59 | Routerich**
промотал вверх за вас, не благодарите
v0.5.0-r150
  - Исправлена обработка комментариев в пользовательских списках(теперь через #)
  - Реализовано дробление конфига для sing-box и расположение в /tmp/zeroblock/conf.d
  - Убран бесполезный popup о запуске/остановке/ошибке
  - В дашборде теперь отображается тип vpn интерфейса

---

**2026-01-14T22:42:56 | Routerich**
logread | grep -i "unsupported\|skipping"
Wed Jan 14 20:17:35 2026 daemon.info zeroblock[14400]: AWG already configured (peer=162.159.192.4), skipping auto-install
Wed Jan 14 20:17:35 2026 daemon.info zeroblock[14400]: Opera Proxy already installed, skipping
Wed Jan 14 21:48:08 2026 daemon.info zeroblock[19087]: AWG already configured (peer=162.159.192.4), skipping auto-install
Wed Jan 14 21:48:08 2026 daemon.info zeroblock[19087]: Opera Proxy already installed, skipping
Wed Jan 14 21:48:11 2026 daemon.warn zeroblock[19087]: [proxy_parser   ] Skipping huy-79: reality requires public_key
Wed Jan 14 21:48:11 2026 daemon.warn zeroblock[19087]: [proxy_parser   ] Skipping huy-88: reality requires public_key
Wed Jan 14 22:39:59 2026 daemon.info zeroblock[28480]: AWG already configured (peer=162.159.192.4), skipping auto-install
Wed Jan 14 22:39:59 2026 daemon.info zeroblock[28480]: Opera Proxy already installed, skipping
Wed Jan 14 22:40:02 2026 daemon.warn zeroblock[28480]: [proxy_parser   ] Skipping huy-79: reality requires public_key
Wed Jan 14 22:40:02 2026 daemon.warn zeroblock[28480]: [proxy_parser   ] Skipping huy-88: reality requires public_key

---

**2026-01-14T22:46:57 | Den**
Не устанавливается luci-app-zeroblock_0.5.0-r162_all.ipk В чем трабл, подскажите пожалста?

---

**2026-01-14T23:27:02 | Юрий**
opkg list | grep luci-app-zeroblock*

---

**2026-01-15T09:24:11 | Роман**
Всем доброго утра! Скажите пожалуйста, ZeroBlock сейчас работает стабильнее или лучше чем все имеющиеся скрипты?

---

**2026-01-15T09:30:10 | Routerich**
возможно будет чисто скрипт, который будет устанавливать пакеты zeroblock.

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

**2026-01-17T02:17:15 | None**
Всем доброй ночи! Я правильно понимаю, что в будущем все блокировки ресурсов будут обходиться через Zeroblock? 5 скрипт у меня совсем перестал работать.

---

**2026-01-17T02:17:51 | None**
что можете сказать по поводу Zeroblock? Отрабатывает свой функционал?

---

**2026-01-17T12:29:21 | None**
А что такое  zeroblock?

---

**2026-01-17T18:03:16 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r30:
  - Добавлен чекбокс "Скрыть недоступные"(работает только для подписок) на панели управления(включен по умолчанию)
  - Исправлено переключение серверов в панели управления(для подписок)
  - Исправлена работа DNS Hijack ломавшая доступ к роутеру по имени
#ZeroBlock

---

**2026-01-18T11:56:06 | Routerich**
расширяйте системный журнал до 1280кб, ставьте zeroblock и singbox в trace и присылайте логи, раз вы считаете что что-то работает неправильно

---

**2026-01-18T13:29:45 | Григорий**
что такое ZeroBlock?

---

**2026-01-18T14:19:16 | Routerich**
я использую zeroblock+zapret2 на постоянной основе и сам нахожу глубокие косяки в правилах nft, остальное находят пользователи по примеру вашего фидбека о селекторе или кастомного path в днс. и могу сказать что связка работает стабильно

---

**2026-01-18T17:08:19 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r35:
  - Добавлен чекбокс в "настройки - Дополнительные" Исключить BitTorrent(по умолчанию включена)
  - Добавлено поле в секции "Исключённые Source IP"(в следующих билдах переименую на человеческий)
  - Исправлено добавление кастомного dns server в vpn секцию с правильным парсингом /path
#ZeroBlock

---

**2026-01-18T23:40:22 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r40:
  - Изменена логика опции "Исключить BitTorrent", теперь она создаёт отдельный outbound и пытается сделать offload силами nftables(Попытка избежать торрент нагрузки при отключенном fakeip)
Да, первые пакеты всё-равно попадут в tproxy, но на продолжительных раздачах это должно сказаться. Нужна обратная связь, возможно таймаут слишком мал(30 сек)
#ZeroBlock

---

**2026-01-19T18:17:58 | Routerich**
поставьте логирование в strace отключите логирование sing-box примените, остановите зероблок , откройте новую вкладку  c терминалом выполните logread -f |grep zeroblock , запустите зероблок и скиньте всю простыню

---

**2026-01-19T18:28:00 | Routerich**
ссзб это называется "Не изменять DHCP" выключите
Mon Jan 19 18:20:07 2026 daemon.info zeroblock[14151]: [config_builder ] DNS configuration DISABLED (enable_dns_configuration=0)

---

**2026-01-19T18:45:03 | Routerich**
zeroblock check_fakeip

---

**2026-01-19T18:51:16 | Routerich**
Впн свой или покупной? Если свой то в настройках панели исключения для торрент трафика сделать, Если покупной то попросить продавца сделать это, либо установить Zeroblock и там исключения сделать

---

**2026-01-19T18:55:46 | Игорь**
А почему, когда запущен ZeroBlock , в подкопе пишет что он запущен, при этом я подкоп отключил перед установкой зеро

---

**2026-01-19T19:16:39 | Atomm**
Покупной, что за Zeroblock?

---

**2026-01-19T19:18:27 | Routerich**
Тема Zeroblock BETA, аналог подкопа с большим функционалом

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

**2026-01-20T09:17:35 | Navisal**
не обновляются списки. напрямую или через секцию. браузером доступ к спискам есть
root@RouteRich:~# zeroblock update_lists
{"status":"updating","message":"Starting lists update..."}
{"status":"updating","message":"Checking DNS availability..."}
{"status":"updating","message":"DNS check passed"}
{"status":"updating","message":"Checking GitHub connectivity..."}
{"status":"updating","message":"GitHub unavailable [10/30]..."}
{"status":"updating","message":"GitHub unavailable [20/30]..."}
{"status":"updating","message":"GitHub unavailable [30/30]..."}
{"status":"error","message":"GitHub check failed after 30 attempts"}

---

**2026-01-20T09:54:42 | Routerich**
nslookup github.com
и 
curl -v https://github.com
плюсом переведите лог в strace, перезапустите zeroblock и дайте системный журнал полностью

---

**2026-01-20T10:10:15 | Routerich**
Здравствуйте.
v2raya, zeroblock (https://t.me/routerich/394153)

---

**2026-01-20T10:30:28 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r55:
  - Увеличен размер лога до 500 строк в диагностике
  - Увеличен лимит подписок до 500
  - Увеличен размер ожидаемого ответа для списков 
  - Увеличен таймер тестирования задержки для большого количества ссылок в одной подписке
  - Добавлена обработка и отображение неподдерживаемых транспортов для подписки и url_test. неподдерживаемое пропускается, в дашборд пишется сколько из скольки работает, в лог пишется что не поддерживается
  - Добавлена обработка для транспорта SS, если конфиг считается невалидным, пропускается
  - Убрана ошибочная конвертация xhttp в tcp
Раз читать мы не умеем, значит будем скрывать ссылки из лога и сами гадайте где проблема
  - Добавлено отсечение полного URL подписки в логе
Обновлен manual для страждущих, которые не следят или только вкатились в тест
#ZeroBlock

---

**2026-01-20T21:20:30 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r58:
  - Удалены параметры `subscription_selector` и `urltest_selector`
  - Добавлен булевый флаг `single_proxy` (true = только первый прокси, без wrapper)
  - По-умолчанию создаётся wrapper (selector + urltest) для автовыбора
  - Автоматическое обновление данных после запуска sing-box
  - Увеличен таймаут теста задержки группы до 30 секунд
  - Пропуск прокси с неподдерживаемым транспортом
  - Исправлено предупреждение о локальном маршруте
  - Скрытие proxy URL в логах
  - Увеличен лимит HTTP ответа до 2MB
  - Добавлена валидация Shadowsocks: диапазон портов, символы метода
  - Увеличен буфер до 64KB
  - Отображение количества пропущенных неподдерживаемых прокси в dashboard
#ZeroBlock

---

**2026-01-20T21:34:46 | Routerich**
покажи
cat /etc/config/zeroblock

---

**2026-01-20T21:41:37 | Routerich**
uci set zeroblock.settings.log_level='trace'
uci commit
service zeroblock restart
cat /etc/config/zeroblock

---

**2026-01-20T22:21:54 | Routerich**
Zeroblock поставить

---

**2026-01-20T23:00:56 | Den**
Подскажите, если обновить прошивку (пакеты) через ASU, слетит ли zeroblock и все его настройки?

---

**2026-01-20T23:50:07 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r59:
  - Быстрофикс luci-app. в некоторых случаях ломался дашборд
Если работает, обновление необязательно
#ZeroBlock

---

**2026-01-21T11:26:48 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r66:
  - Устранены найденные проблемы которые могли привести к зависаниям luci в некоторых ситуациях
  - Дополнен список зависимостей
  - Удалён перевод для уровней логирования
  - Исправлена проблема дублирования плитки в дашборде
#ZeroBlock

---

**2026-01-21T12:22:54 | Юрий (◕‿◕)**
Zeroblock грузится а Luci выдает ошибку

---

**2026-01-21T13:41:13 | Routerich**
Будет zeroblock, который сам будет все делать и следить за всем.

---

**2026-01-21T15:24:51 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r70:
  - Маскировка secret, server, uuid, server_name, public_key, password, private_key, short_id в диагностике по кнопке "Показать конфиг"
  - Исправлена версия в бинарнике
#ZeroBlock

---

**2026-01-21T15:56:15 | Routerich**
Установите Zeroblock из темы Zeroblock beta. Там есть список исключений для каждой секции

---

**2026-01-21T15:59:20 | Михаил**
А с zapret дружит zeroblock?

---

**2026-01-21T17:26:00 | isinva**
хрен с ним с тейлом, zeroblock добивайте

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

**2026-01-21T17:58:16 | Михаил**
Он генерится сервисами в инете, но в случае с ZeroBlock все само делается, нужно просто галочку тыкнуть)

---

**2026-01-21T18:02:29 | Роман**
а что за zeroblock такой на owrt? не могу про него ничего нагуглить...

---

**2026-01-21T18:11:33 | Anna Bagler**
Zeroblock вместо подкопа должен быть.

---

**2026-01-22T00:01:27 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r71:
  - Исправлен парсинг plain text листов для "Внешние списки доменов" и "Внешние списки подсетей"
#ZeroBlock

---

**2026-01-22T00:16:29 | Den**
что значит ошибка 2026 daemon.err zeroblock[15049]

---

**2026-01-22T13:11:24 | Павел**
После установки zeroblock  ошибка при обновлении пакетов, перезагрузка роутера, перезапуск zeroblock не помогают. После полной остановки zeroblock ошибка уходит.

---

**2026-01-22T13:24:11 | Панда**
Ну допустим, мне нужно свое вкинуть перед/после загрузкой конфигов которые создал zb, просто zb запускает сингбокс через чтение конфига из категории /tmp/zeroblock

То есть только перед запуском ему вкинуть туда можно.

---

**2026-01-22T14:14:58 | Routerich**
скриптов не будет, будет только zeroblock

---

**2026-01-22T14:33:26 | Алексей Пумпур**
Ясно,значит надо zeroblock осваивать😀,пробовал установить,но чт то не пошло

---

**2026-01-23T00:47:19 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r77:
  - Полная переработка выключенного fakeip. теперь трафик не из листов и подсетей не попадает в tproxy. Exclude Bittorrent оставлен как рудимент на всякий случай
  - Исправлена очередность nft правил
#ZeroBlock

---

**2026-01-23T06:12:40 | Routerich**
поздравляю, zeroblock запущен. а причем тут Ютуб?

---

**2026-01-23T23:12:18 | Routerich**
немножко инсайдерских сливов
Fri Jan 23 23:11:09 2026 daemon.info zeroblock[30766]: [proxy_parser   ] Parsed VLESS: host=91.84.103.111 port=443 uuid=166aa5c1... security=reality transport=xhttp
Fri Jan 23 23:11:09 2026 daemon.info zeroblock[30766]: [proxy_parser   ] Parsed VLESS: host=V2ngFast.huqpmfood.ir port=1146 uuid=1cd99383... security=reality transport=xhttp
Fri Jan 23 23:11:09 2026 daemon.info zeroblock[30766]: [proxy_parser   ] Parsed VLESS: host=s.pou-ria.com port=80 uuid=1f1096d3... security= transport=xhttp
Fri Jan 23 23:11:09 2026 daemon.info zeroblock[30766]: [proxy_parser   ] Parsed VLESS: host=151.101.25.242 port=80 uuid=240026c6... security= transport=xhttp
Fri Jan 23 23:11:09 2026 daemon.info zeroblock[30766]: [proxy_parser   ] Parsed VLESS: host=V2ngFast.huqpmfood.ir port=1146 uuid=268be772... security=reality transport=xhttp
Fri Jan 23 23:11:09 2026 daemon.info zeroblock[30766]: [proxy_parser   ] Parsed VLESS: host=trt.fastlynew.hosting-ip.com port=80 uuid=29267952... security= transport=xhttp
Fri Jan 23 23:11:09 2026 daemon.info zeroblock[30766]: [proxy_parser   ] Parsed VLESS: host=151.101.25.242 port=80 uuid=2a509678... security=none transport=xhttp
Fri Jan 23 23:11:09 2026 daemon.info zeroblock[30766]: [proxy_parser   ] Parsed VLESS: host=104.16.1.106 port=8080 uuid=2ad3d767... security= transport=xhttp
Fri Jan 23 23:11:09 2026 daemon.info zeroblock[30766]: [proxy_parser   ] Parsed VLESS: host=frx.fastdbn.com port=443 uuid=2ce48b7b... security=reality transport=xhttp
Fri Jan 23 23:11:09 2026 daemon.info zeroblock[30766]: [proxy_parser   ] Parsed VLESS: host=25.129.199.12 port=2052 uuid=3-JKVPN-... security=none transport=xhttp
Fri Jan 23 23:11:09 2026 daemon.info zeroblock[30766]: [proxy_parser   ] Parsed VLESS: host=146.75.119.82 port=80 uuid=31a097a5... security=none transport=xhttp
Fri Jan 23 23:11:09 2026 daemon.info zeroblock[30766]: [proxy_parser   ] Parsed VLESS: host=test.fast.hosting-ip.com port=80 uuid=31c17e80... security=none transport=xhttp

---

**2026-01-24T03:03:40 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r81:
 Xray-core интеграция:
  - Xray устанавливается так же как opera-proxy через автонастройку
  - Полная поддержка транспортов xhttp и kcp через SOCKS5-мост
  - Поддержка raw xray outbound JSON — можно вставить готовый конфиг xray напрямую
  — Автоматическое определение xray-транспортов в подписках
 Исправления парсеров:
  — VMess: пустое/невалидное поле network теперь корректно обрабатывается как tcp
 Subscription: 
  - Исправлена валидация obfs
  - Исправлен бесконечный цикл дедупликации тегов при длинных именах прокси (>192 байт) из подписки.
 LuCI:
  — "Сохранить и Применить" больше не перезапускает сервис (применяйте через Restart на дашборде)
#ZeroBlock

---

**2026-01-24T12:54:55 | Yury Kuzmenko**
zeroblock[7276]: [lists_loader   ] Section awg10: failed to convert domain txt to srs: https://raw.githubusercontent.com/itdoginfo/allow-

---

**2026-01-24T13:08:55 | Routerich**
cat /etc/config/zeroblock пришлите вывод

---

**2026-01-24T16:05:41 | Routerich**
потому что в6 трафик не проходит через zeroblock и singbox

---

**2026-01-24T16:06:56 | Routerich**
предположу что спешите и коннекты устанавливаются при перезапуске zeroblock далее contrack отправляет их мимо singbox

---

**2026-01-24T20:31:00 | Kiss_My_Axe**
Лучше ZeroBlock.
Хотя бы текушчую в репку засунуть.

---

**2026-01-24T20:52:56 | Routerich**
если у кого-то проблемы с роблоксом через zeroblock, отключите исключение bittorent, в следующем билде исправлено будет

---

**2026-01-25T02:55:06 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r90:
  - Сохранение cache/rulesets при stop:
  1. Без повторного скачивания — sing-box не перекачивает remote rule-sets (geoip, geosite, community lists) при каждом restart. Экономия времени и трафика.
  2. Быстрый старт — sing-box стартует быстрее, т.к. файлы .srs уже на диске.
  3. Работа при отсутствии интернета — если restart происходит когда нет связи (например, переключение WAN), списки уже есть локально.

  - BT exclude правило — перемещено после section rules (пользовательские IP приоритетнее)
  - Переработано окно показа логов(zeroblock - всегда, sing-box/xray в зависимости от настройки - по-умолчанию выключены)
#ZeroBlock

---

**2026-01-25T14:05:52 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r91:
  Переписана функция http_download_file() с поддержкой условного скачивания:
  - При повторном запуске отправляется заголовок If-Modified-Since с датой модификации файла
  - Если файл не изменился (HTTP 304), скачивание пропускается
  - Время модификации файла устанавливается из заголовка Last-Modified
  - Результат: значительное ускорение перезапуска zeroblock

  Исправления:
  - Добавлена генерация dnsmasq nftset конфигов для user_domains_text
  - Добавлено создание nft set и правил маркировки в mangle/mangle_output
  - Добавлена очистка xray при ошибках в config_apply
#ZeroBlock

---

**2026-01-25T16:25:08 | Kiss_My_Axe**
Это сообщение написано с выключенным ZeroBlock, то есть напрямую.

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

**2026-01-25T21:19:02 | Максим Росошанский**
Подкоп насыпал ошибок загрузки листов, с чем это может быть связано? И глобально - чем сейчас лучше пользоваться? Прошивка давно обновлялась? Что стабильнее - скрипт или zeroblock?

---

**2026-01-26T08:12:51 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r103:
  - Отслеживание загрузки списков: красный если все упали, жёлтый если частично
  - Обрезка имён прокси в Dashboard до 40 символов
#ZeroBlock

---

**2026-01-26T09:10:43 | Сергей**
Добрый день, до заводского состояния снес роутер и установил ZeroBlock, поставил галочки , перезагрузил роутер но Xray так и не устанавливается , я что-то не так делаю ?

---

**2026-01-26T10:47:55 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r105:
  - raw transport: теперь парсится корректно
  - chacha20-poly1305 → chacha20-ietf-poly1305 для Shadowsocks
  - Добавлена проверка Xray в диагностику Services(если запущен, показывает сколько прокси)
  - Убран двойной скролл в модальном окне конфига
  - Буфер логов: 64KB → 128KB. Количество строк: 500 → 1000
  - Фильтрация мусора - строки без :// не логируются. раньше пыталось парситься как ссылка и падало в ошибку
  - Уровень лога ERR → WARN для неподдерживаемых схем
#ZeroBlock

---

**2026-01-26T11:24:46 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r107:
  - automerge в nft при пересечении ip диапазонов в списках(исправление необязательное, если вы не используете отключение fakeip)
#ZeroBlock

---

**2026-01-26T13:25:47 | Сергей**
А подскажите пожалуйста как на zeroblock gemini ai запустить , все кроме него завелось

---

**2026-01-26T14:12:33 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.0-r111:
  - Дедупликация доменов в одной секции для отключенного fakeip(если домен есть в предустановленном листе, введённый вручную дубль отбрасывается)
  - Увеличены буферы всех пользовательских списков до динамических 64kb(~2000 доменов) и добавлен warning при переполнении
#ZeroBlock

---

**2026-01-26T15:33:43 | Routerich**
сторонний софт(podkop, zapret/zapret2), собственная разработка (zeroblock)

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

**2026-01-26T17:47:08 | Routerich**
zeroblock check_fakeip whatsapp.com
что покажет?

---

**2026-01-26T17:47:58 | Kiss_My_Axe**
root@roskomnadzor:~# zeroblock check_fakeip whatsapp.com
{"fakeip":1,"IP":"198.18.0.3"}

---

**2026-01-26T22:49:22 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.1-r2:
  - поддержка ipv6(включается в настройках)
  - Удален показ статуса включен/выключен для самого Zeroblock(есть кнопка, она показывает)
  - Устранены обнаруженные возможные утечки памяти
#ZeroBlock

---

**2026-01-26T23:05:20 | Kiss_My_Axe**
В подкопе для каждой секции можно указать свои ДНС.
Правда гонять рутуб с вк через подкоп такое себе.
Для этого гораздо лучше подойдёт ZeroBlock, так как он умеет направлять через себя траф не только в обходы, но и в обычный WAN.

---

**2026-01-27T11:31:47 | Михаил**
Который идет из ZeroBlock

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

**2026-01-27T14:21:25 | Routerich**
2 верхние, применить, перезапустить  zeroblock

---

**2026-01-27T17:35:05 | Kiss_My_Axe**
Использовать ZeroBlock.

---

**2026-01-27T17:35:30 | Anna Bagler**
Подкоп не поддерживает такой формат. Вам поможет zeroblock.

---

**2026-01-27T20:12:51 | Anna Bagler**
Точно через zeroblock yt?

---

**2026-01-27T20:53:28 | Юрий**
коннекты есть. Иногда в журнале урл адресов, фуй какойто появляется fakeip.zeroblock.fyi 😁

---

**2026-01-28T01:23:49 | Kiss_My_Axe**
Я тут малость очешуел.
Удалил curl, нужно для теста было.
Теперь у меня нет zapret2 и zeroblock.
ШТААААААААААААА?????

---

**2026-01-28T22:26:35 | Дмитрий**
Здесь? Zeroblock стоит

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

**2026-01-29T11:45:33 | Kiss_My_Axe**
Даже я сплю. Редко и тревожно, вскрикивая - zeroblock! podkop! куда ты, чёрт возьми, это прописал и зачем?! - но всё же.

---

**2026-01-29T13:32:46 | Kiss_My_Axe**
Придётся убирать. Есть некий нерешённый глюк - при включении ПМА отваливается нахрен локальная сеть.
Пробуйте заменить подкоп на ZeroBlock, в нём, возможно, этой проблемы не будет.

---

**2026-01-29T15:25:05 | Арчибальд**
Эту? Устанавливайте ZeroBlock на чистый роутер без других инструмен-
тов маршрутизации трафика (mwan3, pbr).

---

**2026-01-29T16:24:25 | @Dr.Medvedolog**
да, там уже вон скоро видео по установке ZeroBlock на Xiaomi, грядет буря

---

**2026-01-29T20:32:23 | Sh1nn**
А у меня так [nft_wrapper ] nft syntax check failed: Error: No such file or directory; did you mean table 'fw4' in family inet? add table inet zeroblock ^^^^^^^^^ Error: No such file or directory; did you mean table 'fw4' in family inet? add table inet zeroblock ^^^^^^^^^

---

**2026-01-29T20:58:17 | вася778**
[opkg_manager] Executing opkg command: install opera-proxy
[opkg_manager] Failed to install package 'opera-proxy'
[auto_install] Failed to install opera-proxy
[zeroblock] Opera Proxy auto-install failed: Error

---

**2026-01-29T21:02:29 | Dmitrii Burenin**
Thu Jan 29 20:00:00 2026 cron.err crond[13856]: USER root pid 14912 cmd /usr/bin/zeroblock badwan_check >/dev/null 2>&1
Thu Jan 29 20:10:00 2026 cron.err crond[13856]: USER root pid 18497 cmd /usr/bin/zeroblock badwan_check >/dev/null 2>&1
Thu Jan 29 20:20:00 2026 cron.err crond[13856]: USER root pid 21863 cmd /usr/bin/zeroblock badwan_check >/dev/null 2>&1
Thu Jan 29 20:30:00 2026 cron.err crond[13856]: USER root pid 23663 cmd /usr/bin/zeroblock badwan_check >/dev/null 2>&1
Thu Jan 29 20:40:00 2026 cron.err crond[13856]: USER root pid 25717 cmd /usr/bin/zeroblock badwan_check >/dev/null 2>&1
Thu Jan 29 20:50:00 2026 cron.err crond[13856]: USER root pid 29671 cmd /usr/bin/zeroblock badwan_check >/dev/null 2>&1

---

**2026-01-29T21:47:34 | Anna Bagler**
Пробуйте zeroblock, для полной маршрутизации устройства он должен быть лучше.

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

**2026-01-29T23:11:34 | Andrew Arzaev**
спасибо большое но у меня только ZeroBlock

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

**2026-01-30T00:03:35 | Anna Bagler**
https://telegra.ph/Polnaya-instrukciya-nastrojki-xHTTP-v-Podkop-12-08
Переходите на zeroblock.

---

**2026-01-30T02:46:28 | M D**
Я про zeroblock. Сразу на роутере

---

**2026-01-30T03:11:44 | Kiss_My_Axe**
Создать раздел с именем Direct_connection (имя для примера).
Тип подключения: VPN
Сетевой интерфейс: wan(switch)
Разместить раздел выше других.
Сохранить.
Далее прописать там адреса, которые должны ходить напрямую.

Под этим разделом разместить второй, указать интерфейс выхода, какой вам нужен.
Не заполнять в нём ничего, это переключит раздел в режим "catch all", то есть всё, кроме того, что прописано в разделе/разделах выше, будет уходить в него.

ZeroBlock 0.6.1-r80:
  Новое:
  - Catch-all секция — первая секция без доменов становится финальным outbound для всего трафика. Секции после catch-all полностью игнорируются

---

**2026-01-30T07:56:21 | ZЁма**
Zeroblock пока еще BETA.
Вы видели что твориться в топике Zeroblock BETA? Не успеешь отслеживать обновы в которых поправили 1 баг и добавили два (шутка).
Пришлось купить ещё один РР (пока в пути) что бы пробовать и тестить Zeroblock. На основном в доме РР я такого позволить себе не могу.

---

**2026-01-30T12:20:31 | ­**
zeroblock_manual.pdf  https://t.me/routerich/394153/432061?single
ну не прям талмут, но все же. Я не только для себя, а новичкам просто заглянувним в тему, чтобы быстро одним сообщением понять, в чем отличия. Тем более вы пишите "Полная с доп функционалом (альтернатива подкопа)"

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

**2026-01-30T13:41:55 | Kiss_My_Axe**
Это будет интересно, если и вправду заработает.
Тогда я бы предложил перейти на ZeroBlock.

---

**2026-01-30T16:12:42 | Routerich**
Здравствуйте, бывает. но причем тут zeroblock?

---

**2026-01-30T20:44:05 | Антон**
Добрый вечер! Как пользоваться 
ZeroBlock 0.6.1-r80:
  Новое:
  - Catch-all секция — первая секция без доменов становится финальным outbound для всего трафика. Секции после catch-all полностью игнорируются

---

**2026-01-31T00:08:49 | Anna Bagler**
В zeroblock, если это валидная подписка. Если же открывает граф. страницей с выбором клиента, то нет.

---

**2026-01-31T00:27:55 | Routerich**
Здравствуйте, бывает. но причем тут zeroblock?

---

**2026-01-31T00:28:00 | Temur K**
Sat Jan 31 00:26:40 2026 user.notice zeroblock: Generated Clash API secret
Sat Jan 31 00:26:40 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[ruleset_manager] API request failed (ret: 0, code: 400, size: 95)
[ruleset_manager] Failed to load community lists from API
[zeroblock] ZeroBlock started successfully
[cron_manager] Cron file not found: /etc/crontabs/root

---

**2026-01-31T05:59:34 | M L**
Решил поиграться с ZeroBlock после продолжительного пользования скрипта BETA. Такие параметры на скрине. Это норм?

---

**2026-01-31T11:00:59 | Mojo Man**
Еще бы помощь развёрнутую, списки не меняю уже неделю, Zeroblock в службах нет

---

**2026-01-31T13:09:04 | 𝒢𝑒𝒻𝑒𝓈𝓉**
Подскажите пожалуйста, почему у меня трафик не идет через Tailscale-Exit Node (мой RouteRich - секции последнего ZeroBlock), при этом Youtube проходит через Zapret2 того же роутера в том же режиме.

---

**2026-01-31T13:14:57 | 𝒢𝑒𝒻𝑒𝓈𝓉**
через старый ZeroBlock 1.0.0-r1 трафик полностью проходил.

---

**2026-01-31T16:27:50 | Anna Bagler**
Попробуйте zeroblock с отключенным подкопом.

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

**2026-01-31T19:26:12 | Routerich**
Заранее хотел написать. Стоит переходить медленно не верно на ZeroBlock. Так как в блажащее время откажемся от PodKop и его поддержки

---

**2026-01-31T22:26:53 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.1-r105:
  Исправления:
  - Добавлено правило nft для endpoint серверов при включеном proxy_router_traffic
  - Дедупликация ip nft правила для endpoint серверов
#ZeroBlock

---

**2026-02-01T03:08:39 | M L**
у меня ZeroBlock, Подкоп отдельно не установлен. пожалуйста, покажите скриншотом где  находится список клауда в подкопе используя зероблок

---

**2026-02-01T12:46:18 | Hump Dog**
Sun Feb 1 12:30:00 2026 cron.err crond[26621]: USER root pid 29176 cmd /usr/bin/zeroblock badwan_check >/dev/null 2>&1
Sun Feb 1 12:30:05 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Sun Feb 1 12:30:06 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[zeroblock] ZeroBlock started successfully
Sun Feb 1 12:40:00 2026 cron.err crond[29484]: USER root pid 32074 cmd /usr/bin/zeroblock badwan_check >/dev/null 2>&1
Sun Feb 1 12:40:05 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Sun Feb 1 12:40:05 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[zeroblock] ZeroBlock started successfully
WAN у меня хороший, а ZB думает что плохой?

---

**2026-02-01T13:14:59 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.1-r106:
  Исправления:
  - Race condition: dnsmasq пытался использовать nftsets до их создания 
  - Полный рестарт singbox при использовании bootstrap
#ZeroBlock

---

**2026-02-01T15:07:22 | Anna Bagler**
Если прошивка старая, то вам сюда https://t.me/routerich/80283/352975?single
А потом сюда https://t.me/routerich/173678/449069 или в zeroblock beta.

---

**2026-02-01T15:08:50 | Anna Bagler**
Да, старайтесь не использовать полный список, берите отдельными. Или пробуйте zeroblock.

---

**2026-02-01T15:11:14 | Anna Bagler**
Улучшенная альтернатива подкопу. Ветка zeroblock beta.

---

**2026-02-01T15:58:33 | Александр Самсонов**
Еще один вопрос, принцип работы с точки зрения пользователя zeroblock и подкопа схож? Списки там, простота добавления и т.п?

---

**2026-02-01T17:46:29 | Роман**
dnsmasq[1]: nftset inet zeroblock dns_awg10_cloudflare Error: No such file or directory
Что-то пропало? Или это и есть недоступный список?

---

**2026-02-01T17:54:06 | Камиль**
А подскажите пожалуйста, по двум вопросам:
1) Куда можно посмотреть, до субботы использовал подкоп, в субботу поставил zb, иногда для некоторых сайтов я включаю спец.по чтобы получить заветный доступ и не копаться в доменах с подкопом спец.по работало корректно и пускало куда хотел. 
Сейчас же спец.по запустилось я вижу коннект, но при попытке открыть любой сайт, он не открывается. Отключаю спец.по -> сайт открылся. Дело похоже либо в RR либо в Zero, я подключился к своей чистой сети, включил спец.по с тем же самым конфигом и все завелось. 
2) При обновлении Zero через пакеты:

udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: no lease, failing
Collected errors:
 * resolve_conffiles: Existing conffile /etc/config/zeroblock is different from the conffile in the new package. The new conffile will be placed at /etc/config/zeroblock-opkg.
Это норм ?

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

**2026-02-01T18:23:18 | Роман**
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Sun Feb 1 19:50:45 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[zeroblock] ZeroBlock started successfully
Sun Feb 1 20:10:23 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_cloudflare Error: No such file or directory
Sun Feb 1 20:10:23 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_cloudflare Error: No such file or directory
Всё равно после перезапуска в консоли.

---

**2026-02-01T18:24:04 | Камиль**
Аналогично) 
Sun Feb 1 18:16:05 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_domains Error: No such file or directory
[zeroblock] ZeroBlock started successfully
Sun Feb 1 18:20:16 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_user_text Error: No such file or directory
Sun Feb 1 18:20:27 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_domains Error: No such file or directory
Sun Feb 1 18:20:37 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_domains Error: No such file or directory
Sun Feb 1 18:20:49 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_google_play Error: No such file or directory
Sun Feb 1 18:20:50 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_google_play Error: No such file or directory
Sun Feb 1 18:23:18 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_google_play Error: No such file or directory

---

**2026-02-01T19:10:48 | Kiss_My_Axe**
Я бы предложил перейти на ZeroBlock, создать одну пустую секцию, в которой выходом указать ваш влесс. Сохранить, Применить, Перезапустить.
Настройка завершена.

Но устанавливать ZB придётся руками, его пока нет в репозиториях.

---

**2026-02-01T21:01:59 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.1-r110:
  Исправления:
  - Исправлен race condition после SIGHUP reload sing-box
  - DNS nftsets теперь создаются до записи конфигов dnsmasq
  - В two stage режиме используется полный restart вместо reload для sing-box

  Улучшения:
  - Параллельная загрузка списков через libcurl multi
  - Переименование badwan в bad_interface
  - Мониторинг bad_interface теперь детектит смену IP-адреса
  - Увеличены лимиты: MAX_SECTIONS 25, MAX_PROXIES 150

#ZeroBlock

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

**2026-02-02T07:42:20 | Anna Bagler**
Если прошивка старая, то вам сюда https://t.me/routerich/80283/352975?single
А потом сюда https://t.me/routerich/173678/449069 или в zeroblock beta.

---

**2026-02-02T08:30:24 | Anna Bagler**
Запрет2, zeroblock или podkop не помогают?

---

**2026-02-02T11:35:08 | Kiss_My_Axe**
Это баг подкопа, его пока не устранили.
Переходите на ZeroBlock - https://t.me/routerich/394153

---

**2026-02-02T11:35:34 | Роман**
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Mon Feb 2 13:14:35 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[zeroblock] ZeroBlock started successfully
Mon Feb 2 13:20:21 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_cloudflare Error: No such file or directory
Mon Feb 2 13:27:32 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_cloudflare Error: No such file or directory
Mon Feb 2 13:31:32 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_cloudflare Error: No such file or directory

Да он файл этот ищет вроде как.

---

**2026-02-02T12:44:21 | Роман**
Если говорить про ZeroBlock (да и подкоп) - то это список заблокированных ресурсов в России, очень большой. Не рекомендую его использовать.

---

**2026-02-02T12:53:57 | Routerich**
ZeroBlock писал сам ItDog для нас. Так что весь код его. А мы лишь просим исправить баги

---

**2026-02-02T14:48:22 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.1-r111:
  Исправления
  - Пропуск несуществующих VPN интерфейсов
  - Скрытие паролей из логов(hysteria2)
  - Скрытие полной ссылки подписки из лога
  - Защита от зависаний
  - 3 попытки скачивания с задержкой по экспоненте(1-2-4 секунды)
  - Строгая валидация nft set flags
#ZeroBlock

---

**2026-02-02T15:01:02 | Bullet for my valentine Poison**
Или Zeroblock + Zapret2 (все равно скоро будет релиз, Буянов обещал)

---

**2026-02-02T15:51:19 | Anna Bagler**
Обновлять пакеты все на роутере не надо. Прошейте его актуальной прошивкой. Потом скрип из ветки Beta или ZeroBlock.

---

**2026-02-02T15:56:11 | Добрый Кот**
Пошагово, сбрасываю в дефолт. Далее скриптом Beta или ZeroBlock ?

---

**2026-02-02T15:57:43 | Anna Bagler**
Если первая настройка, прошейте на 10.4 из темы Прошивка, потом бета-скрипт или zeroblock. Я тоже за zb.

---

**2026-02-02T16:17:06 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.1-r114:
  Исправления
  - Полный пропуск nft конфигурации при отсутствии интерфейса для секции
  - Маскирование ссылки самой подписки в логе
#ZeroBlock

---

**2026-02-02T16:35:18 | Kiss_My_Axe**
Тогда Применить = uci commit && /etc/init.d/zeroblock reload || restart

---

**2026-02-02T17:36:29 | Anna Bagler**
Какие списки ещё есть? Пробуйте zeroblock.

---

**2026-02-02T17:44:02 | Александр Воробьев**
Такой вопрос zeroblock идет только под RR или можно под ax3000t owrt использовать?

---

**2026-02-02T22:26:09 | Юрий**
выпал на несколько дней из теста... насколько я понял из планировщика эту строку можно удалить?
# ZeroBlock BadWAN Monitor
*/10 * * * * /usr/bin/zeroblock badwan_check >/dev/null 2>&1

---

**2026-02-02T23:34:54 | Anna Bagler**
Прошивку обновляйте без сохранения, потом скрипт Beta или ZeroBlock.

---

**2026-02-02T23:38:01 | Anna Bagler**
Тогда usb3.0 файлик нужен будет. https://t.me/routerich/80283/352975?single
А потом сюда https://t.me/routerich/173678/449069 или в zeroblock beta.

---

**2026-02-03T02:11:17 | Anna Bagler**
@Ugrumii_technar, эта тема для zeroblock. Пишите такие вопросы в Общении или ОфТопе. Если кратко, то да, роутеры схожи, поэтому на них спокойно встаёт owrt и портированый кинетик и прочее, форк от РР может встать, но с проблемами.

---

**2026-02-03T05:10:47 | Anna Bagler**
Настройки zeroblock посмотрите, должно быть там.

---

**2026-02-03T10:24:21 | Kiss_My_Axe**
Я ночером пропустил, видимо.
uci show zeroblock | grep "catch" писаль, но глаза не видель. Древнею.

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

**2026-02-03T11:16:42 | Роман**
То-есть дядя Вася берет роутер что-бы смотреть Ютуб, при этом ему надо попасть на замедленный Ютуб что-бы прошить роутер, накатить подкоп, настроить его? Так?
Да даже тот-же zeroblock  и zapret2 (с отличным веб интерфейсом и блокчеком) собственной разработки уже стоят того, что я "переплатил" - по вашему мнению. 
ИМХО, кому что нравится - тот то и берет. Без негатива естественно 😁

---

**2026-02-03T11:19:08 | Роман**
Пятый скрипт основан на бесплатных решениях. Лучшим выходом (в моем случае) было - Ютуб, Дискорд - запрет2, остальное в zeroblock со своим vless.

---

**2026-02-03T11:21:29 | Routerich**
поэтому в ZeroBlock 0.6.1-r103
  - Валидация IP, подсетей, доменов и интерфейсов(если есть такие, кто трогает конфиг zeroblock руками

---

**2026-02-03T12:11:45 | Routerich**
nft list table inet zeroblock
всю простыню сюда файлом

---

**2026-02-03T12:49:06 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.1-r124:
  Исправления:
  - Исправлена двойной restart при обновлении/установке пакета
  - Убраны дефолтные значения из конфига — теперь LuCI не удаляет опции при сохранении

  Новое:
  - Счётчики на всех правилах nftables — теперь можно видеть статистику через nft list table inet zeroblock
  - Подсветка catch-all секции в дашборде со списком исключённых IP
#ZeroBlock

---

**2026-02-03T15:13:54 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.1-r127:
  Исправления:
  - Очистка конфигов dnsmasq при перезапуске
#ZeroBlock

---

**2026-02-03T16:47:54 | Routerich**
https://t.me/routerich/394153/432059
ZeroBlock 0.6.1-r128:
  Исправления:
  - Ошибочная двойная очистка конфигов dnsmasq при перезапуске
#ZeroBlock

---

**2026-02-03T19:33:17 | Anna Bagler**
Ставьте zeroblock или скрипт из beta.

---

**2026-02-04T00:31:49 | Fredd**
А дальше будет еще печальнее.А пока изучите тему Интернет без границ,и Zeroblock,вместе с закрепами в них.Вам еще больше понравится).Можете еще и тему ремоте контрол почитать,тоже приятно удивитесь)

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

**2026-02-04T10:02:16 | Kiss_My_Axe**
@Fresa
Результат ночных бдений, промежуточный.

Нулевая прошивка USB2.0_routerich_24.10.4_RR382_ax3000.bin  - режим "Всё через запрет2" работает прекрасно.
Актуализация USB2.0_routerich_24.10.4_RR382_ax3000.bin через ASU - режим "Всё через запрет2" работает прекрасно.
Установка ZeroBlock - режим "Всё через запрет2" работать перестаёт.

Отключение ZeroBlock, отключение автозапуска ZerobLock с перезагрузкой, восстановление DNS "Как было до установки ZeroBlock" - нет, ми не хочим работать в режиме TAD.

---

**2026-02-04T10:04:22 | Bullet for my valentine Poison**
Хм, а Zeroblock на дефолтном конфиге? И какой порядок установки был?

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

**2026-02-04T12:53:29 | Routerich**
детальная инструкция по zeroblock, смотрим, впитываем, дополнения приветствуются. upd 16:05 15.04.2026
https://t.me/routerich/394153/432059

---

**2026-02-04T12:55:03 | Routerich**
пакеты  | полный мануал 
ZeroBlock 0.6.1-r130:
  Исправления:
  - Трафик xray-core теперь маркируется 0x40000000, чтобы Zapret2 его не обрабатывал (как
  sing-box и VPN интерфейсы)
#ZeroBlock

---

**2026-02-04T13:24:38 | Routerich**
пакеты  | полный мануал 
ZeroBlock 0.6.1-r131:
  Исправления:
  - Полностью маршрутизированные IP-адреса игнорировали fakeip
#ZeroBlock

---

**2026-02-04T13:54:51 | Евгений**
Здравствуйте! Пытаюсь собрать прошивку, не получается. Выдаёт ошибку "Impossible package selection". Я не специалист во всех этих делах, но как я понял из кучи всего, что написано, проблема в пакете zeroblock. Он должен ставиться через ASU или нет?

---

**2026-02-04T13:57:29 | Routerich**
Здравствуйте.
удалите пакет zeroblock из запроса сборки

---

**2026-02-04T14:05:54 | Евгений**
Ещё подскажите, пожалуйста, а youtubeunblock нужен вообще? Он отключён же получается всегда, пока zeroblock работает? Его может тоже исключить?

---

**2026-02-04T15:05:07 | Anna Bagler**
Скрипт из закрепов темы Веta или Zeroblock использовать.

---

**2026-02-04T17:41:41 | Anna Bagler**
Как вариант, попробуйте удалить интерфейс, который вы создали. Поставьте скриптом 5 подкоп, импортируйте в интерфейс awg10 свою конфигурацию. Удалите секцию proxy в подкоп. Удалите списки в секции discord, в полной маршрутизации укажите подсеть роутера. Или через zeroblock можно.

---

**2026-02-04T18:43:46 | Anna Bagler**
Потом вам или скрипт 5/бету, или zeroblock. Прошивка только с анблоком, ютубу может не помочь.

---

**2026-02-04T19:21:40 | Anna Bagler**
Обновлять прошивку без сохранения настроек и смотреть в стону zeroblock или скрипта 5/бета.

---

**2026-02-04T20:40:35 | Ww II**
Скажите пожалуйста, кто знает. Этот Zeroblock только для RR? Или можно его установить на ванильную OpenWRT допустим на Xiaomi Mi Router AX3000T?

---

**2026-02-04T21:07:03 | Routerich**
А если стопать Zeroblock, то все ок?

---

**2026-02-04T23:45:56 | Routerich**
ожидаем восстание против zeroblock как при блокировке roblox

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

**2026-02-05T11:05:09 | Kiss_My_Axe**
Багрепорт
Не устанавливается zeroblock_manual.pdf
Что делать?

---

**2026-02-05T13:00:37 | Routerich**
вывод покажите и что насчёт fakeip для секции?
nft list table inet zeroblock

---

**2026-02-05T13:03:44 | Routerich**
пакеты  | полный мануал 
ZeroBlock 0.6.1-r145:
  Исправление:
  - Пропущенное правило для conntrack
  Добавлено
  - Симметричные правила для output цепочки(снизит нагрузку от tailscale)
#ZeroBlock

---

**2026-02-05T13:31:14 | Routerich**
nft list table inet zeroblock

---

**2026-02-05T13:39:24 | Routerich**
пакеты  | полный мануал 
ZeroBlock 0.6.1-r146:
  Исправление:
  - user_subnets теперь маркируются в nftables независимо от disable_fakeip
#ZeroBlock

---

**2026-02-05T13:45:56 | Routerich**
это покажет что проблемы нет
nft list table inet zeroblock | grep 217

---

**2026-02-05T15:32:09 | Редиска на Луне**
добрый день! как увидеть какие домены в списках ZeroBlock,где они лежат на роутере?

---

**2026-02-05T16:26:48 | Routerich**
пакеты  | полный мануал 
ZeroBlock 0.6.1-r150:
  Исправление:
  - Удалены правила conntrack(до лучших времен)
  - Убран дубликат создания правил для disable_fakeip=1 секций
#ZeroBlock

---

**2026-02-05T16:38:45 | Редиска на Луне**
ZeroBlock  0.6.1-r131
Latest  Unknown
LuCI App  0.6.1-r81

подскажите, LuCI App такую версию пишет,на обновление нет ничего, это нормальная работа?

---

**2026-02-05T17:14:21 | Vkus Govna**
Господа, привет. 
В ожидании роутера курю гайды и инфу, но пока дается ннемножко со скрипом. 

Суть такая: есть пара своих конфигов shadowsocks и vless. Нужно будет включать один из них на постоянку, переключать в случае необходимости, и чтобы весь трафик шел через них - не по спискам доменов  (чтобы не заморачиваться), а прямо все целиком. Я так понимаю мне для этого лучше всего подойдет zeroblock?

Так же при этом нужно будет сделать так, чтобы одни клиенты (условно пачка телефонов, тв, пс5) лезли в интернет исключительно через прокси (ss/vless), а другие (рабочий комп) шли напрямую. Возможно ли будет раздать клиентам фиксированные локальные ip и указать что и через что будет в интернет ломиться?

---

**2026-02-05T18:33:41 | Anna Bagler**
Прошивку до последней обновите и бета-скрипт запустите.
Или zeroblock.

---

**2026-02-05T20:27:36 | Anna Bagler**
Со сбросом можно перейти на zeroblock.

---

**2026-02-05T21:18:51 | Anna Bagler**
Или скрипт из закрепов Beta, или файлы из ZeroBlock.

---

**2026-02-06T00:06:44 | Андрей**
Возможно ли сделать чтоб расширения для браузеров типа Smart Proxy, Proxy SwitchyOmega подключались к запущенным на роутере Opera, Sing box, AWG, Tor ? И чтоб это включалось через ZeroBlock.

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

**2026-02-06T08:56:46 | Andrey**
так. у меня тут вопрос родился. выяснил, что у меня в доме провайдер с оптухой появился, я вот думаю, стоит заморачиваться с 100мбит на 400 переходить. Вопрос собственно в следующем, роутрич нормально работает если от главного пустить витую к нему в ван? чтоб провайдера роутер мне просто отдавал интернет на него, а уже на роутриче настроить zeroblock, Что у них за роутер я понятия не имею и это не общеизвестный провайдер так сказать

---

**2026-02-06T10:06:39 | Routerich**
zeroblock check_dns_available
{
  "dns_status": 1,
  "dns_on_router": 1,
  "dns_server": "8.8.8.8",
  "dns_type": "doh",
  "bootstrap_dns_status": 1,
  "bootstrap_dns_server": "77.88.8.8",
  "dhcp_config_status": 1,
  "dnsmasq_server": "127.0.0.1#5359",
  "failsafe_installed": 1,
  "failsafe_primary_dns": "127.0.0.42#53",
  "failsafe_listen": "127.0.0.1#5359"
}
zeroblock show_sing_box_config | jq '.route.rule_set'
[
  {
    "type": "local",
    "tag": "community-opera-geoblock",
    "format": "binary",
    "path": "/tmp/zeroblock/rulesets/geoblock.srs"
  },
  {
    "type": "local",
    "tag": "community-opera-block",
    "format": "binary",
    "path": "/tmp/zeroblock/rulesets/block.srs"
  },
  {
    "type": "local",
    "tag": "community-opera-meta",
    "format": "binary",
    "path": "/tmp/zeroblock/rulesets/meta.srs"
  },
  {
    "type": "local",
    "tag": "community-opera-tiktok",
    "format": "binary",
    "path": "/tmp/zeroblock/rulesets/tiktok.srs"
  },
  {
    "type": "local",
    "tag": "community-awg10-cloudflare",
    "format": "binary",
    "path": "/tmp/zeroblock/rulesets/cloudflare.srs"
  },
  {
    "type": "local",
    "tag": "awg10-cloudflare-wildcard",
    "format": "source",
    "path": "/tmp/zeroblock/rulesets/awg10-cloudflare-wildcard.json"
  },
  {
    "type": "inline",
    "tag": "user-domains-awg10",
    "rules": [
      {
        "domain_suffix": [
          "2ip.io"
        ]
      }
    ]
  }
]
root@RouteRich:/tmp# zeroblock show_sing_box_config | jq '.route.rule_set' |grep tag
    "tag": "community-opera-geoblock",
    "tag": "community-opera-block",
    "tag": "community-opera-meta",
    "tag": "community-opera-tiktok",
    "tag": "community-awg10-cloudflare",
    "tag": "awg10-cloudflare-wildcard",
    "tag": "user-domains-awg10"

---

**2026-02-06T10:47:34 | Bullet for my valentine Poison**
Zapret2 + Zeroblock. И настраиваете.

---

**2026-02-06T11:39:18 | Семьдесят Семь**
а zeroblock это получается подкоп улучшенный?

---

**2026-02-06T11:41:35 | Семьдесят Семь**
окей, спасибо, а то когда роутер придёт не знаб что ставить подкоп или zeroblock

---

**2026-02-06T14:12:12 | Anna Bagler**
Zeroblock изучайте.

---

**2026-02-06T14:19:21 | Vasa**
podkop \ zeroblock

---

**2026-02-06T15:24:10 | Bullet for my valentine Poison**
Может вам попробовать пересесть на Zeroblock?

---

**2026-02-06T23:32:51 | Vasa**
подкоп или zeroblock бери. и туда vless \ амнезию суй

---

**2026-02-06T23:33:15 | Anna Bagler**
Можно zeroblock, а потом уже что хотите.

---

**2026-02-06T23:34:47 | Роман**
а сложно в zeroblock вставить свою url?

---

**2026-02-06T23:48:52 | Роман**
А если с умом к этому подойти, как лучше настроить? 
И если я поставлю zeroblock, мне нужно вручную всё прописывать, создавать секции для обхода аналогично подкопу?

---

**2026-02-07T09:59:07 | Роман**
Хронология простая, обновили прошивку, настроили сети, установили пароли. Далее, в прошивке уже установлен youtubeunblock без веб интерфейса - если он не помогает - удаляем его (если ставите 5й скрипт - он сам удалит). Далее если есть свои ключи vless или другое - ставите или zeroblock или podkop. Для Ютуба - zapret2. 
Если всё написанное выше для вас какие-то каракули - скрипт 5 из закреплённых сообщений в ветке интернет без границ, либо скрипт бета из ветки бета.

---

**2026-02-07T11:15:37 | Yury Kuzmenko**
Тут тема zeroblock

---

**2026-02-07T12:14:14 | Vlad Harden**
а после установки zeroblock как остановить подкоп?

---

**2026-02-07T12:57:58 | Vlad Harden**
Поставил  zeroblock ничего не поменялось, на андроид ТВ скорость 70, но подключаю впн и сразу 300, фигня какая-то 🧐

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

**2026-02-07T14:41:54 | Anna Bagler**
Попробуйте обновить прошивку, сбросить настройки, чтоб исключить глюки, настроить интернет, отключить ipv6, если провайдер не требует, и ещё раз скрипт запустить. Можете попробовать zeroblock вместо подкопа, но он в бета-тесте пока.

---

**2026-02-07T15:01:56 | Routerich**
он такими темпами zeroblock мутирует в ось на роутер

---

**2026-02-07T18:59:55 | Routerich**
полный мануал по zeroblock, зачем-то обновлён

---

**2026-02-07T19:37:13 | 🇷🇺Вячеслав**
Люди подскажите что может быть  обновил роутер обновлены все пакеты  стоит тока zeroblock и все .  Но вот проблема такая что по вайфаю 5г на компе скорость около 80мбит  на телефоне вообще 4мбит на второй машине подключение по проводу за место 1гб что показывает если вставить в обход роутера. Показывает тока 100 а измерения скорости дают тока 20мбит. Что за фигня.  Притом что если брать чисто кабель тотвсе норма по скорости и также если конектиться к роутеру мгтс на прямую так же все норма

---

**2026-02-07T20:09:19 | Azizkhan**
Поставил начистую Zeroblock, у меня одна секция с vless:
вроде бы всё работает, но по факту заблокированные сайты не работают
UPD: я не тот ключ вписал, всё ок, работает.

---

**2026-02-07T23:31:22 | Артем Дрезнель**
Я перед установкой ZeroBlock роутер скинул до заводских, не смогу продемонстрировать.. пороюсь в скриншотах на пк завтра,может сохранилось

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

**2026-02-08T11:38:17 | Bullet for my valentine Poison**
Ну как в мануале написано. Вставил youtube.com и поехал. И Запрет2 в основном работает по сайтам которые выдают connection_reset. Для всего остального используйте Zeroblock. (можете еще чат перечитать, может что-то полезное найдете)

---

**2026-02-08T11:45:53 | Matvey**
youtubeunblock не установлен, запрет2 остановил. просто у меня телевизор LG и там часто стратегии обхода перестают работать, а через ZeroBlock ютуб работал до недавнего времени

---

**2026-02-08T12:14:29 | Bullet for my valentine Poison**
Сделайте сброс или перепрошейте на завод. Потом установите ASU и через него обновите все пакеты. После попробуйте Zeroblock + Zapret2. Может будет лучше. Все надо пробовать. Провайдеры у всех делают разные блокировки.

---

**2026-02-08T13:28:37 | Matvey**
для работы ZeroBlock AWG нужен? у меня авг уже несколько месяцев не фурычит)

---

**2026-02-08T13:35:23 | Kiss_My_Axe**
Хотя может она и в релизе есть, некромантия эта. :)
ZeroBlock тогда.

---

**2026-02-08T18:57:35 | Maharishi**
root@RouteRich:~# logread | grep -i zeroblock | tail -20
Sun Feb  8 18:47:16 2026 daemon.err zeroblock[24343]: [http_client] curl_easy_perform failed: Error
Sun Feb  8 18:50:00 2026 cron.err crond[22542]: USER root pid 25399 cmd /usr/bin/zeroblock bad_interface_check >/dev/null 2>&1
Sun Feb  8 18:50:05 2026 user.notice zeroblock: Stopping ZeroBlock...
Sun Feb  8 18:50:05 2026 daemon.err zeroblock[25414]: [zeroblock] Stopping ZeroBlock...
Sun Feb  8 18:50:05 2026 daemon.err zeroblock[25414]: [zeroblock] ZeroBlock stopped successfully
Sun Feb  8 18:50:06 2026 user.notice zeroblock: Starting ZeroBlock...
Sun Feb  8 18:50:06 2026 daemon.err zeroblock[25551]: [zeroblock] Starting ZeroBlock...
Sun Feb  8 18:50:07 2026 daemon.err zeroblock[25551]: [http_client] Failed after 0 retries: https://raw.githubusercontent.com/itdoginfo/allow-domains/refs/heads/main/Subnets/IPv4/tiktok.lst (curl=0, http=404)
Sun Feb  8 18:50:07 2026 daemon.err zeroblock[25551]: [http_client] Failed after 0 retries: https://raw.githubusercontent.com/itdoginfo/allow-domains/refs/heads/main/Subnets/IPv4/geoblock.lst (curl=0, http=404)
Sun Feb  8 18:50:07 2026 daemon.err zeroblock[25551]: [http_client] Failed after 0 retries: https://raw.githubusercontent.com/itdoginfo/allow-domains/refs/heads/main/Subnets/IPv4/block.lst (curl=0, http=404)
Sun Feb  8 18:50:11 2026 daemon.err zeroblock[25551]: [zeroblock] ZeroBlock started successfully
Sun Feb  8 18:51:50 2026 user.notice zeroblock: Stopping ZeroBlock...
Sun Feb  8 18:51:50 2026 daemon.err zeroblock[26260]: [zeroblock] Stopping ZeroBlock...
Sun Feb  8 18:51:50 2026 daemon.err zeroblock[26260]: [zeroblock] ZeroBlock stopped successfully
Sun Feb  8 18:51:51 2026 user.notice zeroblock: Starting ZeroBlock...
Sun Feb  8 18:51:51 2026 daemon.err zeroblock[26397]: [zeroblock] Starting ZeroBlock...
Sun Feb  8 18:51:52 2026 daemon.err zeroblock[26397]: [http_client] Failed after 0 retries: https://raw.githubusercontent.com/itdoginfo/allow-domains/refs/heads/main/Subnets/IPv4/block.lst (curl=0, http=404)
Sun Feb  8 18:51:52 2026 daemon.err zeroblock[26397]: [http_client] Failed after 0 retries: https://raw.githubusercontent.com/itdoginfo/allow-domains/refs/heads/main/Subnets/IPv4/tiktok.lst (curl=0, http=404)
Sun Feb  8 18:51:52 2026 daemon.err zeroblock[26397]: [http_client] Failed after 0 retries: https://raw.githubusercontent.com/itdoginfo/allow-domains/refs/heads/main/Subnets/IPv4/geoblock.lst (curl=0, http=404)
Sun Feb  8 18:51:56 2026 daemon.err zeroblock[26397]: [zeroblock] ZeroBlock started successfully

---

**2026-02-08T19:04:49 | che**
В zeroblock не ставится галка на автозагрузка секций. Так и должно быть ?

---

**2026-02-08T20:42:20 | Anna Bagler**
Тогда да, настраивать под себя. Для инстаграм и другого - подкоп/zeroblock.

---

**2026-02-08T21:28:19 | Anna Bagler**
Cброс, zeroblock и запрет2 тогда уж. И анблок удалить.

---

**2026-02-08T22:15:50 | Anna Bagler**
Ставьте чистую систему, не трогайте обновление пакетов. Смотрите на работу. Скрипт 5/бета или zeroblock, zapret2. Больше ничего не трогайте.

---

**2026-02-09T09:32:13 | Камиль**
Поиск по похожим логам ничего не дал, может скриншотами кидали

Mon Feb  9 09:13:35 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_meta Error: No such file or directory; did you mean set 'cs_main_meta' in table inet 'zeroblock'?
Mon Feb  9 09:13:45 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_meta Error: No such file or directory; did you mean set 'cs_main_meta' in table inet 'zeroblock'?
Mon Feb  9 09:14:01 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_meta Error: No such file or directory; did you mean set 'cs_main_meta' in table inet 'zeroblock'?
Mon Feb  9 09:14:35 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_meta Error: No such file or directory; did you mean set 'cs_main_meta' in table inet 'zeroblock'?
Mon Feb  9 09:14:35 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_block Error: No such file or directory; did you mean set 'cs_main_meta' in table inet 'zeroblock'?
Mon Feb  9 09:14:45 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_meta Error: No such file or directory; did you mean set 'cs_main_meta' in table inet 'zeroblock'?
Mon Feb  9 09:19:33 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_meta Error: No such file or directory; did you mean set 'cs_main_meta' in table inet 'zeroblock'?
Mon Feb  9 09:19:44 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_meta Error: No such file or directory; did you mean set 'cs_main_meta' in table inet 'zeroblock'?
Mon Feb  9 09:22:53 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_meta Error: No such file or directory; did you mean set 'cs_main_meta' in table inet 'zeroblock'?
Mon Feb  9 09:22:54 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_meta Error: No such file or directory; did you mean set 'cs_main_meta' in table inet 'zeroblock'?
Mon Feb  9 09:22:58 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_meta Error: No such file or directory; did you mean set 'cs_main_meta' in table inet 'zeroblock'?
Mon Feb  9 09:23:41 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_user_text Error: No such file or directory
Mon Feb  9 09:23:41 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_user_text Error: No such file or directory
Mon Feb  9 09:24:33 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_meta Error: No such file or directory; did you mean set 'cs_main_meta' in table inet 'zeroblock'?
Mon Feb  9 09:24:40 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_user_text Error: No such file or directory
Mon Feb  9 09:24:42 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_user_text Error: No such file or directory
Mon Feb  9 09:24:43 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_user_text Error: No such file or directory
Mon Feb  9 09:24:44 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_meta Error: No such file or directory; did you mean set 'cs_main_meta' in table inet 'zeroblock'?
Mon Feb  9 09:24:45 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_user_text Error: No such file or directory
Mon Feb  9 09:25:07 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_meta Error: No such file or directory; did you mean set 'cs_main_meta' in table inet 'zeroblock'?
Mon Feb  9 09:25:11 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_meta Error: No such file or directory; did you mean set 'cs_main_meta' in table inet 'zeroblock'?
Mon Feb  9 09:25:25 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_user_text Error: No such file or directory
Mon Feb  9 09:25:28 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_user_text Error: No such file or directory
Mon Feb  9 09:25:33 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_meta Error: No such file or directory; did you mean set 'cs_main_meta' in table inet 'zeroblock'?
Mon Feb  9 09:25:33 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_main_meta Error: No such file or directory; did you mean set 'cs_main_meta' in table inet 'zeroblock'?
Версия: 0.6.2-r37

---

**2026-02-09T09:37:45 | Bullet for my valentine Poison**
[zeroblock] ZeroBlock started successfully
[clash_api] HTTP request failed with code 503
Mon Feb 9 03:00:00 2026 cron.err crond[24103]: USER root pid 837 cmd /usr/bin/zeroblock system_monitor >/dev/null 2>&1
[http_client] curl_easy_perform failed: Error
[http_client] curl_easy_perform failed: Error
[http_client] curl_easy_perform failed: Error
[dpi_checker] Failed (HTTP 202, no data)
[http_client] Response size exceeds maximum (2097152 bytes)
[http_client] curl_easy_perform failed: Error
[dpi_checker] Failed (HTTP 200, no data)
[http_client] Response size exceeds maximum (2097152 bytes)
[http_client] curl_easy_perform failed: Error
[dpi_checker] Failed (HTTP 200, no data)
[dpi_checker] Invalid or unsafe URL: https://media-assets.stryker.com/is/image/stryker/gateway_1?$max_width_1410$
[dpi_checker] HTTP error 404
Mon Feb 9 09:13:00 2026 cron.err crond[24103]: USER root pid 13597 cmd /usr/bin/zeroblock update_lists >/dev/null 2>&1
Mon Feb 9 09:13:01 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Mon Feb 9 09:13:03 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[http_client] Failed after 0 retries: https://raw.githubusercontent.com/itdoginfo/allow-domains/refs/heads/main/Subnets/IPv4/hodca.lst (curl=0, http=404)
не, у меня другие ошибки. Потом поправят. Так как на работу никак не влияет.

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

**2026-02-09T16:18:50 | Routerich**
пакеты  | полный мануал 
ZeroBlock 0.6.2-r47:
  Изменения:
  - В секциях с "Тип подключения = VPN" можно выбрать "Тип протокола DNS = Не настроено" что приведёт к использованию DNS сервера из основных настроек
  - Сортировка серверов подписки/urltest по пингу
  - Секции с 1 сервером/интерфейсом теперь выводятся в строку в dashboard
  - Всплывающая подсказка с полной ссылкой при наведении на кнопку удаления ссылки для urltest в окне редактирования(следующий билд)
  - Перенесена 404 ошибка на скачивание subnet списков в debug уровень логов
  - Диагностика не выполняется автоматически при открытии вкладки "Диагностика"
  - Полное переименование remote_domain_lists/remote_subnet_lists → user_domain_lists/user_subnet_lists
  - Поддержка локальных путей (/path/to/file.txt) с автоопределением формата (.srs/.json/.txt) и конвертацией
  - Кросс-секционная валидация дубликатов для user_domain_lists и user_subnet_lists
  - Внутрисекционная дедупликация: user_domains и user_domains_text добавляются в community_domains set

  Исправления:
  - Скачивание ipv6 subnet списков при выключенном ipv6
  - Обработка значения "undefined" из LuCI в DNS-полях
#ZeroBlock

---

**2026-02-10T07:09:19 | Anna Bagler**
Zeroblock.

---

**2026-02-10T13:33:53 | Routerich**
возможно как-то с zeroblock конфликтует это всё, адресация ipv6
как вариант

---

**2026-02-10T13:42:54 | Routerich**
поставьте галочку на маршрутизировать, потом проверьте если не будет работать нормально, стопните zeroblock и проверьте как будет, можно даже ребутнуть чтобы наверняка

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

**2026-02-10T17:50:37 | Писарев Андрей**
Отключил всё, Tailscale, ZeroBlock, Zapret2, роутер перезагрузил, так-же ничего не работает с этим скриптом.
Обновление списка пакетов вылетает с ошибкой, скрипты не запускаются.
Проблема видать не в программах.
Может в файерволе что надо подкрутить? Какие-то запросы куда-то не пускает.

---

**2026-02-10T18:09:43 | Anna Bagler**
Тогда ставьте скрипт из beta или zeroblock. И потом пускайте устройство в полную маршрутизацию.

---

**2026-02-10T19:44:19 | Routerich**
пакеты  | полный мануал 
ZeroBlock 0.6.2-r53:
  Изменения:
  - Сортировка конфига при сохранении(стал более читабельным)
  - Раньше один битый xray-прокси убивал запуск всех xray-секций. Теперь двухпроходная валидация: быстрый путь (один xray run -test на
  всё), а при ошибке — fallback с проверкой каждого прокси отдельно. Битые отсеиваются, рабочие запускаются
#ZeroBlock

---

**2026-02-10T20:05:52 | Maksim Lapin**
Мануал ... странный, если не сказать другим языком.
4.1 Установка через LuCI
1. Скачайте пакеты из релизов:  (как, где, откуда, порядок пунктов установки?)
• zeroblock_*.ipk
• luci-app-zeroblock_*.ipk
2. Откройте веб-интерфейс роутера
3. Перейдите в Система → Программное обеспечение (отсутствует путь, есть Система->Пакеты)
4. Нажмите Обновить списки
5. Загрузите и установите пакеты через Загрузить пакет (отсутвует пакеты в списке доступных, после обновления списков и фильтрации  пакетов по имени).

Это же первые ... пункты ... мануала. Они не должны быть легко повторяемыми и актуальными текущей поставляемой стоковой прошивке?

---

**2026-02-10T21:02:17 | Maksim Lapin**
Как я думаю? 
Пытаюсь думать логически.
К примеру, неинтуитивного вида инструмент (не молоток и не ложка) абсолютно любой степени распрекрасности четкости крутости и полезности вероятно абсолютно БЕСПОЛЕЗЕН без инструкции.

Неявные вещи:
Я новенький. Прежде чем сыпать в чатик вопросами, дай думаю прочешу доку. Начинаю это дело, файлик за файликом.
Тут бац, вроде файл с нужными мне словами в незнакомой экосистеме, и оформлен с вотермаркой  и лейбл и нигде на первой странице не написано например, что руководство надо начинать читать с закрепов тем в телеграмме, и не написано с закрепов каких тем.
Я же нуб, мне неочевидно зачем "комната наполнена швабрами", и вид мануала предполагает что он "вещь в себе", то есть целостный по сути. 
И вот только когда все менюшки уже истыкал в вебморде, и в телеге по поиску слова "zeroblock" дошел, тут уже узнается "Hello mazerfazer, мануал начинается с закрепа соседнего чата".

---

**2026-02-10T21:12:12 | Anna Bagler**
Обновляйте прошивку без сохранения настроек, потом бета-скрипт или zeroblock.

---

**2026-02-10T21:13:56 | Stanislav Gurov**
Добрый вечер!

Использую связку podkop + zapret. Вижу, что сейчас активно рекламируют связку zeroblock + zapret2.

Подскажите, где-то можно ознакомиться со сравнением podkop и zeroblock?

---

**2026-02-10T21:52:25 | Dmitriy M 🎃**
Здравствуйте. Если установил zeroblock то через ASU не получится обновиться? Не находит этот пакет

---

**2026-02-10T22:50:10 | Сергей**
Обновил до последней версии и получил не рабочий zeroblock

---

**2026-02-10T22:55:48 | Routerich**
в логе которого написано в чем проблема
Tue Feb 10 22:47:27 2026 daemon.err zeroblock[11866]: [config_builder] Duplicate community_list 'russia_outside' in sections 'opera' and 'awg10'
Tue Feb 10 22:47:27 2026 daemon.err zeroblock[11866]: [config_builder] Duplicate community_list 'tiktok' in sections 'opera' and 'awg10'
Tue Feb 10 22:47:27 2026 daemon.err zeroblock[11866]: [config_builder] Duplicate community_list 'google_ai' in sections 'opera' and 'awg10'
Tue Feb 10 22:47:27 2026 daemon.err zeroblock[11866]: [config_builder] Duplicate community_list 'google_play' in sections 'opera' and 'awg10'

---

**2026-02-11T06:01:07 | Routerich**
Так заведите как завели zeroBlock

---

**2026-02-11T08:25:02 | Maharishi**
А как правильно Zeroblock обновить? Просто закинуть новый пакет?

---

**2026-02-11T09:19:41 | Руслан**
Как уже можно ставить zeroblock как полноценную замену подкопа?

---

**2026-02-11T09:30:53 | Maharishi**
а через какую команду обновить списки? В мануале упоминается zeroblock update_lists, но она не рабоатет

---

**2026-02-11T09:32:21 | Maharishi**
мануале упоминается zeroblock update_lists, но она не рабоатет

---

**2026-02-11T14:46:12 | Роман**
Обновляете прошивку со сбросом всех настроек. Ставите ручками zeroblock, в него свою ссылку vless, рядышком запрет2 для Ютуба и никаких шляп 😁 
P.S не забудьте про бекапы.

---

**2026-02-11T15:11:23 | Роман**
Куда захотите. 
Если будете ставить подкоп или zeroblock - https://github.com/itdoginfo/allow-domains

---

**2026-02-11T18:06:29 | Роман**
А где свежий релиз? Чтоб как установить, как багов поймать, да багрепорт оформить 😁
Или zeroblock ВСЁ?!

---

**2026-02-11T18:30:41 | HiLLL**
Привет. Подписки обновляются только перезапуском ZeroBlock ?

---

**2026-02-11T18:34:24 | HiLLL**
Ок. В планировщик добавил. Пущай каждый час обновляет. 0 * * * * /etc/init.d/zeroblock restart

---

**2026-02-11T19:57:15 | Azizkhan**
zeroblock update_lists
{"status":"updating","message":"Starting lists update..."}
{"status":"updating","message":"Checking DNS availability..."}
{"status":"updating","message":"DNS check passed"}
{"status":"updating","message":"Checking GitHub connectivity..."}
{"status":"updating","message":"GitHub check passed"}
{"status":"updating","message":"Downloading and processing lists..."}
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: no lease, failing

========================================================================
         REMOVING ZEROBLOCK CRON JOB                           
========================================================================

✅ ZeroBlock cron job removed successfully
{"status":"success","message":"Lists updated successfully"}

---

**2026-02-11T19:58:09 | Антон**
Добрый вечер! Подскажите Roblox сегодня перестал работать - как исправить установлен ZeroBlock

---

**2026-02-11T20:00:05 | Anna Bagler**
Поиском пользуйтесь. Список tg в подкоп/zeroblock. С wa cложнее.
Вот так пробовать в ту секцию, где у вас своя ссылка https://t.me/routerich/3845/386082 и использовать приложение с оф. сайта, чтоб его не трогал маркет. Если не поможет, то дополнять подсети.

---

**2026-02-11T20:06:57 | Anna Bagler**
Вы в теме zeroblock. Эти списки в нем есть. Сам пакет и luci к нему установлены?

---

**2026-02-11T21:15:38 | Fredd**
Wed Feb 11 20:59:29 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[zeroblock] ZeroBlock started successfully
Wed Feb 11 20:59:52 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Wed Feb 11 20:59:53 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[zeroblock] ZeroBlock started successfully
[clash_api] /awg10/delay?url=http://cp.cloudflare.com&timeout=5000 failed: HTTP 504
[clash_api] /awg10/delay?url=http://cp.cloudflare.com&timeout=5000 failed: HTTP 504
[clash_api] /awg10/delay?url=http://cp.cloudflare.com&timeout=5000 failed: HTTP 504
[clash_api] /awg10/delay?url=http://cp.cloudflare.com&timeout=5000 failed: HTTP 504

---

**2026-02-11T21:18:48 | Fredd**
Wed Feb 11 21:16:33 2026 user.notice ucitrack: Setting up /etc/config/zeroblock reload trigger for non-procd /etc/init.d/zeroblock
Wed Feb 11 21:17:16 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[file_utils] Cannot open file: /tmp/zeroblock/versions.json: No such file or directory
Wed Feb 11 21:17:22 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: udhcpc: started, v1.36.1
Wed Feb 11 21:17:22 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: udhcpc: broadcasting discover
Wed Feb 11 21:17:24 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: udhcpc: no lease, failing
[zeroblock] ZeroBlock started successfully
Wed Feb 11 21:17:27 2026 daemon.notice procd: /etc/rc.d/S99zeroblock:
Wed Feb 11 21:17:27 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: ========================================================================
Wed Feb 11 21:17:27 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: REMOVING ZEROBLOCK CRON JOB
Wed Feb 11 21:17:27 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: ========================================================================
Wed Feb 11 21:17:27 2026 daemon.notice procd: /etc/rc.d/S99zeroblock:
Wed Feb 11 21:17:27 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: ✅ ZeroBlock cron job removed successfully
[clash_api] /awg10/delay?url=http://cp.cloudflare.com&timeout=5000 failed: HTTP 504
[clash_api] /awg10/delay?url=http://cp.cloudflare.com&timeout=5000 failed: HTTP 504

---

**2026-02-11T22:15:03 | De1Dev**
Всем привет! Извините за беспокойство.
Можно ли как то вернуть телеграмм в строй через Zero block?
Вроде, стоит телеграмм в ZeroBlock, но изображения грузятся дольше обычного, работает через раз.
Через ВПН, работает отлично.

---

**2026-02-11T22:24:02 | Роман**
Добавил в zeroblock - работает видео и сайт.

---

**2026-02-11T22:44:29 | vladimir**
www.udemy.com
frontends.udemycdn.com
hls-c.udemycdn.com
mp4-c.udemycdn.com
img-c.udemycdn.com
trk.udemy.com
m.stripe.com
m.stripe.network Странно как-то)) Стоит добавить такую штуку в Main Podkopa сразу отлетает Meta с Телегой))) Видимо придется прокачаться до ZeroBlock))) Неохота.... работает же все кроме этого курса будь он неладен))) Всем спасибо за помощь!

---

**2026-02-11T23:21:24 | Anna Bagler**
Скрипт из Beta или файлы из Zeroblock.
И потом контроль списков сообщества.

---

**2026-02-12T00:05:22 | Fos**
Только что узнал про ZeroBlock. Пока не понял, стоит ли его ставить вместо подкопа+запрет2... Пытаюсь найти достаточно информации в местных чатах. Обнаружил 2 инструкции по зероблоку. Обычная и полная. Логично было бы поместить в полную инструкцию (zeroblock_full_manual) всё содержимое zeroblock_manual. Особенно, описания способа установки, чего сейчас, увы, нет.

---

**2026-02-12T00:14:40 | Роман**
Zeroblock пока в бете, выйдет в окончательный релиз - будет полный мануал. Пока мануал в основном для тех, кто тестирует. Если что-то не понятно спрашивайте в ветке zeroblock.

---

**2026-02-12T08:13:04 | Вадим**
ZeroBlock в релиз вышел с новой прошивкой или до сих пор вета

---

**2026-02-12T11:21:44 | Routerich**
решите проблему с opkg, это не проблема zeroblock

---

**2026-02-12T11:33:35 | Courtney Love**
всем привет, подскажите пожалуйста, в репозитории не находится zeroblock, его там нет?

---

**2026-02-12T11:50:27 | Mikhail**
Здравствуйте, посмотрел в мануале и не нашел информации, может быть кто-то сталкивался: 

имеется Self-hosted Amnezia vpn и не могу разобраться можно ли его подключить в zeroblock? Не понимаю где можно подключить свой конфиг

---

**2026-02-12T12:08:02 | Anna Bagler**
Zeroblock, ecли вы готовы.

---

**2026-02-12T12:10:46 | Anna Bagler**
Пока zeroblock в тесте, но вполне нормально работает.

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

**2026-02-12T12:27:20 | Камиль**
Т.е. вроде как оптимальный сценарий это включить:
cloudfront,hetzner,ovh,digitalocean,hodca
Скрипт 
  zeroblock списки        main prx: geoblock,block,porn,news,anime,meta,twitter,hdrezka,tiktok,cloudfront,hetzner,ovh,digitalocean,google_ai,hodca
  zeroblock списки          ru prx: telegram,google_play
Пересечений не находит и по чекеру результаты не плохие 

Я всё правильно понял? Или это не доработка скрипта ? 
Еще смущает явное добавление Cloudflare, скрипт ругается а чекер говорит что больше ничего не находит...

---

**2026-02-12T12:47:45 | Andrey**
там уже zeroblock не апдейтят. проект закинули

---

**2026-02-12T13:44:46 | Routerich**
и если остановить zeroblock то что там же будет?

---

**2026-02-12T14:19:18 | Роман**
zeroblock, podkop

---

**2026-02-12T15:37:33 | Роман**
Здраствуйте. С подкопом скрипт закинул и всё, а как установить  ZeroBlock?

---

**2026-02-12T17:47:43 | Stanislav Gurov**
Спасибо за прошивку, очень ждал)

Только что перепрошился, настроил сеть + WiFi. Мастер настройки - жирный лайк 👍👏

WiFi потестил на iPhone 13 Pro Max возле роутера, по ощущениям ~ на 15% выросла скорость.

Теперь настал момент для тестирования новой связки zeroblock + zapret2 вместо старой podkop + zapret :)

---

**2026-02-12T18:09:01 | Anna Bagler**
Тогда zeroblock или бету, но отключить watchdoc.
Работал после прошивки или до?

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

**2026-02-12T19:39:25 | Anna Bagler**
Все как всегда, если zeroblock, то пакеты ставить руками из закрепа соответствующей темы.

---

**2026-02-12T19:42:24 | Роман**
Главное подкоп с zeroblock не ставьте. А уж последовательность не важна. 
Для только Ютуб в 24.10.5 уже есть youtubeunblock 1.3, к нему нужно установить веб интерфейс через пакеты. 
Так-же для Ютуба есть заперт2.  
Из прокси - zeroblock, подкоп.

---

**2026-02-12T19:45:24 | Роман**
5й скрипт это бесплатное решение со всеми вытекающими отсюда последствиями. Рекомендую не поскупиться и приобрести ключик vless (или поднять свой сервер) и перейти на zeroblock.

---

**2026-02-12T20:01:54 | Настроить Роутер**
Добрый вечер , подскажите , принимает ли другие транспорты/протоколы , или только vless ключи ZeroBlock ?

---

**2026-02-12T20:26:17 | Настроить Роутер**
Перед установкой ZeroBlock , обязательно удалять Podkop? Или достаточно, отключить/остановить ?

---

**2026-02-12T20:43:39 | Роман**
Проще zeroblock накатить.

---

**2026-02-12T20:48:37 | Роман**
А вот в zeroblock поставить галочку, применить, вставить ключик - готово. 👌

---

**2026-02-12T21:28:18 | Роман**
В zeroblock. В личку пойдет? А то в бан ещё раз не охота 😁

---

**2026-02-12T22:58:02 | Gomer Simpson**
Подкоп. Или ZeroBlock.

---

**2026-02-12T23:10:07 | Роман**
rabby.io закинуть в подкоп/zeroblock.

---

**2026-02-12T23:12:28 | Stanislav Gurov**
При использовании podkop и tailscale для удаленного доступа к роутеру, в подкопе необходимо было указывать Source Network Interface. Скажите, в ZeroBlock нужно что-то подобное сделать?

---

**2026-02-12T23:19:21 | Роман**
Обновите на 1.3 unblock через пакеты. 
А для обхода по ip вам либо zeroblock, либо podkop.
Или если уже стоит 1.3 - перезапустите.

---

**2026-02-12T23:23:01 | Anna Bagler**
Интернет без границ, скрипт 5 или закреп beta. Лучше zeroblock.

---

**2026-02-13T00:26:57 | chocho**
А telemt пойдет с ZeroBlock?

---

**2026-02-13T00:28:46 | chocho**
ну вместе с zeroblock будет работать?

---

**2026-02-13T00:30:08 | @Dr.Medvedolog**
Mixed Proxy в Zeroblock включаете, в telemt указываете 127.0.0.1:2080 в качестве Upstream Proxy, Профит

---

**2026-02-13T08:22:57 | Routerich**
Здравствуйте
по 5-му скрипту ставится Podkop.
при чём тут ZeroBlock?

---

**2026-02-13T08:23:18 | Routerich**
если нужен ZeroBlock ставьте его сразу, минуя 5-й скрипт.

---

**2026-02-13T09:59:17 | Kiss_My_Axe**
ZeroBlock установили, он вам подарочек под ёлочку принёс.

---

**2026-02-13T10:40:01 | Роман**
База под использование различных пакетов как zeroblock, podkop, zapret2, в виде openwrt есть. Но придется их самому установить и настроить.

---

**2026-02-13T11:40:38 | Routerich**
Здравствуйте.
а интерфейс TailScale добавлен в Podkop/ZeroBlock?

---

**2026-02-13T11:41:06 | ZЁма**
1. Скидываю в завод РР или перепрошиваю без сохранения настроек;
2. Обновляю списки пакетов;
3. Удаляю пакет "youtubeUnblock" в установленных пакетах;
4. Ставлю пакет "zeroblock_X.X.X-rXX_aarch64_cortex-a53", если есть ошибки, то игнорю;
5. Ставлю пакет "luci-app-zeroblock_X.X.X-r1XX_all";
6. Перезагружаю РР что бы в службе появился ZeroBlock;
7. Необходимо настроить автоконфигурацию в LuCI:
   - откройте веб-интерфейс роутера;
   - перейдите в Службы → ZeroBlock → Автонастройка;
   - включите нужные опции:
      • Install Opera Proxy — для секции opera;
      • Configure AmneziaWG WARP — для секции awg10;
   - нажмите Применить;
   - перезапустите сервис: Вкладка "Секции маршрутизации", кнопка "Перезапустить"

---

**2026-02-13T12:44:17 | Антонов Александр**
Здравствуйте, после установки ZeroBlocka на Андройд телевизоре перестало работать Movix домру, ip стал шведским с этим по моему это связано, прошу помочь

---

**2026-02-13T14:49:37 | Владимир Сурков**
в мануале не нашел как его установить 
пролистал пару раз 
и там уже идет первоначальная установка 
можете подсказать как это сделать

к примеру я сброшу РР до заводских 
или остановклю подкоп и уберу автозапуск 
а дальше как (как сделать так чтоб zeroblock появился у меня в службах?)

---

**2026-02-13T15:25:33 | Roman Zhukovskii**
Добрый день! Подскажите, пожалуйста, сбросил роутер до заводских, поставил zeroblock, но вот например youtube перестал работать, пошел смотреть конфиги и увидел там такое

---

**2026-02-13T17:21:57 | 𝒢𝑒𝒻𝑒𝓈𝓉**
добрый вечер всем! Настраиваю ZeroBlock на роутере Cudy и при удаленном доступе по Tailscale к нему выскочила такая ошибка. Подскажите , где исправить Перенаправление DNS на DNS Failsafe Proxy?

---

**2026-02-13T19:58:43 | Anna Bagler**
Да, переходите на zeroblock. Обязательно сделайте бэкап, чтоб откатиться, если что.

---

**2026-02-13T21:32:48 | Bullet for my valentine Poison**
Ну это же логично, человек пилит одновременно Zapret2 и Zeroblock. На все нужно время.

---

**2026-02-13T22:05:48 | Anna Bagler**
Вам достаточно будет zeroblock.

---

**2026-02-13T22:06:17 | Yury Kuzmenko**
Тогда смотрите, идете в тему зероблок качаете два файла, через менеджер пакетов устанавливаете. Сначала zeroblock потом luci app. Далее создаете секцию, закидываете туда свою ссылку(ставите режим URL proxy). Выбираете нужные списки

---

**2026-02-13T22:12:41 | Anna Bagler**
Вам надо самостоятельно подбирать стратегии для zapret2/zapret самостоятельно, т.к. LG капризен. Можно пробовать zeroblock или радикально - приставка на андроид к вашему ТВ и потом уже обходы.

---

**2026-02-13T22:19:24 | Routerich**
#Zeroblock пройдитесь по тегу, там будут видны изменения и что добавляли и какие баги исправляли

---

**2026-02-13T22:57:12 | Kiss_My_Axe**
Готовьтесь, будет гениальное предложение о скрещивании ужа и ежа.
Автохостлист в Z2, в отличие от Z1, надо подключать к секции отдельно.
То есть автохостлист может собираться, но не применяться.
Отсюда - подключить его к ZeroBlock, как локальный файл со списком доменов.
А? Каково? Это вам не это!

---

**2026-02-14T00:06:53 | Bullet for my valentine Poison**
ну 1000 это слишком много. А как  тестировал? Включл страту на проверку, перезапустил ютуб на тв? (тогда идти в раздел Zeroblock и ставить его) Потом расскажу что делать дальше.

---

**2026-02-14T00:07:14 | Anna Bagler**
Zapret удалить. Zeroblock и свежий youtubeUnblock поставить.

---

**2026-02-14T00:11:23 | Anna Bagler**
Zeroblock и запрет2. Только zb надо будет обновлять в связи с изменениями.

---

**2026-02-14T00:19:49 | Fredd**
Тема ZeroBlock Beta

---

**2026-02-14T00:19:49 | Anna Bagler**
zeroblock.

---

**2026-02-14T02:03:31 | Kiss_My_Axe**
Схема более чем рабочая, но довольно медленная.
Детект, внесение в список, циклический скрипт каждые 10 секунд проверяет размер списка, при изменении рестартует ZeroBlock.
Тут возникает проблема номер 1 - ДНС-кэш - из-за внезапного перехода на фейкайпи некоторые интернет-бродилки впадают в кататонию на длительное время. Это может сбивать с толку.

Проблема 2 - если сканить ютуб, например, то rr—-s8erfhl.djkn.googlevideo.com на отличненько залетают в список, нужны предварительные заглушки в виде googlevideo.com, ytimg.com etc.

А в остальном вполне себе решение, создающее проколы там, где универсальная страта не справляется.
youtube
default на все домены (вот тут вопрос)
zeroblock-domain-catch - Автосписок включен, применён список из одного левого домена, стратегии отсутствуют.

---

**2026-02-14T08:30:52 | sergey**
Установил ZeroBlock все нормально ютуб летает, но меня напрягло, что включен youtubeUnblock.... отключаешь его, ютуб не работает, так и должно ? Он должен быть вллючен

---

**2026-02-14T09:45:13 | Роман**
zeroblock конечно.
В вот в чате itdoga скажут что подкоп. 
Вот и думайте 😁

---

**2026-02-14T09:46:01 | Megaherz**
zeroblock уже установил

---

**2026-02-14T09:57:20 | Vasa**
ZeroBlock, по подписке...

с флешки нет такого

---

**2026-02-14T10:39:41 | Kiss_My_Axe**
Зависит от настроек ZeroBlock.
Запустите это в терминале роутера, cкрин-фото-текст результата пришлите.
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/test_config_script/test_config_script_nightly)

---

**2026-02-14T11:00:01 | Роман**
Можете установить через пакеты zapret2. 
Или отключить ЮАБ, и включить Ютуб в zeroblock. Главное чтобы не было никаких пересечений.

---

**2026-02-14T11:47:05 | sergey**
Анализ запущен: 2026-02-14 15:45:15
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  157.240.205.35 | YouTube IP:  198.18.0.26

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.41 MB
  Пинг (ya.ru via awg10): 56.199 / 64.555 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock списки       awg10 vpn: meta
  zeroblock списки       opera prx: geoblock,block,youtube,telegram
  Версия zeroblock: 0.6.2-r66
  zeroblock DNS/Bootstrap DNS: 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.19 | RAM: 44% | NAND: 25% занято / 50.7M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-02-14T13:08:45 | Den**
В темной теме RR сделать бы галочки не серыми (их плохо видно. пример - вкладка автонастройки в zeroblock), а ярко зелеными.

---

**2026-02-14T13:57:53 | ㅤㅤ**
Подскажите, пожалуйста, читать лень копец.  Поставил начисто новую прошивку и zeroblock. Если ставить галочку в нём на запрет два, он отдельную службу делает или как? Если нет, то нет смысла ставить отдельно запрет2 ?

---

**2026-02-14T15:27:02 | Anna Bagler**
Тогда вам нужен zeroblock.

---

**2026-02-14T16:34:19 | Rom@n**
А что это не правильно, у меня так же.
root@RouteRich:~# ip rule show
0:      from all lookup local
105:    from all fwmark 0x1 lookup zeroblock
5210:   from all fwmark 0x80000/0xff0000 lookup main
5230:   from all fwmark 0x80000/0xff0000 lookup default
5250:   from all fwmark 0x80000/0xff0000 unreachable
5270:   from all lookup 52
32766:  from all lookup main
32767:  from all lookup default
root@RouteRich:~# ip route show table 100
local default dev lo proto static scope host

---

**2026-02-14T16:54:13 | Роман**
Zapret2 для Ютуба и дискорда, zeroblock для телеги.

---

**2026-02-14T16:58:30 | Dmitriy**
прикольно, не надо вспоминать что ставил при asu ===============================================
opkg update
opkg install luci-app-zeroblock
opkg install zeroblock
opkg install luci-i18n-attendedsysupgrade-ru
=============================================== прикрутить бы его к asu, чтоб вываливал список перед обновлением😁

---

**2026-02-14T17:33:10 | Anna Bagler**
Лучше zeroblock вместо подкопа.

---

**2026-02-14T18:15:59 | Routerich**
Здравствуйте.
Можете поставить 5 скрипт или Zeroblock, потом создать интерфейс AWG новый туда Импортировать конфиг свой и зону назначить как на интерфейсе Awg10

---

**2026-02-14T18:20:34 | Марат**
Проще и надежнее zeroblock?

---

**2026-02-14T18:50:09 | Олег**
А для x86/64 zeroblock будет?

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

**2026-02-14T19:48:46 | Anna Bagler**
Если ничего не делали руками, пробуйте обновить youtubeUnblock на более свежий и с ним посмотреть. Но если не пойдет, то вам zeroblock нужен. И прошивку обновить на свежую.

---

**2026-02-14T20:39:29 | K**
Если анблок установлен (ютуб работает отлично), то запрет2 не нужно ставить? Осталось установить только zeroblock для всего остального?

---

**2026-02-14T20:41:07 | K**
А работа WA и TG звоники в Zeroblock, верно?

---

**2026-02-14T21:44:27 | Марат**
А как в zeroblock свою амнезию прописать? Где это там? Не понимаю.

---

**2026-02-14T21:51:36 | Борис**
Читал документацию по zeroblock и у меня возник странный вопрос. А можно ли скомпилировать правила для sing-box в виде .srs на компьютере, и затем закинуть на роутер (как-то рядом с config.json, чтобы сохранилась возможность для люси читать его), или правила будут скомпилированы под архитектуру компьютера и не будут работать на роутере? Ответ на упреждение, почему я об этом подумал - чтобы сравнить скорость маршрутизации с json и с srs

---

**2026-02-14T23:27:46 | Роман**
Инсту проще в zeroblock или подкоп закинуть.

---

**2026-02-14T23:51:20 | Борис**
Поставил zeroblock, вроде бы маршрутизация работает из коробки, Российские сайты с Российским ip открываются и chatgpt работает, значит прокси в деле. Но почему-то плитки над секцией opera и warp не грузятся - в консоли браузера пишет, что по websocket на 9090 порту не может соединиться. Хотя панель Yacd на этом порту работает, если её в браузере открыть. Использую веб-сервер nginx (на нём luci морда, uhttpd отключен, включено перенаправление на https в люси). Это из-за моего конфига, или какой-то баг?

---

**2026-02-14T23:58:06 | Anna Bagler**
Бета или Интернет без границ, или zeroblock.

---

**2026-02-15T00:24:10 | Anna Bagler**
Ну, все... Теперь мастер. Парольте сети. И задайте пароль администратора, но чтоб не забыли.  Обход блокировок завтра крутить или самому разбираться - zeroblock beta тема.

---

**2026-02-15T00:33:48 | Anna Bagler**
Контроль доступа не работает, если стоит подкоп. С zeroblock - работает. Есть блокировка по IP. Но надо руками туда-сюда, нет расписания.

---

**2026-02-15T00:34:53 | Виктор ZEUS**
С zeroblock  где этот раздел ?

---

**2026-02-15T00:39:52 | Anna Bagler**
Значит на ТВ не разблокировался. Или завтра, или самостоятельно разбирайтесь, тема Zeroblock.

---

**2026-02-15T01:25:23 | Павел Четвертков**
zeroblock это типа podkop? Раздельное туннелирование?

---

**2026-02-15T01:28:26 | Routerich**
Перейдите в тему зероблок бета и по тегу #Zeroblock почитайте о добавлении фичей и исправлении багов

---

**2026-02-15T05:27:11 | Art S.**
Приветствую. очень интересная у вас затея. А я правильно понял, что zeroblock - это исключительно для ваших фирменных роутеров? а то я тут на xiaomi ax3600 хотел накатить, так смотрю ничего не ставится автоматом, все пакеты пришлось руками нести. 

Было бы классно кстати иметь возможность купить не роутер, а доступ к сервису ) тожэе прикольная тема была бы ) ну а так я пока be7200 подожду, довольно заманчивая конфигурация у него..

---

**2026-02-15T06:28:57 | M L**
не удержался, обновился до 24.10.5 со сбросом до заводских, но теперь не могу установить ZeroBlock. у кого-то таже проблема была, но не могу найти в этой массе переписки. посоветуйте, плиз, как запустить ZB.

---

**2026-02-15T11:52:19 | K**
Прошивка роутера, Zapret2, ZeroBlock и прочие пакеты каким образом обновляются?

Где то будет кнопка обновить или как этот принцип в Openwrt реализован?

---

**2026-02-15T12:59:42 | Anna Bagler**
Надо знать тип и данные подключения к провайдеру. Далее в админку роутера и Мастер настроек в меню слева.
Если роутер из последней партии, то прошивка уже свежая.
Далее вам нужна тема Zeroblock. Если нет своих решений по vpn пока можно потестировать бесплатные. Но на них большая нагрузка.

---

**2026-02-15T13:26:48 | Dmitry Apelt**
Нашел в доке по ZeroBlock что его можно включить в службах, но его там не наблюдаю (вероятно нужно обновиться или как-то его добавить)

---

**2026-02-15T13:28:32 | Роман**
Качать в закрепе темы zeroblock.

---

**2026-02-15T13:30:52 | Роман**
3.8.2 можно ставить zeroblock.

---

**2026-02-15T13:34:01 | Dmitry Apelt**
Я правильно понимаю что эти файлы (luci-app-zeroblock_0.6.2-r66_all.ipk и zeroblock_0.6.2-r66_aarch64_cortex-a53.ipk) нужно через (Система -> Пакеты -> Загрузить пакет) ставить?

---

**2026-02-15T13:35:54 | Роман**
Всё верно, для начала zeroblock, затем luci.

---

**2026-02-15T13:41:35 | Routerich**
Почитайте документацию к zeroblock. И пишите в тему самого zeroblock

---

**2026-02-15T13:42:53 | Dmitry Apelt**
Спасибо ZeroBlock появился в меню службы

---

**2026-02-15T14:21:16 | Вячеслав**
А как правильно установить Zeroblock? Там же кроме самой программы и люси-апп наверное нужны зависимости? xray или sing-box или еще что-то. Если просто 2 файла через интерфейс роутера установлю - зависимости все подтянет или нет?

---

**2026-02-15T18:26:34 | Routerich**
В тему zeroblock с логами и прочим

---

**2026-02-15T18:48:15 | Denis**
Уже кажется я запутался во всем вновь, в том числе и в ветках
Мне телек кинуть в АВГ через ZeroBlock?

---

**2026-02-15T18:52:01 | Anna Bagler**
Ничего не трогайте или читайте полный мануал к zeroblock.

---

**2026-02-15T18:59:05 | Anna Bagler**
Оно может падает по своим причинам - блокировкам. Если у вас есть свой vless или ещё что, добавляйте в zeroblock и все.

---

**2026-02-15T20:00:47 | Вячеслав**
Не думал вообще, что клиент на роутере поднять сложнее, чем xray на сервере. Уже с четвертой программой вожусь. v2rayA падал, Passwall2 не работал, так и не разобрался, Podkop вот заработал частично, но кроме ютуба на телефоне и тв, а мне как раз на тв надо. ZeroBlock пока вообще не фурычит

---

**2026-02-15T20:05:57 | Вячеслав**
где их глянуть по зероблоку? вот это все что выдает logread
root@RouteRich:~# logread | grep -iE 'zeroblock' | tail -20
Sun Feb 15 18:08:25 2026 daemon.err zeroblock[16739]: [zeroblock] Starting ZeroBlock...
Sun Feb 15 18:08:29 2026 daemon.err zeroblock[16739]: [zeroblock] ZeroBlock started successfully
Sun Feb 15 18:11:37 2026 user.notice zeroblock: Stopping ZeroBlock...
Sun Feb 15 18:11:37 2026 daemon.err zeroblock[17975]: [zeroblock] Stopping ZeroBlock...
Sun Feb 15 18:11:38 2026 daemon.err zeroblock[17975]: [zeroblock] ZeroBlock stopped successfully
Sun Feb 15 18:11:39 2026 user.notice zeroblock: Starting ZeroBlock...
Sun Feb 15 18:11:39 2026 daemon.err zeroblock[18110]: [zeroblock] Starting ZeroBlock...
Sun Feb 15 18:11:40 2026 daemon.err zeroblock[18110]: [zeroblock] ZeroBlock started successfully
Sun Feb 15 18:12:02 2026 user.notice zeroblock: Stopping ZeroBlock...
Sun Feb 15 18:12:02 2026 daemon.err zeroblock[18522]: [zeroblock] Stopping ZeroBlock...
Sun Feb 15 18:12:03 2026 daemon.err zeroblock[18522]: [zeroblock] ZeroBlock stopped successfully
Sun Feb 15 18:12:04 2026 user.notice zeroblock: Starting ZeroBlock...
Sun Feb 15 18:12:04 2026 daemon.err zeroblock[18593]: [zeroblock] Starting ZeroBlock...
Sun Feb 15 18:12:08 2026 daemon.err zeroblock[18593]: [zeroblock] ZeroBlock started successfully
Sun Feb 15 20:04:48 2026 user.notice zeroblock: Stopping ZeroBlock...
Sun Feb 15 20:04:48 2026 daemon.err zeroblock[7477]: [zeroblock] Stopping ZeroBlock...
Sun Feb 15 20:04:48 2026 daemon.err zeroblock[7477]: [zeroblock] ZeroBlock stopped successfully
Sun Feb 15 20:04:49 2026 user.notice zeroblock: Starting ZeroBlock...
Sun Feb 15 20:04:49 2026 daemon.err zeroblock[7612]: [zeroblock] Starting ZeroBlock...
Sun Feb 15 20:04:54 2026 daemon.err zeroblock[7612]: [zeroblock] ZeroBlock started successfully

---

**2026-02-15T20:48:44 | Роман**
Sun Feb 15 22:47:09 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[config_builder] Duplicate community_list 'geoblock' in sections 'zbs' and 'awg10'
[config_builder] Found 1 duplicate target(s) between sections, aborting
[config_builder] Failed to load config
[zeroblock] Failed to start ZeroBlock

---

**2026-02-15T20:49:39 | Bullet for my valentine Poison**
[zeroblock] Failed to start ZeroBlock

---

**2026-02-15T21:33:13 | Stas Vasiliev**
всем привет!
перепрошился с нуля на последнюю, без сохранения конфига, установил ЗБ, вот, что в логах

Sun Feb 15 16:33:09 2026 user.notice ucitrack: Setting up /etc/config/zeroblock reload trigger for non-procd /etc/init.d/zeroblock
Sun Feb 15 16:33:26 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[config_builder] Sing-box failed to start in bootstrap mode (port 19999)
[zeroblock] Failed to start ZeroBlock
Sun Feb 15 16:33:42 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: Error: Failed to start ZeroBlock
luci: accepted login on /admin/services/zeroblock for root from 192.168.1.179

при этом сайнбокс есть

---

**2026-02-15T21:42:06 | Вячеслав**
Sun Feb 15 21:38:11 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[zeroblock] ZeroBlock started successfully
[clash_api] /Moldova/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 404
[clash_api] /Moldova/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 404
[clash_api] /Moldova/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 404
Sun Feb 15 21:38:21 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully

---

**2026-02-15T22:43:44 | Михаил**
Добавить список youtube в список к opera или awg zeroblock и стопнуть youtubeunblock.  Имхо...

---

**2026-02-15T23:08:45 | Виктор Миронов**
В инструкции написано зайти в службы  -> ZeroBlock  но в службах такого нет спасайте

---

**2026-02-15T23:09:14 | Роман**
На чистой прошивке установлен youtubeunblock, поэтому Ютуб работает. Для доступа к запрещёнке можете установить скрипт 5 для бесплатных решений, так же руками zeroblock или подкоп для своего сервера или ссылки vless.

---

**2026-02-15T23:21:04 | Виктор Миронов**
Collected errors:
 * pkg_hash_check_unresolved: cannot find dependency zeroblock for luci-app-zeroblock
 * pkg_hash_fetch_best_installation_candidate: Packages for luci-app-zeroblock found, but incompatible with the architectures configured
 * opkg_install_cmd: Cannot install package luci-app-zeroblock.

---

**2026-02-15T23:25:44 | Виктор Миронов**
Если честно я  не знаю,но вот что выдало при установки zeroblock

---

**2026-02-16T09:29:58 | Роман**
Доступ к Ютуб - youtubeunblock установлен изначально в прошивке (веб интерфейс устанавливать самому), не поможет - запрет 2. 
Для Инстаграма zeroblock со своим сервером или подкоп. 
Для бесплатных (у меня лапки) решений скрипт 5 в разделе интернет без границ, либо бета скрипт в разделе бета.

---

**2026-02-16T11:04:21 | Routerich**
во-первых, это не проблема zeroblock. во вторых настройте интернет детектор на перезапуск, или включите мониторинг в zeroblock
вот что делает мониторинг
  1. Пинг через awg10 — icmp_ping_full("awg10", "1.1.1.1") с таймаутом 6 сек
  2. Если пинга нет — запускает zeroblock awg warp (полная переустановка WARP)
  3. Если пинг есть, но мониторинг считает что что-то сломано — делает ifdown awg10; sleep 1; ifup awg10 (перезапуск интерфейса)

---

**2026-02-16T11:19:57 | Симеона**
Здравствуйте! Видит ли провайдер факт использования zapret/podkop/zeroblock?

---

**2026-02-16T11:24:38 | Vigilante**
Здравствуйте! Извините, если совсем глупый вопрос...
В общем, установил ZeroBlock, настроил со своим VPN (подписка), две секции - основная и Youtube, всё работало прекрасно, но. Пришлось сменить провайдера. Старый провайдер настраивался по DHCP и веб-авторизации, новый - через статический адрес со своими DNS-серверами. И тут я обнаружил проблему с DNS-проверкой и неработоспособностью Youtube. Остальное вроде работает нормально. Куда копать?

---

**2026-02-16T11:27:27 | Владислав**
zeroblock > секции маршрутизации > на нужной секции "изменить" > Ввод пользовательских доменов: текстовое поле > Список пользовательских доменов: вбиваете ваши домены

---

**2026-02-16T11:39:49 | Routerich**
Mon Feb 16 11:38:10 2026 daemon.err zeroblock[7535]: [http_client] curl_easy_perform failed: Error
Mon Feb 16 11:38:10 2026 daemon.debug zeroblock[7535]: [http_client] Freed HTTP request
Mon Feb 16 11:38:10 2026 daemon.err zeroblock[7535]: [ruleset_manager] API request failed (ret: -4, code: 0, size: 0)
Mon Feb 16 11:38:10 2026 daemon.warn zeroblock[7535]: [ruleset_manager] Failed to load community lists from any source
Mon Feb 16 11:38:10 2026 daemon.debug zeroblock[7535]: [ruleset_manager] <<< EXIT ruleset_refresh_community_lists() -> 0
Mon Feb 16 11:38:10 2026 daemon.err zeroblock[7535]: [lists_loader] Failed to load community index for v2 API
Mon Feb 16 11:38:10 2026 daemon.debug zeroblock[7535]: [http_client] Freed multi context
Mon Feb 16 11:38:10 2026 daemon.info zeroblock[7535]: [lists_loader] Downloaded lists, 1 errors
Mon Feb 16 11:38:10 2026 daemon.warn zeroblock[7535]: [config_builder] Download failed (1 errors), enabling auto_fallback two-stage via awg10
Mon Feb 16 11:38:10 2026 daemon.info zeroblock[7535]: [config_builder] Stopping sing-box before config generation...
Mon Feb 16 11:38:10 2026 daemon.info zeroblock[7535]: [config_builder] Restoring DNS for API requests...
Mon Feb 16 11:38:10 2026 daemon.debug zeroblock[7535]: [dns_manager] >>> ENTER dns_auto_restore()
Mon Feb 16 11:38:10 2026 daemon.info zeroblock[7535]: [dns_manager] No DNS backup found, nothing to restore
Mon Feb 16 11:38:10 2026 daemon.debug zeroblock[7535]: [dns_manager] <<< EXIT dns_auto_restore() -> 0

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

**2026-02-16T11:54:30 | Роман**
Zeroblock, ставить руками, настраивать. Есть авто настройка на бесплатные opera proxy, или воткнуть свою ссылку.

---

**2026-02-16T11:54:54 | Anna Bagler**
Zeroblock, свои ключи и домены, которые надо обходить.

---

**2026-02-16T11:57:56 | Anna Bagler**
По vpn/ссылкам vless и т.д. - интернет. Zeroblock - тут в темах, в wiki - мануал по нему.

---

**2026-02-16T11:59:05 | Семьдесят Семь**
что лучше для vless сервера zeroblock или podkop?

---

**2026-02-16T12:00:38 | Роман**
Zeroblock.

---

**2026-02-16T12:05:08 | Дмитрий Кобзарь**
У нас я так понял на выбор три приложения: podkop, zapret, zeroblock. С каким лучше заморочится

---

**2026-02-16T12:06:31 | Routerich**
Здравствуйте.
Podkop,zeroblock Это средства маршрутизации
а zapret это средство обхода DPI

---

**2026-02-16T12:13:27 | Anna Bagler**
Если у вас все работает, пусть работает. Если нет, прошивку свежую и zeroblock.

---

**2026-02-16T12:19:26 | Rustam Ikramov**
Да, спасибо. 
Zeroblock чем то лучше подкопа?

---

**2026-02-16T12:39:47 | 𝕾𝖊𝖗𝖌𝖊𝖎 𝕷𝖎𝖘𝖆𝖑𝖔**
нет файла zeroblock_0.6.2-r90_aarch64_cortex-a53
пожалуйста исправьте

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

**2026-02-16T12:56:41 | Виктор Миронов**
Добрый день!Есть вопрос по ZeroBlock, работает ютуб но не дискорд как посмотреть в чем проблема?

---

**2026-02-16T13:39:34 | Anna Bagler**
Если ничего на него не ставили, то тема Zeroblock Beta.

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

**2026-02-16T14:09:50 | Роман**
Так у вас Дискорда и нет в списках zeroblock.

---

**2026-02-16T15:24:34 | Routerich**
opkg remove zeroblock && rm /etc/config/zeroblock
затем заново поставить. но не понятно то там такого можно поломать

---

**2026-02-16T16:06:34 | Sahro IT**
Всем привет. Пылился значит РР на полке почти год. Смотрю на форуме вышел Zeroblock. Хотел поставить, попробовать. Проблема на скрине. Типа нет интернета. Но он есть и днс прописаны от гугла и клоуда. Что делал перед этим. Полный сброс, обновил прошивку на последнюю. Настроил интернет по PPOE и Wifi. Пытался вручную загрузить пакеты Zeroblock, ругается об отсутствии sing-box. В пакетах его нет, а обновление пакетов не работает. Как это победить?
PS Если открывать ссылки из строк, на которые ругается, на ПК всё открывается и загружается соответствующий файл.

---

**2026-02-16T16:20:07 | Anna Bagler**
Подкоп/zeroblock стоит?

---

**2026-02-16T16:39:01 | Михаил**
Внесу мою лепту в тестирование продукта. Резервный роутер cudy. Для тестирования. 2 секции - опера proxy и awg20 vpn. Естественно галка полной маршрутизации в настройках выключена и dns во вкладке расширенные настройки удалены. На роутере тестовая конфигурация с подпопом и зероблоком. Итак, если мета в списках опера, - sing-box забирает dns фейсбука на себя. А вот на секции awg20 беда, dns просачивается мимо sing-box. Картинку прикладываю. Далее тоже самое пробую в подкопе,  остановив zeroblock. В обеих секциях все норм - адреса dns sing-box.

---

**2026-02-16T16:40:23 | Михаил**
Протокол старта zeroblock: Starting ZeroBlock...
[ruleset_manager] API request failed (ret: 0, code: 400, size: 95)
[disable_fakeip] Failed to open dnsmasq config: /tmp/dnsmasq.d/zeroblock-awg20-meta.conf
[disable_fakeip] Failed to open dnsmasq config: /tmp/dnsmasq.d/zeroblock-awg20-twitter.conf
[zeroblock] ZeroBlock started successfully

---

**2026-02-16T18:12:50 | Роман**
Я нуб, zeroblock с vless на своих серверах работает, ЮАБ отключен, запрет 2 с конфигом по умолчанию (Ютуб) работает. 
Попробуйте поискать стратегии для того, что у вас не работает.

---

**2026-02-16T18:19:02 | Anna Bagler**
Zeroblock.

---

**2026-02-16T18:20:19 | Роман**
Если лапки то 5й скрипт. Если ручки - zeroblock и запрет 2 для Ютуба/Дискорда. 😁

---

**2026-02-16T18:39:58 | Routerich**
Здравствуйте.
Отследить все домены на которые он обращается и добавить их в Podkop/zeroblock

---

**2026-02-16T19:00:20 | Routerich**
Я имею ввиду через Podkop /zeroblock в полный прокси на крайний случай.

---

**2026-02-16T19:15:39 | Anna Bagler**
Ещё раз скрипт 5 запустить и руками ничего не трогать. Потом ещё раз эту диагностику. Если прошивка старенькая, то можно обновиться без сохранения и начать использовать zeroblock.

---

**2026-02-16T19:27:12 | Anna Bagler**
Отключите и остановите анблок, проверьте родительский контроль. Потом ставьте zeroblock и выбирайте в его секции awg список YouTube.

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

**2026-02-16T19:51:58 | Денис**
Проблема в том, что его нет в службах. Zeroblock накатил сразу после обновления без сохранений на 24.10.5. Есть скрипт?

---

**2026-02-16T20:04:08 | kk**
у него как раз роутеричный - routerich/packages.routerich/raw/24.10.5/base/
видимо что-то случилось при добавлении base в репо.
из апстрима на owrt cortex-a53 24.10.5 работает.

p/s +вам спасибо за debug логи в zeroblock =)

---

**2026-02-16T21:09:20 | Anna Bagler**
С LG головняк, долгий и мучительный, только @BFMVPoison подвластный. Для LG пробовать анблок, запрет1 с автоконфигуратором от Kissa. Или пускать через zeroblock.

---

**2026-02-16T22:06:13 | Anna Bagler**
Ставьте zeroblock по мануалу, засовывайте бокс в полную маршрутизацию, потом смотрите по портам.

---

**2026-02-16T22:21:00 | Ikа**
Ребят, помогите, пожалуйста, не могу понять в чем дело, в впн или настройки не докручиваю в роутере

Есть сайт, на котором блокируются по стране некоторые сериалы (пишет 404 server error), но если выбрать, например, Польшу, то все показывает.
В ВПН уверен, т.к. если тот же самый ключ вставляю в телефоне через приложение v2RayTun, то все работает на телефоне, а если вставляю его в секции (не важно, подпиской или чисто vless ключ) и указываю именно этот сайт для впн, то не работает все равно. Для теста, в эту секцию добавляю еще 2ip, он показывает что мое местоположение Польша, пробую в режиме инкогнито, чтобы кэш не мешал

У меня на чистую прошивку установлен только zeroblock 0.6.2-r30 и темная тема, в автонастройках еще zapret2

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

**2026-02-16T22:34:33 | Gomer Simpson**
ZeroBlock перезапуск, почистить кеш браузера, проверить в инкогнито.

---

**2026-02-16T22:41:28 | Ikа**
Правильно же делаю, вставляю их в пользовательские домены?
Я несколько раз применил, перезапустил zeroblock и на всякий даже перезагрузил роутер, проверяю также в новой вкладке инкогнито и все равно ошибка(

---

**2026-02-16T22:44:10 | Роман**
А вообще zeroblock работает?

---

**2026-02-16T23:25:18 | Павел Великов**
Я верно понимаю, что в Zeroblock нельзя сделать redundancy - при отказе одного из VPN перенаправить этот трафик другой
Не дает указать один и тот же список для 2х секций маршрутизации

---

**2026-02-16T23:35:03 | Павел Великов**
Так, запрет работает  одновременно с Zeroblock,  но требуется удалить секцию из ZB верно?

---

**2026-02-17T00:46:03 | Anna Bagler**
Шлем пустить по IP в zeroblock/podkop или не работает?

---

**2026-02-17T02:28:18 | Борис**
подскажите пожалуйста, откуда записывается файл /tmp/zeroblock/sing-box.d/01-experimental.json? Мне нужно отредактировать порт, на котором clash api работает (использую проксирование nginx на https). Пробовал отредактировать /etc/config/zeroblock (там тоже указан порт), но изменения не вступили в силу. Перезагружал через service zeroblock restart

---

**2026-02-17T02:49:17 | Борис**
очень-очень жаль. не помогает ни проксирование через nginx (часть ресурсов всё равно будто жёстко зашито на http и пытается из https качаться по http), и сертификат в clash api я не могу прописать, потому что такие параметры в uci не предусмотрены видимо. Чтобы их в конечном итоге в /tmp/zeroblock/sing-box.d/01-experimental.json записать

---

**2026-02-17T12:11:23 | Руслан**
Давно хотел попробовать zeroblock там ведь поддерживает?

---

**2026-02-17T17:01:11 | Anna Bagler**
Для YouTube пробуйте запрет2 и zeroblock.

---

**2026-02-17T17:04:49 | Anna Bagler**
Тема zeroblock beta, в закреплённых сообщениях файлы и мануал. Внимательно.

---

**2026-02-17T17:13:16 | Anna Bagler**
Навыки ваши начальные или продвинутые? Начальные - скрипт №5 из закрепов Интернета без границ. Продвинутые - закрепы темы Zeroblock.

---

**2026-02-17T17:24:29 | mrack**
как добавить taiscale0,стоит zeroblock..

---

**2026-02-17T18:44:50 | Андрей**
Анализ запущен: 2026-02-17 18:39:50
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
  Facebook IP:  198.18.0.82 | YouTube IP:  198.18.0.83
  Программы в автозапуске: zeroblock

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 198.18.0.83
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Внутреннее пересечение в zeroblock:
    zeroblock                 : Proxy (Условия: default)
    zeroblock                 : Proxy (Условия: default)
    Домены: googlevideo.com youtube.com 

  zeroblock          Proxy (prx url): !!!_russia_inside,geoblock,block,porn,news,anime,!!!_youtube,discord,meta,twitter,hdrezka,tiktok,telegram,!_cloudflare,cloudfront,hetzner,ovh,digitalocean,google_ai,google_play,roblox,hodca
  Версия zeroblock: 0.6.2-r91
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.10.1 (Прошивка: 24.10.5)
  CPU: 0.00 | RAM: 21% | NAND: 21% занято / 53.4M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

root@RouteRich:~# 
А что за пересечение доменов?

---

**2026-02-17T19:01:33 | Николаич**
Скажите откуда скачать файлы для установки ZeroBlock

---

**2026-02-17T19:03:11 | Kiss_My_Axe**
zeroblock                 : Proxy (Условия: default)
Вот это означает, что есть пересечения в юзерсписках доменов/подсетей/ip_адресов. Недопилено.
В общем смысле не так страшно, что в юзерсписке несколько раз встречается ютуб, например. Всё равно внутри одной секции маршрутизации.

---

**2026-02-17T19:23:29 | Anna Bagler**
Пробуйте отключить и остановить youtubeUnblock и поставить zapret2. Проверить. Если не поможет, то закрепы темы zeroblock и через него.

---

**2026-02-17T19:58:52 | vladimir**
Приветствую Вас! Сегодня получил еще два замечательных роутера!15 минут и оба отправились отцу и тестю в семью, поскольку те, заинтересовавшись открывающимися перед ними возможностями теперь станут выносить мозг нашей любимой техподдержке 🤗🤗🤗😂😂😂Клянусь-своими силами не допускать подобных безобразий и решать возможные возникающие проблемы своими силами, путем курения мануалов(Курение убивает😂😂😂)Ну а уж если и придется обратиться не откажите в любезности направьте в ZeroBlock или Zapret 2😂😂😂p.s("шепотом" правда моим отцам и podkop'a за глаза хватает👍👍👍)

---

**2026-02-17T20:18:24 | Симеона**
В ZeroBlock пинг в секции opera - 364ms и в секции awg10 -  486ms - это нормально? Все работает, только Zapret2 нигде не появился, хотя стоит галочка, что установлен. Сверху справа в интерфейсе надпись "Обновляется" очень долго висит. Нужно ждать, пока она уйдет?

---

**2026-02-17T20:31:41 | Anna Bagler**
Или подбирать стратегию долго и больно, или пробовать zeroblock и полную маршрутизацию, или приставку на андроиде. Если тв старый, приставка - лучший выход, омолодит ваш ТВ.

---

**2026-02-17T20:34:01 | Anna Bagler**
Пробуйте через zeroblock.

---

**2026-02-17T21:51:06 | Routerich**
пакеты  | полный мануал | списки | ру списки
ZeroBlock 0.6.4-r8:
  Clash/Mihomo YAML подписки
  Полная поддержка парсинга Clash/Mihomo YAML подписок. FSM-парсер на libyaml, поддержка протоколов: VLESS, VMess, Trojan, Shadowsocks, Hysteria2, SOCKS5, HTTP(wireguard нет и нужны тесты различных подписок).
  Вложенные блоки: ws-opts, grpc-opts, h2-opts, reality-opts, plugin-opts, ALPN. Автодетекция формата (YAML прямой + base64), fallback на URI-список.

  Исправления
  - Убран хардкод clash_api_port 9090(редактируется только в uci или конфиге)

  UI
  - Добавлены сброс настроек(не распространяется на секции и автонастройку)

  Тесты
  - Дополнены списки сообщества с github ITDog
#ZeroBlock

---

**2026-02-17T22:39:52 | Роман**
А типа -opkg remove zeroblock нет еще?

---

**2026-02-17T22:40:38 | Routerich**
rm /etc/config/zeroblock* && reboot

---

**2026-02-17T23:57:44 | Routerich**
а там что-то живое есть? zeroblock утверждает что нет

---

**2026-02-18T10:00:28 | Routerich**
Здравствуйте.
zeroblock достаточно.

---

**2026-02-18T10:05:19 | Ａｌｅｘａｎｄｅｒ**
Всем привет. Что за ZeroBlock?

---

**2026-02-18T10:06:00 | Роман**
Zeroblock, для Ютуба запрет 2, если телевизоры на закрытых ос - полностью проксировать.

---

**2026-02-18T10:11:00 | Routerich**
Здравствуйте
пускайте их тогда в Podkop/zeroblock

---

**2026-02-18T10:35:00 | Александр 🔴🔵**
Где почитать про Zeroblock??

---

**2026-02-18T10:35:54 | Andrey**
в Wiki лежит мануал. + тема zeroblock beta

---

**2026-02-18T10:43:34 | Иван**
Добрый день! Подскажите почему в службах не вижу ZeroBlock?

---

**2026-02-18T10:53:38 | Роман**
В закрепе темы zeroblock качаете пакеты, система - пакеты - обновить списки - установить 2 пакета. Сначала больший по размеру, затем меньший.

---

**2026-02-18T10:57:30 | Иван**
Допустимые ошибки? Это первый пакет большой Zeroblock

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

**2026-02-18T11:57:58 | Alex**
дорброго дня! сегодня собираюсь заменить роутер  домашний на РР - хотел поставить ZeroBlock  чтобы сразу быть так сказать в основном потоке развития - после прочтения мануалов и поиска   не понял  - для использования selfhosted awg 2.0 - нужно доустанавливать чтолибо ? или клиент встроенный сейчас в РР - понимает этот протокол?

---

**2026-02-18T12:14:33 | Routerich**
найти домены куда оборудование обращается и добавлять в Podkop/zeroblock в пользовательские домены

---

**2026-02-18T12:57:58 | Виталий**
Было бы интересно, вчера с пол тычка все завелось с zeroblock

---

**2026-02-18T14:48:38 | Anna Bagler**
Zeroblock и zapret2.

---

**2026-02-18T15:23:44 | Роман**
Zeroblock умеет так.

---

**2026-02-18T15:34:02 | Роман**
Не зная терминов не следует интересоваться openwrt вообще. Коротко zeroblock лучше. Длиннее расписывать нет смысла т.к вы не знаете терминов. Вам ответит любой в этом чате zeroblock лучше, а в чате itdoga скажут что podkop лучше. Вот и думайте.

---

**2026-02-18T17:27:09 | .**
Всем привет!) 
Друзья, подскажите пожалуйста, ZeroBlock и Podkop, в целом имеют равное назначение? Кто что юзает? 
Вкратце скажите, что будет попроще для освоения?
Podkop так понимаю чуть попроще, а ZeroBlock более жирный в плане функционала?

---

**2026-02-18T18:14:46 | Роман**
После более года пользования роутером думаю пора оставить отзыв. Первой моей моделью был роутер с 256 мб оперативной памяти, работает до сих пор отлично. После взял второй с 512 мб. Третий уже из последней партии. 
Дом, мама, и теперь старшая дочь будут на связи. 
Настроил буквально за 15 минут, запрет 2, zeroblock - всё работает как часики (конечно, долго тёрся в чатике впитывал знания 😁).
Большая благодарность всей команде RouteRich за создание, развитие, поддержку данного, очень нужного в наше время проекта. 
Отдельно хочу поблагодарить комьюнити данного сообщества - вы лучшие! Поможете в любой ситуации 👍

---

**2026-02-18T18:35:25 | Anna Bagler**
Оно будет, если блоков нет. Лучше посмотрите в сторону zeroblock.

---

**2026-02-18T18:38:48 | Андрей**
Zeroblock не тестил , на старом xiaomi ax3000t стоял подкоп и awg , устанавливал все сам сложно было.
Так советуете , zeroblock разберусь с ним сам? чтобы вас не мучить? Vless свой есть и awg свой есть

---

**2026-02-18T19:10:33 | Андрей**
При установке zeroblock такие ошибки это норм?

---

**2026-02-18T19:37:45 | Андрей**
А можно в zeroblock к примеру весь firefox отправить и как это сделать?

---

**2026-02-18T19:50:56 | Роман**
Если нет понимания что делать, лучше не трогать 😁
А так на чистую, новую  прошивку ставите zeroblock - галки на авто настройку, до кучи запрет 2 для Ютуба.

---

**2026-02-18T19:52:37 | Роман**
Для Ютуба запрет 2, для остального zeroblock.  Если лапки - скрипт 5 или бета.

---

**2026-02-18T19:53:00 | Anna Bagler**
Скрипт №5/бету или zeroblock. Интернет без границ - 5 для подкопа. Beta - бета-скрипт для подкопа. Zeroblock Beta - zeroblock.

---

**2026-02-18T20:00:07 | Роман**
В тему zeroblock напишете - помогут.

---

**2026-02-18T20:17:36 | Ivan Akhmatov**
Добрейшего. При установке zeroblock (ставил на относительно чистую систему - никаких скриптов не запускал, только вручную ставил ютубанблок) произошла непонятная штука: обновил списки, загрузил пакет, висело окно установки, но не появилось сообщения с результатами, окно установки просто закрылось. После этого роутер самостоятельно ушел в ребут. При установке люси для  зероблок ошибка 255, в установленных пакетах зероблок нет, но в процессах и автозагрузке он есть и судя по статусу запущен. Что могло пойти не так?

---

**2026-02-18T22:00:25 | Руслан**
Приветствую! Подскажите пожалуйста, хочу понять направление, в какую сторону двигаться и что изучить, получил сегодня роутер Routerich ax3000 и хочу настроить так, чтобы Дискорд, Ютуб и всё остальное работало, что для этого нужно? Zapret2 или zeroblock или podkop или что-то ещё?

---

**2026-02-18T22:13:35 | Роман**
Поиск доменов и ip:
IPV4OO
Хром - https://chromewebstore.google.com/detail/ipvfoo/ecanpcehffngcegjmadlcijfolapggal?hl=kk
Лиса - https://addons.mozilla.org/ru/firefox/addon/ipvfoo/
Включаем ВПН -> идём на сайт -> копируем домены в zeroblock/podkop.

Браузер
https://www.youtube.com/watch?v=rtXTaClSXR0
Андройд
https://www.youtube.com/watch?v=h7OUgOrezdQ
iOS
https://www.youtube.com/watch?v=-ePERMmabDA
Винда
https://www.youtube.com/watch?v=eIrD5XvDTto
Линукс
https://www.youtube.com/watch?v=TXAayoJ-vpY

---

**2026-02-18T22:21:22 | Anna Bagler**
Уровень ваших навыков? Высокий - как сказали выше, zeroblock. Низкий - настроить через Мастер и сюда https://t.me/routerich/3845/245550

---

**2026-02-18T22:25:22 | Руслан**
Получается подкоп лучше или лучше сразу изучить zeroblock и поставить его?

---

**2026-02-18T22:26:39 | Anna Bagler**
Вы без навыков не особо разберётесь с zeroblock. Но пробуйте, если верите в себя. Тогда внимательно мануал читайте.

---

**2026-02-18T23:35:00 | V I T Λ L Y**
А где взять zeroblock? У меня егл ни в службах ни в пакетах нет и не ищется...

---

**2026-02-18T23:40:31 | Роман**
Zeroblock принимает домены и ip адреса.

---

**2026-02-19T02:37:21 | вася778**
почему проверка routing_mark может выдавать:
grep: /tmp/zeroblock/conf.d/: No such file or directory ?

---

**2026-02-19T06:16:53 | Danil**
С такой же ситуацией столкнулся вчера после обновления. Были конфликты со старыми файлами (conffile) singbox, zeroblock и ещё что-то там. ZB после установки не запустился. Сначала удалил zapret2, так как думал, что это в нем проблема, но это не помогло. После этого и zapret2 через zeroblock не хотел устанавливаться. 
Решил действовать кардинально. Обновил прошивку до последней без сохранения настроек. Потом накатил zeroblock. Все заработало.

---

**2026-02-19T07:51:28 | Routerich**
Zeroblock, Podkop

---

**2026-02-19T09:17:45 | Роман**
Нормально всё со speedtest, с zeroblock тоже всё в порядке. Возможно (в мобильном приложении) что сам тест работает криво.

---

**2026-02-19T09:30:24 | Routerich**
Здравствуйте.
Система->Пакеты->Обновить списки->
потом скачать два файла из закрепа, установить сперва zeroblock, потом luci-app-zeroblock

---

**2026-02-19T10:26:36 | Игорь**
Потому что на телефоне появляются сервера, а в zeroblock пусто, хотя ссылка рабочая и она именно для sing-box вроде

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

**2026-02-19T11:44:22 | Routerich**
покажите 
nft list table inet zeroblock

---

**2026-02-19T13:24:03 | Anna Bagler**
Zeroblock или скрипт 5/бета. Закрепы этой темы, beta или zeroblock.

---

**2026-02-19T14:28:40 | Павел**
Я таки дико извиняюсь. Можете ссылку прислать на Zeroblock и мануал.

---

**2026-02-19T15:54:54 | Роман**
А можно просто установить zeroblock 😁

---

**2026-02-19T15:58:03 | Роман**
Ветка zeroblock, в закрепе файлы и инструкция.

---

**2026-02-19T16:01:14 | Кирилл**
Привет, установил на роутер zeroblock и zapret2. zeroblock ругался при диагностике на youtubeUnblock, вырубил его. И вроде как сейчас все работает (не знаю на сколько качественно еще), кроме телеги. подскажите пожалуйста как пофиксить телегу и что еще нужно сделать, чтоб было огонь)

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

**2026-02-19T17:19:03 | Святос**
Ветка ZeroBlock beta

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

**2026-02-19T17:46:46 | Вадим**
А такой глупый, но логичный вопрос. Zeroblock чем-то лучше подкопа для рядового юзера (ютуб, мета, нейронки)?

---

**2026-02-19T18:07:11 | Rom@n**
Пнул, не помогло
root@RouteRich:~# zeroblock update_lists
{"status":"updating","message":"Starting lists update..."}
{"status":"updating","message":"Checking DNS availability..."}
{"status":"updating","message":"DNS check passed"}
{"status":"updating","message":"Checking GitHub connectivity..."}
{"status":"updating","message":"GitHub check passed"}
{"status":"updating","message":"Downloading and processing lists..."}

========================================================================
         REMOVING ZEROBLOCK CRON JOB
========================================================================

✅ ZeroBlock cron job removed successfully
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: no lease, failing
{"status":"success","message":"Lists updated successfully"}

---

**2026-02-19T18:07:51 | Maxim =)))**
не могу установить zeroblock

---

**2026-02-19T18:16:43 | Роман**
Надо защиту от подкопа делать, при установке zeroblock писать - удаляй подкоп!

---

**2026-02-19T20:03:35 | Семьдесят Семь**
Программы в автозапуске: zeroblock= 

ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):  
OPERA (Proxy): ОФЛАЙН  
Запускаем остановленные службы, ожидайте...--
------------------------------------------------------------  
! Диагностика DNS (youtube.com):  
  Server:             127.0.0.1  
  Address:    127.0.0.1:53  
  Name:       youtube.com  
  Address: 198.18.0.179--
------------------------------------------------------------= 

СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):  
zeroblock       | RUNNING                        | РАЗРЕШЁН  
sing-box        | RUNNING (MANAGED BY ZB)        | РАЗРЕШЁН  
youtubeUnblock  | STOPPED                        | ОТКЛ= 

ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:  
zeroblock            vpn (prx url): geoblock,block,porn,anime,youtube,discord,twitter,telegram,google_ai,roblox  
Версия zeroblock: 0.6.4-r8  
zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8= 

СИСТЕМНЫЕ РЕСУРСЫ:  
LAN IP: 192.168.1.1 (Прошивка: 24.10.5)  
CPU: 0.10 | RAM: 21% | NAND: 37% занято / 42.3M доступно  
# ZeroBlock Monitor  
0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1  
# ZeroBlock Lists Update  
13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-02-19T20:51:53 | Maxim =)))**
Кстати, а это норм, что у меня в ZeroBlock в секции Opera стоит - {"type":"http","server":"127.0.0.1","server_port":18080}

А в сети в DHCP и DNS в перенаправлении - 127.0.0.1#5359

---

**2026-02-19T21:01:24 | Maxim =)))**
в диагностике ZeroBlock все норм, везде галки

---

**2026-02-19T21:12:53 | Routerich**
Здравствуйте.
А чем пользуетесь на роутере? Podkop, zeroblock имеется?

---

**2026-02-19T21:18:19 | Anna Bagler**
Тогда как было выше сказано, zeroblock удаляйте, и скриптом подкоп пробуйте.

---

**2026-02-19T21:25:45 | Maxim =)))**
Но в ZeroBlock все проверки проходит...

---

**2026-02-19T22:10:59 | Семьдесят Семь**
как переустановить zeroblock?

---

**2026-02-19T22:13:20 | Семьдесят Семь**
сервак показывает в zeroblock и на телефоне, я не понимаю как настраивать

---

**2026-02-19T22:19:19 | Boris Ivanov**
А где найти инструкцию как zeroblock поставить? Только получил роутер и пока ничего не понимаю

---

**2026-02-19T22:26:18 | Kiss_My_Axe**
В терминале роутера:
# полная переустановка ZeroBlock
opkg remove zeroblock luci-app-zeroblock
rm -rf /etc/config/zeroblock 
opkg update
opkg install zeroblock luci-app-zeroblock
Тьфу, блин. Это же зероблок, а не запрет.

---

**2026-02-19T22:31:19 | Семьдесят Семь**
маршрутизация,у меня ни тг не работает с включенным zeroblock ни ютуб ,ничего

---

**2026-02-19T22:47:58 | che**
Ребята. Openconnect на работает в работающим zeroblock или podkop. Предполагаю что как то связано с dns. Выключаю zb и доступ в интернет появляется. Как поправить настройку?

---

**2026-02-19T22:51:04 | Роман**
У вас и zeroblock и подкоп установлены. Выбирайте что то одно.

---

**2026-02-19T23:09:20 | Семьдесят Семь**
я переустановил zeroblock и теперь такая ошибка RPCError

RPC call to uci/get failed with ubus code 4: Ресурс не найден
  at handleCallReply (http://192.168.1.1/luci-static/resources/rpc.js:15:3)

---

**2026-02-19T23:18:15 | Роман**
Zeroblock всё может 😁

---

**2026-02-19T23:24:04 | ㅤㅤHer01n 4dd1ct10n**
Хм...поставил ZeroBlock, вроде всё работает, ошибок вроде нет но тот же ютуб не работает...

---

**2026-02-19T23:47:20 | Роман**
Я бы сброс сделал и только zeroblock и запрет 2 (для Ютуба) установил.

---

**2026-02-19T23:49:07 | Anna Bagler**
Сбрасывайте. Если сразу yt не заработает, отключайте и стопайте анблок, можно удалить вообще. И ставьте zeroblock.

---

**2026-02-19T23:57:57 | Kiss_My_Axe**
В любом случае после релиза придётся писать скрипт установки ZeroBlock.
Так как проще выдать ссыль, по которой ливнётся настроенная частично конфига (хотя бы в плане создания интерфейса авг10 и установки опера-прокси), чем объяснять кругами где взять, да как интерфейс создать.

---

**2026-02-20T00:13:02 | ­**
а планируется выпуск исходников ZeroBlock ? если да, то когда, если нет, то почему?

---

**2026-02-20T02:49:05 | Rashid**
и как его накатывать zeroblock?

---

**2026-02-20T09:18:17 | Routerich**
нет, он предлагает перезапускать openclash, а у вас  zeroblock

---

**2026-02-20T09:19:30 | Kiss_My_Axe**
Создать в зероблок секцию 20_00
Разместить в самом верху списка правил.
Настроить её на работу с БС как вам надо (просто ничего в неё не прописывать, кроме выходного канала).
Галку активации секции после проверки снять.
Сохранить - применить.

Код скопировать и вставить в терминал. Дальше он сам.
mkdir -p /opt/zb_scripts
cat > /opt/zb_scripts/zb_bs.sh << 'EOF'
#!/bin/sh
hour=$(date +%H)

case $hour in
    20)
        # Включаем в 20:00
        service zeroblock stop
        uci set zeroblock.20_00.enabled='1'
        uci commit zeroblock
        sleep 3
        service zeroblock start
        ;;
    07)
        # Отключаем в 07:00
        service zeroblock stop
        uci set zeroblock.20_00.enabled='0'
        uci commit zeroblock
        sleep 3
        service zeroblock start
        ;;
esac
EOF
chmod +x /opt/zb_scripts/zb_bs.sh
grep -q '/opt/zb_scripts/zb_bs.sh' /etc/crontabs/root || echo '0 * * * * /opt/zb_scripts/zb_bs.sh' >> /etc/crontabs/root
/etc/init.d/cron restart
Пару минут себе запрашивал. Вышло дольше.
Естественно я не предлагал вам писать код.

---

**2026-02-20T09:32:40 | Routerich**
Установите zeroblock, поставите галочки на автонастройки.
Если будет две секции, в секцию с awg10 закинете список Telegram

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

**2026-02-20T10:21:01 | Виктор Миронов**
Добрый день столкнулся  с проблемой Cloudflare ZeroBlock не помогает достучаться  с сервисами CloudFlare.  только сам CloudFlare Warp помогает преодолеть этот барьер. Но теряется слишком много скорости  с 450 мбит  до 60-80(в 5-6 раз скорость падает) как решить даннный вопрос?Не хотелось бы терять скорость в 5-6 раз

---

**2026-02-20T11:23:18 | Максим Бычков**
Хотел бы спросить возможно ли использовать ZeroBlock одновременно  с другими обходами (тот же Подкоп или запрет 2)?

---

**2026-02-20T12:08:27 | Kiss_My_Axe**
Переходите на ZeroBlock.

А пока:
Запустите это в терминале роутера, cкрин-фото-текст результата пришлите.
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/test_config_script/test_config_script_nightly)

---

**2026-02-20T12:24:03 | Сергей**
Забрал наконец-то и я свой роутер. Коробку чуть подмяли в доставке, но с внутренностями всё хорошо. На вид роутер нравится. Куча антенн добавляют уверенности в том, что это какое-то крутое современное устройство😁

С подобной системой работаю впервые. Да и вообще не силён в сетях, только общее представление. Раньше только слышал про owrt (или как оно там правильно😅). Роутер запустился без проблем, первоначальная настройка прошла легко и непринуждённо. Самое сложное было снять основной роутер от РТ, чтобы увидеть его Mac (решил сразу продублировать, чтобы потом не вспоминать, где и что пропустил).
После первоначальной настройки полез проверять, какие сайты работают... Оказалось, никакие😅 Удалил youtubeUnblock, накатил ZeroBlock и всё нужное мне завелось без проблем😌 Осталось теперь чуть подробнее вникнуть в настройки, чтобы понимать как быть, если чего-то не хватило)

Всей команде RR большое спасибо за проделанную работу и за то, что продолжаете активно развиваться. Вы превносите луч света в наши гнетущие будни интернета 😇

Для тех, кто всё ещё сомневается - берите. Надо. Но будьте готовы хотя бы слегка погрузиться в этот мир - прочитать мануалы, разобраться в терминологии, набраться внимательности и терпеливости.

---

**2026-02-20T12:36:58 | Александр**
Сидел два дня над роутером, но достиг цели 50/50.
Цель: Сделать чтобы VPN был только на одной WiFi сети 5Ггц.

Имеется купленная подписка с VPN. Установил ZeroBlock, в "Секции маршрутизации" создал секцию с VPN, добавил подписку.
В "Полностью маршрутизированные IP-адреса" добавил два IP адреса двух телефонов подключённых к 5Ггц. Всё работает для них через VPN, переключаю их на сеть 2.4Ггц, тоже все нормально уже без VPN, т.к. IP у них другой на 2.4ГГц.

Подключаю PS5 и TV на Android к сети 5Ггц, вношу их в Полностью маршрутизированные IP-адреса. Ок, для них тоже всё работает с VPN. Но, если их подключить к сети 2.4Ггц, их IP не меняется, соответственно они всё работает идут через VPN. 😭

---

**2026-02-20T12:38:23 | Anna Bagler**
Если вы их не добавляли в свои списки и их нет в выбранных списках сообщества, то они идут прямо. Вам тогда лучше в zeroblock.

---

**2026-02-20T15:26:31 | Ivan Matveev**
Полистал гайд по зероблоку из вики. По поводу самого процесса установки не нашел ни слова. В том смысле, что то вроде порядка установки или скрипта. Решил прошерстить саму ветку зероблока. По итогу, как я понял, этапы установки такие:
1. Обновление прошивки без сохранения настроек или сброс всех настроек.
2. Установка пакетов zeroblock и zeroblcok luci-app
Ну и далее пункт 4 из гайда с вики.
Остался только вопрос по поводу пункта 3 из гайда. Мне нужно самому установить/обновить указанные пакеты: амнезия тула, опера прокси и тд?

---

**2026-02-20T16:35:39 | Роман**
В ветке zeroblock, в закрепе.

---

**2026-02-20T16:57:22 | Oleg Mi**
Всем добрый день, получил недавно роутер, уже второй, вашей торговой марки. Роутеры классные, все нравится. Спасибо вам большое за вашу работу.
Последний с прошивкой 24.10.5 с «завода». Установил zeroblock, выключил и отключил автозапуск YouTubeunblock. Автонастройки по мануалу сделал, в секциях включил нужные списки. 
YouTube сначала закинул на opera, до вечера проработало отлично, грузилось все с бешеной скоростью на всех устройствах.  Вечером начало жестко тормозить и видосы стали очень долго прогружаться. Перенес YouTube  на awg10 стало значительно лучше. На ноуте в браузере YouTube грузиться отлично, кэш вовремя прогружается и видосы идут без остановок и прогрузок. 
Но, параллельно в это же время, на телефоне (iPhone) каждые 2-3 минуты видео останавливается на 30-60-90… и более секунд, потом внезапно прогружается большой кусок (смотрю по полоске) и продолжается опять 2-3 минуты и цикл повторяется.
Мониторил трафик, идет как положено через awg10.
Направьте пожалуйста куда копать. Перегруз интерфейса? Но ведь на ноуте нету такой проблемы…

---

**2026-02-20T17:13:12 | Ｅｘｃｌｕｓｉ v e**
Здравствуйте! Установил zeroblock, сначала вся запрещенка работала, сейчас перестало работать все!

---

**2026-02-20T18:44:30 | Anna Bagler**
Обновить прошивку
https://t.me/routerich/80283/352974?single
Потом это
https://t.me/routerich/173678/449069
Или zeroblock, если умения позволяют.

---

**2026-02-20T19:35:46 | Александр**
В ZeroBlock это наверное оно.

Но что с, что без этого. К созданной WiFi сети не удаётся подключится. Время аренды пробовал уменьшать.

---

**2026-02-20T19:44:33 | Bullet for my valentine Poison**
да, Zeroblock. У вас наверху же есть строчка фильтр. Слева. Впишите туда Zeroblock

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

**2026-02-20T19:57:18 | Denis**
Всем привет, недавно приобрел роутер. Подскажите чем отличается podcop, zeroBlock и скрипт 5?
Хочется настроить точечную маршрутизацию с возможностью докидывания динамических списков-ссылок по необходимости.

И в чем минусы включения раша инсайд по сравнению с составлением списка по частям по нужным сервисам?

---

**2026-02-20T19:58:24 | Routerich**
Здравствуйте.
Они оба подходят, просто zeroblock наша разработка и оперативно новые функции внедряем.

---

**2026-02-20T20:01:22 | Ｅｘｃｌｕｓｉ v e**
Установил два файла, в пакетах не появился zeroblock

---

**2026-02-20T20:02:49 | Routerich**
Система->Пакеты->zeroblock->установлено
Покажите

---

**2026-02-20T20:04:32 | Routerich**
В zeroblock можно

---

**2026-02-20T20:13:17 | Routerich**
Аналогично делается и для Zeroblock
https://podkop.net/docs/faq/#gostevaya-wi-fi-set-i-podkop

---

**2026-02-20T20:17:49 | Routerich**
в терминале 
rm /etc/config/zeroblock
ставьте заново

---

**2026-02-20T20:23:15 | Lelik**
Ну хз
Fri Feb 20 20:22:19 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Fri Feb 20 20:22:20 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[ruleset_manager] API request failed (ret: 0, code: 400, size: 95)
Fri Feb 20 20:22:25 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[ruleset_manager] API request failed (ret: 0, code: 400, size: 95)

---

**2026-02-20T20:26:16 | S W**
Здравствуйте, подскажите пожалуйста, поставил zeroblock, опера с личным vless спокойно встала, а awg не работает
Ошибка: [clash_api] /awg10/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 504

Куда копать? 
Роутер из последней ревизии (сестре взял, так как у меня дома стоит и ей решил купить)
Прошивка : RouteRich 24.10.5 (r29087-d9c5716d1d)
ZeroBlock  0.6.4-r8  
Последняя  0.6.4-r8  
LuCI App  0.6.4-r8  
sing-box  1.12.17  
Xray  25.1.30  
opera-proxy  v1.15.0  
OpenWrt  24.10.5  
Устройство  Routerich AX3000 v1 (24:0F:5E:)


Оператор beeline

---

**2026-02-20T20:35:24 | S W**
Нашел скрипт для анализа:
Анализ запущен: 2026-02-20 20:31:05
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
  Facebook IP:  31.13.72.36 | YouTube IP:  198.18.0.9

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.68 MB / ↑0.34 MB
  Пинг (ya.ru via awg10): 112.626 / 113.471 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock

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
  Запускаем остановленные службы, ожидайте...
Terminated
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 108.177.14.190
    Name:       youtube.com
    Address: 108.177.14.93
    Name:       youtube.com
    Address: 108.177.14.136
    Name:       youtube.com
    Address: 108.177.14.91
    Name:       youtube.com
    Address: 2a00:1450:4010:c01::5b
    Name:       youtube.com
    Address: 2a00:1450:4010:c01::88
    Name:       youtube.com
    Address: 2a00:1450:4010:c01::be
    Name:       youtube.com
    Address: 2a00:1450:4010:c01::5d
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | STOPPED                        | РАЗРЕШЁН
  sing-box        | STOPPED                        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Пересечение между zeroblock и youtubeUnblock:
    zeroblock                 : Proxy
    youtubeUnblock            : YouTube
    Домены: googlevideo.com youtube.com 

  zeroblock          Proxy (prx url): geoblock,block,youtube
  Версия zeroblock: 0.6.4-r8
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.40 | RAM: 23% | NAND: 40% занято / 40.6M доступно


Откуда появился youtubeUnblock не пониамю, вроде чисто zeroblock ставил начистый роутер. 


Есть смысл перепрошить роутер и попробовать все заново поставить?

---

**2026-02-20T20:43:30 | Kiss_My_Axe**
Разработчик обещал подумать. Если голубя дадут и от батареи отцепят.
Пока, при использовании ZeroBlock в опцию "Полностью маршрутизируемые IP" вписывайте стартовый адрес новосозданного интерфейса.
Если по гайду, то 192.168.200.1/24

---

**2026-02-20T20:44:14 | Ｅｘｃｌｕｓｉ v e**
Удалять zeroblock?

---

**2026-02-20T20:55:18 | Dim-soft**
Подскажите, реально запустить ZeroBlock на FriendlyElec NanoPi R3Sпод FriendlyWrt ?
автоустановка не сработает, но если opera proxy и zapret2 руками установить ?

---

**2026-02-20T20:55:45 | Kiss_My_Axe**
Я же вам писал, что кнопки "Воскресить" нет.
Переустановка ЗБ так же не вернёт всё "кагбыло", так как конфиги не переписываются.
Разработчик выдал вам команду для терминала:
rm -f /etc/config/zeroblock
которая удаляет конфиг.
После выполнения этой команды надо повторно, прям можно поверх, установить оба пакета заново.
Всё вернётся "кагбыло".
Затем галки итд.
СВОЁ в прокси вставите ЗАВТРА.
Сейчас всё по дефолту и проверка работоспособности.

---

**2026-02-20T21:22:34 | S W**
Снова прошу помощи, вроде большая часть нужных сервисов работает, но опять упал awg 
Анализ запущен: 2026-02-20 21:15:36
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  198.18.0.106 | YouTube IP:  198.18.0.107

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓0.00 MB / ↑0.22 MB
  Пинг (ya.ru via awg10): ERROR (OFFLINE)
  ! Ошибка: PING ya.ru (77.88.44.242): 56 data bytes
  Программы в автозапуске: zeroblock

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
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 198.18.0.107
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock          Proxy (prx url): geoblock,block,youtube,meta
  zeroblock              awg10 (vpn): discord,twitter,tiktok,telegram,google_ai
  Версия zeroblock: 0.6.4-r8
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.07 | RAM: 23% | NAND: 40% занято / 40.7M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

Нашел еще таие логи
[zeroblock] ZeroBlock stopped successfully
Fri Feb 20 21:16:09 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_discord Error: No such file or directory
Fri Feb 20 21:16:09 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_discord Error: No such file or directory
Fri Feb 20 21:16:09 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_discord Error: No such file or directory
Fri Feb 20 21:16:09 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_discord Error: No such file or directory
Fri Feb 20 21:16:09 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_discord Error: No such file or directory
Fri Feb 20 21:16:46 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_discord Error: No such file or directory
Fri Feb 20 21:16:46 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_discord Error: No such file or directory
Fri Feb 20 21:16:46 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_discord Error: No such file or directory
Fri Feb 20 21:16:46 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_discord Error: No such file or directory
Fri Feb 20 21:16:46 2026 daemon.err dnsmasq[1]: nftset inet zeroblock dns_awg10_discord Error: No such file or directory

как вообще отслеживать для быстрофиксов такое?

---

**2026-02-20T23:22:26 | Anna Bagler**
После установки именно zeroblock?

---

**2026-02-21T00:49:43 | Роман**
В ходе обсуждения родилась идея. Вот стоит у тебя подписка clash, она обновляется на гите. Допустим обновляется подписка криво, роутер перечитывает подписку и zeroblock не стартует? Или от этого тоже есть защита? Или это вообще не так работает?

---

**2026-02-21T03:27:07 | Борис**
Если кому-то интересно, вот как можно заставить clash api работать по https из-под панели управления роутером. Мой конфиг:
1) адрес роутера - https://192.168.1.1:81
2) порт clash api :9090 (задаётся в файле /etc/config/zeroblock или через uci)
3) конфигурация _lan.conf в nginx:

server {
  listen 81 ssl;
  listen [::]:81 ssl;
  server_name _lan;
        ssl_certificate /etc/nginx/conf.d/_lan.crt;
        ssl_certificate_key /etc/nginx/conf.d/_lan.key;
        ssl_session_cache shared:SSL:32k;
        ssl_session_timeout 64m;
  include restrict_locally;
  include conf.d/luci.locations;
  add_header Content-Security-Policy "upgrade-insecure-requests";
  error_page 497 https://$host:81$request_uri;
  access_log off;
}

server {
  listen 9443 ssl;
  server_name clash_api;

  ssl_certificate /etc/nginx/conf.d/_lan.crt;
  ssl_certificate_key /etc/nginx/conf.d/_lan.key;

  location / {
  proxy_pass http://127.0.0.1:9090;
  proxy_http_version 1.1;
  proxy_set_header Host $host;
  proxy_set_header Upgrade $http_upgrade;
  proxy_set_header Connection "upgrade";
  }
}
4) создано перенаправление портов в разделе Сеть -> Межсетевой экран -> Перенаправление портов (из lan 9090 в lan 9443, где сидит nginx)

Таким образом zeroblock пытается связаться с clash api по адресу https://192.168.1.1:9090 (благодаря директиве add_header Content-Security-Policy "upgrade-insecure-requests";), наш форвардинг портов отправляет его на 9443, а там встречает nginx с SSL, и проксирует запрос на http://:9090

---

**2026-02-21T03:44:40 | Борис**
А теперь, что мне не нравится в zeroblock:
1) я удаляю warp, как интерфейс, и удаляю из Internet detector зеленую плашку на Warp. В итоге после перезапуска зероблока варп опять появляется у меня в этих местах, т.е. утилита зачем-то пересоздаёт его, хотя он мне не нужен, и из секции я его тоже удалил...
2) нет возможности использовать config.json из постоянной памяти (ПЗУ) - я бы хотел перенести reality server на sing-box и отказаться от xray, но из-за того, что в zeroblock все конфиги хранятся только в оперативной памяти, я никаким образом не могу настраивать sing-box
3) изменения в секциях вступают в силу не сразу, используется какой-то кеш. иногда приходится ждать очень долго
4) если я использую активную секцию с подпиской vless reality, то все сервера будут отображаться на главной странице. Проблема в том, что я легко могу кликнуть на любую плитку с сервером и сразу подключиться к нему, но вот как отключиться? Я кликаю обратно на ту же плитку, ничего не происходит. Я просто прилип к этому серверу и никак не могу отключиться от него. Смена сервера из подписки (клик на другую плитку) тоже ничего не даёт (см. пункт 3, скорее всего из-за кеша я не могу менять сервера мгновенно)
5) если остановить service zeroblock stop, почему-то он останавливает xray тоже (хотя он мне нужен активным всегда как отдельная программа)

---

**2026-02-21T08:14:23 | Maxim =)))**
Всем привет, кто может подсказать, YouTube через браузер - работает нормально и стабильно, но через приложение прям затыки, то не грузит ни фига, то если и загрузит, то очень медленно.
Что можно сделать?
Стоит ZeroBlock.

---

**2026-02-21T11:08:04 | Anna Bagler**
Инструкция по прошивке для самых маленьких в wiki, внимательно по цвету usb. Прошивку можно взять в теме Прошивка или на оф. сайте. Потом скрипт №5 или бета. Или zeroblock.

---

**2026-02-21T11:40:44 | Борис**
2) ну вот я прямым текстом говорю, что мне нужно в пзу, потому что закрытая природа zeroblock в этом месте мне препятствует настраивать config.json. Я посмотрел в папке /tmp/zeroblock/sing-box.d конфиги, если их все склеить в один, получится от силы 3 килобайта... Здесь простым решением из разряда "и вашим и нашим" было бы сделать опцию (отдельную галочку?) чтобы можно было использовать локальный конфиг. Openwrt Nginx похожим образом работает - у него есть uci конфиг, но есть обычный файл-конфиг, и это настраивается, можно полностью отключить uci
3) про изменения в секциях оговорюсь: вкл/выкл секцию происходит сразу (так я решаю проблему #4, кстати). Но если я добавлю новый пользовательский домен в секцию (скажем, сайт 2ip.ru) и применю настройки, то программа будет долго принимать изменения. Мои изменения вступают в силу не сразу
4) зачем мне нажимать на другую плитку? Я хочу отключиться от сервера, серфить обратно от лица своего ip. Вы мне предлагаете вариант, что если мне надоел сервер, нужно просто выбрать другой... В итоге мне приходится отключаться от сервера таким образом, что я полностью вырубаю всю секцию с этой подпиской

P.S. переключение на другую плитку vless опять же не даёт результат мгновенно. Она может гореть зелёной, но на том же 2ip.ru я буду видеть старый адрес достаточно долго

---

**2026-02-21T11:54:12 | Anna Bagler**
Все от ваших навыков, лучше zeroblock, но если все плохо, то скрипт 5/бету.

---

**2026-02-21T11:55:15 | Routerich**
я не ваш карманный разработчик чтобы удовлетворять именно ваши хотелки и потребности. я могу рассмотреть вариант переноса конфигурации, но она все-равно будет пересоздаваться каждый раз перед стартом.
применение изменений работает через ucitrack и полностью перезапускает zeroblock и его компоненты.
вы хотите чтобы софт понимал что вы именно от него хотите на каком-то ментальном уровне? что значит отключиться от сервера и серфить от своего лица? вы используете средство точечной маршрутизации, это подразумевает статичные маршруты в конкретные точки, а не сейчас хочу, потом не хочу.
вы смотрите кеширующий 2ip, уже не раз обсуждалось, хотите проверять точно? curl 2ip.ru, курл не кеширует

---

**2026-02-21T12:27:53 | Роман**
Скоро zeroblock жирненьким станет, комбайном 😁

---

**2026-02-21T12:32:02 | Роман**
Ищите откуда игра тянет моды, прописывайте домены и ip в zeroblock/podkop.

---

**2026-02-21T12:44:16 | Anna Bagler**
Подкоп не поддерживает xhttp. Переходите на zeroblock.

---

**2026-02-21T12:45:27 | Роман**
Добавить домены и ip телеги в zeroblock/podkop, выбрать в списках сообщества телеграмм.

---

**2026-02-21T13:36:46 | ㅤㅤ**
Я наверное 100500, кто задает этот вопрос за последнее время, не нашел.

В последней партии роутеров как понимаю уже самая последняя прошивка и остается лишь накатить самый актуальный и рабочий скрипт №5? И ставить ZeroBlock пока смысла нет?

---

**2026-02-21T13:38:02 | Anna Bagler**
Лучше ставить zeroblock, если навыки позволяют или хотя бы желание есть и внимательность.

---

**2026-02-21T14:10:22 | Lelik**
я вчера пытсля zeroblock поставить, потом откатился из0за глюков, может с этим связапнно

---

**2026-02-21T14:21:14 | Александр**
Всё получилось. 🥳 Пришлось переключил интерфейс роутера на английский, так гораздо понятнее. Настроил гостевую сеть как в офф. гайде openwrt. 
Всё, гостевая теперь чистая, на других сетях VPN.

Вопрос по ZeroBlock, почему некоторые страны с роутера не пингуются и не коннектится к ним? Ну вот например Albania.(1 скрин). С телефона через happ подключается. С роутера недоступна. 
Некоторые отсутствуют(2 скрин). Russia в интерфейсе роутера отсутствует. А на телефоне, через happ подключается и работает. Пробовал скопировать отдельно ссылку на Vless RU из подписки и добавить на роутер, но не хочет роутер подключаться к Vless'y RU.

Не то что мне прям это нужно, та же Albania на роутере. Просто интересно, почему так? 🤔  Так-то 44 прокси из подписки пингуются и работают отлично.

---

**2026-02-21T14:26:14 | Александр**
Ну я первым делом пробовал, конечно. Подключается, но интернет пропадает. Пробовал и перезапуск ZeroBlock.
Russia вообще отсутствует в интерфейсе роутера.

---

**2026-02-21T14:32:54 | Lelik**
Странно, ну после zeroblock чето сломалось похоже

---

**2026-02-21T14:41:13 | Максим Бычков**
Пытаюсь полностью вернуть дефолтный конфиг Zeroblock. Но какого-то хрена пишет что у меня вообще он не установлен. Хотя на веб морде он есть, но от слова совсем не заводиться, из-за того что я решил закинуть Vless протокол в прокси

---

**2026-02-21T14:48:24 | Anna Bagler**
rm -f /etc/config/zeroblock

---

**2026-02-21T14:51:07 | Максим Бычков**
Мне кажется Zeroblock находится в другом месте. Ладно сейчас переустановлю

---

**2026-02-21T14:55:07 | Борис**
Я думаю потому что happ делает обычный tcp пинг, который всегда будет работать, если сервер включен в розетку, а zeroblock делает url test до указанного в настройках адреса. И по факту этот Албанский сервер не может его открыть

---

**2026-02-21T14:56:38 | ㅤㅤ**
Не хватает ума и времени разобраться с секциями. Изначально в ZeroBlock обе секции присутствуют и частично настроены. Но тот же GoogleAI не работает. Добавляется в Opera Proxy. Почему он не работает в AmneziaWG не ясно. И так со всеми секциями. Нужно над каждым списком экспериментировать. Или прочитать пару технических мануалов и разобраться, на что сейчас здоровья не хватает.

---

**2026-02-21T15:01:20 | Anna Bagler**
Навыки? Если есть желание, то идём в тему zeroblock, в закреплённых 2 файла и ссылка на полный мануал. Если нет, Интернет без границ и в закреплённых сообщениях находим скрипт №5, первый код с автоконфигурацией.

---

**2026-02-21T15:10:38 | Александр**
Проверил, xray установлен. Я его установил ещё когда ZeroBlock ставил. 🤷

---

**2026-02-21T15:15:15 | Борис**
Возможного у самой конфигурации используются специфические настройки, которые сейчас не поддерживаются в zeroblock. Попробуй этот ru сервер добавить не как vless:// ссылку, а указать режим "Сервер прокси" и выбрать "xray конфигурация outbound". Там ты можешь руками заполнить всё то, что тебе happ выдаст при попытке экспорта конфигурации в виде json (я не знаю, что happ использует под капотом - если тоже sing-box, то попробуй outbound конфигурацию sing-box)

---

**2026-02-21T15:21:45 | ㅤㅤ**
Тогда по какой причине секция РКН (Block) по-умолчанию находится в ZeroBlock - opera? И там же находится Geoblock.

---

**2026-02-21T16:15:54 | Александр**
Фух, разобрался. Короче, из подписки, когда вытягиваешь конфиг под одну локацию с помощью happ. Он в итоге какой-то битый выходит, что ссылка, что json.
Тут я поле в ЛК, так там можно было взять ключ под локацию и он заходит в ZeroBlock без проблем.

---

**2026-02-21T17:38:31 | ㅤㅤHer01n 4dd1ct10n**
почитал потыкался в настройки ZeroBlock, в итоге ютуб не работает совсем (страницы открывается видео не прогружается)...хотя как таковых ошибок не выдаёт

---

**2026-02-21T18:18:38 | ㅤㅤ**
Лично у меня странности с сохранение настроек в том же ZeroBlock. Сейчас перенастроил 6 роутеров подряд. В различных браузерах сталкивался с тем, что зачастую никакого отклика при нажатии на "Сохранить" не происходило. Помогало обновление страницы, и не всегда.

---

**2026-02-21T18:37:50 | Lelik**
Ну у меня и так уже их 30 в автопереборе, да и вот блокчек может после zeroblock сломался(

---

**2026-02-21T18:49:53 | Сергей**
Ребят, помогите разобраться в работе TailScale.
Получил роутер. Установил ZeroBlock. В локальной сети всё заработало (и на телефоне, и на ПК). 
Решил попробовать настроить удаленный доступ, чтобы нужный мне интернет был везде...

Создал сеть, получил и сохранил все ключи. 
Проверил пакеты из инструкции на роутере - уже установлено, обновлений нет. 
Перешел в VPN → Tailscale. Прописал ключ авторизации, нажал галочку включить, применил. Статус - Подключено. Выше надпись "Tailscale РАБОТАЕТ". В расширенных настройках поставил галочку "Узел выхода", применил. 
В ZeroBlock добавил во входящие интерфейсы tailscale0.
Установил приложение на андроид, добавил там сеть по инструкции. Отображаются 2 устройства (RR и андроид). ВПН на телефоне подключен. 

В панели управления remote поставил галку у роутера на Exit Node. Подождал некоторое время (уже минут 20) - не работают нужные сайты на телефоне при отключении WiFi. 
При этом ZeroBlock в диагностике показывает всё отлично, на роутере в Tailscale в устройствах видно андроид, какой-то трафик с него идёт. 

Я что-то упускаю?

---

**2026-02-21T18:58:55 | Lelik**
А где можно глянуть какой доп софт ставится вместе с zeroblock?

---

**2026-02-21T19:44:57 | Роман**
Zeroblock не сложный. Ну не особо 😁

---

**2026-02-21T20:03:44 | В.**
Всё равно ZeroBlock в списке служб не появляется

---

**2026-02-21T20:06:36 | В.**
zeroblock_0.6.4-r8_aarch64_cortex-a53

мы же это загружаем после обновления списков через "загрузить пакет"?

---

**2026-02-21T20:46:29 | Марсель Сайфиев**
Ребят, сразу извиняюсь за глупый вопрос. Но тут появились темы про zapret2 и zeroblock. На что стоит переходить? Или лучше оставаться на стандартных версиях?

---

**2026-02-21T20:57:44 | Роман**
Было такое даже со своим сервером. Перешёл на zeroblock - всё нормализовалось.

---

**2026-02-21T21:20:20 | В.**
Как организиовать раздельное туннелирование по устройствам (ТВ, ПК, смартфон, телевизор и т.п.), используя Xray через ZeroBlock?

---

**2026-02-21T21:21:52 | Максим Бычков**
Привет вновь всем. У меня возник вопрос. Я пользуюсь Zeroblock, и меня всё более менее устраивает. Но есть одно но, я хотел бы сыграть в МК1 с онлайн функциями. Для этого я специально менял днс на самом компьютере, но при этом блокировка оставалась в силе. И только тогда, когда я закинул в одну из секций полностью IP компа то все работает. Вопрос, я могу оставить днс сервера на уровне компа, без закидывания в секции?

---

**2026-02-21T21:35:08 | Максим Бычков**
Привет вновь всем. У меня возник вопрос. Я пользуюсь Zeroblock, и меня всё более менее устраивает. Но есть одно но, я хотел бы сыграть в МК1 с онлайн функциями. Для этого я специально менял днс на самом компьютере, но при этом блокировка оставалась в силе. И только тогда, когда я закинул в одну из секций полностью IP компа то все работает. Вопрос, я могу оставить днс сервера на уровне компа, без закидывания в секции?

---

**2026-02-21T21:35:42 | Viktor Agafonov**
детальная инструкция по zeroblock, смотрим, впитываем, дополнения приветствуются. upd 23:10 20.02.2026

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

**2026-02-21T21:54:21 | Александр**
Ок. Убрал галку, добавил 1  домен.

Пока всё так же. 
Телефон ходит в сеть без обходов, Web YouTube не грузит. Сайты определения IP определяют мою локацию.

ZeroBlock перезапускал.

---

**2026-02-21T22:12:47 | Роман**
Добавить домены сервера в zeroblock/podkop.

---

**2026-02-21T22:25:54 | Gomer Simpson**
```[config_builder] Download failed (5 errors), enabling auto_fallback two-stage via VLESS_random
[http_client] Failed after 0 retries: https://zeroblock.routerich.ru/api/v2/community-lists/telegram (curl=35, http=0)
[http_client] Failed after 0 retries: https://zeroblock.routerich.ru/api/v2/community-lists/cloudflare (curl=0, http=404)
[http_client] Failed after 0 retries: https://zeroblock.routerich.ru/api/v2/community-lists/twitter (curl=35, http=0)
[http_client] Failed after 0 retries: https://zeroblock.routerich.ru/api/v2/community-lists/tiktok (curl=35, http=0)
[http_client] Failed after 0 retries: https://zeroblock.routerich.ru/api/v2/community-lists/google_ai (curl=35, http=0)
[lists_loader] Failed to download v2: /tmp/zeroblock/rulesets/twitter_domains.json
[lists_loader] Failed to download v2: /tmp/zeroblock/rulesets/tiktok_domains.json
[lists_loader] Failed to download v2: /tmp/zeroblock/rulesets/cloudflare_domains.json
[lists_loader] Failed to download v2: /tmp/zeroblock/rulesets/google_ai_domains.json
[lists_loader] Failed to download v2: /tmp/zeroblock/rulesets/telegram_domains.json
[config_builder] Some lists failed to download (5 errors)
[lists_loader] v2 community list has no data files: twitter
[lists_loader] Section VLESS_random: list unavailable: twitter
[lists_loader] v2 community list has no data files: tiktok
[lists_loader] Section VLESS_random: list unavailable: tiktok
[lists_loader] v2 community list has no data files: cloudflare
[lists_loader] Section VLESS_random: list unavailable: cloudflare
[lists_loader] v2 community list has no data files: google_ai
[lists_loader] Section VLESS_random: list unavailable: google_ai
[lists_loader] v2 community list has no data files: telegram
[lists_loader] Section awg10: list unavailable: telegram
[zeroblock] ZeroBlock started successfully
Sat Feb 21 22:09:47 2026 user.notice ucitrack: Setting up /etc/config/zeroblock reload trigger for non-procd /etc/init.d/zeroblock```

---

**2026-02-21T22:34:24 | Viktor Agafonov**
пошел в иинструкцию, zeroblock и luci-app-zeroblock в списке пакетов нет. пошел в ветку с зероблоком бета, luci-app-zeroblock_0.6.4-r39_all.ipk попробовал его установить через загрузку, получил ошибку:
Выполнение операции
opkg install /tmp/upload.ipk
Unknown package 'luci-app-zeroblock'.
Ошибки
Collected errors:
 * pkg_hash_check_unresolved: cannot find dependency zeroblock for luci-app-zeroblock
 * pkg_hash_fetch_best_installation_candidate: Packages for luci-app-zeroblock found, but incompatible with the architectures configured
 * opkg_install_cmd: Cannot install package luci-app-zeroblock.
Команда opkg install завершилась с ошибкой с кодом 255.

---

**2026-02-21T22:39:39 | Роман**
В ветку zeroblock пишите, тут бета.

---

**2026-02-21T22:53:18 | Mallory**
RouteRich 24.10.5 r29087-d9c5716d1d RR-3.9.0 / LuCI openwrt-24.10 branch 26.039.68875~ec3d818

Installing zeroblock (0.6.4-r39) to root...
Installing kmod-inet-diag (6.6.119-r1) to root...
Downloading https://github.com/routerich/packages.routerich/raw/24.10.5/core/kmod-inet-diag_6.6.119-r1_aarch64_cortex-a53.ipk
Installing sing-box-tiny (1.12.17-r1) to root...
Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/sing-box-tiny_1.12.17-r1_aarch64_cortex-a53.ipk
Configuring kmod-inet-diag.
Configuring sing-box-tiny.
Configuring zeroblock.


udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: no lease, failing
Collected errors:
 * resolve_conffiles: Existing conffile /etc/config/zeroblock is different from the conffile in the new package. The new conffile will be placed at /etc/config/zeroblock-opkg.

opkg install /tmp/upload.ipk
Installing luci-app-zeroblock (0.6.4-r39) to root...
Configuring luci-app-zeroblock. 

TypeError
Cannot convert undefined or null to object

---

**2026-02-21T22:56:09 | Dark Ghost**
Поскольку голубей Fresa выдавать перестали, будем подкармливать свежими багами-жучками... 😊
Конкретно зовущимися "Не удалось проверить: Failed to fetch"

Ситуация - обновил прошивку с 23.05.05 до 24.10.05. 
Вторым шагом натянул zeroblock_0.6.4-r8_aarch64_cortex-a53.ipk.
Полюбовался на дефолтные opera и avg10 в панели управления (амнезия при этом показывала вполне разумное для мобильного инета число ms ), добавил свой vless.
Инет в локалке исчез.
Детектор продолжал показывать, что, вообще-то со стороны WAN он есть.
Полез в диагностику - там всё хорошо, кроме того самого  Failed to fetch.

---

**2026-02-21T23:01:48 | Дима**
подозреваю у других так же
Uncaught (in promise) TypeError: can't convert null to object
    render http://192.168.2.1/luci-static/resources/ui.js:39
    renderWidget http://192.168.2.1/luci-static/resources/form.js:282
    promise callback*render http://192.168.2.1/luci-static/resources/form.js:262
    renderChildren http://192.168.2.1/luci-static/resources/form.js:36
    renderOptions http://192.168.2.1/luci-static/resources/form.js:92
    renderUCISection http://192.168.2.1/luci-static/resources/form.js:89
    render http://192.168.2.1/luci-static/resources/form.js:161
    renderChildren http://192.168.2.1/luci-static/resources/form.js:36
    renderContents http://192.168.2.1/luci-static/resources/form.js:50
    promise callback*render http://192.168.2.1/luci-static/resources/form.js:50
    render http://192.168.2.1/luci-static/resources/view/zeroblock/zeroblock.js:144
    promise callback*__init__ http://192.168.2.1/luci-static/resources/luci.js?v=26.039.68875~ec3d818-1771703218:139
    super http://192.168.2.1/luci-static/resources/luci.js?v=26.039.68875~ec3d818-1771703218:15
    ClassConstructor http://192.168.2.1/luci-static/resources/luci.js?v=26.039.68875~ec3d818-1771703218:5
    compileClass http://192.168.2.1/luci-static/resources/luci.js?v=26.039.68875~ec3d818-1771703218:175
    promise callback*compileClass http://192.168.2.1/luci-static/resources/luci.js?v=26.039.68875~ec3d818-1771703218:171
    promise callback*require http://192.168.2.1/luci-static/resources/luci.js?v=26.039.68875~ec3d818-1771703218:177
    instantiateView http://192.168.2.1/luci-static/resources/ui.js:373
    <anonymous> http://192.168.2.1/cgi-bin/luci/admin/services/zeroblock:63
    promise callback* http://192.168.2.1/cgi-bin/luci/admin/services/zeroblock:62

---

**2026-02-21T23:22:24 | Anna Bagler**
youtubeUnblock может не помочь. Вам нужен zeroblock/podkop как средство точечного обхода.
На роутере есть URL-loger.

---

**2026-02-21T23:29:17 | Kiss_My_Axe**
Все ошибки при массовом применении свеженьких правил для nft.
Ругается, что отсутствует открывающая скобка '{'.
Возможно какой-то модуль при установке поверх не переписался, или типтаво.

Сделать бэкап.
Вынести ZB через манагер пакетов, /etc/config/zeroblock удалить и установить всё заново.

---

**2026-02-21T23:33:50 | Dark Ghost**
Застыдил...
Нашёл zeroblock_0.6.4-r39_aarch64_cortex-a53.ipk, установил поверх, включил обратно awg10
Задержки немного снизились, но это не показатель, ибо до завтра - на мобильном инете, со всеми вытекающими.
 awg10 - всё так же N/A, но эффект  "Failed to fetch" исчез, тьфу-тьфу.

---

**2026-02-21T23:56:22 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.6.4-r44:
  Исправления:
  - Очистка dnsmasq ДО удаления nft таблицы + принудительный restart
  - При автозагрузке секций учитываются пользовательские domain/subnet
  - Не блокировать старт при отсутствии секций если автозагрузка секций включена
  - Исправления в luci(Cannot convert undefined or null to object)
#ZeroBlock

---

**2026-02-22T00:12:20 | DD**
аналогичные проблемы. переходим на zeroblock?

---

**2026-02-22T00:47:50 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.6.4-r46:
  Исправления:
  - Автозагрузка секций ломала пользовательские списки domain/subnet
#ZeroBlock

---

**2026-02-22T01:27:29 | Figaro**
в последнее время youtube стал подтормаживать. Работает, но не быстро и не стабильно. Опять решил поковыряться в настройках, пообновлять, попробовать опять zeroblock .
C 5 вечера ставлю, настраиваю, сношу, переделываю. Решил воспользоваться deepseek в качестве ИИ помощника. В конце концов сломал ВСЁ. 
Плюнул на эксперименты и снова перепрошил роутер и просто запустил скрипт для обхода блокировок. Всё. Работает
1й час ночи. я наконец-то перестал мучать роутер и себя. У меня впереди 2 выходных, а всем спок ночи и быстрого инета

---

**2026-02-22T09:17:13 | Dmitriy**
ZeroBlock 0.6.4-r44 исправило проблему

---

**2026-02-22T09:55:01 | Симеона**
У меня ZeroBlock. Его переустановить?

---

**2026-02-22T10:43:15 | Anna Bagler**
Попробуйте отключить автонастройку warp и мониторинг интерфейса в zb. И можете писать о проблемах в теме самого zeroblock. Вам там быстрее ответят.

---

**2026-02-22T10:49:34 | Александр**
Да я как бы и не спорить. 😁 Просто опять лезть, курочить. И понять, что это не то. Не хочу.
У меня VPN подпиской. Т.е. ZeroBlock по любому нужен.
маркировкой трафф в фаерволле и последующим перенаправлением
Ради интереса зашёл по этим разделам, для меня это всё тёмный лес. Я то гостевую сеть смог сделать только по офф гайду openwrt.

---

**2026-02-22T10:52:54 | Дима**
RouteRich 24.10.5 r29087-d9c5716d1d RR-3.9.0 / LuCI openwrt-24.10 branch 26.039.68875~ec3d818
Подскажите, что я делаю не так?
1. Установил zeroBlock r46 на чистый роутер Routerich AX3000 v1
2. Сделал автонастройку
3. Включил CIDR списки сообществ
Вроде все поставилось, но заблокированные сайты не работают, например ютуб

---

**2026-02-22T11:55:33 | Роман**
Ставьте zeroblock и пишите в соответствующую тему, разработчик в теме - будет больше помощи. 
Желательно на чистый роутер.

---

**2026-02-22T12:49:43 | STIG**
Какой zeroblock нужно устанавливать. Первый или второй?

---

**2026-02-22T12:53:10 | Anna Bagler**
Сначала zeroblock..., а потом luci-app...

---

**2026-02-22T13:08:58 | Виктор Самарский**
Добрый день, долгое время сидел сначала на 5, затем на бета скрипте. В последнее время он стал плохо работать у меня. решил попробовать ZeroBlock. Обновил прошивку чистым способом. Обновил пакеты, загрузил последний ZeroBlock и luci. Получил вот такое. ZroBlock не запускается, перезагрузки и сброс не дали результатов, он повторился. Что делать?

---

**2026-02-22T13:37:23 | ㅤㅤ**
Каким образом можно заставить работать gemini.google.com при использовании dns.nextdns.io? Прописать его в DNS ZeroBlock? В этом случае он отказывается работать с персональным вида  https://dns.nextdns.io/*****

---

**2026-02-22T13:37:40 | Владимир Волков**
Чисто интерфейсно отличий там почти нет, может ему надо полежать
https://docs.routerich.ru/ru/remote#%D0%B4%D0%BB%D1%8F-routerich-%D1%81-zeroblock

---

**2026-02-22T14:46:37 | Сергей**
+ тоже весь день тг тупит через awg. При этом остальное из секции работает нормально. 
Ночью обновил zeroblock, по-быстрому проверил списки и успокоился. 
До обновления работал отлично.

---

**2026-02-22T15:03:44 | I5EEYOU**
Всем привет!) Установил я zeroblock, некоторые сайты теперь работают, но при этом не работает blizzard, он заблочен провайдером, что надо сделать чтоб он заработал?

---

**2026-02-22T15:37:52 | I5EEYOU**
Подскажите пожалуйста куда надо капать) Я установил zeroblock, все работает, но у меня есть блокировка от моего провайдера на blizzard. Как я могу это обойти?

---

**2026-02-22T15:38:43 | Yury Kuzmenko**
2 пакета надо установить 
Зероблок
Luci app zeroblock

---

**2026-02-22T15:47:27 | I5EEYOU**
Подскажите пожалуйста куда надо капать) Я установил zeroblock, все работает, но у меня есть блокировка от моего провайдера на blizzard. Как я могу это обойти?

---

**2026-02-22T15:49:28 | XapXan@27RUS**
Здравствуйте. Важно - все работает. Прошивка 24.10.5. После обновления до 24.10.5 (ставил начисто), пытался подтянуть настройки из бекапа. Сломалось обновление пакетов, ну да ладно - сбросил и настроил ручками. Подкоп через 5 скрипт из беты. Сейчас все работает, но есть одно но - ролики на Ютуб грузятся замечательно, а вот стримы зависают и порой загрузка останавливается. Чукча писатель. Вопрос вот какой - если переходить с решения на "подкопе" на "zeroblock" какой примерно порядок действий? Подкоп нужно удалять?

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

**2026-02-22T17:14:32 | Роман**
Надёжнее zeroblock, несколько своих серверов в url test. Так надёжнее.

---

**2026-02-22T17:17:24 | Святос**
opkg_install_cmd: Cannot install package zeroblock.
make[2]: *** [Makefile:234: package_install] Error 255
make[1]: *** [Makefile:171: 

Понятно, собрать с ним низя всё ещё

---

**2026-02-22T17:22:18 | Routerich**
opkg_install_cmd: Cannot install package zeroblock.

---

**2026-02-22T17:27:01 | Routerich**
Cannot install package luci-app-zeroblock
  Cannot install package nfqws
  Cannot install package nfqws2
Это тоже твое ?

---

**2026-02-22T17:43:10 | Kiss_My_Axe**
ZeroBlock. Он кушает такое.

---

**2026-02-22T17:54:45 | Routerich**
Здравствуйте

В Podkop/zeroblock в зависимости от того, что используете.

---

**2026-02-22T17:59:16 | Anton**
А что советуете использовать podkop или zeroblock? Роутер только получил, настроил запрет. Но для нескольких ресурсов (git, intellij, chatgpt, Claude code) хочу настроить через впн. Ключ vless уже имеется - до покупки роутера юзал квн на пк под весь трафик

---

**2026-02-22T18:01:12 | Роман**
Zeroblock, свои фишки, разработчик в чате.

---

**2026-02-22T18:33:12 | Kirill Y**
Подскажите пожалуста, в разделе zeroblock -awg10- отключить fakeIP галка должна стоять или нет?

---

**2026-02-22T18:39:33 | Владимир Волков**
24.10.5-3.9.0, преднастроенный авг10 из ЗБ

Добавляем домен, фейк выключен, сохранить.
Сохранить, применить.
logread -  [zeroblock] ZeroBlock started successfully

nslookup - 198.18.1.56, дичь, но предположим. И эта запись даже попала в сет (хотя до этого кучу раз не попадала, поэтому я её даже выносил в отдельную секцию).
Как тут оказалось фейкование?

---

**2026-02-22T18:52:26 | Роман**
Нет, нужны домены сайта. Ipv4oo в хром и ВПН, заходите на сайт - смотрите домены, заносите в zeroblock.

---

**2026-02-22T19:13:58 | Алексей**
Заказал 18 февраля, 22 уже получил. Это мой второй роутер. Установил его у родителей вместо Keenetic Giga, настроил ZeroBlock, весь интернет разблокировался. Добавил свои домены, всё что нужно стало открываться. У себя оставил подкоп, с ним тоже всё работает. Лучший роутер на данный момент! 🏆🚀👍

---

**2026-02-22T20:19:24 | Kirill ☕️**
Collected errors:
 * check_conflicts_for: The following packages conflict with sing-box-tiny:
 * check_conflicts_for:  sing-box * 
 * opkg_install_cmd: Cannot install package zeroblock.

---

**2026-02-22T20:46:16 | Роман**
В ветке zeroblock скачать файлы из закрепа, установить через пакеты.

---

**2026-02-22T21:03:11 | Kirill ☕️**
Анализ запущен: 2026-02-22 21:02:04
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
  Facebook IP:  31.13.72.36 | YouTube IP:  64.233.163.190
  Программы в автозапуске: zeroblock

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:             127.0.0.1
    Address:    127.0.0.1:53
    Name:       youtube.com
    Address: 2a00:1450:4010:c03::88
    Name:       youtube.com
    Address: 2a00:1450:4010:c03::5d
    Name:       youtube.com
    Address: 2a00:1450:4010:c03::be
    Name:       youtube.com
    Address: 2a00:1450:4010:c03::5b
    Name:       youtube.com
    Address: 209.85.233.93
    Name:       youtube.com
    Address: 209.85.233.190
    Name:       youtube.com
    Address: 209.85.233.91
    Name:       youtube.com
    Address: 209.85.233.136
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  youtubeUnblock  | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Пересечение между zeroblock и youtubeUnblock:
    zeroblock                 : vless
    youtubeUnblock            : YouTube
    Домены: googlevideo.com youtube.com 

  zeroblock          vless (prx url): ai,torrent,youtube
  Версия zeroblock: 0.6.4-r46
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.4)
  CPU: 0.30 | RAM: 19% | NAND: 20% занято / 53.1M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

root@RouteRich:~#

---

**2026-02-22T21:17:19 | Роман**
Я бы сбросил и zeroblock по новой установил 😁

---

**2026-02-22T21:22:55 | Роман**
Ну явно не просто так после подкопа не работает zeroblock, я с подкопа ушёл - сброс сделал и всё хорошо было. Даже сегодня роутер на 256 старого образца настраивал - всё с пол пинка завелось.

---

**2026-02-22T21:27:06 | Nikita**
Анализ запущен: 2026-02-22 21:24:58
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------

= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  157.240.205.35 | YouTube IP:  209.85.233.93

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓0.82 MB / ↑0.07 MB
  Пинг (ya.ru via awg10): 30.122 / 44.669 ms (2 из 10 потеряно)
  Программы в автозапуске: zeroblock

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Внутреннее пересечение в zeroblock:
    zeroblock                 : awg10 (Условия: default)
    zeroblock                 : awg10 (Условия: default)
    zeroblock                 : awg10 (Условия: default)
    Домены: googlevideo.com youtube youtube.com 

  zeroblock              awg10 (vpn): ai,discord,googleplay,messengers,meta,repo,socials,tools,youtube,cdn_azure,cdn_github
  Версия zeroblock: 0.6.4-r46
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 3.96 | RAM: 25% | NAND: 23% занято / 52.1M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1


Что здесь не так сделал? подскажите пожалуйста

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

**2026-02-22T21:57:58 | Роман**
Zeroblock итак использует sing box tiny.

---

**2026-02-23T00:40:11 | Routerich**
а вот это вариант повторить?
Mon Feb 23 00:47:06 2026 daemon.warn zeroblock[14170]: [clash_parser] Proxy limit reached (150)
Mon Feb 23 00:47:09 2026 daemon.err zeroblock[14170]: [nft_wrapper] nft apply error: Error: Could not resolve hostname: Name has no usable address add table inet zeroblock                                            ^^^^^^^^^^^^^^^
Mon Feb 23 00:47:09 2026 daemon.err zeroblock[14170]: [nft_manager] Batch apply failed

---

**2026-02-23T02:46:42 | Борис**
неа, не взлетело. вот такой у меня файл /etc/zeroblock/sing-box.d/custom-inbounds.json (начинается с фигурных скобок и содержит вначале контент оригинальной секции inbounds из /tmp...):

{
  "inbounds": [
    {
      "type": "tproxy",
      "tag": "tproxy-in",
      "listen": "127.0.0.1",
      "listen_port": 2154
    },
    {
      "type": "tproxy",
      "tag": "tproxy-in6",
      "listen": "::1",
      "listen_port": 2154
    },
    {
      "type": "direct",
      "tag": "dns-in",
      "listen": "127.0.0.42",
      "listen_port": 53
    },
    {
  "type": "vless",
  "tag": "vless-in",
  "listen": "127.0.0.1",
  "listen_port": 10443,
  "users": [
    {
      "uuid": "***",
      "flow": "xtls-rprx-vision",
      "name": "normis"
    }
  ],
  "tls": {
    "enabled": true,
    "server_name": "m.vk.com",
    "reality": {
      "enabled": true,
      "handshake": {
        "server": "m.vk.com",
        "server_port": 443
      },
      "private_key": "***",
      "short_id": [
        "***",
        "***"
      ]
    }
  }
}
  ]
}

---

**2026-02-23T02:52:10 | Kiss_My_Axe**
root@roskomnadzor:~# date && echo "" && logread | grep -n '\[zeroblock\] Starting ZeroBlock\.\.\.'
Mon Feb 23 02:51:50 MSK 2026

30:Sun Feb 22 01:08:31 2026 daemon.err zeroblock[26244]: [zeroblock] Starting ZeroBlock...
77:Sun Feb 22 01:30:10 2026 daemon.err zeroblock[31495]: [zeroblock] Starting ZeroBlock...
121:Sun Feb 22 01:30:27 2026 daemon.err zeroblock[32412]: [zeroblock] Starting ZeroBlock...
165:Sun Feb 22 01:30:48 2026 daemon.err zeroblock[890]: [zeroblock] Starting ZeroBlock...
207:Sun Feb 22 01:31:06 2026 daemon.err zeroblock[1843]: [zeroblock] Starting ZeroBlock...
249:Sun Feb 22 01:31:22 2026 daemon.err zeroblock[2716]: [zeroblock] Starting ZeroBlock...
396:Sun Feb 22 09:13:05 2026 daemon.err zeroblock[9622]: [zeroblock] Starting ZeroBlock...
441:Sun Feb 22 12:18:22 2026 daemon.err zeroblock[26045]: [zeroblock] Starting ZeroBlock...
483:Sun Feb 22 12:18:41 2026 daemon.err zeroblock[26916]: [zeroblock] Starting ZeroBlock...
541:Sun Feb 22 12:45:46 2026 daemon.err zeroblock[32616]: [zeroblock] Starting ZeroBlock...
640:Sun Feb 22 22:05:22 2026 daemon.err zeroblock[20166]: [zeroblock] Starting ZeroBlock...
682:Sun Feb 22 22:06:36 2026 daemon.err zeroblock[21186]: [zeroblock] Starting ZeroBlock...
724:Sun Feb 22 22:07:09 2026 daemon.err zeroblock[22109]: [zeroblock] Starting ZeroBlock...
766:Sun Feb 22 22:13:44 2026 daemon.err zeroblock[23619]: [zeroblock] Starting ZeroBlock...
808:Sun Feb 22 22:26:22 2026 daemon.err zeroblock[26105]: [zeroblock] Starting ZeroBlock...
850:Sun Feb 22 22:27:24 2026 daemon.err zeroblock[27140]: [zeroblock] Starting ZeroBlock...
892:Sun Feb 22 22:28:00 2026 daemon.err zeroblock[28174]: [zeroblock] Starting ZeroBlock...
934:Sun Feb 22 22:28:13 2026 daemon.err zeroblock[29039]: [zeroblock] Starting ZeroBlock...
976:Sun Feb 22 22:31:28 2026 daemon.err zeroblock[30793]: [zeroblock] Starting ZeroBlock...
1018:Sun Feb 22 22:36:34 2026 daemon.err zeroblock[503]: [zeroblock] Starting ZeroBlock...
1060:Sun Feb 22 22:37:49 2026 daemon.err zeroblock[1849]: [zeroblock] Starting ZeroBlock...
1102:Sun Feb 22 22:39:27 2026 daemon.err zeroblock[3173]: [zeroblock] Starting ZeroBlock...
1145:Sun Feb 22 22:39:56 2026 daemon.err zeroblock[4227]: [zeroblock] Starting ZeroBlock...
1227:Sun Feb 22 22:42:29 2026 daemon.err zeroblock[6178]: [zeroblock] Starting ZeroBlock...
root@roskomnadzor:~#

---

**2026-02-23T02:52:28 | Борис**
окей. я ничего предварительно не настраивал - удалил старый зероблок, поставил новый. он ещё создал версию конфига под новую версию zeroblock-opkg, я старый конфиг удалил и поставил полностью заводской. поэтому эти inbounds как бы из коробки шли

---

**2026-02-23T03:09:51 | Kiss_My_Axe**
Ага...
Mon Feb 23 03:05:11 2026 daemon.err zeroblock[23742]: [zeroblock] Starting ZeroBlock...
Mon Feb 23 03:05:11 2026 daemon.err zeroblock[23742]: [config_builder] Duplicate community_list 'ai' in sections 'GROBLOX' and 'other'
Mon Feb 23 03:05:11 2026 daemon.err zeroblock[23742]: [config_builder] Found 1 duplicate target(s) between sections, aborting
Но это после:
service log restart

Причём:
logread | grep 'Starting ZeroBlock'
так же выводил последней записью ZB запись за вчерашний день.

То есть - ЗБ-лог на месте, однако демон log почему-то невзлюбил ZB и перестал записывать его WARN-сообщения.

---

**2026-02-23T03:32:15 | Борис**
Кстати, пока я под вдохновением от новой прорывной версии Zeroblock, поделюсь своим опытом. Как я делал до Zeroblock: у меня стояли утилиты xray-core и opera-proxy на роутере. В xray-core (сервер vless-reality) было 2 секции outbound - freedom (обычный выход в интернет) и 127.0.0.1:18080 (выход через opera-proxy, Швеция). Также в xray было настроено 2 клиента с разными short-id - один клиент ходит через указанный выше freedom (просто с российского ip роутера), а другой short id ходит через opera-proxy. Таким образом у меня технически было 2 vless-сервера на моих клиентах (на телефоне и ноуте), которые по сути хостились на одном роутере. Теперь благодаря новым функциям Зероблока вариации маршрутизации возрастают невероятно: я (и любой великий пользователь zeroblock) может себе создать хоть сто тыщ подключений на телефоне, каждое из которых ведёт через определённую секцию на роутере, и нажатием буквально одной кнопки (пресловутый "плагин для браузера") переключать сервера в зависимости от потребностей, используя только роутер с его настроенными списками и маршрутами. Очень круто и молодёжно...

---

**2026-02-23T07:08:30 | Anna Bagler**
Все зависит от ваших навыков. Лучше zeroblock.

---

**2026-02-23T07:15:01 | Anna Bagler**
Пробуйте и для себя решите. Файлы из закрепа темы zeroblock beta, ставятся через пакеты, использование аналогично подкопу. Все зависит только от вас.

---

**2026-02-23T09:54:16 | Nikolai Korp**
ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Внутреннее пересечение в zeroblock:
    zeroblock                 : awg10 (Условия: default)
    zeroblock                 : awg10 (Условия: default)
    zeroblock                 : awg10 (Условия: default)
    Домены: googlevideo.com youtube youtube.com

  zeroblock              awg10 (vpn): youtube
  zeroblock          opera (prx out): ai,block,geoblock
  Версия zeroblock: 0.6.4-r46
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

Как гуманно снести zerobloсk?
Что бы не сбрасывать роутер? хочу скрипт 5 попробывать

---

**2026-02-23T10:04:44 | Роман**
С Вацапом всё сложно, если через полный ВПН - нормально работает, если через точечную маршрутизацию - он ломится на большой спектр различных серверов - поэтому может и не завестись на zeroblock/podkop.

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

**2026-02-23T10:30:15 | Ø**
всем привет. сегодня установил последнюю версию прошивки, а также zapret2 и zeroblock, и всё из списков zeroblock работает нормально, кроме всего, что связано с гугловским ИИ. любые другие геоблокнутые сайты (chatgpt, grok, intel.com) работают нормально. в инкогнито на gemini.google.com при попытке сгенерировать ответ получаю 1060. на пятом скрипте с подкопом, до того как я обновился, всё работало. ручной список из доменов с itdoginfo/allow-domains создавать пробовал, тоже не помогло

---

**2026-02-23T11:03:11 | Роман**
Zeroblock/podkop, если лапки скрипт 5, но всё равно домены/ip возможно нужно будет докинуть.

---

**2026-02-23T11:37:05 | Роман**
Как мне кажется будет проще всю приставку в туннель завернуть, чем искать куда ходит приставка.
Zeroblock/podkop вам в помощь для этого.

---

**2026-02-23T13:44:56 | Routerich**
Тогда вам нужен не он, а Zeroblock
https://t.me/routerich/80283/468513

---

**2026-02-23T14:21:26 | Routerich**
вы всегда можете посмотреть что получает ваш роутер от сервера в /tmp/zeroblock/rulesets

---

**2026-02-23T14:25:44 | Routerich**
nft list table inet zeroblock |grep 5.255

---

**2026-02-23T14:29:19 | Routerich**
nft list table inet zeroblock |grep 90.156
nft list table inet zeroblock |grep 185.180
nft list table inet zeroblock |grep 89.221

---

**2026-02-23T14:30:06 | Routerich**
nft list table inet zeroblock |grep 77.88

---

**2026-02-23T14:57:06 | Роман**
По логике полностью приставку в впн заворачивать. Но пинг вырастет. Через zeroblock/podkop можно реализовать.

---

**2026-02-23T15:00:57 | Kiss_My_Axe**
Я нашёл, видимо, проблему пустых пересечений.
zeroblock.awg10.community_lists='socials' 'news' 'anime' 'youtube' 'video' 'messengers'
zeroblock.awg10.server_community_lists='socials' 'news' 'anime' 'youtube' 'video' 'messengers'
Но не знаю, что сделать. :)

---

**2026-02-23T15:04:31 | Ivan Num**
Подскажите. В скором времени получу роутер. Но что всё таки нужно ставить так и не понятно. Zeroblock? Скрипт #5 или asu обновление?

---

**2026-02-23T15:06:18 | Роман**
Это обновление прошивки с пакетами. Скрипт 5 если у вас лапки. Zeroblock - для более продвинутых пользователей.

---

**2026-02-23T15:52:36 | Юрий Теленков**
Если zeroblock использовать только для обхода блокировок (не вдаваясь в подробности, типа весь трафик клиента заворачивать в определенный интерфейс и т.д) есть плюсы ? ну например в скорости работы и подобное. Возможно грузит роутер меньше и т.д

---

**2026-02-23T16:23:52 | Андрей**
Да сначала поставил zeroblock, потом снёс , установил скрипт 5 , не понравился и вернулся на zeroblock

---

**2026-02-23T16:25:08 | Konstantin Uk**
Подскажите пожалуйста, насколько я знаю проблема сейчас проявляется на Билайн/МГТС, не работает Huddle (часть Slack), прерывается звонок каждые надцать секунд.
Что пробовал:
1. Добавить 
slack-imgs.com
slack-edge.com
slack.com
В VPN/Proxy (и так и так)
2. Переустановить с нуля, переехать на ZeroBlock Beta

Лучше не становится, может конечно у худдл какой-то хитрый стриминговый домен?
Подскажите пожалуйста, если кто сталкивался, если бы не аналогичная проблема у некоторых коллег, то предположил бы, что проблема у меня. Все для обхода пользуются разными средствами.

---

**2026-02-23T17:09:54 | Андрей**
А из предустановленных списков zeroblock, telegram убрали?

---

**2026-02-23T18:32:17 | Роман**
victronenergy.com
typekit.net
В zeroblock/podkop.

---

**2026-02-23T18:59:39 | Anna Bagler**
Попробуйте обновить версию анблока, если он у вас не новый. Или уходите на другие способы обхода: zeroblock, скрипт 5/бету.

---

**2026-02-23T20:58:54 | Anna Bagler**
IP в полную маршрутизацию в zeroblock/podkop и проверять.

---

**2026-02-23T21:01:40 | Anna Bagler**
Что вы ставили для обхода zeroblock или podkop скриптом?

---

**2026-02-23T22:00:11 | Routerich**
у кого там проблемы с листами и телегой сделайте в терминале 
zeroblock update_lists
он перекачает исправленные или просто перезагрузите роутер

---

**2026-02-23T22:51:38 | Anna Bagler**
Скрипт 5/бету или zeroblock ставили?

---

**2026-02-23T23:26:01 | Роман**
Удалить пакеты ZB через пакеты, затем rm /etc/config/zeroblock* && reboot - подчистить конфиги.

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

**2026-02-24T00:33:40 | Routerich**
zeroblock get_wg_endpoints

---

**2026-02-24T00:41:36 | kk**
nft list table inet zeroblock? тут тоже нет =)

---

**2026-02-24T01:19:47 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.6.4-r64:
  Исправления:
  - Исправлена dns петля для fully routed в секции c отключенным fakeip
  - Исправлено некорректная запись пользовательских доменов/подсетей
#ZeroBlock

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

**2026-02-24T09:47:16 | 𝒳**
На роутере. Хочу zeroblock поставить и не сломать ничего 😂

---

**2026-02-24T12:14:09 | Роман**
Та ещё морока скачать вашу эту игру. Запихнул в zeroblock, прошел 2 начальных уровня, дальше сами 😁
И да, придется гугл в ВПН заворачивать, последствий этого я не знаю.

---

**2026-02-24T12:31:04 | ㅤㅤ**
Нужна помощь в настройке Routerich + Mash Xiaomi AC1200 в режиме Access Point - Wireless Bridge
Проще было настроить Wired Bridge, но тянуть провода в четырехэтажном частном доме не вариант для родителей. 
В режиме Wireless Bridge Xiaomi создает свою внутреннюю сеть. 

Собственно проблема в том, как подружить это с ZeroBlock. 
Инструкция https://t.me/routerich/80283/123172 этот вопрос не проясняет.

---

**2026-02-24T12:56:30 | Роман**
На левой верхней картинке должен быть текст: "zeroblock не работает".

---

**2026-02-24T13:12:10 | Арсений Спиридонов**
Это не ZeroBlock, это PayToUnblock)

---

**2026-02-24T13:26:47 | ㅤㅤ**
Хм, после настройки ZeroBlock совсем забыл отключить youtubeunblolck
/etc/init.d/youtubeUnblock stop && /etc/init.d/youtubeUnblock disable

---

**2026-02-24T13:48:06 | Михаил**
В чем тут порядок? В нарушении указаний документации от itdog? Мне кажется, в части использования podkop и zeroblock абсолютно ненужные действия. Нет?

---

**2026-02-24T13:50:34 | Роман**
Закинуть TG в zeroblock/podkop.

---

**2026-02-24T14:03:24 | Борис**
Предложение по улучшению. Вы могли бы собирать пользовательские outbound-конфиги при помощи Zeroblock, тем самым пополняя свою базу vless-серверов. Когда база клиентов и собранных от них серверов станет достаточно крупной, вы могли бы договориться с правительством и с Роскомнадзором в частности, чтобы отдать на анализ эти сервера или прикрыть их все в одночасье. На вырученные деньги от сделки с правительством вы могли бы создать новые мощные роутеры, позволяющие сёрфить VK и RuTube на гигабитных скоростях. Эта благородная и важная миссия позволила бы улучшить безопасность и суверенность Российского интернета, а в некоторых аспектах даже превзойти Китайские наработки (что добавило бы стране веса на политической арене)

---

**2026-02-24T14:42:54 | Иван**
Как продиагнострировать проблему, с ПК не грузится ютуб, на телефоне и ТВ хорошо работает, DNS в CHROME выключен, VPN на ПК нет, в другом браузере тоже не открывается ютуб
сижу через ZAPRET2 по ZeroBlock
Дискорд работает, ютуб нет

---

**2026-02-24T16:18:36 | Nook Scheel**
Зная хоть чуть чут как устроен openwrt прочитав 2 инструкции на github zapret2 и на zeroblock все встает даж на чистый openwrt

---

**2026-02-24T17:25:09 | ㅤㅤ**
Инструкция по настройке Xiaomi Wi-Fi Mesh System AC1200 на Routerich в беспроводном режиме для самых маленьких.

1. Включаем Mash и подключаемся к внутренней wi-fi сети вида RD13_minet и задаем пароль администратора устройства.
2. В всплывающем окне браузера выбираем режим работы роутера: Wireless relay mode
3. Подключаемся к основной WiFi сети Routerich (не Routerich-Mesh) и создаем одноименное подключение. Будет создано два подключения, которые идут в обход ZeroBlock не расстраиваемся.
4. Скачиваем Xiaomi Home выбираем русский язык и регион Россия, вручную добавляем устройство, соглашаемся со всем и вводим пароль администратора для подключения. 
5. Переходим в меню "Настройка Wi-Fi" и ставим галочку "Многочастотный управляемый". В настройках прямо под названиями точек доступа есть возможность переименовать их и убрать лишнее "_5G"

В итоге у вас будет одна точка доступа с бесшовным переключением между Routerich и Mash. Доступ к заблокированным ресурсам сохранен.

---

**2026-02-24T18:41:27 | GT_6**
Всем доброго вечера. Подскажите не опытному. Стоит zeroblock все работает как часы. Youtube работает через zapret. Но у меня проблема с Ubisoft коннектом,через раз коннектится к игре. Собрать лобби с друзьями не получается. Приходится использовать КВН. Поиском искал и не нашел где можно взять стратегии. Пытался скачать прогу warp но она не коннектится

---

**2026-02-24T19:15:46 | Vitalisevskiy**
Привет. позавчера поставил ZeroBlock версии r-6 со старыми списками. Запустил автонастройку, поменял бесплатную амнезию в awg10 на конфиг платной и все один день работало прекрасно. Вчера трафик через awg10 идти перестал, думал что проблемы в сервере амнезии. Переустанавливал все несколько раз, обновлял ZeroBlock до 46 версии. Ради эксперимента поменял сейчас API V2 на V1 и все заработало. 

Вопрос, почему с API V2 не идет трафик через амнезию? Как использовать API V2 и наслаждатся маршрутизацией через VPN?)

Ps. Списки перевыбирал, все равно не чет не заводилось

---

**2026-02-24T20:58:18 | Philipp**
Здравствуйте, такой вопрос, у меня есть рабочая конфигурация Amnezia, ключ vpn://AAAGX..
Можно ли как-то добавить её, как секцию в ZeroBlock?

---

**2026-02-24T21:03:00 | Михаил**
У себя решил просто. На первом рабочем роутере zapret2 (youtube) и podkop. Далее роутер для экспериментов 2 со zeroblock, в секции AmneziaWG (awg) тоже  youtube. У кого zapret2 на основном роутере не аллё( samsung, lg и айфон), идут на wifi второго роутера. :)

---

**2026-02-24T21:57:04 | Борис**
Я, собственно, зашёл в эту тему, когда увидел, по какой цене доступны роутеры на Озоне. У меня наверное будет непопулярное мнение, но что поделать... А заключается оно вот в чём: я часто вижу, что люди пишут отзывы, какой роутер замечательный (это действительно так), но почему они покупают их пачками? Разве не выгоднее, когда вы освоили устройство на OpenWRT, покупать что-то более доступное и просто перепрошивать на OpenWRT, и использовать все те же самые преимущества? Ну кроме Zeroblock™ с его api v2, конечно же

---

**2026-02-24T22:59:48 | I5EEYOU**
ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  57.144.110.1 | YouTube IP:  142.250.130.190

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.71 MB / ↑0.40 MB
  Пинг (ya.ru via awg10): 69.942 / 70.609 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock              awg10 (vpn): socials,porn,news,anime,youtube,discord,meta,video,messengers,googleplay
  zeroblock          opera (prx out): geoblock,ai,block
  Версия zeroblock: 0.6.4-r46
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.65 | RAM: 24% | NAND: 52% занято / 32.6M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-02-24T23:21:17 | Роман**
В zeroblock/podkop.

---

**2026-02-24T23:54:07 | Роман**
Zeroblock это средство точечной маршрутизации, если оно вам нужно - установите. Вы изначально за запрет 2 спрашивали.

---

**2026-02-24T23:55:18 | Роман**
Тогда не ставьте zeroblock.

---

**2026-02-24T23:58:15 | Роман**
Может встал криво, ещё раз попробуйте. Zeroblock не устанавливали?

---

**2026-02-25T00:09:17 | Виктор ZEUS**
Так , а zeroblock как найти

---

**2026-02-25T00:47:00 | Владимир Соловьев**
обход через zeroblock

---

**2026-02-25T00:50:49 | Владимир Соловьев**
у zeroblock настройки такие

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

**2026-02-25T07:41:38 | Anna Bagler**
В подкопе они просто работают, если доступны. С выбором - в zeroblock.

---

**2026-02-25T07:45:35 | Anna Bagler**
Тут есть Fresa, он пилит и запрет2, и свой zeroblock.

---

**2026-02-25T08:36:39 | Anna Bagler**
В вашей версии zeroblock есть отдельно список торрентов? Попробуйте переключить на v1 саму секцию.

---

**2026-02-25T08:47:58 | Anna Bagler**
Чтобы пускать отдельные списки через ваш vpn, надо. Или что-то аналогичное, тут есть собственная разработка - zeroblock.

---

**2026-02-25T09:26:59 | Dmitriy**
В zeroblock можно сразу несколько списков доменов itdog добавлять? К примеру Russia inside, YouTube, telegram. Они у него делятся

---

**2026-02-25T09:28:58 | Роман**
Zeroblock, podkop установлен?

---

**2026-02-25T09:42:12 | Dmitriy**
Я новичок, забегая наперед хотел спросить:

Amnezia wg 2 поддерживается zeroblock или не имеет значения протокол и настраивается в отдельном месте? 
Вообще, хотел бы настроить zeroblock со списками + tailscale  и через Routerich домашний по vpn подключаться и выходить через одну точку через клиента tailscale, если не дома.

Это же все хорошо работает на практике, стоит времени на изучение и настройку?

---

**2026-02-25T09:53:48 | Роман**
Иногда нужно время что-бы zeroblock/podkop заработали. Иногда нужно чистить кеш страницы.

---

**2026-02-25T10:14:38 | のイドリ**
Wed Feb 25 10:11:20 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[ruleset_manager] Failed to parse API response
[zeroblock] ZeroBlock started successfully
[clash_api] /xhttp_test__auto/delay?url=http://www.gstatic.com/generate_204&timeout=30000 failed: HTTP 503
Такой текст возвращается в логах после теста, через ссылку подписки также попробовал.

---

**2026-02-25T10:47:22 | Routerich**
для кого написано?
  - Пользовательские JSON фрагменты из /etc/zeroblock/sing-box.d/
если какие-то проблемы с листами, напишите какие

---

**2026-02-25T12:51:14 | ㅤㅤ**
Повторяюсь существует баг с сохранением настроек ZeroBlock! Прослеживается на всех роутерах, на всех компьютерах, в разных браузерах, включая мобильный, по разным адресам. Не даёт сохранить выбор в секциях.

---

**2026-02-25T12:54:08 | Роман**
Это для начала. Или руками ставьте zeroblock, podkop и настраивайте.

---

**2026-02-25T12:55:46 | ㅤㅤ**
ZeroBlock настроен и работает. Параметры сохраняются. Уже после когда ты пытаешься что-то изменить сохранение невозможно с любыми вариациями во всех секциях.

---

**2026-02-25T13:11:59 | Кирилл**
Доброго дня, подскажите пожалуйста.. Поставил zeroblock на чистую owrt 24.10.4. Аппарат cudy tr3000. Все работает на обычном vless. При xhttp (ссылку конвертировал конвертором, в подкопе через sing-box extended работает) не поднимается. По логам увидел ошибку отсутствует xray-core.. Доустановил через менеджер.. Появилась в дашборде в сервис инфо sing-box running и xray stopped.. Что делаю не так?

---

**2026-02-25T13:22:55 | Routerich**
Wed Feb 25 12:58:58 2026 daemon.warn zeroblock[2821]: [config_builder] Xray full config validation failed, trying per-proxy fallback
Wed Feb 25 12:58:58 2026 daemon.warn zeroblock[2821]: [config_builder] Proxy ?:0 — xray validation failed, disabling
Wed Feb 25 12:58:58 2026 daemon.err zeroblock[2821]: [config_builder] No valid xray proxies after per-proxy fallback

---

**2026-02-25T13:48:22 | Кирилл**
[zeroblock] Starting ZeroBlock...
[clash_api] /proxies failed: Error
[config_builder] Sing-box failed to start within timeout
[zeroblock] Failed to start ZeroBlock

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

**2026-02-25T14:00:31 | Azizkhan**
The authenticity of host '192.168.1.1 (192.168.1.1)' can't be established.
==========================================
  ZeroBlock Setup
  API V2 / UrlTest
==========================================

Отключение предустановленных секций...
=== ОТКЛЮЧЕНИЕ ПРЕДУСТАНОВЛЕННЫХ СЕКЦИЙ ===
Отключаю секцию: opera
Отключаю секцию: googleai
Отключаю секцию: all
Предустановленные секции отключены и очищены
Настройка глобальных параметров...
=== ГЛОБАЛЬНЫЕ ПАРАМЕТРЫ ===
Глобальные параметры настроены
Создание секции 'all'...
=== СЕКЦИЯ: all ===
  all: добавлен VLESS ключ
  all: добавлен VLESS ключ
  all: добавлен VLESS ключ
Секция 'all' создана
Создание секции 'ai'...
=== СЕКЦИЯ: ai ===
  ai: добавлен VLESS ключ
  ai: добавлен VLESS ключ
  ai: добавлен VLESS ключ
  ai: добавлен VLESS ключ
Секция 'ai' создана
Перезапуск ZeroBlock...
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: no lease, failing

========================================================================
         REMOVING ZEROBLOCK CRON JOB
========================================================================

✅ ZeroBlock cron job removed successfully
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
dudhcpc: no lease, failing




Анализ запущен: 2026-02-25 17:58:09
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
  Facebook IP:  198.18.0.8 | YouTube IP:  198.18.0.9
  Программы в автозапуске: zeroblock

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock             ai (prx url): ai
  zeroblock            all (prx url): anime,art,block,geoblock,discord,games,googleplay,messengers,meta,music,news,porn,repo,shop,socials,tools,torrent,video,youtube,cdn_akamai,cdn_aws,cdn_azure,cdn_cdn77,!_cdn_cloudflare,cdn_digitalocean,cdn_fastly,cdn_github,cdn_gcore,cdn_google,cdn_ovh,cdn_selectel,cdn_vultr,cdn_bunny,cdn_hetzner,cdn_linode,cdn_oracle,cdn_scaleway
  Версия zeroblock: 0.6.4-r64
  zeroblock DNS/Bootstrap DNS: (doh) dns.malw.link/dns-query / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.53 | RAM: 24% | NAND: 24% занято / 51.0M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-02-25T15:45:40 | Anna Bagler**
Если закажите типы как было по умолчанию, должно вернуться. Но лучше вам тогда в zeroblock. Там просто можно убрать галочку с секций.

---

**2026-02-25T15:52:00 | Aleksei**
Ребята, а подскажите, пожалуйста, для новеньких.

Скрипт №5 или ZeroBlock?
Что лучше? ZeroBlock не заменяет zapret? Их можно использовать вместе?

---

**2026-02-25T16:00:34 | Azizkhan**
нашёл такие логи)

root@RouteRich-iLink:~# logread | grep dnsmasq | tail -15
Wed Feb 25 19:53:21 2026 user.notice dnsmasq: found already running DHCP-server on interface 'lan1.12' refusing to start, use 'option force 1' to override
Wed Feb 25 19:53:30 2026 daemon.err zeroblock[27088]: [dns_manager] Failed to restart dnsmasq
Wed Feb 25 19:53:55 2026 user.notice dnsmasq: found already running DHCP-server on interface 'lan1.12' refusing to start, use 'option force 1' to override
Wed Feb 25 19:54:03 2026 daemon.err zeroblock[27725]: [dns_manager] Failed to restart dnsmasq
Wed Feb 25 19:54:16 2026 user.notice dnsmasq: found already running DHCP-server on interface 'lan1.12' refusing to start, use 'option force 1' to override
Wed Feb 25 19:54:24 2026 daemon.err zeroblock[28253]: [dns_manager] Failed to restart dnsmasq
Wed Feb 25 19:58:32 2026 user.notice dnsmasq: found already running DHCP-server on interface 'lan1.12' refusing to start, use 'option force 1' to override
Wed Feb 25 19:58:38 2026 daemon.err zeroblock[29590]: [dns_manager] Failed to restart dnsmasq
Wed Feb 25 19:58:48 2026 user.notice dnsmasq: found already running DHCP-server on interface 'lan1.11' refusing to start, use 'option force 1' to override
Wed Feb 25 19:58:49 2026 user.notice dnsmasq: found already running DHCP-server on interface 'lan1.12' refusing to start, use 'option force 1' to override
Wed Feb 25 19:59:00 2026 daemon.err zeroblock[29978]: [dns_manager] Failed to restart dnsmasq
Wed Feb 25 19:59:09 2026 user.notice dnsmasq: found already running DHCP-server on interface 'lan1.11' refusing to start, use 'option force 1' to override
Wed Feb 25 19:59:09 2026 user.notice dnsmasq: found already running DHCP-server on interface 'lan1.12' refusing to start, use 'option force 1' to override
Wed Feb 25 19:59:31 2026 user.notice dnsmasq: found already running DHCP-server on interface 'lan1.11' refusing to start, use 'option force 1' to override
Wed Feb 25 19:59:31 2026 user.notice dnsmasq: found already running DHCP-server on interface 'lan1.12' refusing to start, use 'option force 1' to override

---

**2026-02-25T16:22:33 | Kirill Y**
Здравствуйте! Подскажите обновлять zeroblock прям в Luci можно? Или отдельным файлом загружать отсюда? И старый удалять предварительно или просто обновлять?

---

**2026-02-25T18:46:43 | HiLLL**
zeroblock awg warp в терменале

---

**2026-02-25T19:26:36 | Роман**
Для точечной маршрутизации на роутере есть zeroblock/podkop. А на клиенты куча информации в интернете.

---

**2026-02-25T23:30:26 | Роман**
Я имею ввиду все что не идёт в zeroblock, на ру сайты допустим, кто днс рулит?

---

**2026-02-25T23:32:28 | Роман**
Получается если стоит галка перехват dns, всем dns рулит zeroblock?

---

**2026-02-25T23:47:49 | Ikа**
Доброй ночи!
Подскажите, пожалуйста, уже 4ый роутер настраиваю)
И всем друзьям ставлю zeroblock, но вот в первый раз столкнулся с такой ошибкой и youtube gpt  и тд не работают

---

**2026-02-25T23:54:45 | Ikа**
Wed Feb 25 23:45:52 2026 user.notice ucitrack: Setting up /etc/config/zeroblock reload trigger for non-procd /etc/init.d/zeroblock
Wed Feb 25 23:46:39 2026 user.notice zeroblock: Starting ZeroBlock...
Wed Feb 25 23:46:39 2026 daemon.err zeroblock[7684]: [zeroblock] Starting ZeroBlock...
Wed Feb 25 23:46:43 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: udhcpc: started, v1.36.1
Wed Feb 25 23:46:43 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: udhcpc: broadcasting discover
Wed Feb 25 23:46:46 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: udhcpc: no lease, failing
Wed Feb 25 23:46:46 2026 daemon.err zeroblock[7684]: [zeroblock] ZeroBlock started successfully

---

**2026-02-26T00:21:24 | Anna Bagler**
Вот, у Романа тоже не открывается, тогда вам в zeroblock и домены отслеживать и прописывать.

---

**2026-02-26T00:52:21 | Evgeny**
Пожалуйста

Thu Feb 26 00:49:55 2026 user.notice ucitrack: Setting up /etc/config/zeroblock reload trigger for non-procd /etc/init.d/zeroblock
Thu Feb 26 00:50:41 2026 user.notice zeroblock: Starting ZeroBlock...
Thu Feb 26 00:50:41 2026 daemon.err zeroblock[7723]: [zeroblock] Starting ZeroBlock...
Thu Feb 26 00:50:45 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: udhcpc: started, v1.36.1
Thu Feb 26 00:50:45 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: udhcpc: broadcasting discover
Thu Feb 26 00:50:48 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: udhcpc: no lease, failing
Thu Feb 26 00:50:48 2026 daemon.err zeroblock[7723]: [zeroblock] ZeroBlock started successfully

---

**2026-02-26T01:03:56 | Роман**
В запрет2 по умолчанию Ютуб и дефолт стратегии, какие пересечения с zeroblock?

---

**2026-02-26T01:12:05 | Роман**
Через система пакеты обновить списки фильтр zapret2, установить 2 пакета, убрать Ютуб из подкопа zeroblock.

---

**2026-02-26T01:17:55 | Роман**
Я забыл что там галки криво стоят при установке из zeroblock.

---

**2026-02-26T01:23:39 | Роман**
Я бы и Ютуб и Дискорд в запрет2, а запрещенку в zeroblock.

---

**2026-02-26T03:43:19 | Yuri Kovalev**
А если уже обновил все пакеты? Только ZeroBlock поставил и пакеты обновил. Лучше сбросить или оставить как есть? 

П.С Вроде бы все работает

---

**2026-02-26T06:11:02 | Oleg Mi**
Добрый день, 
Подскажите пожалуйста, не имею возможности установить Tailscale (iphone с подписками) но имею необходимость подключится к домашней сети из другой страны с этого же телефона (и ПК) и в идеале использовать роутер как российский высокоскоростной  ркн находясь за границами РФ. 
Возможно ли это реализовать и если возможно то если можно кратенько что нужно установить/сделать/настроить. 
Роутер RR свежей поставки, Установлен Zeroblock 0.6.4r-8, настроено работает хорошо.
Буду рад любой помощи

---

**2026-02-26T08:12:07 | HiLLL**
Варп отвалился? Попробуйте в терминале ввести zeroblock awg warp

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

**2026-02-26T09:38:12 | Алексей Сергеевич**
Я обновил Routerich до 24.10.5 https://t.me/routerich/7/479323 и поставил ZeroBlock BETA https://t.me/routerich/394153/432059 Если надо чтобы вне дома работало, поднимаешь на роутере Tailnet с Exit Node и цепляешься к нему с мобилки

---

**2026-02-26T09:53:28 | Anna Bagler**
Руками ставить zeroblock из соответствующей темы.

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

**2026-02-26T13:03:17 | Routerich**
часа через 2, если я не забуду
zeroblock update_lists
или дождаться когда зб сам списки обновит

---

**2026-02-26T13:06:06 | 1v@nk0**
Вопрос чайника, извиняюсь, - чем отличаются сущности? 
1/ ZeroBlock  2/ Zapret   3/ Podkop
Что выбрать для работы с нейронками чтобы снизить вероятность отлететь в бан?

В wiki и руководстве пользователя не нашел - наверно плохо искал

---

**2026-02-26T13:16:32 | kk**
если просто добавить к регуляркам (...|pppossh), то в  luci появляется выбор инт-са в списке vpn,
НО если выбрать этот инт-с и сохранить в вэб инт-се, в uci уходит след. команда -  
uci set zeroblock.ssh1.interface='ssh1', а должна быть ...='pppossh-ssh1', как в системе

т.е регулярки отрабатывают, но имя инт-са режется. 
подкрутил вчера displayName и получилось... быстрый костыль моим говнокодом сработал.
всё работает кроме этого нюанса.

---

**2026-02-26T13:21:31 | Aleksei**
это нормальное состояние ZeroBlock? 
дашборд не грузится(
хотя по диагностике, всё зелёное, кроме FakeIP (клиент). И диагностика показывает пинг до VLESS-сервера

---

**2026-02-26T13:29:55 | Aleksei**
обновил до 82
всё равно висит Подключение к Clash API...
и также дашборд недоступен.

а есть возможность сборсить как-то конфигурацию ZeroBlock?

оно писало при обновлении:

udhpc: started, v1.36.1 udhcpc: broadcasting discover udhcpc: no lease, failing udhcpc: started, v1.36.1 udhcpc: broadcasting discover udhcpc: no lease, failing
Collected errors:
* resolve_conffiles: Existing conffile /etc/config/zeroblock is different from the conffile in the new package. The new conffile will be placed at /etc/config/zeroblock-opkg-

---

**2026-02-26T13:34:31 | Aleksei**
Thu Feb 26 13:26:14 2026 user.notice ucitrack: Setting up /etc/config/zeroblock reload trigger for non-procd /etc/init.d/zeroblock
Thu Feb 26 13:26:58 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[dns_manager] No backup found, nothing to restore
Thu Feb 26 13:27:03 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: udhcpc: started, v1.36.1
Thu Feb 26 13:27:03 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: udhcpc: broadcasting discover
Thu Feb 26 13:27:06 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: udhcpc: no lease, failing
[zeroblock] ZeroBlock started successfully

---

**2026-02-26T13:37:02 | Routerich**
service zeroblock stop && mv /etc/config/zeroblock-opkg /etc/config/zeroblock

---

**2026-02-26T14:17:27 | Azizkhan**
luci: accepted login on /admin/services/zeroblock for root from 100.86.195.251
[ 16585] 0 16585 1369 64 36864 0 0 zeroblock
Thu Feb 26 17:53:52 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Thu Feb 26 17:53:56 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[zeroblock] ZeroBlock started successfully
Thu Feb 26 18:15:25 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Thu Feb 26 18:15:29 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[clash_api] /ai__auto/delay?url=http://www.gstatic.com/generate_204&timeout=30000 failed: Error
[clash_api] /ai__auto/delay?url=http://www.gstatic.com/generate_204&timeout=30000 failed: Error
[clash_api] /ai__auto/delay?url=http://www.gstatic.com/generate_204&timeout=30000 failed: Error
[clash_api] /all__auto/delay?url=http://www.gstatic.com/generate_204&timeout=30000 failed: Error
[clash_api] /all__auto/delay?url=http://www.gstatic.com/generate_204&timeout=30000 failed: Error
[clash_api] /all__auto/delay?url=http://www.gstatic.com/generate_204&timeout=30000 failed: Error
[clash_api] /ai__auto/delay?url=http://www.gstatic.com/generate_204&timeout=30000 failed: Error
[clash_api] /all__auto/delay?url=http://www.gstatic.com/generate_204&timeout=30000 failed: Error
[zeroblock] ZeroBlock started successfully

---

**2026-02-26T14:26:21 | Alexander cewil Pankratov**
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
  Facebook IP:  157.240.199.35 | YouTube IP:  64.233.162.136

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓5.86 MB / ↑0.31 MB
  Пинг (ya.ru via awg10): 158.628 / 160.708 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock              awg10 (vpn): meta
  zeroblock          opera (prx out): geoblock,block
  Версия zeroblock: 0.6.4-r82
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.23 | RAM: 23% | NAND: 23% занято / 51.7M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-02-26T14:49:37 | Routerich**
используйте zeroblock show_sing_box_config

---

**2026-02-26T17:18:41 | ㅤㅤ**
Решаю вопрос удаленно, чуть позже попробую и отпишусь. 

На данный момент проверили отключение iCloud Private Relay (Частный узел) и Limit IP Address Tracking

Также нужно перепроверить работает ли там ZeroBlock с IPv6 так как Apple и LG любят туда лезть. Попробую его наглухо отключить.

Гляну "частный DNS" и QUIC в Chrome, в Safari «Скрывать IP-адрес от трекеров».

---

**2026-02-26T17:30:43 | Wenzel Perminov**
тут у меня опять youtube через zapret2 отвалился, но на Андройде где стоит ByeDPI одна стратегия долго живет. Я подумал может можно в качестве альтернативы запрету добавить, пакеты скомпилированные под openwrt есть на github, сам ByeDPI маршрутезировать не умеет, но создает прокси через которую может zeroblock маршрутизировать.

---

**2026-02-26T17:45:06 | Anna Bagler**
Если навыки позволяют, то тема zeroblock beta. Если нет, то https://t.me/routerich/3845/245550

---

**2026-02-26T17:48:51 | Denis**
Всем привет, подскажите, cтандартные списки с iplist’а, которые есть в zeroblock добавляются по доменам или там есть что-то еще?

Хочу составить кастомный список, думаю какие типы данных выбирать

Еще вопрос есть, можно ли где-то поменять в ZB iplist.my-handbook.ru на стандартный iplist или на тот же allow domains, чтобы можно было из них галочками выбирать?

---

**2026-02-26T18:06:25 | konnlori**
Ладно, всё-таки придётся самому скрипт писать с zapret-discord-youtube, просто думал уже есть готовое решение) Но если бы разаботчики ZeroBlock такое добавили я бы не отказался

---

**2026-02-26T18:15:13 | Anna Bagler**
Да, или переходить на zeroblock.

---

**2026-02-26T18:16:41 | Anna Bagler**
В настройках zeroblock.

---

**2026-02-26T19:15:25 | Marseille Geertje**
А вот Вы пишете переходить на zeroblock.
1. Взамен чего его нужно использовать?
2. Устанавливать его уже после запуска скрипта 5 или вместо?

---

**2026-02-26T19:20:07 | Marseille Geertje**
После сброса до заводских и установки zeroblock и podkop2 у меня даже обновление пакетов перестаёт работать. 😬 Вот так показывает при установке.

---

**2026-02-26T20:06:19 | Роман**
Накатить zeroblock, закинуть свою ссылку vless и выбрать список messengers.

---

**2026-02-26T20:31:57 | HiLLL**
запустите в терминале zeroblock awg warp

---

**2026-02-26T21:27:08 | Борис**
Я обнаружил такую проблему в Zeroblock™... Программа всегда приписывает приоритет = 50, и я не могу им управлять, если скажем, сделаю файл 35-route.json, то он будет сохранён в итоговой папке как 50-custom-35-route.json... Это является проблемой, потому что роутинг в sing-box, как я понял, работает таким образом, что отправляет по первому подходящему правилу route, а поскольку мои конфиги всегда добавляются методом append в самый конец, то до моих роутов не доходит и всегда применяется роутинг по умолчанию (директ?). Можно что-то с этим сделать? 👉👈

---

**2026-02-26T21:30:41 | Anna Bagler**
Полная маршрутизация по IP/подсети. Но лучше тогда на zeroblock перейти.

---

**2026-02-26T21:35:50 | Борис**
моя проблема такая, что у меня есть custom inbound - там описан мой vless-клиент (tag = "vless-in")
соответственно, дефолтный /tmp/zeroblock/sing-box.d/40-route.json ничего не знает о моём inbound tag = "vless-in", и надобно его туда засунуть...
какой выход из ситуации, если я не могу редактировать файлы в /tmp? Правильно, создать пользовательский конфиг в /etc
я создаю пользовательский route.json и получаю поведение, что до моего vless-in не доходит маршрутизация, потому что она спотыкается о default, описанный в 40-route.json (у него выше приоритет, поэтому берётся сначала он)

и выходит, что я в тупике, а на щеках слёзы...

---

**2026-02-26T22:38:38 | Борис**
в общем, я немного ввёл в заблуждение по поводу своих слёз на щеках изначально. Если создать кастомный route.json с таким содержанием, то всё в принципе работает (трафик vless-клиента направляется в opera proxy):
{
  "route": {
    "rules": [
      {
        "inbound": ["vless-in"],
        "outbound": "opera"
      }
    ]
  }
}

но в чём проблема: я на роутере, очень счастливый, в Luci Zeroblock настраиваю Секции Маршрутизации, добавляю в секции списки сообщества... Всё это в итоге записывается в /tmp../route.json, где, грубо говоря, написаны такие инструкции (и ещё много-много правил и списков):

{
        "inbound": [
          "tproxy-in",
          "tproxy-in6"
        ],
        "outbound": "opera",
        "rule_set": [
          "community-opera-geoblock",
          "community-ip-opera-geoblock",
          "community-ip6-opera-geoblock",
          "community-opera-ai",
          "community-ip-opera-ai",
          "community-ip6-opera-ai"
        ]
      },

И мой кастомный inbound с тегом "vless-in" никак не "зашит" в этот route.json. То есть мои секции маршрутизации не действуют на мой кастомный inbound, поскольку route.json ничего не знает о таком инбаунде, и у него нет для него правил... Я бы хотел, чтобы инбаунд "vless-in" использовал эти настроенные списки и секции, и не понимаю, как этого добиться (без полного копирования route.json из /tmp в /etc, но это ведь полумера, потому что когда я поменяю в luci свои секции, они изменятся в /tmp, но в /etc всё останется старым)

---

**2026-02-26T22:50:59 | Ilya Gorbunov**
[nft_manager] Failed to read batch file for apply
[config_builder] Failed to apply NFT batch
[config_builder] Failed to setup NFTables
[zeroblock] Failed to start ZeroBlock
Как тут лучше подебажить что ему на 82 для счастья не хватает?)

---

**2026-02-26T23:03:03 | Владимир Сурков**
подскажите пожалуйста почему warp работает очень плохо на роутере 
при подключении через дефолтное приложение(amneziaVPN)  - проблем нет
закидываю конфиг в awg10 
настраиваю секцию маршрутизации в ZeroBlock 
и через него vpn работает в разы хуже 

подскажите пожалуйста, как решить это проблему

---

**2026-02-26T23:19:20 | Борис**
я кажется понял... это из-за того, что в вашем конфиге он слушает listen 0.0.0.0:10443 со всех устройств в сети?
потому что у меня слушает 127.0.0.1:10443, а попадает туда запрос так:

Запрос из Интернета (wan) -> nginx на роутере смотрит запрашиваемый SNI. Если SNI = m.vk.com, перенаправляю на 127.0.0.1:10443, иначе в 127.0.0.1:8080
(порты закрыты снаружи, чтобы их нельзя было прозвонить, поэтому использую listen 127.0.0.1)

может из-за этого такое быть, что маршрутизация zeroblock не работает, потому что запрос типа внутренний (из устройства роутера 127.0.0.1, а не с устройства извне) ?

---

**2026-02-26T23:29:18 | Борис**
под петлёй подразумевается что? 127.0.0.1? Nginx проксирует запрос из инета на 127.0.0.1:10443, и поскольку nginx и sing-box установлены на одном устройстве (127.0.0.1), то такое проксирование возможно, поэтому запрос из интернета путешествует, грубо говоря, по такой схеме:


Клиент IP 5.12.32.1 => Мой роутер IP 31.31.12.41:443 => Мой роутер внутри себя 127.0.0.1:10443 => (выход в интернет под IP роутера 31.31.12.41)

а я типа хотел так:

Клиент IP 5.12.32.1 => Мой роутер IP 31.31.12.41:443 => Мой роутер внутри себя 127.0.0.1:10443 => Секции из ZeroBlock на роутере => (выход в интернет с IP в зависимости от секции)

ладно, в любом случае спасибо большое за отклик и сопровождение, мне кажется всё-таки дело либо в listen 127.0.0.1, либо то что я транспорт grpc использую, а у вас в конфиге стандартный tcp + vision, хотя тоже хз как это может влиять... Буду дальше пердолиться

---

**2026-02-26T23:50:33 | S W**
Здравствуйте, возможно не совсем по теме, но может сможете помочь мне понять как сменить у варпа (использую zeroblock, секция awg) ip с московского на ближайший ко мне (возможно ли это вообще?) зарубежный, чтобы избежать геоблока (в конкретной игре россия в геоблоке) 

Реализуемо ли это? Вроде же был какой то алгоритм подбора ближайшей точки

---

**2026-02-26T23:57:30 | Евгений Фролов**
Здравствуйте ребята!
Заметил  в uci следующие настройки
zeroblock.WARP.dns_bootstrap='77.88.8.8'
zeroblock.WARP.bootstrap_dns_server='1.1.1.1'
В luci выбран 1.1.1.1.
Это не критично?

---

**2026-02-27T00:24:03 | Алексей**
Здравия желаю!Что-то я не понял как установить.Обновляю список пакетов,но zeroblock в итоге не могу найти в вебморде.Что-то не так делаю?

---

**2026-02-27T00:24:17 | Борис**
речь про /tmp/zeroblock/sing-box.d/40-route.json ? У меня он там ничего сам не подставляет... Я зероблок после изменений перезапускаю кнопкой "Перезагрузить" из Luci, может я что-то не так делаю?

---

**2026-02-27T01:15:13 | Борис**
Благодаря программе Zeroblock™, разработанной командой Routerich, а также компетентной работе службы поддержки, смог превратить свой мобильный интернет из первой картины во вторую. Роутер обладает не только высокой производительностью и скоростью, но и активной группой поддержки в лице талантливых разработчиков и отзывчивых пользователей. Не купить такой роутер в 2026 году — настоящее преступление.

---

**2026-02-27T04:21:50 | Anna Bagler**
Чего именно, всего? Если навыки позволяют, то вам в закрепы темы zeroblock beta. Если нет, то сюда https://t.me/routerich/3845/245550

---

**2026-02-27T07:50:53 | .**
Ребят, скажите пожалуйста:
ZeroBlock  0.6.4-r8  
Последняя  0.6.4-r8  
LuCI App  0.6.4-r8  
sing-box  1.12.17  
OpenWrt  24.10.5
судя по всему, в последних версиях vless  не работает flow=xtls-rprx-vision
zeroblock просто не зпускается, бесконечно крутится и не запукается
Fri Feb 27 08:08:19 2026 daemon.err zeroblock[8910]: [zeroblock] Starting ZeroBlock...
или только у меня такая проблема?

если попробовать ручками обновить sing-box, zeroblock не отлетит? или ждать пока в прошивке обновят пакеты?

---

**2026-02-27T08:01:43 | .**
у меня почему то не работает именно с flow=xtls-rprx-vision..
убрал из конфига эти строки и почти норм, во всяком случае zeroblock хотя бы стартанул, но почему-то часть маршрутов не работает,не пойму в чём дело🥲

---

**2026-02-27T08:31:55 | John Deere**
Добрый день! Стоит zapret2 и zeroblock, после обновы до zeroblock с API v2 YouTube перестал работать на некоторых устройствах. YouTube unblock в автозагрузке отключен, в списке только запрета не зироблока, cidr вкл/выкл разницы нет. Попробовать убрать ют с запрета и выбрать его в зироблоке или есть другие решения?

---

**2026-02-27T09:02:16 | Инженер Проектировщик**
Приветствую! почему zeroblock не парсит подписку?

[zeroblock] Starting ZeroBlock... [subscription_parser] HTTP 500 from subscription server [singbox_gen] Catch-all section Liberty_VLESS: auto-disabled FakeIP (no exclusions) [singbox_gen] Catch-all section Liberty_VLESS has disable_fakeip but no DNS config, using dns-main [singbox_gen] Section Liberty_VLESS: no parsed proxies from subscription

Секция urltest работает нормально, но вот секция Подписка как будто не видит конфиги по ссылке, хотя они там есть и приложухи типа V2Ray по этим ссылкам все добавляют. 

Как решить этот вопрос?

---

**2026-02-27T09:06:06 | Routerich**
Здравствуйте.
пишите в тему ZeroBlock с полным описанием и логами желательно приложить пример подписки, с которой проблема.

---

**2026-02-27T09:07:22 | Инженер Проектировщик**
Приветствую! почему zeroblock не парсит подписку?

[zeroblock] Starting ZeroBlock... [subscription_parser] HTTP 500 from subscription server [singbox_gen] Catch-all section Liberty_VLESS: auto-disabled FakeIP (no exclusions) [singbox_gen] Catch-all section Liberty_VLESS has disable_fakeip but no DNS config, using dns-main [singbox_gen] Section Liberty_VLESS: no parsed proxies from subscription

Секция urltest работает нормально, но вот секция Подписка как будто не видит конфиги по ссылке, хотя они там есть и приложухи типа V2Ray по этим ссылкам все добавляют. 

Как решить этот вопрос?

---

**2026-02-27T09:35:24 | Роман**
И так дали zeroblock ставить на другие роутеры без автонастройки, так ещё и скрипт 5 хотят на халяву.

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

**2026-02-27T11:09:39 | Борис**
Вот такие результаты я получаю. Расшифровка скриншотов:
1) сайт активно используется секцией opera в zeroblock
2) сайт не используется секциями зероблок; мой обычный Российский IP
3) Использую подключение с телефона через opera proxy напрямую (192.168.1.1:18080)

Что примечательно: один и тот же ipv6 - мой, Российский, когда сайт находится и не находится в секции zb. Меняется только ipv4. Настройки стоят такие: dns prefer ipv6, стоит галочка "Поддержка ipv6"

У меня проблемы и жалобы никакой нет, просто делюсь результатами, если интересно

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

**2026-02-27T11:49:36 | Routerich**
Здравствуйте.
Самый простой в Podkop/zeroblock пустить в полный впн устройство
посложнее искать домены/подсети или использовать готовые из чата и добавлять их

---

**2026-02-27T12:59:24 | Kiss_My_Axe**
А детектить стейты по тейблам это прям мёёёд.
Что хошь пиши в ретурне /etc/init.d/zeroblock status, табличка покажет кто где кто!
Хотя по злобЕ можно пустую оставлять, штобе не расслаблялись.

---

**2026-02-27T12:59:27 | Марат Гулагаев**
Друзья, всем добрый день
подскажите пожалуйста, помимо Tailscale есть возможность пустить трафик через впн через роутер?
недавно приобрёл роутер, не очень сильно разбираюсь во всем этом, установил себе zeroblock, настроил его, и два раза ставил Tailscale, всё запускалось, работало пару дней и начинало отваливаться, при этом просто через WiFi всё работает, сбрасывал роутер и настраивал всё заново
может можно как-то развернуть ещё какой-нибудь VPN-сервер на роутере и подключаться к нему, чтобы выходить через него в интернет с телефона например
или tailscale это лучшее решение?
прошивка роутера последняя, зероблок тоже последний

---

**2026-02-27T12:59:40 | Борис**
Через nginx пролазит такой странный формат. Как видно, это начальный кусок моего российского IPV6. Формат ::1 на конце мне непонятен, выглядит как подсеть, а может это типа ipv6 моего телефона в локальной сети (я не знаю как работает ipv6 по сути)

Подключение выполнено так: телефон подключен по wifi к моему домашнему роутеру Routerich. Используя интернет этого роутера, телефон через vpn подключается по интернету по публичному ipv4 к нему же (к роутеру из wan), попадает на nginx:443, далее nginx стримит запрос на 127.0.0.1:10443 роутера (zeroblock sing-box), ну и дальше выходит в интернет. секцию не подключал для 2ip

---

**2026-02-27T13:11:49 | Anna Bagler**
Удалить пакеты zeroblock в Система - Пакеты. Подкоп поставить скриптом, как вы делали до этого.
Обновлять установкой пакетов из соответствующей темы. Ваш личный выбор.

---

**2026-02-27T13:17:17 | Anna Bagler**
Поле фильтра, в нем вписать zeroblock, ok и удалить нужное.

---

**2026-02-27T14:40:09 | konnlori**
Может я, конечно, тупой, но мои секции не работают нормально. Просто нифига не грузит. В диагностике пингуется, через другие клиенты работает - только в Zeroblock такая фигня. Это раз

Во-вторых, он в дашборде вечно их тестирует (в диагностике сразу же)
В-третьих, он не может прочитать десинк запрета

Вчера всё работало прекраснейше, сегодня почалось... Я сейчас обновился до 85, но на 83-ей та же фигня была

---

**2026-02-27T15:23:36 | Михаил**
Искал, искал и вроде бы нашел ошибку zeroblock. 
Есть две секции с awg - вторая и четвертая в списке. Оба интерфейса провереные в podkop - оба работающие. К слову первый из них протон, второй warp. Первая секция opera - она вообще тут не при делах. А вот третья urltest  в ней несколько ссылок ss, hysteria2 и пр. Итог - при активной третьей секции urltest - секция awg перед ней в норме, а после нее - awg не отзывается. Если сделать секцию urltest неактивной - то и второй и червертый awg работают.

---

**2026-02-27T15:43:34 | Aleksandr**
Zeroblock 0.6.4-r64

---

**2026-02-27T15:43:46 | Routerich**
А ты думаешь зачем Zeroblock появился?)

---

**2026-02-27T15:54:35 | Михаил**
Наверно после активной замены ссылок в ней что-то нарушилось в структуре. Если вам для отладки надо - могу конфиг zeroblock вам перекинуть.

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

**2026-02-27T16:01:39 | Роман**
То есть подкоп лучше чем zeroblock 😭

---

**2026-02-27T16:13:22 | Роман**
Ставьте запрет 1, подбирайте стратегии скриптом от zteessozz, скриптом от Kiss_My_Axe, запрет 2 - гайд на Дискорд в теме по запрет2. Купить ключ vless вставить в подкоп/zeroblock. Поднять свой ВПН.

---

**2026-02-27T16:19:23 | Anna Bagler**
На РР популярна связка zeroblock и zapret2.

---

**2026-02-27T16:40:44 | Anna Bagler**
Ставьте zeroblock.

---

**2026-02-27T17:08:55 | Алексей Максимов**
здесь должен быть zeroblock? или ставить из пакета в закрепе  к каналу zeroblock-beta?
Открыл ман - там сразу  "послу установки..."

---

**2026-02-27T19:05:22 | Михаил**
У меня и podkop и zeroblock отлично на одном роутере сожительствуют. Через автозапуск то один стопорю и другой запускаю. Пока проблем не было. Зато есть возможность сравнить одно ПО с другим.

---

**2026-02-27T19:23:12 | Kiss_My_Axe**
В терминале роутера
service sing-box disable
service zeroblock restart
Зайти в настройки зероблок и выключить секцию awg10, сохранить, применить. Ещё раз зероблок перезапустить.

---

**2026-02-27T19:27:26 | Kiss_My_Axe**
Ок. Вам автор по спискам ответил, в настройках zeroblock пока установите API V1, сохранить, применить.

---

**2026-02-27T19:31:08 | Kiss_My_Axe**
Ужос! Ютубанблок остановить, что там у вас было установлено, я не знаю, но этого там больше нет.
То есть нет либо ZeroBlock, либо Podkop.
DNS пугающе прекрасны!

Устанавливайте повторно или зероблок, или подкоп.

---

**2026-02-27T19:31:22 | Anna Bagler**
https://t.me/routerich/173678/449069 или тема по zeroblock.

---

**2026-02-27T19:42:01 | LevM**
Outbounds проверки — Не удалось получить результаты проверки zeroblock пишет

---

**2026-02-27T19:54:58 | Алексей**
поставил zeroblock, настроил разные vpn url для разных приложений, полет нормальный
отдельное спасибо за возможность указать несколько ссылок на подключение, очень удобно

---

**2026-02-27T21:20:41 | Александр Меркушев**
Добрый вечер, вот такая ерунда при попытке поставить зероблок. Роутер чистый. Версия zeroblock_0.6.2-r53_aarch64_cortex-a53

---

**2026-02-27T22:04:55 | Routerich**
zeroblock или podkop остановили?

---

**2026-02-28T00:21:12 | Михаил**
Вопрос по подписке url. Если я правильно понял, выбор лучшего url в подписке происходит раз в 3 мин. Это время можно изменить в параметрах.
 А обновление содержимого самой подписки? Если меняется состав подписки, как быстро zeroblock зацепит эти изменения?

---

**2026-02-28T00:28:25 | Kirill Y**
Подскажите, что надо добавить в списки zeroblock, чтоб 4pda работало?

---

**2026-02-28T03:09:16 | Сергей**
Недавно купил роутер. Пытаюсь пакетами из wiki поставить zeroblock. Выдает ошибку. Как исправить?

---

**2026-02-28T03:13:18 | Anna Bagler**
Вы уже в zeroblock. Вот его и пробуйте.

---

**2026-02-28T05:15:39 | X**
Есть планы, когда ZeroBlock станет стабильным и его можно будет ставить всем?

---

**2026-02-28T05:28:23 | X**
У меня сейчас podkop просто работает и не глючит. Не особо понятно зачем ставить и быть тестировщиком ZeroBlock. Я бы попробовал что-то новое, может там какие-то полезные функции, но возиться с недоработанными программами желания нет.

---

**2026-02-28T05:37:17 | M D**
Вообщем не одна vless подписка не работает. Они рабочие. Сбрасывал роутер, делал просто подключение к провайдеру через визарда, а потом отдельно vpn на телефон/пк - все работают. В zeroblock не открывают заблоченные сайты, latencyN/A

---

**2026-02-28T07:28:04 | Михаил**
А как у вас в podkope подписки работают? Я в нем  типа конфигурации подписки  не вижу. А вот в zeroblock такой тип  как раз есть.

---

**2026-02-28T07:37:07 | Михаил**
У меня на рабочем(для семьи) podkop, на экспериментальном (для души)и podkop и zeroblock. В zeroblocke возможностей поболе получается.

---

**2026-02-28T09:15:56 | Александр**
PS5. ZeroBlock или podkop, пробовал и то и другое. Весь трафик консоли идёт через VPN wireguard.
Про ip, не понял. Белый ли ip у меня? То я так понимаю нет. Да и у друзей точно нет.

---

**2026-02-28T09:40:30 | ㅤㅤ**
У меня WhatsApp работает шустро. Дополнительные списки не добавлял. По общим спискам в ZeroBlock, которые добавлены:
🔹Opera Proxy: GeoBlock, Block
🔹AmneziaWG: Meta

📱 Для смартфона нужно скачать сам apk для android (скачать напрямую) https://www.whatsapp.com/android

Далее списки логично добавлять в AmneziaWG, экспериментируйте.

Ввод пользовательских подсетей (текстовое поле):
3.0.0.0/10
16.0.0.0/10
18.194.0.0/15
31.13.24.0/21
31.13.64.0/18
34.224.0.0/12
54.242.0.0/15
57.141.0.0/20
57.144.0.0/14
66.220.144.0/20
69.63.160.0/19
69.171.192.0/18
74.119.76.0/22
108.168.174.0/24
129.134.0.0/17
157.240.0.0/16
163.64.0.0/12
173.252.64.0/18
185.60.216.0/22
204.15.20.0/22

Ввод пользовательских доменов (текстовое поле):
fb.me
graph.facebook.com
bintray.com
wl.co
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

Черпать вдохновение можно здесь:
Динамический список доменов:
https://raw.githubusercontent.com/KharunDima/whatsapp-lists/main/results/domains.txt
https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_domainlist.txt

Динамический список подсетей:
https://raw.githubusercontent.com/KharunDima/whatsapp-lists/main/results/cidr_ipv4.txt
https://raw.githubusercontent.com/HybridNetworks/whatsapp-cidr/main/WhatsApp/whatsapp_cidr_ipv4.txt

---

**2026-02-28T10:08:38 | Роман**
Обычным, через zeroblock.

---

**2026-02-28T10:30:03 | ㅤㅤ**
Есть мысли по какой причине ZeroBlock не дружит с современными устройствами Apple на MacOS и iOS? Ну и ТВ. Куда глядеть? https://t.me/routerich/3845/514163

---

**2026-02-28T11:10:41 | DG**
Методом научного тыка выяснил почему не работают голосовые  в discord. Если в секции выбран список discord (у меня это секция awg - свой сервер) и в настроках zeroblock стоит галочка на "Маршрутизировать голосовой трафик Discord (UDP 50000-65535) через прокси." то голосовые не работают, но если эту галку снять, то голосовые начинают работать. Zeroblock последняя версия.

---

**2026-02-28T11:18:15 | Роман**
Подскажите пожалуйста, уважаемый разработчик, zeroblock обновляет подписки (если в них произошли изменения допустим) или просто пингует? Или при обновлении листов парсит подписку по новой?

---

**2026-02-28T11:22:46 | Роман**
Буду знать что для обновления подписки нужно перезапустить zeroblock, либо руками, либо обновлением списков. Спасибо.

---

**2026-02-28T12:03:03 | DG**
перезапуск Zeroblock и голосовые опять появились, галка в настройках снята

---

**2026-02-28T12:11:54 | DG**
чудеса, сейчас опять поставил галку на discord voice через прокси, перезапустил zeroblock и голосовые снова заработали, но не на долго через пару вызовов опять отруб....

---

**2026-02-28T12:30:25 | Михаил**
Проверил. При перезапуске zeroblock списки в подписке точно поменялись. Это работает. Если ваши списки меняются на удаленном сервере, к которому вы указали доступ через https, как мне кажется(!), zeroblock ничего не чувствует и продолжает работать со старыми списками. Так что железобетонный способ все же -перезапуск zeroblock. 
В принципе, если бы разработчик поставил бы еще один таймер и дал им управлять, и по нему обновлял бы список, было бы вообще шоколадно. Podkop бы в этом вопросе остался далеко позади.

---

**2026-02-28T12:55:00 | Marseille Geertje**
Пробовал. У меня два роутера. Один со скриптом 5, второй с zeroblock и zapret2. И то и то работает плохо в части скорости ютуба. А на втором ещё и rutracker не работает без браузерного плагина. 🤷🏻‍♂️

---

**2026-02-28T13:08:32 | Marseille Geertje**
Спасибо. Сейчас попробую.
А правильно ли я понимаю, что связка ZeroBlock и Zapret2 удобнее в части ковыряний в настройках в которых я ничего не смыслю. 😄

---

**2026-02-28T13:09:43 | Роман**
На вкус и цвет. Кому удобнее подкоп, кому zeroblock.

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

**2026-02-28T14:24:29 | ㅤㅤ**
На данный момент возможности нет, как только поеду на объект в другом городе сделаю. Была произведена установка ZeroBlock, автонастройка: Opera Proxy, AmneziaWG WARP

Уже на этом этапе все заработал на Android 16 и одном iPhone 17. Дальнейшие эксперименты смысла не имели.

---

**2026-02-28T16:13:27 | Александр**
Не понимаю, почему RDR2 такой капризный. 😵‍💫
Короче говоря, получилось запустить RDR2 через VPN WireGuard силами роутера получается? 
https://lsetc.ru/openwrt-nastrojka-wireguard-klienta/#%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0_WireGuard_%D0%BA%D0%BB%D0%B8%D0%B5%D0%BD%D1%82%D0%B0_%D0%BD%D0%B0_OpenWRT_%D1%80%D0%BE%D1%83%D1%82%D0%B5%D1%80%D0%B5

Без всяких Podkop/ZeroBlock/V2RayA. Через всё это онлайн в RDR2 не работает.
В других играх ещё не сталкивался,всё всегда работает через ZeroBlock.

Теперь придётся скакать между ZeroBlock и WireGuard на роутере.

---

**2026-02-28T16:23:37 | Александр**
Вот, вот. Это первая игра, которая не хочет работать через VPN через ZeroBlock, Podkop, V2rayA. Даже если в ZeroBlock Wireguard проходит. Хоть убей, не работает только RDR2. Как только напрямую wireguard запустил, всё заработало.

---

**2026-02-28T16:26:22 | Anna Bagler**
Для этого есть списки сообщества. Подсеть пустить в полную маршрутизацию, но для этого больше подходит zeroblock.

---

**2026-02-28T16:43:35 | Bullet for my valentine Poison**
Я так жду обновлений для zeroblock'a

---

**2026-02-28T16:59:46 | Роман**
У вас и так последняя прошивка. Сами файлы в теме zeroblock, в закрепе. Скачать и через пакеты установить. Обновить списки не забудьте.

---

**2026-02-28T17:00:18 | Святос**
На главной посмотрите версию прошивки, и в тему Zeroblock

---

**2026-02-28T17:19:06 | Ａｌｅｘａｎｄｅｒ**
А где находятся списки доменов сервисов у ZeroBlock?

---

**2026-02-28T18:41:53 | Yuri Kovalev**
Здравствуйте. У меня есть несколько вопросов ответы на которые я не нашел. Подскажете пожалуйста

1) После установки ZeroBlock создается интерфейс awg10 который внутри себя уже имеет настройки Амнезии. Я правильно понимаю что это чей-то VPN сервер который используется для всех по умолчанию? Могу ли я его поменять на свой? 
2) В интерфейсах используются списки Block, GeoBlock и Meta. Вижу в настройках списков YouTube отдельно, нужно ли настраивать эти списки чтобы все заработало?


Ютюб и инстаграм не работают. У меня MacBook

---

**2026-02-28T18:55:46 | Routerich**
Здравствуйте.
а в zeroblock автоконфигурация awg10 галочка стоит?

---

**2026-02-28T19:44:03 | Yuri Kovalev**
Вот переключился на сеть роутера на котором настроен правильно zeroBlock и у меня заработал ютюб. Третий запрос на фейсбук уже с этой сети

---

**2026-02-28T19:53:11 | Stanislav Gurov**
Из той же секции AI, СМИ открываются. Даже ссылка в браузере открывается, но зависает opkg update и zeroblock update_lists

Включил проксирование роутера, к сожалению, не помогло. Версия 0.6.4-r94

---

**2026-02-28T20:36:59 | Михаил**
А  почему в crontab время обновления списков zeroblock установлено в 9:13?  Как то необычно.

---

**2026-02-28T20:47:34 | Степан**
"zeroblock awg warp" в терминале

---

**2026-02-28T21:07:27 | Anna Bagler**
warp жив? Посмотрите на страничке самого роутера или в панели zeroblock.

---

**2026-02-28T21:10:00 | Роман**
Смотря что нужно. Zeroblock вам Анна скинула, podkop.net это по подкопу. Для запрета 2 в ветке запрет 2 в закрепленных сообщениях.

---

**2026-02-28T21:14:09 | Anna Bagler**
Zeroblock/Podkop.

---

**2026-02-28T22:02:21 | Fredd**
Тему Zeroblock читайте,много интересного узнаете,там есть мануал в закрепе.

---

**2026-02-28T22:02:27 | Anna Bagler**
Можно несколько URL-test в подкопе или возможности zeroblock использовать.

---

**2026-02-28T23:05:00 | Роман**
В тему zeroblock пишите.

---

**2026-03-01T00:05:59 | Роман**
В zeroblock есть похожий функционал, только сервера переключаются по пингу.

---

**2026-03-01T00:11:49 | Денис Азаров**
Это у меня с подкопа, а у тебя скрин с zeroblock? То есть его надо ставить? Подкопа не старый вроде - месяц или два назад ставил..

---

**2026-03-01T00:40:55 | Роман**
Если нет, сброс и zeroblock, кмк так проще.

---

**2026-03-01T00:57:18 | Anna Bagler**
Тогда сброс, zeroblock и пока бесплатные варианты использовать. Или уточните у поставщика особенности. Прямо сейчас на телефоне конфигурация из файла срабатывает?

---

**2026-03-01T01:12:56 | Anna Bagler**
Пробуйте zeroblock и это как подписку. Если не поможет, просите прямые ссылки vless, ss или ещё какие у поддержки своего поставщика.
Попробуйте попросить у них другой конфиг для awg.

---

**2026-03-01T01:21:13 | Nook Scheel**
zeroblock есть в apk под 25?

---

**2026-03-01T02:27:15 | iamkokos**
Добрый день. А мне, чтобы ставить ZeroBlock - роутер сбрасывать надо? В нём подкоп уже стоит

---

**2026-03-01T10:21:21 | Роман**
Да. У меня Ютуб Дискорд через запрет 2, остальное в zeroblock.

---

**2026-03-01T10:23:08 | Anna Bagler**
Актуален. Можно переходить на zeroblock. Может у вас секция отвалилась.

---

**2026-03-01T11:07:02 | Anna Bagler**
Если навыки есть, то смотреть в сторону zeroblock.

---

**2026-03-01T12:03:53 | Михаил**
А это на zeroblock. И с только ipv4 и на префер ipv4. Вы правы.

---

**2026-03-01T12:07:20 | Anna Bagler**
Из коробки может заработать только yt, если повезёт. Дальше запрет2 и zeroblock. Или запрет + zeroblock.

---

**2026-03-01T12:15:17 | Борис**
Отлично, не знал. Я не ставил sing-box отдельно, как пакет, я просто установил zeroblock, в нем видимо sing-box прекомпилирован с такой поддержкой

---

**2026-03-01T12:20:08 | Роман**
Не для начала, если нужно всё и сразу zeroblock для прокси, запрет 1-2 для ютуба дискорда. Не умеете (не хотите) скрипт 5 (Beta).

---

**2026-03-01T13:22:21 | Kiss_My_Axe**
Вводные приаттачены.

Винда:
Видно, что работает фейкайпи. Следовательно даже без IPv6 шлюза и вообще при отключенном IPv6 на клиенте запрос на загрузку нтцпарти должен быть направлен роутеру.
Видно, что курл не может получить доступ из-за ркн-бана.

Роутер, ZB:
Активна 1 секция. В секции 1 домен нтцпарти. Выход в awg10 (есть поддержка IPv6)
Настройки - фейкайпи для IPv6 включен.
Роутер перезагружен.

Смотрим inet zeroblock, оринтируясь на 2a02:e00:ffec:4b8::1 (нтцпарти IP):
root@roskomnadzor:~#
root@roskomnadzor:~# nft list table inet zeroblock | grep 2a02:e00:ffec:4b8::1
root@roskomnadzor:~#

Смотрим inet zeroblock, ориентируясь на фейкайпи fc00::3 (тот же результат и для IPv4)
root@roskomnadzor:~#
root@roskomnadzor:~# nft list table inet zeroblock | grep fc00::3
root@roskomnadzor:~#
Далее шагнуть не позволяет уровень знаний.

---

**2026-03-01T14:03:03 | Maksim**
я жестко прокрастинирующий чел, полный сто процентный ноль в этом всём что касается темы роутеров, каких то там прошивок, настроек и т.д. и т.п.
Получил роутер 2 месяца назад, и 100500 раз пытался сесть и настроить, но становилось плохо от обилия инфы и в то же время абсолютно полного непонимания с чего начать.
И только вчера смог всё настроить на zeroblock, и пока что всё устраивает.
Не слезая с кресла 18-19 часов сидел холодный голодный, тыкался потому что полностью нормально обходы не хотели работать, внутренний перфекционист давил на меня и я пытался наладить обходы к сайтам которые мне вообще нафиг ни когда не пригодятся.
Сначала с зеро ковырялся, потом сносил всё откатом до завода, и так раз 5 заново на зеро начинал тыкаться.
Потом друг сказал надо на подкопе сделать обходы, скинул мне пост с инструкцией, там типа изи всё и более работоспособное, но у меня ничего не вышло с подкопом и работало еще хуже чем на зероблоке.
Я почти опустил руки, думал уже квн купить на год и ипись оно всё конём.
Но потом просидев еще часов 5, всё таки настроил на зероблоке.
Сейчас пашет прям фул всё чётко, надеюсь это продолжится и дальше, надеюсь это надолго.

---

**2026-03-01T14:56:00 | Bullet for my valentine Poison**
zeroblock есть? нет.

---

**2026-03-01T15:13:47 | Вячеслав Шевченко**
Добрый день подскажите как установить zeroblock есть пошаговая инструкция?

---

**2026-03-01T15:54:12 | Kiss_My_Axe**
Судя по IP фейсбука и ютуба у вас на Zeroblock не работает фейкайпи. Совсем.
В секции party точно снята галка "Отключить FakeIP"?

---

**2026-03-01T16:23:18 | Роман**
Здравствуйте. Из коробки может заработать только Ютуб. Если нет, удалять youtubeunblock и ставить запрет 1-2, если только для Ютуба. Если инста - zeroblock/podkop, если лапки - скрипт 5.

---

**2026-03-01T17:34:30 | Михаил**
Прелесть zeroblock, как и podkop, что при правильной настройке эти ресурсы проходят мимо. И маршрутизируются только выбранные в секциях.

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

**2026-03-01T19:22:35 | Роман**
В канал упирается, zeroblock и zapret2.

---

**2026-03-01T19:30:25 | Михаил**
Меня в подкопии влегкую. И на этом же роутере через zeroblock ну никак. Одно стопарю, другое пускаю. Через квн естественно на ура.

---

**2026-03-01T19:57:36 | Stanislav Gurov**
Здравствуйте!

Есть проблема во взаимодействии zeroblock + tailscale, включенный tailscale каким-то образом влияет на работу сингбокса.

Дано:
- Zeroblock, проксирование списка "Repositories" через оперу.
- Tailscale, роутер принимает маршруты, является выходным узлом и открывает подсеть 192.168.1.0/24


Как воспроизвести?
- Включить tailscale, ввести одну из команд в терминале:
opkg update

curl -v https://github.com

zeroblock update_lists

Все команды зависают. Если tailscale выключить, то отработают. Пробовал включать проксирование трафика роутера в ZB, увы, не помогло. Прикладываю скриншоты с настройками.

---

**2026-03-01T20:10:18 | Serg**
Доброго времени суток. Подскажите, где взять файл ZeroBlock, для установки на новый роутер?

---

**2026-03-01T22:10:57 | Роман**
Обход нужен вижу я... Zeroblock вижу со своим сервером, на бесплатном не работает потому что... 
Warp генератор со сменой локации тоже вижу...
Vless ссылку...

---

**2026-03-01T22:16:26 | Роман**
Ставьте и играйте, кто вам мешает? Ну серьезно?
Я же вам написал, если нужен обход на уровне роутера - ставите zeroblock/podkop - суете туда vless:// или hy:// выбираете список роблокс или games и играете.

---

**2026-03-01T22:26:23 | Роман**
В zeroblock в списке games есть эти игры.

---

**2026-03-01T22:47:04 | Михаил**
Странности двух последних версий. Открытые ресурсы rbc.ru и ya.ru открываются(или даже не открываются) из-под палки.
Если почистить кэш, то открываются в сломанном виде. Даунгрейд к версии 85 полностью исправляет ситуацию. Все летает. Параметры zeroblock естественно теже. Api v1.
Повторяемость полная. Домены из секций и там и там открываются на ура.
Ping и tracert отличий в путях к rbc и ya.ru не выявил.

---

**2026-03-01T23:39:08 | Михаил**
Завтра напрямую роутер  заведу и проверю снова. Но ведь на 85 версии то летает. Вот в чем заковыка.
PS. К слову. Разработчик для нероутеречей убирает часть меню в zeroblock. Так можно и V1 для них сразу прописать, что бы не дергаться с этим каждый раз.

---

**2026-03-02T08:43:52 | Routerich**
она есть в планировщике
# ZeroBlock Monitor
0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
# ZeroBlock Lists Update
13 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-03-02T10:15:27 | Роман**
Совершенно верно, не понравился. Связка zeroblock и zapret2 с автохостлистом полностью покрывает мои нужды.

---

**2026-03-02T10:24:15 | kk**
сделал для теста - pppossh-pppOssh: <POINTOPOINT,MULTICAST,NOARP,UP,LOWER_UP>

выбираем в luci инт-с, жмём сохранить, получаем  - uci set zeroblock.pppSSH.interface='pppOssh'

zb переустановлен полностью, с удалением /etc/config/zeroblock

з.ы с консоли всё замечательно (uci set ...)

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

**2026-03-02T11:06:26 | Роман**
Для вас может быть проще установить zeroblock и воспользоваться автонастройкой awg. 
На сколько я помню там ещё в фаерволе правила надо настраивать. А тут просто свой конфиг внесёте и всё.

---

**2026-03-02T11:18:04 | Anna Bagler**
Если у вас РР, то все функции zeroblock будут доступны.

---

**2026-03-02T11:24:28 | Роман**
Пишите в тему zeroblock.

---

**2026-03-02T11:29:57 | Kiss_My_Axe**
Службы - ZeroBlock есть?

---

**2026-03-02T11:55:34 | N Z**
Добрый день!
Установил два пакета. Сначала zeroblock, потом luci. Понажимал на то, что указано в pdf (извините за обывательский сленг). Но не помогло... Youtube на ТВ не хочет открываться. IPad через wifi и ПК через провод работают (как и до установки zeroblock). Дальше моих знаний не хватает, что бы настроить, я так понимаю. Помогите пожалуйста ))

---

**2026-03-02T11:57:09 | Anna Bagler**
Список yt в zeroblock или его запрет2 на себя забрал и какой тв?
Код выполните он Kissa и скрин киньте.

---

**2026-03-02T12:03:11 | Anna Bagler**
Тогда отключить и стопнуть анблок. Список yt и cdn google выбрать в секции awg zeroblock.
Или если @BFMVPoison захочет помочь, теребонькать запрет2.

---

**2026-03-02T12:11:35 | N Z**
Извините за уровень моих вопросов. Это речь уже о Службы > ZeroBlock > Секции маршрутизации?

---

**2026-03-02T12:19:31 | kk**
так. у вас в конфиге зероблока приходит qwe ? 
zeroblock.ssh1.interface='qwe' ?
и это работает?

---

**2026-03-02T12:29:03 | Anna Bagler**
Изучайте списки, ссылка на них есть в теме Zeroblock. Вдруг вам иная запрещенка ещё нужна. Интерфейс awg10 может падать периодически. Его надо будет перезапускать в Сеть - Интерфейсы.

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

**2026-03-02T15:26:01 | Oleg Belskiy**
Здравствуйте. Поставил ZeroBlock на чистую систему, при установке были ошибки  как на скрине, вся запрещёнка при этом открывается. По ощущениям работает лучше Podkop, спасибо вам за это, хотя всё равно лучше конечно посмотреть на длительной дистанции использования. Вот ещё странность, может сможете мне объяснить в чём может быть причина: добавил третью секцию со своим ключом, ничего из списков не выбирал, на Хроме speedtest определяется oslo, то есть идёт через верхний прокси как и должно быть, а вот в Яндексе определяется ip сервиса, который в новой секции. Убираю галочку с третьей секции и Яндекс показывает уже мою локацию и мой ip. Вопрос как? Там же секция с ключом пустая, она же не должна пускать весь трафик через себя по идее. Скрин прилагаю.

---

**2026-03-02T15:58:21 | Ruslan**
подскажете что сейчас лучше работает ZeroBlock или скрипт №5? стал притормаживать вифи, обновил прошивку,  думаю что лучше накатить

---

**2026-03-02T17:05:38 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.6.4-r104:
  Исправления:
  - VPN interface selector для PPP-протоколов (pppossh, pptp, l2tp) — LuCI отдавал имя UCI секции вместо реального устройства (напр. ssh1 вместо pppossh-ssh1), sing-box не мог найти интерфейс
  - YACD кнопка — теперь использует hostname текущего подключения вместо LAN IP роутера
  - Время обновления списков — новый параметр в настройках (HH:MM) вместо захардкоженного 09:13
  - Удалены предустановленные секции
  - sing-box 1.12.17 не поддерживает timestamp: false для stdout. PR #1391 открыт. Как примут, фикс должен сработать
#ZeroBlock

---

**2026-03-02T18:05:43 | Роман**
rm /etc/config/zeroblock* && reboot
Это делали? Или сброс полностью?

---

**2026-03-02T18:55:30 | Mallory**
добрался тут до обновления зебры на своем роутере, все завелось по дефолту, но после того как добавил еще один awg  интерфейс и секцию к нему зебра стала ругаться на проверке дефолтного awg

[zeroblock] Starting ZeroBlock...
[system_monitor] WARP is not working (ping failed)
[zeroblock] AWG health check failed, restarting interface...
[system_monitor] WARP is not working (ping failed)
[zeroblock] AWG still not working after restart
[zeroblock] ZeroBlock started successfully
[clash_api] /awg10/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 504

решилось все методом бубна - остановкой нового awg интерфейса, перезапуском зебры (после чего ошибки исчезли) и потом запуском нового интерфейса

---

**2026-03-02T19:08:43 | kk**
видимо баг? удалил полностью zb, включая config/zeroblock. поставил 104 (была 97) и ни одной секции не добавилось в "Routing Section", даже те "инт-сы", которые есть в системе (аwg10, opera)
включил дебаг, добавил pppOssh(ssh1) секцию (других в списке нет), перезапустил, увидел: 
... 
Checking WARP connectivity via awg10 to 1.1.1.1
Checking Opera Proxy via HTTP proxy 127.0.0.1:18080
...
Loaded section: ssh1 (type=1)
Added VPN interface outbound: ssh1 -> pppossh-pppOssh
(теперь тут ок)
соответственно в конфиге только секция zeroblock.ssh1, с верными настройками, которая теперь сохраняет\работает как надо. по логам zb пинг через awg проходит, хттп чек через оперу тоже (zb их видит получается). (uci show zeroblock из секций показывает только добавленную ssh1)
тут протупил, спасибо, что сразу указал на это =)))
timestamp.. вот тут я лопухнулся, думал раз есть true, должен быть и false, но жизнь поправила=))
глянул PR#1391, печально конечно... =)
upd. отбой. как и предпологал...работает без задвоения=) надо просто убрать из 00-log timestamp

---

**2026-03-02T19:24:42 | Роман**
В zeroblock Ютуба нет?

---

**2026-03-02T19:41:06 | Михаил**
Уф! Вроде нащупал. На последних трех версиях, после 85-ой, у меня нормально не пускались rbc.ru и ya.ru. Либо это занимало в 10 раз больше времени, либо вообще отваливалось. Со стопнутом zeroblock все таинственным образом начинало летать. После поисков вроде бы нашел разгадку. Виновата секция подписки со списком url в файле с доступом по https. С секцией экспериментировал и не выбрал в ней ни одного списка и домена. И, что забавно, как только выбрал в ней roblox, сайты rbc.ru и ya.ru просто ожили. Убрал - умерли. И почему то в 85 версии все было хорошо, а с 90-х скривило все. И именно с отсутствующими выбранными доменами и списками в секции).
Вот что roblox чудодейственный творит. Api V1.

---

**2026-03-02T19:56:14 | Роман**
Если со смартфона всё нормально, а с ноутбука нет, дело в ноутбуке. 
На крайний случай сброс и попробовать zeroblock, а не подкоп.

---

**2026-03-02T20:23:41 | ㅤㅤ**
Добрый вечер. Как бы решали вопрос по обходу на iPhone по логике Zapret2|Podkop|ZeroBlock и т.п.

Наткнулся на китайский Quantumult X. Целый день возился с их китайскими конфигами. Штука интересная, но непростая в работе. Конфиг сильно ограничен в синтаксисе. AmneziaWG не поддерживает. Зато работает с VLESS (Reality пока не поддерживает).

Быть может я просто закопался и стоит пойти по более простым путям? Каким образом наладить работу по обходу DPI в достаточно закрытой и ограниченной оси. В этом дилемма.

---

**2026-03-02T20:28:55 | Александр Меркушев**
Добрый вечер, подскажите, пожалуйста, что сейчас ставить актуально? Попробовал zeroblock 0.6.4-r85 и интернет не работал вообще (обрывы соединения были, я даже провайдера достал), сегодня сеть вырубилась вообще. Провйадер сказал что видит "множественные обрывы соединения), думали в проводах дело. Перешил роутер начиссто - все работает. Ну, кроме ютуба ессно. Вот и думаю что поставить чтобы оживить вацап и остальное, чтобы гарантировано без такого.

---

**2026-03-02T20:30:20 | Routerich**
Заново можете поставить zeroblock, и в случае проблем выслать логи для анализа.

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

**2026-03-02T21:20:44 | Роман**
Если ставить запрет2 через zeroblock - поставить правильно галочки в запрете2.

---

**2026-03-02T23:34:11 | Борис**
Я себе на роутере сделал vless reality сервер. Это бесплатно и помогает обходить белые списки с телефона. Работает это так, что роутер выступает в роли сервера, телефон в роли клиента. Клиент подключается к серверу по протоколу vless с примочками для reality (дополнительные атрибуты в отправляемых пакетах). Из-за того, что клиент сообщает, что идёт на m.vk.com (это неправда), провайдер пускает его трафик до моего роутера, думая, что это сайт ВКонтакте. На деле же роутер выступает выходной нодой для интернета (на роутере в свою очередь установлены zapret2 и zeroblock, позволяющие открывать ютуб, chatgpt и прочие плохие вещи)

---

**2026-03-03T00:07:35 | 🌶️🌶️**
Executing package manager

opkg install /tmp/upload.ipk

Installing luci-app-zeroblock (0.6.4-r104) to root...
Installing sing-box-tiny (1.12.17-r1) to root...

Errors

Collected errors:
 * check_conflicts_for: The following packages conflict with sing-box-tiny:
 * check_conflicts_for:   sing-box * 
 * opkg_install_cmd: Cannot install package luci-app-zeroblock.

The opkg install command failed with code 255.

---

**2026-03-03T00:21:28 | Борис**
У меня нет для такого времени, но могу подсказать в какую сторону смотреть - в этой группе поиск по сообщениям "vless reality", в основном в теме Zeroblock я писал свой опыт и даже скидывал конфиги, как я sing-box настроил в качестве сервера

И да, для роутеров routerich есть пакеты в репозитории, называются они xray-core или sing-box - эти программы выступают как сервер для vless, выбирать можно любую. Я начинал с xray, т.к. Reality это их собственная разработка, и возможности у этой утилиты больше. Sing-box является аналогом xray-core. Также программа Zeroblock от Routerich является обёрткой для sing-box, то есть в каком-то смысле в зероблок встроена возможность создавать #reality сервер на роутере

---

**2026-03-03T00:40:30 | Anna Bagler**
Присваивайте IP телевизору на роутере, чтоб не менялся, идите в подкоп, секция discord, полностью маршрутизированные IP-адреса и там вписывайте адрес ТВ. Если не поможет или будет не очень стабильно, то сброс настроек роутера и переход на zeroblock. Может и @BFMVPoison тогда поможет с zapret2 для LG.
Если ТВ старый, рассмотрите возможность покупки тв-бокса на андроиде к нему.

---

**2026-03-03T00:52:45 | Anna Bagler**
Сброс настроек и zeroblock+zapret2, youtubeUnblock удалить.

---

**2026-03-03T00:57:04 | Inko**
Эм я чет не очень понимаю... я вроде поставил все по мануалу через пакеты поставил загрузить пакет zeroblock_0.6.4-r104_aarch64_cortex-a53, затем так же luci-app-zeroblock_0.6.4-r104_all... Затем зашел в зероблок в автонастройку поставил установить опера прокси и настроить амнезия вг варп... и чет после всего и после перезагрузки в секциях маршрутизации ничего не появилось... хотя какие-то блоки обходит ютуб работает например, но гемини отвалилась... хм... теперь в автонастройке пишет что опера прокси уже установлен а в амнезии интерфейс авг10 уже существует... окей авг10 интерфейс даже есть в интерфейсах... но где списками управлять? Не понятно чет, написано в мануале что зайдите и настройте списки а где если в секциях маршрутизации пусто...? Ничего не понятно...
sing-box почему-то сперва писало запущено, а сейчас пишет остановлена перезапуск или запуск не помогает...

Вот если что прикрепляю диагностику если надо еще что-то говорите...

---

**2026-03-03T01:17:54 | Kiss_My_Axe**
Подкоп работает так - создаёшь секцию, прописываешь выходной канал, свой, или бесплатный.
Все адреса, помещённые в данную секцию списками сообщества, или вручную, уходят в интернет через прописанный в секции канал.

Запрет на 100% совместим с подкопом при условии, что ya.ru прописан ИЛИ в подкопе, ИЛИ в запрете.
То же справедливо и для более удобного ZeroBlock.

---

**2026-03-03T03:06:50 | Евгений Фролов**
Обязательно ли надо
zeroblock.WARP.disable_fakeip='1'
Для секции с туннелем awg10?

---

**2026-03-03T04:57:12 | IT**
Zeroblock это ваше творение?

---

**2026-03-03T05:12:35 | De1Dev**
Другой мой старый роутер, на OpenWrt работает.
Этот я подруге заказал, хотел настроить ZeroBlock и Zapret и отдать ей.😅
Но даже не добрался в luci.🥲

---

**2026-03-03T06:45:59 | Anna Bagler**
Скорее всего блок пошел. Попробуйте скрипт из ветки Beta или переходите на zeroblock.

---

**2026-03-03T08:46:27 | Keeper**
Приобрел уже 5 роутеров у этой шикарной команды! Низкий Вам поклон и бесконечная благодарность за труды!

3 установил у родни в своем регионе, 1 сейчас едет на суровый север страны, 1 лежит в запасе.
Я хоть и фанат Mikrotik, но для установки родне и знакомым выбрал данный девайс, ни разу не пожалел, ибо все максимально просто и понятно для человека с любым уровнем знаний.
Поэтому моя задача - это первоначальные настройки и удаленный доступ на всякий случай, а дальше человек уже сам начинает интересоваться.
Буквальный пример: бывший заводчанин 60+ лет, который ни разу не интересовался технологиями уже сам находит и добавляет в podkop'е домены и CIDR'ы для обхода WA 😁

Команда не просто своевременно выпустила на рынок нужный девайс, но и обеспечила поддержку такого уровня, какого многим более крупным вендорам не достичь уже никогда. Одни подробные мануалы чего стоят!
Устройство разворачивается и начинает приносить пользу буквально в несколько кликов.
Отдельно хотелось бы отметить простых ребят из чата, которые помогают в поддержке, тестировании и в развитии продукта.

Отдельная благодарность за ZeroBlock, поставил на последний аппарат, буду тестировать на живых людях 😈

---

**2026-03-03T09:29:00 | Anna Bagler**
Включите точку на смартфоне, подключитесь к ней роутером, обновите списки. Запреты, анблок удалите и ставьте zeroblock.

---

**2026-03-03T09:38:48 | Владимир**
ZeroBlock это форк podkop?

---

**2026-03-03T09:55:38 | Anna Bagler**
Ключ в zeroblock.

---

**2026-03-03T10:04:19 | Stas Ivanov**
А подскажите, в zeroblock есть возможность пустить весь трафик через впн?

---

**2026-03-03T10:05:32 | Anna Bagler**
Секция сatch all. Вам в полный мануал по zeroblock.

---

**2026-03-03T11:54:29 | Denis**
Зачем при дефолтной установке zeroblock вместе с zapret2 в секции awg10 установлен youtube Community List? Awg же могут конфликтовать с zapret2 за дележ трафика youtube

---

**2026-03-03T12:17:47 | Роман**
Если лапки - скрипт 5 из закрепа ветки интернет без границ или бета из ветки бета, если более менее продвинутый пользователь - zeroblock.

---

**2026-03-03T12:24:07 | Даниил Хамчишкин Самолёт+**
А какое принципиальное отличие Скрипта 5 от Zeroblock?

---

**2026-03-03T12:25:48 | Даниил Хамчишкин Самолёт+**
С Zeroblock справлюсь, если Samsungi шил?)

---

**2026-03-03T12:44:48 | Daniil**
добрый день.Создал новый интерфейс с конфигом wireguard(awg0).Добавил его в новую секцию zeroblock.В секции оставил только мессенджеры.Так телега чет вообще не очень,а вот если этот конфиг применить в приложухе (клиенте)на тел или пк то все летает и грузит быстро фото и видео.Где я свернул не туда?)помню было тут обсуждение похожей проблемы,но вот  решения не помню(и есть ли оно).Спасибо

---

**2026-03-03T12:52:27 | Anna Bagler**
Zeroblock похож на подкоп, но лучше функционал, разработка РР, т.е. разработчик на связи. Запрет - дурилка.

---

**2026-03-03T12:52:50 | Роман**
Zeroblock перенаправляет ваш трафик на другие сервера, запрет режет трафик так, что тспу его пропускает. Разные принципы работы.

---

**2026-03-03T14:29:02 | Роман**
Хорошо, напишите по обывательски, по простому, принцип работы zeroblock?

---

**2026-03-03T15:07:54 | Anna Bagler**
Не работает только часть запрещенки, верно? Желательно прошивку обновить и скрипт 5 вновь запустить. Или перейти на zeroblock, если навыки позволяют.

---

**2026-03-03T15:12:42 | Routerich**
а конкретнее? что не работает?
что диагностика ZeroBlock показывает?

---

**2026-03-03T15:14:11 | Aleksandr**
Warp лежит. Хотел команду Zeroblock awg warp в терминале написать, но ошибка при подключении к терминалу.

---

**2026-03-03T15:44:17 | Nook Scheel**
zeroblock же динамично не может запрашивать контекст у процесса соседнего?

---

**2026-03-03T16:38:40 | Routerich**
ага, начинаю писать zeroblock2 с искуственным интеллектом, чтобы он сам всё роутил. ссылки в интернете искал тебе и за хлебом следил

---

**2026-03-03T16:46:42 | Rom@n**
Ну как бы:
T
ue Mar  3 16:40:17 2026 user.notice zeroblock: No sections configured, restoring DNS and skipping start
Tue Mar  3 16:40:17 2026 daemon.info zeroblock[15965]: [dns_manager] No DNS backup found, nothing to restore

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

**2026-03-03T16:52:33 | Routerich**
ничего не настроено
Tue Mar  3 16:40:17 2026 user.notice zeroblock: No sections configured, restoring DNS and skipping start

---

**2026-03-03T18:25:09 | Aleksandr**
Через несколько минут WARP отключен. Команда Zeroblock awg warp или перезапуск интерфейса по web морде оживляет его на несколько минут 2-3 примерно и снова WARP отключен по статусу в обзоре.

---

**2026-03-03T18:31:13 | Routerich**
Искать домены игры и добавлять их в Zapret, а с Zeroblock убрать

---

**2026-03-03T18:38:16 | Роман**
А как она (игра) в zeroblock попала? 
Тут многие домены и ip ищут чтобы поиграть, а у вас автоматом 🧐
В списке games ареха нет.

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

**2026-03-03T19:00:51 | Routerich**
никуда, а вот ключ/конфиг из неё в новую секцию zeroblock

---

**2026-03-03T20:16:47 | Routerich**
zeroblock awg warp в терминале

---

**2026-03-03T20:32:02 | Роман**
Zeroblock не поднимется пока нет ни одной секции.

---

**2026-03-03T21:28:05 | Павел**
Пост выше обязателен к прочтению! выше микро мануал
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
#ZeroBlock

---

**2026-03-03T21:37:31 | В.**
Добрый вечер.
Можно ли в ZeroBlock при настроенном Xray на конкретном устройстве разделить трафик: TCP пускать через туннель, а UDP не трогать?

---

**2026-03-03T22:15:58 | HiLLL**
в терминале введите zeroblock awg warp

---

**2026-03-03T22:45:22 | Владимир**
Добрый вечер. У меня в списке Служб нет Zeroblock. Как его отобразить/подключить?

---

**2026-03-03T22:58:22 | РУЗОВ Дмитрий**
жду коробочку, начитался тут, пипец...
я правильно понимаю, что лучше сразу смотреть в сторону Zeroblock и Запрета?

---

**2026-03-03T22:58:44 | Роман**
В секцию со своим сервером в zeroblock/podkop.

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

**2026-03-03T23:09:19 | Михаил**
К слову. Читайте внимательно мануал. Можно придумать десяток способов глушить работающие сайты через zeroblock. От неправильно выбранных списков до галок с полным проксированием трафика устройства через дохлый впн.

---

**2026-03-03T23:20:30 | Anna Bagler**
Вам прошивку надо обновлять и скрипт запускать, а лучше на zeroblock переходить.

---

**2026-03-03T23:22:30 | Alex**
по поводу zeroblock надо почитать)

---

**2026-03-04T00:00:01 | Роман**
Через пакеты можно установить. Убрать из секций Ютуб zeroblock/podkop. Отключить youtubeunblock.

---

**2026-03-04T00:33:49 | Anna Bagler**
Стратегии пробовать https://t.me/routerich/3845/509958
Или тогда в zeroblock/podkop.

---

**2026-03-04T08:09:11 | Anna Bagler**
На первом шаге вы воспользуетесь Мастером настройки, чтобы настроить интернет и беспроводные сети. На втором шаге, в зависимости от знаний, вам нужен будет zeroblock из закрепов темы Zeroblock Beta и настроить его или скрипт №5 из закрепов темы Интернет без границ. Дальше с большей долей вероятности вам ничего не надо будет, только настройка отдельных служб.

---

**2026-03-04T09:27:29 | De1Dev**
Всем привет! Извините за беспокойство.
При использовании ZeroBlock, работает singbox, но не работает xray, в галочках, написано установлено ядро X-ray (мб баг, и не установлен).
Singbox прибавляет нагрузку к пингу на100мс?
Можно ли через X-ray её снизить?
Просто, через приложение V2Rayn у меня пинг 43~мс, а в singbox ZeroBlock показывает на 100 или 150~мс больше, это нормально?
Понизить возможно?

---

**2026-03-04T10:07:17 | Anna Bagler**
С zeroblock работает контроль доступа, переходите на него.

---

**2026-03-04T10:07:18 | Роман**
Шок! Zeroblock ВСЁ! Разраб кормит людей завтраками, проект заброшен!

---

**2026-03-04T10:39:33 | Garsia**
В браузере я знаю как. Там вроде речь шла о zeroblock

---

**2026-03-04T10:53:20 | Garsia**
Помогите, плиз, разобраться в ситуации. 
У меня стоит Zapret2 (включена секция Ютуба) и ZeroBlock. В ZB Опера прокси и AWG10 (те, что по умолчанию) отключены. 

Добавил свой конфиг AWG (создал новый интерфейс) и через него в ZB пустил несколько списков сообщества (AI, Meta и др.), но не Ютуб. При этом в Ютубе появилась реклама (той страны, в которой мой сервер с AWG).

Почему такое может быть, и куда копать? 
Самое интересное: если в секции маршрутизации выключить все списки сообщества и оставить только свои домены, реклама в Ютубе уходит.

---

**2026-03-04T11:03:13 | Anna Bagler**
Podkop - точечная маршрутизация. У РР есть свой zeroblock c возможностью cекций без списков.

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

**2026-03-04T11:42:43 | Routerich**
попробуйте стопнуть его и проверить.
если всё ок, то переходите на ZeroBlock, там есть родительский контроль

---

**2026-03-04T11:43:31 | Garsia**
Галку поставил, применил, перезапустил интерфейс и ZeroBlock. Всё равно реклама :(

---

**2026-03-04T11:47:17 | Routerich**
да, пользуйтесь в ZeroBlock.
потом отпишитесь, как работает оно у вас, добились ли желаемого.

---

**2026-03-04T11:50:51 | Routerich**
да, лучше сразу переходите на ZeroBlock и его блокировки, так как скорее всего так и будут проблемы с штатным решением из-за этого

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

**2026-03-04T12:04:04 | Роман**
rm /etc/config/zeroblock* && reboot - этого же явно будет мало (к удалению пакетов) что-бы полностью вынести zb? Или сброс проще сдлать?

---

**2026-03-04T12:05:50 | Роман**
Полностью удалить zeroblock. Что-бы не сбрасывать роутер, сотрётся же.

---

**2026-03-04T12:10:40 | Роман**
Возможно у нас возникло недопонимание. Моя цель полностью удалить zeroblock. Иду в пакеты и удаляю оба, затем командой rm /etc/config/zeroblock* && reboot тру конфиг. Этого достаточно для полного удаления zeroblock? Если нет, то какие команды нужны в терминал (или иные действия) для полного удаления.
Как то так.

---

**2026-03-04T12:16:09 | Routerich**
rm /etc/config/zeroblock* /tmp/zeroblock_status.json && rm -rf /tmp/zeroblock /etc/sing-box/subscriptions /etc/zeroblock
rm /etc/config/zapret2* && rm -rf /opt/zapret2

---

**2026-03-04T12:17:09 | Garsia**
Думаю, проблема не в этом. 
Если в ZeroBlock в секции маршрутизации отключить все списки сообщества, а оставить только свои домены, то реклама в Ютубе пропадает. В этом случае он и работает шустрее - то есть сразу видно, что с любым включенным списком Ютуб идёт через ВПН, а без списков - через Запрет.

Ну что за чудеса...

---

**2026-03-04T12:38:07 | Роман**
Удалил через пакеты zapret2, zeroblock, затем вашу команду в терминал для удаления остатков zeroblock.
Установил последний zb, в нем поставил галку скачать zapret2, он скачался, а мои секции остались. Вопрос, как полностью удалить zapret2 с роутера?

---

**2026-03-04T13:23:57 | Fredd**
Целая тема Zeroblock BETA,там и обсуждение,и пакеты с мануалом в шапке

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

**2026-03-04T14:49:01 | Routerich**
Здравствуйте.
либо Podkop, либо zeroblock

---

**2026-03-04T14:49:42 | Routerich**
zeroblock более точечный и там их много, списков

---

**2026-03-04T14:56:15 | Роман**
Да там и подкоп, и старый zeroblock, фарш короче.

---

**2026-03-04T15:24:38 | Anna Bagler**
ipvfoo в браузер + vpn и потом смотрим, домены второго уровня добавляем в zeroblock/podkop.

---

**2026-03-04T15:52:50 | Petr Shcherbinin**
[sing_box_manager] Failed to write config to /tmp/zeroblock/sing-box.d/40-route.json.tmp.24922: No space left on device
[config_builder] Sing-box failed to start with full configuration

вижу это снова по упавшему сайнбоксу

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

**2026-03-04T16:41:06 | Роман**
Удалить/остановить youtubeunblock, если нужен только Ютуб - запрет 1/2, если Вацап/инста - скрипт 5/бета/zeroblock.

---

**2026-03-04T16:42:51 | -Miracle**
а как установить этот скрипт zeroblock

---

**2026-03-04T16:44:37 | Роман**
Скрипт 5 - закреп ветки интернет без границ, скрипт бета - закреп ветки бета, zeroblock  - закреп ветки zeroblock.

---

**2026-03-04T16:44:46 | Артем Михайлов**
Добрый вечер!
В 2х словах, что такое ZeroBlock?
В каких случаях его нужно ставить ?

Полистал закрепленные, ни 1 информационного сообщения для общего понимания =\

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

**2026-03-04T17:49:17 | Роман**
Решение найдено для игры MK1, эти домены в zeroblock/podkop:

api.wbgames.com
wb-hydra.wbgames.com
mortalkombat.com
amazonaws.com.
bugs.wbgames.com
telemetry.wbgames.com
cdn.wbgames.com

Плюс скопировать все cidr:

https://github.com/123jjck/cdn-ip-ranges/blob/main/aws/aws_plain_ipv4.txt

Взято из соседнего чата itdog.
#games

---

**2026-03-04T17:58:27 | Den**
Доброго всем. Подскажите, в ASU пакет Zeroblock часом не добавили?

---

**2026-03-04T18:00:58 | -Miracle**
подскажите пожалуйста я установил zeroblock  а есть ли монуал как его теперь настроить ?

---

**2026-03-04T18:06:30 | Святос**
Либо есть тема Zeroblock, с нами весело

---

**2026-03-04T18:35:11 | Александр**
Как правильно обновить ZeroBlock?

Установил поверх, перезагрузка роутера. Удалил 0.6.4-r8, установил с нуля. 
Во всех вариантах, всё равно версия 0.6.4-r8 с сохранением настроек, но в "пакетах" новая.

---

**2026-03-04T20:10:45 | Александр**
Появилась проблема на 0.7.0-r2. А именно, при включённом ZeroBlock, Гостевая сеть становится без интернета, отключаю ZeroBlock, гостевая работает.

Изначально гостевая настроена по гайду:
https://t.me/routerich/499562
На версии ZeroBlock 0.6.4-r8 всё работало.

---

**2026-03-04T20:23:53 | Fredd**
тема Zeroblock BETA.Там два пакета для установки,и мануал.Только перед тем как что-то начинать делать-внимательно и неспеша прочтите мануал!

---

**2026-03-04T20:40:25 | Александр**
Гостевая была создана, чтобы она была постоянно чистой без VPN. А обычная WiFi сеть всегда под VPN.

Теперь при включённом ZeroBlock, интернет пропадает на созданной гостевой сети. Стоит отключить ZeroBlock, интернет появляется на гостевой.

---

**2026-03-04T21:08:25 | Smallin**
Добрый день! Подскажите, в чём преимущество ZeroBlock перед Podkop?
В двух словах
Если все устраивает в методе №5, помимо медленной загрузки тг, есть смысл протестировать?

---

**2026-03-04T21:50:54 | Александр**
Так здесь сказано, по аналогии с Podkop.
https://t.me/routerich/499562

Последний пункт оставался. Я так понял, это как раз выбрать гостевую в "Входящие интерфейсы", но только в ZeroBlock. + ещё кто-то мне отвечал из темы вопросов, что нужно выбрать в этом пункте гостевую.

Но даже если убрать галку, на 0.7.0 гостевая не работает при Вкл. ZeroBlock. На 0.6.4 я ковыряю настройки, вроде как завелось. Создавал с нуля гостевой интерфейс.

Сейчас пока эксперементирую перед сном, накатил 0.7.0, всё, гостевая померла.

---

**2026-03-04T22:25:24 | Routerich**
Здравствуйте.
Есть ещё Zeroblock, можете его опробовать.

---

**2026-03-04T22:30:01 | Aндрей**
пардон за тупой вопрос, zeroblock это альтернатива обходам из скрипта 5? нсли да, то есть скрипт для терминала чтобы его затестить?

---

**2026-03-04T22:39:02 | Anna Bagler**
Если вы поставили zeroblock или подкоп, то вписывать отдельно не надо, списки проверить в секции с proxy.

---

**2026-03-04T22:43:50 | Александр**
Всю строку? 127.0.0.1#5359 

Раньше получается этого перенаправления не было?

И ещё, как удалять ZeroBlock, чтобы и его данные полностью удалялись? Хотело бы ставить  при необходимости с удалением данных ZeroBlock.

---

**2026-03-05T00:12:33 | dasehak**
что делать если zeroblock игнорирует настройку dns в routing sections?
UPD: мой косяк, был врублен "Auto-load Sections"

---

**2026-03-05T00:22:58 | Garsia**
Ошибка ушла после включения галки "Перехват ДНС" в настройках. 
А для чего вообще эта галка? Разве перехват ДНС не является одной из главных функций ZeroBlock?

---

**2026-03-05T00:33:05 | Den**
Спасибо. Так получилось. Задумка, кроме этого, была в том, чтоб с включенным Тейлскейл трафик с телефона шел через Zeroblock. Может просветите, что еще жмакнуть нужно, чтоб заработало? Exit Node включил.

---

**2026-03-05T00:37:20 | Владимир Волков**
По инструкции к тейлу найдите слово zeroblock, там есть галочка проксирование трафика роутера. У некоторых по пока непонятным причинам не работает, но мало ли, вы не включили

---

**2026-03-05T05:43:33 | IT**
Zeroblock это более удобная замена podkop? Назначение у них одинаковые, направлять трафик в нужные дырки?

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

**2026-03-05T06:11:15 | Routerich**
Проверьте, потом расскажете.
Возможно будут проблемы если используете Podkop / zeroblock

---

**2026-03-05T06:13:49 | Алексей Емельянов**
А обойти родительский контроль zeroblock ребёнок может использованием VPN на мобильном устройстве или включив iCloud Private Relay?

---

**2026-03-05T06:16:07 | Anna Bagler**
Проверяйте. Проверен только контроль доступа на роутере с zeroblock.

---

**2026-03-05T08:53:22 | Anna Bagler**
Если изучите и разберетесь по мануалу, то zeroblock, иначе скрипт №5.

---

**2026-03-05T08:57:52 | Dmitriy Vorobiev**
Купил уже третий родителям - завел все через tailscsale, везде настроил zeroblock через свои впн-ы с subscribe link - какая же красота, все летает. Мама счастлива что ни в телевизоре ни в телефон с планшетом больше не надо мучаться с vpn. Огромная благодарность за устройство и софт. ❤️

---

**2026-03-05T09:14:22 | Алексей🈴**
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: no lease, failing
Collected errors:
 * resolve_conffiles: Existing conffile /etc/config/zeroblock is different from the conffile in the new package. The new conffile will be placed at /etc/config/zeroblock-opkg.

с 0.6.2 до 0.7.0 апался - лучше бы конфиг от новой версии закинуть?

---

**2026-03-05T09:45:50 | Александр Ткаченко**
Свой vless, пользуюсь ZeroBlock

---

**2026-03-05T11:49:09 | Anna Bagler**
Если есть навыки, то вы можете ставить zeroblock и использовать его со своей ссылкой https://t.me/routerich/394153/520562 или https://t.me/routerich/3845/245550

---

**2026-03-05T11:49:10 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.0-r7:
  Исправления:
  - Исправлен dns резолвинг для гостевой сети, исключенной из обработки zeroblock
  - Исправлен поломанный youtube API
#ZeroBlock

---

**2026-03-05T12:29:46 | Routerich**
Здравствуйте. 
ставьте zeroblock.

---

**2026-03-05T12:33:48 | СН**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.0-r7:
  Исправления:
  - Исправлен dns резолвинг для гостевой сети, исключенной из обработки zeroblock
  - Исправлен поломанный youtube API
#ZeroBlock Накатывать можно поверх старого, или роутер на завод?

---

**2026-03-05T12:57:16 | Garsia**
А может уже можно добавить ZeroBlock в "Пакеты" на роутере? Чтобы обновлять одной кнопкой. :)

---

**2026-03-05T13:08:08 | Вячеслав Шевченко**
Здравствуйте. а инстаграмм и роблокс реально сделать имея zeroblock+zapret2 ?

---

**2026-03-05T13:10:40 | Владимир**
ZeroBlock 0.7.0-r7
   хм... сейчас даже полностью снес ЗБ, поставил из пакетов, он у меня все равно пишет Версия 0.7.0-r2 в Luci

---

**2026-03-05T13:47:12 | Роман**
Установить zeroblock/podkop и вставить вашу ссылку.

---

**2026-03-05T13:55:49 | Anna Bagler**
Переходить на zeroblock. Смотреть и пробовать другие ограничивающие пакеты, кроме того, что есть.

---

**2026-03-05T13:57:08 | Роман**
Ставьте zeroblock - там контроль работает.

---

**2026-03-05T13:58:32 | Anna Bagler**
Если у вас LG, то вам в запрет2 и просить о помощи @BFMVPoison 
В любом случае лучше использовать связку zeroblock и zapret2.

---

**2026-03-05T14:54:01 | Anna Bagler**
Zeroblock ставьте. Смотрите полный мануал по нему.

---

**2026-03-05T15:19:42 | Anna Bagler**
Если совсем не хотите разбираться с zeroblock, то обновиться и скрипт 5, как и раньше, будет вам знакомый podkop.

---

**2026-03-05T16:40:15 | Роман**
Отключить обходы, протестировать. Запрет не меняет локацию, вам нужен zeroblock/podkop.

---

**2026-03-05T16:55:47 | Роман**
Нет, правда zeroblock.

---

**2026-03-05T17:17:05 | Stas Ivanov**
Ребят, сорян за вопросы, но я действительно не понимаю.
Я использовал zeroblock, создал секцию со своим vless URL, оставил только ее включенной и ничего не работает (интернетометр видит мой ip соответствующий vless) но на этом все, входящая/исходящая скорость 0)
Компания предоставляющая VPN заверяет, что сейчас не работает ни один способ и готова вернуть деньги.
Но я вижу, что у вас работает, судя по чату.
Либо я не правильно что-то сделал, либо менять того, кто предоставил сервер, либо ничего не сделать...помогите разобраться пожалуйста

---

**2026-03-05T17:39:36 | Stas Ivanov**
Ну как вы и сказали zeroblock стартовал вроде как...однако наверху автозагрузки сбились

---

**2026-03-05T18:11:45 | Роман**
Логи warn, логирование singbox - применить. В диагностике обновить - отдача - лог в текстовои варианте в ветку zeroblock.

---

**2026-03-05T18:23:30 | Stas Ivanov**
Видимо который zeroblock beta

---

**2026-03-05T19:28:21 | Роман**
Вы писали про 4х человек. Я тестировал несколько часов, был только один вылет из катки. У меня и запрет 2 и zeroblock. 
Если явно не указать фортнайт в этих "приложениях" - конфликтов быть не должно. 
Или у вас первый запрет?

---

**2026-03-05T19:28:42 | Stas Ivanov**
ASU пройдено успешно...теперь надо снова по гайду Zeroblock все службы (Зероблок запрет и прочие) накидывать как я понял.

---

**2026-03-05T19:38:19 | Routerich**
Здравствуйте.
Либо искать домены игр и добавлять их в Podkop / zeroblock, либо полностью устройство в VPN пускать

---

**2026-03-05T19:45:19 | Den**
Доброго дня всем! Настроил ZB и tailscale. Подключился через смартфон по tailscale (подключен к моб. интернету). В настройки роутера зайти возможность есть, а вот трафик с мобилы не идет через Zeroblock. Подскажите пожалуйста, что упустил? Все настройки делал, как прописано в Wiki...

---

**2026-03-05T20:13:14 | AlexChus**
Название роутера из панели управления должно быть. + Лучше в tail scale (удаленный доступ- remote control) тему пишите.
Текущая для zeroblock

---

**2026-03-05T22:11:52 | Руслан**
@routerich Здравствуйте, сижу на подкопе. Нужно ли переучиваться на zeroblock? Есть или может планируется скрипт для ZB?

---

**2026-03-05T22:23:02 | Роман**
Всё есть в zeroblock. И автонастройка, и авто скачивание запрета 2.

---

**2026-03-05T22:38:59 | Михаил**
А как с dns в zeroblock? Мимо не проходит? В диагностике все зеленое?

---

**2026-03-05T22:41:08 | Михаил**
Для того, что-бы пустить через byedpi только определенные домены. С помощью podkop или zeroblock.

---

**2026-03-06T07:04:26 | Azizkhan**
Fri Mar 6 10:11:59 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock(0.7.0-r7)...
[zeroblock] ZeroBlock started successfully
[clash_api] /main__auto/delay?url=http://www.gstatic.com/generate_204&timeout=30000 failed: HTTP 503
[clash_api] /main__auto/delay?url=http://www.gstatic.com/generate_204&timeout=30000 failed: HTTP 503
[clash_api] /main__auto/delay?url=http://www.gstatic.com/generate_204&timeout=30000 failed: HTTP 503
[clash_api] /main__auto/delay?url=http://www.gstatic.com/generate_204&timeout=30000 failed: HTTP 503
[clash_api] /main__auto/delay?url=http://www.gstatic.com/generate_204&timeout=30000 failed: HTTP 503
[clash_api] /main__auto/delay?url=http://www.gstatic.com/generate_204&timeout=30000 failed: HTTP 503
Fri Mar 6 10:15:33 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[clash_api] /main__auto/delay?url=http://www.gstatic.com/generate_204&timeout=30000 failed: HTTP 503
[clash_api] /main__auto/delay?url=http://www.gstatic.com/generate_204&timeout=30000 failed: HTTP 503
[clash_api] /main__auto/delay?url=http://www.gstatic.com/generate_204&timeout=30000 failed: HTTP 503
[clash_api] /main__auto/delay?url=http://www.gstatic.com/generate_204&timeout=30000 failed: HTTP 503
[clash_api] /main__auto/delay?url=http://www.gstatic.com/generate_204&timeout=30000 failed: HTTP 503
[zeroblock] ZeroBlock stopped successfully
Fri Mar 6 10:16:07 2026 user.notice zeroblock: Starting ZeroBlock...

---

**2026-03-06T09:11:04 | Андрей**
Добрый день. Подскажите, в zeroblock можно выбрать готовый список roblox, как это реализовано в крайней версии подкопа? Или тут самому нужно собирать спиок доменов/ip?

---

**2026-03-06T09:17:30 | Роман**
Зачем покупать? Сам поднял и всё. Добавлять в zeroblock. Стабильность в наше время никто не обещает.

---

**2026-03-06T09:17:42 | Routerich**
Здравствуйте.
создавать интерфейс в 
Сеть->Интерфейсы->AmneziaWG->Импортировать конфигурацию
потом создаёте секцию в zeroblock с типом VPN и добавленным интерфейсом

---

**2026-03-06T09:21:17 | Роман**
Я конкретно про zeroblock.

---

**2026-03-06T10:11:23 | HiLLL**
Но всё равно ошибки сыпет 
[http_client] curl_easy_perform failed: Error
[ruleset_manager] API request failed (ret: -4, code: 0, size: 0)
[ruleset_manager] Failed to load community lists from any source
[lists_loader] Failed to load community index for v2 API
[config_builder] Download failed (1 errors), enabling auto_fallback two-stage via OPERA
[http_client] curl_easy_perform failed: Error
[ruleset_manager] API request failed (ret: -4, code: 0), assuming access allowed
[http_client] curl_easy_perform failed: Error
[ruleset_manager] API request failed (ret: -4, code: 0, size: 0)
[ruleset_manager] Failed to load community lists from any source
[lists_loader] Failed to load community index for v2 API
[config_builder] Some lists failed to download (1 errors)
[zeroblock] ZeroBlock started successfully

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

**2026-03-06T10:47:54 | None**
Наткнулся на этот роутер случайно на 4pda, решил взять. Установил ZeroBlock, настройка элементарная - всё шо було заблокировано теперь работает. Отдельное спасибо команде RouteRich за крутой продукт

---

**2026-03-06T11:54:40 | Артем Александрович**
Один мой товарищ купил данный роутер и так сильно его нахваливал, что я решил купить. Сначала установил zeroblock и все работало, но понадобилась более детальная настройка и я открыл для себя мир sing-box. Он прекарасен и опасен одновременно. Пропущенная запятушка, не законченное правило и все упало. Одна ошибка и ты ошибся(с).
Огромное спасибо команде RR за предоставленные возможности в развитии. Всё работает так как мне надо.
Может другой роутер умеет тоже самое? Может и умеет, но первое моё знакомство с openWRT это вы и вы навсегда останетесь в моем сердце:)
Ах да. Чатик это супер! 2 раза обращался и в течении 10 минут проблема была решена.
Буду рекомендовать всем!
Ещё раз спасибо!

---

**2026-03-06T12:33:15 | Anna Bagler**
Система - Пакеты, в поле фильтра zeroblock и удалить.

---

**2026-03-06T12:58:38 | Anna Bagler**
Установил. Но зачем вам вновь zeroblock, если вы его удаляли?

---

**2026-03-06T13:11:50 | Anna Bagler**
100% нет, но попробовать стоит с zeroblock и zapret2.

---

**2026-03-06T13:23:45 | Azizkhan**
[zeroblock] ZeroBlock started successfully
[clash_api] /main/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 504
[clash_api] /main/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 504
[clash_api] /main/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 504
Fri Mar 6 17:10:34 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[clash_api] /main/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: Error
[clash_api] /main/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: Error
[clash_api] /main/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: Error
[zeroblock] ZeroBlock stopped successfully
Fri Mar 6 17:10:37 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock(0.7.0-r7)...
[http_client] curl_easy_perform failed: Error
[ruleset_manager] API request failed (ret: -4, code: 0, size: 0)
[ruleset_manager] Failed to load community lists from any source
[http_client] Failed after 0 retries: https://github.com/itdoginfo/allow-domains/releases/latest/download/telegram.srs (curl=35, http=0)
[http_client] Failed after 0 retries: https://github.com/itdoginfo/allow-domains/releases/latest/download/google_play.srs (curl=35, http=0)
[lists_loader] Failed to download: https://github.com/itdoginfo/allow-domains/releases/latest/download/telegram.srs
[lists_loader] Failed to download: https://github.com/itdoginfo/allow-domains/releases/latest/download/google_play.srs
[config_builder] Some lists failed to download (2 errors)
[lists_loader] Community list not found: /tmp/zeroblock/rulesets/telegram.srs
[lists_loader] Section main: list unavailable: telegram
[lists_loader] Community list not found: /tmp/zeroblock/rulesets/google_play.srs
[lists_loader] Section main: list unavailable: google_play
[zeroblock] ZeroBlock started successfully
[clash_api] /main/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 504
[clash_api] /main/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 504
[clash_api] /main/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 504
[clash_api] /main/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 504
[clash_api] /main/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 504
[clash_api] /main/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 504
[clash_api] /main/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 504
[clash_api] /main/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 504
luci: failed login on /admin/services/zeroblock for root from 192.168.33.241
luci: accepted login on /admin/services/zeroblock for root from 192.168.33.241
[clash_api] /main/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 504
[clash_api] /main/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 504
[clash_api] /main/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 504
Fri Mar 6 17:23:03 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[clash_api] /main/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: Error
[zeroblock] ZeroBlock stopped successfully
Fri Mar 6 17:23:06 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock(0.7.0-r7)...
[http_client] curl_easy_perform failed: Error
[ruleset_manager] API request failed (ret: -4, code: 0, size: 0)
[ruleset_manager] Failed to load community lists from any source
[http_client] Failed after 0 retries: https://github.com/itdoginfo/allow-domains/releases/latest/download/google_play.srs (curl=35, http=0)
Системная информация

---

**2026-03-06T13:26:10 | Azizkhan**
[lists_loader] Failed to load community index for v2 API
[config_builder] Some lists failed to download (1 errors)
[lists_loader] v2 community list has no data files: youtube
[lists_loader] Section main: list unavailable: youtube
[lists_loader] v2 community list has no data files: discord
[lists_loader] Section main: list unavailable: discord
[lists_loader] v2 community list has no data files: meta
[lists_loader] Section main: list unavailable: meta
[lists_loader] v2 community list has no data files: telegram
[lists_loader] Section main: list unavailable: telegram
[lists_loader] v2 community list has no data files: google_play
[lists_loader] Section main: list unavailable: google_play
Fri Mar 6 17:25:43 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock started successfully
[zeroblock] ZeroBlock stopped successfully
Fri Mar 6 17:25:47 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock(0.7.0-r7)...

---

**2026-03-06T15:06:11 | Danila Sazonov**
Всем добрый день 
Недавно приобрел RR для того чтобы поставить его между основным маршрутизатором и TV для доступа в YouTube и Netflix, поставил sing-box, понял что лень ковыряться в config.json, добавил HomeProxy, загрузил VLESS конфиг и все работает 
После чего нашел данную группу и что-то меня немного разорвало количеством информации, а именно подкопами, запретами и зероблоками 
Хотел бы уточнить один момент, стоит ли переходить с HomeProxy на ZeroBlock? Получу ли я от него какие-либо преимущества учитывая что у меня особо нет знаний в этой области или HomeProxy для моей задачи выше крыши? Заранее извиняюсь за тупые вопросы

---

**2026-03-06T15:30:40 | воппер уполномоченный**
не открываются сайты на клиентах с запущенным у них vpn сервисом (любой, кроме vless, который стоит в маршрутизации zeroblock)
protonvpn (расширение в браузере), amneziavpn (на мобильном работает)
кто нибудь сталкивался с этим? сам zeroblock отрабатывает нормально, все сервисы открываются и маршрутизация нормально проходит

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

**2026-03-06T19:18:05 | Роман**
Catch-all секция в zeroblock делает так.

---

**2026-03-06T19:26:27 | HiLLL**
Сожрало нет? Но я не понял зачем.
[zeroblock] Starting ZeroBlock(0.7.0-r18)...
[lists_loader] Skipping invalid domain from user list: app-234483.games.s3.yandex.net:443
[lists_loader] Skipping invalid domain from user list: app-239966.games.s3.yandex.net:443
[lists_loader] Skipping invalid domain from user list: captcha-backgrounds.s3.yandex.net:443
[zeroblock] ZeroBlock started successfully

---

**2026-03-06T19:42:01 | Святос**
Кто такая Софи ZeroBlock?

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

**2026-03-06T21:21:57 | Роман**
У час старая версия zeroblock? В новых запреты распознаются корректно.

---

**2026-03-06T21:52:10 | Роман**
Если навыков никаких - скрипт 5 из темы интернет без границ, или скрипт бета из ветки бета, если умеете читать и тыкать в терминал - zeroblock из ветки zeroblock.

---

**2026-03-06T22:11:56 | 🌶️🌶️**
[zeroblock] Starting ZeroBlock...
[config_builder] Invalid bootstrap_dns_server '9.9.9.9', using default
[zeroblock] ZeroBlock started successfully
Fri Mar 6 21:03:57 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Fri Mar 6 21:04:02 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[config_builder] Invalid bootstrap_dns_server '9.9.9.9', using default
[zeroblock] ZeroBlock started successfully
Fri Mar 6 22:08:23 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Fri Mar 6 22:08:28 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[config_builder] Invalid bootstrap_dns_server '8.8.8.8', using default
[zeroblock] ZeroBlock started successfully
Fri Mar 6 22:10:04 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Fri Mar 6 22:10:09 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock...
[config_builder] Invalid bootstrap_dns_server '1.1.1.1', using default
[zeroblock] ZeroBlock started successfully

---

**2026-03-06T22:34:50 | Netizen**
ребят, только сегодня получил роутер. в zeroblock можно засунуть свою подписку или vless конфиг или это только через podkop?

---

**2026-03-07T08:45:13 | Роман**
И кстати Instagram в браузере через zeroblock не загружается. Но мне пофиг, я костыль в виде запрета 2 приделал.

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

**2026-03-07T09:57:09 | Роман**
Качайте zeroblock, создавайте свою секцию с вашим ВПН и выбирайте списки для обхода. Можно сайты ручками добавлять. 
ВПН какого вида у вас?

---

**2026-03-07T09:59:54 | Anna Bagler**
Если zeroblock, то ai.

---

**2026-03-07T10:03:29 | Роман**
В ветке zeroblock, файлы в закрепе.

---

**2026-03-07T12:04:05 | Даниил Тащиан**
Добрый день, перестал работать подкоп 5 , ни ютуб ни телега ни принтер бамбук не заводится 😃. Что лучше переустановить подкоп попытаться или сбросить роутер и вижу в чате советуют zeroblock ?

---

**2026-03-07T14:14:09 | Anna Bagler**
5 или zeroblock.

---

**2026-03-07T15:04:58 | Anna Bagler**
Отключить пока zeroblock и zapret2. Проверить обновление списков.

---

**2026-03-07T15:51:36 | Anna Bagler**
У вас подкоп или zeroblock?

---

**2026-03-07T15:52:04 | Вячеслав Шевченко**
у меня zeroblock и запрет2

---

**2026-03-07T16:30:17 | Andrew**
Здравствуйте. Подскажите плиз, установил zeroblock, но пишет что sing-box не запущен. Что нужно сделать? Кнопка запустить не реагирует

---

**2026-03-07T16:47:27 | Вячеслав Шевченко**
Система-пакеты и жмем на кнопку "Загрузить пакет". И по очереди ставим скачанные пакеты: Zeroblock_*** а затем luci-app***.(Табличку с надписью Error игнорируем)
 обновление так же делается?

---

**2026-03-07T16:52:26 | Роман**
Актуальный скрипт 5, zeroblock.

---

**2026-03-07T17:31:32 | Роман**
В zeroblock? В подкоп?
В zb есть исключения в настройках секции.

---

**2026-03-07T18:27:18 | Yuri Kovalev**
Сделал как вы сказали, вроде бы установилось но WARP отвалился и в разделе ZeroBlock всеравно 0.6.4-r64 версия

---

**2026-03-07T18:27:53 | HiLLL**
запустите в терминале zeroblock awg warp

---

**2026-03-07T18:36:42 | Роман**
Вам придётся установить zeroblock или скрипт 5, туда вставить свой ключ с сервером(потому-что на бесплатных обходах вряд-ли роблокс заведется, только если через варп), прописать домены и ip роблокса.

---

**2026-03-07T19:24:46 | Megaherz**
Здравствуйте подскажите пожалуйста есть две секции маршрутизации в zeroblock opera и awg10 списки какие куда лучше добавить?

---

**2026-03-07T20:46:48 | Kirill Y**
Здраствуйте! А если с podkop переходить в zeroblock, то надо до заводских сбрасывать? Или просто добавлять?

---

**2026-03-07T21:32:59 | Vladislav**
Всем привет!
А подскажите, переустановил прошивку
и решил попробовать вместо подкопа zeroblock

в логах ошибка:
[proxy_parser] Failed to parse Shadowsocks URL: invalid port 0
[singbox_gen] Section MAIN: failed to parse proxy[0]: ss://xxxxxxxxxxx...
[singbox_gen] Section MAIN: no valid proxies for URLTest (0/1)

ключ имеет такой вид
ss://xxxxxxxxxxx@domain.xyz:35673/?outline=1#poland

подкоп нормально переваривал этот ключ

---

**2026-03-07T22:23:52 | Роман**
Сбрасывайте, первоначальная настройка, время, пароль, и бета скипт. Или zeroblock.

---

**2026-03-07T22:45:50 | Роман**
Ставьте либо подкоп, либо zeroblock. После установки создаёте секцию, туда свой ключ, выбираете списки дискорда.

---

**2026-03-07T22:56:52 | Роман**
Вам уже кучу вариантов дали. Бета скрипт. Просто подкоп. Zeroblock.
Накосячили - сброс сделали. Это нормально.

---

**2026-03-07T23:25:45 | Bullet for my valentine Poison**
Zeroblock!!

---

**2026-03-07T23:44:47 | Роман**
Нет, ютуб через юаб идёт, подкоп всё остальное в прокси по спискам тянет. Ставьте zeroblock, и пишите в соответствующуюю тему, разработчик в чате, подскажет что не так. Простоя не понимаю как у вас так выходит 🤷‍♂️

---

**2026-03-08T00:10:40 | Дмитрий Григорьев**
Всем привет, такой вопрос, я только приобрёл роутер и начинаю во всём разбираться, Поставил ZB + Zapret2 по инструкции, Выкинул из списков Ютуб и Дискорд, запрет не пашет, Кинуть VLESS ключ пока не пробовал, хочу сначала разобраться с запретом. Есть ли какие-то доп инструкции, что бы это всё запахало, возможно выбор стратегий в запрете и тд, пока чёт вообще ничего не понимаю

И можно ли бахнуть первый запрет вместо второго, что бы работал в паре с Zeroblock?

---

**2026-03-08T01:11:01 | Роман**
Что установлено? Это не подкоп и не zeroblock.

---

**2026-03-08T01:21:53 | Роман**
Да. Автозапуском рулит zeroblock.

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

**2026-03-08T01:24:46 | Serg**
zeroblock          opera (prx out): ai,geoblock,shop,torrent,cdn_akamai,cdn_aws,cdn_cdn77,!_cdn_cloudflare, -  тут еще воскл знак и выделено цветом

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

**2026-03-08T09:30:30 | Anna Bagler**
Диагностика zeroblock.

---

**2026-03-08T10:10:18 | Роман**
Даже ради zeroblock. Я понимаю что мы все обязаны, невзирая ни на что, устанавливать zeroblock и искать баги (это превыше всего), но выходной же. Праздник. Зачем людей отсутствием интернета огорчать?

---

**2026-03-08T11:27:47 | Sergey**
При попытке установить по  Zeroblock ,  Zapret2 не установился. Попробовал установить пакеты отдельно, выдаёт ошибку. Подскажите, что делать?

---

**2026-03-08T11:56:06 | Winter_soon**
Добрый день. У меня в списках отсутствует Zeroblock прошивка  24.10.5 - r29087-d9c5716d1d. Его как-то отдельно ставят?

---

**2026-03-08T12:50:35 | Роман**
Здравствуйте, ссылки вида ss:// можно использовать в zeroblock/podkop, как и конфиги амнезии.

---

**2026-03-08T12:54:30 | ꧁ 𝓐𝓷𝓽𝓸𝓷 𝓑𝓮𝔃𝓴𝓪𝓹𝓾𝓼𝓽𝓲𝓷 ꧂**
Мне казалось, что я находил zeroblock прям в репозитории
Или там старая версия?

---

**2026-03-08T14:18:17 | GoodWin**
Сегодня один хороший человек из группы помог перейти на zeroblock.
Однозначно лучше подкопа. Только через пункт games в awg не работает роблок, заработало через присвоение айпи. Очень радует что с таким количеством присвоенных айпи тырнет не падает. Иначе мои мне плешь бы всю проели. Спасибо огромное разработчику зероблока и моему виртуальному другу помощнику Пуле!)

---

**2026-03-08T14:21:05 | HiLLL**
подкоп не умеет в xhttp, ставьте zeroblock

---

**2026-03-08T15:42:37 | Dmitriy M 🎃**
Подскажите, почему у меня Zeroblock не принимает ключ HysreriaII  в формате: hy2://ae3b42782d2740a.....? а в подкопе все было Ок

---

**2026-03-08T19:23:56 | Netizen**
А вот это у меня что за проблема?
Sun Mar 8 21:10:00 2026 cron.err crond[26914]: USER root pid 29990 cmd /usr/bin/zeroblock bad_interface_check >/dev/null 2>&1
Sun Mar 8 21:20:00 2026 cron.err crond[26914]: USER root pid 32322 cmd /usr/bin/zeroblock bad_interface_check >/dev/null 2>&1
Sun Mar 8 21:30:00 2026 cron.err crond[26914]: USER root pid 2108 cmd /usr/bin/zeroblock bad_interface_check >/dev/null 2>&1
Sun Mar 8 21:40:00 2026 cron.err crond[26914]: USER root pid 3953 cmd /usr/bin/zeroblock bad_interface_check >/dev/null 2>&1
Sun Mar 8 21:50:00 2026 cron.err crond[26914]: USER root pid 4970 cmd /usr/bin/zeroblock bad_interface_check >/dev/null 2>&1
Sun Mar 8 22:00:00 2026 cron.err crond[26914]: USER root pid 6040 cmd /usr/bin/zeroblock bad_interface_check >/dev/null 2>&1
Sun Mar 8 22:10:00 2026 cron.err crond[26914]: USER root pid 6981 cmd /usr/bin/zeroblock bad_interface_check >/dev/null 2>&1
Sun Mar 8 22:20:00 2026 cron.err crond[26914]: USER root pid 7534 cmd /usr/bin/zeroblock bad_interface_check >/dev/null 2>&1

---

**2026-03-08T22:42:25 | Роман**
Установить zeroblock/podkop, настроить, присвоить приставке постоянный ip и пустить её в полный прокси.

---

**2026-03-08T22:56:11 | X**
почему то не появился zeroblock в службах. в установленных видно его 🤔

---

**2026-03-08T23:14:16 | Роман**
О как, а я то думаю почему то интернет отвалится, то роутер перезагрузился, то zeroblock не проксирует трафик. А вон оно что оказывается.

---

**2026-03-08T23:45:25 | Vyacheslav S**
Коллеги, после обновления на 0.7.0-r18 На месте дашбордов с временем отклика секций висит "подключение к Clash API", которое потом менятся на "Дашборд сейчас недоступен". При этом Zeroblock работает.
Ставил на чистую 24.10.5 r29087. Как подлечить?

---

**2026-03-08T23:52:41 | Vyacheslav S**
Этот кусок?
NetworkError: HTTP error 404 while loading class file "/luci-static/resources/protocol/3g.js"
  at compileClass (https://192.168.1.1/luci-static/resources/luci.js?v=26.039.68875~ec3d818-1773001949:161:16)
    raise https://192.168.1.1/luci-static/resources/luci.js?v=26.039.68875~ec3d818-1773001949:147
    compileClass https://192.168.1.1/luci-static/resources/luci.js?v=26.039.68875~ec3d818-1773001949:161
luci.js:154:9
NetworkError: HTTP error 404 while loading class file "/luci-static/resources/protocol/qmi.js"
  at compileClass (https://192.168.1.1/luci-static/resources/luci.js?v=26.039.68875~ec3d818-1773001949:161:16)
    raise https://192.168.1.1/luci-static/resources/luci.js?v=26.039.68875~ec3d818-1773001949:147
    compileClass https://192.168.1.1/luci-static/resources/luci.js?v=26.039.68875~ec3d818-1773001949:161
luci.js:154:9
NetworkError: HTTP error 404 while loading class file "/luci-static/resources/protocol/wwan.js"
  at compileClass (https://192.168.1.1/luci-static/resources/luci.js?v=26.039.68875~ec3d818-1773001949:161:16)
    raise https://192.168.1.1/luci-static/resources/luci.js?v=26.039.68875~ec3d818-1773001949:147
    compileClass https://192.168.1.1/luci-static/resources/luci.js?v=26.039.68875~ec3d818-1773001949:161
luci.js:154:9
Заблокирована загрузка смешанного активного содержимого «http://192.168.1.1:9090/proxies» 9 zeroblock
Error: Please use $(ref:runtime.lastError).

---

**2026-03-08T23:57:33 | Vyacheslav S**
Да, на хроме живет. Но появилась после обновления c ZeroBlock 0.6.4, там было всё ок.

---

**2026-03-09T04:36:52 | Anna Bagler**
Если ничего не ставили, то анблок, он мог не подхватить ТВ, рассмотрите связку zeroblock+zapret2 для установки. Анблок тогда отключить. Он есть, но нет luci к нему.

---

**2026-03-09T04:46:45 | Anna Bagler**
Можете пробовать копать. Но я бы удалила и поставила zeroblock c галочкой на zapret2.

---

**2026-03-09T10:22:28 | V I T Λ L Y**
А у меня почему то не zeroblock...запрет2 поставил, а этого нет🤷‍♂️ пакеты обновлял

---

**2026-03-09T10:26:08 | Anna Bagler**
Ставить из закрепов темы Zeroblock Beta.

---

**2026-03-09T10:42:55 | Anna Bagler**
Ну, рутрекер работает через zeroblock/podkop, для zapret2 надо стратегию подбирать. Что у вас стояло до обновления прошивки?

---

**2026-03-09T10:44:19 | Nikita Reshetilov**
Zeroblock?

---

**2026-03-09T10:46:07 | Артём Давыдов**
Zeroblock

---

**2026-03-09T10:55:35 | Routerich**
Мы в курсе проблем с zeroblock, asu и remote.routerich.ru. Решение по zeroblock это обновление пакетов https://t.me/routerich/394153/432061
Разбираемся в проблеме, приносим извинения.

---

**2026-03-09T10:55:40 | Артём Давыдов**
Zeroblock тоже включить?
Код пока обрабатывается

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

**2026-03-09T12:38:26 | Anna Bagler**
Домены сайта добавьте в секцию main zeroblock и будет открываться. В списки пользователя.

---

**2026-03-09T12:48:08 | Игорь Щеголев**
У меня также ZeroBlock и Zapret2 есть, но нет секции awg10, только opera. И ASU обновление не работает, крутится колёсико бесконечно.😱

---

**2026-03-09T12:57:46 | РУЗОВ Дмитрий**
Ребята,: 
- лучше сразу смотреть в сторону Zeroblock+Zapret2, чтобы не переучиваться еще раз.
- если устанавливать Zeroblock+Zapret2, то в иструкции написано, что установка долгая. Правильно понимаю, что в этот момет роутер отрубит всю сетку? Т.е если сейчас по сети смотрят ТВ, то отрубится соединение

---

**2026-03-09T12:57:56 | Роман**
У меня тоже всё работает. Правда у меня подкоп и я не пользуюсь ASU и zeroblock 🤷‍♂

---

**2026-03-09T13:00:06 | РУЗОВ Дмитрий**
лучше сразу смотреть в сторону Zeroblock+Zapret2 - это направление правильное

---

**2026-03-09T13:16:06 | Routerich**
Восстановлена работоспособность zeroblock, asu и remote.routerich.ru. 
Приносим извинения за неудобства.

---

**2026-03-09T13:24:16 | РУЗОВ Дмитрий**
Если установлю пакеты по инструкции из тем в чате  Zeroblock+Zapret2 могу решить такую потребность:
- полноценная работа Телеги
- внедрить квн на RR , чтобы можно было не включать на устройствах (ключи работающие есть разных типов vMess, Vless)

---

**2026-03-09T13:42:08 | Anna Bagler**
Zeroblock можно, исключения по IP, zapret - нет.

---

**2026-03-09T14:06:27 | Anna Bagler**
Раз ничего больше не ставили, то больше ничего. Возможно, наоборот, надо поставить zeroblock и в него добавить домены и списки. Через браузер доступ к сервисам есть или тоже не хочет заходить никуда?

---

**2026-03-09T15:31:15 | Alex Korshun**
Что за поломка была с zeroblock, asu и remotecontrol? Я пропустил момент, к сожалению...

---

**2026-03-09T16:12:57 | Роман**
Установить zeroblock/podkop, настроить, вставить свою ссылку.

---

**2026-03-09T16:15:24 | J Khan**
Это либо zeroblock, либо podkop установить? Правильно понимаю?

---

**2026-03-09T16:27:30 | Роман**
Для обхода блокировок видимо. Мы вчера ночью на плойке MK1 через zeroblock завели, пинг 80.

---

**2026-03-09T16:29:03 | Роман**
Конечно можете, устанавливайте zeroblock.
https://t.me/routerich/394153/520562

---

**2026-03-09T17:04:07 | Pavel**
Поставил zeroblock, включил для секций opera, и для awg 10, нажал применить, инста и ютуб заработали на айфоне( до этого работал ютуб только на телевизоре lg, и на компе), Ip прежний, дальше сломался на пункте в настройках Люси, настройте секции и списки доменов

---

**2026-03-09T18:07:41 | HiLLL**
что логи пишут? ZeroBlock-диагностика-логи обновить скрин покажите

---

**2026-03-09T19:14:23 | Никита Веселов**
Привет, только приобрел Routerich AX3000. Неделю читал мануалы и хочу сказать огромное спасибо! ZeroBlock + Zapret2 выбрал для обхода. И все заработало чуть ли не с первого раза (пришлось список для AWG10 расширить)) Теперь везде все работает и даже Meta VR. Низкий поклон☺️

---

**2026-03-09T19:48:04 | Роман**
А где флуд?
Флуд (от англ. flood — «наводнение», «потоп») — это поток бессмысленных, однотипных или нетематических сообщений в чатах, форумах, комментариях или соцсетях.
Был задан конкретный вопрос и дан конкретный ответ с отсылкой к мануалу zeroblock.

---

**2026-03-09T20:09:36 | Routerich**
лишён права использовать zeroblock

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

**2026-03-09T20:49:42 | Никита Веселов**
Вопрос по родительскому контролю через zeroblock. А можно в нем обрубить домены для определенных устройств? Временное ограничение работает, а сайты все равно открывает нежелетальные

---

**2026-03-09T21:56:44 | Routerich**
cat /etc/config/zeroblock |grep opencck

---

**2026-03-10T01:07:26 | Bullet for my valentine Poison**
Я принимаю Zeroblock таким, какой он есть. Со всеми его УНИКАЛЬНЫМИ плюшками и недостатками. Так что никакого нытья. (Стоило вас тут оставить на несколько часов, так началось) 🙄

---

**2026-03-10T01:13:13 | ROMA**
opkg install /tmp/upload.ipk
Installing zeroblock (0.7.0-r28) to root...
Installing sing-box-tiny (1.12.22-r1) to root...
Ошибки
Collected errors:
 * verify_pkg_installable: Only have 5276kb available on filesystem /overlay, pkg sing-box-tiny needs 28430
 * opkg_install_cmd: Cannot install package zeroblock.
Команда opkg install завершилась с ошибкой с кодом 255

---

**2026-03-10T03:02:42 | Anna Bagler**
Пробуете вытащить прямую ссылку из happ, запросить прямую ссылку у поддержки сервиса (запросить ссылку для роутера). Поставить zeroblock и уже в роутере прямую ссылку использовать.

---

**2026-03-10T03:06:00 | Nikolai Korp**
zeroblock умеет с подписками работать? 
Я в подкопе делал тестово, там вариант был с много ссылок из подписки добавлял как отдельный vless и стратегия выбор какой работает быстрее.

---

**2026-03-10T07:39:00 | Михаил**
В zeroblock подписки можно использовать. Список ссылок в https. У podkop этого нет.

---

**2026-03-10T09:03:40 | Anna Bagler**
В zeroblock, да.

---

**2026-03-10T09:04:04 | Routerich**
Здравствуйте.
через ZeroBlock, v2raya есть возможность.

---

**2026-03-10T09:04:33 | Routerich**
переходите на ZeroBlock https://t.me/routerich/394153/432061

---

**2026-03-10T09:06:22 | Routerich**
tailscale  в ZeroBlock подкинуть можно.

---

**2026-03-10T09:19:21 | Routerich**
uci show zeroblock |grep enabled
покажет все опции поддерживающие включение, выбираем оттуда секции, делаем 
uci set zeroblock.name_section enabled = '1' 
 чтоб включить
uci set zeroblock.name_section enabled = '0' 
чтоб выключить
uci commit && service zeroblock restart
сохранить, перезапустить

---

**2026-03-10T09:21:04 | 𝕾𝖊𝖗𝖌𝖊𝖎 𝕷𝖎𝖘𝖆𝖑𝖔**
Да, я про это. 
Теперь понял. 
"uci set zeroblock.opera.enabled='0'
uci set zeroblock.awg10.enabled='0'
uci set zeroblock.whitelist_vless.enabled='1'
uci commit zeroblock
/etc/init.d/zeroblock restart"

---

**2026-03-10T09:28:03 | 𝕾𝖊𝖗𝖌𝖊𝖎 𝕷𝖎𝖘𝖆𝖑𝖔**
Типа так?
Скажем первый когда инет сдох?:
uci set zeroblock.opera.enabled='0'
uci set zeroblock.awg10.enabled='0'
uci set zeroblock.vless_whitelist.enabled='1'

uci set zeroblock.dns.type='udp'
uci set zeroblock.dns.server='77.88.8.8'

uci commit
service zeroblock restart

---

**2026-03-10T09:28:40 | 𝕾𝖊𝖗𝖌𝖊𝖎 𝕷𝖎𝖘𝖆𝖑𝖔**
uci set zeroblock.opera.enabled='1'
uci set zeroblock.awg10.enabled='1'
uci set zeroblock.vless_whitelist.enabled='0'

uci set zeroblock.dns.type='doh'
uci set zeroblock.dns.server='https://dns.cloudflare.com/dns-query'

uci commit
service zeroblock restart

---

**2026-03-10T10:57:19 | Anna Bagler**
Лучше zeroblock. По подкопу - более свежий в теме Beta.

---

**2026-03-10T11:32:23 | Anna Bagler**
@dchernyshkov Если стратегии не помогают, пустите его в zeroblock по IP и посмотрите. Может ПО обновите как раз и приложения.

---

**2026-03-10T11:53:40 | Роман**
А по результату не видно? Я уже и не помню. Что-то вроде Support Fresa сидит на кресле из костей, внизу люди молятся о новой версии  zeroblock, вокруг валяются объедки голубей 😁

---

**2026-03-10T12:15:01 | Роман**
Здравствуйте, вам уже ответили, добавить список messengers в zeroblock.

---

**2026-03-10T12:15:45 | Евгений Могилевский**
День добрый. Подскажите, пожалуйста, на Xbox вылезла ошибка с регионом после установки routerich. Стоит main+zeroblock+zapret2 (по инструкции ставил), все работает, а региональная ошибка вот вылезла. До этого сидел на кинетиках, там просто прописал по инструкции с Xbox DNS правило и в ус не дул. Как и куда запихнуть DNS адреса, или правило с DNS, раздел какой, или поставить что нужно дополнительно? Заранее благодарен.

---

**2026-03-10T12:17:39 | Routerich**
Здравствуйте.
в настройках ZeroBlock сменить DNS на Xbox DNS

---

**2026-03-10T12:26:15 | Евгений Могилевский**
В zeroblock/настройки/DNS, этот раздел? Где сервер, или bootstrap прописать DNS с Xbox, верно?

---

**2026-03-10T12:30:50 | ROMA**
тут было 0% я установил пакет minidlna и стало занято 95% и я не смог установить зероблок. Я полностью ребутнул роутер, и снова стало 0% (minidlna удалился ествественно) Я установил zeroblock и теперь половина памяти занята. Так и должно быть? Получается я что только 1 пакет могу установить? Или я что-то не так делаю? Подскажите пожалуйста

---

**2026-03-10T13:15:22 | Anna Bagler**
Ставьте сразу zeroblock и zapret2. И потом смотрите. Анблок отключить или крутите его.

---

**2026-03-10T13:18:40 | Routerich**
Здравствуйте.
Для zeroblock лучше сперва сбросить роутер, а потом установить его.

---

**2026-03-10T13:19:05 | Никита Веселов**
Добавил в ZeroBlock VPN на hy2 и все работает вроде как даже. Но в диагностике, outbound проверки не выполнены. Это критично?

---

**2026-03-10T13:29:56 | Routerich**
в ZeroBlock для использования xhttp включается xray, для всего что не поддерживает sing-box

---

**2026-03-10T13:54:49 | Molodoy Makkonehi**
прощу прощения. изваините за именно тупые вопросы ) но времени нет образоываться 😆кеак его инсталлить ?  - ZEROBLOCK я пакет скормил ему ipk и чет сделал логаут и залогинился и не нахожу его в службах ...

---

**2026-03-10T14:20:33 | Владимир Волков**
Make Zeroblock Greate Again?

---

**2026-03-10T14:30:18 | Евгений Могилевский**
Смотрю прямо сейчас, подкоп не использую. На чистую систему поставил по инструкции zeroblock+zapret2, все завелось по умолчанию без дополнительных настроек. Проверил в браузере, apple tv 4k, android mi box. Единственное, что не завелось, apple tv3, прописывать/разбираться не стал.

---

**2026-03-10T14:49:05 | Andrew**
Подскажите пожалуйста, хочу выполнить сброс роутера к заводским настройкам, на роутере установлен zeroblock и настроена конфигурация. После сброса к заводским настройкам есть вероятность окирпичить устройство, или это штатная процедура?

---

**2026-03-10T15:47:27 | @Dr.Medvedolog**
Два глупых вопроса. При каких настройках Zeroblock на роутере с модемом, на котором БС жесткие и из днс только Yandex, будет работать opkg через outband xray xhttp?

---

**2026-03-10T16:50:42 | Роман**
Потому что эти сайты не прописаны в zeroblock, а то что вы включаете отдельно ВЕСЬ трафик направляет в прокси.

---

**2026-03-10T16:57:33 | Routerich**
где-то рядом
========================================
ZeroBlock Generator Validator v2
ZeroBlock v0.7.1-r13
Начало: 09:25:21
========================================
========================================
ИТОГИ
========================================
Всего тестов: 824
Пройдено: 811
Ошибок: 7
Конец: 12:38:29
========================================

---

**2026-03-10T17:28:20 | @Dr.Medvedolog**
[zeroblock] Starting ZeroBlock(0.7.0-r28)...
[http_client] curl_easy_perform failed: Error
[ruleset_manager] GitHub API request failed (ret: -4, code: 0, size: 0)
[ruleset_manager] Failed to load community lists from any source
[http_client] curl_easy_perform failed: Error
[ruleset_manager] GitHub API request failed (ret: -4, code: 0, size: 0)
[http_client] Retry 1/3 for https://raw.githubusercontent.com/itdoginfo/allow-domains/refs/heads/main/Subnets/IPv4/russia_inside.lst (delay=1000ms, error=Error)
[http_client] Retry 1/3 for https://github.com/itdoginfo/allow-domains/releases/latest/download/twitter.srs (delay=1000ms, error=Error)
[http_client] Retry 1/3 for https://raw.githubusercontent.com/itdoginfo/allow-domains/refs/heads/main/Subnets/IPv4/twitter.lst (delay=1000ms, error=Error)
[http_client] Retry 1/3 for https://raw.githubusercontent.com/itdoginfo/allow-domains/refs/heads/main/Subnets/IPv4/google_ai.lst (delay=1000ms, error=Error)

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

**2026-03-10T18:08:32 | Anna Bagler**
zeroblock и zapret2. Анблок отключить и остановить или удалить. Остальное по вашим целям.

---

**2026-03-10T19:19:08 | Роман**
Установить zeroblock и создать catch all секцию. Весь трафик пойдет в прокси. 
Там-же есть URL test который тестирует доступность vless.

---

**2026-03-10T19:32:05 | Роман**
Тогда велика возможность что заработает запрет2. Если youyubeunblock не сработал. Затем, если запрет 2 с несколькими стратегиями не помог, можно попробовать запрет 1. Если и это не поможет - ZeroBlock/podkop.

---

**2026-03-10T21:19:24 | Aleks Buryi**
Добрый вечер.
Zeroblock предпочтительнее Подкопа для нормальной работы Телеграм?
Их одновременно можно юзать? Как установить и настроить (заменить подкоп на зероблок?)

---

**2026-03-10T21:22:41 | Роман**
Попробуйте ссылки сменить. Разницы то нет, что zeroblock, что podkop - средства маршрутизации.

---

**2026-03-10T21:30:36 | Николаич**
Скажите на zeroblock_0.7.0-r28 стоит переходить с r-85 ?

---

**2026-03-10T22:59:01 | Den Kihot**
Добрый вечер. Пытаюсь установить Zeroblock. В логах ошибки, Zapret2 так и не появляется. Можете помочь?

---

**2026-03-10T23:02:41 | Den Kihot**
Спасибо. Zapret2 появился, но в логах Zeroblock эти ошибки остались. Это норм?

---

**2026-03-10T23:06:43 | Den Kihot**
Что делать? Перезапустить Zeroblock?

---

**2026-03-10T23:36:01 | Routerich**
а я понять не могу, почему ошибки синга, но зб падает на запуске
Tue Mar 10 17:39:22 2026 user.notice podkop: [debug] '# This File Date  : 2025-12-18 00:51:31' is not IPv4 or IPv4 CIDR
Tue Mar 10 17:39:22 2026 user.notice podkop: [debug] '# Update Frequency: 24 hours' is not IPv4 or IPv4 CIDR
Tue Mar 10 17:39:22 2026 user.notice podkop: [debug] '# Entries         : 229' is not IPv4 or IPv4 CIDR
Tue Mar 10 17:39:22 2026 user.notice podkop: [debug] '#' is not IPv4 or IPv4 CIDR
Tue Mar 10 17:39:22 2026 user.notice podkop: [debug] '# (C) 2011-2025 HybridNetworks Ltd. -- All Rights Reserved' is not IPv4 or IPv4 CIDR
Tue Mar 10 17:39:22 2026 user.notice podkop: [debug] '#' is not IPv4 or IPv4 CIDR
Tue Mar 10 17:39:22 2026 user.notice podkop: [debug] '# ============================================================' is not IPv4 or IPv4 CIDR
Tue Mar 10 17:39:22 2026 user.notice podkop: [debug] '#' is not IPv4 or IPv4 CIDR
Tue Mar 10 17:39:24 2026 user.notice podkop: [debug] Adding 229 elements to nft set podkop_subnets
Tue Mar 10 17:39:24 2026 user.notice podkop: [info] ✅ Lists update completed successfully
Tue Mar 10 23:07:01 2026 daemon.err zeroblock[7348]: [zeroblock] ZeroBlock stopped successfully
Tue Mar 10 23:07:02 2026 user.notice zeroblock: Starting ZeroBlock...
Tue Mar 10 23:07:02 2026 daemon.err zeroblock[7560]: [zeroblock] Starting ZeroBlock(0.7.0-r28)...
Tue Mar 10 23:07:39 2026 daemon.err zeroblock[7560]: [config_builder] Sing-box failed to start within timeout
Tue Mar 10 23:07:39 2026 daemon.err zeroblock[7560]: [zeroblock] Failed to start ZeroBlock
Tue Mar 10 23:10:02 2026 daemon.err zeroblock[8670]: [clash_api] /proxies failed: Error
Tue Mar 10 23:10:13 2026 daemon.warn odhcpd[2785]: No default route present, setting ra_lifetime to 0!
Tue Mar 10 23:17:56 2026 daemon.warn odhcpd[2785]: No default route present, setting ra_lifetime to 0!
Tue Mar 10 23:18:29 2026 daemon.err uhttpd[2982]: [info] luci: accepted login on /admin/services/podkop for root from 192.168.1.165
Tue Mar 10 23:21:26 2026 daemon.err sing-box[7591]:  [31mERROR [0m[0859] [ [38;5;72m838382392 [0m 0ms] router: UDP is not supported by outbound: main-out
Tue Mar 10 23:21:26 2026 daemon.err sing-box[7591]:  [31mERROR [0m[0860] [ [38;5;120m2648276840 [0m 0ms] router: UDP is not supported by outbound: main-out
Tue Mar 10 23:21:26 2026 daemon.err sing-box[7591]:  [31mERROR [0m[0860] [ [38;5;30m4157589262 [0m 0ms] router: UDP is not supported by outbound: main-out
ue Mar 10 23:07:02 2026 daemon.err zeroblock[7560]: [zeroblock] Starting ZeroBlock(0.7.0-r28)...
Tue Mar 10 23:07:39 2026 daemon.err zeroblock[7560]: [config_builder] Sing-box failed to start within timeout
Tue Mar 10 23:07:39 2026 daemon.err zeroblock[7560]: [zeroblock] Failed to start ZeroBlock
Tue Mar 10 23:10:02 2026 daemon.err zeroblock[8670]: [clash_api] /proxies failed: Error
Tue Mar 10 23:10:13 2026 daemon.warn odhcpd[2785]: No default route present, setting ra_lifetime to 0!
Tue Mar 10 23:17:56 2026 daemon.warn odhcpd[2785]: No default route present, setting ra_lifetime to 0!
Tue Mar 10 23:18:29 2026 daemon.err uhttpd[2982]: [info] luci: accepted login on /admin/services/podkop for root from 192.168.1.165
Tue Mar 10 23:21:30 2026 daemon.err sing-box[7591]:  [31mERROR [0m[0863] [ [38;5;96m1637773392 [0m 0ms] router: UDP is not supported by outbound: main-out
Tue Mar 10 23:25:48 2026 daemon.warn odhcpd[2785]: No default route present, setting ra_lifetime to 0!

---

**2026-03-10T23:45:54 | Den Kihot**
я остановил подкоп, и ZeroBlock вроде завелся.
Вот и уточняю - подкоп надо именно сносить или достаточно остановить?

---

**2026-03-10T23:52:30 | Den Kihot**
там уже zeroblock поработал

---

**2026-03-11T07:45:10 | Anna Bagler**
Если есть навыки, то вы можете ставить zeroblock https://t.me/routerich/394153/520562 или https://t.me/routerich/3845/245550

---

**2026-03-11T08:15:33 | Vlkklb**
При попытке обновления , ошибка на ZB Package list missing or not up-to-date, generating it.

Building package index...
Downloading file:/local-repos/24.10.5/core/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/routerich_core
Downloading file:/local-repos/24.10.5/base/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/routerich_base
Downloading file:/local-repos/24.10.5/routerich/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/routerich
Downloading file:/local-repos/24.10.5/openwrt/base/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/openwrt_base
Downloading file:/local-repos/24.10.5/openwrt/luci/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/openwrt_luci
Downloading file:/local-repos/24.10.5/openwrt/packages/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/openwrt_packages
Downloading file:/local-repos/24.10.5/openwrt/routing/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/openwrt_routing
Downloading file:/local-repos/24.10.5/openwrt/telephony/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/openwrt_telephony
Downloading file:packages/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/imagebuilder
Collected errors:
 * opkg_install_cmd: Cannot install package luci-app-zeroblock.
 * opkg_install_cmd: Cannot install package zeroblock.
make[2]: *** [Makefile:234: package_install] Error 255
make[1]: *** [Makefile:171: _call_manifest] Error 2
make: *** [Makefile:349: manifest] Error 2

Traceback (most recent call last):
  File "/usr/local/lib/python3.12/site-packages/rq/worker.py", line 1659, in perform_job
    return_value = job.perform()
                   ^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/rq/job.py", line 1318, in perform
    self._result = self._execute()
                   ^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/rq/job.py", line 1376, in _execute
    result = self.func(*self.args, **self.kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/asu/build.py", line 63, in build
    return _build_internal(build_request, job, request_hash, build_start, bin_dir)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/asu/build.py", line 504, in _build_internal
    report_error(job, "Impossible package selection")
  File "/app/asu/util.py", line 302, in report_error
    raise RuntimeError(msg)
RuntimeError: Impossible package selection

---

**2026-03-11T08:18:22 | Routerich**
Здравствуйте.
Удалите из списка zeroblock
Его в репозиториях нет

---

**2026-03-11T08:45:17 | Routerich**
Здравствуйте.
Найти домены на которые он обращается и добавить в zeroblock

---

**2026-03-11T08:48:37 | Nikolai Korp**
На чистый openwrt встанет ? Zeroblock?

---

**2026-03-11T09:01:57 | Александр**
Всем привет! Второй день за ночь отваливается ZeroBlock и zapret2 (не открываются нужные сайты при этом службы запущены). Захожу в панель, а там "WARP: Отключено"
Помогает перезапуск нужных служб. В чем может быть проблема?

---

**2026-03-11T09:07:47 | Bogdan**
Почему-то каждый день в 9 утра тупит с обновлением списков, в это время не работает обход и приходится его вручную перезапускать
Часть лога я удалил, а то не влезало
Wed Mar 11 09:00:01 2026 user.notice zeroblock: Stopping ZeroBlock...
Wed Mar 11 09:00:01 2026 daemon.err zeroblock[4848]: [zeroblock] Stopping ZeroBlock...
Wed Mar 11 09:00:04 2026 daemon.err zeroblock[4848]: [zeroblock] ZeroBlock stopped successfully
Wed Mar 11 09:00:06 2026 user.notice zeroblock: Starting ZeroBlock...
Wed Mar 11 09:00:06 2026 daemon.err zeroblock[5220]: [zeroblock] Starting ZeroBlock(0.7.0-r28)...
Wed Mar 11 09:00:06 2026 daemon.warn zeroblock[5220]: [sections_loader] Dedup: removed 'geoblock' from server section 'opera'.community_lists — already in user section
Wed Mar 11 09:00:06 2026 daemon.warn zeroblock[5220]: [sections_loader] Dedup: removed 'ai' from server section 'opera'.community_lists — already in user section
Wed Mar 11 09:00:06 2026 daemon.warn zeroblock[5220]: [sections_loader] Dedup: removed 'geoblock' from server section 'opera'.server_community_lists — already in user section
Wed Mar 11 09:00:06 2026 daemon.warn zeroblock[5220]: [sections_loader] Dedup: removed 'ai' from server section 'opera'.server_community_lists — already in user section
Wed Mar 11 09:00:06 2026 daemon.warn zeroblock[5220]: [sections_loader] Dedup: server section 'opera' has no targets after dedup, disabling
Wed Mar 11 09:00:20 2026 daemon.warn zeroblock[5220]: [http_client] Using stale cache after 0 retries: v2_art_ipv4.json
Wed Mar 11 09:00:21 2026 daemon.warn zeroblock[5220]: [http_client] Retry 1/3 for https://zeroblock.routerich.ru/api/v2/community-
Wed Mar 11 09:02:01 2026 daemon.warn zeroblock[4835]: bash_executor_run_timeout: script killed by timeout
Wed Mar 11 09:02:04 2026 daemon.warn zeroblock[5220]: [http_client] Retry 3/3 for https://zeroblock.routerich.ru/api/v2/community-lists/youtube (delay=4000ms, error=Error)
Wed Mar 11 09:02:08 2026 daemon.warn zeroblock[5220]: [http_client] Retry 3/3 for https://zeroblock.routerich.ru/api/v2/community-lists/youtube (delay=4000ms, error=Error)
Wed Mar 11 09:02:12 2026 daemon.warn zeroblock[5220]: [http_client] Using stale cache after 3 retries: v2_repo_ipv4.json
Wed Mar 11 09:02:14 2026 daemon.warn zeroblock[5220]: [http_client] Retry 1/3 for https://zeroblock.routerich.ru/api/v2/community-lists/cdn_akamai (delay=1000ms, error=Error)
Wed Mar 11 09:02:15 2026 daemon.warn zeroblock[5220]: [http_client] Retry 1/3 for https://zeroblock.routerich.ru/api/v2/community-lists/cdn_aws (delay=1000ms, error=Error)
Wed Mar 11 09:02:16 2026 daemon.warn zeroblock[5220]: [http_client] Retry 1/3 for https://zeroblock.routerich.ru/api/v2/community-lists/cdn_aws (delay=1000ms, error=Error)
Wed Mar 11 09:02:17 2026 daemon.warn zeroblock[5220]: [http_client] Retry 1/3 for https://zeroblock.routerich.ru/api/v2/community-lists/cdn_azure (delay=1000ms, error=Error)
Wed Mar 11 09:02:18 2026 daemon.warn zeroblock[5220]: [http_client] Retry 1/3 for https://zeroblock.routerich.ru/api/v2/community-lists/cdn_azure (delay=1000ms, error=Error)

---

**2026-03-11T09:19:14 | Bogdan**
# ZeroBlock Monitor
0 * * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
# ZeroBlock Lists Update
0 4 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-03-11T09:19:45 | Александр**
В логах постоянно фигурирует:
https://zeroblock.routerich.ru/api/v2/community-lists/...

появляются ошибки:

Retry 1/3
Retry 2/3
Retry 3/3
curl_easy_perform failed
Using stale cache
..
WARP is not working (ping failed)
AWG health check failed

root@RouteRich:~# curl -I https://zeroblock.routerich.ru
curl: (7) Failed to connect to zeroblock.routerich.ru port 443 after 47 ms: Error
Нужно добавить этот демон в список?

---

**2026-03-11T09:30:36 | Routerich**
Мы в курсе проблем с zeroblock, asu и remote.routerich.ru. Решение по zeroblock это обновление пакетов https://t.me/routerich/394153/432061
Разбираемся в проблеме, приносим извинения.

---

**2026-03-11T09:40:38 | Routerich**
Восстановлена работоспособность zeroblock, asu и remote.routerich.ru. 
Приносим извинения за неудобства.

---

**2026-03-11T10:10:46 | Vladimir**
А у zeroblock ядро singbox или xray?

---

**2026-03-11T10:56:22 | Alexey Tselishchev**
Не могу что-то разобраться. А чем принципиально zeroblock отличается от podkop? Подскажите пожалуйста

---

**2026-03-11T11:16:41 | Aндрей**
Все привет!
Может быть кто-то знает, почему не работает чат гпт в приложении айфон, если список ai стоит не в опера, а в впн?

Десктоп работает, а именно в приложении на айфон - нет

Zeroblock, vpn awg

---

**2026-03-11T12:05:22 | Роман**
О как. А я нахваливаю zeroblock, списки расширенные 🙈

---

**2026-03-11T14:04:26 | Aleksey**
Господа, а zeroblock и mwan3 вообще не дружат или надо пошаманить просто маленько? Может кто-то пробовал?

---

**2026-03-11T16:23:54 | Роман**
rm /etc/config/zeroblock* /tmp/zeroblock_status.json && rm -rf /tmp/zeroblock /etc/sing-box/subscriptions /etc/zeroblock

---

**2026-03-11T16:49:44 | Никита Веселов**
у меня в zeroblock настроен свой VPN локация Нидерланды протокол HY2 и выбран список games (по скорости там все хорошо). Однако когда захожу в REPO, то пинг улетает в космос. Если погнать список через AWG10 то пинг будет в норме. Почему такое может быть?

---

**2026-03-11T16:55:26 | Anna Bagler**
Файлы zeroblock в закреплённых сообщениях темы zeroblock beta.

---

**2026-03-11T17:28:35 | Туркан**
В службах не появляется Zeroblock

---

**2026-03-11T17:38:59 | Anna Bagler**
Сначала пакет zeroblock, потом luci-app. В такой последовательности ставили?

---

**2026-03-11T17:51:04 | Юрий Теленков**
Для тех у кого через zeroblock не работает интаграмм, список CIDR не полный. Нужно ручками докидовать.

---

**2026-03-11T19:28:04 | HiLLL**
в терминале запустите zeroblock awg warp

---

**2026-03-11T19:38:44 | Фома Кузьмич**
Подскажите zeroblock кушает vless/xhttp url конфигурацию или только vless/tcp? 
у меня сейчас подкоп 0.7.10 стоит и он xhttp в прокси режиме не хочет кушать ругаеся с ошибкой user.notice podkop [error] Unknown transport 'xhttp' detected

---

**2026-03-11T21:24:13 | Фома Кузьмич**
поставил zeroblock, все что проксируется по спискам сообщества и моим доменам не работает кроме ютуба он работает отлично, в пункте авто настройка только ставил "установить xray" куда копать дальше ?

---

**2026-03-11T21:31:47 | HiLLL**
службы - терминал запустите  zeroblock awg warp

---

**2026-03-11T21:43:04 | HiLLL**
Fresa, нужен чекер варпа в ZB, парой перезапуска интерфейса недостаточно, нужна команда zeroblock awg warp при отвале

---

**2026-03-11T22:35:20 | Дмитрий**
Подскажите что сделать. Обновить прошивку, поставить скрипт 5 и ZeroBlock? Перестали открываться большая часть сайтов, видимо, по геоблоку.

---

**2026-03-11T22:44:37 | Artem**
я так понимаю на сателлит тоже надо установить zeroblock

---

**2026-03-11T23:22:19 | Роман**
Так вот кто засланный-то выходит, и подкоп у него, и zeroblock 😁

---

**2026-03-12T00:29:29 | IM**
Добрый вечер. Если на роутер с zeroblock и zapret2 поднять сервер wireguard и извне подключаться к нему со смартфона, я правильно понимаю, что весь трафик смартфона будет идти через домашнюю сеть? То есть на смартфоне после подключения по wireguard с роутеру заработают youtube и т.д.?

---

**2026-03-12T01:10:24 | Petr Shcherbinin**
стоит потушить zeroblock - начинает пускать на vps и gemini открывается заглушкой про страну

---

**2026-03-12T07:49:34 | Андрей**
Народ как понять почему роутер постоянно виснет? Установлен только ZeroBlock и все. Через свой VPN.. Виснет так что сетевое подключение отрубается

---

**2026-03-12T09:30:13 | Bkmz**
[system_monitor] WARP is not working (ping failed)
[zeroblock] AWG health check failed, restarting interface...

Понятно что варп выключен, остается вопрос как его включить. Вчера пол дня убил, но результата ноль

---

**2026-03-12T09:39:23 | HiLLL**
запустите в терминале zeroblock awg warp

---

**2026-03-12T09:59:51 | I/O**
Здравствуйте. Подскажите пожалуйста по моей задаче? У меня сейчас стоит zeroblock, настроил по инструкции, которую здесь часто кидают. В секциях отключил работу awg и оперу (вроде как пока не нужно если есть свой сервер), сделал секцию со своим vless. Через vless у меня сейчас идут списки Ютуб, мессенджеры итд, остальное идёт напрямую. Хотелось бы попробовать вариант чтобы пустить обход блокировки Ютуба по dpi, а не через ВПН (остальное можно оставить на ВПН). Подскажите последовательность действий, какими инструментами лучше пользоваться, как маршрут настроить? Вместе с зероблоком установился zapret2, я так понимаю его как-то настроить можно? Или лучше через youtubeunblock? Заранее благодарю за инфу.

---

**2026-03-12T10:18:10 | Roman Alexandrovich 🫥**
zeroblock стоит (ща потушу). это провод.

---

**2026-03-12T10:47:37 | Bullet for my valentine Poison**
А вот был бы Zeroblock...

---

**2026-03-12T11:56:53 | Никита Веселов**
через zeroblock например

---

**2026-03-12T13:08:42 | Bullet for my valentine Poison**
Когда всю ночь кодил баги для Zeroblock'a

---

**2026-03-12T13:29:12 | Anna Bagler**
Если навыки позволяют, то ставьте zeroblock, если нет - скрипт №5.

---

**2026-03-12T15:44:03 | Gomer Simpson**
Типичный чат владельцев:
— «Ребята, поставил ZeroBlock, отвалилось приложение банка и умный чайник».
— «Почитай мануал на 348-й странице, там надо в белый список добавить один китайский IP, но тогда реклама в утюге вернется».
— Владелец: (плачет, но продолжает прописывать правила в LuCI).

---

**2026-03-12T16:47:15 | Vasa**
тема Zeroblock или Интернет без границ (podkop)

на выбор варианты

---

**2026-03-12T17:10:22 | Никита Байдин (DOOMGUY)**
Не уж-то пора переходить Zapret2 или ZeroBlock?

---

**2026-03-12T17:16:10 | Роман**
Если вы хотите распространить обход на все устройства в доме, а не запускать на каждом локально, лучше взять роутер. 
Ну установите вы ВПН на VPS, и придется на каждое устройство ставить клиенты. А так установил на роутер zeroblock/podkop, вписал туда свой ключ vless, и все устройства уже с обходами.

---

**2026-03-12T17:17:17 | Никита Байдин (DOOMGUY)**
Был уже. Не пора уже переходить на Zapret2 или ZeroBlock...

---

**2026-03-12T17:20:01 | Роман**
Повторюсь, связка podkop/zapret1/2 работает. Zeroblock/zapret2/1 тоже работает. 
А что вам удобнее - ваш выбор.

---

**2026-03-12T18:28:08 | Роман**
А zeroblock нюхает трафик?

---

**2026-03-12T20:02:08 | Роман**
rm /etc/config/zeroblock* /tmp/zeroblock_status.json && rm -rf /tmp/zeroblock /etc/sing-box/subscriptions /etc/zeroblock
rm /etc/config/zapret2* && rm -rf /opt/zapret2
Мне такие команды дал разработчик.

---

**2026-03-12T21:29:39 | Роман**
У вас zeroblock поддельный 😁

---

**2026-03-12T21:51:51 | Garsia**
Да нет же, если включить на клиенте Амнезию или v2RayN с теми же конфигами, то всё окей. Проблема где-то в ZeroBlock

---

**2026-03-12T22:27:17 | rsm**
Добрый вечер, вчера купил роутер, перечитал вики, есть вопросы, помогите, пожалуйста:
Задача у меня такая, что я хочу поднять на роутере VLESS и чтобы весь трафик шёл через него, не только ютуб и пр., а вообще весь. Мне подойдёт ZeroBlock?

---

**2026-03-12T22:29:25 | Роман**
Напишите в тему zeroblock.

---

**2026-03-12T22:52:37 | Роман**
Ну попробуйте ещё раз запустить скрипт. 
Всё сломаете, сбросите и по новой скрипт 😁
А эти проблемы с подкопом как решать я не знаю. Когда у меня был подкоп он просто работал и всё, сейчас у меня zeroblock.

---

**2026-03-12T22:57:09 | Роман**
А там сбросите роутер и zeroblock установите 😁

---

**2026-03-13T09:05:16 | Andrew**
Здравствуйте. На роутере стоит zeroblock + zapret2. Можно ли это все дело подружить с adguard home? Я ещё не пробовал его ставить, решил сначала узнать можно ли это сделать в принципе?

---

**2026-03-13T09:59:54 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.1-r30:
Новые возможности
  - Поддержка протокола AnyTLS + распознавание hysteria2/hy2/anytls в подписках
  - Unified user_lists — объединение доменов и IP в один список с автоопределением типа, поддержка nft sets и grouped JSON
  - Автоконвертация grouped JSON доменов в sing-box ruleset формат
  - Messengers force_cidr — фильтрация только telegram.org IP при неявном CIDR
  - Fallback API для WARP — автоматический retry через резервный сервер
  - Переименована кнопка добавления секции в LuCI
  - Выбор URL для проверки в Settings(приоритет per-section → global → fallback gstatic)
  - Детекция /etc/init.d/podkop при старте с LOG_ERR предупреждением
  - singbox_startup_timeout (5-300с, default 30с) и xray_startup_timeout (1-120с, default 10с) вынесены в UCI
  - YACD кнопка readonly без secret
  - Выбор URL для проверки задержки (Google, Cloudflare, Huawei, Microsoft) — или свой
  - Поддержка reverse proxy (nginx + HTTPS) — dashboard работает за SSL без mixed content

  Исправления
  - Bootstrap DNS: убран ложный warning при UDP, исправлен маппинг dns_bootstrap для секций, bootstrap-dns не создаётся в конфиге когда не нужен
  - Clash API: переход на json-c вместо popen+curl (решён 4K buffer overflow)
  - Xray диагностика: правильные UCI опции + fallback на proxy_string
  - Outbound диагностика: fallback на proxy_string для всех типов
  - Duplicate rule-set tag для URL с одинаковым хостом
  - LuCI: валидатор порта с trailing slash, YACD кнопка readonly без secret, force_update очистка HTTP-кеша
  - SS Outline URL parsing
  - Парсинг URLTest ссылок с пробелами и эмодзи в именах

  Рефакторинг
  - Удалены legacy user_domain_lists/user_subnet_lists, добавлена миграция
#ZeroBlock

---

**2026-03-13T10:28:45 | Routerich**
[zeroblock] podkop detected! It may conflict with ZeroBlock routing/nftables rules
отлично

---

**2026-03-13T10:50:14 | Anton**
Привет, давно не заходил, решил потестить ZeroBlock 0.7.1-r29, у меня сейчас не RR, а cudy. Vless ключ есть, хотел просто добавить секцию и потестить, все добавилось, выставил из списка russian inside, но трафик не идет через впн, просто обычный инет... что-то с днс ? Или что-то надо доустановливать. списки v1. Диагностика ок все. Думал как подкоп работает - вставил ключ и погнали, но не прокатило ) 

PS Переустановил все начисто и через какое-то время само все заработало без доп операций, как в подкопе, вставил ключ и завелось. Буду тестить

---

**2026-03-13T13:17:26 | Роман**
Все блокировки обходите вы, роутер это инструмент. Сможете найти стратегию для запрет 1/2 - обошли блок. Нашли нормального хостера, подняли сервер, закинули ссылку в zeroblock/podkop - обошли блокировки. 
Сам роутер ничего не делает, он даёт широкие возможности из-за своей прошивки, по сути это мини ПК с Линукс на борту который умеет раздавать интернет.

---

**2026-03-13T13:41:55 | Anna Bagler**
Да, zeroblock.

---

**2026-03-13T14:09:02 | Роман**
Сброс, установка zeroblock по гайдам, настройка ютуба через запрет 1/2 и всё. В первый раз тяжело, потом на автомате 😁

---

**2026-03-13T14:24:27 | Роман**
Засунул подписку в zeroblock, раздал с мобильного интернет роутеру, отключил проводной интернет. Весь трафик пошел через подписку - БС обошёл.

---

**2026-03-13T16:03:17 | Anna Bagler**
На 7.10 без последствий не добавить. На zeroblock не хотите перейти?

---

**2026-03-13T16:07:15 | Anna Bagler**
Лучше на zeroblock перейти https://t.me/routerich/394153/520562
Подкоп отключить и остановить, а лучше на чистый.

---

**2026-03-13T17:23:15 | Marik Kiram**
Здравствуйте, настроен Zeroblock, всё работает. Купил личный awg конфиг, а куда его теперь, я не понимаю 😭🤣

---

**2026-03-13T17:28:17 | Anna Bagler**
Интернет без границ или zeroblock beta.

---

**2026-03-13T17:31:03 | Владимир Волков**
Вам и написали две темы - "Интернет без границ" и "Zeroblock BETA"

---

**2026-03-13T19:05:47 | Anna Bagler**
Анблок есть, но нет luci к нему, ставить zeroblock или скрипт 5 для подкопа.

---

**2026-03-13T19:06:10 | Роман**
Да, в zeroblock есть список games который это разблокирует. Ну на крайний случай домены и ip роблокса вручную докинуть из вики.

---

**2026-03-13T19:39:48 | X**
сорри, от компа уехал, а тгшка слетела с мобилы. я через Zeroblock делал отдельную секцию, туда вставил домены в колонку "Список пользовательских доменов",  которые Роман @ded_ikar ниже скинул тебе. Единственное я через арендный сервер впн настроил, по протоколу shadowsocks, а не vless. не знаю какая разница, но гдето видел запись, что для мортальника якобы он лучше подходит. все заработало в итоге. в оперу пробовал вписывать домены, в онлайн зашло, но при попытке найти матч в боевой лиге с серверов МК выкидывало. поэтому сделал отдельную секцию со своим впн и заработало все

---

**2026-03-13T19:54:22 | 𝒢𝑒𝒻𝑒𝓈𝓉**
подскажите пожалуйста - заново перепрошил Cudy на 24.10.5, установил ZeroBlock последний. VLESS секция работает норм, а TrustTunnel нету в панели управления... В Диагностике ошибок нет.  Куда копать?

---

**2026-03-13T19:56:18 | Роман**
Теперь подбирать стратегию для ютуба дискорда. И дискорд убрать из zeroblock.

---

**2026-03-13T21:47:27 | Никита Веселов**
Заметил странность, при использовании ключа HY2 и я пробовал разные локации. В REPO пинг улетает в максимум. А при ключе VLESS все окей. Список games в ZeroBlock

---

**2026-03-14T00:07:06 | Egor Sorokin**
[config_builder] Sing-box config generated successfully
[config_builder] Starting sing-box...
[config_builder] Sing-box failed to start within timeout
[zeroblock] Failed to start ZeroBlock

---

**2026-03-14T02:14:07 | Anna Bagler**
В обсуждениях youtubeUnblock у самого автора смотрите. Лучше перейти на zeroblock https://t.me/routerich/394153/520562 или скрипт №5 вам выше скинули.

---

**2026-03-14T06:01:06 | Anna Bagler**
Разбирайтесь с перенаправлениями. awg, не хочет подниматься, видимо, блокируют, meta в обоих секциях. Ставили и удаляли zeroblock до подкопа? Определитесь, с чем будете работать, тогда сбрасывайте и настраивайте внимательно. Прошивку можно обновить.

---

**2026-03-14T06:52:21 | Artem**
Я извиняюсь, а zeroblock это где? Есть в Podkop списки сообщества, но там games нету...

---

**2026-03-14T06:57:01 | Anna Bagler**
Zeroblock нужно ставить вместо подкопа. Тема Zeroblock Beta https://t.me/routerich/394153/520562

---

**2026-03-14T08:23:23 | Routerich**
Здравствуйте.
Отловить все домены куда оно обращается и добавить в Zeroblock

---

**2026-03-14T08:29:11 | Данила Ступин**
Здравствуйте! А если обновлять zeroblock с версии 0.6.4 до версии 0.7.1, то конфигурация (настройки и секции) сохраняется или сбрасывается?

---

**2026-03-14T09:17:32 | HiLLL**
По тегу ищите #ZeroBlock

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

**2026-03-14T10:29:36 | 𝒢𝑒𝒻𝑒𝓈𝓉**
уважаемые, если есть у кого ZeroBlock с первыми TrustTunnel клиентами (это 0.6-ые версии, начиная с 0.6.2-r30), скиньте пожалуйста. Буду весьма благодарен!

---

**2026-03-14T10:31:14 | Роман**
Для обхода белых списков на мобильном интернете. Потому что людям при БС важно остаться на связи, а не смотреть Ютуб и качать торренты. А если они это будут делать - сервера быстро прикроют. 
Для zeroblock достаточно одного сервера по цене пачки сигарет на месяц, с амнезией или чем другим.
Ютуб через дурилку для отсутствия рекламы и 4к, остальное в прокси. Не думаю что там будут терабайты трафика идти.

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

**2026-03-14T10:38:22 | 𝒢𝑒𝒻𝑒𝓈𝓉**
уважаемые, если есть у кого ZeroBlock с первыми TrustTunnel клиентами (это 0.6-ые версии, начиная с 0.6.2-r30), скиньте пожалуйста. Буду весьма благодарен!

---

**2026-03-14T10:47:50 | Данила Ступин**
Здравствуйте! Может кто сталкивался с такой проблемой и нашёл решение. Установлены zapret2 и zeroblock. На каждом настроены свои секции. Но есть небольшое количество сайтов, которые после установки запрета и зероблока начинают бесконечно загружаться (к примеру у меня одним из таких сайтов является https://calibre-ebook.com/). При этом этих сайтов нет в секциях запрета и зероблока (и РКН их не блокировал). Добавление доменов этих сайтов в запрет или зероблок также не помогает. И даже, если остановить обе этих службы, то сайты все равно грузиться не будет. 

Раньше я подобное наблюдал, если установить запрет через zapret manager, где все сайты принудительно идут через него. Но там это решалось включением режима работы только с заблокированными сайтами. Но zapret2 у меня и так работает в таком режиме.

И вот я даже не знаю куда копать. Единственное, что я выяснил, так это то, что у некоторых сайтов (rutracker к примеру) происходит dns hijacking. Проверял я это через специальную утилиту. Если не добавить такие сайты со всеми их доменами в zb (zapret2 использовать), то происходит перехват dns запроса оператором. Но этого быть не должно, так как роутер по умолчанию (а я сбрасывал настройки) вроде и так использует google dns. Может проблема, описанная выше, связана с этим, а может нет. В общем, если кто сталкивался с этим - буду рад любой помощи.

---

**2026-03-14T10:48:12 | Роман**
В zeroblock/podkop.

---

**2026-03-14T11:12:45 | Kirill Y**
Здравствуйте! Подскажите, после обновления zeroblock пункты с 6 по 11 тоже всегда надо выполнять?

---

**2026-03-14T12:57:27 | Сергей**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.1-r30:
Новые возможности
  - Поддержка протокола AnyTLS + распознавание hysteria2/hy2/anytls в подписках
  - Unified user_lists — объединение доменов и IP в один список с автоопределением типа, поддержка nft sets и grouped JSON
  - Автоконвертация grouped JSON доменов в sing-box ruleset формат
  - Messengers force_cidr — фильтрация только telegram.org IP при неявном CIDR
  - Fallback API для WARP — автоматический retry через резервный сервер
  - Переименована кнопка добавления секции в LuCI
  - Выбор URL для проверки в Settings(приоритет per-section → global → fallback gstatic)
  - Детекция /etc/init.d/podkop при старте с LOG_ERR предупреждением
  - singbox_startup_timeout (5-300с, default 30с) и xray_startup_timeout (1-120с, default 10с) вынесены в UCI
  - YACD кнопка readonly без secret
  - Выбор URL для проверки задержки (Google, Cloudflare, Huawei, Microsoft) — или свой
  - Поддержка reverse proxy (nginx + HTTPS) — dashboard работает за SSL без mixed content

  Исправления
  - Bootstrap DNS: убран ложный warning при UDP, исправлен маппинг dns_bootstrap для секций, bootstrap-dns не создаётся в конфиге когда не нужен
  - Clash API: переход на json-c вместо popen+curl (решён 4K buffer overflow)
  - Xray диагностика: правильные UCI опции + fallback на proxy_string
  - Outbound диагностика: fallback на proxy_string для всех типов
  - Duplicate rule-set tag для URL с одинаковым хостом
  - LuCI: валидатор порта с trailing slash, YACD кнопка readonly без secret, force_update очистка HTTP-кеша
  - SS Outline URL parsing
  - Парсинг URLTest ссылок с пробелами и эмодзи в именах

  Рефакторинг
  - Удалены legacy user_domain_lists/user_subnet_lists, добавлена миграция
#ZeroBlock

---

**2026-03-14T13:58:34 | Святос**
Ставьте ZeroBlock, через него живет

---

**2026-03-14T13:58:48 | Anna Bagler**
Можно поставить zeroblock и пустить сбербокс в полную маршрутизацию.

---

**2026-03-14T14:04:48 | Никита Веселов**
Настроен VPN в zeroblock и дискорд оттуда убран. Настроены домены дискорда через Zapret2. Но трафик через Zeroblock все равно идет в дискорд. Не понимаю почему такое может быть

---

**2026-03-14T14:07:44 | Anna Bagler**
Если есть навыки, то вы можете ставить zeroblock https://t.me/routerich/394153/520562 или подкоп  https://t.me/routerich/3845/245550

---

**2026-03-14T14:36:10 | Anna Bagler**
Конечно, но лучше на zeroblock перейти.

---

**2026-03-14T15:57:23 | Вадим**
Открываю службы... Подкопа нет первое идёт zeroblock

---

**2026-03-14T15:59:31 | Anna Bagler**
Ну, в секциях zeroblock находите awg, изменить, в IP для полной маршрутизации выбирайте нужный IP.

---

**2026-03-14T16:42:15 | Роман**
Выбрать список telgram в podkop, или messengers в zeroblock. Или искать прокси для телеги.

---

**2026-03-14T16:45:17 | Роман**
Здравствуйте. Запрет весь трафик модифицирует. А в zeroblock/podkop можно в исключения добавить ip ноутбуков. И это не только на данном роутере, на любом с openwrt.

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

**2026-03-14T22:04:47 | Дмитрий**
Было такое когда поставил ZeroBlock и игрался с секциями. Остановил ZB и пакеты обновились. После старта ZB опять ошибка, забил так как понял как обойти.

---

**2026-03-14T22:08:17 | Routerich**
Разные способы разблокировки, кому что нравится.
Скорой перейдём на Zeroblock

---

**2026-03-14T23:03:49 | Дмитрий**
Zeroblock + Zapret2. Копался только в ZB, в запрете ютуб по дефолту

---

**2026-03-14T23:43:36 | Nick**
Завтра будем zeroblock  вкорячивать. До сегодня обходился постом, молитвой и zapret.
Да и то последнего недели три как роставил

---

**2026-03-14T23:55:46 | РУЗОВ Дмитрий**
Можно у знать ZeroBlock какая версия крайняя? У Романа на скриншоте 0.7.1-r30, у меня в доступных 0.7.0-r28

---

**2026-03-15T02:30:41 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.1-r33:
  Исправления:
  - Диагностика DNS. Исправлена проверка перенаправления DNS в LuCI.

  Изменения:
  - Post-Quantum VLESS. Добавлена поддержка PQ шифрования VLESS (mlkem768x25519). Поскольку sing-box не поддерживает PQ encryption, такие прокси автоматически маршрутизируются через xray-core (требуется v26.1.13+). Парсинг параметров encryption и pqv из URL, генерация tcp+reality streamSettings для xray.
  - Кастомный путь к бинарникам. Добавлена UCI опция trusttunnel_path по аналогии с xray_path — можно указать свой путь к бинарнику TrustTunnel.
  - DPI Checker. Убран спам ошибок в логах — результаты проверки DPI теперь выводятся как INFO с понятными описаниями, технические детали перемещены в DEBUG. Статус "Failed" переименован в "Inconclusive".
  - Буферы для PQ ключей. Увеличены лимиты URL: подписки до 10 КБ, proxy_string до 32 КБ — post-quantum ключи занимают значительно больше места.
#ZeroBlock

---

**2026-03-15T09:24:10 | Константин**
Тоже планирую сегодня начать настройку, подскажите а zeroblock не лучше будет скрипта, так как почитал, они вроде конфликтуют

---

**2026-03-15T09:24:58 | Anna Bagler**
Zeroblock лучше, если навыки позволяют, ставьте его.

---

**2026-03-15T10:29:53 | Святос**
Есть ZeroBlock

---

**2026-03-15T11:07:38 | Anna Bagler**
Так если все, что надо, работает, пусть себе работает. Если прям хотите, обновляйтесь и zeroblock и zapret2.

---

**2026-03-15T11:10:21 | Владимир**
Для протокола, вдруг еще кому понадобится. В zeroblock секции awg активируем список cdn:aws.  Так же ds3 делает вызовы к fdp-steam-ope-login.fromsoftware-game.net. Остальные сослы небось где то ррядом живут. Я завернул в awg только этот хост, но думаю можно весь домен смело туда отправить. Онлайн в игре ожил.

---

**2026-03-15T11:44:46 | ㅤㅤ**
Да, это было очевидно. Последние недели экспериментировал с со своими серваками, а также Xkeen/Mihomo уже и подзабыл что предлагает ZeroBlock. В Routerich по пятому скрипту ставится AmneziaWG 1.0 верно?

---

**2026-03-15T12:02:54 | Роман**
Dear developer, такое zeroblock примет?
https://t.me/routerich/4/547277

---

**2026-03-15T12:24:46 | Роман**
Нет, нисколько. Я бы и обновления списков в zeroblock сделал бы раз в дней десять - пятнадцать, что-бы не ломалось ничего при неполадках на сервере.

---

**2026-03-15T13:34:46 | Anna Bagler**
Zeroblock+zapret2.

---

**2026-03-15T13:35:46 | Роман**
Запрет, запрет2, полное прокси через podkop/zeroblock.
Приставка пс 5
Задача разблокировать то что заблокировано 
И не мешало играть на пс 5 
Не поднимало пинг и не резало скорость скачивания 
То-же самое, прокси поднимет пинг в любом случае.
Разница между скриптои бета и пятым в версии подкопа, и всё.

---

**2026-03-15T15:19:44 | Роман**
Я на голом запрете 1 тестировал, без podkop/zeroblock/zapret2, всё отключил.

---

**2026-03-15T15:28:32 | Роман**
Можно проще, установить zeroblock, включить автонастройку, как появятся секции отключить автонастройку и автозагрузку секций и импортировать свой конфиг в awg10 - я так использую. (Разработчики советуют самому создавать интерфейс, но я с этим не разобрался 😁)

---

**2026-03-15T15:29:10 | Роман**
https://t.me/routerich/394153/520562
Хороший мануал по zeroblock.

---

**2026-03-15T15:30:22 | Alex Gubkin**
приветы! сильно не пинать, поставил пакеты zeroblock и lucy в опенврт xiaomi ax3000t, но не появилось пункта автозагрузки, на роутерич ставил было норм

---

**2026-03-15T15:34:27 | Nikita**
Получается, что ты живешь с залетом левого трафика?)
ipv6 ? не понял, у меня выключено.
видимо синг ругается на dns и смог поймать такую проблему, скрин закинул. ( запуская диагностику подряд несколько раз(до 10), сразу после применения конфигурации, то 20%, что покажет проблему с dns)
повторная диагностика показывает уже нормально, всё зелёное, но в логах всё еще ошибка dns rule.

Вот лог:
[zeroblock] Starting ZeroBlock(0.7.1-r30)...
[clash_api] /proxies failed: Error
[clash_api] /proxies failed: Error
[clash_api] /proxies failed: Error
[ [38;5;183m1140320423 [0m 615ms] dns: exchange failed for wpad.lan. IN A: read udp 127.0.0.1:37648->127.0.0.1:53: read: connection refused
[ [38;5;183m1140320423 [0m 615ms] router: process DNS packet: read udp 127.0.0.1:37648->127.0.0.1:53: read: connection refused
[zeroblock] ZeroBlock started successfully
[ [38;5;200m1698192568 [0m 0ms] router: process DNS packet: drop connections by rule
[ [38;5;216m2431505608 [0m 1ms] router: process DNS packet: drop connections by rule

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

**2026-03-15T15:44:35 | Роман**
Я бы ответил что особой разницы нет, но меня забанят.
В zeroblock добавлено много улучшений по сравнению с подкопом, поддержка подписок, xhttp, исключений, списки расширенные.

---

**2026-03-15T16:36:58 | Nikita**
Да, 1.1 это роутер.
У меня 24.10.5 практически чистая, установлен только tailscale + zeroblock с awg 2.0 (собственный сервер)
И еще attended upgrade, делал сборку на чистую, чтобы в дальнейшем получать обновы

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

**2026-03-15T17:23:22 | Роман**
В zeroblock одну галку поставить.

---

**2026-03-15T17:23:52 | Alexander**
гуглю zeroblock и всякую дичь получаю

---

**2026-03-15T17:24:17 | Anna Bagler**
Тема zeroblock beta.

---

**2026-03-15T18:45:39 | Artem**
А что значит свой vless? Как сделать? Такая же ошибка 279 через opera (zeroblock)

---

**2026-03-15T19:03:09 | Aleks**
Скажите пожалуйста, практически каждый день останавливается warp, иногда хватает на 2 дня. Приходится постоянно контролировать его на роутере и перезапускать zeroblock. Может что то нужно настроить еще? Настраивал роутер с нуля так, установил zeroblock, потом в нем в автонастройки и поставил все галочки по краткому мануалу и все установилось и заработало. но периодически останавливается warp и как результат не работает ютуб телега вотсап и торренты. opera работает.

---

**2026-03-15T19:20:42 | Фома Кузьмич**
один из проксируемых сайтов а именно rutracker.org через пк (что по кабелю подключен) не открывается - висит бесконечная загрузка а вот через телефон что подключен к этому же роутеру но по wi-fi все норм работает за исключением что когда открываешь на пк на телефоне тоже временно перестает работать, если на пк перестать пытаться то на телефоне оживает и на сайт сразу заходит, zeroblock ставил строго по инструкции из закрепа на чистый только что сброшенный роутер, есть еще пара сайтов что себя так ведут, в остальном нормально, куда копать подскажите и какие логи или что нужно?

---

**2026-03-15T19:56:30 | ARTEM**
Как загрузить свой конфиг awg в zeroblock, создаю секцию но не понимаю куда именно конфиг вставлять

---

**2026-03-15T20:16:49 | HiLLL**
это err?
[zeroblock] Starting ZeroBlock(0.7.0-r18)...
[zeroblock] ZeroBlock started successfully

---

**2026-03-15T20:35:31 | Anna Bagler**
Тогда лучше zeroblock и по IP ПК в полную маршрутизацию.

---

**2026-03-15T20:36:09 | Усатый Бро**
Luci zero block установлена 38 версия но если сам zeroblock открывать показано что 28 . В чем может быть дело . Брал удалял принудительно и званого 38 версию ставил и все равно остаётся 28я. Это критично ?

---

**2026-03-15T22:15:58 | HiLLL**
по тегу #ZeroBlock запишите на бумажке, пригодится

---

**2026-03-15T23:00:49 | AndrewKomarov**
Вопрос.
На чистый RR сейчас накатил скрипт5 ( он же еще относительно актуален?) Теперь надо запрет сносить и ставить Zeroblock+Zapret2 (где про него почитать?)

---

**2026-03-15T23:17:47 | AndrewKomarov**
я же верно понял, что zeroblock заменяет podkop теперь?

---

**2026-03-16T08:19:49 | Alex Korshun**
Я с discord воюю уже третьи сутки, blockcheck2 цепляет стратегии, но в последствии ни одна не работает. Делал по инструкции pdf от местного человека. Пока что плюнул и завернул дис в zeroblock.

---

**2026-03-16T09:40:56 | Роман**
Попробуйте начисто zeroblock установить.

---

**2026-03-16T09:48:52 | Anna Bagler**
Тема zeroblock beta.

---

**2026-03-16T09:56:08 | Роман**
У меня он пока работает по Ютубу, Дискорду и автохостлист - иногда открывает заблокированное иногда нет.
Мне проще домены сайта в прокси zeroblock закинуть, чем сидеть с блокчеком и ковырять стратегии. Или локально амнезию ВПН запустить - если сайт нужен один раз.

---

**2026-03-16T10:45:19 | Andrey Voloshin**
root@OpenWrt:~# zeroblock status
ZeroBlock Status
================

Service enabled: yes
Sing-box running: yes
Config exists: yes
NFTables rules: active
Policy routing: active
DNS forwarding: configured

Overall: RUNNING
root@OpenWrt:~#

---

**2026-03-16T11:36:07 | Anna Bagler**
https://t.me/routerich/80283/352975?single - прошивка
Zeroblock по инструкции выше.

---

**2026-03-16T12:43:41 | Anna Bagler**
У вас ютуб и через zeroblock, и через zapret2. Уберите из секции zeroblock. И проверьте.

---

**2026-03-16T12:43:49 | Uintik️️️🐈‍⬛**
Добрый день. Обновил прошивку на роутере(rr usb2.0) установил ZeroBlock 0.7.1-r33 Не могу запустить ZeroBlock лог: Mon Mar 16 12:29:58 2026 user.notice ucitrack: Setting up /etc/config/zeroblock reload trigger for non-procd /etc/init.d/zeroblock
Mon Mar 16 12:30:10 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock(0.7.1-r33)...
[clash_api] /proxies failed: Error
[clash_api] /proxies failed: Error
[clash_api] /proxies failed: Error
[config_builder] Sing-box failed to start within timeout
[zeroblock] Failed to start ZeroBlock
Mon Mar 16 12:34:50 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: Error: Failed to start ZeroBlock
Mon Mar 16 12:35:29 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock(0.7.1-r33)...
Mon Mar 16 12:35:42 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[cron_manager] Cron file not found: /etc/crontabs/root
[zeroblock] ZeroBlock stopped successfully
Mon Mar 16 12:35:46 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock(0.7.1-r33)...
[config_builder] Sing-box failed to start within timeout
[zeroblock] Failed to start ZeroBlock
[config_builder] Sing-box failed to start within timeout
[zeroblock] Failed to start ZeroBlock
[clash_api] /proxies failed: Error
[clash_api] /proxies failed: Error
[clash_api] /proxies failed: Error

---

**2026-03-16T14:06:22 | Anna Bagler**
Zeroblock есть? В секцию списки и интерфейс добавляйте и проверяйте.

---

**2026-03-16T14:17:31 | Роман**
Для игры в Guild Wars 2 достаточно этих CDN в ZeroBlock.
#Games

---

**2026-03-16T14:25:50 | Алексей Михайлов**
на nyaa.si захода так и нет. сайт выдает ошибку 504. в журнале зероблок сыпятся следующие ошибки

[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
[clash_api] /proxies failed: Error

---

**2026-03-16T14:33:48 | User Friendly**
А чем podkop от zeroblock отличается?

---

**2026-03-16T14:34:44 | Routerich**
Тем что это наша разработка, плюс доп фичи, которых сейчас нет в подкопе. По тегу #Zeroblock в теме зероблок всё можно найти

---

**2026-03-16T14:50:59 | Paulus**
В пакетах потом zeroblock можно найти? я обновил и его там нет

---

**2026-03-16T15:43:28 | Святос**
Зайти в тему ZeroBlock и установить

---

**2026-03-16T17:29:07 | Борис**
Да, это будут статичные файлы inbounds.json и route.json в папке /etc/zeroblock/sing-box.d

---

**2026-03-16T18:01:31 | Ivan Num**
Подскажите в zeroblock в отличии от podkop списки доменов и подсетей автоматически обновляются в сообществе?

---

**2026-03-16T19:45:49 | Роман**
Выбрать список games в zeroblock.

---

**2026-03-16T20:13:25 | Мишевый Плюшка**
А то что в закрепе, и то что zeroblock beta как отличаются?

---

**2026-03-16T21:38:38 | Борис**
Здравствуйте. На роутер можно поставить podkop и zapret :)

Ещё можно поставить zeroblock из соседней темы. Но он так же неустойчив к психическим припадкам и может быть опрометчиво удалён в гневе, так что обходы снова перестанут работать...

---

**2026-03-16T21:40:29 | Борис**
Ну а если серьёзно, то по идее одного запрета2 достаточно, чтобы большинство сайтов открывались, нужно только потратить время на поиск хорошей стратегии. Для обхода геоблокировок достаточно opera-proxy (встроена в zeroblock)

---

**2026-03-16T22:03:10 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.1-r50:
  Исправления:
  - DNS: исправлена критическая проблема с AAAA
  Полностью переработана обработка AAAA запросов при выключенном IPv6. Ранее AAAA reject rules с методами drop/default/NULL ломали системный резолвер musl на роутере — ping, opkg, wget зависали или получали REFUSED. AAAA reject rules полностью убраны — strategy: "ipv4_only" в sing-box сам возвращает пустой ответ на AAAA запросы. DNS strategy теперь автоматически выбирается:
  - ipv6_enabled=0 → ipv4_only
  - ipv6_enabled=1 → prefer_ipv4

  - PTR reverse DNS для Fully Routed устройств
  При полной маршрутизации устройства обратные DNS запросы (nslookup) уходили в туннель вместо dnsmasq. Добавлена автоматическая генерация PTR суффиксов (.in-addr.arpa) на основе IP/маски source интерфейсов.

  - Фоновый запуск при обновлении пакета
  При установке через opkg/apk zeroblock теперь стартует в фоне, не блокируя пакетный менеджер. Ожидание dnsmasq до 10 сек перед запуском.

  - Кастомный порт DNS
  Во всех местах (UDP, TCP, DoH, DoT, bootstrap,+ per-section) поддерживается формат host:port и [::1]:port. Например 127.0.0.1:9053 для локального DNS.

  Диагностика DNS
  - DNS redirect 127.0.0.42 без порта теперь валиден (порт 53 дефолтный)
#ZeroBlock

---

**2026-03-16T22:13:16 | Aydar**
как я понял надо курить тему Zeroblock, т.к. у меня чисто ютуб анблок стоял и этого хватало, но на телегу не работает, такие дела

---

**2026-03-16T22:25:51 | Anna Bagler**
Для них нужен zeroblock или podkop.

---

**2026-03-16T22:26:18 | Виктор ZEUS**
Да, Zeroblock стоит

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

**2026-03-16T23:29:15 | Александр**
Mon Mar 16 23:13:00 2026 user.notice ucitrack: Setting up /etc/config/zeroblock reload trigger for non-procd /etc/init.d/zeroblock
Mon Mar 16 23:23:17 2026 user.notice zeroblock: Starting ZeroBlock...
Mon Mar 16 23:23:17 2026 daemon.err zeroblock[8991]: [zeroblock] Starting ZeroBlock(0.7.1-r50)...
Mon Mar 16 23:23:56 2026 daemon.err zeroblock[8991]: [config_builder] Sing-box failed to start within timeout
Mon Mar 16 23:23:56 2026 daemon.err zeroblock[8991]: [zeroblock] Failed to start ZeroBlock
Mon Mar 16 23:23:56 2026 daemon.notice procd: /etc/rc.d/S99zeroblock: Error: Failed to start ZeroBlock
Mon Mar 16 23:24:09 2026 daemon.err zeroblock[9986]: [clash_api] /proxies failed: Error
Mon Mar 16 23:24:09 2026 daemon.err zeroblock[9987]: [clash_api] /proxies failed: Error
Mon Mar 16 23:24:09 2026 daemon.err zeroblock[9993]: [clash_api] /proxies failed: Error
Mon Mar 16 23:25:28 2026 daemon.err zeroblock[12970]: [clash_api] /proxies failed: Error
Mon Mar 16 23:25:28 2026 daemon.err zeroblock[12975]: [clash_api] /proxies failed: Error
Mon Mar 16 23:25:28 2026 daemon.err zeroblock[12977]: [clash_api] /proxies failed: Error
Mon Mar 16 23:25:50 2026 daemon.err zeroblock[13141]: [clash_api] /proxies failed: Error
Mon Mar 16 23:25:50 2026 daemon.err zeroblock[13143]: [clash_api] /proxies failed: Error
Mon Mar 16 23:25:50 2026 daemon.err zeroblock[13147]: [clash_api] /proxies failed: Error
Mon Mar 16 23:28:42 2026 daemon.err zeroblock[14844]: [clash_api] /proxies failed: Error
Mon Mar 16 23:28:42 2026 daemon.err zeroblock[14866]: [clash_api] /proxies failed: Error
Mon Mar 16 23:28:42 2026 daemon.err zeroblock[14867]: [clash_api] /proxies failed: Error

---

**2026-03-17T00:26:10 | Роман**
Выбрать список messengers  в zeroblock.

---

**2026-03-17T00:27:40 | Дмитрий**
Доброй ночи, подскажите плиз. Настроил. Подключается из внешней сети и могу управлять роутером. Но правила обхода не работают. Использую zeroblock.

---

**2026-03-17T00:51:53 | Роман**
А знаете почему работает? Потому что весь трафик идёт в ВПН. Ищите домены и добавляйте в zeroblock - будет работать.

---

**2026-03-17T01:05:37 | Routerich**
HiLLL Александр перекачайте zeroblock_0.7.1-r50_aarch64_cortex-a53 удалите и поставьте заново, проверяйте списки

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

**2026-03-17T09:41:50 | Alex Korshun**
Перед походом на тренировку увидел zeroblock r50 и патчноут к нему. Вернулся с тренировки и уже висит r52, а патч ноута не вижу.🐒

---

**2026-03-17T11:22:57 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.1-r53:
  Исправления:
  - FIX регрессии dns-rule
#ZeroBlock

---

**2026-03-17T12:20:22 | Max**
а если у меня Zeroblock привязан к своему интерфейсу?

---

**2026-03-17T12:30:15 | Andrey Volgin**
нужно ли при обновлении версии zeroblock удалять сначала старую? Накатил сверху, без удаления, пока полет нормальный.

---

**2026-03-17T12:35:04 | Anna Bagler**
Нет, или повторно скрипт, или zeroblock. Запустите это в терминале роутера, cкрин результата пришлите.
sh <(wget -qO- https://raw.githubusercontent.com/kkkkCampbell/master/refs/heads/test_config_script/test_config_script_nightly)

---

**2026-03-17T12:37:40 | iProxx**
Ок, завтра проверю.
А в zeroblock такие же возможности как у Beta?

---

**2026-03-17T15:20:40 | Anna Bagler**
Ставить файлами из темы zeroblock beta.

---

**2026-03-17T15:35:13 | Виталий Савченко**
а где есть прям пошаговая инструкция куда жать и какие файлы надо? опять же в чате zeroblock beta нашел в закрепе 2 файла а что с ними делать без понятия

---

**2026-03-17T15:37:31 | ZZII | RTK**
Стоит ли включать SQM на OpenWRT при скорости ~500 Мбит/с, если использую VPN (ZeroBlock / VLESS) и есть bufferbloat (оценка C)?

---

**2026-03-17T16:15:08 | Keeper**
Приветствую!
А в секциях поля "Пользовательские списки" на локальные списки как должны заполняться правильно?
Делал по аналогии с подкопом /path/file.lst для доменов и вторую строку файл для cidr
В итоге получил такое в логе:
[config_builder] Sing-box failed to start with full configuration
[zeroblock] Failed to start ZeroBlock
Обновил zb до *53 с ребутом - тож самое.
Убираю строки, перезапускаю и zb с sing-box стартуют без проблем, все летит.

Списки roblox обычные с iplist.opencck.org текстовый файл построчный, права 777.
Список "games" убирал перед тем как пихать локальные списки.
Секция VLESS. DNS doh от adg.

---

**2026-03-17T16:38:02 | Роман**
https://t.me/routerich/394153/534505
Или диагностику zeroblock запустите.

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

**2026-03-17T17:44:11 | Shtef**
спасибо. в таком же порядке? сначала Zeroblock_*** а затем luci-app***?

---

**2026-03-17T19:44:07 | Anna Bagler**
Zeroblock или podkop скриптом ставить.

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

**2026-03-17T21:16:02 | Константин**
Вот и я получил коробочку (Routerich AX3000 v1 с USB 3.0). В Брянск доставили за 2 дня(оперативно). Что могу сказать... По сравнению с MediaTek MT7621 это конечно песня! Всё шустро шевелится. Поставил Zeroblock, вписал свои ссылки vless. Всё шустро работает. Zerotier настроил мухой. Пока впечатления чисто положительные, буду дальше разбираться с остальными установленными пакетами. Спасибо за такую железку! Порадовали деда. :)

---

**2026-03-17T21:41:02 | HiLLL**
через ZeroBlock

---

**2026-03-17T21:52:17 | Роман**
Ну закиньте свой ВПН в zeroblock и протестируйте грок. Всё хорошо работает.

---

**2026-03-17T21:59:44 | Den**
Доброго вечера. Подскажите, как можно пустить IPTV (vipdrive) с Android TV box, через zeroblock? В yacd при просмотре каналов IP-шники меняются постоянно... CDN
Весь трафик с приставки маршрутизировать в моих условиях нет смысла...

---

**2026-03-17T22:38:55 | Александр**
В logread | grep zeroblock пусто
Все клиенты с телефона вроде как хавают, а ZB

---

**2026-03-17T23:02:20 | Routerich**
Здравствуйте.
Создать интерфейс AmneziaWG и Импортировать вв него свой конфиг, потом в Zeroblock создать новую секцию vpn и там выбрать созданный интерфейс

---

**2026-03-18T00:24:21 | Sergey G**
здравствуйте.  есть роутер OpenWrt 24.10.5 с ZeroBlock 0.7.1-r38
в интернет детекторе висит статус WARP отключен
перезапускал интерфейс awg10 и zb - ничего не поменялось

когда запускаю команду - zeroblock awg warp
наблюдаю что интерфейс перезапускается несколько раз
затем выводится сообщение

========================================================================
         WARP CONFIGURATOR - Full AWG Setup
========================================================================

Starting AmneziaWG WARP configuration...
This will:
  1. Request WARP configuration from RouteRich API
  2. Configure network interface (awg10)
  3. Configure firewall zones
  4. Restart firewall service
  5. Bring up interface
  6. Test connectivity and find working endpoint

Automatically including '/usr/share/nftables.d/table-post/20-miniupnpd.nft'
Automatically including '/usr/share/nftables.d/chain-post/dstnat/20-miniupnpd.nft'
Automatically including '/usr/share/nftables.d/chain-post/forward/20-miniupnpd.nft'
Automatically including '/usr/share/nftables.d/chain-post/srcnat/20-miniupnpd.nft'

========================================================================
 ❌ WARP CONFIGURATION FAILED
========================================================================

Status: Connectivity test failed
Message: No working endpoint found

Работает ли  вообще этот генератор конфигов?
Или может дело в в том, что роутер у меня подключен вторым, после роутера OpenWrt 24.10.2, где стоит podkop
Может ли это как то мешать?

---

**2026-03-18T00:30:08 | Sergey G**
на 24.10.2 я не могу поставить ZeroBlock
чтобы не обновлять прошивку роутера со сбросом настроек
пробую понять чем лучше в данном случае ZeroBlock на подменном роутере

---

**2026-03-18T00:41:51 | Sergey G**
я сделал проще, на первом роутере остановил podkop и zapret2
выполнил команду zeroblock awg warp
WARP подключился

---

**2026-03-18T01:24:02 | Sergey G**
можно вопрос
почему в podkop по умолчанию почти все списки выбраны в секции с "proxy" (при этом почти все работает), а в секции с "vpn" всего несколько списков

а в zeroblock наоборот, больше списков выбрано в секции с "vpn"?
и мне показалось теже самые ресурсы через "vpn" открываются медленнее

---

**2026-03-18T01:40:23 | Никита Веселов**
А как работает автозагрузка Zapret2 стратегий в zeroblock? галки стоят, а rr_ стратегии не появляются в запрете

---

**2026-03-18T09:18:44 | Routerich**
поищите слово в теме zeroblock

---

**2026-03-18T09:47:26 | Роман**
В zeroblock создаете новую секцию, выбираете - сервер прокси - trust tunnel - вносите нужные данные, выбираете списки profit.

---

**2026-03-18T09:54:29 | Роман**
В podkop/zeroblock.

---

**2026-03-18T11:25:11 | Artem**
В podkop и  zeroblock списки включены, а есть ещё какие то решения ?

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

**2026-03-18T13:01:41 | Anna Bagler**
А если включить подкоп и что у вас там было из запретов и ещё раз код диагностики?
На zeroblock не хотите попробовать перейти?

---

**2026-03-18T13:57:19 | Konstantin Uk**
подскажите пожалуйста, а если две амнезии (основная и бекап), и вдруг одна из них не работает, можно ли как-то настроить в самом ZeroBlock чтобы он использовал запасную конфигурацию? Может быть конечно это как-то на уровне интерфейсов разруливается, тогда ткните пожалуйста куда копать, чтобы так сделать.

---

**2026-03-18T17:40:20 | Anna Bagler**
Если есть навыки, то вы можете ставить zeroblock https://t.me/routerich/394153/520562 или подкоп  https://t.me/routerich/3845/245550

---

**2026-03-18T18:56:31 | Владислав**
Ну чёт, видимо либо у меня json кривой, либо я опять что то не так делаю😂
Как только включаю zeroblock сразу в ошибку proxy падает и всё

---

**2026-03-18T19:02:04 | Владислав**
прошу помочь)
пытаюсь в zeroblock закинуть впн клиент через расширение json после того как всё вписываю и включаю zeroblock сразу падает в ошибку proxy и выключается

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

**2026-03-18T19:43:02 | Владислав**
в общем щас сам конфиг кривой?
или просто в нём не нужной инфы много для zeroblock?

---

**2026-03-18T19:53:32 | Routerich**
zeroblock + fragment (как создавать в changelog) 
либо подкоп и mixed proxy. последний в любом из двух пакетов есть

---

**2026-03-18T20:10:49 | Anna Bagler**
Если есть навыки, то вы можете ставить zeroblock https://t.me/routerich/394153/520562 или подкоп  https://t.me/routerich/3845/245550

---

**2026-03-18T20:27:22 | Anna Bagler**
Обновляйтесь, потом zeroblock или скрипт №5.

---

**2026-03-18T20:41:12 | HiLLL**
ну у вас синг бокс болеет попробуйте в терминале
service zeroblock stop
opkg update
opkg remove sing-box --force-depends
opkg install sing-box-tiny
service zeroblock start

---

**2026-03-18T20:41:37 | Anna Bagler**
Вам лучше zeroblock и секцию catch-all. В подкопе тогда пробуйте полную маршрутизацию по IP/подсети.

---

**2026-03-18T20:53:02 | Andrey**
Zeroblock. Вам Анна ровно это и написала

---

**2026-03-18T21:02:38 | Anna Bagler**
Тема Zeroblock Beta. Файлы и ссылка на полный мануал в закрепе. Кратко - https://t.me/routerich/394153/520562

---

**2026-03-18T21:03:00 | Борис**
Zeroblock нет в репозитории, его надо скачать из закрепа в соседней теме "zeroblock" и установить вручную по инструкции из закрепа (установка на этой же странице со скриншота)

---

**2026-03-18T21:26:57 | Алексей**
А где брать zeroblock или скрипт 5?

---

**2026-03-18T21:30:19 | Anna Bagler**
Тема Zeroblock Beta https://t.me/routerich/394153/520562 или подкоп  https://t.me/routerich/3845/245550

---

**2026-03-18T21:38:16 | Anna Bagler**
Значит ищите тему Zeroblock Beta, закреп в ней, там файлы для установки и ссылка на полный мануал или Интернет без границ, закреплённые сообщения и ищем скрипт №5.

---

**2026-03-18T21:51:06 | Andrey**
Добрый вечер, подскажите пожалуйста, как добавить ссылкой свой vless сервер в секцию vpn в podkop?или нужно ставить zeroblock beta?

---

**2026-03-18T21:51:24 | X**
То есть мне надо этот скрипт поставить? У меня стоит zeroblock. В настройках а iPhone я не вижу безопасных днс. Там «автоматически» стоит

---

**2026-03-18T21:52:21 | Anna Bagler**
Лучше zeroblock.

---

**2026-03-19T07:22:18 | Anna Bagler**
Если есть навыки, то вы можете ставить zeroblock, он предпочтительнее https://t.me/routerich/394153/520562 или подкоп  https://t.me/routerich/3845/245550

---

**2026-03-19T08:48:48 | Роман**
Установил зероблок
Подкоп
Что может пойти не так?
Останавливайте что-то одно. И да, без логов вам сложно помочь. Подкоп с zeroblock вы используете на свой страх и риск.

---

**2026-03-19T08:54:59 | Routerich**
Вам легче роутер сбросить и установить Zeroblock на чистую

---

**2026-03-19T09:01:19 | Роман**
Запрет 2 работает по Ютубу и Дискорду, плюс автохостлист. 
Запрет 1 остановлен. 
Подкоп остановлен на данный момент. 
Zeroblock работает.

---

**2026-03-19T11:12:17 | Anna Bagler**
В zeroblock ссылка vless своя и все. Или что там у вас будет из поддерживаемого.

---

**2026-03-19T11:19:59 | Anna Bagler**
Если желания разбираться совсем нет, то сюда https://t.me/routerich/3845/245550, если есть, то zeroblock beta и сюда https://t.me/routerich/394153/520562

---

**2026-03-19T11:40:08 | Anna Bagler**
Если в discord, попробуйте в main, но голоса не будет. Ещё это посмотрите https://t.me/routerich/394153/550458
Ecть zeroblock вместо подкопа.

---

**2026-03-19T12:50:05 | Anna Bagler**
Сброс будет проще и передходите на zeroblock.

---

**2026-03-19T13:21:48 | Anna Bagler**
Потенциально можно, изучите podkop.net на предмет корпоративного vpn и полный мануал по zeroblock.

---

**2026-03-19T13:52:32 | Вера Н**
Добрый день, на айфоне пропал YouTube, на тв работает. Установлен zeroblock

---

**2026-03-19T13:57:01 | Алексей Сергеевич**
Нет, Zeroblock это автонастройка, в которой можно отметить установку Zapret2

---

**2026-03-19T14:01:19 | Алексей Сергеевич**
Мне zeroblock больше нравится, не каких скриптов запускать не нужно, сбросил роутер, обновил пакеты, поставил 2 приложения, отметил 3 галочки opera, awg и zapret2 и готово. + в настройках выставил списки куда ходить, geo блок через opera остальное awg, YouTube через Zapret2

---

**2026-03-19T14:20:53 | Andrey 🐸**
При установке пакета zeroblock такая ошибка, что делать?

---

**2026-03-19T14:34:37 | Chezok**
службы,  zeroblock, секции маршрутизации, изменить

---

**2026-03-19T14:47:14 | iProxx**
Привет всем! По инструкции выше настроил Zeroblock + Zapret2 на последнюю прошивку. Youtube и Whatsapp работают. А как добавить Telegram? В списке сообществ его нет

---

**2026-03-19T16:03:59 | S V**
Прошу поправить если не верно понимаю рекомендацию.  1.Установка "скрипт 5 "не обязательна, если пойти, в порядке предпочтения, рассматривать в приоритете  zeroblock. 2. Установка  "скрипта 5"   не противоречит и допускает применение zeroblock в дальнеешем без конфликтов. 3. "Скрипт 5" предпочтителен во всех отношения, так  облегчает дальнейшую установку zeroblock и других пакетов..

---

**2026-03-19T16:06:05 | Anna Bagler**
Нет, скрипт 5 помогает с подкопом, zeroblock сам по себе, вместе они конфликтуют. Или Zeroblock, или скрипт №5.

---

**2026-03-19T16:33:38 | S V**
Принято, благодарю! Еще немного позвольте уточнить: 1. из ранних  постов была рекомендация, что zeroblock предпочтительнее установки "скрипта 5".  Это в целях минимизации возможных ошибок не опытного пользователя, а  полный пакет более  надёжен, хоть и в настройках сложнее.  2. Два блока "скрипт 5" в связке с подкоп,  и zeroblok функционально выполняют  однотипные задачи. Следовательно в роутере должен быть пакет загружен   одного или другого. Как разработчики отдаете предпочтение  пакету zeroblok, но и облегчаете жизнь соответственно простым пользователям. 👍

---

**2026-03-19T16:40:22 | Anna Bagler**
Просто zeroblock - разработка от РР, т.е. помощь будет более оперативной. Podkop - разработка itdog, скрипт 5 создан РР для упрощения манипуляций по установке подкопа. По функционалу они похожи, zero может то, с чем в подкопе надо ещё позаморачиваться.

---

**2026-03-19T17:05:02 | S V**
Спасибо! Принято. Работаем в направлении zeroblock

---

**2026-03-19T17:37:51 | Anna Bagler**
Если вы можете их вытянуть через поделиться из happ, то да. Подпиской пробовали в zeroblock?

---

**2026-03-19T17:51:32 | S V**
Какие обязательные действия  необхдимо выполнить на роутере  до скачивания пакета zeroblock? Роутер свежий.  Без каких либо изменений. 2. Загружаем пакеты по ссылке на рекомендации - мануал.

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

**2026-03-19T20:06:43 | er404**
Здравствуйте. Поставил zeroblock, ооооочень крутая штука, большое спасибо)

---

**2026-03-19T20:08:33 | er404**
Здравствуйте. Поставил zeroblock, ооооочень крутая штука, большое спасибо)

---

**2026-03-19T20:55:52 | Routerich**
Beta
Либо Zeroblock

---

**2026-03-19T21:15:55 | Anna Bagler**
Пробуйте через zeroblock. Или пытаться вытащить/выпросить прямые ссылки в поддерживаемом формате.

---

**2026-03-19T21:22:28 | Anna Bagler**
Если ее сможет принять zeroblock, то будет прямо подпиской, если нет, надо будет вытягивать ссылки.

---

**2026-03-19T21:38:35 | Bullet for my valentine Poison**
Z - Zeroblock

---

**2026-03-19T21:45:54 | Serge**
Приветствую! В общем двойной NAT и прочие прелести статической маршрутизации принудили перевести Gpon в мост и поднять сессию, и это оказалось не сложно. Накатить zeroblock скриптом так тем более (низкий поклон). С tailscale поигрался, но хочу все таки поднять awg на роутере. Ткните носом, пож, в мануал.
Мерси боку

---

**2026-03-19T21:55:39 | Routerich**
Здравствуйте.
Попробуйте стопнуть zeroblock и проверить

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

**2026-03-19T23:56:36 | ᚢᚹᛟᛈᛠᛋᛠᛊ ᛖᛊᚺᚱ**
С zeroblock будет лучше работать тг?

---

**2026-03-20T00:01:10 | ᚢᚹᛟᛈᛠᛋᛠᛊ ᛖᛊᚺᚱ**
Как будто без разницы, как я понял zeroblock использует zapret

---

**2026-03-20T00:33:52 | Роман**
Куда проще? Как объяснить поддержку xhttp? Zeroblock (да и вообще ковыряние в openwrt) подразумевает наличие хоть каких-то знаний. И если человек спрашивает о различиях - подразумевается что он хоть как-то освоил (либо хоть чуть-чуть вник) в работу обходов. Нет - не надо оно ему, гугл в помощь или в ВК с maxом. Блокировка не первый день существует и вводятся, было как минимум полгода что-бы хоть чему-то научится.

---

**2026-03-20T07:43:31 | Anna Bagler**
Осуществляет, но на бесплатное всегда нагрузка очень большая, лучше иметь свое. И смотрите сразу в сторону zeroblock.

---

**2026-03-20T08:39:09 | Routerich**
Здравствуйте.
Покажите диагностику Zeroblock

---

**2026-03-20T09:12:05 | S V**
И так подготовил пакет.  Согласно инструкции  установил оба файла.  В пукте 6. " .... проставляем галки на пунктах: 1,2,3,4,6,7. Жмем по очереди на кнопки: сохранить и применить. Возможно не совсем правильно понял : выполнил поэтапно каждый пункт. 6. и 7. Прогружаться отказались. Ссылка на ошибку.  В службе появились: Zeroblock и  Zapret 2.  После установки  галочки    пропали со всем пунктов. Скрины. сечас подготовлю и вышлю.

---

**2026-03-20T10:04:15 | Garsia**
У меня в принципе через ZeroBlock Телеграм не работает (пробовал добавлять и в Opera, и в AWG10). Через любой ВПН или встроенный прокси - отлично.

---

**2026-03-20T10:19:42 | Роман**
Здравствуйте. Для вас лучше на чистый роутер. Схема podkop/zeroblock на одном устройстве для опытных пользователей.

---

**2026-03-20T11:37:24 | Lelik**
Всем привет. А есть возможность в zeroblock устраивать цепочки проксей/впн, как в xray клиентах, например в троне?
https://github.com/throneproj/Throne

---

**2026-03-20T11:51:09 | Роман**
После пары дней мучения, нашел способ завести войсчат и проксимити чат в ARC Raiders и APEX Legends. Для этого вставьте в podkop /zeroblock следующие подсети

18.128.0.0/9
13.48.0.0/13
13.24.0.0/13
13.56.0.0/14
13.32.0.0/12
18.128.0.0/9
18.64.0.0/10
8.0.0.0/13
8.8.0.0/22

так же желательно добавить данные домены 
voice-eu1.embark.io
aws-voice-region.amazonaws.com
vivox.com
agora.io
ip.fish
turn.rtcp.on.epicgames.com
turn-eun1.rtcp.on.epicgames.com
turn-euc1.rtcp.on.epicgames.com
rtcp.on.epicgames.com
signaling-service-prod.eun1.live.rtcp.on.epicgames.com
signaling-service-prod.euc1.live.rtcp.on.epicgames.com
signaling-service-prod.use1a.live.rtcp.on.epicgames.com
eos-gateway-prod.ak.epicgames.com
api.epicgames.dev
game.hosting.epicgames.dev
videodelivery.net
cloudflarestream.com
cfargotunnel.com
argotunnel.com


18.128.0.0/9
13.48.0.0/13
13.24.0.0/13
13.56.0.0/14
13.32.0.0/12
18.128.0.0/9
18.64.0.0/10
8.0.0.0/13
8.8.0.0/22
34.4.16.0/20
34.4.32.0/19
34.4.64.0/19
34.4.96.0/22
34.4.128.0/18
34.6.0.0/15
34.8.0.0/13
34.16.0.0/12
34.32.0.0/11
34.64.0.0/10
34.128.0.0/10
35.184.0.0/13
35.192.0.0/14
35.196.0.0/15
35.198.0.0/16
35.199.0.0/17
35.199.128.0/18
35.200.0.0/13
35.208.0.0/12
35.224.0.0/12
35.240.0.0/13
136.107.0.0/16
136.108.0.0/14
136.112.0.0/13

Это допустим решение для войс чата.

---

**2026-03-20T12:17:35 | Борис**
Только если руками создать цепочку route-outbound-inbound в папке  /etc/zeroblock/sing-box.d

---

**2026-03-20T12:46:43 | Anna Bagler**
wiki, Инструкция по прошивке для самых маленьких, потом тема zeroblock beta или интернет без границ.

---

**2026-03-20T13:33:05 | Vasilii Pavlenko**
выключить? или как убрать? STDERR:undefined
Package list missing or not up-to-date, generating it.

Building package index...
Downloading file:/local-repos/24.10.5/core/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/routerich_core
Downloading file:/local-repos/24.10.5/base/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/routerich_base
Downloading file:/local-repos/24.10.5/routerich/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/routerich
Downloading file:/local-repos/24.10.5/openwrt/base/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/openwrt_base
Downloading file:/local-repos/24.10.5/openwrt/luci/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/openwrt_luci
Downloading file:/local-repos/24.10.5/openwrt/packages/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/openwrt_packages
Downloading file:/local-repos/24.10.5/openwrt/routing/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/openwrt_routing
Downloading file:/local-repos/24.10.5/openwrt/telephony/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/openwrt_telephony
Downloading file:packages/Packages
Updated list of available packages in /builder/build_dir/target-aarch64_cortex-a53_musl/root-mediatek/../../../../builder/dl/imagebuilder
Collected errors:
 * opkg_install_cmd: Cannot install package luci-app-zeroblock.
make[2]: *** [Makefile:234: package_install] Error 255
make[1]: *** [Makefile:171: _call_manifest] Error 2
make: *** [Makefile:349: manifest] Error 2

Traceback (most recent call last):
  File "/usr/local/lib/python3.12/site-packages/rq/worker.py", line 1659, in perform_job
    return_value = job.perform()
                   ^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/rq/job.py", line 1318, in perform
    self._result = self._execute()
                   ^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/rq/job.py", line 1376, in _execute
    result = self.func(*self.args, **self.kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/asu/build.py", line 63, in build
    return _build_internal(build_request, job, request_hash, build_start, bin_dir)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/asu/build.py", line 504, in _build_internal
    report_error(job, "Impossible package selection")
  File "/app/asu/util.py", line 302, in report_error
    raise RuntimeError(msg)
RuntimeError: Impossible package selection

---

**2026-03-20T13:45:00 | Vasilii Pavlenko**
все, понял, luci_app_zeroblock...

---

**2026-03-20T14:30:34 | Lelik**
Не только, хочу под 0 прошится, и снова zeroblock попробовать

---

**2026-03-20T15:19:26 | Борис**
К сожалению сейчас попал в такую ситуацию. Всё настроил, всё работает и не приходится ничего делать. А эти блокировки и белые списки - курам насмех, обходятся в два счёта. Даже скучно как-то, что оппонент в лице Регулятора оказался таким слабым. Жду новых блокировок, а пока не обновляю ни Zeroblock, ни Zapret2 - хорошее, стабильное ПО

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

**2026-03-20T16:14:25 | Gomer Simpson**
ZeroBlock. Соседняя тема. Оно умеет фсё.

---

**2026-03-20T16:17:02 | Anna Bagler**
Ветка zeroblock beta, полный мануал в закрепе и файлы, быстро -  https://t.me/routerich/394153/520562

---

**2026-03-20T16:18:53 | Routerich**
grep -rl "74.125.205" /tmp/zeroblock/rulesets/

---

**2026-03-20T16:21:25 | Egor Sorokin**
root@RouteRich3000:~# grep -rl "74.125.205" /tmp/zeroblock/rulesets/
/tmp/zeroblock/rulesets/ai_ipv4.json
root@RouteRich3000:~#

---

**2026-03-20T16:36:01 | Anna Bagler**
В закреплённом сообщении темы Zeroblock Beta есть ссылка на полный мануал и ссылка на списки.

---

**2026-03-20T16:56:08 | Владимир Ионов**
На RR поднят OpenVPN Server для доступа к ресурсам локальной сети.
ВПН-клиент нормально видит сеть...
Подскажите, а как завернуть исходящий трафик от ВПН-клиента в ZeroBlock?

---

**2026-03-20T17:27:57 | Артем Михайлов**
Вообщем моя последовательность шагов.
1.  Удалил Podkop и YouTubeUnBlock.
2. Обновил пакеты.
3. Попробовал поставить ZeroBlock - не получилось.
4. Перезапустил роутер. 
Все =))) 
Сча после ребута посмотрим.

---

**2026-03-20T18:26:43 | Anna Bagler**
Можно. Если есть навыки, то вы можете ставить zeroblock, он предпочтительнее https://t.me/routerich/394153/520562 или подкоп  https://t.me/routerich/3845/245550

---

**2026-03-20T18:28:38 | Роман**
ZeroBlock всё это имеет.

---

**2026-03-20T18:35:23 | Артем Михайлов**
Подскажите,  а ютуб через zeroblock - это обход через dpi или трафик через VPN гонится?
С условием, что мы удаляем секцию ютуба из маршрута впн (список)

---

**2026-03-20T20:10:22 | Константин**
Скажите, youtubeUnblock по умолчанию в прошивке есть? Я вроде только zeroblock ставил(со своими ссылками на vless), а он установлен.  Если youtubeUnblock удалю, ничего не испорчу?

---

**2026-03-20T20:36:36 | Алексей Пышкин**
Здраствуйте. сегодня установил zeroblock на свежую прошивку. сейчас всё работает. по началу трафик через opera не хотел идти, но это вылечил перезапуск устройства. спасибо всем причастным к разработке. завтра буду ставить на другое устройство, там проблемы с покопом, надеюсь с zeroblock никаких проблем не будет.

---

**2026-03-20T20:43:55 | Routerich**
будут, ведь все знают что podkop = zeroblock просто под другим именем

---

**2026-03-20T21:04:14 | Aydar**
привет, а надо youtubeunlock сносить перед установкой zeroblock>?

---

**2026-03-20T21:06:13 | Mstislav**
Спасибо, по ссылке была инструкция: Итак пошаговый мануал для владельцев Routerich, как завести Zeroblock+Zapret2 на дефолтных настройках.
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки"и ждем, закрываем появившуюся табличку нажав на кнопку "ОК".
3. Качаем два файла (zeroblock_*** и luci-app-***) из закрепа темы "Zeroblock" и сохраняем в папку на рабочем столе.
4. Возвращаемся в разделы Система-пакеты и жмем на кнопку "Загрузить пакет". И по очереди ставим скачанные пакеты: Zeroblock_*** а затем luci-app***.(Табличку с надписью Error игнорируем)

---

**2026-03-20T22:32:51 | Routerich**
Zeroblock

---

**2026-03-20T23:19:40 | Routerich**
По тегу #zeroblock можете посмотреть историю изменений

---

**2026-03-21T00:36:14 | Dmitry**
Только получил ещё 1 роутер….
Подскажите что на данный момент лучше ставить zapret2, zeroblock или старый добрый интернет без границ?

---

**2026-03-21T00:37:53 | Роман**
Zeroblock (но это только моё мнение).

---

**2026-03-21T10:35:57 | Святос**
Кнопка Messengers в ZeroBlock

---

**2026-03-21T11:14:50 | Константин**
Подскажите пожалуйста, стоит zeroblock и zapret, все вроде работает за исключением wats app 🤔

---

**2026-03-21T11:28:48 | HiLLL**
запустите в терминале, хуже не будет
zeroblock awg warp

---

**2026-03-21T11:33:56 | Andrey**
Сейчас установлен Скрипт-5 с Подкопом. Что бы установить ZeroBlock надо скинуть роутер к заводским настройкам сначала или достаточно "Службы - Подкоп - Диагностика - Остановить Подкоп"?

---

**2026-03-21T11:49:51 | Anna Bagler**
Старый подкоп из-за старой прошивки, обновляться без сохранения, и вновь подкоп или zeroblock.

---

**2026-03-21T11:57:09 | Роман**
Выбрать торренты в podkop/zeroblock.

---

**2026-03-21T12:37:51 | AleXXXey**
Уже попробовал по команде: 
zeroblock awgwarp

Он умирает, а в терминале ошибки лезут, мол варп не работает. 

Я могу Попробовать через warp generator у лимоникса с указанием эндпоинта.

 Но На какой сменить, например?

---

**2026-03-21T12:38:53 | Борис**
Это весёлое изображение натолкнуло меня на мысль - почему бы не сделать zeroblock на xray, ведь всё равно в большинстве случаев zb советует его установить? Мне всегда был непотянен этот момент - зачем держать на роутере две одинаковых программы (sing-box и xray-core), чтобы обслуживать zeroblock, ведь по идее, если zb неполноценен без xray, можно было бы его сразу сделать на xray, и без sing-box'а зероблок наверное легко проживёт? Я технических нюансов не знаю, может есть что-то такое в sing-box, без чего невозможно было бы сделать zeroblock?

---

**2026-03-21T12:49:18 | Alexei**
Поставил на роутор ZeroBlock - ютюбушка, дискорд, телега работают быстро (без замедления).  Вопрос - торенты трекеры всё равно не доступны - как и чем их открыть можно?

---

**2026-03-21T13:11:49 | Борис**
Благодарю) ссылка ведёт на автора Podkop, я ознакомился, концептуально осмыслил проблемы и отличия. Но ведь это аргументы именно автора Podkop, а у уважаемого автора Zeroblock точно такое же мнение? Или выбор в пользу sing-box бы обусловлен тем, чтобы "меньше пердолиться и быстрее выпустить готовый продукт, плюс есть наработки от коллеги (podkop)"? Были ли мысли перейти на xray? Всё же это позволило бы ощутимо сократить занимаемую память... Да и открыло бы (возможно) пространство для творчества, т.к. сейчас зб как бы ограничен возможностями sing-box и протоптанной дорожкой автора Podkopa, или я не прав и все эти "возможности для творчества" лишь иллюзорны и в сущности дадут только лишний гемор и принципиально ничего нового? 

Лично моё мнение, что устанавливать целый комбайн xray ради пары специфических конфигов - выглядит как костыль, и так будто бы не должно быть. Я иногда думал об этом перед сном, но стеснялся задать такой вопрос, потому что ожидаемо в ответ можно получить что-то в духе "ну сделай тогда сам если такой умный" 🤔

---

**2026-03-21T13:18:32 | Роман**
Это про установку zeroblock. Про списки там ни слова.

---

**2026-03-21T13:19:18 | Роман**
Какие списки вы хотите внести в zeroblock?

---

**2026-03-21T13:29:10 | Artem**
Подскажите пожалуйста по chatgpt, в zeroblock в списке прокси стоит ai , но всё равно вылазит ошибка что не доступен в вашем регионе. Может есть ещё какие то списки/настройки и тд...?

---

**2026-03-21T13:30:05 | Anna Bagler**
Нет, показывайте диагностику zeroblock.

---

**2026-03-21T13:40:25 | Artem**
reset роутера всмысле? И накатить по новой zeroblock без podkop?

---

**2026-03-21T13:44:27 | Anna Bagler**
Zeroblock.

---

**2026-03-21T13:58:12 | Routerich**
/etc/config/zeroblock

---

**2026-03-21T14:22:43 | Anna Bagler**
Секция proxy zeroblock, там выбираете списки, которым нужен зарубежный IP.

---

**2026-03-21T14:23:03 | Artem**
Хотя нет, залогиниться всё равно не выходит. Попробую тогда ещё раз, podkop наоборот, вместо zeroblock...

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

**2026-03-21T15:02:43 | Евгений**
Ребятки, всем здарова! Есть смысл менять podkop на zeroblock ? Я так понимаю эту программы в роутере для обхода блокировок. Я просто нуб в этом деле. Мне нужно что бы ютуб , телега да инста работали. Сейчас podkop стоит. В целом все работает но иногда тормозит. Перезагрузка помогает пока что.

---

**2026-03-21T15:42:17 | Роман**
Свои (покупные) сервера с различными панелями, vless, amneziaWG - с последующей интеграцией в podkop/zeroblock.

---

**2026-03-21T16:32:43 | Anna Bagler**
Ставьте zeroblock, все равно сбрасывали.

---

**2026-03-21T16:37:17 | MVLD**
Лучше zeroblock?

---

**2026-03-21T18:10:01 | Alexander Martyanov**
В zeroblock r56 по кнопке открыть yacd в десктопном браузере не открывается: The requested URL /clash-api/ui/?hostname=192.168.1.1&port=9090&secret= was not found on this server. В телефоне нормально. Вручную если ссылку открыть http://192.168.1.1:9090/ui/?hostname=192.168.1.1&port=9090&secret=32aa19af0cd0196456131318a55b8e3d то нормально работает.

---

**2026-03-21T18:16:45 | Валерий**
Благодарю, зероблок сработал. Бета версия подкоп не поставилась. Еще вопрос, Tailscale VPN настроить доступ через Zeroblock можно?

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

**2026-03-21T18:49:53 | Валерий**
У меня аналогичная проблема была. Ставь Zeroblock по гайду из соответствующей темы

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

**2026-03-21T20:45:27 | Виталий**
Здравствуйте, подскажите пожалуйста такой момент. Возможно ли сделать для zeroblock доступ из вне к проксе с логин паролем? Для тг.

---

**2026-03-21T20:50:05 | Виталий**
Взамен zeroblock?

---

**2026-03-21T20:50:24 | Routerich**
нет, внутри zeroblock

---

**2026-03-21T21:43:05 | Андрей**
Привет! Помогите продиагностировать проблему, плиз. В zeroblock работают комьюнити списки, но не работают пользовательские списки доменов. До этого стоял podkop, было точно такое же поведение.

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

**2026-03-21T22:01:52 | Борис**
Как вам идея сделать редирект/кастомное сообщение об ошибке, когда используется секция в Zeroblock, но при этом сервер для обхода недоступен? 

Что я имею виду: иногда люди пишут, что "у меня включена секция, но я вижу свой Российский ip" - значит, ZB отказался от использования сервера из секции и принудительно сделал вывод трафика в direct (с обычного Российского ip).

Что предлагается сделать: в браузере выдаётся html страница "Секция zeroblock не работает" (по принципу того, как провайдер может перехватить http-запрос и подсунуть другую страницу, например о том, что ресурс заблокирован)

Какую проблему это решает: не допускает ситуаций, когда у пользователя "слетела маска 👺", а он об этом даже не в курсе и продолжает делать противоправные действия в интернете со своего настоящего IP (что может приводить к плачевным последствиям). К тому же, это ускоряет поиск неисправности, ведь человек сразу видит "ага, мой сервер перестал работать. Пойду отключу zb или сменю сервер". Указанная опция включается пользователем по желанию и по умолчанию выключена

---

**2026-03-21T22:51:33 | Борис**
Я сейчас посмотрел, у меня в zeroblock зашито поведение "final": "direct-out". Так почему fallback не будет? Он как раз есть, просто идёт в direct как раз, а предлагаемая мною Опция™ меняла бы direct-out на outbound-заглушку, которая срабатывает, если сервера погибли... (Там у нас html страница с ошибкой, что маскировка отключена, недостаточно маны)

---

**2026-03-21T22:59:50 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.2-r4:
  Изменения:
  - Красная рамка, когда задержка n/a
  
  fix: несколько тегов для исключений 
#ZeroBlock

---

**2026-03-21T23:10:35 | Sergey G**
Подскажите, действительно ли данные настройки могут блокировать какую-то рекламу?
кажется это добавляет podkop (это на роутер с 24.10.2), при выполнении скрипта 5/beta

после установки zeroblock (на роутере с 24.10.5), тут появляется единственная настройка
у нее аналогичная задача или нужно дополнять настройки в данной секции?

---

**2026-03-21T23:17:57 | ꧁ 𝓐𝓷𝓽𝓸𝓷 𝓑𝓮𝔃𝓴𝓪𝓹𝓾𝓼𝓽𝓲𝓷 ꧂**
Итак, первый баг репорт на версию 0.7.2-r3 касательно фичи "not-add":

В целом вроде работает - мои конфиги not-add-inbounds.json и not-add-route.json из /etc/zeroblock/sing-box.d/ скопированы в /tmp/zeroblock/sing-box.d как 50-custom-not-add-inbounds.json и 50-custom-not-add-route.json в /tmp/zeroblock/sing-box.d

Судя по netstat порт кастомного inbound поднят (тобишь всё фурычит)

В 40-route.json кастомный inbound не фигурирует (как того и хотелось)

В Luci в службе ЗБ в "Диагностика"->"Показать конфиг" вкладка "Custom" соответствует реальности.

Однако, кнопка "Копировать" выдаёт конфиг без всех моих секций, прописанных в not-add-inbounds.json и not-add-route.json!

Баг не критический, но многих может ввести в заблуждение и депрессию...

---

**2026-03-21T23:19:27 | Sergey G**
спс, похоже на то что эти настройки внесены вручную
для совместной работы с youtubeUnblock (с первого знакомства с роутером)
лень перепроверять что туда пропишет установка 5 скрипта/beta,т.к. решил остановить свой выбор на zeroblock

---

**2026-03-21T23:25:17 | Sergey G**
8. Возвращаемся в Zeroblock, открываем вкладку Автонастройка и убираем галки с 6 и 7 пункта.(Автозагрузка) Иначе мы не сможем вносить изменения в секциях со списками. Сохранить, применить.
Подскажите, в этой части гайда описано что нужно отжимать галки? Это все еще надо делать?
И что имеется ввиду вносить изменения в секциях - состав внутри секций изменять?
Или добавлять свои секции новые нельзя будет?

---

**2026-03-21T23:43:53 | Роман**
Конечно. Покупаете vps с ip нужной страны, поднимаете нужную панель, настраиваете, закидываете ссылку в zeroblock/podkop.

---

**2026-03-21T23:46:51 | Роман**
А у вас твич через запрет? Мне кажется в zeroblock у вас выбран список геоблок, не так ли?

---

**2026-03-21T23:49:54 | Alexey Zh**
понял) нет, должен быть не через запрет, в zeroblock - opera - список пользовательских доменов,

---

**2026-03-22T00:07:12 | Routerich**
Это нормально, так как им управляет Podkop/zeroblock

---

**2026-03-22T00:57:13 | Борис**
Тут противоречия никакого нет. Этот пакет я ставил по молодости в конце 2025 в надежде, что там будет интерфейс luci, через который я смогу настроить xray как сервер (и подключаться к роутеру с телефона по LTE). Но всё оказалось так, как я написал - замороченный, причудливый интерфейс. В нём было что угодно, кроме банальных самых простых вещей (даже для клиента) - чтобы можно было ввести ip сервера, uuid, транспорт и так далее. Потом я его снёс и просто поставил xray-core из репозитория RR. И уже эту консольную утилиту я освоил и через неё поднял свой сервер (там несложно, просто редактировать тот же config.json). А потом я узнал про zeroblock, скачал его, свой сервер с xray переделал на sing-box, а сам xray удалил... И вот сейчас я пользуюсь только синг боксом (а зероблок предлагает дополнительно скачать xray размером в 25 мегабайт, чтобы добавилось пару функций). Собственно поэтому и началось моё сегодняшнее обсуждение - почему бы сразу зероблок не сделать на xray, вроде как программы с sing-box одинаковые, отличается синтаксис конфига и может быть какие-то подходы...

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

**2026-03-22T01:19:04 | Борис**
Ну подписки - это не беда. Можно же их по крону качать через указанный url и вставлять в config.outbound раз в период. Если был намёк на то, что в Zeroblock это уже всё есть и он в тыщу раз круче, то конечно, так и есть... Там пердолинга меньше и интерфейс уже присутствует. Ну при желании можно и подписки реализовать на xray описанным мною способом (если концептуально рассматривать переезд zb на xray)

---

**2026-03-22T01:20:55 | A̴͂ ̖͔͎͍͔̮̌̾̈̓̇̅͗̓̒̌̉̀̕͠͝ ̧̙͕̬̦̩̞ͅͅv̸̡̡̬̬͔͕̰̖̻̄́̎̽ͅř̸̆̓͛̉̋̈́̔̔̔͂**
Да, на xiaomi качает без проблем

Пробовал разные комбинации настроек на случай если это баг

Пробовал отключить Zapret, Zeroblock - безрезультатно

FakeIP тоже отключал в специальной секции eth0 WAN для консоли

Где сохраняется этот отчет test_config_script_nightly ? В root файла analyzer.log нет

---

**2026-03-22T01:22:27 | Борис**
В моём розовом мире предполагается, что разработчик Zeroblock™ примет волевое решение и СДЕЛАЕТ это сам, через какой-нибудь python или php, который будет внутри curl вызывать, скачивать txt с подписками, парсить url, превращать в надлежащий json и мержить в config.json 😊

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

**2026-03-22T06:40:47 | Dark Ghost**
Вообще-то, никаких голубей, а zeroblock - так, для души...

---

**2026-03-22T09:26:47 | Anna Bagler**
Используйте запрет/запрет2 + стратегии, если вам только yt нужен, или ещё zeroblock добавляйте или podkop.

---

**2026-03-22T09:29:39 | Андрей**
Я понимаю, zeroblock стоит, я хочу в корне проблемы разобраться, почему только на android приложении не работает YouTube

---

**2026-03-22T09:46:18 | Владимир Волков**
Подкоп - тема "Интернет без границ"
Зероблок - тема "Zeroblock Beta"

---

**2026-03-22T09:47:02 | Роман**
Если вы хотите использовать запрет для обхода блокировки ТГ - никак. 
Для остального есть zeroblock в соответствующей теме.

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

**2026-03-22T11:57:57 | Anna Bagler**
Закрепы этой темы или тема Beta. Или переходите на zeroblock.

---

**2026-03-22T11:59:41 | S V**
Анализ запущен: 2026-03-22 09:13:10 Лог сохраняется в: /root/analyzer.log -------------------------------------------------------------- Попытка обновления списка пакетов: (1/2) Списки обновлены успешно Installing wget-ssl (1.24.5-r1) to root... Downloading https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages/wget-ssl_1.24.5-r1_aarch64_cortex-a53.ipk Package curl (8.12.1-r1) installed in root is up to date. Configuring wget-ssl. = ПРОВЕРКА DNS (Прошивка: 24.10.5): DNS Server: 127.0.0.1:53 | DNS Redirect: 127.0.0.1#5359 Facebook IP: 198.18.4.15 | YouTube IP: 108.177.14.93 = ИНТЕРФЕЙС awg10 (ДЕТАЛИ): Статус : UP (ON) ↓10.69 MB / ↑0.21 MB Пинг (ya.ru via awg10): 10.882 / 12.208 ms (0 из 10 потеряно) Программы в автозапуске: zeroblock zapret2 opera-proxy = ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM): OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK) awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3] awg10 (IPv6) : ОФЛАЙН Запускаем остановленные службы, ожидайте... = СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ): zeroblock | RUNNING | РАЗРЕШЁН sing-box | RUNNING (MANAGED BY ZB) | ОТКЛ zapret2 | RUNNING | РАЗРЕШЁН opera-proxy | RUNNING | РАЗРЕШЁН = ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ: zeroblock awg10 (vpn): anime,discord,googleplay,messengers,meta,news,porn,socials,video zeroblock opera (prx out): ai,geoblock Версия zeroblock: 0.7.1-r53 zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8 = СИСТЕМНЫЕ РЕСУРСЫ: LAN IP: 192.168.1.1 (Прошивка: 24.10.5) CPU: 0.30 | RAM: 23% | NAND: 50% занято / 34.1M доступно # ZeroBlock Monitor 0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1 # ZeroBlock Lists Update 0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1 root@RouteRich:~#

---

**2026-03-22T11:59:58 | Anna Bagler**
Полный мануал в теме zeroblock beta, только ставить пока файлами.

---

**2026-03-22T13:22:19 | Anna Bagler**
Посмотрите Секции на сайте podkop.net, чтоб понимать общие принципы. Полный мануал по zeroblock изучите.

---

**2026-03-22T13:47:10 | Alex Korshun**
Как будто что-то из установленного переехало в системное. 
Раньше zapret2+zeroblock занимали ±22мб памяти.

---

**2026-03-22T13:59:02 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.2-r10:
  Изменения:
  - Множественные подписки.
  Теперь в одной секции можно указать несколько URL подписок. Прокси из всех подписок объединяются, теги извлекаются из всех. В LuCI поле Subscription URL заменено на DynamicList — добавляйте URL по одному.
  - Per-section Device Model / Device OS.
  Новые поля в Advanced для subscription секций: Device Model и Device OS. Переопределяют заголовки x-device-model и x-device-os при загрузке подписок. Если не указаны — определяются автоматически из системы (модель роутера и версия OpenWrt).

  Исправления
  - Fix: Show Config Copy/Download теперь включает custom config файлы (50-*)
  - Fix: Сжатые подписки разбираются вручную, потому что системный curl не умеет в сжатие
  - Лимит прокси на одну подписку снижен до 100 (было 150), общий лимит на секцию — 500
  - [clash_api] /proxies failed: Error перемещена в debug
#ZeroBlock

---

**2026-03-22T14:08:52 | Anna Bagler**
Анблок отключайте. Ставьте связку zeroblock + zapret2.

---

**2026-03-22T14:15:45 | Stepan**
Добрый день, начал настраивать по этой инструкции, дошел до 7 пункта, за 30 минут zapret2 в службах так и не появился, но при этом все сервисы вроде как работают. Можете пожалуйста объяснить, зачем нужен еще и zapret2? И чем чревато оставить все как есть, то есть маршрутизацию чисто через zeroblock?

---

**2026-03-22T14:17:41 | Anna Bagler**
Обновлять прошивку до актуальной и запускать скрипт ещё раз или zeroblock + zapret2.

---

**2026-03-22T14:26:22 | Борис Диденко**
Добрый день! Стоит подкоп, хочу поставить zeroblock. Нужно роутер до заводских сбрасывать?

---

**2026-03-22T15:46:25 | Роман**
Согласен. Приобретайте VPS, накатывайте x3ui, ссылку в zeroblock - будет одна рабочая секция. А то чей-то, бесплатно дали - да ещё и разбираться нужно! Негодяи.

---

**2026-03-22T16:10:49 | Борис Диденко**
А где можно почитать про добавление своего конфига amneziawg в zeroblock? Никак найти не могу про это информацию

---

**2026-03-22T16:13:45 | Sergey**
чтобы обновить зероблок надо откатывать роутер к чистому или прямо поверх старого zeroblock_0.6.4-r46_aarch64_cortex-a53 и luci-app-zeroblock_0.6.4-r46_all можно ставить?

---

**2026-03-22T16:17:15 | ZЁма**
Установка ZB с нуля:


1. Если до этого стоял podkop, то создайте резервную копию настроек.
1. Прошиваем RR без сохранения настроек прошивкой 24.10.5 в соответствии с версией USB: USB2.0-белый, USB3.0-синий. Или делаем сброс на заводские настройки.
2. Переходим в "Система" -> "Пакеты" -> "Действия" и прожимаем кнопку "Обновить списки...". Если были ошибки, то повторяем процедуру еще раз.
3. В окне "Фильтр" вводим "you" и во вкладке "Установлено" видим пакет "youtubeUnblock" и удаляем его. Также можно остановить и отключить его в "Система" -> "Автозапуск".
4. В окне "Фильтр" вводим "awg" и во вкладке "Обновления" видим два пакета для обновления и обновляем их, это для установки конфигурации awg2.0.
5. Желательно выполнить обновление прошивки ASU-обновление.
6. Перезагружаем RR.
7. Заходим в RR через окно Инкогнито.
8. Переходим в "Система" -> "Пакеты" -> "Действия" и прожимаем кнопку "Загрузить пакет..." и устанавливаем последний ZB, сначала сам zeroblock, а потом luci-app-zeroblock.

Далее VLESS и AWG2.0

---

**2026-03-22T16:39:27 | Anna Bagler**
В awg в zeroblock, в мессенджерах.

---

**2026-03-22T16:45:28 | Anna Bagler**
Из секции awg в zeroblock убираете список messengers. Сохраняете, применяете. Добавляете этот список в proxy. Авторизуетесь. Потом возвращаете все назад, если важны звонки.

---

**2026-03-22T16:47:15 | Виталий**
Кто нибудь сталкивался с тем что после установки zeroblock в браузере на телефоне ютуб работает а в приложении нет?

---

**2026-03-22T17:29:58 | Роман**
Смотря какие у вас блокировки. По возрастающей - запрет2, запрет 1 с перебором стратегий, Zeroblock.
Если не работает youtubeunblock - отключить его.

---

**2026-03-22T17:30:17 | Fredd**
Темы слева- Wiki,Интернет без границ,Zeroblock Beta и так далее.Осваивайтесь в чатах,там есть всё что нужно.В шапках всё самое важное

---

**2026-03-22T17:33:07 | Виталий**
Анализ запущен: 2026-03-22 17:31:20
Лог сохраняется в: /root/analyzer.log
--------------------------------------------------------------
= ПРОВЕРКА DNS  (Прошивка: 24.10.5):
  DNS Server:   1.1.1.1:53 | DNS Redirect: 127.0.0.1#5359
  Facebook IP:  UNKNOWN | YouTube IP:  UNKNOWN
= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.68 MB / ↑0.23 MB
  Пинг (ya.ru via awg10): 84.873 / 91.860 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock opera-proxy
= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.2]
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы, ожидайте...
= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock     DadiaVania (prx url): ai,anime,art,block,geoblock,discord,games,googleplay,messengers,meta,music,news,porn,repo,shop,socials,tools,torrent,video,youtube,cdn_akamai,cdn_aws,cdn_azure,cdn_bunny,cdn_cdn77,!_cdn_cloudflare,cdn_digitalocean,cdn_fastly,cdn_gcore,cdn_github,cdn_google,cdn_hetzner,cdn_linode,cdn_oracle,cdn_ovh,cdn_scaleway,cdn_selectel,cdn_vultr
  Версия zeroblock: 0.7.1-r56
  zeroblock DNS/Bootstrap DNS: (doh) 9.9.9.9 / 9.9.9.9
= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.0.1 (Прошивка: 24.10.5)
  CPU: 1.63 | RAM: 27% | NAND: 43% занято / 38.6M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  0 * * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1
root@RouteRich:~#

---

**2026-03-22T17:58:08 | Виталий**
root@RouteRich:~# uci show |grep route
firewall.@rule[5].icmp_type='echo-request' 'echo-reply' 'destination-unreachable' 'packet-too-big' 'time-exceeded' 'bad-header' 'unknown-header-type' 'router-solicitation' 'neighbour-solicitation' 'router-advertisement' 'neighbour-advertisement'
fstab.@mount[2].target='/mnt/router'
luci.main.mediaurlbase='/luci-static/routerich'
luci.themes.Routerich='/luci-static/routerich'
luci.diag.route='openwrt.org'
network.awg10.nohostroute='1'
openvpn_recipes.server_tun_ptp._description='Simple server configuration for a routed point-to-point VPN'
openvpn_recipes.client_tun_ptp._description='Simple client configuration for a routed point-to-point VPN'
openvpn_recipes.server_tun._description='Server configuration for a routed multi-client VPN'
openvpn_recipes.client_tun._description='Client configuration for a routed multi-client VPN'
tailscale.settings.accept_routes='0'
tailscale.settings.login_server='https://rc.routerich.ru/'
tailscale.settings.advertise_routes='192.168.0.0/24'
zeroblock.settings.proxy_router_traffic='0'
root@RouteRich:~#

---

**2026-03-22T18:00:53 | Виталий**
dhcp.@dnsmasq[0].noresolv='1'
dns-failsafe-proxy.main.zeroblock_noresolv_backup='1'

---

**2026-03-22T18:13:14 | Dmitry**
Поставил zeroblock. Я правильно понимаю что свои домены надо вносить в zapret2 - списки - user ?

---

**2026-03-22T18:44:03 | HiLLL**
в терминале напишите
service zeroblock stop

---

**2026-03-22T19:17:28 | Kiss_My_Axe**
Фейкайпи отрабатывает, значит, скорее всего, запросы к гроку идут "через подкоп".
Видимо доменов каких-то не хватает в AI-списке.
Рекомендую стопнуть и отключить подкоп.
Затем установить ZeroBlock. У меня на нём проблемы не наблюдаются (только что открыл грок без вопросов).

---

**2026-03-22T19:19:02 | Anna Bagler**
Если есть навыки, то вы можете ставить zeroblock, он предпочтительнее https://t.me/routerich/394153/520562 или подкоп  https://t.me/routerich/3845/245550

---

**2026-03-22T19:24:00 | Макс**
ZeroBlock получше подкопа будет получается? Я просто пробовал вчера ставить и на пункте с "галки на пунктах: 1,2,3,4,6,7 проставить" некоторые пункты были неактивируемые. Из за установленного запрета2 видимо, да? Вроде 1,2,3 не нажимались

---

**2026-03-22T19:25:26 | Andrey**
похоже пора пробовать zeroblock

---

**2026-03-22T19:50:58 | Khamzat**
Всем доброго времени суток!
Сегодня занимался перекатом с podkop на zeroblock: обновил прошивку до 24.10.5 на роутере файлом из соответствующего раздела группы, выполнил первичные настройки, поставил в нужном порядке 2 файла zeroblock из закрепа и следовал в целом инструкции, но столкнулся с тем, что интерфейс awg не хочет создаваться, что и отражено в логах в приложенном файле

Видел, что в топике тут у некоторых людей такая же проблема возникла. Решения для этой проблемы пока нет?

---

**2026-03-22T19:54:32 | ARTEM**
При поиске стратегий zeroblock отключается ? Или обязательно вручную отключать ?

---

**2026-03-22T20:27:55 | ARTEM**
Хочу сделать новую стратегию через zapret2 finder , так как что в шапке стратегия что в rr-youtube, когда захожу на ютуб долго прогружается превьюшки а через awg в zeroblock пускать не хочу потому что 4к лагать начинает
--
Вот щяс вставил домены ютуба и убрал sni prob и все в blocked упали
Как правильно запустить finder чтобы найти стратегию только для ютуба ?

---

**2026-03-22T20:51:21 | Khamzat**
во вкладке diagnostics надо прожать?
не нахожу
до этого сделал рестарт zeroblock после смены уровня логирования на trace, потом diagnostics -> logs -> download

---

**2026-03-22T21:01:26 | Routerich**
попробуйте
zeroblock awg warp

---

**2026-03-22T21:51:24 | V1r00z**
Sun Mar 22 21:49:35 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Sun Mar 22 21:49:39 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock(0.7.1-r53)...
[clash_api] /proxies failed: Error
[clash_api] /proxies failed: Error
[clash_api] /proxies failed: Error
[config_builder] xray-core not found at /usr/bin/xray, xray proxies will be skipped
[singbox_gen] Section erevan: proxy requires xray-core (transport=xhttp), skipping
[zeroblock] ZeroBlock started successfully

---

**2026-03-22T22:59:49 | 🆂🅷🅾🅳🅸🅼🅰🆂🆃🅴🆁**
дело в том что она и не работала на zeroblock+zapret с чистого роутера. Но если скрипт номер 5 поверх вкорячить то работает. FakeIP постоянно красный крестих без подкопа

---

**2026-03-22T23:21:21 | Игорь**
А WatchDoc уже не нужен, если ZeroBlock стоит?

---

**2026-03-23T01:13:40 | Garsia**
Всем привет! 
Обратил внимание, что самые известные standalone клиенты Opera Proxy (в том числе от Snawoot) исчезли с Гитхаба. У меня теперь открывается страница 404 там, где они были.

Интересно, почему? И не скажется ли это на работе нашего любимого ZeroBlock?

---

**2026-03-23T09:09:07 | Anna Bagler**
Zeroblock или скрипт №5 использовали?

---

**2026-03-23T09:56:23 | Руслан**
Здравствуйте! Скажите, а нужно ли после установки на чистый RR ZeroBlock+Zapret2 скрипт №5 или Бета?

---

**2026-03-23T10:46:28 | HiLLL**
ну на крайний случай запустите в терминале
zeroblock awg warp

---

**2026-03-23T10:52:30 | Emir Otarjaur**
Добрый день подскажите пожалуйста. Решил обновить до последней версии. Все по схеме обновил пакеты , установил зероблок, но на этапе обновления luci-app-zeroblock выдает ошибку.

---

**2026-03-23T10:54:20 | воппер уполномоченный**
luci-app-zeroblock-0.7.2-r10.apk 
apk формат разве устанавливается на эту версию openwrt?

---

**2026-03-23T11:08:34 | Anna Bagler**
Zeroblock+zapret2 лучше. Подкоп скриптом, если с навыками все плохо.
https://t.me/routerich/394153/520562

---

**2026-03-23T11:15:27 | Anna Bagler**
Разные вещи. Zeroblock - точечная маршрутизация. Zapret - дурилка, как написали выше.

---

**2026-03-23T11:24:01 | Anna Bagler**
Zeroblock.

---

**2026-03-23T11:30:39 | Nick**
Вновь напишу пару добрых слов.
Роутер изначально покупался на дачу для тутуба. Что бы ребенок понимал, кто в доме хозяин и кто вправе разрешать или запрещать что либо. Понятно, что таким человеком в семье должен быть папа, а не дедок из телевизора. 
Второй задачей было видеонаблюдение.
Третьей - управление зачатками умного дома на esp32.
С первыми двумя задачами справлялись. Начали с предустановленного по, потом, по мере закручивания вентиля, симметрично ответили установкой запрета. 
Все бы нормально было, но перестал работать, недели три назад, бот в телеге, с которого управлялась esp.
Команды проходили но пинами espшка не дрыгала.
Все перепробовал, результат нулевой. 
Поставил zeroblock и наступило блгорастворение воздухов. Не знаю как, но зашуршало все как прежде!
Нет слов, шаманы какие то эти авторы. 
Спасибо ещё раз всем причастным!

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

**2026-03-23T13:01:57 | OnixKid**
так хорошо, это решил. настроил так же точку выхзода с проксированием трафика через zeroblock но на телефоне не хочет например в ютуб заходить =(

---

**2026-03-23T13:06:04 | OnixKid**
ИНФОРМАЦИЯ О TAILSCALE:
  Версия: 1.94.2          | Статус: RUNNING | Автозапуск: РАЗРЕШЁН

= АНАЛИЗ КОНФИГУРАЦИИ /etc/config/tailscale:

1. ОБЯЗАТЕЛЬНЫЕ ПАРАМЕТРЫ:
  [OK]   enabled                        | 1 [галочка "Включить"]
  [OK]   accept_dns                     | 0 [галочка "Принимать DNS"]
  [OK]   accept_routes                  | 1 [галочка "Принимать маршруты"]

2. ОПЦИОНАЛЬНЫЕ ПАРАМЕТРЫ:
  [ИНФО] fw_mode                        | nftables [настройка "Режим межсетевого экрана"]
  [ИНФО] log_stdout                     | выключен [галочка "Журнал вывода"]
  [ИНФО] log_stderr                     | выключен [галочка "Журнал ошибок"]
  [ИНФО] disable_snat_subnet_routes     | SNAT включен [CLI флаг]

3. ПРОВЕРКА EXIT NODE:
  [OK]   advertise_exit_node            | включен [галочка "Узел выхода"]
  [OK]   advertise_routes               | 192.168.1.0/24 = 192.168.1.0/24 (br-lan) [настройка "Открыть подсети"]
  [OK]   zeroblock (running)            | интерфейсы br-lan,tailscale0 [настройка "Входящие интерфейсы"]

= СТАТУС ПОДКЛЮЧЕНИЯ:
  [OK]   Tailscale: подключен
  IPv4: 100.88.153.245
  IPv6: fd7a:115c:a1e0:ab12:4843:cd96:6258:99f5

= ДОПОЛНИТЕЛЬНЫЕ ПРОВЕРКИ:
  [OK]   Интерфейс tailscale0: существует

---

**2026-03-23T15:30:58 | Routerich**
ну попробуйте почитать
зероблока нет в репозитории
 * opkg_install_cmd: Cannot install package luci-app-zeroblock.
 * opkg_install_cmd: Cannot install package zeroblock.

---

**2026-03-23T15:46:17 | Andrey**
Приветствую. Нужен совет по общей стратегии настройки роутера. Я в этой теме новичок, поэтому хочу понять какой подход нормальный и в какой последовательности лучше всё настраивать. Насколько я понимаю, возможны разные варианты: например, установить Podkop, настроить списки, затем дополнительно использовать zapret2, Zeroblock и др. Но мне не очень ясно, что действительно нужно ставить вместе, что дублирует друг друга, а с чего лучше начать чтобы не усложнить себе жизнь с самого начала. Понимаю, что многое уже обсуждалось, но буду благодарен, если подскажете именно общую логику действий типа с чего лучше начинать, что ставить в первую очередь и какой сейчас рабочий вариант лучше всего

---

**2026-03-23T15:48:19 | Anna Bagler**
Zeroblock и Podkop - конфликт. Zeroblock + Zapret2.

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

**2026-03-23T16:34:25 | Максим**
Подскажите, пожалуйста, что такое ZeroBlock?

---

**2026-03-23T16:56:12 | Andrey**
напиши сочинение на тему как ты провел пол года с zeroblock

---

**2026-03-23T17:13:05 | Yury Kuzmenko**
по хэщ тегу #zeroblock

---

**2026-03-23T17:28:59 | Роман**
Zeroblock + zapret2.
AI, Block, Geoblock, Porn, Torrent, Games, Messengers, Meta списки.
▾

---

**2026-03-23T18:34:04 | Борис**
Скорее всего в Zeroblock -> Автонастройка стоит галочка "Автозагрузка секций". Из-за неё. Я у себя убрал и ZB перестал самовольничать

---

**2026-03-23T19:29:42 | Anna Bagler**
Все должно работать, youtubeUnblock отключайте и останавливайте, zeroblock и zapret2 ставьте.

---

**2026-03-23T19:36:46 | Kirill**
господа, стоит из коробки подкоп и запрет. но не пашут звонки тг. 
Если поставить zeroblock - не будут  эти служьы все конфликтовать? Хочу реанимировать звонки)

---

**2026-03-23T19:36:51 | Рамис Ганиев 🗿**
Zeroblock luci

---

**2026-03-23T19:41:04 | Anna Bagler**
По умолчанию на РР только youtubeUnblock. Он может не работать с настройками по умолчанию. Пробуйте связку zeroblock+zapret2 или только zapret2 для YouTube. Анблок тогда удалить или остановить и отключить.

---

**2026-03-23T19:44:54 | Anna Bagler**
Роdkop и zeroblock - прямой конфликт.

---

**2026-03-23T20:27:17 | Anna Bagler**
Забейте на подкоп, переходите на сторону zeroblock.

---

**2026-03-23T21:42:12 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.2-r24:
  Изменения:
  -DNS rule для локальных доменов/PTR не матчил запросы от dnsmasqm(source 127.0.0.1), PTR для приватных адресов уходил на внешний DNS и возвращал NXDOMAIN вместо ответа от dnsmasq
#ZeroBlock

---

**2026-03-23T21:44:28 | Anna Bagler**
Переходите на zeroblock.

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

**2026-03-23T22:31:58 | Роман**
Это списки доменов которые находятся в списках zeroblock.

---

**2026-03-23T22:40:17 | DmitrO**
У меня с отключённым Zapret2 и  ZeroBlock не открывает, да и с ними тоже(

---

**2026-03-23T23:00:12 | Anna Bagler**
Дальше ставить zeroblock в теме по нему есть полный мануал.

---

**2026-03-23T23:08:42 | Борис**
ну да, они там. по идее и на роутере должны отображаться

https://github.com/routerich/packages.routerich/blob/24.10.5/routerich/zeroblock_0.7.2-r24_aarch64_cortex-a53.ipk
https://github.com/routerich/packages.routerich/blob/24.10.5/routerich/luci-app-zeroblock_0.7.2-r24_all.ipk

---

**2026-03-24T06:58:16 | karat**
Да секция Zeroblock

---

**2026-03-24T07:15:07 | Routerich**
Здравствуйте.
отследить сервера/домены на которые они обращаются и добавить их в podkop/zeroblock

---

**2026-03-24T07:43:12 | Alex_Jester**
Возможно, что Zeroblock может повлиять на качество звука.

---

**2026-03-24T08:27:44 | Александр**
Просьба не пинать,я в том деле можно сказать совсем не шарю) установлен zeroblock и zapret2, ютуб,телега работают нормально,хотелось бы узнать как можно добавить определенные сайты,что бы они тоже открывались.Например рутрекер?

---

**2026-03-24T08:29:15 | Anna Bagler**
Cписок torrents добавить секцию proxy в zeroblock.

---

**2026-03-24T08:31:40 | Stepan**
Про zeroblock так вообще гуглится только то, что это для тильды какая-то щтука

---

**2026-03-24T08:35:27 | Anna Bagler**
Полный мануал по zeroblock в соотвктствуюшей теме читаем.

---

**2026-03-24T09:06:36 | Anna Bagler**
Дело не в прошивке, пробуйте стратегии для запрет или запрет2, или zeroblock и zapret2.

---

**2026-03-24T09:09:34 | Роман**
Zeroblock собственная разработка команды RR, средство точечной маршрутизации. Если вам нужно внести свои сайты в списки вам нужно: установить в браузер расширение ipv4oo, зайти на сайт с впн, отследить основные домены, внести их в пользовательские списки zeroblock.

---

**2026-03-24T09:11:47 | Anna Bagler**
Закреплённое сообщение в теме по zeroblock, там есть ссылка на списки.

---

**2026-03-24T09:20:17 | Artem**
Подскажите пожалуйста, как разблокировать определенный домен в zeroblock, ввести в секции awg10 его в пользовательские домены или это так не работает ?)

---

**2026-03-24T10:37:32 | ㅤㅤ**
Добрый день! 

Имеется 6 серверов в разных странах. Доступ к каждому из них осуществляется по протоколам и режимах: VLESS TCP REALITY XTLS VISION, VLESS TCP REALITY, VLESS GRPC REALITY, VMess TCP, VMess WebSocket, TROJAN WS TLS, SHADOWSOCKS

Требуется настроить работу через ZeroBlock на замену awg10. Пока не представляю как выстроить балансир, url-check. Предполагаю, что в ZeroBlock процесс автоматизирован.

Разумно использовать только один из протоколов, допустим Vless Reality Vision?

Какие технологии/пакеты в RouteRich нужно задействовать для грамотной организации обхода?

---

**2026-03-24T11:41:21 | Bullet for my valentine Poison**
Fresa и Zeroblock...😅

---

**2026-03-24T14:57:07 | 01000000**
Привет всем. Как верифицировать RouteRich чтобы в службах открылась вкладка zeroblock - автонастройка? В самом начале долгого пути! Интернет есть, dhcp. Прошивка 24.10.5.

---

**2026-03-24T15:04:53 | Роман**
Через пакеты устанавливайте zeroblock, создавайте новую секцию - туда свой vless и выбрать списки.

---

**2026-03-24T15:09:47 | Алексей Дербеденев**
Или при установке zeroblock так и будет?

---

**2026-03-24T15:12:02 | Константин**
А откуда в ванильной zeroblock? А он был в списке пакетов.

---

**2026-03-24T15:18:11 | Anna Bagler**
Вы списки кнопочкой обновили, zeroblock установили?

---

**2026-03-24T15:41:26 | Anna Bagler**
Если индикаторы в норме, сети сбросились, то прошилось. Ставьте zeroblock.

---

**2026-03-24T15:42:12 | 'Z' Sonic 'V'**
А про zeroblock можно подробнее?🤷‍♂

---

**2026-03-24T15:45:12 | Алексей Сергеевич**
Лучше ставь Zeroblock

---

**2026-03-24T15:45:33 | Anna Bagler**
Zeroblock Beta.

---

**2026-03-24T16:31:50 | Роман**
Выбрать список music в zeroblock.

---

**2026-03-24T16:32:25 | Nikonow**
ZeroBlock

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

**2026-03-24T17:50:09 | Wenzel Perminov**
убил какое-то время но поставил  byedpi на роутер, настроил youtube с ним через zeroblock, и результат браузер и офф приложение работают нормально как это было и с zapert2, newpipe иногда заикается, а smarttube, из-за которого я полез, ну он плохо буферит и долго начинается воспроизведение, лучше чем с запретом 2 было но все равно смотреть так не получится

---

**2026-03-24T18:02:18 | Роман**
Домены для разблокировки lol wild rift, закинуть zeroblock/podkop в список пользовательских доменов.

riotcdn.net
pvp.net
leagueoflegends.com
rgpub.io
rdatasrv.net
akamaihd.net

#games

---

**2026-03-24T19:40:57 | Bullet for my valentine Poison**
Zeroblock+Zapret2.

---

**2026-03-24T19:42:18 | Роман**
Я бы сбросил, и накатил zeroblock по новой.

---

**2026-03-24T19:55:44 | Роман**
Снести всё резетом, установить по новой zeroblock 😁

---

**2026-03-24T20:06:40 | Artur Shvydko**
Всем привет. Подскажите пожалуйста, есть ли кто-нибудь кто играет в where winds meet? Если да, может быть знаете, можно ли добавить какие то сервера для стабильной работы игры, постоянно наблюдается пинг. Сейчас установлен zapret2 + zeroblock, возможно там можно прописать в настройках маршрутизации какие то сервера? Например как с mortal kombat 1

---

**2026-03-24T20:43:10 | Роман**
А у друга там zeroblock не пытается с запретом за Ютуб драться?

---

**2026-03-24T20:59:16 | Oleg Shmyrin**
А подскажите, есть смысл попробовать установить ZeroBlock вместо podkop ?

---

**2026-03-24T21:37:50 | Anna Bagler**
Zeroblock cтавьте, Система - Пакеты, кнопочка Обновить списки, в поле фильтра zeroblock, а потом полный мануал по нему смотрите и поиском по чату пользуйтесь.

---

**2026-03-24T21:38:17 | Kiss_My_Axe**
Система - Пакеты. Обновить списки.
Установить
zeroblock
luci-app-zeroblock

---

**2026-03-24T21:55:26 | Anna Bagler**
Сбрасывайте и переходите на сторону zeroblock.

---

**2026-03-24T22:08:16 | Роман**
На основе этого сделан zeroblock.

---

**2026-03-24T22:20:15 | Роман**
clash royale и brawl stars обходятся списком games в zeroblock.

---

**2026-03-24T23:27:35 | Routerich**
/tmp/zeroblock/sing-box.d/ruleset

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

**2026-03-25T01:23:07 | Игорь**
Анализ запущен: 2026-03-25 01:21:25
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
  Facebook IP:  198.18.0.246 | YouTube IP:  198.18.0.152

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.13 MB
  Пинг (ya.ru via awg10): 29.615 / 30.638 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock opera-proxy

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200) [TLSv1.3]
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | STOPPED                        | ОТКЛ

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  zeroblock          Anime (prx url): anime
  zeroblock              awg10 (vpn): block,discord,googleplay,messengers,meta,news,porn,socials,video,youtube
  zeroblock          opera (prx out): ai,geoblock,cdn_aws,!_cdn_cloudflare
  Версия zeroblock: 0.7.2-r23
  zeroblock DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.42 | RAM: 23% | NAND: 24% занято / 51.4M доступно
  # ZeroBlock Monitor
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  # ZeroBlock Lists Update
  0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-03-25T08:46:00 | Routerich**
Здравствуйте.
Сбросить роутер и установить только Zeroblock

---

**2026-03-25T09:22:53 | Routerich**
Здравствуйте.
А у вас Podkop/zeroblock установлен?

---

**2026-03-25T09:41:59 | Udo**
Добрый день. Я так понял все разработки в данном ТГК в том числе и ZeroBlock вместе с Zapret2-finder залочены на фирменный роутер и их невозможно запустить на ванильной OpenWRT ?

---

**2026-03-25T10:02:00 | Роман**
Там zeroblock и запрет 😁

---

**2026-03-25T11:57:29 | Никита Веселов**
На телефонах при подключении к роутеру не приходят Push уведомления например от того же ВК. Настроен zeroblock + zapret2. Из за чего такое может быть? При подключении к мобильной сети сразу куча уведомлений приходит.

---

**2026-03-25T11:59:45 | Routerich**
Здравствуйте.
а если остановить ZeroBlock, Zapret2 приходят?

---

**2026-03-25T12:24:50 | Routerich**
Здравствуйте 
Лучше сброс, потом установка Zeroblock.

---

**2026-03-25T14:13:01 | Kiss_My_Axe**
ZeroBlock

---

**2026-03-25T14:18:53 | Максим**
Чёт не ищет пакет zeroblock

---

**2026-03-25T14:55:03 | Артём Фомин**
Народ, как полагаю, ZeroBlock выполняет те же функции что и podkop. Так что лучше из них поставить?

---

**2026-03-25T15:00:57 | Anna Bagler**
Zeroblock.

---

**2026-03-25T15:22:12 | Борис**
то есть ему лень было просто бинарник из телеграма ставить? По сути-то ничего не изменилось - так же ставится новая версия, и старый конфиг остаётся в системе, что может вызывать ошибки

Collected errors:
 * resolve_conffiles: Existing conffile /etc/config/zeroblock is different from the conffile in the new package. The new conffile will be placed at /etc/config/zeroblock-opkg.

---

**2026-03-25T15:48:49 | Anna Bagler**
Полный мануал для zeroblock изучите, схему в начале можно пропустить.

---

**2026-03-25T17:38:08 | Grigory**
Я вроде уже спрашивал, но есть ли способ разблокировать chatgpt и gemini? На zeroblock+zapret2. Сейчас как я понял обход работает только на grok

---

**2026-03-25T18:13:17 | Routerich**
Ставьте ZeroBlock и перестаньте мучаться. Для пользователей RR мы делали что бы работало в 2 клика

---

**2026-03-25T18:16:15 | Anna Bagler**
Связка идёт обычно zeroblock+zapret2.

---

**2026-03-25T18:27:41 | Anna Bagler**
Сбросить роутер, поставить zeroblock. Настроить. Инструкция есть в соответствующей теме.

---

**2026-03-25T18:40:39 | Костя**
на zeroblock тоже ютуб не работает

---

**2026-03-25T18:52:50 | Konstantin Fominykh**
Диагностика вся в зеленые галки. А в логах видно только Wed Mar 25 20:49:52 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Wed Mar 25 20:49:57 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock(0.7.2-r24)...
[zeroblock] ZeroBlock started successfully

---

**2026-03-25T18:54:07 | Костя**
не могу убрать ютуб из списка zeroblock он стоит в awg10 убираю галочку с ютуб нажимаю примянить все норм но только стоит перезагрузить страницу он опять включен . как его убрать

---

**2026-03-25T18:58:21 | Роман**
Можете тогда в тему zeroblock написать, разработчик посмотрит.

---

**2026-03-25T19:56:05 | ⁧pcall⁧**
Ну это я вижу,

Wed Mar 25 19:37:16 daemon.info zeroblock[12443]: [lists_loader] Section social: https://raw.githubusercontent.com/.../refs/heads/main/telegram/cidr.txt is not JSON, converting as mixed txt
...
Wed Mar 25 19:37:16 daemon.info zeroblock[12443]: [lists_loader] Converted mixed list to: /tmp/zeroblock/rulesets/remote-mixed-social-cidr.json (0 domains, 12 CIDRs)
Wed Mar 25 19:37:16 daemon.debug zeroblock[12443]: [sing_box_routing] >>> ENTER sing_box_cm_add_local_ruleset()
Wed Mar 25 19:37:16 daemon.info zeroblock[12443]: [sing_box_routing] Added local ruleset: tag=remote-mixed-social-cidr, path=/tmp/zeroblock/rulesets/remote-mixed-social-cidr.json
Wed Mar 25 19:37:16 daemon.info zeroblock[12443]: [lists_loader] Section social: added mixed list: https://raw.githubusercontent.com/.../refs/heads/main/telegram/cidr.txt

потом

Wed Mar 25 19:37:20 daemon.info zeroblock[12443]: [lists_loader] Section social: https://raw.githubusercontent.com/.../refs/heads/main/whatsapp/cidr.txt is not JSON, converting as mixed txt
...
Wed Mar 25 19:37:20 daemon.info zeroblock[12443]: [lists_loader] Converted mixed list to: /tmp/zeroblock/rulesets/remote-mixed-social-cidr.json (0 domains, 229 CIDRs)
Wed Mar 25 19:37:20 daemon.debug zeroblock[12443]: [sing_box_routing] >>> ENTER sing_box_cm_add_local_ruleset()
Wed Mar 25 19:37:20 daemon.info zeroblock[12443]: [sing_box_routing] Added local ruleset: tag=remote-mixed-social-cidr, path=/tmp/zeroblock/rulesets/remote-mixed-social-cidr.json
Wed Mar 25 19:37:20 daemon.info zeroblock[12443]: [lists_loader] Section social: added mixed list: https://raw.githubusercontent.com/.../refs/heads/main/whatsapp/cidr.txt
0.7.2-r24; уже конечно не важно, решил это по-другому

---

**2026-03-25T20:26:22 | Роман**
Dear developer. Это zeroblock в логах спамит? Как исправить не подскажете?

---

**2026-03-25T20:26:54 | Артём Фомин**
Народ, подскажите, пожалуйста.

Я установил ZeroBlock. После в автонастройках отметил галочками «Установить Opera Proxy», «Настроить AmneziaWG WARP», «Установить Zapret2», «Автозагрузка секций» и «Автозагрузка новой стратегии Zapret2». У меня заработал YouTube, Facebook, Instagram и другие сайты. Всё, больше вообще ничего не менял. Приятно впечатлён, что всё это без платных сервисов.

Хотелось бы уточнения по некоторым настройкам. Скажите, в данном случае необходимо или, может, желательно установить Xray через автонастройку? Xray будет использоваться с такими настройками?

---

**2026-03-25T20:32:32 | Grigory**
Есть люди кто юзает прокси zeroblock и играет в тарков? Повлиял ли он как то у вас на выходы из рейдов?

---

**2026-03-25T20:51:57 | Routerich**
если бы не "пахало", не стартанул бы. или ключ кривой, или xray молча принимает неподдерживаемое
Wed Mar 25 20:16:57 2026 user.notice xray: 2026/03/25 17:16:57 Using confdir from arg: /tmp/zeroblock/xray.d
Wed Mar 25 20:16:57 2026 user.notice xray: 2026/03/25 17:16:57.686745 [Info] infra/conf/serial: Reading config: &{Name:/tmp/zeroblock/xray.d/00-log.json Format:json}
Wed Mar 25 20:16:57 2026 user.notice xray: 2026/03/25 17:16:57.690464 [Info] infra/conf/serial: Reading config: &{Name:/tmp/zeroblock/xray.d/10-inbounds.json Format:json}
Wed Mar 25 20:16:57 2026 user.notice xray: 2026/03/25 17:16:57.690882 [Info] infra/conf: [/tmp/zeroblock/xray.d/10-inbounds.json] appended inbound with tag: in_20001
Wed Mar 25 20:16:57 2026 user.notice xray: 2026/03/25 17:16:57.690949 [Info] infra/conf/serial: Reading config: &{Name:/tmp/zeroblock/xray.d/20-outbounds.json Format:json}
Wed Mar 25 20:16:57 2026 user.notice xray: 2026/03/25 17:16:57.691573 [Info] infra/conf: [/tmp/zeroblock/xray.d/20-outbounds.json] prepend outbound with tag: out_20001
Wed Mar 25 20:16:57 2026 user.notice xray: 2026/03/25 17:16:57.691637 [Info] infra/conf/serial: Reading config: &{Name:/tmp/zeroblock/xray.d/30-routing.json Format:json}
Wed Mar 25 20:16:57 2026 user.notice xray: 2026/03/25 17:16:57.700515 [Warning] core: Xray 25.1.30 started
и коннекты xray принимает
Wed Mar 25 20:25:21 2026 user.notice xray: 2026/03/25 17:25:21.944534 from tcp:127.0.0.1:47368 accepted tcp:2ip.io:443 [in_20001 -> out_20001]
Wed Mar 25 20:25:22 2026 user.notice xray: 2026/03/25 17:25:22.983436 from tcp:127.0.0.1:47370 accepted tcp:2ip.io:443 [in_20001 -> out_20001]
Wed Mar 25 20:25:24 2026 user.notice xray: 2026/03/25 17:25:24.104271 from tcp:127.0.0.1:47380 accepted tcp:2ip.io:443 [in_20001 -> out_20001]
Wed Mar 25 20:25:25 2026 user.notice xray: 2026/03/25 17:25:25.137301 from tcp:127.0.0.1:47392 accepted tcp:2ip.io:443 [in_20001 -> out_20001]
Wed Mar 25 20:37:49 2026 user.notice xray: 2026/03/25 17:37:49.366925 from tcp:127.0.0.1:57626 accepted tcp:2ip.io:443 [in_20001 -> out_20001]
Wed Mar 25 20:37:50 2026 user.notice xray: 2026/03/25 17:37:50.396339 from tcp:127.0.0.1:57632 accepted tcp:2ip.io:443 [in_20001 -> out_20001]
Wed Mar 25 20:37:51 2026 user.notice xray: 2026/03/25 17:37:51.428555 from tcp:127.0.0.1:57644 accepted tcp:2ip.io:443 [in_20001 -> out_20001]
Wed Mar 25 20:37:52 2026 user.notice xray: 2026/03/25 17:37:52.560674 from tcp:127.0.0.1:57648 accepted tcp:2ip.io:443 [in_20001 -> out_20001]
Wed Mar 25 20:37:53 2026 user.notice xray: 2026/03/25 17:37:53.595452 from tcp:127.0.0.1:57660 accepted tcp:2ip.io:443 [in_20001 -> out_20001]
Wed Mar 25 20:37:54 2026 user.notice xray: 2026/03/25 17:37:54.628055 from tcp:127.0.0.1:57676 accepted tcp:2ip.io:443 [in_20001 -> out_20001]
Wed Mar 25 20:37:55 2026 user.notice xray: 2026/03/25 17:37:55.655994 from tcp:127.0.0.1:39380 accepted tcp:2ip.io:443 [in_20001 -> out_20001]

---

**2026-03-25T21:25:43 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.2-r42:
  Изменения:
  - Кнопки управления и статус сервиса перенесены над вкладками
  - Ignore tags — word-boundary matching (точное совпадение слов в тегах)
  - VPN секции — DNS всегда через direct-out
  - PTR запросы от dnsmasq — добавлен 127.0.0.0/8 в source_ip_cidr
  - TrustTunnel — кастомный путь к бинарнику через UCI
  - Opera health check — проверка через ya.ru (реальная связность)
  - Dashboard — кеширование DOM при Save (без перерисовки)
  
  Исправления:
  - Уникальные имена файлов для URL с одинаковым filename (whatsapp/cidr.txt vs telegram/cidr.txt)
#ZeroBlock

---

**2026-03-25T22:00:22 | Роман**
В коробке. Остальное в закрепах тем и в вики.
Можно сразу идти изучать тему zeroblock.

---

**2026-03-25T22:14:09 | Святос**
Ставьте ZeroBlock

---

**2026-03-25T22:24:01 | Vladislav**
Эти настройки? ZeroBlock » Настройки

---

**2026-03-25T22:59:42 | Артём Фомин**
Народ, а ZeroBlock можно поставить на другой роутер? У дочки «Xiaomi Mi Router 3G» с ванильным OpenWRT 24.10.5. Прекрасно работает Podkop. Хотел бы также попробовать в связке ZeroBlock и Zapret2. Оперативной памяти на этом роутере 256 Мб. Процессор двухъядерный MT7621A 880 МГц.

---

**2026-03-25T23:07:03 | Святос**
А где zeroblock клали

---

**2026-03-25T23:07:05 | Anna Bagler**
Подбирайте дальше тогда. Или пробуйте перейти на zeroblock со сбросом настроек.

---

**2026-03-25T23:14:57 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.2-r43:

  Исправления:
  - Исключения в настройках не принимали cidr
#ZeroBlock

---

**2026-03-25T23:44:50 | Святос**
Установите ZeroBlock, получите набор стратегий

---

**2026-03-26T00:44:57 | Kiss_My_Axe**
Кажись вилы нашёл...

Фейлсейф, стабби, doh удалены.
На WAN DNSами повешены: 77.88.8.8 1.1.1.1 8.8.8.8
В ZB (DOT) main: 9.9.9.9, bootstrap 77.88.8.8
DHCP и DNS, Перенаправления: 127.0.0.42
ZeroBlock не запускается. А пчему? А он списки скачать не может. А пчему? А sing-box не запущен, потому для ZB DNS не работает.
А сингбокс чо не запущен? Так листы же скачать невозможно!

Ну ничо такая петля вышла.
Версия: 0.7.2-r41

---

**2026-03-26T08:01:53 | Routerich**
Здравствуйте.
система->пакеты->zeroblock->установить->

---

**2026-03-26T08:34:32 | Routerich**
уровень логирования смените и рестарт zeroblock

---

**2026-03-26T09:28:27 | Aleksandr U**
А могу узнать для интереса (скрипт пока тьфу тьфу работает) чем скрипт отличается от zeroblock?

---

**2026-03-26T09:30:49 | Anna Bagler**
Тема zeroblock beta. В закрепах есть краткая инструкция и полный мануал.

---

**2026-03-26T09:39:34 | Aleksandr U**
Пока уточнить (жду доставки), как понял zeroblock ставить на чистую прошивку?

---

**2026-03-26T09:47:27 | Роман**
Возможно ли реализовать отключение youtubeunblock  (с автозапуском) при установке zeroblock? По сути переходя на ZB человек переходит на запрет 2 уже. Ну или галку в настройках на отключение.

---

**2026-03-26T09:54:54 | Роман**
Вы хотите рулить трафиком через амнезию? Устанавливаете zeroblock, там это есть.

---

**2026-03-26T10:03:05 | Роман**
Zeroblock юзер френдли, просто нужно создать новый интерфейс Amnezia, импортировать туда свой конфиг (.conf перетянуть в окошко), поставить галку не создавать маршруты, чуть-чуть настроить фаервол (скриншоты попозже могу скинуть), создать новую секцию в ZB, убрать галку с fake ip, выбрать список с тем что пойдет через Amnezia, и в принципе готово 😁

---

**2026-03-26T10:03:56 | HiLLL**
запустите в терминале
zeroblock awg warp

---

**2026-03-26T10:10:59 | Роман**
Zeroblock

---

**2026-03-26T10:16:00 | Роман**
rm /etc/config/zeroblock* /tmp/zeroblock_status.json && rm -rf /tmp/zeroblock /etc/sing-box/subscriptions /etc/zeroblock
Если ничего не менялось можно и конфиги почистить после пакетоудаления.

---

**2026-03-26T10:55:34 | Александр Самсонов**
В журнале кстати ругается
Thu Mar 26 09:00:01 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[config_builder] sing-box did not exit within 2000ms, sending SIGKILL
[zeroblock] ZeroBlock stopped successfully
Thu Mar 26 09:00:08 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock(0.7.2-r41)...
[ruleset_manager] API request failed (ret: 0, code: 502, size: 0)
[ruleset_manager] Failed to load community lists from any source
[lists_loader] Failed to load community index for v2 API
[config_builder] Download failed (1 errors), enabling auto_fallback two-stage-list via opera
[zeroblock] ZeroBlock started successfully

---

**2026-03-26T11:18:12 | Максим**
Интерфейс Амнезия уже создан, нужно ещё один? И все последующие манипуляции с фаерволом в новом интерфейсе производить или от ZeroBlockа

---

**2026-03-26T11:47:03 | Роман**
Значит в ЗБ новую секцию, там выбрать свой интерфейс, убрать fake ip, выбрать списки (кроме CDN) и наслаждаться работой zeroblock 😁

---

**2026-03-26T11:52:41 | Anna Bagler**
Zeroblock поставили? Какие списки выбраны? Локация вашего awg?

---

**2026-03-26T11:55:38 | Максим**
Zeroblock стоит. В списках и мета и social отмечены. Локация Нидерланды.

---

**2026-03-26T11:59:32 | Anna Bagler**
Zeroblock и меньше слушайте ИИ.

---

**2026-03-26T11:59:34 | Роман**
Zeroblock есть.

---

**2026-03-26T12:00:49 | Rockey**
Zeroblock не поможет в моем случае?

---

**2026-03-26T12:01:03 | Роман**
В панели управления, в zeroblock.

---

**2026-03-26T12:01:41 | Kiss_My_Axe**
Сингбокс это ядро, оно мешать не может.
А вам надо открыть настройки вашего интерфейса амнезии, перейти на крайнюю вкладку справа, открыть настройки пира и снять галку "Маршрутизировать разрешённые адреса", Сохранить, Применить.
Затем запустить скрипт №5, раздел BETA, закреп, либо установить ЗероБлок из репы, Система - Пакеты, Обновить списки, Фильтр zeroblock.

---

**2026-03-26T12:12:39 | Kiss_My_Axe**
Джентльмены! А чота я поплыл.
Надо завернуть траф роутера к адресу 9.9.9.9 через интерфейс AWG10.
Мне в Маршрутизацию итить, или ZeroBlock сам могёт?

---

**2026-03-26T12:29:21 | Святос**
Zeroblock должон позволять, ядро xray в нём ж есть

---

**2026-03-26T12:31:48 | Anna Bagler**
Ссылка вытаскивается из вашего приложения на телефоне? Если да, то вам в zeroblock. Или просить поддержку поставщика дать подходящую.

---

**2026-03-26T13:22:48 | Александр**
По прошествии пары недель уже можно написать отзыв) С покупкой и получением проблем не возникло,две недели борьбы с onu,дабы не зависеть от провайдерского оборудования,в итоге победили))Подключил роутер,установил zeroblock и zapret 2,практически не составило труда,хотя я далек от этой сферы деятельности,ютуб,телеграм,инстаграм,на телефонах и телевизорах работает на ура,дети в шоке,говорят все летает как раньше) Еще большой плюс в сообществе в телеграм,где подскажут в каком направлении двигаться,если что то не работает.Вообщем годная тема,главное что бы "товарищи" которые сами знаете,не обрубили совсем интернет.

---

**2026-03-26T13:26:42 | Diffie Hellman**
здравствуйте, такая проблема - можно ли в Zeroblock отправлять траффик одного конкретного хоста в туннель, а остальные ходят напрямую? у меня все хосты заворачиваются в туннель и я понять не могу как сделать то что мне нужно.
то есть как отключить Catch-all ?

---

**2026-03-26T13:37:13 | Роман**
Так и делайте всё не скриптом, а нормально. А то скрипт запустили и всё должно быть хорошо? Нет.
На бесплатных скриптах/вариантах будут проблемы. 
А вот установили бы zeroblock, прописали бы свой прокси сервер - всё взлетело бы 😁

---

**2026-03-26T13:50:23 | Diffie Hellman**
печально... вроде элементарнейшая  задача, а получается она не решаема средствами zeroblock 😒 может есть какие другие решения?

---

**2026-03-26T14:50:56 | Роман**
Проще установить zeroblock и создать свой интерфейс.

---

**2026-03-26T15:13:14 | Anna Bagler**
С вотсап через роутер может быть сложно. Ноут или ПК у бабушки есть, чтоб вы могли удаленно подключиться стандартными программами, а не средствами роутера?
И лучше себе zeroblock поставьте вместо подкопа, поработайте с ним, посмотрите.

---

**2026-03-26T15:15:18 | Олег**
Нет к сожалению ноута,zeroblock к сожалению тоже для меня как другой язык, с подкопом то не могу ничего понять, поставили друзья вот и сижу пытаюсь понять, что это за зверь)

---

**2026-03-26T15:50:39 | Anna Bagler**
Галочка в Мастере настройки. Даже если приложение выключено, закройте его полностью, чтоб ушло из памяти.
Накатить можно zeroblock. Но проблема устройства останется, раз на остальном и сейчас работает.

---

**2026-03-26T16:12:16 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.2-r47:
  Изменения:
  - DNS via Outbound — маршрутизация DNS-запросов через outbound секции (VPN/прокси) вместо direct. Отдельные опции для dns-main и bootstrap (глобально), а также для каждой секции.
  - Block catch-all — секция Block без доменов теперь корректно работает как killswitch (route.final = block-out).
  - PC Allow Mode — инвертированный родительский контроль: разрешить доступ только в указанное время, блокировать в остальное.
  - Обновлён мануал.

  Исправления:
  - CIDR в excluded IPs — routing_excluded_ips теперь принимает подсети.
  - Дедупликация — корректная работа при создании новых секций до первого сохранения.
#ZeroBlock

---

**2026-03-26T16:24:04 | Anna Bagler**
Тогда пробуйте отключить на самом устройстве, а роутеру верните.
Или сбрасывайте и пробуйте zeroblock.

---

**2026-03-26T16:40:42 | Anna Bagler**
Тогда zeroblock и запрет2 прямо просятся к вам.

---

**2026-03-26T16:51:03 | SCORPION**
БЛИИН! СПАСИБО ОГРОМНОЕ!!!!!!!
после ребута RR на всех устройствах ютуп заработал )))
ТОлько теперь вопрос: преимущество ZeroBlock + Zapret2  перед скриптом5, если нужны только соц сети и ютуп?

---

**2026-03-26T16:56:08 | Anna Bagler**
Преимущества вам выше кинули. Сама тема Zeroblock Beta. Быстрая установка в закрепах темы.

---

**2026-03-26T17:04:27 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.2-r48:
  Исправления:
  - Исправлена валидация dns bootstrap dns per section.
#ZeroBlock

---

**2026-03-26T17:53:29 | Anna Bagler**
Убирать анблок, ставить zeroblock и zapret2.

---

**2026-03-26T17:57:54 | Anna Bagler**
Тема zeroblock beta, в закрепах темы ссылка на полный мануал.

---

**2026-03-26T18:15:57 | Anna Bagler**
Закреп темы Zeroblock Beta.

---

**2026-03-26T18:44:23 | Игорь**
Выражаю огромную благодарность всей команде Routerich, за возврат в беззаботное прошлое👍 Настроил zeroblock и zapret 2 - всё летает👌Ещё раз всем СПАСИБО !

---

**2026-03-26T18:44:30 | Василий**
Добрый день, подскажите пожалуйста, зачем нужна эта настройка? Учитывая что в ZeroBlock в настройках задается DNS и в настройках интерфейса AWG тоже задается

---

**2026-03-26T20:12:00 | Роман**
Список видео выбран в zeroblock?

---

**2026-03-26T20:16:06 | Роман**
Перезапустите zeroblock. Проверьте в инкогнито.

---

**2026-03-26T21:37:03 | Артём Фомин**
Подскажите, я могу ZeroBlock в списках доменов указывать их таким образом? Чтобы включались абсолютно все поддомены.
*.duckdns.org

---

**2026-03-26T22:50:32 | Anna Bagler**
Идите в тему zeroblock beta. В закрепе есть краткая инструкция по настройке, выполняйте. youtubeUnblock можно пока остановить и отключить в Системе - Автозапуск, а потом и удалить.
Какой ТВ?

---

**2026-03-26T22:53:24 | Anna Bagler**
Тогда вам точно как минимум запрет2 нужен. Как раз поставите zeroblock и zapret2 по краткой инструкции, а потом можно будет смотреть.

---

**2026-03-26T23:22:53 | ZZII | RTK**
Как то возможно сделать отключение ZeroBlock, если впн ключ отвалился?

---

**2026-03-26T23:59:28 | Святос**
В теме ZeroBlock тут

---

**2026-03-27T00:07:57 | Роман**
С чем угодно, хоть zeroblock, хоть podkop. Но со своим сервером.

---

**2026-03-27T00:11:02 | Anna Bagler**
Zeroblock изучайте полный мануал.

---

**2026-03-27T00:13:25 | Роман**
Такое есть в zeroblock.

---

**2026-03-27T00:14:51 | Art**
Через zeroblock?

---

**2026-03-27T00:15:56 | Art**
А что за ошибка 255 при установке zeroblock?

---

**2026-03-27T00:31:04 | Anna Bagler**
Тема Zeroblock Beta. В закрепах краткая инструкция. Потом изучать полный мануал.

---

**2026-03-27T00:34:16 | Роман**
В службах есть zeroblock?

---

**2026-03-27T01:28:22 | Kiss_My_Axe**
Службы - ZeroBlock, вкладка "Панель управления", скрин.

---

**2026-03-27T07:39:20 | Routerich**
так вы про последнюю версию, я думал в целом о ZeroBlock в ASU

---

**2026-03-27T09:08:53 | er404**
Здравствуйте. Можно ли zeroblock установить на другой роутер, тоже с opwrt?

---

**2026-03-27T09:25:20 | S V**
Доброе утро!  Подскажите. пожалуйста,  в разделе система пакеты появились новые версии zeroblock /luci-app-zeroblock   0.7.2-r43 ( установлено 0.7.1-r53). Как понимаю их следует обновить.  Как понимаю это обязательное обновление.  И какая процедура внесения изменений? требуется  ли в этом случае какие либо моменты подготовки роутера?

---

**2026-03-27T09:33:05 | ZZII | RTK**
потому что если впн ложится то гугл не рабоатае, тк он в zeroblock как обход включен

---

**2026-03-27T10:48:02 | Vet**
Подскажите, zeroblock каки подкоп юзает fakeip?

---

**2026-03-27T10:49:08 | Виталий Александрович**
Всем привет. Помогите разобраться почему не открывается rutracker.
Установлены zeroblock+zapret2
Причем изначально после установки пакетов, rutracker c компа открывался, а сейчас ни с компа ни с телефона не работает. nnmclub тоже туда же

---

**2026-03-27T11:05:51 | Kiss_My_Axe**
В вики есть отличная инструкция по ZeroBlock, крупный шрифт, солидные отступы, увлекательный сюжет!
7 страниц театральной и 48 страниц режиссёрской версии. Категорически рекомендуется!

---

**2026-03-27T13:26:28 | Yrii**
Здравствуйте. Если я поставлю zeroblock  то Ютуб перестанет работать на zapret2

---

**2026-03-27T13:28:41 | Anna Bagler**
Тогда сбрасывайте, и переходите на zeroblock.

---

**2026-03-27T13:31:59 | Yrii**
Здравствуйте. Если поставлю на роутер zeroblock то утюб будет работать на  zapret2

---

**2026-03-27T14:07:20 | I**
Да вроде нет , никаких драйверов не обновлял,  только пакеты ставил zapret2, zeroblock

---

**2026-03-27T14:55:06 | Kirill Kulikov**
Здравствуйте. Подскажите, в чем проблема может быть? Роутер routerich AX3000, накатил zeroblock+zapret2. Вопрос касается нейронок, в частности Gemini. С пк работает корректно, но на телефоне Samsung S25 по wifi поработал пару дней и отлетел, стал ругаться на неподдерживаемую страну

---

**2026-03-27T15:05:52 | Kirill Kulikov**
Скрипт так же необходимо ставить, если уже стоит zeroblock?

---

**2026-03-27T15:26:00 | Routerich**
пакеты  | полный мануал | списки | ру списки | Полный перечень списков доступен в мануале
ZeroBlock 0.7.2-r55:
  Исправления:
  - Исправлены уязвимости command injection через UCI (source_ips, source_macs, trusttunnel_path, xray_path, yacd_secret)
  - Расширена валидация shell-метасимволов (# \ * ? [ ] ~)
  - Исправлены утечки памяти (21 место в outbounds, error path в facade/xray/subscription)
  - Валидация пустого proxy URL — блокирует сохранение секции без URL
  
  Изменения:
  - Liberty xray подписки
На этом жизненный цикл zeroblock как одноразового запускальщика заканчивается. Дополнительный функционал не будет принят в эту ветку. zeroblock будет полностью переделан в демона. Ожидайте новостей
#ZeroBlock

---

**2026-03-27T15:26:45 | Anna Bagler**
Система - Автозапуск отключаем и останавливаем youtubeUnblock. Идем в тему Zeroblock Beta. В закрепах есть краткая инструкция. Выполняем. Потом изучаем полный мануал по нему и настраиваем под себя.

---

**2026-03-27T15:32:50 | Bullet for my valentine Poison**
"zeroblock будет полностью переделан" даешь ремейк в 4к! 😊

---

**2026-03-27T16:29:58 | Andrew**
Здравствуйте. Хочу настроить резалку рекламы. Сейчас стоит zeroblock+zapret2,  установил из пакетов Adblock, как настроить чтобы это все вместе работало? Сейчас похоже не работает, хотя служба adblock активна. Настройках адблока надо интерфейс для запуска выбирать?

---

**2026-03-27T17:42:11 | Anna Bagler**
Диагностику zeroblock покажите. На страничке zeroblock.

---

**2026-03-27T17:50:28 | Anna Bagler**
PS надо в полную маршрутизацию. Присвоить IP на роутере. Идём в секции маршрутизации zeroblock. Находим awg10, изменить, находим адреса для полной маршрутизации и добавляем свою приставку. Не забываем сохранить и применить. Проверяем.

---

**2026-03-27T17:54:03 | Роман**
Идёте обзор, там находите ip приставки, жмёте присвоить ip. 
Далее в zeroblock жмёте изменить секцию, поле дополнительно - полная маршрутизация - выбираете ip приставки.

---

**2026-03-27T18:04:28 | Anna Bagler**
Zeroblock, Cекции маршрутизации, возле каждой есть кнопочка.

---

**2026-03-27T18:25:37 | Routerich**
uci set wireless.radio0.channel='auto'
uci set zeroblock.settings.enable_bad_interface_monitoring='0'
uci commit wireless
uci commit zeroblock
wifi reload
/etc/init.d/zeroblock restart

---

**2026-03-27T18:27:50 | Ilia Kotovich**
Я на чистый routerich установил zeroblock + zapret2. Далее я добавляю интерфейс с моим конфигом amnezia, но в RX всегда 0 (и handshake never). Что-то не так делаю?

---

**2026-03-27T18:29:13 | Ilia Kotovich**
Ну я имею ввиду что я новый интерфейс добавляю (помимо awg10, который с zeroblock как я понимаю добавляется). При этом конфиг (если использовать через приложение), то работает. TX при этом меняется

---

**2026-03-27T18:38:50 | Роман**
Либо пятый скрипт, либо https://t.me/routerich/394153/405571 Zeroblock.

---

**2026-03-27T18:48:19 | Роман**
Я вам уже написал, ютуб работает через youtubeunblock. Если этого достаточно можете более ничего не торгать. Но бывают разные побочные эффекты (не работает гугл диск, не входит в гугл аккаунт). Если нужно больше - скрипт 5/бета, zeroblock.

---

**2026-03-27T18:49:37 | Роман**
А если я хочу на каждый список свою секцию? Лишите права на zeroblock 😁

---

**2026-03-27T19:12:25 | Anna Bagler**
Тогда можно не скрипт, а в тему zeroblock. В закрепах есть краткая инструкция и потом изучать полный мануал к нему.

---

**2026-03-27T19:42:27 | Роман**
Всё равно придёте в zeroblock.

---

**2026-03-27T20:24:59 | Kirill Y**
Обновил роутер на последнюю прошивку. Установлен zeroblock по инструкции. Вроде многое работает, но перестал работать вход в приложение Xmeye.. Это камеры видеонаблюдения. Кто то может подсказать в чем проблема?

---

**2026-03-27T20:41:15 | Павел**
Здравствуйте, в приложении zeroblock пустил весь трафик через vpn, что нужно добавить чтобы WhatsApp заработал и другие мессенджеры

---

**2026-03-27T21:15:29 | HiLLL**
А потом устал. Запустите в терминале 
zeroblock awg warp

---

**2026-03-27T21:15:34 | Роман**
Дело ваше, при работающем zeroblock могут быть конфликты.

---

**2026-03-27T21:44:41 | Zorg**
Всем привет. Подскажите, пожалуйста. Только подключил новый роутер. Почитал темы. Не понял что сейчас устанавливать - ZeroBlock, Zapret2, podcop, всё вместе? Дайте направление о чем дальше читать)

---

**2026-03-27T22:02:07 | Роман**
Вы ставите Протон ВПН на роутер? Или просто конфиг в zeroblock импортировать хотите?

---

**2026-03-27T22:34:32 | Роман**
Устанавливается на сервер amnezia, в приложении генерируется конфиг и импортируется в zeroblock.

---

**2026-03-27T22:41:51 | Роман**
Пользуйтесь zeroblock со своими vless, hy2, amnezia2.0 - и проблем не будет.

---

**2026-03-27T23:17:13 | Alex_Jester**
Ну что господа и дамы, приехала ко мне данное устройство. Завтра буду тестить в связке с Кенетиком Гига. На кенетике оставлю usb_ssd по самбе и торрентокачалку, а также провайдерский интернет. А на Роутериче уже буду мутить машрутизацию через AmneziaWG с помощью Zeroblock

---

**2026-03-27T23:24:35 | Alex_Jester**
И еще вопрос Zeroblock поддерживает конфиги 2.0 Амнезии?

---

**2026-03-28T00:04:39 | Anna Bagler**
Zeroblock - Автонастройки скриншотом покажите.

---

**2026-03-28T00:29:47 | Anna Bagler**
Автонастройки zeroblock в режиме инкогнито покажите.

---

**2026-03-28T09:33:35 | Роман**
Даже альфа скорее, думаю с нуля перепишут и функционал докрутят. А zeroblock был большим бета тестом 😁
Будет zeroblock 2 remake.

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

**2026-03-28T12:23:02 | Владимир Ерусланов**
Спасибо большое 👌 возможно сможете подсказать по zeroblock, как настроить?

---

**2026-03-28T12:24:11 | Роман**
Ну что, как он, zeroblock remake?

---

**2026-03-28T12:54:06 | Святос**
Прошивку новую ждём со дня на день, пока не надо, ZeroBlock

---

**2026-03-28T12:56:01 | Anna Bagler**
Прошивка у вас актуальная. Связка zeroblock+zapret2 или zeroblock и zapret.

---

**2026-03-28T13:03:05 | Anna Bagler**
Любой бесплатный вариант загружен и не совсем стабилен. Ставьте zeroblock по краткой инструкции из темы Zeroblock Beta.

---

**2026-03-28T13:10:57 | Владимир Ерусланов**
Подскажите пожалуйста, установил zeroblock, но не могу поиграть в ps5, нет подключения к серверам. Есть возможность обойти это?

---

**2026-03-28T14:19:28 | Dmitriy**
Ребят, а кто знает в чем отличие: 

https://iplist.my-handbook.ru/ru

https://iplist.opencck.org/ru

по второй ссылке больше доменов и cidr при выгрузке. Вчера оттуда для телеги cidr стянул , пободрее пошла. По первой, если выгружать, то совсем уныло работала. 

Ещё вопрос: Как часто они обновляются эти списки и кто вообще из ведёт ? имеют они что то общее с теми, что в zeroblock нужно отмечать?

---

**2026-03-28T15:36:36 | Anna Bagler**
Если обновляли прошивку, то можно было и zeroblock вместо подкопа поставить. Без обновления, просто скрипт №5 запустить.
Код диагностики теперь ещё раз.

---

**2026-03-28T16:41:39 | Anna Bagler**
Что сделать, написано выше было для вашей ситуации. Раз сбросили, то в закрепы темы zeroblock, там краткая инструкция есть.

---

**2026-03-28T16:41:52 | Роман**
Очевидно не накатывать скрипт 5. Попробуйте zeroblock. 
Ютуб сейчас работает через youtubeunblock.

---

**2026-03-28T16:56:59 | Igor Korsakov**
на компе ютуб перестал оаботать, на телефоне ок по вайфаю. ZeroBlock перезапустить надо?

---

**2026-03-28T17:41:10 | Routerich**
Здравствуйте.
Вам выше написали
Zeroblock->Вкладка Диагностика

---

**2026-03-28T17:45:13 | Routerich**
А если перезапустить Zeroblock тоже не работает?

---

**2026-03-28T17:48:17 | Routerich**
@cooperm вывод покажите
zeroblock check_nft_rules
zeroblock nft_list_tables

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

**2026-03-28T18:00:32 | Routerich**
в zeroblock диагностику

---

**2026-03-28T18:16:10 | Николаич**
Спецы такой вопрос: обновив zeroblock надо так же через пакеты обновлять zapret2?

---

**2026-03-28T18:57:15 | Роман**
В сторону обновления прошивки (если старая), затем установки zeroblock.
Если лень - скрипт бета/5 снова накатить (на удачу).
Для ютуба/дискорда/роблокса - запрет 2/1.

---

**2026-03-28T18:59:36 | Артём Фомин**
Всем привет.
Как я полагаю, zapret2 и zeroblock лучше периодически обновлять. Подскажите, после обновления всё надо будет настраивать заново, или настройки сохраняться?

---

**2026-03-28T19:15:16 | Routerich**
Да, или zeroblock

---

**2026-03-28T19:19:12 | Роман**
Zeroblock получше будет.

---

**2026-03-28T19:50:21 | Routerich**
да или zeroblock

---

**2026-03-28T19:50:46 | Anna Bagler**
Zeroblock тогда уж.

---

**2026-03-28T20:08:31 | Alla Eva**
При установки пакета zeroblock выдает ошибку 255. Что не так, подскажите?

---

**2026-03-28T20:15:44 | Routerich**
А можете раздать с телефона wifi точку доступа?
Потом сеть->Беспроводная сеть->Поиск-> подключайтесь к своей точки (от телефона) вводим пароль, потом опять в пакеты идеи и обновляем список и устанавливаем zeroblock по инструкции

---

**2026-03-28T20:19:40 | Anna Bagler**
Запрет2 заточен на YouTube. Если вы его поставили, то из zeroblock YouTube надо убрать.

---

**2026-03-28T20:28:05 | Yury Kuzmenko**
zeroblock

---

**2026-03-28T20:52:16 | Anna Bagler**
У вас приставка была прописана по IP в подкопе, скорее всего. Так же надо сделать и в zeroblock. Вы не сами ранее настраивали?

---

**2026-03-28T23:12:10 | Kiss_My_Axe**
Либо устанавливать ZeroBlock из реп - Система - Пакеты, обновить списки, Фильтр ZeroBlock, установить оба пакета.
Либо скрипт №5 с подкопом.

Рекомендую зероблок.

---

**2026-03-28T23:47:07 | De**
Добрый вечер установил zeroblock указал свои vless. chatgpt грузится обновление на шлем oculus прилетело установил. Телеграмм не неработает не на ПК не на телефонах. Если через hidify на телефоне то телеграмм работает. Как исправить.

---

**2026-03-29T08:44:55 | Routerich**
но и еси чо 
ZeroBlock 0.7.2-r47:
  - Block catch-all — секция Block без доменов теперь корректно работает как killswitch (route.final = block-out).

---

**2026-03-29T09:11:38 | ꧁ 𝓐𝓷𝓽𝓸𝓷 𝓑𝓮𝔃𝓴𝓪𝓹𝓾𝓼𝓽𝓲𝓷 ꧂**
Я telemt вчера поставил - он прям в пакетах есть

Единственное, по умолчанию не понял как сделать, чтобы он через Zeroblock ходил

В итоге в качестве upstream указал ему сокс5 прокси, который на этом же роутере крутится и всё завелось

---

**2026-03-29T09:43:32 | Routerich**
С обновления прошивки до актуальной версии, потом либо скрипт либо Zeroblock

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

**2026-03-29T10:19:58 | Routerich**
Потом создайте секцию zeroblock и укажите свой созданный интерфейс

---

**2026-03-29T10:29:27 | Роман**
Нет, я спросил как дела с zeroblock. Поинтересовался. Может новой партией скриншотов порадуете. Это я так (remake) вашу переделку zeroblockа называю 😁

---

**2026-03-29T12:24:29 | Роман**
Будем готовить уважаемый zeroblock. 
Будем ждать релиз уважаемого zeroblockа.

---

**2026-03-29T12:31:21 | Роман**
По логике если папа - Fresa, его мама это @BFMVPoison! А ну выпускай уважаемый zeroblock погулять! 😁
(Шутка юмора без целей принизить или оскорбить кого либо)

---

**2026-03-29T13:01:48 | Anna Bagler**
Список музыки добавьте в секцию opera zeroblock и оттуда уберите IP для полной маршрутизации.

---

**2026-03-29T13:03:58 | Роман**
Верим. Оно само там оказалось. Если не сами, сбрасывайте на завод и начисто устанавливайте zeroblock.

---

**2026-03-29T13:31:34 | Роман**
Для этого другие люди есть 😁
Они уважаемого zeroblock погулять не пускают.

---

**2026-03-29T13:52:50 | Bullet for my valentine Poison**
https://scpfoundation.net/scp-079 Походу я нашел доки на Fresa 😅 Даже Zeroblock удалил.

---

**2026-03-29T14:09:51 | Степан**
День добрый!Телеграмм начал соединение терять , выгрузишь приложение запустишь заново, какое время работает нормально, может быть из-за версии zeroblock или вряд ли (версия из шапки)?

---

**2026-03-29T14:51:12 | Միխայիլ Կուլագին**
Не получается отредактировать community lists в zb 0.7.2-r52.
Помогите, пожалуйста, разобраться, это я что-то делаю не так или лыжи не едут?

Сценарий в luci:
1. Services->ZeroBlock
2. Routing Sections
3. awg10 -> edit
4. закладка lists, в списке community lists снимаю галочку youtube, нажимаю save
5. контрольный взгляд на unsaved changes (см. скриншот), тут нажимаю save & apply
6. происходит обычное применение настроек, система сообщает об успехе применения этих настроек, но
7. при просмотре community list'а галочка у youtube в итоге так и остаётся.
Это у меня воспроизводится на
zeroblock  0.7.2-r52
luci-app-zeroblock  0.7.2-r52
и нормально работает на "соседнем" роутере с 
zeroblock  0.7.2-r43
luci-app-zeroblock  0.7.2-r43
Пробовал загружать страницу с очисткой кеша браузера, пробовал другой браузер, другой компьютер...

---

**2026-03-29T15:13:52 | Роман**
Не ест xray в zeroblock конфиг Amnezia xray. Редактировать надо (разработчик сказал). А как редактировать не знаю 😁

---

**2026-03-29T15:14:00 | I.S.**
Добрый день. Коллеги подарили ваш роутер 😊 начал настраивать - поставил zeroblock и следом начал конфигурить AWG-2.0. при импорте файла или попытке вбить хендшейки в виде диапазонов - ругается на неверные значения. При этом, рядом на виртуалке есть ванильная wrt-ха, и она их ест и все работает. Ждём обновление ?

---

**2026-03-29T15:59:21 | I.S.**
В вашем мануале написано, что конфиг singbox-tiny должен лежать в /tmp/zeroblock/conf.d, а он лежит в /tmp/zeroblock/sing-box.d. Нет ли в этом какого-то ... ? sing-box-tiny - 1.12.22-r1

---

**2026-03-29T16:05:28 | Anna Bagler**
Добавьте cdn github в zeroblock и попробуйте ещё раз.

---

**2026-03-29T16:38:11 | Anna Bagler**
Zeroblock стоит с zapret2?

---

**2026-03-29T16:47:32 | Anna Bagler**
Zeroblock по краткой инструкции поставили?

---

**2026-03-29T17:11:22 | Alex Korshun**
Хороший человек и по совместительству разработчик Zeroblock

---

**2026-03-29T17:16:52 | Денис Давидчук**
Я забиваю zeroblock внизу ни чего не появляется

---

**2026-03-29T17:17:58 | ARTEM**
Как пустить весь трафик через zapret а после него через zeroblock ?

Такая проблема ютуб работает через zapret, но именно когда первый раз открываешь ютуб на любом устройстве прогружается долго потом уже нормально,хочу убрать этот так называемый "спящий режим" zapret

---

**2026-03-29T18:15:15 | Anna Bagler**
Если на чистую, то ставьте zeroblock, скопируйте себе краткую инструкцию из закрепа.

---

**2026-03-29T19:06:03 | Илья**
Что в ZeroBlock необходимо выбрать что num начал работать ?

---

**2026-03-29T19:18:30 | Роман**
И значальное моё сообщение про пол-интернета содержит подтекст того, что много лишнего может попасть в прокси. Что мне пытаешься доказать?
У каждого разный кейс использования zeroblock, я например стараюсь как меньше всего пускать в прокси. Если ваше использование отличается от моего - что с того? Мне тоже кучу CDN выбрать? 
Каждый делает как хочет, но последствия выбора кучи CDN уже не раз видели в чате, поэтому рекомендуют их выбирать только если знаешь что делаешь, и последствия разгребать самому.

---

**2026-03-29T19:23:48 | Роман**
Ты шаришь за zeroblock? Да. А в чат приходят те, кто не разбирается, а потом ой, а чё не так.
Лол, сижу с портянкой доменов.

---

**2026-03-29T20:02:58 | Святос**
Похоже, что прокисла конфигурация awg, генерите другую. Или применяйте ZeroBlock

---

**2026-03-29T20:16:04 | Алексей Храбрых**
День добрый. Настроил по инструкции Zeroblock+zapret2. Из списков Music - Tidal не робит что-то,на разных устройствах.  Пишет на сайте Your request was blocked. Куда копать? Soundcloud нормально все

---

**2026-03-29T20:37:00 | Gomer Simpson**
Тема ZeroBlock

---

**2026-03-29T20:51:54 | Alex_Jester**
Я правильно понимаю, что Zapret2 в Zeroblock используется только для Youtube. И если я планирую пускать трафик Ютуба через VPN, то можно Запрет и не устанавливать (не ставить галочку №4)

---

**2026-03-29T20:53:10 | AEBus**
вообще хронология такая - только вчера забрал с озона роутерич, подключил к своему ONT роутеру через PPOE BRIDGE, установил zeroblock, всё. больше ничего не трогал и не настраивал

---

**2026-03-29T21:13:55 | Роман**
Для игры в Infection Free Zone достаточно доменов

openstreetmap.org
jutsugames.com
maptiler.com

Добавлять в список пользовательских доменов zeroblock/podkop.
P.S Open Street Maps сомневаюсь что нужно, закинул докучи 😁
#games

---

**2026-03-29T21:21:12 | Роман**
Из lan вашего роутера в wan routerich. 
Остановить/удалить youtubeunblock, установить zeroblock. Свои впн/vless сервера имеются?

https://t.me/routerich/394153/405571

---

**2026-03-29T21:42:03 | Eljerbo**
почитал, не увидел инструкцию по моему вопросу. 

из того что прочитал: создать секцию маршрутизации, тип VPN, а дальше не понятно.

мой вопрос конкретный - "можно ли свой конфиг xray со своего сервера скормить перенести в роутер" ?

в документации zeroblock_full_manual2.pdf в разделе "19.3 Транспорт mKCP "есть шаблон:
vless://uuid@host:port?type=kcp&seed=SEED&headerType=wireguard#Name

в каком месте в настройках роутера нужно вставлять такого типа ключ?

---

**2026-03-29T22:34:08 | Андрей**
все верно, не нужно. не забудьте включить tailscale0 во Входящие интерфейсы в ZeroBlock

---

**2026-03-29T23:15:03 | Nick**
За тую не знаю а esp на телеграмовском боте глючила. Команды доходили но пины не включались. Через zeroblock  расчихалась

---

**2026-03-29T23:39:55 | HiLLL**
Установка zeroblock opera + awg. Далее выбирайте в секции списки которые вам нужны. Не выбирайте CDN все подряд!

---

**2026-03-29T23:59:10 | Роман**
Мдя. Короче удел запрета 2 быть придатком уважаемого zeroblockа 😁
Не каждый будет этим заниматься.

---

**2026-03-30T10:48:54 | I.S.**
В целом - все хорошо, завелось и работает - zeroblock. Но есть мелкие детальки - мало lan-портов, ну хотя бы 4, короткий провод у блока питания (да , найду аналогичный по параметрам, но хотелось бы сразу). По настройке - в принципе все без проблем.

---

**2026-03-30T11:29:48 | Anna Bagler**
Смотрите закреплённые сообщения темы zeroblock beta.

---

**2026-03-30T11:43:09 | Routerich**
Здравствуйте.
сбросить роутер и поставить zeroblock

---

**2026-03-30T12:51:19 | Роман**
Просто продолжайте настройку. Никакие пакеты обновлять массово не стоит, для этого есть (как заметили выше) ASU (но это потом, как разберётесь немного). 
Такие пакеты как zeroblock, zapret2 - можно обновить.

---

**2026-03-30T13:13:55 | Святос**
1) Установить ZeroBlock (лучше со сбросом)
2) С установкой авто настройки подождать/перезагрузить раза два

---

**2026-03-30T14:54:18 | Anna Bagler**
Если у вас все работает, то можно даже связку zeroblock+zapret2 не обновлять.

---

**2026-03-30T15:48:52 | Grigory**
grok по умолчанию вроде работает в стандартной конфигурации без настроек, zapret2+zeroblock с включенным списком ai

---

**2026-03-30T15:51:08 | Роман**
И ChatGPT, и Gemini нормально работают с zeroblock.

---

**2026-03-30T16:05:47 | Grigory**
zapret2 zeroblock и вроде там опера включена, остальное стандартное ничего не настраивал

---

**2026-03-30T17:05:21 | Anna Bagler**
Скрипта нет, есть краткая инструкция в теме zeroblock beta.

---

**2026-03-30T17:11:24 | Anna Bagler**
Тема Zeroblock Beta.

---

**2026-03-30T17:50:06 | Данила Ступин**
Здравствуйте! У меня вопрос по zeroblock. После настройки catch-all секции с warp зероблок стал работать нестабильно. Он какое-то время работает нормально, а затем "умирает". То есть маршрутизация работает исправно, а интерфейс зероблока глючит (нельзя выбрать интерфейс, выбранные списки не все отображаются). При этом интерфейс зероблока очень долго загружается, а в консоли появляются ошибки. Перезапуск зероблока помогает, но ненадолго. Вот и не знаю, что ему не нравится.

---

**2026-03-30T18:29:18 | Ivan Num**
Подскажите. В zeroblock когда убираем из авг10 Ютуб. Через что он начинает работать?

---

**2026-03-30T18:35:48 | Ivan Num**
Просто по инструкции настроил zeroblock. Zapret2 получается установлен тоже. Летает быстрее чем на скрипт 5

---

**2026-03-30T18:42:02 | Ivan Num**
Я на сток накатил zeroblock

---

**2026-03-30T19:58:26 | Routerich**
Здравствуйте.
Поддержка тут.
Ставьте либо 5 скрипт либо Zeroblock

---

**2026-03-30T20:15:54 | Роман**
Только после релиза уважаемого zeroblockа.

---

**2026-03-30T20:23:37 | Андрей**
@RouterichSupport а вы zeroblock на github не выкладывали?

---

**2026-03-30T20:36:47 | Роман**
То есть вы сначала установили скрипт 5, затем zeroblock?

---

**2026-03-30T20:38:11 | Данил**
Установил zeroblock

---

**2026-03-30T21:16:42 | Данил**
Если сбросить настройки, то нужно будет запустить только скрипт? Или zeroblock тоже нужен.

---

**2026-03-30T21:19:57 | Роман**
Zeroblock нужно устанавливать отдельно. Либо скрипт 5, либо zeroblock.

---

**2026-03-30T21:24:27 | Anna Bagler**
Cбросьте и ставьте zeroblock внимательно.

---

**2026-03-30T21:24:50 | Данил**
Кароче, сбрасываю настройки, ставлю zeroblock, и потом скрипт? Правильно?

---

**2026-03-30T21:25:24 | Anna Bagler**
Никаких скриптов, сброс и zeroblock.

---

**2026-03-30T21:26:39 | Роман**
Никаких скриптов. Только zeroblock.

---

**2026-03-30T21:34:11 | Routerich**
использовать zeroblock

---

**2026-03-30T22:07:48 | Anna Bagler**
Тогда ставьте первым и добавляйте исключения в zeroblock.

---

**2026-03-30T22:30:21 | Routerich**
хм. из вариантов. провод в wan рр, открытие доступа к wan в firewall, zeroblock, создать секцию по вкусу, в ней mixed proxy на все интерфейсы, прокси готов. тогда из рр получится standalone прокси в сети, подключать к нему естественно ничего не нужно

---

**2026-03-30T23:10:45 | Роман**
Вам проще экспортировать из amnezia формат .conf, создать новый интерфейс, настроить фаервол и указать этот интерфейс в zeroblock.
https://t.me/routerich/4/573119

---

**2026-03-31T00:36:08 | DEMYAN DUDKIN**
Установил zeroblock выдает такие ошибки

---

**2026-03-31T01:26:04 | Anna Bagler**
Роdkop и zeroblock не взаимодействуют. У подкопа остановить и отключить. Зироблок запустить. Ещё раз диагностику.

---

**2026-03-31T01:32:08 | Anna Bagler**
Да. И потом только zeroblock ставить.

---

**2026-03-31T02:16:45 | Alex_Jester**
Установи Zeroblock по гайду из закрепа и все будет открываться.

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

**2026-03-31T02:41:52 | DEMYAN DUDKIN**
Спасибо при огромнейшее, сбросился до заводских, , установил zeroblock, вроде всё ок , и телега без прокси пашет , Ютуб пошёл 😀👏

---

**2026-03-31T06:44:16 | Routerich**
на всех устройствах проблема?
что показывает диагностика в ZeroBlock?

---

**2026-03-31T06:46:45 | Роман**
Как без полного ребута, удалить zeroblock?

---

**2026-03-31T08:55:35 | Routerich**
Здравствуйте.
Сразу 5-й или Zeroblock установить

---

**2026-03-31T09:30:04 | Routerich**
Здравствуйте.
Он добавлен у вас в список для обхода скорее всего.
Попробуйте остановить zeroblock/podkop и проверить, сможете войти или нет

---

**2026-03-31T09:50:35 | Iceking**
Здравствуйте, остановил zeroblock, 2ip.ru пишет корректное местоположение - Москва. Смотреть в «Секции маршрутиризации» - Списки? Там есть Списки сообщества AI, Block, Geoblock, Socials и т.д. Может быть тут лишние галочки поставил? Где можно посмотреть, что включено в этот список?

---

**2026-03-31T09:55:12 | Iceking**
Зашел на мос.ру - заблокировало, зашел проверить 2ip.ru - показывало Швецию, чуть позже Нидерланды. Выключил ZeroBlock - 2ip.ru показывает Москва. В секции маршрутиризации убрал галочку Opera Proxy, теперь 2ip.ru показывает Москва, как и хочу. Телеграм, ютуб, инстаграм - работают

---

**2026-03-31T10:10:16 | Routerich**
какую монету "не встроил"? может zeroblock не то майнит?

---

**2026-03-31T10:12:43 | Alx**
всем привет,поставил ZeroBlock все нормально,работало 24 часа,сегодня было отключение эл энергии и после этого роутер в статусе пишет что Internet подключен, а warp отключен.. как полечить? всем спасибо кто по делу откликнется

---

**2026-03-31T10:41:06 | Владимир Волков**
Не увидел ответа вам, поэтому кратко направления:
1) Если есть какие-либо базовые навыки, читайте закреплённые сообщения в теме "Zeroblock Beta", там есть полный мануал по функциям и инфа для настройки
2) Если навыков нет, читайте закреплённое сообщение про скрипт №5 в теме "Интернет без границ"

---

**2026-03-31T11:52:18 | Andrew**
Добрый день. Подскажите возможно ли на роутере поднять впн, и чтобы другие клиенты могли подключиться к нему и смотреть Ютуб с настроенным на роутере обходом zeroblock+zapret2? Ширина канала позволяет. Если это возможно, то сколько клиентов он потянет?

---

**2026-03-31T11:56:51 | Routerich**
zeroblock

---

**2026-03-31T12:10:50 | Evgeny**
а скрипт на установку zeroblock не выпускали еще?

---

**2026-03-31T12:18:40 | Anna Bagler**
Если у вас есть свой vless, запускайте клиент с ним локально.
Если надумаете cтавить zeroblock, то настройки роутера лучше сбросить, подкоп и зироблок не совместимы.

---

**2026-03-31T13:42:44 | Anna Bagler**
Сбрасывайте и переходите на zeroblock.

---

**2026-03-31T13:46:01 | ່fassha**
Всем добрый день, хотелось бы узнать
Вчера когда я все настроил, ютуб на телеке "летал" (в хорошем смысле ),
А сегодня я захожу в ютуб, то идет с нормальными такими лагами, хотя ZeroBlock я настраивал, и фильтры тоже, кто помочь сможет?

---

**2026-03-31T13:51:45 | Макс**
Ничего не вылезало, но спустя  время фильтр проснулся. Запустил первую установку ZeroBlock. 2й зироблок почему то с луси  перед зиро.
В инструкции написано, что сначала зиро должен быть. 
Вот пока писал сообщение во время установки произошла ошибка

---

**2026-03-31T14:08:52 | Anna Bagler**
А точно без сохранения настроек прошили? По инструкции выше для zeroblock идите.

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

**2026-03-31T14:51:02 | Aidar Garikhanov**
Всем привет! ZeroBlock переваривает такого вида файлы (JSON) при добавлении в пользовательские списки?
https://raw.githubusercontent.com/rekryt/iplist/refs/heads/master/config/tools/clickup.com.json

Или нужен обязательно plain text с одним доменом/IP на строке?

---

**2026-03-31T15:00:40 | Anna Bagler**
Анблок удалять, ставить zeroblock.

---

**2026-03-31T15:01:07 | Роман**
Лучше zeroblock.

https://t.me/routerich/394153/405571

https://t.me/routerich/394153/581524

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

**2026-03-31T15:35:36 | Anna Bagler**
Если у вас закрытая ОС на ТВ и YouTube через zeroblock, то это может быть нормально. Руками качество не даёт поднять? ТВ какой?

---

**2026-03-31T16:19:49 | Anna Bagler**
Пусть он вам и поможет тогда, наверняка настраивал, раз посоветовал.
Убирайте YouTube из zeroblock, разбирайтесь, как вносить стратегию в zapret2 Включайте zapret2 и пробуйте стратегию из закрепа темы Zapret2.

---

**2026-03-31T16:22:53 | Gomer Simpson**
Попробуйте ZeroBlock. Соседняя тема. Информация в закрепе темы ZeroBlock.

---

**2026-03-31T16:24:38 | Evgen**
opkg install zeroblock

Installing zeroblock (0.7.2-r52) to root...
Downloading https://github.com/routerich/packages.routerich/raw/24.10.5/routerich/zeroblock_0.7.2-r52_aarch64_cortex-a53.ipk
Installing sing-box-tiny (1.12.22-r1) to root...

Ошибкиundefined
Collected errors:
 * check_conflicts_for: The following packages conflict with sing-box-tiny:
 * check_conflicts_for:  sing-box * 
 * opkg_install_cmd: Cannot install package zeroblock.

Команда opkg install завершилась с ошибкой с кодом 255.

---

**2026-03-31T16:33:31 | Petro**
Заходите система пакеты твм нажать обновить списки далее когда обновяться то в поиске вписываете Zeroblock И устанвливаете

---

**2026-03-31T17:07:05 | Petro**
А если теперь попробовать через пакеты установить Zeroblock

---

**2026-03-31T17:15:15 | Anna Bagler**
Если будете включать анблок, отключайте запрет2 и убирайте список YouTube из zeroblock. Иначе будут конфликты.

---

**2026-03-31T17:20:31 | Anna Bagler**
Если стоит zeroblock, то пробуйте в нем.

---

**2026-03-31T17:31:15 | Aziz Dadaboev**
Всем привет. Я поставил ZeroBlock, включил все галочки в Автонастройке, все летает, все отлично, но почему то WhatsApp прям совсем медленный, даже сообщения идут с большим трудом, кто нибудь знает почему так и можно ли это поправить?

---

**2026-03-31T18:43:15 | Роман**
Найти хостера, купить vps, поднять ранель (разные варианты) - импортировать ссылку в zeroblock.

---

**2026-03-31T18:57:07 | Routerich**
с обновления zeroblock

---

**2026-03-31T18:59:19 | Routerich**
Здравствуйте.
можно, либо 5-й скрипт, либо zeroblock

---

**2026-03-31T19:29:31 | Mau**
Всем привет. Можно ставить к  zeroblock  скрипт #5  или только что то одно  ?

---

**2026-03-31T19:35:14 | Alik Shaimov**
Всем привет. Zeroblock лечит телегу? Сижу давно на подкопе по 5 скрипту, сегодня телега прилегла.

---

**2026-03-31T19:46:40 | Anna Bagler**
Если у вас zeroblock, то в нем, по аналогии с подкопом.

---

**2026-03-31T19:52:22 | Routerich**
Создать интерфейс AmneziaWG, закинуть туда свой конфиг, потом в Zeroblock создать секцию и выбрать в качестве vpn интерфейса ранее созданный и все

---

**2026-03-31T20:48:39 | Jelani**
Подскажите как вы решаете что использовать?
Получается есть 2 основных варианта или нет?
1) Установить скрипт #5 (это Podkop)
2) Установить Zeroblock и Zapret2

Или там много разных вариантов просто это два готовых варианта для чайников кто не шарит в сетях?

---

**2026-03-31T20:52:47 | Anna Bagler**
Ставьте zeroblock.

---

**2026-03-31T21:59:06 | Роман**
Когда уважаемый zeroblock выйдет?

---

**2026-03-31T22:28:13 | Роман**
Уважаемый zeroblock ему слили, тестовую сборку, вот и молчит.

---

**2026-03-31T23:21:45 | Anna Bagler**
На странице zeroblock находим секции маршрутизации, изменить возле нужной.

---

**2026-04-01T00:50:41 | Iceking**
Господа, подскажите, пожалуйста, есть несколько вопросов:
1. Пользуюсь сервисом, там есть: WireGuard Pro, AmneziaWG и OpenVPN. Сейчас в ZeroBlock поставил AmneziaWG Германия. Есть еще варианты: Англия, Гонконг, Польша и Турция. Если загрузить второй конфиг, то придется выбирать, чем пользоваться или оба могут работать в параллели?
2. Chatgpt отлично работает в браузере, а в приложении на телефоне сообщение о недоступности в регионе. Куда смотреть?

---

**2026-04-01T01:30:56 | Iceking**
Значит не совсем понимаю. Службы-ZeroBlock-секции маршрутиризации?

---

**2026-04-01T07:33:04 | Камиль**
А есть тут кто активно использует codex/claude и сидит на zeroblock? Прям активно, многочасовые сессии. 
Покажите пожалуйста свои настройки zero. Спустя 5 минут активной работы ip палится. Yacd смотрю, похоже какие-то запросы не попадают, либо каких-то доменов нет.

---

**2026-04-01T09:18:32 | Роман**
Support Fresa, неделя думаю прошла, уважаемый zeroblock выйдет?

---

**2026-04-01T09:20:49 | ㅤㅤ**
То есть ZeroBlock сейчас работает со списками в формате JSON? 

В папке /tmp/zeroblock/rulesets имеется весомый список remote-ads-adlist.srs
Каким образом в ZB отлажена работа с блокировкой рекламы используя .srs?

---

**2026-04-01T09:26:28 | ㅤㅤ**
Второго вопроса не было. Есть некий список remote-ads-adlist.srs на 1,3 мб. Как его использовать?

И судя по наличию списков в памяти ZeroBlock использует локальные файлы, которые создаются скриптами?

---

**2026-04-01T09:30:51 | Routerich**
что значит какой пакет? директория /tmp/zeroblock/rulesets создаётся и курируется зероблоком. то, что вы ему кормите, то там и лежит

---

**2026-04-01T09:47:31 | Routerich**
Здравствуйте.
по умолчанию не стоят VPN никакие.
для этого есть скрипт 5 или ZeroBlock

---

**2026-04-01T10:14:09 | Роман**
recraft.ai
azurefd.net

Эти домены в список пользовательских доменов zeroblock/podkop.

---

**2026-04-01T10:19:09 | Фотограф Александр Москаленко**
zeroblocka у меня нет на сколько я понимаю

---

**2026-04-01T10:49:56 | Anna Bagler**
А теперь и диагностику zeroblock покажите. Смените пару основного DNS и bootstrap в настройках самого zeroblock.

---

**2026-04-01T11:03:55 | Роман**
Уважаемый zeroblock научился ходить? Пусть выходит 😁

---

**2026-04-01T11:05:49 | Роман**
Ещё раз. Что в подкопе, что в zeroblock используется точечная маршрутизация, то что указано идёт в прокси - всё остальное напрямую. 
Если вы сами не внесли ру домены в подкоп - они идут без прокси. 
Вангую Russia Outside выбран.

---

**2026-04-01T11:41:02 | Bullet for my valentine Poison**
Просто ожидайте. Все получат Zeroblock когда Fresa будет в нем уверен) Иначе потом будут стенания - "ОНО СЛОМАЛОСЬ", "ИНСТА НЕ РАБОТАЕТ", "НА УЛИЦЕ ДОЖДЬПОШЕЛ", "FRESA МЕНЯ ИГНОРИТ"!😂

---

**2026-04-01T12:15:37 | Anna Bagler**
А обновите zeroblock через Пакеты, почистите кэш браузера и посмотрите.

---

**2026-04-01T12:46:55 | Den**
Адепты Zeroblock призывают демона )))

---

**2026-04-01T12:51:43 | Nick**
Ставь zeroblock

---

**2026-04-01T13:59:25 | Роман**
Тогда что то своё приколачивайте, а то - нет оперы - нет zeroblocka. Странная зависимость. А если у человека просто опера не доступна? Что тогда?

---

**2026-04-01T16:40:12 | Роман**
В zeroblock выбран список messengers, всё работает.

---

**2026-04-01T16:40:51 | Marseille Gaysin**
Face time  есть? Есть поддержка  vless ? Zeroblock

---

**2026-04-01T18:22:29 | Routerich**
Здравствуйте.
Zeroblock тему смотрите

---

**2026-04-01T18:34:40 | Marseille Gaysin**
zeroblock2 для arch mipsel_24kc нету ?

---

**2026-04-01T18:35:46 | Marseille Gaysin**
zeroblock2 для процессора arch mipsel_24kc он есть?

---

**2026-04-01T18:41:39 | Marseille Gaysin**
установочный файл ipk  для этого процессора Zeroblock можно найти?

---

**2026-04-01T19:08:36 | Роман**
Установлен zeroblock, свои сервера, выбраны все списки кроме CDN и socials, более ничего.

---

**2026-04-01T19:21:58 | Дмитрий**
Добрый вечер. Снова отвалился xbox. Поскажите плиз, что и куда нужно прописать? Спасибо(zeroblock)

---

**2026-04-01T19:37:34 | Артем Михайлов**
Подскажите,  как ускорить прогрузку картинок в телеграме?

Установлен ZeroBlock.
Сообщения норм загружаются,а с картинками беда.
Включаешь впн, все моментально загружается.

---

**2026-04-01T22:12:19 | ㅤㅤ**
Терзают сомнения, что за полдня простуда миновала, но все же надеюсь, что зараза подкосила не всех модераторов. 
В папке /tmp/zeroblock/rulesets/remote-ads-adlist.srs существует некий рекламный список в формате sing-box rule-set. Оптимальный вариант его использования для меня - секция ADS/Block. Но каким образом ZB указать на ссылку во внутренней памяти? Иначе, откуда тянется этот список и для чего именно там лежит?

---

**2026-04-01T22:15:40 | Роман**
Уважаемого zeroblocka релизнет?

---

**2026-04-01T22:38:37 | Igor Ivanov**
А планируется? :)
ну вот захотелось например попробовать zeroblock на openwrt 25.12 , а там ipk не поставить, ну и мало ли чего еще вздумается попробовать:)

---

**2026-04-01T22:54:25 | Ivan Num**
Что то nnmclub на zeroblock тупит

---

**2026-04-01T23:32:46 | Роман**
Актуальный ответ, устанавливайте zeroblock и импортируйте vless, дел на пять - десять минут.

---

**2026-04-02T00:14:19 | Артём Фомин**
Пустил YouTube через ZeroBlock/awg10 и всё залетало. Не хочет через Zapret2 нормально работать. Видео грузится очень долго и постоянно зависает.

---

**2026-04-02T00:21:02 | Роман**
Ещё раз, то что откроет прокси (подкоп/zeroblock) - не откроет zapret (грубо говоря). Точечная маршрутизация и дурение разные вещи. Списки из подкопа никак не помогут в запрете.

---

**2026-04-02T00:26:57 | Артём Фомин**
Вместо Podkop ставь ZeroBlock. Сделай автонастройку с нужными компонентами, здесь где-то была видеоинструкция, и никакие сторонние VPN не нужны будут

---

**2026-04-02T07:28:58 | Routerich**
Здравствуйте.
Да, что-то одно должно быть.
У Zeroblock функционал шире.

---

**2026-04-02T08:53:03 | Routerich**
Здравствуйте.
Сброс и затем установка Zeroblock

---

**2026-04-02T09:10:41 | Роман**
Из zeroblock Ютуб убрали?

---

**2026-04-02T09:22:05 | ᚢᚹᛟᛈᛠᛋᛠᛊ ᛖᛊᚺᚱ**
Всем хай, хочу щас снести у себя подкоп, и накатить zeroblock
Будет ли работать oculus при этом способе обхода блокировок?

---

**2026-04-02T09:24:19 | Роман**
Всё зависит от настроек, никакой волшебной кнопки (чтобы всё работало) нет. Podkop/zeroblock лишь инструменты для проксирования трафика, как настроите - так и будет.

---

**2026-04-02T09:37:42 | Роман**
Приветствую, о любезный творец, ибо сказано: «Благословен грядущий во имя Господне», однако скажи, ныне ли, в сей день, явится почтенный Zeroblock?

---

**2026-04-02T10:03:38 | Дмитрий З**
После logread | grep -i TrustTunnel видено вот это 

Thu Apr  2 09:48:33 2026 user.notice trusttunnel-TT: 02.04.2026 06:48:33.087744 INFO  [7855] SOCKS5_LISTENER socks5_listener_start: Listening on 127.0.0.1:20100
Thu Apr  2 09:48:33 2026 user.notice trusttunnel-TT: 02.04.2026 06:48:33.087761 INFO  [7855] VPNCORE start_listening: [0] Client has been successfully prepared to run
Thu Apr  2 09:48:33 2026 user.notice trusttunnel-TT: 02.04.2026 06:48:33.087971 INFO  [7843] VPNCORE vpn_listen: [0] Done
Thu Apr  2 09:48:33 2026 user.notice trusttunnel-TT: 02.04.2026 06:48:33.195490 INFO  [7855] VPNCORE pinger_handler: [0] Using endpoint: name=XXX.xyz, address=2.27.XX.XX:443, relay=none, ping=52ms
Thu Apr  2 09:48:33 2026 daemon.info zeroblock[7771]: [config_builder] TrustTunnel launched with 1 sections (port wait deferred)
Thu Apr  2 09:48:33 2026 user.notice trusttunnel-TT: 02.04.2026 06:48:33.275080 INFO  [7855] VPNCORE raise_state: [0] VPN_SS_CONNECTED
Thu Apr  2 09:48:33 2026 user.notice trusttunnel-TT: 02.04.2026 06:48:33.275143 INFO  [7855] TRUSTTUNNEL_CLIENT_APP operator(): Successfully connected to endpoint
Thu Apr  2 09:48:33 2026 user.notice trusttunnel-TT: 02.04.2026 06:48:33.322533 INFO  [7855] UPSTREAM_MUX child_upstream_handler: [3] Error on upstream id=0 is fatal, closing all upstreams: (5) Authorization Required
Thu Apr  2 09:48:33 2026 user.notice trusttunnel-TT: 02.04.2026 06:48:33.322646 INFO  [7855] VPNCORE raise_state: [0] VPN_SS_DISCONNECTED
Thu Apr  2 09:48:33 2026 user.notice trusttunnel-TT: 02.04.2026 06:48:33.323506 INFO  [7843] VPNCORE vpn_stop: [0] ...
Thu Apr  2 09:48:33 2026 user.notice trusttunnel-TT: 02.04.2026 06:48:33.323707 INFO  [7843] VPNCORE vpn_stop: [0] Stopping event loop...
Thu Apr  2 09:48:33 2026 user.notice trusttunnel-TT: 02.04.2026 06:48:33.323964 INFO  [7843] VPNCORE vpn_stop: [0] Event loop has been stopped
SKIPPED 
Thu Apr  2 09:48:33 2026 user.notice trusttunnel-TT: 02.04.2026 06:48:33.331144 INFO  [7843] VPNCORE vpn_stop: [0] Done
Thu Apr  2 09:48:33 2026 user.notice trusttunnel-TT: 02.04.2026 06:48:33.331160 INFO  [7843] VPNCORE vpn_close: [0] ...
Thu Apr  2 09:48:33 2026 user.notice trusttunnel-TT: 02.04.2026 06:48:33.331215 INFO  [7843] VPNCORE vpn_close: [0] Done
Thu Apr  2 09:48:33 2026 daemon.info zeroblock[7771]: [singbox_gen] Section TT: TrustTunnel socks outbound (port=20100)
Thu Apr  2 09:48:42 2026 daemon.err zeroblock[7771]: [config_builder] TrustTunnel last SOCKS5 port 20100 not ready
Thu Apr  2 09:48:42 2026 daemon.info zeroblock[7771]: [config_builder] TrustTunnel endpoint 2.27.XX.XX: mark 0x40000000 + return (section TT)

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

**2026-04-02T11:44:58 | A V**
А чего мне zeroBlock даст?

---

**2026-04-02T12:44:56 | karat**
Подскажите пожалуйста, в Zeroblock очередность обработки секций начинается с верхней секции, а как   выставлять приоритет  обработки в секциях Podkop?

---

**2026-04-02T13:15:22 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-02T13:29:38 | Anna Bagler**
Сброс возвращает первозданный вид вашему роутеру. Пакеты обновляются через Система - Пакеты. Если будете через ASU собирать прошивку, то сброс - возврат к начальным настройкам после ASU.
Eще раз, Система - Пакеты, поверх можно ставить zeroblock, 2 файла, кэш браузера обязательно чистить.

---

**2026-04-02T13:34:49 | Anna Bagler**
А в подкоп ловля всего может не сработать, переходите на zeroblock.

---

**2026-04-02T13:36:18 | karat**
В Zeroblock они просто перетягиваются в подкоп я не понял как это делать.

---

**2026-04-02T13:38:11 | karat**
Да у меня второй роутер на zeroblock, но в podkop сегодня лучше идет телеграм, решил с ним немножко познакомится

---

**2026-04-02T13:52:16 | karat**
Спасибо, но я так понял что zeroblock работает по этим же списка, но здержка в соединении намного больше

---

**2026-04-02T13:58:26 | Роман**
Бравл в списке games. Как и роблокс. Но у вас роблокс через запрет 1. Выход: пустить всё в прокси через zeroblock, но роблокс работать через оперу не будет. Вывод: хотите все игры - используйте свои сервера 😁

---

**2026-04-02T14:15:05 | Роман**
Какие списки выбраны в zeroblock?

---

**2026-04-02T14:18:37 | Routerich**
Здравствуйте.
Он может не корректно работать если есть Podkop.
Ставьте zeroblock и ттам родительский контроль есть.

---

**2026-04-02T15:18:51 | Михаил**
Здравствуйте! Никак не могу разобраться как добавить конфиг shadowsocks в zeroblock

---

**2026-04-02T15:34:31 | Александр**
Назрел очередной вопрос,установлен zeroblock zapret2.Нужно зайти на сайт xiaomi.eu,открывается только при включении впн в браузере.Пните в нужном направлении где что включить ,прописать,что бы был свободный доступ.

---

**2026-04-02T17:29:17 | Vladislav Nadezhdin**
Zeroblock-Настройки-DNS
Во вкладке сервер вбивать xbox-dns.com вместо Гугла, верно?
Или лучше это делать в одном из маршрутов секции(opera,awg10)?

---

**2026-04-02T17:37:13 | Bullet for my valentine Poison**
Хороший подкоп, это Zeroblock?🤨

---

**2026-04-02T17:56:45 | Bullet for my valentine Poison**
Я б за Fresa голосовал. Он Zeroblock с Zapretom2 нашаманил.😂

---

**2026-04-02T18:33:29 | Routerich**
Здравствуйте.
Начать со сброса и решить, что вам нужно Podkop или Zeroblock

---

**2026-04-02T18:41:03 | Anna Bagler**
Cброс зубочисткой или из меню роутера. Лучше zeroblock и в нем галочка на запрет2.

---

**2026-04-02T18:41:21 | Routerich**
Сброс полный, всего роутера.
Лучше Zeroblock по инструкции из темы.

---

**2026-04-02T18:52:16 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-02T19:13:01 | QweNo HarD**
zeroblock ставит из поиска роутера или загружать из поста ТГ r53?

---

**2026-04-02T19:26:21 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-02T20:01:48 | Anna Bagler**
Теперь по инструкции ставьте zeroblock.
Для обхода БС вам нужен будет vpn c обходом БС, тогда ссылку сможете закинуть в роутер.

---

**2026-04-02T20:05:19 | Anna Bagler**
Скрипт №5 из закреплённых сообщений Интернет без границ делает все за вас. Если подкоп ещё не ставили, ставьте zeroblock.

---

**2026-04-02T20:11:05 | Роман**
Злравствуйте. Что значит через морду? Есть поддержка протокола amnezia 2.0 в роутере. Если вы про управление через веб интерфейс - есть. Реализовано через добавление нового интрерфейса и установку zeroblock.

---

**2026-04-02T20:13:00 | Anna Bagler**
Zeroblock поставили?

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

**2026-04-02T21:52:59 | Iceking**
Отключил в ZeroBlock, оставил в Zapret2 - не работает
Отключил в Zapret2, оставил в ZeroBlock - не работает
Включил в Zapret2 и ZeroBlock - YouTube открывается, но с рекламой
Куда смотреть?

---

**2026-04-02T21:55:51 | Iceking**
Отключил еще раз в секции с квн в ZeroBlock еще раз - заработало О_о

---

**2026-04-02T22:06:47 | Iceking**
В списке Awg в ZeroBlock убрал YouTube и он заработал. Единственное что - не могу залогиниться, пишет «Вы вышли из аккаунта», пытаюсь нажать на аккаунт - не получается. Хотел зайти через accounts.google.com - ввожу адрес почты, нажимаю «Далее», ничего не происходит. Пробовал в Сафари и Яндекс.браузере. Что может блокировать это?

---

**2026-04-02T22:10:03 | Роман**
Этим вы ничего не измените. В бете последний подкоп, в пятом 0.7.10. Разницы нет. Я бы на вашем месте сделал сброс до заводских настроек и установил zeroblock.

---

**2026-04-02T22:28:29 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-02T22:37:53 | Iceking**
Понял, спасибо, почему-то через Zapret2 вообще перестал открываться YouTube, работает только через ZeroBlock

---

**2026-04-02T22:44:05 | Iceking**
Да моя ошибка 100%. Зашел ZeroBlock, секции, квн, списки, убираю галочку YouTube
Zapret2. youtube, rr_youtube со стандартными настройками включены. Еще включено rr_blackhole
Так YouTube работает, только не могу залогиниться (см.видео)

---

**2026-04-02T23:10:51 | Anna Bagler**
Сброс и zeroblock. Должно быть стабильнее.

---

**2026-04-02T23:12:13 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-02T23:18:17 | Роман**
Вы включаете полный впн на устройстве, весь трафик лезет в него.  Тут точечная маршрутизация. Засуньте в zeroblock свой стабильный сервер и проблем не будет.

---

**2026-04-02T23:20:21 | Артем Погодин**
А через zeroblock трафик будет весь через настроенный сервер идти?

---

**2026-04-02T23:23:07 | Alon Zone**
После того как установил zeroblock , zapret 2 , еще что то надо делать ?

---

**2026-04-02T23:24:17 | Kiss_My_Axe**
Никакие для обычного. Для необычного ZeroBlock, или подкоп.

---

**2026-04-02T23:25:57 | Anna Bagler**
Полный мануал по zeroblock изучаем из соответствующей темы.
Пока просто проверьте работу запрещенки, если все по инструкции сделали.

---

**2026-04-03T00:16:57 | Iceking**
Как обновить пакеты амнезии?
Сделал новый интерфейс амнезии Англия (Мозилла инкогнито). Сделал новую секцию с этим интерфейсом в ZeroBlock, там активировал список YouTube. Смог залогиниться, 12 минут посмотрел видео, рекламы нет. Значит все нормально получилось?

---

**2026-04-03T00:35:13 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-03T00:45:25 | Kiss_My_Axe**
https://raw.githubusercontent.com/KharunDima/whatsapp-lists/main/results/domains.txt

Эту ссылку ставить в ZeroBlock, или подкоп. (см. скрины).

---

**2026-04-03T09:29:36 | Anton Alyx**
Не могу Zeroblock установить, выдает ошибку:

---

**2026-04-03T09:57:33 | Артем Погодин**
Помогите разобраться с блокировкой ChatGpt по недоступности в регионе

Я вчера настроил ZeroBlock по инструкции 
Добавил свою прокси, чтобы через него направлять список AI. 
Но захожу на телефоне в приложение - получаю "...недоступен в вашем регионе". В вебе +- тоже самое

При том, что если включить ту же прокси в клиенте ВПН - работает отлично

Что-то донастроить может надо..

---

**2026-04-03T10:52:04 | Артем Погодин**
Теперь другая проблема))
Такого не было с podkop'ом

Есть корпоративный VPN через checkpoint
Вот он не хочет подключаться с включенным zeroBlock. Отключаю - подключается корпоративный

Куда-то что-то в исключения может надо?

---

**2026-04-03T11:00:05 | Роман**
Мне стыдится нечего, был подкоп с zeroblock для тестов. Зато я в стикерах не увековечен 😁

---

**2026-04-03T11:09:29 | Anna Bagler**
Если сбросили, переходите на zeroblock. Сделайте по краткой инструкции https://t.me/routerich/394153/405571

---

**2026-04-03T11:27:42 | Bullet for my valentine Poison**
Первый вариант, зайти в система-пакеты. Вписать слева в фильтр zeroblock и нажать обновить списки. Закрыть окно с логом. Появятся пакеты зеро и нажать справа кнопку обновить. Либо установить Asu(в теме Asu закреп с инструкцией) и обновлять все пакеты сразу, с сохранением настроек.

---

**2026-04-03T11:31:07 | Bullet for my valentine Poison**
Слева строка фильтр. Туда Zeroblock вписать

---

**2026-04-03T11:31:24 | Роман**
Фильтр zeroblock

---

**2026-04-03T11:31:57 | Anna Bagler**
На странице zeroblock вкладка Секции маршрутизации. Галочку автозагрузки секций ставили?

---

**2026-04-03T11:40:01 | Anna Bagler**
Изучите списки в закрепе темы по Zeroblock. Если что, вносите домены. Все схоже с подкопом.

---

**2026-04-03T12:58:18 | A V**
После установки zeroBlock перестала выполняться opkg update.
root@RouteRich:~# opkg update
Collected errors:
 * opkg_conf_load: Could not lock /var/lock/opkg.lock: Resource temporarily unavailable.
root@RouteRich:~# ps | grep opkg
15249 root      1800 S    opkg update
15355 root      8140 S    wget -q -O /tmp/opkg-bjOoHO/Packages.gz ht
17792 root      1336 S    grep opkg
root@RouteRich:~#

И висит в таком состоянии часами. Куда копать?

---

**2026-04-03T13:25:18 | A V**
Отключал zeroBlock в веб интерфейсе, не помогает.

---

**2026-04-03T13:27:40 | A V**
Я не сказал, что в zeroBlockе дело. Я сказал, что после установки заметил.

---

**2026-04-03T13:31:34 | A V**
Мы, вероятно, по разному понимаем. После установки zeroBlock, независимо, включён он, или отключён в веб-интерфейсе, происходит такая странная фигня. Вот так правильно.

---

**2026-04-03T13:42:20 | Evgen**
я спрашиваю про подкод, а не zeroblock

---

**2026-04-03T13:48:52 | Роман**
Что можно качать через zeroblock на 20 гигов?

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

**2026-04-03T15:17:09 | Василий**
Подскажите, Zeroblock не умеет работать с приложениями? Нет возможности указывать приложуху, а не домен или ip?

---

**2026-04-03T15:22:10 | Vlad Maker**
Добрый день. Поставил ZeroBlock и Zapret2 пару дней назад, дефот настройки. Все работало без проблем. 
Сегодня не грузит Ютуб в браузере ПК и Телефона(в приложении работает). После перезагрузки роутера в Хроме на ПК какое то время работает. Хэлп.

---

**2026-04-03T15:54:51 | Anna Bagler**
Сейчас актуальнее zeroblock, для него скрипта нет. Не хотите актуальнее, https://t.me/routerich/3845/245550

---

**2026-04-03T15:56:58 | Akira Yamaoka**
Привет. А где почитать про zeroblock и zapret2? Ну что это? чем отличается от скрипта #5, в каких случаях что лучше использовать? Есть такое описание где то?

---

**2026-04-03T16:16:19 | Роман**
Можете не трогать раз работает. В скором времени должны 25 прошивку выпустить и zeroblock обновлённый, можете дождаться и обновиться.

---

**2026-04-03T16:42:09 | Андрей**
Господа, здравствуйте. Подскажите, пожалуйста а решается ли через zeroblock блокировка Google meet? Поиском не нашлось ничего

---

**2026-04-03T16:58:21 | Андрей**
А через что у zeroblock проксируются коннекты? Т.к. xray рвет длительные коннекты и это ломает звонки

---

**2026-04-03T17:54:47 | Вячеслав**
Добрый день. Купил роутер, в zeroblock закинул подписку квн, выбрал списки нужные. Всё что надо работает через квн. Вопрос такой, нужно ли что-то добавлять в исключения чтобы всё остальное шло напрямую? Или оно автоматом туда идёт?

---

**2026-04-03T17:56:07 | Routerich**
Все что не добавлено в Zeroblock идёт напрямую, без обходов.

---

**2026-04-03T18:01:35 | Gomer Simpson**
Гм.. Список AI в ZeroBlock в секции proxy и список CDN Google там же. Но CDN гугла добавляю только для notebooklm. Закончил - список убрал.

---

**2026-04-03T18:02:32 | Роман**
zeroblock со всеми списками кроме CDN, используются свои сервера.

---

**2026-04-03T18:34:48 | Александр Камышлейцев**
Печально очень. Тогда может подскажите, вот в инструкции есть подпункт 2 в  пункте 3.3: Перейдите в Службы -> ZeroBlock -> Автонастройка. А у меня нет ZeroBlock в Службы. Прошивка RouteRich 24.10.5 r29087-d9c5716d1d RR-3.9.0 / LuCI openwrt-24.10 branch 26.039.68875~ec3d818

---

**2026-04-03T18:35:43 | Роман**
https://t.me/routerich/80283/468513 - полный мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-03T18:52:24 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-03T18:57:57 | Kiss_My_Axe**
Смотрите, есть решение - ZeroBlock - списки которого уже полнее списков подкопа.
В настоящий момент вы не решаете проблему (вашу проблему), вы тираните ТП на предмет "А я хочу на подкопе! Делайте мне!".

---

**2026-04-03T19:23:26 | Anna Bagler**
Засуньте vless в zeroblock. warp в интерфейс на роутере и привяжите к zeroblock в другой секции.

---

**2026-04-03T19:43:28 | Loraool**
а в чем разница скрипт 5 и zeroblock? Что лучше ставить?

---

**2026-04-03T19:46:54 | Роман**
zeroblock со своими серверами, ничего дополнительного.

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

**2026-04-03T20:17:00 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-03T20:47:14 | Loraool**
подскажите, пожалуйста, установил zeroblock, тг и ютуб работают, чатгпт говорит что не доступен в регионе, где надо галочку поставиь или прописать что-то?

---

**2026-04-03T20:57:47 | HiLLL**
файл zeroblock /etc/config/

---

**2026-04-03T21:19:18 | Роман**
Можете dns на 9.9.9.9 сменить в настройках zeroblock, а так всё в порядке.

---

**2026-04-03T21:32:11 | Anna Bagler**
Обновлять прошивку и запускать скрипт №5 или ставить zeroblock.

---

**2026-04-03T22:48:06 | Grigory**
И пользуясь случаем, существует ли подобная инструкция по zeroblock?

---

**2026-04-03T22:52:19 | Grigory**
Хорошо хорошо, лагает не zeroblock, а сайты подвисать начинают будто dial up инет

---

**2026-04-03T22:58:04 | Роман**
Ну вы и наворотили. Сносить всё сбросом и ставить (внимательно читая) zeroblock.
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-03T23:01:58 | Роман**
Ну тогда приобретайте что-то платное и закидывайте в zeroblock - раз бесплатное не работает, окулус затем в полное прокси.

---

**2026-04-03T23:52:51 | Роман**
Работает запрет2 и zeroblock.

---

**2026-04-04T00:03:35 | Роман**
Для игры в lineage2ertheia добавьте эти домены и ip в список пользовательских доменов/ip в zeroblock/podkop
lineage2ertheia.com
yani.tv
ajay.app
cloudfront.net
lineage2splendor.com
ip-51-255-64.eu

188.114.97.11
172.67.191.217
51.255.64.201
13.33.216.158
13.33.216.53
188.114.96.11
172.67.191.217
112.175.192.62
Можно ещё добваить CDN:Cloudflare
#games

---

**2026-04-04T03:30:40 | Артем Погодин**
Я уже далеко ушел в преисполнении
Сбросил до заводских, поднял zeroblock, реализовал маршрутизацию только заблокированного трафика и добавил в исключения ip рабочего впна, иначе конфликтовало
Вроде часа 3 схема работала

---

**2026-04-04T06:21:46 | Константин**
ДД. Куча тем куча сообщений. Немного не въезжаю. До RR пользовал самопрошитый девайс с запретом плюс подкоп. Что ставит 5й скрипт? Ставит zeroblock или zeroblcok это отдельная тема?

---

**2026-04-04T11:05:51 | Роман**
Если будете пользоваться обходами ставьте zeroblock , там есть родительский контроль.

---

**2026-04-04T12:26:26 | Dmitriy**
а может кто подсказать , можно ли на телефоне реализовать аналогичную схему как на роутериче с zapret2 для ютуба + zeroblock ? просто одновременно включить сразу vpn клиент и byebyedpi нельзя или это проще через на роутере накатить и через tailscale?

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

**2026-04-04T13:40:22 | Anna Bagler**
Если можете вытащить прямую ссылку vless из happ, то можете пробовать. С подписками работает zeroblock, но будет ли воспринимать вашу, надо смотреть.

---

**2026-04-04T14:08:52 | Loraool**
Добрый день. Вопрос, увидел в пакетах "Adguard home". Насколько эффективно он работает? Или лучше на устройство ставить блокировщик рекламы, а не на роутер. Не будет ли конфликтов в zeroblock+zapret2?

---

**2026-04-04T14:20:36 | Назар Назаров**
странно, что после обновления пакетов zeroblock в списке ниже не появляется

---

**2026-04-04T14:25:09 | Anna Bagler**
В поле фильтра zeroblock и ok. И скрин.

---

**2026-04-04T14:57:45 | ㅤㅤ**
Решение найдено для игры MK1, эти домены в zeroblock/podkop:

api.wbgames.com
wb-hydra.wbgames.com
mortalkombat.com
amazonaws.com.
bugs.wbgames.com
telemetry.wbgames.com
cdn.wbgames.com

Плюс скопировать все cidr:

https://github.com/123jjck/cdn-ip-ranges/blob/main/aws/aws_plain_ipv4.txt

Взято из соседнего чата itdog.
#games

---

**2026-04-04T15:03:35 | Назар Назаров**
уже сделал, спасибо! Автонастройку пропускаем дальше в zeroblock?

---

**2026-04-04T15:06:21 | Anna Bagler**
Да, дальше zeroblock.

---

**2026-04-04T15:14:45 | Anna Bagler**
Cнимаем галочки с тех секций, что идут по умолчанию. Применить. Создаём свою секцию типа прокси, дальше выбираем конфигурацию URL и туда свой vless. Выбираем списки. Применяем. Проверяем. В теме по zeroblock есть полный мануал.

---

**2026-04-04T15:14:55 | Дмитрий**
Добрый день, поскажите плиз. 
Не могу нажать крестик и убрать из секции полную маршрутизацию. Zeroblock -opera.(На другом роутере все ок, спокойно можно добавить и убрать) Спасибо

---

**2026-04-04T15:23:34 | Виталий Александрович**
Подскажите пожалуйста, в zeroblock куда именно добавлять? 
В opera или awg10  ?

---

**2026-04-04T15:50:55 | Anna Bagler**
Если вы всего этого не делали, то вам надо сбросить роутер, лучше прошить свежей прошивкой и сделать настройку с нуля. И поставить zeroblock. Если сами ставили, то надо https://t.me/routerich/173678/449069

---

**2026-04-04T17:39:09 | A_che ngel 🐮**
Всем привет)
Добавил в zeroblock свою секцию маршрутизации через поднятый vless. Добавил туда 2ip вот таким способом. Однако если захожу на 2ip все еще не через впн. Может что-то не так делаю?

---

**2026-04-04T17:43:53 | Роман**
В панели управления zeroblock.

---

**2026-04-04T19:53:57 | Anna Bagler**
Zeroblock - Секции маршрутизации.

---

**2026-04-04T19:59:36 | Александр**
А только у меня косяк с сайтом themoviedb.org? Установлена последня прошивка 24.10.5 и zeroblock 0.7.2-r53 если перейти на сайт themoviedb.org то открывается интерфейс роутера. А мне нужен этот сайт для kodi с podkop такой проблемы не было.

---

**2026-04-04T20:11:14 | Максим**
Добрый вечер, подскажите пожалуйста если не сложно. Установил zeroblock через пакеты последнюю версию, все включил во вкладке автонастройка(автозагрузка секций и стратегий тоже стоит), но awg10 n/a, opera показывает 300мс
Что то не так сделал?

---

**2026-04-04T20:37:11 | Роман**
Телегу в прокси. Устанавливайте - кроме запрета 2.
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-04T21:11:02 | Vlad**
В закрепе темы Zeroblock

---

**2026-04-04T21:32:49 | Anna Bagler**
opera не хочет шевелиться, попробуйте перезапустить ее руками в Система - Автозапуск. И диагностику самого zeroblock покажите. В запрет2 попробуйте подобрать другую стратегию.

---

**2026-04-04T22:10:12 | Константин Волчек**
Роман, у меня похожая проблема, только не работает дискорд, а не ютуб. До этого делал стандартную установку ZeroBlock + Zapret 2

---

**2026-04-04T22:14:50 | Роман**
Это запрет, а не zeroblock. Будьте внимательнее.

---

**2026-04-04T22:16:41 | Константин Волчек**
вроде да. ютуб и дискорд в zeroblock выключал

---

**2026-04-04T22:17:14 | Роман**
Что вы мне запретом тычете? ZEROBLOCK откройте.

---

**2026-04-04T22:41:17 | Anna Bagler**
Зачем вы ставите подкоп, если есть zeroblock?

---

**2026-04-04T22:53:50 | Роман**
Тогда уже уважаемый zeroblock выйдет, 25.10 на подходе.

---

**2026-04-04T22:55:07 | Роман**
Верно, зачем он - когда есть уважаемый zeroblock?

---

**2026-04-04T23:32:06 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-04T23:52:37 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-05T01:24:19 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock
Это. Автонастройку (если есть свой сервер) можете не делать. Просто создаёте секцию, вписываете впн, выбираете списки.

---

**2026-04-05T01:43:09 | Роман**
Устанавливайте zeroblock из пакетов и настраивайте.

---

**2026-04-05T01:55:02 | Роман**
Zeroblock. Изучите немного то, что вы установили. Секция авг.

---

**2026-04-05T01:57:22 | Anna Bagler**
Секции маршрутизации в zeroblock, awg, cписок мессенджеров.
По discord есть стратегии в теме zapret2. Можете его отключить и остановить. Вернуть просто запрет и ваши стратегии.

---

**2026-04-05T07:32:25 | viktr**
Вводим в окне "Фильтр" (слева) Zeroblock. Внизу должны появиться два пакета: Zeroblock и luci-app-zeroblock.
 не поЯвля.тся в пакетах ни зеро не люся

---

**2026-04-05T08:38:16 | Константин Волчек**
сделал все по основному гайду zeroblock + zapret2

---

**2026-04-05T08:38:35 | Константин Волчек**
в zeroblock выключил ютуб и дискорд

---

**2026-04-05T09:29:38 | Константин**
Подскажите пожалуйста, если установлен Zeroblock и Zapret 2 то пс 5 полную маршрутизацию сделать в оперу или aw10?
Спасибо

---

**2026-04-05T10:23:22 | Роман**
Присвоить постоянный ip в обзоре, выбрать ip телевизора в секции zeroblock.

---

**2026-04-05T10:38:55 | Дмитрий**
я не нашел вкладку как у Вас ZeroBlock - zbs. у меня только такие вкладки

---

**2026-04-05T10:41:56 | Evgeny**
zeroblock работает только на роутеричах или на других роутерах может работать?

---

**2026-04-05T10:51:51 | D I**
Уважаемые, вопрос а в чем принципиальная разница Zapret(2)/ZeroBlock/PodKop? и что выбрать, если ничего не стоит/стояло до?

---

**2026-04-05T10:53:09 | Nick**
Zeroblock  и zapret2
В комплекте

---

**2026-04-05T10:56:04 | JustKosha**
zeroblock awg warp попробуй этим поднять

---

**2026-04-05T11:30:06 | Khamzat**
Всем доброго дня!
Не подскажете пожалуйста, zeroblock с mwan3 невозможно подружить?
2 витые пары от разных провайдеров на квартире, потребовалось вторую витую пару к RR подключить

Делал настройку mwan3 по инструкции с сайта openwrt, коннект по двум wan портам в итоге был, но zeroblock начал рестартиться каждые секунд 15-20, побороть это я не смог и пока откатил все настройки, что я делал для mwan3 с удалением исходного пакета

---

**2026-04-05T12:06:54 | Марат**
Привет всем. А чет амнезия отвалилась. Ночью работало, ща уже нет. 
zeroblock[2543]: [awg_configurator] No working endpoint found after testing 4 endpoints with 3 retries each

---

**2026-04-05T12:13:11 | HiLLL**
запустите в терминале zeroblock awg warp

---

**2026-04-05T12:46:44 | Routerich**
/tmp/zeroblock/rulesets
там лежат списки, проверяйте

---

**2026-04-05T12:51:03 | Navisal**
на роутере Routerich штатными средствами поднят OpenVPN сервер, подключено несколько клиентов, которые прекрасно ходят в инет через Zeroblock и Zapret2.
Вопрос: Как можно посмотреть статус OpenVPN клиентов? Желательно через Luci, через морду какую-нибудь ) Ну или просто командой

---

**2026-04-05T12:53:22 | Anna Bagler**
Если у вас на роутере пока ничего нет, ставьте zeroblock
https://t.me/routerich/394153/405571

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

**2026-04-05T14:24:44 | Aleksandr Khandoga**
Ребят, всем привет! Недавно приобрел роутер. Поставил из коробки, ничего не менял, не считая первоначальной настройки (на удивление, почти все заработало как надо - большой респект за это). Но есть моменты, которые хотелось бы донастроить. Например, на двух ноутах (Win10, один через wifi, другой по шнуру) и на двух телефонах (android) через wifi ютуб запускается, а телега - нет. Подскажите, пожалуйста, можно ли это полечить и где можно найти\почитать мануал (желательно, для совсем новичков). Правильно ли понимаю, что надо ставить\настроить zeroblock (нашел ссылку на него в обсуждениях сообщества)? Спасибо!

---

**2026-04-05T14:29:15 | Anna Bagler**
Да, на чистый роутер ставьте zeroblock. Потом смотрите, что и где не работает.

---

**2026-04-05T14:38:13 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-05T14:45:49 | Олег Каргаев**
3. Вводим в окне "Фильтр" (слева) Zeroblock. Внизу должны появиться два пакета: Zeroblock и luci-app-zeroblock.

---

**2026-04-05T14:46:41 | D S**
https://t.me/routerich/394153 ветка по zeroblock

---

**2026-04-05T16:28:20 | Anna Bagler**
Zeroblock - точечная маршрутизация, в запрет 2 можно засунуть ютуб и дискорд. В запрет попробовать некоторые игры. Вам что надо?

---

**2026-04-05T16:42:23 | Anna Bagler**
Есть полный мануал по zeroblock.

---

**2026-04-05T17:04:03 | Anna Bagler**
У вас стоит zeroblock или подкоп?

---

**2026-04-05T17:25:30 | Никита**
Всем добрый вечер
Сделал всё строго по гайду ZeroBlock — в целом всё работает отлично. Поставил свой VLESS (локация Польша) + штатный AWG10. В конфиге VLESS прописал домены openai и chatgpt (через rules/geosite).
Проблема такая: ChatGPT (и openai.com) нормально работает везде — на Windows, Android, Mac, в браузере и в приложении.
А вот на iPhone совсем не заходит. в Safari работает, а  в официальном приложении ChatGPT нет.

Кто-нибудь сталкивался с похожим? Подскажите, пожалуйста, в чём может быть дело и что в первую очередь проверить.
Заранее огромное спасибо! 🙏

---

**2026-04-05T17:25:58 | Никита**
Всем добрый вечер
Сделал всё строго по гайду ZeroBlock — в целом всё работает отлично.
Поставил свой VLESS (локация Польша) + штатный AWG10.
В конфиге VLESS прописал домены openai и chatgpt (через rules/geosite).
Проблема такая:
ChatGPT (и openai.com) нормально работает везде — на Windows, Android, Mac, в браузере и в приложении.
А вот на iPhone совсем не заходит. в Safari работает, а  в официальном приложении ChatGPT нет.

Кто-нибудь сталкивался с похожим? Подскажите, пожалуйста, в чём может быть дело и что в первую очередь проверить.
Заранее огромное спасибо! 🙏

---

**2026-04-05T17:48:11 | HiLLL**
запустите в терминале zeroblock awg warp

---

**2026-04-05T18:00:49 | Роман**
На zeroblock работает.

---

**2026-04-05T19:04:08 | Alex EfremoFF**
Похоже не стоило мучить жопу, как в поговорке.
ZeroBlock накатил, а теперь он ругается что sing-box не запущен. Пипец.

---

**2026-04-05T20:16:31 | Роман**
Не устанавливать zeroblock на подкоп.

---

**2026-04-05T20:18:29 | Andrey O.**
Возможно из консоли удалить пакет sing-box ручками, либо для чистоты сбросить рутёр на заводские настройки и установить zeroblock

---

**2026-04-05T20:21:22 | Роман**
Роутер в завод для надёжности. Первичная настройка, затем установить zeroblock.

---

**2026-04-05T20:40:43 | Илья**
Еще один наверное странный вопрос. Почему после автонастройки zeroblock не появляется пункт zapret 2

---

**2026-04-05T21:33:32 | Виталя**
Всем привет, только забрал с озона роутер подскажите пожалуйста что лучше ставить Zeroblock+Zapret2 или  скрипт 5 ?

---

**2026-04-05T21:50:25 | Вадим Ободов**
Всем привет.Может кто сталкивался с такой проблемой.Стоит прошивка 24.10.5 и установил zeroblock и zapret2 .Всё работает, но ютуб на телевизоре lg c1 перестал работать.Ютуб через zapret2 работает.Ютуб на пк и смартфонах прекрасно работает

---

**2026-04-05T22:05:02 | Вадим Ободов**
Всем привет.Может кто сталкивался с такой проблемой.Стоит прошивка 24.10.5 и установил zeroblock и zapret2 .Всё работает, но ютуб на телевизоре lg c1 перестал работать.Ютуб через zapret2 работает.Ютуб на пк и смартфонах прекрасно работает

---

**2026-04-05T22:12:42 | Камиль**
Заметил что zeroblock временами просто падает, работал более менее стабильно, но на версии 52 каждый день падает и автозапуск не помогает. Сейчас обновился посмотрим как сейчас будет

---

**2026-04-05T22:13:51 | Роман**
На новый уважаемый zeroblock раз, на встраивание нейронок в роутер два. Пока вроде всё. 
Сам же говорил, а вам гайд нужен? Или не твои слова?

---

**2026-04-05T22:20:45 | Роман**
Желательно сброс на заводские настройки и на чистую систему устанавливать zeroblock. Но можете удалить способом указанным на podkop.net.

---

**2026-04-06T00:03:44 | Роман**
Конечно есть. Купить vps, настроить, ссылку в zeroblock.
оделитесь будьте добры
Нет.
платные тоже рассмотрю
Рассматривайте.

---

**2026-04-06T05:28:46 | Routerich**
Службы->Zeroblock->Секции маршрутизации

---

**2026-04-06T05:33:51 | Routerich**
https://t.me/routerich/394153/405571
Потом добавьте список Games и проверяйте
Потом, если не отпустит ещё поискать сервера игры в инете и добавить их в Zeroblock

---

**2026-04-06T08:46:55 | Санчо Панчо**
сначала zeroblock ставите, потом luci-app

---

**2026-04-06T08:49:25 | Санчо Панчо**
обновляйте страницу, чистите кэш браузера и заходите в службы, там должен появиться Zeroblock

---

**2026-04-06T08:54:53 | Routerich**
В службах Zeroblock появился?

---

**2026-04-06T09:02:01 | Bullet for my valentine Poison**
Я предлагаю раз в сутки удалять zeroblock полностью и по новой его устанавливать. Так сможешь ломку побороть, пока ждешь пакеты новые😂

---

**2026-04-06T10:13:34 | Routerich**
zeroblock умеет во входящие, был кейс для обхода бс

---

**2026-04-06T11:28:01 | Дмитрий З**
А последнюю версию ZeroBlock 0.7.2-r55  в репозитории РР зальёте? А то там только ZeroBlock 0.7.2-r52

---

**2026-04-06T11:42:37 | Роман**
Кто знает, этот сервис следит только за zeroblock?

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

**2026-04-06T12:07:39 | Роман**
В zeroblock всё работает.

---

**2026-04-06T12:19:01 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-06T12:19:56 | Dmitry**
Добрый день,
ZeroBlock отключает интерфейс wg0:

90 Mon Apr 6 14:10:00 2026 cron err crond[25378]: USER root pid 31177 cmd /usr/share/wginstaller/wg.sh cleanup_wginterfaces 91 Mon Apr 6 14:10:00 2026 cron err crond[25378]: USER root pid 31178 cmd /usr/bin/zeroblock bad_interface_check >/dev/null 2>&1 92 Mon Apr 6 14:10:01 2026 daemon notice netifd: Network device 'wg0' link is down 93 Mon Apr 6 14:10:01 2026 daemon info ModemManager[31197]: hotplug: remove network interface wg0: event processed

Как можно решить эту проблему? И если я отключу удаление интерфейса не помешает ли это работе zeroblock?

---

**2026-04-06T12:23:58 | Никита**
Всем привет!

Использую роутер Routerich AX3000 с установленным ZeroBlock — всё работает отлично.

Но возникла задача: есть ноутбук на Linux, который сейчас выходит в интернет через настройки роутера (VPN/прокси от ZeroBlock). Хочу для этого ноутбука:
- полностью обходить VPN/прокси роутера (чтобы он работал через обычный интернет),
- и при этом настроить отдельный прокси уже внутри самого ноутбука через Clash Verge.

Подскажите, пожалуйста:
1. Как правильно исключить одно устройство (ноутбук) из VPN/прокси, настроенного на роутере (ZeroBlock)?
2. Какие есть способы — через MAC/IP, правила маршрутизации или что-то ещё?
3. Как корректно затем настроить Clash Verge на Linux, чтобы он работал независимо и не конфликтовал с сетью роутера?

Буду благодарен за любые советы и примеры 🙏

---

**2026-04-06T12:26:18 | Routerich**
Здравствуйте.
Zeroblock->настройки->Исключённые IP->сюда прописать ip ноутбука, только задайте статический ip ему

---

**2026-04-06T13:06:24 | Никита**
Не работает тик ток на zeroblock на iPhone. Подскажите пожалуйста как сделать ?

---

**2026-04-06T13:16:03 | Kureko**
Ни у кого телеграм не отвалился сегодня утром?

Просто электричество в доме выключали сегодня утром. Роутер перезапустился и теперь не работает телеграм, через Zeroblock и список "Мессенджеры" и свой VPN.

Не могу понять, что случилось, web.telegram.org работает, а приложение нет...

---

**2026-04-06T13:18:59 | Александр Ткаченко**
Добрый день, подскажите если я  конфиг zeroblock скачаю со своего роутера и закину на другой роутерич то все интерфейсы и настройки списков с подписками также продублируются как на моём роутере ?

---

**2026-04-06T13:20:41 | Никита**
Подскажите пожалуйста как это сделать в zeroblock

---

**2026-04-06T13:20:57 | Дмитрий З**
Запрет - это "дурилка" для обхода замедленного. Можно использовать для ютуба. А zeroblock - это уже квн для обхода всего . При настройке по инструкции они друг другу не мешают, а дполняют

---

**2026-04-06T13:30:33 | Gomer Simpson**
Вот такое имею в планировщике: 
00 5 * * * service zeroblock restart
11 5 * * * service zapret2 restart
15 5 * * * service tailscale restart

---

**2026-04-06T13:35:04 | Роман**
Тут за другое речь шла, за приветливость интерфейса, а не за внесение изменений в cron. С таким же успехом можно и zeroblock через терминал рулить, а чё такого, всего лишь нужно и далее описание на пару страниц 😁

---

**2026-04-06T13:44:20 | Routerich**
Отключайте zapret2, добавляйте список в zeroblock и проверяйте

---

**2026-04-06T14:04:13 | Артур**
zeroblock в интернете ничего не нахожу это разработа роутерича?

---

**2026-04-06T14:06:49 | Routerich**
Можно через родительский контроль блокнуть домен ютуб,как вариант и проверить.
Если zapret2 отключать не хотите и переносить ютуб в zeroblock

---

**2026-04-06T14:29:01 | Bumbon4ik**
А его можно сразу в прошивку встроить, что б через zeroblock работало?

---

**2026-04-06T14:30:12 | Routerich**
Можно, через ASU собрать прошивку с этим пакетом и zeroblock .

---

**2026-04-06T14:31:26 | Bumbon4ik**
А он через zeroblock будет работать? Я просто роутер еще не получил, что б начать тестировать и пробовать)

---

**2026-04-06T14:48:41 | Bumbon4ik**
Ну роутере установить MTproxy, который будет работать через zeroblock/podkop через amneziawg.

Дальше в телеграме с прописываю свой ip mtproxy, и работаю через него уже.

---

**2026-04-06T15:24:05 | Routerich**
Здравствуйте.
пробуйте zeroblock, но только предварительно сброс.

---

**2026-04-06T15:26:26 | Anna Bagler**
От ваших блокировок многое зависит. Для запрет вы можете подобрать стратегии https://t.me/routerich/3845/509958
Попробуйте zeroblock и zapret2, но со сбросом роутера.

---

**2026-04-06T16:09:25 | Роман**
Вроде работает, это zeroblock.

---

**2026-04-06T16:42:10 | Никита**
Всем привет!

Столкнулся с проблемой на роутере Routerich AX3000 (ZeroBlock, vless). Не работает корректно сайт tavily.com, а именно — не проходит логин (страница грузится, но авторизация зависает/не завершается).

Текущие настройки в разделе «Списки»:
- включены: AI, Geoblock, Socials  
- CDN: Cloudflare и Google тоже включены  

Вопрос:
👉 Какие списки нужно включить/отключить, чтобы корректно работал tavily.com?  

Домены их сайтов прописывал не работки все равно 
Буду благодарен за помощь!

---

**2026-04-06T16:44:37 | Никита**
Всем привет!

Столкнулся с проблемой на роутере Routerich AX3000 (ZeroBlock, vless). Не работает корректно сайт tavily.com, а именно — не проходит логин (страница грузится, но авторизация зависает/не завершается).

Текущие настройки в разделе «Списки»:
- включены: AI, Geoblock, Socials  
- CDN: Cloudflare и Google тоже включены  

Вопрос:
👉 Какие списки нужно включить/отключить, чтобы корректно работал tavily.com?  

Домены их сайтов прописывал не работки все равно 
Буду благодарен за помощь!

---

**2026-04-06T18:18:48 | Валерий**
Уважаемые подскажите почему ПК подключенный кабелем нормально работает с телегой, а все устройства по вайфаю нет? 
Установлен zeroblock по инструкции

---

**2026-04-06T18:26:00 | Роман**
Тогда ищите кто на месте настроит. Можно предустановить zeroblock, прописать там свои сервера, для надёжности пару. Но запреты точно на месте настраивать, страиегии перебирать. Да и в случае какого сбоя - непонятно что делать.

---

**2026-04-06T19:15:24 | Routerich**
Надо, а можно после сразу перейти на Zeroblock

---

**2026-04-06T19:38:17 | Александр Юг**
Доброго времени суток! Подскажите, что сейчас лучше поставить на новый роутер Скрипт 5 или zeroblock+zapret2?

---

**2026-04-06T19:57:28 | Bullet for my valentine Poison**
Я на 256 сижу (полная прошивка) + Zeroblock c Zapretom. Всегда занято 150-160мб. И проблем как бы не наблюдаю. Учитывая что у меня сейчас Zapret и Zeroblock не вшиты в прошивку.

---

**2026-04-06T20:03:40 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-06T20:58:59 | Александр Меркушев**
ютуб идет через юиубанблок и при выключенном зероблоке работает прекрасно. Влючаю - тормозит.

Вот вывод скрипта:


Анализ запущен: 2026-04-06 20:55:05
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
  Facebook IP:  198.18.0.104 | YouTube IP:  198.18.0.105

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.69 MB / ↑0.27 MB
  Пинг (ya.ru via awg10): 23.247 / 37.582 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock opera-proxy youtubeUnblock

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОНЛАЙН (HTTP/1.1 200 OK)
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200 OK) [tlsv1.3] [try: 2]
  awg10 (IPv6) : ОФЛАЙН
  Запускаем остановленные службы, ожидайте...

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Пересечение между zeroblock и youtubeUnblock:
    zeroblock                 : awg10
    youtubeUnblock            : YouTube
    Домены: googlevideo.com youtube.com 

  zeroblock              awg10 (vpn): socials,block,porn,news,anime,youtube,discord,meta,video,messengers,googleplay
  zeroblock          opera (prx out): geoblock,ai
  zeroblock        DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8
  Версия zeroblock: 0.7.2-r55

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.45 | RAM: 23% | NAND: 49% занято / 34.4M доступно
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

root@RouteRich:~#

---

**2026-04-06T22:01:30 | HiLLL**
запустите в терминале zeroblock awg warp

---

**2026-04-06T22:15:02 | Роман**
У вас zeroblock?

---

**2026-04-06T22:42:59 | Anna Bagler**
В zeroblock, если вы его поставили. Там вкладочки есть.

---

**2026-04-06T22:46:29 | Роман**
А где писАть, варп кто устанавливает? Правильно - уважаемый zeroblock. Вот и пишут.

---

**2026-04-07T00:15:45 | Сергей Никифоров**
Всем привет! После запуска диагностики, проверка FakeIP (клиент) завершилась с ошибкой Не удалось проверить: Load failed
Подскажите, в чем может быть проблема?
Openwrt 24.10.5
Zeroblock 0.7.2-r52

---

**2026-04-07T01:44:15 | Anna Bagler**
Есть тема Zeroblock Beta.

---

**2026-04-07T03:07:02 | Kiss_My_Axe**
opkg update
opkg install zeroblock luci-app-zeroblock
service uhttpd restart

---

**2026-04-07T04:23:30 | Константин**
Походу действо связано с днс. У меня локальный днс сервер развернут и не проходят doh запросы к апстрим списку. Попробуйте сменить podkop zeroblock протокол doh апстрим 9.9.9.9 бустрап 78.88.8.8 из списка. Такое временное решение пока работает у меня

---

**2026-04-07T06:28:56 | Камиль**
Это все логи после падения ZB, сейчас включу trace и буду следить
[zeroblock] ZeroBlock stopped successfully
Mon Apr 6 09:00:11 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock(0.7.2-r55)...
[http_client] curl_easy_perform failed: Error
[ruleset_manager] API request failed (ret: -4, code: 0, size: 0)
[ruleset_manager] Failed to load community lists from any source
[lists_loader] Failed to load community index for v2 API
[config_builder] Download failed (1 errors), enabling auto_fallback two-stage-list via ai
[http_client] curl_easy_perform failed: Error
[utils] Switched to fallback API
[http_client] Retry 1/3 for https://zeroblock.routerich.ru/api/v2/community-lists/news (delay=1000ms, error=No error)
[http_client] Retry 1/3 for https://zeroblock.routerich.ru/api/v2/community-lists/cdn_akamai (delay=1000ms, error=No error)
[http_client] Retry 1/3 for https://zeroblock.routerich.ru/api/v2/community-lists/cdn_digitalocean (delay=1000ms, error=No error)
[http_client] Retry 1/3 for https://zeroblock.routerich.ru/api/v2/community-lists/cdn_gcore (delay=1000ms, error=No error)
[http_client] Retry 1/3 for https://zeroblock.routerich.ru/api/v2/community-lists/cdn_gcore (delay=1000ms, error=No error)
[http_client] Retry 1/3 for https://zeroblock.routerich.ru/api/v2/community-lists/cdn_oracle (delay=1000ms, error=No error)
[zeroblock] ZeroBlock started successfully
Tue Apr 7 03:00:00 2026 cron.err crond[7662]: USER root pid 603 cmd /usr/bin/zeroblock system_monitor >/dev/null 2>&1

---

**2026-04-07T07:51:18 | Aleksei**
Ребята, а почему могут слететь галки в стратегиях Zapret2: rr_default, rr_youtube? Остается только rr_blackhole.

Из-за включенной Автозагрузка новой стратегии в Zeroblock?

Как раз после 3 утра часть сайтов отвалилась вместе с галками в zapret2

---

**2026-04-07T08:09:36 | 𝓛𝓐𝓢𝓣**
Всем привет, немного запутался во всех возможностях роутера. 
Что лучше поставить для повседневного использования и обхода всех ограничений? 
Пока выбираю между ZeroBlock и темой «Интернет без границ» 
У меня есть свой VDS с x-ui, так что могу подкинуть в любой из этих конфигов

---

**2026-04-07T08:12:05 | Routerich**
Здравствуйте.
выбирайте ZeroBlock

---

**2026-04-07T08:25:08 | Routerich**
вам бы прошивку обновить и переходить на zeroblock, или заново скрипт запустить

---

**2026-04-07T08:28:52 | Grigoriy Orlov**
А что такое zeroblock, новая служба? На выходных займусь обновлением прошивки и накаткой скрипта. А на сейчас может есть какой нибудь hotfix чтобы дотянуть неделю?

---

**2026-04-07T08:38:24 | Данила Ступин**
Здравствуйте! Если zapret2 работает в режиме catch-all и при этом в zeroblock так же настроены секции на определенные домены, то будет ли конфликт без настроенных исключений в запрете или это не имеет значения?

---

**2026-04-07T08:57:17 | Routerich**
И если в zeroblock его нет, то значит он через Zapret2 идёт?

---

**2026-04-07T08:58:10 | 𝓐𝓵𝓮𝓴𝓼𝓪𝓷𝓭𝓻**
да,через zeroblock ТОРМОЗИТ СИЛЬНО

---

**2026-04-07T09:29:35 | Артур**
добрый день, zeroblock можно установить на чистый openwrt? или только на роутерич?

---

**2026-04-07T09:41:33 | Константин**
09:00:00 → zeroblock update_lists
ошибки загрузки
Stopping ZeroBlock
Starting ZeroBlock
И судя по журналу так всегда

---

**2026-04-07T09:42:44 | Владимир Волков**
Система - пакеты - кнопка "Обновить списки" - поиск - zeroblock - установить (с luci-app-zeroblock)

---

**2026-04-07T10:03:10 | Владимир Волков**
Система - пакеты - остановить youtubeunblock, zapret, zeroblock, podkop - попробовать снова

---

**2026-04-07T10:15:35 | Routerich**
1. Zapret2

2. zeroblock + vless

---

**2026-04-07T10:18:18 | Константин**
Tue Apr 7 03:00:00 2026 cron.err crond[32709]: USER root pid 22530 cmd /usr/bin/zeroblock system_monitor >/dev/null 2>&1
Tue Apr 7 09:00:00 2026 cron.err crond[32709]: USER root pid 6084 cmd /usr/bin/zeroblock update_lists >/dev/null 2>&1
[http_client] curl_easy_perform failed: Error
[http_client] curl_easy_perform failed: Error
[http_client] curl_easy_perform failed: Error
Tue Apr 7 09:00:08 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Tue Apr 7 09:00:13 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock(0.7.1-r33)...
[ruleset_manager] API request failed (ret: 0, code: 502, size: 0)
[ruleset_manager] Failed to load community lists from any source
[lists_loader] Failed to load community index for v2 API
[config_builder] Download failed (1 errors), enabling auto_fallback two-stage via opera
[http_client] Retry 1/3 for https://zeroblock.routerich.ru/api/v2/community-lists/googleplay (delay=1000ms, error=No error)
[http_client] Retry 1/3 for https://zeroblock.routerich.ru/api/v2/community-lists/messengers (delay=1000ms, error=No error)
[http_client] Retry 2/3 for https://zeroblock.routerich.ru/api/v2/community-lists/messengers (delay=2000ms, error=No error)
[http_client] Retry 1/3 for https://zeroblock.routerich.ru/api/v2/community-lists/news (delay=1000ms, error=No error)
[zeroblock] ZeroBlock started successfully

---

**2026-04-07T10:26:51 | Георгий Новожилов**
По поводу прошивки: помогло, спасибо огромное! Заработал интернет в принципе, но, естественно, без обходов блокировок

В связи с чем вопрос: какой сервис посоветуете ставить для надёжности? Нужно стабильное решение, я просто в запреты / подкопы / zeroblock-и не погружался еще

Количество сервисов, для которых необходим обход, пополняется с каждым днем, в руантиблоке было порядка 300 имен

---

**2026-04-07T10:27:05 | Роман**
https://t.me/routerich/80283/468513 - полный мануал zeroblock

https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

---

**2026-04-07T10:27:15 | Routerich**
zeroblock

---

**2026-04-07T10:29:01 | Роман**
https://t.me/routerich/80283/468513 - полный мануал zeroblock

https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

---

**2026-04-07T10:30:55 | Роман**
Спасибо за уточнение dear developer. Слышал радостную весть о вашем выздоровлении, поздравляю. Надеюсь разработка уважаемого zeroblockа теперь пойдёт стахановскими темпами.

---

**2026-04-07T10:46:02 | Роман**
Что нравится - то и выбирайте. Но уважаемый zeroblock лучше, он эволюционирует в демона.

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

**2026-04-07T12:13:18 | Роман Лобарев**
Добрый день!  Роутер стоит в районе где "белый список" 100%, есть смысл пытаться Zeroblock или zapret2 настраивать? или только vless подключить через лазейку остается?

---

**2026-04-07T12:35:47 | Константин**
[clash_api] /Ps5/delay?url=http://www.gstatic.com/generate_204&timeout=5000 failed: HTTP 504
Tue Apr 7 12:25:09 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Tue Apr 7 12:25:15 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock(0.7.1-r33)...
[zeroblock] ZeroBlock started successfully

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

**2026-04-07T12:56:39 | Макс**
А причем тут огород  если вопрос на прямую касается ZeroBlock и не рабочей оперы в нем?

---

**2026-04-07T13:07:40 | Роман**
https://t.me/routerich/80283/468513 - полный мануал zeroblock
Вперёд.
Зачем сидеть на опере при наличии своего варианта и теребить людей своим - не работает - НЕЯСНО.
Давайте выясним, какого вида ваш впн? Подписка? vless? HY2?

---

**2026-04-07T13:21:12 | Routerich**
да, если на телефоне включен ExitNode и интерфейс добавлен в Podkop/zeroblock (на случай если этот адрес у вас прописан в этих службах)

---

**2026-04-07T13:27:33 | e.mamaev**
Народ подскажите как разрешить routerich принимать пакеты с другого роутера с порта wan и использовать через сервис zeroblock. Этим роутером пользуют неделю не знаю всех нюансов правил файревола и маршрутизации.

---

**2026-04-07T14:10:21 | Vadim**
Привет! Только получил роутер и конечно же судорожно принялся устанавливать все подряд из этого форума - и скрипт №5, и Zeroblock, и Zapret2. Подскажите, плиз, для тупых - выполнения скрипта №5 достаточно для базового пользования? В Zeroblock лезть не нужно было?
Нужно ли как-то удалять пакеты и откатывать установки/ресетить роутер или достаточно отключить эти службы?

---

**2026-04-07T14:11:48 | Anna Bagler**
На чистый роутер лучше ставить zeroblock. Лучше сбросьте до заводских.

---

**2026-04-07T14:20:57 | Routerich**
система->пакеты->удалите пакет sing-box
а лучше сбросьте роутер потом установите zeroblock

---

**2026-04-07T14:31:00 | Роман**
Только создать (или заменить) не в zeroblock, а в подкопе.

---

**2026-04-07T15:27:57 | Никита**
Уважаемые, есть видео как настроить zeroblock оптимально и правильно?

---

**2026-04-07T15:35:46 | Никита**
Выбраны в vless (zeroblock) в машрутизации ai

---

**2026-04-07T16:00:02 | Костя Токарев**
Ребят! У всех AWG отвалился на роутере?
В пятницу у меня упал VLESS. И не как не хотел работать, доступ к серверу при этом оставался. Обновил роутер (очень понравилось обновление, восторгу нет предела), на VPS развернул AWG. что бы не сносить с ZeroBlock AWG10, я добавил свой как дополнительный. Работало всё отлично, до сегодняшнего дня, на роутере отвалился и AWG10 и мой AWG. Со смарта и мобильной сети AWG работает. С роутера, не работает. Что стоит сделать?

---

**2026-04-07T16:45:47 | Павел**
Получил роутер, настроил zeroblock со своим vless. Все летает по встроенным спискам. Ребята, вы лучшие!

---

**2026-04-07T17:06:24 | Routerich**
zeroblock + custom config

---

**2026-04-07T17:21:40 | Gomer Simpson**
Тема ZeroBlock Beta.

---

**2026-04-07T17:34:05 | Viktor Polesov**
Уважаемое сообщество, прошу прощения, но не реально пересматривать тонны сообщений,  ткните плз.  в ссылку с чего начинать в текущих условиях. Есть RouteRich AX3000 c 24.10.4 c Podkop`ом через vless, который перестал работать. Говорят, что влесс уже не актуален и нужно переходить на  Zeroblock+Zapret2. Что в этом случае надо сделать X-Ray на VPS? Задача минимум вернуть ЮТ на ТВ, возможно-ли это сделать малой кровью, попроще? Или ставить 25-ю прошивку и начинать всё  нуля? Спасибо заранее!)))

---

**2026-04-07T17:52:46 | Anna Bagler**
Скрин диагностики zeroblock покажите.

---

**2026-04-07T18:16:15 | Никита**
извиняюсь, то качество не то, то днс палит которого нет в zeroblock

---

**2026-04-07T18:47:23 | Routerich**
Здравствуйте.
А что-то используете типо Podkop, zeroblock?

---

**2026-04-07T19:49:21 | Anna Bagler**
У вас zeroblock стоит? Есть готовый список. Если awg упал, то перенесите его в секцию с proxy.

---

**2026-04-07T20:19:19 | VecH.Pro**
А zeroblock из бета выходить собирается вообще ? 😁

---

**2026-04-07T20:20:22 | Kiss_My_Axe**
Оно не просто "Не обязательно", оно однозначно "Вредно!".
Во всех случаях, кроме одного - весь траф внутрь этого канала.
Но такой вопрос ныне решается с помощью секции "Catch-all" в Zeroblock.
Далее в офтоп, или вопросы предлагаю перейти.

---

**2026-04-07T20:37:23 | Максим**
Новую стратегию мне помогли поставить, ZeroBlock и Zapret2

---

**2026-04-07T21:31:54 | Alex_Jester**
Обновил вручную через меню пакеты zeroblock и zapret2, при их обновлении выдавало ошибки, там было сказано, что-то про то что конфиги не совпадают. Так и должно быть? Нужно просто проигнорировать ошибки?

---

**2026-04-07T21:33:47 | Raux**
Твой ZeroBlock видит IP-адрес из подсети 92.123..., смотрит в свою базу и говорит: «А, я знаю этот адрес! Он записан в группе "Новости" (News), потому что его использует DW». И бац — отправляет твой Стим в туннель для новостей (awg10), хотя ты Стим туда не просил.

ИИ мне такое же ответил )

---

**2026-04-07T21:38:35 | Gomer Simpson**
Обновитесь, потом в тему ZeroBlock, читать, ставить, радоваться.

---

**2026-04-07T22:09:22 | ARTEM**
У меня как бы всё работает zeroblock и сам интернет но дальше первоначальной настройки зайти не могу можно ли как то без сброса первоначальную скипнуть ?

---

**2026-04-07T22:33:33 | Keros1n**
что лучше ставить? zeroblock или podkop?

---

**2026-04-07T22:55:32 | Anna Bagler**
Базовая настройка - бумажка из коробки. Затем тема zeroblock beta, в ней есть полный мануал и краткая инструкция, и даже видео можно найти.

---

**2026-04-07T23:21:20 | Alex_Jester**
Надо ли перезагружать роутер при обновлении пакетов zeroblock и zapret 2, или это лишнее?

---

**2026-04-08T06:52:16 | Владимир Волков**
Тема "Zeroblock beta", прочитали инструкцию, вставили подписку, выбрали списочки и живёте счастливым

---

**2026-04-08T06:57:42 | Виталий**
День добрый. Получил вчера роутер. Обновил, поставил zeroblock и zapret2. Все отлично, но не работает стимовская версия albion. При этом если запустить awg на компе, то все работает. Подскажите пожалуйста, может кто сталкивался, куда и что прописать чтобы заработало? =)

---

**2026-04-08T07:03:44 | Routerich**
Здравствуйте.
найти все домены и подсети и добавить в zeroblock

---

**2026-04-08T07:57:09 | Tim Mars**
а чем zeroblock от podkop отличается?

---

**2026-04-08T08:50:33 | Routerich**
из Zeroblock убрать список Messengers

---

**2026-04-08T09:27:54 | Роман**
С этим тоже не спорю. 
Релиз уважаемого zeroblockа когда?

---

**2026-04-08T09:29:38 | Роман**
Хорошо. Когда уважаемый zeroblock выйдет в люди (хотя бы в виде бета версии)?

---

**2026-04-08T09:48:31 | Роман**
Какой список? Два манула: один - по функции в уважаемом zeroblockе (забыл как называется, из четырёх букв 😁), второй - как нейронку в роутер запихать.

---

**2026-04-08T09:51:17 | Routerich**
Здравствуйте.
https://t.me/routerich/3845/245550

но лучше сразу переходите на ZeroBlock, но там без скрипта, только мануал.

---

**2026-04-08T09:52:52 | Роман**
Всё подряд устанавливать не стОит. 
Амнезию руками придется вносить. 
Zeroblock лучше вместо подкопа.
Из запретов выбирайте один, либо первый, либо второй. 
Под прочим непонятно что имелось в виду. 
И да, будете сидеть на халяве - будете постоянно скидывать диагностику в чат. Заранее поищите платные варианты, либо подписки.

---

**2026-04-08T10:03:34 | Сергей Никифоров**
Всем привет!
Ставил Zeroblock по мануалу на чистую новую прошивку, не проходили проверки FakeIP, как в диагностике так и по скрипту.
Поставил podkop так же на чистую новую прошивку скриптом из beta, проверки FakeIP проходят, как в диагностике так и скриптом.
Подскажите, в чем может быть проблема?

---

**2026-04-08T10:11:47 | ZZII | RTK**
Возникла очень странная проблемма. У меня ZeroBlock и мне впн не приходится включать. Но почему то в тик токе не работает нифига. Приходится на телефоне включать свой же впн и только тогда работает всё

---

**2026-04-08T10:29:29 | ZZII | RTK**
Возникла просто очень странная проблемма. У меня же ZeroBlock и мне впн не приходится включать. Но почему то в тик токе не работает нифига. Приходится на телефоне включать свой же впн и только тогда сработает

---

**2026-04-08T10:31:03 | Роман**
Сделайте уже варнинг - удалить подкоп перед употребленим уважаемого zeroblockа.

---

**2026-04-08T10:45:01 | Bullet for my valentine Poison**
И зероблок можно обновить. Система-пакеты. Нажать обновить списки. Слева в фильтр вписать zeroblock и выбрать вкладку обновления

---

**2026-04-08T10:48:45 | Александр Король 👑**
Добрый день! Являюсь владельцем устройства с марта. Во первых спасибо за прекрасный девайс. Во вторых есть ряд вопросов, причём достаточно нубских. Сразу после получения обновил все пакеты и поставил zapret, zapret2, podkop и zeroblock. В принципе из того что нужно: tg, wa, youtube, insta, детям сервера brawl stars, торрент-трекеры. И вроде все более менее работает, но каждый день приходится перезапускать службы (в частности podkop) чтобы стали доступны торренты. Может я что-то не так сделал? Куда глянуть?

---

**2026-04-08T10:53:29 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock
Два.

---

**2026-04-08T11:02:18 | Bullet for my valentine Poison**
ты Luci-app-zeroblock не поставил

---

**2026-04-08T12:09:21 | S W**
Ребят, подскажите пожалуйста, вне дома на пк использовал nekoray от MatsuriDayo на пк, но, не знаю точно с чем связано, перестал работать 
(если кратко, то сначал думал что провайдер начал блокировать из-за подмены sni мой vps с vless+reality. Но с телефона (v2rayNG) и дома (zeroblock, настроенная секция) все работает штатно, вышел на то что прооблемы с клиентом nekoray (nekobox))

Решил заменить на другой, вижу есть какой то форк от qr243vbi (так и называется nekobox), версия  5.10.34 (будто наследовал от MatsuriDayo), но выглядит сомнительно. Так же поискал по чату и люди говорят о Throne как он официальном(?) форке-продолжении nekoray, насколько этому можно верить и вообще что по итогу лучше использовать на пк?

---

**2026-04-08T12:29:36 | Роман**
На это может ответить или разработчик или тот, кому вы скинете подписку для теста в уважаемом zeroblockе.

---

**2026-04-08T13:19:25 | Anna Bagler**
Тема Zeroblock Beta. В закрепах есть краткая инструкция по установке и полный мануал.

---

**2026-04-08T13:42:50 | Роман**
А ты ему: - а я говорил, я предупреждал! 
Вон товарищ HiLLL полинтернета в уважаемый zeroblock засунул (в иде cdn) и в ус не дует.

---

**2026-04-08T13:50:07 | Routerich**
только потом созданный интерфейс надо добавлять в Podkop/zeroblock рядом с br-lan, чтобы обходы работали

---

**2026-04-08T14:15:41 | Роман**
Нашло бой менее чем за минуту, пинг до 50, нормально играется.
Установлен zeroblock, zapret 2.

---

**2026-04-08T14:19:15 | Max**
Вопрос в тему-вацап сообщения уходят/приходят, но не скачиваются картинки/ файлы. Настройки стандартные, zeroblock zapret2. Что можно сделать?

---

**2026-04-08T14:26:03 | Max**
Messengers  в списках сообщества в zeroblock не достаточно?

---

**2026-04-08T14:30:39 | Max**
спасибо, я как понимаю тоже в zeroblock в awg секции?

---

**2026-04-08T15:42:36 | Роман**
Установить уважаемый zeroblock и сделать секцию catch-all.

---

**2026-04-08T15:49:04 | Роман**
Тогда проще zeroblock с одной секцией. Свой сервер имеется?

---

**2026-04-08T15:56:21 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

Желательно избавиться от подкопа сбросом на заводские настройки.
Автонастройку пропустить, создать свою секцию без доменов и списков, вставить ссылку сервера.

---

**2026-04-08T16:04:25 | Hump Dog**
[http_client] Retry 3/3 for https://zeroblock.routerich.ru/api/v2/community-lists/tools (delay=4000ms, error=Error)
[http_client] Retry 3/3 for https://zeroblock.routerich.ru/api/v2/community-lists/torrent (delay=4000ms, error=Error)
[http_client] Retry 3/3 for https://zeroblock.routerich.ru/api/v2/community-lists/video (delay=4000ms, error=Error)

Что ему от меня надо на V2 списках? Ни один список по V2 не скачивает

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

**2026-04-08T17:52:37 | Роман**
с первого рыйтыртырыча я беру файл /etc/config/zeroblock и копирую на второй рыйтытырыч

---

**2026-04-08T18:04:13 | Anna Bagler**
Вам тогда в тему Zeroblock Beta.

---

**2026-04-08T18:29:05 | Артём**
Выключил zeroblock, позволил прогнать скрипт. Но в скрипте везде ОК (кроме журналов вывода и ошибок)

---

**2026-04-08T19:09:31 | Anna G**
Скоро буду передавать RR для подруги, возник вопрос - лучше сейчас сразу ZeroBlock ставить или скрипт номер 5 (или его бету)? Что сейчас более "готовое решение" и стабильнее с текущими блокировками? Особенно если нужно настроить хоть какие-то обходы быстро, а потом уже доработать позже как появится время.

Скрипт вроде сам проверял, какие сервисы обхода доступны, и выставлял нужные конфигурации, а в случае с зероблоком это как работает? Нужно больше понимания того, что делаешь?

Также понимаю, что в случае скрипта его оптимальнее запускать уже на провайдере подруги, но у меня не будет такой возможности. Подруга если придется - разберется, но мне самой было бы проще настроить. В идеале хотелось бы передать уже настроенным и с удаленным доступом, но не факт, что это все на ее сети заведется. У нее московский билайн, у меня мелкий районный провайдер.

Посоветуйте плиз, как лучше быть.

---

**2026-04-08T19:10:07 | Routerich**
Здравствуйте 
Zeroblock

---

**2026-04-08T19:10:27 | Anna Bagler**
Zeroblock.

---

**2026-04-08T19:49:35 | Routerich**
Здравствуйте.
Можно, но лучше не ставить.
Zeroblock есть, он будет лучше. Ещё есть Podkop

---

**2026-04-08T20:00:01 | Alex Korotkov**
Ну по acl получается, как в том же passwall? Читал по нему мануалы, надо ознакомиться будет еще с zeroblock, не слышал просто о таком)

---

**2026-04-08T20:25:39 | Alex Korotkov**
Пакеты соответсвенно нужно скачать тут из раздела zeroblock или на роутере есть что-то типа репозитория, где можно докачивать необходимые модули?

---

**2026-04-08T20:30:48 | Kiss_My_Axe**
Система - Пакеты, обновить списки, поиск zeroblock.

---

**2026-04-08T20:34:10 | Kiss_My_Axe**
Когда НЕТ качол секции, то в /tmp/zeroblock НЕТ инфы о качол секции.
А раз она есть, то ЗБ считает, что качол активна.

---

**2026-04-08T20:36:38 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-08T21:36:05 | Alex Korotkov**
Всем салют.
Изучаю мануал по зероблок, пока роутер еще не пришел и возник вопрос.
В мануале есть пункт по установки секций, там opera,awg10 и так далее. И вот мне не совсем понятно, их обязательно надо устанавливать в автонастройке?
У меня есть купленная vless подписка у впн сервиса и я хочу ее применить в zeroblock и настроить списки какое сайты через этот впн гонять , но в мануале не смог найти

---

**2026-04-08T21:37:49 | Роман**
А у вас zeroblock?

---

**2026-04-08T22:53:19 | Anna Bagler**
На чистый роутер zeroblock, потом смотреть.

---

**2026-04-08T22:59:39 | Anna Bagler**
Zeroblock.

---

**2026-04-08T23:00:05 | kittyflanger**
есть полный мануал по установке zeroblock в интерфейсе routerich?

---

**2026-04-08T23:06:04 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-08T23:46:14 | Фил**
Добрый вечер, только начинаю знакомиться с openwrt и роутерич, скажите пожалуйста на ютубе все используют podkop, а тут zeroblock и на зероблок вообще нет роликов, что лучше или актуальнее использовать? или где можно почитать сравнение?
Спасибо!

---

**2026-04-08T23:47:54 | Anna Bagler**
Zeroblock.

---

**2026-04-09T00:48:03 | Роман**
А как же уважаемый zeroblock ?

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

**2026-04-09T06:41:12 | Routerich**
а если стопнуть ZeroBlock? так же ругается и не пускает?

---

**2026-04-09T08:34:46 | Routerich**
Здравствуйте.
службы->zeroblock->автонастройка->Автозагрузка новой стратегии Zapret2->галочку убираем, сохраняем и применяем

---

**2026-04-09T09:28:27 | Роман**
Эх, если бы уважаемый zeroblock был открытой разработкой...

---

**2026-04-09T10:25:22 | Routerich**
Отследить все домены и добавить их в Podkop/zeroblock

---

**2026-04-09T10:40:48 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

Автонастройку можете пропустить. Создать секцию, вписать свой прокси, выбрать списки.

---

**2026-04-09T12:14:42 | Серёга_44rus**
Здрасьте) Zeroblock с podkop несовместим?

---

**2026-04-09T12:48:13 | Артём Буданов**
Подскажите пожалуйста, а можно ли накатывать zeroblock, если уже подкоп работает?

---

**2026-04-09T12:50:55 | Артём Буданов**
Мне оставаться на подкопе, или перейти на Zeroblock? Что мне сейчас делать то?))

---

**2026-04-09T12:51:50 | Роман**
Уважаемый zeroblock естественно.

---

**2026-04-09T12:57:42 | Routerich**
чтобы хвостов не было надо ресет, потом zeroblock и потом ASU

---

**2026-04-09T13:45:23 | Роман**
Вам бы на zeroblock перейти со сбросом на заводские.

---

**2026-04-09T14:44:38 | Anna Bagler**
Тут поддерживается zeroblock и пока podkop.

---

**2026-04-09T14:46:31 | DedLovesFrogs**
Подскажите пожалуйста, уважаемые, B4 кто-нибудь тут ставил? Или лучше использовать Zeroblock/иные средства?

---

**2026-04-09T15:20:54 | Петр**
вот я по нему прогнал, получил 15 стратегий, их всех вставил и запустил, но ничего не поменялось. Мб что-то не так делаю? в самом zeroblock нужно тоже что-то менять (там discord есть в awg10, я его там убрал попробовал, и добавил попробовал, не получается)

---

**2026-04-09T15:28:29 | Anna Bagler**
Если обновили прошивку. Ставьте сразу zeroblock https://t.me/routerich/394153/405571

---

**2026-04-09T15:34:12 | Anna Bagler**
Для обходов у РР есть гибкий zeroblock.

---

**2026-04-09T15:35:34 | Anna Bagler**
Полный мануал по zeroblock тогда изучайте. Какие списки cdn в секциях выбраны сейчас?

---

**2026-04-09T15:56:41 | Anna Bagler**
Либо вернуть YouTube в zeroblock, но awg в бесплатном варианте может часто падать, либо подбирать стратегию для zapret2.

---

**2026-04-09T16:01:22 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-09T16:06:45 | Никита**
Ребята, всем привет. Нужна помощь 🙏

Столкнулся с такой проблемой: купил роутер, в целом всё отлично работает — скорость, стабильность, остальные сервисы без нареканий. Но есть один момент: не работает приложение Claude на iOS.

Суть проблемы: отправляю запрос в Claude — и он просто не отвечает, как будто зависает (нет ни ошибки, ни ответа).

Что уже сделал:
- В zeroblock (панель управления роутера) добавил свой VLESS
- В секции маршрутизации для VLESS указал категории: ai и cloudflare
- Также отдельно прописал пользовательские домены, связанные с Claude

Но, к сожалению, это вообще не помогло — ситуация не изменилась.

Может, кто-то уже сталкивался с таким?  
Подскажите, куда копать:

Буду очень благодарен за любые советы 🙌

---

**2026-04-09T16:25:55 | Vitaly**
1. Открываем раздел Система, потом пакеты.
2. Жмем зеленую кнопку "Обновить списки" и ждем, закрываем появившуюся табличку нажав на кнопку "Закрыть".
3. Вводим в окне "Фильтр" (слева) Zeroblock. Внизу должны появиться два пакета: Zeroblock и luci-app-zeroblock.
4. Нажимаем кнопку "Установить" напротив каждого пакета.(Первым идет Zeroblock, а затем luci-app). В появившемcя окне жмем еще раз установить. После завершения закрываем окно. 
5. Очищаем в браузере кэш и перезагружаем страницу. В службах появится новый пункт "Zeroblock"

---

**2026-04-09T16:30:02 | Anna Bagler**
Я бы на вашем месте сбросила до заводских без восстановления настроек и поставила zeroblock, потом туда свою ссылку и смотреть.

---

**2026-04-09T16:31:28 | Антон Чепкасов**
Всем привет, ни у кого интернет по wifi не отваливался? На 2 роутерах РР перестал работать. Один обновил на актуальную прошивку и накатил ZeroBlock + Zapret2, всё работает. Второй ещё не трогал. Раньше настроено было через yotubeunblock и podkop, Интересно вот, проблема в прошивке старой или  yotubeunblock и podkop ?

---

**2026-04-09T16:44:01 | Danya Co**
Подскажите, что делать если в Пакетах Фильтр Zeroblock не ищет 
Списки обновлял

---

**2026-04-09T16:52:47 | Валентин**
Читаю тему и никак не могу понять, сейчас актуально использовать zeroblock+zapret2 или podkop+zapret1? Что дальше будет в поддержке и что правильнее настроить?

---

**2026-04-09T16:54:01 | Роман**
Это.
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-09T16:54:09 | Anna Bagler**
Zeroblock. Zapret2/1 - что вам нужнее.

---

**2026-04-09T16:56:12 | Валентин**
Т.е. сношу podkop и singbox и ставлю zeroblock+zapret2, получается так? И как я понимаю развиваться дальше будет все таки zapret2, не первый?

---

**2026-04-09T17:01:05 | Валентин**
это про zeroblock, на сколько понимаю, спасибо. а запреты чем отличаются?

---

**2026-04-09T17:16:32 | Роман**
Да, устанавливать и настраивать самому.
И можно ли сделать сплит-туннелинг (как понимаю это так называется), чтобы ВПН на роутере включался только при заходе на запрещенные сайты, а отечественные не трогал?
zeroblock/podkop работают по такому принципу.

---

**2026-04-09T17:17:07 | Anna Bagler**
Тема zeroblock, в закрепах краткая настройка есть и полный мануал.

---

**2026-04-09T17:17:51 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-09T17:33:18 | Роман**
Подкоп и zeroblock ммм. 
Я не буду в этом копаться, извините.

---

**2026-04-09T17:35:26 | Anna Bagler**
Изучите интерфейс службы zeroblock.

---

**2026-04-09T17:41:15 | Роман**
А зачем вам подкоп, если в zeroblock можно делать всё то же, только лучше?

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

**2026-04-09T18:12:54 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-09T18:17:34 | Роман**
zeroblock и zapret разные вещи, zb работает с прокси/впн, запрет "дурит" трафик.

---

**2026-04-09T18:51:01 | Anna Bagler**
Zeroblock/podkop, отдельная секция с привязкой к интерфейсу и спискам.

---

**2026-04-09T18:54:55 | Anna Bagler**
Ставьте zeroblock, если ничего нет.

---

**2026-04-09T18:55:55 | Роман**
Вы zeroblock/podkop установили? Они рулят списками и трафиком через ваш интерфейс.

---

**2026-04-09T18:56:14 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-09T18:56:25 | Владимир Волков**
Раздел Допвозможностей, Exit Node + Podkop или Zeroblock

---

**2026-04-09T19:03:27 | Дмитрий Кирин**
Подскажите настроил обход через Zeroblock. Сначала все нормально работает, через какое то время выкидывает с модема, телефон или ноутбук сеть видео, просит пароль, вводишь его а не подключается. Питанием перезагрузишь модем, помогает.

---

**2026-04-09T19:06:42 | Anna Bagler**
К zeroblock это пока не относится. Собирайте логи https://t.me/routerich/4/414561 и в Вопросы.

---

**2026-04-09T19:07:41 | Дмитрий Кирин**
Подскажите настроил обход через Zeroblock. Сначала все нормально работает, через какое то время выкидывает с модема, телефон или ноутбук сеть видео, просит пароль, вводишь его а не подключается. Питанием перезагрузишь модем, помогает.

---

**2026-04-09T19:13:31 | Dr. Strange**
investizo.com подскажите а как проще всего данный сайт добавить в Zeroblock чтобы он тоже работал, не подключая ни каких КВН?

---

**2026-04-09T19:14:59 | Anna Bagler**
Нет, что-то одно. Zeroblock.

---

**2026-04-09T19:16:56 | Дмитрий Кирин**
Подскажите настроил обход через Zeroblock. Сначала все нормально работает, через какое то время выкидывает с модема, телефон или ноутбук сеть видео, просит пароль, вводишь его а не подключается. Питанием перезагрузишь модем, помогает.

---

**2026-04-09T19:26:53 | Александр Кормановский**
добрый день, вопрос куда лучше добавлять свои домены
• установлен ZeroBlock, там есть секции opera и awg10, и в каждой из них есть вкладка Списки, и там можно указать Пользовательские домены
• еще установлен zapret2, и там тоже есть вкладка Списки, где в секции user (/opt/zapret2/ipset/zapret_hosts_user.txt) я как понимаю тоже можно добавить домены

---

**2026-04-09T19:29:22 | Routerich**
Здравствуйте.
Используйте zeroblock

---

**2026-04-09T19:33:16 | Anna Bagler**
zeroblock не даст, а так, конфликт.

---

**2026-04-09T19:37:19 | Anna Bagler**
Какой код вы пытаетесь запустить? Для zeroblock скриптов нет.

---

**2026-04-09T19:39:55 | Anna Bagler**
Полный мануал по zb читайте. Ссылка на списки есть в закрепах в теме по zeroblock.

---

**2026-04-09T19:52:40 | Александр Кормановский**
добавлял в opera и в awg10 домен myip.com и при переходе на него показывает почему в обоих случаях один и тот же российский айпи или я как-то не так проверяю? zeroblock перезапускал

---

**2026-04-09T20:01:55 | Alex Korotkov**
Всем привет.
Через Zeroblock можно можно блокнуть рекламу на ютубе?
Я нашел какие-то домены в ветке Wiki, прописал их в секцию маршрутизации с действием block, но эт не помогло. Или это где-то в другом месте прописывать?

---

**2026-04-09T20:05:57 | Routerich**
Здравствуйте.
Остановите вае обходы, Podkop /zeroblock, youtubeunblock, zapret, и проверяйте будет работать так или нет

---

**2026-04-09T20:25:38 | Роман**
Zeroblock перезапустить попробуйте.

---

**2026-04-09T20:44:05 | Kiss_My_Axe**
Не, так не сработает.
Так сработает:
opkg update && opkg install zeroblock luci-app-zeroblock && /etc/init.d/podkop stop && /etc/init.d/podkop disable
Впрочем и так не сработает, сингбокс-конфликт вылезет.

---

**2026-04-09T20:53:36 | Alex Korotkov**
вот что в крите
ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Внутреннее пересечение в youtubeUnblock:
    youtubeUnblock            : YouTube (Условия: default)
    youtubeUnblock            : YouTube (Условия: default)
    Домены: googlevideo.com youtube.com 

  !!!_КРИТ: Пересечение между zeroblock и youtubeUnblock:
    zeroblock                 : awg10
    youtubeUnblock            : YouTube
    Домены: googlevideo.com youtube.com

---

**2026-04-09T21:06:52 | Alex Korotkov**
я отключил службу.
перетащил правило авг10 вверх над своим правило vless.
перезапустил zeroblock.
авг10 стал не N/A, ютуб заработал.
спасибо вам за наводку

---

**2026-04-09T21:32:37 | ㅤㅤ**
После отключения света, warp сразу не стартует и после перезагрузки роутера. Приходится вводить команду в терминале zeroblock awg warp. Вроде в подкопе была возможность автоматического поднятия warp, такое в zb есть, как найти?

---

**2026-04-09T21:48:35 | Петр Горбунов**
Подскажите, в чем может быть проблема, раньше был podkop + предыдущая прошивка. Обновился до последней версии, поставил ZeroBlock, настроил работу через vless. Но сейчас если на телефоне подключен wifi и поднят на телефоне vless то ничего не грузится, кроме морды модема. Раньше они не конфликтовали, работало с включенным впн на телефоне.

---

**2026-04-09T22:34:32 | WizardTech**
доброй ночи )) познаю ZeroBlock 

подскажите плз . после установки зашел в авто-настройку прожал все )) 
добавил секцию proxy вставил свой сервер

---

**2026-04-09T22:57:42 | Anna Bagler**
По умолчанию его нет. Ставить скриптом. Или вместо него zeroblock.

---

**2026-04-09T23:14:37 | Роман**
Раньше, на заре времён, уважаемый zeroblock был обёрткой 🌱. Да-да, представьте себе. Пихал разные процессы, толкал их и спать ложился 😴. Но однажды создателю надоело это сонное поведение и решил он его вообще не спящим сделать, взял код его и принялся за работу ⚙️. День работал, неделю работал, и получился демон 👹: не спит демон, чутко бдит за процессами различным, ходит да тыкает в них трезубцем своим 🔱. Заодно и функционала прибавилось 📈. 
Тут и сказочке конец, кто прочёл - тот огурец 🥒😁

---

**2026-04-09T23:19:23 | Anna Bagler**
Первый шаг - первичная настройка. Второй - zeroblock.

---

**2026-04-10T00:02:14 | Алексей**
Купил устройство, настроил интернет без границ - запусти скрипт. Добавил в подкоп, что было мне необходимо. И вроде все работает. Потом начал читать про zeroblock и zapret2. Вопрос - надо ли перейти с zapret+podkop? На что лучше перейти - zeroblock или zapret2? Как перейти если zeroblock валится в ошибку:
Thu Apr 9 23:45:54 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Thu Apr 9 23:45:59 2026 user.notice zeroblock: No sections configured, restoring DNS and skipping start

---

**2026-04-10T00:17:22 | Алексей**
С английского не нужен, а на понятный пригодится )) 
Но помогите сперва понять - если у меня и так все на zapret работает, имеет ли смысл доп телодвижения делать? Что мне это даст? Стабильность? Скорость? Или пусть все пока остается как есть (zeroblock остановлю или снесу)?

---

**2026-04-10T07:27:50 | Routerich**
покажите диагностику ZeroBlock

---

**2026-04-10T07:59:59 | Routerich**
Вам легче сбросить роутер и потом установить Zeroblock

---

**2026-04-10T08:29:06 | Routerich**
Всем у кого проблема с Telegram, перенесите список Messengers из секции awg10 в секцию Opera

так же в ZeroBlock, в настройках, изменяем  сервер DNS на 9.9.9.9

И обновляем opera-proxy через Система->Пакеты

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

**2026-04-10T09:14:11 | Egor Mikhaylov**
Привет!
Проблема на IOS аналогичная, приложение chatgpt по региону не работает
Есть такое наблюдение:
Это не связано с конкретными доменами, потому-что у меня все домены в файлах и эти же файлы при работе в podkop не вызывали проблем при работе chatgpt, я пока не могу понять, какая опция в zeroBlock может препятствовать работе, потому-что, повторюсь в podkop при тех-же доменах и настройках - chatgpt работал корректно на ios, соответственно никаких изменений на телефона тоже не производилось и Wifi сеть та-же.

---

**2026-04-10T09:37:15 | Routerich**
у вас Podkop или zeroblock?

---

**2026-04-10T09:37:47 | XP Humanikus**
Вопрос: из коробки маршрутизатор RR обеспечивал блокировку рекламы на планшете Xiaomi. После установки ZeroBlock функция блокировки рекламы перестала работать. Как правильно настроить блокировку рекламы?

---

**2026-04-10T09:38:29 | Routerich**
Здравствуйте.
в настройках ZeroBlock изменить сервер DNS на AdGuard

---

**2026-04-10T09:48:36 | Баир**
Zeroblock

---

**2026-04-10T10:01:41 | Routerich**
Podkop или ZeroBlock используете?

---

**2026-04-10T10:16:20 | Роман**
Вы интерфейс zeroblock хоть в глаза видели?

---

**2026-04-10T10:17:04 | Mikhail Velichko**
Извините за глупый вопрос, но как пустить что-то именно через Zapret? Или правила Zapret срабатывают после правил Zeroblock? Ну то есть если я хочу дискорд через запрет, то исключаю его из списка секций и добавляю соответствующий список в правила пункта Zapret2, так?

---

**2026-04-10T11:12:11 | Gomer Simpson**
Система - Пакеты. Обновить списки. Фильтр zeroblock. Будет актуальная.

---

**2026-04-10T11:21:36 | Андрей**
Народ подскажите плиз - посоветовали в эту тему обратиться..  Постоянно виснет роутер при раздаче торрентов на большой скорости.. ~ 800-900Мбит.. причем именно при раздаче, при загрузке все ок.  Галка Исключить BitTorrent стоит разумеется.. ZeroBlock через свой vless инет использую

---

**2026-04-10T11:31:26 | Георгий Новожилов**
UPD: рестартнул ZeroBlock, всё ок, всё ожило

---

**2026-04-10T11:37:23 | Тимур Шамиладзе**
Подскажите. Первоначальная настройка. Запустил скрипт 5. Заработал ютуб, инста и chatgpt, но через пол часа опять перестал. 
Посмотрел вчера поддержка здесь дала совет при запуске: "Итак пошаговый мануал для владельцев Routerich, как завести Zeroblock+Zapret2 на дефолтных настройках".  
Я дошел до пункта что через 5 минут появится Zapret2 в службах, но ничего не произошло и не появился Zapret2. Еще раз запустил скрипт5, но все по-прежнему к закрытым сайтам доступа нет.
Что нужно сделать чтобы заработало?

---

**2026-04-10T11:39:39 | Роман**
Вы на подкоп уважаемый zeroblock ставите?
Перечитал внимательнее, делайте сброс на заводские (через интерфейс) и устанавливайте zeroblock по мануалу.

---

**2026-04-10T11:51:09 | Routerich**
Здравствуйте.
у вас ZeroBlock?

---

**2026-04-10T11:51:52 | Routerich**
Службы->Zeroblock->секции маршрутизации->

---

**2026-04-10T12:02:09 | Mikhail Velichko**
Все же  подскажите, пожалуйста, как исключить конфликт Zeroblock с условным корпоративным VPN, при условии что последний запускается на клиенте роутера, а не на самом роутере.

---

**2026-04-10T12:07:25 | Alex L**
У меня не перезапускается , в секциях её нет . Сделал сброс до заводских , поставил zeroblock по инструкции . Сменил dns на 9999/8888 , всё заработало . Почему опера не запустилась ?

---

**2026-04-10T12:14:15 | Routerich**
сервер DNS измените на 9.9.9.9 в настройках ZeroBlock

---

**2026-04-10T12:39:24 | M D**
Просто для уточнения,  zeroblock уже может принимать happ подписки. Или мне продолжать vless ссылки выковыривать?

---

**2026-04-10T12:47:44 | Роман**
Телега в прокси через уважаемый zeroblock (как и всё остальное для чего требуется прокси - свои сервера) - ютуб и дискорд через запрет 2.

---

**2026-04-10T12:48:15 | Nook Scheel**
Фнукциональность в zeroblock есть но на более менее живых не работает

---

**2026-04-10T12:48:31 | Nook Scheel**
Я написал свою проксю через которую сам zeroblock стучится

---

**2026-04-10T12:49:01 | Игорь**
А что такое zeroblock?

---

**2026-04-10T12:49:54 | Bullet for my valentine Poison**
Система-пакеты-обновить списки-слева в фильтр вписать"zeroblock"-обновить

---

**2026-04-10T12:51:26 | Роман**
ZeroBlock — продвинутая система маршрутизации для OpenWrt, использующая sing-box в
качестве основного движка, xray-core в качестве вспомогательного (для транспортов xhttp и
mKCP) и TrustTunnel для шифрованных туннелей. Система обеспечивает прозрачную маршрутизацию трафика на основе списков доменов и IP-адресов через прокси-серверы или VPNинтерфейсы.
Для чего это нужно: Представьте, что ваш роутер — это умный диспетчер на
перекрёстке. Обычно весь ваш интернет-трафик идёт по одной дороге напрямую.
ZeroBlock позволяет направлять трафик к определённым сайтам (YouTube, Telegram
и др.) по альтернативным маршрутам — через прокси-серверы или VPN-туннели.
При этом всё происходит прозрачно: вам не нужно ничего настраивать на телефонах,
компьютерах или телевизорах — роутер сам решает, какой трафик куда отправить.

---

**2026-04-10T12:51:34 | Игорь**
Слушай а мне поставить zeroblock и zapret 2 лучше роутер откатить на заводские ? Щас у меня, тока скрипт 5 и вроде стратегии для ютуба делал через терминал

---

**2026-04-10T12:57:02 | Владимир Волков**
Вы можете сами себе скрипт написать/переписать с использованием локальных пакетов, но и это может не подтянуть все зависимости. Также без интернета скрипт не проверит состояние/работоспособность разных сервисов.
Если важен инструмент обхода, познавайте Zeroblock

---

**2026-04-10T12:59:37 | Роман**
Да, сброс не помешает. Только учтите, там при автонастройке те-же опера и авг, то что у меня на скриншоте - все мои сервера.
Скрипт 5 устанавливает подкоп, а уважаемый zeroblock его не любит 😁

---

**2026-04-10T13:34:37 | Роман**
Вы в ветке zeroblock, какой подкоп?
У меня тут список, где у вас - ищите.

---

**2026-04-10T13:42:42 | Alex L**
Вопрос . Есть платный квн через cisco anyconnect  . Можно ли , поставив openconnect  , прикрутить его в zeroblock? Или ещё как , чтобы часть списков на него заворачивать , ну или включать когда стратегии перестают работать ?

---

**2026-04-10T13:49:45 | Anna Bagler**
С zeroblock. Cоздать свою секцию с vless, настроить списки.

---

**2026-04-10T13:53:22 | Владимир Волков**
Тема "Zeroblock Beta" - в теме "Wiki" есть полный мануал для него. Поставить зероблок, туда добавить секцию со своим ключом (если ключ работает), добавить списки нужные

---

**2026-04-10T13:53:26 | S**
Подскажите пожалуйста, правильно ли я понял, что zeroblock можно ставить на любой openwrt роутер или только на routerich?

---

**2026-04-10T13:53:47 | Anna Bagler**
Есть полный мануал по zeroblock.

---

**2026-04-10T13:54:58 | S**
С подкопом с недавних пор начало регулярно отваливаться соединение с сервером, думаю zeroblock попробовать

---

**2026-04-10T13:58:38 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock
Автонастройку можете пропустить, создать секцию, вписать vless, выбрать списки.

---

**2026-04-10T14:35:20 | Никита**
Добрый день всем!
 На iPhone App Store работает нормально — все открывается, приложения скачиваются без проблем.

Но на ноутбуке (macOS) ситуация странная: сам App Store открывается, страницы приложений загружаются, но при нажатии кнопки «Скачать» или «Установить» ничего не происходит.

Прикладываю два скрина конфигурации роутера и ZeroBlock.

Кто-нибудь сталкивался с такой проблемой? В чем может быть причина — в настройках роутера, ZeroBlock или самого macOS? Как это можно исправить?

---

**2026-04-10T14:38:13 | Анатолий**
Добрый день. Подскажите пожалуйста. Не могу установить Zeroblock

---

**2026-04-10T15:07:47 | Александр Меркушев**
Вот вывод терминала:

Анализ запущен: 2026-04-10 15:03:55
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
  Facebook IP:  198.18.0.104 | YouTube IP:  173.194.221.93

= ИНТЕРФЕЙС awg10 (ДЕТАЛИ):
  Статус                : UP (ON)  ↓10.71 MB / ↑0.31 MB
  Пинг (ya.ru via awg10): 23.454 / 28.886 ms (0 из 10 потеряно)
  Программы в автозапуске: zeroblock opera-proxy youtubeUnblock

= ПРОВЕРКА ДОСТУПОВ (WWW.YOUTUBE.COM):
  OPERA (Proxy): ОФЛАЙН  !!!_ОПЕРА ЗАБЛОКИРОВАЛА РОССИЮ_!!! 
  awg10 (IPv4) : ОНЛАЙН (HTTP/2 200 OK) [tlsv1.2] [try: 3]
  Запускаем остановленные службы, ожидайте...
--------------------------------------------------------------
  ! Диагностика DNS (youtube.com):
    Server:     127.0.0.1:53
    Name:       youtube.com        Address: 64.233.162.93
    Name:       youtube.com        Address: 64.233.162.136
    Name:       youtube.com        Address: 64.233.162.91
    Name:       youtube.com        Address: 64.233.162.190
--------------------------------------------------------------

= СТАТУС СЛУЖБ (НЕ УСТАНОВЛЕННЫЕ НЕ ОТОБРАЖАЮТСЯ):
  zeroblock       | RUNNING                        | РАЗРЕШЁН
  sing-box        | RUNNING (MANAGED BY ZB)        | ОТКЛ
  opera-proxy     | RUNNING                        | РАЗРЕШЁН
  youtubeUnblock  | RUNNING                        | РАЗРЕШЁН

= ПЕРЕСЕЧЕНИЯ ДОМЕНОВ И АНАЛИЗ КОНФИГУРАЦИИ:
  !!!_КРИТ: Внутреннее пересечение в zeroblock:
    zeroblock                 : opera (Условия: default)
    Домены: telegram.org 

  !!!_КРИТ: Внутреннее пересечение в youtubeUnblock:
    youtubeUnblock            : YouTube (Условия: default)
    youtubeUnblock            : YouTube (Условия: default)
    Домены: googlevideo.com youtube.com 

  zeroblock              awg10 (vpn): anime,block,googleplay,meta,news,porn,socials,video
  zeroblock          opera (prx out): ai,geoblock,discord
  zeroblock        DNS/Bootstrap DNS: (doh) 8.8.8.8 / 77.88.8.8
  Секция в режиме catch-all: vps
  Версия zeroblock: 0.7.2-r55

= СИСТЕМНЫЕ РЕСУРСЫ:
  LAN IP: 192.168.1.1 (Прошивка: 24.10.5)
  CPU: 0.24 | RAM: 26% | NAND: 48% занято / 34.9M доступно
  0 3 * * * /usr/bin/zeroblock system_monitor >/dev/null 2>&1
  0 9 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-04-10T15:19:42 | Grigory**
Есть люди у кого провайдер билайн и роутерыч(zeroblock+zapret2)?

---

**2026-04-10T15:21:32 | DedLovesFrogs**
Извиняюсь, что немного туплю, но: я почитал документацию на ZeroBlock я правильно понимаю, что можно отключить  awg и включить xray-core (у меня есть конфиг xhttp + reality) после первоначальной настройки Zeroblock?
(Я просто сейчас не имею доступа к роутеру).

---

**2026-04-10T15:43:45 | Anna Bagler**
Zeroblock xray поддерживает.

---

**2026-04-10T15:49:04 | Kiss_My_Axe**
Не обязательно делать отдельную секцию, но желательно.
И если по каким-то причинам ZeroBlock ну никак не подходит, рассмотрите вариант Podkop-Plus на гите.
Это форк, в котором интерфейс человеческий сделали.

---

**2026-04-10T15:57:09 | Val**
Спасибо. То есть сейчас лучше сбросить настройки и установить ZeroBlock или он с подкопом не конфликтует?

---

**2026-04-10T16:09:31 | Mikhail Velichko**
Так, как я понимаю, после установки Zeroblock добавляет правила для перехвата всех DNS запросов от всех клиентов. В том числе и при включении условного корпоративного VPN на клиенте, запросы перехватываются и те, что должны были уходить на DNS сервера тунеля. Как можно этого избежать?

---

**2026-04-10T16:19:56 | Anna Bagler**
Не трогать. Захотите свежее, лучше сброс и zeroblock.

---

**2026-04-10T16:27:08 | Anna Bagler**
Останавливаем zeroblock. Cмотрим на обычные ресурсы. Потом останавливаем zapret2. Cмотрим. Это можно сделать на соответствующих страничках в Службах.

---

**2026-04-10T16:28:42 | Anna Bagler**
Галочкой исключите торрент-трафик в zeroblock.

---

**2026-04-10T16:29:47 | Некит**
ребят вопрос, позавчера ставил последнюю прошивку и пропал podkop и zapret, потом всё накатил с помощью zeroBlock, и вопрос в следующем если я сейчас заново накачу прошивку так же всё слетит? Или же как удалить Zeroblock и zapret2, так как непривычно с ними работать? Что вообще надо сделать чтоб остался podkop и zapret?

---

**2026-04-10T16:34:21 | Anna Bagler**
Вам для подкопа с таким сценарием нужен свой vless. А лучше сбросить настройки роутера и поставить zeroblock https://t.me/routerich/394153/405571

---

**2026-04-10T16:47:51 | Anna Bagler**
Конфиги разные, проблемы будут. Лучше переходите на zeroblock.

---

**2026-04-10T16:56:31 | Maxim**
Я удалил Podkop, установил ZeroBlock + Zapret2, изменил DNS на 9.9.9.9 и вроде всё пока что работает.

---

**2026-04-10T17:02:33 | Anna Bagler**
Zeroblock и привязать к своей секции. В секцию списки. Или будет все в себя ловить.

---

**2026-04-10T17:09:12 | Hump Dog**
Fri Apr 10 17:07:30 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[zeroblock] ZeroBlock stopped successfully
Fri Apr 10 17:07:35 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock(0.7.2-r55)...
[subscription_parser] Subscription profile: 🐾 Лягушка КВН
[zeroblock] ZeroBlock started successfully
Да как бы ничего, если здесь

---

**2026-04-10T17:09:35 | Алексей Михайлов**
спасите....

Fri Apr 10 17:03:44 2026 user.notice zeroblock: Stopping ZeroBlock...
[zeroblock] Stopping ZeroBlock...
[cron_manager] Cron file not found: /etc/crontabs/root
[zeroblock] ZeroBlock stopped successfully
Fri Apr 10 17:03:48 2026 user.notice zeroblock: No sections yet, but auto-config enabled
Fri Apr 10 17:03:48 2026 user.notice zeroblock: Starting ZeroBlock...
[zeroblock] Starting ZeroBlock(0.7.2-r55)...
[health_monitor] Opera Proxy is not working
[zeroblock] ZeroBlock started successfully
[cron_manager] Cron file not found: /etc/crontabs/root
[health_monitor] Opera Proxy is not working
[health_monitor] Failed to recover Opera Proxy

---

**2026-04-10T17:12:24 | Woohard**
ну т.е. сбрасываются только настройки, но не прошивка?
Я хочу на чистую попробовать этот zeroBlock новомодный настроить, до этого только пятым скриптом пользовался успешно

---

**2026-04-10T17:14:01 | Михаил Аржанников**
Я полистал чат, но умнее не стал, киньте пож в меня пару советов.

У меня ZeroBlock. Внутри ZeroBlock:

- opera (работало до сегодняшнего дня норм, сегодня работает скрипя зубами, оч медленно)
- awg10 (через нее ничего никогда не получалось завести)

Прошивка роутера актуальная. DNS внутри opera по совету выше менял на 9.9.9.9 (так все что завернуто в opera совсем переставало работать).

Имею свои прокси на socks5 и впн vless.

Пытался в ZeroBlock - opera выставить "Тип конфигурации прокси": "URL прокси" - вставлял туда socks5 - не работает. Через vless всё ОК.

Что еще можно понастраивать для работы всякого вместо использования своего vless?

---

**2026-04-10T17:44:06 | Nick Chernobaev**
Здравствуйте. Установил zeroblock opera и awg10 по вашей видеоинструкции. Подскажите как теперь включить заблокированные сервисы?

---

**2026-04-10T17:47:43 | Anna Bagler**
Лучше иметь свой vless. Cоздать свою секцию, выбрать нужные списки и добавить свой vless в URL-конфигурацию.
А так, изучайте полный мануал к zeroblock по работе с секциями и списками. Сегодня бесплатная опера плохо себя чувствует и списки в ней могут не работать. Пробуйте менять DNS.

---

**2026-04-10T17:47:52 | Woohard**
Оп-паа, спасибо за ответ!
Уже сделал сброс до заводских, завел на zeroBlockе. Пока посижу так понаблюдаю тогда. Но метод со скриптом был самый удобный для меня всегда. В прошлый раз когда все намертво полегло, обновление прошивки спасло

---

**2026-04-10T18:00:11 | Val**
Если кому-то интересно, у кого сегодня начались проблемы - я снёс скрипт #5 и поставил вместо него ZeroBlock - всё заработало и файлы в ТГ теперь грузятся гораздо быстрее. Спасибо @Az098yosflasd7tow4

---

**2026-04-10T18:05:13 | Val**
Т.е. zeroblock тоже может отвалиться?

---

**2026-04-10T18:06:03 | Виталий Александрович**
Какие у вас dns настроены zeroblock?

---

**2026-04-10T18:07:45 | Nick Chernobaev**
Читаю мануал по zeroblock. Все очень техническим языком написано. Нет ли краткой инструкции как настроить секции на ютуб и тг для полных профанов как я в этом?

---

**2026-04-10T18:09:06 | Val**
система - пакеты - обновить списки - в "фильтр" ввести ZeroBlock и отобразить "все". Далее установить ZeroBlock и после него ZeroBlock Luci

---

**2026-04-10T18:09:50 | Nick Chernobaev**
Это уже установил. Имею ввиду как теперь включить запрещенку через zeroblock

---

**2026-04-10T18:10:29 | Anna Bagler**
Если вы zeroblock уже по краткой инструкции/видео настроили, то YouTube должен работать.

---

**2026-04-10T18:19:06 | Anna Bagler**
youtubeUnblock отключайте и останавливайте или удаляйте вообще. И прижмите галочки для запрет2 в автонастройках zeroblock. Потом стратегию для zapret2 пробовать.

---

**2026-04-10T18:22:45 | Алексей**
Подскажите пожалуйста,zeroblock нужно ставить если так всё работает?

---

**2026-04-10T18:27:27 | Евгений Макаренко**
ZeroBlock
Маршрутизация трафика через прокси и VPN по спискам доменов. Версия: 0.7.2-r55

---

**2026-04-10T18:34:17 | Anna Bagler**
Zeroblock запустите. Если провайдер не требует, ipv6 на роутере отключите.

---

**2026-04-10T18:37:43 | Anna Bagler**
Опера приболела. Пробуйте cменить DNS в настройках zeroblock. Список Мессенджерс у вас уже есть.

---

**2026-04-10T18:58:30 | Routerich**
Если у вас Podkop, то

переносите Telegram из секции с VPN awg10 (WARP) в секцию с  Opera (Proxy) или в свою секцию (если она есть у вас)
через WARP Telegram болеет.

Если у вас ZeroBlock

перенесите список Messengers из секции awg10 в секцию Opera

---

**2026-04-10T19:05:53 | Routerich**
Вам легче роутер сбросить и заново настроить и потом zeroblock поставить

---

**2026-04-10T19:19:59 | мелкий цуко**
Доброго времени суток всем. Может кто подскажет в какую сторону копать. Установлен ZeroBlock на RR,  добавлен дополнительный интерфейс AWG2, он же добавлен в аналогичную доп. секцию в ZeroBlock (AWG2) и на  для теста 2ip.ru, 2ip.io и xerox.com. С компа и по ВиФи всё отлично работает открывается и xerox.com и 2ip.ru показывает ip что на AWG2. На роутере поднять от команды RR для подключения с телефона интерфейс Tailscale, а также до того как поднять Tailscale, был поднял сервер OpenVPN. И тут ситуация, при подключении с телефона через Tailscale, сайты добавленные в секцию AWG2, wg10 и opera открываются на ура согласно секциям, при подключении через  OpenVPN все сайты из секций awg10 и opera открываются, но будто игнорят секцию AWG2. Может кто сталкивался с подобным?

---

**2026-04-10T19:23:30 | Routerich**
Добавить свой квн в Podkop/zeroblock и подкинуть его туда

---

**2026-04-10T19:24:32 | Виталий Александрович**
Свой квн в zeroblock есть, подкинуть его туда это что?

---

**2026-04-10T19:34:26 | Vvv Vvv**
Приветствую, перенастроил роутер на zeroblock, по прокси оперы всё понятно, оставил телеграмм на awg10 и он работает на компе через провод, но не через wi fi на смартфонах, куда копать?

---

**2026-04-10T19:38:23 | мелкий цуко**
Доброго времени суток всем. Может кто подскажет в какую сторону копать. Установлен ZeroBlock на RR,  добавлен дополнительный интерфейс awg20, он же добавлен в аналогичную доп. секцию в ZeroBlock (awg20) и на  для теста 2ip.ru, 2ip.io и xerox.com. С компа и по ВиФи всё отлично работает открывается и xerox.com и 2ip.ru показывает ip что на awg20. На роутере поднять от команды RR для подключения с телефона интерфейс Tailscale, а также до того как поднять Tailscale, был поднял сервер OpenVPN. И тут ситуация, при подключении с телефона через Tailscale, сайты добавленные в секцию awg20, wg10 и opera открываются на ура согласно секциям, при подключении через  OpenVPN все сайты из секций awg10 и opera открываются, но будто игнорят секцию awg20. Может кто сталкивался с подобным?

---

**2026-04-10T19:51:00 | M D**
Кто-нибудь настраивал delta chat с zeroblock? Аудио/Видео звонки не проходят.

---

**2026-04-10T20:00:49 | Anna Bagler**
Zeroblock ставьте. И над своим vless думайте.

---

**2026-04-10T20:00:58 | Евгений Макаров**
Добрый вечер. Кто нибудь пробовал вручную обновлять списки в ZB через команду "ubus call zeroblock reload '{"scope":"lists"}'"?
У меня ошибка выскакивает "Command failed: Not found"

---

**2026-04-10T20:18:42 | Maxim**
ZeroBlock + Zapret2 и всё работает (пока что).

---

**2026-04-10T20:40:01 | Maxim**
Пробуйте ZeroBlock + Zapret2

---

**2026-04-10T20:43:01 | Bumbon4ik**
Подскажите, пришёл роутер, запустил zeroblock вроде настроил всё, всё работает, подключил свой amneziaVPN , все сайты работают, телега работает.
НО telemt MTProxy не может подключиться к серверам телеги почемуто. сейчас удалил zeroblock и установил podkop, с ним MTProxy сразу заработало

---

**2026-04-10T20:44:26 | Anna Bagler**
Zeroblock.

---

**2026-04-10T20:46:10 | B R**
Я правильно понял, что podkop и zapret надо поменять на zeroblock и zapret2?

---

**2026-04-10T20:52:57 | Maxim**
Я добавлял в ZeroBlock/Секции маршрутизации/awg10/Изменить/Списки/Ввод пользовательских доменов - Динамический список. И там в следующей строке добавлять каждый домен по 1 штуке.

---

**2026-04-10T21:01:44 | Kris Krets**
Zeroblock awg warp

---

**2026-04-10T21:03:19 | B R**
Ага, спасибо, завтра попробую. 

Еще вопрос - я все это добро ставил скриптом номер 5, теперь zeroblock и zapret2 ставлю руками после сброса роутера в дефолт. Верно? 

Для zeroblock инструкцию уже нашел, читаю :) 

Всем спасибо, что помогаете новичкам. Встретить нетоксичное рукомьюнити прям удивительно для меня)

---

**2026-04-10T21:12:04 | Alex Korotkov**
Всем салют.
Заметил, что при добавлении vless подписки, в списке не все доступные локации, что у меня есть? У Zeroblock ограничение какое-то или баг словил?

---

**2026-04-10T21:14:58 | Сергей Ларшин**
А замена podkopa на zeroblock не решит проблему с телегой?

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

**2026-04-10T21:36:48 | Gomer Simpson**
ZeroBlock поддерживает икслучи.

---

**2026-04-10T21:37:59 | Gomer Simpson**
ZeroBlock + Zapret2. Соседние темы. Везде есть подробные инструкции .PDF

---

**2026-04-10T21:46:36 | Anna Bagler**
youtubeUnblock удаляйте. Zeroblock по инструкции ставьте https://t.me/routerich/394153/405571
Потом с пылесосом можно пробовать разбираться.

---

**2026-04-10T21:48:40 | Алексей**
У меня нет ZeroBlock, подкоп есть но там нет Оперы. Что делать?

---

**2026-04-10T21:50:22 | Anna Bagler**
Ну, текст Итак пошаговый мануал ... вы же видите, поищите в теме zeroblock.

---

**2026-04-10T21:53:45 | Алексей**
Может снести подкоп и поставить ZeroBlock?

---

**2026-04-10T21:54:03 | Mikhail Velichko**
Разобрался я с проблемой DNS резолвинга при поднятии  VPN туннеля  на клиентах роутера  - проблема оказалась не в Zeroblock и перехвате DNS, а в опции Защита от DNS rebinding в общих настройках DHСP  и DNS.

---

**2026-04-10T22:04:13 | Mikhail Velichko**
При подключении к условному корпоративному OpenVPN на ПК, игнорировались пропушенные "внутренние"  DNS и все запросы все равно шли через DNS роутера. Грешил на Zeroblock и dns hijack, но оказалось  что дело в базовой настройке DNS  Защита от DNS rebinding активной по умолчанию. Как-то так )

---

**2026-04-10T22:11:04 | Алексей**
Ребята,сегодня установил Zeroblock.Действовал по мануалу для чайников из закрепленного сообщения.Вроде разобрался со всем этим хозяйством,хоть и со скрипом мозга,но почему-то в вебморде в разделе Службы никак не хочет появляться zapret2.Список пакетов успешно обновляется и там указано,что zapret2 и lucy zapret2 установлена,а в разделе Службы на вебморде он так и не появился(И ещё Телеграмм стал очень плохо работать.На последней версии Подкопа как-то всё повеселее было до сегодняшнего дня.Но вот сегодня с утра совсем всё плохо с интернетом стало.Видимо РКН там очередной рубильник выключили.Пришлось заморачиваться с установкой Zeroblock

---

**2026-04-10T22:30:53 | Gomer Simpson**
Пошевелите её, стоп/старт, рестарт ZeroBlock, ребут ровтера.

---

**2026-04-10T22:47:46 | Артём**
Начал ставить zeroblock+zapret2 по мануалу, но в п.6 не отображаются активными 1 и 2 (вроде как установлены). Следовательно в 7 пункт данного манула не появляется zapret 2 в службах.

А в Zeroblock такие логи.

Сайты вроде rutracker, YouTube не открываются. А хотелось бы)

---

**2026-04-10T23:00:42 | Anna Bagler**
Изучите интерфейс службы Zeroblock.

---

**2026-04-10T23:01:14 | Bumbon4ik**
а почему zeroblock может не сохранять настройки маршрутизации? я удаляю оперу, нажимаю применить, а она возвращается, настройки списков тоже обратно возвращаются аи и геоблок на оперу, остальное на awg. секция ютуб в awg тоже при сохранении возвращалась

---

**2026-04-10T23:28:06 | Woohard**
Господа, чистый обход через ZeroBlock и запрет 2 сегодня накатил после смерти оперы, полет вроде ок, но ТГ не работает в мобильном приложении, на пк работает. С чем может быть связано?

---

**2026-04-10T23:32:42 | Woohard**
Господа, чистый обход через ZeroBlock и запрет 2 сегодня накатил после смерти оперы, полет вроде ок, но ТГ не работает в мобильном приложении, на пк работает. С чем может быть связано?

---

**2026-04-10T23:44:36 | Bumbon4ik**
одно я понять не могу, почему на роутере, где удалён zeroblock пишет warp не подключён на странице обзора, хотя я так понял это от зероблок идёт эта надписаь, а там где зероблок поставлен роутер, там нету ничего про warp

---

**2026-04-10T23:56:29 | Woohard**
ах, искал я вовсе не то, пункт Messengers а не Telegram нужен был. Олень, выходит.
Забросил адреса туда как в чате ZeroBlock, все равно на телефоне телега мертва.
Попробую перекинуть в секцию Opera

---

**2026-04-11T00:05:06 | Bumbon4ik**
вот у меня на платном awg на zeroblock телега плохо работала, а mtproxy вообще не работал, пока ip в ручную не добавил все

---

**2026-04-11T00:06:08 | Anna Bagler**
Отключите zeroblock, tailscale и попробуйте ещё раз списки обновить.

---

**2026-04-11T00:44:22 | Woohard**
Заработал тг на телефоне.
Сегодня снес настройки в завод, поставил метод ZeroBlock плюс Zapret 2, когда все у всех отвалилось. СИдел на пятом скрипте до этого всегда.
Всё заработало, кроме тг на телефоне.
Сейчас поставил по приколу поверх этого всего пятый скрипт снова, телегу убрал из списков подкопа, вроде работает теперь на телефоне тг

---

**2026-04-11T00:49:17 | Iceking**
Господа, прошу помощи. В ZeroBlock есть 2 секции, Германия на все, Англия на ютуб. Обе секции сегодня перестали работать с разницой 2-3, пинг не пишут, только N/A. Перезапустил интерфейсы этих секций - все заработало. В чем может быть причина? Можно настроить автоматическую перезагрузку интерфейса, если подобное происходит?

---

**2026-04-11T00:52:23 | Anna Bagler**
Вникайте. Сеть - Интерфейсы, Система - Пакеты, Настройки zeroblock.

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

**2026-04-11T01:11:01 | Anna Bagler**
И этот vless в zeroblock не работал?

---

**2026-04-11T01:21:05 | Роман**
1 - да. 
2 - да. 
3 - у вас там подкоп не затесался совместно с zeroblock ?
Скриншоты тоже бы не помешали, диагностику.

---

**2026-04-11T03:21:43 | Routerich**
#ZeroBlock по хештегу отслеживать изменения в новых версиях и если исправлен какой-то критический баг или добавлена новая функция - то обновлять

---

**2026-04-11T04:39:04 | Alex_Jester**
Сеть - интерфейсы 
Создаёшь нужный тебе интерфейс, вставляешь свой конфиг, настраиваешь firewall, снимаешь галки с opera и awg в Zeroblock и выбираешь в списках нужные тебе секции.

---

**2026-04-11T04:45:41 | Alex_Jester**
В разделе Zeroblock есть мануал, как установить. Смотри в закреплённых сообщениях. Если до этого стоял подкоп, то его удали.

---

**2026-04-11T06:30:40 | Routerich**
Здравствуйте.
У всех.
Пробуйте это
так же в ZeroBlock, в настройках, изменяем  сервер DNS на 9.9.9.9

---

**2026-04-11T06:43:13 | IT**
Пока нет возможности, в zeroblock настроить резервный канал? Типо если awg0 недоступна, то пустить по awg1

---

**2026-04-11T06:49:23 | Maxim =)))**
По итогу что делать то?
Сносить ZeroBlock и ставить скрипт 5?

---

**2026-04-11T07:02:31 | Константин**
Так теперь из списка он пропал как luci zeroblock

---

**2026-04-11T07:25:01 | Kiss_My_Axe**
У вас ютуб в подкопе и запрете. Выберите что-то одно.
Переходите на ZeroBlock.

---

**2026-04-11T07:25:59 | Андрей**
добавили бы по ZeroBlock информацию в Wiki.

---

**2026-04-11T07:27:52 | Kiss_My_Axe**
Она там есть, насколько мне известно.
Есть отдельный раздел Zeroblock, в нём закрепы, в закрепах тоже ссылка на инструкцию есть.
Проблема в том, что собой и сами занимаются единицы. Остальные ждут, когда им покажут, где что лежит.

---

**2026-04-11T08:52:21 | Вячеслав Шевченко**
Всем доброе утро. телеграмм на в zeroblock в нем опера прокси и awg10 так вот в прокси воообще тишина. а в awg работает оооочень медленно и доооолго подключается. что то можно попытаться исправить? может какой то новый способ обхода появился или стратегия или обновление вышло?

---

**2026-04-11T09:13:52 | Kirill Y**
Так в zeroblock скрипта вроде нет.. Или Вы советуете на podkop перейти на 5-й скрипт или бету?

---

**2026-04-11T09:59:01 | BopKyTa**
Добрый день. Я запускал зероблок по инструкции. Интерфейс опера до вчерашнего дня работал, вчера поднял влесс. Но AWG-Warp никогда не видел в ZeroBlock. Почему?

---

**2026-04-11T10:06:29 | Nick Chernobaev**
Добрый день. @bagleranna попробовал как вы вчера сказали сменить dns в опера в zeroblock. Все правильно сделал? Прикладываю терминал проверку.

Ютуб работает как работал. А тг, инста и гпт нет

Что сделать еще можно чтобы запустить эти сайты? Главное чтобы ютуб не поломать 🙏:)

---

**2026-04-11T10:27:54 | Роман**
На своём всё прекрасно работает и с подкопом, и с уважаемым zeroblock. Любой ценой, но бесплатно, понимаю.

---

**2026-04-11T11:14:42 | Миша Луничев**
Все привет подскажите пожалуйста в чём может быть беда и куда копать, вчера отвалился подкоп не заглужал list телеги клаудфаера и меты, установил  zeroblock вроде более менее настроил дигноситка показывает всё кул кроме   
FakeIP (клиент)  Не удалось проверить: Failed to fetch
Но на mac по wifi всё работает вроде стабильно, а на телефоне не открывается ни тг ни тик ток ни некоторые игры, при том что если закинуть домены игр в оперу 1 открывается другая нет, щас упала опера и не поднимается, закинул и домены в qwg  и ip нужных приложений не спасло, по логам кроме того что опера померла всё ок вроде. Подскажите куда смотреть пожалуйста

---

**2026-04-11T11:20:36 | Роман**
С оперой общая проблема, попробуйте обновить пакет оперы. И я бы не стал устанавливать подкоп и zeroblock вместе. 
Если есть свой vless или другие варианты - замените оперу на них.

---

**2026-04-11T11:57:29 | Sergey G**
Через авг тг - то подключится, то отключится(
В данный момент тг работает при использовании бесплатных mt proxy, заданных в моб. приложении
Есть ли какой то вариант подружить zeroblock с этим типом прокси?

---

**2026-04-11T12:14:42 | Александр Ёлохов**
Добрый день.
Поставил себе Zeroblock и Zapret2, ютуб, мета, дискорд, все работает, но не работает телеграмм, подскажете что сделать можно?

---

**2026-04-11T12:59:20 | GREY**
Странная проблема.
При включенном Zeroblock, Xbox 360 выдает MTU Error (даже если консоль в исключениях или в полной маршрутизации). 
При выключенном, подключается без проблем (без VPN или чего-либо еще).
По сути роутер чистый, устанавливался только zeroblock и zapret2.
Есть идеи?

---

**2026-04-11T13:18:47 | ᅠ ᅠ**
Щас сделал так, чтобы появился Zeroblock и zapret2

---

**2026-04-11T13:21:01 | ᅠ ᅠ**
Это в zeroblock там где автозагрузка?

---

**2026-04-11T13:31:08 | Алексей Сергеевич**
@RouterichSupport  подскажите пожалуйста - поднял интерфейс awg20 WireGuard в zeroblock перенес в него списки и остальные интерфейсы потушил. Телега заработала, а вот Google AI не хочет, что нужно сделать чтобы заработало(раньше работало в Opera Proxy)? Как я понял нужно скрыть свой ip адрес?

---

**2026-04-11T13:32:50 | GREY**
Я ничего не понимаю. Проверил в yacd, zeroblock правильно перенаправляет трафик, но xbox не может подключится, пока тот включен. Напрямую или vpn, не важно. MTU Error. При выключенном zeroblock и напрямую - работает.

---

**2026-04-11T13:41:02 | GREY**
Может Zeroblock меняет MTU значение (Google пишет, что 360-й ожидает 1400-1500)? Только поставив IP Xbox 360 в исключения настройках всего Zeroblock (а не в правилах маршрутизации), он смог подключиться. Как временное решение пойдет? Мне все же его надо пробрасывать через VPN иногда. Я в этом мало понимаю, так что догадки из заднего места.

---

**2026-04-11T13:44:02 | GREY**
Ну да, как и я написал, это я сделал и помогло. Но, мне нужен VPN для скачивания некоторых вещей из Xbox Live. Если он хоть как-то взаимодействует с Zeroblock - ошибка

---

**2026-04-11T13:46:59 | GREY**
Если его засунуть в секцию маршрутизации - MTU Error, даже если он в исключениях
Я его засунул в Настройки - Исключенные IP. Тогда он исключен из ZeroBlock полностью. И тогда ошибки нет

---

**2026-04-11T13:47:39 | iProxx**
Всем привет! Есть арендованный vps с установленным Xray (vless).
Хочу добавить конфиг на роутерич. Добавляю в Zeroblock новую секцию, выбираю Xray конфигурация Outband, копирую конфиг в формате JSON. В списках сообществ выбираю то что мне нужно. Сохраняю применяю. Перезапускаю Zeroblock.
В информации о сервисах выдает: xray остановлена.
Что я упускаю?

---

**2026-04-11T13:48:38 | ZZII | RTK**
что вообще лучше, podkop или zeroblock? просто у меня какие то проблемы с ним, то некоторые сервисы не работают, включаю и отключаю какие то сообщества - начинает работать. что делать, вообще не понимаю

---

**2026-04-11T13:50:03 | Anna Bagler**
Zeroblock предпочтительнее.

---

**2026-04-11T14:03:22 | Александр**
Добрый день. В zeroblock убрал из списков сообщества ют,  он работает, а вот с телегой так и сложности.

---

**2026-04-11T14:18:17 | Роман**
Ютуб - Дискорд через запрет 2 (нагрузка пр трафику большая), остальное в свой прокси. 
В подкопе только удаление секций - нет отключения.
А вот zeroblock "кушает" xhttp из коробки и есть отключение секций 😁

---

**2026-04-11T14:20:11 | Юстас Фенакертибан**
В связи с последними событиями предлагается добавить в ZeroBlock третью предустановленную секцию - Tor. 
Это возможно?

---

**2026-04-11T14:22:53 | ᅠ ᅠ**
В zeroblock?

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

**2026-04-11T14:45:03 | BigSix**
Добрый день, сейчас установил zeroblock по вот этому мануалу, но нет секции опера-прокси есть только awg10

---

**2026-04-11T14:45:46 | ZZII | RTK**
что вообще лучше, podkop или zeroblock? просто у меня какие то проблемы с ним, то некоторые сервисы не работают, включаю и отключаю какие то сообщества - начинает работать. что делать, вообще не понимаю

---

**2026-04-11T14:46:15 | Routerich**
Zeroblock более функциональный

---

**2026-04-11T14:46:28 | Anna Bagler**
Вам уже отвечали, zeroblock.

---

**2026-04-11T15:17:16 | Ghost**
подскажите пож-та у кого получилось настроить доступ к Copilot через ZeroBlock/Zapret2 - как вы этого добились?

---

**2026-04-11T15:33:37 | Dmitriy Vavilov**
zeroblock не ищется

---

**2026-04-11T15:33:58 | Роман**
Купить. Купить сервер - поднять самому панель. Найти подписку на халяву (требуется zeroblock).

---

**2026-04-11T15:35:17 | Bullet for my valentine Poison**
не растет кокос!
Плачут, богу молятся, не жалея слёз
Плачут, богу молятся, не жалея слёз
zeroblock не ищется, не растет кокос!

а если серьезно, обновить списки в пакетах. Либо прошивку до последней.

---

**2026-04-11T15:36:09 | Максим**
Здравствуйте. Помогите пожалуйста с телеграммом. Не работает совсем. Пробовал переключаться в ZeroBlock, с "awg10" на "opera", и обратно, но телега по прежнему не грузится

---

**2026-04-11T15:40:20 | M D**
Не работает vless у zeroblock сейчас.

---

**2026-04-11T15:42:46 | Николай Каменных**
люди добрые, недавно совсем в этой теме, помогите!
в zeroblock добавил секцию с vless подпиской, перенес туда messengers.
телега завелась, но контент аудио/фото/видео не грузит

---

**2026-04-11T16:06:27 | Routerich**
Zeroblock поставьте, там есть поддержка

---

**2026-04-11T16:15:32 | Андрей**
Привет! я хочу создать 2 интерфейса AmneziaWG (у меня 2 vpn сервера в разных регионах). Первый интерфейс поднялся, на втором handshake не проходит. В чем может быть дело? Какие нюансы есть при поднятии 2 vpn соединений одновременно?
В эти интерфейсы хотел заруливать трафик через zeroblock

---

**2026-04-11T16:28:17 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock
Автонастройку пропустить, создать новую секцию, вписать vless ссылку, выбрать списки.

---

**2026-04-11T16:45:35 | V T**
Добрый день! Не работает телеграмм через приложение на телефонах. WEB-версия на ПК работает. Подскажите, проблема может быть именно через приложение? Или я с настройками что-то накосячил?

Включен Podkop v0.7.14, поменял Bootstrap DNS-сервер на 9.9.9.9. До секции MAIN пингуется, там подключены списки:
1) Meta;
2) Twitter;
3) Telegram;
4) Заблокировать;
5) Google AI;

Так же установлен ZeroBlock 0.6.1-r150 с двумя секциями маршрутизации:
1) opera - тут полностью маршрутизируется только IP адрес ПК. Списки Geo Block, Заблокировать, Meta, Twitter, Google AI;
2) awg10 - тут полностью маршрутизируются все остальные девайсы И исключён IP адрес ПК. Списки YouTube, Meta, Twitter, Telegram, Google AI. Конфиг для этой секции прикреплю скрином к сообщению;

С телефонов нормально работает ютуб/инстаграмм и прочая запрещёнка, настроенная в списках секции awg10 в ZeroBlock'е, но телеграмм через приложение вообще не работает.

---

**2026-04-11T17:13:46 | Alex_Jester**
Добавлением своего AWG 2.0 в Zeroblock

---

**2026-04-11T17:17:15 | Роман**
zeroblock со своими серверами )

---

**2026-04-11T17:22:28 | Роман**
У юаб просто нет интерфейса, установите через пакеты.
Всё пропало - так вы прошили просто, а не через ASU, так и должно быть.
Если есть свои сервера - zeroblock, нет - всё что хотите, на удачу так сказать.

---

**2026-04-11T17:25:32 | Andrew Arzaev**
подскажите пожалуйста это речь идет о - 
zeroblock_0.7.2-r55_aarch64_cortex-a53.ipk
и
luci-app-zeroblock_0.7.2-r55_all.ipk
???

---

**2026-04-11T17:40:52 | Роман**
Можно. Ищите подписку халявную, устанавливайте zeroblock.

---

**2026-04-11T18:02:46 | VIKTOR DMITRIEV**
Ща попробую, мне zeroblock для ютуба нужен на тв

---

**2026-04-11T18:13:37 | Роман**
Смотря какой. Если vless hy2 ss - легко. Подписка - смотря какя (zeroblock). WG, Amnezia - создавать интерфейс и настраивать фаервол.

---

**2026-04-11T18:38:51 | Роман**
Для этого и существуют zeroblock/podkop, они точечно маршрутизируют трфик. Вопрос в том какого вида конфиг.

---

**2026-04-11T18:58:04 | Роман**
Установил пакет из беты DNS failsafe, запустил скрипт диагностики, всё сломалось, скрипт повис, zeroblock отвалился, снёс пакет dns failsafe - новый не могу установить, как чинить?

---

**2026-04-11T19:00:15 | Никита**
Всем привет
: SmartTube — меню грузится, видео на 0:00
Routerich AX3000 + ZeroBlock + Zapret 2. На телефоне и в официальном YouTube всё работает. На Ugoos X4 Pro в SmartTube меню открывается, а видео не стартует (стоит на 0:00, чёрный экран).
Пробовал: все домены для googlevideo, ручной профиль, отключение IPv6, очистка кэша.
Подскажите рабочие стратегии Zapret 2 именно под видео-стримы SmartTube или решение через PowerTunnel.

---

**2026-04-11T19:01:07 | Василий**
Я не могу завернуть во vless игру через zeroblock. Прочитал, что это может passwall2. Хочу попробовать. Если получится - оставлю его. Если нет - верну все в зад)

---

**2026-04-11T19:04:20 | А А**
то есть: система ->восстановление/обновление->Выполнить сброс на заводские настройки-> ставим пакеты: zeroblock, luci-app-zeroblock?

---

**2026-04-11T19:35:05 | Anna Bagler**
Zeroblock и создать свою секцию с proxy и URL.

---

**2026-04-11T19:37:29 | Anna Bagler**
Принцип создания интерфейса один. Потом привязываете к секции в zeroblock.

---

**2026-04-11T19:38:42 | А А**
в zeroblock в секции opera AI есть гугл? отвалился что-то

---

**2026-04-11T19:43:06 | dik23rus**
Всем доброго вечера.
Получил роутер, настроил на обычную работу.
Сейчас хочу настроить доступ к закрытым ресурсам.
Вижу что есть две ветки:
Интернет без границ и ZeroBlock
Подскажите пожалуйста в чем разница и что стабильней?
Заранее благодаю.

---

**2026-04-11T19:49:50 | Routerich**
Zeroblock установили?

---

**2026-04-11T20:01:53 | Timur**
сбросил routerich , скажите что лучше ставить podkop или zeroblock?

---

**2026-04-11T20:09:20 | Bumbon4ik**
Можно для тупого лентяя, zeroblock с нуля ставлю на роутер роутерич, ставлю Галки автоматической настройки, он там качает, устанавливает, и создаёт интерфейс awg10. Так вот этот впн он как то самообновляется или нет?

---

**2026-04-11T20:17:53 | Routerich**
в терминале выполните, потом очистка кеша и должен появиться ваш опенконнект
sed -i 's/amneziawg|wireguard|openvpn|pptp/amneziawg|wireguard|openvpn|openconnect|pptp/g' /www/luci-static/resources/view/zeroblock/section.js

---

**2026-04-11T20:26:23 | ㅤㅤ**
Сейчас настраивался очередной Routerich c нуля, где изначально opera_proxy лежал. 

Мои минимальные условия при которых opera_proxy заводится:
ZeroBlock v0.7.2-r53
luci-app-dns-failsafe-proxy v1.1.1

DNS в ZeroBlock 9.9.9.9
Службы  — DNS Сервисы —DNS over TLS — приоритеты DNS over TLS серверы верхнего уровня как на скриншоте

---

**2026-04-11T20:27:42 | ZZII | RTK**
кто-то может скрин фулл настроек  ZeroBlock?

---

**2026-04-11T20:29:36 | Timur**
скажите а где ключ прописать vless? стоит zeroblock. podkop не стоит

---

**2026-04-11T20:39:44 | Anna Bagler**
Если у вас zeroblock, то есть полный мануал, если подкоп - podkop.net Ceкции.

---

**2026-04-11T20:44:38 | Timur**
поподробнее напишите куда ключ вставлять если стоит zeroblock?

---

**2026-04-11T20:52:55 | Timur**
В zeroblock  понял как создать секцию. Но где прописать ключ?

---

**2026-04-11T20:59:34 | Yiliam**
Подскажите пожалуйста, что не так с zeroblock? Секции маршрутиризации пустые.

---

**2026-04-11T21:01:24 | Anna Bagler**
Исключить трафик торрентов в zeroblock.

---

**2026-04-11T21:04:59 | Anna Bagler**
Спросите тогда у интернета, вам нужен свой vless, конфиг awg или ещё что, что поддерживается zeroblockом.

---

**2026-04-11T21:10:42 | Timur**
а почему через подкоп Вы? а не через zeroblock?

---

**2026-04-11T21:14:16 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-11T21:24:26 | Timur**
а скажите пожалуйста в zeroblock пишет xray остановлен, он установлен, как его запустить?

---

**2026-04-11T21:29:36 | Eugene Baranov**
Кстати, а почему в самом актуальном скрипт (пятом) не используется zeroblock?

---

**2026-04-11T21:33:19 | Yiliam**
Подкоп снес, zeroblock снова переустановил, но ничего не поменялось

---

**2026-04-11T21:33:31 | Eugene Baranov**
Почему тогда рекомендуют именно zeroblock?

---

**2026-04-11T21:35:28 | Anna Bagler**
У вас перенаправлений куча. Сбросьте. Поставьте zeroblock и используйте свой vless.

---

**2026-04-11T21:37:18 | Timur**
а если hysteria 2 ключ в zeroblock , просто   прописываем  json outband или xray outband?

---

**2026-04-11T21:57:37 | Anna Bagler**
Интернет настраивайте. Дальше ставьте zeroblock по пошаговой инструкции. А дальше смотрите. Из коробки запрещенка и не работает. Все в руках пользователя.

---

**2026-04-11T21:58:55 | Кэр Лаэда**
Zeroblock🤔😳

---

**2026-04-11T22:03:55 | Стас Немченко**
Всем доброго времени суток! 
Выполнил автонастройку ZeroBlock, проставив первые 4 галочки. По сути всё работает, но в панели управления роутера не появляется веб-интерфейс запрет2, хотя в пакетах всё установлено...

---

**2026-04-11T22:10:14 | Timur**
а zeroblock  чем отличается от podkopa?

---

**2026-04-11T22:38:06 | Anna Bagler**
Если подкоп, то просто конфигурацию у main смените. Если zeroblock, познакомьтесь с интерфейсом для начала и мануал полный изучите, там примеры есть.

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

**2026-04-11T22:58:13 | Sergio Yakovlev**
как добавить приложение lampa вZeroBlock

---

**2026-04-11T22:59:45 | Eugene Baranov**
Не, это вы врываетесь в переписку, не читая её. Мы с товарищем переписывались начиная с моего сообщения:
Кстати, а почему в самом актуальном скрипт (пятом) не используется zeroblock?

Речь идёт о самом актуальном на данный момент скрипте. А какая у него цифра - без разницы.

---

**2026-04-11T23:04:15 | Kiss_My_Axe**
Нет, ему нужен скрипт реально.
Не надоело звиздякать каждый день - Система - Пакеты, Обновить списки, Фильтр Zeroblock, установить luci-app... итыды и тыпы?

Давай я напишу.

---

**2026-04-11T23:17:20 | Sergey G**
Норм ли такое поведение, что служба zeroblock сама остановилась?
при этом в Диагностика - Показать логи, зафиксирован только последний запуск службы
ну я ее запустил заново, пока работает
просто никогда такого раньше не было, вчера обновил версию с 52 на 55
может быть как то связано с тем, чтобы был установлен xray?

---

**2026-04-11T23:20:53 | Garsia**
У меня тоже после последнего обновления что-то похожее.  Периодически как будто перестаёт работать ZeroBlock - весь трафик  начинает идти напрямую (проверяю по 2ip.ru), ChatGPT начинает писать про региональные ограничения. А потом вдруг через пару минут - опять всё работает. Ни у кого такого не было?

---

**2026-04-11T23:24:08 | Игорь Сандырев**
Добрый вечер! Настроил zeroblock, Подскажите почему десктопный телеграм нормально грузит, а с телефона не грузит?

---

**2026-04-11T23:24:27 | Василий**
Подскажите, сижу на ZeroBlock , отключил и podkop и zapret. Перенес список Messengers из секции awg10 в секцию Opera, полет нормальной, кроме телеграм на телефоне.

---

**2026-04-11T23:32:38 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock
Автоустановку пропустить, создать секцию, вписать прокси, выбрать списки.

---

**2026-04-11T23:54:21 | Әмир**
3 раза сбрасывал до завода. После чего пытался zeroblock накатить. Из раза в раз происходила такая чехарда с DNS. (5-ый скрипт не применял)
В итоге, забрал с той квартиры роутер, привёз к себе. Подключил также вторым номером, но через первый - Routerich. На первом отключил Podkop перед манипуляциями со вторым роутером.

В итоге, всё встало, vless поднялся с пол тычка 🤷🏻‍♂️
Мистика какая-то

---

**2026-04-11T23:58:41 | Mike**
получается 5-й скрипт на 80% все? переходить на zeroblock?

---

**2026-04-12T00:25:19 | Anna Bagler**
Если zeroblock, то работать будет. Если подкоп, то нет.

---

**2026-04-12T00:54:38 | Роман**
Установить zeroblock? Поддержка xhttp из коробки.

---

**2026-04-12T00:57:33 | Anna Bagler**
Параграф/пункт 14 в полном мануале по zeroblock.

---

**2026-04-12T01:25:58 | Vyacheslav Shirshov**
А с zeroblock дела еще хуже, нет смысла пробовать?

---

**2026-04-12T01:27:52 | Kiss_My_Axe**
Убрать. Сохранить, применить.
Если рабочий клауд нужен - велкам ту ZeroBlock!

---

**2026-04-12T01:29:54 | Роман**
Единственное что приходит на ум, добавить устройство со шпионом в исключения zeroblock, но запрет думаю видно будет.

---

**2026-04-12T01:51:54 | Джугашвили**
[proxy_parser] Invalid proxy URL
[singbox_gen] Section XHTTP: no parsed proxies from subscription
[zeroblock] ZeroBlock started successfully
вот оно че)

---

**2026-04-12T01:55:29 | Джугашвили**
[zeroblock] Starting ZeroBlock(0.7.2-r55)...
[config_builder] xray-core not found at /usr/bin/xray, xray proxies will be skipped
[singbox_gen] Section XHTTP: proxy requires xray-core (transport=xhttp), skipping
[zeroblock] ZeroBlock started successfully
Упд: а шо, он не видит ядро x-core? Он зависимостями с зероблоком не идёт, дэ?

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

**2026-04-12T03:03:52 | Anna Bagler**
Вам zeroblock бы поставить.

---

**2026-04-12T03:29:48 | Kiss_My_Axe**
Тогда это в терминал.

service ruantiblock stop
service ruantiblock disable
service youtubeUnblock stop
service youtubeUnblock disable
opkg update
opkg install zeroblock
opkg install luci-app-zeroblock

---

**2026-04-12T06:57:40 | Maksim**
Подскажите почему на смартфоне через вифи Ютуб не работает (ну или иногда работает 1 из 10 видео), и так произходит через запрет2, и через zeroblock awg10 и через прикрученный к zb свой квн, но если заюзать через karing этот же квн на смарте с тем же подключение к вифи, или даже через мобильную сеть то всё ок с ютубом

Такая же фигня была и с тг, что он на смарте через вифи не грузился, хотя на пк было ок в это же время, но потом все решилось, я в квн на zb прописал ip и домены тг, но с ютубом так не прокает

Надо как то решить, а то это бред какой-то, юзать вифи на который прикручен квн и поверх этого повторно активировать этот же квн ещё и на смарте 😢

---

**2026-04-12T07:20:32 | Routerich**
В Zeroblock можно подписку добавить.
Это у вас подписка 
https://t.me/routerich/394153/405571

---

**2026-04-12T07:28:42 | Kiss_My_Axe**
Ну мошт про неё составитель списков не знал вообще. А когда было "открыт набор" ресурсов в списки, активная часть ё не упомянула.
Разместите запрос на добавление в разделе ZeroBlock почти не бета.

---

**2026-04-12T07:39:48 | Джугашвили**
Господа, не могу настроить обход в zeroBlock, все через xhttp свой сервер идет. Ютуб, телега и прочие пашут, пяток сайтов добавил вручную- работает лишь часть, (через впн напрямую с пека все открываются), например https://code-basics.com/ru/blog_posts/html-i-css-plan-izucheniya-roadmap-obucheniya

---

**2026-04-12T08:43:42 | Kiss_My_Axe**
В терминале роутера

# 
#
opkg update
opkg install opera-proxy
service zeroblock restart
service podkop restart
#
#

---

**2026-04-12T09:22:51 | Олег Михайлович**
Всем доброго времени суток, у меня нет zeroblock, нет второго списка с дискордом в подкопе, что нужно сделать?

---

**2026-04-12T09:25:00 | Олег Михайлович**
Всем доброго времени суток, у меня нет zeroblock, нет второго списка с дискордом в подкопе, что нужно сделать?

---

**2026-04-12T09:37:14 | Smallin**
Вроде ничего кроме sing и zeroblock zapret amnezia tailscale не ставил))
Что он хочет?
hdp.getServiceInfo is not a function

---

**2026-04-12T09:37:26 | ㅤㅤ**
Крайне любопытно, используете ZeroBlock? Что и где дополнительно прописано? Список AI в opera_proxy? DNS?

---

**2026-04-12T09:52:15 | A V**
Всех с праздником!
Удалось наладить телеграмм через zeroBlock? Чего только не делал, не идёт. И на оперу заводил, поработал чуть и сдох, и в списки awg10 сервера заводил... У меня руки кривые, или бесполезно?

---

**2026-04-12T09:59:26 | Роман**
Вам не поможет с оперой ни подкоп, ни zeroblock, лучше иметь своё.

---

**2026-04-12T10:11:55 | GREY**
Zeroblock и почти все из коробки работает. Заблокированые маршруты через vpn

---

**2026-04-12T10:17:39 | Владимир Волков**
Вам написали - zeroblock

---

**2026-04-12T10:21:49 | GREY**
В Zeroblock теме закреплен гайд, полистайте несколько сообщений. Там и пакеты и инструкция. Все настраивается автоматически, нужно лишь свой конфиг предоставить. Я закинул через awg

---

**2026-04-12T10:43:41 | Святос**
[zeroblock] ZeroBlock started successfully
[config_builder] Sing-box failed to start with full configuration
[zeroblock] Failed to start ZeroBlock

---

**2026-04-12T10:50:33 | Anna Bagler**
Все зависит от того, сможет ли zeroblock поработать с вашей подпиской или сможете ли вытащить из нее прямые ссылки, или запросить прямые ссылки у поставщика.

---

**2026-04-12T11:05:39 | Anton**
Zeroblock если есть, закреп в его ветке

---

**2026-04-12T11:08:59 | Anna Bagler**
В zeroblock.

---

**2026-04-12T11:12:53 | Anna Bagler**
Обновите подкоп. Или со сбросом переходите на zeroblock.

---

**2026-04-12T11:52:04 | Anna Bagler**
Zeroblock и свой vless или что-то другое, что поддерживается.

---

**2026-04-12T11:58:16 | Anna Bagler**
Полный мануал по zeroblock есть. Тип меняете на URL вместо outbound и свой ключ туда. Или есть вариант с подпиской. Как разворачивать, покупать - гугл.

---

**2026-04-12T12:07:24 | Андрей**
Добрый день, направьте пожалуйста по дальнейшим действиям) Не особо силен в терминах, но постараюсь объяснить.

1) Есть уже один роутер routeRich, на нем еще в декабре ставил прошивку последнюю (на тот момент), потом ставил скрипт №5, в итоге ютуб работал через podkop. 
После нового года купил второй роутер, и вот только сейчас решил его настроить (+ на первом роутере ютуб и телеграмм работают через раз). 
Думаю использовать второй роутер для эксперимента: обновить прошивку, поставить скрипт №5 так же и нахваленный ZeroBlock. Норм вариант или лучше пробовать что-то другое сразу ?

2) Думал, что если получится все настроить на роутере, то затем использовать его как Exit Node (видел такое в теме Remote Control) ,  чтобы мобильные телефоны (вне дома) выходили в заблокированные сайты через роутер. Звучит как будто прекрасным вариантом (в плане того, что одна точка входа и одна настройка для всех устройств). Или такое не получится / лучше так не делать ?

3) И еще: у меня есть подписка на отдельном сервисе, который позволяет:
• сгенерить ключ Stealth Proxies (на телефоне им пользуюсь в режиме Proxy/Vpn) через клиент Hiddify и v2rayNG - телеграмм и ютуб работают (правда, частенько страну подключения приходится менять)
• сгенерить ключик для Amnezia WG (на телефоне через клиент Amnezia WG не работает этот подход) 
Может, лучше будет этот ключ подсунуть в роутер ?

---

**2026-04-12T12:13:17 | Sergey G**
Понижать версию zeroblock можно? Если да, то как?

---

**2026-04-12T12:30:13 | Никита Байдин (DOOMGUY)**
Бляха. Я уже час долблюс с этим ZeroBlockом а он Zapret2 не хочет ставить

---

**2026-04-12T12:42:19 | ᚢᚹᛟᛈᛠᛋᛠᛊ ᛖᛊᚺᚱ**
Всем ку, на zeroblock  телега не работает, как порешать?

---

**2026-04-12T13:16:20 | Cloudy ☁️**
Пошаговый гайд по тому, как вбить свой vless-ключ в Routerich:

1. В браузере переходим по этой ссылке
2. Раскрываем вкладку «Службы», в ней — клик по «ZeroBlock»
3. В открывшемся окне кликнуть на «Секции маршрутизации». Снизу будет возможность добавить новую секцию — это и делаем. Вводите нужное вам имя 
4. Во вновь открывшемся окне кликаем на «Тип подключения» — меняем на «Сервер прокси»
5. Появляются новые поля. Нас интересует «URL прокси» — в него вставляем наш vless ключ. Готово
6. Сохраняем, запускаем, включаем и перекидываем на новую секцию нужные списки сообщества, проверяем

---

**2026-04-12T13:53:03 | Роман**
У вас есть такая настройка в подкопе?  Я не могу посмотреть, у меня zeroblock.

---

**2026-04-12T14:12:18 | Александр**
Подскажите, плз, где глянуть состав списков сообщества (которые по умолчанию в zeroblock подтягиваются)?

---

**2026-04-12T14:19:09 | Александр**
Подскажите, плз, где глянуть какие адреса входят в различные списки сообщества (которые по умолчанию в zeroblock подтягиваются)?

---

**2026-04-12T14:32:30 | Антон**
Всем привет. Может, кто подскажет - через секции маршрутизации Zeroblock не открываются ни рутрекер, ни телега. При этом через подключенный клиент Амнезии, который работает через тот же VPS-сервер, все работает. Диагностика никаких ошибок не показывает, все работает

---

**2026-04-12T14:33:08 | Kiss_My_Axe**
В терминале роутера
#
#
opkg update
opkg install opera-proxy
service zeroblock restart
service podkop restart
#
# 
Потом минут 10 потерпеть.
Телега, скорее всего, на опере работать не будет, но остальное бегает как-то.

---

**2026-04-12T14:34:13 | Роман**
Вам дополнительно нужно будет либо купить, либо поднять свой прокси/впн, беспланые решения увы, всё.
С играми на виндовс идут тесты в обновлённом zeroblock, возможно найдётся для них решение. 
Так же для игрушек есть запрет 1, возможно он поможет. 
И да, на другом роутере с openwrt вы будуте всё настраивать сами.

---

**2026-04-12T14:35:17 | ᚢᚹᛟᛈᛠᛋᛠᛊ ᛖᛊᚺᚱ**
Да че, я щас гулять,потом zeroblock верну,хз
Подожду когда к телеге выкатят ченить

---

**2026-04-12T14:41:31 | Mikhail**
Не могу понять как выбрать расширенные списки с API v2. Zeroblock обновил, но их просто нет в выпадающем списке "Списки сообщества"

---

**2026-04-12T14:45:18 | Роман**
Без понятия, подписками не пользуюсь. Но такая возможность есть в zeroblock. Возможно ваша подписка и вовсе зашифрована.

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

**2026-04-12T15:24:36 | Anna Bagler**
В zeroblock. Вы хоть знакомьтесь с интерфейсом того, что ставите.

---

**2026-04-12T15:32:05 | Routerich**
Если кому-то интересно, как разрабатывается Zeroblock

---

**2026-04-12T15:47:51 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-12T15:56:40 | Роман**
Удалять старые, что бы не мешали. Там нельзя секции отключать (а в zeroblock можно).

---

**2026-04-12T16:09:43 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-12T16:09:51 | Артем⸙ꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋ 𓆏ࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩࣩ**
Так всё таки zeroblock лучше , чем подкоп получается 🤔, значит поставлю zeroblock

---

**2026-04-12T16:19:58 | Виталя**
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

**2026-04-12T16:49:47 | M L**
Имеется ключ vless, установлен ZeroBlock. Подскажите, куда вставить ключ?

---

**2026-04-12T16:52:10 | Anna Bagler**
Тогда вам только сброс поможет. Первичная настройка. Потом zeroblock по инструкции и свой vless потом.

---

**2026-04-12T17:23:25 | Роман**
В zeroblock?

---

**2026-04-12T17:24:25 | Виктор**
Приветствую всех! Полгода назад установил скрипт №5. Насколько я понимаю - это установка и настройка podkop. Но последнюю неделю много сайтов перестала работать, в т.ч. и youtube. Есть такое же простое решение для нашего роутера? Почитал, zeroblock советуют. Надо его устанавливать? Podkop отключать?

---

**2026-04-12T17:32:58 | Роман**
В zeroblock.

---

**2026-04-12T18:04:02 | Vasya Mafia**
Всем привет! Осмотрел wiki, не нашел базовой для меня инфы. Отдельно вроде про всё есть: zapret, podkop, zeroblock и тп. Есть ли какая-то между ними взаимозависимости? Я так понимаю что это разные средства для обхода блокировок. У кого-то стоит podkop, а у кого-то zeroblock вместе zapret, они должны быть вместе или одного достаточно? Я только купил роутер, у меня есть vps с поднятым vless, может подскажите что-то простое чтобы использовать его?

---

**2026-04-12T18:06:07 | Anna Bagler**
Zeroblock.

---

**2026-04-12T18:08:58 | Aidar Safiullin**
Друзья, подскажите, пожалуйста, есть платный квн дядя Ваня. 
Его ключ для прокси начинается с “ssconf://“. 
Но он не поддерживается ZeroBlock 🥲

Получается его не завести в зб?

---

**2026-04-12T18:43:16 | Maxim =)))**
Подскажите, а vless ключ можно как-то преобразовать,чтобы добавить в ZeroBlock?

---

**2026-04-12T19:33:35 | Андрей**
Парни, а кто то может рассказать, в чем принципиальное отличие zeroblock от подкопа? Что побудило написать его? Я посмотрел, вроде принцип то основной тот же?

---

**2026-04-12T19:37:56 | Андрей**
Всем привет. Вчера успешно перешел с подкопа на ZeroBlock. Но вот мучает меня один вопрос. После установки я не стал включать секции opera и awg т.к. они мне не нужны. Создал свою секцию, добавил ключи из своей подписки, включил нужные мне списки. В итоге всё нормально работает, но вот терзают меня сомнения, не нарушил ли я логику работы ZeroBlock не включив эти предустановленные секции?

---

**2026-04-12T19:51:24 | Андрей**
Только что на свежей прошивке (на сегодняшний день) и на новом zeroblock проверил - воспроизводится) А это не баг?
(не появляется в списке интерфейсов интерфейс openconnect)

---

**2026-04-12T19:58:34 | Андрей**
Оу. команда routerich,  подскажите, пожалуйста) А можно ли получить на платной основе консультацию по настройке zeroblock) ? В частности - есть непонятный эффект - на андроид приставке работает дефолтный youtube но не работает smartyoutube (форк) при этом приставка и форк точно рабочие, буквально 2дня назад за границей все работало)

---

**2026-04-12T20:43:05 | Kiss_My_Axe**
Она оживает минуток так за 10.
Пока не знаю, как её тестировать, потому что остановка ZeroBlock, чтобы он юзерправилами не мешал тесту рушит и оперу.
Вот.

---

**2026-04-12T20:49:06 | Артём Фомин**
Полагаю что список AI в ZeroBlock в секции VLESS-tcp. Но полагаю, будет работать и в секции awg10, что добавляется при автоматической установке. Перенёс во VLESS-tcp, когда перестала opera работать.

---

**2026-04-12T20:51:11 | Arsen Kornienko**
О-о, спасибо. Это не podkop, получается, а вместо него ZeroBlock поставить? Или можно через podkop?

---

**2026-04-12T20:54:37 | Артём Фомин**
Думаю можно и через podkop. ZeroBlock просто более продвинутый пакет. Там больше гибкости с настройками и можно добавлять не только vless tcp Reality

---

**2026-04-12T21:05:13 | Артём Фомин**
У меня телега прекрасно работает через ZeroBlock - awg10.

---

**2026-04-12T21:06:29 | Timur**
можно попросить прислать фото zeroblock -awg10 настройки. удалил профиль.

---

**2026-04-12T21:12:13 | Артём**
Вроде всё настроил, конфигурацию импортировал, сам ВПН через приложение работает, но в роутере не пингует (N/A) в zeroblock(

---

**2026-04-12T21:15:32 | Anna Bagler**
Zeroblock и свой vpn в него.

---

**2026-04-12T22:10:40 | Роман**
Ну устанавливайте bye dpi в роутер. В чём проблема?
Я ссылку vless в zeroblock закинул и всё работает.

---

**2026-04-12T22:23:44 | Санчо Панчо**
Настройки тут 👉 Службы-Zeroblock-Настройки-Обновление списков

---

**2026-04-12T23:01:11 | Anna Bagler**
Либо подкоп не удалять, либо сброс и Zeroblock. Cоздать свой интерфейс по аналогии с awg10, импортировать туда свою конфигурацию, привязать свой интерфейс к секции в podkop/zero. Выбрать нужные списки. Zeroblock гибче.

---

**2026-04-13T00:55:14 | Фил**
скажите пожалуйста, как вы настраивали амнезию? просто в книжке пишет про автонастройку, а как добавить свой сервер я вообще не понял.
На устройствах RouteRich WARP настраивается автоматически:
1. Включите AmneziaWG WARP в автонастройке
2. ZeroBlock запросит конфигурацию WARP с сервера RouteRich

---

**2026-04-13T01:20:54 | Артём Фомин**
В настройках ZeroBlock ещё можно попробовать включить "CIDR списки сообществ". Как я понимаю, вместе с доменами также будет загружать и IP адреса. Не уверен, но вроде как помогло с телеграмом.

---

**2026-04-13T03:37:05 | Andrew Arzaev**
Всем привет!
С Tailscale как-то беда
Прошил роутер (u-boot)
Поставил zeroblock
Потом подключил tailscale
Все как в инструкции (документация роутерич) строго по шагам, включая пункт - дополнительные возможности 
Подключился 1 раз, смог проверить по 2ip адрес, спустя небольшое время перестал вообще перестал грузить какие дибо сайты через тэил, но при этом подключается в программе и отображается устройства онлай
Подскажите пожалуйста в чем может быть беда?

---

**2026-04-13T06:49:51 | Anna Bagler**
Zeroblock лучше ставить на чистый роутер, но если без этого никак, то удалять подкоп и файлы конфигураций от него. Руками. Пока zeroblock не чистит от других служб.

---

**2026-04-13T09:00:26 | Routerich**
а если остановить zeroblock,zapret2 начинают сайты открываться?

---

**2026-04-13T09:47:44 | Роман**
Для обновления того, что нужно. Zapret2, zeroblock, фиксы WiFi, оперу фиксили недавно.

---

**2026-04-13T09:51:55 | Роман**
Zeroblock, свои прокси - всё отлично работает.

---

**2026-04-13T10:05:22 | Ваня Лалетин**
т.е лучше будет сбросить до заводских перед установкой zeroblock?

---

**2026-04-13T11:00:09 | Mikhail Velichko**
Хорошо, а варианты подружитьMultiWan с  Zeroblock существуют?

---

**2026-04-13T11:10:16 | Vladislav**
Zeroblock не устанавливается что делать?

---

**2026-04-13T12:16:23 | Rockey**
В Zeroblock с awg в списках добавляю пользовательские домены через динамичский список, сохраняю применяю перезагружаю
но все равно не идёт через впн
в чем причина?

---

**2026-04-13T12:42:39 | Владимир Волков**
Поставьте Zeroblock (соседняя тема), настройте его (в Wiki есть полный мануал), туда добавьте секцию и ссылку под тип прокси (скорее всего)

---

**2026-04-13T14:03:52 | Anna Bagler**
Свой vless или ещё что, что поддерживается zeroblock, и пустить ПС по IP в полную маршрутизацию.

---

**2026-04-13T14:30:23 | Kiss_My_Axe**
Для авг10 сгенерировать новый конфиг, генератор llimonix warp в google.
А лучше переходите на ZeroBlock, там две галки поставить и половина нужного настроится сама.

Решите перейти на зероблок, удалите подкоп через Система - Пакеты, вкладка Установленные. Фильтр podkop.

---

**2026-04-13T14:30:36 | Anna Bagler**
Настраивайте базовый функционал роутера. Потом zeroblock.

---

**2026-04-13T14:39:34 | Anna Bagler**
Чтобы нормально работать с zeroblock, нужно сбросить настройки роутера. Не ставить подкоп, а ставить zeroblock.

---

**2026-04-13T14:59:18 | Anna Bagler**
Если там не только сервера для БС, то попробуйте засунуть подпиской в zeroblock. Или запросить у поддержки прямые ссылки.

---

**2026-04-13T15:03:21 | Anna Bagler**
Да, zeroblock поддерживает подписки, если сможет воспринять.

---

**2026-04-13T15:52:33 | Routerich**
и оно в подкопе работает при переключении gateway? запустите mwan и zeroblock потрогайте сайты из списков и пришлите файл
nft list table inet zeroblock > /root/zerorule.txt

---

**2026-04-13T16:01:00 | Anna Bagler**
В тему Zeroblock, там в закрепах есть пошаговая инструкция. Но нужен свой vless, awg или ещё что.

---

**2026-04-13T16:11:13 | Vlad**
а в zeroblock подобные настройки есть?

---

**2026-04-13T16:11:55 | Anna Bagler**
Нужны свои платные конфиги, vless, awg и прочее, что можно скормить zeroblock.

---

**2026-04-13T16:14:54 | Anna Bagler**
Все должно быть аналогично и у zeroblock.

---

**2026-04-13T16:17:30 | Vlad**
awg, настроено через zeroblock через списки сообщества

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

**2026-04-13T17:12:27 | Anna Bagler**
Vless. Удалить секции в zeroblock. Cоздать свою, тип proxy, конфигурация URL, cвою ссылку vless вставить, выбрать списки. Проверить.

---

**2026-04-13T17:17:43 | frnchesko178 (Влад)**
Нет пакетов соответствующих запросу Zeroblock

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

**2026-04-13T17:24:17 | Anna Bagler**
В zeroblock cекции маршрутизации.

---

**2026-04-13T17:45:55 | Джалиль**
Здравствуйте! А xray-core устанавливается/обновляется Zeroblock-ом из openwrt репы? Есть ли ipk xray-core по-свежее 25.1.30? 
А то ZB 0.7.2-r55 устанавливает xray-core 25.1.30 для openwrt 24.10.4 (автонастройкой "Установить Xray"), но в этой версии xray-core отсутствует PQ Encryption, добавленную в ZB релизом 0.7.1-r33, отчего фактически не получается использовать ключи vless с PQ шифрованием (mlkem768x25519) из-за старого xray-core.

---

**2026-04-13T18:18:16 | frnchesko178 (Влад)**
У меня тут сбой на пункте 7.
Эти пункты уже установлены в zeroblock, но Zapret2 не появился в службах

---

**2026-04-13T18:20:40 | Routerich**
Здравствуйте.
Подбирать стратегию или ставить Zeroblock по инструкции

---

**2026-04-13T18:23:44 | Routerich**
Здравствуйте.
Используйте Zeroblock.
А в целом сейчас с бесплатными вариантами много проблем, так что лучше свое, конечно

---

**2026-04-13T18:24:02 | Роман**
zeroblock как средство точечной маршрутизации, в него найти халявные подписки.

---

**2026-04-13T18:25:44 | Routerich**
Это прям тяжёлая артиллерия, он, слишком большой и жрёт много памяти, лучше Zeroblock

---

**2026-04-13T18:36:27 | Алексей**
Как я понял там только с разделением трафика на рус-зарубеж трудности, сам-то v2raya по минималке ставится и настраивается довольно легко. По крайней мере после установки v2raya на SteamOS меня мало что пугает. Просто подумал может сейчас не придется запариваться, чтобы сразу на телике смотреть видосы в 4K. Но гляну что за зверь такой Zeroblock

---

**2026-04-13T18:44:00 | Anna Bagler**
Для начала обзаведетесь, а потом изучайте полный мануал по zeroblock.

---

**2026-04-13T18:50:30 | Routerich**
Если zeroblock https://iplist.my-handbook.ru/ru

---

**2026-04-13T18:52:03 | Timur**
и может лучше zapret 2 не ставить если есть zeroblock?

---

**2026-04-13T19:09:37 | Алексей**
Такс, прошу прощения, если вопрос глупый, но в мануале по ZeroBlock в разделе первоначальной настройки есть пункт "Перейдите в Службы -> ZeroBlock -> Автонастройка". У меня в службах ZeroBlock отсутствует. Получается, его надо установить? Но я не пойму как

---

**2026-04-13T19:10:12 | Алексей**
В разделе "Система - Пакеты" не могу найти пакет ZeroBlock для установки

---

**2026-04-13T19:15:57 | Pavel**
Добрый день. Обновил прошивку, в интерфейсах добавил свой впн сервер amniziawg, установил zeroblock и дальше чет туплю. Zeroblock не видит мой сервер amneziawg. что еще надо сделать? Справа статус Sing-box остановлена. Мне необходимо настроить что бы не весь трафик через впн летел

---

**2026-04-13T19:17:28 | Timur**
а wireguard как установить на zeroblock?

---

**2026-04-13T19:18:04 | Routerich**
Через интерфейсы создать и потом в Zeroblock выбрать этот интерфейс

---

**2026-04-13T19:41:49 | Василий**
Собрал инструкцию как поставить на роутерич awg 2.0 + маршрутизация

Сперва узнайте что такое «self-hosted amnezia», затем переходите к инструкции.

1. Сброс настроек роутера зажатием мелкой кнопкой. Держим 7-10 сек. Ждем минуту-две.
2. Подключаемся к вайфай сети Routerich 2 или Routerich 5
3. Заходим в админку на routerich.lan. При первом входе логин root без пароля
Если не открывается. То подключаемся к роутеру по интернет кабелю.
4. Жмем Перейти к настройке пароля. Придумываем пароль, сохраняем
5. Обновляем прошивку роутера. У меня стояло 23.05.5
Заходим на сайт https://routerich.ru/firmware
Смотрим на заднюю панель роутера. Там выход usb 2 (белый) или usb 3 (синий). Согласно тому, какой usb, то и прошивку скачиваем соответствующую
В меню админки роутера идем в: Система/Восстановление обновление
Нажимаем установить новый образ прошивки, выбираем скаченный файл с сайта. Нажимаем загрузить
Не пугаемся красных сообщений. Находим галочку Принудительная прошивка и включаем ее. Нажимаем продолжить и ждем, пока не перезагрузится роутер (3-5мин). После перезагрузки заново входим в админку через routerich.lan или 192.168.2.1 или 192.168.1.1
6. Мастер первоначальной настройки. Ставим внизу галочку Выключить IPV6
Жмем Далее, Далее. На экране 3 можно сразу настроить домашнюю сеть вайфай. На экране 4 - Далее и Завершить . Страница перезагрузится. Проверяем версию встроенного ПО. Должна быть актуальная версия, которую скачали
7. Открываем раздел Система , потом пакеты .
Жмем зеленую кнопку "Обновить списки" и ждем. Закрываем появившуюся табличку нажав на кнопку "Закрыть".
Вводим в окне "Фильтр" (слева вверху) Zeroblock . Внизу должны появиться два пакета: Zeroblock и luci-app-zeroblock. Нажимаем кнопку "Установить" напротив каждого пакета. (Первым идет Zeroblock, а затем luci-app). В появившемcя окне жмем еще раз установить . После завершения закрываем окно. Вводим в окне "Фильтр" (слева вверху) «amnezia». Внизу появятся пакеты. Нужно обновить те, где будет кнопка «обновить». Скорее всего 2 пакета. 
8. Далее выходим и обратно входим в интерфейс роутера. Внизу слева нажать кнопку Выйти и заново входим. После этого должен появится ZeroBlock в службах. Слева вкладка Службы, сразу ниже под кнопкой будет ZeroBlock. Если не появился, то сбрасываем кэш браузера.
9. В браузере Хром нужно сбросить весь кеш. Жмем Ctrl+Shift+Delete (Windows) или Cmd+Shift+Delete (macOS). И обязательно проставляем все галочки и нажимаем Удалить с устройства
10. Заходим снова в админку роутера. Идем в Сеть - Интерфейсы . Жмем Добавить новый интерфейс . Имя AWG20 и протокол AmneziaWG VPN. Жмем Создать интерфейс . В списке находим и ставим галочку не создавать маршруты . Дажее жмем загрузка конфигурации. Туда перетаскиваем конфиг AWG 2.0 (в виде файла amnezia_for_awg.conf) (Нужно арендовать свой сервер, это обычно 200-500р в месяц и ставить туда амнезию. Как ставить и создавать конфиг - в чате не спрашивайте, есть на это гугл и ютуб, где все наглядно рассказывают и показывают). Жмем Импорт настроек .
Сохранить . Переходим во вкладку настройки межсетевого экрана Жмем на
выпадающий список и в cамом низу в поле «пользовательский» пишем AWG и жмем ENTER. Появится вот так (AWG; (создать)) далее сохранить, сохранить, применить.

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

**2026-04-13T19:44:11 | Anna Bagler**
Zeroblock работает с подписками. Воспримет ли вашу, будет видно.

---

**2026-04-13T20:12:11 | Роман**
https://github.com/StressOzz/Zapret-Manager
Этим попробуйте обойти блок, там игровые стратегии есть. 
Если не поможет - искать домены игры и добавлять их в подкоп. 
Либо ждать когда выйдет улучшенный zeroblock, там есть фича запуска приложений и игр в обход через политики windows. 
Скрипт может вам что-то сломать, раз вы сами не знаете как оно работает.

---

**2026-04-13T20:19:28 | Anna Bagler**
На чистый роутер лучше ставить zeroblock.

---

**2026-04-13T20:28:23 | Anna Bagler**
Ccылку на вашу подписку zeroblock воспринял?

---

**2026-04-13T20:29:45 | Gomer Simpson**
ZeroBlock. Из ZeroBlock установить Zapret2.

---

**2026-04-13T20:34:12 | Anna Bagler**
Ставьте Zeroblock. https://t.me/routerich/394153/405571

---

**2026-04-13T20:44:12 | Anna Bagler**
Удалять youtubeUnblock. Ставить zeroblock и скармливать ему свой vpn.

---

**2026-04-13T20:48:58 | Anna Bagler**
Если только YouTube нужен, то читаем выше. Если и другая запрещенка, то zeroblock, но бесплатные варианты сейчас работают с ограничениями.

---

**2026-04-13T20:52:04 | Anna Bagler**
Сможет zeroblock вытащить то, что внутри.

---

**2026-04-13T21:22:30 | Anna Bagler**
Нужно обзавестись ссылками vless и ещё чем, что поддерживается подкопом. Если у вас подписка, то сбросить, поставить zeroblock и попробовать скормить ему вашу подписку.

---

**2026-04-13T21:29:22 | Anna Bagler**
Cбрасывайте роутер. Ставьте zeroblock на чистый https://t.me/routerich/394153/405571
Потом можно посмотреть вашу подписку.

---

**2026-04-13T21:33:56 | Sergey G**
Подскажите - у функции мониторинга есть функционал поднятия сервиса или нет?

Я вручную выполнил запрос из планировщика (/usr/bin/zeroblock system_monitor) при отключенной вручную службе, он выдал те же результаты что при включенной.

Я надеялся что мониторинг каждый час мне поможет победить проблему остановки службы - но оказалось что не помог

---

**2026-04-13T21:50:54 | Pavel**
Такс, вроде завелось, но не могу до конйа понять как списки работают в zeroblock. 2ip.io у меня кажет страну моего впн. 2ip.ru я вбил в "список пользовательских доменов" все верно ведь?

---

**2026-04-13T21:53:59 | Anna Bagler**
В zeroblock.

---

**2026-04-13T21:56:44 | Anna Bagler**
Zeroblock поддерживает подписки. Воспримет ли вашу, будет видно. Смотрите, какие прямые ссылки на платное вам доступны и поддерживаются ли они средством обхода на роутере.

---

**2026-04-13T21:58:18 | Anna Bagler**
Когда поставите zeroblock. Можно будет пробовать создать свою секцию и туда добавить вашу ссылку.

---

**2026-04-13T21:59:55 | ARTYOM RISEMAN**
О как, спасибо. Будем пробовать. 
А zeroblock это вообще что такое?

---

**2026-04-13T22:05:56 | ~**
Всем доброго времени суток!
A zeroblock откуда лучше брать?

---

**2026-04-13T22:19:13 | Pavel**
Я искренне не пон почему нельзя сделать так, что бы просто добавить свой впн, в zeroblock настроить списки и все)

---

**2026-04-13T22:21:59 | Kiss_My_Axe**
Переходите на ZeroBlock.
PBR туннельного уровня прилада. Хорошая, но ужа на ежа не натянешь.

---

**2026-04-13T22:32:37 | iProxx**
Кстати, по поводу FakeIP. Ее нужно отключать в своей секции независимо от типа подключения (Proxy или VPN) ?
Просто в Zeroblock в секциях awg10 и opera proxy по умолчанию галочка снята.

---

**2026-04-13T22:42:18 | Alexey Kobzev**
ребят как zeroblock полностью снести и переустановить? через службы сношу и ставлю он снова устанавливает мои настройки

---

**2026-04-14T00:18:16 | Геннадий**
А в ZeroBlock как то можно настроить интервал обновления подписок , ну скажем раз в 3 часа например ?

---

**2026-04-14T00:29:59 | Роман**
Zeroblock НЕ с халявой, списки стандартные.

---

**2026-04-14T00:31:18 | Роман**
Предатель zeroblocka! Скоро демон выйдет, имба будет.

---

**2026-04-14T00:58:41 | Роман**
Все в zeroblocke будем! ASU и Zapret братья навек! 😁

---

**2026-04-14T01:29:48 | .**
Отменил я установку awg2... (Пропал Ютуб) Поудалял лишнего. Накатил бекап когда всё работало... Теперь так. Ютуб работает на компе и на телефоне (на ТВ не проверял, поздно)... Вопрос... А куда делась opera proxy из панели управления zeroblock...? Если в авто настройках указано что она установлена, ну и пакет её в пакетах есть и установлен.

---

**2026-04-14T01:43:27 | .**
Отменил я установку awg2... (Пропал Ютуб) Поудалял лишнего. Накатил бекап когда всё работало... Теперь так, как на фото и Ютуб работает на компе и на телефоне (на ТВ не проверял, поздно).

Вопрос... А куда делась opera proxy из панели управления zeroblock...? Если в автонастройках указано, что она установлена, ну и пакет её в пакетах есть и установлен.

Раньше в панели управления была и opera proxy и awg10... Теперь только awg

---

**2026-04-14T02:02:20 | .**
Очень хотелось бы вернуться opera proxy в панель управления zeroblock... Как это сделать?

---

**2026-04-14T02:18:43 | Kallenn**
Закинул в ZeroBlock. Пока тестирую, полет нормальный. После vless как глоток свежего воздуха. Единственное, затупил с созданием интерфейса wg. Там ребут роутера надо сделать, что бы интерфейс поднялся. А то я все понять не мог, пакет стоит, а создать/поднять коннект wg не могу 😭
Крч, спасибо. Посмотрим сколько протянет.

---

**2026-04-14T06:42:37 | Андрей**
При загрузке роутера возникает гонка между зероблоком и openconnect

Tue Apr 14 09:20:48 2026 user.notice zeroblock: Starting ZeroBlock... [zeroblock] Starting ZeroBlock(0.7.2-r55)... [singbox_gen] Section op: interface 'vpn-ps' does not exist, skipping

Zeroblock загружается быстрее, чем успевает подняться интерфейс ( 
Есть ли у openwrt механизм запуска чтоб zeroblock стартовал после сети?

---

**2026-04-14T06:55:41 | Routerich**
как вариант, в автозагрузку перед exit 0 добавить
sleep 60
service zeroblock restart
exit 0

---

**2026-04-14T09:50:26 | Vladimir**
Подскажите, почему не запускается трафик через zeroblock... когда подкопом пользовался, всё было - ок...

---

**2026-04-14T10:14:41 | Sharky**
Ок. Но это же получается на конкретный хост - как например ютуб сделан.
А чтобы применялось для всего заблокированного? Zeroblock + zapret2 стоит и то есть ютуб но нет ничего другого, то наоборот. Уже задолбался искать описание и понять что за чем и почему не работает

---

**2026-04-14T10:30:19 | Gomer Simpson**
Давайте не усложнять. Ютуб через Z2, остальное через ZeroBlock. Для Ю стратегии ищутся легко. В инструкции есть описание процесса и правила оформления стратегий перед применением.

---

**2026-04-14T10:33:05 | karat**
Подскажите пожалуйста в связи с поправками в настройках ДНС,- серверы менять менять на обоих вкладках в настройка Zeroblock и в секции, или достаточно только в секции?

---

**2026-04-14T10:54:40 | Егор**
Ребят в целом для работы телеги в т.ч. на Андройде лучше серчить стратегии для Запрета или zeroblock/podkop мучать? Сейчас на Zeroblock, десктоп работает норм а вот на телефоне борода

---

**2026-04-14T11:49:37 | Алексей**
Товарищи, подскажите, пожалуйста. Вчера настроил ZeroBlock по минималкам, подключил свой предоплаченный VPN через подписку (удаленный список прокси, использующий подключения VLESS): список доступных стран подключения отображается, VPN работает, ютюб на телике завелся. Теперь хочу немного адаптировать все это дело, чтобы можно было вырубить VPN на каждом отдельном устройстве в доме, используя его только на роутере. В какой раздел мануала по ZeroBlock смотреть, чтобы грамотно настроить разделение трафика на зарубеж и сайты РФ (чтобы всякие госуслуги, яндексы и озоны проходили вне VPN, а зарубежные сайты – через VPN)? А также, чтобы отфильтровать рекламу и больше не видеть ее нигде? Инфы в мануале много, но я чувствую себя нубом, читая это все. Буду благодарен за наводку, в какой раздел нужно вгрызться.

---

**2026-04-14T12:01:20 | Routerich**
zeroblock

---

**2026-04-14T12:04:13 | Роман**
Выбрать список социальный в zeroblock.

---

**2026-04-14T12:21:52 | Gomer Simpson**
Я бы рекомендовал начать изучение ZeroBlock в соответствующей теме. Это продукт от RR. Оно гораздо более лояльно к пользователю и имеет более широкие возможности.

---

**2026-04-14T12:28:56 | Михаил Краев**
Подскажите, пожалуйста. 
Вчера ночью настроил zeroblock:
awg10 и proxy со своим vless. Zapret2 выключен. После проверки все ок работало - списки отрабатывали корректно. Сегодня (часов через 10-12) начал отваливаться/пытаться пере подключиться WiFi от разных устройств. Грешу на какие то настройки, возможно в списках CDN cloudflare/google в awg10

---

**2026-04-14T12:35:19 | Routerich**
wiki - zeroblock_manual, zeroblock закреплённые сообщения пощелкать до мануала

---

**2026-04-14T13:04:56 | Kiss_My_Axe**
root@roskomnadzor:~# uci show zeroblock | grep tail
zeroblock.settings.source_network_interfaces='br-lan' 'tailscale0'

---

**2026-04-14T13:12:27 | Routerich**
вам интерфейс надо сделать и импортировать конфиг туда, а потом уже в zeroblock секцию создать и там выбрать новый интерфейс

---

**2026-04-14T13:12:59 | Docvspb 🇷🇺**
а по этому поводу тоже есть где-то описание (как для zeroblock)?

---

**2026-04-14T13:25:04 | Вадим Гумурзаков**
Поключил zeroblock с zapret2, внес ссылку на свои ключи через "Подписка (удаленный список прокси)". Ключи добавились, пинг отображется. Но кроме YouTube ничего не работает, ни телеграм, ни инстаграм и т.п.

---

**2026-04-14T13:35:27 | Yiliam**
Насчёт тг на андроиде, еле как работает на Zeroblock в секции awg. В  zaprete2 со стратегией ютуба не пошёл, страты не ищет часами ни в блокчеке ни в поиске, крутит крутит без результата, даже те которые раньше находило, по торент доменам например. Оператор мтс. Поитогу работает только ютуб через запрет и немного тг через зероблок, торенты не работают через зероблок.

---

**2026-04-14T14:49:18 | Роман**
Не зашифрованные подписки поддерживает zeroblock. Если просто ссылка vless - будет работать.

---

**2026-04-14T14:59:26 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock
Устанавливайте пропустив атонастройку, затем
https://t.me/routerich/394153/583283
https://t.me/routerich/4/573119

---

**2026-04-14T15:22:13 | Anna Bagler**
Ставьте zeroblock. Cоздавайте в нем свою секцию вместо дефолтных. Привязывайте к ней свои интерес и списки.

---

**2026-04-14T16:02:08 | Сергей**
Zeroblock умеет маршрутизовать по базам geoip, как завернуть весь ru трафик напрямую?

---

**2026-04-14T16:12:39 | Anna Bagler**
https://t.me/routerich/394153/405571
Но нужен свой vless, awg или ещё что, что поддерживается zeroblock.

---

**2026-04-14T16:33:11 | Vadim Morozov**
Подскажите, пожалуйста, будет ли работать в zeroblock конфиг awg, сгенерированный в warp-generator?

---

**2026-04-14T16:47:23 | Sergio Yakovlev**
В YouTube не все грузиться поскажите где чё подправить ZeroBlock или в  zapret

---

**2026-04-14T16:49:44 | Sergio Yakovlev**
Установлен ZeroBlock и zapret

---

**2026-04-14T17:24:36 | Anna Bagler**
Панель управления zeroblock покажите.

---

**2026-04-14T17:30:49 | .**
добавил zeroblock и zapret2 по инструкции, работает только ютуб и инста по сути. могу ли я как-то добавлять сервисы и сайты куда-то, чтобы оно работало? есть впн wireguard, но я для того, чтобы избавиться от него дома и купил данный роутер. может кто помочь с настройкой? или хотябы объяснить что к чему тут вообще. информации море, я ничерта не понимаю. был бы очень благодарен.

---

**2026-04-14T17:37:26 | Anna Bagler**
Подкоп xray не поддерживает. Вам тогда в zeroblock. Другая секция не нужна.

---

**2026-04-14T17:37:32 | Роман**
Установите zeroblock, создать секцию, вставить ссылку, выбрать списки. Всё.

---

**2026-04-14T17:44:26 | .**
приветствую
добавил zeroblock и zapret2 по инструкции, работает только ютуб и инста по сути. могу ли я как-то добавлять сервисы и сайты куда-то, чтобы оно работало? есть впн wireguard, но я для того, чтобы избавиться от него дома и купил данный роутер. может кто помочь с настройкой? или хотябы объяснить что к чему тут вообще. информации море, я ничерта не понимаю. был бы очень благодарен.

---

**2026-04-14T18:01:42 | Сергей**
Куда вбивать домены маской. Не могу найти этого поля в Zeroblock

---

**2026-04-14T18:02:46 | Volshur**
Всем привет. Подскажите, на новом роутере,чтобы поставить весь нужный софт. (Zeroblock итд) Нужно "собрать" прошивку ASU? На данный момент я так понял не работает.

---

**2026-04-14T18:05:46 | Oleg Shmyrin**
Так, чет не охота пока в zeroblock погружаться, я правильно понимаю что если я поставлю на VPSку AWG, и подниму подключение с роутера (клиент же амнезии уже есть) подключение awg123 — то могу выбрать в секции YOUTUBE_DISCORD этот интерфейс и все списки перекинуть на него, а секцию main вообще удалить, ну или оставить без списков?

---

**2026-04-14T18:07:35 | Anna Bagler**
Не вижу ничего по подписке. Попросите Fresa в теме Zeroblock посмотреть на вашу подписку. Если захочет, напишет свои контакты, куда отправить ссылку.
В happ можете на отдельных локациях взять прямую ссылку?

---

**2026-04-14T18:29:01 | Volshur**
Подскажите скрипт 5 ставит подкоп? Или даёт выбрать между подкоп и zeroblock?

---

**2026-04-14T18:38:24 | Anna Bagler**
Zeroblock и в него попробовать засунуть подписку. Посмотреть, будет ли блокировка со стороны поставщика.

---

**2026-04-14T18:40:50 | Volshur**
Спасибо за ответ . Буду пробовать ставить zeroblock+zapret 2. Приобрел сегодня Ваш роутер. На старом стоит подкоп+zapret.  Если не  трудно подскажите, можно ли собрать прошивку сразу с нужными пакетами например с zeroblock+zapret2? Если да то это делать через тестовый сервер ASU?

---

**2026-04-14T18:45:57 | .**
Настроил zeroblock и zapret2
Вроде работает. Есть впн от wireguard, но как его накатывать на роутер вообще не понимаю. Все еще и терминами с абривиатурами сыпят, так что ничего не понятно. На ютубе аналогично. Понял, что нужно впн на влесс ставить, а как - гадай. 
У меня претензий нет, оборудование отличное, веб интерфейс удобный и приятный, но вот с технической точки зрения я совсем не подкован. Думал будет все проще.

---

**2026-04-14T18:48:15 | Anna Bagler**
С 10 пункта пробуйте cоздать свой интерфейс https://t.me/routerich/394153/625333
И привязать к секции в zeroblock.

---

**2026-04-14T19:09:18 | Routerich**
Платные/собственные решения добавлять в zeroblock, с бесплатными сейчас все плохо

---

**2026-04-14T19:09:41 | Anna Bagler**
В zeroblock.

---

**2026-04-14T19:20:35 | Anna Bagler**
У zeroblock сейчас или что?

---

**2026-04-14T19:29:41 | Anna Bagler**
Если вам нужен zeroblock, то его ставить на чистый роутер. Если не знаете, что такое подкоп, то скрипт №5 не использовали ранее?

---

**2026-04-14T19:38:26 | Kiss_My_Axe**
БАГРЕПОРТ (или я чо не понил)

Новая вайфай-сеть с привязкой к NEWLAN интерфейсу.
Настройка, туда-сюда, клиент подключается, адрес назначается.
Иду в ZeroBlock - Настройки и в "Сеть - Входящие интерфейсы" не наблюдаю NEWLAN-интерфейса в выпадающем списке.
Сильно опечален.

---

**2026-04-14T19:50:57 | Eduard Ivanov**
Все установил, но я не понимаю мануал. Где кнопка авто настройки. Служба-zeroblock-автонастройка требует мануал. Но нету

---

**2026-04-14T19:53:05 | Anna Bagler**
Zeroblock есть в Службах?

---

**2026-04-14T19:57:00 | Eduard Ivanov**
Luciapp zeroblock пакет нужно ставить?

---

**2026-04-14T20:02:58 | Anna Bagler**
Не слушайте бота. Убирайте подкоп. Zeroblock вместо подкопа.

---

**2026-04-14T20:06:16 | Anna Bagler**
Познакомьтесь с интерфейсом Zeroblock.

---

**2026-04-14T20:06:53 | Routerich**
Сброс потом установка Zeroblock

---

**2026-04-14T20:14:23 | Routerich**
Сбросить роутер и установить Zeroblock

---

**2026-04-14T20:17:08 | Eduard Ivanov**
Zeroblock manual  сделал авто настройку. Дальше идут пояснения что чем является а не что нужно делать. И в конце диагностика и устранение неполадок. А что делать дальше? Ютуб к примеру не работает

---

**2026-04-14T20:26:14 | Евгений Вихарев**
Всем добрый вечер!
Такой вопрос, пробую ставить zeroblock, но при установке пишет, что не может найти пакет kmod-inet-diag. 
Бегло погуглил, не нашел ссылку на него. Может кто-нибудь поделится ?

---

**2026-04-14T20:32:40 | B R**
А куда подписку вставлять? В zeroblock?

---

**2026-04-14T20:42:40 | Marik Kiram**
Здравствуйте, поставил в zeroblock свой конфиг амнезии, всё делал по инструкции. Делал не в первый раз и до этого всё работало, а сейчас почему-то не хочет через этот впн пускать на сайты, хотя телеграм почему-то работает великолепно. Подскажите, пожалуйста, в чём может быть проблема?

---

**2026-04-14T20:52:24 | Роман**
В zeroblock. Вкладка секции маршрутизации. Там опера и авг. Нажимаете редактировать, идёте во вкладку списки и там будут списки.

---

**2026-04-14T20:52:56 | Anna Bagler**
Читайте полный мануал по zeroblock или в целом по средствам точечной маршрутизации.

---

**2026-04-14T21:00:17 | Виктор**
Добрый вечер! Обновил прошивку, поставил ZeroBlock. Диагностику проходит, ошибок нет. Смущает, что секцию наобум создал и FakeIP не используется. В мануале только  пункты настроек, никаких рекомендаций. Может где подробнее почитать можно?

---

**2026-04-14T21:08:43 | Роман**
Не вижу телеги.
По zeroblock вопросы в соответствующей теме.

---

**2026-04-14T21:10:07 | Vladimir**
zeroblock не ставится.... завершается с ошибкой с кодом 255. кто знает почему?

---

**2026-04-14T21:38:06 | Anna Bagler**
В теме Beta. Но лучше ставить zeroblock.

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

**2026-04-14T21:47:54 | Eired**
Товарищи кому не сложно подскажите zeroblock умеет в ipv6 или нужно отключить, пока что не увидел инфу. Заранее спасибо

---

**2026-04-14T22:18:30 | Garsia**
Не подтверждаю ни по одному пункту. ZeroBlock - это лучше, что случалось с моим роутером за всё время его работы! :)

---

**2026-04-14T22:28:58 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-14T23:17:33 | Den**
Zeroblock из ASU убрали что ль?

---

**2026-04-14T23:36:59 | Grigory**
Не пойму почему при загрузке своего конфига амнезии заместо стандартного warp от zeroblock - пропадает интернет. Есть нюансы какие то?

---

**2026-04-14T23:46:06 | Mikhail Velichko**
По поводу первого - есть сомнения. Конфиг генерирую в ЛК подписки. Через "фирменное" приложения - подключается нормально.  Интерфейс создавал из скаченного конфига, засунул его в ту же секцию, что и awg10  zeroblock сует. Галочку поставил, после вашего совета - улучшений не наблюдаю.

---

**2026-04-15T00:14:23 | Алексей Микоянов**
Господа, тут, кажется, Operу помаленьку начало попускать (по крайней мере, у меня), но я уже перешёл на ZeroBlock / Zapret2. В целом полёт отличный, но хотелось бы пускать NoteBookLM через Оперу. (через свой квн в Немеччине слетает авторизация). 
Вопрос - как-то можно подружить opera-proxy и ZeroBlock, кто-то уже проходил этот путь?  Или не стоит пока пытаться даже?

---

**2026-04-15T03:15:28 | Kiss_My_Axe**
Лан, отгрызание порта и сращивание вафли с портом в бридж дало пропуск в ZeroBlock.
Но это сильно геморнее создания обычного интерфейса.

---

**2026-04-15T03:49:55 | Kiss_My_Axe**
ФИЧРЕКВЕСТ

В настоящий момент в список "Входящие интерфейсы" могут попасть только избранные, элитные интерфейсы.
Путём некоторых манипуляций можно и свой интерфейс туда внедрить, но это относительно сложно, и не относительно долго и нудно. Особенно если не сам делаешь, а с чьих-то слов.
Предлагаю создать "спецкод" в имени интерфейса. Если он присутствует - добавлять интерфейс в список вход. интерфейсов ZeroBlock.
Любой набор более-менее осмысленных символов, например "inz".
Надеюсь и уповаю токмо на Вас, ненаглядная моя Екатерина Матвеевна!

---

**2026-04-15T07:07:06 | VK11**
Добрый день. Имеется в наличии vless ключ с опциями Authentication ML-KEM-768 который работает в клиенте v2raytun на смартфоне, но не работает в podkop + sing-box. вопрос собственно будет ли это работать на zeroblock или никаких вариантов нет?

---

**2026-04-15T09:19:11 | Aleksandr Kuzin**
Добрый день, подскажите через zeroblock telegram будет работать?

---

**2026-04-15T09:19:29 | Andrey**
Настроил новый роутер на работу с zeroblock + zapret2 + amneziawg. Хочу вместо амнезии арендовать свой vps и через него трафик пускать. Ткните, пожалуйста, в инструкцию как это сделать 🙂

---

**2026-04-15T09:29:17 | Andrey**
Кучу инструкций по настройке vless на vps я нашел, а вот по запросу zeroblock + vps ничего толкового не находится

---

**2026-04-15T09:46:46 | Eduard Ivanov**
Доброе утро. Сделал настройку zeroblock и zapret2. НО! Я так и не понял как дать доступ к сайтам, которые заблочены. Через опера и авг10? ну я пробовал добовлять сайт в список и 0 толку, мб не тот список . Дискорд доступ я так и не смог получить, возможно я как то неправильно перебираю стратегии @_@.  Подскажите пж. 😱😱

---

**2026-04-15T10:30:21 | Роман**
Zeroblock с vless или амнезией нажать.

---

**2026-04-15T10:34:17 | Nick Chernobaev**
Ребята, привет. Помогите пожалуйста новичку. Не понимаю как установить в zeroblock AmneziaVPN. Там как понимаю нужен vless ключ, а как его сделать на амнезии я не понимаю

---

**2026-04-15T10:45:30 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock
Для стабильной работы обходов рекомендуются свои сервера.

---

**2026-04-15T11:17:06 | Andrey**
Тема zeroblock, там в закрепленных сообщениях есть инструкция по настройке зероблок с запрет2 и авг20. Работает почти все, кроме тг через вайфай

---

**2026-04-15T11:19:18 | Алексей Микоянов**
Продолжаю ковырять нерабочую ссылку vless. Указал нужный транспорт (raw - подсмотрел в работающем клиенте)
Интерфейс её принял, но всё равно не работает. 
Поменял уровень логирования
uci set zeroblock.settings.singbox_logging='1'
uci commit zeroblock
/etc/init.d/zeroblock reload

sing-box начал писать логи. 
Но про секцию со злополучной ссылкой - ни слова.  (про другую секцию с рабочим конфигом видна диагностическая инфа)
Куда копать?


upd: сам случайно расковырял. Пока смотрел логи, увидел, что не резолвятся некоторые домены. (у меня стоит DNS от xbox, так иногда чинится проблема с Gemini). Сменил DNS на девятки - и всё взлетело. 
Похоже, если не резолвится домен, то секция даже не стартует, и в логах её не видно. 

Ну вдруг кому-то поможет.

---

**2026-04-15T11:31:05 | Aleksandr**
Добрый день, настроил ZeroBlock с своей ссылкой vless - все прекрасно работает, спасибо за убер-девайос. 

Но один сервис который доступен под корпоративным VPN-ом не открывается. В обе секции добавил его в исключения и включил смешанный прокси в секции main, но все равно не открывается. Остальные рабочие сервисы кстати открываются - склоняюсь к тому что может этот настроен как-то криво на работе )

Подскажите куда копать? И еще вопрос: нужна ли обязательно секция awg10 если использовать свою vless-ссылку?

---

**2026-04-15T11:37:08 | Nick Chernobaev**
Получается мне надо .conf скачать с сайта амнезия и как-то залить в awg10 в zeroblock? А есть скриншот, где именно это заливать?

---

**2026-04-15T11:59:35 | Aleksey**
Такс, у меня тут мистика какая-то. zeroblock со своей секцией AWG2.  Выбраны списки. Работает все, кроме ютуба. Я уже не знаю куда копать. Кто направит на путь истинный?

---

**2026-04-15T12:15:57 | Aleksey**
https://t.me/routerich/394153/629963 - Уважаемый Фреса, направьте на пусть истинный. 
Единственное что заметил это сообщение в журнале zeroblock "[dns_manager] No backup found, nothing to restore".

---

**2026-04-15T12:20:43 | Aleksey**
Их нет, только zeroblock

---

**2026-04-15T12:52:49 | Routerich**
а Podkop/zeroblock/zapret что-то такое используете?

---

**2026-04-15T12:53:25 | Routerich**
у вас почему то sing-box не стартует, смотрите логи zeroblock

---

**2026-04-15T13:56:05 | Gomer Simpson**
Актуальная - НЕ демон. Система - Пакеты. Обновить списки. Фильтр zeroblock. Обновить.

---

**2026-04-15T14:27:48 | Anna Bagler**
Установить zeroblock https://t.me/routerich/394153/405571 и потом создать свою секцию вместо тех, что будут по умолчанию.

---

**2026-04-15T14:37:05 | Anna Bagler**
Тогда все нужные списки в свою секции. Остальные секции удалить.
YouTube не добавляйте в zeroblock. У вас zapret2 запущен.

---

**2026-04-15T14:43:16 | Роман**
И в zeroblock есть списки.

---

**2026-04-15T14:47:16 | Anna Bagler**
Свой vless, awg или ещё что, что поддерживается zeroblock. C бесплатными вариантами проблемы.

---

**2026-04-15T14:59:01 | Routerich**
самая свежая и актуальная информация по текущим выбранным листам в 
/tmp/zeroblock/rulesets

---

**2026-04-15T15:05:06 | afig**
выгрузил с этого сайта раздел геоблок с нужными мне сайтами в формате txt (чтобы каждая запись была на отдельной строке, как написано в мануале).

ls -la /etc/zeroblock/ | grep ip-lis
-rw-------    1 root     root          1041 Apr 15 14:58 ip-list-geo.txt

в настройках zeroblock включил пользовательские списки и указал путь, но похоже не отрабатывает

может что-то не так указываю?

---

**2026-04-15T15:08:00 | балтийский чай**
Доброго времени. Компьютер подключен кабелем напрямую к роутеру (wan). Поставил Zeroblock, там использую для списка Messengers собственный VLESS и как минимум Телеграм работает. Для списков AI и Geoblock использую уже другой VLESS (оба проверенные, рабочие и платные), но доступа к нейрослопям нет, то есть буквально не могу зайти на сайты claude.ai, chatgpt.com (notebooklm и gemini аналогично). С другими списками, думаю, та же ситуация, так как при включенном списке Torrent, rutracker.org недоступен. В режиме catch-all доступ к всему этому появляется.

НО перечисленные VLESS обходы по спискам работают на устройствах (смартфон и ноутбук), подключенных к Wi-Fi сети роутера.

Как заставить работать списки через wan?

---

**2026-04-15T15:21:40 | Петр**
Всем привет!
А можете, пожалуйста, подсказать, как правильно настроить ZeroBlock  на твиттер? Вроде всё есть, и домена и IP есть, а на ПК не работает? Маршрутизирую через КВН

---

**2026-04-15T15:42:25 | балтийский чай**
Throne выключен, убран из автозагрузки. AmneziaWG клиент с WARP конфигами я удалил, сетевые окружения почистил. DPI скриптов уже давно никаких не стоит, в фоне ничего подозрительного не крутится. Диагностика идеальная в Zeroblock, если она, конечно, показатель

---

**2026-04-15T15:54:58 | Gomer Simpson**
Через ZeroBlock же.

---

**2026-04-15T16:20:42 | Panzerhalzen**
В общем для информации, особенно тем, кто как я сначала пытается решить свою проблему поиском по чату.

В очередной большой по счету раз сбросил роутер до заводских настроек. Далее удалил пакет youtubeUnlock, затем обновил все пакеты, установил zeroblock и перезагрузил роутер. После перезагрузки В ОЧЕРЕДНОЙ РАЗ создал подключение амнезии, пробежался по настройкам фаервола, создал список зероблока и всё заработало.

Несколько дней воевал с этой маршрутизацией, каких-то отличий от того, что делалось в прошлые попытки наладить маршрутизацию, я не вижу, но видимо они есть.

---

**2026-04-15T16:34:45 | Никита Байдин (DOOMGUY)**
Всем привет. В очередной раз обращаюсь за помощью. Телега продолжает на мобиле не работать через ZeroBlock. Ну как не работать. Вроде иногда подсоединяет, но видео или картинки ваще не пробивает. Даже добавил свой отдельный интерфейс АВГ чтобы через него проксировать но хрен там. В чём проблема может быть?

---

**2026-04-15T16:40:58 | Danil**
Всем привет
Настроил интерфейс awg2, интерфейс работает, файервол тоже по инструкции сделал.
Но вот в ZeroBlock не пойму где проблема, трафик не через впн идет и список игнорируется. Если подрубаю прокси в настройках, то прокси рабочий

---

**2026-04-15T17:13:21 | балтийский чай**
На самом деле оказалось, что в плане AI открывается без проблем только сам сайт claude.ai на устройствах, но войти в аккаунт или пользоваться приложением невозможно. Думаю, с остальными AI также.

Подрубил Throne на ноуте (там сайт открывался в отличие от компа) c польским VLESS, вошел в браузере сразу же без проблем. Затем отрубил VLESS, перезагрузил страницу и получил "App unavailable in region", то есть все таки обход по спискам не работает.

Справедливости ради списки, которые я сам делал ранее на базе доменов из v2fly тоже либо не работали, либо работали плохо. Поэтому в Throne использовался профиль Bypass Russia (outbound - proxy, [geoip:ru" geosite:ru, geosite:category-ru, geosite:ru-available-only-inside]). Только с ним не было проблем с доступам к большинству сервисов.

Так что Zeroblock не решает мои проблемы. Пока что

---

**2026-04-15T17:25:30 | Anna Bagler**
А панель управления zeroblock что показывает по секциям?

---

**2026-04-15T17:37:25 | балтийский чай**
По какому устройству? Имеется в виду сам роутер? Потому что я сейчас все тестил на компьютере (wan), ноутбуке и смартфоне (wifi). На любом устройстве могу врубить тот же VLESS, что запущен на Zeroblock, и пробраться на все нехорошие сайты

---

**2026-04-15T17:39:52 | балтийский чай**
Ну и да, если убрать списки и оставить catch all в Zeroblock, то все работает. То есть буквально проблема в роутинге по спискам (конкретные сайты я тоже забивал в конфиг - эффекта нуль), а в нем как бы вся соль

---

**2026-04-15T17:41:36 | Anna Bagler**
Напишите в тему Zeroblock со своей проблемой. Fresa посмотрит.

---

**2026-04-15T18:21:24 | Anna Bagler**
Что из обходов у вас стоит сейчас? Если роутер чистый, ставьте zeroblock. C wa cложно, для него проще локально запускать vpn.

---

**2026-04-15T18:25:08 | балтийский чай**
Кратко: Некорректная маршрутизация по спискам AI-сервисов и прочим - адреса не проксируются, но сatch-all режим работает

Окружение:
• Устройство: RouteRich AX3000 v1 с USB 3.0
• Прошивка: RouteRich 24.10.5 r29087-d9c5716d1d RR-3.9.0
• Подключение клиента: 1) компьютер кабелем напрямую в порт WAN роутера; 2) ноутбук от WiFi; 3) смартфон от WiFi

Проблема:
Маршрутизация трафика на основе списков не проксирует трафик из категорий AI, Geoblock, Torrent и др., в то время как глобальный прокси (сatch-all) работает корректно.

Ноды:
• messengers — VLESS Польша, списки Messengers, Social - работает (как минимум Telegram проксируется)
• ai — VLESS Норвегия, списки AI и Geoblock - не работает (тестировались Claude, ChatGPT, NotebookLM, Gemini)
• awg20 — AmneziaWG 2.0 конфиг из бесплатного генератора WARP  - работает (тестировались YouTube, Discord)

Дополнительная информация:
• Оба VLESS конфига работают идеально в Throne на том же компьютере (и на других устройствах). Но для этого используется правило маршрутизации Bypass Russia (outbound - proxy, [geoip:ru, geosite:ru, geosite:category-ru, geosite:ru-available-only-inside]).
• Zeroblock подключен корректно: в catch-all режиме проблема отсутствует.
• Ручное добавление доменов (например, из репозитория v2fly) в конфигурацию не даёт эффекта/
• На устройствах работающих от WiFi есть доступ к сайтам AI (claude.ai, chatgpt.com), но авторизоваться невозможно (ошибка), как невозможно использовать их приложения на Android.
• rutracker.org проксируется нестабильно (в рамках списка Torrent для ноды awg20) - c разной периодичностью недоступен на разных устойствах и в разных браузерах.

---

**2026-04-15T18:30:33 | Docvspb 🇷🇺**
Кто-то знает, по установке Zeroblock ставить эту галочку?

---

**2026-04-15T18:36:09 | Даниил**
Где можно посмотреть список норм сайтов для покупки сервера под Амнезию? Чтоб поставить ZeroBlock.

---

**2026-04-15T18:37:16 | Павлик🤫**
Вопросик, мне помогли провести настройку роутера
Все сделали
Поставил zeroblock и туда влеску кинули
Сервер выбирается автоматом, попадается и Ютуб с рекламой
Удалял Ютуб анблок, на телевизоре нет рекламы, на телефоне есть
Поставил обратно анблок и убрал влеску на Ютуб
Телефон без рекламы, телевизор не стартует
Поставил Ютуб влеску, телевизор без рекламы, на телефоне нет рекламы
Так и должно быть ?)

---

**2026-04-15T18:43:53 | Роман**
Ну так совсем просто, раз свой. 
Вам что бы хвосты почистить легче сделать сброс на заводские, затем установить zeroblock, создать секцию, вписать свою подписку, выбрать списки. 
А зачем на своём сервере подписку делать, а не отдельную ссылку?

---

**2026-04-15T18:58:03 | Артём**
Добрый день! Настроил Амнезию через собственный VPS, маршрутизацию Zeroblock. Озона и WB нет в списках маршрутизации, но приложения на Андройде всё-равно пишут "Выключите VPN", в чём может быть дело? в списке же нет этих сервисов

---

**2026-04-15T19:01:27 | Олег **
Добрый вечер! В телеграмме не грузятся фото, картинки, видео. Как можно исправить? стоит ZeroBlock и Zapret2.

---

**2026-04-15T19:07:18 | Anna Bagler**
Включайте zeroblock назад. Сделайте замеры на другом сайте, но не спидтест. Проводом же подключено?

---

**2026-04-15T19:12:54 | балтийский чай**
Теперь Яндекс Маркет встречает меня этим. Помогает выключить Zeroblock, загрузить страницу и снова включить. Но надолго ли помогает, непонятно. 

Причем отключение только AWG не помогает, VLESS каким-то образом тоже детектят (либо дело в чем-то другом). 

Яндекс - контора солнышек, как всегда

---

**2026-04-15T19:13:39 | Марк**
подскажите, пожалуйста, пеньку, где можно достать конфиг awg 2.0 для zeroblock? его, получается, отдельно купить надо? Если да, то где можно сделать это? Посоветуйте!

---

**2026-04-15T19:31:48 | Anna Bagler**
Настройки zeroblock. И там есть основной DNS и bootstrap.

---

**2026-04-15T19:40:15 | Ruslan Bilyk**
После установки zeroblock + awg 2.0 некоторые страницы открываются вот так. Причём сайты такие как ютуб, chatgpt, openai и т.д. открываются нормально. Дискорд при этом не открывается. Кто сталкивался? (На скриншоте видно как не открываются темы форума на github, причём не открываются они не все)

---

**2026-04-15T19:44:16 | балтийский чай**
Не сильно разбираюсь во всех тонкостях. На уровне пользователя сейчас такое не настроить в Zeroblock. Может, нужны geoip и geosite базы данных

---

**2026-04-15T20:04:21 | Docvspb 🇷🇺**
Друзья, я установил Zeroblock, Zapret 2. У меня заработало все: Youtube, Instagram, десктопный и мобильный Whatsapp. Все работает на хорошем уровне (СПб). 
Тут пишут про скрипт 5. Напомните, пож, для чего он? Мне он нужен? 

Если все так и останется (хотя не верится даже), то я задумываюсь только о доступе к роутеру извне, с телефона, на котором подключен мобильный интернет (если это возможно, конечно 🤔).

---

**2026-04-15T20:05:31 | Алексей Микоянов**
А как такое чудо посмотреть? Активировал, на кнопку жму - а оно вот так. Можно счхитрить и открыть по доменному, но как будто авторизации нет - ничего не отображается и вылетает через секунду

Можно, наверное, через консоль сбросить пароль [uci set zeroblock.settings.yacd_secret_key=](но вот вопрос - точно ничего больше не сломается?)

---

**2026-04-15T20:36:48 | Дмитрий Григорьев**
Что бы лишний раз Zeroblock не проксировал

---

**2026-04-15T20:47:37 | Alex Korotkov**
но как выше написал, я на всякий случай сорсы из менеджера пустил через квн в zeroblock

---

**2026-04-15T20:58:07 | Anna Bagler**
Подкоп не поддерживает xhttp. Переходите на zeroblock.

---

**2026-04-15T21:05:12 | Николай**
Здравствуйте, подскажите пожалуйста, хочу воспользоваться vpn, через платный конфиг файл.
Отключил awg10
Создал интерфейс awg0, поставил в настройках AmnesiaWGVPN, вставил конфиг файл. Но трафик не проходит через него. Всё  подкоп, zeroblock, zapret и тд отключал.

---

**2026-04-15T21:15:26 | Артём**
в zeroblock нужно создать секцию маршрутизации с сетевым интерфейсом вашего впна

---

**2026-04-15T21:27:14 | Артём**
Да он же zeroblock отключил сам сказал, для начала его включить надо для созданного интерфейса)

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

**2026-04-15T22:10:21 | Anna Bagler**
Если у вас zeroblock, есть полный мануал по нему. Если podkop, то podkop.net Ceкции. Как развернуть/купить готовое подскажет интернет.

---

**2026-04-15T22:33:58 | Anton Лопата**
Не, я поставил zeroblock по инструкции, потом добавил влесс свой в секции, удалил авг 10, добавил списки в влесс соединение и все заработало, после. Добавления пункта geoblock в влесс на ру ресурсы стало ходить не через туннель а напрямую

---

**2026-04-15T23:46:57 | Anna Bagler**
Никто за вас этого делать не будет. Ставьте zeroblock и потом разбирайтесь.

---

**2026-04-16T00:49:46 | Anna Bagler**
Мануал полный по zeroblock читаем. Там, где секции.

---

**2026-04-16T01:19:41 | Ива Саня**
тогда вопрос,при скачке zeroblock такое выдает

---

**2026-04-16T01:39:37 | Kiss_My_Axe**
Смотрите.
Если в секции awg10 у вас реально скриптовый ВАРП (автонастройка ZeroBlock) то им вы ни ка гда не разблокируете чатгепете, гемини, нетфликс и тепе.
Оперу приделайте через Автонастройка.

---

**2026-04-16T01:45:40 | Danil**
не, у меня свой сервер
интерфейс работает, но zeroblock не хочет через него трафик перенаправлять

---

**2026-04-16T02:47:44 | Anna Bagler**
Если подписка и zeroblock, то просите Fresa посмотреть вашу подписку. Никто, кроме него, не поможет.

---

**2026-04-16T03:47:31 | Volshur**
Подскажите, все настроил вроде все работает, вопрос - есть два разных vds. Добавил первый в Секции маршрутизации там настроил списки итд ИТП. Создаю второй нужно чтобы весь трафик шел через ВПН на один нужный мне  ip. Не выбираю списки просто указываю в Дополнительные-Полная маршрутизация нужный мне ip (все адреса в статике) получаю не то что хочу - секция переходит в catch all :( как это можно реализовать в zeroblock? (В подкопе это работает) Ещё в Настройки-дополнительные-исключенные ip добавил ip телефона на котором стоит всякий "плохой" софт. Я правильно понял в этом списке  все ip будут идти на прямую? Проверил да это так :) остался вопрос как сделать секцию для одного ip

---

**2026-04-16T04:40:04 | Routerich**
Ну у вас же есть подписка, вы её так же сможете добавить в Zeroblock на роутере,только его установить нужно предварительно.

---

**2026-04-16T07:18:44 | Evgen**
Понял попробую, еще подскажите есть у меня ключ Vless и амнезии, если получится до репозиториев достучаться, что лучше будет поставить podkop или zeroblock?

---

**2026-04-16T08:39:58 | Routerich**
ага, тогда диагностику Podkop/zeroblock пришлите

---

**2026-04-16T08:52:36 | Routerich**
https://docs.routerich.ru/ru/remote
Раздел
Настройка Podkop и ZeroBlock (Subnet Router) для маршрутизации

---

**2026-04-16T09:05:55 | Routerich**
РКН
пробуйте интерфейс рестартнуть или сам zeroblock рестартите

---

**2026-04-16T10:26:06 | Роман**
Ну кроме теории заговора что ТСПУ видит дурение и блочит ру сайты - я ничего предложить не могу. Вы же просто заперт2 устанавливаете или с zeroblock?

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

**2026-04-16T11:18:27 | Алексей Микоянов**
Есличо - PcapDroid в помощь. Рута не требует. Можно даже дамп не записывать, соединений TG делает не очень много, можно глазками отследить. 
Далее сравнить с содержимым
cat /tmp/zeroblock/rulesets/messengers_ipv4.json | jq .
..понятно, что это не правила sing-box, но будем считать, что всё что загрузилось - то и работает

---

**2026-04-16T11:31:02 | wee**
Здравствуйте!
Сегодня пытаюсь накатить пакет zeroblock, зависает на этом моменте обновления пакетов и все

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

**2026-04-16T12:41:38 | Артём**
Если я настроил VPN через роутер и zeroblock, приложения на телефоне и компьютере тоже ходят через маршрутизацию zeroblock или маршрутизация только на веб браузер работает?

---

**2026-04-16T12:42:48 | Routerich**
маршрутизация работает на всё, что прописано в zeroblock и не зависит от устройств, но зависит от их настроек.

---

**2026-04-16T13:21:28 | Anna Bagler**
Берите стратегии в теме по запрет2 или поставьте галочку автозагрузки стратегии для z2 в zeroblock. Перезапустите и посмотрите.

---

**2026-04-16T13:44:14 | Routerich**
Здравствуйте.
ютуб возможно будет, для остального ставить ZeroBlock.

---

**2026-04-16T14:03:21 | Anna Bagler**
Вам надо обновлять прошивку без сохранения настроек. Производить первоначальную настройку роутера. Потом ставить zeroblock, но можно и скрипт 5, если совсем сложно все. А потом уже смотреть.

---

**2026-04-16T14:04:20 | Alex L**
Аналогично , поставил ZeroBlock + Zapret2  , создал секцию прокси с платным  vless  .  awg и оперу удалил  . Всё работает ( 9999/dot , mgts/gpon ) кроме gemini  , но им редко пользуюсь . Когда надо - запускаю cisco anyconnect через Германию .  Пробовал прописать в ZB , создав интерфейс на опенконнект и секцию в ZB , но через неё работают только соцсети - fb, insta  , больше практически ничего и youtubе тоже не работает , секция всегда красная , не знаю как настроить и куда ещё смотреть в настройках.

---

**2026-04-16T14:04:26 | Anna Bagler**
Домены внести в исключения zeroblock.

---

**2026-04-16T14:08:42 | Anna Bagler**
https://t.me/routerich/80283/352975?single - прошивка. Только внимательно по цвету usb
https://routerich.ru/setup - первичная настройка роутера
https://t.me/routerich/394153/405571 - zeroblock.

---

**2026-04-16T14:51:06 | М П**
Здравствуйте где можно узнать что такое zeroblock ?

---

**2026-04-16T14:54:46 | Денис Сурков**
Всем привет, наверное уже есть решение, но в чате не смог найти. У меня стоит ZeroBlock + Zapret2, настроенное remote control с телефона до роутера. А проблема в том, что телеграм на телефоне очень долго крутит обновление, подключение быстро проходит, но вот обновление очень долго, может так минут 7-10 висеть. Есть уже решение по такой проблеме?

---

**2026-04-16T14:59:05 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-16T15:13:48 | М П**
подскажи пожалуйста мануал zeroblock Pdf  страница 10 архитектура куда добавлять домены  мне нужно будет вручаю вводить сайты ?

---

**2026-04-16T16:01:17 | A V**
Благодарю ещё раз, всё получилось. Я просто не понял, насколько всё просто в zeroBlock, ломился в открытую дверь. Ещё раз спасибо за Ваше терпение. )

---

**2026-04-16T16:40:22 | Роман**
Уверены что запрет помог,  а не zeroblock?

---

**2026-04-16T16:42:23 | Валентин**
Имею ввиду,я не уверен, возможно и zeroblock

---

**2026-04-16T17:04:25 | Роман**
Каким образом секции из zeroblock имеют отношение к запрет2?

---

**2026-04-16T17:42:30 | Docvspb 🇷🇺**
Я роутер на днях получил. Делал всё по инструкции: Zeroblock, Zapret2. Больше ничего не менял. Все работало отлично. Я не готов к экспериментам: боюсь все сломать. Мне нужно чётко понимать: доустановить пакет / удалить пакет, и что получится в результате? Если можете подсказать более конкретно, был бы благодарен...

---

**2026-04-16T17:45:41 | iProxx**
Если Zeroblock ставили то Youtube работает через Zapret2, а не через Youtubeunblock как на дефолтных настройках.

---

**2026-04-16T17:50:03 | Вадим Яриков**
Поделитесь пожалуйста ссылкой на инструкцию по zeroblock. Как поставить на роутер

---

**2026-04-16T17:57:54 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

https://t.me/routerich/80283/468513 - полный мануал zeroblock

---

**2026-04-16T18:27:40 | Dmitry**
Подумываю перебраться с podkopa на zeroblock+zapret2 случайно нет скрипта для автоматической установки и настройки по типу скрипта N5

---

**2026-04-16T18:28:28 | Роман**
Через пакеты устанавливайте.
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-16T18:28:37 | Ruslan Bilyk**
Нажатие на СТОП справа выключает ZeroBlock правильно?

---

**2026-04-16T18:28:38 | Routerich**
Только надо сбросить роутер перед установкой Zeroblock

---

**2026-04-16T18:45:29 | Ruslan Bilyk**
Уже 5 нашел. Видимо не мог из-за zeroblock, а если сейчас заработает дискорд зероблок потом дальше не будет мешать? Или он только при тесте мешает?

---

**2026-04-16T19:04:20 | Алексей**
Всем привет. Перехожу на Zeroblock, и возникла проблема. Не устанавливается запрет. В чем проблема может быть?

---

**2026-04-16T19:13:12 | Роман**
Дс из zeroblock убран?

---

**2026-04-16T19:41:46 | Роман**
Установить zeroblock, создать свою секцию, вписать прокси, выбрать списки. Автонастройку пропустить. 
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-16T19:57:11 | Anna Bagler**
Тогда изучайте небесплатные варианты, которые можно использовать в zeroblock/podkop.

---

**2026-04-16T20:23:37 | Роман**
А кто сказал что в подкопе такое есть? В zeroblock - есть.
В подкопе надо создать секцию с исключениями и уже туда внести домены.

---

**2026-04-16T20:30:21 | Nick Kalugin**
есть ли возможность маршрутизировать через секцию zeroblock-a только часть локальных устройств (не полностью их трафик завернуть, а именно по спискам, но не все устройства)?

---

**2026-04-16T21:05:03 | Anna Bagler**
А если отключить zeroblock, начинает google нормально работать?

---

**2026-04-16T21:07:58 | Ruslan Bilyk**
Чем можно попробовать заменить zapret2, если он не работает. Zeroblock тоже не работает когда я включаю в нём discord. Ну точнее дискорд не работает

---

**2026-04-16T21:20:43 | Ruslan Bilyk**
он же занимается ими при включённом zeroblock или где-то ещё?

---

**2026-04-16T21:23:22 | Anna Bagler**
Zeroblock. И свой vless.

---

**2026-04-16T21:26:37 | Усталый пехотей**
Zeroblock и прописи vless

---

**2026-04-16T21:28:19 | Ruslan Bilyk**
Я отключил zapret2 и zeroblock, а сайт всё равно не открывается. Который про какую-то игру. И я почти уверен, что он не заблокирован и т.д.

---

**2026-04-16T21:29:19 | Key**
У меня вообще не установлен zeroblock. А тг запущена через отдельную секцию подкопа куда и прописан мой vless ключ.

Я же грю у всех все по-разному )

---

**2026-04-16T21:32:08 | Docvspb 🇷🇺**
К сожалению, да. Я сейчас попробовал остановить службу ZeroBlock — google drive шустро заработал. 

А что случилось-то?..

---

**2026-04-16T21:39:16 | Anna Bagler**
cidr в настройках zeroblock. Исключения по доменам в секции, списки.

---

**2026-04-16T21:45:41 | Ruslan Bilyk**
А у вас zeroblock работает?

---

**2026-04-16T21:48:24 | Anna Bagler**
Это если та сторона вытаскивание разрешила. Пробуйте прямо подпиской, но в zeroblock.

---

**2026-04-16T22:07:43 | Honest Fox**
Здравствуйте, почитал мануал к zeroblock, поставилось zeroblock+zapret2 и вроде всё работает, но можно мне тыкнуть пальцем куда можно ткнуть свой впн ( типа подписка, там ссылку только дают) в zeroblock, сказали что так можно, но я никак не найду

---

**2026-04-16T22:14:18 | Владимир Волков**
Zeroblock в соседней теме

---

**2026-04-16T22:41:01 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock

---

**2026-04-16T22:41:25 | Роман**
Потом это.
https://t.me/routerich/80283/468513 - полный мануал zeroblock

---

**2026-04-17T00:15:44 | Роман**
Тогда просто сброс и установка zeroblock. Создать секцию, вписать прокси, выбрать списки и готово.

---

**2026-04-17T01:32:51 | Роман**
https://t.me/routerich/394153/405571 - мануал zeroblock

https://t.me/routerich/394153/588710 - мануал zeroblock PDF

https://t.me/routerich/394153/581524 - видео zeroblock
Автонастройку пропустить, создать свою секцию, вписать своё прокси, выбрать списки.

---

**2026-04-17T07:21:49 | Routerich**
вам надо определится либо Podkop, либо ZeroBlock (лучше его)

---

**2026-04-17T07:24:50 | Molodoy Makkonehi**
zeroblock удобнее:
1. удобнее рбаотать с секциями
2. из под коробки поддерживает саб линки с автосвапом
3. xray (хз подкоп ворде только vless)
4. автоматом ставит zapret2
это то что прям маст хев. поправьте если чтото не так написал

---

**2026-04-17T07:28:08 | Anna Bagler**
Его нет из коробки, поэтому он не может быть предустановлен. Если был, то тем более сбрасывайте настройки. Потом zeroblock. Галочка Не создавать маршруты нужна для интерфейса с амнезией. Можно использовать и vless, и интерфейс.

---

**2026-04-17T08:43:14 | Kuz Ka**
Привет, если ли большая разница между скриптом N5 и zeroblock?
Или если 5 работает, то лучше не обновляться?

---

**2026-04-17T09:32:41 | Kuz Ka**
Установил zeroblock
Добавил свой awg

Как доустановить opera proxy в качестве запасного варианта?
Сейчас на чистой установке без скрипта N5 опера прокси нет

---

**2026-04-17T09:47:59 | Роман**
Zeroblock со своими серверами, zapret2 для Дискорда и Ютуба, стандартнаые списки, никаких специальных доменов не вносил.

---

**2026-04-17T11:03:36 | Routerich**
Но лучше смотрите в сторону Zeroblock, вместо Podkop

---

**2026-04-17T11:34:51 | Виктор**
Обновил прошивку, установил Zeroblock. Не все сайты доступны. В Zapret2 запустил вечером поиск стратегий, утром все искал, может ищет до сих пор. Это нормально? И интернет сильно тупил.

---

**2026-04-17T11:51:18 | Bullet for my valentine Poison**
А если зайти в система - пакеты и в фильтр вписать Zeroblock. Какие версии у пакетов?

---

**2026-04-17T11:59:41 | Виктор**
Вбил конфиги для zeroblock и узнал что это графический редактор оказывается.

---

**2026-04-17T12:56:46 | Gomer Simpson**
Вероятно, нужно и кэш браузера почистить, и ZeroBlock перезапустить, и роутер перезагрузить.

---

**2026-04-17T13:06:05 | Routerich**
Здравствуйте. 
Ставьте сразу Zeroblock

---

**2026-04-17T13:06:38 | Сергей Сергеевич**
ИИ советует так сделать, как думаете, есть право на жизнь?

Остался один путь — кастомное правило sing-box в /etc/zeroblock/sing-box.d/. Там можно задать source + geosite matching вручную.

Сначала разведка — скинь вывод:

ls -la /etc/zeroblock/
ls -la /etc/zeroblock/sing-box.d/ 2>/dev/null
find /tmp -name "sing-box*.json" 2>/dev/null
find /var/run -name "sing-box*" 2>/dev/null
ps | grep -E "sing-box|xray"
Нужно найти:

Куда класть custom JSON фрагмент
Формат — это override/merge к основному route.rules
Имя outbound для wan-direct и для USA-vless
После этого сделаем файл типа /etc/zeroblock/sing-box.d/device_228_split.json с правилом:

{
  "route": {
    "rules": [
      { "source_ip_cidr": ["192.168.1.228/32"], "rule_set": ["russia_outside"], "outbound": "direct" }
    ]
  }
}
И уберём fully_routed_ips='192.168.1.228' из секции USA — кастомное правило заменит. Скинь listing — соберу точный конфиг.

---

**2026-04-17T13:16:45 | Андрей**
Доброго дня!
У меня zeroblock не реагирует на zeroblock.settings.output_network_interface
Я так понимаю, достигаться это должно путём использования 
"bind_interface": "interfacename",
в конфиге sing-box. 
Однако,  я там ничего не нашёл
00-log.json
01-experimental.json
10-dns.json
20-inbounds.json
30-outbounds.json
40-route.json
root@RouteRich:/tmp/zeroblock/sing-box.d# grep -i "bind_interface" *
root@RouteRich:/tmp/zeroblock/sing-box.d# 
Натурные испытания также показывают, что трафик идёт через интерфейс wan с наименьшей метрикой

---

**2026-04-17T13:37:34 | Алексей Николаев**
chatgpt через AWG в zeroblock перестал на телефоне работать! вСЁ, хана, нужен свой КВН или какие то бесплатные шаги можно предпринять?

---

**2026-04-17T13:45:54 | Nikita Gukovskiy**
господа, помогите не шарящему. сделал openconnect интерфейс, но он не появляется в zeroblock в списке сетевых интерфейсов. шо делать?

---

**2026-04-17T14:14:57 | Bullet for my valentine Poison**
Удаляйте и ставьте Zeroblock

---

**2026-04-17T14:18:12 | Bullet for my valentine Poison**
Пусть ставит Zeroblock - это будущее.

---

**2026-04-17T15:02:06 | Роман**
Имею в виду оперу прокси и авг, взять vps поднять панель или купить vless, amnezia - вставить в роутер. 
Что zeroblock, что подкоп это инструменты, без каналов связи с серверами - они бесполезны.

---

**2026-04-17T15:53:57 | sHpr1t3!++**
вплане настраивать? просто посмотретьч то надо из сайтов и если они есть в этих списках, то тогда галочку поставить в списках ZeroBlock?

---

**2026-04-17T16:10:13 | sHpr1t3!++**
я поставил в ZeroBlock music галочку, спотифай так и не работает, есть решение?

---

**2026-04-17T16:17:31 | IT**
Правильно, что я обновляются периодически только:
zeroblock
zapret2
operaproxy
amnezia
Больше ничего особе не надо обновлять из реп?

---

**2026-04-17T17:19:02 | Артем Яковлев**
А вот там какой то ZeroBlock решает это или тоже нет?

---

**2026-04-17T17:28:21 | Anna Bagler**
Подкоп сам по себе, вместо него лучше zeroblock. Для YouTube пробовать запреты и стратегии.

---

**2026-04-17T17:55:09 | Anna Bagler**
К секции в средстве обхода интерфейс привязали? В zeroblock, например.

---

**2026-04-17T18:26:31 | Anna Bagler**
В zeroblock есть галка исключить торрент-трафик. Сайты вообще-то сами по себе, а закачки сами по себе.

---

**2026-04-17T19:16:42 | Dh_z**
подскажите пожалуйста, zeroblock обязательно должен ставится на чистую прошивку сброшенного в дефаул роутера? если конфигурацию сохранить её потом можно восстановить или нет?

---

**2026-04-17T19:24:26 | Anna Bagler**
Отключите пока zeroblock и посмотрите на скорость от провайдера.

---

**2026-04-17T20:25:18 | K163R**
В итоге поставил в ZeroBlock прокси ,где дал урл тест на несколько ссылок 1 на троян и 1 на влесс, поставил в списках что проксировать и все заработало..

Спасибо вам кто помог, чтоб ваша семья жила до 100 лет!

---

**2026-04-17T20:28:29 | Anna Bagler**
Vless, awg и прочее. podkop.net Секции - можете посмотреть, что поддерживает подкоп. Можете со сбросом перейти на zeroblock, в нем есть поддержка подписок.

---

**2026-04-17T20:30:52 | Дмитрий Митченко**
Я пытался поставить Zeroblock. Но у меня на этапе обновления все остановилось. Постоянно висит статус "обновление"

---

**2026-04-17T21:13:57 | Anna Bagler**
Ну, киньте в zeroblock с описанием вашей проблемы. Fresa, посмотрит, наверное.

---

**2026-04-17T21:17:12 | Anna Bagler**
Нужно что-то своё: vless, hy2, ещё что и zeroblock.

---

**2026-04-17T21:22:17 | Anna Bagler**
Zeroblock, cвой vless или подписку для секции с нужными списками.

---

**2026-04-17T21:23:04 | Routerich**
включите лог сингбокса, он сам рассказать должен что с ним, или удаляйте зероблок, удаляйте конфиги и ставьте по новой 
rm /etc/config/zeroblock* /tmp/zeroblock_status.json && rm -rf /tmp/zeroblock /etc/sing-box/subscriptions /etc/zeroblock

---

**2026-04-17T21:31:41 | Anna Bagler**
Идите в тему по zeroblock. Там есть пошаговая инструкция по установке в закреплённых сообщениях.

---

**2026-04-17T22:22:48 | Александр Овсянников**
Всем доброго вечера.
Сейчас стоит 5ый скрипт, до последней недели всё было хорошо, а с прошлой пятницы начались проблемы.
Секция Дискорд не работает.
Main вроде ворочается но очень туго, если правильно понял сейчас все переходят на zeroblock + zapret2(если не прав поправьте)
Существует какой-то скрипт? Или может быть подробная инструкция?
Версия так же 24.10.4 остаётся?

---

**2026-04-17T22:25:52 | Anna Bagler**
Бесплатные варианты внутри обходов более не работают. Свой vless или ещё что в подкоп. Лучше со сбросом поставить zeroblock, он более гибкий.

---

**2026-04-17T23:14:50 | Andrew Arzaev**
Всем привет!

Взял роутер, перепрошил на OpenWRT. Настроил AmneziaWG интерфейс и ZeroBlock по аналогии с тем, как делал на WARP — там всё работало.

Интерфейс поднялся, трафик идёт, но ZeroBlock сайты из списков всё равно открывает напрямую, а не через VPN. Пробовал перезагружать роутер и менять параметры в ZeroBlock — не помогло.

Кто сталкивался с таким — подскажите пожалуйста, что может быть не так? 🙏

---

**2026-04-17T23:21:13 | Docvspb 🇷🇺**
Здесь часто пишут, что бесплатные варианты более не работают. Я могу сказать, что делал все по инструкции на роутере из коробки (ZeroBlock, Zapret 2). Не меняя ничего больше. 
Работают на ПК и телефоне Youtube, Instagram, Linkedin, Whatsapp. Telegram работает на телефоне. Только почему-то в группе этой не загружаются скриншоты. С остальными пользователями могу ими обмениваться. Браузерная версия Telegram тоже работает, но в ней я могу и скриншоты просматривать. 
Короче, все базовые приложения и сайты работают у меня без платных ключей/подписок.

---

**2026-04-17T23:23:40 | Роман**
У вас подкоп наверное, у меня zeroblock.

---

**2026-04-18T00:08:17 | Михаил Краев**
Не могу побороть Spotify - а именно авторизацию у них через веб, не пускает регион блок (в апп все работает отлично).  Что пробовал, со своим прокси в zeroblock:
1. Основная (единственная) секция с нужными листами - включал Music. Не помогает. Добавлял кучу доменов - аналогично. 
2. Добавил новую секцию выше первой. Отключил fakeip. Добавил те же домены. Результат точно такой же.

---

**2026-04-18T00:22:41 | HiLLL**
zeroblock чкрез поиск найдите

---

**2026-04-18T00:24:04 | Tony Montana**
Всем привет.
Ребят подскажите что не так, после покупки роутера установил себе zapret. Всё было отлично вся МЕТА вселенная работала в том числе и ютуб. 
Позавчера разом все перестало работать. Запустил запрет заново, с телефона работает а с телика нет.
 Решил установить zeroblock, всё сделал по инструкции! Почему то запрещена так и не работает. Ещё почему то из списков сообществ убираю ютуб, сохраняю применяю. А он всё равно в списках остаётся!
Что сделал не так??

---

**2026-04-18T00:41:20 | Роман**
Zeroblock имба лютая, но только когда выйдет масштабное обновление, куча новых фич,  особенно выбор приложений на windows (с помощью политик) которые пойдут в прокси. Проще говоря - можно будет выбирать отдельные приложения (игры) для отправки в прокси через секцию.

---

**2026-04-18T00:41:31 | Anna Bagler**
В закрепах темы zeroblock есть ссылка на списки.

---

**2026-04-18T08:19:43 | Николаич**
После сброса на заводские установил zeroblock + zapret2. В zapret2 нет дефолтных страт, как установить?

---

**2026-04-18T08:34:58 | Slava**
Странно. Поставил по методичке AWG2+ZeroBlock, 2ip.ru и 2ip.io показывают правильные айпишники. Вроде всё взлетело, всё открывается. А один сайт, my.animespirit.ru, не пашет, хотя добавлен в пользовательский список ZeroBlock. При этом, если включаю на компе отдельно амнезию, то на сайт спокойно влетает.
Подскажите, как поправить.

---

**2026-04-18T10:20:18 | Роман**
А на данный момент как дела у zeroblock? Сыроват или уже лучше Podkop'а?

---

**2026-04-18T11:01:36 | Nikita Tkachuk**
Подскажите, а если поиском не могу найти Zeroblock пакеты, что делать?

---

**2026-04-18T11:06:00 | Гев**
А подскажите пожалуйста,в инструкции написано что "Важно: Вкладка Автонастройка доступна только на верифицированных устройствах RouteRich. Если ваше устройство не прошло верификацию, эта вкладка будет
скрыта. В таком случае все компоненты необходимо устанавливать и настраивать
вручную.
1. Откройте веб-интерфейс роутера
2. Перейдите в Службы -> ZeroBlock -> Автонастройка" 
но у меня в службе нет раздела ZeroBlock,его нужно вручную ставить?

---

**2026-04-18T11:23:30 | iProxx**
В Zeroblock в Секциях маршрутизации добавляете новую секцию выбираете Прокси и вставляете ссылку Vless.
Ну и в списках сообществ выбираете нужное.

---

**2026-04-18T11:56:03 | Vadim**
Уважаемые участники чата, помогите пожалуйста!
Уже все инструкции просмотрел, не могу найти.

Как на Zeroblock настроить подключения к нужным IP адресам чтобы обходить блокировку РКН?

Пример: у меня есть proxy IP:port, куда мне его прописать ?Чтобы потом с телефона подключенного к routerich через прокси приложение подключиться к этому IP.

---

**2026-04-18T12:25:11 | VK11**
День добрый. поставили товарищу ну пустую прошивку zeroblock со всем содержимым и он пытается все под себя настроить и спрашивает, а почему в секциях маршрутизации не отключаются списки сообщества после сохранения и применения все остается как было.

---

**2026-04-18T13:28:18 | Константин**
В нашей локации ну это видимо пока. Трём товарищам посоветовал, все завелось из коробки так же как и у меня, операторы разные.  Ютуб так вообще сразу с базовым анблоком. Тестил zeroblock+zapret2 awg opera proxy так же все без проблем подтянулось и заработало. Сейчас все это конечно настроено под себя, ненужное убрано типа awg и opera добавлены свои каналы так скажем.

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

**2026-04-18T16:06:53 | Артём**
У кого не работает мир танков через zeroblock, уберите из списка AWS весь, видел в чате у кого то были проблемы с этим

---

**2026-04-18T16:29:03 | Bullet for my valentine Poison**
Зероблок и там закрепы пощелкайте, будет мануал как Завести Zeroblock

---

**2026-04-18T17:27:51 | wee**
Кто-нибудь настраивал на Zeroblock белые списки?

---

**2026-04-18T18:00:18 | ~**
Ну во-первых, вы же уже прислали скрин с нужными кнопками. Во-вторых, в топике по Zeroblock в закрепе есть мануалы в pdf. Почитайте. В любом случае будет полезно.

---

**2026-04-18T18:56:08 | Dmitry**
Кстати, вопрос, встроенные списки доменов для Zeroblock локально где-то хранятся? Я Zeroblock  настраивал по одному из гайдов и обломался на 2ip.io, пока до меня не дошло, что он есть в списке CDN:Hetzner.

---

**2026-04-18T18:56:23 | Anna Bagler**
Своe в zeroblock вставили или бесплатное по умолчанию?

---

**2026-04-18T19:36:02 | Никита**
Здравствуйте. Я новичок в этом и хочу понять, нормально ли у меня сейчас со свободной оперативной памятью и хранилищем на Routerich AX3000 v1.
поставлен пока только запрет 2 и zeroblock

По скриншоту вижу примерно:

ОЗУ: 485.76 MiB всего, свободно около 291 MiB.

Хранилище: 71.34 MiB всего, свободно около 30.44 MiB.

Временное хранилище: 242.88 MiB всего, свободно около 3.65 MiB.

Подскажите, пожалуйста, это нормальные значения для такой модели или уже мало?
Я пишу, потому что только начинаю разбираться и не понимаю, это еще ок или уже стоит чистить/экономить место.

---

**2026-04-18T19:57:01 | Anna Bagler**
Не работают бесплатные решения в zeroblock. Есть свой vless или ещё что? YouTube через запрет2 тоже не заработал?

---

**2026-04-18T19:57:28 | Gomer Simpson**
Я сегодня РР обновлял. ZeroBlock поставил, оперу, авг. Так воот: в Опере выбрал список Messenger - Телеграм заработал, даже созвониться получилось. Без списков доменов и подсетей. Просто список Messenger в Опере.

---

**2026-04-18T20:03:22 | Mike Rizhoff**
Еще раз. Роутер прошит последней прошивкой (форком). Настройки пооизведнны через мастер настроек. Дальше иду в пакеты - обновить- ввожу маску доступные на zeroblock. Пакеты находятся, но не ставятся - скрины в моих сообщениях. Дома, на проводном инете делал все то же самое, все встало, настроилось и работает без проблем

---

**2026-04-18T20:36:01 | Alex L**
Не знаю почему, но секция на vpn-oc0 начинает работать только после того как загрузится ZB и после этого пропишется значение мту . При этом как писали выше  , ZB загружается быстрее , чем поднимается интерфейс vpn-ос0 , то есть надо ждать создания интерфейса , потом делать рестарт ZB , потом прописывать мту , и только полсе этого секция заработает . С учётом этого прописал а автозагрузку : # Put your custom commands here that should be executed once
# the system init finished. By default this file does nothing.
sleep 10
service zeroblock restart
# Проверка интерфейса перед изменением MTU
if ip link show vpn-oc0 &>/dev/null; then
    ip link set dev vpn-oc0 mtu 1200
    echo "MTU для vpn-oc0 установлен в 1200"
else
    echo "Интерфейс vpn-oc0 не найден"
fi
exit 0

---

**2026-04-18T20:55:59 | Роман**
Открывайте в zeroblock и смотрите куда гугл ходит.

---

**2026-04-18T21:05:37 | Sergio Yakovlev**
zeroblock

---

**2026-04-18T21:11:01 | Дестападор**
Добрый день, есть какие-то хорошие схемы разблокировки ТГ на уровне роутера без ВПН/проксей? Сейчас стоит zeroblock и zapret2, может что обновить можно?

---

**2026-04-18T21:21:15 | Anna Bagler**
https://routerich.ru/setup - первичная настройка роутера
https://t.me/routerich/394153/405571 - zeroblock. Но нужен свой vless или ещё что-то. Бесплатное может не работать.

---

**2026-04-18T21:35:31 | Алексей**
Здравствуйте! Откуда zeroblock списки запрещенных доменов парсит? Где можно список посмотреть?

---

**2026-04-18T21:36:21 | Alex**
Дорого вечера всем... Вопрос возник (понятно что и сам покопаюсь - но хотелось бы меньше граблей собрать) накупил настроил родственники и знакомым уже штук 5 RR - и в принципе разобрался с логикой интерфейса zeroblock - удобно понятно и огромное спасибо за то что двигаетесь и развиваетесь... У меня для командировок роутер маленький и удобный - gl.inet Beryl AX (GL-MT3000) на него сейчас установлена ванилька openwrt - хочу туда установить zeroblock - понятно что не будет авто настроек и тп.. но в принципе - какие-нибудь зависимости есть у него которые нужно учеть (не из главной ветки owrt пакеты) ?  ... Не хочу изучать настройку подкопа и чего нить ещё подобного - всё равно в основном RR везде у меня и ради 1 роутера во что-то другое погружаться не очень хочется . А возить с собой RR - просто не удобно). Кароче главный вопрос встанет на чистую оврт с люси - на тойже архитектуре...

---

**2026-04-18T22:38:43 | Роман**
Да ладно! А почему тогда уже на протяжении всего времени как существует zeroblock (я давно на него перешёл) - у меня всё работает? Вывод, прокладка между роутером (с рученками) и ПК во всём виновата. 
Пока я констатирую факт - зероблок после установки не работает.
Логи будут? Пока я констатирую факт что всё работает. 
Невозможно разобраться с причиной не работы ютуба и телеграма, так как списки после добавления крошат установку. 
Ещё раз, логи будут?
Сделайте такой же скрипт для установки зероблока, какой был сделан для подкоп, и вопросов не будет.
Скриптов для zeroblock не будет. 
Роутерич в первую очередь продукт, приобретаемый для определённых функций. А не за опенврт и медиатек процессор
И тут мимо! Это не чудо роутер который сам вам обойдет блокировки, это инструмент который нужно настраивать, чего к сожалению вы не умеете (надеясь на чудодейственные скрипты). За сим откланиваюсь, хорошего вам вечера.

---

**2026-04-18T22:58:13 | Anna Bagler**
На чистую систему zeroblock ставить. Но бесплатные варианты стабильно все равно не работают. По этой ошибке найти скачивание списков через vpn/proxy и поставить или убрать галочку, если уже стоит.

---

**2026-04-18T23:04:08 | Anna Bagler**
Ага, у вас не та ошибка. Прошу прощения. Да вам перезапуск скрипта или на чистый zeroblock ставить.

---

**2026-04-18T23:30:21 | Anna Bagler**
Если vless, то прокси. Пусть будет зарубежный. Перетащить. Кроме YouTube, для него запрет1 и подбор стратегий. На ссылку вашу не ругается? Вам лучше zeroblock поставить со сбросом роутера, я думаю.

---

**2026-04-18T23:31:58 | Anna Bagler**
Нет. Не работают стабильно бесплатные варианты, а не сам подкоп. Ему на замену на РР в любом случае приходит zeroblock.

---

**2026-04-18T23:58:54 | HiLLL**
запустите в терминале zeroblock awg warp

---

**2026-04-19T00:00:33 | Gomer Simpson**
Вставить ссылку в ZeroBlock.

---

**2026-04-19T00:03:17 | Kiss_My_Axe**
Посмотрел я, как выглядит вывод
Zeroblock разбор урла влесс итп    : время_отклика [ секция ] 
и чото не возрадовался. Надо переделывать.

---

**2026-04-19T00:15:46 | 𝕮𝖞𝖇𝖊𝖗 𝕮𝖗𝖔𝖜**
Добрый вечер всем
Настроил Zeroblock, подкинул свой ВПН, все работает, но есть ньюанс. 
Скорость всего этого порой бывает безбожно мала. Видео подгружаются, и порой бывают в 480р. Причем как на телефоне, так и в браузере. 
Тг тоже загружается раза в 2-3 дольше, чем с тем же впн через роутер. 
Что я мог не правильно сделать в настройках?

---

**2026-04-19T00:36:18 | iProxx**
Ставьте Zeroblock. В нем уже есть Zapret2, и потом свою секцию с Vless добавьте

---

**2026-04-19T00:38:29 | Anna Bagler**
А ключики нужны будут для другой запрещенки в zeroblock.

---

**2026-04-19T02:13:25 | Kiss_My_Axe**
Просто на файл конфигурации ЗероБлок повесили триггер, который срабатывает, если этот файл меняется. И "запускает" команду 
/etc/init.d/zeroblock <reload> (релоад действие по умолчанию, потому опущено). ЗБ перечитывает изменённый конфиг.

---

**2026-04-19T05:07:23 | Anna Bagler**
Zeroblock.

---

**2026-04-19T05:23:30 | Anna Bagler**
Когда вы в поле фильтра введёте zeroblock, увидите и luci. Подкоп рядом хоть не стоит?

---

**2026-04-19T05:25:49 | IT**
Подкоп не стоит.
luci-app-zeroblock - конечно установлен

---

**2026-04-19T05:27:24 | IT**
zeroblock работает, пользуюсь им.
Я не найду вкладку xray, который через зероблок поставил

---

**2026-04-19T05:44:46 | IT**
Нашел, спасибр)
Службы > ZeroBlock > Секции маршрутизации
Тип конфигурации прокси: Xray конфигурация Outbound

---

**2026-04-19T07:22:20 | Виталий**
Здравствуйте! Сбросил роутер до заводских, хочу подключить модем E3372.
Есть свой Vless, нужно ли сначала подключать роутер по проводу от провайдера и ставить Zeroblock и Zapret, или сразу воткнуть модем и всё устанавливать подключившись к модему?

---

**2026-04-19T08:46:56 | Руслан Покатилов**
Можно ли как-то настроить zeroblock и zapret 2 что бы скорость не падала почти в половину?

---

**2026-04-19T09:10:27 | Руслан Покатилов**
Ну у меня стояли стандартные настройки zeroblock с awg10, его выключил и скорость загрузки в стиме выросла, хотя трафик не должен идти через awg10 от стима

---

**2026-04-19T09:28:14 | Umka**
Добрый день!
Как выкорчевать you tube из zeroblock
Awg10? Снимаю галочку, сохраняю, применяю, захожу обратно в списки а он там же....

---

**2026-04-19T09:31:00 | Валерий**
Добрый день. Подскажет кто, настроил Zeroblock и tailscale, подцепляюсь удаленно по tailscale, выход настроен через роутер, все по мануалам. На ПК домашнем работают все обходы, на телефоне при подключении через tailscale работает только ТГ. Все остальное словно в тупик валится, ни вк, ни ютуб, вообще ничего не маршрутизируется по ощущениям. Куда копать и смотреть?

---

**2026-04-19T09:35:51 | Валерий**
Добрый день. Подскажет кто, настроил Zeroblock и tailscale, подцепляюсь удаленно по tailscale, выход настроен через роутер, все по мануалам. На ПК домашнем работают все обходы, на телефоне при подключении через tailscale работает только ТГ. Все остальное словно в тупик валится, ни вк, ни ютуб, вообще ничего не маршрутизируется по ощущениям. Куда копать и смотреть?

---

**2026-04-19T10:09:57 | Роман**
А как это относится к zeroblock?

---

**2026-04-19T10:22:55 | Bullet for my valentine Poison**
Zeroblock и мануал в разделе Вики

---

**2026-04-19T11:01:12 | Sergey Lonchakov**
А что лучше zeroblock или podkop?

---

**2026-04-19T11:27:44 | Nick Chernobaev**
Добрый день. Подскажите пожалуйста, в zeroblock в настройках секции под спискам есть поле «пользовательские домены». Это чтобы вставить сайты, которых нет в списках, но нужно, чтобы они тоже открывались через впн? Просто мне нужно, чтобы открывался сайт https://www.affinity.studio/ я его туда вставил, но он не открывается

---

**2026-04-19T13:08:42 | Pavel**
Добрый день. 
Изучил документации Запрет2 и ZeroBlock. Поставил и запустил обе службы по умолчанию - ничео не меняя в инструкциях по сути. Есть странности - заблокированные ресурсы открываются по разному на разных устройствах вроде компьютер/телефон/телевизор (с отключенными ВПН). И есть две ошибки: 

1) Awg10 будто не показывает размер задержки что может наверное означать, что с ВПН что-то не так? По тестам в терминале вроде работает.
2) ⚠ NFTables проверки — Обнаружены проблемы - ⚠ Другая маркировка youtubeUnblock. Кто-нибудь знает, как это поправить? Если это надо поправлять

И есть два вопроса для меня:

1) Каким образом я могу создать на роутере архитектуру, при которой все ресурсы кроме ru шли бы с иностранного IP под впн, чтобы не гадать что там откроется в списках. А россиские сайты и приложения шли напрямую байпасом?
2) Как поставить на роутер работающий ВПН - как self hosted или условный Blank?

Отправьте меня к какому-то гайду или мануалу пожалуйста ))

---

**2026-04-19T14:03:08 | Анатолий Шарков**
Подскажите, пожалуйста:

Планирую использовать внешний прокси (VLESS) через Podkop (секции / ZeroBlock).

Текущая конфигурация:
— RouteRich 24.10.5 (RR-3.9.0)
— Podkop v0.7.10 (помечен как устаревший)
— sing-box 1.12.17

Вопросы:

1. Достаточно ли этой версии Podkop для работы с VLESS?
2. Есть ли рекомендуемая версия Podkop и ПРОШИВКИ под такую схему?
3. Есть ли критичные изменения в новых версиях для секций / outbound?

И как лучше сделать — сначала обновиться, а потом настраивать, или можно сначала всё настроить на текущей версии?

---

**2026-04-19T15:22:34 | Routerich**
я не представляю что вы там обновили. rutracker.cc теперь есть в списке
cat /tmp/zeroblock/rulesets/torrent_domains.json |grep rutracker.cc
{"1337x.to":["1337x.to","www.1337x.to"],"bitru.org":["bitru.org"],"booktracker.org":["booktracker.org","bt.booktracker.work","www.booktracker.org"],"filmitorrent.net":["filmitorrent.net","www.filmitorrent.net"],"freetp.org":["freetp.org"],"kinozal.tv":["kinozal.me","kinozal.tv","wstracker.online"],"nnmclub.to":["nnmclub.to","nnmstatic.win","www.nnmclub.to","www.nnmstatic.win"],"opentrackr.org":["opentrackr.org"],"rustorka.com":["open.stealth.si","rustorka.com","tr.ysagin.top","tr3.ysagin.top","tracker.torrent.eu.org","wstracker.online","www.rustorka.com"],"rutor.info":["rutor.info","rutor.is","rutor.org","www.rutor.info","www.rutor.is","www.rutor.org"],"rutracker.org":["bt.t-ru.org","bt2.t-ru.org","bt3.t-ru.org","bt4.t-ru.org","rutracker.cc","rutracker.net","rutracker.org","rutracker.ru","rutracker.wiki","rutrk.org","static.rutracker.cc","t-ru.org","www.rutracker.org","www.rutracker.ru","www.rutracker.wiki","www.rutrk.org","www.t-ru.org"],"thepiratebay.org":["thepiratebay.org","torrindex.net","www.thepiratebay.org","www.torrindex.net"],"torrent.by":["torrent.by","www.torrent.by"]}

---

**2026-04-19T16:21:49 | Pavel**
@routerich  добрый день! У меня ZeroBlock, интерфейс AmneziaWG (awg10) работает. Нужно: весь трафик пустить через awg10 кроме кроме российских (.ru, .su, .рф, .by, .kz и конкретные домены вроде gosuslugi.ru). Российские должны идти напрямую (WAN).

Проблемы/Вопросы:

В ZeroBlock нет глобальных исключений?

Секция типа Proxy с пустым URL не сохраняется (поле обязательно).

Секция типа VPN с исключёнными доменами (excluded domains) — работает ли это как «direct» для этих доменов?

Могу я настроить для этой задачи одну секцию Catch-all c исключениями зоны ру и приложений? Есть у вас списки geoIP или списки для исключений по РФ?

---

**2026-04-19T16:28:53 | Алексей**
Добрый день. Наблюдаю проблему подключения к WebEx. Установлен zeroblock + zapret2. В какую сторону смотреть?

---

**2026-04-19T16:52:45 | Pavel**
Можете подсказать пожалуйста как пдключить платный ВПН в Zeroblock? Не могу найти нигде

---

**2026-04-19T17:10:06 | Aleksei**
Народ, подскажите пожалуйста - в zeroblock вставил свою ссылку vless, поставил категорию "мессенджеры" - работает 20 минут, потом телега отваливается, перезапускаю зерблок - работает снова определенное время

---

**2026-04-19T17:20:19 | Артём**
Народ, подскажите пожалуйста почему-то на моём платном впн меня сегодня больше не конектит к серверам рб. Что делать чтобы оно снова всё заработало? Если что у меня обход идёт в zeroblock через сервер прокси по подписке.

---

**2026-04-19T17:21:31 | Артём**
Если что пинг на серверах в панели управления zeroblock показывает 70-90 но в самом роблоксе не конектит к серверам.

---

**2026-04-19T18:37:57 | Anna Bagler**
Что пустит, отключение запрет2 или зироблок? Список мессенджеров уберите, раз у вас руками прописано. YouTube в запрет2 и zeroblock.

---

**2026-04-19T18:54:07 | Routerich**
А у вас он в Zeroblock выбран или в zapret2?

---

**2026-04-19T18:57:07 | Routerich**
Ну если он в Zeroblock то надо

---

**2026-04-19T19:00:46 | Anna Bagler**
YouTube убрать из zeroblock, запрет2 включить.

---

**2026-04-19T19:04:08 | Дмитрий Шаповалов**
Помогите побороть утечку ру ip для зарубежных сервисов. Я попробовал заменить скрипт5 на zeroblock + vless, но проблема осталась

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

**2026-04-19T19:12:00 | Кирилл Коробов**
Последняя строка не влезла. Там: 0 5 * * * /usr/bin/zeroblock update_lists >/dev/null 2>&1

---

**2026-04-19T19:25:36 | Anna Bagler**
Тогда убрать список YouTube из zeroblock. В двух местах его быть не должно. Добавить исключения в zapret2. Проверить.

---

**2026-04-19T19:26:31 | Maxim =)))**
Из ZeroBlock уже исключил

---

**2026-04-19T19:35:34 | Кирилл Коробов**
А вот это в настройках ZeroBlock. Всё правильно?

---

**2026-04-19T19:38:03 | Mike Rizhoff**
Если интересно, то поборол свою проблему с невозможностью что-либо установить на роутер из репозиториев (в моем случае zeroblock). Проблема в том, что провайдер мобильного интернета, в моем случае Билайн, блокирует доступ к репозиториям. Хорошо бы поддержке продукта как-то подумать над этим вопросом. Я свою проблему решил, когда завернул весь трафик с роутерича на свой городской роутер, в котором проблем блокировки репо нет. После этого все на роутерич скачалось, установилось и прекрасно работает. Спасибо всем, кто пытался помочь, но проблема оказалась банальной (поддерка ее озвучивала), но она нерешаема, если человек приобрел сабж и никакого другого роутера, через который можно пробросить сетку до репозиториев, у него нет.

---

**2026-04-19T20:00:11 | Роман**
Zeroblock.

---

**2026-04-19T20:00:35 | Anna Bagler**
Галочку в настройках zeroblock поставить на yacd.

---

**2026-04-19T20:43:52 | Артём**
Оказывается проблема была в моём платном VPN, у них на серверах нагрузка огромная. Может кто-то посоветовать хороший впн для стабильной работы zeroblock ну и со скоростью 200-250 Мбит в секунду или выше?

---

**2026-04-19T21:11:17 | Anna Bagler**
https://t.me/routerich/394153/625333 потом привязать интерфейс к секции подкопа. Если не хотите сбрасывать и ставить zeroblock.

---

**2026-04-19T22:08:13 | Gomer Simpson**
Вам в тему ZeroBlock. Или Интернет без границ.

---

**2026-04-19T22:10:34 | Dmitry**
Поставил сегодня товарищу РР, засунул внутрь AWG2 Premium + Zeroblock по мануалу. Все завелось, а теперь товарищ пишет.
————————————————————-
в какой-то момент пропадает интернет
подключаю старый кинетик — все работает
возвращаю РР — снова есть интернет
через пару часов пропадает
————————————————————-
Пропадает доступ в интернет целиком как по спискам, так и внутренний. Бывает у кого-то такое? Куда смотреть? Логов пока нет, обещал прислать в следующий раз.

---

**2026-04-19T22:43:41 | Артур**
Подскажите, как добавить свой домен в список zeroblock?

---

**2026-04-19T22:45:10 | Роман**
Zeroblock для прокси, запреты для ютуба/дискорда.

---

**2026-04-19T22:54:00 | Вячеслав**
Здравствуйте. На роутере через zeroblock работают выбранные списки, всё ок. А на телефоне сервисы яндекса стали писать вот так) куда-то стучится он при подключении, кто нибудь сталкивался? Как решили?

---

**2026-04-19T22:56:14 | Олег **
Привет всем. Открываю 2ip.ru 2ip.io вот эти сайты результат на них одинаковый ip  и местоположение РФ так и должно быть? стоит zeroblock и zapren2 устанавливал по мануалу автонастройка

---

**2026-04-19T23:08:35 | Aleksey**
В настройках zeroblock

---

**2026-04-19T23:18:11 | Максим Солдатов**
https://4pda.to/forum/index.php?showtopic=1080524&view=findpost&p=143016113

дубль текста с темы 4pda:
Сижу на openwrt со времён netgear-wndr3700, когда брал роутерич, сразу планировал уйти на ванильный openwrt, т.к. много других устройств с ним и хотел, чтобы мой howto по настройке всех роутеров asus rt58u, cudy tr3000v1, ... был везде одинаковый.
По факту посмотрел, как оно .... так и сижу на форке openwrt от роутеречей, имена пакетов одинаковые, ну и что, что часть уже предустановлено, мой howto ничем не сломался.
Понятное дело, что специфику типа zeroblock не использую, т.к. его нет в ванили для др роутеров, но мне пока хватает возможностей чистого openwrt, который весь есть и в этом роутере.
Хз что тут люди не годуют, а порой пишут такую дичь, что кажется целенаправленно гнобят на ровном месте, все очень даже отлично работает, тем кто ищет возможности openwrt точно зайдет... остальным по способностям, чем ближе к it, тем легче

---

**2026-04-20T06:48:30 | Routerich**
Здравствуйте.
а если наоборот стопнуть zeroblock, zapret2 и посмотреть?

---

**2026-04-20T07:18:42 | Routerich**
В настройках Zeroblock
Clash API
Включить YACD галочку поставить

---

**2026-04-20T07:37:42 | Routerich**
А если cdn убрать из списков? И в настройках отключить cdn если включали
Если не поможет стопнуть zeroblock, Zapret2 и посмотреть, потом по очереди включать и наблюдать

---

**2026-04-20T08:12:49 | Anna Bagler**
Если прямую ccылку vless сможете вытащить и подкоп не будет на нее ругаться. Подписки поддерживает zeroblock. Но его надо ставить на чистый роутер.

---

**2026-04-20T08:30:47 | Данила Ступин**
Здравствуйте! Может кто нашёл решение? Сегодня перестал работать кинопоиск (вчера всё было нормально). Я решил проверить список доменов к которым обращается приложение и не нашёл ничего подозрительного, этих доменов нет в zeroblock. При этом если отключить zeroblock, то всё начинает работать. Как это вообще возможно?

---

**2026-04-20T08:30:50 | Routerich**
Zeroblock->секции маршрутизации->вводим имя->добавить секцию->Тип подключения->сервер прокси->тип конфигурации->url прокси->вводим ссылку

---

**2026-04-20T08:34:03 | Евгений Макаренко**
Кто знает как исправить данную ошибку. Она возникает когда я устанавливаю ZeroBlock. Почему незнаю.

---

**2026-04-20T08:39:06 | Евгений Макаренко**
Сброс роутрера в заводские настройки. И после установки ZeroBlock. Сразу ошибка.

---

**2026-04-20T09:41:59 | GREY**
Zeroblock - Секции маршрутизации - списки - исключения.
Списки уже исправили, можете просто принудительно обновить их из Zeroblock - Диагностика
Больше доменов в канале Zeroblock

---

**2026-04-20T09:42:28 | Константин**
Ткните пожалуйста где инструкция как поставить amneziawg когда на роутере zeroblock и zapret2

---

**2026-04-20T09:47:10 | Vadim**
Zeroblock+zapret2+vless

---

**2026-04-20T11:12:44 | Artem Kirillov**
Добрый день. Есть ли какая-то актуальная инструкция что сейчас нужно сделать с роутером, чтобы работал ChatGPT и т.п.? Я просто смотрю разные есть инструкции, и вопрос сегодня задавал в Интернет без границ. Но пока не могу понять какой способ верный и рабочеспособный. Сейчас сбросил настройки на роутере и думаю воспользоваться инструкцией, где amnezia + zeroblock. Но может есть что-то в чатах здесь более актуальное?

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

**2026-04-20T12:10:03 | Routerich**
Здравствуйте.
новую секцию создайте в Zeroblock с типом сервер прокси и выбрать тип конфигурации url прокси.

---

**2026-04-20T12:41:09 | Вячеслав**
Добрый день. После сброса роутера и восстановления настроек из резервной копии в службах отсутствует zeroblock. Так и должно быть?

---

**2026-04-20T12:55:08 | Dmitry**
Кто-то сможет подсказать, возможно ли одновременно с конфигом AWG подключить к Zeroblock еще один конфиг к другому серверу на обычном WG? Нужно поднимать еще один интерфейс? Какой?

---

**2026-04-20T12:56:43 | Proff-comp**
Добрых дней. Подскажите пожалуйста, хочу попробовать zeroblock, у меня стоит podkop, достаточно будет его просто удалить например через менеджер пакетов и поставить, или все же на чистый роутер нужно, и я как понял с vless он работает. Поправьте если ошибаюсь.

---

**2026-04-20T13:33:50 | Анатолий Шарков**
Добрый день.
Подскажите, какой сейчас рекомендуемый и рабочий вариант обхода блокировок?

Использовал скрипт 5 — часть сайтов перестала открываться.

Сейчас вижу варианты Podkop / Zapret / ZeroBlock — какой из них актуальный?

И нужно ли при переходе на ZeroBlock удалять Podkop (или они могут работать параллельно)?

---

**2026-04-20T13:36:48 | Павел**
Здравствуйте. Подскажите пожалуйста. Можно ли установить zeroblock на openwrt? Дома routerich, на даче beeline smartbox giga с установленным подкопом на данный момент. Стоит пробовать или он там в принципе не заведётся? И второй вопрос, ещё не устанавливал zeroblock, там конфиг vless интуитивно понятно можно будет подставить? В инструкции вроде про это не написано, только что поддерживается.

---

**2026-04-20T13:36:51 | Routerich**
ZeroBlock на чистую ставить, с предварительным сбросом роутера.
ставьте ZB.

---

**2026-04-20T14:06:05 | Лев**
Ребята привет, прошу помочь. Когда включен вайфай, адгуард перестает блокировать рекламу в хроме. На мобильном все хорошо. 
Обход посредством zeroblock, в обоих секциях исключил телефон.
Что сделать чтобы адгуард работал при подключении через вай-фай?

---

**2026-04-20T14:22:09 | Kiss_My_Axe**
Сложно. При подключении к РР адгард перестаёт быть главным ДНС в системе.
Все запросы уходят в РР. Следовательно по доменам адгард резать перестаёт.
Самое простое - включить адгард ДНС в ZeroBlock, та же резалка по доменам-адресам будет. С проблемами.
А так фиг знает... Выкинуть приложуху адгарда из системы, ограничиться плагинами в браузере, разве что.

---

**2026-04-20T15:18:15 | Anna Bagler**
Zeroblock на чистый роутер поставили?

---

**2026-04-20T15:18:25 | Victor**
Сейчас стоят zeroblock и zapret2, все работает.

---

**2026-04-20T15:29:23 | Anna Bagler**
https://t.me/routerich/29/636875 - запустите код из этого сообщения и покажите скриншотами результаты, чтоб посмотреть, что работает и как.
Для zeroblock надо сбрасывать роутер и настраивать с нуля. Справитесь?

---

**2026-04-20T15:35:39 | Anna Bagler**
@asd334521 если со сбросом перейдете на zeroblock, то такой транспорт сможете использовать.

---

**2026-04-20T15:40:26 | Влад**
zeroblock работает как подкоп?

---

**2026-04-20T15:51:12 | Евгений Макаренко**
Остановил ZeroBlock.

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

**2026-04-20T16:38:37 | Влад**
в мануале по zeroblock нету команды для его установки?

---

**2026-04-20T16:39:57 | Routerich**
opkg update && opkg install luci-app-zeroblock

---

**2026-04-20T17:32:40 | Anna Bagler**
Запрет2 остановить и отключить, в секцию со своим vless в zeroblock добавить.

---

**2026-04-20T17:34:42 | Anna Bagler**
По интерфейсу zeroblock походите. Список в секции отметьте. Посмотрите.

---

**2026-04-20T18:41:19 | Андрей**
Комрады, подкиньте идей, куда копать. В zeroblock есть секция, которая отправляет трафик до yotube в openconnect интерфейс, speedtest тоже идёт через этот же интерфейс. 
Делаю тест speedtest - 150мбит. Но вот проблема - ютуб тормозит (видео не успевают прогружаться, превьюшки загрудаются тоже прям неспеша очень). Смотрю через yacd - трафик уходит как и должен в openconnect
Тут можно сделать вывод, что это канал у vpn сервера херовый, но подключаю на комп этот же сервак через openconnect - ютуб летает....
В zapret2 стратегия для ютуба отключена

---

**2026-04-20T18:48:40 | Anna Bagler**
Удалите zeroblock и поставьте заново https://t.me/routerich/4/636320
Домены руками не пишите, выбирайте списки.

---

**2026-04-20T19:00:00 | Евгений**
Я с zeroblock вообще не знаком,сюда не могу поставить тот же подкоп?

---

**2026-04-20T19:24:53 | Routerich**
Удалите sing-box
Потом ставьте zeroblock

---

**2026-04-20T19:41:10 | 𝔸𝓵𝖙𝕖𝓻**
Добрый день уважаемые, подскажите правильно ли мыслю , хочу заворачивать всякие плохие рекламные домены чёрез zeroblock используя листы с гитхаба, можете проинформировать как )
Upd. Просто из логики если буду использовать решения  вроде адблок при завороте траффика оно станет неэффективно?

---

**2026-04-20T19:52:23 | Routerich**
У вас ZeroBlock?

---

**2026-04-20T19:52:38 | Vit**
Спасибо! Не так давно перешёл с podkop на zeroblock + zapret2. Часть трафика пустил через свой awg. Работает всё что нужно. Ещё раз спасибо! Ещё бы всё это на х86 поднять, вот был бы комбайн.

---

**2026-04-20T19:54:59 | The Wisest**
Здравствуйте!
С чем может быть связана не работа Майнкрафта?
С запретом или Zeroblock?

---

**2026-04-20T19:57:31 | Николай Каменных**
Приветствую!
Как настроить ZeroBlock чтобы обойти эту блокировку приложений Яндекс?
Пустить в обход по доменам?

---

**2026-04-20T20:08:33 | Anna Bagler**
Бесплатные варианты более не работают. Свой vless или ещё что в zeroblock/podkop.

---

**2026-04-20T20:09:33 | The Wisest**
Так Zeroblock это же VPN на роутере, или нет?

---

**2026-04-20T20:22:41 | Routerich**
Здравствуйте.
В zeroblock создавайте новую секцию, в секциях маршрутизации, затем выбирайте тип прокси сервер, затем URL подключения и туда вставляете свой ключ и выбираете нужные вам списки

---

**2026-04-20T20:36:44 | MichaelN_29**
Доброго всем времени суток) Ребят подскажите как направить трафик telemt в zeroblock

---

**2026-04-20T20:55:37 | D B**
Может есть какая-то инструкция, как правильно обновиться... А то я пока никак не могу понять - что брать и где, для корректного и правильного обновления, что бы потом задействовать zeroblock. Разобраться с ним хотелось бы...

---

**2026-04-20T21:32:42 | Anna Bagler**
Вам бы обновить и прошивку и podkop. А лучше zeroblock после прошивки.

---

**2026-04-20T22:55:34 | Timur**
скажите пожалуйста если пакеты эти то нет zeroblock
src/gz openwrt_core https://downloads.openwrt.org/releases/24.10.5/targets/mediatek/filogic/packages
src/gz openwrt_base https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/base
src/gz openwrt_luci https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/luci
src/gz openwrt_packages https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/packages
src/gz openwrt_routing https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/routing
src/gz openwrt_telephony https://downloads.openwrt.org/releases/24.10.5/packages/aarch64_cortex-a53/telephony

---

**2026-04-20T23:14:37 | Timur**
2. Откройте браузер в режиме инкогнито/приватном режиме

    Chrome/Edge: Ctrl+Shift+N

    Firefox: Ctrl+Shift+P

    Safari: Cmd+Shift+N

3. Зайдите в веб-интерфейс роутера

    Обычный адрес: http://192.168.1.1 или http://192.168.0.1

    Логин/пароль: ваши учётные данные (если не меняли — root / пустой или admin / admin)

4. Проверьте работу LuCI

    Перейдите в раздел System → Software (Система → Программное обеспечение)

    Нажмите Update lists... (Обновить списки)

    Посмотрите, появилась ли ошибка JSON.parse

5. Если ошибка осталась — обновите списки пакетов через SSH
bash

opkg update
opkg list-upgradable

6. Очистите кэш LuCI (если инкогнито не помогло)
bash

rm -rf /tmp/luci-*
/etc/init.d/uhttpd restart

Что должно произойти

Если репозиторий packages.routerich.ru заработал:

    opkg update завершится без ошибок

    В веб-интерфейсе исчезнет ошибка JSON.parse

    Вы сможете установить zeroblock

Если репозиторий всё ещё недоступен (ошибка 503):

    В консоли будут ошибки wget returned 4 или 404

    В LuCI будет та же ошибка JSON.parse

Если ошибка сохранится

Временно отключите проблемные репозитории Routerich:
bash

mv /etc/opkg/customfeeds.conf /etc/opkg/customfeeds.conf.disabled
opkg update

После того как сервер packages.routerich.ru восстановится, верните конфиг:
bash

mv /etc/opkg/customfeeds.conf.disabled /etc/opkg/customfeeds.conf
opkg update

Выполните сейчас: перезагрузите роутер и откройте LuCI в режиме инкогнито. Напишите, что получилось — заработало или нет?

---

**2026-04-20T23:18:46 | Docvspb 🇷🇺**
Камнями не кидайте, я на разбираюсь в деталях. Но Deepseek мне так написал о причинах:


Telegram — это сложная система, которая для разных задач использует разные серверы. Для медиафайлов в больших группах и каналах он часто обращается к своей CDN (сети доставки контента), IP-адреса которой могут меняться или отличаться от основных серверов мессенджера. 

Проблема в том, что ваш Zeroblock в режиме FakeIP пытается применить правила обхода (например, отправить трафик в VPN-туннель awg10) ко всем этим серверам. Но для конкретного CDN-сервера, который использует проблемная группа, этот маршрут по каким-то причинам не срабатывает. Возможно, этот сервер блокирует подключение из вашего VPN, или же пакеты теряются из-за особенностей работы туннеля.

Приложение Telegram на iPhone, в отличие от веб-версии, может быть более чувствительно к таким сбоям при загрузке медиа, что и приводит к ошибке.

---

**2026-04-20T23:30:55 | Владислав**
Добрый вечер,  подскажете пожалуйста, в zeroblock opera не пингуется, она крашнулась или появились новые настройки?

---

**2026-04-21T00:00:10 | Timur**
все заработало вроде тьфу тьфу тьфу , свой ключ можно поставить в секции? zeroblock нужно останавливать во время вписывания ключа в секцию?

---

**2026-04-21T00:00:26 | Anna Bagler**
Сбрасывайте настройки роутера и только zeroblock ставьте. И подкоп, и зироблок одновременно нельзя. Потом код диагностики ещё раз.

---

**2026-04-21T01:13:13 | Роман**
Для игры Epic Seven нужно добавить эти домены в список прользовательских доменов zeroblock/podkop. Внимание используется cloudfront!
playstove.com
onstove.com
singular.net
81plug.com
cloudfront.net
facebook.com
#games

---

