import paramiko
import time

def setup_zapret(host, user, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, username=user, password=password, timeout=15)
        print(f"Connected to {host}")

        # Check if zapret is installed
        stdin, stdout, stderr = ssh.exec_command('ls /opt/zapret/config')
        if stdout.channel.recv_exit_status() != 0:
            print("Zapret not found in /opt/zapret. Attempting opkg install...")
            ssh.exec_command('opkg update && opkg install zapret')
            time.sleep(10)
        
        # New Config Content with Fixed Mark
        config_content = r"""FWTYPE=nftables
SET_MAXELEM=524288
IPSET_OPT="hashsize 262144 maxelem 524288"
DISABLE_IPV4=0
DISABLE_IPV6=1
MODE_FILTER=none
NFQWS_ENABLE=1

# TUNED FOR YOUTUBE (No conflict with ZeroBlock)
# We use 0x2 as the mark for Zapret
DESYNC_MARK=0x2
DESYNC_MARK_POSTNAT=0x4

NFQWS_OPT="
--filter-tcp=80 --dpi-desync=fake,multisplit --dpi-desync-split-pos=method+2 --dpi-desync-fooling=md5sig --new
--filter-tcp=443 --dpi-desync=disorder --dpi-desync-split-pos=1,midsld --dpi-desync-fooling=md5sig,badsum --dpi-desync-repeats=6 --dpi-desync-autottl --new
--filter-udp=443 --dpi-desync=fake --dpi-desync-repeats=10 --dpi-desync-fooling=md5sig
"

OPENWRT_LAN="lan"
NFQWS="/opt/zapret/nfq/nfqws"
TPWS="/opt/zapret/tpws/tpws"
"""
        # Write the configuration
        print("Applying fixed configuration (mark 0x2)...")
        ssh.exec_command(f"cat <<'EOF' > /opt/zapret/config\n{config_content}\nEOF")
        
        # Restart service
        print("Restarting zapret service...")
        ssh.exec_command('/etc/init.d/zapret restart')
        time.sleep(3)
        
        # Final check
        stdin, stdout, stderr = ssh.exec_command('ps | grep nfqws | grep -v grep')
        if stdout.read():
            print("SUCCESS: Zapret is running with fixed config.")
        else:
            print("WARNING: Zapret service started but nfqws process not found. Check /var/log/messages")

        ssh.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    setup_zapret("192.168.3.1", "root", "mewpas7835")
