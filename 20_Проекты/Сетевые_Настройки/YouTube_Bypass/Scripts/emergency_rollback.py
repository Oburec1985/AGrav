import paramiko
import sys

def emergency_rollback(host, user, password):
    print(f"Connecting to {host} for EMERGENCY ROLLBACK...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, username=user, password=password, timeout=10)
        
        # 1. Restore IPv6
        print("Restoring IPv6 on LAN...")
        ssh.exec_command('uci set network.lan.ipv6=1; uci commit network; /etc/init.d/network restart')
        
        # 2. Delete all zapret/nfqws firewall rules
        print("Wiping all zapret/nfqws firewall rules...")
        ssh.exec_command('rm /etc/nftables.d/*nfqws*.nft /etc/nftables.d/*zapret*.nft 2>/dev/null')
        ssh.exec_command('/etc/init.d/firewall restart')
        
        # 3. Stop and delete custom services
        print("Stopping and disabling custom nfqws services...")
        ssh.exec_command('/etc/init.d/nfqws_final stop; /etc/init.d/nfqws_final disable; rm /etc/init.d/nfqws_final 2>/dev/null')
        ssh.exec_command('/etc/init.d/nfqws_custom stop; /etc/init.d/nfqws_custom disable; rm /etc/init.d/nfqws_custom 2>/dev/null')
        
        # 4. Final Cleanup
        ssh.exec_command('killall -9 nfqws tpws 2>/dev/null')
        
        print("ROLLBACK COMPLETE. Basic internet should be restored.")
        ssh.close()
    except Exception as e:
        print(f"Error during rollback: {e}")
        sys.exit(1)

if __name__ == "__main__":
    emergency_rollback("192.168.2.2", "root", "mewpas7835")
