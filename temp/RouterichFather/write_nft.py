import subprocess
import base64

content = """chain zapret_unified_forward {
    type filter hook forward priority 10; policy accept;
    
    # Global MSS Clamping (1300) for Double NAT compatibility
    tcp flags syn tcp option maxseg size set 1300
    
    # Forward to NFQWS ONLY IF NOT ALREADY PROCESSED BY ZAPRET2 (0x40000000)
    iifname "br-lan" meta mark & 0x40000000 == 0x00000000 tcp dport { 80, 443 } counter queue num 200
    iifname "br-lan" meta mark & 0x40000000 == 0x00000000 udp dport 443 counter queue num 200
}
"""

b64 = base64.b64encode(content.encode()).decode()
cmd = f"echo {b64} | openssl enc -base64 -d > /etc/nftables.d/10-zapret_unified.nft"

subprocess.run(['plink', '-pw', 'mewpas7835', 'root@192.168.3.1', '-batch', '-hostkey', 'ssh-ed25519 255 SHA256:S/M0IGXIkS+8jr97SeJ2eoC3MpeQ1+MVz8kakYRV+nI', cmd])
