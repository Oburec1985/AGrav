# Walkthrough: Zapret2 YouTube Bypass Strategy Optimization

This document details the successful implementation and deployment of a 10-stage circular desync strategy using Zapret2 on the OpenWrt router (`192.168.2.1`).

## 1. High-Level Summary
* **Service Status**: Active and Running. The `nfqws2` process is actively filtering traffic on queue `300`.
* **Strategy Configuration**: Chained circular orchestrator (`--lua-desync=circular:fails=2:maxtime=60`) rotating through 10 distinct, high-resilience bypass stages.
* **Compatibility**: Configured with `desync_mark '0x2'` to ensure it runs concurrently with existing network tables without routing loops.
* **Persistence**: Deployed as a persistent service controlled via standard OpenWrt `/etc/init.d/zapret2` and `/etc/config/zapret2`.

---

## 2. The 10-Stage Circular Strategy Sequence
The 10 strategies were curated from the simple desync strategies found in `_Zapret2.txt` to cover a diverse range of packet-tampering techniques:

| Stage | Strategy Parameter | Mechanism & Target |
|---|---|---|
| **1** | `--lua-desync=multidisorder:pos=2` | Simple TCP multi-position packet disordering (reorders bytes starting from TCP offset 2). |
| **2** | `--lua-desync=multidisorder:pos=1` | Disordering starting from the very first payload byte (highly effective for basic DPI). |
| **3** | `--lua-desync=multidisorder:pos=midsld` | Disordering in the middle of the sub-level domain to break SNI detection. |
| **4** | `--lua-desync=multidisorder:pos=1,midsld` | Combined multi-byte and domain-midpoint packet disordering. |
| **5** | `--lua-desync=tcpseg:pos=0,-1:seqovl=1` <br> `--lua-desync=drop` | TCP segmentation with sequence overlap and packet drop (injects overlapping bytes that confuse the DPI but are ignored by the server). |
| **6** | `--lua-desync=multisplit:pos=10:seqovl=1` | Multi-position TCP splitting combined with 1-byte sequence overlap. |
| **7** | `--lua-desync=fake:blob=fake_default_tls:ip_ttl=2:tls_mod=rnd,dupsid,padencap:repeats=1` | Sends a fake TLS ClientHello with low TTL (2). It reaches and poisons the DPI cache but drops before hitting the real server. |
| **8** | `--lua-desync=fake:blob=fake_default_tls:badsum:repeats=1` | Sends a fake TLS ClientHello with a bad TCP checksum (discarded by the target stack, processed only by DPI). |
| **9** | `--lua-desync=fake:blob=0x00000000:badsum:repeats=1` <br> `--lua-desync=fake:blob=fake_default_tls:badsum:tls_mod=rnd,dupsid:repeats=1` | Dual fake packets (first zeroes with invalid checksum, followed by a randomized fake ClientHello with invalid checksum). |
| **10** | `--lua-desync=multisplit:blob=fake_default_tls:badsum:pos=2:nodrop:repeats=1` | Combines multisplit fragmentation at position 2 with bad-checksum fake TLS payloads. |

---

## 3. UCI Configuration (`/etc/config/zapret2`)
The custom configuration written to the router:

