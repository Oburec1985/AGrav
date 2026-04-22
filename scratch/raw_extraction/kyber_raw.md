# Raw Extraction: kyber

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

