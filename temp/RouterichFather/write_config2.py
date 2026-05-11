import subprocess
import base64

config = """# zapret2 configuration

DESYNC_MARK=0x40000000
DESYNC_MARK_POSTNAT=0x20000000

NFQWS2_ENABLE=1
NFQWS2_PORTS_TCP=443
NFQWS2_PORTS_UDP=443
NFQWS2_TCP_PKT_OUT=25
NFQWS2_TCP_PKT_IN=5
NFQWS2_UDP_PKT_OUT=5
NFQWS2_UDP_PKT_IN=3

# Optimized for YouTube
NFQWS2_OPT="--lua-gc=600 --blob=blob_tls_clienthello_www_google_com:@/opt/zapret2/files/fake/tls_clienthello_www_google_com.bin --name=youtube --filter-tcp=443 --filter-l7=tls --hostlist=/opt/zapret2/ipset/zapret_hosts_youtube.txt --lua-desync=multisplit:pos=1,sniext+1:seqovl=1 --new --filter-udp=443 --filter-l7=quic --hostlist=/opt/zapret2/ipset/zapret_hosts_youtube.txt --lua-desync=fake:repeats=6"

MODE_FILTER=none
FLOWOFFLOAD=donttouch
INIT_APPLY_FW=1
DISABLE_IPV4=0
DISABLE_IPV6=1
FILTER_TTL_EXPIRED_ICMP=1
DAEMON_LOG_ENABLE=1
DAEMON_LOG_FILE="/tmp/zapret2/<DAEMON_CFGNAME>.log"
"""

b64 = base64.b64encode(config.encode()).decode()
cmd = f"echo {b64} | openssl enc -base64 -d > /opt/zapret2/config"

subprocess.run(['plink', '-pw', 'mewpas7835', 'root@192.168.3.1', '-batch', '-hostkey', 'ssh-ed25519 255 SHA256:S/M0IGXIkS+8jr97SeJ2eoC3MpeQ1+MVz8kakYRV+nI', cmd])
