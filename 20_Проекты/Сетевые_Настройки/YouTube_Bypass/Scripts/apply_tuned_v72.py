import paramiko
import sys
import time

def apply_tuned_v72(host, user, password):
    print(f"Connecting to {host}...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, username=user, password=password, timeout=10)
        
        # Correct variable names for zapret v72
        config_content = r"""FWTYPE=nftables
SET_MAXELEM=524288
IPSET_OPT="hashsize 262144 maxelem 524288"

# Enable IPv4, disable IPv6 to prevent leaks through v6
DISABLE_IPV4=0
DISABLE_IPV6=1

# Mode and Filter
MODE_FILTER=none
NFQWS_ENABLE=1

# nfqws options tuned for Windows 11
# We use disorder and multiple fooling methods
NFQWS_OPT="
--filter-tcp=80 --dpi-desync=fake,multisplit --dpi-desync-split-pos=method+2 --dpi-desync-fooling=md5sig --new
--filter-tcp=443 --dpi-desync=disorder --dpi-desync-split-pos=1,midsld --dpi-desync-fooling=md5sig,badsum --dpi-desync-repeats=6 --dpi-desync-autottl --new
--filter-udp=443 --dpi-desync=fake --dpi-desync-repeats=10 --dpi-desync-fooling=md5sig
"

# OpenWrt specific
OPENWRT_LAN="lan"
DESYNC_MARK=0x40000000
DESYNC_MARK_POSTNAT=0x20000000

# Binary paths
NFQWS="/opt/zapret/nfq/nfqws"
TPWS="/opt/zapret/tpws/tpws"
"""
        # Write config
        print("Writing tuned config (v72 style)...")
        stdin, stdout, stderr = ssh.exec_command(f"cat <<'EOF' > /opt/zapret/config\n{config_content}\nEOF")
        stdout.read(); stderr.read()
        
        # Fully restart: kill all, stop, start
        print("Force restarting zapret...")
        ssh.exec_command('killall nfqws 2>/dev/null; /etc/init.d/zapret stop; sleep 2; nft delete table inet zapret 2>/dev/null; /etc/init.d/zapret start')
        time.sleep(5)
        
        # Check processes
        stdin, stdout, stderr = ssh.exec_command('ps | grep nfqws | grep -v grep')
        ps_out = stdout.read().decode().strip()
        if ps_out:
            print("SUCCESS: Tuned nfqws is running with new config!")
            print(ps_out)
        else:
            print("FAILURE: nfqws is not running. Checking init script errors...")
            stdin, stdout, stderr = ssh.exec_command('/etc/init.d/zapret start_daemons')
            print(stdout.read().decode())
            print(stderr.read().decode())
            
        ssh.close()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    apply_tuned_v72("192.168.2.2", "root", "mewpas7835")