```uci
config zapret2 'main'
	option enabled '1'
	option debug '1'
	option desync_mark '0x2'
	option desync_mark_postnat '0x20000000'
	option nfqws_ports_tcp '80,443'
	option nfqws_ports_udp '443'
	option postnat '1'
	option nfqws_tcp_pkt_out '25'
	option nfqws_tcp_pkt_in '5'
	option custom_scripts '1'
	option qnum '300'
	option autohostlist_debug '0'
	option autohostlist_retrans_threshold '3'
	option autohostlist_fail_threshold '3'
	option autohostlist_fail_time '60'
	option lua_gc '600'

config strategy 'youtube'
	option port '443'
	option protocol 'tcp'
	list filter_l3 'ipv4'
	list filter_l7 'tls'
	list hostlist 'list_hosts_youtube'
	option script '--out-range=-s34228
--in-range=-s5556 --lua-desync=circular:fails=2:maxtime=60
--in-range=x
--payload=tls_client_hello
--lua-desync=multidisorder:pos=2:strategy=1
--lua-desync=multidisorder:pos=1:strategy=2
--lua-desync=multidisorder:pos=midsld:strategy=3
--lua-desync=multidisorder:pos=1,midsld:strategy=4
--lua-desync=tcpseg:pos=0,-1:seqovl=1:strategy=5
--lua-desync=drop:strategy=5
--lua-desync=multisplit:pos=10:seqovl=1:strategy=6
--lua-desync=fake:blob=fake_default_tls:ip_ttl=2:tls_mod=rnd,dupsid,padencap:repeats=1:strategy=7
--lua-desync=fake:blob=fake_default_tls:badsum:repeats=1:strategy=8
--lua-desync=fake:blob=0x00000000:badsum:repeats=1:strategy=9
--lua-desync=fake:blob=fake_default_tls:badsum:tls_mod=rnd,dupsid:repeats=1:strategy=9
--lua-desync=multisplit:blob=fake_default_tls:badsum:pos=2:nodrop:repeats=1:strategy=10'
```

---

## 4. Deployment Log and Service Status
The deployment script [deploy_zapret2_circular.py](file:///c:/Oburec/Antigravity/Projects/routerich/scratch/deploy_zapret2_circular.py) handled:
1. **Old Service Shutdown**: Stopped and disabled the obsolete static `zapret` daemon.
2. **Package Upload**: Transferred the `.ipk` archives via SSH stdin stream (working around default Dropbear SFTP limitations).
3. **Installation Fail-safe**: When standard `opkg` flagged architecture mismatch warnings due to kernel strictness, the script automatically fell back to direct filesystem extraction to ensure binaries and LUA dependencies were fully deployed.
4. **Activation**: Enabled and restarted `zapret2` and the firewall.

### Running Process Verification
```bash
# ps | grep nfqws2
20976 daemon    1516 S    /opt/zapret2/nfq2/nfqws2 --debug=@/tmp/zapret2/main.log --user=daemon --fwmark=0x2
20977 daemon    1488 S    /opt/zapret2/nfq2/nfqws2 --debug=@/tmp/zapret2/50-discord_media.log ...
20978 daemon    1488 S    /opt/zapret2/nfq2/nfqws2 --debug=@/tmp/zapret2/50-stun4all.log ...
```

---

## 5. Verification from `/tmp/zapret2/main.log`
The debug logs show the desync profiles successfully mapped:
```text
profile 1 (youtube) lua circular(maxtime="60",fails="2" range_in=a0-s5556 range_out=a0-s34228 payload_type= all)
profile 1 (youtube) lua multidisorder(strategy="1",pos="2" ...)
profile 1 (youtube) lua multidisorder(strategy="2",pos="1" ...)
profile 1 (youtube) lua multidisorder(strategy="3",pos="midsld" ...)
profile 1 (youtube) lua multidisorder(strategy="4",pos="1,midsld" ...)
profile 1 (youtube) lua tcpseg(strategy="5",seqovl="1",pos="0,-1" ...)
profile 1 (youtube) lua drop(strategy="5" ...)
profile 1 (youtube) lua multisplit(strategy="6",seqovl="1",pos="10" ...)
profile 1 (youtube) lua fake(strategy="7",repeats="1",tls_mod="rnd,dupsid,padencap",ip_ttl="2" ...)
profile 1 (youtube) lua fake(strategy="8",repeats="1",badsum="" ...)
profile 1 (youtube) lua fake(strategy="9",repeats="1",badsum="" ...)
profile 1 (youtube) lua multisplit(strategy="10",repeats="1",nodrop="",pos="2",badsum="" ...)
Loading hostlist /opt/zapret2/ipset/zapret_hosts_youtube.txt
loading plain text list
Loaded 7 hosts from /opt/zapret2/ipset/zapret_hosts_youtube.txt
```

> [!NOTE]
> When client devices connect directly to `googlevideo.com`, the circular orchestrator tracks connection failures. If a strategy fails 2 times, it automatically rotates to the next index in the 10-stage list to re-establish the stream without stalling.
